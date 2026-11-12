#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""spill_sweep.py — standing gate: cream-box whole-line spill sweep (W47).

Promoted 2026-11-11 from the core-nl fix5 re-proof script
``hidden_files/w47/scratch-fix-nl5b/spill_sweep_reproof.py`` (unchanged
detection logic; generalised to any edition dir, plus auto-adjudication).

Blind spot it closes (run-log 2026-11-11 ~16:15 UTC): ``check_creambox.py``
only inspects texts whose baseline falls inside a cream rect, so a whole
line sitting entirely OUTSIDE its box is skipped; and the occlusion audit's
BOXTITLE class only counts stroked boxes, so borderless (pure-fill) cream
boxes are invisible to it. This sweep looks at the 60 px neighbourhood of
every cream (``#f0eee5``) rect:

  BELOW — baseline 0..60 px below the box bottom, x-start inside the box
  ABOVE — baseline 0..60 px above the box top, x-start inside the box
  SIDE  — baseline inside the box y-range, x-start 0..60 px outside its
          x-range on either side

Every candidate is adjudicated by the same-flow test (the rule the nl fix5
re-proof used by hand): a candidate is a real SPILL only if it continues
the box's own line flow — same font-size as the box's last (BELOW) / first
(ABOVE) inside line, same x-start (within 1 px), and the vertical gap to
that line matches the expected line advance for that size (within 3 px).
The expected advance is the median gap between consecutive inside lines
of the same size, or, when the box holds only one line of that size, the
nominal advance 1.40 x font-size (measured across all 12 W47 cores and
fan-outs: same-size medians run 1.30–1.45 x size). The box-wide median
advance is deliberately NOT used: in a mixed-size box it mixes title/body
transitions and misstates the advance of any one size (W47 ko-it P2:
a 19 pt gloss wraps at 24.7 px while the box median is 40.0 px, and the
spilled 'kimchi' line was missed). A single-line box's near-above hit is
a table header row, not spilled content (W47 core-ko P6: labels 17 px
above the lower cells, 35 px below the upper cells, same size and column
— deliberately placed headers; their 52 px gap fails the 29.4 px nominal
advance). Next-section headings (+20/+24/+26/+28 px below a box), photo
credits, gloss lines and neighbouring boxes' own titles all fail the
same-flow test and are reported as OBSERVE, never as defects. SIDE hits
are always OBSERVE (a line starting outside the box belongs to another
column; horizontal ink running past a box edge is boxtitle_check.py's
job).

Read-only wrt the edition dir. Writes nothing except the optional JSON
report (--json-dir) and stdout.

Usage:
  python3 tools/spill_sweep.py <edition-dir> [<edition-dir> ...]
      [--json-dir DIR]
Exit 0 iff no SPILL in any edition; exit 1 if any SPILL found.
Requires only the Python 3 standard library.
"""
import collections
import json
import os
import re
import sys
import xml.etree.ElementTree as ET

WINDOW = 60.0       # px neighbourhood around each cream rect
ADV_TOL = 3.0       # px tolerance on the line-advance match
X_TOL = 1.0         # px tolerance on the x-start match
NOMINAL_ADV = 1.40  # x font-size: nominal line advance when a box holds
# only one line of the candidate's size (measured 1.30-1.45 across W47)
NS = "{http://www.w3.org/2000/svg}"


def _num(el, attr, default=None):
    v = el.get(attr)
    if v is None:
        return default
    try:
        return float(v)
    except ValueError:
        return default


def _page_no(fname):
    m = re.match(r"p(\d+)-", fname)
    return int(m.group(1)) if m else None


def _median(vals):
    s = sorted(vals)
    n = len(s)
    if n == 0:
        return None
    return s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2.0


def _flow(inside):
    """inside: [(baseline, size, x, text)] sorted by baseline.
    Returns (modal_x, last_line, first_line)."""
    if not inside:
        return None, None, None
    xs = collections.Counter(round(x, 1) for (_, _, x, _) in inside)
    modal_x = xs.most_common(1)[0][0]
    return modal_x, inside[-1], inside[0]


def _expected_advance(inside, size):
    """Line advance to expect for a line of `size` in this box: the median
    gap between consecutive inside lines of the same size, else the
    nominal advance NOMINAL_ADV x size."""
    gaps = [b[0] - a[0] for a, b in zip(inside, inside[1:])
            if abs(a[1] - size) < 0.01 and abs(b[1] - size) < 0.01
            and b[0] - a[0] > 1.0]
    if gaps:
        return _median(gaps)
    return NOMINAL_ADV * size


def _is_spill(kind, cand, modal_x, ref_line, inside):
    """cand: (baseline, size, x, text). ref_line: last (BELOW) / first
    (ABOVE) inside line. A candidate is a SPILL iff it continues the
    box's own line flow: same font-size and same x-start as the reference
    line, and the vertical gap to it matches the expected advance for
    that size (within ADV_TOL)."""
    if ref_line is None or modal_x is None:
        return False
    cy, csz, cx, _ = cand
    ry, rsz, _, _ = ref_line
    if abs(csz - rsz) > 0.01 or abs(cx - modal_x) > X_TOL:
        return False
    gap = abs(cy - ry)
    return abs(gap - _expected_advance(inside, csz)) <= ADV_TOL


def scan_edition(ed):
    slug = os.path.basename(os.path.normpath(ed))
    svg_dir = os.path.join(ed, "svg")
    files = sorted(f for f in os.listdir(svg_dir) if f.endswith(".svg"))
    result = {"edition": slug, "dir": ed, "pages": {}, "spills": [],
              "observes": [], "boxes": 0, "candidates": 0}
    for i, fn in enumerate(files):
        pg = _page_no(fn) or (i + 1)
        path = os.path.join(svg_dir, fn)
        root = ET.parse(path).getroot()
        rects = []
        for r in root.iter(NS + "rect"):
            if (r.get("fill") or "").lower() == "#f0eee5":
                x, y, w, h = (_num(r, a) for a in ("x", "y", "width", "height"))
                if None not in (x, y, w, h):
                    rects.append((x, y, w, h))
        texts = []
        for t in root.iter(NS + "text"):
            x, y, sz = (_num(t, a) for a in ("x", "y", "font-size"))
            if None in (x, y, sz):
                continue
            txt = "".join(t.itertext())
            if txt.strip():
                texts.append((x, y, sz, txt))
        result["boxes"] += len(rects)
        page_cands = []
        for (rx, ry, rw, rh) in rects:
            bot = ry + rh
            inside = sorted([(y, sz, x, s) for (x, y, sz, s) in texts
                             if rx - 1 <= x <= rx + rw + 1 and ry - 5 <= y <= bot])
            modal_x, last_line, first_line = _flow(inside)
            below = [(y, sz, x, s) for (x, y, sz, s) in texts
                     if rx <= x <= rx + rw and bot < y <= bot + WINDOW]
            above = [(y, sz, x, s) for (x, y, sz, s) in texts
                     if rx <= x <= rx + rw and ry - WINDOW <= y < ry]
            side = [(y, sz, x, s) for (x, y, sz, s) in texts
                    if ry <= y <= bot and (rx - WINDOW <= x < rx
                                           or rx + rw < x <= rx + rw + WINDOW)]
            for kind, cands in (("BELOW", below), ("ABOVE", above),
                                ("SIDE", side)):
                for cand in cands:
                    cy, csz, cx, ctext = cand
                    if kind == "BELOW":
                        dist = cy - bot
                        spill = _is_spill(kind, cand, modal_x, last_line,
                                          inside)
                    elif kind == "ABOVE":
                        dist = cy - ry
                        spill = _is_spill(kind, cand, modal_x, first_line,
                                          inside)
                    else:
                        dist = min(abs(cx - rx), abs(cx - (rx + rw)))
                        spill = False
                    rec = {"page": pg, "kind": kind, "distance": round(dist, 2),
                           "x": round(cx, 1), "y": round(cy, 1),
                           "size": csz, "text": ctext[:80],
                           "box": [round(rx, 1), round(ry, 1),
                                   round(rw, 1), round(rh, 1)],
                           "box_bottom": round(bot, 1),
                           "verdict": "SPILL" if spill else "OBSERVE"}
                    page_cands.append(rec)
                    (result["spills"] if spill else result["observes"]).append(rec)
        result["pages"][str(pg)] = {"file": fn, "boxes": len(rects),
                                    "candidates": page_cands}
        result["candidates"] += len(page_cands)
    return result


def print_edition(res, out=sys.stdout):
    print(f"== {res['edition']}  ({res['dir']})", file=out)
    for pg in sorted(res["pages"], key=lambda p: int(p)):
        info = res["pages"][pg]
        for c in info["candidates"]:
            x, y, w, h = c["box"]
            tag = "SPILL" if c["verdict"] == "SPILL" else "observe"
            if c["kind"] == "BELOW":
                print(f"P{pg} box=({x},{y},{w},{h}) bottom={c['box_bottom']:.1f}",
                      file=out)
                print(f"   BELOW +{c['distance']:.2f}px x={c['x']} y={c['y']} "
                      f"[{tag}] {c['text'][:60]!r}", file=out)
            elif c["kind"] == "ABOVE":
                print(f"P{pg} box=({x},{y},{w},{h}) bottom={c['box_bottom']:.1f}",
                      file=out)
                print(f"   ABOVE {c['distance']:.2f}px x={c['x']} y={c['y']} "
                      f"[{tag}] {c['text'][:60]!r}", file=out)
            else:
                print(f"P{pg} box=({x},{y},{w},{h}) bottom={c['box_bottom']:.1f}",
                      file=out)
                print(f"   SIDE x={c['x']} y={c['y']} [{tag}] {c['text'][:60]!r}",
                      file=out)
    print(f"SPILL_SWEEP {res['edition']}: {res['boxes']} boxes, "
          f"{res['candidates']} candidates, {len(res['spills'])} SPILL, "
          f"{len(res['observes'])} OBSERVE", file=out)


def main(argv):
    args, json_dir = [], None
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--json-dir" and i + 1 < len(argv):
            json_dir = argv[i + 1]
            i += 2
        elif a.startswith("--"):
            print(f"unknown option: {a}", file=sys.stderr)
            return 2
        else:
            args.append(a)
            i += 1
    if not args:
        print("usage: spill_sweep.py <edition-dir> [...] [--json-dir DIR]",
              file=sys.stderr)
        return 2
    if json_dir:
        os.makedirs(json_dir, exist_ok=True)
    rc = 0
    for ed in args:
        res = scan_edition(ed)
        print_edition(res)
        if json_dir:
            with open(os.path.join(json_dir, res["edition"] + ".json"),
                      "w", encoding="utf-8") as f:
                json.dump(res, f, ensure_ascii=False, indent=1)
        if res["spills"]:
            rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
