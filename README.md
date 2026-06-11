# Markdown Session Scaffold

This workspace includes a ready-made Markdown session scaffold under `./.md-session` with templates, a live-preview script, and recommended VS Code settings.

Quick start (PowerShell):

```powershell
# Run the start script (uses Node npx live-server if available, otherwise Python livereload)
.\.md-session\scripts\start-md-session.ps1
```

Templates:

- `.md-session/templates/note.md` — general note template
- `.md-session/templates/project.md` — project template
- `.md-session/templates/meeting.md` — meeting notes template

VS Code: open workspace and install recommended extensions from the Extensions view if prompted.

If using Python preview server manually:

```powershell
python -m pip install --user livereload
python .\.md-session\scripts\preview_server.py
```
