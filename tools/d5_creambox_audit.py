#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""d5_creambox_audit.py — D5 standing gate: cream-box differential audit.

Promoted 2026-11-12 from
``hidden_files/w47/scratch-d5-plan/mechanism/d5_creambox_audit.py``
(unchanged detection logic; see the Validation note below). The one
addition is an old-style-baseline fallback in ``ink_bbox``: ja/ko-target
editions (and the shipped W43/W45/W46 generations) still ship the
old-style single-font svglib with no ``_runs``/``_pil`` split, so the
pre-fix side of a differential audit cannot be measured through the
new-style API. When the loaded module has no ``_runs``/``_pil``, the
audit measures the whole string with that module's ``_font`` — which is
exactly the face the old-style renderer used. ``--selftest`` exercises
both paths on synthetic fixtures under tools/scratch/.

Converged (2026-11-11) from the pt-fr D5 pilot's analyze.py (same ink math,
same #f0eee5 rect rule, same thresholds), generalised to any edition pair:
  python3 d5_creambox_audit.py <baseline-edition-dir> <patched-edition-dir>
      [--json out.json]
Exit 0 iff no DEFECT; exit 1 if any DEFECT; exit 2 on usage/blocked input.
Run with tools/venv/bin/python (PIL + fontTools via the edition's svglib).

Why this gate exists (pilot PILOT-NOTE.md §4): the D5 font change widens
bold caps box titles in Newsreader SemiBold (bold median +5.7%, `A2`
+18.4%), pushing the trailing reader-language subtitle out of its cream
box. gates.py 16/16 stayed green on 5 of the 6 such defects and the
occlusion audit caught only 1 (a true collision, P2 TEXTX). This audit
catches the other 5: for every cream (#f0eee5) rect, it measures the PIL
true-ink bbox of every text element whose baseline sits inside the box
and flags ink running past any box edge by > 2.0 px.

Gate semantics (adjudication vs the pre-fix baseline):
  * A patched abs-overflow is a DEFECT iff the same box had no
    baseline overflow on the same side at equal-or-greater severity
    (within 2.0 px). Equal severity in the baseline = OBSERVE
    (pre-existing, not caused by the font change).
  * A line that sat inside a box in the baseline and sits below the box
    in the patched build ("spilled below box") is a DEFECT.
  * "line vanished/rewrapped" diff flags are INFORMATIONAL (reflow is
    expected: ~2.8% of lines re-break under D5) and never fail the gate.
  * Defect #1-class (title ink colliding with a neighbour column's text
    while staying inside its own box) is NOT covered here — the occlusion
    audit owns it. This gate + occlusion + boxtitle_check + spill_sweep
    together cover the pilot's 6/6.

Also reported (non-gating, same as the pilot): per-page element/family/
character counts, line reflow counts, element movement, max right ink,
advance ratios of every distinct sans string (baseline vs patched
text_w, split by bold), and P8 slack (last baseline, max ink bottom,
distance to the footer rule at y=2596 and to the page bottom at 2700).
Read-only wrt both edition dirs; writes only --json + stdout.
"""
import argparse
import html
import importlib.util
import json
import os
import re
import sys
from collections import Counter

TEXT_RE = re.compile(
    r'<text x="([^"]+)" y="([^"]+)" font-family="([^"]+)" font-size="([^"]+)"([^>]*)>([^<]*)</text>')
RECT_RE = re.compile(
    r'<rect x="([^"]+)" y="([^"]+)" width="([^"]+)" height="([^"]+)"[^>]*fill="(#[0-9a-f]{6})"')
FOOTER_RULE_Y = 2596.0
PAGE_BOTTOM_Y = 2700.0
OVER_TOL = 2.0


def load_svgmod(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def texts(path):
    t = open(path, encoding="utf-8").read()
    els = []
    for m in TEXT_RE.finditer(t):
        x, y, fam, size, rest, s = (float(m.group(1)), float(m.group(2)),
                                    m.group(3), float(m.group(4)), m.group(5),
                                    html.unescape(m.group(6)))
        els.append({"x": x, "y": y, "fam": fam, "size": size,
                    "bold": "700" in rest, "s": s})
    return els


def rects(path, fill="#f0eee5"):
    t = open(path, encoding="utf-8").read()
    out = []
    for m in RECT_RE.finditer(t):
        x, y, w, h, f = (float(m.group(1)), float(m.group(2)), float(m.group(3)),
                         float(m.group(4)), m.group(5))
        if f.lower() == fill.lower():
            out.append({"x": x, "y": y, "w": w, "h": h})
    return out


def kind_of(fam):
    if "Serif" in fam or "Newsreader" in fam:
        return "serif"
    if "Sans" in fam:
        return "sans"
    return "other"


def ink_bbox(el, svglib):
    if kind_of(el["fam"]) == "other" or not el["s"].strip():
        return None
    kind = kind_of(el["fam"])
    if not (hasattr(svglib, "_runs") and hasattr(svglib, "_pil")):
        # Old-style svglib (core-ja/core-ko generation; shipped W43/W45/
        # W46): one face per (kind, bold); the whole string renders in
        # that face, so a single getbbox is the faithful ink box.
        f = svglib._font(kind, el["bold"], el["size"])
        bx0, by0, bx1, by1 = f.getbbox(el["s"], anchor="ls")
        return (el["x"] + bx0, el["y"] + by0, el["x"] + bx1, el["y"] + by1)
    boxes, cx = [], el["x"]
    for t, cls in svglib._runs(el["s"], kind, el["bold"]):
        f = svglib._pil(kind, el["bold"], cls, el["size"])
        bx0, by0, bx1, by1 = f.getbbox(t, anchor="ls")
        boxes.append((cx + bx0, el["y"] + by0, cx + bx1, el["y"] + by1))
        cx += f.getlength(t)
    return (min(b[0] for b in boxes), min(b[1] for b in boxes),
            max(b[2] for b in boxes), max(b[3] for b in boxes))


def lines_of(els):
    ys = sorted({round(e["y"], 1) for e in els})
    clusters, cur = [], []
    for y in ys:
        if cur and y - cur[-1] > 1.0:
            clusters.append(cur)
            cur = []
        cur.append(y)
    if cur:
        clusters.append(cur)
    lines = []
    for cl in clusters:
        members = [e for e in els if round(e["y"], 1) in cl]
        members.sort(key=lambda e: e["x"])
        lines.append({"y": sum(cl) / len(cl),
                      "s": "".join(e["s"] for e in members)})
    return lines


def abs_flags(els, boxes, svglib):
    out = []
    for e in els:
        b = ink_bbox(e, svglib)
        if not b:
            continue
        for bi, bx in enumerate(boxes):
            if bx["x"] <= e["x"] <= bx["x"] + bx["w"] and bx["y"] <= e["y"] <= bx["y"] + bx["h"]:
                ov = {"left": round(bx["x"] - b[0], 1), "right": round(b[2] - (bx["x"] + bx["w"]), 1),
                      "top": round(bx["y"] - b[1], 1), "bottom": round(b[3] - (bx["y"] + bx["h"]), 1)}
                bad = {k: v for k, v in ov.items() if v > OVER_TOL}
                if bad:
                    out.append({"box": bi, "s": e["s"][:60], "y": e["y"], "over": bad})
    return out


def p8_stats(els, svglib):
    flow = [e for e in els if e["y"] < FOOTER_RULE_Y]
    last = sorted(flow, key=lambda e: e["y"])[-6:]
    maxb = None
    for e in flow:
        b = ink_bbox(e, svglib)
        if b and (maxb is None or b[3] > maxb):
            maxb = b[3]
    return {"n_flow_elements": len(flow),
            "last_baselines": [round(e["y"], 1) for e in last],
            "last_strings": [e["s"][:40] for e in last],
            "max_ink_bottom": round(maxb, 1) if maxb else None,
            "slack_to_footer_rule_2596": round(FOOTER_RULE_Y - maxb, 1) if maxb else None,
            "slack_to_page_bottom_2700": round(PAGE_BOTTOM_Y - maxb, 1) if maxb else None}


def audit_page(base_svg, patch_svg, s_base, s_patch):
    b_els, p_els = texts(base_svg), texts(patch_svg)
    fam_b = Counter(e["fam"] for e in b_els)
    fam_p = Counter(e["fam"] for e in p_els)
    chars_b, chars_p = Counter(), Counter()
    for e in b_els:
        chars_b[e["fam"]] += len(e["s"])
    for e in p_els:
        chars_p[e["fam"]] += len(e["s"])
    bl, pl = lines_of(b_els), lines_of(p_els)
    same = diff = 0
    changed = []
    for i in range(max(len(bl), len(pl))):
        bs = bl[i]["s"] if i < len(bl) else None
        ps = pl[i]["s"] if i < len(pl) else None
        if bs == ps:
            same += 1
        else:
            diff += 1
            changed.append({"i": i, "y_base": bl[i]["y"] if i < len(bl) else None,
                            "y_patch": pl[i]["y"] if i < len(pl) else None,
                            "base": bs, "patch": ps})
    boxes = rects(patch_svg)
    boxes_b = rects(base_svg)
    assert len(boxes) == len(boxes_b), \
        f"box count changed: base {len(boxes_b)} vs patch {len(boxes)}"
    abs_b = abs_flags(b_els, boxes_b, s_base)
    abs_p = abs_flags(p_els, boxes, s_patch)
    # Adjudicate patched flags against baseline flags (same box, same side).
    defects, observes = [], []
    for f in abs_p:
        covered = False
        for g in abs_b:
            if g["box"] != f["box"]:
                continue
            for side, over in f["over"].items():
                if side in g["over"] and g["over"][side] >= over - OVER_TOL:
                    covered = True
        (observes if covered else defects).append(f)
    # Spill check: a patched line is a spill only if it lies below the
    # PATCHED box bottom (boxes[bi]), not the base box bottom. The base box
    # is the right reference for "was inside before", but when D5 reflow moves
    # a whole box down (e.g. it-ru P2 E TU box: base bottom 1379.6, patched
    # bottom 1399.75, line inside with identical 5.6px clearance), comparing
    # against the base bottom flags a false spill. (Fixed 2026-11-12.)
    spill, vanished = [], []
    for bi, bx in enumerate(boxes_b):
        inside_b = []
        for ln in bl:
            mem = [e for e in b_els if abs(e["y"] - ln["y"]) < 0.6]
            if mem and bx["y"] <= ln["y"] <= bx["y"] + bx["h"] and \
               any(bx["x"] <= e["x"] <= bx["x"] + bx["w"] for e in mem):
                inside_b.append(ln["s"])
        for s in inside_b:
            cands = [ln for ln in pl if ln["s"] == s]
            if not cands:
                vanished.append({"box": bi, "s": s[:60], "issue": "line vanished/rewrapped"})
            elif cands[0]["y"] > boxes[bi]["y"] + boxes[bi]["h"]:
                spill.append({"box": bi, "s": s[:60], "issue": "spilled below box",
                              "y_base": round([ln for ln in bl if ln["s"] == s][0]["y"], 1),
                              "y_patch": round(cands[0]["y"], 1),
                              "box_bottom": round(boxes[bi]["y"] + boxes[bi]["h"], 1)})
    # Element movement (greedy match by text/size/bold, doc order).
    def key(e):
        return (e["s"], e["size"], e["bold"])
    b_by_key, p_by_key = {}, {}
    for e in b_els:
        b_by_key.setdefault(key(e), []).append(e)
    for e in p_els:
        p_by_key.setdefault(key(e), []).append(e)
    moved = []
    for k in set(b_by_key) & set(p_by_key):
        for be, pe in zip(b_by_key[k], p_by_key[k]):
            dx, dy = pe["x"] - be["x"], pe["y"] - be["y"]
            if abs(dx) > 0.5 or abs(dy) > 0.5:
                moved.append({"s": k[0][:40], "dx": round(dx, 1), "dy": round(dy, 1)})
    return {
        "elements_base": len(b_els), "elements_patch": len(p_els),
        "fam_base": dict(fam_b), "fam_patch": dict(fam_p),
        "chars_base": dict(chars_b), "chars_patch": dict(chars_p),
        "lines_base": len(bl), "lines_patch": len(pl),
        "lines_same": same, "lines_diff": diff,
        "moved_elements": len(moved),
        "max_abs_dx": max([abs(m["dx"]) for m in moved], default=0),
        "max_abs_dy": max([abs(m["dy"]) for m in moved], default=0),
        "boxes": len(boxes),
        "creambox_abs_base": abs_b,
        "creambox_defects": defects,
        "creambox_observes": observes,
        "creambox_spill_defects": spill,
        "creambox_vanished_info": vanished,
        "changed_lines_sample": changed[:6],
    }, (b_els, p_els)


def _write_fixture(root, title, shim):
    """One synthetic edition dir: a single page with one cream rect and
    one bold title inside it, plus a shim svglib.py (new- or old-style)."""
    import shutil
    shutil.rmtree(root, ignore_errors=True)
    os.makedirs(os.path.join(root, "svg"))
    page = ('<svg xmlns="http://www.w3.org/2000/svg" width="1950" height="2700">'
            '<rect x="100" y="100" width="300" height="100" fill="#f0eee5"/>'
            '<text x="110" y="150" font-family="Noto Sans CJK SC" font-size="20" '
            f'font-weight="700">{title}</text></svg>')
    open(os.path.join(root, "svg", "p1-test.svg"), "w", encoding="utf-8").write(page)
    open(os.path.join(root, "svglib.py"), "w", encoding="utf-8").write(shim)


_NEW_SHIM = '''from PIL import ImageFont
_CJK = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
_CJK_B = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
_cache = {}
def _face(bold, size):
    key = (bold, size)
    if key not in _cache:
        _cache[key] = ImageFont.truetype(_CJK_B if bold else _CJK, size, index=2)
    return _cache[key]
def _runs(s, kind, bold):
    return [(s, "sans")]
def _pil(kind, bold, cls, size):
    return _face(bold, size)
def text_w(s, kind, bold, size):
    return _face(bold, size).getlength(s)
'''

_OLD_SHIM = '''from PIL import ImageFont
_CJK = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
_CJK_B = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
_cache = {}
def _face(bold, size):
    key = (bold, size)
    if key not in _cache:
        _cache[key] = ImageFont.truetype(_CJK_B if bold else _CJK, size, index=2)
    return _cache[key]
def _font(kind, bold, size):
    return _face(bold, size)
def text_w(s, kind, bold, size):
    return _face(bold, size).getlength(s)
'''


def selftest():
    """Synthetic fixtures under tools/scratch/: a widened title must be
    1 DEFECT, an identical pair 0 defects, and an old-style baseline
    shim must run without error (fallback path) and report 0 defects."""
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "scratch", "d5-creambox-selftest")
    fails = []
    base = os.path.join(root, "base")
    _write_fixture(base, "SHORT TITLE", _NEW_SHIM)
    wide = os.path.join(root, "wide")
    _write_fixture(wide, "A MUCH LONGER BOX TITLE THAT OVERFLOWS", _NEW_SHIM)
    rc = main([base, wide])
    if rc != 1:
        fails.append(f"defect pair: expected exit 1, got {rc}")
    same = os.path.join(root, "same")
    _write_fixture(same, "SHORT TITLE", _NEW_SHIM)
    rc = main([base, same])
    if rc != 0:
        fails.append(f"clean pair: expected exit 0, got {rc}")
    oldbase = os.path.join(root, "oldbase")
    _write_fixture(oldbase, "SHORT TITLE", _OLD_SHIM)
    rc = main([oldbase, same])
    if rc != 0:
        fails.append(f"old-style baseline pair: expected exit 0, got {rc}")
    if fails:
        print("SELFTEST FAILED")
        for x in fails:
            print(" -", x)
        return 1
    print("SELFTEST OK: widened title -> 1 defect; identical pair -> 0; "
          "old-style baseline shim -> 0 (fallback path exercised)")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="D5 cream-box differential audit")
    ap.add_argument("baseline", nargs="?", help="baseline (pre-fix) edition dir")
    ap.add_argument("patched", nargs="?", help="patched (post-fix) edition dir")
    ap.add_argument("--json", dest="json_out", default=None)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)
    if args.selftest:
        return selftest()
    if not args.baseline or not args.patched:
        ap.error("baseline and patched edition dirs are required")
    base_svg_dir = os.path.join(args.baseline, "svg")
    patch_svg_dir = os.path.join(args.patched, "svg")
    for d in (base_svg_dir, patch_svg_dir):
        if not os.path.isdir(d):
            print(f"BLOCKED: no svg/ dir: {d}")
            return 2
    base_pages = sorted(f for f in os.listdir(base_svg_dir) if f.endswith(".svg"))
    patch_pages = sorted(f for f in os.listdir(patch_svg_dir) if f.endswith(".svg"))
    if base_pages != patch_pages:
        print(f"BLOCKED: page sets differ: {base_pages} vs {patch_pages}")
        return 2
    if not base_pages:
        print("BLOCKED: no pages")
        return 2
    s_base = load_svgmod("svglib_base", os.path.join(args.baseline, "svglib.py"))
    s_patch = load_svgmod("svglib_patch", os.path.join(args.patched, "svglib.py"))
    report, tot = {"pages": {}}, Counter()
    all_b_els = {}
    for page in base_pages:
        d, (b_els, p_els) = audit_page(os.path.join(base_svg_dir, page),
                                       os.path.join(patch_svg_dir, page),
                                       s_base, s_patch)
        report["pages"][page] = d
        all_b_els[page] = (b_els, p_els)
        tot["defects"] += len(d["creambox_defects"]) + len(d["creambox_spill_defects"])
        tot["observes"] += len(d["creambox_observes"])
        tot["elements_base"] += d["elements_base"]
        tot["elements_patch"] += d["elements_patch"]
        tot["lines_base"] += d["lines_base"]
        tot["lines_patch"] += d["lines_patch"]
        tot["lines_diff"] += d["lines_diff"]
        tot["moved"] += d["moved_elements"]
    report["totals"] = dict(tot)
    # Advance ratios over distinct sans strings (pilot §3c).
    ratios, seen = [], set()
    for page in base_pages:
        b_els, _ = all_b_els[page]
        for e in b_els:
            if "Sans CJK" in e["fam"] and e["s"].strip():
                k = (e["s"], e["bold"], e["size"])
                if k in seen:
                    continue
                seen.add(k)
                wb = s_base.text_w(e["s"], "sans", e["bold"], e["size"])
                wp = s_patch.text_w(e["s"], "sans", e["bold"], e["size"])
                if wb > 0:
                    ratios.append({"s": e["s"][:60], "bold": e["bold"], "size": e["size"],
                                   "w_base": round(wb, 1), "w_patch": round(wp, 1),
                                   "ratio": round(wp / wb, 3)})
    rs = sorted(r["ratio"] for r in ratios)
    n = len(rs)
    ar = {"n_strings": n,
          "longer": sum(1 for r in rs if r > 1.005),
          "shorter": sum(1 for r in rs if r < 0.995),
          "same": sum(1 for r in rs if 0.995 <= r <= 1.005),
          "median_ratio": rs[n // 2] if n else None,
          "mean_ratio": round(sum(rs) / n, 3) if n else None,
          "min_ratio": rs[0] if n else None,
          "max_ratio": rs[-1] if n else None,
          "widest": sorted(ratios, key=lambda r: -r["ratio"])[:8],
          "narrowest": sorted(ratios, key=lambda r: r["ratio"])[:8]}
    for b in (True, False):
        sub = [r["ratio"] for r in ratios if r["bold"] == b]
        if sub:
            ar[f"bold_{b}"] = {"n": len(sub), "median": round(sorted(sub)[len(sub) // 2], 3),
                              "mean": round(sum(sub) / len(sub), 3),
                              "longer": sum(1 for r in sub if r > 1.005)}
    report["advance_ratios"] = ar
    # P8 slack (page whose name contains p8, else the last page).
    p8_page = next((p for p in base_pages if "p8" in p), base_pages[-1])
    b8, p8 = all_b_els[p8_page]
    report["p8"] = {"page": p8_page,
                    "base": p8_stats(b8, s_base), "patch": p8_stats(p8, s_patch),
                    "lines_base": report["pages"][p8_page]["lines_base"],
                    "lines_patch": report["pages"][p8_page]["lines_patch"]}
    if args.json_out:
        json.dump(report, open(args.json_out, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
    n_def = tot["defects"]
    for page in base_pages:
        d = report["pages"][page]
        print(f"{page}: els {d['elements_base']}->{d['elements_patch']} "
              f"lines {d['lines_base']}->{d['lines_patch']} diff {d['lines_diff']} "
              f"moved {d['moved_elements']} defects "
              f"{len(d['creambox_defects']) + len(d['creambox_spill_defects'])} "
              f"observe {len(d['creambox_observes'])}")
        for f in d["creambox_defects"]:
            print(f"  DEFECT abs box#{f['box']} y={f['y']} {f['s']!r} over={f['over']}")
        for f in d["creambox_spill_defects"]:
            print(f"  DEFECT spill box#{f['box']} {f['s']!r} {f}")
    print(f"ratios: n={ar['n_strings']} median={ar['median_ratio']} "
          f"boldT={ar.get('bold_True', {}).get('median')} "
          f"boldF={ar.get('bold_False', {}).get('median')}")
    print(f"P8 {p8_page}: lines {report['p8']['lines_base']}->"
          f"{report['p8']['lines_patch']} slack_footer "
          f"{report['p8']['base']['slack_to_footer_rule_2596']}->"
          f"{report['p8']['patch']['slack_to_footer_rule_2596']}")
    print(f"CREAMBOX {'FAIL ' + str(n_def) + ' defects' if n_def else 'PASS 0 defects'}")
    return 1 if n_def else 0


if __name__ == "__main__":
    sys.exit(main())
