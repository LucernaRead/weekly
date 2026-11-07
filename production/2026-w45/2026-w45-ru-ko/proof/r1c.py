#!/usr/bin/env python3
import re
BASE="/home/hatch/workspace/goals/lucernaread-social-media-operations/files"
CORE=f"{BASE}/weekly-report-w45-ru-core/svg"; ED=f"{BASE}/weekly-report-w45-ru-ko/svg"
def elems(path):
    t=open(path,encoding="utf-8").read(); out=[]
    for m in re.finditer(r"<text([^>]*)>(.*?)</text>",t,re.S):
        a=m.group(1)
        def g(k):
            mm=re.search(k+r'="([^"]*)"',a); return mm.group(1) if mm else ""
        if g("x") and g("y"): out.append((float(g("x")),float(g("y")),m.group(2)))
    return out
def norm(dd):
    txt=[]
    for p in ["p1-pervaya","p2-zhizn","p3-kultura","p4-sport","p5-molodezh","p6-razbor","p7-yazyk","p8-test"]:
        txt.append(" ".join(s for _,_,s in elems(f"{dd}/{p}.svg")))
    return re.sub(r"\s+"," "," ".join(txt))
edn,con=norm(ED),norm(CORE)
p7=elems(f"{ED}/p7-yazyk.svg")
quotes=[s for x,y,s in p7 if x in (65.0,989.0) and y in (1857.0,2002.0,2147.0,2292.0)]
print("== quotes without guillemets ==")
for q in quotes:
    bare=q.strip("«»")
    print(f"  ed={edn.count(bare)} core={con.count(bare)} :: {bare[:70]}")
print("== model paragraph ==")
for label,dd in (("core",CORE),("ed",ED)):
    es=elems(f"{dd}/p8-test.svg")
    # lines in the H box: x>=1451? print lines with y between Primer y and Primer y+250, x in 1451..1900, sorted by y
    prim=[(x,y,s) for x,y,s in es if s.strip().startswith("Пример:")][0]
    print(label,"Primer:",prim)
    box=sorted([(y,s) for x,y,s in es if x>=1451 and prim[1]<y<prim[1]+300], key=lambda t:t[0])
    for y,s in box: print(f"   y={y} {s[:100]}")
    # word count of paragraph lines (exclude header line itself and any trailing non-paragraph?)
    para=" ".join(s for y,s in box)
    print(label,"paragraph words (raw join):",len(para.split()),"::",para[:200])
