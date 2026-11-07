# -*- coding: utf-8 -*-
"""Independent RU×IT W45 proof audit (read-only on shipped files)."""
import re, json, hashlib, collections, glob, os, sys

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE = os.path.join(GOAL, "files/weekly-report-w45-ru-core/svg")
ED = os.path.join(GOAL, "files/weekly-report-w45-ru-it/svg")
W43 = os.path.join(GOAL, "files/weekly-report-ru-it/svg")
PAGES = ["p1-pervaya", "p2-zhizn", "p3-kultura", "p4-sport", "p5-molodezh", "p6-razbor", "p7-yazyk", "p8-test"]
OUT = os.path.join(GOAL, "hidden_files/w45/ru-it-proof")
CYR = re.compile(r"[\u0400-\u04FF]+")
CJK = re.compile(r"[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af]")

def texts(path):
    s = open(path, encoding="utf-8").read()
    # text elements content (strip tags inside)
    raw = re.findall(r"<text[^>]*>(.*?)</text>", s, re.S)
    return [re.sub(r"<[^>]+>", "", t) for t in raw]

def cyr_multiset(path):
    c = collections.Counter()
    for t in texts(path):
        for tok in CYR.findall(t):
            c[tok] += 1
    return c

report = {}
print("== CYRILLIC MULTISET ==")
for p in PAGES:
    a, b = cyr_multiset(f"{CORE}/{p}.svg"), cyr_multiset(f"{ED}/{p}.svg")
    diff = {k: (a.get(k, 0), b.get(k, 0)) for k in set(a) | set(b) if a.get(k, 0) != b.get(k, 0)}
    print(f"{p}: core_tokens={sum(a.values())} ed_tokens={sum(b.values())} ndiff_keys={len(diff)}")
    if diff:
        for k, v in sorted(diff.items()):
            print(f"   {k}: core {v[0]} -> ed {v[1]}")
    report[p + "_cyr"] = {"core": sum(a.values()), "ed": sum(b.values()), "diff": diff}

print("== CJK ==")
for p in PAGES:
    s = open(f"{ED}/{p}.svg", encoding="utf-8").read()
    print(f"{p}: CJK_chars={len(CJK.findall(s))}")
    report[p + "_cjk"] = len(CJK.findall(s))

print("== P8 DASH-PARSE ==")
def p8_lines(path):
    ts = texts(path)
    # P8 answer lines look like "N. key — note" ; collect lines matching ^\d+\.
    out = {}
    for t in ts:
        m = re.match(r"\s*(\d+)\.\s*(.*)", t)
        if m:
            out[int(m.group(1))] = m.group(2).strip()
    return out

core8, ed8 = p8_lines(f"{CORE}/p8-test.svg"), p8_lines(f"{ED}/p8-test.svg")
print(f"core lines={len(core8)} ed lines={len(ed8)} missing={sorted(set(core8)-set(ed8))} extra={sorted(set(ed8)-set(core8))}")
keydiff, notediff = [], []
for n in sorted(set(core8) & set(ed8)):
    ck = core8[n].split(" — ", 1)[0].strip()
    ek = ed8[n].split(" — ", 1)[0].strip()
    if ck != ek:
        keydiff.append(n)
        print(f"  KEYDIFF {n}: core={ck!r} ed={ek!r}")
    if core8[n] != ed8[n] and n not in keydiff:
        notediff.append(n)
print(f"dash-parse keydiff={keydiff} note_only_diffs={len(notediff)}")
for n in [83, 137, 138, 148]:
    print(f"  #{n} core full: {core8.get(n)!r}")
    print(f"  #{n} ed   full: {ed8.get(n)!r}")
    print(f"  #{n} core key-dash: {core8.get(n, '').split(' — ',1)[0]!r}  ed key-dash: {ed8.get(n, '').split(' — ',1)[0]!r}")
    # also paren-branch view: what p8.py sees
for n in [139, 140, 150]:
    print(f"  #{n} core: {core8.get(n)!r}")
    print(f"  #{n} ed:   {ed8.get(n)!r}")
# 150 model text word count: find section H model? count words of the model paragraph on P8
# model text lives in P8 as Russian paragraph; search for it via build? Instead: check KIT claim via P8 text blocks containing model - report raw
report["p8_dash"] = {"core": len(core8), "ed": len(ed8), "keydiff": keydiff, "note_only": len(notediff)}

print("== P7 GOLDEN SENTENCES ==")
# golden sentences: Russian quoted lines on P7; count occurrences of each distinct Russian sentence line in page-joined text
def page_text(path):
    return " ".join(texts(path))
for label, d in [("core", CORE), ("ed", ED)]:
    t = page_text(f"{d}/p7-yazyk.svg")
    print(f"  {label} P7 text len {len(t)}")
# extract Russian sentences: lines that are long Cyrillic strings; compare multiset of Cyrillic sentences between core/ed P7
def rus_sentences(path):
    c = collections.Counter()
    for t in texts(path):
        for s in re.findall(r"[\u0400-\u04FF][\u0400-\u04FF\s,—:;.!?\-«»\"]{20,}", t):
            c[s.strip()] += 1
    return c
# simpler: the 8 golden quotes - find text elements starting with « or containing long Russian quote; just compare full Cyrillic line multisets
def cyr_lines(path):
    c = collections.Counter()
    for t in texts(path):
        tt = t.strip()
        if CYR.search(tt) and len(tt) > 15:
            c[tt] += 1
    return c
a, b = cyr_lines(f"{CORE}/p7-yazyk.svg"), cyr_lines(f"{ED}/p7-yazyk.svg")
# golden sentences should be identical lines present 2x in both? print lines present in both with counts
print("  P7 Cyrillic lines differing core vs ed:")
for k in sorted(set(a) | set(b)):
    if a.get(k, 0) != b.get(k, 0):
        print(f"    {a.get(k,0)}->{b.get(k,0)}: {k[:120]!r}")
report["p7_cyr_lines_diff"] = {k: (a.get(k, 0), b.get(k, 0)) for k in set(a) | set(b) if a.get(k, 0) != b.get(k, 0)}

print("== IMAGE BLOBS ==")
def blobs(path):
    s = open(path, encoding="utf-8").read()
    return [hashlib.sha256(x.encode()).hexdigest()[:16] for x in re.findall(r"data:image/[^;]+;base64,([A-Za-z0-9+/=]+)", s)]
for p in PAGES:
    cb, eb = blobs(f"{CORE}/{p}.svg"), blobs(f"{ED}/{p}.svg")
    print(f"{p}: core blobs={cb} ed blobs={eb} equal={cb==eb}")
    report[p + "_blobs_equal"] = (cb == eb)

print("== P7 GEOMETRY ==")
def rects(path):
    s = open(path, encoding="utf-8").read()
    out = []
    for m in re.finditer(r"<rect[^>]*>", s):
        tag = m.group(0)
        def attr(n):
            mm = re.search(n + r'="([0-9.]+)"', tag)
            return float(mm.group(1)) if mm else None
        out.append((attr("x"), attr("y"), attr("width"), attr("height"), tag[:120]))
    return out
for label, d in [("core", CORE), ("ed", ED)]:
    rs = [r for r in rects(f"{d}/p7-yazyk.svg") if r[0] == 1451.0]
    print(f"  {label} x=1451 rects: {[(r[1], r[3], (r[1]+r[3]) if r[1] is not None and r[3] is not None else None) for r in rs]}")
    # disclosure: find text elements with baseline y near 1738
    s = open(f"{d}/p7-yazyk.svg", encoding="utf-8").read()
    for m in re.finditer(r'<text[^>]*y="([0-9.]+)"[^>]*>(.*?)</text>', s, re.S):
        y = float(m.group(1))
        if 1700 < y < 1780:
            print(f"    {label} text y={y}: {re.sub('<[^>]+>', '', m.group(2))[:110]!r}")
report["p7_geom"] = "see log"

print("== P6 CHART ==")
for label, d in [("core", CORE), ("ed", ED)]:
    s = open(f"{d}/p6-razbor.svg", encoding="utf-8").read()
    # texts with % values and bar labels
    for m in re.finditer(r'<text[^>]*x="([0-9.]+)"[^>]*y="([0-9.]+)"[^>]*>(.*?)</text>', s, re.S):
        t = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        if re.search(r"^\d+%?$", t) or t in ("34", "28", "22", "16", "34%", "28%", "22%", "16%"):
            print(f"  {label} chart text x={m.group(1)} y={m.group(2)}: {t!r}")
    # rects on P6: list bars (wide rects)
    for m in re.finditer(r'<rect[^>]*x="([0-9.]+)"[^>]*y="([0-9.]+)"[^>]*width="([0-9.]+)"[^>]*height="([0-9.]+)"[^>]*>', s):
        x, y, w, h = map(float, m.groups())
        if w > 200 and h < 60:
            print(f"  {label} bar rect x={x} y={y} w={w} h={h} end={x+w}")
    # check later rect covering chart texts: occlusion tool already covers; here list any rect drawn after chart texts - skip, rely on occlusion
    # labels: search known bar label words? print all P6 texts containing % or numbers near chart
    print(f"  {label} P6 texts with digits: {[t for t in texts(f'{d}/p6-razbor.svg') if re.search(chr(37), t)][:20]}")

print("== FURNITURE TRI-COMPARE (P1 badge, top strip, footers, gloss prefix, separators) ==")
def find_text(path, needle):
    return [(m.group(1), m.group(2), re.sub(r"<[^>]+>", "", m.group(3))[:160]) for m in re.finditer(r'<text[^>]*x="([0-9.]+)"[^>]*y="([0-9.]+)"[^>]*>(.*?)</text>', open(path, encoding="utf-8").read(), re.S) if needle in re.sub(r"<[^>]+>", "", m.group(3))]
for needle in ["TESTI IN RUSSO", "OGNI SETTIMANA", "SPIEGAZIONI IN ITALIANO", "Pagina ", "Nota — "]:
    for label, d in [("W43", W43), ("W45-ed", ED)]:
        hits = []
        for p in PAGES:
            for x, y, t in find_text(f"{d}/{p}.svg", needle):
                hits.append((p, x, y, t))
        print(f"  {needle!r} {label}: {hits[:4]} (n={len(hits)})")
# badge full element detail W43 vs W45-ed P1
for label, d in [("W43", W43), ("W45-ed", ED), ("core", CORE)]:
    s = open(f"{d}/p1-pervaya.svg", encoding="utf-8").read()
    for m in re.finditer(r"<text[^>]*>(.*?)</text>", s, re.S):
        t = re.sub(r"<[^>]+>", "", m.group(1))
        if "TESTI IN RUSSO" in t or "ЕЖЕНЕДЕЛЬНАЯ" in t:
            # get full opening tag
            start = s.rfind("<text", 0, m.start())
            print(f"  P1 badge-line {label}: tag={s[start:m.start()+5][:220]!r} text={t!r}")
# W43 vs ed footer + top strip raw
for label, d in [("W43", W43), ("W45-ed", ED)]:
    for p in ["p1-pervaya", "p2-zhizn"]:
        ts = texts(f"{d}/{p}.svg")
        print(f"  {label} {p} footer-ish: {[t for t in ts if 'Pagina' in t or 'SETTIMANALE' in t][:3]}")

print("== BUILD LOG + REGISTRY ==")
log = open(os.path.join(GOAL, "hidden_files/weekly-report-w45-ru-it-build/run-w45-ru-it.log"), encoding="utf-8").read()
print("  FLOW OVERFLOW:", log.count("FLOW OVERFLOW"), " HEAD TOO WIDE:", log.count("HEAD TOO WIDE"))
print("  log tail:", log[-600:])
vlog = open(os.path.join(GOAL, "hidden_files/weekly-report-w45-ru-it-build/verify-w45-ru-it.log"), encoding="utf-8").read()
print("  verify log tail:", vlog[-800:])

json.dump(report, open(os.path.join(OUT, "audit.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("DONE")
