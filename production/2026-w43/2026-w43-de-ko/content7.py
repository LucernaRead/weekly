# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE FOCUS =================
CURPAGE[0] = 7
p = BSPage4()
p.band("SPRACHE　언어", "Die Lucerna", "A2 → B2　Sätze der Woche & Fehlerklinik　이번 주 문장과 오류 클리닉")

p.para(MX, 226, "Diese Seite gehört der Sprache: drei kleine Lektionen, die Sätze der Woche aus dieser Ausgabe, unsere Fehlerklinik — und Ihre Briefe.", 23, "serif", False, INK, RIGHT - MX, 1.4)
p.para(MX, 262, "이 면은 언어 전용이에요: 작은 수업 세 개, 이번 호 문장 (모두 이번 호 기사에서 그대로), 오류 클리닉과 독자 편지예요.", 20, "sans", False, GREY, RIGHT - MX, 1.4)

CTOP, CBOT = 330, 1480
# --- col A2 ---
fa = Flow(p, [(COLX[0], CW)], CTOP, CBOT, tag="P7-A2")
fa.head("A2　DIE UHRZEIT & «WERDEN»", 24)
fa.para("So sagen Sie die Zeit: Es ist halb drei (2.30 Uhr), Viertel vor acht (7.45 Uhr). Mit werden sprechen Sie über die Zukunft: Morgen wird es kalt. Am Sonntag wird die Uhr umgestellt.")
fa.box("BEISPIELE　예문", [("„Es ist Viertel vor acht.“　„Morgen wird es sonnig.“", "serif", False, INK, 21, 1.4)])
fa.ex("A2", "문장 완성", "vor", "7:45 = 8시 15분 전",
      "Es ist Viertel ___ acht. (7.45 Uhr)", instr="빈칸", size=20, gap=8)
fa.ex("A2", "문장 완성", "wird", "wird + Partizip II (수동태)",
      "Am Sonntag ___ die Uhr zurückgestellt. (werden)", instr="빈칸", size=20, gap=8)
fa.ex("A2", "문장 완성", "wird", "werden + 원형 = 미래",
      "Morgen ___ es in Berlin regnen. (werden)", instr="빈칸", size=20, gap=8)
fa.ex("A2", "객관식", "A", "halb vier = 3:30",
      "„Halb vier“ ist... A. 3.30 Uhr · B. 4.30 Uhr · C. 16.00 Uhr", size=20, gap=8)
fa.end_report()
# --- col B1 ---
fb = Flow(p, [(COLX[1], CW)], CTOP, CBOT, tag="P7-B1")
fb.head("B1　VERGLEICHE & GRÜNDE", 24)
fb.para("Vergleichen geht mit dem Komparativ: Die Nacht ist länger als sonst. Gründe geben Sie mit weil: Ich bleibe zu Hause, weil es regnet — das Verb steht am Ende des Satzes.")
fb.box("BEISPIELE　예문", [("„Der Zug ist schneller als das Auto.“　„Ich lese, weil das Buch spannend ist.“", "serif", False, INK, 21, 1.4)])
fb.ex("B1", "문장 완성", "länger", "lang → länger (25시간의 밤)",
      "Die Nacht zum Sonntag ist ___ (lang) als andere Nächte.", instr="빈칸", size=20, gap=8)
fb.ex("B1", "문장 완성", "weil", "weil은 이유를 이끌어요",
      "Es wird früher dunkel, ___ die Tage kürzer werden.", instr="빈칸", size=20, gap=8)
fb.ex("B1", "문장 전환", "Viele reisen, weil Herbstferien sind.", "weil 문장은 동사가 끝에",
      "Viele reisen. Es sind Herbstferien. (weil) → ___", instr="바꿔 쓰기", size=20, gap=8)
fb.ex("B1", "객관식", "A", "비교급 kürzer",
      "Die Tage werden im Herbst... A. kürzer · B. kurz · C. der kürzeste", size=20, gap=8)
fb.end_report()
# --- col B2 ---
fc = Flow(p, [(COLX[2], CW)], CTOP, CBOT, tag="P7-B2")
fc.head("B2　MEINUNG SAGEN", 24)
fc.para("Eine Meinung sagen Sie höflich so: Meiner Meinung nach ... Oder: Ich finde, dass ... — bei dass steht das Verb am Ende! Nicht sicher? Dann: Es ist fraglich, ob ...")
fc.box("BEISPIELE　예문", [("„Meiner Meinung nach bleibt die Umstellung.“　„Niemand weiß, ob sie nächstes Jahr noch gilt.“", "serif", False, INK, 21, 1.4)])
fc.ex("B2", "문장 완성", "ob", "ob가 이끄는 간접 의문",
      "Ich weiß nicht, ___ die Umstellung bleibt.", instr="빈칸", size=20, gap=8)
fc.ex("B2", "문장 완성", "fraglich", "Es ist fraglich, ob ... = 확실하지 않아요",
      "Es ist ___ , ob die Mitgliedstaaten sich einigen.", instr="빈칸", size=20, gap=8)
fc.ex("B2", "문장 전환", "Ich finde, dass die Sommerzeit gut ist.", "dass 문장은 동사가 끝에",
      "Ich finde: Die Sommerzeit ist gut. (dass) → ___", instr="바꿔 쓰기", size=20, gap=8)
fc.ex("B2", "객관식", "B", "Meiner Meinung nach = 정중한 의견 표현",
      "Höflich eine Meinung sagen: A. „Das ist Quatsch!“ · B. „Meiner Meinung nach ist das zu kompliziert.“ · C. „Du liegst falsch.“", size=20, gap=8)
fc.end_report()

# --- col 3 rail: toolbox + readers + word ---
ix = COLX[3]
tb = ["Es ist halb drei. = 2.30 Uhr (3.30이 아니에요)",
      "eine Stunde länger schlafen = 한 시간 더 자기",
      "Von O bis O = 10월부터 부활절까지 (타이어 교체 암기 문장)",
      "Meiner Meinung nach ... = 제 생각에는……",
      "Ich finde, dass ... = 저는 ……라고 생각해요 (동사는 끝에)",
      "Es ist fraglich, ob ... = ……인지 의문"]
tbh = 62 + sum(len(wrap(t, "serif", False, 20.5, CW - 44)) * 29.5 + 6 for t in tb) + 110
p.rect(ix, CTOP, CW, tbh, fill=BOX)
yy3 = CTOP + 16
p.text(ix + 22, yy3 + 26, "DER WERKZEUGKASTEN　도구 상자", 21, "sans", True, OLIVE)  # D5 fix run2
yy3 += 52
for t in tb:
    yy3 = p.para(ix + 22, yy3 + 20.5, t, 20.5, "serif", False, INK, CW - 44, 1.42) + 6
ry = CTOP + tbh + 16
reader = "„Liebe Lucerna, ich stelle meine Uhren schon am Samstagabend um. Dann ist der Sonntag ganz ruhig. Viele Grüße — ein Leser“"
rh = 62 + 30 + len(wrap("Ein Beispiel der Redaktion — VOL.2 druckt Ihre Briefe!", "sans", True, 20, CW - 44)) * 29 \
    + len(wrap(reader, "serif", False, 21, CW - 44)) * 30 + 8 \
    + len(wrap("Schreiben Sie uns Ihre Sätze von Seite 2, 3 und 5 — und Ihre Texte zur Schreibaufgabe auf Seite 8!", "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap("편집부의 예시예요. 다음 호 (VOL.2)에 실제 독자 편지와 8면 쓰기 작품을 실어요.", "sans", False, 19.5, CW - 44)) * 28 + 40
p.rect(ix, ry, CW, rh, fill="#f0eee5")
yy3 = ry + 16
p.text(ix + 22, yy3 + 26, "LESERBRIEFE　독자 편지", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 20, "Ein Beispiel der Redaktion — VOL.2 druckt Ihre Briefe!", 20, "sans", True, OLIVE, CW - 44, 1.42)
yy3 = p.para(ix + 22, yy3 + 21, reader, 21, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 20.5, "Schreiben Sie uns Ihre Sätze von Seite 2, 3 und 5 — und Ihre Texte zur Schreibaufgabe auf Seite 8!", 20.5, "serif", False, INK, CW - 44, 1.42) + 8
p.para(ix + 22, yy3 + 19.5, "편집부의 예시예요. 다음 호 (VOL.2)에 실제 독자 편지와 8면 쓰기 작품을 실어요.", 19.5, "sans", False, GREY, CW - 44, 1.42)
wy3 = ry + rh + 16
p.rect(ix, wy3, CW, 150, fill=BOX)
p.text(ix + 22, wy3 + 40, "NOCH EIN WORT　단어 하나 더", 21, "sans", True, OLIVE)  # D5 fix run2
p.para(ix + 22, wy3 + 78, "«der Klassiker» (Seite 4): das größte Spiel der Saison — Bayern gegen Dortmund. 국가 더비예요.", 20.5, "serif", False, INK, CW - 44, 1.42)
print("P7 col3 ends", wy3 + 150)

# --- phrases of the week (verbatim from this issue) ---
py = 1520
p.hline(MX, RIGHT, py - 12, OLIVE, 2)
p.text(MX, py + 28, "SÄTZE DER WOCHE　이번 주 문장", 28, "sans", True, OLIVE)
p.text(RIGHT, py + 28, "이번 호 기사에서 그대로　괄호 안은 출처", 20, "sans", False, GREY, anchor="end")
phrases = [
    ("Die Nacht hat dann 25 Stunden, und alle dürfen eine Stunde länger schlafen.", "그 밤은 25시간이고, 모두가 한 시간 더 잘 수 있어요.", "Seite 1 · A2"),
    ("Im Frühjahr stellt man die Gartenmöbel VOR das Haus — im Herbst stellt man sie ZURÜCK ins Haus.", "봄에는 정원 가구를 집 앞으로, 가을에는 집 안으로 되돌려요. (암기 문장)", "Seite 2 · A2"),
    ("Wer vom 26. bis 29. Oktober einen geschnitzten Kürbis abgibt, bekommt für den 31. Oktober ein Freiticket für ein Kind.", "10월 26–29일에 조각한 호박을 내면 10월 31일 어린이 무료표를 받아요.", "Seite 3 · B1"),
    ("Borussia Dortmund gewann am Dienstagabend 2:1 bei Sabah FK in Baku.", "도르트문트가 화요일 밤 바쿠에서 사바흐를 2:1로 이겼어요.", "Seite 4 · B1"),
    ("Man wählt ein Buch, ohne es zu kennen.", "책을 고르는데, 아직 그 책을 몰라요. (도서관 블라인드 데이트)", "Seite 5 · B1"),
    ("84 Prozent von ihnen wollten die Umstellung abschaffen.", "그들 중 84%가 시간 조정을 폐지하길 원했어요.", "Seite 6 · B2"),
    ("Die Stunde von 2.00 bis 3.00 Uhr gibt es in dieser Nacht zweimal.", "이 밤에는 2시부터 3시까지의 한 시간이 두 번 있어요.", "Seite 2 · A2"),
    ("Aber die Regierungen der Mitgliedstaaten wurden sich nicht einig — und so blieb alles, wie es ist.", "하지만 회원국 정부들은 합의하지 못했고, 모든 것이 그대로 남았어요.", "Seite 6 · B2"),
]
for i, (q, zh, tag) in enumerate(phrases):
    cx = COLX[i % 4]; cyy = py + 56 + (i // 4) * 204
    quote = "„" + q + "“"
    qlines = len(wrap(quote, "serif", True, 20.5, CW))
    p.para(cx, cyy + 21, quote, 20.5, "serif", True, INK, CW, 1.38)
    t_y = cyy + 21 + (qlines - 1) * 28.3 + 36
    tlines = len(wrap(zh, "sans", False, 19, CW))
    p.para(cx, t_y, zh, 19, "sans", False, GREY, CW, 1.35)
    p.text(cx, t_y + (tlines - 1) * 25.6 + 30, tag, 18, "sans", True, OLIVE)

# --- error clinic ---
ey = 1980
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "FEHLERKLINIK　오류 클리닉", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "학습자가 가장 자주 하는 실수 네 가지　먼저 고치고 답을 보세요", 20, "sans", False, GREY, anchor="end")
clinic = [
    ("Ich habe 25 Jahre alt.", "Ich bin 25 Jahre alt.", "나이는 haben이 아니라 sein을 써요!"),
    ("Halb drei ist 3.30 Uhr.", "Halb drei ist 2.30 Uhr.", "halb drei = 2시 반 (drei 앞이에요)."),
    ("Berlin ist größer wie Hamburg.", "Berlin ist größer als Hamburg.", "비교급 뒤에는 wie가 아니라 als를 써요."),
    ("Ich bleibe zu Hause, weil ich lese ein Buch.", "Ich bleibe zu Hause, weil ich ein Buch lese.", "weil 문장에서 동사는 문장 끝에 와요."),
]
for i, (wrong, right, note) in enumerate(clinic):
    cx = COLX[i]
    p.text(cx, ey + 84, "FALSCH", 19, "sans", True, OLIVE)
    yy = p.para(cx, ey + 112, wrong, 20.5, "serif", False, INK, CW, 1.38)
    p.text(cx, yy + 28, "RICHTIG", 19, "sans", True, OLIVE)
    yy = p.para(cx, yy + 56, right, 20.5, "serif", True, INK, CW, 1.38)
    p.para(cx, yy + 26, note, 19, "sans", False, GREY, CW, 1.35)

# --- next issue teaser ---
ty = 2400
p.rect(MX, ty, RIGHT - MX, 130, fill=CLOTH)
p.text(MX + 26, ty + 46, "IN DER NÄCHSTEN AUSGABE　다음 호 예고 (VOL.2)", 24, "sans", True, ONCLOTH)
p.para(MX + 26, ty + 82, "Samstag, 31. Oktober: Halloween UND Reformationstag UND der Klassiker in Dortmund · Sonntag, 1. November: Allerheiligen · Baden-Württemberg startet in die Herbstferien · dazu Ihre Leserbriefe und die besten Texte von Seite 8!", 21, "serif", False, "#cac8ba", RIGHT - MX - 52, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-sprache.svg")
print("P7 saved, exercises so far:", len(REG))
