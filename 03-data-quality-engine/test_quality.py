import pandas as pd
from quality import pd

def test_duplicate_detection(tmp_path):
    path=tmp_path/'sample.csv'; pd.DataFrame({'a':[1,1],'b':['x','x']}).to_csv(path,index=False); df=pd.read_csv(path); assert df.duplicated().sum()==1

def test_missing_detection(tmp_path):
    path=tmp_path/'sample.csv'; pd.DataFrame({'a':[1,None]}).to_csv(path,index=False); df=pd.read_csv(path); assert int(df.isna().sum().sum())==1
