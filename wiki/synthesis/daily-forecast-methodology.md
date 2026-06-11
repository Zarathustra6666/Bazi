---
title: "Daily Forecast Methodology — สูตรคะแนนคุณภาพวัน (流日 Scoring)"
type: synthesis
tags: [bazi, daily, scoring, methodology, useful-god, clash, harmony]
created: 2026-06-11
updated: 2026-06-11
sources: 0
---

# Daily Forecast Methodology — สูตรคะแนนคุณภาพวัน (流日 Scoring)

> สูตรคะแนนวันที่ใช้ในแอป Bazi — สังเคราะห์จากหลักการ annual scoring ที่พิสูจน์แล้ว ลดน้ำหนักตาม [[daily-pillar|流日]] hierarchy

## สูตรคะแนน

สูตรนี้ adapted จาก `scoreAnnualYear()` ใน Bazi app โดยใช้ Day Stem/Branch แทน Year Stem/Branch:

```
score_base = 0

ถ้า Day Stem element == Useful God element     → +2
ถ้า Day Branch element == Useful God element   → +2
ถ้า Day Stem generates Useful God element     → +1
ถ้า Day Branch generates Useful God element   → +1
ถ้า Day Stem controls DM element              → -1
ถ้า Day Branch controls DM element            → -1
ถ้า Day Stem controls Useful God              → -1
ถ้า Day Branch controls Useful God            → -1

ถ้า Day Branch 六冲 กับ natal Day Branch       → -2  (สำคัญสุด)
ถ้า Day Branch 六冲 กับ natal เสาอื่น          → -1 ต่อเสา
ถ้า Day Branch 六合 กับ natal เสาใดเสาหนึ่ง    → +1

ถ้า LP ปัจจุบัน element ตรงกับ Useful God      → LP Bonus (ปลดล็อคดาวคู่เมื่อ stars ≥ 3)

stars = max(1, min(4, score_base + 2))
```

**Range:** คะแนนก่อน clamp อยู่ที่ประมาณ -3 ถึง +6 → clamp เป็น 1–4 ดาว

## ป้ายคุณภาพ

| ดาว | ป้าย | ความหมาย |
|-----|------|----------|
| 1 | ⚠ ระวัง | วันที่พลังงานขัดต่อ nature ดวง หรือมี clash สำคัญ |
| 2 | ★ ปกติ | วันกลางๆ — ทำงานปกติได้ แต่ไม่ใช่จังหวะเดิน |
| 3 | ★★ ดี | วันที่ธาตุเอื้อ — เหมาะเจรจา เริ่มต้น ลงมือ |
| 4 | ★★★ ดีมาก | วันที่ทั้ง LP และ Day ตรงกับ Useful God — "วันทอง" หายาก |

## การแจกแจงคะแนนที่คาดหวัง

ในเดือนปกติ (30 วัน):
- ★★★ ดีมาก: ~3–5 วัน (ต้องมี LP bonus ด้วย)
- ★★ ดี: ~8–12 วัน
- ★ ปกติ: ~10–14 วัน
- ⚠ ระวัง: ~3–7 วัน (วัน clash มักได้ 1–2 ดาว)

> ถ้า LP ปัจจุบันไม่ตรงกับ Useful God → ★★★ จะหายากมาก เพราะ LP bonus ไม่ทำงาน

## กฎเชิงปฏิบัติ (Decision Rules)

**วันที่ควรเลื่อนการตัดสินใจใหญ่:**
- Day Branch 六冲 กับ natal Day Branch (ตัวตนไม่มั่นคง)
- Stars = 1 (⚠) ร่วมกับ Day Stem ควบคุม Useful God

**วันที่เหมาะลงมือ:**
- Day Stem/Branch ตรงกับ Useful God (stars ≥ 3)
- ไม่มี clash กับเสาสำคัญ (Day/Month branch)

**วันทองที่หายาก (★★★ + ✦):**
- LP เสริม UG + Day ตรงกับ UG + ไม่มี clash = "Double Luck Day"
- ใน LP ที่ไม่เอื้อ วันแบบนี้แทบไม่เกิด

## สูตรคะแนน 流月 (Monthly Scoring)

สูตรนี้ใช้ Month Stem/Branch แทน Day Stem/Branch — weights เหมือน 流日 ทุกประการ น้ำหนักในลำดับชั้น: **LP >> 流年 >> 流月 >> 流日**

```
score_base = 0

ถ้า Month Stem element == Useful God element     → +2
ถ้า Month Branch element == Useful God element   → +2
ถ้า Month Stem generates Useful God element     → +1
ถ้า Month Branch generates Useful God element   → +1
ถ้า Month Stem controls DM element              → -1
ถ้า Month Branch controls DM element            → -1
ถ้า Month Stem controls Useful God              → -1
ถ้า Month Branch controls Useful God            → -1

ถ้า Month Branch 六冲 กับ natal Day Branch       → -2  (สำคัญสุด)
ถ้า Month Branch 六冲 กับ natal เสาอื่น          → -1 ต่อเสา
ถ้า Month Branch 六合 กับ natal เสาใดเสาหนึ่ง    → +1

ถ้า LP ปัจจุบัน element ตรงกับ Useful God      → LP Bonus (ปลดล็อคดาวคู่เมื่อ stars ≥ 3)

stars = max(1, min(4, score_base + 2))
```

ความแตกต่างจาก 流日: น้ำหนักในลำดับชั้นสูงกว่า — เดือนดีใน LP ที่ไม่ดีมีผลจำกัด แต่เดือนดีใน LP ที่ดีขยายผลได้มาก

## ข้อจำกัดของโมเดล

1. **น้ำหนักเบา (流日):** 流日 คือชั้นเวลาที่เบาที่สุด — แม้วัน ★★★ แต่ถ้า LP และ Annual ไม่ดี ผลก็จำกัด
2. **Shen Sha ไม่รวม:** ดาวพิเศษ (神煞) บางดวงมีผลต่อวัน (เช่น 天德, 月德) แต่ยังไม่ได้รวมในสูตรนี้
3. **ไม่รองรับ Classical Late-Zi:** สูตรใช้ midnight เป็นขอบวัน ไม่ใช่ 23:00 ของสำนัก Late-Zi
4. **Solar term approximation (流月):** เดือนแสดงตามปักษ์สุริยะโดยประมาณ (เช่น 寅月 ≈ ก.พ.-มี.ค.) ไม่ใช่ขอบ solar term แม่นยำ

## Related

- [[daily-pillar]] — หลักการ 流日 และน้ำหนักในลำดับชั้น
- [[luck-pillar-arc|LP 10-Year Arc]] — น้ำหนัก LP > Annual ที่ทำให้ LP Bonus สำคัญ
- [[เทพใช้งาน (用神)]] — Useful God คือเกณฑ์หลักของสูตรทั้งหมด
- [[วงจรดวงชะตา (大運)]] — LP ปัจจุบันกำหนด LP Bonus
