# Recommendation System

Build a content-based movie recommender using public MovieLens ratings and item metadata.

The baseline represents items by genre features and ranks candidates with cosine similarity. This makes the recommendation logic inspectable before moving to collaborative filtering or neural recommenders.

Run `pip install -r requirements.txt` then `python train.py`.

Next experiments: user-user collaborative filtering, matrix factorisation, implicit feedback and ranking metrics.