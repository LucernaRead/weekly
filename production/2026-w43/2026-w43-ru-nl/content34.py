# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-ru-nl/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · КУЛЬТУРА (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("КУЛЬТУРА · Cultuur", "Lucerna", "УРОВЕНЬ A2 → B1 · День лицеиста и сказки в кино · Lyceumdag en sprookjes in de bioscoop")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P3-feature")
f.title("День лицеиста: праздник школы и Пушкина", 37)
f.byline("От редакции Lucerna · Уровень чтения: A2 → B1")
f.para("В понедельник, 19 октября, в России — Всероссийский день лицеиста. В этот день в 1811 году — 215 лет назад — открылся Царскосельский лицей, знаменитая школа под Санкт-Петербургом.")
f.para("Александр Пушкин учился в лицее с первого дня: он был лицеистом первого набора. Пушкин очень любил лицей и своих друзей. В стихотворении «19 октября» он написал знаменитые слова: «Друзья мои, прекрасен наш союз!»")
f.para("Сегодня лицеи и гимназии по всей России отмечают этот день: в школах проходят торжественные линейки, вечера стихов и викторины. Ученики читают стихи Пушкина и говорят о дружбе.")
f.para("Почему именно 19 октября? Потому что лицей открылся в этот день. Для Пушкина лицейские годы были очень важны: там он начал писать стихи и нашёл друзей на всю жизнь. И через много лет, уже взрослый, он каждый год вспоминал этот день.")
f.gloss("лицеистом lyceumleerling · союз verbond · набора een lichting leerlingen.")
f.head("СКАЗОЧНЫЙ ЧЕТВЕРГ", 25)
f.para("А в четверг, 22 октября, — большой день для семей. В четверг в кино выходят сразу четыре сказки. Студии специально выбрали этот день: в субботу начинаются каникулы, и дети пойдут в кино с родителями.")
f.para("Первая сказка — «Морозко»: в роли ведьмы — Елизавета Боярская. Вторая — «Сказка о потерянном времени»: это ремейк знаменитого советского фильма. Третья — «Чудо-Юдо» с Сергеем Безруковым и Викторией Исаковой. Четвёртая — «Королевство кривых зеркал» режиссёра Клима Шипенко, по сказке Виталия Губарева.")
f.para("Все эти сказки пришли из книг и старых фильмов, которые любят в России. «Сказку о потерянном времени» написал Евгений Шварц, а «Морозко» — народная сказка: её знают все дети.")
f.gloss("ведьмы de heks · ремейк een remake · режиссёра de regisseur.")
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
p.text(MX, ey + 28, "УПРАЖНЕНИЯ · Oefeningen van pagina 3", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antwoorden op pagina 8 · niveaus door elkaar: zoek op nummer", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · ПОНИМАНИЕ", 25)
e.expl("Lees de teksten van pagina 3 en kies het juiste antwoord.")
e.ex("A2", "Meerkeuze", "B", "De Lyceumdag is 19 oktober",
     "День лицеиста отмечают... A. 18 октября · B. 19 октября · C. 25 октября", size=20, gap=8)
e.ex("A2", "Meerkeuze", "A", "Het lyceum opende in 1811",
     "Царскосельский лицей открылся в... A. 1811 году · B. 1911 году · C. 1800 году", size=20, gap=8)
e.ex("A2", "Meerkeuze", "B", "Poesjkin was leerling van de eerste lichting",
     "Пушкин был лицеистом... A. последнего набора · B. первого набора · C. второго набора", size=20, gap=8)
e.ex("A2", "Meerkeuze", "C", "Vier sprookjes op donderdag",
     "Сколько новых сказок выходит в четверг? A. две · B. три · C. четыре", size=20, gap=8)
e.ex("B1", "Meerkeuze", "A", "Omdat de vakantie op zaterdag begint",
     "Почему студии выбрали четверг? A. В субботу начинаются каникулы · B. В четверг билеты дешевле · C. В четверг нет школы", size=20, gap=8)
e.head("B · ГЛАГОЛЫ И ФОРМЫ", 25)
e.expl("Vul de juiste werkwoordsvorm of de juiste naamval in.")
e.ex("B1", "Voltooi de zin", "открылся", "открыться → открылся (verleden tijd, mannelijk)",
     "Лицей ___ в 1811 году. (открыться)", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "учился", "учиться → учился",
     "Пушкин ___ в лицее с первого дня. (учиться)", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "написал", "написать → написал",
     "В стихотворении «19 октября» Пушкин ___ знаменитые слова. (написать)", instr="Vul in", size=20, gap=8)
e.ex("A2", "Voltooi de zin", "читают", "читать → читают (meervoud)",
     "В школах ученики ___ стихи Пушкина. (читать)", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "режиссёра", "фильм + genitief: режиссёра",
     "«Королевство кривых зеркал» — фильм ___ Клима Шипенко. (режиссёр)", instr="Vul in", size=20, gap=8)
e.head("C · ЧЕТЫРЕ СКАЗКИ", 25)
e.match_set("B1", "Woorden koppelen",
            ["«Морозко»", "«Сказка о потерянном времени»", "«Чудо-Юдо»", "«Королевство кривых зеркал»"],
            ["сказка по книге Виталия Губарева, режиссёр Клим Шипенко",
             "в роли ведьмы — Елизавета Боярская",
             "фильм с Сергеем Безруковым и Викторией Исаковой",
             "ремейк знаменитого советского фильма"],
            ["b", "d", "c", "a"],
            ["«Морозко» b", "«Сказка о потерянном времени» d", "«Чудо-Юдо» c", "«Королевство кривых зеркал» a"],
            instr="Combineer")
e.head("D · СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 25)
e.expl("Vorm correcte zinnen met de woorden.")
e.ex("A2", "Zinnen bouwen", "Лицей открылся в 1811 году.", "onderwerp + werkwoord + tijd",
     "лицей / открылся / в 1811 году → ___", instr="Vorm de zin", size=20, gap=8)
e.ex("A2", "Zinnen bouwen", "Пушкин учился в лицее.", "onderwerp + werkwoord + plaats",
     "пушкин / учился / в лицее → ___", instr="Vorm de zin", size=20, gap=8)
e.ex("B1", "Zinnen bouwen", "В четверг выходят четыре сказки.", "tijd vooraan, werkwoord tweede",
     "в четверг / выходят / четыре сказки → ___", instr="Vorm de zin", size=20, gap=8)
e.ex("B1", "Zinnen bouwen", "Ученики читают стихи Пушкина.", "let op de genitief: стихи Пушкина",
     "ученики / читают / стихи пушкина → ___", instr="Vorm de zin", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-kultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · СПОРТ (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("СПОРТ · Sport", "Lucerna", "УРОВЕНЬ B1 · Главное дерби страны · De grote derby van het land")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1100, tag="P4-main")
f.title("Главное дерби страны: ЦСКА — «Спартак»", 37)
f.byline("От спортивной редакции Lucerna · Уровень чтения: B1")
f.para("Какая неделя для футбола! В пятницу, 23 октября, начинается 12-й тур чемпионата России: первый матч — «Ахмат» — «Оренбург», начало в 19:30. А главный матч тура будет в воскресенье.")
f.para("В воскресенье, 25 октября, в 16:00 по московскому времени ЦСКА играет со «Спартаком». Это главное московское дерби: два больших клуба из одного города. Мы пишем эти строки до игры, поэтому результата здесь нет: кто победил, вы узнаете в следующем номере.")
f.para("Перед дерби борьба в таблице очень плотная. Динамо — единоличный лидер: у него 25 очков. «Зенит» — второй: у него 24 очка. А «Спартак» — третий: у него 23 очка. Всё решит игра!")
f.para("В понедельник, 19 октября, закончился 11-й тур: последний матч «Родина» — «Оренбург» закончился со счётом 2:2. А «Динамо» в 11-м туре победило ЦСКА со счётом 3:1 — поэтому «Динамо» и вышло на первое место.")
f.para("Болельщики ждут дерби всю неделю: дома, на работе и в школе говорят только о футболе. ЦСКА и «Спартак» — старые соперники, и их матч — это не просто игра, а главное событие футбольной осени в Москве.")
f.gloss("дерби de derby (strijd tussen clubs uit dezelfde stad) · тур speelronde · таблица de ranglijst · счёт de score.")
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
p.text(MX, ty, "12-Й ТУР: ГЛАВНОЕ · Speelronde 12: het belangrijkste", 26, "sans", True, OLIVE)
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
p.text(MX, ey + 28, "УПРАЖНЕНИЯ · Oefeningen van pagina 4", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antwoorden op pagina 8 · niveaus door elkaar: zoek op nummer", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A · ПОНИМАНИЕ", 25)
e.expl("Lees de teksten van pagina 4 en kies het juiste antwoord.")
e.ex("B1", "Meerkeuze", "B", "De derby is op zondag",
     "Дерби ЦСКА — «Спартак» будет... A. в пятницу · B. в воскресенье · C. в понедельник", size=20, gap=8)
e.ex("B1", "Meerkeuze", "B", "De derby begint om 16:00",
     "Дерби начинается в... A. 19:30 · B. 16:00 · C. 12:00", size=20, gap=8)
e.ex("B1", "Meerkeuze", "C", "De koploper is «Динамо»",
     "Кто сейчас лидер чемпионата? A. «Зенит» · B. «Спартак» · C. «Динамо»", size=20, gap=8)
e.ex("B1", "Meerkeuze", "A", "«Спартак» heeft 23 punten",
     "Сколько очков у «Спартака»? A. 23 · B. 24 · C. 25", size=20, gap=8)
e.ex("B1", "Meerkeuze", "B", "«Родина» — «Оренбург» 2:2",
     "Матч «Родина» — «Оренбург» закончился... A. 3:1 · B. 2:2 · C. 1:0", size=20, gap=8)
e.head("B · ТАБЛИЦА И ДАТЫ", 25)
e.expl("Vul in met de getallen en woorden van pagina 4.")
e.ex("A2", "Voltooi de zin", "25", "«Динамо» heeft 25 punten",
     "У «Динамо» ___ очков.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "24", "«Зенит» heeft 24 punten",
     "У «Зенита» ___ очка.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "третий", "derde plaats: третий (mannelijk, nominatief)",
     "«Спартак» сейчас ___ в таблице: у него 23 очка.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Voltooi de zin", "пятницу", "в + accusatief voor de weekdag: в пятницу",
     "12-й тур начинается в ___ (день недели), 23 октября.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "восемь", "acht wedstrijden per ronde: восемь матчей",
     "В 12-м туре всего ___ матчей.", instr="Vul in", size=20, gap=8)
e.head("C · КОМАНДЫ И ФАКТЫ", 25)
e.match_set("B1", "Woorden koppelen",
            ["«Динамо»", "«Зенит»", "«Спартак»", "«Родина» и «Оренбург»"],
            ["24 очка после 11 туров",
             "лидер: 25 очков и победа над ЦСКА 3:1",
             "сыграли 2:2 в понедельник, 19 октября",
             "23 очка; в воскресенье — дерби с ЦСКА"],
            ["b", "a", "d", "c"],
            ["«Динамо» b", "«Зенит» a", "«Спартак» d", "«Родина» en «Оренбург» c"],
            instr="Combineer")
e.head("D · ВРЕМЯ ГЛАГОЛА", 25)
e.expl("Vul de juiste tijdsvorm van het werkwoord tussen haakjes in.")
e.ex("B1", "Voltooi de zin", "будет играть", "toekomstige tijd: будет играть",
     "В воскресенье ЦСКА ___ со «Спартаком». (играть)", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "победило", "победить → победило (verleden tijd, onzijdig)",
     "«Динамо» ___ ЦСКА со счётом 3:1. (победить)", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "закончился", "закончиться → закончился",
     "Матч «Родина» — «Оренбург» ___ со счётом 2:2. (закончиться)", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "ждут", "ждать → ждут (3e persoon meervoud)",
     "Болельщики ___ дерби всю неделю. (ждать)", instr="Vul in", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
