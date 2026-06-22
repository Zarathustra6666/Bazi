# Wiki Agent Schema

This file is the operating manual for the LLM wiki agent. Every session starts by reading this file. Every operation follows the rules here. You (Codex) own the `wiki/` layer entirely — you create pages, update them, maintain cross-references, and keep everything consistent. The human curates sources, directs analysis, and asks questions.

---

## Purpose

This is a personal second-brain wiki. The domain will evolve over time and is reflected in `wiki/overview.md`. When the overview page does not yet exist, ask the user what the wiki's focus is before doing any ingest.

---

## Directory layout

```
Vault/Bazi/
├── AGENTS.md           ← this file — read every session
├── index.md            ← master catalog of all wiki pages
├── log.md              ← append-only operation log
├── raw/                ← source documents (immutable — never edit these)
│   └── assets/         ← locally downloaded images
└── wiki/
    ├── overview.md     ← high-level synthesis, evolving thesis
    ├── entities/       ← people, orgs, places, projects, products
    ├── concepts/       ← ideas, topics, themes, methods, frameworks
    ├── sources/        ← one summary page per raw source
    └── queries/        ← filed answers to questions worth keeping
```

**Rules:**
- `raw/` is read-only. Never create or modify files there unless explicitly placing a new source.
- `wiki/` is fully LLM-owned. Create, update, delete pages freely here.
- File names: lowercase, hyphen-separated, `.md` extension. Examples: `attention-mechanism.md`, `geoffrey-hinton.md`, `nature-2024-scaling-laws.md`.
- Every wiki page gets YAML frontmatter (see formats below).

---

## Page frontmatter

Every `wiki/` page must have this frontmatter:

```yaml
---
title: Human-readable title
type: entity | concept | source | query | overview
tags: [tag1, tag2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: N
---
```

- `type`: one of the five values above
- `tags`: topic/domain tags to enable Dataview queries in Obsidian
- `sources`: count of raw source documents this page draws on (0 for query pages)

---

## Page formats by type

### entity
Pages for people, organizations, places, projects, or products.

```markdown
# Name

> One-sentence description.

## Overview
2–4 sentences of stable facts.

## Key facts
- Fact 1
- Fact 2

## Connections
- [[Related entity or concept]] — why related
- [[Another page]] — why related

## Source notes
Brief notes on what specific sources say about this entity, with [[source page]] links.
```

### concept
Pages for ideas, topics, themes, methods, or frameworks.

```markdown
# Concept Name

> One-sentence definition.

## What it is
Core explanation, 2–5 sentences.

## Why it matters
Significance or implications.

## Key aspects
- Aspect 1
- Aspect 2

## Connections
- [[Related concept or entity]] — relationship

## Open questions
- Question or tension that hasn't been resolved yet

## Source notes
What the sources say, with [[source page]] links.
```

### source
One page per raw source document.

```markdown
# [Source Title]

> **Type:** article | paper | book | podcast | video | data | other  
> **Author(s):** Name(s)  
> **Date:** YYYY-MM-DD (or best estimate)  
> **File:** `raw/filename.md`

## Summary
3–6 sentence summary of the source.

## Key claims
- Claim 1
- Claim 2

## Data / evidence
Notable data points, statistics, or evidence cited.

## Connections
- [[Entity or concept]] — what this source says about it

## Contradictions
Any claims in this source that conflict with other wiki pages. Format:
- Conflicts with [[page]] on [topic]: this source says X, that page says Y.

## Quotes
> Notable direct quotes worth preserving.
```

### query
A filed answer to a question worth keeping.

```markdown
# [Question as title]

> **Asked:** YYYY-MM-DD  
> **Sources consulted:** [[source1]], [[source2]]

## Answer
The synthesized answer.

## Key supporting points
- Point 1 (from [[source]])
- Point 2 (from [[source]])

## Caveats
Limitations, unknowns, or things that could change the answer.

## Related
- [[Concept or entity]] relevant to this question
```

### overview
One file: `wiki/overview.md`. The top-level synthesis.

```markdown
# Wiki Overview

> **Domain:** [topic/focus]  
> **Started:** YYYY-MM-DD  
> **Sources ingested:** N  
> **Wiki pages:** N

## Current thesis
The evolving main insight or argument this wiki is building toward.

## Key themes
- Theme 1 — brief description
- Theme 2 — brief description

## Open questions
- Question the wiki hasn't answered yet

## Recent updates
- YYYY-MM-DD: [what changed]
```

---

## Operations

### INGEST

Triggered when the user says "ingest [filename]" or drops a new source.

**Steps (in order):**

1. **Read** the source file from `raw/`.
2. **Discuss** with the user: what are the 3–5 most important takeaways? Ask if there's anything specific to emphasize or de-emphasize.
3. **Create** a source summary page in `wiki/sources/`. File name: derived from the source file name.
4. **Identify** all entities and concepts mentioned significantly in the source.
5. **Update or create** entity pages in `wiki/entities/` for each significant entity.
6. **Update or create** concept pages in `wiki/concepts/` for each significant concept.
7. **Check for contradictions** between the new source and existing wiki pages. Document contradictions on the source page and update affected pages.
8. **Update `wiki/overview.md`** — revise the thesis and themes if the new source adds something important.
9. **Update `index.md`** — add or update entries for every page touched.
10. **Append to `log.md`** — one log entry summarizing what was done.

After ingest, report: pages created, pages updated, contradictions found.

### QUERY

Triggered when the user asks a question.

**Steps:**

1. Read `index.md` to find relevant pages.
2. Read those pages. If needed, read additional linked pages.
3. Synthesize an answer with inline `[[wiki page]]` citations.
4. Ask: "Want me to file this answer as a query page?" If yes, create in `wiki/queries/`.
5. If the answer reveals a gap (missing page, missing source), note it.

### LINT

Triggered when the user says "lint" or "health check".

**Steps:**

1. Read all pages in `wiki/` (use index.md as the entry point).
2. Report:
   - **Contradictions**: claims on different pages that conflict.
   - **Orphans**: pages with no inbound links from other wiki pages.
   - **Stubs**: pages with fewer than 3 bullets or 2 sentences of real content.
   - **Missing pages**: entities or concepts mentioned with `[[links]]` but no corresponding file.
   - **Stale overview**: if `wiki/overview.md` hasn't been updated since the last 3 ingests.
   - **Suggested sources**: topics with open questions that a web search could fill.
3. Offer to fix any of the above automatically.

---

## index.md format

`index.md` is a catalog, not a memory. It must be kept current after every ingest.

Structure:
```markdown
# Wiki Index

> **Last updated:** YYYY-MM-DD | **Sources:** N | **Pages:** N

## Overview
- [Overview](wiki/overview.md) — [one-line summary of domain/thesis]

## Sources
- [Source Title](wiki/sources/filename.md) — [one-line summary] | YYYY-MM-DD

## Entities
- [Name](wiki/entities/filename.md) — [one-line description]

## Concepts
- [Name](wiki/concepts/filename.md) — [one-line description]

## Queries
- [Question](wiki/queries/filename.md) — [one-line answer summary] | YYYY-MM-DD
```

---

## log.md format

`log.md` is append-only and chronological. Newest entries at the top.

Each entry header must match this exact format so it's grep-parseable:
```
## [YYYY-MM-DD] operation | label
```

Where `operation` is one of: `ingest`, `query`, `lint`, `init`, `update`.

Entry body: 3–6 bullet points summarizing what happened. Include pages created, pages updated, contradictions found, queries filed.

---

## Cross-referencing rules

- Every entity and concept mentioned in a page that has its own wiki page **must** be linked with `[[page title]]` Obsidian-style wikilinks on first mention in each section.
- Source pages link to entity/concept pages. Entity/concept pages link back to source pages.
- Query pages link to the source pages they draw on.
- `overview.md` links to all major concept pages.
- When creating a new page, scan all existing pages for mentions of that name and add backlinks.

---

## Contradiction handling

When a new source contradicts an existing claim:
1. Note it in the **Contradictions** section of the new source page.
2. Add a `> **Note:** Contradicted by [[source]]` block to the affected section of the existing page.
3. If there's a way to resolve the contradiction (one source is more recent, more authoritative), explain it. Otherwise, leave it flagged as open.
4. Add an open question to the relevant concept page.

---

## Session startup checklist

At the start of every session:
1. Read `AGENTS.md` (this file).
2. Read `log.md` — last 3 entries to understand recent context.
3. Read `index.md` — scan to understand wiki scope and what exists.
4. Report to user: "Wiki has N sources and N pages. Last activity: [date and operation]."
5. Ask what the user wants to do: ingest, query, lint, or explore.

If `wiki/overview.md` does not exist yet, step 5 becomes: "What is this wiki about? Let's create the overview first."

---

## Quality rules

- Never delete content without telling the user.
- Never invent facts. Only write what can be supported by a source in `raw/` or a prior wiki page.
- If a claim has no source, mark it `[unsourced]`.
- Keep pages focused. If a page exceeds ~400 lines, consider splitting it.
- Prefer updating existing pages over creating redundant new ones.
- The wiki should read as if written by one coherent author, not as a patchwork of session summaries.
