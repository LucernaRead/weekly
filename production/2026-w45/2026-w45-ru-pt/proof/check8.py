from xml.etree import ElementTree as ET
import re
ED="/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-pt/svg"
CORE="/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-core/svg"
print("=== P6 chart: texts with 34/28/22/16 + rects in chart region ===")
t=ET.parse(f"{ED}/p6-razbor.svg")
els=[]
for el in t.iter():
    tag=el.tag.split('}')[-1]
    if tag=='text':
        txt=''.join(el.itertext()).strip()
        try: y=float(el.get('y')); x=float(el.get('x'))
        except: continue
        els.append((y,x,txt))
    if tag=='rect':
        try: y=float(el.get('y')); x=float(el.get('x')); w=float(el.get('width')); h=float(el.get('height'))
        except: continue
        if 1200<=y<=1850 and w>50: els.append((y,x,f"RECT w={w} h={h} fill={el.get('fill')}"))
for y,x,s in sorted(els):
    if 1200<=y<=1850: print(f"  y={y} x={x} :: {s}")
print("=== P6 chart: check later-drawn rect overlapping label/value ink (draw order) ===")
# list elements in doc order with y in chart region, check any rect after a label text covering x range
seq=[]
for el in ET.parse(f"{ED}/p6-razbor.svg").iter():
    tag=el.tag.split('}')[-1]
    if tag=='text':
        txt=''.join(el.itertext()).strip()
        try: y=float(el.get('y')); x=float(el.get('x'))
        except: continue
        if 1200<=y<=1850: seq.append(('text',x,y,txt))
    if tag=='rect':
        try: y=float(el.get('y')); x=float(el.get('x')); w=float(el.get('width'))
        except: continue
        if 1200<=y<=1850: seq.append(('rect',x,y,f"w={w} fill={el.get('fill')}"))
for s in seq: print("  ",s)
