import xml.etree.ElementTree as ET, re
from collections import Counter, defaultdict
BASE="/home/hatch/workspace/goals/lucernaread-social-media-operations"
def texts(path):
    tree=ET.parse(path); return [''.join(el.itertext()) for el in tree.iter() if el.tag.endswith('text')]
HAN=re.compile(r'[\u4E00-\u9FFF]+')
KANA=re.compile(r'[\u3040-\u30FF]')
pages=["p1-pyoji","p2-saenghwal","p3-munhwa","p4-seupocheu","p5-cheongnyeon","p6-gipi","p7-mal","p8-siheom"]
allnodes=[]
for i,p in enumerate(pages,1):
    for t in texts(f"{BASE}/files/weekly-report-w45-ko-ja/svg/{p}.svg"):
        allnodes.append((i,t))
runs=Counter(); contexts=defaultdict(list)
for i,t in allnodes:
    for m in HAN.finditer(t):
        runs[m.group()]+=1
        if len(contexts[m.group()])<3: contexts[m.group()].append((i,t))
print(f"distinct Han runs: {len(runs)} total occurrences: {sum(runs.values())}")
for r,c in sorted(runs.items()):
    print(f"{c:4d}  {r}   e.g. p{contexts[r][0][0]}: {contexts[r][0][1][:80]!r}")
# simplified-only char panel
panel="红说话让过发对为认识语译练读汉观见车东头简体发与发"
print("\n--- simplified-only char hits ---")
for ch in sorted(set(panel)):
    hits=[(i,t) for i,t in allnodes if ch in t]
    print(f"{ch}: {len(hits)} hits")
    for i,t in hits[:3]: print(f"    p{i}: {t[:100]!r}")
# P1 badge nodes containing 解説 — 
print("\n--- P1 nodes containing 解説 — ---")
for t in texts(f"{BASE}/files/weekly-report-w45-ko-ja/svg/p1-pyoji.svg"):
    if '解説 — ' in t: print(repr(t))
