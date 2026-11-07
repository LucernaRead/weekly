# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-nl/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · ТЕСТ И ОТВЕТЫ =================
CURPAGE[0] = 8
p = BSPage4()
p.band("ТЕСТ И ОТВЕТЫ · Test en antwoorden", "Lucerna", "PAGINA 8 · Большой тест недели + все ответы")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · ХРОНИКА НЕДЕЛИ", 21, OLIVE, 5)
f.ex("B1", "Cloze-meerkeuze", "A", "4 november vrij",
     "Выходной посреди недели — ___ ноября. (A. 4 · B. 5)", size=13.8, gap=0)
f.ex("B1", "Cloze-meerkeuze", "B", "3 november korte werkdag",
     "Короткий день — ___ ноября. (A. 2 · B. 3)", size=13.8, gap=0)
f.ex("B1", "Cloze-meerkeuze", "A", "Sale tot 12 november",
     "Распродажа 11.11 закончится ___ ноября. (A. 12 · B. 8)", size=13.8, gap=0)
f.ex("B1", "Cloze-meerkeuze", "A", "De topwedstrijd is op zaterdag",
     "Матч «Краснодар» — ЦСКА будет в ___. (A. субботу · B. пятницу)", size=13.8, gap=0)
f.ex("B1", "Cloze-meerkeuze", "A", "Derby-uitslag 2:0",
     "Дерби ЦСКА — «Спартак» закончилось со счётом ___. (A. 2:0 · B. 0:0)", size=13.8, gap=0)
f.ex("B1", "Cloze-meerkeuze", "A", "Ronde 15 op 20 november",
     "15-й тур будет ___ ноября. (A. 20 · B. 8)", size=13.8, gap=0)
f.ex("B1", "Cloze-meerkeuze", "B", "Weer naar school op 5 november",
     "Школьники идут в школу ___ ноября. (A. 4 · B. 5)", size=13.8, gap=0)
f.ex("B1", "Cloze-meerkeuze", "A", "Een promocode is een kortingscode",
     "Промокод — это код со ___. (A. скидкой · B. списком)", size=13.8, gap=0)
f.head("B · ОБЩИЕ ВОПРОСЫ", 21, OLIVE, 5)
f.ex("A2", "Meerkeuze", "B", "4 november is Dag van de Eenheid",
     "Когда День народного единства? A. 2 ноября · B. 4 ноября · C. 5 ноября", size=13.8, gap=0)
f.ex("B1", "Meerkeuze", "B", "Verlof donderdag en vrijdag: 5 vrije dagen achter elkaar",
     "Сколько дней отдыха подряд, если взять отпуск в четверг и в пятницу? A. 3 · B. 5 · C. 7", size=13.8, gap=0)
f.ex("B2", "Meerkeuze", "B", "Vrije dagen: woensdag, zaterdag, zondag",
     "Сколько выходных дней в неделе 2–8 ноября? A. 2 · B. 3 · C. 4", size=13.8, gap=0)
f.ex("B1", "Meerkeuze", "A", "Sale begonnen op 22 oktober",
     "Когда началась распродажа 11.11? A. 22 октября · B. 2 ноября · C. 12 ноября", size=13.8, gap=0)
f.ex("B1", "Meerkeuze", "B", "Handelspers: kortingen worden misschien kleiner",
     "Что пишет торговая пресса о скидках? A. Их будет больше · B. Их может быть меньше · C. Их не будет", size=13.8, gap=0)
f.ex("A2", "Meerkeuze", "A", "Derbywinnaar: CSKA",
     "Кто победил в дерби? A. ЦСКА · B. «Спартак» · C. Ничья", size=13.8, gap=0)
f.ex("B1", "Meerkeuze", "A", "Ronde 13 eindigt op maandag",
     "Когда закрывается 13-й тур? A. 2 ноября · B. 6 ноября · C. 8 ноября", size=13.8, gap=0)
f.ex("A2", "Meerkeuze", "B", "Een promocode is een kortingscode",
     "Что такое промокод? A. Список · B. Код со скидкой · C. Магазин", size=13.8, gap=0)
f.head("C · ЧИТАЙТЕ И ОТВЕЧАЙТЕ", 21, OLIVE, 5)
f.para("Маша учится в школе в Москве. На этой неделе у неё последние дни каникул: в среду, 4 ноября, — праздник, а в четверг — снова в школу. В среду Маша пойдёт на ярмарку с семьёй. А в субботу она будет смотреть футбол: «Краснодар» играет с ЦСКА. Маша болеет за «Краснодар».", 15, lh=1.3, split=False)
f.ex("A2", "Meerkeuze", "B", "Masha's laatste vakantiedagen",
     "Что у Маши на этой неделе? A. Экзамены · B. Последние дни каникул · C. Новая школа", size=13.8, gap=0)
f.ex("A2", "Meerkeuze", "B", "Woensdag naar de markt",
     "Куда Маша пойдёт в среду? A. В школу · B. На ярмарку · C. На футбол", size=13.8, gap=0)
f.ex("A2", "Meerkeuze", "B", "Donderdag weer naar school",
     "Когда Маша снова идёт в школу? A. В среду · B. В четверг · C. В субботу", size=13.8, gap=0)
f.ex("B1", "Meerkeuze", "B", "Masha steunt Krasnodar",
     "За кого болеет Маша? A. За ЦСКА · B. За «Краснодар» · C. За «Спартак»", size=13.8, gap=0)
f.head("D · СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 21, OLIVE, 5)
f.ex("A2", "Zinnen bouwen", "В четверг школьники идут в школу.", "Tijd eerst, werkwoord tweede",
     "в четверг / школьники / идут в школу → ___", instr="Zinnen bouwen", size=13.8, gap=0)
f.ex("A2", "Zinnen bouwen", "Мы берём отпуск в четверг и в пятницу.", "Onderwerp + werkwoord + tijd",
     "мы / берём отпуск / в четверг и в пятницу → ___", instr="Zinnen bouwen", size=13.8, gap=0)
f.ex("B1", "Zinnen bouwen", "В субботу будет главный матч тура.", "Tijd eerst, werkwoord tweede",
     "в субботу / будет / главный матч тура → ___", instr="Zinnen bouwen", size=13.8, gap=0)
f.ex("B1", "Zinnen bouwen", "Сначала составьте список покупок.", "Gebiedende wijs + lijdend voorwerp",
     "сначала / составьте / список покупок → ___", instr="Zinnen bouwen", size=13.8, gap=0)
f.head("E · ПЕРЕВЕДИТЕ", 21, OLIVE, 5)
f.ex("A2", "Vertaling", "Woensdag 4 november is een vrije dag.", "Vergelijk pagina 3",
     "В среду, 4 ноября, — выходной. → ___", instr="Vertaal naar het Nederlands", size=13.8, gap=0)
f.ex("B1", "Vertaling", "Een promocode is een kortingscode.", "Vergelijk pagina 5",
     "Промокод — это код со скидкой. → ___", instr="Vertaal naar het Nederlands", size=13.8, gap=0)
f.ex("B1", "Vertaling", "В субботу «Краснодар» играет с ЦСКА.", "Let op: играть + с + instrumentalis",
     "Op zaterdag speelt Krasnodar tegen CSKA. → ___", instr="Vertaal naar het Russisch", size=13.8, gap=0)
f.ex("B2", "Vertaling", "Поздравляю с Днём народного единства!", "поздравляю + с + instrumentalis",
     "Ik wens iedereen een fijne Dag van de Eenheid! → ___", instr="Vertaal naar het Russisch", size=13.8, gap=0)
f.head("F · СЛОВА НЕДЕЛИ", 21, OLIVE, 5)
f.match_set("B2", "Woorden koppelen",
            ["выходной", "промокод", "пауза", "ярмарка"],
            ["код со скидкой",
             "место, где продают еду и подарки",
             "перерыв в чемпионате",
             "день, когда не работают"],
            ["d", "a", "c", "b"],
            ["Vrije dag d", "Promocode a", "Pauze c", "Markt b"],
            instr="Koppel de paren")
f.head("G · ДИАЛОГ В МАГАЗИНЕ", 21, OLIVE, 5)
f.ex("B1", "Cloze-meerkeuze", "A", "скидка = korting",
     "— Здравствуйте! На эту куртку есть ___? (A. скидка · B. список)", size=13.8, gap=0)
f.ex("B1", "Cloze-meerkeuze", "B", "скидка 20%",
     "— Да, сегодня ___ 20%. (A. цена · B. скидка)", size=13.8, gap=0)
f.ex("B1", "Cloze-meerkeuze", "A", "у меня есть = ik heb een promocode",
     "— А у меня есть ___! (A. промокод · B. выходной)", size=13.8, gap=0)
f.ex("B1", "Cloze-meerkeuze", "A", "его = de promocode (mannelijk)",
     "— Отлично! Введите ___ в приложении. (A. его · B. её)", size=13.8, gap=0)
f.ex("B1", "Cloze-meerkeuze", "B", "Veel winkelplezier",
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
f.bridge(f"Schrijfopdracht (geen eenduidig antwoord); voorbeeldtekst ({NWORDS} woorden) hieronder.")
f.ex("B1", "Schrijven", "(open opdracht, voorbeeldtekst hieronder)", f"Voorbeeldtekst in deel H van deze pagina ({NWORDS} woorden)",
     "«Моя неделя с праздником посреди недели» Напишите 80–100 слов: что вы будете делать в среду, в выходные и куда поедете?", instr="Schrijven", size=13.8, gap=0)
f.para("Пример: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "ОТВЕТЫ · Antwoorden — per pagina gerangschikt; zoek je nummer", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Bij elk antwoord een korte Nederlandse toelichting · ✓ = voorbeeldtekst-opdracht", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— Pagina {pg} —", 13.3, "sans", True, OLIVE, lh=1.13, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Schrijven":
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
