# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/de-es-proof/baseline-out/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE FOCUS =================
CURPAGE[0] = 7
p = BSPage4()
p.band("SPRACHE · Lengua", "Die Lucerna", "A2 → B2 · Sätze der Woche & Fehlerklinik · Frases de la semana y clínica de errores")

p.para(MX, 226, "Diese Seite gehört der Sprache: drei kleine Lektionen, die Sätze der Woche aus dieser Ausgabe, unsere Fehlerklinik — und Ihre Briefe.", 23, "serif", False, INK, RIGHT - MX, 1.4)
p.para(MX, 262, "Esta página es para la lengua: tres minilecciones, las frases de la semana (todas de los artículos de este número), la clínica de errores y las cartas de los lectores.", 20, "sans", False, GREY, RIGHT - MX, 1.4)

CTOP, CBOT = 330, 1480
# --- col A2 ---
fa = Flow(p, [(COLX[0], CW)], CTOP, CBOT, tag="P7-A2")
fa.head("A2 · DIE ZAHLEN & «WERDEN»", 24)
fa.para("So sagen Sie die Zahlen: 14,04 Cent pro Liter, rund 8,35 Euro für 50 Liter. Mit werden sprechen Sie über die Zukunft und das Passiv: Am Freitag wird gespielt. Der Tankrabatt wird bis Dezember gelten.")
fa.box("BEISPIELE · Ejemplos", [("„Am Freitag wird gespielt.“ · „Der Tankrabatt gilt bis Dezember.“", "serif", False, INK, 21, 1.4)])
fa.ex("A2", "completar", "wird", "pasiva: wird + Partizip II",
      "Am Freitag ___ gespielt: Hamburg gegen Gladbach.", instr="Completa", size=20, gap=8)
fa.ex("A2", "completar", "werden", "plural: werden",
      "Am Sonntag ___ drei Spiele gespielt.", instr="Completa", size=20, gap=8)
fa.ex("A2", "completar", "wird", "werden + infinitivo expresa futuro",
      "Der Tankrabatt ___ bis Dezember gelten.", instr="Completa", size=20, gap=8)
fa.ex("A2", "opción múltiple", "A", "la voz pasiva",
      "„Es wird gespielt“ ist... A. Passiv · B. Perfekt · C. Imperativ", size=20, gap=8)
fa.end_report()
# --- col B1 ---
fb = Flow(p, [(COLX[1], CW)], CTOP, CBOT, tag="P7-B1")
fb.head("B1 · VERGLEICHE & GRÜNDE", 24)
fb.para("Vergleichen geht mit dem Komparativ: Der Abend ist länger als sonst. Gründe geben Sie mit weil: Ich bleibe zu Hause, weil es kalt ist — das Verb steht am Ende des Satzes.")
fb.box("BEISPIELE · Ejemplos", [("„Das Spiel ist später als sonst.“ · „Ich lese, weil das Buch spannend ist.“", "serif", False, INK, 21, 1.4)])
fb.ex("B1", "completar", "später", "spät → später (las 19:30 es lo más tarde)",
      "Das Spiel Hoffenheim–Schalke ist ___ (spät) als die anderen Sonntagsspiele.", instr="Completa", size=20, gap=8)
fb.ex("B1", "completar", "weil", "weil introduce la causa",
      "Es wird früher dunkel, ___ die Tage kürzer werden.", instr="Completa", size=20, gap=8)
fb.ex("B1", "transformación", "Viele bleiben zu Hause, weil es kalt ist.", "el verbo va al final en la frase con weil",
      "Viele bleiben zu Hause. Es ist kalt. (weil) → ___", instr="Reescribe", size=20, gap=8)
fb.ex("B1", "opción múltiple", "A", "länger als = más largo que",
      "„Länger als sonst“ heißt... A. más largo que de costumbre · B. igual que de costumbre · C. más corto que de costumbre", size=20, gap=8)
fb.end_report()
# --- col B2 ---
fc = Flow(p, [(COLX[2], CW)], CTOP, CBOT, tag="P7-B2")
fc.head("B2 · MEINUNG SAGEN", 24)
fc.para("Eine Meinung sagen Sie höflich so: Meiner Meinung nach ... Oder: Ich finde, dass ... — bei dass steht das Verb am Ende! Nicht sicher? Dann: Es ist fraglich, ob ...")
fc.box("BEISPIELE · Ejemplos", [("„Meiner Meinung nach braucht die Pflege mehr Geld.“ · „Niemand weiß, ob die Steuer sinkt.“", "serif", False, INK, 21, 1.4)])
fc.ex("B2", "completar", "ob", "ob introduce una pregunta indirecta",
      "Ich weiß nicht, ___ die Stromsteuer sinkt.", instr="Completa", size=20, gap=8)
fc.ex("B2", "completar", "fraglich", "Es ist fraglich, ob ... = no está claro si ...",
      "Es ist ___ , ob sich Union und SPD einigen.", instr="Completa", size=20, gap=8)
fc.ex("B2", "transformación", "Ich finde, dass die Pflege mehr Hilfe braucht.", "el verbo va al final en la frase con dass",
      "Ich finde: Die Pflege braucht mehr Hilfe. (dass) → ___", instr="Reescribe", size=20, gap=8)
fc.ex("B2", "opción múltiple", "B", "expresar una opinión con cortesía",
      "„Die Pflege braucht mehr Geld“ höflich sagen: A. „Mehr Geld, sofort!“ · B. „Meiner Meinung nach braucht die Pflege mehr Geld.“ · C. „Die Politik macht alles falsch.“", size=20, gap=8)
fc.end_report()

# --- col 3 rail: toolbox + readers + word (post-patch geometry: gap 6, pad 110) ---
ix = COLX[3]
tb = ["14,04 Cent = 14,04 céntimos por litro",
      "rund 8,35 Euro = unos 8,35 euros",
      "Es wird gespielt. = se juega (pasiva)",
      "Meiner Meinung nach = en mi opinión",
      "Ich finde, dass ... = yo creo que ...",
      "Es ist fraglich, ob ... = no está claro"]
tbh = 62 + sum(len(wrap(t, "serif", False, 20.5, CW - 44)) * 29.5 + 6 for t in tb) + 110
p.rect(ix, CTOP, CW, tbh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = CTOP + 16
p.text(ix + 22, yy3 + 26, "DER WERKZEUGKASTEN · Útiles", 23, "sans", True, OLIVE)
yy3 += 52
for t in tb:
    yy3 = p.para(ix + 22, yy3 + 20.5, t, 20.5, "serif", False, INK, CW - 44, 1.42) + 6
ry = CTOP + tbh + 16
label = "¡Un ejemplo de la redacción!"
defer = "Bis Redaktionsschluss keine Briefe oder Texte — sie erscheinen in VOL.3."
reader = "„Liebe Lucerna, am Dienstag schaue ich Bayern bei Atlético. Die Fußballwoche ist toll! Viele Grüße — die Redaktion“"
invite = "Schreiben Sie uns Ihre Sätze und Ihre Texte von Seite 8! Die besten echten Briefe drucken wir in VOL.3."
chinese = "Ejemplo de la redacción, no una carta real: hasta el cierre, sin cartas reales ni mejores textos de la página 8. ¡Envíanos tu carta real para VOL.3!"
rh = 62 + 30 + len(wrap(label, "sans", True, 20, CW - 44)) * 29 \
    + len(wrap(defer, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(reader, "serif", False, 21, CW - 44)) * 30 + 8 \
    + len(wrap(invite, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(chinese, "sans", False, 19.5, CW - 44)) * 28 + 40 + 16
# NOTE (fix1): the +16 corrects the readers-box formula's per-paragraph
# transition undercount (each drawn para adds its size on top of the
# formula's +8 gap); without it the last Chinese line was painted over by
# the word box below (occlusion COVER flag on the first fix1 render).
p.rect(ix, ry, CW, rh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ry + 16
p.text(ix + 22, yy3 + 26, "LESERBRIEFE · Tus cartas", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 20, label, 20, "sans", True, BRICK, CW - 44, 1.42)
yy3 = p.para(ix + 22, yy3 + 20.5, defer, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 21, reader, 21, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 20.5, invite, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
p.para(ix + 22, yy3 + 19.5, chinese, 19.5, "sans", False, GREY, CW - 44, 1.42)
wy3 = ry + rh + 16
p.rect(ix, wy3, CW, 150, fill=BOX, stroke=LINE, sw=1.4)
p.text(ix + 22, wy3 + 40, "NOCH EIN WORT · Una palabra más", 22, "sans", True, OLIVE)
p.para(ix + 22, wy3 + 78, "«der Tankrabatt» (Seite 2): die gesenkte Steuer auf Benzin und Diesel. El descuento en la gasolina.", 20.5, "serif", False, INK, CW - 44, 1.42)
print("P7 col3 ends", wy3 + 150)

# --- phrases of the week (verbatim from this issue) ---
py = 1520
p.hline(MX, RIGHT, py - 12, GOLD, 2)
p.text(MX, py + 28, "SÄTZE DER WOCHE · Frases de la semana", 28, "sans", True, OLIVE)
p.text(RIGHT, py + 28, "Citas textuales de los artículos de este número · entre paréntesis, la fuente", 20, "sans", False, GREY, anchor="end")
phrases = [
    ("Vier Nächte Fußball hintereinander, dann ein ganzes Wochenende Liga.", "Cuatro noches de fútbol seguidas y luego todo un fin de semana de liga.", "Seite 4 · B1"),
    ("Die Energiesteuer auf Benzin und Diesel sinkt um 14,04 Cent pro Liter.", "El impuesto sobre la energía de la gasolina y el diésel baja 14,04 céntimos por litro.", "Seite 2 · A2"),
    ("Wer 50 Liter tankt, spart rund 8,35 Euro.", "Con 50 litros se ahorran unos 8,35 euros.", "Seite 2 · A2"),
    ("Die Schule hat nach den Herbstferien wieder begonnen.", "Después de las vacaciones de otoño, la escuela volvió a empezar.", "Seite 5 · B1"),
    ("Die Tage sind kurz, die Abende lang.", "Los días son cortos y las noches, largas.", "Seite 3 · A2"),
    ("Zwei schwere Auswärtsspiele für die deutschen Teams.", "Dos difíciles partidos fuera de casa para los equipos alemanes.", "Seite 4 · B1"),
    ("Die deutsche Wirtschaft kommt langsam aus der Stagnation heraus, doch der Aufschwung trägt sich nicht selbst.", "La economía alemana sale del estancamiento, pero aún no se sostiene sola.", "Seite 6 · B2"),
    ("Es geht langsam aufwärts — aber von allein geht es nicht.", "Mejora lentamente, pero no mejora sola.", "Seite 6 · B2"),
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
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "FEHLERKLINIK · Clínica de errores", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Los cuatro errores más frecuentes · corrígelos tú antes de mirar la respuesta", 20, "sans", False, GREY, anchor="end")
clinic = [
    ("Die Schule beginnt wieder in Baden-Württemberg am Montag.", "In Baden-Württemberg beginnt die Schule am Montag wieder.", "El verbo en segunda posición: aunque el sujeto no abra la frase, el verbo sigue en segundo lugar."),
    ("Halb acht ist 8.30 Uhr.", "Halb acht ist 7.30 Uhr.", "halb acht = las siete y media (antes de las ocho)."),
    ("Die Preise sind gefallen um 14 Cent.", "Die Preise sind um 14 Cent gefallen.", "En el Perfekt, el Partizip II va al final."),
    ("Er fragt, ob kommt der Bus?", "Er fragt, ob der Bus kommt.", "En la frase con ob, el verbo va al final."),
]
for i, (wrong, right, note) in enumerate(clinic):
    cx = COLX[i]
    p.text(cx, ey + 84, "FALSCH", 19, "sans", True, BRICK)
    yy = p.para(cx, ey + 112, wrong, 20.5, "serif", False, INK, CW, 1.38)
    p.text(cx, yy + 28, "RICHTIG", 19, "sans", True, OLIVE)
    yy = p.para(cx, yy + 56, right, 20.5, "serif", True, INK, CW, 1.38)
    p.para(cx, yy + 26, note, 19, "sans", False, GREY, CW, 1.35)

# --- next issue teaser ---
ty = 2400
p.rect(MX, ty, RIGHT - MX, 130, fill=DARK)
p.text(MX + 26, ty + 46, "IN DER NÄCHSTEN AUSGABE · Próximo número (VOL.3)", 24, "sans", True, "#f3edda")
p.para(MX + 26, ty + 82, "Sonntag, 15. November: Volkstrauertag und NFL in München — American Football in der Allianz Arena · dazu St. Martin am 11. November, die Europapokal-Rückspiele und Ihre Briefe: Schreiben Sie uns! Die besten echten Briefe erscheinen in VOL.3!", 21, "serif", False, "#e8dfc8", RIGHT - MX - 52, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-sprache.svg")
print("P7 saved, exercises so far:", len(REG))
