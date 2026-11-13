# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE FOCUS =================
CURPAGE[0] = 7
p = BSPage4()
p.band("SPRACHE　Lengua", "Die Lucerna", "A2 → B2　Sätze der Woche & Fehlerklinik　Frases de la semana y clínica de errores")

p.para(MX, 226, "Diese Seite gehört der Sprache: drei kleine Lektionen, die Sätze der Woche aus dieser Ausgabe, unsere Fehlerklinik — und Ihre Briefe.", 23, "serif", False, INK, RIGHT - MX, 1.4)
p.para(MX, 262, "Esta página es de lengua: tres lecciones cortas, las frases de la semana (citadas tal cual en este número), la clínica de errores, y vuestras cartas.", 20, "sans", False, GREY, RIGHT - MX, 1.4)

CTOP, CBOT = 330, 1480
# --- col A2 ---
fa = Flow(p, [(COLX[0], CW)], CTOP, CBOT, tag="P7-A2")
fa.head("A2　DATEN SAGEN", 24)
fa.para("So sagen Sie Daten: Am 18. November ist Buß- und Bettag. Am 29. November ist der erste Advent. Mit werden sprechen Sie über das Passiv: Um 20.30 Uhr wird in München gespielt.")
fa.box("BEISPIELE　Ejemplos", [("„Am 18. November ist Buß- und Bettag.“　„Um 20.30 Uhr wird in München gespielt.“", "serif", False, INK, 21, 1.4)])
fa.ex("A2", "completar", "wird", "pasiva: wird + Part. II",
      "Am Freitag ___ in München gespielt.", instr="Completa", size=22, gap=8)
fa.ex("A2", "completar", "werden", "Plural: werden",
      "Die Weihnachtsmärkte ___ am Montag geöffnet.", instr="Completa", size=22, gap=8)
fa.ex("A2", "completar", "wird", "werden + infinitivo: futuro",
      "Der Adventskalender ___ am 1. Dezember beginnen.", instr="Completa", size=22, gap=8)
fa.ex("A2", "opción múltiple", "A", "pasiva",
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
fb.box("BEISPIELE　Ejemplos", [("„Der November ist stiller als der Oktober.“　„Ich lese, weil das Buch spannend ist.“", "serif", False, INK, 21, 1.4)])
fb.ex("B1", "completar", "stiller", "still → stiller (más tranquilo que octubre)",
      "Im November ist es ___ (still) als im Oktober.", instr="Completa", size=22, gap=8)
fb.ex("B1", "completar", "weil", "weil: la causa",
      "Es wird früher dunkel, ___ die Tage kürzer werden.", instr="Completa", size=22, gap=8)
fb.ex("B1", "transformación", "Viele bleiben zu Hause, weil es dunkel ist.", "weil: verbo al final",
      "Viele bleiben zu Hause. Es ist dunkel. (weil) → ___", instr="Reescribe", size=22, gap=8)
fb.ex("B1", "opción múltiple", "A", "stiller als = más tranquilo que …",
      "„Stiller als sonst“ heißt... A. más tranquilo que de costumbre · B. igual que de costumbre · C. más ruidoso que de costumbre", size=22, gap=8)
fb.end_report()
# --- col B2 ---
fc = Flow(p, [(COLX[2], CW)], CTOP, CBOT, tag="P7-B2")
fc.head("B2　MEINUNG SAGEN", 24)
fc.para("Eine Meinung sagen Sie höflich so: Meiner Meinung nach ... Oder: Ich finde, dass ... — bei dass steht das Verb am Ende! Nicht sicher? Dann: Es ist fraglich, ob ...")
fc.box("BEISPIELE　Ejemplos", [("„Meiner Meinung nach braucht das Gedenken Stille.“　„Niemand weiß, ob die Einigung gelingt.“", "serif", False, INK, 21, 1.4)])
fc.ex("B2", "completar", "ob", "ob: interrogativa indirecta",
      "Ich weiß nicht, ___ die Stromsteuer sinkt.", instr="Completa", size=22, gap=8)
fc.ex("B2", "completar", "fraglich", "fraglich: aún dudoso",
      "Es ist ___ , ob sich Union und SPD einigen.", instr="Completa", size=22, gap=8)
fc.ex("B2", "transformación", "Ich finde, dass das Gedenken Stille braucht.", "dass: verbo al final",
      "Ich finde: Das Gedenken braucht Stille. (dass) → ___", instr="Reescribe", size=22, gap=8)
fc.ex("B2", "opción múltiple", "B", "opinar con educación",
      "„Das Gedenken braucht Stille“ höflich sagen: A. „Stille, sofort!“ · B. „Meiner Meinung nach braucht das Gedenken Stille.“ · C. „Die Politik macht alles falsch.“", size=22, gap=8)
fc.end_report()

# --- col 3 rail: toolbox + readers + word (post-patch geometry: gap 6, pad 110) ---
ix = COLX[3]
tb = ["18. November = 18 de noviembre",
      "der Buß- und Bettag = día de arrepentimiento y oración",
      "vor fast leeren Rängen = en gradas casi vacías",
      "Es wird gespielt. = Se jugará el partido (pasiva)",
      "Meiner Meinung nach = En mi opinión",
      "Es ist fraglich, ob ... = aún dudoso"]
tbh = 62 + sum(len(wrap(t, "serif", False, 20.5, CW - 44)) * 29.5 + 6 for t in tb) + 110  # fix1 D1: pad 90 -> 110 (= core-de value). Formula misses the +20.5/entry p.para offset (6 entries = +123), only partly offset by the 29.5 vs 29.11 line-height gap: clearance = pad - 90.4 for es (9 lines), so 90 gave -0.4 (last baseline 783.9 vs box bottom 783.5, 'fraglich' descender ~4.7 below the box). 110 gives clearance +19.6 (bottom 803.5), same class as core +18.8. Boxes below shift +20 (LESERBRIEFE y 819.5, NOCH EIN WORT ends 1538.0, 10px before the 1548 Satze rule). Occlusion audit cannot see this defect class (text drawn after its own box, nothing covers it) -- the old "validated by occlusion 0 flags" claim was false. Edition-local fix only; shared helper untouched.
p.rect(ix, CTOP, CW, tbh, fill=BOX)
yy3 = CTOP + 16
p.text(ix + 22, yy3 + 26, "DER WERKZEUGKASTEN　Útiles", 23, "sans", True, OLIVE)
yy3 += 52
for t in tb:
    yy3 = p.para(ix + 22, yy3 + 20.5, t, 20.5, "serif", False, INK, CW - 44, 1.42) + 6
ry = CTOP + tbh + 16
label = "Ein Beispiel der Redaktion!"
defer = "Bis Redaktionsschluss keine Briefe oder Texte — sie erscheinen in VOL.5."
reader = "„Liebe Lucerna, im November bastle ich einen Adventskalender. Am 1. Dezember öffne ich das erste Türchen. Viele Grüße — die Redaktion“"
invite = "Schreiben Sie uns Ihre Sätze und Ihre Texte von Seite 8! Die besten echten Briefe drucken wir in VOL.5."
chinese = "Ejemplo de la redacción: no llegó ninguna carta real antes del cierre. ¡Envía tus textos para el VOL.5!"
rh = 62 + 30 + len(wrap(label, "sans", True, 20, CW - 44)) * 29 \
    + len(wrap(defer, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(reader, "serif", False, 21, CW - 44)) * 30 + 8 \
    + len(wrap(invite, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(chinese, "sans", False, 19.5, CW - 44)) * 28 + 40 + 16
p.rect(ix, ry, CW, rh, fill="#f0eee5")
yy3 = ry + 16
p.text(ix + 22, yy3 + 26, "LESERBRIEFE　Cartas", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 20, label, 20, "sans", True, OLIVE, CW - 44, 1.42)
yy3 = p.para(ix + 22, yy3 + 20.5, defer, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 21, reader, 21, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 20.5, invite, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
p.para(ix + 22, yy3 + 19.5, chinese, 19.5, "sans", False, GREY, CW - 44, 1.42)
wy3 = ry + rh + 16
p.rect(ix, wy3, CW, 150, fill=BOX)
p.text(ix + 22, wy3 + 40, "NOCH EIN WORT　Una palabra más", 22, "sans", True, OLIVE)
p.para(ix + 22, wy3 + 78, "«der Adventskalender» (p. 5): un calendario de 24 puertecitas.", 20.5, "serif", False, INK, CW - 44, 1.42)
print("P7 col3 ends", wy3 + 150)

# --- phrases of the week (verbatim from this issue) ---
py = 1560
p.hline(MX, RIGHT, py - 12, OLIVE, 2)
p.text(MX, py + 28, "SÄTZE DER WOCHE　Frases de la semana", 28, "sans", True, OLIVE)
p.text(RIGHT, py + 28, "Citadas tal cual en este número　Fuente entre paréntesis", 20, "sans", False, GREY, anchor="end")
phrases = [
    ("Nach zwei Wochen Pause spielt am Freitagabend der FC Bayern gegen den 1. FC Köln.", "Tras dos semanas de pausa, el Bayern juega el viernes por la noche contra el Colonia.", "Seite 1 · A2"),
    ("Es geht ums Viertelfinale der Nations League.", "Todo se decide en los cuartos de la Nations League.", "Seite 1 · A2"),
    ("Nur in Sachsen ist der Buß- und Bettag ein gesetzlicher Feiertag.", "Solo en Sajonia el Buß- und Bettag es festivo.", "Seite 2 · A2"),
    ("Die Märkte beginnen fast zwei Wochen früher.", "Los mercados empiezan casi dos semanas antes.", "Seite 3 · A2"),
    ("Hinter jedem Türchen wartet eine kleine Überraschung.", "Tras cada puertecita espera una sorpresita.", "Seite 5 · B1"),
    ("Der FC Bayern gewann in Mainz mit 2:1.", "El Bayern ganó 2–1 en Maguncia.", "Seite 4 · B1"),
    ("Die stille Woche ist der Übergang: vom November in den Advent.", "La semana tranquila es la transición: de noviembre al Adviento.", "Seite 6 · B2"),
    ("Am Sonntag ist es still im Land.", "El domingo, todo el país está tranquilo.", "Seite 6 · B2"),
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
p.text(MX, ey + 28, "FEHLERKLINIK　Clínica de errores", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Los cuatro errores más comunes　Corrige primero, luego comprueba", 20, "sans", False, GREY, anchor="end")
clinic = [
    ("Am Mittwoch die Kinder basteln einen Adventskalender.", "Am Mittwoch basteln die Kinder einen Adventskalender.", "Verbo en 2.ª posición: el verbo sigue segundo aunque el sujeto no vaya primero."),
    ("Halb neun ist 9.30 Uhr.", "Halb neun ist 8.30 Uhr.", "halb neun = las ocho y media (antes de neun)."),
    ("Die Mannschaft ist nach Berlin gereist am Montag.", "Die Mannschaft ist am Montag nach Berlin gereist.", "En Perfekt, el participio va al final."),
    ("Er fragt, ob spielt die Nationalelf am Montag?", "Er fragt, ob die Nationalelf am Montag spielt.", "En la subordinada con ob, el verbo va al final."),
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
p.text(MX + 26, ty + 46, "IN DER NÄCHSTEN AUSGABE　Próximo número (VOL.5)", 24, "sans", True, ONCLOTH)
p.para(MX + 26, ty + 82, "Sonntag, 29. November: Der erste Advent beginnt — Kerzen, Lieder und das erste Türchen. Dazu die Ergebnisse der Europapokale (24.–26. November), der 11. Spieltag und die Weihnachtsmärkte in vollem Gang. Und Ihre Briefe: Die besten echten Briefe erscheinen in VOL.5!", 21, "serif", False, "#cac8ba", RIGHT - MX - 52, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-sprache.svg")
print("P7 saved, exercises so far:", len(REG))
