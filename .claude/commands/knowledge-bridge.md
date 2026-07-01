---
name: knowledge-bridge
description: >
  Orchestrates a 4-tool knowledge-to-code pipeline connecting NotebookLM, Obsidian, VSCode,
  and Claude Code into a unified research-development workflow. Use this skill whenever
  the user wants to: bridge research notes with their codebase, convert NotebookLM exports
  or summaries into Obsidian notes, generate code scaffolds from Obsidian spec notes,
  sync VSCode project structure into an Obsidian knowledge graph, or run any workflow
  that spans research → notes → code. Trigger on phrases like "sync my notes with my code",
  "create Obsidian notes from my research", "generate code from my spec notes",
  "document my project in Obsidian", "import NotebookLM to Obsidian", "link my vault
  to my project", "knowledge-to-code", "note-driven development", or any mention of
  combining two or more of: NotebookLM, Obsidian, VSCode, Claude Code.
compatibility:
  required_tools: [Read, Write, Bash, Glob, Grep]
  optional_tools: [WebFetch]
  environment: Claude Code (terminal)
  os: macOS, Linux, Windows (WSL)
---

# Knowledge Bridge

A skill that connects **NotebookLM** (research) → **Obsidian** (knowledge graph) →
**VSCode** (code editor) → **Claude Code** (AI agent) into one fluid workflow.

---

## Mental Model

```
NotebookLM                Obsidian Vault              VSCode Project
 (Research)  ──export──▶  (Knowledge Hub)  ──spec──▶  (Codebase)
                               ▲                           │
                               └────── Claude Code ────────┘
                                     (this skill)
                               (sync, generate, link)
```

- **NotebookLM** = source of truth for research, PDFs, papers, transcripts
- **Obsidian** = the connective tissue — markdown vault linking ideas to code
- **VSCode** = where code actually lives; workspace files, tasks, extensions
- **Claude Code** = the agent doing the bridging (that's you, reading this skill)

---

## Step 0 — Orient Yourself

Before doing anything, identify:

1. **Obsidian vault path** — ask the user if unknown; typically `~/Documents/Obsidian/VaultName` or `~/vault`
2. **VSCode project path** — the repo root (look for `.git`, `package.json`, `pyproject.toml`, etc.)
3. **Which workflow** the user wants (see §Workflows below)

```bash
# Quick orientation commands
ls ~/Documents/Obsidian/          # find vaults
ls ~/vault/ 2>/dev/null           # alt location
code --list-extensions 2>/dev/null # check VSCode extensions
find . -name ".git" -maxdepth 2   # find git roots nearby
```

Store confirmed paths in a local `.knowledge-bridge.json` in the project root for future sessions:
```json
{
  "vault_path": "/Users/you/Documents/Obsidian/MyVault",
  "project_path": "/Users/you/projects/my-app",
  "bridge_folder": "Projects/my-app",
  "last_sync": "2026-01-01T00:00:00Z"
}
```

---

## Workflows

There are **five core workflows**. Read the right section based on the user's intent.

---

### Workflow 1 — NotebookLM → Obsidian Import

**When**: User has copied/exported text from NotebookLM and wants it as structured Obsidian notes.

**NotebookLM has no public API** — content must arrive via:
- Clipboard paste (most common: user pastes NotebookLM summary/outline into the prompt)
- Exported `.txt` or `.md` file from NotebookLM's share feature
- Saved audio overview transcript

#### Steps

1. **Receive the content** — ask user to paste or provide the file path
2. **Parse the structure** — detect headings, key points, source citations
3. **Create Obsidian notes** following the conventions in `references/obsidian-conventions.md`
4. **Write files** to `{vault_path}/{bridge_folder}/Research/`
5. **Create an index note** linking all generated notes

#### Note Structure for Research Content

```markdown
---
title: "{Detected Title}"
created: {ISO date}
source: NotebookLM
tags: [research, {auto-detected topic tags}]
project: {project name if detectable}
---

# {Title}

## Summary
{2-3 sentence distillation}

## Key Points
- {point 1}
- {point 2}

## Questions & Gaps
- {open questions to explore in code or further research}

## Related
- [[{related note 1}]]
- [[{related note 2}]]

## Source Material
{preserve any citations or source references verbatim}
```

---

### Workflow 2 — VSCode Project → Obsidian Knowledge Graph

**When**: User wants their codebase documented and mapped inside Obsidian.

#### Steps

1. **Scan the project structure**:
```bash
# Get project tree (respects .gitignore)
find {project_path} \
  -not -path '*/.git/*' \
  -not -path '*/node_modules/*' \
  -not -path '*/__pycache__/*' \
  -not -path '*/dist/*' \
  -not -path '*/.next/*' \
  | sort | head -200
```

2. **Identify key artifacts**: entry points, config files, main modules, tests, docs

3. **Generate these Obsidian notes**:

| Note | Location | Content |
|------|----------|---------|
| `Project Overview` | `{bridge_folder}/` | Architecture, purpose, stack |
| `File Map` | `{bridge_folder}/` | Directory tree with descriptions |
| One note per module/package | `{bridge_folder}/Modules/` | Purpose, exports, dependencies |
| `Open Questions` | `{bridge_folder}/` | TODOs, FIXMEs, design decisions |
| `Dependency Graph` | `{bridge_folder}/` | Key libraries and their roles |

4. **Module Note Template**:
```markdown
---
title: "{Module Name}"
created: {date}
source: VSCode sync
tags: [code, {language}, {module-type}]
file_path: {relative path in project}
---

# {Module Name}

## Purpose
{one-line description inferred from code}

## Exports / Public API
{list of exported functions/classes/constants}

## Dependencies
- [[{internal module}]]
- `{external package}` — {what it's used for}

## Design Notes
{any patterns, architecture decisions Claude can infer}

## TODOs
{extracted from // TODO, # TODO, FIXME comments}

## Code Snippet
\`\`\`{language}
{representative snippet — entry point, main class, etc.}
\`\`\`
```

5. **Create a Dataview-compatible index** if the user has the Dataview plugin:
```markdown
\`\`\`dataview
TABLE file.ctime AS Created, tags
FROM "Projects/{project-name}"
SORT file.ctime DESC
\`\`\`
```

---

### Workflow 3 — Obsidian Spec Note → VSCode Code

**When**: User has written a specification, feature plan, or design note in Obsidian and wants Claude Code to generate code from it.

#### Steps

1. **Read the spec note** — get the path from the user, then:
```bash
cat "{vault_path}/{note_path}.md"
```

2. **Parse the spec** looking for:
   - Functional requirements (what it should do)
   - Data models / schemas
   - API endpoints or function signatures
   - Edge cases and constraints
   - Tech stack preferences (tags like `#python`, `#typescript`)

3. **Scaffold code** in the VSCode project:
   - Create files in appropriate locations
   - Write stub implementations with docstrings referencing the spec note
   - Generate tests stubs for each requirement
   - Add a header comment with the Obsidian note path for traceability

4. **Header convention** (add to every generated file):
```python
# Generated from Obsidian spec: {note_relative_path}
# Last synced: {date}
# To regenerate: claude "sync spec {note_name}" in project root
```

5. **Update the spec note** with links to generated files:
```markdown
## Implementation
- `{relative_file_path}` — {what was generated}
- Status: 🟡 Scaffolded / 🟢 Complete / 🔴 Failing tests
```

---

### Workflow 4 — Bidirectional Sync (Keep Everything Up to Date)

**When**: User wants ongoing synchronization — code changes reflected in Obsidian, new research reflected as code tasks.

#### Setup a Sync Script

Generate `{project_path}/.claude/sync-vault.sh`:
```bash
#!/bin/bash
# Knowledge Bridge — Vault Sync
# Run: bash .claude/sync-vault.sh [--full | --notes | --code]

VAULT="{vault_path}"
PROJECT="{project_path}"
BRIDGE_FOLDER="Projects/{project_name}"
MODE="${1:---full}"

echo "Knowledge Bridge Sync — $(date)"

if [[ "$MODE" == "--full" || "$MODE" == "--code" ]]; then
  echo "Scanning project changes..."
  claude "Run knowledge-bridge workflow 2 using project at $PROJECT and vault at $VAULT"
fi

if [[ "$MODE" == "--full" || "$MODE" == "--notes" ]]; then
  echo "Checking for new spec notes..."
  find "$VAULT/$BRIDGE_FOLDER/Specs" -name "*.md" -newer "$PROJECT/.knowledge-bridge.json" 2>/dev/null
fi

echo "Sync complete"
```

#### Setup VSCode Task

Generate or append to `{project_path}/.vscode/tasks.json`:
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Sync Knowledge Vault",
      "type": "shell",
      "command": "bash .claude/sync-vault.sh",
      "group": "build",
      "presentation": {
        "reveal": "always",
        "panel": "new"
      },
      "problemMatcher": []
    },
    {
      "label": "Open Project Vault",
      "type": "shell",
      "command": "open 'obsidian://open?vault={vault_name}&file=Projects/{project_name}/Project Overview'",
      "group": "build",
      "presentation": { "reveal": "silent" }
    },
    {
      "label": "Import NotebookLM Export",
      "type": "shell",
      "command": "claude 'Run knowledge-bridge workflow 1 — import notebooklm file at ${input:notebooklmFile}'",
      "group": "build",
      "inputs": [
        {
          "id": "notebooklmFile",
          "description": "Path to NotebookLM export file",
          "type": "promptString"
        }
      ]
    }
  ]
}
```

---

### Workflow 5 — Full Project Initialization

**When**: User is starting fresh and wants everything set up at once.

#### Steps (in order)

1. Confirm `vault_path` and `project_path`
2. Create vault folder structure:
```
{vault_path}/Projects/{project_name}/
├── Project Overview.md       ← auto-generated
├── File Map.md               ← auto-generated
├── Open Questions.md         ← auto-generated
├── Dependency Graph.md       ← auto-generated
├── Research/                 ← for NotebookLM imports
├── Specs/                    ← for feature specs → code
├── Modules/                  ← one note per code module
└── Daily/                    ← optional: daily dev logs
```
3. Run Workflow 2 (project scan → Obsidian)
4. Create `.claude/sync-vault.sh`
5. Create/update `.vscode/tasks.json`
6. Write `.knowledge-bridge.json` config
7. Add `.knowledge-bridge.json` to `.gitignore` (it's machine-specific)
8. Print a summary of what was created

The `setup_vault.py` script in `references/setup_vault.py` can automate step 2.
The `sync_codebase.py` script in `references/sync_codebase.py` handles project scanning for step 3.

---

## Obsidian Conventions

Read `references/obsidian-conventions.md` for:
- Frontmatter schema (required fields, optional fields)
- Folder naming rules
- Tag taxonomy (`#research`, `#spec`, `#code`, `#question`, `#decision`)
- Wiki-link patterns (`[[Note Name]]`, `[[Note Name|Display Text]]`)
- Dataview queries for cross-project views

---

## VSCode Integration Details

Read `references/vscode-integration.md` for:
- Recommended extensions list (Obsidian-compatible markdown preview, etc.)
- `settings.json` tweaks for markdown files
- Keyboard shortcut suggestions
- How to use the Obsidian URI scheme (`obsidian://`) from the terminal

---

## NotebookLM Tips

Since NotebookLM has no API, teach the user these export methods when relevant:

| Method | How | Best for |
|--------|-----|---------|
| Copy summary | Select all text in NotebookLM summary panel, Cmd+C | Quick research notes |
| Share → Copy link | Notebook → Share → Copy (if available) | Referencing source |
| Audio overview transcript | Generate audio → copy transcript text | Long-form research |
| Export to Google Doc | Share menu → Google Docs | Structured documents |

For Google Docs exports: once in Google Docs, user can download as `.md` (File → Download → Markdown) and pass the file to this skill.

---

## Error Handling

| Problem | Resolution |
|---------|-----------|
| Vault path not found | Ask user to confirm path; check `~/Documents/Obsidian/` and `~/vault/` |
| VSCode not installed | Skill still works — just skip tasks.json generation |
| `obsidian://` URI not working | Obsidian must be installed; on Linux use `xdg-open` |
| Note already exists | Always ask before overwriting; offer to append/merge instead |
| Large project (1000+ files) | Limit scan depth; focus on entry points and top-level modules first |
| Binary/minified files | Skip automatically; never try to read `node_modules`, `dist`, `.pyc` |

---

## Output Checklist

After completing any workflow, confirm:

- [ ] Obsidian notes written to correct vault folder
- [ ] All notes have valid frontmatter (title, created, tags)
- [ ] Wiki-links use `[[double brackets]]` not markdown links
- [ ] VSCode files (tasks.json, etc.) are valid JSON
- [ ] `.knowledge-bridge.json` is updated with `last_sync`
- [ ] User knows where to find new files (print full paths)
- [ ] No files were overwritten without confirmation
