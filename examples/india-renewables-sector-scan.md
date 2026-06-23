<!--
Example output — aiib-sector-scan (Mode A), run live 2026-06-23 in a clean Claude Code session
(Sonnet subagents, WebSearch + WebFetch + fetch_financials.py all enabled).
Stats: 12 sub-sectors · 2 waves of 6 subsector-researcher workers · 42 web searches · 18 primary-doc
fetches · 47 fetch_financials pulls · ~15 min · 24 turns. Provenance: 46 live (🟢) claims vs 2
training-unverified (⚠️). Listed multiples are live yfinance (FY26); the ⚠️ items are project-level
IRR models, flagged for re-modeling before IC. Reproduce: see ../TESTING.md.
Note: figures are a point-in-time snapshot for illustration — not investment advice (see ../README.md).
-->

Now the synthesized market map.

---

# India · Renewables (Energy) — AIIB Sector Scan (Mode A)

**Coverage:** 12 sub-sectors, full A–I each · **Date:** 2026-06-23 · **Method:** one bounded `subsector-researcher` per sub-sector, 2 waves of 6, primary-source-first, comps verified live via `fetch_financials.py` (yfinance).

**Provenance banner:** Live web + live yfinance pulls were available this run. Auction/tariff/scheme figures are mostly 🟢 (SECI/CERC/MNRE/MoP/PIB + trade press); all listed multiples are 🟢 live yfinance (FY26, 2026-06-23). Project-level capex/O&M/IRR assumptions are largely ⚠️ training-unverified models — flagged as such and to be re-modeled before IC. No connector data used.

---

## 1. Sub-sector deep-dives (digested A–I — full blocks retained in research log)

Each digest keeps the load-bearing numbers and the bad news; the worker outputs above are the full A–I of record.

### ① Utility-scale solar PV (incl. floating) — **Tier A**
- **A.** ~136 GW cumulative solar (Dec 2025); record ~44 GW added FY26 (~34.8 GW ground-mount); ~169 GW awarded pipeline 🟢 [JMK; MNRE via pv-magazine].
- **B.** SECI plain-solar L1 **₹2.54/kWh** (Tranche XI); ₹2.86 solar+ESS (Oct 2025); ~3.0 ¢/kWh — among cheapest globally 🟢 [Mercom; SolarQuarter].
- **C/E.** EBITDA 83–87% verified: AGEL 83.1%, NTPC Green 86.6% 🟢 yfinance. Listed comps rich: **AGEL 33.8x EV/EBITDA, 161x P/E; NTPC Green 45.9x; KPI Green 13.3x; JSW Energy 17.4x** 🟢.
- **F.** Bad news: **Andhra Pradesh PPA renegotiation 2019–22** (₹10,500 cr dispute, payments withheld ~3 yrs; AP HC restored sanctity Mar 2022); Hindenburg/AGEL governance overhang; DISCOM dues 🟢.
- **G.** New-project levered equity IRR ~13–16% INR (~9–11% USD). **H.** DISCOM credit, land, ISTS/curtailment, ALMM/BCD module supply.
- **Tier A** — best contracted-cashflow depth + dealflow; bear case = DISCOM credit + 34–46x listed entry.

### ② Rooftop & C&I solar (PM Surya Ghar + open-access) — **Tier B**
- **A.** PM Surya Ghar: **9.56 GW / 26.2 lakh installs** by Mar 2026 vs 30 GW target (running behind) 🟢 [energetica-india]. C&I open-access ~2.5–3.5 GW/yr.
- **B.** Residential CFA up to ₹78,000; loans repo+50bps (~5.75%); C&I landed OA cost ₹4.30–7.40/kWh across states vs grid ₹6.5–9 🟢 [Mercom Q3-24].
- **E.** KPI Green 13.3x EV/EBITDA (35.5% margin, +40% rev); Tata Power 15.3x; **Sterling & Wilson EPC 3.9% margin, net loss FY26** 🟢.
- **F.** **Gensol Engineering blow-up — SEBI April 2025: ₹977 cr fund diversion, forged rating letters, promoters barred** 🟢 [SEBI via Business Standard/Taxmann]. S&W three loss years.
- **G.** C&I OA levered equity IRR ~18–22% (model). **H.** Open-access charge/banking volatility (cliff risk), net-metering caps, governance.
- **Tier B** — strong demand + IRRs, but state OA regulatory cliff + governance blow-ups.

### ③ Onshore wind (+ OEM/O&M, repowering) — **Tier B**
- **A.** **56.09 GW** installed (Mar 2026); record **6.05 GW** added FY26; NIWE potential 695 GW @120m 🟢 [Enerdata; MNRE].
- **B.** SECI wind L1 recovered to **₹3.67–3.69/kWh** (Feb 2026) from the ₹2.43 floor of 2017–18 🟢 [Mercom; Renewable Watch].
- **E.** Suzlon 26.4x EV/EBITDA (18.4% margin, +44.9% rev, net cash); Inox Wind 17.8x; Inox Green 123.7x (early O&M ramp) 🟢.
- **F.** **2017–20 auction-transition wreck** (additions collapsed to ~1.1 GW; Suzlon near-bankruptcy, ~60% bank haircut, FCCB default); Mytrah distress→ReNew 🟢 [BusinessToday; Windpower Monthly].
- **G.** New-project IRR ~12–15% INR. **H.** Site/PLF scarcity, land/evacuation in TN/GJ/KA, DISCOM credit, OEM concentration.
- **Tier B** — viable post-recovery, but counterparty + cyclical scars.

### ④ Offshore wind — **Tier C**
- **A.** **0 MW operational**; 30 GW-by-2030 aspiration is unachievable; ~37 GW developable (GJ/TN) 🟢 [NIWE; MNRE].
- **B.** **VGF ₹7,453 cr for 1 GW** (GJ+TN); LCOE ~₹9.7/kWh bridged toward ~₹5.5–6.5 net 🟢 [Cabinet/PM-India; Renewable Watch]. Capex ~₹20 cr/MW (≈$2.4m).
- **F.** **Two SECI tenders cancelled Aug 2025** for lack of bids; global precedent (Ørsted ~$5.5bn write-down; UK CfD-5 zero bids) 🟢 [Down to Earth; CNBC].
- **Tier C** — zero track record, no ports/vessels/grid, repeated tender failure; revisit at first financial close.

### ⑤ Solar-wind hybrid / RTC / FDRE (firm RE) — **Tier B**
- **B.** RTC/FDRE clearing **₹4.98–5.08/kWh** (2024–25) vs plain solar ~₹2.5 → ~250bps+ premium; DFR obligations 75/80/90% 🟢 [Mercom; Renewable Watch].
- **F.** **Undersubscription epidemic — 8.5 GW undersubscribed 2024 (5× 2023), storage = 44%; 38.3 GW cancelled 2020–24; 40+ GW PSAs unsigned** as DISCOMs resist ₹5/kWh 🟢 [SauEnergy/SBI Caps]. ReNew RTC-1 commissioning slipped ~6–12 mo.
- **E.** ReNew (RNW) **8.5x EV/EBITDA** is the FDRE-representative comp (D/E 544x); AGEL/NTPC Green 34–46x 🟢. BESS cost collapse (~$130→$55/kWh) aids new awards.
- **Tier B** — structurally the future of Indian RE, but offtake-finalization + DFR-execution risk.

### ⑥ Standalone BESS (grid-scale, tolling) — **Tier B**
- **A.** CEA target ~**47 GW / 236 GWh by 2032**; ~102 GWh tendered in 2025; **VGF Tranche 2 ₹5,400 cr / 30 GWh** 🟢 [CEA; JMK; PIB].
- **B.** Tolling charges collapsed to **₹1.48–1.77 lakh/MW/month** (VGF, 2-hr) from ~₹2.8–3.5 in 2023; capex ~$125/kWh (Ember) 🟢 [SauEnergy; Mercom].
- **E.** No pure play; proxies JSW Energy 17.4x, Tata Power 15.3x, Exide 17.6x, Amara Raja 10.5x 🟢.
- **F.** Pre-commercial — first cohort commissioning 2026; China cell dependence (~95%), ACC-PLI delays (Rajesh Exports exited). **G.** Tolling+VGF IRR ~18–22% (model).
- **Tier B** — high-conviction, but no realized track record + tariff already thin.

### ⑦ Pumped storage hydro (PSP) — **Tier B**
- **A.** **6.2 GW operational** (10 projects), 8.5 GW under construction, 98.3 GW tracked; MoP 2023 PSP guidelines 🟢 [PIB/CEA].
- **B.** First live tolling: **JSW–UPPCL 1.5 GW at ₹77.2 lakh/MW/yr** 🟢 [Energy-Storage.News]. Capex ~₹10 cr/MW (Pinnapuram-implied), 4–6 yr build.
- **F.** Greenko **Pinnapuram** (first off-river closed-loop, ~$1.2bn/1.2 GW) — Unit-1 pump-mode commissioned but **~1 yr behind**; endemic Indian hydro overruns; aggressive PSP-linked bidding flagged as a financial-stress risk 🟢 [Water Power; GreentechLead].
- **E.** NHPC 25.7x, SJVN 17.6x, JSW Energy 17.4x 🟢. **G.** IRR ~12–15%, sinks to <10% on overrun.
- **Tier B** — unambiguous demand, but immature revenue model + construction risk; A-path = Pinnapuram success + competitive standalone tenders.

### ⑧ Small hydro (≤25 MW) — **Tier C**
- **A.** ~5.1 GW installed vs **21 GW potential — only ~24% utilized, stagnant since ~2017**; additions ~58–97 MW/yr 🟢 [MNRE]. New ₹2,584 cr scheme targets just 1.5 GW/5 yrs.
- **B.** State-ERC FiTs ₹4–6/kWh; GBI lapsed ~2017. **F.** **61 hydro projects stuck on forest clearance**; cumulative overruns ₹31,530 cr; Orient Green ticker defunct 🟢 [PRS India; yfinance].
- **G.** IRR 13–15% base but 7–9% on adverse hydrology (a recurring, not tail, outcome).
- **Tier C** — sub-economic at the margin; tariffs lag Himalayan capex; not a PE-scale class.

### ⑨ Green hydrogen & ammonia — **Tier C**
- **A.** NGHM **₹19,744 cr; 5 MMT/yr by 2030**; commercial output ≈ zero (pilots only); **one large FID — AM Green Kakinada (2028)** 🟢 [MNRE; Ammonia Energy].
- **B.** SIGHT Mode-2A green ammonia **₹49.75/kg** (only ~10% over grey); LCOH ~$3.5–5/kg vs grey $1.5–2 🟢 [PV-magazine; CEEW].
- **F.** Global electrolyzer-maker collapse (**Plug Power $1.6bn FY25 loss; Nel, ITM**); offtake near-zero outside MoUs; budget under-disbursed (~₹600 cr) 🟢 [CleanTechnica; IEA; IEEFA].
- **G.** IRR ~6–10% only with subsidy + $600+/t offtake; <5% otherwise.
- **Tier C** — policy aspiration, not yet an investable asset; offtake is the #1 unresolved risk.

### ⑩ Bioenergy: WtE / biomass / CBG — **Tier B (CBG only); WtE & biomass Tier C**
- **A.** ~10.7 GW bio-power; **SATAT massively missed — ~100 CBG plants vs 5,000 target**; **CBO mandate now binding FY26 (1%→5% by FY29)**, ~₹37,500 cr investment pull 🟢 [REGlobal/MoPNG].
- **B.** CERC WtE tariff **₹10.47/kWh**; CBG procurement raised to **85% of CNG (~₹76–81/kg)** 🟢 [SolarQuarter/CERC; REGlobal].
- **E.** Praj 38.5x EV/EBITDA (earnings collapsed, FY25 ₹805 cr write-off); Thermax 51.5x — both EPC, not asset owners 🟢. **F.** WtE failure record (Timarpur, ~half of 14 plants closed, Okhla NGT fines) 🟢 [Scroll/DTE].
- **G.** CBG plant IRR ~18–22% base / ~10–13% bear (feedstock-cost driven).
- **CBG Tier B** (PSU offtake + mandate); **WtE/biomass Tier C** (ULB credit, feedstock volatility, failure record).

### ⑪ Solar PV manufacturing (PLI/ALMM/DCR + glass) — **Tier B**
- **A.** ~120–125 GW module capacity (oversupplied) but **cells only ~26–29 GW (the bottleneck); wafer/poly ~near-zero**; **ALMM List-II (cells) mandatory 1 Jun 2026** creates a domestic-cell demand floor 🟢 [Wood Mackenzie; gosolarindex].
- **C/E.** **Premier Energies EBITDA 30.4%, Waaree 22.3%** (live) — Premier 20.7x, Waaree 14.3x, Borosil 18.1x EV/EBITDA 🟢. Module utilization industry-wide ~25%.
- **F.** **US AD/CVD petition on Indian cells (2025)** threatens Waaree's ~33% US revenue; Chinese price crash; post-IPO de-rating of Waaree/Premier 🟢 [Whalesbook; PV-Tech].
- **G.** Integrated cell+module IRR ~18–26% bull / 10–14% if US access lost.
- **Tier B** — real ALMM/PLI tailwind + top margins, but binary US-export and overcapacity risk; safest entry = ALMM cell-integrated, domestic-tilted (Premier-type).

### ⑫ RE transmission & grid evacuation (TBCB/ISTS) — **Tier A**
- **A.** **₹9.15 lakh crore (~$110bn) transmission plan to 2032**; 45 ISTS-TBCB schemes transferred FY25; GEC Phases 3–4 for +150 GW 🟢 [CEA NEP-T; PIB; T&D India].
- **B/D.** **35-yr fixed availability-based ATC**, pooled PoC counterparty (sovereign-adjacent) — highest revenue quality in Indian infra; ATC ≈ 12–13% of capex/yr 🟢.
- **C/E.** POWERGRID **81.3% EBITDA, 10.8x EV/EBITDA, 4.2% yield** 🟢; Adani Energy Solutions 25.7x (growth + governance premium); PFC/REC financiers at ~5–6x P/E 🟢.
- **F.** Bad news: **ROW/forest-clearance delays** (Khavda II-B +9 mo), one scheme **de-notified**, PGCIL's PSU cost-of-capital edge competes returns down; transmission lags generation (RE curtailment) 🟢 [T&D India].
- **G.** New-TBCB levered equity IRR ~12–14%. **Tier A** — best cashflow structure + proven InvIT exit; risk is execution, not revenue.

---

## 2. Sector synthesis — cross-sub-sector comparison

| # | Sub-sector | New-project levered IRR (INR, modeled) | Tariff / revenue benchmark | Margin (EBITDA) | Cycle / stage | Tier |
|---|---|---|---|---|---|---|
| ① | Utility-scale solar | 13–16% | ₹2.54–2.86/kWh | 83–87% (IPP) | Mature, scaling | **A** |
| ⑫ | RE transmission (TBCB) | 12–14% | 35-yr fixed ATC (~12–13% capex/yr) | ~81–90% | Scaling, proven exits | **A** |
| ⑤ | Hybrid/RTC/FDRE | 12–15% | ₹4.98–5.08/kWh | 65–72% | Fast-growing, frictional | **B** |
| ⑥ | Standalone BESS | 18–22% (w/ VGF) | ₹1.48–1.77 lakh/MW/mo | 85–90% (tolling) | Pre-commercial | **B** |
| ⑦ | Pumped storage (PSP) | 12–15% | ₹77.2 lakh/MW/yr (1st deal) | 70–80% | Early, construction-heavy | **B** |
| ③ | Onshore wind | 12–15% | ₹3.67–3.69/kWh | 75–85% (IPP) | Recovered post-2020 | **B** |
| ② | Rooftop & C&I solar | 18–22% | ₹4.2/kWh C&I; CFA ₹78k | 35–75% (model) | Growing, policy-exposed | **B** |
| ⑪ | Solar manufacturing | 18–26% / 10–14% | ₹18–23/Wp DCR module | 22–30% | Boom→shakeout | **B** |
| ⑩ | Bioenergy — CBG | 18–22% | 85% of CNG (~₹78/kg) | 35–50% | Mandate-driven takeoff | **B** (CBG) |
| ④ | Offshore wind | 12–16% (if it works) | ~₹5.5–6.5/kWh w/ VGF | 55–65% (model) | Pre-tender, failing | **C** |
| ⑧ | Small hydro | 7–15% (hydrology-swung) | ₹4–6/kWh FiT | 70–80% (op.) | Stagnant | **C** |
| ⑨ | Green hydrogen/ammonia | 6–10% (subsidy-dep.) | ₹49.75/kg gr. ammonia | n/m (pre-comm.) | Pre-commercial | **C** |
| — | Bioenergy — WtE/biomass | <12% realized | ₹7–10.47/kWh | 25–45% (volatile) | Failure-prone | **C** |

**Most investable, from the evidence:**
1. **Utility-scale solar (A)** and **RE transmission (A)** are the twin anchors — the deepest contracted-cashflow pools with proven exits. Transmission has the single best revenue structure (35-yr availability ATC, pooled counterparty); solar has the dealflow and verified 83–87% margins. *Bear case:* solar's DISCOM-credit tail (AP precedent) and 34–46x listed entry; transmission's PGCIL cost-of-capital edge competing private IRRs toward ~12%.
2. **The storage cluster — FDRE/RTC, standalone BESS, PSP (all B)** — is where the *next* decade of mandated growth sits (firm/dispatchable RE), with the best modeled IRRs (BESS 18–22%) but no realized track record and live offtake-finalization friction (40+ GW unsigned PSAs). *Bear case:* tariffs already compressed before the first cohort proves cycle fidelity.
3. **Manufacturing (B)** and **CBG (B)** are real but idiosyncratic: manufacturing carries a binary US-AD/CVD risk on top of ~25% utilization; CBG finally has a binding demand mandate (CBO) and AAA PSU offtake but an unproven feedstock-aggregation model.
4. **Avoid/wait (C):** offshore wind (zero execution, cancelled tenders), small hydro (sub-economic, climate-exposed), green hydrogen (no offtake, global sector in distress), WtE/biomass (counterparty + feedstock failure record).

---

## 3. AIIB mandate alignment `[ref: aiib-mandate.md]`

- **Sector match:** All 12 map to **Energy** (sector 1 — clean-energy transition, energy access/security, private-capital mobilization). RE transmission also reads as **Connectivity** infrastructure. [aiib.org/our-work-in-sectors]
- **Theme match:** Strong on **Green Infrastructure** (theme 1 — all Paris-aligned post-2023) and **Private Capital Mobilization** (theme 4 — VGF/TBCB/InvIT structures are textbook crowding-in). Transmission + grid corridors also hit **Connectivity & Regional Cooperation** (theme 2). Manufacturing, BESS and green-H2 hit **Technology-enabled Infrastructure** (theme 3).
- **Climate/Paris:** Every sub-sector is climate-mitigation — directly serves AIIB's >50% climate-finance target and the $17bn/yr-by-2030 scale-up.
- **Verdict:** **Strong fit** for the whole sector. Tiers A/B are the deployable set; Tier-C sub-sectors are mandate-aligned but currently **bankability-out**, not mandate-out. *Bear case on fit:* AIIB's bar is bankability + additionality — the C-tier names (offshore wind, green-H2) need concessional/blended structures, not standard project finance, to be mandate-actionable today.

---

## 4. Anchors — hand-off to `aiib-company-sourcing` (Mode S)

Listed leaders, DFI/PE investees, and recent auction/deal winners per high-conviction sub-sector. These are the graph-expansion seeds (competitors, suppliers, JV partners, fund-siblings) for Mode S.

**① Utility-scale solar (A):** Adani Green (TotalEnergies, GQG), NTPC Green (PSU), **ReNew** (CPPIB, ADIA, GS — Nasdaq), **Greenko** (GIC, ADIA, ORIX — private), Avaada (Macquarie/Brookfield), O2 Power (EQT), Tata Power, KPI Green. *Anchor reason:* SECI allocation leaders + DFI-backed platforms.

**⑫ RE transmission (A):** **POWERGRID** + POWERGRID InvIT, **Adani Energy Solutions**, **IndiGrid** (KKR, GIC — InvIT, the proven DFI-compatible exit), Sterlite Power, Apraava (CLP/CPPIB), Techno Electric, GR Infraprojects. *Anchor reason:* TBCB ATC-share leaders; InvIT roll-up model.

**⑤ Hybrid/RTC/FDRE (B):** **ReNew** (RTC-1 pioneer), **Greenko/AM Green**, Adani Green, JSW Neo, NTPC Green, **Serentica Renewables** (Sterlite/Ares), Hero Future Energies (I Squared, IFC). *Anchor reason:* FDRE auction winners.

**⑥ Standalone BESS (B):** JSW Energy (Fluence JV), Tata Power, Greenko, ReNew, IndiGrid (KKR); cells — Exide (SVOLT JV), Amara Raja, Reliance, Ola. *Anchor reason:* VGF/tender winners + ACC-PLI holders.

**⑦ PSP (B):** **Greenko** (Pinnapuram — GIC/ADIA), JSW Energy (UPPCL deal), NHPC, SJVN, Adani Green, Tata Power. *Anchor reason:* operating/under-construction PSP developers.

**③ Onshore wind (B):** Suzlon, Inox Wind/Inox Green (OEMs); ReNew, Greenko, Apraava (CPPIB), BluPine (Actis), Adani Green, JSW (IPPs). *Anchor reason:* OEM duopoly + DFI-backed IPPs.

**② Rooftop & C&I (B):** Tata Power Solar; **CleanMax** (Warburg Pincus), **Amplus** (PETRONAS), **Fourth Partner** (responsAbility/TPG/Norfund), Radiance (CPPIB), Sunsure, KPI Green. *Anchor reason:* PE/DFI-backed C&I RESCO leaders (the private-heavy pool Mode S should mine).

**⑪ Solar manufacturing (B):** Waaree, Premier Energies, Adani Solar, Vikram Solar (GS legacy), ReNew, Reliance (integrated), Tata Power Solar, Borosil (glass). *Anchor reason:* ALMM List-II cell-integrated leaders.

**⑩ Bioenergy/CBG (B):** **EverEnviro** (EverSource/GGEF — seeking first PE), **GPS Renewables**, Adani TotalEnergies Biomass, IOCL/ONGC CBG JVs, Praj (tech/EPC). *Anchor reason:* corporate-grade CBG developers with PSU offtake.

**Watch-list (C, revisit-on-trigger):** Offshore — NTPC/JSW/Adani (next SECI tender); Green-H2 — Reliance, Adani New Industries, **AM Green** (Greenko/Uniper offtake), ACME, Hygenco (KKR), Ohmium (electrolyzers); Small hydro — SJVN/NHPC + state agencies. Financiers usable as anchors across all: **IREDA, PFC, REC** (RE lending books reveal the private developer universe).

---

### Self-check
- **Wide net?** ✅ 12 sub-sectors, full A–I on every one; tiers assigned *after* evidence.
- **Fan-out shape?** ✅ One `subsector-researcher` each, one level deep, 2 waves of 6, ~3–4 searches each.
- **Bad news?** ✅ Gensol fraud, AP PPA renegotiation, Suzlon near-bankruptcy, offshore tender cancellations, SATAT miss, WtE failures, FDRE undersubscription, Plug Power collapse, Khavda ROW delay.
- **Provenance?** ✅ 🟢 auctions/schemes + live yfinance; ⚠️ on modeled IRR/capex; banner set.
- **Mandate?** ✅ scored from aiib-mandate.md (cited).
- **Hand-off?** ✅ anchors per sub-sector for Mode S.

**Next step:** feed any Tier-A/B sub-sector's economics + anchors into **`aiib-company-sourcing` (Mode S)** to build the ranked private-candidate longlist, then **`aiib-company-dossier` (Mode B)** on the top names.
