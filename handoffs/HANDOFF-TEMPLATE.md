# Handoff — <Task Title>

> From: claude / codex
> To: claude / codex
> Date: YYYY-MM-DD HH:MM
> Related commit(s): `<hash> <message>`
> Related handoff(s): `handoffs/<prior-handoff>.md` (or "none")

---

## Claim

One short statement of what changed or what is being requested.

---

## Verified Facts

List every factual claim about local state. Each fact must include the command or file read used to verify it. Do not state something as fact if you inferred it.

- **Fact:** <e.g. file exists at path X>
  **Evidence:** `find /c/Bazi -name "filename.md"` → `/c/Bazi/wiki/concepts/filename.md`

- **Fact:** <e.g. lint is clean>
  **Evidence:** `python C:/Vault/tools/lint_wiki.py C:/Bazi` → `[lint] Clean — N pages checked`

- **Fact:** <e.g. push landed on remote>
  **Evidence:** `git log origin/master -1 --oneline` → `<hash> <message>`

---

## Interpretation

What the verified facts appear to imply — clearly separated from the facts above.

---

## Open Questions

Anything not yet verified. The receiving agent should resolve these before acting on them.

- [ ] ...

---

## Files Touched

- `path/to/file.md` — reason

---

## Commands Run

- `command` — result summary

---

## Next Action

One concrete next step for the receiving agent, specific enough to start immediately.

---

## Correction (include only when correcting a prior handoff)

> Correction of: `handoffs/<filename>.md`
> Wrong claim: ...
> Verified replacement: ...
> Evidence: ...

---

## Session Accomplishments (include for full session handoffs; omit for task-scoped ones)

- bullet: what was completed — `path/to/file.md`

---

## Resume From Here (include if task is incomplete; omit if done)

**Next step:** [exact action]
**Files to read first:** [`path/to/file.md`]
**Decisions already made:** [so partner doesn't re-litigate]
**Blockers:** [anything the partner cannot proceed without]

---

## Open Items Added to Queue

- [ ] item — `path/to/relevant/file.md`

---

## Convention Reminders

- Filenames: `lowercase-hyphens.md` — never PascalCase or spaces
- Wiki location: `C:\Bazi\wiki\{sources,concepts,entities,queries}\`
- Lint before committing: `python C:/Vault/tools/lint_wiki.py C:/Bazi` — must show Clean
- Commit prefix: `[claude]` or `[codex]`
- Update `COLLAB.md` at session end: release In Progress row, update Latest Handoff, add Done item
