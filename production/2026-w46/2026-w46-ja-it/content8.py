# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-ja-it/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · テストと答え =================
CURPAGE[0] = 8
p = BSPage4()
p.band("テストと答え · Test e risposte", "Lucerna", "第 8 面 · 週の大きなテスト + 全ての答え")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · 週のクロニクル", 21, OLIVE, 5)
f.ex("B1", "completamento", "A", "La Settimana della Lettura finisce il 9 novembre (lunedì)",
     "読書週間は、11月9日（___）で終わります。(A. 月よう日 · B. 日よう日)", size=13.8, gap=0)
f.ex("B1", "completamento", "A", "Il giorno dei Pocky è l'11 novembre (mercoledì)",
     "ポッキーの日は、11月11日（___）です。(A. 水よう日 · B. 金よう日)", size=13.8, gap=0)
f.ex("B1", "completamento", "A", "La gara 3 delle Japan Series è stata il 27 ottobre (martedì)",
     "日本シリーズの第3戦は、10月27日（___）でした。(A. 火よう日 · B. 水よう日)", size=13.8, gap=0)
f.ex("B1", "completamento", "A", "Gara 4: SoftBank ha vinto 4-2",
     "第4戦は、ソフトバンクが ___ 対2で勝ちました。(A. 4 · B. 2)", size=13.8, gap=0)
f.ex("B1", "completamento", "B", "Shichi-Go-San si concentra il 15 novembre (domenica)",
     "七五三の中心の日は、11月 ___ 日（日）です。(A. 9 · B. 15)", size=13.8, gap=0)
f.ex("B1", "completamento", "A", "Le foglie del monte Takao culminano dal 13 novembre (venerdì) circa",
     "高尾山の見頃は、11月 ___ 日ごろからです。(A. 13 · B. 23)", size=13.8, gap=0)
f.ex("B1", "completamento", "A", "Il giorno dei Pocky è iniziato nel 1999",
     "『ポッキー＆プリッツの日』は、___ 年に始まりました。(A. 1999 · B. 1989)", size=13.8, gap=0)
f.ex("B1", "completamento", "A", "Il Ni-no-tori di Tori-no-ichi è il 19 novembre (giovedì)",
     "二の酉は、11月 ___ 日です。(A. 19 · B. 7)", size=13.8, gap=0)
f.head("B · 一般問題", 21, OLIVE, 5)
f.ex("A2", "scelta multipla", "A", "Shichi-Go-San celebra i bambini di 3, 5 e 7 anni",
     "七五三は、だれのお祝いですか。 A. 3歳・5歳・7歳の子ども · B. 大人 · C. お年寄り", size=13.8, gap=0)
f.ex("B1", "scelta multipla", "B", "Le visite culminano a inizio novembre (26 %), dice l'indagine",
     "調査では、お参りがいちばん多いのはいつですか。 A. 11月15日 · B. 11月上旬 · C. 12月", size=13.8, gap=0)
f.ex("B1", "scelta multipla", "A", "L'MVP della serie è Masaki Tomoya",
     "日本シリーズのMVPはだれですか。 A. 正木選手 · B. 山川選手 · C. 筒香選手", size=13.8, gap=0)
f.ex("B1", "scelta multipla", "A", "Il 13º titolo di SoftBank",
     "ソフトバンクは、何度目の日本一ですか。 A. 13度目 · B. 3度目 · C. 1度目", size=13.8, gap=0)
f.ex("A2", "scelta multipla", "A", "Chitose-ame è una lunga caramella rossa e bianca",
     "千歳飴は、どんな飴ですか。 A. 赤と白の長い飴 · B. 黒い丸い飴 · C. 緑の四角い飴", size=13.8, gap=0)
f.ex("B2", "scelta multipla", "A", "Le date previste segnano l'inizio della stagione migliore",
     "紅葉の予報の日にちは、何ですか。 A. 見頃が始まる目安 · B. いちばん美しい日 · C. 落葉の日", size=13.8, gap=0)
f.ex("B2", "scelta multipla", "A", "Il 74 % delle famiglie fa foto in studio, dice l'indagine",
     "写真館で撮る家庭は何%ですか。 A. 74% · B. 71% · C. 26%", size=13.8, gap=0)
f.ex("A2", "scelta multipla", "A", "Lo slogan è 「静かだけど、冒険中。」",
     "読書週間のスローガンは？ A. 静かだけど、冒険中。 · B. 本の秋 · C. 紅葉の秋", size=13.8, gap=0)
f.head("C · 読んで答えましょう", 21, OLIVE, 5)
f.para("ユウは中学生です。今週の月よう日は、読書週間の最後の日です。ユウは図書館で借りた本を読みます。水よう日には、友達とポッキーを分けます。金よう日には、高尾山へ紅葉を見に行くつもりです。日よう日には、妹の七五三で神社へ行きます。", 15, lh=1.3, split=False)
f.ex("A2", "scelta multipla", "B", "Il lunedì legge un libro della biblioteca",
     "ユウは月よう日に何をしますか。 A. 神社へ行く · B. 図書館で借りた本を読む · C. ポッキーを買う", size=13.8, gap=0)
f.ex("A2", "scelta multipla", "B", "Il mercoledì condivide i Pocky con gli amici",
     "水よう日に何をしますか。 A. 高尾山へ行く · B. 友達とポッキーを分ける · C. 神社へ行く", size=13.8, gap=0)
f.ex("A2", "scelta multipla", "A", "Il venerdì va sul monte Takao per le foglie",
     "金よう日にどこへ行きますか。 A. 高尾山 · B. 神社 · C. 図書館", size=13.8, gap=0)
f.ex("B1", "scelta multipla", "B", "La domenica va al santuario per lo Shichi-Go-San della sorella",
     "日よう日にどこへ行きますか。 A. 高尾山 · B. 神社 · C. 浅草", size=13.8, gap=0)
f.head("D · 文を作りましょう", 21, OLIVE, 5)
f.ex("A2", "costruzione di frasi", "私は水よう日に友達とポッキーを分けます。", "soggetto + tempo + oggetto + verbo",
     "私は / 水よう日に / 友達とポッキーを分けます → ___", instr="Costruisci una frase", size=13.8, gap=0)
f.ex("A2", "costruzione di frasi", "七五三は子どものお祝いです。", "七五三 = una festa per bambini",
     "七五三は / 子どもの / お祝いです → ___", instr="Costruisci una frase", size=13.8, gap=0)
f.ex("B1", "costruzione di frasi", "神社で千歳飴をもらいます。", "Usa 「で」 per il luogo",
     "神社で / 千歳飴を / もらいます → ___", instr="Costruisci una frase", size=13.8, gap=0)
f.ex("B1", "costruzione di frasi", "ソフトバンクは4連勝で日本一になりました。", "Quattro vittorie di fila hanno portato il titolo",
     "ソフトバンクは / 4連勝で / 日本一になりました → ___", instr="Costruisci una frase", size=13.8, gap=0)
f.head("E · 翻訳しましょう", 21, OLIVE, 5)
f.ex("A2", "traduzione", "Shichi-Go-San è il 15 novembre.", "Vedi pagina 3",
     "七五三は11月15日です。 → ___", instr="Traduci", size=13.8, gap=0)
f.ex("B1", "traduzione", "Il giorno dei Pocky è iniziato nel 1999.", "Vedi pagina 2",
     "『ポッキー＆プリッツの日』は1999年に始まりました。 → ___", instr="Traduci", size=13.8, gap=0)
f.ex("B1", "traduzione", "読書週間は10月27日から始まります。", "Vedi pagina 7",
     "La Settimana della Lettura inizia il 27 ottobre. → ___", instr="Traduci", size=13.8, gap=0)
f.ex("B2", "traduzione", "紅葉を見に行く人は、北から南へ、見頃を追いかけることができます。", "Vedi pagina 6 (a caccia della stagione migliore)",
     "Chi va a vedere le foglie può inseguire la stagione migliore da nord a sud. → ___", instr="Traduci", size=13.8, gap=0)
f.head("F · 今週のことば", 21, OLIVE, 5)
f.match_set("B2", "abbinamento",
            ["七五三", "千歳飴", "落葉", "見頃"],
            ["木から落ちた葉",
             "3歳・5歳・7歳の子どものお祝い",
             "紅葉がいちばん美しい時",
             "赤と白の長い飴"],
            ["b", "d", "a", "c"],
            ["七五三 = una festa per bambini di 3, 5 e 7 anni b", "千歳飴 = lunga caramella rossa e bianca d", "落葉 = foglie cadute a", "見頃 = la stagione migliore c"],
            instr="Abbina parola e senso")
f.head("G · 神社で", 21, OLIVE, 5)
f.ex("B1", "completamento", "A", "お参りします = andare a pregare",
     "— 七五三ですね。— はい、神社へ ___ ます。(A. お参りに行き · B. お参りに行か)", size=13.8, gap=0)
f.ex("B1", "completamento", "A", "撮ります = scattare una foto",
     "— 写真を ___ か。 (A. 撮ります · B. 撮った)", size=13.8, gap=0)
f.ex("B1", "completamento", "A", "Shichi-Go-San si concentra il 15 novembre (pagina 3)",
     "— 七五三はいつですか。— 11月 ___ 日です。(A. 15 · B. 9)", size=13.8, gap=0)
f.ex("B1", "completamento", "A", "千歳飴 è popolare",
     "— おすすめはありますか。— 『___ 』が人気です。(A. 千歳飴 · B. ポッキー)", size=13.8, gap=0)
f.ex("B1", "completamento", "A", "どういたしまして = prego",
     "— ありがとうございました。— ___ 。(A. どういたしまして · B. さようなら)", size=13.8, gap=0)
f.head("H · 書いてみましょう", 21, OLIVE, 5)
MODELO = ("私の11月の1週間は、本と秋の1週間です。"
          "月よう日は、読書週間の最後の日です。図書館で借りた本を読みます。"
          "水よう日は、友達とポッキーを分けます。1が4つ並ぶ日です。"
          "金よう日は、高尾山へ紅葉を見に行きます。"
          "日よう日は、妹の七五三です。神社へ行って、写真を撮ります。"
          "11月は短いですが、楽しいことが多い季節です。")
NCHARS = len(MODELO.replace(" ", ""))
f.bridge(f"Compito di scrittura (senza un'unica risposta giusta); il testo modello ({NCHARS} caratteri) è sotto.")
f.ex("B1", "scrittura", "(compito aperto — testo modello sotto)", f"Testo modello nella sezione H di questa pagina ({NCHARS} caratteri)",
     "『私の11月の1週間』について、150〜200字で書いてください。読書、七五三、紅葉の中から一つ選んでください。", instr="Scrittura", size=13.8, gap=0)
f.para("例： " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= 答え =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "答え · Risposte — raggruppate per pagina; trova solo il tuo numero", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Una breve nota in italiano con ogni risposta · ✓ = l'esercizio con testo modello", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PAGINA {pg} —", 12.9, "sans", True, OLIVE, lh=1.13, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "scrittura":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 12.9, lh=1.13, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-tesuto.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("by type", dict(Counter(e["type"] for e in REG)))
print("model chars:", NCHARS)
