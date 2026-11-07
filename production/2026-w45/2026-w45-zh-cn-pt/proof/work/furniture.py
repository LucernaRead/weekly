# -*- coding: utf-8 -*-
import re, os
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files")

def nodes(path):
    s = open(path, encoding="utf-8").read()
    out = []
    for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"([^>]*)>([^<]*)</text>', s):
        x, y, fam, sz, rest, t = m.groups()
        out.append((float(x), float(y), fam, float(sz), '700' in rest, t))
    return out

def show(name, path, needles):
    ns = nodes(path)
    print('===', name, os.path.basename(path))
    for nd in needles:
        hits = [n for n in ns if nd in n[5]]
        if not hits:
            print(f"  {nd[:60]!r} -> NOT FOUND")
        for h in hits[:2]:
            print(f"  {nd[:40]!r} -> x={h[0]} y={h[1]} fam={h[2]} size={h[3]} bold={h[4]} full={h[5][:120]!r}")

cases = [
    ('core', BASE + '/weekly-report-w45-zhcn-core/svg/p1-touiban.svg'),
    ('W43', BASE + '/weekly-report-zh-cn-pt/svg/p1-touiban.svg'),
    ('ed', BASE + '/weekly-report-w45-zh-cn-pt/svg/p1-touiban.svg'),
]
for name, path in cases:
    show(name, path, ['SEMANÁRIO CHINÊS', '简体中文版', 'TEXTOS EM CHINÊS', '简体中文正文 · 英语讲解', 'Leia chinês de verdade', 'Read the real China', '每周读中文', 'Leia a China de verdade'])
    ns = nodes(path)
    badges = [n for n in ns if 'LEITORES DE LÍNGUA' in n[5] or 'English-speaking readers' in n[5]]
    print('  BADGE:', badges)
    # footer: nodes with y>2600
    foot = [n for n in ns if n[1] > 2600]
    print('  FOOTER nodes:', [(n[1], n[3], n[5][:130]) for n in foot[:4]])
    pageline = [n for n in ns if 'Página 1 de 8' in n[5] or '第 1 版' in n[5]]
    print('  PAGELINE:', pageline)

# P8 heads/separators + footers on p8
for name, path in [('core', BASE + '/weekly-report-w45-zhcn-core/svg/p8-ceyan.svg'),
                   ('W43', BASE + '/weekly-report-zh-cn-pt/svg/p8-ceyan.svg'),
                   ('ed', BASE + '/weekly-report-w45-zh-cn-pt/svg/p8-ceyan.svg')]:
    ns = nodes(path)
    print('=== P8', name)
    for nd in ['答案 ·', 'Gabarito', 'Página', 'Page', 'Todas as notas', 'All notes']:
        hits = [n for n in ns if nd in n[5]]
        for h in hits[:4]:
            print(f"  {nd!r} -> y={h[1]} size={h[3]} {h[5][:130]!r}")
    # dash vs paren sample: first 3 key lines
    keys = [n for n in ns if re.match(r'^\d+\. ', n[5])]
    print('  sample key lines:', [k[5][:100] for k in keys[:3]])
    print('  writing key line:', [k[5][:100] for k in keys if k[5].startswith('150.')][:2])
