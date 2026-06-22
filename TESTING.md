# Testing the AIIB research skills

Two things to verify, separately: **(A) does the skill trigger**, and **(B) does it enforce depth once
triggered**. Skills are not invoked every turn — Claude reads each skill's `description` (always in
context) and loads the skill body (the rules) only when your request matches. So a skill that never
triggers reminds Claude of nothing.

## A. Trigger test

Ask something that matches the skill description and confirm the skill is actually used.

- **Mode A (`aiib-sector-scan`):** "Research Indonesia · Renewables for AIIB."
- **Mode B (`aiib-company-dossier`):** "Build a dossier on <company>."

How you see it triggered:
- **Claude Code (terminal / web):** the session shows the skill being invoked, and — because subagents
  are available here — spawns `subsector-researcher` / `company-dossier-researcher` agents in parallel.
- **claude.ai chat app:** Claude indicates it is using the skill in its response (no subagents there).

If it does NOT trigger, the `description` frontmatter needs to better match how you phrase the request —
that field is the only trigger signal.

## B. Depth test (the main thing)

Each SKILL.md ends with a **Self-check before returning** gate. Confirm the output actually meets it.

**Mode A — sector scan.** The output must have:
- [ ] **Exhaustive sub-sectors** — all of them, not just the obvious 3–4 (renewables should yield ~8–9:
      utility solar, C&I/rooftop, onshore wind, offshore wind, geothermal, small hydro, BESS, WtE/biomass,
      distributed generation).
- [ ] **Full A–I per sub-sector with real numbers** — market size, tariffs (actual ¢/kWh), margins, IRRs,
      a comps table, track record incl. blow-ups, IRR estimate, named risks, competitors. A one-paragraph
      sub-sector is a FAILURE.
- [ ] **Negative signals included** — write-downs, stalled projects, payment delays, policy reversals.
- [ ] **Provenance tags** on every numeric claim (🟢 web / 🔵 connector / ⚠️ training-unverified).
- [ ] **Mandate alignment cited to aiib.org** (not model memory).
- [ ] **Ranked, mandate-fit company shortlist** at the end (the hand-off to Mode B).

**Mode B — company dossier.** The output must have:
- [ ] **All 5 sections** — background · forward guidance · financials · AIIB-mandate alignment · key people.
- [ ] **Financials with numbers**, each tagged; every missing figure marked `[not available]`, not invented.
- [ ] **Mandate verdict** — sector + theme + climate + Strong/Partial/Out, citing aiib.org.
- [ ] **Provenance** on every claim; fact vs. inference separated.
- [ ] **"Verify before relying"** list of the riskiest unsourced claims.

If any output comes back shallow, harden the **Self-check** block in that skill's `SKILL.md` and re-test.

## C. Provenance / web-search-floor test

Run the same prompt twice:
1. **Web search ON** — expect mostly 🟢 `[web: source, date]` tags.
2. **Web search OFF** (or a sandbox with no network) — expect the top banner
   `⚠️ NO LIVE SOURCES THIS RUN — all claims are from model training and must be independently verified.`
   and ⚠️ tags throughout. The skill must still produce full output, just fully flagged.

This proves the tool degrades safely instead of silently presenting unverified figures as fact.

## D. Both surfaces

| Surface | Trigger | Subagents | Setup |
|---|---|---|---|
| Claude Code — web (claude.ai/code) | ✓ | ✓ parallel fan-out | point a session at this repo |
| Claude Code — terminal | ✓ | ✓ parallel fan-out | clone + open this repo |
| claude.ai chat (Pro/Max/Team/Enterprise) | ✓ | ✗ sequential | upload each `.claude/skills/<skill>/` folder in Settings → Capabilities → Skills |

Test Mode A → take a shortlist name → Mode B, on at least one Claude Code surface (to confirm subagent
fan-out) and on claude.ai (to confirm the sequential fallback produces the same structure).
