---
name: depomovsearch
version: "1.0"
description: |
  Research flow สำหรับ Vault DepoMov — ค้นคว้าเรื่อง Deposit Movement (NMD behavior, deposit beta, rate passthrough, run risk, behavioral segmentation, IRRBB linkage) จากหลายแหล่ง แล้ว ingest เข้า C:\Vault\DepoMov\Wiki\

  Trigger keywords:
  - "depomovsearch", "@depomov research", "@depomov firesearch"
  - "NMD", "non-maturing deposits", "deposit beta", "deposit repricing"
  - "rate passthrough", "run risk", "deposit run", "behavioral segmentation"
  - "IRRBB", "replicating portfolio", "decay rate", "core deposits"
  - "volatile deposits", "LCR", "NSFR", "deposit insurance"
  - "DPA", "ธปท. monetary policy", "Thai deposit market"
author: Vault DepoMov Research Stack
---

# DepoMov Search Skill — Deposit Movement Research Workflow

## วัตถุประสงค์

Skill นี้เลียนแบบ `bazisearch` / `firesearch` แต่ปรับสำหรับการค้นคว้าหัวข้อ **Deposit Movement**
(NMD behavior, deposit beta, rate passthrough, run risk, behavioral segmentation, IRRBB linkage)
ทำ Dual-Channel Research: NotebookLM (academic/regulatory sources) + WebSearch (practitioner, Thai FI context)
แล้ว ingest ผลลัพธ์ลง Vault DepoMov wiki

---

## Vault Target

**C:\Vault\DepoMov** — Deposit Movement Knowledge Wiki

| Folder | เนื้อหา |
|--------|--------|
| Wiki\concepts\ | ทฤษฎีและแนวคิด |
| Wiki\models\ | โมเดลและวิธีการ |
| Wiki\data\ | ข้อมูลและแหล่งข้อมูล |
| Wiki\regulation\ | กำกับดูแล |
| Wiki\entities\ | FI-specific deposit profiles |
| Wiki\synthesis\ | การวิเคราะห์และ application |

## Related Vaults

- `C:\Vault\Z` — NMD/IRRBB theory wiki (เชื่อมกันได้)
- `C:\Vault\md` — DPA/TFRS 9 FI entity wiki (เชื่อมกันได้)

---

## Notebook ID Table

| Notebook | ID | Sources | หัวข้อ |
|---|---|---|---|
| (ยังไม่มี) | — | — | — |

**Re-auth session**: local_f11bb3f3-a47b-4a7a-9402-e856b153cfda

---

## Flow — 8 Steps

### Step 1 — Auth Check

```
mcp__notebooklm-mcp__refresh_auth
```

ถ้าได้ error "Authentication expired" → ส่ง message ไป re-auth session ก่อน:
- session: `local_f11bb3f3-a47b-4a7a-9402-e856b153cfda`
- สั่ง: รัน `notebooklm-mcp-auth.exe` ที่ `C:\claude` แล้วรอ SUCCESS

แล้ว `refresh_auth` อีกครั้ง

---

### Step 2 — Create/Reuse Notebook

- ตรวจ **Notebook ID Table** ด้านบน
- ถ้ามีแล้ว → ใช้ notebook เดิม (ข้าม Step 2.5)
- ถ้าไม่มี → `notebook_create` — title: `"DepoMov — [หัวข้อ]"`

---

### Step 2.5 — Configure Notebook (NEW notebooks เท่านั้น)

ทำ 2 อย่างพร้อมกัน:

**A) Add Research Skill as Source**
`notebook_add_text` — title: "Research Skill"
content:
```
Rigorous research copilot. Synthesize across sources. Separate facts from interpretation.
Use tables and ranked lists. Answer in Thai. End: what we know / uncertain / check next.
```

**B) Set Custom Instructions**
`chat_configure` — custom_prompt:
```
Research copilot for Deposit Movement (DepoMov). Focus on: NMD behavior, deposit beta,
rate passthrough, run risk, behavioral segmentation, IRRBB framework, Thai FI deposit dynamics.
Use Thai. Be analytical. Use tables.
```

---

### Step 3 — Dual Channel Research (parallel)

**Channel A — NotebookLM research_start:**
```
notebook_id: [ID from Step 2]
query: "[หัวข้อ] deposit movement NMD IRRBB behavioral model academic regulatory"
mode: fast
source: web
```

**Channel B — WebSearch (6–8 queries):**
ครอบหัวข้อจากหลายมุม:
1. นิยามและทฤษฎีพื้นฐาน (academic definition)
2. วิธีการวัดและโมเดล (quantitative methods)
3. มาตรฐานกำกับดูแล (Basel, ธปท., BIS)
4. Thai FI context และ local dynamics
5. Practitioner perspective (bank ALM, treasury)
6. Case studies และ empirical evidence
7. ความเชื่อมโยงกับ IRRBB / LCR / NSFR
8. แหล่งข้อมูล academic + regulatory

---

### Step 4 — Poll research_status

```
poll_interval: 30 วินาที
max_rounds: 6
```

---

### Step 5 — research_import

import ทั้งหมด (ไม่ต้องระบุ `source_indices`)

---

### Step 6 — Queries ×3–4 (refresh_auth ก่อนทุก query)

ปรับตาม domain ของหัวข้อ:

| Query type | เนื้อหา |
|-----------|--------|
| `/map` | topic map — ความสัมพันธ์กับ concept อื่นใน DepoMov domain |
| `/evidence` | evidence table — งานวิจัย, empirical findings, ตัวเลขสำคัญ |
| `/compare` | เปรียบเทียบแนวทาง / โมเดล / ผลการศึกษาต่างๆ |
| `/methodology` | step-by-step method สำหรับ implementation |

---

### Step 7 — Compile Report

รวม query results + WebSearch findings → **structured markdown report** ครอบคลุม:
- Core definition และ theory
- Key metrics และ parameters
- Regulatory framework
- Thai FI context
- Implementation methodology
- Open questions / uncertainties

---

### Step 8 — Vault Update

ส่งผลไปที่ **Open Vault DepoMov session** (code session ที่ `C:\Vault\DepoMov`)
สร้าง/อัพเดต wiki pages ที่เหมาะสม + `index.md` + `log.md`

---

## Standard Page Structure (DepoMov Wiki)

```markdown
---
title: [ชื่อ concept ภาษาไทย / English]
date: [วันที่]
tags: [NMD, deposit-beta, IRRBB, ...]
type: concept | model | regulation | entity | synthesis
source: NotebookLM Notebook — [ชื่อ notebook]
status: draft | in-progress | complete
---

## Overview
[ชื่อ, ประเภท, บทบาทใน DepoMov framework]

## Definition (นิยาม)
[นิยามจาก academic / regulatory sources]

## Theory & Mechanics (ทฤษฎี)
[กลไกและที่มาของ behavior]

## Key Parameters (พารามิเตอร์หลัก)
[ตาราง parameters, typical ranges, calibration approach]

## Measurement Methods (วิธีวัด)
[quantitative approaches, data requirements]

## Regulatory Context (กำกับดูแล)
[Basel, ธปท., BIS guidance]

## Thai FI Context
[ลักษณะเฉพาะของตลาดเงินฝากไทย]

## IRRBB / ALM Linkage
[ความเชื่อมโยงกับ IRRBB, NII, EVE]

## Related Concepts (backlinks)
- [[concept-a]]
- [[concept-b]]

## References
- [แหล่งอ้างอิง]
- NotebookLM: [URL]
```

---

## Typical Wiki Pages Created

| Path | เนื้อหา |
|------|--------|
| `Wiki/concepts/[concept].md` | ทฤษฎีและนิยาม |
| `Wiki/models/[model].md` | โมเดลและวิธีการ |
| `Wiki/regulation/[regulation].md` | มาตรฐานกำกับดูแล |
| `Wiki/entities/[fi-name]-deposit-profile.md` | FI-specific |
| `Wiki/synthesis/[topic]-synthesis.md` | การวิเคราะห์ประยุกต์ |
| `Wiki/sources/notebooklm.md` | อัพเดต Notebook ID Table |

---

## Domain Keywords

NMD, non-maturing deposits, deposit beta, deposit repricing, rate passthrough,
run risk, deposit run, behavioral segmentation, IRRBB, replicating portfolio,
decay rate, core deposits, volatile deposits, LCR, NSFR, deposit insurance,
DPA, ธปท. monetary policy, Thai deposit market

---

## Anti-Patterns (ห้ามทำ)

- ❌ สร้าง notebook ซ้ำถ้ามีอยู่แล้วใน Notebook ID Table
- ❌ ใช้ `research_import` (always times out) — ใช้ `add_sources` แทน
- ❌ ใช้ `max_wait > 90` สำหรับ `research_status`
- ❌ ลืม `refresh_auth` ก่อนทุก query
- ❌ ใส่ข้อมูล speculative โดยไม่ระบุว่าเป็น interpretation
- ❌ Merge concepts ที่ต่างกัน (เช่น deposit beta กับ rate passthrough) โดยไม่แยกแยะ
- ❌ ลืม cite source สำหรับทุก empirical claim

## Red Flags (ต้องระบุในหน้า wiki)

- ⚠️ Concept ที่ differ ระหว่าง Thai FI practice กับ Basel standard → ต้องระบุทั้งสองมุม
- ⚠️ Parameter ที่ไม่มี empirical benchmark สำหรับ Thai market → ต้องระบุว่าเป็น assumption
- ⚠️ Model ที่ theoretical แต่ยังไม่ได้ implement ใน practice → ต้องแยกแยะ

---

## ตัวอย่างการเรียกใช้

**Case 1 — Concept ใหม่:**
```
depomovsearch deposit beta Thai market
```
→ Auth → Create notebook "DepoMov — Deposit Beta" → Step 2.5 → Dual Channel →
Poll → Import → Query ×3 → สร้าง `Wiki/concepts/deposit-beta.md`

**Case 2 — Regulatory topic:**
```
@depomov research IRRBB NMD guidelines
```
→ Auth → Create notebook "DepoMov — IRRBB NMD" → ... →
สร้าง `Wiki/regulation/irrbb-nmd-guidelines.md`

**Case 3 — Entity profile:**
```
depomovsearch SCB deposit structure
```
→ Auth → Create notebook "DepoMov — SCB Deposit Profile" → ... →
สร้าง `Wiki/entities/scb-deposit-profile.md`

---

## วิธีอัปเดต Notebook ID Table

เมื่อสร้าง notebook ใหม่สำเร็จ ให้เพิ่มแถวใน table ด้านบน:
```
| [TOPIC] | [notebook UUID] | [จำนวน sources] | [หัวข้อสั้น] |
```

แล้วอัพเดตไฟล์ `Wiki/sources/notebooklm.md` ใน Vault DepoMov ด้วย
