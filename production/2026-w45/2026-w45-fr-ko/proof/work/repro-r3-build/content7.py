# -*- coding: utf-8 -*-
"""W45 FR core VOL.3 — P7."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/fr-ko-proof/work/repro-r3-edition/svg"
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 7
p = BSPage4()
p.band("LANGUE EN MAIN · 정독", "Le Lucerna", "A2 → B2 · Les phrases de la semaine · 이번 주 문장")

cA = Flow(p, [(COLX[0], CW)], 200, 1150, tag="P7-A2")
cA.head("NIVEAU A2 · 기초", 27)
cA.head("REPRENDRE", 24)
cA.para("« Le lundi 2 novembre, on reprend les cours. » Reprendre, c'est recommencer après une pause : on reprend les cours, on reprend le travail, on reprend la lecture. (page 2)", 22.5)
cA.head("LE FUTUR PROCHE", 24)
cA.para("aller + infinitif : « Ce soir, on va préparer le cartable. » « Lundi, les élèves vont raconter leurs vacances. » Pour parler d'un futur tout proche, c'est la forme la plus simple.", 22.5)
cA.box("LA PHRASE EXEMPLE", [
    ("« Le lundi 2 novembre, on reprend les cours. » — la phrase de la rentrée, à dire lundi matin.", "serif", False, INK, 21.5, 1.42),
])
cA.end_report()

cB = Flow(p, [(COLX[1], CW)], 200, 1150, tag="P7-B1")
cB.head("NIVEAU B1 · 중급", 27)
cB.head("LE PASSÉ COMPOSÉ", 24)
cB.para("« Les enfants se sont déguisés samedi. » « Les cimetières se sont remplis de fleurs. » Avec se + être + participe passé : attention à l'accord avec le sujet : déguisés, remplis. (page 3)", 22.5)
cB.head("LE COMPARATIF", 24)
cB.para("plus / moins / aussi + adjectif (+ que) : « Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ? » « Ce match est aussi important que la finale. » — deux comparatifs opposés par ou ; bon devient meilleur, jamais « plus bon ».", 22.5)
cB.box("LA PHRASE EXEMPLE", [
    ("« Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ? » — le comparatif du débat sportif (page 4).", "serif", False, INK, 21.5, 1.42),
])
cB.end_report()

cC = Flow(p, [(COLX[2], CW), (COLX[3], CW)], 200, 1150, tag="P7-B2")
cC.head("NIVEAU B2 · 고급", 27)
cC.head("IL EST PRÉVU QUE + SUBJONCTIF", 24)
cC.para("« Il est prévu que l'Assemblée examine la Culture mardi. » Après « il est prévu que », le verbe passe au subjonctif : examiner → examine, voter → vote, changer → change. (page 6)", 22.5)
cC.head("EXPRIMER L'ATTENTE", 24)
cC.para("« On ne connaît pas encore les finalistes. » « Les résultats seront connus samedi soir. » Pour parler d'un avenir incertain, on distingue le programme prévu et le résultat connu — jamais l'inverse.", 22.5)
cC.box("LA PHRASE EXEMPLE", [
    ("« Ce calendrier peut encore bouger. » — pouvoir + infinitif : la phrase de prudence des journaux.", "serif", False, INK, 21.5, 1.42),
])
cC.end_report()

cD = Flow(p, [(COLX[3], CW)], 200, 1150, tag="P7-outils")
cD.head("BOÎTE À OUTILS · 도구 상자", 27)
cD.para("Trois phrases à garder dans la poche, une pour chaque niveau :", 22.5)
cD.para("A2 — « Le lundi 2 novembre, on reprend les cours. »", 22.5, "serif", True, OLIVE)
cD.para("B1 — « Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ? »", 22.5, "serif", True, OLIVE)
cD.para("B2 — « Il est prévu que l'Assemblée examine la Culture mardi. »", 22.5, "serif", True, OLIVE)
cD.para("Gardez aussi le réflexe du journal : chaque phrase de la semaine vient d'un article de ce numéro. Relisez l'article, la phrase devient facile.", 22.5)
cD.expl("이번 호 주머니 문장 세 개, 수준별로 하나씩. 이번 주 문장은 모두 이번 호 글에서 왔어요. 원문을 다시 읽으면 가장 효과적이에요.")
cD.end_report()

py = 1160
p.hline(MX, RIGHT, py - 14, GOLD, 2)
p.text(MX, py + 26, "LES PHRASES DE LA SEMAINE · 이번 주 문장(모두 본문에서)", 27, "sans", True, OLIVE)
p.text(RIGHT, py + 26, "매 문장 문법 포인트 + 미니 문제 · 정답은 8면", 20, "sans", False, GREY, anchor="end")
pf = Flow(p, [(COLX[i], CW) for i in range(4)], py + 52, 1830, tag="P7-phrases")
phrases = [
    ("« Le lundi 2 novembre, on reprend les cours. » (page 2)",
     "문법 포인트 — reprendre: 복교, 다시 시작하기(pause 뒤).",
     "A2", "Après les vacances, on ___ (reprendre) les cours.", "reprend", "on → reprend"),
    ("« On ne connaît pas encore les finalistes. » (page 1)",
     "문법 포인트 — ne...pas encore: 아직 ~않다.",
     "B1", "Il ne fait pas ___ nuit : il est 15 heures.", "encore", "pas encore 아직 ~않다"),
    ("« Les cimetières se sont remplis de chrysanthèmes. » (page 3)",
     "문법 포인트 — passé composé 대동사: se + être + 과거분사.",
     "B1", "Les enfants se sont ___ (déguiser) samedi.", "déguisés", "se déguiser → se sont déguisés"),
    ("« Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ? » (page 4)",
     "문법 포인트 — comparatif: plus + 형용사, ou 대조.",
     "B1", "La finale est ___ (excitante) !", "plus excitante", "plus + 형용사"),
    ("« Le festival se promène dans Paris. » (page 5)",
     "문법 포인트 — se promener: 대동사, 거닐다, 돌아다니다.",
     "A2", "Le dimanche, nous nous ___ (promener) au parc.", "promenons", "se promener → nous promenons"),
    ("« Ce calendrier peut encore bouger. » (page 6)",
     "문법 포인트 — pouvoir + 동사 원형: ~할 수 있다, ~해도 된다.",
     "B2", "Le programme ___ (pouvoir) changer demain.", "peut", "pouvoir → peut"),
    ("« Ce week-end, tout se joue. » (page 1)",
     "문법 포인트 — se jouer: 결판이 나다, 상연되다(대동사).",
     "A2", "La finale se ___ (jouer) dimanche.", "joue", "se jouer → se joue"),
    ("« Les jeunes créateurs y rencontrent leur public, en vrai. » (page 5)",
     "문법 포인트 — rencontrer: 관객과 만나다, y는 장소를 가리킨다.",
     "A2", "Ils ___ (rencontrer) leur public.", "rencontrent", "rencontrer → rencontrent"),
]
for sent, point, lv, q, key, note in phrases:
    pf.para(sent, 22, "serif", True, INK, 1.4, 4)
    pf.expl(point, 19.5, 5)
    pf.ex(lv, "跟练", key, note, q, size=22)
pf.end_report()

by7 = 1870
p.hline(MX, RIGHT, by7 - 14, GOLD, 2)
cf = Flow(p, [(COLX[0], CW), (COLX[1], CW)], by7 + 8, 2268, tag="P7-clinic")
cf.head("CLINIQUE DES ERREURS · 오류", 25)
cf.expl("매 문장에 오류가 하나씩 있어요. 찾아서 고치세요.")
cf.ex("A2", "改错", "On n'offre jamais de chrysanthèmes pour un anniversaire.", "jamais + de: 부정문에서는 des가 de로 바뀌어요",
      "✗ « On offre des chrysanthèmes pour un anniversaire. »", instr="오류 고치기", size=22.5)
cf.ex("A2", "改错", "Les jeunes créateurs y rencontrent leur public, en vrai.", "주어-동사 일치: créateurs는 복수 → rencontrent, rencontre가 아니에요",
      "✗ « Les jeunes créateurs y rencontre leur public, en vrai. »", instr="오류 고치기", size=22.5)
cf.ex("B2", "改错", "Il est prévu que l'Assemblée examine la Culture mardi.", "가정법: il examine, s를 붙이지 않아요",
      "✗ « Il est prévu que l'Assemblée examines la Culture. »", instr="오류 고치기", size=22.5)
cf.ex("B1", "改错", "La finale a lieu dimanche 8 novembre.", "사실: 결승은 8일, 7일이 아니에요",
      "✗ « La finale a lieu dimanche 7 novembre. »", instr="오류 고치기", size=22.5)
cf.end_report()

rx, rw = span_x(2, 2)
p.rect(rx, by7 + 8, rw, 380, fill=BOX, stroke=LINE, sw=1.4)
p.text(rx + 24, by7 + 48, "LE COURRIER DES LECTEURS · 독자 마당", 24, "sans", True, OLIVE)
p.para(rx + 24, by7 + 86, "« Mon week-end de novembre : samedi, j'ai regardé un match à la télévision ; dimanche, j'ai cuisiné une soupe et j'ai lu vingt pages. » — Exemple de la rédaction (ce texte n'est pas une lettre de lecteur).", 21, "serif", False, INK, rw - 48, 1.42)
p.para(rx + 24, by7 + 196, "샤오모의 한마디 — passé composé가 안정적이고 세미콜론이 좋아요. VOL.4에 여러분의 편지와 최고의 P8 작문을 보내 주세요!", 20, "sans", False, GREY, rw - 48, 1.4)
p.para(rx + 24, by7 + 272, "Note de la rédaction : aucun texte du VOL.2 n'était arrivé au moment de mettre sous presse (le numéro W44 n'a pas paru). Le VOL.4 reprendra la promesse.", 20, "serif", False, INK, rw - 48, 1.4)
p.para(rx + 24, by7 + 336, "편집부 알림: 인쇄 때까지 VOL.2 편지가 오지 않았고(W44 미발행), 최고의 P8 작문도 없어 예시를 싣습니다. VOL.4에서 실제 편지와 작문을 다룹니다.", 19.5, "sans", False, GREY, rw - 48, 1.4)
ty7 = by7 + 8 + 380 + 12
p.rect(rx, ty7, rw, 2540 - ty7, fill=DARK)
p.text(rx + 24, ty7 + 46, "LA SEMAINE PROCHAINE · VOL.4 다음 주", 24, "sans", True, "#f3edda")
p.para(rx + 24, ty7 + 84, "Lundi 9 novembre : le Sénat examine le budget de la Sécurité sociale. Mercredi 11 novembre : l'Armistice, un jour de mémoire. Samedi 14 et dimanche 15 novembre : la Foire aux harengs et à la coquille Saint-Jacques, à Dieppe. Et vos lettres, enfin !", 21, "serif", False, "#e8dfc8", rw - 48, 1.45)
p.para(rx + 24, ty7 + 196, "다음 주: 상원 사회보장 예산 심의, 11월 11일 정전 기념일, 디에프 가리비 시장. 여러분의 편지도요!", 20, "sans", False, "#b3a06a", rw - 48, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-langue.svg")
print("P7 saved, exercises so far:", len(REG))
