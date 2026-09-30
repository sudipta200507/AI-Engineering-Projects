import os
import faiss
from sentence_transformers import SentenceTransformer
files=[os.path.join('documents',f) for f in os.listdir('documents')] if os.path.isdir('documents') else []
texts=[]
for f in files:
 if f.endswith('.txt'):
  with open(f,encoding='utf-8') as h: raw=h.read()
  texts += [raw[i:i+700] for i in range(0,len(raw),550)]
if not texts: raise SystemExit('Add .txt files to documents/.')
model=SentenceTransformer('all-MiniLM-L6-v2'); emb=model.encode(texts,normalize_embeddings=True); index=faiss.IndexFlatIP(emb.shape[1]); index.add(emb)
q=input('Question: '); qe=model.encode([q],normalize_embeddings=True); scores,ids=index.search(qe,3)
for score,i in zip(scores[0],ids[0]): print('\n--- score',round(float(score),3),'---\n',texts[int(i)])
