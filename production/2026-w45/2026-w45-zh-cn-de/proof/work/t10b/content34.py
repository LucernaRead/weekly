# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-cn-de-proof/work/t10b/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · 文化 (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("文化 · Kultur", "Lucerna", "Niveau A2→B1 · 立冬:冬天的第一个节气 · Winteranfang")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-feature")
f.title("立冬到了,冬天要来了", 37)
f.byline("Lucerna-Redaktion · Leseniveau A2→B1")
f.para("11月7日星期六,是立冬。立冬是二十四节气里的第十九个,也是冬天的第一个节气。这一天17点52分交节,冬天正式开始。")
f.para("立冬有三候:一候水始冰,二候地始冻,三候雉入大水为蜃。简单说:水开始结冰,地开始上冻,野鸡不多见了。古人说,雉变成了大蛤,这是古人的想象,不是真的变化。")
f.para("立冬的吃法,各地不一样。北方很多地方吃饺子,因为饺子和交子同音,是秋冬交替的意思。南方有的地方吃鸡鸭鱼肉,有的地方吃汤圆、糍粑,还有的地方喝羊肉汤。没有一种吃法是全国统一的。")
f.para("立冬以后,天气会一天比一天冷,但不是每个地方同时变冷。南方有的地方立冬还很暖和,北方有的地方已经下雪了。出门以前,先看天气预报,加衣服,别着凉。")
f.para("11月8日星期日是中国记者节。记者的工作是采访和写新闻:去现场看一看,问一问,再把事情写清楚。写新闻的时候,时间、地点、数字都要写对。")
f.gloss("hòu 候 — eine fünftägige Mikro-Jahreszeit · jiāotì 交替 — eine Sache löst die andere ab · cǎifǎng 采访 — interviewen, vor Ort berichten.")
f.head("冬天第一天,做什么好", 25)
f.para("立冬那天,可以做三件事:加一件厚衣服,吃一顿热饭,给家人打一个电话。冬天来了,身体暖和,心里也暖和。")
f.gloss("hòu yīfu 厚衣服 — warme Kleidung · rè fàn 热饭 — eine warme Mahlzeit · zháoliáng 着凉 — sich erkälten.")
f.end_report()

# col 3: frost + facts + dumplings + 你呢
ix = COLX[3]
image(p, "frost.jpg", ix, 200, CW, 185)
cy3 = caption(p, ix, 385, CW, "带霜的红叶。霜降已过,立冬要来,早上能看见白白的霜。",
              "Foto: Gerda Arendt — CC0 (Wikimedia Commons)")
facts = ["11月7日星期六 — 立冬,冬天第一个节气",
         "11月7日 17:52 — 立冬交节",
         "11月8日星期日 — 中国记者节"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "节日小日历 · Festtermine", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ay3 = sy3 + sh + 26
image(p, "dumplings.jpg", ix, ay3, CW, 200)
cy4 = caption(p, ix, ay3 + 200, CW, "饺子(资料图)。北方很多地方立冬吃饺子。",
              "Foto: Syced — CC0 (Wikimedia Commons)")
ey3 = cy4 + 18
etvous = "你呢?立冬那天,你想吃什么?你住的地方冷不冷?写两句中文寄来。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Und Sie? Was würden Sie an 立冬 essen? Ist es kalt, wo Sie wohnen? Schreiben Sie zwei Sätze auf Chinesisch.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "说说你自己 · Und Sie?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Und Sie? Was würden Sie an 立冬 essen? Ist es kalt, wo Sie wohnen? Schreiben Sie zwei Sätze auf Chinesisch.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "练习 · Übungen", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Lösungen auf Seite 8 · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · 读一读选一选 · Lesen & wählen", 25)
e.glossline("Lesen Sie Seite 3 und wählen Sie die beste Antwort.")
e.ex("A2", "单选", "A", "立冬 ist der 19. der 24 Solartermine.",
     "立冬是第几个节气? A. 第19个 · B. 第18个 · C. 第24个", size=19, gap=6)
e.ex("A2", "单选", "B", "Winteranfang fällt auf Samstag, den 7. Nov.",
     "立冬在11月几日? A. 11月1日 · B. 11月7日 · C. 11月11日", size=19, gap=6)
e.ex("A2", "单选", "A", "Erste Mikro-Jahreszeit: Das Wasser beginnt zu gefrieren.",
     "立冬一候是什么? A. 水始冰 · B. 地始冻 · C. 雉入大水为蜃", size=19, gap=6)
e.ex("A2", "单选", "B", "Nordchinesische Familien essen an 立冬 Teigtaschen.",
     "北方立冬吃什么? A. 汤圆 · B. 饺子 · C. 月饼", size=19, gap=6)
e.ex("A2", "单选", "A", "Journalist: interviewt und schreibt Nachrichten.",
     "记者的工作是什么? A. 采访和写新闻 · B. 只管卖东西 · C. 只管做饭", size=19, gap=6)
e.head("B · 词语填空 · Wörter einsetzen", 25)
e.glossline("Setzen Sie das richtige Wort ein.")
e.ex("A2", "完成句子", "立冬", "lìdōng — Winteranfang, 7. Nov.",
     "11月7日是___。", instr="Ausfüllen", size=19, gap=6)
e.ex("A2", "完成句子", "水始冰", "shuǐ shǐ bīng — das Wasser beginnt zu gefrieren (1. Mikro-Jahreszeit).",
     "立冬一候是___。", instr="Ausfüllen", size=19, gap=6)
e.ex("A2", "完成句子", "饺子", "jiǎozǐ — nordchinesische Familien essen sie an 立冬.",
     "北方很多地方立冬吃___。", instr="Ausfüllen", size=19, gap=6)
e.ex("B1", "完成句子", "汤圆", "tāngyuán — Klebreisbällchen, die mancherorts im Süden gegessen werden.",
     "南方有的地方吃___。", instr="Ausfüllen", size=19, gap=6)
e.ex("B1", "完成句子", "记者", "jìzhě — Journalist: interviewt, schreibt Nachrichten.",
     "采访和写新闻的人,叫___。", instr="Ausfüllen", size=19, gap=6)
e.head("C · 数字与日期 · Zahlen & Daten", 25)
e.glossline("Antworten Sie mit Daten und Zahlen von Seite 3.")
e.ex("A2", "完成句子", "19", "立冬 ist der 19. Solarterm.",
     "立冬是第___个节气。", instr="Ausfüllen", size=19, gap=6)
e.ex("A2", "完成句子", "7", "Winteranfang ist am 7. Nov.",
     "立冬在11月___日。", instr="Ausfüllen", size=19, gap=6)
e.ex("B1", "完成句子", "52", "Der Solarterm-Moment ist 17:52 Uhr.",
     "立冬交节在17点___分。", instr="Ausfüllen", size=19, gap=6)
e.ex("A2", "完成句子", "8", "Der Journalistentag ist am 8. Nov.",
     "中国记者节在11月___日。", instr="Ausfüllen", size=19, gap=6)
e.head("D · 词语配对 · Zuordnen", 25)
e.match_set("A2", "词汇配对",
            ["水始冰", "地始冻", "雉入大水为蜃", "补冬"],
            ["冬天以前吃点好的",
             "水面结了薄冰",
             "地开始上冻",
             "古人说雉变成了大蛤"],
            ["b", "c", "d", "a"],
            ["水始冰 = das Wasser beginnt zu gefrieren, b", "地始冻 = die Erde beginnt zu gefrieren, c", "雉入大水为蜃 = die alte Fasanengeschichte, d", "bǔdōng 补冬 = vor dem Winter gut essen, a"],
            instr="Zuordnen")
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-wenhua.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · 体育 (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("体育 · Sport", "Lucerna", "Niveau B1 · S16 瑞士轮与淘汰赛 · Worlds S16: Swiss-Runde & K.-o.-Spiele")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1180, tag="P4-feature")
f.title("S16:一支队出局,三支队冲八强", 37)
f.byline("Lucerna-Redaktion · Leseniveau B1")
f.para("《英雄联盟》全球总决赛S16正在美国得克萨斯州的艾伦市举行。瑞士轮从10月24日打到11月1日,四分之一决赛在11月4日到7日,半决赛在11月8日到9日,都是北京时间早上6点开始。")
f.para("先说坏消息:中国LPL赛区的一号种子AL出局了。AL先输给KC,又在内战里输给TES,最后0比2输给北美TL,三场都输了,小局一场没赢,止步16强。")
f.para("再说好消息:IG和TES在10月26日都赢了。IG打赢了HLE,TES一度落后,后来翻盘打赢了G2,两支队都是2胜1负,进了2胜1负组。BLG也打赢了KC,同样是2胜1负。三支队离八强只差一场BO3的胜利。")
f.para("瑞士轮怎么打?赢的队和赢的队打,输的队和输的队打。先赢三场的队进淘汰赛,输三场的队回家。第四轮在10月29日到31日打,全部是BO3:IG对LYON,BLG对TES,还有MKOI对T1。")
f.para("本期截稿时是10月27日,第四轮还没有打。所以,四分之一决赛的对手,要等瑞士轮打完才知道。这一周,早上6点看比赛的人,又要早起了。")
f.para("总决赛在11月14日举行,地点是纽约的巴克莱中心。换成北京时间,是11月15日凌晨3点。想看决赛的人,要先安排好睡觉的时间。")
f.gloss("tǎotài 淘汰 — ausschalten, eliminieren · nèizhàn 内战 — ein Spiel zwischen zwei Teams derselben Region · zhǐbù 止步 — hier endet es, nicht weiter.")
f.end_report()

# ---- schedule (cols 0-2) ----
ly = 1210
p.text(MX, ly + 26, "S16 赛程 · S16-Spielplan (Pekinger Zeit)", 26, "sans", True, OLIVE)
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
p.para(MX, syy + 14, "Stand am 27. Okt. 2026: GEN und DK schon 3–0 und weiter; AL und TSW 0–3 und ausgeschieden. Quelle: Sina-Sports-S16-Leitfaden (Pekinger Zeiten) und Spielberichte, 26.–27. Okt.", 20.5, "serif", False, GREY, 1388, 1.4)

# col 3: lan party + facts + match words
ix = COLX[3]
image(p, "lanparty.jpg", ix, 200, CW, 220)
cy3 = caption(p, ix, 420, CW, "一起打游戏的老照片(2003 年,法国)。今天看比赛,更多人是在网上一起看直播。",
              "Foto: Syced — CC0 (Wikimedia Commons)")
facts = ["10月26日 — IG胜HLE,TES胜G2",
         "10月27日 — AL三连败出局",
         "11月4日—7日 — 四分之一决赛",
         "11月15日 03:00 — 总决赛(北京时间)"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "体育小日历 · Sporttermine", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ay3 = sy3 + sh + 26
mwords = [("通宵", "tōngxiāo — für ein Spiel die ganze Nacht wach bleiben."),
          ("加油", "jiāyóu — Auf geht's! (was Fans rufen)."),
          ("翻盘", "fānpán — ein Comeback-Sieg, ein Spiel drehen.")]
mh = 62 + sum(len(wrap(m[0] + " " + m[1], "serif", False, 21.5, CW - 44)) * 30.5 + 14 for m in mwords) + 30
p.rect(ix, ay3, CW, mh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ay3 + 16
p.text(ix + 22, yy3 + 26, "看比赛的中文 · Wörter zum Spiel", 24, "sans", True, OLIVE)
yy3 += 52
for w_, d_ in mwords:
    yy3 = p.para(ix + 22, yy3 + 21, w_ + " " + d_, 21.5, "serif", False, INK, CW - 44, 1.42) + 8
print("P4 col3 ends", ay3 + mh)

# ---- P4 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "练习 · Übungen", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Lösungen auf Seite 8 · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A · 读一读选一选 · Lesen & wählen", 25)
e.glossline("Lesen Sie Seite 4 und wählen Sie die beste Antwort.")
e.ex("B1", "单选", "A", "Die Swiss-Runde wird in Allen, Texas, gespielt.",
     "瑞士轮在哪个城市? A. 艾伦 · B. 洛杉矶 · C. 纽约", size=19, gap=6)
e.ex("B1", "单选", "A", "AL verlor alle drei Swiss-Runden-Serien.",
     "AL为什么出局? A. 一场都没赢 · B. 赢了三场 · C. 没有参加", size=19, gap=6)
e.ex("B1", "单选", "B", "IG schlug HLE am 26. Okt.",
     "IG打赢了哪个队? A. G2 · B. HLE · C. KC", size=19, gap=6)
e.ex("B1", "单选", "B", "Die Viertelfinale beginnen um 06:00 Uhr Pekinger Zeit.",
     "四分之一决赛在北京时间几点? A. 凌晨1点 · B. 早上6点 · C. 晚上8点", size=19, gap=6)
e.ex("B1", "单选", "B", "Finale: 15. Nov., 03:00 Uhr Pekinger Zeit.",
     "总决赛在北京时间哪天? A. 11月14日 · B. 11月15日凌晨3点 · C. 11月8日", size=19, gap=6)
e.head("B · 词语填空 · Wörter einsetzen", 25)
e.glossline("Setzen Sie das richtige Wort ein.")
e.ex("B1", "完成句子", "艾伦", "Àilún — Allen, Texas, Austragungsort der Swiss-Runde.",
     "瑞士轮在美国___市举行。", instr="Ausfüllen", size=19, gap=6)
e.ex("B1", "完成句子", "内战", "nèizhàn — AL verlor das reine LPL-Spiel gegen TES.",
     "AL在___里输给了TES。", instr="Ausfüllen", size=19, gap=6)
e.ex("B1", "完成句子", "淘汰", "táotài — drei Siege schicken ein Team in die K.-o.-Runde.",
     "先赢三场的队进___赛。", instr="Ausfüllen", size=19, gap=6)
e.ex("B1", "完成句子", "翻盘", "fānpán — TES drehte das Spiel gegen G2.",
     "TES打赢G2,是一场___。", instr="Ausfüllen", size=19, gap=6)
e.ex("B1", "完成句子", "加油", "jiāyóu — was Fans für ihr Team rufen.",
     "看比赛时,观众喊___。", instr="Ausfüllen", size=19, gap=6)
e.head("C · 读赛程 · Spielplan lesen", 25)
e.glossline("Lesen Sie den Spielplan auf Seite 4.")
e.ex("B1", "完成句子", "3", "Drei Siege bringen ein Team aus der Swiss-Runde weiter.",
     "先赢___场进淘汰赛。", instr="Ausfüllen", size=19, gap=6)
e.ex("B1", "完成句子", "6", "Die Viertelfinale beginnen um 06:00 Uhr Pekinger Zeit.",
     "四分之一决赛在早上___点。", instr="Ausfüllen", size=19, gap=6)
e.ex("B1", "完成句子", "0", "AL gewann keine einzige Serie in der Swiss-Runde.",
     "AL一场都没赢,战绩是___胜3负。", instr="Ausfüllen", size=19, gap=6)
e.ex("B1", "完成句子", "1", "Die Swiss-Runde läuft bis zum 1. Nov.",
     "瑞士轮打到11月___日。", instr="Ausfüllen", size=19, gap=6)
e.head("D · 词语配对 · Zuordnen", 25)
e.match_set("B1", "词汇配对",
            ["瑞士轮", "内战", "淘汰赛", "总决赛"],
            ["最后一场比赛,决定冠军",
             "输了就回家的比赛",
             "同一个赛区的两支队打",
             "按胜负分组打的比赛"],
            ["d", "c", "b", "a"],
            ["瑞士轮 = die Swiss-Runde, d", "内战 = ein Spiel innerhalb einer Region, c", "淘汰赛 = Verlierer fährt heim, b", "总决赛 = das Finale, a"],
            instr="Zuordnen")
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-tiyu.svg")
print("P4 saved, exercises so far:", len(REG))
