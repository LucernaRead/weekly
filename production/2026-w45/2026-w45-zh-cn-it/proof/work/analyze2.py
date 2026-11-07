import re, pathlib
import xml.etree.ElementTree as ET
BASE = pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations"
DEL = BASE/"files/weekly-report-w45-zh-cn-it"
CORE = BASE/"files/weekly-report-w45-zhcn-core"

def nodes(p):
    tree = ET.parse(p); out=[]
    for el in tree.iter():
        if el.tag.endswith("text"):
            out.append((float(el.get("x",0)), float(el.get("y",0)), "".join(el.itertext())))
    return out
def concat(p): return "".join(t for _,_,t in nodes(p))
def spaced(p): return " ".join(t for _,_,t in nodes(p))

# P5 personaggi / immagini nodes
print("== P5 nodes with personaggi/immagini/digitali ==")
for x,y,t in nodes(DEL/"svg/p5-qingnian.svg"):
    if any(w in t for w in ["personaggi","immagini","digitali","film"]):
        print(y, repr(t))
print("== P5 concat contains ex70 full? ==")
c5=concat(DEL/"svg/p5-qingnian.svg")
print("concat ex70:", "i personaggi del film sono immagini digitali" in c5)
print("spaced ex70:", "i personaggi del film sono immagini digitali" in spaced(DEL/"svg/p5-qingnian.svg"))
# search raw (no separator) around shùzì in concat
i=c5.find("shùzì")
print("concat around first shùzì:", repr(c5[max(0,i-50):i+200]))

# P7 invitation in concat/spaced
for name, fn in [("concat",concat),("spaced",spaced)]:
    t=fn(DEL/"svg/p7-ciyu.svg")
    print(f"P7 {name} invitation:", "mandateci le vostre lettere in cinese, le pubblicheremo!" in t)
    j=t.find("mandateci")
    print("  around:", repr(t[max(0,j-80):j+120]) if j>=0 else "NOT FOUND mandateci")
    # full disclosure concat extract
    k=t.find("Una lettera di esempio")
    print("  disclosure:", repr(t[k:k+600]) if k>=0 else "none")

# Golden with concat (no separator) and spaced
for name, fn in [("concat",concat),("spaced",spaced)]:
    print(f"== golden {name} ==")
    gold = ["不用等11月11日","下单就能发货","先看结算页，再付款","水开始结冰","三场都输了","小局一场没赢","故事够不够好","别以后，就现在"]
    for g in gold:
        counts={}
        for pi in range(1,9):
            fnp = sorted((DEL/"svg").glob("*.svg"))[pi-1]
            counts[pi]=fn(fnp).count(g)
        print(" ", g, counts, "total", sum(counts.values()))

# P8 identical notes, note-content extraction
def note_del(t):
    m=re.match(r"^\d+\.\s*(?:✓\s*)?\((.*)\)\s*$", t)
    if m: return m.group(1)
    m=re.match(r"^\d+\.\s*(?:✓\s*)?\(?(.*)", t)
    return t
def note_core(t):
    # core form: N. key — note  OR N. answer — note ; take after last ' — '?? first proof: note = after key dash
    parts=t.split(" — ")
    return parts[-1] if len(parts)>=2 else t
# P8 keys are wrapped: need join continuation? First proof used node comparison? Instead compare per-key first nodes only, plus check #94 and #135 specifically across full node sets
print("== P8 #94 nodes del/core ==")
for label,d in [("DEL",DEL),("CORE",CORE)]:
    for x,y,t in nodes(d/"svg/p8-ceyan.svg"):
        if t.startswith("94."): print(" ",label,y,repr(t))
print("== P8 nodes y>=2500 DEL (key-flow end) ==")
for x,y,t in nodes(DEL/"svg/p8-ceyan.svg"):
    if y>=2490: print(" ",y,repr(t[:160]))
print("== P8 nodes y>=2500 CORE ==")
for x,y,t in nodes(CORE/"svg/p8-ceyan.svg"):
    if y>=2490: print(" ",y,repr(t[:160]))
# P7 teaser rect bottom: find rects near bottom on P7
tree=ET.parse(DEL/"svg/p7-ciyu.svg")
rects=[(float(el.get("y",0)), float(el.get("height",0)), el.get("fill")) for el in tree.iter() if el.tag.endswith("rect")]
print("P7 rects with bottom>2500:", [(y,y+h,f) for y,h,f in rects if y+h>2500])
# P6 chart rects
tree=ET.parse(DEL/"svg/p6-shendu.svg")
for el in tree.iter():
    if el.tag.endswith("rect") and float(el.get("y",0)) in (1282.0,1340.0,1398.0):
        print("P6 chart rect:", el.get("x"), el.get("y"), el.get("width"), el.get("height"))
