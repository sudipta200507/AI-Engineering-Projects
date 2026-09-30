# Recommendation System

## Goal
Build an inspectable content-based recommendation baseline and establish a path toward collaborative filtering.

## Dataset
**MovieLens latest-small — GroupLens Research.**
Official page: https://grouplens.org/datasets/movielens/
Exact archive: https://files.grouplens.org/datasets/movielens/ml-latest-small.zip

## Architecture
Movie metadata → genre normalization → TF-IDF representation → cosine similarity → ranked recommendations.

## Run
`pip install -r requirements.txt`
`python train.py`

Enter part of a movie title when prompted.

## Why this baseline
It makes the ranking mechanism transparent before introducing matrix factorization or neural recommenders.

## Next level
Add collaborative filtering, user/item embeddings, implicit-feedback ranking, Precision@K, Recall@K, NDCG and cold-start handling.