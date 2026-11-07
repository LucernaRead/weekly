# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-ko-de/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 말 공부 (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("말 공부 · Sprache", "Lucerna", "언어 포커스 · 세 가지 레벨, 세 가지 주제 · Drei Niveaus, drei Themen")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 김장의 말", 24)
a.para("겨울 김치를 담그는 일을 '김장'이라고 해요. 김장이 한창이면 온 집안이 바빠요. 배추를 소금에 절이고, 양념을 버무려요. 양념에는 고춧가루, 마늘, 생강, 새우젓이 들어가요.", 21.5)
a.para("김장을 담글 때는 '절임배추'를 쓰기도 해요. 절임배추는 미리 소금에 절인 배추예요. 절임배추를 쓰면 시간을 아낄 수 있어요. 김장, 절임배추, 양념 — 세 말이 이번 주의 김장을 말해요.", 21.5)
a.glossline("미리 = im Voraus · 아끼다 = sparen · 들어가다 = hineingehen")
a.ex("A2", "Satz ergänzen", "김장", "Kimjang = Winter-Kimchi",
     "겨울 김치를 담그는 일을 ___이라고 해요.", instr="Ausfüllen", size=20.5, gap=10)
a.ex("A2", "Auswahl", "A", "Kimjang ist in vollem Gange",
     "'김장이 한창이에요'는 무슨 뜻이에요? A. 김장이 한창 바빠요 · B. 김장이 끝났어요 · C. 김장을 안 해요", size=20.5, gap=10)
a.ex("A2", "Satz ergänzen", "절임배추", "Im Voraus gesalzener Chinakohl",
     "미리 소금에 절인 배추를 ___라고 해요.", instr="Ausfüllen", size=20.5, gap=10)
a.ex("A2", "Auswahl", "A", "Die Würze enthält Garnelen",
     "양념에 들어가는 것은 뭐예요? A. 새우젓 · B. 사과 · C. 야구공", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 날짜 세는 말", 24)
b.para("한국에서는 중요한 날까지 남은 날짜를 'D-10'처럼 써요. 오늘이 11월 9일, 수능이 11월 19일이니까 오늘이 D-10예요. 목요일 11월 12일은 D-7예요. D-7은 '일주일이 남았다'는 뜻이에요.", 21.5)
b.para("내일이 바로 그날이면 D-1, 오늘이 바로 그날이면 D-데이예요. 달력에서 날짜를 셀 때 자주 쓰는 말이에요. D-4는 11월 15일이에요.", 21.5)
b.glossline("남다 = übrig bleiben · 딱 = genau")
b.ex("B1", "Satz ergänzen", "D-7", "Der 12. November ist D-7",
     "수능까지 7일이 남았어요. 오늘이 ___예요.", instr="Ausfüllen", size=20.5, gap=10)
b.ex("B1", "Auswahl", "B", "D-4 = 15. November",
     "D-4는 며칠이에요? A. 11월 9일 · B. 11월 15일 · C. 11월 19일", size=20.5, gap=10)
b.ex("B1", "Satz ergänzen", "10", "Der 9. November ist D-10",
     "11월 9일은 D-___예요.", instr="Ausfüllen", size=20.5, gap=10)
b.ex("B1", "Auswahl", "A", "D-7 heißt: noch eine Woche",
     "맞는 말은 어느 것이에요? A. D-7은 일주일이 남았다는 뜻이에요 · B. D-7은 7일이 지났어요 · C. D-7은 오늘이 시험 날이에요", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 예보와 발표 읽는 법", 24)
c.para("예보를 읽을 때는 날짜와 함께 '기준'을 봐야 해요. 산림청은 잎의 50%, 기상청 관측은 산 전체의 약 80%를 절정의 기준으로 해요. 기준이 다르면 날짜도 달라져요.", 21.5)
c.para("그리고 '발표'와 '결과'도 나눠야 해요. 발표는 미리 알린 일정, 결과는 경기가 끝난 뒤에 나온 점수예요. 한국시리즈 결과는 마감일 뒤에 확인하세요. (4면)", 21.5)
c.glossline("기준 = Kriterium · 나누다 = unterscheiden")
c.ex("B2", "Satz ergänzen", "기준", "Daten unterscheiden sich wegen der Kriterien (S. 3)",
     "두 날짜가 다른 이유는 ___이 다르기 때문이에요.", instr="Ausfüllen", size=20.5, gap=10)
c.ex("B2", "Auswahl", "A", "Der Wetterdienst beobachtet etwa 80 %",
     "기상청 관측의 절정 기준은 뭐예요? A. 산 전체의 약 80% · B. 잎의 50% · C. 첫눈이 오는 날", size=20.5, gap=10)
c.ex("B2", "Satz ergänzen", "결과", "Ergebnisse gibt es erst nach den Spielen",
     "한국시리즈 ___는 경기가 끝난 뒤에 나와요.", instr="Ausfüllen", size=20.5, gap=10)
c.ex("B2", "Auswahl", "B", "Ankündigung und Ergebnis unterscheiden",
     "발표와 결과를 읽을 때 먼저 할 일은 뭐예요? A. 날짜만 보기 · B. 발표인지 결과인지 나누기 · C. 사진 보기", size=20.5, gap=10)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「친구에게에게 빼빼로를 줬어요」", "→ 조사는 하나만 써요: '친구에게 빼빼로를 줬어요'.", "Nur eine Partikel."),
    ("「뉴스를 듣었어요」", "→ '듣다'의 과거형은 '들었어요'예요.", "Die Vergangenheit von 듣다 ist 들었어요."),
    ("「11월11일은 빼빼로데이예요」", "→ 날짜는 띄어 써요: '11월 11일은 빼빼로데이예요'.", "Nach Datumsangaben ein Leerzeichen lassen."),
    ("「도서관에 공부해요」", "→ 공부하는 장소는 '에서'예요: '도서관에서 공부해요'.", "Für den Lernort steht 에서."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44 - 80 if errs.index(r) == 2 else CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "실수 병원 · Fehlerklinik", 23, "sans", True, OLIVE)
yy3 += 54
for i, (wrong, right, cn) in enumerate(errs):
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44 - 80 if i == 2 else CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「〜 전에」 — '수능 전에 마지막 정리를 해요.' 먼저 하는 일을 말할 때 쓰는 틀이에요. 물어볼 때는 '〜 전에 뭐 해요?'라고 해요."
wcn = "Satzmuster: „vor ~“. Frage: „〜 전에 뭐 해요?“"
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "이번 주의 틀 · Satzmuster", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「안녕하세요. 저는 고등학생이에요. 수요일에는 친구에게 빼빼로를 나눠 줘요. 토요일에는 가족과 김장을 도와요. 수능이 끝나면 단풍을 보러 가고 싶어요.」 — 독자 편지의 예"
lcn = "Beispiel der Redaktion, kein echter Brief."
lko = "Keine echten Briefe bis Redaktionsschluss. Das Beispiel steht; das Versprechen gilt für VOL.4."
lcn2 = "Schreiben Sie uns Ihren Brief — und Ihren besten Text von Seite 8!"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 12 + len(wrap(lko, "serif", False, 20.5, CW - 44)) * 29 + 12 + len(wrap(lcn2, "sans", False, 20, CW - 44)) * 29 + 66
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "독자의 편지 · Leserecke", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 21, lko, 20.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn2, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "이번 주의 문장 · Sätze der Woche (wörtlich aus dieser Ausgabe)", 27, "sans", True, OLIVE)
quotes = [
    ("「배추 값은 내렸는데 새우젓 값은 올랐어요」", "Chinakohl ist billiger geworden, aber die Garnelen sind teurer geworden.", "1면"),
    ("「11월 11일은 이름이 세 개인 날이에요」", "Der 11. November ist ein Tag mit drei Namen.", "1면"),
    ("「김장이 한창이에요」", "Kimjang ist in vollem Gange.", "2면"),
    ("「수능까지 7일 남았어요. 오늘이 D-7예요」", "Noch 7 Tage bis zur Suneung. Heute ist D-7.", "2면"),
    ("「예보 날짜와 실제 관측 날짜는 달라요」", "Vorhersagedaten und echte Beobachtungsdaten unterscheiden sich.", "3면"),
    ("「결과는 KBO 홈페이지에서 확인하세요」", "Das Ergebnis steht auf der KBO-Website.", "4면"),
    ("「수능까지 딱 일주일이 남아요」", "Genau noch eine Woche bis zur Suneung.", "5면"),
    ("「날짜와 기준과 결과를 나누면」", "Datum, Kriterium und Ergebnis trennen.", "6면"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 112
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 112 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "다음 주 · Nächste Woche (VOL.4)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "다음 주에는 수능 당일이에요. 11월 18일 예비소집과 11월 19일 수능 소식을 전해요. 한능검 시험 준비와 11월 22일 김치의 날 이야기도 있어요. 여러분의 편지와 8면 쓰기 우수작도 실어요. 기대해 주세요!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-mal.svg")
print("P7 saved, exercises so far:", len(REG))
