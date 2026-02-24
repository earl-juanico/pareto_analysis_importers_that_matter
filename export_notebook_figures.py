#!/usr/bin/env python3
"""
Execute `analyze_importer_landscape.ipynb`, extract PNG outputs from executed cells, save them to `figs/`,
and append a markdown section with image links to CONSOLIDATED_REPORT.md.

Notes:
- If `main.csv` is missing but `main.csv.gzip` exists, this script will temporarily decompress
  `main.csv.gzip` to `main.csv.temp` for notebook execution and remove it afterwards.
- Requires: nbformat, nbconvert
"""
import os
import sys
import io
import gzip
import base64
from pathlib import Path

try:
    import nbformat
    from nbconvert.preprocessors import ExecutePreprocessor
except Exception as e:
    print("Missing nbformat/nbconvert. Install with: pip install nbformat nbconvert")
    raise

ROOT = Path(__file__).resolve().parent
NB_PATH = ROOT / "analyze_importer_landscape.ipynb"
REPORT = ROOT / "CONSOLIDATED_REPORT.md"
FIGS_DIR = ROOT / "figs"
FIGS_DIR.mkdir(exist_ok=True)

# If main.csv is missing but main.csv.gzip exists, decompress temporarily
MAIN_CSV = ROOT / "main.csv"
MAIN_GZIP = ROOT / "main.csv.gzip"
TEMP_MAIN = None
if not MAIN_CSV.exists() and MAIN_GZIP.exists():
    TEMP_MAIN = ROOT / "main.csv.temp"
    print(f"Decompressing {MAIN_GZIP} -> {TEMP_MAIN} (temporary)")
    with gzip.open(MAIN_GZIP, "rb") as rf, open(TEMP_MAIN, "wb") as wf:
        wf.write(rf.read())
    # create a symlink named main.csv pointing to temp file so notebook can read it
    try:
        os.symlink(str(TEMP_MAIN.name), str(MAIN_CSV))
    except Exception:
        # fallback: copy
        import shutil
        shutil.copy(TEMP_MAIN, MAIN_CSV)

print(f"Executing notebook: {NB_PATH}")
with open(NB_PATH, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
try:
    ep.preprocess(nb, {'metadata': {'path': str(ROOT)}})
except Exception as e:
    print("Notebook execution raised an exception:", e)
    # proceed to attempt to extract any images produced before the error

img_count = 0
md_lines = ["\n**Notebook Figures**\n\nThe following figures were generated from `analyze_importer_landscape.ipynb` and saved into the `figs/` folder.\n"]
for i, cell in enumerate(nb.cells, start=1):
    outputs = cell.get('outputs', []) if isinstance(cell, dict) else []
    for out in outputs:
        data = out.get('data', {})
        if not data:
            continue
        png = data.get('image/png')
        if png:
            img_count += 1
            img_bytes = base64.b64decode(png)
            fname = FIGS_DIR / f"figure_{img_count:02d}.png"
            with open(fname, "wb") as wf:
                wf.write(img_bytes)
            md_lines.append(f"- Figure {img_count}: [figs/figure_{img_count:02d}.png](figs/figure_{img_count:02d}.png)\n")

if img_count == 0:
    md_lines.append("- No PNG outputs were found in the executed notebook.\n")

# Append the markdown block to the consolidated report
with open(REPORT, "a", encoding="utf-8") as rf:
    rf.write("\n---\n\n")
    rf.writelines([l + "\n" if not l.endswith("\n") else l for l in md_lines])

print(f"Extracted {img_count} images to {FIGS_DIR}")

# Clean up temporary main.csv if we created one
if TEMP_MAIN is not None:
    try:
        if MAIN_CSV.is_symlink():
            MAIN_CSV.unlink()
        else:
            MAIN_CSV.unlink()
        TEMP_MAIN.unlink()
        print("Removed temporary decompressed main.csv files")
    except Exception:
        print("Warning: failed to fully remove temporary main.csv files")

print("Done.")
