# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-it-ja/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · VALUTAZIONE E RISPOSTE =================
CURPAGE[0] = 8
p = BSPage4()
p.band("VALUTAZIONE E RISPOSTE · 演習と答え", "La Lucerna", "8 ページ · La grande prova della settimana + tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1332, tag="P8-ex")
f.head("A · COMPLETA LA CRONACA", 22, OLIVE, 5)
f.ex("B1", "穴埋め選択", "B", "聖マルティーノ = San Martino",
     "Mercoledì 11 novembre è ___. (A. Natale · B. San Martino)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "ブドウ果汁が新しいワインになる",
     "A San Martino ogni mosto diventa ___. (A. vino · B. latte)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "イタリア対フランスはサン・シーロで",
     "Italia–Francia si gioca a ___. (A. San Siro · B. Cremona)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "チョコレート祭りは金曜に開幕",
     "Eurochocolate apre venerdì a ___. (A. Perugia · B. Cuneo)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "B", "トローネ祭りはクレモナで",
     "La Festa del Torrone continua a ___. (A. Milano · B. Cremona)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "B", "ポポリ映画祭：86作品",
     "Il Festival dei Popoli ha presentato ___ film. (A. 50 · B. 86)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "ベルギー対イタリアは日曜の夜",
     "Belgio–Italia si gioca domenica ___. (A. sera · B. mattina)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "B", "スクリットリンチッタはクーネオで",
     "Scrittorincittà è a ___. (A. Milano · B. Cuneo)", size=15.5, gap=1)
f.head("B · DOMANDE GENERALI", 22, OLIVE, 5)
f.ex("A2", "単一選択", "B", "聖マルティーノの夏は3日と少し続く",
     "L'estate di San Martino dura... A. un mese · B. tre giorni e un pochino · C. un'ora", size=15.5, gap=1)
f.ex("A2", "単一選択", "B", "マントはマルティーノが乞食と分けたもの",
     "Martino divide... A. il pane · B. il mantello · C. il vino", size=15.5, gap=1)
f.ex("A2", "単一選択", "A", "チョコレート祭りは第32回",
     "Eurochocolate è alla sua... A. 32ª edizione · B. 29ª edizione · C. 67ª edizione", size=15.5, gap=1)
f.ex("B1", "単一選択", "B", "グループ1位フランス、10点",
     "Nel girone di Nations League, la Francia ha... A. 7 punti · B. 10 punti · C. 0 punti", size=15.5, gap=1)
f.ex("B1", "単一選択", "C", "アルバのトリュフ祭りは12月6日まで",
     "La Fiera del Tartufo Bianco di Alba chiude... A. il 22 novembre · B. l'8 novembre · C. il 6 dicembre", size=15.5, gap=1)
f.ex("B1", "単一選択", "A", "DPBは10月15日に送付",
     "Il DPB è partito per Bruxelles... A. il 15 ottobre · B. il 19 ottobre · C. il 28 ottobre", size=15.5, gap=1)
f.ex("B2", "単一選択", "B", "政府の提案はまだ法律ではない",
     "«Il governo propone»... A. è già legge · B. non è ancora legge · C. è un errore", size=15.5, gap=1)
f.ex("B1", "単一選択", "B", "ポポリ映画祭は11月8日に閉幕",
     "Il Festival dei Popoli si è chiuso... A. il 31 ottobre · B. l'8 novembre · C. il 15 novembre", size=15.5, gap=1)
f.head("C · LEGGI E RISPONDI", 22, OLIVE, 5)
f.para("Giulia vive a Cuneo: mercoledì 11 novembre va a Scrittorincittà e ascolta un autore. Paolo vive a Cremona: sabato 14 novembre va alla Festa del Torrone. Domenica, Giulia e Paolo guardano Belgio–Italia: è San Martino, ma il calcio non si ferma.", 16.5, lh=1.3, split=False)
f.ex("A2", "単一選択", "B", "ジュリアは水曜にスクリットリンチッタへ行く",
     "Chi va a Scrittorincittà? A. Paolo · B. Giulia · C. i due", size=15.5, gap=1)
f.ex("A2", "単一選択", "A", "Paoloは土曜にトローネ祭りへ",
     "Paolo, sabato, va... A. alla Festa del Torrone · B. a Cuneo · C. allo stadio", size=15.5, gap=1)
f.ex("A2", "単一選択", "B", "作者を聞くのはジュリアだ",
     "L'autore è ascoltato da... A. Paolo · B. Giulia · C. nessuno", size=15.5, gap=1)
f.ex("A2", "単一選択", "A", "タイトルは2都市と2つの祭りをまとめる",
     "Il titolo migliore è... A. «Due città, due feste» · B. «La manovra» · C. «Il meteo»", size=15.5, gap=1)
f.head("D · COSTRUISCI LE FRASI", 22, OLIVE, 5)
f.ex("A2", "文を作る", "Mercoledì è San Martino.", "時間の語が前",
     "mercoledì / è / San Martino → ___", instr="文を作る", size=15.5, gap=1)
f.ex("B1", "文を作る", "Eurochocolate è a Perugia dal 13 novembre.", "主語 + essere + 場所 + 日付",
     "Eurochocolate / è a Perugia / dal 13 novembre → ___", instr="文を作る", size=15.5, gap=1)
f.ex("B1", "文を作る", "A che ora gioca l'Italia?", "疑問の語句が文頭",
     "a che ora / gioca / l'Italia / ? → ___", instr="文を作る", size=15.5, gap=1)
f.ex("B1", "文を作る", "Il vino nuovo si assaggia in cantina.", "主語 + 動詞 + 場所",
     "il vino nuovo / si assaggia / in cantina → ___", instr="文を作る", size=15.5, gap=1)
f.head("E · TRADUCI", 22, OLIVE, 5)
f.ex("A2", "翻译", "聖マルティーノの日にブドウ果汁はワインになる。", "原文と比べる",
     "A San Martino ogni mosto diventa vino. → ___", instr="日本語に翻訳", size=15.5, gap=1)
f.ex("B1", "翻译", "木曜の夜、イタリア対フランス。", "si gioca = 試合が行われる",
     "Giovedì sera si gioca Italia–Francia. → ___", instr="日本語に翻訳", size=15.5, gap=1)
f.ex("B1", "翻译", "日曜の夜、ベルギー対イタリア。", "si gioca = 試合が行われる",
     "Domenica sera si gioca Belgio–Italia. → ___", instr="日本語に翻訳", size=15.5, gap=1)
f.ex("B2", "翻译", "Ogni cifra deve essere chiara.", "dovere = ～しなければならない",
     "すべての数字は明確でなければならない。→ ___", instr="イタリア語に翻訳", size=15.5, gap=1)
f.head("F · LE PAROLE DELLA MANOVRA", 22, OLIVE, 5)
f.match_set("B2", "単語の組み合わせ",
            ["la manovra", "il deficit", "la copertura", "lo scaglione"],
            ["la parte del sistema fiscale, un livello di reddito",
             "i soldi che pagano una misura, la sua fonte",
             "la differenza tra spese ed entrate, in rosso",
             "la legge di bilancio, il documento dello Stato"],
            ["d", "c", "b", "a"],
            ["manovra=予算法案 d", "deficit=赤字 c", "copertura=財源 b", "scaglione=税率区分 a"],
            instr="語と意味を結ぶ")
f.head("G · DIALOGO ALLA SAGRA", 22, OLIVE, 5)
f.ex("B1", "穴埋め選択", "B", "torrone = トローネ",
     "— Cerco il ___ di Cremona. (A. biglietto · B. torrone)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "mandorle = アーモンド",
     "— È fatto di ___ e miele. (A. mandorle · B. patate)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "B", "quanto costa? = いくらですか",
     "— Quanto ___ tutto? (A. dorme · B. costa)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "pagare con carta = カードで払う",
     "— Pago con ___. (A. carta · B. cosplay)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "B", "トローネ祭りは11月22日まで",
     "— La festa dura fino al ___. (A. 6 dicembre · B. 22 novembre)", size=15.5, gap=1)
f.head("H · SCRIVI TU", 22, OLIVE, 5)
MODELO = ("Mercoledì 11 novembre metto la sciarpa e vado in cantina: è San Martino e il vino nuovo si assaggia. "
          "A scuola parliamo della leggenda del mantello diviso e dell'estate di tre giorni. "
          "Sabato assaggio il torrone con la mia famiglia: preferisco quello di Cremona, con le mandorle e il miele. "
          "Giovedì sera guardiamo Italia–Francia in televisione, alle 20.45. "
          "Domenica, poi, il Belgio: due notti azzurre in una settimana. "
          "San Martino è arrivato, ma la settimana è dolce: vino nuovo, castagne e calcio, come nel giornale. "
          "Lunedì prossimo racconto tutto alla classe, con le parole nuove di San Martino.")
NWORDS = len(MODELO.split())
f.expl(f"作文問題（答えは一つではない）；模範文（{NWORDS} 語）は下です。")
f.ex("B1", "作文", "（自由作文、模範文は以下）", f"模範文は本ページ H 欄（{NWORDS} 語）",
     "«La tua settimana di San Martino» Scrivi 80–100 parole: San Martino, cosa assaggi, un evento o una festa del tuo weekend.", instr="作文", size=15.5, gap=1)
f.para("Testo modello: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RISPOSTE =================
p.hline(MX, RIGHT, 1344, GOLD, 2)
p.text(MX, 1382, "RISPOSTE · 全解答と解説（1–8ページ）", 25, "sans", True, OLIVE)
p.text(RIGHT, 1382, "各問に日本語の短い解説つき · ✓ は模範文のある問題", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1408, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— {pg} ページ —", 14, "sans", True, OLIVE, lh=1.14, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "作文":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13, lh=1.14, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-valutazione.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("model words:", NWORDS)
