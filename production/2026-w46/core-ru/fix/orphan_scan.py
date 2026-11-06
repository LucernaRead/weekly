# -*- coding: utf-8 -*-
"""Orphan-fragment scan (D2 class): grey 20.5pt instruction text stranded at a
column start in the exercise-flow top band, detached from its home line.
Reports every candidate with document-order context for adjudication.
Usage: orphan_scan.py <edition-dir>...  (reads svg/*.svg only)
Exit 0 = no candidates; exit 1 = candidates found (listed)."""
import re, sys, os, glob

TEXT_RE = re.compile(r'<text[^>]*x="([0-9.]+)"[^>]*y="([0-9.]+)"[^>]*font-size="([0-9.]+)"[^>]*?(?:fill="([^"]*)")?[^>]*>(.*?)</text>', re.S)

def nodes(svg):
    t = open(svg, encoding="utf-8").read()
    out = []
    for m in TEXT_RE.finditer(t):
        x, y, fs = float(m.group(1)), float(m.group(2)), float(m.group(3))
        fill = m.group(4) or ""
        txt = re.sub(r"<[^>]+>", "", m.group(5))
        out.append((x, y, fs, fill, txt))
    return out

def main():
    found = 0
    for ed in sys.argv[1:]:
        for svg in sorted(glob.glob(os.path.join(ed, "svg", "*.svg"))):
            ns = nodes(svg)
            for i, (x, y, fs, fill, txt) in enumerate(ns):
                # True orphan: the immediately preceding node in document order
                # is that 1st line at the bottom of the previous column
                # (x=65, y>2400, 20.5pt). A bridge directly under its own head
                # in the same column (e.g. P5 D) is a legitimate adjacent pair.
                # (Checked at every y, not only the 1600-1800 exercise band.)
                prev = ns[i - 1] if i else None
                is_orphan = bool(prev and prev[0] == 65.0 and prev[1] > 2400 and prev[2] == 20.5)
                if fs == 20.5 and x in (527.0, 989.0, 1451.0) and is_orphan:
                    print(f"ORPHAN {ed} {os.path.basename(svg)} x={x} y={y} fill={fill} text={txt!r}")
                    print(f"  prev: ({prev[0]},{prev[1]},{prev[2]}){prev[4]!r}")
                    found += 1
                elif fs == 20.5 and x in (527.0, 989.0, 1451.0) and 1600 <= y <= 1800:
                    print(f"band-hit (legitimate pair) {ed} {os.path.basename(svg)} x={x} y={y} text={txt!r}")
    print(f"TOTAL ORPHANS: {found}")
    return 1 if found else 0

if __name__ == "__main__":
    sys.exit(main())
