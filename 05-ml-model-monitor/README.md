# ML Model Monitoring

## Goal
Demonstrate the first layer of ML observability: compare reference and current feature distributions and report model performance.

## Data source
The baseline uses scikit-learn's built-in Iris dataset through `sklearn.datasets.load_iris`, so no external download is required.

## Architecture
Reference/current split → feature distribution comparison → model training → held-out evaluation → monitoring output.

## Run
`pip install -r requirements.txt`

`python monitor.py`

## Why monitoring matters
A model can remain unchanged while the world around it changes. Data drift, label drift and performance degradation can turn a previously acceptable model into an unreliable system.

## Next level
Add PSI/KS tests, rolling windows, label-delay handling, model-performance tracking, alert thresholds, dashboards and scheduled monitoring.
