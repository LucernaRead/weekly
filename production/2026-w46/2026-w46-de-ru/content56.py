# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-de-ru/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · YOUTH (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JUGEND · Молодёжь", "Die Lucerna", "LEVEL B1 · Laternen, Lieder & Schule · Фонарики, песни и школа")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P5-main")
f.title("Laternen basteln, Lieder singen: Die Woche der Kinder", 37)
f.byline("Von der Lucerna-Redaktion · Leseniveau: B1")
f.para("Am Montag, dem 9. November, sind alle wieder in der Schule: Auch in Bayern sind die Herbstferien jetzt vorbei. Die Rucksäcke sind gepackt, die Pausenhöfe sind wieder laut. Und in vielen Klassen wird schon gebastelt: Laternen für St. Martin.")
f.para("Was basteln die Kinder? Bunte Laternen aus Papier, mit Sternen, Monden und Tieren. In der Kita und in der Schule singen sie Martinslieder und üben den Umzug. Am Mittwochabend ziehen sie dann mit ihren Laternen durch die Straßen — vorneweg der heilige Martin auf dem Pferd.")
f.para("Und in Köln? Dort beginnt am Mittwoch um 11.11 Uhr die Karnevalssession. Auch Kinder verkleiden sich: als Prinzessin, als Pirat, als Tier. Aber Vorsicht: Am Vormittag ist Karneval, am Abend ist St. Martin — zwei Feste, zwei Stimmungen, ein Tag.")
f.para("Was macht man nach der Schule im dunklen November? Lesen, was man im Herbst begonnen hat, oder ein neues Hobby probieren. Unser Tipp: Suchen Sie sich ein Buch für die dunklen Abende — die Bibliotheken haben im November oft neue Bücher und Lesungen. Und wer Sport mag: Am Sonntag läuft die NFL im Fernsehen.")
f.para("Auch der Fußball gehört zur Woche: Am Freitag spielt die Nationalmannschaft in Belgrad — viele Jugendliche schauen das Spiel im Fernsehen. Wer in München wohnt, sieht am Sonntag vielleicht sogar die NFL-Stars in der Stadt. Mehr dazu auf Seite 4.")
f.gloss("basteln = мастерить · der Pausenhof = школьный двор · sich verkleiden = наряжаться · die Stimmung = настроение · der Pirat = пират.")
f.end_report()

# col 3: facts + vocab + Und Sie (hand-rolled; CORRECTED height formula — see W45 KIT §geometry)
ix = COLX[3]
facts = ["Am 9. November sind alle Bundesländer wieder in der Schule.",
         "In vielen Klassen werden Laternen für St. Martin gebastelt.",
         "Am 11. November: Karneval am Vormittag, Laternen am Abend."]
sy3 = 200
sh = 45 + 33 * len(facts) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in facts)
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "SCHULWOCHE · Снова в школу", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P5 col3 facts ends", sy3 + sh)
words = ["die Laterne — фонарик", "basteln — мастерить", "das Lied — песня",
         "das Kostüm — костюм", "der Umzug — шествие", "der Stern — звезда"]
sy3 = sy3 + sh + 26
sh = 45 + 33 * len(words) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in words)
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "MARTINSWÖRTER · Св. Мартин", 24, "sans", True, OLIVE)
yy3 += 52
for t in words:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P5 col3 vocab ends", sy3 + sh)
ey3 = sy3 + sh + 26
etvous = "Und Sie? Haben Sie als Kind eine Laterne gebastelt? Welches Lied singen Sie im November? Schreiben Sie zwei Sätze auf Deutsch!"
eh = 140 + 30.53 * len(wrap(etvous, "serif", False, 21.5, CW - 44)) + 29 * (len(wrap("Вы делали фонарик в детстве? Какую песню вы поёте в ноябре? Напишите два предложения!", "sans", False, 20, CW - 44)) - 1)
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "UND SIE? · А вы?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Вы делали фонарик в детстве? Какую песню вы поёте в ноябре? Напишите два предложения!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- Wochenplan wide box (cols 0-2) ----
sx, swd = span_x(0, 3)
p.rect(sx, 1120, swd, 300, fill=BOX, stroke=LINE, sw=1.4)
p.text(sx + 24, 1162, "DER WOCHENPLAN DER REDAKTION · Неделя редакции", 24, "sans", True, OLIVE)
planrows = [
    ("Mo 9.11.", "Schule für alle: Auch Bayern ist wieder da."),
    ("Di 10.11.", "Laternen basteln: Die Kitas bereiten den Umzug vor."),
    ("Mi 11.11.", "Karneval um 11.11 Uhr, Laternen am Abend."),
    ("Do 12.11.", "Nach dem Fest: In der Schule wird erzählt und geschrieben."),
    ("Fr 13.11.", "Nations League: Serbien – Deutschland (20.45 Uhr, RTL)."),
]
pyy = 1184
for t, txt in planrows:
    p.text(sx + 24, pyy + 24, t, 21, "sans", True, BRICK)
    p.text(sx + 190, pyy + 24, txt, 21.5, "serif", False, INK)
    pyy += 45

# ---- P5 exercises ----
ey = 1500
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ÜBUNGEN · Упражнения стр. 5", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Ответы на стр. 8 · Уровни смешаны — ищите каждый ответ по его номеру", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · LESEVERSTEHEN", 25)
e.bridge("Прочитайте статью на стр. 5 и выберите правильный ответ.")
e.ex("B1", "Выбор ответа", "A", "школа возобновляется везде 9 ноября",
     "Wann sind alle wieder in der Schule? A. am 9. November · B. am 11. November · C. am 15. November", size=20, gap=8)
e.ex("B1", "Выбор ответа", "B", "дети делают бумажные фонарики",
     "Was basteln die Kinder? A. ein Kostüm · B. Laternen aus Papier · C. einen Kürbis", size=20, gap=8)
e.ex("B1", "Выбор ответа", "B", "карнавал утром, святой Мартин днём",
     "Was ist am 11. November richtig? A. Nur Karneval. · B. Karneval am Vormittag, St. Martin am Abend. · C. Nur St. Martin.", size=20, gap=8)
e.ex("B1", "Выбор ответа", "B", "NFL по телевизору в воскресенье",
     "Was läuft am Sonntag im Fernsehen? A. die Bundesliga · B. die NFL · C. ein Film", size=20, gap=8)
e.ex("A2", "Выбор ответа", "A", "смотреть сборную в пятницу",
     "Was schauen viele Jugendliche am Freitag? A. die Nationalmannschaft in Belgrad · B. die NFL · C. den Karneval", size=20, gap=8)
e.head("B · WÖRTER AUS DEM TEXT", 25)
e.bridge("Дополните словами из рамки.")
e.para("Laterne · basteln · Lied · Kostüm · Umzug · Stern", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "Дополните предложение", "Laterne", "бумажный фонарик",
     "Die Kinder tragen eine bunte ___ durch die Straßen.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополните предложение", "basteln", "делать фонарики",
     "In der Schule ___ die Kinder Laternen.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополните предложение", "Lied", "петь песни о святом Мартине",
     "Die Kinder singen ein Martins___.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополните предложение", "Kostüm", "карнавальный костюм",
     "In Köln tragen die Kinder ein buntes ___.", instr="Вставьте", size=20, gap=8)
e.ex("A2", "Дополните предложение", "Umzug", "шествие с фонариками",
     "Am Abend zieht der ___ durch die Straßen.", instr="Вставьте", size=20, gap=8)
e.ex("A2", "Дополните предложение", "Stern", "звезда на фонарике",
     "Auf der Laterne ist ein ___.", instr="Вставьте", size=20, gap=8)
e.head("C · SÄTZE MIT «WEIL»", 25)
e.bridge("Соедините два предложения с помощью weil (глагол — в конец).")
e.ex("B1", "Преобразуйте предложение", "Die Kinder freuen sich, weil St. Martin kommt.", "в придаточном с weil глагол — в конце",
     "Die Kinder freuen sich. St. Martin kommt. (weil) → ___", instr="Перепишите", size=20, gap=8)
e.ex("B1", "Преобразуйте предложение", "Er bleibt zu Hause, weil es dunkel ist.", "ist — в конец",
     "Er bleibt zu Hause. Es ist dunkel. (weil) → ___", instr="Перепишите", size=20, gap=8)
e.ex("B1", "Преобразуйте предложение", "Sie geht in die Bibliothek, weil sie ein Buch lesen will.", "will — в конец",
     "Sie geht in die Bibliothek. Sie will ein Buch lesen. (weil) → ___", instr="Перепишите", size=20, gap=8)
e.ex("B1", "Преобразуйте предложение", "Köln feiert, weil die Karnevalssession beginnt.", "beginnt — в конец",
     "Köln feiert. Die Karnevalssession beginnt. (weil) → ___", instr="Перепишите", size=20, gap=8)
e.head("D · RICHTIG ODER FALSCH?", 25)
e.bridge("Верно или нет?")
e.ex("A2", "Верно или нет", "Richtig", "Бавария тоже возвращается 9 ноября",
     "Auch in Bayern sind die Herbstferien am 9. November vorbei. Richtig oder falsch?", instr="Верно или нет", size=20, gap=8)
e.ex("B1", "Верно или нет", "Falsch", "шествие с фонариками — вечером",
     "Der Laternenumzug findet am Vormittag statt. Richtig oder falsch?", instr="Верно или нет", size=20, gap=8)
e.ex("A2", "Верно или нет", "Richtig", "дети поют песни о святом Мартине",
     "Die Kinder singen Martinslieder. Richtig oder falsch?", instr="Верно или нет", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jugend.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · DEEP READ (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("VERTIEFUNG · Углубление", "Die Lucerna", "LEVEL B2 · Volkstrauertag & Stromsteuer · День памяти и налог на электричество")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P6-main")
f.title("Stille am Sonntag: Was bedeutet der Volkstrauertag?", 37)
f.byline("Von der Lucerna-Redaktion · Leseniveau: B2")
f.para("Am Sonntag, dem 15. November, ist Volkstrauertag: ein staatlicher Gedenktag. Die Menschen gedenken der Opfer von Gewalt und Krieg aller Nationen. In vielen Städten gibt es Gedenkstunden und Kranzniederlegungen. Der Tag liegt zwei Sonntage vor dem ersten Advent — und er ist ein stiller Tag.")
f.para("Die zentrale Gedenkstunde findet im Bundestag statt. Das ZDF überträgt ab 13.30 Uhr live. In diesem Jahr steht sie im Zeichen der deutsch-österreichischen Verbundenheit: Die Gedenkrede hält der österreichische Bundespräsident Alexander Van der Bellen. Bundespräsident Frank-Walter Steinmeier spricht das Totengedenken.")
f.para("Warum gibt es diesen Tag? Die erste Gedenkstunde fand 1922 im Reichstag statt. Seit 1952 wird der Volkstrauertag zwei Sonntage vor dem ersten Advent begangen. Gedenken heißt hier: innehalten, erinnern — und für Frieden und Versöhnung einstehen.")
f.para("Zweites Thema: die Stromsteuer. Kanzler Friedrich Merz will sie für alle auf das europäische Mindestmaß senken — versprochen war das schon im Koalitionsvertrag. Bisher gilt die Senkung nur für bestimmte Branchen. Haushalte zahlen weiter 2,05 Cent pro Kilowattstunde. Finanzminister Lars Klingbeil zeigt sich offen, zweifelt aber an der Finanzierung.")
f.para("Die Grünen hatten im April einen Entwurf zur Senkung für alle vorgelegt — der Bundestag lehnte ihn mit 310 zu 270 Stimmen ab. Der Haushalt 2027 soll am 27. November verabschiedet werden. Ob eine Einigung gelingt, ist offen.")
f.para("Zwei Themen, ein Muster: Gedenken und Energiepolitik betreffen fast jeden Haushalt. Am Sonntag ist es still im Land. Am Montag geht die Debatte weiter.", gap=0)
f.gloss("gedenken = поминать · Kranzniederlegung = возложение венков · stille Tag = тихий день · Verbundenheit = связь · Versöhnung = примирение.", gap=0)
f.end_report()

# col 3: numbers box + debate box (measured)
ix = COLX[3]
tl = [("15.11.", "Volkstrauertag — zwei Sonntage vor dem ersten Advent."),
      ("1922", "erste Gedenkstunde im Reichstag in Berlin."),
      ("13.30", "Uhr: Das ZDF überträgt die Gedenkstunde live."),
      ("2,05", "Cent pro Kilowattstunde: Stromsteuer für Haushalte."),
      ("0,05", "Cent: Stromsteuer für die Industrie seit 2026."),
      ("27.11.", "Verabschiedung des Bundeshaushalts 2027 geplant.")]
tlh = 45 + 30.5 * len(tl) + 29.11 * sum(len(wrap(t, "serif", False, 20.5, CW - 152)) for yr, t in tl)
p.rect(ix, 200, CW, tlh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(ix + 22, yy3 + 26, "DIE ZAHLEN · Цифры", 24, "sans", True, OLIVE)
yy3 += 52
for yr, t in tl:
    p.text(ix + 22, yy3 + 21, yr, 21, "sans", True, BRICK)
    yy3 = p.para(ix + 130, yy3 + 20.5, t, 20.5, "serif", False, INK, CW - 152, 1.42) + 10
print("P6 col3 numbers ends", 200 + tlh)
deb = "Volkstrauertag: Gedenken braucht Stille — darüber sind sich fast alle einig. Stromsteuer: Wie stark sie sinkt, ist noch offen. Beides betrifft fast jeden Haushalt."
hy3 = 200 + tlh + 26
hh = 140 + 29.82 * len(wrap(deb, "serif", False, 21, CW - 44)) + 27.69 * (len(wrap("День памяти: память требует тишины — почти все согласны. Налог на электричество: насколько он снизится, пока открыто. Оба касаются почти каждой семьи.", "sans", False, 19.5, CW - 44)) - 1)
p.rect(ix, hy3, CW, hh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = hy3 + 16
p.text(ix + 22, yy3 + 26, "DIE DEBATTE IN EINEM SATZ", 22.5, "sans", True, OLIVE)
yy3 += 50
yy3 = p.para(ix + 22, yy3 + 21, deb, 21, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "День памяти: память требует тишины — почти все согласны. Налог на электричество: насколько он снизится, пока открыто. Оба касаются почти каждой семьи.", 19.5, "sans", False, GREY, CW - 44, 1.42)
print("P6 col3 ends", hy3 + hh)

# ---- Two Sundays wide box (cols 0-2) ----
sx, swd = span_x(0, 3)
p.rect(sx, 1120, swd, 252, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(sx + 24, 1162, "ZWEI SONNTAGE IM NOVEMBER · Два воскресенья ноября", 24, "sans", True, OLIVE)
p.text(sx + 24, 1210, "VOLKSTRAUERTAG — 15. NOVEMBER", 21, "sans", True, BRICK)
p.text(sx + 24 + (swd - 48) // 2, 1210, "TOTENSONNTAG — 22. NOVEMBER", 21, "sans", True, BRICK)
pro = ["Gedenken an die Opfer von Gewalt und Krieg aller Nationen.",
       "Zentrale Gedenkstunde im Bundestag, Kranzniederlegungen im ganzen Land."]
contra = ["Evangelischer Gedenktag für die Verstorbenen.",
          "Eine Woche nach dem Volkstrauertag; dazwischen der Buß- und Bettag (18. November, Feiertag in Sachsen)."]
pyy = 1232
for t in pro:
    pyy2 = p.para(sx + 24, pyy + 20, "· " + t, 20.5, "serif", False, INK, (swd - 72) // 2, 1.4)
    pyy = max(pyy, pyy2) + 8
pyy = 1232
for t in contra:
    pyy2 = p.para(sx + 24 + (swd - 48) // 2, pyy + 20, "· " + t, 20.5, "serif", False, INK, (swd - 72) // 2, 1.4)
    pyy = max(pyy, pyy2) + 8

# ---- practice chart (full width) ----
cy = 1420
p.hline(MX, RIGHT, cy - 12, GOLD, 2)
p.text(MX, cy + 28, "WAS INTERESSIERT DIE LESER? · Что интересует читателей?", 26, "sans", True, OLIVE)
bars = [("Nations League und NFL", 46, "футбол"),
        ("St. Martin und Karneval", 34, "праздники"),
        ("Volkstrauertag und Gedenken", 20, "память")]
byy = cy + 58
for lab, v, zh in bars:
    p.text(MX, byy + 26, lab, 22, "serif", True, INK)
    p.text(MX + 360, byy + 26, zh, 20, "sans", False, GREY)
    p.rect(MX + 470, byy + 4, v * 17, 30, fill=OLIVE)
    p.text(MX + 470 + v * 17 + 16, byy + 26, f"{v} %", 22, "sans", True, BRICK)
    byy += 52
p.text(MX, byy + 22, "ÜBUNGSDATEN · Учебные данные — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage. (Учебные данные, не настоящий опрос.)", 19.5, "sans", False, GREY)

# ---- P6 exercises ----
ey = 1808
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ÜBUNGEN · Упражнения стр. 6", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Ответы на стр. 8 · Уровни смешаны — ищите каждый ответ по его номеру", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · DAS DIAGRAMM LESEN", 25, gap=9)
e.bridge("Используйте учебную диаграмму выше.")
e.ex("B1", "Выбор ответа", "A", "футбол лидирует — 46%",
     "Was interessiert die Leser am meisten (Übungsdaten)? A. Nations League und NFL · B. St. Martin · C. Volkstrauertag", size=20, gap=7)
e.ex("B1", "Выбор ответа", "B", "праздники вторые — 34%",
     "Was ist die zweitgrößte Gruppe? A. Volkstrauertag · B. St. Martin und Karneval · C. Nations League", size=20, gap=7)
e.ex("B1", "Выбор ответа", "B", "46+34=80",
     "Fußball und Feste zusammen sind... A. 66 % · B. 80 % · C. 100 %", size=20, gap=7)
e.ex("B2", "Выбор ответа", "B", "память — меньше всего, 20%",
     "Welche Gruppe ist kleiner? A. Feste · B. Gedenken · C. beide gleich", size=20, gap=7)
e.ex("B1", "Выбор ответа", "A", "память 20%",
     "Wie viele Prozent interessieren sich für den Volkstrauertag? A. 20 % · B. 34 % · C. 46 %", size=20, gap=7)
e.ex("B2", "Выбор ответа", "B", "46+34+20=100",
     "Die drei Zahlen zusammen ergeben... A. 90 % · B. 100 % · C. 110 %", size=20, gap=7)
e.head("B · LESEVERSTEHEN (B2)", 25, gap=9)
e.bridge("Прочитайте статью на стр. 6.")
e.ex("B2", "Выбор ответа", "B", "день памяти — 15 ноября",
     "Wann ist Volkstrauertag? A. am 11. November · B. am 15. November · C. am 22. November", size=20, gap=7)
e.ex("B2", "Выбор ответа", "A", "ZDF в прямом эфире с 13.30",
     "Wer überträgt die Gedenkstunde ab 13.30 Uhr? A. das ZDF · B. RTL · C. die ARD", size=20, gap=7)
e.ex("B2", "Выбор ответа", "B", "налог для домохозяйств — 2,05 цента",
     "Wie hoch ist die Stromsteuer für Haushalte? A. 0,05 Cent · B. 2,05 Cent · C. 3,05 Cent", size=20, gap=7)
e.ex("B1", "Выбор ответа", "B", "голосование по бюджету 2027 — 27 ноября",
     "Wann soll der Bundeshaushalt 2027 verabschiedet werden? A. am 15. November · B. am 27. November · C. am 18. November", size=20, gap=7)
e.head("C · GRAMMATIK", 25, gap=9)
e.bridge("Вставьте форму из скобок.")
e.ex("B2", "Дополните предложение", "wird", "пассив: wird + причастие прошедшего времени",
     "Die Gedenkstunde ___ (werden) live übertragen.", instr="Вставьте", size=20, gap=7)
e.ex("B2", "Дополните предложение", "ob", "ob вводит косвенный вопрос",
     "Niemand weiß, ___ die Einigung gelingt.", instr="Вставьте", size=20, gap=7)
e.ex("B1", "Дополните предложение", "geht", "gehen → geht",
     "Die Debatte ___ (gehen) weiter.", instr="Вставьте", size=20, gap=7)
e.ex("B2", "Дополните предложение", "spricht", "sprechen → spricht",
     "Steinmeier ___ (sprechen) das Totengedenken.", instr="Вставьте", size=20, gap=7)
e.head("D · WÖRTER DER DEBATTE", 25, gap=9)
e.bridge("Дополните словами из рамки.")
e.para("Kranzniederlegung · Versöhnung · Verbundenheit · gedenken", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "Дополните предложение", "Kranzniederlegung", "церемония возложения венков",
     "In vielen Städten gibt es eine ___.", instr="Вставьте", size=20, gap=7)
e.ex("B2", "Дополните предложение", "Versöhnung", "за мир и примирение",
     "Gedenken heißt: für Frieden und ___ einstehen.", instr="Вставьте", size=20, gap=7)
e.ex("B2", "Дополните предложение", "Verbundenheit", "немецко-австрийская связь",
     "Die Gedenkstunde steht im Zeichen der deutsch-österreichischen ___.", instr="Вставьте", size=20, gap=7)
e.ex("B1", "Дополните предложение", "gedenken", "память о жертвах",
     "Die Menschen ___ der Opfer von Gewalt und Krieg.", instr="Вставьте", size=20, gap=7)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-vertiefung.svg")
print("P6 saved, exercises so far:", len(REG))
