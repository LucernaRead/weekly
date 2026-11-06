import re, sys, json, glob
from xml.etree import ElementTree as ET
NS = {'s': 'http://www.w3.org/2000/svg'}
def texts(path):
    t = ET.parse(path); out = []
    for el in t.iter():
        tag = el.tag.split('}')[-1]
        if tag == 'text' and (el.text or '').strip():
            out.append({'text': el.text, 'x': el.get('x'), 'y': el.get('y'),
                        'fs': el.get('font-size'), 'fam': el.get('font-family')})
    return out
def cjk(s):
    return [c for c in s if '\u4e00' <= c <= '\u9fff' or '\u3400' <= c <= '\u4dbf']
G = '/home/hatch/workspace/goals/lucernaread-social-media-operations'
for label, pat in [('edition', G+'/files/weekly-report-w45-it-fr/svg/*.svg'),
                   ('core', G+'/files/weekly-report-w45-it-core/svg/*.svg')]:
    tot_cjk = 0; tot_qj = 0; alltxt = []
    for f in sorted(glob.glob(pat)):
        ts = texts(f)
        for e in ts:
            tot_cjk += len(cjk(e['text']))
            if '桥接' in e['text']: tot_qj += 1
            alltxt.append(e['text'])
        print(f"{label} {f.split('/')[-1]}: textnodes={len(ts)} cjk_chars={sum(len(cjk(e['text'])) for e in ts)}")
    print(f"{label} TOTAL cjk={tot_cjk} qiaojie_nodes={tot_qj}")
    if label == 'edition':
        joined = '\n'.join(alltxt)
        open('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-fr-proof/edition-alltext.txt','w').write(joined)
        # P7 checks
        p7 = texts(G+'/files/weekly-report-w45-it-fr/svg/p7-lingua.svg')
        p7j = '\n'.join(e['text'] for e in p7)
        print("--- P7 nodes containing assaggio/def ---")
        for e in p7:
            if 'assaggio' in e['text'] or 'prova di un cibo' in e['text'] or 'dégustation' in e['text']:
                print(repr(e))
        print("--- P7 LETTERE nodes ---")
        for e in p7:
            if 'LETTERE' in e['text'] or 'redazione' in e['text'] or 'Écrivez' in e['text'] or 'VOL.3' in e['text'] or 'Exemple de rédaction' in e['text'] or 'Li,' in e['text'] or 'Pechino' in e['text']:
                print(repr(e))
        print("--- P7 FRASI section: nodes after FRASI ---")
        inj = [e['text'] for e in p7]
        # print all p7 texts with y for col3 check later
        for e in p7:
            print(f"P7 y={e['y']} x={e['x']} fs={e['fs']} :: {e['text']!r}")
    if label == 'core':
        open('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-fr-proof/core-alltext.txt','w').write('\n'.join(alltxt))
