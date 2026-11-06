# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-de/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · ПЕРВАЯ ПОЛОСА (A2) =================
CURPAGE[0] = 1
p = BSPage4()

p.text(MX, 92, "VOL. 2 · ВТОРОЙ ВЫПУСК", 23, "sans", True, OLIVE)
p.text(975, 92, "КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · JEDE WOCHE · RUSSISCH, WIE RUSSLAND ES LIEST", 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "НЕДЕЛЯ СО 2 ПО 8 НОЯБРЯ 2026 ГОДА", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, GOLD, 1.6)
p.text(975, 262, "Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "РУССКАЯ ГАЗЕТА · VOL.2 · ПРАЗДНИК · СКИДКИ · ФУТБОЛ", 40, "serif", True, INK, anchor="middle")
p.text(975, 372, "ЕЖЕНЕДЕЛЬНАЯ ГАЗЕТА ДЛЯ ИЗУЧАЮЩИХ РУССКИЙ ЯЗЫК — НАСТОЯЩАЯ РОССИЯ, ПО-РУССКИ", 19, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)
p.text(975, 574, "RUSSISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER", 22, "sans", True, BRICK, anchor="middle")

p.rect(MX, 424, RIGHT - MX, 118, fill=DARK)
p.text(MX + 30, 478, "ОДНА СРЕДА ПОСРЕДИ НЕДЕЛИ!", 36, "sans", True, "#f3edda")
p.text(MX + 30, 522, "4 ноября — выходной, а 3 ноября — короткий день. Плюс скидки 11.11 и футбол.", 23, "serif", False, "#e8dfc8")
p.text(RIGHT - 30, 478, "DER MITTWOCH IN DER MITTE", 24, "sans", True, "#b3a06a", anchor="end")
p.text(RIGHT - 30, 522, "4. November frei · mehr auf Seite 2 und 6", 21, "sans", False, "#b3a06a", anchor="end")

hy = 580
p.text(MX, hy + 26, "ГЛАВНАЯ ТЕМА · Das Hauptthema", 22, "sans", True, BRICK)
hy = p.para(MX, hy + 92, "Одна среда посреди недели", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 30, "Праздник, скидки и футбол: как Россия живёт неделю с выходным в среду", 25, "serif", False, GREY)
hy += 46
p.text(MX, hy + 28, "От редакции Lucerna · Уровень чтения: A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Эта неделя в России — необычная. В понедельник и во вторник люди работают, а в среду — выходной. Среда, 4 ноября, — выходной посреди рабочей недели.", size=24)
f.para("Во вторник, 3 ноября, день короче на час. Это правило: день перед праздником всегда короче на один час.", size=24)
f.para("У школьников — последние дни каникул: они отдыхают со 2 по 4 ноября, а в четверг, 5 ноября, снова идут в школу.", size=24)
f.para("Всю неделю идёт распродажа 11.11: она началась 22 октября и закончится 12 ноября. А в выходные — футбол: 14-й тур чемпионата России, последний перед паузой.", size=24)
f.para("Как жить неделю с праздником посреди недели? Об этом — весь наш номер. Приятного чтения!", size=24)
f.bridge("посреди in der Mitte · короче на час eine Stunde kürzer · пауза die Pause.")
f.box("НЕДЕЛЯ В ЦИФРАХ · Zahlen", [
    ("1 — выходной посреди недели: среда, 4 ноября", "serif", False, INK, 20, 1.35),
    ("1 — час: на столько короче рабочий день 3 ноября (3. November: eine Stunde kürzer)", "serif", False, INK, 20, 1.35),
    ("12 — ноября закончится распродажа 11.11 (Ausverkauf bis 12. November)", "serif", False, INK, 20, 1.35),
    ("19:30 — начало матча «Краснодар» — ЦСКА в субботу (Samstag, 19:30)", "serif", False, INK, 20, 1.35),
])
f.head("СЕЙЧАС ВЫ · Jetzt üben", 25)
f.ex("A2", "Ausfüllen", "4", "Mittwoch, der 4. November",
     "Выходной посреди недели — ___ ноября.", size=19.5, gap=6)
f.ex("A2", "Ausfüllen", "3", "Dienstag, der 3. November",
     "Короткий день — ___ ноября.", size=19.5, gap=6)
f.ex("A2", "Ausfüllen", "час", "eine Stunde kürzer: на час",
     "День перед праздником короче на один ___.", size=19.5, gap=6)
f.ex("A2", "Ausfüllen", "5", "Donnerstag, der 5. November: zurück in die Schule",
     "Школьники снова идут в школу ___ ноября.", size=19.5, gap=6)
f.ex("A2", "Ausfüllen", "12", "Ausverkauf bis 12. November",
     "Распродажа 11.11 закончится ___ ноября.", size=19.5, gap=6)
f.ex("B1", "Ausfüllen", "последний", "последний перед паузой = der letzte Spieltag vor der Pause",
     "14-й тур — ___ тур перед паузой.", size=19.5, gap=6)
f.end_report()

gx, gw = COLX[3], CW
gy = 580
p.rect(gx, gy, gw, 700, fill=BOX, stroke=LINE, sw=1.4)
p.text(gx + 22, gy + 40, "О ЧЁМ ПИШУТ", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "СМИ · In den Medien", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Главные темы недели в российских СМИ", 19, "sans", False, GREY)
topics = [
    "Неделя с выходным в среду: как её прожить?",
    "Распродажа 11.11: скидки и промокоды",
    "14-й тур: последний перед паузой",
    "Последние дни школьных каникул",
    "Что меняется с 1 ноября?",
]
byy = gy + 150
for i, t in enumerate(topics):
    yy_t = p.para(gx + 22, byy + 22, f"{i+1}. {t}", 20, "serif", True, INK, gw - 44, 1.32)
    byy = yy_t + 26
p.text(gx + 22, gy + 636, "По российским СМИ, октябрь 2026 г.", 18.5, "sans", False, GREY)
p.text(gx + 22, gy + 664, "Nach russischen Medien, Oktober 2026", 19, "sans", False, GREY)

sy = 1296
p.rect(gx, sy, gw, 330, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(gx + 22, sy + 40, "В ЭТОМ НОМЕРЕ · Inhalt", 24, "sans", True, OLIVE)
som = [
    ("Стр. 2", "Короткий день и 1 ноября", "A2"),
    ("Стр. 3", "Праздник 4 ноября", "A2→B1"),
    ("Стр. 4", "14-й тур: футбол", "B1"),
    ("Стр. 5", "Скидки 11.11", "B1"),
    ("Стр. 6", "Неделя: разбор", "B2"),
    ("Стр. 7", "Фразы недели", "A2→B2"),
    ("Стр. 8", "Тест и все ответы", "alle"),
]
yy = sy + 82
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, BRICK)
    p.text(gx + 108, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 37

my = 1636
p.text(gx, my + 24, "СЛОВО НЕДЕЛИ · Wort der Woche", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, GOLD, 2)
y2 = p.para(gx, my + 76, "«сокращённый день» — рабочий день на час короче. 3 ноября — сокращённый день.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, y2 + 28, "сокращённый день = verkürzter Arbeitstag.", 19, "sans", False, GREY, gw, 1.35)

p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "autumn_path.jpg", ix, iy, iw, 320, par="xMidYMax slice")
caption(p, ix, iy + 320, iw,
        "Ноябрь в парке: аллея, жёлтые листья и пустые скамейки. На этой неделе — последние дни каникул.",
        "Фото: Toxer427 — лицензия CC0 (Wikimedia Commons)")
f2 = Flow(p, [(COLX[2], CW)], 1874, 2290, tag="P1-school")
f2.head("ПОСЛЕДНИЕ ДНИ КАНИКУЛ", 25)
f2.para("Понедельник, 2 ноября, — ещё каникулы. Вторник, 3 ноября, — тоже каникулы. А в среду, 4 ноября, — праздник. В четверг, 5 ноября, — снова в школу!", 22.5)
f2.para("Три дня — и снова уроки. Успейте отдохнуть! Подробнее — на 2-й странице.", 22.5)
f2.end_report()
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 1914, "КОРОТКО · Kurz", 24, "sans", True, OLIVE)
brefs = [
    ("СРЕДА", "4 ноября — выходной. 3 ноября — день на час короче."),
    ("СКИДКИ", "Распродажа 11.11 идёт всю неделю, до 12 ноября."),
    ("ФУТБОЛ", "В выходные — 14-й тур. В субботу «Краснодар» — ЦСКА в 19:30."),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, BRICK)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

qy = 2312
p.hline(MX, RIGHT, qy, GOLD, 2)
p.text(MX, qy + 36, "БЛИЦ-ВИКТОРИНА · Blitzquiz", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Seite 1 lesen, richtige Antwort wählen · Antworten auf Seite 8", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", "Ankreuzen", "B", "Mittwoch, der 4. November",
      "Выходной посреди недели — это... A. вторник · B. среда · C. пятница", size=21)
qf.ex("A2", "Ankreuzen", "B", "Der 3. November ist eine Stunde kürzer",
      "Короткий день — это... A. 2 ноября · B. 3 ноября · C. 5 ноября", size=21)
qf.ex("A2", "Ankreuzen", "C", "Ausverkauf bis 12. November",
      "Распродажа 11.11 закончится... A. 4 ноября · B. 8 ноября · C. 12 ноября", size=21)
qf.ex("A2", "Ankreuzen", "A", "Samstag: Krasnodar gegen ZSKA",
      "В субботу играют... A. «Краснодар» — ЦСКА · B. «Спартак» — «Акрон» · C. «Зенит» — «Ростов»", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-pervaya.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · ЖИЗНЬ (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("ЖИЗНЬ · Leben", "Lucerna", "УРОВЕНЬ A2 · Короткий день, 1 ноября и прошлая неделя · Kurzer Tag, 1. November und die vergangene Woche")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("Вторник короче на час", 37)
f.byline("От редакции Lucerna · Уровень чтения: A2")
f.para("Во вторник, 3 ноября, рабочий день короче на час. Это правило: день перед праздником всегда короче на один час. Если вы обычно работаете до шести, во вторник вы уйдёте в пять.")
f.para("А в среду, 4 ноября, — выходной. В четверг и в пятницу — снова рабочие дни. Получается странная неделя: два дня работаем, один день отдыхаем, два дня работаем — и выходные.")
f.para("Что делать в среду? Многие поедут на один день в другой город или к родным. Другие останутся дома: выспаться и отдохнуть тоже важно.")
f.gloss("перед праздником vor dem Feiertag · уйдёте Sie gehen (von der Arbeit) · выспаться ausschlafen.")
f.head("ЧТО МЕНЯЕТСЯ С 1 НОЯБРЯ", 25)
f.para("С 1 ноября в России меняются некоторые правила: налоги, аренда, платежи. А ещё из-за праздника меняются даты выплат: пенсии, которые должны прийти 4 ноября, придут раньше — 3 ноября.")
f.para("Проверьте свои даты: если выплата должна прийти в праздник, она придёт раньше. Это обычное правило: в праздник банки и почта не работают.")
f.gloss("выплат Zahlungen · раньше früher · почта die Post.")
f.head("ПРОШЛАЯ НЕДЕЛЯ: ЧТО БЫЛО", 25)
f.para("В воскресенье, 25 октября, ЦСКА победил «Спартак» в дерби со счётом 2:0. Оба гола забили в первом тайме: Глебов и Мусаев. В прошлом номере мы писали о дерби до игры — теперь результат известен.")
f.para("А первый снег в Москве в обещанные дни не выпал: конец октября выдался тёплым. 26 октября в Москве было +12 градусов. Прогнозы не сбылись — и это тоже новость.")
f.para("В среду, 28 октября, был День бабушек и дедушек, а в субботу, 31 октября, — Хэллоуин. Обе даты уже прошли: о них мы писали в прошлом номере.")
f.gloss("сбылись eingetroffen (von einer Prognose) · дерби ein Derby · в прошлом номере in der vorigen Ausgabe.")
f.end_report()

ix = COLX[3]
last = ["Дерби 25 октября: ЦСКА — «Спартак» 2:0.",
        "Первый снег в Москве не выпал: 26 октября было +12°.",
        "28 октября — День бабушек и дедушек.",
        "31 октября — Хэллоуин.",
        "Каникулы заканчиваются 4 ноября."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in last) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "ПРОШЛАЯ НЕДЕЛЯ", 24, "sans", True, OLIVE)
yy3 += 52
for t in last:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "А вы? Как вы проведёте среду, 4 ноября: поедете в другой город, пойдёте на ярмарку или просто выспитесь? Напишите два предложения по-русски и пришлите в редакцию: лучшие мы напечатаем в VOL.3 (страница 7, «Письма читателей»)."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Und Sie? Wie verbringen Sie den Mittwoch, den 4. November? Schreiben Sie zwei Sätze auf Russisch an die Redaktion.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "А ВЫ? · Und Sie?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Und Sie? Wie verbringen Sie den Mittwoch, den 4. November? Schreiben Sie zwei Sätze auf Russisch an die Redaktion.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

dy = 1566
p.hline(MX, RIGHT, dy - 12, GOLD, 2)
p.text(MX, dy + 28, "СЛОВА НЕДЕЛИ · Wörter der Woche", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "Четыре слова о неделе с праздником · Vier Wörter zur Woche mit Feiertag", 20, "sans", False, GREY, anchor="end")
words = [
    ("выходной", "день, когда не работают", "Ruhetag"),
    ("будни", "рабочие дни недели", "Werktage"),
    ("сокращённый день", "день на час короче", "verkürzter Arbeitstag"),
    ("отпуск", "дни отдыха от работы", "Urlaub"),
]
for i, (t, lab, cn) in enumerate(words):
    bx = COLX[i]
    p.rect(bx, dy + 52, CW, 150, fill=BOX, stroke=LINE, sw=1.4)
    p.text(bx + 22, dy + 106, t, 34, "serif", True, OLIVE)
    yy = p.para(bx + 22, dy + 140, lab, 20.5, "serif", False, INK, CW - 44, 1.32)
    p.para(bx + 22, yy + 19, cn, 19, "sans", False, GREY, CW - 44, 1.3)
p.para(MX, dy + 234, "Запомните: выходной — это день отдыха, а будни — рабочие дни. 4 ноября — выходной, а 3 ноября — сокращённый день.", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

ey = dy + 282
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "УПРАЖНЕНИЯ · Übungen zu Seite 2", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antworten auf Seite 8 · Niveaus gemischt — Aufgabe nach Nummer suchen", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A · ПОНИМАНИЕ", 25)
e.bridge("Lesen Sie die Artikel auf Seite 2 und wählen Sie die richtige Antwort.")
e.ex("A2", "Ankreuzen", "B", "Der 3. November ist eine Stunde kürzer",
     "Короткий день — это... A. 2 ноября · B. 3 ноября · C. 4 ноября", size=19, gap=6)
e.ex("A2", "Ankreuzen", "B", "Arbeitstag vor dem Feiertag: eine Stunde kürzer",
     "Почему 3 ноября короче? A. Это выходной · B. Это день перед праздником · C. Это воскресенье", size=19, gap=6)
e.ex("A2", "Ankreuzen", "A", "Die Rente für den 4. November kommt am 3. November",
     "Пенсии за 4 ноября придут... A. 3 ноября · B. 4 ноября · C. 5 ноября", size=19, gap=6)
e.ex("A2", "Ankreuzen", "C", "Derby-Ergebnis 2:0",
     "Дерби ЦСКА — «Спартак» закончилось... A. 1:0 · B. 0:0 · C. 2:0", size=19, gap=6)
e.ex("A2", "Ankreuzen", "B", "Am 26. Oktober in Moskau +12 Grad",
     "Почему первый снег не выпал? A. Было холодно · B. Было тепло: +12° · C. Был дождь", size=19, gap=6)
e.head("B · СЛОВА НЕДЕЛИ", 25)
e.bridge("Setzen Sie die Wörter von Seite 2 ein.")
e.ex("A2", "Ausfüllen", "выходной", "выходной = Ruhetag",
     "4 ноября — ___.", instr="Ausfüllen", size=19, gap=6)
e.ex("A2", "Ausfüllen", "будни", "будни = Werktage",
     "Понедельник и вторник — это ___.", instr="Ausfüllen", size=19, gap=6)
e.ex("A2", "Ausfüllen", "сокращённый", "сокращённый день = verkürzter Arbeitstag",
     "3 ноября — ___ день.", instr="Ausfüllen", size=19, gap=6)
e.ex("B1", "Ausfüllen", "отпуск", "взять отпуск = Urlaub nehmen",
     "Многие берут ___ в четверг и в пятницу.", instr="Ausfüllen", size=19, gap=6)
e.ex("B1", "Ausfüllen", "выспаться", "выспаться = ausschlafen",
     "В выходной можно хорошо ___.", instr="Ausfüllen", size=19, gap=6)
e.head("C · ЧИСЛА И ДАТЫ", 25)
e.bridge("Setzen Sie die Zahlen und Daten von Seite 1 und 2 ein.")
e.ex("A2", "Ausfüllen", "2", "Montag, der 2. November",
     "Неделя начинается ___ ноября.", instr="Ausfüllen", size=19, gap=6)
e.ex("B1", "Ausfüllen", "5", "Donnerstag, der 5. November: zurück in die Schule",
     "Школьники идут в школу ___ ноября.", instr="Ausfüllen", size=19, gap=6)
e.ex("A2", "Ausfüllen", "12", "Ausverkauf bis 12. November",
     "Распродажа закончится ___ ноября.", instr="Ausfüllen", size=19, gap=6)
e.ex("B1", "Ausfüllen", "25", "Derby am 25. Oktober",
     "Дерби было ___ октября.", instr="Ausfüllen", size=19, gap=6)
e.head("D · ПРОШЛАЯ НЕДЕЛЯ", 25)
e.match_set("A2", "Zuordnen",
            ["25 октября", "26 октября", "28 октября", "31 октября"],
            ["День бабушек и дедушек",
             "Хэллоуин",
             "дерби ЦСКА — «Спартак» 2:0",
             "в Москве было +12 градусов"],
            ["c", "d", "a", "b"],
            ["Derby c", "+12 Grad d", "Großelterntag a", "Halloween b"],
            instr="Paare zuordnen")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-zhizn.svg")
print("P2 saved, exercises so far:", len(REG))
