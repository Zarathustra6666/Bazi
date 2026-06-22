---
name: firesearch
description: |
  Deep-dive research workflow สำหรับสถาบันการเงินไทย (DPA members) โดยใช้ dual-channel:
  NotebookLM (automated web research + Q&A engine) ควบคู่กับ WebSearch task (targeted search)
  แล้ว ingest ผลลัพธ์ทั้งหมดเข้า Vault MD wiki (C:\Vault\md\Wiki\entities\) พร้อมกัน

  ใช้ skill นี้ทุกครั้งที่ผู้ใช้พูดว่า:
  - "ทำ ธ. [ชื่อธนาคาร]"
  - "deep dive [ธนาคาร]"
  - "firesearch [FI]"
  - "ค้นคว้า [สถาบันการเงิน]"
  - "วิเคราะห์ [ธนาคาร] เชิงลึก"
  - "หาข้อมูล [bank name] สำหรับ DPA"
  - ชื่อธนาคารไทย/ต่างชาติที่เป็น DPA member เช่น SCB, KTB, BAY, Krungsri, CIMBT, ICBCT, TISCO, GSB, BAAC, GHB, SME Bank, Citibank, HSBC, Deutsche Bank, BNP Paribas, JPMorgan, BOA, OCBC, Standard Chartered
---

# FIResearch — Thai FI Deep Dive Skill

## วัตถุประสงค์

ค้นคว้าข้อมูลสถาบันการเงินไทยภายใต้ DPA อย่างเป็นระบบ โดยใช้ dual-channel workflow แล้ว
ingest ผลลัพธ์เข้า Vault MD wiki และ NotebookLM notebook พร้อมกัน

## Sessions ที่ใช้ประจำ

```
vault_session:  local_57201435-c8f7-463a-b698-feca2f3fa77a  (cwd: C:\Vault\md)
reauth_session: local_f11bb3f3-a47b-4a7a-9402-e856b153cfda  (NotebookLM re-auth)
```

## NotebookLM Notebooks ที่มีอยู่แล้ว

| ธนาคาร | Notebook ID |
|---|---|
| BBL | 83ed779c-a71a-4e50-8ecf-1e2680b50b5f |
| KBANK | df5d2ba7-a149-4532-a93b-e41720e02f1d |
| LHBANK | 1856be8b-5453-4d0e-b24f-70463f82db6f |
| Mizuho | 32056d9e-c4eb-4642-add9-6736867c5e72 |
| KKP | a46e5331-c7c5-4c9c-839a-53a8e5cecbba |
| SMBT | 22a5dafe-a785-46e9-b307-ac6bdf02e320 |
| TTB | 56c4430e-c126-4836-b49e-ad623530f018 |
| IOB | a96bbbf7-b4bc-4ada-af6e-1c0be4aadd3d |
| RHB | 1ee8b226-ec25-4a0a-b1b1-be518133abe5 |
| CIMBT | 3ca2cb37-0792-46fb-a2e3-3619f7a4eef9 |
| Thai Credit | 7ca853bf-9f24-41fa-aa1d-464aab9b50b9 |

ถ้าธนาคารมี notebook แล้ว ไม่ต้องสร้างใหม่ ใช้ notebook เดิมได้เลย

---

## FLOW หลัก

### Step 1 — Auth Check

```
mcp__notebooklm-mcp__refresh_auth()
```

ถ้า error "Authentication expired":
1. `send_message(reauth_session, 'Run auth: & "$env:USERPROFILE\.local\bin\notebooklm-mcp-auth.exe"')`
2. รอ transcript ยืนยัน "SUCCESS — N cookies extracted"
3. `refresh_auth()` อีกครั้ง

### Step 2 — สร้าง Notebook (ถ้าธนาคารนี้ยังไม่มี)

```
notebook_create(title="[FI NAME] — [ชื่อเต็ม] Deep Dive")
```

บันทึก notebook_id ไว้ใช้ตลอด flow

### Step 2.5 — Configure Notebook with Research Skill (NEW notebooks only)

> ข้าม step นี้ถ้าใช้ notebook เดิมที่มีอยู่แล้ว — ทำเฉพาะ notebook ที่เพิ่งสร้างใน Step 2

ทำ 2 อย่างพร้อมกันใน same turn:

**A) Add skill.md as Source**

```
notebook_add_text(
  notebook_id=<id>,
  title="NotebookLM Research Skill — Master Prompt",
  content="""
# NotebookLM Research Skill — Master Prompt & skill.md

## Mission
Turn this notebook into a rigorous, source-grounded research workspace that can investigate any topic efficiently.

## Operating Principles
- Treat notebook sources as primary evidence.
- Synthesize across sources, not sequential summaries.
- Separate fact, interpretation, and speculation.
- Highlight contradictions, uncertainty, and missing context.
- Prefer structured outputs: tables, ranked lists, decision trees, argument maps.
- Ask clarifying questions when the task is underspecified.
- State when the notebook cannot support a conclusion.

## Default Answer Contract
Every substantial answer must include:
1. Direct answer
2. Evidence from sources
3. Contradictions / caveats
4. Best current interpretation
5. Research gaps
6. Next best questions

## Analysis Lenses
| Lens | ใช้เมื่อ |
|---|---|
| Overview | ต้องการภาพรวมทั้งหมด |
| Comparative | เปรียบเทียบมุมมอง / วิธี / กรณีศึกษา |
| Critical | หาจุดอ่อนและข้อโต้แย้ง |
| Method | ประเมินคุณภาพข้อมูลและการออกแบบวิจัย |
| Teaching | อธิบายเพื่อการเรียนรู้และจดจำ |
| Decision | แปลงผลลัพธ์เป็นตัวเลือกการตัดสินใจ |

## Shortcut Commands
| คำสั่ง | ผลลัพธ์ |
|---|---|
| /map | สร้าง topic map ของทั้ง notebook |
| /compare | เปรียบเทียบมุมมองที่แตกต่างกัน |
| /critique | ท้าทาย thesis หลักของ notebook |
| /evidence | สร้าง evidence table |
| /gaps | ระบุหลักฐานที่ขาดหาย |
| /teach | อธิบายเนื้อหาแบบบทเรียน |
| /brief | สรุปแบบ executive brief |
| /thesis | เสนอ thesis ที่สามารถป้องกันได้ |

## Style
- ภาษา: ภาษาไทยเป็นค่าเริ่มต้น / ภาษาอังกฤษเมื่อร้องขอ
- โทน: วิเคราะห์, กระชับ, ชัดเจน
- หลีกเลี่ยง: คำฟุ่มเฟือย, การซ้ำซ้อน, สำนวนจูงใจทั่วไป
"""
)
```

**B) Set Custom Instructions**

```
chat_configure(
  notebook_id=<id>,
  custom_instructions="""
You are a source-grounded research copilot for this notebook.

PRIMARY GOAL
Help me investigate any topic rigorously using only the sources inside this notebook
unless I explicitly ask for broader hypotheses.

CORE RULES
1. Use notebook sources as the ground truth.
2. Distinguish clearly between:
   - Facts supported by sources
   - Reasonable interpretations
   - Open questions / missing evidence
3. Synthesize across sources instead of summarizing one source at a time.
4. Surface disagreements, contradictions, and uncertainty early.
5. Never overstate confidence when the sources are thin, outdated, or conflicting.
6. When my request is vague, ask up to 3 clarifying questions before deep analysis.
7. When possible, cite the strongest source passages or pinpoint evidence.
8. Prefer compact structure, tables, and ranked lists over long generic prose.
9. End substantial answers with:
   - What we know
   - What is uncertain
   - What to check next

DEFAULT OUTPUT FORMAT
A. Direct answer
B. Key evidence across sources
C. Contradictions or blind spots
D. Best interpretation
E. Next research questions

ANALYSIS BEHAVIOR
- Extract concepts, claims, evidence, assumptions, counterarguments, and implications.
- Compare definitions when multiple sources use the same term differently.
- Identify methodological weakness, bias, or missing context when relevant.
- If the notebook does not contain enough evidence, say so explicitly.

STYLE
Concise, analytical, plain language, zero fluff, no marketing tone.
Use Thai unless I ask for English.
"""
)
```

### Step 3 — เริ่ม Dual Channel พร้อมกัน (same turn)

**Channel A — NotebookLM research_start:**
```
research_start(
  notebook_id=<id>,
  query="[FI] [ชื่อเต็ม] [ปีงบการเงิน] financial results NPL NIM CAR TFRS9 strategy annual report",
  mode="fast",
  source="web"
)
```

**Channel B — WebSearch task (start_task พร้อมกัน):**
prompt ควรครอบคลุม:
- สินทรัพย์, สินเชื่อ, เงินฝาก, กำไรสุทธิ, NIM, NPL, Coverage, CAR, CET1, LCR
- โครงสร้างผู้ถือหุ้น, กลยุทธ์, ข่าวล่าสุด
- Credit rating (TRIS/Fitch/Moody's/S&P/RAM)
- TFRS9 ECL methodology
- สำหรับ foreign branch: SWIFT, ที่อยู่, DPA membership, parent financials
- แหล่งข้อมูลหลัก: เว็บ IR ของธนาคาร, SET/BoT/DPA

### Step 4 — Poll research_status

```
research_status(notebook_id, max_wait=90, poll_interval=15)
```

### Step 5 — Add Sources ที่สำคัญ

จาก sources ที่ได้ ให้ add เข้า notebook โดยเน้น:
- PDF annual report / 56-1 One Report
- Pillar 3 / Basel III disclosure
- MD&A PDF
- Factsheet / investor presentation
- Credit rating release (Fitch/Moody's/TRIS)
- หน้า major shareholders

```
notebook_add_url(notebook_id, url) — ทีละ URL
```

### Step 6 — notebook_query (3 รอบ)

**รอบที่ 1 — Financial KPIs:**
```
"สรุปผลประกอบการ FY[ปี] ของ [FI]: กำไรสุทธิ, NIM, NPL ratio, Coverage ratio,
ROE, ROA, CAR, CET1, สินเชื่อรวม, เงินฝากรวม, สินทรัพย์รวม, credit cost พร้อม source"
```

**รอบที่ 2 — Ownership + Strategy + Ratings:**
```
"โครงสร้างผู้ถือหุ้นหลัก, กลยุทธ์ธุรกิจปัจจุบัน [ชื่อแผน],
credit rating จาก Fitch/Moody's/S&P/TRIS/RAM พร้อม outlook"
```

**รอบที่ 3 — TFRS9 + ECL + Segment risks:**
```
"TFRS9 ECL Stage 1/2/3 breakdown, PD/LGD/EAD approach, management overlay,
forward-looking macro variables, และ key loan segments ที่มีความเสี่ยงหลัก"
```

ถ้า auth หมดระหว่างนี้ → ทำ re-auth แล้ว retry query เดิม

### Step 7 — Vault MD Update

ส่ง message ไปที่ vault_session พร้อม data ครบจากทั้ง 2 channels:

```
send_message(vault_session, """
[ข้อมูลทั้งหมดจาก NotebookLM queries + WebSearch]

Full rebuild [filename].md ด้วยข้อมูล FY[ปี] จริง:
- อัพเดท frontmatter: updated: [today]
- อัพเดท simulation parameters ทั้งหมดด้วยค่าจริง
- เพิ่ม/rebuild sections: TFRS9/ECL, Credit Ratings,
  กลยุทธ์, IRRBB/ALM, Key Risks, Connections
- อัพเดท log.md ด้วย
""")
```

รอ transcript ยืนยัน "done (success)"

---

## Entity File Naming Convention

| ธนาคาร | ชื่อไฟล์ใน vault |
|---|---|
| Thai commercial banks | ชื่อย่อตัวพิมพ์เล็ก เช่น bbl.md, kbank.md, scb.md |
| Foreign branches | ชื่อย่อ + thai suffix เช่น rhbthai.md, iob.md, uob.md |
| Specialized banks | gsb.md, baac.md, ghb.md, sme.md |

ถ้าไม่แน่ใจชื่อไฟล์ ให้ `send_message(vault_session, "ls Wiki/entities/")` ก่อน

---

## Vault Entity Page Structure (Standard)

ทุก entity page ควรมี sections ต่อไปนี้ตามลำดับ:

1. YAML frontmatter (title, type, tags, created, updated)
2. Overview (2-3 ย่อหน้า)
3. Key Facts (table)
4. Default Simulation Parameters (table — ค่า FY จริงล่าสุด)
5. TFRS 9 / ECL (Stage breakdown table + methodology)
6. IRRBB / ALM
7. Credit Ratings
8. กลยุทธ์ / Strategy
9. Key Risks (numbered list)
10. Connections (WikiLinks)

---

## ข้อควรระวัง (Anti-patterns)

- **อย่า** รัน research_import — timeout เสมอ ใช้ notebook_add_url ทีละ URL แทน
- **อย่า** poll research_status ด้วย max_wait > 120 — ใช้ 90
- **อย่า** spawn WebSearch task แล้วปล่อยให้วน loop หา source ไม่หยุด — ใส่คำสั่งในตอนท้าย prompt ว่า "เมื่อได้ข้อมูลพอแล้ว ให้หยุดและสรุป อย่าวน loop"
- **อย่า** สร้าง notebook ใหม่ถ้ามีอยู่แล้วใน notebook list ด้านบน
- **อย่า** เขียนค่าประมาณเป็น simulation parameters — ต้องเป็นค่าจริงจากงบการเงินเท่านั้น
- **ถ้าเป็น notebook ใหม่ต้อง configure ก่อน query เสมอ** (Step 2.5) — อย่า skip แม้จะรีบ; custom instructions และ skill source จะทำให้ query quality ดีขึ้นมาก

---

## Coverage ratio ต่ำ = Red Flag

ถ้า coverage < 100%: แสดงความเสี่ยงชัดใน Key Risks
ถ้า NPL > 5%: ใส่ tag `distressed` ใน frontmatter
ถ้าธนาคารขาดทุน: ใส่ ROA ติดลบ และ note ใน simulation parameters

---

## ตัวอย่างการเรียกใช้

User: "ทำ ธ. กสิกรไทย"
→ ตรวจ notebook list → มี KBANK notebook แล้ว (df5d2ba7)
→ refresh_auth → research_start + start_task (parallel)
→ add key PDFs → query × 3
→ send data to vault_session → update kbank.md

User: "firesearch Deutsche Bank Thailand"
→ ไม่มี notebook → notebook_create
→ ดำเนิน dual-channel flow ตามปกติ
→ ตรวจชื่อไฟล์ใน vault → update deutschebank.md (หรือ dbthai.md)
