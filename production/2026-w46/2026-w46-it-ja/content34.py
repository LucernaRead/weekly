# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-it-ja/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA · 文化", "La Lucerna", "A2 → B1 · Torrone, cioccolato e tartufo · トローネ、チョコレートとトリュフ")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("Due feste dolci: il torrone a Cremona, il cioccolato a Perugia", 37)
f.byline("Dalla redazione de La Lucerna · Livello di lettura: A2 → B1")
f.para("Il secondo weekend della Festa del Torrone è a Cremona, sabato 14 e domenica 15 novembre: laboratori per i più piccoli, degustazioni e una maxi racchetta da tennis fatta di torrone, per il tennis in carrozzina. Domenica 15 novembre arriva anche il Treno Storico Arlecchino, da Milano a Cremona, e lo spettacolo delle Terre di mezzo in piazza del Comune.")
f.para("Lo stesso weekend, venerdì 13 novembre, apre a Perugia Eurochocolate, la 32ª edizione, fino al 22 novembre: il titolo è «Fate dolci», un invito a vivere il cioccolato in modo attivo e creativo, con laboratori, spettacoli e il grande Chocolate Show. La Regione ospite di quest'anno è la Calabria.")
f.para("E il tartufo bianco non va in vacanza: ad Alba, in Piemonte, la Fiera del Tartufo Bianco continua fino al 6 dicembre, con il Mercato Mondiale ogni sabato e domenica. Il re dell'autunno resta in tavola anche con il sole di San Martino.")
f.para("Per chi ama la storia, il torrone di Cremona racconta un matrimonio: la rievocazione è quella di Bianca Maria Visconti e Francesco Sforza, con il corteo storico che torna domenica 22 novembre, l'ultimo giorno della festa. Il tema del 2026 è «Il Confine», la soglia tra tradizione e innovazione.")
f.gloss("il torrone トローネ · il cioccolato チョコレート · il laboratorio 工房 · la degustazione 試食会 · la rievocazione 歴史の再現。")
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
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("トローネとチョコレート、どちらが好き？2文書いて送って。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E TU? · あなたは？", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "トローネとチョコレート、どちらが好き？2文書いて送って。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ESERCIZI · 3ページの練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答えは8ページ · レベル混合出題、番号で答えを探す", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · COMPRENSIONE", 25)
e.expl("3ページの記事を読んで、正しい答えを選びましょう。")
e.ex("A2", "単一選択", "B", "トローネ祭り第2週末：11月14–15日",
     "Il secondo weekend del Torrone è... A. il 7–8 novembre · B. il 14–15 novembre · C. il 21–22 novembre", size=20, gap=8)
e.ex("A2", "単一選択", "C", "チョコレート祭りは11月22日まで",
     "Eurochocolate dura fino al... A. 6 dicembre · B. 15 novembre · C. 22 novembre", size=20, gap=8)
e.ex("A2", "単一選択", "B", "チョコレート祭りは第32回",
     "Eurochocolate è alla sua... A. 29ª edizione · B. 32ª edizione · C. 67ª edizione", size=20, gap=8)
e.ex("B1", "単一選択", "A", "今年のユーロチョコレートのテーマは「Fate dolci」",
     "Il titolo di Eurochocolate 2026 è... A. «Fate dolci» · B. «Il Confine» · C. «Legacy»", size=20, gap=8)
e.ex("B1", "単一選択", "B", "アルバのトリュフ祭りは12月6日まで",
     "La Fiera del Tartufo Bianco di Alba chiude... A. il 22 novembre · B. il 6 dicembre · C. l'8 novembre", size=20, gap=8)
e.head("B · LE PAROLE DEL TESTO", 25)
e.expl("枠の中の語で空所を補いましょう。")
e.para("torrone · cioccolato · laboratorio · degustazione · tartufo · mandorle", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "文を完成させる", "torrone", "torrone = トローネ",
     "A Cremona si festeggia il ___.", instr="空所補充", size=20, gap=8)
e.ex("A2", "文を完成させる", "cioccolato", "cioccolato = チョコレート",
     "A Perugia si festeggia il ___.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文を完成させる", "laboratorio", "laboratorio = 工房（ここでは）",
     "Per i più piccoli c'è il ___ della dolcezza.", instr="空所補充", size=20, gap=8)
e.ex("A2", "文を完成させる", "degustazione", "degustazione = 試食会",
     "Alla festa c'è una ___ con i dolci.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文を完成させる", "mandorle", "mandorle = アーモンド（複数）",
     "Il torrone è fatto di ___ e miele.", instr="空所補充", size=20, gap=8)
e.ex("A2", "文を完成させる", "tartufo", "tartufo = トリュフ",
     "Il ___ bianco è il fungo più prezioso d'Italia.", instr="空所補充", size=20, gap=8)
e.head("C · IL PASSATO PROSSIMO", 25)
e.expl("passato prossimo（近過去）で補いましょう。助動詞avere / essereに注意。")
e.ex("B1", "文を完成させる", "è arrivato", "arrivareはessere：è arrivato",
     "Il Treno Storico ___ (arrivare) a Cremona domenica.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文を完成させる", "abbiamo assaggiato", "assaggiareはavere：abbiamo assaggiato",
     "Noi ___ (assaggiare) il torrone a Cremona.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文を完成させる", "sono andati", "andareはessere、複数sono andati",
     "I visitatori ___ (andare) a Perugia per Eurochocolate.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文を完成させる", "ha aperto", "aprireはavere：ha aperto",
     "Perugia ___ (aprire) Eurochocolate venerdì.", instr="空所補充", size=20, gap=8)
e.head("D · COSTRUISCI LE FRASI", 25)
e.expl("語を並べて正しい文を作りましょう。")
e.ex("B1", "文を作る", "Eurochocolate è a Perugia dal 13 novembre.", "主語 + essere + 場所 + 日付",
     "Eurochocolate / è a Perugia / dal 13 novembre → ___", instr="文を作る", size=20, gap=8)
e.ex("A2", "文を作る", "A Cremona il torrone è il re.", "場所が前、主語が後",
     "a Cremona / il torrone / è il re → ___", instr="文を作る", size=20, gap=8)
e.ex("B1", "文を作る", "La fiera dura fino al 6 dicembre.", "dura fino a = ～まで続く",
     "la fiera / dura / fino al 6 dicembre → ___", instr="文を作る", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT · スポーツ", "La Lucerna", "LIVELLO B1 · Le notti azzurre e il tennis · アッズーリの夜とテニス")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("Due notti azzurre: Francia a San Siro, Belgio a Bruxelles", 37)
f.byline("Dalla redazione sportiva de La Lucerna · Livello di lettura: B1")
f.para("È una settimana di grande calcio, senza Serie A: il campionato si ferma per la sosta delle nazionali. Giovedì 12 novembre, alle 20.45, l'Italia gioca a San Siro con la Francia, nella quinta giornata di Nations League. Domenica 15 novembre, alle 20.45, gli Azzurri chiudono il girone a Bruxelles, con il Belgio.")
f.para("Nel girone 1 di Lega A, la Francia è prima con 10 punti, l'Italia è seconda con 7, il Belgio è terzo con 6 e la Turchia è a zero. Le prime due vanno ai quarti di finale, a marzo 2027. Per l'Italia, le due partite di questa settimana sono decisive: attenzione, qui sono presentazioni, senza risultati.")
f.para("Giovedì e domenica il calcio scende in campo anche per la ricerca: con «Un gol per la ricerca», le partite ricordano i Giorni della Ricerca AIRC, che durano fino al 15 novembre e raccontano il lavoro di più di 770 progetti di ricerca.")
f.para("Domenica 15 novembre comincia anche un'altra storia: a Torino, all'Inalpi Arena, iniziano le Nitto ATP Finals, con gli otto migliori giocatori e le otto migliori coppie di doppio. Giovedì 12 novembre, all'Inalpi Arena, c'è il Grand Opening Show con Achille Lauro.")
f.para("E per chi segue la Serie A: l'undicesima giornata, giocata dal 6 all'8 novembre, è appena finita — i risultati e la classifica li leggiamo nel prossimo numero. La dodicesima giornata si gioca dal 21 al 23 novembre: Como–Cagliari e Lazio–Lecce sabato, Juventus–Venezia, Bologna–Udinese, Sassuolo–Genoa e Milan–Frosinone domenica, Atalanta–Inter la sera, Monza–Fiorentina lunedì.")
f.gloss("la sosta リーグ中断 · il girone グループ · decisivo 決定的な · la presentazione 試合前紹介。")
f.end_report()

# col 3: data box + e tu? (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 436, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 240, "LE PARTITE DA SEGNARE", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "Giovedì 12 novembre, ore 20.45 · Italia – Francia, a San Siro, Nations League. Domenica 15 novembre, ore 20.45 · Belgio – Italia, a Bruxelles. Domenica 15 novembre · ATP Finals a Torino: iniziano le gare all'Inalpi Arena.", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 662
etvous = "E tu? Quale partita guardi giovedì sera? Scrivi due frasi in italiano."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("木曜の夜、どの試合を見る？イタリア語で2文書いて送って。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "E TU? · あなたは？", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "木曜の夜、どの試合を見る？イタリア語で2文書いて送って。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "LA SETTIMANA DELLO SPORT · スポーツの週", 26, "sans", True, OLIVE)
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
p.text(MX, ey + 28, "ESERCIZI · 4ページの練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答えは8ページ · レベル混合出題、番号で答えを探す", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A · COMPRENSIONE", 25)
e.expl("4ページの記事を読んで、正しい答えを選びましょう。")
e.ex("B1", "単一選択", "B", "イタリア対フランスは11月12日木曜",
     "Italia–Francia si gioca... A. domenica 15 novembre · B. giovedì 12 novembre · C. lunedì 9 novembre", size=20, gap=8)
e.ex("B1", "単一選択", "B", "日曜、イタリアはブリュッセルでベルギーと対戦",
     "Domenica, l'Italia gioca... A. a San Siro · B. a Bruxelles · C. a Torino", size=20, gap=8)
e.ex("B1", "単一選択", "A", "グループ首位はフランス、10点",
     "Nel girone, la Francia ha... A. 10 punti · B. 7 punti · C. 6 punti", size=20, gap=8)
e.ex("B1", "単一選択", "C", "代表の試合はプレビューのみ、結果なし",
     "Le partite dell'Italia, in questo giornale, sono... A. risultati finali · B. cancellate · C. presentazioni senza risultati", size=20, gap=8)
e.ex("B1", "単一選択", "B", "ATPファイナルズはトリノで",
     "Le ATP Finals si giocano... A. a Milano · B. a Torino · C. a Bruxelles", size=20, gap=8)
e.head("B · LE PAROLE", 25)
e.match_set("B1", "単語の組み合わせ",
            ["la sosta", "il girone", "decisivo", "la presentazione"],
            ["il racconto prima della partita, senza risultati",
             "che decide tutto, molto importante",
             "il gruppo di squadre che giocano tra loro",
             "la pausa del campionato, senza partite"],
            ["d", "c", "b", "a"],
            ["sosta=リーグ中断 d", "girone=グループ c", "decisivo=決定的な b", "presentazione=試合前紹介 a"],
            instr="語と意味を結ぶ")
e.head("C · I COMPARATIVI", 25)
e.expl("かっこの語の比較級で補いましょう（データは日程表参照）。")
e.ex("B1", "文を完成させる", "più tardi", "両試合とも20時45分開始：日曜の試合は木曜より遅くない：più tardi",
     "Le partite di domenica sera NON cominciano ___ di quelle di giovedì. (tardi)", instr="空所補充", size=20, gap=8)
e.ex("B1", "文を完成させる", "più presto", "両試合とも20時45分開始：木曜の試合は日曜より早くない：più presto",
     "Le partite di giovedì NON cominciano ___ di quelle di domenica. (presto)", instr="空所補充", size=20, gap=8)
e.ex("B1", "文を完成させる", "più bella", "più + bella：木曜の夜が一番美しい（主観的評価）",
     "Per i tifosi, la serata di giovedì è la serata ___ del weekend. (bella)", instr="空所補充", size=20, gap=8)
e.ex("B2", "文型変換", "meglio", "beneの比較級は不規則なmeglio",
     "L'Italia gioca bene. → L'Italia gioca ___ (bene).", instr="空所補充", size=20, gap=8)
e.head("D · IL PASSATO DELLO SPORT", 25)
e.expl("passato prossimoで補いましょう。")
e.ex("B1", "文を完成させる", "ha vinto", "vincere：ha vinto",
     "La mia squadra ___ (vincere) la partita di ieri.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文を完成させる", "ha pareggiato", "pareggiare：ha pareggiato",
     "La mia squadra ___ (pareggiare) 1–1.", instr="空所補充", size=20, gap=8)
e.ex("B2", "文を完成させる", "sono arrivati", "arrivareはessere、複数sono arrivati",
     "I tifosi ___ (arrivare) allo stadio alle cinque.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文を完成させる", "abbiamo guardato", "guardareはavere：abbiamo guardato",
     "Noi ___ (guardare) la partita in televisione.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文を完成させる", "ha preso", "prendereの分詞はpreso：ha preso",
     "Il portiere ___ (prendere) un gol al 90°.", instr="空所補充", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
