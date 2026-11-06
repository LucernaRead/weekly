# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ja-it/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · テストと答え =================
CURPAGE[0] = 8
p = BSPage4()
p.band("テストと答え · Test e risposte", "Lucerna", "第 8 面 · 週の大きなテスト + 全ての答え")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · 週のクロニクル", 21, OLIVE, 5)
f.ex("B1", "cloze", "A", "La Festa della Cultura è il 3 novembre (martedì)",
     "文化の日は、11月3日（___）です。(A. 火よう日 · B. 土よう日)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "La Settimana della Lettura dura fino al 9 novembre",
     "読書週間は、11月 ___ 日までです。(A. 9 · B. 8)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "Gara 1 delle Japan Series era il 24 ottobre (sabato)",
     "日本シリーズの第1戦は、10月24日（___）でした。(A. 土よう日 · B. 日よう日)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "Gara 2: SoftBank ha vinto 4–3",
     "第2戦は、ソフトバンクが ___ 対3で勝ちました。(A. 4 · B. 3)", size=13.8, gap=0)
f.ex("B1", "cloze", "B", "Halloween era il 31 ottobre (sabato)",
     "ハロウィンは、10月 ___ 日（土）でした。(A. 30 · B. 31)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "立冬 cade il 7 novembre (sabato)",
     "立冬は、11月 ___ 日（土）です。(A. 7 · B. 3)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "Le cene con nabe sono 1,5 volte quelle dello scorso anno",
     "鍋の食卓は、去年の ___ 倍になりました。(A. 1.5 · B. 2)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "Le luminarie di Kobe cominciano il 7",
     "神戸のライトアップは、___ 日から始まります。(A. 7 · B. 3)", size=13.8, gap=0)
f.head("B · 一般問題", 21, OLIVE, 5)
f.ex("A2", "scelta multipla", "A", "L'evento di Suginami è un'orchestra di famiglia",
     "杉並区のイベントは何ですか。 A. 家族オーケストラ · B. 伝統工芸展 · C. 野球の試合", size=13.8, gap=0)
f.ex("B1", "scelta multipla", "B", "La mostra dura fino all'8 novembre",
     "伝統工芸展はいつまでですか。 A. 11月3日 · B. 11月8日 · C. 11月9日", size=13.8, gap=0)
f.ex("B1", "scelta multipla", "A", "Pubblico di gara 1: 33.388",
     "第1戦の観客は何人でしたか。 A. 33,388人 · B. 33,432人 · C. 33,000人", size=13.8, gap=0)
f.ex("B1", "scelta multipla", "A", "Percentuale di titolo per chi parte 2–0: 73%",
     "2連勝で始めたチームの優勝率は？ A. 73% · B. 24% · C. 100%", size=13.8, gap=0)
f.ex("A2", "scelta multipla", "A", "Buttare rifiuti costa una multa di 2.000 yen",
     "渋谷でゴミを捨てた時の罰金は？ A. 2,000円 · B. 200円 · C. 20,000円", size=13.8, gap=0)
f.ex("B2", "scelta multipla", "A", "La previsione della JMA: più caldo della media",
     "気象庁の予報では、気温はどうなりますか。 A. 平年より高い · B. 平年より低い · C. 平年と同じ", size=13.8, gap=0)
f.ex("B2", "scelta multipla", "A", "Ricerche di viaggi in Kyushu quasi doppie",
     "九州の旅の検索は、去年と比べてどうなりましたか。 A. ほぼ2倍 · B. 半分 · C. 同じ", size=13.8, gap=0)
f.ex("A2", "scelta multipla", "A", "Lo slogan è 「静かだけど、冒険中。」",
     "読書週間のスローガンは？ A. 静かだけど、冒険中。 · B. 本の秋 · C. 紅葉の秋", size=13.8, gap=0)
f.head("C · 読んで答えましょう", 21, OLIVE, 5)
f.para("ミカは高校生です。今週の火よう日は文化の日です。ミカは家族と金沢へ行くつもりです。伝統工芸展とライトアップを見たいです。土よう日には、友達と神戸へ紅葉を見に行くつもりです。読書週間には、図書館で本を2冊借りたいと思っています。", 15, lh=1.3, split=False)
f.ex("A2", "scelta multipla", "B", "Martedì Mika va a Kanazawa con la famiglia",
     "ミカは火よう日に何をしますか。 A. 神戸へ行く · B. 家族と金沢へ行く · C. 図書館へ行く", size=13.8, gap=0)
f.ex("A2", "scelta multipla", "B", "A Kanazawa vede la mostra di artigianato e le luminarie",
     "金沢で何を見ますか。 A. 野球の試合 · B. 伝統工芸展とライトアップ · C. 鍋の料理", size=13.8, gap=0)
f.ex("A2", "scelta multipla", "A", "Sabato va a Kobe con gli amici",
     "土よう日にどこへ行きますか。 A. 神戸 · B. 金沢 · C. 杉並区", size=13.8, gap=0)
f.ex("B1", "scelta multipla", "B", "Per la Settimana della Lettura: 2 libri in prestito",
     "読書週間に借りたい本は？ A. 3冊 · B. 2冊 · C. 9冊", size=13.8, gap=0)
f.head("D · 文を作りましょう", 21, OLIVE, 5)
f.ex("A2", "costruzione di frasi", "私は火よう日に金沢へ行きます。", "soggetto + tempo + luogo + verbo",
     "私は / 火よう日に / 金沢へ行きます → ___", instr="Costruisci la frase", size=13.8, gap=0)
f.ex("A2", "costruzione di frasi", "紅葉は今週末が見頃です。", "見頃 = il momento migliore per ammirare",
     "紅葉は / 今週末が / 見頃です → ___", instr="Costruisci la frase", size=13.8, gap=0)
f.ex("B1", "costruzione di frasi", "図書館で本を借ります。", "usa 「で」 per il luogo",
     "図書館で / 本を / 借ります → ___", instr="Costruisci la frase", size=13.8, gap=0)
f.ex("B1", "costruzione di frasi", "ソフトバンクは2連勝でスタートしました。", "partire con due vittorie di fila",
     "ソフトバンクは / 2連勝で / スタートしました → ___", instr="Costruisci la frase", size=13.8, gap=0)
f.head("E · 翻訳しましょう", 21, OLIVE, 5)
f.ex("A2", "traduzione", "La Festa della Cultura è il 3 novembre.", "Vedi pagina 3",
     "文化の日は11月3日です。 → ___", instr="Traduci", size=13.8, gap=0)
f.ex("B1", "traduzione", "Se butti i rifiuti, la multa è di 2.000 yen.", "Vedi pagina 5",
     "ゴミを捨てると、2,000円の罰金です。 → ___", instr="Traduci", size=13.8, gap=0)
f.ex("B1", "traduzione", "読書週間は10月27日から始まります。", "Vedi pagina 7",
     "La Settimana della Lettura comincia il 27 ottobre. → ___", instr="Traduci", size=13.8, gap=0)
f.ex("B2", "traduzione", "神戸の紅葉のライトアップを見に行きたいです。", "Vedi pagina 6 (le luminarie di Kobe)",
     "Vorrei andare a Kobe a vedere le luminarie delle foglie. → ___", instr="Traduci", size=13.8, gap=0)
f.head("F · 今週のことば", 21, OLIVE, 5)
f.match_set("B2", "abbinamento",
            ["見頃", "鍋", "落葉", "予算"],
            ["木から落ちた葉",
             "花や紅葉がいちばん美しい時",
             "1回の旅のお金",
             "一つの鍋で作る料理"],
            ["b", "d", "a", "c"],
            ["見頃 = momento migliore per ammirare b", "鍋 = piatto unico in pentola d", "落葉 = foglie cadute a", "予算 = budget c"],
            instr="Abbina parole e significati")
f.head("G · 図書館で", 21, OLIVE, 5)
f.ex("B1", "cloze", "A", "見せてください = per favore, mostri",
     "— 本を借りたいです。— はい、カードを ___ ください。(A. 見せて · B. 見て)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "借りられます = prendere in prestito (potenziale)",
     "— 2冊、___ か。 (A. 借りられます · B. 借りますた)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "Settimana della Lettura fino al 9 novembre (pagina 7)",
     "— 読書週間はいつまでですか。— 11月 ___ 日までです。(A. 9 · B. 3)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "「紅葉の本」 è popolare",
     "— おすすめはありますか。— 『___ 』の本が人気です。(A. 紅葉 · B. 野球)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "どういたしまして = prego, di niente",
     "— ありがとうございました。— ___ 。(A. どういたしまして · B. さようなら)", size=13.8, gap=0)
f.head("H · 書いてみましょう", 21, OLIVE, 5)
MODELO = ("私の11月の週末は、文化と紅葉の週末です。"
          "火よう日は、家族と金沢へ行きます。伝統工芸展とライトアップを見たいです。"
          "土よう日は、友達と神戸へ紅葉を見に行きます。夜は、ライトアップを見ます。"
          "日よう日は、図書館で借りた本を読みます。"
          "読書週間も終わりますから、静かな場所で大きな冒険をしたいです。"
          "11月は短いですが、楽しいことが多い季節です。")
NCHARS = len(MODELO.replace(" ", ""))
f.bridge(f"Compito di scrittura (senza un'unica risposta esatta); il testo modello ({NCHARS} caratteri) è qui sotto.")
f.ex("B1", "scrittura", "(compito aperto — testo modello qui sotto)", f"Testo modello nella sezione H ({NCHARS} caratteri)",
     "『私の11月の週末』について、150〜200字で書いてください。文化の日、紅葉、読書の中から一つ選んでください。", instr="Scrittura", size=13.8, gap=0)
f.para("例： " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= 答え =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "答え · Risposte — raggruppate per pagina: basta cercare il numero", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Una breve nota in italiano per ogni risposta · ✓ = la domanda con il testo modello", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PAGINA {pg} —", 13.3, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "scrittura":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.3, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-tesuto.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("by type", dict(Counter(e["type"] for e in REG)))
print("model chars:", NCHARS)
