#!/usr/bin/env python3
# Independent reproof for W45 zh-tw x ja (fixed render). Fresh code, ET parsing.
import xml.etree.ElementTree as ET, os, re, sys, json, hashlib, base64
from collections import Counter
GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = os.path.join(GOAL, "files/weekly-report-w45-zh-tw-ja")
CORE = os.path.join(GOAL, "files/weekly-report-w45-zhtw-core")
W43 = os.path.join(GOAL, "files/weekly-report-zh-tw-ja")
EDB = os.path.join(GOAL, "hidden_files/weekly-report-w45-zh-tw-ja-build")
COREB = os.path.join(GOAL, "hidden_files/weekly-report-w45-zhtw-build")
PAGES = ["p1-front.svg","p2-life.svg","p3-culture.svg","p4-sport.svg","p5-youth.svg","p6-deep.svg","p7-lang.svg","p8-test.svg"]

def nodes(d, fn):
    t = ET.parse(os.path.join(d, fn)); out=[]
    for e in t.getroot().iter():
        if e.tag.endswith('text'):
            out.append({'x':e.get('x'),'y':e.get('y'),'size':e.get('font-size'),
                        'fill':e.get('fill'),'weight':e.get('font-weight'),
                        'text': ''.join(e.itertext())})
    return out

def allnodes(d):
    return {fn: nodes(os.path.join(d,'svg'), fn) for fn in PAGES}

ed = allnodes(ED); core = allnodes(CORE); w43 = allnodes(W43)
tot = sum(len(v) for v in ed.values()); print(f"NODES edition total={tot} per-page={[len(ed[f]) for f in PAGES]}")
print(f"NODES core total={sum(len(v) for v in core.values())} w43 total={sum(len(v) for v in w43.values())}")

# ---- Gate 6 kinsoku (W43 precedent sets) ----
NO_START = set("。、，．！？：；）」』】％ー…‥・)]}〉》.,!?%:;\"")
SMALL = set("ぁぃぅぇぉっゃゅょゎゕゖァィゥェォッャュョヮヵヶ")
NO_END = set("「『（【〈《([{\"")
ns, sm, ne = [], [], []
for fn, ns_ in ed.items():
    for n in ns_:
        tx = n['text']
        if not tx: continue
        if tx[0] in SMALL: sm.append((fn, n['x'], n['y'], tx[:60]))
        elif tx[0] in NO_START: ns.append((fn, n['x'], n['y'], tx[:60]))
        if tx[-1] in NO_END: ne.append((fn, n['x'], n['y'], tx[:60]))
print(f"KINSOKU nodes={tot} NO_START={len(ns)} {ns[:5]} small-kana={len(sm)} {sm[:5]} NO_END={len(ne)} {ne[:5]}")
# W43 shipped re-scan
w_ns=w_sm=w_ne=0
for fn, ns_ in w43.items():
    for n in ns_:
        tx=n['text']
        if not tx: continue
        if tx[0] in SMALL: w_sm+=1
        elif tx[0] in NO_START: w_ns+=1
        if tx[-1] in NO_END: w_ne+=1
print(f"KINSOKU W43-shipped NO_START={w_ns} small={w_sm} NO_END={w_ne}")

# ---- Fix verification: P5 gloss + P8 key2 ----
print("--- P5 nodes containing コメディショー ---")
for n in ed["p5-youth.svg"]:
    if "コメディショー" in n['text'] or "JUMP" in n['text'] and "テコンドー" in n['text']:
        print(f"  x={n['x']} y={n['y']} :: {n['text']}")
print("--- P5 nodes starting with ィ (must be none) ---")
print([n for n in ed["p5-youth.svg"] if n['text'].startswith('ィ')])
print("--- P8 nodes containing コンベンション / エキシビション ---")
for n in ed["p8-test.svg"]:
    if "コンベンション" in n['text'] or "エキシビション" in n['text']:
        print(f"  x={n['x']} y={n['y']} :: {n['text']}")
print("--- P8 key2 area: nodes y in 1380..1460 on p8 ---")
for n in ed["p8-test.svg"]:
    try: y=float(n['y'])
    except: continue
    if 1380 <= y <= 1460: print(f"  x={n['x']} y={n['y']} :: {n['text'][:80]}")
old_p5 = "韓国のJUMPテコンドー・コメディショー"
new_p5 = "韓国のJUMPによるテコンドー・コメディショー"
joined_p5 = "".join(n['text'] for n in ed["p5-youth.svg"])
print(f"P5 old-fragment present={old_p5 in joined_p5} new-fragment present={new_p5 in joined_p5}")
joined_p8 = "".join(n['text'] for n in ed["p8-test.svg"])
print(f"P8 old 'アンド・エキシビション' present={'アンド・エキシビション' in joined_p8}")
print(f"P8 new 'コンベンション・エキシビション・センターで開催' present={'コンベンション・エキシビション・センターで開催' in joined_p8}")
print(f"P8 key2 subject present={'メインカンファレンスは香港' in joined_p8}")

# ---- Gate 2: CJK union + outside adjudication ----
CJK = re.compile(r"[\u2e80-\u9fff\u3040-\u30ff\uff00-\uffef]")
def cjkset(alln): return set(''.join(n['text'] for v in alln.values() for n in v))
edset, unionset = cjkset(ed), cjkset(w43) | cjkset(core)
outside = sorted(edset - unionset)
print(f"UNION edition={len(edset)} union={len(unionset)} outside={len(outside)}")
print("OUTSIDE:", outside)
KANA = re.compile(r"[\u3040-\u30ff]")
for ch in outside:
    hits=[]
    for fn, ns_ in ed.items():
        for n in ns_:
            if ch in n['text']: hits.append((fn, 'KANA' if KANA.search(n['text']) else 'NO-KANA', n['text'][:70]))
    nok = [h for h in hits if h[1]=='NO-KANA']
    print(f"  {ch}: nodes={len(hits)} no-kana-nodes={len(nok)} {nok[:3]}")

# Simplified-only spot list
SPOT = list("让说国学发对为经时车马龙凤云电动话语读认点头乐尔广厂厅开贝见长门问间队阳阴孙学宝实汉刘关应并复万与发")
core_strs = Counter(n['text'] for v in core.values() for n in v)
ed_strs = Counter(n['text'] for v in ed.values() for n in v)
shared = core_strs & ed_strs
spot_shared = {}
for s in shared:
    for ch in SPOT:
        if ch in s: spot_shared.setdefault(ch, []).append(s[:60])
print(f"SPOT over frozen shared strings: chars={list(spot_shared.keys())} hits={sum(len(v) for v in spot_shared.values())}")
spot_all = {}
for fn, ns_ in ed.items():
    for n in ns_:
        for ch in SPOT:
            if ch in n['text']: spot_all.setdefault(ch, []).append((fn, 'KANA' if KANA.search(n['text']) else 'NO-KANA', n['text'][:60]))
for ch, lst in spot_all.items():
    print(f"  SPOT-ALL {ch}: {len(lst)} no-kana={[x for x in lst if x[1]=='NO-KANA'][:3]}")

# ---- Gate 14: Latin sweep + 算一算 + apostrophes ----
LAT = re.compile(r"[A-Za-z]{2,}")
for fn, ns_ in ed.items():
    for n in ns_:
        if "'" in n['text'] or "’" in n['text']: print(f"APOS {fn} :: {n['text'][:80]}")
print("APOS scan done (ASCII ' and ’ above, if any)")
heads = ["Work it out","Did you get it","Over to you","Quick quiz","Headline words","This week","Word of the week","Practice example","Read the chart","Deep-read quiz","True or false","The big quiz","Read and answer","Say it in context","Test & keys","Language focus","Fill in"]
alltxt = {fn: "".join(n['text'] for n in ns_) for fn, ns_ in ed.items()}
for h in ["算一算 · 計算してみよう"] + heads:
    print(f"HEAD {h!r}: per-page={[alltxt[f].count(h) for f in PAGES]} total={sum(alltxt[f].count(h) for f in PAGES)}")
print("LATIN nodes (for adjudication):")
for fn, ns_ in ed.items():
    for n in ns_:
        if LAT.search(n['text']): print(f"  {fn} :: {n['text'][:100]}")

# ---- Gate 13: badge measured on all three P1s ----
for label, d in [("core", CORE), ("w43", W43), ("edition", ED)]:
    p1 = nodes(os.path.join(d,'svg'), "p1-front.svg")
    # badge: node containing the pairing text; print candidates near y=378
    cands = [n for n in p1 if n['y'] and abs(float(n['y'])-378) < 3]
    print(f"BADGE {label}: y~378 nodes={[(n['x'],n['y'],n['size'],n['fill'],n['weight'],n['text'][:60]) for n in cands]}")

# ---- Gate 12 readers corner: compare core vs edition P7 ----
def find_nodes(ns_, needle):
    return [n['text'] for n in ns_ if needle in n['text']]
for label, d in [("core", core), ("edition", ed)]:
    p7 = d["p7-lang.svg"]
    print(f"READERS {label} disclosure-nodes:")
    for n in p7:
        if "延期披露" in n['text'] or "本物の投書" in n['text'] or "あなたの手紙" in n['text'] or "Deferral" in n['text'] or "你的來信" in n['text']:
            print(f"   :: {n['text']}")
# line-for-line: Traditional letter+disclosure identical?
core_p7 = [n['text'] for n in core["p7-lang.svg"]]; ed_p7 = [n['text'] for n in ed["p7-lang.svg"]]
print(f"READERS trad-identical check: core P7 nodes={len(core_p7)} ed P7 nodes={len(ed_p7)}")
# Traditional nodes = those present in both (frozen); report any core Traditional node missing
cm, em = Counter(core_p7), Counter(ed_p7)
print("  core-only P7 strings:", [s[:60] for s in (cm-em)][:20])

# ---- Gate 9 gloss counts + images ----
for label, d in [("core", core), ("edition", ed)]:
    print(f"GLOSS {label}: per-page={[sum(1 for n in d[f] if n['text'].startswith('解説 — ') or n['text'].startswith('Notes｜')) for f in PAGES]}")
    print(f"  gloss-prefix nodes total core-style Notes={sum(1 for f in PAGES for n in d[f] if n['text'].startswith('Notes｜'))} ja-style={sum(1 for f in PAGES for n in d[f] if n['text'].startswith('解説 — '))}")
for label, d in [("core", CORE), ("edition", ED)]:
    import re as _re
    for fn in PAGES:
        raw = open(os.path.join(d,'svg',fn), encoding='utf-8').read()
        imgs = _re.findall(r"data:image/[^;]+;base64,([A-Za-z0-9+/=]+)", raw)
        print(f"IMG {label} {fn}: {[hashlib.sha256(base64.b64decode(i)).hexdigest()[:16] for i in imgs]}")
    # credits
    txt = "".join(n['text'] for f in PAGES for n in nodes(os.path.join(d,'svg'), f))
    print(f"  credits {label}: {[c for c in ['Wilfredor','CorraleH','Bain News Service','Benjamin Balazs'] if c in txt]}")

# ---- Gate 10 P7 golden sentences vs core content7 ----
import ast
def quotes(fn):
    src = open(fn, encoding='utf-8').read(); tree = ast.parse(src)
    out=[]
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str) and '、' in node.value and len(node.value) > 10:
            out.append(node.value)
    return out
# Instead: compare rendered P7 quote nodes directly core vs edition
print("P7 rendered core-vs-edition diff (multiset):")
cm, em = Counter(n['text'] for n in core["p7-lang.svg"]), Counter(n['text'] for n in ed["p7-lang.svg"])
print("  core-only:", [s[:60] for s in (cm-em)])
print("  ed-only (first 30):", [s[:60] for s in (em-cm)][:30])
# tags
print("P7 tags edition:", Counter(re.findall(r"\(p\. \d\)", "".join(n['text'] for n in ed["p7-lang.svg"]))))
print("P7 tags core:", Counter(re.findall(r"\(p\. \d\)", "".join(n['text'] for n in core["p7-lang.svg"]))))
# issue-wide counts of golden sentences: use core content7 quotes list
src = open(os.path.join(COREB, "content7.py"), encoding='utf-8').read()
m = re.search(r"quotes\s*=\s*\[(.*?)\]", src, re.S)
print("content7 quotes block found:", bool(m))
if m:
    qs = re.findall(r'"([^"]+)"', m.group(1))
    print(f"  quotes count={len(qs)}")
    def norm(s):
        return re.sub(r"\s+", "", s.replace("，", ",").replace("、", ","))
    for q in qs:
        ce = sum(norm(n['text']).count(norm(q)) for v in core.values() for n in v)
        ee = sum(norm(n['text']).count(norm(q)) for v in ed.values() for n in v)
        print(f"  quote {q[:30]}... core={ce} ed={ee}")
