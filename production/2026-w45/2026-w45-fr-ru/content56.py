# -*- coding: utf-8 -*-
"""W45 FR core VOL.2 — P5 + P6."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · молодёжь (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JEUNESSE & MUSIQUE　МОЛОДЁЖЬ", "Le Lucerna", "NIVEAU B1　Pitchfork Paris　МУЗЫКАЛЬНЫЙ ФЕСТИВАЛЬ")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2560, tag="P5-main")
f.title("Pitchfork Paris : une semaine, dix lieux, cent artistes", 32)
f.byline("Par la rédaction　Niveau de lecture : B1")
f.para("Du lundi 2 au dimanche 8 novembre, Paris devient une salle de concert géante : c'est la 15e édition du Pitchfork Music Festival Paris. Dix lieux, une centaine d'artistes, sept jours de musique — de l'Élysée Montmartre au Trabendo, du Badaboum au Café de la Danse.")
f.para("La soirée d'ouverture, lundi 2 novembre, donne le ton : un double concert, Headache et Iceage, plus DIIV. Ensuite, le festival se promène dans Paris : chaque soir, un lieu différent, une ambiance différente. Du jeudi 5 au samedi 7 novembre, c'est « Pitchfork Avant-Garde » dans les salles de Bastille ; les nuits club ont lieu vendredi 6 et samedi 7.")
f.para("Pourquoi ce festival plaît-il aux jeunes ? Parce qu'on n'y reste pas assis : on découvre des groupes qu'on ne connaît pas, on danse, on discute entre deux concerts. Pour un apprenant de français, c'est idéal : les affiches et les discussions à la sortie sont en français — et les paroles des chansons donnent envie de chercher les mots.")
f.para("Le festival tombe pile pendant la semaine de la rentrée : après les vacances, les étudiants retrouvent Paris, et Paris leur offre de la musique. Et le dimanche 8 novembre, quand le festival se termine, la ville a déjà une autre finale en tête : celle du tennis, à Nanterre.")
f.gloss("un lieu место, площадка · une affiche афиша · les paroles слова песни · donner le ton задавать тон · se promener гулять, перемещаться · pile точно, как раз.")
f.head("À VOUS !　ВАШ ХОД", 25)
f.bridge("Прочитайте статью на стр. 5 и выберите правильный ответ.")
f.ex("B1", "单选", "B", "фестиваль идёт 2–8 ноября, целую неделю",
     "Le festival Pitchfork dure... A. un soir · B. sept jours · C. un mois")
f.ex("B1", "单选", "A", "15-й фестиваль",
     "C'est la... A. 15e édition · B. 10e édition · C. 5e édition")
f.ex("B1", "单选", "C", "Avant-Garde — на площадках Бастилии, с четверга по субботу",
     "Pitchfork Avant-Garde a lieu... A. lundi · B. à Nanterre · C. à Bastille, du jeudi au samedi")
f.ex("B1", "单选", "B", "клубные ночи — в пятницу и субботу",
     "Les nuits club ont lieu... A. lundi et mardi · B. vendredi et samedi · C. dimanche")
f.ex("B1", "单选", "A", "вечер открытия: Headache, Iceage, DIIV",
     "La soirée d'ouverture, lundi 2, propose... A. Headache, Iceage, DIIV · B. un seul groupe · C. un orchestre classique")
f.bridge("Вставьте lieux / paroles / affiche / ambiance / danse / découvre.")
f.ex("B1", "完成句子", "lieux", "десять площадок",
     "Le festival se joue dans dix ___.")
f.ex("B1", "完成句子", "paroles", "тексты песен помогают учить французский",
     "Les ___ des chansons aident à apprendre le français.")
f.ex("B1", "完成句子", "affiche", "афиша: состав участников",
     "Sur l'___ du festival, on lit les noms des groupes.")
f.ex("B1", "完成句子", "ambiance", "каждый вечер — своя атмосфера",
     "Chaque soir, une ___ différente.")
f.ex("B1", "完成句子", "danse", "на фестивале танцуют",
     "Au festival, on ___ entre deux concerts.")
f.ex("A2", "完成句子", "découvre", "открывать незнакомые группы",
     "On ___ des groupes qu'on ne connaît pas.")
f.bridge("Соедините музыкальные слова со значениями.")
f.match_set("B1", "词汇配对",
            ["un concert", "une scène", "un groupe", "un billet"],
            ["un spectacle de musique en direct", "l'endroit où jouent les musiciens",
             "plusieurs musiciens ensemble", "le papier qui permet d'entrer"],
            ["a", "b", "c", "d"],
            ["concert = концерт a", "scène = сцена b", "groupe = группа c", "billet = билет d"],
            instr="Соедините")
f.bridge("Дополните диалог (у входа на фестиваль).")
f.ex("B1", "完成句子", "ce soir", "группа сегодня вечером",
     "— Tu vas voir qui ___ ? — DIIV, à l'Élysée Montmartre.")
f.ex("B1", "完成句子", "deux places", "покупка двух билетов",
     "— Tu as pris ___ ? — Oui, pour toi et moi.")
f.end_report()

ix = COLX[3]
p.rect(ix, 200, CW, 470, fill=BOX)
p.text(ix + 22, 240, "OÙ SORTIR CETTE SEMAINE", 23, "sans", True, OLIVE)
p.para(ix + 22, 278, "Lundi 2 : ouverture à l'Élysée Montmartre. Jeudi 5 – samedi 7 : Avant-Garde à Bastille (Supersonic, POPUP!, Café de la Danse). Vendredi 6 – samedi 7 : nuits club. Dimanche 8 : clôture du festival.", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, 520, "Le festival, c'est toute la semaine du numéro : du lundi de la rentrée au dimanche des finales.", 21.5, "serif", False, INK, CW - 44, 1.42)
qy5 = 696
p.rect(ix, qy5, CW, 400, fill="#f0eee5")
p.text(ix + 22, qy5 + 40, "MOTS DE LA MUSIQUE　МУЗЫКА", 23, "sans", True, OLIVE)
mots5 = [
    "un festival — фестиваль", "un concert — концерт",
    "une chanson — песня", "un chanteur — певец",
    "danser — танцевать", "écouter — слушать",
    "une salle — зал", "le public — публика",
]
yy5 = qy5 + 82
for m in mots5:
    p.text(ix + 22, yy5, m, 21.5, "serif", False, INK)
    yy5 += 37
dy5 = qy5 + 400 + 26
p.rect(ix, dy5, CW, 440, fill=BOX)
p.text(ix + 22, dy5 + 40, "PARIS CREATOR WEEK　КРЕАТОРЫ", 23, "sans", True, OLIVE)
p.para(ix + 22, dy5 + 78, "Mercredi 4 et jeudi 5 novembre, à La Villette, c'est la Paris Creator Week : deux jours pour les créateurs en ligne — vidéos, podcasts, réseaux sociaux. Les jeunes créateurs y rencontrent leur public, en vrai.", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, dy5 + 300, "4–5 ноября в Ла-Виллет: Неделя креаторов — авторы онлайн встречаются со своей публикой вживую.", 20, "sans", False, GREY, CW - 44, 1.4)
ty5 = dy5 + 440 + 26
p.rect(ix, ty5, CW, 2560 - ty5, fill=BOX)
p.text(ix + 22, ty5 + 40, "LE DÉBAT　ДИСКУССИЯ", 23, "sans", True, OLIVE)
p.para(ix + 22, ty5 + 78, "Un festival dans dix lieux différents : mieux qu'une seule grande salle ? Discutez en classe : deux phrases pour, deux phrases contre. Et vous, quelle musique écoutez-vous pour apprendre le français ?", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, ty5 + 285, "Фестиваль на десяти площадках — лучше, чем один большой зал? Какую музыку вы слушаете, чтобы учить французский?", 20, "sans", False, GREY, CW - 44, 1.4)
p.foot(5)
p.save(f"{OUT}/p5-jeunesse.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · актуальные события (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("POLITIQUE & CHIFFRES　ПОЛИТИКА И ЦИФРЫ", "Le Lucerna", "NIVEAU B2　Budget 2027　БЮДЖЕТНАЯ НЕДЕЛЯ")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW)], 200, 1300, tag="P6-deep")
f.title("À l'Assemblée, cette semaine : le budget 2027", 32)
f.byline("Par la rédaction　Niveau de lecture : B2")
f.para("Cette semaine, l'Assemblée nationale examine la deuxième partie du budget 2027, mission par mission. C'est le calendrier prévu : mardi 3 novembre, la Culture et les Médias, le livre et les industries culturelles ; mercredi 4, l'Agriculture ; jeudi 5, la Cohésion des territoires et la Recherche et l'enseignement supérieur ; vendredi 6, la Gestion des finances publiques et l'Économie.")
f.para("Attention, lecteurs : ce calendrier peut encore bouger, et les résultats des votes ne sont pas connus au moment où nous écrivons. Ce numéro ne prétend donc pas les annoncer : il explique le programme, pas les résultats.")
f.para("Contexte : vendredi 23 octobre, les députés ont rejeté, presque à l'unanimité, les recettes du budget de la Sécurité sociale — 115 voix contre 1. Le texte part donc au Sénat, qui l'examinera à partir du lundi 9 novembre, la semaine prochaine.")
f.para("Pourquoi le budget compte-t-il pour un apprenant de français ? Parce que c'est le vocabulaire de la vie publique : une mission, un crédit, un vote, un amendement. Et parce que les débats, à la télévision, sont une leçon de français réel — rapide, mais réel.")
f.gloss("un budget бюджет · une mission (бюджетная) статья · un député депутат Национального собрания · rejeter отклонять · à l'unanimité единогласно · un amendement поправка.")
f.end_report()

# schedule chart (cols 0-1, below deep read)
chx, chw = COLX[0], 2 * CW + GUT
chy = 1330
p.rect(chx, chy, chw, 470, fill=BOX)
p.text(chx + 22, chy + 40, "LE CALENDRIER PRÉVU　ПЛАН ГОЛОСОВАНИЙ (БЕЗ РЕЗУЛЬТАТОВ)", 24, "sans", True, OLIVE)
p.text(chx + 22, chy + 74, "Programme prévu, susceptible de changer — ne pas confondre avec des résultats.", 19, "sans", False, GREY)
rows6 = [
    ("mar. 3 nov.", "Culture · Médias, livre", OLIVE),
    ("mer. 4 nov.", "Agriculture", OLIVE),
    ("jeu. 5 nov.", "Cohésion · Recherche", OLIVE),
    ("ven. 6 nov.", "Finances publiques · Économie", OLIVE),
]
byy = chy + 112
for d, t, col in rows6:
    p.text(chx + 22, byy + 22, d, 21, "sans", True, OLIVE)
    p.text(chx + 200, byy + 22, t, 21.5, "serif", False, INK)
    byy += 76
p.text(chx + 22, byy + 16, "Source : ordre du jour du 20 octobre (nosparlementaires.fr).", 18.5, "sans", False, GREY)
p.text(chx + 22, byy + 44, "Это расписание — план; результатов пока нет, продолжение — в следующем номере.", 19, "sans", False, GREY)

e6 = Flow(p, [(COLX[0], CW), (COLX[1], CW)], chy + 470 + 30, 2560, tag="P6-ex")
e6.head("LIRE LE CALENDRIER　ПЛАН", 25)
e6.bridge("Прочитайте расписание выше и выберите правильный ответ.")
e6.ex("B2", "图表读数", "B", "вторник: культура и СМИ",
      "Mardi 3, on vote... A. l'Agriculture · B. la Culture · C. l'Économie", size=22)
e6.ex("B2", "图表读数", "A", "среда: сельское хозяйство",
      "Mercredi 4, c'est... A. l'Agriculture · B. la Recherche · C. la Culture", size=22)
e6.ex("B2", "图表读数", "C", "четверг 5-го: территории и наука",
      "Jeudi 5, on examine... A. les Finances · B. l'Agriculture · C. Cohésion et Recherche", size=22)
e6.ex("B2", "图表读数", "A", "пятница 6-го: финансы и экономика",
      "Vendredi 6, c'est... A. Finances et Économie · B. la Culture · C. l'Agriculture", size=22)
e6.ex("B1", "图表读数", "B", "23 октября доходы отклонены 115–1",
      "Le 23 oct., les recettes ont été... A. adoptées · B. rejetées 115–1 · C. reportées", size=22)
e6.ex("B1", "图表读数", "C", "Сенат: текст с 9 ноября",
      "Le Sénat examinera le texte dès le... A. 3 nov. · B. 6 nov. · C. 9 nov.", size=22)
e6.head("LES MOTS　СЛОВА", 25)
e6.match_set("B2", "词汇配对",
              ["un député", "rejeter", "un vote", "un amendement"],
              ["un élu de l'Assemblée nationale", "dire non à un texte",
               "la décision prise ensemble", "proposer un changement"],
              ["a", "b", "c", "d"],
              ["député = депутат a", "rejeter = отклонять b", "vote = голосование c", "amendement = поправка d"],
              instr="Соедините")
e6.end_report()

# col 2-3: opinion + micro-drills
g = Flow(p, [(COLX[2], CW), (COLX[3], CW)], 200, 1300, tag="P6-opinion")
g.head("EXPRIMER UNE OPINION", 25)
g.para("À mon avis, ... · Selon les chiffres, ... · D'après le calendrier, ... Trois portes pour commencer une phrase d'opinion — et une règle : on distingue le programme prévu et le résultat connu.", 23.5)
g.box("LES PHRASES DES JOURNAUX", [
    ("« Le texte part au Sénat. » — Законопроект уходит в Сенат.", "serif", False, INK, 21.5, 1.42),
    ("« Ce calendrier peut encore bouger. » — Расписание ещё может измениться.", "serif", False, INK, 21.5, 1.42),
    ("« Les résultats ne sont pas connus. » — Результаты пока неизвестны.", "serif", False, INK, 21.5, 1.42),
])
g.head("IL EST PRÉVU QUE + SUBJONCTIF", 25)
g.para("Après « il est prévu que », le verbe passe au subjonctif : examiner → examine, voter → vote, changer → change. C'est la forme des journaux quand le programme est prévu mais pas encore réalisé.", 23.5)
g.bridge("Пояснение — prévu запланированный · réaliser осуществлять · distinguer различать.")
g.end_report()

g2 = Flow(p, [(COLX[2], CW), (COLX[3], CW)], 1330, 2560, tag="P6-micro")
g2.head("LE COMPARATIF EN POLITIQUE", 25)
g2.bridge("Дополните сравнительной степенью.")
g2.ex("B1", "完成句子", "plus long", "дебаты о бюджете длиннее концерта",
      "Un débat sur le budget est ___ (long) qu'un concert.", size=21.5)
g2.ex("B2", "完成句子", "moins simple", "бюджет сложнее расписания",
      "Le budget est ___ (simple) qu'un calendrier. (moins)", size=21.5)
g2.ex("B2", "完成句子", "aussi important", "бюджет культуры так же важен, как бюджет сельского хозяйства",
      "Le budget de la Culture est ___ (important) que celui de l'Agriculture. (aussi)", size=21.5)
g2.head("MICRO-DRILLS　ПРАКТИКА", 25)
g2.bridge("Вставьте examine / ont rejeté / part / peut / connus.")
g2.ex("B2", "完成句子", "examine", "Собрание рассматривает бюджет",
      "Cette semaine, l'Assemblée ___ le budget.", size=21.5)
g2.ex("B2", "完成句子", "ont rejeté", "депутаты отклонили доходную часть",
      "Le 23 octobre, les députés ___ les recettes du texte.", size=21.5)
g2.ex("B2", "完成句子", "part", "законопроект уходит в Сенат",
      "Le texte ___ au Sénat.", size=21.5)
g2.ex("B1", "完成句子", "peut", "расписание ещё может измениться",
      "Le calendrier ___ encore bouger.", size=21.5)
g2.ex("B1", "完成句子", "connus", "результаты пока неизвестны",
      "Les résultats ne sont pas encore ___.", size=21.5)
g2.box("TROIS DATES POUR COMPRENDRE", [
    ("23 oct. — rejet 115–1 des recettes de la Sécurité sociale.", "serif", False, INK, 21.5, 1.42),
    ("3–6 nov. — votes par mission, programme prévu.", "serif", False, INK, 21.5, 1.42),
    ("9 nov. — le Sénat examine le texte.", "serif", False, INK, 21.5, 1.42),
])
g2.head("LE DÉBAT　ДИСКУССИЯ", 25)
g2.para("Faut-il annoncer un programme avant les résultats ? Discutez en classe : deux phrases pour, deux phrases contre — en distinguant « prévu » et « décidé ».", 23.5)
g2.bridge("Дискуссия: стоит ли объявлять расписание до результатов? Различайте prévu (запланировано) и décidé (решено).")
g2.end_report()
p.foot(6)
p.save(f"{OUT}/p6-politique.svg")
print("P6 saved, exercises so far:", len(REG))
