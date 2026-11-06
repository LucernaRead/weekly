import xml.etree.ElementTree as ET, os
from PIL import Image
GOAL='/home/hatch/workspace/goals/lucernaread-social-media-operations'
ED=GOAL+'/files/weekly-report-w45-zh-tw-ja'
t=ET.parse(ED+'/svg/p7-lang.svg')
print("P7 col3 (x>=1451) text nodes y 1184..1770:")
for e in t.getroot().iter():
    if e.tag.endswith('text'):
        try: x=float(e.get('x')); y=float(e.get('y'))
        except: continue
        if x>=1451 and 1184<=y<=1770:
            print(f"  x={x} y={y} size={e.get('font-size')} :: {''.join(e.itertext())[:70]}")
print("P7 teaser rect + nodes y>2400:")
for e in t.getroot().iter():
    if e.tag.endswith('rect') and e.get('y') and float(e.get('y'))>2400: print('  rect', e.attrib)
    if e.tag.endswith('text'):
        try: y=float(e.get('y'))
        except: continue
        if y>2400: print(f"  text y={y} :: {''.join(e.itertext())[:70]}")
print("P8 last nodes (max y):")
t8=ET.parse(ED+'/svg/p8-test.svg'); ns=[]
for e in t8.getroot().iter():
    if e.tag.endswith('text'):
        try: ns.append((float(e.get('y')), e.get('font-size'), ''.join(e.itertext())[:60]))
        except: pass
for y,s,tx in sorted(ns)[-6:]: print(f"  y={y} size={s} :: {tx}")
# Card pixel measurement P7
im=Image.open(ED+'/cards/p7-lang.png').convert('RGB'); print('card size', im.size)
px=im.load()
def dark(x,y):
    r,g,b=px[x,y]; return (r+g+b)/3 < 110
last_ink=None
for y in range(1700,1790):
    if any(dark(x,y) for x in range(1460,1880)): last_ink=y
print('P7 card: last dark-ink row in box x-range =', last_ink)
# border row: rows where many pixels are close to #d8cfb4 (216,207,180)
for y in range(1755,1770):
    cnt=sum(1 for x in range(1455,1885) if abs(px[x,y][0]-216)<12 and abs(px[x,y][1]-207)<12 and abs(px[x,y][2]-180)<12)
    print(f'  row {y}: border-tan pixels={cnt}')
