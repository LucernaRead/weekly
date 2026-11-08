# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · ТЕСТ И ОТВЕТЫ =================
CURPAGE[0] = 8
p = BSPage4()
p.band("ТЕСТ И ОТВЕТЫ　TEST UND ANTWORTEN", "Lucerna", "SEITE 8　Der große Wochentest + alle Antworten")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　ХРОНИКА НЕДЕЛИ", 21, OLIVE, 5)
f.ex("B1", "Ankreuzen", "A", "Montag, 9. November",
     "Обычная неделя начинается ___ ноября. (A. 9 · B. 10)", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "B", "10. November — Tag der Polizei",
     "День полиции — ___ ноября. (A. 9 · B. 10)", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "A", "Rabatttag: 11. November",
     "День распродажи 11.11 — ___ ноября. (A. 11 · B. 12)", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "A", "Donnerstag gegen Usbekistan",
     "Сборная России играет с ___. (A. Узбекистаном · B. Венесуэлой)", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "A", "Ergebnisse des 14. Spieltags bei Redaktionsschluss unbekannt",
     "Итоги 14-го тура на момент сдачи номера ___. (A. неизвестны · B. известны)", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "A", "15. Spieltag am 20. November",
     "15-й тур будет ___ ноября. (A. 20 · B. 15)", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "B", "Lilja startet am 12. November",
     "Фильм «Лиля» выходит ___ ноября. (A. 13 · B. 12)", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "A", "Ein Promocode ist ein Rabattcode.",
     "Промокод — это код со ___. (A. скидкой · B. списком)", size=13.8, gap=0)
f.head("B　ОБЩИЕ ВОПРОСЫ", 21, OLIVE, 5)
f.ex("A2", "Ankreuzen", "B", "10. November — Tag der Polizei",
     "Когда День полиции? A. 9 ноября · B. 10 ноября · C. 11 ноября", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "B", "5 Arbeitstage in der Woche",
     "Сколько рабочих дней на этой неделе? A. 3 · B. 5 · C. 7", size=13.8, gap=0)
f.ex("B2", "Ankreuzen", "B", "10 freie Tage im November",
     "Сколько выходных и праздничных дней в ноябре? A. 20 · B. 10 · C. 5", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "A", "Der Sale begann am 22. Oktober",
     "Когда началась распродажа 11.11 на Ozon? A. 22 октября · B. 9 ноября · C. 12 ноября", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "B", "Wetterfrösche: nasser Schnee möglich",
     "Что обещают синоптики? A. Жаркое лето · B. Первый мокрый снег · C. Устойчивый снег", size=13.8, gap=0)
f.ex("A2", "Ankreuzen", "A", "Spartak schlug Lokomotive 4:0",
     "Кто победил в матче «Спартак» — «Локомотив»? A. «Спартак» 4:0 · B. «Локомотив» · C. Ничья", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "A", "13. Spieltag: ZSKA 0:0 Orenburg",
     "Как сыграли ЦСКА и «Оренбург»? A. 0:0 · B. 4:0 · C. 1:2", size=13.8, gap=0)
f.ex("A2", "Ankreuzen", "B", "Ein Paket muss verfolgt, abgeholt, geprüft werden",
     "Что надо сделать с посылкой? A. Выбросить · B. Отследить, получить и проверить · C. Вернуть в кино", size=13.8, gap=0)
f.head("C　ЧИТАЙТЕ И ОТВЕЧАЙТЕ", 21, OLIVE, 5)
f.para("Маша учится в школе в Москве. На этой неделе у неё обычная неделя: пять учебных дней и никаких праздников. В среду, 11 ноября, Маша заказывает книгу на распродаже 11.11. В четверг она получает посылку в пункте выдачи и проверяет книгу. А в субботу Маша идёт в кино с друзьями: они смотрят фильм «Лиля».", 15, lh=1.3, split=False)
f.ex("A2", "Ankreuzen", "B", "Maschas Woche ist eine gewöhnliche Woche",
     "Какая неделя у Маши? A. Каникулы · B. Обычная неделя · C. Экзамены", size=13.8, gap=0)
f.ex("A2", "Ankreuzen", "B", "Am Mittwoch bestellt sie ein Buch",
     "Что Маша заказывает в среду? A. Билет в кино · B. Книгу · C. Промокод", size=13.8, gap=0)
f.ex("A2", "Ankreuzen", "B", "Am Donnerstag holt sie ein Paket an der Abholstation ab",
     "Где Маша получает посылку? A. В кино · B. В пункте выдачи · C. В школе", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "B", "Am Samstag sieht sie mit einer Freundin Lilja",
     "Куда Маша идёт в субботу? A. В школу · B. В кино с друзьями · C. На ярмарку", size=13.8, gap=0)
f.head("D　СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 21, OLIVE, 5)
f.ex("A2", "Sätze bilden", "В среду Маша заказывает книгу.", "Subjekt + Verb + Objekt",
     "в среду / Маша / заказывает книгу → ___", instr="Sätze bilden", size=13.8, gap=0)
f.ex("A2", "Sätze bilden", "В четверг она получает посылку.", "Subjekt + Verb + Objekt",
     "в четверг / она / получает посылку → ___", instr="Sätze bilden", size=13.8, gap=0)
f.ex("B1", "Sätze bilden", "В субботу Маша идёт в кино.", "Zeit zuerst, Verb an zweiter Stelle",
     "в субботу / Маша / идёт в кино → ___", instr="Sätze bilden", size=13.8, gap=0)
f.ex("B1", "Sätze bilden", "Сначала составьте список покупок.", "Imperativ + Objekt",
     "сначала / составьте / список покупок → ___", instr="Sätze bilden", size=13.8, gap=0)
f.head("E　ПЕРЕВЕДИТЕ", 21, OLIVE, 5)
f.ex("A2", "Übersetzen", "Dienstag, 10. November — Tag der Polizei.", "Vergleiche Seite 2",
     "Во вторник, 10 ноября, — День полиции. → ___", instr="Ins Deutsche übersetzen", size=13.8, gap=0)
f.ex("B1", "Übersetzen", "Ein Paket muss verfolgt, abgeholt und geprüft werden.", "Vergleiche Seite 5",
     "Посылку нужно отследить, получить и проверить. → ___", instr="Ins Deutsche übersetzen", size=13.8, gap=0)
f.ex("B1", "Übersetzen", "Am Donnerstag spielt Russland gegen Usbekistan.", "Achtung: играть + с + Instrumental",
     "В четверг сборная России играет с Узбекистаном. → ___", instr="Ins Deutsche übersetzen", size=13.8, gap=0)
f.ex("B2", "Übersetzen", "Allen einen schönen Tag der Polizei!", "поздравляю + с + Instrumental",
     "Поздравляю с Днём полиции! → ___", instr="Ins Deutsche übersetzen", size=13.8, gap=0)
f.head("F　СЛОВА НЕДЕЛИ", 21, OLIVE, 5)
f.match_set("B2", "Zuordnen",
            ["предзимье", "посылка", "пик", "гололедица"],
            ["самое большое число заказов",
             "лёд на дороге",
             "время между осенью и зимой",
             "товар, который прислали по почте"],
            ["c", "d", "a", "b"],
            ["Vorwinterzeit c", "Paket d", "Höhepunkt a", "Glatteis b"],
            instr="Paare zuordnen")
f.head("G　ДИАЛОГ В ПУНКТЕ ВЫДАЧИ", 21, OLIVE, 5)
f.ex("B1", "Ankreuzen", "A", "Paket abholen: номер заказа",
     "— Здравствуйте! Я пришла за посылкой. Вот ___ заказа. (A. номер · B. пик)", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "B", "Das Paket ist da",
     "— Да, ваша посылка уже ___. (A. ушла · B. пришла)", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "A", "Bitte prüfen Sie das Paket",
     "— Проверьте ___, пожалуйста. (A. посылку · B. промокод)", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "A", "Alles ist gut",
     "— Всё в порядке, спасибо! Книга ___. (A. целая · B. мокрая)", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "B", "Viel Freude beim Einkaufen",
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
f.bridge(f"Schreibaufgabe (keine eindeutige Antwort); Mustertext ({NWORDS} Wörter) unten.")
f.ex("B1", "Schreiben", "(Offene Aufgabe, Mustertext unten)", f"Mustertext in Abschnitt H dieser Seite ({NWORDS} Wörter)",
     "«Моя обычная неделя в ноябре» Напишите 80–100 слов: что вы будете делать каждый день недели?", instr="Schreiben", size=13.8, gap=0)
f.para("Пример: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "ОТВЕТЫ　LÖSUNGEN — NACH SEITEN GEORDNET; AUFGABENNUMMER SUCHEN", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Jede Lösung mit einer kurzen deutschen Erläuterung　✓ markiert Mustertextaufgaben", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— СТРАНИЦА {pg} —", 13.3, "sans", True, OLIVE, lh=1.13, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Schreiben":
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
