# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURE (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURE　Культура", "The Lucerna", "A2 → B1　Friday at the movies　В пятницу — в кино")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2560, tag="P3-main")
f.title("Friday Night at the Movies : A Cat and a Monster", 32)
f.byline("By The Lucerna newsroom　Reading level : A2 → B1")
f.para("On Friday, November 6, two very different films open in cinemas across America. One is for children and families. The other is for monster fans. Both give you a reason to go out on a dark autumn evening.")
f.para("The first is « The Cat in the Hat », from the famous children's book by Dr. Seuss. The Cat — tall, funny, and always in trouble — comes to life on the big screen, with Bill Hader as the voice of the Cat. If you know the book, you know the hat : red and white, and much too tall.")
f.para("The second is « Godzilla Minus Zero », the new film from Japanese director Takashi Yamazaki. Godzilla is the giant monster who has walked through Japanese films for more than seventy years. This time, the monster returns to the cinema — bigger, darker, and louder than ever.")
f.para("Which film would you choose ? A talking cat in a striped hat, or a giant monster in a city ? In our newsroom, the vote is split — half for the cat, half for the monster. Tell us your choice on page 7.")
f.box("AT HOME THIS WEEK　Дома", [
    ("Wed Nov 4 — « A Dog's Perfect Christmas » and « Taken : Natalee Holloway » arrive on Netflix.", "serif", False, INK, 21.5, 1.4),
    ("Thu Nov 5 — « Black Doves » Season 2 begins. Fri Nov 6 — « Under Siege » Season 1 and « Unprotected : Murder in Galicia ».", "serif", False, INK, 21.5, 1.4),
    ("Sun Nov 8 — « Love Is Blind : The Reunion » closes the week. One week, one screen, many stories.", "serif", False, INK, 21.5, 1.4),
])
f.para("A film is not only a story — it is also English practice. Listen for three things : the catchphrase (the line everybody repeats), the joke (why does the room laugh ?), and the ending (happy, sad, or open ?). After the film, try to tell the story in five English sentences.")
f.para("And if you stay at home, the same rule works for a series : one episode, five sentences, in English. The best five-sentence reviews will be printed in VOL.3 — send yours to the newsroom.")
f.gloss("to open (о фильме) выйти в прокат · a monster чудовище · a catchphrase крылатая фраза · a series сериал.")
f.head("A　COMPREHENSION", 25)
f.bridge("Прочитай статью стр. 3 и выбери ответ.")
f.ex("A2", "Выбрать ответ", "B", "фильм про Кота выходит в пятницу 6 ноября",
     "« The Cat in the Hat » opens on... A. November 3 · B. Friday, November 6 · C. November 8", size=22)
f.ex("A2", "Выбрать ответ", "A", "Кот — из книги доктора Сьюза",
     "The Cat comes from a book by... A. Dr. Seuss · B. Takashi Yamazaki · C. Bill Hader", size=22)
f.ex("A2", "Выбрать ответ", "C", "Кота озвучивает Билл Хейдер",
     "The voice of the Cat is... A. the director · B. Godzilla · C. Bill Hader", size=22)
f.ex("B1", "Выбрать ответ", "B", "режиссёр «Годзиллы» — Такаси Ямадзаки",
     "« Godzilla Minus Zero » is directed by... A. Dr. Seuss · B. Takashi Yamazaki · C. Bill Hader", size=22)
f.ex("B1", "Выбрать ответ", "A", "второй сезон «Чёрных голубей» выходит 5 ноября",
     "« Black Doves » Season 2 begins on... A. Thursday, November 5 · B. Friday, November 6 · C. Sunday, November 8", size=22)
f.ex("B1", "Выбрать ответ", "C", "воскресный выпуск-воссоединение завершает неделю",
     "The week closes with... A. a film · B. a monster · C. « Love Is Blind : The Reunion »", size=22)
f.head("B　SENTENCES", 25)
f.bridge("Дополни предложения данными словами.")
f.ex("A2", "Дополнить предложения", "opens", "open = выйти в прокат (3-е лицо ед. ч. + s)",
     "The film ___ on Friday, November 6.", instr="Заполни")
f.ex("A2", "Дополнить предложения", "taller", "tall → taller, сравнительная степень",
     "The hat is ___ than the Cat himself !", instr="Заполни")
f.ex("B1", "Дополнить предложения", "louder", "loud → louder",
     "Godzilla is bigger, darker, and ___ than ever this time.", instr="Заполни")
f.ex("B1", "Дополнить предложения", "split", "split = расколотый",
     "In our newsroom, the vote is ___ : half cat, half monster.", instr="Заполни")
f.head("C　THE WORDS", 25)
f.match_set("A2", "Подобрать пары",
            ["a monster", "a catchphrase", "a series", "to open"],
            ["a line everybody repeats",
             "a giant frightening creature",
             "a film's first day in cinemas",
             "a story told in many episodes"],
            ["b", "a", "d", "c"],
            ["monster=чудовище b", "catchphrase=крылатая фраза a", "series=сериал d", "open=выйти в прокат c"],
            instr="Подбери пары")
f.head("D　GOING TO", 25)
f.bridge("Перепиши с be going to.")
f.ex("A2", "Перестроить", "We are going to watch the cat film on Friday.", "we → are going to",
     "We (watch) the cat film on Friday. → ___", instr="Перепиши")
f.ex("A2", "Перестроить", "She is going to tell the story in five sentences.", "she → is going to",
     "She (tell) the story in five sentences. → ___", instr="Перепиши")
f.ex("B1", "Перестроить", "Are you going to choose the monster ?", "вопрос: be в начале",
     "You (choose) the monster ? → ___", instr="Перепиши")
f.ex("B1", "Перестроить", "They are going to send their reviews to the newsroom.", "they → are going to",
     "They (send) their reviews to the newsroom. → ___", instr="Перепиши")
f.end_report()

# col 3: image + side flow
ix = COLX[3]
image(p, "catmanet.jpg", ix, 200, CW, 470)
cy3 = caption(p, ix, 670, CW, "A cat in art : « Cat and Flowers », an illustration by Édouard Manet for « The Cats » by Champfleury. Not film art — but this week, every cat is a star.",
              "Édouard Manet — CC0, via Wikimedia Commons")
v3 = Flow(p, [(ix, CW)], int(cy3) + 18, 2560, tag="P3-col3")
v3.box("THE CAT'S HAT　Шляпа Кота", [
    ("Red and white stripes, much too tall — the most famous hat in children's books. In the film, the hat is back, and so is the trouble.", "serif", False, INK, 21.5, 1.42),
])
v3.head("FIVE SENTENCES", 25)
v3.para("After any film or episode, tell the story in five English sentences : who, where, what happened, the surprise, the ending. Five sentences are enough — and they are excellent practice.", 22)
v3.para("Example : « A cat comes to a house. Two children are bored. The cat plays games. The house is a mess. Then the cat cleans it all up. » Now it is your turn.", 22)
v3.bridge("Пять фраз рецензии: кто, где, что случилось, поворот, финал — пяти хватит.")
v3.end_report()
p.foot(3)
p.save(f"{OUT}/p3-culture.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT　Спорт", "The Lucerna", "LEVEL B1　NFL　F1　NASCAR　WTA　Boxing")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2560, tag="P4-main")
f.title("Sunday in Madrid, São Paulo and Miami", 32)
f.byline("By The Lucerna newsroom　Reading level : B1")
f.para("Sunday, November 8, is the biggest sports day of the autumn. Three countries, five sports, one Sunday — and American football in a Spanish football stadium.")
f.para("In Madrid, the NFL plays its international game at the Santiago Bernabéu : the Cincinnati Bengals against the Atlanta Falcons. American football in the home of Real Madrid — a strange and wonderful mix. The game is part of NFL Week 9, and it is the week's most talked-about fixture.")
f.para("Back in the United States, Week 9 continues the same day : the Miami Dolphins play the Detroit Lions at Hard Rock Stadium in Miami Gardens. Two games, two continents, one league — that is the modern NFL.")
f.para("In Brazil, Formula 1 races the São Paulo Grand Prix, the second race after the United States Grand Prix in Austin. Fast cars, a famous track, and a championship still to decide — the perfect Sunday afternoon for racing fans.")
f.para("And there is more : NASCAR races at Homestead-Miami, the WTA Finals begin at Indian Wells, and in Arlington, Texas, Alycia Baumgardner defends her women's lightweight title against Elif Nur Turhan. One Sunday is not enough — good thing the week has seven days.")
f.box("WHY MADRID ?　Почему Мадрид?", [
    ("The NFL plays games outside the United States every year, so new fans can see the sport live. Madrid joins London, Munich and São Paulo on the international map.", "serif", False, INK, 21.5, 1.4),
])
f.para("How do you follow five sports in one day ? Choose one game to watch fully, and follow the others on your phone. That is the modern fan : one screen for the game, one screen for the scores.")
f.para("On Saturday, November 7, the warm-up is already on : Major League Soccer plays its late-season fixtures, including Charlotte against Inter Miami and Atlanta against the New York Red Bulls. The weekend starts on Saturday — and it does not stop.")
f.gloss("a fixture матч по расписанию · a title чемпионский титул · to defend (о чемпионе) защищать титул · a fan болельщик.")
f.head("A　COMPREHENSION", 25)
f.bridge("Прочитай статью стр. 4 и выбери ответ.")
f.ex("B1", "Выбрать ответ", "A", "Мадрид: «Бенгалс» против «Фэлконс»",
     "In Madrid, the Bengals play... A. the Falcons · B. the Lions · C. Real Madrid", size=22)
f.ex("B1", "Выбрать ответ", "C", "стадион в Мадриде — «Бернабеу»",
     "The Madrid game is at... A. Hard Rock Stadium · B. Wembley · C. the Santiago Bernabéu", size=22)
f.ex("B1", "Выбрать ответ", "B", "«Долфинс» против «Лайонс» в Майами",
     "The Dolphins play the Lions in... A. Madrid · B. Miami · C. São Paulo", size=22)
f.ex("B1", "Выбрать ответ", "A", "Гран-при Сан-Паулу «Формулы-1» в Бразилии",
     "The São Paulo Grand Prix is in... A. Brazil · B. Spain · C. Texas", size=22)
f.ex("B1", "Выбрать ответ", "C", "Итоговый турнир WTA начинается в Индиан-Уэлсе",
     "The WTA Finals begin at... A. Miami · B. Madrid · C. Indian Wells", size=22)
f.ex("B1", "Выбрать ответ", "B", "бокс — в Арлингтоне",
     "The Baumgardner fight is in... A. Miami · B. Arlington, Texas · C. Madrid", size=22)
f.head("B　SENTENCES", 25)
f.bridge("Дополни предложения данными словами.")
f.ex("B1", "Дополнить предложения", "defends", "defend, 3-е лицо ед. ч. + s",
     "Baumgardner ___ her title on Sunday.", instr="Заполни")
f.ex("B1", "Дополнить предложения", "begin", "как в статье на стр. 4, глагол во мн. ч.",
     "The WTA Finals ___ on Sunday.", instr="Заполни")
f.ex("A2", "Дополнить предложения", "bigger", "big → bigger",
     "The Bernabéu is ___ than most NFL stadiums.", instr="Заполни")
f.ex("A2", "Дополнить предложения", "faster", "fast → faster",
     "Formula 1 cars are ___ than NASCAR cars on a road course.", instr="Заполни")
f.head("C　THE WORDS", 25)
f.match_set("B1", "Подобрать пары",
            ["a fixture", "a title", "a fan", "to defend"],
            ["a person who loves a team or sport",
             "a game in a season's schedule",
             "to keep a championship you already hold",
             "the honour of being champion"],
            ["b", "d", "a", "c"],
            ["fixture=матч по расписанию b", "title=чемпионский титул d", "fan=болельщик a", "defend=защищать титул c"],
            instr="Подбери пары")
f.head("D　PAST SIMPLE", 25)
f.bridge("Перепиши в простом прошедшем времени (матчи уже закончились).")
f.ex("B1", "Перестроить", "The Bengals played in Madrid on Sunday.", "play → played",
     "The Bengals (play) in Madrid on Sunday. → ___", instr="Перепиши")
f.ex("B1", "Перестроить", "She watched the race in São Paulo.", "watch → watched",
     "She (watch) the race in São Paulo. → ___", instr="Перепиши")
f.ex("B1", "Перестроить", "They followed the scores on their phones.", "follow → followed",
     "They (follow) the scores on their phones. → ___", instr="Перепиши")
f.ex("B1", "Перестроить", "He chose one game to watch fully.", "choose → chose",
     "He (choose) one game to watch fully. → ___", instr="Перепиши")
f.end_report()

# col 3: image + fixtures
ix = COLX[3]
image(p, "football1910.jpg", ix, 200, CW, 470)
cy4 = caption(p, ix, 670, CW, "American football in 1910 : Miami against Wittenberg. The helmets were leather, the fields were mud — but the game was already America's game.",
              "Frank R. Snyder — public domain, via Wikimedia Commons")
v4 = Flow(p, [(ix, CW)], int(cy4) + 18, 2560, tag="P4-col3")
v4.box("SUNDAY, NOVEMBER 8　Воскрес.", [
    ("NFL : Bengals–Falcons, Madrid (Bernabéu) ; Dolphins–Lions, Miami.", "serif", False, INK, 21.5, 1.42),
    ("F1 : São Paulo Grand Prix, Brazil. NASCAR : Homestead-Miami.", "serif", False, INK, 21.5, 1.42),
    ("WTA Finals begin, Indian Wells. Boxing : Baumgardner–Turhan, Arlington.", "serif", False, INK, 21.5, 1.42),
    ("SATURDAY, NOVEMBER 7 : MLS — Charlotte–Inter Miami ; Atlanta–New York Red Bulls.", "serif", False, INK, 21.5, 1.42),
])
v4.head("ONE SCREEN, TWO SCREENS", 25)
v4.para("The modern fan watches one game fully and follows the others on a phone. Try it in English : « The score is 14–10. » « Who scored ? » « Madrid is winning ! » — short sentences, live English.", 22)
v4.bridge("Язык матча: счёт, кто забил, кто ведёт — короткие фразы, как в прямом эфире.")
v4.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
