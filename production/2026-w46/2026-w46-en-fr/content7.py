# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE FOCUS =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LANGUAGE IN HAND　La langue en main", "The Lucerna", "A2 → B2　Phrases of the week　Les phrases de la semaine")

cA = Flow(p, [(COLX[0], CW)], 200, 1150, tag="P7-A2")
cA.head("LEVEL A2　Les bases", 27)
cA.head("ELEVEN ELEVEN", 24)
cA.para("« At eleven o'clock, we stop. » Eleven is the number of the week : the eleventh hour, the eleventh day, the eleventh month. Say it slowly : e-LEV-en. The silence starts at eleven — and the word is easy to remember, because the date is the word.", 22.5)
cA.head("WILL + VERB", 24)
cA.para("For a plan or a promise : « We will remember them. » will + the verb, with no change. It is the future of the week — use it for every promise of November 11.", 22.5)
cA.box("THE EXAMPLE　L’exemple", [
    ("« The silence will last two minutes. » — will + last (page 2).", "serif", False, INK, 21.5, 1.42),
])
cA.end_report()

cB = Flow(p, [(COLX[1], CW)], 200, 1150, tag="P7-B1")
cB.head("LEVEL B1　Plus loin", 27)
cB.head("COMPARATIVES", 24)
cB.para("Short adjective + -er + than : « The Allianz Arena is bigger than most NFL stadiums. » Long adjective : more + adjective : « more convenient ». And good becomes better — never « more good ». The Allianz example is on page 4.", 22.5)
cB.head("THE PAST SIMPLE", 24)
cB.para("Regular verbs add -ed : remembered, watched. Irregular verbs change : write → wrote, go → went, choose → chose. Use it for what is already finished — Diwali, which was on November 8, and Bonfire Night, which was on November 5. The November 15 games are still to come at press time, so their results are not past yet.", 22.5)
cB.box("THE EXAMPLE　L’exemple", [
    ("« Dickens wrote the story in 1843. » — write → wrote (page 3).", "serif", False, INK, 21.5, 1.42),
])
cB.end_report()

cC = Flow(p, [(COLX[2], CW)], 200, 1150, tag="P7-B2")
cC.head("LEVEL B2　Le défi", 27)
cC.head("HEADLINE PRESENT", 24)
cC.para("Headlines speak in the present : « Munich waits for the NFL. » The present simple makes news feel live. Read the front page again and find three present-tense verbs.", 22.5)
cC.head("WHETHER = IF ?", 24)
cC.para("« Nobody knows whether this year will be faster or slower. » Whether introduces an open question inside a sentence — more elegant than if, and safe everywhere. It is the word for counting-week uncertainty.", 22.5)
cC.box("THE EXAMPLE　L’exemple", [
    ("« Patience is part of the system, not a failure of it. » — part of = une partie (page 6).", "serif", False, INK, 21.5, 1.42),
])
cC.end_report()

cD = Flow(p, [(COLX[3], CW)], 200, 1150, tag="P7-tools")
cD.head("THE TOOLBOX　Boîte à outils", 27)
cD.para("Three sentences to keep in your pocket, one for each level :", 22.5)
cD.para("A2 — « At eleven o'clock — we stop. »", 22.5, "serif", True, OLIVE)
cD.para("B1 — « Dickens wrote the story in 1843.»", 22.5)
cD.para("B2 — « Nobody knows whether this year will be faster. »", 22.5, "serif", True, OLIVE)
cD.para("And the newspaper reflex : every phrase of the week comes from an article of this issue. Re-read the article, and the phrase becomes easy.", 22.5)
cD.instrline("Boîte à outils : trois phrases de poche, une par niveau ; toutes les phrases de la semaine viennent des articles de ce numéro — relisez l’article, et la phrase devient facile.")
cD.end_report()

# --- phrases of the week ---
py = 1210
p.hline(MX, RIGHT, py - 14, OLIVE, 2)
p.text(MX, py + 26, "PHRASES OF THE WEEK　Phrases de la semaine (de ce numéro)", 27, "sans", True, OLIVE)
p.text(RIGHT, py + 26, "Chaque phrase : un point de grammaire + un petit exercice　Réponses page 8", 20, "sans", False, GREY, anchor="end")
pf = Flow(p, [(COLX[i], CW) for i in range(4)], py + 52, 1830, tag="P7-phrases")
phrases = [
    ("« On Wednesday, November 11, at eleven o'clock in the morning, something quiet happens across the English-speaking world. » (page 1)",
     "Grammaire : happen prend un -s à la 3e personne.",
     "A2", "Something quiet ___ across the world. (happen)", "happens", "happen → happens"),
    ("« At 11 a.m. on November 11, 1918, the guns of the First World War fell silent. » (page 1)",
     "Grammaire : le prétérit de fall est fell.",
     "B1", "The guns ___ silent in 1918. (fall)", "fell", "fall → fell"),
    ("« For two minutes, nobody speaks. » (page 2)",
     "Grammaire : après nobody, le verbe est au singulier.",
     "A2", "For two minutes, nobody ___. (speak)", "speaks", "nobody → speaks"),
    ("« Christmas is still six weeks away. » (page 3)",
     "Grammaire : is = est ; still = toujours, encore.",
     "B1", "Christmas ___ still six weeks away. (be)", "is", "is = est toujours"),
    ("« One Sunday is not enough — good thing the week has seven days. » (page 4)",
     "Grammaire : has = a ; the week, singulier, prend has.",
     "B1", "The week ___ seven days. (have)", "has", "have → has"),
    ("« The total will still be there in the morning — and so will the kindness. » (page 5)",
     "Grammaire : will still = continuera ; still se place après will.",
     "B2", "The total ___ still be there. (will)", "will", "will still = continuera"),
    ("« Patience is part of the system, not a failure of it. » (page 6)",
     "Grammaire : of = de ; part of = une partie de.",
     "B2", "Patience is part of the system, not a failure ___ it. (of)", "of", "of = de"),
    ("« There were no results to print — and this paper invents none. » (page 6)",
     "Grammaire : there were = prétérit de « il y a ».",
     "A2", "There ___ no results to print. (be)", "were", "there were = prétérit de « there are »"),
]
for sent, point, lv, q, key, note in phrases:
    pf.para(sent, 20.5, "serif", True, INK, 1.34, 3)
    pf.instrline(point, 19, 4)
    pf.ex(lv, "À vous", key, note, q, size=20.5)
pf.end_report()

# --- bottom: clinic (left) + readers' corner & teaser (right) ---
by7 = 1870
p.hline(MX, RIGHT, by7 - 14, OLIVE, 2)
cf = Flow(p, [(COLX[0], CW), (COLX[1], CW)], by7 + 8, 2268, tag="P7-clinic")
cf.head("THE ERROR CLINIC　Les erreurs", 25)
cf.instrline("Chaque phrase contient une erreur : trouvez-la et corrigez-la.")
cf.ex("A2", "Correction", "He doesn't remember them.", "À la 3e personne, doesn’t + verbe de base",
     "✗ « He don't remember them. »", instr="Corrigez", size=22.5)
cf.ex("A2", "Correction", "Yesterday the guns fell silent.", "Le prétérit de fall est fell",
     "✗ « Yesterday the guns falled silent. »", instr="Corrigez", size=22.5)
cf.ex("B1", "Correction", "This stadium is bigger than most.", "bigger est déjà un comparatif : pas de more en plus",
     "✗ « This stadium is more bigger than most. »", instr="Corrigez", size=22.5)
cf.ex("B1", "Correction", "She will watch the film on Friday.", "Après will, le verbe est à l’infinitif",
     "✗ « She will watches the film on Friday. »", instr="Corrigez", size=22.5)
cf.end_report()

rx, rw = span_x(2, 2)
p.rect(rx, by7 + 8, rw, 300, fill=BOX)
p.text(rx + 24, by7 + 48, "READERS' CORNER　Courrier des lecteurs", 24, "sans", True, OLIVE)
p.para(rx + 24, by7 + 86, "« I wore a poppy all week, and I stood still at eleven. Two minutes felt very long — and very short, at the same time. » — an editor's example : no real reader letters had arrived when this issue went to press, so the example stands, honestly labeled", 21.5, "serif", False, INK, rw - 48, 1.42)
p.para(rx + 24, by7 + 206, "Note de la rédaction | VOL.2 avait promis de publier de vraies lettres de lecteurs dans VOL.3, mais à la mise sous presse la rédaction n’avait reçu aucune vraie lettre ni aucun texte de VOL.2 — ce numéro le dit honnêtement et n’invente aucune lettre. Envoie-nous ta lettre et ton texte ; à partir de VOL.4, nous publierons les vraies lettres reçues.", 20, "sans", False, GREY, rw - 48, 1.4)
ty7 = by7 + 332
p.rect(rx, ty7, rw, 2560 - ty7, fill=CLOTH)
p.text(rx + 24, ty7 + 46, "NEXT WEEK　VOL.4 La semaine prochaine", 24, "sans", True, ONCLOTH)
p.para(rx + 24, ty7 + 84, "The verified midterm results — who won, and what changes. The Ashes begin in Perth on Saturday, November 21. « The Hunger Games : Sunrise on the Reaping » opens on Friday, November 20. And your real letters, if they arrive.", 21.5, "serif", False, "#cac8ba", rw - 48, 1.45)
p.para(rx + 24, ty7 + 218, "Les résultats vérifiés des élections de mi-mandat, le premier test des Ashes le 21 novembre, le nouveau « Hunger Games » le 20 novembre — et vos vraies lettres de lecteurs.", 20, "sans", False, GOOSE, rw - 48, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-langue.svg")
print("P7 saved, exercises so far:", len(REG))
