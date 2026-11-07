# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-zh-cn-ja/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 词语精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("词语 · 言葉の焦点", "Lucerna", "语言聚焦 · 三个级别,三个主题 · 3レベル、3テーマ")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 双11与包裹 · ショッピング", 24)
a.para("今週の買い物言葉： 高潮场 (gāocháochǎng、ピークセール期間）、包裹 (bāoguǒ、荷物）、取件码 (qǔjiànmǎ、受取コード）、快递柜 (kuàidìguì、宅配ロッカー）。安全の言葉： 消防 (xiāofáng、防火）、疏散 (shūsàn、避難する）、自救 (zìjiù、自力で助かる）。", 21.5)
a.glossline("量詞は今も大事： 一个包裹（荷物1つ）、一部电影（映画1本）、一场演练（訓練1回）。")
a.ex("A2", "完成句子", "个", "包裹 は量詞 个 gè を取る。",
     "我拿了___包裹。", instr="入れよう", size=20.5, gap=10)
a.ex("A2", "单选", "A", "高潮场 はピークセール期間という意味。",
     "「高潮场」是什么意思? A. 最忙的卖货时间 · B. 必须先付定金 · C. 只有11月11日便宜", size=20.5, gap=10)
a.ex("A2", "完成句子", "消防", "xiāofáng — 防火、11月9日。",
     "11月9日是全国___日。", instr="入れよう", size=20.5, gap=10)
a.ex("A2", "单选", "A", "荷物は 個 を使う — 只 や 条 ではない。",
     "哪个说法对? A. 一个包裹 · B. 一只包裹 · C. 一条包裹", size=20.5, gap=10)
a.para("もう一つ練習： 「我的包裹到了吗?」（荷物は届いた？）荷物を待つときはまず聞いて、それからロッカーへ行こう。", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 时间与日期 · 時間と日付", 24)
b.para("中国語は時間を大きい→小さい順に言う：年、月、日、曜日、時間帯、時。この号の例： 「11月9日星期一」（11月9日月曜）、「11月10日星期二20点」（11月10日火曜20時）、「11月15日星期日凌晨3点」（11月15日日曜午前3時）。一番大きい単位が先で、順序は崩れない。", 21.5)
b.glossline("英語の «Monday, Nov 9» は 11月9日星期一 になる。")
b.ex("B1", "单选", "B", "凌晨 língchén — 真夜中過ぎの未明。",
     "「凌晨3点」是什么时候? A. 下午3点 · B. 半夜3点 · C. 中午12点", size=20.5, gap=10)
b.ex("B1", "完成句子", "早上", "06:00は 早上（朝）— 夜ではない。",
     "四分之一决赛在北京时间11月4日___6点开始。(不是晚上)", instr="入れよう", size=20.5, gap=10)
b.ex("B1", "单选", "A", "大きい→小さい順：11月15日、日曜、03:00。",
     "哪个顺序对? A. 11月15日星期日凌晨3点 · B. 凌晨3点星期日11月15日 · C. 星期日凌晨3点11月15日", size=20.5, gap=10)
b.ex("B1", "完成句子", "周一", "11月9日は月曜 — 周一。",
     "11月9日是星期一,也可以说___。消防日在这天。", instr="入れよう", size=20.5, gap=10)
b.para("あと2語： 凌晨 (língchén) は真夜中過ぎ、夜明け前の未明。傍晚 (bàngwǎn) は暗くなる直前の短い時間。", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 读新闻 · ニュースを読む", 24)
c.para("話に主張（说法）が入るときは、3種類の文を分けよう：主張（说法）、データ（数据）、予報（预报）。6ページが例： 「最大的一波」 は11月11日についての主張、倍率1.5と2.5は報じられたデータ、寒気の気温は予報 — 予測であって、まだ事実ではない。", 21.5)
c.glossline("どの数字にも聞こう：誰の数字で、いつ測ったのか？")
c.ex("B2", "单选", "C", "「最大的一波」 は11月11日のピークについての主張で、測ったデータではない。",
     "「最大的一波」在第6版里是什么? A. 数据 · B. 预报 · C. 说法", size=20.5, gap=10)
c.ex("B2", "完成句子", "数据", "shùjù — 測った数字で、主張ではない。",
     "买东西以前,先看___,再看广告。", instr="入れよう", size=20.5, gap=10)
c.ex("B2", "单选", "B", "データと決済ページが先、見出しは最後。",
     "读新闻时,哪个做法最好? A. 只看标题 · B. 先看数据和结算页 · C. 只看评论", size=20.5, gap=10)
c.ex("B2", "完成句子", "预报", "yùbào — 予報は予測で、まだ事実ではない。",
     "冷空气的温度是___,还没发生。", instr="入れよう", size=20.5, gap=10)
c.para("自分でやってみよう：1ページのカレンダーで 「11月11日」 は日付 — データ。広告の言葉は主張。見分けられるかな？", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「他开心的去拿包裹」", "→ 「他开心地去拿包裹。」", "地 (de) は動作のしかたを示す。"),
    ("「包裹来的很快」", "→ 「包裹来得很快。」", "得 (de) は動詞＋程度をつなぐ： 来得快。"),
    ("「我拿了两个包裹个」", "→ 「我拿了两个包裹。」", "順序：数＋量詞＋名詞。"),
    ("「总决赛在星期日11月15日凌晨3点」", "→ 「总决赛在11月15日,星期日凌晨3点。」", "時間は大きい→小さい順：曜日が最後。"),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易错诊所 · 間違いクリニック", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「先看取件码,再开柜门。」（コードを確認してからロッカーを開ける。）型 先…再… が行動の順序を示す。"
wcn = "型： 先 … 再 … — まずX、それからY。"
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本周句式 · 文の型", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「你好!我住在北京。11月9日学校做了消防演练,我学会了走楼梯。双11我买了一本书,包裹两天就到了。周日凌晨,我想看S16总决赛!」"
lcn = "编辑部示例信,不是真实来信。VOL.2曾预告本期刊登真实来信和最佳作文;截至11月2日截稿,仍未收到,本期仍刊示例,继续征集。延期不是取消。編集部注：VOL.2はVOL.3に本物の手紙を約束したが、11月2日までに届かなかった。例文を載せる。延期であって中止ではない。"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "读者园地 · 読者のコーナー", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "本周金句 · 今週のフレーズ（原文のまま、この号の記事から）", 27, "sans", True, OLIVE)
quotes = [
    ("「双11的正日子」", "双11当日そのもの。", "p. 1"),
    ("「先看结算页,再决定买不买」", "決済ページを確認してから決めよう。", "p. 2"),
    ("「提高自防自救能力」", "自ら守り自ら助かる力を高める。", "p. 3"),
    ("「三支队进了八强」", "3チームが準々決勝へ。", "p. 4"),
    ("「输了就回家」", "負けたら帰る。", "p. 4"),
    ("「老电影,新画面」", "古い映画、新しい映像。", "p. 5"),
    ("「快递的高峰分三波」", "荷物のピークは3波で来る。", "p. 6"),
    ("「着火了不坐电梯」", "火事のとき、エレベーターに乗らない。", "p. 3"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, en, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 150
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, en + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 150 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "下期预告 · 来週（VOL.4）", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "S16总决赛打完了,谁是冠军?包裹都到了吗?还有你们的来信和第8版最佳作文。下周见!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-ciyu.svg")
print("P7 saved, exercises so far:", len(REG))
