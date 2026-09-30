import numpy as np
from sklearn.datasets import load_iris
from scipy.stats import ks_2samp
X=load_iris(as_frame=True).frame.drop(columns='target'); rng=np.random.default_rng(42); reference=X.sample(frac=.5,random_state=42); current=X.drop(reference.index)
for col in X.columns:
    stat,p=ks_2samp(reference[col],current[col]); print(f'{col}: KS={stat:.4f}, p={p:.4f}')
