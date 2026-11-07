import re, glob, os, html
BASE=os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
def texts_of(fn):
    s=open(fn,encoding="utf-8").read()
    return [html.unescape(re.sub(r"<[^>]+>","",c)) for c in re.findall(r"<text[^>]*>(.*?)</text>", s, re.S)]
print("===== GLOSS COUNTS (split on U+00B7 '·' in gloss/prefix lines) =====")
# Gloss boxes: lines containing ' · ' separators with term+gloss pattern are hard to isolate generically.
# Targeted: P1 headline explanation line (contains prefix + terms) + P2-P5 gloss box lines.
# Method: for each page, collect lines that look like gloss entries: contain '·' AND (start with gloss prefix OR contain '=' OR are in gloss boxes).
# Instead count TOTAL '·'-separated items in lines whose line contains a term-citation pattern: use freeze diff? Simpler robust proxy:
# Count items in the specific gloss strings: extract all text lines on P2-P5 that contain '·' and are NOT headers/footers, split on '·', sum items, compare core vs edition.
for code in ["core","de","en","fr","it","ja","ko","nl","pt","ru","zh-cn","zh-tw"]:
    tot_core=None
    counts={}
    for pg,fn in [(2,"p2-vida.svg"),(3,"p3-cultura.svg"),(4,"p4-deporte.svg"),(5,"p5-juventud.svg")]:
        ts=texts_of(BASE+f"/files/weekly-report-w46-es-{code}/svg/{fn}")
        # gloss lines: lines containing '·' that are short (<120 chars) and not section headers (all caps) and not calendar lines
        items=0; nlines=0
        for t in ts:
            if "·" in t and len(t)<160 and t!=t.upper():
                # exclude footer/page lines and exercise stems with options (contain 'A.' etc.)? gloss lines contain '=' or are term lists
                if "=" in t or "·" in t:
                    pass
        counts[pg]=None
    print(code, "(gloss proxy skipped - see dedicated check below)")
print("\n===== DEDICATED: gloss-box item counts via '·' split on lines with '=' (term = gloss) =====")
for code in ["core","de","en","fr","it","ja","ko","nl","pt","ru","zh-cn","zh-tw"]:
    per={}
    for pg,fn in [(1,"p1-portada.svg"),(2,"p2-vida.svg"),(3,"p3-cultura.svg"),(4,"p4-deporte.svg"),(5,"p5-juventud.svg")]:
        ts=texts_of(BASE+f"/files/weekly-report-w46-es-{code}/svg/{fn}")
        items=0
        for t in ts:
            if "=" in t:
                items+=len([p for p in t.split("·") if p.strip()])
        per[pg]=items
    print(code, per, "total=", sum(per.values()))
