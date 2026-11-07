import xml.etree.ElementTree as ET, hashlib, base64
BASE="/home/hatch/workspace/goals/lucernaread-social-media-operations"
def nodes(path):
    tree=ET.parse(path); out=[]
    for el in tree.iter():
        if el.tag.endswith('text'): out.append((float(el.get('x')), float(el.get('y')), ''.join(el.itertext())))
    return out
print("--- P2 all nodes containing 쌈/아니에요/사진 ---")
for x,y,t in nodes(f"{BASE}/files/weekly-report-w45-ko-ja/svg/p2-saenghwal.svg"):
    if any(k in t for k in ['쌈','아니에요','사진','채소','쌈장']): print(f"  y={y} x={x}: {t!r}")
print("--- P2 nodes y 400-560 (caption zone) ---")
for x,y,t in sorted(nodes(f"{BASE}/files/weekly-report-w45-ko-ja/svg/p2-saenghwal.svg"), key=lambda z:z[1]):
    if 400<=y<=560: print(f"  y={y} x={x}: {t!r}")
print("--- credit continuations p3/p4 ---")
for p in ["p3-munhwa","p4-seupocheu"]:
    print(f" {p}:")
    for x,y,t in sorted(nodes(f"{BASE}/files/weekly-report-w45-ko-ja/svg/{p}.svg"), key=lambda z:z[1]):
        if 'Wikimedia' in t or 'Commons' in t: print(f"   y={y}: {t!r}")
print("--- full image hashes ---")
def imgs(path):
    tree=ET.parse(path); out=[]
    for el in tree.iter():
        if el.tag.endswith('image'):
            href=el.get('{http://www.w3.org/1999/xlink}href') or el.get('href','')
            out.append(href)
    return out
for i,p in enumerate(["p1-pyoji","p2-saenghwal","p3-munhwa","p4-seupocheu","p5-cheongnyeon"],1):
    e=imgs(f"{BASE}/files/weekly-report-w45-ko-ja/svg/{p}.svg"); c=imgs(f"{BASE}/files/weekly-report-w45-ko-core/svg/{p}.svg")
    for j,(eh,ch) in enumerate(zip(e,c)):
        eb=eh.split(',',1)[1]; cb=ch.split(',',1)[1]
        ej=base64.b64decode(eb); cj=base64.b64decode(cb)
        print(f"p{i} img{j} b64 ED={hashlib.sha256(eb.encode()).hexdigest()} match={eb==cb} | jpeg ED={hashlib.sha256(ej).hexdigest()} match={ej==cj} bytes={len(ej)}")
print("--- core P2 ssam caption (for comparison) ---")
for x,y,t in nodes(f"{BASE}/files/weekly-report-w45-ko-core/svg/p2-saenghwal.svg"):
    if any(k in t for k in ['쌈','아니에요','사진']): print(f"  y={y}: {t!r}")
