import re, glob, html, json
BASE='/home/hatch/workspace/goals/lucernaread-social-media-operations'
ED=f'{BASE}/files/weekly-report-w45-pt-de/svg'
CO=f'{BASE}/files/weekly-report-w45-pt-core/svg'
W43=f'{BASE}/files/weekly-report-pt-de/svg'
def parse(path):
    t=open(path,encoding='utf-8').read()
    out=[]
    for m in re.finditer(r'<text([^>]*)>(.*?)</text>',t,re.S):
        a,raw=m.group(1),html.unescape(m.group(2))
        def g(k):
            mm=re.search(k+r'="([^"]+)"',a); return mm.group(1) if mm else None
        out.append({'x':float(g('x') or 0),'y':float(g('y') or 0),'size':g('font-size'),'bold':'700' in a,'anchor':g('text-anchor'),'t':raw})
    return out
def dump(path):
    return '\n'.join(f"{e['y']:7.1f} x={e['x']:7.1f} {e['t']}" for e in parse(path))
open('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/pt-de-proof/p7-ed.txt','w').write(dump(ED+'/p7-lingua.svg'))
open('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/pt-de-proof/p7-core.txt','w').write(dump(CO+'/p7-lingua.svg'))
# P7 word-box: find texts containing 'PALAVRA' / word box region; print P7 lines y 1500-2000 both
for label,path in [('ED',ED+'/p7-lingua.svg'),('CORE',CO+'/p7-lingua.svg')]:
    print('==== P7',label,'y 1000-2700 ====')
    for e in parse(path):
        if e['y']>=1000: print(f"{e['y']:7.1f} x={e['x']:7.1f} {e['t']}")
