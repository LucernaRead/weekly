# -*- coding: utf-8 -*-
"""PT core -> PT x ZH-CN fan-out transform for W46 VOL.3 (furniture only).

The core edition IS the Simplified-Chinese-explanation edition (W45
precedent: the core was inserted as slug 2026-w46-pt-zh-cn). The
explanation layer is therefore UNCHANGED; only the pairing furniture
is set explicitly, mirroring the ZH-TW pattern in Simplified characters:
footer (pairing description) + P1 pairing badge (372 line). Subtitle,
page line, gloss prefix, disc strings, P7 geometry and P8 size all keep
core values. Print PDF stem unchanged: A-Lucerna-VOL3.pdf.
Run inside the already-copied build dir, once, on a pristine core copy.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))

def load(fn):
    with open(os.path.join(HERE, fn), encoding='utf-8') as f:
        return f.read()

def save(fn, txt):
    with open(os.path.join(HERE, fn), 'w', encoding='utf-8') as f:
        f.write(txt)

def sub(txt, old, new, fn=''):
    n = txt.count(old)
    assert n >= 1, f'{fn}: {old!r} not found'
    return txt.replace(old, new)

def line_replace(txt, anchor, newline, fn=''):
    lines = txt.split('\n')
    hits = [i for i, ln in enumerate(lines) if anchor in ln]
    assert len(hits) == 1, f'{fn}: anchor {anchor!r} hits {hits}'
    lines[hits[0]] = newline
    return '\n'.join(lines)

FILES = ['bslib4.py', 'content12.py', 'content34.py', 'content56.py',
         'content7.py', 'content8.py', 'render.py']

for fn in FILES:
    t = load(fn)
    if 'weekly-report-w46-pt-core' in t:
        t = t.replace('weekly-report-w46-pt-core', 'weekly-report-w46-pt-zh-cn')
        save(fn, t)

t = load('bslib4.py')
t = sub(t, 'A Lucerna · 葡萄牙语周报 VOL.3 · LUCERNA PORTUGUESE WEEKLY',
        'A Lucerna · 葡萄牙语周报 VOL.3 · 正文葡萄牙语 · 讲解简体中文', 'bslib4.py')
save('bslib4.py', t)

t = load('content12.py')
t = line_replace(t, 'p.text(975, 372,',
    'p.text(975, 372, "葡萄牙语正文 · 简体中文讲解 — 给简体中文读者的版本", 19.5, "sans", True, BRICK, anchor="middle")',
    'content12.py')
save('content12.py', t)
print('TRANSFORM COMPLETE')
