---
name: preflight
description: >
  Environment check before Bazi MCP-dependent or tool-dependent work. Verifies Git,
  Node.js, `C:\Bazi\.mcp.json`, NotebookLM auth tooling, and Bazi repo status. Trigger
  on: /preflight, "check environment", "verify setup", "is everything installed".
---

# /preflight - Environment Preflight Check

Run before any Bazi session that depends on MCP servers, Node.js, or external tooling.

## Checks

### 1. Git

```bash
git --version
```

### 2. Node.js

```bash
node --version
```

### 3. `.mcp.json` Validity

```bash
python -c "import json; json.load(open(r'C:\Bazi\.mcp.json', encoding='utf-8')); print('OK')"
```

### 4. NotebookLM Auth Executable

```bash
find "$APPDATA/uv/tools/notebooklm-mcp-server/Scripts" -name "notebooklm-mcp-auth*" 2>/dev/null | head -1
```

### 5. NotebookLM MCP Live Test

Call `mcp__notebooklm-mcp__notebook_list`.

If auth fails, tell the user to run:

```bash
notebooklm-mcp-auth
```

Then stop MCP-dependent work until the user confirms re-auth or explicitly switches to
WebSearch-only mode.

### 6. Bazi Repo Status

```bash
git -C "C:/Bazi" status --short
git -C "C:/Bazi" rev-parse --abbrev-ref HEAD
git -C "C:/Bazi" log --oneline -1
```

### 7. Summary

Report Git, Node.js, `.mcp.json`, NotebookLM auth tooling, NLM MCP status, and the Bazi
branch/status.
