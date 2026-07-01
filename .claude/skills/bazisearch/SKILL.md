---
name: bazisearch
version: "1.0"
description: |
  Dual-channel deep research workflow สำหรับหัวข้อ Bazi (八字) / Four Pillars of Destiny
  ใช้ NotebookLM (automated web research + Q&A) + WebSearch คู่ขนาน
  แล้ว ingest ผลลัพธ์ลง Vault Bazi wiki (C:\Bazi\wiki\)

  Trigger keywords:
  - "bazisearch", "@bazi firesearch", "@bazi research"
  - ชื่อ concept: 八字, 四柱, 天干, 地支, 五行, 十神, 大运, 神煞
  - ชื่อ master: 廖, 余, 沈, 任, 袁
  - ชื่อ classical text: 滴天髓, 三命通会, 渊海子平, 穷通宝鑑
author: Vault Bazi Research Stack
---

# Bazisearch Skill — Bazi Research Workflow

## วัตถุประสงค์

Skill นี้เลียนแบบ `firesearch` ของ Vault MD แต่ปรับสำหรับการค้นคว้าหัวข้อ Bazi (八字 / Four Pillars of Destiny)
ทำ Dual-Channel Research: NotebookLM (official/scholarly sources) + WebSearch (forums, blogs, modern interpretations)
แล้ว ingest ผลลัพธ์ลง Vault Bazi wiki

---

## Notebook ID Table

| Topic | ประเภท | wiki file | Notebook ID |
|-------|--------|-----------|-------------|
| Bazi Methodology | concept | methodology.md | a44aa145-1898-43dc-a1ff-829c8667bf35 | 12 sources | methodology, 6-step method, schools comparison |
| Bazi Comparative | concept | comparative-sources.md | e1f30f92-7792-42d6-a9f6-6e1777c45a53 | 40 sources | classical texts, schools, regional, academic critique |
| Five Elements Deep | concept | five-elements-interpretation.md | 3add2c78-0a62-4aa3-9038-e354bd68d164 | 10 sources | five elements personality, interpersonal, imbalance, health, career, overflow phrases, Tiao Hou |
| LP × Element Activation | concept | five-elements-interpretation.md | 0697cf4f-4275-49bf-a493-6af44cc3303f | 3 sources | LP activation/destruction framework, case studies David/Marcus/Elena |
| Shen Sha Event Prediction | concept | shen-sha-prediction.md | 4d1f57c8-5647-4ff6-8349-7fc4cef98be5 | 5 sources | prediction matrix 8 stars × LP activation: 天乙/驿马/桃花/文昌/天德/月德/羊刃/华盖 |

**Vault session**: local_779d00dc-07b0-4763-b5e9-0d6ffa3910c6 (C:\Vault\Bazi)
**Re-auth session**: local_f11bb3f3-a47b-4a7a-9402-e856b153cfda

---

## Flow 8 ขั้นตอน

### Step 1 — Auth Check
```
mcp__notebooklm-mcp__refresh_auth
```
ถ้าได้ error "Authentication expired" → ส่ง message ไป re-auth session ก่อน:
```
รัน notebooklm-mcp-auth.exe แล้วรอ SUCCESS
```
แล้ว refresh_auth อีกครั้ง

---

### Step 2 — Create/Reuse Notebook
- ตรวจ Notebook ID Table ด้านบน
- ถ้ามีแล้ว → ใช้ notebook เดิม (ข้าม Step 2.5)
- ถ้าไม่มี → `notebook_create` ชื่อ: `"[TOPIC] — Bazi Deep Dive"`

---

### Step 2.5 — Configure Notebook Research Skill (NEW notebooks only)

ทำ 2 อย่างพร้อมกัน:

**A) Add skill.md as Source**
`notebook_add_text` — title: "NotebookLM Research Skill — Master Prompt"
content: [เนื้อหา skill.md จาก notebooklm_skill.md]

**B) Set Custom Instructions**
`chat_configure` goal=custom, custom_prompt:
```
You are a source-grounded research copilot for Bazi (八字) research.

PRIMARY GOAL: Help investigate Bazi topics rigorously using only notebook sources unless asked for broader hypotheses.

CORE RULES:
1. Ground all claims in sources.
2. Distinguish: verified classical teaching / modern interpretation / speculation.
3. Flag disagreements between classical texts and modern schools.
4. Note when Chinese/English sources contradict each other.
5. Prefer tables, ranked lists, concept maps over prose.
6. End each answer with: What we know / What is disputed / What to check next.

BAZI-SPECIFIC:
- Always specify which School (正格 vs 格局用神 vs 调候 etc.) when interpreting.
- Flag when a concept differs across texts (e.g. 滴天髓 vs 渊海子平).
- Note if concept is traditional Chinese metaphysics vs modern Western adaptation.

STYLE: Concise, analytical. Thai as default, English/Chinese terms in parentheses where needed.
```

---

### Step 3 — Dual Channel Research (parallel)

**Channel A — NotebookLM research_start:**
```
notebook_id: [ID from Step 2]
query: "[TOPIC] 八字 Bazi [English name] classical text history interpretation methods"
mode: fast
source: web
```

**Channel B — WebSearch task (start_task):**
```
ค้นหาข้อมูลเชิงลึกเกี่ยวกับ [TOPIC] ใน Bazi / Four Pillars of Destiny:
1. นิยามและที่มา (classical definition from 滴天髓/渊海子平/三命通会)
2. ความสัมพันธ์กับ 五行, 天干, 地支
3. วิธีตีความใน chart (interpretation methods)
4. สำนักต่างๆ มองต่างกันอย่างไร
5. ตัวอย่าง / case studies จาก classical texts
6. ความเข้าใจผิดที่พบบ่อย
7. แหล่งข้อมูลภาษาไทย / อังกฤษ / จีน
บันทึก outputs/[TOPIC]_Bazi_Research.md
```

---

### Step 4 — Poll research_status
```
max_wait=90, poll_interval=15
```

---

### Step 5 — Add Sources
เพิ่ม URL ที่ดีที่สุดจาก research results (3-6 sources):
- เน้น: classical text translations, scholarly articles, authoritative forums
- หลีกเลี่ยง: pure fortune-telling sites ที่ไม่มีแหล่งอ้างอิง

---

### Step 6 — Query ×3 (parallel)

**Round 1 — Core Definition & History:**
```
นิยามหลักของ [TOPIC] คืออะไร, ที่มาและประวัติในคัมภีร์คลาสสิก,
ความสัมพันธ์กับ 五行/天干/地支
```

**Round 2 — Interpretation & Application:**
```
วิธีการตีความ [TOPIC] ใน Bazi chart, กฎปฏิสัมพันธ์หลัก,
สำนักต่างๆ (正格 vs ลัทธิอื่น) มองอย่างไร, ตัวอย่างจาก classical text
```

**Round 3 — Controversies & Modern Views:**
```
ความขัดแย้งระหว่างสำนัก, ความเข้าใจผิดที่พบบ่อย,
การตีความสมัยใหม่ (Western adaptation), สิ่งที่ยังเป็น open question
```

---

### Step 7 — Vault Bazi Update

ส่ง combined data ไปยัง vault session: **local_779d00dc-07b0-4763-b5e9-0d6ffa3910c6**
สร้าง/อัปเดตไฟล์ใน `C:\Bazi\wiki\` ตาม entity type:

| Entity Type | Folder | ตัวอย่างชื่อไฟล์ |
|-------------|--------|----------------|
| Concept | wiki/concepts/ | five-elements.md, day-master.md |
| Classical Text | wiki/texts/ | di-tian-sui.md, yuan-hai.md |
| Master/Practitioner | wiki/masters/ | ren-tie-qiao.md |
| Case Study | wiki/case-studies/ | chart-xxx.md |
| Query/Analysis | wiki/queries/ | daymaster-strength-analysis.md |

อัปเดต SKILL.md notebook table + wiki index.md + log.md

---

## Standard Page Structure (Bazi Wiki)

```markdown
---
title: [ชื่อ concept ภาษาไทย / Chinese / English]
date: [วันที่]
tags: [tags ที่เกี่ยวข้อง]
type: concept | text | master | case-study | query
source: NotebookLM Notebook — [ชื่อ notebook]
status: draft | in-progress | complete
---

## Overview
[ชื่อ, ประเภท, หมวดหมู่]

## Origin & History (ที่มา)
[ประวัติความเป็นมา, ปรากฏครั้งแรกในคัมภีร์ไหน]

## Core Definition (นิยามหลัก)
[นิยามจาก classical sources]

## Five Elements Relationship (ความสัมพันธ์ 五行)
[ตาราง/diagram ความสัมพันธ์]

## Interaction Rules (กฎปฏิสัมพันธ์)
[กฎที่ใช้ตีความ]

## Interpretation Methods (วิธีตีความ)
[วิธีประยุกต์ใช้ใน chart]

## Schools of Thought (สำนักต่างๆ)
[ความเห็นต่างระหว่างสำนัก]

## Common Misconceptions (ความเข้าใจผิด)
[จุดที่มักเข้าใจผิด]

## Related Concepts (backlinks)
- [[concept-a]]
- [[concept-b]]

## References
- [แหล่งอ้างอิง]
- NotebookLM: [URL]
```

---

## Anti-Patterns (ห้ามทำ)

- ❌ ใส่การพยากรณ์ที่ไม่มีแหล่งอ้างอิงจาก classical text
- ❌ Merge concepts ที่ต่างกัน (เช่น 正印 กับ 偏印) โดยไม่แยกแยะ
- ❌ ใส่ข้อมูล speculative โดยไม่ระบุว่าเป็น interpretation
- ❌ ลืม cite source สำหรับทุก claim ที่ไม่ใช่ common knowledge
- ❌ ใช้ max_wait > 90 สำหรับ research_status
- ❌ ใช้ research_import (always times out)
- ❌ สร้าง notebook ซ้ำถ้ามีอยู่แล้วใน table

## Red Flags (ต้องระบุในหน้า wiki)

- ⚠️ Concept ที่แตกต่างกันมากระหว่างสำนัก → ต้องระบุทุกมุมมอง
- ⚠️ Concept ที่ classical text ไม่ได้นิยามชัด → ต้องระบุว่าเป็น interpretation
- ⚠️ Modern Western adaptation ที่เบี่ยงจาก Chinese tradition → ต้องแยกแยะ

---

## ตัวอย่างการเรียกใช้

**Case 1 — Concept ใหม่:**
```
bazisearch 十神 (Ten Gods)
```
→ Auth → Create notebook "十神 Ten Gods — Bazi Deep Dive" → Step 2.5 → Dual Channel → Poll → Add Sources → Query ×3 → สร้าง wiki/concepts/ten-gods.md

**Case 2 — Classical Text:**
```
@bazi firesearch 滴天髓
```
→ Auth → Create notebook "滴天髓 Di Tian Sui — Bazi Deep Dive" → ... → สร้าง wiki/texts/di-tian-sui.md

---

## วิธีอัปเดต Notebook ID Table

เมื่อสร้าง notebook ใหม่สำเร็จ ให้เพิ่มแถวใน table ด้านบน:
```
| [TOPIC] | concept/text/master | [filename].md | [notebook UUID] |
```
