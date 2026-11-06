# -*- coding: utf-8 -*-
"""W45 FR core VOL.3 — P3 + P4."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-de/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · 文化 (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURE · KULTUR", "Le Lucerna", "NIVEAU A2 → B1 · Halloween, Toussaint · HALLOWEEN & TOUSSAINT")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2540, tag="P3-main")
f.title("Halloween, puis la Toussaint : deux fêtes, deux ambiances", 37)
f.byline("Par la rédaction · Niveau de lecture : A2 → B1")
f.para("Samedi 31 octobre, les enfants français se sont déguisés : sorcières, fantômes, super-héros. Ils ont frappé aux portes et crié : « Des bonbons ou un sort ! » Dans les parcs, les soirées costumées ont attiré les familles, et les citrouilles orange étaient partout.")
f.para("Le lendemain, dimanche 1er novembre, l'ambiance a changé : c'était la Toussaint, le jour des fleurs. Les cimetières se sont remplis de chrysanthèmes — blancs, jaunes, violets. Les familles ont posé les fleurs sur les tombes, nettoyé les pierres, et sont restées un moment en silence.")
f.para("Deux jours, deux visages de l'automne : le rire d'abord, le souvenir ensuite. En France, le chrysanthème reste la fleur des cimetières : on n'offre jamais de chrysanthèmes pour un anniversaire. Pour faire plaisir, on choisit des roses ou des tulipes.")
f.para("Et lundi 2 novembre ? C'est le jour des morts : un jour de souvenir en famille, plus discret que la Toussaint, souvent confondu avec elle. La Toussaint honore tous les saints ; le 2 novembre, on pense à ses propres morts. Deux jours voisins, deux sens différents.")
f.gloss("se déguiser sich verkleiden · un sort Zauber, Streich · une ambiance Stimmung · le souvenir Erinnerung, Gedenken · confondre verwechseln · discret dezent, leise.")
f.head("À VOUS ! · SIE SIND DRAN", 25)
f.bridge("Richtig oder falsch? (Vrai / Faux)")
f.ex("A2", "Richtig/Falsch", "Vrai", "Halloween war am Samstag, 31. Oktober",
     "Halloween a eu lieu samedi 31 octobre.", instr="Vrai ou faux ?")
f.ex("A2", "Richtig/Falsch", "Vrai", "An Toussaint sind die Friedhöfe voller Chrysanthemen",
     "Le 1er novembre, les cimetières sont pleins de chrysanthèmes.", instr="Vrai ou faux ?")
f.ex("A2", "Richtig/Falsch", "Faux", "Chrysanthemen schenkt man nie",
     "On offre des chrysanthèmes pour un anniversaire.", instr="Vrai ou faux ?")
f.ex("B1", "Richtig/Falsch", "Faux", "2. November ist jour des morts, nicht Toussaint",
     "Le 2 novembre, c'est la Toussaint.", instr="Vrai ou faux ?")
f.ex("B1", "Richtig/Falsch", "Vrai", "Im Text: le rire d'abord, le souvenir ensuite",
     "Halloween, c'est le rire ; la Toussaint, c'est le souvenir.", instr="Vrai ou faux ?")
f.bridge("Ergänzen Sie mit déguisement / tombe / citrouille / souvenir.")
f.ex("B1", "Satzergänzung", "déguisement", "An Halloween tragen Kinder Kostüme",
     "Pour Halloween, les enfants portent un ___.")
f.ex("A2", "Satzergänzung", "tombe", "Blumen stehen auf dem Grab",
     "On pose les fleurs sur la ___.")
f.ex("A2", "Satzergänzung", "citrouille", "Der Kürbis ist das Symbol von Halloween",
     "Une ___ orange est le symbole d'Halloween.")
f.ex("B1", "Satzergänzung", "souvenir", "Toussaint ist ein Gedenktag",
     "La Toussaint est le jour du ___.")
f.bridge("Schreiben Sie die Sätze um (mit ne...jamais / ne...plus / ne...pas).")
f.ex("B1", "Umformung", "On n'offre jamais de chrysanthèmes pour un anniversaire.", "jamais + de (ohne Artikeländerung)",
     "(jamais) On offre des chrysanthèmes pour un anniversaire. → ___", instr="Umformen")
f.ex("B1", "Umformung", "Les feuilles ne sont plus vertes en novembre.", "ne...plus = nicht mehr",
     "(plus) Les feuilles sont vertes en novembre. → ___", instr="Umformen")
f.ex("B1", "Umformung", "Le 2 novembre n'est pas la Toussaint.", "n'est pas = ist nicht",
     "(pas) Le 2 novembre est la Toussaint. → ___", instr="Umformen")
f.head("PEUR SUR LE PARC", 25)
f.para("Au parc Astérix, à Plailly, la fête d'Halloween s'appelle « Peur sur le Parc ». Elle a commencé le 3 octobre et se termine dimanche 8 novembre. Cette année, les nouveautés s'appellent « La Forêt sans Retour » et « Le Parcours des Petits Chaudrons ».", 23.5)
f.para("Le parc distingue les journées en famille et les nuits qui font peur, avec une échelle de peur par couleurs. Pour les enfants sensibles, il existe même un badge gratuit « repousse-monstres ». La dernière soirée nocturne, samedi 7 novembre de 19 heures à 1 heure du matin, demande un billet spécial.", 23.5)
f.bridge("Kurz üben · Fragen zu Halloween im Park.")
f.ex("A2", "Satzergänzung", "nocturne", "Samstag, 7.: letzte Nachtveranstaltung",
     "Samedi 7 novembre, c'est la dernière ___ du parc.")
f.ex("B1", "Satzergänzung", "badge", "Empfindsame Kinder erhalten ein kostenloses Monster-Abzeichen",
     "Les enfants sensibles reçoivent un ___ gratuit.")
f.ex("A2", "Satzergänzung", "Plailly", "Der Parc Astérix liegt in Plailly",
     "Le parc Astérix se trouve à ___.")
f.ex("B1", "Multiple Choice", "B", "Peur sur le Parc vom 3. Oktober bis 8. November",
     "Peur sur le Parc se termine... A. le 31 octobre · B. le 8 novembre · C. le 1er novembre")
f.ex("B1", "Satzergänzung", "couleurs", "Die Angststufen unterscheiden sich nach Farben",
     "L'échelle de peur utilise des ___.")
f.ex("A2", "Satzergänzung", "19 heures", "Die Nachtveranstaltung dauert von 19 bis 1 Uhr",
     "La nocturne commence à ___ .")
f.end_report()

ix = COLX[3]
image(p, "chrysanthemum-blanco.jpg", ix, 200, CW, 540)
cy3 = caption(p, ix, 740, CW,
              "Le chrysanthème, fleur du souvenir en France : on le pose sur les tombes, on ne l'offre jamais en cadeau.",
              "Planche botanique, Flora de Filipinas (Blanco), XIXe siècle, domaine public")
by3 = cy3 + 22
p.rect(ix, by3, CW, 452, fill=BOX, stroke=LINE, sw=1.4)
p.text(ix + 22, by3 + 40, "LES MOTS DES FÊTES · WÖRTER", 23, "sans", True, OLIVE)
mots = [
    "un saint — Heiliger", "un cimetière — Friedhof", "une tombe — Grab",
    "un jour férié — Feiertag", "se souvenir — sich erinnern, gedenken",
    "un déguisement — Kostüm", "une citrouille — Kürbis",
    "un bonbon — Bonbon", "un fantôme — Gespenst", "un sort — Zauber, Fluch",
]
yy3 = by3 + 82
for m in mots:
    p.text(ix + 22, yy3, m, 21.5, "serif", False, INK)
    yy3 += 37
zy3 = by3 + 452 + 26
p.rect(ix, zy3, CW, 476, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(ix + 22, zy3 + 40, "ZOOM · LE PARC EN CHIFFRES", 23, "sans", True, OLIVE)
p.para(ix + 22, zy3 + 78, "Du 3 octobre au 8 novembre : 12 soirées nocturnes, dont la dernière samedi 7 novembre. Le jour, le parc ouvre de 10 heures à 19 heures. Deux nouveautés 2026 : « La Forêt sans Retour » et « Le Parcours des Petits Chaudrons ».", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, zy3 + 340, "Vom 3. Oktober bis 8. November: 12 Nachtveranstaltungen, die letzte am Samstag, 7. November. Tagsüber geöffnet von 10 bis 19 Uhr.", 20, "sans", False, GREY, CW - 44, 1.4)
dy3 = zy3 + 476 + 26
p.rect(ix, dy3, CW, 330, fill=BOX, stroke=LINE, sw=1.4)
p.text(ix + 22, dy3 + 40, "DATES À RETENIR · TERMINE", 23, "sans", True, OLIVE)
dates3 = [
    ("lun. 2 nov.", "rentrée + jour des morts"),
    ("sam. 7 nov.", "dernière nocturne à Plailly"),
    ("dim. 8 nov.", "finales + fermeture du parc"),
    ("sam. 14 nov.", "foire de Dieppe (à venir)"),
]
yy3 = dy3 + 84
for d, t in dates3:
    p.text(ix + 22, yy3, d, 19.5, "sans", True, BRICK)
    p.text(ix + 168, yy3, t, 18.5, "serif", False, INK)
    yy3 += 42
p.para(ix + 22, yy3 + 20, "Achtung: Dieppe erst am 14.–15. November, nicht diese Woche.", 19.5, "sans", False, GREY, CW - 44, 1.4)
py3 = dy3 + 330 + 30
p.text(ix, py3 + 24, "POUR OU CONTRE ?", 23, "sans", True, OLIVE)
p.hline(ix, ix + CW, py3 + 38, GOLD, 2)
p.para(ix, py3 + 74, "Halloween au parc : fête joyeuse ou trop effrayante ? Écrivez votre avis en deux phrases pour le courrier des lecteurs (page 7).", 20.5, "serif", False, INK, CW, 1.4)
p.foot(3)
p.save(f"{OUT}/p3-culture.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · 体育 (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT", "Le Lucerna", "NIVEAU B1 · Tennis · Masters de Paris")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2540, tag="P4-main")
f.title("Le Masters de Paris : la dernière finale de la saison", 37)
f.byline("Par la rédaction · Niveau de lecture : B1")
f.para("C'est le dernier grand tournoi de tennis de la saison : le Rolex Paris Masters, sur dur, en salle, à la Paris La Défense Arena de Nanterre. Les qualifications ont eu lieu les 31 octobre et 1er novembre ; le tableau principal se joue du lundi 2 au dimanche 8 novembre.")
f.para("Le programme est simple à retenir : quarts de finale vendredi 6 novembre, demi-finales samedi 7, finales dimanche 8 — la finale du simple, la finale du double, et la finale du simple en fauteuil, à midi. Le tenant du titre, Jannik Sinner, vainqueur en 2025, est le nom à connaître — mais pour 2026, on ne connaît pas encore les finalistes.")
f.para("Pourquoi ce tournoi compte-t-il tant ? Parce que c'est un Masters 1000, le plus haut niveau après les quatre tournois du Grand Chelem. Les meilleurs joueurs du monde s'y retrouvent, en salle, où la balle va très vite. Un match peut basculer sur deux ou trois points.")
f.para("En France, on regarde aussi les tribunes : Nanterre devient, une semaine par an, la capitale du tennis. Les enfants des clubs viennent voir leurs héros de près, raquette à la main, et repartent avec des phrases de commentateurs dans la tête.")
f.para("Et après le tennis ? Le football continue : la 10e journée de Ligue 1 se joue du vendredi 6 au dimanche 8 novembre. Le grand match du week-end, c'est Lens – Marseille, dimanche 8. Au Parc des Princes, samedi 7, le Paris SG reçoit Troyes.")
f.gloss("un tournoi Turnier, Wettkampf · sur dur auf Hartplatz · en salle in der Halle · un tableau principal Hauptfeld · le tenant du titre Titelverteidiger · basculer kippen, sich wenden · les tribunes Tribünen.")
f.head("À VOUS ! · SIE SIND DRAN", 25)
f.bridge("Lesen Sie den Artikel auf Seite 4 und wählen Sie die richtige Antwort.")
f.ex("B1", "Multiple Choice", "B", "Finale am Sonntag, 8. November",
     "Les finales du Masters ont lieu... A. samedi 7 · B. dimanche 8 · C. vendredi 6")
f.ex("B1", "Multiple Choice", "A", "Das Masters findet in der Halle auf Hartplatz statt",
     "Le Masters se joue... A. en salle, sur dur · B. sur terre battue · C. sur herbe")
f.ex("B1", "Multiple Choice", "C", "Titelverteidiger 2025 ist Sinner",
     "Le tenant du titre 2025, c'est... A. Novak Djokovic · B. Carlos Alcaraz · C. Jannik Sinner")
f.ex("B1", "Multiple Choice", "B", "Topspiel der 10. Ligue-1-Runde: Lens – Marseille",
     "Le grand match du week-end, c'est... A. Paris SG – Troyes · B. Lens – Marseille · C. Rennes – Lille")
f.ex("B1", "Multiple Choice", "A", "Sonntag, 8.: auch Rollstuhl-Einzelfinale (mittags)",
     "Dimanche 8, on joue aussi... A. la finale fauteuil · B. les qualifications · C. un match amical")
f.bridge("Ordnen Sie die Tenniswörter ihren Bedeutungen zu.")
f.match_set("B1", "Zuordnung",
            ["un tournoi", "une raquette", "les tribunes", "un tenant du titre"],
            ["la compétition avec plusieurs matchs", "l'instrument pour frapper la balle",
             "les places des spectateurs", "le vainqueur de l'année dernière"],
            ["a", "b", "c", "d"],
            ["tournoi=Wettkampf a", "raquette=Schläger b", "tribunes=Tribünen c", "tenant=Titelverteidiger d"],
            instr="Zuordnen")
f.bridge("Ergänzen Sie mit dem Komparativ (plus / moins).")
f.ex("B1", "Satzergänzung", "plus vite", "In der Halle ist der Ball schneller",
     "En salle, la balle va ___ (vite) qu'en plein air.")
f.ex("B1", "Satzergänzung", "plus grand", "Ein Masters 1000 ist die Stufe unter den Grand Slams",
     "Un Masters 1000 est ___ (grand) qu'un petit tournoi.")
f.ex("B1", "Satzergänzung", "moins longue", "Die Hallensaison ist kürzer als die Sommersaison",
     "La saison en salle est ___ (longue) que la saison d'été. (moins)")
f.head("LE FOOTBALL DU WEEK-END", 25)
f.para("La 10e journée de Ligue 1 commence vendredi 6 novembre avec Toulouse – Strasbourg. Samedi 7, Auxerre reçoit le Paris FC, et le Paris SG reçoit Troyes au Parc des Princes. Dimanche 8, six matchs : Rennes – Lille, Le Mans – Monaco, Le Havre – Lorient, Brest – Lyon, Angers – Nice — dont le choc Lens – Marseille.", 23.5)
f.para("Pour les lecteurs de français, un match de football est une leçon gratuite : les commentateurs répètent les mêmes phrases — « il frappe ! », « c'est le but ! », « quelle ambiance ! » — et les noms des villes deviennent familiers.", 23.5)
f.bridge("HINWEIS · un choc Topspiel, Spitzenduell · recevoir empfangen, antreten gegen · familier vertraut.")
f.head("REGARDER UN MATCH", 25)
f.para("Quelques phrases suffisent pour suivre un match avec les commentaires français. Les commentateurs parlent vite, mais ils répètent souvent les mêmes expressions : écoutez, répétez, criez avec eux !", 23.5)
f.box("LES PHRASES DU COMMENTATEUR", [
    ("« Allez ! » — Auf geht's! · « Quelle action ! » — Was für eine Aktion!", "serif", False, INK, 21.5, 1.42),
    ("« Il marque ! » — Er trifft! · « C'est gagné ! » — Gewonnen!", "serif", False, INK, 21.5, 1.42),
    ("« Quel point ! » — Was für ein Punkt! (Tennis) · « Balle de match ! » — Matchball!", "serif", False, INK, 21.5, 1.42),
])
f.end_report()

ix = COLX[3]
p.rect(ix, 200, CW, 470, fill=BOX, stroke=LINE, sw=1.4)
p.text(ix + 22, 240, "LE MASTERS EN CHIFFRES", 23, "sans", True, OLIVE)
p.para(ix + 22, 278, "41e édition en 2026 (40e anniversaire). Dernier Masters 1000 de la saison. En salle, sur dur, à Nanterre. Qualifications les 31 octobre et 1er novembre ; tableau principal du 2 au 8 novembre ; finales dimanche 8.", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, 520, "Le tournoi en fauteuil se joue du 6 au 8 novembre, avec sa finale simple dimanche à midi.", 21.5, "serif", False, INK, CW - 44, 1.42)
vy = 696
p.rect(ix, vy, CW, 416, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(ix + 22, vy + 40, "LES MOTS DU TENNIS · WÖRTER", 23, "sans", True, OLIVE)
mots4 = [
    "le tennis — Tennis", "une balle — Ball", "un set — Satz",
    "un match — Spiel", "un point — Punkt", "la finale — Finale",
    "un adversaire — Gegner", "un titre — Titel",
]
yy4 = vy + 82
for m in mots4:
    p.text(ix + 22, yy4, m, 21.5, "serif", False, INK)
    yy4 += 37
sy4 = vy + 416 + 26
p.rect(ix, sy4, CW, 218, fill=BOX, stroke=LINE, sw=1.4)
p.text(ix + 22, sy4 + 40, "À SUIVRE · FORTSETZUNG", 23, "sans", True, OLIVE)
p.para(ix + 22, sy4 + 80, "Les finalistes seront connus samedi soir, après les demi-finales. Les résultats du week-end seront dans le VOL.4.", 21.5, "serif", False, INK, CW - 44, 1.42)
mf = Flow(p, [(ix, CW)], sy4 + 218 + 30, 2540, tag="P4-micro")
mf.head("MICRO-DRILLS · ÜBUNGEN", 24)
mf.bridge("Ergänzen Sie mit finale / quarts / demi-finales / tableau / fauteuil / choc.")
mf.ex("B1", "Satzergänzung", "quarts", "Viertelfinals am Freitag",
      "Les ___ de finale ont lieu vendredi 6.", size=23)
mf.ex("B1", "Satzergänzung", "demi-finales", "Halbfinals am Samstag",
      "Les ___ ont lieu samedi 7.", size=23)
mf.ex("B1", "Satzergänzung", "finale", "Einzelfinale am Sonntag",
      "La ___ du simple a lieu dimanche 8.", size=23)
mf.ex("B1", "Satzergänzung", "tableau", "Das Hauptfeld beginnt am Montag",
      "Le ___ principal commence lundi 2.", size=23)
mf.ex("B1", "Satzergänzung", "fauteuil", "Rollstuhlturnier von Freitag bis Sonntag",
      "Le tournoi en ___ se joue du 6 au 8.", size=23)
mf.ex("A2", "Satzergänzung", "choc", "Lens – Marseille ist das Topspiel des Wochenendes",
      "Lens – Marseille, c'est le ___ du week-end.", size=23)
mf.end_report()
db4 = mf.y + 6
p.rect(ix, db4, CW, 2540 - db4, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(ix + 22, db4 + 40, "LE DÉBAT · DISKUSSION", 23, "sans", True, OLIVE)
p.para(ix + 22, db4 + 78, "Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ? Discutez en classe : deux phrases pour, deux phrases contre.", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, db4 + 196, "Finalisten vorab unbekannt: spannender oder frustrierender? Schreiben Sie je zwei Sätze dafür und dagegen.", 20, "sans", False, GREY, CW - 44, 1.4)
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
