---
name: firesearch
description: >
  Bank firesearch belongs outside the Bazi repo. This command exists here only for
  command-set parity and should redirect the user to the finance-oriented vault instead
  of writing bank research into `C:\Bazi`.
---

# /firesearch - Redirect Out of Bazi

This repo is for Bazi content. Do not write DPA-bank or BankProfile research into
`C:\Bazi\wiki`.

> **Why this stub exists (do not delete):** there is a global `firesearch` skill at
> `~/.claude/skills/firesearch/SKILL.md` (also mirrored in `C:\Vault\.claude\skills\`)
> that triggers on Thai-bank phrases ("ทำ ธ. [bank]", "deep dive [bank]", or a bare DPA
> bank name like SCB/KTB/BAY) and writes into `C:\Vault\md\Wiki\entities\`. Global
> skills only yield to a local one when a same-named local skill exists in the current
> repo's `.claude/commands/` or `.claude/skills/`. Without this local override, that
> global bank-research skill is what actually fires when `/firesearch` (or a matching
> Thai trigger phrase) is invoked from a Bazi session — silently doing Thai-bank
> research in the wrong repo. This stub is the interception point, not a redundant
> command-set-parity placeholder.

## Behavior

When invoked from `C:\Bazi`:

1. Explain that `/firesearch` is a finance/bank-research workflow and is out of scope for
   the Bazi wiki.
2. Ask the user whether they want to switch to the finance-oriented repo before doing any work.
3. Do not create or update files under `C:\Bazi` for bank firesearch content.

## Allowed References

- It is acceptable to point the user to the finance-oriented repo or vault that owns bank
  research.
- It is not acceptable to treat `C:\Bazi` as a BankProfile target.
