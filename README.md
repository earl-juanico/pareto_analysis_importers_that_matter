# pareto_analysis_importers_that_matter

This repository contains the importer-landscape analysis used to identify and validate mid-tier importers that are scaling up through increased volume and geographic diversification.

Key contents
- `analyze_importer_landscape.ipynb`, `exam1.ipynb`: interactive notebooks implementing data cleaning, segmentation, visual diagnostics, and predictive models.
- `importer_normalized_data.csv`, `ports.csv`, `main.csv.gzip`: datasets used for the analysis (large raw CSV stored with Git LFS as `main.csv.gzip`).
- `CONSOLIDATED_REPORT.md`: consolidated narrative of findings and segment definitions.
- `figs/`: extracted figures from the notebook (PNG).

Main insight
- Importer scale‑up is strongly associated with both increased TEU (volume) and greater supplier‑country diversification. The LightGBM early‑warning model (trained on H1 signals) reliably ranks importers by year‑end Segment 1 risk (high‑volume, concentrated importers) and surfaces upgrade candidates (Segment 3/4 → 2/1) when combined with diversification metrics.

Backtest highlights
- Early‑warning classifier (H1 features → year‑end Segment 1):
  - Test ROC AUC: ≈ 0.9461
  - Test PR AUC: ≈ 0.8667
  - Classification (threshold 0.5):

Confusion matrix (approximate, test set)

| Actual \ Predicted | Positive (Segment 1) | Negative |
|---:|---:|---:|
| Positive (175) | TP = 138 | FN = 37 |
| Negative (855) | FP = 51 | TN = 804 |

- Precision (Segment 1): ≈ 0.7302; Recall: ≈ 0.7886; F1: ≈ 0.7582
- Overall accuracy: ≈ 0.9146

Why this matters
- The model's strong ranking performance (ROC AUC ≈ 0.95) and class‑imbalance robustness (PR AUC ≈ 0.87) mean that a short, actionable Top‑K list (e.g., Top‑50 candidates) can be produced early in the year to target monitoring, outreach, or due diligence for potential upgrade/scale opportunities.

Reproducibility notes
- Figures in `figs/` were extracted from `exam1.ipynb` and are embedded or linked in `CONSOLIDATED_REPORT.md`.
- Large raw exports should be kept outside the repo; use Git LFS (already configured) if you must store compressed paid‑DB exports.

Next steps
- To produce an audit‑grade ranked upgrade list, export TEU and supplier‑country breakdowns from a paid trade database (ImportGenius/Panjiva/Datamyne) and run the scoring script (available in the notebooks). The notebooks include a ready‑to‑adapt scoring pipeline and a PDF export script.
