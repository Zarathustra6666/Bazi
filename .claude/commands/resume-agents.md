---
name: resume-agents
description: >
  Resumes interrupted research subagents by reading the agent journal, re-dispatching
  each interrupted task (up to 3 at a time), and falling back to direct WebSearch if
  re-dispatch fails. Trigger on: /resume-agents, "resume agents", "continue interrupted research".
---

# /resume-agents — Resume Interrupted Research Agents

Re-dispatches agents that were interrupted by usage limits or auth failures. Reads
`C:\Vault\tools\agent_journal.json` to find interrupted tasks and re-runs them.

---

## Steps

### 1. Check journal for interrupted agents

```bash
python C:/Vault/tools/agent_journal.py interrupted
```

- If output is "No interrupted agents." — report this and exit. Nothing to do.
- If interrupted agents exist — proceed to step 2.

### 2. Re-dispatch each interrupted agent (up to 3 at a time)

For each interrupted agent (process in batches of 3 if more exist):

**Determine channel:**
- If `attempts >= 2` and channel is `nlm`: switch channel to `websearch`
- Otherwise use the channel from the journal entry

**Mark as running:**
```bash
python C:/Vault/tools/agent_journal.py update <task_id> running
```

**Spawn subagent** with this prompt (fill in `[topic]`, `[channel]`, `[attempt_number]`):
```
Resume research for topic: [topic]
Channel: [channel] (WebSearch only if channel=websearch; NotebookLM if channel=nlm)
Attempt: [attempt_number]

Research [topic] and write or update the wiki page at C:\Bazi\wiki\[relevant-path]\[slug].md.
Add at minimum: 3 content bullets, 1 WikiLink to a related page, correct YAML frontmatter.
Return a one-line result: "done — [topic]: N facts added" or "failed — [reason]".
```

### 3. Collect results

For each subagent response:

**On success** (returns "done — ...")):
```bash
python C:/Vault/tools/agent_journal.py update <task_id> done "<result line>"
```

**On failure** (returns "failed — ..." or no output):
- If `channel == nlm`: switch to websearch and retry directly in the main session
- If `channel == websearch` or attempt >= 3: mark as failed
  ```bash
  python C:/Vault/tools/agent_journal.py update <task_id> failed "<reason>"
  ```
- Log the topic as needing manual research

### 4. Update research orchestrator

For each successfully completed topic, sync status to the research ledger:

```bash
python C:/Vault/tools/research_orchestrator.py mark "<topic>" done
```

### 5. Cleanup and report

If all tasks are done or failed:
```bash
python C:/Vault/tools/agent_journal.py clear-done
```

Print summary:
```
Resume complete:
  Re-dispatched: N agents
  Succeeded:     N
  Failed:        N (manual follow-up needed)
  NLM->WebSearch fallbacks: N

Failed topics (research manually):
  - [topic]
```

---

## Fallback Rules

| Condition | Action |
|-----------|--------|
| Subagent returns no output | Fall back to direct WebSearch in main session |
| `channel=nlm` and attempt >= 2 | Switch to `channel=websearch` automatically |
| `channel=websearch` and attempt >= 2 | Mark failed; surface to user |
| NLM auth expired during re-dispatch | Switch all remaining tasks to websearch |

---

## Usage

```
/resume-agents
```

Run after hitting a usage limit mid-research, or after an NLM auth interruption.
The journal persists across sessions — interrupted tasks from yesterday are still resumable today.

Note: `agent_journal.json` lives at the shared `C:\Vault\tools\` location and is not
per-repo — interrupted tasks from any vault (Bazi, Vault, etc.) appear in the same
journal. The `[relevant-path]` in the resume prompt is filled in per-task based on
which vault the original task targeted.
