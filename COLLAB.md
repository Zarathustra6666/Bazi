---
title: Collaboration Work Board
type: synthesis
tags: [collab, coordination]
created: 2026-07-01
updated: 2026-07-01
---

# Collaboration Work Board

> Both agents (Claude Code + Codex) read this **BEFORE** `index.md` at every session start.
> Update at session start (claim task) and session end (release claim / mark done).

---

## In Progress

| Task | Agent | Since | Status | Resume Handoff |
|------|-------|-------|--------|----------------|
| (none) | - | - | - | - |

---

## Queue (unclaimed - either agent picks up anything here)

- [ ] Undocumented `Wiki/masters/`, `Wiki/synthesis/`, `Wiki/texts/` subfolders vs
  `CLAUDE.md`'s documented schema - decide whether to formalize or consolidate
- [ ] `C:\Vault\.claude\commands\parallel-sync.md` hardcodes `find /c/Vault` instead of
  `find /c` - misses Bazi/TicketBots/TicketBotsWeb in fleet-wide discovery; fix in
  Vault, then re-sync to Bazi
- [ ] 272 pre-existing lint issues in `Wiki/` content (broken bilingual WikiLinks,
  missing frontmatter, orphans) - candidate for `/wiki-batch-expand` or `/nightly-pipeline`

---

## Done This Week

- [x] 2026-07-01 claude - ported full operating-protocol parity from C:\Vault (commands, checkpoint/resume, git sync protocol, debugging/error handling, output limits, Partner Agent Protocol + this board)
- [x] 2026-07-01 codex - fixed remaining Bazi command parity gaps (stale Vault paths, single-repo sync docs, Bazi-local wiki-heal/preflight/sync/endsession)

---

## Latest Handoff

| From | Date | File |
|------|------|------|
| codex | 2026-07-01 | `handoffs/handoff_2026-07-01_07-18_codex-command-parity-cleanup.md` |

---

## How to Use This Board

### Claiming a task
1. Move a Queue item to **In Progress** - add your agent name and today's date
2. If you stop mid-task: write a handoff, fill in the "Resume Handoff" column, leave the row in In Progress
3. The partner reads that handoff and continues from exactly where you stopped

### Finishing a task
1. Remove your row from In Progress
2. Add a `[x]` line to Done This Week
3. Update the **Latest Handoff** row with your new handoff file
4. Add any new open items to the Queue

### Writing handoffs
- Copy `handoffs/HANDOFF-TEMPLATE.md` for every non-trivial handoff
- **Verified Facts must include evidence** - for every local-state claim (file exists, lint clean, push landed, repo is clean), include the exact command or file read used to confirm it. Do not state inferences as facts.
- **Correction block required** when correcting a prior handoff - see template `## Correction` section

### Format rules (both agents - non-negotiable)
| What | Convention |
|------|-----------|
| Filenames | `lowercase-hyphens.md` (never PascalCase or spaces) |
| Wiki location | `C:\Bazi\wiki\{sources,concepts,entities,queries}\` |
| Handoff naming | `handoff_YYYY-MM-DD_HH-MM_<agent>-<slug>.md` |
| Session summaries | `session-summary-YYYY-MM-DD-HHMM.md` in `wiki/synthesis/` with `> Agent:` line |
| Commit prefix | `[claude] verb: description` or `[codex] verb: description` |
| Python: module docstring | Triple-quoted at top; list functions/phases |
| Python: section headers | `# -- Section Name -------------------------` |
| Python: file I/O | `pathlib.Path`; `encoding="utf-8"` on all `open()` calls |
| Shell in docs | Bash syntax only (`rm -rf`, `$VAR`, `/c/Bazi`) - never PowerShell |
| Code blocks | Always labeled: ` ```python `, ` ```bash `, ` ```yaml `, ` ```markdown ` |
| Lint before commit | `python C:/Vault/tools/lint_wiki.py C:/Bazi` |
