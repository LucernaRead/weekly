from xml.etree import ElementTree as ET
def texts(path):
    tree=ET.parse(path); out=[]
    for el in tree.iter():
        if el.tag.split('}')[-1]=='text':
            t=''.join(el.itertext()).strip()
            if t:
                try: y=float(el.get('y')); x=float(el.get('x'))
                except: continue
                out.append((y,x,t))
    return out
pages=["p1-pervaya","p2-zhizn","p3-kultura","p4-sport","p5-molodezh","p6-razbor","p7-yazyk","p8-test"]
ED="/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-pt/svg"
W43="/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-ru-pt/svg"
CORE="/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-core/svg"
print("=== footers edition vs W43 (VOL-normalized) ===")
for i,pg in enumerate(pages,1):
    e=[t for y,x,t in texts(f"{ED}/{pg}.svg") if y>2550]
    w=[t for y,x,t in texts(f"{W43}/{pg}.svg") if y>2550]
    en=[s.replace("VOL.2","VOL.X") for s in e]; wn=[s.replace("VOL.1","VOL.X") for s in w]
    print(f"P{i} MATCH={en==wn} ED={e} W43={w}")
print("=== top strip: first lines y<150 ===")
for label,base in [("ED",ED),("W43",W43),("CORE",CORE)]:
    ts=[t for y,x,t in texts(f"{base}/p1-pervaya.svg") if y<150]
    print(label, ts)
print("=== gloss prefix count 'Nota —' in edition ===")
for i,pg in enumerate(pages,1):
    all_t=[t for y,x,t in texts(f"{ED}/{pg}.svg")]
    n=sum(t.count('Nota —') for t in all_t)
    print(f"P{i} Nota-count={n}")
print("=== section suffix spot: lines containing '· Em ' or '· ' PT suffixes ===")
import re
for i,pg in enumerate(pages,1):
    for y,x,t in texts(f"{ED}/{pg}.svg"):
        if re.search(r'· (Em |Sumário|A palavra|Na |Tema|Agora|Palavras|Prós|Dados|Clínica|Frases|Teste)', t):
            print(f"P{i} y={y} :: {t}")
print("=== page bands ===")
for i,pg in enumerate(pages,1):
    for y,x,t in texts(f"{ED}/{pg}.svg"):
        if t.strip() in ('Vida','Cultura','Esporte','Juventude','Análise','Língua'):
            print(f"P{i} y={y} :: {t}")
