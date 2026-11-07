# -*- coding: utf-8 -*-
import re, os
import xml.etree.ElementTree as ET
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE = BASE + "/files/weekly-report-w45-zhtw-core/svg"
ED = BASE + "/files/weekly-report-w45-zh-tw-ko/svg"
W43 = BASE + "/files/weekly-report-zh-tw-ko/svg"
NS="{http://www.w3.org/2000/svg}"
def elems(d,p):
    t=ET.parse(f"{d}/{p}.svg"); out=[]
    for el in t.getroot().iter(NS+"text"):
        out.append((float(el.get("x",0)), float(el.get("y",0)), float(el.get("font-size",0)), el.text or ""))
    return out
print("=== P7 phrase-strip full nodes (y>=1800) ===")
for d,label in [(CORE,"CORE"),(ED,"ED")]:
    print(f"--- {label}")
    for (x,y,sz,s) in elems(d,"p7-lang"):
        if y>=1800 and y<2600 and x<1451:
            print(f"  x={x} y={y} sz={sz}: {s!r}")
print("\n=== Hanzi-order check: core Hanzi string minus furniture vs ed Hanzi string ===")
def is_hanzi(ch):
    o=ord(ch); return (0x4E00<=o<=0x9FFF) or (0x3400<=o<=0x4DBF) or (0xF900<=o<=0xFAFF)
def nodes(d,p):
    t=open(f"{d}/{p}.svg",encoding="utf-8").read()
    return re.findall(r'<text[^>]*>([^<]*)</text>', t)
for p in ["p1-front","p2-life","p3-culture","p4-sport","p5-youth","p6-deep","p7-lang","p8-test"]:
    ch = "".join(ch for n in nodes(CORE,p) for ch in n if is_hanzi(ch))
    eh = "".join(ch for n in nodes(ED,p) for ch in n if is_hanzi(ch))
    # furniture Hanzi substrings in core: badge, footer, pageline
    n = int(re.search(r'p(\d)',p).group(1))
    furn = (["繁體中文正文英語講解"] if p=="p1-front" else []) + ["繁體中文週報繁體中文正文英語講解", "第版共版"]
    cc = ch
    for f in furn:
        assert f in cc, (p,f)
        cc = cc.replace(f, "", 1)
    print(f"{p}: furniture-stripped core Hanzi == ed Hanzi? {cc==eh} (len core-stripped={len(cc)} ed={len(eh)})")
    if cc!=eh:
        import difflib
        for tag,i1,i2,j1,j2 in difflib.SequenceMatcher(None,cc,eh,autojunk=False).get_opcodes():
            if tag!="equal": print(f"   {tag} core[{i1}:{i2}]={cc[max(0,i1-10):i2+10]!r} ed[{j1}:{j2}]={eh[max(0,j1-10):j2+10]!r}")
print("\n=== W43 full Korean disclosure block ===")
for (x,y,sz,s) in elems(W43,"p7-lang"):
    if 1380<=y<=1750 and x>=1451:
        print(f"  y={y}: {s!r}")
print("\n=== ED P7 last-line + box ===")
for (x,y,sz,s) in elems(ED,"p7-lang"):
    if x>=1451 and y>=1600:
        print(f"  x={x} y={y} sz={sz}: {s!r}")
print("\n=== ED P7 teaser nodes (y>=2400) ===")
for (x,y,sz,s) in elems(ED,"p7-lang"):
    if y>=2400:
        print(f"  x={x} y={y} sz={sz}: {s!r}")
