# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · ТЕСТ И ОТВЕТЫ =================
CURPAGE[0] = 8
p = BSPage4()
p.band("ТЕСТ И ОТВЕТЫ　TEST AND ANSWERS", "Lucerna", "PAGE 8　The big test of the week + all the answers")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　ХРОНИКА НЕДЕЛИ", 21, OLIVE, 5)
f.ex("B1", "cloze", "A", "Monday 9 November",
     "Обычная неделя начинается ___ ноября. (A. 9 · B. 10)", size=13.8, gap=0)
f.ex("B1", "cloze", "B", "10 November — Police Day",
     "День полиции — ___ ноября. (A. 9 · B. 10)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "The sale day: 11 November",
     "День распродажи 11.11 — ___ ноября. (A. 11 · B. 12)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "Thursday against Uzbekistan",
     "Сборная России играет с ___. (A. Узбекистаном · B. Венесуэлой)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "Round 14 results unknown at press time",
     "Итоги 14-го тура на момент сдачи номера ___. (A. неизвестны · B. известны)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "Round 15 on 20 November",
     "15-й тур будет ___ ноября. (A. 20 · B. 15)", size=13.8, gap=0)
f.ex("B1", "cloze", "B", "Lilya opens on 12 November",
     "Фильм «Лиля» выходит ___ ноября. (A. 13 · B. 12)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "A promo code is a discount code",
     "Промокод — это код со ___. (A. скидкой · B. списком)", size=13.8, gap=0)
f.head("B　ОБЩИЕ ВОПРОСЫ", 21, OLIVE, 5)
f.ex("A2", "multiple choice", "B", "10 November — Police Day",
     "Когда День полиции? A. 9 ноября · B. 10 ноября · C. 11 ноября", size=13.8, gap=0)
f.ex("B1", "multiple choice", "B", "5 working days in the week",
     "Сколько рабочих дней на этой неделе? A. 3 · B. 5 · C. 7", size=13.8, gap=0)
f.ex("B2", "multiple choice", "B", "10 days off in November",
     "Сколько выходных и праздничных дней в ноябре? A. 20 · B. 10 · C. 5", size=13.8, gap=0)
f.ex("B1", "multiple choice", "A", "The sale started on 22 October",
     "Когда началась распродажа 11.11 на Ozon? A. 22 октября · B. 9 ноября · C. 12 ноября", size=13.8, gap=0)
f.ex("B1", "multiple choice", "B", "Forecasters: wet snow possible",
     "Что обещают синоптики? A. Жаркое лето · B. Первый мокрый снег · C. Устойчивый снег", size=13.8, gap=0)
f.ex("A2", "multiple choice", "A", "Spartak beat Lokomotiv 4–0",
     "Кто победил в матче «Спартак» — «Локомотив»? A. «Спартак» 4:0 · B. «Локомотив» · C. Ничья", size=13.8, gap=0)
f.ex("B1", "multiple choice", "A", "Round 13: CSKA 0–0 Orenburg",
     "Как сыграли ЦСКА и «Оренбург»? A. 0:0 · B. 4:0 · C. 1:2", size=13.8, gap=0)
f.ex("A2", "multiple choice", "B", "A parcel must be tracked, collected, checked",
     "Что надо сделать с посылкой? A. Выбросить · B. Отследить, получить и проверить · C. Вернуть в кино", size=13.8, gap=0)
f.head("C　ЧИТАЙТЕ И ОТВЕЧАЙТЕ", 21, OLIVE, 5)
f.para("Маша учится в школе в Москве. На этой неделе у неё обычная неделя: пять учебных дней и никаких праздников. В среду, 11 ноября, Маша заказывает книгу на распродаже 11.11. В четверг она получает посылку в пункте выдачи и проверяет книгу. А в субботу Маша идёт в кино с друзьями: они смотрят фильм «Лиля».", 15, lh=1.3, split=False)
f.ex("A2", "multiple choice", "B", "Masha’s week is an ordinary one",
     "Какая неделя у Маши? A. Каникулы · B. Обычная неделя · C. Экзамены", size=13.8, gap=0)
f.ex("A2", "multiple choice", "B", "On Wednesday she orders a book",
     "Что Маша заказывает в среду? A. Билет в кино · B. Книгу · C. Промокод", size=13.8, gap=0)
f.ex("A2", "multiple choice", "B", "On Thursday she collects a parcel at a pickup point",
     "Где Маша получает посылку? A. В кино · B. В пункте выдачи · C. В школе", size=13.8, gap=0)
f.ex("B1", "multiple choice", "B", "On Saturday she sees Lilya with a friend",
     "Куда Маша идёт в субботу? A. В школу · B. В кино с друзьями · C. На ярмарку", size=13.8, gap=0)
f.head("D　СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 21, OLIVE, 5)
f.ex("A2", "sentence building", "В среду Маша заказывает книгу.", "Subject + verb + object",
     "в среду / Маша / заказывает книгу → ___", instr="Build the sentence", size=13.8, gap=0)
f.ex("A2", "sentence building", "В четверг она получает посылку.", "Subject + verb + object",
     "в четверг / она / получает посылку → ___", instr="Build the sentence", size=13.8, gap=0)
f.ex("B1", "sentence building", "В субботу Маша идёт в кино.", "Time first, verb second",
     "в субботу / Маша / идёт в кино → ___", instr="Build the sentence", size=13.8, gap=0)
f.ex("B1", "sentence building", "Сначала составьте список покупок.", "Imperative + object",
     "сначала / составьте / список покупок → ___", instr="Build the sentence", size=13.8, gap=0)
f.head("E　ПЕРЕВЕДИТЕ", 21, OLIVE, 5)
f.ex("A2", "translation", "Tuesday 10 November — Police Day.", "Compare page 2",
     "Во вторник, 10 ноября, — День полиции. → ___", instr="Translate into English", size=13.8, gap=0)
f.ex("B1", "translation", "A parcel must be tracked, collected and checked.", "Compare page 5",
     "Посылку нужно отследить, получить и проверить. → ___", instr="Translate into English", size=13.8, gap=0)
f.ex("B1", "translation", "On Thursday Russia play Uzbekistan.", "Note: играть + с + instrumental",
     "В четверг сборная России играет с Узбекистаном. → ___", instr="Translate into English", size=13.8, gap=0)
f.ex("B2", "translation", "Happy Police Day to everyone!", "поздравляю + с + instrumental",
     "Поздравляю с Днём полиции! → ___", instr="Translate into English", size=13.8, gap=0)
f.head("F　СЛОВА НЕДЕЛИ", 21, OLIVE, 5)
f.match_set("B2", "matching",
            ["предзимье", "посылка", "пик", "гололедица"],
            ["самое большое число заказов",
             "лёд на дороге",
             "время между осенью и зимой",
             "товар, который прислали по почте"],
            ["c", "d", "a", "b"],
            ["early-winter season c", "parcel d", "peak a", "black ice b"],
            instr="Match words and meanings")
f.head("G　ДИАЛОГ В ПУНКТЕ ВЫДАЧИ", 21, OLIVE, 5)
f.ex("B1", "cloze", "A", "Collecting a parcel: номер заказа",
     "— Здравствуйте! Я пришла за посылкой. Вот ___ заказа. (A. номер · B. пик)", size=13.8, gap=0)
f.ex("B1", "cloze", "B", "The parcel has arrived",
     "— Да, ваша посылка уже ___. (A. ушла · B. пришла)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "Please check the parcel",
     "— Проверьте ___, пожалуйста. (A. посылку · B. промокод)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "Everything is fine",
     "— Всё в порядке, спасибо! Книга ___. (A. целая · B. мокрая)", size=13.8, gap=0)
f.ex("B1", "cloze", "B", "Happy shopping",
     "— Спасибо! Хороших ___! (A. скидок · B. покупок)", size=13.8, gap=0)
f.head("H　НАПИШИТЕ САМИ", 21, OLIVE, 5)
MODELO = ("Моя обычная неделя в ноябре начинается в понедельник, 9 ноября. "
          "В понедельник и во вторник я работаю, а вечером читаю книгу. "
          "Во вторник, 10 ноября, я поздравляю знакомого полицейского с Днём полиции. "
          "В среду, 11 ноября, — день распродажи 11.11: я заказываю книгу и проверяю промокод. "
          "В четверг я получаю посылку и проверяю покупку. "
          "В пятницу вечером я иду в кино с друзьями. "
          "В субботу я высыпаюсь и гуляю в парке, а в воскресенье готовлюсь к новой неделе. "
          "Обычная неделя мне нравится: ровный ритм — это хорошо!")
NWORDS = len(MODELO.split())
f.bridge(f"Writing task (no single answer); model text ({NWORDS} words) below.")
f.ex("B1", "writing", "(Open task; model text below)", f"See the model text in section H of this page ({NWORDS} words)",
     "«Моя обычная неделя в ноябре» Напишите 80–100 слов: что вы будете делать каждый день недели?", instr="Write", size=13.8, gap=0)
f.para("Пример: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "ОТВЕТЫ　ANSWER KEY — ARRANGED BY PAGE; FIND THE EXERCISE NUMBER", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Each answer comes with a one-line English note　✓ marks a model-text task", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
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
