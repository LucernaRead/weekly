# -*- coding: utf-8 -*-
"""W47 FR core VOL.4 — P7. Golden sentences are verbatim from P1–P6."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 7
p = BSPage4()
p.band(E["band_p7"], "Le Lucerna", E["band_p7_sub"])

cA = Flow(p, [(COLX[0], CW)], 200, 1150, tag="P7-A2")
cA.head(E["head_niv_a2"], 27)
cA.head("LE FUTUR PROCHE", 24)
cA.para("aller + infinitif : « Mercredi, le Sénat va voter. » « Nous allons goûter le beaujolais jeudi. » Pour parler d'un futur tout proche, c'est la forme la plus simple.", 22.5)
cA.head("LE PASSÉ COMPOSÉ", 24)
cA.para("« Dimanche 8 novembre, Carlos Alcaraz a battu Ben Shelton 7-6(5), 7-5. » Avec être ou avoir + participe passé : battre → a battu. Le passé composé raconte ce qui est fini. (page 4)", 22.5)
cA.box("LA PHRASE EXEMPLE", [
    ("« Jeudi 19 novembre, à 0 heure, le beaujolais nouveau est arrivé ! » — la phrase du jeudi, à dire à minuit. (page 3)", "serif", False, INK, 21.5, 1.42),
])
cA.end_report()

cB = Flow(p, [(COLX[1], CW)], 200, 1150, tag="P7-B1")
cB.head(E["head_niv_b1"], 27)
cB.head("LE PASSÉ COMPOSÉ, ENCORE", 24)
cB.para("« Dimanche 8 novembre, Carlos Alcaraz a battu Ben Shelton 7-6(5), 7-5. » Le passé composé ferme l'action : battre → a battu. (page 4)", 22.5)
cB.head("LE COMPARATIF", 24)
cB.para("plus / moins / aussi + adjectif (+ que) : « Un débat au Sénat est plus long qu'un concert. » Bon devient meilleur, jamais « plus bon ».", 22.5)
cB.box("LA PHRASE EXEMPLE", [
    ("« Le meilleur déchet est celui qu'on ne produit pas. » (page 5).", "serif", False, INK, 21.5, 1.42),
])
cB.end_report()

# ---- Doré image under the B1 column (measured slot, IT pattern) ----
dy0 = cB.y + 16
print("P7 B1 flow ends y=", cB.y, "dore slot y0=", dy0)
if dy0 + 170 + 80 <= 1150:
    image(p, "dore-hare-frogs.jpg", COLX[1] + 87, dy0, 260, 170)
    caption(p, COLX[1] + 87, dy0 + 170, 260, "Doré illustre La Fontaine.",
            "Gustave Doré (1832-1883), domaine public")
else:
    print("  !! P7 DORE NOSPACE: y0=", dy0)

cC = Flow(p, [(COLX[2], CW), (COLX[3], CW)], 200, 1150, tag="P7-B2")
cC.head(E["head_niv_b2"], 27)
cC.head("IL EST PRÉVU QUE + SUBJONCTIF", 23)
cC.para("« Il est prévu que le Sénat examine le budget mercredi. » Après « il est prévu que », le verbe passe au subjonctif : examiner → examine, voter → vote, changer → change. (page 6)", 22.5)
cC.head("SI + CONDITIONNEL", 24)
cC.para("« Si tu venais dimanche, tu verrais les finales. » Si + imparfait, puis conditionnel : l'hypothèse, en une phrase. Pour le réel, on reste au présent : si la première partie est rejetée, tout le texte tombe.", 22.5)
cC.box("LA PHRASE EXEMPLE", [
    ("« La première partie est rejetée, et tout le texte tombe en première lecture. » — la phrase courte des journaux, à retenir telle quelle.", "serif", False, INK, 21.5, 1.42),
])
cC.end_report()

cD = Flow(p, [(COLX[3], CW)], 200, 1150, tag="P7-outils")
cD.head(E["head_outils"], 27)
cD.para(E["outils_intro"], 22.5)
cD.para("A2 — « Jeudi 19 novembre, à 0 heure, le beaujolais nouveau est arrivé ! »", 22.5, "serif", True, OLIVE)
cD.para("B1 — « Le meilleur déchet est celui qu'on ne produit pas. »", 22.5, "serif", True, OLIVE)
cD.para("B2 — « La première partie est rejetée, et tout le texte tombe en première lecture. »", 22.5, "serif", True, OLIVE)
cD.para("Gardez aussi le réflexe du journal : chaque phrase de la semaine vient d'un article de ce numéro. Relisez l'article, la phrase devient facile.", 22.5)
cD.bridge(E["bridge_outils"])
cD.end_report()

py = 1160
p.hline(MX, RIGHT, py - 14, OLIVE, 2)
p.text(MX, py + 26, E["head_phrases"], 27, "sans", True, OLIVE)
p.text(RIGHT, py + 26, E["phrases_sub"], 20, "sans", False, GREY, anchor="end")
pf = Flow(p, [(COLX[i], CW) for i in range(4)], py + 52, 1830, tag="P7-phrases")
phrases = [
    ("« Dimanche 8 novembre, Carlos Alcaraz a battu Ben Shelton 7-6(5), 7-5, en finale du Rolex Paris Masters, à Nanterre. » (page 1)",
     E["gp1"], "A2", "Alcaraz a ___ (battre) Shelton.", "battu", E["n_gp1"]),
    ("« Jeudi 19 novembre, à 0 heure, le beaujolais nouveau est arrivé ! » (page 3)",
     E["gp2"], "B1", "Le beaujolais nouveau ___ (arriver) jeudi.", "est arrivé", E["n_gp2"]),
    ("« C'est le mercredi des sorties en France : un jour pour voter le matin, un film le soir. » (page 2)",
     E["gp3"], "A2", "Le Sénat ___ (voter) mercredi.", "vote", E["n_gp3"]),
    ("« Et dimanche 22 novembre, la semaine se termine en beauté : les finales de Turin, et le retour de la Ligue 1 — Marseille reçoit Le Mans à 20 h 45. » (page 2)",
     E["gp4"], "A2", "La semaine se termine en ___ (beau).", "beauté", E["n_gp4"]),
    ("« Comme dit l'ADEME : le meilleur déchet est celui qu'on ne produit pas. » (page 5)",
     E["gp5"], "B1", "Le meilleur déchet est celui qu'on ne ___ (produire) pas.", "produit", E["n_gp5"]),
    ("« Mercredi 18 novembre, seize films sortent dans les salles de cinéma en France. » (page 5)",
     E["gp6"], "A2", "Mercredi, seize films ___ (sortir) dans les salles de cinéma.", "sortent", E["n_gp6"]),
    ("« La première partie est rejetée, et tout le texte tombe en première lecture. » (page 6)",
     E["gp7"], "B2", "La première partie est ___ (rejeter).", "rejetée", E["n_gp7"]),
    ("« Une semaine en trois temps : voter, fêter, jouer. » (page 1)",
     E["gp8"], "A2", "Une semaine en trois temps : voter, fêter et ___.", "jouer", E["n_gp8"]),
]
for sent, point, lv, q, key, note in phrases:
    pf.para(sent, 22, "serif", True, INK, 1.4, 4)
    pf.bridge(point, 19.5, 5)
    pf.ex(lv, "跟练", key, note, q, size=22)
pf.end_report()

by7 = 1870
p.hline(MX, RIGHT, by7 - 14, OLIVE, 2)
cf = Flow(p, [(COLX[0], CW), (COLX[1], CW)], by7 + 8, 2268, tag="P7-clinic")
cf.head(E["head_clinic"], 22)
cf.bridge(E["bridge_clinic"])
cf.ex("A2", "改错", "Alcaraz a battu Shelton.", E["n_cl1"],
      "✗ « Alcaraz a battre Shelton. »", instr=E["instr_correct"], size=22.5)
cf.ex("B1", "改错", "Le Sénat vote mercredi.", E["n_cl2"],
      "✗ « Le Sénat votent mercredi. »", instr=E["instr_correct"], size=22.5)
cf.ex("B2", "改错", "Il est prévu que le Sénat examine le texte.", E["n_cl3"],
      "✗ « Il est prévu que le Sénat va examiner le texte. »", instr=E["instr_correct"], size=22.5)
cf.ex("B1", "改错", "Le beaujolais nouveau arrive jeudi 19 novembre.", E["n_cl4"],
      "✗ « Le beaujolais nouveau arrive vendredi 20 novembre. »", instr=E["instr_correct"], size=22.5)
cf.end_report()

rx, rw = span_x(2, 2)
p.rect(rx, by7 + 8, rw, 380, fill=BOX)
p.text(rx + 24, by7 + 48, E["head_courrier"], 24, "sans", True, OLIVE)
p.para(rx + 24, by7 + 86, "« Mon dimanche 22 novembre : le matin, j'ai regardé les finales de Turin à la télévision ; l'après-midi, j'ai marché jusqu'au parc et j'ai lu vingt pages. » — Exemple de la rédaction (ce texte n'est pas une lettre de lecteur).", 21, "serif", False, INK, rw - 48, 1.42)
p.para(rx + 24, by7 + 196, E["courrier_comment"], 20, "sans", False, GREY, rw - 48, 1.4)
p.para(rx + 24, by7 + 272, "Note de la rédaction : aucun texte du VOL.4 n'était arrivé au moment de mettre sous presse. Le VOL.5 reprendra la promesse.", 20, "serif", False, INK, rw - 48, 1.4)
p.para(rx + 24, by7 + 336, E["courrier_disclosure"], 19.5, "sans", False, GREY, rw - 48, 1.4)
ty7 = by7 + 8 + 380 + 12
p.rect(rx, ty7, rw, 2560 - ty7, fill=CLOTH)
p.text(rx + 24, ty7 + 46, E["head_teaser"], 24, "sans", True, ONCLOTH)
p.para(rx + 24, ty7 + 84, "Dimanche 22 novembre : les finales de Turin. Lundi 23 novembre : les résultats des Bleus et de la 11e journée. Vendredi 27 novembre : le Black Friday. Le résultat du vote du Sénat, et vos lettres, enfin !", 21, "serif", False, "#cac8ba", rw - 48, 1.45)
p.para(rx + 24, ty7 + 196, E["teaser_note"], 20, "sans", False, GOOSE, rw - 48, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-langue.svg")
print("P7 saved, exercises so far:", len(REG))
