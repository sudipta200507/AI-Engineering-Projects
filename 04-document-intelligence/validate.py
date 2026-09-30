from pathlib import Path

def validate_extracted_text(folder='output',min_chars=50):
    results=[]
    for path in Path(folder).glob('*.txt'):
        text=path.read_text(encoding='utf-8',errors='ignore').strip(); results.append({'file':path.name,'characters':len(text),'usable':len(text)>=min_chars})
    return results

if __name__=='__main__':
    for row in validate_extracted_text(): print(row)