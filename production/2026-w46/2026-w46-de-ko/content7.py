# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE FOCUS =================
CURPAGE[0] = 7
p = BSPage4()
p.band("SPRACHE　언어", "Die Lucerna", "A2 → B2　Sätze der Woche & Fehlerklinik　이번 주의 문장과 오류 클리닉")

p.para(MX, 226, "Diese Seite gehört der Sprache: drei kleine Lektionen, die Sätze der Woche aus dieser Ausgabe, unsere Fehlerklinik — und Ihre Briefe.", 23, "serif", False, INK, RIGHT - MX, 1.4)
p.para(MX, 262, "이 페이지는 온통 언어입니다. 세 가지 짧은 수업, 이번 주의 문장들（이번 호 기사에서 한 글자도 빠짐없이 인용）, 오류 클리닉, 독자 편지.", 20, "sans", False, GREY, RIGHT - MX, 1.4)

CTOP, CBOT = 330, 1480
# --- col A2 ---
fa = Flow(p, [(COLX[0], CW)], CTOP, CBOT, tag="P7-A2")
fa.head("A2　UHRZEITEN & DATEN", 24)
fa.para("So sagen Sie Uhrzeiten und Daten: Um 11.11 Uhr beginnt der Karneval. Am 15. November ist Volkstrauertag. Mit werden sprechen Sie über das Passiv: Um 20.45 Uhr wird in Belgrad gespielt. Die NFL wird in München gespielt.")
fa.box("BEISPIELE　예문", [("„Um 11.11 Uhr beginnt der Karneval.“　„Am Sonntag wird in München Football gespielt.“", "serif", False, INK, 21, 1.4)])
fa.ex("A2", "문장 완성", "wird", "수동태: wird＋과거분사",
      "Am Freitag ___ in Belgrad gespielt.", instr="빈칸", size=20, gap=8)
fa.ex("A2", "문장 완성", "werden", "복수: werden",
      "Am 11. November ___ zwei Feste gefeiert.", instr="빈칸", size=20, gap=8)
fa.ex("A2", "문장 완성", "wird", "werden＋부정사로 미래",
      "Die Karnevalssession ___ um 11.11 Uhr beginnen.", instr="빈칸", size=20, gap=8)
fa.ex("A2", "객관식", "A", "수동태",
      "„Es wird gespielt“ ist... A. Passiv · B. Perfekt · C. Imperativ", size=20, gap=8)
fa.end_report()
# --- col B1 ---
fb = Flow(p, [(COLX[1], CW)], CTOP, CBOT, tag="P7-B1")
fb.head("B1　VERGLEICHE & GRÜNDE", 24)
fb.para("Vergleichen geht mit dem Komparativ: Die Nacht ist länger als der Tag. Gründe geben Sie mit weil: Ich bleibe zu Hause, weil es dunkel ist — das Verb steht am Ende des Satzes.")
fb.box("BEISPIELE　예문", [("„Die Nacht ist länger als der Tag.“　„Ich lese, weil das Buch spannend ist.“", "serif", False, INK, 21, 1.4)])
fb.ex("B1", "문장 완성", "länger", "lang → länger（밤은 낮보다 길다）",
      "Im November ist die Nacht ___ (lang) als der Tag.", instr="빈칸", size=20, gap=8)
fb.ex("B1", "문장 완성", "weil", "weil은 이유를 이끈다",
      "Es wird früher dunkel, ___ die Tage kürzer werden.", instr="빈칸", size=20, gap=8)
fb.ex("B1", "문장 전환", "Viele bleiben zu Hause, weil es dunkel ist.", "weil 절에서는 동사가 맨 끝으로",
      "Viele bleiben zu Hause. Es ist dunkel. (weil) → ___", instr="바꿔 쓰기", size=20, gap=8)
fb.ex("B1", "객관식", "A", "länger als＝～보다 길다",
      "„Länger als sonst“의 뜻은… A. 평소보다 길다 · B. 평소와 같다 · C. 평소보다 짧다", size=20, gap=8)
fb.end_report()
# --- col B2 ---
fc = Flow(p, [(COLX[2], CW)], CTOP, CBOT, tag="P7-B2")
fc.head("B2　MEINUNG SAGEN", 24)
fc.para("Eine Meinung sagen Sie höflich so: Meiner Meinung nach ... Oder: Ich finde, dass ... — bei dass steht das Verb am Ende! Nicht sicher? Dann: Es ist fraglich, ob ...")
fc.box("BEISPIELE　예문", [("„Meiner Meinung nach braucht das Gedenken Stille.“　„Niemand weiß, ob die Einigung gelingt.“", "serif", False, INK, 21, 1.4)])
fc.ex("B2", "문장 완성", "ob", "ob는 간접의문문을 이끈다",
      "Ich weiß nicht, ___ die Stromsteuer sinkt.", instr="빈칸", size=20, gap=8)
fc.ex("B2", "문장 완성", "fraglich", "Es ist fraglich, ob ...＝～인지 의심스럽다",
      "Es ist ___ , ob sich Union und SPD einigen.", instr="빈칸", size=20, gap=8)
fc.ex("B2", "문장 전환", "Ich finde, dass das Gedenken Stille braucht.", "dass 절에서는 동사가 맨 끝으로",
      "Ich finde: Das Gedenken braucht Stille. (dass) → ___", instr="바꿔 쓰기", size=20, gap=8)
fc.ex("B2", "객관식", "B", "정중하게 의견을 말하는 방법",
      "„Das Gedenken braucht Stille“ höflich sagen: A. „Stille, sofort!“ · B. „Meiner Meinung nach braucht das Gedenken Stille.“ · C. „Die Politik macht alles falsch.“", size=20, gap=8)
fc.end_report()

# --- col 3 rail: toolbox + readers + word (post-patch geometry: gap 6, pad 110) ---
ix = COLX[3]
tb = ["11.11 Uhr＝11시 11분",
      "vor leeren Rängen＝무관중",
      "Es wird gespielt.＝경기가 열린다",
      "Meiner Meinung nach＝제 생각에는",
      "Ich finde, dass＝～라고 생각한다",
      "Es ist fraglich, ob ...＝～인지 의심스럽다"]
tbh = 62 + sum(len(wrap(t, "serif", False, 20.5, CW - 44)) * 29.5 + 6 for t in tb) + 110
p.rect(ix, CTOP, CW, tbh, fill=BOX)
yy3 = CTOP + 16
p.text(ix + 22, yy3 + 26, "DER WERKZEUGKASTEN　도구 상자", 23, "sans", True, OLIVE)
yy3 += 52
for t in tb:
    yy3 = p.para(ix + 22, yy3 + 20.5, t, 20.5, "serif", False, INK, CW - 44, 1.42) + 6
ry = CTOP + tbh + 16
label = "편집부의 예시입니다!"
defer = "Bis Redaktionsschluss keine Briefe oder Texte — sie erscheinen in VOL.4."
reader = "„Liebe Lucerna, am Mittwoch bastle ich eine Laterne. Am Abend singe ich mit meiner Klasse. Viele Grüße — die Redaktion“"
invite = "Schreiben Sie uns Ihre Sätze und Ihre Texte von Seite 8! Die besten echten Briefe drucken wir in VOL.4."
chinese = "편집부의 예시이며 실제 편지가 아닙니다. 마감 시점까지 실제 편지는 도착하지 않았습니다. VOL.4로 보내 주세요!"
rh = 62 + 30 + len(wrap(label, "sans", True, 20, CW - 44)) * 29 \
    + len(wrap(defer, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(reader, "serif", False, 21, CW - 44)) * 30 + 8 \
    + len(wrap(invite, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(chinese, "sans", False, 19.5, CW - 44)) * 28 + 40 + 16
p.rect(ix, ry, CW, rh, fill="#f0eee5")
yy3 = ry + 16
p.text(ix + 22, yy3 + 26, "LESERBRIEFE　독자 편지", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 20, label, 20, "sans", True, OLIVE, CW - 44, 1.42)
yy3 = p.para(ix + 22, yy3 + 20.5, defer, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 21, reader, 21, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 20.5, invite, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
p.para(ix + 22, yy3 + 19.5, chinese, 19.5, "sans", False, GREY, CW - 44, 1.42)
wy3 = ry + rh + 16
p.rect(ix, wy3, CW, 150, fill=BOX)
p.text(ix + 22, wy3 + 40, "NOCH EIN WORT　한 마디 더", 22, "sans", True, OLIVE)
p.para(ix + 22, wy3 + 78, "«das Geisterspiel» (Seite 4) : ein Spiel ohne Zuschauer im Stadion. 무관중 경기: 관중 없는 경기.", 20.5, "serif", False, INK, CW - 44, 1.42)
print("P7 col3 ends", wy3 + 150)

# --- phrases of the week (verbatim from this issue) ---
py = 1520
p.hline(MX, RIGHT, py - 12, OLIVE, 2)
p.text(MX, py + 28, "SÄTZE DER WOCHE　이번 주의 문장", 28, "sans", True, OLIVE)
p.text(RIGHT, py + 28, "이번 호 기사에서 한 글자도 빠짐없이 인용　출처는 괄호 안", 20, "sans", False, GREY, anchor="end")
phrases = [
    ("Die Bundesliga pausiert — aber die Nationalmannschaft spielt.", "분데스리가는 쉬지만——대표팀은 경기를 한다.", "Seite 4 · B1"),
    ("Um 11.11 Uhr beginnt in Köln die neue Karnevalssession.", "11시 11분, 쾰른에서 새 카니발 시즌이 시작된다.", "Seite 2 · A2"),
    ("Sein Gedenktag ist der 11. November.", "그의 기념일은 11월 11일이다.", "Seite 3 · A2"),
    ("Die Rucksäcke sind gepackt, die Pausenhöfe sind wieder laut.", "가방은 챙겨졌고, 운동장은 다시 시끄럽다.", "Seite 5 · B1"),
    ("Der November ist dunkel, aber er ist nicht still: Er singt, leuchtet und feiert.", "11월은 어둡지만 조용하지 않다. 노래하고, 빛나고, 축제를 연다.", "Seite 2 · A2"),
    ("Das Spiel ist ausverkauft, RTL überträgt live.", "경기는 매진, RTL이 생중계한다.", "Seite 4 · B1"),
    ("Gedenken heißt hier: innehalten, erinnern — und für Frieden und Versöhnung einstehen.", "여기서 추모란 멈추고, 기억하고——평화와 화해를 위해 일어서는 것이다.", "Seite 6 · B2"),
    ("Am Sonntag ist es still im Land.", "일요일, 나라는 조용하다.", "Seite 6 · B2"),
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
p.text(RIGHT, ey + 28, "학습자가 가장 자주 하는 네 가지 실수　먼저 고치고 확인하세요", 20, "sans", False, GREY, anchor="end")
clinic = [
    ("Am Mittwoch die Kinder basteln Laternen.", "Am Mittwoch basteln die Kinder Laternen.", "동사는 두 번째: 주어가 처음이 아니어도 동사는 두 번째 자리를 지킨다."),
    ("Halb zwölf ist 12.30 Uhr.", "Halb zwölf ist 11.30 Uhr.", "halb zwölf＝11시 30분, zwölf의 30분 전."),
    ("Die Mannschaft ist nach Herzogenaurach gereist am Montag.", "Die Mannschaft ist am Montag nach Herzogenaurach gereist.", "Perfekt에서는 과거분사가 맨 끝으로 간다."),
    ("Er fragt, ob spielt Deutschland am Freitag?", "Er fragt, ob Deutschland am Freitag spielt.", "ob 절에서는 동사가 맨 끝으로 간다."),
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
p.text(MX + 26, ty + 46, "IN DER NÄCHSTEN AUSGABE　다음 호（VOL.4）", 24, "sans", True, ONCLOTH)
p.para(MX + 26, ty + 82, "Freitag, 20. November: Die Bundesliga kehrt zurück — Bayern gegen Köln. Dazu die Europapokal-Spieltage (24.–26. November), Buß- und Bettag, Totensonntag — und die Ergebnisse vom 3. bis 8. November. Und Ihre Briefe: Die besten echten Briefe erscheinen in VOL.4!", 21, "serif", False, "#cac8ba", RIGHT - MX - 52, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-sprache.svg")
print("P7 saved, exercises so far:", len(REG))
