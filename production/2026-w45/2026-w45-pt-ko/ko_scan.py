# -*- coding: utf-8 -*-
"""Standalone KO scan for PT x KO round 1: raw-corpus S3, S1, Stail."""
import re, sys, os, glob
ED = '/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-pt-ko'
BUILD = '/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-pt-ko-build'
HANG = re.compile(r'[\uac00-\ud7a3]')
def hang_n(s):
    return len(HANG.findall(s))
corpus = ''
for fn in ['bslib4.py', 'content12.py', 'content34.py', 'content56.py', 'content7.py', 'content8.py']:
    corpus += open(os.path.join(BUILD, fn), encoding='utf-8').read() + '\n'
START_PUNCT = set('.!?\u2026)]\u00bb\u300d,;:')
SEP = re.compile(r'^— 제 \d+ 면 —$')
def strip_tok(tok):
    return re.sub(r'^[^\uac00-\ud7a3]+|[^\uac00-\ud7a3]+$', '', tok)
s3, s1, stail, minor = [], [], [], []
for path in sorted(glob.glob(os.path.join(ED, 'svg', '*.svg'))):
    pg = os.path.basename(path)
    src = open(path, encoding='utf-8').read()
    els = []
    for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"([^>]*)>([^<]*)</text>', src):
        anch = 'end' if 'text-anchor="end"' in m.group(5) else ('middle' if 'text-anchor="middle"' in m.group(5) else 'start')
        els.append({'x': float(m.group(1)), 'y': float(m.group(2)), 's': m.group(6), 'anchor': anch})
    by_x = {}
    for e in els:
        if e['anchor'] != 'start' or not e['s'].strip():
            continue
        by_x.setdefault(round(e['x'], 1), []).append(e)
    for x, lines in by_x.items():
        lines.sort(key=lambda e: e['y'])
        for e1, e2 in zip(lines, lines[1:]):
            gap = e2['y'] - e1['y']
            if gap < 10 or gap > 45:
                continue
            s1t, s2t = e1['s'].strip(), e2['s'].strip()
            if not s1t or not s2t or s2t.startswith('\u00b7') or SEP.match(s2t):
                continue
            if re.match(r'^\d+\. ', s2t):
                continue
            if hang_n(s2t) >= 1 and s2t[0] in START_PUNCT:
                s1.append((pg, round(e2['y'], 1), s2t[:60]))
            if hang_n(s2t) >= 1 and hang_n(s2t) <= 2:
                stail.append((pg, round(e2['y'], 1), s2t[:60], s1t[-40:]))
            last, first = s1t.split(' ')[-1], s2t.split(' ')[0]
            last_c, first_c = strip_tok(last), strip_tok(first)
            if (hang_n(last_c) >= 1 and hang_n(first_c) >= 1
                    and first and first[0] not in START_PUNCT
                    and (last_c + first_c) in corpus):
                if hang_n(first_c) >= 3:
                    s3.append((pg, round(e1['y'], 1), s1t[-40:], s2t[:50], hang_n(first_c)))
                else:
                    minor.append((pg, round(e1['y'], 1), s1t[-40:], s2t[:50], hang_n(first_c)))
print(f"S3 (tail>=3, raw corpus): {len(s3)}")
for h in s3: print('  S3', h)
print(f"S1 (line-start orphan punct): {len(s1)}")
for h in s1: print('  S1', h)
print(f"Stail (1-2 syllable continuations): {len(stail)}")
for h in stail: print('  ST', h)
print(f"minor splits (tail 1-2): {len(minor)}")
for h in minor: print('  MI', h)
