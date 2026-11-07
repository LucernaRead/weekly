# -*- coding: utf-8 -*-
"""Follow-up checks for W45 KO x NL proofread."""
import os, re, sys, json
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools"))
import occlusion_audit as OA
GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = os.path.join(GOAL, "files/weekly-report-w45-ko-nl")
CORE = os.path.join(GOAL, "files/weekly-report-w45-ko-core")
W43 = os.path.join(GOAL, "files/weekly-report-ko-nl")
PAGES = ["p1-pyoji.svg", "p2-saenghwal.svg", "p3-munhwa.svg", "p4-seupocheu.svg",
         "p5-cheongnyeon.svg", "p6-gipi.svg", "p7-mal.svg", "p8-siheom.svg"]
def els(d, pg): return OA.parse_svg(open(os.path.join(d, "svg", pg), encoding="utf-8").read())[0]
def texts(d, pg): return [e for e in els(d, pg) if e.kind == "text" and e.text.strip()]

print("== 1. badge (fill #a4553a, size 20) ==")
for name, d in [("core", CORE), ("w43", W43), ("ed", ED)]:
    hits = [(e.text, round(e.baseline, 1), OA.fnum(e.attrs, "font-size"), e.attrs.get("fill"), e.attrs.get("font-weight"), OA.fnum(e.attrs, "x"), e.attrs.get("text-anchor"))
            for e in texts(d, "p1-pyoji.svg") if e.attrs.get("fill") == "#a4553a"]
    print(f"   {name}: {hits}")

print("== 2. section headers ed vs w43 ==")
heads = ["생활 · Dagelijks leven", "문화 · Cultuur", "스포츠 · Sport", "청년 · Jongeren",
         "깊이 읽기 · Dieper lezen", "말 공부 · Taal", "시험과 답 · Toets en antwoorden"]
for h in heads:
    he = [pg for pg in PAGES for e in texts(ED, pg) if e.text == h]
    hw = [pg for pg in PAGES for e in texts(W43, pg) if e.text == h]
    print(f"   {h}: ed={he} w43={hw}")
print("== 2b. instruction labels ==")
for lab in ["Vul in", "Koppel", "Herschrijf", "Bouw", "Vertaal", "W of O", "Schrijf"]:
    ce = sum(1 for pg in PAGES for e in texts(ED, pg) if e.text == lab)
    cw = sum(1 for pg in PAGES for e in texts(W43, pg) if e.text == lab)
    print(f"   {lab}: ed_texts={ce} w43_texts={cw}")

print("== 3. P7 Korean-only lines diff core vs ed (pure Korean texts) ==")
def kor_lines(d):
    return [(pg, e.text) for pg in PAGES for e in texts(d, pg) if e.text and all(("\uac00" <= ch <= "\ud7af" or ch in " ·—.,!?~'\"()[]「」『』〜" or ch.isspace() or ch.isdigit()) for ch in e.text) and any("\uac00" <= ch <= "\ud7af" for ch in e.text)]
# simpler: P7 texts containing Hangul, compare sets
p7e = [(e.text) for e in texts(ED, "p7-mal.svg") if any("\uac00" <= ch <= "\ud7af" for ch in e.text)]
p7c = [(e.text) for e in texts(CORE, "p7-mal.svg") if any("\uac00" <= ch <= "\ud7af" for ch in e.text)]
from collections import Counter
print(f"   P7 Hangul-containing lines: ed={len(p7e)} core={len(p7c)}")
print("   in core only:", [t for t, c in (Counter(p7c) - Counter(p7e)).items() for _ in range(c)])
print("   in ed only:", [t for t, c in (Counter(p7e) - Counter(p7c)).items() for _ in range(c)])

print("== 4. P7 #104 numbering: texts near y 960-1010, x 65 ==")
for e in texts(ED, "p7-mal.svg"):
    if abs(OA.fnum(e.attrs, "x") - 65) < 1 and 940 < e.baseline < 1030:
        print(f"   ED y={e.baseline} {e.text!r}")
for e in texts(CORE, "p7-mal.svg"):
    if abs(OA.fnum(e.attrs, "x") - 65) < 1 and 940 < e.baseline < 1030:
        print(f"   CORE y={e.baseline} {e.text!r}")
print("   P7 exercise number texts (ed):", sorted(set(e.text for e in texts(ED, "p7-mal.svg") if re.fullmatch(r"\d+\.", e.text.strip()))))
print("   P7 A2 stem raw bytes check:")
for d, nm in [(ED, "ed"), (CORE, "core")]:
    s = open(os.path.join(d, "svg/p7-mal.svg"), encoding="utf-8").read()
    m = re.search(r"'김장'은 무슨 뜻이에요\? A\. ([^<]*)", s)
    print(f"   {nm}: {m.group(0) if m else 'NOT FOUND'}")

print("== 5. P2 all texts (find ssam honest caption) ==")
for e in texts(ED, "p2-saenghwal.svg"):
    print(f"   y={e.baseline} x={OA.fnum(e.attrs,'x')} {e.text!r}")
print("== 5b. CREDITS.md ==")
print(open(os.path.join(GOAL, "hidden_files/weekly-report-w45-ko-nl-build/assets/CREDITS.md"), encoding="utf-8").read())
print("== 5c. full credit lines joined (P3/P4, consecutive same-x lines) ==")
for pg in ["p3-munhwa.svg", "p4-seupocheu.svg"]:
    es = [e for e in texts(ED, pg) if "사진:" in e.text or "그림:" in e.text or "Wikimedia" in e.text or "Commons" in e.text]
    for e in es: print(f"   {pg} y={e.baseline} x={OA.fnum(e.attrs,'x')} {e.text!r}")

print("== 6. P8 #55/#131 raw rendered lines ==")
for n_want in (55, 131):
    for d, nm in [(ED, "ed")]:
        es = [e for e in texts(d, "p8-siheom.svg") if e.baseline and e.baseline > 1328]
        byx = {}
        for e in es: byx.setdefault(round(OA.fnum(e.attrs, "x"), 1), []).append(e)
        for x, g in byx.items():
            g.sort(key=lambda e: e.baseline)
            for i, e in enumerate(g):
                if re.match(rf"^{n_want}\.\s", e.text):
                    print(f"   #{n_want} {nm} x={x}:")
                    for e2 in g[i:i+3]: print(f"      y={e2.baseline} {e2.text!r}")
print("== 6b. registry notes #55/#131 (edition source via build content? use reg-scratch if present) ==")
import glob
for f in glob.glob(os.path.join(GOAL, "hidden_files/weekly-report-w45-ko-nl-build/reg-scratch-ed/reg.json")):
    reg = json.load(open(f, encoding="utf-8"))
    for e in reg:
        if e["n"] in (55, 131, 104, 137, 138, 139, 140, 150):
            print(f"   REG ed #{e['n']}: key={e['key']!r} note={e['note']!r}")

print("== 7. orphan first/last char scan (all rendered lines, ed + core) ==")
CLOSERS = set(")]}〉》.,!?%:;\"'」』）】〕、。·")
OPENERS = set("「『（【〈《([{\"“‘")
# Note: ' is ambiguous; handled separately. Report lines starting with unambiguous closers, and ending with openers.
for d, nm in [(ED, "ed"), (CORE, "core")]:
    start_flags, end_flags = [], []
    for pg in PAGES:
        for e in texts(d, pg):
            t = e.text.strip()
            if not t: continue
            if t[0] in CLOSERS - {"'"}:
                start_flags.append((pg, round(OA.fnum(e.attrs, "x"), 1), round(e.baseline, 2), t[:40]))
            if t[-1] in OPENERS:
                end_flags.append((pg, round(OA.fnum(e.attrs, "x"), 1), round(e.baseline, 2), t[-40:]))
    print(f"   {nm}: start-with-unambiguous-closer={start_flags}")
    print(f"   {nm}: end-with-opener={end_flags}")

print("== 8. P7 letters box geometry ed vs core ==")
for d, nm in [(ED, "ed"), (CORE, "core")]:
    es = els(d, "p7-mal.svg")
    rects = [(OA.fnum(e.attrs, "x"), OA.fnum(e.attrs, "y"), OA.fnum(e.attrs, "width"), OA.fnum(e.attrs, "height")) for e in es if e.kind == "rect" and abs(OA.fnum(e.attrs, "x") - 1451) < 1 and 1200 < OA.fnum(e.attrs, "y") < 1900]
    lets = [e for e in es if e.kind == "text" and abs(OA.fnum(e.attrs, "x") - 1473) < 1 and 1350 < e.baseline < 1900]
    last = max(lets, key=lambda e: e.baseline) if lets else None
    print(f"   {nm}: letters rects={rects} last_baseline={last.baseline if last else None} last_ink_bottom={last.box[3] if last and last.box else None} last_text={last.text if last else None}")
    lines = [(OA.fnum(e.attrs, "y1")) for e in es if e.kind == "line" and 1850 < OA.fnum(e.attrs, "y1") < 1950]
    print(f"   {nm}: rule lines 1850-1950={lines}")
    teas = [(OA.fnum(e.attrs, "y"), OA.fnum(e.attrs, "y") + OA.fnum(e.attrs, "height")) for e in es if e.kind == "rect" and OA.fnum(e.attrs, "height") == 118 and OA.fnum(e.attrs, "y") > 2400]
    print(f"   {nm}: teaser rect (y,bottom)={teas}")
