---
name: "source-command-preflight"
description: "Environment check before starting MCP-dependent or tool-dependent work. Verifies Git, Node.js, .mcp.json validity, and NotebookLM auth executable presence. Use at session start when about to do MCP setup, NotebookLM work, or notebook generation. Skip for git-only or firesearch-only sessions. Trigger on: /preflight, \"check environment\", \"verify setup\", \"is everything installed\"."
---

# source-command-preflight

Use this skill when the user asks to run the migrated source command `preflight`.

## Command Template

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

```
Test-Path "C:\Users\FIAD_\AppData\Roaming\uv\tools\notebooklm-mcp-server\Scripts\notebooklm-mcp-auth.exe"
```

Expected: `True`
If `False`: the NLM MCP package is not installed. Run:
```
uv tool install notebooklm-mcp-server
```

### 5. NotebookLM MCP live test

Call `mcp__notebooklm-mcp__notebook_list` (lightweight — lists notebooks without modifying anything).

- If it responds: NLM MCP is connected and authenticated
- If it returns an auth error or times out: instruct the user to run `notebooklm-mcp-auth` in their terminal, then set session mode to WebSearch-only and note it in the preflight summary
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
