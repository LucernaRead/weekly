# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · TAAL (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("TAAL · 언어", "De Lucerna", "언어에 집중 · Drie niveaus, drie gereedschappen · 세 단계, 세 가지 도구")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · KLIMAATWOORDEN", 24)
a.para("De woorden van deze week horen bij de Klimaatweek: het klimaat, de boom planten, besparen en de waarschuwing. Het klimaat is het weer en de natuur over een lange tijd — niet het weer van vandaag.", 21.5)
a.para("En de codes: geel is let op, oranje is gevaarlijk, rood is blijf binnen. Onthoud ook: een waarschuwing geldt voor jouw eigen omgeving.", 21.5)
a.bridge("het klimaat 기후(장기적인); een boom planten 나무 심기; besparen 절약하기; de waarschuwing 경보.")
a.ex("A2", "문장 완성", "planten", "wij → planten",
     "In de Klimaatweek ___ (planten) wij een boom.", instr="빈칸 채우기", size=20.5, gap=10)
a.ex("A2", "문장 완성", "bespaar", "je → bespaar",
     "Met de fiets ___ (besparen) je energie.", instr="빈칸 채우기", size=20.5, gap=10)
a.ex("A2", "객관식", "B", "기후는 장기적인 날씨와 자연이에요",
     "«Het klimaat» is... A. het weer van vandaag · B. het weer en de natuur over een lange tijd · C. een museum", size=20.5, gap=10)
a.ex("A2", "문장 완성", "blijf", "rood = blijf binnen",
     "Code rood betekent: ___ binnen.", instr="빈칸 채우기", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · SCHEIDBARE WERKWOORDEN", 24)
b.para("Deze week doen we iets met scheidbare werkwoorden: meedoen (deed mee, meegedaan), opruimen (ruimde op, opgeruimd) en vastzetten (zette vast, vastgezet). Het eerste deel gaat in de zin naar het einde.", 21.5)
b.para("Voorbeeld: «Ik doe mee aan de Klimaatweek.» «Wij hebben de tuin opgeruimd.» «Zij zette de losse spullen vast.» Let op de volgorde: het deel staat achteraan.", 21.5)
b.bridge("meedoen 참여하다: ik doe mee; opruimen 치우다: wij hebben de tuin opgeruimd; vastzetten 고정하다: zij zette vast.")
b.ex("B1", "문장 완성", "doe mee", "ik → doe mee",
     "Ik ___ (meedoen) aan de Klimaatweek.", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "문장 완성", "opgeruimd", "opruimen의 과거분사: opgeruimd",
     "Wij hebben de tuin ___ (opruimen).", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "문장 완성", "zette vast", "vastzetten 과거형: zette vast",
     "Zij ___ (vastzetten) de losse spullen.", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "객관식", "B", "meedoen = 참여하다",
     "«Meedoen» betekent... A. meekijken · B. deelnemen, erbij zijn · C. weggaan", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · EEN MENING GEVEN", 24)
c.para("Over het klimaat heeft iedereen een mening. Beleefd geef je die zo: «Ik vind dat ...», «Volgens mij ...» of «Het lijkt me dat ...» Zo praat je mee over de Klimaatweek én over de codes van het KNMI.", 21.5)
c.para("Voorbeeld: «Volgens mij moet iedereen meedoen.» «Het lijkt me dat lokaal waarschuwen beter is.» Een mening is geen feit — zeg er dus bij dat het jouw mening is.", 21.5)
c.bridge("Ik vind dat… 저는 ~라고 생각해요; Volgens mij… 제 생각에는; Het lijkt me dat… ~인 것 같아요.")
c.ex("B2", "문장 완성", "Volgens", "Volgens mij… = 제 생각에는",
     "___ mij moet iedereen meedoen aan de Klimaatweek.", instr="빈칸 채우기", size=20.5, gap=10)
c.ex("B2", "객관식", "B", "Ik vind dat… 생각을 말할 때 써요",
     "«Ik vind dat iedereen moet meedoen» is... A. een bevel · B. een mening · C. een vraag", size=20.5, gap=10)
c.ex("B2", "문장 완성", "lijkt", "Het lijkt me dat… = 제 생각에는 ~인 것 같아요",
     "Het ___ me dat lokaal waarschuwen beter is.", instr="빈칸 채우기", size=20.5, gap=10)
c.ex("B2", "문장 완성", "mij", "Volgens mij… = 제 생각에는",
     "Volgens ___ is fietsen beter dan autorijden.", instr="빈칸 채우기", size=20.5, gap=10)
c.end_report()

# ---- col 3: pas op + het woord + brieven ----
bx = COLX[3]
errs = [
    ("«Het klimaat is slecht weer.»", "→ Fout: het klimaat is het weer over een lange tijd.", "기후는 장기적인 날씨와 자연이지, 오늘 날씨가 아니에요."),
    ("«Ik doe mee aan de klimaatweek.»", "→ «Klimaatweek» krijgt een hoofdletter: het is een naam.", "Klimaatweek는 고유명사라서 첫 글자를 대문자로 써요."),
    ("«Ik plant een bomen.»", "→ «Een» is enkelvoud: «een boom» of «bomen».", "een은 단수예요: een boom, 복수는 그냥 bomen."),
    ("«Omdat het regent, ik blijf thuis.»", "→ Na «omdat» staat het werkwoord op plaats 2: «... blijf ik thuis.»", "omdat 절 뒤에서는 본문 동사가 2번 자리에 와요: blijf ik thuis."),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 192
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "PAS OP! · 실수 클리닉", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 18
wt = "«meedoen» betekent: deelnemen, erbij zijn. In de Klimaatweek doet heel Nederland mee."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("meedoen = 참여하다: 기후 주간에는 모두가 참여해요.", "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "HET WOORD · 이번 주 단어", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "meedoen = 참여하다: 기후 주간에는 모두가 참여해요.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 18
lt = "«Hallo! Ik ben Li en ik leer Nederlands in Shanghai. In de Klimaatweek plant ik een boom op mijn balkon!» — Li (voorbeeldbrief van de redactie)"
# Fix-1 disclosure (independent proof Problem 2): on-page, Dutch + matching Chinese.
# No real letters/best P8 texts had arrived by press time, so the labeled example
# stands and the promise carries to VOL.3. Existing labeling/invitation kept verbatim.
dt_nl = "Ter perse: nog geen echte brieven of beste pagina-8-teksten binnen — daarom dit voorbeeld; belofte naar VOL.3."
dt_zh = "마감 때까지 실제 독자 편지나 8면 최고 작문이 들어오지 않아서, 이 예시를 싣고 약속은 VOL.3으로 이어져요."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(dt_nl, "serif", False, 21.5, CW - 44)) * 30.5 + 10 + len(wrap(dt_zh, "sans", False, 20, CW - 44)) * 29 + 10 + len(wrap("편집부 예시예요(실제 편지가 아니에요). 여러분의 실제 편지와 8면 최고 작문을 보내 주세요. VOL.3에 실어 드릴게요!", "sans", False, 20, CW - 44)) * 29 + 34 + 50
# +50 measured correction: rendered inter-paragraph spacing runs ~20px above the
# formula per added paragraph (verified on the rendered SVG: last baseline sat
# 21px below the box edge before this correction).
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "BRIEVEN VAN LEZERS", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 21, dt_nl, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 20, dt_zh, 20, "sans", False, GREY, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "편집부 예시예요(실제 편지가 아니에요). 여러분의 실제 편지와 8면 최고 작문을 보내 주세요. VOL.3에 실어 드릴게요!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- zinnen van de week (verbatim from this issue) ----
# Fix-1 layout only: fy moved down for the taller BRIEVEN box; row pitch
# 158 -> 90 (rows have ~77px of content from quote top to Chinese descender,
# so 90px still leaves a clear gap); no quote text changed.
fy = 1951
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "ZINNEN VAN DE WEEK · 이번 주 금문장(본문에서 그대로 가져왔어요)", 27, "sans", True, OLIVE)
quotes = [
    ("«Van maandag 2 tot en met zondag 8 november is het Klimaatweek in Nederland»", "11월 2일 월요일부터 8일 일요일까지 네덜란드는 기후 주간이에요.", "Pagina 1"),
    ("«De herfst is de beste tijd om te planten»", "가을은 나무를 심기에 가장 좋은 계절이에요.", "Pagina 1"),
    ("«Geel betekent: let op, het weer kan gevaarlijk zijn»", "노란색은 주의하라는 뜻이에요. 날씨가 위험할 수 있어요.", "Pagina 2"),
    ("«Meer dan 70 musea zijn open van 19:00 uur 's avonds tot 02:00 uur 's nachts»", "70곳이 넘는 박물관이 저녁 7시부터 새벽 2시까지 문을 열어요.", "Pagina 3"),
    ("«Ajax won donderdag 22 oktober met 2–0 van Atalanta»", "아약스가 10월 22일 목요일에 아탈란타를 2-0으로 이겼어요.", "Pagina 4"),
    ("«Zondag 1 november begon Expeditie Robinson op RTL 4, om 20:00 uur»", "11월 1일 일요일, 로빈슨이 RTL 4에서 저녁 8시에 시작했어요.", "Pagina 5"),
    ("«Een code is geen verbod, maar een advies»", "경보 코드는 금지령이 아니라 조언이에요.", "Pagina 6"),
    ("«Het weer is van ons allemaal, maar het raakt ons allemaal anders»", "날씨는 우리 모두의 것이지만, 우리 모두에게 다르게 다가와요.", "Pagina 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 90
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- volgende week ----
# Fix-1 layout only: py moved down (fy shift minus pitch saving); text unchanged.
py = 2439
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "VOLGENDE WEEK · 다음 호 예고 (VOL.3)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "Zondag 15 november komt Sinterklaas aan in Amsterdam. En woensdag 11 november is het Sint-Maarten: kinderen gaan met lampionnen langs de deuren. Verder: jullie brieven en de beste teksten van pagina 8. Tot maandag!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-taal.svg")
print("P7 saved, exercises so far:", len(REG))
