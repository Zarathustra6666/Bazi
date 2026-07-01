---
name: wiki-heal
description: >
  Self-healing wiki pipeline: lint and fix the active wiki, detect concept/entity gaps,
  research and draft missing pages via WebSearch (MCP fallback), update index and log,
  then commit and push. Stops on merge conflicts and surfaces them to the user.
  Trigger on: /wiki-heal, "self-heal wiki", "auto-maintain wiki", "heal the wiki".
---

# /wiki-heal — Self-Healing Wiki Pipeline

Runs unattended: lint → fix → gap detection → research stubs → index/log update → commit.
Stops only when a merge conflict requires user judgment.

---

## When to invoke

- `/wiki-heal` — full pipeline run on the active wiki
- "self-heal wiki", "auto-maintain wiki", "heal the wiki"
- Scheduled: safe to run on a cron/schedule, idempotent

---

## Steps

### 0. Orient

1. Read `index.md` and last 5 `log.md` entries
2. Identify active wiki root (default: `C:\Vault\Z\Wiki\` or wiki closest to cwd)

### 1. Checkpoint

Write `session-checkpoint.md` before starting (per CLAUDE.md checkpoint protocol):
- task: "wiki-heal pipeline"
- step 1 of 6

### 2. Lint pass

Run the full lint check (per `/lintfix` logic):
- Broken WikiLinks — every `[[Target]]` must resolve to a `title:` in the wiki
- Orphan pages — every page must appear as a link target in at least one other page
- Frontmatter errors — flag pages missing `title`, `type`, `tags`, `created`, `updated`
- Misplaced files — `type:` field must match directory
- index.md gaps — pages in `Wiki/` but absent from `index.md`

Fix all issues found. Re-run (cap at 3 iterations). If still failing after 3, report remaining issues and continue.

Update checkpoint → step 2 done.

### 3. Gap detection

Scan all wiki pages for entity and concept names that appear in `[[WikiLink]]` syntax but have **no corresponding page** in `Wiki/entities/` or `Wiki/concepts/`. These are stubs.

Collect a gap list: `[[Name]] — mentioned in N pages, no page exists`.

If gap list is empty, skip to step 5.

Update checkpoint → step 3 done.

### 4. Research and draft missing pages

For each gap (up to 5 per run to stay within session limits):

1. Run 2 WebSearch queries to gather core facts about the entity/concept
   - If NotebookLM MCP is available, use it; if it errors or stalls once, fall back to WebSearch immediately
2. Draft a stub page using the appropriate template from CLAUDE.md
3. Write to `Wiki/entities/<slug>.md` or `Wiki/concepts/<slug>.md`
4. Add bidirectional links from the pages that mentioned it

Mark gaps with fewer than 3 facts as `[STUB — needs enrichment]` rather than fabricating content.

If 5+ gaps remain after the run, log "N gaps deferred — run /wiki-heal again to continue."

Update checkpoint → step 4 done.

### 5. Update index and log

- Add each new stub page to `index.md` under the correct category
- Append one `log.md` entry:
  ```
  ## [YYYY-MM-DD] update | Wiki Heal — N fixes, M stubs drafted
  - Lint: [summary of issues fixed]
  - Gaps: [list of new stub pages, or "none"]
  - Deferred: [gaps not yet researched, or "none"]
  ```

Update checkpoint → step 5 done.

### 6. Commit and push

**Before committing, run one final lint pass** to confirm the new pages didn't introduce issues.

Stage all changed files by name — not `git add -A`. Commit:

```
git add [list of changed files]
git commit -m "wiki-heal: [N] lint fixes, [M] stubs drafted ([date])"
```

Pull --rebase then push:

```
git pull --rebase origin master
git push origin master
```

**If pull --rebase produces a conflict:**
- Stop immediately
- Show the conflicting files
- Ask the user: "take ours / take theirs / manual?" — do not auto-resolve

After a clean push: delete `session-checkpoint.md`.

---

## Output report

```
Wiki Heal — [date]
  Lint fixes:   N
  Stubs drafted: M  ([list of new page titles])
  Gaps deferred: K  (run /wiki-heal again)
  Status: ✓ pushed  |  ⚠ stopped at merge conflict
```

---

## Failure handling

| Failure | Action |
|---------|--------|
| MCP disconnects | Fall back to WebSearch immediately; note in log |
| WebFetch stalls after 1 attempt | Skip that URL; continue with other sources |
| Lint fails after 3 iterations | Commit clean pages; report remaining lint issues |
| Merge conflict on push | Stop; surface conflict files to user |
| Session limit hit mid-run | Checkpoint preserves progress; resume with /wiki-heal |
