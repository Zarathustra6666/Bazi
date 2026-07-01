# /domain-daily — Daily Research Scout & Triage Report

> **Pre-flight (Remote):** Call ToolSearch once before starting: `select:WebSearch,WebFetch`
> Skip if these tools were already loaded earlier in this session.

Run the daily knowledge-expansion loop: scout new sources, triage for quality, and produce a report. Does **not** ingest anything. Safe to run every day.

---

## What It Does

1. Loads the watchlist from `.autoresearch/program.md`
2. Delegates to `domain-scout` — finds new candidate sources across watchlist topics
3. Delegates to `reference-triage` — assigns APPROVE / DEFER / MERGE / REJECT to each candidate
4. Produces a daily markdown report
5. Appends a summary row to `.autoresearch/run-log.tsv`

No wiki files are created or modified during a daily run.

---

## Usage

```
/domain-daily
/domain-daily [topic]       ← focus scout on one watchlist topic
/domain-daily status        ← show last 7 run-log entries, no new scouting
```

---

## Daily Report Format

The report is produced inline (not saved to a file unless you ask).

```
## Domain Daily Report — YYYY-MM-DD

### Candidate Sources
[decision table from reference-triage]

### Summary
- APPROVE: N
- DEFER:   N
- MERGE:   N  (targets: …)
- REJECT:  N

### Likely Duplicates
[list any MERGE candidates with target wiki page]

### Rejected Items
[list with one-line rejection reason each]

### Unresolved Questions
[questions raised by candidates that the wiki cannot currently answer]

### Suggested Next Search Directions
[3–5 search angles worth pursuing in the next cycle]

### Top Domain Gaps
[watchlist topics with the fewest approved candidates still awaiting ingest]
```

---

## Run Log Update

After producing the report, append one row to `.autoresearch/run-log.tsv`:

```
YYYY-MM-DD\tdaily\t[topics covered]\t[approve count]\t[reject count]\t[defer count]\t[notes]
```

---

## Notes

- APPROVE decisions here go into a pending queue — they are not ingested until `/domain-weekly ingest` is run
- If `domain-scout` finds nothing new for a topic, that is a valid result — report "no new candidates" rather than padding with weak sources
- If NotebookLM MCP is unavailable, proceed with WebSearch-only; note the gap in the report
