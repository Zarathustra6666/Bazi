# VSCode Integration Reference

## Recommended Extensions

Suggest these to the user when running Workflow 5 (full init):

| Extension ID | Purpose |
|-------------|---------|
| `foam.foam-vscode` | Foam — Obsidian-like wiki links inside VSCode |
| `yzhang.markdown-all-in-one` | Markdown preview, TOC, shortcuts |
| `bierner.markdown-preview-github-styles` | GitHub-style markdown rendering |
| `eamodio.gitlens` | Blame/history — helps link commits to Obsidian decisions |
| `ms-python.python` / `dbaeumer.vscode-eslint` | Language-specific (add as relevant) |

Install via terminal:
```bash
code --install-extension foam.foam-vscode
code --install-extension yzhang.markdown-all-in-one
```

## settings.json Additions

Append to `.vscode/settings.json` (create if missing):
```json
{
  "markdown.preview.openMarkdownLinks": "inPreview",
  "editor.wordWrap": "on",
  "[markdown]": {
    "editor.defaultFormatter": "yzhang.markdown-all-in-one",
    "editor.formatOnSave": false
  },
  "foam.openDailyNote.directory": "${workspaceFolder}/.notes/daily",
  "files.associations": {
    "*.md": "markdown"
  },
  "search.exclude": {
    "**/node_modules": true,
    "**/.git": true
  }
}
```

## tasks.json Full Template

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Sync Knowledge Vault",
      "type": "shell",
      "command": "bash .claude/sync-vault.sh",
      "group": "build",
      "presentation": { "reveal": "always", "panel": "new" },
      "problemMatcher": []
    },
    {
      "label": "Open Project in Obsidian",
      "type": "shell",
      "command": "open 'obsidian://open?vault=${input:vaultName}&file=Projects/${input:projectName}/Project Overview'",
      "group": "build",
      "presentation": { "reveal": "silent" },
      "inputs": [
        { "id": "vaultName", "description": "Obsidian vault name", "type": "promptString" },
        { "id": "projectName", "description": "Project folder name", "type": "promptString" }
      ]
    },
    {
      "label": "Import NotebookLM Export",
      "type": "shell",
      "command": "claude 'knowledge-bridge: import notebooklm file at ${input:notebooklmFile}'",
      "group": "build",
      "inputs": [
        { "id": "notebooklmFile", "description": "Path to NotebookLM .md or .txt export", "type": "promptString" }
      ]
    },
    {
      "label": "Generate Code from Spec Note",
      "type": "shell",
      "command": "claude 'knowledge-bridge: generate code from Obsidian spec at ${input:specNote}'",
      "group": "build",
      "inputs": [
        { "id": "specNote", "description": "Obsidian spec note path (relative to vault)", "type": "promptString" }
      ]
    },
    {
      "label": "Rebuild File Map",
      "type": "shell",
      "command": "claude 'knowledge-bridge: update file map note for this project'",
      "group": "build",
      "presentation": { "reveal": "always", "panel": "shared" },
      "problemMatcher": []
    }
  ]
}
```

## Keyboard Shortcuts (keybindings.json)

Optional — suggest to user who wants rapid switching:
```json
[
  {
    "key": "ctrl+shift+o",
    "command": "workbench.action.tasks.runTask",
    "args": "Open Project in Obsidian"
  },
  {
    "key": "ctrl+shift+k",
    "command": "workbench.action.tasks.runTask",
    "args": "Sync Knowledge Vault"
  }
]
```

## Obsidian URI Scheme

Use these URIs to deep-link from VSCode tasks into Obsidian:

```
# Open vault
obsidian://open?vault={vault-name}

# Open specific note
obsidian://open?vault={vault-name}&file={note-path}

# Open and create new note
obsidian://new?vault={vault-name}&file={path}&content={url-encoded-content}

# Search inside vault
obsidian://search?vault={vault-name}&query={query}
```

**Platform notes:**
- **macOS**: `open "obsidian://..."` works natively
- **Linux**: `xdg-open "obsidian://..."` (requires Obsidian AppImage registered)
- **Windows**: `Start-Process "obsidian://..."` in PowerShell

## .gitignore Additions

Add to project `.gitignore`:
```gitignore
# Knowledge Bridge
.knowledge-bridge.json     # machine-specific paths
.claude/sync-vault.sh      # optional — contains vault paths
```
