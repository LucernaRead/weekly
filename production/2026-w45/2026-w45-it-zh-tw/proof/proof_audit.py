#!/usr/bin/env python3
"""Independent proof audit for W45 IT x ZH-TW. Read-only: parses SVG/source
text only, never imports content modules, never writes into files/ dirs."""
import re, sys, json, glob, html, hashlib
from collections import Counter
sys.path.insert(0, '/home/hatch/workspace/goals/lucernaread-social-media-operations/tools')
import occlusion_audit as OA

BASE = '/home/hatch/workspace/goals/lucernaread-social-media-operations'
CORE = BASE + '/files/weekly-report-w45-it-core/svg'
ED = BASE + '/files/weekly-report-w45-it-zh-tw/svg'
W43ED = BASE + '/files/weekly-report-it-zh-tw/svg'
ZHTWCORE = BASE + '/files/weekly-report-zh-tw-it/svg'
COREBUILD = BASE + '/hidden_files/weekly-report-w45-it-build'
EDBUILD = BASE + '/hidden_files/weekly-report-w45-it-zh-tw-build'
W43BUILD = BASE + '/hidden_files/weekly-report-it-zh-tw-build'
PAGES = ['p1-prima','p2-vita','p3-cultura','p4-sport','p5-giovani','p6-approfondimento','p7-lingua','p8-valutazione']
CJK = re.compile(r'[\u4e00-\u9fff]')
FREEZE_CJK = re.compile(r'[\u2e80-\u9fff\u3040-\u30ff\uac00-\ud7af\uff00-\uffef]')

def texts(path):
    s = open(path, encoding='utf-8').read()
    return [html.unescape(re.sub(r'<[^>]+>', '', c)) for c in re.findall(r'<text\b[^>]*>(.*?)</text>', s, re.S)], s

def joined(d):
    out = []
    for p in PAGES:
        t, _ = texts(f'{d}/{p}.svg'); out.append(' '.join(t))
    return out

print('=== 1. 桥接 scan: 8 SVG + 5 content ===')
for path in sorted(glob.glob(ED + '/*.svg')) + [f'{EDBUILD}/content{n}.py' for n in ['12','34','56','7','8']]:
    s = open(path, encoding='utf-8').read()
    print(f"  {path.split('/')[-1]}: 桥接={s.count('桥接')} 桥={s.count('桥')}")

print('=== 2. stripped non-CJK multiset diff per page (Italian freeze) ===')
for p in PAGES:
    tc, _ = texts(f'{CORE}/{p}.svg'); te, _ = texts(f'{ED}/{p}.svg')
    dc = Counter(CJK.sub('', t) for t in tc); de = Counter(CJK.sub('', t) for t in te)
    print(f'-- {p}: core-only {len(list((dc-de).elements()))} edition-only {len(list((de-dc).elements()))}')
    for t in (dc - de).elements(): print('   CORE-only:', repr(t))
    for t in (de - dc).elements(): print('   ED-only  :', repr(t))

print('=== 3. CJK accounting: freeze口径 vs 纯汉字口径 ===')
tot_f = tot_h = 0
for p in PAGES:
    tc, _ = texts(f'{CORE}/{p}.svg'); te, _ = texts(f'{ED}/{p}.svg')
    cc = Counter(ch for t in tc for ch in t if FREEZE_CJK.match(ch))
    ce = Counter(ch for t in te for ch in t if FREEZE_CJK.match(ch))
    add_f = sum((ce - cc).values())
    hc = Counter(ch for t in tc for ch in t if CJK.match(ch))
    he = Counter(ch for t in te for ch in t if CJK.match(ch))
    add_h = sum((he - hc).values())
    tot_f += add_f; tot_h += add_h
    print(f'  {p}: freeze新增={add_f} 纯汉字新增={add_h} 差额={add_f-add_h}')
    # list the non-Han freeze additions on this page
    nonhan = {ch: n for ch, n in (ce - cc).items() if not CJK.match(ch)}
    if nonhan: print(f'    非汉字freeze新增: {nonhan}')
print(f'  TOTAL freeze新增={tot_f} 纯汉字新增={tot_h} 差额={tot_f-tot_h}')

print('=== 4. quotes per page core->edition ===')
for p in PAGES:
    _, sc = texts(f'{CORE}/{p}.svg'); _, se = texts(f'{ED}/{p}.svg')
    row = {}
    for ch, name in [('“','ldquo'),('”','rdquo'),('「','lcorner'),('」','rcorner'),('«','laquo'),('»','raquo')]:
        row[name] = (sc.count(ch), se.count(ch))
    print(f'  {p}: ' + ' '.join(f'{k}={v[0]}->{v[1]}' for k, v in row.items() if v[0] or v[1]))

print('=== 5. union charset: W43 ITxZHTW ∪ W43 ZHTWxIT ===')
union = set()
for d in (W43ED, ZHTWCORE):
    for f in glob.glob(d + '/*.svg'):
        union |= set(CJK.findall(open(f, encoding='utf-8').read()))
print(f'  union size: {len(union)}')
edchars = Counter()
for p in PAGES:
    t, _ = texts(f'{ED}/{p}.svg')
    for x in t: edchars.update(CJK.findall(x))
novel = sorted(set(edchars) - union)
print(f'  edition distinct CJK: {len(edchars)}; NOT in union: {len(novel)} -> {novel}')
for ch in novel:
    ctxs = []
    for p in PAGES:
        t, _ = texts(f'{ED}/{p}.svg')
        for x in t:
            if ch in x: ctxs.append(f'{p}:{x}')
    print(f'    {ch}: ' + ' || '.join(ctxs[:3]))

print('=== 6. s2twp-variant scan (OpenCC) ===')
from opencc import OpenCC
conv = OpenCC('s2twp')
sus = {ch: conv.convert(ch) for ch in edchars if conv.convert(ch) != ch}
print(f'  variant chars: {sus}')
for ch in sus:
    ctxs = []
    for p in PAGES:
        t, _ = texts(f'{ED}/{p}.svg')
        for x in t:
            if ch in x: ctxs.append(f'{p}:{x}')
    print(f'    {ch}->{sus[ch]}: ' + ' || '.join(ctxs[:6]))
print(f"  只 count in edition: {sum(1 for p in PAGES for t,_ in [texts(f'{ED}/{p}.svg')] for x in t for _ in [0] if False)}")
alled = ''.join(''.join(texts(f'{ED}/{p}.svg')[0]) for p in PAGES)
print(f"  只 occurrences: {alled.count('只')} ; contexts:")
for p in PAGES:
    for x in texts(f'{ED}/{p}.svg')[0]:
        if '只' in x: print(f'    {p}: {x}')

print('=== 7. mainland-vocab scan ===')
pairs = [('代码','代碼'),('比赛项目','比賽項目'),('报道','報導'),('集市','市集'),('片语','片語'),('片語','詞組'),('把词组成','把詞組成'),('把詞組成','把詞組成'),
         ('软件','軟體'),('视频','影片'),('打印机','印表機'),('网络','網路'),('信息','資訊'),('数据','數據'),('周报','週報'),('意大利语','義大利語'),('意大利','義大利'),('概率','機率'),('搜索','搜尋')]
for sc, tc in pairs:
    print(f'  {sc}={alled.count(sc)} {tc}={alled.count(tc)}')
for w in ['週報','義大利語','義大利','數據','詞組','機率']:
    print(f'  TW-form {w}={alled.count(w)}')

print('=== 8. svglib diffs ===')
import difflib
def diffstat(a, b, label):
    la = open(a, encoding='utf-8').read().splitlines()
    lb = open(b, encoding='utf-8').read().splitlines()
    d = list(difflib.unified_diff(la, lb, lineterm=''))
    print(f'  {label}: {len(d)} diff lines')
    for line in d: print('   ', line)
diffstat(f'{COREBUILD}/svglib.py', f'{EDBUILD}/svglib.py', 'W45 core svglib -> W45 edition svglib')
diffstat(f'{W43BUILD}/svglib.py', f'{EDBUILD}/svglib.py', 'W43 edition svglib -> W45 edition svglib')

print('=== 9. P7 word-box definition + gloss source (static parse, no import) ===')
for f, label in [(f'{COREBUILD}/content7.py','core'), (f'{EDBUILD}/content7.py','edition')]:
    s = open(f, encoding='utf-8').read()
    m = re.search(r'wt\s*=\s*"([^"]*)"', s)
    print(f'  {label} wt: {m.group(1) if m else "NOT-FOUND"}')
    m2 = re.search(r'lt\s*=\s*"([^"]*)"', s)
    print(f'  {label} lt: {m2.group(1) if m2 else "NOT-FOUND"}')
# gloss() calls: find gloss( ... ) string literals per content file
def gloss_items(path):
    s = open(path, encoding='utf-8').read()
    items = []
    for m in re.finditer(r'gloss\(\s*"((?:[^"\\]|\\.)*)"', s):
        items.append(m.group(1))
    return items
for f in ['content12.py','content34.py','content56.py']:
    c = gloss_items(f'{COREBUILD}/{f}'); e = gloss_items(f'{EDBUILD}/{f}')
    print(f'  {f}: core gloss calls={len(c)} edition={len(e)}')
    for i,(a,b) in enumerate(zip(c,e)):
        ca = a.split('·'); cb = b.split('·')
        print(f'    call{i}: core items={len(ca)} edition items={len(cb)} equal={ca==cb}')
        if ca != cb:
            print(f'      CORE: {a}')
            print(f'      ED  : {b}')

print('=== 10. P7 gold sentences + (Pagina N) ===')
for d, label in [(CORE,'core'),(ED,'edition')]:
    js = joined(d)
    alltext = ' '.join(js)
    p7 = js[6]
    print(f'  {label} (Pagina N) in P7: {Counter(re.findall(r"\(Pagina \d+\)", p7))}')
    # gold sentences: extract P7 gold block? count each distinct P7-only Italian sentence occurrence in whole book
    print(f'  {label} P7 text count: {len(js[6])} chars')

print('=== 11. P8 keys full compare (p8.py extract, then first-segment check) ===')
sys.path.insert(0, BASE + '/tools')
import p8 as P8
for d, label in [(f'{CORE}/p8-valutazione.svg','core'),(f'{ED}/p8-valutazione.svg','edition')]:
    notes, keys = P8.extract_notes(d, 150) if hasattr(P8,'extract_notes') else (None, None)
    print(f'  {label}: extract via p8 module attrs: {[a for a in dir(P8) if not a.startswith("_")]}')
    break

print('=== 12. furniture vs W43 ===')
def find_text(d, pat):
    out = []
    for p in PAGES:
        t, s = texts(f'{d}/{p}.svg')
        for x in t:
            if re.search(pat, x): out.append((p, x))
    return out
print('  edition badge:', find_text(ED, r'義大利語正文'))
print('  edition footer count:', len(find_text(ED, r'La Lucerna · 義大利語週報 VOL\.2')))
print('  W43 footer:', find_text(W43ED, r'La Lucerna · 義大利語週報 VOL\.1')[:2])
print('  edition page lines:', find_text(ED, r'第 \d 版 / 共 8 版'))
print('  edition gloss prefix 譯注｜:', len(find_text(ED, r'譯注｜')), '講解｜:', find_text(ED, r'講解｜'))
print('  edition P8 head:', find_text(ED, r'RISPOSTE'))
print('  edition P8 separators:', find_text(ED, r'— 第 \d 版 —'))
print('  edition P8 band:', find_text(ED, r'VALUTAZIONE'))
# badge geometry from raw svg
for d, label in [(W43ED,'W43'),(ED,'W45')]:
    s = open(f'{d}/p1-prima.svg', encoding='utf-8').read()
    for m in re.finditer(r'<text[^>]*>([^<]*義大利語正文[^<]*)</text>', s):
        print(f'  {label} badge element: {s[max(0,m.start()-260):m.start()]} || {m.group(1)}')

print('=== 13. images: raster payload hash core vs edition ===')
def images(d):
    out = {}
    for p in PAGES:
        s = open(f'{d}/{p}.svg', encoding='utf-8').read()
        for m in re.finditer(r'(?:xlink:href|href)="data:image/[^;]+;base64,([^"]+)"', s):
            out.setdefault(p, []).append(hashlib.sha256(m.group(1).encode()).hexdigest()[:16])
    return out
ci, ei = images(CORE), images(ED)
print(f'  core: {ci}')
print(f'  edition: {ei}')
print(f'  equal: {ci==ei}')
for p in PAGES:
    t, _ = texts(f'{ED}/{p}.svg')
    for x in t:
        if 'Foto:' in x or 'Disegno' in x or 'dominio' in x or 'CC0' in x: print(f'  credit {p}: {x}')

print('=== 14. P7 disclosure joined + in-box geometry ===')
t7, s7 = texts(f'{ED}/p7-lingua.svg')
disc = [x for x in t7 if '編輯部示例信' in x or '最佳第 8 版作文' in x or '請寄來信' in x]
print('  disclosure fragments:', disc)
print('  joined:', ''.join(disc))
# find y/x of disclosure fragments in raw svg
for m in re.finditer(r'<text[^>]*x="([^"]+)"[^>]*y="([^"]+)"[^>]*>([^<]*?(?:編輯部示例信|最佳第 8 版作文|請寄來信)[^<]*)</text>', s7):
    print(f'  disclosure text at x={m.group(1)} y={m.group(2)}: {m.group(3)}')
# letter box: find rects near P7 reader garden? print all text y in P7 after LETTERE
print('  P7 letter tag present:', '(esempio della redazione)' in t7)

print('=== 15. ABSTRACT checks ===')
ab = open(BASE + '/files/weekly-report-w45-it-zh-tw/ABSTRACT.txt', encoding='utf-8').read()
print(f'  lines: {ab.count(chr(10))} (trailing newline only expected: {ab.endswith(chr(10))})')
print(f'  ascii dquote: {ab.count(chr(34))} ; text: {ab.strip()}')
print(f"  has 義大利語: {'義大利語' in ab} ; 150題: {'150' in ab} ; A2–B2: {'A2' in ab and 'B2' in ab} ; La Lucerna: {'La Lucerna' in ab}")

print('=== 16. level tags + exercise numbers from SVG ===')
for d, label in [(CORE,'core'),(ED,'edition')]:
    alltext = ' '.join(joined(d))
    print(f'  {label}: [A2]={alltext.count("[A2]")} [B1]={alltext.count("[B1]")} [B2]={alltext.count("[B2]")}')
    print(f'  {label}: A2→ etc variants: {Counter(re.findall(r"A2\s*→\s*B1|A2/B1/B2", alltext))}')

print('=== 17. transform-log / build residue checks ===')
tl = open(f'{EDBUILD}/transform-log.txt', encoding='utf-8').read()
print('  transform-log last lines:', tl.strip().splitlines()[-3:])
for f in ['transform.py','svglib.py']:
    s = open(f'{EDBUILD}/{f}', encoding='utf-8').read()
    print(f'  {f}: 重阳={s.count("重阳")} Double Ninth={s.count("Double Ninth")}')
for p in PAGES:
    t, _ = texts(f'{ED}/{p}.svg')
    for x in t:
        if '�' in x or '练习' in x: print(f'  RESIDUE? {p}: {x}')
print('  (no residue lines above = clean)')
print('=== 18. PDF page counts ===')
from pypdf import PdfReader
for f in ['La-Lucerna-VOL2-ZHTW.pdf','La-Lucerna-VOL2-ZHTW-web.pdf']:
    r = PdfReader(BASE + f'/files/weekly-report-w45-it-zh-tw/{f}')
    print(f'  {f}: {len(r.pages)} pages')
