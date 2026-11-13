# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE (A2→B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LANGUAGE IN HAND　La langue en main", "The Lucerna", "A2 → B2　Phrases of the week　Phrases de la semaine")

f = Flow(p, [(COLX[i], CW) for i in range(3)], 200, 2560, tag="P7-main")

f.head("WORDS　A2　win / won", 28)
f.gloss("Win est au présent (on gagne à chaque fois) ; won est au passé (on a déjà gagné) — cette semaine, on emploie surtout le passé.")
f.para("win = to get first place. won = the past of win.", 23.5)
f.para("A2: “The Democrats won the House.” The vote is over, so the verb is in the past: won, not win.", 23.5)
f.para("Try it: win / won — ask “Will England win the next Ashes?” about the future: the next series is in England, in June 2027. About last year: “Australia won the first Test.”", 23.5)

f.head("WORDS　B1　more than", 28)
f.gloss("comparative = le comparatif : avec more than, on parle de quantité et de taille.")
f.para("more than = a bigger number than. In the House, 254 is more than 218. The majority is 218 — and 254 is 36 more than the majority.", 23.5)
f.para("B1: “254 seats is more than the 218 needed.” With numbers, use more than: more people, more seats, more votes.", 23.5)
f.para("Try it: “The film is longer than the trailer.” “The book is cheaper than the film.”", 23.5)

f.head("GRAMMAR　A2　will + verb", 28)
f.gloss("will + infinitif : pour ce qui va se passer ; dans les questions, will se met au début.")
f.para("The counting will continue. The new Congress will meet in January. Will the count change? Nobody knows.", 23.5)
f.para("Rule: will + verb, no -s, no -ed. “She will win.” “They will vote.” Question: “Will they watch the jungle?”", 23.5)

f.head("GRAMMAR　B1　past simple", 28)
f.gloss("past simple = le prétérit : pour ce qui s'est déjà passé ; il faut apprendre les verbes irréguliers.")
f.para("Use the past for the past: Collins published the novel in 2025. Haymitch won the 50th Games. England lost 4–0 in 2021–22. India beat Australia by 295 runs.", 23.5)
f.para("Irregular verbs in this issue: win → won, lose → lost, beat → beat, choose → chose, run → ran.", 23.5)

f.head("GRAMMAR　B2　headlines", 28)
f.gloss("headline present = le présent des titres : les journaux racontent au présent ce qui s'est déjà passé.")
f.para("Newspapers use the present in headlines for what already happened: “Democrats Win the House and the Senate” — the vote was on November 3, but the headline says Win, not Won. The present makes the news feel fresh.", 23.5)

f.head("GRAMMAR　B2　whether", 28)
f.gloss("whether introduit une subordonnée : pour ce qu'on ne sait pas, on emploie whether.")
f.para("Nobody knows whether the count will change. Nobody knows whether it will rain in Perth. Whether = if — for what you do not know.", 23.5)

f.head("GOLDEN SENTENCES", 28)
f.bridge("Phrases d'or (phrases originales de ce numéro) — apprenez-les par cœur, et vous pourrez écrire comme ça.")
gold = [
    ("The vote is over. The counting is not.", "P2"),
    ("A “call” is not the official result.", "P1"),
    ("The Ashes are not a sport for early nights.", "P4"),
    ("A midterm changes Congress, not the President.", "P6"),
    ("The map is drawn. The work starts in January.", "P6"),
    ("Two jungles, one week: a painted jungle in the cinema, and a real jungle on television.", "P3"),
    ("A small act is not small to the person it helps — and a loud voice starts with one sentence.", "P5"),
    ("On Tuesday, November 3, Americans voted in the midterm election — for all 435 seats in the House of Representatives, for 35 seats in the Senate, and for governor in 36 states.", "P1"),
]
for en, src in gold:
    f.para(f"“{en}”", 23.5, "serif", False, INK, 1.42, 2)
    f.para(f"—— From page {src.replace('P', '')} of this issue.", 19, "sans", False, GREY, 1.4, 2)
f.head("THE DRILLS　Exercices", 28)
f.bridge("Complétez avec ces mots : won / more / lost / will / published / whether / chose / win.")
f.ex("A2", "Phrases d'or", "won", "won = le passé de win (a déjà gagné)",
     "“The Democrats ___ the House.”", instr="Complétez")
f.ex("B1", "Comparatifs", "more", "more than = plus que",
     "254 is ___ than 218.", instr="Complétez")
f.ex("B1", "Passé", "lost", "lose → lost",
     "England ___ 4–0 in 2021–22.", instr="Complétez")
f.ex("A2", "Futur", "will", "will + verbe à l'infinitif",
     "The new Congress ___ meet in January.", instr="Complétez")
f.ex("B1", "Temps", "published", "publish → published",
     "Collins ___ the novel in 2025.", instr="Complétez")
f.ex("B2", "Subordonnées", "whether", "whether = si (pour ce qu'on ne sait pas)",
     "Nobody knows ___ the count will change.", instr="Complétez")
f.ex("B2", "Passé", "chose", "choose → chose",
     "ITV ___ Monday for the launch.", instr="Complétez")
f.ex("A2", "Compléter", "win", "Avec un sujet au pluriel, on met win (présent des titres)",
     "“Democrats ___ the House” is a headline.", instr="Complétez")
f.head("ERROR CLINIC　Les erreurs", 28)
f.ex("A2", "Correction", "Correct: The Democrats won the House.", "won / win, erreur de temps",
     "“The Democrats win the House in 2026.” (wrong tense)", instr="Corrigez")
f.ex("A2", "Correction", "Correct: The count continued after the vote.", "le passé de continue : continued",
     "“The count continue after the vote.” (wrong tense)", instr="Corrigez")
f.ex("B1", "Correction", "Correct: 254 is more than 218.", "more than, structure",
     "“254 is more then 218.” (wrong word)", instr="Corrigez")
f.ex("B2", "Correction", "Correct: Nobody knows whether it will change.", "whether introduit une subordonnée",
     "“Nobody knows if the count will change or not whether.” (wrong structure)", instr="Corrigez")
f.end_report()

# ---- col 3: image + toolbox + drills ----
ix = COLX[3]
image(p, "johnson.jpg", ix, 200, CW, 290)
cy7 = caption(p, ix, 490, CW, "Samuel Johnson, painted by Sir Joshua Reynolds in 1772. Johnson's dictionary fixed English words — and this page fixes yours.",
              "Sir Joshua Reynolds — public domain, via Wikimedia Commons")
v7 = Flow(p, [(ix, CW)], int(cy7) + 18, 2560, tag="P7-col3")
v7.box("THE TOOLBOX　Boîte à outils", [
    ("A2 — “The Democrats won the House.” Les démocrates ont remporté la Chambre.", "serif", False, INK, 21.5, 1.42),
    ("B1 — “254 is more than 218.” 254 est plus que 218.", "serif", False, INK, 21.5, 1.42),
    ("B2 — “Nobody knows whether the count will change.” Personne ne sait si le décompte va changer.", "serif", False, INK, 21.5, 1.42),
])
v7.head("READERS' CORNER　Courrier", 25)
v7.para("VOL.3 promised real letters from VOL.4. No letters arrived by press time. This page keeps the promise open: send your letter, your three sentences, or your five-sentence film review to the newsroom. Real letters, with your name and city only if you give them, will appear here from VOL.5.", 22)
v7.para("Le VOL.3 l'avait promis : à partir du VOL.4, nous publions les vraies lettres des lecteurs. Aucune lettre n'était arrivée au moment de mettre sous presse — la promesse reste valable : envoyez votre lettre, vos trois phrases ou votre critique de film en cinq phrases à la rédaction. Les vraies lettres paraîtront à partir du VOL.5, avec votre nom et votre ville seulement si vous l'acceptez.", 20, "sans", False, GREY, 1.4, 2)
v7.head("AN EXAMPLE LETTER　Exemple", 24)  # D5: 25->24, HEAD TOO WIDE +8.6px advance at 25
v7.para("This letter is written by the editor, only to show the shape. It is not a reader's letter. No name and no city are given, because no real letter has arrived yet.", 20, "sans", False, GREY, 1.4, 2)
v7.para("“Dear Lucerna, I read the midterm story with my class. We counted the seats together — 254, 162, 19. My question: when will the count be final? Thank you for the numbers.” — A reader, somewhere in the world.", 22)
v7.para("Cette lettre a été écrite par la rédaction, seulement pour montrer la forme. Ce n'est pas une lettre de lecteur. Ni nom ni ville n'y figurent, car aucune vraie lettre n'est encore arrivée.", 20, "sans", False, GREY, 1.4, 2)
v7.head("NEXT WEEK　Aperçu du VOL.5", 25)
v7.para("Thanksgiving in America. The Ashes: England's rematch waits until June 2027. More certified results of the midterm election. And your letters — the first real ones.", 22)
v7.end_report()
p.foot(7)
p.save(f"{OUT}/p7-lang.svg")
print("P7 saved, exercises so far:", len(REG))
