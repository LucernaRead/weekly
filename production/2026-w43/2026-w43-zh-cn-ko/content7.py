# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zh-cn-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 词语精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("词语 · 단어 집중", "Lucerna", "语言聚焦 · 三个级别,三个主题 · 세 단계, 세 주제")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 购物与量词 · 양사", 24)
a.para("쇼핑할 때 중국어는 양사 (量词)를 써요: 一件外套 (코트 한 벌), 一条围巾 (목도리 한 장), 一斤蟹 (게 500그램), 一只蟹 (게 한 마리). 틀은 숫자 + 양사 + 명사 (数词 + 量词 + 名词)예요.", 21.5)
a.glossline("영어는 대략 세지만, 중국어는 물건의 종류마다 양사를 골라요 — 복수형도 -s도 없어요.")
a.ex("A2", "完成句子", "件", "外套의 양사는 件 (jiàn)이에요.",
     "我想买一___外套。", instr="빈칸 채우기", size=20.5, gap=10)
a.ex("A2", "单选", "B", "围巾의 양사는 条 (tiáo, 길고 부드러운 물건)이에요.",
     "「一条」可以说什么? A. 一条外套 · B. 一条围巾 · C. 一条大闸蟹", size=20.5, gap=10)
a.ex("A2", "完成句子", "斤", "斤 (jīn) — 500그램; 시장 가격은 1斤 단위예요.",
     "大闸蟹多少钱一___?", instr="빈칸 채우기", size=20.5, gap=10)
a.ex("A2", "单选", "A", "옷에는 件을 쓰고, 个나 条는 쓰지 않아요.",
     "哪个说法对? A. 一件衣服 · B. 一个衣服 · C. 一条衣服", size=20.5, gap=10)
a.para("하나 더 연습해요: 「这件外套多少钱?」 (이 코트는 얼마예요?) 쇼핑할 때는 먼저 가격을 묻고, 그다음에 내세요.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 时间与日期 · 시간과 날짜", 24)
b.para("중국어의 시간 표현은 큰 단위에서 작은 단위 순이에요: 연, 월, 일, 요일, 하루의 구분, 시. 예: 「10月20日晚上8点」 (10월 20일 저녁 8시) — 가장 큰 단위가 먼저 오고, 순서는 바뀌지 않아요.", 21.5)
b.glossline("그래서 영어 «Friday evening, Oct 23»는 중국어로 10月23日星期五晚上예요.")
b.ex("B1", "单选", "B", "凌晨 (língchén) — 자정이 지난 새벽 시간대예요.",
     "「凌晨3点」是什么时候? A. 下午3点 · B. 半夜3点 · C. 中午12点", size=20.5, gap=10)
b.ex("B1", "完成句子", "上午", "NBA는 베이징 시간 오전에 개막했어요.",
     "NBA 在北京时间10月21日___开打。(不是晚上)", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "单选", "A", "큰 단위에서 작은 단위 순: 10월 20일, 저녁, 8시.",
     "哪个顺序对? A. 10月20日晚上8点 · B. 8点晚上10月20日 · C. 晚上8点10月20日", size=20.5, gap=10)
b.ex("B1", "完成句子", "周五", "10월 23일은 금요일 — 周五예요.",
     "10月23日是星期五,也可以说___。霜降在这天。", instr="빈칸 채우기", size=20.5, gap=10)
b.para("단어 두 개 더: 凌晨 (língchén)은 자정이 지나고 새벽이 오기 전의 시간대이고, 傍晚 (bàngwǎn)은 어두워지기 직전의 짧은 시간이에요.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 读新闻 · 뉴스 읽기", 24)
c.para("논쟁 (争议)이 있는 기사에서는 문장을 세 종류로 나눠 보세요: 온라인 주장 (说法), 공식 발표 (声明), 시장 데이터 (数据). 주장은 과장될 수 있고, 데이터에는 출처와 날짜가 꼭 있어야 해요. 6면이 그 예예요: 「暴跌40%」는 주장, 77.5위안과 57.5위안은 데이터, 「崩盘不实」는 발표예요.", 21.5)
c.glossline("숫자마다 물어보세요: 누가, 언제 잰 걸까요?") 
c.ex("B2", "单选", "C", "「暴跌40%」는 온라인 주장이지 실측 데이터가 아니에요.",
     "「暴跌超过40%」在第6版里是什么? A. 数据 · B. 声明 · C. 网上的说法", size=20.5, gap=10)
c.ex("B2", "完成句子", "声明", "声明 (shēngmíng) — 협회의 공식 발표예요.",
     "协会10月19日发表___,说「崩盘」不是真的。", instr="빈칸 채우기", size=20.5, gap=10)
c.ex("B2", "单选", "B", "데이터와 출처가 먼저, 제목은 나중이에요.",
     "读新闻时,哪个做法最好? A. 只看标题 · B. 先看数据和出处 · C. 只看评论", size=20.5, gap=10)
c.ex("B2", "完成句子", "25.8", "6면에서 실제로 계산한 하락률은 25.8%예요.",
     "第6版真正算出的数据降幅是___%。", instr="빈칸 채우기", size=20.5, gap=10)
c.para("직접 해 보세요: 1면의 인기 검색 상자에서 「第 8 位」는 순위, 즉 데이터예요. 제목 속 단어는 주장이에요. 구별할 수 있나요?", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「他高兴的跳起来」", "→ 「他高兴地跳起来。」", "地 (de)는 동사 앞에 와서 동작의 모습을 나타내요."),
    ("「他跑的很快」", "→ 「他跑得很快。」", "得 (de)는 동사와 정도 보어를 이어 줘요: 跑得快."),
    ("「我买了三只大闸蟹个」", "→ 「我买了三只大闸蟹。」", "순서: 숫자 + 양사 + 명사. 마지막 个는 하나 남아요; 게에는 只를 써요."),
    ("「霜降在星期五十月二十三日」", "→ 「霜降在10月23日,星期五。」", "시간은 큰 단위에서 작은 단위 순: 월과 일이 먼저, 요일은 마지막이에요."),
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
wt = "「先付定金,后付尾款。」(먼저 계약금, 나중에 잔금.) 틀 先…后/再…는 동작의 순서를 나타내요. 또: 「先看天气,再出门。」「先洗手,再吃饭。」"
wcn = "틀: 先 … 后/再 … — 먼저 X, 그다음 Y. 나만의 문장을 만들어 보세요."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本周句式 · 이번 주 문형", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「你好!我住在多伦多。霜降那天,我吃了柿子,也给妈妈打了电话。我的购物车里有一件外套,还在等付尾款。」"
lcn = "편집부가 만든 예시 편지예요 — 실제 편지는 아니에요. VOL.2에서는 진짜 독자 편지와 8면 쓰기의 최고 작품을 실어요!"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
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
    ("「今年的双11来得早」", "올해 双11은 일찍 왔어요.", "p. 1"),
    ("「付完尾款，快递就开始送货了」", "잔금을 다 내면 배송이 시작돼요.", "p. 1"),
    ("「付完尾款，商家就发货」", "잔금을 내면 판매자가 발송해요.", "p. 2"),
    ("「遥知兄弟登高处，遍插茱萸少一人」", "王维의 유명한 重阳 시구예요.", "p. 3"),
    ("「两个分数只差2.735分」", "두 점수의 차이는 겨우 2.735점이에요.", "p. 4"),
    ("「最大的看点是詹姆斯」", "가장 큰 볼거리는 르브론이에요.", "p. 4"),
    ("「看S16，要通宵了」", "S16을 보려면 밤을 새워야 해요.", "p. 5"),
    ("「先看数据，再看标题」", "데이터가 먼저, 제목은 나중 (6면의 규칙).", "p. 6"),
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
p.text(MX + 28, py + 44, "下期预告 · 다음 호 예고 (VOL.2)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "S16 瑞士轮打完了:LPL 的四支队打得怎么样?双11 的包裹都到了吗?我们追踪报道。11月7日是立冬,冬天要来了。还有你们的来信和第 8 版最佳作文。下周见!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-ciyu.svg")
print("P7 saved, exercises so far:", len(REG))
