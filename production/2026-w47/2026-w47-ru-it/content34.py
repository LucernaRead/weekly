# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · КУЛЬТУРА (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("КУЛЬТУРА　CULTURA", "Lucerna", "УРОВЕНЬ A2 → B1　Кино 19 ноября: пять премьер　Cinque prime il 19 novembre")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P3-feature")
f.title("Кино 19 ноября: пять премьер", 32)
f.byline("От редакции Lucerna　Уровень чтения: A2 → B1")
f.para("В ноябре вечера тёмные и долгие: в Москве солнце садится около 16:20. Самое время пойти в кино! В четверг, 19 ноября, в прокат выходят сразу пять новых фильмов — на любой вкус.")
f.para("«Рокки — это я» — биография: история Сильвестра Сталлоне и его пути к фильму «Рокки». Фильм снял Питер Фаррелли, автор «Зелёной книги».")
f.para("«Бумажный тигр» — криминальная драма Джеймса Грэя, её показали на Каннском фестивале 2026 года. А «Увидеть всё» — документальный фильм студии A24 об Элизабет Холмс, основательнице стартапа Theranos.")
f.para("Семьям — тоже есть что посмотреть: добрая комедия «Дедмобиль» с Юрием Стояновым и сказочное фэнтези «Колотун и Волшебное королевство». А уже 26 ноября — «Голодные игры: Рассвет жатвы»!")
f.gloss("биография biopic · криминальная poliziesco · сказочное da favola.")
f.head("А ЧТО УЖЕ В КИНО?", 25)
f.para("С 12 ноября в прокате — «Лиля», история Лили Брик, музы Владимира Маяковского, и «Лес», экранизация романа Светланы Тюльбашевой. Хороший план на тёмный ноябрьский вечер — сначала один фильм, потом другой!")
f.para("Не забудьте: ноябрьские вечера холодные. Тёплая одежда — лучший друг кинозрителя, как и зонт по дороге в кино.")
f.gloss("экранизация adattamento cinematografico · кинозрителя spettatore.")
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
p.text(MX, ey + 28, "УПРАЖНЕНИЯ　ESERCIZI DI PAGINA 3", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Risposte a pagina 8　I livelli possono essere mescolati; cerca per numero di esercizio", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A　ПОНИМАНИЕ", 25)
e.bridge("Leggi la pagina 3 e scegli la risposta corretta.")
e.ex("A2", "Scelta multipla", "B", "19 novembre — cinque prime",
     "Сколько премьер выходит 19 ноября? A. Три · B. Пять · C. Двенадцать", size=20, gap=8)
e.ex("A2", "Scelta multipla", "A", "Rocky, sono io è un biopic su Stallone",
     "«Рокки — это я» — это... A. биография Сталлоне · B. комедия · C. хоррор", size=20, gap=8)
e.ex("A2", "Scelta multipla", "B", "Tigre di carta è stato presentato a Cannes 2026",
     "«Бумажный тигр» показали... A. в Москве · B. на Каннском фестивале · C. на стриминге", size=20, gap=8)
e.ex("A2", "Scelta multipla", "C", "Vedere tutto parla di Elizabeth Holmes",
     "«Увидеть всё» — это фильм о... A. Сталлоне · B. Лиле Брик · C. Элизабет Холмс", size=20, gap=8)
e.ex("B1", "Scelta multipla", "A", "Hunger Games esce il 26 novembre",
     "«Голодные игры: Рассвет жатвы» выходят... A. 26 ноября · B. 19 ноября · C. 12 ноября", size=20, gap=8)
e.head("B　ГЛАГОЛЫ И ФОРМЫ", 25)
e.bridge("Metti la forma verbale o il caso giusti.")
e.ex("B1", "Completare", "выходят", "выходить → выходят",
     "19 ноября в прокат ___ пять фильмов. (выходить)", instr="Completare", size=20, gap=8)
e.ex("B1", "Completare", "рассказывает", "рассказывать → рассказывает",
     "Фильм ___ о жизни Сталлоне. (рассказывать)", instr="Completare", size=20, gap=8)
e.ex("B1", "Completare", "снял", "снять → снял",
     "Фильм ___ Питер Фаррелли. (снять)", instr="Completare", size=20, gap=8)
e.ex("A2", "Completare", "посмотреть", "посмотреть = guardare",
     "Вечером можно ___ фильм в кино. (посмотреть)", instr="Completare", size=20, gap=8)
e.ex("B1", "Completare", "ноября", "19 + genitivo: ноября",
     "Премьеры будут 19 ___. (ноябрь)", instr="Completare", size=20, gap=8)
e.head("C　КИНО", 25)
e.match_set("B1", "Abbinamento",
            ["биография", "документальный", "сеанс", "зритель"],
            ["человек, который смотрит фильм",
             "фильм о жизни реального человека",
             "показ фильма в кинотеатре",
             "фильм о реальных событиях"],
            ["b", "d", "c", "a"],
            ["biopic b", "Documentario d", "spettacolo c", "spettatore a"],
            instr="Abbina")
e.head("D　СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 25)
e.bridge("Forma frasi corrette con le parole.")
e.ex("A2", "Frasi", "Пять премьер выходят 19 ноября.", "Soggetto + verbo + tempo",
     "пять премьер / выходят / 19 ноября → ___", instr="Frasi", size=20, gap=8)
e.ex("A2", "Frasi", "Питер Фаррелли снял этот фильм.", "Soggetto + verbo + oggetto",
     "Питер Фаррелли / снял / этот фильм → ___", instr="Frasi", size=20, gap=8)
e.ex("B1", "Frasi", "В ноябре солнце садится около 16:20.", "Il sole tramonta verso le 16:20",
     "в ноябре / солнце / садится около 16:20 → ___", instr="Frasi", size=20, gap=8)
e.ex("B1", "Frasi", "Вечером можно посмотреть фильм в кино.", "potere + infinito",
     "вечером / можно / посмотреть фильм в кино → ___", instr="Frasi", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-kultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · СПОРТ (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("СПОРТ　SPORT", "Lucerna", "УРОВЕНЬ B1　14-й тур: все восемь результатов + сборная　14ª giornata: tutti e otto i risultati + la nazionale")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1020, tag="P4-main")
f.title("14-й тур: все восемь результатов", 32)
f.byline("От спортивной редакции Lucerna　Уровень чтения: B1")
f.para("14-й тур сыграли 6–8 ноября — все восемь матчей завершены. «Зенит» и «Динамо» набрали по 31 очку и делят первое место. «Спартак» — третий (29 очков), а «Краснодар» и ЦСКА — по 26.")
f.para("Самый яркий матч тура — «Краснодар» — ЦСКА 4:2. «Зенит» сыграл вничью с «Ростовом» 2:2: гости сравняли счёт на 83-й минуте. «Динамо» победило «Факел» 2:1 — победный гол на 90+1-й минуте. А «Локомотив» проиграл «Рубину» 0:1 и оказался на 15-м месте, в зоне вылета.")
f.para("Поправка к VOL.3: в прошлом номере мы напечатали только семь матчей тура. Восьмой матч — «Балтика» — «Динамо» Махачкала 0:1 (8 ноября, 20:45). Спасибо внимательным читателям!")
f.para("После паузы чемпионат возвращается 20 ноября: 15-й тур играют 20–22 ноября. А сборная России 12 ноября играла с Узбекистаном в Ташкенте, 17 ноября играет с Венесуэлой в Краснодаре — об этом справа.")
f.gloss("сравняли счёт pareggiato · поправка rettifica · в зоне вылета in zona retrocessione.")
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
p.text(MX, ty, "14-Й ТУР: РЕЗУЛЬТАТЫ　Risultati della 14ª giornata", 26, "sans", True, OLIVE)
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
p.text(MX, ty2, "СБОРНАЯ: ТАШКЕНТ И КРАСНОДАР　Nazionale: Tashkent e Krasnodar", 26, "sans", True, OLIVE)
nteam = ("12 ноября, четверг, 18:00 (Москва): Узбекистан — Россия, Ташкент, стадион «Пахтакор». "
         "Результат на момент сдачи номера (10 ноября) неизвестен — полный итог в VOL.5. "
         "17 ноября, вторник, 19:00: Россия — Венесуэла, Краснодар, «Ozon Арена». "
         "Первая встреча сборных в истории; матч посвящён 100-летию Никиты Симоняна, команда сыграет в ретро-форме. "
         "Матч в Краснодаре закроет год для сборной. Трансляция — «Первый канал» и Okko.")
ny = p.para(MX, ty2 + 34, nteam, 20.5, "serif", False, INK, RIGHT - MX, 1.42)
ty3 = ny + 18
p.text(MX, ty3, "15-Й ТУР: 20–22 НОЯБРЯ　15ª giornata: 20–22 novembre", 26, "sans", True, OLIVE)
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
p.text(MX, ey + 28, "УПРАЖНЕНИЯ　ESERCIZI DI PAGINA 4", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Risposte a pagina 8　I livelli possono essere mescolati; cerca per numero di esercizio", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A　ПОНИМАНИЕ", 25)
e.bridge("Leggi la pagina 4 e scegli la risposta corretta.")
e.ex("B1", "Scelta multipla", "B", "La 14ª giornata ha avuto 8 partite",
     "Сколько матчей сыграли в 14-м туре? A. 7 · B. 8 · C. 9", size=19.5, gap=6)
e.ex("B1", "Scelta multipla", "B", "La grande partita di sabato: Krasnodar 4:2",
     "Какой счёт матча «Краснодар» — ЦСКА? A. 2:4 · B. 4:2 · C. 0:0", size=19.5, gap=6)
e.ex("B1", "Scelta multipla", "C", "Il Rostov ha pareggiato all'83° minuto",
     "«Ростов» сравнял счёт с «Зенитом»... A. на 15-й минуте · B. на 45-й минуте · C. на 83-й минуте", size=19.5, gap=6)
e.ex("B1", "Scelta multipla", "A", "La 15ª giornata inizia il 20 novembre",
     "15-й тур начнётся... A. 20 ноября · B. 8 ноября · C. 6 ноября", size=19.5, gap=6)
e.ex("B1", "Scelta multipla", "B", "La nazionale gioca martedì alle 19:00 a Krasnodar",
     "Сборная играет с Венесуэлой... A. в четверг в Ташкенте · B. во вторник в Краснодаре · C. в субботу в Москве", size=19.5, gap=6)
e.head("B　СЧЁТ И ДАТЫ", 25)
e.bridge("Completa con i numeri e i risultati della pagina 4.")
e.ex("A2", "Completare", "0:1", "Il Lokomotiv ha perso 0:1 contro il Rubin",
     "«Локомотив» — «Рубин» ___.", instr="Completare", size=19.5, gap=6)
e.ex("B1", "Completare", "2:2", "Lo Zenit ha pareggiato 2:2 con il Rostov",
     "«Зенит» — «Ростов» ___.", instr="Completare", size=19.5, gap=6)
e.ex("B1", "Completare", "2:0", "Il Krylia Sovetov ha battuto l'Orenburg 2:0",
     "«Крылья Советов» — «Оренбург» ___.", instr="Completare", size=19.5, gap=6)
e.ex("A2", "Completare", "0:1", "Il Baltika ha perso 0:1 contro la Dinamo di Machačkala",
     "«Балтика» — «Динамо» Мх ___.", instr="Completare", size=19.5, gap=6)
e.ex("B1", "Completare", "20:45", "Calcio d'inizio alle 20:45",
     "Матч «Балтика» — «Динамо» Мх начался в ___.", instr="Completare", size=19.5, gap=6)
e.head("C　КОМАНДЫ И МАТЧИ", 25)
e.match_set("B1", "Abbinamento",
            ["«Локомотив»", "«Краснодар»", "«Спартак»", "«Зенит»"],
            ["победил ЦСКА 4:2",
             "проиграл «Рубину» 0:1",
             "победил «Акрон» 2:1",
             "сыграл с «Ростовом» 2:2"],
            ["b", "a", "c", "d"],
            ["Lokomotiv b", "Krasnodar a", "Spartak c", "Zenit d"],
            instr="Abbina")
e.head("D　ВРЕМЯ ГЛАГОЛА", 25)
e.bridge("Completa con il tempo giusto del verbo tra parentesi.")
e.ex("B1", "Completare", "сыграли", "сыграть → сыграли",
     "14-й тур ___ 6–8 ноября. (сыграть)", instr="Completare", size=19.5, gap=6)
e.ex("B1", "Completare", "будет", "будет = sarà",
     "15-й тур ___ 20–22 ноября. (быть)", instr="Completare", size=19.5, gap=6)
e.ex("B1", "Completare", "играет", "играть → играет",
     "17 ноября сборная ___ с Венесуэлой. (играть)", instr="Completare", size=19.5, gap=6)
e.ex("B1", "Completare", "победило", "победить → победило",
     "«Динамо» ___ «Факел» 2:1. (победить)", instr="Completare", size=19.5, gap=6)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
