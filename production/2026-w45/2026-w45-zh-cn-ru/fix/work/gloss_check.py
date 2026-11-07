# -*- coding: utf-8 -*-
"""Gloss gate: AST-extract gloss() string args from core build vs RU build,
split on '·', compare per-page item counts; verify every gloss headword
(CJK run in each item) present in the corresponding delivered page SVG.
Page attribution by call order within each file (proof table structure):
content12: box1->P1, rest->P2; content34: first 2 boxes->P3, rest->P4;
content56: first 2 boxes->P5, rest->P6; content7/8: none."""
import ast, re, sys

CORE = '/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-zhcn-build/'
RU = '/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-zh-cn-ru-build/'
SVG = '/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-ru/svg/'
PAGES = {'content12.py': ['p1', 'p2'], 'content34.py': ['p3', 'p4'],
         'content56.py': ['p5', 'p6'], 'content7.py': ['p7'], 'content8.py': ['p8']}
PAGEFILE = {'p1': 'p1-touiban.svg', 'p2': 'p2-shenghuo.svg', 'p3': 'p3-wenhua.svg',
            'p4': 'p4-tiyu.svg', 'p5': 'p5-qingnian.svg', 'p6': 'p6-shendu.svg',
            'p7': 'p7-ciyu.svg', 'p8': 'p8-ceyan.svg'}

def gloss_calls(build, fn):
    src = open(build + fn, encoding='utf-8').read()
    tree = ast.parse(src)
    out = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            f = node.func
            name = getattr(f, 'id', None) or getattr(f, 'attr', None)
            if name == 'gloss' and node.args and isinstance(node.args[0], ast.Constant):
                out.append(node.args[0].value)
    return out

def per_page(build):
    res = {}
    for fn, pages in PAGES.items():
        calls = gloss_calls(build, fn)
        counts = [len(c.split('·')) for c in calls]
        if fn == 'content12.py':
            res['p1'] = counts[:1]; res['p2'] = counts[1:]
        elif fn in ('content34.py', 'content56.py'):
            res[pages[0]] = counts[:2]; res[pages[1]] = counts[2:]
        else:
            res[pages[0]] = counts
    return res

core = per_page(CORE)
ru = per_page(RU)
ok = True
for p in ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8']:
    c, r = sum(core[p]), sum(ru[p])
    status = 'OK' if c == r else 'MISMATCH'
    if c != r:
        ok = False
    print(f'{p}: core {c} {core[p]} | ru {r} {ru[p]} -> {status}')

# headword presence in delivered SVGs (RU build gloss items)
CJK = re.compile(r'[\u4e00-\u9fff]+')
missing = []
for fn, pages in PAGES.items():
    calls = gloss_calls(RU, fn)
    # attribute boxes to pages the same way
    if fn == 'content12.py':
        boxpages = ['p1'] + ['p2'] * (len(calls) - 1)
    elif fn in ('content34.py', 'content56.py'):
        boxpages = [pages[0]] * 2 + [pages[1]] * (len(calls) - 2)
    else:
        boxpages = [pages[0]] * len(calls)
    for call, pg in zip(calls, boxpages):
        svg = open(SVG + PAGEFILE[pg], encoding='utf-8').read()
        for item in call.split('·'):
            for hw in CJK.findall(item.split('—')[0]):
                if hw not in svg:
                    missing.append((pg, hw))
print('missing headwords:', missing)
print('GLOSS GATE:', 'PASS' if ok and not missing else 'FAIL')
sys.exit(0 if ok and not missing else 1)
