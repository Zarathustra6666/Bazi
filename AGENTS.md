# Wiki Agent Schema

This file is the operating manual for the LLM wiki agent. Every session starts by reading this file. Every operation follows the rules here. You (Codex) own the `wiki/` layer entirely — you create pages, update them, maintain cross-references, and keep everything consistent. The human curates sources, directs analysis, and asks questions.

---

## Purpose

This is a personal second-brain wiki. The domain will evolve over time and is reflected in `wiki/overview.md`. When the overview page does not yet exist, ask the user what the wiki's focus is before doing any ingest.

---

## Directory layout

```
Vault/Bazi/
├── CLAUDE.md           ← this file — read every session
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

---

## Operating Protocol

The sections below are shared operational conventions, ported from `C:\Vault\CLAUDE.md`
so this repo behaves the same way as Vault: same commands (`.claude/commands/`,
`.claude/agents/`, `.claude/skills/`), same checkpoint/resume behavior, same git sync
discipline, same debugging/error/output conventions. Domain-specific Vault rules that
don't apply here (Regulatory Facts Rule, Bot & App Builds) are intentionally omitted.

### Checkpoint & Auto-Resume

**Philosophy:** Checkpointing is milestone-based — write after each major step
completes. There is no way to detect how close a usage limit is, so checkpointing is
not limit-proximity-based. When a limit hits mid-stream, the checkpoint reflects the
last completed milestone.

**When to write a checkpoint** — `session-checkpoint.md` at the repo root
(`C:\Bazi\session-checkpoint.md`):
- At the **start** of any task with 3+ steps — before executing step 1
- After each major step completes — update the file immediately
- Before any expensive or irreversible operation (large web fetch, multi-file rewrite, git push)
- **Delete** the checkpoint when the full task is done and the lint pass is clean
- **Front-load expensive steps** — for tasks involving subagents, NLM notebooks, or web
  research: order phases so token-heavy work runs first, while context is still small.
  Never leave the most expensive phase for last.

**Checkpoint format:** Frontmatter `task`, `updated`, `step_current`, `step_next`,
`status: in-progress`. Body sections: `## Task`, `## Progress` (checkboxes),
`## Files Modified`, `## Decisions Made`, `## Next Actions`.

**Session start — checkpoint detection:** Before reading `index.md` or `log.md`, check
if `session-checkpoint.md` exists.
- If found — announce: `Checkpoint found: "[task]" — step [N], next: [step_next].` then
  `Type "resume" to continue, or "discard checkpoint" to ignore.` Wait for the user.
- If not found — proceed with the normal Session Startup Checklist.

**Resume trigger** — on "continue", "resume", "pick up", or "/resume":
1. Read `session-checkpoint.md`
2. Print `Resuming "[task]" — executing: [step_next]`
3. Execute `step_next` immediately without asking for re-explanation
4. Continue through remaining steps
5. On full completion + clean lint: delete the checkpoint and log the completion

On "discard checkpoint": delete it, ask what to work on. If the user starts a different
task while a checkpoint exists, ask: `Checkpoint exists for "[task]" — discard it?`

**Checkpoint file location:** `C:\Bazi\session-checkpoint.md` — listed in `.gitignore`,
never committed. Only one checkpoint at a time (overwrite, never append). After a usage
limit: run `C:\Vault\tools\wait_and_resume.ps1 <time>` or
`python C:\Vault\tools\wait_and_resume.py <time>` to auto-resume (shared script, works
from any repo).

### Git Sync Protocol

This repo syncs **itself only** — it is not a multi-repo hub like `C:\Vault`. If
cross-vault sync is ever needed, that's `/parallel-sync` run from `C:\Vault`.

1. Stage files by name (not `git add -A`) — avoids accidentally including output artifacts
2. Commit with a descriptive message summarising what changed (not just "update files")
3. If `.obsidian/workspace.json` or other workspace-state files are dirty: stash →
   pull --rebase → push → stash pop
4. If merge conflict: stop, show conflict files, ask "take ours / take theirs / manual?"
   — never auto-resolve
5. **After resolving merge conflicts, re-run lint before committing** — never commit
   conflict-resolved files without a clean lint pass first
6. After push, confirm with `git log --oneline -3`
7. **Verify the repo path exists before any git operation** — run `git -C C:\Bazi status`
   first; if it errors, stop and report rather than proceeding
8. **Never assume the branch name** — detect with
   `git -C C:\Bazi rev-parse --abbrev-ref HEAD` and use the result throughout
9. **Verify push landed on the remote** — after push, run
   `git log origin/<branch> -1` and compare the hash to the commit from the staging
   step; if they differ, flag "push unconfirmed" and retry

### Partner Agent Protocol (Codex)

Codex is a co-equal partner — both agents work on **any task** in this repo: wiki
ingests, lint, synthesis, research. No lane assignment. Coordination is at the task
level via `COLLAB.md`.

**Session start:**
1. Read `COLLAB.md` (repo root) **BEFORE** `index.md`
2. Check **In Progress**: do not touch tasks claimed by the partner unless their Resume
   Handoff file says to continue
3. Claim a Queue item by moving it to In Progress with your name and today's date

**Session end:**
1. Run `python C:/Vault/tools/lint_wiki.py C:/Bazi` — fix all issues
2. Write handoff to `handoffs/handoff_<YYYY-MM-DD>_<HH-MM>_<agent>-<slug>.md` using
   `handoffs/HANDOFF-TEMPLATE.md`
3. Update `COLLAB.md`: release In Progress row, update Latest Handoff, add Done item
4. Commit with `[claude]` or `[codex]` prefix; push

**Parallel work (both agents active simultaneously):**
- Each agent claims separate rows in COLLAB.md In Progress before editing
- Never edit the same file at the same time — if partner has a file claimed, skip it
- After both finish: one agent pulls, runs lint, resolves any conflicts, pushes

Shared format rules (filenames, wiki location, handoff naming, commit prefix, Python/
shell conventions) live in `COLLAB.md § Format rules` — that table is the single source
of truth, not duplicated here.

### Debugging Approach

Always check the simplest causes first before theorizing complex root causes:

1. **Credentials** — wrong password, expired token, wrong account?
2. **Auth state** — session expired, MCP disconnected, cookie stale?
3. **Path/config** — pointing at the wrong file, wrong URL, wrong selector?
4. **Then** — frame-scoping, JS execution model, redirect chains, network errors

Run a manual spot-check (e.g., log in manually, print the credential, open the URL) to
rule out the obvious before diving into code-level diagnosis. Document which simple
causes were ruled out when reporting a complex hypothesis.

### Error Handling

When a tool or MCP call returns an auth or connectivity error:
1. State the likely cause in plain language (not just the raw error code)
2. Print the exact command the user needs to run to fix it
3. Wait for the user to confirm the fix before continuing

Common cases:
- NLM 401 / auth expired → `NLM auth expired — run notebooklm-mcp-auth in your terminal`
- GitHub 401 → `Check the GITHUB_TOKEN in settings.local.json`
- NotebookLM MCP timeout → `MCP server may need restart; run /preflight to confirm`

Never echo a raw API error message as the sole response — always add the diagnosis and the fix.

### Research Workflow

- **NLM MCP is a session gate, not a dependency** — if any NLM work is planned, verify
  auth before doing anything else (including reading index.md). Check auth by calling
  `mcp__notebooklm-mcp__notebook_list` as the very first action of the session.
- **Before any NotebookLM MCP work:** call `mcp__notebooklm-mcp__notebook_list` first.
  If it returns an auth error or 400, stop immediately and tell the user to run
  `notebooklm-mcp-auth` in their terminal. Do not attempt any NLM MCP tasks until the
  user confirms re-auth succeeded. Switch to WebSearch-only for the session if re-auth
  is not possible.
- Prefer **WebSearch** and **WebFetch** directly for any web research
- If NotebookLM MCP is disconnected or returns an error mid-task: **fall back to
  WebSearch-only immediately** — do not stall waiting for MCP to reconnect; note the
  gap in the log entry
- For PDF sources: **cap at 2 fetch attempts** per PDF — if extraction stalls or the
  file is large/binary, write the page with the data already gathered and note what's
  missing; do not retry indefinitely
- For multi-entity research (≥3 sources/concepts): prefer **sequential WebSearch** over
  parallel subagents — parallel agents have repeatedly hit rate limits and forced a
  full redo elsewhere in this vault system. Only spawn parallel subagents when the task
  is time-critical and entities are truly independent; if doing so, stagger start times
  and cap at 3 agents.
- **Batch research loops** — for multi-topic research runs: process one topic per turn,
  write session files to disk immediately after each topic, output a one-line status,
  then continue. Never hold results in context until a batch is complete.
- **Delegate large wiki reads to subagents** — when exploration spans many files
  ("understand the whole wiki", "find all pages about X"): spawn an `Explore` or
  `general-purpose` subagent and ask for a concise summary.

### Output Limits

Exceeding output-token limits terminates sessions without saving work. Treat these as
hard constraints:

- **Never generate more than ~200 lines of prose output in a single turn** — split
  large multi-file edits, research digests, and wiki batches into sequential operations
- For multi-topic research loops: process **one topic at a time**, write to disk
  immediately, output a one-line status summary, then continue
- For vault-wide reads ("read the whole wiki", "find all mentions of X"): **delegate to
  a subagent** (Explore or general-purpose type) — subagents return a concise summary
  without expanding main-context tokens
- When a task requires generating more than 500 lines total: break it into named
  batches, confirm the plan first, and write each batch to disk before starting the next
- If compelled to output a large text block in conversation: summarize instead and
  write the full content to a file
- **Default response length for non-synthesis, non-ingest tasks: ≤5 bullets or ≤150
  words.** No trailing summaries. Override explicitly ("expand", "full detail") when
  more is needed.

### Windows Encoding

- Avoid Unicode box-drawing characters (┌, ─, └, │, etc.) in console output, scripts,
  or runner files — PowerShell/cmd on Windows may crash or produce garbled output
- When writing files read by Python or Node.js scripts, specify UTF-8 encoding
  explicitly (`-Encoding utf8` in PowerShell; `encoding='utf-8'` in Python `open()`)
- If a script produces garbled output or `UnicodeEncodeError`: add `chcp 65001` at the
  top of PowerShell scripts, or `sys.stdout.reconfigure(encoding='utf-8')` at the top of
  Python scripts
- The wiki lint tool (`C:\Vault\tools\lint_wiki.py`) already uses
  `encoding="utf-8", errors="replace"` for file reads and stdout — do not add redundant
  encoding flags when calling it
- PowerShell lint broken-link reports may be encoding false positives — always re-run
  `python C:/Vault/tools/lint_wiki.py C:/Bazi` to confirm before acting or reporting

### Skill Execution

When executing any skill (slash command) with 3 or more steps:
- **Before each step**, emit one short status line in the format:
  `> **[Step N/M — Step Name]** starting…`
- This applies to all skills in `C:\Bazi\.claude\commands\` and global skills
- The line must appear *before* the first tool call for that step, not after
- Keep the label to ≤ 8 words — not a sentence, just a label

### Correction Protocol

When correcting a factual claim that may have propagated to multiple files:

1. **Grep first** — search the full wiki for the pattern before touching any file
2. **Fix all instances in one pass** — do not fix one file and leave others
3. **Log the scope** — the `log.md` entry must state how many files were corrected,
   not just which file was the primary one
4. **Add a ⚠️ note** on the canonical page explaining what the old claim was and why it
   was wrong

### Testing

- This repo has **no test suite** — wiki-only changes are verified by lint, not tests
- If a future task adds a test suite (e.g. to a code component), actually execute it
  and show the output — do NOT treat data updates, file writes, or lint passes as
  equivalent to passing tests
- Never assert "tests pass" without running them

### Verification

Before declaring any task complete, **prove the goal was met**:
- For wiki work: run the lint pass and show a clean result
- For web automation: confirm the flow executes (screenshots, logs, or DOM evidence)
- "I updated the files" is not proof — observable output is proof
- If you cannot verify, say so explicitly

### Definition of Done

- "Done" for a wiki session means a clean lint pass (no broken WikiLinks, no orphans,
  no frontmatter errors)
- **Never fabricate a test suite** to satisfy a completion criterion
- Run `python C:/Vault/tools/lint_wiki.py C:/Bazi` to verify completion
- If a Stop hook or goal-loop fires on an unsatisfiable condition: diagnose the hook,
  surface the configuration issue to the user, and stop — never fabricate artifacts to
  escape the loop

### Handoffs & Collaboration

- All handoff documents and shared files must be saved inside the `C:\Bazi` repo (not
  local temp paths or scratchpad directories) so collaborators can access them after sync
- Save handoffs to `handoffs/<YYYY-MM-DD>-<slug>.md` or
  `handoffs/handoff_<YYYY-MM-DD>_<HH-MM>_<agent>-<slug>.md` (see `COLLAB.md`)
- Never reference a file path in a handoff that only exists on your local machine

### Scope Clarity

Before starting any research, build, or automation task, confirm the deliverable type
if it is ambiguous:
- **Plan only** — write a plan file and stop; do not research live UIs, run code, or
  make edits beyond the plan
- **Implementation** — execute the full task through to completion
- **Live run** — execute against a real system

Default to **plan only** for first-time or under-specified tasks — never dive into live
exploration without confirming scope.
