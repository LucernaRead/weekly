# -*- coding: utf-8 -*-
"""W45 FR core VOL.3 — P5 + P6."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/fr-ko-proof/work/repro-r3-edition/svg"
os.makedirs(OUT, exist_ok=True)

# ================= P5 · 청년 (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JEUNESSE & MUSIQUE · 청년", "Le Lucerna", "NIVEAU B1 · Pitchfork Paris · 음악제")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2540, tag="P5-main")
f.title("Pitchfork Paris : une semaine, dix lieux, cent artistes", 37)
f.byline("Par la rédaction · Niveau de lecture : B1")
f.para("Du lundi 2 au dimanche 8 novembre, Paris devient une salle de concert géante : c'est la 15e édition du Pitchfork Music Festival Paris. Dix lieux, une centaine d'artistes, sept jours de musique — de l'Élysée Montmartre au Trabendo, du Badaboum au Café de la Danse.")
f.para("La soirée d'ouverture, lundi 2 novembre, donne le ton : un double concert, Headache et Iceage, plus DIIV. Ensuite, le festival se promène dans Paris : chaque soir, un lieu différent, une ambiance différente. Du jeudi 5 au samedi 7 novembre, c'est « Pitchfork Avant-Garde » dans les salles de Bastille ; les nuits club ont lieu vendredi 6 et samedi 7.")
f.para("Pourquoi ce festival plaît-il aux jeunes ? Parce qu'on n'y reste pas assis : on découvre des groupes qu'on ne connaît pas, on danse, on discute entre deux concerts. Pour un apprenant de français, c'est idéal : les affiches et les discussions à la sortie sont en français — et les paroles des chansons donnent envie de chercher les mots.")
f.para("Le festival tombe pile pendant la semaine de la rentrée : après les vacances, les étudiants retrouvent Paris, et Paris leur offre de la musique. Et le dimanche 8 novembre, quand le festival se termine, la ville a déjà une autre finale en tête : celle du tennis, à Nanterre.")
f.gloss("un lieu 공연장 · une affiche 포스터 · les paroles 가사 · donner le ton 분위기를 정하다 · se promener 거닐다, 돌아다니다 · pile 정확히, 딱.")
f.head("À VOUS ! · 해보기", 25)
f.expl("5면 글을 읽고 정답을 고르세요.")
f.ex("B1", "单选", "B", "음악제는 11월 2–8일, 꼬박 일주일",
     "Le festival Pitchfork dure... A. un soir · B. sept jours · C. un mois")
f.ex("B1", "单选", "A", "15회째 음악제",
     "C'est la... A. 15e édition · B. 10e édition · C. 5e édition")
f.ex("B1", "单选", "C", "Avant-Garde는 바스티유 일대 공연장, 목요일부터 토요일까지",
     "Pitchfork Avant-Garde a lieu... A. lundi · B. à Nanterre · C. à Bastille, du jeudi au samedi")
f.ex("B1", "单选", "B", "클럽 나이트는 금요일과 토요일",
     "Les nuits club ont lieu... A. lundi et mardi · B. vendredi et samedi · C. dimanche")
f.ex("B1", "单选", "A", "개막 밤: Headache, Iceage, DIIV",
     "La soirée d'ouverture, lundi 2, propose... A. Headache, Iceage, DIIV · B. un seul groupe · C. un orchestre classique")
f.expl("lieux / paroles / affiche / ambiance / danse / découvre로 빈칸을 채우세요.")
f.ex("B1", "完成句子", "lieux", "공연장 10곳",
     "Le festival se joue dans dix ___.")
f.ex("B1", "完成句子", "paroles", "가사도 프랑스어 학습 자료예요",
     "Les ___ des chansons aident à apprendre le français.")
f.ex("B1", "完成句子", "affiche", "포스터에 공연 정보가 적혀 있어요",
     "Sur l'___ du festival, on lit les noms des groupes.")
f.ex("B1", "完成句子", "ambiance", "매일 밤 분위기가 달라요",
     "Chaque soir, une ___ différente.")
f.ex("B1", "完成句子", "danse", "음악제에서는 사람들이 춤을 춰요",
     "Au festival, on ___ entre deux concerts.")
f.ex("A2", "完成句子", "découvre", "모르는 밴드를 발견해요",
     "On ___ des groupes qu'on ne connaît pas.")
f.expl("음악 단어와 뜻을 짝지으세요.")
f.match_set("B1", "词汇配对",
            ["un concert", "une scène", "un groupe", "un billet"],
            ["un spectacle de musique en direct", "l'endroit où jouent les musiciens",
             "plusieurs musiciens ensemble", "le papier qui permet d'entrer"],
            ["a", "b", "c", "d"],
            ["concert=콘서트 a", "scène=무대 b", "groupe=밴드 c", "billet=입장권 d"],
            instr="짝짓기")
f.expl("대화를 완성하세요(음악제 입구).")
f.ex("B1", "完成句子", "ce soir", "오늘 밤 공연하는 밴드",
     "— Tu vas voir qui ___ ? — DIIV, à l'Élysée Montmartre.")
f.ex("B1", "完成句子", "deux places", "표 두 장 사기",
     "— Tu as pris ___ ? — Oui, pour toi et moi.")
f.end_report()

ix = COLX[3]
p.rect(ix, 200, CW, 470, fill=BOX, stroke=LINE, sw=1.4)
p.text(ix + 22, 240, "OÙ SORTIR CETTE SEMAINE", 23, "sans", True, OLIVE)
p.para(ix + 22, 278, "Lundi 2 : ouverture à l'Élysée Montmartre. Jeudi 5 – samedi 7 : Avant-Garde à Bastille (Supersonic, POPUP!, Café de la Danse). Vendredi 6 – samedi 7 : nuits club. Dimanche 8 : clôture du festival.", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, 520, "Le festival, c'est toute la semaine du numéro : du lundi de la rentrée au dimanche des finales.", 21.5, "serif", False, INK, CW - 44, 1.42)
qy5 = 696
p.rect(ix, qy5, CW, 400, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(ix + 22, qy5 + 40, "MOTS DE LA MUSIQUE · 음악 단어", 23, "sans", True, OLIVE)
mots5 = [
    "un festival — 음악제", "un concert — 콘서트",
    "une chanson — 노래", "un chanteur — 가수",
    "danser — 춤추다", "écouter — 듣다",
    "une salle — 공연장", "le public — 관객",
]
yy5 = qy5 + 82
for m in mots5:
    p.text(ix + 22, yy5, m, 21.5, "serif", False, INK)
    yy5 += 37
dy5 = qy5 + 400 + 26
p.rect(ix, dy5, CW, 440, fill=BOX, stroke=LINE, sw=1.4)
p.text(ix + 22, dy5 + 40, "PARIS CREATOR WEEK", 23, "sans", True, OLIVE)
p.para(ix + 22, dy5 + 78, "Mercredi 4 et jeudi 5 novembre, à La Villette, c'est la Paris Creator Week : deux jours pour les créateurs en ligne — vidéos, podcasts, réseaux sociaux. Les jeunes créateurs y rencontrent leur public, en vrai.", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, dy5 + 300, "11월 4–5일 라빌레트: 크리에이터 위크, 온라인 크리에이터와 관객이 직접 만나요.", 20, "sans", False, GREY, CW - 44, 1.4)
ty5 = dy5 + 440 + 26
p.rect(ix, ty5, CW, 2540 - ty5, fill=BOX, stroke=LINE, sw=1.4)
p.text(ix + 22, ty5 + 40, "LE DÉBAT · 토론", 23, "sans", True, OLIVE)
p.para(ix + 22, ty5 + 78, "Un festival dans dix lieux différents : mieux qu'une seule grande salle ? Discutez en classe : deux phrases pour, deux phrases contre. Et vous, quelle musique écoutez-vous pour apprendre le français ?", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, ty5 + 285, "열 곳에서 열리는 음악제가 하나의 큰 공연장보다 나을까요? 프랑스어를 배우려고 어떤 음악을 들어요?", 20, "sans", False, GREY, CW - 44, 1.4)
p.foot(5)
p.save(f"{OUT}/p5-jeunesse.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · 시사 (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("POLITIQUE & CHIFFRES · 시사", "Le Lucerna", "NIVEAU B2 · Budget 2027 · 예산 주간")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW)], 200, 1300, tag="P6-deep")
f.title("À l'Assemblée, cette semaine : le budget 2027", 36)
f.byline("Par la rédaction · Niveau de lecture : B2")
f.para("Cette semaine, l'Assemblée nationale examine la deuxième partie du budget 2027, mission par mission. C'est le calendrier prévu : mardi 3 novembre, la Culture et les Médias, le livre et les industries culturelles ; mercredi 4, l'Agriculture ; jeudi 5, la Cohésion des territoires et la Recherche et l'enseignement supérieur ; vendredi 6, la Gestion des finances publiques et l'Économie.")
f.para("Attention, lecteurs : ce calendrier peut encore bouger, et les résultats des votes ne sont pas connus au moment où nous écrivons. Ce numéro ne prétend donc pas les annoncer : il explique le programme, pas les résultats.")
f.para("Contexte : vendredi 23 octobre, les députés ont rejeté, presque à l'unanimité, les recettes du budget de la Sécurité sociale — 115 voix contre 1. Le texte part donc au Sénat, qui l'examinera à partir du lundi 9 novembre, la semaine prochaine.")
f.para("Pourquoi le budget compte-t-il pour un apprenant de français ? Parce que c'est le vocabulaire de la vie publique : une mission, un crédit, un vote, un amendement. Et parce que les débats, à la télévision, sont une leçon de français réel — rapide, mais réel.")
f.gloss("un budget 예산 · une mission 예산 항목 · un député 국회의원 · rejeter 부결하다 · à l'unanimité 만장일치로 · un amendement 수정안.")
f.end_report()

# schedule chart (cols 0-1, below deep read)
chx, chw = COLX[0], 2 * CW + GUT
chy = 1330
p.rect(chx, chy, chw, 470, fill=BOX, stroke=LINE, sw=1.4)
p.text(chx + 22, chy + 40, "LE CALENDRIER PRÉVU · 예정된 투표 일정(결과 미정)", 24, "sans", True, OLIVE)
p.text(chx + 22, chy + 74, "Programme prévu, susceptible de changer — ne pas confondre avec des résultats.", 19, "sans", False, GREY)
rows6 = [
    ("mar. 3 nov.", "Culture · Médias, livre", OLIVE),
    ("mer. 4 nov.", "Agriculture", GOLD),
    ("jeu. 5 nov.", "Cohésion · Recherche", OLIVE),
    ("ven. 6 nov.", "Finances publiques · Économie", GOLD),
]
byy = chy + 112
for d, t, col in rows6:
    p.text(chx + 22, byy + 22, d, 21, "sans", True, BRICK)
    p.text(chx + 200, byy + 22, t, 21.5, "serif", False, INK)
    byy += 76
p.text(chx + 22, byy + 16, "Source : ordre du jour du 20 octobre (nosparlementaires.fr).", 18.5, "sans", False, GREY)
p.text(chx + 22, byy + 44, "이 면의 일정은 계획일 뿐, 결과는 아직 없어요. 다음 호에서 다룹니다.", 19, "sans", False, GREY)

e6 = Flow(p, [(COLX[0], CW), (COLX[1], CW)], chy + 470 + 30, 2540, tag="P6-ex")
e6.head("LIRE LE CALENDRIER · 일정 읽기", 25)
e6.expl("위 일정표를 읽고 정답을 고르세요.")
e6.ex("B2", "图表读数", "B", "화요일 3일: 문화와 미디어",
      "Mardi 3, on vote... A. l'Agriculture · B. la Culture · C. l'Économie", size=22)
e6.ex("B2", "图表读数", "A", "수요일 4일: 농업",
      "Mercredi 4, c'est... A. l'Agriculture · B. la Recherche · C. la Culture", size=22)
e6.ex("B2", "图表读数", "C", "목요일 5일: 국토 조정과 연구",
      "Jeudi 5, on examine... A. les Finances · B. l'Agriculture · C. Cohésion et Recherche", size=22)
e6.ex("B2", "图表读数", "A", "금요일 6일: 공공 재정과 경제",
      "Vendredi 6, c'est... A. Finances et Économie · B. la Culture · C. l'Agriculture", size=22)
e6.ex("B1", "图表读数", "B", "10월 23일 사회보장 예산 수입이 115–1로 부결",
      "Le 23 oct., les recettes ont été... A. adoptées · B. rejetées 115–1 · C. reportées", size=22)
e6.ex("B1", "图表读数", "C", "상원은 11월 9일부터 심의",
      "Le Sénat examinera le texte dès le... A. 3 nov. · B. 6 nov. · C. 9 nov.", size=22)
e6.head("LES MOTS · 단어", 25)
e6.match_set("B2", "词汇配对",
              ["un député", "rejeter", "un vote", "un amendement"],
              ["un élu de l'Assemblée nationale", "dire non à un texte",
               "la décision prise ensemble", "proposer un changement"],
              ["a", "b", "c", "d"],
              ["député=국회의원 a", "rejeter=부결하다 b", "vote=투표 c", "amendement=수정안 d"],
              instr="짝짓기")
e6.end_report()

# col 2-3: opinion + micro-drills
g = Flow(p, [(COLX[2], CW), (COLX[3], CW)], 200, 1300, tag="P6-opinion")
g.head("EXPRIMER UNE OPINION", 25)
g.para("À mon avis, ... · Selon les chiffres, ... · D'après le calendrier, ... Trois portes pour commencer une phrase d'opinion — et une règle : on distingue le programme prévu et le résultat connu.", 23.5)
g.box("LES PHRASES DES JOURNAUX", [
    ("« Le texte part au Sénat. » — 법안, 상원으로 넘어가요.", "serif", False, INK, 21.5, 1.42),
    ("« Ce calendrier peut encore bouger. » — 일정은 아직 바뀔 수 있어요.", "serif", False, INK, 21.5, 1.42),
    ("« Les résultats ne sont pas connus. » — 결과는 아직 알려지지 않았어요.", "serif", False, INK, 21.5, 1.42),
])
g.head("IL EST PRÉVU QUE + SUBJONCTIF", 25)
g.para("Après « il est prévu que », le verbe passe au subjonctif : examiner → examine, voter → vote, changer → change. C'est la forme des journaux quand le programme est prévu mais pas encore réalisé.", 23.5)
g.expl("prévu 예정된, 계획된 · réaliser 이루다, 완성하다 · distinguer 구분하다.")
g.end_report()

g2 = Flow(p, [(COLX[2], CW), (COLX[3], CW)], 1330, 2540, tag="P6-micro")
g2.head("LE COMPARATIF EN POLITIQUE", 25)
g2.expl("비교급으로 문장을 완성하세요.")
g2.ex("B1", "完成句子", "plus long", "예산 토론은 콘서트보다 길어요",
      "Un débat sur le budget est ___ (long) qu'un concert.", size=21.5)
g2.ex("B2", "完成句子", "moins simple", "예산은 일정표보다 복잡해요",
      "Le budget est ___ (simple) qu'un calendrier. (moins)", size=21.5)
g2.ex("B2", "完成句子", "aussi important", "문화 예산은 농업 예산만큼 중요해요",
      "Le budget de la Culture est ___ (important) que celui de l'Agriculture. (aussi)", size=21.5)
g2.head("MICRO-DRILLS · 미니 연습", 25)
g2.expl("examine / ont rejeté / part / peut / connus로 빈칸을 채우세요.")
g2.ex("B2", "完成句子", "examine", "국민의회가 예산을 심의해요",
      "Cette semaine, l'Assemblée ___ le budget.", size=21.5)
g2.ex("B2", "完成句子", "ont rejeté", "의원들이 수입 부분을 부결했어요",
      "Le 23 octobre, les députés ___ les recettes du texte.", size=21.5)
g2.ex("B2", "完成句子", "part", "법안이 상원으로 넘어가요",
      "Le texte ___ au Sénat.", size=21.5)
g2.ex("B1", "完成句子", "peut", "일정은 아직 바뀔 수 있어요",
      "Le calendrier ___ encore bouger.", size=21.5)
g2.ex("B1", "完成句子", "connus", "결과는 아직 알려지지 않았어요",
      "Les résultats ne sont pas encore ___.", size=21.5)
g2.box("TROIS DATES POUR COMPRENDRE", [
    ("23 oct. — rejet 115–1 des recettes de la Sécurité sociale.", "serif", False, INK, 21.5, 1.42),
    ("3–6 nov. — votes par mission, programme prévu.", "serif", False, INK, 21.5, 1.42),
    ("9 nov. — le Sénat examine le texte.", "serif", False, INK, 21.5, 1.42),
])
g2.head("LE DÉBAT · 토론", 25)
g2.para("Faut-il annoncer un programme avant les résultats ? Discutez en classe : deux phrases pour, deux phrases contre — en distinguant « prévu » et « décidé ».", 23.5)
g2.expl("결과가 나오기 전에 일정을 먼저 발표해야 할까요? prévu(계획)와 décidé(확정)를 구분하세요.")
g2.end_report()
p.foot(6)
p.save(f"{OUT}/p6-politique.svg")
print("P6 saved, exercises so far:", len(REG))
