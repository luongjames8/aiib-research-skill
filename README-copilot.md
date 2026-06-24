# AIIB Research Skill — GitHub Copilot (VS Code) Install & Usage Guide

This guide covers running the AIIB research skill on **GitHub Copilot in VS Code**. The three research
modes (Sector Scan, Company Sourcing, Company Dossier) work on Copilot via slash-prompt entry points and
parallel agent fan-out. The underlying methodology and output format are identical to the Claude Code
port; the packaging maps to Copilot's native conventions.

---

## Layout

```
.github/
  copilot-instructions.md          ← always-on: loaded into every Copilot session in this repo
  prompts/
    aiib-sector-scan.prompt.md     ← /aiib-sector-scan slash entry point (Mode A)
    aiib-company-sourcing.prompt.md← /aiib-company-sourcing slash entry point (Mode S)
    aiib-company-dossier.prompt.md ← /aiib-company-dossier slash entry point (Mode B)
  agents/
    aiib-sector-scan.md            ← Mode A orchestrator agent
    aiib-company-sourcing.md       ← Mode S orchestrator agent
    aiib-company-dossier.md        ← Mode B orchestrator agent
    subsector-researcher.md        ← worker: one per sub-sector (Mode A)
    source-expander.md             ← worker: one per anchor per round (Mode S)
    company-dossier-researcher.md  ← worker: one per company (Mode B)

aiib-research/
  references/
    aiib-mandate.md                ← AIIB 6 sectors + 4 thematic priorities (cited, never hallucinated)
    ai-template.md                 ← 9-field A-I sub-sector output template
    dossier-template.md            ← 7-section company dossier template
    data-sources.md                ← financials ladder (yfinance / EDGAR / web / training)
    provenance.md                  ← tagging rules (🟢 / 🔵 / ⚠️)
    sourcing-methods.md            ← graph-expand, fund-follow, value-chain methods
  scripts/
    fetch_financials.py            ← pulls live EV/EBITDA, P/E, P/B, margins via yfinance (auto-installs)
    dedup_candidates.py            ← normalizes + merges candidate JSON arrays (Mode S)
```

---

## Install

**Prerequisites:** VS Code with the GitHub Copilot extension, Copilot Pro/Business/Enterprise, agent
mode enabled (`github.copilot.chat.agent.enabled: true` in VS Code settings).

**Steps:**

1. Clone this repo and open it as a VS Code workspace:
   ```
   git clone https://github.com/<org>/aiib-research-skill
   code aiib-research-skill
   ```

2. That is it. VS Code picks up `.github/copilot-instructions.md`, `.github/prompts/`, and
   `.github/agents/` automatically from the open workspace root. No extension config, no import step.

---

## How each file loads

**`.github/copilot-instructions.md` — always-on.**
Injected into every Copilot chat session in this workspace without the user doing anything. It
establishes the three provenance tags (🟢 / 🔵 / ⚠️), the financials ladder (script → web → training),
and the mandate-citation rule. These rules apply to all sessions, not just research ones.

**`.github/prompts/` — slash entry points.**
Each `.prompt.md` file becomes a slash command in Copilot chat. Typing `/aiib-sector-scan` inserts the
Mode A prompt template, which accepts `$ARGUMENTS` (your country + sector). Similarly for
`/aiib-company-sourcing` and `/aiib-company-dossier`. These prompts hand off immediately to the
corresponding orchestrator agent.

**`.github/agents/` — mode orchestrators + worker subagents.**
Agent `.md` files define named agents. Three are user-invocable mode orchestrators (one per research
mode); three are worker subagents that the orchestrators spawn. Workers are marked
`user-invocable: false`, which hides them from the agent picker — they only appear in the orchestrator's
`agent` calls, not as options the user can select directly.

---

## Invoking the skill

Two equivalent paths:

**Via slash command (recommended):**
Open Copilot chat, switch to agent mode, type the slash command and fill in the argument:
```
/aiib-sector-scan Indonesia · Renewables
/aiib-company-sourcing Indonesia · geothermal — expand anchors from Mode A
/aiib-company-dossier Sunsure Energy · India · C&I solar
```

**Via the agent picker:**
Click the agent icon in Copilot chat, select **AIIB Sector Scan**, **AIIB Company Sourcing**, or
**AIIB Company Dossier**, then describe the task. The three worker agents (`subsector-researcher`,
`source-expander`, `company-dossier-researcher`) do not appear in the picker because they are marked
`user-invocable: false`.

---

## Parallel subagents

Subagent fan-out is a **first-party VS Code feature** (Copilot agent mode, not a workaround). The mode
orchestrators use `agent` to spawn worker agents in parallel:

- **Mode A** spawns one `subsector-researcher` per sub-sector, in waves of up to ~6 concurrent workers.
- **Mode S** spawns a batch of ~3–4 `source-expander` workers per sourcing round, then decides whether
  to run another round based on how many new names were found.
- **Mode B** spawns one `company-dossier-researcher` per company (up to ~6 concurrent).

Workers are initiated by the orchestrator agent (`agent`), not by the user, which is why the
"agent-initiated" phrasing applies. The orchestrator merges their returns and produces the final output.

**Non-recursion is enforced by design.** The worker agents (`subsector-researcher`, `source-expander`,
`company-dossier-researcher`) do not have the `agent` capability — they have web search, file
read, and (where relevant) Bash for `fetch_financials.py`, nothing else. This structurally prevents a
worker from spawning further sub-workers. The recursion risk (which can fan into hundreds of agents) is
not mitigated by a prompt instruction; it is prevented by capability omission.

---

## Cost-tier rule

**Worker model must be equal to or cheaper than the main session model.** The orchestrator's job is
coordination: resolve entities, load context, dispatch workers, assemble results. The expensive token
work (web searches, template filling, financial analysis) runs in the workers. Running the session on
Sonnet keeps both orchestrator and workers on Sonnet — cheapest path, and verified sufficient for this
research methodology.

To run on Sonnet in VS Code: open settings, set `github.copilot.chat.agentModel` to `claude-sonnet-*`
(or whichever Sonnet-tier model Copilot exposes). Alternatively, tell the orchestrator explicitly in
your prompt: "use Sonnet for all subagents."

---

## References and scripts

All reference files live under `aiib-research/references/` and are read by both orchestrator and worker
agents at runtime via the `codebase` and `githubRepo` tools declared in each agent's front matter.

| File | Purpose |
|---|---|
| `aiib-mandate.md` | Authoritative AIIB mandate (6 sectors, 4 themes, 2030 targets) — cited by every mandate-fit scoring step |
| `ai-template.md` | 9-field A–I sub-sector output template (fields A market economics through I competitive landscape) |
| `dossier-template.md` | 7-section company dossier template (background through risk assessment) |
| `data-sources.md` | Financials ladder and data-tier descriptions |
| `provenance.md` | Tagging rules: 🟢 web-sourced, 🔵 connector, ⚠️ training-unverified |
| `sourcing-methods.md` | Graph-expand, fund-follow, value-chain, source-sweep methods for Mode S |

Two scripts under `aiib-research/scripts/` are invoked by workers via Bash:

- **`fetch_financials.py <ticker>`** — pulls EV/EBITDA, P/E, P/B, revenue, margins via yfinance.
  Auto-installs yfinance on first use if pip is available. Returns `unavailable` if network is blocked,
  triggering graceful fallback to web search. Results tagged 🟢.
- **`dedup_candidates.py`** — reads **one JSON document** on stdin (a flat array, or an array of the
  per-worker arrays `[[...],[...]]`, which it flattens one level — do NOT pipe adjacent `[...][...]`,
  that's invalid JSON), normalizes company names (strips legal suffixes, lowercases), merges duplicates,
  ranks multi-sourced names first, and emits one entry per company. Used by the Mode S orchestrator
  between sourcing rounds.

---

## Example prompts

```
# Full funnel
/aiib-sector-scan India · Renewables
/aiib-company-sourcing India · C&I solar — expand from Mode A anchors
/aiib-company-dossier Sunsure Energy

# Standalone
/aiib-company-dossier PT Barito Renewables · Indonesia · geothermal
/aiib-company-sourcing Vietnam · offshore wind — find private developers
```

See `examples/` for real outputs produced on a Claude Code run (same methodology, same templates):
- `examples/india-renewables-sector-scan.md` — Mode A: 12 sub-sectors
- `examples/india-solar-company-sourcing.md` — Mode S: 121 companies, 96 private
- `examples/sunsure-energy-dossier.md` — Mode B: 7-section dossier, private company
