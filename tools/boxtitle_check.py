#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""boxtitle_check.py — standing gate: horizontal box-title true-ink check (W47).

Promoted 2026-11-11 from two proven measurements:
  * ``hidden_files/w47/scratch-proof-pt-en2/boxtitle_trueink.py`` — PIL
    true-ink bbox of a title via the edition's own svglib (per-character
    font runs, anchor + letter-spacing aware);
  * ``hidden_files/w47/scratch-proof2-it-de1/h-overflow-proof2.py`` — the
    same ink math applied to every <text> node of a page.

Blind spot it closes (run-log 2026-11-11 20:58 UTC, it-de proof2): box
titles are drawn single-line, start-anchored (``bslib4.py:186``) with NO
width check against their cream box, so a long reader-language gloss can
run past the box onto white paper — e.g. it-de P1 cifre +138.5 px, P2
frase +30.5 px — while all 20 existing gates stay green (occlusion only
counts stroked boxes; cream boxes have no border).

What it does: for every cream (``#f0eee5``) rect on every page, measure the
PIL true-ink left/right edge of every text element whose baseline sits
inside the box, and flag ink running past either box edge. Title lines
(the box's first line when bold and >= 22 pt, or any line whose text
matches an ``f.box("TITLE", ...)`` call in the edition's content files)
are reported as TITLE; other lines as BODY. The same ink math also catches
body-line horizontal overflow (en-it SAY IT +36 px class).

Adjudication follows the proof1 STRADDLE rule (run-log L1836/L1940):
a past-the-edge line is a DEFECT iff it is clipped (ink crosses the page
edge), overlaps another element, or is a regression — i.e. it overflows
where the old version (``--backup-root`` backup copy, when one exists) or
the core edition's same box (same target family) does not. The same
overflow in the old version / core is an OBSERVATION, not a defect.
Overflow of 1.0 px or less is MARGINAL (measurement tolerance).

Read-only wrt the edition dir. Writes nothing except the optional JSON
report (--json-dir) and stdout. Fonts come from the edition's own
``svglib.py`` (loaded once per distinct file hash, so family-specific
font variants are always honoured).

Usage:
  python3 tools/boxtitle_check.py <edition-dir> [<edition-dir> ...]
      [--json-dir DIR] [--backup-root DIR]
Exit 0 iff no DEFECT in any edition; exit 1 if any DEFECT found.
Run with the repo venv (tools/venv/bin/python) for PIL + fontTools.
"""
import ast
import gc
import glob
import hashlib
import html
import importlib.util
import json
import os
import re
import sys
import xml.etree.ElementTree as ET

PAGE_W = 1950.0
TOL = 0.5            # px: ink past the box edge beyond this counts as over
MARGINAL = 1.0       # px: over at or below this is measurement tolerance
TITLE_MIN_SIZE = 22.0
NS = "{http://www.w3.org/2000/svg}"
TARGETS = ["zh-cn", "zh-tw", "de", "en", "es", "fr", "it", "ja", "ko",
           "nl", "pt", "ru"]
NEWS_DIR = "/home/hatch/.local/share/fonts"
UNI_PATH = os.path.join(NEWS_DIR, "UnifrakturMaguntia-Book.ttf")

_sg_cache = {}
_SG_MAX = 4   # max live svglib variants (see load_svglib)
_uni_cache = {}


def parse_slug(slug):
    """-> (target, reader, is_core)"""
    if slug.startswith("core-"):
        return slug[5:], None, True
    rest = slug[len("2026-w47-"):] if slug.startswith("2026-w47-") else slug
    for t in TARGETS:
        if rest == t or rest.startswith(t + "-"):
            return t, rest[len(t) + 1:] or None, False
    return None, None, False


def md5_file(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_svglib(ed_dir):
    """Load the edition's svglib.py, keyed by file hash (LRU, max 4 live
    copies — each holds 9 font cmaps; editions are processed grouped by
    variant so reloads are rare). A byte change in svglib.py loads as a
    different variant, so family-specific fonts are always honoured."""
    path = os.path.join(ed_dir, "svglib.py")
    key = md5_file(path)
    if key in _sg_cache:
        return _sg_cache[key]
    while len(_sg_cache) >= _SG_MAX:
        old_key = next(iter(_sg_cache))
        old_mod = _sg_cache.pop(old_key)
        sys.modules.pop(getattr(old_mod, "__name__", ""), None)
    gc.collect()
    name = "edition_svglib_" + key[:12]
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    _sg_cache[key] = mod
    return mod


def uni_font(size):
    from PIL import ImageFont
    key = int(round(size))
    if key not in _uni_cache:
        _uni_cache[key] = ImageFont.truetype(UNI_PATH, key)
    return _uni_cache[key]


def kind_of(family):
    if "Serif" in family or "Newsreader" in family:
        return "serif"
    if "Sans" in family:
        return "sans"
    return "serif"


def ink_bbox(sg, family, size, bold, italic, anchor, spacing, x, txt):
    """True-ink bbox (left, right, top, bottom) in SVG coords, baseline = y.
    Mirrors the build's svglib.text(): one <text> per font run, x positions
    already include letter-spacing advances; the attr adds spacing inside
    each run. Returns None for whitespace-only text (no ink).
    Old-generation svglib (core-ja / core-ko) has no _runs/_pil: one CJK
    font per kind, so the whole string is measured in _font(kind,...)."""
    if not txt.strip():
        return None
    sp = spacing or 0.0
    if family == "UnifrakturMaguntia":
        f = uni_font(size)
        total = f.getlength(txt) + sp * max(0, len(txt) - 1)
        x0 = x - total / 2.0 if anchor == "middle" else (
            x - total if anchor == "end" else x)
        l, t, r, b = f.getbbox(txt) if txt.strip() else (0, 0, 0, 0)
        return (x0 + l, x0 + sp * max(0, len(txt) - 1) + r, t, b)
    kind = kind_of(family)
    if hasattr(sg, "_runs"):
        runs = sg._runs(txt, kind, bold, italic)
        pil = lambda cls: sg._pil(kind, bold, cls, size)
    else:
        # Old-generation svglib (W47 core-ja / core-ko, 305-line build):
        # no per-character runs — one CJK font per kind, _font(kind, bold,
        # size). The builder laid out with that font, so measure the whole
        # string in it. _font ignores italic.
        f0 = sg._font(kind, bold, size)
        runs = [(txt, None)]
        pil = lambda cls: f0
    total = sum(pil(cls).getlength(t)
                for t, cls in runs) + sp * max(0, len(txt) - 1)
    x0 = x - total / 2.0 if anchor == "middle" else (
        x - total if anchor == "end" else x)
    il, ir, itop, ibot = None, None, None, None
    cx = x0
    for i, (t, cls) in enumerate(runs):
        f = pil(cls)
        if t.strip():
            bx0, by0, bx1, by1 = f.getbbox(t, anchor="ls")
            cand_l = cx + bx0
            cand_r = cx + sp * max(0, len(t) - 1) + bx1
            il = cand_l if il is None else min(il, cand_l)
            ir = cand_r if ir is None else max(ir, cand_r)
            itop = by0 if itop is None else min(itop, by0)
            ibot = by1 if ibot is None else max(ibot, by1)
        w = f.getlength(t)
        cx += w + (sp * len(t) if i < len(runs) - 1 else 0)
    if il is None:
        return None
    return (il, ir, itop, ibot)


def parse_page(path, sg):
    """-> (cream_rects, elements, obstacles)
    elements: dicts with x, y, fs, bold, text, ink (l, r, top, bot rel. y).
    obstacles: geometry of images / stroked rects / rules, for overlap."""
    root = ET.parse(path).getroot()
    rects = []
    obstacles = []
    for r in root.iter(NS + "rect"):
        try:
            x, y, w, h = (float(r.get(a)) for a in ("x", "y", "width", "height"))
        except (TypeError, ValueError):
            continue
        if (r.get("fill") or "").lower() == "#f0eee5":
            rects.append((x, y, w, h))
        if r.get("stroke"):
            obstacles.append(("rect", x, y, x + w, y + h))
    for im in root.iter(NS + "image"):
        try:
            x, y, w, h = (float(im.get(a)) for a in ("x", "y", "width", "height"))
        except (TypeError, ValueError):
            continue
        obstacles.append(("image", x, y, x + w, y + h))
    for ln in root.iter(NS + "line"):
        try:
            x1, y1, x2, y2 = (float(ln.get(a)) for a in ("x1", "y1", "x2", "y2"))
        except (TypeError, ValueError):
            continue
        obstacles.append(("line", min(x1, x2) - 0.6, min(y1, y2) - 0.6,
                          max(x1, x2) + 0.6, max(y1, y2) + 0.6))
    els = []
    for t in root.iter(NS + "text"):
        try:
            x, y, fs = (float(t.get(a)) for a in ("x", "y", "font-size"))
        except (TypeError, ValueError):
            continue
        txt = html.unescape("".join(t.itertext()))
        if not txt.strip():
            continue
        fam = (t.get("font-family") or "Newsreader").split(",")[0].strip()
        wt = t.get("font-weight") or ""
        bold = wt.isdigit() and int(wt) >= 600
        italic = (t.get("font-style") or "") == "italic"
        anchor = t.get("text-anchor") or "start"
        try:
            spacing = float(t.get("letter-spacing"))
        except (TypeError, ValueError):
            spacing = 0.0
        ink = ink_bbox(sg, fam, fs, bold, italic, anchor, spacing, x, txt)
        if ink is None:
            continue
        els.append({"x": x, "y": y, "fs": fs, "bold": bold, "family": fam,
                    "text": txt, "il": ink[0], "ir": ink[1],
                    "itop": ink[2], "ibot": ink[3]})
    # register text ink as obstacles for the overlap test (excluding self
    # at check time by identity)
    for e in els:
        obstacles.append(("text", e["il"], e["y"] + e["itop"],
                          e["ir"], e["y"] + e["ibot"], id(e)))
    return rects, els, obstacles


def page_no(fname):
    m = re.match(r"p(\d+)-", fname)
    return int(m.group(1)) if m else None


def box_titles(ed_dir):
    """Titles from f.box("TITLE", ...) calls in the edition's content files."""
    titles = set()
    for path in sorted(glob.glob(os.path.join(ed_dir, "content*.py"))):
        try:
            src = open(path, encoding="utf-8").read()
        except OSError:
            continue
        for m in re.finditer(r"""f\.box\(\s*("([^"\\]|\\.)*"|'([^'\\]|\\.)*')""", src):
            try:
                val = ast.literal_eval(m.group(1))
            except (ValueError, SyntaxError):
                continue
            if val.strip():
                titles.add(val)
    return titles


def find_backup(backup_root, slug):
    """Newest backup copy of this edition under backup-root, or None."""
    if not backup_root:
        return None
    cands = []
    for pat in ("scratch-refanout-*/backup*/" + slug,
                "scratch-refanout-*/backup-old/" + slug,
                "scratch-fanout-*/backup*/" + slug):
        for d in glob.glob(os.path.join(backup_root, pat)):
            if os.path.isdir(os.path.join(d, "svg")):
                cands.append(d)
    if not cands:
        return None
    return max(cands, key=lambda d: os.path.getmtime(d))


def _enclosing(rects, e):
    """Cream rect enclosing element e, or None."""
    for (rx, ry, rw, rh) in rects:
        if rx - 1 <= e["x"] <= rx + rw + 1 and ry <= e["y"] <= ry + rh:
            return (rx, ry, rw, rh)
    return None


def _over_in(e, box):
    rx, _, rw, _ = box
    return max(e["ir"] - (rx + rw), rx - e["il"])


def core_baseline(core_parsed, text, is_title, rx, ry, rw):
    """Core edition's over for the corresponding title/box (same page).
    Matches by title head (target-language part before U+3000 — the gloss
    differs per reader), else by the nearest same-column box. The core's
    boxes sit at different y than the fan-out's, so y is never matched."""
    if core_parsed is None:
        return None
    crects, cels = core_parsed
    head = text.split("　")[0]
    if is_title and head:
        for ce in cels:
            if ce["bold"] and ce["fs"] >= TITLE_MIN_SIZE and (
                    ce["text"] == head
                    or ce["text"].startswith(head + "　")):
                box = _enclosing(crects, ce)
                if box:
                    return _over_in(ce, box)
    cands = [(abs(cry - ry), crx, cry, crw, crh)
             for (crx, cry, crw, crh) in crects
             if abs(crx - rx) <= 1.0 and abs(crw - rw) <= 1.0]
    if not cands:
        return None
    _, crx, cry, crw, crh = min(cands)
    cins = [ce for ce in cels
            if crx - 1 <= ce["x"] <= crx + crw + 1 and cry <= ce["y"] <= cry + crh]
    if not cins:
        return None
    if is_title:
        cmin = min(ce["y"] for ce in cins)
        ct = [ce for ce in cins if abs(ce["y"] - cmin) <= 0.5 and ce["bold"]
              and ce["fs"] >= TITLE_MIN_SIZE]
        pool = ct if ct else cins
    else:
        pool = cins
    return max(_over_in(ce, (crx, cry, crw, crh)) for ce in pool)


def backup_baseline(backup_parsed, text):
    """Old version's over for the same text (exact match), or None."""
    if backup_parsed is None:
        return None
    brects, bels = backup_parsed
    for be in bels:
        if be["text"] == text:
            box = _enclosing(brects, be)
            if box:
                return _over_in(be, box)
            return None
    return None


def _parse_cached(cache, base_dir, fn):
    if fn not in cache:
        path = os.path.join(base_dir, "svg", fn)
        if not os.path.exists(path):
            cache[fn] = None
        else:
            try:
                cache[fn] = parse_page(path, load_svglib(base_dir))[:2]
            except Exception:
                cache[fn] = None
    return cache[fn]


def _overlaps(seg, obstacles, self_id):
    """seg: (x0, y0, x1, y1). True if it overlaps any obstacle by > 0.5 px
    in both dimensions."""
    sx0, sy0, sx1, sy1 = seg
    for ob in obstacles:
        if len(ob) == 6 and ob[5] == self_id:
            continue
        _, ox0, oy0, ox1, oy1 = ob[:5]
        if (min(sx1, ox1) - max(sx0, ox0) > 0.5
                and min(sy1, oy1) - max(sy0, oy0) > 0.5):
            return True, ob[0]
    return False, None


def scan_edition(ed_dir, week_dir, backup_root):
    slug = os.path.basename(os.path.normpath(ed_dir))
    target, reader, is_core = parse_slug(slug)
    sg = load_svglib(ed_dir)
    titles = box_titles(ed_dir)
    core_dir = ed_dir if is_core else os.path.join(week_dir, "core-" + target) \
        if target else None
    core_ok = core_dir and os.path.isdir(core_dir) and not is_core
    backup_dir = find_backup(backup_root, slug) if backup_root else None
    svg_dir = os.path.join(ed_dir, "svg")
    files = sorted(f for f in os.listdir(svg_dir) if f.endswith(".svg"))
    res = {"edition": slug, "target": target, "reader": reader,
           "is_core": is_core, "core_dir": core_dir,
           "backup_dir": backup_dir, "titles": 0, "body_lines": 0,
           "flags": [], "marginal": [], "defects": 0, "observes": 0}
    core_pages, backup_pages = {}, {}
    for i, fn in enumerate(files):
        pg = page_no(fn) or (i + 1)
        rects, els, obstacles = parse_page(os.path.join(svg_dir, fn), sg)
        # elements per box
        for (rx, ry, rw, rh) in rects:
            bot = ry + rh
            inside = [e for e in els
                      if rx - 1 <= e["x"] <= rx + rw + 1 and ry <= e["y"] <= bot]
            if not inside:
                continue
            min_y = min(e["y"] for e in inside)
            for e in inside:
                is_title = (e["text"] in titles) or (
                    abs(e["y"] - min_y) <= 0.5 and e["bold"]
                    and e["fs"] >= TITLE_MIN_SIZE)
                if is_title:
                    res["titles"] += 1
                else:
                    res["body_lines"] += 1
                over_r = e["ir"] - (rx + rw)
                over_l = rx - e["il"]
                over = max(over_r, over_l)
                if over <= TOL:
                    continue
                side = "right" if over_r >= over_l else "left"
                # --- baselines for adjudication
                core_over = None
                if core_ok:
                    core_over = core_baseline(
                        _parse_cached(core_pages, core_dir, fn),
                        e["text"], is_title, rx, ry, rw)
                backup_over = None
                if backup_dir:
                    backup_over = backup_baseline(
                        _parse_cached(backup_pages, backup_dir, fn),
                        e["text"])
                # --- overlap / clip
                if side == "right":
                    seg = (rx + rw, e["y"] + e["itop"], e["ir"], e["y"] + e["ibot"])
                else:
                    seg = (e["il"], e["y"] + e["itop"], rx, e["y"] + e["ibot"])
                hit, hit_kind = _overlaps(seg, obstacles, id(e))
                clip = e["ir"] > PAGE_W or e["il"] < 0
                if over <= MARGINAL:
                    verdict, why = "MARGINAL", "within 1.0px tolerance"
                elif clip or hit:
                    verdict = "DEFECT"
                    why = ("ink crosses page edge" if clip else
                           f"overflowing ink overlaps {hit_kind}")
                elif backup_over is not None:
                    if over - backup_over > 1.0:
                        verdict, why = "DEFECT", (
                            f"regression vs backup ({backup_over:+.1f}px)")
                    else:
                        verdict, why = "OBSERVE", (
                            f"same as backup ({backup_over:+.1f}px)")
                elif core_over is not None:
                    if core_over <= MARGINAL:
                        verdict, why = "DEFECT", (
                            f"regression vs core (core {core_over:+.1f}px)")
                    else:
                        verdict, why = "OBSERVE", (
                            f"inherited from core ({core_over:+.1f}px)")
                elif is_core:
                    verdict, why = "DEFECT", "core title overflows its box"
                else:
                    verdict, why = "DEFECT", "no baseline; overflow is new"
                rec = {"page": pg, "role": "TITLE" if is_title else "BODY",
                       "text": e["text"][:80], "x": round(e["x"], 1),
                       "y": round(e["y"], 1), "fs": e["fs"],
                       "box": [round(rx, 1), round(ry, 1), round(rw, 1),
                               round(rh, 1)],
                       "ink_l": round(e["il"], 1), "ink_r": round(e["ir"], 1),
                       "over": round(over, 1), "side": side,
                       "core_over": (None if core_over is None
                                     else round(core_over, 1)),
                       "backup_over": (None if backup_over is None
                                       else round(backup_over, 1)),
                       "overlap": hit_kind if hit else None,
                       "clip": clip, "verdict": verdict, "why": why}
                if verdict == "MARGINAL":
                    res["marginal"].append(rec)
                else:
                    res["flags"].append(rec)
                    if verdict == "DEFECT":
                        res["defects"] += 1
                    else:
                        res["observes"] += 1
    return res


def print_edition(res, out=sys.stdout):
    print(f"== {res['edition']}  core={'self' if res['is_core'] else res['core_dir']} "
          f"backup={res['backup_dir'] or '-'}", file=out)
    for f in res["flags"]:
        tag = "DEFECT" if f["verdict"] == "DEFECT" else "observe"
        print(f"  P{f['page']} [{f['role']}] {tag} over={f['over']:+.1f}px "
              f"({f['side']}) core={f['core_over']} backup={f['backup_over']} "
              f"| {f['why']} | {f['text'][:60]!r}", file=out)
    print(f"BOXTITLE {res['edition']}: {res['titles']} titles, "
          f"{res['body_lines']} body lines, {res['defects']} DEFECT, "
          f"{res['observes']} OBSERVE, {len(res['marginal'])} marginal",
          file=out)


def main(argv):
    args, json_dir, backup_root = [], None, None
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--json-dir" and i + 1 < len(argv):
            json_dir = argv[i + 1]
            i += 2
        elif a == "--backup-root" and i + 1 < len(argv):
            backup_root = argv[i + 1]
            i += 2
        elif a.startswith("--"):
            print(f"unknown option: {a}", file=sys.stderr)
            return 2
        else:
            args.append(a)
            i += 1
    if not args:
        print("usage: boxtitle_check.py <edition-dir> [...] [--json-dir DIR] "
              "[--backup-root DIR]", file=sys.stderr)
        return 2
    if json_dir:
        os.makedirs(json_dir, exist_ok=True)
    # process editions grouped by svglib variant so the font cache stays hot
    def _variant(ed):
        try:
            return md5_file(os.path.join(ed, "svglib.py"))
        except OSError:
            return ""
    args = sorted(args, key=lambda ed: (_variant(ed), ed))
    rc = 0
    for ed in args:
        week_dir = os.path.dirname(os.path.normpath(ed))
        res = scan_edition(ed, week_dir, backup_root)
        print_edition(res)
        if json_dir:
            with open(os.path.join(json_dir, res["edition"] + ".json"),
                      "w", encoding="utf-8") as f:
                json.dump(res, f, ensure_ascii=False, indent=1)
        if res["defects"]:
            rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
