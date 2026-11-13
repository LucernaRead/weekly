# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-it-ja/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · VALUTAZIONE E RISPOSTE =================
CURPAGE[0] = 8
p = BSPage4()
p.band("VALUTAZIONE E RISPOSTE　演習と答え", "La Lucerna", "8ページ　La grande prova della settimana + tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1332, tag="P8-ex")
f.head("A　COMPLETA LA CRONACA", 22, OLIVE, 5)
f.ex("B1", "穴埋め選択", "B", "ラツィオ = Lazio",
     "La prima in classifica è la ___. (A. Roma · B. Lazio)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "第11節は計24ゴール",
     "L'11ª giornata ha portato ___ gol. (A. 24 · B. 31)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "アタランタ対インテルはベルガモで",
     "Atalanta–Inter si gioca a ___. (A. Bergamo · B. Torino)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "トッローネ祭は日曜日に閉幕",
     "La Festa del Torrone chiude domenica a ___. (A. Cremona · B. Perugia)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "B", "チョコレート祭はペルージャで",
     "Eurochocolate chiude a ___. (A. Cremona · B. Perugia)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "B", "聖母健康祭は11月21日",
     "La Madonna della Salute si celebra il ___ novembre. (A. 20 · B. 21)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "ブックシティは11月23日に開幕",
     "BookCity apre lunedì ___. (A. 23 novembre · B. 22 novembre)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "B", "トリノ映画祭は11月24日に開幕",
     "Il Torino Film Festival apre... A. il 20 novembre · B. il 24 novembre", size=15.5, gap=1)
f.head("B　DOMANDE GENERALI", 22, OLIVE, 5)
f.ex("A2", "選択問題", "B", "ラツィオが29点で首位",
     "La prima in classifica ha... A. 28 punti · B. 29 punti · C. 27 punti", size=15.5, gap=1)
f.ex("A2", "選択問題", "B", "インテルがコモに2–0で勝利",
     "L'Inter vince 2–0 con... A. la Roma · B. il Como · C. il Milan", size=15.5, gap=1)
f.ex("A2", "選択問題", "A", "チョコレート祭は第32回",
     "Eurochocolate è alla sua... A. 32ª edizione · B. 29ª edizione · C. 15ª edizione", size=15.5, gap=1)
f.ex("B1", "選択問題", "C", "ウディネーゼは5点で最下位",
     "L'ultima in classifica è... A. il Monza · B. il Venezia · C. l'Udinese", size=15.5, gap=1)
f.ex("B1", "選択問題", "C", "アルバのトリュフ祭は12月6日まで",
     "La Fiera del Tartufo Bianco di Alba chiude... A. il 22 novembre · B. l'8 novembre · C. il 6 dicembre", size=15.5, gap=1)
f.ex("B1", "選択問題", "A", "修正案の締め切りは11月17日18時",
     "Il termine per gli emendamenti è... A. il 17 novembre · B. il 9 novembre · C. il 31 dicembre", size=15.5, gap=1)
f.ex("B2", "選択問題", "B", "政府の提案はまだ法律ではない",
     "«Il governo propone»... A. è già legge · B. non è ancora legge · C. è un errore", size=15.5, gap=1)
f.ex("B1", "選択問題", "B", "聖母健康祭は1630年の誓いに由来する",
     "La festa della Salute nasce da un voto del... A. 1687 · B. 1630 · C. 1898", size=15.5, gap=1)
f.head("C　LEGGI E RISPONDI", 22, OLIVE, 5)
f.para("Giulia vive a Venezia: sabato 21 novembre attraversa il ponte votivo e porta una candela in basilica. Paolo vive a Cremona: domenica 22 novembre guarda il corteo del Torrone e assaggia il dolce con la sua famiglia. Domenica sera, Giulia e Paolo guardano Atalanta–Inter: è la festa del torrone, ma il calcio non si ferma.", 16.5, lh=1.3, split=False)
f.ex("A2", "選択問題", "B", "ジュリアは土曜に聖母健康祭へ行く",
     "Chi va alla Madonna della Salute? A. Paolo · B. Giulia · C. i due", size=15.5, gap=1)
f.ex("A2", "選択問題", "A", "パオロは日曜にトッローネのパレードを見る",
     "Paolo, domenica, guarda... A. il corteo del Torrone · B. il ponte votivo · C. lo stadio", size=15.5, gap=1)
f.ex("A2", "選択問題", "B", "ろうそくを持って行くのはジュリア",
     "La candela è portata da... A. Paolo · B. Giulia · C. nessuno", size=15.5, gap=1)
f.ex("A2", "選択問題", "A", "タイトルは二つの都市、二つの祭りを表す",
     "Il titolo migliore è... A. «Due città, due feste» · B. «La manovra» · C. «Il meteo»", size=15.5, gap=1)
f.head("D　COSTRUISCI LE FRASI", 22, OLIVE, 5)
f.ex("A2", "文を作りなさい", "Domenica è il 22 novembre.", "時間のことばが先",
     "domenica / è / il 22 novembre → ___", instr="文を作りなさい", size=15.5, gap=1)
f.ex("B1", "文を作りなさい", "Eurochocolate chiude a Perugia il 22 novembre.", "主語 + 動詞 + 場所 + 日付",
     "Eurochocolate / chiude / a Perugia / il 22 novembre → ___", instr="文を作りなさい", size=15.5, gap=1)
f.ex("B1", "文を作りなさい", "A che ora gioca la Lazio?", "疑問句は文頭に",
     "a che ora / gioca / la Lazio / ? → ___", instr="文を作りなさい", size=15.5, gap=1)
f.ex("B1", "文を作りなさい", "Il torrone si assaggia a Cremona.", "主語 + 動詞 + 場所",
     "il torrone / si assaggia / a Cremona → ___", instr="文を作りなさい", size=15.5, gap=1)
f.head("E　TRADUCI", 22, OLIVE, 5)
f.ex("A2", "翻訳", "聖母健康祭では、人々は奉納の橋を渡ります。", "原文と比べなさい",
     "Per la Madonna della Salute si attraversa il ponte votivo. → ___", instr="日本語に訳しなさい", size=15.5, gap=1)
f.ex("B1", "翻訳", "日曜の夜、アタランタがインテルと対戦します。", "si gioca = 試合がある",
     "Domenica sera si gioca Atalanta–Inter. → ___", instr="日本語に訳しなさい", size=15.5, gap=1)
f.ex("B1", "翻訳", "土曜、ラツィオはホームでレッチェと対戦します。", "in casa = ホームで",
     "Sabato la Lazio gioca in casa con il Lecce. → ___", instr="日本語に訳しなさい", size=15.5, gap=1)
f.ex("B2", "翻訳", "Ogni cifra deve essere chiara.", "dovere = ～しなければならない",
     "すべての数字がはっきりしていなければなりません。→ ___", instr="イタリア語に訳しなさい", size=15.5, gap=1)
f.head("F　LE PAROLE DELLA MANOVRA", 22, OLIVE, 5)
f.match_set("B2", "語彙の組み合わせ",
            ["la manovra", "il deficit", "la copertura", "lo scaglione"],
            ["un livello di reddito del sistema fiscale",
             "i soldi che pagano una misura",
             "la differenza tra spese ed entrate",
             "la legge di bilancio, il documento dello Stato"],
            ["d", "c", "b", "a"],
            ["manovra = 予算案 d", "deficit = 赤字 c", "copertura = 財源 b", "scaglione = 税率区分 a"],
            instr="単語と意味を合わせなさい")
f.head("G　DIALOGO ALLA SAGRA", 22, OLIVE, 5)
f.ex("B1", "穴埋め選択", "B", "torrone = ヌガー",
     "— Cerco il ___ di Cremona. (A. biglietto · B. torrone)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "mandorle = アーモンド",
     "— È fatto di ___ e miele. (A. mandorle · B. patate)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "B", "quanto costa? = いくらですか",
     "— Quanto ___ tutto? (A. dorme · B. costa)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "pagare con carta = カードで払う",
     "— Pago con ___. (A. carta · B. cosplay)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "B", "トッローネ祭は11月22日まで続く",
     "— La festa dura fino al ___. (A. 6 dicembre · B. 22 novembre)", size=15.5, gap=1)
f.head("H　SCRIVI TU", 22, OLIVE, 5)
MODELO = ("Domenica 22 novembre metto la sciarpa e vado a Cremona: è l'ultimo giorno della Festa del Torrone e il corteo passa in piazza del Comune. "
          "Assaggio il torrone con la mia famiglia: preferisco quello con le mandorle e il miele, a forma di Torrazzo. "
          "La sera guardiamo Atalanta–Inter, alle 20.45, e la Lazio è ancora prima con 29 punti. "
          "Sabato, a Venezia, c'era la Madonna della Salute: il ponte votivo e le candele accese. "
          "La settimana è dolce e azzurra: torrone, cioccolato e calcio, come nel giornale. "
          "Lunedì prossimo racconto tutto alla classe, con le parole nuove della settimana.")
NWORDS = len(MODELO.split())
f.bridge(f"作文課題（正解は一つではありません）；模範文（{NWORDS}語）下記。")
f.ex("B1", "作文", "（自由課題、模範文は下）", f"模範文は本ページ H 欄（{NWORDS} 語）",
     "«La tua domenica del 22 novembre» Scrivi 80–100 parole: una festa, una partita, cosa assaggi.", instr="書く", size=15.5, gap=1)
f.para("Testo modello: " + MODELO, 16, lh=1.3, split=False)
f.end_report()
print("P8 exercises flow ends col", f.ci, "y=", f.y)
# ---- Vermeer image under the exercises flow (measured slot, col 3) ----
if f.y + 10 + 170 + 70 <= 1332:
    image(p, "lettera.jpg", COLX[3], f.y + 10, CW, 170)
    caption(p, COLX[3], f.y + 180, CW, "Una donna scrive una lettera: la scrittura è l'ultimo esercizio della settimana.",
            "Foto: Johannes Vermeer — Wikimedia Commons, dominio pubblico")
    print("P8 lettera image placed at y=", f.y + 10)
else:
    print("  !! P8 LETTERA NOSPACE: flow ends y=", f.y)

# ================= RISPOSTE =================
p.hline(MX, RIGHT, 1344, OLIVE, 2)
p.text(MX, 1382, "RISPOSTE　解答 — ページ別に整理：番号で探しなさい", 25, "sans", True, OLIVE)
p.text(RIGHT, 1382, "各解答に日本語の一行解説付き　✓ = 模範文の課題", 19.5, "sans", False, GREY, anchor="end")
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
