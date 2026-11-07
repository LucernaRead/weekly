import re, json, html, hashlib, base64, os, sys
from collections import Counter, defaultdict
ROOT=os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
G=f"{ROOT}/hidden_files/w46/zh-cn-proofread-gates-round2"
FILES=f"{ROOT}/files"
EDITIONS={"en":"weekly-report-w46-zh-cn-core","de":"weekly-report-w46-zh-cn-de","es":"weekly-report-w46-zh-cn-es","fr":"weekly-report-w46-zh-cn-fr","it":"weekly-report-w46-zh-cn-it","ja":"weekly-report-w46-zh-cn-ja","ko":"weekly-report-w46-zh-cn-ko","nl":"weekly-report-w46-zh-cn-nl","pt":"weekly-report-w46-zh-cn-pt","ru":"weekly-report-w46-zh-cn-ru"}
PAGES=["p1-touiban","p2-shenghuo","p3-wenhua","p4-tiyu","p5-qingnian","p6-shendu","p7-ciyu","p8-ceyan"]
TEXT_RE=re.compile(r'<text x="([0-9.\-]+)" y="([0-9.\-]+)" font-family="([^"]+)" font-size="([0-9.]+)"([^>]*)>([^<]*)</text>')
def texts(ed,page):
    t=open(f"{FILES}/{EDITIONS[ed]}/svg/{page}.svg",encoding="utf-8").read()
    out=[]
    for m in TEXT_RE.finditer(t):
        out.append({"x":float(m.group(1)),"y":float(m.group(2)),"fam":m.group(3),"size":float(m.group(4)),"rest":m.group(5),"s":html.unescape(m.group(6))})
    return out,t
def alltexts(ed):
    d={}
    for p in PAGES: d[p]=texts(ed,p)[0]
    return d
out={}
# 1. Rendered P8 keys vs registry
reg=json.load(open(f"{G}/registry-numbered-r3.json"))
regkeys={}
n=0
for e in reg:
    if e["name"]=="ex": n+=1; regkeys[n]=e["key"]
    else:
        for k in e["keys"]: n+=1; regkeys[n]=k
out["registry_total"]=n
out["p8_rendered_keys"]={}
for ed in EDITIONS:
    ext=json.load(open(f"{G}/p8-extract-{ed}.json"))
    keys=ext["keys"]
    mism=[]
    for i in range(1,150):
        if keys.get(str(i))!=regkeys[i]: mism.append((i,regkeys[i],keys.get(str(i))))
    out["p8_rendered_keys"][ed]={"mismatches_1_149":mism,"key150":keys.get("150"),"noted":len(ext["noted_set"])}
    # note trailing letters for matching items from P8 SVG lines
    p8=texts(ed,"p8-ceyan")[0]
    lines=[t["s"] for t in p8 if re.match(r"^\d+\. ",t["s"]) and " — " in t["s"]]
    trail={}
    for ln in lines:
        m=re.match(r"^(\d+)\. (\S) — (.*)$",ln)
        if m:
            num=int(m.group(1)); note=m.group(3)
            tm=re.search(r",\s*([a-d])\s*$",note)
            trail[num]=(m.group(2), tm.group(1) if tm else None, ln)
    out["p8_rendered_keys"][ed]["matching_trailing"]={str(k):trail.get(k) for k in [25,26,27,28,43,44,45,46,61,62,63,64,79,80,81,82,97,98,99,100]}
# 2. Freeze totals
out["freeze_totals"]={}
for ed in EDITIONS:
    f=json.load(open(f"{G}/freeze-{ed}.json"))
    per={}; hanzi=0; detail={}
    for k,pg in f["pages"].items():
        added=pg.get("cjk_added",{})
        tot=sum(added.values()) if isinstance(added,dict) else len(added)
        per[k]=tot
        if isinstance(added,dict):
            for ch,cnt in added.items():
                if "\u4e00"<=ch<="\u9fff": hanzi+=cnt; detail[ch]=detail.get(ch,0)+cnt
    out["freeze_totals"][ed]=per
    out["freeze_totals"][ed]["TOTAL"]=sum(per.values())
    out["freeze_totals"][ed]["hanzi_added"]=hanzi; out["freeze_totals"][ed]["hanzi_detail"]=detail
    out["freeze_totals"][ed]["core_totals"]={k:pg.get("cjk_core_total") for k,pg in f["pages"].items()}
    out["freeze_totals"][ed]["edition_totals"]={k:pg.get("cjk_edition_total") for k,pg in f["pages"].items()}
# 3. Chip counts
out["chips"]={}
for ed in EDITIONS:
    per={}; allnums=[]
    for p in PAGES:
        nums=[]
        for t in texts(ed,p)[0]:
            if t["size"]==24.0 and 'font-weight="700"' in t["rest"]:
                m=re.match(r"^(\d+)\.$",t["s"])
                if m: nums.append(int(m.group(1)))
                m2=re.match(r"^(\d+)–(\d+)\.$",t["s"])
                if m2: nums.extend(range(int(m2.group(1)),int(m2.group(2))+1))
        per[p]=sorted(nums); allnums+=nums
    out["chips"][ed]={"per_page":{k:len(v) for k,v in per.items()},"per_page_nums":per,"union":sorted(set(allnums)),"dups":[k for k,c in Counter(allnums).items() if c>1],"total_unique":len(set(allnums))}
# 4. P7 phrases
PHRASES=["双11的正日子","先看结算页，再决定买不买","提高自防自救能力","三支队进了八强","输了就回家","老电影，新画面","快递的高峰分三波","着火了不坐电梯"]
out["phrases"]={}
for ed in EDITIONS:
    joined={p:"".join(t["s"] for t in texts(ed,p)[0]) for p in PAGES}
    res={}
    for ph in PHRASES:
        pages=[p for p in PAGES if ph in joined[p]]
        res[ph]={"pages":pages,"total_occurrences":sum(joined[p].count(ph) for p in PAGES)}
    out["phrases"][ed]=res
# 5. Chart rects
out["chart"]={}
for ed in EDITIONS:
    t=open(f"{FILES}/{EDITIONS[ed]}/svg/p6-shendu.svg",encoding="utf-8").read()
    rects=re.findall(r'<rect x="([0-9.]+)" y="([0-9.]+)" width="([0-9.]+)" height="([0-9.]+)"[^>]*fill="([^"]+)"',t)
    bars=[r for r in rects if r[0]=="325" and r[3]=="30"]
    out["chart"][ed]=bars
# 6. Kinsoku
NO_START=set("、。，．・：；？！）〕］｝」』〉》】〗〜…―ーぁぃぅぇぉっゃゅょゎァィゥェォッャュョヮ")
NO_END=set("（〔［｛「『〈《【〖")
out["kinsoku"]={}
for ed in EDITIONS:
    flags=[]
    for p in PAGES:
        for t in texts(ed,p)[0]:
            s=t["s"]
            if s and s[0] in NO_START: flags.append((p,"START",s[:30],t["x"],t["y"]))
            if s and s[-1] in NO_END: flags.append((p,"END",s[-30:],t["x"],t["y"]))
    out["kinsoku"][ed]=flags
# 7. Badge/footer
out["badge_footer"]={}
for ed in EDITIONS:
    p1=texts(ed,"p1-touiban")[0]
    badge=[(t["s"],t["rest"]) for t in p1 if "#3e4c2a" in t["rest"] and len(t["s"])>20]
    mast=[t["s"] for t in p1 if t["s"]=="Lucerna"]
    foot={}
    for p in PAGES:
        ts=texts(ed,p)[0]
        foot[p]=[t["s"] for t in ts if "VOL.3" in t["s"] or "Lucerna" in t["s"]]
    out["badge_footer"][ed]={"badge_candidates":badge,"masthead_Lucerna_count":len(mast),"footer_lines":foot}
# 8. Scripts + trad strict
TRAD=set("學讀雙讓還為與來東長門關發對說國親觀歡灣臺議論權機歲處帳陽陰雲靈龍龜點麵")
POL=["战争","地缘","外交","政治","选举","民调","政党","政府","领导人","主席","总理","人大","政协","台独","六四"]
SWEEP=["W46","w46","zh-cn","2026-w46","SOP","proofread","occlusion","audit","GitHub","insert.py","freeze","lint"]
out["scripts"]={}
for ed in EDITIONS:
    alls="".join(t["s"] for p in PAGES for t in texts(ed,p)[0])
    hang=sum(1 for c in alls if "\uac00"<=c<="\ud7af")
    hira=sum(1 for c in alls if "\u3040"<=c<="\u309f")
    kata=sum(1 for c in alls if "\u30a0"<=c<="\u30ff")
    cyr=sum(1 for c in alls if "\u0400"<=c<="\u04ff")
    tradhits=[(c,alls.count(c)) for c in sorted(set(alls)&TRAD)]
    polhits={w:alls.count(w) for w in POL if w in alls}
    sweephits={w:alls.count(w) for w in SWEEP if w in alls}
    out["scripts"][ed]={"hangul":hang,"hiragana":hira,"katakana":kata,"cyrillic":cyr,"trad_hits":tradhits,"politics":polhits,"reader_sweep":sweephits,"total_chars":len(alls)}
# 9. Orphan scan
out["orphan"]={}
for ed in EDITIONS:
    cands=[]; outside=[]
    for p in PAGES:
        for t in texts(ed,p)[0]:
            if re.match(r"^\d\.$",t["s"]) and t["x"] in (65.0,527.0,989.0,1451.0): cands.append((p,t["s"],t["x"],t["y"]))
            if re.match(r"^(\d+)\.$",t["s"]) or re.match(r"^\d+–\d+\.$",t["s"]):
                if t["x"] not in (137.0,599.0,1061.0,1523.0) and t["size"]!=13.3: outside.append((p,t["s"],t["x"],t["y"],t["size"]))
    out["orphan"][ed]={"colstart_single_digit":cands,"digitdot_outside_number_x":outside}
# 10. Images + credits + payload md5
out["images"]={}
for ed in EDITIONS:
    per={}; payloads=[]
    for p in PAGES:
        t=open(f"{FILES}/{EDITIONS[ed]}/svg/{p}.svg",encoding="utf-8").read()
        imgs=re.findall(r'<image[^>]*>',t)
        hrefs=re.findall(r'xlink:href="data:image/[^;]+;base64,([^"]+)"',t)
        for h in hrefs: payloads.append(hashlib.md5(base64.b64decode(h)).hexdigest())
        credits=[x["s"] for x in texts(ed,p)[0] if "Photo:" in x["s"]]
        per[p]={"images":len(imgs),"credits":credits}
    out["images"][ed]={"per_page":per,"payload_md5s":payloads}
# 11. text.md + abstracts
out["textmd"]={}
for ed in EDITIONS:
    fn=f"{FILES}/{EDITIONS[ed]}/2026-w46-zh-cn-{ed}.text.md"
    lines=open(fn,encoding="utf-8").read().splitlines()
    secs=[l for l in lines if l.startswith("## ")]
    txt="\n".join(lines)
    out["textmd"][ed]={"lines":len(lines),"sections":len(secs),"es_p_fix":(lines[622] if ed=="es" and len(lines)>622 else None),"es_p5_fix":(lines[1062] if ed=="es" and len(lines)>1062 else None),
      "old_instr_count":txt.count("Responde con fechas y números de la página"),
      "key25":("25. d" in txt),"key26":("26. c" in txt),"key27":("27. b" in txt),"key99":("99. a" in txt),"key100":("100. b" in txt),
      "oldkey25c":("25. c" in txt),"stem101":("我拿了一个" in txt)}
    ab=open(f"{FILES}/{EDITIONS[ed]}/ABSTRACT.txt",encoding="utf-8").read()
    out["textmd"][ed]["abstract"]={"bytes":len(ab.encode()),"lines":ab.count("\n")+1 if ab else 0,"has_dquote":'"' in ab,"has_Lucerna":"Lucerna" in ab,"has_VOL3":"VOL.3" in ab,"has_A2B2":"A2" in ab and "B2" in ab,"has_150":"150" in ab,"text":ab}
json.dump(out,open(f"{G}/counts-phrases-chart-r3.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("WROTE counts-phrases-chart-r3.json")
for ed in EDITIONS:
    print(ed,"p8mismatch",out["p8_rendered_keys"][ed]["mismatches_1_149"][:3],"key150",out["p8_rendered_keys"][ed]["key150"])
print("freeze",{ed:out["freeze_totals"][ed].get("TOTAL") for ed in ("ja","ko")})
print("ko hanzi",out["freeze_totals"]["ko"]["hanzi_added"])
print("chips",{ed:out["chips"][ed]["per_page"] for ed in EDITIONS})
print("chart-en",out["chart"]["en"])
print("kinsoku totals",{ed:len(out["kinsoku"][ed]) for ed in EDITIONS})
print("orphan",{ed:(len(out["orphan"][ed]["colstart_single_digit"]),len(out["orphan"][ed]["digitdot_outside_number_x"])) for ed in EDITIONS})
print("images",{ed:sum(v["images"] for v in out["images"][ed]["per_page"].values()) for ed in EDITIONS})
print("payloads identical:", len(set(tuple(out["images"][ed]["payload_md5s"]) for ed in EDITIONS))==1, out["images"]["en"]["payload_md5s"])
print("scripts",{ed:(out["scripts"][ed]["hangul"],out["scripts"][ed]["hiragana"],out["scripts"][ed]["katakana"],out["scripts"][ed]["cyrillic"],out["scripts"][ed]["trad_hits"],out["scripts"][ed]["politics"],out["scripts"][ed]["reader_sweep"]) for ed in EDITIONS})
