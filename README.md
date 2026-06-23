# AIIB Investment Research Skills

Three portable [Agent Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) for
AIIB-style developing-markets infrastructure investment research, usable in **claude.ai** (web + desktop)
and **Claude Code** (terminal + web). A top-down deal-sourcing funnel in three stages:

```
Mode A  sector scan      → sub-sector economics + anchors          (context)
Mode S  company sourcing  → graph-expand anchors → PRIVATE candidates (the longlist)
Mode B  company dossier   → deep-dive each candidate, in sector context (the deep-dive)
```

- **Mode A — `aiib-sector-scan`** — input `Country · Sector` (e.g. "Indonesia · Renewables") → exhaustive
  sub-sector **enumeration + cheap triage**, a full 9-field A–I deep-dive on the **most-investable few**
  (deep-on-all is opt-in), plus the **anchors** (listed leaders, DFI investees, deal winners) that
  sourcing expands from.
- **Mode S — `aiib-company-sourcing`** — input a sub-sector (+ its economics) → a ranked list of mostly-
  **PRIVATE**, mandate-fit companies, found by **graph-expanding anchors** (competitors, suppliers,
  customers, co-investors, PE/DFI fund-siblings), **fund-following**, **value-chain decomposition**, and
  sweeping deal trackers / PPP pipelines / credit-rating lists / local-language sources.
- **Mode B — `aiib-company-dossier`** — input a company (or a Mode-S candidate) → a structured dossier,
  screened **within its sub-sector economics**: background + moat · forward guidance & catalysts ·
  financials (margins, earnings quality, peer multiples) · valuation & bull/base/bear scenarios ·
  AIIB-mandate alignment incl. ESG · key people & management quality · risk assessment.

### Design principles

- **Provenance-tagged.** Every claim is marked 🟢 web-sourced / 🔵 connector / ⚠️ training-unverified, so
  unverified figures are visible. Built for a **web-search floor**: with no network it still runs, fully
  ⚠️-tagged under a "no live sources" banner.
- **Mandate-anchored.** Each skill bundles `references/aiib-mandate.md` — AIIB's 6 sectors + 4 thematic
  priorities + 2030 targets, sourced from aiib.org — so mandate fit is cited, not hallucinated.
- **Subagents where available, never required.** On Claude Code the skills delegate each sub-sector /
  company to a parallel subagent (`.claude/agents/`); on the claude.ai chat app (no subagents) they run
  sequentially. Same output either way.
- **Tiered free data, web-search floor.** When a code tool + network are available, the skills pull free
  structured financials directly — **yfinance** (broad international coverage), **SEC EDGAR**, **stooq**,
  or **OpenBB**'s free providers — via the bundled `scripts/fetch_financials.py`, tagged 🟢; otherwise
  they fall back to web search, and finally to ⚠️-tagged training knowledge. No API keys required.

### Data availability by surface (important)

The structured-data tier needs a **code-execution sandbox with network access**. That differs by surface,
so the same skill produces richer or thinner financials depending on where it runs — by design, it
degrades gracefully and the provenance tags always show which tier was used:

| Surface | Web search (floor) | Structured data (`fetch_financials.py`, yfinance/EDGAR) |
|---|---|---|
| **Claude Code — terminal** | ✅ | ✅ (pip + network available) |
| **Claude Code — web** (claude.ai/code) | ✅ | ✅ if the cloud environment's network level allows package + data-API access (configurable; the default *Trusted* allowlist may need Yahoo/SEC hosts added) |
| **claude.ai chat app** | ✅ | ⚠️ **sandbox network is settings-dependent** — may be off, and packages are pre-configured-only, so the script can return `unavailable` and the skill falls back to web search |

**Takeaway:** for the fullest, numbers-from-live-feeds dossiers, run on **Claude Code**. On the claude.ai
chat app it still works end-to-end — it just leans on web search rather than direct data pulls when the
sandbox has no network. Either way, every figure is provenance-tagged so you can see what it relied on.

## Platform support

The research **methodology** is cross-platform; the **packaging** and the **live-data tier** are
Claude-native. Verified against vendor docs (Anthropic + OpenAI, early 2026):

| Capability | Claude Code (terminal / web) | claude.ai chat | ChatGPT |
|---|---|---|---|
| Import as an auto-triggering **Skill** | ✅ | ✅ (Settings → Capabilities) | ❌ — rebuild as a **Custom GPT** (see [`ports/chatgpt-custom-gpt/`](ports/chatgpt-custom-gpt/)) |
| **Subagent** parallel fan-out | ✅ (`.claude/agents/`, Sonnet) | ❌ sequential | ❌ sequential |
| **Web-search** floor | ✅ | ✅ | ✅ (GPT "Web search" capability) |
| **Live structured data** in-sandbox (yfinance / EDGAR) | ✅ pip + network | ⚠️ network is settings-dependent | ❌ sandbox can't make web/API calls — use file upload or a GPT **Action** |

For **ChatGPT**, the methodology is delivered as a **Custom GPT** running on web search — see
[`ports/chatgpt-custom-gpt/`](ports/chatgpt-custom-gpt/) (instructions + knowledge files + setup). The
in-sandbox data pulls (`scripts/fetch_financials.py`) don't run there, because *"the Python environment
used for data analysis cannot make external web requests or API calls"*
([OpenAI docs](https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt)).

## Credits & licenses

- This repo: **MIT** (see `LICENSE`).
- The fundamental + qualitative analysis framework adapts **[claude-equity-research](https://github.com/quant-sentiment-ai/claude-equity-research)**
  (MIT), reframed for AIIB-style direct/PE infrastructure investing — the public-equity *trading*
  apparatus (technical analysis, options flow, 12-month price targets) is intentionally omitted.
- **[OpenBB](https://github.com/OpenBB-finance/OpenBB)** is **AGPL-3.0** and is **not bundled** here; the
  skills only invoke it at runtime *if the user already has it installed*. `yfinance` (Apache-2.0) and
  SEC EDGAR cover the same free ground, so they are the default.

## Install

### claude.ai (web / desktop) — Pro, Max, Team, Enterprise (code execution enabled)
Each skill folder is self-contained. In **Settings → Capabilities → Skills**, upload each of:
- `.claude/skills/aiib-sector-scan/`
- `.claude/skills/aiib-company-sourcing/`
- `.claude/skills/aiib-company-dossier/`

(Subagents in `.claude/agents/` are not used on claude.ai; the skills detect this and run sequentially.)

### Claude Code (terminal or web)
Clone this repo and open it (or point a Claude Code web session at it). The skills in `.claude/skills/`
and subagents in `.claude/agents/` are picked up automatically — subagent fan-out works here.

## Usage

```
Mode A:  "Research Indonesia · Renewables for AIIB."      →  sub-sector economics (triage + deep top few) + anchors
Mode S:  "Find private geothermal developers in Indonesia." →  ranked list of mostly-private candidates
Mode B:  "Build a dossier on <company>."                  →  7-section investment dossier
```
Typical flow: **A** (context + anchors) → **S** (source the private companies) → **B** (dossier each).

**See real runs** (live, 2026-06-23, clean Claude Code session):
- [`examples/india-renewables-sector-scan.md`](examples/india-renewables-sector-scan.md) — Mode A: 12
  sub-sectors, 2 waves of 6 Sonnet workers, primary-sourced, **comps verified live via yfinance** (46 🟢 / 2 ⚠️).
- [`examples/india-solar-company-sourcing.md`](examples/india-solar-company-sourcing.md) — Mode S: **121
  companies (96 private)** over 3 iterative rounds, 13 `source-expander` workers (zero recursion),
  deterministic dedup, ranked deal pipeline with PE/DFI backers.

### Controlling cost / the Sonnet subagents (Claude Code)

A skill can't *force* Claude to delegate or pick a model — that's the model's call + your session config.
Two levers that **do** work, verified live:

1. **Run the session on Sonnet** — `claude --model sonnet` (or `/model sonnet` interactively). Then the
   *whole* run — orchestrator and any subagents — is Sonnet. Cheapest, always works, and Sonnet is plenty
   for web research + filling the template.
2. **Tell it to delegate, in your prompt** — add e.g. *"delegate each deep sub-sector to a
   `subsector-researcher` subagent"* (Mode S: `source-expander`; Mode B: `company-dossier-researcher`).
   Verified: this makes it spawn the **purpose-built, non-recursive agents on Sonnet** while the
   orchestrator stays on your session model — so the heavy searching runs cheap. Without this nudge, on a
   small/triaged scan the model often just does it inline (fine, but on your session model).

Either way the run is **bounded** — triage + round caps + per-worker search budgets + non-recursive
agents mean it can't run away, whichever model it lands on.


## Disclaimer

- **Not affiliated with AIIB.** This is an independent, unofficial tool. It is **not** affiliated with,
  endorsed by, sponsored by, or sanctioned by the Asian Infrastructure Investment Bank (AIIB). "AIIB" and
  related names and marks are the property of their respective owner and are used here only for
  descriptive reference (nominative fair use).
- **Source of mandate data.** The AIIB sector and thematic-priority information in
  `references/aiib-mandate.md` was sourced from AIIB's public website (**aiib.org**) as of 2026-06-22 and
  may be incomplete or out of date. Consult **aiib.org** for authoritative, current information.
- **Not investment advice.** Output is AI-generated research for informational purposes only. It may
  contain errors, omissions, or fabricated figures — that is exactly why every claim is provenance-tagged
  (🟢 web / 🔵 connector / ⚠️ training-unverified). It does **not** constitute investment, financial,
  legal, or tax advice. Verify every figure independently and do your own due diligence before relying on
  anything here.
- **No warranty.** Provided "as is", without warranty of any kind. Use at your own risk; the authors
  accept no liability for any decision made on the basis of this tool's output.
