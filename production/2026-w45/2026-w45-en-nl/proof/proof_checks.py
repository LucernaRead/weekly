#!/usr/bin/env python3
"""Independent ENxNL W45 proof checks. Reads only; writes only into proof dir."""
import os, re, html, json
from collections import Counter
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = os.path.join(BASE, "files/weekly-report-w45-en-nl/svg")
CO = os.path.join(BASE, "files/weekly-report-w45-en-core/svg")
W43 = os.path.join(BASE, "files/weekly-report-en-nl/svg")
OUT = os.path.dirname(os.path.abspath(__file__))
log = open(os.path.join(OUT, "proof_checks.log"), "w", encoding="utf-8")
def p(*a):
    s = " ".join(str(x) for x in a); print(s); log.write(s + "\n")
def texts(path):
    s = open(path, encoding="utf-8").read()
    out = []
    for m in re.finditer(r"<text([^>]*)>(.*?)</text>", s, re.S):
        a = dict(re.findall(r'([\w-]+)="([^"]*)"', m.group(1)))
        out.append({"x": a.get("x"), "y": a.get("y"), "size": a.get("font-size"), "fam": a.get("font-family"),
                    "bold": a.get("font-weight"), "anchor": a.get("text-anchor", "start"),
                    "text": html.unescape(re.sub(r"<[^>]+>", "", m.group(2)))})
    return out
def rects(path):
    s = open(path, encoding="utf-8").read()
    out = []
    for m in re.finditer(r"<rect([^>]*)/>", s):
        a = dict(re.findall(r'([\w-]+)="([^"]*)"', m.group(1)))
        try: out.append({"x": float(a.get("x",0)), "y": float(a.get("y",0)), "w": float(a.get("width",0)), "h": float(a.get("height",0)), "fill": a.get("fill",""), "stroke": a.get("stroke","")})
        except ValueError: pass
    return out
def joined(d, fn): return " ".join(t["text"] for t in texts(os.path.join(d, fn)))
def filemap(d):
    return {fn: texts(os.path.join(d, fn)) for fn in sorted(os.listdir(d)) if fn.endswith(".svg")}
EDT, COT, W43T = filemap(ED), filemap(CO), filemap(W43)
def bypage(dmap, pg):
    for fn, ts in dmap.items():
        if re.match(rf"p{pg}-", fn): return ts
    raise KeyError(pg)

# --- 5. gloss rendered: gloss boxes are #f1ead6 rects; texts inside their y-range, joined, split on middle dot ---
p("== GLOSS rendered (box-anchored join, split on ·) ==")
for label, dmap, d, prefix in [("CORE", COT, CO, "讲解｜"), ("ED", EDT, ED, "Uitleg — ")]:
    tot = 0; dist = {}
    for pg in (2,3,4,5,6):
        fn = [f for f in dmap if re.match(rf"p{pg}-", f)][0]
        rs = [r for r in rects(os.path.join(d, fn)) if r["fill"] == "#f1ead6"]
        ts = dmap[fn]
        items = []
        for r in rs:
            inside = [t for t in ts if r["y"] < float(t["y"]) < r["y"] + r["h"]]
            s = " ".join(t["text"] for t in inside)
            if prefix in s:
                body = s.split(prefix, 1)[1]
                items += [x.strip() for x in body.split("·") if x.strip()]
        dist[pg] = len(items); tot += len(items)
        p(f"  {label} P{pg}: gloss boxes={len(rs)} items={len(items)} :: {items}")
    p(f"  {label} TOTAL={tot} dist={dist}")
# gloss source strings (build files, independent of rendered join)
p("== GLOSS source strings (content files, split on ·) ==")
import glob as _g
for label, bdir in [("CORE", os.path.join(BASE, "hidden_files/weekly-report-w45-en-build")), ("ED", os.path.join(BASE, "hidden_files/weekly-report-w45-en-nl-build"))]:
    tot = 0
    for f in sorted(_g.glob(os.path.join(bdir, "content*.py"))):
        s = open(f, encoding="utf-8").read()
        for m in re.finditer(r"\.gloss\(\"([^\"]+)\"\)", s):
            body = m.group(1)
            if label == "CORE": body = body.split("讲解｜",1)[-1]
            items = [x.strip() for x in body.split("·") if x.strip()]
            tot += len(items); p(f"  {label} {os.path.basename(f)}: {len(items)} :: {items}")
    p(f"  {label} source TOTAL={tot}")

# --- 6. P7 ---
p("\n== P7 ==")
co7 = " ".join(t["text"] for t in COT["p7-langue.svg"]); ed7 = " ".join(t["text"] for t in EDT["p7-langue.svg"])
p("  P7 headings ED:")
for t in EDT["p7-langue.svg"]:
    if any(k in t["text"] for k in ["LEVEL ", "TOOLBOX", "PHRASES OF THE WEEK", "ERROR CLINIC", "READERS' CORNER", "NEXT WEEK", "LANGUAGE IN HAND"]):
        p(f"    y={t['y']} {t['text']!r}")
p("  P7 headings CORE:")
for t in COT["p7-langue.svg"]:
    if any(k in t["text"] for k in ["LEVEL ", "TOOLBOX", "PHRASES OF THE WEEK", "ERROR CLINIC", "READERS' CORNER", "NEXT WEEK", "LANGUAGE IN HAND"]):
        p(f"    y={t['y']} {t['text']!r}")
# golden sentences: use core P7 phrases section? Extract from core full-issue: golden sentences are the 8 listed in KIT; verify verbatim presence in ED P7 + levels/tags + whole-issue counts
gold = [
    ("Tuesday, November 3", "p1"), ("The hour from 1 to 2", "p2"), ("Which film would you choose ?", "p3"),
    ("Two games, two continents", "p4"), ("The results will still be there", "p5"), ("Patience is part of the system", "p6"),
    ("Not every place changes.", "p2"), ("One Sunday is not enough", "p4"),
]
# whole-issue counts: count occurrences of each full golden sentence fragment across all pages (core vs ed), using joined page text with wrapping normalised (join texts with space, collapse spaces)
def norm_join(dmap):
    out = {}
    for fn, ts in dmap.items():
        out[fn] = re.sub(r"\s+", " ", " ".join(t["text"] for t in ts))
    return out
co_all = norm_join(COT); ed_all = norm_join(EDT)
full_gold = [
    "Tuesday, November 3, is Election Day in the United States.",
    "The hour from 1 to 2 happened twice.",
    "Which film would you choose ?",
    "Two games, two continents, one league",
    "The results will still be there in the morning.",
    "Patience is part of the system, not a failure of it.",
    "Not every place changes.",
    "One Sunday is not enough",
]
for g in full_gold:
    cc = sum(v.count(g) for v in co_all.values()); ec = sum(v.count(g) for v in ed_all.values())
    p(f"  GOLD whole-issue core={cc} ed={ec} :: {g!r}")
# P7 golden block: print ED P7 texts in phrases region (y between? find PHRASES header y then list following texts)
p("  ED P7 phrases-region texts:")
ph = [t for t in EDT["p7-langue.svg"] if "PHRASES OF THE WEEK" in t["text"]]
if ph: p(f"    header y={ph[0]['y']}")
for t in EDT["p7-langue.svg"]:
    if ph and float(t["y"]) > float(ph[0]["y"]) and float(t["y"]) < 1900:
        p(f"    y={t['y']} {t['text']!r}")
p("  CORE P7 phrases-region texts:")
phc = [t for t in COT["p7-langue.svg"] if "PHRASES OF THE WEEK" in t["text"]]
for t in COT["p7-langue.svg"]:
    if phc and float(t["y"]) > float(phc[0]["y"]) and float(t["y"]) < 1900:
        p(f"    y={t['y']} {t['text']!r}")
# P7 level tags in phrases block: texts like "page 1" + level? print all texts containing "page " in P7
p("  ED P7 'page' tag texts:")
for t in EDT["p7-langue.svg"]:
    if "page " in t["text"] or "(page" in t["text"]: p(f"    y={t['y']} {t['text']!r}")
p("  CORE P7 'page' tag texts:")
for t in COT["p7-langue.svg"]:
    if "page " in t["text"] or "(page" in t["text"]: p(f"    y={t['y']} {t['text']!r}")

# --- 7. readers corner ---
p("\n== READERS CORNER (P7) ==")
for label, dmap in [("CORE", COT), ("ED", EDT)]:
    ts = dmap["p7-langue.svg"]
    hdr = [t for t in ts if "READERS' CORNER" in t["text"]]
    p(f"  {label} header: {[t['text'] for t in hdr]}")
    if hdr:
        hy = float(hdr[0]["y"])
        # next-week header y as end bound
        nw = [t for t in ts if "NEXT WEEK" in t["text"]]
        end = float(nw[0]["y"]) if nw else 2700
        for t in ts:
            if hy < float(t["y"]) < end: p(f"    y={t['y']} {t['text']!r}")

# --- 8. furniture vs W43 ---
p("\n== FURNITURE W43 vs W45-NL (verbatim) ==")
checks = ["TEKSTEN IN HET ENGELS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS",
          "WEEKLY IN ENGLISH · ELKE WEEK EEN NUMMER · HET ENGELS DAT AMERIKA LEEST",
          "The Lucerna · ENGELS WEEKBLAD VOL.2 · TEKSTEN IN HET ENGELS · UITLEG IN HET NEDERLANDS",
          "Uitleg — ", "— Pagina 1 —", "— Pagina 8 —"]
for c in checks:
    inw43 = any(c in t["text"] for ts in W43T.values() for t in ts)
    ined = any(c in t["text"] for ts in EDT.values() for t in ts)
    p(f"  {c!r}: W43={inw43} ED={ined}")
p("  ED footers per page:")
for pg in range(1,9):
    ts = bypage(EDT, pg)
    foots = [t["text"] for t in ts if "Pagina " in t["text"] and "van 8" in t["text"]]
    p(f"    P{pg}: {foots}")
p("  ED band suffixes:")
for pg in range(1,9):
    ts = bypage(EDT, pg)
    for t in ts:
        if "· Leven" in t["text"] or "· Cultuur" in t["text"] or "· Sport" in t["text"] or "· Jeugd" in t["text"] or "· Verdieping" in t["text"] or "· Taal in handen" in t["text"] or "· Oefeningen en antwoorden" in t["text"]:
            p(f"    P{pg}: {t['text']!r}")
p("  ED P7 section Dutch suffixes:")
for t in EDT["p7-langue.svg"]:
    if "· Basis" in t["text"] or "· Verder" in t["text"] or "· Uitdaging" in t["text"] or "· Gereedschap" in t["text"] or "· Zinnen van de week" in t["text"] or "· Fouten" in t["text"] or "· Lezershoek" in t["text"] or "VOL.3 Volgende week" in t["text"]:
        p(f"    {t['text']!r}")
p("  ED exercise type names present:")
for typ in ["Zinnen aanvullen","Meerkeuze","Zinnen omvormen","Woorden combineren","Grafiek lezen","Gatentekst","Leestekst","Vertalen","Dialoog aanvullen","Fouten verbeteren","Meedoen","Schrijven"]:
    found = any(typ in t["text"] for ts in EDT.values() for t in ts)
    p(f"    {typ}: {found}")
p("  W43 type names (for comparison, W43 file):")
for typ in ["Zinnen aanvullen","Meerkeuze","Zinnen omvormen","Woorden combineren","Grafiek lezen","Gatentekst","Leestekst","Vertalen","Dialoog aanvullen","Fouten verbeteren","Meedoen","Schrijven"]:
    found = any(typ in t["text"] for ts in W43T.values() for t in ts)
    p(f"    {typ}: {found}")
p("  ED P8 font sizes for keys flow (para sizes in svg): check 13.5 present, 15.5 absent in P8 keys area")
s8 = open(os.path.join(ED, "p8-exercices.svg"), encoding="utf-8").read()
p(f"    P8 font-size 13.5 count={s8.count('font-size=\"13.5\"')} 15.5 count={s8.count('font-size=\"15.5\"')}")
s8w = open(os.path.join(W43, "p8-exercices.svg"), encoding="utf-8").read()
p(f"    W43 P8 font-size 13.5 count={s8w.count('font-size=\"13.5\"')} 15.5 count={s8w.count('font-size=\"15.5\"')}")
p("  ED P8 battery gaps: content8 gap values (from build file, informational)")
c8 = open(os.path.join(BASE, "hidden_files/weekly-report-w45-en-nl-build/content8.py"), encoding="utf-8").read()
p(f"    gap=8 occurrences in content8: {c8.count('gap=8')} ; gap=11 occurrences: {c8.count('gap=11')}")

# --- 9. images / credits / model essay ---
p("\n== IMAGES ==")
for label, d in [("CORE", CO), ("ED", ED)]:
    for pg in range(1,9):
        fn = [f for f in os.listdir(d) if re.match(rf"p{pg}-", f)][0]
        s = open(os.path.join(d, fn), encoding="utf-8").read()
        imgs = re.findall(r"<image[^>]*>", s)
        p(f"  {label} P{pg} images={len(imgs)}")
        for im in imgs: p(f"      {im[:220]}")
for label, d in [("CORE", CO), ("ED", ED)]:
    s = "".join(open(os.path.join(d, f), encoding="utf-8").read() for f in sorted(os.listdir(d)) if f.endswith(".svg"))
    # credit-like texts: search for Wikimedia/Commons/artist/photo credits in texts
    ts_all = []
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".svg"): ts_all += [t["text"] for t in texts(os.path.join(d, fn))]
    cred = [t for t in ts_all if any(k in t for k in ["Wikimedia", "Commons", "Photo", "photo", "©", "Credit", "Manet", "1910", "1912"])]
    p(f"  {label} credit-ish texts: {cred[:20]}")
p("  build assets CREDITS.md:")
print(open(os.path.join(BASE, "hidden_files/weekly-report-w45-en-nl-build/assets/CREDITS.md"), encoding="utf-8").read())
p("  build assets meta.json:")
print(open(os.path.join(BASE, "hidden_files/weekly-report-w45-en-nl-build/assets/meta.json"), encoding="utf-8").read())
p("\n== MODEL ESSAY (P8 writing box) ==")
for label, dmap in [("CORE", COT), ("ED", EDT)]:
    ts = dmap["p8-exercices.svg"]
    # model box: after MODEL header
    mh = [t for t in ts if "MODEL" in t["text"]]
    p(f"  {label} MODEL header: {[t['text'] for t in mh]}")
    if mh:
        hy = float(mh[0]["y"])
        # print following ~12 texts
        idx = ts.index(mh[0])
        for t in ts[idx:idx+14]: p(f"    y={t['y']} {t['text']!r}")
log.close()
print("DONE proof_checks")
