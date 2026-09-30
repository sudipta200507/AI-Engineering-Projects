# Document Intelligence Baseline

Extract text from PDFs and classify the document with a lightweight local NLP model.

Put PDFs in `documents/`, install dependencies and run `python extract.py`.

The extraction stage uses PyMuPDF. The classification stage is intentionally simple so you can later replace it with a fine-tuned transformer.

Study document parsing, chunking, text classification, confidence thresholds and human review.