# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-cn-ko-proof/work/gate10/out"
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 词语精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("词语 · 단어 집중", "Lucerna", "语言聚焦 · 三个级别,三个主题 · 세 단계, 세 주제")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 双11与冬天 · 쇼핑", 24)
a.para("이번 주 쇼핑 단어: 现货 (xiànhuò, 재고 있음), 直降 (zhíjiàng, 직접 인하), 立减 (lìjiǎn, 결제 시 즉시 할인), 结算页 (jiésuàn yè, 결제 페이지). 겨울 단어: 立冬 (lìdōng, 입동), 补冬 (bǔdōng, 겨울을 앞두고 잘 먹기), 厚衣服 (hòu yīfu, 따뜻한 옷).", 21.5)
a.glossline("양사는 여전히 중요해요: 一件毛衣 (스웨터 한 벌), 一条围巾 (목도리 하나), 一部电影 (영화 한 편).")
a.ex("A2", "完成句子", "件", "毛衣에는 양사 件 jiàn을 써요.",
     "我想买一___毛衣。", instr="빈칸 채우기", size=20.5, gap=10)
a.ex("A2", "单选", "A", "直降은 가격 자체가 내려간다는 뜻이에요.",
     "「直降」是什么意思? A. 价格直接变低 · B. 必须先付定金 · C. 只有11月11日便宜", size=20.5, gap=10)
a.ex("A2", "完成句子", "立冬", "lìdōng — 입동, 11월 7일.",
     "11月7日是___。", instr="빈칸 채우기", size=20.5, gap=10)
a.ex("A2", "单选", "A", "옷에는 件을 쓰고, 个나 条는 쓰지 않아요.",
     "哪个说法对? A. 一件毛衣 · B. 一个毛衣 · C. 一条毛衣", size=20.5, gap=10)
a.para("하나 더 연습해요: 「这件毛衣多少钱?」(이 스웨터는 얼마예요?) 쇼핑할 때는 먼저 가격을 묻고, 그다음에 결제하세요.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 时间与日期 · 시간과 날짜", 24)
b.para("중국어는 시간을 큰 단위에서 작은 단위 순으로 말해요: 연, 월, 일, 요일, 하루 중 시간대, 시각. 이번 호의 예: 「11月7日星期六17点52分」(11월 7일 토요일 17:52), 「11月10日星期二20点」(11월 10일 화요일 20:00), 「11月15日凌晨3点」(11월 15일 새벽 3시). 가장 큰 단위가 먼저, 순서가 바뀌지 않아요.", 21.5)
b.glossline("그래서 영어 «Saturday evening, Nov 7»는 중국어로 11月7日星期六晚上이 돼요.")
b.ex("B1", "单选", "B", "凌晨 língchén — 자정 이후의 이른 새벽 시간.",
     "「凌晨3点」是什么时候? A. 下午3点 · B. 半夜3点 · C. 中午12点", size=20.5, gap=10)
b.ex("B1", "完成句子", "早上", "06:00은 早上(아침)이지 저녁이 아니에요.",
     "四分之一决赛在北京时间11月4日___6点开始。(不是晚上)", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "单选", "A", "큰 단위에서 작은 단위 순: 11월 7일, 토요일, 17:52.",
     "哪个顺序对? A. 11月7日星期六17点52分 · B. 17点52分星期六11月7日 · C. 星期六17点52分11月7日", size=20.5, gap=10)
b.ex("B1", "完成句子", "周六", "11월 7일은 토요일, 즉 周六예요.",
     "11月7日是星期六,也可以说___。立冬在这天。", instr="빈칸 채우기", size=20.5, gap=10)
b.para("두 단어 더: 凌晨 (língchén)은 자정 이후 새벽 전의 이른 시간, 傍晚 (bàngwǎn)은 어두워지기 직전의 짧은 시간이에요.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 读新闻 · 뉴스 읽기", 24)
c.para("기사에서 주장(说法)이 나오면 세 종류의 문장을 구분하세요: 주장(说法), 데이터(数据), 광고(广告). 6면이 그 예예요: 「最低价」는 주장이고, 연습 장바구니의 270元은 연습용 데이터이며, 결제 페이지에 실제로 내는 금액이 나와요.", 21.5)
c.glossline("모든 가격에 물어보세요: 누구의 숫자이고, 어디에 적혀 있나요?")
c.ex("B2", "单选", "C", "「最低价」는 측정된 데이터가 아니라 광고 문구예요.",
     "「最低价」在第6版里是什么? A. 数据 · B. 声明 · C. 说法", size=20.5, gap=10)
c.ex("B2", "完成句子", "数据", "shùjù — 측정된 숫자이지 주장이 아니에요.",
     "买东西以前,先看___,再看广告。", instr="빈칸 채우기", size=20.5, gap=10)
c.ex("B2", "单选", "B", "데이터와 결제 페이지를 먼저, 헤드라인은 나중에.",
     "读新闻时,哪个做法最好? A. 只看标题 · B. 先看数据和结算页 · C. 只看评论", size=20.5, gap=10)
c.ex("B2", "完成句子", "结算", "jiésuàn — 결제 페이지에 실제 가격이 나와요.",
     "真正要付的钱,看___页的价格。", instr="빈칸 채우기", size=20.5, gap=10)
c.para("직접 해 보세요: 1면 달력 상자에서 「11月7日」는 날짜, 즉 데이터예요. 광고 속 말은 주장이에요. 둘을 구분할 수 있나요?", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「他高兴的跳起来」", "→ 「他高兴地跳起来。」", "地 (de)는 동작 방식을 나타내요."),
    ("「他跑的很快」", "→ 「他跑得很快。」", "得 (de)는 동사와 정도를 연결해요: 跑得快."),
    ("「我买了三只毛衣个」", "→ 「我买了三件毛衣。」", "순서: 숫자 + 양사 + 명사. 마지막 个는 하나가 많아요. 스웨터에는 件을 써요."),
    ("「立冬在星期六十一月七日」", "→ 「立冬在11月7日,星期六。」", "시간은 큰 단위에서 작은 단위 순으로, 요일이 마지막이에요."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易错诊所 · 실수 클리닉", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「先看评价,再下单。」(먼저 후기를 보고, 그다음 주문하세요.) 문형 先…再…는 행동의 순서를 나타내요. 더 보기: 「先看天气,再出门。」"
wcn = "문형: 先 … 再 … — 먼저 X, 그다음 Y."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本周句式 · 이번 주 문형", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「你好!我住在上海。立冬那天,我吃了饺子,也给妈妈打了电话。双11,我买了一件毛衣,现货第二天就到了。」"
lcn = "编辑部示例信,不是真实来信。编辑部说明:VOL.1曾预告本期(VOL.2)刊登真实读者来信和VOL.1第8版最佳作文;至今没有收到真实来信,也没有可刊登的投稿,所以本期仍刊登编辑部示例,并继续征集。延期不是取消。편집자 주: VOL.1에서 약속한 실제 독자 편지와 VOL.1 8면 우수 작문은 아직 도착하지 않아, 이번 호에도 편집부 예시를 싣습니다. 연기가 취소는 아닙니다. 여러분의 편지와 작문을 보내 주세요!"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
# NOTE: the disclosure above mixes Chinese and English in one string; the
# sans wrap measures CJK and Latin with the same SC face, so the height
# formula above (sans, 20pt) matches the render path. Verified in the build log.
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "读者园地 · 독자 마당", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "本周金句 · 이번 주의 문장 (이 호 기사에서 그대로 인용)", 27, "sans", True, OLIVE)
quotes = [
    ("「不用等11月11日」", "11월 11일을 기다릴 필요가 없어요.", "p. 1"),
    ("「下单就能发货」", "주문하면 바로 발송돼요.", "p. 2"),
    ("「先看结算页,再付款」", "결제 페이지를 확인하고, 그다음 결제하세요.", "p. 2"),
    ("「水开始结冰」", "물이 얼기 시작해요.", "p. 3"),
    ("「三场都输了」", "세 시리즈를 모두 졌어요.", "p. 4"),
    ("「小局一场没赢」", "한 게임도 이기지 못했어요.", "p. 4"),
    ("「故事够不够好」", "그런데 이야기가 충분히 좋을까요?", "p. 5"),
    ("「别以后,就现在」", "나중이 아니라 지금.", "p. 5"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, en, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 150
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, en + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 150 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "下期预告 · 다음 호 예고 (VOL.3)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "双11当天11月11日星期三,包裹到了吗?S16淘汰赛打完了,谁进了决赛?总决赛北京时间11月15日凌晨3点。还有你们的来信和第8版最佳作文。下周见!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-ciyu.svg")
print("P7 saved, exercises so far:", len(REG))
