# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-zh-cn-ja/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 词语精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("词语　言葉のポイント", "Lucerna", "语言聚焦　三个级别，三个主题　3レベル、3つのテーマ")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　决赛与包裹　決勝と荷物", 24)
a.para("今週の言葉：决赛 (juésài、決勝)、冠军 (guànjūn、優勝者)、半决赛 (bànjuésài、準決勝)、到货 (dàohuò、届いた)、退换货 (tuìhuànhuò、返品と交換)、价保 (jiàbǎo、価格保証)。", 21.5)
a.glossline("量詞は今も大事： 一个包裹（荷物1つ）、一部电影（映画1本）、一场演练（訓練1回）。")
a.ex("A2", "完成句子", "个", "包裹 は量詞 个 gè を取る。",
     "我拿了___包裹。", instr="入れよう", size=20, gap=10)
a.ex("A2", "单选", "A", "决赛は決勝、最後の試合という意味。",
     "「决赛」是什么意思？ A. 最后一场比赛 · B. 第一场比赛 · C. 练习赛", size=20, gap=10)
a.ex("A2", "完成句子", "决赛", "juésài — 決勝。11月15日はBLG対GEN。",
     "11月15日凌晨3点，BLG和GEN打___。", instr="入れよう", size=20, gap=10)
a.ex("A2", "单选", "A", "荷物は 個 を使う — 只 や 条 ではない。",
     "哪个说法对？ A. 一个包裹 · B. 一只包裹 · C. 一条包裹", size=20, gap=10)
a.para("もうひとつ練習：「我的包裹到了吗？」（荷物は届きましたか？）荷物を待つときは、まず聞いてからロッカーへ行こう。", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　时间与日期　時刻と日付", 24)
b.para("中国語の時刻は大きい順：年、月、日、曜日、時間帯、時。例：「11月15日星期日凌晨3点」（11月15日（日）午前3時）、「11月22日星期日」（11月22日（日））、「11月21日星期六」（11月21日（土））。一番大きい単位が先で、順序は崩れない。", 21.5)
b.glossline("英語の «Sunday, Nov 22» は 11月22日星期日 になる。")
b.ex("B1", "单选", "B", "凌晨 língchén — 真夜中過ぎの未明。",
     "「凌晨3点」是什么时候？ A. 下午3点 · B. 半夜3点 · C. 中午12点", size=20, gap=10)
b.ex("B1", "完成句子", "早上", "06:00は 早上（朝）— 夜ではない。",
     "半决赛在北京时间11月8日___6点开始。（不是晚上）", instr="入れよう", size=20, gap=10)
b.ex("B1", "单选", "A", "大きい順：11月22日、日曜日。",
     "哪个顺序对？ A. 11月22日星期日 · B. 星期日11月22日 · C. 星期日小雪11月22日", size=20, gap=10)
b.ex("B1", "完成句子", "周日", "11月22日は日曜日 — 周日。",
     "11月22日是星期日，也可以说___。小雪在这天。", instr="入れよう", size=20, gap=10)
b.para("あと2語： 凌晨 (língchén) は真夜中過ぎ、夜明け前の未明。傍晚 (bàngwǎn) は暗くなる直前の短い時間。", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　读新闻　ニュースを読む", 24)
c.para("話に主張（说法）が入るときは、3種類の文を分けよう：主張（说法）、データ（数据）、予報（预报）。6ページが例です。「没有爆掉」は今年の荷物についての主張、139.38億件の合計は報告されたデータ — すでに数えられており、推測ではない — そして「第三波是最高峰」は中通云仓による予報：予想であり、まだ数えられていない。", 21.5)
c.glossline("どの数字にも聞こう：誰の数字で、いつ測ったのか？")
c.ex("B2", "单选", "A", "「139.38亿件」は郵政局の最終集計で、すでに数えられた数です。",
     "「139.38亿件」在第6版里是什么？ A. 已经数完的事实 · B. 邮政局的预计 · C. 广告词", size=20, gap=10)
c.ex("B2", "完成句子", "数据", "shùjù — 測った数字で、主張ではない。",
     "买东西以前，先看___，再看广告。", instr="入れよう", size=20, gap=10)
c.ex("B2", "单选", "B", "データと決済ページが先、見出しは最後。",
     "读新闻时，哪个做法最好？ A. 只看标题 · B. 先看数据和结算页 · C. 只看评论", size=20, gap=10)
c.ex("B2", "完成句子", "预报", "yùbào — 予報は予測で、まだ事実ではない。",
     "「第三波是最高峰」是___，还没发生。", instr="入れよう", size=20, gap=10)
c.para("自分で試そう：1ページのカレンダー枠で「11月22日」は日付 — データです。広告の言葉は主張です。見分けられますか？", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters + image ----
bx = COLX[3]
errs = [
    ("「他开心的去拿包裹」", "→ 「他开心地去拿包裹。」", "地 (de) は動作のしかたを示す。"),
    ("「包裹来的很快」", "→ 「包裹来得很快。」", "得 (de) は動詞＋程度をつなぐ： 来得快。"),
    ("「我拿了两个包裹个」", "→ 「我拿了两个包裹。」", "順序：数＋量詞＋名詞。"),
    ("「总决赛在星期日11月15日凌晨3点」", "→ 「总决赛在11月15日，星期日凌晨3点。」", "時間は大きい→小さい順：曜日が最後。"),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易错诊所　まちがいクリニック", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「先看预报，再决定穿什么。」先…再…の型は行動の順番を示す。"
wcn = "型： 先 … 再 … — まずX、それからY。"
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill=BOX)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本周句式　文型", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「你好！我住在上海。11月9日半决赛，我看了BLG打T1，3比1，真好看！双11我买了一件外套，包裹两天就到了。你们呢？」"
lcn = "编辑部示例信，不是真实来信。VOL.3曾预告本期刊登真实来信和最佳作文；截至11月10日截稿，仍未收到，继续征集。延期不是取消。編集部注：VOL.3はVOL.4に本物の手紙を載せると約束しましたが、11月10日までに届きませんでした。延期であり、中止ではありません。"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "读者园地　読者の広場", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- P7 image (brush) below the letters box ----
iy7 = col3_end + 12
image(p, "brush.jpg", bx, iy7, CW, 130)
cy7 = caption(p, bx, iy7 + 130, CW, "毛笔（资料图）。写中文，先从一笔一画开始。",
              "写真：Mx. Granger — CC0（Wikimedia Commons）")
img_end = cy7
print("P7 image ends", img_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, img_end + 44)
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "本周金句　今週の名文（本号の記事からそのまま）", 27, "sans", True, OLIVE)
quotes = [
    ("「决赛对阵GEN」", "決勝：BLG対GEN。", "p. 1"),
    ("「包裹都到了吗」", "荷物は全部届いた？", "p. 2"),
    ("「小雪气寒而将雪矣」", "小雪：空気が冷たくなり、雪が近づく。", "p. 3"),
    ("「两支中国队进了四强」", "中国の2チームが準決勝に進んだ。", "p. 4"),
    ("「先看简介，再决定」", "まずあらすじを読んでから決めよう。", "p. 5"),
    ("「无高峰，全高峰」", "ひとつのピークだけではない — 毎日がピーク。", "p. 6"),
    ("「先打开看一看，再确认收货」", "まず開けて確認し、それから受け取りを確認しよう。", "p. 6"),
    ("「悦读深圳」", "深圳で楽しく読む — 深圳読書月間のテーマ。", "p. 3"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, en, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 120
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, en + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 120 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "下期预告　来週 (VOL.5)", 24, "sans", True, GOOSE)
p.para(MX + 28, py + 84, "S16总决赛打完了，谁是冠军？小雪之后，冬天怎么过？还有你们的来信和第8版最佳作文。下周见！", 21, "serif", False, ONCLOTH, RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-ciyu.svg")
print("P7 saved, exercises so far:", len(REG))
