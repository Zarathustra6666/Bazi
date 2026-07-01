# Handoff — Bazi Operating-Protocol Parity with C:\Vault

> From: claude
> To: codex
> Date: 2026-07-01 07:07
> Related commit(s): `1e6d065 Port operating-protocol parity from C:\Vault: commands, checkpoint/resume, git sync, Partner Agent Protocol`
> Related handoff(s): none (first handoff in this repo — `handoffs/` and `COLLAB.md` were created in this same session)

---

## Claim

User asked for C:\Bazi to operate with the same ability as C:\Vault (commands, protocol,
git sync). Full parity was scoped and executed: `.claude/` version-control blocker fixed,
commands/agents refreshed and completed, and Vault's generic operating protocol merged
into `CLAUDE.md`/`AGENTS.md`. Committed and pushed as `1e6d065`.

---

## Verified Facts

- **Fact:** Before this session, `C:\Bazi\.claude\` had never been committed — all
  commands/agents/skills that existed on disk since 2026-06-20/21 were invisible to git.
  **Evidence:** `git -C /c/Bazi ls-files .claude | wc -l` → `0`, and
  `git -C /c/Bazi check-ignore -v .claude/commands/sync.md` →
  `.gitignore:2:.claude/	.claude/commands/sync.md`

- **Fact:** `.gitignore` line 2 (`.claude/`) was the sole cause — Vault's `.gitignore`
  only ignores `.claude/settings.local.json` and `.claude/worktrees/`.
  **Evidence:** direct read of both `.gitignore` files, compared side by side.

- **Fact:** After the fix, all 47 previously-invisible/updated files are now tracked and
  pushed to `origin/master`.
  **Evidence:** `git -C /c/Bazi log origin/master -1 --oneline` →
  `1e6d065 Port operating-protocol parity from C:\Vault...` — matches local HEAD hash
  `1e6d0658c76740e02af9134a08558903ad516ff4` exactly (verified via
  `git rev-parse HEAD` vs `git rev-parse origin/master` before declaring done).

- **Fact:** `C:\Bazi\.claude\settings.local.json` remained untracked after staging
  (correctly excluded).
  **Evidence:** `git -C /c/Bazi ls-files .claude/settings.local.json` → empty output.

- **Fact:** Bazi's actual `Wiki/` content tree has 272 pre-existing lint issues
  (broken bilingual `[[WikiLinks]]`, missing/invalid YAML frontmatter, orphan pages) —
  none introduced by this session; none of the files touched this session are under
  `Wiki/` or `wiki/`.
  **Evidence:** `python C:/Vault/tools/lint_wiki.py C:/Bazi` → `[lint] 272 issue(s) found`,
  cross-checked against `git -C /c/Bazi status --short` before staging, which showed only
  `.gitignore`, `AGENTS.md`, `CLAUDE.md`, plus new `.claude/`, `COLLAB.md`, `handoffs/`.

- **Fact:** `AGENTS.md` and `CLAUDE.md` are now identical except two intentional lines
  (line 3: "Codex" vs "Claude Code"; line 311: "Read `AGENTS.md`" vs "Read `CLAUDE.md`").
  **Evidence:** Python line-by-line diff (CRLF-normalized) → `diff count: 2`, both at the
  expected line numbers with the expected content.

---

## Interpretation

Bazi's `.claude/` config existed and *worked locally* for whoever set it up on
2026-06-20/21, which is presumably why the gap went unnoticed — but a second checkout
(you, or CI, or a fresh clone) got none of it. That silent gitignore bug is the most
important thing to internalize from this handoff: it means any prior session's claim
that "Bazi has the same commands as Vault" was true on disk but false in git history
until this commit.

The 272 wiki-content lint issues are unrelated technical debt in Bazi's actual `Wiki/`
folder (note: also check whether the real folder is cased `Wiki/` vs the lowercase
`wiki/` documented in `CLAUDE.md` — on this Windows/NTFS filesystem the two are the same
directory since NTFS is case-insensitive, so it's cosmetic, but worth normalizing case
in the docs at some point). It was flagged to the user and intentionally left untouched
— fixing it would have required content edits (sourcing, correction protocol) well
beyond "port the operating protocol."

---

## Open Questions

- [ ] Bazi's `Wiki/` tree also has `masters/`, `synthesis/`, and `texts/` subfolders that
  are **not** documented in `CLAUDE.md`'s directory layout (which only lists `overview.md`,
  `entities/`, `concepts/`, `sources/`, `queries/`). Was this an intentional schema
  extension from an earlier session? If so, `CLAUDE.md`'s "Directory layout" and page
  frontmatter `type:` enum should be updated to document it — currently undocumented
  drift between schema and actual content. Not resolved this session.
- [ ] Vault's own `.claude/commands/parallel-sync.md` (and therefore Bazi's freshly-copied
  identical version) hardcodes `find /c/Vault -maxdepth 3 -name ".git" -type d` for repo
  discovery — this misses `C:\Bazi`, `C:\TicketBots`, `C:\TicketBotsWeb` entirely, since
  the real repos live at `C:\` root, not nested under `C:\Vault`. CLAUDE.md's own "Vault
  Structure" section documents the correct authoritative command as
  `find /c -maxdepth 2 -name ".git" -type d`. This is a pre-existing bug in Vault's
  command file (not something introduced or fixed this session) — flagging since it
  affects both repos identically. Worth a follow-up fix in `C:\Vault\.claude\commands\parallel-sync.md`
  and then re-syncing to Bazi.

---

## Files Touched

- `C:\Bazi\.gitignore` — replaced bare `.claude/` with the granular Vault pattern; also
  added `session-checkpoint.md` to the ignore list (was missing)
- `C:\Bazi\CLAUDE.md` / `C:\Bazi\AGENTS.md` — appended a new `## Operating Protocol`
  section (Checkpoint & Auto-Resume, Git Sync Protocol, Partner Agent Protocol,
  Debugging Approach, Error Handling, Research Workflow, Output Limits, Windows
  Encoding, Skill Execution, Correction Protocol, Testing, Verification, Definition of
  Done, Handoffs & Collaboration, Scope Clarity)
- `C:\Bazi\COLLAB.md` — new, work board (empty Queue, seeded Done entry for this session)
- `C:\Bazi\handoffs\HANDOFF-TEMPLATE.md` — new, adapted from Vault's template
- `C:\Bazi\.claude\commands\` — 12 files refreshed verbatim from Vault (`preflight.md`,
  `sync.md`, `endsession.md`, `autoresearch.md`, `domain-daily.md`, `domain-weekly.md`,
  `wiki-heal.md`, `lit-review.md`, `parallel-sync.md`, `research.md`, `firesearch.md`,
  `knowledge-bridge.md`); 6 new files added with paths rewritten for Bazi
  (`knowledge-summary.md`, `nightly-pipeline.md`, `resume-agents.md`, `usage-plan.md`
  copied as-is, `wiki-batch-expand.md`, `wiki-quality-loop.md`)
- `C:\Bazi\.claude\agents\stub-researcher.md` — new (was missing; needed by
  `wiki-batch-expand`)
- `C:\Bazi\.claude\settings.json` — added `UserPromptSubmit` → `session_state.py load`
  and `PreToolUse` (`mcp__notebooklm` matcher) → `check_nlm_auth.py` hooks
- `C:\Bazi\.claude\agents\{citation-verifier,domain-scout,knowledge-expander,knowledge-ingest,reference-triage}.md`
  and `C:\Bazi\.claude\skills\*` — pre-existing files on disk since 2026-06-20/21, now
  committed for the first time (see gitignore fix above)
- `C:\Bazi\wiki\synthesis\` — new empty directory (storage location for auto-generated
  session-summary/nightly-report artifacts; not a formal page type in Bazi's schema)

---

## Commands Run

- `git -C /c/Bazi ls-files .claude | wc -l` → `0` (confirmed the blocker)
- `python C:/Vault/tools/lint_wiki.py C:/Bazi` → 272 pre-existing issues, none from this session
- `git -C /c/Bazi add <files by name>` then `git commit` → `1e6d065`
- `git -C /c/Bazi push origin master` → `a31d22a..1e6d065  master -> master`
- `git -C /c/Bazi rev-parse HEAD` vs `git -C /c/Bazi rev-parse origin/master` → match, push confirmed

---

## Next Action

Nothing blocking. If you want to pick something up next:
1. Resolve the two Open Questions above (undocumented `Wiki/` subfolders; `parallel-sync.md`
   discovery bug) — the second one affects Vault too, so fix it there first, then re-sync to Bazi.
2. Optionally run `/nightly-pipeline` or `/wiki-batch-expand` from `C:\Bazi` to start working
   down the 272 pre-existing lint issues — not urgent, just flagged.

---

## Session Accomplishments

- Fixed `.claude/` gitignore blocker (0 → 47 files tracked and pushed)
- Refreshed 12 stale commands, added 6 missing generic commands with Bazi-scoped paths
- Added missing `stub-researcher` agent
- Fixed `settings.json` hook gaps (NLM auth guard, session-state hooks)
- Merged Vault's generic Operating Protocol into `CLAUDE.md`/`AGENTS.md` (domain-specific
  Vault rules intentionally excluded)
- Created `COLLAB.md` + `handoffs/HANDOFF-TEMPLATE.md` to bootstrap the Partner Agent
  Protocol in this repo
- Verified push landed on remote before declaring done

---

## Open Items Added to Queue

- [ ] Undocumented `Wiki/masters/`, `Wiki/synthesis/`, `Wiki/texts/` subfolders vs
  `CLAUDE.md`'s documented schema — decide whether to formalize or consolidate
- [ ] `C:\Vault\.claude\commands\parallel-sync.md` hardcodes `find /c/Vault` instead of
  `find /c` — misses Bazi/TicketBots/TicketBotsWeb when run as a fleet-wide discovery;
  fix in Vault, then re-sync to Bazi
- [ ] 272 pre-existing lint issues in Bazi's `Wiki/` content (see Verified Facts) — not
  urgent, candidate for `/wiki-batch-expand` or `/nightly-pipeline`

---

## Convention Reminders

- Filenames: `lowercase-hyphens.md` — never PascalCase or spaces
- Wiki location: `C:\Bazi\wiki\{sources,concepts,entities,queries}\`
- Lint before committing: `python C:/Vault/tools/lint_wiki.py C:/Bazi` — must show Clean
- Commit prefix: `[claude]` or `[codex]`
- Update `COLLAB.md` at session end: release In Progress row, update Latest Handoff, add Done item
