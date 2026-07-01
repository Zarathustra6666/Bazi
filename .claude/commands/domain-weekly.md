# /domain-weekly — Weekly Verification & Ingest-Prep Report

> **Pre-flight (Remote):** Call ToolSearch once before starting: `select:WebSearch,WebFetch,mcp__notebooklm-mcp__notebook_list,mcp__notebooklm-mcp__notebook_add_url,mcp__notebooklm-mcp__notebook_query`
> Skip if these tools were already loaded earlier in this session.

Run the weekly verification loop: review all APPROVE-status candidates from the past 7 days, verify metadata and claim-source alignment, and prepare an ingest-ready list. Does **not** ingest unless you explicitly add `ingest`.

---

## What It Does

1. Reads `.autoresearch/run-log.tsv` to find APPROVE-status sources from the past 7 daily cycles
2. Delegates to `citation-verifier` — verifies metadata, URL liveness, and claim-source alignment
3. Produces a weekly markdown report
4. If `ingest` argument is passed: delegates to `knowledge-ingest` for all INGEST-READY sources

---

## Usage

```
/domain-weekly              ← verify and report only, no ingest
/domain-weekly ingest       ← verify + ingest all INGEST-READY sources
/domain-weekly ingest [N]   ← ingest only the Nth source from the INGEST-READY list
/domain-weekly status       ← show pending approve queue without running verification
```

---

## Weekly Report Format

```
## Domain Weekly Report — YYYY-MM-DD

### Verified Sources (INGEST-READY)
[list with verified title, URL, and one-line description of what it adds]

### Metadata Fixes Needed (NEEDS-FIX)
[list with source title and specific fields requiring correction]

### Claim-Source Mismatches
[list with source title, what scout claimed, and what the source actually says]

### Stale or Broken Links
[list of previously approved sources whose URLs are now dead or redirecting]

### Ingestion-Ready Items
| # | Title | Watchlist topic | Type | Verified date |
|---|---|---|---|---|

### Rejected (post-verification)
[sources that were APPROVE at triage but REJECT after citation verification, with reason]

### Unresolved Issues
[items requiring manual review, author confirmation, or DOI resolution]
```

---

## Ingest Behaviour

When run with `ingest`:

1. For each INGEST-READY source: delegate to `knowledge-ingest`
2. `knowledge-ingest` will show a diff for any existing page before overwriting — confirm each change
3. After all ingest operations, run a lint pass to confirm no broken WikiLinks or orphans
4. Commit all new and modified wiki files with message: `ingest: [N] sources — weekly cycle YYYY-MM-DD`

If any source is NEEDS-FIX or REJECT, it is skipped — fix the metadata issue first, then re-run `/domain-weekly ingest [N]` for that item.

---

## Run Log Update

After producing the report, append one row to `.autoresearch/run-log.tsv`:

```
YYYY-MM-DD\tweekly\t[topics covered]\t[ingest-ready count]\t[needs-fix count]\t[reject count]\t[notes]
```

---

## Notes

- INGEST-READY status requires both APPROVE (from triage) and INGEST-READY (from verifier) — no exceptions
- The weekly cycle is the only path to ingest; `/domain-daily` never ingests
- If the approve queue is empty (no daily runs this week), the report will say so — do not fabricate candidates
- If NotebookLM MCP is unavailable, proceed with WebSearch-based verification only; note the gap
