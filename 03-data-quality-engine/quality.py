import sys,json,pandas as pd
if len(sys.argv)!=2: raise SystemExit('Usage: python quality.py data.csv')
df=pd.read_csv(sys.argv[1]); numeric=df.select_dtypes('number')
report={'rows':len(df),'columns':len(df.columns),'duplicate_rows':int(df.duplicated().sum()),'missing_by_column':df.isna().sum().to_dict(),'dtypes':df.dtypes.astype(str).to_dict(),'numeric_summary':numeric.describe().round(4).to_dict()}
with open('quality_report.json','w',encoding='utf-8') as f: json.dump(report,f,indent=2,default=str)
print(json.dumps({'rows':report['rows'],'columns':report['columns'],'duplicates':report['duplicate_rows']},indent=2)); print('Wrote quality_report.json')
