#!/usr/bin/env python3
"""Dump shipped explanation-layer strings: edition SVG texts minus core SVG texts
(multiset difference, document order), P1-P7 only. P8 handled separately."""
import re, html, pathlib
from collections import Counter
BASE = pathlib.Path.home()/'workspace/goals/lucernaread-social-media-operations/files'
OUT = pathlib.Path.home()/'workspace/goals/lucernaread-social-media-operations/hidden_files/w46/de-proofread-gates/added'
OUT.mkdir(exist_ok=True)
PAGES = ['p1-front.svg','p2-leben.svg','p3-kultur.svg','p4-sport.svg','p5-jugend.svg','p6-vertiefung.svg','p7-sprache.svg']
def texts(slug, pg):
    s = (BASE/f'weekly-report-w46-{slug}/svg/{pg}').read_text(encoding='utf-8')
    s = re.sub(r'data:image[^"\']*', 'IMG', s)
    return [html.unescape(re.sub(r'<[^>]+>', '', c)).strip() for c in re.findall(r'<text[^>]*>(.*?)</text>', s, re.S)]
core = {pg: Counter(texts('de-core', pg)) for pg in PAGES}
for slug in ['de-en','de-es','de-fr','de-it','de-ja','de-ko','de-nl','de-pt','de-ru','de-zh-tw']:
    lines = []
    for pg in PAGES:
        rem = Counter(texts(slug, pg)) - core[pg]
        # document order: walk edition texts, emit when count remaining
        left = dict(rem)
        lines.append(f'===== {pg} =====')
        for t in texts(slug, pg):
            if left.get(t, 0) > 0:
                lines.append(t)
                left[t] -= 1
    (OUT/f'{slug}-added-p1p7.txt').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(slug, 'added P1-P7 strings:', len(lines) - 7)
