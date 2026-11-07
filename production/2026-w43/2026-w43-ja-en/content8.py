# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-ja-en/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · テストと答え =================
CURPAGE[0] = 8
p = BSPage4()
p.band("テストと答え · Test and answers", "Lucerna", "第 8 面 · 週の大きなテスト + 全ての答え")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · 週のクロニクル", 21, OLIVE, 5)
f.ex("B1", "cloze", "A", "Game 1 is Sat, October 24",
     "日本シリーズの第1戦は、10月24日（___）です。(A. 土よう日 · B. 日よう日)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "The Para Games also end on the 24th",
     "アジアパラ競技大会の最終日も、___ 日です。(A. 24 · B. 25)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "Jidai Matsuri was Thu, October 22",
     "時代祭は、10月 ___ 日（木）でした。(A. 22 · B. 24)", size=13.8, gap=0)
f.ex("B1", "cloze", "B", "General sale: the 22nd at 12:00",
     "日本シリーズのチケットの一般発売は、___ 日12時でした。(A. 20 · B. 22)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "Irohazaka peaks from Fri the 23rd",
     "日光のいろは坂の見頃は、___ 日（金）からです。(A. 23 · B. 15)", size=13.8, gap=0)
f.ex("B1", "cloze", "B", "Geraldon's total was 1,342 points",
     "ジェラードンの合計点は、___ 点でした。(A. 671 · B. 1,342)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "Reading Week starts Tue, October 27",
     "読書週間は、10月 ___ 日（火）からです。(A. 27 · B. 31)", size=13.8, gap=0)
f.ex("B1", "cloze", "B", "Halloween is Sat, October 31",
     "ハロウィンは、10月 ___ 日（土）です。(A. 30 · B. 31)", size=13.8, gap=0)
f.head("B · 一般問題", 21, OLIVE, 5)
f.ex("A2", "multiple choice", "B", "45 countries and regions",
     "アジアパラ競技大会に参加した国と地域は？ A. 18 · B. 45 · C. 282", size=13.8, gap=0)
f.ex("A2", "multiple choice", "A", "282 Japanese athletes",
     "日本の選手は何人でしたか。 A. 282人 · B. 120人 · C. 17人", size=13.8, gap=0)
f.ex("B1", "multiple choice", "A", "Toyo's time: 10h 31m 30s",
     "予選会で1位の東洋大学のタイムは？ A. 10時間31分30秒 · B. 1分46秒 · C. 9時間31分", size=13.8, gap=0)
f.ex("B1", "multiple choice", "B", "1m 46s = 106 seconds",
     "法政大学は国士舘大学より何秒速かったですか。 A. 33秒 · B. 106秒 · C. 46秒", size=13.8, gap=0)
f.ex("A2", "multiple choice", "C", "Mochi reviews rose 168%",
     "『餅』の口コミは何%増えましたか。 A. 82% · B. 84% · C. 168%", size=13.8, gap=0)
f.ex("B1", "multiple choice", "A", "The littering fine is 2,000 yen",
     "渋谷でゴミを捨てた時の罰金は？ A. 2,000円 · B. 1,000万円 · C. 900円", size=13.8, gap=0)
f.ex("A2", "multiple choice", "B", "The Shosoin Exhibition ends Nov 9",
     "正倉院展はいつまでですか。 A. 11月1日 · B. 11月9日 · C. 10月31日", size=13.8, gap=0)
f.ex("B1", "multiple choice", "C", "SoftBank won 91 games",
     "ソフトバンクのレギュラーシーズンの勝ち数は？ A. 71 · B. 49 · C. 91", size=13.8, gap=0)
f.head("C · 読んで答えましょう", 21, OLIVE, 5)
f.para("ケンは大学生です。今週の土よう日、横浜スタジアムで日本シリーズの第1戦があります。ケンはチケットを買うことができませんでしたから、テレビで応援します。日よう日は、奈良の正倉院展へ行くつもりです。来週の読書週間には、図書館で本を3冊借りたいと思っています。", 15, lh=1.3, split=False)
f.ex("A2", "multiple choice", "B", "Ken cheers at home in front of the TV",
     "ケンは土よう日に何をしますか。 A. スタジアムへ行く · B. テレビで応援する · C. 奈良へ行く", size=13.8, gap=0)
f.ex("A2", "multiple choice", "B", "He could not buy a ticket",
     "ケンはなぜスタジアムへ行きませんか。 A. 時間がない · B. チケットが買えなかった · C. 雨だった", size=13.8, gap=0)
f.ex("A2", "multiple choice", "A", "Sunday is the Shosoin Exhibition",
     "日よう日の予定は？ A. 正倉院展 · B. 図書館 · C. ハロウィン", size=13.8, gap=0)
f.ex("B1", "multiple choice", "B", "He wants to borrow three books",
     "読書週間に借りたい本は？ A. 2冊 · B. 3冊 · C. 9冊", size=13.8, gap=0)
f.head("D · 文を作りましょう", 21, OLIVE, 5)
f.ex("A2", "sentence building", "私は土よう日に試合を見ます。", "Subject + time + object + verb",
     "私は / 土よう日に / 試合を見ます → ___", instr="Build a sentence", size=13.8, gap=0)
f.ex("A2", "sentence building", "紅葉は今週末が見頃です。", "見頃 = the peak viewing time",
     "紅葉は / 今週末が / 見頃です → ___", instr="Build a sentence", size=13.8, gap=0)
f.ex("B1", "sentence building", "図書館で本を借ります。", "The place of an action takes 「で」",
     "図書館で / 本を / 借ります → ___", instr="Build a sentence", size=13.8, gap=0)
f.ex("B1", "sentence building", "ジェラードンは1,342点で優勝しました。", "Points + で + 優勝しました",
     "ジェラードンは / 1,342点で / 優勝しました → ___", instr="Build a sentence", size=13.8, gap=0)
f.head("E · 翻訳しましょう", 21, OLIVE, 5)
f.ex("A2", "translation", "The procession leaves Kyoto Gyoen at 12:00.", "See page 3",
     "行列は京都御苑を12時に出発します。 → ___", instr="Translate", size=13.8, gap=0)
f.ex("B1", "translation", "If you drop litter, the fine is 2,000 yen.", "See page 5",
     "ゴミを捨てると、2,000円の罰金です。 → ___", instr="Translate", size=13.8, gap=0)
f.ex("B1", "translation", "読書週間は来週の火よう日から始まります。", "See page 7",
     "Reading Week starts next Tuesday. → ___", instr="Translate", size=13.8, gap=0)
f.ex("B2", "translation", "私は池袋のハロウィンのイベントに行きたいです。", "See page 5 (the Ikebukuro event)",
     "I want to go to the Halloween event in Ikebukuro. → ___", instr="Translate", size=13.8, gap=0)
f.head("F · 今週のことば", 21, OLIVE, 5)
f.match_set("B2", "matching",
            ["見頃", "福袋", "行列", "勝率"],
            ["勝った割合（.650など）",
             "花や紅葉がいちばん美しい時",
             "中身が見えない本のセット",
             "昔の服を着た人の列"],
            ["b", "c", "d", "a"],
            ["見頃 = peak viewing time (b)", "福袋 = a set with hidden contents (c)", "行列 = a procession (d)", "勝率 = winning percentage (a)"],
            instr="Match words to meanings")
f.head("G · 図書館で", 21, OLIVE, 5)
f.ex("B1", "cloze", "A", "見せてください = please show me",
     "— 本を借りたいです。— はい、カードを ___ ください。(A. 見せて · B. 見て)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "借りられます = can borrow (potential)",
     "— 3冊、___ か。 (A. 借りられます · B. 借りますた)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "Reading Week starts Tuesday (page 7)",
     "— いつ返しますか。— 読書週間が始まる ___ に返します。(A. 火よう日 · B. 土よう日)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "The book lucky bags are popular",
     "— おすすめはありますか。— 『本の ___ 』が人気です。(A. 福袋 · B. 行列)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "どういたしまして = you are welcome",
     "— ありがとうございました。— ___ 。(A. どういたしまして · B. さようなら)", size=13.8, gap=0)
f.head("H · 書いてみましょう", 21, OLIVE, 5)
MODELO = ("私の秋の週末は、スポーツと読書の週末です。"
          "土よう日は、友達と家で日本シリーズを見ます。私はDeNAを応援します。"
          "試合の後は、近くの公園へ紅葉を見に行きます。"
          "日よう日は、図書館で借りた本を読みます。"
          "読書週間も始まりますから、静かな場所で大きな冒険をしたいです。"
          "秋は短いですが、楽しいことが多い季節です。")
NCHARS = len(MODELO.replace(" ", ""))
f.expl(f"Writing task (no single correct answer); the model text ({NCHARS} characters) is below.")
f.ex("B1", "writing", "(open task — model text below)", f"Model text in section H on this page ({NCHARS} characters)",
     "『私の秋の週末』について、150〜200字で書いてください。スポーツ、紅葉、読書の中から一つ選んでください。", instr="Writing", size=13.8, gap=0)
f.para("例： " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= 答え =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "答え · Answers — grouped by page; just find your number", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "A short English note with every answer · ✓ = the model-text item", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— Page {pg} —", 13.3, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "writing":
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
