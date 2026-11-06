import re, ast, xml.etree.ElementTree as ET
BASE="/home/hatch/workspace/goals/lucernaread-social-media-operations"
# Parse gloss()/glossline() call first-arg strings via AST (handles multiline/concat? check)
def calls(path, func):
    src=open(path, encoding='utf-8').read()
    tree=ast.parse(src); out=[]
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr==func and node.args:
            try: out.append(ast.literal_eval(node.args[0]))
            except Exception as e: out.append(f"<NONLIT {e}>")
    return out
for label,root in [("ED",f"{BASE}/hidden_files/weekly-report-w45-ko-ja-build"),("CORE",f"{BASE}/hidden_files/weekly-report-w45-ko-build")]:
    print(f"===== {label} =====")
    tot_items=0; tot_boxes=0
    for f in ["content12","content34","content56"]:
        gs=calls(f"{root}/{f}.py","gloss")
        items=sum(len([x for x in g.split("·") if x.strip()]) for g in gs)
        print(f"  {f}: gloss boxes(calls)={len(gs)} items(split ·)={items}")
        tot_items+=items; tot_boxes+=len(gs)
        gl=calls(f"{root}/{f}.py","glossline")
        print(f"    glossline calls={len(gl)}")
    print(f"  TOTAL gloss items={tot_items} boxes={tot_boxes}")
    g7=calls(f"{root}/content7.py","glossline")
    print(f"  content7 glosslines={len(g7)} items={[len([x for x in g.split('·') if x.strip()]) for g in g7]}")
    for g in g7: print(f"    P7 glossline: {g!r}")
# Rendered nodes
def texts(path):
    tree=ET.parse(path); return [''.join(el.itertext()) for el in tree.iter() if el.tag.endswith('text')]
pages=["p1-pyoji","p2-saenghwal","p3-munhwa","p4-seupocheu","p5-cheongnyeon","p6-gipi","p7-mal","p8-siheom"]
for i,p in enumerate(pages,1):
    ed=texts(f"{BASE}/files/weekly-report-w45-ko-ja/svg/{p}.svg")
    co=texts(f"{BASE}/files/weekly-report-w45-ko-core/svg/{p}.svg")
    ed_start=sum(1 for t in ed if t.startswith("解説 — "))
    co_start=sum(1 for t in co if t.startswith("译注｜"))
    ed_sub=sum(t.count("解説 — ") for t in ed)
    co_sub=sum(t.count("译注｜") for t in co)
    dbl=sum(1 for t in ed if t.count("解説 — ")>=2)
    print(f"p{i}: ED start={ed_start} substr={ed_sub} double={dbl} | CORE start={co_start} substr={co_sub}")
