# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LANGUE EN MAIN　LA LENGUA EN MANO", "Le Lucerna", "A2 → B2　Les phrases de la semaine　FRASES DE LA SEMANA")

# --- three level columns ---
cA = Flow(p, [(COLX[0], CW)], 200, 1150, tag="P7-A2")
cA.head("NIVEAU A2　NIVEL BÁSICO", 27)
cA.head("DIRE L'HEURE", 24)
cA.para("Il est trois heures. · Il est sept heures et demie. · Il est midi moins le quart. On dit toujours « Il est » + l'heure — jamais « c'est ». (page 2)", 22.5)
cA.head("LE FUTUR PROCHE", 24)
cA.para("aller + infinitif : « Ce soir, on va reculer les horloges. » « Dimanche, les élèves vont dormir une heure de plus. » Pour parler d'un futur tout proche, c'est la forme la plus simple.", 22.5)
cA.box("LA PHRASE EXEMPLE", [
    ("« À trois heures, il sera deux heures. » — la phrase du week-end, à dire dimanche à voix haute.", "serif", False, INK, 21.5, 1.42),
])
cA.end_report()

cB = Flow(p, [(COLX[1], CW)], 200, 1150, tag="P7-B1")
cB.head("NIVEAU B1　NIVEL INTERMEDIO", 27)
cB.head("LE COMPARATIF", 24)
cB.para("plus / moins / aussi + adjectif + que : « Wemby est plus grand que les autres. » « Ce sondage est meilleur que le précédent » — bon devient meilleur, jamais « plus bon ».", 22.5)
cB.head("DEPUIS + PRÉSENT", 24)
cB.para("« Les élèves sont en vacances depuis samedi. » Pour une action qui commence dans le passé et continue : présent + depuis. Attention : pas de passé composé ici — le verbe reste au présent.", 22.5)
cB.box("LA PHRASE EXEMPLE", [
    ("« Il gagne deux points, elle en perd trois. » — le comparatif vit dans les chiffres des sondages (page 6).", "serif", False, INK, 21.5, 1.42),
])
cB.end_report()

cC = Flow(p, [(COLX[2], CW), (COLX[3], CW)], 200, 1150, tag="P7-B2")
cC.head("NIVEAU B2　DESAFÍO", 27)
cC.head("EXPRIMER UNE OPINION", 24)
cC.para("À mon avis, ... · Selon les chiffres, ... · D'après ce sondage, ... Pour commencer une phrase d'opinion, ces trois portes sont toujours ouvertes.", 22.5)
cC.head("IL SEMBLE QUE + SUBJONCTIF", 24)
cC.para("« Il semble que la candidate soit en tête. » Après « il semble que », le verbe passe au subjonctif : être → soit, avoir → ait, voter → vote. C'est la forme des journaux sérieux.", 22.5)
cC.box("LA PHRASE EXEMPLE", [
    ("« Si l'élection avait lieu dimanche, pour qui voteriez-vous ? » — si + imparfait, réponse au conditionnel : la phrase signature des sondages.", "serif", False, INK, 21.5, 1.42),
])
cC.end_report()

cD = Flow(p, [(COLX[3], CW)], 200, 1150, tag="P7-outils")
cD.head("BOÎTE À OUTILS　RECURSOS", 27)
cD.para("Trois phrases à garder dans la poche, une pour chaque niveau :", 22.5)
cD.para("A2 — « Il est dix heures moins le quart. »", 22.5, "serif", True, OLIVE)
cD.para("B1 — « Les vacances commencent depuis samedi... » Non ! « Je suis en vacances depuis samedi. »", 22.5)
cD.para("B2 — « Selon les chiffres, la candidate devance son rival. »", 22.5, "serif", True, OLIVE)
cD.para("Gardez aussi le réflexe du journal : chaque phrase de la semaine vient d'un article de ce numéro. Relisez l'article, la phrase devient facile.", 22.5)
cD.expl("Tres frases para llevar, una por nivel. Todas las frases de la semana salen de los artículos de este número: relee el artículo y la frase se vuelve fácil.")
cD.end_report()

# --- phrases de la semaine ---
py = 1210
p.hline(MX, RIGHT, py - 14, OLIVE, 2)
p.text(MX, py + 26, "LES PHRASES DE LA SEMAINE　FRASES DE LA SEMANA", 27, "sans", True, OLIVE)
p.text(RIGHT, py + 26, "Un punto de gramática y una pregunta por frase　Soluciones en la página 8", 20, "sans", False, GREY, anchor="end")
pf = Flow(p, [(COLX[i], CW) for i in range(4)], py + 52, 1830, tag="P7-phrases")
phrases = [
    ("« À trois heures, il sera deux heures. » (page 2)",
     "Gramática — futur simple: el futuro de être es sera.",
     "B1", "Demain, il ___ (être) trop tard pour téléphoner.", "sera", "être → futur : sera"),
    ("« Les élèves sont en vacances depuis samedi. » (page 2)",
     "Gramática — depuis + presente: desde que… (la acción continúa).",
     "B1", "Nous apprenons le français ___ 2024.", "depuis", "para lo que dura hasta hoy: depuis"),
    ("« On n'offre jamais de chrysanthèmes pour un anniversaire. » (page 3)",
     "Gramática — ne...jamais + de: nunca se regala (crisantemos en un cumpleaños).",
     "B1", "Il ne boit ___ de café : il déteste ça.", "jamais", "ne...jamais = nunca"),
    ("« Wembanyama est plus grand que la plupart des joueurs. » (page 4)",
     "Gramática — comparatif: plus + adjetivo + que.",
     "A2", "Ce match est ___ (long) que prévu.", "plus long", "long → plus long que"),
    ("« Les fans attendent ce jeu depuis des années. » (page 5)",
     "Gramática — attendre lleva complemento directo, sin preposición.",
     "A2", "Ils attendent ___ bus devant la gare.", "le", "attendre le bus"),
    ("« Si l'élection avait lieu dimanche, pour qui voteriez-vous ? » (page 6)",
     "Gramática — si + imperfecto → condicional: la hipótesis.",
     "B2", "Si j'étais président, je ___ (changer) les horaires.", "changerais", "si+imparfait → conditionnel"),
    ("« On gagne une heure de sommeil. » (page 1)",
     "Gramática — gagner + cantidad: ganar (una hora de más).",
     "A2", "Avec ce train rapide, on gagne ___ heure.", "une", "une heure de sommeil"),
]
for sent, point, lv, q, key, note in phrases:
    pf.para(sent, 22, "serif", True, INK, 1.4, 4)
    pf.expl(point, 19.5, 5)
    pf.ex(lv, "跟练", key, note, q, size=22)
pf.end_report()

# --- bottom: clinic (left) + courrier & teaser (right) ---
by7 = 1870
p.hline(MX, RIGHT, by7 - 14, OLIVE, 2)
cf = Flow(p, [(COLX[0], CW), (COLX[1], CW)], by7 + 8, 2268, tag="P7-clinic")
cf.head("CLINIQUE DES ERREURS　CLÍNICA", 25)
cf.expl("Cada frase tiene un error: encuéntralo y corrígelo.")
cf.ex("A2", "改错", "J'ai vingt ans.", "la edad se dice con avoir, no con être",
      "✗ « Je suis vingt ans. »", instr="Corrige", size=22.5)
cf.ex("B1", "改错", "J'attends le bus.", "attendre lleva complemento directo, sin preposición",
      "✗ « J'attends pour le bus. »", instr="Corrige", size=22.5)
cf.ex("A2", "改错", "Il est trois heures.", "para decir la hora se usa Il est",
      "✗ « C'est trois heures. »", instr="Corrige", size=22.5)
cf.ex("B1", "改错", "Elle offre des roses pour mon anniversaire.", "para regalar, rosas; crisantemos, no",
      "✗ « Elle offre des chrysanthèmes pour mon anniversaire. »", instr="Corrige", size=22.5)
cf.end_report()

rx, rw = span_x(2, 2)
p.rect(rx, by7 + 8, rw, 300, fill=BOX)
p.text(rx + 24, by7 + 48, "LE COURRIER DES LECTEURS　EL RINCÓN DE LOS LECTORES", 24, "sans", True, OLIVE)
p.para(rx + 24, by7 + 86, "« En automne, je me suis couché de bonne heure, comme Proust. » — L. M., lectrice fidèle (composition du VOL.1, « Mon automne »)", 21.5, "serif", False, INK, rw - 48, 1.42)
p.para(rx + 24, by7 + 176, "Comentario de Xiaomo — El passé composé hace eco a la frase célebre de Proust, y « de bonne heure » suena muy natural. Un detalle: L. M. es una lectora, así que couché lleva una e más: couchée. En el próximo número, este rincón comentará los textos enviados para el VOL.2: el tema está en la página 8.", 20, "sans", False, GREY, rw - 48, 1.42)
ty7 = by7 + 332
p.rect(rx, ty7, rw, 2560 - ty7, fill=CLOTH)
p.text(rx + 24, ty7 + 46, "LA SEMAINE PROCHAINE　VOL.3 LA SEMANA QUE VIENE", 24, "sans", True, ONCLOTH)
p.para(rx + 24, ty7 + 84, "Samedi 31 octobre : Halloween en France, en direct. Dimanche 1er novembre : la Toussaint, le jour des fleurs. Et la première semaine à l'heure d'hiver : la nuit tombe à 18 heures — que lit-on quand il fait nuit tôt ?", 21.5, "serif", False, "#cac8ba", rw - 48, 1.45)
p.para(rx + 24, ty7 + 218, "El sábado que viene es Halloween y el domingo, Todos los Santos; en la primera semana con horario de invierno, anochece cada vez más temprano.", 20, "sans", False, GOOSE, rw - 48, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-langue.svg")
print("P7 saved, exercises so far:", len(REG))
