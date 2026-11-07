# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-ja-de/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · テストと答え =================
CURPAGE[0] = 8
p = BSPage4()
p.band("テストと答え · Test und Antworten", "Lucerna", "第 8 面 · 週の大きなテスト + 全ての答え")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · 週のクロニクル", 21, OLIVE, 5)
f.ex("B1", "Lückentext", "A", "Spiel 1 ist am Sa, 24. Oktober",
     "日本シリーズの第1戦は、10月24日（___）です。(A. 土よう日 · B. 日よう日)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Auch die Para-Asienspiele enden am 24.",
     "アジアパラ競技大会の最終日も、___ 日です。(A. 24 · B. 25)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Das Jidai Matsuri war am Do, 22. Oktober",
     "時代祭は、10月 ___ 日（木）でした。(A. 22 · B. 24)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "B", "Allgemeiner Verkauf: der 22., 12 Uhr",
     "日本シリーズのチケットの一般発売は、___ 日12時でした。(A. 20 · B. 22)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Die Irohazaka ist ab Fr, dem 23., am schönsten",
     "日光のいろは坂の見頃は、___ 日（金）からです。(A. 23 · B. 15)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "B", "Geraldons Gesamtpunktzahl: 1.342",
     "ジェラードンの合計点は、___ 点でした。(A. 671 · B. 1,342)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Die Lesewoche beginnt am Di, 27. Oktober",
     "読書週間は、10月 ___ 日（火）からです。(A. 27 · B. 31)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "B", "Halloween ist am Sa, 31. Oktober",
     "ハロウィンは、10月 ___ 日（土）です。(A. 30 · B. 31)", size=13.8, gap=0)
f.head("B · 一般問題", 21, OLIVE, 5)
f.ex("A2", "Multiple Choice", "B", "45 Länder und Regionen",
     "アジアパラ競技大会に参加した国と地域は？ A. 18 · B. 45 · C. 282", size=13.8, gap=0)
f.ex("A2", "Multiple Choice", "A", "282 japanische Sportler",
     "日本の選手は何人でしたか。 A. 282人 · B. 120人 · C. 17人", size=13.8, gap=0)
f.ex("B1", "Multiple Choice", "A", "Toyos Zeit: 10 Std. 31 Min. 30 Sek.",
     "予選会で1位の東洋大学のタイムは？ A. 10時間31分30秒 · B. 1分46秒 · C. 9時間31分", size=13.8, gap=0)
f.ex("B1", "Multiple Choice", "B", "1 Min. 46 Sek. = 106 Sekunden",
     "法政大学は国士舘大学より何秒速かったですか。 A. 33秒 · B. 106秒 · C. 46秒", size=13.8, gap=0)
f.ex("A2", "Multiple Choice", "C", "Mochi-Bewertungen +168 %",
     "『餅』の口コミは何%増えましたか。 A. 82% · B. 84% · C. 168%", size=13.8, gap=0)
f.ex("B1", "Multiple Choice", "A", "Die Müllstrafe beträgt 2.000 Yen",
     "渋谷でゴミを捨てた時の罰金は？ A. 2,000円 · B. 1,000万円 · C. 900円", size=13.8, gap=0)
f.ex("A2", "Multiple Choice", "B", "Die Shosoin-Ausstellung endet am 9. November",
     "正倉院展はいつまでですか。 A. 11月1日 · B. 11月9日 · C. 10月31日", size=13.8, gap=0)
f.ex("B1", "Multiple Choice", "C", "SoftBank gewann 91 Spiele",
     "ソフトバンクのレギュラーシーズンの勝ち数は？ A. 71 · B. 49 · C. 91", size=13.8, gap=0)
f.head("C · 読んで答えましょう", 21, OLIVE, 5)
f.para("ケンは大学生です。今週の土よう日、横浜スタジアムで日本シリーズの第1戦があります。ケンはチケットを買うことができませんでしたから、テレビで応援します。日よう日は、奈良の正倉院展へ行くつもりです。来週の読書週間には、図書館で本を3冊借りたいと思っています。", 15, lh=1.3, split=False)
f.ex("A2", "Multiple Choice", "B", "Ken feuert zu Hause vor dem Fernseher an",
     "ケンは土よう日に何をしますか。 A. スタジアムへ行く · B. テレビで応援する · C. 奈良へ行く", size=13.8, gap=0)
f.ex("A2", "Multiple Choice", "B", "Er konnte kein Ticket kaufen",
     "ケンはなぜスタジアムへ行きませんか。 A. 時間がない · B. チケットが買えなかった · C. 雨だった", size=13.8, gap=0)
f.ex("A2", "Multiple Choice", "A", "Am Sonntag geht es zur Shosoin-Ausstellung",
     "日よう日の予定は？ A. 正倉院展 · B. 図書館 · C. ハロウィン", size=13.8, gap=0)
f.ex("B1", "Multiple Choice", "B", "Er möchte drei Bücher ausleihen",
     "読書週間に借りたい本は？ A. 2冊 · B. 3冊 · C. 9冊", size=13.8, gap=0)
f.head("D · 文を作りましょう", 21, OLIVE, 5)
f.ex("A2", "Satzbau", "私は土よう日に試合を見ます。", "Subjekt + Zeit + Objekt + Verb",
     "私は / 土よう日に / 試合を見ます → ___", instr="Satz bilden", size=13.8, gap=0)
f.ex("A2", "Satzbau", "紅葉は今週末が見頃です。", "見頃 = die schönste Zeit",
     "紅葉は / 今週末が / 見頃です → ___", instr="Satz bilden", size=13.8, gap=0)
f.ex("B1", "Satzbau", "図書館で本を借ります。", "Der Handlungsort steht mit 「で」",
     "図書館で / 本を / 借ります → ___", instr="Satz bilden", size=13.8, gap=0)
f.ex("B1", "Satzbau", "ジェラードンは1,342点で優勝しました。", "Punktzahl + で + 優勝しました",
     "ジェラードンは / 1,342点で / 優勝しました → ___", instr="Satz bilden", size=13.8, gap=0)
f.head("E · 翻訳しましょう", 21, OLIVE, 5)
f.ex("A2", "Übersetzen", "Der Festzug startet um 12:00 Uhr am Kyoto Gyoen.", "Siehe Seite 3",
     "行列は京都御苑を12時に出発します。 → ___", instr="Übersetzen", size=13.8, gap=0)
f.ex("B1", "Übersetzen", "Wer Müll wegwirft, zahlt 2.000 Yen Strafe.", "Siehe Seite 5",
     "ゴミを捨てると、2,000円の罰金です。 → ___", instr="Übersetzen", size=13.8, gap=0)
f.ex("B1", "Übersetzen", "読書週間は来週の火よう日から始まります。", "Siehe Seite 7",
     "Die Lesewoche beginnt nächsten Dienstag. → ___", instr="Übersetzen", size=13.8, gap=0)
f.ex("B2", "Übersetzen", "私は池袋のハロウィンのイベントに行きたいです。", "Siehe Seite 5 (das Event in Ikebukuro)",
     "Ich möchte zum Halloween-Event in Ikebukuro gehen. → ___", instr="Übersetzen", size=13.8, gap=0)
f.head("F · 今週のことば", 21, OLIVE, 5)
f.match_set("B2", "Zuordnen",
            ["見頃", "福袋", "行列", "勝率"],
            ["勝った割合（.650など）",
             "花や紅葉がいちばん美しい時",
             "中身が見えない本のセット",
             "昔の服を着た人の列"],
            ["b", "c", "d", "a"],
            ["見頃 = die schönste Zeit (b)", "福袋 = ein Set mit verborgenem Inhalt (c)", "行列 = der Festzug (d)", "勝率 = die Siegquote (a)"],
            instr="Wörter zuordnen")
f.head("G · 図書館で", 21, OLIVE, 5)
f.ex("B1", "Lückentext", "A", "見せてください = bitte zeigen Sie mir",
     "— 本を借りたいです。— はい、カードを ___ ください。(A. 見せて · B. 見て)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "借りられます = ausleihen können (Potenzialform)",
     "— 3冊、___ か。 (A. 借りられます · B. 借りますた)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Die Lesewoche beginnt am Dienstag (Seite 7)",
     "— いつ返しますか。— 読書週間が始まる ___ に返します。(A. 火よう日 · B. 土よう日)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Die Buch-Glückspakete sind sehr beliebt",
     "— おすすめはありますか。— 『本の ___ 』が人気です。(A. 福袋 · B. 行列)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "どういたしまして = gern geschehen",
     "— ありがとうございました。— ___ 。(A. どういたしまして · B. さようなら)", size=13.8, gap=0)
f.head("H · 書いてみましょう", 21, OLIVE, 5)
MODELO = ("私の秋の週末は、スポーツと読書の週末です。"
          "土よう日は、友達と家で日本シリーズを見ます。私はDeNAを応援します。"
          "試合の後は、近くの公園へ紅葉を見に行きます。"
          "日よう日は、図書館で借りた本を読みます。"
          "読書週間も始まりますから、静かな場所で大きな冒険をしたいです。"
          "秋は短いですが、楽しいことが多い季節です。")
NCHARS = len(MODELO.replace(" ", ""))
f.expl(f"Schreibaufgabe (keine einzige richtige Antwort); der Mustertext ({NCHARS} Zeichen) steht unten.")
f.ex("B1", "Schreiben", "(offene Aufgabe — Mustertext unten)", f"Mustertext in Abschnitt H auf dieser Seite ({NCHARS} Zeichen)",
     "『私の秋の週末』について、150〜200字で書いてください。スポーツ、紅葉、読書の中から一つ選んでください。", instr="Schreiben", size=13.8, gap=0)
f.para("例： " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= 答え =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "答え · Antworten — nach Seiten geordnet; einfach die Nummer suchen", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Zu jeder Antwort eine kurze Anmerkung · ✓ = die Mustertext-Aufgabe", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— Seite {pg} —", 13.3, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Schreiben":
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
