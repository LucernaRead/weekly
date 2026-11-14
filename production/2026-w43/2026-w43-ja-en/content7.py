# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · ことば (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("ことば　Language", "Lucerna", "言語フォーカス　三つのレベル、三つのテーマ　Three levels, three themes")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　本と読書のことば", 24)
a.para("来週の火よう日（27日）から、『第80回読書週間』が始まります。11月9日までです。今年のスローガンは『静かだけど、冒険中。』です。秋は『読書の秋』。本を読む季節です。", 21.5)
a.para("町田市の図書館では、子どものための『本の福袋』が発表されました（20日）。中身が見えない、3冊の本のセットです。開ける時の楽しみも、読書の楽しみです。", 21.5)
a.expl("読書週間 Reading Week · 福袋 a lucky bag with hidden contents · 中身 what is inside.")
a.ex("A2", "fill-in", "27", "Reading Week starts Tue the 27th",
     "読書週間は ___ 日（火）から始まります。", instr="Fill in", size=20.5, gap=10)
a.ex("A2", "fill-in", "9", "Reading Week runs to November 9",
     "読書週間は11月 ___ 日までです。", instr="Fill in", size=20.5, gap=10)
a.ex("A2", "fill-in", "80", "This is the 80th Reading Week",
     "今年は第 ___ 回の読書週間です。", instr="Fill in", size=20.5, gap=10)
a.ex("A2", "multiple choice", "B", "A lucky bag holds three books",
     "『本の福袋』の中には、本が何冊ありますか。 A. 2冊 · B. 3冊 · C. 9冊", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　応援のことば", 24)
b.para("スポーツの応援では、こんな言葉を使います。『頑張れ！』『勝つぞ！』『負けるな！』。日本シリーズでは、横浜スタジアムで大きな声が聞こえます。", 21.5)
b.para("応援する時は、チームの名前を呼びます。『DeNA、頑張れ！』。勝った時は『勝った！』、負けた時は『次、頑張ろう』と言います。", 21.5)
b.expl("頑張れ Go for it! · 勝つぞ We'll win! · 負けるな Don't give up!")
b.ex("B1", "multiple choice", "B", "頑張れ = Go for it!",
     "応援の言葉はどれですか。 A. おはよう · B. 頑張れ · C. さようなら", size=20.5, gap=10)
b.ex("B1", "fill-in", "勝つ", "勝つぞ = We'll win!",
     "勝ちたい気持ちの言葉：『___ ぞ！』", instr="Fill in", size=20.5, gap=10)
b.ex("B1", "multiple choice", "B", "After a loss, say 「次、頑張ろう」",
     "負けた時に言う言葉は？ A. 勝った！ · B. 次、頑張ろう · C. お帰り", size=20.5, gap=10)
b.ex("B1", "fill-in", "応援", "応援する = to cheer on",
     "大きな声でチームを助けることを「___ する」と言います。", instr="Fill in", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　パーセントを読む", 24)
c.para("数字の読み方を練習しましょう。『168%増えました』は、前の年の約2.7倍になった、という意味です。100%増えると2倍、50%増えると1.5倍です。", 21.5)
c.para("野球の勝率『.650』は、『6割5分』と読みます。割合の言葉は、ニュースによく出ます。『過去最多』『約〜』『〜以上』も、大切な言葉です。", 21.5)
c.expl("〜倍 times · 割 one tenth · 過去最多 the most ever.")
c.ex("B2", "multiple choice", "B", "Up 100% means twice as much",
     "100%増えると、何倍になりますか。 A. 1倍 · B. 2倍 · C. 10倍", size=20.5, gap=10)
c.ex("B2", "multiple choice", "A", ".650 is read 「6割5分」",
     "勝率『.650』の読み方は？ A. 6割5分 · B. 65割 · C. 6分5割", size=20.5, gap=10)
c.ex("B2", "fill-in", "1.5", "Up 50% means 1.5 times",
     "50%増えると、___ 倍になります。", instr="Fill in", size=20.5, gap=10)
c.ex("B2", "fill-in", "168", "Page 2: mochi reviews rose 168%",
     "『餅』の口コミは、前の年より ___ %増えました。（2面）", instr="Fill in", size=20.5, gap=10)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「本を三本買いました」", "→ 本の数え方は「冊」です：『本を三冊買いました』。", "Books are counted with 「冊」, not 「本」."),
    ("「昨日、図書館へ行きます」", "→ 『昨日』があるので過去形：『図書館へ行きました』。", "With 「昨日」, use the past tense."),
    ("「趣味は本を読むです」", "→ 『こと』が必要です：『本を読むことです』。", "To turn a verb into a noun phrase, add 「こと」."),
    ("「図書館に本を借ります」", "→ 場所は『で』：『図書館で本を借ります』。", "The place where an action happens takes 「で」."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "まちがい診療所　Error clinic", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "『静かだけど、冒険中。』 — 静かだ＋けど（でも）＋冒険中（〜の最中）。本を読む人は、静かな場所で、大きな冒険をしています。"
wcn = "The slogan, broken down: quiet — yet mid-adventure."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "今週のフレーム　Frame of the week", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「こんにちは。私は高校生です。読書週間には、図書館で借りた本を3冊読みたいです。静かだけど、冒険中！」— 読者の手紙の例"
lcn = "Editors' example — not a real letter. VOL.2: real letters and the best Page 8 writing!"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "読者の手紙　Readers' corner", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "今週のフレーズ　Phrases of the week (verbatim from this issue)", 27, "sans", True, OLIVE)
quotes = [
    ("「この対決は2年ぶりです」", "This match-up returns after two years.", "p.1"),
    ("「スポーツが熱い週末になります」", "It will be a weekend of great sport.", "p.1"),
    ("「紅葉前線は北から南へ下りています」", "The foliage front is moving from north to south.", "p.2"),
    ("「秋は、食の季節でもあります」", "Autumn is also a season of food.", "p.2"),
    ("「歩きながら、日本の長い歴史を見ることができます」", "Walking, you can see Japan's long history.", "p.3"),
    ("「結果は来週の新聞でお知らせします」", "We will give the results in next week's paper.", "p.4"),
    ("「テレビの前で笑った人も多い週末でした」", "A weekend when many laughed in front of the TV.", "p.5"),
    ("「障害のある人もない人も、同じ場所で同じ試合を見ます」", "Disabled or not, all watch the same match in the same place.", "p.6"),
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
p.text(MX + 28, py + 44, "来週　Next week (VOL.2)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "読書週間が始まります（27日・火〜11月9日）。ハロウィンは31日（土）！日本シリーズの結果もお知らせします。あなたの手紙と、第8版の作文の優秀作も載せます。お楽しみに！", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-kotoba.svg")
print("P7 saved, exercises so far:", len(REG))
