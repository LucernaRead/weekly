import xml.etree.ElementTree as ET, re
BASE="/home/hatch/workspace/goals/lucernaread-social-media-operations"
def nodes(path):
    tree=ET.parse(path); out=[]
    for el in tree.iter():
        if el.tag.endswith('text'): out.append(''.join(el.itertext()))
    return out
pages=["p1-pyoji","p2-saenghwal","p3-munhwa","p4-seupocheu","p5-cheongnyeon","p6-gipi","p7-mal","p8-siheom"]
core={}; ed={}
for p in pages:
    core[p]=nodes(f"{BASE}/files/weekly-report-w45-ko-core/svg/{p}.svg")
    ed[p]=nodes(f"{BASE}/files/weekly-report-w45-ko-ja/svg/{p}.svg")
print("--- core P1 masthead ---")
for t in core["p1-pyoji"]:
    if t.strip()=='Lucerna' or 'VOL.2' in t and 'Lucerna' in t: print(repr(t))
print("--- golden 8 frequencies (substring occurrences across core nodes, per page) ---")
gold=["11월 7일은 입동이에요","절정에 가까운 주말이라고만 말할 수 있어요","김장은 겨울 내내 먹는 김치를 담그는 일이에요","수능까지 17일 남았어요. 오늘이 D-17예요","낮은 길은 더 늦게 물들어요","KIA 타이거즈가 LG 트윈스를 3연승으로 이겼어요","온 나라가 수험생을 응원해요","날짜를 먼저 보세요"]
for g in gold:
    per={}
    for p in pages:
        n=sum(t.count(g) for t in core[p])
        if n: per[p]=n
    print(f"  {g!r} total={sum(per.values())} per={per}")
print("--- essay: H section nodes on core P8 vs edition P8 ---")
for label,d in [("CORE",core),("ED",ed)]:
    p8=d["p8-siheom"]
    # essay starts at '나의 겨울 준비는 김장부터 시작해요.'
    idx=[i for i,t in enumerate(p8) if '나의 겨울 준비는 김장부터 시작해요' in t]
    print(f"  {label} essay-start node idx: {idx} :: {[p8[i][:60] for i in idx]}")
    # essay body: nodes after H head? print nodes containing essay sentences: find '나의 겨울' context: take all nodes from first essay node to footer? Instead: build essay from content8? Use SVG: nodes after the '150.' key node? Simpler: join nodes that are part of H essay column (x>=1451? H is col4?) - print all p8 nodes with x? nodes() lost x; redo below
import xml.etree.ElementTree as ET
def nodesxy(path):
    tree=ET.parse(path); out=[]
    for el in tree.iter():
        if el.tag.endswith('text'): out.append((float(el.get('x')), float(el.get('y')), ''.join(el.itertext())))
    return out
for label,path in [("CORE",f"{BASE}/files/weekly-report-w45-ko-core/svg/p8-siheom.svg"),("ED",f"{BASE}/files/weekly-report-w45-ko-ja/svg/p8-siheom.svg")]:
    ns=nodesxy(path)
    # H essay: texts in col4 (x>=1451) with y between H head (~?) - find '나의 겨울' node y, take following col4 nodes until footer y>2500? Essay nodes are the H body paragraphs
    start=[(x,y,t) for x,y,t in ns if '나의 겨울 준비는 김장부터 시작해요' in t]
    print(f"  {label} essay start: {start}")
    if start:
        sy=start[0][1]
        body=[t for x,y,t in ns if x>=1451 and sy<=y<2500 and 'Lucerna' not in t and '페이지' not in t and 'H ·' not in t and '써 보기' not in t and '쓰기 문제예요' not in t and '150' not in t[:4]]
        # filter: essay paragraphs are serif long lines; print them
        print(f"  {label} col4 body lines from essay start:")
        for x,y,t in ns:
            if x>=1451 and y>=sy and y<2500: print(f"    y={y}: {t[:90]!r}")
