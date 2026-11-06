import re, glob, html, json
pages = ['p1-une','p2-vie','p3-culture','p4-sport','p5-jeunesse','p6-politique','p7-langue','p8-exercices']
base='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-core/svg/'
def nodes(f):
    data=open(f,encoding='utf-8').read()
    out=[]
    for m in re.finditer(r'<text([^>]*)>(.*?)</text>',data,re.S):
        attrs,inner=m.group(1),m.group(2)
        t=html.unescape(re.sub(r'<[^>]+>','',inner)).strip()
        x=re.search(r'x="([\d.]+)"',attrs); y=re.search(r'y="([\d.]+)"',attrs)
        out.append({'x':float(x.group(1)) if x else None,'y':float(y.group(1)) if y else None,'t':t})
    return out
all_items={}; per_page={}
for pg in pages:
    ns=nodes(base+pg+'.svg')
    lvl=None; items=[]
    for n in ns:
        t=n['t']
        if t in ('A2','B1','B2'):
            lvl=t; continue
        m=re.fullmatch(r'(\d+)\.',t)
        if m:
            num=int(m.group(1)); items.append((num,lvl)); all_items[num]=(pg,lvl); continue
        m=re.fullmatch(r'(\d+)[–-](\d+)\.',t)
        if m:
            for num in range(int(m.group(1)),int(m.group(2))+1):
                items.append((num,lvl)); all_items[num]=(pg,lvl)
    per_page[pg]=items
    print(pg, 'count', len(items), 'nums', items[0][0], '-', items[-1][0])
nums=sorted(all_items)
print('TOTAL distinct stems:', len(nums), 'missing:', [n for n in range(1,151) if n not in all_items], 'dupes/out-of-range:', [n for n in nums if n<1 or n>150])
from collections import Counter
c=Counter(lvl for pg,lvl in all_items.values())
print('LEVELS:', dict(c), 'sum', sum(c.values()))
print('PER-PAGE counts:', {pg:len(v) for pg,v in per_page.items()})
json.dump({str(k):v for k,v in all_items.items()}, open('/tmp/fr45txt/stem-levels.json','w'), ensure_ascii=False, indent=1)
# P8 answer keys: manual transcription cross-check target list (from full read of P8 answer block)
# Extract answer block: nodes after 'RÉPONSES' node, join with space, then segment per number
ns=nodes(base+'p8-exercices.svg')
idx=[i for i,n in enumerate(ns) if n['t'].startswith('RÉPONSES')][0]
ans=' '.join(n['t'] for n in ns[idx:])
ans=re.sub(r'\s+',' ',ans)
# find segments: 'N. ' markers for N in 1..150 in order (answer block lists in page order)
marks=list(re.finditer(r'(?<![\d.])(\d+)\.\s', ans))
print('answer markers found:', len(marks), 'first:', marks[0].group(0) if marks else None)
seq=[int(m.group(1)) for m in marks]
print('answer sequence == 1..150:', seq==list(range(1,151)))
if seq!=list(range(1,151)):
    print('seq diff at:', [(i+1,s) for i,s in enumerate(seq) if i+1!=s][:20])
