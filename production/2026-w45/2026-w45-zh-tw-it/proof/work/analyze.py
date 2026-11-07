# Read-only analysis over extracted text-node JSONs.
import json, re, sys, unicodedata
from collections import Counter

W = '/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-tw-it-proof/work/'
ed = json.load(open(W + 'ed.json'))
core = json.load(open(W + 'core.json'))
w43 = json.load(open(W + 'w43.json'))

def is_cjk(ch):
    return '\u4e00' <= ch <= '\u9fff' or '\u3400' <= ch <= '\u4dbf' or '\uf900' <= ch <= '\ufaff'

def cjk_set(d):
    s = set()
    for pg in d.values():
        for t in pg['texts']:
            for ch in t['text']:
                if is_cjk(ch):
                    s.add(ch)
    return s

def cjk_runs(text):
    return re.findall(r'[\u4e00-\u9fff\u3400-\u4dbf\uf900-\ufaff]+', text)

print('=== GATE 2: Traditional independence ===')
ed_set = cjk_set(ed); union = cjk_set(core) | cjk_set(w43)
print('edition distinct CJK:', len(ed_set), 'union distinct:', len(union))
outside = sorted(ed_set - union)
print('OUTSIDE union:', outside)
spot = list('邮说国龙马发对让为这听车门电话认识语学习发为')
hits = {}
for fn, pg in ed.items():
    for t in pg['texts']:
        for ch in set(t['text']):
            if ch in spot:
                hits.setdefault(ch, []).append((fn, t['text'][:80]))
print('simplified-spot hits:', {k: len(v) for k, v in hits.items()})
for k, v in hits.items():
    print('  ', k, v[:3])

print()
print('=== GATE 3: pure-CJK node multiset core vs edition ===')
for fn in sorted(ed):
    def pure(d):
        c = Counter()
        for t in d[fn]['texts']:
            tx = t['text']
            if any(is_cjk(ch) for ch in tx) and not re.search(r'[A-Za-z]', tx):
                c[tx] += 1
        return c
    cc, ce = pure(core), pure(ed)
    added = ce - cc; removed = cc - ce
    print(fn, 'pure-node added:', sum(added.values()), 'removed:', sum(removed.values()))
    for k, v in list(removed.items())[:10]:
        print('   REMOVED:', repr(k[:100]), v)
    for k, v in list(added.items())[:10]:
        print('   ADDED:', repr(k[:100]), v)

print()
print('=== GATE 3b: CJK-run multiset diff (removed runs only; added must be 0) ===')
for fn in sorted(ed):
    cc, ce = Counter(), Counter()
    for t in core[fn]['texts']:
        for r in cjk_runs(t['text']):
            cc[r] += 1
    for t in ed[fn]['texts']:
        for r in cjk_runs(t['text']):
            ce[r] += 1
    added = ce - cc; removed = cc - ce
    print(fn, 'run-added:', sum(added.values()), 'run-removed:', sum(removed.values()))
    for k, v in removed.most_common(25):
        print('   REMOVED RUN:', repr(k), v)

print()
print('=== Round-3 rewording: 封王 context ===')
for name, d in (('core', core), ('ed', ed)):
    for fn, pg in d.items():
        for t in pg['texts']:
            if '封王' in t['text']:
                print(name, fn, t['y'], repr(t['text'][:220]))
