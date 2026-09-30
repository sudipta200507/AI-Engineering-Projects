from pathlib import Path
import faiss
from sentence_transformers import SentenceTransformer
class LocalRetriever:
    def __init__(self,folder='documents',chunk_size=700,overlap=150):
        self.model=SentenceTransformer('all-MiniLM-L6-v2'); self.texts=[]
        for path in Path(folder).glob('*.txt'):
            raw=path.read_text(encoding='utf-8')
            step=max(1,chunk_size-overlap)
            self.texts.extend(raw[i:i+chunk_size] for i in range(0,len(raw),step))
        if not self.texts: raise ValueError('No authorized .txt documents found.')
        vectors=self.model.encode(self.texts,normalize_embeddings=True); self.index=faiss.IndexFlatIP(vectors.shape[1]); self.index.add(vectors)
    def search(self,query,k=5):
        vector=self.model.encode([query],normalize_embeddings=True); scores,ids=self.index.search(vector,min(k,len(self.texts))); return [(float(s),self.texts[int(i)]) for s,i in zip(scores[0],ids[0])]

if __name__=='__main__':
    r=LocalRetriever(); q=input('Question: ')
    for score,text in r.search(q): print(f'\n[{score:.3f}]\n{text}')