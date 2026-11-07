# -*- coding: utf-8 -*-
"""Supplementary scans for the KO x DE edition (run with tools venv python).

1. ADVANCE right-edge scan: every SVG text node's advance end vs the inner
   frame (x=1910) and page edge, using the build's own advance metric
   (svglib text_w, KR face).
2. Frame-line scan: every text ink box (canonical audit ink_box, 4x
   supersampled, baseline-anchored) vs every rect border / line element
   in the same page. (Canonical audit's BOXTITLE covers only box titles;
   this covers body text vs box borders.)
3. Same-baseline scan: text nodes sharing a baseline (within 0.6px) whose
   ink intervals overlap.
4. P6 table-label coverage: per-label ink fraction covered by later-drawn
   rects on P6 (baseline-anchored true ink, reported for every label;
   gate <30%, not just the audit's >=30% COVER flag).
5. Korean orphan scan: driven by wrap-spy.log (see spy_wrap.py, run in a
   scratch copy): line-start NO_START on post-kinsoku lines, and
   mid-word breaks with >=3-syllable tails on pre-kinsoku lines.
Usage: audit_extra.py <edition-svg-dir> <wrap-spy-log>
"""
import html, json, os, re, sys
from collections import defaultdict

TOOLS = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools")
sys.path.insert(0, TOOLS)
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-ko-build"))
import occlusion_audit as OA
from svglib import text_w

NO_START = "。、，．！？：；）」』】ー…‥・)]}〉》.,!?%:;"
HANGUL = re.compile(r"[\uac00-\ud7a3]")

TEXT_RE = re.compile(r'<text[^>]*x="([\d.]+)" y="([\d.]+)"[^>]*font-size="([\d.]+)"([^>]*)>(.*?)</text>')
RECT_RE = re.compile(r'<rect[^>]*x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"([^>]*)>')
LINE_RE = re.compile(r'<line[^>]*x1="([\d.]+)" y1="([\d.]+)" x2="([\d.]+)" y2="([\d.]+)"[^>]*stroke-width="([\d.]+)"')


def parse_page(path):
    s = open(path, encoding="utf-8").read()
    texts = []
    for m in TEXT_RE.finditer(s):
        x, y, size = float(m.group(1)), float(m.group(2)), float(m.group(3))
        rest = m.group(4)
        fam = re.search(r'font-family="([^"]+)"', rest)
        bold = 'font-weight="700"' in rest
        anchor = re.search(r'text-anchor="([^"]+)"', rest)
        t = html.unescape(re.sub(r"<[^>]+>", "", m.group(5)))
        texts.append({"x": x, "y": y, "size": size, "bold": bold,
                      "family": fam.group(1) if fam else "",
                      "anchor": anchor.group(1) if anchor else "start",
                      "text": t})
    rects = []
    for m in RECT_RE.finditer(s):
        x, y, w, h = (float(m.group(i)) for i in (1, 2, 3, 4))
        rest = m.group(5)
        sw = re.search(r'stroke-width="([\d.]+)"', rest)
        if "stroke=" in rest and w > 0 and h > 0:
            rects.append({"x": x, "y": y, "w": w, "h": h,
                          "sw": float(sw.group(1)) if sw else 1.2})
    lines = []
    for m in LINE_RE.finditer(s):
        lines.append({"x1": float(m.group(1)), "y1": float(m.group(2)),
                      "x2": float(m.group(3)), "y2": float(m.group(4)),
                      "sw": float(m.group(5))})
    return texts, rects, lines


def adv_interval(t):
    """Advance x-interval for a text node, honouring its anchor."""
    w = text_w(t["text"], "serif" if "Serif" in t["family"] else "sans",
               t["bold"], t["size"])
    if t["anchor"] == "middle":
        return (t["x"] - w / 2, t["x"] + w / 2)
    if t["anchor"] == "end":
        return (t["x"] - w, t["x"])
    return (t["x"], t["x"] + w)


def main():
    svgdir, spylog = sys.argv[1], sys.argv[2]
    print("== 1. ADVANCE right-edge scan (inner frame 1910, page 1950) ==")
    edge_flags = 0
    for fn in sorted(os.listdir(svgdir)):
        if not fn.endswith(".svg"):
            continue
        texts, _, _ = parse_page(os.path.join(svgdir, fn))
        for t in texts:
            a, b = adv_interval(t)
            if b > 1910 or a < 40:
                print(f"  EDGE {fn} y={t['y']} adv=({a:.1f},{b:.1f}) {t['text'][:50]!r}")
                edge_flags += 1
    print(f"  advance edge flags: {edge_flags}")

    print("== 2. Frame-line scan (ink vs rect borders + lines) ==")
    frame_flags = 0
    for fn in sorted(os.listdir(svgdir)):
        if not fn.endswith(".svg"):
            continue
        texts, rects, lines = parse_page(os.path.join(svgdir, fn))
        for t in texts:
            ib = OA.ink_box(t["text"], t["family"], t["size"], t["bold"],
                            t["x"], t["y"], t["anchor"])
            if ib is None:
                continue
            l, tp, r, b = ib
            for rc in rects:
                sw2 = rc["sw"] / 2 + 0.5
                # border crossing: ink straddles one of the 4 edges
                cx = ((l < rc["x"] + sw2 and r > rc["x"] - sw2) or
                      (l < rc["x"] + rc["w"] + sw2 and r > rc["x"] + rc["w"] - sw2))
                cy = ((tp < rc["y"] + sw2 and b > rc["y"] - sw2) or
                      (tp < rc["y"] + rc["h"] + sw2 and b > rc["y"] + rc["h"] - sw2))
                in_y = not (b < rc["y"] or tp > rc["y"] + rc["h"])
                in_x = not (r < rc["x"] or l > rc["x"] + rc["w"])
                if (cx and in_y) or (cy and in_x):
                    print(f"  FRAME {fn} y={t['y']} ink=({l:.1f},{tp:.1f},{r:.1f},{b:.1f}) "
                          f"rect=({rc['x']},{rc['y']},{rc['w']},{rc['h']}) {t['text'][:40]!r}")
                    frame_flags += 1
            for ln in lines:
                if ln["y1"] == ln["y2"]:  # horizontal rule
                    sw2 = ln["sw"] / 2 + 0.5
                    if tp - sw2 <= ln["y1"] <= b + sw2 and not (r < ln["x1"] or l > ln["x2"]):
                        # footer rule vs footer text is exempt by design (ink
                        # below the rule); section rules sit below head ink
                        if ln["y1"] == 2580 and t["y"] == 2624:
                            continue
                        print(f"  LINECROSS {fn} y={t['y']} rule_y={ln['y1']} {t['text'][:40]!r}")
                        frame_flags += 1
    print(f"  frame-line flags: {frame_flags}")

    print("== 3. Same-baseline scan (ink overlap, tolerance 0.6px) ==")
    base_flags = 0
    for fn in sorted(os.listdir(svgdir)):
        if not fn.endswith(".svg"):
            continue
        texts, _, _ = parse_page(os.path.join(svgdir, fn))
        groups = defaultdict(list)
        for t in texts:
            groups[round(t["y"] / 0.6)].append(t)
        for _, g in groups.items():
            if len(g) < 2:
                continue
            boxes = []
            for t in g:
                ib = OA.ink_box(t["text"], t["family"], t["size"], t["bold"],
                                t["x"], t["y"], t["anchor"])
                if ib:
                    boxes.append((ib[0], ib[2], t))
            boxes.sort()
            for (l1, r1, t1), (l2, r2, t2) in zip(boxes, boxes[1:]):
                if l2 < r1 - 0.5:
                    print(f"  BASE {fn} y={t1['y']} overlap {r1 - l2:.1f}px "
                          f"{t1['text'][:30]!r} vs {t2['text'][:30]!r}")
                    base_flags += 1
    print(f"  same-baseline flags: {base_flags}")

    print("== 4. P6 table-label coverage (later rects, true ink) ==")
    p6 = os.path.join(svgdir, "p6-gipi.svg")
    s = open(p6, encoding="utf-8").read()
    # Re-parse in paint order: walk elements sequentially.
    els = []
    for m in re.finditer(r'<(rect|text)[^>]*?(?:/>|>(.*?)</text>)', s):
        tag = m.group(0)
        if tag.startswith("<rect"):
            mm = re.search(r'x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"', tag)
            fill = re.search(r'fill="([^"]+)"', tag)
            if mm and fill and fill.group(1) not in ("none",):
                els.append(("rect", float(mm.group(1)), float(mm.group(2)),
                            float(mm.group(3)), float(mm.group(4))))
        else:
            mm = re.search(r'x="([\d.]+)" y="([\d.]+)"[^>]*font-size="([\d.]+)"([^>]*)>(.*?)</text>', tag)
            if mm:
                fam = re.search(r'font-family="([^"]+)"', mm.group(4))
                bold = 'font-weight="700"' in mm.group(4)
                t = html.unescape(re.sub(r"<[^>]+>", "", mm.group(5)))
                els.append(("text", float(mm.group(1)), float(mm.group(2)),
                            float(mm.group(3)), fam.group(1) if fam else "",
                            bold, t))
    worst = 0.0
    for i, el in enumerate(els):
        if el[0] != "text":
            continue
        _, x, y, size, fam, bold, t = el
        # table region: rows y 1245..1470, cols x 65..1453
        if not (1240 <= y <= 1470 and 65 <= x <= 1453):
            continue
        ib = OA.ink_box(t, fam, size, bold, x, y, "start")
        if ib is None:
            continue
        l, tp, r, b = ib
        area = max(0.0, (r - l) * (b - tp))
        cov = 0.0
        for el2 in els[i + 1:]:
            if el2[0] != "rect":
                continue
            _, rx, ry, rw, rh = el2
            ox = max(0.0, min(r, rx + rw) - max(l, rx))
            oy = max(0.0, min(b, ry + rh) - max(tp, ry))
            if area:
                cov = max(cov, ox * oy / area)
        worst = max(worst, cov)
        print(f"  P6 label y={y} cov={cov * 100:.1f}% {t[:40]!r}")
    print(f"  P6 worst label coverage: {worst * 100:.1f}% (gate <30%)")

    print("== 5. Korean orphan scan (wrap-spy) ==")
    seen = set()
    start_flags, split_flags, split_info = [], [], []
    for line in open(spylog, encoding="utf-8"):
        rec = json.loads(line)
        key = (rec["text"], rec["size"], rec["max_w"])
        if key in seen:
            continue
        seen.add(key)
        pre, post = rec["pre"], rec["post"]
        for ln in post:
            if ln and ln[0] in NO_START and HANGUL.search(ln):
                start_flags.append((rec["text"][:30], ln))
        # walk pre-kinsoku lines against source text
        pos = 0
        src = rec["text"]
        for j, ln in enumerate(pre):
            seg = ln.rstrip()
            if src[pos:pos + len(seg)] == seg:
                pos += len(seg)
            else:
                # try skipping one space (word-boundary break already consumed)
                if src[pos:pos + 1] == " " and src[pos + 1:pos + 1 + len(seg)] == seg:
                    pos += 1 + len(seg)
                else:
                    break  # kinsoku-distorted or non-prose; stop this record
            if j + 1 < len(pre):
                if pos < len(src) and src[pos] == " ":
                    pos += 1  # word-boundary break
                elif pos < len(src):
                    # mid-word break: tail = syllables to next space
                    tail = []
                    k = pos
                    while k < len(src) and src[k] != " ":
                        tail.append(src[k])
                        k += 1
                    nsyl = len(HANGUL.findall("".join(tail)))
                    entry = (nsyl, "".join(tail)[:20], src[max(0, pos - 8):pos + 12])
                    if nsyl >= 3:
                        split_flags.append(entry)
                    else:
                        split_info.append(entry)
    print(f"  line-start NO_START flags (Korean lines): {len(start_flags)}")
    for f in start_flags[:20]:
        print("   START", f)
    print(f"  mid-word splits tail>=3 syllables: {len(split_flags)}")
    for f in split_flags[:20]:
        print("   SPLIT>=3", f)
    print(f"  mid-word splits tail 1-2 syllables (info): {len(split_info)}")
    for f in split_info[:20]:
        print("   split-info", f)


if __name__ == "__main__":
    main()
