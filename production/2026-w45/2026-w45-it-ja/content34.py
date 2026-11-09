# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA　文化", "La Lucerna", "A2 → B1　Panettone, torrone e musei aperti　スイーツと美術館")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("Il weekend più dolce: panettone a Milano, torrone a Cremona", 32)
f.byline("Dalla redazione de La Lucerna　Livello di lettura: A2 → B1")
f.para("Il freddo porta con sé la voglia di dolci. Sabato 7 e domenica 8 novembre, a Milano, c'è la finale della Coppa del Mondo del Panettone: pasticceri da 19 paesi si sfidano con il dolce simbolo di Milano, e il pubblico può assaggiare gratis. Due le categorie in gara: il panettone tradizionale e il panettone al cioccolato.")
f.para("Lo stesso fine settimana apre a Cremona la Festa del Torrone, che dura fino al 22 novembre: bancarelle, degustazioni e musica nella città dei violini. Il torrone è un dolce antico, di mandorle e miele — e Cremona ne è la capitale.")
f.para("E il tartufo bianco non va in vacanza: ad Alba, in Piemonte, la Fiera del Tartufo Bianco continua fino al 6 dicembre, con mercati e piatti speciali. Il re dell'autunno resta in tavola anche con il primo freddo.")
f.para("Per chi ama la cultura, la settimana comincia martedì 3 novembre a Milano con il Forum Cultura: più di 50 eventi e aperture straordinarie di musei e biblioteche. Si comincia con il cantiere di restauro della Sala delle Asse al Castello Sforzesco, la GAM e Palazzo Morando; nel fine settimana il Forum si sposta alla Bovisa, al sito della Goccia.")
f.gloss("il panettone パネットーネ · il torrone トローネ · l'assaggio 試食 · la bancarella 屋台 · il cantiere 工事現場")
f.head("IL TARTUFO RESTA IN TAVOLA", 25)
f.para("La Fiera di Alba è aperta dal 10 ottobre: quasi due mesi di profumi e piatti speciali. Con il freddo, il tartufo bianco diventa ancora più prezioso — e i ristoranti lo servono con pasta, uova e risotti.", 23.5)
f.end_report()

# col 3: truffle image + facts + e tu? (sequential)
ix = COLX[3]
image(p, "tartufo.jpg", ix, 200, CW, 265)
cy3 = caption(p, ix, 465, CW, "Un tartufo bianco, il fungo più prezioso d'Italia. Ad Alba la fiera dura fino al 6 dicembre; con il primo freddo, il tartufo è ancora più prezioso.",
              "Foto: Wikimedia Commons — dominio pubblico")
facts = ["Milano, 7–8 novembre: finale della Coppa del Mondo del Panettone, degustazioni gratuite.",
         "Cremona, 7–22 novembre: Festa del Torrone, bancarelle e musica.",
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
etvous = "E tu? Preferisci il panettone tradizionale o quello al cioccolato? Scrivi due frasi in italiano e mandale alla redazione."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("伝統的なパネットーネとチョコレート味、どちらが好き？2文書いて送りましょう。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E TU?　あなたは？", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "伝統的なパネットーネとチョコレート味、どちらが好き？2文書いて送りましょう。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ESERCIZI　3ページの練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答えは8ページ　レベル混合出題、番号で答えを探す", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P3-ex")
e.head("A　COMPRENSIONE", 25)
e.expl("3ページの記事を読んで、正しい答えを選びましょう。")
e.ex("A2", "単一選択", "B", "パネットーネ決勝はミラノで",
     "La finale della Coppa del Mondo del Panettone è a... A. Cremona · B. Milano · C. Alba", size=20, gap=8)
e.ex("A2", "単一選択", "C", "クレモナのトローネ祭りは11月22日まで",
     "La Festa del Torrone dura fino al... A. 6 dicembre · B. 8 novembre · C. 22 novembre", size=20, gap=8)
e.ex("A2", "単一選択", "B", "パネットーネ決勝には19か国の菓子職人",
     "Alla finale del Panettone partecipano pasticceri da... A. 5 paesi · B. 19 paesi · C. 50 paesi", size=20, gap=8)
e.ex("B1", "単一選択", "A", "文化フォーラムは11月3日火曜に開幕",
     "Il Forum Cultura apre... A. martedì 3 novembre · B. sabato 7 novembre · C. lunedì 2 novembre", size=20, gap=8)
e.ex("B1", "単一選択", "B", "アルバのトリュフ祭りは12月6日まで",
     "La Fiera del Tartufo Bianco di Alba chiude... A. il 22 novembre · B. il 6 dicembre · C. l'8 novembre", size=20, gap=8)
e.head("B　LE PAROLE DEL TESTO", 25)
e.expl("枠の中の語で空所を補いましょう。")
e.para("panettone · torrone · assaggio · bancarella · tartufo · mandorle", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "文を完成させる", "panettone", "panettone = ミラノのクリスマス菓子",
     "Il ___ è il dolce simbolo di Milano.", instr="空所補充", size=20, gap=8)
e.ex("A2", "文を完成させる", "torrone", "torrone = トローネ",
     "A Cremona si festeggia il ___.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文を完成させる", "assaggio", "assaggio = 試食",
     "Alla finale del Panettone, il pubblico può fare un ___ gratis.", instr="空所補充", size=20, gap=8)
e.ex("A2", "文を完成させる", "bancarella", "bancarella = 屋台",
     "Alla festa ci sono tante ___ con i dolci.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文を完成させる", "mandorle", "mandorle = アーモンド（複数）",
     "Il torrone è fatto di ___ e miele.", instr="空所補充", size=20, gap=8)
e.ex("A2", "文を完成させる", "tartufo", "tartufo = トリュフ",
     "Il ___ bianco è il fungo più prezioso d'Italia.", instr="空所補充", size=20, gap=8)
e.head("C　IL PASSATO PROSSIMO", 25)
e.expl("passato prossimo（近過去）で補いましょう。助動詞avere / essereに注意。")
e.ex("B1", "文を完成させる", "è arrivato", "arrivareはessere：è arrivato",
     "Il primo freddo ___ (arrivare) lunedì.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文を完成させる", "abbiamo assaggiato", "assaggiareはavere：abbiamo assaggiato",
     "Noi ___ (assaggiare) il panettone a Milano.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文を完成させる", "sono andati", "andareはessere、複数sono andati",
     "I pasticceri ___ (andare) a Milano per la finale.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文を完成させる", "ha aperto", "aprireはavere：ha aperto",
     "Cremona ___ (aprire) la Festa del Torrone sabato.", instr="空所補充", size=20, gap=8)
e.head("D　COSTRUISCI LE FRASI", 25)
e.expl("語を並べて正しい文を作りましょう。")
e.ex("B1", "文を作る", "La finale è a Milano il 7 novembre.", "主語 + essere + 場所 + 日付",
     "la finale / è a Milano / il 7 novembre → ___", instr="文を作る", size=20, gap=8)
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
p.band("SPORT　スポーツ", "La Lucerna", "LIVELLO B1　La Serie A e l'Europa　セリエAと欧州戦")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("L'undicesima giornata: Genoa–Milan, Inter–Como, Fiorentina–Juventus", 32)
f.byline("Dalla redazione sportiva de La Lucerna　Livello di lettura: B1")
f.para("È una settimana di grande calcio. Da martedì 3 a giovedì 5 novembre si gioca la quarta giornata delle coppe europee: Champions League, Europa League e Conference League. Attenzione: queste partite si giocano dopo la chiusura del giornale — qui sono una presentazione, senza risultati.")
f.para("Poi arriva l'undicesima giornata di Serie A, da venerdì 6 a domenica 8 novembre. La giornata chiude domenica 8 novembre con tre partite grandi: Genoa–Milan, Inter–Como e Fiorentina–Juventus, la sera a Firenze.")
f.para("Domenica è anche il giorno del freddo sugli spalti: chi va allo stadio mette sciarpa e guanti, come a pagina 2. Ma il calcio non si ferma per il primo freddo — anzi, con il freddo le partite della sera diventano ancora più belle, sotto le luci.")
f.para("E per chi segue i giovani: anche le squadre giovani giocano nel weekend. Il consiglio della redazione è uno solo: scegli una partita, guarda il calendario e non perderti la domenica sera a Firenze.")
f.gloss("la giornata 節 · la presentazione 事前紹介 · gli spalti 観客席 · la sera 夜")
f.end_report()

# col 3: data box + e tu? (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 436, fill=BOX)
p.text(bx + 22, 240, "LE PARTITE DA SEGNARE", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "Martedì 3 – giovedì 5 novembre · Coppe europee, 4ª giornata — si giocano dopo la chiusura del giornale. Venerdì 6 – domenica 8 novembre · Serie A, 11ª giornata. Domenica 8 novembre · Genoa – Milan; Inter – Como; Fiorentina – Juventus (sera, a Firenze).", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 662
etvous = "E tu? Quale partita guardi domenica sera? Scrivi due frasi in italiano."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("日曜の夜、どの試合を見ますか？イタリア語で2文書いて送りましょう。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "E TU?　あなたは？", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "日曜の夜、どの試合を見ますか？イタリア語で2文書いて送りましょう。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "LA SETTIMANA DEL CALCIO　サッカーの週", 26, "sans", True, OLIVE)
rows = [
    ("Mar–Gio", "Coppe europee · 4ª giornata", "Champions, Europa e Conference League: presentazione, senza risultati"),
    ("Ven–Dom", "Serie A · 11ª giornata", "L'undicesima giornata si gioca da venerdì 6 a domenica 8 novembre"),
    ("Dom 8.11", "Serie A", "Genoa – Milan — domenica, a Genova"),
    ("Dom 8.11", "Serie A", "Inter – Como — a San Siro, a Milano"),
    ("Dom 8.11", "Serie A · sera", "Fiorentina – Juventus — la sera, a Firenze"),
]
yy = ty + 16
for i, (d, t, m) in enumerate(rows):
    p.rect(MX, yy, RIGHT - MX, 44, fill="#f4efe0" if i % 2 == 0 else "#efe8d2")
    p.text(MX + 18, yy + 29, d, 20.5, "sans", True, OLIVE)
    p.text(MX + 185, yy + 29, t, 20, "sans", False, GREY)
    p.text(MX + 470, yy + 29, m, 21, "serif", False, INK)
    yy += 44
tnote = "Attenzione: le partite europee di martedì–giovedì e le partite di Serie A del weekend si giocano dopo la chiusura di questa edizione — per questo qui sono presentazioni, senza risultati."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ESERCIZI　4ページの練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答えは8ページ　レベル混合出題、番号で答えを探す", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P4-ex")
e.head("A　COMPRENSIONE", 25)
e.expl("4ページの記事を読んで、正しい答えを選びましょう。")
e.ex("B1", "単一選択", "B", "セリエA第11節は日曜に閉幕",
     "L'undicesima giornata di Serie A chiude... A. venerdì · B. domenica 8 novembre · C. lunedì", size=20, gap=8)
e.ex("B1", "単一選択", "B", "日曜の夜フィオレンティーナ対ユヴェントス",
     "Domenica sera, a Firenze, si gioca... A. Inter–Como · B. Fiorentina–Juventus · C. Genoa–Milan", size=20, gap=8)
e.ex("B1", "単一選択", "A", "欧州戦第4節は11月3～5日",
     "La quarta giornata delle coppe europee si gioca... A. dal 3 al 5 novembre · B. dal 6 all'8 novembre · C. il 2 novembre", size=20, gap=8)
e.ex("B1", "単一選択", "C", "欧州戦は展望のみ、結果なし",
     "Le partite europee, in questo giornale, sono... A. risultati finali · B. cancellate · C. presentazioni senza risultati", size=20, gap=8)
e.ex("B1", "単一選択", "B", "インテル対コモはサン・シーロで",
     "Inter–Como si gioca... A. a Firenze · B. a San Siro · C. a Genova", size=20, gap=8)
e.head("B　LE PAROLE", 25)
e.match_set("B1", "単語の組み合わせ",
            ["la giornata", "la presentazione", "gli spalti", "la sera"],
            ["il posto del pubblico allo stadio, con le gradinate",
             "il racconto prima della partita, senza risultati",
             "ciascuna delle parti del campionato, una dopo l'altra",
             "la parte del giorno dopo il tramonto, con le luci accese"],
            ["c", "b", "a", "d"],
            ["giornata = リーグの一節、c", "presentazione = 事前紹介、b", "spalti = 観客席、a", "sera = 夜、d"],
            instr="語と意味を結ぶ")
e.head("C　I COMPARATIVI", 25)
e.expl("かっこの語の比較級で補いましょう（データは日程表参照）。")
e.ex("B1", "文を完成させる", "più tardi", "日曜夜の試合は金曜より遅い：più tardi",
     "Le partite di domenica sera cominciano ___ di quelle di venerdì. (tardi)", instr="空所補充", size=20, gap=8)
e.ex("B1", "文を完成させる", "più presto", "金曜の試合は日曜より早い：più presto",
     "Le partite di venerdì cominciano ___ di quelle di domenica. (presto)", instr="空所補充", size=20, gap=8)
e.ex("B1", "文を完成させる", "più bella", "più + bella 日曜夜が一番美しい（主観的評価）",
     "Per i tifosi, la domenica sera è la serata ___ del weekend. (bella)", instr="空所補充", size=20, gap=8)
e.ex("B2", "文型変換", "meglio", "beneの比較級は不規則なmeglio",
     "L'Inter gioca bene. → L'Inter gioca ___ (bene).", instr="空所補充", size=20, gap=8)
e.head("D　IL PASSATO DELLO SPORT", 25)
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
