# -*- coding: utf-8 -*-
"""Follow-up checks: badge attrs, P6 chart contents, P7 golden sentences, gloss calls,
P8 separators, readers-corner stack, short heads, ABSTRACT, card dims, KIT SHA table."""
import re, os, collections
from PIL import Image

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE = os.path.join(GOAL, "files/weekly-report-w45-ru-core/svg")
ED = os.path.join(GOAL, "files/weekly-report-w45-ru-it/svg")
W43 = os.path.join(GOAL, "files/weekly-report-ru-it/svg")

def elements(path):
    s = open(path, encoding="utf-8").read()
    out = []
    for m in re.finditer(r"<text\s+([^>]*)>(.*?)</text>", s, re.S):
        attrs, inner = m.group(1), re.sub(r"<[^>]+>", "", m.group(2)).strip()
        def a(n):
            mm = re.search(n + r'="([^"]*)"', attrs)
            return mm.group(1) if mm else None
        out.append({"x": a("x"), "y": a("y"), "size": a("font-size"), "weight": a("font-weight"),
                    "fill": a("fill"), "anchor": a("text-anchor"), "text": inner})
    return out

print("== BADGE ELEMENT (P1) ==")
for label, d in [("W43", W43), ("W45-ed", ED)]:
    for e in elements(f"{d}/p1-pervaya.svg"):
        if "TESTI IN RUSSO" in e["text"]:
            print(f"  {label}: {e}")
print("== TOP STRIP ==")
for label, d in [("W43", W43), ("W45-ed", ED)]:
    for e in elements(f"{d}/p1-pervaya.svg"):
        if "OGNI SETTIMANA" in e["text"]:
            print(f"  {label}: {e}")
print("== FOOTERS all pages ==")
for label, d in [("W43", W43), ("W45-ed", ED)]:
    foots = []
    for p in ["p1-pervaya", "p2-zhizn", "p3-kultura", "p4-sport", "p5-molodezh", "p6-razbor", "p7-yazyk", "p8-test"]:
        for e in elements(f"{d}/{p}.svg"):
            if e["y"] == "2624":
                foots.append((p, e["x"], e["text"]))
    for f in foots:
        print(f"  {label} {f}")

print("== P6 CHART (fixed groups) ==")
for label, d in [("core", CORE), ("ed", ED)]:
    els = elements(f"{d}/p6-razbor.svg")
    vals = [e for e in els if e["text"] in ("34%", "28%", "22%", "16%")]
    print(f"  {label} values: {[(e['x'], e['y'], e['text']) for e in vals]}")
    # bar labels: texts with y in bar rows 1612-1780 and x < 685
    labs = [e for e in els if e["y"] and 1600 <= float(e["y"]) <= 1790 and e["x"] and float(e["x"]) < 685]
    print(f"  {label} left labels: {[(e['x'], e['y'], e['text'][:60]) for e in labs]}")
    # draw order: position of bar rects vs value texts in file
    s = open(f"{d}/p6-razbor.svg", encoding="utf-8").read()
    barpos = [m.start() for m in re.finditer(r'<rect[^>]*x="685\.0"', s)]
    valpos = [m.start() for m in re.finditer(r">34%<", s)]
    print(f"  {label} bar rect file offsets {barpos[:2]} value-34% offset {valpos} (bars before values: {bool(barpos and valpos and max(barpos) < min(valpos))})")
    # any rect after value texts whose box covers value x range? occlusion already 0; list rects after first value
    rects = [(m.start(), m.group(0)) for m in re.finditer(r"<rect[^>]*>", s)]
    after = [r for r in rects if valpos and r[0] > min(valpos)]
    print(f"  {label} rects drawn after 34% text: {len(after)} -> {[r[1][:110] for r in after[:6]]}")

print("== P7 GOLDEN SENTENCES x2 ==")
# Golden quotes: Russian sentences on P7. Strategy: take core P7 elements that are long
# Cyrillic-only sentences (no Latin, no Chinese), count occurrences in page-joined text.
def joined(path):
    return " ".join(e["text"] for e in elements(path))
cj, ej = joined(f"{CORE}/p7-yazyk.svg"), joined(f"{ED}/p7-yazyk.svg")
cands = set()
for e in elements(f"{CORE}/p7-yazyk.svg"):
    t = e["text"].strip()
    if re.search(r"[\u0400-\u04FF]", t) and not re.search(r"[A-Za-z\u4e00-\u9fff]", t) and len(t) >= 25:
        cands.add(t)
print(f"  pure-Cyrillic long candidates in core P7: {len(cands)}")
for t in sorted(cands):
    print(f"    core x{cj.count(t)} ed x{ej.count(t)}: {t[:100]!r}")

print("== GLOSS CALLS (source) ==")
for label, bdir in [("core-build", os.path.join(GOAL, "hidden_files/weekly-report-w45-ru-build")),
                    ("ed-build", os.path.join(GOAL, "hidden_files/weekly-report-w45-ru-it-build"))]:
    print(f"  {label} dir exists: {os.path.isdir(bdir)}")
    if os.path.isdir(bdir):
        for f in ["content12.py", "content34.py", "content56.py"]:
            p = os.path.join(bdir, f)
            if not os.path.exists(p):
                print(f"    {f}: MISSING"); continue
            src = open(p, encoding="utf-8").read()
            calls = re.findall(r"gloss\((.*?)\)\s*$", src, re.M)
            # gloss calls may span lines; fallback: count 'gloss(' occurrences and split items on '·'
            n = src.count("gloss(")
            print(f"    {f}: gloss( occurrences={n}")
            # extract gloss blocks: gloss( ... ) with string args; print first 200 chars of each call region
            for m in re.finditer(r"gloss\(", src):
                seg = src[m.start():m.start()+600].replace("\n", " ")
                print(f"      ... {seg[:300]}")

print("== P8 SEPARATORS ==")
for label, d in [("W43", W43), ("core", CORE), ("ed", ED)]:
    seps = [e["text"] for e in elements(f"{d}/p8-test.svg") if "СТРАНИЦА" in e["text"] or "PAGINA" in e["text"]]
    print(f"  {label}: {seps}")
print("== P8 keys flow end (max y of numbered lines) ==")
for label, d in [("core", CORE), ("ed", ED)]:
    ys = [float(e["y"]) for e in elements(f"{d}/p8-test.svg") if re.match(r"\d+\.", e["text"]) and e["y"]]
    print(f"  {label}: max numbered-line y={max(ys)}")

print("== P7 READERS CORNER STACK (x>=1400, y 1200-1800) ==")
for label, d in [("core", CORE), ("ed", ED)]:
    print(f"  --- {label}")
    for e in elements(f"{d}/p7-yazyk.svg"):
        if e["x"] and float(e["x"]) >= 1400 and e["y"] and 1200 <= float(e["y"]) <= 1800:
            print(f"    x={e['x']} y={e['y']} size={e['size']}: {e['text'][:110]!r}")

print("== SHORT HEADS in ed vs W43 ==")
shorts = ["In cifre", "Sommario", "La parola", "Quiz lampo", "In breve", "Pro e contro", "Analisi", "Giovani", "E tu?"]
for sname in shorts:
    in_ed = any(sname in e["text"] for p in ["p1-pervaya", "p2-zhizn", "p3-kultura", "p4-sport", "p5-molodezh", "p6-razbor", "p7-yazyk", "p8-test"] for e in elements(f"{ED}/{p}.svg"))
    in_w43 = any(sname in e["text"] for p in ["p1-pervaya", "p2-zhizn", "p3-kultura", "p4-sport", "p5-molodezh", "p6-razbor", "p7-yazyk", "p8-test"] for e in elements(f"{W43}/{p}.svg"))
    print(f"  {sname!r}: ed={in_ed} w43={in_w43}")

print("== P8 138/139 wrap continuation ==")
for label, d in [("core", CORE), ("ed", ED)]:
    for e in elements(f"{d}/p8-test.svg"):
        if "Confronta pagina" in e["text"] or "对照第" in e["text"] or (e["text"].strip() in ("5",) and e["y"] and 2000 < float(e["y"])):
            print(f"  {label}: x={e['x']} y={e['y']}: {e['text']!r}")
    s = open(f"{d}/p8-test.svg", encoding="utf-8").read()
    idx = s.find("Confronta pagina")
    print(f"  {label} raw around 'Confronta pagina': {s[idx-200:idx+300]!r}" if idx >= 0 else f"  {label}: no 'Confronta pagina' raw")

print("== ABSTRACT ==")
ab = open(os.path.join(GOAL, "files/weekly-report-w45-ru-it/ABSTRACT.txt"), encoding="utf-8").read()
print(f"  repr: {ab!r}")
print(f"  lines={ab.strip().count(chr(10))+1 if ab.strip() else 0} has_ascii_dquote={'\"' in ab} len={len(ab.strip())}")

print("== CARDS (independent PIL) ==")
for p in ["p1-pervaya", "p2-zhizn", "p3-kultura", "p4-sport", "p5-molodezh", "p6-razbor", "p7-yazyk", "p8-test"]:
    im = Image.open(os.path.join(GOAL, f"files/weekly-report-w45-ru-it/cards/{p}.png"))
    print(f"  {p}: {im.size} mode={im.mode}")

print("== KIT SHA TABLE vs delivered ==")
import hashlib
kit = open(os.path.join(GOAL, "files/weekly-report-w45-ru-it/WEEKLY-KIT.md"), encoding="utf-8").read()
for p in ["p1-pervaya", "p2-zhizn", "p3-kultura", "p4-sport", "p5-molodezh", "p6-razbor", "p7-yazyk", "p8-test"]:
    h = hashlib.sha256(open(os.path.join(ED, f"{p}.svg"), "rb").read()).hexdigest()
    print(f"  {p}: delivered={h} in_KIT={h in kit}")
print("DONE2")
