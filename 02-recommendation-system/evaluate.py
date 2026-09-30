import io,zipfile,requests,pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
u='https://files.grouplens.org/datasets/movielens/ml-latest-small.zip'; z=zipfile.ZipFile(io.BytesIO(requests.get(u,timeout=30).content)); movies=pd.read_csv(z.open('ml-latest-small/movies.csv')); movies['genres']=movies['genres'].fillna('').str.replace('|',' ',regex=False)
M=TfidfVectorizer().fit_transform(movies['genres']); sim=cosine_similarity(M)
coverage=(sim.sum(axis=1)>0).mean(); print(f'catalog coverage: {coverage:.3f}'); print('Mean non-self similarity:',((sim.sum(axis=1)-1)/(len(movies)-1)).mean())