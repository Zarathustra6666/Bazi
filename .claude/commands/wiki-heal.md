---
name: wiki-heal
description: >
  Self-healing wiki pipeline for Bazi: lint and fix `C:\Bazi\wiki`, detect missing
  pages, research and draft stubs, update `index.md` and `log.md`, then commit and
  push. Trigger on: /wiki-heal, "self-heal wiki", "auto-maintain wiki", "heal the wiki".
---

# /wiki-heal - Self-Healing Wiki Pipeline

Runs unattended against `C:\Bazi` only.

## Steps

### 0. Orient

1. Read `C:\Bazi\index.md` and the last 5 entries of `C:\Bazi\log.md`.
2. Set the active wiki root to `C:\Bazi\wiki\`.

### 1. Checkpoint

Write `C:\Bazi\session-checkpoint.md`.

### 2. Lint Pass

Run:

```bash
python C:/Vault/tools/lint_wiki.py C:/Bazi
```

Fix Bazi-local issues only. Re-run up to 3 times.

### 3. Gap Detection

Find unresolved links or missing concept/entity pages under `C:\Bazi\wiki\`.

### 4. Draft Missing Pages

Write new pages only under:
- `C:\Bazi\wiki\entities\`
- `C:\Bazi\wiki\concepts\`

Update backlinks in Bazi pages only.

### 5. Update Index and Log

Append updates to `C:\Bazi\index.md` and `C:\Bazi\log.md`.

### 6. Commit and Push

```bash
BRANCH=$(git -C "C:/Bazi" rev-parse --abbrev-ref HEAD)
git -C "C:/Bazi" add <changed files by name>
git -C "C:/Bazi" commit -m "wiki-heal: <summary>"
git -C "C:/Bazi" pull --rebase origin "$BRANCH"
git -C "C:/Bazi" push origin "$BRANCH"
```

If conflicts appear, stop and ask the user how to resolve them.
