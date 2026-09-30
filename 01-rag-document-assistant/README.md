# RAG Document Assistant

A local retrieval-augmented generation foundation: ingest text files, chunk them, create embeddings and retrieve the most relevant passages for a question.

Run:
```bash
pip install -r requirements.txt
python app.py
```

Put `.txt` documents in `documents/`. The system uses sentence-transformers for embeddings and FAISS for vector retrieval. No document is sent to an external API by this baseline.

Study chunking, embedding spaces, cosine similarity, top-k retrieval, metadata and retrieval evaluation.