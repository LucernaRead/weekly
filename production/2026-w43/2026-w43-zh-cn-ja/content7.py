# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zh-cn-ja/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 词语精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("词语 · 言葉の焦点", "Lucerna", "语言聚焦 · 三个级别，三个主题 · 3つのレベル、3つのテーマ")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 购物与量词 · 量詞", 24)
a.para("買い物のとき、中国語は量詞（量词）を使います：一件外套（コート1着）、一条围巾（マフラー1本）、一斤蟹（カニ500グラム）、一只蟹（カニ1匹）。型は：数 + 量詞 + 名詞（数词 + 量词 + 名词）です。", 21.5)
a.glossline("英語は大まかに数えますが、中国語は物の種類ごとに量詞を選びます — 複数形も -s もありません。")
a.ex("A2", "完成句子", "件", "外套の量詞は件（jiàn）。",
     "我想买一___外套。", instr="空所補充", size=20.5, gap=10)
a.ex("A2", "单选", "B", "围巾の量詞は条（tiáo、長くて柔らかい物）。",
     "「一条」可以说什么? A. 一条外套 · B. 一条围巾 · C. 一条大闸蟹", size=20.5, gap=10)
a.ex("A2", "完成句子", "斤", "斤 jīn — 500グラム；市場の価格は1斤あたり。",
     "大闸蟹多少钱一___?", instr="空所補充", size=20.5, gap=10)
a.ex("A2", "单选", "A", "服には件を使い、个や条ではない。",
     "哪个说法对? A. 一件衣服 · B. 一个衣服 · C. 一条衣服", size=20.5, gap=10)
a.para("もう一つ練習：「这件外套多少钱？」（このコートはいくらですか？）買い物のときは、まず値段を聞いて、それから払いましょう。", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 时间与日期 · 時刻と日付", 24)
b.para("中国語の時刻は大→小の順：年、月、日、曜日、一日の区分、時。例：「10月20日晚上8点」（10月20日夜8時）— いちばん大きい単位が先で、順番は崩れません。", 21.5)
b.glossline("だから英語の «Friday evening, Oct 23» は 10月23日星期五晚上 になります。")
b.ex("B1", "单选", "B", "凌晨 língchén — 真夜中過ぎの時間帯。",
     "「凌晨3点」是什么时候? A. 下午3点 · B. 半夜3点 · C. 中午12点", size=20.5, gap=10)
b.ex("B1", "完成句子", "上午", "NBAは北京時間の午前に開幕。",
     "NBA 在北京时间10月21日___开打。(不是晚上)", instr="空所補充", size=20.5, gap=10)
b.ex("B1", "单选", "A", "大→小の順：10月20日、夜、8時。",
     "哪个顺序对? A. 10月20日晚上8点 · B. 8点晚上10月20日 · C. 晚上8点10月20日", size=20.5, gap=10)
b.ex("B1", "完成句子", "周五", "10月23日は金曜日 — 周五。",
     "10月23日是星期五,也可以说___。霜降在这天。", instr="空所補充", size=20.5, gap=10)
b.para("もう二つ：凌晨（língchén）は真夜中過ぎから夜明け前の時間帯；傍晚（bàngwǎn）は暗くなる直前の短い時間です。", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 读新闻 · ニュースの読み方", 24)
c.para("争い（争议）のある話題では、文を3種類に分けましょう：ネットの主張（说法）、公式の発表（声明）、市場のデータ（数据）。主張は大げさになることがあります；データには出典と日付が必要です。6ページが例です：「暴跌40%」は主張、77.5元と57.5元はデータ、「崩盘不实」は発表です。", 21.5)
c.glossline("数字ごとに聞きましょう：誰が、いつ測ったのか？") 
c.ex("B2", "单选", "C", "「暴跌40%」はネットの主張で、実測データではない。",
     "「暴跌超过40%」在第6版里是什么? A. 数据 · B. 声明 · C. 网上的说法", size=20.5, gap=10)
c.ex("B2", "完成句子", "声明", "声明 shēngmíng — 協会の公式発表。",
     "协会10月19日发表___,说「崩盘」不是真的。", instr="空所補充", size=20.5, gap=10)
c.ex("B2", "单选", "B", "データと出典が先、見出しは後。",
     "读新闻时,哪个做法最好? A. 只看标题 · B. 先看数据和出处 · C. 只看评论", size=20.5, gap=10)
c.ex("B2", "完成句子", "25.8", "6ページで実際に計算した下落率は25.8%。",
     "第6版真正算出的数据降幅是___%。", instr="空所補充", size=20.5, gap=10)
c.para("自分でやってみましょう：1ページのホット検索欄で、「第 8 位」は順位 — データです。見出しの言葉は主張です。区別できますか？", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「他高兴的跳起来」", "→ 「他高兴地跳起来。」", "地（de）は動作の様子を表し、動詞の前に置きます。"),
    ("「他跑的很快」", "→ 「他跑得很快。」", "得（de）は動詞と程度の補語をつなぎます：跑得快。"),
    ("「我买了三只大闸蟹个」", "→ 「我买了三只大闸蟹。」", "順番：数 + 量詞 + 名詞。最後の个は余分です；カニには只を使います。"),
    ("「霜降在星期五十月二十三日」", "→ 「霜降在10月23日,星期五。」", "時刻は大→小：月と日が先、曜日は最後。"),
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
wt = "「先付定金，后付尾款。」（まず手付金、次に残金。）型「先…后/再…」は動作の順番を表します。ほかにも：「先看天气，再出门。」「先洗手，再吃饭。」"
wcn = "型：先 … 后/再 … — まずX、それからY。自分の文を作ってみよう。"
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本周句式 · 今週の文型", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「你好!我住在多伦多。霜降那天,我吃了柿子,也给妈妈打了电话。我的购物车里有一件外套,还在等付尾款。」"
lcn = "編集部が作った例文の手紙で、本物ではありません。VOL.2では本物の読者の手紙と、8ページ作文の最優秀作を載せます！"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
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
    ("「今年的双11来得早」", "今年の双11は早く来た。", "p. 1"),
    ("「付完尾款，快递就开始送货了」", "残金を払い終えると、配送が始まる。", "p. 1"),
    ("「付完尾款，商家就发货」", "残金を払うと、お店が出荷する。", "p. 2"),
    ("「遥知兄弟登高处，遍插茱萸少一人」", "王維の有名な重阳の詩句。", "p. 3"),
    ("「两个分数只差2.735分」", "二つのスコアの差はわずか2.735点。", "p. 4"),
    ("「最大的看点是詹姆斯」", "最大の見どころはレブロン。", "p. 4"),
    ("「看S16，要通宵了」", "S16を見るのは徹夜ということ。", "p. 5"),
    ("「先看数据，再看标题」", "データが先、見出しは後（6ページのルール）。", "p. 6"),
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
p.text(MX + 28, py + 44, "下期预告 · 来週予告（VOL.2）", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "S16 瑞士轮打完了:LPL 的四支队打得怎么样?双11 的包裹都到了吗?我们追踪报道。11月7日是立冬,冬天要来了。还有你们的来信和第 8 版最佳作文。下周见!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-ciyu.svg")
print("P7 saved, exercises so far:", len(REG))
