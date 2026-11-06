import re, json, hashlib, collections, pathlib, sys
core=pathlib.Path.home()/ "workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-core/svg"
ed=pathlib.Path.home()/ "workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-fr/svg"
files=sorted(core.glob("*.svg"))
def texts(p):
    s=p.read_text(encoding='utf-8')
    # rendered text elements only: <text ...>...</text>, strip tags inside (tspan)
    raw=re.findall(r'<text[^>]*>(.*?)</text>', s, flags=re.S)
    out=[]
    for t in raw:
        t=re.sub(r'<[^>]+>','',t)
        import html; t=html.unescape(t).strip()
        if t: out.append(t)
    return s, out
def cyr_tokens(txts):
    c=collections.Counter()
    for t in txts:
        for tok in re.findall(r'[А-Яа-яЁё]+(?:-[А-Яа-яЁё]+)*', t):
            c[tok]+=1
    return c
def cjk(txts):
    n=0; chars=collections.Counter()
    for t in txts:
        for ch in t:
            if '\u4e00' <= ch <= '\u9fff' or '\u3040' <= ch <= '\u30ff' or '\uac00' <= ch <= '\ud7af':
                n+=1; chars[ch]+=1
    return n, chars
res={}
for cf in files:
    ef=ed/cf.name
    cs,ct=texts(cf); es,et=texts(ef)
    cc=cyr_tokens(ct); ec=cyr_tokens(et)
    diff_c = (ec-cc); diff_r=(cc-ec)
    # diff_c positive = added in edition, diff_r removed
    print(f"\n== {cf.name} core_texts={len(ct)} ed_texts={len(et)} cyr_core={sum(cc.values())} cyr_ed={sum(ec.values())} CJK_core={cjk(ct)[0]} CJK_ed={cjk(et)[0]}")
    print("  added_cyr:", dict(diff_c))
    print("  removed_cyr:", dict(diff_r))
    res[cf.name]={'core_cyr_total':sum(cc.values()),'ed_cyr_total':sum(ec.values()),'added':dict(diff_c),'removed':dict(diff_r),'cjk_ed':cjk(et)[0]}
json.dump(res, open(pathlib.Path(__file__).parent/"cyr.json","w"), ensure_ascii=False, indent=1)
# P1 lines at y=330,372
for label, d in [('core',core),('ed',ed)]:
    s=(d/'p1-pervaya.svg').read_text()
    for m in re.finditer(r'<text[^>]*x="([^"]*)"[^>]*y="([^"]*)"[^>]*>(.*?)</text>', s, flags=re.S):
        if m.group(2) in ('330','372','330.0','372.0') or float(m.group(2)) in (330,372):
            txt=re.sub(r'<[^>]+>','',m.group(3)).strip()
            print(label, 'y=',m.group(2),'x=',m.group(1), repr(txt[:200]))
