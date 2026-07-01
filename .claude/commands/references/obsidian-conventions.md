# Obsidian Conventions for Knowledge Bridge

## Frontmatter Schema

### Required Fields
```yaml
---
title: "Human-readable note title"
created: "2026-01-15"          # ISO date, not datetime
tags: [tag1, tag2]             # always an array
---
```

### Optional Fields
```yaml
---
source: NotebookLM | VSCode sync | manual | spec
project: project-name          # matches folder name
status: draft | active | archived
file_path: src/module/file.py  # for code-linked notes
last_synced: "2026-01-15"     # for auto-generated notes
---
```

## Folder Structure

```
vault/
└── Projects/
    └── {project-name}/
        ├── Project Overview.md
        ├── File Map.md
        ├── Open Questions.md
        ├── Dependency Graph.md
        ├── Research/
        │   └── {Topic from NotebookLM}.md
        ├── Specs/
        │   └── {Feature Name}.md
        ├── Modules/
        │   └── {Module Name}.md
        └── Daily/
            └── {YYYY-MM-DD}.md
```

## Tag Taxonomy

| Tag | Meaning |
|-----|---------|
| `#research` | Imported from NotebookLM or external source |
| `#spec` | Feature specification — intended to generate code |
| `#code` | Auto-generated from codebase scan |
| `#question` | Open question needing resolution |
| `#decision` | Architecture or design decision made |
| `#todo` | Action item |
| `#python` / `#typescript` / `#go` | Language tags |
| `#api` / `#ui` / `#db` / `#infra` | Domain tags |

## Wiki-Link Patterns

```markdown
Basic link:          [[Note Name]]
With display text:   [[Note Name|What to show]]
Link to heading:     [[Note Name#Section]]
Link to block:       [[Note Name#^block-id]]
```

**Rules:**
- Always use `[[wiki-links]]` for internal references, never `[markdown](links.md)`
- Note names are case-sensitive in Obsidian
- Use the full note title, not the file path

## Dataview Queries

Install the Dataview community plugin for dynamic views.

### All project notes
```dataview
TABLE source, status, file.ctime AS Created
FROM "Projects/my-project"
SORT file.ctime DESC
```

### All open questions
```dataview
LIST
FROM #question
WHERE !contains(tags, "resolved")
```

### Research notes linked to code
```dataview
TABLE file_path, last_synced
FROM "Projects/my-project/Research"
WHERE file_path != null
```

## Callout Syntax (for important blocks)

```markdown
> [!NOTE] Implementation Hint
> This note was generated from code — manual edits may be overwritten on next sync.

> [!WARNING] Pending Sync
> This spec has not yet been converted to code.

> [!TIP] NotebookLM Source
> Original research available at: {url or description}
```
