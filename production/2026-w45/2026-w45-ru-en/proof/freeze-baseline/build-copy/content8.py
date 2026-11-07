# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/ru-en-proof/freeze-baseline/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · ТЕСТ И ОТВЕТЫ =================
CURPAGE[0] = 8
p = BSPage4()
p.band("ТЕСТ И ОТВЕТЫ · Test and answers", "Lucerna", "PAGE 8 · Большой тест недели + все ответы")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · ХРОНИКА НЕДЕЛИ", 21, OLIVE, 5)
f.ex("B1", "cloze", "A", "4 November is a day off",
     "Выходной посреди недели — ___ ноября. (A. 4 · B. 5)", size=13.8, gap=0)
f.ex("B1", "cloze", "B", "3 November is a short working day",
     "Короткий день — ___ ноября. (A. 2 · B. 3)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "Sale until 12 November",
     "Распродажа 11.11 закончится ___ ноября. (A. 12 · B. 8)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "The top match is on Saturday",
     "Матч «Краснодар» — ЦСКА будет в ___. (A. субботу · B. пятницу)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "Derby score 2:0",
     "Дерби ЦСКА — «Спартак» закончилось со счётом ___. (A. 2:0 · B. 0:0)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "Round 15 on 20 November",
     "15-й тур будет ___ ноября. (A. 20 · B. 8)", size=13.8, gap=0)
f.ex("B1", "cloze", "B", "Back to school on 5 November",
     "Школьники идут в школу ___ ноября. (A. 4 · B. 5)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "A promo code is a discount code",
     "Промокод — это код со ___. (A. скидкой · B. списком)", size=13.8, gap=0)
f.head("B · ОБЩИЕ ВОПРОСЫ", 21, OLIVE, 5)
f.ex("A2", "multiple choice", "B", "4 November is Unity Day",
     "Когда День народного единства? A. 2 ноября · B. 4 ноября · C. 5 ноября", size=13.8, gap=0)
f.ex("B1", "multiple choice", "B", "Leave Thursday and Friday: 5 days off in a row",
     "Сколько дней отдыха подряд, если взять отпуск в четверг и в пятницу? A. 3 · B. 5 · C. 7", size=13.8, gap=0)
f.ex("B2", "multiple choice", "B", "Days off: Wednesday, Saturday, Sunday",
     "Сколько выходных дней в неделе 2–8 ноября? A. 2 · B. 3 · C. 4", size=13.8, gap=0)
f.ex("B1", "multiple choice", "A", "Sale began on 22 October",
     "Когда началась распродажа 11.11? A. 22 октября · B. 2 ноября · C. 12 ноября", size=13.8, gap=0)
f.ex("B1", "multiple choice", "B", "Trade press: discounts may be smaller",
     "Что пишет торговая пресса о скидках? A. Их будет больше · B. Их может быть меньше · C. Их не будет", size=13.8, gap=0)
f.ex("A2", "multiple choice", "A", "Derby winner: CSKA",
     "Кто победил в дерби? A. ЦСКА · B. «Спартак» · C. Ничья", size=13.8, gap=0)
f.ex("B1", "multiple choice", "A", "Round 13 ends on Monday",
     "Когда закрывается 13-й тур? A. 2 ноября · B. 6 ноября · C. 8 ноября", size=13.8, gap=0)
f.ex("A2", "multiple choice", "B", "A promo code is a discount code",
     "Что такое промокод? A. Список · B. Код со скидкой · C. Магазин", size=13.8, gap=0)
f.head("C · ЧИТАЙТЕ И ОТВЕЧАЙТЕ", 21, OLIVE, 5)
f.para("Маша учится в школе в Москве. На этой неделе у неё последние дни каникул: в среду, 4 ноября, — праздник, а в четверг — снова в школу. В среду Маша пойдёт на ярмарку с семьёй. А в субботу она будет смотреть футбол: «Краснодар» играет с ЦСКА. Маша болеет за «Краснодар».", 15, lh=1.3, split=False)
f.ex("A2", "multiple choice", "B", "Masha's last holiday days",
     "Что у Маши на этой неделе? A. Экзамены · B. Последние дни каникул · C. Новая школа", size=13.8, gap=0)
f.ex("A2", "multiple choice", "B", "To the fair on Wednesday",
     "Куда Маша пойдёт в среду? A. В школу · B. На ярмарку · C. На футбол", size=13.8, gap=0)
f.ex("A2", "multiple choice", "B", "Back to school on Thursday",
     "Когда Маша снова идёт в школу? A. В среду · B. В четверг · C. В субботу", size=13.8, gap=0)
f.ex("B1", "multiple choice", "B", "Masha supports Krasnodar",
     "За кого болеет Маша? A. За ЦСКА · B. За «Краснодар» · C. За «Спартак»", size=13.8, gap=0)
f.head("D · СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 21, OLIVE, 5)
f.ex("A2", "sentence building", "В четверг школьники идут в школу.", "Time first, verb second",
     "в четверг / школьники / идут в школу → ___", instr="sentence building", size=13.8, gap=0)
f.ex("A2", "sentence building", "Мы берём отпуск в четверг и в пятницу.", "Subject + verb + time",
     "мы / берём отпуск / в четверг и в пятницу → ___", instr="sentence building", size=13.8, gap=0)
f.ex("B1", "sentence building", "В субботу будет главный матч тура.", "Time first, verb second",
     "в субботу / будет / главный матч тура → ___", instr="sentence building", size=13.8, gap=0)
f.ex("B1", "sentence building", "Сначала составьте список покупок.", "Imperative + object",
     "сначала / составьте / список покупок → ___", instr="sentence building", size=13.8, gap=0)
f.head("E · ПЕРЕВЕДИТЕ", 21, OLIVE, 5)
f.ex("A2", "translation", "Wednesday, 4 November is a day off.", "Compare page 3",
     "В среду, 4 ноября, — выходной. → ___", instr="Translate into English", size=13.8, gap=0)
f.ex("B1", "translation", "A promo code is a discount code.", "Compare page 5",
     "Промокод — это код со скидкой. → ___", instr="Translate into English", size=13.8, gap=0)
f.ex("B1", "translation", "В субботу «Краснодар» играет с ЦСКА.", "Note: играть + с + instrumental",
     "On Saturday, Krasnodar play CSKA. → ___", instr="Translate into Russian", size=13.8, gap=0)
f.ex("B2", "translation", "Поздравляю с Днём народного единства!", "поздравляю + с + instrumental",
     "I wish everyone a happy Unity Day! → ___", instr="Translate into Russian", size=13.8, gap=0)
f.head("F · СЛОВА НЕДЕЛИ", 21, OLIVE, 5)
f.match_set("B2", "matching",
            ["выходной", "промокод", "пауза", "ярмарка"],
            ["код со скидкой",
             "место, где продают еду и подарки",
             "перерыв в чемпионате",
             "день, когда не работают"],
            ["d", "a", "c", "b"],
            ["Day off d", "Promo code a", "Break c", "Fair b"],
            instr="Match the pairs")
f.head("G · ДИАЛОГ В МАГАЗИНЕ", 21, OLIVE, 5)
f.ex("B1", "cloze", "A", "скидка = discount",
     "— Здравствуйте! На эту куртку есть ___? (A. скидка · B. список)", size=13.8, gap=0)
f.ex("B1", "cloze", "B", "скидка 20%",
     "— Да, сегодня ___ 20%. (A. цена · B. скидка)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "у меня есть = I have a promo code",
     "— А у меня есть ___! (A. промокод · B. выходной)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "его = the promo code (masculine)",
     "— Отлично! Введите ___ в приложении. (A. его · B. её)", size=13.8, gap=0)
f.ex("B1", "cloze", "B", "Happy shopping",
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
f.bridge(f"Writing task (no single answer); model text ({NWORDS} words) below.")
f.ex("B1", "writing", "(open task, model text below)", f"Model text in section H of this page ({NWORDS} words)",
     "«Моя неделя с праздником посреди недели» Напишите 80–100 слов: что вы будете делать в среду, в выходные и куда поедете?", instr="writing", size=13.8, gap=0)
f.para("Пример: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "ОТВЕТЫ · Answers — grouped by page; find your number", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "A short English note with every answer · ✓ marks the model-text task", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— СТРАНИЦА {pg} —", 13.3, "sans", True, OLIVE, lh=1.13, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "writing":
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
