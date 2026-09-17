from pathlib import Path
import csv

from qct_reliability.core import sha256_file

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "data" / "manifest.csv"
URL = "https://docs.huduser.gov/portal/datasets/qct/qct_data_{year}.xlsx"

rows = []
for path in sorted(RAW.glob("qct_data_*.xlsx")):
    year = path.stem.rsplit("_", 1)[-1]
    rows.append({"year": year, "filename": path.name, "bytes": path.stat().st_size,
                 "sha256": sha256_file(path), "source_url": URL.format(year=year)})
with OUT.open("w", newline="", encoding="utf-8") as stream:
    writer = csv.DictWriter(stream, fieldnames=rows[0].keys())
    writer.writeheader(); writer.writerows(rows)
print(OUT)
