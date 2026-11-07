import re
from PIL import ImageFont
SANS='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
def rows(path):
    s=open(path,encoding='utf-8').read(); out=[]
    for m in re.finditer(r'<text[^>]*>',s):
        tag=m.group(0); xm=re.search(r'x="([\d.]+)"',tag); ym=re.search(r'y="([\d.]+)"',tag); fm=re.search(r'font-size="([\d.]+)"',tag)
        end=s.find('</text>',m.end())
        if end<0 or not xm or not ym: continue
        out.append((float(xm.group(1)),float(ym.group(1)),float(fm.group(1)) if fm else 0,re.sub(r'<[^>]+>','',s[m.end():end])))
    return out
r=rows('files/weekly-report-w45-de-ko/svg/p6-vertiefung.svg')
# chart labels: Korean labels near bars; find rects (bars) x positions
s=open('files/weekly-report-w45-de-ko/svg/p6-vertiefung.svg',encoding='utf-8').read()
rects=re.findall(r'<rect[^>]*>',s)
for rc in rects:
    xm=re.search(r'x="([\d.]+)"',rc); wm=re.search(r'width="([\d.]+)"',rc); ym=re.search(r'y="([\d.]+)"',rc); hm=re.search(r'height="([\d.]+)"',rc)
    if xm and wm and float(wm.group(1))>50:
        print('RECT',rc[:160])
for x,y,fs,t in sorted(r):
    if any(k in t for k in ['가족 돌봄','방문 돌봄','요양원']) or (fs==20.0 and 1800<y<2300):
        print(f"  text x={x} y={y} fs={fs} {t!r}")
f=ImageFont.truetype(SANS,80,index=2)  # 20pt*4 supersample
for lab,x0 in [('가족 돌봄',None),('방문 돌봄',None),('요양원 생활',None)]:
    bb=f.getbbox(lab); print(lab,'ink width/4=',(bb[2]-bb[0])/4)
