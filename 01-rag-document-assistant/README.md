# Local RAG Document Assistant

## Goal
Build the retrieval layer of a Retrieval-Augmented Generation system before adding an LLM generation layer.

## Data
No external corpus is required. Place `.txt` documents that you are authorized to process in `documents/`. This keeps proprietary information out of Git.

## Architecture
Documents → chunking with overlap → Sentence-Transformer embeddings → FAISS inner-product index → top-k retrieval → evidence passages.

The repository now separates the retrieval implementation into `retriever.py`; `app.py` remains a simple interactive entry point.

## Run
`pip install -r requirements.txt`

Place text files in `documents/` and run `python retriever.py` or `python app.py`.

## Engineering questions

- How does chunk size change retrieval recall?
- Does overlap improve boundary retrieval?
- Which embedding model works best for your corpus?
- How do you evaluate Recall@K before adding an LLM?

## Next level
Add metadata filters, hybrid BM25/vector retrieval, reranking, retrieval benchmarks, citations, answer faithfulness evaluation and a local LLM generation stage.