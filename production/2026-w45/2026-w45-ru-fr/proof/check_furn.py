import re, pathlib, html
base=pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations"
def texts(d, name):
    s=(base/d/name).read_text()
    out=[]
    for m in re.finditer(r'<text\b([^>]*)>(.*?)</text>', s, flags=re.S):
        txt=html.unescape(re.sub(r'<[^>]+>','',m.group(2))).strip()
        if txt: out.append((m.group(1),txt))
    return out
def find(d, name, needle):
    return [(a,t) for a,t in texts(d,name) if needle in t]
dirs={'core':'files/weekly-report-w45-ru-core/svg','ed':'files/weekly-report-w45-ru-fr/svg','w43':'files/weekly-report-ru-fr/svg'}
for needle in ['КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ','TEXTE EN RUSSE','Page ','sur 8','Note — ','Донн','СТРАНИЦА','УЧЕБНЫЕ ДАННЫЕ','Données d\'exercice']:
    print('\n###', needle)
    for k,d in dirs.items():
        for pg in ['p1-pervaya.svg','p6-razbor.svg','p8-test.svg']:
            for a,t in find(d,pg,needle):
                print(f" {k} {pg} :: {t[:220]}")
# footers all pages ed vs w43 pattern
print('\n### footers ed all pages')
for pg in sorted((base/dirs['ed']).glob('*.svg')):
    for a,t in texts(dirs['ed'],pg.name):
        if 'Lucerna ·' in t or 'sur 8' in t: print(pg.name, t)
print('\n### footers w43 all pages')
for pg in sorted((base/dirs['w43']).glob('*.svg')):
    for a,t in texts(dirs['w43'],pg.name):
        if 'Lucerna ·' in t or 'sur 8' in t: print(pg.name, t)
print('\n### gloss prefix occurrences ed (Note — )')
for pg in sorted((base/dirs['ed']).glob('*.svg')):
    n=sum(1 for a,t in texts(dirs['ed'],pg.name) if t.startswith('Note —'))
    print(pg.name, n)
print('\n### section heads ed p1')
for a,t in texts(dirs['ed'],'p1-pervaya.svg'):
    if '·' in t and any(k in t for k in ['ГЛАВНАЯ','НЕДЕЛЯ','В ЭТОМ','СЛОВО','УПРАЖНЕНИЯ','ФРАЗЫ','СЛЕДУЮЩАЯ','ТЕСТ','ОТВЕТЫ']):
        print(' ',t)
print('\n### contents Стр.8 row / level tag vse')
for k,d in dirs.items():
    for a,t in texts(d,'p1-pervaya.svg'):
        if 'Стр. 8' in t or t.strip()=='все': print(k,t)
