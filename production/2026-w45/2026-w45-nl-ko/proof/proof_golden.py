import re, os
CORE='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-core/svg'
ED='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-ko/svg'
def page_texts(dire):
    out={}
    for f in sorted(os.listdir(dire)):
        s=open(dire+'/'+f,encoding='utf-8').read()
        els=[]
        for m in re.finditer(r'<text\s+([^>]*)>([^<]*)</text>', s):
            a,t=m.group(1),m.group(2)
            x=re.search(r'x="([0-9.]+)"',a); y=re.search(r'y="([0-9.]+)"',a)
            if x and y: els.append((float(x.group(1)),float(y.group(1)),t))
        els.sort(key=lambda e:e[1])
        out[f]=els
    return out
core=page_texts(CORE); ed=page_texts(ED)
# P7 golden block: lines in right column? Find ZINNEN header then following lines until VOLGENDE WEEK
def golden(els):
    lines=[t for x,y,t in els]
    try: i=lines.index(next(t for t in lines if t.startswith('ZINNEN VAN DE WEEK')))
    except StopIteration: return []
    out=[]
    for t in lines[i+1:]:
        if t.startswith('VOLGENDE WEEK'): break
        out.append(t)
    return out
print("CORE P7 golden raw lines:", golden(core['p7-taal.svg']))
print("ED P7 golden raw lines:", golden(ed['p7-taal.svg']))
# The golden sentences are Dutch sentences with (Pagina N) in the Korean/Chinese translation line? Actually structure: Dutch sentence line(s) + translation line with (Pagina N).
# Reconstruct: in P7, golden section lines alternate? Print P7 lines with y in golden region for both.
for label,dat in [('CORE',core),('ED',ed)]:
    print(f"--- {label} P7 lines y>2000 ---")
    for x,y,t in dat['p7-taal.svg']:
        if y>2000: print(f"  y={y} x={x} {t!r}")
