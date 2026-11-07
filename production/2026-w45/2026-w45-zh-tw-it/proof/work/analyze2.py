# Analyze 2: freeze-regex CJK counts; P8 added runs; CJK char-sequence diffs;
# memory-trick sentence; P7/P8 reflow contexts.
import json, re, difflib
from collections import Counter

W = '/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-tw-it-proof/work/'
ed = json.load(open(W + 'ed.json'))
core = json.load(open(W + 'core.json'))
w43 = json.load(open(W + 'w43.json'))

FREEZE = re.compile(r'[\u2e80-\u9fff\u3040-\u30ff\uac00-\ud7af\uff00-\uffef]')
def fset(d):
    s = set()
    for pg in d.values():
        for t in pg['texts']:
            for ch in t['text']:
                if FREEZE.match(ch):
                    s.add(ch)
    return s
ed_f, core_f, w43_f = fset(ed), fset(core), fset(w43)
print('freeze-regex distinct: edition', len(ed_f), 'union(core,w43)', len(core_f | w43_f))
print('edition chars outside my earlier CJK range (freeze-only):',
      sorted(ed_f - set(ch for ch in ed_f if '\u4e00' <= ch <= '\u9fff' or '\u3400' <= ch <= '\u4dbf' or '\uf900' <= ch <= '\ufaff')))
print('freeze-outside-union:', sorted(ed_f - (core_f | w43_f)))

def cjk_runs(text):
    return re.findall(r'[\u4e00-\u9fff\u3400-\u4dbf\uf900-\ufaff]+', text)
print()
print('=== P8 added runs (full) ===')
cc, ce = Counter(), Counter()
for t in core['p8-test.svg']['texts']:
    for r in cjk_runs(t['text']):
        cc[r] += 1
for t in ed['p8-test.svg']['texts']:
    for r in cjk_runs(t['text']):
        ce[r] += 1
print('added:', dict(ce - cc))
print('removed (non-furniture, top 40):',
      {k: v for k, v in (cc - ce).most_common(40) if k not in ('版', '第', '共', '繁體中文週報', '繁體中文正文', '英語講解')})

print()
print('=== CJK char-sequence diff per page (document order) ===')
def seq(d, fn):
    out = []
    for t in d[fn]['texts']:
        for ch in t['text']:
            if '\u4e00' <= ch <= '\u9fff' or '\u3400' <= ch <= '\u4dbf' or '\uf900' <= ch <= '\ufaff':
                out.append(ch)
    return ''.join(out)
for fn in sorted(ed):
    a, b = seq(core, fn), seq(ed, fn)
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    blocks = [op for op in sm.get_opcodes() if op[0] != 'equal']
    print(fn, 'core-len', len(a), 'ed-len', len(b), 'diff-blocks', len(blocks))
    for tag, i1, i2, j1, j2 in blocks:
        print('  ', tag, 'core:', repr(a[max(0, i1 - 6):i2 + 6]), '-> ed:', repr(b[max(0, j1 - 6):j2 + 6]))

print()
print('=== Memory-trick sentence, full nodes around y=1355 (P7) ===')
for name, d in (('core', core), ('ed', ed)):
    print('--', name)
    for t in d['p7-lang.svg']['texts']:
        try:
            y = float(t['y'])
        except (TypeError, ValueError):
            continue
        if 1330 <= y <= 1420:
            print('  ', t['y'], repr(t['text']))
print()
print('=== P8 model paragraph lines ===')
for name, d in (('core', core), ('ed', ed)):
    print('--', name)
    for t in d['p8-test.svg']['texts']:
        if '南港展覽' in t['text'] or '探索廚房' in t['text'] or '薑母' in t['text'] or '購物清單' in t['text']:
            print('  ', t['y'], repr(t['text']))
