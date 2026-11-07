# -*- coding: utf-8 -*-
"""W46 FR core VOL.4 — P5 + P6. Press time 2 Nov 2026."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-fr-nl/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 =================
CURPAGE[0] = 5
p = BSPage4()
p.band(E["band_p5"], "Le Lucerna", E["band_p5_sub"])

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2540, tag="P5-main")
f.title("Paris Photo : deux cents ans de photographie", 37)
f.byline("Par la rédaction · Niveau de lecture : B1")
f.para("Du jeudi 12 au dimanche 15 novembre, le Grand Palais devient une immense galerie : c'est la 29e édition de Paris Photo, le salon de la photographie. Cette année est spéciale : on y fête les 200 ans de la photographie, née en 1826. Des galeries et des éditeurs de 38 pays montrent des tirages, des livres et des installations.")
f.para("Au programme : « Révéler », une exposition tirée de la collection de photographie du Centre Pompidou, et « Elles × Paris Photo », qui met en avant les femmes photographes. Partout, des conversations avec des photographes, des livres à feuilleter, des séances de signatures dans les allées.")
f.para("Pratique : le salon ouvre de 13 heures à 20 heures, 19 heures dimanche. Le billet coûte 36 euros en semaine, 41 euros le week-end, en ligne seulement ; le billet du soir et le tarif étudiant coûtent 26 euros. Le vernissage, mercredi 11 novembre, est réservé aux invités — le public entre jeudi.")
f.para("Pourquoi ce salon plaît-il aux jeunes ? Parce qu'on n'y reste pas assis : on regarde, on compare, on discute. Pour un apprenant de français, c'est idéal : chaque photo a une légende à lire, chaque galerie une histoire à demander. Et le mercredi 11 novembre, jour férié, le cinéma propose aussi ses nouveautés : « Il faut brûler Maman », la comédie d'Albert Dupontel, « Scrooge », avec Johnny Depp, et un film de braquage de David Leitch. En revanche, « Kaamelott » ne sort pas : le film est repoussé au 10 mars 2027.")
f.gloss(E["g5"])
f.head(E["head_avous"], 25)
f.bridge(E["bridge_read5"])
f.ex("B1", "单选", "B", E["n_photo1"],
     "Paris Photo 2026, c'est la... A. 15e édition · B. 29e édition · C. 56e édition")
f.ex("B1", "单选", "A", E["n_photo2"],
     "La photographie est née en... A. 1826 · B. 1926 · C. 2026")
f.ex("B1", "单选", "C", E["n_photo3"],
     "Le salon ouvre au public... A. mercredi 11 · B. mardi 10 · C. jeudi 12")
f.ex("B1", "单选", "B", E["n_photo4"],
     "Le billet du soir coûte... A. 36 € · B. 26 € · C. 41 €")
f.ex("B1", "单选", "A", E["n_photo5"],
     "« Kaamelott » sort... A. le 10 mars 2027 · B. le 11 novembre · C. le 12 novembre")
f.bridge(E["bridge_fill5"])
f.ex("B1", "完成句子", "Grand Palais", E["n_palais"],
     "Paris Photo a lieu au ___.")
f.ex("B1", "完成句子", "légende", E["n_legende"],
     "Chaque photo a une ___ à lire.")
f.ex("B1", "完成句子", "vernissage", E["n_vernissage"],
     "Le ___ est réservé aux invités.")
f.ex("B1", "完成句子", "photographes", E["n_photographes"],
     "« Elles × Paris Photo » met en avant les femmes ___.")
f.ex("B1", "完成句子", "Depp", E["n_depp"],
     "« Scrooge », c'est avec Johnny ___.")
f.ex("A2", "完成句子", "mercredi", E["n_mercredi_cine"],
     "Les nouveautés cinéma sortent le ___ 11 novembre.")
f.bridge(E["bridge_match5"])
f.match_set("B1", "词汇配对",
            ["un tirage", "une galerie", "un vernissage", "une légende"],
            ["une photographie imprimée sur papier", "le lieu où l'on expose des œuvres",
             "la première soirée d'une exposition", "le petit texte sous une image"],
            ["a", "b", "c", "d"],
            [E["m_tirage"], E["m_galerie"], E["m_vernissage2"], E["m_legende2"]],
            instr=E["instr_match"])
f.bridge(E["bridge_dialogue5"])
f.ex("B1", "完成句子", "jeudi", E["n_dial1"],
     "— Tu vas à Paris Photo quand ? — ___, le premier jour.")
f.ex("B1", "完成句子", "deux billets", E["n_dial2"],
     "— Tu as pris ___ ? — Oui, pour toi et moi.")
f.para("Regarder une photo, c'est déjà lire. Chaque photo a une légende à lire, chaque galerie une histoire à demander. Et le soir, on peut aussi aller au cinéma : le mercredi 11 novembre est un jour de sorties, comme un samedi.")
f.box("REGARDER UNE PHOTO", [("« Une photo vaut mille mots. » — dit-on. Et vous, quelle photo raconterait votre semaine ?", "serif", False, INK, 22, 1.5), (E["debat5_note"], "sans", False, GREY, 21, 1.45)], bsize=22, tsize=22, pad=16, gap=10)
f.end_report()

ix = COLX[3]
p.rect(ix, 200, CW, 470, fill=BOX, stroke=LINE, sw=1.4)
p.text(ix + 22, 240, E["head_sortir"], 23, "sans", True, OLIVE)
p.para(ix + 22, 278, "Mercredi 11 : vernissage de Paris Photo (invités) + cinéma. Jeudi 12 – dimanche 15 : Paris Photo, de 13 h à 20 h (19 h dimanche). Samedi 14 – dimanche 15 : la foire de Dieppe.", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, 520, E["sortir_note"], 21.5, "serif", False, INK, CW - 44, 1.42)
qy5 = 696
p.rect(ix, qy5, CW, 400, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(ix + 22, qy5 + 40, E["head_mots_photo"], 23, "sans", True, OLIVE)
mots5 = E["mots_photo"]
yy5 = qy5 + 82
for m in mots5:
    p.text(ix + 22, yy5, m, 21.5, "serif", False, INK)
    yy5 += 37
dy5 = qy5 + 400 + 26
p.rect(ix, dy5, CW, 440, fill=BOX, stroke=LINE, sw=1.4)
p.text(ix + 22, dy5 + 40, E["head_cine"], 23, "sans", True, OLIVE)
p.para(ix + 22, dy5 + 78, "Mercredi 11 novembre, jour férié : « Il faut brûler Maman » (Albert Dupontel), « Scrooge » (Ti West, avec Johnny Depp), un film de braquage (David Leitch), et la ressortie de « Dune ». « Kaamelott » est repoussé au 10 mars 2027.", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, dy5 + 300, E["cine_note"], 20, "sans", False, GREY, CW - 44, 1.4)
ty5 = dy5 + 440 + 26
p.rect(ix, ty5, CW, 2540 - ty5, fill=BOX, stroke=LINE, sw=1.4)
p.text(ix + 22, ty5 + 40, E["head_debat"], 23, "sans", True, OLIVE)
p.para(ix + 22, ty5 + 78, "Une photo vaut-elle mille mots ? Discutez en classe : deux phrases pour, deux phrases contre. Et vous, quelle photo raconterait votre semaine ?", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, ty5 + 285, E["debat5_note"], 20, "sans", False, GREY, CW - 44, 1.4)
p.foot(5)
p.save(f"{OUT}/p5-jeunesse.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 =================
CURPAGE[0] = 6
p = BSPage4()
p.band(E["band_p6"], "Le Lucerna", E["band_p6_sub"])

f = Flow(p, [(COLX[0], CW), (COLX[1], CW)], 200, 1300, tag="P6-deep")
f.title("Au Sénat, cette semaine : le budget de la Sécu", 36)
f.byline("Par la rédaction · Niveau de lecture : B2")
f.para("Cette semaine, le Sénat examine le projet de loi de financement de la Sécurité sociale pour 2027. La discussion générale s'ouvre lundi 9 novembre ; ensuite, les sénateurs discutent les articles, un par un. Le texte qu'ils examinent est celui du gouvernement, dans sa version initiale.")
f.para("Pourquoi la version initiale ? Parce que le 23 octobre, l'Assemblée nationale a rejeté la partie « recettes » du texte, par 115 voix contre 1. Le rejet a arrêté l'examen : la partie « dépenses » n'a jamais été débattue par les députés. La commission des affaires sociales du Sénat a préparé son rapport le mercredi 4 novembre.")
f.para("Attention, lecteurs : ce numéro corrige son propre calendrier. La semaine dernière, nous avions annoncé des votes par mission, du 3 au 6 novembre. Ce calendrier n'a pas eu lieu : le vote solennel est prévu mardi 3 novembre, sur la première partie du budget de l'État, celle des recettes.")
f.para("La règle est simple : si la première partie est rejetée, les amendements votés en séance tombent, et c'est le texte initial du gouvernement qui part au Sénat. C'est ce qui s'était passé l'an dernier, avec un rejet par 404 voix contre 1. Pour la Sécu, le Parlement dispose de cinquante jours, jusqu'au 26 novembre ; ensuite, une commission mixte paritaire cherchera un texte commun.")
f.gloss(E["g6"])
f.end_report()

chx, chw = COLX[0], 2 * CW + GUT
chy = 1330
p.rect(chx, chy, chw, 436, fill=BOX, stroke=LINE, sw=1.4)
p.text(chx + 22, chy + 40, E["head_chart"], 24, "sans", True, OLIVE)
p.text(chx + 22, chy + 74, E["chart_sub"], 19, "sans", False, GREY)
rows6 = [
    ("23 oct.", "Rejet 115–1 des recettes de la Sécu", OLIVE),
    ("3 nov.", "Vote solennel : recettes du budget", GOLD),
    ("4 nov.", "Commission du Sénat : rapport", OLIVE),
    ("9 nov.", "Discussion générale au Sénat", GOLD),
]
byy = chy + 112
for d, t, col in rows6:
    p.text(chx + 22, byy + 22, d, 21, "sans", True, BRICK)
    p.text(chx + 200, byy + 22, t, 21.5, "serif", False, INK)
    byy += 68
p.text(chx + 22, byy + 16, "Source : ordre du jour du Sénat ; NosParlementaires.", 18.5, "sans", False, GREY)
p.text(chx + 22, byy + 44, E["chart_note"], 19, "sans", False, GREY)

e6 = Flow(p, [(COLX[0], CW), (COLX[1], CW)], chy + 436 + 24, 2540, tag="P6-ex")
e6.head(E["head_lire"], 25)
e6.bridge(E["bridge_chart"])
e6.ex("B2", "图表读数", "B", E["n_chart1"],
      "Le 23 octobre, les recettes ont été... A. adoptées · B. rejetées · C. reportées", size=22)
e6.ex("B2", "图表读数", "B", E["n_chart2"],
      "Mardi 3 novembre, on vote... A. les dépenses · B. les recettes · C. les deux", size=22)
e6.ex("B2", "图表读数", "B", E["n_chart3"],
      "La commission du Sénat a préparé son rapport le... A. 9 nov. · B. 4 nov. · C. 23 oct.", size=22)
e6.ex("B2", "图表读数", "A", E["n_chart4"],
      "La discussion générale s'ouvre le... A. 9 nov. · B. 3 nov. · C. 26 nov.", size=22)
e6.ex("B1", "图表读数", "C", E["n_chart5"],
      "Le Sénat examine... A. le texte des députés · B. un texte neuf · C. le texte du gouvernement", size=22)
e6.ex("B1", "图表读数", "B", E["n_chart6"],
      "Le Parlement a cinquante jours, jusqu'au... A. 9 nov. · B. 26 nov. · C. 18 déc.", size=22)
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
g.para("À mon avis, ... · Selon les chiffres, ... · D'après le calendrier, ... Trois portes pour commencer une phrase d'opinion — et une règle : on distingue le programme prévu et le résultat connu.", 23.5)
g.box("LES PHRASES DES JOURNAUX", [
    ("« Le texte part au Sénat. » — " + E["box_senat"], "serif", False, INK, 21.5, 1.42),
    ("« Ce calendrier peut encore bouger. » — " + E["box_bouger"], "serif", False, INK, 21.5, 1.42),
    ("« Les résultats ne sont pas connus. » — " + E["box_connus"], "serif", False, INK, 21.5, 1.42),
])
g.head("IL EST PRÉVU QUE + SUBJONCTIF", 25)
g.para("Après « il est prévu que », le verbe passe au subjonctif : examiner → examine, voter → vote, changer → change. C'est la forme des journaux quand le programme est prévu mais pas encore réalisé.", 23.5)
g.bridge(E["bridge_prevu"])
g.end_report()

g2 = Flow(p, [(COLX[2], CW), (COLX[3], CW)], 1330, 2540, tag="P6-micro")
g2.head(E["head_comp6"], 25)
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
      "Le 23 octobre, les députés ___ les recettes du texte.", size=21.5)
g2.ex("B2", "完成句子", "part", E["n_micro6c"],
      "Le texte ___ au Sénat.", size=21.5)
g2.ex("B1", "完成句子", "peut", E["n_micro6d"],
      "Le calendrier ___ encore bouger.", size=21.5)
g2.ex("B1", "完成句子", "connus", E["n_micro6e"],
      "Les résultats du 3 novembre ne sont pas encore ___.", size=21.5)
g2.box(E["head_3dates"], [
    ("23 oct. — rejet 115–1 des recettes de la Sécu.", "serif", False, INK, 21.5, 1.42),
    ("3 nov. — vote solennel sur les recettes.", "serif", False, INK, 21.5, 1.42),
    ("9 nov. — le Sénat ouvre la discussion.", "serif", False, INK, 21.5, 1.42),
])
g2.head(E["head_debat"], 25)
g2.para("Faut-il annoncer un programme avant les résultats ? Discutez en classe : deux phrases pour, deux phrases contre — en distinguant « prévu » et « décidé ».", 23.5)
g2.bridge(E["bridge_debat6"])
g2.end_report()
p.foot(6)
p.save(f"{OUT}/p6-politique.svg")
print("P6 saved, exercises so far:", len(REG))
