import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
D=load_iris(as_frame=True).frame; X=D.drop(columns='target'); y=D.target
ref,cur=train_test_split(X,test_size=.5,random_state=42); print('Feature drift summary')
for c in X.columns:
 a,b=ref[c].mean(),cur[c].mean(); print(c,'reference_mean=',round(a,4),'current_mean=',round(b,4),'delta=',round(b-a,4))
xt,xv,yt,yv=train_test_split(X,y,test_size=.2,random_state=42,stratify=y); m=RandomForestClassifier(n_estimators=200,random_state=42).fit(xt,yt); print('Reference model accuracy:',accuracy_score(yv,m.predict(xv)))
