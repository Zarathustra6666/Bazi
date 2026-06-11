---
title: เวลาสุริยะจริง (True Solar Time)
type: concept
tags: [bazi, calculation, time, timezone, longitude, thailand, application]
aliases: [true-solar-time, solar-time-correction, เวลาสุริยะ, RST]
created: 2026-05-30
updated: 2026-05-30
sources: 0
status: complete
---

# เวลาสุริยะจริง (True Solar Time)

> เวลาสุริยะจริงคือเวลาที่ดวงอาทิตย์อยู่ตรงเส้นเมอริเดียน ณ ตำแหน่งเกิดจริง — ซึ่งต่างจากนาฬิกามาตรฐาน และเป็นฐานที่ถูกต้องสำหรับคำนวณเสาชั่วโมง (時柱) ใน [[Bazi (八字)]]

## What it is

ตำราโบราณทุกเล่มถูกเขียนก่อนมีโซนเวลามาตรฐาน — นักพยากรณ์บอกเวลาด้วยตำแหน่งดวงอาทิตย์จริงๆ ณ ที่เกิด ดังนั้น [[สี่เสา (Four Pillars)|เสาชั่วโมง (時柱)]] ที่ถูกต้องต้องใช้ **True Solar Time (เวลาสุริยะจริง)** ไม่ใช่เวลานาฬิกามาตรฐาน

เวลาสุริยะจริงต่างจากนาฬิกาเพราะสองสาเหตุ:
1. **ตำแหน่งลองจิจูด** — โซนเวลาบังคับให้ทุกคนในพื้นที่กว้างใช้เวลาเดียวกัน แต่ดวงอาทิตย์ขึ้นต่างเวลาจริงตามตำแหน่งตะวันออก-ตะวันตก
2. **วงโคจรโลกไม่เป็นวงกลมสมบูรณ์** — ทำให้เวลาสุริยะ drift ได้ถึง ±16 นาที ตลอดปี

## Why it matters

[[สี่เสา (Four Pillars)|เสาชั่วโมง (時柱)]] เปลี่ยนทุก **2 ชั่วโมง (120 นาที)** — ถ้าเวลานาฬิกาต่างจากเวลาสุริยะจริงเพียง 10–28 นาที และเวลาเกิดอยู่ใกล้ขอบชั่วโมง เสาเวลาจะ **เปลี่ยนทั้งเสา** กระทบ [[สิบเทพ (十神)]] และ [[โครงสร้างดวงชะตา (格局)]] ทั้งหมด

ตัวอย่าง — กรุงเทพฯ:
- นาฬิกาบอก **07:05 น.** → อยู่ใน 辰 (มะโรง) 07:00–09:00
- หักลบ 18 นาที → เวลาสุริยะจริง **06:47 น.**
- 06:47 อยู่ใน 卯 (เถาะ) 05:00–07:00
- **เสาเวลาเปลี่ยนไปทั้งเสา**

## Key aspects

### สูตรคำนวณ (3 ขั้นตอน)

**ขั้นที่ 1 — Longitude Correction**

```
standard_meridian      = timezone_offset × 15
longitude_correction   = (birth_longitude − standard_meridian) × 4  [นาที]
```

- ค่า **บวก** = อยู่ทางตะวันออกของเมอริเดียน → เวลาสุริยะเร็วกว่านาฬิกา
- ค่า **ลบ** = อยู่ทางตะวันตกของเมอริเดียน → เวลาสุริยะช้ากว่านาฬิกา

**ขั้นที่ 2 — Equation of Time (EoT)**

สูตร Spencer (1971):
```
B   = 2π × (day_of_year − 1) / 365
EoT = 229.18 × (0.000075 + 0.001868·cos B − 0.032077·sin B
                           − 0.014615·cos 2B − 0.04089·sin 2B)  [นาที]
```

ค่าโดยประมาณรายเดือน:

| เดือน | EoT (นาที) | เดือน | EoT (นาที) |
|-------|-----------|-------|-----------|
| ม.ค. | −3 ถึง −9 | ก.ค. | −4 ถึง −6 |
| ก.พ. | −13 ถึง −14 | ส.ค. | −6 ถึง 0 |
| มี.ค. | −13 ถึง −4 | ก.ย. | 0 ถึง +5 |
| เม.ย. | −4 ถึง +3 | ต.ค. | +10 ถึง +16 |
| พ.ค. | +3 ถึง +4 | พ.ย. | +16 ถึง +11 |
| มิ.ย. | +4 ถึง 0 | ธ.ค. | +11 ถึง +4 |

**ขั้นที่ 3 — รวมผล**

```
true_solar_time = birth_time + longitude_correction + EoT
```

### ตัวเลขสำหรับประเทศไทย (UTC+7, standard meridian = 105°E)

ไทยทั้งประเทศอยู่ทางตะวันตกของ 105°E — เวลาสุริยะช้ากว่านาฬิกาเสมอ

| เมือง | ลองจิจูด | Longitude Correction | หมายเหตุ |
|-------|----------|---------------------|----------|
| แม่ฮ่องสอน | 97.97°E | −28.1 นาที | ช้าที่สุดในไทย |
| เชียงใหม่ | 98.98°E | −24.1 นาที | |
| เชียงราย | 99.83°E | −20.7 นาที | |
| กรุงเทพฯ | 100.50°E | −18.0 นาที | ศูนย์กลาง |
| นครราชสีมา | 102.10°E | −11.6 นาที | |
| ขอนแก่น | 102.83°E | −8.7 นาที | |
| อุบลราชธานี | 104.87°E | −0.5 นาที | ใกล้ meridian มากที่สุด |

**ช่วงความแตกต่างภายในไทย: ~28 นาที** (แม่ฮ่องสอน vs อุบล)

### กรณีพิเศษ — ประวัติเวลาประเทศไทย

```python
if "1941-12-08" <= birth_date <= "1945-09-15":
    timezone_offset = +9   # ไทยใช้เวลาญี่ปุ่นช่วงสงครามโลกครั้งที่ 2
else:
    timezone_offset = +7   # ปกติ — ไทยไม่มี Daylight Saving Time
```

### ความแม่นยำแต่ละวิธี

| วิธี | ความคลาดเคลื่อน |
|------|----------------|
| ใช้นาฬิกาล้วน (ไม่ปรับ) | 0–28+ นาที |
| ปรับ Longitude อย่างเดียว | 0–16 นาที |
| ปรับทั้ง Longitude + EoT | < 30 วินาที |

## Connections

- [[สี่เสา (Four Pillars)]] — เสาชั่วโมง (時柱) คือเสาที่ได้รับผลกระทบโดยตรง
- [[สำนักและวิธีตีความ Bazi]] — สำนักต่างกันในการใช้/ไม่ใช้ True Solar Time
- [[วิธีการอ่านดวง Bazi แบบมีหลักการ|methodology]] — ขั้นตอน Chart Construction ต้องใช้ True Solar Time ก่อน

## Open questions

- ซินแสไทยรุ่นเก่าส่วนใหญ่ไม่ปรับเวลา — ผลต่อความแม่นยำมีนัยสำคัญหรือไม่ในทางปฏิบัติ?
- มี master จีนแผ่นดินใหญ่คนใดที่ทำ large-scale study เปรียบเทียบผลลัพธ์ระหว่าง standard time vs solar time?

## Application Spec (สำหรับนักพัฒนา)

```python
from math import cos, sin, pi, floor

def calc_true_solar_time(birth_date, birth_time_min, longitude):
    """
    birth_time_min: นาทีนับจากเที่ยงคืน เช่น 7:05 = 425
    longitude: องศาทศนิยม เช่น 100.5013
    คืนค่า: true_solar_time เป็นนาที
    """
    tz = get_historical_timezone(birth_date)  # +7 หรือ +9
    standard_meridian = tz * 15               # 105 หรือ 135
    lng_corr = (longitude - standard_meridian) * 4

    doy = day_of_year(birth_date)
    B = 2 * pi * (doy - 1) / 365
    eot = 229.18 * (0.000075
                    + 0.001868 * cos(B)
                    - 0.032077 * sin(B)
                    - 0.014615 * cos(2*B)
                    - 0.04089  * sin(2*B))

    result = (birth_time_min + lng_corr + eot) % 1440
    return result

def get_hour_pillar_index(true_time_min):
    """คืนค่า 0=子(ชวด) ถึง 11=亥(กุน)"""
    return floor((true_time_min + 60) / 120) % 12

HOUR_PILLARS = [
    ("子", "ชวด",  "23:00–01:00"),
    ("丑", "ฉลู",  "01:00–03:00"),
    ("寅", "ขาล",  "03:00–05:00"),
    ("卯", "เถาะ", "05:00–07:00"),
    ("辰", "มะโรง","07:00–09:00"),
    ("巳", "มะเส็ง","09:00–11:00"),
    ("午", "มะเมีย","11:00–13:00"),
    ("未", "มะแม", "13:00–15:00"),
    ("申", "วอก",  "15:00–17:00"),
    ("酉", "ระกา", "17:00–19:00"),
    ("戌", "จอ",   "19:00–21:00"),
    ("亥", "กุน",  "21:00–23:00"),
]

def get_historical_timezone(birth_date):
    if "1941-12-08" <= birth_date <= "1945-09-15":
        return 9
    return 7
```

**Input ที่ควรรองรับ:**
```
birth_date      : YYYY-MM-DD
birth_time      : HH:MM
birth_longitude : float (หรือ birth_city → lookup)
auto_detect     : bool (GPS บน mobile)
warn_if_pillar_changes : bool
```

## Source notes

ข้อมูลรวบรวมจาก web research session 2026-05-30:
- [True Solar Time Calculator — bazi-lab.com](https://www.bazi-lab.com/true-solar-time)
- [What is Real Solar Time? — bazi-calculator.com (PDF)](https://bazi-calculator.com/instr/RST.pdf)
- [Adjusting for Timezones — bazi-web.com](https://bazi-web.com/adjusting-for-time-zones-and-longitude-in-bazi/)
- [Why We Adjust Birth Time — adestiny.com](https://adestiny.com/articles/why-we-adjust-your-birth-time-accurate-bazi-charts/)
- [True Solar Time — freeastroapi.com](https://www.freeastroapi.com/guide/true-solar-time)
- [BaZi Local Solar Time — astrology-api.io](https://astrology-api.io/blog/bazi-local-solar-time)
