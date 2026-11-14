# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("ÜBUNGEN & ANTWORTEN　Упражнения и ответы", "Die Lucerna", "SCHLUSSTEST　Итоговый тест　Alle Antworten unten auf dieser Seite — все ответы внизу этой страницы")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1505, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "B", "schnitzen = вырезать тыкву"),
    ("A2", "A", "geht in die Bibliothek = идёт в библиотеку"),
    ("A2", "A", "Uhr zurückgestellt = часы переведены назад"),
    ("A2", "C", "Winterzeit = начинается зимнее время"),
    ("A2", "B", "eine Stunde länger = спать на час дольше"),
    ("A2", "A", "der erste Frost = первый мороз"),
    ("B1", "B", "gefällt mir gut = мне очень нравится"),
    ("A2", "C", "ich gehe (1-е лицо)"),
]
cnums = [reg_ex(lv, "Заполните пропуски", k, nt) for lv, k, nt in cloze_defs]
bf.head("A　LÜCKENTEXT　Пропуски", 24)
bf.para(f"Jonas freut sich auf das Wochenende. Am Samstag kauft er einen Kürbis und ({cnums[0]})___ ihn zu Hause. Am Nachmittag ({cnums[1]})___ er in die Bibliothek — sie hat am Samstag ein besonderes Programm. Am Abend spielt Dortmund, und Jonas sieht das Spiel mit Freunden. In der Nacht wird die Uhr ({cnums[2]})___: Die ({cnums[3]})___ beginnt. Am Sonntag schläft Jonas eine Stunde ({cnums[4]})___. Draußen ist es kalt, der erste ({cnums[5]})___ ist da. „Ein Sonntag mit 25 Stunden“, sagt Jonas, „({cnums[6]})___ mir gut! Und am Montag ({cnums[7]})___ ich wieder in die Schule.“", 20.5)
bf.expl("Варианты:")
for n, opts in zip(cnums, [
    "A. kocht · B. schnitzt · C. malt",
    "A. geht · B. schläft · C. kocht",
    "A. zurückgestellt · B. vorgestellt · C. vergessen",
    "A. Sommerzeit · B. Ferienzeit · C. Winterzeit",
    "A. früh · B. länger · C. laut",
    "A. Frost · B. Sommer · C. Frühling",
    "A. geht · B. gefällt · C. macht",
    "A. gehen · B. gehst · C. gehe",
]):
    bf.para(f"{n}. {opts}", 18.5, "sans", False, INK, 1.32, 2)

# ---- B. general MC ----
bf.head("B　WISSENSFRAGEN　Вопросы", 24)
bf.ex("B1", "Выбор ответа", "A", "День библиотек — в память о Пройскере",
      "Der Tag der Bibliotheken erinnert an... A. Karl Preusker · B. Martin Luther · C. Lucas Cranach", size=19.5, gap=8)
bf.ex("A2", "Выбор ответа", "B", "в воскресенье в 3 часа — назад",
      "Die Uhr wird umgestellt am... A. Freitag um 20.30 Uhr · B. Sonntag um 3.00 Uhr · C. Samstag um Mitternacht", size=19.5, gap=8)
bf.ex("A2", "Выбор ответа", "A", "O bis O = с октября до Пасхи",
      "„Von O bis O“ heißt: Winterreifen von... A. Oktober bis Ostern · B. Oktober bis Oktober · C. Ostern bis Oktober", size=19.5, gap=8)
bf.ex("B1", "Выбор ответа", "B", "Классикер — в Дортмунде",
      "Am 31. Oktober spielen die Bayern... A. zu Hause · B. in Dortmund · C. in Berlin", size=19.5, gap=8)
bf.ex("B1", "Выбор ответа", "B", "защита формируется за 10–14 дней",
      "Die Grippeimpfung schützt nach... A. 2 Tagen · B. 10 bis 14 Tagen · C. 3 Monaten", size=19.5, gap=8)
bf.ex("B1", "Выбор ответа", "B", "в аптеках прививают с 18 лет",
      "In Apotheken impft man Menschen... A. ab 6 Jahren · B. ab 18 Jahren · C. nur ab 60", size=19.5, gap=8)
bf.ex("A2", "Выбор ответа", "B", "главный матч субботы: Дортмунд — Франкфурт",
      "Das Topspiel am Samstag ist... A. Freiburg–Bayern · B. Dortmund–Frankfurt · C. Stuttgart–Gladbach", size=19.5, gap=8)
bf.ex("A2", "Выбор ответа", "B", "час с 2 до 3 бывает дважды",
      "Die Stunde 2.00–3.00 Uhr gibt es in der Nacht... A. einmal · B. zweimal · C. gar nicht", size=19.5, gap=8)

# ---- C. reading ----
bf.head("C　LESEVERSTEHEN　Чтение", 24)
bf.para("Frau Berger arbeitet in einer Berliner Bibliothek. Am Samstag, dem 24. Oktober, beginnt sie um halb zehn mit der Arbeit. Heute ist der Tag der Bibliotheken: Um elf Uhr spielt sie mit den Kindern Bibliotheks-Bingo. Am Nachmittag hilft sie bei den Book-Blind-Dates. Um 18 Uhr schließt die Bibliothek. Frau Berger fährt nach Hause und stellt am Abend alle Uhren um — morgen darf sie eine Stunde länger schlafen.", 20.5)
bf.ex("B1", "Выбор ответа", "A", "halb zehn = 9:30",
      "Wann beginnt Frau Berger mit der Arbeit? A. um 9.30 Uhr · B. um 10.30 Uhr · C. um halb elf", size=19.5, gap=8)
bf.ex("A2", "Выбор ответа", "B", "в 11 часов — бинго с детьми",
      "Was spielt sie um elf Uhr mit den Kindern? A. Fußball · B. Bibliotheks-Bingo · C. Karten", size=19.5, gap=8)
bf.ex("A2", "Выбор ответа", "B", "вечером дома переводит часы",
      "Was macht sie am Abend zu Hause? A. Sie schnitzt einen Kürbis. · B. Sie stellt die Uhren um. · C. Sie liest ein Buch.", size=19.5, gap=8)
bf.ex("B1", "Выбор ответа", "B", "часы переводят назад — можно спать дольше",
      "Warum darf sie am Sonntag länger schlafen? A. Die Bibliothek ist zu. · B. Die Uhr wird zurückgestellt. · C. Sie hat Urlaub.", size=19.5, gap=8)

# ---- D. sentence building ----
bf.head("D　SÄTZE BAUEN　Предложения", 22)  # D5 fix run2
bf.ex("A2", "Составьте предложение", "Die Uhr wird am Sonntag zurückgestellt.", "wird — второе место, Partizip — в конце",
      "die Uhr / wird / am Sonntag / zurückgestellt → ___", instr="Составьте", size=19.5, gap=8)
bf.ex("A2", "Составьте предложение", "Wir schlafen eine Stunde länger.", "подлежащее — сказуемое — дополнение",
      "wir / schlafen / eine Stunde / länger → ___", instr="Составьте", size=19.5, gap=8)
bf.ex("B1", "Составьте предложение", "Die Kinder freuen sich, weil Ferien sind.", "с weil глагол — в конце",
      "die Kinder / freuen sich / weil / Ferien / sind → ___", instr="Составьте", size=19.5, gap=8)
bf.ex("B1", "Составьте предложение", "Am Samstag ist der Tag der Bibliotheken.", "сначала время, глагол — второй",
      "am Samstag / ist / der Tag / der Bibliotheken → ___", instr="Составьте", size=19.5, gap=8)

# ---- E. translation ----
bf.head("E　ÜBERSETZEN　Перевод", 24)
bf.ex("A2", "Перевод", "Эта ночь длится 25 часов.", "Stunden = часы",
      "Die Nacht hat 25 Stunden. (RU)", instr="Переведите", size=19.5, gap=8)
bf.ex("A2", "Перевод", "В субботу вечером я перевожу часы.", "umstellen = переводить (часы)",
      "Ich stelle die Uhr am Samstagabend um. (RU)", instr="Переведите", size=19.5, gap=8)
bf.ex("B1", "Перевод", "Am Sonntag schlafe ich eine Stunde länger.", "спать на час дольше = eine Stunde länger schlafen",
      "В воскресенье я сплю на час дольше. (DE)", instr="Переведите", size=19.5, gap=8)
bf.ex("B1", "Перевод", "In der Bibliothek kann man Bücher leihen.", "kann man ... leihen = можно брать",
      "В библиотеке можно брать книги. (DE)", instr="Переведите", size=19.5, gap=8)

# ---- F. matching ----
bf.head("F　WÖRTER PAAREN　Пары слов", 24)
bf.match_set("B1", "Соедините пары",
             ["die Umstellung", "die Mitgliedstaaten", "die Mehrheit", "der Feiertag"],
             ["ein Tag, an dem man nicht arbeiten muss",
              "der Wechsel zwischen Sommer- und Winterzeit",
              "die Länder, die zu einer Union gehören",
              "mehr als die Hälfte, zum Beispiel 84 Prozent"],
             ["b", "c", "d", "a"],
             ["Umstellung = переход между летним и зимним временем b", "Mitgliedstaaten = государства-члены c", "Mehrheit = большинство d", "Feiertag = государственный праздник a"],
             instr="Соедините пары")

# ---- G. dialogue ----
ddefs = [
    ("A2", "A", "Buch = книга (сыну)"),
    ("B1", "B", "im ersten Stock = второй этаж (по-немецки — первый)"),
    ("A2", "C", "Bingo = библиотечное бинго"),
    ("B1", "A", "Bibliotheksausweis = читательский билет"),
    ("B1", "B", "behalten = держать у себя"),
]
dnums = [reg_ex(lv, "Дополните диалог", k, nt) for lv, k, nt in ddefs]
bf.head("G　DIALOG　Дополните диалог", 24)
bf.para(f"— Guten Tag! Ich suche ein Buch für meinen Sohn. — Gern. Wie alt ist er? — Er ist neun, und er mag Tiere. — Dann ist dieses ({dnums[0]})___ perfekt: „Tiere im Herbst“. Mehr Tierbücher finden Sie im ersten ({dnums[1]})___. — Danke! Gibt es heute auch das ({dnums[2]})___? — Ja, um elf Uhr im Kinderzimmer. Bitte zeigen Sie mir noch Ihren ({dnums[3]})___. — Hier ist er. Wie lange kann ich das Buch ({dnums[4]})___? — Drei Wochen. Viel Spaß beim Lesen!", 20.5)
bf.expl("Варианты:")
for n, opts in zip(dnums, [
    "A. Buch · B. Bett · C. Brot",
    "A. Keller · B. Stock · C. Garten",
    "A. Fußball · B. Kino · C. Bingo",
    "A. Bibliotheksausweis · B. Bibliotheksausflug · C. Bibliotheksautor",
    "A. essen · B. behalten · C. singen",
]):
    bf.para(f"{n}. {opts}", 18.5, "sans", False, INK, 1.32, 2)
bf.end_report()

# ---- writing strip ----
wy = 1520
p.hline(MX, RIGHT, wy - 14, OLIVE, 2)
reg_ex("B1", "Письмо", "открытое задание — пункты в рамке задания; образец — в рамке на этой странице", "оценка по пунктам")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H　SCHREIBEN　Письмо", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Schreiben Sie einen kurzen Text (80 bis 100 Wörter): «Mein Sonntag, der 25. Oktober». Erzählen Sie: Wie lange schlafen Sie? Was machen Sie am Morgen, am Nachmittag und am Abend? Schreiben Sie auch einen Satz über die Uhr! Die besten Texte drucken wir in VOL.2 (Seite 7, «Leserbriefe»).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 196, "Напишите по-немецки короткий текст (80–100 слов): «Моё воскресенье, 25 октября». Расскажите: как долго вы спите? Что вы делаете утром, днём и вечером? Напишите также одно предложение о часах.", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 276, fill=BOX)
p.text(mx2 + 22, wy + 38, "MUSTER　Образец (87 Wörter)", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "Am Sonntag, dem 25. Oktober, schlafe ich eine Stunde länger. Dann frühstücke ich langsam mit meiner Familie. Um elf Uhr gehe ich in den Park, denn die Sonne scheint. Am Nachmittag lese ich mein neues Buch aus der Bibliothek. Am Abend koche ich eine Suppe mit Kürbis. Danach rufe ich meine Freundin an. Wir sprechen über das Fußballspiel am Samstag. Dortmund hat gewonnen, und wir freuen uns. Der Sonntag mit 25 Stunden ist mein Lieblingstag. Ich gehe früh ins Bett, denn am Montag beginnt die Arbeit wieder.", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 296
p.hline(MX, RIGHT, ky - 12, OLIVE, 2)
p.text(MX, ky + 26, "ANTWORTEN　Все ответы и пояснения (страницы 1–8)", 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2560, tag="P8-keys")
from itertools import groupby
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— СТРАНИЦА {pg} —", 17, "sans", True, OLIVE, 1.28, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"]:
            s += f" ({e['note']})"
        parts.append(s)
    kf.para(" · ".join(parts), 13.0, "sans", False, INK, 1.16, 9)
kf.end_report()
p.foot(8)
p.save(f"{OUT}/p8-uebungen.svg")
print("P8 saved, TOTAL exercises:", len(REG))
