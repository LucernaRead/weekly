# -*- coding: utf-8 -*-
"""Supplementary gates for KOxES W45 (venv PIL):
- ADVANCE full-page right-edge scan (inner frame x=1910)
- frame-line scan: text ink vs every rect border / line element
  (footer rule y=2580 vs footer baseline 2624 exempt by design)
- same-baseline scan (0.6px tolerance, ink-interval overlap)
- P6 table-label coverage vs later-drawn rects, TRUE ink with
  getmetrics baseline-anchored boxes (gate <30%)
Run: venv/bin/python audit_extra.py <edition-dir> [core-dir]
"""
import sys, os, re, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import _font, text_w
from PIL import ImageFont

ED = sys.argv[1]
CORE = sys.argv[2] if len(sys.argv) > 2 else None

def parse_svg(path):
    s = open(path, encoding="utf-8").read()
    texts = []
    for m in re.finditer(r'<text x="([^"]+)" y="([^"]+)" font-family="([^"]+)" font-size="([^"]+)"[^>]*?(?: font-weight="700")?[^>]*>([^<]*)</text>', s):
        x, y, fam, size, t = float(m.group(1)), float(m.group(2)), m.group(3), float(m.group(4)), m.group(5)
        bold = 'font-weight="700"' in m.group(0)
        anchor_end = 'text-anchor="end"' in m.group(0)
        anchor_mid = 'text-anchor="middle"' in m.group(0)
        texts.append(dict(x=x, y=y, fam=fam, size=size, t=t, bold=bold, end=anchor_end, mid=anchor_mid))
    rects = []
    for m in re.finditer(r'<rect x="([^"]+)" y="([^"]+)" width="([^"]+)" height="([^"]+)"', s):
        rects.append(tuple(float(v) for v in m.groups()))
    lines = []
    for m in re.finditer(r'<line x1="([^"]+)" y1="([^"]+)" x2="([^"]+)" y2="([^"]+)"[^>]*stroke-width="([^"]+)"', s):
        lines.append(tuple(float(v) for v in m.groups()))
    return texts, rects, lines, s

def ink_box(t):
    """Baseline-anchored TRUE ink box: PIL getbbox at 4x, anchored so the
    font baseline sits on y (getmetrics ascent). Returns (x0,y0,x1,y1)."""
    kind = "serif" if "Serif" in t["fam"] else "sans"
    f = _font(kind, t["bold"], t["size"] * 4)
    bb = f.getbbox(t["t"])
    asc, _desc = f.getmetrics()
    w = text_w(t["t"], kind, t["bold"], t["size"])
    if t["end"]:
        x0 = t["x"] - w
    elif t["mid"]:
        x0 = t["x"] - w / 2
    else:
        x0 = t["x"]
    # getbbox is relative to the draw origin at (0,0) with baseline at asc/4 in
    # original units: ink top = y - asc/4 + bb[1]/4 ; ink bottom = y - asc/4 + bb[3]/4
    y0 = t["y"] - asc / 4 + bb[1] / 4
    y1 = t["y"] - asc / 4 + bb[3] / 4
    return (x0 + bb[0] / 4, y0, x0 + bb[2] / 4, y1)

def run_dir(d):
    out = {}
    for path in sorted(glob.glob(os.path.join(d, "svg", "*.svg"))):
        pg = os.path.basename(path)
        texts, rects, lines, s = parse_svg(path)
        boxes = [(t, ink_box(t)) for t in texts]
        # right edge (advance width, superset of ink)
        edge = []
        for t in texts:
            kind = "serif" if "Serif" in t["fam"] else "sans"
            w = text_w(t["t"], kind, t["bold"], t["size"])
            x1 = t["x"] + w if not t["end"] else t["x"]
            if t["mid"]:
                x1 = t["x"] + w / 2
            if x1 > 1910:
                edge.append((t["t"][:40], round(x1, 1)))
        # frame-line scan: ink vs rect borders + line elements
        frame = []
        for t, b in boxes:
            if t["y"] == 2624:
                continue  # footer text, rule at 2580 exempt by design
            for (rx, ry, rw, rh) in rects:
                for bx0, by0, bx1, by1 in [(rx, ry, rx + rw, ry), (rx, ry + rh, rx + rw, ry + rh),
                                            (rx, ry, rx, ry + rh), (rx + rw, ry, rx + rw, ry + rh)]:
                    if b[0] < bx1 and b[2] > bx0 and b[1] < by1 + 0.6 and b[3] > by0 - 0.6:
                        # only flag if the border line actually passes through ink vertically/horizontally
                        if (by0 == by1 and b[1] < by0 < b[3]) or (bx0 == bx1 and b[0] < bx0 < b[2]):
                            frame.append((t["t"][:40], (rx, ry, rw, rh)))
                            break
            for (x1, y1, x2, y2, sw) in lines:
                if y1 == 2580:
                    continue
                if y1 == y2 and b[1] < y1 < b[3] and b[0] < max(x1, x2) and b[2] > min(x1, x2):
                    frame.append((t["t"][:40], ("hline", y1)))
        # same-baseline scan
        same = []
        by_y = {}
        for t, b in boxes:
            by_y.setdefault(round(t["y"], 1), []).append((t, b))
        for y, items in by_y.items():
            items.sort(key=lambda tb: tb[1][0])
            for (t1, b1), (t2, b2) in zip(items, items[1:]):
                if abs(t1["y"] - t2["y"]) <= 0.6 and b1[2] > b2[0] and b1[3] > b2[1] and b1[1] < b2[3]:
                    same.append((round(y, 1), t1["t"][:30], t2["t"][:30]))
        out[pg] = dict(edge=edge, frame=frame, same=same, texts=texts, boxes=boxes, s=s)
    return out

def p6_coverage(res):
    """P6 comparison-table labels vs later-drawn rects (paint order):
    labels are the table cell texts; coverage = ink area overlapped by
    any rect drawn AFTER the label, / label ink area. Gate <30%."""
    pg = "p6-gipi.svg"
    if pg not in res:
        return None
    s = res[pg]["s"]
    # paint order: split elements in document order
    elems = re.findall(r'<(?:text|rect)[^>]*>', s)
    # table label texts (the 12 cells) are identified by their content
    labels = ["구분", "이번 주 (11월 2~8일)", "시험 날 (11월 19일)", "날짜 세기",
              "D-17 ~ D-12", "D-데이", "분위기", "카운트다운", "시험 당일",
              "특별 조치", "없어요 (평상시)", "있어요 (10시 출근 등)"]
    # find each label's element index and its ink box via parse
    texts = res[pg]["texts"]
    boxes = dict()
    for t, b in res[pg]["boxes"]:
        boxes.setdefault(t["t"], []).append(b)
    rects_after = []
    # document-order rect list with positions
    rect_iter = list(re.finditer(r'<rect x="([^"]+)" y="([^"]+)" width="([^"]+)" height="([^"]+)"', s))
    text_iter = list(re.finditer(r'<text x="([^"]+)" y="([^"]+)"[^>]*>([^<]*)</text>', s))
    out = {}
    for lab in labels:
        # first occurrence of this label text
        ti = next((i for i, m in enumerate(text_iter) if m.group(3) == lab), None)
        if ti is None:
            out[lab] = "NOT-FOUND"
            continue
        # ink box for that occurrence (match by order among same-text nodes)
        occ = [m for m in text_iter if m.group(3) == lab].index(text_iter[ti])
        b = boxes[lab][occ]
        # rects drawn after this text element: compare raw positions in s
        tpos = text_iter[ti].start()
        cov = 0.0
        area = max((b[2] - b[0]) * (b[3] - b[1]), 1e-9)
        for rm in rect_iter:
            if rm.start() > tpos:
                rx, ry, rw, rh = (float(v) for v in rm.groups())
                ix = max(0, min(b[2], rx + rw) - max(b[0], rx))
                iy = max(0, min(b[3], ry + rh) - max(b[1], ry))
                cov += ix * iy
        out[lab] = round(100 * cov / area, 1)
    return out

for label, d in [("EDITION", ED)] + ([("CORE", CORE)] if CORE else []):
    res = run_dir(d)
    print(f"===== {label} {d}")
    for pg, r in res.items():
        print(f"{pg}: right-edge={len(r['edge'])} frame={len(r['frame'])} same-baseline={len(r['same'])}")
        for e in r["edge"][:5]:
            print("   EDGE", e)
        for e in r["frame"][:5]:
            print("   FRAME", e)
        for e in r["same"][:5]:
            print("   SAME", e)
    cov = p6_coverage(res)
    print("P6 label coverage % (gate <30):", cov)
