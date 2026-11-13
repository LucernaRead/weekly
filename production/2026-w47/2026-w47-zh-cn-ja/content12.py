# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-zh-cn-ja/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · 头版 (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 4　第4号", 17, "sans", True, OLIVE, spacing=1.7)
p.text(975, 92, "每周读中文　本物の中国語を毎週読もう", 17, "sans", False, GREY, anchor="middle", spacing=1.7)
p.text(RIGHT, 92, "2026年11月16日—22日", 17, "sans", False, GREY, anchor="end", spacing=1.7)
p.text(975, 262, "Lucerna", 196, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "简体中文版　VOL.4　S16决赛　包裹到了　小雪", 36, "serif", True, OLIVE, anchor="middle", spacing=11.5)
p.text(975, 372, "给学中文的人的周报 — 本物の中国を中国語で読む", 16, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)
# pairing badge: which text, which explanation language, which reader
# (left-aligned so it clears the moth centred on the masthead rule)
p.text(MX, 434, "中国語（簡体字）テキスト　日本語の解説 — 日本語読者のための版", 14, "sans", True, OLIVE)

# band
p.rect(MX, 470, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 30, 524, "决赛来了，BLG打GEN", 46, "sans", True, ONCLOTH)
p.text(MX + 30, 568, "11月15日凌晨3点，纽约巴克莱中心，BO5决出冠军。", 25, "serif", False, "#cac8ba")
p.text(RIGHT - 30, 524, "S16决赛×包裹", 27, "sans", True, GOOSE, anchor="end")
p.text(RIGHT - 30, 568, "決勝と荷物　2ページと4ページを見よう", 18, "sans", False, GOOSE, anchor="end")

# ---- headline (span cols 0-2) ----
hy = 590
p.text(MX, hy + 26, "头条　トップ記事", 17, "sans", True, OLIVE)
hy = p.para(MX, hy + 92, "BLG赢了T1，决赛对阵GEN", 53, "serif", True, INK, 1323, 1.06)
p.text(MX, hy + 28, "Lucerna 編集部　読解レベル A2", 17, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("S16的半决赛打完了。11月8日星期日，GEN 3比0打赢了IG。11月9日星期一，BLG 3比1打赢了T1。决赛是BLG对GEN，北京时间11月15日星期日凌晨3点，在纽约的巴克莱中心打。")
f.para("四分之一决赛先打完：11月4日，IG 3比1打赢TES；11月5日，GEN 3比0打赢LYON；11月6日，BLG 3比0打赢DK；11月7日，T1 3比1打赢KC。全部是BO5，输了就回家。")
f.para("决赛是BO5，五局三胜，先赢三局的队拿冠军。GEN在S16一场没输，只丢了一小局：瑞士轮3胜0负，八强3比0，半决赛3比0。BLG一路打赢了三支韩国队：瑞士轮打赢HLE，八强打赢DK，半决赛打赢T1。")
f.para("本期截稿时是11月10日，总决赛还没打。谁是冠军？下一期再报。想看决赛的人，记得调好闹钟：北京时间11月15日凌晨3点，正是半夜。")
f.para("这一周还有两件大事：双11的包裹还在路上，11、12、13日三天是高峰；11月22日星期日是小雪，冬天更冷了。")
f.para("这是《Lucerna》简体中文版第4号。每周，我们用简单的中文，带你读真正的中国新闻。欢迎你！")
f.gloss("juésài 决赛 — 決勝、最後の試合 · guànjūn 冠军 — 優勝者、勝者 · bànjuésài 半决赛 — 準決勝 · kuàidì 快递 — 速達、宅配便の荷物。")
f.box("数字看本周　今週の数字", [
    ("11月15日03:00 — S16決勝：BLG対GEN（北京時間）", "serif", False, INK, 20, 1.35),
    ("11月11〜13日 — 荷物のピーク：忙しい3日間（11、12、13日）", "serif", False, INK, 20, 1.35),
    ("11月21日（土）— 新作映画《試探》が公開", "serif", False, INK, 20, 1.35),
    ("11月22日（日）— 小雪", "serif", False, INK, 20, 1.35),
])
f.head("即学即练　今すぐ試そう", 25)
f.ex("A2", "完成句子", "T1", "BLGは準決勝でT1に3-1で勝った。",
     "半决赛，BLG 3比1打赢了___。", instr="文を完成させよう", size=20.5, gap=6)
f.ex("A2", "完成句子", "15", "S16決勝は11月15日、北京時間。",
     "决赛在11月___日凌晨3点。", instr="文を完成させよう", size=20.5, gap=6)
f.ex("A2", "完成句子", "巴克莱", "決勝はニューヨーク、ブルックリンのバークレイズ・センター。",
     "决赛在纽约___中心打。", instr="文を完成させよう", size=20.5, gap=6)
f.ex("A2", "完成句子", "三", "BLGは韓国チームに3連勝した。",
     "BLG一路打赢了___支韩国队。", instr="文を完成させよう", size=20.5, gap=6)
f.ex("A2", "完成句子", "22", "小雪は11月22日。",
     "小雪在11月___日。", instr="文を完成させよう", size=20.5, gap=6)
f.ex("A2", "完成句子", "21", "映画《試探》は11月21日公開。",
     "电影《试探》在11月___日上映。", instr="文を完成させよう", size=20.5, gap=6)
f.end_report()

# ---- this-week calendar box (col 3) ----
gx, gw = COLX[3], CW
gy = 588
p.rect(gx, gy, gw, 700, fill=BOX)
p.text(gx + 22, gy + 40, "本周日历　今週", 25, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "11月15日—22日　11月15日〜22日", 22, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "今週の出来事", 19, "sans", False, GREY)
topics = [
    "周日 11月15日 03:00 — S16总决赛，BLG对GEN",
    "11月12日—15日 — 快递配送高峰",
    "周六 11月21日 — 电影《试探》上映",
    "周日 11月22日 — 小雪，冬天更冷了",
    "11月11日—13日 — 包裹揽收高峰",
]
byy = gy + 150
for i, t in enumerate(topics):
    yy_t = p.para(gx + 22, byy + 22, f"{i+1}. {t}", 20, "serif", True, INK, gw - 44, 1.32)
    byy = yy_t + 10
p.para(gx + 22, byy + 12, "締切：11月10日。決勝は11月15日03:00（北京時間）— 締切時点ではまだ行われておらず、優勝者は来週報じます。準決勝（11月8〜9日）は確定した結果です。", 18.5, "sans", False, GREY, gw - 44, 1.35)
p.text(gx + 22, gy + 636, "時刻はすべて北京時間", 18.5, "sans", False, GREY)
p.text(gx + 22, gy + 664, "締切：11月10日 — 決勝はまだ行われていない", 19, "sans", False, GREY)

# ---- contents (col 3) ----
sy = 1312
p.rect(gx, sy, gw, 340, fill=BOX)
p.text(gx + 22, sy + 40, "本期目录　目次", 24, "sans", True, OLIVE)
som = [
    ("2版", "包裹到了吗：收、退、查", "A2"),
    ("3版", "小雪到了，冬天真的来了", "A2→B1"),
    ("4版", "S16：四强打完，决赛见", "B1"),
    ("5版", "新电影《试探》与11月片单", "B1"),
    ("6版", "包裹深读：为什么没爆掉", "B2"),
    ("7版", "词语精讲", "A2→B2"),
    ("8版", "测验与答案", "全部"),
]
yy = sy + 84
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, OLIVE)
    p.text(gx + 72, yy, t, 18, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 40

# ---- word of the week (col 3) ----
my = 1652
p.text(gx, my + 24, "本周词　今週の言葉", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, OLIVE, 2)
p.para(gx, my + 76, "「决赛」 juésài — 決勝、最後の試合。决赛是谁和谁打？赢了就是冠军。", 21.5, "serif", False, INK, gw, 1.4)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "locker.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "快递柜（资料图）。包裹到了，先看取件码，再去快递柜拿。",
        "写真：Map hobby — CC0（Wikimedia Commons）")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2300, tag="P1-week")
f2.head("决赛夜，怎么看", 25)
f2.para("决赛在凌晨3点，是半夜。想看的人，要先睡一觉，再起来看；也可以早上起来看结果。先睡好，再看比赛。", 22.5)
f2.end_report()
# col 3 brief box
bx = COLX[3]
p.rect(bx, 1874, CW, 416, fill=BOX)
p.text(bx + 22, 1914, "快讯　速報", 24, "sans", True, OLIVE)
brefs = [
    ("S16", "半决赛打完：GEN 3比0胜IG，BLG 3比1胜T1。决赛11月15日凌晨3点。（第4版）"),
    ("包裹", "包裹高峰在11、12、13日三天。（第2版）"),
    ("小雪", "11月22日是小雪，冬天更冷了。（第3版）"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, OLIVE)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- lightning quiz ----
qy = 2312
p.hline(MX, RIGHT, qy, OLIVE, 2)
p.text(MX, qy + 36, "闪电问答　クイッククイズ", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "1ページを読んで選ぼう　答案见第8版", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2560, tag="P1-quiz")
qf.ex("A2", "单选", "A", "BLGは準決勝でT1に3-1で勝った。",
      "半决赛，BLG打赢了哪个队？ A. T1 · B. DK · C. LYON", size=21)
qf.ex("A2", "单选", "A", "S16決勝は11月15日03:00（北京時間）。",
      "决赛在北京时间几点？ A. 凌晨3点 · B. 早上6点 · C. 晚上8点", size=21)
qf.ex("A2", "单选", "A", "荷物のピークは11月11〜13日。",
      "包裹高峰是哪几天？ A. 11月11日到13日 · B. 11月12日到15日 · C. 11月21日到22日", size=21)
qf.ex("A2", "单选", "B", "小雪は11月22日。",
      "小雪在哪天？ A. 11月21日 · B. 11月22日 · C. 11月15日", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-touiban.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · 生活 (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("生活　暮らし", "Lucerna", "Level A2　包裹到了吗　天冷了　荷物が届き、寒い日々")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("包裹到了吗？收、退、查", 32)
f.byline("Lucerna 編集部　読解レベル A2")
f.para("双11过去了。包裹都到了吗？去年22天一共揽收139.38亿件，单日最高7.77亿件。今年的高峰在11、12、13日三天，包裹还在路上。")
f.para("今年和往年不一样：往年是11月11日、12日两天最忙，快递量一下子冲到最高；今年，快递量被打散了，从10月下旬一直忙到11月中旬，没有一天突然爆掉。")
f.para("湖南顺丰说，配送高峰在11月12日到15日，人力和运力比平时多了约20%。铁路也帮忙：11月1日开始，高铁急送覆盖196个主要城市，最快4小时门到门。")
f.para("包裹到了，先打开看一看：对不对？有没有坏？有问题，早点联系卖家。东西不合适，想退换货，也要早点寄，别拖到最后。价保不是自动的：想保价，要先看规则，再自己申请。")
f.para("还有一件事：取件码别给别人。快递柜的取件码就是开门的钥匙，别人拿到了，就能把你的包裹拿走。")
f.para("天气也冷了。小雪在11月22日，冬天更冷了。出门加一件厚衣服，晚上早点睡觉，别着凉。")
f.gloss("dàohuò 到货 — （荷物が）届いた · tuìhuànhuò 退换货 — 返品と交換 · jiàbǎo 价保 — 価格保証 · pàisòng 派送 — 届ける、配送 · shēnqǐng 申请 — 申請する。")
f.head("小雪之后，怎么穿", 25)
f.para("小雪之后，天气更冷了。北方很多地方已经开始供暖，家里暖和了。南方没有供暖，出门要多穿一件，晚上睡觉盖好被子。天冷了，先看天气预报，再决定穿什么。")
f.box("練習例　练习例子", [
    ("一件外套 320 元，直降 80 元，实付 240 元。", "serif", False, INK, 20, 1.35),
    ("包邮，运费 0 元。结算页的价格就是实付价。", "serif", False, INK, 20, 1.35),
])
f.head("天冷了，吃什么好", 25)
f.para("天冷的时候，吃点热的，喝点热的，身体暖和。北方吃饺子、喝羊肉汤，南方吃汤圆、喝热汤，都是冬天里的热饭。")
f.para("11月中旬，有的学校还在期中考试，日子各不相同。天冷加考试，更要早点睡觉，别熬夜。")
f.gloss("yángròutāng 羊肉汤 — 羊肉スープ · rètāng 热汤 — 熱いスープ · áoyè 熬夜 — 夜更かしする。")
f.box("本周生活小日历　今週のカレンダー", [
    ("周日 11月15日 03:00 — S16总决赛，BLG对GEN", "serif", False, INK, 20, 1.35),
    ("11月12日—15日 — 快递配送高峰", "serif", False, INK, 20, 1.35),
    ("周六 11月21日 — 电影《试探》上映", "serif", False, INK, 20, 1.35),
])
f.end_report()

# col 3: valley image + facts + 你呢 (sequential, measured)
ix = COLX[3]
image(p, "valley.jpg", ix, 200, CW, 230)
cy3 = caption(p, ix, 430, CW, "秋天的山谷，红叶正当时。天冷了，山里的叶子也要落了。",
              "写真：Paul Gilmore — CC0（Wikimedia Commons）")
facts = ["去年双11 — 22天揽收139.38亿件",
         "单日最高 — 7.77亿件",
         "配送高峰 — 11月12日到15日",
         "高铁急送 — 196个城市，最快4小时"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "你知道吗　知ってる？", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "你呢？这个双11，你买了什么？你的包裹到了吗？写两句中文寄来。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("あなたは？ この双11で何を買いましたか？ 荷物は届きましたか？ 中国語で2文書きましょう。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill=BOX)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "说说你自己　あなたは？", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "あなたは？ この双11で何を買いましたか？ 荷物は届きましたか？ 中国語で2文書きましょう。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- word strip ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, OLIVE, 2)
p.text(MX, dy + 28, "双11词语卡　買い物の言葉", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "どの買い物アプリでも見る4つの言葉", 20, "sans", False, GREY, anchor="end")
words = [
    ("到货", "dàohuò · （荷物が）届いた", "荷物が届いたよ、取りに行こう"),
    ("退换货", "tuìhuànhuò · 返品と交換", "合わなければ早めに送り返そう"),
    ("价保", "jiàbǎo · 価格保証", "自動ではない — 自分で申請しよう"),
    ("派送", "pàisòng · 配送", "配達員があなたに届ける"),
]
for i, (t, lab, en) in enumerate(words):
    bx = COLX[i]
    p.rect(bx, dy + 52, CW, 150, fill=BOX)
    p.text(bx + 22, dy + 106, t, 34, "serif", True, OLIVE)
    yy = p.para(bx + 22, dy + 140, lab, 20.5, "serif", False, INK, CW - 44, 1.32)
    p.para(bx + 22, yy + 19, en, 19, "sans", False, GREY, CW - 44, 1.3)
p.para(MX, dy + 222, "この文を覚えよう：「包裹到了，先看取件码，再去快递柜拿。」", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P2 exercises ----
ey = dy + 250
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "练习　練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答えは 8 ページ　答案见第8版", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P2-ex")
e.head("A　读一读选一选　読んで選ぶ", 25)
e.glossline("2ページを読んでいちばんよい答えを選ぼう。")
e.ex("A2", "单选", "A", "去年のダブルイレブン：22日間で139億3800万個の荷物。",
     "去年双11，22天一共揽收多少件？ A. 139.38亿件 · B. 7.77亿件 · C. 6.34亿件", size=20, gap=6)
e.ex("A2", "单选", "A", "配達のピークは11月12〜15日。",
     "配送高峰在哪几天？ A. 11月12日到15日 · B. 11月9日到11日 · C. 10月20日到21日", size=20, gap=6)
e.ex("A2", "单选", "B", "価格保証は自動ではありません。ルールを確認してから申請しよう。",
     "价保是怎么回事？ A. 自动就有 · B. 要先看规则，再自己申请 · C. 只有11月11日有", size=20, gap=6)
e.ex("A2", "单选", "B", "受け取り確認の前に荷物を開けて確認しよう。",
     "包裹到了，先做什么？ A. 直接确认收货 · B. 先打开看一看 · C. 先放一个月", size=20, gap=6)
e.ex("A2", "单选", "A", "高速鉄道エクスプレス：ドアツードアで最速4時間。",
     "高铁急送最快多久？ A. 4小时 · B. 1天 · C. 3天", size=20, gap=6)
e.head("B　词语填空　単語の穴埋め", 25)
e.glossline("空欄に正しい言葉を入れよう。")
e.ex("A2", "完成句子", "包裹", "bāoguǒ — 荷物。",
     "我的___到了，去快递柜拿。", instr="入れよう", size=20, gap=6)
e.ex("A2", "完成句子", "退换货", "tuìhuànhuò — 返品と交換。早めに送り返そう。",
     "东西不合适，可以___。", instr="入れよう", size=20, gap=6)
e.ex("A2", "完成句子", "申请", "shēnqǐng — 価格保証は自動ではない。申請しよう。",
     "价保不是自动的，要自己___。", instr="入れよう", size=20, gap=6)
e.ex("A2", "完成句子", "派送", "pàisòng — 配達員が荷物を届ける。",
     "快递员正在___包裹。", instr="入れよう", size=20, gap=6)
e.ex("B1", "完成句子", "20", "湖南SFエクスプレスは人員と輸送力を約20％増やした。",
     "湖南顺丰的人力和运力多了约___%。", instr="入れよう", size=20, gap=6)
e.head("C　数字与日期　数字", 25)
e.glossline("このページの練習例を使おう。")
e.ex("A2", "完成句子", "320", "例のコートは320元。",
     "练习例子里，外套___元。", instr="入れよう", size=20, gap=6)
e.ex("A2", "完成句子", "240", "直接値引きで 320 − 80 = 240 元。",
     "直降以后实付___元。", instr="入れよう", size=20, gap=6)
e.ex("B1", "完成句子", "80", "例の直接値引きは80元。",
     "练习例子里直降___元。", instr="入れよう", size=20, gap=6)
e.ex("B1", "完成句子", "7.77", "去年の1日最多は7億7700万件だった。",
     "去年双11，单日最高___亿件。", instr="入れよう", size=20, gap=6)
e.head("D　词语配对　マッチング", 25)
e.match_set("A2", "词汇配对",
            ["到货", "退换货", "价保", "派送"],
            ["东西到了，可以去拿了",
             "东西不合适，寄回去换",
             "降价了，补回差价",
             "快递员把包裹送到你手里"],
            ["a", "b", "c", "d"],
            ["到货 = 荷物が届いた、a", "退换货 = 返品と交換、b", "价保 = 価格保証、c", "派送 = 配送、d"],
            instr="言葉を合わせよう")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-shenghuo.svg")
print("P2 saved, exercises so far:", len(REG))
