---
name: research
description: >
  General-purpose research workflow using NotebookLM as the extraction layer for any
  research target — bank firesearch, topic investigation, document analysis, or
  multi-source synthesis. NotebookLM handles source ingestion and cited extraction so
  raw PDFs never enter Codex's context (token optimization). Codex handles orient,
  verify, synthesize, and write. Trigger on: /research [target], "firesearch [bank]",
  "investigate [topic]", "research [subject]", or any multi-source information gathering task.
compatibility:
  required_tools: [Read, Write, Edit, WebSearch, Glob, Grep]
  optional_tools: [WebFetch, Bash]
  mcp_tools:
    preferred: [mcp__notebooklm-mcp__notebook_create, mcp__notebooklm-mcp__notebook_add_url,
                mcp__notebooklm-mcp__notebook_add_text, mcp__notebooklm-mcp__notebook_query,
                mcp__notebooklm-mcp__notebook_get, mcp__notebooklm-mcp__notebook_describe]
    fallback: WebFetch + pdftotext (if NLM MCP unavailable)
  environment: Codex (terminal)
  os: Windows, macOS, Linux
---

# /research — NotebookLM-First Research Workflow

> NotebookLM is the extraction layer. Codex is the synthesis and writing layer.
> Raw PDFs and large documents never enter Codex's context — only NLM query responses do.

---

## Mental Model

```
WebSearch          NotebookLM (MCP)           Codex
  │                    │                         │
  ├── find URLs ──────▶│ notebook_add_url        │
  ├── find PDFs ───────▶│ notebook_add_url        │
  │                    │ (indexes all sources)   │
  │                    │                         │
  │                    │◀── notebook_query ──────┤  "extract CET1, NPL, LCR..."
  │                    │──── cited answer ───────▶│  ~300 tokens, not ~10,000
  │                                               │
  │                                               ├── verify critical figures
  │                                               ├── synthesize into wiki/report
  │                                               └── update index + log
```

**Token saving**: A 300KB Pillar 3 PDF extracted via WebFetch = ~8,000–15,000 tokens in context.
The same PDF added to NLM + queried = ~300–500 tokens (the cited answer only).

**Quality gain**: NLM cites source + section for every figure. No hallucinated ratios.
Figures without citations stay `[E]` — the absence of citation is itself signal.

---

## Phase 1 — Orient

Before touching any source, establish what is needed and what already exists.

1. **Identify the research target** from the user's input (bank name, topic, document)
2. **Check existing wiki data** — read the entity/concept page if it exists
   - Note which fields are `[E]` (need confirmation) vs `[C]` (already confirmed)
   - Note the `updated:` date — anything older than 6 months is stale for financial data
3. **List the data points needed** — be explicit before searching:
   - For bank firesearch: total assets, net loans, deposits, CET1, CAR, LCR, NSFR, NPL, Stage 2, coverage, NIM, ROA, net profit
   - For topic research: define the 5–10 key questions to answer
4. **Identify likely sources** before searching:
   - Bank: BoT Pillar 3 URL pattern, SET filing, bank IR page, parent group IR
   - Topic: define primary vs secondary sources
5. **Choose extraction method by source type** — decide before fetching:

   | Source type | Preferred method | Why |
   |---|---|---|
   | BoT Pillar 3 PDF (accessible, structured tables) | pdftotext → Bash | Fast, reliable for tabular capital/NPL data |
   | Annual reports (large, >10MB, possibly encrypted) | NLM `notebook_add_url` | Token savings; NLM handles encrypted + large files |
   | Parent group PDFs (foreign language, complex layout) | NLM preferred | Cross-source synthesis; NLM handles Thai+English |
   | YouTube / Oppday presentations | NLM only | WebFetch cannot read video transcripts |
   | Web articles / press releases | WebFetch or NLM | Either works; NLM if >3 articles to synthesize |
   | SET filings (compact quarterly PDF) | pdftotext | Fast; structured Thai accounting format |

   Token rule: if raw fetch would exceed ~5,000 tokens, route through NLM instead.

---

## Phase 2 — Source Discovery

Use WebSearch to find source URLs. Do NOT fetch full content yet — just collect URLs.

```
WebSearch queries (examples for bank research):
  "[Bank name] Pillar 3 2025 filetype:pdf"
  "[Bank name] annual report FY2025 investor relations"
  "[Bank name] BoT capital fund maintenance December 2025"
  site:bot.or.th "[bank name]" pillar-3
```

Record each URL found with a one-line description. Aim for:
- 1–2 primary sources (Pillar 3 or annual report)
- 1 secondary source (parent group IR or BoT aggregate)

**Stop at 3–4 sources** — NLM quality degrades with too many conflicting sources in one notebook.

---

## Phase 3 — Stage Sources into NotebookLM

> This is the token-saving step. Sources are indexed by NLM, not read into Codex's context.

### Check NLM availability first
If NLM MCP tools are available and authenticated, use them. If not, skip to [Fallback](#fallback).

```
Step 3a: Create notebook
  mcp__notebooklm-mcp__notebook_create
  name: "[Target] — [Date]"  (e.g., "BOC Thai Dec 2025" or "LCR Regulation Research")

Step 3b: Add each source URL
  mcp__notebooklm-mcp__notebook_add_url
  For each URL from Phase 2 — NLM fetches and indexes; content never enters Codex's context

Step 3c: Add any text already in context (if user pasted content)
  mcp__notebooklm-mcp__notebook_add_text
  Paste extracted text or quotes into NLM as a source

Step 3d: Confirm sources loaded
  mcp__notebooklm-mcp__notebook_get or notebook_describe
  Verify all sources show as indexed before querying
```

**Note**: NLM may take 30–120 seconds to index PDF sources. If a source fails to load, note it and continue with what indexed successfully.

---

## Phase 4 — Structured Extraction via NLM Queries

Query NLM once per data domain. Use precise, structured queries — NLM returns cited answers.

### Query templates

**For bank capital & liquidity:**
```
"Extract the following with exact figures and source citations (page/section):
CET1 ratio, Tier 1 ratio, Total CAR (BIS ratio), AT1 amount (if any),
LCR ratio, NSFR ratio (if disclosed), RWA total, reporting date."
```

**For bank asset quality:**
```
"Extract with citations: NPL ratio (gross), Stage 1 %, Stage 2 %, Stage 3 %,
ECL coverage ratio, total loans, any notable NPL concentration by sector."
```

**For bank balance sheet:**
```
"Extract with citations: total assets, net loans, total deposits,
loan-to-deposit ratio, investment securities total, reporting date."
```

**For bank profitability:**
```
"Extract with citations: NIM, ROA, ROE, net profit (THB), credit cost,
cost-to-income ratio. If not available, state explicitly."
```

**For topic research:**
```
"Answer the following questions with citations from the sources:
[Question 1], [Question 2], [Question 3]..."
```

### Recording NLM responses

For each query response:
- Mark figures with NLM citation as `[C]` — confirmed from cited source
- Mark figures NLM could not find as `[E]` — to be estimated or left blank
- Note any conflicts between sources: "Source A says X, Source B says Y"

### Quarterly snapshot — always run for listed Thai banks

For any listed Thai bank (SET-traded), add Q1/current-year snapshot alongside the annual data:
- Source: SET filing (56-1, management discussion, or Oppday PDF)
- Add a separate period column in the Financial Performance table
- This applies regardless of whether the annual data is already confirmed [C]

---

## Phase 5 — Verify Critical Figures

Before writing, cross-check the most critical figures from NLM's responses.

**Always verify for financial research:**
- Capital ratios (CET1, CAR) — errors here are high-stakes
- NPL ratio — if significantly different from prior wiki value, flag ⚠️
- Total assets — if >10% change from prior value, confirm it's a real change, not a source error

**Verification method:**
- If NLM cited a specific page/section: fetch only that section via WebFetch to confirm
- If NLM's answer contradicts prior wiki data by >20%: fetch the source URL directly
- If NLM returned [E] (no citation found): do a targeted WebSearch for that specific figure

**Contradiction handling:**
- Flag with ⚠️ in the output
- Note both values: "Prior wiki: X / New source: Y"
- Do not auto-resolve — document the conflict and ask if needed

### Capital trend alerts

Flag ⚠️ if any of these thresholds are triggered:

| Metric | Alert trigger |
|---|---|
| Tier 1 ratio | Drop >1pp in a single quarter, or drop >2pp YoY |
| Total CAR | Falls below 14% (approaching BoT minimum 10.5% + buffer) |
| CET1 | Falls below 10% |
| NPL ratio | Rises >1pp from prior reporting period |
| ECL coverage | Falls below 150% (especially for D-SIBs) |

Alert format: append `⚠️` to the figure and add a note — e.g., `12.04% ⚠️ (-1.22pp QoQ)`.

### Institutional context checks

Run these checks for every bank; they affect how data is interpreted:

1. **Parent verification** — confirm the immediate parent entity vs. ultimate parent.  
   Example: BOC Thai's immediate parent is BOCHK (Hong Kong), not BOC China directly.  
   This matters for capital support assumptions and group structure diagrams.

2. **Operational status** — confirm the bank is still actively licensed and operating.  
   For foreign branches: check BoT's licensed institution list or BoT press releases for suspension/revocation.  
   Example: IOB (Indian Overseas Bank Thai branch) had an active BoT temporary suspension as of mid-2026.  
   Flag in the entity page header: `⚠️ Operational status: Temporary suspension (as of [date])`

3. **Tier assignment** — confirm the institution tier from `institution-tiers.md` before writing.  
   Tier determines which data fields are required, which are optional, and update frequency.

---

## Phase 6 — Synthesize & Write

Write the output using NLM-extracted [C] data and modeled [E] estimates.

### For wiki entity pages (bank firesearch)

Follow the entity page schema in `AGENTS.md`:
- One-liner: update with latest confirmed figures
- Financial Performance table: add new period column with [C] flags
- Default simulation parameters: update any [C] values
- DPA Exposure Analysis: recalculate from new balance sheet
- Sources section: add NLM notebook entry + original source URL

### For wiki concept pages

Follow the concept page schema. Link to all entity pages mentioned.

### For reports / ad-hoc research

Structure as: Summary → Key findings (with citations) → Data gaps → Open questions

### [C] vs [E] discipline

- `[C]` = NLM returned a cited figure from a primary source
- `[E]` = modeled estimate; NLM had no citation, or source was secondary only
- Never upgrade `[E]` to `[C]` without a citation chain

---

## Phase 7 — Persist

1. **Update entity/concept page** — the main deliverable
2. **Update index.md** — refresh the institution/topic entry
3. **Append log.md** entry:
   ```
   ## [YYYY-MM-DD] firesearch | [Target]
   - Sources staged in NLM: [N] ([list URLs])
   - Key confirmed figures: [brief summary]
   - Files changed: [list]
   ```
4. **Save NLM notebook reference** — add the NLM notebook name/ID to the entity page's Source notes section so it can be re-queried in future sessions without re-staging sources
5. **Commit and push** (if requested or at session end)

---

## Fallback — NLM Unavailable

If NLM MCP is not authenticated or returns errors:

1. Log: "NLM MCP unavailable — falling back to direct fetch"
2. For each source URL:
   - WebFetch the URL
   - If PDF binary: save to temp file, run `pdftotext` via Bash
   - Read extracted text into context (token cost applies)
3. Extract data points manually from the text
4. Continue from Phase 5 (Verify)
5. In the log entry, note: "NLM fallback — raw PDF read; token cost elevated"

**Re-authentication command** (run in terminal if NLM keeps failing):
```
notebooklm-mcp-auth
```
Then restart the Codex session before retrying.

---

## Usage

```
/research BOC Thai          → bank firesearch (default: BankProfile wiki target)
/research LCR regulation    → topic research (concept page target)
/research HSBC Thailand     → entity investigation
/research KTB FY2025        → annual firesearch with year hint
```

Arguments are flexible — the research target can be a bank name, topic, institution, or question.
If the target is ambiguous, ask one clarifying question before proceeding.

---

## Quick Reference — NLM MCP Tool Names

| Action | Tool |
|---|---|
| Create notebook | `mcp__notebooklm-mcp__notebook_create` |
| Add URL source | `mcp__notebooklm-mcp__notebook_add_url` |
| Add text source | `mcp__notebooklm-mcp__notebook_add_text` |
| Query notebook | `mcp__notebooklm-mcp__notebook_query` |
| Get notebook info | `mcp__notebooklm-mcp__notebook_get` |
| Describe notebook | `mcp__notebooklm-mcp__notebook_describe` |
| List notebooks | `mcp__notebooklm-mcp__notebook_list` |
| Describe source | `mcp__notebooklm-mcp__source_describe` |
| Get source content | `mcp__notebooklm-mcp__source_get_content` |

---

## Notes

- One NLM notebook per research target — don't mix banks or topics in one notebook
- NLM notebooks persist across sessions — re-query without re-staging if sources unchanged
- NLM cannot ingest password-protected PDFs — fall back to pdftotext for those
- For Thai-language PDFs: NLM handles Thai text; query in English for best results
- Phase 4 query depth scales with tier: Tier A banks → all 4 query templates; Tier D stubs → capital query only
