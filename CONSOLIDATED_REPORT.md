**Executive Summary**

This report consolidates results from `analyze_importer_landscape.ipynb`, the pasted backtest text (from `brief.pdf`), and public-trade surrogates (ImportYeti / ImportGenius summaries) to assess whether companies identified as likely to grow from 2021 have in fact developed larger, more diversified import footprints in 2022+. It also implements a reproducible Segment 2 Upgrade Score (0–100) and provides recommended next steps for definitive verification using paid trade databases (ImportGenius / Panjiva / Datamyne).

**Key conclusions**
- Several companies flagged in the 2021 analysis show structural evidence of growth and multi-country sourcing in 2022+: Eastman Chemical Company, Foster Electric, Ingrasys Technology USA, International Flavors & Fragrances, Arrow Electronics, Pacific American Fish Co., Tradin Organics, and SpaceX (group-level signals).
- A defensible set of Segment 2 upgrade candidates (mid-tier, institutionalized importers with multi-country sourcing) includes: Haldex, UPM Raflatac, Tesa Tape, Hollister, Tablecraft, InterAmerican Coffee, Global Natural Foods, and Magnesita (per free-surrogate evidence).
- Free surrogates (shipment counts, public ImportGenius/ImportYeti listings, supplier-country lists) support structural inference but do not substitute for formal TEU-by-year and per-year distinct-country counts available via paid exports.

**Data & Methods**
- Primary inputs: `analyze_importer_landscape.ipynb`, the backtest text from `brief.pdf`, `importer_normalized_data.csv`, `main.csv.gzip`, and `ports.csv` in the workspace.
- Public surrogates consulted (as described in the notebook/backtest): ImportYeti (free views), ImportGenius public snippets, TradeMo/ImportInfo public summaries. These provide shipment counts and visible supplier-country lists as proxies for TEU and diversification.
- Scoring: the Segment 2 Upgrade Score is computed from four components: Volume Intensity (0–35), Diversification (0–25), Post-2022 Growth (0–25), Structural Stability (0–15). See the Appendix for exact score bands and interpretation.

**Backtest overview (2021 → 2022+)**
- Objective: test whether the 2021-derived signals (TEU proxy + supplier-country diversity) predicted which companies would become stable mid-tier importers by 2022+.
- Outcome: the backtest (as summarized in `brief.pdf`) shows that companies with: (a) near-threshold 2021 TEU proxies (≈150–200) and (b) early multi-country sourcing signals were the easiest to validate as growth cases in 2022–2024 using public surrogates. Examples: Eastman Chemical, Foster Electric, Ingrasys.
- Limitations: exact TEU reconciliation (20' vs 40') and precise per-year distinct-country tallies require paid dataset exports for audit-quality confirmation.

**Segment 2 Upgrade Score — brief**
- Components (quick):
  - Volume Intensity (0–35): TEU or shipment proxy averaged 2023–2024
  - Diversification (0–25): distinct supplier origin countries in 2024
  - Post-2022 Growth (0–25): % TEU growth 2022→2024
  - Structural Stability (0–15): multi-quarter activity, low supplier concentration, multi-port use
- Scoring bands: 0–39 remain Segment 3, 40–59 borderline Segment 2, 60–79 strong Segment 2, 80–100 near Segment 1.

**Applied findings (summary of candidates)**
- Strong Segment 2 candidates (high confidence from free surrogates): Haldex, UPM Raflatac, Tesa Tape, Hollister, Tablecraft, InterAmerican Coffee, Global Natural Foods, Magnesita.
- Strong structural breakouts (closer to Segment 1): International Flavors & Fragrances, Arrow Electronics, Pacific American Fish, Tradin Organics, SpaceX (group-level evidence).
- Not confirmed as upgrades from free sources: Columbia Frame, Jill Acquisition LLC, Precor (declining), some trading entities that require paid-DB lookups.

**Corroboration via public databases**
- Where free surrogates were available we used ImportYeti/ImportGenius public pages and other trade-summary pages to validate shipment counts and supplier-country breadth. For audit-level confirmation (TEU/year and 1:1 country counts) the recommended data sources are ImportGenius (paid exports), Panjiva (S&P), or Descartes Datamyne.



**Appendix**
- Files saved in this workspace/repo: `analyze_importer_landscape.ipynb`, `importer_normalized_data.csv`, `main.csv.gzip`, `ports.csv`, `brief.pdf`, `report_importer_landscape.pptx`, and this `CONSOLIDATED_REPORT.md`.
- Segment 2 scoring details (exact table mapping) are recorded in the notebook and can be exported as a Python function or Excel formula upon request.
- Public sources referenced as surrogates: ImportYeti (public views), ImportGenius (public snippets), TradeMo/ImportInfo.



**Segment Definitions & Visual Context**

- **Segment definitions (exact rules used in `analyze_importer_landscape.ipynb`):**
  - **Segment 1 — High-volume / Low-diversification:** total TEU >= 200 AND top‑2 country share >= 80% (i.e., >=80% TEU sourced from 1–2 countries).
  - **Segment 2 — High-volume / High-diversification:** total TEU >= 200 AND top‑2 country share < 80% (i.e., diversified across 3+ countries to reach 80% of TEU).
  - **Segment 3 — Low-volume / Low-diversification:** total TEU < 200 AND top‑2 country share >= 80% (concentrated small importers).
  - **Segment 4 — Low-volume / High-diversification:** total TEU < 200 AND top‑2 country share < 80% (small but diversified importers).

- **Key numeric thresholds and calculations:**
  - Volume threshold: 200 TEU (used to separate "high" vs "low" volume).
  - Diversification threshold: the number of source countries required to reach 80% cumulative TEU (used to separate low vs high diversification; `threshold_diversification = 3` in the notebook logic).
  - TEU standardization: calculated TEU is parsed and converted to numeric; outliers and zeros are flagged/winsorized where appropriate.

- **Segment summary (interpretation & investment lens):**
  - Segment 1: Large but concentrated — Supply‑chain risk (high volume + single/dual-country dependence).
  - Segment 2: Large and diversified — Resilient / best‑in‑class (preferred cohort for scale + diversification).
  - Segment 3: Small and concentrated — Fragile long tail (low volume and concentrated sourcing).
  - Segment 4: Small but diversified — Promising growth segment (diversified small importers with upgrade potential).

- **Visuals & diagnostics applied in the notebook (for context and reproducibility):**
  - TEU distribution histogram (log–log) and Lorenz curve with Gini coefficient to show heavy tails and concentration.
  - Monthly TEU trend charts (seasonality and volatility checks).
  - Four‑panel pie charts (one quadrant per segment) showing top source countries within each segment.
  - Country dependency heatmaps and stacked bar views showing the number of countries required to reach 80% TEU (proportion of importers by country‑dependency group).
  - Port ↔ country heatmaps and directed graphs (country → port flows) to reveal logistics concentration.
  - Boxplots and Mann–Whitney tests comparing risk/score distributions between segments (e.g., Segment 3 vs 4).
  - Petri‑net / directed graph of upgrade paths (Segment 3 → Segment 1/4, Segment 4 → Segment 2) with edge widths proportional to mean predicted probability.

- **Predictive model notes (early-warning & upgrade models):**
  - A LightGBM early‑warning classifier was trained to predict year‑end Segment 1 using H1 (≤ June) features; primary signals: early TEU (log), top‑2 share, country entropy, TEU volatility, and port concentration.
  - Reported performance (notebook): Test ROC AUC ≈ 0.95; Test PR AUC ≈ 0.867; Segment 1 precision ≈ 0.73, recall ≈ 0.79 at 0.5 threshold — good discrimination under class imbalance.
  - The notebook distills LightGBM teachers into monotonic linear mimics (signed linear weights) to produce interpretable weighted scorers for Segment 1, Segment 2, and Segment upgrade paths.

  - **How this maps to the consolidated analysis:**
  - The Segment rules above were used when labeling companies and when computing the Segment 2 Upgrade Score described earlier. Visual diagnostics listed above are available in `analyze_importer_landscape.ipynb` and can be exported as PNGs for inclusion in slide decks or the final PDF report.



---


**Notebook Figures**

The following figures were generated from `analyze_importer_landscape.ipynb` and saved into the `figs/` folder.
- Figure 1: [figs/figure_01.png](figs/figure_01.png)
- Figure 2: [figs/figure_02.png](figs/figure_02.png)
- Figure 3: [figs/figure_03.png](figs/figure_03.png)
- Figure 4: [figs/figure_04.png](figs/figure_04.png)
- Figure 5: [figs/figure_05.png](figs/figure_05.png)
- Figure 6: [figs/figure_06.png](figs/figure_06.png)
- Figure 7: [figs/figure_07.png](figs/figure_07.png)
- Figure 8: [figs/figure_08.png](figs/figure_08.png)
- Figure 9: [figs/figure_09.png](figs/figure_09.png)
- Figure 10: [figs/figure_10.png](figs/figure_10.png)
- Figure 11: [figs/figure_11.png](figs/figure_11.png)
- Figure 12: [figs/figure_12.png](figs/figure_12.png)
- Figure 13: [figs/figure_13.png](figs/figure_13.png)
- Figure 14: [figs/figure_14.png](figs/figure_14.png)
- Figure 15: [figs/figure_15.png](figs/figure_15.png)
- Figure 16: [figs/figure_16.png](figs/figure_16.png)
- Figure 17: [figs/figure_17.png](figs/figure_17.png)
- Figure 18: [figs/figure_18.png](figs/figure_18.png)
- Figure 19: [figs/figure_19.png](figs/figure_19.png)
- Figure 20: [figs/figure_20.png](figs/figure_20.png)
- Figure 21: [figs/figure_21.png](figs/figure_21.png)
- Figure 22: [figs/figure_22.png](figs/figure_22.png)
- Figure 23: [figs/figure_23.png](figs/figure_23.png)
- Figure 24: [figs/figure_24.png](figs/figure_24.png)
