import re, html, os, json, hashlib
CORE='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-core/svg'
ED='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-en/svg'
def raw(p): return open(p,encoding='utf-8').read()
def texts(p):
    s=raw(p)
    return [(m.group(1), html.unescape(re.sub(r"<[^>]+>","",m.group(2)))) for m in re.finditer(r"<text([^>]*)>(.*?)</text>",s,re.S)]
def attrs(a): return dict(re.findall(r'([\w-]+)="([^"]*)"',a))
out={}
# images: count + sha of image element strings (no printing payload)
for fn in sorted(os.listdir(CORE)):
    ci=re.findall(r"<image[^>]*>",raw(os.path.join(CORE,fn)))
    ei=re.findall(r"<image[^>]*>",raw(os.path.join(ED,fn)))
    def sig(els):
        return [(re.search(r'x="([^"]*)"',e).group(1) if re.search(r'x="([^"]*)"',e) else '', re.search(r'y="([^"]*)"',e).group(1) if re.search(r'y="([^"]*)"',e) else '', hashlib.sha256(e.encode()).hexdigest()[:16]) for e in els]
    print(fn,'images core',len(ci),'ed',len(ei),'elements-identical',ci==ei)
    out[fn]={'core_n':len(ci),'ed_n':len(ei),'identical':ci==ei}
# footers
for label,d in [('core',CORE),('ed',ED)]:
    print('== footers',label)
    for fn in sorted(os.listdir(d)):
        foots=[t for a,t in texts(os.path.join(d,fn)) if attrs(a).get('y')=='2624']
        print(' ',fn,foots)
# top strip y=92 centre
for label,d in [('core',CORE),('ed',ED)]:
    for fn in ['p1-pervaya.svg']:
        ts=texts(os.path.join(d,fn))
        print(label,'top-centre:',[t for a,t in ts if attrs(a).get('y')=='92' and attrs(a).get('text-anchor')=='middle'])
# gloss rendered: count items by splitting rendered gloss-box texts? Use source gloss strings split on ' · ' -> builder method; redo independently from sources
for label,base in [('core','/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-ru-build'),('ed','/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-ru-en-build')]:
    print('== gloss source',label)
    for fn in ['content12.py','content34.py','content56.py']:
        s=open(f'{base}/{fn}',encoding='utf-8').read()
        calls=re.findall(r'\.gloss\("(.*?)"\)',s,re.S)
        counts=[len(c.split('·')) for c in calls]
        print(' ',fn,'calls',len(calls),'items-per-call',counts,'total',sum(counts))
json.dump(out,open('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/ru-en-proof/images.json','w'),indent=1)
