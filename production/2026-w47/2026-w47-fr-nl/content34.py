# -*- coding: utf-8 -*-
"""W47 FR core VOL.4 — P3 + P4. Press time 10 Nov 2026."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 =================
CURPAGE[0] = 3
p = BSPage4()
p.band(E["band_p3"], "Le Lucerna", E["band_p3_sub"])

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2560, tag="P3-main")
f.title("Le beaujolais nouveau a 75 ans", 32)
f.byline("Par la rédaction　Niveau de lecture : A2 → B1")
f.para("Jeudi 19 novembre, à 0 heure, le beaujolais nouveau est arrivé ! Dans les bars, dans les caves, dans les restaurants, on lève le verre et on dit la phrase de chaque année : « Le beaujolais nouveau est arrivé ! » C'est le troisième jeudi de novembre, comme chaque année depuis 1985.")
f.para("Pourquoi le troisième jeudi ? L'histoire commence en 1951 : les vignerons du Beaujolais obtiennent le droit de mettre leur vin en bouteille et de le vendre plus tôt, sans attendre le 15 décembre. Mais la date du 15 novembre tombe trop près du 11 novembre, jour férié, et parfois un week-end. En 1985, on fixe la règle : le troisième jeudi de novembre.")
f.para("Le vin, lui, est simple : un seul cépage, le gamay ; deux appellations seulement, beaujolais et beaujolais-villages ; un vin rouge — et aussi un rosé. C'est un vin primeur : il est vendu quelques semaines seulement après les vendanges. Cette année, on a commencé à couper le raisin dans les vignes dès le 13 août, très tôt ; la récolte sera courte : le ministère prévoit 22 % de vin en moins qu'en 2025 pour l'ensemble Bourgogne-Beaujolais.")
f.para("Et la fête ? Elle commence dès mercredi 18 novembre au soir, à Beaujeu, avec les Sarmentelles : on perce le premier tonneau à minuit, on chante, on danse. À Lyon, les Nouveaux arrivent en tracteur, puis on les met en perce place des Terreaux. L'interprofession, Inter Beaujolais, compte plus de 500 événements — et elle fête cette année les 75 ans du rendez-vous.")
f.para("Comment le goûter ? On regarde sa couleur, on sent son parfum — fruité, léger — puis on boit une petite gorgée. Il accompagne le saucisson, les lentilles, la volaille rôtie. Et on n'oublie pas : l'abus d'alcool est dangereux pour la santé, à consommer avec modération — et jamais avant 18 ans.")
f.para("Un vin primeur, une fête populaire : le beaujolais nouveau, c'est la France qui trinque à l'automne. Santé — avec modération !")
f.gloss(E["g3"])
f.head(E["head_avous"], 25)
f.bridge(E["bridge_vraifaux"])
f.ex("A2", "阅读判断", "Vrai", E["n_vf1"],
     "En 1951, les vignerons obtiennent le droit de vendre plus tôt.", instr="Vrai ou faux ?")
f.ex("A2", "阅读判断", "Faux", E["n_vf2"],
     "Le beaujolais nouveau sort le deuxième jeudi de novembre.", instr="Vrai ou faux ?")
f.ex("A2", "阅读判断", "Vrai", E["n_vf3"],
     "Le beaujolais nouveau est mis en vente le 19 novembre.", instr="Vrai ou faux ?")
f.ex("B1", "阅读判断", "Faux", E["n_vf4"],
     "Les Sarmentelles ont lieu à Paris.", instr="Vrai ou faux ?")
f.ex("B1", "阅读判断", "Vrai", E["n_vf5"],
     "Le gamay est le cépage du Beaujolais.", instr="Vrai ou faux ?")
f.bridge(E["bridge_fill3"])
f.ex("B1", "完成句子", "gamay", E["n_gerbe"],
     "Le cépage du Beaujolais, c'est le ___.")
f.ex("A2", "完成句子", "jeudi", E["n_bleuet"],
     "Le beaujolais nouveau sort le troisième ___ de novembre.")
f.ex("A2", "完成句子", "Beaujeu", E["n_quais"],
     "Les Sarmentelles ont lieu à ___.")
f.ex("B1", "完成句子", "1985", E["n_grills"],
     "La règle du troisième jeudi date de ___.")
f.bridge(E["bridge_neg"])
f.ex("B1", "句型转换", "Le vin ne se vend jamais avant le troisième jeudi.", E["n_neg1"],
     "(jamais) Le vin se vend avant le troisième jeudi. → ___", instr=E["instr_rewrite"])
f.ex("B1", "句型转换", "On ne boit pas d'alcool avant 18 ans.", E["n_neg2"],
     "(pas) On boit de l'alcool avant 18 ans. → ___", instr=E["instr_rewrite"])
f.ex("B1", "句型转换", "Le beaujolais n'est pas un vin blanc.", E["n_neg3"],
     "(pas) Le beaujolais est un vin blanc. → ___", instr=E["instr_rewrite"])
f.head(E["head_dieppe_ex"], 25)
f.bridge(E["bridge_dieppe"])
f.ex("A2", "完成句子", "75 ans", E["n_56e"],
     "Cette année, ce sont les ___ du rendez-vous.")
f.ex("B1", "完成句子", "minuit", E["n_samedi14"],
     "La mise en perce a lieu à ___.")
f.ex("A2", "完成句子", "troisième", E["n_colbert"],
     "Le vin sort le ___ jeudi de novembre.")
f.ex("B1", "单选", "B", E["n_coquille"],
     "Le gamay est... A. un fromage　B. un cépage　C. un village")
f.ex("B1", "完成句子", "13", E["n_14h"],
     "Les vendanges 2026 ont commencé le ___ août.")
f.ex("A2", "完成句子", "saucisson", E["n_libre"],
     "Pour accompagner le beaujolais : du ___.")
f.end_report()

ix = COLX[3]
image(p, "vendanges-moreau.jpg", ix, 200, CW, 320)
cy3 = caption(p, ix, 520, CW,
              "Les vendanges : les grappes, les paniers, la charrette — le vin nouveau commence ici.",
              "Adrien Moreau (1843-1906), Les vendanges, huile sur toile, domaine public")
by3 = cy3 + 22
p.rect(ix, by3, CW, 452, fill=BOX)
p.text(ix + 22, by3 + 40, E["head_mots_fetes"], 23, "sans", True, OLIVE)
mots = E["mots_fetes"]
yy3 = by3 + 82
for m in mots:
    p.text(ix + 22, yy3, m, 21.5, "serif", False, INK)
    yy3 += 37
zy3 = by3 + 452 + 26
p.rect(ix, zy3, CW, 476, fill="#f0eee5")
p.text(ix + 22, zy3 + 40, E["head_zoom"], 22, "sans", True, OLIVE)
illus_flame(p, ix + 22, zy3 + 58, s=0.85)
p.para(ix + 70, zy3 + 78, "1951 : le droit de vendre plus tôt. 1985 : le troisième jeudi. 2026 : les 75 ans du rendez-vous.", 21.5, "serif", False, INK, CW - 92, 1.42)
p.para(ix + 22, zy3 + 300, E["zoom_note"], 20, "sans", False, GREY, CW - 44, 1.4)
dy3 = zy3 + 476 + 26
p.rect(ix, dy3, CW, 330, fill=BOX)
p.text(ix + 22, dy3 + 40, E["head_dates3"], 23, "sans", True, OLIVE)
dates3 = [
    ("mer. 18 nov.", "Sarmentelles à Beaujeu"),
    ("jeu. 19 nov.", "Mise en vente à 0 h"),
    ("ven. 20 nov.", "Journée de l'enfance"),
    ("sam. 21 nov.", "SERD　1er jour"),
]
yy3 = dy3 + 84
for d, t in dates3:
    p.text(ix + 22, yy3, d, 19.5, "sans", True, OLIVE)
    p.text(ix + 168, yy3, t, 18.5, "serif", False, INK)
    yy3 += 42
p.para(ix + 22, yy3 + 20, E["dates3_note"], 19.5, "sans", False, GREY, CW - 44, 1.4)
py3 = dy3 + 330 + 30
p.text(ix, py3 + 24, "POUR OU CONTRE ?", 23, "sans", True, OLIVE)
p.hline(ix, ix + CW, py3 + 38, OLIVE, 2)
p.para(ix, py3 + 74, "Une fête du vin au milieu de novembre : une belle tradition, ou une fête trop commerciale ? Écrivez votre avis en deux phrases pour le courrier des lecteurs (page 7).", 20.5, "serif", False, INK, CW, 1.4)
p.foot(3)
p.save(f"{OUT}/p3-culture.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 =================
CURPAGE[0] = 4
p = BSPage4()
p.band(E["band_p4"], "Le Lucerna", E["band_p4_sub"])

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2560, tag="P4-main")
f.title("Alcaraz gagne Paris, Turin commence", 32)
f.byline("Par la rédaction　Niveau de lecture : B1")
f.para("C'était le dernier grand tournoi de tennis de la saison : le Rolex Paris Masters, 41e édition, sur dur, en salle, à Nanterre. Le tableau comptait 56 joueurs ; la finale du simple a eu lieu dimanche 8 novembre. Carlos Alcaraz, tête de série n° 2, a battu son adversaire, Ben Shelton, tête de série n° 3, 7-6(5), 7-5, en deux sets.")
f.para("Pour Alcaraz, c'est un premier titre à Paris, et un neuvième titre en Masters 1000. L'Espagnol a sauvé six balles de break dans le premier set, puis il a pris le service de Shelton à 6-5 dans le deuxième. Un choc remporté en deux sets, sans tie-break dans le deuxième.")
f.para("Mais une absence a marqué le tournoi : Jannik Sinner, le tenant du titre, n'a pas joué. Blessé au genou, l'Italien a mis fin à sa saison le 6 octobre. Il ne jouera pas non plus les Masters de Turin : sa place ira au joueur suivant dans la course, arrêtée lundi 9 novembre — l'Espagnol Rafael Jodar, neuvième de la course.")
f.para("Dimanche 15 novembre, c'est Turin qui prend le relais : les Nitto ATP Finals réunissent les huit meilleurs joueurs de l'année, en deux groupes de quatre. Les huit : Alexander Zverev, Carlos Alcaraz, Ben Shelton, Daniil Medvedev, Flavio Cobolli, Arthur Fils, Frances Tiafoe et Rafael Jodar. Quatre débutants : Cobolli, Fils, Tiafoe et Jodar — dont un Français, Arthur Fils. Le tirage au sort des groupes a eu lieu jeudi 12 novembre ; les matches de groupe se jouent du 15 au 20 novembre, les demi-finales samedi 21, les finales dimanche 22.")
f.para("Et le football ? Pas de Ligue 1 ce week-end-là : c'est la trêve internationale, et la 11e journée se jouera du 20 au 22 novembre. À la place, les Bleus jouent deux fois : jeudi 12 novembre en Italie, à Milan, puis dimanche 15 à Bordeaux, contre la Turquie, à 20 h 45. En tête du groupe A1 avec 10 points après quatre matches, la France peut valider sa place en quarts de finale.")
f.gloss(E["g4"])
f.head(E["head_avous"], 25)
f.bridge(E["bridge_read4"])
f.ex("B1", "单选", "B", E["n_mcq1"],
     "La finale du Masters a eu lieu... A. samedi 7　B. dimanche 8　C. lundi 9")
f.ex("B1", "单选", "A", E["n_mcq2"],
     "Alcaraz a battu en finale... A. Shelton　B. Sinner　C. Zverev")
f.ex("B1", "单选", "C", E["n_mcq3"],
     "Les Masters de Turin commencent... A. le 9 nov.　B. le 12 nov.　C. le 15 nov.")
f.ex("B1", "单选", "A", E["n_mcq4"],
     "Le Français débutant à Turin, c'est... A. Fils　B. Cobolli　C. Jodar")
f.ex("B1", "单选", "A", E["n_mcq5"],
     "La 11e journée de Ligue 1 reprend... A. vendredi 20　B. dimanche 15　C. lundi 9")
f.bridge(E["bridge_match4"])
f.match_set("B1", "词汇配对",
            ["un forfait", "un tableau", "un tirage", "la trêve"],
            ["ne pas jouer, à cause d'une blessure", "la liste des matches d'un tournoi",
             "le sort qui fait les groupes", "la pause entre deux séries de matches"],
            ["a", "b", "c", "d"],
            [E["m_forfait"], E["m_tableau"], E["m_tirage3"], E["m_treve"]],
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
f.para("Jeudi 12, à Milan, puis dimanche 15, à Bordeaux : deux soirs, deux matches, et une qualification à valider. Les résultats seront dans le VOL.5.", 23.5)
f.bridge(E["bridge_treve"])
f.head(E["head_debat4"], 25)
f.para("Alcaraz peut-il gagner Turin après Paris ? Discutez en classe : deux phrases pour, deux phrases contre.", 23.5)
f.box("LES PHRASES DU COMMENTATEUR", [
    ("« Allez ! » — " + E["box_allez"] + "　« Quelle action ! » — " + E["box_action"], "serif", False, INK, 21.5, 1.42),
    ("« Il marque ! » — " + E["box_marque"] + "　« C'est gagné ! » — " + E["box_gagne"], "serif", False, INK, 21.5, 1.42),
], tsize=21)
f.end_report()

ix = COLX[3]
p.rect(ix, 200, CW, 470, fill=BOX)
p.text(ix + 22, 240, E["head_chiffres"], 23, "sans", True, OLIVE)
p.para(ix + 22, 278, "41e édition du Masters en 2026. 7-6(5), 7-5 : la finale de Paris. 8 joueurs à Turin, dont 4 débutants. 10 points pour la France après quatre matches de Ligue des nations.", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, 520, E["chiffres_note"], 21.5, "serif", False, INK, CW - 44, 1.42)
vy = 696
p.rect(ix, vy, CW, 416, fill="#f0eee5")
p.text(ix + 22, vy + 40, E["head_mots_tennis"], 21, "sans", True, OLIVE)
mots4 = E["mots_tennis"]
yy4 = vy + 82
for m in mots4:
    p.text(ix + 22, yy4, m, 21.5, "serif", False, INK)
    yy4 += 37
sy4 = vy + 416 + 26
p.rect(ix, sy4, CW, 218, fill=BOX)
p.text(ix + 22, sy4 + 40, E["head_asuivre"], 23, "sans", True, OLIVE)
p.para(ix + 22, sy4 + 80, "Les finales de Turin, dimanche 22 : le nom du vainqueur sera dans le VOL.5, avec les résultats des Bleus et de la 11e journée de Ligue 1.", 21.5, "serif", False, INK, CW - 44, 1.42)
mf = Flow(p, [(ix, CW)], sy4 + 218 + 30, 2560, tag="P4-micro")
mf.head(E["head_micro"], 24)
mf.bridge(E["bridge_micro4"])
mf.ex("B1", "完成句子", "forfait", E["n_forfait"],
      "Sinner a déclaré ___ : blessé, il n'a pas joué.", size=23)
mf.ex("B1", "完成句子", "finale", E["n_finale8"],
      "La ___ du simple a eu lieu dimanche 8.", size=23)
mf.ex("B1", "完成句子", "groupes", E["n_groupes"],
      "À Turin, huit joueurs, en deux ___ de quatre.", size=23)
mf.ex("B1", "完成句子", "tirage", E["n_treve"],
      "Le ___ des groupes a eu lieu jeudi 12.", size=23)
mf.ex("B1", "完成句子", "Bordeaux", E["n_bordeaux"],
      "France – Turquie, dimanche 15, à ___.", size=23)
mf.ex("A2", "完成句子", "Milan", E["n_milan"],
      "Italie – France, jeudi 12, à ___.", size=23)
mf.end_report()
db4 = mf.y + 6
p.rect(ix, db4, CW, 2560 - db4, fill="#f0eee5")
p.text(ix + 22, db4 + 40, E["head_debat"], 23, "sans", True, OLIVE)
p.para(ix + 22, db4 + 78, "Turin sans Sinner : un tournoi plus ouvert, ou un tournoi moins beau ? La question reste posée pour dimanche 22.", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, db4 + 196, E["debat_note"], 20, "sans", False, GREY, CW - 44, 1.4)
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
