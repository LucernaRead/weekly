#!/usr/bin/env python3
"""Round 2 independent analysis. Read-only: parses shipped SVGs/PDFs/text.md only."""
import xml.etree.ElementTree as ET, pathlib, re, json, subprocess, os, sys
from collections import Counter
BASE = pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations"
G = BASE/"hidden_files/w46/zh-tw-proofread-gates-round2"
NS = "{http://www.w3.org/2000/svg}"
EDITIONS = {"en":"weekly-report-w46-zhtw-core","de":"weekly-report-w46-zh-tw-de",
 "es":"weekly-report-w46-zh-tw-es","fr":"weekly-report-w46-zh-tw-fr",
 "it":"weekly-report-w46-zh-tw-it","ja":"weekly-report-w46-zh-tw-ja",
 "ko":"weekly-report-w46-zh-tw-ko","nl":"weekly-report-w46-zh-tw-nl",
 "pt":"weekly-report-w46-zh-tw-pt","ru":"weekly-report-w46-zh-tw-ru"}
PAGES = ["p1-front","p2-life","p3-culture","p4-sport","p5-youth","p6-deep","p7-lang","p8-test"]
OUT = open(G/"analysis-report.txt","w",encoding="utf-8")
def p(*a):
    print(*a, file=OUT)
def texts(svgpath):
    root = ET.parse(svgpath).getroot()
    out=[]
    for el in root.iter(NS+"text"):
        t="".join(el.itertext()).strip()
        if t:
            out.append({"x":float(el.get("x",0)),"y":float(el.get("y",0)),
                        "fs":el.get("font-size",""),"fill":el.get("fill",""),
                        "fam":el.get("font-family",""),"w":el.get("font-weight",""),
                        "anchor":el.get("text-anchor",""),"t":t})
    return out
def joined(code, page=None):
    d = BASE/"files"/EDITIONS[code]/"svg"
    ts=[]
    for pg in (PAGES if page is None else [page]):
        ts += texts(d/f"{pg}.svg")
    return ts
def alltext(code, page=None):
    return "".join(n["t"] for n in joined(code, page))

# ---------- D4 ----------
p("===== D4: 19座城市 / 3座城市 sweep (all SVGs + text.md) =====")
for code,dirname in EDITIONS.items():
    d = BASE/"files"/dirname
    n19 = n3 = 0
    for svg in sorted((d/"svg").glob("*.svg")):
        s = svg.read_text(encoding="utf-8"); n19 += s.count("19座城市"); n3 += s.count("3座城市")
    md = next((d).glob("*.text.md")).read_text(encoding="utf-8")
    p(f"{code}: SVG 19座城市={n19} 3座城市={n3} | text.md 19座城市={md.count('19座城市')} 3座城市={md.count('3座城市')}")
p("--- D4 evidence: city names in core P1+P5, timetable rows ---")
core15 = alltext("en","p1-front") + alltext("en","p5-youth")
for city in ["洛杉磯","東京","首爾","洛杉矶","东京","首尔"]:
    p(f"  {city}: P1+P5 occurrences={core15.count(city)}")
for n in joined("en","p5-youth"):
    if re.search(r"11月1[123]日", n["t"]):
        p(f"  P5 y={n['y']:.1f} :: {n['t']}")
for n in joined("en","p1-front"):
    if "23" in n["t"] or "19天" in n["t"] or "10月26" in n["t"]:
        p(f"  P1 y={n['y']:.1f} :: {n['t']}")
p("--- D4: P6 box lines containing 抽機票 (all editions) ---")
for code in EDITIONS:
    for n in joined(code,"p6-deep"):
        if "抽機票" in n["t"]:
            p(f"  {code} y={n['y']:.1f} :: {n['t']}")

# ---------- D1 ----------
p("\n===== D1: P5 practice-example glossline (all editions) =====")
for code in EDITIONS:
    hits=[n for n in joined(code,"p5-youth") if "450" in n["t"] or "Practice numbers" in n["t"]
          or "Übungszahlen" in n["t"] or "Números de práctica" in n["t"]
          or "Chiffres d'entra" in n["t"] or "Numeri di pratica" in n["t"]
          or "練習の数字" in n["t"] or "연습 숫자" in n["t"] or "Oefengetallen" in n["t"]
          or "Числа для практики" in n["t"]]
    p(f"-- {code}:")
    for n in hits: p(f"   y={n['y']:.1f} :: {n['t']}")
p("--- D1: P2 practice glossline (check translated, no English 'Practice numbers') ---")
for code in EDITIONS:
    hits=[n for n in joined(code,"p2-life") if "Practice numbers" in n["t"] or "3,000" in n["t"] or "3.000" in n["t"] or "3 000" in n["t"]]
    p(f"-- {code}:")
    for n in hits: p(f"   y={n['y']:.1f} :: {n['t']}")
p("--- D1/D2 English-residue word scan (non-en editions): nodes with English function words ---")
ENG = re.compile(r"\b(the|is|are|was|were|with|for|and|his|her|exactly|practice|collecting|points|budget|numbers)\b", re.I)
for code in EDITIONS:
    if code=="en": continue
    for pg in PAGES:
        for n in joined(code,pg):
            if ENG.search(n["t"]):
                p(f"  {code} {pg} y={n['y']:.1f} :: {n['t']}")

# ---------- D2 ----------
p("\n===== D2: P8 notes 132-135 (all editions) =====")
for code in EDITIONS:
    for n in joined(code,"p8-test"):
        if re.match(r"^13[2-5]\.", n["t"]):
            p(f"  {code} y={n['y']:.1f} :: {n['t']}")

# ---------- D3 ----------
p("\n===== D3: FR P4 gloss lines (full, in order) =====")
fr4 = joined("fr","p4-sport")
# gloss block: lines containing the parade/festival/U-Sport content; find by anchor phrases
for n in fr4:
    if any(k in n["t"] for k in ["défilé","Tianmu","supporters","Taipei double","U-Sport","concert sur"]):
        p(f"  y={n['y']:.1f} x={n['x']:.0f} fs={n['fs']} fam={n['fam']} :: {n['t']}")
p("--- D3 split-fragment check: any text node equal to/ending with fragments ---")
for code in ["fr"]:
    for pg in PAGES:
        for n in joined(code,pg):
            t=n["t"]
            if t in ("Tianm","u","u21","vill","ede","La vill","du") or t.endswith("Tianm") or t.startswith("u:") or t.startswith("ede "):
                p(f"  FRAGMENT {code} {pg} y={n['y']:.1f} :: {t!r}")

# ---------- D5 ----------
p("\n===== D5: P7 rect bottoms (rects with bottom > 2400) =====")
for code in EDITIONS:
    d = BASE/"files"/EDITIONS[code]/"svg"/"p7-lang.svg"
    root = ET.parse(d).getroot()
    rects=[]
    for el in root.iter(NS+"rect"):
        try:
            y=float(el.get("y",0)); h=float(el.get("height",0))
        except ValueError: continue
        if y+h>2400:
            rects.append((y,h,y+h,el.get("fill",""),el.get("stroke","")))
    for y,h,b,fill,stroke in sorted(rects):
        p(f"  {code}: rect y={y:.2f} h={h:.2f} bottom={b:.2f} fill={fill} stroke={stroke}")
    # footer rule lines
    for el in root.iter(NS+"line"):
        try: y1=float(el.get("y1",0)); y2=float(el.get("y2",0))
        except ValueError: continue
        if y1 in (2580,2580.0) or y2 in (2580,2580.0):
            p(f"  {code}: footer-rule line y1={y1} y2={y2} x1={el.get('x1')} x2={el.get('x2')} stroke={el.get('stroke')} width={el.get('stroke-width')}")
p("--- D5: P7 teaser text nodes es/fr/nl vs core (content multiset, y positions) ---")
for code in ["es","fr","nl"]:
    ts=[n for n in joined(code,"p7-lang") if n["y"]>2400]
    p(f"-- {code} P7 nodes y>2400:")
    for n in ts: p(f"   y={n['y']:.1f} x={n['x']:.0f} :: {n['t']}")
ts=[n for n in joined("en","p7-lang") if n["y"]>2400]
p("-- en P7 nodes y>2400:")
for n in ts: p(f"   y={n['y']:.1f} x={n['x']:.0f} :: {n['t']}")

# ---------- Badge + footer ----------
p("\n===== Badge (P1 y=378) + footers =====")
for code in EDITIONS:
    for n in joined(code,"p1-front"):
        if abs(n["y"]-378)<3:
            p(f"  {code} BADGE y={n['y']} fs={n['fs']} fill={n['fill']} :: {n['t']}")
    foots=set()
    for pg in PAGES:
        for n in joined(code,pg):
            if abs(n["y"]-2624)<3:
                foots.add(n["t"])
    for f in sorted(foots): p(f"  {code} FOOTER :: {f}")
    # page lines
    pls=set()
    for pg in PAGES:
        for n in joined(code,pg):
            if re.search(r"第 [1-8] 版|Seite \d|Página \d|Page \d|Pagina \d|Pagina \d|Bladzijde|Страница|ページ|쪽", n["t"]):
                pls.add(n["t"])
    for f in sorted(pls)[:10]: p(f"  {code} PAGELINE :: {f}")

# ---------- Level chips + exercise counts ----------
p("\n===== Level chips (occurrences of >A2< >B1< >B2<) =====")
for code in EDITIONS:
    tot=Counter(); perpage={}
    for pg in PAGES:
        s=(BASE/"files"/EDITIONS[code]/"svg"/f"{pg}.svg").read_text(encoding="utf-8")
        c={lv: len(re.findall(r">"+lv+r"<", s)) for lv in ["A2","B1","B2"]}
        perpage[pg]=c
        for k,v in c.items(): tot[k]+=v
    p(f"  {code}: TOTAL A2={tot['A2']} B1={tot['B1']} B2={tot['B2']} sum={sum(tot.values())} | per-page sums={[sum(perpage[pg].values()) for pg in PAGES]} | {perpage}")

# ---------- P7 phrases ----------
p("\n===== P7 phrases: verbatim counts (joined edition text, quotes stripped) =====")
PHRASES=["先列清單，再比價，最後才結帳","旅展四天，一次看完123個國家及城市","早晚溫差大，外套要隨身帶",
 "金馬影展，就是一年一度的大電影課","保險箱裡，裝的是高雄的勞動記憶","穿上紅色衣服，一起上街為龍隊喝采",
 "嘉年華不用門票，全家人都能來玩","回饋不是折價，實付金額才是真的"]
for code in EDITIONS:
    blob = alltext(code)
    counts=[blob.count(ph) for ph in PHRASES]
    p(f"  {code}: counts={counts} {'OK' if all(c==2 for c in counts) else 'MISMATCH'}")
    # also count P7-box quoted forms
    p7blob = alltext(code,"p7-lang")
    qc=[p7blob.count("「"+ph+"」") for ph in PHRASES]
    p(f"     P7 quoted forms: {qc}")

# ---------- Charts ----------
p("\n===== Charts: P4/P6 rect widths =====")
for code in EDITIONS:
    for pg in ["p4-sport","p6-deep"]:
        root = ET.parse(BASE/"files"/EDITIONS[code]/"svg"/f"{pg}.svg").getroot()
        ws=[]
        for el in root.iter(NS+"rect"):
            try: w=float(el.get("width",0)); h=float(el.get("height",0)); x=float(el.get("x",0)); y=float(el.get("y",0))
            except ValueError: continue
            if h>10 and w>20:
                ws.append((round(w,1),round(h,1),round(x,1),round(y,1),el.get("fill","")))
        ws.sort(key=lambda r:-r[0])
        p(f"  {code} {pg}: widest rects (w,h,x,y,fill): {ws[:8]}")

# ---------- Simplified-residue scan ----------
p("\n===== Simplified-residue scan =====")
SIMPL_ONLY = set("邮说国龙马发观欢对让认识语学读书报纸电话车门问间见风云气头为这那与从达运务义习乐丽万专东业国")  # candidates; adjudicate per hit with context
# NOTE: 国/东/发/业/动 etc. are valid Japanese kanji / Korean hanja — hits need context adjudication.
for code in EDITIONS:
    blob = alltext(code)
    hits={ch: blob.count(ch) for ch in SIMPL_ONLY if ch in blob}
    p(f"  {code}: simplified-candidate hits={hits}")
p("--- ja/ko added-string simplified scan (freeze added strings, with context) ---")
for code in ["ja","ko"]:
    fj=json.loads((G/f"freeze-{code}.json").read_text())
    added=[]
    for pg,dat in fj["pages"].items():
        for s in dat["added_strings"]: added.append(s["text"])
    for s in added:
        bad=[ch for ch in s if ch in set("说龙邮观欢让认语读报纸电话车门问间见风云气头为这那与从达运务义习乐丽万专个")]
        if bad:
            p(f"  {code}: chars={bad} :: {s}")

# ---------- Reader-facing sweep ----------
p("\n===== Reader-facing sweep (SVG text + text.md + ABSTRACT) =====")
TERMS=["W46","w46","2026-w46","zh-tw","zh_tw","SOP","proofread","校对","lint","GitHub","github","Discord","discord","insert.py","freeze.py","occlusion","kicker","masthead","cover","VOL.3 ","VOL.4"]
for code in EDITIONS:
    blob = alltext(code)
    md = next((BASE/"files"/EDITIONS[code]).glob("*.text.md")).read_text(encoding="utf-8")
    ab = (BASE/"files"/EDITIONS[code]/"ABSTRACT.txt").read_text(encoding="utf-8")
    found={}
    for t in TERMS:
        c = blob.count(t)+md.count(t)+ab.count(t)
        if c: found[t]=c
    p(f"  {code}: {found}")
    # show contexts for suspicious terms
    for t in ["SOP","proofread","lint","GitHub","Discord","zh-tw","W46"]:
        for n in joined(code):
            if t in n["t"]:
                p(f"    CTX {t} :: {n['t'][:160]}")

# ---------- W45 promises ----------
p("\n===== W45 promises: deferral disclosure + VOL.4 teaser =====")
for code in EDITIONS:
    p7 = alltext(code,"p7-lang")
    has_zh = "延期披露" in p7
    p(f"  {code}: Chinese deferral disclosure present={has_zh}")
    # print readers-corner/teaser region nodes
    for n in joined(code,"p7-lang"):
        if n["y"]>2380:
            p(f"    y={n['y']:.1f} :: {n['t']}")
    p("    ---")

# ---------- ABSTRACT checks ----------
p("\n===== ABSTRACT.txt checks =====")
LEARN_NEWS = ["learn Traditional Chinese by reading","by reading this week's","mit den Nachrichten","con las noticias","avec les nouvelles","ニュースで","뉴스로","met het nieuws","по новостям"]
for code in EDITIONS:
    ab=(BASE/"files"/EDITIONS[code]/"ABSTRACT.txt").read_text(encoding="utf-8")
    lines=ab.strip().split("\n")
    p(f"  {code}: lines={len(lines)} ascii-quote={'\"' in ab} bytes={len(ab.encode())} has150={'150' in ab} hasA2B2={('A2' in ab and 'B2' in ab)} learnnews={[w for w in LEARN_NEWS if w in ab]}")
    p(f"    :: {ab.strip()[:220]}")

# ---------- PDF checks ----------
p("\n===== PDF checks =====")
PDFNAMES={"en":("Lucerna-VOL3.pdf","Lucerna-VOL3-web.pdf"),"de":("Lucerna-VOL3-DE.pdf","Lucerna-VOL3-DE-web.pdf"),
 "es":("Lucerna-VOL3-ES.pdf","Lucerna-VOL3-ES-web.pdf"),"fr":("Lucerna-VOL3-FR.pdf","Lucerna-VOL3-FR-web.pdf"),
 "it":("Lucerna-VOL3-IT.pdf","Lucerna-VOL3-IT-web.pdf"),"ja":("Lucerna-VOL3-JA.pdf","Lucerna-VOL3-JA-web.pdf"),
 "ko":("Lucerna-VOL3-KO.pdf","Lucerna-VOL3-KO-web.pdf"),"nl":("Lucerna-VOL3-NL.pdf","Lucerna-VOL3-NL-web.pdf"),
 "pt":("Lucerna-VOL3-PT.pdf","Lucerna-VOL3-PT-web.pdf"),"ru":("Lucerna-VOL3-RU.pdf","Lucerna-VOL3-RU-web.pdf")}
for code,(pr,web) in PDFNAMES.items():
    d=BASE/"files"/EDITIONS[code]
    out={}
    for label,fn in [("print",pr),("web",web)]:
        fp=d/fn; sz=fp.stat().st_size
        r=subprocess.run(["pdftotext",str(fp),"-"],capture_output=True)
        out[label]=(sz,len(r.stdout),r.stdout)
    same = out["print"][2]==out["web"][2]
    p(f"  {code}: print={out['print'][0]}B txt={out['print'][1]}B | web={out['web'][0]}B txt={out['web'][1]}B | web<=7MB={out['web'][0]<=7*1024*1024} | print==web text: {same}")
    # text.md H1
    md = next(d.glob("*.text.md")).read_text(encoding="utf-8")
    p(f"    text.md first line: {md.splitlines()[0][:150] if md.splitlines() else ''}")

OUT.close()
print("analysis written:", G/"analysis-report.txt")
