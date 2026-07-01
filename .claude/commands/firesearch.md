# /firesearch

Research a DPA member bank end-to-end and update the BankProfile wiki.

This command runs the `/research` skill with BankProfile-specific defaults.

## Defaults for BankProfile context

- **Wiki target**: `C:\Vault\BankProfile\md\wiki\entities\[bank].md`
- **Index**: `C:\Vault\BankProfile\md\index.md`
- **Log**: `C:\Vault\BankProfile\md\log.md`
- **Data points**: full Pillar 4 (capital) + Pillar 3 (asset quality) + Pillar 1 (balance sheet)
- **Source priority**: BoT Pillar 3 → SET filing → bank IR → parent group IR
- **Tier requirements**: check `C:\Vault\BankProfile\md\wiki\concepts\institution-tiers.md` for required fields and update frequency before starting

## Steps

Follow the `/research` skill workflow (Phases 1–7) with these BankProfile-specific additions:

1. **Orient**
   - Read existing entity page; note all `[E]` fields and `updated:` date
   - Confirm institution tier from `institution-tiers.md`
   - Check operational status (active / suspended / branch / etc.) — flag if non-standard
   - Confirm immediate parent entity vs. ultimate parent (relevant for foreign subsidiaries/branches)

2. **Stage** — create NLM notebook named `"[Bank] [Reporting Date]"` (e.g., `"KTB FY2025"`)
   - BoT Pillar 3 PDFs: use pdftotext if accessible + structured; NLM if large/encrypted/complex
   - Parent group PDFs / Oppday YouTube: NLM required

3. **Extract**
   - Run all 4 NLM query templates (capital, asset quality, balance sheet, profitability)
   - **Quarterly snapshot**: for listed banks (SET-traded), also extract latest quarterly data (Q1 or most recent)
   - SET-listed Thai banks: BBL, KBANK, SCB, KTB, BAY, TTB, UOB, KKP, TISCO, CIMBT, LHBank, ThaïCredit

4. **Verify**
   - Cross-check CET1, CAR, NPL against prior wiki values; flag ⚠️ if >20% change
   - **Capital trend alerts** (from `/research` Phase 5): flag Tier1 drop >1pp QoQ, CAR <14%, NPL rise >1pp, Coverage <150%

5. **Write** — update entity page following BankProfile CLAUDE.md schema; [C]/[E] discipline

6. **Update index** — refresh entry in `index.md`

7. **Append log** — format: `## [YYYY-MM-DD] firesearch | [Bank Name]`

## Source discovery hints

BoT Pillar 3 URL starting pattern (verify live — BoT restructures URLs):
```
https://www.bot.or.th/th/financial-institutions/financial-reporting/[bank-slug]/pillar-3.html
```
Start with a WebSearch: `site:bot.or.th "[bank name]" pillar-3 filetype:pdf` to confirm current path.

BoT Monthly (per-institution balance sheet): ⚠️ requires browser session as of Jun 2026.  
URL: `https://www.bot.or.th/en/statistics/financial-institutions/summary-statement-of-assets-and-liabilities.html`

## Usage

```
/firesearch TTB
/firesearch Mizuho
/firesearch KTB
/firesearch BOC Thai
```
