import re, collections, pathlib, html
core=pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-core/svg"
ed=pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-fr/svg"
def texts(p):
    s=p.read_text(encoding='utf-8')
    raw=re.findall(r'<text[^>]*>(.*?)</text>', s, flags=re.S)
    return [html.unescape(re.sub(r'<[^>]+>','',t)).strip() for t in raw if html.unescape(re.sub(r'<[^>]+>','',t)).strip()]
for cf in sorted(core.glob("*.svg")):
    for name, d in [('core',core),('ed',ed)]:
        txts=texts(d/cf.name)
        # split tokenization: any maximal Cyrillic run
        toks=[]
        for t in txts: toks+=re.findall(r'[А-Яа-яЁё]+', t)
        print(cf.name, name, 'split_total=',len(toks), 'counter_hyphen_tokens=', sum(1 for t in txts for tok in re.findall(r'[А-Яа-яЁё]+(?:-[А-Яа-яЁё]+)*',t)))
    # P1 removed under split
    cc=collections.Counter(); ec=collections.Counter()
    for t in texts(core/cf.name): cc.update(re.findall(r'[А-Яа-яЁё]+',t))
    for t in texts(ed/cf.name): ec.update(re.findall(r'[А-Яа-яЁё]+',t))
    if cf.name.startswith('p1'):
        print(' P1 split removed:', dict(cc-ec), 'added:', dict(ec-cc))
