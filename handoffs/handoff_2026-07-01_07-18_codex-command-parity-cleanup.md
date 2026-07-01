# Handoff - Bazi Command Parity Cleanup

> From: codex
> To: claude
> Date: 2026-07-01 07:18
> Related commit(s): `pending local commit for command-parity cleanup`
> Related handoff(s): `handoffs/handoff_2026-07-01_07-07_claude-protocol-parity.md`

---

## Claim

Finished the remaining command-layer parity cleanup that the earlier protocol-port session
missed: several `.claude/commands/*.md` files in `C:\Bazi` still pointed at `C:\Vault`
paths or Vault fleet-wide behavior and were rewritten for Bazi-local behavior.

---

## Verified Facts

- **Fact:** The earlier parity handoff claimed completion, but `C:\Bazi\.claude\commands\`
  still contained stale Vault-scoped references afterward.
  **Evidence:** `rg -n "C:\\Vault|/c/Vault" C:\Bazi\.claude\commands C:\Bazi\CLAUDE.md C:\Bazi\AGENTS.md`
  showed stale hits in `autoresearch.md`, `endsession.md`, `firesearch.md`,
  `parallel-sync.md`, `preflight.md`, `sync.md`, `wiki-heal.md`, and an example in
  `lit-review.md`.

- **Fact:** The Bazi command set exists locally and was the active write target for this
  cleanup.
  **Evidence:** `Get-ChildItem -Recurse -Depth 2 C:\Bazi\.claude\commands | Select-Object FullName,LastWriteTime`
  listed the full command tree, including the affected files.

- **Fact:** The current cleanup modified 9 tracked files in `C:\Bazi`.
  **Evidence:** `git -c safe.directory=C:/Bazi -C /c/Bazi status --short` showed modified
  files for `.claude/commands/{autoresearch,endsession,firesearch,lit-review,parallel-sync,preflight,sync,wiki-heal}.md`
  plus `COLLAB.md`.

- **Fact:** The diff is command-doc focused, not wiki-content focused.
  **Evidence:** `git -c safe.directory=C:/Bazi -C /c/Bazi diff --stat` showed edits only in
  command markdown files and `COLLAB.md`.

- **Fact:** Some remaining `C:\Vault` references are intentional shared-tool or cross-repo
  mentions, not stale repo-target paths.
  **Evidence:** post-edit `rg -n "C:\\Vault|/c/Vault" C:\Bazi\.claude\commands` shows
  surviving references only in:
  - shared-tool notes (`resume-agents.md` -> `C:\Vault\tools\agent_journal.*`)
  - shared-vault examples or explicit contrast (`parallel-sync.md`, `autoresearch.md`)
  - cross-repo explanatory notes (`nightly-pipeline.md`, `knowledge-summary.md`)

- **Fact:** I did not verify a clean Bazi lint pass during this cleanup.
  **Evidence:** `bash -lc "python /c/Vault/tools/lint_wiki.py /c/Bazi"` returned
  `/usr/bin/bash: line 1: python: command not found`, so no new clean-lint claim was made.

---

## Interpretation

The prior session correctly ported the high-level protocol and committed the hidden
`.claude/` tree, but it missed a second layer of drift inside several copied command
files. The repo now has Bazi-local command behavior for the main operational commands
instead of silently pointing those workflows back at `C:\Vault`.

This does not resolve Bazi's pre-existing wiki-content lint debt. It resolves the
command/protocol parity gap only.

---

## Open Questions

- [ ] Whether `firesearch` should remain as a redirect-only command in Bazi, or be removed
  from the Bazi command set entirely in a later cleanup.
- [ ] Whether the shared-tool commands should eventually move shared helpers out of
  `C:\Vault\tools\` into a neutral shared location.
- [ ] Whether to normalize the remaining explanatory references to `C:\Vault` for style,
  even though they are no longer load-bearing path bugs.

---

## Files Touched

- `C:\Bazi\.claude\commands\autoresearch.md` - localized to Bazi `.autoresearch` and Bazi-only lint/commit flow
- `C:\Bazi\.claude\commands\endsession.md` - rewrote for single-repo Bazi cleanup
- `C:\Bazi\.claude\commands\firesearch.md` - converted to Bazi-safe redirect behavior
- `C:\Bazi\.claude\commands\lit-review.md` - removed stale `C:\Vault\Z` example
- `C:\Bazi\.claude\commands\parallel-sync.md` - fixed fleet discovery to start from `C:\`
- `C:\Bazi\.claude\commands\preflight.md` - localized to `C:\Bazi\.mcp.json` and Bazi repo status
- `C:\Bazi\.claude\commands\sync.md` - rewrote for `C:\Bazi` single-repo git flow
- `C:\Bazi\.claude\commands\wiki-heal.md` - localized to `C:\Bazi\wiki`
- `C:\Bazi\COLLAB.md` - claimed then closed the task, updated done row and latest handoff

---

## Commands Run

- `Get-ChildItem -Recurse -Depth 2 C:\Bazi\.claude\commands | Select-Object FullName,LastWriteTime` - confirmed command inventory
- `rg -n "C:\\Vault|/c/Vault" C:\Bazi\.claude\commands C:\Bazi\CLAUDE.md C:\Bazi\AGENTS.md` - found stale path references
- `git -c safe.directory=C:/Bazi -C /c/Bazi status --short` - verified modified file set
- `git -c safe.directory=C:/Bazi -C /c/Bazi diff --stat` - verified diff scope
- `bash -lc "python /c/Vault/tools/lint_wiki.py /c/Bazi"` - failed because `python` is not on the Bash PATH here

---

## Next Action

Commit and push the Bazi repo changes, then decide separately whether to tackle the
pre-existing Bazi wiki lint debt.

---

## Convention Reminders

- Filenames: `lowercase-hyphens.md` - never PascalCase or spaces
- Wiki location: `C:\Bazi\wiki\{sources,concepts,entities,queries}\`
- Lint before committing: `python C:/Vault/tools/lint_wiki.py C:/Bazi`
- Commit prefix: `[claude]` or `[codex]`
- Update `COLLAB.md` at session end: release In Progress row, update Latest Handoff, add Done item
