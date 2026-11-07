# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-zh-cn-ja/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · 文化 (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("文化 · 文化", "Lucerna", "Level A2→B1 · 消防日与读书月 · 消防の日と読書月間")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-feature")
f.title("11月9日,先学会保护自己", 37)
f.byline("Lucerna編集部 · 読解レベル A2→B1")
f.para("11月9日星期一,是全国消防日。今年是第35个全国消防日。11月也是消防宣传月,今年的主题是:全民消防、生命至上——提高自防自救能力。")
f.para("为什么是11月9日?因为火警电话是119,11月9日就是119。这一天,很多地方会做疏散自救演练:大家按平时的逃生路线走一走,看看消防站,学一学怎么保护自己。")
f.para("着火的时候,最重要的是人,不是东西。先离开,再求救。着火了不坐电梯,走楼梯。烟很大的时候,低下身子,用湿毛巾捂住口鼻,快点离开。")
f.para("平时也要小心:出门以前,看看电器关了没有;充电的时候,人不要走远;楼道里不要放很多东西,逃生路要一直通着。")
f.para("11月还有一件文化事:深圳读书月。读书月从11月1日开始,主题是悦读深圳、阅连世界。11月14日星期六晚上,深圳市文化馆有文化馆之夜:读者可以亲手摸一摸古籍的装帧,抄一抄,读一读,把看展变成读经典。")
f.gloss("zìfáng 自防 — 自分を守ること · zìjiù 自救 — 自分を助けること、自力救助 · shūsàn 疏散 — 避難させる、人を安全に外へ出す · lóudào 楼道 — 廊下、階段の通路。")
f.head("冬天里,安全第一", 25)
f.para("冬天来了,天冷了,用火用电也多了。取暖的时候,人不要离开太久;睡觉以前,看看取暖器关了没有。安全第一,比什么都重要。")
f.gloss("qǔnuǎn 取暖 — 暖を取る、暖房 · diànqì 电器 — 電化製品 · tōng 通 — 通っている、ふさがっていない。")
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
p.text(ix + 22, yy3 + 26, "节日小日历 · 祭りの日程", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ay3 = sy3 + sh + 26
rbox = ["读书月:11月1日开始,深圳七个文化场馆一起办活动。",
        "文化馆之夜:11月14日,亲手摸古籍、抄经典。"]
rh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 14 for t in rbox) + 30
p.rect(ix, ay3, CW, rh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ay3 + 16
p.text(ix + 22, yy3 + 26, "读书月 · 読書月間", 24, "sans", True, OLIVE)
yy3 += 52
for t in rbox:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 8
ey3 = ay3 + rh + 26
etvous = "你呢?你参加过消防演练吗?这个月,你在读什么书?写两句中文寄来。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("あなたは？ 消防訓練に参加したことがありますか？ 今月は何を読んでいますか？ 中国語で2文書きましょう。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "说说你自己 · あなたは？", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "あなたは？ 消防訓練に参加したことがありますか？ 今月は何を読んでいますか？ 中国語で2文書きましょう。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "练习 · 練習問題", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答えは8ページ · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · 读一读选一选 · 読んで選ぼう", 25)
e.glossline("3ページを読んでいちばんよい答えを選ぼう。")
e.ex("A2", "单选", "A", "11月9日は第35回消防の日。",
     "今年是第几个全国消防日? A. 第35个 · B. 第19个 · C. 第24个", size=19, gap=6)
e.ex("A2", "单选", "B", "消防の日は11月9日。",
     "全国消防日在11月几日? A. 11月1日 · B. 11月9日 · C. 11月11日", size=19, gap=6)
e.ex("A2", "单选", "A", "火事のときはまず逃げて助けを呼び、エレベーターは使わない。",
     "着火的时候,先做什么? A. 先离开,再求救 · B. 先拿东西 · C. 先坐电梯", size=19, gap=6)
e.ex("A2", "单选", "B", "読書月間の文化の夜は11月14日。",
     "深圳读书月文化馆之夜在哪天? A. 11月1日 · B. 11月14日 · C. 11月9日", size=19, gap=6)
e.ex("A2", "单选", "A", "避難経路を空けておく — 廊下をふさがない。",
     "楼道里应该怎么样? A. 逃生路一直通着 · B. 放很多东西 · C. 关上所有的门", size=19, gap=6)
e.head("B · 词语填空 · 言葉の穴埋め", 25)
e.glossline("空欄に正しい言葉を入れよう。")
e.ex("A2", "完成句子", "消防", "xiāofáng — 防火。11月9日は消防の日。",
     "11月9日是全国___日。", instr="入れよう", size=19, gap=6)
e.ex("A2", "完成句子", "119", "火事の番号は119。",
     "火警电话是___。", instr="入れよう", size=19, gap=6)
e.ex("A2", "完成句子", "楼梯", "lóutī — 火事のときは階段で、エレベーターではない。",
     "着火的时候,走___,不坐电梯。", instr="入れよう", size=19, gap=6)
e.ex("B1", "完成句子", "疏散", "shūsàn — 避難訓練は避難経路を練習する。",
     "消防日那天,很多地方会做___演练。", instr="入れよう", size=19, gap=6)
e.ex("B1", "完成句子", "古籍", "gǔjí — 古い本。読者は古書の装丁に触れられる。",
     "文化馆之夜,读者可以亲手摸一摸___的装帧。", instr="入れよう", size=19, gap=6)
e.head("C · 数字与日期 · 数字", 25)
e.glossline("3ページの日付と数字で答えましょう。")
e.ex("A2", "完成句子", "35", "第35回消防の日。",
     "今年是第___个全国消防日。", instr="入れよう", size=19, gap=6)
e.ex("A2", "完成句子", "9", "消防の日は11月9日。",
     "全国消防日在11月___日。", instr="入れよう", size=19, gap=6)
e.ex("B1", "完成句子", "14", "文化の夜は11月14日。",
     "文化馆之夜在11月___日。", instr="入れよう", size=19, gap=6)
e.ex("A2", "完成句子", "1", "読書月間は11月1日開始。",
     "深圳读书月从11月___日开始。", instr="入れよう", size=19, gap=6)
e.head("D · 词语配对 · 言葉合わせ", 25)
e.match_set("A2", "词汇配对",
            ["消防", "疏散", "自救", "楼道"],
            ["自己救自己,先保护自己",
             "火警电话119,防火的事",
             "大家按逃生路线离开",
             "楼里的走道,逃生路要通"],
            ["b", "c", "a", "d"],
            ["消防 = 防火、b", "疏散 = 避難させる、c", "自救 = 自力救助、a", "楼道 = 廊下、d"],
            instr="言葉を合わせよう")
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-wenhua.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · 体育 (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("体育 · スポーツ", "Lucerna", "Level B1 · S16 瑞士轮打完 · 世界大会S16：スイスステージ終了")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1180, tag="P4-feature")
f.title("S16:瑞士轮打完,八强出炉", 37)
f.byline("Lucerna編集部 · 読解レベル B1")
f.para("《英雄联盟》全球总决赛S16的瑞士轮,在11月1日打完了。八支队进了淘汰赛:韩国的GEN、DK、T1,中国的IG、TES、BLG,欧洲的KC,北美的LYON。")
f.para("先说中国队:IG和TES都是3胜1负,BLG是3胜2负,三支队进了八强。BLG最后一场2比0打赢了韩国的HLE,拿到了最后一张八强门票。")
f.para("再说出局的队:中国的一号种子AL三场都输了,小局一场没赢,止步16强。韩国的HLE也出局了,成了韩国唯一没进八强的队。")
f.para("四分之一决赛的抽签也出来了:11月4日TES对IG,中国队先打内战;11月5日GEN对LYON;11月6日DK对BLG;11月7日T1对KC。全部是BO5,输了就回家,都是北京时间早上6点开始。")
f.para("本期截稿时是11月2日,四分之一决赛还没有打。所以,半决赛和决赛的队伍,还不知道。半决赛在11月8日到9日,总决赛在11月15日凌晨3点,地点是纽约的巴克莱中心。")
f.para("想看决赛的人,要先安排好睡觉的时间:凌晨3点,正是半夜。下一期,我们再报淘汰赛的结果。")
f.gloss("chūlú 出炉 — （リストが）出る、確定する · nèizhàn 内战 — 同じ地域の2チームの対戦 · dān bài 单败 — 一敗敗退：一度負けたら終わり。")
f.end_report()

# ---- schedule (cols 0-2) ----
ly = 1210
p.text(MX, ly + 26, "S16 赛程 · S16日程（北京時間）", 26, "sans", True, OLIVE)
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
p.para(MX, syy + 14, "2026年11月1日時点：スイスステージ完了。ALは0–3で敗退、HLEは2–3で敗退。準々決勝の組み合わせは11月1〜2日発表。出典：Sina/IT Homeの試合報道（11月1日）、S16観戦ガイド（北京時間）。", 20.5, "serif", False, GREY, 1388, 1.4)

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
p.text(ix + 22, yy3 + 26, "体育小日历 · スポーツの日程", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ay3 = sy3 + sh + 26
mwords = [("出炉", "chūlú — リストが出た、確定した。"),
          ("内战", "nèizhàn — 同じ地域の2チームが対戦する。"),
          ("单败", "dānbài — 一度負けたら帰る。")]
mh = 62 + sum(len(wrap(m[0] + " " + m[1], "serif", False, 21.5, CW - 44)) * 30.5 + 14 for m in mwords) + 30
p.rect(ix, ay3, CW, mh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ay3 + 16
p.text(ix + 22, yy3 + 26, "看比赛的中文 · 試合の中国語", 24, "sans", True, OLIVE)
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
e.glossline("4ページを読んでいちばんよい答えを選ぼう。")
e.ex("B1", "单选", "A", "スイスステージは11月1日終了。",
     "瑞士轮哪天打完? A. 11月1日 · B. 11月15日 · C. 10月27日", size=19, gap=6)
e.ex("B1", "单选", "A", "LPLの3チームが準々決勝へ。",
     "几支中国队进了八强? A. 三支 · B. 一支 · C. 四支", size=19, gap=6)
e.ex("B1", "单选", "B", "BLGがHLEに2–0、スイスステージ最終戦。",
     "BLG最后一场打赢了哪个队? A. G2 · B. HLE · C. KC", size=19, gap=6)
e.ex("B1", "单选", "B", "準々決勝は北京時間06:00開始。",
     "四分之一决赛在北京时间几点? A. 凌晨3点 · B. 早上6点 · C. 晚上8点", size=19, gap=6)
e.ex("B1", "单选", "B", "決勝は11月15日03:00（北京時間）開始。",
     "总决赛在北京时间哪天? A. 11月14日 · B. 11月15日凌晨3点 · C. 11月8日", size=19, gap=6)
e.head("B · 词语填空 · 言葉の穴埋め", 25)
e.glossline("空欄に正しい言葉を入れよう。")
e.ex("B1", "完成句子", "八强", "bāqiáng — 準々決勝の8チーム。",
     "瑞士轮打完,___出炉了。", instr="入れよう", size=19, gap=6)
e.ex("B1", "完成句子", "内战", "nèizhàn — TES対IGはLPL同士の対戦。",
     "TES对IG,是中国队的___。", instr="入れよう", size=19, gap=6)
e.ex("B1", "完成句子", "单败", "dānbài — 一敗敗退：一度負けたら帰る。",
     "淘汰赛是___制,输一场就出局。", instr="入れよう", size=19, gap=6)
e.ex("B1", "完成句子", "出炉", "chūlú — 準々決勝の組み合わせは11月1〜2日に出た。",
     "四分之一决赛的抽签___了。", instr="入れよう", size=19, gap=6)
e.ex("B1", "完成句子", "半夜", "bànyè — 03:00は真夜中。",
     "总决赛在凌晨3点,正是___。", instr="入れよう", size=19, gap=6)
e.head("C · 读赛程 · 日程を読もう", 25)
e.glossline("4ページの日程を読もう。")
e.ex("B1", "完成句子", "3", "GENとDKはスイスステージを3–0で終えた。",
     "GEN和DK都是___胜0负。", instr="入れよう", size=19, gap=6)
e.ex("B1", "完成句子", "6", "準々決勝は北京時間06:00開始。",
     "四分之一决赛在早上___点。", instr="入れよう", size=19, gap=6)
e.ex("B1", "完成句子", "0", "ALはスイスステージで0勝。",
     "AL一场都没赢,战绩是___胜3负。", instr="入れよう", size=19, gap=6)
e.ex("B1", "完成句子", "4", "TES対IGは11月4日。",
     "TES对IG在11月___日。", instr="入れよう", size=19, gap=6)
e.head("D · 词语配对 · 言葉合わせ", 25)
e.match_set("B1", "词汇配对",
            ["瑞士轮", "内战", "单败", "总决赛"],
            ["最后一场比赛,决定冠军",
             "输一场就回家的赛制",
             "同一个赛区的两支队打",
             "按胜负分组打的比赛"],
            ["d", "c", "b", "a"],
            ["瑞士轮 = スイスステージ、d", "内战 = 地域内対戦、c", "单败 = 一度負けたら終わり、b", "总决赛 = 決勝、a"],
            instr="言葉を合わせよう")
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-tiyu.svg")
print("P4 saved, exercises so far:", len(REG))
