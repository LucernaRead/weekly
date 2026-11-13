# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-zh-cn-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · 文化 (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("文化　문화", "Lucerna", "Level A2→B1　小雪与读书月　소설과 독서의 달")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-feature")
f.title("小雪到了，冬天真的来了", 32)
f.byline("Lucerna 편집부　읽기 수준 A2 → B1")
f.para("11月22日星期日，是小雪。农历十月十四。小雪是二十四节气里的第20个，也是冬天的第2个。古人说：“小雪气寒而将雪矣，地寒未甚而雪未大也。”")
f.para("小雪有三候：一候虹藏不见，二候天气上升地气下降，三候闭塞而成冬。简单说：天冷了，雨少了，彩虹不见了；天地间的气慢慢闭住了，冬天就到了。")
f.para("小雪之后，天气会更冷。北方很多地方已经开始供暖，家里暖和了。南方没有供暖，出门要多穿一件。古人说，小雪前后，要注意保暖，头和脚别着凉。")
f.para("11月还有一件文化事：深圳读书月。读书月从11月1日开始，主题是悦读深圳、阅连世界，七个文化场馆一起办活动。11月7日是国际美术馆日，在艺术品中间读书；11月14日是文化馆之夜，读者可以亲手摸古籍、抄经典。")
f.para("冬天读书也很好：天冷了，坐在家里，泡一杯热茶，读一本书。读书月就是想让更多人这样读。")
f.gloss("jiéqì 节气 — 절기 · sānhòu 三候 — 절기의 세 다섯 날 주기 · bǎonuǎn 保暖 — 따뜻하게 하기 · zháoliáng 着凉 — 몸이 차서 감기에 걸리다.")
f.head("小雪三候，怎么记", 25)
f.para("三候是古人看天气的办法：一候虹藏不见——雨少了，彩虹不见了；二候天气上升地气下降——天上的气往上走，地上的气往下走；三候闭塞而成冬——天地闭住了，冬天就到了。")
f.gloss("hóng 虹 — 무지개 · bìsè 闭塞 — 닫힌, 막힌.")
f.end_report()

# col 3: frost + facts + reading box + 你呢
ix = COLX[3]
image(p, "frost.jpg", ix, 200, CW, 185)
cy3 = caption(p, ix, 385, CW, "带霜的红叶。冬天来了，早上能看见白白的霜，出门要加衣服。",
              "사진: Gerda Arendt — CC0 (Wikimedia Commons)")
facts = ["11月22日星期日 — 小雪",
         "第20个节气 — 冬天第2个",
         "11月 — 深圳读书月"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "节日小日历　축제 날짜", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ay3 = sy3 + sh + 26
rbox = ["读书月：11月1日开始，深圳七个文化场馆一起办活动。",
        "文化馆之夜：11月14日，亲手摸古籍、抄经典。"]
rh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 14 for t in rbox) + 30
p.rect(ix, ay3, CW, rh, fill=BOX)
yy3 = ay3 + 16
p.text(ix + 22, yy3 + 26, "读书月　독서의 달", 24, "sans", True, OLIVE)
yy3 += 52
for t in rbox:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 8
ey3 = ay3 + rh + 26
etvous = "你呢？你喜欢冬天吗？这个月，你在读什么书？写两句中文寄来。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("당신은요? 겨울이 좋나요? 이번 달에 무엇을 읽고 있나요? 중국어로 두 문장 써 보세요.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill=BOX)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "说说你自己　당신은요?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "당신은요? 겨울이 좋나요? 이번 달에 무엇을 읽고 있나요? 중국어로 두 문장 써 보세요.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "练习　연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8쪽　答案见第8版", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P3-ex")
e.head("A　读一读选一选　읽고 고르기", 25)
e.glossline("3쪽을 읽고 가장 좋은 답을 고르세요.")
e.ex("A2", "单选", "A", "소설(小雪)은 11월 22일입니다.",
     "小雪在哪天？ A. 11月22日 · B. 11月21日 · C. 11月15日", size=20, gap=6)
e.ex("A2", "单选", "A", "小雪는 24절기 중 20번째입니다.",
     "小雪是第几个节气？ A. 第20个 · B. 第24个 · C. 第2个", size=20, gap=6)
e.ex("A2", "单选", "A", "첫 번째 기후는 虹藏不见입니다.",
     "小雪三候的第一候是什么？ A. 虹藏不见 · B. 天气上升 · C. 闭塞而成冬", size=20, gap=6)
e.ex("A2", "单选", "A", "독서의 달은 11월 1일에 시작했어요.",
     "深圳读书月哪天开始？ A. 11月1日 · B. 11月14日 · C. 11月7日", size=20, gap=6)
e.ex("A2", "单选", "B", "문화의 밤은 11월 14일.",
     "文化馆之夜在哪天？ A. 11月7日 · B. 11月14日 · C. 11月1日", size=20, gap=6)
e.head("B　词语填空　단어 빈칸", 25)
e.glossline("각 빈칸에 맞는 단어를 넣으세요.")
e.ex("A2", "完成句子", "小雪", "xiǎoxuě — 소설; 11월 22일.",
     "11月22日是___。", instr="채우세요", size=20, gap=6)
e.ex("A2", "完成句子", "20", "小雪는 24절기 중 20번째입니다.",
     "小雪是二十四节气里的第___个。", instr="채우세요", size=20, gap=6)
e.ex("A2", "完成句子", "冷", "소설이 지나면 날씨가 더 추워진다.",
     "小雪之后，天气会更___。", instr="채우세요", size=20, gap=6)
e.ex("B1", "完成句子", "七", "일곱 곳이 독서의 달에 참여해요.",
     "读书月有___个场馆一起参加。", instr="채우세요", size=20, gap=6)
e.ex("B1", "完成句子", "古籍", "gǔjí — 오래된 책. 독자는 고서의 제본을 만져 볼 수 있어요.",
     "文化馆之夜，读者可以亲手摸一摸___的装帧。", instr="채우세요", size=20, gap=6)
e.head("C　数字与日期　숫자", 25)
e.glossline("3쪽 날짜와 숫자로 답하세요.")
e.ex("A2", "完成句子", "22", "소설은 11월 22일 일요일입니다.",
     "小雪在11月___日星期日。", instr="채우세요", size=20, gap=6)
e.ex("A2", "完成句子", "2", "小雪는 겨울의 두 번째 절기입니다.",
     "小雪是冬天第___个节气。", instr="채우세요", size=20, gap=6)
e.ex("B1", "完成句子", "14", "문화의 밤은 11월 14일.",
     "文化馆之夜在11月___日。", instr="채우세요", size=20, gap=6)
e.ex("A2", "完成句子", "1", "독서의 달은 11월 1일에 시작했어요.",
     "深圳读书月从11月___日开始。", instr="채우세요", size=20, gap=6)
e.head("D　词语配对　짝짓기", 25)
e.match_set("A2", "词汇配对",
            ["小雪", "三候", "保暖", "着凉"],
            ["天冷了，多穿衣服，别冻着",
             "二十四节气里的一个，11月22日",
             "不小心冷到了，身体不舒服",
             "古人看天气的三个变化"],
            ["b", "d", "a", "c"],
            ["小雪 = 소설, b", "三候 = 세 시기, d", "保暖 = 따뜻하게 하기, a", "着凉 = 몸이 차서 감기에 걸리다, c"],
            instr="단어를 맞추세요")
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-wenhua.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · 体育 (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("体育　스포츠", "Lucerna", "Level B1　S16 四强打完　월드 S16: 준결승 완료")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1180, tag="P4-feature")
f.title("S16：四强打完，决赛见", 32)
f.byline("Lucerna 편집부　읽기 수준 B1")
f.para("S16的淘汰赛打完了三分之二：四分之一决赛11月4日到7日打完，半决赛11月8日到9日打完。决赛在11月15日凌晨3点，纽约巴克莱中心，BLG对GEN。")
f.para("四分之一决赛：11月4日，IG 3比1打赢TES，中国队内战；11月5日，GEN 3比0打赢LYON；11月6日，BLG 3比0打赢DK；11月7日，T1 3比1打赢KC。全部是BO5，输了就回家。")
f.para("半决赛：11月8日，GEN 3比0打赢IG；11月9日，BLG 3比1打赢T1。IG时隔七年重返四强，半决赛输给了GEN，止步四强。两支中国队进了四强：IG和BLG。BLG赢了T1，这是中国队第一次在全球总决赛的BO5里打赢T1。")
f.para("决赛的两个队：GEN在S16一场没输，只丢了一小局——瑞士轮3胜0负（对LYON 2比1），八强3比0，半决赛3比0。BLG一路打赢了三支韩国队：瑞士轮2比0打赢HLE，八强3比0打赢DK，半决赛3比1打赢T1。")
f.para("本期截稿时是11月10日，总决赛还没打。谁是冠军？下一期再报。想看决赛的人，记得调好闹钟：北京时间11月15日凌晨3点。")
f.para("BO5是五局三胜，先赢三局的队拿冠军。决赛夜，先睡一觉，再起来看。")
f.gloss("sìqiáng 四强 — 마지막 네 팀, 준결승 진출 팀 · zhǐbù 止步 — 여기서 멈추다, 더 나아가지 못하다 · nàozhōng 闹钟 — 자명종 · wǔjú sānshèng 五局三胜 — 5전 3선승제: 3판 먼저 이기는 쪽이 승리.")
f.end_report()

# ---- schedule (cols 0-2) ----
ly = 1210
p.text(MX, ly + 26, "S16 赛程　S16 일정 (베이징 시간)", 26, "sans", True, OLIVE)
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
p.para(MX, syy + 14, "2026년 11월 9일 기준: 8강전과 준결승 완료. 결승은 마감(11월 10일) 당시 아직 치러지지 않았다. 출처: Sina, 扬子晚报, 中关村在线 경기 보도(11월 8〜9일), S16 관람 가이드(베이징 시간).", 20.5, "serif", False, GREY, 1323, 1.4)

# col 3: lan party + facts + match words
ix = COLX[3]
image(p, "lanparty.jpg", ix, 200, CW, 220)
cy3 = caption(p, ix, 420, CW, "一起打游戏的老照片（2003年，法国）。今天看比赛，更多人是在网上一起看直播。",
              "사진: Syced — CC0 (Wikimedia Commons)")
facts = ["11月8日 — GEN 3比0胜IG",
         "11月9日 — BLG 3比1胜T1",
         "11月15日 03:00 — 总决赛 BLG对GEN",
         "GEN今年 — 淘汰赛一局没输"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "体育小日历　스포츠 날짜", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ay3 = sy3 + sh + 26
mwords = [("四强", "sìqiáng — 마지막 네 팀."),
          ("止步", "zhǐbù — 여기서 멈추다, 더 나아가지 못하다."),
          ("闹钟", "nàozhōng — 자명종.")]
mh = 62 + sum(len(wrap(m[0] + " " + m[1], "serif", False, 21.5, CW - 44)) * 30.5 + 14 for m in mwords) + 30
p.rect(ix, ay3, CW, mh, fill=BOX)
yy3 = ay3 + 16
p.text(ix + 22, yy3 + 26, "看比赛的中文　경기 단어", 24, "sans", True, OLIVE)
yy3 += 52
for w_, d_ in mwords:
    yy3 = p.para(ix + 22, yy3 + 21, w_ + " " + d_, 21.5, "serif", False, INK, CW - 44, 1.42) + 8
print("P4 col3 ends", ay3 + mh)

# ---- P4 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "练习　연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8쪽　答案见第8版", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P4-ex")
e.head("A　读一读选一选　읽고 고르기", 25)
e.glossline("4쪽을 읽고 가장 좋은 답을 고르세요.")
e.ex("B1", "单选", "A", "IG는 8강전에서 TES를 3-1로 이겼다.",
     "四分之一决赛，IG打赢了哪个队？ A. TES · B. GEN · C. DK", size=20, gap=6)
e.ex("B1", "单选", "B", "GEN은 준결승에서 IG를 3-0으로 이겼다.",
     "半决赛，GEN打赢了哪个队？ A. T1 · B. IG · C. BLG", size=20, gap=6)
e.ex("B1", "单选", "C", "BLG는 준결승에서 T1을 3-1로 이겼다.",
     "半决赛，BLG打赢了哪个队？ A. LYON · B. KC · C. T1", size=20, gap=6)
e.ex("B1", "单选", "A", "결승은 11월 15일 03:00 베이징 시간입니다.",
     "决赛在哪天？ A. 11月15日凌晨3点 · B. 11月14日 · C. 11月8日", size=20, gap=6)
e.ex("B1", "单选", "A", "결승은 BLG 대 GEN입니다.",
     "决赛的两个队是？ A. BLG和GEN · B. IG和T1 · C. TES和DK", size=20, gap=6)
e.head("B　词语填空　단어 빈칸", 25)
e.glossline("각 빈칸에 맞는 단어를 넣으세요.")
e.ex("B1", "完成句子", "DK", "BLG는 8강전에서 DK를 3-0으로 이겼다.",
     "四分之一决赛，BLG 3比0打赢了___。", instr="채우세요", size=20, gap=6)
e.ex("B1", "完成句子", "IG", "GEN은 준결승에서 IG를 3-0으로 이겼다.",
     "半决赛，GEN 3比0打赢了___。", instr="채우세요", size=20, gap=6)
e.ex("B1", "完成句子", "BLG", "결승은 BLG 대 GEN입니다.",
     "决赛是___对GEN。", instr="채우세요", size=20, gap=6)
e.ex("B1", "完成句子", "3", "결승은 03:00 베이징 시간입니다.",
     "决赛在北京时间11月15日凌晨___点。", instr="채우세요", size=20, gap=6)
e.ex("B1", "完成句子", "T1", "BLG는 Worlds BO5에서 처음으로 T1을 이겼다.",
     "BLG是第一次在全球总决赛的BO5里打赢___。", instr="채우세요", size=20, gap=6)
e.head("C　读赛程　일정 읽기", 25)
e.glossline("4쪽 일정을 읽으세요.")
e.ex("B1", "完成句子", "4", "IG는 11월 4일에 TES를 이겼다.",
     "IG 3比1打赢TES，在11月___日。", instr="채우세요", size=20, gap=6)
e.ex("B1", "完成句子", "5", "GEN은 11월 5일에 LYON을 이겼다.",
     "GEN 3比0打赢LYON，在11月___日。", instr="채우세요", size=20, gap=6)
e.ex("B1", "完成句子", "6", "BLG는 11월 6일에 DK를 이겼다.",
     "BLG 3比0打赢DK，在11月___日。", instr="채우세요", size=20, gap=6)
e.ex("B1", "完成句子", "7", "T1은 11월 7일에 KC를 이겼다.",
     "T1 3比1打赢KC，在11月___日。", instr="채우세요", size=20, gap=6)
e.head("D　词语配对　짝짓기", 25)
e.match_set("B1", "词汇配对",
            ["四强", "止步", "闹钟", "五局三胜"],
            ["先赢三局的队拿冠军",
             "半决赛输了，就不往前走了",
             "到时间会响，叫你起床",
             "最后四支队，半决赛的队"],
            ["d", "b", "c", "a"],
            ["四强 = 마지막 네 팀, d", "止步 = 여기서 멈추다, b", "闹钟 = 자명종, c", "五局三胜 = 5전 3선승제, a"],
            instr="단어를 맞추세요")
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-tiyu.svg")
print("P4 saved, exercises so far:", len(REG))
