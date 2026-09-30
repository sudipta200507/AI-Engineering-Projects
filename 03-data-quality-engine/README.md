# Data Quality Engine

## Goal
Turn raw CSV inspection into a repeatable quality gate for ML pipelines.

## Data source
No external dataset is required. Provide an authorized CSV file. This avoids bundling potentially sensitive business data.

## Checks
- row/column counts
- duplicate rows
- missing values by column
- data types
- numeric summary statistics

## Run
`pip install -r requirements.txt`

`python quality.py path/to/data.csv`

The command writes `quality_report.json`.

## Engineering value
Data quality is upstream of model quality. A model trained on broken types, unexpected nulls or duplicate records can produce misleading results even when the algorithm is correct.

## Next level
Add schema contracts, configurable thresholds, Pandera/Great Expectations integration, distribution drift, CI failure gates and machine-readable validation status.