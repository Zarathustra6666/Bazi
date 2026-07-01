---
name: knowledge-summary
disable-model-invocation: true
description: >
  Summarizes the key findings of the current session — past and present conversation —
  grouped by auto-inferred concept categories. Outputs a table with columns:
  Vault | Topic | Concept | Details, followed by a separate Action Items section.
  Findings are factual and specific; uncertain items are labelled with a question mark;
  max 5 rows per category; hardcoded category names are forbidden. Each invocation
  extracts only NEW findings since the last summary was saved — not a full replay.
  Saves each summary as a dated file in C:\Bazi\wiki\synthesis\.
  Trigger on: /knowledge-summary, "summarize this session", "session summary",
  "summarize session", "what did we cover", "session recap".
---

# /knowledge-summary — Incremental Session Summary

Scans the current conversation for findings, decisions, and outcomes that have NOT
already been captured in a prior summary. Groups them by auto-inferred concept
category and renders a scannable table. Saves a new dated snapshot each invocation —
never overwrites prior summaries — so the most recent file is always the baseline for
the next run.

---

## Steps

### 1. Find the prior summary (baseline)

Glob `C:\Bazi\wiki\synthesis\session-summary-*.md` and sort filenames descending.
Read the most recent file if one exists. That file's content is the **already-captured
baseline** — do not re-summarise anything already in it.

If no file exists: treat the entire conversation as new (first invocation).

### 2. Identify the new window

Scan the conversation history for content that post-dates or is absent from the
baseline. Focus on:
- Explicit decisions or conclusions ("X was set to Y", "we chose approach Z")
- Tool results that produced a concrete finding (git status, MCP responses, file reads)
- User corrections or clarifications that changed direction
- Outcomes: files created, config changed, task completed

Ignore: greetings, tool calls with no meaningful result, content already summarised.

### 3. Extract findings

For each new finding, capture exactly:
- **Vault** — which repo or project this belongs to (e.g. `C:\Bazi`, `C:\Vault`,
  `Session-wide` for cross-project findings)
- **Topic** — the broad area, inferred from content (e.g. "Bazi Methodology", "NLM Notebooks",
  "Skill Design") — never use a hardcoded name
- **Concept** — a concise noun phrase for the specific finding or decision
- **Details** — one clear sentence. Append ❓ if the finding is uncertain or still open.

Rules:
- Each Detail must be a standalone factual sentence — not "we discussed X" but "X was
  determined to be Y"
- No jargon without expansion
- Maximum 5 rows per Topic category
- If nothing new: output "No new findings since last summary." and stop (still save the
  empty-delta file so the timestamp advances)

### 4. Render the output

Print the table, then the action items:

```
## Session Summary — YYYY-MM-DD HH:MM
> Delta since: [filename of prior summary, or "first invocation"]

| Vault | Topic | Concept | Details |
|-------|-------|---------|---------|
| ...   | ...   | ...     | ...     |

## Action Items
- [ ] Item one
- [ ] Item two
```

Action items = open questions, follow-up tasks, or anything labelled ❓ that needs
resolution. If none, omit the section.

### 5. Save the summary

Ensure the output directory exists before writing:
```bash
mkdir -p "C:\Bazi\wiki\synthesis"
```

Write the rendered output (table + action items) to:
```
C:\Bazi\wiki\synthesis\session-summary-YYYY-MM-DD-HHMM.md
```

Use the current date and time (24-hour, zero-padded). Add YAML frontmatter:
```yaml
---
title: Session Summary YYYY-MM-DD HH:MM
type: synthesis
tags: [session-summary]
created: YYYY-MM-DD
---
```

`type: synthesis` is not a formal Bazi page type (entity/concept/source/query/overview) —
`wiki/synthesis/` is a bookkeeping folder for auto-generated session artifacts only,
excluded from the formal lint type-check.

Do NOT overwrite any existing file. Each invocation produces a new dated snapshot.

### 6. Push to collaborators

After saving, immediately commit and push the new file so the other side receives it:

```bash
git -C "C:\Bazi" add "wiki/synthesis/session-summary-YYYY-MM-DD-HHMM.md"
git -C "C:\Bazi" commit -m "knowledge-summary: session snapshot YYYY-MM-DD HH:MM"
git -C "C:\Bazi" push origin HEAD
```

- Use `push origin HEAD` — pushes to whatever branch is currently checked out.
- Stage by filename only — do not use `git add -A` or `git add .`
- If push succeeds: print `Pushed to origin/<branch> — the other side will see this on next pull.`
- If push fails (offline, conflict, auth error): print a warning with the error, then stop
  gracefully — the local file is already saved and can be pushed manually via /sync.
  Do NOT abort or delete the local file on push failure.

---

## Output format reference

```
## Session Summary — 2026-06-24 14:30
> Delta since: session-summary-2026-06-24-1015.md

| Vault     | Topic           | Concept              | Details                                                        |
|-----------|-----------------|----------------------|----------------------------------------------------------------|
| C:\Bazi   | Environment     | NLM MCP auth         | Connected and authenticated; 35 notebooks found.              |
| C:\Bazi   | Git State       | Workspace dirty      | .obsidian/workspace.json and graph.json modified; stash before push. |
| C:\Bazi   | Skill Design    | knowledge-summary    | Skill created with incremental delta logic and dated output files. |

## Action Items
- [ ] Stash .obsidian changes before next git push on C:\Bazi
```

---

## Usage

```
/knowledge-summary
summarize this session
session recap
what did we cover
```

Run at any point during a session to capture a snapshot of what has been found or
decided. Each call saves a new dated file and uses the most recent prior file as its
baseline — so repeated calls throughout a long session accumulate an incremental log
without duplication.
