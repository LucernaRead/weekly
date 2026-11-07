import re, html, pathlib, sys
sys.path.insert(0, str(pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-es-pt-build"))
import svglib
base=pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations"
def els(root,f):
    s=(base/f"{root}/{f}.svg").read_text(encoding='utf-8'); out=[]
    for m in re.finditer(r'<text\b([^>]*)>(.*?)</text>', s, flags=re.S):
        a=m.group(1); t=html.unescape(re.sub(r'<[^>]+>','',m.group(2)))
        fs=float(re.search(r'font-size="([\d.]+)"',a).group(1)); x=float(re.search(r'x="([\d.]+)"',a).group(1)); y=float(re.search(r'y="([\d.]+)"',a).group(1))
        bold='font-weight="700"' in a; anchor=re.search(r'text-anchor="(\w+)"',a); anchor=anchor.group(1) if anchor else 'start'
        fam='serif' if 'Serif' in a else 'sans'
        out.append((x,y,fs,bold,anchor,fam,t,a))
    return out
def ink(t, fam, bold, fs):
    fnt=svglib._font(fam, bold, int(round(fs*4))); bb=fnt.getbbox(t); return bb[0]/4.0, bb[2]/4.0, fnt.getlength(t)/4.0
def span(x, fs, bold, anchor, fam, t):
    l,r,adv=ink(t,fam,bold,fs)
    if anchor=='start': return x+l, x+r
    if anchor=='end': return x-adv+l, x-adv+r
    return x-adv/2+l, x-adv/2+r
print("=== W43 P8 right text / P7 FOCO ===")
for a_t in els('files/weekly-report-es-pt/svg','p8-ejercicios'):
    if 'Cada resposta' in a_t[7] or 'marca' in a_t[7]: print(f"  W43 P8: {a_t[7]!r}")
for a_t in els('files/weekly-report-es-pt/svg','p7-lengua'):
    if 'FOCO' in a_t[7] or 'Tres niveles' in a_t[7]: print(f"  W43 P7: {a_t[7]!r}")
for a_t in els('files/weekly-report-w45-es-pt/svg','p8-ejercicios'):
    if 'Cada resposta' in a_t[7]: print(f"  ED P8: {a_t[7]!r}")
print("\n=== F1: P1 top strip vs date line, same row y=92 ===")
for x,y,fs,bold,anchor,fam,t,a in els('files/weekly-report-w45-es-pt/svg','p1-portada'):
    if y==92.0: print(f"  y=92 :: {t!r} attrs={a[:170]} span={span(x,fs,bold,anchor,fam,t)}")
print("\n=== F2: box title ink widths (slot 416 per KIT) ===")
for f,pat,ship,core in [('p1-portada','CIFRAS',20,23),('p2-vida','CALENDARIO',19,20),('p5-juventud','PLAN DEL PUENTE',20,23),('p7-lengua','ERRORES',20,20),('p7-lengua','PALABRA',22,22)]:
    for x,y,fs,bold,anchor,fam,t,a in els('files/weekly-report-w45-es-pt/svg',f):
        if pat in t:
            l,r,adv=ink(t,fam,bold,fs); l2,r2,adv2=ink(t,fam,bold,core)
            print(f"  {f} {t!r}: shipped fs={fs} ink_width={r-l:.1f} adv={adv:.1f} | at core fs={core} ink_width={r2-l2:.1f} adv={adv2:.1f} | slot 416 -> shipped fits: {r-l<416}")
print("\n=== F3: paren spacing counts ===")
# CIFRAS box P1: texts in box region; calendar box P2; PLAN box P5: count ' (' in gloss lines
for f,box in [('p1-portada','CIFRAS'),('p2-vida','CALENDARIO'),('p5-juventud','PLAN')]:
    ts=els('files/weekly-report-w45-es-pt/svg',f)
    # gloss lines: lines containing '(' in the box area - print all lines with '(' and whether preceded by space
    print(f"  {f}:")
    for x,y,fs,bold,anchor,fam,t,a in ts:
        if '(' in t:
            # check each '(' preceded by space or start
            bad=[i for i,ch in enumerate(t) if ch=='(' and i>0 and t[i-1]!=' ']
            print(f"    y={y} :: {t[:110]!r}  paren-without-preceding-space: {bad}")
print("\n=== F4: P1 word note ===")
for x,y,fs,bold,anchor,fam,t,a in els('files/weekly-report-w45-es-pt/svg','p1-portada'):
    if 'Pré-campanha' in t:
        l,r,adv=ink(t,fam,bold,fs); print(f"  y={y} fs={fs} ink_width={r-l:.1f} adv={adv:.1f} (KIT 419.9 < 434) :: {t!r} attrs={a[:150]}")
        print(f"  rule y=1844 clearance: note y={y} (baseline) vs rule 1844")
print("\n=== P1 word-note rule element ===")
s=(base/"files/weekly-report-w45-es-pt/svg/p1-portada.svg").read_text(encoding='utf-8')
for m in re.finditer(r'<line\b([^>]*?)/?>', s):
    a=m.group(1); ym=re.search(r'y1="([\d.]+)"',a)
    if ym and 1830<float(ym.group(1))<1860: print(f"  line: {a}")
