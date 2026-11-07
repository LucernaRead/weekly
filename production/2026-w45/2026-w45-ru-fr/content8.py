# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · ТЕСТ И ОТВЕТЫ =================
CURPAGE[0] = 8
p = BSPage4()
p.band("ТЕСТ И ОТВЕТЫ · Test et réponses", "Lucerna", "PAGE 8 · Большой тест недели + все ответы")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · ХРОНИКА НЕДЕЛИ", 21, OLIVE, 5)
f.ex("B1", "Cloze", "A", "Le 4 novembre, jour férié",
     "Выходной посреди недели — ___ ноября. (A. 4 · B. 5)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "Le 3 novembre, journée de travail courte",
     "Короткий день — ___ ноября. (A. 2 · B. 3)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "Soldes jusqu'au 12 novembre",
     "Распродажа 11.11 закончится ___ ноября. (A. 12 · B. 8)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "Le match phare, samedi",
     "Матч «Краснодар» — ЦСКА будет в ___. (A. субботу · B. пятницу)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "Derby : 2:0",
     "Дерби ЦСКА — «Спартак» закончилось со счётом ___. (A. 2:0 · B. 0:0)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "La 15e journée, le 20 novembre",
     "15-й тур будет ___ ноября. (A. 20 · B. 8)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "Rentrée le 5 novembre",
     "Школьники идут в школу ___ ноября. (A. 4 · B. 5)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "Un code promo est un code de réduction",
     "Промокод — это код со ___. (A. скидкой · B. списком)", size=13.8, gap=0)
f.head("B · ОБЩИЕ ВОПРОСЫ", 21, OLIVE, 5)
f.ex("A2", "Choix", "B", "Le 4 novembre, Journée de l'unité nationale",
     "Когда День народного единства? A. 2 ноября · B. 4 ноября · C. 5 ноября", size=13.8, gap=0)
f.ex("B1", "Choix", "B", "Congé jeudi et vendredi : 5 jours d'affilée",
     "Сколько дней отдыха подряд, если взять отпуск в четверг и в пятницу? A. 3 · B. 5 · C. 7", size=13.8, gap=0)
f.ex("B2", "Choix", "B", "Jours de congé : mercredi, samedi, dimanche",
     "Сколько выходных дней в неделе 2–8 ноября? A. 2 · B. 3 · C. 4", size=13.8, gap=0)
f.ex("B1", "Choix", "A", "Soldes dès le 22 octobre",
     "Когда началась распродажа 11.11? A. 22 октября · B. 2 ноября · C. 12 ноября", size=13.8, gap=0)
f.ex("B1", "Choix", "B", "Presse spécialisée : des réductions peut-être moindres",
     "Что пишет торговая пресса о скидках? A. Их будет больше · B. Их может быть меньше · C. Их не будет", size=13.8, gap=0)
f.ex("A2", "Choix", "A", "Vainqueur du derby : le CSKA",
     "Кто победил в дерби? A. ЦСКА · B. «Спартак» · C. Ничья", size=13.8, gap=0)
f.ex("B1", "Choix", "A", "La 13e journée se termine lundi",
     "Когда закрывается 13-й тур? A. 2 ноября · B. 6 ноября · C. 8 ноября", size=13.8, gap=0)
f.ex("A2", "Choix", "B", "Un code promo est un code de réduction",
     "Что такое промокод? A. Список · B. Код со скидкой · C. Магазин", size=13.8, gap=0)
f.head("C · ЧИТАЙТЕ И ОТВЕЧАЙТЕ", 21, OLIVE, 5)
f.para("Маша учится в школе в Москве. На этой неделе у неё последние дни каникул: в среду, 4 ноября, — праздник, а в четверг — снова в школу. В среду Маша пойдёт на ярмарку с семьёй. А в субботу она будет смотреть футбол: «Краснодар» играет с ЦСКА. Маша болеет за «Краснодар».", 15, lh=1.3, split=False)
f.ex("A2", "Choix", "B", "Les derniers jours de congé de Macha",
     "Что у Маши на этой неделе? A. Экзамены · B. Последние дни каникул · C. Новая школа", size=13.8, gap=0)
f.ex("A2", "Choix", "B", "À la foire mercredi",
     "Куда Маша пойдёт в среду? A. В школу · B. На ярмарку · C. На футбол", size=13.8, gap=0)
f.ex("A2", "Choix", "B", "Rentrée jeudi",
     "Когда Маша снова идёт в школу? A. В среду · B. В четверг · C. В субботу", size=13.8, gap=0)
f.ex("B1", "Choix", "B", "Macha soutient Krasnodar",
     "За кого болеет Маша? A. За ЦСКА · B. За «Краснодар» · C. За «Спартак»", size=13.8, gap=0)
f.head("D · СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 21, OLIVE, 5)
f.ex("A2", "Phrases", "В четверг школьники идут в школу.", "Le moment d'abord, le verbe en deuxième position",
     "в четверг / школьники / идут в школу → ___", instr="Phrases", size=13.8, gap=0)
f.ex("A2", "Phrases", "Мы берём отпуск в четверг и в пятницу.", "Sujet + verbe + moment",
     "мы / берём отпуск / в четверг и в пятницу → ___", instr="Phrases", size=13.8, gap=0)
f.ex("B1", "Phrases", "В субботу будет главный матч тура.", "Le moment d'abord, le verbe en deuxième position",
     "в субботу / будет / главный матч тура → ___", instr="Phrases", size=13.8, gap=0)
f.ex("B1", "Phrases", "Сначала составьте список покупок.", "Impératif + objet",
     "сначала / составьте / список покупок → ___", instr="Phrases", size=13.8, gap=0)
f.head("E · ПЕРЕВЕДИТЕ", 21, OLIVE, 5)
f.ex("A2", "Traduction", "Mercredi 4 novembre, c'est un jour férié.", "Comparez page 3",
     "В среду, 4 ноября, — выходной. → ___", instr="Traduire en français", size=13.8, gap=0)
f.ex("B1", "Traduction", "Un code promo est un code de réduction.", "Comparez page 5",
     "Промокод — это код со скидкой. → ___", instr="Traduire en français", size=13.8, gap=0)
f.ex("B1", "Traduction", "В субботу «Краснодар» играет с ЦСКА.", "Note : играть + с + instrumental",
     "Le samedi, Krasnodar joue contre le CSKA. → ___", instr="Traduire en russe", size=13.8, gap=0)
f.ex("B2", "Traduction", "Поздравляю с Днём народного единства!", "поздравляю + с + instrumental",
     "Je souhaite à tout le monde une bonne Journée de l'unité nationale ! → ___", instr="Traduire en russe", size=13.8, gap=0)
f.head("F · СЛОВА НЕДЕЛИ", 21, OLIVE, 5)
f.match_set("B2", "Appariement",
            ["выходной", "промокод", "пауза", "ярмарка"],
            ["код со скидкой",
             "место, где продают еду и подарки",
             "перерыв в чемпионате",
             "день, когда не работают"],
            ["d", "a", "c", "b"],
            ["Jour de congé d", "Code promo a", "Pause c", "Foire b"],
            instr="Associer")
f.head("G · ДИАЛОГ В МАГАЗИНЕ", 21, OLIVE, 5)
f.ex("B1", "Cloze", "A", "скидка = réduction",
     "— Здравствуйте! На эту куртку есть ___? (A. скидка · B. список)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "скидка 20%",
     "— Да, сегодня ___ 20%. (A. цена · B. скидка)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "у меня есть = j'ai un code promo",
     "— А у меня есть ___! (A. промокод · B. выходной)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "его = le code promo (masculin)",
     "— Отлично! Введите ___ в приложении. (A. его · B. её)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "Bonnes courses",
     "— Спасибо! Хороших ___! (A. скидок · B. покупок)", size=13.8, gap=0)
f.head("H · НАПИШИТЕ САМИ", 21, OLIVE, 5)
MODELO = ("Моя неделя с праздником посреди недели начинается в понедельник, 2 ноября. "
          "В понедельник и во вторник я работаю, а в среду, 4 ноября, — выходной. "
          "В среду я пойду на ярмарку с семьёй: куплю еду и подарки. "
          "В четверг и в пятницу я снова работаю, но вечером смотрю футбол. "
          "В субботу, 7 ноября, «Краснодар» играет с ЦСКА, и я буду болеть за «Краснодар». "
          "В воскресенье я отдохну дома и подготовлюсь к новой неделе. "
          "Такая неделя мне нравится: праздник посреди недели — как маленький подарок!")
NWORDS = len(MODELO.split())
f.bridge(f"Exercice d'écriture (sans solution unique) ; le texte modèle ({NWORDS} mots) est ci-dessous.")
f.ex("B1", "Rédaction", "(Question ouverte — texte modèle ci-dessous)", f"Le texte modèle se trouve dans la section H de cette page ({NWORDS} mots)",
     "«Моя неделя с праздником посреди недели» Напишите 80–100 слов: что вы будете делать в среду, в выходные и куда поедете?", instr="Rédaction", size=13.8, gap=0)
f.para("Пример: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "ОТВЕТЫ · Réponses — classées par page ; cherchez votre numéro", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Chaque réponse avec une courte note en français · ✓ = exercice à texte modèle", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— СТРАНИЦА {pg} —", 13.3, "sans", True, OLIVE, lh=1.13, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Rédaction":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.0, lh=1.13, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-test.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("by type", dict(Counter(e["type"] for e in REG)))
print("model words:", NWORDS)
