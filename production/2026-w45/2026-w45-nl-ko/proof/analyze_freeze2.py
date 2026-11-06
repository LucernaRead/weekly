import json, re, collections
d = json.load(open('freeze-diff-proof.json'))
def cls(ch):
    o = ord(ch)
    if 0xAC00 <= o <= 0xD7A3: return 'hangul_syl'
    if 0x4E00 <= o <= 0x9FFF or 0x3400 <= o <= 0x4DBF: return 'hanja'
    if 0x1100 <= o <= 0x11FF or 0x3130 <= o <= 0x318F: return 'hangul_jamo'
    if 0x3040 <= o <= 0x30FF: return 'kana'
    if 0x0400 <= o <= 0x04FF: return 'cyrillic'
    return 'other_cjk?'
for pg in sorted(d['pages'], key=lambda x: int(x)):
    v = d['pages'][pg]
    added = v['cjk_added']
    s = sum(added.values())
    by = collections.Counter()
    for ch, n in added.items():
        by[cls(ch)] += n
    print(f"p{pg}: core={v['cjk_core_total']} ed={v['cjk_edition_total']} cjk_added_sum={s} byclass={dict(by)} n_distinct={len(added)}")
print("cjk_added_total field:", d['cjk_added_total'])
# removed strings: list all, flag those with NO CJK char at all
def has_cjk(s):
    return any(0x2E80<=ord(c)<=0x9FFF or 0xAC00<=ord(c)<=0xD7A3 or 0x3040<=ord(c)<=0x30FF for c in s)
print("\n=== REMOVED strings with NO CJK (per page) ===")
tot=0
for pg in sorted(d['pages'], key=lambda x: int(x)):
    v=d['pages'][pg]
    for r in v['removed_strings']:
        if not has_cjk(r['text']):
            tot+=1
            print(f"p{pg} x{r['count']}: {r['text']!r}")
print("TOTAL removed-no-CJK strings:", tot)
print("\n=== REMOVED strings total counts ===")
for pg in sorted(d['pages'], key=lambda x: int(x)):
    v=d['pages'][pg]
    print(f"p{pg}: removed {len(v['removed_strings'])} added {len(v['added_strings'])}")
# edition raw CJK scan: read SVGs directly, count Hangul syllables vs Hanja in edition text
import glob, xml.etree.ElementTree as ET
ED='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-ko/svg'
CORE='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-core/svg'
def scan(dire):
    hang=syl=hanja=jamo=0; tot=0
    texts=[]
    for f in sorted(glob.glob(dire+'/*.svg')):
        s=open(f,encoding='utf-8').read()
        for m in re.finditer(r'<text[^>]*>([^<]*)</text>', s):
            t=m.group(1); texts.append(t)
            for c in t:
                o=ord(c)
                if 0xAC00<=o<=0xD7A3: syl+=1; tot+=1
                elif 0x4E00<=o<=0x9FFF or 0x3400<=o<=0x4DBF: hanja+=1; tot+=1
                elif 0x1100<=o<=0x11FF or 0x3130<=o<=0x318F: jamo+=1; tot+=1
    return tot,syl,hanja,jamo
print("\nRAW SVG text scan edition:", scan(ED))
print("RAW SVG text scan core:", scan(CORE))
# multiset delta: edition minus core per char across all pages (from JSON cjk_added? need raw)
# Instead compute from SVGs directly
def multiset(dire):
    c=collections.Counter()
    for f in sorted(glob.glob(dire+'/*.svg')):
        s=open(f,encoding='utf-8').read()
        for m in re.finditer(r'<text[^>]*>([^<]*)</text>', s):
            for ch in m.group(1):
                o=ord(ch)
                if 0x2E80<=o<=0x9FFF or 0xAC00<=o<=0xD7A3 or 0x1100<=o<=0x11FF or 0x3130<=o<=0x318F or 0x3040<=o<=0x30FF:
                    c[ch]+=1
    return c
ce=multiset(ED); cc=multiset(CORE)
delta=collections.Counter()
for ch,n in ce.items():
    if n>cc.get(ch,0): delta[ch]=n-cc.get(ch,0)
by=collections.Counter()
for ch,n in delta.items(): by[cls(ch)]+=n
print("MULTISET DELTA edition-core: total", sum(delta.values()), dict(by))
print("  delta hangul syllables:", sum(n for ch,n in delta.items() if cls(ch)=='hangul_syl'))
print("  delta hanja:", sum(n for ch,n in delta.items() if cls(ch)=='hanja'))
print("  delta hanja chars:", {ch:n for ch,n in delta.items() if cls(ch)=='hanja'})
print("  edition hanja total raw:", sum(n for ch,n in ce.items() if cls(ch)=='hanja'))
print("  edition hanja chars:", {ch:n for ch,n in ce.items() if cls(ch)=='hanja'})
