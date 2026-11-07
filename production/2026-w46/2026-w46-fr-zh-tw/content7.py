# -*- coding: utf-8 -*-
"""W46 FR core VOL.4 — P7. Golden sentences are verbatim from P1–P6."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-fr-zh-tw/svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 7
p = BSPage4()
p.band(E["band_p7"], "Le Lucerna", E["band_p7_sub"])

cA = Flow(p, [(COLX[0], CW)], 200, 1150, tag="P7-A2")
cA.head(E["head_niv_a2"], 27)
cA.head("LE FUTUR PROCHE", 24)
cA.para("aller + infinitif : « Le Sénat va ouvrir la discussion lundi. » « Nous allons visiter Paris Photo jeudi. » Pour parler d'un futur tout proche, c'est la forme la plus simple.", 22.5)
cA.head("LE PASSÉ COMPOSÉ", 24)
cA.para("« Le 11 novembre 1918, à 11 heures, les armes se sont tues. » Avec être ou avoir + participe passé : se taire → se sont tues. Le passé composé raconte ce qui est fini. (page 3)", 22.5)
cA.box("LA PHRASE EXEMPLE", [
    ("« Lundi 9 novembre, le Sénat ouvre la discussion sur le budget de la Sécurité sociale pour 2027. » — la phrase du lundi, à dire le matin. (page 1)", "serif", False, INK, 21.5, 1.42),
])
cA.end_report()

cB = Flow(p, [(COLX[1], CW)], 200, 1150, tag="P7-B1")
cB.head(E["head_niv_b1"], 27)
cB.head("LE PASSÉ COMPOSÉ, ENCORE", 24)
cB.para("« La flamme du Soldat inconnu brûle sous l'Arc de Triomphe depuis 1923, sans jamais s'éteindre. » Depuis + présent : une action qui dure encore. Le passé composé, lui, ferme l'action : « les armes se sont tues ». (pages 2 et 3)", 22.5)
cB.head("LE COMPARATIF", 24)
cB.para("plus / moins / aussi + adjectif (+ que) : « Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ? » — deux comparatifs opposés par ou ; bon devient meilleur, jamais « plus bon ».", 22.5)
cB.box("LA PHRASE EXEMPLE", [
    ("« Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ? » — le comparatif du débat sportif (page 4).", "serif", False, INK, 21.5, 1.42),
])
cB.end_report()

cC = Flow(p, [(COLX[2], CW), (COLX[3], CW)], 200, 1150, tag="P7-B2")
cC.head(E["head_niv_b2"], 27)
cC.head("IL EST PRÉVU QUE + SUBJONCTIF", 24)
cC.para("« Il est prévu que le Sénat examine le budget lundi. » Après « il est prévu que », le verbe passe au subjonctif : examiner → examine, voter → vote, changer → change. (page 6)", 22.5)
cC.head("SI + CONDITIONNEL", 24)
cC.para("« Si la première partie est rejetée, les amendements votés en séance tombent. » Si + présent, puis présent ou futur : la règle du budget, en une phrase. Pour l'hypothèse, on passe au conditionnel : si j'étais libre, j'irais à Dieppe.", 22.5)
cC.box("LA PHRASE EXEMPLE", [
    ("« Le texte part au Sénat. » — la phrase courte des journaux, à retenir telle quelle.", "serif", False, INK, 21.5, 1.42),
])
cC.end_report()

cD = Flow(p, [(COLX[3], CW)], 200, 1150, tag="P7-outils")
cD.head(E["head_outils"], 27)
cD.para(E["outils_intro"], 22.5)
cD.para("A2 — « Lundi 9 novembre, le Sénat ouvre la discussion sur le budget de la Sécurité sociale pour 2027. »", 22.5, "serif", True, OLIVE)
cD.para("B1 — « Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ? »", 22.5, "serif", True, OLIVE)
cD.para("B2 — « Le texte part au Sénat. »", 22.5, "serif", True, OLIVE)
cD.para("Gardez aussi le réflexe du journal : chaque phrase de la semaine vient d'un article de ce numéro. Relisez l'article, la phrase devient facile.", 22.5)
cD.bridge(E["bridge_outils"])
cD.end_report()

py = 1160
p.hline(MX, RIGHT, py - 14, GOLD, 2)
p.text(MX, py + 26, E["head_phrases"], 27, "sans", True, OLIVE)
p.text(RIGHT, py + 26, E["phrases_sub"], 20, "sans", False, GREY, anchor="end")
pf = Flow(p, [(COLX[i], CW) for i in range(4)], py + 52, 1830, tag="P7-phrases")
phrases = [
    ("« Lundi 9 novembre, le Sénat ouvre la discussion sur le budget de la Sécurité sociale pour 2027. » (page 1)",
     E["gp1"], "A2", "Lundi, le Sénat ___ (ouvrir) la discussion.", "ouvre", E["n_gp1"]),
    ("« Le 11 novembre 1918, à 11 heures, les armes se sont tues. » (page 3)",
     E["gp2"], "B1", "En 1918, les armes se sont ___ (taire).", "tues", E["n_gp2"]),
    ("« La flamme du Soldat inconnu brûle sous l'Arc de Triomphe depuis 1923, sans jamais s'éteindre. » (page 2)",
     E["gp3"], "B1", "La flamme ___ (brûler) depuis 1923.", "brûle", E["n_gp3"]),
    ("« Une semaine en trois temps : débattre, se souvenir, fêter. » (page 1)",
     E["gp4"], "A2", "Trois temps : débattre, se souvenir et ___.", "fêter", E["n_gp4"]),
    ("« Le hareng, « poisson roi », et la coquille Saint-Jacques, emblème du port, sont les rois de la fête. » (page 3)",
     E["gp5"], "A2", "Le hareng est le « poisson ___ ».", "roi", E["n_gp5"]),
    ("« Ce numéro ne les invente pas — les résultats du week-end seront dans le VOL.5, avec le nom du vainqueur. » (page 4)",
     E["gp6"], "B2", "Les résultats ___ (être) dans le VOL.5.", "seront", E["n_gp6"]),
    ("« Regarder une photo, c'est déjà lire — et Paris Photo en offre des centaines. » (page 2)",
     E["gp7"], "A2", "Regarder une photo, c'est déjà ___.", "lire", E["n_gp7"]),
    ("« Le texte qu'ils examinent est celui du gouvernement, dans sa version initiale. » (page 6)",
     E["gp8"], "B2", "Le texte est celui du ___.", "gouvernement", E["n_gp8"]),
]
for sent, point, lv, q, key, note in phrases:
    pf.para(sent, 22, "serif", True, INK, 1.4, 4)
    pf.bridge(point, 19.5, 5)
    pf.ex(lv, "跟练", key, note, q, size=22)
pf.end_report()

by7 = 1870
p.hline(MX, RIGHT, by7 - 14, GOLD, 2)
cf = Flow(p, [(COLX[0], CW), (COLX[1], CW)], by7 + 8, 2268, tag="P7-clinic")
cf.head(E["head_clinic"], 25)
cf.bridge(E["bridge_clinic"])
cf.ex("A2", "改错", "La flamme ne s'éteint jamais.", E["n_cl1"],
      "✗ « La flamme s'éteint jamais. »", instr=E["instr_correct"], size=22.5)
cf.ex("B1", "改错", "Les sénateurs examinent le texte lundi.", E["n_cl2"],
      "✗ « Les sénateurs examine le texte lundi. »", instr=E["instr_correct"], size=22.5)
cf.ex("B2", "改错", "Il est prévu que le Sénat examine le texte.", E["n_cl3"],
      "✗ « Il est prévu que le Sénat examines le texte. »", instr=E["instr_correct"], size=22.5)
cf.ex("B1", "改错", "La foire a lieu samedi 14 novembre.", E["n_cl4"],
      "✗ « La foire a lieu samedi 15 novembre. »", instr=E["instr_correct"], size=22.5)
cf.end_report()

rx, rw = span_x(2, 2)
p.rect(rx, by7 + 8, rw, 380, fill=BOX, stroke=LINE, sw=1.4)
p.text(rx + 24, by7 + 48, E["head_courrier"], 24, "sans", True, OLIVE)
p.para(rx + 24, by7 + 86, "« Mon mercredi 11 novembre : le matin, j'ai regardé la cérémonie à la télévision ; l'après-midi, j'ai marché jusqu'au monument aux morts et j'ai lu vingt pages. » — Exemple de la rédaction (ce texte n'est pas une lettre de lecteur).", 21, "serif", False, INK, rw - 48, 1.42)
p.para(rx + 24, by7 + 196, E["courrier_comment"], 20, "sans", False, GREY, rw - 48, 1.4)
p.para(rx + 24, by7 + 272, "Note de la rédaction : aucun texte du VOL.3 n'était arrivé au moment de mettre sous presse. Le VOL.5 reprendra la promesse.", 20, "serif", False, INK, rw - 48, 1.4)
p.para(rx + 24, by7 + 336, E["courrier_disclosure"], 19.5, "sans", False, GREY, rw - 48, 1.4)
ty7 = by7 + 8 + 380 + 12
p.rect(rx, ty7, rw, 2540 - ty7, fill=DARK)
p.text(rx + 24, ty7 + 46, E["head_teaser"], 24, "sans", True, "#f3edda")
p.para(rx + 24, ty7 + 84, "Mercredi 18 novembre : le vote solennel du Sénat est prévu. Jeudi 19 novembre : le beaujolais nouveau arrive. Dimanche 22 novembre : les finales de Turin. Les résultats du Masters, et vos lettres, enfin !", 21, "serif", False, "#e8dfc8", rw - 48, 1.45)
p.para(rx + 24, ty7 + 196, E["teaser_note"], 20, "sans", False, "#b3a06a", rw - 48, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-langue.svg")
print("P7 saved, exercises so far:", len(REG))
