---
name: preflight
description: >
  Environment check before starting MCP-dependent or tool-dependent work. Verifies
  Git, Node.js, .mcp.json validity, and NotebookLM auth executable presence. Use at
  session start when about to do MCP setup, NotebookLM work, or notebook generation.
  Skip for git-only or firesearch-only sessions. Trigger on: /preflight,
  "check environment", "verify setup", "is everything installed".
---

# /preflight — Environment Preflight Check

Run before any session that depends on MCP servers, Node.js, or external tooling.
Skip if the session is git-only or wiki-editing-only.

---

## Checks

### 1. Git

```
git --version
```

Expected: `git version 2.x.x` or higher.
If missing: install from https://git-scm.com/download/win before proceeding.

### 2. Node.js

```
node --version
```

Expected: `v18.x` or higher (required for npx-based MCP servers).
If missing: install from https://nodejs.org/en/download before proceeding.

### 3. .mcp.json validity

```
python -c "import json; json.load(open('C:\\Vault\\.mcp.json')); print('OK')"
```

Expected: `OK`
If error: fix the JSON before registering any MCP server. Common issue: missing `mcpServers` wrapper key.

### 4. NotebookLM auth executable

```bash
NLM_AUTH=$(find "$APPDATA/uv/tools/notebooklm-mcp-server/Scripts" -name "notebooklm-mcp-auth*" 2>/dev/null | head -1)
```

Expected: a non-empty path.
If empty: the NLM MCP package is not installed. Run:
```
uv tool install notebooklm-mcp-server
```

### 5. NotebookLM MCP live test (self-healing)

Call `mcp__notebooklm-mcp__notebook_list` (lightweight — lists notebooks without modifying anything).

- **If it responds:** NLM MCP is connected and authenticated — continue to Step 6.
- **If it returns an auth error or times out:** attempt auto-auth before escalating:

  **Auto-auth attempt 1/2:**
  Print: `NLM auth expired — attempting auto-auth (1/2)…`
  Run `notebooklm-mcp-auth` via Bash tool.
  Retry `mcp__notebooklm-mcp__notebook_list`.

  **If retry succeeds:** print `✓ NLM auto-auth succeeded` and continue.

  **Auto-auth attempt 2/2 (if first retry still fails):**
  Print: `NLM auth still failing — attempting auto-auth (2/2)…`
  Run `notebooklm-mcp-auth` again.
  Retry `mcp__notebooklm-mcp__notebook_list`.

  **If second retry succeeds:** print `✓ NLM auto-auth succeeded` and continue.

  **If both retries fail:** **STOP**. Print exactly:
  ```
  NLM auto-auth failed after 2 attempts.
  Run `notebooklm-mcp-auth` in your terminal, then re-run /preflight.
  Do NOT proceed with MCP-dependent work until /preflight shows ✓ NLM.
  ```
  Do not read `index.md`. Do not start any task. Wait for the user to re-authenticate and re-run `/preflight`. If the user explicitly opts for WebSearch-only mode, note it and proceed without NLM.

- Never assume MCP is live based on the auth exe existing — always confirm with a live call

### 6. Dynamic Subvault Discovery

Discover all git repos under the vault — never use a hardcoded list:

```bash
find /c/Vault -maxdepth 3 -name ".git" -type d | sed 's|/.git$||' | sort
```

For each repo found, check status:

```bash
git -C "<repo_path>" status --short
git -C "<repo_path>" log --oneline -1
```

Report the full repo list with branch and whether each has uncommitted changes. This catches any new subvaults added since the last session.

### 7. Summary

Print a checklist:

```
Git          ✓  v2.47.0
Node.js      ✓  v20.11.0
.mcp.json    ✓  valid JSON
NLM auth exe ✓  found
NLM MCP      ✓  connected (N notebooks)

Ready to proceed.
```

Or if MCP is down:

```
NLM MCP      ✗  auth expired — run: notebooklm-mcp-auth
             →  session mode: WebSearch-only
```

If any item is missing, list install steps and stop — do not proceed until fixed.

---

## Usage

```
/preflight
```

Run at the start of any session involving MCP servers, NotebookLM, or Node.js tooling.
