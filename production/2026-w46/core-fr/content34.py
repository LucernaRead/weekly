# -*- coding: utf-8 -*-
"""W46 FR core VOL.4 — P3 + P4. Press time 2 Nov 2026."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-fr-core/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 =================
CURPAGE[0] = 3
p = BSPage4()
p.band(E["band_p3"], "Le Lucerna", E["band_p3_sub"])

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2540, tag="P3-main")
f.title("Le 11 novembre : se souvenir, puis faire la fête", 37)
f.byline("Par la rédaction · Niveau de lecture : A2 → B1")
f.para("Le 11 novembre 1918, à 11 heures, les armes se sont tues. La Première Guerre mondiale était finie. Depuis, chaque 11 novembre, la France se souvient : c'est le jour de l'Armistice, un jour férié, un jour de silence et de mémoire.")
f.para("Le matin, dans chaque commune, les gens se retrouvent devant le monument aux morts. On dépose une gerbe, on lit les noms des soldats morts pour la France, on observe une minute de silence. Depuis 2012, l'hommage concerne aussi tous les morts pour la France, dans toutes les guerres.")
f.para("À Paris, la cérémonie nationale a lieu sous l'Arc de Triomphe. Le Soldat inconnu y repose depuis 1920, et sa flamme brûle depuis 1923, sans jamais s'éteindre. Le bleuet, fleur bleue, est devenu le symbole de ce jour : on le porte à la boutonnière, comme on porte le souvenir.")
f.para("Et puis, la semaine continue, et samedi, la mémoire laisse la place à la fête : à Dieppe, en Normandie, c'est la 56e Foire aux harengs et à la coquille Saint-Jacques. Deux jours, samedi 14 et dimanche 15 novembre, sur les quais et dans la Grande Rue.")
f.para("Le hareng, « poisson roi », et la coquille Saint-Jacques, emblème du port, sont les rois de la fête. Devant les restaurants, les grills fument ; dans les rues, la Confrérie du hareng et de la coquille Saint-Jacques défile en costume. Samedi matin, l'inauguration a lieu à 10 heures, au départ du pont Colbert, avec la Banda SP76.")
f.para("L'entrée est libre, et la fête est populaire : on goûte, on écoute de la musique, on visite. Samedi après-midi, une visite guidée, « Les quatre ports », part de l'Office de tourisme à 14 heures.")
f.gloss(E["g3"])
f.head(E["head_avous"], 25)
f.bridge(E["bridge_vraifaux"])
f.ex("A2", "阅读判断", "Vrai", E["n_vf1"],
     "L'Armistice a été signé le 11 novembre 1918.", instr="Vrai ou faux ?")
f.ex("A2", "阅读判断", "Vrai", E["n_vf2"],
     "La flamme du Soldat inconnu brûle depuis 1923.", instr="Vrai ou faux ?")
f.ex("A2", "阅读判断", "Faux", E["n_vf3"],
     "Le 11 novembre est un jour de travail comme les autres.", instr="Vrai ou faux ?")
f.ex("B1", "阅读判断", "Faux", E["n_vf4"],
     "La foire de Dieppe a lieu le 11 novembre.", instr="Vrai ou faux ?")
f.ex("B1", "阅读判断", "Vrai", E["n_vf5"],
     "Le hareng est le « poisson roi » de la foire.", instr="Vrai ou faux ?")
f.bridge(E["bridge_fill3"])
f.ex("B1", "完成句子", "gerbe", E["n_gerbe"],
     "On dépose une ___ devant le monument aux morts.")
f.ex("A2", "完成句子", "bleuet", E["n_bleuet"],
     "Le ___ est la fleur du 11 novembre.")
f.ex("A2", "完成句子", "quais", E["n_quais"],
     "La foire a lieu sur les ___ de Dieppe.")
f.ex("B1", "完成句子", "grills", E["n_grills"],
     "Devant les restaurants, les ___ fument.")
f.bridge(E["bridge_neg"])
f.ex("B1", "句型转换", "La flamme ne s'éteint jamais.", E["n_neg1"],
     "(jamais) La flamme s'éteint. → ___", instr=E["instr_rewrite"])
f.ex("B1", "句型转换", "On n'oublie pas les morts pour la France.", E["n_neg2"],
     "(pas) On oublie les morts pour la France. → ___", instr=E["instr_rewrite"])
f.ex("B1", "句型转换", "La foire n'est pas à Paris.", E["n_neg3"],
     "(pas) La foire est à Paris. → ___", instr=E["instr_rewrite"])
f.head(E["head_dieppe_ex"], 25)
f.bridge(E["bridge_dieppe"])
f.ex("A2", "完成句子", "56e", E["n_56e"],
     "C'est la ___ édition de la foire de Dieppe.")
f.ex("B1", "完成句子", "samedi", E["n_samedi14"],
     "L'inauguration a lieu ___ 14 novembre, à 10 heures.")
f.ex("A2", "完成句子", "pont Colbert", E["n_colbert"],
     "L'inauguration part du ___ .")
f.ex("B1", "单选", "B", E["n_coquille"],
     "La coquille Saint-Jacques est... A. un poisson · B. l'emblème du port · C. un bateau")
f.ex("B1", "完成句子", "14 heures", E["n_14h"],
     "La visite « Les quatre ports » part à ___ .")
f.ex("A2", "完成句子", "libre", E["n_libre"],
     "L'entrée de la foire est ___.")
f.end_report()

ix = COLX[3]
image(p, "chrysanthemum-blanco.jpg", ix, 200, CW, 540)
cy3 = caption(p, ix, 740, CW,
              "Le chrysanthème, fleur du souvenir en France : on le pose sur les tombes, on ne l'offre jamais en cadeau.",
              "Planche botanique, Flora de Filipinas (Blanco), XIXe siècle, domaine public")
by3 = cy3 + 22
p.rect(ix, by3, CW, 452, fill=BOX, stroke=LINE, sw=1.4)
p.text(ix + 22, by3 + 40, E["head_mots_fetes"], 23, "sans", True, OLIVE)
mots = E["mots_fetes"]
yy3 = by3 + 82
for m in mots:
    p.text(ix + 22, yy3, m, 21.5, "serif", False, INK)
    yy3 += 37
zy3 = by3 + 452 + 26
p.rect(ix, zy3, CW, 476, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(ix + 22, zy3 + 40, E["head_zoom"], 23, "sans", True, OLIVE)
illus_flame(p, ix + 22, zy3 + 58, s=0.85)
p.para(ix + 70, zy3 + 78, "1918 : l'Armistice. 1920 : le Soldat inconnu. 1922 : le jour férié. 1923 : la flamme. 2026 : la 56e foire de Dieppe.", 21.5, "serif", False, INK, CW - 92, 1.42)
p.para(ix + 22, zy3 + 300, E["zoom_note"], 20, "sans", False, GREY, CW - 44, 1.4)
dy3 = zy3 + 476 + 26
p.rect(ix, dy3, CW, 330, fill=BOX, stroke=LINE, sw=1.4)
p.text(ix + 22, dy3 + 40, E["head_dates3"], 23, "sans", True, OLIVE)
dates3 = [
    ("mer. 11 nov.", "Armistice · cérémonies"),
    ("jeu. 12 nov.", "Paris Photo ouvre"),
    ("sam. 14 nov.", "Dieppe · inauguration 10 h"),
    ("dim. 15 nov.", "Dieppe · jour 2"),
]
yy3 = dy3 + 84
for d, t in dates3:
    p.text(ix + 22, yy3, d, 19.5, "sans", True, BRICK)
    p.text(ix + 168, yy3, t, 18.5, "serif", False, INK)
    yy3 += 42
p.para(ix + 22, yy3 + 20, E["dates3_note"], 19.5, "sans", False, GREY, CW - 44, 1.4)
py3 = dy3 + 330 + 30
p.text(ix, py3 + 24, "POUR OU CONTRE ?", 23, "sans", True, OLIVE)
p.hline(ix, ix + CW, py3 + 38, GOLD, 2)
p.para(ix, py3 + 74, "Un jour férié au milieu de la semaine : une bonne coupure, ou une semaine cassée ? Écrivez votre avis en deux phrases pour le courrier des lecteurs (page 7).", 20.5, "serif", False, INK, CW, 1.4)
p.foot(3)
p.save(f"{OUT}/p3-culture.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 =================
CURPAGE[0] = 4
p = BSPage4()
p.band(E["band_p4"], "Le Lucerna", E["band_p4_sub"])

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2540, tag="P4-main")
f.title("Le Masters est fini, Turin commence", 37)
f.byline("Par la rédaction · Niveau de lecture : B1")
f.para("C'était le dernier grand tournoi de la saison : le Rolex Paris Masters, 41e édition, sur dur, en salle, à la Paris La Défense Arena de Nanterre. Le tableau comptait 56 joueurs ; les finales ont eu lieu dimanche 8 novembre, comme prévu, avec la finale du simple, la finale du double et la finale du simple en fauteuil.")
f.para("Mais une absence a marqué le tournoi : Jannik Sinner, le tenant du titre, n'a pas joué. Blessé au genou, l'Italien a mis fin à sa saison le 6 octobre. Il ne jouera pas non plus les Masters de Turin : sa place ira au joueur suivant dans la course, arrêtée lundi 9 novembre.")
f.para("Au moment où nous écrivons, le 2 novembre, les premiers matches venaient à peine de commencer : il est donc impossible de donner ici les résultats des finales. Ce numéro ne les invente pas — les résultats du week-end seront dans le VOL.5, avec le nom du vainqueur.")
f.para("Dimanche 15 novembre, c'est Turin qui prend le relais : les Nitto ATP Finals réunissent les huit meilleurs joueurs de l'année, en deux groupes de quatre. Les matches de groupe se jouent du 15 au 20 novembre, les demi-finales samedi 21, les finales dimanche 22. Trois joueurs étaient déjà qualifiés le 19 octobre : Alexander Zverev, Carlos Alcaraz et Ben Shelton.")
f.para("Et le football ? Pas de Ligue 1 ce week-end : c'est la trêve internationale, et la 11e journée se jouera les 21 et 22 novembre. À la place, les Bleus jouent deux fois : jeudi 12 novembre en Italie, à Milan, puis dimanche 15 à Bordeaux, contre la Turquie, à 20 h 45. En tête du groupe A1 avec 10 points après quatre matches, la France peut valider sa place en quarts de finale.")
f.gloss(E["g4"])
f.head(E["head_avous"], 25)
f.bridge(E["bridge_read4"])
f.ex("B1", "单选", "B", E["n_mcq1"],
     "Les finales du Masters ont eu lieu... A. samedi 7 · B. dimanche 8 · C. lundi 9")
f.ex("B1", "单选", "A", E["n_mcq2"],
     "Sinner n'a pas joué parce qu'il est... A. blessé au genou · B. en vacances · C. à Turin")
f.ex("B1", "单选", "C", E["n_mcq3"],
     "Les Masters de Turin commencent... A. le 9 nov. · B. le 12 nov. · C. le 15 nov.")
f.ex("B1", "单选", "B", E["n_mcq4"],
     "France – Turquie, c'est... A. à Milan · B. à Bordeaux · C. à Nanterre")
f.ex("B1", "单选", "A", E["n_mcq5"],
     "La 11e journée de Ligue 1, c'est... A. les 21–22 nov. · B. le 15 nov. · C. le 9 nov.")
f.bridge(E["bridge_match4"])
f.match_set("B1", "词汇配对",
            ["un forfait", "un tableau", "un groupe", "la trêve"],
            ["ne pas jouer, à cause d'une blessure", "la liste des matches d'un tournoi",
             "quatre joueurs qui se rencontrent", "la pause entre deux séries de matches"],
            ["a", "b", "c", "d"],
            [E["m_forfait"], E["m_tableau"], E["m_groupe"], E["m_treve"]],
            instr=E["instr_match"])
f.bridge(E["bridge_comp4"])
f.ex("B1", "完成句子", "plus vite", E["n_comp4a"],
     "En salle, la balle va ___ (vite) qu'en plein air.")
f.ex("B1", "完成句子", "plus grand", E["n_comp4b"],
     "Turin est ___ (grand) qu'un petit tournoi.")
f.ex("B1", "完成句子", "moins longue", E["n_comp4c"],
     "La trêve est ___ (longue) que la saison. (moins)")
f.head(E["head_foot"], 25)
f.para("La trêve internationale, c'est le moment où les clubs s'arrêtent et où les sélections jouent. Pour les lecteurs de français, c'est une leçon gratuite : les mêmes phrases reviennent — « il frappe ! », « c'est le but ! » — et les noms des villes deviennent familiers.", 23.5)
f.para("Jeudi 12, à Milan, puis dimanche 15, à Bordeaux : deux soirs, deux matches, et une qualification à valider. Le sélectionneur devait dévoiler sa liste vendredi 6 novembre, à 18 heures.", 23.5)
f.bridge(E["bridge_treve"])
f.head(E["head_debat4"], 25)
f.para("Turin sans Sinner : un tournoi plus ouvert, ou un tournoi moins beau ? Discutez en classe : deux phrases pour, deux phrases contre.", 23.5)
f.box("LES PHRASES DU COMMENTATEUR", [
    ("« Allez ! » — " + E["box_allez"] + " · « Quelle action ! » — " + E["box_action"], "serif", False, INK, 21.5, 1.42),
    ("« Il marque ! » — " + E["box_marque"] + " · « C'est gagné ! » — " + E["box_gagne"], "serif", False, INK, 21.5, 1.42),
])
f.end_report()

ix = COLX[3]
p.rect(ix, 200, CW, 470, fill=BOX, stroke=LINE, sw=1.4)
p.text(ix + 22, 240, E["head_chiffres"], 23, "sans", True, OLIVE)
p.para(ix + 22, 278, "41e édition du Masters en 2026. 56 joueurs au tableau. 8 joueurs à Turin, en deux groupes de quatre. 10 points pour la France après quatre matches de Ligue des nations.", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, 520, E["chiffres_note"], 21.5, "serif", False, INK, CW - 44, 1.42)
vy = 696
p.rect(ix, vy, CW, 416, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(ix + 22, vy + 40, E["head_mots_tennis"], 23, "sans", True, OLIVE)
mots4 = E["mots_tennis"]
yy4 = vy + 82
for m in mots4:
    p.text(ix + 22, yy4, m, 21.5, "serif", False, INK)
    yy4 += 37
sy4 = vy + 416 + 26
p.rect(ix, sy4, CW, 218, fill=BOX, stroke=LINE, sw=1.4)
p.text(ix + 22, sy4 + 40, E["head_asuivre"], 23, "sans", True, OLIVE)
p.para(ix + 22, sy4 + 80, "Les résultats du Masters de Paris seront dans le VOL.5 : le nom du vainqueur, les finalistes, et la liste complète des huit joueurs de Turin.", 21.5, "serif", False, INK, CW - 44, 1.42)
mf = Flow(p, [(ix, CW)], sy4 + 218 + 30, 2540, tag="P4-micro")
mf.head(E["head_micro"], 24)
mf.bridge(E["bridge_micro4"])
mf.ex("B1", "完成句子", "forfait", E["n_forfait"],
      "Sinner a déclaré ___ : blessé, il n'a pas joué.", size=23)
mf.ex("B1", "完成句子", "finale", E["n_finale8"],
      "La ___ du simple a eu lieu dimanche 8.", size=23)
mf.ex("B1", "完成句子", "groupes", E["n_groupes"],
      "À Turin, huit joueurs, en deux ___ de quatre.", size=23)
mf.ex("B1", "完成句子", "trêve", E["n_treve"],
      "Pas de Ligue 1 : c'est la ___ internationale.", size=23)
mf.ex("B1", "完成句子", "Bordeaux", E["n_bordeaux"],
      "France – Turquie, dimanche 15, à ___.", size=23)
mf.ex("A2", "完成句子", "Milan", E["n_milan"],
      "Italie – France, jeudi 12, à ___.", size=23)
mf.end_report()
db4 = mf.y + 6
p.rect(ix, db4, CW, 2540 - db4, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(ix + 22, db4 + 40, E["head_debat"], 23, "sans", True, OLIVE)
p.para(ix + 22, db4 + 78, "Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ? La question reste posée pour Turin.", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, db4 + 196, E["debat_note"], 20, "sans", False, GREY, CW - 44, 1.4)
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
