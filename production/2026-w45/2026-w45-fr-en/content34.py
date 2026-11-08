# -*- coding: utf-8 -*-
"""W45 FR core VOL.2 — P3 + P4."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · culture (A2->B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURE　FESTIVALS", "Le Lucerna", "NIVEAU A2 → B1　Halloween, Toussaint　HALLOWEEN AND ALL SAINTS")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2560, tag="P3-main")
f.title("Halloween, puis la Toussaint : deux fêtes, deux ambiances", 32)
f.byline("Par la rédaction　Niveau de lecture : A2 → B1")
f.para("Samedi 31 octobre, les enfants français se sont déguisés : sorcières, fantômes, super-héros. Ils ont frappé aux portes et crié : « Des bonbons ou un sort ! » Dans les parcs, les soirées costumées ont attiré les familles, et les citrouilles orange étaient partout.")
f.para("Le lendemain, dimanche 1er novembre, l'ambiance a changé : c'était la Toussaint, le jour des fleurs. Les cimetières se sont remplis de chrysanthèmes — blancs, jaunes, violets. Les familles ont posé les fleurs sur les tombes, nettoyé les pierres, et sont restées un moment en silence.")
f.para("Deux jours, deux visages de l'automne : le rire d'abord, le souvenir ensuite. En France, le chrysanthème reste la fleur des cimetières : on n'offre jamais de chrysanthèmes pour un anniversaire. Pour faire plaisir, on choisit des roses ou des tulipes.")
f.para("Et lundi 2 novembre ? C'est le jour des morts : un jour de souvenir en famille, plus discret que la Toussaint, souvent confondu avec elle. La Toussaint honore tous les saints ; le 2 novembre, on pense à ses propres morts. Deux jours voisins, deux sens différents.")
f.gloss("se déguiser to dress up · un sort a spell, a trick · une ambiance an atmosphere · le souvenir a memory · confondre to confuse · discret discreet, quiet.")
f.head("À VOUS !　YOUR TURN", 25)
f.bridge("True or false (Vrai / Faux).")
f.ex("A2", "阅读判断", "Vrai", "Halloween was on Saturday 31 October",
     "Halloween a eu lieu samedi 31 octobre.", instr="Vrai ou faux ?")
f.ex("A2", "阅读判断", "Vrai", "cemeteries full of chrysanthemums",
     "Le 1er novembre, les cimetières sont pleins de chrysanthèmes.", instr="Vrai ou faux ?")
f.ex("A2", "阅读判断", "Faux", "chrysanthemums are never given as a present",
     "On offre des chrysanthèmes pour un anniversaire.", instr="Vrai ou faux ?")
f.ex("B1", "阅读判断", "Faux", "2 November is the jour des morts",
     "Le 2 novembre, c'est la Toussaint.", instr="Vrai ou faux ?")
f.ex("B1", "阅读判断", "Vrai", "in the text: le rire d'abord, le souvenir ensuite",
     "Halloween, c'est le rire ; la Toussaint, c'est le souvenir.", instr="Vrai ou faux ?")
f.bridge("Fill in with déguisement / tombe / citrouille / souvenir.")
f.ex("B1", "完成句子", "déguisement", "children wear costumes at Halloween",
     "Pour Halloween, les enfants portent un ___.")
f.ex("A2", "完成句子", "tombe", "flowers are placed on the grave",
     "On pose les fleurs sur la ___.")
f.ex("A2", "完成句子", "citrouille", "the pumpkin is the symbol of Halloween",
     "Une ___ orange est le symbole d'Halloween.")
f.ex("B1", "完成句子", "souvenir", "All Saints' Day is a day of remembrance",
     "La Toussaint est le jour du ___.")
f.bridge("Rewrite the sentences (with ne...jamais / ne...plus / ne...pas).")
f.ex("B1", "句型转换", "On n'offre jamais de chrysanthèmes pour un anniversaire.", "jamais + de (no article change)",
     "(jamais) On offre des chrysanthèmes pour un anniversaire. → ___", instr="Rewrite")
f.ex("B1", "句型转换", "Les feuilles ne sont plus vertes en novembre.", "ne...plus = no longer",
     "(plus) Les feuilles sont vertes en novembre. → ___", instr="Rewrite")
f.ex("B1", "句型转换", "Le 2 novembre n'est pas la Toussaint.", "n'est pas = is not",
     "(pas) Le 2 novembre est la Toussaint. → ___", instr="Rewrite")
f.head("PEUR SUR LE PARC", 25)
f.para("Au parc Astérix, à Plailly, la fête d'Halloween s'appelle « Peur sur le Parc ». Elle a commencé le 3 octobre et se termine dimanche 8 novembre. Cette année, les nouveautés s'appellent « La Forêt sans Retour » et « Le Parcours des Petits Chaudrons ».", 23.5)
f.para("Le parc distingue les journées en famille et les nuits qui font peur, avec une échelle de peur par couleurs. Pour les enfants sensibles, il existe même un badge gratuit « repousse-monstres ». La dernière soirée nocturne, samedi 7 novembre de 19 heures à 1 heure du matin, demande un billet spécial.", 23.5)
f.bridge("Your turn · little questions about the park at Halloween.")
f.ex("A2", "完成句子", "nocturne", "Saturday 7th is the last night event",
     "Samedi 7 novembre, c'est la dernière ___ du parc.")
f.ex("B1", "完成句子", "badge", "sensitive children get a free badge",
     "Les enfants sensibles reçoivent un ___ gratuit.")
f.ex("A2", "完成句子", "Plailly", "the Astérix park is in Plailly",
     "Le parc Astérix se trouve à ___.")
f.ex("B1", "单选", "B", "Peur sur le Parc runs 3 October to 8 November",
     "Peur sur le Parc se termine... A. le 31 octobre · B. le 8 novembre · C. le 1er novembre")
f.ex("B1", "完成句子", "couleurs", "the fear scale uses colours",
     "L'échelle de peur utilise des ___.")
f.ex("A2", "完成句子", "19 heures", "the night event runs 7 p.m. to 1 a.m.",
     "La nocturne commence à ___ .")
f.end_report()

ix = COLX[3]
image(p, "chrysanthemum-blanco.jpg", ix, 200, CW, 540)
cy3 = caption(p, ix, 740, CW,
              "Le chrysanthème, fleur du souvenir en France : on le pose sur les tombes, on ne l'offre jamais en cadeau.",
              "Planche botanique, Flora de Filipinas (Blanco), XIXe siècle, domaine public")
by3 = cy3 + 22
p.rect(ix, by3, CW, 452, fill=BOX)
p.text(ix + 22, by3 + 40, "LES MOTS DES FÊTES　FESTIVAL", 23, "sans", True, OLIVE)
mots = [
    "un saint — a saint", "un cimetière — a cemetery", "une tombe — a grave",
    "un jour férié — a public holiday", "se souvenir — to remember",
    "un déguisement — a costume", "une citrouille — a pumpkin",
    "un bonbon — a sweet", "un fantôme — a ghost", "un sort — a spell, a curse",
]
yy3 = by3 + 82
for m in mots:
    p.text(ix + 22, yy3, m, 21.5, "serif", False, INK)
    yy3 += 37
zy3 = by3 + 452 + 26
p.rect(ix, zy3, CW, 476, fill="#f0eee5")
p.text(ix + 22, zy3 + 40, "ZOOM　LE PARC EN CHIFFRES", 23, "sans", True, OLIVE)
p.para(ix + 22, zy3 + 78, "Du 3 octobre au 8 novembre : 12 soirées nocturnes, dont la dernière samedi 7 novembre. Le jour, le parc ouvre de 10 heures à 19 heures. Deux nouveautés 2026 : « La Forêt sans Retour » et « Le Parcours des Petits Chaudrons ».", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, zy3 + 340, "From 3 October to 8 November: 12 night events; the last one on 7 November; open 10 a.m. to 7 p.m. in the daytime.", 20, "sans", False, GREY, CW - 44, 1.4)
dy3 = zy3 + 476 + 26
p.rect(ix, dy3, CW, 330, fill=BOX)
p.text(ix + 22, dy3 + 40, "DATES À RETENIR　TO REMEMBER", 23, "sans", True, OLIVE)
dates3 = [
    ("lun. 2 nov.", "rentrée + jour des morts"),
    ("sam. 7 nov.", "dernière nocturne à Plailly"),
    ("dim. 8 nov.", "finales + fermeture du parc"),
    ("sam. 14 nov.", "foire de Dieppe (à venir)"),
]
yy3 = dy3 + 84
for d, t in dates3:
    p.text(ix + 22, yy3, d, 19.5, "sans", True, OLIVE)
    p.text(ix + 168, yy3, t, 18.5, "serif", False, INK)
    yy3 += 42
p.para(ix + 22, yy3 + 20, "Note: the Dieppe scallop fair is on 14–15 November, not this week.", 19.5, "sans", False, GREY, CW - 44, 1.4)
py3 = dy3 + 330 + 30
p.text(ix, py3 + 24, "POUR OU CONTRE ?", 23, "sans", True, OLIVE)
p.hline(ix, ix + CW, py3 + 38, OLIVE, 2)
p.para(ix, py3 + 74, "Halloween au parc : fête joyeuse ou trop effrayante ? Écrivez votre avis en deux phrases pour le courrier des lecteurs (page 7).", 20.5, "serif", False, INK, CW, 1.4)
p.foot(3)
p.save(f"{OUT}/p3-culture.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · sport (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT　SPORTS", "Le Lucerna", "NIVEAU B1　Tennis　Masters de Paris")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2560, tag="P4-main")
f.title("Le Masters de Paris : la dernière finale de la saison", 32)
f.byline("Par la rédaction　Niveau de lecture : B1")
f.para("C'est le dernier grand tournoi de tennis de la saison : le Rolex Paris Masters, sur dur, en salle, à la Paris La Défense Arena de Nanterre. Les qualifications ont eu lieu les 31 octobre et 1er novembre ; le tableau principal se joue du lundi 2 au dimanche 8 novembre.")
f.para("Le programme est simple à retenir : quarts de finale vendredi 6 novembre, demi-finales samedi 7, finales dimanche 8 — la finale du simple, la finale du double, et la finale du simple en fauteuil, à midi. Le tenant du titre, Jannik Sinner, vainqueur en 2025, est le nom à connaître — mais pour 2026, on ne connaît pas encore les finalistes.")
f.para("Pourquoi ce tournoi compte-t-il tant ? Parce que c'est un Masters 1000, le plus haut niveau après les quatre tournois du Grand Chelem. Les meilleurs joueurs du monde s'y retrouvent, en salle, où la balle va très vite. Un match peut basculer sur deux ou trois points.")
f.para("En France, on regarde aussi les tribunes : Nanterre devient, une semaine par an, la capitale du tennis. Les enfants des clubs viennent voir leurs héros de près, raquette à la main, et repartent avec des phrases de commentateurs dans la tête.")
f.para("Et après le tennis ? Le football continue : la 10e journée de Ligue 1 se joue du vendredi 6 au dimanche 8 novembre. Le grand match du week-end, c'est Lens – Marseille, dimanche 8. Au Parc des Princes, samedi 7, le Paris SG reçoit Troyes.")
f.gloss("un tournoi a tournament · sur dur on hard court · en salle indoors · un tableau principal the main draw · le tenant du titre the defending champion · basculer to swing, to turn · les tribunes the stands.")
f.head("À VOUS !　YOUR TURN", 25)
f.bridge("Read page 4 and choose the right answer.")
f.ex("B1", "单选", "B", "the finals are on Sunday 8th",
     "Les finales du Masters ont lieu... A. samedi 7 · B. dimanche 8 · C. vendredi 6")
f.ex("B1", "单选", "A", "the Masters is played indoors, on hard court",
     "Le Masters se joue... A. en salle, sur dur · B. sur terre battue · C. sur herbe")
f.ex("B1", "单选", "C", "the 2025 defending champion is Sinner",
     "Le tenant du titre 2025, c'est... A. Novak Djokovic · B. Carlos Alcaraz · C. Jannik Sinner")
f.ex("B1", "单选", "B", "the big Ligue 1 match of the weekend: Lens – Marseille",
     "Le grand match du week-end, c'est... A. Paris SG – Troyes · B. Lens – Marseille · C. Rennes – Lille")
f.ex("B1", "单选", "A", "on Sunday 8th there is also the wheelchair singles final (at noon)",
     "Dimanche 8, on joue aussi... A. la finale fauteuil · B. les qualifications · C. un match amical")
f.bridge("Match the tennis words with their meanings.")
f.match_set("B1", "词汇配对",
            ["un tournoi", "une raquette", "les tribunes", "un tenant du titre"],
            ["la compétition avec plusieurs matchs", "l'instrument pour frapper la balle",
             "les places des spectateurs", "le vainqueur de l'année dernière"],
            ["a", "b", "c", "d"],
            ["tournoi = tournament a", "raquette = racket b", "tribunes = stands c", "tenant = defending champion d"],
            instr="Match")
f.bridge("Complete with the comparative (plus / moins).")
f.ex("B1", "完成句子", "plus vite", "the ball is faster indoors",
     "En salle, la balle va ___ (vite) qu'en plein air.")
f.ex("B1", "完成句子", "plus grand", "a Masters 1000 is just below the Grand Slams",
     "Un Masters 1000 est ___ (grand) qu'un petit tournoi.")
f.ex("B1", "完成句子", "moins longue", "the indoor season is shorter than the summer season",
     "La saison en salle est ___ (longue) que la saison d'été. (moins)")
f.head("LE FOOTBALL DU WEEK-END", 25)
f.para("La 10e journée de Ligue 1 commence vendredi 6 novembre avec Toulouse – Strasbourg. Samedi 7, Auxerre reçoit le Paris FC, et le Paris SG reçoit Troyes au Parc des Princes. Dimanche 8, six matchs : Rennes – Lille, Le Mans – Monaco, Le Havre – Lorient, Brest – Lyon, Angers – Nice — dont le choc Lens – Marseille.", 23.5)
f.para("Pour les lecteurs de français, un match de football est une leçon gratuite : les commentateurs répètent les mêmes phrases — « il frappe ! », « c'est le but ! », « quelle ambiance ! » — et les noms des villes deviennent familiers.", 23.5)
f.bridge("NOTE · un choc a big match · recevoir to host, to receive · familier familiar.")
f.head("REGARDER UN MATCH", 25)
f.para("Quelques phrases suffisent pour suivre un match avec les commentaires français. Les commentateurs parlent vite, mais ils répètent souvent les mêmes expressions : écoutez, répétez, criez avec eux !", 23.5)
f.box("LES PHRASES DU COMMENTATEUR", [
    ("« Allez ! » — Come on! · « Quelle action ! » — What a play!", "serif", False, INK, 21.5, 1.42),
    ("« Il marque ! » — He scores! · « C'est gagné ! » — It's won!", "serif", False, INK, 21.5, 1.42),
    ("« Quel point ! » — What a point! (tennis) · « Balle de match ! » — Match point!", "serif", False, INK, 21.5, 1.42),
])
f.end_report()

ix = COLX[3]
p.rect(ix, 200, CW, 470, fill=BOX)
p.text(ix + 22, 240, "LE MASTERS EN CHIFFRES", 23, "sans", True, OLIVE)
p.para(ix + 22, 278, "41e édition en 2026 (40e anniversaire). Dernier Masters 1000 de la saison. En salle, sur dur, à Nanterre. Qualifications les 31 octobre et 1er novembre ; tableau principal du 2 au 8 novembre ; finales dimanche 8.", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, 520, "Le tournoi en fauteuil se joue du 6 au 8 novembre, avec sa finale simple dimanche à midi.", 21.5, "serif", False, INK, CW - 44, 1.42)
vy = 696
p.rect(ix, vy, CW, 416, fill="#f0eee5")
p.text(ix + 22, vy + 40, "LES MOTS DU TENNIS　TENNIS", 23, "sans", True, OLIVE)
mots4 = [
    "le tennis — tennis", "une balle — a ball", "un set — a set",
    "un match — a match", "un point — a point", "la finale — the final",
    "un adversaire — an opponent", "un titre — a title",
]
yy4 = vy + 82
for m in mots4:
    p.text(ix + 22, yy4, m, 21.5, "serif", False, INK)
    yy4 += 37
sy4 = vy + 416 + 26
p.rect(ix, sy4, CW, 218, fill=BOX)
p.text(ix + 22, sy4 + 40, "À SUIVRE　TO BE CONTINUED", 23, "sans", True, OLIVE)
p.para(ix + 22, sy4 + 80, "Les finalistes seront connus samedi soir, après les demi-finales. Les résultats du week-end seront dans le VOL.4.", 21.5, "serif", False, INK, CW - 44, 1.42)
mf = Flow(p, [(ix, CW)], sy4 + 218 + 30, 2560, tag="P4-micro")
mf.head("MICRO-DRILLS　QUICK PRACTICE", 24)
mf.bridge("Fill in with finale / quarts / demi-finales / tableau / fauteuil / choc.")
mf.ex("B1", "完成句子", "quarts", "the quarter-finals are on Friday",
      "Les ___ de finale ont lieu vendredi 6.", size=23)
mf.ex("B1", "完成句子", "demi-finales", "the semi-finals are on Saturday",
      "Les ___ ont lieu samedi 7.", size=23)
mf.ex("B1", "完成句子", "finale", "the singles final is on Sunday",
      "La ___ du simple a lieu dimanche 8.", size=23)
mf.ex("B1", "完成句子", "tableau", "the main draw starts on Monday",
      "Le ___ principal commence lundi 2.", size=23)
mf.ex("B1", "完成句子", "fauteuil", "the wheelchair tournament runs Friday to Sunday",
      "Le tournoi en ___ se joue du 6 au 8.", size=23)
mf.ex("A2", "完成句子", "choc", "Lens – Marseille is the big match of the weekend",
      "Lens – Marseille, c'est le ___ du week-end.", size=23)
mf.end_report()
db4 = mf.y + 6
p.rect(ix, db4, CW, 2560 - db4, fill="#f0eee5")
p.text(ix + 22, db4 + 40, "LE DÉBAT　DEBATE", 23, "sans", True, OLIVE)
p.para(ix + 22, db4 + 78, "Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ? Discutez en classe : deux phrases pour, deux phrases contre.", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, db4 + 196, "Not knowing the finalists in advance: more exciting or more frustrating? Two sentences for, two against.", 20, "sans", False, GREY, CW - 44, 1.4)
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
