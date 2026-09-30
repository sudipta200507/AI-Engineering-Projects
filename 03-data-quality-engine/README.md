# Data Quality Engine

A reusable data-quality gate for ML pipelines. It profiles missingness, duplicates, data types, numeric ranges and simple distribution statistics, then writes a machine-readable report.

Run `python quality.py path/to/data.csv`.

This project demonstrates that production ML begins with reliable data, not only model selection.

Next experiments: schema contracts, Great Expectations/Pandera integration, drift thresholds and CI checks.