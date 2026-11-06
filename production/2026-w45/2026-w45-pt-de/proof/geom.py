import sys, re, html
sys.path.insert(0,'/home/hatch/workspace/goals/lucernaread-social-media-operations/tools')
import occlusion_audit as OA
BASE='/home/hatch/workspace/goals/lucernaread-social-media-operations'
ED=f'{BASE}/files/weekly-report-w45-pt-de/svg'; CO=f'{BASE}/files/weekly-report-w45-pt-core/svg'; W43=f'{BASE}/files/weekly-report-pt-de/svg'
def elements(path):
    t=open(path,encoding='utf-8').read(); els=[]
    for m in OA.TAG_RE.finditer(t):
        if m.group('tattrs') is not None:
            a=OA.parse_attrs(m.group('tattrs')); txt=OA.clean_text(m.group('tcontent'))
            els.append(('text',a,txt))
        else:
            els.append((m.group('tag'),OA.parse_attrs(m.group('attrs')),None))
    return els
def ink(a,txt):
    return OA.ink_box(txt,a.get('font-family'),float(a.get('font-size',20)),'700' in a.get('font-weight',''),float(a.get('x',0)),float(a.get('y',0)),a.get('text-anchor','start'))
print("=== FRAME / PAGE-EDGE scan (ink vs page 0..1950x0..2700, inner frame 40..1910x40..2660, frame lines x=28/1922/40/1910, y=28/2672/40/2660) ===")
for pg in ['p1-capa','p2-vida','p3-cultura','p4-esporte','p5-jovens','p6-aprofundamento','p7-lingua','p8-avaliacao']:
    bad=[]
    for kind,a,txt in elements(f'{ED}/{pg}.svg'):
        if kind!='text' or not txt.strip(): continue
        b=ink(a,txt)
        if not b: continue
        l,t_,r,bb=b
        if l<0 or t_<0 or r>1950 or bb>2700: bad.append(('EDGE',txt[:40],b))
        if l<40 or t_<40 or r>1910 or bb>2660:
            # footer baseline 2624 exempt only if footer text
            if not (float(a.get('y',0))==2624.0): bad.append(('INNERFRAME',txt[:40],b))
        for fx in (28,1922,40,1910):
            if l<fx<r and not (t_>2660): bad.append(('FRAME-X',fx,txt[:40],b))
        for fy in (28,2672,40,2660):
            if t_<fy<bb: bad.append(('FRAME-Y',fy,txt[:40],b))
    print(pg, 'violations:', len(bad))
    for v in bad[:20]: print('   ',v)
print("=== same-baseline ink gaps: P1 top band (y=92) ED vs CORE ===")
for label,d in [('ED',ED),('CORE',CO)]:
    tops=[]
    for kind,a,txt in elements(f'{d}/p1-capa.svg'):
        if kind=='text' and float(a.get('y',0))==92.0:
            tops.append((float(a.get('x',0)),a.get('text-anchor'),txt,ink(a,txt)))
    tops.sort(key=lambda z:z[3][0])
    print(label,[(t[2][:30],tuple(round(v,1) for v in t[3])) for t in tops])
    gaps=[round(tops[i+1][3][0]-tops[i][3][2],1) for i in range(len(tops)-1)]
    print(label,'gaps:',gaps)
print("=== P1 contents tight line: find 'Finados, o dia da memória' + level label on same baseline ===")
for label,d in [('ED',ED),('CORE',CO)]:
    for kind,a,txt in elements(f'{d}/p1-capa.svg'):
        if kind=='text' and ('Finados, o dia da memória' in txt or txt.strip() in ('A2→B1',) or 'A2' in txt and 'B1' in txt):
            print(label,f"y={a.get('y')} x={a.get('x')} anchor={a.get('text-anchor')} sz={a.get('font-size')} :: {txt} :: ink={tuple(round(v,2) for v in ink(a,txt))}")
print("=== P1 edition line width (34pt) ED vs W43 ===")
for label,path,needle in [('ED',f'{ED}/p1-capa.svg','PORTUGIESISCHE WOCHENZEITUNG'),('W43',f'{W43}/p1-capa.svg','PORTUGIESISCHE WOCHENZEITUNG')]:
    for kind,a,txt in elements(path):
        if kind=='text' and needle in txt:
            b=ink(a,txt); print(label,f"sz={a.get('font-size')} ink=({b[0]:.1f},{b[2]:.1f}) width={b[2]-b[0]:.1f} :: {txt[:60]}")
print("=== P2 band subtitle width ED vs W43 ===")
for label,path in [('ED',f'{ED}/p2-vida.svg'),('W43',f'{W43}/p2-vida.svg')]:
    for kind,a,txt in elements(path):
        if kind=='text' and float(a.get('y',0))==142.0 and float(a.get('x',0))>1500:
            b=ink(a,txt); print(label,f"ink=({b[0]:.1f},{b[2]:.1f}) width={b[2]-b[0]:.1f} :: {txt}")
print("=== P8 column bottoms ED (key lines y>1250, grouped by x) ===")
cols={}
for kind,a,txt in elements(f'{ED}/p8-avaliacao.svg'):
    if kind=='text' and float(a.get('y',0))>1250 and float(a.get('y',0))<2580:
        cols.setdefault(float(a.get('x',0)),[]).append((float(a.get('y',0)),txt))
for x in sorted(cols):
    last=max(cols[x]); print(f"col x={x}: lowest baseline={last[0]:.2f} clearance_to_2580={2580-last[0]:.2f} :: {last[1][:70]}")
print("=== P1 palavra gloss clearance: line + rule y ===")
for label,d in [('ED',ED),('CORE',CO)]:
    for kind,a,txt in elements(f'{d}/p1-capa.svg'):
        if kind=='text' and ('Feriadão' in txt and 'langes' in txt or 'Feriadão' in txt and '三天' in txt or 'feriadão' in txt.lower() and 'langes' in txt):
            print(label,f"y={a.get('y')} :: {txt} :: ink-bottom={ink(a,txt)[3]:.1f}")
    # rules: lines near y 1844?
    for kind,a,txt in elements(f'{d}/p1-capa.svg'):
        if kind=='line' and abs(float(a.get('y1',0))-1844)<30: print(label,'line y1=',a.get('y1'),'y2=',a.get('y2'),'x1=',a.get('x1'),'x2=',a.get('x2'))
print("=== P7 word box + letters box geometry ED ===")
els=elements(f'{ED}/p7-lingua.svg')
for kind,a,txt in els:
    if kind=='rect' and float(a.get('x',0))>1400:
        print(f"rect x={a.get('x')} y={a.get('y')} w={a.get('width')} h={a.get('height')} bottom={float(a.get('y',0))+float(a.get('height',0)):.1f}")
for kind,a,txt in els:
    if kind=='text' and txt and ('feriadão = langes' in txt or 'Beispiel der Redaktion' in txt or 'Anmerkung: Echte' in txt or 'Versprechen gilt' in txt):
        b=ink(a,txt); print(f"text y={a.get('y')} :: {txt[:60]} :: ink-bottom={b[3]:.1f} ink=({b[0]:.1f},{b[2]:.1f})")
print("=== P7 quotes last translation ink bottom vs next-issue box top ED ===")
for kind,a,txt in els:
    if kind=='text' and txt and ('Karte prüfen, gut schlafen' in txt or 'Erinnern heißt' in txt):
        print(f"text y={a.get('y')} :: {txt[:60]} :: ink-bottom={ink(a,txt)[3]:.1f}")
    if kind=='rect':
        y=float(a.get('y',0))
        if 2390<y<2420: print(f"rect x={a.get('x')} y={y} w={a.get('width')} h={a.get('height')}")
print("=== P6 chart labels coverage ED ===")
els6=elements(f'{ED}/p6-aprofundamento.svg')
for i,(kind,a,txt) in enumerate(els6):
    if kind=='text' and txt and txt.strip() in ('portões abertos','espera','prova'):
        b=ink(a,txt); area=(b[2]-b[0])*(b[3]-b[1]); cov=0.0
        for kind2,a2,_ in els6[i+1:]:
            if kind2=='rect':
                rx,ry,rw,rh=float(a2.get('x',0)),float(a2.get('y',0)),float(a2.get('width',0)),float(a2.get('height',0))
                ox=max(0,min(b[2],rx+rw)-max(b[0],rx)); oy=max(0,min(b[3],ry+rh)-max(b[1],ry))
                cov+=ox*oy
        print(f"label {txt!r} y={a.get('y')} ink={tuple(round(v,1) for v in b)} coverage={100*cov/area:.1f}%")
print("=== P6 chart label texts present? ===")
for kind,a,txt in els6:
    if kind=='text' and txt and any(k in txt for k in ['portões','espera','prova']): print(f"y={a.get('y')} x={a.get('x')} :: {txt}")
