---
title: BaZi × AI / LLM Benchmarking
type: concept
tags: [chinese-metaphysics, ai, llm, benchmarking, symbolic-reasoning, nlp]
aliases: ["Bazi AI", "BaZi LLM", "BaZi Benchmark", "Chinese Metaphysics AI", "BaziQA"]
sources: [Raw/arxiv-bazi-llm.md]
created: 2026-06-13
updated: 2026-06-13
---

การใช้ [[Bazi (八字)]] เป็น test bed สำหรับประเมินความสามารถของ Large Language Models ในการใช้เหตุผลเชิงสัญลักษณ์และการผสานเวลา (temporal integration) ห่วงโซ่สัญลักษณ์ Stem→Element→Ten God→Pattern→การทำนาย ต้องการการผสาน [[วงจรดวงชะตา (大運)]] × Annual Luck ซ้อนกัน ซึ่ง frontier LLMs ยังทำได้ไม่ดี (32–37% accuracy vs. baseline 25%) (arXiv 2510.23337; arXiv 2602.12889)

## งานวิจัยหลัก

- **BaZi Character Simulation Benchmark (arXiv 2510.23337)** — Zheng et al. 2025; Celebrity 50 dataset (488 QA); LLM ที่ augment ด้วย Bazi ทำได้ดีกว่า GPT-5-Mini 62.6% และ DeepSeek-v3 30.3% ในการจำลองบุคลิกภาพ
- **BaziQA Benchmark (arXiv 2602.12889)** — Chen & Liu 2026; 200 MCQ จาก Global Fortune-teller Competition; frontier LLMs ได้ 32–37% (baseline 25%); temporal integration (大運×流年) ยากที่สุด (23–40%)
- **Health-LLM Agent (ResearchGate, 2024)** — ประยุกต์ [[ธาตุทั้งห้า (Five Elements)]] เป็น AI diagnostic ontology สำหรับ TCM; 81% ความแม่นยำ; 92% practitioner validation → ดู [[Bazi Health Prognosis × Five Elements × TCM]]

## บริบทตลาด

- ตลาด AI metaphysics จีน ¥12B+ (2024) เติบโต 43.7% ต่อปี
- "DeepSeek fortune-telling" มีโพสต์ WeChat 2M+ ในเดือนเดียว (2025)
- AI Bazi reading apps ที่ผู้ใช้ treat as authoritative — แต่ยังไม่มีการตรวจสอบความแม่นยำกับผลลัพธ์จริง

## ข้อจำกัดที่พบ

- **Symbol Grounding Problem** — AI จัดการสัญลักษณ์ Bazi ได้ทางไวยากรณ์ (syntax) แต่ขาด temporal/contextual grounding — แสดง gap ระหว่าง symbol manipulation กับ genuine understanding
- **ข้อจำกัดการคำนวณ** — LLM ส่วนใหญ่ยังสร้างดวงชะตา Bazi จากข้อมูลวันเกิดไม่ได้ถูกต้องโดยไม่มี tool assistance

## ข้อถกเถียงหลัก ⚠️

Benchmark ใช้ "คำตอบผู้เชี่ยวชาญ" เป็น ground truth แต่ถ้า [[สำนักและวิธีตีความ Bazi]] คลาสสิกกับสมัยใหม่ให้คำตอบที่ขัดแย้งกันสำหรับดวงเดียวกัน — ground truth ของ benchmark เองก็ถูกตั้งคำถาม ผู้ปฏิบัติมองว่า AI เป็นเครื่องมือช่วยคำนวณแต่ไม่สามารถแทนการอ่านแบบ holistic ของ practitioner ได้

## Related Concepts

- [[Bazi (八字)]] — ระบบแม่
- [[Bazi Health Prognosis × Five Elements × TCM]] — Health-LLM Agent เป็นสะพานระหว่าง AI benchmarking และ health prognosis
- [[สำนักและวิธีตีความ Bazi]] — ความขัดแย้งระหว่างสำนักสร้างปัญหา ground truth สำหรับ AI benchmarks
- [[สิบเทพ (十神)]] — Ten Gods เป็น symbolic chain ที่ LLM ต้องเดินผ่าน
- [[วงจรดวงชะตา (大運)]] — Temporal integration ของ LP × Annual Luck คือ hardest subtask ใน BaziQA
