# -*- coding: utf-8 -*-
"""W45 FR core VOL.3 — P7."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-en/svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 7
p = BSPage4()
p.band("LANGUE EN MAIN · LANGUAGE IN DEPTH", "Le Lucerna", "A2 → B2 · Les phrases de la semaine · PHRASES OF THE WEEK")

cA = Flow(p, [(COLX[0], CW)], 200, 1150, tag="P7-A2")
cA.head("NIVEAU A2 · THE BASICS", 27)
cA.head("REPRENDRE", 24)
cA.para("« Le lundi 2 novembre, on reprend les cours. » Reprendre, c'est recommencer après une pause : on reprend les cours, on reprend le travail, on reprend la lecture. (page 2)", 22.5)
cA.head("LE FUTUR PROCHE", 24)
cA.para("aller + infinitif : « Ce soir, on va préparer le cartable. » « Lundi, les élèves vont raconter leurs vacances. » Pour parler d'un futur tout proche, c'est la forme la plus simple.", 22.5)
cA.box("LA PHRASE EXEMPLE", [
    ("« Le lundi 2 novembre, on reprend les cours. » — la phrase de la rentrée, à dire lundi matin.", "serif", False, INK, 21.5, 1.42),
])
cA.end_report()

cB = Flow(p, [(COLX[1], CW)], 200, 1150, tag="P7-B1")
cB.head("NIVEAU B1 · STEP UP", 27)
cB.head("LE PASSÉ COMPOSÉ", 24)
cB.para("« Les enfants se sont déguisés samedi. » « Les cimetières se sont remplis de fleurs. » Avec se + être + participe passé : attention à l'accord avec le sujet : déguisés, remplis. (page 3)", 22.5)
cB.head("LE COMPARATIF", 24)
cB.para("plus / moins / aussi + adjectif (+ que) : « Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ? » « Ce match est aussi important que la finale. » — deux comparatifs opposés par ou ; bon devient meilleur, jamais « plus bon ».", 22.5)
cB.box("LA PHRASE EXEMPLE", [
    ("« Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ? » — le comparatif du débat sportif (page 4).", "serif", False, INK, 21.5, 1.42),
])
cB.end_report()

cC = Flow(p, [(COLX[2], CW), (COLX[3], CW)], 200, 1150, tag="P7-B2")
cC.head("NIVEAU B2 · THE CHALLENGE", 27)
cC.head("IL EST PRÉVU QUE + SUBJONCTIF", 24)
cC.para("« Il est prévu que l'Assemblée examine la Culture mardi. » Après « il est prévu que », le verbe passe au subjonctif : examiner → examine, voter → vote, changer → change. (page 6)", 22.5)
cC.head("EXPRIMER L'ATTENTE", 24)
cC.para("« On ne connaît pas encore les finalistes. » « Les résultats seront connus samedi soir. » Pour parler d'un avenir incertain, on distingue le programme prévu et le résultat connu — jamais l'inverse.", 22.5)
cC.box("LA PHRASE EXEMPLE", [
    ("« Ce calendrier peut encore bouger. » — pouvoir + infinitif : la phrase de prudence des journaux.", "serif", False, INK, 21.5, 1.42),
])
cC.end_report()

cD = Flow(p, [(COLX[3], CW)], 200, 1150, tag="P7-outils")
cD.head("BOÎTE À OUTILS · TOOLBOX", 27)
cD.para("Trois phrases à garder dans la poche, une pour chaque niveau :", 22.5)
cD.para("A2 — « Le lundi 2 novembre, on reprend les cours. »", 22.5, "serif", True, OLIVE)
cD.para("B1 — « Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ? »", 22.5, "serif", True, OLIVE)
cD.para("B2 — « Il est prévu que l'Assemblée examine la Culture mardi. »", 22.5, "serif", True, OLIVE)
cD.para("Gardez aussi le réflexe du journal : chaque phrase de la semaine vient d'un article de ce numéro. Relisez l'article, la phrase devient facile.", 22.5)
cD.bridge("Toolbox: this issue's three pocket phrases, one per level; every phrase of the week comes from an article in this issue — reread the article and the phrase becomes easy.")
cD.end_report()

py = 1160
p.hline(MX, RIGHT, py - 14, GOLD, 2)
p.text(MX, py + 26, "LES PHRASES DE LA SEMAINE · PHRASES OF THE WEEK", 27, "sans", True, OLIVE)
p.text(RIGHT, py + 26, "One grammar point + one mini-exercise per phrase · answers on page 8", 20, "sans", False, GREY, anchor="end")
pf = Flow(p, [(COLX[i], CW) for i in range(4)], py + 52, 1830, tag="P7-phrases")
phrases = [
    ("« Le lundi 2 novembre, on reprend les cours. » (page 2)",
     "Grammar point · reprendre: to go back, to start again (after a pause).",
     "A2", "Après les vacances, on ___ (reprendre) les cours.", "reprend", "on → reprend"),
    ("« On ne connaît pas encore les finalistes. » (page 1)",
     "Grammar point · ne...pas encore: not yet.",
     "B1", "Il ne fait pas ___ nuit : il est 15 heures.", "encore", "pas encore = not yet"),
    ("« Les cimetières se sont remplis de chrysanthèmes. » (page 3)",
     "Grammar point · passé composé with reflexive verbs: se + être + past participle.",
     "B1", "Les enfants se sont ___ (déguiser) samedi.", "déguisés", "se déguiser → se sont déguisés"),
    ("« Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ? » (page 4)",
     "Grammar point · comparative: plus + adjective, two opposites joined by ou.",
     "B1", "La finale est ___ (excitante) !", "plus excitante", "plus + adjective"),
    ("« Le festival se promène dans Paris. » (page 5)",
     "Grammar point · se promener: reflexive verb, to stroll.",
     "A2", "Le dimanche, nous nous ___ (promener) au parc.", "promenons", "se promener → nous promenons"),
    ("« Ce calendrier peut encore bouger. » (page 6)",
     "Grammar point · pouvoir + infinitive: can, may.",
     "B2", "Le programme ___ (pouvoir) changer demain.", "peut", "pouvoir → peut"),
    ("« Ce week-end, tout se joue. » (page 1)",
     "Grammar point · se jouer: to be decided, to be played out (reflexive).",
     "A2", "La finale se ___ (jouer) dimanche.", "joue", "se jouer → se joue"),
    ("« Les jeunes créateurs y rencontrent leur public, en vrai. » (page 5)",
     "Grammar point · rencontrer: to meet one's audience; y stands for the place.",
     "A2", "Ils ___ (rencontrer) leur public.", "rencontrent", "rencontrer → rencontrent"),
]
for sent, point, lv, q, key, note in phrases:
    pf.para(sent, 22, "serif", True, INK, 1.4, 4)
    pf.bridge(point, 19.5, 5)
    pf.ex(lv, "跟练", key, note, q, size=22)
pf.end_report()

by7 = 1870
p.hline(MX, RIGHT, by7 - 14, GOLD, 2)
cf = Flow(p, [(COLX[0], CW), (COLX[1], CW)], by7 + 8, 2268, tag="P7-clinic")
cf.head("CLINIQUE DES ERREURS", 25)
cf.bridge("The error clinic · Each sentence has one mistake: find it and correct it.")
cf.ex("A2", "改错", "On n'offre jamais de chrysanthèmes pour un anniversaire.", "jamais + de: in a negative sentence des becomes de",
      "✗ « On offre des chrysanthèmes pour un anniversaire. »", instr="Correct it", size=22.5)
cf.ex("A2", "改错", "Les jeunes créateurs y rencontrent leur public, en vrai.", "créateurs is plural → rencontrent",
      "✗ « Les jeunes créateurs y rencontre leur public, en vrai. »", instr="Correct it", size=22.5)
cf.ex("B2", "改错", "Il est prévu que l'Assemblée examine la Culture mardi.", "Subjunctive: il examine, no -s",
      "✗ « Il est prévu que l'Assemblée examines la Culture. »", instr="Correct it", size=22.5)
cf.ex("B1", "改错", "La finale a lieu dimanche 8 novembre.", "Fact: the final is on the 8th, not the 7th",
      "✗ « La finale a lieu dimanche 7 novembre. »", instr="Correct it", size=22.5)
cf.end_report()

rx, rw = span_x(2, 2)
p.rect(rx, by7 + 8, rw, 380, fill=BOX, stroke=LINE, sw=1.4)
p.text(rx + 24, by7 + 48, "LE COURRIER DES LECTEURS · READERS' CORNER", 24, "sans", True, OLIVE)
p.para(rx + 24, by7 + 86, "« Mon week-end de novembre : samedi, j'ai regardé un match à la télévision ; dimanche, j'ai cuisiné une soupe et j'ai lu vingt pages. » — Exemple de la rédaction (ce texte n'est pas une lettre de lecteur).", 21, "serif", False, INK, rw - 48, 1.42)
p.para(rx + 24, by7 + 196, "Editor's comment · An editorial example: steady passé composé, and a semicolon joining two days is worth copying. Send us your letter for VOL.4!", 20, "sans", False, GREY, rw - 48, 1.4)
p.para(rx + 24, by7 + 272, "Note de la rédaction : aucun texte du VOL.2 n'était arrivé au moment de mettre sous presse (le numéro W44 n'a pas paru). Le VOL.4 reprendra la promesse.", 20, "serif", False, INK, rw - 48, 1.4)
p.para(rx + 24, by7 + 336, "Editor's note: no VOL.2 texts had arrived by press time (no W44 issue), so this issue prints a labelled editorial example; VOL.4 will comment on real submissions.", 19.5, "sans", False, GREY, rw - 48, 1.4)
ty7 = by7 + 8 + 380 + 12
p.rect(rx, ty7, rw, 2540 - ty7, fill=DARK)
p.text(rx + 24, ty7 + 46, "LA SEMAINE PROCHAINE · VOL.4 NEXT WEEK", 24, "sans", True, "#f3edda")
p.para(rx + 24, ty7 + 84, "Lundi 9 novembre : le Sénat examine le budget de la Sécurité sociale. Mercredi 11 novembre : l'Armistice, un jour de mémoire. Samedi 14 et dimanche 15 novembre : la Foire aux harengs et à la coquille Saint-Jacques, à Dieppe. Et vos lettres, enfin !", 21, "serif", False, "#e8dfc8", rw - 48, 1.45)
p.para(rx + 24, ty7 + 196, "Next week: the Senate debates the Social Security budget, 11 November Armistice Day, the Dieppe scallop fair — and your letters, at last!", 20, "sans", False, "#b3a06a", rw - 48, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-langue.svg")
print("P7 saved, exercises so far:", len(REG))
