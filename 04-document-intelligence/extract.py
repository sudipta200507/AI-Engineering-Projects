import os,fitz
os.makedirs('output',exist_ok=True); files=[f for f in os.listdir('documents') if f.lower().endswith('.pdf')] if os.path.isdir('documents') else []
if not files: raise SystemExit('Put PDFs in documents/.')
for name in files:
 doc=fitz.open(os.path.join('documents',name)); text='\n'.join(page.get_text() for page in doc); out=os.path.splitext(name)[0]+'.txt'; open(os.path.join('output',out),'w',encoding='utf-8').write(text); print(name,'->',out,len(text),'chars')
