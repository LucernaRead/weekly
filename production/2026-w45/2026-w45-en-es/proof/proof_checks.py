# -*- coding: utf-8 -*-
"""Independent proof checks for W45 EN x ES. Reads deliverables + core + W43 only.
Writes only into this proof dir (log/json). Uses tools/occlusion_audit.py font
resolution (same TTFs as the audit) for geometry; all counts recomputed here.
"""
import sys, os, re, json, html, hashlib, difflib
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools"))
import occlusion_audit as OA
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = os.path.join(BASE, "files/weekly-report-w45-en-es/svg")
CORE = os.path.join(BASE, "files/weekly-report-w45-en-core/svg")
W43 = os.path.join(BASE, "files/weekly-report-en-es/svg")
OUT = os.path.dirname(os.path.abspath(__file__))
LOG = open(os.path.join(OUT, "proof_checks.log"), "w", encoding="utf-8")
def log(*a):
    s = " ".join(str(x) for x in a)
    print(s); LOG.write(s + "\n"); LOG.flush()
RES = {}

TEXT_RE = re.compile(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"([^>]*)>([^<]*)</text>')
RECT_RE = re.compile(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*fill="([^"]+)"')
CJK = re.compile(r"[\u2e80-\u9fff\u3040-\u30ff\uac00-\ud7af\uff00-\uffef]")

def parse(path):
    src = open(path, encoding="utf-8").read()
    texts = []
    for m in TEXT_RE.finditer(src):
        x, y, fam, size, attrs, t = float(m.group(1)), float(m.group(2)), m.group(3), float(m.group(4)), m.group(5), html.unescape(m.group(6))
        am = re.search(r'text-anchor="(start|middle|end)"', attrs)
        texts.append({"x": x, "y": y, "fam": fam, "size": size, "bold": 'font-weight="700"' in attrs,
                      "anchor": am.group(1) if am else "start", "t": t, "pos": m.start()})
    rects = [{"x": float(m.group(1)), "y": float(m.group(2)), "w": float(m.group(3)),
              "h": float(m.group(4)), "fill": m.group(5), "pos": m.start()}
             for m in RECT_RE.finditer(src)]
    return texts, rects, src

def font_for(fam, bold, size):
    path, idx = OA.resolve_font(fam, size, bold)
    return ImageFont.truetype(path, int(round(size * 4)), index=idx)

def ink_span(t, fam, bold, size, x, anchor):
    f = font_for(fam, bold, size)
    bb = f.getbbox(t); adv = f.getlength(t) / 4.0
    l, r = bb[0] / 4.0, bb[2] / 4.0
    if anchor == "start": return x + l, x + r, adv
    if anchor == "end": return x - adv + l, x - adv + r, adv
    return x - adv / 2 + l, x - adv / 2 + r, adv

def page_texts(d, fn):
    texts, _, _ = parse(os.path.join(d, fn))
    return texts

def all_texts(d):
    out = {}
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".svg"): out[fn] = page_texts(d, fn)
    return out

# ---------- 1. banned word + CJK ----------
BANNED = chr(0x6865) + chr(0x63a5)
hits = {}
for d, label in [(ED, "ed"), (CORE, "core")]:
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".svg"):
            src = open(os.path.join(d, fn), encoding="utf-8").read()
            if BANNED in src: hits[f"{label}/{fn}"] = src.count(BANNED)
for f in ["WEEKLY-KIT.md", "ABSTRACT.txt"]:
    src = open(os.path.join(BASE, "files/weekly-report-w45-en-es", f), encoding="utf-8").read()
    if BANNED in src: hits[f] = src.count(BANNED)
log("== 1. banned-word hits (must be {}):", hits)
RES["banned_hits"] = hits
cjk_ed, cjk_core = {}, {}
for d, acc in [(ED, cjk_ed), (CORE, cjk_core)]:
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".svg"):
            src = open(os.path.join(d, fn), encoding="utf-8").read()
            acc[fn] = len(CJK.findall(html.unescape(re.sub(r"<[^>]+>", "", src))))
log("CJK per page ED:", cjk_ed, "total", sum(cjk_ed.values()))
log("CJK per page CORE:", cjk_core, "total", sum(cjk_core.values()))
RES["cjk_ed"] = cjk_ed; RES["cjk_core"] = cjk_core

# ---------- 2. freeze-diff adjudication (my own freeze-diff.json) ----------
diff = json.load(open(os.path.join(OUT, "freeze-diff.json")))
ed_pages = all_texts(ED); core_pages = all_texts(CORE)
def words(s):
    return re.findall(r"[A-Za-zÀ-ÿ0-9'’\-]+", s.lower())
STRAP = None
for t in core_pages["p1-front.svg"]:
    if abs(t["y"] - 372) < 0.01: STRAP = t["t"]
log("core P1 strapline (y=372):", repr(STRAP))
prob = []
for pg in sorted(diff["pages"], key=int):
    fn = {1: "p1-front.svg", 2: "p2-life.svg", 3: "p3-culture.svg", 4: "p4-sport.svg",
          5: "p5-jeunesse.svg", 6: "p6-politique.svg", 7: "p7-langue.svg", 8: "p8-exercices.svg"}[int(pg)]
    added = [a["text"] for a in diff["pages"][pg]["added_strings"]]
    removed = [r["text"] for r in diff["pages"][pg]["removed_strings"]]
    added_words = set()
    for a in added: added_words.update(words(a))
    log(f"-- page {pg} {fn}: +{len(added)} -{len(removed)}")
    for r in removed:
        if CJK.search(r):
            verdict = "CJK explanation-layer removal (expected)"
        elif r == STRAP:
            verdict = "BADGE REPLACEMENT (P1 strapline -> W43 furniture)"
        else:
            rw = set(words(r))
            missing = sorted(w for w in rw if w not in added_words)
            verdict = "REFLOW (all words reappear in added strings)" if not missing else f"POTENTIAL LOSS missing words={missing}"
            if missing: prob.append((fn, r, missing))
        log(f"   REMOVED {verdict}: {r!r}")
    RES.setdefault("freeze_removed_problems", prob)
log("freeze removed problems:", prob)
# added-side: ASCII-only added strings whose words are NOT all in core page words
for pg in sorted(diff["pages"], key=int):
    fn = {1: "p1-front.svg", 2: "p2-life.svg", 3: "p3-culture.svg", 4: "p4-sport.svg",
          5: "p5-jeunesse.svg", 6: "p6-politique.svg", 7: "p7-langue.svg", 8: "p8-exercices.svg"}[int(pg)]
    core_words = set()
    for t in core_pages[fn]: core_words.update(words(t["t"]))
    review = []
    for a in diff["pages"][pg]["added_strings"]:
        s = a["text"]
        if all(ord(c) < 128 for c in s):
            w = set(words(s))
            if w and not w <= core_words:
                review.append(s)
    log(f"page {pg} ASCII-only added strings with novel words (expect only furniture labels): {review}")
    RES.setdefault("added_ascii_novel", {})[pg] = review

# ---------- 3. P8 independent segmenter ----------
def p8_segments(d):
    texts, _, _ = parse(os.path.join(d, "p8-exercices.svg"))
    # answers elements: from ANSWERS header to before last 2 footer texts
    idx = next(i for i, t in enumerate(texts) if re.match(r"^ANSWERS", t["t"]))
    els = texts[idx:-2]
    def is_hdr(t):
        return t.startswith("ANSWERS") or (bool(re.match(r"^— .* —$", t.strip())) and len(t.strip()) <= 34)
    stream = ""
    for t in els:
        if t["t"].startswith("ANSWERS"): continue
        piece = "·" if is_hdr(t["t"]) else t["t"]
        if not stream: stream = piece
        elif CJK.search(stream[-1:]) or CJK.search(piece[:1]): stream += piece
        else: stream += " " + piece
    stream = re.sub(r"\s+", " ", stream).strip()
    stream = re.sub(r"^[\s·]+", "", stream)
    assert stream.startswith("1. "), stream[:20]
    entries, pos, cur = {}, re.match(r"1\.\s", stream).end(), 1
    while cur < 150:
        mm = re.compile(r"·\s*" + str(cur + 1) + r"\.\s").search(stream, pos)
        assert mm, f"split fail at {cur+1}"
        entries[cur] = stream[pos:mm.start()].strip().rstrip("·").strip()
        pos, cur = mm.end(), cur + 1
    entries[150] = stream[pos:].strip()
    def noted(seg):
        # trailing paren group?
        for op, cl in (("(", ")"), ("（", "）")):
            depth, st, groups = 0, None, []
            for j, ch in enumerate(seg):
                if ch == op:
                    if depth == 0: st = j
                    depth += 1
                elif ch == cl and depth > 0:
                    depth -= 1
                    if depth == 0: groups.append((st, j))
            for g in groups:
                if seg[g[1] + 1:].strip() == "":
                    return True, seg[:g[0]].strip()
        if " — " in seg:
            k, tail = seg.split(" — ", 1)
            if tail.strip(): return True, k.strip()
        return False, seg
    res = {}
    for n, seg in entries.items():
        h, k = noted(seg)
        res[n] = {"has_note": h, "key": k, "seg": seg}
    return res
ed_p8 = p8_segments(ED); co_p8 = p8_segments(CORE)
ed_noted = sorted(n for n, v in ed_p8.items() if v["has_note"])
co_noted = sorted(n for n, v in co_p8.items() if v["has_note"])
log("== 3. P8 independent segmenter: core noted", len(co_noted), "ed noted", len(ed_noted))
log("   noted sets equal:", co_noted == ed_noted, "missing:", sorted(set(co_noted) - set(ed_noted)), "extra:", sorted(set(ed_noted) - set(co_noted)))
log("   total segments core/ed:", len(co_p8), len(ed_p8), "numbers 1..150 continuous:", sorted(co_p8) == list(range(1, 151)) and sorted(ed_p8) == list(range(1, 151)))
kd = sorted(n for n in range(1, 151) if co_p8[n]["key"] != ed_p8[n]["key"])
log("   keydiff (my segmenter):", kd)
for n in kd:
    log(f"   KEY {n} CORE printed segment: {co_p8[n]['seg']!r}")
    log(f"   KEY {n} ED   printed segment: {ed_p8[n]['seg']!r}")
RES["p8_noted_core"] = co_noted; RES["p8_noted_ed"] = ed_noted; RES["p8_keydiff"] = kd
# P8 key-area CJK + paren style
ed_p8src = open(os.path.join(ED, "p8-exercices.svg"), encoding="utf-8").read()
ed_key_texts = [t for t in ed_pages["p8-exercices.svg"] if t["y"] >= 1838]
log("   ED P8 key-area texts CJK count:", sum(len(CJK.findall(t["t"])) for t in ed_key_texts))
log("   ED P8 key paren style: half-width '(' count in key area:", sum(t["t"].count("(") for t in ed_key_texts),
    "full-width count:", sum(t["t"].count("（") for t in ed_key_texts))
co_key_texts = [t for t in core_pages["p8-exercices.svg"] if t["y"] >= 1838]
log("   CORE P8 key paren style: half-width:", sum(t["t"].count("(") for t in co_key_texts),
    "full-width:", sum(t["t"].count("（") for t in co_key_texts))
# P8 E stems (battery) for keydiff context
for label, pages in [("CORE", core_pages), ("ED", ed_pages)]:
    stems = [t["t"] for t in pages["p8-exercices.svg"] if ("Translate" in t["t"] or "Traduce" in t["t"] or "翻译" in t["t"])]
    log(f"   {label} E instruction lines:", stems)

# ---------- 4. P1 masthead TEXTX pixel verification (independent redraw) ----------
def render_mask(text, fam, size, bold, x, anchor):
    path, idx = OA.resolve_font(fam, size, bold)
    f = ImageFont.truetype(path, int(round(size)), index=idx)
    adv = f.getlength(text)
    if anchor == "start": left = x
    elif anchor == "end": left = x - adv
    else: left = x - adv / 2
    mask = Image.new("1", (1950, 2700), 0)
    d = ImageDraw.Draw(mask)
    d.text((left, 0), text, font=f, fill=1, anchor="ls")  # baseline handled below via offset trick
    # NOTE: anchor 'ls' puts baseline at y=0; re-render properly with baseline y:
    return mask, f, adv
def ink_box_and_mask(text, fam, size, bold, x, y, anchor):
    path, idx = OA.resolve_font(fam, size, bold)
    f = ImageFont.truetype(path, int(round(size)), index=idx)
    adv = f.getlength(text)
    if anchor == "start": left = x
    elif anchor == "end": left = x - adv
    else: left = x - adv / 2
    mask = Image.new("1", (1950, 2700), 0)
    d = ImageDraw.Draw(mask)
    d.text((left, y), text, font=f, fill=1, anchor="ls")
    bb = mask.getbbox()
    return bb, mask
mast = next(t for t in ed_pages["p1-front.svg"] if t["t"] == "The Lucerna")
hdr = next(t for t in ed_pages["p1-front.svg"] if t["t"].startswith("SEMANARIO EN"))
log("== 4. masthead:", mast, "header:", hdr)
bb1, m1 = ink_box_and_mask(mast["t"], mast["fam"], mast["size"], mast["bold"], mast["x"], mast["y"], mast["anchor"])
bb2, m2 = ink_box_and_mask(hdr["t"], hdr["fam"], hdr["size"], hdr["bold"], hdr["x"], hdr["y"], hdr["anchor"])
log("   PIL masthead ink bbox (x0,y0,x1,y1):", bb1)
log("   PIL header ink bbox:", bb2)
from PIL import ImageChops
inter = ImageChops.logical_and(m1, m2)
log("   PIXEL OVERLAP count (masthead & header masks):", sum(1 for px in inter.getdata() if px))
# y-band analysis: rows where both have ink
def rows_with_ink(mask):
    rows = set()
    b = mask.getbbox()
    if not b: return rows
    px = mask.load()
    for yy in range(b[1], b[3] + 1):
        for xx in range(b[0], b[2] + 1):
            if px[xx, yy]: rows.add(yy); break
    return rows
r1, r2 = rows_with_ink(m1), rows_with_ink(m2)
log("   masthead ink rows:", min(r1), "..", max(r1), " header ink rows:", min(r2), "..", max(r2), " shared rows:", sorted(r1 & r2))
# x-sets within shared rows
if r1 & r2:
    px1, px2 = m1.load(), m2.load()
    for yy in sorted(r1 & r2):
        xs1 = {xx for xx in range(1950) if px1[xx, yy]}
        xs2 = {xx for xx in range(1950) if px2[xx, yy]}
        log(f"   shared row y={yy}: masthead x {min(xs1)}..{max(xs1)} n={len(xs1)}; header x {min(xs2)}..{max(xs2)} n={len(xs2)}; x-overlap n={len(xs1 & xs2)}")
RES["masthead_bbox"] = bb1; RES["header_bbox"] = bb2

# ---------- 5. rowcheck (decoded) / edgescan / chartcheck, my implementation ----------
def rowcheck(d, label):
    bad = []
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".svg"): continue
        texts, _, _ = parse(os.path.join(d, fn))
        rows = {}
        for e in texts:
            if not e["t"].strip(): continue
            a, b, _ = ink_span(e["t"], e["fam"], e["bold"], e["size"], e["x"], e["anchor"])
            rows.setdefault(round(e["y"], 1), []).append((a, b, e["t"]))
        for y, spans in rows.items():
            spans.sort()
            for (a1, b1, t1), (a2, b2, t2) in zip(spans, spans[1:]):
                if a2 - b1 < 6: bad.append((fn, y, round(a2 - b1, 1), t1[:45], t2[:45]))
    log(f"== 5a. rowcheck(decoded) {label}: collisions={len(bad)}")
    for b in bad: log("   ", b)
    return bad
rc_ed = rowcheck(ED, "ED"); rc_co = rowcheck(CORE, "CORE")
RES["rowcheck_ed"] = rc_ed; RES["rowcheck_core"] = rc_co
# the & pair on P8 y=116, decoded vs raw '&amp;'
p8t = ed_pages["p8-exercices.svg"]
pair = [t for t in p8t if abs(t["y"] - 116) < 0.01]
log("   P8 y=116 texts:", [(t["x"], t["anchor"], t["t"][:50]) for t in pair])
for t in pair:
    a, b, adv = ink_span(t["t"], t["fam"], t["bold"], t["size"], t["x"], t["anchor"])
    log(f"   decoded ink span {t['t'][:30]!r}: {a:.1f}..{b:.1f} adv={adv:.1f}")
    raw = t["t"].replace("&", "&amp;")
    if raw != t["t"]:
        a2, b2, _ = ink_span(raw, t["fam"], t["bold"], t["size"], t["x"], t["anchor"])
        log(f"   UNDECODED span {raw[:30]!r}: {a2:.1f}..{b2:.1f}")
if len(pair) >= 2:
    srt = sorted(pair, key=lambda t: ink_span(t["t"], t["fam"], t["bold"], t["size"], t["x"], t["anchor"])[0])
    l = ink_span(srt[0]["t"], srt[0]["fam"], srt[0]["bold"], srt[0]["size"], srt[0]["x"], srt[0]["anchor"])
    r = ink_span(srt[1]["t"], srt[1]["fam"], srt[1]["bold"], srt[1]["size"], srt[1]["x"], srt[1]["anchor"])
    log(f"   decoded gap P8 y=116: {r[0]-l[1]:.1f}px")

def edgescan(d, label):
    flags, margin, mx_all = [], [], {}
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".svg"): continue
        texts, _, _ = parse(os.path.join(d, fn))
        mx = 0.0; items = []
        for e in texts:
            f = font_for(e["fam"], e["bold"], e["size"])
            adv = f.getlength(e["t"]) / 4.0
            if e["anchor"] == "start": ar = e["x"] + adv
            elif e["anchor"] == "end": ar = e["x"]
            else: ar = e["x"] + adv / 2
            mx = max(mx, ar)
            if ar > 1885: items.append((round(ar, 1), e["t"][:60]))
            if ar > 1910: flags.append((fn, round(ar, 1), e["t"][:60]))
        mx_all[fn] = round(mx, 1); margin.append((fn, items))
    log(f"== 5b. edgescan(ADVANCE) {label}: frame flags (>1910)={flags}")
    log(f"   max advance-right per page: {mx_all}")
    for fn, items in margin:
        if items: log(f"   margin-crossers >1885 {fn}: {items}")
    return flags, mx_all, margin
ef_ed, mx_ed, mg_ed = edgescan(ED, "ED"); ef_co, mx_co, mg_co = edgescan(CORE, "CORE")
RES["edge_flags_ed"] = ef_ed; RES["edge_max_ed"] = mx_ed

def chartcheck(d, label):
    texts, rects, _ = parse(os.path.join(d, "p6-politique.svg"))
    labels = [e for e in texts if re.match(r"^(No lines|Work on Tuesday|Travel plans|Habit) : \d+%$", e["t"])]
    intro = [e for e in texts if ("practice survey" in e["t"] or "teaching data" in e["t"])]
    log(f"== 5c. chartcheck {label}: labels={len(labels)} intro={len(intro)}")
    worst = 0.0
    for e in labels + intro:
        f = font_for(e["fam"], e["bold"], e["size"])
        asc, desc = f.getmetrics(); asc, desc = asc / 4.0, desc / 4.0
        adv = f.getlength(e["t"]) / 4.0
        bx0, bx1 = e["x"], e["x"] + adv; by0, by1 = e["y"] - asc, e["y"] + desc
        area = (bx1 - bx0) * (by1 - by0); cov = 0.0
        for r in rects:
            if r["pos"] < e["pos"] or r["fill"] == "none": continue
            ix = max(0.0, min(bx1, r["x"] + r["w"]) - max(bx0, r["x"]))
            iy = max(0.0, min(by1, r["y"] + r["h"]) - max(by0, r["y"]))
            cov = max(cov, ix * iy / area)
        a, b, _ = ink_span(e["t"], e["fam"], e["bold"], e["size"], e["x"], e["anchor"])
        log(f"   {e['t'][:55]!r} baseline-box coverage={cov*100:.1f}%")
        worst = max(worst, cov)
    log(f"   worst={worst*100:.1f}% (gate <30%)")
    return worst
wc_ed = chartcheck(ED, "ED"); wc_co = chartcheck(CORE, "CORE")
RES["chart_worst_ed"] = wc_ed; RES["chart_worst_core"] = wc_co

# ---------- 6. gloss: rendered boxes ----------
def gloss_boxes(d, prefix):
    out = {}
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".svg"): continue
        texts, rects, _ = parse(os.path.join(d, fn))
        boxes = []
        for r in rects:
            if r["fill"] != "#f1ead6": continue
            inside = [u for u in texts if r["x"] <= u["x"] <= r["x"] + r["w"] and r["y"] <= u["y"] <= r["y"] + r["h"]]
            if not inside or not inside[0]["t"].startswith(prefix): continue
            joined = " ".join(u["t"] for u in inside)
            body = joined[len(prefix):] if joined.startswith(prefix) else joined
            items = [s.strip() for s in body.split("·")]
            boxes.append({"rect": r, "joined": joined, "items": items})
        out[fn] = boxes
    return out
gb_ed = gloss_boxes(ED, "Nota — "); gb_co = gloss_boxes(CORE, "译注｜")
def ascii_tokens(s):
    return re.findall(r"[A-Za-z][A-Za-z'’\-]*", s)
for fn in sorted(gb_ed):
    ed_b, co_b = gb_ed[fn], gb_co[fn]
    ed_items = [it for b in ed_b for it in b["items"]]
    co_items = [it for b in co_b for it in b["items"]]
    log(f"== 6. gloss {fn}: ED boxes={len(ed_b)} items={len(ed_items)} | CORE boxes={len(co_b)} items={len(co_items)}")
    for b in ed_b: log("   ED box items:", b["items"])
    for b in co_b: log("   CORE box items:", b["items"])
    # subsequence check on ASCII tokens (headwords preserved in order)
    ed_tok = [tok for b in ed_b for tok in ascii_tokens(" ".join(b["items"]))]
    co_tok = [tok for b in co_b for tok in ascii_tokens(" ".join(b["items"]))]
    # core items include Chinese gloss words (non-ASCII, excluded) and '讲解' prefix stripped already (prefix is 译注｜, body starts with 讲解｜ -> first item starts with 讲解｜)
    co_tok_clean = [t for t in co_tok]
    it = iter(ed_tok); subseq = all(any(x == y for y in it) for x in co_tok_clean)
    log(f"   core ASCII-token sequence is subsequence of ED ASCII-token sequence: {subseq} (core n={len(co_tok_clean)}, ed n={len(ed_tok)})")
    if not subseq:
        sm = difflib.SequenceMatcher(None, co_tok_clean, ed_tok)
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag != "equal": log(f"   diff {tag}: core{co_tok_clean[i1:i2]} ed{ed_tok[j1:j2]}")
    RES.setdefault("gloss", {})[fn] = {"ed_items": len(ed_items), "co_items": len(co_items), "subseq": subseq}

# ---------- 7. P7: example definitions, golden sentences, levels, frequencies ----------
def p7_texts(d):
    return page_texts(d, "p7-langue.svg")
ed7, co7 = p7_texts(ED), p7_texts(CORE)
def norm_ws(s): return re.sub(r"\s+", " ", s).strip()
def quoted_in(texts, y0, y1):
    sel = [t for t in texts if y0 <= t["y"] <= y1]
    joined = norm_ws(" ".join(t["t"] for t in sel))
    return re.findall(r"«(.*?)»", joined), joined
for label, texts in [("CORE", co7), ("ED", ed7)]:
    for colx, col in [(83, "A2"), (545, "B1"), (1007, "B2")]:
        sel = [t for t in texts if t["x"] == colx and 790 <= t["y"] <= 1160]
        joined = norm_ws(" ".join(t["t"] for t in sel))
        log(f"== 7. example box {label} {col}: {joined!r}")
ed_q, _ = quoted_in(ed7, 1236, 1903); co_q, _ = quoted_in(co7, 1236, 1903)
log("== 7. golden sentences CORE:", co_q)
log("== 7. golden sentences ED:  ", ed_q)
log("   golden identical & count 8:", co_q == ed_q and len(ed_q) == 8)
def level_seq(texts):
    seq = []
    for i, t in enumerate(texts):
        if 1236 <= t["y"] <= 1903 and t["t"] in ("A2", "B1", "B2"):
            nxt = texts[i + 1]["t"] if i + 1 < len(texts) else ""
            if re.match(r"^\d+\.$", nxt): seq.append((nxt, t["t"]))
    return seq
log("   level seq CORE:", level_seq(co7))
log("   level seq ED:  ", level_seq(ed7))
def whole_issue_text(d):
    parts = []
    for fn in ["p1-front.svg", "p2-life.svg", "p3-culture.svg", "p4-sport.svg", "p5-jeunesse.svg", "p6-politique.svg", "p7-langue.svg", "p8-exercices.svg"]:
        parts.append(norm_ws(" ".join(t["t"] for t in page_texts(d, fn))))
    return " ".join(parts)
wi_co, wi_ed = whole_issue_text(CORE), whole_issue_text(ED)
for s in ed_q:
    log(f"   freq {s!r}: CORE={wi_co.count(norm_ws(s))} ED={wi_ed.count(norm_ws(s))}")
# P7 headers language attribution
for label, texts in [("CORE", co7), ("ED", ed7)]:
    hdrs = [t["t"] for t in texts if t["y"] in (227.0, 1236.0, 1903.0, 1918.0, 2248.0) or (t["y"] in (797.0, 1002.2, 831.2) and "EXAMPLE" in t["t"])]
    log(f"   P7 headers {label}: {hdrs}")
for label, texts in [("CORE", co7), ("ED", ed7)]:
    notas = [t["t"] for t in texts if 1236 <= t["y"] <= 1903 and (t["t"].startswith("Nota —") or t["t"].startswith("语法点"))]
    log(f"   P7 golden grammar-note prefixes {label}: {[t[:12] for t in notas]}")
    clinic_intro = [t["t"] for t in texts if 1903 <= t["y"] <= 1960 and t["x"] == 65.0]
    log(f"   P7 clinic intro {label}: {clinic_intro}")

# ---------- 8. readers corner ----------
def readers(texts):
    return [t for t in texts if t["x"] == 1013.0 and 1918 <= t["y"] <= 2248]
rc_ed, rc_co = readers(ed7), readers(co7)
log("== 8. readers CORE:", [t["t"] for t in rc_co])
log("== 8. readers ED:  ", [t["t"] for t in rc_ed])
eng_co = [t["t"] for t in rc_co if all(ord(ch) < 128 or ch in "—«»’" for ch in t["t"])]
eng_ed = [t["t"] for t in rc_ed if all(ord(ch) < 128 or ch in "—«»’" for ch in t["t"])]
log("   English lines CORE readers:", eng_co)
log("   English lines ED readers:  ", eng_ed)
log("   English letter paragraph identical (first 3 lines):", [t["t"] for t in rc_co[1:4]] == [t["t"] for t in rc_ed[1:4]])
disc = [t["t"] for t in rc_ed[4:7]]
log("   Spanish disclosure lines verbatim:", disc)
joined_disc = " ".join(disc)
for name, frag in [("fact1 no real letter", "no llegó ninguna carta"), ("fact2 no VOL.1 best p8 text", "el mejor texto de la página 8 de VOL.1"),
                   ("fact3 nothing invented + example stays labeled", "no inventamos nada"), ("fact3b example stays", "el ejemplo sigue marcado"),
                   ("imperative invitation", "¡Envíanos tu carta y tu texto!"), ("VOL.3 promise", "En VOL.3 publicaremos las cartas recibidas.")]:
    log(f"   disclosure check {name}: {'OK' if frag in joined_disc else 'MISSING'} ({frag!r})")
for t in rc_ed[4:7]:
    f = font_for(t["fam"], t["bold"], t["size"]); adv = f.getlength(t["t"]) / 4.0
    log(f"   disclosure line advance-right: {t['x']+adv:.1f} (col4 starts 1451) text={t['t'][:40]!r}")
# P8 writing box frozen English + model
for label, pages in [("CORE", core_pages), ("ED", ed_pages)]:
    wb = [t["t"] for t in pages["p8-exercices.svg"] if t["x"] == 65.0 and 1562 <= t["y"] <= 1656]
    mo = [t["t"] for t in pages["p8-exercices.svg"] if t["x"] == 1011.0 and 1574 <= t["y"] <= 1724]
    log(f"   P8 writing box {label}: {wb}")
    log(f"   P8 model {label} words={len(norm_ws(' '.join(mo)).split())} identical-check stored")
    RES[f"model_{label.lower()}"] = norm_ws(" ".join(mo))
log("   model identical CORE==ED:", RES["model_core"] == RES["model_ed"], "word count:", len(RES["model_ed"].split()))
for label, pages in [("CORE", core_pages), ("ED", ed_pages)]:
    es_instr = [t["t"] for t in pages["p8-exercices.svg"] if t["x"] == 65.0 and 1690 <= t["y"] <= 1719]
    log(f"   P8 writing Spanish instruction {label}: {es_instr}")

# ---------- 9. furniture: badge three-way + W43 deviations ----------
def badge(d):
    texts, _, src = parse(os.path.join(d, "p1-front.svg"))
    for t in texts:
        if abs(t["y"] - 372) < 0.01:
            return t
    return None
for label, d in [("W43", W43), ("W45-CORE", CORE), ("W45-ED", ED)]:
    b = badge(d); log(f"== 9. badge {label}: {b}")
def headers_p8(d):
    texts, _, _ = parse(os.path.join(d, "p8-exercices.svg"))
    return [t["t"] for t in texts if re.match(r"^[A-H] · ", t["t"])]
log("   P8 headers W43:", headers_p8(W43))
log("   P8 headers ED: ", headers_p8(ED))
log("   P8 headers CORE:", headers_p8(CORE))
def p7_phrases_header(d):
    texts, _, _ = parse(os.path.join(d, "p7-langue.svg"))
    return [t["t"] for t in texts if t["y"] == 1236.0 and t["x"] == 65.0]
log("   P7 phrases header W43:", p7_phrases_header(W43), " ED:", p7_phrases_header(ED), " CORE:", p7_phrases_header(CORE))
def p8_band(d):
    texts, _, _ = parse(os.path.join(d, "p8-exercices.svg"))
    return [t["t"] for t in texts if t["y"] == 142.0 and t["x"] == 1872.0]
log("   P8 band line W43:", p8_band(W43), " ED:", p8_band(ED), " CORE:", p8_band(CORE))
def clinic_intro_w(d):
    texts, _, _ = parse(os.path.join(d, "p7-langue.svg"))
    return [t["t"] for t in texts if 1903 <= t["y"] <= 1960 and t["x"] == 65.0]
log("   clinic intro W43:", clinic_intro_w(W43), " ED:", clinic_intro_w(ED))
# deviation 3: shortened strings widths
for s in ["En casa", "El sombrero", "Domingo", "Muy reñido", "Papeleta", "El mandato"]:
    found = [(fn, t) for fn in ed_pages for t in ed_pages[fn] if s in t["t"]]
    for fn, t in found[:2]:
        f = font_for(t["fam"], t["bold"], t["size"]); w = f.getlength(t["t"]) / 4.0
        log(f"   shortened-string width: {s!r} in {fn} full-line={t['t'][:60]!r} size={t['size']} width={w:.1f} (box 434)")
dark = [t for t in ed_pages["p1-front.svg"] if t["x"] == 1855.0]
for t in dark:
    f = font_for(t["fam"], t["bold"], t["size"]); w = f.getlength(t["t"]) / 4.0
    log(f"   P1 dark-band right line: {t['t']!r} width={w:.1f}")
wordbox = [t for t in ed_pages["p1-front.svg"] if "midterm election" in t["t"]]
for t in wordbox:
    f = font_for(t["fam"], t["bold"], t["size"]); w = f.getlength(t["t"]) / 4.0
    log(f"   P1 word-box line: {t['t']!r} width={w:.1f}")
# deviation 4: P8 Levels line + gold line
for label, d in [("CORE", CORE), ("ED", ED)]:
    texts, _, src = parse(os.path.join(d, "p8-exercices.svg"))
    lv = [t for t in texts if t["t"].startswith("Levels") or "LEVEL" in t["t"][:10]]
    lines = [(float(m.group(1)), float(m.group(2))) for m in re.finditer(r'<line x1="[\d.]+" y1="([\d.]+)" x2="[\d.]+" y2="([\d.]+)"', src)]
    log(f"   P8 Levels-ish {label}: {[(t['x'], t['y'], t['t'][:60]) for t in lv]} gold-ish lines y~1486: {[y for y in lines if 1470 <= y[0] <= 1500]}")
# deviation 5: AND YOU box
texts, rects, _ = parse(os.path.join(ED, "p2-life.svg"))
ay = [r for r in rects if r["x"] == 1451.0 and abs(r["y"] - 1225.25) < 1]
log("   AND YOU box rect ED:", ay, "bottom:", ay[0]["y"] + ay[0]["h"] if ay else None)
inside = [t for t in texts if ay and ay[0]["x"] <= t["x"] <= ay[0]["x"] + ay[0]["w"] and ay[0]["y"] <= t["y"] <= ay[0]["y"] + ay[0]["h"]]
log("   AND YOU texts inside rect:", [(t["y"], t["t"][:45]) for t in inside])
after = [t for t in texts if t["x"] >= 1451.0 and t["y"] > (ay[0]["y"] + ay[0]["h"] if ay else 0)]
log("   next col4 texts below AND YOU box:", [(t["y"], t["t"][:45]) for t in after[:3]])

# ---------- 10. P3 quirk ----------
for label, d in [("CORE", CORE), ("ED", ED)]:
    texts, _, _ = parse(os.path.join(d, "p3-culture.svg"))
    idx = next((i for i, t in enumerate(texts) if "THE WORDS" in t["t"]), None)
    log(f"== 10. P3 quirk {label}: header={texts[idx] if idx is not None else None}")
    if idx is not None:
        log(f"    following 4 texts: {[(t['x'], t['y'], t['t'][:50]) for t in texts[idx+1:idx+5]]}")
        log(f"    occlusion flags for P3 handled in occlusion run (see occlusion-ed.json)")

# ---------- 11. images + credits ----------
def images(d):
    out = {}
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".svg"): continue
        src = open(os.path.join(d, fn), encoding="utf-8").read()
        ims = []
        for m in re.finditer(r'<image x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*href="data:image/[^;]+;base64,([^"]+)"', src):
            ims.append((m.group(1), m.group(2), m.group(3), m.group(4), hashlib.sha256(m.group(5).encode()).hexdigest()[:16], len(m.group(5))))
        out[fn] = ims
    return out
im_ed, im_co = images(ED), images(CORE)
for fn in sorted(im_ed):
    log(f"== 11. image {fn}: ED={im_ed[fn]} CORE={im_co[fn]} equal={im_ed[fn]==im_co[fn]}")
for label, d in [("CORE", CORE), ("ED", ED)]:
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".svg"):
            texts, _, _ = parse(os.path.join(d, fn))
            cred = [t["t"] for t in texts if ("Commons" in t["t"] or "Wikimedia" in t["t"] or "©" in t["t"])]
            if cred: log(f"   credit {label} {fn}: {cred}")

# ---------- 12. ABSTRACT + PDFs ----------
ab = open(os.path.join(BASE, "files/weekly-report-w45-en-es/ABSTRACT.txt"), encoding="utf-8").read()
log("== 12. ABSTRACT lines:", ab.count("\n"), "raw:", repr(ab))
log("   ASCII double-quote count:", ab.count('"'), "single-line (strip):", len(ab.strip().splitlines()) == 1)
for kw in ["The Lucerna", "inglés", "hispanohablantes", "3 de noviembre", "1 de noviembre", "Halloween", "Madrid", "A2", "B2", "150 ejercicios", "aprende inglés leyendo noticias reales"]:
    log(f"   ABSTRACT keyword {kw!r}: {'OK' if kw in ab else 'MISSING'}")
from pypdf import PdfReader
for fn in ["The-Lucerna-VOL2-ES.pdf", "The-Lucerna-VOL2-ES-web.pdf"]:
    p = os.path.join(BASE, "files/weekly-report-w45-en-es", fn)
    r = PdfReader(p); h = hashlib.sha256(open(p, "rb").read()).hexdigest()
    log(f"   PDF {fn}: pages={len(r.pages)} bytes={os.path.getsize(p)} sha={h}")
kit = open(os.path.join(BASE, "files/weekly-report-w45-en-es/WEEKLY-KIT.md"), encoding="utf-8").read()
log("   KIT contains print sha:", "382f1e81b1249123b1ca2d28ebb53d825f82c55ece01f822f576e27fd9b733f1" in kit, "web sha:", "6282726a0a79ee6ce72131372e4ccc4c5243015c8e087e9853903dc2b4f23e13" in kit,
    "print bytes 17,292,956:", "17,292,956" in kit, "web bytes 4,004,747:", "4,004,747" in kit)
json.dump(RES, open(os.path.join(OUT, "proof_checks.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False, default=str)
log("DONE")
LOG.close()
