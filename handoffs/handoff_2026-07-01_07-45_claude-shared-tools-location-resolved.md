# Handoff — Resolved: "Should shared tools move out of C:\Vault\tools?"

> From: claude
> To: codex
> Date: 2026-07-01 07:45
> Related commit(s): `C:\Vault a5b85c3` (fix commit), pending local commit in `C:\Bazi` (settings.json + .gitignore)
> Related handoff(s): `handoffs/handoff_2026-07-01_07-32_claude-firesearch-question-resolved.md`

---

## Claim

Picked up your second open question: whether shared-tool commands should move out of
`C:\Vault\tools\` into a neutral location. Asked the user directly — decision: **keep
tools in `C:\Vault\tools`, don't migrate.** While investigating the tradeoffs, found and
fixed a real bug: `session_state.py` hardcoded `C:\Vault` internally, so the
`UserPromptSubmit`/`Stop` hooks I wired into Bazi's `settings.json` during the earlier
parity session were silently reading/writing **Vault's** `session-state.json`, not
Bazi's. The hook fired without erroring, so this went unnoticed until now.

---

## Verified Facts

- **Fact:** `session_state.py` had `VAULT_ROOT = Path("C:/Vault")` hardcoded, used for
  `STATE_PATH`, `BANNER_HASH_PATH`, `CHECKPOINT_PATH`, and the `git -C <path> status`
  target inside `_uncommitted_count()`.
  **Evidence:** direct read of `C:\Vault\tools\session_state.py` (pre-fix), lines 24–28
  and 94.

- **Fact:** Neither Vault's nor Bazi's `.claude/settings.json` passed any argument to
  `session_state.py load`/`dump` — the hooks called it bare, so the hardcoded default
  was the only path it ever used, for either repo.
  **Evidence:** pre-fix read of both `settings.json` files, `UserPromptSubmit` and
  `Stop` hook commands.

- **Fact:** `wait_and_resume.py` had a similar but lower-severity issue — a hardcoded
  read of `C:/Vault/session-state.json` used only for a cosmetic "[resume] Restoring:
  ..." print. The core wait-then-`claude --continue` logic never depended on it.
  **Evidence:** line 85 of the pre-fix file; `wait_and_resume.ps1` (the PowerShell
  counterpart) has no such dependency at all — confirmed by full read, no `C:\Vault`
  reference anywhere in it.

- **Fact:** `quick_check.py` and `kb_sync_diff.py` also hardcode `C:/Vault` internally,
  but neither is referenced anywhere in Bazi's `.claude/` or `CLAUDE.md`/`AGENTS.md` —
  confirmed Vault-only tools, out of scope for this fix.
  **Evidence:** `grep -rn "quick_check\|kb_sync_diff" C:\Bazi\.claude C:\Bazi\CLAUDE.md
  C:\Bazi\AGENTS.md` → no matches.

- **Fact:** Of the 7 tool scripts actually invoked cross-repo (`agent_journal.py`,
  `check_nlm_auth.py`, `lint_wiki.py`, `research_orchestrator.py`, `session_state.py`,
  `usage_planner.py`, `wait_and_resume.py`), only `session_state.py` and (cosmetically)
  `wait_and_resume.py` had the hardcoding bug. `lint_wiki.py` already takes the target
  path as an argument; `check_nlm_auth.py` points at a user-level auth file, not a repo
  path; `agent_journal.py`/`research_orchestrator.py` are `Path(__file__).parent`-relative
  (correctly always resolve to `C:\Vault\tools\`, which is intentional — the agent
  journal and research ledger are genuinely shared cross-repo state); `usage_planner.py`
  hardcodes its own config path but that's correct too, since usage quota is one
  account-wide resource, not a per-repo concept.
  **Evidence:** direct reads of all 7 scripts (done in this session and the prior
  parity session).

- **Fact:** Fix verified working — `python C:/Vault/tools/session_state.py dump
  C:/Vault` and `dump C:/Bazi` produced two independently-correct
  `session-state.json` files (`uncommitted_files: 6` for Vault vs `1` for Bazi at time
  of test, matching each repo's actual `git status --short` count). Misuse (missing or
  unknown args) still exits 0 without crashing a hook — confirmed by direct invocation
  with no args and with a bogus subcommand.
  **Evidence:** commands run this session, output pasted below.

- **Fact:** Bazi's `.gitignore` was missing `session-state.json` and
  `session-banner-hash.txt` entries (present in Vault's `.gitignore` since the earlier
  parity session, but I missed adding them to Bazi's — the gap didn't matter before
  since the hook never actually wrote to `C:\Bazi\` due to the bug above; now that it's
  fixed, the gap was live). Fixed in the same pass.
  **Evidence:** `grep -n "session-state\|session-banner" C:\Bazi\.gitignore
  C:\Vault\.gitignore` — pre-fix, only Vault's had the entries.

---

## Interpretation

The "shared tools location" question and this bug are related but distinct. Keeping
tools physically in `C:\Vault\tools` (the user's choice) means Bazi still has a hard
dependency on `C:\Vault` existing on the machine — that coupling is unchanged and
accepted, not eliminated. What changed is that the coupling is now *correct*: Bazi's
hooks operate on Bazi's own state instead of silently touching Vault's. If the user
ever wants to revisit relocating the tools (new sibling repo, or `~/.claude/tools`),
the script is now in the right shape for that — it already takes an explicit repo-root
argument rather than assuming its own location.

---

## Open Questions

Your third one is still open — not picked up:
- [ ] Whether to normalize remaining explanatory (non-load-bearing) `C:\Vault`
  references for style.

---

## Files Touched

**In `C:\Vault`** (commit `a5b85c3`):
- `tools/session_state.py` — removed hardcoded `VAULT_ROOT`; `dump`/`load` now require
  an explicit `<repo_root>` positional argument; `research_ledger.json`/
  `agent_journal.json` stay `Path(__file__).parent`-relative (correct, shared state)
- `tools/wait_and_resume.py` — cosmetic banner now reads `Path.cwd()/session-state.json`
- `.claude/settings.json` — hooks now pass `C:/Vault` explicitly

**In `C:\Bazi`** (this handoff's companion commit):
- `.claude/settings.json` — hooks now pass `C:/Bazi` explicitly
- `.gitignore` — added missing `session-state.json` / `session-banner-hash.txt` entries
- `COLLAB.md` — Done entry + Latest Handoff row

---

## Commands Run

```
python C:/Vault/tools/session_state.py dump C:/Vault
→ {"uncommitted_files": 6, ...}  (matched git status --short -C C:/Vault)

python C:/Vault/tools/session_state.py dump C:/Bazi
→ {"uncommitted_files": 1, ...}  (matched git status --short -C C:/Bazi)

python C:/Vault/tools/session_state.py load          # no repo_root
→ prints usage, exit 0, no crash

python C:/Vault/tools/session_state.py bogus C:/Vault  # unknown subcommand
→ prints usage, exit 0, no crash
```

---

## Next Action

Nothing blocking. The one remaining open question from your original handoff (style
normalization of non-load-bearing `C:\Vault` references) is low-stakes — pick it up
whenever, or leave it queued.

---

## Convention Reminders

- Filenames: `lowercase-hyphens.md` — never PascalCase or spaces
- Wiki location: `C:\Bazi\wiki\{sources,concepts,entities,queries}\`
- Lint before committing: `python C:/Vault/tools/lint_wiki.py C:/Bazi` — must show Clean
- Commit prefix: `[claude]` or `[codex]`
- Update `COLLAB.md` at session end: release In Progress row, update Latest Handoff, add Done item
