#!/usr/bin/env python3
"""Round 4 independent count: exercise numbers in prompt order per page
(excluding P1 Fragen box and P8 answer-key region), level-chip tally,
standalone chip inventory, and P8 answer-block item check via p8 extract."""
import re, html, pathlib, json, collections
ED = pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-de-zh-cn"
PAGES = ['p1-front.svg','p2-leben.svg','p3-kultur.svg','p4-sport.svg','p5-jugend.svg','p6-vertiefung.svg','p7-sprache.svg','p8-uebungen.svg']
def texts(pg):
    s=(ED/'svg'/pg).read_text(encoding='utf-8')
    return [html.unescape(re.sub(r'<[^>]+>','',c)).strip() for c in re.findall(r'<text[^>]*>(.*?)</text>', s, re.S)]
per_page={}; chips=collections.Counter(); chip_elems=[]
for pg in PAGES:
    ts=texts(pg); items=[]; cur=None; expected=None; skip=False; inex=False
    for t in ts:
        if not inex and ('ÜBUNGEN' in t or 'JETZT ÜBEN' in t or 'UHRZEITEN' in t): inex=True
        if not inex: continue
        if pg.startswith('p1') and 'FRAGEN' in t: skip=True
        if skip and t.startswith('IN DIESER AUSGABE'): skip=False
        if skip: continue
        if pg.startswith('p8') and t.startswith('ANTWORTEN'): break
        if t in ('A2','B1','B2'):
            cur=t; chips[t]+=1; chip_elems.append((pg,t)); continue
        m=re.match(r'^(\d+)\.$', t) or re.match(r'^(\d+)\.\s', t)
        if m and '–' not in t:
            n=int(m.group(1))
            if expected is None: expected=n
            if n==expected and n not in [x[0] for x in items]:
                items.append((n,cur)); expected=n+1
    per_page[pg]=items
    print(pg, "items:", len(items), "numbers:", [n for n,_ in items])
allnums=[n for pg in PAGES for n,_ in per_page[pg]]
print("TOTAL numbered prompt items:", len(allnums), "continuous 1..149:", allnums==list(range(1,150)))
print("chip elements (standalone):", dict(chips), "total chip elements:", sum(chips.values()))
print("per-item levels:", collections.Counter(lv for pg in PAGES for _,lv in per_page[pg]))
untagged=[n for pg in PAGES for n,lv in per_page[pg] if lv is None]
print("untagged items:", untagged)
# P8 prompt items 113-150: which carry chips? P8 groups 113-120 options + 141-144 group header
for pg in ['p8-uebungen.svg']:
    print("P8 items:", per_page[pg])
json.dump({"per_page":{k:[list(x) for x in v] for k,v in per_page.items()},"chips":dict(chips),"total":len(allnums)}, open(pathlib.Path(__file__).parent/"counts-r4.json","w"), ensure_ascii=False, indent=1)
