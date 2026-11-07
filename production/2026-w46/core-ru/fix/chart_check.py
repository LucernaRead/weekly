# -*- coding: utf-8 -*-
"""P6 chart check: bars at x=685 (MX+620), height 30, OLIVE fill — widths must
be 600/343/286/200 for 42/24/20/14% (14.29 px/pt), values sum to 100%."""
import re, sys, os, glob

def main():
    ok = True
    for ed in sys.argv[1:]:
        svg = os.path.join(ed, "svg", "p6-razbor.svg")
        t = open(svg, encoding="utf-8").read()
        bars = []
        for m in re.finditer(r'<rect x="685(?:\.0)?" y="([0-9.]+)" width="([0-9.]+)" height="30"[^>]*fill="#3e4c2a"', t):
            bars.append(float(m.group(2)))
        labels = re.findall(r">(\d+)%<", t)
        print(f"{os.path.basename(ed)}: bars={bars} pct_labels={labels} sum={sum(int(v) for v in labels)}")
        if bars != [600.0, 343.0, 286.0, 200.0]:
            print("  <-- BAR MISMATCH"); ok = False
        if sum(int(v) for v in labels) != 100:
            print("  <-- SUM MISMATCH"); ok = False
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
