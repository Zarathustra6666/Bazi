---
name: sync
description: >
  Single-repo git sweep for C:\Vault: detects current branch dynamically, checks for
  changes, verifies output files are not gitignored, commits with a descriptive message,
  pulls --rebase, pushes, and verifies the commit landed on the remote.
  Use at the end of any session that produced file changes. Trigger on: /sync,
  "sync all repos", "commit and push everything", "git sweep".
---

# /sync — Vault Git Sweep

Commit and push all changes in the single vault repo at `C:\Vault`.

**Repo:** `C:\Vault` → `origin/<current-branch>` (https://github.com/Zarathustra6666/Vault.git)

---

## Steps

### 0. Detect current branch

```bash
BRANCH=$(git -C "C:/Vault" rev-parse --abbrev-ref HEAD)
```

Use `$BRANCH` in all subsequent git commands — never hardcode `master` or `main`.

### 1. Status check

```
git -C "C:\Vault" status --ignored --short
```

Report modified, untracked, and ignored files. Skip `.obsidian/workspace.json` — it is Obsidian UI state and should never be committed.

### 2. Gitignore guard

Before staging anything, scan the ignored files list for output file types:
`*.docx`, `*.xlsx`, `*.html`, `*.pdf`, `*.ipynb`, `*.csv`

If any output file appears as ignored (`!!`):
- Stop. Do not commit.
- Show which file is ignored.
- Fix `.gitignore` first, then re-run `/sync`.

### 3. Stage and commit

Stage everything except `.obsidian/workspace.json`. Use explicit exclusion so the unstage never errors even if workspace.json wasn't staged:

```
git -C "C:\Vault" add -A
git -C "C:\Vault" restore --staged .obsidian/workspace.json 2>$null; $true
git -C "C:\Vault" commit -m "<descriptive message>"
```

Write a commit message that describes what changed (wiki pages added, analysis run, skill updated, etc.) — not just "update files".

### 4. Pull --rebase then push

Check for unstaged changes before stashing — only stash if there is something to stash:

```bash
dirty=$(git -C "C:/Vault" diff --name-only)
if [ -n "$dirty" ]; then git -C "C:/Vault" stash; fi
git -C "C:/Vault" pull --rebase origin "$BRANCH"
git -C "C:/Vault" push origin "$BRANCH"
if [ -n "$dirty" ]; then git -C "C:/Vault" stash pop; fi
```

If pull --rebase fails (conflict), stop and report the conflict files before pushing — never auto-resolve.

### 5. Verify push landed on remote

```bash
git -C "C:/Vault" log "origin/$BRANCH" -1 --oneline
```

Capture the hash and compare to the commit hash from Step 3. If they differ, flag as **"push unconfirmed"** and re-run Step 4.

### 6. Summary report

```
Vault (<branch>)  ✓ pushed  abc1234 — <commit message first line>
```

---

## Usage

```
/sync
/sync   (after firesearch or ingest)
/sync   (end of session)
/sync skill   → update this skill file
```
