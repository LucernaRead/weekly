# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · ТЕСТ И ОТВЕТЫ =================
CURPAGE[0] = 8
p = BSPage4()
p.band("ТЕСТ И ОТВЕТЫ　TEST UND ANTWORTEN", "Lucerna", "SEITE 8　Большой тест недели + все ответы")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　ХРОНИКА НЕДЕЛИ", 21, OLIVE, 5)
f.ex("B1", "Ankreuzen", "A", "Montag, 16. November",
     "Неделя 16–22 ноября начинается ___ ноября. (A. 16 · B. 17)", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "A", "17. November — Tag der Studierenden",
     "День студента — ___ ноября. (A. 17 · B. 18)", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "B", "18. November — Geburtstag von Väterchen Frost",
     "День рождения Деда Мороза — ___ ноября. (A. 17 · B. 18)", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "A", "Dienstag — gegen Venezuela",
     "Сборная играет с Венесуэлой ___ ноября. (A. 17 · B. 12)", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "A", "Fünf Premieren am 19. November",
     "Пять премьер выходят ___ ноября. (A. 19 · B. 26)", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "A", "Der 15. Spieltag beginnt am 20. November",
     "15-й тур начнётся ___ ноября. (A. 20 · B. 15)", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "A", "Black Friday beginnt am 16. November",
     "«Чёрная пятница» на Wildberries — с ___ ноября. (A. 16 · B. 27)", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "A", "Cyber Monday ist der 30. November",
     "«Киберпонедельник» будет ___ ноября. (A. 30 · B. 27)", size=13.8, gap=0)
f.head("B　ОБЩИЕ ВОПРОСЫ", 21, OLIVE, 5)
f.ex("A2", "Ankreuzen", "B", "17. November — Tag der Studierenden",
     "Когда День студента? A. 16 ноября · B. 17 ноября · C. 18 ноября", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "B", "5 Arbeitstage in der Woche",
     "Сколько рабочих дней на этой неделе? A. 3 · B. 5 · C. 7", size=13.8, gap=0)
f.ex("B2", "Ankreuzen", "C", "Zenit und Dynamo haben je 31 Punkte",
     "Сколько очков у «Зенита» и «Динамо»? A. 26 · B. 29 · C. 31", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "A", "Krasnodar schlug ZSKA 4:2",
     "Как сыграли «Краснодар» и ЦСКА? A. 4:2 · B. 2:4 · C. 0:0", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "A", "Black Friday bei Ozon: 13. November–2. Dezember",
     "Когда «чёрная пятница» на Ozon? A. 13 ноября – 2 декабря · B. 16–30 ноября · C. 25–27 ноября", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "B", "Die Wettervorhersage: Regen mit Schneeregen",
     "Что обещают синоптики? A. Жаркое лето · B. Дождь с мокрым снегом · C. Устойчивый снег", size=13.8, gap=0)
f.ex("A2", "Ankreuzen", "B", "Dynamo Machatschkala schlug Baltika 1:0",
     "Кто победил в матче «Балтика» — «Динамо» Мх? A. «Балтика» 1:0 · B. «Динамо» Мх 1:0 · C. Ничья", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "B", "Ein Paket muss verfolgt, abgeholt, geprüft werden",
     "Что надо сделать с посылкой? A. Выбросить · B. Отследить, получить и проверить · C. Вернуть в кино", size=13.8, gap=0)
f.head("C　ЧИТАЙТЕ И ОТВЕЧАЙТЕ", 21, OLIVE, 5)
f.para("Маша учится в университете в Москве. На этой неделе у неё обычная неделя: пять учебных дней и никаких праздников. Во вторник, 17 ноября, Маша поздравляет друга-студента с Днём студента. В четверг, 19 ноября, Маша идёт в кино с друзьями: они смотрят фильм «Рокки — это я». В пятницу Маша заказывает подарок на «чёрную пятницу». А в субботу Маша получает посылку в пункте выдачи и проверяет подарок.", 15, lh=1.3, split=False)
f.ex("A2", "Ankreuzen", "B", "Mascha ist Studentin",
     "Кто такая Маша? A. Школьница · B. Студентка · C. Учительница", size=13.8, gap=0)
f.ex("A2", "Ankreuzen", "B", "Einem Studentenfreund am Dienstag gratulieren",
     "Кого Маша поздравляет во вторник? A. Деда Мороза · B. Друга-студента · C. Преподавателя", size=13.8, gap=0)
f.ex("A2", "Ankreuzen", "B", "Am Donnerstag mit Freunden ins Kino gehen",
     "Куда Маша идёт в четверг? A. В университет · B. В кино с друзьями · C. На рынок", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "B", "Das Paket am Samstag in der Abholstation holen",
     "Где Маша получает посылку? A. В кино · B. В пункте выдачи · C. В университете", size=13.8, gap=0)
f.head("D　СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 21, OLIVE, 5)
f.ex("A2", "Sätze bilden", "Во вторник Маша поздравляет друга-студента.", "Subjekt + Verb + Objekt",
     "во вторник / Маша / поздравляет друга-студента → ___", instr="Sätze bilden", size=13.8, gap=0)
f.ex("A2", "Sätze bilden", "В четверг Маша идёт в кино.", "Subjekt + Verb + Objekt",
     "в четверг / Маша / идёт в кино → ___", instr="Sätze bilden", size=13.8, gap=0)
f.ex("B1", "Sätze bilden", "В пятницу Маша заказывает подарок.", "Zeit zuerst, Verb an zweiter Stelle",
     "в пятницу / Маша / заказывает подарок → ___", instr="Sätze bilden", size=13.8, gap=0)
f.ex("B1", "Sätze bilden", "Сначала составьте список покупок.", "Imperativ + Objekt",
     "сначала / составьте / список покупок → ___", instr="Sätze bilden", size=13.8, gap=0)
f.head("E　ПЕРЕВЕДИТЕ", 21, OLIVE, 5)
f.ex("A2", "Übersetzen", "Dienstag, 17. November, Tag der Studierenden.", "Siehe Seite 2",
     "Во вторник, 17 ноября, — День студента. → ___", instr="Ins Deutsche übersetzen", size=13.8, gap=0)
f.ex("B1", "Übersetzen", "Ein Paket muss verfolgt, abgeholt und geprüft werden.", "Siehe Seite 5",
     "Посылку нужно отследить, получить и проверить. → ___", instr="Ins Deutsche übersetzen", size=13.8, gap=0)
f.ex("B1", "Übersetzen", "Am Dienstag spielt Russland gegen Venezuela.", "Achtung: играть + с + Instrumental",
     "Во вторник сборная России играет с Венесуэлой. → ___", instr="Ins Deutsche übersetzen", size=13.8, gap=0)
f.ex("B2", "Übersetzen", "Allen einen schönen Tag der Studierenden!", "поздравляю + с + Instrumental",
     "Поздравляю с Днём студента! → ___", instr="Ins Deutsche übersetzen", size=13.8, gap=0)
f.head("F　СЛОВА НЕДЕЛИ", 21, OLIVE, 5)
f.match_set("B2", "Zuordnen",
            ["оттепель", "распродажа", "счёт", "гололедица"],
            ["результат матча, например 2:2",
             "лёд на дороге",
             "тепло зимой: снег тает",
             "большая продажа со скидками"],
            ["c", "d", "a", "b"],
            ["Tauwetter c", "Großer Ausverkauf d", "Spielstand a", "Glatteis b"],
            instr="Paare zuordnen")
f.head("G　ДИАЛОГ В МАГАЗИНЕ", 21, OLIVE, 5)
f.ex("B1", "Ankreuzen", "A", "Ein Geschenk mit Rabatt kaufen wollen",
     "— Здравствуйте! Я хочу купить подарок со ___. (A. скидкой · B. списком)", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "B", "Heute Black Friday",
     "— Да, сегодня у нас ___. (A. пятница · B. «чёрная пятница»)", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "B", "Bitte den Rabattcode prüfen",
     "— Проверьте ___, пожалуйста. (A. посылку · B. промокод)", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "A", "Das Geschenk ist heil",
     "— Всё в порядке, спасибо! Подарок ___. (A. целый · B. мокрый)", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "B", "Viel Freude beim Einkaufen",
     "— Спасибо! Хороших ___! (A. скидок · B. покупок)", size=13.8, gap=0)
f.head("H　НАПИШИТЕ САМИ", 21, OLIVE, 5)
MODELO = ("Моя неделя 16–22 ноября начинается в понедельник, 16 ноября. "
          "В понедельник я работаю, а вечером читаю книгу. "
          "Во вторник, 17 ноября, я поздравляю друга-студента с Днём студента. "
          "В среду я пишу письмо Деду Морозу: прошу снег и хорошую зиму. "
          "В четверг, 19 ноября, я иду в кино с друзьями: мы смотрим фильм «Рокки — это я». "
          "В пятницу вечером я проверяю промокоды и заказываю подарок на «чёрную пятницу». "
          "В субботу я получаю посылку, проверяю покупку и смотрю футбол: начинается 15-й тур! "
          "В воскресенье я отдыхаю, гуляю в парке и готовлюсь к новой неделе. "
          "Мне нравится такая неделя!")
NWORDS = len(MODELO.split())
f.bridge(f"Schreibaufgabe (keine eindeutige Antwort); Mustertext ({NWORDS} Wörter) unten.")
f.ex("B1", "Schreiben", "(Offene Aufgabe, Mustertext unten)", f"Mustertext in Abschnitt H dieser Seite ({NWORDS} Wörter)",
     "«Моя неделя 16–22 ноября» Напишите 80–100 слов: что вы будете делать каждый день недели?", instr="Schreiben", size=13.8, gap=0)
f.para("Пример: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "ОТВЕТЫ　LÖSUNGEN — NACH SEITEN GEORDNET; AUFGABENNUMMER SUCHEN", 22, "sans", True, OLIVE)
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
print("P8 keys end col", af.ci, "y", af.y)
# --- Morozko image in the free space below the keys (last column only) ---
img_y = af.y + 24
img_h = 250
if af.ci == 3 and img_y + img_h + 90 < 2560:
    image(p, "morozko.jpg", COLX[3], img_y, CW, img_h)
    cy8 = caption(p, COLX[3], img_y + img_h, CW, "«Морозко»: иллюстрация Ивана Билибина, 1932 год. Зимняя сказка — к ноябрю.",
                  "Иллюстрация: Иван Билибин — общественное достояние (Wikimedia Commons)")
    print("P8 morozko ends", cy8)
else:
    print("P8 morozko SKIPPED: no room (col", af.ci, "y", af.y, ")")
p.foot(8)
p.save(f"{OUT}/p8-test.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("by type", dict(Counter(e["type"] for e in REG)))
print("model words:", NWORDS)
