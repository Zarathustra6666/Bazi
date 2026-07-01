# /autoresearch — Autonomous Research Loop

> **Pre-flight (Remote):** Call ToolSearch once before starting: `select:WebSearch,WebFetch,mcp__notebooklm-mcp__notebook_list,mcp__notebooklm-mcp__notebook_create,mcp__notebooklm-mcp__notebook_add_url,mcp__notebooklm-mcp__notebook_query`
> Skip if these tools were already loaded earlier in this session.

Vault autoresearch system. Runs the 9-step loop across all 3 wikis (Z, BankProfile, Deposit Research), sourcing new content from WebSearch + NotebookLM and staging digests for human review.

---

## Invocation Modes

```
/autoresearch              → run all stale topics (sweeps all 3 wikis; NEVER STOPS mid-run)
/autoresearch [topic-id]   → run one topic immediately (full pipeline, same rules)
/autoresearch apply        → write pending digest(s) to wiki (shows diff, asks confirmation)
/autoresearch status       → show all 12 topics with staleness: ⚠️ overdue / ✓ fresh / 🔴 ERROR
```

---

## Configuration Files

- `C:\Vault\.autoresearch\program.md` — research agenda (human edits to steer)
- `C:\Vault\.autoresearch\run-log.tsv` — full history of every run (agent reads for self-calibration)
- `C:\Vault\.autoresearch\pending-review\` — staged digests awaiting human review (gitignored)

---

## The 9-Step Loop (per topic)

**Step 1 — Read program.md.**
Load research philosophy, evaluation criteria, budget constraints, and topic list.

**Step 2 — Read run-log.tsv.**
Check: has this topic returned STALE 3+ consecutive times? If yes, note it — append a calibration warning ("Search query may need refinement") to this run's digest section.

**Step 3 — Staleness check.**
Compare `last_checked` + `schedule` to today's date. If fresh → skip, log nothing, continue to next topic. If stale (or `last_checked: 2020-01-01` / never run) → continue.

**Step 4 — Hypothesis formation.**
Read all `target_pages` for this topic. State explicitly in the log: "Current wiki says [X]. I expect to find [Y] since [last_checked]. The what-constitutes-new criterion is [Z]." Write this hypothesis into run-log.tsv.

**Step 5 — WebSearch (budget: max 3 queries).**
Use the topic's `search_query` as the primary query. Form up to 2 hypothesis-driven follow-up queries. Collect URLs with publication dates after `last_checked`.

**Step 6 — Ratchet gate #1.**
If 0 URLs found → outcome = STALE. Update `last_checked` in program.md. Append one row to run-log.tsv. CONTINUE to next topic (do not stop).

**Step 7 — NLM stage + query (budget: max 2 queries).**
If `nlm_notebook` is a UUID: add new URLs to that notebook via `mcp__notebooklm-mcp__notebook_add_url`.
If `nlm_notebook` is `create-new`: create a new notebook via `mcp__notebooklm-mcp__notebook_create`, update program.md with the new UUID, then add URLs.
Query the notebook: "Based on the new sources just added, what information is NEW relative to: [paste target page summaries]? Cite specific claims with source titles."

**Step 8 — Ratchet gate #2 (the metric).**
Evaluate the NLM response against the topic's `what-constitutes-new` field:
- **NEW** → append a digest section to `pending-review/YYYY-MM-DD-digest.md`; update `last_checked` in program.md
- **STALE** → update `last_checked` only; no digest entry (ratchet holds — no clutter)
- **CONTRADICTION** → append digest section with ⚠️ CONTRADICTION flag; update `last_checked`; mark for mandatory manual review before `/autoresearch apply` can touch that page
- **ERROR** → log as ERROR; leave `last_checked` unchanged (will retry next cycle)

**Step 9 — Log + continue.**
Write exactly one row to `run-log.tsv` with columns: date, topic-id, hypothesis (one sentence), sources_found, outcome, pages_staged, note. Continue to next stale topic WITHOUT pausing or asking the user.

---

## After All Topics Processed

Append a **Calibration Notes** section to the digest:
- Topics with 3+ consecutive STALE → "Consider refining search query or reducing schedule frequency"
- Topics with repeated ERROR → "NLM notebook may need refresh or URL is blocked"
- Topics with high NEW rate → "Consider increasing schedule frequency"

Then report: N topics run, M new digests staged, K skipped (fresh), J errors.

---

## `/autoresearch apply` Pipeline

1. Read all `.md` files in `pending-review/` (skip archive/)
2. Display a summary: topic-id, outcome, proposed target page for each item
3. Ask user which ✓ NEW items to apply (do NOT auto-apply ⚠️ CONTRADICTION items — those require explicit user resolution first)
4. For each confirmed item: write the update to the target wiki page (create stub or edit existing)
5. Update `index.md` and `log.md` for each affected wiki
6. Archive the applied digest to `pending-review/archive/YYYY-MM-DD-digest.md`
7. Remind user to run `/sync`

---

## `/autoresearch status` Display

Show a table for each wiki:

```
DEPOSIT RESEARCH
  bot-deposit-monthly      ⚠️ overdue (monthly, last: 2020-01-01)
  dpa-news                 ⚠️ overdue (monthly, last: 2020-01-01)
  dsib-quarterly           ⚠️ overdue (quarterly, last: 2020-01-01)
  virtual-banks-news       ⚠️ overdue (weekly, last: 2020-01-01)

Z WIKI
  nmd-irrbb-papers         ⚠️ overdue (monthly, last: 2020-01-01)
  deposit-passthrough-research  ⚠️ overdue (monthly, last: 2020-01-01)
  bot-monetary-policy      ⚠️ overdue (monthly, last: 2020-01-01)
  forecasting-models-new   ⚠️ overdue (monthly, last: 2020-01-01)

BANKPROFILE
  bot-pillar3-quarterly    ⚠️ overdue (quarterly, last: 2020-01-01)
  set-quarterly-filings    ⚠️ overdue (quarterly, last: 2020-01-01)
  fitch-moody-thai-banks   ⚠️ overdue (monthly, last: 2020-01-01)
  virtual-bank-regulatory  ⚠️ overdue (monthly, last: 2020-01-01)

Pending digests: 0 files in pending-review/
```

Staleness logic:
- `weekly`: overdue if last_checked > 7 days ago
- `monthly`: overdue if last_checked > 30 days ago
- `quarterly`: overdue if last_checked > 90 days ago
- `never run` (last_checked = 2020-01-01): always ⚠️ overdue

---

## NEVER STOP Rule

The loop processes ALL stale topics in one sweep. It does not pause to ask the user between topics. It does not stop on ERROR — it logs the error and moves on. The only pauses are:
1. Before `/autoresearch apply` writes to wiki pages (requires explicit confirmation per item)
2. CONTRADICTION items (always require manual resolution before apply)

This is the Karpathy invariant: "NEVER STOP."

---

## Phase 2 — Lint, Fix & Push

After all topics are processed and the calibration report is appended to the digest:

1. Run lint on all wikis:
   ```bash
   python C:/Vault/tools/lint_wiki.py C:/Vault
   ```
2. If broken WikiLinks are found: fix them (update link targets only — do not expand or rewrite content). Re-run lint. Cap at 2 fix iterations.
3. If lint is clean: commit all changes using the branch-aware pattern:
   ```bash
   BRANCH=$(git -C "C:/Vault" rev-parse --abbrev-ref HEAD)
   git -C "C:/Vault" add -A
   git -C "C:/Vault" commit -m "autoresearch: N topics run, M digests staged (YYYY-MM-DD)"
   git -C "C:/Vault" push origin "$BRANCH"
   git -C "C:/Vault" log "origin/$BRANCH" -1 --oneline
   ```
4. Compare the pushed hash to the commit hash. If they differ, flag "push unconfirmed" and retry.
5. Report final one-line summary:
   ```
   autoresearch: N topics run · M new digests staged · lint clean · pushed <hash>
   ```
