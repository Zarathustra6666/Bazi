---
name: ticketbook
description: |
  Speed-optimized ticket booking assistant สำหรับกดบัตร concert/event ออนไลน์ให้ได้เร็วที่สุด
  รองรับ allticket.com และ platform อื่นๆ
  ช่วย user เตรียมตัว → countdown → กดบัตรแบบ step-by-step real-time

  ใช้ skill นี้ทุกครั้งที่ user พูดว่า:
  - "ticketbook", "กดบัตร", "จองบัตร", "ซื้อบัตร"
  - "ช่วยกดบัตร", "เตรียมกดบัตร", "countdown บัตร"
  - "allticket", "ALL TICKET", "Thai Ticket Major"
  - ชื่อ event + "บัตร" เช่น "NCT บัตร", "BLACKPINK บัตร"
  - "fanmeeting บัตร", "concert บัตร", "บัตรคอนเสิร์ต"
---

# TicketBook — Speed Ticket Booking Skill

## วัตถุประสงค์

ช่วย user กดบัตร concert/fanmeeting/event ออนไลน์ให้ได้เร็วที่สุดในเวลาที่เปิดขาย
โดยมี 3 phase: **PREP** (เตรียมตัว) → **COUNTDOWN** (นับถอยหลัง) → **EXECUTE** (กดบัตร)

---

## FLOW หลัก

### เมื่อ user invoke skill นี้

**Step 1 — รับข้อมูล event**

ถามข้อมูลต่อไปนี้จาก user (ถามรวดเดียวทีเดียว ไม่ถามทีละข้อ):

```
ขอข้อมูลสำหรับเตรียมกดบัตร:
1. เว็บไซต์ขายบัตร (เช่น allticket.com, thaiticketmajor.com)
2. วัน/เวลา เปิดขายบัตร (เช่น 5 มิ.ย. 2569 เวลา 19:00 น.)
3. ชื่อ event / concert
4. โซนที่ต้องการ (เรียงลำดับ priority 1, 2, 3)
5. มี Membership number ต้องใส่ไหม? ถ้ามีให้เตรียมไว้
6. วิธีชำระเงินที่ต้องการ (7-11 / บัตรเครดิต)
```

**Step 2 — สร้าง PREP CHECKLIST**

หลังได้ข้อมูลครบ ให้สร้าง checklist เฉพาะ event นั้น พร้อม timing ที่ชัดเจน:

---

## PREP PHASE (T-15 ถึง T-1 นาที)

### T-15 นาที (ก่อนเปิดขาย 15 นาที)
- [ ] เปิดคอมพิวเตอร์ (แนะนำ PC/laptop ไม่ใช่มือถือ — ใช้ F5 ได้)
- [ ] เชื่อมต่อ internet ที่เร็วที่สุดที่มี (สาย LAN ดีกว่า WiFi)
- [ ] ปิด program ที่ไม่จำเป็น ทั้งหมด เพื่อให้ browser ทำงานเร็ว
- [ ] เปิด browser ที่เร็วที่สุด (Chrome แนะนำ)
- [ ] เปิด tab ใหม่ ไปที่เว็บขายบัตร และ **LOG IN ให้เรียบร้อย**
- [ ] คัดลอก Membership number ไว้ใน clipboard (Ctrl+C) หรือเปิด notepad ไว้
- [ ] ซิงค์นาฬิกาคอม: เปิด time.is หรือ google.com/search?q=time เพื่อเช็ควินาที
- [ ] ปิด notification ทั้งหมด (Windows: Focus Assist ON)

### T-5 นาที (ก่อนเปิดขาย 5 นาที)
- [ ] ไปที่หน้า event page บนเว็บขายบัตร
- [ ] เตรียมนิ้วไว้ที่ปุ่ม F5
- [ ] เปิด tab ที่ 2 ไว้สำรอง (หน้าเดิม)
- [ ] ไม่ต้อง Refresh ก่อนถึงเวลา — รอ!

### T-1 นาที (1 นาทีก่อนเปิดขาย)
- [ ] จ้องหน้าจอ
- [ ] มือซ้ายพร้อมที่ F5
- [ ] มือขวาพร้อมที่ mouse
- [ ] Membership number พร้อม paste

---

## EXECUTE PHASE (เวลา T ถึง T+5 นาที)

### ⚡ T+00:00 — กด F5 ทันที!
```
กด F5 ที่ T-3 วินาที (เช่น ถ้าเปิด 19:00:00 ให้กดที่ 18:59:57)
เพราะ request ใช้เวลาเดินทาง network ~1-3 วินาที
```
→ รอปุ่ม **"Buy Now"** ปรากฏ → คลิกทันที!

### ⚡ Step A — Accept Cookies (ถ้ามี)
```
Cookies popup → คลิก Accept/ยืนยัน → Tab 1 ครั้ง → Tick → Confirm
ทำให้เร็วที่สุด ไม่ต้องอ่าน
```

### ⚡ Step B — ใส่ Membership Number
```
Paste ทันที (Ctrl+V) — ห้ามพิมพ์เอง!
กด Buy Now / Confirm
```

### ⚡ Step C — เลือกโซน
```
เลือกโซน Priority 1 ก่อน
ถ้าเต็ม → Priority 2 → Priority 3
ห้ามลังเล เกิน 5 วินาที/โซน
```

### ⚡ Step D — เลือกที่นั่ง
```
เลือกที่นั่งแรกที่เห็นว่าว่าง — ไม่ต้องเลือกที่ดีที่สุด
ได้บัตรก่อนดีกว่าเลือกที่นาน
```

### ⚡ Step E — รอคิว (ห้าม Refresh!)
```
🚨 ห้าม Refresh!
🚨 ห้ามปิดหน้าต่าง!
🚨 ห้ามเปิด tab อื่น!
นั่งรอเฉยๆ จนระบบประมวลผลเสร็จ
```

### ⚡ Step F — Reserve Summary
```
ถ้าขึ้น RESERVE SUMMARY = สำเร็จ! ✅
1. อย่า tick ประกันภัย (ปล่อยว่าง)
2. เลือก Payment: 7-Eleven (เร็วสุด ไม่ต้องกรอกบัตร)
3. Tick ยอมรับเงื่อนไข
4. กด Payment (ปุ่มสีน้ำเงิน)
5. SCREENSHOT หน้า barcode ทันที!
6. ดูใน Purchase History เพื่อสำรองไว้
```

---

## FAIL & RETRY FLOW

```
ถ้าขึ้น Error หรือ Sold Out:
1. กด "Back to Home" หรือไปหน้าหลัก
2. อย่า panic — รีสตาร์ท Execute Phase ใหม่
3. กลับ Step A ทันที
4. บางโซนอาจมีคนยกเลิก → refresh ได้บัตร
```

**ห้ามทำ:**
- ❌ ปิด browser แล้วเปิดใหม่ (เสียเวลา)
- ❌ เปลี่ยน device กลางคัน
- ❌ กด Back ของ browser ระหว่างรอคิว

---

## PLATFORM-SPECIFIC NOTES

### allticket.com
- Login ล่วงหน้า 10-15 นาที
- หน้า event อยู่ที่ allticket.com → Concert & Entertainment
- Membership field: Paste ตรง input box "NCTzen Membership"
- Payment แนะนำ: 7-Eleven Counter Service
- ดูผลใน: allticket.com → Purchase History

### thaiticketmajor.com
- ต้อง login ผ่าน account
- Queue system อาจใช้เวลานาน — รอได้เลย
- Payment: บัตรเครดิต/เดบิต หรือ PromptPay

---

## QUICK REFERENCE CARD

พิมพ์ออกมาแปะข้างจอ:

```
┌─────────────────────────────────────┐
│  TICKET BOOKING QUICK GUIDE         │
├─────────────────────────────────────┤
│ T-15m  Login + เตรียม Membership    │
│ T-5m   เปิดหน้า event              │
│ T-0:03 กด F5!                      │
│ ──────────────────────────────────  │
│ Buy Now → Cookies → Membership     │
│ → โซน → ที่นั่ง → รอคิว           │
│ ──────────────────────────────────  │
│ ❌ ห้าม Refresh ระหว่างรอคิว       │
│ ✅ Screenshot barcode ทันที        │
│ ✅ จ่ายที่ 7-11 ก่อนหมดเวลา       │
└─────────────────────────────────────┘
```

---

## OUTPUT FORMAT

หลังรับข้อมูล event จาก user แล้ว ให้ output:

1. **PREP TIMELINE** — ตารางเวลาเตรียมตัวแบบ absolute time (เช่น 18:45, 18:55, 18:59:57)
2. **EXECUTE CHECKLIST** — steps กดบัตรแบบ numbered, กระชับ
3. **MEMBERSHIP REMINDER** — เตือนให้ copy membership number ไว้ล่วงหน้า
4. **ZONE PRIORITY** — แสดง priority โซนที่ user เลือกไว้

ถ้า user บอกว่า "เริ่มเลย" หรือ "countdown" → เริ่ม countdown แบบ real-time และ remind แต่ละ step ตามเวลาจริง

---

## ตัวอย่าง Invocation

```
User: "ticketbook NCT JnJm Duality, allticket, 5 มิ.ย. 19:00, NCTzen1 ก่อน, มี membership"
```

→ Codex ออก PREP TIMELINE + EXECUTE CHECKLIST ทันที พร้อมถามว่าต้องการให้ช่วย countdown real-time ไหม
