# Analyze 3: P8 paren discipline, furniture, readers corner, golden sentences,
# images, credits.
import json, re
from collections import Counter

W = '/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-tw-it-proof/work/'
ed = json.load(open(W + 'ed.json'))
core = json.load(open(W + 'core.json'))
w43 = json.load(open(W + 'w43.json'))
HAN = re.compile(r'[\u4e00-\u9fff]')

print('=== P8 paren discipline (edition P8) ===')
p8 = ed['p8-test.svg']['texts']
full_paren = [t for t in p8 if '（' in t['text'] or '）' in t['text']]
print('P8 nodes with full-width parens:', len(full_paren))
for t in full_paren[:10]:
    print('  ', t['y'], repr(t['text'][:120]))
han_in_paren = []
for t in p8:
    for m in re.finditer(r'\(([^)]*)\)', t['text']):
        if HAN.search(m.group(1)):
            han_in_paren.append((t['y'], t['text'][:120], m.group(1)[:40]))
print('Han inside half-width parens (P8):', len(han_in_paren))
for h in han_in_paren[:10]:
    print('  ', h)
seps = [t['text'] for t in p8 if 'Pagina' in t['text']]
print('P8 separators:', seps)
print('P8 writing key line:', [t['text'] for t in p8 if t['text'].startswith('150.')])
print('full-width ＋ in edition P8:', sum(1 for t in p8 if '＋' in t['text']))
print('full-width ＋ in edition all pages:', {fn: sum(1 for t in pg['texts'] if '＋' in t['text']) for fn, pg in ed.items()})
print('shùzì notes:')
for fn, pg in ed.items():
    for t in pg['texts']:
        if 'zhìnéng' in t['text'] or 'rengong' in t['text'].lower():
            print('  ', fn, t['y'], repr(t['text'][:160]))
print('W43 P8 separators:', [t['text'] for t in w43['p8-test.svg']['texts'] if 'Pagina' in t['text']][:3])
print('W43 P8 paren sample:', [t['text'] for t in w43['p8-test.svg']['texts'] if t['text'].startswith('1. ')][:2])
print('W43 P8 full-width parens:', sum(1 for t in w43['p8-test.svg']['texts'] if '（' in t['text'] or '）' in t['text']))

print()
print('=== P1 badge three-way ===')
for name, d in (('core', core), ('w43', w43), ('ed', ed)):
    for t in d['p1-front.svg']['texts']:
        if t['y'] in ('378', '378.0') or 'TESTI IN CINESE' in t['text'] or '繁體中文正文' in t['text']:
            print(name, t)
            break

print()
print('=== Footers (edition, all pages) ===')
for fn, pg in ed.items():
    foots = [t for t in pg['texts'] if t['y'] == '2624' or (t['y'] and float(t['y']) > 2600)]
    for t in foots:
        print(fn, t['y'], t['size'], repr(t['text'][:130]))
print('=== W43 footers (P1) ===')
for t in w43['p1-front.svg']['texts']:
    if t['y'] and float(t['y']) > 2600:
        print(t['y'], t['size'], repr(t['text'][:130]))

print()
print('=== Box titles / gloss prefix ===')
for s in ['本週句式 · Struttura settimanale', '本週一詞 · Parola settimanale']:
    found = [(fn, t['y']) for fn, pg in ed.items() for t in pg['texts'] if t['text'] == s]
    print(repr(s), '->', found)
print('gloss prefix Nota count:', sum(1 for pg in ed.values() for t in pg['texts'] if t['text'].startswith('Nota — ')))
print('gloss prefix Notes count (must be 0):', sum(1 for pg in ed.values() for t in pg['texts'] if t['text'].startswith('Notes')))
print('P8 heads:', [t['text'] for t in ed['p8-test.svg']['texts'] if '測驗與答案' in t['text'] or 'Test e risposte' in t['text'] or 'Risposte' in t['text'] or 'Tutte le note' in t['text']][:6])

print()
print('=== Readers corner ===')
for name, d in (('core', core), ('ed', ed)):
    print('--', name)
    for t in d['p7-lang.svg']['texts']:
        if '延期披露' in t['text'] or 'Deferral notice' in t['text'] or 'Avviso di rinvio' in t['text'] or 'Scrivici' in t['text'] or 'L\'angolo dei lettori' in t['text'] or '編輯範例' in t['text']:
            print('  ', t['y'], repr(t['text'][:200]))
print('core disclosure lines (Traditional, y-sorted):')
for t in sorted([t for t in core['p7-lang.svg']['texts'] if '延期披露' in t['text'] or 'VOL.1曾預告' in t['text'] or '未收到可刊登' in t['text'] or '仍刊登編輯範例' in t['text'] or '下一期見' in t['text']], key=lambda t: float(t['y'])):
    print('  ', t['y'], repr(t['text']))
print('ed disclosure lines (Traditional, y-sorted):')
for t in sorted([t for t in ed['p7-lang.svg']['texts'] if '延期披露' in t['text'] or 'VOL.1曾預告' in t['text'] or '未收到可刊登' in t['text'] or '仍刊登編輯範例' in t['text'] or '下一期見' in t['text']], key=lambda t: float(t['y'])):
    print('  ', t['y'], repr(t['text']))

print()
print('=== Golden sentences (edition counts, all pages concatenated) ===')
gold = ['用手機轉帳、掃碼付款、網上買保險，都是金融科技', '123個國家及城市、1,600個攤位',
        '需要才買，不要為了折扣買一堆用不到的東西', '在高雄，鋼鐵也能變成舞台',
        '福隆的夏天，在10月26日畫下句點', '6比0完封兄弟，龍隊拋下紅色彩帶',
        '250家店家一起討糖', '旅展首日中午12點才開門']
alltext = {fn: ' '.join(t['text'] for t in pg['texts']) for fn, pg in ed.items()}
for g in gold:
    pages = [fn for fn, tx in alltext.items() if g in tx]
    print(repr(g), 'pages:', pages)
print('P7 golden nodes + tags:')
for t in ed['p7-lang.svg']['texts']:
    if any(g in t['text'] for g in gold) or re.match(r'^p\.\d', t['text']):
        print('  ', t['y'], repr(t['text'][:110]))

print()
print('=== Images ===')
for fn in sorted(ed):
    print(fn, 'ed:', [(im['w'], im['h'], im['sha'][:16]) for im in ed[fn]['images']],
          'core:', [(im['w'], im['h'], im['sha'][:16]) for im in core[fn]['images']])
print('=== Credits ===')
for fn, pg in ed.items():
    for t in pg['texts']:
        if 'Photo:' in t['text']:
            print(fn, repr(t['text']))
