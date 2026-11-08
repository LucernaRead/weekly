# -*- coding: utf-8 -*-
"""W45 FR core VOL.2 — P3 + P4."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · 文化 (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURE　CULTURA", "Le Lucerna", "NIVEAU A2 → B1　Halloween, Toussaint　HALLOWEEN Y TODOS LOS SANTOS")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2560, tag="P3-main")
f.title("Halloween, puis la Toussaint : deux fêtes, deux ambiances", 32)
f.byline("Par la rédaction　Niveau de lecture : A2 → B1")
f.para("Samedi 31 octobre, les enfants français se sont déguisés : sorcières, fantômes, super-héros. Ils ont frappé aux portes et crié : « Des bonbons ou un sort ! » Dans les parcs, les soirées costumées ont attiré les familles, et les citrouilles orange étaient partout.")
f.para("Le lendemain, dimanche 1er novembre, l'ambiance a changé : c'était la Toussaint, le jour des fleurs. Les cimetières se sont remplis de chrysanthèmes — blancs, jaunes, violets. Les familles ont posé les fleurs sur les tombes, nettoyé les pierres, et sont restées un moment en silence.")
f.para("Deux jours, deux visages de l'automne : le rire d'abord, le souvenir ensuite. En France, le chrysanthème reste la fleur des cimetières : on n'offre jamais de chrysanthèmes pour un anniversaire. Pour faire plaisir, on choisit des roses ou des tulipes.")
f.para("Et lundi 2 novembre ? C'est le jour des morts : un jour de souvenir en famille, plus discret que la Toussaint, souvent confondu avec elle. La Toussaint honore tous les saints ; le 2 novembre, on pense à ses propres morts. Deux jours voisins, deux sens différents.")
f.gloss("se déguiser disfrazarse · un sort hechizo, broma · une ambiance ambiente · le souvenir recuerdo, conmemoración · confondre confundir · discret discreto, silencioso.")
f.head("À VOUS !　A PRACTICAR", 25)
f.bridge("¿Verdadero o falso? (Vrai / Faux).")
f.ex("A2", "Verdadero/Falso", "Vrai", "Halloween fue el sábado 31 de octubre",
     "Halloween a eu lieu samedi 31 octobre.", instr="Vrai ou faux ?")
f.ex("A2", "Verdadero/Falso", "Vrai", "En Todos los Santos los cementerios se llenan de crisantemos",
     "Le 1er novembre, les cimetières sont pleins de chrysanthèmes.", instr="Vrai ou faux ?")
f.ex("A2", "Verdadero/Falso", "Faux", "Los crisantemos nunca se regalan",
     "On offre des chrysanthèmes pour un anniversaire.", instr="Vrai ou faux ?")
f.ex("B1", "Verdadero/Falso", "Faux", "El 2 de noviembre es jour des morts, no Toussaint",
     "Le 2 novembre, c'est la Toussaint.", instr="Vrai ou faux ?")
f.ex("B1", "Verdadero/Falso", "Vrai", "En el texto: le rire d'abord, le souvenir ensuite",
     "Halloween, c'est le rire ; la Toussaint, c'est le souvenir.", instr="Vrai ou faux ?")
f.bridge("Completa con déguisement / tombe / citrouille / souvenir.")
f.ex("B1", "Completar", "déguisement", "En Halloween los niños se disfrazan",
     "Pour Halloween, les enfants portent un ___.")
f.ex("A2", "Completar", "tombe", "Las flores se ponen sobre la tumba",
     "On pose les fleurs sur la ___.")
f.ex("A2", "Completar", "citrouille", "La calabaza es el símbolo de Halloween",
     "Une ___ orange est le symbole d'Halloween.")
f.ex("B1", "Completar", "souvenir", "Todos los Santos es un día de recuerdo",
     "La Toussaint est le jour du ___.")
f.bridge("Reescribe las frases (con ne...jamais / ne...plus / ne...pas).")
f.ex("B1", "Reescribir", "On n'offre jamais de chrysanthèmes pour un anniversaire.", "jamais + de (sin cambio de artículo)",
     "(jamais) On offre des chrysanthèmes pour un anniversaire. → ___", instr="Reescribe")
f.ex("B1", "Reescribir", "Les feuilles ne sont plus vertes en novembre.", "ne...plus = ya no",
     "(plus) Les feuilles sont vertes en novembre. → ___", instr="Reescribe")
f.ex("B1", "Reescribir", "Le 2 novembre n'est pas la Toussaint.", "n'est pas = no es",
     "(pas) Le 2 novembre est la Toussaint. → ___", instr="Reescribe")
f.head("PEUR SUR LE PARC", 25)
f.para("Au parc Astérix, à Plailly, la fête d'Halloween s'appelle « Peur sur le Parc ». Elle a commencé le 3 octobre et se termine dimanche 8 novembre. Cette année, les nouveautés s'appellent « La Forêt sans Retour » et « Le Parcours des Petits Chaudrons ».", 23.5)
f.para("Le parc distingue les journées en famille et les nuits qui font peur, avec une échelle de peur par couleurs. Pour les enfants sensibles, il existe même un badge gratuit « repousse-monstres ». La dernière soirée nocturne, samedi 7 novembre de 19 heures à 1 heure du matin, demande un billet spécial.", 23.5)
f.bridge("Practica · Preguntas sobre Halloween en el parque.")
f.ex("A2", "Completar", "nocturne", "Sábado 7: último evento nocturno",
     "Samedi 7 novembre, c'est la dernière ___ du parc.")
f.ex("B1", "Completar", "badge", "Los niños sensibles reciben una insignia gratuita contra monstruos",
     "Les enfants sensibles reçoivent un ___ gratuit.")
f.ex("A2", "Completar", "Plailly", "El parque Astérix está en Plailly",
     "Le parc Astérix se trouve à ___.")
f.ex("B1", "Opción múltiple", "B", "Peur sur le Parc, del 3 de octubre al 8 de noviembre",
     "Peur sur le Parc se termine... A. le 31 octobre · B. le 8 novembre · C. le 1er novembre")
f.ex("B1", "Completar", "couleurs", "Los niveles de miedo se distinguen por colores",
     "L'échelle de peur utilise des ___.")
f.ex("A2", "Completar", "19 heures", "El evento nocturno dura de 19 h a 1 h",
     "La nocturne commence à ___ .")
f.end_report()

ix = COLX[3]
image(p, "chrysanthemum-blanco.jpg", ix, 200, CW, 540)
cy3 = caption(p, ix, 740, CW,
              "Le chrysanthème, fleur du souvenir en France : on le pose sur les tombes, on ne l'offre jamais en cadeau.",
              "Planche botanique, Flora de Filipinas (Blanco), XIXe siècle, domaine public")
by3 = cy3 + 22
p.rect(ix, by3, CW, 452, fill=BOX)
p.text(ix + 22, by3 + 40, "LES MOTS DES FÊTES　LÉXICO", 23, "sans", True, OLIVE)
mots = [
    "un saint — santo", "un cimetière — cementerio", "une tombe — tumba",
    "un jour férié — día festivo", "se souvenir — recordar, conmemorar",
    "un déguisement — disfraz", "une citrouille — calabaza",
    "un bonbon — caramelo", "un fantôme — fantasma", "un sort — hechizo, maldición",
]
yy3 = by3 + 82
for m in mots:
    p.text(ix + 22, yy3, m, 21.5, "serif", False, INK)
    yy3 += 37
zy3 = by3 + 452 + 26
p.rect(ix, zy3, CW, 476, fill="#f0eee5")
p.text(ix + 22, zy3 + 40, "ZOOM　LE PARC EN CHIFFRES", 23, "sans", True, OLIVE)
p.para(ix + 22, zy3 + 78, "Du 3 octobre au 8 novembre : 12 soirées nocturnes, dont la dernière samedi 7 novembre. Le jour, le parc ouvre de 10 heures à 19 heures. Deux nouveautés 2026 : « La Forêt sans Retour » et « Le Parcours des Petits Chaudrons ».", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, zy3 + 340, "Del 3 de octubre al 8 de noviembre: 12 eventos nocturnos, el último el sábado 7. De día, abierto de 10 a 19 h.", 20, "sans", False, GREY, CW - 44, 1.4)
dy3 = zy3 + 476 + 26
p.rect(ix, dy3, CW, 330, fill=BOX)
p.text(ix + 22, dy3 + 40, "DATES À RETENIR　FECHAS", 23, "sans", True, OLIVE)
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
p.para(ix + 22, yy3 + 20, "Ojo: Dieppe, el 14–15 de noviembre, no esta semana.", 19.5, "sans", False, GREY, CW - 44, 1.4)
py3 = dy3 + 330 + 30
p.text(ix, py3 + 24, "POUR OU CONTRE ?", 23, "sans", True, OLIVE)
p.hline(ix, ix + CW, py3 + 38, OLIVE, 2)
p.para(ix, py3 + 74, "Halloween au parc : fête joyeuse ou trop effrayante ? Écrivez votre avis en deux phrases pour le courrier des lecteurs (page 7).", 20.5, "serif", False, INK, CW, 1.4)
p.foot(3)
p.save(f"{OUT}/p3-culture.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · 体育 (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT　DEPORTE", "Le Lucerna", "NIVEAU B1　Tennis　Masters de Paris")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2560, tag="P4-main")
f.title("Le Masters de Paris : la dernière finale de la saison", 32)
f.byline("Par la rédaction　Niveau de lecture : B1")
f.para("C'est le dernier grand tournoi de tennis de la saison : le Rolex Paris Masters, sur dur, en salle, à la Paris La Défense Arena de Nanterre. Les qualifications ont eu lieu les 31 octobre et 1er novembre ; le tableau principal se joue du lundi 2 au dimanche 8 novembre.")
f.para("Le programme est simple à retenir : quarts de finale vendredi 6 novembre, demi-finales samedi 7, finales dimanche 8 — la finale du simple, la finale du double, et la finale du simple en fauteuil, à midi. Le tenant du titre, Jannik Sinner, vainqueur en 2025, est le nom à connaître — mais pour 2026, on ne connaît pas encore les finalistes.")
f.para("Pourquoi ce tournoi compte-t-il tant ? Parce que c'est un Masters 1000, le plus haut niveau après les quatre tournois du Grand Chelem. Les meilleurs joueurs du monde s'y retrouvent, en salle, où la balle va très vite. Un match peut basculer sur deux ou trois points.")
f.para("En France, on regarde aussi les tribunes : Nanterre devient, une semaine par an, la capitale du tennis. Les enfants des clubs viennent voir leurs héros de près, raquette à la main, et repartent avec des phrases de commentateurs dans la tête.")
f.para("Et après le tennis ? Le football continue : la 10e journée de Ligue 1 se joue du vendredi 6 au dimanche 8 novembre. Le grand match du week-end, c'est Lens – Marseille, dimanche 8. Au Parc des Princes, samedi 7, le Paris SG reçoit Troyes.")
f.gloss("un tournoi torneo · sur dur en pista dura · en salle en pista cubierta · un tableau principal cuadro principal · le tenant du titre defensor del título · basculer cambiar, inclinarse · les tribunes gradas.")
f.head("À VOUS !　A PRACTICAR", 25)
f.bridge("Lee el artículo de la página 4 y elige la respuesta correcta.")
f.ex("B1", "Opción múltiple", "B", "La final es el domingo 8",
     "Les finales du Masters ont lieu... A. samedi 7 · B. dimanche 8 · C. vendredi 6")
f.ex("B1", "Opción múltiple", "A", "El Masters se juega en pista cubierta y dura",
     "Le Masters se joue... A. en salle, sur dur · B. sur terre battue · C. sur herbe")
f.ex("B1", "Opción múltiple", "C", "El defensor del título 2025 es Sinner",
     "Le tenant du titre 2025, c'est... A. Novak Djokovic · B. Carlos Alcaraz · C. Jannik Sinner")
f.ex("B1", "Opción múltiple", "B", "Gran partido de la 10.ª jornada de Ligue 1: Lens – Marsella",
     "Le grand match du week-end, c'est... A. Paris SG – Troyes · B. Lens – Marseille · C. Rennes – Lille")
f.ex("B1", "Opción múltiple", "A", "Domingo 8: también final individual en silla de ruedas (mediodía)",
     "Dimanche 8, on joue aussi... A. la finale fauteuil · B. les qualifications · C. un match amical")
f.bridge("Une cada palabra de tenis con su significado.")
f.match_set("B1", "Emparejar",
            ["un tournoi", "une raquette", "les tribunes", "un tenant du titre"],
            ["la compétition avec plusieurs matchs", "l'instrument pour frapper la balle",
             "les places des spectateurs", "le vainqueur de l'année dernière"],
            ["a", "b", "c", "d"],
            ["tournoi=torneo a", "raquette=raqueta b", "tribunes=gradas c", "tenant=defensor del título d"],
            instr="Une")
f.bridge("Completa con el comparativo (plus / moins).")
f.ex("B1", "Completar", "plus vite", "En pista cubierta la pelota va más rápido",
     "En salle, la balle va ___ (vite) qu'en plein air.")
f.ex("B1", "Completar", "plus grand", "Un Masters 1000 está por debajo de los Grand Slams",
     "Un Masters 1000 est ___ (grand) qu'un petit tournoi.")
f.ex("B1", "Completar", "moins longue", "La temporada en pista cubierta es más corta que la de verano",
     "La saison en salle est ___ (longue) que la saison d'été. (moins)")
f.head("LE FOOTBALL DU WEEK-END", 25)
f.para("La 10e journée de Ligue 1 commence vendredi 6 novembre avec Toulouse – Strasbourg. Samedi 7, Auxerre reçoit le Paris FC, et le Paris SG reçoit Troyes au Parc des Princes. Dimanche 8, six matchs : Rennes – Lille, Le Mans – Monaco, Le Havre – Lorient, Brest – Lyon, Angers – Nice — dont le choc Lens – Marseille.", 23.5)
f.para("Pour les lecteurs de français, un match de football est une leçon gratuite : les commentateurs répètent les mêmes phrases — « il frappe ! », « c'est le but ! », « quelle ambiance ! » — et les noms des villes deviennent familiers.", 23.5)
f.bridge("Nota — un choc gran partido · recevoir recibir, enfrentarse a · familier familiar.")
f.head("REGARDER UN MATCH", 25)
f.para("Quelques phrases suffisent pour suivre un match avec les commentaires français. Les commentateurs parlent vite, mais ils répètent souvent les mêmes expressions : écoutez, répétez, criez avec eux !", 23.5)
f.box("LES PHRASES DU COMMENTATEUR", [
    ("« Allez ! » — ¡Vamos! · « Quelle action ! » — ¡Qué jugada!", "serif", False, INK, 21.5, 1.42),
    ("« Il marque ! » — ¡Marca! · « C'est gagné ! » — ¡Ganado!", "serif", False, INK, 21.5, 1.42),
    ("« Quel point ! » — ¡Qué punto! (Tenis) · « Balle de match ! » — ¡Punto de partido!", "serif", False, INK, 21.5, 1.42),
])
f.end_report()

ix = COLX[3]
p.rect(ix, 200, CW, 470, fill=BOX)
p.text(ix + 22, 240, "LE MASTERS EN CHIFFRES", 23, "sans", True, OLIVE)
p.para(ix + 22, 278, "41e édition en 2026 (40e anniversaire). Dernier Masters 1000 de la saison. En salle, sur dur, à Nanterre. Qualifications les 31 octobre et 1er novembre ; tableau principal du 2 au 8 novembre ; finales dimanche 8.", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, 520, "Le tournoi en fauteuil se joue du 6 au 8 novembre, avec sa finale simple dimanche à midi.", 21.5, "serif", False, INK, CW - 44, 1.42)
vy = 696
p.rect(ix, vy, CW, 416, fill="#f0eee5")
p.text(ix + 22, vy + 40, "LES MOTS DU TENNIS　LÉXICO", 23, "sans", True, OLIVE)
mots4 = [
    "le tennis — tenis", "une balle — pelota", "un set — set",
    "un match — partido", "un point — punto", "la finale — final",
    "un adversaire — rival", "un titre — título",
]
yy4 = vy + 82
for m in mots4:
    p.text(ix + 22, yy4, m, 21.5, "serif", False, INK)
    yy4 += 37
sy4 = vy + 416 + 26
p.rect(ix, sy4, CW, 218, fill=BOX)
p.text(ix + 22, sy4 + 40, "À SUIVRE　CONTINUARÁ", 23, "sans", True, OLIVE)
p.para(ix + 22, sy4 + 80, "Les finalistes seront connus samedi soir, après les demi-finales. Les résultats du week-end seront dans le VOL.4.", 21.5, "serif", False, INK, CW - 44, 1.42)
mf = Flow(p, [(ix, CW)], sy4 + 218 + 30, 2560, tag="P4-micro")
mf.head("MICRO-DRILLS　A PRACTICAR", 24)
mf.bridge("Completa con finale / quarts / demi-finales / tableau / fauteuil / choc.")
mf.ex("B1", "Completar", "quarts", "Los cuartos de final son el viernes",
      "Les ___ de finale ont lieu vendredi 6.", size=23)
mf.ex("B1", "Completar", "demi-finales", "Las semifinales son el sábado",
      "Les ___ ont lieu samedi 7.", size=23)
mf.ex("B1", "Completar", "finale", "La final individual es el domingo",
      "La ___ du simple a lieu dimanche 8.", size=23)
mf.ex("B1", "Completar", "tableau", "El cuadro principal empieza el lunes",
      "Le ___ principal commence lundi 2.", size=23)
mf.ex("B1", "Completar", "fauteuil", "El torneo en silla de ruedas, de viernes a domingo",
      "Le tournoi en ___ se joue du 6 au 8.", size=23)
mf.ex("A2", "Completar", "choc", "Lens – Marsella es el gran partido del fin de semana",
      "Lens – Marseille, c'est le ___ du week-end.", size=23)
mf.end_report()
db4 = mf.y + 6
p.rect(ix, db4, CW, 2560 - db4, fill="#f0eee5")
p.text(ix + 22, db4 + 40, "LE DÉBAT　EL DEBATE", 23, "sans", True, OLIVE)
p.para(ix + 22, db4 + 78, "Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ? Discutez en classe : deux phrases pour, deux phrases contre.", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, db4 + 196, "¿Finalistas desconocidos de antemano: más emocionante o más frustrante? Escribe dos frases a favor y dos en contra.", 20, "sans", False, GREY, CW - 44, 1.4)
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
