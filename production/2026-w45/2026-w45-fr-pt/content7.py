# -*- coding: utf-8 -*-
"""W45 FR core VOL.2 — P7."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 7
p = BSPage4()
p.band("LANGUE EN MAIN　LÍNGUA", "Le Lucerna", "A2 → B2　Les phrases de la semaine　FRASES DA SEMANA")

cA = Flow(p, [(COLX[0], CW)], 200, 1150, tag="P7-A2")
cA.head("NIVEAU A2　NÍVEL BÁSICO", 27)
cA.head("REPRENDRE", 24)
cA.para("« Le lundi 2 novembre, on reprend les cours. » Reprendre, c'est recommencer après une pause : on reprend les cours, on reprend le travail, on reprend la lecture. (page 2)", 22.5)
cA.head("LE FUTUR PROCHE", 24)
cA.para("aller + infinitif : « Ce soir, on va préparer le cartable. » « Lundi, les élèves vont raconter leurs vacances. » Pour parler d'un futur tout proche, c'est la forme la plus simple.", 22.5)
cA.box("LA PHRASE EXEMPLE", [
    ("« Le lundi 2 novembre, on reprend les cours. » — la phrase de la rentrée, à dire lundi matin.", "serif", False, INK, 21.5, 1.42),
])
cA.end_report()

cB = Flow(p, [(COLX[1], CW)], 200, 1150, tag="P7-B1")
cB.head("NIVEAU B1　INTERMEDIÁRIO", 27)
cB.head("LE PASSÉ COMPOSÉ", 24)
cB.para("« Les enfants se sont déguisés samedi. » « Les cimetières se sont remplis de fleurs. » Avec se + être + participe passé : attention à l'accord avec le sujet : déguisés, remplis. (page 3)", 22.5)
cB.head("LE COMPARATIF", 24)
cB.para("plus / moins / aussi + adjectif (+ que) : « Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ? » « Ce match est aussi important que la finale. » — deux comparatifs opposés par ou ; bon devient meilleur, jamais « plus bon ».", 22.5)
cB.box("LA PHRASE EXEMPLE", [
    ("« Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ? » — le comparatif du débat sportif (page 4).", "serif", False, INK, 21.5, 1.42),
])
cB.end_report()

cC = Flow(p, [(COLX[2], CW), (COLX[3], CW)], 200, 1150, tag="P7-B2")
cC.head("NIVEAU B2　DESAFIO", 27)
cC.head("IL EST PRÉVU QUE + SUBJONCTIF", 24)
cC.para("« Il est prévu que l'Assemblée examine la Culture mardi. » Après « il est prévu que », le verbe passe au subjonctif : examiner → examine, voter → vote, changer → change. (page 6)", 22.5)
cC.head("EXPRIMER L'ATTENTE", 24)
cC.para("« On ne connaît pas encore les finalistes. » « Les résultats seront connus samedi soir. » Pour parler d'un avenir incertain, on distingue le programme prévu et le résultat connu — jamais l'inverse.", 22.5)
cC.box("LA PHRASE EXEMPLE", [
    ("« Ce calendrier peut encore bouger. » — pouvoir + infinitif : la phrase de prudence des journaux.", "serif", False, INK, 21.5, 1.42),
])
cC.end_report()

cD = Flow(p, [(COLX[3], CW)], 200, 1150, tag="P7-outils")
cD.head("BOÎTE À OUTILS　PARA LEVAR", 27)
cD.para("Trois phrases à garder dans la poche, une pour chaque niveau :", 22.5)
cD.para("A2 — « Le lundi 2 novembre, on reprend les cours. »", 22.5, "serif", True, OLIVE)
cD.para("B1 — « Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ? »", 22.5, "serif", True, OLIVE)
cD.para("B2 — « Il est prévu que l'Assemblée examine la Culture mardi. »", 22.5, "serif", True, OLIVE)
cD.para("Gardez aussi le réflexe du journal : chaque phrase de la semaine vient d'un article de ce numéro. Relisez l'article, la phrase devient facile.", 22.5)
cD.bridge("Caixa de ferramentas: três frases para levar, uma por nível; todas as frases vêm dos artigos deste número — releiam o artigo e a frase fica.")
cD.end_report()

py = 1160
p.hline(MX, RIGHT, py - 14, OLIVE, 2)
p.text(MX, py + 26, "LES PHRASES DE LA SEMAINE　FRASES DA SEMANA", 27, "sans", True, OLIVE)
p.text(RIGHT, py + 26, "Cada frase, um ponto de gramática + um exercício　respostas na página 8", 20, "sans", False, GREY, anchor="end")
pf = Flow(p, [(COLX[i], CW) for i in range(4)], py + 52, 1830, tag="P7-phrases")
phrases = [
    ("« Le lundi 2 novembre, on reprend les cours. » (page 2)",
     "Ponto de gramática: reprendre — voltar às aulas, recomeçar (após uma pausa).",
     "A2", "Après les vacances, on ___ (reprendre) les cours.", "reprend", "on → reprend"),
    ("« On ne connaît pas encore les finalistes. » (page 1)",
     "Ponto de gramática: ne...pas encore — ainda não.",
     "B1", "Il ne fait pas ___ nuit : il est 15 heures.", "encore", "pas encore = ainda não"),
    ("« Les cimetières se sont remplis de chrysanthèmes. » (page 3)",
     "Ponto de gramática: passé composé reflexo — se + être + particípio passado.",
     "B1", "Les enfants se sont ___ (déguiser) samedi.", "déguisés", "se déguiser → se sont déguisés"),
    ("« Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ? » (page 4)",
     "Ponto de gramática: comparatif — plus + adjetivo; ou opõe os dois termos.",
     "B1", "La finale est ___ (excitante) !", "plus excitante", "plus + adjetivo"),
    ("« Le festival se promène dans Paris. » (page 5)",
     "Ponto de gramática: se promener — verbo reflexo, passear, andar.",
     "A2", "Le dimanche, nous nous ___ (promener) au parc.", "promenons", "se promener → nous promenons"),
    ("« Ce calendrier peut encore bouger. » (page 6)",
     "Ponto de gramática: pouvoir + infinitivo — poder, ser possível.",
     "B2", "Le programme ___ (pouvoir) changer demain.", "peut", "pouvoir → peut"),
    ("« Ce week-end, tout se joue. » (page 1)",
     "Ponto de gramática: se jouer — decidir o resultado, acontecer (verbo reflexo).",
     "A2", "La finale se ___ (jouer) dimanche.", "joue", "se jouer → se joue"),
    ("« Les jeunes créateurs y rencontrent leur public, en vrai. » (page 5)",
     "Ponto de gramática: rencontrer — encontrar o público; y refere-se ao lugar.",
     "A2", "Ils ___ (rencontrer) leur public.", "rencontrent", "rencontrer → rencontrent"),
]
for sent, point, lv, q, key, note in phrases:
    pf.para(sent, 22, "serif", True, INK, 1.4, 4)
    pf.bridge(point, 19.5, 5)
    pf.ex(lv, "Prática", key, note, q, size=22)
pf.end_report()

by7 = 1870
p.hline(MX, RIGHT, by7 - 14, OLIVE, 2)
cf = Flow(p, [(COLX[0], CW), (COLX[1], CW)], by7 + 8, 2268, tag="P7-clinic")
cf.head("CLINIQUE DES ERREURS　CLÍNICA", 25)
cf.bridge("Cada frase tem um erro: encontrem-no e corrijam-no.")
cf.ex("A2", "Correção de erros", "On n'offre jamais de chrysanthèmes pour un anniversaire.", "jamais + de: na negação, des passa a de",
      "✗ « On offre des chrysanthèmes pour un anniversaire. »", instr="Correção de erros", size=22.5)
cf.ex("A2", "Correção de erros", "Les jeunes créateurs y rencontrent leur public, en vrai.", "Concordância: créateurs (plural) → rencontrent, não rencontre",
      "✗ « Les jeunes créateurs y rencontre leur public, en vrai. »", instr="Correção de erros", size=22.5)
cf.ex("B2", "Correção de erros", "Il est prévu que l'Assemblée examine la Culture mardi.", "Subjuntivo: il examine, sem s",
      "✗ « Il est prévu que l'Assemblée examines la Culture. »", instr="Correção de erros", size=22.5)
cf.ex("B1", "Correção de erros", "La finale a lieu dimanche 8 novembre.", "Facto: a final é no dia 8, não no dia 7",
      "✗ « La finale a lieu dimanche 7 novembre. »", instr="Correção de erros", size=22.5)
cf.end_report()

rx, rw = span_x(2, 2)
p.rect(rx, by7 + 8, rw, 380, fill=BOX)
p.text(rx + 24, by7 + 48, "LE COURRIER DES LECTEURS　CARTAS DOS LEITORES", 24, "sans", True, OLIVE)
p.para(rx + 24, by7 + 86, "« Mon week-end de novembre : samedi, j'ai regardé un match à la télévision ; dimanche, j'ai cuisiné une soupe et j'ai lu vingt pages. » — Exemple de la rédaction (ce texte n'est pas une lettre de lecteur).", 21, "serif", False, INK, rw - 48, 1.42)
p.para(rx + 24, by7 + 196, "Xiao Mo comenta (texto-exemplo): o passé composé está seguro na narrativa do fim de semana; o ponto e vírgula liga os dois dias e vale a pena imitar. No próximo número, a secção comentará textos reais.", 20, "sans", False, GREY, rw - 48, 1.4)
p.para(rx + 24, by7 + 272, "Note de la rédaction : aucun texte du VOL.2 n'était arrivé au moment de mettre sous presse (le numéro W44 n'a pas paru). Le VOL.4 reprendra la promesse.", 20, "serif", False, INK, rw - 48, 1.4)
p.para(rx + 24, by7 + 336, "Nota da redação: sem cartas nem redações do VOL.2 até ao fecho (o W44 não saiu) — exemplo identificado. Enviem-nos cartas e as melhores redações da página 8 para o VOL.4!", 19.5, "sans", False, GREY, rw - 48, 1.4)
ty7 = by7 + 8 + 380 + 12
p.rect(rx, ty7, rw, 2560 - ty7, fill=CLOTH)
p.text(rx + 24, ty7 + 46, "LA SEMAINE PROCHAINE　PRÓXIMA SEMANA　VOL.4", 24, "sans", True, ONCLOTH)
p.para(rx + 24, ty7 + 84, "Lundi 9 novembre : le Sénat examine le budget de la Sécurité sociale. Mercredi 11 novembre : l'Armistice, un jour de mémoire. Samedi 14 et dimanche 15 novembre : la Foire aux harengs et à la coquille Saint-Jacques, à Dieppe. Et vos lettres, enfin !", 21, "serif", False, "#cac8ba", rw - 48, 1.45)
p.para(rx + 24, ty7 + 196, "Na próxima semana: o Senado e o orçamento da Segurança Social, 11 de novembro, Dia do Armistício, feira de Dieppe — e as vossas cartas, finalmente!", 20, "sans", False, GOOSE, rw - 48, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-langue.svg")
print("P7 saved, exercises so far:", len(REG))
