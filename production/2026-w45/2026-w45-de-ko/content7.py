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
p.para(MX, 262, "이 면은 언어 전용이에요. 작은 수업 세 개, 이번 호 문장(모두 이번 호 기사 원문에서 그대로), 오류 클리닉과 독자 편지가 있어요.", 20, "sans", False, GREY, RIGHT - MX, 1.4)

CTOP, CBOT = 330, 1480
# --- col A2 ---
fa = Flow(p, [(COLX[0], CW)], CTOP, CBOT, tag="P7-A2")
fa.head("A2　DIE ZAHLEN & «WERDEN»", 24)
fa.para("So sagen Sie die Zahlen: 14,04 Cent pro Liter, rund 8,35 Euro für 50 Liter. Mit werden sprechen Sie über die Zukunft und das Passiv: Am Freitag wird gespielt. Der Tankrabatt wird bis Dezember gelten.")
fa.box("BEISPIELE　예문", [("„Am Freitag wird gespielt.“　„Der Tankrabatt gilt bis Dezember.“", "serif", False, INK, 21, 1.4)])
fa.ex("A2", "문장 완성", "wird", "수동태: wird + 과거분사",
      "Am Freitag ___ gespielt: Hamburg gegen Gladbach.", instr="빈칸", size=20, gap=8)
fa.ex("A2", "문장 완성", "werden", "복수형: werden",
      "Am Sonntag ___ drei Spiele gespielt.", instr="빈칸", size=20, gap=8)
fa.ex("A2", "문장 완성", "wird", "werden + 원형은 미래를 나타내요",
      "Der Tankrabatt ___ bis Dezember gelten.", instr="빈칸", size=20, gap=8)
fa.ex("A2", "객관식", "A", "수동태예요",
      "„Es wird gespielt“ ist... A. Passiv · B. Perfekt · C. Imperativ", size=20, gap=8)
fa.end_report()
# --- col B1 ---
fb = Flow(p, [(COLX[1], CW)], CTOP, CBOT, tag="P7-B1")
fb.head("B1　VERGLEICHE & GRÜNDE", 24)
fb.para("Vergleichen geht mit dem Komparativ: Der Abend ist länger als sonst. Gründe geben Sie mit weil: Ich bleibe zu Hause, weil es kalt ist — das Verb steht am Ende des Satzes.")
fb.box("BEISPIELE　예문", [("„Das Spiel ist später als sonst.“　„Ich lese, weil das Buch spannend ist.“", "serif", False, INK, 21, 1.4)])
fb.ex("B1", "문장 완성", "später", "spät → später(19:30이 가장 늦어요)",
      "Das Spiel Hoffenheim–Schalke ist ___ (spät) als die anderen Sonntagsspiele.", instr="빈칸", size=20, gap=8)
fb.ex("B1", "문장 완성", "weil", "weil 뒤에는 이유가 와요",
      "Es wird früher dunkel, ___ die Tage kürzer werden.", instr="빈칸", size=20, gap=8)
fb.ex("B1", "문장 전환", "Viele bleiben zu Hause, weil es kalt ist.", "weil 절에서는 동사가 끝에 와요",
      "Viele bleiben zu Hause. Es ist kalt. (weil) → ___", instr="바꿔 쓰기", size=20, gap=8)
fb.ex("B1", "객관식", "A", "länger als = ……보다 더 길다",
      "„Länger als sonst“ heißt... A. 평소보다 더 길다 · B. 평소와 같다 · C. 평소보다 더 짧다", size=20, gap=8)
fb.end_report()
# --- col B2 ---
fc = Flow(p, [(COLX[2], CW)], CTOP, CBOT, tag="P7-B2")
fc.head("B2　MEINUNG SAGEN", 24)
fc.para("Eine Meinung sagen Sie höflich so: Meiner Meinung nach ... Oder: Ich finde, dass ... — bei dass steht das Verb am Ende! Nicht sicher? Dann: Es ist fraglich, ob ...")
fc.box("BEISPIELE　예문", [("„Meiner Meinung nach braucht die Pflege mehr Geld.“　„Niemand weiß, ob die Steuer sinkt.“", "serif", False, INK, 21, 1.4)])
fc.ex("B2", "문장 완성", "ob", "ob는 간접 의문을 이끌어요",
      "Ich weiß nicht, ___ die Stromsteuer sinkt.", instr="빈칸", size=20, gap=8)
fc.ex("B2", "문장 완성", "fraglich", "Es ist fraglich, ob ... = ……인지 몰라요",
      "Es ist ___ , ob sich Union und SPD einigen.", instr="빈칸", size=20, gap=8)
fc.ex("B2", "문장 전환", "Ich finde, dass die Pflege mehr Hilfe braucht.", "dass 절에서는 동사가 끝에 와요",
      "Ich finde: Die Pflege braucht mehr Hilfe. (dass) → ___", instr="바꿔 쓰기", size=20, gap=8)
fc.ex("B2", "객관식", "B", "정중하게 의견을 말하기",
      "„Die Pflege braucht mehr Geld“ höflich sagen: A. „Mehr Geld, sofort!“ · B. „Meiner Meinung nach braucht die Pflege mehr Geld.“ · C. „Die Politik macht alles falsch.“", size=20, gap=8)
fc.end_report()

# --- col 3 rail: toolbox + readers + word (post-patch geometry: gap 6, pad 110) ---
ix = COLX[3]
tb = ["14,04 Cent = 리터당 14.04센트",
      "rund 8,35 Euro = 약 8.35유로를 아껴요",
      "Es wird gespielt. = 경기가 열려요(수동태)",
      "Meiner Meinung nach ... = 제 생각에는",
      "Ich finde, dass ... = ……라고 생각해요",
      "Es ist fraglich, ob ... = ……인지 몰라요"]
tbh = 62 + sum(len(wrap(t, "serif", False, 20.5, CW - 44)) * 29.5 + 6 for t in tb) + 110
p.rect(ix, CTOP, CW, tbh, fill=BOX)
yy3 = CTOP + 16
p.text(ix + 22, yy3 + 26, "DER WERKZEUGKASTEN　도구 상자", 23, "sans", True, OLIVE)
yy3 += 52
for t in tb:
    yy3 = p.para(ix + 22, yy3 + 20.5, t, 20.5, "serif", False, INK, CW - 44, 1.42) + 6
ry = CTOP + tbh + 16
label = "Ein Beispiel der Redaktion!"
defer = "Bis Redaktionsschluss keine Briefe oder Texte — sie erscheinen in VOL.3."
reader = "„Liebe Lucerna, am Dienstag schaue ich Bayern bei Atlético. Die Fußballwoche ist toll! Viele Grüße — die Redaktion“"
invite = "Schreiben Sie uns Ihre Sätze und Ihre Texte von Seite 8! Die besten echten Briefe drucken wir in VOL.3."
korean = "편집부 예시예요, 실제 편지가 아니에요. 아직 실제 편지나 쓰기 작품이 없어요. 여러분의 글을 보내 주세요! VOL.3에 실어 드릴게요."
rh = 62 + 30 + len(wrap(label, "sans", True, 20, CW - 44)) * 29 \
    + len(wrap(defer, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(reader, "serif", False, 21, CW - 44)) * 30 + 8 \
    + len(wrap(invite, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(korean, "sans", False, 19.5, CW - 44)) * 28 + 40 + 16
# NOTE (fix1): the +16 corrects the readers-box formula's per-paragraph
# transition undercount (each drawn para adds its size on top of the
# formula's +8 gap); without it the last Chinese line was painted over by
# the word box below (occlusion COVER flag on the first fix1 render).
p.rect(ix, ry, CW, rh, fill="#f0eee5")
yy3 = ry + 16
p.text(ix + 22, yy3 + 26, "LESERBRIEFE　독자 편지", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 20, label, 20, "sans", True, OLIVE, CW - 44, 1.42)
yy3 = p.para(ix + 22, yy3 + 20.5, defer, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 21, reader, 21, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 20.5, invite, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
p.para(ix + 22, yy3 + 19.5, korean, 19.5, "sans", False, GREY, CW - 44, 1.42)
wy3 = ry + rh + 16
p.rect(ix, wy3, CW, 150, fill=BOX)
p.text(ix + 22, wy3 + 40, "NOCH EIN WORT　단어 하나 더", 22, "sans", True, OLIVE)
p.para(ix + 22, wy3 + 78, "«der Tankrabatt» (Seite 2): die gesenkte Steuer auf Benzin und Diesel. 유가 할인이에요.", 20.5, "serif", False, INK, CW - 44, 1.42)
print("P7 col3 ends", wy3 + 150)

# --- phrases of the week (verbatim from this issue) ---
py = 1520
p.hline(MX, RIGHT, py - 12, OLIVE, 2)
p.text(MX, py + 28, "SÄTZE DER WOCHE　이번 주 문장", 28, "sans", True, OLIVE)
p.text(RIGHT, py + 28, "기사 원문에서 그대로 인용했어요　괄호 안은 출처예요", 20, "sans", False, GREY, anchor="end")
phrases = [
    ("Vier Nächte Fußball hintereinander, dann ein ganzes Wochenende Liga.", "연속 네 밤의 축구, 그리고 주말 내내 리그예요.", "Seite 4 · B1"),
    ("Die Energiesteuer auf Benzin und Diesel sinkt um 14,04 Cent pro Liter.", "휘발유와 디젤의 에너지세가 리터당 14.04센트 내려가요.", "Seite 2 · A2"),
    ("Wer 50 Liter tankt, spart rund 8,35 Euro.", "50리터를 넣으면 약 8.35유로를 아껴요.", "Seite 2 · A2"),
    ("Die Schule hat nach den Herbstferien wieder begonnen.", "가을 방학 뒤에 학교가 다시 개학했어요.", "Seite 5 · B1"),
    ("Die Tage sind kurz, die Abende lang.", "낮은 짧고 밤은 길어요.", "Seite 3 · A2"),
    ("Zwei schwere Auswärtsspiele für die deutschen Teams.", "독일 팀들의 어려운 원정 경기 두 경기예요.", "Seite 4 · B1"),
    ("Die deutsche Wirtschaft kommt langsam aus der Stagnation heraus, doch der Aufschwung trägt sich nicht selbst.", "독일 경제는 침체에서 천천히 벗어나고 있지만, 회복이 아직 스스로 이어지지 않아요.", "Seite 6 · B2"),
    ("Es geht langsam aufwärts — aber von allein geht es nicht.", "천천히 나아지고 있어요. 하지만 저절로 좋아지지는 않아요.", "Seite 6 · B2"),
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
p.text(RIGHT, ey + 28, "자주 틀리는 네 가지 오류　먼저 고쳐 보고 정답 확인", 20, "sans", False, GREY, anchor="end")
clinic = [
    ("Die Schule beginnt wieder in Baden-Württemberg am Montag.", "In Baden-Württemberg beginnt die Schule am Montag wieder.", "동사 두 번째 자리: 주어가 문장 앞에 없어도 동사는 두 번째 자리에 와요."),
    ("Halb acht ist 8.30 Uhr.", "Halb acht ist 7.30 Uhr.", "halb acht = 7시 30분(8시 전)이에요."),
    ("Die Preise sind gefallen um 14 Cent.", "Die Preise sind um 14 Cent gefallen.", "Perfekt에서는 과거분사가 문장 끝에 와요."),
    ("Er fragt, ob kommt der Bus?", "Er fragt, ob der Bus kommt.", "ob 절에서는 동사가 문장 끝에 와요."),
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
p.text(MX + 26, ty + 46, "IN DER NÄCHSTEN AUSGABE　다음 호 예고 (VOL.3)", 24, "sans", True, ONCLOTH)
p.para(MX + 26, ty + 82, "Sonntag, 15. November: Volkstrauertag und NFL in München — American Football in der Allianz Arena · dazu St. Martin am 11. November, die Europapokal-Rückspiele und Ihre Briefe: Schreiben Sie uns! Die besten echten Briefe erscheinen in VOL.3!", 21, "serif", False, "#cac8ba", RIGHT - MX - 52, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-sprache.svg")
print("P7 saved, exercises so far:", len(REG))
