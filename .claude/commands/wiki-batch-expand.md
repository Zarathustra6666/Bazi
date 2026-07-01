# /wiki-batch-expand

Parallel stub-expansion swarm. Discovers stub wiki pages, spawns parallel `stub-researcher` subagents (one per stub per batch), self-scores each result, writes approved pages, and commits a clean lint-passing batch.

## Trigger

`/wiki-batch-expand [--domain <tag>] [--max <N>]`

Options:
- `--domain <tag>`: filter to pages whose `tags:` frontmatter contains the tag
- `--max <N>`: cap total stubs processed this run (default: 9)

Also triggers on: "expand stubs", "batch expand wiki", "expand all stubs"

## When to Use

- Vault has stub pages from `/expand` or `wiki-quality-loop` gap-fill
- You want to enrich multiple stubs in one session instead of one at a time

## When Not to Use

- NLM MCP auth is expired (run `/preflight` first)
- Another agent has claimed overlapping pages in COLLAB.md

---

## Step 1 — Discover Stubs

Scan `C:\Bazi\wiki\**\*.md` for stub pages. A page qualifies if ANY of:
- `tags:` frontmatter contains `stub`
- Page body has fewer than 3 non-empty, non-header lines after stripping YAML frontmatter
- First body line contains `[STUB]`

If the strict scan returns 0 results, **fall back to thin-page mode**: include any page with fewer than 12 non-empty non-header body lines. Present the thin candidates with a note: "(no strict stubs found — showing thin pages as expansion candidates)".

Apply `--domain` filter if provided. Apply `--max` cap (default 9), preferring pages with fewest body lines.

## Step 2 — Present List and Confirm

Print a table (path, topic, tags, line count). Ask "Expand these N stubs? [y/N]" and wait. Exit without changes if user says no.

## Step 3 — Claim COLLAB.md

Add In Progress row to `C:\Bazi\COLLAB.md`:

```
| wiki-batch-expand -- N stubs | Claude | YYYY-MM-DD | running | -- |
```

## Step 4 — Write Checkpoint

Write `C:\Bazi\session-checkpoint.md` with task, step_next = "batch-loop", progress checkboxes for each phase.

## Step 5 — Batch Loop

Process stubs in batches of at most 3. For each batch:

1. **Spawn parallel `stub-researcher` subagents** -- one per stub. Pass: `stub_path`, `topic` (from frontmatter title), `domain` (if --domain provided).

2. **Collect results** -- wait for all agents' `### STUB-RESULT:` blocks.

3. **Route by score**:
   - APPROVED (total >= 8): add to write queue
   - FLAGGED (5--7): log to flagged list; do NOT write
   - SKIP (< 5): log to skipped list; do NOT write

4. **Write approved pages immediately** to their `stub_path` (write-as-you-go, not accumulated).

5. **Update checkpoint** after each batch.

## Step 6 — Merge Step

Single coordinator pass across all written pages:

1. **WikiLink validation**: for each `[[WikiLink]]` in new pages, verify target file exists. If missing: convert to plain text and note in commit message.

2. **Back-links**: for each "Back-links needed" from stub-researcher results, add a `[[WikiLink]]` to the referenced page's Related/Connections section (only if that file exists).

3. **Update `C:\Bazi\index.md`**: add entry for each approved page under its category. Update page count in header.

4. **Append to `C:\Bazi\log.md`**:
   ```
   ## [YYYY-MM-DD] update | wiki-batch-expand
   - Expanded N stubs: [topic names]
   - Flagged N for manual review: [topics]
   - Skipped N: [topics]
   ```

## Step 7 — Lint and Commit

1. Run `python C:/Vault/tools/lint_wiki.py C:/Bazi`. Fix issues (max 2 iterations).
2. Stage files by name (expanded pages + index.md + log.md + COLLAB.md). Never `git add -A`.
3. Commit: `[claude] expand: N stubs enriched -- wiki-batch-expand YYYY-MM-DD`
4. Pull --rebase, push, verify with `git log --oneline -3`.

## Step 8 — Report Scorecard

Print summary:
```
wiki-batch-expand complete:
  Approved & committed: N pages
  Flagged (manual review): [paths + scores]
  Skipped: [paths + scores]
```

## Step 9 — Cleanup

Move COLLAB.md row to Done. Delete `C:\Bazi\session-checkpoint.md`.

---

## Error Handling

- Subagent returns no STUB-RESULT block: treat as SKIP
- Write fails on a page: log, skip, continue
- Lint still dirty after 2 passes: **STOP**. Print the unresolved lint issues. Do NOT commit. Ask the user to fix manually, then re-run `/lintfix` before committing.
- git rebase conflict: stop, show conflict files, ask "take ours / take theirs / manual?"
