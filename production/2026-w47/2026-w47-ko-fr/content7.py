# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 말 공부 (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("말 공부　Étude de la langue", "Lucerna", "언어 포커스　세 가지 레벨, 세 가지 주제　Trois niveaux, trois thèmes")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　김치의 날의 말", 24)
a.para("11월 22일은 김치의 날이에요. 김치의 날은 2020년 2월에 법으로 정한 기념일이에요. 김장문화는 유네스코 인류무형문화유산이에요. 김치를 담그는 일을 '김장'이라고 해요. 김장은 가을에 온 가족이 함께 해요.", 21.5)
a.para("김치는 발효 음식이에요. 배추에 양념을 버무리면 시간이 지나면서 맛이 깊어져요. 갓 담근 김치는 아삭하고, 익은 김치는 신맛이 나요. 절임배추를 쓰면 시간을 아낄 수 있어요. 김치, 김장, 발효 — 세 말이 이번 주의 김치를 말해요.", 21.5)
a.glossline("발효 = fermentation · 익다 = fermenter · 아삭하다 = croquant")
a.ex("A2", "Compléter", "김장", "Préparer le kimchi d'hiver = 김장",
     "김치를 담그는 일을 ___이라고 해요.", instr="Compléter", size=20.5, gap=10)
a.ex("A2", "Choix multiple", "A", "Le Jour du kimchi fixé par la loi en fév. 2020",
     "김치의 날은 언제 법으로 정해졌어요? A. 2020년 2월 · B. 2013년 · C. 2022년", size=20.5, gap=10)
a.ex("A2", "Compléter", "절임배추", "Chou salé à l'avance",
     "미리 소금에 절인 배추를 ___라고 해요.", instr="Compléter", size=20.5, gap=10)
a.ex("A2", "Choix multiple", "A", "L'assaisonnement contient des crevettes salées",
     "양념에 들어가는 것은 뭐예요? A. 새우젓 · B. 사과 · C. 야구공", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　날짜 세는 말", 24)
b.para("한국에서는 중요한 날까지 남은 날짜를 'D-3'처럼 써요. 오늘이 11월 16일, 수능이 11월 19일이니까 오늘이 D-3예요. 수요일 11월 18일은 D-1예요. D-1은 '내일 시험'이라는 뜻이에요.", 21.5)
b.para("내일이 바로 그날이면 D-1, 오늘이 바로 그날이면 D-데이예요. 김치의 날은 11월 22일이에요. 수능이 끝나고 사흘 뒤에 김치의 날이 와요.", 21.5)
b.glossline("사흘 = trois jours · 뒤 = après")
b.ex("B1", "Compléter", "D-1", "18 nov. = D-1",
     "수능까지 1일이 남았어요. 오늘이 ___예요.", instr="Compléter", size=20.5, gap=10)
b.ex("B1", "Choix multiple", "B", "D-3 = 16 nov.",
     "D-3은 며칠이에요? A. 11월 19일 · B. 11월 16일 · C. 11월 22일", size=20.5, gap=10)
b.ex("B1", "Compléter", "데이", "19 nov. = D-day",
     "11월 19일은 D-___예요.", instr="Compléter", size=20.5, gap=10)
b.ex("B1", "Choix multiple", "A", "D-1 : l'examen, c'est demain",
     "맞는 말은 어느 것이에요? A. D-1은 내일이 시험 날이라는 뜻이에요 · B. D-1은 1일이 지났어요 · C. D-1은 오늘이 시험 날이에요", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　예보와 결과 읽는 법", 24)
c.para("예보를 읽을 때는 날짜와 함께 '기준'을 봐야 해요. 산림청은 잎의 50%, 기상청 관측은 산 전체의 약 80%를 절정의 기준으로 해요. 기준이 다르면 날짜도 달라져요.", 21.5)
c.para("그리고 '발표'와 '결과'도 나눠야 해요. 발표는 미리 알린 일정, 결과는 경기가 끝난 뒤에 나온 점수예요. 한국시리즈 결과는 11월 8일에 나왔어요. (4면)", 21.5)
c.glossline("기준 = critère · 나누다 = distinguer")
c.ex("B2", "Compléter", "기준", "Les dates diffèrent parce que les critères diffèrent (p. 3)",
     "두 날짜가 다른 이유는 ___이 다르기 때문이에요.", instr="Compléter", size=20.5, gap=10)
c.ex("B2", "Choix multiple", "A", "Le service météo observe environ 80 %",
     "기상청 관측의 절정 기준은 뭐예요? A. 산 전체의 약 80% · B. 잎의 50% · C. 첫눈이 오는 날", size=20.5, gap=10)
c.ex("B2", "Compléter", "결과", "Les résultats ne viennent qu'après les matches",
     "한국시리즈 ___는 경기가 끝난 뒤에 나와요.", instr="Compléter", size=20.5, gap=10)
c.ex("B2", "Choix multiple", "B", "Distinguer annonces et résultats",
     "발표와 결과를 읽을 때 먼저 할 일은 뭐예요? A. 날짜만 보기 · B. 발표인지 결과인지 나누기 · C. 사진 보기", size=20.5, gap=10)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「김치의날이에요」", "→ 띄어 써요: '김치의 날이에요'.", "「김치의 날」 prend un espace."),
    ("「삼성는 우승했어요」", "→ 받침이 있으면 '은'을 써요: '삼성은 우승했어요'.", "Avec une consonne finale, on met 「은」."),
    ("「김치를 담궈요」", "→ '담그다'의 현재형은 '담가요'예요.", "Le présent de 「담그다」, c'est 「담가요」."),
    ("「내일 김치의 날예요」", "→ 받침이 있으면 '이에요'를 써요: '김치의 날이에요'.", "Avec une consonne finale, on met 「이에요」."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44 - 80 if errs.index(r) == 2 else CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "실수 병원　Clinique des fautes", 23, "sans", True, OLIVE)
yy3 += 54
for i, (wrong, right, cn) in enumerate(errs):
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44 - 80 if i == 2 else CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「〜 후에」 — '수능이 끝나면 일요일 11월 22일에는 김치의 날이 와요.' 나중에 하는 일을 말할 때 쓰는 틀이에요. 물어볼 때는 '〜 후에 뭐 해요?'라고 해요."
wcn = "Cadre : 「après ~」. Demandez : 「〜 후에 뭐 해요?」"
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "이번 주의 틀　La structure", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「안녕하세요. 저는 수험생이에요. 수요일에는 예비소집에 가요. 목요일에는 수능을 봐요. 일요일에는 가족과 김치를 나눠 먹어요. 수능이 끝나면 한능검 시험을 준비해요.」 — 독자 편지의 예"
lcn = "Note de la rédaction : cette lettre est un exemple rédigé par la rédaction, pas une vraie lettre. Aucune vraie lettre ni aucun meilleur texte de la page 8 n'était arrivé au bouclage ; l'exemple reste et la promesse passe au VOL.5. À vous — deux phrases en coréen !"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "독자의 편지　Courrier des lecteurs", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42) + 10

col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- kimchi-making photo (W47 new: P7 gets a PD image) ----
# Placed in the empty band below the three language columns (cols 0-2 end
# ~1100-1130); phrases section starts at fy >= 1712, so the strip fits.
iy7 = 1180
# W47-KO fix3: photo spans cols 0-2 only: width = 3*CW + 2*GUT = 1323.5
# (the old literal 1388 ran 36.5px into col 4 and covered the col-4 boxes'
# left edge after the MX 65 -> 88 margin change)
image(p, "kimchi-making.jpg", MX, iy7, span_x(0, 3)[1], 380)
cy7 = caption(p, MX, iy7 + 380, span_x(0, 3)[1],
        "김치를 담그는 손. 김장철에 찍은 사진이에요. 김치의 날 이야기는 3면에 있어요.",
        "사진: Anattadairy — CC0 (Wikimedia Commons) · 자료 사진")
print("P7 photo ends", cy7)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "이번 주의 문장　Phrases de la semaine (tirées de ce numéro)", 27, "sans", True, OLIVE)
quotes = [
    ("「수능까지 3일 남았어요. 오늘이 D-3예요」", "Plus que 3 jours avant le CSAT — aujourd'hui, c'est D-3.", "2면"),
    ("「김장비용은 4인 가족 20포기 기준 199,456원이에요」", "Kimjang pour une famille de quatre, 20 choux : 199 456 wons.", "1면"),
    ("「삼성이 12년 만에 우승했어요」", "Samsung a gagné le titre après 12 ans.", "4면"),
    ("「11월 22일은 김치의 날이에요」", "Le 22 nov., c'est le Jour du kimchi.", "2면"),
    ("「예보 날짜와 실제 관측 날짜는 달라요」", "Les dates prévues diffèrent des dates observées.", "3면"),
    ("「결과를 점수와 함께 전했어요」", "Il a rapporté les résultats avec les scores.", "6면"),
    ("「수능이 끝나면 일요일 11월 22일에는 김치의 날이 와요」", "Après le CSAT, c'est le Jour du kimchi.", "1면"),
    ("「발표가 결과로 바뀐 것이에요」", "Une annonce est devenue un résultat.", "6면"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 124
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 124 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "다음 주　La semaine prochaine (VOL.5)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "다음 주에는 한능검 시험이 있어요. 11월 28일 토요일, 한국사 시험 소식을 전해요. 수능이 끝난 뒤의 이야기와 김치의 날 뒤이야기도 있어요. 여러분의 편지와 8면 쓰기 우수작도 실어요. 기대해 주세요!", 21, "serif", False, ONCLOTH, RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-mal.svg")
print("P7 saved, exercises so far:", len(REG))
