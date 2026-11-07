# -*- coding: utf-8 -*-
"""Independent JA x RU W45 proof script (proof-owned, reads only)."""
import re, html, json, os
from collections import Counter
BASE = "/home/hatch/workspace/goals/lucernaread-social-media-operations"
ED = BASE + "/files/weekly-report-w45-ja-ru/svg"
CO = BASE + "/files/weekly-report-w45-ja-core/svg"
W43 = BASE + "/files/weekly-report-ja-ru/svg"
PAGES = ["p1-hyoushi", "p2-kurashi", "p3-bunka", "p4-supotsu",
         "p5-wakamono", "p6-fukayomi", "p7-kotoba", "p8-tesuto"]

def raw(p):
    return open(p, encoding="utf-8").read()

def texts(p):
    out = []
    for m in re.finditer(r'<text([^>]*)>(.*?)</text>', raw(p)):
        ad = dict(re.findall(r'([\w-]+)="([^"]*)"', m.group(1)))
        out.append({"x": float(ad["x"]), "y": float(ad["y"]),
                    "size": ad.get("font-size"), "bold": ad.get("font-weight"),
                    "fam": ad.get("font-family", ""), "anchor": ad.get("text-anchor", "start"),
                    "t": html.unescape(re.sub(r"<[^>]+>", "", m.group(2)))})
    return out

def rects(p):
    out = []
    for m in re.finditer(r'<rect([^>]*)/>', raw(p)):
        ad = dict(re.findall(r'([\w-]+)="([^"]*)"', m.group(1)))
        out.append(ad)
    return out

def lines(p):
    out = []
    for m in re.finditer(r'<line([^>]*)/>', raw(p)):
        ad = dict(re.findall(r'([\w-]+)="([^"]*)"', m.group(1)))
        out.append(ad)
    return out

def images(p):
    return re.findall(r"<image[^>]*>", raw(p))

print("== FURNITURE P1 rects/lines (y near masthead) ==")
for label, d in [("CORE", CO), ("RU", ED), ("W43", W43)]:
    p = os.path.join(d, "p1-hyoushi.svg")
    print(f"-- {label}")
    for r in rects(p):
        try:
            y = float(r.get("y", 0)); h = float(r.get("height", 0))
        except ValueError:
            continue
        if y < 460:
            print("   rect", r)
    for ln in lines(p):
        try:
            y1 = float(ln.get("y1", 0))
        except ValueError:
            continue
        if y1 < 460:
            print("   line", ln)
    # footer texts (last 3)
    ts = texts(p)
    print("   footer tail:", [(t["y"], t["t"]) for t in ts[-3:]])

print("\n== P1 badge rect fill: rect containing badge text baseline 356 ==")
for label, d in [("CORE", CO), ("RU", ED), ("W43", W43)]:
    p = os.path.join(d, "p1-hyoushi.svg")
    cands = []
    for r in rects(p):
        try:
            y = float(r.get("y", 0)); h = float(r.get("height", 0))
            x = float(r.get("x", 0)); w = float(r.get("width", 0))
        except ValueError:
            continue
        if y <= 356 <= y + h:
            cands.append(r)
    print(label, cands)

print("\n== PAGE TABS: core P7 'p.N' vs RU P7 '(Страница N)' ==")
for label, d in [("CORE", CO), ("RU", ED), ("W43", W43)]:
    ts = texts(os.path.join(d, "p7-kotoba.svg"))
    core_tabs = [t["t"] for t in ts if re.fullmatch(r"p\.\d", t["t"].strip())]
    ru_tabs = [t["t"] for t in ts if "Страница" in t["t"]]
    print(label, "p.N:", core_tabs, "| Страница:", ru_tabs)

print("\n== FOOTER page line all pages RU vs CORE vs W43 ==")
for pg in PAGES:
    def foot(d):
        ts = texts(os.path.join(d, pg + ".svg"))
        return [t["t"] for t in ts if " из 8" in t["t"] or " / 8" in t["t"] or "页" in t["t"] and "8" in t["t"]]
    print(pg, "RU:", foot(ED), "CORE:", foot(CO), "W43:", foot(W43))

print("\n== GLOSS prefix + P8 separators ==")
for label, d in [("CORE", CO), ("RU", ED)]:
    gp = Counter()
    for pg in PAGES:
        for t in texts(os.path.join(d, pg + ".svg")):
            if "Пояснение" in t["t"] or "解説" in t["t"] or "讲解" in t["t"]:
                gp[t["t"][:24]] += 1
    print(label, "gloss-prefix-ish:", dict(gp))
    seps = [t["t"] for t in texts(os.path.join(d, "p8-tesuto.svg")) if t["t"].strip().startswith("—") and t["t"].strip().endswith("—")]
    print(label, "P8 seps:", seps)

print("\n== '全部' vs 'ВСЕ' across W45 JA family ==")
import glob
for d in sorted(glob.glob(BASE + "/files/weekly-report-w45-ja-*")):
    if d.endswith("-build") or "core" in d:
        continue
    hits = []
    for pg in PAGES:
        s = raw(os.path.join(d, pg + ".svg"))
        if "全部" in s:
            hits.append((pg, s.count("全部")))
        if "ВСЕ" in s:
            hits.append((pg, "ВСЕ:" + str(s.count("ВСЕ"))))
    if hits:
        print(os.path.basename(d), hits)
print("core 全部:", [(pg, raw(os.path.join(CO, pg + ".svg")).count("全部")) for pg in PAGES])
print("RU 全部/ВСЕ:", [(pg, raw(os.path.join(ED, pg + ".svg")).count("全部"), raw(os.path.join(ED, pg + ".svg")).count("ВСЕ")) for pg in PAGES])

print("\n== IMAGES per page core vs RU identical ==")
for pg in PAGES:
    ie, ic = images(os.path.join(ED, pg + ".svg")), images(os.path.join(CO, pg + ".svg"))
    print(pg, "ed", len(ie), "core", len(ic), "identical", ie == ic)
    for im in ie:
        print("   ", im[:220])

print("\n== IMAGE CREDIT lines ==")
for label, d in [("CORE", CO), ("RU", ED)]:
    print("--", label)
    for pg in PAGES:
        for t in texts(os.path.join(d, pg + ".svg")):
            if any(k in t["t"] for k in ["Poliphilo", "CC0", "Public domain", "パブリックドメイン", "出典", "Credit", "Hiroshige", "広重", "Wikimedia"]):
                print("  ", pg, round(t["y"], 1), repr(t["t"][:160]))
