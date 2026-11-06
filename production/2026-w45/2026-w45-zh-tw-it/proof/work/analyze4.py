# Analyze 4: refined P8 key-section discipline, P5 AI form, frozen + counts,
# readers line 2 + Italian disclosure, golden recount (no-separator join) + tags,
# P4 credit wrap.
import json, re

W = '/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-tw-it-proof/work/'
ed = json.load(open(W + 'ed.json'))
core = json.load(open(W + 'core.json'))
HAN = re.compile(r'[\u4e00-\u9fff]')

print('=== P8 KEY section only (y >= 1328) ===')
keys = [t for t in ed['p8-test.svg']['texts'] if t['y'] and float(t['y']) >= 1328]
print('key-section nodes:', len(keys))
print('full-width parens in key section:', [t['text'][:100] for t in keys if '（' in t['text'] or '）' in t['text']])
hip = []
for t in keys:
    for m in re.finditer(r'\(([^)]*)\)', t['text']):
        if HAN.search(m.group(1)):
            hip.append(t['text'][:100])
print('Han inside half-width parens in key section:', hip)
print('Han chars anywhere in key-section paren contents (both widths):',
      [t['text'][:100] for t in keys if re.search(r'（[^）]*[\u4e00-\u9fff]', t['text'])])
print('key-section nodes identical to core key-section nodes?')
ckeys = [t for t in core['p8-test.svg']['texts'] if t['y'] and float(t['y']) >= 1328]
print('core key nodes:', len(ckeys), 'ed key nodes:', len(keys))
# stems with full-width parens: identical core vs ed?
for name, d in (('core', core), ('ed', ed)):
    fw = [(t['y'], t['text']) for t in d['p8-test.svg']['texts'] if '（' in t['text']]
    print(name, 'P8 full-width-paren nodes:', len(fw))
print('stem full-width nodes equal sets:', sorted(t['text'] for t in core['p8-test.svg']['texts'] if '（' in t['text']) == sorted(t['text'] for t in ed['p8-test.svg']['texts'] if '（' in t['text']))

print()
print('=== AI-variant forms (P5 vs P8) ===')
for fn in ('p5-youth.svg', 'p6-deep.svg'):
    for t in ed[fn]['texts']:
        if 'zhìnéng' in t['text'] or 'IA' in t['text'] and 'finanz' in t['text']:
            print(fn, t['y'], repr(t['text'][:200]))
for fn in ('p5-youth.svg', 'p6-deep.svg'):
    for t in core[fn]['texts']:
        if '人工智慧' in t['text'] and ('＋' in t['text'] or 'AI' in t['text']):
            print('core', fn, t['y'], repr(t['text'][:200]))
print('=== frozen ＋ counts core vs ed ===')
for fn in sorted(ed):
    c = sum(1 for t in core[fn]['texts'] if '＋' in t['text'])
    e = sum(1 for t in ed[fn]['texts'] if '＋' in t['text'])
    print(fn, 'core', c, 'ed', e)

print()
print('=== Readers corner line 2 + Italian disclosure full ===')
for t in ed['p7-lang.svg']['texts']:
    if '讀者來信和第8版最佳作文' in t['text']:
        print('line2:', t['y'], repr(t['text']))
for t in sorted(ed['p7-lang.svg']['texts'], key=lambda t: float(t['y'])):
    y = float(t['y'])
    if 1630 <= y <= 1760:
        print('ed P7', t['y'], repr(t['text'][:220]))
print('--- core same band ---')
for t in sorted(core['p7-lang.svg']['texts'], key=lambda t: float(t['y'])):
    y = float(t['y'])
    if 1630 <= y <= 1760:
        print('core P7', t['y'], repr(t['text'][:220]))

print()
print('=== Golden recount, no-separator join ===')
gold = ['用手機轉帳、掃碼付款、網上買保險，都是金融科技', '123個國家及城市、1,600個攤位',
        '需要才買，不要為了折扣買一堆用不到的東西', '在高雄，鋼鐵也能變成舞台',
        '福隆的夏天，在10月26日畫下句點', '6比0完封兄弟，龍隊拋下紅色彩帶',
        '250家店家一起討糖', '旅展首日中午12點才開門']
for g in gold:
    hits = []
    for fn, pg in ed.items():
        tx = ''.join(t['text'] for t in pg['texts'])
        hits.append((fn, tx.count(g)))
    print(repr(g), [h for h in hits if h[1] > 0], 'total', sum(h[1] for h in hits))
print('=== P7 golden area nodes (all nodes y 1860-2340) ===')
for t in sorted(ed['p7-lang.svg']['texts'], key=lambda t: (float(t['y']), t['x'] or '')):
    y = float(t['y'])
    if 1860 <= y <= 2345:
        print(' ', t['y'], t['x'], repr(t['text'][:120]))

print()
print('=== P4 credit wrap (ed vs core) ===')
for name, d in (('core', core), ('ed', ed)):
    print('--', name)
    for t in d['p4-sport.svg']['texts']:
        if 'Photo:' in t['text'] or 'Commons)' in t['text']:
            print('  ', t['y'], repr(t['text']))
