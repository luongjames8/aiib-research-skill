---
name: aiib-company-dossier
description: >-
  Mode B of AIIB-style investment research: turn a company into a structured, sourced investment dossier.
  Given a company (optionally with country/sector context, or a row from an aiib-sector-scan shortlist),
  produce a structured dossier — background + competitive moat, forward guidance & catalysts, financials
  (margins, earnings quality, peer multiples), valuation & bull/base/bear scenarios, AIIB-mandate
  alignment incl. ESG (vs. the 6 sectors + 4 thematic priorities), key people & management quality, and
  risk assessment — pulling free structured financial data (yfinance / SEC EDGAR) when a code tool is
  available and falling back to web search otherwise, with every claim provenance-tagged so unverified
  figures are visible. Use this whenever the user wants a company deep-dive,
  investment dossier, due-diligence brief, company profile, or to assess a company as an investment —
  especially for infrastructure / development-finance / emerging-market investing, or when they hand over
  a shortlist from the aiib-sector-scan skill (Mode A). Trigger even if they never say "dossier" or
  "AIIB" — e.g. "is <company> a good investment", "research <company> for me", "profile <company>",
  "what's the investment case for <company>". Web-search floor; uses subagents when available, runs
  sequentially when not.
---

# AIIB Company Dossier (Mode B)

Top-down funnel, stage two: **company → structured investment dossier.** Consumes the shortlist produced
by the **aiib-sector-scan** skill (Mode A), or runs standalone on any named company.

Integrity is the whole point. This dossier feeds an investment decision, so a confidently-stated wrong
number is worse than an honest gap. A private company with thin public data yields a thin dossier — that
is the correct output, never a reason to invent. Mark missing figures `[not available]`, tag every claim
by source, and keep your own inferences visibly separate from sourced facts.

## Inputs

- **Required:** a company name.
- **Optional:** country / sector / sub-sector context (improves disambiguation and mandate scoring),
  or a shortlist row from Mode A. Multiple companies → produce one dossier each.

## Workflow

### Step 1 — Resolve the company + pull data
Confirm which entity (disambiguate by country/sector; identify parent/group and listing status).
**Get the best data tier available** (`references/data-sources.md`): if you have a code tool with
network, pull free structured financials with `scripts/fetch_financials.py <ticker>` (yfinance — works
for international tickers via exchange suffixes, e.g. `PGEO.JK`); if it returns `unavailable`, or for
private/unlisted names, fall back to web search of filings/earnings. Tag everything by provenance.

### Step 2 — Produce the dossier
Follow `references/dossier-template.md` — the **5 core sections + 2 analytical sections** (Valuation &
scenarios, Risk), adapted from institutional equity research for AIIB direct/PE investing:
1. **Background** (+ competitive moat) · 2. **Forward guidance & catalysts** · 3. **Financials** (margins
with history, earnings quality, cash flow, peer-comparison multiples) · 4. **Valuation & scenarios**
(comps / precedent / DCF + bull-base-bear, expressed as conviction not a price target) · 5. **AIIB-mandate
alignment incl. ESG** (cite `references/aiib-mandate.md`) · 6. **Key people & management quality** ·
7. **Risk assessment** (company-specific + macro). The template has the full spec for each.

**Delegation (the portability rule):** If you have a Task/subagent tool (Claude Code), and especially
when handed **multiple** companies, spawn one `company-dossier-researcher` subagent **per company** (or,
for a single company, optionally one per section) and run them in parallel, then assemble. If you do not
(claude.ai chat app), produce the dossier(s) **sequentially** in this context. Identical output either way.

### Step 3 — Verify & flag
Re-read the dossier for any untagged numbers (→ ⚠️) and any fabricated-looking specifics. Add the
section provenance summaries. Surface the biggest open verification items at the end.

## Output structure

Per company: a header (name + one-line identity + provenance banner) then the **seven sections in order**,
each ending with a provenance summary line, then a short **"Verify before relying"** list of the
highest-risk unsourced claims.

## Self-check before returning (depth gate — do this every run)

Stop and verify; if any answer is "no", fix it before returning:
- [ ] **All 7 sections** present (background+moat · guidance+catalysts · financials · valuation & scenarios · mandate+ESG · people+mgmt quality · risk)?
- [ ] **Best data tier used?** Tried `fetch_financials.py` (or filings) before settling for web/training?
- [ ] **Financials with numbers**, each tagged — and every missing figure marked `[not available]`, not invented?
- [ ] **Mandate** scored from `aiib-mandate.md` (cited): sector + theme + climate + Strong/Partial/Out verdict?
- [ ] **Provenance** on every claim (🟢/🔵/⚠️), with the no-live-sources banner if web was off?
- [ ] **Fact vs inference** separated; a "Verify before relying" list of the riskiest unsourced claims included?
