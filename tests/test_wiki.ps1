# Wiki integrity tests for C:\Vault\Bazi
# Tests: file existence, frontmatter, index/overview consistency, new bazisearch pages

$BASE  = "C:\Vault\Bazi"
$WIKI  = "$BASE\wiki"
$PASS  = @()
$FAIL  = @()

function ok($name)        { $script:PASS += $name }
function fail($name, $msg){ $script:FAIL += "${name}: $msg" }

function Has($text, $sub) { $text.Contains($sub) }

# ── 1. New entity pages exist ─────────────────────────────────────────────
foreach ($slug in @("xu-ziping","shen-xiaozhan","ren-tieqiao")) {
    $p = "$WIKI\entities\$slug.md"
    if (Test-Path $p) { ok "$slug.md exists" }
    else              { fail "$slug.md" "file not found" }
}

# ── 2. New concept pages exist ────────────────────────────────────────────
foreach ($slug in @("pattern-purity","transformation-patterns")) {
    $p = "$WIKI\concepts\$slug.md"
    if (Test-Path $p) { ok "$slug.md exists" }
    else              { fail "$slug.md" "file not found" }
}

# ── 3. Frontmatter required fields on all 5 new pages ────────────────────
$required = @("title","type","tags","created","updated","sources")
$newPages = @(
    "$WIKI\entities\xu-ziping.md",
    "$WIKI\entities\shen-xiaozhan.md",
    "$WIKI\entities\ren-tieqiao.md",
    "$WIKI\concepts\pattern-purity.md",
    "$WIKI\concepts\transformation-patterns.md"
)
foreach ($p in $newPages) {
    if (-not (Test-Path $p)) { continue }
    $name = Split-Path $p -Leaf
    $text = Get-Content $p -Raw -Encoding UTF8
    foreach ($field in $required) {
        if ($text -match "(?m)^$field\s*:") { ok "$name has '$field'" }
        else { fail "$name frontmatter" "missing field '$field'" }
    }
}

# ── 4. Entity type = entity ───────────────────────────────────────────────
foreach ($slug in @("xu-ziping","shen-xiaozhan","ren-tieqiao")) {
    $p = "$WIKI\entities\$slug.md"
    if (Test-Path $p) {
        $text = Get-Content $p -Raw -Encoding UTF8
        if ($text -match "(?m)^type:\s*entity") { ok "$slug type=entity" }
        else { fail "$slug type" "expected 'entity'" }
    }
}

# ── 5. Concept type = concept ─────────────────────────────────────────────
foreach ($slug in @("pattern-purity","transformation-patterns")) {
    $p = "$WIKI\concepts\$slug.md"
    if (Test-Path $p) {
        $text = Get-Content $p -Raw -Encoding UTF8
        if ($text -match "(?m)^type:\s*concept") { ok "$slug type=concept" }
        else { fail "$slug type" "expected 'concept'" }
    }
}

# ── 2b. follow-patterns.md and dominant-patterns.md exist ────────────────
foreach ($slug in @("follow-patterns","dominant-patterns")) {
    $p = "$WIKI\concepts\$slug.md"
    if (Test-Path $p) { ok "$slug.md exists" }
    else { fail "$slug.md" "file not found" }
}

# ── 6. index.md pages count = 31 ─────────────────────────────────────────
$index = Get-Content "$BASE\index.md" -Raw -Encoding UTF8
if (Has $index "**Pages:** 31") { ok "index.md pages count = 31" }
else { fail "index.md pages count" "expected '**Pages:** 31'" }

# ── 7. index.md Entities section has ≥3 entries ───────────────────────────
$entSection = if ($index -match "(?s)## Entities\n(.*?)(?=\n##)") { $Matches[1] } else { "" }
$entCount = ($entSection -split "\n" | Where-Object { $_ -match "^\s*-" }).Count
if ($entCount -ge 3) { ok "index.md Entities has $entCount entries (>=3)" }
else { fail "index.md Entities" "expected >=3 entries, found $entCount" }

# ── 7b. bazi.html has Follow Pattern detection ────────────────────────────
$htmlPath = "$BASE\app\bazi.html"
$html = if (Test-Path $htmlPath) { Get-Content $htmlPath -Raw -Encoding UTF8 } else { "" }
if (Has $html "detectFollowPattern") { ok "bazi.html has detectFollowPattern()" }
else { fail "bazi.html" "detectFollowPattern() not found" }
if (Has $html "detectDominantPattern") { ok "bazi.html has detectDominantPattern()" }
else { fail "bazi.html" "detectDominantPattern() not found" }
$hasFollowLogic = (Has $html "special:'follow'") -or (Has $html 'special:"follow"')
if ($hasFollowLogic) { ok "bazi.html has follow special pattern logic" }
else { fail "bazi.html" "follow special pattern logic not found" }
$hasDomLogic = (Has $html "special:'dominant'") -or (Has $html 'special:"dominant"')
if ($hasDomLogic) { ok "bazi.html has dominant special pattern logic" }
else { fail "bazi.html" "dominant special pattern logic not found" }

# ── 8. overview.md pages count = 29 ──────────────────────────────────────
$overview = Get-Content "$WIKI\overview.md" -Raw -Encoding UTF8
if ((Has $overview "pages: 31") -and (Has $overview "**Wiki pages:** 31")) {
    ok "overview.md pages count = 31 (frontmatter + body)"
} else {
    fail "overview.md pages count" "expected 'pages: 31' and '**Wiki pages:** 31'"
}

# ── 9. overview.md has bazisearch recent update entry ────────────────────
if ((Has $overview "bazisearch") -and (Has $overview "Classical Masters")) {
    ok "overview.md has bazisearch recent update"
} else {
    fail "overview.md recent update" "missing bazisearch / Classical Masters entry"
}

# ── 10. log.md has bazisearch ingest entry ────────────────────────────────
$log = Get-Content "$BASE\log.md" -Raw -Encoding UTF8
if (Has $log "ingest | bazisearch") { ok "log.md has bazisearch ingest entry" }
else { fail "log.md" "missing 'ingest | bazisearch' entry" }

# ── 11. Cross-links between entity pages ─────────────────────────────────
$xu   = if (Test-Path "$WIKI\entities\xu-ziping.md")    { Get-Content "$WIKI\entities\xu-ziping.md" -Raw -Encoding UTF8 } else { "" }
$shen = if (Test-Path "$WIKI\entities\shen-xiaozhan.md") { Get-Content "$WIKI\entities\shen-xiaozhan.md" -Raw -Encoding UTF8 } else { "" }
$ren  = if (Test-Path "$WIKI\entities\ren-tieqiao.md")   { Get-Content "$WIKI\entities\ren-tieqiao.md" -Raw -Encoding UTF8 } else { "" }

if (Has $xu   "Shen Xiaozhan") { ok "xu-ziping links to Shen Xiaozhan" }
else { fail "xu-ziping cross-link" "missing link to Shen Xiaozhan" }
if (Has $shen "Xu Ziping")     { ok "shen-xiaozhan links to Xu Ziping" }
else { fail "shen-xiaozhan cross-link" "missing link to Xu Ziping" }
if (Has $ren  "Shen Xiaozhan") { ok "ren-tieqiao links to Shen Xiaozhan" }
else { fail "ren-tieqiao cross-link" "missing link to Shen Xiaozhan" }

# ── 12. Pattern pages reference expected content ─────────────────────────
$pp = if (Test-Path "$WIKI\concepts\pattern-purity.md")          { Get-Content "$WIKI\concepts\pattern-purity.md" -Raw -Encoding UTF8 } else { "" }
$tp = if (Test-Path "$WIKI\concepts\transformation-patterns.md") { Get-Content "$WIKI\concepts\transformation-patterns.md" -Raw -Encoding UTF8 } else { "" }

if ((Has $pp "子平真诠") -or (Has $pp "ZPZQ")) { ok "pattern-purity references ZPZQ" }
else { fail "pattern-purity" "missing ZPZQ reference" }
if ((Has $tp "True vs False") -or (Has $tp "hua-ge") -or (Has $tp "True Transformation")) { ok "transformation-patterns has transformation content" }
else { fail "transformation-patterns" "missing True/False transformation content" }

# ── 13. bazi.html has TG_AFFECTIONS and SS_TIPS ───────────────────────────
$htmlPath = "$BASE\app\bazi.html"
if (Test-Path $htmlPath) {
    $html = Get-Content $htmlPath -Raw -Encoding UTF8
    if (Has $html "TG_AFFECTIONS") { ok "bazi.html contains TG_AFFECTIONS" }
    else { fail "bazi.html" "TG_AFFECTIONS not found" }
    if (Has $html "SS_TIPS") { ok "bazi.html contains SS_TIPS" }
    else { fail "bazi.html" "SS_TIPS not found" }
    $tgCount = ([regex]::Matches($html, "zh:'")).Count
    if ($tgCount -ge 11) { ok "bazi.html TG_AFFECTIONS has >= 11 entries (found $tgCount)" }
    else { fail "bazi.html TG_AFFECTIONS count" "expected >=11, found $tgCount" }
} else {
    fail "bazi.html" "file not found"
}

# ── 14. New interpretation constants exist ────────────────────────────────
$htmlPath2 = "$BASE\app\bazi.html"
if (Test-Path $htmlPath2) {
    $html2 = Get-Content $htmlPath2 -Raw -Encoding UTF8
    if (Has $html2 "UG_LIFE_GUIDANCE") { ok "bazi.html contains UG_LIFE_GUIDANCE" }
    else { fail "bazi.html" "UG_LIFE_GUIDANCE not found" }
    if (Has $html2 "LP_QUALITY_DESC") { ok "bazi.html contains LP_QUALITY_DESC" }
    else { fail "bazi.html" "LP_QUALITY_DESC not found" }
    if (Has $html2 "scoreAnnualYear") { ok "bazi.html contains scoreAnnualYear()" }
    else { fail "bazi.html" "scoreAnnualYear not found" }
    if (Has $html2 "getPurityExplanation") { ok "bazi.html contains getPurityExplanation()" }
    else { fail "bazi.html" "getPurityExplanation not found" }
} else {
    fail "bazi.html" "file not found (test 14)"
}

# ── Report ────────────────────────────────────────────────────────────────
$total = $PASS.Count + $FAIL.Count
Write-Host ""
Write-Host ("=" * 55)
Write-Host "  Bazi Wiki Tests: $($PASS.Count)/$total passed"
Write-Host ("=" * 55)
if ($FAIL.Count -gt 0) {
    Write-Host ""
    Write-Host "FAILED:"
    foreach ($f in $FAIL) { Write-Host "  x $f" }
}
Write-Host ""
Write-Host "PASSED:"
foreach ($p in $PASS) { Write-Host "  v $p" }
Write-Host ""
Write-Host ("=" * 55)
if ($FAIL.Count -gt 0) { exit 1 } else { exit 0 }
