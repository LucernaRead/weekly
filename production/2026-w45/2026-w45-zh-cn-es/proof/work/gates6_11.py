# Gates 6-11 checks: gloss counts, P7 goldens, images, readers corner, furniture, glosslines.
import re, sys, os, glob, json, hashlib, base64
from xml.etree import ElementTree as ET

BASE = os.path.expanduser('~/workspace/goals/lucernaread-social-media-operations')
ED = os.path.join(BASE, 'files/weekly-report-w45-zh-cn-es/svg')
CORE = os.path.join(BASE, 'files/weekly-report-w45-zhcn-core/svg')
W43 = os.path.join(BASE, 'files/weekly-report-zh-cn-es/svg')

def texts(path):
    tree = ET.parse(path)
    out = []
    for el in tree.iter():
        if el.tag.endswith('}text') or el.tag == 'text':
            out.append((el, ''.join(el.itertext())))
    return out

def text_attrs(path):
    # (x, y, size, text)
    out = []
    for el, s in texts(path):
        try:
            out.append((float(el.get('x', '0')), float(el.get('y', '0')),
                        float(el.get('font-size', '0')), s))
        except ValueError:
            pass
    return out

print("=== GATE 6a: source gloss() counts (split on '·') ===")
def gloss_counts(builddir):
    res = {}
    for f in ['content12.py', 'content34.py', 'content56.py']:
        src = open(os.path.join(builddir, f), encoding='utf-8').read()
        # gloss calls: gloss("...") possibly multiline? find gloss( then quoted string
        calls = re.findall(r'gloss\(\s*"((?:[^"\\]|\\.)*)"', src)
        counts = [len(c.split('·')) for c in calls]
        res[f] = counts
    return res
core_build = os.path.join(BASE, 'hidden_files/weekly-report-w45-zhcn-build')
es_build = os.path.join(BASE, 'hidden_files/weekly-report-w45-zh-cn-es-build')
print("core:", gloss_counts(core_build))
print("es  :", gloss_counts(es_build))
print("total core:", sum(sum(v) for v in gloss_counts(core_build).values()),
      "total es:", sum(sum(v) for v in gloss_counts(es_build).values()))

print("=== GATE 6b: rendered gloss boxes ===")
for d, name, prefix in [(CORE, 'core', 'Notes｜'), (ED, 'edition', 'Nota — ')]:
    per_page = {}
    for f in sorted(glob.glob(os.path.join(d, '*.svg'))):
        pg = os.path.basename(f)
        boxes = []
        for el, s in texts(f):
            if s.startswith(prefix):
                boxes.append(len(s[len(prefix):].split('·')))
        if boxes:
            per_page[pg] = boxes
    print(name, per_page)

print("=== GATE 7: P7 golden sentences (concatenated per-page text) ===")
phrases = {
    '不用等11月11日': 'p1-touiban.svg',
    '下单就能发货': 'p2-shenghuo.svg',
    '先看结算页，再付款': 'p2-shenghuo.svg',
    '水开始结冰': 'p3-wenhua.svg',
    '三场都输了': 'p4-tiyu.svg',
    '小局一场没赢': 'p4-tiyu.svg',
    '故事够不够好': 'p5-qingnian.svg',
    '别以后，就现在': 'p5-qingnian.svg',
}
for d, name in [(ED, 'edition'), (CORE, 'core')]:
    print(f"-- {name}")
    for ph, pg in phrases.items():
        cat_article = ''.join(s for _, _, _, s in text_attrs(os.path.join(d, pg)))
        cat_p7 = ''.join(s for _, _, _, s in text_attrs(os.path.join(d, 'p7-ciyu.svg')))
        print(f"  {ph}: article {cat_article.count(ph)}x, P7 {cat_p7.count(ph)}x")
    # P7 tags
    p7 = ''.join(s for _, _, _, s in text_attrs(os.path.join(d, 'p7-ciyu.svg')))
    print("  P7 has (Página 1)..(Página 5) tags:", [f'(Página {n})' in p7 for n in range(1, 6)])

print("=== GATE 8: images ===")
for d, name in [(CORE, 'core'), (ED, 'edition')]:
    print(f"-- {name}")
    for f in sorted(glob.glob(os.path.join(d, '*.svg'))):
        tree = ET.parse(f)
        imgs = []
        for el in tree.iter():
            if el.tag.endswith('}image') or el.tag == 'image':
                href = el.get('{http://www.w3.org/1999/xlink}href') or el.get('href', '')
                x, y, w, h = el.get('x'), el.get('y'), el.get('width'), el.get('height')
                payload = href.split(',', 1)[1] if ',' in href else ''
                try:
                    raw = base64.b64decode(payload)
                    md5 = hashlib.md5(raw).hexdigest()[:16]
                except Exception as e:
                    md5 = f'ERR {e}'
                imgs.append((x, y, w, h, md5))
        print(f"  {os.path.basename(f)}: {len(imgs)} images {imgs}")
print("-- asset files md5:")
for a in sorted(glob.glob(os.path.join(es_build, 'assets/*.jpg'))):
    print("  ", os.path.basename(a), hashlib.md5(open(a, 'rb').read()).hexdigest()[:16])
print("-- credits lines edition:")
for f in sorted(glob.glob(os.path.join(ED, '*.svg'))):
    for _, _, _, s in text_attrs(f):
        if s.startswith('Foto:'):
            print(f"   {os.path.basename(f)}: {s}")
print("-- CREDITS.md sha:")
for dd in [core_build, es_build]:
    p = os.path.join(dd, 'assets/CREDITS.md')
    print("  ", dd.split('/')[-1], hashlib.sha256(open(p, 'rb').read()).hexdigest()[:16], os.path.getsize(p))

print("=== GATE 9: readers corner (P7) ===")
p7texts = [s for _, _, _, s in text_attrs(os.path.join(ED, 'p7-ciyu.svg'))]
cat = ''.join(p7texts)
checks = {
    'disclosure ES (Ejemplo de la redacción, no una carta real)': 'Ejemplo de la redacción, no una carta real' in cat,
    'no genuine letters (no ha llegado ninguna carta real)': 'no ha llegado ninguna carta real' in cat,
    'deferred promise (Aplazado, no cancelado)': 'Aplazado, no cancelado' in cat,
    'invitation verbatim': '¡Envíanos tu carta en chino!' in cat,
    'letter intact (你好！我住在上海)': '你好！我住在上海' in cat,
}
for k, v in checks.items():
    print(f"  {k}: {v}")

print("=== GATE 10 furniture: P1 badge ===")
for d, name in [(CORE, 'core EN'), (W43, 'W43 ES'), (ED, 'this edition')]:
    nodes = [(x, y, sz, s) for x, y, sz, s in text_attrs(os.path.join(d, 'p1-touiban.svg')) if y == 434]
    print(f"  {name}: {nodes}")
print("=== P8 separators ===")
for d, name in [(CORE, 'core'), (W43, 'W43'), (ED, 'edition')]:
    seps = [s for _, _, _, s in text_attrs(os.path.join(d, 'p8-ceyan.svg')) if s.startswith('— ') and s.endswith(' —')]
    print(f"  {name}: {seps}  allcaps PÁGINA count: {sum(1 for s in seps if 'PÁGINA' in s)}")
print("=== footers / page lines / P8 header / strap / strapline / top strip ===")
for d, name in [(ED, 'edition')]:
    for pg in ['p1-touiban.svg', 'p2-shenghuo.svg', 'p8-ceyan.svg']:
        ts = [s for _, _, _, s in text_attrs(os.path.join(d, pg))]
        foot = [s for s in ts if s.startswith('Lucerna · SEMANARIO')]
        pl = [s for s in ts if re.match(r'Página \d de 8', s)]
        print(f"  {pg}: footer={foot} pageline={pl}")
    p1 = [s for _, _, _, s in text_attrs(os.path.join(d, 'p1-touiban.svg'))]
    print("  P1 strap:", [s for s in p1 if 'SEMANARIO CHINO' in s])
    print("  P1 strapline:", [s for s in p1 if '给学中文的人的周报' in s])
    print("  P1 top strip:", [s for s in p1 if '每周读中文' in s])
    print("  masthead The/Le counts:", sum(1 for s in p1 if 'The Lucerna' in s), sum(1 for s in p1 if 'Le Lucerna' in s))
    p8 = [s for _, _, _, s in text_attrs(os.path.join(d, 'p8-ceyan.svg'))]
    print("  P8 header:", [s for s in p8 if 'Claves' in s or 'Todas las notas' in s])
    print("  P8 dash sample:", [s for s in p8 if re.match(r'\d+\. .* — ', s)][:3])
    print("  P8 writing sample:", [s for s in p8 if '✓' in s][:3])

print("=== GATE 11 glosslines ===")
for d, name in [(ED, 'edition')]:
    alls = {}
    for f in sorted(glob.glob(os.path.join(d, '*.svg'))):
        alls[os.path.basename(f)] = ''.join(s for _, _, _, s in text_attrs(f))
    print("  P1 glossline 'primer término solar del invierno' on P1:",
          'primer término solar del invierno' in alls['p1-touiban.svg'])
    print("  old 凌晨 wording 'las horas pequeñas después de medianoche' anywhere:",
          [pg for pg, c in alls.items() if 'las horas pequeñas después de medianoche' in c])
    print("  new 凌晨 wording 'las primeras horas tras medianoche' anywhere:",
          [pg for pg, c in alls.items() if 'las primeras horas tras medianoche' in c])
    print("  P1 glossline full:", [s for _, _, _, s in text_attrs(os.path.join(d, 'p1-touiban.svg')) if 'primer término' in s])
