# -*- coding: utf-8 -*-
"""Proof check 2: concatenated-strip diff, P7 tags, readers corner, Latin set, AI."""
import re, os, glob, difflib
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE = BASE + "/files/weekly-report-w45-zhtw-core/svg"
ED = BASE + "/files/weekly-report-w45-zh-tw-ko/svg"
W43 = BASE + "/files/weekly-report-zh-tw-ko/svg"
PAGES = ["p1-front","p2-life","p3-culture","p4-sport","p5-youth","p6-deep","p7-lang","p8-test"]
def nodes(d,p):
    t = open(f"{d}/{p}.svg", encoding="utf-8").read()
    return re.findall(r'<text[^>]*>([^<]*)</text>', t)
def is_hangul(ch):
    o=ord(ch); return 0xAC00<=o<=0xD7A3 or 0x1100<=o<=0x11FF or 0x3130<=o<=0x318F
def strip_ko_lat(s):
    return "".join(ch for ch in s if not is_hangul(ch) and not (ch.isascii() and ch.isalpha()))

print("=== A. Concatenated strip diff (Hangul+Latin removed), core vs ed ===")
for p in PAGES:
    c = strip_ko_lat("".join(nodes(CORE,p)))
    e = strip_ko_lat("".join(nodes(ED,p)))
    sm = difflib.SequenceMatcher(None, c, e, autojunk=False)
    print(f"--- {p}: ratio={sm.ratio():.4f}")
    for tag,i1,i2,j1,j2 in sm.get_opcodes():
        if tag != "equal":
            print(f"  {tag}: CORE[{i1}:{i2}]={c[max(0,i1-15):i2+15]!r} ED[{j1}:{j2}]={e[max(0,j1-15):j2+15]!r}")

print("\n=== B. P7 golden quote -> tag pairing (node order) ===")
import xml.etree.ElementTree as ET
NS="{http://www.w3.org/2000/svg}"
def elems(d,p):
    t=ET.parse(f"{d}/{p}.svg"); out=[]
    for el in t.getroot().iter(NS+"text"):
        out.append((float(el.get("x",0)), float(el.get("y",0)), el.text or ""))
    return out
for d,label in [(CORE,"CORE"),(ED,"ED")]:
    els = elems(d,"p7-lang")
    print(f"--- {label}")
    for i,(x,y,s) in enumerate(els):
        if s.startswith("「") and len(s)>8:
            nxt = els[i+1][2] if i+1<len(els) else ""
            print(f"  y={y} quote={s[:34]!r} next-node={nxt[:40]!r}")

print("\n=== C. Readers corner: Traditional nodes core vs ed (box col x>=1451) ===")
for d,label in [(CORE,"CORE"),(ED,"ED")]:
    els = elems(d,"p7-lang")
    box = [(y,s) for (x,y,s) in els if x>=1451]
    print(f"--- {label} box-col nodes ({len(box)}):")
    for y,s in box:
        print(f"  y={y}: {s[:150]!r}")
print("--- W43 KO disclosure nodes:")
for (x,y,s) in elems(W43,"p7-lang"):
    if "편지" in s or "예시" in s or "독자" in s:
        print(f"  x={x} y={y}: {s[:200]!r}")

print("\n=== D. Latin word-set diff core vs ed ===")
def latwords(d):
    ws=set()
    for p in PAGES:
        txt=" ".join(nodes(d,p))
        for w in re.findall(r"[A-Za-z][A-Za-z']+", txt):
            ws.add(w)
    return ws
cw, ew = latwords(CORE), latwords(ED)
print("ED-only Latin words:", sorted(ew-cw))
print("CORE-only Latin words:", sorted(cw-ew))

print("\n=== E. AI forms ===")
for p in PAGES:
    for n in nodes(ED,p):
        if "데이터를 읽고" in n or "위험을 포착" in n:
            print(f"  ED {p}: {n[:200]!r}")
for p in PAGES:
    for n in nodes(W43,p):
        if "人工智慧" in n:
            print(f"  W43 {p} has 人工智慧: {n[:120]!r}")
print("  W43 AI-topic scan done (blank above = no precedent)")
for p in PAGES:
    for n in nodes(CORE,p):
        if "AI helps read data" in n or "AI inside finance" in n:
            print(f"  CORE {p}: {n[:160]!r}")
print("  P4 full credit:", [n for n in nodes(ED,'p4-sport') if 'Photo:' in n])
print("  ABSTRACT bytes:", open(BASE+"/files/weekly-report-w45-zh-tw-ko/ABSTRACT.txt",encoding="utf-8").read())
print("  ABSTRACT has ASCII double quote:", '"' in open(BASE+"/files/weekly-report-w45-zh-tw-ko/ABSTRACT.txt",encoding="utf-8").read())
print("  ABSTRACT lines:", len(open(BASE+"/files/weekly-report-w45-zh-tw-ko/ABSTRACT.txt",encoding="utf-8").read().strip().splitlines()))
