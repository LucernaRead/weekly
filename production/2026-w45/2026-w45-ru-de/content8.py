# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-de/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · ТЕСТ И ОТВЕТЫ =================
CURPAGE[0] = 8
p = BSPage4()
p.band("ТЕСТ И ОТВЕТЫ · Test und Antworten", "Lucerna", "SEITE 8 · Большой тест недели + все ответы")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · ХРОНИКА НЕДЕЛИ", 21, OLIVE, 5)
f.ex("B1", "Lückentext", "A", "Am 4. November ist frei",
     "Выходной посреди недели — ___ ноября. (A. 4 · B. 5)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "B", "Der 3. November ist ein verkürzter Arbeitstag",
     "Короткий день — ___ ноября. (A. 2 · B. 3)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Ausverkauf bis 12. November",
     "Распродажа 11.11 закончится ___ ноября. (A. 12 · B. 8)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Das Topspiel ist am Samstag",
     "Матч «Краснодар» — ЦСКА будет в ___. (A. субботу · B. пятницу)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Derby-Ergebnis 2:0",
     "Дерби ЦСКА — «Спартак» закончилось со счётом ___. (A. 2:0 · B. 0:0)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Spieltag 15 am 20. November",
     "15-й тур будет ___ ноября. (A. 20 · B. 8)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "B", "Am 5. November zurück in die Schule",
     "Школьники идут в школу ___ ноября. (A. 4 · B. 5)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Ein Promocode ist ein Rabattcode",
     "Промокод — это код со ___. (A. скидкой · B. списком)", size=13.8, gap=0)
f.head("B · ОБЩИЕ ВОПРОСЫ", 21, OLIVE, 5)
f.ex("A2", "Ankreuzen", "B", "Der 4. November ist der Tag der Volkseinheit",
     "Когда День народного единства? A. 2 ноября · B. 4 ноября · C. 5 ноября", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "B", "Mit Urlaub am Donnerstag und Freitag: 5 Tage am Stück frei",
     "Сколько дней отдыха подряд, если взять отпуск в четверг и в пятницу? A. 3 · B. 5 · C. 7", size=13.8, gap=0)
f.ex("B2", "Ankreuzen", "B", "Ruhetage: Mittwoch, Samstag, Sonntag",
     "Сколько выходных дней в неделе 2–8 ноября? A. 2 · B. 3 · C. 4", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "A", "Der Ausverkauf begann am 22. Oktober",
     "Когда началась распродажа 11.11? A. 22 октября · B. 2 ноября · C. 12 ноября", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "B", "Laut Handelspresse: Rabatte könnten geringer ausfallen",
     "Что пишет торговая пресса о скидках? A. Их будет больше · B. Их может быть меньше · C. Их не будет", size=13.8, gap=0)
f.ex("A2", "Ankreuzen", "A", "Derbysieger ist ZSKA",
     "Кто победил в дерби? A. ЦСКА · B. «Спартак» · C. Ничья", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "A", "Spieltag 13 endet am Montag",
     "Когда закрывается 13-й тур? A. 2 ноября · B. 6 ноября · C. 8 ноября", size=13.8, gap=0)
f.ex("A2", "Ankreuzen", "B", "Ein Promocode ist ein Rabattcode",
     "Что такое промокод? A. Список · B. Код со скидкой · C. Магазин", size=13.8, gap=0)
f.head("C · ЧИТАЙТЕ И ОТВЕЧАЙТЕ", 21, OLIVE, 5)
f.para("Маша учится в школе в Москве. На этой неделе у неё последние дни каникул: в среду, 4 ноября, — праздник, а в четверг — снова в школу. В среду Маша пойдёт на ярмарку с семьёй. А в субботу она будет смотреть футбол: «Краснодар» играет с ЦСКА. Маша болеет за «Краснодар».", 15, lh=1.3, split=False)
f.ex("A2", "Ankreuzen", "B", "Mascha hat die letzten Ferientage",
     "Что у Маши на этой неделе? A. Экзамены · B. Последние дни каникул · C. Новая школа", size=13.8, gap=0)
f.ex("A2", "Ankreuzen", "B", "Am Mittwoch auf den Jahrmarkt",
     "Куда Маша пойдёт в среду? A. В школу · B. На ярмарку · C. На футбол", size=13.8, gap=0)
f.ex("A2", "Ankreuzen", "B", "Am Donnerstag zurück in die Schule",
     "Когда Маша снова идёт в школу? A. В среду · B. В четверг · C. В субботу", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "B", "Mascha ist Fan von Krasnodar",
     "За кого болеет Маша? A. За ЦСКА · B. За «Краснодар» · C. За «Спартак»", size=13.8, gap=0)
f.head("D · СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 21, OLIVE, 5)
f.ex("A2", "Sätze bilden", "В четверг школьники идут в школу.", "Zeitangabe vorn, Verb an zweiter Stelle",
     "в четверг / школьники / идут в школу → ___", instr="Sätze bilden", size=13.8, gap=0)
f.ex("A2", "Sätze bilden", "Мы берём отпуск в четверг и в пятницу.", "Subjekt + Verb + Zeitangabe",
     "мы / берём отпуск / в четверг и в пятницу → ___", instr="Sätze bilden", size=13.8, gap=0)
f.ex("B1", "Sätze bilden", "В субботу будет главный матч тура.", "Zeitangabe vorn, Verb an zweiter Stelle",
     "в субботу / будет / главный матч тура → ___", instr="Sätze bilden", size=13.8, gap=0)
f.ex("B1", "Sätze bilden", "Сначала составьте список покупок.", "Imperativ + Objekt",
     "сначала / составьте / список покупок → ___", instr="Sätze bilden", size=13.8, gap=0)
f.head("E · ПЕРЕВЕДИТЕ", 21, OLIVE, 5)
f.ex("A2", "Übersetzen", "Am Mittwoch, dem 4. November, ist frei.", "Vergleichen Sie Seite 3",
     "В среду, 4 ноября, — выходной. → ___", instr="Ins Deutsche übersetzen", size=13.8, gap=0)
f.ex("B1", "Übersetzen", "Ein Promocode ist ein Rabattcode.", "Vergleichen Sie Seite 5",
     "Промокод — это код со скидкой. → ___", instr="Ins Deutsche übersetzen", size=13.8, gap=0)
f.ex("B1", "Übersetzen", "В субботу «Краснодар» играет с ЦСКА.", "Achten Sie auf: играть + с + Instrumental",
     "Am Samstag spielt Krasnodar gegen ZSKA. → ___", instr="Ins Russische übersetzen", size=13.8, gap=0)
f.ex("B2", "Übersetzen", "Поздравляю с Днём народного единства!", "поздравляю + с + Instrumental",
     "Ich wünsche allen einen schönen Tag der Volkseinheit! → ___", instr="Ins Russische übersetzen", size=13.8, gap=0)
f.head("F · СЛОВА НЕДЕЛИ", 21, OLIVE, 5)
f.match_set("B2", "Zuordnen",
            ["выходной", "промокод", "пауза", "ярмарка"],
            ["код со скидкой",
             "место, где продают еду и подарки",
             "перерыв в чемпионате",
             "день, когда не работают"],
            ["d", "a", "c", "b"],
            ["Ruhetag d", "Promocode a", "Pause c", "Jahrmarkt b"],
            instr="Paare zuordnen")
f.head("G · ДИАЛОГ В МАГАЗИНЕ", 21, OLIVE, 5)
f.ex("B1", "Lückentext", "A", "скидка = Rabatt",
     "— Здравствуйте! На эту куртку есть ___? (A. скидка · B. список)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "B", "скидка 20%",
     "— Да, сегодня ___ 20%. (A. цена · B. скидка)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "у меня есть = ich habe einen Promocode",
     "— А у меня есть ___! (A. промокод · B. выходной)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "его = der Promocode (maskulin)",
     "— Отлично! Введите ___ в приложении. (A. его · B. её)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "B", "Viel Spaß beim Einkaufen",
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
f.bridge(f"Schreibaufgabe (ohne eindeutige Lösung); der Mustertext ({NWORDS} Wörter) steht unten.")
f.ex("B1", "Schreiben", "(offene Aufgabe — Mustertext unten)", f"Der Mustertext steht in Abschnitt H dieser Seite ({NWORDS} Wörter)",
     "«Моя неделя с праздником посреди недели» Напишите 80–100 слов: что вы будете делать в среду, в выходные и куда поедете?", instr="Schreiben", size=13.8, gap=0)
f.para("Пример: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "ОТВЕТЫ · Antworten — nach Seiten geordnet; suchen Sie Ihre Nummer", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Jede Antwort mit einer kurzen deutschen Anmerkung · ✓ = Mustertext-Aufgabe", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag="P8-keys")
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
