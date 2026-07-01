---
name: vscode
description: Interact with VS Code on the user's Windows machine — check running tasks and terminals, open files or folders, run/stop tasks, inspect workspace config (.vscode/tasks.json, launch.json, settings.json), and query child processes. Use this skill whenever the user asks what's running in VS Code, wants to open something in the editor, wants to trigger a task, or needs to inspect the VS Code workspace state. Always use this skill for VS Code-related requests even if the user only says "VS Code", "code", or "editor".
---

# VS Code Skill

Interact with VS Code via PowerShell + VS Code CLI in a code session. Keep every command targeted — never dump full process lists or large config files unless the user asks. Filter and summarize.

## Setup

Always run in a code session (`start_code_task`) at the relevant workspace path.  
VS Code CLI: `code` (on PATH). PowerShell: available in all code sessions.

---

## 1. Check VS Code Status

```powershell
# Is VS Code running?
Get-Process code -ErrorAction SilentlyContinue |
  Select-Object Id, CPU, @{n='Window';e={$_.MainWindowTitle}} |
  Format-Table -AutoSize
```

---

## 2. Find Running Tasks / Terminal Processes

VS Code tasks and integrated terminals run as child processes. Query them like this:

```powershell
# Get VS Code PIDs first
$vscodePids = (Get-Process code -ErrorAction SilentlyContinue).Id

# Find all child processes of VS Code
$children = Get-CimInstance Win32_Process |
  Where-Object { $vscodePids -contains $_.ParentProcessId } |
  Select-Object Name, ProcessId, CommandLine, @{n='CPU';e={$_.KernelModeTime}} |
  Sort-Object Name

$children | Format-Table Name, ProcessId, CommandLine -AutoSize -Wrap
```

**Filter for specific task runners** (more focused):
```powershell
Get-Process node,npm,tsc,webpack,python,dotnet,cargo,go,java,gradle,mvn `
  -ErrorAction SilentlyContinue |
  Select-Object Name, Id, CPU, StartTime |
  Format-Table -AutoSize
```

**Summarize** — when user just asks "task running?", return a short summary, not the full list.

---

## 3. Read Workspace Config

```powershell
# tasks.json — defined tasks
Get-Content ".vscode\tasks.json" -ErrorAction SilentlyContinue

# launch.json — debug configs  
Get-Content ".vscode\launch.json" -ErrorAction SilentlyContinue

# settings.json — workspace settings
Get-Content ".vscode\settings.json" -ErrorAction SilentlyContinue
```

Parse with ConvertFrom-Json for targeted queries:
```powershell
$tasks = Get-Content ".vscode\tasks.json" | ConvertFrom-Json
$tasks.tasks | Select-Object label, type, command | Format-Table -AutoSize
```

---

## 4. Open File or Folder in VS Code

```powershell
# Open file
code "C:\path\to\file.py"

# Open folder
code "C:\Vault\DepoMov"

# Open file at specific line
code --goto "C:\path\to\file.py:42"

# Diff two files
code --diff "file1.py" "file2.py"
```

---

## 5. VS Code CLI — Other Useful Commands

```powershell
# VS Code status (version, PID, logs path)
code --status

# List installed extensions
code --list-extensions

# Install extension
code --install-extension ms-python.python

# Open new window
code --new-window "C:\path"
```

---

## 6. Kill a Specific Task Process

```powershell
# Stop by name
Stop-Process -Name tsc -Force

# Stop by PID
Stop-Process -Id 12345 -Force
```

---

## Output Guidelines (token-saving)

- **Default**: return a short summary (3-5 lines) — process name, PID, status
- **On request**: return full details
- Never print raw JSON unless user asks; parse and format key fields only
- If nothing is running: say so in one line
- If VS Code is not open: say so, offer to open it

---

## Common Patterns

**"task running ใน VS Code?"**
→ Run #2 (child process query), summarize what's found

**"เปิดไฟล์ X ใน VS Code"**  
→ Run #4 (`code "path"`)

**"task ไหน define ไว้บ้าง?"**
→ Run #3 (read tasks.json, show label + command table)

**"run task X"**
→ `code --task` ไม่ support ใน CLI — ให้ตอบว่าต้องรันจาก terminal ใน VS Code หรือใช้ `node`/`npm` ตรงๆ แทน

**"VS Code version ?"**
→ `code --version`
