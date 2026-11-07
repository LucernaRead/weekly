import re, html, pathlib
base=pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations"
def els(path):
    s=path.read_text(encoding='utf-8'); out=[]
    for m in re.finditer(r'<text\b([^>]*)>(.*?)</text>', s, flags=re.S):
        a=m.group(1); t=html.unescape(re.sub(r'<[^>]+>','',m.group(2)))
        fs=float(re.search(r'font-size="([\d.]+)"',a).group(1)) if re.search(r'font-size="([\d.]+)"',a) else 0
        x=float(re.search(r'x="([\d.]+)"',a).group(1)); y=float(re.search(r'y="([\d.]+)"',a).group(1))
        out.append((x,y,fs,t))
    return out
print("=== (a) P7 letter attribution: W43 vs W45-core vs W45-ED ===")
for label,root,f in [('W43','files/weekly-report-es-pt/svg','p7-lengua'),('W45CORE','files/weekly-report-w45-es-core/svg','p7-lengua'),('W45ED','files/weekly-report-w45-es-pt/svg','p7-lengua')]:
    ts=els(base/f"{root}/{f}.svg")
    for x,y,fs,t in ts:
        if 'Ana' in t and ('ejemplo' in t or 'exemplo' in t or 'redacción' in t or 'redac' in t):
            print(f"  {label}: {t!r}  fullwidth parens: {'（' in t or '）' in t} halfwidth: {'(' in t or ')' in t}")
    # also print all Ana lines
    for x,y,fs,t in ts:
        if t.strip().startswith('«¡Hola!') or 'Soy Ana' in t:
            pass
print("\n=== (b) P8 separators ===")
for label,root in [('W43','files/weekly-report-es-pt/svg'),('W45CORE','files/weekly-report-w45-es-core/svg'),('W45ED','files/weekly-report-w45-es-pt/svg')]:
    ts=els(base/f"{root}/p8-ejercicios.svg")
    seps=sorted(set(t for x,y,fs,t in ts if t.startswith('— ') and ('PÁGINA' in t or 'Página' in t or 'SEITE' in t)))
    print(f"  {label}: {seps}")
    hdrs=[t for x,y,fs,t in ts if 'RESPUESTAS' in t]
    print(f"    RESPUESTAS header: {hdrs}")
print("\n=== (c) rendered instruction chips + section/type headers: W43 vs W45ED ===")
def chips(root):
    s=set()
    for f in ['p2-vida','p3-cultura','p4-deporte','p5-juventud','p6-afondo','p7-lengua','p8-ejercicios']:
        for x,y,fs,t in els(base/f"{root}/{f}.svg"):
            s.add(t)
    return s
w43=chips('files/weekly-report-es-pt/svg'); ed=chips('files/weekly-report-w45-es-pt/svg')
# instruction chips are short PT strings; list W43 chips that look like instructions
import re
cands_w43=sorted(t for t in w43 if re.fullmatch(r'(Complete|Verdadeiro ou falso|Forme a frase|Reescreva|Traduza|Escreva|Associe|Completa|Escolha.*|Preencha.*)', t))
print("  W43 chip candidates:", cands_w43)
cands_ed=sorted(t for t in ed if re.fullmatch(r'(Complete|Verdadeiro ou falso|Forme a frase|Reescreva|Traduza|Escreva|Associe|Completa|Escolha.*|Preencha.*)', t))
print("  ED chip candidates:", cands_ed)
# full distinct-text diff restricted to short furniture-like strings (<=40 chars, no digits-heavy): show W43-only and ED-only among band/header/footer-ish
for label,ss in [('W43-only', w43-ed), ('ED-only', ed-w43)]:
    short=sorted(t for t in ss if len(t)<=45)
    print(f"  {label} short strings ({len(short)}):")
    for t in short: print(f"    {t!r}")
