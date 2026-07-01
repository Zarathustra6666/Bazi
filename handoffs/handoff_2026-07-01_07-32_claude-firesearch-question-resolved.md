# Handoff — Resolved: "Should /firesearch stay as a redirect stub in Bazi?"

> From: claude
> To: codex
> Date: 2026-07-01 07:32
> Related commit(s): pending local commit (this handoff + `firesearch.md` doc update + `COLLAB.md`)
> Related handoff(s): `handoffs/handoff_2026-07-01_07-18_codex-command-parity-cleanup.md`

---

## Claim

Picked up the first of your three Open Questions: whether `/firesearch` should remain
as a redirect-only command in Bazi or be removed. Answer: **keep it, don't remove it.**
Removing it would reopen a real misfire risk. Documented the reasoning inline in the
file so it doesn't get "cleaned up" as dead weight in a future pass.

---

## Verified Facts

- **Fact:** A global `firesearch` skill exists at
  `C:\Users\user\.claude\skills\firesearch\SKILL.md` (332 lines), separate from both
  Vault's and Bazi's local `.claude/commands/firesearch.md`.
  **Evidence:** direct file read of `~/.claude/skills/firesearch/SKILL.md`.

- **Fact:** That global skill is a Thai-bank/DPA-member deep-dive workflow. It triggers
  on `/firesearch [FI]` **and** on plain Thai phrases ("ทำ ธ. [ชื่อธนาคาร]", "deep dive
  [ธนาคาร]", "ค้นคว้า [สถาบันการเงิน]") and on bare DPA bank names (SCB, KTB, BAY,
  Krungsri, CIMBT, ICBCT, TISCO, GSB, BAAC, GHB, SME Bank, Citibank, HSBC, Deutsche
  Bank, BNP Paribas, JPMorgan, BOA, OCBC, Standard Chartered — per its frontmatter
  `description:` trigger list).
  **Evidence:** frontmatter block, lines 3–15 of that file.

- **Fact:** That global skill writes into `C:\Vault\md\Wiki\entities\` and drives a
  hardcoded NotebookLM session workflow (hardcoded notebook IDs per bank, a hardcoded
  local session ID `local_57201435-...` for `vault_session`). None of this is
  Bazi-aware or repo-scoped — it always targets the Vault MD wiki.
  **Evidence:** lines 6, 25–29, 251–266 of that file.

- **Fact:** `C:\Vault` also has a project-scoped copy at
  `C:\Vault\.claude\skills\firesearch\SKILL.md`, separate again from
  `C:\Vault\.claude\commands\firesearch.md` (the BankProfile-flavored command you
  found stale references in during your cleanup — different file, same name).
  **Evidence:** `ls -la /c/Vault/.claude/skills/firesearch/`.

- **Fact:** Bazi's local `.claude/commands/firesearch.md` (your redirect-only rewrite)
  is the only thing standing between a Bazi session and that global skill firing.
  **Evidence:** interpreted from the Skill-tool resolution rule stated in this
  environment's tool docs — "most specific directory wins" when a local and global
  skill share a name — combined with the fact above that no other local override exists.

---

## Interpretation

Your redirect stub isn't a leftover "command-set parity placeholder" — it's the
interception point that prevents a heavyweight, hardcoded-path, Thai-bank research
skill from silently activating in an astrology repo. If someone in a Bazi session types
a bare bank name or a Thai research phrase out of habit (plausible, since the same
person also works DPA/bank research in Vault), the global skill would otherwise run and
write bank data into `C:\Vault\md\Wiki\entities\` while the user thinks they're in Bazi
context. Removing the stub would silently restore that risk.

I didn't find evidence this was reasoned through in the original parity session (mine)
or your cleanup — both of us treated it as a generic "does this command make sense
here" question without checking whether a global fallback existed. Worth remembering
as a pattern: before deciding "remove this Bazi-irrelevant command," check
`~/.claude/skills/` for a same-named global skill first.

---

## Open Questions

Your other two are still open — I did not pick these up:
- [ ] Whether shared-tool commands should eventually move helpers out of
  `C:\Vault\tools\` into a neutral shared location.
- [ ] Whether to normalize remaining explanatory (non-load-bearing) `C:\Vault`
  references for style.

---

## Files Touched

- `C:\Bazi\.claude\commands\firesearch.md` — added a `> **Why this stub exists**` block
  explaining the global-skill interception rationale (no behavioral change, doc-only)
- `C:\Bazi\COLLAB.md` — added Done entry, updated Latest Handoff row

---

## Commands Run

- `grep -n "firesearch" /c/Vault/.claude/skills/firesearch/SKILL.md` — confirmed the
  skill's existence and scope
- `ls -la ~/.claude/skills/firesearch/` and `ls -la /c/Vault/.claude/skills/firesearch/`
  — confirmed both global and Vault-local copies exist

---

## Next Action

Nothing blocking. Pick up either of the two remaining open questions above if you want
to continue the command-cleanup thread, or leave them queued — they're lower-stakes
(style/location, not a correctness risk like the firesearch one was).

---

## Convention Reminders

- Filenames: `lowercase-hyphens.md` — never PascalCase or spaces
- Wiki location: `C:\Bazi\wiki\{sources,concepts,entities,queries}\`
- Lint before committing: `python C:/Vault/tools/lint_wiki.py C:/Bazi` — must show Clean
- Commit prefix: `[claude]` or `[codex]`
- Update `COLLAB.md` at session end: release In Progress row, update Latest Handoff, add Done item
