#!/usr/bin/env python3
"""Round 3 key audit (verify3). Read-only. Independent of p8.py code path
for letter keys (raw-SVG parse), plus registry recount, counts, golden
phrases, P6 chart, P1 bars, masthead, native-script scans.
"""
import re, json, html, sys
from pathlib import Path
from collections import Counter
BASE = Path.home()/'workspace/goals/lucernaread-social-media-operations/files'
HF = Path.home()/'workspace/goals/lucernaread-social-media-operations/hidden_files/w46'
GATE = HF/'en-proofread-gates-round3'
TEXT_RE = re.compile(r'<text\b([^>]*)>(.*?)</text>', re.S)
ATTR_RE = re.compile(r'(\w[\w-]*?)="([^"]*)"')
def texts_of(p):
    raw = Path(p).read_text(encoding='utf-8', errors='replace')
    out=[]
    for m in TEXT_RE.finditer(raw):
        attrs=dict(ATTR_RE.findall(m.group(1)))
        out.append({'x':attrs.get('x'),'y':attrs.get('y'),'size':attrs.get('font-size'),
                    'fam':attrs.get('font-family'),'text':html.unescape(re.sub(r'<[^>]+>','',m.group(2)))})
    return out
def joined(eddir):
    parts=[]
    for svg in sorted((Path(eddir)/'svg').glob('*.svg')):
        parts.append(' '.join(t['text'] for t in texts_of(svg)))
    return ' '.join(parts)

print('===== A. REGISTRY RECOUNT =====')
reg=json.loads((HF/'en-core/registry.json').read_text(encoding='utf-8'))
nums=[e['n'] for e in reg]
print('entries', len(reg), 'unique', len(set(nums)), 'complete 1..150:', sorted(nums)==list(range(1,151)), 'all keyed:', all('key' in e and e['key'] for e in reg))
perpage=Counter(); perlevel=Counter()
for e in reg:
    perpage[e.get('page')]+=1; perlevel[e.get('level')]+=1
print('per-page:', dict(sorted(perpage.items(), key=lambda kv: str(kv[0]))))
print('per-level:', dict(perlevel))
print('keys 1..150:', {str(e['n']): e['key'] for e in reg if e['n'] in (24,25,26,27,38,39,40,41,56,57,58,59,74,75,76,77,141,142,143,144)})

print()
print('===== B. TEXT.MD ANSWERS COUNTS (all 4 incl core) =====')
for ed,fn in [('core','2026-w46-en-zh-cn.text.md'),('es','2026-w46-en-es.text.md'),('fr','2026-w46-en-fr.text.md'),('zh-tw','2026-w46-en-zh-tw.text.md')]:
    d='weekly-report-w46-en-core' if ed=='core' else f'weekly-report-w46-en-{ed}'
    md=(BASE/d/fn).read_text(encoding='utf-8')
    ans=md.split('## Answers',1)[1]
    found=[int(m.group(1)) for m in re.finditer(r'^(\d+)\. \[', ans, re.M)]
    print(ed, 'n=',len(found),'unique=',len(set(found)),'complete=',sorted(found)==list(range(1,151)))

print()
print('===== C. INDEPENDENT RAW-SVG LETTER PARSE (core + 3 editions) =====')
# p8keys JSONs are produced by the p8.py CLI separately (verify3-p8keys-*.json);
# this section uses ONLY the raw parse, compared against the registry letters.
regk={str(e['n']): e['key'] for e in reg}
letter_nums=[n for n,v in regk.items() if len(v)==1 and v in 'ABCD']
print('single-letter keys in registry:', len(letter_nums), letter_nums)
pat=re.compile(r"(?<!\d)(\d{1,3})\. ([A-D])(?=[\s·\(\),;。：、！？（]|$)")
bad=0; total=0
for name in ['core','es','fr','zh-tw']:
    d=BASE/('weekly-report-w46-en-core' if name=='core' else f'weekly-report-w46-en-{name}')
    s=(d/'svg/p8-exercices.svg').read_text(encoding='utf-8')
    els=re.findall(r'<text x="([^"]+)" y="([^"]+)"[^>]*>([^<]*)</text>', s)
    els=[(float(x),float(y),html.unescape(t)) for x,y,t in els if float(y)>1850]
    cols={}
    for x,y,t in els: cols.setdefault(round(x),[]).append((y,t))
    txt=' '.join(' '.join(t for _,t in sorted(cols[x])) for x in sorted(cols))
    got={m.group(1): m.group(2) for m in pat.finditer(txt)}
    for n in letter_nums:
        total+=1
        if got.get(n)!=regk[n]:
            bad+=1; print(f'  MISMATCH {name} #{n}: registry {regk[n]!r} printed {got.get(n)!r}')
    print(name, 'letters found:', sum(1 for n in letter_nums if n in got), '/', len(letter_nums))
print(f'TOTAL letter checks: {total}, mismatches: {bad}')

print()
print('===== D. P8 PRINTED KEYS vs REGISTRY (from verify3-p8keys JSONs) =====')
for name in ['core','es','fr','zh-tw']:
    p=GATE/f'verify3-p8keys-{name}.json'
    if not p.exists(): print(name, 'p8keys JSON MISSING (run CLI first)'); continue
    keys=json.loads(p.read_text())['keys']
    diffs=[(n,regk[n],keys.get(n)) for n in regk if regk[n]!=keys.get(n)]
    print(name, 'printed keys n=',len(keys),'diffs-vs-registry:',[d[0] for d in diffs])
    for n,a,b in diffs: print(f'   {n}: registry={a!r} printed={b!r}')

print()
print('===== E. CLOZE OPTIONS 112-119 (from core P8 SVG) =====')
s=(BASE/'weekly-report-w46-en-core/svg/p8-exercices.svg').read_text(encoding='utf-8')
for t in texts_of(BASE/'weekly-report-w46-en-core/svg/p8-exercices.svg'):
    if re.match(r'11[2-9]\. \[', t['text']): print(' ', t['text'])
print('  expected: 112 B Wednesday / 113 A poppy / 114 C silence / 115 B Eleven / 116 A Pudsey / 117 C will / 118 B going / 119 A still')

print()
print('===== F. MATCHING BLOCKS (stems+options from core text.md, keys from registry) =====')
md=(BASE/'weekly-report-w46-en-core/2026-w46-en-zh-cn.text.md').read_text(encoding='utf-8')
blocks=[('P2 D (24-27)',24),('P3 C (38-41)',38),('P4 C (56-59)',56),('P5 C (74-77)',74),('P8 F (141-144)',141)]
for label,start in blocks:
    print(f'-- {label}: keys', {n: regk[str(n)] for n in range(start,start+4)})

print()
print('===== G. P7 GOLDEN PHRASES verbatim (8 sentences) =====')
golden=[
 'On Wednesday, November 11, at eleven o\'clock in the morning, something quiet happens across the English-speaking world.',
 'At 11 a.m. on November 11, 1918, the guns of the First World War fell silent.',
 'For two minutes, nobody speaks.',
 'Christmas is still six weeks away.',
 'One Sunday is not enough — good thing the week has seven days.',
 'The total will still be there in the morning — and so will the kindness.',
 'Patience is part of the system, not a failure of it.',
 'There were no results to print — and this paper invents none.',
]
def norm(s): return re.sub(r'\s+',' ',s).strip()
for name in ['core','es','fr','zh-tw']:
    d=BASE/('weekly-report-w46-en-core' if name=='core' else f'weekly-report-w46-en-{name}')
    p7=norm(' '.join(t['text'] for t in texts_of(d/'svg/p7-langue.svg')))
    whole=norm(joined(d))
    ok7=sum(1 for g in golden if norm(g) in p7)
    oka=sum(1 for g in golden if norm(g) in whole)
    print(name, f'golden in P7: {ok7}/8, in whole issue: {oka}/8')
    for g in golden:
        if norm(g) not in p7: print('   MISSING from P7:', g)

print()
print('===== H. P6 CHART + P1 BARS =====')
for name in ['core','es','fr','zh-tw']:
    d=BASE/('weekly-report-w46-en-core' if name=='core' else f'weekly-report-w46-en-{name}')
    p6=(d/'svg/p6-politique.svg').read_text(encoding='utf-8')
    rects=re.findall(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*fill="([^"]*)"', p6)
    print(name, 'P6 rects total:', len(rects))
    p1=(d/'svg/p1-front.svg').read_text(encoding='utf-8')
    bars=[]
    for m in re.finditer(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*fill="(#[0-9a-fA-F]+)"', p1):
        x,y,w,h,fill=m.groups()
        if float(w)>50 and float(h)<40: bars.append((float(w),fill))
    print(name, 'P1 wide bars (w,fill):', bars)

print()
print('===== I. MASTHEAD (SVG font-size + badge/footer) =====')
for name in ['core','es','fr','zh-tw']:
    d=BASE/('weekly-report-w46-en-core' if name=='core' else f'weekly-report-w46-en-{name}')
    p1=texts_of(d/'svg/p1-front.svg')
    mast=[t for t in p1 if t['text'].strip()=='The Lucerna']
    print(name, 'masthead elements:', [(t['size'],t['x'],t['y']) for t in mast])
    badge=[t['text'] for t in p1 if 'WEEKLY' in t['text'] or '英語正文' in t['text'] or 'ENGLISCHER' in t['text'] or 'texto' in t['text'].lower() or 'en anglais' in t['text'].lower()]
    print('   badge/tagline candidates:', badge[:3])
    foot=set()
    for svg in sorted((d/'svg').glob('*.svg')):
        for t in texts_of(svg):
            if t['y']=='2624': foot.add(t['text'])
    print('   footer y=2624 texts:', sorted(foot))

print()
print('===== J. NATIVE-SCRIPT SCANS =====')
simpl_only=set('说读让为国学动词来发过时见长门问题语话译注讲解将发生事承诺改原形')
for name in ['es','fr']:
    d=BASE/f'weekly-report-w46-en-{name}'
    txt=joined(d)
    import unicodedata
    nonlatin=sorted(set(c for c in txt if ord(c)>127 and not ('\u0400'<=c<='\u04FF')))
    print(name, 'non-Latin chars in all SVG texts:', ''.join(nonlatin)[:200])
for name in ['zh-tw']:
    d=BASE/f'weekly-report-w46-en-{name}'
    txt=joined(d)
    hits={c: txt.count(c) for c in simpl_only if c in txt}
    print(name, 'simplified-only char hits:', hits)
    print(name, 'Traditional markers present:', {c: txt.count(c) for c in '動詞原形改寫承諾將發生的事來' if c in txt})
print('DONE verify3-keys')
