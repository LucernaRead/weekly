# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zhcn-vol1/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · 青年 (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("青年 · Youth", "Lucerna", "Level B1 · 电竞 S16 · 维密秀 · 红包口令 · Worlds S16 & the fashion show")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-feature")
f.title("看S16要通宵了", 37)
f.byline("Lucerna editors · Reading level B1")
f.para("《英雄联盟》全球总决赛 S16 正在美国举行。比赛从10月15日到11月14日,在三个城市打:洛杉矶、艾伦和纽约。")
f.para("10月15日到18日是入围赛,在洛杉矶。10月23日到31日是瑞士轮,在得克萨斯州的艾伦市。11月初,还是在艾伦打淘汰赛。")
f.para("总决赛在11月14日举行,地点是纽约的巴克莱中心。换成北京时间,是11月15日凌晨3点。难怪网友说:「看S16,要通宵了!」")
f.para("今年有19支队。中国的 LPL 赛区有四支队:AL、BLG、TES 和 IG。四支队都从瑞士轮开始打。")
f.para("瑞士轮怎么打?赢的队和赢的队打,输的队和输的队打。先赢三场的队进淘汰赛,输三场的队回家。所以每一场都很重要。")
f.para("北京时间10月24日凌晨1点,第一场瑞士轮比赛开始;后面的比赛,有的在凌晨4点开始。想看比赛的人,要早点睡觉,或者准备好咖啡。")
f.gloss("quánqiú zǒngjuésài 全球总决赛 — the World Championship (Worlds) · rùwéi 入围 — to make the cut · tōngxiāo 通宵 — to stay up all night.")
f.head("维密秀:刘雯第十次走秀", 25)
f.para("10月19日星期一早上7点30分(北京时间),维多利亚的秘密时装秀在洛杉矶举行,还在网上直播。")
f.para("中国模特刘雯也走秀了。这是她第十次走上维密的舞台。对中国观众来说,她的出场是最大的看点之一。")
f.para("这场秀在洛杉矶举行,换成北京时间是早上7点30分。很多中国观众一大早就在手机上看直播,一边看,一边在网上聊天。")
f.gloss("zǒuxiù 走秀 — to walk the runway · mótè 模特 — a fashion model · zhíbō 直播 — a livestream.")
f.box("这一周的高频词 · Words of the week", [
    ("红包口令 — a code word a shop gives out: type it into the shopping app and you can collect a red packet.", "serif", False, INK, 20, 1.35),
    ("双11 期间,大家在群里互相发口令,一起领红包。", "serif", False, INK, 20, 1.35),
])
f.end_report()

# col 3: lan party + S16 calendar + 你呢
ix = COLX[3]
image(p, "lanparty.jpg", ix, 200, CW, 220)
cy3 = caption(p, ix, 420, CW, "一起打游戏的老照片(2003 年,法国)。今天看比赛,更多人是在网上一起看直播。",
              "Photo: Syced — CC0 (Wikimedia Commons)")
facts = ["10月23日—31日 — 瑞士轮(美国艾伦)",
         "北京时间10月24日 01:00 — 瑞士轮第一场",
         "11月14日 — 总决赛(纽约)",
         "北京时间11月15日 03:00 — 总决赛开打"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "S16 小日历 · S16 dates", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "你呢?你会为了看比赛通宵吗?你最喜欢哪支队?写两句中文寄来。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("And you? Would you stay up all night for a match? Which team do you support? Write two sentences in Chinese.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "说说你自己 · And you?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "And you? Would you stay up all night for a match? Which team do you support? Write two sentences in Chinese.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "练习 · Exercises", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Answers on page 8 · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · 读一读选一选 · Read & choose", 25)
e.glossline("Read page 5 and choose the best answer.")
e.ex("B1", "单选", "A", "S16 (Worlds 2026) is being played in the USA.",
     "S16 在哪个国家举行? A. 美国 · B. 中国 · C. 韩国", size=19, gap=6)
e.ex("B1", "单选", "B", "The Swiss stage is played in Allen, Texas.",
     "瑞士轮在哪个城市? A. 洛杉矶 · B. 艾伦 · C. 纽约", size=19, gap=6)
e.ex("B1", "单选", "A", "The final starts at 03:00 Beijing time on Nov 15.",
     "总决赛在北京时间几点? A. 11月15日凌晨3点 · B. 10月24日凌晨1点 · C. 11月14日晚上8点", size=19, gap=6)
e.ex("B1", "单选", "B", "The LPL sends four teams: AL, BLG, TES, IG.",
     "LPL 有几支队打 S16? A. 三支 · B. 四支 · C. 十九支", size=19, gap=6)
e.ex("B1", "单选", "A", "The fashion show streamed on Mon Oct 19, Beijing time.",
     "维密秀在北京时间哪天直播? A. 10月19日 · B. 10月20日 · C. 11月14日", size=19, gap=6)
e.head("B · 词语填空 · Word blanks", 25)
e.glossline("Fill each blank with the right word.")
e.ex("B1", "完成句子", "通宵", "tōngxiāo — staying up all night for a match.",
     "看比赛看到天亮,这叫___。", instr="Fill in", size=19, gap=6)
e.ex("B1", "完成句子", "入围", "rùwéi — the play-in stage comes first.",
     "S16 的第一个阶段是___赛。", instr="Fill in", size=19, gap=6)
e.ex("B1", "完成句子", "走秀", "zǒuxiù — Liu Wen walked the runway a 10th time.",
     "刘雯是第十次上台___。", instr="Fill in", size=19, gap=6)
e.ex("B1", "完成句子", "口令", "kǒulìng — type the code word to get a red packet.",
     "在 App 里输入___,就能领红包。", instr="Fill in", size=19, gap=6)
e.ex("A2", "完成句子", "四", "Four LPL teams play at S16.",
     "十九支队里,LPL 有___支。", instr="Fill in", size=19, gap=6)
e.head("C · 时间换算 · Time zones", 25)
e.glossline("Convert the times to Beijing time.")
e.ex("B1", "完成句子", "15", "Nov 14 in New York is Nov 15 in Beijing.",
     "总决赛在美国时间11月14日,北京时间是11月___日。", instr="Fill in", size=19, gap=6)
e.ex("A2", "完成句子", "1", "The first Swiss game starts at 01:00 Beijing time.",
     "瑞士轮第一场在北京时间凌晨___点。", instr="Fill in", size=19, gap=6)
e.ex("B1", "完成句子", "4", "Some later games start at 04:00 Beijing time.",
     "后面的比赛,有的在凌晨___点开始。", instr="Fill in", size=19, gap=6)
e.ex("B2", "完成句子", "难怪", "难怪 nánguài — no wonder people stay up all night.",
     "比赛在凌晨三点开始,___网友说要通宵。", instr="Fill in", size=19, gap=6)
e.head("D · 词语配对 · Matching", 25)
e.match_set("B1", "词汇配对",
            ["入围赛", "瑞士轮", "淘汰赛", "总决赛"],
            ["最后一场比赛,决定冠军",
             "输了就回家的比赛",
             "第一阶段的比赛",
             "按胜负分组打的比赛"],
            ["c", "d", "b", "a"],
            ["入围赛 = the first stage, c", "瑞士轮 = the Swiss stage, d", "淘汰赛 = loser goes home, b", "总决赛 = the final, a"],
            instr="Match the words")
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-qingnian.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · 深读 (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("深读 · Deep read", "Lucerna", "Level B2 · 大闸蟹价格争议 · Is the crab price really crashing?")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1180, tag="P6-feature")
f.title("大闸蟹「价格崩盘」,是真的吗?", 37)
f.byline("Lucerna editors · Reading level B2")
f.para("这几天,网上有文章说:大闸蟹「全面滞销」,价格「暴跌超过40%」。大闸蟹真的卖不动了吗?我们查了数据,也看了行业里的说法。")
f.para("先看价格。北京新发地市场的数据说:中秋节那天,约三两的母蟹平均77.5元一斤。10月6日,价格是57.5元一斤。10月15日以后,价格触底,又慢慢涨回来。")
f.para("从77.5元到57.5元,便宜了20元,大约是25.8%。这个数字,比网上的「暴跌40%」小得多。")
f.para("苏州阳澄湖大闸蟹行业协会10月18日发了通知,10月19日又发表声明:所谓「崩盘」不是真的。只有少数外围产区的蟹卖得慢一点;真正的阳澄湖大闸蟹,供求基本稳定,出水价和最近三年差不多。")
f.gloss("zhìxiāo 滞销 — to sell badly, to sit unsold · bàodiē 暴跌 — to plunge (of prices) · bēngpán 崩盘 — a market crash · gōngqiú 供求 — supply and demand.")
f.para("今年阳澄湖大闸蟹9月28日开捕,预计总产量约1.01万吨。吃蟹也有学问:蟹黄是母蟹的卵,蟹膏是公蟹的精。老话说「九月圆脐十月尖」:农历九月吃母蟹(圆脐),十月吃公蟹(尖脐)。")
f.para("还有一个老话题:蟹券。有人买蟹券送人,券常常换不到蟹,或者换到小蟹。买蟹券之前,要先问清楚。")
f.para("结论:价格确实降了一点,但「崩盘」是夸张的说法。读新闻的时候,先看数据,再看标题。")
f.gloss("kāibǔ 开捕 — the fishing season opens · chǎnliàng 产量 — total output · xièquàn 蟹券 — a crab gift voucher · kuāzhāng 夸张 — exaggerated.")
f.end_report()

# ---- price chart (cols 0-2), bars exactly proportional from zero ----
ly = 1210
p.text(MX, ly + 26, "新发地批发价:约三两母蟹(元/斤)· Xinfadi wholesale prices", 26, "sans", True, OLIVE)
p.hline(MX, COLX[2] + CW, ly + 40, GOLD, 2)
rows = [("中秋节当天", 77.5), ("10月6日", 57.5)]
SCALE = 6.0
by0 = ly + 66
for i, (name, val) in enumerate(rows):
    yy = by0 + i * 64
    p.text(MX, yy + 34, name, 24, "sans", True, INK)
    bw_ = val * SCALE
    p.rect(MX + 190, yy + 6, bw_, 34, fill=OLIVE if i == 0 else GOLD)
    p.text(MX + 190 + bw_ + 16, yy + 34, f"{val} 元/斤", 24, "serif", True, INK)
p.para(MX, by0 + 2 * 64 + 22, "Bars are drawn from 0 (6 px = 1 yuan). Prices bottomed out and rose again after Oct 15; reports gave no figure for the rebound, so no bar is drawn for it. Sources: 新浪财经 (Sina Finance) and 华龙网 (2026-10-20); 中华网 (2026-10-10).", 20.5, "serif", False, GREY, 1388, 1.4)

# col 3: crab + facts + minicrabs
ix = COLX[3]
image(p, "crab.jpg", ix, 200, CW, 240)
cy3 = caption(p, ix, 440, CW, "切开的大闸蟹:橙色的部分是蟹黄。吃蟹的季节,就是现在。",
              "Photo: Fumikas Sagisavas — CC0 (Wikimedia Commons)")
facts = ["阳澄湖 9 月 28 日开捕",
         "预计总产量约 1.01 万吨",
         "九月圆脐,十月尖"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "蟹的小知识 · Crab facts", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ay3 = sy3 + sh + 26
image(p, "minicrabs.jpg", ix, ay3, CW, 200)
caption(p, ix, ay3 + 200, CW, "小蟹排排队。买蟹时,要问清大小和重量,别只看价格。",
        "Photo: Fumikas Sagisavas — CC0 (Wikimedia Commons)")
print("P6 col3 ends", ay3 + 300)

# ---- P6 exercises ----
ey = 1560
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "练习 · Exercises", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Answers on page 8 · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · 读一读选一选 · Read & choose", 25)
e.glossline("Read page 6 and choose the best answer.")
e.ex("B2", "单选", "B", "Online posts claimed prices had plunged over 40%.",
     "网上的文章说大闸蟹价格怎么样? A. 涨了40% · B. 暴跌超过40% · C. 完全没变", size=19, gap=6)
e.ex("B2", "单选", "A", "The Xinfadi price fell to 57.5 yuan per jin.",
     "新发地的数据说,10月6日价格是多少? A. 57.5元 · B. 40元 · C. 77.5元", size=19, gap=6)
e.ex("B2", "单选", "B", "The association said the 'crash' story is not true.",
     "协会的声明说什么? A. 蟹都卖完了 · B. 「崩盘」不是真的 · C. 今年没有蟹", size=19, gap=6)
e.ex("B2", "单选", "B", "20 ÷ 77.5 ≈ 25.8% — the real drop.",
     "真正算一下,价格大约降了多少? A. 40% · B. 25.8% · C. 2.58%", size=19, gap=6)
e.ex("B2", "单选", "A", "The Yangcheng Lake season opened on Sep 28.",
     "阳澄湖大闸蟹什么时候开捕? A. 9月28日 · B. 10月18日 · C. 中秋节当天", size=19, gap=6)
e.head("B · 词语填空 · Word blanks", 25)
e.glossline("Fill each blank with the right word.")
e.ex("B2", "完成句子", "滞销", "zhìxiāo — goods that will not sell.",
     "东西卖不动,叫___。", instr="Fill in", size=19, gap=6)
e.ex("B2", "完成句子", "暴跌", "bàodiē — a sharp price plunge.",
     "价格一下子降很多,叫___。", instr="Fill in", size=19, gap=6)
e.ex("B2", "完成句子", "供求", "gōngqiú — supply and demand, basically stable.",
     "市场的___基本稳定,价格就不会大变。", instr="Fill in", size=19, gap=6)
e.ex("B2", "完成句子", "产量", "chǎnliàng — expected output is about 10,100 tonnes.",
     "今年阳澄湖大闸蟹预计总___约1.01万吨。", instr="Fill in", size=19, gap=6)
e.ex("B2", "完成句子", "夸张", "kuāzhāng — the 'crash' headline is exaggerated.",
     "「崩盘」的说法太___了。", instr="Fill in", size=19, gap=6)
e.head("C · 数字与计算 · Do the maths", 25)
e.glossline("Compute from the prices on page 6.")
e.ex("B2", "完成句子", "20", "77.5 − 57.5 = 20 yuan cheaper.",
     "77.5 − 57.5 = ___元。", instr="Fill in", size=19, gap=6)
e.ex("B2", "完成句子", "25.8", "20 ÷ 77.5 ≈ 0.258, i.e. about 25.8%.",
     "20 ÷ 77.5 ≈ ___%。", instr="Fill in", size=19, gap=6)
e.ex("B1", "完成句子", "重量", "三两 describes the crab's weight (about 150 g).",
     "约三两的母蟹,「三两」说的是蟹的___。", instr="Fill in", size=19, gap=6)
e.ex("B1", "完成句子", "10", "The notice came on Oct 18, the statement on Oct 19.",
     "协会___月18日发通知,19日发声明。", instr="Fill in", size=19, gap=6)
e.head("D · 词语配对 · Matching", 25)
e.match_set("B2", "词汇配对",
            ["蟹黄", "蟹膏", "蟹券", "圆脐"],
            ["买蟹的礼品券",
             "母蟹的肚脐形状",
             "母蟹的卵,橙色",
             "公蟹的精,白色黏黏的"],
            ["c", "d", "a", "b"],
            ["蟹黄 = the female's orange roe, c", "蟹膏 = the male's milt, d", "蟹券 = a gift voucher, a", "圆脐 = the female's round apron, b"],
            instr="Match the words")
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-shendu.svg")
print("P6 saved, exercises so far:", len(REG))
