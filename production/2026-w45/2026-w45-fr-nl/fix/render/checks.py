# -*- coding: utf-8 -*-
"""FR x NL W45 builder checks (run with tools venv python)."""
import re, sys, os, hashlib, base64
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools"))
from svglib import text_w
from occlusion_audit import ink_box

G = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = os.path.join(G, "hidden_files/w45/fr-nl-fix/render/svg")
CO = os.path.join(G, "files/weekly-report-w45-fr-core/svg")
W43 = os.path.join(G, "files/weekly-report-fr-nl/svg")
PAGES = ["p1-une", "p2-vie", "p3-culture", "p4-sport", "p5-jeunesse",
         "p6-politique", "p7-langue", "p8-exercices"]
ATTR = re.compile(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]*)" font-size="([\d.]+)"([^>]*)>([^<]*)</text>')

def texts(path):
    t = open(path, encoding="utf-8").read()
    out = []
    for m in ATTR.finditer(t):
        attrs = m.group(5)
        bold = 'font-weight="700"' in attrs
        am = re.search(r'text-anchor="([^"]*)"', attrs)
        out.append(dict(x=float(m.group(1)), y=float(m.group(2)), fam=m.group(3),
                        size=float(m.group(4)), bold=bold,
                        anchor=am.group(1) if am else "start", s=m.group(6)))
    return out

def adv(e):
    kind = "serif" if "Serif" in e["fam"] else "sans"
    return text_w(e["s"], kind, e["bold"], e["size"])

def ink(e):
    # returns (l, t, r, b) in svg coords or None
    try:
        return ink_box(e["s"], e["fam"], e["size"], e["bold"], e["x"], e["y"], e["anchor"])
    except Exception as ex:
        return ("ERR", str(ex))

print("== A. same-baseline spacing (P1 top y=92, footers y=2624) ==")
for pg in PAGES:
    ts = [e for e in texts(os.path.join(ED, pg + ".svg")) if e["y"] in (92.0, 2624.0)]
    for y in (92.0, 2624.0):
        row = sorted([e for e in ts if e["y"] == y], key=lambda e: e["x"])
        if len(row) < 2:
            continue
        gaps = []
        for a, b in zip(row, row[1:]):
            ia, ib = ink(a), ink(b)
            if isinstance(ia, tuple) and len(ia) == 4 and isinstance(ib, tuple) and len(ib) == 4:
                gaps.append(round(ib[0] - ia[2], 1))
        print(f"  {pg} y={y}: {len(row)} segments, ink gaps {gaps} {'OVERLAP!' if any(g < 0 for g in gaps) else 'ok'}")

print("== B. right-edge scan (advance end > 1885; ink right > 1885) ==")
for pg in PAGES:
    for e in texts(os.path.join(ED, pg + ".svg")):
        a = adv(e)
        if e["anchor"] == "start":
            ae = e["x"] + a
        elif e["anchor"] == "middle":
            ae = e["x"] + a / 2
        else:
            ae = e["x"]
        ib = ink(e)
        ir = ib[2] if isinstance(ib, tuple) and len(ib) == 4 else None
        if ae > 1885 or (ir is not None and ir > 1885):
            print(f"  {pg}: adv_end={ae:.1f} ink_right={ir} :: {e['s'][:80]}")

print("== C. P6 chart-label baseline-anchored coverage ==")
# chart rect: x 65..961, y 1330..1800 on p6; coverage vs any opaque rect
# on the page other than the chart's own box (drawn before its texts)
raw = open(os.path.join(ED, "p6-politique.svg"), encoding="utf-8").read()
rects = [(float(a), float(b), float(a) + float(c), float(b) + float(d))
         for a, b, c, d, f in re.findall(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*fill="([^"]*)"', raw) if f != "none"]
chart_texts = [e for e in texts(os.path.join(ED, "p6-politique.svg"))
               if 1330 <= e["y"] <= 1800 and 65 <= e["x"] <= 961]
maxcov = 0.0
for e in chart_texts:
    ib = ink(e)
    if not (isinstance(ib, tuple) and len(ib) == 4):
        continue
    l, t, r, b = ib
    area = max(0.0, (r - l) * (b - t))
    if area == 0:
        continue
    cov = 0.0
    for (rl, rt, rr, rb) in rects:
        if abs(rl - 65) < 1 and abs(rt - 1330) < 1:
            continue
        ow = max(0.0, min(r, rr) - max(l, rl)); oh = max(0.0, min(b, rb) - max(t, rt))
        cov = max(cov, ow * oh / area)
    maxcov = max(maxcov, cov)
    if cov > 0:
        print(f"  chart text cov {cov:.1%}: {e['s'][:60]}")
print(f"  P6 chart texts: {len(chart_texts)}, max baseline-anchored coverage {maxcov:.1%} (gate <30%)")

print("== D. orphan scan, y-gap window 10-45 ==")
print("  definition: blocks = same page/x/size/family, consecutive y gaps in [10,45];")
print("  flags: (i) line starting with . , ; : ! ? % ) ] } (ii) final line = single token <=3 chars")
for pg in PAGES:
    ts = texts(os.path.join(ED, pg + ".svg"))
    ts.sort(key=lambda e: (round(e["x"], 1), e["y"]))
    blocks, cur = [], []
    for e in ts:
        if cur and (round(e["x"], 1) != round(cur[-1]["x"], 1) or e["size"] != cur[-1]["size"]
                    or e["fam"] != cur[-1]["fam"] or not (10 <= e["y"] - cur[-1]["y"] <= 45)):
            blocks.append(cur); cur = []
        cur.append(e)
    if cur:
        blocks.append(cur)
    for bl in blocks:
        if len(bl) < 2:
            continue
        first, last = bl[0], bl[-1]
        s0 = first["s"].lstrip()
        if s0 and s0[0] in ".,;:!?%)]}":
            print(f"  {pg} LINE-START-PUNCT y={first['y']}: {first['s'][:60]}")
        lt = last["s"].strip()
        toks = lt.split()
        if len(toks) == 1 and len(lt) <= 3:
            print(f"  {pg} ORPHAN-SHORT-FINAL y={last['y']}: {lt!r} (block {len(bl)} lines)")
    # same scan on core for comparison of frozen blocks
print("  (core comparison: identical scan on core SVGs)")
for pg in PAGES:
    ts = texts(os.path.join(CO, pg + ".svg"))
    ts.sort(key=lambda e: (round(e["x"], 1), e["y"]))
    blocks, cur = [], []
    for e in ts:
        if cur and (round(e["x"], 1) != round(cur[-1]["x"], 1) or e["size"] != cur[-1]["size"]
                    or e["fam"] != cur[-1]["fam"] or not (10 <= e["y"] - cur[-1]["y"] <= 45)):
            blocks.append(cur); cur = []
        cur.append(e)
    if cur:
        blocks.append(cur)
    for bl in blocks:
        if len(bl) < 2:
            continue
        first, last = bl[0], bl[-1]
        s0 = first["s"].lstrip()
        if s0 and s0[0] in ".,;:!?%)]}":
            print(f"  CORE {pg} LINE-START-PUNCT y={first['y']}: {first['s'][:60]}")
        lt = last["s"].strip()
        if len(lt.split()) == 1 and len(lt) <= 3:
            print(f"  CORE {pg} ORPHAN-SHORT-FINAL y={last['y']}: {lt!r}")

print("== E. gloss counts (source gloss() strings, split on bare ·) ==")
import glob
tot = 0
for f in ["content12.py", "content34.py", "content56.py"]:
    src = open(os.path.join(HERE, f), encoding="utf-8").read()
    for m in re.finditer(r'\.gloss\("([^"]*)"\)', src):
        items = [x for x in m.group(1).split("·")]
        print(f"  {f}: {len(items)} items :: {m.group(1)[:50]}...")
        tot += len(items)
print(f"  TOTAL gloss items: {tot} (core 38)")

print("== F. CJK in edition SVGs ==")
CJK = re.compile(r'[\u4e00-\u9fff]')
for pg in PAGES:
    t = open(os.path.join(ED, pg + ".svg"), encoding="utf-8").read()
    txt = " ".join(re.findall(r'<text[^>]*>([^<]*)</text>', t))
    print(f"  {pg}: CJK chars in text nodes = {len(CJK.findall(txt))}")

print("== G. frozen French spot checks ==")
checks = [
    ("p4-sport", "41e édition en 2026 (40e anniversaire)"),
    ("p8-exercices", "Si j'étais libre dimanche, j'___ à Nanterre."),
    ("p7-langue", "plus excitante ou plus frustrante ?"),
    ("p7-langue", "Les jeunes créateurs y rencontrent leur public, en vrai."),
    ("p6-politique", "Ce calendrier peut encore bouger."),
    ("p8-exercices", "si + imparfait → conditionnel; j' = je geëlideerd"),
]
for pg, s in checks:
    t = open(os.path.join(ED, pg + ".svg"), encoding="utf-8").read()
    print(f"  {pg} {'FOUND' if s in t else 'MISSING'}: {s[:60]}")
for tok in ["40e", "41e"]:
    hits = []
    for pg in PAGES:
        t = open(os.path.join(ED, pg + ".svg"), encoding="utf-8").read()
        txt = " ".join(re.findall(r'<text[^>]*>([^<]*)</text>', t))
        if tok in txt:
            hits.append((pg, txt.count(tok)))
    print(f"  token {tok}: {hits}")
# Q120 options + key + neighbours untouched (compare core vs edition P8 text nodes for Q119-121 region)
print("== H. images: payload double-hash vs core ==")
for pg in ["p1-une", "p2-vie", "p3-culture"]:
    for label, d in [("ed", ED), ("core", CO)]:
        t = open(os.path.join(d, pg + ".svg"), encoding="utf-8").read()
        for m in re.finditer(r'<image[^>]*href="data:image/(jpeg|png);base64,([^"]+)"', t):
            raw = base64.b64decode(m.group(2))
            print(f"  {pg} {label}: b64-sha256={hashlib.sha256(m.group(2).encode()).hexdigest()[:16]} decoded-sha256={hashlib.sha256(raw).hexdigest()[:16]} bytes={len(raw)}")
for pg, cred in [("p1-une", "Eugène Atget (1857-1927)"), ("p2-vie", "Utagawa Hiroshige (1797-1858)"), ("p3-culture", "Flora de Filipinas (Blanco)")]:
    t = open(os.path.join(ED, pg + ".svg"), encoding="utf-8").read()
    print(f"  {pg} credit {'FOUND' if cred in t else 'MISSING'}: {cred}")

print("== I. furniture ==")
for pg in PAGES:
    ts = texts(os.path.join(ED, pg + ".svg"))
    foots = [e["s"] for e in ts if e["y"] == 2624.0]
    print(f"  {pg} footer: {foots}")
p1 = texts(os.path.join(ED, "p1-une.svg"))
badge = [e for e in p1 if e["y"] == 574.0]
print(f"  P1 badge: {badge}")
p8 = texts(os.path.join(ED, "p8-exercices.svg"))
seps = [e["s"] for e in p8 if e["s"].startswith("— PAGINA")]
print(f"  P8 separators: {seps}")
print("== J. forbidden term + reader corner ==")
bad = 0
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py", "bslib4.py", "transform.py"]:
    t = open(os.path.join(HERE, f), encoding="utf-8").read()
    if "\u6865\u63a5" in t:
        bad += 1; print(f"  {f}: CONTAINS forbidden term")
for pg in PAGES:
    t = open(os.path.join(ED, pg + ".svg"), encoding="utf-8").read()
    if "\u6865\u63a5" in t:
        bad += 1; print(f"  {pg}.svg: CONTAINS forbidden term")
print(f"  forbidden-term hits: {bad}")
p7t = " ".join(e["s"] for e in texts(os.path.join(ED, "p7-langue.svg")))
for s in ["Exemple de la rédaction (ce texte n'est pas une lettre de lecteur)",
          "Stuur je brief én je beste pagina-8-tekst in voor VOL.4!",
          "geen echte brieven en geen beste VOL.2-pagina-8-tekst binnen",
          "beide volgen in VOL.4",
          "Note de la rédaction : aucun texte du VOL.2"]:
    print(f"  reader-corner {'FOUND' if s in p7t else 'MISSING'}: {s[:60]}")
print("== K. registry level/type multiset vs core (source args) ==")
def regtokens(d):
    out = []
    for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        src = open(os.path.join(d, f), encoding="utf-8").read()
        out += re.findall(r'"(A2|B1|B2)"', src)
    from collections import Counter
    return Counter(out)
print("  core build:", dict(regtokens(os.path.join(G, "hidden_files/weekly-report-w45-fr-build"))))
print("  nl build:  ", dict(regtokens(HERE)))
