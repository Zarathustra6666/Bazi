"""
Wiki integrity tests for C:\Vault\Bazi
Tests: file existence, frontmatter, index consistency, new pages from bazisearch session
"""
import os, re, sys

BASE = r"C:\Vault\Bazi"
WIKI = os.path.join(BASE, "wiki")
PASS = []
FAIL = []

def ok(name):
    PASS.append(name)

def fail(name, msg):
    FAIL.append(f"{name}: {msg}")

def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip()
    return fm

# ── 1. New entity pages exist ──────────────────────────────────────────────
for slug, label in [
    ("xu-ziping",    "Xu Ziping entity page"),
    ("shen-xiaozhan","Shen Xiaozhan entity page"),
    ("ren-tieqiao",  "Ren Tieqiao entity page"),
]:
    path = os.path.join(WIKI, "entities", f"{slug}.md")
    if os.path.exists(path):
        ok(label)
    else:
        fail(label, f"file not found: {path}")

# ── 2. New concept pages exist ────────────────────────────────────────────
for slug, label in [
    ("pattern-purity",          "Pattern Purity concept page"),
    ("transformation-patterns", "Transformation Patterns concept page"),
]:
    path = os.path.join(WIKI, "concepts", f"{slug}.md")
    if os.path.exists(path):
        ok(label)
    else:
        fail(label, f"file not found: {path}")

# ── 3. Frontmatter required fields on all 5 new pages ────────────────────
REQUIRED_FM = ["title", "type", "tags", "created", "updated", "sources"]
new_pages = [
    os.path.join(WIKI, "entities", "xu-ziping.md"),
    os.path.join(WIKI, "entities", "shen-xiaozhan.md"),
    os.path.join(WIKI, "entities", "ren-tieqiao.md"),
    os.path.join(WIKI, "concepts", "pattern-purity.md"),
    os.path.join(WIKI, "concepts", "transformation-patterns.md"),
]
for path in new_pages:
    if not os.path.exists(path):
        continue
    name = os.path.basename(path)
    fm = frontmatter(read(path))
    for field in REQUIRED_FM:
        if field in fm:
            ok(f"{name} has '{field}'")
        else:
            fail(f"{name} frontmatter", f"missing field '{field}'")

# ── 4. Entity type check ───────────────────────────────────────────────────
for slug in ["xu-ziping", "shen-xiaozhan", "ren-tieqiao"]:
    path = os.path.join(WIKI, "entities", f"{slug}.md")
    if os.path.exists(path):
        fm = frontmatter(read(path))
        if fm.get("type") == "entity":
            ok(f"{slug} type=entity")
        else:
            fail(f"{slug} type", f"expected 'entity', got '{fm.get('type')}'")

# ── 5. Concept type check ──────────────────────────────────────────────────
for slug in ["pattern-purity", "transformation-patterns"]:
    path = os.path.join(WIKI, "concepts", f"{slug}.md")
    if os.path.exists(path):
        fm = frontmatter(read(path))
        if fm.get("type") == "concept":
            ok(f"{slug} type=concept")
        else:
            fail(f"{slug} type", f"expected 'concept', got '{fm.get('type')}'")

# ── 6. index.md pages count = 29 ──────────────────────────────────────────
index = read(os.path.join(BASE, "index.md"))
if "**Pages:** 29" in index:
    ok("index.md pages count = 29")
else:
    fail("index.md pages count", "expected '**Pages:** 29' not found")

# ── 7. index.md has Entities section with 3 entries ──────────────────────
entities_section = re.search(r"## Entities\n(.*?)(?=\n##|\Z)", index, re.DOTALL)
if entities_section:
    entries = [l for l in entities_section.group(1).splitlines() if l.strip().startswith("-")]
    if len(entries) >= 3:
        ok(f"index.md Entities section has {len(entries)} entries (≥3)")
    else:
        fail("index.md Entities", f"expected ≥3 entries, found {len(entries)}")
else:
    fail("index.md Entities", "section not found")

# ── 8. overview.md pages count = 29 ───────────────────────────────────────
overview = read(os.path.join(WIKI, "overview.md"))
if "pages: 29" in overview and "**Wiki pages:** 29" in overview:
    ok("overview.md pages count = 29 (frontmatter + body)")
else:
    fail("overview.md pages count", "expected 'pages: 29' and '**Wiki pages:** 29'")

# ── 9. overview.md has bazisearch recent update entry ─────────────────────
if "bazisearch" in overview and "Classical Masters" in overview:
    ok("overview.md has bazisearch recent update")
else:
    fail("overview.md recent update", "missing bazisearch / Classical Masters entry")

# ── 10. log.md has bazisearch ingest entry ────────────────────────────────
log = read(os.path.join(BASE, "log.md"))
if "ingest | bazisearch" in log:
    ok("log.md has bazisearch ingest entry")
else:
    fail("log.md", "missing 'ingest | bazisearch' entry")

# ── 11. Cross-links: entity pages link to each other ─────────────────────
xu = read(os.path.join(WIKI, "entities", "xu-ziping.md")) if os.path.exists(os.path.join(WIKI, "entities", "xu-ziping.md")) else ""
shen = read(os.path.join(WIKI, "entities", "shen-xiaozhan.md")) if os.path.exists(os.path.join(WIKI, "entities", "shen-xiaozhan.md")) else ""
ren = read(os.path.join(WIKI, "entities", "ren-tieqiao.md")) if os.path.exists(os.path.join(WIKI, "entities", "ren-tieqiao.md")) else ""

if "Shen Xiaozhan" in xu:
    ok("xu-ziping links to Shen Xiaozhan")
else:
    fail("xu-ziping cross-link", "missing link to Shen Xiaozhan")

if "Xu Ziping" in shen:
    ok("shen-xiaozhan links to Xu Ziping")
else:
    fail("shen-xiaozhan cross-link", "missing link to Xu Ziping")

if "Shen Xiaozhan" in ren:
    ok("ren-tieqiao links to Shen Xiaozhan")
else:
    fail("ren-tieqiao cross-link", "missing link to Shen Xiaozhan")

# ── 12. Pattern pages reference ZPZQ / Di Tian Sui ───────────────────────
pp = read(os.path.join(WIKI, "concepts", "pattern-purity.md")) if os.path.exists(os.path.join(WIKI, "concepts", "pattern-purity.md")) else ""
tp = read(os.path.join(WIKI, "concepts", "transformation-patterns.md")) if os.path.exists(os.path.join(WIKI, "concepts", "transformation-patterns.md")) else ""

if "子平真诠" in pp or "ZPZQ" in pp:
    ok("pattern-purity references ZPZQ")
else:
    fail("pattern-purity", "missing ZPZQ reference")

if "化格" in tp:
    ok("transformation-patterns has 化格 content")
else:
    fail("transformation-patterns", "missing 化格 content")

# ── 13. bazi.html has TG_AFFECTIONS and SS_TIPS ───────────────────────────
bazi_html = os.path.join(BASE, "app", "bazi.html")
if os.path.exists(bazi_html):
    html = read(bazi_html)
    if "TG_AFFECTIONS" in html:
        ok("bazi.html contains TG_AFFECTIONS")
    else:
        fail("bazi.html", "TG_AFFECTIONS not found")
    if "SS_TIPS" in html:
        ok("bazi.html contains SS_TIPS")
    else:
        fail("bazi.html", "SS_TIPS not found")
    tg_count = html.count("zh:'")
    if tg_count >= 11:
        ok(f"bazi.html TG_AFFECTIONS has ≥11 entries (found {tg_count})")
    else:
        fail("bazi.html TG_AFFECTIONS count", f"expected ≥11, found {tg_count}")
else:
    fail("bazi.html", f"file not found: {bazi_html}")

# ── Report ─────────────────────────────────────────────────────────────────
total = len(PASS) + len(FAIL)
print(f"\n{'='*55}")
print(f"  Bazi Wiki Tests: {len(PASS)}/{total} passed")
print(f"{'='*55}")
if FAIL:
    print("\nFAILED:")
    for f in FAIL:
        print(f"  ✗ {f}")
if PASS:
    print("\nPASSED:")
    for p in PASS:
        print(f"  ✓ {p}")
print(f"\n{'='*55}")
sys.exit(0 if not FAIL else 1)
