---
name: wiki-pipeline
description: Autonomous wiki research pipeline — spawn parallel research agents per entity, draft wiki pages, lint, and commit unattended.
triggers:
  - "/wiki-pipeline"
  - "autonomous wiki"
  - "overnight research"
  - "batch enrich"
---

# Wiki Pipeline Skill

Orchestrates parallel research sub-agents per entity, drafts wiki pages from
results, runs a lint pass, fixes issues, then commits and pushes — all unattended.

## When to invoke

- User says `/wiki-pipeline`, "batch enrich", "autonomous wiki", or "overnight research"
- User provides a list of entities/topics to research and wants wiki pages produced

## Workflow

### Step 0 — Orient
1. Read `index.md` and last 10 entries of `log.md`
2. Identify the target wiki directory (default: `C:\Vault\Z\Wiki\` or wiki closest to cwd)
3. Build the work list:
   - If the user provided an explicit list: use it
   - If no list provided: read `C:\Vault\.Codex\skills\expand\session\frontier-queue.md`
     and use all queued items with status `"deferred"` as the work list — sorted by score (highest first)
   - Report the work list to the user before proceeding

### Step 1 — Checkpoint manifest + task tracking
Before any research:
1. Write a manifest via the ingest tool:
   ```
   python C:\Vault\tools\ingest.py --topic "<topic>" --sources <url1> <url2> ...
   ```
   This saves progress so the run survives session limits or MCP disconnects.
2. Create one TaskCreate entry per entity in the work list so progress is visible:
   - Status: `pending` → `in_progress` (when agent starts) → `completed` / `blocked`
   - Update TaskUpdate after each agent reports back

### Step 2 — Parallel research agents
Spawn one Agent per entity, ALL in parallel (single message, multiple Agent tool calls).
Each agent gets:
- Entity name and known context
- Wiki page template from AGENTS.md schema
- Instruction: run 2–3 WebSearch queries + max 2 WebFetch attempts per URL
- Exact frontmatter schema to populate
- Output contract: return a complete markdown page

Agent prompt template per entity:
```
Research [ENTITY] for the wiki. Run 2–3 WebSearch queries to gather:
- Core facts, key figures, role/function
- Recent developments (last 12 months)
- Relationships to other wiki entities

Return a complete wiki page in this exact format:
---
title: [Entity Name]
type: entity
tags: [relevant, tags]
sources: [url1, url2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
[one-paragraph description]

## Key Facts
- bullet facts

## Appearances
- [[Source Page]] — context

## Related
- [[Related Entity]]

Rules:
- Max 2 WebFetch attempts per URL; skip binary/PDF/large files immediately
- If a source fails, note it and continue — do NOT stall
- Return the page even with partial data; mark gaps with "unclear as of [date]"
```

### Step 3 — Write pages
For each agent result:
1. Write to `Wiki/entities/<slug>.md`
2. If page exists: merge new facts, don't overwrite existing content
3. Update `sources:` frontmatter list
4. Add bidirectional links to mentioned entities/concepts that have pages

### Step 4 — Update index + log
- Add each new page to `index.md` under correct category
- Append one `log.md` entry per entity processed

### Step 5 — Lint
```
python C:\Vault\tools\lint_wiki.py [wiki_root]
```
- Fix orphans, broken links, frontmatter errors, then re-run
- Accept only when lint exits 0
- Max 3 fix attempts; surface remaining issues to user if still failing

### Step 6 — Commit and push
Stage files by name (not `git add -A`), then commit and push:
```
git add Wiki/entities/<slug1>.md Wiki/entities/<slug2>.md ... index.md log.md
git commit -m "wiki-pipeline: enrich [N] entities — [topic] ([date])"
git push
```
Verify `git status` is clean. If workspace.json is dirty, stash before push and stash pop after.

### Step 7 — Report
Print a summary table:
| Entity | Status | Sources | Issues |
|--------|--------|---------|--------|

## Failure handling

| Failure | Action |
|---------|--------|
| Agent returns empty | Write stub page with "unclear as of [date]", continue |
| WebFetch stalls / binary PDF | Skip after 2 attempts, add fallback WebSearch query |
| MCP disconnected | Log it, proceed WebSearch-only for that agent |
| Lint fails after 3 attempts | Commit clean pages, surface remaining issues |
| Usage/session limit | Manifest preserves progress; resume with `--resume` flag |

## Resume after interruption
```
python C:\Vault\tools\ingest.py --resume tools/manifest_<topic>_<ts>.json
```
Then re-run from Step 2 for entities whose pages weren't written.
