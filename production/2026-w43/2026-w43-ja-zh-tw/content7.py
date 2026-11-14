# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · ことば (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("ことば　語言", "Lucerna", "言語フォーカス　三つのレベル、三つのテーマ　三個級別，三個主題")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　本と読書のことば", 24)
a.para("来週の火よう日（27日）から、『第80回読書週間』が始まります。11月9日までです。今年のスローガンは『静かだけど、冒険中。』です。秋は『読書の秋』。本を読む季節です。", 21.5)
a.para("町田市の図書館では、子どものための『本の福袋』が発表されました（20日）。中身が見えない、3冊の本のセットです。開ける時の楽しみも、読書の楽しみです。", 21.5)
a.expl("読書週間 讀書週 · 福袋 看不見內容的套裝 · 中身 裡面的東西。")
a.ex("A2", "完成句子", "27", "讀書週從27日（週二）開始",
     "読書週間は ___ 日（火）から始まります。", instr="填空", size=20.5, gap=10)
a.ex("A2", "完成句子", "9", "讀書週到11月9日",
     "読書週間は11月 ___ 日までです。", instr="填空", size=20.5, gap=10)
a.ex("A2", "完成句子", "80", "今年是第80屆讀書週",
     "今年は第 ___ 回の読書週間です。", instr="填空", size=20.5, gap=10)
a.ex("A2", "單選", "B", "福袋裡有3本書",
     "『本の福袋』の中には、本が何冊ありますか。 A. 2冊 · B. 3冊 · C. 9冊", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　応援のことば", 24)
b.para("スポーツの応援では、こんな言葉を使います。『頑張れ！』『勝つぞ！』『負けるな！』。日本シリーズでは、横浜スタジアムで大きな声が聞こえます。", 21.5)
b.para("応援する時は、チームの名前を呼びます。『DeNA、頑張れ！』。勝った時は『勝った！』、負けた時は『次、頑張ろう』と言います。", 21.5)
b.expl("頑張れ 加油 · 勝つぞ 必贏 · 負けるな 別認輸")
b.ex("B1", "單選", "B", "頑張れ＝加油",
     "応援の言葉はどれですか。 A. おはよう · B. 頑張れ · C. さようなら", size=20.5, gap=10)
b.ex("B1", "完成句子", "勝つ", "勝つぞ＝一定會贏",
     "勝ちたい気持ちの言葉：『___ ぞ！』", instr="填空", size=20.5, gap=10)
b.ex("B1", "單選", "B", "輸了要說「次、頑張ろう」",
     "負けた時に言う言葉は？ A. 勝った！ · B. 次、頑張ろう · C. お帰り", size=20.5, gap=10)
b.ex("B1", "完成句子", "応援", "応援する＝聲援",
     "大きな声でチームを助けることを「___ する」と言います。", instr="填空", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　パーセントを読む", 24)
c.para("数字の読み方を練習しましょう。『168%増えました』は、前の年の約2.7倍になった、という意味です。100%増えると2倍、50%増えると1.5倍です。", 21.5)
c.para("野球の勝率『.650』は、『6割5分』と読みます。割合の言葉は、ニュースによく出ます。『過去最多』『約〜』『〜以上』も、大切な言葉です。", 21.5)
c.expl("〜倍 倍 · 割 成（十分之一）· 過去最多 歷史最多。")
c.ex("B2", "單選", "B", "增加100%就是變成2倍",
     "100%増えると、何倍になりますか。 A. 1倍 · B. 2倍 · C. 10倍", size=20.5, gap=10)
c.ex("B2", "單選", "A", "勝率.650讀作「6割5分」",
     "勝率『.650』の読み方は？ A. 6割5分 · B. 65割 · C. 6分5割", size=20.5, gap=10)
c.ex("B2", "完成句子", "1.5", "增加50%就是1.5倍",
     "50%増えると、___ 倍になります。", instr="填空", size=20.5, gap=10)
c.ex("B2", "完成句子", "168", "第2版：「餅」的評論增加168%",
     "『餅』の口コミは、前の年より ___ %増えました。（2面）", instr="填空", size=20.5, gap=10)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「本を三本買いました」", "→ 本の数え方は「冊」です：『本を三冊買いました』。", "書用「冊」來數，不用「本」。"),
    ("「昨日、図書館へ行きます」", "→ 『昨日』があるので過去形：『図書館へ行きました』。", "有「昨日」時要用過去式。"),
    ("「趣味は本を読むです」", "→ 『こと』が必要です：『本を読むことです』。", "動詞名詞化時要加「こと」。"),
    ("「図書館に本を借ります」", "→ 場所は『で』：『図書館で本を借ります』。", "動作發生的場所用「で」。"),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "まちがい診療所　易錯診所", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "『静かだけど、冒険中。』 — 静かだ＋けど（でも）＋冒険中（〜の最中）。本を読む人は、静かな場所で、大きな冒険をしています。"
wcn = "口號拆解：安靜著，卻在冒險中。"
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "今週のフレーム　本週句式", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「こんにちは。私は高校生です。読書週間には、図書館で借りた本を3冊読みたいです。静かだけど、冒険中！」— 読者の手紙の例"
lcn = "編輯部示例信，非真實來信。VOL.2 將刊登真實來信和第 8 版最佳作文！"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "読者の手紙　讀者園地", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "今週のフレーズ　本週金句（逐字摘自本期文章）", 27, "sans", True, OLIVE)
quotes = [
    ("「この対決は2年ぶりです」", "這場對決時隔兩年。", "第1版"),
    ("「スポーツが熱い週末になります」", "這將是一個體育火熱的週末。", "第1版"),
    ("「紅葉前線は北から南へ下りています」", "紅葉前線正自北向南推進。", "第2版"),
    ("「秋は、食の季節でもあります」", "秋天也是美食的季節。", "第2版"),
    ("「歩きながら、日本の長い歴史を見ることができます」", "可以邊走邊看日本的悠久歷史。", "第3版"),
    ("「結果は来週の新聞でお知らせします」", "結果將在下週的報紙上公布。", "第4版"),
    ("「テレビの前で笑った人も多い週末でした」", "這是一個很多人在電視機前大笑的週末。", "第5版"),
    ("「障害のある人もない人も、同じ場所で同じ試合を見ます」", "無論有無殘障，都在同一地點看同一場比賽。", "第6版"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 150
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 150 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "来週　下期預告 (VOL.2)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "読書週間が始まります（27日・火〜11月9日）。ハロウィンは31日（土）！日本シリーズの結果もお知らせします。あなたの手紙と、第8版の作文の優秀作も載せます。お楽しみに！", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-kotoba.svg")
print("P7 saved, exercises so far:", len(REG))
