# ML Model Monitoring

A small monitoring lab for detecting data drift and comparing model performance across reference and current datasets.

The baseline creates a reference/current split from the Iris dataset, computes per-feature distribution statistics and trains a classifier for comparison.

Run `pip install -r requirements.txt` then `python monitor.py`.

Next experiments: Evidently, PSI, KS tests, alert thresholds, model registry integration and scheduled monitoring.