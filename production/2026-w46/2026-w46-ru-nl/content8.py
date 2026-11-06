# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-ru-nl/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · ТЕСТ И ОТВЕТЫ =================
CURPAGE[0] = 8
p = BSPage4()
p.band("ТЕСТ И ОТВЕТЫ · TEST EN ANTWOORDEN", "Lucerna", "PAGINA 8 · De grote weektest + alle antwoorden")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · ХРОНИКА НЕДЕЛИ", 21, OLIVE, 5)
f.ex("B1", "Meerkeuze", "A", "Maandag 9 november",
     "Обычная неделя начинается ___ ноября. (A. 9 · B. 10)", size=13.8, gap=0)
f.ex("B1", "Meerkeuze", "B", "10 november — Dag van de Politie",
     "День полиции — ___ ноября. (A. 9 · B. 10)", size=13.8, gap=0)
f.ex("B1", "Meerkeuze", "A", "Kortingsdag: 11 november",
     "День распродажи 11.11 — ___ ноября. (A. 11 · B. 12)", size=13.8, gap=0)
f.ex("B1", "Meerkeuze", "A", "Donderdag tegen Oezbekistan",
     "Сборная России играет с ___. (A. Узбекистаном · B. Венесуэлой)", size=13.8, gap=0)
f.ex("B1", "Meerkeuze", "A", "Uitslagen speelronde 14 onbekend bij het ter perse gaan",
     "Итоги 14-го тура на момент сдачи номера ___. (A. неизвестны · B. известны)", size=13.8, gap=0)
f.ex("B1", "Meerkeuze", "A", "Speelronde 15 op 20 november",
     "15-й тур будет ___ ноября. (A. 20 · B. 15)", size=13.8, gap=0)
f.ex("B1", "Meerkeuze", "B", "Lilja gaat op 12 november in première",
     "Фильм «Лиля» выходит ___ ноября. (A. 13 · B. 12)", size=13.8, gap=0)
f.ex("B1", "Meerkeuze", "A", "Een kortingscode is een code met korting.",
     "Промокод — это код со ___. (A. скидкой · B. списком)", size=13.8, gap=0)
f.head("B · ОБЩИЕ ВОПРОСЫ", 21, OLIVE, 5)
f.ex("A2", "Meerkeuze", "B", "10 november — Dag van de Politie",
     "Когда День полиции? A. 9 ноября · B. 10 ноября · C. 11 ноября", size=13.8, gap=0)
f.ex("B1", "Meerkeuze", "B", "5 werkdagen in de week",
     "Сколько рабочих дней на этой неделе? A. 3 · B. 5 · C. 7", size=13.8, gap=0)
f.ex("B2", "Meerkeuze", "B", "10 vrije dagen in november",
     "Сколько выходных и праздничных дней в ноябре? A. 20 · B. 10 · C. 5", size=13.8, gap=0)
f.ex("B1", "Meerkeuze", "A", "De uitverkoop begon op 22 oktober",
     "Когда началась распродажа 11.11 на Ozon? A. 22 октября · B. 9 ноября · C. 12 ноября", size=13.8, gap=0)
f.ex("B1", "Meerkeuze", "B", "Weermannen: mogelijk natte sneeuw",
     "Что обещают синоптики? A. Жаркое лето · B. Первый мокрый снег · C. Устойчивый снег", size=13.8, gap=0)
f.ex("A2", "Meerkeuze", "A", "Spartak versloeg Lokomotiv met 4-0",
     "Кто победил в матче «Спартак» — «Локомотив»? A. «Спартак» 4:0 · B. «Локомотив» · C. Ничья", size=13.8, gap=0)
f.ex("B1", "Meerkeuze", "A", "Speelronde 13: CSKA 0-0 Orenburg",
     "Как сыграли ЦСКА и «Оренбург»? A. 0:0 · B. 4:0 · C. 1:2", size=13.8, gap=0)
f.ex("A2", "Meerkeuze", "B", "Een pakket moet gevolgd, opgehaald en gecontroleerd worden",
     "Что надо сделать с посылкой? A. Выбросить · B. Отследить, получить и проверить · C. Вернуть в кино", size=13.8, gap=0)
f.head("C · ЧИТАЙТЕ И ОТВЕЧАЙТЕ", 21, OLIVE, 5)
f.para("Маша учится в школе в Москве. На этой неделе у неё обычная неделя: пять учебных дней и никаких праздников. В среду, 11 ноября, Маша заказывает книгу на распродаже 11.11. В четверг она получает посылку в пункте выдачи и проверяет книгу. А в субботу Маша идёт в кино с друзьями: они смотрят фильм «Лиля».", 15, lh=1.3, split=False)
f.ex("A2", "Meerkeuze", "B", "Masha’s week is een gewone week",
     "Какая неделя у Маши? A. Каникулы · B. Обычная неделя · C. Экзамены", size=13.8, gap=0)
f.ex("A2", "Meerkeuze", "B", "Op woensdag bestelt ze een boek",
     "Что Маша заказывает в среду? A. Билет в кино · B. Книгу · C. Промокод", size=13.8, gap=0)
f.ex("A2", "Meerkeuze", "B", "Op donderdag haalt ze een pakket op bij het afhaalpunt",
     "Где Маша получает посылку? A. В кино · B. В пункте выдачи · C. В школе", size=13.8, gap=0)
f.ex("B1", "Meerkeuze", "B", "Op zaterdag ziet ze Lilja met een vriendin",
     "Куда Маша идёт в субботу? A. В школу · B. В кино с друзьями · C. На ярмарку", size=13.8, gap=0)
f.head("D · СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 21, OLIVE, 5)
f.ex("A2", "Zinnen bouwen", "В среду Маша заказывает книгу.", "Onderwerp + werkwoord + lijdend voorwerp",
     "в среду / Маша / заказывает книгу → ___", instr="Zinnen bouwen", size=13.8, gap=0)
f.ex("A2", "Zinnen bouwen", "В четверг она получает посылку.", "Onderwerp + werkwoord + lijdend voorwerp",
     "в четверг / она / получает посылку → ___", instr="Zinnen bouwen", size=13.8, gap=0)
f.ex("B1", "Zinnen bouwen", "В субботу Маша идёт в кино.", "Eerst de tijd, het werkwoord op de tweede plaats",
     "в субботу / Маша / идёт в кино → ___", instr="Zinnen bouwen", size=13.8, gap=0)
f.ex("B1", "Zinnen bouwen", "Сначала составьте список покупок.", "Gebiedende wijs + lijdend voorwerp",
     "сначала / составьте / список покупок → ___", instr="Zinnen bouwen", size=13.8, gap=0)
f.head("E · ПЕРЕВЕДИТЕ", 21, OLIVE, 5)
f.ex("A2", "Vertaling", "Dinsdag 10 november — Dag van de Politie.", "Vergelijk pagina 2",
     "Во вторник, 10 ноября, — День полиции. → ___", instr="Vertaal naar het Nederlands", size=13.8, gap=0)
f.ex("B1", "Vertaling", "Een pakket moet gevolgd, opgehaald en gecontroleerd worden.", "Vergelijk pagina 5",
     "Посылку нужно отследить, получить и проверить. → ___", instr="Vertaal naar het Nederlands", size=13.8, gap=0)
f.ex("B1", "Vertaling", "Donderdag speelt Rusland tegen Oezbekistan.", "Let op: играть + с + instrumentalis",
     "В четверг сборная России играет с Узбекистаном. → ___", instr="Vertaal naar het Nederlands", size=13.8, gap=0)
f.ex("B2", "Vertaling", "Fijne Dag van de Politie allemaal!", "поздравляю + с + instrumentalis",
     "Поздравляю с Днём полиции! → ___", instr="Vertaal naar het Nederlands", size=13.8, gap=0)
f.head("F · СЛОВА НЕДЕЛИ", 21, OLIVE, 5)
f.match_set("B2", "Woorden koppelen",
            ["предзимье", "посылка", "пик", "гололедица"],
            ["самое большое число заказов",
             "лёд на дороге",
             "время между осенью и зимой",
             "товар, который прислали по почте"],
            ["c", "d", "a", "b"],
            ["voorwinter c", "pakket d", "hoogtepunt a", "gladheid op de weg b"],
            instr="Koppel")
f.head("G · ДИАЛОГ В ПУНКТЕ ВЫДАЧИ", 21, OLIVE, 5)
f.ex("B1", "Meerkeuze", "A", "Pakket ophalen: номер заказа",
     "— Здравствуйте! Я пришла за посылкой. Вот ___ заказа. (A. номер · B. пик)", size=13.8, gap=0)
f.ex("B1", "Meerkeuze", "B", "Het pakket is aangekomen",
     "— Да, ваша посылка уже ___. (A. ушла · B. пришла)", size=13.8, gap=0)
f.ex("B1", "Meerkeuze", "A", "Controleer het pakket alstublieft",
     "— Проверьте ___, пожалуйста. (A. посылку · B. промокод)", size=13.8, gap=0)
f.ex("B1", "Meerkeuze", "A", "Alles is in orde",
     "— Всё в порядке, спасибо! Книга ___. (A. целая · B. мокрая)", size=13.8, gap=0)
f.ex("B1", "Meerkeuze", "B", "Veel winkelplezier",
     "— Спасибо! Хороших ___! (A. скидок · B. покупок)", size=13.8, gap=0)
f.head("H · НАПИШИТЕ САМИ", 21, OLIVE, 5)
MODELO = ("Моя обычная неделя в ноябре начинается в понедельник, 9 ноября. "
          "В понедельник и во вторник я работаю, а вечером читаю книгу. "
          "Во вторник, 10 ноября, я поздравляю знакомого полицейского с Днём полиции. "
          "В среду, 11 ноября, — день распродажи 11.11: я заказываю книгу и проверяю промокод. "
          "В четверг я получаю посылку и проверяю покупку. "
          "В пятницу вечером я иду в кино с друзьями. "
          "В субботу я высыпаюсь и гуляю в парке, а в воскресенье готовлюсь к новой неделе. "
          "Обычная неделя мне нравится: ровный ритм — это хорошо!")
NWORDS = len(MODELO.split())
f.bridge(f"Schrijfopdracht (geen uniek antwoord); modeltekst ({NWORDS} woorden) hieronder.")
f.ex("B1", "Schrijven", "(Open opdracht, modeltekst hieronder)", f"Zie de modeltekst in deel H van deze pagina ({NWORDS} woorden)",
     "«Моя обычная неделя в ноябре» Напишите 80–100 слов: что вы будете делать каждый день недели?", instr="Schrijven", size=13.8, gap=0)
f.para("Пример: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "ОТВЕТЫ · ANTWOORDEN — PER PAGINA GERANGSCHIKT; ZOEK HET OPGAVENUMMER", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Elk antwoord met een korte Nederlandse toelichting · ✓ = modeltekst", 19.5, "sans", False, GREY, anchor="end")
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
