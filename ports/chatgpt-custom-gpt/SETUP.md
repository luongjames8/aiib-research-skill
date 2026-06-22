# Set up the ChatGPT Custom GPT

This port carries the same AIIB research methodology to ChatGPT, where the Claude **Skill** format,
**subagents**, and the **in-sandbox live-data tier** are not available. It runs on ChatGPT's
**Web search** capability (the floor), with the reference docs as **Knowledge**.

Requires a ChatGPT plan that can create GPTs (Plus / Pro / Team / Enterprise / Edu).

## Steps

1. **Create a GPT** — ChatGPT → your name → **My GPTs** → **Create a GPT** → **Configure** tab.
2. **Name / description** — e.g. "AIIB Investment Research"; description from this repo's README.
3. **Instructions** — paste the text from `INSTRUCTIONS.md` (everything **below the `---`**) into the
   Instructions box. (It's ~5.8k characters, under ChatGPT's instruction limit.)
4. **Knowledge** — upload all five files from `knowledge/`:
   `aiib-mandate.md`, `ai-template.md`, `dossier-template.md`, `provenance.md`, `data-sources.md`.
5. **Capabilities** — enable **Web search** (required — it's the data floor). You may also enable
   **Code Interpreter & Data Analysis** so the GPT can crunch files the user uploads. Image gen / Canvas
   are not needed.
6. **Save** → set visibility (Only me / Anyone with the link / Workspace).

## Usage

- **Mode A (sector):** "Research Indonesia · Renewables for AIIB." → sub-sector deep-dive + shortlist.
- **Mode B (company):** "Build a dossier on <company>." → 7-section dossier.

## Important limits on ChatGPT (verified from OpenAI docs)

- **The data-analysis sandbox cannot reach the internet** — *"The Python environment used for data
  analysis cannot make external web requests or API calls"*
  (help.openai.com/en/articles/8437071-data-analysis-with-chatgpt). So the repo's
  `scripts/fetch_financials.py` / yfinance path **does not run here**. For hard numbers, either:
  - let the GPT pull from **Web search** (the default), or
  - **upload** a financials file (CSV/XLSX) and the GPT will analyse it (🔵 `[uploaded: file]`), or
  - wire an **Action** to an external financial-data API (Configure → Actions). Note a GPT can use
    **either Actions or Apps, not both** (help.openai.com/en/articles/8554397-creating-a-gpt).
- **No subagents** — research runs sequentially in one context (no parallel fan-out).
- **Not an auto-installed Skill** — it's a Custom GPT you configure once; the methodology is identical,
  the packaging differs.

The provenance tagging makes the active tier visible on every claim, so output is honest about whether a
figure came from web search, an upload, or model memory.
