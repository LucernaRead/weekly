#!/usr/bin/env python3
"""Reproof R1b: answer-column-only P8 dash-parse, P7 quotes, model words, numbering extras."""
import re, collections
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
pat=re.compile(r"^(\d+)\.\s*(.*)$")
def anskeymap(dd):
    m={}
    for x,y,s in elems(f"{dd}/p8-test.svg"):
        if x in (65.0,527.0,989.0,1451.0) and y>1300:
            mm=pat.match(s.strip())
            if mm:
                rest=mm.group(2)
                k,n=(rest.split(" — ",1)+[""])[:2] if " — " in rest else (rest,"")
                m[int(mm.group(1))]=(k,n)
    return m
ck,ek=anskeymap(CORE),anskeymap(ED)
print(f"answer-col lines: core={len(ck)} ed={len(ek)} missing={sorted(set(ck)-set(ek))} extra={sorted(set(ek)-set(ck))}")
kd=[n for n in sorted(set(ck)&set(ek)) if ck[n][0]!=ek[n][0]]; print("answer-col dash keydiffs:",kd)
for n in kd: print(f"  {n}: core={ck[n]!r}\n      ed  ={ek[n]!r}")
for n in (83,148,139,140):
    print(f"  byte-eq {n}: {ck[n][0]==ek[n][0]} core_key={ck[n][0]!r} ed_key={ek[n][0]!r}")
print("  ed 99:",ek[99]); print("  core 99:",ck[99]); print("  ed 137/138:",ek[137],ek[138]); print("  ed 150:",ek[150])
print("== P7 quotes (exact 8 Russian sentences, whitespace-normalized full-text count) ==")
def norm_all(dd):
    txt=[]
    for p in ["p1-pervaya","p2-zhizn","p3-kultura","p4-sport","p5-molodezh","p6-razbor","p7-yazyk","p8-test"]:
        txt.append(" ".join(s for _,_,s in elems(f"{dd}/{p}.svg")))
    return re.sub(r"\s+"," "," ".join(txt))
edn,con=norm_all(ED),norm_all(CORE)
p7=[e for e in elems(f"{ED}/p7-yazyk.svg")]
quotes=[s for x,y,s in p7 if x in (65.0,989.0) and y in (1857.0,2002.0,2147.0,2292.0)]
print("n quotes:",len(quotes))
for q in quotes:
    qn=re.sub(r"\s+"," ",q)
    print(f"  ed={edn.count(qn)} core={con.count(qn)} :: {q[:70]}")
    # page tags in P7: translation line following
print("== P7 quote page tags ==")
for x,y,s in p7:
    if "Страница" in s: print(f"  x={x} y={y} {s[:60]}")
print("== numbering extras ==")
for p in ["p1-pervaya","p5-molodezh"]:
    for x,y,s in elems(f"{ED}/{p}.svg"):
        mm=pat.match(s.strip())
        if mm and int(mm.group(1)) in (11,) and p=="p1-pervaya": print(f"  {p} x={x} y={y} {s[:80]!r}")
    # P5: list all line-head numbers
    nums=sorted({int(pat.match(s.strip()).group(1)) for x,y,s in elems(f"{ED}/{p}.svg") if pat.match(s.strip())})
    print(f"  {p} all head numbers: {nums}")
    for x,y,s in elems(f"{ED}/{p}.svg"):
        mm=pat.match(s.strip())
        if mm and p=="p5-molodezh" and int(mm.group(1))<65: print(f"    low-num {p} x={x} y={y} {s[:80]!r}")
print("== model words ==")
for label,dd in (("core",CORE),("ed",ED)):
    es=elems(f"{dd}/p8-test.svg")
    # model paragraph: lines after the 'Пример:' line in exercise area (x~95/1019 area, y 700-1250), starting with 'Моя неделя'
    idx=[i for i,(x,y,s) in enumerate(es) if s.strip().startswith("Пример:")]
    print(label,"Primer idx:",idx, [es[i] for i in idx])
    # print surrounding lines in y order for the H section
    sec=sorted([(y,x,s) for x,y,s in es if 700<y<1252 and x<1100], key=lambda t:t[0])
    for y,x,s in sec[-25:]: print(f"   {label} y={y} x={x} {s[:90]}")
