---
title: BaZi × AI / LLM Benchmarking
type: concept
tags: [chinese-metaphysics, ai, llm, benchmarking, symbolic-reasoning, nlp]
aliases: ["Bazi AI", "BaZi LLM", "BaZi Benchmark", "Chinese Metaphysics AI", "BaziQA"]
sources: [Raw/arxiv-bazi-llm.md, NLM/e1f30f92]
created: 2026-06-13
updated: 2026-06-15
---

การใช้ [[Bazi (八字)]] เป็น test bed สำหรับประเมินความสามารถของ Large Language Models ในการใช้เหตุผลเชิงสัญลักษณ์และการผสานเวลา (temporal integration) ห่วงโซ่สัญลักษณ์ Stem→Element→Ten God→Pattern→การทำนาย ต้องการการผสาน [[วงจรดวงชะตา (大運)]] × Annual Luck ซ้อนกัน ซึ่ง frontier LLMs ยังทำได้ไม่ดี (32–37% accuracy vs. baseline 25%) (arXiv 2510.23337; arXiv 2602.12889)

## งานวิจัยหลัก

- **BaZi Character Simulation Benchmark (arXiv 2510.23337)** — Zheng et al. 2025; Celebrity 50 dataset (488 QA); LLM ที่ augment ด้วย Bazi ทำได้ดีกว่า GPT-5-Mini 62.6% และ DeepSeek-v3 30.3% ในการจำลองบุคลิกภาพ
- **BaziQA Benchmark (arXiv 2602.12889)** — Chen & Liu 2026; 200 MCQ จาก Global Fortune-teller Competition; frontier LLMs ได้ 32–37% (baseline 25%); temporal integration (大運×流年) ยากที่สุด (23–40%)
- **Health-LLM Agent (ResearchGate, 2024)** — ประยุกต์ [[ธาตุทั้งห้า (Five Elements)]] เป็น AI diagnostic ontology สำหรับ TCM; 81% ความแม่นยำ; 92% practitioner validation → ดู [[Bazi Health Prognosis × Five Elements × TCM]]

## แอปพลิเคชัน AI Bazi ในตลาด

**Master Mystic AI Bazi Reading (Sean Chan):**
แอปอ่านดวง Bazi ด้วย AI ที่ให้ผลลัพธ์ครอบคลุม: บุคลิกภาพ, อาชีพ, ความรัก, ความมั่งคั่ง, สุขภาพ และการพยากรณ์รายปี — เป็นตัวอย่างของการประยุกต์ commercial AI กับ Chinese Metaphysics

**Head-System-816 (Reddit community):**
แหล่งชุมชนที่แนะนำ free Bazi calculator เป็น "Chinese MBTI shortcut" — แสดงให้เห็นว่า Bazi ถูก democratize ผ่าน AI ในฐานะเครื่องมือ self-discovery ที่เข้าถึงง่าย โดยไม่ต้องมีผู้เชี่ยวชาญ

## โครงการวิจัยเชิงประจักษ์

**Lifelog Canvas Project:**
โครงการ big data ที่เชื่อมโยงดวงชะตา Bazi กับเหตุการณ์ชีวิตจริงโดยใช้ AI + data science เป้าหมาย: ทดสอบความแม่นยำของ Bazi เชิงประจักษ์ในกลุ่มตัวอย่างขนาดใหญ่ → ดูเพิ่มเติมที่ [[Bazi Health Prognosis × Five Elements × TCM]]

**Korean TCI-RS Study:**
ใช้ Temperament and Character Inventory-Revised Short พบ correlation ระหว่าง Output/Hurt Officer Star กับ Novelty Seeking behavior แบบมีนัยสำคัญทางสถิติ [อ้างอิงจาก NLM; ต้องการการยืนยัน]

**Sidereal Bazi Revival (Austin Bright) [single-source — unverified]:**
Austin Bright โต้แย้งว่า Bazi ดั้งเดิมต้องติดตาม Jupiter จริงใน 28 Mansions ไม่ใช่ปฏิทินสัญลักษณ์ — สร้าง Sidereal Bazi ที่แตกต่างจาก Tropical Bazi ที่ใช้กันทั่วไป [single-source — Austin Bright เท่านั้น; ไม่มีฉันทามติในแหล่งอื่น]

## งานที่ยากที่สุดสำหรับ AI ใน Bazi

**3 งานที่ LLMs ยังทำได้ไม่ดี (ตามแหล่ง NLM):**
1. **Yong Shen Identification** — การหา Useful God ต้องชั่งน้ำหนักระหว่าง Strength (Strong/Weak framework) กับ Tiao Hou (Climate Adjustment) — AI ไม่ทราบว่าจะใช้กรอบใดในบริบทนั้น
2. **LP Timing** — การผสาน 6 pillars × 12 characters ข้ามเวลา (natal + LP + annual) — complexity แบบ combinatorial ที่ LLMs ยังไม่ผ่าน
3. **Retroactive Hour Correction / Ding Pan** — การแก้ไขเวลาเกิดย้อนหลังจากเหตุการณ์จริงในชีวิต ต้องอาศัย interview + qualitative analysis ที่ไม่สามารถ encode เป็น rules ได้

## กฎ Di Tian Sui 4-test

ตำรา Di Tian Sui (滴天髓) กำหนด 4 ระดับการทดสอบดวงชะตา: **Season (ฤดูกาล) / Root (รากฐาน) / Purity (ความบริสุทธิ์) / Role (บทบาท)**

AI มักผ่าน Season และ Root ได้ดี แต่ล้มเหลวใน **Purity vs. Mixture conditional logic** — ความแตกต่างระหว่างดวงบริสุทธิ์ (pure pattern) กับดวงที่ผสมปนเปต้องการ gestalt judgment ที่ rule-based systems ไม่สามารถ capture ได้

## ปัญหา Clash + Combination Complexity

เมื่อ Earthly Branch ชน (Clash) และรวม (Combination) เกิดขึ้นพร้อมกัน: การรวมอาจแก้ไขการชน แต่อาจสร้าง Punishment ใหม่ — **AI ล้มเหลวกับ chained interactions** เหล่านี้เพราะต้องประเมินลำดับและน้ำหนักของ interaction ที่ขึ้นอยู่กับบริบทรวม

## บริบทตลาด

- ตลาด AI metaphysics จีน ¥12B+ (2024) เติบโต 43.7% ต่อปี
- "DeepSeek fortune-telling" มีโพสต์ WeChat 2M+ ในเดือนเดียว (2025)
- AI Bazi reading apps ที่ผู้ใช้ treat as authoritative — แต่ยังไม่มีการตรวจสอบความแม่นยำกับผลลัพธ์จริง

## ข้อจำกัดที่พบ

- **Symbol Grounding Problem** — AI จัดการสัญลักษณ์ Bazi ได้ทางไวยากรณ์แต่ขาด temporal/contextual grounding
- **ข้อจำกัดการคำนวณ** — LLM ส่วนใหญ่ยังสร้างดวงชะตา Bazi จากวันเกิดได้ไม่ถูกต้องโดยไม่มี tool assistance

## ข้อถกเถียงหลัก ⚠️

Benchmark ใช้ "คำตอบผู้เชี่ยวชาญ" เป็น ground truth แต่ถ้า [[สำนักและวิธีตีความ Bazi]] คลาสสิกกับสมัยใหม่ให้คำตอบที่ขัดแย้งกันสำหรับดวงเดียวกัน — ground truth ของ benchmark เองก็ถูกตั้งคำถาม ผู้ปฏิบัติมองว่า AI เป็นเครื่องมือช่วยคำนวณแต่ไม่สามารถแทนการอ่านแบบ holistic ของ practitioner ได้

## Related Concepts

- [[Bazi (八字)]] — ระบบแม่
- [[Bazi Health Prognosis × Five Elements × TCM]] — Health-LLM Agent เป็นสะพานระหว่าง AI benchmarking และ health prognosis
- [[สำนักและวิธีตีความ Bazi]] — ความขัดแย้งระหว่างสำนักสร้างปัญหา ground truth สำหรับ AI benchmarks
- [[Si Hua / Flying Star School (四化飛星)]] — Si Hua มีความเป็นมิตรต่อ AI สูงสุดเนื่องจากตาราง deterministic
- [[สิบเทพ (十神)]] — Ten Gods เป็น symbolic chain ที่ LLM ต้องเดินผ่าน
- [[วงจรดวงชะตา (大運)]] — Temporal integration ของ LP × Annual Luck คือ hardest subtask ใน BaziQA
