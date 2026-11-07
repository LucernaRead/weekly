import xml.etree.ElementTree as ET, re
BASE="/home/hatch/workspace/goals/lucernaread-social-media-operations"
def texts(path):
    tree=ET.parse(path); return [''.join(el.itertext()) for el in tree.iter() if el.tag.endswith('text')]
pages=["p1-pyoji","p2-saenghwal","p3-munhwa","p4-seupocheu","p5-cheongnyeon","p6-gipi","p7-mal","p8-siheom"]
for w in ["立冬","生活","文化","体育","青年"]:
    print(f"===== {w} =====")
    tot=0
    for i,p in enumerate(pages,1):
        for t in texts(f"{BASE}/files/weekly-report-w45-ko-ja/svg/{p}.svg"):
            n=t.count(w)
            if n: tot+=n; print(f"  p{i} x{n}: {t[:110]!r}")
    print(f"  TOTAL substring occurrences: {tot}")
# chapter headers
print("===== chapter headers =====")
for i,p in enumerate(pages,1):
    for t in texts(f"{BASE}/files/weekly-report-w45-ko-ja/svg/{p}.svg"):
        if re.search(r'^(생활|문화|스포츠|청년|깊이 읽기|말 공부|시험과 답|다음 주) ·', t): print(f"  p{i}: {t!r}")
# cross-node splice artifacts: document-order concatenation vs node-aware
print("===== splice artifact check (adjacent node pairs) =====")
for target in ["立冬立冬","練習答","翻訳特別措置","翻訳土曜日"]:
    found=[]
    for i,p in enumerate(pages,1):
        ts=texts(f"{BASE}/files/weekly-report-w45-ko-ja/svg/{p}.svg")
        for a,b in zip(ts,ts[1:]):
            if target in (a+b): found.append((i,a[-30:],b[:30]))
        # also check single nodes contain target (real word?)
        for t in ts:
            if target in t: found.append((i,"SINGLE-NODE",t[:100]))
    print(f"  {target}: {found}")
