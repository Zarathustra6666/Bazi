# /usage-plan — Quota-Aware Job Planner

Measures remaining weekly quota + 5-hour window, then outputs a time-boxed job schedule that fits both caps and maximises throughput.

**Trigger:** `/usage-plan`, `/usage-plan --jobs job1,job2`, `/usage-plan --manual <pct_used> <reset_iso>`

**Known limitations:**
- Cost weights in `usage_planner_config.yaml` are estimates -- tune after observing real cutoffs
- 5-hour window is inferred from session start time, not queried directly
- Browser scraping may break if claude.ai updates its UI -- use `--manual` as fallback
- Usage % from claude.ai may lag a few minutes behind actual

---

## Pre-flight

Load browser tools in ONE ToolSearch call:

```
ToolSearch: select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__javascript_tool,mcp__claude-in-chrome__tabs_close_mcp
```

Also verify PyYAML is available:
```bash
python -c "import yaml; print('ok')"
```
If missing: `pip install pyyaml` and continue.

---

## Steps

### Step 1 -- Track session start

Run:
```bash
python C:/Vault/tools/usage_planner.py status
```
This initialises `~/.claude/usage_session.json` if absent or stale (>5h old).
Print the one-line banner it outputs.

---

### Step 2 -- Scrape usage from claude.ai

**If `--manual <pct_used> <reset_iso>` was passed:** skip to Step 3 with those values.

Otherwise:

1. Call `mcp__claude-in-chrome__tabs_context_mcp` -- note existing tabs, do not disturb them.
2. Call `mcp__claude-in-chrome__tabs_create_mcp` -- open a new tab.
3. Navigate to `https://claude.ai/settings` and wait for load.
4. Run this JS to extract usage data:

```javascript
(function() {
  // Strategy 1: progress bar with aria attributes
  const bar = document.querySelector('[role="progressbar"]');
  if (bar) {
    const val = bar.getAttribute('aria-valuenow') || bar.getAttribute('aria-valuetext');
    if (val) return JSON.stringify({ method: 'aria', raw: val });
  }

  // Strategy 2: scan all text nodes for "X%" near usage/limit/quota keywords
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const hits = [];
  let node;
  while ((node = walker.nextNode())) {
    const t = node.textContent.trim();
    if (/\d+\s*%/.test(t)) {
      const parent = node.parentElement;
      const ctx = (parent?.closest('[class]')?.className || '') + (parent?.textContent || '');
      if (/usage|limit|quota|message|token/i.test(ctx)) {
        hits.push({ text: t, ctx: ctx.slice(0, 120) });
      }
    }
  }

  // Strategy 3: look for reset date text
  const resetEl = [...document.querySelectorAll('*')].find(el =>
    el.children.length === 0 && /resets?\s+(on|in|at)/i.test(el.textContent)
  );
  const resetText = resetEl?.textContent?.trim() || null;

  return JSON.stringify({ method: 'scan', hits: hits.slice(0, 5), resetText });
})()
```

5. Parse the JS result:
   - If `method: aria` with a numeric value: that is `weekly_pct_used`
   - If `method: scan`: read `hits` -- the first hit with a clear percentage is `weekly_pct_used`; `resetText` gives the reset date
   - If extraction fails or is ambiguous: ask the user to provide the values manually:
     > "Could not read usage automatically. Please check claude.ai/settings and tell me: what % is the usage bar at, and what date does it reset?"
     Then proceed with the user-supplied values.

6. Write to `~/.claude/usage_cache.json`:
```json
{
  "weekly_pct_used": <number 0-100>,
  "reset_iso": "<ISO 8601 datetime>",
  "scraped_at": "<now ISO>"
}
```

7. Close the tab with `mcp__claude-in-chrome__tabs_close_mcp`.

**Reset date parsing:**
- If the page shows "Resets July 8" or "Resets on Tue Jul 8": convert to ISO using today's year and UTC midnight
- If it shows a countdown like "Resets in 3 days": add 3 days to today
- If ambiguous: ask the user

---

### Step 3 -- Compute schedule

Build the command:
```bash
python C:/Vault/tools/usage_planner.py plan <weekly_pct_used> <reset_iso> [--jobs job1,job2]
```
- Use values from Step 2 (or `--manual` args)
- If the user passed `--jobs`, forward them
- Run and capture output

Print the full output to the user.

---

### Step 4 -- Offer actions

After printing the schedule, ask:

> **Ready to act? Choose one or more:**
> 1. Start Window 1 now -- I'll print the `/loop` command(s)
> 2. Schedule Window 2 as a cloud trigger -- fires automatically after 5hr reset
> 3. Just the plan -- no actions

**If option 1:** Read `~/.claude/usage_plan_result.json` (written by the Python script) and print the `/loop` commands from `window1`:
```
/loop 10m /wiki-quality-loop
```

**If option 2:** Read `w2_trigger_at` from `~/.claude/usage_plan_result.json`. For each job in `window2`, call `mcp__claude_ai_Claude_Code_Remote__create_trigger` with:
- `name`: `usage-plan-w2-<job_name>`
- `run_once_at`: the `w2_trigger_at` timestamp
- `prompt`: `/<job_name>`
- `create_new_session_on_fire`: false (fires into this session)

Confirm: "Trigger created for /<job_name> at <time>."

**If quota is very low (< 15% remaining):** Also suggest:
```
python C:/Vault/tools/wait_and_resume.py "<reset_iso>"
```

---

## Manual fallback

If browser automation is unavailable or produces no result, the user can always run:

```bash
python C:/Vault/tools/usage_planner.py plan 45 "2026-07-08T09:00:00+07:00" --jobs wiki-quality-loop,domain-daily
```

Substitute actual values from the claude.ai settings page.

---

## Calibration

After each job run completes (or Claude cuts off), log the actual duration:
```bash
python C:/Vault/tools/usage_planner.py run-log domain-daily 28
```
Over time, update `cost_weight` values in `usage_planner_config.yaml` to match observed burn rates.
