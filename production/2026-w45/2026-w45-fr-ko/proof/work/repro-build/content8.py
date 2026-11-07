# -*- coding: utf-8 -*-
"""W45 FR core VOL.3 — P8 (battery 42 + writing + all keys from REG)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/fr-ko-proof/work/repro-edition/svg"
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("EXERCICES & RÉPONSES · 연습과 정답", "Le Lucerna", "종합 평가 ÉVALUATION · 정답은 이 면 아래에")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1485, tag="P8-battery")

# ---- A. cloze ----
cloze_defs = [
    ("A2", "C", "2026년 11월 8일은 일요일"),
    ("A2", "A", "낭테르에 결승 보러 가기"),
    ("A2", "B", "결승 진출자는 토요일 밤에야 알려짐"),
    ("A2", "B", "맛보는 맥락（un régal）→ goûté"),
    ("B1", "C", "se promener 거닐다"),
    ("B1", "A", "avoir + 과거분사 goûté(일치 없음)"),
    ("B1", "C", "les finales 주어 복수 → ont lieu"),
    ("A2", "A", "elle écrit 그녀가 써요"),
]
cnums = [reg_ex(lv, "完形填空", k, nt) for lv, k, nt in cloze_defs]
bf.head("A · TEXTE À TROUS · 빈칸 채우기", 24)
bf.para(f"Léa a seize ans. Le ({cnums[0]})___ 8 novembre, elle se lève tôt : c'est le jour des finales. Avec son frère, elle va à ({cnums[1]})___ pour voir le tennis. « On ne connaît pas encore les ({cnums[2]})___ », dit son frère. Le soir, Léa raconte : « À Port-en-Bessin, on a ({cnums[3]})___ des coquilles, un régal ! » Le festival ({cnums[4]})___ dans Paris. Léa a ({cnums[5]})___ la musique. Les finales ({cnums[6]})___ dimanche, et elle l'({cnums[7]})___ dans son cahier.", 21)
bf.expl("선택지:")
for n, opts in zip(cnums, [
    "A. lundi · B. samedi · C. dimanche",
    "A. Nanterre · B. Plailly · C. Dieppe",
    "A. vainqueurs · B. finalistes · C. spectateurs",
    "A. acheté · B. goûté · C. vendu",
    "A. promène · B. promènent · C. se promène",
    "A. goûté · B. goûtée · C. goûter",
    "A. a lieu · B. ont lieus · C. ont lieu",
    "A. écrit · B. écrivent · C. écris",
]):
    bf.para(f"{n}. {opts}", 19.5, "sans", False, INK, 1.32, 2)

# ---- B. single choice ----
bf.head("B · CHOIX MULTIPLE · 객관식", 24)
mcq = [
    ("A2", "B", "7 nov. = samedi(마지막 야간 행사)", "La dernière nocturne a lieu... A. vendredi 6 · B. samedi 7 · C. dimanche 8"),
    ("A2", "A", "nous → allons", "Lundi, nous ___ reprendre les cours. A. allons · B. allez · C. vont"),
    ("B1", "B", "s'intéresser aux（à+les）", "Elle s'intéresse ___ festivals. A. à les · B. aux · C. des"),
    ("B2", "B", "si + imparfait → conditionnel; j'은 je의 생략형", "Si j'étais libre dimanche, j'___ à Nanterre. A. irai · B. irais · C. vais"),
    ("B2", "A", "주어 ce programme 3인칭 단수 → semble", "À mon avis, ce programme ___ très riche. A. semble · B. sembler · C. semblant"),
    ("B1", "B", "미래형 aura lieu(결승은 일요일)", "Dimanche, la finale ___ à Nanterre. A. a lieu · B. aura lieu · C. avait lieu"),
    ("A2", "A", "세 지역 같은 날 복교", "Les trois zones reprennent... A. le même jour · B. à des jours différents · C. en décembre"),
    ("B1", "C", "가리비 축제는 11월 7–8일", "Le Goût du Large, c'est... A. 14–15 nov. · B. 31 oct. · C. 7–8 nov."),
]
for lv, k, nt, body in mcq:
    bf.ex(lv, "单选", k, nt, body, size=20)

# ---- C. reading ----
bf.head("C · LECTURE · 읽기", 24)
bf.para("Samedi soir, la famille Martin prépare son week-end. Samedi 7 novembre, ils iront à Plailly pour la dernière nocturne : de 19 heures à 1 heure du matin, avec un badge repousse-monstres pour le petit Léo. Dimanche 8, ils regarderont les finales à la télévision, puis ils goûteront des coquilles de Port-en-Bessin. « Trois finales en un week-end ! » dit Monsieur Martin. Le soir, Léo dormira tôt : demain, c'est l'école.", 21)
read_qs = [
    ("A2", "C", "야간 행사는 19시부터 새벽 1시까지", "La nocturne dure de... A. 10 h à 19 h · B. 18 h à 20 h · C. 19 h à 1 h"),
    ("A2", "A", "작은 배지는 꼬마 Léo의 괴물 퇴치용", "Le badge repousse-monstres, c'est pour... A. le petit Léo · B. le père · C. la mère"),
    ("B1", "B", "일요일에는 결승을 보고 가리비를 먹어요", "Dimanche, la famille... A. va à Plailly · B. regarde les finales puis goûte des coquilles · C. reste au lit"),
    ("B1", "A", "일요일 밤 일찍 자는 건 월요일에 학교가 있기 때문", "Dimanche soir, Léo dort tôt parce que... A. demain, c'est l'école · B. il est malade · C. il pleut"),
    ("B2", "A", "월요일은 등교일(복교 후 정상적인 월요일)", "Lundi, Léo... A. retourne à l'école · B. reste en vacances · C. va à Plailly"),
]
for lv, k, nt, body in read_qs:
    bf.ex(lv, "阅读理解", k, nt, body, size=20)

# ---- D. sentence building ----
bf.head("D · PHRASES · 문장 완성", 24)
d_items = [
    ("A2", "Les élèves vont reprendre les cours lundi.", "aller + 원형(futur proche)",
     "Futur proche : « Les élèves reprennent les cours lundi. » → ___"),
    ("B2", "Si tu venais samedi, tu verrais la nocturne.", "si + 반과거 venais",
     "Hypothèse : « Si tu (venir) samedi, tu verrais la nocturne. »"),
    ("B1", "Elle a goûté les coquilles à Port-en-Bessin.", "passé composé: a + 과거분사",
     "Passé composé : « Elle (goûter) les coquilles à Port-en-Bessin. »"),
    ("B2", "Selon moi, les finales sont excitantes.", "selon moi = 제 생각에는",
     "Opinion : « ___ moi, les finales sont excitantes. »"),
    ("B1", "Il est prévu que le Sénat examine le texte lundi.", "il est prévu que + 가정법",
     "Subjonctif : « Il est prévu que le Sénat (examiner) le texte lundi. » → ___"),
]
for lv, k, nt, body in d_items:
    bf.ex(lv, "完成句子", k, nt, body, size=20)

# ---- E. translation ----
bf.head("E · TRADUCTION · 번역", 24)
e_items = [
    ("B2", "일정을 읽는 것 자체가 이미 프랑스를 이해하는 거예요.", "lire un programme = 일정 읽기",
     "한국어로: « Lire un programme, c'est déjà comprendre la France. »"),
    ("A2", "Il court plus vite que son frère.", "비교급 plus vite + court",
     "프랑스어로: 그는 형보다 더 빨리 달려요."),
    ("B1", "Les élèves sont en vacances depuis le 17 octobre.", "être en vacances + depuis",
     "프랑스어로: 학생들은 10월 17일부터 방학이에요."),
    ("B1", "Ce soir, nous allons préparer nos cartables.", "futur proche + préparer",
     "프랑스어로: 오늘 밤 책가방을 챙길 거예요."),
    ("B2", "On ne connaît pas encore les finalistes.", "ne...pas encore = 아직 ~않다",
     "프랑스어로: 아직 결승 진출자를 몰라요."),
]
for lv, k, nt, body in e_items:
    bf.ex(lv, "翻译", k, nt, body, size=20)

# ---- F. matching ----
bf.head("F · LES MOTS · 단어 짝짓기", 24)
bf.match_set("B1", "词汇配对",
             ["un tournoi", "une nocturne", "un budget", "une coquille", "un festival"],
             ["une compétition avec plusieurs matchs", "une soirée qui dure jusqu'à la nuit",
              "le plan des dépenses de l'État", "le coquillage fêté à Port-en-Bessin",
              "plusieurs concerts en une semaine"],
             ["a", "b", "c", "d", "e"],
             ["tournoi=대회 a", "nocturne=야간 행사 b", "budget=예산 c", "coquille=가리비 d", "festival=음악제 e"],
             instr="짝짓기")

# ---- G. dialogue ----
dlg_defs = [
    ("A2", "samedi", "11월 7일은 토요일"),
    ("A2", "coquilles (des coquilles Saint-Jacques)", "시장에서 가리비 사기"),
    ("B1", "goûter", "goûter 맛보다(원형)"),
    ("A2", "recette", "à la portaise는 조리법의 일종"),
    ("A2", "week-end", "Bon week-end! 즐거운 주말 보내세요"),
]
gnums = [reg_ex(lv, "对话补全", k, nt) for lv, k, nt in dlg_defs]
bf.head("G · DIALOGUE · 대화 완성", 24)
bf.para(f"— Bonjour madame, c'est le marché du Goût du Large ? — Oui ! — Pour ({gnums[0]})___, le 7 novembre : je veux des ({gnums[1]})___ pour ma famille. — Goûtez celle-ci ! Vous voulez les ({gnums[2]})___ à la portaise ? — Oui, donnez-moi votre ({gnums[3]})___. — Voilà. Bon ({gnums[4]})___ ! — Merci !", 21)
bf.end_report()

# ---- writing strip ----
wy = 1500
p.hline(MX, RIGHT, wy - 14, GOLD, 2)
reg_ex("B1", "写作", "열린 문제 — 기준은 쓰기 칸에, 모범 답안은 8면 쓰기 칸 안에", "기준에 따라 채점")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H · ÉCRITURE · 쓰기", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Écrivez un petit texte (80 à 100 mots) : « Mon week-end du 7–8 novembre ». Racontez : un match, une fête, un plat. Les meilleurs textes paraîtront dans le VOL.4 (page 7, « Le courrier des lecteurs »).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 190, "프랑스어로 80–100단어를 쓰세요: 저의 11월 7–8일 주말. 경기 하나, 축제 하나, 요리 하나를 분명히 쓰세요.", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 288, fill=BOX, stroke=LINE, sw=1.4)
p.text(mx2 + 22, wy + 38, "MODÈLE · 모범 답안", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "Samedi 7 novembre, j'ai regardé les demi-finales du Masters à la télévision : quelle ambiance ! Le soir, nous avons fêté la dernière nocturne avec des amis, déguisés en fantômes. Dimanche 8, nous avons goûté des coquilles Saint-Jacques à la portaise, achetées au marché de Port-en-Bessin. Le matin, nous avons marché au bord de la mer et nous avons acheté des fleurs pour ma grand-mère. Le soir, nous avons écouté de la musique et j'ai lu vingt pages de mon roman français. C'était un week-end parfait.", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 312
p.hline(MX, RIGHT, ky - 12, GOLD, 2)
p.text(MX, ky + 26, "RÉPONSES · 모든 정답과 해설(1–8면)", 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2545, tag="P8-keys")
from itertools import groupby
# Notes printed on this page = exactly the set printed in the core
# edition, measured from the shipped core P8 SVG with tools/p8.py
# extract (97 noted). Reproduced as an explicit set so the Korean
# edition shows the same notes for the same exercises.
PRINT_NOTES = {1, 3, 4, 7, 8, 10, 11, 13, 14, 17, 19, 21, 27, 28, 31, 32, 33, 34, 42, 44, 53, 55, 56, 57, 58, 59, 60, 63, 67, 68, 69, 70, 71, 72, 74, 77, 78, 79, 80, 81, 82, 83, 84, 87, 90, 92, 93, 94, 95, 96, 100, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150}
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— 제 {pg} 면 —", 17, "sans", True, OLIVE, 1.28, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"] and e["n"] in PRINT_NOTES:
            s += f" ({e['note']})"
        parts.append(s)
    kf.para(" · ".join(parts), 15.5, "sans", False, INK, 1.3, 9)
kf.end_report()
p.foot(8)
p.save(f"{OUT}/p8-exercices.svg")
print("P8 saved, TOTAL exercises:", len(REG))
