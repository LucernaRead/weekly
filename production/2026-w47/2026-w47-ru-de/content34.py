# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · КУЛЬТУРА (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("КУЛЬТУРА　KULTUR", "Lucerna", "УРОВЕНЬ A2 → B1　Кино 19 ноября: пять премьер　Fünf Premieren am 19. November")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P3-feature")
f.title("Кино 19 ноября: пять премьер", 32)
f.byline("От редакции Lucerna　Уровень чтения: A2 → B1")
f.para("В ноябре вечера тёмные и долгие: в Москве солнце садится около 16:20. Самое время пойти в кино! В четверг, 19 ноября, в прокат выходят сразу пять новых фильмов — на любой вкус.")
f.para("«Рокки — это я» — биография: история Сильвестра Сталлоне и его пути к фильму «Рокки». Фильм снял Питер Фаррелли, автор «Зелёной книги».")
f.para("«Бумажный тигр» — криминальная драма Джеймса Грэя, её показали на Каннском фестивале 2026 года. А «Увидеть всё» — документальный фильм студии A24 об Элизабет Холмс, основательнице стартапа Theranos.")
f.para("Семьям — тоже есть что посмотреть: добрая комедия «Дедмобиль» с Юрием Стояновым и сказочное фэнтези «Колотун и Волшебное королевство». А уже 26 ноября — «Голодные игры: Рассвет жатвы»!")
f.gloss("биография Filmbiografie · криминальная Krimi- · сказочное Märchen-.")
f.head("А ЧТО УЖЕ В КИНО?", 25)
f.para("С 12 ноября в прокате — «Лиля», история Лили Брик, музы Владимира Маяковского, и «Лес», экранизация романа Светланы Тюльбашевой. Хороший план на тёмный ноябрьский вечер — сначала один фильм, потом другой!")
f.para("Не забудьте: ноябрьские вечера холодные. Тёплая одежда — лучший друг кинозрителя, как и зонт по дороге в кино.")
f.gloss("экранизация Verfilmung · кинозрителя Kinobesucher.")
f.end_report()

ix = COLX[3]
facts = ["19 ноября — пять премьер сразу.",
         "«Рокки — это я»: биография Сталлоне.",
         "«Бумажный тигр»: Канны-2026.",
         "«Увидеть всё»: документальный фильм A24.",
         "26 ноября — «Голодные игры».",
         "В Москве темнеет около 16:20."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "ГЛАВНОЕ — КОРОТКО", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ideas = ["Вечером — в кино: «Рокки — это я».",
         "С семьёй: «Дедмобиль» или «Колотун».",
         "С друзьями: обсудить фильм после сеанса."]
sy3b = sy3 + sh + 24
shb = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in ideas) + 32
p.rect(ix, sy3b, CW, shb, fill="#f0eee5")
yy3 = sy3b + 16
p.text(ix + 22, yy3 + 26, "КАК ПРОВЕСТИ ВЕЧЕР", 24, "sans", True, OLIVE)
yy3 += 52
for t in ideas:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P3 col3 ends", sy3b + shb)

ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "УПРАЖНЕНИЯ　ÜBUNGEN ZU SEITE 3", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antworten auf Seite 8　Niveaus können gemischt sein; Antworten nach Aufgabennummer suchen", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A　ПОНИМАНИЕ", 25)
e.bridge("Seite 3 lesen und die Antwort wählen.")
e.ex("A2", "Ankreuzen", "B", "19. November — fünf Premieren",
     "Сколько премьер выходит 19 ноября? A. Три · B. Пять · C. Двенадцать", size=20, gap=8)
e.ex("A2", "Ankreuzen", "A", "Rocky bin ich ist ein Stallone-Biopic",
     "«Рокки — это я» — это... A. биография Сталлоне · B. комедия · C. хоррор", size=20, gap=8)
e.ex("A2", "Ankreuzen", "B", "Papiertiger lief 2026 in Cannes",
     "«Бумажный тигр» показали... A. в Москве · B. на Каннском фестивале · C. на стриминге", size=20, gap=8)
e.ex("A2", "Ankreuzen", "C", "Alles sehen handelt von Elizabeth Holmes",
     "«Увидеть всё» — это фильм о... A. Сталлоне · B. Лиле Брик · C. Элизабет Холмс", size=20, gap=8)
e.ex("B1", "Ankreuzen", "A", "Die Tribute von Panem starten am 26. November",
     "«Голодные игры: Рассвет жатвы» выходят... A. 26 ноября · B. 19 ноября · C. 12 ноября", size=20, gap=8)
e.head("B　ГЛАГОЛЫ И ФОРМЫ", 25)
e.bridge("Setzen Sie Verbform und Kasus richtig ein.")
e.ex("B1", "Ausfüllen", "выходят", "выходить → выходят",
     "19 ноября в прокат ___ пять фильмов. (выходить)", instr="Ausfüllen", size=20, gap=8)
e.ex("B1", "Ausfüllen", "рассказывает", "рассказывать → рассказывает",
     "Фильм ___ о жизни Сталлоне. (рассказывать)", instr="Ausfüllen", size=20, gap=8)
e.ex("B1", "Ausfüllen", "снял", "снять → снял",
     "Фильм ___ Питер Фаррелли. (снять)", instr="Ausfüllen", size=20, gap=8)
e.ex("A2", "Ausfüllen", "посмотреть", "посмотреть = ansehen",
     "Вечером можно ___ фильм в кино. (посмотреть)", instr="Ausfüllen", size=20, gap=8)
e.ex("B1", "Ausfüllen", "ноября", "19 + Genitiv: ноября",
     "Премьеры будут 19 ___. (ноябрь)", instr="Ausfüllen", size=20, gap=8)
e.head("C　КИНО", 25)
e.match_set("B1", "Zuordnen",
            ["биография", "документальный", "сеанс", "зритель"],
            ["человек, который смотрит фильм",
             "фильм о жизни реального человека",
             "показ фильма в кинотеатре",
             "фильм о реальных событиях"],
            ["b", "d", "c", "a"],
            ["Biopic b", "Dokumentarfilm d", "Vorstellung c", "Zuschauer a"],
            instr="Paare zuordnen")
e.head("D　СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 25)
e.bridge("Bilden Sie richtige Sätze aus den Wörtern.")
e.ex("A2", "Sätze bilden", "Пять премьер выходят 19 ноября.", "Subjekt + Verb + Zeit",
     "пять премьер / выходят / 19 ноября → ___", instr="Sätze bilden", size=20, gap=8)
e.ex("A2", "Sätze bilden", "Питер Фаррелли снял этот фильм.", "Subjekt + Verb + Objekt",
     "Питер Фаррелли / снял / этот фильм → ___", instr="Sätze bilden", size=20, gap=8)
e.ex("B1", "Sätze bilden", "В ноябре солнце садится около 16:20.", "Die Sonne geht gegen 16:20 Uhr unter",
     "в ноябре / солнце / садится около 16:20 → ___", instr="Sätze bilden", size=20, gap=8)
e.ex("B1", "Sätze bilden", "Вечером можно посмотреть фильм в кино.", "können + Infinitiv",
     "вечером / можно / посмотреть фильм в кино → ___", instr="Sätze bilden", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-kultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · СПОРТ (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("СПОРТ　SPORT", "Lucerna", "УРОВЕНЬ B1　14-й тур: все восемь результатов + сборная　14. Spieltag: alle acht Ergebnisse + Nationalmannschaft")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1020, tag="P4-main")
f.title("14-й тур: все восемь результатов", 32)
f.byline("От спортивной редакции Lucerna　Уровень чтения: B1")
f.para("14-й тур сыграли 6–8 ноября — все восемь матчей завершены. «Зенит» и «Динамо» набрали по 31 очку и делят первое место. «Спартак» — третий (29 очков), а «Краснодар» и ЦСКА — по 26.")
f.para("Самый яркий матч тура — «Краснодар» — ЦСКА 4:2. «Зенит» сыграл вничью с «Ростовом» 2:2: гости сравняли счёт на 83-й минуте. «Динамо» победило «Факел» 2:1 — победный гол на 90+1-й минуте. А «Локомотив» проиграл «Рубину» 0:1 и оказался на 15-м месте, в зоне вылета.")
f.para("Поправка к VOL.3: в прошлом номере мы напечатали только семь матчей тура. Восьмой матч — «Балтика» — «Динамо» Махачкала 0:1 (8 ноября, 20:45). Спасибо внимательным читателям!")
f.para("После паузы чемпионат возвращается 20 ноября: 15-й тур играют 20–22 ноября. А сборная России 12 ноября играла с Узбекистаном в Ташкенте, 17 ноября играет с Венесуэлой в Краснодаре — об этом справа.")
f.gloss("сравняли счёт ausgeglichen · поправка Berichtigung · в зоне вылета in der Abstiegszone.")
f.end_report()

bx = COLX[3]
image(p, "football1912.jpg", bx, 200, CW, 250)
cy4 = caption(p, bx, 450, CW, "Сборная России по футболу на Олимпиаде 1912 года. Футболу в России — больше ста лет.",
              "Фото: автор неизвестен, 1912 — общественное достояние (Wikimedia Commons)")
tab = ["1–2. «Зенит» и «Динамо» — 31 очко.",
       "3. «Спартак» — 29 очков.",
       "4–5. «Краснодар» и ЦСКА — 26 очков.",
       "15. «Локомотив» — зона вылета."]
sy4 = cy4 + 22
sh4 = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in tab) + 32
p.rect(bx, sy4, CW, sh4, fill=BOX)
yy4 = sy4 + 16
p.text(bx + 22, yy4 + 26, "ТАБЛИЦА: ТОП-5", 24, "sans", True, OLIVE)
yy4 += 52
for t in tab:
    yy4 = p.para(bx + 22, yy4 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P4 col3 ends", sy4 + sh4)

ty = 1080
p.text(MX, ty, "14-Й ТУР: РЕЗУЛЬТАТЫ　Ergebnisse des 14. Spieltags", 26, "sans", True, OLIVE)
res14 = [
    ("Пт 6.11.", "«Локомотив» — «Рубин» 0:1"),
    ("Сб 7.11.", "«Факел» — «Динамо» 1:2"),
    ("Сб 7.11.", "«Ахмат» — «Родина» 1:0"),
    ("Сб 7.11.", "«Краснодар» — ЦСКА 4:2"),
    ("Вс 8.11.", "«Крылья Советов» — «Оренбург» 2:0"),
    ("Вс 8.11.", "«Спартак» — «Акрон» 2:1"),
    ("Вс 8.11.", "«Зенит» — «Ростов» 2:2"),
    ("Вс 8.11.", "«Балтика» — «Динамо» Мх 0:1"),
]
half = (RIGHT - MX - 28) // 2
yy = ty + 16
for col in range(2):
    cx = MX + col * (half + 28)
    y0 = yy
    for i, (d, m) in enumerate(res14[col * 4:(col + 1) * 4]):
        p.rect(cx, y0, half, 37, fill="#f4efe0" if i % 2 == 0 else "#efe8d2")
        p.text(cx + 14, y0 + 27, d, 19.5, "sans", True, OLIVE)
        p.text(cx + 130, y0 + 27, m, 20, "serif", False, INK)
        y0 += 37
    yy = max(yy, y0)
ty2 = yy + 24
p.text(MX, ty2, "СБОРНАЯ: ТАШКЕНТ И КРАСНОДАР　Nationalmannschaft: Taschkent und Krasnodar", 26, "sans", True, OLIVE)
nteam = ("12 ноября, четверг, 18:00 (Москва): Узбекистан — Россия, Ташкент, стадион «Пахтакор». "
         "Результат на момент сдачи номера (10 ноября) неизвестен — полный итог в VOL.5. "
         "17 ноября, вторник, 19:00: Россия — Венесуэла, Краснодар, «Ozon Арена». "
         "Первая встреча сборных в истории; матч посвящён 100-летию Никиты Симоняна, команда сыграет в ретро-форме. "
         "Матч в Краснодаре закроет год для сборной. Трансляция — «Первый канал» и Okko.")
ny = p.para(MX, ty2 + 34, nteam, 20.5, "serif", False, INK, RIGHT - MX, 1.42)
ty3 = ny + 18
p.text(MX, ty3, "15-Й ТУР: 20–22 НОЯБРЯ　15. Spieltag: 20.–22. November", 26, "sans", True, OLIVE)
fix15 = [
    ("Пт 20.11. 19:30", "«Ростов» — «Крылья Советов»"),
    ("Сб 21.11. 13:00", "«Оренбург» — «Балтика»"),
    ("Сб 21.11. 15:15", "«Акрон» — «Факел»"),
    ("Сб 21.11. 17:30", "«Рубин» — «Зенит»"),
    ("Сб 21.11. 19:45", "ЦСКА — «Ахмат»"),
    ("Вс 22.11. 14:00", "«Динамо» — «Краснодар»"),
    ("Вс 22.11. 16:30", "«Динамо» Мх — «Спартак»"),
    ("Вс 22.11. 19:00", "«Родина» — «Локомотив»"),
]
yy = ty3 + 16
for col in range(2):
    cx = MX + col * (half + 28)
    y0 = yy
    for i, (d, m) in enumerate(fix15[col * 4:(col + 1) * 4]):
        p.rect(cx, y0, half, 37, fill="#f4efe0" if i % 2 == 0 else "#efe8d2")
        p.text(cx + 14, y0 + 27, d, 19.5, "sans", True, OLIVE)
        p.text(cx + 250, y0 + 27, m, 20, "serif", False, INK)
        y0 += 37
    yy = max(yy, y0)
print("P4 tables end", yy)

ey = yy + 44
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "УПРАЖНЕНИЯ　ÜBUNGEN ZU SEITE 4", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antworten auf Seite 8　Niveaus können gemischt sein; Antworten nach Aufgabennummer suchen", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A　ПОНИМАНИЕ", 25)
e.bridge("Seite 4 lesen und die Antwort wählen.")
e.ex("B1", "Ankreuzen", "B", "Der 14. Spieltag hatte 8 Spiele",
     "Сколько матчей сыграли в 14-м туре? A. 7 · B. 8 · C. 9", size=19.5, gap=6)
e.ex("B1", "Ankreuzen", "B", "Das Spitzenspiel am Samstag: Krasnodar 4:2",
     "Какой счёт матча «Краснодар» — ЦСКА? A. 2:4 · B. 4:2 · C. 0:0", size=19.5, gap=6)
e.ex("B1", "Ankreuzen", "C", "Rostow glich in der 83. Minute aus",
     "«Ростов» сравнял счёт с «Зенитом»... A. на 15-й минуте · B. на 45-й минуте · C. на 83-й минуте", size=19.5, gap=6)
e.ex("B1", "Ankreuzen", "A", "Der 15. Spieltag beginnt am 20. November",
     "15-й тур начнётся... A. 20 ноября · B. 8 ноября · C. 6 ноября", size=19.5, gap=6)
e.ex("B1", "Ankreuzen", "B", "Die Nationalmannschaft spielt Dienstag um 19:00 Uhr in Krasnodar",
     "Сборная играет с Венесуэлой... A. в четверг в Ташкенте · B. во вторник в Краснодаре · C. в субботу в Москве", size=19.5, gap=6)
e.head("B　СЧЁТ И ДАТЫ", 25)
e.bridge("Lücken mit Zahlen und Spielständen von Seite 4 füllen.")
e.ex("A2", "Ausfüllen", "0:1", "Lokomotive verlor 0:1 gegen Rubin",
     "«Локомотив» — «Рубин» ___.", instr="Ausfüllen", size=19.5, gap=6)
e.ex("B1", "Ausfüllen", "2:2", "Zenit spielte 2:2 gegen Rostow",
     "«Зенит» — «Ростов» ___.", instr="Ausfüllen", size=19.5, gap=6)
e.ex("B1", "Ausfüllen", "2:0", "Krylja Sowetow besiegten Orenburg 2:0",
     "«Крылья Советов» — «Оренбург» ___.", instr="Ausfüllen", size=19.5, gap=6)
e.ex("A2", "Ausfüllen", "0:1", "Baltika verlor 0:1 gegen Dynamo Machatschkala",
     "«Балтика» — «Динамо» Мх ___.", instr="Ausfüllen", size=19.5, gap=6)
e.ex("B1", "Ausfüllen", "20:45", "Anstoß 20:45 Uhr",
     "Матч «Балтика» — «Динамо» Мх начался в ___.", instr="Ausfüllen", size=19.5, gap=6)
e.head("C　КОМАНДЫ И МАТЧИ", 25)
e.match_set("B1", "Zuordnen",
            ["«Локомотив»", "«Краснодар»", "«Спартак»", "«Зенит»"],
            ["победил ЦСКА 4:2",
             "проиграл «Рубину» 0:1",
             "победил «Акрон» 2:1",
             "сыграл с «Ростовом» 2:2"],
            ["b", "a", "c", "d"],
            ["Lokomotive b", "Krasnodar a", "Spartak c", "Zenit d"],
            instr="Paare zuordnen")
e.head("D　ВРЕМЯ ГЛАГОЛА", 25)
e.bridge("Füllen Sie die Lücken mit der richtigen Zeitform des Verbs in Klammern aus.")
e.ex("B1", "Ausfüllen", "сыграли", "сыграть → сыграли",
     "14-й тур ___ 6–8 ноября. (сыграть)", instr="Ausfüllen", size=19.5, gap=6)
e.ex("B1", "Ausfüllen", "будет", "будет = wird sein",
     "15-й тур ___ 20–22 ноября. (быть)", instr="Ausfüllen", size=19.5, gap=6)
e.ex("B1", "Ausfüllen", "играет", "играть → играет",
     "17 ноября сборная ___ с Венесуэлой. (играть)", instr="Ausfüllen", size=19.5, gap=6)
e.ex("B1", "Ausfüllen", "победило", "победить → победило",
     "«Динамо» ___ «Факел» 2:1. (победить)", instr="Ausfüllen", size=19.5, gap=6)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
