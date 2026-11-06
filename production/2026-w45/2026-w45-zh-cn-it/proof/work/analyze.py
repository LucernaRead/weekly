import re, sys, hashlib, pathlib, json
import xml.etree.ElementTree as ET
BASE = pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations"
DEL = BASE/"files/weekly-report-w45-zh-cn-it"
CORE = BASE/"files/weekly-report-w45-zhcn-core"
W43 = BASE/"files/weekly-report-zh-cn-it"
NS = "{http://www.w3.org/2000/svg}"

def texts(p):
    tree = ET.parse(p)
    out=[]
    for el in tree.iter():
        if el.tag.endswith("text"):
            t="".join(el.itertext())
            out.append((float(el.get("x",0)), float(el.get("y",0)), t, el.get("font-size")))
    return out

def page_text(p):
    return "\n".join(t for _,_,t,_ in texts(p))

# --- Gate 2/3: P8 keys ---
for label, d in [("DEL",DEL),("CORE",CORE)]:
    ts = texts(d/"svg/p8-ceyan.svg")
    keys={}
    for x,y,t,fs in ts:
        m=re.match(r"^(\d+)\.\s", t)
        if m: keys[int(m.group(1))]= (y,t)
        m2=re.match(r"^(\d+)\.\s*✓", t)
        if m2: keys[int(m2.group(1))]= (y,t)
    print(label, "P8 text nodes:", len(ts))
    for n in (134,135,136,150):
        print(" ", label, n, keys.get(n))
    # last keys by y
    ks=sorted(keys.items(), key=lambda kv: kv[1][0])
    print(" ", label, "last 5 by y:", ks[-5:])
    # footer rule
    tree=ET.parse(d/"svg/p8-ceyan.svg")
    rules=[(el.get("y1"),el.get("y2")) for el in tree.iter() if el.tag.endswith("line") and el.get("y1")=="2580"]
    print(" ", label, "footer rules y=2580:", len(rules))
    if label=="DEL":
        print("  DEL key135 full:", keys.get(135))
        # all notes identical check handled elsewhere
        # P8 header
        hdr=[t for _,_,t,_ in ts if "Tutte le note" in t or "Soluzioni" in t]
        print("  DEL P8 header texts:", hdr)

# --- B1 / ex70 mirror ---
p5 = page_text(DEL/"svg/p5-qingnian.svg")
for needle in ["i personaggi del film sono immagini digitali", "shùzì"]:
    print("P5 contains", needle, ":", needle in p5)
# find ex70 context: lines containing shùzì in P5
for x,y,t,fs in texts(DEL/"svg/p5-qingnian.svg"):
    if "shùzì" in t: print(" P5 shùzì node:", y, repr(t))
for x,y,t,fs in texts(DEL/"svg/p8-ceyan.svg"):
    if "shùzì" in t: print(" P8 shùzì node:", y, repr(t))

# --- Header claim + English scan ---
EN_WORDS = [" the "," are "," characters "," digital "," images"," film's ","characters are","the AI film"]
old135 = "the AI film's characters are digital images"
for i,fn in enumerate(sorted((DEL/"svg").glob("*.svg")),1):
    txt = page_text(fn)
    print(f"P{i} old135 absent: {old135 not in txt}; 'the AI film' absent: {'the AI film' not in txt}")
# distinctive English words scan over joined SVG text
import re as _re
words = set(["the","characters","digital","images","film","are","this","that","with","from","which","have","been","will","would","should","because","about","their","there","here","when","where","what","your","yours"])
for i,fn in enumerate(sorted((DEL/"svg").glob("*.svg")),1):
    txt = page_text(fn)
    # tokenise latin words
    toks = _re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", txt)
    low=[t.lower() for t in toks]
    hits = sorted(set(t for t in low if t in words))
    print(f"P{i} distinctive-EN tokens present: {hits}")
    # show contexts for hits
    for h in hits:
        for line in txt.splitlines():
            if _re.search(rf"\b{h}\b", line, _re.I):
                print("   ", h, ":", line[:200])
                break

# --- P8 notes vs core identical ---
def p8_notes(d):
    out={}
    for x,y,t,fs in texts(d/"svg/p8-ceyan.svg"):
        m=re.match(r"^(\d+)\.\s*(.*)$", t)
        if m: out[int(m.group(1))]=m.group(2)
    return out
dn, cn = p8_notes(DEL), p8_notes(CORE)
same=[n for n in dn if n in cn and dn[n]==cn[n]]
print("P8 identical notes vs core:", same, [dn[n] for n in same])
print("P8 notes count del/core:", len(dn), len(cn))

# --- Badge measurement P1 three-way ---
for label,d in [("CORE",CORE),("W43",W43),("DEL",DEL)]:
    ts=texts(d/"svg/p1-touiban.svg")
    badge=[(x,y,fs,t) for x,y,t,fs in ts if "CINESE" in t or "TESTI IN" in t or "SEMPLIFICATO" in t and "SETTIMANALE" in t]
    print(label, "P1 badge-ish:", badge[:4])
    # all texts with y near 434
    near=[(x,y,fs,t) for x,y,t,fs in ts if abs(y-434)<2]
    print(" ", label, "y≈434 texts:", near)
    # masthead ys
    for pat in ["Lucerna"]:
        print(" ", label, pat, [(x,y,fs) for x,y,t,fs in ts if t.strip()==pat][:3])

# --- P7 disclosure + golden + footer ---
p7 = page_text(DEL/"svg/p7-ciyu.svg")
print("P7 disclosure invitation verbatim:", "mandateci le vostre lettere in cinese, le pubblicheremo!" in p7)
for frag in ["Una lettera di esempio della redazione", "non è una lettera vera", "non è arrivato nulla"]:
    print(" P7 frag", frag, frag in p7)
# footer + page lines
for i,fn in enumerate(sorted((DEL/"svg").glob("*.svg")),1):
    ts=texts(fn)
    foot=[t for _,_,t,_ in ts if "SETTIMANALE CINESE" in t]
    pg=[t for _,_,t,_ in ts if re.match(r"Pagina \d+ di 8", t)]
    sep=[t for _,_,t,_ in ts if t.startswith("— Pagina")]
    print(f"P{i} footer={foot} pageline={pg} seps={len(sep)}")
# P8 separators
p8ts=texts(DEL/"svg/p8-ceyan.svg")
print("P8 separators:", [t for _,_,t,_ in p8ts if t.startswith("— Pagina")])
# P7 golden
gold = ["不用等11月11日","下单就能发货","先看结算页，再付款","水开始结冰","三场都输了","小局一场没赢","故事够不够好","别以后，就现在"]
alltxt = {i: page_text(fn) for i,fn in enumerate(sorted((DEL/"svg").glob("*.svg")),1)}
for g in gold:
    pages=[i for i,t in alltxt.items() if g in t]
    total=sum(alltxt[i].count(g) for i in pages)
    print(" GOLD", g, "pages", pages, "total count", total)
# P7 tags: lines near golden on P7
for x,y,t,fs in texts(DEL/"svg/p7-ciyu.svg"):
    if any(g in t for g in gold): print("  P7 golden node:", y, repr(t[:120]))
