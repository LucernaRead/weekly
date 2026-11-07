#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""W45 FRxNL proofround-2 own checks (text/geometry/furniture/images)."""
import re, sys, os, json, html, base64, hashlib
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools"))
from occlusion_audit import ink_box, get_font, SCALE
from pathlib import Path
G = Path.home() / "workspace/goals/lucernaread-social-media-operations"
ED = G / "files/weekly-report-w45-fr-nl/svg"
CO = G / "files/weekly-report-w45-fr-core/svg"
W43 = G / "files/weekly-report-fr-nl/svg"
PAGES = ["p1-une", "p2-vie", "p3-culture", "p4-sport", "p5-jeunesse",
         "p6-politique", "p7-langue", "p8-exercices"]
ATTR = re.compile(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]*)" font-size="([\d.]+)"([^>]*)>([^<]*)</text>')
RECT = re.compile(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*>')

def texts(p):
    raw = p.read_text(encoding="utf-8")
    out = []
    for m in ATTR.finditer(raw):
        x, y, fam, fs, rest, s = float(m.group(1)), float(m.group(2)), m.group(3), float(m.group(4)), m.group(5), html.unescape(m.group(6))
        bold = 'font-weight="700"' in rest
        am = re.search(r'text-anchor="([^"]*)"', rest); anchor = am.group(1) if am else "start"
        out.append(dict(x=x, y=y, fam=fam, size=fs, bold=bold, anchor=anchor, s=s))
    return out, raw

def joined(d):
    per = {}
    for pn in PAGES:
        els, _ = texts(d / f"{pn}.svg")
        per[pn] = " ".join(e["s"] for e in els if e["s"].strip())
    return per

EDJ, COJ = joined(ED), joined(CO)
EDALL, COALL = " ".join(EDJ.values()), " ".join(COJ.values())

print("===== A. P4 commentator box (serif 21.5, x~1007) =====")
p4, _ = texts(ED / "p4-sport.svg")
box = [e for e in p4 if e["size"] == 21.5 and abs(e["x"] - 1007) < 5]
for e in sorted(box, key=lambda e: e["y"]):
    ib = ink_box(e["s"], e["fam"], e["size"], e["bold"], e["x"], e["y"], e["anchor"])
    print(f"  y={e['y']} ink=({ib[0]:.2f},{ib[2]:.2f}) w={ib[2]-ib[0]:.2f} :: {e['s']!r}")
print("  first-line starts with '!':", any(e["s"].strip().startswith("!") for e in box))
p4c, _ = texts(CO / "p4-sport.svg")
boxc = [e for e in p4c if e["size"] == 21.5 and abs(e["x"] - 1007) < 5]
print("  CORE box lines:")
for e in sorted(boxc, key=lambda e: e["y"]):
    print(f"  y={e['y']} :: {e['s']!r}")
# byte-level French segments in cheer lines
for label, els in [("ED", box), ("CORE", boxc)]:
    for e in els:
        if "Quelle action" in e["s"]:
            seg = e["s"]
            print(f"  {label} cheer node bytes: {seg.encode('utf-8')!r}")

print("===== B. frozen strings (concatenated page text) =====")
checks = [
    ("P4 41e string", "p4-sport", "41e édition en 2026 (40e anniversaire)"),
    ("P8 Q120 stem", "p8-exercices", "Si j'étais libre dimanche, j'___ à Nanterre."),
    ("P8 Q120 opts", "p8-exercices", "A. irai · B. irais · C. vais"),
    ("P8 Q120 note", "p8-exercices", "si + imparfait → conditionnel; j' = je geëlideerd"),
    ("P8 Q119 stem", "p8-exercices", "Elle s'intéresse ___ festivals."),
    ("P8 Q121 stem", "p8-exercices", "À mon avis, ce programme ___ très riche."),
    ("P7 #4 verbatim", "p7-langue", "plus excitante ou plus frustrante ?"),
    ("P7 #8 verbatim", "p7-langue", "Les jeunes créateurs y rencontrent leur public, en vrai."),
    ("P6 sync", "p6-politique", "Ce calendrier peut encore bouger."),
    ("P4 40e count", "p4-sport", None),
]
for name, pg, s in checks:
    if s is None:
        print(f"  {name}: ED '40e' count={EDJ[pg].count('40e')} '41e' count={EDJ[pg].count('41e')} | CORE '40e'={COJ[pg].count('40e')} '41e'={COJ[pg].count('41e')} | whole-ED '40e'={EDALL.count('40e')}")
    else:
        print(f"  {name}: ED={'FOUND' if s in EDJ[pg] else 'MISSING'} CORE={'FOUND' if s in COJ[pg] else 'MISSING'} :: {s[:70]}")
print("  P7 French definition heads in ED:")
for h in ["REPRENDRE", "FUTUR PROCHE", "PASSÉ COMPOSÉ", "COMPARATIF", "SUBJONCTIF", "ATTENTE"]:
    print(f"    {h}: ED={h in EDJ['p7-langue']} CORE={h in COJ['p7-langue']}")

print("===== C. freeze-diff added/removed classification =====")
fd = json.load(open(G / "hidden_files/w45/fr-nl-proof2/work/freeze-diff.json"))
CJK = re.compile(r"[\u2e80-\u9fff\u3040-\u30ff\uff00-\uffef]")
for pg, v in fd["pages"].items():
    added, removed = v.get("added", []), v.get("removed", [])
    pure_fr_removed = [s for s in removed if not CJK.search(s)]
    print(f"  p{pg}: +{len(added)} -{len(removed)} removed-without-CJK={len(pure_fr_removed)}")
    for s in pure_fr_removed:
        print(f"      REMOVED-noCJK: {s[:110]!r}")

print("===== D. right-edge scan (ink>1885 or adv>1885) =====")
def adv_end(e):
    f = get_font(e["fam"], e["size"], e["bold"]); adv = f.getlength(e["s"]) / SCALE
    if e["anchor"] == "middle": return e["x"] + adv / 2
    if e["anchor"] == "end": return e["x"]
    return e["x"] + adv
for label, d in [("ED", ED), ("CORE", CO)]:
    for pn in PAGES:
        els, _ = texts(d / f"{pn}.svg")
        for e in els:
            ib = ink_box(e["s"], e["fam"], e["size"], e["bold"], e["x"], e["y"], e["anchor"])
            if ib is None: continue
            ae = adv_end(e)
            if ib[2] > 1885 or ae > 1885:
                print(f"  {label} {pn} y={e['y']} adv={ae:.2f} ink_right={ib[2]:.2f} :: {e['s'][:70]!r}")

print("===== E. same-baseline spacing P1 y=92 + footers y=2624 =====")
for label, d in [("ED", ED), ("CORE", CO)]:
    for pn in PAGES:
        els, _ = texts(d / f"{pn}.svg")
        for yy in (92.0, 2624.0):
            segs = []
            for e in els:
                if e["y"] == yy:
                    ib = ink_box(e["s"], e["fam"], e["size"], e["bold"], e["x"], e["y"], e["anchor"])
                    if ib: segs.append((ib[0], ib[2]))
            segs.sort()
            gaps = [round(segs[i+1][0] - segs[i][1], 1) for i in range(len(segs)-1)]
            print(f"  {label} {pn} y={yy}: {len(segs)} segs gaps={gaps}")

print("===== F. orphan scan window 10-45 (line-start punct + short-final) =====")
def orphans(d):
    out = []
    for pn in PAGES:
        els, _ = texts(d / f"{pn}.svg")
        els_sorted = sorted(els, key=lambda e: (e["x"], e["size"], e["fam"], e["y"]))
        blocks = []; cur = []
        for e in els_sorted:
            if cur and (e["x"], e["size"], e["fam"]) == (cur[-1]["x"], cur[-1]["size"], cur[-1]["fam"]) and 10 <= e["y"] - cur[-1]["y"] <= 45:
                cur.append(e)
            else:
                if len(cur) >= 2: blocks.append(cur)
                cur = [e]
        if len(cur) >= 2: blocks.append(cur)
        for b in blocks:
            for e in b[1:]:
                s = e["s"].strip()
                if s and s[0] in ".,;:!?%)]}":
                    out.append((pn, e["y"], "LINESTART", s))
            last = b[-1]["s"].strip(); toks = last.split()
            if len(toks) == 1 and len(toks[0]) <= 3:
                out.append((pn, b[-1]["y"], "SHORT-FINAL", last))
    return out
EDO, COO = orphans(ED), orphans(CO)
print("  ED flags:", len(EDO))
for f in EDO: print("   ED ", f)
print("  CORE flags:", len(COO))
for f in COO: print("   CO ", f)
edkeys = {(p, round(y, 2), t) for p, y, k, t in EDO}
cokeys = {(p, round(y, 2), t) for p, y, k, t in COO}
print("  ED flags NOT in CORE (page/y/text):", [f for f in EDO if (f[0], round(f[1], 2), f[3]) not in cokeys])
print("  ED line-start-punct flags:", [f for f in EDO if f[2] == "LINESTART"])
# safety net: every text element starting with punct, any block position
print("  safety-net: ALL ED text elements starting with punct:")
for pn in PAGES:
    els, _ = texts(ED / f"{pn}.svg")
    for e in els:
        s = e["s"].strip()
        if s and s[0] in "!?":
            print(f"    {pn} y={e['y']} x={e['x']} :: {s[:60]!r}")

print("===== G. P8 calibers (max baseline / ink bottom) =====")
for label, d in [("ED", ED), ("CORE", CO)]:
    els, _ = texts(d / "p8-exercices.svg")
    batt = [e for e in els if 194 <= e["y"] < 1526]
    ans = [e for e in els if 1838 <= e["y"] < 2580]
    for name, grp in [("battery", batt), ("answers", ans)]:
        mb = max(e["y"] for e in grp)
        mi = max(ink_box(e["s"], e["fam"], e["size"], e["bold"], e["x"], e["y"], e["anchor"])[3] for e in grp)
        print(f"  {label} {name}: n={len(grp)} max_baseline={mb:.2f} max_ink_bottom={mi:.2f} gap_to_2580={2580-mi:.2f}")
        worst = max(grp, key=lambda e: ink_box(e["s"], e["fam"], e["size"], e["bold"], e["x"], e["y"], e["anchor"])[3])
        print(f"      worst-ink node y={worst['y']} x={worst['x']} :: {worst['s'][:70]!r}")

print("===== H. P7 reader box + preview margins, P1 gloss rightmost =====")
for label, d in [("ED", ED)]:
    els, raw = texts(d / "p7-langue.svg")
    rects = [(float(a), float(b), float(a)+float(c), float(b)+float(d)) for a, b, c, d in RECT.findall(raw)]
    # reader texts: find max ink bottom among texts with y in reader region 1900-2260
    reg = [e for e in els if 1900 <= e["y"] <= 2260]
    if reg:
        mi = max(ink_box(e["s"], e["fam"], e["size"], e["bold"], e["x"], e["y"], e["anchor"])[3] for e in reg)
        print(f"  P7 reader-region max ink bottom={mi:.2f} (box bottom 2258 -> margin {2258-mi:.2f})")
    prev = [e for e in els if e["y"] >= 2400]
    if prev:
        mi = max(ink_box(e["s"], e["fam"], e["size"], e["bold"], e["x"], e["y"], e["anchor"])[3] for e in prev)
        print(f"  P7 preview-region max ink bottom={mi:.2f} (bar bottom 2540 -> margin {2540-mi:.2f})")
    els1, _ = texts(d / "p1-une.svg")
    gloss = [e for e in els1 if e["s"].strip().startswith("Uitleg — ")]
    print(f"  P1 gloss-prefix lines: {len(gloss)}")
    for e in gloss:
        ib = ink_box(e["s"], e["fam"], e["size"], e["bold"], e["x"], e["y"], e["anchor"])
        print(f"    y={e['y']} ink_right={ib[2]:.2f} (box right 961) margin={961-ib[2]:.2f} :: {e['s'][:60]!r}")

print("===== I. P6 chart-label baseline-anchored coverage =====")
for label, d in [("ED", ED), ("CORE", CO)]:
    els, raw = texts(d / "p6-politique.svg")
    rects = [(float(a), float(b), float(a)+float(c), float(b)+float(d)) for a, b, c, d in RECT.findall(raw)]
    # chart texts: texts inside chart box region (x 65..961, y 200..1300 approx, excluding heads) — use same heuristic as builder: texts whose ink overlaps a later rect
    # simpler: report all texts in y 300..1250 with their max overlap vs later-drawn rects
    worst = 0.0; nchart = 0
    items = list(enumerate(els))
    # order in file = draw order; rects order unknown vs texts — approximate with all rects drawn before? Use occlusion audit COVER logic via ink overlap with rects that appear AFTER the text in raw order
    rawpos = []
    for m in ATTR.finditer(raw):
        rawpos.append(m.start())
    # map element index to raw order already (finditer order)
    for i, e in enumerate(els):
        if not (300 <= e["y"] <= 1250): continue
        ib = ink_box(e["s"], e["fam"], e["size"], e["bold"], e["x"], e["y"], e["anchor"])
        if ib is None: continue
        # rects after this text in file order
        after = [r for (m, r) in zip(RECT.finditer(raw), [(float(a), float(b), float(a)+float(c), float(b)+float(d)) for a, b, c, d in RECT.findall(raw)]) if m.start() > rawpos[i]]
        cov = 0.0
        for r in after:
            ix = max(0, min(ib[2], r[2]) - max(ib[0], r[0])); iy = max(0, min(ib[3], r[3]) - max(ib[1], r[1]))
            area = (ib[2]-ib[0]) * (ib[3]-ib[1])
            if area: cov = max(cov, ix*iy/area)
        nchart += 1; worst = max(worst, cov)
    print(f"  {label}: chart-region texts={nchart} max later-rect coverage={worst*100:.1f}% (gate <30%)")

print("===== J. reader corner + furniture =====")
p7t = EDJ["p7-langue"]
for s in ["Exemple de la rédaction (ce texte n'est pas une lettre de lecteur)",
          "Stuur je brief én je beste pagina-8-tekst in voor VOL.4!",
          "geen echte brieven en geen beste VOL.2-pagina-8-tekst binnen",
          "beide volgen in VOL.4",
          "Note de la rédaction : aucun texte du VOL.2"]:
    print(f"  P7 {'FOUND' if s in p7t else 'MISSING'}: {s}")
print("  P7 preview line contains 'en jullie brieven!':", "en jullie brieven!" in p7t)
for pn in PAGES:
    els, _ = texts(ED / f"{pn}.svg")
    foots = [e["s"] for e in els if e["y"] == 2624.0]
    print(f"  footer {pn}: {foots}")
els1, _ = texts(ED / "p1-une.svg")
badge = [e for e in els1 if e["y"] == 574.0]
print("  P1 badge:", [(e["x"], e["y"], e["size"], e["bold"], e["anchor"], e["s"]) for e in badge])
els1w, _ = texts(W43 / "p1-une.svg")
badgew = [e for e in els1w if e["y"] == 574.0]
print("  W43 P1 badge:", [(e["x"], e["y"], e["size"], e["bold"], e["anchor"], e["s"]) for e in badgew])
print("  badge byte-equal ED==W43:", [e["s"] for e in badge] == [e["s"] for e in badgew])
els8, _ = texts(ED / "p8-exercices.svg")
seps = [e["s"] for e in els8 if e["s"].startswith("— PAGINA")]
print("  P8 separators:", seps)
keys_head = [e["s"] for e in els8 if "RÉPONSES" in e["s"]]
print("  P8 keys head:", keys_head)
els8w, _ = texts(W43 / "p8-exercices.svg")
print("  W43 keys head:", [e["s"] for e in els8w if "RÉPONSES" in e["s"]])
print("  W43 separators:", [e["s"] for e in els8w if e["s"].startswith("— PAGINA")])

print("===== K. images double-hash + placement + credit =====")
IMG = re.compile(r'<image[^>]*x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*href="data:image/jpeg;base64,([^"]+)"')
for label, d in [("ED", ED), ("CORE", CO)]:
    for pn, expect in [("p1-une", None), ("p2-vie", None), ("p3-culture", None)]:
        raw = (d / f"{pn}.svg").read_text(encoding="utf-8")
        for m in IMG.finditer(raw):
            b64 = m.group(5); dec = base64.b64decode(b64)
            print(f"  {label} {pn} place=({m.group(1)},{m.group(2)},{m.group(3)}x{m.group(4)}) b64sha16={hashlib.sha256(b64.encode()).hexdigest()[:16]} decsha16={hashlib.sha256(dec).hexdigest()[:16]} decbytes={len(dec)}")
for s in ["Eugène Atget (1857-1927), photographie, domaine public",
          "Utagawa Hiroshige (1797-1858), estampe, domaine public · LACMA",
          "Planche botanique, Flora de Filipinas (Blanco), XIXe siècle, domaine public"]:
    pg = "p1-une" if "Atget" in s else ("p2-vie" if "Hiroshige" in s else "p3-culture")
    els, _ = texts(ED / f"{pg}.svg")
    hit = [e for e in els if s in e["s"]]
    print(f"  credit {pg}: {'FOUND y=' + str([e['y'] for e in hit]) if hit else 'MISSING'} :: {s[:60]}")

print("===== L. ABSTRACT + forbidden term =====")
ab = (G / "files/weekly-report-w45-fr-nl/ABSTRACT.txt").read_text(encoding="utf-8")
print(f"  ABSTRACT bytes={len(ab.encode())} lines={ab.count(chr(10))} ascii-quote={'\"' in ab} text={ab.strip()!r}")
for term in ["桥接"]:
    hits = []
    for pn in PAGES:
        els, _ = texts(ED / f"{pn}.svg")
        if any(term in e["s"] for e in els): hits.append(pn)
    print(f"  term {term!r} in ED SVG pages: {hits}")
    print(f"  term in ABSTRACT: {term in ab}")
    kit = (G / "files/weekly-report-w45-fr-nl/WEEKLY-KIT.md").read_text(encoding="utf-8")
    print(f"  term in KIT: {term in kit}")
    for f in ["bslib4.py", "content12.py", "content34.py", "content56.py", "content7.py", "content8.py", "svglib.py", "transform.py"]:
        src = (G / "hidden_files/weekly-report-w45-fr-nl-build" / f).read_text(encoding="utf-8")
        if term in src: print(f"  term in build {f}: YES")
    print("  (build-code scan done; silence above = 0 hits)")
print("  ABSTRACT keywords in-edition counts:")
for kw in ["Rolex Paris Masters", "Nanterre", "Peur sur le Parc", "Plailly", "Le Goût du Large", "Port-en-Bessin", "Pitchfork", "Assemblée"]:
    print(f"    {kw}: ED={EDALL.count(kw)} in-ABSTRACT={kw in ab}")
for ph in ["leer Frans door te lezen", "Franse grammatica", "woordenschat"]:
    print(f"    phrase {ph!r}: in-ABSTRACT={ph in ab}")
