# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-it-ja/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · GIOVANI (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("GIOVANI　若者", "La Lucerna", "LIVELLO B1　Leggere, guardare, giocare　読む、観る、遊ぶ")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-main")
f.title("I giovani leggono: BookCity arriva, il cinema torna a Torino", 37)
f.byline("Dalla redazione de La Lucerna　Livello di lettura: B1")
f.para("Dal 23 al 29 novembre, a Milano, torna BookCity, la festa dei libri e della lettura: la quindicesima edizione, con il tema «Il senno sulla Luna», ispirato all'Orlando furioso di Ludovico Ariosto: sette giorni di libri, ragioni e follie, con 1.360 eventi, 2.487 protagonisti e 1.164 libri presentati, in 443 sedi.")
f.para("L'apertura è lunedì 23 novembre, alle 20, al Teatro Dal Verme, con lo scrittore statunitense Colson Whitehead, due volte vincitore del Premio Pulitzer. Ma l'anteprima è già domenica 22 novembre, alle 16, alla Fondazione Luigi Rovati, con Edmund de Waal.")
f.para("E martedì 24 novembre, a Torino, apre il Torino Film Festival, la 44ª edizione, fino al 2 dicembre: nove giorni di film, incontri e anteprime per chi ama il cinema. A Milano, invece, domenica 22 novembre si chiude il Filmmaker Festival, il festival del cinema indipendente, aperto dal 14 novembre.")
f.para("Nel weekend, poi, la scelta è dolce e azzurra: Eurochocolate a Perugia e la Festa del Torrone a Cremona (pagina 3), e domenica sera Atalanta–Inter (pagina 4). Il consiglio della redazione: un libro in mano, un film negli occhi — e domenica sera, la grande partita.")
f.box("IL PIANO DELLA SETTIMANA", [
    ("1. Venerdì: a Perugia, «I tesori della Calabria» a Eurochocolate（金曜：ペルージャのチョコレート祭、カラブリア特集）", "serif", False, INK, 21, 1.36),
    ("2. Sabato: Madonna della Salute a Venezia（土曜：ヴェネツィアの聖母健康祭）", "serif", False, INK, 21, 1.36),
    ("3. Domenica: chiude il Filmmaker Festival（日曜：フィルムメーカー映画祭が閉幕）", "serif", False, INK, 21, 1.36),
    ("4. Domenica: Atalanta–Inter, ore 20.45（日曜20:45：アタランタ対インテル）", "serif", False, INK, 21, 1.36),
    ("5. Lunedì: apre BookCity a Milano（月曜：ミラノでブックシティ開幕）", "serif", False, INK, 21, 1.36),
])
f.gloss("l'anteprima プレビュー · il protagonista 主役・ゲスト · la sede 会場 · l'incontro 交流会 · indipendente 独立の。")
f.end_report()

# col 3: lettrice image + facts + e tu? (sequential)
ix = COLX[3]
image(p, "lettrice.jpg", ix, 200, CW, 300)
cy3 = caption(p, ix, 500, CW, "Una giovane lettrice, in un quadro del 1868: leggere è il primo passo per imparare una lingua — e BookCity è la festa dei lettori.",
              "Foto: Jean-Baptiste-Camille Corot — Wikimedia Commons, dominio pubblico")
facts = ["BookCity, Milano: dal 23 al 29 novembre, 15ª edizione, tema «Il senno sulla Luna».",
         "Torino Film Festival: dal 24 novembre al 2 dicembre, 44ª edizione.",
         "Filmmaker Festival, Milano: chiude domenica 22 novembre."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "I GIOVANI IN NUMERI", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E tu? Preferisci un libro, un film o una partita? Scrivi due frasi in italiano."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("本と映画と試合、どれが好きですか。二文書いて送りましょう。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill=BOX)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E TU?　あなたは？", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "本と映画と試合、どれが好きですか。二文書いて送りましょう。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ESERCIZI　5ページの練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答えは8ページ　レベルは混ざっています—番号で探しなさい", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A　COMPRENSIONE", 25)
e.bridge("5ページの記事を読んで、正しい答えを選びなさい。")
e.ex("B1", "選択問題", "B", "ブックシティは第15回",
     "BookCity è alla sua... A. 14ª edizione · B. 15ª edizione · C. 32ª edizione", size=20, gap=8)
e.ex("B1", "選択問題", "B", "ブックシティは11月23日から",
     "BookCity comincia... A. il 20 novembre · B. il 23 novembre · C. il 29 novembre", size=20, gap=8)
e.ex("B1", "選択問題", "C", "今年のテーマはアリオストから",
     "Il tema «Il senno sulla Luna» viene da... A. Dante · B. Manzoni · C. Ariosto", size=20, gap=8)
e.ex("B1", "選択問題", "A", "トリノ映画祭は第44回",
     "Il Torino Film Festival è alla sua... A. 44ª edizione · B. 15ª edizione · C. 29ª edizione", size=20, gap=8)
e.ex("B1", "選択問題", "A", "フィルムメーカー映画祭はミラノで閉幕",
     "Il Filmmaker Festival chiude... A. a Milano · B. a Torino · C. a Cuneo", size=20, gap=8)
e.head("B　LE PAROLE DEL TESTO", 25)
e.bridge("枠の中の語を使って穴埋めしなさい。注意：一部の語は複数形にします。")
e.para("anteprima · protagonista · sede · incontro · indipendente · lettrice", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "文を完成させなさい", "protagonisti", "protagonisti = ゲスト（複数）",
     "BookCity ha 2.487 ___.", instr="穴埋め", size=20, gap=8)
e.ex("B1", "文を完成させなさい", "indipendente", "indipendente = 独立の",
     "Il Filmmaker Festival è un festival del cinema ___.", instr="穴埋め", size=20, gap=8)
e.ex("B1", "文を完成させなさい", "anteprima", "anteprima = プレビュー",
     "Domenica c'è l'___ di BookCity a Milano.", instr="穴埋め", size=20, gap=8)
e.ex("B1", "文を完成させなさい", "sedi", "sedi = 会場（複数）",
     "BookCity ha 443 ___ a Milano e dintorni.", instr="穴埋め", size=20, gap=8)
e.ex("B1", "文を完成させなさい", "lettrice", "lettrice = 女性の読者",
     "La giovane ___ del quadro legge in silenzio.", instr="穴埋め", size=20, gap=8)
e.ex("B1", "文を完成させなさい", "incontri", "incontri = 交流会（複数）",
     "Al festival ci sono tanti ___ con gli autori.", instr="穴埋め", size=20, gap=8)
e.head("C　IL FUTURO", 25)
e.bridge("単純未来（futuro semplice）で補いなさい。")
e.ex("B1", "文を完成させなさい", "andremo", "andare 未来形 noi：andremo",
     "Lunedì noi ___ (andare) a BookCity a Milano.", instr="穴埋め", size=20, gap=8)
e.ex("B2", "文を完成させなさい", "ci sarà", "esserci 未来形：ci sarà（～があるだろう）",
     "A Milano ___ (esserci) tanto cinema giovane.", instr="穴埋め", size=20, gap=8)
e.ex("B1", "文を完成させなさい", "guarderemo", "guardare 未来形 noi：guarderemo",
     "Domenica noi ___ (guardare) Atalanta–Inter.", instr="穴埋め", size=20, gap=8)
e.ex("B2", "文を完成させなさい", "durerà", "durare 未来形：durerà",
     "BookCity ___ (durare) fino al 29 novembre.", instr="穴埋め", size=20, gap=8)
e.head("D　VERO O FALSO?", 25)
e.ex("B1", "正誤問題", "Vero", "ブックシティは1,360件の行事がある",
     "BookCity ha 1.360 eventi. Vero o falso?", instr="正誤判定", size=20, gap=8)
e.ex("B1", "正誤問題", "Vero", "トリノ映画祭は11月24日に開幕",
     "Il Torino Film Festival apre il 24 novembre. Vero o falso?", instr="正誤判定", size=20, gap=8)
e.ex("B2", "正誤問題", "Falso", "ブックシティが11月22日に開幕するのは誤り",
     "BookCity apre il 22 novembre. Vero o falso?", instr="正誤判定", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-giovani.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · APPROFONDIMENTO (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("APPROFONDIMENTO　深読み", "La Lucerna", "LIVELLO B2　La manovra in Parlamento　議会の予算案")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1520, tag="P6-main")
f.title("La manovra va in Parlamento: audizioni, emendamenti, voto", 37)
f.byline("Dalla redazione de La Lucerna　Livello di lettura: B2　La legge di bilancio e i numeri")
f.para("La manovra è la legge di bilancio: il documento che dice come lo Stato spende e dove trova i soldi. Il Documento programmatico di bilancio (DPB), mandato a Bruxelles il 15 ottobre, prevede per il 2027 una crescita del +0,8% e un deficit del 3,4% del PIL. Il 28 ottobre il Consiglio dei ministri ha approvato il disegno di legge: circa 26 miliardi di euro, secondo le ricostruzioni dei giornali.")
f.para("Dal 9 al 12 novembre, le commissioni Bilancio di Camera e Senato ascoltano enti e istituzioni: quattro giorni di audizioni, fino a giovedì 12 novembre, con la Banca d'Italia, l'Ufficio parlamentare di bilancio e il ministro Giorgetti. Il termine per presentare gli emendamenti è martedì 17 novembre, alle 18.")
f.para("Attenzione, però: approvato dal governo non vuol dire già legge. Il Parlamento decide, non il governo da solo. Il testo, alla Camera con il numero C. 3174-bis, deve essere discusso e votato dalle Camere entro il 31 dicembre, e il testo può ancora cambiare. Chi legge i giornali trova cifre diverse per le coperture — circa 5 miliardi dal settore finanziario, banche e assicurazioni, secondo le prime ricostruzioni — perché il testo definitivo si conosce solo alla fine dell'iter.")
f.para("Tra le misure raccontate dai giornali: l'allargamento del secondo scaglione Irpef al 33%, da 50 mila a 55 mila euro, e più soldi per la sanità. Sono misure raccontate, non ancora votate: il lettore saggio distingue tra «il governo propone» e «la legge dice».")
f.bridge("締め切り時点で議会はまだ採決していません。本号は日付、DPBの数字、報道された施策のみで、採決結果は載せていません。")
f.gloss("la manovra 予算案 · l'audizione 公聴会 · l'emendamento 修正案 · il deficit 赤字 · la copertura 財源 · lo scaglione 税率区分 · l'iter 審議手続き。")
f.end_report()

# col 3: timeline + leggere i numeri (sequential, measured)
bx = COLX[3]
p.rect(bx, 200, CW, 640, fill=BOX)
p.text(bx + 22, 240, "LA STRADA DELLA MANOVRA", 22, "sans", True, OLIVE)
steps = [
    ("28 OTT.", "Il Consiglio dei ministri approva il disegno di legge, circa 26 miliardi."),
    ("9–12 NOV.", "Audizioni in commissione Bilancio: si chiude giovedì 12 con Giorgetti."),
    ("MAR 17 NOV.", "Scade il termine per gli emendamenti, alle ore 18."),
    ("31 DIC.", "Le Camere devono votare il testo: può ancora cambiare."),
]
sy3 = 282
for w, t in steps:
    p.text(bx + 22, sy3 + 21, w, 20, "sans", True, OLIVE)
    # FIX 2026-11-12 (F-2): MAR 17 NOV. label ink ends bx+161.9; body at bx+164 left
    # only a 2px gap ("NOV.Scade"). Give this row a full word space (bx+172, gap 10px);
    # right edge stays bx+CW-22. Other rows unchanged.
    bx_body = bx + 172 if w == "MAR 17 NOV." else bx + 164
    sy3 = p.para(bx_body, sy3 + 21, t, 21, "serif", False, INK, CW - 22 - (bx_body - bx), 1.4) + 16
by3 = 866
bb = ("Davanti a una cifra della manovra, fai tre domande: chi la pubblica? Quando? "
      "È una proposta del governo o una legge votata? Senza queste tre risposte, un numero dice poco.")
bh = 62 + len(wrap(bb, "serif", False, 21.5, CW - 44)) * 30.5 + 16
p.rect(bx, by3, CW, bh, fill=BOX)
yy3 = by3 + 16
p.text(bx + 22, yy3 + 26, "LEGGERE I NUMERI", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, bb, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P6 col3 ends", by3 + bh)

# ---- Practice-data chart (explicitly labeled as exercise data) ----
gy = 1566
p.hline(MX, RIGHT, gy - 18, OLIVE, 2)
p.text(MX, gy + 10, "LE MINIME DI ESEMPIO　練習用の最低気温の例 (DATI INVENTATI PER L'ESERCIZIO)", 26, "sans", True, OLIVE)
dpb = [("Torino", 5.0),
       ("Milano", 6.0),
       ("Bologna", 7.0),
       ("Roma", 11.0),
       ("Napoli", 13.0)]
bx1, bw_, bhh = MX, 2 * CW + GUT, 322
p.rect(bx1, gy + 28, bw_, bhh, fill=BOX)
p.text(bx1 + 22, gy + 68, "MINIME DI ESEMPIO　gradi, dati inventati", 21, "sans", True, INK)
yy = gy + 96
for lab, v in dpb:
    p.text(bx1 + 22, yy + 24, lab, 20, "serif", True, INK)
    labw = text_w(lab, "serif", True, 20)
    p.rect(bx1 + 40 + labw, yy + 6, v * 34, 22, fill=OLIVE)
    p.text(bx1 + 58 + labw + v * 34, yy + 24, f"{v:.0f}°", 20.5, "serif", False, INK)
    yy += 38
p.para(bx1 + 22, gy + bhh - 26, "Questi numeri sono inventati per l'esercizio: servono per imparare a leggere un grafico, NON sono previsioni reali.", 17.5, "sans", False, GREY, bw_ - 44, 1.3)
# right box: probabilities
bx2 = COLX[2]
p.rect(bx2, gy + 28, bw_, bhh, fill=BOX)
p.text(bx2 + 22, gy + 68, "PROPOSTA ≠ LEGGE", 21, "sans", True, INK)
p.para(bx2 + 22, gy + 118, "«Il governo propone» ≠ «la legge dice»", 23, "serif", True, INK, bw_ - 44, 1.35)
p.para(bx2 + 22, gy + 158, "Una cifra raccontata ≠ una cifra votata", 23, "serif", True, INK, bw_ - 44, 1.35)
p.para(bx2 + 22, gy + 198, "Il testo definitivo si conosce solo alla fine dell'iter in Parlamento.", 19.5, "serif", False, INK, bw_ - 44, 1.4)
p.para(bx2 + 22, gy + bhh - 62, "Le cifre della manovra si aggiornano con il dibattito: controllale prima di citarle.", 17.5, "sans", False, GREY, bw_ - 44, 1.3)

# ---- P6 exercises ----
ey = 1930
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ESERCIZI　6ページの練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答えは8ページ　レベルは混ざっています—番号で探しなさい", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A　LEGGERE IL GRAFICO", 25)
e.bridge("上の練習用グラフを見て、正しい答えを選びなさい。")
e.ex("B2", "選択問題", "B", "例のデータで一番寒いのはトリノ、5°",
     "La città più fredda del grafico è... A. Milano · B. Torino · C. Napoli", size=18, gap=2)
e.ex("B2", "選択問題", "A", "例のデータで一番暖かいのはナポリ、13°",
     "La città più calda del grafico è... A. Napoli · B. Roma · C. Bologna", size=18, gap=2)
e.ex("B2", "選択問題", "B", "13 − 11 = 2",
     "La differenza tra Napoli (13°) e Roma (11°) è... A. 3° · B. 2° · C. 4°", size=18, gap=2)
e.ex("B2", "選択問題", "A", "6 + 7 = 13",
     "Milano (6°) e Bologna (7°) insieme fanno... A. 13° · B. 12° · C. 14°", size=18, gap=2)
e.ex("B2", "選択問題", "B", "グラフの数字は練習用のデータで、本物の予報ではありません",
     "I numeri del grafico sono... A. previsioni reali · B. dati inventati per l'esercizio · C. temperature di ieri", size=18, gap=2)
e.ex("B2", "選択問題", "A", "政府の提案はまだ法律ではない",
     "«Il governo propone»... A. non è ancora legge · B. è già legge · C. è un errore", size=18, gap=2)
e.head("B　COMPRENSIONE", 25)
e.ex("B2", "選択問題", "B", "法案は予算法です",
     "La manovra è... A. una festa · B. la legge di bilancio · C. un film", size=18, gap=2)
e.ex("B2", "選択問題", "A", "修正案の締め切りは11月17日18時",
     "Il termine per gli emendamenti è... A. il 17 novembre · B. il 9 novembre · C. il 31 dicembre", size=18, gap=2)
e.ex("B2", "選択問題", "A", "DPBは10月15日にブリュッセルへ送られた",
     "Il DPB è stato mandato a Bruxelles... A. il 15 ottobre · B. il 19 ottobre · C. il 28 ottobre", size=18, gap=2)
e.ex("B2", "選択問題", "B", "2027年の成長予測 +0.8%",
     "La crescita prevista per il 2027 è... A. +3,4% · B. +0,8% · C. +5%", size=18, gap=2)
e.head("C　IL CONGIUNTIVO", 25)
e.ex("B2", "文を完成させなさい", "piova", "è probabile che + 接続法 piova",
     "È probabile che domani ___ (piovere) in pianura.", instr="穴埋め", size=18, gap=2)
e.ex("B2", "文を完成させなさい", "nevichi", "è possibile che + 接続法 nevichi",
     "È possibile che in montagna ___ (nevicare) nel weekend.", instr="穴埋め", size=18, gap=2)
e.ex("B2", "文を完成させなさい", "controllino", "bisogna che + 接続法 controllino",
     "Bisogna che i lettori ___ (controllare) il testo più recente.", instr="穴埋め", size=18, gap=2)
e.ex("B2", "文を完成させなさい", "sia", "è importante che + 接続法 sia",
     "È importante che la cifra ___ (essere) chiara per tutti.", instr="穴埋め", size=18, gap=2)
e.head("D　LE PAROLE DELLA MANOVRA", 23)  # D5 (2026-11-12): was 25, head ran past the column (HEAD TOO WIDE); 23 fits (same defect as core-it)
e.bridge("枠の中の語で穴埋めしなさい：manovra · deficit · copertura · scaglione")
e.ex("B2", "文を完成させなさい", "manovra", "manovra = 予算案",
     "La ___ è la legge di bilancio.", instr="穴埋め", size=18, gap=2)
e.ex("B2", "文を完成させなさい", "deficit", "deficit = 赤字",
     "Il ___ previsto per il 2027 è del 3,4% del PIL.", instr="穴埋め", size=18, gap=2)
e.ex("B2", "文を完成させなさい", "copertura", "copertura = 財源",
     "Ogni misura deve avere la sua ___.", instr="穴埋め", size=18, gap=2)
e.ex("B2", "文を完成させなさい", "scaglione", "scaglione = 税率区分",
     "Il secondo ___ Irpef si allarga, secondo le ricostruzioni.", instr="穴埋め", size=18, gap=2)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-approfondimento.svg")
print("P6 saved, exercises so far:", len(REG))
