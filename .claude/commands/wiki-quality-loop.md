---
name: wiki-quality-loop
description: >
  Single-iteration wiki quality improvement designed for /loop 10m wrapping.
  Each invocation runs exactly ONE task from a priority queue (lint → stub expansion →
  thin page enrichment → cross-link audit → expand topic → gap fill → idle),
  then commits and exits. The loop restarts it every 10 minutes.
  Trigger on: /wiki-quality-loop
---

# /wiki-quality-loop — 10-Minute Wiki Quality Iteration

> **Pre-flight (Remote):** Call ToolSearch once before starting: `select:WebSearch,WebFetch`
> Skip if these tools were already loaded earlier in this session.

One focused improvement per run. Completes in ≤10 minutes. Designed for:

```
/loop 10m /wiki-quality-loop
```

---

## Time Budget

| Phase | Budget |
|-------|--------|
| Orient + lint | ~2 min |
| One work task (research cap: 2 WebSearch queries, 1 new page max) | ~6 min |
| Commit + push | ~2 min |
| **Total** | **≤10 min** |

Never chain tasks. Complete one, then commit and exit.

---

## Step 1 — Orient

1. Read `C:\Bazi\index.md` — build the set of all known `[[WikiLink]]` targets
2. Read the last **5 entries** of `C:\Bazi\log.md` — build a **skip list** of pages/tasks touched recently
3. Note today's date for log entries

---

## Step 2 — Lint Pass (always runs)

Check `C:\Bazi\wiki\` for:
- **Broken WikiLinks** — `[[Target]]` where no page with `title: Target` or matching alias exists
- **Frontmatter errors** — missing `title`, `type`, `tags`, `created`, or `updated` fields
- **Orphan pages** — pages with no inbound links from any other page
- **Index gaps** — `.md` files in `wiki/` not listed in `index.md`
- **Misplaced files** — `type:` in frontmatter doesn't match directory (e.g., `type: entity` in `concepts/`)

**If any issues found:** fix all of them now. Update `index.md` for index gaps. Then **jump to Step 9 (Commit)**. Do not evaluate Steps 3–8.

**If lint is clean:** continue to Step 3.

---

## Step 3 — Stub Expansion

Scan `wiki/` for pages that are stubs:
- Contain `[STUB]` anywhere in body, OR
- Body has fewer than 3 meaningful bullet points (frontmatter doesn't count)

Skip any page on the skip list from Step 1.

**If a stub is found:** pick the first one not on the skip list.
- Run **2 WebSearch queries** to gather factual content
- Expand the page: add at minimum 3 substantive bullets, update `updated:` date, remove `[STUB]` tag
- Add or verify bidirectional links to related pages
- **Jump to Step 9 (Commit)**

**If no stubs:** continue to Step 4.

---

## Step 4 — Thin Page Enrichment

Scan `wiki/entities/` and `wiki/concepts/` for pages with fewer than 3 meaningful bullets. Skip pages on the skip list.

**If a thin page is found:** pick the one most referenced by other pages (most inbound `[[WikiLink]]` mentions).
- Run **2 WebSearch queries** focused on the page's subject
- Add at minimum 3 new factual bullets; update `updated:` date
- **Jump to Step 9 (Commit)**

**If none:** continue to Step 5.

---

## Step 5 — Cross-Link Audit

Identify pages modified in the **last 3 days** (check `updated:` frontmatter field or `git log --since="3 days ago" --name-only`).

For each recent page, scan its body for plain-text mentions of entity or concept names that exist as wiki pages but are not currently wrapped in `[[WikiLink]]` syntax. Limit scan to the first 5 recently-modified pages.

**If unlinked mentions found:** add `[[WikiLink]]` syntax around them, update `updated:` date.
- **Jump to Step 9 (Commit)**

**If none:** continue to Step 6.

---

## Step 6 — Expand Topic

Pick **1 concept** from Bazi's active research domains that has not been touched recently (skip list):
- **Ten Gods (十神)** — e.g., subtopics of output/wealth/officer/resource/companion star interactions, favorable vs unfavorable configurations
- **Five Elements (五行)** — e.g., generating/controlling cycles, element strength assessment, seasonal adjustment (調候)
- **Useful God (用神)** — e.g., selection methodology, conflicting schools of thought, 6-category useful-god framework
- **Structural Patterns (格局)** — e.g., pattern purity, transformation patterns (化格), pattern-breaking conditions
- **Special Stars (神煞)** — e.g., individual star meanings, activation conditions, modern vs classical interpretation
- **Luck Pillars / Annual Cycles** — e.g., 10-year luck pillar transitions, annual stem-branch interaction with the natal chart

Choose the concept that appears most frequently in existing pages but has the shallowest own-page content, or a concept mentioned in log.md as a planned gap.

Run **2 WebSearch queries** to map its subtopics and lateral connections.

Draft **1 new concept or entity page** (`wiki/concepts/` or `wiki/entities/`):
- Full frontmatter (title, type, tags, sources, created, updated)
- Intro paragraph
- At minimum 3 substantive bullets (Key Facts / What It Is)
- `## Connections` section linking to parent and sibling pages
- Add a reciprocal link on the parent concept page

Update `index.md` — add the new page entry.

**Jump to Step 9 (Commit)**

---

## Step 7 — Knowledge Gap Fill

From `index.md` or any wiki page, identify `[[WikiLink]]` references that have no corresponding file in `wiki/`. Skip any on the skip list.

**If a gap is found:** pick the most-referenced missing target.
- Draft a stub page with full frontmatter + at minimum 3 bullets (even if brief)
- Add it to `index.md`
- **Jump to Step 9 (Commit)**

**If none:** continue to Step 8.

---

## Step 8 — Idle

Nothing to do. Append to `log.md`:

```
## [YYYY-MM-DD] quality-loop | idle
- Wiki clean: lint passed, no stubs, no thin pages, no cross-link gaps, no missing targets
- No files changed
```

Exit without committing.

---

## Step 9 — Commit

1. Append to `log.md`:
   ```
   ## [YYYY-MM-DD] quality-loop | [task name]
   - [What was done — 2–3 bullets]
   - Files changed: [list]
   ```
2. If `index.md` was modified, include it in staging
3. Stage only the files actually changed (by name, never `git add -A`)
4. Commit:
   ```
   git commit -m "quality-loop: [task] [YYYY-MM-DD]"
   ```
5. Pull with rebase, then push:
   ```
   git pull --rebase && git push
   ```
6. Confirm: `git log --oneline -3`
7. Report: one line to user — what was done, how many files changed

---

## Failure Modes

| Situation | Action |
|-----------|--------|
| Merge conflict on pull | Stop. Show conflict files. Ask user: take ours / take theirs / manual? |
| WebSearch returns no useful content | Skip this page; try next candidate; note in log |
| All 6 tasks skipped (everything on skip list) | Log idle; exit — skip list will clear over next few iterations |
| Task exceeds 8 minutes | Commit whatever is complete; note "partial" in log entry |
