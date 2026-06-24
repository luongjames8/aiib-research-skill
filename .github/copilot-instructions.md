# Copilot Instructions — AIIB Research Skill

## Provenance Tagging (always-on, every file)

Tag every claim at the point of use. Three tags, no exceptions:

- **🟢 web-sourced** — fetched live from a URL or via `fetch_financials.py` in this session
- **🔵 connector** — from a connected MCP data source / uploaded file the user provided
- **⚠️ training-unverified** — from model training knowledge; not verified against a live source

Never omit a tag. Never assume a claim is common knowledge. If you are unsure which tag applies, use ⚠️.

When no live source is available, prepend a banner before the section:

```
> **No live sources available.** The following is drawn from training knowledge and is unverified. Treat as a starting point only.
```

## Mandate Fit

AIIB mandate citations must come from `aiib-research/references/aiib-mandate.md` in this repo. Never hallucinate a mandate clause. If the file does not contain the relevant language, say so explicitly rather than paraphrasing from training.

## Live Financials Ladder

Always attempt sources in this order:

1. **`python aiib-research/scripts/fetch_financials.py <tickers>`** — run this first; tag results 🟢
2. **Web search** — if the script fails or returns no data; tag results 🟢
3. **Training knowledge** — last resort; tag results ⚠️ and show the "no live sources" banner

Do not skip to step 3 without attempting steps 1 and 2.

## General Discipline

- Port provenance tags into every file you touch or generate, including notebooks, markdown reports, and code comments that assert facts.
- Do not merge tagged and untagged claims in the same sentence. If a sentence mixes sources, split it.
- When editing existing files, add missing tags to lines you modify. Do not silently strip or ignore tags already present.
