# Operation Log

## [2026-06-11] update | 流月 Monthly Pillar — app tab + wiki scoring section

- **App:** เพิ่ม tab `流月 / เดือน` ระหว่าง 大運/流年 และ 流日/วันนี้ ใน `deploy/index.html`
- **App:** เพิ่ม `calcMonthlyForecast()`, `scoreMonthlyLuck()`, `renderMonthlyForecast()` — 3×4 grid แสดง 12 เดือนสุริยะ, year nav ← →, click month → detail, clash/harmony tags, narrative
- **Wiki:** `wiki/synthesis/daily-forecast-methodology.md` — เพิ่ม section สูตรคะแนน 流月 (weights เหมือน 流日, น้ำหนัก LP >> 流年 >> 流月 >> 流日)
- **Wiki:** `wiki/concepts/luck-pillars.md` — เพิ่ม subsection "เดือนสำคัญ (流月)" พร้อม link ไป daily-forecast-methodology

## [2026-06-11] lint | Full Vault Lint Pass — 1 broken link fixed

- Fixed broken WikiLink `[[zi-ping]]` → `[[bazi|Zi Ping]]` in `sources/arxiv-bazi-llm.md` (×2 occurrences)
- Standardized frontmatter: `type: text` → `type: source` in all 5 `wiki/texts/` pages (di-tian-sui, qiong-tong-bao-jian, san-ming-tong-hui, yuan-hai-zi-ping, zi-ping-zhen-quan)
- Confirmed `wiki/queries/` directory intentionally empty (no orphan query pages)
- No other broken links, orphans, or stubs detected across 50 pages

## [2026-06-11] update | 流日 Daily Pillar — wiki pages + app Phase 2 prep

- **หน้าใหม่:** `wiki/concepts/daily-pillar.md` — 流日 concept: 60-cycle jiazi, Ten God ธีมวัน, Clash/Harmony domain effects, น้ำหนักในลำดับชั้น LP >> 流年 >> 流月 >> 流日, กฎ 择日
- **หน้าใหม่:** `wiki/synthesis/daily-forecast-methodology.md` — สูตรคะแนน 1–4 ดาว: UG alignment (±2/±1), 六冲 (−2/−1), 六合 (+1), LP bonus; กฎเชิงปฏิบัติ; ข้อจำกัดโมเดล
- **อัพเดท:** `wiki/concepts/luck-pillars.md` — เพิ่ม subsection "วันสำคัญ (流日)" พร้อม links ไปยัง daily-pillar และ daily-forecast-methodology
- **Research:** WebSearch 3 queries (treybazi.blogspot.com + general 流日 methodology) — ไม่พบ dedicated article; เนื้อหาสังเคราะห์จาก wiki ที่มีอยู่
- **อัพเดท:** index.md (Pages 49→51, เพิ่ม Synthesis section), log.md

## [2026-06-10] lint | Lint Pass — WikiLink fixes, index catch-up, overview update

- **Broken WikiLinks fixed:** 15 links ใน 3 concept pages (day-master-strength, tiao-hou, yin-yang) — เปลี่ยนจาก English-format links เป็น Thai/mixed format ที่ตรงกับ page titles/aliases ที่มีอยู่
- **Aliases เพิ่ม:** `david-yek.md` → aliases: [David Yek (Quan Yuan), Quan Yuan]; `sean-chan.md` → aliases: [Sean Chan (Master Mystic), Master Mystic]; แก้ link ผิด `[[วงจรดวงชะตา (大運)|Qi Men Dun Jia]]` → plain text
- **Index อัพเดท:** เพิ่ม 3 concept pages ที่ยังไม่ถูก index: Yin-Yang (陰陽), Day Master Strength, Tiao Hou (調候); Pages 46 → 49
- **Overview อัพเดท:** sources 7→10, pages 31→49; เพิ่ม Contemporary Masters theme; เพิ่ม recent updates 2026-06-09 + 2026-06-04
- **ลบ 5 orphan entity pages:** di-tian-sui, zi-ping-zhen-quan, qiong-tong-bao-jian, san-ming-tong-hui, yuan-hai-zi-ping ใน entities/ — duplicate ของ wiki/texts/ ที่สมบูรณ์กว่า, sources: [], ไม่มี inbound links

## [2026-06-09] update | entity — 3 Contemporary Masters (Joey Yap, David Yek, Sean Chan)

- **สร้าง 3 entity pages:** `joey-yap.md`, `david-yek.md`, `sean-chan.md`
- **แหล่งข้อมูล:** NLM notebook e1f30f92 (40 sources) — 2 queries ครอบคลุม methodologies, สายวิชา, จุดขัดแย้ง, Bird Profiles system
- **Joey Yap:** MsAocm founder; Commercial Modern school; DOPE profiling + Cai Guan Yin; ถูกวิจารณ์ว่า bastardize ศาสตร์ดั้งเดิม
- **David Yek:** Quan Yuan; Bird Profiles 10 นก; Anti-literal DTS; Month Commander quality > DM Strength score; Qi Flow paradigm
- **Sean Chan:** Rational Spirituality manifesto; The Bazi App; anti-trinket; AI-translated ZPZQ/DTS; "chart is a map not a prison"
- **อัพเดท:** `index.md` — เพิ่ม Contemporary Masters section; Pages 43 → 46

## [2026-06-04] update | source — treybazi-blog.md expanded (35 articles, 4 new Raw Notes sections)

- **ขยาย:** `wiki/sources/treybazi-blog.md` — เพิ่มจาก 17 → 35 บทความในตาราง Key Articles; เพิ่ม Raw Notes 4 ส่วนใหม่: (O) YueLing historical background จาก Book of Rites ~200 BC; (P) Useful God 6 subcategories (顺用/逆用/清浊/救应/忌神/相神); (Q) Classical vs Contemporary, WuXing vs ZiPing distinction; (R) 格局派 Structural Sect overview + 5-text canon (ZPZQ/SFTK/SMTH/XPHH/YHZP)
- **Research:** WebSearch 6 queries (treybazi.blogspot.com domain-filtered); new articles found: Classical BaZi structural sect, 定格局诀, Month command (2014/01), Names of Ten Gods, Useful God overview, Is my DM strong or weak?, SMTH Follow Wealth, SMTH DM sitting on Wealth, DTS wealthy chapter, chart structure list, Zi hour controversy, SYDB Part 6, HS/EB intro, 12 Qi stages, EB 6 combinations
- **Key position added:** 13th Key Position — Useful God has 6 named subcategories (相神 Minister God clarified via Warren Buffett case)
- **Contradiction added:** SFTK/XPHH identity not confirmed from snippets; flagged [unsourced]
- **อัพเดท:** index.md (source summary updated), log.md

## [2026-06-04] update | source — treybazi-blog.md expanded (17 articles, full raw notes)

- **ขยาย:** `wiki/sources/treybazi-blog.md` — เพิ่มจาก 11 → 17 บทความ; เพิ่ม Raw Notes sections N ส่วน: Classical vs Modern (4 differences), DM Strength 4-factor self-critique, HS/EB passive/active distinction, Ten Gods benevolent/malevolent framework, Shun/Ni operational rules, JianLu/YueJie criteria + structure rankings, Follow Output 6 criteria, Clear/Murky (清浊) DTS spectrum, True/Fake (真假) DTS, Original ZiPing (情×力), SYDB Four Words poem, Warren Buffett case study (Indirect Seal), Transformation 10 days, GuiKang SMTH
- **Research:** WebSearch (site:treybazi.blogspot.com) + WebFetch 11 URLs: 2018/02 Classical-vs-Modern, 2018/02 poverty DTS, 2018/02 JianLu, 2013/02 DM Strength, 2013/04 HS-vs-EB, 2014/11 Ten Gods, 2018/01 Follow Output, 2018/01 Warren Buffett, 2015/03 Clear-Murky, 2015/03 True-Fake, 2015/03 Original-ZiPing
- **New contradictions flagged:** (1) Trey's own 2013→2018 shift on DM strength contradicts Modern approach; (2) JianLu collapse vs separation — intra-classical disagreement; (3) DTS poverty principles vs Qian Li Ming Gao — internal classical inconsistency
- **Vault links added:** follow-patterns, pattern-purity, master-reading-synthesis, day-master (DM strength debate), di-tian-sui (DTS verse translations)
- **อัพเดท:** log.md (this entry)

## [2026-06-04] ingest | source — Trey Bazi blog (treybazi.blogspot.com)

- **หน้าใหม่:** `wiki/sources/treybazi-blog.md` — English-language classical Bazi blog by self-taught practitioner "Trey" (2013–2018); ครอบคลุม 11 บทความหลัก
- **Research:** WebSearch 2 queries + WebFetch 6 URLs (About page, 10 Gods intro, 用神逆用, SYDB poem, 10 transform days, GuiKang, main page listing)
- **Key positions:** Month Command เป็น exclusive structure anchor; classical vs modern เป็น irreconcilable systems; shun-yong (顺用) vs ni-yong (逆用) เป็น central axis; GuiKang practical rarity <1%; transformation charts ใช้กฎแยกจาก standard structure
- **Classical texts cited:** ZPZQ (primary), YHZP (SYDB poem, transformation), SMTH (GuiKang), DTS (wealth/poverty, transformation)
- **Vault links:** useful-god, ten-gods, patterns, transformation-patterns, yuan-hai-zi-ping, zi-ping-zhen-quan, san-ming-tong-hui, methodology, schools, shen-sha
- **อัพเดท:** index.md (Sources 9→10, Pages 42→43), log.md

## [2026-06-04] ingest | source — arXiv papers: BaZi as LLM Benchmark (2510.23337 + 2602.12889)

- **หน้าใหม่:** `wiki/sources/arxiv-bazi-llm.md` — source page รวม 2 academic papers: (1) BaZi-Based Character Simulation Benchmark (Zheng et al., 2025) + (2) BaziQA-Benchmark (Chen & Liu, 2026)
- **Research:** WebFetch arxiv.org/abs/2510.23337 + arxiv.org/html/2602.12889v1 + WebSearch ทั้งสอง paper; ได้ full methodology, dataset specs, accuracy tables
- **Key findings:** Paper 1 — Celebrity 50 dataset (488 QA), hybrid BaZi-LLM ดีกว่า vanilla 30–62%; Paper 2 — 200 MCQ จาก Global Fortune-teller Competition, frontier LLMs ได้ 32–37% (baseline 25%), temporal domains ยากที่สุด (23–40%)
- **Ontology confirmed:** ทั้งสอง paper ใช้ Ten Gods (十神) เป็น primary symbolic layer; Heavenly Stems/Earthly Branches เป็น input; 大运+流年 integration เป็น hardest reasoning task
- **อัพเดท:** index.md (Sources 7→9, Pages 41→42), log.md

## [2026-06-04] update | entity — สร้าง 2 master pages: Liang Xiangrun + Ni Haisha

- **หน้าใหม่:** `wiki/entities/liang-xiangrun.md` — 梁湘润 (1930–2013) ปรมาจารย์ห้าศาสตร์ไต้หวัน เน้นสำนัก Zi Ping กระแสหลัก ผลงาน 103+ เล่ม รวม 子平基礎概要, 子平命學精論, 神煞探源, 四角方陣刑沖合會透解, 余氏用神辭淵
- **หน้าใหม่:** `wiki/entities/ni-haisha.md` — 倪海厦 (1954–2012) แพทย์จีนและนักพยากรณ์ไต้หวัน-อเมริกัน ชุดบรรยาย 天纪: บาจีเป็น input → แปลงเป็น hexagram ผ่าน 皇極經世 + 鐵板神數, บูรณาการ TCM-Fate
- **Research:** WebSearch 4 queries (ชีวประวัติ, ผลงาน, methodology ทั้งสองท่าน)
- **อัพเดท:** index.md (+2 pages → 41 total), log.md

## [2026-06-03] ingest | bazisearch Cluster 2 — Annual × LP Interaction Matrix

- **Research:** NotebookLM 4d1f57c8 (3 queries + 10 new sources: deeporacle, skillon, baziadvisor, bazichic, fengshuixinyu, shen-shu, hifortune, humaninsightpath, zh.wikipedia ZPZQ)
- **อัพเดท:** `luck-pillar-arc.md` — เพิ่ม Section 7 "Annual × LP Interaction Matrix": (1) Annual Branch clash table → 4 pillar domain effects (Day/Month/Year/Hour), (2) Double-Favorable Golden Year criteria (Good/Golden/Peak 三 levels), (3) Pattern activation via 三合 + สัมพันธ์กับ Pattern Purity, (4) Annual Stem TG prediction table 8 TG
- **Fixed:** duplicate ## 6. heading → renumbered sections 7-11; updated: frontmatter updated→2026-06-03, sources 1→3; added source note for notebook queries
- **Commit:** 56 files Bazi initial commit (e3e5fe4) — สร้าง .gitignore + staged Bazi/ ไม่รวม .obsidian/.claude/.vscode

## [2026-06-03] update | app — B4 Shen Sha integration: Para 5.5 ⭐ ดาวพิเศษในดวง

- **App:** `deploy/index.html` — เพิ่ม Para 5.5 "⭐ ดาวพิเศษในดวง" ใน renderMasterReading: แสดง top 3 Shen Sha จาก natal chart + LP activation check (天乙/驿马/桃花/文昌/华盖/将星/羊刃); ถ้า LP กระตุ้นดาว → แสดง event prediction sentence; 羊刃 + LP SK + ไม่มี mitigator → warning แดง
- **Logic:** isSsActivated() — clash-based (驿马), match-based (桃花/文昌/华盖/将星), tyBi-array (天乙), ctrlEl-check (羊刃); LP timing vars ย้ายออกนอก Para 6 เพื่อ share กับ Para 5.5
- **อัพเดท:** skill.md — เพิ่มแถว Shen Sha notebook (4d1f57c8) ใน Notebook ID Table

## [2026-06-03] ingest | bazisearch — ยกระดับความสามารถทำนาย: Shen Sha Prediction + Year/Hour Pillar + LP Arc + Branch Harmony

- **Research:** NotebookLM 4d1f57c8 ใหม่ "Shen Sha Event Prediction" (10 sources), Methodology notebook a44aa145 (Year/Hour pillar 10 sources)
- **หน้าใหม่:** `wiki/concepts/shen-sha-prediction.md` — prediction matrix 8 stars × LP activation (天乙/驿马/桃花/文昌/天德/月德/羊刃/华盖) + activation formula + warning conditions
- **อัพเดท:** `ten-gods-pillar.md` — เพิ่ม Section 9 classical prediction sentences ทั้ง 10 TG สำหรับ Year Pillar (รากฐาน) และ Hour Pillar (ปลายทาง)
- **App:** `deploy/index.html` — เพิ่ม 4 features: (1) 🏛️ Para 0 รากฐาน (Year Pillar TG), (2) Para 5 six-harmony/three-harmony narratives (六合/三合), (3) LP Arc phase label + 三七开 note + 交运 transition warning, (4) 🌙 Para 8 ปลายทาง (Hour Pillar TG)
- **อัพเดท:** index.md (+1 หน้าใหม่, 39 pages total), overview.md, log.md, skill.md

## [2026-06-03] ingest | bazisearch — Element Narrative Templates + LP Activation Framework

- **Research channel:** NotebookLM 3add2c78 (3 queries, 6 sources added) + NotebookLM 0697cf4f ใหม่ (3 queries, 3 sources added) + WebSearch (5 queries)
- **หน้าใหม่:** `wiki/concepts/element-narrative-templates.md` — classical overflow phrases (木多无金/火多土焦/水多木漂/土多金埋/金多水浊), DM narrative prose (Jia/Ren-Gui/Xin), hook sentences, Tiao Hou decision tree, LP activation templates (generating/controlling/same/Tiao Hou repair)
- **อัพเดท:** `five-elements-interpretation.md` — เพิ่ม Section 9 LP × Element Activation Framework + case studies David/Marcus/Elena + link to element-narrative-templates
- **Notebook ใหม่:** 0697cf4f "LP × Element Activation — Bazi Deep Dive"
- **Sources ใหม่:** LadiesTalk Bazi Podcast, OpenFate Five Elements, DestinySeek Heavenly Stems, FatePath Fire Imbalance, BaZi Advisor Fui Gong/Fan Yin
- **อัพเดท:** index.md (+2 entries, total 38 pages), log.md

## [2026-06-02] ingest | bazisearch — 五行 Five Elements Deep Interpretation

- **Research channel:** NotebookLM e1f30f92 (3 queries) + a44aa145 (2 queries) + WebSearch (7 queries) + new notebook 3add2c78 (5 sources added)
- **สร้าง:** `wiki/concepts/five-elements-interpretation.md` — หน้าใหม่ 10 sections
- **เนื้อหาหลัก:** บุคลิก Yang/Yin ทุกธาตุ (甲乙丙丁戊己庚辛壬癸), ปฏิสัมพันธ์ 5 รูปแบบ (帮生泄克耗), วิธีประเมิน DM strength (得令/得地/得势), ความสัมพันธ์ DM กับผู้อื่น (Ten God lens), ธาตุขาด/ล้น/อ่อน, สุขภาพ TCM, อาชีพ
- **Case studies:** Wei Qianli (โลหะอ่อน/ไม้ล้น), Frozen Water chart, Mr. J (วิเคราะห์ DM strength ผิด), Yuan Shushan (หนีจากธาตุพิฆาต), Stephen Hawking (โลหะ 70%+ ไม้ขาด → ALS)
- **อัพเดท:** index.md (+1 page, total 36)
- **Notebook ใหม่:** 3add2c78 "五行 Five Elements — Bazi Deep Dive" (4 sources)

## [2026-06-02] update | App Integration — Master Interpretation Layer

- **TG_FULL[].pillar:** ขยายจาก 1-line label → 2 ประโยคต่อ pillar (10 TG × 4 pillars) — บอกความหมายชีวิตเฉพาะตำแหน่ง เช่น 食神 Month = "อาชีพใช้พรสวรรค์เป็นหลัก ทำงานที่รักโดยธรรมชาติ"
- **LP_ROAD_NARR:** เปลี่ยนจาก string → object `{narr, early, mid, late}` — แสดง arc ภายใน 10 ปี (3 ปีแรก/กลาง/ปลาย) ตาม yearsIn LP; แสดงใน LP detail panel (highlight bar สีน้ำเงิน) และใน Master Reading (↳ italic)
- **renderMasterReading — paragraph ใหม่ "🔗 โครงสร้างดวง (情 × 格局)":** Pattern Purity label + คำอธิบายความหมาย + 情 affection analysis ตรวจ 7 คู่ TG (官印相生, 食神制杀, 傷官生财, 杀印相生, 傷官见官, 财破印, 枭神夺食)
- **renderMasterReading — Para 5 clash:** เพิ่มชื่อ pillar คู่ที่ชน + life domain context เช่น "子午冲 (เสาปี↔เสาเดือน) — [รากฐาน/บรรพบุรุษ ปะทะ อาชีพ/สภาพแวดล้อมหลัก]"
- **renderMasterReading — Para 5 TG:** เพิ่ม pillar-specific narr ต่อ Ten God ที่สำคัญ "↳ ตำแหน่งนี้: ..."
- File: 2729 → 2793 lines

## [2026-06-02] ingest | bazisearch — Master Interpretation Layer (4 หน้าใหม่)

- **Research channel:** WebSearch 8 queries (4 clusters × 2 rounds) — NotebookLM ไม่พร้อมใช้งาน (auth expired)
- **Cluster A — Ten Gods × Pillar:** สร้าง `wiki/concepts/ten-gods-pillar.md` — ความหมาย 食神/伤官/七杀/正官/印星 ในแต่ละเสา; กฎ 4 ข้อระดับปรมาจารย์
- **Cluster B — LP 10-Year Arc:** สร้าง `wiki/concepts/luck-pillar-arc.md` — ทฤษฎี 三七开 (San Ming Tong Hui), จังหวะ Early/Mid/Late, Transition period 1-2 ปีทับซ้อน, LP × Useful God framework
- **Cluster C — Branch Interactions × Pillar Pairs:** สร้าง `wiki/concepts/branch-interaction-meaning.md` — matrix 5 คู่เสา × Clash/Harmony → ความหมายชีวิต (配偶宫, 子女宫); 三合=明合, 六合=暗合
- **Cluster D — Master Reading Synthesis:** สร้าง `wiki/concepts/master-reading-synthesis.md` — ZPZQ: 情×力 dual criteria, Pattern Purity (純格/有情格/雜格), กระบวนการ 5 ขั้น, ตัวอย่าง 官印相生 + 伤官见官
- **อัพเดท:** ten-gods-affection.md (cross-links), overview.md (+Master Layer theme, page count 31→35), index.md (+4 entries)
- **Round 2 (NotebookLM):** re-auth สำเร็จ → query 4 rounds (full UUID a44aa145, e1f30f92) → อัพเดท 4 หน้าด้วย insights: 交运 (Jiao Yun) term, 显/实 distinction, Ren Tieqiao's Branch emphasis, Wei Qianli example, "Speed Penalty" concept, You Qing ≠ You Li distinction, Sidereal BaZi controversy
- **Round 3 (NotebookLM):** query 3 notebooks (a44aa145, 1da6308d, 0c70b831) → insights: 成格/破格 matrix, Wei Qianli full case + Frozen Water case, 10yr "infinitely more weight" (Sean Chan), Chen-Xu Void removal, Si-Shen relationship penalty, 辰辰自刑 Spouse Palace, "wealth in branches = grows" (Anita Rosenberg), Hidden Stem activation via Clash/Punishment

## [2026-06-01] update | Thai Localization — Chinese-Only UI Text + Deploy

- Fixed `枭神夺食` in 食神格 narrative: now shows `"อินลอบขโมยพร (枭神夺食)"` — Thai first, Chinese in parentheses
- Fixed `Indirect Seal (偏印/枭神)` → `อินนอก (偏印 枭神)`
- Replaced all 7 bare Chinese chip labels in `getBranchInteractionChips` with Thai: รวมพลัง, สามประสาน, ครึ่งประสาน, ชน, โทษ, โทษตน, เบียด
- Interaction card chips: removed Chinese `g.type` prefix — now shows Thai label only
- Self-penalty card: `自刑` → `โทษตน` in chip and branch name line
- Deployed to `https://delicate-peony-3f0dfb.netlify.app` via drag-and-drop

## [2026-06-01] update | Deploy to Netlify

- Deployed `deploy/index.html` (2729 lines) to `https://delicate-peony-3f0dfb.netlify.app` via drag-and-drop
- No code changes — publish of current app state including: Master Reading narrative, LP interactivity, annual luck branch scoring, share/permalink, Five Elements UG labels, twelve stages color coding, LP transition tags, DM strength numeric score fix

## [2026-06-01] fix+update | Strength Score Bug + Stage Color Coding + LP Transition Tags

- **Bug fix (critical):** `getDayMasterStrength` returned a string label ('แข็ง'/'อ่อน'/'สมดุล') but `renderMasterReading` compared it to numbers (strength>=50/70/45) — always evaluated false, DM condition always showed weak variant. Fixed by returning 0-100 numeric score; added `strengthLabel(s)` helper function; updated `getUsefulGod` thresholds (>=60=strong, <=40=weak), `renderDayMaster` badge class logic, and `renderElementBalance` label display
- **DM strength percentage shown:** `renderDayMaster` and `renderElementBalance` now show score as "(N%)" alongside the label
- **Twelve stages color coding:** 长生/临官/帝旺 (indices 0,3,4) highlighted green; 病/死/墓/绝 (6-9) highlighted red; each cell gets a Thai tip line (e.g. "จุดสูงสุด", "กักเก็บ")
- **LP transition tag in annual luck:** years within 2 years of an LP boundary show `🔄LP` purple tag — signals upcoming/recent LP change (often turbulent period)
- File: 2714 → 2729 lines; synced to deploy/index.html

## [2026-06-01] update | LP Enhancements — Hidden Stems + Click Detail + Expanded Narrative

- **LP card hidden stem TG badges:** each LP card now shows tiny colored badges for all hidden stems (藏干) of the LP branch with their TG zh names (e.g. `壬 偏印` · `甲 比肩`)
- **LP card click-to-expand:** clicking any LP card highlights it (`.selected-lp`) and expands `#lp-detail` panel below the grid showing: LP stem/branch + quality badge + road metaphor + hidden stem TG full descriptions + 六冲/六合 clash/harmony with chart pillars
- **LP narrative box (B3) upgraded:** replaced simple alert div with styled box showing LP zh/th, quality badge, road metaphor, hidden stem TG line items with TG.core, peak timing from pattern narrative
- CSS: `.luck-card:hover`, `.luck-card.selected-lp`, `#lp-detail` added
- File: 2646 → 2714 lines; synced to deploy/index.html

## [2026-06-01] update | Five Elements Tab + Current Year Narrative

- **ธาตุ 五行 tab — missing/weak/dominant analysis:** new section below element bars; missing elements (0%) shown with full prescription (color, direction, season, career, health areas); weak elements (<10%) shown with quick tip; dominant elements (≥40%) flagged; five-elements cycle reminder at bottom; UG element labeled on bar
- **"อ่านดวงปีนี้" narrative:** synthesized 3-4 sentence reading for the current year at bottom of 流年 section; covers year TG role, UG alignment sentence, LP context, clash/harmony warning; built from TG_FULL.core + LP_ROAD_NARR logic
- File: 2544 → 2646 lines; synced to deploy/index.html

## [2026-06-01] update | Annual Luck Enhancements — Branch Interactions + Top Years

- **Bug fix:** hardcoded `2026` in `calcAnnualLuck` default param, `renderLuckPillars` currentAge, and `renderAnnualLuck` title → all replaced with `new Date().getFullYear()`
- **scoreAnnualYear enhanced:** now checks 六冲 (BRANCH_SIX_CHONG) against all 4 chart pillar branches; day pillar clash = -2 score, other pillars = -1; 六合 match = +1 bonus
- **Clash tags in table:** years with 六冲 against chart pillars show `⚡ชนวัน/เดือน` red tag in quality cell
- **六合 tags:** years combining with chart branches show `合วัน` blue tag
- **Top years summary box:** "🌟 ปีที่น่าจับตา" (stars≥3, sorted) + "⚡ ปีเปลี่ยนแปลง (六冲)" summary boxes above the table
- File: 2478 → 2544 lines; synced to deploy/index.html

## [2026-06-01] update | Share/Permalink Feature (U1)

- **URL encoding:** form submit pushes `?y=&m=&d=&h=&min=&g=&city=&nt=&lon=` via `history.replaceState`; LINE share and clipboard copy both use the live URL with params
- **Copy Link button:** `🔗 คัดลอกลิงก์` added alongside LINE button in `#output`; uses `navigator.clipboard` with `execCommand` fallback; 2s feedback "✓ คัดลอกแล้ว!"
- **Auto-load on open:** `loadFromURL()` IIFE runs on DOMContentLoaded, reads URL params, populates all form fields, fires `submit` event — chart renders immediately from shared link
- **notime flag:** `nt=1` param suppresses hour/min fields and unchecks required attr correctly on auto-load
- File: 2427 → 2478 lines; synced to deploy/index.html

## [2026-06-01] update | Description Enrichment — Pattern Narratives + Ten Gods (Multi-source)

- **Research:** 4 parallel NotebookLM queries (40-source + 12-source Bazi notebooks, Pattern Narratives notebook, Master Sean Chan/Joey Yap web sources) → extracted DM archetypes, classical quotes, life mission framing for all 10 patterns + all 10 Ten Gods
- **PATTERN_NARRATIVES[].life** (10 patterns) — expanded from 2-sentence descriptions to full mission statements with:
  - Classical text quotes (ZPZQ, DTS) embedded inline
  - Life mission framing ("คุณเกิดมาเพื่อ..." / "ภารกิจชีวิตของคุณคือ...")
  - Key danger/warning from classical texts (枭神夺食, 傷官见官, 建禄不富, 财破印, etc.)
  - Shadow side and what success requires
- **TG_FULL[].core** (10 Ten Gods) — upgraded from keyword lists to narrative sentences:
  - 比肩: "พลังตัวตนที่แน่วแน่ — คุณพึ่งตัวเองได้ดี... แต่ระวังความดื้อรั้น"
  - 食神: "พรสวรรค์ที่สร้างความสุขและดึงดูดโชคลาภ — ตำราเรียกว่า 'ดาวแห่งอายุยืนและทรัพย์'"
  - 七杀: "อำนาจที่เด็ดขาดในภาวะวิกฤต — 食神制杀 หรือ 印绶化杀 = ผู้นำที่ทรงอิทธิพล"
  - (all 10 upgraded)
- File: 2427 lines (in-place replacement); synced to deploy/index.html

## [2026-06-01] update | Master Reading v2 — Fortune Teller Prose Upgrade (Sean Chan / Joey Yap style)

- **Research:** NotebookLM query on 40-source + 12-source Bazi notebooks + Master Sean Chan sample report + Joey Yap profiling PDF → synthesized 5 narrative techniques
- **DM_CONDITION (10 entries):** new constant — element-as-condition prose (strong vs weak variant per stem), e.g. "ต้นไม้ใหญ่ที่พุ่งสู่ท้องฟ้าเต็มกำลัง — แต่ระวังความแข็งกระด้างจนหักโดยไม่ยอมโค้ง"
- **LP_ROAD_NARR (5 keys):** new constant — car/road metaphor per LP quality (same/gen/ctr/weakens/neutral)
- **Para 1 upgrade:** DM condition sentence injected (strong vs weak based on strength≥50); "cost of personality" shadow side included
- **Para 2 upgrade:** "ขีดความสามารถในการรับภาระ" capacity-to-carry framing replaces generic "แข็งแกร่ง/สมดุล/อ่อน" grade language
- **Para 6 upgrade:** renamed to "ช่วงชีวิต (Elemental Phase)" per Sean Chan; road metaphor sentence from LP_ROAD_NARR appended; peak timing as subscript
- **Opening hook:** honest-conversational 1-line before paragraphs — "ดวงชะตาคือแผนที่ ไม่ใช่บทละครที่ถูกเขียนตายตัว"
- File: 2391 → 2427 lines; synced to deploy/index.html

## [2026-06-01] update | Master Reading — Fortune Teller Narrative Upgrade

- **renderMasterReading(chart,sec):** new function replacing the old DM Profile card; outputs 7 labeled paragraphs as flowing prose
- **Para 1 (ตัวตน):** Day Master zh + STEM_DESC metaphor + PATTERN_DATA格局 name + purity badge
- **Para 2 (พลังธาตุ):** top 2 elements by % + DM strength sentence (strong/balanced/weak framing)
- **Para 3 (เส้นทางชีวิต):** full PATTERN_NARRATIVES.life text embedded verbatim
- **Para 4 (อาชีพ & การเงิน):** PATTERN_NARRATIVES.career + .wealth as two lines
- **Para 5 (แรงตึงในดวง):** top 2 Ten Gods by priority (Officer→Killing→Wealth→Output…) + detected 六冲 clashes with narrative
- **Para 6 (ช่วงชีวิตปัจจุบัน):** current Luck Pillar by birth year/current year + LP_QUALITY_DESC badge + pn.peak
- **Para 7 (คำแนะนำ):** pn.ug_tip + pn.challenge + UG_LIFE_GUIDANCE finance line
- **DM Profile card removed** from renderInterpretation; TG section relabelled "รายละเอียดสิบเทพในดวงของคุณ"
- CSS: `.master-reading`, `.mr-para`, `.mr-label`, `.mr-text em`, `.mr-divider` added
- File: 2309 → 2391 lines; synced to deploy/index.html

## [2026-06-01] update | Narrative Enrichment Pack — 合冲刑害 + Stem Personalities + 天干合

- **STEM_DESC (10 entries):** classical metaphor (大樹/花草/太陽/燈火/山嶽/田園/刀斧/珠寶/大海/雨露) + personality sentence; shown as italic line under each stem in pillar table
- **Branch interaction data:** BRANCH_SIX_HE (六合×6), BRANCH_THREE_HE (三合×4), BRANCH_SIX_CHONG (六冲×6), BRANCH_SAN_XING (三刑×3)+BRANCH_SELF_XING, BRANCH_SIX_HAI (六害×6); all with Thai narrative
- **STEM_FIVE_HE (5 entries):** 天干五合 with result element + narrative
- **detectBranchInteractions():** checks all pillar pairs/triples for 合冲刑害; returns categorised results
- **detectStemCombos():** checks 4 stems for 天干合 pairings
- **getBranchInteractionChips():** maps pillar index to chip list for badge row
- **renderStemCombos():** colored card section below pillar table (only if combos found)
- **renderBranchInteractions():** interaction narrative cards grouped by type after 十二長生 section
- **pillar table:** new stem-metaphor line + new interaction badge row (4th row) showing 六合/三合/六冲/三刑/六害 chips per branch
- **Files:** app/bazi.html (2309 lines), deploy/index.html synced

## [2026-05-31] update | D2 Compatibility Check — ความเข้ากัน 合

- **Feature:** compat mini-form (year/month/day/hour/min/gender for person B) appears below main chart output
- **`TG_COMPAT_MEANING`:** 10-entry constant — romantic feel + tip per Ten God index
- **`computeCompatibility(chartA,chartB)`:** computes tgAtoB / tgBtoA via `getTenGodIdx`, affinity stars (1–5) by spouse-star logic + TG pair patterns (傷官見官→2★, peer→2★, spouse pair→5★)
- **`renderCompatibility`:** two-column card — star rating + synergy line + A→B and B→A TG panels with element-colored DM names
- **Wiring:** main submit → sets `currentChart`, shows `#compat-wrap`; compat submit → `calculateBazi` for person B → render; c2-day populates dynamically
- **Files:** app/bazi.html (2055 lines), deploy/index.html synced

## [2026-05-31] update | D1 Fortune Card — ดวงชะตาสรุป

- **Feature:** `renderFortuneCard()` — new screenshot-worthy summary card at top of ดวงชะตา tab
- **Zone 1:** Header bar "✦ ดวงชะตาของคุณ · ปี 2026" + 📋 คัดลอก button (clipboard API + flash confirm)
- **Zone 2:** Identity line — DM icon + zh/th + element polarity + Pattern name + Purity badge (color-coded Pure/有情/雜)
- **Zone 3:** Quote — first sentence of `PATTERN_NARRATIVES[monthTG].life`, italic blockquote style
- **Zone 4:** Three mini-chips — Useful God (element + career hint) / Current LP (age range + quality badge) / Top auspicious Shen Sha (name + life tip)
- **Removed:** old B2 run-on paragraph; DM card + TG grid + dominant element section unchanged below the card
- **Files:** app/bazi.html (1876 lines), deploy/index.html synced

## [2026-05-31] update | App interpretation depth — 5 enhancements

- **I — LP Forecast badges**: LP_QUALITY_DESC constant + all 8 Luck Pillar cards now show colored quality badge (🌟เสริม UG / ✅สร้าง UG / ⚠️ขัด UG / ↘ดูดพลัง / ➡กลาง)
- **II — Annual luck quality stars**: scoreAnnualYear() function + คอลัมน์คุณภาพ ★ ใน annual luck table พร้อม ✦ดาวคู่ tag เมื่อ LP+year ตรง UG พร้อมกัน
- **III — Purity explanation**: getPurityExplanation() — ข้อความอธิบายว่าทำไม格局ถึงบริสุทธิ์/ผสม แสดงใต้ purity badge
- **IV — UG Life Guidance cards**: UG_LIFE_GUIDANCE constant (5 elements) + 3 mini-cards (💼อาชีพ / ❤ความสัมพันธ์ / 💰การเงิน) ใต้ UG grid ในแท็บ格局
- **V — Special pattern condition checklist**: detectFollowPattern/detectDominantPattern คืน conditions[] — แสดงเป็น checklist ใน banner ของ Follow/Dominant patterns
- **Tests**: เพิ่ม 4 tests ใหม่ รวม 63/63 tests passed; sync deploy/index.html

## [2026-05-31] update | Dominant Patterns (专旺格) wiki + app detection

- **Wiki:** สร้าง dominant-patterns.md (31st page) — 5 ประเภท: 曲直/炎上/稼穡/从革/润下, branch directional+three-harmony combos, no-controlling-element rules, ผลชีวิตแต่ละ type
- **App:** เพิ่ม `detectDominantPattern()` — ตรวจ `brHas()` directional/three-harmony + `noEl()` controlling element; gold banner ใน格局 tab
- **Files:** app/bazi.html, deploy/index.html (135,168 bytes), wiki/concepts/dominant-patterns.md, index.md (31 pages), overview.md
- **Tests:** 56/56 passed (ก่อนเพิ่ม dominant test)

## [2026-05-31] update | Follow Patterns (从格) wiki + app detection

- **Wiki:** สร้าง follow-patterns.md (30th page) — 4 ประเภท: 从财/从儿/从杀/从势, เงื่อนไข DM rootless + no Peer + no Seal + dominant TG ≥40%, Pure vs Flawed
- **App:** เพิ่ม `detectFollowPattern()` — ตรวจ DM rootlessness across all branch hidden stems, นับ TG groups, เรียกก่อน normal pattern detection; purple banner ใน格局 tab
- **App:** `getPattern()` รับ `dayP` parameter ใหม่ — ส่งต่อจาก `calculateBazi()`
- **Source:** cantian.ai (从财格, 从儿格) + deeporacle.ai (all 4 types)
- **Tests:** 56/56 passed

## [2026-05-31] update | Pattern Purity badge in app

- **Feature:** 格局 tab now shows 純格/有情格/雜格 purity badge (coloured, with description)
- **Logic:** `getPattern()` returns `purity` field — pure = transparent+!mixed, affectionate = !transparent+!mixed, mixed = any mixing
- **Source:** logic from [[pattern-purity.md]] ZPZQ 3-level classification
- **Files:** app/bazi.html (getPattern + renderPattern), deploy/index.html synced
- **Tests:** 53/53 passed
- **Wiki:** overview.md sources count cosmetic fix (2→3)

## [2026-05-31] ingest | bazisearch — Classical Masters + Pattern Purity + 化格

- **สร้าง entity pages ใหม่ 3 หน้า:** xu-ziping.md (ห้าราชวงศ์→ซ่งเหนือ), shen-xiaozhan.md (ราชวงศ์ชิง, Jinshi 1739, เขียน ZPZQ), ren-tieqiao.md (1773–1848, วิจารณ์ Di Tian Sui)
- **สร้าง concept pages ใหม่ 2 หน้า:** pattern-purity.md (透出 mechanism, 純格/有情格/雜格 3 ระดับ, ตัวอย่าง ZPZQ), transformation-patterns.md (5 ประเภท 化格, True vs False conditions, ผลชีวิตแต่ละ type)
- **Cross-links:** entity pages link กัน (Xu Ziping ↔ Shen Xiaozhan ↔ Ren Tieqiao) + link concept pages (ZPZQ, Di Tian Sui, patterns.md)
- **Contradictions:** ไม่มี — งาน Classical Masters เป็นข้อมูลใหม่ที่ยังไม่มีใน wiki ก่อนหน้า
- **อัปเดต:** index.md (24→29 pages, เพิ่ม Entities section + 2 concept entries), overview.md (pages 24→29, Recent updates)
- **Source method:** WebSearch 2026-05-31 (NotebookLM notebooks e165bb2f + 2ff215a5 ยังประมวลผล)

## [2026-05-31] fix | duplicate const topEl crash

- **Bug:** `const topEl` declared twice ใน `renderInterpretation()` — B2 (line 1375) + Dominant Element section (line 1460) → SyntaxError ทำให้ script ไม่ load เลย form ใช้ไม่ได้
- **Fix:** ลบ `const topEl` ที่ duplicate ออก (line 1460) → ใช้ตัวแปรเดิมจาก B2 section
- **Root cause:** Pre-existing ตั้งแต่ B2 update ไม่ถูกตรวจจับเพราะ test suite ไม่ test UI form

## [2026-05-31] update | C1+C2+C3 App features complete

- **C1 (Ten Gods Affection Matrix):** เพิ่มใน tab สิบเทพ — ตรวจจับคู่ปฏิสัมพันธ์ Ten Gods จากดวงจริง (11 patterns: 官印相生 ★★★★★ ถึง 比劫争财 ★★) แสดงการ์ดสี เขียว/แดง/เหลือง พร้อม tip จาก ZPZQ
- **C2 (Pillar Domain Analysis):** เพิ่มใน tab สี่เสา — 4 การ์ดตาม domain: เสาปี (รากฐาน 0-16), เสาเดือน (อาชีพ 17-35), เสาวัน (Spouse Palace gender-aware), เสาเวลา (ลูก/มรดก 52+); Spouse Palace อ่านดาวทรัพย์ (ดวงชาย) หรือออฟิเซอร์ (ดวงหญิง)
- **C3 (Shen Sha expanded):** เพิ่มในทุก star card — "ผลในชีวิต" และ "⚡ Activate: ..." จาก SS_TIPS 14 entries; แก้ key ให้ตรงกับ zh string จริง (驿马星, 桃花星 มี suffix 星; เพิ่ม 华盖)
- **Data tables ใหม่ใน bazi.html:** TG_AFFECTIONS (11 entries), SS_TIPS (14 entries)
- **gender** เพิ่มใน calculateBazi return — ใช้ใน Spouse Palace reading
- **Deploy:** synced to deploy/index.html (127,819 bytes, 1,496 lines)

## [2026-05-31] lint | full wiki health check — 2 issues fixed

- **Missing pages:** 0 ✓
- **Orphans (fixed):** pillar-domain-rules + ten-gods-affection → เพิ่ม backlinks จาก overview.md + pattern-narratives.md
- **Stubs:** earthly-branches / heavenly-stems / qiong-tong-bao-jian แสดง 0 sentences (false positive — Thai format ไม่มี `. ` แต่ content ครบ 44-55 บรรทัด)
- **Stale overview (fixed):** อัปเดต overview.md — updated 2026-05-19 → 2026-05-31, pages 20→24, sources 2→3, เพิ่ม Recent updates 3 entries
- **Contradictions:** 0 ✓
- **Suggested sources:** pattern purity examples จาก ZPZQ ยังขาด — open research gap

## [2026-05-31] update | A4+A5 wiki + B1-B3 App Narrative Engine complete

- **A4:** เพิ่ม section "Useful God as Life Direction" ใน wiki/concepts/useful-god.md — ตาราง per-element UG แนวทางอาชีพ/ความสัมพันธ์/การเงิน + กฎ LP เสริม/ขัดแย้ง UG
- **A5:** เพิ่ม section "Luck Pillar × Pattern — สูตรการพยากรณ์ทศวรรษ" ใน wiki/concepts/luck-pillars.md — ตาราง LP × Pattern (10 patterns), LP Transition Period, Double Luck formula
- **B1 (Pattern Life Narrative):** เพิ่มใน tab 格局/用神 — เส้นทางชีวิต/อาชีพ/ทรัพย์/ท้าทาย/จุดพีค + UG tip
- **B2 (Chart Summary):** เพิ่มที่ต้น tab ดวงชะตา ✦ — ย่อหน้าสังเคราะห์ DM+Pattern+TG+ธาตุเด่น+UG
- **B3 (LP Narrative):** เพิ่มใน tab 大運/流年 — emoji UG comparison per card + กล่องช่วงปัจจุบัน
- **Data tables ใหม่ใน bazi.html:** PATTERN_NARRATIVES (10 entries), UG_EL_NARRATIVE (5 elements)
- **Deploy:** https://delicate-peony-3f0dfb.netlify.app (ready)
- **Tests:** test_suite_v3.html 58/58 PASSED (50 เดิม + 8 B-tests ใหม่)

## [2026-05-30] ingest | Ten Gods Affection Matrix — bazisearch A3

- **สร้างหน้าใหม่ 1 หน้า:** wiki/concepts/ten-gods-affection.md — ปฏิสัมพันธ์คู่ Ten Gods ทั้งหมด: 5 auspicious combinations (官印相生, 食神生财, 傷官生财, 食神制杀, 印绶化杀) + 5 destructive combinations (傷官见官, 财破印, 枭神夺食, 官杀混杂, 比劫争财)
- **Matrix สรุป:** ตาราง 11 คู่ พร้อม rating ★ และผลหลักในชีวิต
- **วิธีใช้:** Step-by-step วิธีอ่านดวงด้วย combination matrix + Luck Pillar activation
- **แหล่งข้อมูล:** WebSearch 2026-05-30 (masterseanchan.com, imperialharvest.com, ZPZQ classical references)
- **อัปเดต index.md** (24 หน้า) และ log.md

## [2026-05-30] ingest | Pillar Domain Rules — bazisearch A2

- **สร้างหน้าใหม่ 1 หน้า:** wiki/concepts/pillar-domain-rules.md — ความหมายเฉพาะของ 4 เสา: Year (บรรพบุรุษ 0-16), Month (อาชีพ Pattern 17-35), Day (ตัวตน/คู่ครอง 36-51), Hour (ลูก/มรดก 52+)
- **เนื้อหา:** TG ของแต่ละเสา + ความหมาย, Day Branch = Spouse Palace, กฎการชน, วิธีสังเคราะห์ทั้งสี่เสาเป็นประโยคเดียว
- **แหล่งข้อมูล:** WebSearch 2026-05-30 (yourchineseastrology.com, shen-shu.com, kenlai.wordpress.com, masterseanchan.com)
- **อัปเดต index.md** (23 หน้า) และ log.md

## [2026-05-30] ingest | 格局 Pattern Life Narratives — bazisearch A1

- **สร้างหน้าใหม่ 1 หน้า:** wiki/concepts/pattern-narratives.md — เส้นทางชีวิตตาม Pattern ครบ: 8 Normal (建禄格 月刃格 食神格 傷官格 偏财格 正财格 七杀格 正官格 偏印格 正印格) + 4 Follow patterns (从财 从官杀 从儿 从势) + 5 Dominant patterns (曲直 炎上 稼穑 从革 润下)
- **เนื้อหาต่อ Pattern:** เส้นทางชีวิต, อาชีพ, ทรัพย์, Useful God, Nemesis, Luck Pillar activation
- **ตาราง Useful God × Pattern** ครบทุก 10 Normal patterns
- **หลักการ Pattern Purity:** 純格 vs 有情格 vs 雜格 + กฎ LP × Pattern activation
- **แหล่งข้อมูล:** WebSearch 2026-05-30 (cantian.ai, deeporacle.ai, masterseanchan.com) + ZPZQ classical text references
- **อัปเดต index.md** (22 หน้า, 3 sources) และ log.md
- NotebookLM notebook `0c70b831-ca53-4966-95a4-06f4935baa63` สร้างแล้ว (auth issue ทำให้เพิ่ม sources ได้จำกัด)



## [2026-05-30] ingest | Thai regional practice + True Solar Time — WebSearch session

- **สร้างหน้าใหม่ 1 หน้า:** wiki/concepts/true-solar-time.md — เวลาสุริยะจริง: สูตร Longitude Correction + Equation of Time (Spencer 1971), ตารางเมืองไทย 7 เมือง, กรณีพิเศษ WWII UTC+9, pseudocode สำหรับ application
- **อัปเดต wiki/concepts/schools.md:** เพิ่มส่วน "Thai Practice — โครงสร้าง 3 ชั้น" และ "Regional Comparison — ไทย vs จีน vs สิงคโปร์"
- **อัปเดต wiki/concepts/comparative-sources.md:** ขยาย Thailand row ในตาราง Regional Adaptations (ปาขื่อ, 3-layer structure, True Solar Time gap), เพิ่ม Singapore/Malaysia row, อัปเดต Research Gaps
- **อัปเดต index.md** (21 หน้า) และ log.md
- ไม่พบ contradictions — ข้อมูลใหม่ขยายส่วนที่ระบุว่า "understudied" ใน comparative-sources เดิม
- Source: WebSearch session 2026-05-30 (ปาขื่อ, Bazi Thailand, Bazi schools, True Solar Time)

## [2026-05-29] lint | full wiki health check — pass

- ตรวจ 20 หน้า: 5 หมวด (contradictions, orphans, stubs, missing pages, stale overview)
- **ผลลัพธ์: 0 critical issues** — wiki สะอาดสมบูรณ์
- ยืนยัน page count 20 ตรงกับ index.md + overview.md frontmatter
- พบ minor: ten-gods.md + patterns.md ไม่มี aliases field (ไม่ blocking — links ปัจจุบันใช้ title ตรงๆ)
- บันทึก 4 open research gaps ที่ยังไม่ได้ปิด (Pseudo-Follow, Hidden Stem rooting weights, Ge Ju→careers, Thai academic sources)

## [2026-05-19] ingest | comparative research — NotebookLM e1f30f92 + WebSearch

- **สร้างหน้าใหม่ 1 หน้า:** wiki/concepts/comparative-sources.md — cross-source comparative analysis (5 classical texts, schools, regional traditions, academic critique, non-falsifiability)
- **เขียนใหม่ 1 หน้า:** wiki/concepts/methodology.md — ปรับโครงสร้างเป็น 8-section format ใหม่ พร้อมข้อขัดแย้งในแต่ละขั้นตอน
- **อัปเดต 3 หน้า:** useful-god.md (ZPZQ vs QTBJ contradiction block), schools.md (Xu Ziping historical uncertainty + epistemological critique), overview.md (Regional Traditions section)
- **อัปเดต index.md** (20 หน้า, 2 sources) และ log.md
- **อัปเดต SKILL.md** — เพิ่ม Notebook ID: Methodology a44aa145 + Comparative e1f30f92
- Source: NotebookLM e1f30f92 (9 sources) + WebSearch bazi_comparative_research.md

## [2026-05-19] lint | pass 2 verification — all checks clean

- ตรวจสอบ 5 หมวด: broken wikilinks, unregistered pages, orphan pages, missing frontmatter, stray files
- **ผลลัพธ์: 0 issues** ทั้ง 5 หมวดผ่านสะอาด
- พบและแก้ไข page count ที่ผิด: index.md + overview.md แสดง 22 (ผิด) → แก้เป็น 19 (จำนวนจริง)
- ยืนยัน 12 aliases ที่เพิ่มใน pass 1 ทำงานถูกต้องทุกตัว — wikilinks resolve ครบ 19 หน้า

## [2026-05-18] lint | full wiki health check and repair

- **ลบ 3 stray empty files** ที่ vault root: `สิบเทพ (十神).md`, `กิ่งฟ้า (Heavenly Stems).md`, `穷通宝鑑 Qiong Tong Bao Jian.md` — ไม่มีเนื้อหา แต่ hijack wikilink resolution
- **เพิ่ม aliases frontmatter** ใน 12 หน้า (7 concepts + 5 texts) เพื่อให้ wikilinks ที่ใช้ชื่อย่อ/ต่างจาก title resolve ได้ใน Obsidian
- **Register wiki/concepts/methodology.md** ใน index.md — หน้านี้มีอยู่แล้วแต่ไม่ถูกลงทะเบียน (orphan + unregistered)
- **เพิ่ม link ถึง methodology.md** ใน wiki/overview.md ภายใต้ Key themes — แก้ orphan status
- **อัปเดต page count** จาก 21 → 22 ใน index.md และ overview.md
- พบ note: wiki/texts/*.md ใช้ `type: text` ซึ่งไม่อยู่ใน schema — พิจารณาเปลี่ยนเป็น `source` ในอนาคต

## [2026-05-17] ingest | Bazi_Comprehensive_Research.md — comprehensive Bazi research

- อ่านและประมวลผล Bazi_Comprehensive_Research.md (503 บรรทัด) จาก local agent session
- **สร้าง concept pages ใหม่ 5 หน้า:** ten-gods.md (ตารางครบ), useful-god.md (สองแนวทาง+ความขัดแย้ง), patterns.md (~22 patterns จาก ZPZQ), shen-sha.md (ดาวมงคล+ท้าทาย), schools.md (4 สำนัก)
- **สร้าง wiki/texts/ folder + 5 text pages:** di-tian-sui.md, yuan-hai-zi-ping.md, san-ming-tong-hui.md, qiong-tong-bao-jian.md, zi-ping-zhen-quan.md
- **อัปเดต 7 concept pages เดิม** ให้ใช้ bazisearch 8-section structure + เพิ่มข้อมูล: bazi.md (ประวัติ Tang-Song-Ming-Qing), day-master.md (Strength Debate + Follow/Dominant), luck-pillars.md (วิธีคำนวณละเอียด), five-elements.md, four-pillars.md, heavenly-stems.md, earthly-branches.md
- อัปเดต index.md (21 หน้า) และ wiki/overview.md (thesis ใหม่ + open questions อัปเดต)
- ไม่พบ contradictions หลัก — ข้อมูลที่เพิ่มเข้ามาเสริมและขยาย concept เดิม

## [2026-05-16] update | web research — Bazi concept pages ภาษาไทย

- ค้นคว้าข้อมูล Bazi จากแหล่งภาษาไทยและอังกฤษ (fengshuix.com, mahamongkol.com, Wikipedia, imperialharvest.com, thaibazi.blogspot.com และอื่นๆ)
- สร้าง 7 concept pages ใหม่ทั้งหมดเป็นภาษาไทย: bazi.md, four-pillars.md, five-elements.md, heavenly-stems.md, earthly-branches.md, day-master.md, luck-pillars.md
- ทุกหน้ามี wikilinks เชื่อมโยงซึ่งกันและกันครบถ้วน
- อัปเดต wiki/overview.md (thesis เป็นภาษาไทย, เพิ่ม key themes และ open questions)
- อัปเดต index.md (8 หน้า, 0 sources)
- ไม่พบ contradictions เนื่องจากเป็นการสร้างครั้งแรก

## [2026-05-16] init | wiki domain set to Bazi

- User confirmed domain: Bazi (八字), Four Pillars of Destiny
- Created wiki/overview.md with domain thesis, key themes, open questions
- Updated index.md (1 page, 0 sources)

## [2026-05-16] init | wiki agent setup

- Created CLAUDE.md with full wiki agent schema (INGEST, QUERY, LINT operations)
- Created directory structure: wiki/entities/, wiki/concepts/, wiki/sources/, wiki/queries/, raw/assets/
- Created starter index.md and log.md
- wiki/overview.md not yet created — pending user input on wiki domain/focus
