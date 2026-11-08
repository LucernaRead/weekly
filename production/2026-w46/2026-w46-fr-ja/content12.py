# -*- coding: utf-8 -*-
"""W46 FR core VOL.4 — P1 + P2. Issue week Mon 9 – Sun 15 Nov 2026.
French core text is frozen here; every reader-language string comes
from expl.py (E). Press time: 2 Nov 2026 — results not yet produced
(Masters finals 8 Nov, budget vote 3 Nov) are stated as unknown."""
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
p.text(RIGHT, 92, "SEMAINE DU 9 AU 15 NOVEMBRE 2026", 17, "sans", False, GREY, anchor="end", spacing=1.7)
p.text(975, 262, "Le Lucerna", 196, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, E["subtitle"], 36, "serif", True, OLIVE, anchor="middle", spacing=11.5)
p.text(975, 372, "LE JOURNAL DES APPRENANTS DE FRANÇAIS — LIRE LA VRAIE VIE, EN FRANÇAIS", 16, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)

p.rect(MX, 470, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 30, 524, "LUNDI 9 NOVEMBRE : LE SÉNAT PREND LE RELAIS !", 46, "sans", True, ONCLOTH)
p.text(MX + 30, 568, "Le budget de la Sécurité sociale arrive au Sénat. Mercredi, le pays se souvient.", 25, "serif", False, "#cac8ba")
p.text(RIGHT - 30, 524, E["band_r1"], 27, "sans", True, GOOSE, anchor="end")
p.text(RIGHT - 30, 568, E["band_r2"], 18, "sans", False, GOOSE, anchor="end")

p.text(975, 612, E["badge"], 16, "sans", False, GREY, anchor="middle")

hy = 610
p.text(MX, hy + 26, E["kicker"], 17, "sans", True, OLIVE)
hy = p.para(MX, hy + 92, "Le Sénat débat, la France se souvient, Dieppe fait la fête", 53, "serif", True, INK, 1323, 1.06)
p.text(MX, hy + 28, "Par la rédaction du Lucerna　Niveau de lecture : A2", 17, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1812, tag="P1-headline")
f.para("Lundi 9 novembre, le Sénat ouvre la discussion sur le budget de la Sécurité sociale pour 2027. Le texte arrive dans la version du gouvernement : le 23 octobre, les députés avaient rejeté la partie « recettes » par 115 voix contre 1, et la partie « dépenses » n'avait pas été examinée.")
f.para("Mercredi 11 novembre, la France s'arrête : c'est le jour de l'Armistice, jour férié. Dans chaque commune, une cérémonie a lieu devant le monument aux morts ; à Paris, le président ravive la flamme du Soldat inconnu, sous l'Arc de Triomphe.")
f.para("Samedi 14 et dimanche 15 novembre, Dieppe fête la mer : la 56e Foire aux harengs et à la coquille Saint-Jacques. Sur les quais, les grills fument devant les restaurants, et la Confrérie du hareng défile en costume.")
f.para("Entre les deux, la semaine continue : jeudi 12, les Bleus jouent en Italie et Paris Photo ouvre ; dimanche 15, la France reçoit la Turquie, et les Masters de Turin commencent. Une semaine en trois temps : débattre, se souvenir, fêter.")
f.para("Trois rendez-vous, une seule semaine : le Sénat pour le débat, le 11 novembre pour la mémoire, Dieppe pour les saveurs. Suite en pages 3 et 6.")
f.gloss(E["g1"])
f.box(E["dates_box_title"], [
    ("lun. 9 nov. — le Sénat ouvre la discussion", "serif", False, INK, 21.5, 1.4),
    ("mer. 11 nov. — l'Armistice, jour férié", "serif", False, INK, 21.5, 1.4),
    ("sam. 14 – dim. 15 nov. — la foire de Dieppe", "serif", False, INK, 21.5, 1.4),
])
f.head(E["head_avous"], 25)
f.ex("A2", "完成句子", "Sénat", E["n_senat9"],
     "Lundi 9 novembre, le ___ ouvre la discussion sur le budget.", size=21.5)
f.ex("A2", "完成句子", "mercredi", E["n_mercredi11"],
     "L'Armistice, c'est ___ 11 novembre.", size=21.5)
f.ex("A2", "完成句子", "harengs", E["n_harengs"],
     "À Dieppe, on fête les ___ et la coquille Saint-Jacques.", size=21.5)
f.ex("B1", "完成句子", "115", E["n_115"],
     "Le 23 octobre, les recettes ont été rejetées par ___ voix contre 1.", size=21.5)
f.ex("B1", "完成句子", "flamme", E["n_flamme"],
     "Sous l'Arc de Triomphe, on ravive la ___ du Soldat inconnu.", size=21.5)
f.ex("B1", "完成句子", "Dieppe", E["n_dieppe"],
     "La foire aux harengs a lieu à ___.", size=21.5)
f.end_report()

gx, gw = COLX[3], CW
gy = 588
p.rect(gx, gy, gw, 668, fill=BOX)
p.text(gx + 22, gy + 40, "CETTE SEMAINE", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "JOUR PAR JOUR", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, E["agenda_sub"], 19, "sans", False, GREY)
agenda = [
    ("lun. 9", "Sénat : discussion générale"),
    ("mar. 10", "Sénat : suite des articles"),
    ("mer. 11", "Armistice · jour férié"),
    ("jeu. 12", "Bleus en Italie · Paris Photo"),
    ("ven. 13", "Paris Photo · cinéma"),
    ("sam. 14", "Dieppe · jour 1"),
    ("dim. 15", "Dieppe · Bleus · Turin"),
]
byy = gy + 150
for d, t in agenda:
    p.text(gx + 22, byy + 22, d, 21, "sans", True, OLIVE)
    p.text(gx + 118, byy + 22, t, 20, "serif", False, INK)
    byy += 62
p.text(gx + 22, byy + 16, "Le vote solennel du Sénat", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "aura lieu la semaine suivante.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 76, E["agenda_note"], 19, "sans", False, GREY)

sy = 1280
p.rect(gx, sy, gw, 372, fill="#f0eee5")
p.text(gx + 22, sy + 40, E["sommaire_title"], 24, "sans", True, OLIVE)
som = [
    ("p.2", "La semaine coupée en deux", "A2"),
    ("p.3", "Armistice et foire de Dieppe", "A2→B1"),
    ("p.4", "Masters, Turin et les Bleus", "B1"),
    ("p.5", "Paris Photo et le cinéma", "B1"),
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
p.text(gx, my + 76, "« prendre le relais »", 21.5, "serif", False, INK, italic=True)
wy = p.para(gx, my + 108, "succéder à quelqu'un, continuer son travail.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, wy + 10, E["mot_gloss"], 19, "sans", False, GREY, gw, 1.35)

p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "atget-paris.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "Paris, un matin de novembre : la ville débat, se souvient, et prépare déjà le week-end de Dieppe.",
        "Eugène Atget (1857-1927), photographie, domaine public")
f2 = Flow(p, [(COLX[2], CW)], 1874, 2300, tag="P1-budget")
f2.head(E["head_budget3"], 25)
f2.para("Le 23 octobre, l'Assemblée nationale a rejeté les recettes du budget de la Sécurité sociale, par 115 voix contre 1. Le texte part au Sénat dans sa version initiale.", 21)
f2.para("Au moment où nous écrivons, le 2 novembre, le vote du mardi 3 novembre n'a pas encore eu lieu. Son résultat sera dans le VOL.5.", 21)
f2.end_report()
bx = COLX[3]
p.rect(bx, 1874, CW, 424, fill=BOX)
p.text(bx + 22, 1914, E["head_enbref"], 24, "sans", True, OLIVE)
brefs = [
    ("MASTERS", "Sinner, tenant du titre, a déclaré forfait, blessé au genou. Finales le 8 novembre : résultats dans le VOL.5."),
    ("BUDGET", "Vote solennel mardi 3 novembre sur les recettes : résultat inconnu à la mise sous presse. (page 6)"),
    ("PARIS PHOTO", "Vernissage mercredi 11 novembre, sur invitation ; ouverture jeudi 12. (page 5)"),
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
      "La discussion au Sénat commence... A. lundi 9 · B. mercredi 11 · C. samedi 14", size=21)
qf.ex("A2", "单选", "B", E["n_q2"],
      "L'Armistice, c'est... A. lundi 9 · B. mercredi 11 · C. dimanche 15", size=21)
qf.ex("A2", "单选", "C", E["n_q3"],
      "La foire de Dieppe a lieu... A. à Paris · B. à Bordeaux · C. à Dieppe", size=21)
qf.ex("A2", "单选", "A", E["n_q4"],
      "France – Turquie, dimanche 15, c'est à... A. Bordeaux · B. Milan · C. Turin", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-une.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 =================
CURPAGE[0] = 2
p = BSPage4()
p.band(E["band_p2"], "Le Lucerna", E["band_p2_sub"])

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("Mercredi 11 novembre : la semaine coupée en deux", 32)
f.byline("Par la rédaction　Niveau de lecture : A2")
f.para("Cette semaine est coupée en deux : lundi et mardi, on travaille et on débat ; mercredi 11 novembre, on s'arrête. C'est un jour férié au milieu de la semaine, et beaucoup de Français en profitent pour souffler, partir en famille ou visiter un musée.")
f.para("Le matin du 11 novembre, les cérémonies commencent à 11 heures, devant les monuments aux morts. On dépose une gerbe, on écoute les noms des morts pour la France, on observe une minute de silence. Le bleuet, petite fleur bleue, est le symbole de ce jour : sa couleur rappelle l'uniforme des soldats de 1914.")
f.para("L'après-midi, la vie reprend doucement : beaucoup de musées et de monuments restent ouverts ce jour férié, à Paris et ailleurs. C'est aussi le jour du vernissage de Paris Photo, au Grand Palais — mais sur invitation seulement. Le public, lui, entre jeudi 12.")
f.para("Jeudi et vendredi, la semaine repart : Paris Photo, le cinéma du mercredi, les préparatifs du week-end. Et dimanche 15, deux rendez-vous : la foire de Dieppe, qui se termine, et les Bleus, qui reçoivent la Turquie à Bordeaux. Une semaine coupée, mais une semaine pleine.")
f.para("Que lire quand la semaine est coupée en deux ? Un livre de photographies, par exemple : on regarde une image, on lit sa légende, on imagine l'histoire. Regarder une photo, c'est déjà lire — et Paris Photo en offre des centaines.")
f.para("Bon mercredi férié à tous ! Que vous alliez à une cérémonie, à un musée ou simplement en promenade, cette semaine vous donne deux lundis : le 9 et le 12 novembre.")
f.gloss(E["g2"])
f.head("LA SEMAINE EN CHIFFRES", 25)
f.para("Deux jours de travail, puis un jour férié, puis deux jours de travail, puis le week-end : la semaine du 9 au 15 novembre se lit comme une phrase avec une virgule au milieu. Le mercredi 11 novembre tombe en plein milieu — ni début, ni fin.", 23.5)
f.para("Depuis 1922, le 11 novembre est un jour férié en France. La flamme du Soldat inconnu brûle sous l'Arc de Triomphe depuis 1923, sans jamais s'éteindre. Cent ans de mémoire, et une flamme qui ne s'éteint pas.", 23.5)
f.bridge(E["bridge_valise"])
f.end_report()

ix = COLX[3]
image(p, "hiroshige-maple.jpg", ix, 200, CW, 480)
cy3 = caption(p, ix, 680, CW, "L'automne, près d'Edo : les feuilles rouges annoncent les soirées de lecture et les promenades de novembre.",
              "Utagawa Hiroshige (1797-1858), estampe, domaine public · LACMA")
sav = ["Le 11 novembre est férié depuis 1922.",
       "La flamme brûle depuis 1923.",
       "Paris Photo ouvre jeudi 12."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in sav) + 50
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "LE SAVIEZ-VOUS ?", 24, "sans", True, OLIVE)
yy3 += 52
for t in sav:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "Et vous ? Racontez votre mercredi 11 novembre en deux phrases : cérémonie, musée, ou promenade ? Les meilleurs textes paraîtront dans le VOL.5 (page 7)."
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
    ("lundi 9 novembre", E["date_9"]),
    ("mardi 10 novembre", E["date_10"]),
    ("mercredi 11 novembre", E["date_11"]),
    ("jeudi 12 novembre", E["date_12"]),
    ("dimanche 15 novembre", E["date_15"]),
]:
    p.text(lx, ly + 24, line[0], 24, "serif", True, OLIVE)
    p.text(lx + 330, ly + 24, line[1], 21, "sans", False, GREY)
    ly += 40
p.para(lx, ly + 24, "Exemples : Le mercredi 11 novembre, c'est l'Armistice. · Lundi 9 novembre, le Sénat ouvre la discussion. · Dimanche 15 novembre, les Bleus jouent à Bordeaux.", 20.5, "serif", False, INK, RIGHT - lx, 1.42)

ey = dy + 320
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, E["head_p2ex"], 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, E["p2ex_sub"], 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P2-ex")
e.head("A　QUELLE DATE ?", 25)
e.bridge(E["bridge_dates"])
e.ex("A2", "完成句子", "mercredi", E["n_mercredi11"],
     "L'Armistice a lieu ___ 11 novembre.", instr=E["instr_fill"], size=23)
e.ex("A2", "完成句子", "lundi", E["n_lundi9"],
     "La discussion au Sénat commence ___ 9 novembre.", instr=E["instr_fill"], size=23)
e.ex("A2", "完成句子", "jeudi", E["n_jeudi12"],
     "Paris Photo ouvre au public ___ 12 novembre.", instr=E["instr_fill"], size=23)
e.ex("A2", "完成句子", "dimanche", E["n_dimanche15"],
     "France – Turquie, c'est ___ 15 novembre.", instr=E["instr_fill"], size=23)
e.head("B　LE FUTUR PROCHE", 25)
e.bridge(E["bridge_futur"])
e.ex("A2", "句型转换", "Le Sénat va ouvrir la discussion lundi.", E["n_futur1"],
     "Lundi, le Sénat (ouvrir) la discussion. → ___", instr=E["instr_rewrite"], size=21.5)
e.ex("A2", "句型转换", "Nous allons visiter Paris Photo jeudi.", E["n_futur2"],
     "Jeudi, nous (visiter) Paris Photo. → ___", instr=E["instr_rewrite"], size=21.5)
e.ex("A2", "句型转换", "Tu vas raconter ton mercredi férié.", E["n_futur3"],
     "Tu (raconter) ton mercredi férié. → ___", instr=E["instr_rewrite"], size=21.5)
e.ex("B1", "句型转换", "Vous allez goûter des harengs à Dieppe.", E["n_futur4"],
     "À Dieppe, vous (goûter) des harengs. → ___", instr=E["instr_rewrite"], size=21.5)
e.head("C　COMPRÉHENSION", 25)
e.bridge(E["bridge_read2"])
e.ex("A2", "单选", "C", E["n_comp1"],
     "Le 11 novembre, les cérémonies commencent à... A. 9 h · B. 10 h · C. 11 h", size=22)
e.ex("A2", "单选", "B", E["n_comp2"],
     "Le bleuet est le symbole... A. de Dieppe · B. du 11 novembre · C. du Sénat", size=22)
e.ex("A2", "单选", "A", E["n_comp3"],
     "Paris Photo ouvre au public... A. jeudi 12 · B. mercredi 11 · C. dimanche 15", size=22)
e.head("D　LES MOTS", 25)
e.match_set("A2", "词汇配对",
            ["une gerbe", "une flamme", "un musée", "un vernissage"],
            ["un bouquet de fleurs déposé en hommage", "le feu qui brûle sans s'éteindre",
             "le lieu où l'on regarde des œuvres", "la première soirée d'une exposition"],
            ["a", "b", "c", "d"],
            [E["m_gerbe"], E["m_flamme"], E["m_musee"], E["m_vernissage"]],
            instr=E["instr_match"])
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-vie.svg")
print("P2 saved, exercises so far:", len(REG))
