#!/usr/bin/env python3
"""Round 3: extract SVG texts for es/fr/zh-tw in the Round 2 texts/*.txt
format, then multiset-diff (page + text, positions ignored) against the
Round 2 extractions to prove the ONLY string changes are the two fixes.
Also: text.md Answers-section counts (unique 1..150) per edition."""
import re, sys
from pathlib import Path
from collections import Counter

TEXT_RE = re.compile(r'<text\b([^>]*)>(.*?)</text>', re.S)
ATTR_RE = re.compile(r'(\w[\w-]*?)="([^"]*)"')
def texts_of(p):
    raw = Path(p).read_text(encoding='utf-8', errors='replace')
    out = []
    for m in TEXT_RE.finditer(raw):
        attrs = dict(ATTR_RE.findall(m.group(1)))
        inner = re.sub(r'<[^>]+>', '', m.group(2)).replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"').replace('&apos;', "'")
        out.append({'x': attrs.get('x'), 'y': attrs.get('y'), 'size': attrs.get('font-size'),
                    'weight': attrs.get('font-weight'), 'anchor': attrs.get('text-anchor'), 'text': inner})
    return out

BASE = Path.home()/'workspace/goals/lucernaread-social-media-operations/files'
OUT = Path.home()/'workspace/goals/lucernaread-social-media-operations/hidden_files/w46/en-fix-round3/texts'
OUT.mkdir(parents=True, exist_ok=True)
for ed in ('es', 'fr', 'zh-tw'):
    eddir = BASE/f'weekly-report-w46-en-{ed}'
    lines = []
    for svg in sorted((eddir/'svg').glob('*.svg')):
        for i, t in enumerate(texts_of(svg)):
            lines.append(f"[{svg.stem}#{i} x={t['x']} y={t['y']} {t['size']}pt w={t['weight']} a={t['anchor']}] {t['text']}")
    (OUT/f'texts-{ed}.txt').write_text('\n'.join(lines)+'\n', encoding='utf-8')
    print(ed, len(lines))

def load(p):
    c = Counter()
    for line in open(p, encoding='utf-8'):
        m = re.match(r'^\[(\S+)#\d+ [^\]]*\] (.*)$', line.rstrip('\n'))
        if m: c[(m.group(1), m.group(2))] += 1
        else: c[('?', line)] += 1
    return c

R2 = Path.home()/'workspace/goals/lucernaread-social-media-operations/hidden_files/w46/en-proofread-gates-round2/texts'
for ed in ('es', 'fr', 'zh-tw'):
    a = load(R2/f'texts-{ed}.txt'); b = load(OUT/f'texts-{ed}.txt')
    d1, d2 = a-b, b-a
    print(f"== {ed}: only-Round2 {sum(d1.values())}, only-Round3 {sum(d2.values())}")
    for k, v in sorted(d1.items()): print('  R2-only', v, k)
    for k, v in sorted(d2.items()): print('  R3-only', v, k)

# text.md Answers counts
for ed in ('es', 'fr', 'zh-tw'):
    md = (BASE/f'weekly-report-w46-en-{ed}/2026-w46-en-{ed}.text.md').read_text(encoding='utf-8')
    ans = md.split('## Answers', 1)[1]
    nums = [int(m.group(1)) for m in re.finditer(r'^(\d+)\. \[', ans, re.M)]
    print(f"{ed} text.md Answers: n={len(nums)} unique={len(set(nums))} range={min(nums)}..{max(nums)} "
          f"complete={sorted(nums)==list(range(1,151))} header6={md.splitlines()[:6]}")
