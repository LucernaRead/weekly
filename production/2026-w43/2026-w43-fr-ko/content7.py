# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band('LANGUE EN MAIN　집중 해설', "Le Lucerna", 'A2 → B2　Les phrases de la semaine　이번 주 명문장')

# --- three level columns ---
cA = Flow(p, [(COLX[0], CW)], 200, 1150, tag="P7-A2")
cA.head('NIVEAU A2　기초', 27)
cA.head("DIRE L'HEURE", 24)
cA.para("Il est trois heures. · Il est sept heures et demie. · Il est midi moins le quart. On dit toujours « Il est » + l'heure — jamais « c'est ». (page 2)", 22.5)
cA.head("LE FUTUR PROCHE", 24)
cA.para("aller + infinitif : « Ce soir, on va reculer les horloges. » « Dimanche, les élèves vont dormir une heure de plus. » Pour parler d'un futur tout proche, c'est la forme la plus simple.", 22.5)
cA.box("LA PHRASE EXEMPLE", [
    ("« À trois heures, il sera deux heures. » — la phrase du week-end, à dire dimanche à voix haute.", "serif", False, INK, 21.5, 1.42),
])
cA.end_report()

cB = Flow(p, [(COLX[1], CW)], 200, 1150, tag="P7-B1")
cB.head('NIVEAU B1　심화', 27)
cB.head("LE COMPARATIF", 24)
cB.para("plus / moins / aussi + adjectif + que : « Wemby est plus grand que les autres. » « Ce sondage est meilleur que le précédent » — bon devient meilleur, jamais « plus bon ».", 22.5)
cB.head("DEPUIS + PRÉSENT", 24)
cB.para("« Les élèves sont en vacances depuis samedi. » Pour une action qui commence dans le passé et continue : présent + depuis. Attention : pas de passé composé ici — le verbe reste au présent.", 22.5)
cB.box("LA PHRASE EXEMPLE", [
    ("« Il gagne deux points, elle en perd trois. » — le comparatif vit dans les chiffres des sondages (page 6).", "serif", False, INK, 21.5, 1.42),
])
cB.end_report()

cC = Flow(p, [(COLX[2], CW), (COLX[3], CW)], 200, 1150, tag="P7-B2")
cC.head('NIVEAU B2　도전', 27)
cC.head("EXPRIMER UNE OPINION", 24)
cC.para("À mon avis, ... · Selon les chiffres, ... · D'après ce sondage, ... Pour commencer une phrase d'opinion, ces trois portes sont toujours ouvertes.", 22.5)
cC.head("IL SEMBLE QUE + SUBJONCTIF", 24)
cC.para("« Il semble que la candidate soit en tête. » Après « il semble que », le verbe passe au subjonctif : être → soit, avoir → ait, voter → vote. C'est la forme des journaux sérieux.", 22.5)
cC.box("LA PHRASE EXEMPLE", [
    ("« Si l'élection avait lieu dimanche, pour qui voteriez-vous ? » — si + imparfait, réponse au conditionnel : la phrase signature des sondages.", "serif", False, INK, 21.5, 1.42),
])
cC.end_report()

cD = Flow(p, [(COLX[3], CW)], 200, 1150, tag="P7-outils")
cD.head('BOÎTE À OUTILS　도구 상자', 27)
cD.para("Trois phrases à garder dans la poche, une pour chaque niveau :", 22.5)
cD.para("A2 — « Il est dix heures moins le quart. »", 22.5, "serif", True, OLIVE)
cD.para("B1 — « Les vacances commencent depuis samedi... » Non ! « Je suis en vacances depuis samedi. »", 22.5)
cD.para("B2 — « Selon les chiffres, la candidate devance son rival. »", 22.5, "serif", True, OLIVE)
cD.para("Gardez aussi le réflexe du journal : chaque phrase de la semaine vient d'un article de ce numéro. Relisez l'article, la phrase devient facile.", 22.5)
cD.expl('도구 상자 — 이번 호의 문장 세 개를 수준별로 하나씩 챙기세요. 명문장은 전부 이번 호 기사에서 나왔으니, 원문을 다시 읽는 것이 가장 좋아요.')
cD.end_report()

# --- phrases de la semaine ---
py = 1210
p.hline(MX, RIGHT, py - 14, OLIVE, 2)
p.text(MX, py + 26, 'LES PHRASES DE LA SEMAINE　이번 주 명문장 (전부 이번 호 기사에서)', 27, "sans", True, OLIVE)
p.text(RIGHT, py + 26, '문장마다 문법 포인트와 작은 문제 하나　정답은 8면', 20, "sans", False, GREY, anchor="end")
pf = Flow(p, [(COLX[i], CW) for i in range(4)], py + 52, 1830, tag="P7-phrases")
phrases = [
    ("« À trois heures, il sera deux heures. » (page 2)",
     '문법 포인트 — futur simple: être의 미래형은 sera예요.',
     "B1", "Demain, il ___ (être) trop tard pour téléphoner.", "sera", "être → futur : sera"),
    ("« Les élèves sont en vacances depuis samedi. » (page 2)",
     '문법 포인트 — depuis + 현재형: ~부터 지금까지 (동작이 계속될 때).',
     "B1", "Nous apprenons le français ___ 2024.", "depuis", '지금까지 이어지면 depuis'),
    ("« On n'offre jamais de chrysanthèmes pour un anniversaire. » (page 3)",
     '문법 포인트 — ne...jamais + de: 절대 주지 않다 (생일에 국화).',
     "B1", "Il ne boit ___ de café : il déteste ça.", "jamais", 'ne...jamais 절대 ~않다'),
    ("« Wembanyama est plus grand que la plupart des joueurs. » (page 4)",
     '문법 포인트 — comparatif: plus + 형용사 + que.',
     "A2", "Ce match est ___ (long) que prévu.", "plus long", "long → plus long que"),
    ("« Les fans attendent ce jeu depuis des années. » (page 5)",
     '문법 포인트 — attendre는 전치사 없이 바로 목적어를 취해요.',
     "A2", "Ils attendent ___ bus devant la gare.", "le", "attendre le bus"),
    ("« Si l'élection avait lieu dimanche, pour qui voteriez-vous ? » (page 6)",
     '문법 포인트 — si + 반과거 → 조건법: 가정문.',
     "B2", "Si j'étais président, je ___ (changer) les horaires.", "changerais", "si+imparfait → conditionnel"),
    ("« On gagne une heure de sommeil. » (page 1)",
     '문법 포인트 — gagner + 수량: 얻다, 한 시간이 늘다.',
     "A2", "Avec ce train rapide, on gagne ___ heure.", "une", "une heure de sommeil"),
]
for sent, point, lv, q, key, note in phrases:
    pf.para(sent, 22, "serif", True, INK, 1.4, 4)
    pf.expl(point, 19.5, 5)
    pf.ex(lv, '따라 연습', key, note, q, size=22)
pf.end_report()

# --- bottom: clinic (left) + courrier & teaser (right) ---
by7 = 1870
p.hline(MX, RIGHT, by7 - 14, OLIVE, 2)
cf = Flow(p, [(COLX[0], CW), (COLX[1], CW)], by7 + 8, 2268, tag="P7-clinic")
cf.head('CLINIQUE DES ERREURS　실수', 25)
cf.expl('문장마다 틀린 곳이 하나씩 있어요: 찾아서 고치세요.')
cf.ex("A2", '오류 고치기', "J'ai vingt ans.", '나이는 être가 아니라 avoir를 써요',
      "✗ « Je suis vingt ans. »", instr='오류 고치기', size=22.5)
cf.ex("B1", '오류 고치기', "J'attends le bus.", 'attendre는 전치사 없이 바로 목적어를 취해요',
      "✗ « J'attends pour le bus. »", instr='오류 고치기', size=22.5)
cf.ex("A2", '오류 고치기', "Il est trois heures.", '시간을 말할 때는 Il est를 써요',
      "✗ « C'est trois heures. »", instr='오류 고치기', size=22.5)
cf.ex("B1", '오류 고치기', "Elle offre des roses pour mon anniversaire.", '꽃은 장미로, 국화는 안 돼요',
      "✗ « Elle offre des chrysanthèmes pour mon anniversaire. »", instr='오류 고치기', size=22.5)
cf.end_report()

rx, rw = span_x(2, 2)
p.rect(rx, by7 + 8, rw, 300, fill=BOX)
p.text(rx + 24, by7 + 48, 'LE COURRIER DES LECTEURS　독자 마당', 24, "sans", True, OLIVE)
p.para(rx + 24, by7 + 86, "« En automne, je me suis couché de bonne heure, comme Proust. » — L. M., lectrice fidèle (composition du VOL.1, « Mon automne »)", 21.5, "serif", False, INK, rw - 48, 1.42)
p.para(rx + 24, by7 + 176, '샤오모의 한마디 — passé composé로 프루스트의 명문장을 살렸고, de bonne heure도 아주 자연스러워요. 작은 주의: L. M. 님은 여성 독자라 couché에 e를 붙여 couchée가 돼요. 다음 호 독자 마당에서는 VOL.2 투고 글을 계속 다뤄요. 주제는 8면에 있어요.', 20, "sans", False, GREY, rw - 48, 1.42)
ty7 = by7 + 332
p.rect(rx, ty7, rw, 2560 - ty7, fill=CLOTH)
p.text(rx + 24, ty7 + 46, 'LA SEMAINE PROCHAINE　VOL.3 다음 주 예고', 24, "sans", True, ONCLOTH)
p.para(rx + 24, ty7 + 84, "Samedi 31 octobre : Halloween en France, en direct. Dimanche 1er novembre : la Toussaint, le jour des fleurs. Et la première semaine à l'heure d'hiver : la nuit tombe à 18 heures — que lit-on quand il fait nuit tôt ?", 21.5, "serif", False, "#cac8ba", rw - 48, 1.45)
p.para(rx + 24, ty7 + 218, '다음 주 토요일은 Halloween, 일요일은 모든 성인의 날이에요. 겨울 시간 첫 주, 밤이 점점 일찍 찾아와요.', 20, "sans", False, GOOSE, rw - 48, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-langue.svg")
print("P7 saved, exercises so far:", len(REG))
