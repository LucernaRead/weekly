#!/usr/bin/env python3
"""Round 2 completion proofreader — independent verification checks (read-only).
Reads prior extraction texts/*.txt AND parses SVGs directly (second path).
Writes only stdout (captured to verify2-checks.log). No edition file touched.
"""
import re, json, subprocess
from pathlib import Path
from collections import Counter

HOME = Path.home()
BASE = HOME/'workspace/goals/lucernaread-social-media-operations/files'
GATE = HOME/'workspace/goals/lucernaread-social-media-operations/hidden_files/w46/en-proofread-gates-round2'
TEXTS = GATE/'texts'
EDS = ['core','de','es','fr','it','ja','ko','nl','pt','ru','zh-tw']
EDDIR = {'core':'weekly-report-w46-en-core'}
for e in EDS[1:]:
    EDDIR[e] = f'weekly-report-w46-en-{e}'

LINE_RE = re.compile(r'^\[(p\d+-\w+)#(\d+) x=(\S+) y=(\S+) (\S+)pt w=(\S+) a=(\S+)\] (.*)$')
def load(ed):
    out=[]
    for line in (TEXTS/f'texts-{ed}.txt').read_text(encoding='utf-8').splitlines():
        m=LINE_RE.match(line)
        if not m:
            out.append({'page':'?','idx':-1,'x':0,'y':0,'size':'?','text':line,'raw':line}); continue
        out.append({'page':m.group(1),'idx':int(m.group(2)),'x':float(m.group(3)),'y':float(m.group(4)),
                    'size':m.group(5),'weight':m.group(6),'anchor':m.group(7),'text':m.group(8),'raw':line})
    return out
ALL={e:load(e) for e in EDS}

TEXT_RE = re.compile(r'<text\b([^>]*)>(.*?)</text>', re.S)
ATTR_RE = re.compile(r'(\w[\w-]*?)="([^"]*)"')
def svg_texts(ed, pagefile):
    raw=(BASE/EDDIR[ed]/'svg'/pagefile).read_text(encoding='utf-8')
    out=[]
    for m in TEXT_RE.finditer(raw):
        attrs=dict(ATTR_RE.findall(m.group(1)))
        inner=re.sub(r'<[^>]+>','',m.group(2)).replace('&amp;','&').replace('&lt;','<').replace('&gt;','>').replace('&quot;','"').replace('&apos;',"'")
        out.append({'x':attrs.get('x'),'y':attrs.get('y'),'size':attrs.get('font-size'),'text':inner})
    return out

def show(ed, pred, label, limit=40):
    hits=[t for t in ALL[ed] if pred(t)]
    print(f'-- {ed} {label}: {len(hits)}')
    for t in hits[:limit]:
        print(f"   [{t['page']}#{t['idx']} x={t['x']} y={t['y']} {t['size']}pt] {t['text']}")
    return hits

print('===== A. LONE-CHAR SCAN (extraction path) =====')
for ed in EDS:
    for t in ALL[ed]:
        s=t['text'].strip()
        if s in ('»','。') or (len(s)==1 and s in '.,;:!?)]})'):
            print(f'LONE {ed} [{t["page"]}#{t["idx"]} x={t["x"]} y={t["y"]}] {s!r} full={t["text"]!r}')
print('A done (no output above = none found except listed).')
print()
print('===== A2. LONE-CHAR SCAN (direct SVG path, all pages) =====')
for ed in EDS:
    for pf in sorted((BASE/EDDIR[ed]/'svg').glob('*.svg')):
        for t in svg_texts(ed, pf.name):
            if t['text'].strip() in ('»','。'):
                print(f'LONE-SVG {ed} {pf.name} x={t["x"]} y={t["y"]} {t["text"]!r}')
print('A2 done.')
print()
print('===== B4. P7 toolbox 1843 lines =====')
for ed in EDS:
    show(ed, lambda t: '1843' in t['text'] and t['page'].startswith('p7-'), 'P7 1843')
print()
print('===== B5. P7 editor-note lines (core/zh-tw) + 你的 scan =====')
for ed in ['core','zh-tw']:
    show(ed, lambda t: ('来信' in t['text'] or '來信' in t['text']) and t['page'].startswith('p7-'), 'P7 letter lines')
    show(ed, lambda t: '你的' in t['text'] or '你的' in t['text'] or '你的' in t['text'], 'any 你的 (all pages)')
    # zh-tw variant chars: 你的 in TC is same glyphs 你的; also check 請把你的
    hits=[t for t in ALL[ed] if '你的' in t['text']]
    print(f'   {ed} 你的 total hits: {len(hits)}')
print()
print('===== B6. P2 will-bridge lines =====')
for ed in EDS:
    show(ed, lambda t: '動詞原形' in t['text'] or '动词' in t['text'] or ('will +' in t['text'] and t['page'].startswith('p2-')), 'P2 will bridge')
print()
print('===== B1. P6 HOW LONG titles =====')
for ed in EDS:
    show(ed, lambda t: 'HOW LONG' in t['text'], 'HOW LONG')
print()
print('===== M1. FINAL TEST lines =====')
for ed in EDS:
    show(ed, lambda t: 'FINAL TEST' in t['text'], 'FINAL TEST')
print()
print('===== M2. Gloss-prefix scan =====')
for ed in EDS:
    pats={'fr':'Note |','ko':'해설 —','zh-tw':'譯注｜','de':'Anmerkung |','core':'译注｜'}
    hits=[t for t in ALL[ed] if any(p in t['text'] for p in ['Note | Note |','해설 — 해설 —','譯注｜譯注｜','译注｜译注｜'])]
    print(f'-- {ed} DOUBLED prefix hits: {len(hits)}')
    for t in hits: print(f"   [{t['page']}#{t['idx']}] {t['text'][:90]}")
    # single-prefix first-lines on P2-P6
    if ed in pats:
        p=pats[ed]
        c=sum(1 for t in ALL[ed] if t['text'].startswith(p) and not t['page'].startswith(('p1-','p7-','p8-')))
        print(f'   {ed} P2-P6 lines starting {p!r}: {c}')
        for t in ALL[ed]:
            if t['text'].startswith(p) and not t['page'].startswith(('p1-','p7-','p8-')):
                print(f"   [{t['page']}#{t['idx']}] {t['text'][:110]}")
print()
print('===== M3. de call-a-race wordings =====')
for t in ALL['de']:
    if 'Rennen entscheiden' in t['text'] or 'Ergebnis verkünden' in t['text']:
        print(f"   [{t['page']}#{t['idx']}] {t['text'][:160]}")
print('counts: old =', sum(1 for t in ALL['de'] if 'ein Rennen entscheiden' in t['text']),
      ' new =', sum(1 for t in ALL['de'] if 'das Ergebnis verkünden' in t['text']))
print()
print('===== M4 + es/fr. P3 box titles (y=873) =====')
for ed in EDS:
    show(ed, lambda t: t['y']==873.0 and t['page'].startswith('p3-'), 'P3 y873')
print()
print('===== K. GENERIC SHORT-TEXT SCAN (stripped len<=2, all editions) =====')
for ed in EDS:
    for t in ALL[ed]:
        s=t['text'].strip()
        if 0 < len(s) <= 2 and not s.replace(' ','').isalnum():
            print(f'SHORT {ed} [{t["page"]}#{t["idx"]} x={t["x"]} y={t["y"]}] {s!r}')
print('K done.')
print()
print('===== KO GLOSS GROUPS (final-line check) =====')
def gloss_groups(ed, prefix):
    ts=sorted([t for t in ALL[ed] if t['page'].startswith(('p2-','p3-','p4-','p5-','p6-'))], key=lambda t:(t['page'],t['x'],t['y']))
    groups=[]
    cur=None
    for t in ts:
        if t['text'].startswith(prefix):
            if cur: groups.append(cur)
            cur=[t]
        elif cur and t['x']==cur[-1]['x'] and 0 < t['y']-cur[-1]['y'] < 40:
            cur.append(t)
        else:
            if cur: groups.append(cur)
            cur=None
    if cur: groups.append(cur)
    return groups
for ed,prefix in [('ko','해설 —'),('fr','Note |'),('zh-tw','譯注｜講解｜')]:
    print(f'-- {ed} gloss groups: ')
    for g in gloss_groups(ed,prefix):
        last=g[-1]['text']
        print(f"   {g[0]['page']} n={len(g)} first={g[0]['text'][:60]!r} LAST={last!r} lastlen={len(last)}")
print()
print('===== SCRIPT SCANS =====')
def script_counts(s):
    c=Counter()
    for ch in s:
        o=ord(ch)
        if '\u4e00' <= ch <= '\u9fff': c['Han']+=1
        elif '\u3040' <= ch <= '\u309f': c['Hiragana']+=1
        elif '\u30a0' <= ch <= '\u30ff': c['Katakana']+=1
        elif '\uac00' <= ch <= '\ud7a3': c['Hangul']+=1
        elif '\u0400' <= ch <= '\u04ff': c['Cyrillic']+=1
    return dict(c)
for ed in EDS:
    allt=''.join(t['text'] for t in ALL[ed])
    print(ed, script_counts(allt), 'total chars', len(allt))
print()
print('===== CREDITS / BADGE / FOOTER / MASTHEAD =====')
credits=['Claude Monet','Horace Nicholls','John Leech','Frank R. Snyder','Kenneth C. Zirkel']
for ed in EDS:
    allt=' '.join(t['text'] for t in ALL[ed])
    print(ed, 'credits:', {c:(c in allt) for c in credits})
    foots=[t for t in ALL[ed] if t['y']==2624.0]
    print('  footer y=2624 lines:', len(foots), '| pages:', sorted({t['page'] for t in foots}))
    for t in foots[:1]: print('   footer e.g.:', t['text'][:130])
    p1=[t for t in ALL[ed] if t['page'].startswith('p1-')]
    mast=[t for t in p1 if t['idx']==4]
    badge=[t for t in p1 if t['idx']==5]
    print('  P1#4 masthead:', [(t['size'],t['text'][:80]) for t in mast])
    print('  P1#5 badge/tagline:', [(t['size'],t['text'][:110]) for t in badge])
print()
print('===== GOLDEN PHRASES (joined per-page text) =====')
gold=[
 "On Wednesday, November 11, at eleven o'clock in the morning, something quiet happens across the English-speaking world.",
 "At 11 a.m. on November 11, 1918, the guns of the First World War fell silent.",
 "For two minutes, nobody speaks.",
 "Christmas is still six weeks away.",
 "One Sunday is not enough — good thing the week has seven days.",
 "The total will still be there in the morning — and so will the kindness.",
 "Patience is part of the system, not a failure of it.",
 "There were no results to print — and this paper invents none.",
]
pages={'1':'p1-front','2':'p2-life','3':'p3-culture','4':'p4-sport','5':'p5-jeunesse','6':'p6-politique'}
total_ok=0; total=0
for ed in EDS:
    for gi,g in enumerate(gold,1):
        pg=pages[str([1,1,2,3,4,5,6,6][gi-1])]
        joined=re.sub(r'\s+',' ',' '.join(t['text'] for t in ALL[ed] if t['page']==pg))
        ok=g in joined; total+=1; total_ok+=ok
        print(ed, gi, pg, 'OK' if ok else 'MISSING', g[:45])
print(f'GOLDEN {total_ok}/{total}')
print()
print('===== P1 SEARCHES BARS =====')
RECT_RE=re.compile(r'<rect x="([0-9.]+)" y="([0-9.]+)" width="([0-9.]+)" height="([0-9.]+)"[^>]*fill="([^"]*)"')
for ed in EDS:
    svg=(BASE/EDDIR[ed]/'svg'/'p1-front.svg').read_text(encoding='utf-8',errors='replace')
    bars=[]
    for m in RECT_RE.finditer(svg):
        x,y,w,h,fill=float(m.group(1)),float(m.group(2)),float(m.group(3)),float(m.group(4)),m.group(5)
        if x>=1470 and 600<=y<=1250 and 30<=w<=420 and 10<=h<=30:
            bars.append((round(y),round(w),fill))
    bars.sort()
    widths=[b[1] for b in bars]
    print(ed, bars, 'strictly decreasing:', widths==sorted(widths,reverse=True) and len(set(widths))==len(widths))
print()
print('===== REGISTRY RE-MEASURE =====')
reg=json.loads((HOME/'workspace/goals/lucernaread-social-media-operations/hidden_files/w46/en-core/registry.json').read_text(encoding='utf-8'))
ns=[it['n'] for it in reg]
print('n=',len(reg),'unique=',len(set(ns)),'range=',min(ns),max(ns),'missing=',sorted(set(range(1,151))-set(ns)),'dup=',[k for k,v in Counter(ns).items() if v>1])
print('per-page:',dict(sorted(Counter(it['page'] for it in reg).items())))
print('levels:',dict(sorted(Counter(it['level'] for it in reg).items())))
print('all keyed (non-empty key):',all(it.get('key') for it in reg))
print()
print('===== TEXT.MD ANSWERS COUNT + HEADERS =====')
for ed in EDS:
    slug='2026-w46-en-zh-cn' if ed=='core' else f'2026-w46-en-{ed}'
    p=BASE/EDDIR[ed]/f'{slug}.text.md'
    txt=p.read_text(encoding='utf-8')
    ans=txt.split('## Answers',1)[1] if '## Answers' in txt else ''
    nums=re.findall(r'^(\d+)\.\s*\[', ans, flags=re.M)
    print(ed, 'answers entries:', len(nums), 'unique:', len(set(nums)), 'first6lines:', txt.splitlines()[:6])
print()
print('===== ABSTRACT CHECKS =====')
for ed in EDS:
    p=BASE/EDDIR[ed]/'ABSTRACT.txt'
    raw=p.read_bytes(); txt=raw.decode('utf-8')
    lines=txt.splitlines()
    print(ed, 'bytes=',len(raw),'lines=',len(lines),'trailingNL=',txt.endswith('\n'),
          'asciiDQ=',('"' in txt),'has150=',('150' in txt),'hasLucerna=',('Lucerna' in txt),
          'hasA2B2=',('A2' in txt and 'B2' in txt))
    if ed=='ko':
        print('   ko codepoints around Munich:', [hex(ord(c)) for c in txt if c in '뮌댦헨'], 'has 뮌헨:', '뮌헨' in txt, 'has 댦:', '댦' in txt)
print()
print('===== PDF CHECKS =====')
for ed in EDS:
    for kind in ['web','print']:
        pdf=BASE/EDDIR[ed]/('The-Lucerna-VOL3-web.pdf' if kind=='web' else 'The-Lucerna-VOL3.pdf')
        size=pdf.stat().st_size
        info=subprocess.run(['pdfinfo',str(pdf)],capture_output=True,text=True)
        pages_m=re.search(r'Pages:\s*(\d+)',info.stdout)
        tout=subprocess.run(['pdftotext',str(pdf),'-'],capture_output=True)
        print(ed, kind, 'bytes=',size, '<=7MB(web):', size<=7*1024*1024 if kind=='web' else '-', 'pages=',pages_m.group(1) if pages_m else '?', 'pdftotext_bytes=',len(tout.stdout))
print('DONE verify2-checks')
