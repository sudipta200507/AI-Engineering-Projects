import io,zipfile,requests,pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
u='https://files.grouplens.org/datasets/movielens/ml-latest-small.zip'; z=zipfile.ZipFile(io.BytesIO(requests.get(u,timeout=30).content)); raw=pd.read_csv(z.open('ml-latest-small/movies.csv')); raw['genres']=raw['genres'].fillna('').str.replace('|',' ',regex=False)
v=TfidfVectorizer(); M=v.fit_transform(raw['genres']); sim=cosine_similarity(M)
title=input('Movie title: '); idx=raw.index[raw.title.str.contains(title,case=False,regex=False)].tolist()
if not idx: raise SystemExit('Movie not found')
i=idx[0]; best=sim[i].argsort()[-11:][::-1][1:]; print(raw.loc[best,['title','genres']].to_string(index=False))
