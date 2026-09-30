# Document Intelligence Baseline

## Goal
Extract text from PDFs through a deterministic parsing stage so later NLP models receive structured input.

## Data source
No external corpus is required. Put PDFs you are authorized to process into `documents/`. Do not commit confidential documents.

## Architecture
PDF → PyMuPDF extraction → normalized text → downstream NLP/classification.

The repository intentionally separates extraction from model inference. This mirrors real document-AI systems where parsing failures can be different from model failures.

## Run
`pip install -r requirements.txt`

Put PDFs in `documents/` and run `python extract.py`.

Extracted `.txt` files are written to `output/`.

## Next level
Add OCR for scanned PDFs, layout-aware extraction, tables, document classification, structured JSON extraction, confidence scores and human review.