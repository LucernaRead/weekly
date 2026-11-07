# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-ru-en/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · КУЛЬТУРА (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("КУЛЬТУРА · Culture", "Lucerna", "УРОВЕНЬ A2 → B1 · День лицеиста и сказки в кино · Lyceum Day and fairy-tale films")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P3-feature")
f.title("День лицеиста: праздник школы и Пушкина", 37)
f.byline("От редакции Lucerna · Уровень чтения: A2 → B1")
f.para("В понедельник, 19 октября, в России — Всероссийский день лицеиста. В этот день в 1811 году — 215 лет назад — открылся Царскосельский лицей, знаменитая школа под Санкт-Петербургом.")
f.para("Александр Пушкин учился в лицее с первого дня: он был лицеистом первого набора. Пушкин очень любил лицей и своих друзей. В стихотворении «19 октября» он написал знаменитые слова: «Друзья мои, прекрасен наш союз!»")
f.para("Сегодня лицеи и гимназии по всей России отмечают этот день: в школах проходят торжественные линейки, вечера стихов и викторины. Ученики читают стихи Пушкина и говорят о дружбе.")
f.para("Почему именно 19 октября? Потому что лицей открылся в этот день. Для Пушкина лицейские годы были очень важны: там он начал писать стихи и нашёл друзей на всю жизнь. И через много лет, уже взрослый, он каждый год вспоминал этот день.")
f.gloss("лицеистом a lyceum student · союз union, bond · набора an intake, a class.")
f.head("СКАЗОЧНЫЙ ЧЕТВЕРГ", 25)
f.para("А в четверг, 22 октября, — большой день для семей. В четверг в кино выходят сразу четыре сказки. Студии специально выбрали этот день: в субботу начинаются каникулы, и дети пойдут в кино с родителями.")
f.para("Первая сказка — «Морозко»: в роли ведьмы — Елизавета Боярская. Вторая — «Сказка о потерянном времени»: это ремейк знаменитого советского фильма. Третья — «Чудо-Юдо» с Сергеем Безруковым и Викторией Исаковой. Четвёртая — «Королевство кривых зеркал» режиссёра Клима Шипенко, по сказке Виталия Губарева.")
f.para("Все эти сказки пришли из книг и старых фильмов, которые любят в России. «Сказку о потерянном времени» написал Евгений Шварц, а «Морозко» — народная сказка: её знают все дети.")
f.gloss("ведьмы a witch · ремейк a remake · режиссёра a director (genitive).")
f.end_report()

# col 3: two images + facts box (sequential, measured)
ix = COLX[3]
image(p, "pushkin.jpg", ix, 200, CW, 300)
cy3 = caption(p, ix, 500, CW, "Александр Пушкин. Портрет написал Орест Кипренский в 1827 году.",
              "Картина: Орест Кипренский, 1827 — общественное достояние (Wikimedia Commons)")
image(p, "morozko.jpg", ix, cy3 + 22, CW, 290)
cy3b = caption(p, ix, cy3 + 22 + 290, CW, "Морозко из сказки. Так его нарисовал художник Иван Билибин.",
               "Иллюстрация: Иван Билибин, 1932 — общественное достояние (Wikimedia Commons)")
facts = ["19 октября 1811 года открылся Царскосельский лицей.",
         "Пушкин — лицеист первого набора.",
         "22 октября в кино выходят четыре сказки."]
sy3 = cy3b + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "ГЛАВНОЕ — КОРОТКО", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P3 col3 ends", sy3 + sh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "УПРАЖНЕНИЯ · Page 3 exercises", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Answers on page 8 · Levels may mix — find your item by number", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · ПОНИМАНИЕ", 25)
e.note("Read the page 3 articles and choose the right answer.")
e.ex("A2", "multiple choice", "B", "Lyceum Day is 19 October",
     "День лицеиста отмечают... A. 18 октября · B. 19 октября · C. 25 октября", size=20, gap=8)
e.ex("A2", "multiple choice", "A", "The lyceum opened in 1811",
     "Царскосельский лицей открылся в... A. 1811 году · B. 1911 году · C. 1800 году", size=20, gap=8)
e.ex("A2", "multiple choice", "B", "Pushkin was in the first intake",
     "Пушкин был лицеистом... A. последнего набора · B. первого набора · C. второго набора", size=20, gap=8)
e.ex("A2", "multiple choice", "C", "Four fairy-tale films on Thursday",
     "Сколько новых сказок выходит в четверг? A. две · B. три · C. четыре", size=20, gap=8)
e.ex("B1", "multiple choice", "A", "Because the holidays start on Saturday",
     "Почему студии выбрали четверг? A. В субботу начинаются каникулы · B. В четверг билеты дешевле · C. В четверг нет школы", size=20, gap=8)
e.head("B · ГЛАГОЛЫ И ФОРМЫ", 25)
e.note("Fill in the correct verb form or the correct case.")
e.ex("B1", "fill-in", "открылся", "открыться → открылся (past tense, masculine)",
     "Лицей ___ в 1811 году. (открыться)", instr="Fill in", size=20, gap=8)
e.ex("B1", "fill-in", "учился", "учиться → учился",
     "Пушкин ___ в лицее с первого дня. (учиться)", instr="Fill in", size=20, gap=8)
e.ex("B1", "fill-in", "написал", "написать → написал",
     "В стихотворении «19 октября» Пушкин ___ знаменитые слова. (написать)", instr="Fill in", size=20, gap=8)
e.ex("A2", "fill-in", "читают", "читать → читают (plural)",
     "В школах ученики ___ стихи Пушкина. (читать)", instr="Fill in", size=20, gap=8)
e.ex("B1", "fill-in", "режиссёра", "фильм + genitive: режиссёра",
     "«Королевство кривых зеркал» — фильм ___ Клима Шипенко. (режиссёр)", instr="Fill in", size=20, gap=8)
e.head("C · ЧЕТЫРЕ СКАЗКИ", 25)
e.match_set("B1", "matching",
            ["«Морозко»", "«Сказка о потерянном времени»", "«Чудо-Юдо»", "«Королевство кривых зеркал»"],
            ["сказка по книге Виталия Губарева, режиссёр Клим Шипенко",
             "в роли ведьмы — Елизавета Боярская",
             "фильм с Сергеем Безруковым и Викторией Исаковой",
             "ремейк знаменитого советского фильма"],
            ["b", "d", "c", "a"],
            ["«Морозко» b", "«Сказка о потерянном времени» d", "«Чудо-Юдо» c", "«Королевство кривых зеркал» a"],
            instr="Match the pairs")
e.head("D · СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 25)
e.note("Put the words in order to make a sentence.")
e.ex("A2", "sentence building", "Лицей открылся в 1811 году.", "Subject + verb + time",
     "лицей / открылся / в 1811 году → ___", instr="Build a sentence", size=20, gap=8)
e.ex("A2", "sentence building", "Пушкин учился в лицее.", "Subject + verb + place",
     "пушкин / учился / в лицее → ___", instr="Build a sentence", size=20, gap=8)
e.ex("B1", "sentence building", "В четверг выходят четыре сказки.", "Time first, verb second",
     "в четверг / выходят / четыре сказки → ___", instr="Build a sentence", size=20, gap=8)
e.ex("B1", "sentence building", "Ученики читают стихи Пушкина.", "Note the genitive: стихи Пушкина",
     "ученики / читают / стихи пушкина → ___", instr="Build a sentence", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-kultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · СПОРТ (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("СПОРТ · Sport", "Lucerna", "УРОВЕНЬ B1 · Главное дерби страны · The country's big derby")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1100, tag="P4-main")
f.title("Главное дерби страны: ЦСКА — «Спартак»", 37)
f.byline("От спортивной редакции Lucerna · Уровень чтения: B1")
f.para("Какая неделя для футбола! В пятницу, 23 октября, начинается 12-й тур чемпионата России: первый матч — «Ахмат» — «Оренбург», начало в 19:30. А главный матч тура будет в воскресенье.")
f.para("В воскресенье, 25 октября, в 16:00 по московскому времени ЦСКА играет со «Спартаком». Это главное московское дерби: два больших клуба из одного города. Мы пишем эти строки до игры, поэтому результата здесь нет: кто победил, вы узнаете в следующем номере.")
f.para("Перед дерби борьба в таблице очень плотная. Динамо — единоличный лидер: у него 25 очков. «Зенит» — второй: у него 24 очка. А «Спартак» — третий: у него 23 очка. Всё решит игра!")
f.para("В понедельник, 19 октября, закончился 11-й тур: последний матч «Родина» — «Оренбург» закончился со счётом 2:2. А «Динамо» в 11-м туре победило ЦСКА со счётом 3:1 — поэтому «Динамо» и вышло на первое место.")
f.para("Болельщики ждут дерби всю неделю: дома, на работе и в школе говорят только о футболе. ЦСКА и «Спартак» — старые соперники, и их матч — это не просто игра, а главное событие футбольной осени в Москве.")
f.gloss("дерби a derby (two clubs from one city) · тур a round · таблице the table · счёт the score.")
f.end_report()

# col 3: image + standings box
bx = COLX[3]
image(p, "football1912.jpg", bx, 200, CW, 250)
cy4 = caption(p, bx, 450, CW, "Сборная России по футболу на Олимпиаде 1912 года. Футболу в России — больше ста лет.",
              "Фото: автор неизвестен, 1912 — общественное достояние (Wikimedia Commons)")
stand = ["1. «Динамо» (Москва) — 25 очков",
         "2. «Зенит» — 24 очка",
         "3. «Спартак» — 23 очка",
         "В 11-м туре «Динамо» победило ЦСКА со счётом 3:1."]
sy4 = cy4 + 22
sh4 = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in stand) + 32
p.rect(bx, sy4, CW, sh4, fill=BOX, stroke=LINE, sw=1.4)
yy4 = sy4 + 16
p.text(bx + 22, yy4 + 26, "ТАБЛИЦА ПОСЛЕ 11 ТУРОВ", 24, "sans", True, OLIVE)
yy4 += 52
for t in stand:
    yy4 = p.para(bx + 22, yy4 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P4 col3 ends", sy4 + sh4)

# ---- round-12 table (full width) ----
ty = 1160
p.text(MX, ty, "12-Й ТУР: ГЛАВНОЕ · Round 12: the essentials", 26, "sans", True, OLIVE)
rows = [
    ("Пт 23.10.", "19:30", "«Ахмат» — «Оренбург» — первый матч 12-го тура"),
    ("23–25.10.", "3 дня", "В 12-м туре — восемь матчей за три дня"),
    ("Вс 25.10.", "16:00", "ЦСКА — «Спартак» — главное дерби страны (время московское)"),
]
yy = ty + 16
for i, (d, t, m) in enumerate(rows):
    p.rect(MX, yy, RIGHT - MX, 44, fill="#f4efe0" if i % 2 == 0 else "#efe8d2")
    p.text(MX + 18, yy + 29, d, 20.5, "sans", True, BRICK)
    p.text(MX + 185, yy + 29, t, 20, "sans", False, GREY)
    p.text(MX + 430, yy + 29, m, 21, "serif", False, INK)
    yy += 44
tnote = "Внимание: дерби будет в воскресенье — после выхода газеты. Поэтому здесь нет результата: итоги тура читайте в следующем номере."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "УПРАЖНЕНИЯ · Page 4 exercises", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Answers on page 8 · Levels may mix — find your item by number", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A · ПОНИМАНИЕ", 25)
e.note("Read the page 4 article and choose the right answer.")
e.ex("B1", "multiple choice", "B", "The derby is on Sunday",
     "Дерби ЦСКА — «Спартак» будет... A. в пятницу · B. в воскресенье · C. в понедельник", size=20, gap=8)
e.ex("B1", "multiple choice", "B", "The derby starts at 16:00",
     "Дерби начинается в... A. 19:30 · B. 16:00 · C. 12:00", size=20, gap=8)
e.ex("B1", "multiple choice", "C", "Dynamo lead the table",
     "Кто сейчас лидер чемпионата? A. «Зенит» · B. «Спартак» · C. «Динамо»", size=20, gap=8)
e.ex("B1", "multiple choice", "A", "Spartak have 23 points",
     "Сколько очков у «Спартака»? A. 23 · B. 24 · C. 25", size=20, gap=8)
e.ex("B1", "multiple choice", "B", "Rodina–Orenburg finished 2:2",
     "Матч «Родина» — «Оренбург» закончился... A. 3:1 · B. 2:2 · C. 1:0", size=20, gap=8)
e.head("B · ТАБЛИЦА И ДАТЫ", 25)
e.note("Fill in the numbers and words from page 4.")
e.ex("A2", "fill-in", "25", "Dynamo have 25 points",
     "У «Динамо» ___ очков.", instr="Fill in", size=20, gap=8)
e.ex("B1", "fill-in", "24", "Zenit have 24 points",
     "У «Зенита» ___ очка.", instr="Fill in", size=20, gap=8)
e.ex("B1", "fill-in", "третий", "third: третий (masculine nominative)",
     "«Спартак» сейчас ___ в таблице: у него 23 очка.", instr="Fill in", size=20, gap=8)
e.ex("A2", "fill-in", "пятницу", "в + accusative for a weekday: в пятницу",
     "12-й тур начинается в ___ (день недели), 23 октября.", instr="Fill in", size=20, gap=8)
e.ex("B1", "fill-in", "восемь", "eight matches in the round: восемь матчей",
     "В 12-м туре всего ___ матчей.", instr="Fill in", size=20, gap=8)
e.head("C · КОМАНДЫ И ФАКТЫ", 25)
e.match_set("B1", "matching",
            ["«Динамо»", "«Зенит»", "«Спартак»", "«Родина» и «Оренбург»"],
            ["24 очка после 11 туров",
             "лидер: 25 очков и победа над ЦСКА 3:1",
             "сыграли 2:2 в понедельник, 19 октября",
             "23 очка; в воскресенье — дерби с ЦСКА"],
            ["b", "a", "d", "c"],
            ["Dynamo b", "Zenit a", "Spartak d", "Rodina and Orenburg c"],
            instr="Match the teams to the facts")
e.head("D · ВРЕМЯ ГЛАГОЛА", 25)
e.note("Fill in the correct tense of the verb in brackets.")
e.ex("B1", "fill-in", "будет играть", "future tense: будет играть",
     "В воскресенье ЦСКА ___ со «Спартаком». (играть)", instr="Fill in", size=20, gap=8)
e.ex("B1", "fill-in", "победило", "победить → победило (past tense, neuter)",
     "«Динамо» ___ ЦСКА со счётом 3:1. (победить)", instr="Fill in", size=20, gap=8)
e.ex("B1", "fill-in", "закончился", "закончиться → закончился",
     "Матч «Родина» — «Оренбург» ___ со счётом 2:2. (закончиться)", instr="Fill in", size=20, gap=8)
e.ex("B1", "fill-in", "ждут", "ждать → ждут (3rd person plural)",
     "Болельщики ___ дерби всю неделю. (ждать)", instr="Fill in", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
