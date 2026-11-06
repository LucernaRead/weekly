# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-it-ru/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA · КУЛЬТУРА", "La Lucerna", "A2 → B1 · Torrone, cioccolato e tartufo · Торроне, шоколад и трюфель")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("Due feste dolci: il torrone a Cremona, il cioccolato a Perugia", 37)
f.byline("Dalla redazione de La Lucerna · Livello di lettura: A2 → B1")
f.para("Il secondo weekend della Festa del Torrone è a Cremona, sabato 14 e domenica 15 novembre: laboratori per i più piccoli, degustazioni e una maxi racchetta da tennis fatta di torrone, per il tennis in carrozzina. Domenica 15 novembre arriva anche il Treno Storico Arlecchino, da Milano a Cremona, e lo spettacolo delle Terre di mezzo in piazza del Comune.")
f.para("Lo stesso weekend, venerdì 13 novembre, apre a Perugia Eurochocolate, la 32ª edizione, fino al 22 novembre: il titolo è «Fate dolci», un invito a vivere il cioccolato in modo attivo e creativo, con laboratori, spettacoli e il grande Chocolate Show. La Regione ospite di quest'anno è la Calabria.")
f.para("E il tartufo bianco non va in vacanza: ad Alba, in Piemonte, la Fiera del Tartufo Bianco continua fino al 6 dicembre, con il Mercato Mondiale ogni sabato e domenica. Il re dell'autunno resta in tavola anche con il sole di San Martino.")
f.para("Per chi ama la storia, il torrone di Cremona racconta un matrimonio: la rievocazione è quella di Bianca Maria Visconti e Francesco Sforza, con il corteo storico che torna domenica 22 novembre, l'ultimo giorno della festa. Il tema del 2026 è «Il Confine», la soglia tra tradizione e innovazione.")
f.gloss("il torrone торроне · il cioccolato шоколад · il laboratorio мастерская · la degustazione дегустация · la rievocazione историческая реконструкция.")
f.head("IL TARTUFO RESTA IN TAVOLA", 25)
f.para("La Fiera di Alba è aperta dal 10 ottobre: quasi due mesi di profumi e piatti speciali. Con il sole di San Martino, il tartufo bianco diventa ancora più prezioso — e i ristoranti lo servono con pasta, uova e risotti.", 23.5)
f.end_report()

# col 3: truffle image + facts + e tu? (sequential)
ix = COLX[3]
image(p, "tartufo.jpg", ix, 200, CW, 265)
cy3 = caption(p, ix, 465, CW, "Un tartufo bianco, il fungo più prezioso d'Italia. Ad Alba la fiera dura fino al 6 dicembre; con il sole di San Martino, il tartufo è ancora più prezioso.",
              "Foto: Wikimedia Commons — dominio pubblico")
facts = ["Cremona, 14–15 novembre: secondo weekend del Torrone, laboratori e treno storico.",
         "Perugia, 13–22 novembre: Eurochocolate, 32ª edizione, «Fate dolci».",
         "Alba: la Fiera del Tartufo Bianco continua fino al 6 dicembre."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "IL WEEKEND DOLCE", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E tu? Preferisci il torrone o il cioccolato? Scrivi due frasi in italiano e mandale alla redazione."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Что тебе больше нравится: торроне или шоколад? Напиши два предложения и пришли.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E TU? · А ты?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Что тебе больше нравится: торроне или шоколад? Напиши два предложения и пришли.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ESERCIZI · УПРАЖНЕНИЯ СТРАНИЦЫ 3", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Ответы на стр. 8 · Уровни смешаны — ищите по номеру", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · COMPRENSIONE", 25)
e.bridge("Прочитайте статью на странице 3 и выберите правильный ответ.")
e.ex("A2", "Один ответ", "B", "Фестиваль торроне, второй уикенд: 14–15 ноября",
     "Il secondo weekend del Torrone è... A. il 7–8 novembre · B. il 14–15 novembre · C. il 21–22 novembre", size=20, gap=8)
e.ex("A2", "Один ответ", "C", "Шоколадный фестиваль — до 22 ноября",
     "Eurochocolate dura fino al... A. 6 dicembre · B. 15 novembre · C. 22 novembre", size=20, gap=8)
e.ex("A2", "Один ответ", "B", "Шоколадный фестиваль: 32-й выпуск",
     "Eurochocolate è alla sua... A. 29ª edizione · B. 32ª edizione · C. 67ª edizione", size=20, gap=8)
e.ex("B1", "Один ответ", "A", "Тема Eurochocolate: «Fate dolci»",
     "Il titolo di Eurochocolate 2026 è... A. «Fate dolci» · B. «Il Confine» · C. «Legacy»", size=20, gap=8)
e.ex("B1", "Один ответ", "B", "Фестиваль трюфелей в Альбе идёт до 6 декабря",
     "La Fiera del Tartufo Bianco di Alba chiude... A. il 22 novembre · B. il 6 dicembre · C. l'8 novembre", size=20, gap=8)
e.head("B · LE PAROLE DEL TESTO", 25)
e.bridge("Дополните слова из рамки.")
e.para("torrone · cioccolato · laboratorio · degustazione · tartufo · mandorle", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "Дополнить предложения", "torrone", "torrone = нуга",
     "A Cremona si festeggia il ___.", instr="Вставить", size=20, gap=8)
e.ex("A2", "Дополнить предложения", "cioccolato", "cioccolato = шоколад",
     "A Perugia si festeggia il ___.", instr="Вставить", size=20, gap=8)
e.ex("B1", "Дополнить предложения", "laboratorio", "laboratorio = мастерская (здесь)",
     "Per i più piccoli c'è il ___ della dolcezza.", instr="Вставить", size=20, gap=8)
e.ex("A2", "Дополнить предложения", "degustazione", "degustazione = дегустация",
     "Alla festa c'è una ___ con i dolci.", instr="Вставить", size=20, gap=8)
e.ex("B1", "Дополнить предложения", "mandorle", "mandorle = миндаль",
     "Il torrone è fatto di ___ e miele.", instr="Вставить", size=20, gap=8)
e.ex("A2", "Дополнить предложения", "tartufo", "tartufo = трюфель",
     "Il ___ bianco è il fungo più prezioso d'Italia.", instr="Вставить", size=20, gap=8)
e.head("C · IL PASSATO PROSSIMO", 25)
e.bridge("Дополните passato prossimo. Внимание: вспомогательный глагол avere или essere.")
e.ex("B1", "Дополнить предложения", "è arrivato", "arrivare с essere: è arrivato",
     "Il Treno Storico ___ (arrivare) a Cremona domenica.", instr="Вставить", size=20, gap=8)
e.ex("B1", "Дополнить предложения", "abbiamo assaggiato", "assaggiare с avere: abbiamo assaggiato",
     "Noi ___ (assaggiare) il torrone a Cremona.", instr="Вставить", size=20, gap=8)
e.ex("B1", "Дополнить предложения", "sono andati", "andare с essere, мн. ч.: sono andati",
     "I visitatori ___ (andare) a Perugia per Eurochocolate.", instr="Вставить", size=20, gap=8)
e.ex("B1", "Дополнить предложения", "ha aperto", "aprire с avere: ha aperto",
     "Perugia ___ (aprire) Eurochocolate venerdì.", instr="Вставить", size=20, gap=8)
e.head("D · COSTRUISCI LE FRASI", 25)
e.bridge("Составьте из слов правильные предложения.")
e.ex("B1", "Составить предложения", "Eurochocolate è a Perugia dal 13 novembre.", "Подлежащее + essere + место + дата",
     "Eurochocolate / è a Perugia / dal 13 novembre → ___", instr="Составить предложения", size=20, gap=8)
e.ex("A2", "Составить предложения", "A Cremona il torrone è il re.", "Сначала место, потом подлежащее",
     "a Cremona / il torrone / è il re → ___", instr="Составить предложения", size=20, gap=8)
e.ex("B1", "Составить предложения", "La fiera dura fino al 6 dicembre.", "dura fino a = длится до",
     "la fiera / dura / fino al 6 dicembre → ___", instr="Составить предложения", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT · СПОРТ", "La Lucerna", "LIVELLO B1 · Le notti azzurre e il tennis · «Синие» ночи и теннис")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("Due notti azzurre: Francia a San Siro, Belgio a Bruxelles", 37)
f.byline("Dalla redazione sportiva de La Lucerna · Livello di lettura: B1")
f.para("È una settimana di grande calcio, senza Serie A: il campionato si ferma per la sosta delle nazionali. Giovedì 12 novembre, alle 20.45, l'Italia gioca a San Siro con la Francia, nella quinta giornata di Nations League. Domenica 15 novembre, alle 20.45, gli Azzurri chiudono il girone a Bruxelles, con il Belgio.")
f.para("Nel girone 1 di Lega A, la Francia è prima con 10 punti, l'Italia è seconda con 7, il Belgio è terzo con 6 e la Turchia è a zero. Le prime due vanno ai quarti di finale, a marzo 2027. Per l'Italia, le due partite di questa settimana sono decisive: attenzione, qui sono presentazioni, senza risultati.")
f.para("Giovedì e domenica il calcio scende in campo anche per la ricerca: con «Un gol per la ricerca», le partite ricordano i Giorni della Ricerca AIRC, che durano fino al 15 novembre e raccontano il lavoro di più di 770 progetti di ricerca.")
f.para("Domenica 15 novembre comincia anche un'altra storia: a Torino, all'Inalpi Arena, iniziano le Nitto ATP Finals, con gli otto migliori giocatori e le otto migliori coppie di doppio. Giovedì 12 novembre, all'Inalpi Arena, c'è il Grand Opening Show con Achille Lauro.")
f.para("E per chi segue la Serie A: l'undicesima giornata, giocata dal 6 all'8 novembre, è appena finita — i risultati e la classifica li leggiamo nel prossimo numero. La dodicesima giornata si gioca dal 21 al 23 novembre: Como–Cagliari e Lazio–Lecce sabato, Juventus–Venezia, Bologna–Udinese, Sassuolo–Genoa e Milan–Frosinone domenica, Atalanta–Inter la sera, Monza–Fiorentina lunedì.")
f.gloss("la sosta перерыв в чемпионате · il girone группа · decisivo решающий · la presentazione превью.")
f.end_report()

# col 3: data box + e tu? (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 436, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 240, "LE PARTITE DA SEGNARE", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "Giovedì 12 novembre, ore 20.45 · Italia – Francia, a San Siro, Nations League. Domenica 15 novembre, ore 20.45 · Belgio – Italia, a Bruxelles. Domenica 15 novembre · ATP Finals a Torino: iniziano le gare all'Inalpi Arena.", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 662
etvous = "E tu? Quale partita guardi giovedì sera? Scrivi due frasi in italiano."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Какой матч ты посмотришь в четверг вечером? Напиши два предложения по-итальянски.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "E TU? · А ты?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Какой матч ты посмотришь в четверг вечером? Напиши два предложения по-итальянски.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "LA SETTIMANA DELLO SPORT · Спортивная неделя", 26, "sans", True, OLIVE)
rows = [
    ("Gio 12.11", "Nations League", "Italia – Francia — ore 20.45, a San Siro, a Milano"),
    ("Ven 13.11", "Tennis · Torino", "Blue Carpet: i campioni sfilano in piazza San Carlo"),
    ("Dom 15.11", "Nations League", "Belgio – Italia — ore 20.45, a Bruxelles"),
    ("Dom 15.11", "Tennis · Torino", "ATP Finals: iniziano le gare all'Inalpi Arena"),
    ("Dom 22.11", "Serie A · 12ª giornata", "Atalanta – Inter — la sera, a Bergamo"),
]
yy = ty + 16
for i, (d, t, m) in enumerate(rows):
    p.rect(MX, yy, RIGHT - MX, 44, fill="#f4efe0" if i % 2 == 0 else "#efe8d2")
    p.text(MX + 18, yy + 29, d, 20.5, "sans", True, BRICK)
    p.text(MX + 185, yy + 29, t, 20, "sans", False, GREY)
    p.text(MX + 470, yy + 29, m, 21, "serif", False, INK)
    yy += 44
tnote = "Attenzione: le partite dell'Italia di giovedì e domenica e le gare di tennis si giocano dopo la chiusura di questa edizione — per questo qui sono presentazioni, senza risultati. I risultati della Serie A, invece, sono nel prossimo numero."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ESERCIZI · УПРАЖНЕНИЯ СТРАНИЦЫ 4", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Ответы на стр. 8 · Уровни смешаны — ищите по номеру", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A · COMPRENSIONE", 25)
e.bridge("Прочитайте статью на странице 4 и выберите правильный ответ.")
e.ex("B1", "Один ответ", "B", "Италия–Франция в четверг, 12 ноября",
     "Italia–Francia si gioca... A. domenica 15 novembre · B. giovedì 12 novembre · C. lunedì 9 novembre", size=20, gap=8)
e.ex("B1", "Один ответ", "B", "Воскресенье: Италия в Брюсселе против Бельгии",
     "Domenica, l'Italia gioca... A. a San Siro · B. a Bruxelles · C. a Torino", size=20, gap=8)
e.ex("B1", "Один ответ", "A", "Франция лидирует в группе с 10 очками",
     "Nel girone, la Francia ha... A. 10 punti · B. 7 punti · C. 6 punti", size=20, gap=8)
e.ex("B1", "Один ответ", "C", "Матчи сборной — только превью, без результатов",
     "Le partite dell'Italia, in questo giornale, sono... A. risultati finali · B. cancellate · C. presentazioni senza risultati", size=20, gap=8)
e.ex("B1", "Один ответ", "B", "Итоговый турнир ATP в Турине",
     "Le ATP Finals si giocano... A. a Milano · B. a Torino · C. a Bruxelles", size=20, gap=8)
e.head("B · LE PAROLE", 25)
e.match_set("B1", "Слова и значения",
            ["la sosta", "il girone", "decisivo", "la presentazione"],
            ["il racconto prima della partita, senza risultati",
             "che decide tutto, molto importante",
             "il gruppo di squadre che giocano tra loro",
             "la pausa del campionato, senza partite"],
            ["d", "c", "b", "a"],
            ["sosta=перерыв d", "girone=группа c", "decisivo=решающий b", "presentazione=превью a"],
            instr="Соединить")
e.head("C · I COMPARATIVI", 25)
e.bridge("Дополните сравнительной степенью слова в скобках (см. расписание).")
e.ex("B1", "Дополнить предложения", "più tardi", "Оба матча начинаются в 20.45: воскресный матч не позже матча четверга: più tardi",
     "Le partite di domenica sera NON cominciano ___ di quelle di giovedì. (tardi)", instr="Вставить", size=20, gap=8)
e.ex("B1", "Дополнить предложения", "più presto", "Оба матча начинаются в 20.45: матч четверга не раньше воскресного: più presto",
     "Le partite di giovedì NON cominciano ___ di quelle di domenica. (presto)", instr="Вставить", size=20, gap=8)
e.ex("B1", "Дополнить предложения", "più bella", "più + bella: вечер четверга — самый красивый (субъективно)",
     "Per i tifosi, la serata di giovedì è la serata ___ del weekend. (bella)", instr="Вставить", size=20, gap=8)
e.ex("B2", "Модели предложений", "meglio", "Сравнительная степень от bene — неправильная: meglio",
     "L'Italia gioca bene. → L'Italia gioca ___ (bene).", instr="Вставить", size=20, gap=8)
e.head("D · IL PASSATO DELLO SPORT", 25)
e.bridge("Дополните passato prossimo.")
e.ex("B1", "Дополнить предложения", "ha vinto", "vincere: ha vinto",
     "La mia squadra ___ (vincere) la partita di ieri.", instr="Вставить", size=20, gap=8)
e.ex("B1", "Дополнить предложения", "ha pareggiato", "pareggiare: ha pareggiato",
     "La mia squadra ___ (pareggiare) 1–1.", instr="Вставить", size=20, gap=8)
e.ex("B2", "Дополнить предложения", "sono arrivati", "arrivare с essere, мн. ч.: sono arrivati",
     "I tifosi ___ (arrivare) allo stadio alle cinque.", instr="Вставить", size=20, gap=8)
e.ex("B1", "Дополнить предложения", "abbiamo guardato", "guardare с avere: abbiamo guardato",
     "Noi ___ (guardare) la partita in televisione.", instr="Вставить", size=20, gap=8)
e.ex("B1", "Дополнить предложения", "ha preso", "Причастие от prendere — preso: ha preso",
     "Il portiere ___ (prendere) un gol al 90°.", instr="Вставить", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
