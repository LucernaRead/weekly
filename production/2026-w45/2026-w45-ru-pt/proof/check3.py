import re
from xml.etree import ElementTree as ET
NS={'s':'http://www.w3.org/2000/svg'}
def texts(path):
    tree=ET.parse(path); out=[]
    for el in tree.iter():
        tag=el.tag.split('}')[-1]
        if tag=='text':
            t=''.join(el.itertext()).strip()
            if t:
                try: y=float(el.get('y')); x=float(el.get('x'))
                except: continue
                out.append((y,x,t,el.get('font-size'),el.get('font-weight'),el.get('fill')))
    return out
for label,path in [("W45-PT","/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-pt/svg/p1-pervaya.svg"),
 ("W43-PT","/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-ru-pt/svg/p1-pervaya.svg"),
 ("W45-CORE","/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-core/svg/p1-pervaya.svg")]:
    print(f"===== {label} =====")
    for y,x,t,fs,fw,fill in sorted(texts(path)):
        if 300<=y<=400:
            print(f"  y={y} x={x} fs={fs} fw={fw} fill={fill} :: {t}")
    print("  -- bottom y>2550 --")
    for y,x,t,fs,fw,fill in sorted(texts(path)):
        if y>2550: print(f"  y={y} x={x} fs={fs} :: {t}")
    # masthead: largest font lines
    print("  -- masthead candidates (fs>=60) --")
    for y,x,t,fs,fw,fill in sorted(texts(path)):
        try:
            if float(fs or 0)>=60: print(f"  y={y} x={x} fs={fs} fw={fw} :: {t}")
        except: pass
