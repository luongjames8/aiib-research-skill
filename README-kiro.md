# AIIB Research Skill — Kiro Install & Usage Guide

Kiro uses different conventions from Claude Code (`.claude/`) and claude.ai. This guide covers
everything specific to running the AIIB research skill on Kiro.

---

## Layout

The Kiro port lives in two directories at the repo root:

```
.kiro/
  steering/          # always-on + auto-triggered context injections
    aiib-mandate.md  # ALWAYS mode — injected into every agent session
    sector-scan.md   # AUTO mode — fires on Mode A requests
    company-sourcing.md  # AUTO mode — fires on Mode S requests
    company-dossier.md   # AUTO mode — fires on Mode B requests
  agents/            # parallel subagent worker definitions
    subsector-researcher.md    # Mode A worker (one per sub-sector)
    source-expander.md         # Mode S worker (one per anchor/round)
    company-dossier-researcher.md  # Mode B worker (one per company)

aiib-research/
  references/        # mandate, templates, sourcing methods, provenance rules, data-sources
  scripts/           # fetch_financials.py, dedup_candidates.py
```

All reference material and scripts are under `aiib-research/`. The `.kiro/` files point into it
with relative paths — do not move either tree independently.

---

## Steering files

Kiro steering files carry a YAML front matter `mode` field:

| Mode | Behavior |
|---|---|
| `always` | Injected into every agent session unconditionally. |
| `auto` | Injected only when Kiro decides it is relevant, based on `description` matching the conversation. |
| `agent` | Injected only when the agent is explicitly invoked by name. |

### What is in each file

**`aiib-mandate.md`** — `mode: always`

The AIIB mandate (6 sectors, 4 thematic priorities, 2030 targets, sourced from aiib.org 2026-06-22).
Always-on so mandate alignment is never disconnected from the agent's context, regardless of which
mode is running.

**`sector-scan.md`** — `mode: auto`

The Mode A (sector scan) system prompt: enumerate every sub-sector, run the 9-field A-I economics
template on each, tier from evidence, surface anchors. Fires automatically on requests like
"research Indonesia renewables", "map the Vietnam data-center landscape", "investment case for
Philippine water", and any AIIB-mandate sector framing.

**`company-sourcing.md`** — `mode: auto`

The Mode S (company sourcing) system prompt: graph-expand anchors in iterative rounds, dedup with
`dedup_candidates.py`, rank private candidates. Fires automatically on "find private solar developers
in Indonesia", "who competes with this company", "build a pipeline of geothermal names", and similar
deal-sourcing language.

**`company-dossier.md`** — `mode: auto`

The Mode B (company dossier) system prompt: 7-section structured investment dossier screened within
sub-sector economics. Fires automatically on "build a dossier on Sunsure Energy", "is this a good
investment", "profile this company", and similar company deep-dive language.

### How auto-trigger works

Kiro matches on the steering file's `name` and `description` fields against the current conversation.
Write description field text that matches the kinds of requests the mode handles — not just the
canonical phrasing. The three auto files cover "AIIB", "sector scan", "sourcing", "dossier",
"investment case", "find companies", "pipeline", "deep-dive", and synonyms. If a request matches
none of the three, only the always-on mandate file is active.

There is no way to force a steering file to fire beyond matching its description. If Kiro is
not picking up the right mode, add the matching phrase to the description front matter.

---

## Agent files (`.kiro/agents/`)

Three parallel worker agents, one per mode:

| File | Used by | Task |
|---|---|---|
| `subsector-researcher.md` | Mode A orchestrator | Researches ONE sub-sector to full 9-field A-I depth |
| `source-expander.md` | Mode S orchestrator | Expands ONE anchor into adjacent private companies |
| `company-dossier-researcher.md` | Mode B orchestrator | Produces ONE full 7-section company dossier |

Each agent file sets a `model:` field pinning workers to Sonnet (cheap) while the orchestrator may run a
larger model. The literal value lives in the `.kiro/agents/*.md` front matter (the source of truth) —
Kiro resolves it literally, so confirm that ID is current before a large run.

### How parallel fan-out works

The orchestrator skill (a steering file's injected prompt, active in the main session) instructs
the agent to spawn worker tasks — one per sub-sector / anchor / company. Kiro executes those as
parallel agent tasks under the hood. The workers run independently and return their results to the
orchestrator, which assembles the final output.

To guarantee the orchestrator actually delegates rather than doing the work inline (which is valid
but uses the more expensive session model), add explicit delegation language to your prompt:

```
Research India · Renewables for AIIB. Delegate each sub-sector to a subsector-researcher agent.
```

```
Find private solar developers in India. Delegate each anchor expansion to a source-expander agent.
```

```
Build a dossier on Sunsure Energy. Delegate to a company-dossier-researcher agent.
```

Without that nudge, on a small or pre-triaged request the model may complete the work inline. Both
paths produce the same output; the delegation path is cheaper on large runs.

---

## Gotchas

**Subagents do not receive Specs.**
Kiro Specs (`.kiro/specs/`) are injected into the primary session only. A spawned worker agent
starts with its own agent file as context plus whatever the orchestrator passes explicitly in the
task prompt. The orchestrator must pass any sub-sector economics, the found-set, or sector context
as literal text in the task description — it cannot rely on Spec injection to do it.

**Hooks do not fire inside subagents.**
Kiro Hooks (`.kiro/hooks/`) fire on events in the primary session (file saves, terminal output,
etc.). They do not fire inside spawned agent tasks. Any behavior you need in workers must be built
into the agent file itself.

**Non-recursion is automatic by tool restriction.**
Workers are defined with a restricted tool set: `WebSearch`, `WebFetch`, `Read` (and `Bash` for
`fetch_financials.py`). They do not have an agent-spawning tool. This is what enforces the
one-level-deep rule — a worker cannot spawn another worker even if the prompt asked it to. You do
not need to implement an explicit recursion guard; the tool list is the guard.

**Confirm the model ID before a large run.**
Each `.kiro/agents/*.md` front matter pins `model:` to a specific Sonnet ID, which Kiro resolves
literally. If Anthropic has released a newer Sonnet and the old ID was retired, workers fail at spawn
time. Check the ID in those files is a valid Kiro model and update it there if needed — the intent is
"current Sonnet", so track the ID, not just the name.

**`dedup_candidates.py` requires Bash access.**
Mode S deduplication runs `aiib-research/scripts/dedup_candidates.py` via Bash in the orchestrator session. The
orchestrator steering file has Bash in its tool list. Workers (`source-expander`) do not have Bash
— they return raw JSON arrays; the orchestrator concatenates and deduplicates. Do not move the dedup
step into a worker.

---

## Usage

```
# Mode A — sector scan
"Research Indonesia · Renewables for AIIB. Delegate each sub-sector to a subsector-researcher agent."

# Mode S — company sourcing
"Find private geothermal developers in Indonesia. Delegate each anchor expansion to a source-expander agent."

# Mode B — company dossier
"Build a dossier on Sunsure Energy. Delegate to a company-dossier-researcher agent."

# Full funnel
Run A first to get sub-sector economics and anchors, then feed those into S, then feed the top
private names from S into B.
```

See `examples/` for real end-to-end outputs (India renewables funnel, 2026-06-23): a sector scan,
a 121-company private pipeline, and a full dossier on a private Tier-1 name.
