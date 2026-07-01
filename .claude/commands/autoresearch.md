---
name: autoresearch
description: >
  Autonomous research loop for the Bazi wiki. Runs configured topic checks against
  `C:\Bazi\wiki`, stages digests for review, and commits only after a Bazi-local lint
  pass. Trigger on: /autoresearch, /autoresearch [topic-id], /autoresearch apply,
  /autoresearch status.
---

# /autoresearch - Autonomous Research Loop

Run a configured research loop for Bazi topics only. This command does not touch
`C:\Vault\Wiki`, `C:\Vault\md`, or any other vault content.

## Invocation Modes

```text
/autoresearch
/autoresearch [topic-id]
/autoresearch apply
/autoresearch status
```

## Configuration Files

- `C:\Bazi\.autoresearch\program.md` - research agenda and topic definitions
- `C:\Bazi\.autoresearch\run-log.tsv` - run history and calibration notes
- `C:\Bazi\.autoresearch\pending-review\` - staged digests awaiting review

If `program.md` does not exist, stop and ask the user to initialize the Bazi
autoresearch program before continuing.

## Loop Rules

1. Read `program.md` and `run-log.tsv`.
2. Evaluate only Bazi-target pages under `C:\Bazi\wiki\`.
3. Use WebSearch first; use NotebookLM only if the session has already passed `/preflight`
   or the user explicitly asked for NLM-backed research.
4. Stage digests into `C:\Bazi\.autoresearch\pending-review\`.
5. On `/autoresearch apply`, update only `C:\Bazi\wiki\*`, `C:\Bazi\index.md`, and `C:\Bazi\log.md`.
6. After any write, run:

```bash
python C:/Vault/tools/lint_wiki.py C:/Bazi
```

7. Commit and push only the `C:\Bazi` repo:

```bash
BRANCH=$(git -C "C:/Bazi" rev-parse --abbrev-ref HEAD)
git -C "C:/Bazi" add <changed files by name>
git -C "C:/Bazi" commit -m "autoresearch: <summary>"
git -C "C:/Bazi" pull --rebase origin "$BRANCH"
git -C "C:/Bazi" push origin "$BRANCH"
git -C "C:/Bazi" log "origin/$BRANCH" -1 --oneline
```

## Guardrails

- Never read or write `C:\Vault\.autoresearch\`.
- Never lint `C:\Vault`; lint `C:\Bazi` only.
- Never assume multi-wiki Bazi/BankProfile/Z behavior.
- If the topic definition points outside `C:\Bazi`, stop and ask the user whether that
  topic belongs in another repo instead.
