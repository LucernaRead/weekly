# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · ТЕСТ И ОТВЕТЫ =================
CURPAGE[0] = 8
p = BSPage4()
p.band("ТЕСТ И ОТВЕТЫ　TEST E RISPOSTE", "Lucerna", "PAGINA 8　Il grande test della settimana + tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　ХРОНИКА НЕДЕЛИ", 21, OLIVE, 5)
f.ex("B1", "Scelta multipla", "A", "Lunedì 9 novembre",
     "Обычная неделя начинается ___ ноября. (A. 9 · B. 10)", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "B", "10 novembre — Giorno della polizia",
     "День полиции — ___ ноября. (A. 9 · B. 10)", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "A", "Giorno degli sconti: 11 novembre",
     "День распродажи 11.11 — ___ ноября. (A. 11 · B. 12)", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "A", "Giovedì contro l’Uzbekistan",
     "Сборная России играет с ___. (A. Узбекистаном · B. Венесуэлой)", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "A", "Risultati della 14ª giornata sconosciuti alla chiusura",
     "Итоги 14-го тура на момент сдачи номера ___. (A. неизвестны · B. известны)", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "A", "15ª giornata il 20 novembre",
     "15-й тур будет ___ ноября. (A. 20 · B. 15)", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "B", "Lilja esce il 12 novembre",
     "Фильм «Лиля» выходит ___ ноября. (A. 13 · B. 12)", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "A", "Un codice promozionale è un codice sconto.",
     "Промокод — это код со ___. (A. скидкой · B. списком)", size=13.8, gap=0)
f.head("B　ОБЩИЕ ВОПРОСЫ", 21, OLIVE, 5)
f.ex("A2", "Scelta multipla", "B", "10 novembre — Giorno della polizia",
     "Когда День полиции? A. 9 ноября · B. 10 ноября · C. 11 ноября", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "B", "5 giorni lavorativi nella settimana",
     "Сколько рабочих дней на этой неделе? A. 3 · B. 5 · C. 7", size=13.8, gap=0)
f.ex("B2", "Scelta multipla", "B", "10 giorni liberi a novembre",
     "Сколько выходных и праздничных дней в ноябре? A. 20 · B. 10 · C. 5", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "A", "Gli sconti sono iniziati il 22 ottobre",
     "Когда началась распродажа 11.11 на Ozon? A. 22 октября · B. 9 ноября · C. 12 ноября", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "B", "Meteorologi: possibile neve bagnata",
     "Что обещают синоптики? A. Жаркое лето · B. Первый мокрый снег · C. Устойчивый снег", size=13.8, gap=0)
f.ex("A2", "Scelta multipla", "A", "Lo Spartak ha battuto la Lokomotiv 4-0",
     "Кто победил в матче «Спартак» — «Локомотив»? A. «Спартак» 4:0 · B. «Локомотив» · C. Ничья", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "A", "13ª giornata: CSKA 0-0 Orenburg",
     "Как сыграли ЦСКА и «Оренбург»? A. 0:0 · B. 4:0 · C. 1:2", size=13.8, gap=0)
f.ex("A2", "Scelta multipla", "B", "Un pacco va tracciato, ritirato, controllato",
     "Что надо сделать с посылкой? A. Выбросить · B. Отследить, получить и проверить · C. Вернуть в кино", size=13.8, gap=0)
f.head("C　ЧИТАЙТЕ И ОТВЕЧАЙТЕ", 21, OLIVE, 5)
f.para("Маша учится в школе в Москве. На этой неделе у неё обычная неделя: пять учебных дней и никаких праздников. В среду, 11 ноября, Маша заказывает книгу на распродаже 11.11. В четверг она получает посылку в пункте выдачи и проверяет книгу. А в субботу Маша идёт в кино с друзьями: они смотрят фильм «Лиля».", 15, lh=1.3, split=False)
f.ex("A2", "Scelta multipla", "B", "La settimana di Masha è una settimana normale",
     "Какая неделя у Маши? A. Каникулы · B. Обычная неделя · C. Экзамены", size=13.8, gap=0)
f.ex("A2", "Scelta multipla", "B", "Mercoledì ordina un libro",
     "Что Маша заказывает в среду? A. Билет в кино · B. Книгу · C. Промокод", size=13.8, gap=0)
f.ex("A2", "Scelta multipla", "B", "Giovedì ritira un pacco al punto di ritiro",
     "Где Маша получает посылку? A. В кино · B. В пункте выдачи · C. В школе", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "B", "Sabato vede Lilja con un’amica",
     "Куда Маша идёт в субботу? A. В школу · B. В кино с друзьями · C. На ярмарку", size=13.8, gap=0)
f.head("D　СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 21, OLIVE, 5)
f.ex("A2", "Frasi", "В среду Маша заказывает книгу.", "Soggetto + verbo + oggetto",
     "в среду / Маша / заказывает книгу → ___", instr="Frasi", size=13.8, gap=0)
f.ex("A2", "Frasi", "В четверг она получает посылку.", "Soggetto + verbo + oggetto",
     "в четверг / она / получает посылку → ___", instr="Frasi", size=13.8, gap=0)
f.ex("B1", "Frasi", "В субботу Маша идёт в кино.", "Il tempo prima, il verbo al secondo posto",
     "в субботу / Маша / идёт в кино → ___", instr="Frasi", size=13.8, gap=0)
f.ex("B1", "Frasi", "Сначала составьте список покупок.", "Imperativo + oggetto",
     "сначала / составьте / список покупок → ___", instr="Frasi", size=13.8, gap=0)
f.head("E　ПЕРЕВЕДИТЕ", 21, OLIVE, 5)
f.ex("A2", "Traduzione", "Martedì 10 novembre — Giorno della polizia.", "Confronta pagina 2",
     "Во вторник, 10 ноября, — День полиции. → ___", instr="Traduci in italiano", size=13.8, gap=0)
f.ex("B1", "Traduzione", "Un pacco va tracciato, ritirato e controllato.", "Confronta pagina 5",
     "Посылку нужно отследить, получить и проверить. → ___", instr="Traduci in italiano", size=13.8, gap=0)
f.ex("B1", "Traduzione", "Giovedì la Russia gioca contro l’Uzbekistan.", "Attenzione: играть + с + strumentale",
     "В четверг сборная России играет с Узбекистаном. → ___", instr="Traduci in italiano", size=13.8, gap=0)
f.ex("B2", "Traduzione", "Buon Giorno della polizia a tutti!", "поздравляю + с + strumentale",
     "Поздравляю с Днём полиции! → ___", instr="Traduci in italiano", size=13.8, gap=0)
f.head("F　СЛОВА НЕДЕЛИ", 21, OLIVE, 5)
f.match_set("B2", "Abbinamento",
            ["предзимье", "посылка", "пик", "гололедица"],
            ["самое большое число заказов",
             "лёд на дороге",
             "время между осенью и зимой",
             "товар, который прислали по почте"],
            ["c", "d", "a", "b"],
            ["preinverno c", "pacco d", "picco a", "il ghiaccio sulla strada b"],
            instr="Abbina")
f.head("G　ДИАЛОГ В ПУНКТЕ ВЫДАЧИ", 21, OLIVE, 5)
f.ex("B1", "Scelta multipla", "A", "Ritirare un pacco: номер заказа",
     "— Здравствуйте! Я пришла за посылкой. Вот ___ заказа. (A. номер · B. пик)", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "B", "Il pacco è arrivato",
     "— Да, ваша посылка уже ___. (A. ушла · B. пришла)", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "A", "Per favore, controlli il pacco",
     "— Проверьте ___, пожалуйста. (A. посылку · B. промокод)", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "A", "Va tutto bene",
     "— Всё в порядке, спасибо! Книга ___. (A. целая · B. мокрая)", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "B", "Buoni acquisti",
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
f.bridge(f"Composizione (senza risposta unica); testo modello ({NWORDS} parole) sotto.")
f.ex("B1", "Composizione", "(Domanda aperta, testo modello qui sotto)", f"Vedi il testo modello nella sezione H di questa pagina ({NWORDS} parole)",
     "«Моя обычная неделя в ноябре» Напишите 80–100 слов: что вы будете делать каждый день недели?", instr="Composizione", size=13.8, gap=0)
f.para("Пример: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "ОТВЕТЫ　SOLUZIONI — ORDINATE PER PAGINA; CERCA IL NUMERO DELL’ESERCIZIO", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Ogni risposta con una breve nota in italiano　✓ = testo modello", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— СТРАНИЦА {pg} —", 13.3, "sans", True, OLIVE, lh=1.13, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Composizione":
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
