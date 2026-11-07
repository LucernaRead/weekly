# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zh-cn-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · 头版 (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 1 · 第 1 号", 23, "sans", True, OLIVE)
p.text(975, 92, "每周读中文 · 매주 진짜 중국어를 읽어요", 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "2026年10月19日（周一）— 25日（周日）", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, GOLD, 1.6)
p.text(975, 262, "Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "简体中文版 · VOL.1 · 双11 · 大闸蟹 · 霜降", 40, "serif", True, INK, anchor="middle")
p.text(975, 372, "给学中文的人的周报 — 진짜 중국을 중국어로 읽어요", 19, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)
# pairing badge: which text, which explanation language, which reader
p.text(975, 434, "중국어 간체 텍스트 · 한국어 해설 — 한국어 독자를 위한 판", 19.5, "sans", True, BRICK, anchor="middle")

# band
p.rect(MX, 458, RIGHT - MX, 118, fill=DARK)
p.text(MX + 30, 512, "双11到了「付尾款周」!周二晚 8 点,天猫付尾款", 36, "sans", True, "#f3edda")
p.text(MX + 30, 556, "京东已经开卖;现货一直卖到 11 月 13 日,这一周就能买。", 23, "serif", False, "#e8dfc8")
p.text(RIGHT - 30, 512, "付尾款周", 24, "sans", True, "#b3a06a", anchor="end")
p.text(RIGHT - 30, 556, "잔금 결제 주간 · 주요 시각은 2면에", 21, "sans", False, "#b3a06a", anchor="end")

# ---- headline (span cols 0-2) ----
hy = 580
p.text(MX, hy + 26, "头条 · 톱 기사", 22, "sans", True, BRICK)
hy = p.para(MX, hy + 92, "双11到了「付尾款」的这一周", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 30, "周二 20:00,天猫付尾款、现货开售——今年的购物季来得更早,也更长", 25, "serif", False, GREY)
hy += 46
p.text(MX, hy + 28, "Lucerna 편집부 · 읽기 수준 A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("今年的双11来得早。京东10月12日晚上8点就开始卖现货,10月20日晚上8点还有「开门红」。", size=24)
f.para("淘宝和天猫10月15日晚上8点开始预售。预售,就是先付一点定金,把看好的东西先订下来。", size=24)
f.para("10月20日晚上8点,是今年双11最重要的时间:大家付尾款,现货也同时开售。付完尾款,快递就开始送货了。", size=24)
f.para("现货会一直卖到11月13日。所以这一周,不用等11月11日,双11已经开始了。", size=24)
f.para("这一周,手机上最常见的话是:定金、尾款、满减、凑单、红包口令。第2版有双11日历和买东西的办法。", size=24)
f.para("这是《Lucerna》简体中文版第1号。每周,我们用简单的中文,带你读真正的中国新闻。欢迎你!", size=24)
f.gloss("yùshòu 预售 — 예약 판매: 판매일보다 먼저 주문하는 것 · dìngjīn 定金 — 계약금 · wěikuǎn 尾款 — 잔금, 나중에 내는 돈 · xiànhuò 现货 — 재고가 있는 상품, 바로 보낼 수 있는 물건이에요.")
f.box("数字看本周 · 숫자로 보는 이번 주", [
    ("10월 20일 20:00 — 티몰 잔금 결제 시작; 현물 판매도 시작", "serif", False, INK, 20, 1.35),
    ("11월 13일 — 현물 판매 기간의 마지막 날", "serif", False, INK, 20, 1.35),
    ("10월 15일 — 타오바오와 티몰의 예약 판매가 시작된 날", "serif", False, INK, 20, 1.35),
    ("8위 — 「大闸蟹价格」가 인기 검색 스냅샷에서 차지한 순위 (오른쪽 단)", "serif", False, INK, 20, 1.35),
])
f.head("即学即练 · 바로 연습", 25)
f.ex("A2", "完成句子", "12", "징둥 (JD.com)은 10월 12일에 현물 판매를 시작했어요.",
     "京东10月___日开始卖现货。", instr="빈칸 채우기", size=19.5, gap=6)
f.ex("A2", "完成句子", "10", "티몰 예약 판매는 10월에 시작했어요.",
     "天猫预售___月15日开始。", instr="빈칸 채우기", size=19.5, gap=6)
f.ex("A2", "完成句子", "8", "잔금 결제는 저녁 8시에 시작했어요.",
     "付尾款的时间是10月20日晚上___点。", instr="빈칸 채우기", size=19.5, gap=6)
f.ex("A2", "完成句子", "定金", "예약 판매에서는 먼저 계약금을 내요.",
     "预售的时候先付___。", instr="빈칸 채우기", size=19.5, gap=6)
f.ex("A2", "完成句子", "13", "현물 판매는 11월 13일까지예요.",
     "现货一直卖到11月___日。", instr="빈칸 채우기", size=19.5, gap=6)
f.ex("A2", "完成句子", "尾款", "잔금을 다 내면 배송이 시작돼요.",
     "付完___,快递就开始送货了。", instr="빈칸 채우기", size=19.5, gap=6)
f.end_report()

# ---- search heat box (col 3) ----
gx, gw = COLX[3], CW
gy = 580
p.rect(gx, gy, gw, 700, fill=BOX, stroke=LINE, sw=1.4)
p.text(gx + 22, gy + 40, "本周热搜 · 이번 주 인기 검색", 25, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "大家在搜什么 · 다들 무엇을 검색할까요", 22, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "웨이보 인기 검색 미러 스냅샷", 19, "sans", False, GREY)
topics = [
    "大闸蟹价格争议 — 第 8 位",
    "NBA 新赛季 — 第 9 位(热度约 34.9 万)",
    "中国体操男队世锦赛铜牌 — 第 19 位",
]
byy = gy + 150
for i, t in enumerate(topics):
    yy_t = p.para(gx + 22, byy + 22, f"{i+1}. {t}", 20, "serif", True, INK, gw - 44, 1.32)
    byy = yy_t + 10
p.para(gx + 22, byy + 12, "순위와 화제 수치는 10월 21일 00:30에 가져온 제3자 미러 스냅샷에서 온 거예요. 숫자는 대략적인 기준으로 봐 주세요. 세 가지 화제 모두 이번 호에서 다뤄요.", 18.5, "sans", False, GREY, gw - 44, 1.35)
p.text(gx + 22, gy + 636, "출처: 웨이보 인기 검색 미러 (rddh.cn)", 18.5, "sans", False, GREY)
p.text(gx + 22, gy + 664, "스냅샷: 2026-10-21 00:30", 19, "sans", False, GREY)

# ---- contents (col 3) ----
sy = 1296
p.rect(gx, sy, gw, 330, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(gx + 22, sy + 40, "本期目录 · 차례", 24, "sans", True, OLIVE)
som = [
    ("2版", "双11日历与本周生活", "A2"),
    ("3版", "重阳刚过,霜降要来", "A2→B1"),
    ("4版", "体操摘铜,NBA 开赛", "B1"),
    ("5版", "电竞 S16 与维密秀", "B1"),
    ("6版", "大闸蟹「价格崩盘」是真的吗", "B2"),
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
p.para(gx, my + 76, "「尾款」 wěikuǎn — 잔금: 가격에서 마지막으로 내는 부분이에요. 先付定金,后付尾款 (먼저 계약금을 내고, 나중에 잔금을 내요). 예: 「尾款付完,快递就来了。」", 21.5, "serif", False, INK, gw, 1.4)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "locker.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "快递柜(资料图)。付完尾款,这一周,包裹会陆续送到你手里。",
        "Photo: Map hobby — CC0 (Wikimedia Commons)")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2290, tag="P1-week")
f2.head("忙碌的一周", 25)
f2.para("这一周又买东西,又过节气:周五是霜降,秋天快要过完了。周六凌晨还有电竞比赛。先看好日历,再安排周末吧。", 22.5)
f2.end_report()
# col 3 brief box
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 1914, "快讯 · 단신", 24, "sans", True, OLIVE)
brefs = [
    ("霜降", "周五霜降:吃柿子,加衣服,看红叶。(第 3 版)"),
    ("体操", "中国体操男队在世锦赛拿到铜牌。(第 4 版)"),
    ("S16", "周六凌晨 1 点,S16 瑞士轮开打。(第 5 版)"),
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
qf.ex("A2", "单选", "A", "잔금 결제는 10월 20일에 시작했어요.",
      "天猫付尾款是哪一天? A. 10月20日 · B. 11月11日 · C. 10月15日", size=21)
qf.ex("A2", "单选", "B", "예약 판매에서는 먼저 계약금을 내요.",
      "预售的时候先付什么? A. 尾款 · B. 定金 · C. 快递费", size=21)
qf.ex("A2", "单选", "C", "게 화제는 스냅샷에서 8위였어요.",
      "「大闸蟹价格」在热搜快照里是第几位? A. 第 9 位 · B. 第 19 位 · C. 第 8 位", size=21)
qf.ex("A2", "单选", "A", "현물 판매는 11월 13일까지예요.",
      "现货一直卖到哪一天? A. 11月13日 · B. 11月11日 · C. 10月31日", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-touiban.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · 生活 (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("生活 · 생활", "Lucerna", "수준 A2 · 双11日历 · 霜降生活 · 달력과 늦가을 생활")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("双11日历:哪天付钱,哪天收货", 37)
f.byline("Lucerna 편집부 · 읽기 수준 A2")
f.para("双11不是一天,是一段时间。今年从10月中旬就开始了。先记住三个日子:10月15日、10月20日、11月13日。")
f.para("10月15日晚上8点,淘宝、天猫开始预售。预售时先付定金,把喜欢的东西订下来。定金不多,但付了定金,就要记得付尾款。")
f.para("10月20日晚上8点付尾款。尾款就是总价减去定金。付完尾款,商家就发货。京东10月20日晚上8点还有「开门红」,很多现货直接开卖。")
f.para("从10月20日到11月13日是现货期。不想等预售的人,可以在这段时间直接买。这一周包裹很多,收货可能比平时慢一点。")
f.gloss("zǒngjià 总价 — 전체 가격 · fāhuò 发货 — 상품을 보내는 것 · shāngjiā 商家 — 판매자, 가게예요.")
f.head("满减怎么玩 · 满减 이용법", 25)
f.para("가게에서는 「满300减50」 (300위안을 사면 50위안 할인) 같은 행사를 자주 해요. 이게 바로 满减 (mǎnjiǎn)이에요. 장바구니가 300위안에 못 미치면 작은 물건 하나를 더해 금액을 채우는데, 이게 凑单 (còudān)이에요. 아래 예시는 연습용 숫자를 써요.")
f.box("练习例子 · 연습 예시", [
    ("一件外套 260 元,一条围巾 60 元,一起 320 元。", "serif", False, INK, 20, 1.35),
    ("满 300 减 50,实付 270 元。先付定金 30 元,尾款是 270 − 30 = 240 元。", "serif", False, INK, 20, 1.35),
])
f.head("周五霜降:秋天的最后一个节气", 25)
f.para("10月23日,星期五,是霜降。霜降是二十四节气里的第十八个,也是秋天的最后一个节气。霜降以后,11月7日就是立冬,冬天要来了。")
f.para("霜降的时候,早上的草地上会有白白的霜。天气一天比一天冷,要记得加衣服。老话说:「补冬不如补霜降。」霜降时吃得好一点,冬天身体才好。")
f.para("霜降吃柿子。还有一句话:「霜降吃柿子,嘴唇不会裂。」这个周末,去看看红叶、吃一个柿子,就是很好的安排。")
f.gloss("jiéqì 节气 — 한 해를 나누는 24절기 · shuāng 霜 — 서리 · lìdōng 立冬 — 겨울의 시작 (11월 7일).")
f.box("本周生活小日历 · 이번 주 생활 달력", [
    ("周二 20:00 — 天猫付尾款,京东「开门红」", "serif", False, INK, 20, 1.35),
    ("周五 — 霜降:吃柿子,赏红叶,加衣服", "serif", False, INK, 20, 1.35),
    ("周六 01:00 — S16 瑞士轮开打(第 5 版)", "serif", False, INK, 20, 1.35),
])
f.end_report()

# col 3: valley image + facts + 你呢 (sequential, measured)
ix = COLX[3]
image(p, "valley.jpg", ix, 200, CW, 230)
cy3 = caption(p, ix, 430, CW, "秋天的山谷,红叶正当时。霜降前后,是看红叶的好时候。",
              "Photo: Paul Gilmore — CC0 (Wikimedia Commons)")
facts = ["霜降是二十四节气里的第 18 个。",
         "霜降以后是立冬,今年在 11 月 7 日。",
         "上周日(10 月 18 日)是重阳节,故事在第 3 版。"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "你知道吗 · 알고 있었나요?", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "你呢?你住的地方,霜降的时候冷不冷?这个双11,你想买什么?写两句中文寄来。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("여러분은요? 사는 곳은 추워졌나요? 이번 双11에 무엇을 사고 싶나요? 중국어로 두 문장을 써서 보내 주세요.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "说说你自己 · 여러분은요?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "여러분은요? 사는 곳은 추워졌나요? 이번 双11에 무엇을 사고 싶나요? 중국어로 두 문장을 써서 보내 주세요.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- word strip ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, GOLD, 2)
p.text(MX, dy + 28, "购物词语卡 · 쇼핑 단어 카드", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "쇼핑 앱마다 꼭 보이는 네 단어", 20, "sans", False, GREY, anchor="end")
words = [
    ("定金", "dìngjīn · 계약금", "가격의 일부, 먼저 내는 돈"),
    ("尾款", "wěikuǎn · 잔금", "가격의 마지막 부분"),
    ("满减", "mǎnjiǎn · 사고 할인받기", "금액을 채우면 가격이 내려가요"),
    ("红包", "hóngbāo · 붉은 봉투", "행운을 비는 붉은 봉투 속 돈"),
]
for i, (t, lab, en) in enumerate(words):
    bx = COLX[i]
    p.rect(bx, dy + 52, CW, 150, fill=BOX, stroke=LINE, sw=1.4)
    p.text(bx + 22, dy + 106, t, 34, "serif", True, OLIVE)
    yy = p.para(bx + 22, dy + 140, lab, 20.5, "serif", False, INK, CW - 44, 1.32)
    p.para(bx + 22, yy + 19, en, 19, "sans", False, GREY, CW - 44, 1.3)
p.para(MX, dy + 234, "이 문장을 기억해요: 「先付定金,后付尾款,买满三百还能减五十。」", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P2 exercises ----
ey = dy + 250
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "练习 · 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면 · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A · 读一读选一选 · 읽고 고르기", 25)
e.glossline("2면을 읽고 가장 좋은 답을 골라요.")
e.ex("A2", "单选", "A", "쇼핑 시즌의 첫 중요 날짜는 10월 15일이에요.",
     "双11第一个要记的日子是哪天? A. 10月15日 · B. 11月11日 · C. 11月13日", size=19, gap=6)
e.ex("A2", "单选", "B", "예약 판매에서는 먼저 계약금을 내요.",
     "预售的时候先付什么? A. 尾款 · B. 定金 · C. 全款", size=19, gap=6)
e.ex("A2", "单选", "A", "잔금을 내면 판매자가 상품을 발송해요.",
     "付完尾款以后,商家做什么? A. 发货 · B. 退定金 · C. 关门", size=19, gap=6)
e.ex("A2", "单选", "B", "霜降는 18번째 절기예요.",
     "霜降是第几个节气? A. 第16个 · B. 第18个 · C. 第24个", size=19, gap=6)
e.ex("A2", "单选", "A", "立冬는 霜降 다음에 와요.",
     "霜降以后是哪个节气? A. 立冬 · B. 冬至 · C. 寒露", size=19, gap=6)
e.head("B · 词语填空 · 단어 빈칸 채우기", 25)
e.glossline("빈칸에 알맞은 단어를 넣어요.")
e.ex("A2", "完成句子", "定金", "dìngjīn 定金 — 예약 판매에서 내는 계약금.",
     "预售时先付___。", instr="빈칸 채우기", size=19, gap=6)
e.ex("A2", "完成句子", "尾款", "wěikuǎn 尾款 — 전체 가격에서 계약금을 뺀 잔금.",
     "总价减去定金,就是___。", instr="빈칸 채우기", size=19, gap=6)
e.ex("A2", "完成句子", "满减", "mǎnjiǎn 满减 — 300위안을 사면 50위안 할인.",
     "买满300元便宜50元,这叫___。", instr="빈칸 채우기", size=19, gap=6)
e.ex("A2", "完成句子", "霜", "shuāng 霜 — 풀 위에 내린 하얀 서리.",
     "霜降的早上,草地上有白白的___。", instr="빈칸 채우기", size=19, gap=6)
e.ex("B1", "完成句子", "节气", "jiéqì 节气 — 霜降는 가을의 마지막 절기예요.",
     "二十四___里,霜降是秋天的最后一个。", instr="빈칸 채우기", size=19, gap=6)
e.head("C · 数字与日期 · 숫자와 날짜", 25)
e.glossline("이 면의 연습 예시를 이용해요.")
e.ex("A2", "完成句子", "260", "예시에서 코트는 260위안이에요.",
     "练习例子里,外套___元。", instr="빈칸 채우기", size=19, gap=6)
e.ex("A2", "完成句子", "320", "260 + 60 = 320위안 (합계).",
     "外套和围巾一起___元。", instr="빈칸 채우기", size=19, gap=6)
e.ex("B1", "完成句子", "270", "320 − 50 = 270위안 (할인 후).",
     "满减以后实付___元。", instr="빈칸 채우기", size=19, gap=6)
e.ex("B1", "完成句子", "240", "잔금은 270 − 30 = 240위안이에요.",
     "练习例子里的尾款是___元。", instr="빈칸 채우기", size=19, gap=6)
e.head("D · 词语配对 · 짝짓기", 25)
e.match_set("A2", "词汇配对",
            ["定金", "尾款", "满减", "节气"],
            ["划分一年的 24 个时间点",
             "先付的一小部分钱",
             "买满多少,便宜多少",
             "最后付的那部分钱"],
            ["b", "d", "c", "a"],
            ["dìngjīn 定金 = 먼저 내는 돈, b", "wěikuǎn 尾款 = 마지막에 내는 돈, d", "mǎnjiǎn 满减 = 사고 할인받기, c", "jiéqì 节气 = 24절기, a"],
            instr="단어와 뜻 짝짓기")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-shenghuo.svg")
print("P2 saved, exercises so far:", len(REG))
