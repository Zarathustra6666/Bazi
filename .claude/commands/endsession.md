---
name: endsession
description: >
  End-of-session cleanup: lint wiki, fix all issues, resolve conflicts, commit and push
  all affected repos. Run at the end of any session that produced wiki or file changes.
  Trigger on: /endsession, "end session", "wrap up", "finish session", "close session".
---

# /endsession — End-of-Session Cleanup & Sync

> **Pre-flight (Remote):** Call ToolSearch once before starting: `select:mcp__notebooklm-mcp__notebook_list`
> Skip if these tools were already loaded earlier in this session.

Run this at the end of any session that produced wiki edits, new pages, or code changes.

---

## Steps

### 0. Auth & Connectivity Check

Before running anything else, verify:

```bash
# Git remote reachable?
git -C "C:/Vault" ls-remote --exit-code origin HEAD && echo "Git OK" || echo "Git: cannot reach remote"
```

And call `mcp__notebooklm-mcp__notebook_list` (lightweight). If it returns an auth error, note it and set session to WebSearch-only — do not block the cleanup.

Report:
```
Git remote   ✓ / ✗
NLM MCP      ✓ connected (N notebooks) / ✗ auth expired (WebSearch-only mode)
```

Proceed regardless — auth failures should not block lint, commit, or push.

### 1. Wiki Lint

Run the lint check on C:\Vault\Wiki (broken WikiLinks, orphans, frontmatter completeness):

```powershell
# Check for broken WikiLinks in index.md, plus orphan pages with zero inbound links
$wikiFiles = Get-ChildItem "C:\Vault\Wiki" -Recurse -Filter "*.md" | Where-Object { $_.Name -ne "README.md" }
$titleSet = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::Ordinal)
$stemSet  = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
$titleByFile = @{}
foreach ($f in $wikiFiles) {
    $null = $stemSet.Add($f.BaseName)
    $lines = Get-Content $f.FullName -TotalCount 20 -Encoding UTF8 -ErrorAction SilentlyContinue
    foreach ($line in $lines) {
        if ($line -match '^title:\s*["'']?(.+?)["'']?\s*$') { $t = $Matches[1].Trim(); $null = $titleSet.Add($t); $titleByFile[$f.FullName] = $t }
        if ($line -match '^aliases:\s*\[(.+)\]\s*$') {
            [regex]::Matches($Matches[1], '"([^"]+)"') | ForEach-Object { $null = $titleSet.Add($_.Groups[1].Value.Trim()) }
        }
    }
}

# Broken links: every [[link]] anywhere in Wiki/ + index.md must resolve to a title or stem
$allMd = @($wikiFiles) + (Get-Item "C:\Vault\index.md")
$allText = ($allMd | ForEach-Object { Get-Content $_.FullName -Encoding UTF8 -Raw -ErrorAction SilentlyContinue }) -join "`n"
$links = [regex]::Matches($allText, '\[\[([^\]\|#]+)') | ForEach-Object { $_.Groups[1].Value.Trim() } | Sort-Object -Unique
$broken = $links | Where-Object { -not $titleSet.Contains($_) -and -not $stemSet.Contains($_) }

# Orphan pages: every Wiki/ page must be referenced (by title or stem) by at least one other page or index.md
$referenced = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
foreach ($l in $links) { $null = $referenced.Add($l) }
$orphans = $wikiFiles | Where-Object {
    $t = $titleByFile[$_.FullName]
    -not $referenced.Contains($_.BaseName) -and ($null -eq $t -or -not $referenced.Contains($t))
}

"Broken: $($broken.Count) | Orphans: $($orphans.Count) | Resolved: $(($links.Count) - $broken.Count)"
$broken | ForEach-Object { "  BROKEN: [[$_]]" }
$orphans | ForEach-Object { "  ORPHAN: $($_.FullName)" }
```

Fix all broken links and orphan pages found (update file titles/index links to match; add an inbound link from the most relevant concept/entity page or from `index.md` for orphans with no obvious home).

### 2. Session Checkpoint Cleanup

If `C:\Vault\session-checkpoint.md` exists and the task is fully done, delete it:

```powershell
if (Test-Path "C:\Vault\session-checkpoint.md") {
    Remove-Item "C:\Vault\session-checkpoint.md"
    Write-Host "Checkpoint deleted."
}
```

### 3. Research Ledger Check

Check for unfinished research tasks:

```powershell
python C:\Vault\tools\research_orchestrator.py check
```

If any tasks are unfinished, report them to the user before proceeding.

### 4. Discover All Repos

Never hardcode the repo list, and never reuse a list remembered from a prior session — re-run this discovery fresh every time (a previous session omitted the `md` Vault by trusting a stale list; see CLAUDE.md "Vault Structure"):

```bash
find /c/Vault -maxdepth 3 -name ".git" -type d | sed 's|/.git$||'
```

Report all found repos.

### 5. Commit and Push Each Repo

For each repo found in step 4 that has changes:

```bash
git -C "<repo_path>" status --short
git -C "<repo_path>" add <specific changed files — never -A blindly>
git -C "<repo_path>" commit -m "<descriptive message of what changed>"
dirty=$(git -C "<repo_path>" diff --name-only)
if [ -n "$dirty" ]; then git -C "<repo_path>" stash; fi
git -C "<repo_path>" pull --rebase origin <branch>
git -C "<repo_path>" push origin <branch>
if [ -n "$dirty" ]; then git -C "<repo_path>" stash pop; fi
git -C "<repo_path>" log --oneline -3
```

**Error handling (per repo):** If any git operation fails for a repo (network error, permission denied, bad state, unexpected output), log `✗ <repo_path> — <reason>`, skip that repo immediately, and continue with the next. One failed repo must never abort the full sync. Surface all failures in the summary report.

If `pull --rebase` fails with a conflict: **stop**, show the conflict files, and ask "take ours / take theirs / manual?" before resolving.

### 6. Summary Report

```
=== End-of-Session Summary ===

Wiki Lint:    ✓ 0 broken links
Checkpoint:   ✓ deleted / ✗ not found
Ledger:       ✓ all tasks done / ⚠ N unfinished

Repos pushed:
  C:\Vault          ✓  master  (N files changed)
  C:\Bazi           ✓  master  (N files changed)
  C:\Vault\md       —  master  (no changes, skipped)
  C:\Vault\Z        ✗  master  FAILED: <reason>
  [others...]       ✓  master  (N files changed)
```

---

## Usage

```
/endsession
```
