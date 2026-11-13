# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE FOCUS =================
CURPAGE[0] = 7
p = BSPage4()
p.band("SPRACHE　Língua", "Die Lucerna", "A2 → B2　Sätze der Woche & Fehlerklinik　Frases da semana e clínica de erros")

p.para(MX, 226, "Diese Seite gehört der Sprache: drei kleine Lektionen, die Sätze der Woche aus dieser Ausgabe, unsere Fehlerklinik — und Ihre Briefe.", 23, "serif", False, INK, RIGHT - MX, 1.4)
p.para(MX, 262, "Esta página é só língua: três lições curtas, as frases da semana (citadas à letra neste número), a clínica de erros — e as vossas cartas.", 20, "sans", False, GREY, RIGHT - MX, 1.4)

CTOP, CBOT = 330, 1480
# --- col A2 ---
fa = Flow(p, [(COLX[0], CW)], CTOP, CBOT, tag="P7-A2")
fa.head("A2　DATEN SAGEN", 24)
fa.para("So sagen Sie Daten: Am 18. November ist Buß- und Bettag. Am 29. November ist der erste Advent. Mit werden sprechen Sie über das Passiv: Um 20.30 Uhr wird in München gespielt.")
fa.box("BEISPIELE　Exemplos", [("„Am 18. November ist Buß- und Bettag.“　„Um 20.30 Uhr wird in München gespielt.“", "serif", False, INK, 21, 1.4)])
fa.ex("A2", "completar", "wird", "passiva: wird + Part. II",
      "Am Freitag ___ in München gespielt.", instr="Completa", size=22, gap=8)
fa.ex("A2", "completar", "werden", "Plural: werden",
      "Die Weihnachtsmärkte ___ am Montag geöffnet.", instr="Completa", size=22, gap=8)
fa.ex("A2", "completar", "wird", "werden + infinitivo: futuro",
      "Der Adventskalender ___ am 1. Dezember beginnen.", instr="Completa", size=22, gap=8)
fa.ex("A2", "escolha múltipla", "A", "passiva",
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
fb.box("BEISPIELE　Exemplos", [("„Der November ist stiller als der Oktober.“　„Ich lese, weil das Buch spannend ist.“", "serif", False, INK, 21, 1.4)])
fb.ex("B1", "completar", "stiller", "still → stiller (mais calmo que outubro)",
      "Im November ist es ___ (still) als im Oktober.", instr="Completa", size=22, gap=8)
fb.ex("B1", "completar", "weil", "weil: a causa",
      "Es wird früher dunkel, ___ die Tage kürzer werden.", instr="Completa", size=22, gap=8)
fb.ex("B1", "transformação", "Viele bleiben zu Hause, weil es dunkel ist.", "weil: verbo no fim",
      "Viele bleiben zu Hause. Es ist dunkel. (weil) → ___", instr="Reescreve", size=22, gap=8)
fb.ex("B1", "escolha múltipla", "A", "stiller als = mais calmo que …",
      "„Stiller als sonst“ heißt... A. mais calmo que o habitual · B. como o habitual · C. mais barulhento que o habitual", size=22, gap=8)
fb.end_report()
# --- col B2 ---
fc = Flow(p, [(COLX[2], CW)], CTOP, CBOT, tag="P7-B2")
fc.head("B2　MEINUNG SAGEN", 24)
fc.para("Eine Meinung sagen Sie höflich so: Meiner Meinung nach ... Oder: Ich finde, dass ... — bei dass steht das Verb am Ende! Nicht sicher? Dann: Es ist fraglich, ob ...")
fc.box("BEISPIELE　Exemplos", [("„Meiner Meinung nach braucht das Gedenken Stille.“　„Niemand weiß, ob die Einigung gelingt.“", "serif", False, INK, 21, 1.4)])
fc.ex("B2", "completar", "ob", "ob: interrogativa indireta",
      "Ich weiß nicht, ___ die Stromsteuer sinkt.", instr="Completa", size=22, gap=8)
fc.ex("B2", "completar", "fraglich", "fraglich: ainda duvidoso",
      "Es ist ___ , ob sich Union und SPD einigen.", instr="Completa", size=22, gap=8)
fc.ex("B2", "transformação", "Ich finde, dass das Gedenken Stille braucht.", "dass: verbo no fim",
      "Ich finde: Das Gedenken braucht Stille. (dass) → ___", instr="Reescreve", size=22, gap=8)
fc.ex("B2", "escolha múltipla", "B", "dar a opinião com educação",
      "„Das Gedenken braucht Stille“ höflich sagen: A. „Stille, sofort!“ · B. „Meiner Meinung nach braucht das Gedenken Stille.“ · C. „Die Politik macht alles falsch.“", size=22, gap=8)
fc.end_report()

# --- col 3 rail: toolbox + readers + word ---
# pt toolbox fix (2026-11-11): box grows UPWARD by 20, bottom fixed.
# Measured: last entry baseline 813.0 == box bottom 813.0 (clearance +0.0); the 'g'
# in 'fraglich' descends 5.2 units, so ink ended 818.2, 5.2px BELOW the box.
# Formula under-counts by 123 (6 x 20.5 missed para offsets); pad 90 -> 110 (the
# family fix) is impossible here: NOCH EIN WORT already ends 1547.5, 0.5px above
# the Sätze rule at 1548, so any downward shift crosses it. Upward growth keeps
# ry/LESERBRIEFE/NOCH EIN WORT fixed; intro ink ends ~266, so 44px gap remains
# above the new top (310). Predicted clearance: baseline +20.0, ink +14.8.
ix = COLX[3]
tb = ["18. November = 18 de novembro",
      "der Buß- und Bettag = dia de arrependimento e oração",
      "vor fast leeren Rängen = em bancadas quase vazias",
      "Es wird gespielt. = O jogo vai ser jogado (passiva)",
      "Meiner Meinung nach = Na minha opinião",
      "Es ist fraglich, ob ... = ainda duvidoso"]
tbt = CTOP - 20  # pt: toolbox top moves up 20; bottom stays 813.0
tbh = 62 + sum(len(wrap(t, "serif", False, 20.5, CW - 44)) * 29.5 + 6 for t in tb) + 90 + 20  # +20: upward growth (see note above); the old "90 validated by occlusion 0 flags" claim was void — the audit cannot see text spilling past its own box
p.rect(ix, tbt, CW, tbh, fill=BOX)
yy3 = tbt + 16
p.text(ix + 22, yy3 + 26, "DER WERKZEUGKASTEN　Material", 21, "sans", True, OLIVE)  # D5 (2026-11-12): @23pt 430.3px ran +30.0px past the box; @21pt 393.0px fits 400.5 (22pt still overflows by 11.2px). No wording change.
yy3 += 52
for t in tb:
    yy3 = p.para(ix + 22, yy3 + 20.5, t, 20.5, "serif", False, INK, CW - 44, 1.42) + 6
ry = tbt + tbh + 16  # = 829, unchanged: LESERBRIEFE / NOCH EIN WORT do not move
label = "Ein Beispiel der Redaktion!"
defer = "Bis Redaktionsschluss keine Briefe oder Texte — sie erscheinen in VOL.5."
reader = "„Liebe Lucerna, im November bastle ich einen Adventskalender. Am 1. Dezember öffne ich das erste Türchen. Viele Grüße — die Redaktion“"
invite = "Schreiben Sie uns Ihre Sätze und Ihre Texte von Seite 8! Die besten echten Briefe drucken wir in VOL.5."
chinese = "Exemplo da redação: nenhuma carta real chegou antes do fecho. Envia os teus textos para o VOL.5!"
rh = 62 + 30 + len(wrap(label, "sans", True, 20, CW - 44)) * 29 \
    + len(wrap(defer, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(reader, "serif", False, 21, CW - 44)) * 30 + 8 \
    + len(wrap(invite, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(chinese, "sans", False, 19.5, CW - 44)) * 28 + 40 + 16
p.rect(ix, ry, CW, rh, fill="#f0eee5")
yy3 = ry + 16
p.text(ix + 22, yy3 + 26, "LESERBRIEFE　Cartas dos leitores", 22, "sans", True, OLIVE)  # D5 (2026-11-12): @23pt 403.5px ran +3.2px past the box; @22pt 385.9px fits 400.5. No wording change.
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 20, label, 20, "sans", True, OLIVE, CW - 44, 1.42)
yy3 = p.para(ix + 22, yy3 + 20.5, defer, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 21, reader, 21, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 20.5, invite, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
p.para(ix + 22, yy3 + 19.5, chinese, 19.5, "sans", False, GREY, CW - 44, 1.42)
wy3 = ry + rh + 16
p.rect(ix, wy3, CW, 150, fill=BOX)
p.text(ix + 22, wy3 + 40, "NOCH EIN WORT　Mais uma palavra", 21, "sans", True, OLIVE)  # D5 (2026-11-12): @22pt 411.7px ran +11.6px past the box; @21pt 393.0px fits 400.5. No wording change.
p.para(ix + 22, wy3 + 78, "«der Adventskalender» (p. 5): um calendário com 24 portinhas.", 20.5, "serif", False, INK, CW - 44, 1.42)
print("P7 col3 ends", wy3 + 150)

# --- phrases of the week (verbatim from this issue) ---
py = 1560
p.hline(MX, RIGHT, py - 12, OLIVE, 2)
p.text(MX, py + 28, "SÄTZE DER WOCHE　Frases da semana", 28, "sans", True, OLIVE)
p.text(RIGHT, py + 28, "Citadas à letra neste número　Fonte entre parênteses", 20, "sans", False, GREY, anchor="end")
phrases = [
    ("Nach zwei Wochen Pause spielt am Freitagabend der FC Bayern gegen den 1. FC Köln.", "Depois de duas semanas de pausa, o Bayern joga sexta à noite contra o Colónia.", "Seite 1 · A2"),
    ("Es geht ums Viertelfinale der Nations League.", "Tudo se decide nos quartos da Nations League.", "Seite 1 · A2"),
    ("Nur in Sachsen ist der Buß- und Bettag ein gesetzlicher Feiertag.", "Só na Saxónia o Buß- und Bettag é feriado.", "Seite 2 · A2"),
    ("Die Märkte beginnen fast zwei Wochen früher.", "Os mercados abrem quase duas semanas antes.", "Seite 3 · A2"),
    ("Hinter jedem Türchen wartet eine kleine Überraschung.", "Atrás de cada portinha espera uma surpresinha.", "Seite 5 · B1"),
    ("Der FC Bayern gewann in Mainz mit 2:1.", "O Bayern ganhou 2–1 em Mainz.", "Seite 4 · B1"),
    ("Die stille Woche ist der Übergang: vom November in den Advent.", "A semana tranquila é a transição: de novembro para o Advento.", "Seite 6 · B2"),
    ("Am Sonntag ist es still im Land.", "Ao domingo, todo o país está calmo.", "Seite 6 · B2"),
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
p.text(MX, ey + 28, "FEHLERKLINIK　Clínica de erros", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Os quatro erros mais comuns　Corrige primeiro, depois verifica", 20, "sans", False, GREY, anchor="end")
clinic = [
    ("Am Mittwoch die Kinder basteln einen Adventskalender.", "Am Mittwoch basteln die Kinder einen Adventskalender.", "Verbo em 2.º lugar: o verbo fica em segundo mesmo sem sujeito no início."),
    ("Halb neun ist 9.30 Uhr.", "Halb neun ist 8.30 Uhr.", "halb neun = oito e meia (antes de neun)."),
    ("Die Mannschaft ist nach Berlin gereist am Montag.", "Die Mannschaft ist am Montag nach Berlin gereist.", "No Perfekt, o particípio vai para o fim."),
    ("Er fragt, ob spielt die Nationalelf am Montag?", "Er fragt, ob die Nationalelf am Montag spielt.", "Na subordinada com ob, o verbo vai para o fim."),
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
