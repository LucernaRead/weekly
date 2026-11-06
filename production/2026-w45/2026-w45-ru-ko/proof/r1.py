#!/usr/bin/env python3
"""Reproof R1: freeze / P8 dash-parse / geometry / badge / gloss / images / quotes / counts."""
import re, json, hashlib, collections
BASE="/home/hatch/workspace/goals/lucernaread-social-media-operations/files"
CORE=f"{BASE}/weekly-report-w45-ru-core/svg"; ED=f"{BASE}/weekly-report-w45-ru-ko/svg"; W43=f"{BASE}/weekly-report-ru-ko/svg"
PAGES=["p1-pervaya","p2-zhizn","p3-kultura","p4-sport","p5-molodezh","p6-razbor","p7-yazyk","p8-test"]
def texts(path):
    t=open(path,encoding="utf-8").read(); out=[]
    for m in re.finditer(r"<text[^>]*>(.*?)</text>",t,re.S):
        s=re.sub(r"<[^>]+>","",m.group(1))
        for a,b in [("&amp;","&"),("&lt;","<"),("&gt;",">"),("&quot;",'"'),("&apos;","'")]: s=s.replace(a,b)
        out.append(s)
    return out,t
def elems(path):
    t=open(path,encoding="utf-8").read(); out=[]
    for m in re.finditer(r"<text([^>]*)>(.*?)</text>",t,re.S):
        attrs=m.group(1); s=re.sub(r"<[^>]+>","",m.group(2))
        def g(k):
            mm=re.search(k+r'="([^"]*)"',attrs); return mm.group(1) if mm else ""
        out.append({"x":float(g("x")) if g("x") else None,"y":float(g("y")) if g("y") else None,
                    "size":g("font-size"),"weight":g("font-weight"),"fill":g("fill"),"anchor":g("text-anchor"),"text":s})
    return out
def rects(path):
    t=open(path,encoding="utf-8").read(); out=[]
    for m in re.finditer(r"<rect([^>]*)/>",t):
        a=m.group(1)
        def g(k):
            mm=re.search(k+r'="([^"]*)"',a); return mm.group(1) if mm else ""
        out.append((g("x"),g("y"),g("width"),g("height"),g("fill")))
    return out
CYR=re.compile(r"[\u0400-\u04FF]+"); HAN=re.compile(r"[\u4E00-\u9FFF]"); HANG=re.compile(r"[\uAC00-\uD7A3\u1100-\u11FF\u3130-\u318F]")
print("== Cyrillic token multiset ==")
for p in PAGES:
    ct,_=texts(f"{CORE}/{p}.svg"); et,_=texts(f"{ED}/{p}.svg")
    cc=collections.Counter(tok for s in ct for tok in CYR.findall(s)); ec=collections.Counter(tok for s in et for tok in CYR.findall(s))
    print(f"{p}: core={sum(cc.values())} ed={sum(ec.values())} core-only={dict(cc-ec)} ed-only={dict(ec-cc)}")
print("== Han/Hangul rendered per page (edition) ==")
for p in PAGES:
    et,raw=texts(f"{ED}/{p}.svg"); j="".join(et)
    print(f"{p}: Han_text={len(HAN.findall(j))} Hangul_text={len(HANG.findall(j))} Han_raw={len(HAN.findall(raw))}")
print("== P8 dash-parse ==")
pat=re.compile(r"^(\d+)\.\s*(.*)$")
def keymap(ts):
    m={}
    for s in ts:
        mm=pat.match(s.strip())
        if mm:
            rest=mm.group(2)
            k,n=(rest.split(" — ",1)+[""])[:2] if " — " in rest else (rest,"")
            m.setdefault(int(mm.group(1)),(k,n))
    return m
ck=keymap(texts(f"{CORE}/p8-test.svg")[0]); ek=keymap(texts(f"{ED}/p8-test.svg")[0])
print(f"core_lines={len(ck)} ed_lines={len(ek)} missing={sorted(set(ck)-set(ek))} extra={sorted(set(ek)-set(ek))}")
kd=[n for n in sorted(set(ck)&set(ek)) if ck[n][0]!=ek[n][0]]; print("dash keydiffs:",kd)
for n in kd: print(f"  {n}: core={ck[n]!r} ed={ek[n]!r}")
for n in (83,148,139,140):
    print(f"  byte-eq {n}: core_key==ed_key {ck[n][0]==ek[n][0]} core={ck[n][0]!r} ed={ek[n][0]!r}")
print("  ed 99:",ek.get(99)); print("  ed 150:",ek.get(150))
print("== rect multiset diff core vs ed (differing only) ==")
for p in PAGES:
    cc=collections.Counter(rects(f"{CORE}/{p}.svg")); ec=collections.Counter(rects(f"{ED}/{p}.svg"))
    d1={k:v for k,v in (cc-ec).items()}; d2={k:v for k,v in (ec-cc).items()}
    print(f"{p}: core-only={d1} ed-only={d2}" if d1 or d2 else f"{p}: identical")
print("== P6 bars/labels ==")
for label,dd in (("core",CORE),("ed",ED)):
    t=open(f"{dd}/p6-razbor.svg",encoding="utf-8").read()
    bars=[(r[1],r[2]) for r in rects(f"{dd}/p6-razbor.svg") if r[0]=="685" and r[3]=="30"]
    print(label,"bars(y,w):",bars)
    es=elems(f"{dd}/p6-razbor.svg")
    labs=[(e["x"],e["y"],e["text"]) for e in es if e["text"].strip().endswith("%") or re.match(r"^\d+%?$",e["text"].strip())]
    print(label,"pct-labels:",labs)
    print(label,"chart % texts:",[(e["x"],e["y"],e["text"]) for e in es if "%" in e["text"]])
print("== P7 geometry ==")
for label,dd in (("core",CORE),("ed",ED)):
    es=elems(f"{dd}/p7-yazyk.svg")
    box=[r for r in rects(f"{dd}/p7-yazyk.svg") if r[0]=="1451"]
    print(label,"x=1451 rects:",box)
    print(label,"disclosure-ish lines:",[(e["x"],e["y"],e["text"][:60]) for e in es if e["y"] and e["y"]>1600])
print("== badge 3-way ==")
for label,dd in (("ed",ED),("w43",W43)):
    es=elems(f"{dd}/p1-pervaya.svg")
    b=[e for e in es if "한국어 독자를 위한 판" in e["text"]]
    print(label,"badge:",b)
    c372=[e for e in elems(f"{CORE}/p1-pervaya.svg") if e["y"]==372.0]
    print("core y372:",[(e["text"][:50]) for e in c372])
    e372=[e for e in es if e["y"]==372.0]
    print(label,"ed/w43 y372:",[(e["text"][:50]) for e in e372])
print("== gloss (edition build gloss() calls) ==")
import pathlib
bdir=pathlib.Path("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-ru-ko-build")
tot=0; per={}
for f in ["content12.py","content34.py","content56.py","content7.py","content8.py"]:
    src=(bdir/f).read_text(encoding="utf-8"); calls=re.findall(r"\.gloss\((.*?)\)\s*$",src,re.M)
    items=[]
    for c in calls:
        # gloss arg is a quoted string; extract first string literal content
        mm=re.search(r'"(.*)"',c)
        if mm: items+= [x.strip() for x in mm.group(1).split("·")]
    per[f]=len(items); tot+=len(items); print(f, "gloss items:", len(items), items)
print("gloss TOTAL:",tot,"per-file:",per)
print("== images byte-identity ==")
for p in PAGES:
    for label,dd in (("core",CORE),("ed",ED)):
        t=open(f"{dd}/{p}.svg",encoding="utf-8").read()
        uris=re.findall(r"data:image/[^\"']+",t)
        hs=[hashlib.sha256(u.encode()).hexdigest()[:16] for u in uris]
        if label=="core": ch=hs
        else: print(f"{p}: core_img={ch} ed_img={hs} equal={ch==hs}")
print("== P7 quotes 2x ==")
ed_all="".join("".join(texts(f"{ED}/{p}.svg")[0]) for p in PAGES)
co_all="".join("".join(texts(f"{CORE}/{p}.svg")[0]) for p in PAGES)
p7=elems(f"{ED}/p7-yazyk.svg")
# quote lines: P7 quote section lines are long Russian sentences; use P7 lines with Cyrillic length>20 in quote area y<1560 excluding headers
quotes=[e["text"] for e in p7 if len(CYR.findall(e["text"]))>=3 and len(e["text"])>25 and e["y"] and e["y"]<1560]
print("candidate quote lines:",len(quotes))
for q in quotes: print(f"  ed_count={ed_all.count(q)} core_count={co_all.count(q)} :: {q[:70]}")
print("== exercise numbering (rendered line-head numbers) ==")
for p in PAGES:
    ts,_=texts(f"{ED}/{p}.svg")
    nums=sorted({int(m.group(1)) for s in ts for m in [pat.match(s.strip())] if m})
    print(f"{p}: n={len(nums)} range={nums[0] if nums else None}-{nums[-1] if nums else None} contiguous={nums==list(range(nums[0],nums[-1]+1)) if nums else None}")
print("== level chips ==")
for label,dd in (("core",CORE),("ed",ED)):
    tot_c=collections.Counter()
    for p in PAGES:
        for e in elems(f"{dd}/{p}.svg"):
            if e["text"].strip() in ("A2","B1","B2"): tot_c[e["text"].strip()]+=1
    print(label,dict(tot_c),"total",sum(tot_c.values()))
print("== CSKA / 체스카 ==")
for p in PAGES:
    t=open(f"{ED}/{p}.svg",encoding="utf-8").read()
    print(p,"CSKA:",t.count("CSKA"),"체스카:",t.count("체스카"))
print("== model text (P8 H-section) core vs ed ==")
for label,dd in (("core",CORE),("ed",ED)):
    ts,_=texts(f"{dd}/p8-test.svg")
    mod=[s for s in ts if "Моя неделя" in s or "Пример" in s]
    print(label,mod[:6])
