import re, html, pathlib, hashlib, collections
base=pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations"
def texts(path):
    s=path.read_text(encoding='utf-8'); out=[]
    for m in re.finditer(r'<text\b([^>]*)>(.*?)</text>', s, flags=re.S):
        out.append(html.unescape(re.sub(r'<[^>]+>','',m.group(2))))
    return out
print("=== GLOSS split-on-· counts ===")
gloss={'p2-vida':("译注｜festivo 放假的 · el puente 连休 · la comunidad 自治区 · anochecer 天黑 · el horario de invierno 冬令时。",
                  "Nota — festivo (de festa) · el puente (a ponte) · la comunidad (a comunidade autónoma) · anochecer (anoitecer) · el horario de invierno (o horário de inverno)."),
 'p3-cultura':("译注｜sobrio 克制的 · el homenaje 纪念表彰 · el disfraz 服装（化装） · el boniato 红薯 · el cementerio 墓地。",
                  "Nota — sobrio (sóbrio) · el homenaje (a homenagem) · el disfraz (o disfarce) · el boniato (a batata-doce) · el cementerio (o cemitério)."),
 'p4-deporte':("译注｜la jornada 轮次 · recortar la distancia 缩小分差 · recibir 主场迎战 · visitar 客场挑战 · el Metropolitano 马竞主场。",
                  "Nota — la jornada (a jornada) · recortar la distancia (reduzir a diferença) · recibir (jogar em casa) · visitar (jogar fora) · el Metropolitano (o estádio do Atlético)."),
 'p5-juventud':("译注｜el emparrillado 美式足球场（烤架形场地） · el himno 国歌 · el touchdown 达阵得分 · la calabaza 南瓜。",
                  "Nota — el emparrillado (o campo com forma de grelha) · el himno (o hino) · el touchdown (o touchdown) · la calabaza (a abóbora).")}
for f,(c,e) in gloss.items():
    # verify joined strings actually occur in SVGs (joined from elements)
    ct=' '.join(texts(base/f"files/weekly-report-w45-es-core/svg/{f}.svg"))
    et=' '.join(texts(base/f"files/weekly-report-w45-es-pt/svg/{f}.svg"))
    # normalise: core gloss wraps: '译注｜festivo 放假的 · el puente 连休 · ...' - check headwords order instead
    print(f"  {f}: core split={len(c.split('·'))} ed split={len(e.split('·'))}")
    # headwords: first token(s) before space/paren in each segment after stripping prefix
    def heads(s, prefix):
        s2=s.split(prefix,1)[1] if prefix in s else s
        return [seg.strip().split('(')[0].strip() for seg in s2.split('·')]
    print(f"    core heads: {heads(c,'｜')}")
    print(f"    ed   heads: {heads(e,'— ')}")
print("\n=== IMAGES in SVGs ===")
for pg,f in [('P1','p1-portada'),('P2','p2-vida'),('P3','p3-cultura'),('P4','p4-deporte'),('P5','p5-juventud'),('P6','p6-afondo'),('P7','p7-lengua'),('P8','p8-ejercicios')]:
    for label,root in [('CORE','files/weekly-report-w45-es-core/svg'),('ED','files/weekly-report-w45-es-pt/svg')]:
        s=(base/f"{root}/{f}.svg").read_text(encoding='utf-8')
        imgs=re.findall(r'<image\b([^>]*?)/?>', s)
        if imgs: print(f"  {pg} {label}: {imgs}")
        # also data URIs?
        if 'data:image' in s: print(f"  {pg} {label}: HAS data:image (len {len(s)})")
print("\n=== asset files MD5 (build assets vs core build assets) ===")
import glob
for name in ['castanas.jpg','kuerbis.jpg','atomuhr.jpg','halloween1910.jpg']:
    for d in ['hidden_files/weekly-report-w45-es-pt-build/assets','hidden_files/weekly-report-w45-es-build/assets']:
        p=base/d/name
        if p.exists(): print(f"  {d}/{name}: {hashlib.md5(p.read_bytes()).hexdigest()} {p.stat().st_size}B")
print("\n=== image credits in SVGs (P3/P5) ===")
for f in ['p3-cultura','p5-juventud']:
    for label,root in [('CORE','files/weekly-report-w45-es-core/svg'),('ED','files/weekly-report-w45-es-pt/svg')]:
        ts=texts(base/f"{root}/{f}.svg")
        cred=[t for t in ts if 'Commons' in t or 'Wikimedia' in t or 'USDA' in t or 'Crédito' in t or '来源' in t or '图片' in t]
        print(f"  {f} {label} credit-ish: {cred}")
