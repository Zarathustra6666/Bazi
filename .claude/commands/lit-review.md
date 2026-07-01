# /lit-review

> **Pre-flight (Remote):** Call ToolSearch once before starting: `select:WebSearch,WebFetch`
> Skip if these tools were already loaded earlier in this session.

Run an academic literature review using the two-brain pipeline (NotebookLM + Claude)
and produce a Claim-Evidence Matrix and traceable manuscript section.

This command runs the `/lit-review` skill with Vault-specific output defaults.

## Vault output defaults

- **Matrix**: `wiki/analyses/[topic]-claim-matrix-[YYYY-MM-DD].md`
- **Manuscript draft**: `wiki/topics/[topic]-manuscript-[section].md`
- **Source summary**: `wiki/sources/[topic]-nlm-litreview-[YYYY-MM-DD].md`
- **Log**: `log.md` in the active vault's root

If invoked from a repo with no `wiki/` structure,
save to the working directory with the same naming convention.

## Steps

Follow the `/lit-review` skill workflow (Steps 0A–6) with these additions:

1. **Scope** (Step 0A) — confirm research question and construct map before proceeding

2. **NLM Discovery** (Step 0B)
   - Name the notebook: `"[Topic] — [Vault] Lit Review [YYYY-MM-DD]"`
   - For DPA/deposit research: add `"Thailand DPA deposit protection"` to the query to surface
     Thai banking context papers alongside international evidence

3. **Curate** (Step 0C)
   - Scopus exports: add top-20 by relevance (not all results)
   - For IRRBB / NMD / passthrough topics: also check PIER, BOT working papers, BIS working papers
   - Thai-language papers from Chulalongkorn, Thammasat, NIDA: add as text source if PDF inaccessible

4. **Matrix output** — include the NLM notebook ID in the matrix file header
   so it can be re-queried in future sessions without re-staging sources

5. **Manuscript output** — include `matrix_source:` frontmatter linking back to the matrix file

6. **Append log** — format: `## [YYYY-MM-DD] analysis | Lit Review — [Topic]`

## Usage

```
/lit-review deposit beta passthrough
/lit-review IRRBB NMD behavioral maturity Thailand
/lit-review virtual bank deposit behavior DPA
/lit-review replicating portfolio EVE NII sensitivity
```

Arguments are flexible — any research topic works.
If the topic is ambiguous, Claude will ask one clarifying question before Step 0B.
