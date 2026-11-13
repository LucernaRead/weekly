# -*- coding: utf-8 -*-
"""Export 2026-w47-ja-it.text.md from the final SVGs (one <text>
element per line, in document order). Created 2026-11-11
(fix round 1): the original export script was absent from this
clone (same gap as en/fr, whose scripts were reconstructed the
same way). Validated: byte-identical reproduction of the pre-fix
.text.md from the pre-fix SVGs. Usage (from the build dir):
    python3 export-textmd-it.py [build-dir, default: this dir]
"""
import re, sys, os, html

BASE = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
ORDER = ['p1-hyoushi', 'p2-kurashi', 'p3-bunka', 'p4-supotsu',
         'p5-wakamono', 'p6-fukayomi', 'p7-kotoba', 'p8-tesuto']

lines = ['# 2026-w47-ja-it', '', 'Week: 2026-W47 (16–22 Nov 2026)', '']
for i, name in enumerate(ORDER, 1):
    t = open(os.path.join(BASE, 'svg', name + '.svg'), encoding='utf-8').read()
    texts = re.findall(r'<text[^>]*>(.*?)</text>', t, re.S)
    lines.append(f'## Page {i}')
    lines.append('')
    for x in texts:
        lines.append(html.unescape(x))
    lines.append('')
out = os.path.join(BASE, '2026-w47-ja-it.text.md')
open(out, 'w', encoding='utf-8').write('\n'.join(lines))
print('wrote', out, len(lines), 'lines')
