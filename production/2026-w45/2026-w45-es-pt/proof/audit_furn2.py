import re, html, pathlib, sys
sys.path.insert(0, str(pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-es-pt-build"))
base=pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations"
def els(root,f):
    s=(base/f"{root}/{f}.svg").read_text(encoding='utf-8'); out=[]
    for m in re.finditer(r'<text\b([^>]*)>(.*?)</text>', s, flags=re.S):
        out.append((m.group(1), html.unescape(re.sub(r'<[^>]+>','',m.group(2)))))
    return out
for label,root in [('W43','files/weekly-report-es-pt/svg'),('W45ED','files/weekly-report-w45-es-pt/svg')]:
    print(f"===== {label} P1 furniture full =====")
    for a,t in els(root,'p1-portada'):
        if any(k in t for k in ['Os cinco temas','Nada inventado','Para entender','Leia a capa','Quiz','cinco temas']):
            print(f"  {t!r} :: {a[:150]}")
    print(f"  -- badge element attrs --")
    for a,t in els(root,'p1-portada'):
        if 'EDIÇÃO PARA OS LEITORES' in t: print(f"  {a}")
    print(f"  -- Y TU / SABIAS --")
    for f in ['p2-vida','p3-cultura','p4-deporte','p5-juventud']:
        for a,t in els(root,f):
            if '¿Y TÚ?' in t or 'SABÍAS' in t: print(f"  {f}: {t!r}")
    print(f"  -- P2 box titles (all texts y 400-600, fs>=19) --")
    for a,t in els(root,'p2-vida'):
        y=float(re.search(r'y="([\d.]+)"',a).group(1)); fs=float(re.search(r'font-size="([\d.]+)"',a).group(1))
        if 400<=y<=650 and fs>=19: print(f"  y={y} fs={fs} :: {t!r}")
    print(f"  -- P5 box titles --")
    for a,t in els(root,'p5-juventud'):
        y=float(re.search(r'y="([\d.]+)"',a).group(1)); fs=float(re.search(r'font-size="([\d.]+)"',a).group(1))
        if 'PLAN' in t or 'CALEND' in t: print(f"  y={y} fs={fs} :: {t!r}")
    print(f"  -- section headers (A · / B · / C · / D · / E · / F · / G · / H ·) P8 --")
    for a,t in els(root,'p8-ejercicios'):
        if re.match(r'^[A-H] · ', t): print(f"  {t!r}")
print("\n=== title-line ink width (rowcheck measure) ===")
import svglib
def measure(t, kind, bold, size):
    fnt=svglib._font(kind, bold, int(round(size*4)))
    bb=fnt.getbbox(t); return bb[0]/4.0, bb[2]/4.0, fnt.getlength(t)/4.0
for label,root in [('W45ED','files/weekly-report-w45-es-pt/svg')]:
    for a,t in els(root,'p1-portada'):
        if 'SEMANÁRIO ESPANHOL · VOL.2' in t:
            print(f"  attrs: {a}")
            bold='font-weight="700"' in a; kind='serif' if 'Serif' in a else 'sans'
            fs=float(re.search(r'font-size="([\d.]+)"',a).group(1)); x=float(re.search(r'x="([\d.]+)"',a).group(1))
            l,r,adv=measure(t,kind,bold,fs)
            print(f"  kind={kind} bold={bold} fs={fs} x={x} ink=({l:.1f},{r:.1f}) adv={adv:.1f} ink_end_x={x+r:.1f} (page width 1950, KIT claims 1715.5)")
print("\n=== top-strip ink end vs date ink start (F1 check) ===")
for label,root in [('W45ED','files/weekly-report-w45-es-pt/svg')]:
    ts=els(root,'p1-portada')
    for a,t in ts:
        if 'SEMANAL EN ESPAÑOL' in t:
            fs=float(re.search(r'font-size="([\d.]+)"',a).group(1)); x=float(re.search(r'x="([\d.]+)"',a).group(1)); bold='font-weight="700"' in a; kind='serif' if 'Serif' in a else 'sans'
            l,r,adv=measure(t,kind,bold,fs); print(f"  strip: x={x} ink_end={x+r:.1f} (KIT 1406.3)")
        if '2 – 8 de novembro' in t or 'novembro' in t.lower() and '2' in t:
            print(f"  date-ish: {t!r} :: {a[:160]}")
