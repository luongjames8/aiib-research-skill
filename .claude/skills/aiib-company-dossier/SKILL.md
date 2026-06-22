---
name: aiib-company-dossier
description: >-
  Mode B of AIIB investment research. Given a company (optionally with country/sector context, or a row
  from an aiib-sector-scan shortlist), produce a structured 5-section investment dossier: (1) background,
  (2) forward guidance, (3) financials, (4) AIIB-mandate alignment against the 6 sectors + 4 thematic
  priorities, (5) key people. Every claim is provenance-tagged (web-sourced vs. model-training vs.
  connector) so unverified figures are visible. Use when the user wants a company deep-dive / investment
  dossier / due-diligence brief for AIIB-style developing-markets infrastructure investing, names a
  company to research, or hands over a shortlist from the aiib-sector-scan skill (Mode A). Built for a
  web-search floor; uses subagents when available, runs sequentially when not.
---

# AIIB Company Dossier (Mode B)

Top-down funnel, stage two: **company → structured investment dossier.** Consumes the shortlist produced
by the **aiib-sector-scan** skill (Mode A), or runs standalone on any named company.

## Inputs

- **Required:** a company name.
- **Optional:** country / sector / sub-sector context (improves disambiguation and mandate scoring),
  or a shortlist row from Mode A. Multiple companies → produce one dossier each.

## Workflow

### Step 1 — Resolve the company
Confirm which entity (disambiguate same-name companies by country/sector; identify parent/group and
listing status). Web-search to confirm it exists and is current; tag provenance.

### Step 2 — Produce the 5-section dossier
Follow `references/dossier-template.md` exactly. The five sections:
1. **Background** — what it is, ownership, geographies, business lines, scale.
2. **Forward guidance** — management guidance, strategy, pipeline, catalysts/headwinds (stated vs. inferred).
3. **Financials** — revenue, margins, leverage, funding/ratings, comps — numbers tagged, gaps flagged `[not available]`.
4. **AIIB-mandate alignment** — sector + theme match + climate/Paris + Strong/Partial/Out verdict, using
   `references/aiib-mandate.md` (cite it).
5. **Key people** — founders, CEO, CFO, chair, major shareholders — name, role, one-line background.

**Delegation (the portability rule):** If you have a Task/subagent tool (Claude Code), and especially
when handed **multiple** companies, spawn one `company-dossier-researcher` subagent **per company** (or,
for a single company, optionally one per section) and run them in parallel, then assemble. If you do not
(claude.ai chat app), produce the dossier(s) **sequentially** in this context. Identical output either way.

### Step 3 — Verify & flag
Re-read the dossier for any untagged numbers (→ ⚠️) and any fabricated-looking specifics. Add the
section provenance summaries. Surface the biggest open verification items at the end.

## Output structure

Per company: a header (name + one-line identity + provenance banner) then the **five sections in order**,
each ending with a provenance summary line, then a short **"Verify before relying"** list of the
highest-risk unsourced claims.

## Hard rules

- **Provenance on every claim** (`references/provenance.md`). Default to ⚠️ when unsure; numbers especially.
  No web access this run → full dossier anyway, fully ⚠️-tagged, under the no-live-sources banner.
- **Never fabricate** financials, guidance, or people. Missing = `[not available]`, explicitly. A private
  company with thin public data yields a thin dossier — that is correct, not a reason to invent.
- **Separate fact from inference** — label analytical judgments distinctly from sourced claims.
- **Mandate fit from `references/aiib-mandate.md`**, cited — not from memory.
