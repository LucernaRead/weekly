#!/usr/bin/env python3
"""Round 3 post-fix checks: rendered P3 title-slot measurement (es/fr) from
the actual SVG <text> elements, using each edition's own svglib metrics."""
import re, sys, html
BASE = '/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-en-%s'
BUILD = '/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-en-%s-build'
import importlib
TEXT_RE = re.compile(r'<text x="([0-9.\-]+)" y="([0-9.\-]+)" font-family="([^"]+)" font-size="([0-9.]+)"([^>]*)>([^<]*)</text>')
for ed in ('es', 'fr'):
    sys.path.insert(0, BUILD % ed)
    import svglib
    importlib.reload(svglib)
    svg = open((BASE % ed) + '/svg/p3-culture.svg', encoding='utf-8').read()
    titles = [(float(m.group(1)), float(m.group(2)), html.unescape(m.group(6)))
              for m in TEXT_RE.finditer(svg) if float(m.group(2)) == 873.0]
    print(f"== {ed} P3 y=873 title elements: {len(titles)}")
    for x, y, s in titles:
        w = svglib.text_w(s, "sans", True, 23)
        f = svglib._font("sans", True, 23)
        l, t, r, b = f.getbbox(s)
        ink_right = x + r
        print(f"  x={x} y={y} advance={w:.1f}px ink_right={ink_right:.1f} (box right edge 1885) "
              f"{'OVERFLOW' if w > 416.0 else 'fits'}  {s!r}")
    # box rect for the P3 col-3 box: find rect containing the title
    assert len(titles) == 1, titles
    sys.path.pop(0)
print("SLOT = 416.0px (box x=1451 w=434, title x=1469)")
