import os, re, json, unicodedata
import xml.etree.ElementTree as ET
G=os.path.expanduser('~/workspace/goals/lucernaread-social-media-operations')
ED=f'{G}/files/weekly-report-w45-pt-it/svg'; CO=f'{G}/files/weekly-report-w45-pt-core/svg'; W43=f'{G}/files/weekly-report-pt-it/svg'
SVG='{http://www.w3.org/2000/svg}text'
def nodes(p):
    t=ET.parse(p); out=[]
    for e in t.getroot().iter(SVG):
        out.append({'x':float(e.get('x') or 0),'y':float(e.get('y') or 0),'fs':e.get('font-size'),'txt':''.join(e.itertext())})
    return out
def alltext(d,pg): return [n['txt'] for n in nodes(f'{d}/{pg}.svg')]
PAGES=['p1-capa','p2-vida','p3-cultura','p4-esporte','p5-jovens','p6-aprofundamento','p7-lingua','p8-avaliacao']
res={}
# --- gloss: reconstruct Nota blocks from rendered SVG (fs 20.5, x=545, contiguous lines) ---
def gloss_count(d,pg):
    ns=sorted([n for n in nodes(f'{d}/{pg}.svg') if n['fs']=='20.5' and abs(n['x']-545)<1 and 'Nota' in n['txt'] or (n['fs']=='20.5' and abs(n['x']-545)<1)],key=lambda r:r['y'])
    # simpler: take lines starting at Nota then following 20.5/x545 lines until gap>45
    ns=sorted([n for n in nodes(f'{d}/{pg}.svg') if n['fs']=='20.5' and abs(n['x']-545)<1],key=lambda r:r['y'])
    start=[i for i,n in enumerate(ns) if n['txt'].startswith('Nota')]
    if not start: return None
    i=start[0]; lines=[ns[i]['txt']]; prev=ns[i]['y']
    for n in ns[i+1:]:
        if n['y']-prev>45: break
        lines.append(n['txt']); prev=n['y']
    joined=' '.join(lines)
    items=[s.strip() for s in joined.split('·')]
    # first item includes prefix
    return {'joined':joined,'items':items,'count':len(items)}
res['gloss_ed']={pg:gloss_count(ED,pg) for pg in PAGES if gloss_count(ED,pg)}
res['gloss_co']={pg:gloss_count(CO,pg) for pg in PAGES if gloss_count(CO,pg)}
# core prefix differs; gloss_count above requires 'Nota' start - core uses Chinese prefix, handle separately
def gloss_count_core(d,pg):
    ns=sorted([n for n in nodes(f'{d}/{pg}.svg') if n['fs']=='20.5' and abs(n['x']-545)<1],key=lambda r:r['y'])
    # core gloss lines contain '=' and start near a box; find first line containing '注' or '=' with preceding box? print candidates instead
    return ns
# --- CJK / Cyrillic / Hangul / kana per page (edition) ---
def script_counts(txt):
    c={'cjk':0,'cyr':0,'hang':0,'kana':0}
    for ch in txt:
        o=ord(ch)
        if 0x4E00<=o<=0x9FFF or 0x3400<=o<=0x4DBF or 0xF900<=o<=0xFAFF: c['cjk']+=1
        elif 0x0400<=o<=0x04FF: c['cyr']+=1
        elif 0xAC00<=o<=0xD7AF or 0x1100<=o<=0x11FF: c['hang']+=1
        elif 0x3040<=o<=0x30FF: c['kana']+=1
    return c
res['scripts_ed']={}
for pg in PAGES:
    tot={'cjk':0,'cyr':0,'hang':0,'kana':0}
    for t in alltext(ED,pg):
        cc=script_counts(t)
        for k in tot: tot[k]+=cc[k]
    res['scripts_ed'][pg]=tot
# --- 桥接 + Note| + Page N of ---
full_ed=' '.join(t for pg in PAGES for t in alltext(ED,pg))
res['qiaojie']=full_ed.count('桥接'); res['note_pipe']=full_ed.count('Note |'); res['page_n_of']=len(re.findall(r'Page \d+ of',full_ed))
res['complete_lines_ed']=[(pg,t) for pg in PAGES for t in alltext(ED,pg) if 'COMPLETE' in t]
res['complete_lines_co']=[(pg,t) for pg in PAGES for t in alltext(CO,pg) if 'COMPLETE' in t]
# --- English standalone words: tokenise edition text, list tokens that are ASCII-only words >=2 letters not in PT/IT allowlist ---
import collections
toks=re.findall(r"[A-Za-zÀ-ÿ]+", full_ed)
# crude: pure-ASCII tokens
ascii_toks=[t for t in toks if all(ord(c)<128 for c in t)]
cnt=collections.Counter(ascii_toks)
res['ascii_token_counts']=dict(cnt.most_common(60))
# --- P7 dump ---
res['p7_ed']=nodes(f'{ED}/p7-lingua.svg')
res['p7_co']=nodes(f'{CO}/p7-lingua.svg')
json.dump(res,open(f'{G}/hidden_files/w45/pt-it-proof/proof1.json','w'),ensure_ascii=False,indent=1)
print('gloss_ed:',{k:v['count'] for k,v in res['gloss_ed'].items()})
print('scripts_ed:',res['scripts_ed'])
print('qiaojie',res['qiaojie'],'note_pipe',res['note_pipe'],'page_n_of',res['page_n_of'])
print('COMPLETE ed:',res['complete_lines_ed']); print('COMPLETE co:',res['complete_lines_co'])
print('top ascii:',cnt.most_common(30))
