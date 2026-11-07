# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-de-pt/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE FOCUS =================
CURPAGE[0] = 7
p = BSPage4()
p.band("SPRACHE · Língua", "Die Lucerna", "A2 → B2 · Sätze der Woche & Fehlerklinik · Frases da semana e clínica de erros")

p.para(MX, 226, "Diese Seite gehört der Sprache: drei kleine Lektionen, die Sätze der Woche aus dieser Ausgabe, unsere Fehlerklinik — und Ihre Briefe.", 23, "serif", False, INK, RIGHT - MX, 1.4)
p.para(MX, 262, "Esta página é toda sobre língua: três lições curtas, as frases da semana (todas citadas palavra por palavra dos artigos desta edição), a clínica de erros e as cartas dos leitores.", 20, "sans", False, GREY, RIGHT - MX, 1.4)

CTOP, CBOT = 330, 1480
# --- col A2 ---
fa = Flow(p, [(COLX[0], CW)], CTOP, CBOT, tag="P7-A2")
fa.head("A2 · DIE ZAHLEN & «WERDEN»", 24)
fa.para("So sagen Sie die Zahlen: 14,04 Cent pro Liter, rund 8,35 Euro für 50 Liter. Mit werden sprechen Sie über die Zukunft und das Passiv: Am Freitag wird gespielt. Der Tankrabatt wird bis Dezember gelten.")
fa.box("BEISPIELE · Exemplos", [("„Am Freitag wird gespielt.“ · „Der Tankrabatt gilt bis Dezember.“", "serif", False, INK, 21, 1.4)])
fa.ex("A2", "Completar frases", "wird", "passiva: wird + Partizip II",
      "Am Freitag ___ gespielt: Hamburg gegen Gladbach.", instr="Complete", size=20, gap=8)
fa.ex("A2", "Completar frases", "werden", "plural: werden",
      "Am Sonntag ___ drei Spiele gespielt.", instr="Complete", size=20, gap=8)
fa.ex("A2", "Completar frases", "wird", "werden + infinitivo para o futuro",
      "Der Tankrabatt ___ bis Dezember gelten.", instr="Complete", size=20, gap=8)
fa.ex("A2", "Escolha múltipla", "A", "voz passiva",
      "„Es wird gespielt“ ist... A. Passiv · B. Perfekt · C. Imperativ", size=20, gap=8)
fa.end_report()
# --- col B1 ---
fb = Flow(p, [(COLX[1], CW)], CTOP, CBOT, tag="P7-B1")
fb.head("B1 · VERGLEICHE & GRÜNDE", 24)
fb.para("Vergleichen geht mit dem Komparativ: Der Abend ist länger als sonst. Gründe geben Sie mit weil: Ich bleibe zu Hause, weil es kalt ist — das Verb steht am Ende des Satzes.")
fb.box("BEISPIELE · Exemplos", [("„Das Spiel ist später als sonst.“ · „Ich lese, weil das Buch spannend ist.“", "serif", False, INK, 21, 1.4)])
fb.ex("B1", "Completar frases", "später", "spät → später (19:30 é o mais tarde)",
      "Das Spiel Hoffenheim–Schalke ist ___ (spät) als die anderen Sonntagsspiele.", instr="Complete", size=20, gap=8)
fb.ex("B1", "Completar frases", "weil", "weil introduz um motivo",
      "Es wird früher dunkel, ___ die Tage kürzer werden.", instr="Complete", size=20, gap=8)
fb.ex("B1", "Transformação de frases", "Viele bleiben zu Hause, weil es kalt ist.", "na oração com weil, o verbo vai para o fim",
      "Viele bleiben zu Hause. Es ist kalt. (weil) → ___", instr="Reescreva", size=20, gap=8)
fb.ex("B1", "Escolha múltipla", "A", "länger als = mais longo que",
      "„Länger als sonst“ heißt... A. mais longo que o habitual · B. igual ao habitual · C. mais curto que o habitual", size=20, gap=8)
fb.end_report()
# --- col B2 ---
fc = Flow(p, [(COLX[2], CW)], CTOP, CBOT, tag="P7-B2")
fc.head("B2 · MEINUNG SAGEN", 24)
fc.para("Eine Meinung sagen Sie höflich so: Meiner Meinung nach ... Oder: Ich finde, dass ... — bei dass steht das Verb am Ende! Nicht sicher? Dann: Es ist fraglich, ob ...")
fc.box("BEISPIELE · Exemplos", [("„Meiner Meinung nach braucht die Pflege mehr Geld.“ · „Niemand weiß, ob die Steuer sinkt.“", "serif", False, INK, 21, 1.4)])
fc.ex("B2", "Completar frases", "ob", "ob introduz uma pergunta indireta",
      "Ich weiß nicht, ___ die Stromsteuer sinkt.", instr="Complete", size=20, gap=8)
fc.ex("B2", "Completar frases", "fraglich", "Es ist fraglich, ob ... = é duvidoso se ...",
      "Es ist ___ , ob sich Union und SPD einigen.", instr="Complete", size=20, gap=8)
fc.ex("B2", "Transformação de frases", "Ich finde, dass die Pflege mehr Hilfe braucht.", "na oração com dass, o verbo vai para o fim",
      "Ich finde: Die Pflege braucht mehr Hilfe. (dass) → ___", instr="Reescreva", size=20, gap=8)
fc.ex("B2", "Escolha múltipla", "B", "uma forma educada de dar uma opinião",
      "„Die Pflege braucht mehr Geld“ höflich sagen: A. „Mehr Geld, sofort!“ · B. „Meiner Meinung nach braucht die Pflege mehr Geld.“ · C. „Die Politik macht alles falsch.“", size=20, gap=8)
fc.end_report()

# --- col 3 rail: toolbox + readers + word (post-patch geometry: gap 6, pad 110) ---
ix = COLX[3]
tb = ["14,04 Cent = 14,04 centavos por litro",
      "rund 8,35 Euro = cerca de 8,35 euros",
      "Es wird gespielt. = Será jogado",
      "Meiner Meinung nach ... = opinião",
      "Ich finde, dass ... = Acho que ...",
      "Es ist fraglich, ob ... = é duvidoso se ..."]
tbh = 62 + sum(len(wrap(t, "serif", False, 20.5, CW - 44)) * 29.5 + 6 for t in tb) + 110
p.rect(ix, CTOP, CW, tbh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = CTOP + 16
p.text(ix + 22, yy3 + 26, "DER WERKZEUGKASTEN · Úteis", 23, "sans", True, OLIVE)
yy3 += 52
for t in tb:
    yy3 = p.para(ix + 22, yy3 + 20.5, t, 20.5, "serif", False, INK, CW - 44, 1.42) + 6
ry = CTOP + tbh + 16
label = "Um exemplo da redação!"
defer = "Bis Redaktionsschluss keine Briefe oder Texte — sie erscheinen in VOL.3."
reader = "„Liebe Lucerna, am Dienstag schaue ich Bayern bei Atlético. Die Fußballwoche ist toll! Viele Grüße — die Redaktion“"
invite = "Schreiben Sie uns Ihre Sätze und Ihre Texte von Seite 8! Die besten echten Briefe drucken wir in VOL.3."
note_pt = "Sem cartas reais nem melhores textos da página 8; a promessa passa ao VOL.3."
invite_pt = "Escreva-nos! Envie a sua carta real e o seu texto da página 8 para o VOL.3."
rh = 62 + 30 + len(wrap(label, "sans", True, 20, CW - 44)) * 29 \
    + len(wrap(defer, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(reader, "serif", False, 21, CW - 44)) * 30 + 8 \
    + len(wrap(invite, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(note_pt, "sans", False, 19.5, CW - 44)) * 28 + 8 \
    + len(wrap(invite_pt, "serif", False, 20.5, CW - 44)) * 29.5 + 40 + 32
# NOTE (fix1): the +16 corrects the readers-box formula's per-paragraph
# transition undercount (each drawn para adds its size on top of the
# formula's +8 gap); without it the last Portuguese line was painted over by
# the word box below (occlusion COVER flag on the first fix1 render).
p.rect(ix, ry, CW, rh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ry + 16
p.text(ix + 22, yy3 + 26, "LESERBRIEFE · Cartas dos leitores", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 20, label, 20, "sans", True, BRICK, CW - 44, 1.42)
yy3 = p.para(ix + 22, yy3 + 20.5, defer, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 21, reader, 21, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 20.5, invite, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 19.5, note_pt, 19.5, "sans", False, GREY, CW - 44, 1.42) + 8
p.para(ix + 22, yy3 + 20.5, invite_pt, 20.5, "serif", False, INK, CW - 44, 1.42)
wy3 = ry + rh + 16
p.rect(ix, wy3, CW, 150, fill=BOX, stroke=LINE, sw=1.4)
p.text(ix + 22, wy3 + 40, "NOCH EIN WORT · Mais uma palavra", 22, "sans", True, OLIVE)
p.para(ix + 22, wy3 + 78, "«der Tankrabatt» (Seite 2): die gesenkte Steuer auf Benzin und Diesel. Desconto no combustível.", 20.5, "serif", False, INK, CW - 44, 1.42)
print("P7 col3 ends", wy3 + 150)

# --- phrases of the week (verbatim from this issue) ---
py = 1520
p.hline(MX, RIGHT, py - 12, GOLD, 2)
p.text(MX, py + 28, "SÄTZE DER WOCHE · Frases da semana", 28, "sans", True, OLIVE)
p.text(RIGHT, py + 28, "Citadas palavra por palavra dos artigos desta edição", 20, "sans", False, GREY, anchor="end")
phrases = [
    ("Vier Nächte Fußball hintereinander, dann ein ganzes Wochenende Liga.", "Quatro noites de futebol seguidas, depois um fim de semana inteiro de liga.", "Seite 4 · B1"),
    ("Die Energiesteuer auf Benzin und Diesel sinkt um 14,04 Cent pro Liter.", "O imposto sobre a energia da gasolina e do diesel cai 14,04 centavos por litro.", "Seite 2 · A2"),
    ("Wer 50 Liter tankt, spart rund 8,35 Euro.", "Se abastecer 50 litros, você economiza cerca de 8,35 euros.", "Seite 2 · A2"),
    ("Die Schule hat nach den Herbstferien wieder begonnen.", "A escola recomeçou depois das férias de outono.", "Seite 5 · B1"),
    ("Die Tage sind kurz, die Abende lang.", "Os dias são curtos, as noites longas.", "Seite 3 · A2"),
    ("Zwei schwere Auswärtsspiele für die deutschen Teams.", "Dois jogos difíceis fora de casa para os times alemães.", "Seite 4 · B1"),
    ("Die deutsche Wirtschaft kommt langsam aus der Stagnation heraus, doch der Aufschwung trägt sich nicht selbst.", "A economia alemã deixa devagar a estagnação, mas a recuperação não se sustenta sozinha.", "Seite 6 · B2"),
    ("Es geht langsam aufwärts — aber von allein geht es nicht.", "As coisas melhoram devagar — mas não sozinhas.", "Seite 6 · B2"),
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
p.text(MX, ey + 28, "FEHLERKLINIK · Clínica de erros", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Os quatro erros mais frequentes dos aprendizes · corrija primeiro, depois confira", 20, "sans", False, GREY, anchor="end")
clinic = [
    ("Die Schule beginnt wieder in Baden-Württemberg am Montag.", "In Baden-Württemberg beginnt die Schule am Montag wieder.", "Verbo em segundo: mesmo que o sujeito não venha primeiro, o verbo fica em segundo lugar."),
    ("Halb acht ist 8.30 Uhr.", "Halb acht ist 7.30 Uhr.", "halb acht = 7h30, meia hora antes das oito."),
    ("Die Preise sind gefallen um 14 Cent.", "Die Preise sind um 14 Cent gefallen.", "No Perfekt, o Partizip II vai para o fim."),
    ("Er fragt, ob kommt der Bus?", "Er fragt, ob der Bus kommt.", "Na oração com ob, o verbo vai para o fim."),
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
p.text(MX + 26, ty + 46, "IN DER NÄCHSTEN AUSGABE · Próxima edição (VOL.3)", 24, "sans", True, "#f3edda")
p.para(MX + 26, ty + 82, "Sonntag, 15. November: Volkstrauertag und NFL in München — American Football in der Allianz Arena · dazu St. Martin am 11. November, die Europapokal-Rückspiele und Ihre Briefe: Schreiben Sie uns! Die besten echten Briefe erscheinen in VOL.3!", 21, "serif", False, "#e8dfc8", RIGHT - MX - 52, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-sprache.svg")
print("P7 saved, exercises so far:", len(REG))
