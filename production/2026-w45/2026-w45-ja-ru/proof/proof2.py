# -*- coding: utf-8 -*-
"""Independent JA x RU W45 proof script #2: counts, P7, gloss, essay, P8."""
import re, html, json, os, ast
from collections import Counter
BASE = "/home/hatch/workspace/goals/lucernaread-social-media-operations"
ED = BASE + "/files/weekly-report-w45-ja-ru/svg"
CO = BASE + "/files/weekly-report-w45-ja-core/svg"
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

print("== EXERCISE NUMBERS per page (numbered stems, body only) ==")
# Body numbered items: texts matching ^N. at line start, excluding P8 answer flow (P8 handled separately)
# and excluding footer/teaser lines. We count distinct numbers per page in core vs RU.
for label, d in [("CORE", CO), ("RU", ED)]:
    dist = {}
    for pg in PAGES[:-1]:
        nums = set()
        for t in texts(os.path.join(d, pg + ".svg")):
            m = re.match(r"^(\d{1,3})\.\s?", t["t"])
            if m:
                nums.add(int(m.group(1)))
        dist[pg] = sorted(nums)
    print(label, {k: (len(v), v[0], v[-1]) for k, v in dist.items()})
    print(label, "total distinct body numbers:", sum(len(v) for v in dist.values()))

print("\n== LEVELS: level tags per exercise in build code (core content files) ==")
# Look for level markers in core build: search for A2/B1/B2 tokens near exercise defs
import glob
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    src = raw(os.path.join(BASE, "hidden_files/weekly-report-w45-ja-build", f))
    print(f, "A2:", src.count('"A2"') + src.count("'A2'"), "B1:", src.count('"B1"'),
          "B2:", src.count('"B2"'))
print("SVG level tokens core P1-P8:")
for label, d in [("CORE", CO), ("RU", ED)]:
    c = Counter()
    for pg in PAGES:
        for t in texts(os.path.join(d, pg + ".svg")):
            for lv in ("A2", "B1", "B2"):
                if t["t"].strip() == lv:
                    c[lv] += 1
    print(label, dict(c))

print("\n== GOLDEN PHRASES 2x (whitespace-stripped concat, core + RU) ==")
phrases = ["文化の日は、11月3日（火よう日）です。",
           "ゆっくり、ゆるく整える日本の11月です。",
           "『ゆる』は、無理をしない、ゆっくり、という意味です。",
           "鍋の材料が1か月早く並び始めました。",
           "伝統工芸と紅葉と光を、いっしょに楽しむことができます。",
           "ソフトバンクが2連勝でスタートしました。",
           "ルールを守って、楽しいハロウィンにしましょう。",
           "紅葉を見に行く人は、北から南へ、見頃を追いかけることができます。"]
for label, d in [("CORE", CO), ("RU", ED)]:
    concat = "".join(re.sub(r"\s+", "", t["t"]) for pg in PAGES for t in texts(os.path.join(d, pg + ".svg")))
    print(label, [concat.count(re.sub(r"\s+", "", ph)) for ph in phrases])

print("\n== GLOSS rendered: texts starting with gloss prefix, split on '·' ==")
for label, d in [("CORE", CO), ("RU", ED)]:
    # Core gloss: lines containing ' · ' inside word-box gloss rows? Identify via build: gloss() rendered
    # as a single text line per call? Instead count from SVG: find texts that match gloss pattern:
    # In RU they start 'Пояснение — '. In core, find the corresponding lines by position:
    # gloss lines are the short lines right after a word-box paragraph. Use build-code gloss() calls
    # as the call inventory AND rendered lines containing the headwords.
    print("--", label)
    tot = 0
    for pg in PAGES[:6]:
        gl = [t for t in texts(os.path.join(d, pg + ".svg")) if t["t"].startswith("Пояснение")]
        n = sum(len(t["t"].split("·")) - 0 for t in gl)  # placeholder, refined below
        print("  ", pg, "prefix lines:", len(gl), [t["t"][:80] for t in gl])
print("NOTE: core gloss prefix differs; rendered split measured in proof2b via gloss-line matching.")

print("\n== ESSAY: P8 model essay reconstruction ==")
for label, d in [("CORE", CO), ("RU", ED)]:
    ts = texts(os.path.join(d, "p8-tesuto.svg"))
    # essay zone H: find texts containing 私の11月の週末
    idx = [i for i, t in enumerate(ts) if "私の11月の週末" in t["t"]]
    print(label, "essay start idx:", idx)
    if idx:
        i = idx[0]
        seg = "".join(t["t"] for t in ts[i:i + 14])
        print("  seg:", repr(seg[:400]))
        # char count: Japanese chars excluding punctuation? Report multiple counts
        s = seg
        print("  raw len:", len(s), "no-whitespace len:", len(re.sub(r"\s+", "", s)))

print("\n== P7 definition freeze: Japanese sentence multiset core vs RU ==")
co7 = Counter(t["t"] for t in texts(os.path.join(CO, "p7-kotoba.svg")))
ed7 = Counter(t["t"] for t in texts(os.path.join(ED, "p7-kotoba.svg")))
print("core-only P7 strings:")
for s, n in sorted((co7 - ed7).items()):
    print("  -", repr(s[:120]))
print("edition-only P7 strings:")
for s, n in sorted((ed7 - co7).items()):
    print("  +", repr(s[:120]))

print("\n== P8 FLOW END + P7 PREVIEW END (excluding footer lines y=2624) ==")
for label, d in [("CORE", CO), ("RU", ED)]:
    ts8 = [t for t in texts(os.path.join(d, "p8-tesuto.svg")) if t["y"] != 2624.0]
    ans = [t for t in ts8 if t["y"] > 1328]
    print(label, "P8 max answer y:", max(t["y"] for t in ans), "last:", [(t["y"], t["t"][:60]) for t in ans[-3:]])
    ts7 = [t for t in texts(os.path.join(d, "p7-kotoba.svg")) if t["y"] != 2624.0]
    print(label, "P7 max non-footer y:", max(t["y"] for t in ts7), "last:", [(t["y"], t["t"][:60]) for t in ts7[-3:]])
    # P7 preview section: texts after '来週' header
    pv = []
    started = False
    for t in ts7:
        if t["t"].startswith("来週"):
            started = True
        if started:
            pv.append(t)
    print(label, "P7 preview texts:", [(t["y"], t["t"][:60]) for t in pv])
