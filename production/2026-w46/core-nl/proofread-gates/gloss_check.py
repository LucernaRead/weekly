import re, xml.etree.ElementTree as ET, json
F="/home/hatch/workspace/goals/lucernaread-social-media-operations/files"
NS="{http://www.w3.org/2000/svg}"
PREFIXES={
 "core": ["译注｜","讲解｜"],
 "de": ["Hinweis","Erklärung"],
 "en": ["Note |"],
 "es": ["Nota —"],
 "fr": ["Note —"],
 "it": ["Nota —"],
 "ja": ["解説 —"],
 "ko": ["해설 —"],
 "pt": ["Nota —"],
 "ru": ["Пояснение —"],
 "zh-tw": ["譯注｜","講解｜"],
}
PAGES=["p1-voorpagina.svg","p2-leven.svg","p3-cultuur.svg","p4-sport.svg","p5-jongeren.svg","p6-verdieping.svg","p7-taal.svg"]
def elements(ed,pg):
    tree=ET.parse(f"{F}/weekly-report-w46-nl-{ed}/svg/{pg}")
    out=[]
    for el in tree.getroot().iter(NS+"text"):
        t="".join(el.itertext())
        out.append({"x":float(el.get("x")),"y":float(el.get("y")),"fs":float(el.get("font-size")),"text":t})
    return out
def flows(ed):
    res={}
    for pi,pg in enumerate(PAGES,1):
        els=elements(ed,pg)
        used=set()
        boxes=[]
        for i,e in enumerate(els):
            if i in used: continue
            txt=e["text"].strip()
            if any(txt.startswith(p) for p in PREFIXES[ed]):
                # collect flow: same x (+/-3), fs within 1.5, y increasing, gap <45
                lines=[e["text"]]; used.add(i)
                last_y=e["y"]
                for j in range(i+1,len(els)):
                    e2=els[j]
                    if j in used: continue
                    if abs(e2["x"]-e["x"])<3 and abs(e2["fs"]-e["fs"])<1.5 and 0<e2["y"]-last_y<45:
                        lines.append(e2["text"]); used.add(j); last_y=e2["y"]
                    elif e2["y"]>last_y+45 and abs(e2["x"]-e["x"])<3:
                        break
                joined=" ".join(l.strip() for l in lines)
                items=[s.strip() for s in joined.split("·") if s.strip()]
                boxes.append({"page":pi,"prefix":txt[:20],"lines":len(lines),"joined":joined,"n_items":len(items),"items":items})
        res[pi]=boxes
    return res
allres={}
for ed in PREFIXES:
    fl=flows(ed)
    allres[ed]=fl
    print(f"===== {ed} =====")
    for pi in range(1,8):
        for b in fl[pi]:
            print(f" P{pi} lines={b['lines']} items={b['n_items']}")
            for it in b["items"]: print(f"    - {it[:110]!r}")
json.dump(allres, open("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/nl-proofread-gates/gloss.json","w"), ensure_ascii=False, indent=1)
