# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/zh-cn-fix-round3/gates/freeze-baseline/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · 文化 (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("文化 · Culture", "Lucerna", "Level A2→B1 · 消防日与读书月 · Fire Day & Reading Month")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-feature")
f.title("11月9日,先学会保护自己", 37)
f.byline("Lucerna editors · Reading level A2→B1")
f.para("11月9日星期一,是全国消防日。今年是第35个全国消防日。11月也是消防宣传月,今年的主题是:全民消防、生命至上——提高自防自救能力。")
f.para("为什么是11月9日?因为火警电话是119,11月9日就是119。这一天,很多地方会做疏散自救演练:大家按平时的逃生路线走一走,看看消防站,学一学怎么保护自己。")
f.para("着火的时候,最重要的是人,不是东西。先离开,再求救。着火了不坐电梯,走楼梯。烟很大的时候,低下身子,用湿毛巾捂住口鼻,快点离开。")
f.para("平时也要小心:出门以前,看看电器关了没有;充电的时候,人不要走远;楼道里不要放很多东西,逃生路要一直通着。")
f.para("11月还有一件文化事:深圳读书月。读书月从11月1日开始,主题是悦读深圳、阅连世界。11月14日星期六晚上,深圳市文化馆有文化馆之夜:读者可以亲手摸一摸古籍的装帧,抄一抄,读一读,把看展变成读经典。")
f.gloss("zìfáng 自防 — protecting yourself · zìjiù 自救 — saving yourself, self-rescue · shūsàn 疏散 — to evacuate, to move people out safely · lóudào 楼道 — a corridor, a stairwell passage.")
f.head("冬天里,安全第一", 25)
f.para("冬天来了,天冷了,用火用电也多了。取暖的时候,人不要离开太久;睡觉以前,看看取暖器关了没有。安全第一,比什么都重要。")
f.gloss("qǔnuǎn 取暖 — keeping warm, heating · diànqì 电器 — an electrical appliance · tōng 通 — open, unblocked.")
f.end_report()

# col 3: frost + facts + reading box + 你呢
ix = COLX[3]
image(p, "frost.jpg", ix, 200, CW, 185)
cy3 = caption(p, ix, 385, CW, "带霜的红叶。冬天来了,早上能看见白白的霜,出门要加衣服。",
              "Photo: Gerda Arendt — CC0 (Wikimedia Commons)")
facts = ["11月9日星期一 — 第35个全国消防日",
         "11月 — 消防宣传月",
         "11月14日 — 深圳读书月文化馆之夜"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "节日小日历 · Festival dates", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ay3 = sy3 + sh + 26
rbox = ["读书月:11月1日开始,深圳七个文化场馆一起办活动。",
        "文化馆之夜:11月14日,亲手摸古籍、抄经典。"]
rh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 14 for t in rbox) + 30
p.rect(ix, ay3, CW, rh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ay3 + 16
p.text(ix + 22, yy3 + 26, "读书月 · Reading Month", 24, "sans", True, OLIVE)
yy3 += 52
for t in rbox:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 8
ey3 = ay3 + rh + 26
etvous = "你呢?你参加过消防演练吗?这个月,你在读什么书?写两句中文寄来。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("And you? Have you taken part in a fire drill? What are you reading this month? Write two sentences in Chinese.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "说说你自己 · And you?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "And you? Have you taken part in a fire drill? What are you reading this month? Write two sentences in Chinese.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "练习 · Exercises", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Answers on page 8 · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · 读一读选一选 · Read & choose", 25)
e.glossline("Read page 3 and choose the best answer.")
e.ex("A2", "单选", "A", "Nov 9 is the 35th National Fire Day.",
     "今年是第几个全国消防日? A. 第35个 · B. 第19个 · C. 第24个", size=19, gap=6)
e.ex("A2", "单选", "B", "National Fire Day is on Nov 9.",
     "全国消防日在11月几日? A. 11月1日 · B. 11月9日 · C. 11月11日", size=19, gap=6)
e.ex("A2", "单选", "A", "In a fire, leave first and call for help; do not take the lift.",
     "着火的时候,先做什么? A. 先离开,再求救 · B. 先拿东西 · C. 先坐电梯", size=19, gap=6)
e.ex("A2", "单选", "B", "The Reading Month culture night is on Nov 14.",
     "深圳读书月文化馆之夜在哪天? A. 11月1日 · B. 11月14日 · C. 11月9日", size=19, gap=6)
e.ex("A2", "单选", "A", "Keep the escape route clear — do not block the corridor.",
     "楼道里应该怎么样? A. 逃生路一直通着 · B. 放很多东西 · C. 关上所有的门", size=19, gap=6)
e.head("B · 词语填空 · Word blanks", 25)
e.glossline("Fill each blank with the right word.")
e.ex("A2", "完成句子", "消防", "xiāofáng — fire prevention; Nov 9 is National Fire Day.",
     "11月9日是全国___日。", instr="Fill in", size=19, gap=6)
e.ex("A2", "完成句子", "119", "The fire alarm number is 119.",
     "火警电话是___。", instr="Fill in", size=19, gap=6)
e.ex("A2", "完成句子", "楼梯", "lóutī — in a fire, take the stairs, not the lift.",
     "着火的时候,走___,不坐电梯。", instr="Fill in", size=19, gap=6)
e.ex("B1", "完成句子", "疏散", "shūsàn — an evacuation drill practises the escape route.",
     "消防日那天,很多地方会做___演练。", instr="Fill in", size=19, gap=6)
e.ex("B1", "完成句子", "古籍", "gǔjí — old books; readers can touch the binding of old books.",
     "文化馆之夜,读者可以亲手摸一摸___的装帧。", instr="Fill in", size=19, gap=6)
e.head("C · 数字与日期 · Numbers", 25)
e.glossline("Answer with dates and numbers from page 3.")
e.ex("A2", "完成句子", "35", "This is the 35th National Fire Day.",
     "今年是第___个全国消防日。", instr="Fill in", size=19, gap=6)
e.ex("A2", "完成句子", "9", "National Fire Day is on Nov 9.",
     "全国消防日在11月___日。", instr="Fill in", size=19, gap=6)
e.ex("B1", "完成句子", "14", "The culture night is on Nov 14.",
     "文化馆之夜在11月___日。", instr="Fill in", size=19, gap=6)
e.ex("A2", "完成句子", "1", "Reading Month began on Nov 1.",
     "深圳读书月从11月___日开始。", instr="Fill in", size=19, gap=6)
e.head("D · 词语配对 · Matching", 25)
e.match_set("A2", "词汇配对",
            ["消防", "疏散", "自救", "楼道"],
            ["自己救自己,先保护自己",
             "火警电话119,防火的事",
             "大家按逃生路线离开",
             "楼里的走道,逃生路要通"],
            ["b", "c", "a", "d"],
            ["消防 = fire prevention, b", "疏散 = to evacuate, c", "自救 = self-rescue, a", "楼道 = a corridor, d"],
            instr="Match the words")
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-wenhua.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · 体育 (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("体育 · Sport", "Lucerna", "Level B1 · S16 瑞士轮打完 · Worlds S16: Swiss stage done")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1180, tag="P4-feature")
f.title("S16:瑞士轮打完,八强出炉", 37)
f.byline("Lucerna editors · Reading level B1")
f.para("《英雄联盟》全球总决赛S16的瑞士轮,在11月1日打完了。八支队进了淘汰赛:韩国的GEN、DK、T1,中国的IG、TES、BLG,欧洲的KC,北美的LYON。")
f.para("先说中国队:IG和TES都是3胜1负,BLG是3胜2负,三支队进了八强。BLG最后一场2比0打赢了韩国的HLE,拿到了最后一张八强门票。")
f.para("再说出局的队:中国的一号种子AL三场都输了,小局一场没赢,止步16强。韩国的HLE也出局了,成了韩国唯一没进八强的队。")
f.para("四分之一决赛的抽签也出来了:11月4日TES对IG,中国队先打内战;11月5日GEN对LYON;11月6日DK对BLG;11月7日T1对KC。全部是BO5,输了就回家,都是北京时间早上6点开始。")
f.para("本期截稿时是11月2日,四分之一决赛还没有打。所以,半决赛和决赛的队伍,还不知道。半决赛在11月8日到9日,总决赛在11月15日凌晨3点,地点是纽约的巴克莱中心。")
f.para("想看决赛的人,要先安排好睡觉的时间:凌晨3点,正是半夜。下一期,我们再报淘汰赛的结果。")
f.gloss("chūlú 出炉 — (of a list) to come out, to be finalised · nèizhàn 内战 — a match between two teams from the same region · dān bài 单败 — single elimination: lose once and you are out.")
f.end_report()

# ---- schedule (cols 0-2) ----
ly = 1210
p.text(MX, ly + 26, "S16 赛程 · S16 schedule (Beijing time)", 26, "sans", True, OLIVE)
p.hline(MX, COLX[2] + CW, ly + 40, GOLD, 2)
sched = [
    "四分之一决赛 — 11月4日 TES对IG,5日 GEN对LYON,6日 DK对BLG,7日 T1对KC,早上6点,BO5",
    "半决赛 — 11月8日—9日,北京时间早上6点,对阵看四分之一决赛结果",
    "总决赛 — 北京时间11月15日凌晨3点,纽约巴克莱中心",
    "瑞士轮结果(11月1日打完):3胜0负 GEN、DK;3胜1负 T1、TES、IG;3胜2负 LYON、KC、BLG",
]
syy = ly + 72
for s_ in sched:
    syy = p.para(MX, syy + 22, s_, 22, "serif", False, INK, 1388, 1.4) + 6
p.para(MX, syy + 14, "Standings as of Nov 1, 2026: Swiss stage complete. AL 0–3 and out; HLE 2–3 and out. Quarter-final draw announced Nov 1–2. Source: Sina/IT Home match reports, Nov 1; S16 viewing guide (Beijing times).", 20.5, "serif", False, GREY, 1388, 1.4)

# col 3: lan party + facts + match words
ix = COLX[3]
image(p, "lanparty.jpg", ix, 200, CW, 220)
cy3 = caption(p, ix, 420, CW, "一起打游戏的老照片(2003 年,法国)。今天看比赛,更多人是在网上一起看直播。",
              "Photo: Syced — CC0 (Wikimedia Commons)")
facts = ["11月1日 — 瑞士轮打完,八强出炉",
         "11月4日 — TES对IG,中国队内战",
         "11月6日 — DK对BLG",
         "11月15日 03:00 — 总决赛(北京时间)"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "体育小日历 · Sports dates", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ay3 = sy3 + sh + 26
mwords = [("出炉", "chūlú — the list is out, finalised."),
          ("内战", "nèizhàn — two teams from the same region play each other."),
          ("单败", "dānbài — lose once and you go home.")]
mh = 62 + sum(len(wrap(m[0] + " " + m[1], "serif", False, 21.5, CW - 44)) * 30.5 + 14 for m in mwords) + 30
p.rect(ix, ay3, CW, mh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ay3 + 16
p.text(ix + 22, yy3 + 26, "看比赛的中文 · Match words", 24, "sans", True, OLIVE)
yy3 += 52
for w_, d_ in mwords:
    yy3 = p.para(ix + 22, yy3 + 21, w_ + " " + d_, 21.5, "serif", False, INK, CW - 44, 1.42) + 8
print("P4 col3 ends", ay3 + mh)

# ---- P4 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "练习 · Exercises", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Answers on page 8 · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A · 读一读选一选 · Read & choose", 25)
e.glossline("Read page 4 and choose the best answer.")
e.ex("B1", "单选", "A", "The Swiss stage ended on Nov 1.",
     "瑞士轮哪天打完? A. 11月1日 · B. 11月15日 · C. 10月27日", size=19, gap=6)
e.ex("B1", "单选", "A", "Three LPL teams reached the quarter-finals.",
     "几支中国队进了八强? A. 三支 · B. 一支 · C. 四支", size=19, gap=6)
e.ex("B1", "单选", "B", "BLG beat HLE 2–0 in the last Swiss-stage match.",
     "BLG最后一场打赢了哪个队? A. G2 · B. HLE · C. KC", size=19, gap=6)
e.ex("B1", "单选", "B", "Quarter-finals start at 06:00 Beijing time.",
     "四分之一决赛在北京时间几点? A. 凌晨3点 · B. 早上6点 · C. 晚上8点", size=19, gap=6)
e.ex("B1", "单选", "B", "The final starts at 03:00 Beijing time on Nov 15.",
     "总决赛在北京时间哪天? A. 11月14日 · B. 11月15日凌晨3点 · C. 11月8日", size=19, gap=6)
e.head("B · 词语填空 · Word blanks", 25)
e.glossline("Fill each blank with the right word.")
e.ex("B1", "完成句子", "八强", "bāqiáng — the eight quarter-final teams.",
     "瑞士轮打完,___出炉了。", instr="Fill in", size=19, gap=6)
e.ex("B1", "完成句子", "内战", "nèizhàn — TES vs IG is an all-LPL match.",
     "TES对IG,是中国队的___。", instr="Fill in", size=19, gap=6)
e.ex("B1", "完成句子", "单败", "dānbài — single elimination: lose once and you go home.",
     "淘汰赛是___制,输一场就出局。", instr="Fill in", size=19, gap=6)
e.ex("B1", "完成句子", "出炉", "chūlú — the quarter-final draw came out on Nov 1–2.",
     "四分之一决赛的抽签___了。", instr="Fill in", size=19, gap=6)
e.ex("B1", "完成句子", "半夜", "bànyè — 03:00 is the middle of the night.",
     "总决赛在凌晨3点,正是___。", instr="Fill in", size=19, gap=6)
e.head("C · 读赛程 · Schedule work", 25)
e.glossline("Read the schedule on page 4.")
e.ex("B1", "完成句子", "3", "GEN and DK finished 3–0 in the Swiss stage.",
     "GEN和DK都是___胜0负。", instr="Fill in", size=19, gap=6)
e.ex("B1", "完成句子", "6", "Quarter-finals start at 06:00 Beijing time.",
     "四分之一决赛在早上___点。", instr="Fill in", size=19, gap=6)
e.ex("B1", "完成句子", "0", "AL won zero series in the Swiss stage.",
     "AL一场都没赢,战绩是___胜3负。", instr="Fill in", size=19, gap=6)
e.ex("B1", "完成句子", "4", "TES vs IG is on Nov 4.",
     "TES对IG在11月___日。", instr="Fill in", size=19, gap=6)
e.head("D · 词语配对 · Matching", 25)
e.match_set("B1", "词汇配对",
            ["瑞士轮", "内战", "单败", "总决赛"],
            ["最后一场比赛,决定冠军",
             "输一场就回家的赛制",
             "同一个赛区的两支队打",
             "按胜负分组打的比赛"],
            ["d", "c", "b", "a"],
            ["瑞士轮 = the Swiss stage, d", "内战 = an all-region match, c", "单败 = lose once and out, b", "总决赛 = the final, a"],
            instr="Match the words")
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-tiyu.svg")
print("P4 saved, exercises so far:", len(REG))
