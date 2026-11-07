#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os, re, hashlib, glob, subprocess, sys
import xml.etree.ElementTree as ET
from collections import Counter
ROOT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
GATE = os.path.join(ROOT, "hidden_files/w46/zh-cn-proofread-gates-round3")
FILES = os.path.join(ROOT, "files")
FIX3 = os.path.join(ROOT, "hidden_files/w46/zh-cn-fix-round3")
LANGS = ["en","de","es","fr","it","ja","ko","nl","pt","ru"]
ED = {l: os.path.join(FILES, "weekly-report-w46-zh-cn-core" if l=="en" else "weekly-report-w46-zh-cn-"+l) for l in LANGS}
OLD = "我拿了一个___包裹。"
NEW = "我拿了___包裹。"
DOUBLED = "我拿了一个个包裹"
out = open(os.path.join(GATE, "analyze-r3.log"), "w", encoding="utf-8")
def log(*a):
    print(*a)
    print(*a, file=out)
def svg_texts(path):
    tree = ET.parse(path)
    texts = []
    for el in tree.iter():
        if el.tag.endswith("text"):
            t = "".join(el.itertext()).strip()
            if t:
                texts.append(t)
    return texts
log("== STEM / CLINIC / GLOSS in P7 SVGs ==")
for l in LANGS:
    texts = svg_texts(os.path.join(ED[l], "svg/p7-ciyu.svg"))
    log(l, "NEW:", texts.count(NEW), "| OLD:", texts.count(OLD),
        "| clinic wrong:", texts.count("「我拿了两个包裹个」"),
        "| clinic right:", texts.count("→ 「我拿了两个包裹。」"),
        "| doubled:", sum(1 for t in texts if DOUBLED in t))
    log("   gloss 一个包裹 nodes:", [t for t in texts if "一个包裹" in t])
log("\n== OLD STEM: SVGs, .text.md, KITs ==")
for l in LANGS:
    n_svg = 0
    for f in glob.glob(os.path.join(ED[l], "svg/*.svg")):
        n_svg += open(f, encoding="utf-8").read().count(OLD)
    tm = glob.glob(os.path.join(ED[l], "*.text.md"))[0]
    s = open(tm, encoding="utf-8").read()
    kit = open(os.path.join(ED[l], "WEEKLY-KIT.md"), encoding="utf-8").read()
    log(l, "old-in-SVGs:", n_svg, "old-in-textmd:", s.count(OLD), "new-in-textmd:", s.count(NEW),
        "old-in-KIT:", kit.count(OLD), "new-in-KIT:", kit.count(NEW))
    log("   textmd line1379:", repr(s.splitlines()[1378]))
log("\n== BUILD SOURCES ==")
BUILDS = {"en": "weekly-report-w46-zhcn-build"}
for l in LANGS[1:]:
    BUILDS[l] = "weekly-report-w46-zh-cn-"+l+"-build"
for l in LANGS:
    bd = os.path.join(ROOT, "hidden_files", BUILDS[l])
    tot_old = tot_new = 0
    hits = []
    for f in glob.glob(os.path.join(bd, "*.py")):
        s = open(f, encoding="utf-8").read()
        tot_old += s.count(OLD); tot_new += s.count(NEW)
        if OLD in s or NEW in s:
            hits.append((os.path.basename(f), s.count(OLD), s.count(NEW)))
    c7 = open(os.path.join(bd, "content7.py"), encoding="utf-8").read().splitlines()
    log(l, "build old:", tot_old, "new:", tot_new, "hits:", hits, "| L19:", c7[18].strip()[:70], "|| L20:", c7[19].strip()[:70])
    allpy = "".join(open(f, encoding="utf-8").read() for f in glob.glob(os.path.join(bd, "*.py")))
    log("   oldkeyD3", allpy.count('["c", "b", "d", "a"]'), "fixedD3", allpy.count('["d", "c", "b", "a"]'),
        "oldkeyD4", allpy.count('["c", "d", "b", "a"]'), "fixedD4", allpy.count('["c", "d", "a", "b"]'))
log("\n== P8 note101 + D3/D4 keys (SVG text) ==")
for l in LANGS:
    texts = svg_texts(os.path.join(ED[l], "svg/p8-ceyan.svg"))
    log(l, "101:", [t for t in texts if t.startswith("101.")])
    for n in (25, 26, 27, 99, 100):
        log("   ", n, [t for t in texts if re.match(r"^"+str(n)+r"\.\s", t)][:2])
log("\n== P8 note101 vs BEFORE-quotes (pre-fix evidence) ==")
before = open(os.path.join(FIX3, "before-quotes.txt"), encoding="utf-8").read()
after = open(os.path.join(FIX3, "after-quotes.txt"), encoding="utf-8").read()
for l in LANGS:
    texts = svg_texts(os.path.join(ED[l], "svg/p8-ceyan.svg"))
    n101 = [t for t in texts if t.startswith("101.")][0]
    log(l, "in before:", n101 in before, "| in after:", n101 in after, "|", n101)
log("\n== P8 HASHES current vs pre-fix snapshot ==")
pre = {}
for line in open(os.path.join(FIX3, "pre-fix-p8-hashes.txt"), encoding="utf-8"):
    h, p = line.split()
    pre[p] = h
mismatch = 0
for l in LANGS:
    dname = "weekly-report-w46-zh-cn-core" if l == "en" else "weekly-report-w46-zh-cn-"+l
    for kind in ("svg/p8-ceyan.svg", "cards/p8-ceyan.png"):
        p = os.path.join(FILES, dname, kind)
        h = hashlib.sha256(open(p, "rb").read()).hexdigest()
        ok = (h == pre.get(dname+"/"+kind))
        if not ok:
            mismatch += 1
        log(l, kind, h, "MATCH" if ok else "MISMATCH pre="+str(pre.get(dname+"/"+kind)))
log("P8 hash mismatches:", mismatch, "/20")
log("\n== FULL EDITION HASH DIFF vs pre-fix snapshot ==")
pre_ed = {}
for line in open(os.path.join(FIX3, "pre-fix-edition-hashes.txt"), encoding="utf-8"):
    parts = line.split()
    if len(parts) >= 2:
        pre_ed[parts[1]] = parts[0]
cur = {}
for l in LANGS:
    dname = "weekly-report-w46-zh-cn-core" if l == "en" else "weekly-report-w46-zh-cn-"+l
    base = os.path.join(FILES, dname)
    for root, _, files in os.walk(base):
        for f in sorted(files):
            fp = os.path.join(root, f)
            cur[os.path.relpath(fp, FILES)] = hashlib.sha256(open(fp, "rb").read()).hexdigest()
changed = sorted([k for k in cur if pre_ed.get(k) != cur[k]])
log("current files:", len(cur), "pre-fix snapshot:", len(pre_ed), "changed:", len(changed))
for l in LANGS:
    dname = "weekly-report-w46-zh-cn-core" if l == "en" else "weekly-report-w46-zh-cn-"+l
    ch = [c for c in changed if c.startswith(dname+"/")]
    log(l, "changed vs pre-fix:", len(ch), ch)
with open(os.path.join(GATE, "current-edition-hashes.txt"), "w") as f:
    for k in sorted(cur):
        f.write(cur[k]+"  "+k+"\n")
with open(os.path.join(GATE, "hash-diff-pre-vs-current.txt"), "w") as f:
    for k in changed:
        f.write(k+"\n")
PHRASES = ["双11的正日子","先看结算页，再决定买不买","提高自防自救能力","三支队进了八强","输了就回家","老电影，新画面","快递的高峰分三波","着火了不坐电梯"]
log("\n== PHRASES / CHART ==")
for l in LANGS:
    alltexts = []
    for f in sorted(glob.glob(os.path.join(ED[l], "svg/*.svg"))):
        alltexts += svg_texts(f)
    joined = "\n".join(alltexts)
    log(l, "phrases:", {p: joined.count(p) for p in PHRASES})
    p6 = open(os.path.join(ED[l], "svg/p6-shendu.svg"), encoding="utf-8").read()
    rects = re.findall(r'<rect[^>]*>', p6)
    sel = [r for r in rects if 'x="325"' in r]
    log("   P6 x=325 rects:", len(sel))
    for r in sel:
        log("     ", r[:200])
log("\n== KINSOKU ==")
OPEN = set("（［｛「『【〈《“‘")
CLOSE = set("、。．，；：？！）］｝」』】〉》”’")
for l in LANGS:
    bs = be = 0
    ex = []
    for f in sorted(glob.glob(os.path.join(ED[l], "svg/*.svg"))):
        for t in svg_texts(f):
            if t and t[0] in CLOSE:
                bs += 1; ex.append(("start", os.path.basename(f), t[:30]))
            if t and t[-1] in OPEN:
                be += 1; ex.append(("end", os.path.basename(f), t[-30:]))
    log(l, "kinsoku start:", bs, "end:", be, ex[:5])
log("\n== ABSTRACT.txt ==")
for l in LANGS:
    b = open(os.path.join(ED[l], "ABSTRACT.txt"), "rb").read()
    s = b.decode("utf-8")
    log(l, "bytes:", len(b), "NLs:", s.count("\n"), "trailingNL:", s.endswith("\n"),
        "asciiDQ:", s.count('"'), "Lucerna:", "Lucerna" in s, "VOL.3:", "VOL.3" in s,
        "A2:", "A2" in s, "150:", "150" in s, "|", s[:110].replace("\n", " "))
log("\n== PDF TEXT LAYER / SIZES ==")
WEBNAME = {"en":"Lucerna-VOL3-web.pdf","de":"Lucerna-VOL3-DE-web.pdf","es":"Lucerna-VOL3-ES-web.pdf","fr":"Lucerna-VOL3-FR-web.pdf","it":"Lucerna-VOL3-IT-web.pdf","ja":"Lucerna-VOL3-JA-web.pdf","ko":"Lucerna-VOL3-KO-web.pdf","nl":"Lucerna-VOL3-NL-web.pdf","pt":"Lucerna-VOL3-PT-web.pdf","ru":"Lucerna-VOL3-RU-web.pdf"}
PRINTNAME = {"en":"Lucerna-VOL3.pdf","de":"Lucerna-VOL3-DE.pdf","es":"Lucerna-VOL3-ES.pdf","fr":"Lucerna-VOL3-FR.pdf","it":"Lucerna-VOL3-IT.pdf","ja":"Lucerna-VOL3-JA.pdf","ko":"Lucerna-VOL3-KO.pdf","nl":"Lucerna-VOL3-NL.pdf","pt":"Lucerna-VOL3-PT.pdf","ru":"Lucerna-VOL3-RU.pdf"}
for l in LANGS:
    web = os.path.join(ED[l], WEBNAME[l]); pr = os.path.join(ED[l], PRINTNAME[l])
    tw = subprocess.run(["pdftotext", web, "-"], capture_output=True).stdout
    tp = subprocess.run(["pdftotext", pr, "-"], capture_output=True).stdout
    pw = subprocess.run(["pdfinfo", web], capture_output=True, text=True).stdout
    pages = [x for x in pw.splitlines() if x.startswith("Pages:")]
    open(os.path.join(GATE, "pdftext-web-"+l+".txt"), "wb").write(tw)
    open(os.path.join(GATE, "pdftext-print-"+l+".txt"), "wb").write(tp)
    tws = tw.decode("utf-8", "ignore")
    log(l, "web bytes:", os.path.getsize(web), "<=7MB:", os.path.getsize(web) <= 7*1024*1024,
        "| web text:", len(tw), "print text:", len(tp), "identical:", tw == tp, pages,
        "| old in web:", tws.count(OLD), "new:", tws.count(NEW), "doubled:", tws.count(DOUBLED))
log("\n== ES p. SURVIVAL ==")
for l in LANGS:
    tm = glob.glob(os.path.join(ED[l], "*.text.md"))[0]
    s = open(tm, encoding="utf-8").read()
    log(l, "old instr:", s.count("Responde con fechas y números de la página"),
        "| p.3:", s.count("Responde con fechas y números de la p. 3."),
        "| p.5:", s.count("Responde con fechas y números de la p. 5."))
es_tm = open(glob.glob(os.path.join(ED["es"], "*.text.md"))[0], encoding="utf-8").read().splitlines()
log("ES line623:", repr(es_tm[622]))
log("ES line1063:", repr(es_tm[1062]))
out.close()
print("ANALYZE DONE")
