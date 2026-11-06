import re, html, json
BASE='/home/hatch/workspace/goals/lucernaread-social-media-operations'
ED=f'{BASE}/files/weekly-report-w45-pt-de/svg'
CO=f'{BASE}/files/weekly-report-w45-pt-core/svg'
def parse(path):
    t=open(path,encoding='utf-8').read(); out=[]
    for m in re.finditer(r'<text([^>]*)>(.*?)</text>',t,re.S):
        a,raw=m.group(1),html.unescape(m.group(2))
        def g(k):
            mm=re.search(k+r'="([^"]+)"',a); return mm.group(1) if mm else None
        out.append({'x':float(g('x') or 0),'y':float(g('y') or 0),'size':g('font-size'),'t':raw})
    return out
def norm(s): return re.sub(r'\s+',' ',s).strip()
def pagetext(p): return norm(' '.join(e['t'] for e in parse(p)))
# phrases
p7=parse(ED+'/p7-lingua.svg')
quotes=[]; tags=[]
for i,e in enumerate(p7):
    if e['t'].startswith('«') and '»' in e['t']:
        # quote may span? quotes here are single lines (checked) except long one? print
        quotes.append(e['t'])
print("P7 quote lines:",len(quotes))
for q in quotes: print(' Q:',q)
allpages={n:pagetext(f'{ED}/{n}') for n in ['p1-capa.svg','p2-vida.svg','p3-cultura.svg','p4-esporte.svg','p5-jovens.svg','p6-aprofundamento.svg','p7-lingua.svg','p8-avaliacao.svg']}
alltxt=norm(' '.join(allpages.values()))
for q in quotes:
    qs=norm(q.strip('«»').strip())
    cnt=alltxt.count(qs)
    print(f"COUNT {cnt} :: {qs[:80]}")
    # per page presence
    pres=[n for n,t in allpages.items() if qs in t]
    print('   on:',pres)
# tag check: translation lines carry (Página N)
for e in p7:
    if 'Página' in e['t']: print(' TAGLINE:',e['t'][:120])
# P8 dump
print("==== P8 ED full text (sorted by y,x) ====")
p8=sorted(parse(ED+'/p8-avaliacao.svg'),key=lambda e:(e['y'],e['x']))
for e in p8: print(f"{e['y']:7.1f} x={e['x']:6.1f} {e['t']}")
