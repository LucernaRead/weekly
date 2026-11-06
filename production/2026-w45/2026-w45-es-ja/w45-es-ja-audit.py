# -*- coding: utf-8 -*-
"""W45 ES x JA builder self-audit: P6 chart graze, same-baseline ink,
line-start orphans, kanji-only nodes, furniture completeness.
Reads shipped SVGs only; writes nothing into the edition dir."""
import re, html, sys, os
sys.path.insert(0, "/home/hatch/workspace/goals/lucernaread-social-media-operations/tools")
import tables as T
from PIL import ImageFont

G = "/home/hatch/workspace/goals/lucernaread-social-media-operations/files"
ED = f"{G}/weekly-report-w45-es-ja/svg"
CO = f"{G}/weekly-report-w45-es-core/svg"
FONTS = T.load()["fonts"]
FACE_INDEX = FONTS["face_index"]
_cache = {}
def get_font(family, size, bold):
    if "Unifraktur" in family:
        path, idx = FONTS["blackletter"], 0
    elif "Serif" in family:
        path = FONTS["serif_bold"] if bold else FONTS["serif_regular"]
        idx = FACE_INDEX["JP"]
    else:
        path = FONTS["sans_bold"] if bold else FONTS["sans_regular"]
        idx = FACE_INDEX["JP"]
    key = (path, idx, round(size * 4))
    if key not in _cache:
        _cache[key] = ImageFont.truetype(path, int(round(size * 4)), index=idx)
    return _cache[key]
def ink_box(x, y, text, family, size, bold, anchor):
    f = get_font(family, size, bold)
    l, t, r, b = [v / 4 for v in f.getbbox(text)]
    if anchor == "end":
        return (x - (r - l), y + t, x - l, y + b)
    if anchor == "middle":
        cx = x - (r + l) / 2
        return (cx + l, y + t, cx + r, y + b)
    return (x + l, y + t, x + r, y + b)

TEXT_RE = re.compile(r'<text x="([\d.]+)" y="([\d.]+)"([^>]*)>(.*?)</text>', re.S)
def parse(path):
    s = open(path, encoding="utf-8").read()
    els = []
    for m in TEXT_RE.finditer(s):
        attrs = m.group(3)
        fam = re.search(r'font-family="([^"]+)"', attrs)
        sz = re.search(r'font-size="([\d.]+)"', attrs)
        bold = 'font-weight="700"' in attrs or 'font-weight="bold"' in attrs
        anch = re.search(r'text-anchor="([^"]+)"', attrs)
        els.append({"x": float(m.group(1)), "y": float(m.group(2)),
                    "fam": fam.group(1) if fam else "", "size": float(sz.group(1)) if sz else 20,
                    "bold": bold, "anchor": anch.group(1) if anch else "start",
                    "t": html.unescape(re.sub(r"<[^>]+>", "", m.group(4)))})
    rects = [(float(a), float(b), float(c), float(d))
             for a, b, c, d in re.findall(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"', s)]
    return els, rects, s

pages = ["p1-portada", "p2-vida", "p3-cultura", "p4-deporte", "p5-juventud", "p6-afondo", "p7-lengua", "p8-ejercicios"]

print("== P6 Inmigración graze (edition vs core, text ink vs rects) ==")
for ed, path in [("core", f"{CO}/p6-afondo.svg"), ("edition", f"{ED}/p6-afondo.svg")]:
    els, rects, s = parse(path)
    # paint order: find index of each element in raw string
    order = []
    for kind, m in [("rect", mm) for mm in re.finditer(r'<rect[^>]*>', s)] + [("text", mm) for mm in TEXT_RE.finditer(s)]:
        order.append((m.start(), kind, m.group(0)))
    order.sort()
    for e in els:
        if e["t"].strip() != "Inmigración":
            continue
        box = ink_box(e["x"], e["y"], e["t"], e["fam"], e["size"], e["bold"], e["anchor"])
        print(f"  {ed} Inmigración ink box: {[round(v,1) for v in box]} (baseline y={e['y']})")
        # rects drawn AFTER this text (later in paint order) overlapping ink
        tpos = s.find(f">{e['t']}</text>")
        for m in re.finditer(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*>', s):
            if m.start() < tpos:
                continue
            rx, ry, rw, rh = map(float, m.groups())
            ox = min(box[2], rx + rw) - max(box[0], rx)
            oy = min(box[3], ry + rh) - max(box[1], ry)
            if ox > 0 and oy > 0:
                print(f"    OVERLAP rect x={rx} y={ry} w={rw} h={rh} overlap={ox:.1f}x{oy:.1f}")
        # rects drawn BEFORE (text over rect is fine) and nearby rects within 10px
        for m in re.finditer(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*>', s):
            rx, ry, rw, rh = map(float, m.groups())
            if abs(ry + rh - box[1]) < 12 or abs(ry - box[3]) < 12:
                if rx < box[2] and rx + rw > box[0]:
                    print(f"    NEAR rect x={rx} y={ry} w={rw} h={rh} (vertical gap to ink: {ry-box[3]:.1f}/{box[1]-(ry+rh):.1f})")

print("== same-baseline ink scan (all pages, edition) ==")
nflag = 0
for p in pages:
    els, _, _ = parse(f"{ED}/{p}.svg")
    boxes = []
    for e in els:
        if not e["t"].strip():
            continue
        boxes.append((e["y"], ink_box(e["x"], e["y"], e["t"], e["fam"], e["size"], e["bold"], e["anchor"]), e["t"]))
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            y1, b1, t1 = boxes[i]; y2, b2, t2 = boxes[j]
            if abs(y1 - y2) > 0.01:
                continue
            ox = min(b1[2], b2[2]) - max(b1[0], b2[0])
            oy = min(b1[3], b2[3]) - max(b1[1], b2[1])
            if ox > 0 and oy > 0:
                print(f"  {p} SAME-LINE OVERLAP {ox:.1f}x{oy:.1f}: {t1[:40]!r} vs {t2[:40]!r}")
                nflag += 1
print("  same-baseline flags:", nflag)

print("== line-start orphan scan (NO_START full-width + SMALL KANA + ASCII closers) ==")
SMALL_KANA = "ぁぃぅぇぉっゃゅょゎァィゥェォッャュョヮ"
NO_START = set("。、，．！？：；）」』】ー…‥・)]}.,!?%:;\"'") | set(SMALL_KANA)
norph = 0
for p in pages:
    els, _, _ = parse(f"{ED}/{p}.svg")
    for e in els:
        t = e["t"].strip()
        if t and t[0] in NO_START:
            print(f"  {p} y={e['y']}: {t[:50]!r}")
            norph += 1
print("  orphan line-starts:", norph)

print("== kanji-only nodes (CJK, no kana) in edition SVGs ==")
KANJI = re.compile(r"[\u4e00-\u9fff]")
KANA = re.compile(r"[\u3040-\u30ff]")
SIMP_ONLY = set("语说读让练观选词对头汉简发现实")
for p in pages:
    els, _, _ = parse(f"{ED}/{p}.svg")
    for e in els:
        t = e["t"]
        if KANJI.search(t) and not KANA.search(t):
            simp = [c for c in t if c in SIMP_ONLY]
            print(f"  {p}: {t[:60]!r} simp_only={simp}")

print("== furniture completeness ==")
all_ed = {p: parse(f"{ED}/{p}.svg")[0] for p in pages}
badge = "スペイン語テキスト · 日本語の解説 — 日本語読者のための版"
foot = "La Lucerna · スペイン語週刊 VOL.2 · 本文はスペイン語 · 解説は日本語"
for p in pages:
    ts = [e["t"] for e in all_ed[p]]
    print(f"  {p}: footer={sum(1 for t in ts if t==foot)} pageline={sum(1 for t in ts if re.match(r'^\\d ページ（全 8 ページ）$', t))} badge={sum(1 for t in ts if t==badge)}")
p1ts = [e["t"] for e in all_ed["p1-portada"]]
print("  P1 top strip:", [t for t in p1ts if "CADA SEMANA" in t])
print("  P1 edition line:", [t for t in p1ts if "週 刊" in t])
print("  P1 band right:", [t for t in p1ts if "29-Nまで" in t or "今号のトップ" in t])
p8ts = [e["t"] for e in all_ed["p8-ejercicios"]]
print("  P8 header:", [t for t in p8ts if "RESPUESTAS" in t])
print("  P8 right note:", [t for t in p8ts if "各問に日本語" in t])
print("  P8 separators:", sorted(set(t for t in p8ts if re.match(r'^— \d ページ —$', t))))
heads = []
for p in pages:
    for e in all_ed[p]:
        if re.match(r"^(VIDA|CULTURA|DEPORTE|JUVENTUD|A FONDO|LENGUA|EJERCICIOS Y RESPUESTAS) · ", e["t"]):
            heads.append((p, e["t"]))
print("  section heads:", heads)
