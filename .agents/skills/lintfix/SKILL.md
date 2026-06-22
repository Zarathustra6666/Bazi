# /lintfix — Wiki Lint, Fix & Commit

Run a full lint pass on the active wiki, fix all issues found, verify clean, then commit and push.

## Trigger Keywords
- `/lintfix`
- "lint and fix"
- "lint pass"
- "health check and fix"
- "clean up wiki"

## Steps

1. **Identify the active wiki** from conversation context (Z/, Bazi/, md/, DepoMov/, etc.). If ambiguous, ask.

2. **Read `index.md`** and list all registered pages to build the link target set.

3. **Scan `Wiki/` subdirectories** — collect every `.md` file path and its frontmatter (`type`, `title`, `tags`, `sources`, `created`, `updated`).

4. **Run lint checks:**
   - **Broken WikiLinks** — every `[[Target]]` must match a `title:` or `aliases:` in the wiki; flag unresolved targets
   - **Orphan pages** — every wiki page must appear as a link target in at least one other page; flag zero-inbound pages
   - **Frontmatter errors** — flag pages missing required fields (`title`, `type`, `tags`, `created`, `updated`)
   - **Misplaced files** — flag pages whose `type:` doesn't match their directory (e.g., `type: synthesis` in `entities/`)
   - **Thin content** — flag entity or concept pages with fewer than 3 meaningful bullets
   - **index.md gaps** — flag pages that exist in `Wiki/` but are missing from `index.md`

5. **Apply all fixes inline** — update WikiLinks, add missing frontmatter fields, move misplaced files, add entries to `index.md`, add inbound links to orphan pages.

6. **Run a second lint pass** to confirm all issues are resolved. If new issues surface, fix and re-check (cap at 3 iterations).

7. **Update `index.md` footer** with current page counts (sources · entities · concepts · synthesis).

8. **Append to `log.md`:**
   ```
   ## [YYYY-MM-DD] lint | Wiki Health Check — Lint Pass (N Pages)
   - Issues fixed: [list]
   - Remaining gaps: [list any deferred items]
   ```

9. **Commit and push:**
   - Stage all changed files by name (not `git add .`)
   - Commit message: `lint: wiki health check — [N] fixes ([date])`
   - Push to remote

## Notes
- This vault has no test suite. A clean lint pass IS the definition of done.
- If a broken WikiLink target is ambiguous, add an `aliases:` entry to the target page rather than changing the link.
- Orphan pages with no obvious inbound link home should be linked from the most relevant concept or entity page, or from `index.md` if no better location exists.
