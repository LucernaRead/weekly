# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-zh-cn-ja/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · 文化 (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("文化　文化", "Lucerna", "Level A2→B1　小雪与读书月　小雪と読書月間")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-feature")
f.title("小雪到了，冬天真的来了", 32)
f.byline("Lucerna 編集部　読解レベル A2 → B1")
f.para("11月22日星期日，是小雪。农历十月十四。小雪是二十四节气里的第20个，也是冬天的第2个。古人说：“小雪气寒而将雪矣，地寒未甚而雪未大也。”")
f.para("小雪有三候：一候虹藏不见，二候天气上升地气下降，三候闭塞而成冬。简单说：天冷了，雨少了，彩虹不见了；天地间的气慢慢闭住了，冬天就到了。")
f.para("小雪之后，天气会更冷。北方很多地方已经开始供暖，家里暖和了。南方没有供暖，出门要多穿一件。古人说，小雪前后，要注意保暖，头和脚别着凉。")
f.para("11月还有一件文化事：深圳读书月。读书月从11月1日开始，主题是悦读深圳、阅连世界，七个文化场馆一起办活动。11月7日是国际美术馆日，在艺术品中间读书；11月14日是文化馆之夜，读者可以亲手摸古籍、抄经典。")
f.para("冬天读书也很好：天冷了，坐在家里，泡一杯热茶，读一本书。读书月就是想让更多人这样读。")
f.gloss("jiéqì 节气 — 二十四節気のひとつ · sānhòu 三候 — 節気の3つの五日間の時期 · bǎonuǎn 保暖 — 暖かくする · zháoliáng 着凉 — 冷えて風邪をひく。")
f.head("小雪三候，怎么记", 25)
f.para("三候是古人看天气的办法：一候虹藏不见——雨少了，彩虹不见了；二候天气上升地气下降——天上的气往上走，地上的气往下走；三候闭塞而成冬——天地闭住了，冬天就到了。")
f.gloss("hóng 虹 — 虹 · bìsè 闭塞 — 閉ざされた、ふさがれた。")
f.end_report()

# col 3: frost + facts + reading box + 你呢
ix = COLX[3]
image(p, "frost.jpg", ix, 200, CW, 185)
cy3 = caption(p, ix, 385, CW, "带霜的红叶。冬天来了，早上能看见白白的霜，出门要加衣服。",
              "写真：Gerda Arendt — CC0（Wikimedia Commons）")
facts = ["11月22日星期日 — 小雪",
         "第20个节气 — 冬天第2个",
         "11月 — 深圳读书月"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "节日小日历　行事カレンダー", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ay3 = sy3 + sh + 26
rbox = ["读书月：11月1日开始，深圳七个文化场馆一起办活动。",
        "文化馆之夜：11月14日，亲手摸古籍、抄经典。"]
rh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 14 for t in rbox) + 30
p.rect(ix, ay3, CW, rh, fill=BOX)
yy3 = ay3 + 16
p.text(ix + 22, yy3 + 26, "读书月　読書月間", 24, "sans", True, OLIVE)
yy3 += 52
for t in rbox:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 8
ey3 = ay3 + rh + 26
etvous = "你呢？你喜欢冬天吗？这个月，你在读什么书？写两句中文寄来。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("あなたは？ 冬は好きですか？ 今月は何を読んでいますか？ 中国語で2文書きましょう。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill=BOX)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "说说你自己　あなたは？", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "あなたは？ 冬は好きですか？ 今月は何を読んでいますか？ 中国語で2文書きましょう。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "练习　練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答えは 8 ページ　答案见第8版", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P3-ex")
e.head("A　读一读选一选　読んで選ぶ", 25)
e.glossline("3ページを読んでいちばんよい答えを選ぼう。")
e.ex("A2", "单选", "A", "小雪は11月22日。",
     "小雪在哪天？ A. 11月22日 · B. 11月21日 · C. 11月15日", size=20, gap=6)
e.ex("A2", "单选", "A", "小雪は二十四節気の20番目。",
     "小雪是第几个节气？ A. 第20个 · B. 第24个 · C. 第2个", size=20, gap=6)
e.ex("A2", "单选", "A", "最初の候は虹藏不见。",
     "小雪三候的第一候是什么？ A. 虹藏不见 · B. 天气上升 · C. 闭塞而成冬", size=20, gap=6)
e.ex("A2", "单选", "A", "読書月間は11月1日開始。",
     "深圳读书月哪天开始？ A. 11月1日 · B. 11月14日 · C. 11月7日", size=20, gap=6)
e.ex("A2", "单选", "B", "文化の夜は11月14日。",
     "文化馆之夜在哪天？ A. 11月7日 · B. 11月14日 · C. 11月1日", size=20, gap=6)
e.head("B　词语填空　単語の穴埋め", 25)
e.glossline("空欄に正しい言葉を入れよう。")
e.ex("A2", "完成句子", "小雪", "xiǎoxuě — 小雪；11月22日。",
     "11月22日是___。", instr="入れよう", size=20, gap=6)
e.ex("A2", "完成句子", "20", "小雪は二十四節気の20番目。",
     "小雪是二十四节气里的第___个。", instr="入れよう", size=20, gap=6)
e.ex("A2", "完成句子", "冷", "小雪のあと、天気はさらに寒くなる。",
     "小雪之后，天气会更___。", instr="入れよう", size=20, gap=6)
e.ex("B1", "完成句子", "七", "7会場が読書月間に参加。",
     "读书月有___个场馆一起参加。", instr="入れよう", size=20, gap=6)
e.ex("B1", "完成句子", "古籍", "gǔjí — 古い本。読者は古書の装丁に触れられる。",
     "文化馆之夜，读者可以亲手摸一摸___的装帧。", instr="入れよう", size=20, gap=6)
e.head("C　数字与日期　数字", 25)
e.glossline("3ページの日付と数字で答えましょう。")
e.ex("A2", "完成句子", "22", "小雪は11月22日、日曜日。",
     "小雪在11月___日星期日。", instr="入れよう", size=20, gap=6)
e.ex("A2", "完成句子", "2", "小雪は冬の2番目の節気。",
     "小雪是冬天第___个节气。", instr="入れよう", size=20, gap=6)
e.ex("B1", "完成句子", "14", "文化の夜は11月14日。",
     "文化馆之夜在11月___日。", instr="入れよう", size=20, gap=6)
e.ex("A2", "完成句子", "1", "読書月間は11月1日開始。",
     "深圳读书月从11月___日开始。", instr="入れよう", size=20, gap=6)
e.head("D　词语配对　マッチング", 25)
e.match_set("A2", "词汇配对",
            ["小雪", "三候", "保暖", "着凉"],
            ["天冷了，多穿衣服，别冻着",
             "二十四节气里的一个，11月22日",
             "不小心冷到了，身体不舒服",
             "古人看天气的三个变化"],
            ["b", "d", "a", "c"],
            ["小雪 = 小雪、b", "三候 = 3つの時期、d", "保暖 = 暖かくする、a", "着凉 = 冷えて風邪をひく、c"],
            instr="言葉を合わせよう")
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-wenhua.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · 体育 (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("体育　スポーツ", "Lucerna", "Level B1　S16 四强打完　ワールズ S16：準決勝終了")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1180, tag="P4-feature")
f.title("S16：四强打完，决赛见", 32)
f.byline("Lucerna 編集部　読解レベル B1")
f.para("S16的淘汰赛打完了三分之二：四分之一决赛11月4日到7日打完，半决赛11月8日到9日打完。决赛在11月15日凌晨3点，纽约巴克莱中心，BLG对GEN。")
f.para("四分之一决赛：11月4日，IG 3比1打赢TES，中国队内战；11月5日，GEN 3比0打赢LYON；11月6日，BLG 3比0打赢DK；11月7日，T1 3比1打赢KC。全部是BO5，输了就回家。")
f.para("半决赛：11月8日，GEN 3比0打赢IG；11月9日，BLG 3比1打赢T1。IG时隔七年重返四强，半决赛输给了GEN，止步四强。两支中国队进了四强：IG和BLG。BLG赢了T1，这是中国队第一次在全球总决赛的BO5里打赢T1。")
f.para("决赛的两个队：GEN在S16一场没输，只丢了一小局——瑞士轮3胜0负（对LYON 2比1），八强3比0，半决赛3比0。BLG一路打赢了三支韩国队：瑞士轮2比0打赢HLE，八强3比0打赢DK，半决赛3比1打赢T1。")
f.para("本期截稿时是11月10日，总决赛还没打。谁是冠军？下一期再报。想看决赛的人，记得调好闹钟：北京时间11月15日凌晨3点。")
f.para("BO5是五局三胜，先赢三局的队拿冠军。决赛夜，先睡一觉，再起来看。")
f.gloss("sìqiáng 四强 — 最後の4チーム、準決勝進出チーム · zhǐbù 止步 — ここで止まる、これ以上進めない · nàozhōng 闹钟 — 目覚まし時計 · wǔjú sānshèng 五局三胜 — 5本先取：3本取った方が勝ち。")
f.end_report()

# ---- schedule (cols 0-2) ----
ly = 1210
p.text(MX, ly + 26, "S16 赛程　S16の日程（北京時間）", 26, "sans", True, OLIVE)
p.hline(MX, COLX[2] + CW, ly + 40, OLIVE, 2)
sched = [
    "四分之一决赛 — 11月4日 IG 3比1 TES，5日 GEN 3比0 LYON，6日 BLG 3比0 DK，7日 T1 3比1 KC，早上6点，BO5",
    "半决赛 — 11月8日 GEN 3比0 IG，9日 BLG 3比1 T1，早上6点，BO5",
    "总决赛 — 北京时间11月15日凌晨3点，纽约巴克莱中心，BLG对GEN，BO5",
    "四强：GEN、IG、BLG、T1；中国队两支，韩国队两支",
]
syy = ly + 72
for s_ in sched:
    syy = p.para(MX, syy + 22, s_, 22, "serif", False, INK, 1323, 1.4) + 6
p.para(MX, syy + 14, "2026年11月9日時点：準々決勝と準決勝が終了。決勝は締切（11月10日）時点ではまだ行われていない。出典：Sina、扬子晚报、中关村在线の試合報道（11月8〜9日）。S16観戦ガイド（北京時間）。", 20.5, "serif", False, GREY, 1323, 1.4)

# col 3: lan party + facts + match words
ix = COLX[3]
image(p, "lanparty.jpg", ix, 200, CW, 220)
cy3 = caption(p, ix, 420, CW, "一起打游戏的老照片（2003年，法国）。今天看比赛，更多人是在网上一起看直播。",
              "写真：Syced — CC0（Wikimedia Commons）")
facts = ["11月8日 — GEN 3比0胜IG",
         "11月9日 — BLG 3比1胜T1",
         "11月15日 03:00 — 总决赛 BLG对GEN",
         "GEN今年 — 淘汰赛一局没输"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "体育小日历　スポーツの日程", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ay3 = sy3 + sh + 26
mwords = [("四强", "sìqiáng — 最後の4チーム。"),
          ("止步", "zhǐbù — ここで止まる、これ以上進めない。"),
          ("闹钟", "nàozhōng — 目覚まし時計。")]
mh = 62 + sum(len(wrap(m[0] + " " + m[1], "serif", False, 21.5, CW - 44)) * 30.5 + 14 for m in mwords) + 30
p.rect(ix, ay3, CW, mh, fill=BOX)
yy3 = ay3 + 16
p.text(ix + 22, yy3 + 26, "看比赛的中文　試合の言葉", 24, "sans", True, OLIVE)
yy3 += 52
for w_, d_ in mwords:
    yy3 = p.para(ix + 22, yy3 + 21, w_ + " " + d_, 21.5, "serif", False, INK, CW - 44, 1.42) + 8
print("P4 col3 ends", ay3 + mh)

# ---- P4 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "练习　練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答えは 8 ページ　答案见第8版", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P4-ex")
e.head("A　读一读选一选　読んで選ぶ", 25)
e.glossline("4ページを読んでいちばんよい答えを選ぼう。")
e.ex("B1", "单选", "A", "IGは準々決勝でTESに3-1で勝った。",
     "四分之一决赛，IG打赢了哪个队？ A. TES · B. GEN · C. DK", size=20, gap=6)
e.ex("B1", "单选", "B", "GENは準決勝でIGに3-0で勝った。",
     "半决赛，GEN打赢了哪个队？ A. T1 · B. IG · C. BLG", size=20, gap=6)
e.ex("B1", "单选", "C", "BLGは準決勝でT1に3-1で勝った。",
     "半决赛，BLG打赢了哪个队？ A. LYON · B. KC · C. T1", size=20, gap=6)
e.ex("B1", "单选", "A", "決勝は11月15日03:00（北京時間）。",
     "决赛在哪天？ A. 11月15日凌晨3点 · B. 11月14日 · C. 11月8日", size=20, gap=6)
e.ex("B1", "单选", "A", "決勝はBLG対GEN。",
     "决赛的两个队是？ A. BLG和GEN · B. IG和T1 · C. TES和DK", size=20, gap=6)
e.head("B　词语填空　単語の穴埋め", 25)
e.glossline("空欄に正しい言葉を入れよう。")
e.ex("B1", "完成句子", "DK", "BLGは準々決勝でDKに3-0で勝った。",
     "四分之一决赛，BLG 3比0打赢了___。", instr="入れよう", size=20, gap=6)
e.ex("B1", "完成句子", "IG", "GENは準決勝でIGに3-0で勝った。",
     "半决赛，GEN 3比0打赢了___。", instr="入れよう", size=20, gap=6)
e.ex("B1", "完成句子", "BLG", "決勝はBLG対GEN。",
     "决赛是___对GEN。", instr="入れよう", size=20, gap=6)
e.ex("B1", "完成句子", "3", "決勝は03:00（北京時間）。",
     "决赛在北京时间11月15日凌晨___点。", instr="入れよう", size=20, gap=6)
e.ex("B1", "完成句子", "T1", "BLGはワールズのBO5で初めてT1に勝った。",
     "BLG是第一次在全球总决赛的BO5里打赢___。", instr="入れよう", size=20, gap=6)
e.head("C　读赛程　日程を読む", 25)
e.glossline("4ページの日程を読もう。")
e.ex("B1", "完成句子", "4", "IGは11月4日にTESに勝った。",
     "IG 3比1打赢TES，在11月___日。", instr="入れよう", size=20, gap=6)
e.ex("B1", "完成句子", "5", "GENは11月5日にLYONに勝った。",
     "GEN 3比0打赢LYON，在11月___日。", instr="入れよう", size=20, gap=6)
e.ex("B1", "完成句子", "6", "BLGは11月6日にDKに勝った。",
     "BLG 3比0打赢DK，在11月___日。", instr="入れよう", size=20, gap=6)
e.ex("B1", "完成句子", "7", "T1は11月7日にKCに勝った。",
     "T1 3比1打赢KC，在11月___日。", instr="入れよう", size=20, gap=6)
e.head("D　词语配对　マッチング", 25)
e.match_set("B1", "词汇配对",
            ["四强", "止步", "闹钟", "五局三胜"],
            ["先赢三局的队拿冠军",
             "半决赛输了，就不往前走了",
             "到时间会响，叫你起床",
             "最后四支队，半决赛的队"],
            ["d", "b", "c", "a"],
            ["四强 = 最後の4チーム、d", "止步 = ここで止まる、b", "闹钟 = 目覚まし時計、c", "五局三胜 = 5本先取、a"],
            instr="言葉を合わせよう")
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-tiyu.svg")
print("P4 saved, exercises so far:", len(REG))
