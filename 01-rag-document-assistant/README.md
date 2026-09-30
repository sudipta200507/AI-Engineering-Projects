# Local RAG Document Assistant

## Goal
Build a local retrieval pipeline that finds relevant passages from documents before an answer-generation layer is added.

## Data source
No external corpus is required. Put `.txt` documents you are authorized to process into `documents/`. This keeps the project reproducible without distributing proprietary material.

## Architecture
Documents → chunking → sentence-transformer embeddings → FAISS vector index → top-k retrieval → retrieved evidence.

The current baseline deliberately stops at retrieval so retrieval quality can be measured independently of an LLM.

## Run
`pip install -r requirements.txt`

Place text files in `documents/`, then run `python app.py`.

## Why this is AI engineering
A useful RAG system is not simply an LLM prompt. Retrieval quality, chunk boundaries, embedding choice, metadata, ranking and evaluation determine what evidence reaches the model.

## Next level
Add metadata filtering, hybrid BM25/vector retrieval, reranking, retrieval recall@k, answer faithfulness evaluation, citations and a local LLM generation layer.