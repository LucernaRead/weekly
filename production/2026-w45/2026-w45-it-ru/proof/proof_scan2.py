#!/usr/bin/env python3
"""Proof scan 2: freeze removed adjudication, golden joined counts, gloss source, counts, furniture per-page, badge context."""
import re, json, os
from xml.etree import ElementTree as ET

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE = f"{BASE}/files/weekly-report-w45-it-core/svg"
ED = f"{BASE}/files/weekly-report-w45-it-ru/svg"
W43 = f"{BASE}/files/weekly-report-it-ru/svg"
W43CORE = f"{BASE}/files/weekly-report-it-vol1/svg"
PAGES = ["p1-prima","p2-vita","p3-cultura","p4-sport","p5-giovani","p6-approfondimento","p7-lingua","p8-valutazione"]
OUT = []
def sec(t): OUT.append("\n### " + t)
def line(s): OUT.append(s)

def load_texts(path):
    tree = ET.parse(path); out = []
    for el in tree.iter():
        if el.tag.split("}")[-1] == "text":
            out.append({"x": el.get("x"), "y": el.get("y"), "fs": el.get("font-size"),
                        "anchor": el.get("text-anchor"), "fam": el.get("font-family"),
                        "weight": el.get("font-weight"), "text": "".join(el.itertext())})
    return out
def raw(p): return open(p, encoding="utf-8").read()
def has_cjk(s): return bool(re.search(r"[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7a3]", s))

# ---- freeze removed
sec("1d freeze-diff removed strings, adjudication")
d = json.load(open(f"{BASE}/hidden_files/w45/it-ru-proof/freeze-diff-proof.json"))
for pg, v in d["pages"].items():
    removed = v.get("removed_strings") or v.get("removed") or []
    # dump structure sample keys
    line(f"page {pg}: keys={list(v.keys())}")
    break
import pprint
for pg, v in d["pages"].items():
    rem = v.get("removed_strings", [])
    noncjk = [r for r in rem if not has_cjk(r["text"] if isinstance(r, dict) else r)]
    line(f"page {pg}: removed_total={len(rem)} nonCJK={len(noncjk)}")
    for r in noncjk:
        t = r["text"] if isinstance(r, dict) else r
        line(f"   NONCJK: {t!r}")
    # also list removed containing PAGINA
    for r in rem:
        t = r["text"] if isinstance(r, dict) else r
        if "PAGINA" in t:
            line(f"   PAGINA-removed: {t!r}")

# ---- core P7 FRASI tag nodes in order + ED FRASI nodes
sec("2e FRASI section nodes in order (core vs edition P7)")
for label, path in [("CORE", f"{CORE}/p7-lingua.svg"), ("ED", f"{ED}/p7-lingua.svg")]:
    ts = load_texts(path)
    line(f"--{label} nodes with y>=1700 (FRASI area) in doc order:")
    for t in ts:
        try: y = float(t["y"])
        except: continue
        if y >= 1700:
            line(f"   y={t['y']} x={t['x']} fs={t['fs']} {t['text']!r}")
    line(f"--{label} FRASI header node:")
    for t in ts:
        if "FRASI DELLA SETTIMANA" in t["text"]:
            line(f"   y={t['y']} {t['text']!r}")

# ---- golden joined-stream counts
sec("2f golden sentences joined-stream counts (whitespace-normalized, all 8 pages)")
def joined(ts_by_page):
    parts = []
    for p in PAGES:
        parts.append(" ".join(t["text"] for t in ts_by_page[p]))
    return re.sub(r"\s+", " ", " ".join(parts))
ce = {p: load_texts(f"{CORE}/{p}.svg") for p in PAGES}
ed = {p: load_texts(f"{ED}/{p}.svg") for p in PAGES}
cj, ej = joined(ce), joined(ed)
gold = ["arriva il primo freddo vero della stagione", "Non è una certezza, è una probabilità",
        "il 2 novembre è la Commemorazione dei defunti", "Fa freddo, copriti bene!",
        "il pubblico può assaggiare gratis", "il calcio non si ferma per il primo freddo",
        "la cultura continua", "Una probabilità alta non è una certezza"]
for g in gold:
    line(f"  {g!r}: core_joined={cj.count(g)} ed_joined={ej.count(g)} core_quoted={cj.count('«'+g+'»')} ed_quoted={ej.count('«'+g+'»')}")

# ---- gloss from source modules (read-only grep, no import)
sec("6d gloss() source strings: core build vs edition build (grep, read-only)")
for label, bdir in [("CORE-BUILD", f"{BASE}/hidden_files/weekly-report-w45-it-build"),
                    ("ED-BUILD", f"{BASE}/hidden_files/weekly-report-w45-it-ru-build")]:
    for mod in ["content12.py","content34.py","content56.py","content7.py"]:
        p = f"{bdir}/{mod}"
        if not os.path.exists(p): line(f"{label} {mod}: MISSING"); continue
        s = raw(p)
        # gloss( occurrences: print lines containing gloss(
        for m in re.finditer(r"gloss\((.*?)\)", s, re.S):
            arg = re.sub(r"\s+", " ", m.group(1))[:300]
            line(f"{label} {mod}: gloss({arg})")
sec("6e rendered P1 bridge/gloss node sequences")
for label, ts in [("CORE-P1", ce["p1-prima"]), ("ED-P1", ed["p1-prima"])]:
    line(f"--{label}:")
    for t in ts:
        if any(k in t["text"] for k in ["primo freddo", "versante", "previsione", "assaggi", "Пояснение", "讲解"]):
            line(f"   y={t['y']} x={t['x']} {t['text']!r}")
sec("6f rendered gloss box reconstruction per page (edition): join nodes from Пояснение start, next 12 nodes)")
for p in PAGES:
    ts = ed[p]
    for i, t in enumerate(ts):
        if t["text"].startswith("Пояснение"):
            seq = " ‖ ".join(x["text"] for x in ts[i:i+14])
            line(f"{p}: {seq!r}")
            break
    else:
        line(f"{p}: NO Пояснение-start node")

# ---- exercise + level counts from rendered SVGs
sec("12 exercise/level counts from rendered SVGs")
# Inspect level marking format first
for p in ["p1-prima"]:
    for t in ed[p]:
        if re.search(r"\[A2\]|\[B1\]|\[B2\]|A2|B1|B2", t["text"]) and len(t["text"]) < 40:
            line(f"ED {p} level-ish: y={t['y']} {t['text']!r}")
    for t in ce[p]:
        if re.search(r"\[A2\]|\[B1\]|\[B2\]", t["text"]):
            line(f"CORE {p} bracket-level: y={t['y']} {t['text']!r}")
# Count exercise numbers: nodes matching ^\d+\. or ^\d+–\d+\. in exercise regions is fragile; instead
# count [A2]/[B1]/[B2] badges across all pages
from collections import Counter
for label, tsd in [("CORE", ce), ("ED", ed)]:
    cnt = Counter(); pages_cnt = {}
    for p in PAGES:
        c = Counter()
        for t in tsd[p]:
            for m in re.finditer(r"\[(A2|B1|B2)\]", t["text"]):
                c[m.group(1)] += 1
        pages_cnt[p] = dict(c); cnt.update(c)
    line(f"{label} bracket-level totals: {dict(cnt)} per-page: {pages_cnt}")
# exercise number nodes: standalone 'N.' at line starts across P1-P7 + P8 keys region handled by p8
for label, tsd in [("CORE", ce), ("ED", ed)]:
    tot = []
    for p in PAGES:
        nums = set()
        for t in tsd[p]:
            m = re.match(r"\s*(\d{1,3})\.\s", t["text"])
            if m: nums.add(int(m.group(1)))
        tot.append((p, len(nums), min(nums) if nums else None, max(nums) if nums else None))
    line(f"{label} line-start N. counts per page: {tot}")

# ---- furniture per page W43 vs ED
sec("9b per-page furniture presence: footer / page line / gloss prefix (W43 vs ED)")
for p in PAGES:
    for label, d0 in [("W43", W43), ("ED", ED)]:
        ts = load_texts(f"{d0}/{p}.svg")
        foot = [t["text"] for t in ts if "ЕЖЕНЕДЕЛЬНИК" in t["text"]]
        pl = [t["text"] for t in ts if re.search(r"Страница \d+ из 8", t["text"])]
        gp = any(t["text"].startswith("Пояснение") for t in ts)
        line(f"{label} {p}: footer={foot} pageline={pl} gloss_prefix={gp}")
    line("---")

# ---- badge context: W43 core strapline, siblings, W43 P1 GIORNALE search
sec("8c W43 core P1 y-band + W43 P1 strapline search + siblings")
if os.path.exists(f"{W43CORE}/p1-prima.svg"):
    for t in load_texts(f"{W43CORE}/p1-prima.svg"):
        try: y = float(t["y"])
        except: continue
        if 340 <= y <= 420:
            line(f"W43CORE y={t['y']} x={t['x']} fs={t['fs']} {t['text']!r}")
else:
    line(f"W43 core dir missing: {W43CORE}")
for label, path in [("W43-ED", f"{W43}/p1-prima.svg"), ("W45-ED", f"{ED}/p1-prima.svg")]:
    for t in load_texts(path):
        if "GIORNALE" in t["text"] or "SETTIMANALE PER" in t["text"] or "ITALIA VERA" in t["text"]:
            line(f"{label} strapline-ish: y={t['y']} {t['text']!r}")
    line(f"{label} strapline search done")
for sib in ["it-de", "it-en", "it-fr"]:
    p = f"{BASE}/files/weekly-report-w45-{sib}/svg/p1-prima.svg"
    if os.path.exists(p):
        for t in load_texts(p):
            if "ОБЪЯСНЕНИЯ" in t["text"] or "EXPLANATIONS" in t["text"] or "EXPLICATIONS" in t["text"]:
                line(f"SIB {sib} badge: x={t['x']} y={t['y']} fs={t['fs']} w={t['weight']} {t['text']!r}")
    else:
        line(f"SIB {sib}: missing {p}")
sec("8d edition P1 band/headline geometry (raw elements near badge)")
s = raw(f"{ED}/p1-prima.svg")
for m in re.finditer(r"<rect[^>]*>", s):
    r = m.group(0)
    if 'y="54' in r or 'y="55' in r or 'y="56' in r or 'y="57' in r:
        line(f"ED P1 rect: {r[:220]}")
for t in ed["p1-prima"]:
    try: y = float(t["y"])
    except: continue
    if 540 <= y <= 640:
        line(f"ED P1 y={t['y']} x={t['x']} fs={t['fs']} {t['text']!r}")

# ---- images: <image> elements
sec("10b <image> elements per page")
for p in PAGES:
    for label, d0 in [("CORE", CORE), ("ED", ED)]:
        s = raw(f"{d0}/{p}.svg")
        imgs = re.findall(r"<image[^>]*>", s)
        line(f"{label} {p}: image_elements={len(imgs)} " + " | ".join(x[:160] for x in imgs))

# ---- ABSTRACT checks
sec("11 ABSTRACT checks")
a = raw(f"{BASE}/files/weekly-report-w45-it-ru/ABSTRACT.txt")
line(f"lines={a.count(chr(10))} ends_newline={a.endswith(chr(10))} ascii_dquote={a.count(chr(34))} chars={len(a)}")
line(f"text: {a!r}")
for k in ["La Lucerna", "итальян", "A2", "B2", "150", "учите итальянский", "первый холод", "поминовения", "панеттоне", "торроне", "Серии А"]:
    line(f"  contains {k!r}: {k in a}")

# ---- round hash diffs
sec("5c round hash diffs (build sha256 files)")
def parse_sha(p):
    d = {}
    for ln in open(p):
        parts = ln.split()
        if len(parts) >= 2: d[parts[1]] = parts[0]
    return d
r0 = parse_sha(f"{BASE}/hidden_files/weekly-report-w45-it-ru-build/sha256-r0.txt")
r1 = parse_sha(f"{BASE}/hidden_files/weekly-report-w45-it-ru-build/sha256-r1.txt")
r2 = parse_sha(f"{BASE}/hidden_files/weekly-report-w45-it-ru-build/sha256-r2.txt")
line(f"sha files keys: r0={len(r0)} r1={len(r1)} r2={len(r2)}")
for a, b, lbl in [(r0, r1, "R0->R1"), (r1, r2, "R1->R2")]:
    diff = [k for k in a if k in b and a[k] != b[k]]
    only = [k for k in set(a) ^ set(b)]
    line(f"{lbl} changed ({len(diff)}): {diff}")
    line(f"{lbl} key-only diffs: {only}")
    for k in sorted(set(a) | set(b)):
        if k not in a or k not in b: line(f"   {k}: r? missing one side")

# ---- model word counts, both口径
sec("12b model text word counts")
def model_words(ts):
    # find 'Testo modello:' node, collect following nodes until footer/section break: model is contiguous lines
    for i, t in enumerate(ts):
        if t["text"].startswith("Testo modello:"):
            buf = [t["text"][len("Testo modello:"):].strip()]
            for x in ts[i+1:i+12]:
                # stop at RISPOSTE header
                if x["text"].startswith("RISPOSTE"): break
                buf.append(x["text"])
            txt = " ".join(buf)
            return txt
    return None
for label, ts in [("CORE", ce["p8-valutazione"]), ("ED", ed["p8-valutazione"])]:
    txt = model_words(ts)
    words = txt.split() if txt else []
    line(f"{label} model words(body)={len(words)} label-inclusive={len(words)+2} identical_text_check_below")
    line(f"  {txt!r}")
mc, me = model_words(ce["p8-valutazione"]), model_words(ed["p8-valutazione"])
line(f"model byte-identical core vs ed: {mc == me}")

open(f"{BASE}/hidden_files/w45/it-ru-proof/scan2.txt", "w").write("\n".join(OUT))
print(f"wrote {len(OUT)} lines")
