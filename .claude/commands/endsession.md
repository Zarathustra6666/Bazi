---
name: endsession
description: >
  End-of-session cleanup for the Bazi repo: lint `C:\Bazi`, clean up any checkpoint,
  commit, push, and confirm the remote landed. Trigger on: /endsession, "end session",
  "wrap up", "finish session", "close session".
---

# /endsession - End-of-Session Cleanup

Run this after a Bazi session that produced file changes.

## Steps

### 0. Connectivity Check

```bash
git -C "C:/Bazi" ls-remote --exit-code origin HEAD
```

If the remote is unreachable, report it and continue with local lint/status only.

### 1. Lint

Run:

```bash
python C:/Vault/tools/lint_wiki.py C:/Bazi
```

Fix any issues in Bazi files only. Re-run until clean or until you hit a real blocker.

### 2. Checkpoint Cleanup

If `C:\Bazi\session-checkpoint.md` exists and the task is complete, delete it.

### 3. Repo Status

Detect branch and current changes:

```bash
BRANCH=$(git -C "C:/Bazi" rev-parse --abbrev-ref HEAD)
git -C "C:/Bazi" status --short
```

### 4. Commit and Push

Stage files by name, not `-A`.

If `.obsidian/workspace.json` is dirty, stash before pull/rebase and pop after push.

```bash
git -C "C:/Bazi" add <changed files by name>
git -C "C:/Bazi" commit -m "<descriptive message>"
git -C "C:/Bazi" pull --rebase origin "$BRANCH"
git -C "C:/Bazi" push origin "$BRANCH"
git -C "C:/Bazi" log "origin/$BRANCH" -1 --oneline
```

If rebase conflicts, stop and ask: `take ours / take theirs / manual?`

### 5. Summary

Report:

```text
Bazi endsession:
  lint: clean / blocked
  checkpoint: deleted / not found
  push: confirmed <hash> / unconfirmed
```
