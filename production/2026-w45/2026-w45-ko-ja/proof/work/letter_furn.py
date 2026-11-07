import xml.etree.ElementTree as ET, re
BASE="/home/hatch/workspace/goals/lucernaread-social-media-operations"
def nodes(path):
    tree=ET.parse(path); out=[]
    for el in tree.iter():
        if el.tag.endswith('text'):
            out.append((float(el.get('x')), float(el.get('y')), el.get('font-size',''), el.get('font-weight',''), el.get('fill',''), el.get('text-anchor',''), ''.join(el.itertext())))
    return out
def raw(path): return open(path, encoding='utf-8').read()
print("===== P7 letter box (x>=1451, 1256<y<1870) in y order =====")
for x,y,fs,fw,fill,anc,t in sorted(nodes(f"{BASE}/files/weekly-report-w45-ko-ja/svg/p7-mal.svg"), key=lambda z:z[1]):
    if x>=1451 and 1256<y<1870: print(f"  y={y} x={x} size={fs} :: {t!r}")
print("===== P7 letter box title + editor note (search) =====")
for x,y,fs,fw,fill,anc,t in nodes(f"{BASE}/files/weekly-report-w45-ko-ja/svg/p7-mal.svg"):
    if '読者の手紙' in t or '編集部' in t or '例文です' in t: print(f"  y={y} x={x} :: {t!r}")
print("===== teaser box texts =====")
for x,y,fs,fw,fill,anc,t in nodes(f"{BASE}/files/weekly-report-w45-ko-ja/svg/p7-mal.svg"):
    if y>2399 and y<2520: print(f"  y={y} :: {t!r}")
print("===== furniture: edition p1 vs W43 p1 =====")
for label,path in [("ED",f"{BASE}/files/weekly-report-w45-ko-ja/svg/p1-pyoji.svg"),("W43",f"{BASE}/files/weekly-report-ko-ja/svg/p1-pyoji.svg")]:
    print(f"--- {label} ---")
    for x,y,fs,fw,fill,anc,t in nodes(path):
        if '解説 — ' in t and 'テキスト' in t: print(f"  BADGE x={x} y={y} size={fs} weight={fw} fill={fill} anchor={anc} :: {t!r}")
        if '韓国語週刊' in t or '韓国語週間' in t or 'VOL.1' in t or 'VOL.2' in t and '週刊' in t: print(f"  FOOTER? y={y} :: {t!r}")
    r=raw(path)
    print("  lines y=392/401:", re.findall(r'<line[^>]*y1="(392|401)"[^>]*>', r)[:4])
    print("  dark rects:", re.findall(r'<rect x="[^"]*" y="(424|478|522)"[^>]*>', r)[:6])
    print("  footer nodes:")
    for x,y,fs,fw,fill,anc,t in nodes(path):
        if y>2600: print(f"    y={y} x={x} size={fs} :: {t!r}")
print("===== footer all 8 pages edition vs W43 =====")
for i,p in enumerate(["p1-pyoji","p2-saenghwal","p3-munhwa","p4-seupocheu","p5-cheongnyeon","p6-gipi","p7-mal","p8-siheom"],1):
    ed=[t for x,y,fs,fw,fill,anc,t in nodes(f"{BASE}/files/weekly-report-w45-ko-ja/svg/{p}.svg") if y>2600]
    w43=[t for x,y,fs,fw,fill,anc,t in nodes(f"{BASE}/files/weekly-report-ko-ja/svg/{p}.svg") if y>2600]
    print(f"p{i} ED: {ed}")
    print(f"p{i} W43: {w43}")
