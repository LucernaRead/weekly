#!/usr/bin/env python3
"""Round 2 completion — independent Korean wrap scan (window method) + word integrity.
NOTE: the canonical koscan script file was not preserved in either gate dir
(only its logs remain); this is an independent re-implementation of the
documented method (consecutive same-column lines, 10-45px baseline gap,
Hangul break; S3 = mid-word split with tail >= 3 syllables; orphan = final
line <= 1 syllable). Read-only.
"""
import re
from pathlib import Path
BASE=Path.home()/'workspace/goals/lucernaread-social-media-operations/files'
TEXT_RE=re.compile(r'<text\b([^>]*)>(.*?)</text>', re.S)
ATTR_RE=re.compile(r'(\w[\w-]*?)="([^"]*)"')
def is_hangul(ch): return '\uac00' <= ch <= '\ud7a3'
def load(ed):
    out=[]
    for pf in sorted((BASE/f'weekly-report-w46-en-{ed}/svg').glob('*.svg')):
        raw=pf.read_text(encoding='utf-8')
        for m in TEXT_RE.finditer(raw):
            attrs=dict(ATTR_RE.findall(m.group(1)))
            inner=re.sub(r'<[^>]+>','',m.group(2)).replace('&amp;','&')
            try: x=float(attrs.get('x','0')); y=float(attrs.get('y','0'))
            except ValueError: continue
            out.append({'page':pf.stem,'x':x,'y':y,'text':inner})
    return out
ko=load('ko')
print('ko text elements:',len(ko))
cands=[]
for a,b in zip(ko,ko[1:]):
    if a['page']!=b['page']: continue
    dy=b['y']-a['y']
    if not (10<=dy<=45): continue
    if abs(a['x']-b['x'])>1.0: continue
    # break between a and b: a ends with Hangul, b starts (after optional punct/paren) with Hangul
    t1=a['text'].rstrip(); t2=b['text'].lstrip()
    if not t1 or not is_hangul(t1[-1]): continue
    t2s=re.sub(r'^[\(（"\'«]','',t2)
    if not t2s or not is_hangul(t2s[0]): continue
    # head: trailing Hangul run of t1 (strip trailing punct first)
    m1=re.search(r'[\uac00-\ud7a3]+$', t1)
    head=m1.group(0) if m1 else ''
    m2=re.match(r'[\uac00-\ud7a3]+', t2s)
    tail=m2.group(0) if m2 else ''
    # no-space break? (t1 does not end with space/punct-space; t2 first token continues)
    nospace = not t1.endswith((' ','·','—','-'))
    cands.append({'page':a['page'],'y1':a['y'],'y2':b['y'],'head':head,'tail':tail,
                  'tail_n':len(tail),'nospace':nospace,'l1':t1[-40:],'l2':t2[:40:]})
print('CANDIDATES (same-x, 10-45 window, Hangul break):',len(cands))
for c in cands:
    print(f"  {c['page']} y={c['y1']}->{c['y2']} head={c['head']!r}({len(c['head'])}) tail={c['tail']!r}({c['tail_n']}) nospace={c['nospace']} :: {c['l1']!r} / {c['l2']!r}")
mid=[c for c in cands if c['nospace']]
print('no-space-break candidates:',len(mid),'max tail syllables:',max([c['tail_n'] for c in mid],default=0))
print('S3 candidates (nospace + tail>=3):',[c for c in mid if c['tail_n']>=3])
print()
print('===== B3 WORD INTEGRITY =====')
allt=' '.join(t['text'] for t in ko)
for w in ['솔퍼드','묵념해요','갈라쇼는 솔퍼드에서 생방송돼요','전교생이 2분 동안 묵념해요']:
    print(repr(w),'present intact:',w in allt,'count:',allt.count(w))
for t in ko:
    if '솔퍼드' in t['text'] or '묵념해요' in t['text']:
        print(f"  [{t['page']} x={t['x']} y={t['y']}] {t['text'][:120]!r}")
print()
print('===== ORPHAN FINAL LINES (grouped blocks, final line <=1 Hangul syllable) =====')
# group by page+x, consecutive dy<45 chains; final line = last in chain; count Hangul syllables in it
groups=[]; cur=[]
prev=None
for t in ko:
    if prev and t['page']==prev['page'] and abs(t['x']-prev['x'])<=1.0 and 0 < t['y']-prev['y'] < 45:
        cur.append(t)
    else:
        if cur: groups.append(cur)
        cur=[t]
    prev=t
if cur: groups.append(cur)
orph=0
for g in groups:
    last=g[-1]['text'].strip()
    ns=sum(1 for ch in last if is_hangul(ch))
    # only flag chains of >=2 lines whose final line is short Hangul-only-ish
    if len(g)>=2 and 0<ns<=1 and len(last)<=3:
        print('ORPHAN?',g[0]['page'],[x['y'] for x in g],repr(last)); orph+=1
print('orphan final lines:',orph)
print()
print('===== LINE-START ORPHAN PUNCT (ko) =====')
for t in ko:
    s=t['text'].lstrip()
    if s.startswith(('!','»','。',')','）')):
        print(f"  [{t['page']} x={t['x']} y={t['y']}] {t['text'][:90]!r}")
print('DONE verify2-koscan')
