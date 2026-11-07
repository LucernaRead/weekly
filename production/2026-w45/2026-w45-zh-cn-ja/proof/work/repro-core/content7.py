# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-cn-ja-proof/work/repro-core/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 词语精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("词语 · 言葉の焦点", "Lucerna", "语言聚焦 · 三个级别,三个主题 · 3つのレベル、3つのテーマ")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 双11与冬天 · 買い物と冬", 24)
a.para("今週の買い物言葉：现货（xiànhuò、在庫あり）、直降（zhíjiàng、直接の値下げ）、立减（lìjiǎn、決済時の値引き）、结算页（jiésuàn yè、決済画面）。冬の言葉：立冬（lìdōng、立冬）、补冬（bǔdōng、冬に備えてしっかり食べること）、厚衣服（hòu yīfu、暖かい服）。", 21.5)
a.glossline("量詞は今も大切：一件毛衣（セーター1着）、一条围巾（マフラー1本）、一部电影（映画1本）。")
a.ex("A2", "完成句子", "件", "毛衣には量詞件 jiàn を使う。",
     "我想买一___毛衣。", instr="空欄に入れよう", size=20.5, gap=10)
a.ex("A2", "单选", "A", "直降は価格そのものが下がること。",
     "「直降」是什么意思? A. 价格直接变低 · B. 必须先付定金 · C. 只有11月11日便宜", size=20.5, gap=10)
a.ex("A2", "完成句子", "立冬", "lìdōng — 立冬、11月7日。",
     "11月7日是___。", instr="空欄に入れよう", size=20.5, gap=10)
a.ex("A2", "单选", "A", "服には件を使い、个や条は使わない。",
     "哪个说法对? A. 一件毛衣 · B. 一个毛衣 · C. 一条毛衣", size=20.5, gap=10)
a.para("もう一つ練習しよう：「这件毛衣多少钱?」（このセーターはいくら？）買い物のときは、まず値段を聞いてから支払おう。", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 时间与日期 · 時刻と日付", 24)
b.para("中国語の時刻は大きい単位から小さい単位へ：年、月、日、曜日、時間帯、時刻。今号の例：「11月7日星期六17点52分」（11月7日（土）17時52分）、「11月10日星期二20点」（11月10日（火）20時）、「11月15日凌晨3点」（11月15日午前3時）。いちばん大きい単位が先で、順序は決して乱れない。", 21.5)
b.glossline("日本語の「11月7日（土）の夜」は中国語では11月7日星期六晚上になる。")
b.ex("B1", "单选", "B", "凌晨 língchén — 真夜中過ぎの未明の時間。",
     "「凌晨3点」是什么时候? A. 下午3点 · B. 半夜3点 · C. 中午12点", size=20.5, gap=10)
b.ex("B1", "完成句子", "早上", "06時は早上（朝）で、夜ではない。",
     "四分之一决赛在北京时间11月4日___6点开始。(不是晚上)", instr="空欄に入れよう", size=20.5, gap=10)
b.ex("B1", "单选", "A", "大きい単位から小さい単位へ：11月7日、土曜日、17時52分。",
     "哪个顺序对? A. 11月7日星期六17点52分 · B. 17点52分星期六11月7日 · C. 星期六17点52分11月7日", size=20.5, gap=10)
b.ex("B1", "完成句子", "周六", "11月7日は土曜日 — 周六。",
     "11月7日是星期六,也可以说___。立冬在这天。", instr="空欄に入れよう", size=20.5, gap=10)
b.para("あと2語：凌晨（língchén）は真夜中過ぎ、夜明け前の時間、傍晚（bàngwǎn）は暗くなる直前の短い時間。", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 读新闻 · ニュースの読み方", 24)
c.para("話に主張（说法）が含まれるときは、3種類の文を分けよう：主張（说法）、データ（数据）、広告（广告）。6ページが例：「最低价」は主張、練習のかごの270元は練習用データ、決済画面には実際に支払う額が表示される。", 21.5)
c.glossline("すべての価格について問おう：誰の数字で、どこに書かれているのか？")
c.ex("B2", "单选", "C", "「最低价」は広告の主張で、測ったデータではない。",
     "「最低价」在第6版里是什么? A. 数据 · B. 声明 · C. 说法", size=20.5, gap=10)
c.ex("B2", "完成句子", "数据", "shùjù — 測った数字で、主張ではない。",
     "买东西以前,先看___,再看广告。", instr="空欄に入れよう", size=20.5, gap=10)
c.ex("B2", "单选", "B", "データと決済画面が先、見出しは最後。",
     "读新闻时,哪个做法最好? A. 只看标题 · B. 先看数据和结算页 · C. 只看评论", size=20.5, gap=10)
c.ex("B2", "完成句子", "结算", "jiésuàn — 決済画面には本当の価格が表示される。",
     "真正要付的钱,看___页的价格。", instr="空欄に入れよう", size=20.5, gap=10)
c.para("自分で試そう：1ページのカレンダー欄では、「11月7日」は日付、つまりデータだ。広告の言葉は主張だ。見分けられるかな？", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「他高兴的跳起来」", "→ 「他高兴地跳起来。」", "地（de）は動作のしかたを示す。"),
    ("「他跑的很快」", "→ 「他跑得很快。」", "得（de）は動詞＋程度をつなぐ：跑得快。"),
    ("「我买了三只毛衣个」", "→ 「我买了三件毛衣。」", "順序：数詞＋量詞＋名詞。最後の个は1つ余計で、セーターには件を使う。"),
    ("「立冬在星期六十一月七日」", "→ 「立冬在11月7日,星期六。」", "時刻は大きい単位から小さい単位へ：曜日は最後。"),
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
wt = "「先看评价,再下单。」（まず評価を確認してから注文する。）文型先…再…は動作の順序を示す。ほかにも：「先看天气,再出门。」"
wcn = "文型：先 … 再 … — まずX、それからY。"
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本周句式 · 今週の文型", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「你好!我住在上海。立冬那天,我吃了饺子,也给妈妈打了电话。双11,我买了一件毛衣,现货第二天就到了。」"
lcn = "编辑部示例信,不是真实来信。编辑部说明:VOL.1曾预告本期(VOL.2)刊登真实读者来信和VOL.1第8版最佳作文;至今没有收到真实来信,也没有可刊登的投稿,所以本期仍刊登编辑部示例,并继续征集。延期不是取消。編集部注：VOL.1では本号（VOL.2）に本物の読者の手紙とVOL.1第8版の最優秀作文を掲載すると予告しました。まだ本物の手紙は届いておらず、掲載できる投稿もありません。そのため今号も編集部の例文を掲載し、引き続き募集します。延期であって中止ではありません。中国語の手紙をぜひお寄せください！"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
# NOTE: the disclosure above mixes Chinese and English in one string; the
# sans wrap measures CJK and Latin with the same SC face, so the height
# formula above (sans, 20pt) matches the render path. Verified in the build log.
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "读者园地 · 読者の広場", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "本周金句 · 今週のフレーズ（今号の記事からそのまま抜粋）", 27, "sans", True, OLIVE)
quotes = [
    ("「不用等11月11日」", "11月11日まで待つ必要はない。", "p. 1"),
    ("「下单就能发货」", "注文すれば発送される。", "p. 2"),
    ("「先看结算页,再付款」", "決済画面を確認してから支払おう。", "p. 2"),
    ("「水开始结冰」", "水が凍り始める。", "p. 3"),
    ("「三场都输了」", "3シリーズすべて負けた。", "p. 4"),
    ("「小局一场没赢」", "1ゲームも勝てなかった。", "p. 4"),
    ("「故事够不够好」", "でも、物語は十分に良いのか？", "p. 5"),
    ("「别以后,就现在」", "あとでではなく、今。", "p. 5"),
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
p.text(MX + 28, py + 44, "下期预告 · 来週（VOL.3）", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "双11当天11月11日星期三,包裹到了吗?S16淘汰赛打完了,谁进了决赛?总决赛北京时间11月15日凌晨3点。还有你们的来信和第8版最佳作文。下周见!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-ciyu.svg")
print("P7 saved, exercises so far:", len(REG))
