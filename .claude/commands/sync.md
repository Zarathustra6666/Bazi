---
name: sync
description: >
  Single-repo git sweep for `C:\Bazi`: detects the current branch dynamically, checks
  for changes, commits with a descriptive message, pulls --rebase, pushes, and verifies
  that the commit landed on the remote.
---

# /sync - Bazi Git Sweep

Commit and push changes in `C:\Bazi` only.

## Steps

### 0. Detect Current Branch

```bash
BRANCH=$(git -C "C:/Bazi" rev-parse --abbrev-ref HEAD)
```

### 1. Status Check

```bash
git -C "C:/Bazi" status --ignored --short
```

Skip `.obsidian/workspace.json` unless the user explicitly asked to include it.

### 2. Gitignore Guard

Before staging, inspect ignored output artifacts. If a file that should be committed is
ignored, stop and fix `.gitignore` first.

### 3. Stage and Commit

Stage files by name. Do not use `git add -A`.

```bash
git -C "C:/Bazi" add <changed files by name>
git -C "C:/Bazi" commit -m "<descriptive message>"
```

### 4. Pull and Push

```bash
git -C "C:/Bazi" pull --rebase origin "$BRANCH"
git -C "C:/Bazi" push origin "$BRANCH"
```

If the rebase conflicts, stop and ask the user how to resolve it.

### 5. Verify Remote

```bash
git -C "C:/Bazi" log "origin/$BRANCH" -1 --oneline
```

Compare the remote hash with the local commit hash and report whether the push is
confirmed.
