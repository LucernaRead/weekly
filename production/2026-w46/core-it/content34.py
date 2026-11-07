# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-it-core/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA · 文化", "La Lucerna", "A2 → B1 · Torrone, cioccolato e tartufo · 牛轧糖、巧克力与松露")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("Due feste dolci: il torrone a Cremona, il cioccolato a Perugia", 37)
f.byline("Dalla redazione de La Lucerna · Livello di lettura: A2 → B1")
f.para("Il secondo weekend della Festa del Torrone è a Cremona, sabato 14 e domenica 15 novembre: laboratori per i più piccoli, degustazioni e una maxi racchetta da tennis fatta di torrone, per il tennis in carrozzina. Domenica 15 novembre arriva anche il Treno Storico Arlecchino, da Milano a Cremona, e lo spettacolo delle Terre di mezzo in piazza del Comune.")
f.para("Lo stesso weekend, venerdì 13 novembre, apre a Perugia Eurochocolate, la 32ª edizione, fino al 22 novembre: il titolo è «Fate dolci», un invito a vivere il cioccolato in modo attivo e creativo, con laboratori, spettacoli e il grande Chocolate Show. La Regione ospite di quest'anno è la Calabria.")
f.para("E il tartufo bianco non va in vacanza: ad Alba, in Piemonte, la Fiera del Tartufo Bianco continua fino al 6 dicembre, con il Mercato Mondiale ogni sabato e domenica. Il re dell'autunno resta in tavola anche con il sole di San Martino.")
f.para("Per chi ama la storia, il torrone di Cremona racconta un matrimonio: la rievocazione è quella di Bianca Maria Visconti e Francesco Sforza, con il corteo storico che torna domenica 22 novembre, l'ultimo giorno della festa. Il tema del 2026 è «Il Confine», la soglia tra tradizione e innovazione.")
f.gloss("il torrone 牛轧糖 · il cioccolato 巧克力 · il laboratorio 实验室/工坊 · la degustazione 品尝会 · la rievocazione 历史重演。")
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
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("你更喜欢牛轧糖还是巧克力？写两句寄来。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E TU? · 说说你自己", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "你更喜欢牛轧糖还是巧克力？写两句寄来。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ESERCIZI · 第 3 版练习", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案见第 8 版 · 题目可跨级混排，按题号找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · COMPRENSIONE", 25)
e.bridge("读第 3 版文章，选出正确答案。")
e.ex("A2", "单选", "B", "牛轧糖节第二周末在 11 月 14–15 日",
     "Il secondo weekend del Torrone è... A. il 7–8 novembre · B. il 14–15 novembre · C. il 21–22 novembre", size=20, gap=8)
e.ex("A2", "单选", "C", "巧克力节到 11 月 22 日",
     "Eurochocolate dura fino al... A. 6 dicembre · B. 15 novembre · C. 22 novembre", size=20, gap=8)
e.ex("A2", "单选", "B", "巧克力节是第 32 届",
     "Eurochocolate è alla sua... A. 29ª edizione · B. 32ª edizione · C. 67ª edizione", size=20, gap=8)
e.ex("B1", "单选", "A", "本届巧克力节主题是“Fate dolci”",
     "Il titolo di Eurochocolate 2026 è... A. «Fate dolci» · B. «Il Confine» · C. «Legacy»", size=20, gap=8)
e.ex("B1", "单选", "B", "阿尔巴松露节到 12 月 6 日",
     "La Fiera del Tartufo Bianco di Alba chiude... A. il 22 novembre · B. il 6 dicembre · C. l'8 novembre", size=20, gap=8)
e.head("B · LE PAROLE DEL TESTO", 25)
e.bridge("用方框里的词填空。")
e.para("torrone · cioccolato · laboratorio · degustazione · tartufo · mandorle", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "完成句子", "torrone", "torrone = 牛轧糖",
     "A Cremona si festeggia il ___.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "cioccolato", "cioccolato = 巧克力",
     "A Perugia si festeggia il ___.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "laboratorio", "laboratorio = 工坊（此处）",
     "Per i più piccoli c'è il ___ della dolcezza.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "degustazione", "degustazione = 品尝会",
     "Alla festa c'è una ___ con i dolci.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "mandorle", "mandorle = 杏仁（复数）",
     "Il torrone è fatto di ___ e miele.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "tartufo", "tartufo = 松露",
     "Il ___ bianco è il fungo più prezioso d'Italia.", instr="填空", size=20, gap=8)
e.head("C · IL PASSATO PROSSIMO", 25)
e.bridge("用 passato prossimo（近过去时）补全，注意助动词 avere / essere。")
e.ex("B1", "完成句子", "è arrivato", "arrivare 用 essere：è arrivato",
     "Il Treno Storico ___ (arrivare) a Cremona domenica.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "abbiamo assaggiato", "assaggiare 用 avere：abbiamo assaggiato",
     "Noi ___ (assaggiare) il torrone a Cremona.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "sono andati", "andare 用 essere，复数 sono andati",
     "I visitatori ___ (andare) a Perugia per Eurochocolate.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "ha aperto", "aprire 用 avere：ha aperto",
     "Perugia ___ (aprire) Eurochocolate venerdì.", instr="填空", size=20, gap=8)
e.head("D · COSTRUISCI LE FRASI", 25)
e.bridge("把词组成正确的句子。")
e.ex("B1", "造句", "Eurochocolate è a Perugia dal 13 novembre.", "主语 + essere + 地点 + 日期",
     "Eurochocolate / è a Perugia / dal 13 novembre → ___", instr="造句", size=20, gap=8)
e.ex("A2", "造句", "A Cremona il torrone è il re.", "地点在前，主语在后",
     "a Cremona / il torrone / è il re → ___", instr="造句", size=20, gap=8)
e.ex("B1", "造句", "La fiera dura fino al 6 dicembre.", "dura fino a = 持续到",
     "la fiera / dura / fino al 6 dicembre → ___", instr="造句", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT · 体育", "La Lucerna", "LIVELLO B1 · Le notti azzurre e il tennis · 国家队之夜与网球")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("Due notti azzurre: Francia a San Siro, Belgio a Bruxelles", 37)
f.byline("Dalla redazione sportiva de La Lucerna · Livello di lettura: B1")
f.para("È una settimana di grande calcio, senza Serie A: il campionato si ferma per la sosta delle nazionali. Giovedì 12 novembre, alle 20.45, l'Italia gioca a San Siro con la Francia, nella quinta giornata di Nations League. Domenica 15 novembre, alle 20.45, gli Azzurri chiudono il girone a Bruxelles, con il Belgio.")
f.para("Nel girone 1 di Lega A, la Francia è prima con 10 punti, l'Italia è seconda con 7, il Belgio è terzo con 6 e la Turchia è a zero. Le prime due vanno ai quarti di finale, a marzo 2027. Per l'Italia, le due partite di questa settimana sono decisive: attenzione, qui sono presentazioni, senza risultati.")
f.para("Giovedì e domenica il calcio scende in campo anche per la ricerca: con «Un gol per la ricerca», le partite ricordano i Giorni della Ricerca AIRC, che durano fino al 15 novembre e raccontano il lavoro di più di 770 progetti di ricerca.")
f.para("Domenica 15 novembre comincia anche un'altra storia: a Torino, all'Inalpi Arena, iniziano le Nitto ATP Finals, con gli otto migliori giocatori e le otto migliori coppie di doppio. Giovedì 12 novembre, all'Inalpi Arena, c'è il Grand Opening Show con Achille Lauro.")
f.para("E per chi segue la Serie A: l'undicesima giornata, giocata dal 6 all'8 novembre, è appena finita — i risultati e la classifica li leggiamo nel prossimo numero. La dodicesima giornata si gioca dal 21 al 23 novembre: Como–Cagliari e Lazio–Lecce sabato, Juventus–Venezia, Bologna–Udinese, Sassuolo–Genoa e Milan–Frosinone domenica, Atalanta–Inter la sera, Monza–Fiorentina lunedì.")
f.gloss("la sosta 休赛期 · il girone 小组 · decisivo 决定性的 · la presentazione 赛前介绍。")
f.end_report()

# col 3: data box + e tu? (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 436, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 240, "LE PARTITE DA SEGNARE", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "Giovedì 12 novembre, ore 20.45 · Italia – Francia, a San Siro, Nations League. Domenica 15 novembre, ore 20.45 · Belgio – Italia, a Bruxelles. Domenica 15 novembre · ATP Finals a Torino: iniziano le gare all'Inalpi Arena.", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 662
etvous = "E tu? Quale partita guardi giovedì sera? Scrivi due frasi in italiano."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("周四晚上你看哪场比赛？写两句意大利语寄来。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "E TU? · 说说你自己", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "周四晚上你看哪场比赛？写两句意大利语寄来。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "LA SETTIMANA DELLO SPORT · 体育周", 26, "sans", True, OLIVE)
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
p.text(MX, ey + 28, "ESERCIZI · 第 4 版练习", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案见第 8 版 · 题目可跨级混排，按题号找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A · COMPRENSIONE", 25)
e.bridge("读第 4 版文章，选出正确答案。")
e.ex("B1", "单选", "B", "意大利对法国在 11 月 12 日周四",
     "Italia–Francia si gioca... A. domenica 15 novembre · B. giovedì 12 novembre · C. lunedì 9 novembre", size=20, gap=8)
e.ex("B1", "单选", "B", "周日意大利在布鲁塞尔对战比利时",
     "Domenica, l'Italia gioca... A. a San Siro · B. a Bruxelles · C. a Torino", size=20, gap=8)
e.ex("B1", "单选", "A", "小组第一是法国 10 分",
     "Nel girone, la Francia ha... A. 10 punti · B. 7 punti · C. 6 punti", size=20, gap=8)
e.ex("B1", "单选", "C", "国家队比赛只作前瞻、无结果",
     "Le partite dell'Italia, in questo giornale, sono... A. risultati finali · B. cancellate · C. presentazioni senza risultati", size=20, gap=8)
e.ex("B1", "单选", "B", "ATP 总决赛在都灵",
     "Le ATP Finals si giocano... A. a Milano · B. a Torino · C. a Bruxelles", size=20, gap=8)
e.head("B · LE PAROLE", 25)
e.match_set("B1", "词汇配对",
            ["la sosta", "il girone", "decisivo", "la presentazione"],
            ["il racconto prima della partita, senza risultati",
             "che decide tutto, molto importante",
             "il gruppo di squadre che giocano tra loro",
             "la pausa del campionato, senza partite"],
            ["d", "c", "b", "a"],
            ["sosta=休赛期 d", "girone=小组 c", "decisivo=决定性的 b", "presentazione=赛前介绍 a"],
            instr="把词和释义配对")
e.head("C · I COMPARATIVI", 25)
e.bridge("用括号里词的比较级填空（数据看赛程表）。")
e.ex("B1", "完成句子", "più tardi", "两场比赛都在 20.45 开始，周日的比赛并不比周四的晚：più tardi",
     "Le partite di domenica sera NON cominciano ___ di quelle di giovedì. (tardi)", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "più presto", "两场比赛都在 20.45 开始，周四的比赛并不比周日的早：più presto",
     "Le partite di giovedì NON cominciano ___ di quelle di domenica. (presto)", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "più bella", "più + bella 周四晚最美（主观评价）",
     "Per i tifosi, la serata di giovedì è la serata ___ del weekend. (bella)", instr="填空", size=20, gap=8)
e.ex("B2", "句型转换", "meglio", "bene 的比较级是不规则的 meglio",
     "L'Italia gioca bene. → L'Italia gioca ___ (bene).", instr="填空", size=20, gap=8)
e.head("D · IL PASSATO DELLO SPORT", 25)
e.bridge("用 passato prossimo 补全。")
e.ex("B1", "完成句子", "ha vinto", "vincere：ha vinto",
     "La mia squadra ___ (vincere) la partita di ieri.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "ha pareggiato", "pareggiare：ha pareggiato",
     "La mia squadra ___ (pareggiare) 1–1.", instr="填空", size=20, gap=8)
e.ex("B2", "完成句子", "sono arrivati", "arrivare 用 essere，复数 sono arrivati",
     "I tifosi ___ (arrivare) allo stadio alle cinque.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "abbiamo guardato", "guardare 用 avere：abbiamo guardato",
     "Noi ___ (guardare) la partita in televisione.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "ha preso", "prendere 的分词是 preso：ha preso",
     "Il portiere ___ (prendere) un gol al 90°.", instr="填空", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
