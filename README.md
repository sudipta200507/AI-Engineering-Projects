# AI Engineering Projects

A systems-oriented AI engineering laboratory focused on what happens **around** a model: retrieval, data quality, document processing, recommendation, monitoring and usable interfaces.

## Project map

| Project | Capability | Data/source |
|---|---|---|
| 01 | Local RAG document assistant | User-supplied documents |
| 02 | Recommendation system | GroupLens MovieLens |
| 03 | Data quality engine | User-supplied CSV |
| 04 | Document intelligence | User-supplied PDFs |
| 05 | ML model monitoring | Scikit-learn Iris + generated reference/current split |

## Exact open-source sources

- MovieLens latest-small — GroupLens: https://grouplens.org/datasets/movielens/ — direct ZIP: https://files.grouplens.org/datasets/movielens/ml-latest-small.zip
- RAG: no external corpus is required. Put documents you are authorized to process in `documents/`.
- Data Quality: no external dataset required; bring an authorized CSV.
- Document Intelligence: no external dataset required; bring authorized PDFs.
- Model Monitoring: the baseline uses scikit-learn's public Iris dataset generated through `sklearn.datasets.load_iris`, so there is no separate download URL.

## Architecture philosophy

These projects demonstrate a production-oriented separation of concerns:

**ingestion → validation → representation → model/service → evaluation → observability**

The repository deliberately avoids pretending that an LLM alone is an AI system. Retrieval quality, data contracts, document parsing, ranking and monitoring are first-class engineering problems.

## Run

Every project has its own README and requirements file. Create a virtual environment, install dependencies, then run the documented entry point.

## What to extend

- RAG: chunking experiments, metadata filtering, reranking, retrieval evaluation, citations and answer evaluation.
- Recommendations: collaborative filtering, matrix factorization and ranking metrics.
- Data quality: schema contracts, drift detection and CI quality gates.
- Documents: OCR, layout-aware parsing, classification and structured extraction.
- Monitoring: PSI/KS tests, model performance tracking, alerts and experiment registry integration.

## Engineering standard

No proprietary corpus is required. No sensitive documents should be committed. Generated embeddings, model artifacts and local input data remain outside Git history.
