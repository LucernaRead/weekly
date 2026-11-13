# -*- coding: utf-8 -*-
"""W47 FR core VOL.4 — P5 + P6. Press time 10 Nov 2026."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 =================
CURPAGE[0] = 5
p = BSPage4()
p.band(E["band_p5"], "Le Lucerna", E["band_p5_sub"])

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2560, tag="P5-main")
f.title("Mercredi 18 novembre : le cinéma, et la seconde main", 32)
f.byline("Par la rédaction　Niveau de lecture : B1")
f.para("Mercredi 18 novembre, seize films sortent dans les salles de cinéma en France. En France, les nouveaux films sortent le mercredi — et ce mercredi-là, le public a l'embarras du choix : il y en a pour tous les goûts. Le plus attendu : « Hunger Games : Lever de soleil sur la moisson », le prequel du réalisateur Francis Lawrence, dont le scénario raconte Haymitch, le héros du district 12, vingt-quatre ans avant Katniss. Le film dure 2 heures 38, sur grand écran.")
f.para("À côté du grand spectacle, des films plus calmes : « Les Braves », le drame historique de Lukas Dhont ; « Jupiter », d'Alexandre Smia, avec l'acteur Denis Ménochet en président face à une crise nucléaire ; « Malika », de Mounia Meddour, le biopic de la chanteuse Malika Bellaribi ; « Camembert », une comédie avec l'actrice Kristin Scott Thomas et Guillermo Guiz — une partie de Trivial Pursuit qui tourne à l'épreuve familiale ; et « Fais-moi un signe », de Mipo O, l'histoire d'un garçon entendant élevé par des parents sourds. Six films, six histoires : choisissez votre séance du mercredi soir.")
f.para("Et si on ne va pas au cinéma, on peut aller chiner : samedi 21 novembre commence la Semaine européenne de la réduction des déchets, jusqu'au 29 novembre. En France, c'est l'ADEME qui coordonne la semaine. Le thème de 2026 : « Passer de l'ultra-conso à la consommation responsable ».")
f.para("Le programme ? Des vide-dressings, des ateliers de réparation, des marchés de seconde main, partout en France. Trois verbes à retenir : réduire, réparer, réutiliser. Comme dit l'ADEME : le meilleur déchet est celui qu'on ne produit pas.")
f.gloss(E["g5"])
f.head(E["head_avous"], 25)
f.bridge(E["bridge_read5"])
f.ex("B1", "单选", "B", E["n_photo1"],
     "Mercredi 18 novembre, il sort... A. 6 films　B. 16 films　C. 56 films")
f.ex("B1", "单选", "B", E["n_photo2"],
     "Haymitch est le héros... A. d'un match　B. du prequel　C. d'une comédie")
f.ex("B1", "单选", "B", E["n_photo3"],
     "« Les Braves », c'est un film de... A. Francis Lawrence　B. Lukas Dhont　C. Mipo O")
f.ex("B1", "单选", "A", E["n_photo4"],
     "Dans « Jupiter », le président, c'est... A. Denis Ménochet　B. Johnny Depp　C. Guillermo Guiz")
f.ex("B1", "单选", "A", E["n_photo5"],
     "« Camembert », c'est l'histoire... A. d'une partie de Trivial Pursuit　B. d'un braquage　C. d'un concert")
f.bridge(E["bridge_fill5"])
f.ex("B1", "完成句子", "mercredi", E["n_palais"],
     "Les nouveaux films sortent le ___.")
f.ex("B1", "完成句子", "prequel", E["n_legende"],
     "« Hunger Games », c'est un ___.")
f.ex("B1", "完成句子", "Ménochet", E["n_vernissage"],
     "« Jupiter », c'est avec Denis ___.")
f.ex("B1", "完成句子", "21", E["n_photographes"],
     "La Semaine de la réduction des déchets commence le ___ novembre.")
f.ex("B1", "完成句子", "produit", E["n_depp"],
     "Le meilleur déchet est celui qu'on ne ___ pas.")
f.ex("A2", "完成句子", "acheter", E["n_mercredi_cine"],
     "Acheter en seconde main, c'est ___ d'occasion.")
f.bridge(E["bridge_match5"])
f.match_set("B1", "词汇配对",
            ["un prequel", "une bande-annonce", "la seconde main", "un atelier"],
            ["un film qui raconte l'avant d'une histoire", "la courte vidéo qui présente un film",
             "acheter des objets déjà utilisés", "le lieu où l'on répare ensemble"],
            ["a", "b", "c", "d"],
            [E["m_prequel"], E["m_bande"], E["m_seconde"], E["m_atelier"]],
            instr=E["instr_match"])
f.bridge(E["bridge_dialogue5"])
f.ex("B1", "完成句子", "des billets", E["n_dial1"],
     "— Tu as pris ___ pour mercredi ? — Oui, pour toi et moi.")
f.ex("B1", "完成句子", "deux", E["n_dial2"],
     "— Tu as pris combien de billets ? — ___, pour toi et moi.")
f.para("Regarder un film, c'est déjà lire : chaque film a une histoire, chaque histoire des mots nouveaux. Et le soir, on peut aussi réparer un vieux pull : le mercredi 18 novembre est un jour de sorties, comme un samedi.")
f.box("REGARDER UN FILM", [("« Un film, c'est une fenêtre sur le monde. » — dit-on. Et vous, quel film raconterait votre semaine ?", "serif", False, INK, 22, 1.5), (E["debat5_note"], "sans", False, GREY, 21, 1.45)], bsize=22, tsize=22, pad=16, gap=10)
f.end_report()

ix = COLX[3]
image(p, "melies-lune.jpg", ix, 200, CW, 270)
cy5 = caption(p, ix, 470, CW, "Georges Méliès, 1902 : la fusée dans l'œil de la Lune — le premier grand trucage du cinéma.",
              "Georges Méliès (1861-1938), Le Voyage dans la Lune, domaine public")
sy5 = cy5 + 26
p.rect(ix, sy5, CW, 470, fill=BOX)
p.text(ix + 22, sy5 + 40, E["head_sortir"], 23, "sans", True, OLIVE)
p.para(ix + 22, sy5 + 78, "Mercredi 18 : cinéma (16 sorties). Jeudi 19 : beaujolais nouveau. Samedi 21 : SERD et demies de Turin. Dimanche 22 : finales de Turin.", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, sy5 + 320, E["sortir_note"], 21.5, "serif", False, INK, CW - 44, 1.42)
qy5 = sy5 + 470 + 26
p.rect(ix, qy5, CW, 400, fill="#f0eee5")
p.text(ix + 22, qy5 + 40, E["head_mots_photo"], 23, "sans", True, OLIVE)
mots5 = E["mots_photo"]
yy5 = qy5 + 82
for m in mots5:
    p.text(ix + 22, yy5, m, 21.5, "serif", False, INK)
    yy5 += 37
dy5 = qy5 + 400 + 26
p.rect(ix, dy5, CW, 480, fill=BOX)
p.text(ix + 22, dy5 + 40, E["head_cine"], 20, "sans", True, OLIVE)
p.para(ix + 22, dy5 + 78, "Mercredi 18 novembre : « Hunger Games : Lever de soleil sur la moisson » (Francis Lawrence, 2 h 38), « Les Braves » (Lukas Dhont), « Jupiter » (Alexandre Smia, Denis Ménochet), « Malika » (Mounia Meddour), « Camembert » (Kristin Scott Thomas) et « Fais-moi un signe » (Mipo O).", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, dy5 + 400, E["cine_note"], 20, "sans", False, GREY, CW - 44, 1.4)
ty5 = dy5 + 480 + 26
p.rect(ix, ty5, CW, 2560 - ty5, fill=BOX)
p.text(ix + 22, ty5 + 40, E["head_debat"], 23, "sans", True, OLIVE)
p.para(ix + 22, ty5 + 78, "Un film au cinéma ou à la maison ? Discutez en classe : deux phrases pour, deux phrases contre. Et vous, achetez-vous d'occasion ?", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, ty5 + 285, E["debat5_note"], 20, "sans", False, GREY, CW - 44, 1.4)
p.foot(5)
p.save(f"{OUT}/p5-jeunesse.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 =================
CURPAGE[0] = 6
p = BSPage4()
p.band(E["band_p6"], "Le Lucerna", E["band_p6_sub"])

f = Flow(p, [(COLX[0], CW), (COLX[1], CW)], 200, 1300, tag="P6-deep")
f.title("Au Sénat, mercredi 18 : le vote du budget de la Sécu", 32)
f.byline("Par la rédaction　Niveau de lecture : B2")
f.para("Cette semaine, le Sénat examine le projet de loi de financement de la Sécurité sociale pour 2027. La discussion générale s'ouvre lundi 9 novembre ; ensuite, les sénateurs discutent les articles, un par un — sauf le 11 novembre, jour férié, et vraisemblablement le dimanche 15. Le texte qu'ils examinent est celui du gouvernement, dans sa version initiale. Plus de 1 200 amendements ont été déposés.")
f.para("Pourquoi la version initiale ? Parce que le 23 octobre, l'Assemblée nationale a rejeté la partie « recettes » du texte, par 115 voix contre 1. Le rejet a arrêté l'examen : la partie « dépenses » n'a jamais été débattue par les députés. La commission des affaires sociales du Sénat a préparé son rapport le mercredi 4 novembre.")
f.para("Attention, lecteurs : ce numéro corrige son propre calendrier. La semaine dernière, nous avions annoncé un vote solennel mardi 3 novembre, sur la première partie du budget de l'État, celle des recettes. Ce vote n'a pas eu lieu mardi 3 novembre : reporté une deuxième fois, il a eu lieu mercredi 4 novembre, le soir. La première partie est rejetée, et tout le texte tombe en première lecture.")
f.para("Le résultat, le soir du 4 novembre : 458 voix contre, 0 voix pour, 2 abstentions. Tous les amendements votés par les députés tombent avec le texte, et c'est la version initiale du gouvernement qui part au Sénat. Le gouvernement veut ramener le déficit de la Sécu de 21,8 à 12,7 milliards d'euros en 2027 ; la commission du Sénat s'engage à tenir ce niveau de déficit. Elle propose aussi de relever de 1 260 à 1 500 euros le montant jusqu'auquel les pensions sont indexées sur l'inflation.")
f.gloss(E["g6"])
f.end_report()

chx, chw = COLX[0], 2 * CW + GUT
chy = 1330
chart_rows = [
    ("23 oct.", "Rejet 115–1 des recettes de la Sécu", OLIVE),
    ("4 nov.", "Rejet 458–0 des recettes du budget", OLIVE),
    ("9–17 nov.", "Débat au Sénat : la Sécu", OLIVE),
    ("18 nov.", "Vote solennel : la Sécu", OLIVE),
    ("20 nov.", "Le Sénat examine le budget de l'État", OLIVE),
    ("26 nov.", "Fin du délai de 50 jours (art. 47-1)", OLIVE),
    ("9 déc.", "Vote solennel : le budget de l'État", OLIVE),
]
chart_h = 90 + len(chart_rows) * 48 + 60  # rows + source/note lines + ~14px pad (was +104: 44px dead space under the notes; W47 fix round: the 7th row costs ~4px net, e6 flow stays under 2560)
p.rect(chx, chy, chw, chart_h, fill=BOX)
p.text(chx + 22, chy + 40, E["head_chart"], 24, "sans", True, OLIVE)
p.text(chx + 22, chy + 74, E["chart_sub"], 19, "sans", False, GREY)
byy = chy + 90
for d, t, col in chart_rows:
    p.text(chx + 22, byy + 22, d, 21, "sans", True, OLIVE)
    p.text(chx + 200, byy + 22, t, 21.5, "serif", False, INK)
    byy += 48
p.text(chx + 22, byy + 14, "Source : ordre du jour du Sénat ; Public Sénat.", 18.5, "sans", False, GREY)
p.text(chx + 22, byy + 40, E["chart_note"], 19, "sans", False, GREY)

e6 = Flow(p, [(COLX[0], CW), (COLX[1], CW)], chy + chart_h + 24, 2560, tag="P6-ex")
e6.head(E["head_lire"], 25)
e6.bridge(E["bridge_chart"])
e6.ex("B2", "图表读数", "B", E["n_chart1"],
      "Le 23 octobre : les recettes... A. adoptées　B. rejetées　C. reportées", size=21)
e6.ex("B2", "图表读数", "B", E["n_chart2"],
      "Le 4 novembre, le vote... A. 115–1　B. 458–0　C. 404–1", size=21)
e6.ex("B2", "图表读数", "B", E["n_chart3"],
      "Le vote sur la Sécu... A. 9 nov.　B. 18 nov.　C. 20 nov.", size=21)
e6.ex("B2", "图表读数", "B", E["n_chart4"],
      "Le budget de l'État, dès le... A. 9 nov.　B. 20 nov.　C. 26 nov.", size=21)
e6.ex("B1", "图表读数", "C", E["n_chart5"],
      "Le vote sur le budget... A. 18 nov.　B. 26 nov.　C. 9 déc.", size=21)
e6.ex("B1", "图表读数", "B", E["n_chart6"],
      "Cinquante jours, jusqu'au... A. 9 nov.　B. 26 nov.　C. 18 déc.", size=21)
e6.head(E["head_mots6"], 25)
e6.match_set("B2", "词汇配对",
              ["un sénateur", "rejeter", "un vote", "une commission"],
              ["un élu du Sénat", "dire non à un texte",
               "la décision ensemble", "le groupe qui prépare"],
              ["a", "b", "c", "d"],
              [E["m_senateur"], E["m_rejeter"], E["m_vote"], E["m_commission"]],
              instr=E["instr_match"])
e6.end_report()

g = Flow(p, [(COLX[2], CW), (COLX[3], CW)], 200, 1300, tag="P6-opinion")
g.head(E["head_opinion"], 25)
g.para("À mon avis, ...　Selon les chiffres, ...　D'après le calendrier, ... Trois portes pour commencer une phrase d'opinion — et une règle : on distingue le programme prévu et le résultat connu.", 23.5)
g.box("LES PHRASES DES JOURNAUX", [
    ("« Le texte part au Sénat. » — " + E["box_senat"], "serif", False, INK, 21.5, 1.42),
    ("« Ce calendrier peut encore bouger. » — " + E["box_bouger"], "serif", False, INK, 21.5, 1.42),
    ("« Les résultats ne sont pas connus. » — " + E["box_connus"], "serif", False, INK, 21.5, 1.42),
])
g.head("IL EST PRÉVU QUE + SUBJONCTIF", 23)
g.para("Après « il est prévu que », le verbe passe au subjonctif : examiner → examine, voter → vote, changer → change. C'est la forme des journaux quand le programme est prévu mais pas encore réalisé.", 23.5)
g.bridge(E["bridge_prevu"])
g.end_report()

g2 = Flow(p, [(COLX[2], CW), (COLX[3], CW)], 1330, 2560, tag="P6-micro")
g2.head(E["head_comp6"], 24)
g2.bridge(E["bridge_comp6"])
g2.ex("B1", "完成句子", "plus long", E["n_comp6a"],
      "Un débat au Sénat est ___ (long) qu'un concert.", size=21.5)
g2.ex("B2", "完成句子", "moins simple", E["n_comp6b"],
      "Le budget est ___ (simple) qu'un calendrier. (moins)", size=21.5)
g2.ex("B2", "完成句子", "aussi important", E["n_comp6c"],
      "Le budget de la Sécu est ___ (important) que le budget de l'État. (aussi)", size=21.5)
g2.head(E["head_micro6"], 25)
g2.bridge(E["bridge_micro6"])
g2.ex("B2", "完成句子", "examine", E["n_micro6a"],
      "Cette semaine, le Sénat ___ le budget de la Sécu.", size=21.5)
g2.ex("B2", "完成句子", "ont rejeté", E["n_micro6b"],
      "Le 4 novembre, les députés ___ les recettes du budget.", size=21.5)
g2.ex("B2", "完成句子", "part", E["n_micro6c"],
      "Le texte ___ au Sénat.", size=21.5)
g2.ex("B1", "完成句子", "peut", E["n_micro6d"],
      "Le calendrier ___ encore bouger.", size=21.5)
g2.ex("B1", "完成句子", "connus", E["n_micro6e"],
      "Les résultats du 18 novembre ne sont pas encore ___.", size=21.5)
g2.box(E["head_3dates"], [
    ("23 oct. — rejet 115–1 des recettes de la Sécu.", "serif", False, INK, 21.5, 1.42),
    ("4 nov. — rejet 458–0 des recettes du budget.", "serif", False, INK, 21.5, 1.42),
    ("18 nov. — vote solennel au Sénat (prévu).", "serif", False, INK, 21.5, 1.42),
], tsize=21)
g2.head(E["head_debat"], 25)
g2.para("Faut-il annoncer un programme avant les résultats ? Discutez en classe : deux phrases pour, deux phrases contre — en distinguant « prévu » et « décidé ».", 23.5)
g2.bridge(E["bridge_debat6"])
g2.head("APRÈS LE VOTE", 25)
g2.para("Après le vote du Sénat, le texte repartira vers l'Assemblée : c'est la navette parlementaire, les allers-retours entre les deux chambres. Si le désaccord persiste, une commission mixte paritaire — sept députés et sept sénateurs — cherchera un texte commun.", 23.5)
g2.end_report()
p.foot(6)
p.save(f"{OUT}/p6-politique.svg")
print("P6 saved, exercises so far:", len(REG))
