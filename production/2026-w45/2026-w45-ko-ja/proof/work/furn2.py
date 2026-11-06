import xml.etree.ElementTree as ET, re
BASE="/home/hatch/workspace/goals/lucernaread-social-media-operations"
def nodes(path):
    tree=ET.parse(path); out=[]
    for el in tree.iter():
        if el.tag.endswith('text'):
            out.append((float(el.get('x')), float(el.get('y')), el.get('font-size',''), el.get('font-weight',''), el.get('fill',''), el.get('text-anchor',''), ''.join(el.itertext())))
    return out
def rects(path):
    tree=ET.parse(path); out=[]
    for el in tree.iter():
        if el.tag.endswith('rect'):
            out.append((float(el.get('x',0)), float(el.get('y',0)), float(el.get('width',0)), float(el.get('height',0)), el.get('fill','')))
    return out
for label,path in [("ED",f"{BASE}/files/weekly-report-w45-ko-ja/svg/p1-pyoji.svg"),("W43",f"{BASE}/files/weekly-report-ko-ja/svg/p1-pyoji.svg")]:
    print(f"--- {label} dark-band rects y 400-550 ---")
    for r in rects(path):
        if 400<=r[1]<=550: print("   ",r)
    print(f"--- {label} subtitle slot (한국어판) ---")
    for x,y,fs,fw,fill,anc,t in nodes(path):
        if '한국어판' in t: print(f"   x={x} y={y} size={fs} weight={fw} fill={fill} anchor={anc} :: {t!r}")
    print(f"--- {label} masthead Lucerna ---")
    for x,y,fs,fw,fill,anc,t in nodes(path):
        if t.strip()=='Lucerna': print(f"   x={x} y={y} size={fs} weight={fw} fill={fill} anchor={anc}")
print("--- P7 pattern box: ED vs CORE ---")
for label,path in [("ED",f"{BASE}/files/weekly-report-w45-ko-ja/svg/p7-mal.svg"),("CORE",f"{BASE}/files/weekly-report-w45-ko-core/svg/p7-mal.svg")]:
    print(f"  {label}:")
    for x,y,fs,fw,fill,anc,t in nodes(path):
        if 962<y<1250 and x>=1451: print(f"    y={y} :: {t!r}")
