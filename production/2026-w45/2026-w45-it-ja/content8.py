# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · VALUTAZIONE E RISPOSTE =================
CURPAGE[0] = 8
p = BSPage4()
p.band("VALUTAZIONE E RISPOSTE　演習と答え", "La Lucerna", "8ページ　La grande prova della settimana + tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1332, tag="P8-ex")
f.head("A　COMPLETA LA CRONACA", 22, OLIVE, 5)
f.ex("B1", "穴埋め選択", "B", "primo freddo = 初寒",
     "Lunedì 2 novembre arriva il primo ___ della stagione. (A. caldo · B. freddo)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "死者の日は11月2日",
     "Il 2 novembre è la Commemorazione dei ___. (A. defunti · B. santi)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "文化フォーラムはミラノで開幕",
     "Il Forum Cultura apre martedì a ___. (A. Milano · B. Cremona)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "パネットーネ決勝は土曜と日曜",
     "La finale del Panettone è sabato e ___ a Milano. (A. domenica · B. lunedì)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "B", "トローネ祭りはクレモナで",
     "La Festa del Torrone apre a ___. (A. Milano · B. Cremona)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "B", "セリエA第11節は日曜に閉幕：chiude",
     "L'undicesima giornata ___ domenica 8 novembre. (A. apre · B. chiude)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "フィオレンティーナ対ユヴェントスは日曜の夜",
     "Fiorentina–Juventus si gioca domenica ___. (A. sera · B. mattina)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "B", "民族映画祭はフィレンツェで",
     "Il Festival dei Popoli è a ___. (A. Milano · B. Firenze)", size=15.5, gap=1)
f.head("B　DOMANDE GENERALI", 22, OLIVE, 5)
f.ex("A2", "単一選択", "B", "初雪は1300～1500メートル付近で",
     "La prima neve leggera può cadere intorno ai... A. 500 m · B. 1.300–1.500 m · C. 3.000 m", size=15.5, gap=1)
f.ex("A2", "単一選択", "B", "死者の日の花は菊",
     "Il fiore del 2 novembre è... A. la rosa · B. il crisantemo · C. il tulipano", size=15.5, gap=1)
f.ex("A2", "単一選択", "A", "パネットーネ決勝には19か国の菓子職人",
     "Alla finale del Panettone partecipano pasticceri da... A. 19 paesi · B. 5 paesi · C. 50 paesi", size=15.5, gap=1)
f.ex("B1", "単一選択", "B", "文化フォーラムは50超の催し",
     "Il Forum Cultura ha... A. 5 eventi · B. più di 50 eventi · C. 19 eventi", size=15.5, gap=1)
f.ex("B1", "単一選択", "C", "アルバのトリュフ祭りは12月6日まで",
     "La Fiera del Tartufo Bianco di Alba chiude... A. il 22 novembre · B. l'8 novembre · C. il 6 dicembre", size=15.5, gap=1)
f.ex("B1", "単一選択", "A", "DPBは10月15日に送付",
     "Il DPB è partito per Bruxelles... A. il 15 ottobre · B. il 19 ottobre · C. il 28 ottobre", size=15.5, gap=1)
f.ex("B2", "単一選択", "B", "確率は確実性ではない",
     "Una probabilità alta... A. è una certezza · B. non è una certezza · C. è un errore", size=15.5, gap=1)
f.ex("B1", "単一選択", "B", "ルッカ・コミックスは11月1日に閉幕",
     "Lucca Comics si è chiusa... A. il 28 ottobre · B. il 1° novembre · C. l'8 novembre", size=15.5, gap=1)
f.head("C　LEGGI E RISPONDI", 22, OLIVE, 5)
f.para("Giulia vive a Milano: sabato 7 novembre va alla finale del Panettone e assaggia il panettone tradizionale. Paolo vive a Cremona: sabato 7 novembre va alla Festa del Torrone. Domenica, Giulia e Paolo guardano la Serie A: fa freddo, ma il calcio non si ferma.", 16.5, lh=1.3, split=False)
f.ex("A2", "単一選択", "B", "Giuliaはミラノのパネットーネ決勝へ",
     "Chi va alla finale del Panettone? A. Paolo · B. Giulia · C. i due", size=15.5, gap=1)
f.ex("A2", "単一選択", "A", "Paoloは土曜にトローネ祭りへ",
     "Paolo, sabato, va... A. alla Festa del Torrone · B. a Milano · C. allo stadio", size=15.5, gap=1)
f.ex("A2", "単一選択", "B", "伝統的なパネットーネはGiuliaが試食したもの",
     "Il panettone tradizionale è assaggiato da... A. Paolo · B. Giulia · C. nessuno", size=15.5, gap=1)
f.ex("A2", "単一選択", "A", "タイトルは2都市と2つの祭りをまとめる",
     "Il titolo migliore è... A. «Due città, due dolci» · B. «La manovra» · C. «Il meteo»", size=15.5, gap=1)
f.head("D　COSTRUISCI LE FRASI", 22, OLIVE, 5)
f.ex("A2", "文を作る", "Lunedì arriva il primo freddo.", "時間の語が前",
     "lunedì / arriva / il primo freddo → ___", instr="文を作る", size=15.5, gap=1)
f.ex("B1", "文を作る", "La finale è a Milano il 7 novembre.", "主語 + essere + 場所 + 日付",
     "la finale / è a Milano / il 7 novembre → ___", instr="文を作る", size=15.5, gap=1)
f.ex("B1", "文を作る", "A che ora apre il Forum Cultura?", "疑問の語句が文頭",
     "a che ora / apre / il Forum Cultura / ? → ___", instr="文を作る", size=15.5, gap=1)
f.ex("B1", "文を作る", "Il freddo arriva lunedì.", "主語 + 動詞 + 時間",
     "il freddo / arriva / lunedì → ___", instr="文を作る", size=15.5, gap=1)
f.head("E　TRADUCI", 22, OLIVE, 5)
f.ex("A2", "翻译", "月曜日に最初の寒さがやってきます。", "原文と照らしましょう。",
     "Lunedì arriva il primo freddo. → ___", instr="日本語に翻訳", size=15.5, gap=1)
f.ex("B1", "翻译", "観客は無料で試食できます。", "assaggiare gratis = 無料で試食",
     "Il pubblico può assaggiare gratis. → ___", instr="日本語に翻訳", size=15.5, gap=1)
f.ex("B1", "翻译", "日曜の夜、フィオレンティーナ対ユヴェントス。", "si gioca = 試合が行われる",
     "Domenica sera si gioca Fiorentina–Juventus. → ___", instr="日本語に翻訳", size=15.5, gap=1)
f.ex("B2", "翻译", "Ogni previsione deve essere chiara.", "dovere = ～しなければならない",
     "すべての予報は明確でなければならない。→ ___", instr="イタリア語に翻訳", size=15.5, gap=1)
f.head("F　LE PAROLE DEL METEO", 22, OLIVE, 5)
f.match_set("B2", "単語の組み合わせ",
            ["la probabilità", "la media", "il bollettino", "il modello"],
            ["il valore medio, tra tanti valori",
             "il documento con le previsioni più recenti",
             "il calcolo che prevede il tempo, come l'ECMWF",
             "quanto è possibile che una cosa succeda"],
            ["d", "a", "b", "c"],
            ["probabilità = 可能性、d", "media = 平均値、a", "bollettino = 予報公報、b", "modello = 予報モデル、c"],
            instr="語と意味を結ぶ")
f.head("G　DIALOGO ALLA SAGRA", 22, OLIVE, 5)
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
f.head("H　SCRIVI TU", 22, OLIVE, 5)
MODELO = ("Lunedì 2 novembre metto il cappotto e la sciarpa: arriva il primo freddo e la mattina è pungente. "
          "A scuola parliamo del Forum Cultura di Milano e del Festival dei Popoli di Firenze. "
          "Sabato assaggio il panettone con la mia famiglia: preferisco quello tradizionale, con i canditi. "
          "Domenica sera guardiamo Fiorentina–Juventus in televisione. "
          "Il freddo è arrivato, ma la settimana è dolce: cultura, dolci e calcio, come nel giornale. "
          "Lunedì prossimo racconto tutto alla classe, con le parole nuove del freddo.")
NWORDS = len(MODELO.split())
f.expl(f"作文問題（答えは一つではない）；模範文（{NWORDS} 語）は下です。")
f.ex("B1", "作文", "（自由作文、模範文は以下）", f"模範文は本ページ H 欄（{NWORDS} 語）",
     "«La tua settimana del primo freddo» Scrivi 80–100 parole: il freddo, cosa metti, un evento o una festa del tuo weekend.", instr="作文", size=15.5, gap=1)
f.para("Testo modello: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RISPOSTE =================
p.hline(MX, RIGHT, 1344, OLIVE, 2)
p.text(MX, 1382, "RISPOSTE　全解答と解説（1–8ページ）", 25, "sans", True, OLIVE)
p.text(RIGHT, 1382, "各問に日本語の短い解説つき　✓ は模範文のある問題", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1408, 2560, tag="P8-keys")
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
