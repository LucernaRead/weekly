# -*- coding: utf-8 -*-
"""W45 zh-tw x es builder self-checks (all read-only except stdout).
1. Gloss counts: split each gloss() call string on '·' itself (README #21),
   core vs edition, item by item, per page.
2. Same-baseline ink-collision scan (all pages, PIL TC metrics).
3. Chart-label element check: P4/P6 text ink vs later-drawn rects.
4. Residual-Latin adjudication: every Latin-script run in edition SVGs.
5. Traditional-independence cross-check: edition Traditional char set vs
   UNION(W43 zh-tw-es shipped SVG text, W45 zh-tw core SVG text).
6. P7 phrases: all 8 verbatim, exactly 2x each, page tags.
7. Image payloads byte-identical core vs edition + credits verbatim.
"""
import ast, base64, hashlib, os, re, sys
from PIL import ImageFont

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE_SVG = os.path.join(GOAL, "files/weekly-report-w45-zhtw-core/svg")
ED_SVG = os.path.join(GOAL, "files/weekly-report-w45-zh-tw-es/svg")
W43_SVG = os.path.join(GOAL, "files/weekly-report-zh-tw-es/svg")
CORE_BUILD = os.path.join(GOAL, "hidden_files/weekly-report-w45-zhtw-build")
ED_BUILD = os.path.join(GOAL, "hidden_files/weekly-report-w45-zh-tw-es-build")
PAGES = ["p1-front", "p2-life", "p3-culture", "p4-sport",
         "p5-youth", "p6-deep", "p7-lang", "p8-test"]
PAGE_OF_FILE = {"content12.py": [1, 2], "content34.py": [3, 4],
                "content56.py": [5, 6], "content7.py": [7], "content8.py": [8]}


def gloss_strings(build):
    """(page -> [item-count per gloss() call]) via AST on content files."""
    out = {}
    for fname, pages in PAGE_OF_FILE.items():
        tree = ast.parse(open(os.path.join(build, fname), encoding="utf-8").read())
        calls = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) \
               and node.func.attr == "gloss" and node.args \
               and isinstance(node.args[0], ast.Constant):
                calls.append((node.lineno, node.args[0].value))
        calls = [v for _, v in sorted(calls)]
        # assign calls to pages in file order by CURPAGE markers is fragile;
        # instead split calls evenly: content files set CURPAGE sequentially
        # and calls appear in page order; use source order + page boundaries
        # from the file's CURPAGE assignments.
        src = open(os.path.join(build, fname), encoding="utf-8").read()
        marks = [(m.start(), int(m.group(1)))
                 for m in re.finditer(r"CURPAGE\[0\] = (\d)", src)]
        # map each gloss call position to its page
        pos = [m.start() for m in re.finditer(r"\.gloss\(", src)]
        for call, p in zip(calls, pos):
            pg = marks[0][1]
            for start, num in marks:
                if start <= p:
                    pg = num
            out.setdefault(pg, []).append(len(call.split("·")))
    return out


def parse_attrs(attrstr):
    d = {}
    for m in re.finditer(r'([\w-]+)="([^"]*)"', attrstr):
        d[m.group(1)] = m.group(2)
    return d


def svg_texts(path):
    src = open(path, encoding="utf-8").read()
    texts = []
    for m in re.finditer(r"<text ([^>]*)>([^<]*)</text>", src):
        a = parse_attrs(m.group(1))
        texts.append((float(a["x"]), float(a["y"]), float(a["font-size"]), m.group(2), a))
    return texts, src


def main():
    print("== 1. gloss counts (split on ·) ==")
    gc, ge = gloss_strings(CORE_BUILD), gloss_strings(ED_BUILD)
    tot_c = tot_e = 0
    for pg in sorted(set(gc) | set(ge)):
        c, e = gc.get(pg, []), ge.get(pg, [])
        tot_c += sum(c); tot_e += sum(e)
        print(f"  P{pg} core {c} (sum {sum(c)})  edition {e} (sum {sum(e)})  {'OK' if c == e else 'MISMATCH'}")
    print(f"  TOTAL core {tot_c} edition {tot_e}")

    print("== 2. same-baseline ink-collision scan ==")
    flags = 0
    for name in PAGES:
        texts, _ = svg_texts(os.path.join(ED_SVG, name + ".svg"))
        nodes = []
        for x, y, size, t, a in texts:
            fam = a.get("font-family", "")
            bold = a.get("font-weight") == "700"
            path = ("/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc" if bold and "Serif" in fam else
                    "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc" if "Serif" in fam else
                    "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc" if bold else
                    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc")
            fnt = ImageFont.truetype(path, int(round(size)), index=3)
            w = fnt.getlength(t)
            anchor = a.get("text-anchor", "start")
            x0 = x - w if anchor == "end" else (x - w / 2 if anchor == "middle" else x)
            nodes.append((y, x0, x0 + w, t))
        by_y = {}
        for y, x0, x1, t in nodes:
            by_y.setdefault(round(y, 1), []).append((x0, x1, t))
        for y, lst in by_y.items():
            lst.sort()
            for (a0, a1, at), (b0, b1, bt) in zip(lst, lst[1:]):
                if b0 < a1 - 1.0:
                    print(f"  COLLISION {name} y={y}: {at[:40]!r} vs {bt[:40]!r}"); flags += 1
    print(f"  same-baseline flags: {flags}")

    print("== 3. chart-label element check (P4/P6: text ink vs later rects) ==")
    for name in ["p4-sport", "p6-deep"]:
        src = open(os.path.join(ED_SVG, name + ".svg"), encoding="utf-8").read()
        elems = []  # (kind, x0, y0, x1, y1, text)
        for m in re.finditer(r"<rect ([^>]*)/>|<text ([^>]*)>([^<]*)</text>", src):
            if m.group(1) is not None:
                a = parse_attrs(m.group(1))
                try:
                    x, y, w, h = float(a["x"]), float(a["y"]), float(a["width"]), float(a["height"])
                except KeyError:
                    continue
                if w >= 1800:
                    continue
                elems.append(("rect", x, y, x + w, y + h, ""))
            else:
                a = parse_attrs(m.group(2))
                t = m.group(3)
                fam = a.get("font-family", "")
                bold = a.get("font-weight") == "700"
                size = float(a["font-size"])
                path = ("/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc" if bold and "Serif" in fam else
                        "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc" if "Serif" in fam else
                        "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc" if bold else
                        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc")
                fnt = ImageFont.truetype(path, int(round(size)), index=3)
                w = fnt.getlength(t)
                x = float(a["x"]); y = float(a["y"])
                anchor = a.get("text-anchor", "start")
                x0 = x - w if anchor == "end" else (x - w / 2 if anchor == "middle" else x)
                elems.append(("text", x0, y - size, x0 + w, y + size * 0.3, t))
        hits = 0
        for i, (k, x0, y0, x1, y1, t) in enumerate(elems):
            if k != "text":
                continue
            for (k2, rx0, ry0, rx1, ry1, _) in elems[i + 1:]:
                if k2 != "rect":
                    continue
                ox = max(0, min(x1, rx1) - max(x0, rx0))
                oy = max(0, min(y1, ry1) - max(y0, ry0))
                if ox > 0 and oy > 0:
                    print(f"  OVERLAP {name}: {t[:50]!r} vs rect ({rx0:.0f},{ry0:.0f})-({rx1:.0f},{ry1:.0f}) {ox:.0f}x{oy:.0f}")
                    hits += 1
        print(f"  {name}: {hits} text-vs-later-rect overlaps")

    print("== 4. residual Latin runs in edition SVGs ==")
    for name in PAGES:
        texts, _ = svg_texts(os.path.join(ED_SVG, name + ".svg"))
        lat = sorted({t for _, _, _, t, _ in texts if re.search(r"[A-Za-z]", t)})
        print(f"  {name} ({len(lat)} Latin-bearing nodes):")
        for t in lat:
            print(f"    {t[:120]}")

    print("== 5. Traditional-independence cross-check ==")
    def charset(d):
        s = set()
        for f in sorted(os.listdir(d)):
            if f.endswith(".svg"):
                txt = open(os.path.join(d, f), encoding="utf-8").read()
                for t in re.findall(r"<text[^>]*>([^<]*)</text>", txt):
                    s |= {c for c in t if "\u4e00" <= c <= "\u9fff"}
        return s
    union = charset(W43_SVG) | charset(CORE_SVG)
    ed = charset(ED_SVG)
    outside = sorted(ed - union)
    print(f"  union chars: {len(union)}, edition chars: {len(ed)}, outside union: {len(outside)}")
    for c in outside:
        print(f"    outside: {c} U+{ord(c):04X}")
    # OpenCC s2t comparison (core KIT method): counts must match the core's
    # 51/26/3/1 pattern exactly, since removed furniture Chinese holds none
    # of 台/吃/表/群.
    import shutil, subprocess
    if shutil.which("opencc"):
        from collections import Counter
        for label, d in [("core", CORE_SVG), ("edition", ED_SVG)]:
            tot = Counter()
            for f in sorted(os.listdir(d)):
                if f.endswith(".svg"):
                    txt = open(os.path.join(d, f), encoding="utf-8").read()
                    vis = " ".join(re.findall(r"<text[^>]*>([^<]*)</text>", txt))
                    conv = subprocess.run(["opencc", "-c", "s2t"], input=vis,
                                          capture_output=True, text=True).stdout
                    for a, b in zip(vis, conv):
                        if a != b:
                            tot[(a, b)] += 1
            print(f"  s2t {label}: {dict(tot)} total {sum(tot.values())}")
    else:
        print("  s2t: opencc not installed, skipped")

    print("== 6. P7 phrases ==")
    alltext = ""
    for name in PAGES:
        texts, _ = svg_texts(os.path.join(ED_SVG, name + ".svg"))
        alltext += "".join(t for _, _, _, t, _ in texts)
    import re as _re
    src7 = open(os.path.join(ED_BUILD, "content7.py"), encoding="utf-8").read()
    quotes = _re.findall(r'\("「(.*?)」", "(.*?)", "(p\. \d)"\)', src7)
    for q, en, pg in quotes:
        # bare sentence: article occurrence (plain) + P7 occurrence (in 「」)
        n = alltext.count(q)
        print(f"  {pg} count={n} {'OK' if n == 2 else 'FAIL'} 「{q}」-> {en}")

    print("== 7. image payloads ==")
    for name in PAGES:
        def payloads(d):
            src = open(os.path.join(d, name + ".svg"), encoding="utf-8").read()
            return sorted(hashlib.sha256(base64.b64decode(m)).hexdigest()
                          for m in re.findall(r'data:image/[^;]+;base64,([A-Za-z0-9+/=]+)', src))
        c, e = payloads(CORE_SVG), payloads(ED_SVG)
        print(f"  {name}: core {len(c)} edition {len(e)} identical={c == e}")
        # credits: Photo: lines
        def credits(d):
            src = open(os.path.join(d, name + ".svg"), encoding="utf-8").read()
            return sorted(re.findall(r"<text[^>]*>(Photo:[^<]*)</text>", src))
        cc, ce = credits(CORE_SVG), credits(ED_SVG)
        if cc or ce:
            print(f"    credits identical={cc == ce} {ce}")


if __name__ == "__main__":
    main()
