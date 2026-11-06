from PIL import ImageFont
import re
SERIF_R = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc"
SERIF_B = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc"
SANS_R = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
SANS_B = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
SC = 2
def adv(path, size, text, bold=False):
    f = ImageFont.truetype(path, size, index=SC)
    # PIL getlength = advance
    return f.getlength(text)
def ink(path, size, text):
    f = ImageFont.truetype(path, size, index=SC)
    bb = f.getbbox(text)  # (l,t,r,b) relative to anchor origin top-left? getbbox returns offset box
    return bb
# 1. masthead edition line 40pt serif bold
line = "JOURNAL PORTUGAIS · VOL.2 · A SEMANA DO ENEM · FINADOS · O FUTEBOL DECIDE"
print("masthead 40pt serif-bold advance:", adv(SERIF_B, 40, line), " (centered x=975 -> left", 975-adv(SERIF_B,40,line)/2, "right", 975+adv(SERIF_B,40,line)/2, ")")
print("masthead 40pt serif-regular advance:", adv(SERIF_R, 40, line))
# 2. ERROS titles 23pt sans (weight? node has no weight -> regular; also bold for comparison)
for s in ["ERROS COMUNS · ERREURS", "ERROS COMUNS · ERREURS FRÉQUENTES"]:
    print(f"ERROS {s!r} sans-reg 23 advance:", adv(SANS_R, 23, s), "sans-bold 23:", adv(SANS_B, 23, s), " ink-right from x=1473 reg:", 1473+adv(SANS_R,23,s))
# 3. badge 19pt BRICK? badge font: check node font-family
t = open('files/weekly-report-w45-pt-fr/svg/p1-capa.svg', encoding='utf-8').read()
m = re.search(r'<text[^>]*y="372"[^>]*>(.*?)</text>', t, re.S)
print("badge node:", t[t.rfind('<text',0,m.start()):m.start()+10] if m else None)
# 4. numbers box title
t1 = open('files/weekly-report-w45-pt-fr/svg/p1-capa.svg', encoding='utf-8').read()
for m in re.finditer(r'<text[^>]*>([^<]*NÚMEROS[^<]*)</text>', t1):
    start = t1.rfind('<text', 0, m.start())
    print("numbers title node:", t1[start:m.start()+6], repr(m.group(1)))
