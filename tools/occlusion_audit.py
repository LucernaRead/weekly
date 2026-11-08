#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""occlusion_audit.py — THE canonical geometric occlusion audit for Lucerna Weekly.

Consolidates the method that a dozen hand-rolled audit scripts re-derived
(two of them wrongly). Rules baked in from the programme's defect history:

  * Glyph boxes are TRUE INK boxes from PIL/FreeType (font.getbbox), NOT
    advance width (getlength) and NOT the -0.88em/+0.30em em band. The
    advance-width method shipped a false pass on zh-TW×IT P7
    «Struttura della settimana» (ink touched the border at x 1885-1886
    while advance width cleared it); the em band over-flags the P1
    masthead/subtitle pair whose real ink has 20+ clear rows.
  * Line/rect border boxes are EXPANDED by half the stroke width. A
    zero-height <line> box can never intersect anything — that blind spot
    shipped a struck-through caption in EN×PT P6.
  * Bold (font-weight=700) texts are parsed and measured with the Bold
    face. (An early audit regex silently skipped bold elements.)
  * Footer band rule at y=2596 (page 1950x2700, footer baseline 2624 is
    exempt — the footers live below the rule by design).

Classes: COVER (later opaque shape covers >=30% of a text's ink),
LINEX (later line / thin rect crossing a text's ink), FOOTER (ink below
y=2596, footer texts exempt), EDGE (ink past the page edge), TEXTX
(text-ink vs text-ink overlap), BOXTITLE (a text's ink crossing the
borders of the bordered box painted just before it that contains it).

Usage:
    occlusion_audit.py <svg-dir|edition-dir> [--core <svg-dir>] [--json out.json]
    occlusion_audit.py --selftest
Exit: 0 clean · 1 flags found (with --core: NEW flags found) · 2 selftest failed.
A real run executes the synthetic selftest first and refuses to report
if it fails. Flags always require pixel adjudication before fixing —
this tool is the gate, not the verdict.
Run with tools/venv/bin/python.
"""
import argparse, html, json, os, re, sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tables as T

FONTS = T.load()["fonts"]
FACE_INDEX = FONTS["face_index"]
FOOTER_RULE_Y = FONTS["page"]["footer_rule_y"]
PAGE_W = FONTS["page"]["width"]
PAGE_H = FONTS["page"]["height"]

_font_cache = {}
SCALE = 4  # supersample font size for sub-pixel ink metrics


def resolve_font(family, size, bold):
    """(path, index) for an SVG font-family string."""
    fam = family or "Noto Sans CJK SC"
    if "Newsreader" in fam:
        # New standard style (§1.1) Latin text is set in Newsreader, not in
        # Noto CJK: measuring it with a CJK font overstates Latin widths and
        # raises false TEXTX alarms (pilot: 15). Bold has no static Bold
        # file; SemiBold is the closest available weight.
        base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")
        return (os.path.join(base, "Newsreader-SemiBold.ttf") if bold
                else os.path.join(base, "Newsreader-Regular.ttf"), 0)
    if "DejaVu Sans" in fam:
        # Symbol glyphs (✗ ☐ →) are set in DejaVu Sans; the CJK fallback
        # overstates their widths (pilot P7: 4 false ✗ overlaps).
        return ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold
                else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 0)
    if "Unifraktur" in fam:
        return (FONTS["blackletter"], 0)
    serif = "Serif" in fam
    suffix = fam.strip().split()[-1] if fam.strip().split() else "SC"
    index = FACE_INDEX.get(suffix, FACE_INDEX["SC"])
    if serif:
        return (FONTS["serif_bold"] if bold else FONTS["serif_regular"], index)
    return (FONTS["sans_bold"] if bold else FONTS["sans_regular"], index)


def get_font(family, size, bold):
    from PIL import ImageFont
    path, index = resolve_font(family, size, bold)
    px = max(1, int(round(size * SCALE)))
    key = (path, index, px)
    if key not in _font_cache:
        _font_cache[key] = ImageFont.truetype(path, px, index=index)
    return _font_cache[key]


def ink_box(text, family, size, bold, x, y, anchor="start", spacing=0.0):
    """True ink box (l, t, r, b) for a text node with SVG baseline (x, y)."""
    if not text.strip():
        return None
    f = get_font(family, size, bold)
    adv = f.getlength(text) / SCALE + (spacing * (len(text) - 1) if spacing else 0.0)
    l, t, r, b = [v / SCALE for v in f.getbbox(text)]
    ascent = f.getmetrics()[0] / SCALE
    if anchor == "middle":
        left = x - adv / 2 + l
        right = x - adv / 2 + r
    elif anchor == "end":
        left = x - adv + l
        right = x - adv + r
    else:
        left = x + l
        right = x + r
    return (left, y - ascent + t, right, y - ascent + b)


# ---------------- SVG parsing (flat paint order; the corpus has no
# transforms / opacity / tspan — verified in the 2026-10-21 audit) ------
TAG_RE = re.compile(
    r"<text\b(?P<tattrs>[^>]*)>(?P<tcontent>.*?)</text>"
    r"|<(?P<tag>rect|line|image|circle|path)\b(?P<attrs>[^>]*?)/?>",
    re.S)
ATTR_RE = re.compile(r'([\w-]+)="([^"]*)"')


def parse_attrs(s):
    return dict(ATTR_RE.findall(s))


def fnum(attrs, name, default=0.0):
    try:
        return float(attrs.get(name, default))
    except (TypeError, ValueError):
        return default


def clean_text(content):
    content = re.sub(r"<[^>]+>", "", content)
    return html.unescape(content)


class El:
    __slots__ = ("kind", "idx", "attrs", "text", "box", "baseline")

    def __init__(self, kind, idx, attrs, text=None):
        self.kind, self.idx, self.attrs, self.text = kind, idx, attrs, text
        self.box = None
        self.baseline = None


_PATH_NUM = re.compile(r"-?\d*\.?\d+(?:[eE]-?\d+)?")
_PATH_CMD = re.compile(r"[MmLlHhVvCcSsQqTtAaZz]")


def _path_points(d):
    """Absolute points traced by an SVG path `d` (endpoints + curve
    control points). Handles M/L/H/V/C/S/Q/T/A, relative and absolute
    forms, implicit lineto pairs after M, and comma/sign separators."""
    pts = []
    cx = cy = sx = sy = 0.0
    pos = 0
    cmd = None
    tokens = []
    for m in _PATH_CMD.finditer(d):
        if m.start() > pos:
            tokens.append((cmd, d[pos:m.start()]))
        cmd = m.group(0)
        pos = m.end()
    if pos < len(d):
        tokens.append((cmd, d[pos:]))
    for cmd, chunk in tokens:
        if cmd is None:
            continue
        nums = [float(v) for v in _PATH_NUM.findall(chunk)]
        rel = cmd.islower()
        up = cmd.upper()
        i = 0
        if up == "Z":
            cx, cy = sx, sy
            continue
        if up == "M":
            if len(nums) < 2:
                continue
            x, y = nums[0], nums[1]
            cx, cy = (cx + x, cy + y) if rel else (x, y)
            sx, sy = cx, cy
            pts.append((cx, cy))
            i = 2
            up = "L"  # further pairs are implicit lineto
        while i < len(nums):
            if up == "L":
                if i + 1 >= len(nums):
                    break
                x, y = nums[i], nums[i + 1]
                cx, cy = (cx + x, cy + y) if rel else (x, y)
                pts.append((cx, cy))
                i += 2
            elif up == "H":
                x = nums[i]
                cx = cx + x if rel else x
                pts.append((cx, cy))
                i += 1
            elif up == "V":
                y = nums[i]
                cy = cy + y if rel else y
                pts.append((cx, cy))
                i += 1
            elif up == "C":
                if i + 5 >= len(nums):
                    break
                pairs = [(nums[i], nums[i + 1]), (nums[i + 2], nums[i + 3]),
                         (nums[i + 4], nums[i + 5])]
                for (x, y) in pairs:
                    pts.append((cx + x, cy + y) if rel else (x, y))
                cx, cy = pts[-1]
                i += 6
            elif up in ("S", "Q"):
                if i + 3 >= len(nums):
                    break
                pairs = [(nums[i], nums[i + 1]), (nums[i + 2], nums[i + 3])]
                for (x, y) in pairs:
                    pts.append((cx + x, cy + y) if rel else (x, y))
                cx, cy = pts[-1]
                i += 4
            elif up == "T":
                if i + 1 >= len(nums):
                    break
                x, y = nums[i], nums[i + 1]
                cx, cy = (cx + x, cy + y) if rel else (x, y)
                pts.append((cx, cy))
                i += 2
            elif up == "A":
                if i + 6 >= len(nums):
                    break
                x, y = nums[i + 5], nums[i + 6]
                cx, cy = (cx + x, cy + y) if rel else (x, y)
                pts.append((cx, cy))
                i += 7
            else:
                break
    return pts


def shape_box(el):
    """Paint box for a non-text element (lines expanded by half stroke)."""
    a = el.attrs
    if el.kind == "rect":
        x, y = fnum(a, "x"), fnum(a, "y")
        w, h = fnum(a, "width"), fnum(a, "height")
        sw = fnum(a, "stroke-width", 0.0) / 2 if a.get("stroke") not in (None, "none") else 0.0
        return (x - sw, y - sw, x + w + sw, y + h + sw)
    if el.kind == "image":
        x, y = fnum(a, "x"), fnum(a, "y")
        return (x, y, x + fnum(a, "width"), y + fnum(a, "height"))
    if el.kind == "circle":
        cx, cy, r = fnum(a, "cx"), fnum(a, "cy"), fnum(a, "r")
        return (cx - r, cy - r, cx + r, cy + r)
    if el.kind == "line":
        x1, y1, x2, y2 = fnum(a, "x1"), fnum(a, "y1"), fnum(a, "x2"), fnum(a, "y2")
        e = fnum(a, "stroke-width", 1.0) / 2
        return (min(x1, x2) - e, min(y1, y2) - e, max(x1, x2) + e, max(y1, y2) + e)
    if el.kind == "path":
        # Resolve path commands properly: the old code treated every number
        # in `d` as an alternating (x, y) pair, so a RELATIVE lineto
        # (e.g. the JA svglib frost "M451 2022 l20 -14 ...") was misread
        # as absolute coords and produced a page-spanning bogus box
        # (-20, -14, 571, 2022) with 31 false COVER flags on W45 IT x JA P1.
        # This walk tracks the current point and resolves relative
        # commands; curve control points are included (conservative bbox).
        pts = _path_points(a.get("d", ""))
        if not pts:
            return None
        xs, ys = [p[0] for p in pts], [p[1] for p in pts]
        e = fnum(a, "stroke-width", 0.0) / 2
        return (min(xs) - e, min(ys) - e, max(xs) + e, max(ys) + e)
    return None


def is_opaque(el):
    if el.kind == "image":
        return True
    fill = el.attrs.get("fill", "#000000")  # SVG default fill is black
    if fill in ("none", "transparent"):
        return False
    if el.attrs.get("fill-opacity") == "0" or el.attrs.get("opacity") == "0":
        return False
    return True


def is_thin_rect(el):
    if el.kind != "rect":
        return False
    w, h = fnum(el.attrs, "width"), fnum(el.attrs, "height")
    return (h <= 4.5 or w <= 4.5) and (is_opaque(el) or el.attrs.get("stroke") not in (None, "none"))


def parse_svg(svg_text):
    m = re.search(r"<svg[^>]*>", svg_text)
    W, H = PAGE_W, PAGE_H
    if m:
        attrs = parse_attrs(m.group(0))
        W = fnum(attrs, "width", PAGE_W) or PAGE_W
        H = fnum(attrs, "height", PAGE_H) or PAGE_H
    els = []
    for i, mm in enumerate(TAG_RE.finditer(svg_text)):
        if mm.group("tattrs") is not None:
            attrs = parse_attrs(mm.group("tattrs"))
            text = clean_text(mm.group("tcontent"))
            el = El("text", i, attrs, text)
            size = fnum(attrs, "font-size", 20.0)
            bold = attrs.get("font-weight", "") in ("700", "bold")
            spacing = fnum(attrs, "letter-spacing", 0.0)
            el.baseline = fnum(attrs, "y")
            el.box = ink_box(text, attrs.get("font-family", ""), size, bold,
                             fnum(attrs, "x"), el.baseline,
                             attrs.get("text-anchor", "start"), spacing)
            els.append(el)
        else:
            el = El(mm.group("tag"), i, parse_attrs(mm.group("attrs")))
            el.box = shape_box(el)
            els.append(el)
    return els, W, H


def overlap(a, b):
    l, t = max(a[0], b[0]), max(a[1], b[1])
    r, bo = min(a[2], b[2]), min(a[3], b[3])
    if r <= l or bo <= t:
        return 0.0, (0.0, 0.0)
    return (r - l) * (bo - t), (r - l, bo - t)


# ---------------- the audit -------------------------------------------
def audit_page(els, W, H, page):
    flags = []
    texts = [e for e in els if e.kind == "text" and e.box]
    shapes = [e for e in els if e.kind != "text" and e.box]

    def add(cls, el, detail, by=None):
        flags.append({"page": page, "class": cls, "text": el.text[:60],
                      "box": [round(v, 1) for v in el.box], "detail": detail,
                      "by": by})

    for el in texts:
        l, t, r, b = el.box
        area = max(1.0, (r - l) * (b - t))
        if l < -0.5 or r > W + 0.5 or t < -0.5 or b > H + 0.5:
            add("EDGE", el, f"ink box {el.box} outside page {W}x{H}")
        if b > FOOTER_RULE_Y + 0.5 and (el.baseline or 0) < 2600:
            add("FOOTER", el, f"ink bottom {b:.1f} below footer rule {FOOTER_RULE_Y} (baseline {el.baseline})")
        for sh in shapes:
            if sh.idx <= el.idx:
                continue
            ov, _ = overlap(el.box, sh.box)
            if ov <= 0:
                continue
            if sh.kind == "line" or is_thin_rect(sh):
                add("LINEX", el, f"later {sh.kind} box {[round(v,1) for v in sh.box]} crosses ink",
                    by=f"{sh.kind}@{sh.idx}")
            elif is_opaque(sh) and ov / area >= 0.30:
                add("COVER", el, f"{ov/area:.0%} of ink covered by later {sh.kind} "
                                 f"box {[round(v,1) for v in sh.box]}",
                    by=f"{sh.kind}@{sh.idx}")
    # TEXTX: text-ink vs text-ink
    ordered = sorted(texts, key=lambda e: e.box[1])
    for i, a in enumerate(ordered):
        for b in ordered[i + 1:]:
            if b.box[1] > a.box[3]:
                break
            ov, (ow, oh) = overlap(a.box, b.box)
            if ov >= 9.0 and ow >= 3.0 and oh >= 3.0:
                flags.append({"page": page, "class": "TEXTX", "text": a.text[:60],
                              "box": [round(v, 1) for v in a.box],
                              "detail": f"ink overlaps {b.text[:40]!r} by {ow:.1f}x{oh:.1f}px",
                              "by": f"text@{b.idx}"})
    # BOXTITLE: ink crossing the borders of the containing bordered box
    rects = [e for e in shapes if e.kind == "rect"
             and (e.attrs.get("stroke") not in (None, "none") or e.attrs.get("fill") == "#2c2822")
             and fnum(e.attrs, "width") < PAGE_W * 0.95
             and not (fnum(e.attrs, "width") >= 1800 and fnum(e.attrs, "height") >= 2500)]
    for el in texts:
        ax, ay = fnum(el.attrs, "x"), el.baseline or 0
        cx, cy = (el.box[0] + el.box[2]) / 2, (el.box[1] + el.box[3]) / 2
        cands = []
        for rc in rects:
            if rc.idx >= el.idx or el.idx - rc.idx > 80:
                continue
            rl, rt, rr, rb = rc.box
            if (rl - 2 <= ax <= rr + 2 and rt - 2 <= ay <= rb + 2) or \
               (rl <= cx <= rr and rt <= cy <= rb):
                cands.append((fnum(rc.attrs, "width") * fnum(rc.attrs, "height"), rc))
        if not cands:
            continue
        rc = min(cands)[1]
        rl, rt, rr, rb = (fnum(rc.attrs, "x"), fnum(rc.attrs, "y"),
                          fnum(rc.attrs, "x") + fnum(rc.attrs, "width"),
                          fnum(rc.attrs, "y") + fnum(rc.attrs, "height"))
        l, t, r, b = el.box
        sides = []
        if l < rl - 0.5: sides.append(f"left ink {l:.1f} < border {rl:.1f}")
        if r > rr + 0.5: sides.append(f"right ink {r:.1f} > border {rr:.1f}")
        if t < rt - 0.5: sides.append(f"top ink {t:.1f} < border {rt:.1f}")
        if b > rb + 0.5: sides.append(f"bottom ink {b:.1f} > border {rb:.1f}")
        if sides:
            add("BOXTITLE", el, "ink crosses its box borders: " + "; ".join(sides),
                by=f"rect@{rc.idx}")
    return flags


def audit_dir(svgdir):
    files = sorted(f for f in os.listdir(svgdir) if f.endswith(".svg"))
    if not files:
        raise SystemExit(f"no SVGs in {svgdir}")
    all_flags = []
    for fn in files:
        els, W, H = parse_svg(open(os.path.join(svgdir, fn), encoding="utf-8").read())
        all_flags.extend(audit_page(els, W, H, fn))
    return all_flags


def resolve_svgdir(path):
    if os.path.isdir(os.path.join(path, "svg")):
        return os.path.join(path, "svg")
    return path


def flag_key(f):
    return (f["page"], f["class"], f["text"][:40])


# ---------------- synthetic selftest ------------------------------------
FAM = "Noto Sans CJK SC"

def _txt(x, y, s, size=25, bold=False):
    wt = ' font-weight="700"' if bold else ""
    return (f'<text x="{x}" y="{y}" font-family="{FAM}" font-size="{size}"{wt} '
            f'fill="#28251d" text-anchor="start">{html.escape(s)}</text>')

SELFTEST_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" width="1950" height="2700" viewBox="0 0 1950 2700">'
    '<rect width="1950" height="2700" fill="#f7f1e2"/>'
    + _txt(100, 300, "Clean control text")
    + '<line x1="90" y1="400" x2="600" y2="400" stroke="#b3a06a" stroke-width="2"/>'
    + _txt(100, 500, "Covered text line")
    + '<rect x="90" y="455" width="520" height="70" fill="#f1ead6"/>'
    + _txt(100, 700, "Line struck text")
    + '<line x1="90" y1="690" x2="600" y2="690" stroke="#28251d" stroke-width="2"/>'
    + _txt(900, 2560, "Agy", size=150)
    + _txt(1850, 1000, "Edge spill text long")
    + _txt(100, 1200, "Overlap one")
    + _txt(110, 1205, "Overlap two")
    + '<rect x="100" y="1400" width="300" height="120" fill="#fdfaf0" stroke="#28251d" stroke-width="1.2"/>'
    + _txt(120, 1450, "A very long box title that spills")
    + _txt(120, 1500, "Inside box fine")
    + "</svg>")
CLEAN_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" width="1950" height="2700" viewBox="0 0 1950 2700">'
    '<rect width="1950" height="2700" fill="#f7f1e2"/>'
    + _txt(100, 300, "Perfectly clean text")
    + '<line x1="90" y1="400" x2="600" y2="400" stroke="#b3a06a" stroke-width="2"/>'
    + '<rect x="100" y="600" width="300" height="120" fill="#fdfaf0" stroke="#28251d" stroke-width="1.2"/>'
    + _txt(120, 660, "Inside box fine")
    + "</svg>")
CLEAN_TEXTS = ("Clean control text", "Inside box fine", "Perfectly clean text")


def run_selftest():
    els, W, H = parse_svg(SELFTEST_SVG)
    flags = audit_page(els, W, H, "selftest.svg")
    by_class = defaultdict(list)
    for f in flags:
        by_class[f["class"]].append(f)
    problems = []
    for cls in ("COVER", "LINEX", "FOOTER", "EDGE", "TEXTX", "BOXTITLE"):
        if not by_class.get(cls):
            problems.append(f"selftest: planted {cls} defect did NOT fire")
    for f in flags:
        if any(f["text"].startswith(c) for c in CLEAN_TEXTS):
            problems.append(f"selftest: clean control flagged: {f}")
    els2, W2, H2 = parse_svg(CLEAN_SVG)
    flags2 = audit_page(els2, W2, H2, "clean.svg")
    if flags2:
        problems.append(f"selftest: clean page produced {len(flags2)} flags: {flags2}")
    return problems, {k: len(v) for k, v in sorted(by_class.items())}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("svgdir", nargs="?", help="edition dir (containing svg/) or svg dir")
    ap.add_argument("--core", help="core svg/edition dir: flags also present there are not NEW")
    ap.add_argument("--json", dest="json_out", help="write JSON report to this path")
    ap.add_argument("--selftest", action="store_true", help="run only the synthetic selftest")
    args = ap.parse_args(argv)

    problems, fired = run_selftest()
    if problems:
        for p in problems:
            print(f"SELFTEST FAIL: {p}", file=sys.stderr)
        return 2
    print(f"selftest OK: planted classes fired {fired}; clean controls silent")
    if args.selftest:
        return 0
    if not args.svgdir:
        ap.error("svgdir is required unless --selftest")

    svgdir = resolve_svgdir(args.svgdir)
    flags = audit_dir(svgdir)
    report = {"svgdir": svgdir, "flags": flags, "flag_count": len(flags)}
    exit_code = 1 if flags else 0
    if args.core:
        core_flags = audit_dir(resolve_svgdir(args.core))
        core_keys = {flag_key(f) for f in core_flags}
        new_flags = [f for f in flags if flag_key(f) not in core_keys]
        report["core_flag_count"] = len(core_flags)
        report["new_flags"] = new_flags
        report["new_flag_count"] = len(new_flags)
        exit_code = 1 if new_flags else 0
    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=1)
    by_class = defaultdict(int)
    for f in flags:
        by_class[f["class"]] += 1
    print(f"{svgdir}: {len(flags)} flags {dict(sorted(by_class.items())) or ''}")
    for f in flags:
        print(f"  [{f['class']}] {f['page']} {f['text']!r} — {f['detail']}")
    if args.core:
        print(f"core: {report['core_flag_count']} flags; NEW vs core: {report['new_flag_count']}")
        for f in report["new_flags"]:
            print(f"  NEW [{f['class']}] {f['page']} {f['text']!r} — {f['detail']}")
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
