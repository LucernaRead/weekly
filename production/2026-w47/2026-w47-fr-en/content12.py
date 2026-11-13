# -*- coding: utf-8 -*-
"""W47 FR core VOL.4 — P1 + P2. Issue week Mon 16 – Sun 22 Nov 2026.
French core text is frozen here; every reader-language string comes
from expl.py (E). Press time: 10 Nov 2026 — results not yet produced
(Senate vote 18 Nov, Beaujolais 19 Nov, Turin finals 22 Nov, Bleus
12/15 Nov) are stated as planned ("prévu")."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 =================
CURPAGE[0] = 1
p = BSPage4()

p.text(MX, 92, E["vol_line"], 17, "sans", True, OLIVE, spacing=1.7)
p.text(975, 92, E["strapline_mid"], 17, "sans", False, GREY, anchor="middle", spacing=1.7)
p.text(RIGHT, 92, "SEMAINE DU 16 AU 22 NOVEMBRE 2026", 17, "sans", False, GREY, anchor="end", spacing=1.7)
p.text(975, 262, "Le Lucerna", 196, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, E["subtitle"], 36, "serif", True, OLIVE, anchor="middle", spacing=11.5)
p.text(975, 372, "LE JOURNAL DES APPRENANTS DE FRANÇAIS — LIRE LA VRAIE VIE, EN FRANÇAIS", 16, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)

p.rect(MX, 470, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 30, 524, "ALCARAZ GAGNE PARIS, LE SÉNAT VOTE MERCREDI", 46, "sans", True, ONCLOTH)
p.text(MX + 30, 568, "Turin commence dimanche. Jeudi, le beaujolais nouveau arrive.", 25, "serif", False, "#cac8ba")
p.text(RIGHT - 30, 524, E["band_r1"], 27, "sans", True, GOOSE, anchor="end")
p.text(RIGHT - 30, 568, E["band_r2"], 18, "sans", False, GOOSE, anchor="end")

p.text(975, 612, E["badge"], 16, "sans", False, GREY, anchor="middle")

hy = 610
p.text(MX, hy + 26, E["kicker"], 17, "sans", True, OLIVE)
hy = p.para(MX, hy + 92, "Alcaraz, roi de Paris : le Sénat tranche mercredi", 53, "serif", True, INK, 1323, 1.06)
p.text(MX, hy + 28, "Par la rédaction du Lucerna　Niveau de lecture : A2", 17, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1812, tag="P1-headline")
f.para("Dimanche 8 novembre, Carlos Alcaraz a battu Ben Shelton 7-6(5), 7-5, en finale du Rolex Paris Masters, à Nanterre. Le vainqueur remporte son premier titre à Paris, le neuvième en Masters 1000. L'Espagnol, tête de série n° 2, a battu l'Américain, tête de série n° 3.")
f.para("Mercredi 18 novembre, c'est le Sénat qui tranche : le vote solennel sur le budget de la Sécurité sociale est prévu ce jour-là. Le texte est débattu depuis lundi 9 novembre ; plus de 1 200 amendements ont été déposés. Le gouvernement veut ramener le déficit de 21,8 à 12,7 milliards d'euros.")
f.para("Jeudi 19 novembre, à 0 heure, le beaujolais nouveau arrive : c'est le troisième jeudi de novembre, comme chaque année depuis 1985. Le vin primeur, fait avec le cépage gamay, sort dans toute la France.")
f.para("Et le week-end, c'est le sport qui prend le relais : dimanche 15 novembre, les Masters de Turin ont commencé — les demi-finales samedi 21, les finales dimanche 22. Les Bleus, eux, jouent jeudi 12 en Italie, puis dimanche 15 à Bordeaux, contre la Turquie.")
f.para("Trois rendez-vous, une seule semaine : le Sénat pour le débat, le beaujolais pour la fête, Turin pour le sport. Une semaine en trois temps : voter, fêter, jouer. Suite en pages 4 et 6.")
f.gloss(E["g1"])
f.box(E["dates_box_title"], [
    ("lun. 16 nov. — Turin continue, le Sénat débat", "serif", False, INK, 21.5, 1.4),
    ("mer. 18 nov. — le Sénat vote, le cinéma sort", "serif", False, INK, 21.5, 1.4),
    ("jeu. 19 nov. — le beaujolais nouveau arrive", "serif", False, INK, 21.5, 1.4),
])
f.head(E["head_avous"], 25)
f.ex("A2", "完成句子", "gagné", E["n_senat9"],
     "Dimanche 8 novembre, Alcaraz a ___ le Masters de Paris.", size=21.5)
f.ex("A2", "完成句子", "mercredi", E["n_mercredi11"],
     "C'est ___ que le Sénat vote, le 18 novembre.", size=21.5)
f.ex("A2", "完成句子", "jeudi", E["n_harengs"],
     "C'est ___ que le beaujolais nouveau arrive, le 19 novembre.", size=21.5)
f.ex("B1", "完成句子", "premier", E["n_115"],
     "C'est son ___ titre à Paris.", size=21.5)
f.ex("B1", "完成句子", "12,7", E["n_flamme"],
     "Le déficit de la Sécu doit passer de 21,8 à ___ milliards.", size=21.5)
f.ex("B1", "完成句子", "22", E["n_dieppe"],
     "Les finales de Turin ont lieu dimanche ___ novembre.", size=21.5)
f.end_report()

gx, gw = COLX[3], CW
gy = 588
p.rect(gx, gy, gw, 668, fill=BOX)
p.text(gx + 22, gy + 40, "CETTE SEMAINE", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "JOUR PAR JOUR", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, E["agenda_sub"], 19, "sans", False, GREY)
agenda = [
    ("lun. 16", "Turin : suite　Sénat"),
    ("mar. 17", "Sénat : suite des articles"),
    ("mer. 18", "Sénat : vote　cinéma"),
    ("jeu. 19", "Beaujolais nouveau"),
    ("ven. 20", "Journée de l'enfance"),
    ("sam. 21", "Turin : demies　SERD"),
    ("dim. 22", "Turin : finales　Ligue 1"),
]
byy = gy + 150
for d, t in agenda:
    p.text(gx + 22, byy + 22, d, 21, "sans", True, OLIVE)
    p.text(gx + 118, byy + 22, t, 20, "serif", False, INK)
    byy += 62
p.text(gx + 22, byy + 16, "Le vote solennel du Sénat", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "aura lieu mercredi 18 novembre.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 76, E["agenda_note"], 19, "sans", False, GREY)

sy = 1280
p.rect(gx, sy, gw, 372, fill="#f0eee5")
p.text(gx + 22, sy + 40, E["sommaire_title"], 21, "sans", True, OLIVE)
som = [
    ("p.2", "La semaine en trois temps", "A2"),
    ("p.3", "Le beaujolais a 75 ans", "A2→B1"),
    ("p.4", "Alcaraz, Turin et les Bleus", "B1"),
    ("p.5", "Cinéma et seconde main", "B1"),
    ("p.6", "Le budget au Sénat", "B2"),
    ("p.7", "Les phrases de la semaine", "A2→B2"),
    ("p.8", "Exercices et réponses", "tous"),
]
yy = sy + 84
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, OLIVE)
    p.text(gx + 72, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 40

my = 1652
p.text(gx, my + 24, "LE MOT DE LA SEMAINE", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, OLIVE, 2)
p.text(gx, my + 76, "« trancher »", 21.5, "serif", False, INK, italic=True)
wy = p.para(gx, my + 108, "décider, couper court : le Sénat tranche, le juge tranche.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, wy + 10, E["mot_gloss"], 19, "sans", False, GREY, gw, 1.35)

p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "atget-paris.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "Paris, un matin de novembre : la ville vote, fête le vin nouveau, et regarde Turin.",
        "Eugène Atget (1857-1927), photographie, domaine public")
f2 = Flow(p, [(COLX[2], CW)], 1874, 2300, tag="P1-budget")
f2.head(E["head_budget3"], 25)
f2.para("Le 4 novembre, l'Assemblée nationale a rejeté les recettes du budget de l'État, par 458 voix contre 0. Tout le texte est tombé en première lecture.", 21)
f2.para("Mercredi 18 novembre, le Sénat vote sur le budget de la Sécu. À partir du 20 novembre, il examine le budget de l'État ; le vote est prévu le 9 décembre.", 21)
f2.end_report()
bx = COLX[3]
p.rect(bx, 1874, CW, 424, fill=BOX)
p.text(bx + 22, 1914, E["head_enbref"], 24, "sans", True, OLIVE)
brefs = [
    ("MASTERS", "Alcaraz bat Shelton 7-6(5), 7-5 : premier titre à Paris, neuvième en Masters 1000."),
    ("BUDGET", "Le vote du 3 novembre n'a pas eu lieu : reporté au 4, rejet 458–0. (page 6)"),
    ("BEAUJOLAIS", "Mise en vente jeudi 19 novembre, à 0 heure. Les Sarmentelles ouvrent dès mercredi soir. (page 3)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, OLIVE)
    byy = p.para(bx + 22, byy + 48, b, 19.5, "serif", False, INK, CW - 44, 1.36) + 6

qy = 2312
p.hline(MX, RIGHT, qy, OLIVE, 2)
p.text(MX, qy + 36, E["head_quiz"], 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, E["quiz_sub"], 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2560, tag="P1-quiz")
qf.ex("A2", "单选", "A", E["n_q1"],
      "Alcaraz a gagné Paris... A. dimanche 8　B. samedi 7　C. lundi 9", size=21)
qf.ex("A2", "单选", "B", E["n_q2"],
      "Le Sénat vote sur la Sécu... A. lundi 16　B. mercredi 18　C. jeudi 19", size=21)
qf.ex("A2", "单选", "A", E["n_q3"],
      "Le beaujolais nouveau arrive... A. jeudi 19　B. vendredi 20　C. samedi 21", size=21)
qf.ex("A2", "单选", "B", E["n_q4"],
      "Les finales de Turin, c'est... A. samedi 21　B. dimanche 22　C. lundi 23", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-une.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 =================
CURPAGE[0] = 2
p = BSPage4()
p.band(E["band_p2"], "Le Lucerna", E["band_p2_sub"])

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("Lundi 16 novembre : une semaine en trois temps", 32)
f.byline("Par la rédaction　Niveau de lecture : A2")
f.para("Lundi 16 novembre, la semaine commence à Turin et au Sénat : à Turin, les matches de groupe continuent ; au Sénat, les sénateurs discutent toujours du budget de la Sécurité sociale. Deux débats, deux scènes — et une semaine qui commence fort.")
f.para("Mercredi 18 novembre, tout s'accélère : le Sénat vote sur le budget de la Sécu, et le cinéma sort seize nouveaux films. C'est le mercredi des sorties en France : un jour pour voter le matin, un film le soir.")
f.para("Jeudi 19 novembre, à 0 heure, le beaujolais nouveau arrive. Dans les bars et les caves, on lève le verre : « Le beaujolais nouveau est arrivé ! » Le vin primeur, léger et fruité, se boit jeune — et avec modération, toujours.")
f.para("Vendredi 20 novembre, c'est la Journée mondiale de l'enfance : dans les écoles, on parle des droits de l'enfant. Un jour pour écouter les plus jeunes, et pour leur laisser la parole.")
f.para("Samedi 21 novembre, la Semaine européenne de la réduction des déchets commence : jusqu'au 29 novembre, partout en France, on répare, on échange, on achète d'occasion. Le même jour, à Turin, ce sont les demi-finales.")
f.para("Et dimanche 22 novembre, la semaine se termine en beauté : les finales de Turin, et le retour de la Ligue 1 — Marseille reçoit Le Mans à 20 h 45. Une semaine en trois temps : voter, fêter, jouer.")
f.para("Que lire quand la semaine est en trois temps ? Le journal, d'abord : un vote, une fête, une finale — trois histoires, trois mots nouveaux par jour. Regarder, voter, fêter : la semaine se lit comme une phrase en trois temps.")
f.gloss(E["g2"])
f.head("LA SEMAINE EN CHIFFRES", 25)
f.para("Trois rendez-vous, une seule semaine : voter mercredi, fêter jeudi, jouer dimanche. Le mercredi 18 novembre tombe en plein milieu — ni début, ni fin, comme une virgule dans la semaine.", 23.5)
f.para("Depuis 1985, le beaujolais nouveau sort le troisième jeudi de novembre. Cette année, la fête a 75 ans — et le vin, lui, n'a que quelques semaines.", 23.5)
f.bridge(E["bridge_valise"])
f.end_report()

ix = COLX[3]
image(p, "chatillon-beaujolais.jpg", ix, 200, CW, 300)
cy3 = caption(p, ix, 500, CW, "Châtillon, dans le Beaujolais : le château au-dessus du village, au cœur du vignoble.",
              "Photographie, domaine public　Wikimedia Commons")
sav = ["Le beaujolais nouveau sort le 3e jeudi de novembre, depuis 1985.",
       "Le gamay est le cépage du Beaujolais.",
       "La Journée de l'enfance, c'est le 20 novembre."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in sav) + 50
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "LE SAVIEZ-VOUS ?", 24, "sans", True, OLIVE)
yy3 += 52
for t in sav:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "Et vous ? Racontez votre jeudi 19 novembre en deux phrases : une sortie, un film, ou une dégustation (pour les adultes) ? Les meilleurs textes paraîtront dans le VOL.5 (page 7)."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(E["etvous_note"], "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, E["head_etvous"], 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, E["etvous_note"], 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

dy = 1570
p.hline(MX, RIGHT, dy - 12, OLIVE, 2)
p.text(MX, dy + 28, E["head_date"], 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, E["date_sub"], 20, "sans", False, GREY, anchor="end")
lx = MX
ly = dy + 66
for line in [
    ("lundi 16 novembre", E["date_16"]),
    ("mardi 17 novembre", E["date_17"]),
    ("mercredi 18 novembre", E["date_18"]),
    ("jeudi 19 novembre", E["date_19"]),
    ("vendredi 20 novembre", E["date_20"]),
    ("samedi 21 novembre", E["date_21"]),
    ("dimanche 22 novembre", E["date_22"]),
]:
    p.text(lx, ly + 24, line[0], 24, "serif", True, OLIVE)
    p.text(lx + 330, ly + 24, line[1], 21, "sans", False, GREY)
    ly += 34
p.para(lx, ly + 24, "Exemples : Le mercredi 18 novembre, le Sénat vote.　Jeudi 19 novembre, le beaujolais nouveau arrive.　Dimanche 22 novembre, ce sont les finales de Turin.", 20.5, "serif", False, INK, RIGHT - lx, 1.42)

ey = dy + 356
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, E["head_p2ex"], 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, E["p2ex_sub"], 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P2-ex")
e.head("A　QUELLE DATE ?", 25)
e.bridge(E["bridge_dates"])
e.ex("A2", "完成句子", "mercredi", E["n_mercredi11"],
     "Le Sénat vote ___ 18 novembre.", instr=E["instr_fill"], size=23)
e.ex("A2", "完成句子", "lundi", E["n_lundi9"],
     "La semaine commence ___ 16 novembre.", instr=E["instr_fill"], size=23)
e.ex("A2", "完成句子", "jeudi", E["n_jeudi12"],
     "Le beaujolais nouveau arrive ___ 19 novembre.", instr=E["instr_fill"], size=23)
e.ex("A2", "完成句子", "dimanche", E["n_dimanche15"],
     "Les finales de Turin, c'est ___ 22 novembre.", instr=E["instr_fill"], size=23)
e.head("B　LE FUTUR PROCHE", 25)
e.bridge(E["bridge_futur"])
e.ex("A2", "句型转换", "Le Sénat va voter mercredi.", E["n_futur1"],
     "Mercredi, le Sénat (voter). → ___", instr=E["instr_rewrite"], size=21.5)
e.ex("A2", "句型转换", "Nous allons goûter le beaujolais jeudi.", E["n_futur2"],
     "Jeudi, nous (goûter) le beaujolais. → ___", instr=E["instr_rewrite"], size=21.5)
e.ex("A2", "句型转换", "Tu vas raconter ton jeudi 19 novembre.", E["n_futur3"],
     "Tu (raconter) ton jeudi 19 novembre. → ___", instr=E["instr_rewrite"], size=21.5)
e.ex("B1", "句型转换", "Vous allez regarder les finales dimanche.", E["n_futur4"],
     "Dimanche, vous (regarder) les finales → ___", instr=E["instr_rewrite"], size=21.5)
e.head("C　COMPRÉHENSION", 25)
e.bridge(E["bridge_read2"])
e.ex("A2", "单选", "C", E["n_comp1"],
     "La Journée de l'enfance, c'est le... A. 18 nov.　B. 19 nov.　C. 20 nov.", size=22)
e.ex("A2", "单选", "B", E["n_comp2"],
     "La Semaine de la réduction des déchets commence... A. le 19 nov.　B. le 21 nov.　C. le 29 nov.", size=22)
e.ex("A2", "单选", "A", E["n_comp3"],
     "Les finales de Turin, c'est... A. dimanche 22　B. samedi 21　C. lundi 23", size=22)
e.head("D　LES MOTS", 25)
e.match_set("A2", "词汇配对",
            ["un vote", "un vin primeur", "un déchet", "une finale"],
            ["la décision ensemble", "un vin de l'année, très jeune",
             "ce qu'on jette", "le dernier match d'un tournoi"],
            ["a", "b", "c", "d"],
            [E["m_vote2"], E["m_primeur2"], E["m_dechet2"], E["m_finale2"]],
            instr=E["instr_match"])
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-vie.svg")
print("P2 saved, exercises so far:", len(REG))
