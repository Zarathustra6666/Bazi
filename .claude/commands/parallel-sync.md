---
name: parallel-sync
description: >
  Parallel multi-repo sync fleet. Discovers all git repos under `C:\` dynamically,
  syncs each changed repo in parallel, and reports a unified dashboard. Trigger on:
  /parallel-sync, "sync all repos", "parallel sync", "sync everything".
---

# /parallel-sync - Parallel Multi-Repo Sync Fleet

Use this for cross-repo sync work. Discovery must start at `C:\`, not `C:\Vault`.

## Steps

### 1. Discover All Repos

```bash
find /c -maxdepth 2 -name ".git" -type d | sed 's|/.git$||' | sort
```

### 2. Check Each Repo

```bash
git -C "<repo>" status --short
git -C "<repo>" rev-parse --abbrev-ref HEAD
```

Skip clean repos.

### 3. Sync Changed Repos

For each changed repo:
- lint the repo if it contains wiki content
- stage files by name
- commit with a descriptive message
- pull `--rebase`
- push
- confirm with `git log --oneline -3`

If any repo conflicts, stop that repo and ask the user how to resolve it, but keep the
other repos' results in the final report.

### 4. Report

Use example output like:

```text
C:\Vault         OK   master
C:\Bazi          OK   master
C:\TicketBots    SKIP main
C:\Vault\Z       CONFLICT master
```
