---
name: nightly-pipeline
description: >
  Autonomous repo-maintenance pipeline for C:\Bazi: preflight, lint, fix, conflict-check,
  stub research via parallel subagents, commit-push, nightly report. Designed to run
  unattended; only escalates wiki-content merge conflicts and silent subagent failures.
  Trigger on: /nightly-pipeline, "run nightly", "autonomous vault maintenance".
---

# /nightly-pipeline — Autonomous Bazi Maintenance

> **Pre-flight (Remote):** Call ToolSearch once before starting: `select:WebSearch,WebFetch,mcp__notebooklm-mcp__notebook_list,mcp__notebooklm-mcp__notebook_add_url,SendMessage`
> Skip if these tools were already loaded earlier in this session.

Runs a full lint-research-sync cycle on **C:\Bazi only** without prompting. Only pauses
for wiki-content merge conflicts and subagent failures that return no output.

This pipeline is scoped to Bazi — it does not act as a multi-repo hub. Vault's own
`/nightly-pipeline` (run from C:\Vault) handles fleet-wide maintenance separately.

---

## Steps

### 1. Preflight

Run the same checks as `/preflight`:
- Git version, Node.js version, `.mcp.json` valid
- Call `mcp__notebooklm-mcp__notebook_list`
  - If auth fails: log `NLM: auth expired — NLM steps skipped` and continue in WebSearch-only mode
  - Do NOT stop the pipeline for NLM auth failure — skip NLM steps and proceed

### 2. Lint the wiki

```bash
python C:/Vault/tools/lint_wiki.py C:/Bazi
```

Post-process output: filter out any line containing Unicode box-drawing characters
(U+2500–U+257F range: `─`, `│`, `┌`, `└`, etc.) before treating results as real issues —
these are encoding false positives on Windows. Only act on lines that survive this filter.

Record: broken WikiLink count, orphan count, frontmatter errors.

### 3. Fix lint issues (1 pass, capped)

Fix all surviving lint issues:
- **Broken WikiLinks**: update the link target or create a stub page with correct title
- **Orphans**: add an inbound link from the most relevant concept/entity page, or add to `index.md`
- **Frontmatter errors**: add missing required keys (`title`, `type`, `created`, `updated`)

Cap at 1 fix pass. If issues remain after the pass, log them in the nightly report and continue.

### 4. Conflict check

```bash
git -C "C:\Bazi" status --short
```

On merge conflict:
- Config-only files (`.obsidian/`, `.vscode/`, `.claude/`): auto-resolve with `ours`
  ```bash
  git -C "C:\Bazi" checkout --ours <file>
  git -C "C:\Bazi" add <file>
  ```
- Wiki content files (`wiki/`, `raw/`, `*.md` outside config dirs): **STOP pipeline**, show filename, ask "take ours / take theirs / manual?" — never auto-resolve wiki content conflicts

### 5. Stub research (WebSearch only)

Read `C:\Bazi\index.md`. Find pages tagged `[STUB]` or with fewer than 3 content bullets.
Take up to 3 stubs. If 0 stubs found, skip this step.

For each stub (up to 3): spawn a parallel `general-purpose` subagent with this prompt:
```
Research [topic] and expand the stub wiki page at [file_path].
Add at minimum: 3 content bullets, 1 WikiLink to a related page, updated frontmatter (updated: YYYY-MM-DD).
Use WebSearch only (no NLM MCP). Return a one-line result: "expanded [topic] — N bullets added".
```

Collect results. If a subagent returns no output or errors: fall back to a direct WebSearch
in the main session for that topic. Log any fallbacks in the nightly report.

### 6. Post-research lint pass

After subagents return, run:
```bash
python C:/Vault/tools/lint_wiki.py C:/Bazi
```

Fix any new issues introduced by subagent edits (cap at 1 pass).

### 7. Commit and push

```bash
git -C "C:\Bazi" add <specific changed files — never -A>
git -C "C:\Bazi" commit -m "nightly-pipeline YYYY-MM-DD: <brief summary>"
git -C "C:\Bazi" pull --rebase origin <branch>
git -C "C:\Bazi" push origin <branch>
git -C "C:\Bazi" log --oneline -1
```

Detect `<branch>` with `git -C "C:\Bazi" rev-parse --abbrev-ref HEAD` — never hardcode `master`.
Include the commit hash in the status report.
On any git failure: log `✗ C:\Bazi — <reason>` and stop the pipeline (single-repo scope —
nothing else to fall back to).

### 8. Write nightly report

Write `C:\Bazi\nightly-report-YYYY-MM-DD.md`:

```markdown
---
title: Nightly Pipeline Report YYYY-MM-DD
type: synthesis
tags: [nightly, maintenance]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# Nightly Pipeline Report — YYYY-MM-DD

## Preflight
- Git: ✓/✗
- NLM MCP: ✓ connected / ✗ skipped (auth expired)

## Lint
- Broken WikiLinks fixed: N
- Orphans fixed: N
- Frontmatter errors fixed: N
- Remaining after fix pass: N (see details below)

## Conflict Check
- Auto-resolved (config): N files
- Manual required: [list filenames if any]

## Stub Research
- Stubs found: N
- Expanded by subagents: N
- Fallbacks (direct WebSearch): N
- Subagent errors: N

## Push Summary
- C:\Bazi    ✓/✗  <branch>  <hash> — <message>

## Escalations Required
[List any issues needing manual attention]
```

`type: synthesis` is a bookkeeping convention here, not a formal Bazi page type — this
report lives at repo root, not inside `wiki/`.

### 9. Log

Append to `C:\Bazi\log.md`:
```
## [YYYY-MM-DD] update | Nightly Pipeline
- Lint: N issues fixed, N remaining
- Stubs expanded: N (topics)
- Push: ✓/✗
```

---

## Escalation Policy

Only pause for:
- Wiki-content merge conflicts (step 4) — ask user
- Subagent returns no output AND direct WebSearch also returns nothing (step 5) — log and continue

Everything else (NLM auth failure, subagent error with fallback available) is logged in
the nightly report and skipped without pausing. Git push failure (step 7) stops the
pipeline since there is only one repo in scope.

---

## Usage

```
/nightly-pipeline
```

Can be scheduled via `/schedule` for recurring autonomous runs.
