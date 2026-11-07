# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-cn-ja-proof/work/repro-build/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · 文化 (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("文化 · 文化特集", "Lucerna", "レベル A2→B1 · 立冬:冬天的第一个节气 · 冬の最初の節気")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-feature")
f.title("立冬到了,冬天要来了", 37)
f.byline("Lucerna 編集部 · 読解レベル A2→B1")
f.para("11月7日星期六,是立冬。立冬是二十四节气里的第十九个,也是冬天的第一个节气。这一天17点52分交节,冬天正式开始。")
f.para("立冬有三候:一候水始冰,二候地始冻,三候雉入大水为蜃。简单说:水开始结冰,地开始上冻,野鸡不多见了。古人说,雉变成了大蛤,这是古人的想象,不是真的变化。")
f.para("立冬的吃法,各地不一样。北方很多地方吃饺子,因为饺子和交子同音,是秋冬交替的意思。南方有的地方吃鸡鸭鱼肉,有的地方吃汤圆、糍粑,还有的地方喝羊肉汤。没有一种吃法是全国统一的。")
f.para("立冬以后,天气会一天比一天冷,但不是每个地方同时变冷。南方有的地方立冬还很暖和,北方有的地方已经下雪了。出门以前,先看天气预报,加衣服,别着凉。")
f.para("11月8日星期日是中国记者节。记者的工作是采访和写新闻:去现场看一看,问一问,再把事情写清楚。写新闻的时候,时间、地点、数字都要写对。")
f.gloss("hòu 候 — 5日間の小さな季節（候） · jiāotì 交替 — あるものが別のものに取って代わること · cǎifǎng 采访 — インタビューし、現場から報道すること。")
f.head("冬天第一天,做什么好", 25)
f.para("立冬那天,可以做三件事:加一件厚衣服,吃一顿热饭,给家人打一个电话。冬天来了,身体暖和,心里也暖和。")
f.gloss("hòu yīfu 厚衣服 — 暖かい服 · rè fàn 热饭 — 温かい食事 · zháoliáng 着凉 — 風邪をひくこと。")
f.end_report()

# col 3: frost + facts + dumplings + 你呢
ix = COLX[3]
image(p, "frost.jpg", ix, 200, CW, 185)
cy3 = caption(p, ix, 385, CW, "带霜的红叶。霜降已过,立冬要来,早上能看见白白的霜。",
              "Photo: Gerda Arendt — CC0 (Wikimedia Commons)")
facts = ["11月7日星期六 — 立冬,冬天第一个节气",
         "11月7日 17:52 — 立冬交节",
         "11月8日星期日 — 中国记者节"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "节日小日历 · 祭りの日付", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ay3 = sy3 + sh + 26
image(p, "dumplings.jpg", ix, ay3, CW, 200)
cy4 = caption(p, ix, ay3 + 200, CW, "饺子(资料图)。北方很多地方立冬吃饺子。",
              "Photo: Syced — CC0 (Wikimedia Commons)")
ey3 = cy4 + 18
etvous = "你呢?立冬那天,你想吃什么?你住的地方冷不冷?写两句中文寄来。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("あなたは？立冬には何を食べる？あなたの住む所は寒い？中国語で2文書こう。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "说说你自己 · あなたは？", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "あなたは？立冬には何を食べる？あなたの住む所は寒い？中国語で2文書こう。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "练习 · 練習問題", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答えは8ページ · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · 读一读选一选 · 読んで選ぼう", 25)
e.glossline("3ページを読んで、いちばん良い答えを選ぼう。")
e.ex("A2", "单选", "A", "立冬は24節気のうち19番目。",
     "立冬是第几个节气? A. 第19个 · B. 第18个 · C. 第24个", size=19, gap=6)
e.ex("A2", "单选", "B", "立冬は11月7日（土）。",
     "立冬在11月几日? A. 11月1日 · B. 11月7日 · C. 11月11日", size=19, gap=6)
e.ex("A2", "单选", "A", "最初の候：水が凍り始める。",
     "立冬一候是什么? A. 水始冰 · B. 地始冻 · C. 雉入大水为蜃", size=19, gap=6)
e.ex("A2", "单选", "B", "北の家庭は立冬に餃子を食べる。",
     "北方立冬吃什么? A. 汤圆 · B. 饺子 · C. 月饼", size=19, gap=6)
e.ex("A2", "单选", "A", "記者は人にインタビューし、ニュースを書く。",
     "记者的工作是什么? A. 采访和写新闻 · B. 只管卖东西 · C. 只管做饭", size=19, gap=6)
e.head("B · 词语填空 · 単語を入れよう", 25)
e.glossline("空欄に合う言葉を入れよう。")
e.ex("A2", "完成句子", "立冬", "lìdōng — 立冬、11月7日。",
     "11月7日是___。", instr="空欄に入れよう", size=19, gap=6)
e.ex("A2", "完成句子", "水始冰", "shuǐ shǐ bīng — 水が凍り始める（第1候）。",
     "立冬一候是___。", instr="空欄に入れよう", size=19, gap=6)
e.ex("A2", "完成句子", "饺子", "jiǎozǐ — 北方の家庭が立冬に食べるもの。",
     "北方很多地方立冬吃___。", instr="空欄に入れよう", size=19, gap=6)
e.ex("B1", "完成句子", "汤圆", "tāngyuán — 南方の一部の地方で食べられるもち米の団子。",
     "南方有的地方吃___。", instr="空欄に入れよう", size=19, gap=6)
e.ex("B1", "完成句子", "记者", "jìzhě — インタビューしてニュースを書く記者。",
     "采访和写新闻的人,叫___。", instr="空欄に入れよう", size=19, gap=6)
e.head("C · 数字与日期 · 数字と日付", 25)
e.glossline("3ページの日付と数字で答えよう。")
e.ex("A2", "完成句子", "19", "立冬は19番目の節気。",
     "立冬是第___个节气。", instr="空欄に入れよう", size=19, gap=6)
e.ex("A2", "完成句子", "7", "立冬は11月7日。",
     "立冬在11月___日。", instr="空欄に入れよう", size=19, gap=6)
e.ex("B1", "完成句子", "52", "節気の瞬間は17時52分。",
     "立冬交节在17点___分。", instr="空欄に入れよう", size=19, gap=6)
e.ex("A2", "完成句子", "8", "記者節は11月8日。",
     "中国记者节在11月___日。", instr="空欄に入れよう", size=19, gap=6)
e.head("D · 词语配对 · ペアにしよう", 25)
e.match_set("A2", "词汇配对",
            ["水始冰", "地始冻", "雉入大水为蜃", "补冬"],
            ["冬天以前吃点好的",
             "水面结了薄冰",
             "地开始上冻",
             "古人说雉变成了大蛤"],
            ["b", "c", "d", "a"],
            ["水始冰 = 水が凍り始める、b", "地始冻 = 地面が凍り始める、c", "雉入大水为蜃 = 昔のキジの話、d", "bǔdōng 补冬 = 冬に備えてしっかり食べる、a"],
            instr="ペアにしよう")
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-wenhua.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · 体育 (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("体育 · スポーツ", "Lucerna", "レベル B1 · S16 瑞士轮与淘汰赛 · Worlds S16：スイスステージと決勝トーナメント")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1180, tag="P4-feature")
f.title("S16:一支队出局,三支队冲八强", 37)
f.byline("Lucerna 編集部 · 読解レベル B1")
f.para("《英雄联盟》全球总决赛S16正在美国得克萨斯州的艾伦市举行。瑞士轮从10月24日打到11月1日,四分之一决赛在11月4日到7日,半决赛在11月8日到9日,都是北京时间早上6点开始。")
f.para("先说坏消息:中国LPL赛区的一号种子AL出局了。AL先输给KC,又在内战里输给TES,最后0比2输给北美TL,三场都输了,小局一场没赢,止步16强。")
f.para("再说好消息:IG和TES在10月26日都赢了。IG打赢了HLE,TES一度落后,后来翻盘打赢了G2,两支队都是2胜1负,进了2胜1负组。BLG也打赢了KC,同样是2胜1负。三支队离八强只差一场BO3的胜利。")
f.para("瑞士轮怎么打?赢的队和赢的队打,输的队和输的队打。先赢三场的队进淘汰赛,输三场的队回家。第四轮在10月29日到31日打,全部是BO3:IG对LYON,BLG对TES,还有MKOI对T1。")
f.para("本期截稿时是10月27日,第四轮还没有打。所以,四分之一决赛的对手,要等瑞士轮打完才知道。这一周,早上6点看比赛的人,又要早起了。")
f.para("总决赛在11月14日举行,地点是纽约的巴克莱中心。换成北京时间,是11月15日凌晨3点。想看决赛的人,要先安排好睡觉的时间。")
f.gloss("tǎotài 淘汰 — 敗退させる、淘汰すること · nèizhàn 内战 — 同じ地域の2チームの対戦 · zhǐbù 止步 — ここで止まる、それ以上進めないこと。")
f.end_report()

# ---- schedule (cols 0-2) ----
ly = 1210
p.text(MX, ly + 26, "S16 赛程 · S16日程（北京時間）", 26, "sans", True, OLIVE)
p.hline(MX, COLX[2] + CW, ly + 40, GOLD, 2)
sched = [
    "瑞士轮第四轮 — 10月29日—31日,北京时间凌晨4点起,BO3",
    "四分之一决赛 — 11月4日—7日,北京时间早上6点",
    "半决赛 — 11月8日—9日,北京时间早上6点",
    "总决赛 — 北京时间11月15日凌晨3点,纽约",
]
syy = ly + 72
for s_ in sched:
    syy = p.para(MX, syy + 22, s_, 22, "serif", False, INK, 1388, 1.4) + 6
p.para(MX, syy + 14, "2026年10月27日時点の順位：GENとDKはすでに3勝0敗で通過、ALとTSWは0勝3敗で敗退。出典：Sina Sports S16ガイド（北京時間）と10月26～27日の試合報道。", 20.5, "serif", False, GREY, 1388, 1.4)

# col 3: lan party + facts + match words
ix = COLX[3]
image(p, "lanparty.jpg", ix, 200, CW, 220)
cy3 = caption(p, ix, 420, CW, "一起打游戏的老照片(2003 年,法国)。今天看比赛,更多人是在网上一起看直播。",
              "Photo: Syced — CC0 (Wikimedia Commons)")
facts = ["10月26日 — IG胜HLE,TES胜G2",
         "10月27日 — AL三连败出局",
         "11月4日—7日 — 四分之一决赛",
         "11月15日 03:00 — 总决赛(北京时间)"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "体育小日历 · スポーツ日程", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ay3 = sy3 + sh + 26
mwords = [("通宵", "tōngxiāo — 試合のために一晩中起きていること。"),
          ("加油", "jiāyóu — がんばれ！（ファンの声援）。"),
          ("翻盘", "fānpán — 逆転勝利、試合をひっくり返すこと。")]
mh = 62 + sum(len(wrap(m[0] + " " + m[1], "serif", False, 21.5, CW - 44)) * 30.5 + 14 for m in mwords) + 30
p.rect(ix, ay3, CW, mh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ay3 + 16
p.text(ix + 22, yy3 + 26, "看比赛的中文 · 観戦の中国語", 24, "sans", True, OLIVE)
yy3 += 52
for w_, d_ in mwords:
    yy3 = p.para(ix + 22, yy3 + 21, w_ + " " + d_, 21.5, "serif", False, INK, CW - 44, 1.42) + 8
print("P4 col3 ends", ay3 + mh)

# ---- P4 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "练习 · 練習問題", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答えは8ページ · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A · 读一读选一选 · 読んで選ぼう", 25)
e.glossline("4ページを読んで、いちばん良い答えを選ぼう。")
e.ex("B1", "单选", "A", "スイスステージはテキサス州アレンで行われる。",
     "瑞士轮在哪个城市? A. 艾伦 · B. 洛杉矶 · C. 纽约", size=19, gap=6)
e.ex("B1", "单选", "A", "ALはスイスステージの3シリーズすべてに負けた。",
     "AL为什么出局? A. 一场都没赢 · B. 赢了三场 · C. 没有参加", size=19, gap=6)
e.ex("B1", "单选", "B", "IGは10月26日にHLEに勝った。",
     "IG打赢了哪个队? A. G2 · B. HLE · C. KC", size=19, gap=6)
e.ex("B1", "单选", "B", "準々決勝は北京時間6時に始まる。",
     "四分之一决赛在北京时间几点? A. 凌晨1点 · B. 早上6点 · C. 晚上8点", size=19, gap=6)
e.ex("B1", "单选", "B", "決勝は11月15日北京時間3時に始まる。",
     "总决赛在北京时间哪天? A. 11月14日 · B. 11月15日凌晨3点 · C. 11月8日", size=19, gap=6)
e.head("B · 词语填空 · 単語を入れよう", 25)
e.glossline("空欄に合う言葉を入れよう。")
e.ex("B1", "完成句子", "艾伦", "Àilún — テキサス州アレン、スイスステージの開催地。",
     "瑞士轮在美国___市举行。", instr="空欄に入れよう", size=19, gap=6)
e.ex("B1", "完成句子", "内战", "nèizhàn — ALはLPL同士の対戦でTESに負けた。",
     "AL在___里输给了TES。", instr="空欄に入れよう", size=19, gap=6)
e.ex("B1", "完成句子", "淘汰", "táotài — 3勝すると決勝トーナメントに進める。",
     "先赢三场的队进___赛。", instr="空欄に入れよう", size=19, gap=6)
e.ex("B1", "完成句子", "翻盘", "fānpán — TESはG2戦を逆転した。",
     "TES打赢G2,是一场___。", instr="空欄に入れよう", size=19, gap=6)
e.ex("B1", "完成句子", "加油", "jiāyóu — ファンが自分のチームにかける声援。",
     "看比赛时,观众喊___。", instr="空欄に入れよう", size=19, gap=6)
e.head("C · 读赛程 · 日程を読み取ろう", 25)
e.glossline("4ページの日程表を読もう。")
e.ex("B1", "完成句子", "3", "スイスステージからは3勝で勝ち抜けられる。",
     "先赢___场进淘汰赛。", instr="空欄に入れよう", size=19, gap=6)
e.ex("B1", "完成句子", "6", "準々決勝は北京時間6時に始まる。",
     "四分之一决赛在早上___点。", instr="空欄に入れよう", size=19, gap=6)
e.ex("B1", "完成句子", "0", "ALはスイスステージで1シリーズも勝てなかった。",
     "AL一场都没赢,战绩是___胜3负。", instr="空欄に入れよう", size=19, gap=6)
e.ex("B1", "完成句子", "1", "スイスステージは11月1日まで続く。",
     "瑞士轮打到11月___日。", instr="空欄に入れよう", size=19, gap=6)
e.head("D · 词语配对 · ペアにしよう", 25)
e.match_set("B1", "词汇配对",
            ["瑞士轮", "内战", "淘汰赛", "总决赛"],
            ["最后一场比赛,决定冠军",
             "输了就回家的比赛",
             "同一个赛区的两支队打",
             "按胜负分组打的比赛"],
            ["d", "c", "b", "a"],
            ["瑞士轮 = スイスステージ、d", "内战 = 同じ地域同士の対戦、c", "淘汰赛 = 負けたら帰る、b", "总决赛 = 決勝、a"],
            instr="ペアにしよう")
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-tiyu.svg")
print("P4 saved, exercises so far:", len(REG))
