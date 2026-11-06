import xml.etree.ElementTree as ET, re, hashlib, base64
BASE="/home/hatch/workspace/goals/lucernaread-social-media-operations"
def nodes(path):
    tree=ET.parse(path); out=[]
    for el in tree.iter():
        if el.tag.endswith('text'): out.append((float(el.get('x')), float(el.get('y')), ''.join(el.itertext())))
    return out
print("--- dark band texts y 424-542, ED vs W43 p1 ---")
for label,path in [("ED",f"{BASE}/files/weekly-report-w45-ko-ja/svg/p1-pyoji.svg"),("W43",f"{BASE}/files/weekly-report-ko-ja/svg/p1-pyoji.svg")]:
    print(f" {label}:", [(y,t) for x,y,t in nodes(path) if 424<=y<=542])
print("--- image payloads ---")
def imgs(path):
    tree=ET.parse(path); out=[]
    for el in tree.iter():
        if el.tag.endswith('image'):
            href=el.get('{http://www.w3.org/1999/xlink}href') or el.get('href','')
            out.append(href)
    return out
for i,p in enumerate(["p1-pyoji","p2-saenghwal","p3-munhwa","p4-seupocheu","p5-cheongnyeon","p6-gipi","p7-mal","p8-siheom"],1):
    e=imgs(f"{BASE}/files/weekly-report-w45-ko-ja/svg/{p}.svg")
    c=imgs(f"{BASE}/files/weekly-report-w45-ko-core/svg/{p}.svg")
    print(f"p{i}: ED images={len(e)} CORE images={len(c)}")
    for j,(eh,ch) in enumerate(zip(e,c)):
        eb=eh.split(',',1)[1] if ',' in eh else eh
        cb=ch.split(',',1)[1] if ',' in ch else ch
        ej=base64.b64decode(eb); cj=base64.b64decode(cb)
        print(f"  img{j}: b64sha ED={hashlib.sha256(eb.encode()).hexdigest()[:16]} CORE={hashlib.sha256(cb.encode()).hexdigest()[:16]} match={eb==cb} | jpegsha ED={hashlib.sha256(ej).hexdigest()[:16]} CORE={hashlib.sha256(cj).hexdigest()[:16]} jmatch={ej==cj} bytes={len(ej)}/{len(cj)}")
    if len(e)!=len(c): print("  COUNT MISMATCH!")
print("--- credit lines ED ---")
for i,p in enumerate(["p1-pyoji","p2-saenghwal","p3-munhwa","p4-seupocheu","p5-cheongnyeon","p6-gipi","p7-mal","p8-siheom"],1):
    for x,y,t in nodes(f"{BASE}/files/weekly-report-w45-ko-ja/svg/{p}.svg"):
        if '사진:' in t or '그림:' in t or 'Wikimedia' in t: print(f"  p{i} y={y}: {t!r}")
    for x,y,t in nodes(f"{BASE}/files/weekly-report-w45-ko-ja/svg/{p}.svg"):
        if '김장 사진이 아니에요' in t: print(f"  p{i} SSAM-HONEST y={y}: {t!r}")
print("--- ABSTRACT checks ---")
ab=open(f"{BASE}/files/weekly-report-w45-ko-ja/ABSTRACT.txt", encoding='utf-8').read()
print(f"  lines={ab.count(chr(10))} ascii-dquote={ab.count(chr(34))} len={len(ab)}")
print(f"  text: {ab!r}")
alltxt={}
for i,p in enumerate(["p1-pyoji","p2-saenghwal","p3-munhwa","p4-seupocheu","p5-cheongnyeon","p6-gipi","p7-mal","p8-siheom"],1):
    alltxt[i]="\n".join(t for x,y,t in nodes(f"{BASE}/files/weekly-report-w45-ko-ja/svg/{p}.svg"))
joined="\n".join(alltxt.values())
for kw in ["立冬","11月7日","紅葉","最終","週末","キムジャン","始まり","D-17","D-12","KIAタイガース","三連勝","韓史試験","申込み","A2","B2","150"]:
    hits=[i for i in range(1,9) if kw in alltxt[i]]
    print(f"  {kw}: pages {hits}")
for kw in ["タイガース","3連勝","韓国史能力検定試験"]:
    print(f"  {kw}: in-issue? {kw in joined}")
