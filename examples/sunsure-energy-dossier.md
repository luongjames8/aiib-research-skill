<!--
Example output — aiib-company-dossier (Mode B), run live 2026-06-23 in a clean Claude Code session.
Subject: Sunsure Energy (PRIVATE, unlisted) — a Tier-1 name from the Mode-S example, screened within the
India C&I/open-access-solar sub-sector economics from the Mode-A example (the A->S->B hand-off).
Demonstrates the private-company path: no ticker, so company financials come from CRISIL/ICRA/CARE rating
rationales, FMO disclosure, sponsor press + registry; listed-PEER comps via fetch_financials.py (yfinance).
Stats: company-dossier-researcher worker (zero general-purpose) · 19 web searches · 10 primary-doc fetches ·
5 yfinance peer pulls · ~3 min. Provenance: 32 🟢 / 17 ⚠️ / 7 [not available]. Point-in-time snapshot for
illustration — not investment advice (see ../README.md).
-->

The `company-dossier-researcher` worker has returned the complete 7-section dossier, with listed-peer comps pulled via `fetch_financials.py` and provenance tagged throughout. Here it is in full.

---

# AIIB INVESTMENT DOSSIER — Sunsure Energy Private Limited

**Identity:** India C&I / open-access solar IPP, Partners Group majority-backed, ~700–800 MWp operational (the worker's web research found a higher figure than the ~600 MWp in your brief — flagged below), 7+ GWp pipeline, targeting 5–10 GW by 2030.

**Provenance banner:** Private, unlisted — no ticker feed. Company-level financials are from CRISIL/ICRA/CARE rating-rationale snippets (🟢), FMO project disclosure (🟢), Partners Group press (🟢), and media (🔵). Section 3/4 comps are listed Indian renewable peers via `fetch_financials.py` (yfinance, 🟢). Consolidated P&L, total debt, and IRR are inferred (⚠️) and must be independently verified. Prepared 23 Jun 2026.

> **Orchestrator screening note:** every margin/IRR/risk claim below is judged against the India C&I/OA-solar yardstick you supplied — OA tariffs ₹4.30–7.40/kWh, equity IRR ~18–22%, ~80–90% project-level EBITDA, and the open-access regulatory cliff as the dominant sub-sector risk.

---

## Section 1 — Background & Competitive Moat

**Identity:** Sunsure Energy Pvt Ltd (CIN U74900HR2014PTC083649), Gurugram-HQ IPP, incorporated 2014 [🟢 Tofler]. Five IIT-alumni co-founders: Shashank Sharma (Chairman/CEO), Shantanu Faugaat (COO), Manish Mehta (CCO), Kartikeya Narain Sharma (CBO), Tarunveer Singh (Head of Projects) [🟢 company site].

**Sponsor:** Partners Group acquired majority via a commitment of up to **USD 400m** (2023); **Rs 1,150 cr (~USD 138m) infused, Rs 2,050 cr (~USD 244m) undrawn** as of Mar 2025 [🟢 CRISIL, May 2025].

**Model transition:** EPC contractor → full IPP during **FY24** — episodic EPC margins replaced by 20–25-yr PPA annuity cash flows at ~80–90% project EBITDA (sub-sector norm; ⚠️ inference, consistent with listed pure-IPP comps ACME 90.3%, NTPC Green 86.6%) [🟢 CRISIL].

**Core product:** Green Energy Open Access — solar to C&I customers at landed ~₹3.5–4.5/kWh vs grid C&I ₹8–11/kWh (30–50% saving) [🔵 Optenpower]; group-captive structures used to escape CSS/AS [🔵 inference, consistent with ICRA Solarpark Ten]. Expanding into ISTS utility-scale, wind/hybrid, **BESS** (125 MW/500 MWh NVVN/Jhansi contract at ₹6.64/kWh, Aug 2025 [🟢 Energy-Storage.News]), and RTC. Green-hydrogen is an aspiration only — **no confirmed project** [⚠️].

**Scale/geography:** ~800 MW operational (UP, Maharashtra, Rajasthan, TN, Karnataka), 7.1–8.3 GW pipeline; 105 MWp Mahoba (UP's first GEC-II project, built in 4 months) [🟢 PV Tech, Jun 2026]. 80+ corporate offtakers — Flipkart, Dabur, Lupin, Bharat Forge, Jindal Stainless, Sify, Haldiram's, APL Apollo [🟢 company]. Recent financing: Rs 606 cr from Aseem Infra + RBL (Mar 2026); FMO ~USD 22m for 75 MWp TN [🟢 PV Tech, FMO].

**Moat (real but narrow):** (1) execution speed — 6-mo cycle vs ~12-mo industry, substantiated by 4-mo Mahoba; (2) UP stronghold + scarce GEC-II evacuation rights; (3) 16-state, multi-tech diversification reducing single-state cliff exposure; (4) PE balance-sheet depth. No regulatory concession or captive grid exists, and well-funded peers (CleanMax 2.54 GW, Fourth Partner 1.5 GW, Amp, O2 Power) hit the same customer set. BESS/RTC differentiation is emerging, not yet proven at scale.

*Provenance: 14 web (primary: company, Partners Group, CRISIL, CARE, FMO, PV Tech) · 3 inference.*

---

## Section 2 — Forward Guidance & Catalysts

**No published IR/annual report.** Targets from rating docs: **2 GW operational by FY27**, **5 GW by FY30** [🟢 CRISIL/CARE]; company website cites an aspirational **10 GW by 2030** [🟢 site — treat as aspirational]. Implies ~15× scale-up; 2 GW by FY27 is a significant stretch from ~700 MW today.

**Capital:** PG's undrawn Rs 2,050 cr is primary growth equity; each GW of OA/ISTS ≈ Rs 4,000–5,000 cr (⚠️ inference) — sufficient for active pipeline but full 5–10 GW needs more equity/leverage. SPV debt via banks (Aseem, RBL, Aditya Birla) and DFIs (FMO) at A-/Stable SPV ratings [🟢].

**Near-term catalysts (0–6m):** commissioning of ~868 MW under construction; FMO TN drawdown; PG equity tranche deployment. **Medium (6–24m):** 125 MW/500 MWh Jhansi BESS commission (Q4 FY27 — India's first developer-charged BESS); UP 500 MW milestone; Green OA policy evolution; **ISTS surcharge step-up (25% from Jun 2025 → 100% by Jul 2028)** compressing inter-state spreads.

**Analyst consensus:** none — private, no sell-side coverage.

*Provenance: 9 web · 3 inference.*

---

## Section 3 — Financials

**Company (private; rating-snippet sourced):**
- FY24 *standalone* revenue Rs 41.2 cr [🟢 CARE/Tracxn] — EPC-tail only, **not representative** of IPP run-rate; do not use for valuation.
- FY25 consolidated revenue **[not available]** — most operational MW commissioned in FY25.
- Weighted-avg PLF **16.9% FY25** (vs P75 17.1%) [🟢 CARE] — in line with central-India OA norms.
- SPVs rated CRISIL/ICRA **A-/Stable**, DSCR described "adequate"/"comfortable" but absolute figures **[not available]**; A- implies ~1.1–1.3× min DSCR [⚠️].
- Cash: consol Rs 374 cr, standalone Rs 185 cr (Mar 2025) [🟢 CRISIL]. **Total consolidated debt [not available]**; per-MW debt ~Rs 65 cr/10 MW [⚠️ from single data points]. CARE flags structure becoming "increasingly leveraged."

**Listed peer comps (yfinance 🟢, Jun 2026):**

| Metric | ADANIGREEN | KPIGREEN | NTPCGREEN | ACMESOLAR | WAAREE |
|---|---|---|---|---|---|
| Mkt cap (₹bn) | 2,553 | 81 | 819 | 247 | 881 |
| Revenue FY26 (₹bn) | 129.9 | 27.0 | 28.6 | 25.1 | 265.4 |
| EBITDA margin | 83.1% | 35.5% | 86.6% | 90.3% | 22.3% |
| Net margin | 12.7% | 17.7% | 18.3% | 19.9% | 14.0% |
| Rev growth YoY | 14.3% | 39.8% | 46.7% | 12.5% | 111.8% |
| EV/EBITDA (TTM) | 33.8× | 13.3× | 46.3× | 15.4× | 14.3× |
| Trailing P/E | 161× | 17× | 157× | 42.8× | 23.8× |
| P/B | 13.2× | 2.7× | 4.4× | 4.2× | 6.1× |

**Comparability caveat:** Adani Green & NTPC Green are utility-scale (25-yr central PPAs → lower regulatory risk than OA); Waaree is a module maker/EPC; KPI Green is the closest listed OA/C&I proxy but its ~35% consolidated EBITDA reflects EPC drag. **No pure-play listed OA/C&I IPP exists** — closest strategic comp CleanMax (2.54 GW) listed Mar 2026 at IPO EV/EBITDA ~17–21× [🟢]. Sunsure's *project-level* economics track the 80–90% pure-IPP margin band (ACME/NTPC Green); consolidated parent margins **[not available]**.

*Provenance: 6 web · 5 yfinance · 4 inference.*

---

## Section 4 — Valuation & Scenarios

Private → expressed as **conviction, not price target**. Forward EBITDA is **entirely inferred** (⚠️, illustrative): ~700 MW × 17% CUF × ₹4.8/kWh × 85% ≈ Rs 424 cr project EBITDA. Applying CleanMax 17–21× → indicative EV ~Rs 7,200–8,900 cr (~USD 860m–1.06bn). CleanMax's ~USD 660/kW basis on Sunsure's 700 MW → ~USD 460m platform equity, directionally consistent with PG's cost basis. Precedent: Fourth Partner USD 275m equity for 1.5 GW (IFC/ADB/DEG, 2024) [🟢 IFC]. Sub-sector equity IRR ~18–22% [⚠️ inference; safearth cites 20%+ for industrial solar 🟢]; regulatory-cliff downside could compress to 12–15% [⚠️].

| Scenario | Prob | Assumptions | Conviction |
|---|---|---|---|
| Bull | 25% | 2 GW FY27 on track; BESS/RTC premium; OA stable in UP/Mah/Raj; DSCR >1.3× | High — EV ~USD 2–3bn at 5 GW |
| Base | 55% | 1.5 GW FY27; modest spread erosion in 1–2 states; BESS on schedule | Medium — EV ~USD 1–1.5bn at 3–4 GW |
| Bear | 20% | Reg disruption in Mah/UP; BESS delay; covenant/financing slippage | Low — IRR <15%, stranded-cost risk |

**Overall conviction: Medium-High**, conditional on structural protections (senior security, DSRA, waterfall), multi-state regulatory monitoring, and consolidated-leverage diligence.

*Provenance: 3 web · 8 inference (all ⚠️-flagged).*

---

## Section 5 — AIIB-Mandate Alignment & ESG  [ref: aiib-mandate.md]

- **Sector — Energy (direct/strong):** clean-energy transition IPP.
- **Green Infrastructure (primary):** 100% renewable, Paris-aligned; FMO rates it "100% green"; 242 MWp tranche offsets ~230,000 tCO₂/yr [🟢 FMO, PV Tech].
- **Private Capital Mobilization (strong):** 100% private platform crowding in PG equity + commercial debt; AIIB co-lending alongside FMO would extend mobilization.
- **Technology-enabled (partial):** BESS/RTC + energy-management platform.

**ESG:** FMO E&S rating **B+ (medium-high)** — module-supply human-rights, biodiversity, construction safety, possible transmission resettlement; manageable with active monitoring under AIIB ESF [🟢 FMO]. Social: C&I model avoids large agricultural-land displacement. Governance: PE-controlled, founder-managed; independent-director presence **[not available]** [⚠️].

**Verdict: Strong fit.** Most natural AIIB entry = **project-level senior secured debt** (replicating FMO's TN structure), not holdco equity — the OA regulatory cliff is the key conditionality.

*Provenance: 4 web + aiib-mandate.md · 2 inference.*

---

## Section 6 — Key People & Management Quality

| Name | Role | Background | Prov |
|---|---|---|---|
| Shashank Sharma | Founder/Chairman/CEO | IIT-BHU B.Tech Civil; certified data scientist | 🟢 |
| Shantanu Faugaat | Co-founder/COO | operational leadership | 🟢 |
| Manish Mehta | Co-founder/CCO | IIT-Delhi; finance/BFSI | 🟢 |
| Kartikeya Narain Sharma | Co-founder/CBO | BD, asset mgmt, M&A | 🟢 |
| Tarunveer Singh | Co-founder/Head of Projects | EPC/delivery | 🟢 |

PG board nominee, CFO names **[not available]** [⚠️].

**Quality:** Strong execution (~700 MW in ~3–4 IPP years, 4-mo Mahoba, marquee repeat offtakers); well-timed EPC→IPP→BESS/RTC progression; multi-lender bank access. Risks: founder concentration / key-person (Shashank Sharma), no evidenced independent board, compensation undisclosed [⚠️]. **No red flags / litigation found** [🟢 searches].

*Provenance: 6 web · 4 inference.*

---

## Section 7 — Risk Assessment

**Company-specific:**
1. **Open-access regulatory cliff (HIGH — dominant):** OA economics hinge on state CSS/AS/banking/wheeling/ISTS waivers, revisable annually. TN GEOA 2025 imposed 8% banking charge + banned third-party banking [🟢 Mercom]; ISTS step-up 25%→100% (2025–28). Mitigant: 25-yr fixed PPAs lock signed contracts; new builds must absorb higher base charges. Affects all OA developers equally — multi-state spread is Sunsure's partial hedge.
2. **Execution/construction (MED-HIGH):** 2 GW FY27 needs ~1.2 GW from 868 MW under construction + new starts; CARE flags implementation risk; grid/ALMM/land dependencies.
3. **Offtaker credit (MED):** corporates (not DISCOMs) — better payment behavior (~15-day collection per ICRA) but exposed to industrial credit cycles; group-captive equity aligns offtakers.
4. **Leverage/refinancing (MED):** "increasingly leveraged"; SPV debt 70–80% of cost [⚠️]; A- ratings downgradeable on PLF/DSCR miss; 20-yr tenors (DSRA to 2045).
5. **Module/ALMM/BCD (MED):** domestic-sourcing + duty risk; recent 195 MW Suzlon wind order diversifies.
6. **Key-person (MED):** founder-embedded, no public succession plan [⚠️].
7. **Banking/curtailment (LOW-MED):** state banking rules (TN ban precedent).

**Macro:** India rates/credit (MED); INR/USD for PG's USD book (MED, ⚠️); pro-renewable policy tailwind (500 GW by 2030); module-price/BCD (LOW-MED); rising competition from Adani Green/ReNew/NTPC Green/Avaada in OA (MED).

*Provenance: 10 web · 6 inference.*

---

## Verify Before Relying — highest-risk unsourced claims
1. **Consolidated FY25 revenue/EBITDA/net profit/total debt** — biggest gap; rating PDFs only snippet-extracted.
2. **PG acquisition valuation & current mark** — undisclosed; Section 4 USD/kW & EV/EBITDA are illustrative.
3. **Absolute SPV DSCRs** — described qualitatively only.
4. **Consolidated/group debt quantum** — [not available]; per-MW figure from single points.
5. **Green-hydrogen strategy** — aspiration only, no confirmed project.
6. **Board composition / governance / comp** — not public.
7. **O2 Power / JSW precedent multiple** — ⚠️ training, unverified this run.
8. **2 GW FY27 / 5 GW FY30 targets** — rating-confirmed but not reaffirmed post-Jun 2025; large gap vs ~700 MW today.

---

### Orchestrator flags for you
- **Operational capacity:** your brief said ~600 MWp; the worker's primary sourcing (company site + PV Tech, Jun 2026) puts it at **~700–800 MW operational**. Worth reconciling — likely your figure is a few months stale.
- **Comp tier:** `fetch_financials.py` ran live on the five listed proxies (Adani Green, KPI Green, NTPC Green, ACME Solar, Waaree) — all 🟢. The honest limitation flagged is that **no pure-play listed OA/C&I IPP exists**, so every comp is a structural mismatch; KPI Green and (private, just-IPO'd) CleanMax are the least-bad anchors.
- **Thinnest section is Financials** — as expected for a private name. The single highest-value next step would be obtaining the **full CRISIL/CARE/ICRA rating reports** (PDFs, behind snippet extraction) for consolidated P&L, debt and absolute DSCRs.

Want me to (a) push the worker to fully extract the CRISIL/CARE/ICRA rating PDFs for the consolidated financials, (b) build a deeper OA-regulatory-cliff state-by-state matrix (UP/Maharashtra/Rajasthan/TN/Karnataka), or (c) run a Mode S sourcing pass on the private OA/C&I peer set (CleanMax, Fourth Partner, Amp, O2 Power, Radiance, Vibrant) for a comparative shortlist?
