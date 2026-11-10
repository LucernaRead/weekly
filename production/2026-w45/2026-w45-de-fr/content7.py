# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE FOCUS =================
CURPAGE[0] = 7
p = BSPage4()
p.band("SPRACHE　Langue", "Die Lucerna", "A2 → B2　Sätze der Woche & Fehlerklinik　Phrases de la semaine et clinique des erreurs")

p.para(MX, 226, "Diese Seite gehört der Sprache: drei kleine Lektionen, die Sätze der Woche aus dieser Ausgabe, unsere Fehlerklinik — und Ihre Briefe.", 23, "serif", False, INK, RIGHT - MX, 1.4)
p.para(MX, 262, "Cette page est consacrée à la langue : trois mini-leçons, les phrases de la semaine (toutes citées mot pour mot dans les articles de ce numéro), la clinique des erreurs et le courrier des lecteurs.", 20, "sans", False, GREY, RIGHT - MX, 1.4)

CTOP, CBOT = 330, 1480
# --- col A2 ---
fa = Flow(p, [(COLX[0], CW)], CTOP, CBOT, tag="P7-A2")
fa.head("A2　DIE ZAHLEN & «WERDEN»", 24)
fa.para("So sagen Sie die Zahlen: 14,04 Cent pro Liter, rund 8,35 Euro für 50 Liter. Mit werden sprechen Sie über die Zukunft und das Passiv: Am Freitag wird gespielt. Der Tankrabatt wird bis Dezember gelten.")
fa.box("BEISPIELE　Exemples", [("„Am Freitag wird gespielt.“　„Der Tankrabatt gilt bis Dezember.“", "serif", False, INK, 21, 1.4)])
fa.ex("A2", "à compléter", "wird", "passif : wird + Partizip II",
      "Am Freitag ___ gespielt: Hamburg gegen Gladbach.", instr="Compléter", size=20, gap=8)
fa.ex("A2", "à compléter", "werden", "pluriel : werden",
      "Am Sonntag ___ drei Spiele gespielt.", instr="Compléter", size=20, gap=8)
fa.ex("A2", "à compléter", "wird", "werden + infinitif pour le futur",
      "Der Tankrabatt ___ bis Dezember gelten.", instr="Compléter", size=20, gap=8)
fa.ex("A2", "QCM", "A", "voix passive",
      "„Es wird gespielt“ ist... A. Passiv · B. Perfekt · C. Imperativ", size=20, gap=8)
fa.end_report()
# --- col B1 ---
fb = Flow(p, [(COLX[1], CW)], CTOP, CBOT, tag="P7-B1")
fb.head("B1　VERGLEICHE & GRÜNDE", 24)
fb.para("Vergleichen geht mit dem Komparativ: Der Abend ist länger als sonst. Gründe geben Sie mit weil: Ich bleibe zu Hause, weil es kalt ist — das Verb steht am Ende des Satzes.")
fb.box("BEISPIELE　Exemples", [("„Das Spiel ist später als sonst.“　„Ich lese, weil das Buch spannend ist.“", "serif", False, INK, 21, 1.4)])
fb.ex("B1", "à compléter", "später", "spät → später (19 h 30, le plus tard)",
      "Das Spiel Hoffenheim–Schalke ist ___ (spät) als die anderen Sonntagsspiele.", instr="Compléter", size=20, gap=8)
fb.ex("B1", "à compléter", "weil", "weil introduit une cause",
      "Es wird früher dunkel, ___ die Tage kürzer werden.", instr="Compléter", size=20, gap=8)
fb.ex("B1", "transformation", "Viele bleiben zu Hause, weil es kalt ist.", "dans une proposition en weil, le verbe va à la fin",
      "Viele bleiben zu Hause. Es ist kalt. (weil) → ___", instr="Réécrire", size=20, gap=8)
fb.ex("B1", "QCM", "A", "länger als = plus long que",
      "„Länger als sonst“ heißt... A. plus long que d'habitude · B. comme d'habitude · C. plus court que d'habitude", size=20, gap=8)
fb.end_report()
# --- col B2 ---
fc = Flow(p, [(COLX[2], CW)], CTOP, CBOT, tag="P7-B2")
fc.head("B2　MEINUNG SAGEN", 24)
fc.para("Eine Meinung sagen Sie höflich so: Meiner Meinung nach ... Oder: Ich finde, dass ... — bei dass steht das Verb am Ende! Nicht sicher? Dann: Es ist fraglich, ob ...")
fc.box("BEISPIELE　Exemples", [("„Meiner Meinung nach braucht die Pflege mehr Geld.“　„Niemand weiß, ob die Steuer sinkt.“", "serif", False, INK, 21, 1.4)])
fc.ex("B2", "à compléter", "ob", "ob introduit une question indirecte",
      "Ich weiß nicht, ___ die Stromsteuer sinkt.", instr="Compléter", size=20, gap=8)
fc.ex("B2", "à compléter", "fraglich", "Es ist fraglich, ob ... = il est douteux que ...",
      "Es ist ___ , ob sich Union und SPD einigen.", instr="Compléter", size=20, gap=8)
fc.ex("B2", "transformation", "Ich finde, dass die Pflege mehr Hilfe braucht.", "dans une proposition en dass, le verbe va à la fin",
      "Ich finde: Die Pflege braucht mehr Hilfe. (dass) → ___", instr="Réécrire", size=20, gap=8)
fc.ex("B2", "QCM", "B", "exprimer poliment une opinion",
      "„Die Pflege braucht mehr Geld“ höflich sagen: A. „Mehr Geld, sofort!“ · B. „Meiner Meinung nach braucht die Pflege mehr Geld.“ · C. „Die Politik macht alles falsch.“", size=20, gap=8)
fc.end_report()

# --- col 3 rail: toolbox + readers + word (post-patch geometry: gap 6, pad 110) ---
ix = COLX[3]
tb = ["14,04 Cent = 14,04 centimes par litre",
      "rund 8,35 Euro = environ 8,35 euros",
      "Es wird gespielt. = On jouera (passif)",
      "Meiner Meinung nach = À mon avis",
      "Ich finde, dass ... = Je trouve que ...",
      "Es ist fraglich, ob = Il est douteux que"]
tbh = 62 + sum(len(wrap(t, "serif", False, 20.5, CW - 44)) * 29.5 + 6 for t in tb) + 110
p.rect(ix, CTOP, CW, tbh, fill=BOX)
yy3 = CTOP + 16
p.text(ix + 22, yy3 + 26, "DER WERKZEUGKASTEN　Outils", 23, "sans", True, OLIVE)
yy3 += 52
for t in tb:
    yy3 = p.para(ix + 22, yy3 + 20.5, t, 20.5, "serif", False, INK, CW - 44, 1.42) + 6
ry = CTOP + tbh + 16
label = "Un exemple de la rédaction !"
defer = "Bis Redaktionsschluss keine Briefe oder Texte — sie erscheinen in VOL.3."
reader = "„Liebe Lucerna, am Dienstag schaue ich Bayern bei Atlético. Die Fußballwoche ist toll! Viele Grüße — die Redaktion“"
invite = "Schreiben Sie uns Ihre Sätze und Ihre Texte von Seite 8! Die besten echten Briefe drucken wir in VOL.3."
note_fr = "Aucune vraie lettre ni aucun meilleur texte de page 8 reçu ; suite en VOL.3."
invite_fr = "Écrivez-nous vos vraies lettres — les meilleures paraîtront dans VOL.3."
rh = 62 + 30 + len(wrap(label, "sans", True, 20, CW - 44)) * 29 \
    + len(wrap(defer, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(reader, "serif", False, 21, CW - 44)) * 30 + 8 \
    + len(wrap(invite, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(note_fr, "sans", False, 19.5, CW - 44)) * 28 + 8 \
    + len(wrap(invite_fr, "serif", False, 20.5, CW - 44)) * 29.5 + 40 + 32
# NOTE (DE x FR fan-out, as DE x EN): the formula's trailing +32 (fix1's
# +16, plus another +16) corrects the readers-box formula's per-paragraph
# transition undercount (each drawn para adds its size on top of the
# formula's +8 gap); without it the last French line would sit below the
# box border.
p.rect(ix, ry, CW, rh, fill="#f0eee5")
yy3 = ry + 16
p.text(ix + 22, yy3 + 26, "LESERBRIEFE　Vos lettres", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 20, label, 20, "sans", True, OLIVE, CW - 44, 1.42)
yy3 = p.para(ix + 22, yy3 + 20.5, defer, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 21, reader, 21, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 20.5, invite, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 19.5, note_fr, 19.5, "sans", False, GREY, CW - 44, 1.42) + 8
p.para(ix + 22, yy3 + 20.5, invite_fr, 20.5, "serif", False, INK, CW - 44, 1.42)
wy3 = ry + rh + 16
p.rect(ix, wy3, CW, 150, fill=BOX)
p.text(ix + 22, wy3 + 40, "NOCH EIN WORT　Un mot de plus", 22, "sans", True, OLIVE)
p.para(ix + 22, wy3 + 78, "«der Tankrabatt» (page 2) : la taxe réduite sur l'essence et le diesel. Réduction du carburant.", 20.5, "serif", False, INK, CW - 44, 1.42)
print("P7 col3 ends", wy3 + 150)

# --- phrases of the week (verbatim from this issue) ---
py = 1520
p.hline(MX, RIGHT, py - 12, OLIVE, 2)
p.text(MX, py + 28, "SÄTZE DER WOCHE　Phrases de la semaine", 28, "sans", True, OLIVE)
p.text(RIGHT, py + 28, "Citées mot pour mot dans les articles de ce numéro", 20, "sans", False, GREY, anchor="end")
phrases = [
    ("Vier Nächte Fußball hintereinander, dann ein ganzes Wochenende Liga.", "Quatre nuits de football d'affilée, puis tout un week-end de championnat.", "Seite 4 · B1"),
    ("Die Energiesteuer auf Benzin und Diesel sinkt um 14,04 Cent pro Liter.", "La taxe sur l'énergie pour l'essence et le diesel baisse de 14,04 centimes par litre.", "Seite 2 · A2"),
    ("Wer 50 Liter tankt, spart rund 8,35 Euro.", "Pour 50 litres, on économise environ 8,35 euros.", "Seite 2 · A2"),
    ("Die Schule hat nach den Herbstferien wieder begonnen.", "L'école a repris après les vacances d'automne.", "Seite 5 · B1"),
    ("Die Tage sind kurz, die Abende lang.", "Les jours sont courts, les soirs longs.", "Seite 3 · A2"),
    ("Zwei schwere Auswärtsspiele für die deutschen Teams.", "Deux difficiles matches à l'extérieur pour les équipes allemandes.", "Seite 4 · B1"),
    ("Die deutsche Wirtschaft kommt langsam aus der Stagnation heraus, doch der Aufschwung trägt sich nicht selbst.", "L'économie allemande sort lentement de la stagnation ; la reprise ne se porte pas seule.", "Seite 6 · B2"),
    ("Es geht langsam aufwärts — aber von allein geht es nicht.", "Ça remonte lentement — mais pas tout seul.", "Seite 6 · B2"),
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
p.text(MX, ey + 28, "FEHLERKLINIK　La clinique des erreurs", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Les quatre erreurs les plus fréquentes　corrigez d'abord, puis vérifiez", 20, "sans", False, GREY, anchor="end")
clinic = [
    ("Die Schule beginnt wieder in Baden-Württemberg am Montag.", "In Baden-Württemberg beginnt die Schule am Montag wieder.", "Verbe en deuxième position : même si le sujet n'est pas en tête, le verbe reste deuxième."),
    ("Halb acht ist 8.30 Uhr.", "Halb acht ist 7.30 Uhr.", "halb acht = 7 h 30, une demi-heure avant huit heures."),
    ("Die Preise sind gefallen um 14 Cent.", "Die Preise sind um 14 Cent gefallen.", "Au Perfekt, le Partizip II va à la fin."),
    ("Er fragt, ob kommt der Bus?", "Er fragt, ob der Bus kommt.", "Dans une subordonnée en ob, le verbe va à la fin."),
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
p.text(MX + 26, ty + 46, "IN DER NÄCHSTEN AUSGABE　Au prochain numéro (VOL.3)", 24, "sans", True, ONCLOTH)
p.para(MX + 26, ty + 82, "Sonntag, 15. November: Volkstrauertag und NFL in München — American Football in der Allianz Arena · dazu St. Martin am 11. November, die Europapokal-Rückspiele und Ihre Briefe: Schreiben Sie uns! Die besten echten Briefe erscheinen in VOL.3!", 21, "serif", False, "#cac8ba", RIGHT - MX - 52, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-sprache.svg")
print("P7 saved, exercises so far:", len(REG))
