# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-it-ru/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA　КУЛЬТУРА", "La Lucerna", "A2 → B1　Torrone, cioccolato e tartufo　Торроне, шоколад и трюфели")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("Due feste dolci chiudono in bellezza: torrone e cioccolato", 37)
f.byline("Dalla redazione de La Lucerna　Livello di lettura: A2 → B1")
f.para("Domenica 22 novembre chiude a Cremona la Festa del Torrone, la 29ª edizione, dal 7 al 22 novembre, con il tema «Il Confine»: sedici giorni, tre weekend, un solo dolce protagonista. Alle 11, al Palatorrone, il Torrone d'Oro va al produttore musicale Davide Simonetta, nato a Cremona.")
f.para("Il momento più atteso è il pomeriggio: alle 16 parte il corteo storico, con oltre centocinquanta figuranti in costumi rinascimentali, e alle 17, in piazza del Comune, arriva la rievocazione del matrimonio tra Bianca Maria Visconti e Francesco Sforza. Poi sbandieratori e giochi di fuoco, fino alle 18, quando al Palatorrone c'è il gran finale: «Il torrone va in brodo».")
f.para("La leggenda dice che il torrone nacque proprio per quelle nozze, il 25 ottobre 1441, con la forma del Torrazzo, la torre di Cremona: un dolce di albumi, zucchero, mandorle e miele.")
f.para("Lo stesso giorno, domenica 22 novembre, chiude a Perugia Eurochocolate, la 32ª edizione, dal 13 al 22 novembre, con il titolo «Fate dolci». La Regione ospite è la Calabria, con bergamotto, cedro, peperoncino e fichi; l'ospite del gran finale è il maestro Iginio Massari. E il tartufo bianco non va in vacanza: ad Alba, in Piemonte, la Fiera del Tartufo Bianco continua fino al 6 dicembre.")
f.gloss("il torrone, торроне (нуга) · il corteo, шествие · il figurante, участник массовки · la rievocazione, историческая реконструкция · lo sbandieratore, знаменосец.")
f.head("IL TORRAZZO E IL TORRONE", 25)
f.para("Il Torrazzo di Cremona è il campanile medievale in mattoni più alto d'Italia. La leggenda lo lega al torrone: un dolce nato da un matrimonio e diventato il simbolo della città. A Cremona, per sedici giorni, il torrone è dappertutto: nelle piazze, nei laboratori, nelle maxi costruzioni.", 23.5)
f.end_report()

# col 3: torrazzo image + facts + e tu? (sequential)
ix = COLX[3]
image(p, "torrazzo.jpg", ix, 200, CW, 300)
cy3 = caption(p, ix, 500, CW, "Il Torrazzo di Cremona: secondo la leggenda, il torrone ha la forma di questa torre — ed è nato per un matrimonio del 1441.",
              "Foto: Wikimedia Commons — CC0")
facts = ["Cremona, dom 22 novembre: corteo alle 16, rievocazione alle 17, gran finale alle 18.",
         "Perugia, dom 22 novembre: Eurochocolate chiude con Iginio Massari.",
         "Alba: la Fiera del Tartufo Bianco continua fino al 6 dicembre."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "IL WEEKEND DOLCE", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E tu? Preferisci il torrone o il cioccolato? Scrivi due frasi in italiano e mandale alla redazione."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Что вам больше нравится — торроне или шоколад? Напишите два предложения и пришлите нам.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill=BOX)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E TU?　А ТЫ?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Что вам больше нравится — торроне или шоколад? Напишите два предложения и пришлите нам.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ESERCIZI　УПРАЖНЕНИЯ СТР. 3", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Ответы на стр. 8　Уровни перемешаны — ищите по номеру", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A　COMPRENSIONE", 25)
e.bridge("Прочитайте статью на стр. 3 и выберите правильный ответ.")
e.ex("A2", "Выберите ответ", "B", "Торроне закрывается в воскресенье 22 ноября",
     "La Festa del Torrone chiude... A. il 15 novembre · B. il 22 novembre · C. il 6 dicembre", size=20, gap=8)
e.ex("A2", "Выберите ответ", "C", "Фестиваль шоколада проходит в 32-й раз",
     "Eurochocolate è alla sua... A. 29ª edizione · B. 67ª edizione · C. 32ª edizione", size=20, gap=8)
e.ex("A2", "Выберите ответ", "B", "Реконструкция — в 17:00 на Пьяцца дель Комуне",
     "La rievocazione del matrimonio è... A. alle 11 · B. alle 17 · C. alle 20", size=20, gap=8)
e.ex("B1", "Выберите ответ", "A", "Тема Eurochocolate в этом году — «Fate dolci»",
     "Il titolo di Eurochocolate 2026 è... A. «Fate dolci» · B. «Il Confine» · C. «Finestrini»", size=20, gap=8)
e.ex("B1", "Выберите ответ", "B", "Ярмарка трюфелей в Альбе — до 6 декабря",
     "La Fiera del Tartufo Bianco di Alba chiude... A. il 22 novembre · B. il 6 dicembre · C. l'8 novembre", size=20, gap=8)
e.head("B　LE PAROLE DEL TESTO", 25)
e.bridge("Вставьте слова из рамки.")
e.para("torrone · cioccolato · corteo · rievocazione · tartufo · mandorle", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "Дополните предложение", "torrone", "torrone = торроне (нуга)",
     "A Cremona si festeggia il ___.", instr="Вставьте", size=20, gap=8)
e.ex("A2", "Дополните предложение", "cioccolato", "cioccolato = шоколад",
     "A Perugia si festeggia il ___.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополните предложение", "corteo", "corteo = шествие",
     "Alle 16 parte il ___ storico in centro.", instr="Вставьте", size=20, gap=8)
e.ex("A2", "Дополните предложение", "mandorle", "mandorle = миндаль (мн. ч.)",
     "Il torrone è fatto di ___ e miele.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополните предложение", "rievocazione", "rievocazione = историческая реконструкция",
     "Alle 17 c'è la ___ del matrimonio del 1441.", instr="Вставьте", size=20, gap=8)
e.ex("A2", "Дополните предложение", "tartufo", "tartufo = трюфель",
     "Il ___ bianco è il fungo più prezioso d'Italia.", instr="Вставьте", size=20, gap=8)
e.head("C　IL PASSATO PROSSIMO", 25)
e.bridge("Дополните формы passato prossimo — следите за вспомогательными глаголами avere / essere.")
e.ex("B1", "Дополните предложение", "è arrivato", "arrivare с essere: è arrivato",
     "Il corteo ___ (arrivare) in piazza domenica.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополните предложение", "abbiamo assaggiato", "assaggiare с avere: abbiamo assaggiato",
     "Noi ___ (assaggiare) il torrone a Cremona.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополните предложение", "sono andati", "andare с essere, мн. ч. sono andati",
     "I visitatori ___ (andare) a Perugia per Eurochocolate.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополните предложение", "ha chiuso", "chiudere с avere: ha chiuso",
     "Perugia ___ (chiudere) Eurochocolate domenica.", instr="Вставьте", size=20, gap=8)
e.head("D　COSTRUISCI LE FRASI", 25)
e.bridge("Составьте из слов правильные предложения.")
e.ex("B1", "Составьте предложения", "Eurochocolate chiude a Perugia il 22 novembre.", "Подлежащее + глагол + место + дата",
     "Eurochocolate / chiude / a Perugia / il 22 novembre → ___", instr="Составьте предложения", size=20, gap=8)
e.ex("A2", "Составьте предложения", "A Cremona il torrone è il re.", "Сначала место",
     "a Cremona / il torrone / è il re → ___", instr="Составьте предложения", size=20, gap=8)
e.ex("B1", "Составьте предложения", "La fiera dura fino al 6 dicembre.", "dura fino a = длится до",
     "la fiera / dura / fino al 6 dicembre → ___", instr="Составьте предложения", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT　СПОРТ", "La Lucerna", "LIVELLO B1　La Serie A e il tennis　Серия А и теннис")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("Lazio prima, Inter e Roma inseguono: i conti dell'11ª giornata", 37)
f.byline("Dalla redazione sportiva de La Lucerna　Livello di lettura: B1")
f.para("La Lazio è ancora prima in Serie A: il pareggio 1–1 a Napoli vale 29 punti, e la squadra di Gattuso è ancora imbattuta dopo 11 giornate. L'Inter vince 2–0 con il Como e sale a 28 punti, a un punto dalla vetta; la Roma batte 3–0 il Sassuolo e arriva a 27, con il miglior attacco del torneo, 31 gol.")
f.para("Il Milan vince 2–1 a Genova e prende il quarto posto, con 24 punti, davanti al Como, fermo a 23. Fiorentina e Juventus chiudono 2–2 al Franchi: i viola restano a 9 punti. In coda, l'Udinese perde 2–1 a Venezia ed è ultima, con 5 punti.")
f.para("La Serie A riparte sabato 21 novembre con la 12ª giornata, che si chiude lunedì 23: sabato la Lazio capolista gioca in casa con il Lecce, domenica sera, alle 20.45, c'è il big match Atalanta–Inter, a Bergamo. Lunedì sera, alle 20.45, Monza–Fiorentina chiude la giornata.")
f.para("Domenica 22 novembre si gioca anche la finale delle Nitto ATP Finals a Torino: otto campioni, due gironi e poi le semifinali. Il numero uno è Alexander Zverev, con Carlos Alcaraz tra i favoriti; l'Italia ha Flavio Cobolli, al debutto. Jannik Sinner, vincitore del 2025, non gioca: è fuori per infortunio.")
f.para("E la Nazionale? Le due notti azzurre — giovedì 12 novembre con la Francia e domenica 15 novembre con il Belgio — si sono giocate prima di questa edizione: i risultati e la classifica finale del girone saranno nel prossimo numero.")
f.gloss("la vetta, первое место · imbattuto, непобеждённый · il big match, центральный матч · il girone, группа · il debutto, дебют.")
f.end_report()

# col 3: tennis image + classifica + e tu? (sequential)
bx = COLX[3]
image(p, "tennis.jpg", bx, 200, CW, 110)
cy3 = caption(p, bx, 310, CW, "Il tennis di cent'anni fa: oggi le Finals si giocano a Torino, all'Inalpi Arena.",
              "Foto: Wikimedia Commons — dominio pubblico")
cb = cy3 + 24
p.rect(bx, cb, CW, 470, fill=BOX)
p.text(bx + 22, cb + 40, "LA CLASSIFICA　DOPO 11 GIORNATE", 19.5, "sans", True, OLIVE)
classifica = [
    "1. Lazio — 29 punti",
    "2. Inter — 28 punti",
    "3. Roma — 27 punti",
    "4. Milan — 24 punti",
    "5. Como — 23 punti",
    "20. Udinese — 5 punti",
]
yy3 = cb + 78
for t in classifica:
    yy3 = p.para(bx + 22, yy3 + 21, t, 21, "serif", False, INK, CW - 44, 1.4) + 4
p.para(bx + 22, yy3 + 14, "La Lazio è ancora imbattuta; la Roma ha il miglior attacco, 31 gol.", 19, "sans", False, GREY, CW - 44, 1.35)
ey3 = cb + 470 + 26
etvous = "E tu? Quale partita guardi domenica sera? Scrivi due frasi in italiano."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Какой матч смотрите в воскресенье вечером? Пишите по-итальянски.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill=BOX)
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "E TU?　А ТЫ?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Какой матч смотрите в воскресенье вечером? Пишите по-итальянски.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- results table (full width, compact) ----
ty = 1140
p.text(MX, ty, "I RISULTATI DELL'11ª GIORNATA　ИТОГИ 11-ГО ТУРА (6–8 ноября)", 26, "sans", True, OLIVE)
rows = [
    ("VEN 6.11", "Venezia – Udinese 2–1", ""),
    ("SAB 7.11", "Cagliari – Frosinone 1–0", "Torino – Lecce 1–1"),
    ("SAB 7.11", "Parma – Bologna 1–2", "Roma – Sassuolo 3–0"),
    ("DOM 8.11", "Napoli – Lazio 1–1", "Genoa – Milan 1–2　Monza – Atalanta 0–1"),
    ("DOM 8.11", "Inter – Como 2–0", "Fiorentina – Juventus 2–2"),
]
yy = ty + 16
for i, (d, m1, m2) in enumerate(rows):
    p.rect(MX, yy, RIGHT - MX, 62, fill=BOX if i % 2 == 0 else PAPER)
    p.text(MX + 18, yy + 29, d, 20, "sans", True, OLIVE)
    p.text(MX + 185, yy + 40, m1, 21, "serif", True, INK)
    p.text(MX + 700, yy + 40, m2, 21, "serif", False, INK)
    yy += 62
p.para(MX, yy + 26, "La 12ª giornata si gioca dal 21 al 23 novembre: Atalanta – Inter, ore 20.45, domenica 22 novembre, a Bergamo. I risultati delle due notti azzurre di Nations League saranno nel prossimo numero.", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ESERCIZI　УПРАЖНЕНИЯ СТР. 4", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Ответы на стр. 8　Уровни перемешаны — ищите по номеру", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A　COMPRENSIONE", 25)
e.bridge("Прочитайте статью на стр. 4 и выберите правильный ответ.")
e.ex("B1", "Выберите ответ", "B", "«Лацио» лидирует с 29 очками",
     "La prima in classifica ha... A. 28 punti · B. 29 punti · C. 27 punti", size=20, gap=8)
e.ex("B1", "Выберите ответ", "B", "«Интер» обыграл «Комо» 2:0",
     "L'Inter vince 2–0 con... A. la Roma · B. il Como · C. il Milan", size=20, gap=8)
e.ex("B1", "Выберите ответ", "A", "У «Ромы» лучшая атака — 31 гол",
     "Il miglior attacco del torneo è... A. della Roma · B. della Lazio · C. del Milan", size=20, gap=8)
e.ex("B1", "Выберите ответ", "C", "«Удинезе» последний с 5 очками",
     "L'ultima in classifica è... A. il Monza · B. il Venezia · C. l'Udinese", size=20, gap=8)
e.ex("B1", "Выберите ответ", "B", "Центральный матч — в Бергамо в воскресенье вечером",
     "Atalanta–Inter si gioca... A. sabato · B. domenica sera · C. lunedì", size=20, gap=8)
e.head("B　LE PAROLE", 25)
e.match_set("B1", "Подберите слова",
            ["la vetta", "imbattuto", "il girone", "il debutto"],
            ["la prima volta in un torneo importante",
             "che non ha mai perso",
             "il gruppo di squadre in un torneo",
             "il primo posto in classifica, la cima"],
            ["d", "b", "c", "a"],
            ["vetta = первое место, d", "imbattuto = непобеждённый, b", "girone = группа, c", "debutto = дебют, a"],
            instr="Соедините слова")
e.head("C　I COMPARATIVI", 25)
e.bridge("Вставьте сравнительную степень (см. таблицу).")
e.ex("B1", "Дополните предложение", "più", "У «Лацио» больше очков, чем у «Интера»: più",
     "La Lazio ha ___ punti dell'Inter. (molti)", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополните предложение", "meno", "У «Удинезе» меньше очков, чем у «Лацио»: meno",
     "L'Udinese ha ___ punti della Lazio. (pochi)", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополните предложение", "più bella", "воскресный вечер — самый лучший (оценка)",
     "Per i tifosi, la serata di domenica è la serata ___ del weekend. (bella)", instr="Вставьте", size=20, gap=8)
e.ex("B2", "Преобразуйте предложения", "meglio", "Сравнительная степень bene: meglio",
     "La Lazio gioca bene. → La Lazio gioca ___ (bene).", instr="Вставьте", size=20, gap=8)
e.head("D　IL PASSATO DELLO SPORT", 25)
e.bridge("Дополните формы passato prossimo.")
e.ex("B1", "Дополните предложение", "ha vinto", "vincere:ha vinto",
     "L'Inter ___ (vincere) 2–0 con il Como.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополните предложение", "ha pareggiato", "pareggiare:ha pareggiato",
     "La Lazio ___ (pareggiare) 1–1 a Napoli.", instr="Вставьте", size=20, gap=8)
e.ex("B2", "Дополните предложение", "sono arrivati", "arrivare с essere, мн. ч. sono arrivati",
     "I tifosi ___ (arrivare) allo stadio alle cinque.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополните предложение", "abbiamo guardato", "guardare с avere: abbiamo guardato",
     "Noi ___ (guardare) la partita in televisione.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополните предложение", "ha preso", "Причастие prendere — preso: ha preso",
     "Il portiere ___ (prendere) un gol al 90°.", instr="Вставьте", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
