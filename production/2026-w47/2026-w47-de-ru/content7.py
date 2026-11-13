# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE FOCUS =================
CURPAGE[0] = 7
p = BSPage4()
p.band("SPRACHE　Язык", "Die Lucerna", "A2 → B2　Sätze der Woche & Fehlerklinik　Предложения недели и клиника ошибок")

p.para(MX, 226, "Diese Seite gehört der Sprache: drei kleine Lektionen, die Sätze der Woche aus dieser Ausgabe, unsere Fehlerklinik — und Ihre Briefe.", 23, "serif", False, INK, RIGHT - MX, 1.4)
p.para(MX, 262, "Эта страница — о языке: три коротких урока, предложения недели (точно из этого номера), клиника ошибок — и ваши письма.", 20, "sans", False, GREY, RIGHT - MX, 1.4)

CTOP, CBOT = 330, 1480
# --- col A2 ---
fa = Flow(p, [(COLX[0], CW)], CTOP, CBOT, tag="P7-A2")
fa.head("A2　DATEN SAGEN", 24)
fa.para("So sagen Sie Daten: Am 18. November ist Buß- und Bettag. Am 29. November ist der erste Advent. Mit werden sprechen Sie über das Passiv: Um 20.30 Uhr wird in München gespielt.")
fa.box("BEISPIELE　Примеры", [("„Am 18. November ist Buß- und Bettag.“　„Um 20.30 Uhr wird in München gespielt.“", "serif", False, INK, 21, 1.4)])
fa.ex("A2", "дополнение", "wird", "пассив: wird + Partizip II",
      "Am Freitag ___ in München gespielt.", instr="Вставьте", size=22, gap=8)
fa.ex("A2", "дополнение", "werden", "Мн. число: werden",
      "Die Weihnachtsmärkte ___ am Montag geöffnet.", instr="Вставьте", size=22, gap=8)
fa.ex("A2", "дополнение", "wird", "werden + инфинитив: будущее время",
      "Der Adventskalender ___ am 1. Dezember beginnen.", instr="Вставьте", size=22, gap=8)
fa.ex("A2", "выбор ответа", "A", "пассив",
      "„Es wird gespielt“ ist... A. Passiv · B. Perfekt · C. Imperativ", size=22, gap=8)
fa.end_report()
# --- P7 image: reading room, below the A2 column (col 0 free space) ---
iy7 = fa.y + 16
image(p, "lesesaal.jpg", COLX[0], iy7, CW, 145)  # W47 D1: was 150; A2 flow grew with 16.5pt stems, keep caption clear of the 1548 rule
cy7 = caption(p, COLX[0], iy7 + 150, CW,
              "Der große Lesesaal der Library of Congress in Washington.",
              "Foto: Carol M. Highsmith — public domain")
print("P7 image ends", cy7, "(A2 flow ended", fa.y, ")")
# --- col B1 ---
fb = Flow(p, [(COLX[1], CW)], CTOP, CBOT, tag="P7-B1")
fb.head("B1　VERGLEICHE & GRÜNDE", 24)
fb.para("Vergleichen geht mit dem Komparativ: Der November ist stiller als der Oktober. Gründe geben Sie mit weil: Ich bleibe zu Hause, weil es dunkel ist — das Verb steht am Ende des Satzes.")
fb.box("BEISPIELE　Примеры", [("„Der November ist stiller als der Oktober.“　„Ich lese, weil das Buch spannend ist.“", "serif", False, INK, 21, 1.4)])
fb.ex("B1", "дополнение", "stiller", "still → stiller (тише, чем в октябре)",
      "Im November ist es ___ (still) als im Oktober.", instr="Вставьте", size=22, gap=8)
fb.ex("B1", "дополнение", "weil", "weil: причина",
      "Es wird früher dunkel, ___ die Tage kürzer werden.", instr="Вставьте", size=22, gap=8)
fb.ex("B1", "преобразование", "Viele bleiben zu Hause, weil es dunkel ist.", "weil: глагол в конце",
      "Viele bleiben zu Hause. Es ist dunkel. (weil) → ___", instr="Перепишите", size=22, gap=8)
fb.ex("B1", "выбор ответа", "A", "stiller als = тише, чем …",
      "„Stiller als sonst“ heißt... A. тише обычного · B. как обычно · C. шумнее обычного", size=22, gap=8)
fb.end_report()
# --- col B2 ---
fc = Flow(p, [(COLX[2], CW)], CTOP, CBOT, tag="P7-B2")
fc.head("B2　MEINUNG SAGEN", 24)
fc.para("Eine Meinung sagen Sie höflich so: Meiner Meinung nach ... Oder: Ich finde, dass ... — bei dass steht das Verb am Ende! Nicht sicher? Dann: Es ist fraglich, ob ...")
fc.box("BEISPIELE　Примеры", [("„Meiner Meinung nach braucht das Gedenken Stille.“　„Niemand weiß, ob die Einigung gelingt.“", "serif", False, INK, 21, 1.4)])
fc.ex("B2", "дополнение", "ob", "ob: косвенный вопрос",
      "Ich weiß nicht, ___ die Stromsteuer sinkt.", instr="Вставьте", size=22, gap=8)
fc.ex("B2", "дополнение", "fraglich", "fraglich: ещё сомнительно",
      "Es ist ___ , ob sich Union und SPD einigen.", instr="Вставьте", size=22, gap=8)
fc.ex("B2", "преобразование", "Ich finde, dass das Gedenken Stille braucht.", "dass: глагол в конце",
      "Ich finde: Das Gedenken braucht Stille. (dass) → ___", instr="Перепишите", size=22, gap=8)
fc.ex("B2", "выбор ответа", "B", "вежливо высказать мнение",
      "„Das Gedenken braucht Stille“ höflich sagen: A. „Stille, sofort!“ · B. „Meiner Meinung nach braucht das Gedenken Stille.“ · C. „Die Politik macht alles falsch.“", size=22, gap=8)
fc.end_report()

# --- col 3 rail: toolbox + readers + word (post-patch geometry: gap 6, pad 110) ---
ix = COLX[3]
tb = ["18. November = 18 ноября",
      "der Buß- und Bettag = день покаяния и молитвы",
      "vor fast leeren Rängen = перед почти пустыми трибунами",
      "Es wird gespielt. = Матч состоится (пассив)",
      "Meiner Meinung nach = По-моему",
      "Es ist fraglich, ob ... = ещё сомнительно"]
tbh = 62 + sum(len(wrap(t, "serif", False, 20.5, CW - 44)) * 29.5 + 6 for t in tb) + 110  # fix1 D1: pad 90 -> 110 (= core-de value) + rail raised (RTOP, see below). Formula misses the +20.5/entry p.para offset (6 entries = +123), only partly offset by the 29.5 vs 29.11 line-height gap: clearance = pad - 90.0 for ru (10 lines), so 90 gave +0.0 (last baseline 813.0 exactly on the box bottom 813.0, 'fraglich' descender ~4.7 below the box). 110 gives clearance +20.0, same class as core +18.8. Occlusion audit cannot see this defect class (text drawn after its own box, nothing covers it) -- the old "validated by occlusion 0 flags" claim was false. Edition-local fix only; shared helper untouched.
RTOP = CTOP - 20  # fix1 D1: col-3 rail raised 20 so the +20 pad leaves the rail bottom exactly where it was (toolbox bottom 813.0, LESERBRIEFE y 829, NOCH EIN WORT ends 1547.5, still 0.5px before the 1548 Satze rule -- a flat +20 pad alone would push it to 1567.5, past the rule). Above-box slack is ~63px (P7 intro ends at baseline 262, toolbox top was 330), 20 used, ~43 left; the box top now sits 20px above the A2/B1/B2 heads (330) -- no overlap, nothing is drawn in col 3 between y 267 and 330.
p.rect(ix, RTOP, CW, tbh, fill=BOX)
yy3 = RTOP + 16
p.text(ix + 22, yy3 + 26, "WERKZEUGKASTEN　Справка", 23, "sans", True, OLIVE)  # fix-de-ru2 D4: was "DER WERKZEUGKASTEN　Справка"; ink ran +33.0px past the box; dropping "DER" leaves +24.5px margin
yy3 += 52
for t in tb:
    yy3 = p.para(ix + 22, yy3 + 20.5, t, 20.5, "serif", False, INK, CW - 44, 1.42) + 6
ry = RTOP + tbh + 16
label = "Ein Beispiel der Redaktion!"
defer = "Bis Redaktionsschluss keine Briefe oder Texte — sie erscheinen in VOL.5."
reader = "„Liebe Lucerna, im November bastle ich einen Adventskalender. Am 1. Dezember öffne ich das erste Türchen. Viele Grüße — die Redaktion“"
invite = "Schreiben Sie uns Ihre Sätze und Ihre Texte von Seite 8! Die besten echten Briefe drucken wir in VOL.5."
chinese = "Пример редакции: к сдаче номера настоящих писем не пришло. Присылайте ваши тексты для VOL.5!"
rh = 62 + 30 + len(wrap(label, "sans", True, 20, CW - 44)) * 29 \
    + len(wrap(defer, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(reader, "serif", False, 21, CW - 44)) * 30 + 8 \
    + len(wrap(invite, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(chinese, "sans", False, 19.5, CW - 44)) * 28 + 40 + 16
p.rect(ix, ry, CW, rh, fill="#f0eee5")
yy3 = ry + 16
p.text(ix + 22, yy3 + 26, "LESERBRIEFE　Письма читателей", 21, "sans", True, OLIVE)  # fix-de-ru2 D5: fs 23 -> 21 (nl 25->23 precedent); ink ran +22.6px past the box, now +13.9px margin; wording kept
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 20, label, 20, "sans", True, OLIVE, CW - 44, 1.42)
yy3 = p.para(ix + 22, yy3 + 20.5, defer, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 21, reader, 21, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 20.5, invite, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
p.para(ix + 22, yy3 + 19.5, chinese, 19.5, "sans", False, GREY, CW - 44, 1.42)
wy3 = ry + rh + 16
p.rect(ix, wy3, CW, 150, fill=BOX)
p.text(ix + 22, wy3 + 40, "NOCH EIN WORT　Ещё слово", 22, "sans", True, OLIVE)  # fix-de-ru2 D6: was "Ещё одно слово"; ink ran +1.3px past the box; dropping "одно" leaves +60.7px margin
p.para(ix + 22, wy3 + 78, "«der Adventskalender» (стр. 5): календарь с 24 окошками.", 20.5, "serif", False, INK, CW - 44, 1.42)
print("P7 col3 ends", wy3 + 150)

# --- phrases of the week (verbatim from this issue) ---
py = 1560
p.hline(MX, RIGHT, py - 12, OLIVE, 2)
p.text(MX, py + 28, "SÄTZE DER WOCHE　Предложения недели", 28, "sans", True, OLIVE)
p.text(RIGHT, py + 28, "Точно из этого номера　Источник в скобках", 20, "sans", False, GREY, anchor="end")
phrases = [
    ("Nach zwei Wochen Pause spielt am Freitagabend der FC Bayern gegen den 1. FC Köln.", "После двухнедельного перерыва «Бавария» играет с «Кёльном» в пятницу вечером.", "Seite 1 · A2"),
    ("Es geht ums Viertelfinale der Nations League.", "Речь о четвертьфинале Лиги наций.", "Seite 1 · A2"),
    ("Nur in Sachsen ist der Buß- und Bettag ein gesetzlicher Feiertag.", "Только в Саксонии Buß- und Bettag — выходной.", "Seite 2 · A2"),
    ("Die Märkte beginnen fast zwei Wochen früher.", "Рынки открываются почти на две недели раньше.", "Seite 3 · A2"),
    ("Hinter jedem Türchen wartet eine kleine Überraschung.", "За каждым окошком — маленький сюрприз.", "Seite 5 · B1"),
    ("Der FC Bayern gewann in Mainz mit 2:1.", "«Бавария» победила в Майнце 2:1.", "Seite 4 · B1"),
    ("Die stille Woche ist der Übergang: vom November in den Advent.", "Тихая неделя — переход: от ноября к Адвенту.", "Seite 6 · B2"),
    ("Am Sonntag ist es still im Land.", "В воскресенье вся страна тиха.", "Seite 6 · B2"),
]
for i, (q, zh, tag) in enumerate(phrases):
    cx = COLX[i % 4]; cyy = py + 56 + (i // 4) * 190
    quote = "„" + q + "“"
    qlines = len(wrap(quote, "serif", True, 20.5, CW))
    p.para(cx, cyy + 21, quote, 20.5, "serif", True, INK, CW, 1.38)
    t_y = cyy + 21 + (qlines - 1) * 28.3 + 36
    tlines = len(wrap(zh, "sans", False, 19, CW))
    p.para(cx, t_y, zh, 19, "sans", False, GREY, CW, 1.35)
    p.text(cx, t_y + (tlines - 1) * 25.6 + 30, tag, 18, "sans", True, OLIVE)

# --- error clinic ---
ey = 2020
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "FEHLERKLINIK　Клиника ошибок", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Четыре самые частые ошибки　Сначала исправьте, потом проверьте", 20, "sans", False, GREY, anchor="end")
clinic = [
    ("Am Mittwoch die Kinder basteln einen Adventskalender.", "Am Mittwoch basteln die Kinder einen Adventskalender.", "Глагол на 2-м месте: глагол остаётся вторым, даже если подлежащее не первое."),
    ("Halb neun ist 9.30 Uhr.", "Halb neun ist 8.30 Uhr.", "halb neun = половина девятого (до neun)."),
    ("Die Mannschaft ist nach Berlin gereist am Montag.", "Die Mannschaft ist am Montag nach Berlin gereist.", "В Perfekt причастие стоит в конце."),
    ("Er fragt, ob spielt die Nationalelf am Montag?", "Er fragt, ob die Nationalelf am Montag spielt.", "В придаточном с ob глагол стоит в конце."),
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
p.text(MX + 26, ty + 46, "IN DER NÄCHSTEN AUSGABE　В следующем номере (VOL.5)", 24, "sans", True, ONCLOTH)
p.para(MX + 26, ty + 82, "Sonntag, 29. November: Der erste Advent beginnt — Kerzen, Lieder und das erste Türchen. Dazu die Ergebnisse der Europapokale (24.–26. November), der 11. Spieltag und die Weihnachtsmärkte in vollem Gang. Und Ihre Briefe: Die besten echten Briefe erscheinen in VOL.5!", 21, "serif", False, "#cac8ba", RIGHT - MX - 52, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-sprache.svg")
print("P7 saved, exercises so far:", len(REG))
