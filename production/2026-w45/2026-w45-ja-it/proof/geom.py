import sys, re
sys.path.insert(0, '/home/hatch/workspace/goals/lucernaread-social-media-operations/tools')
import occlusion_audit as oa
from extract import texts
import xml.etree.ElementTree as ET

ED='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ja-it'
CORE='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ja-core'

def parse(path):
    tree=ET.parse(path); root=tree.getroot()
    els=[]
    for el in root.iter():
        tag=el.tag.split('}')[-1]
        if tag=='text':
            els.append(('text', dict(el.attrib), ''.join(el.itertext())))
        elif tag in ('rect','line'):
            els.append((tag, dict(el.attrib), ''))
    return els

# ADVANCE scan: advance end = x + font.getlength(text) for start-anchored; middle/end adjust
def advance_end(att, t):
    fam=att.get('font-family',''); size=float(att.get('font-size',25)); bold='bold' in (att.get('font-weight','') or '')
    try: f=oa.get_font(fam, size, bold)
    except Exception: return None
    w=f.getlength(t)
    x=float(att.get('x',0)); anchor=att.get('text-anchor','start')
    if anchor=='middle': return x+w/2
    if anchor=='end': return x
    return x+w

for label, base in (('ED',ED),('CORE',CORE)):
    worst=[]
    for p in ['p1-hyoushi','p2-kurashi','p3-bunka','p4-supotsu','p5-wakamono','p6-fukayomi','p7-kotoba','p8-tesuto']:
        for tag,att,t in parse(f'{base}/svg/{p}.svg'):
            if tag!='text': continue
            e=advance_end(att,t)
            if e is not None and e>1885.5: worst.append((p, round(e,2), t[:60]))
    print(label, 'ADVANCE violations >1885.5:', len(worst), worst[:10])
    # max advance end per page for P2 instruction check
    for p in ['p2-kurashi']:
        mx=0; mt=''
        for tag,att,t in parse(f'{base}/svg/{p}.svg'):
            if tag!='text': continue
            e=advance_end(att,t)
            if e and 'Abbina' in t: print('  ', label, p, 'Abbina line:', repr(t), 'advance end:', round(e,2), 'x:', att.get('x'), 'size:', att.get('font-size'))
            if e and e>mx: mx, mt = e, t[:50]
        print('  ', label, p, 'max advance:', round(mx,2), repr(mt))

# P8 end y / P7 teaser end y (edition): max y of text elements, excluding footer lines (Pagina/footer)
for p, name in (('p8-tesuto','P8'), ('p7-kotoba','P7')):
    ts=texts(f'{ED}/svg/{p}.svg')
    body=[(x,y,fs,t) for x,y,fs,t in ts if 'Pagina' not in t and 'Lucerna ·' not in t and 'SETTIMANALE' not in t]
    body.sort(key=lambda r: r[1])
    print(name, 'max body y:', body[-1], '| top3:', body[-3:])
    # P7 teaser: elements with y > 2300
    if p=='p7-kotoba':
        print('  P7 y>2300:', [(round(y,2),t[:70]) for x,y,fs,t in body if y>2300])
    if p=='p8-tesuto':
        print('  P8 y>2300:', [(round(y,2),t[:70]) for x,y,fs,t in body if y>2300])
