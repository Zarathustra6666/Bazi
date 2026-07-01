---
name: parallel-sync
description: >
  Parallel multi-repo sync fleet. Discovers all git repos under C:\Vault dynamically,
  spawns one subagent per repo, each linting and pushing, then reports a unified status
  dashboard. Never hardcodes the repo list. Trigger on: /parallel-sync,
  "sync all repos", "parallel sync", "sync everything".
---

# /parallel-sync — Parallel Multi-Repo Sync Fleet

Discovers all git repos dynamically, syncs them in parallel, reports a unified dashboard.

---

## Steps

### 1. Discover All Repos

```bash
find /c/Vault -maxdepth 3 -name ".git" -type d | sed 's|/.git$||' | sort
```

Report all found repos. Never use a hardcoded list — always discover dynamically.

### 2. Check Each Repo for Changes

For each repo, run:

```bash
git -C "<repo>" status --short
```

Skip repos with no changes (clean working tree and no commits ahead of remote).

### 3. Spawn Parallel Subagents

For each repo **with changes**, spawn one Agent in parallel. Pass the repo path and branch.

Each subagent must:

1. **Check for wiki files** — if `Wiki/` or wiki-style `.md` directories exist, run lint:
   - Broken WikiLinks: compare index.md `[[links]]` against file titles + stems
   - Orphan pages: files not referenced in index.md
   - Fix any issues found

2. **Stage files by name** (not `-A`):
   - Skip `.obsidian/workspace.json`
   - Include all modified `.md` wiki pages, `index.md`, `log.md`

3. **Commit** with a descriptive message summarising what changed

4. **Pull --rebase** the remote branch:
   - If conflict: **stop**, report conflict files, set status = CONFLICT, do not push

5. **Push** if rebase succeeded

6. **Confirm** with `git log --oneline -3`

7. **Return** a one-line status summary: `<repo_path>  ✓/✗  <branch>  (<N files changed>)`

### 4. Coordinator: Aggregate Results

Wait for all subagents to complete, then print the status dashboard:

```
=== Parallel Sync Report — YYYY-MM-DD HH:MM ===

  C:\Vault          ✓  master  (15 files changed)
  C:\Bazi           ✓  master  (3 files changed)
  C:\Vault\md       ✓  master  (no changes — skipped)
  C:\Vault\Z        ✗  master  CONFLICT in Wiki/concepts/foo.md

CONFLICTS (1):
  C:\Vault\Z — Wiki/concepts/foo.md
  → Action needed: "take ours / take theirs / manual?"

Total: 3 pushed, 1 conflict, 0 errors
```

### 5. Resolve Conflicts (if any)

For each conflict repo, show the conflict file(s) and ask:
> `Conflict in <file>: take ours / take theirs / manual?`

Apply the resolution, commit, and push only after user confirmation.

---

## Conflict Resolution Policy

- **Config-only conflicts** (`.obsidian/`, `.vscode/`, etc.): take ours automatically
- **Wiki content conflicts**: always ask the user — never auto-resolve
- **Merge commit vs rebase**: prefer rebase; if rebase fails 2+ times, switch to `pull --merge`

---

## Usage

```
/parallel-sync
```

Tip: use `/endsession` for the full end-of-session flow (lint + parallel-sync + checkpoint cleanup).
