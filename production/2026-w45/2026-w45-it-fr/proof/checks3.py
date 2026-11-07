import re, glob
from xml.etree import ElementTree as ET
from collections import Counter, defaultdict
G = '/home/hatch/workspace/goals/lucernaread-social-media-operations'
def nodes(p):
    t = ET.parse(p)
    return [(el.get('x'), el.get('y'), el.get('font-size'), el.text or '') for el in t.iter() if el.tag.endswith('text') and (el.text or '').strip()]
# Exercise expansion: pair number node with level chip on same baseline (builder method: baseline + x-offset)
# Simpler robust method: count number tokens in exercise areas per page, and level chips.
# We replicate builder's pairing: for each page, nodes matching r'^(\d+)\.$' with fs 24 are exercise numbers;
# level chip is a node 'A2'/'B1'/'B2' on same y (within 1px) with x near number x.
for pi in range(1, 9):
    f = sorted(glob.glob(G + f'/files/weekly-report-w45-it-fr/svg/p{pi}-*.svg'))[0]
    ns = nodes(f)
    nums = [(float(x), float(y), tx) for x, y, fs, tx in ns if re.fullmatch(r'\d+\.', tx) and fs == '24']
    chips = [(float(x), float(y), tx) for x, y, fs, tx in ns if tx in ('A2', 'B1', 'B2')]
    paired = {}
    for x, y, tx in nums:
        n = int(tx[:-1])
        cand = [c for c in chips if abs(c[1] - y) < 1.5 and 0 < c[0] - x < 120]
        paired[n] = cand[0][2] if cand else None
    cnt = Counter(v for v in paired.values())
    missing = [n for n, v in paired.items() if v is None]
    print(f"P{pi}: numbers={len(nums)} range={min(paired) if paired else '-'}-{max(paired) if paired else '-'} levels={dict(cnt)} unpaired={missing}")
    if pi == 8:
        # P8 exercise area is different (113-150 in ex flow, no chips?) - report separately
        pass
print()
# Golden sentences: 8 quotes from P7 FRASI block, count occurrences in joined edition text (exact quote form incl. curly quotes)
ed_text = []
for f in sorted(glob.glob(G + '/files/weekly-report-w45-it-fr/svg/*.svg')):
    ed_text += [tx for _, _, _, tx in nodes(f)]
joined = '\n'.join(ed_text)
p7 = nodes(sorted(glob.glob(G + '/files/weekly-report-w45-it-fr/svg/p7-*.svg'))[0])
quotes = [tx for _, _, fs, tx in p7 if tx.startswith('«') and fs == '21.5' and float(_) > 1700] if False else None
# FRASI quotes are fs 21.5 nodes with y>1720 and x in (65,989) starting with «
quotes = [tx for x, y, fs, tx in p7 if tx.startswith('«') and fs == '21.5' and float(y) > 1720]
print("FRASI quotes found:", len(quotes))
for q in quotes:
    print(f"  {q!r} count_in_joined={joined.count(q)}")
print()
# Model essay: P8 H section - find nodes after 'H' / model text; compare core vs edition word count
for lbl, pat in [('CORE', G+'/files/weekly-report-w45-it-core/svg/p8-*.svg'), ('ED', G+'/files/weekly-report-w45-it-fr/svg/p8-*.svg')]:
    f = sorted(glob.glob(pat))[0]
    ns = nodes(f)
    # model text is Italian prose lines after the '150.' note; locate by searching for known start? print P8 tail nodes y>2500 excluding footer/separators
    print(f"--- {lbl} P8 nodes y>2540 (excl footer) ---")
    for x, y, fs, tx in ns:
        if float(y) > 2540 and float(y) < 2600:
            print(f"  y={y} x={x} fs={fs} {tx!r}")
