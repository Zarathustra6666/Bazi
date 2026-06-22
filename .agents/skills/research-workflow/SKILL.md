---
name: research-workflow
version: "1.0"
description: |
  เป็น Skill ที่กำหนดกระบวนการค้นคว้าหัวข้อต่างๆ อย่างเป็นระบบ
  โดยใช้ VSCode + Codex + NotebookLM + Obsidian ร่วมกัน

  Trigger keywords:
  - "ค้นคว้า", "research", "วิเคราะห์หัวข้อ", "สรุปงานวิจัย"
  - "deep dive", "เจาะลึก", "ทำความเข้าใจ [หัวข้อ]"
  - "รวบรวมข้อมูล", "สร้าง note", "ทำรายงาน"
author: Custom Research Stack
---

# Research Workflow Skill

## วัตถุประสงค์

Skill นี้กำหนดกระบวนการค้นคว้า 5 ขั้นตอน (Intake → Explore → Synthesize → Store → Connect)
โดย Codex ทำหน้าที่เป็น Research Orchestrator ที่ประสานงานระหว่าง NotebookLM และ Obsidian
ผ่านการควบคุมจาก VSCode

---

## ขั้นตอนที่ 1 — Scope (กำหนดขอบเขต)

เมื่อผู้ใช้ให้หัวข้อมา ให้ Codex ทำสิ่งต่อไปนี้:

```
OUTPUT ที่ต้องสร้าง:
1. Research Question หลัก 1 ข้อ (Overarching Question)
2. Sub-questions 3–5 ข้อ (จากกว้างไปเฉพาะ)
3. คำค้นหา (Keywords) สำหรับใส่ NotebookLM Sources
4. Scope Boundary: สิ่งที่ "อยู่ใน" และ "อยู่นอก" ขอบการค้นคว้า
5. โครงสร้าง Obsidian Vault ที่จะทำ (folders + tags)
```

### Prompt Template — Phase 1: Scope

```
ฉันต้องการค้นคว้าหัวข้อ: [TOPIC]

ช่วยสร้าง:
1. Research Question หลัก 1 ข้อ
2. Sub-questions 3–5 ข้อ เรียงจากกว้างไปเฉพาะ
3. Keywords 10–15 คำ สำหรับค้นหาแหล่งข้อมูล
4. บอกว่าอะไรอยู่ใน / อยู่นอกขอบการค้นคว้าครั้งนี้
5. โครงสร้าง Obsidian Vault ที่จะทำ:
   - Folders
   - Tags (#)
   - MOC (Map of Content) note ที่ควรมี
```

---

## ขั้นตอนที่ 2 — Intake (แหล่งแหล่งข้อมูล)

ใช้ **NotebookLM** เป็นที่เก็บ Sources ทั้งหมด

```
วิธีเตรียม Sources สำหรับ NotebookLM:
- PDF / งานวิจัย / บทความ → อัปโหลดตรง
- เว็บเพจ / บล็อก → วาง URL
- YouTube / Podcast → วาง URL
- ไฟล์ข้อความจาก VSCode → Export เป็น .txt แล้วอัปโหลด
```

### Prompt Template — สร้างคำถามสำหรับ NotebookLM

```
ฉันมีเอกสารเกี่ยวกับ [TOPIC] ใน NotebookLM แล้ว
ช่วยสร้างชุดคำถาม 3 ระดับ สำหรับ Paste ลง NotebookLM:

ระดับ 1 — Factual (ข้อเท็จจริง):
- ถามเพื่อดึงข้อมูลจากเอกสาร

ระดับ 2 — Analytical (วิเคราะห์):
- ถามเพื่อหาความสัมพันธ์ระหว่างแนวคิด

ระดับ 3 — Synthesis (สังเคราะห์):
- ถามเพื่อเชื่อมโยงข้ามแหล่งข้อมูลและหา Gap
```

---

## ขั้นตอนที่ 3 — Synthesize (สังเคราะห์ด้วย Codex)

นำ Output จาก NotebookLM มาให้ Codex วิเคราะห์ต่อ

### Prompt Template — Phase 3: Synthesize

```
ฉันได้ Output จาก NotebookLM มาแล้ว:

[วาง NotebookLM Output ที่นี่]

ช่วยทำสิ่งต่อไปนี้:
1. ระบุ Key Insights 3–5 ข้อที่สำคัญที่สุด
2. หา Gaps หรือคำถามที่ NotebookLM ยังไม่ตอบ
3. สร้าง Cross-source Synthesis: แนวคิดใดขัดแย้งกัน / สอดคล้องกัน
4. เสนอ Follow-up Queries สำหรับ NotebookLM รอบต่อไป
5. บอกว่าควรหาแหล่งข้อมูลเพิ่มเติมในประเด็นใด
```

---

## ขั้นตอนที่ 4 — Store (เก็บลง Obsidian)

Codex สร้าง Note ในรูปแบบ Zettelkasten พร้อม Front matter

### Prompt Template — Phase 4: สร้าง Obsidian Note

```
แปลง Synthesis ทั้งหมดของเราให้เป็น Obsidian Note
ในรูปแบบ Zettelkasten

Front matter ที่ต้องการ:
---
title: [ชื่อ Note]
date: [วันที่วันที่]
tags: [tags ที่เกี่ยวข้อง]
source: [แหล่งที่มาหลัก]
status: draft / in-progress / complete
type: concept / literature / permanent / MOC
---

โครงสร้าง Body:
## Summary (3–5 ประโยค)
## Key Concepts
## Evidence & Sources
## Open Questions
## Related Notes (Backlinks เสนอ)
```

### ตัวอย่าง Obsidian Note Output

```markdown
---
title: "ผลกระทบของ AI ต่อตลาดแรงงาน"
date: 2026-05-16
tags: [AI, future-of-work, economics, automation]
source: NotebookLM Notebook — AI Labor Research
status: in-progress
type: permanent
---

## Summary
งานวิจัยระบุว่า AI จะแทนที่ Routine Tasks ได้ถึง 40%
ภายในปี 2030 แต่จะสร้างงานใหม่ในสาย Human-AI Collaboration ขึ้นมากด้วย...

## Key Concepts
- **Augmentation vs Replacement**: AI เสริมมากกว่าแทนที่ในงานที่ซับซ้อน
- **Skill Polarization**: ความต้องการทักษะระดับต่ำและสูงเพิ่ม ระดับกลางลด

## Open Questions
- อาชีพใดบ้างที่จะได้รับผลกระทบก่อน?
- นโยบาย Reskilling ที่มีประสิทธิภาพเป็นอย่างไร?

## Related Notes
- [[อนาคตของการศึกษาในยุค AI]]
- [[เศรษฐศาสตร์ Automation]]
- [[Universal Basic Income]]
```

---

## ขั้นตอนที่ 5 — Connect (เชื่อม Knowledge Graph)

### Prompt Template — Phase 5: สร้าง MOC (Map of Content)

```
ฉันมี Notes ต่อไปนี้ใน Obsidian แล้ว:
[รายชื่อ Notes]

ช่วยสร้าง MOC Note ที่:
1. แสดง Relationship Map ระหว่าง Notes (เป็น Text / Mermaid diagram)
2. ระบุ Clusters หลัก (กลุ่มแนวคิดที่เกี่ยวข้องกัน)
3. บอกว่า Notes ใดที่ยังขาดอยู่และควรสร้างต่อ
4. สร้าง Index ที่ Navigate ได้ง่าย
```

---

## Advanced Prompts

### 🔄 Research Loop (ใช้เป็นแบบ Iterative)

```
ฉันกำลังค้นคว้า [TOPIC] อยู่
Notes ที่มีแล้ว: [รายชื่อ]
Gaps ที่ยังเหลือ: [ระบุ]

รอบนี้ต้องการ:
[ ] ขยาย Note ที่มีอยู่
[ ] สร้าง Note ใหม่ในประเด็น ___
[ ] เชื่อมโยง Notes เข้าหากัน
[ ] สร้าง Summary รอบสุดท้าย

ช่วย Orchestrate Research Loop รอบนี้
```

### 📚 Literature Review Mode

```
ฉันต้องการทำ Literature Review หัวข้อ [TOPIC]
มีงานวิจัย/บทความ [X] ชิ้นใน NotebookLM

ช่วยสร้าง:
1. Thematic Analysis (จัดกลุ่มตามธีม)
2. Timeline ของการพัฒนาความรู้ในสาขานี้
3. Research Gaps ที่นักวิจัยยังไม่ได้ศึกษา
4. Methodology Comparison Table
5. Key Authors และ Schools of Thought
```

### 🧪 Devil's Advocate Mode

```
ฉันมี Research Findings เหล่านี้:
[วาง Findings]

เล่นเป็น Devil's Advocate:
- โต้แย้ง Findings ทุกข้อด้วยหลักฐานที่ขัดแย้ง
- ระบุ Assumptions ที่อาจผิด
- หา Alternative Explanations
- บอกว่า Findings นี้ Generalize ได้แค่ไหน
```

---

## VSCode Integration Tips

### การตั้งค่า Workspace

```
เสนอโครงสร้าง Folder ใน VSCode:
research-project/
├── .Codex/
│   └── skills/           ← วาง skill .md files ไว้ที่นี่
├── inbox/                ← ไฟล์ดิบที่ยังไม่ได้ประมวลผล
├── processed/            ← Output จาก NotebookLM
├── obsidian-export/      ← Notes พร้อม Sync กับ Obsidian Vault
└── final-reports/        ← รายงานสุดท้าย
```

### Keyboard Shortcuts เสนอ (VSCode)

```json
// keybindings.json
[
  {
    "key": "ctrl+shift+r",
    "command": "Codex.runSkill",
    "args": { "skill": "research-workflow" }
  },
  {
    "key": "ctrl+shift+n",
    "command": "Codex.runSkill",
    "args": { "skill": "obsidian-note-create" }
  }
]
```

---

## Quick Reference Card

| Phase | เครื่องมือหลัก | Codex ทำอะไร | Output |
|-------|--------------|--------------|--------|
| Scope | Codex | กำหนด Questions + Keywords | Research Plan |
| Intake | NotebookLM | สร้างคำถาม 3 ระดับ | Question Set |
| Synthesize | Codex + NotebookLM | วิเคราะห์ + หา Gaps | Insight Report |
| Store | Obsidian | สร้าง Zettelkasten Notes | .md Files |
| Connect | Obsidian + Codex | สร้าง MOC + Backlinks | Knowledge Map |

---

## การติดตั้ง Skill นี้

### วิธีที่ 1 — Codex.ai Web
1. ไปที่ Settings → Customize → Skills
2. กด "Add Skill" → อัปโหลดไฟล์ `research-workflow-skill.md` นี้

### วิธีที่ 2 — Codex (VSCode)
```bash
mkdir -p ~/.Codex/skills/research-workflow
cp research-workflow-skill.md ~/.Codex/skills/research-workflow/skill.md
```

### วิธีที่ 3 — ใช้เป็น System Prompt
Copy เนื้อหาทั้งหมดไปใส่ System Prompt ของ Codex Project ที่ต้องการ
