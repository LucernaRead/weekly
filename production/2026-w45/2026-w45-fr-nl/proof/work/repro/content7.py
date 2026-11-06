# -*- coding: utf-8 -*-
"""W45 FR core VOL.3 — P7."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/fr-nl-proof/work/repro/svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 7
p = BSPage4()
p.band("LANGUE EN MAIN · TAAL IN DE PRAKTIJK", "Le Lucerna", "A2 → B2 · Les phrases de la semaine · ZINNEN VAN DE WEEK")

cA = Flow(p, [(COLX[0], CW)], 200, 1150, tag="P7-A2")
cA.head("NIVEAU A2 · BASISNIVEAU", 27)
cA.head("REPRENDRE", 24)
cA.para("« Le lundi 2 novembre, on reprend les cours. » Reprendre, c'est recommencer après une pause : on reprend les cours, on reprend le travail, on reprend la lecture. (page 2)", 22.5)
cA.head("LE FUTUR PROCHE", 24)
cA.para("aller + infinitif : « Ce soir, on va préparer le cartable. » « Lundi, les élèves vont raconter leurs vacances. » Pour parler d'un futur tout proche, c'est la forme la plus simple.", 22.5)
cA.box("LA PHRASE EXEMPLE", [
    ("« Le lundi 2 novembre, on reprend les cours. » — la phrase de la rentrée, à dire lundi matin.", "serif", False, INK, 21.5, 1.42),
])
cA.end_report()

cB = Flow(p, [(COLX[1], CW)], 200, 1150, tag="P7-B1")
cB.head("NIVEAU B1 · GEMIDDELD", 27)
cB.head("LE PASSÉ COMPOSÉ", 24)
cB.para("« Les enfants se sont déguisés samedi. » « Les cimetières se sont remplis de fleurs. » Avec se + être + participe passé : attention à l'accord avec le sujet : déguisés, remplis. (page 3)", 22.5)
cB.head("LE COMPARATIF", 24)
cB.para("plus / moins / aussi + adjectif (+ que) : « Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ? » « Ce match est aussi important que la finale. » — deux comparatifs opposés par ou ; bon devient meilleur, jamais « plus bon ».", 22.5)
cB.box("LA PHRASE EXEMPLE", [
    ("« Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ? » — le comparatif du débat sportif (page 4).", "serif", False, INK, 21.5, 1.42),
])
cB.end_report()

cC = Flow(p, [(COLX[2], CW), (COLX[3], CW)], 200, 1150, tag="P7-B2")
cC.head("NIVEAU B2 · UITDAGING", 27)
cC.head("IL EST PRÉVU QUE + SUBJONCTIF", 24)
cC.para("« Il est prévu que l'Assemblée examine la Culture mardi. » Après « il est prévu que », le verbe passe au subjonctif : examiner → examine, voter → vote, changer → change. (page 6)", 22.5)
cC.head("EXPRIMER L'ATTENTE", 24)
cC.para("« On ne connaît pas encore les finalistes. » « Les résultats seront connus samedi soir. » Pour parler d'un avenir incertain, on distingue le programme prévu et le résultat connu — jamais l'inverse.", 22.5)
cC.box("LA PHRASE EXEMPLE", [
    ("« Ce calendrier peut encore bouger. » — pouvoir + infinitif : la phrase de prudence des journaux.", "serif", False, INK, 21.5, 1.42),
])
cC.end_report()

cD = Flow(p, [(COLX[3], CW)], 200, 1150, tag="P7-outils")
cD.head("BOÎTE À OUTILS · OP ZAK", 27)
cD.para("Trois phrases à garder dans la poche, une pour chaque niveau :", 22.5)
cD.para("A2 — « Le lundi 2 novembre, on reprend les cours. »", 22.5, "serif", True, OLIVE)
cD.para("B1 — « Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ? »", 22.5, "serif", True, OLIVE)
cD.para("B2 — « Il est prévu que l'Assemblée examine la Culture mardi. »", 22.5, "serif", True, OLIVE)
cD.para("Gardez aussi le réflexe du journal : chaque phrase de la semaine vient d'un article de ce numéro. Relisez l'article, la phrase devient facile.", 22.5)
cD.bridge("Gereedschapskist · Drie meeneemzinnen, één per niveau; alle zinnen van de week komen uit artikelen in dit nummer — lees het artikel opnieuw en de zin wordt makkelijk.")
cD.end_report()

py = 1160
p.hline(MX, RIGHT, py - 14, GOLD, 2)
p.text(MX, py + 26, "LES PHRASES DE LA SEMAINE · ZINNEN VAN DE WEEK", 27, "sans", True, OLIVE)
p.text(RIGHT, py + 26, "Eén grammaticapunt + één mini-oefening per zin · antwoorden op pagina 8", 20, "sans", False, GREY, anchor="end")
pf = Flow(p, [(COLX[i], CW) for i in range(4)], py + 52, 1830, tag="P7-phrases")
phrases = [
    ("« Le lundi 2 novembre, on reprend les cours. » (page 2)",
     "Grammaticapunt · reprendre: weer beginnen, na een pauze.",
     "A2", "Après les vacances, on ___ (reprendre) les cours.", "reprend", "on → reprend"),
    ("« On ne connaît pas encore les finalistes. » (page 1)",
     "Grammaticapunt · ne...pas encore: nog niet.",
     "B1", "Il ne fait pas ___ nuit : il est 15 heures.", "encore", "pas encore = nog niet"),
    ("« Les cimetières se sont remplis de chrysanthèmes. » (page 3)",
     "Grammaticapunt · passé composé met wederkerende werkwoorden: se + être + voltooid deelwoord.",
     "B1", "Les enfants se sont ___ (déguiser) samedi.", "déguisés", "se déguiser → se sont déguisés"),
    ("« Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ? » (page 4)",
     "Grammaticapunt · comparatif: plus + bijvoeglijk naamwoord, twee tegenstellingen met ou.",
     "B1", "La finale est ___ (excitante) !", "plus excitante", "plus + bijvoeglijk naamwoord"),
    ("« Le festival se promène dans Paris. » (page 5)",
     "Grammaticapunt · se promener: wederkerend werkwoord, wandelen, rondzwerven.",
     "A2", "Le dimanche, nous nous ___ (promener) au parc.", "promenons", "se promener → nous promenons"),
    ("« Ce calendrier peut encore bouger. » (page 6)",
     "Grammaticapunt · pouvoir + infinitief: kunnen, mogen.",
     "B2", "Le programme ___ (pouvoir) changer demain.", "peut", "pouvoir → peut"),
    ("« Ce week-end, tout se joue. » (page 1)",
     "Grammaticapunt · se jouer: beslist worden, zich afspelen (wederkerend).",
     "A2", "La finale se ___ (jouer) dimanche.", "joue", "se jouer → se joue"),
    ("« Les jeunes créateurs y rencontrent leur public, en vrai. » (page 5)",
     "Grammaticapunt · rencontrer: je publiek ontmoeten; y verwijst naar de plaats.",
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
cf.head("CLINIQUE DES ERREURS · PAS OP!", 25)
cf.bridge("Elke zin bevat één fout: vind hem en verbeter hem.")
cf.ex("A2", "改错", "On n'offre jamais de chrysanthèmes pour un anniversaire.", "jamais + de: des wordt de",
      "✗ « On offre des chrysanthèmes pour un anniversaire. »", instr="Corrigeer", size=22.5)
cf.ex("A2", "改错", "Les jeunes créateurs y rencontrent leur public, en vrai.", "créateurs meervoud → rencontrent",
      "✗ « Les jeunes créateurs y rencontre leur public, en vrai. »", instr="Corrigeer", size=22.5)
cf.ex("B2", "改错", "Il est prévu que l'Assemblée examine la Culture mardi.", "il examine, zonder -s",
      "✗ « Il est prévu que l'Assemblée examines la Culture. »", instr="Corrigeer", size=22.5)
cf.ex("B1", "改错", "La finale a lieu dimanche 8 novembre.", "finale op de 8e, niet de 7e",
      "✗ « La finale a lieu dimanche 7 novembre. »", instr="Corrigeer", size=22.5)
cf.end_report()

rx, rw = span_x(2, 2)
p.rect(rx, by7 + 8, rw, 380, fill=BOX, stroke=LINE, sw=1.4)
p.text(rx + 24, by7 + 48, "LE COURRIER DES LECTEURS · LEZERSRUBRIEK", 24, "sans", True, OLIVE)
p.para(rx + 24, by7 + 86, "« Mon week-end de novembre : samedi, j'ai regardé un match à la télévision ; dimanche, j'ai cuisiné une soupe et j'ai lu vingt pages. » — Exemple de la rédaction (ce texte n'est pas une lettre de lecteur).", 21, "serif", False, INK, rw - 48, 1.42)
p.para(rx + 24, by7 + 196, "Redactiecommentaar · Stabiele passé composé, puntkomma verbindt twee dagen. Stuur je brief én je beste pagina-8-tekst in voor VOL.4!", 20, "sans", False, GREY, rw - 48, 1.4)
p.para(rx + 24, by7 + 272, "Note de la rédaction : aucun texte du VOL.2 n'était arrivé au moment de mettre sous presse (le numéro W44 n'a pas paru). Le VOL.4 reprendra la promesse.", 20, "serif", False, INK, rw - 48, 1.4)
p.para(rx + 24, by7 + 336, "Opmerking van de redactie: geen echte brieven en geen beste VOL.2-pagina-8-tekst binnen (geen W44-nummer); beide volgen in VOL.4.", 19.5, "sans", False, GREY, rw - 48, 1.4)
ty7 = by7 + 8 + 380 + 12
p.rect(rx, ty7, rw, 2540 - ty7, fill=DARK)
p.text(rx + 24, ty7 + 46, "LA SEMAINE PROCHAINE · VOL.4 VOLGENDE WEEK", 24, "sans", True, "#f3edda")
p.para(rx + 24, ty7 + 84, "Lundi 9 novembre : le Sénat examine le budget de la Sécurité sociale. Mercredi 11 novembre : l'Armistice, un jour de mémoire. Samedi 14 et dimanche 15 novembre : la Foire aux harengs et à la coquille Saint-Jacques, à Dieppe. Et vos lettres, enfin !", 21, "serif", False, "#e8dfc8", rw - 48, 1.45)
p.para(rx + 24, ty7 + 196, "Volgende week: de Senaat bespreekt de begroting voor sociale zekerheid, 11 november Wapenstilstand, de haring- en sint-jakobsschelpenbeurs in Dieppe; en jullie brieven!", 20, "sans", False, "#b3a06a", rw - 48, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-langue.svg")
print("P7 saved, exercises so far:", len(REG))
