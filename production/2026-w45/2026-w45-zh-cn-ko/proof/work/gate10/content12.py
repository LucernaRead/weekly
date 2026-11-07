# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-cn-ko-proof/work/gate10/out"
os.makedirs(OUT, exist_ok=True)

# ================= P1 · 头版 (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 2 · 第 2 号", 23, "sans", True, OLIVE)
p.text(975, 92, "每周读中文 · 매주 진짜 중국어를 읽어요", 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "2026年11月2日（周一）— 8日（周日）", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, GOLD, 1.6)
p.text(975, 262, "Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "简体中文版 · VOL.2 · 双11 · 立冬 · S16", 40, "serif", True, INK, anchor="middle")
p.text(975, 372, "给学中文的人的周报 — 진짜 중국을 중국어로 읽어요", 19, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)
# pairing badge: which text, which explanation language, which reader
p.text(975, 434, "중국어 간체 텍스트 · 한국어 해설 — 한국어 독자를 위한 판", 19.5, "sans", True, BRICK, anchor="middle")

# band
p.rect(MX, 458, RIGHT - MX, 118, fill=DARK)
p.text(MX + 30, 512, "双11还在进行,周六就立冬了", 36, "sans", True, "#f3edda")
p.text(MX + 30, 556, "现货一直卖到 11 月 13 日,11 月 7 日星期六立冬,冬天要来了。", 23, "serif", False, "#e8dfc8")
p.text(RIGHT - 30, 512, "双11×立冬", 24, "sans", True, "#b3a06a", anchor="end")
p.text(RIGHT - 30, 556, "쇼핑 주간, 겨울을 만나다 · 2–3면 보기", 21, "sans", False, "#b3a06a", anchor="end")

# ---- headline (span cols 0-2) ----
hy = 580
p.text(MX, hy + 26, "头条 · 톱 기사", 22, "sans", True, BRICK)
hy = p.para(MX, hy + 92, "双11还在进行,冬天也要来了", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 30, "11月7日星期六立冬,现货一直卖到11月13日——这一周,先买东西,再迎冬天", 25, "serif", False, GREY)
hy += 46
p.text(MX, hy + 28, "Lucerna 편집부 · 읽기 수준 A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("今年的双11已经开始了。京东10月12日晚上8点开始卖现货,淘宝和天猫10月15日晚上8点开始预售,10月20日晚上8点付尾款、现货开售。", size=24)
f.para("现货会一直卖到11月13日。所以这一周,不用等11月11日,双11已经在进行了。", size=24)
f.para("这一周还有一件大事:11月7日星期六是立冬。立冬是冬天的第一个节气,冬天要来了。", size=24)
f.para("买东西的时候,今年的规则更简单了:很多商品直接降价,不用再算复杂的满减。买之前,还可以问一问AI助手,比一比价格。", size=24)
f.para("11月7日星期六,还有一部新电影上映:《我们仅有一次的人生》。第5版有介绍。", size=24)
f.para("这是《Lucerna》简体中文版第2号。每周,我们用简单的中文,带你读真正的中国新闻。欢迎你!", size=24)
f.gloss("xiànhuò 现货 — 재고가 있는 상품, 바로 보낼 수 있어요 · lìjiǎn 立减 — 결제할 때 바로 깎아 주는 할인 · zhíjiàng 直降 — 가격 자체를 내리는 것 · jiéqì 节气 — 한 해를 나누는 24절기.")
f.box("数字看本周 · 숫자로 보는 이번 주", [
    ("11월 13일 — 현물 판매 기간의 마지막 날", "serif", False, INK, 20, 1.35),
    ("11월 7일 토요일 — 立冬 (입동)", "serif", False, INK, 20, 1.35),
    ("10월 12일 20:00 — 징둥 현물 판매 시작", "serif", False, INK, 20, 1.35),
    ("11월 10일 20:00 — 고조 판매(高潮场)는 다음 주에 시작", "serif", False, INK, 20, 1.35),
])
f.head("即学即练 · 바로 연습", 25)
f.ex("A2", "完成句子", "10", "징둥 현물 판매는 10월 12일에 시작했어요.",
     "京东___月12日开始卖现货。", instr="빈칸 채우기", size=19.5, gap=6)
f.ex("A2", "完成句子", "预售", "타오바오와 티몰 예약 판매는 10월 15일에 시작했어요.",
     "淘宝和天猫10月15日开始___。", instr="빈칸 채우기", size=19.5, gap=6)
f.ex("A2", "完成句子", "13", "현물 판매는 11월 13일까지 계속돼요.",
     "现货一直卖到11月___日。", instr="빈칸 채우기", size=19.5, gap=6)
f.ex("A2", "完成句子", "立冬", "입동은 11월 7일 토요일이에요.",
     "11月7日星期六是___。", instr="빈칸 채우기", size=19.5, gap=6)
f.ex("A2", "完成句子", "一", "입동은 겨울의 첫 번째 절기예요.",
     "立冬是冬天的第___个节气。", instr="빈칸 채우기", size=19.5, gap=6)
f.ex("A2", "完成句子", "降价", "올해는 많은 상품이 직접 인하돼요.",
     "今年的规则更简单了:很多商品直接___。", instr="빈칸 채우기", size=19.5, gap=6)
f.end_report()

# ---- this-week calendar box (col 3) ----
gx, gw = COLX[3], CW
gy = 580
p.rect(gx, gy, gw, 700, fill=BOX, stroke=LINE, sw=1.4)
p.text(gx + 22, gy + 40, "本周日历 · 이번 주 달력", 25, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "11月2日—8日 · 11월 2–8일", 22, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "이번 주에는 무슨 일이 있을까요", 19, "sans", False, GREY)
topics = [
    "周一 11月2日 — 双11现货进行时",
    "周三—周六早上6点 — S16四分之一决赛",
    "周六 11月7日 — 立冬,新片上映",
    "周日 11月8日 — 中国记者节,S16半决赛",
]
byy = gy + 150
for i, t in enumerate(topics):
    yy_t = p.para(gx + 22, byy + 22, f"{i+1}. {t}", 20, "serif", True, INK, gw - 44, 1.32)
    byy = yy_t + 10
p.para(gx + 22, byy + 12, "스위스 스테이지는 11월 1일에 끝나서, 마감 당시 8강 진출 팀은 아직 정해지지 않았어요. 8강전은 11월 4–7일, 첫 준결승은 11월 8일, 모두 베이징 시간 06:00에 열려요.", 18.5, "sans", False, GREY, gw - 44, 1.35)
p.text(gx + 22, gy + 636, "모든 시각은 베이징 시간", 18.5, "sans", False, GREY)
p.text(gx + 22, gy + 664, "S16 출전 팀은 스위스 스테이지 결과에 달려 있어요", 19, "sans", False, GREY)

# ---- contents (col 3) ----
sy = 1296
p.rect(gx, sy, gw, 330, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(gx + 22, sy + 40, "本期目录 · 차례", 24, "sans", True, OLIVE)
som = [
    ("2版", "双11与立冬生活", "A2"),
    ("3版", "立冬:冬天的第一个节气", "A2→B1"),
    ("4版", "S16:出局与冲八强", "B1"),
    ("5版", "AI电影与立冬新片", "B1"),
    ("6版", "双11深读:规则变简单了", "B2"),
    ("7版", "词语精讲", "A2→B2"),
    ("8版", "测验与答案", "全部"),
]
yy = sy + 82
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, BRICK)
    p.text(gx + 108, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 37

# ---- word of the week (col 3) ----
my = 1636
p.text(gx, my + 24, "本周词 · 이번 주의 단어", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, GOLD, 2)
p.para(gx, my + 76, "「立冬」 lìdōng — 입동: 겨울의 첫 번째 절기. 立冬到了,冬天要来了。예문: 「立冬那天,我们吃饺子。」", 21.5, "serif", False, INK, gw, 1.4)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "locker.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "快递柜(资料图)。现货期里,包裹会陆续送到你手里。",
        "Photo: Map hobby — CC0 (Wikimedia Commons)")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2290, tag="P1-week")
f2.head("忙碌的一周", 25)
f2.para("这一周又买东西,又迎冬天:周六立冬,周日还有半决赛。先看好日历,再安排周末吧。", 22.5)
f2.end_report()
# col 3 brief box
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 1914, "快讯 · 단신", 24, "sans", True, OLIVE)
brefs = [
    ("立冬", "周六立冬:北方吃饺子,南方吃法各不同。(第 3 版)"),
    ("S16", "一号种子AL出局,IG、TES、BLG冲八强。(第 4 版)"),
    ("电影", "AI电影票房遇冷,大家在争AI能不能拍电影。(第 5 版)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, BRICK)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- lightning quiz ----
qy = 2312
p.hline(MX, RIGHT, qy, GOLD, 2)
p.text(MX, qy + 36, "闪电问答 · 번개 퀴즈", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "1면을 읽고 고르세요 · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", "单选", "A", "현물 판매는 11월 13일까지 계속돼요.",
      "现货一直卖到哪一天? A. 11月13日 · B. 11月11日 · C. 10月20日", size=21)
qf.ex("A2", "单选", "B", "입동은 11월 7일 토요일이에요.",
      "立冬在11月几日? A. 11月1日 · B. 11月7日 · C. 11月11日", size=21)
qf.ex("A2", "单选", "C", "징둥 현물 판매는 10월 12일에 시작했어요.",
      "京东现货从哪天开始? A. 10月15日 · B. 10月20日 · C. 10月12日", size=21)
qf.ex("A2", "单选", "A", "올해는 많은 상품이 직접 인하돼요.",
      "今年双11,很多商品怎么便宜? A. 直接降价 · B. 必须先付定金 · C. 只有11月11日便宜", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-touiban.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · 生活 (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("生活 · 생활", "Lucerna", "수준 A2 · 双11购物生活 · 立冬生活 · 쇼핑과 겨울의 첫날들")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("双11购物生活:现货、直降,还有AI帮忙", 37)
f.byline("Lucerna 편집부 · 읽기 수준 A2")
f.para("双11不是一天,是一段时间。京东从10月12日开始卖现货,淘宝和天猫从10月20日开始卖现货,现货一直卖到11月13日。")
f.para("今年和以前不一样:以前要先付定金、等付尾款,现在很多商品直接就是现货。现货就是已经在仓库里的货,下单就能发货。")
f.para("规则也更简单了。以前常见的跨店满减少了,更多是官方立减和商品直降:价格直接变低,不用再算来算去。买之前,还可以问一问AI助手,比如豆包的「买前问豆包」,比一比价格、看一看评价。")
f.para("微信小店今年第一次参加双11,活动从10月12日到11月15日,一共35天。第18个双11,有了新平台,也有了新玩法。")
f.para("这一周,冬天也要来了。11月7日星期六立冬,天气会一天比一天冷。厚外套、围巾、帽子,是很多人购物车里的东西。买之前,先看好尺码,再看退换货的规则。")
f.gloss("cāngkù 仓库 — 창고 · píngjià 评价 — 후기, 구매자가 하는 말 · chǐmǎ 尺码 — 사이즈 · tuìhuànhuò 退换货 — 반품과 교환.")
f.head("满减与直降 · 예전 방식과 새 방식", 25)
f.para("많은 쇼핑객이 알던 예전 규칙은 「满300减50」(300위안을 쓰면 50위안을 아끼는 것)이었어요. 올해 흔한 방식은 直降 (zhíjiàng)이에요: 가격 자체가 내려가고, 결제 페이지 가격이 곧 지불 가격이에요. 아래 예시는 연습용 숫자이지 실제 상점 가격이 아니에요.")
f.box("연습 예시 · 练习例子", [
    ("一件毛衣 240 元,一条围巾 80 元,一起 320 元。", "serif", False, INK, 20, 1.35),
    ("直降 50 元,实付 270 元。先看结算页,再决定买不买。", "serif", False, INK, 20, 1.35),
])
f.head("立冬生活:加衣服,吃点热的", 25)
f.para("立冬是冬天的开始,但不是每个地方同时变冷。中国南北很大,有的地方立冬还很暖和,有的地方已经要穿棉衣了。")
f.para("北方很多地方立冬吃饺子,因为「饺子」和「交子」声音很像,是秋冬交替的意思。南方有的地方吃鸡鸭鱼肉,有的地方吃汤圆、糍粑,都是补冬:冬天以前,吃点好的,身体暖和。")
f.para("11月上旬,有的学校要期中考试,日子各不相同,不是全国统一的日子。考试周里,早点睡觉,比熬夜更重要。")
f.gloss("bǔdōng 补冬 — 겨울을 앞두고 잘 먹기 · jiāozǐ 饺子 — 만두 · cíbā 糍粑 — 찹쌀떡 · qīzhōng 期中 — 중간고사.")
f.box("本周生活小日历 · 이번 주 생활 달력", [
    ("周六 11月7日 — 立冬:吃饺子,加衣服", "serif", False, INK, 20, 1.35),
    ("周日 11月8日 — 中国记者节", "serif", False, INK, 20, 1.35),
    ("下周二 11月10日 20:00 — 双11高潮场开始", "serif", False, INK, 20, 1.35),
])
f.end_report()

# col 3: valley image + facts + 你呢 (sequential, measured)
ix = COLX[3]
image(p, "valley.jpg", ix, 200, CW, 230)
cy3 = caption(p, ix, 430, CW, "秋天的山谷,红叶正当时。立冬以后,秋天就真的要过去了。",
              "Photo: Paul Gilmore — CC0 (Wikimedia Commons)")
facts = ["现货期到 11 月 13 日。",
         "立冬在 11 月 7 日星期六。",
         "微信小店活动到 11 月 15 日。"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "你知道吗 · 알고 있었나요?", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "你呢?这个双11,你想买什么?立冬那天,你想吃什么?写两句中文寄来。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("여러분은요? 이번 双11에 무엇을 사고 싶나요? 立冬에는 무엇을 먹고 싶나요? 중국어로 두 문장을 써서 보내 주세요.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "说说你自己 · 여러분은요?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "여러분은요? 이번 双11에 무엇을 사고 싶나요? 立冬에는 무엇을 먹고 싶나요? 중국어로 두 문장을 써서 보내 주세요.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- word strip ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, GOLD, 2)
p.text(MX, dy + 28, "购物词语卡 · 쇼핑 단어 카드", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "쇼핑 앱마다 보이는 네 단어", 20, "sans", False, GREY, anchor="end")
words = [
    ("现货", "xiànhuò · 재고 상품", "지금 재고가 있어 바로 발송돼요"),
    ("直降", "zhíjiàng · 직접 인하", "가격이 직접 내려가서 계산이 필요 없어요"),
    ("立减", "lìjiǎn · 즉시 할인", "결제할 때 바로 깎여요"),
    ("补冬", "bǔdōng · 겨울을 앞두고 잘 먹기", "겨울을 앞두고 잘 먹는 것"),
]
for i, (t, lab, en) in enumerate(words):
    bx = COLX[i]
    p.rect(bx, dy + 52, CW, 150, fill=BOX, stroke=LINE, sw=1.4)
    p.text(bx + 22, dy + 106, t, 34, "serif", True, OLIVE)
    yy = p.para(bx + 22, dy + 140, lab, 20.5, "serif", False, INK, CW - 44, 1.32)
    p.para(bx + 22, yy + 19, en, 19, "sans", False, GREY, CW - 44, 1.3)
p.para(MX, dy + 222, "이 문장을 기억하세요: 「买现货不用等,先看结算页,再付款。」", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P2 exercises ----
ey = dy + 250
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "练习 · 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면 · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A · 读一读选一选 · 읽고 고르기", 25)
e.glossline("2면을 읽고 가장 좋은 답을 골라요.")
e.ex("A2", "单选", "A", "징둥 현물 판매는 10월 12일에 시작했어요.",
     "京东现货从哪天开始? A. 10月12日 · B. 10月15日 · C. 10月20日", size=19, gap=6)
e.ex("A2", "单选", "B", "타오바오와 티몰 현물 판매는 10월 20일에 시작했어요.",
     "淘宝和天猫现货从哪天开始? A. 10月12日 · B. 10月20日 · C. 11月11日", size=19, gap=6)
e.ex("A2", "单选", "A", "直降은 가격 자체가 내려간다는 뜻이에요.",
     "直降是什么意思? A. 价格直接变低 · B. 必须先付定金 · C. 只有11月11日便宜", size=19, gap=6)
e.ex("A2", "单选", "A", "立冬이 지나면 날씨는 하루하루 추워져요.",
     "立冬以后天气怎么样? A. 一天比一天冷 · B. 一天比一天热 · C. 完全不变", size=19, gap=6)
e.ex("A2", "单选", "B", "웨이신 상점 행사는 11월 15일까지 계속돼요.",
     "微信小店活动到哪天? A. 11月13日 · B. 11月15日 · C. 11月11日", size=19, gap=6)
e.head("B · 词语填空 · 단어 빈칸 채우기", 25)
e.glossline("빈칸에 알맞은 단어를 넣어요.")
e.ex("A2", "完成句子", "现货", "xiànhuò — 재고가 있는 상품, 바로 보낼 수 있어요.",
     "已经在仓库里的货,叫___。", instr="빈칸 채우기", size=19, gap=6)
e.ex("A2", "完成句子", "直降", "zhíjiàng — 가격 자체가 내려가요.",
     "价格直接变低,这叫___。", instr="빈칸 채우기", size=19, gap=6)
e.ex("A2", "完成句子", "补冬", "bǔdōng — 겨울을 앞두고 잘 먹기.",
     "冬天以前吃点好的,这叫___。", instr="빈칸 채우기", size=19, gap=6)
e.ex("A2", "完成句子", "饺子", "jiǎozǐ — 북방 가정은 立冬에 이것을 먹어요.",
     "北方很多地方立冬吃___。", instr="빈칸 채우기", size=19, gap=6)
e.ex("B1", "完成句子", "期中", "qīzhōng — 일부 학교의 중간고사는 11월 초에 있어요.",
     "11月上旬,有的学校要___考试。", instr="빈칸 채우기", size=19, gap=6)
e.head("C · 数字与日期 · 숫자와 날짜", 25)
e.glossline("이 면의 연습 예시를 이용해요.")
e.ex("A2", "完成句子", "240", "예시에서 스웨터는 240위안이에요.",
     "练习例子里,毛衣___元。", instr="빈칸 채우기", size=19, gap=6)
e.ex("A2", "完成句子", "320", "240 + 80 = 320위안, 합쳐서.",
     "毛衣和围巾一起___元。", instr="빈칸 채우기", size=19, gap=6)
e.ex("B1", "完成句子", "270", "320 − 50 = 270위안, 직접 인하 후.",
     "直降以后实付___元。", instr="빈칸 채우기", size=19, gap=6)
e.ex("B1", "完成句子", "35", "웨이신 상점 행사는 모두 35일 동안 열려요.",
     "微信小店活动一共___天。", instr="빈칸 채우기", size=19, gap=6)
e.head("D · 词语配对 · 짝짓기", 25)
e.match_set("A2", "词汇配对",
            ["现货", "直降", "立减", "补冬"],
            ["冬天以前吃点好的,身体暖和",
             "已经在仓库里,马上就能发走",
             "结算时直接减掉的钱",
             "商品价格直接变低"],
            ["b", "d", "c", "a"],
            ["xiànhuò 现货 = 재고 있음, b", "zhíjiàng 直降 = 가격 인하, d", "lìjiǎn 立减 = 결제 시 할인, c", "bǔdōng 补冬 = 겨울을 앞두고 잘 먹기, a"],
            instr="단어와 뜻 짝짓기")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-shenghuo.svg")
print("P2 saved, exercises so far:", len(REG))
