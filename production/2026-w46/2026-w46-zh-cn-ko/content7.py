# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-zh-cn-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 词语精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("词语 · 언어 포커스", "Lucerna", "语言聚焦 · 三个级别,三个主题 · 세 수준, 세 주제")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 双11与包裹 · 쇼핑", 24)
a.para("이번 주 쇼핑 단어: 高潮场 (gāocháochǎng, 피크 세일 기간), 包裹 (bāoguǒ, 소포), 取件码 (qǔjiànmǎ, 수령 코드), 快递柜 (kuàidìguì, 택배 보관함). 안전 단어: 消防 (xiāofáng, 화재 예방), 疏散 (shūsàn, 대피하다), 自救 (zìjiù, 자기 구조).", 21.5)
a.glossline("양사는 여전히 중요해요: 一个包裹 (소포 하나), 一部电影 (영화 한 편), 一场演练 (훈련 한 번).")
a.ex("A2", "完成句子", "个", "包裹 는 양사 个 gè 를 써요.",
     "我拿了___包裹。", instr="채우세요", size=20.5, gap=10)
a.ex("A2", "单选", "A", "高潮场 는 피크 세일 기간이라는 뜻이에요.",
     "「高潮场」是什么意思? A. 最忙的卖货时间 · B. 必须先付定金 · C. 只有11月11日便宜", size=20.5, gap=10)
a.ex("A2", "完成句子", "消防", "xiāofáng — 화재 예방, 11월 9일.",
     "11月9日是全国___日。", instr="채우세요", size=20.5, gap=10)
a.ex("A2", "单选", "A", "소포는 个 를 써요 — 只 나 条 가 아니에요.",
     "哪个说法对? A. 一个包裹 · B. 一只包裹 · C. 一条包裹", size=20.5, gap=10)
a.para("연습 하나 더: 「我的包裹到了吗?」(내 소포 도착했나요?) 소포를 기다릴 때는 먼저 물어보고, 그다음 보관함으로 가세요.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 时间与日期 · 시간과 날짜", 24)
b.para("중국어는 시간을 큰 것부터 작게 말해요: 연, 월, 일, 요일, 시간대, 시. 이번 호의 예: 「11月9日星期一」(11월 9일 월요일), 「11月10日星期二20点」(11월 10일 화요일 20시), 「11月15日星期日凌晨3点」(11월 15일 일요일 새벽 3시). 가장 큰 단위가 먼저, 순서는 바뀌지 않아요.", 21.5)
b.glossline("영어 «Monday, Nov 9»는 11月9日星期一 가 돼요.")
b.ex("B1", "单选", "B", "凌晨 língchén — 자정 이후의 깊은 밤.",
     "「凌晨3点」是什么时候? A. 下午3点 · B. 半夜3点 · C. 中午12点", size=20.5, gap=10)
b.ex("B1", "完成句子", "早上", "06:00은 早上 (아침)이에요 — 저녁이 아니에요.",
     "四分之一决赛在北京时间11月4日___6点开始。(不是晚上)", instr="채우세요", size=20.5, gap=10)
b.ex("B1", "单选", "A", "큰 순서 → 작은 순서: 11월 15일, 일요일, 03:00.",
     "哪个顺序对? A. 11月15日星期日凌晨3点 · B. 凌晨3点星期日11月15日 · C. 星期日凌晨3点11月15日", size=20.5, gap=10)
b.ex("B1", "完成句子", "周一", "11월 9일은 월요일 — 周一.",
     "11月9日是星期一,也可以说___。消防日在这天。", instr="채우세요", size=20.5, gap=10)
b.para("단어 두 개 더: 凌晨 (língchén)은 자정 이후 새벽 전의 깊은 밤, 傍晚 (bàngwǎn)은 어두워지기 직전의 짧은 시간.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 读新闻 · 뉴스 읽기", 24)
c.para("이야기에 주장(说法)이 들어가면 세 종류의 문장을 나누세요: 주장(说法), 데이터(数据), 예보(预报). 6쪽이 예예요: 「最大的一波」는 11월 11일에 대한 주장, 배수 1.5와 2.5는 보도된 데이터, 찬 공기 기온은 예보 — 예측일 뿐, 아직 사실이 아니에요.", 21.5)
c.glossline("모든 숫자마다 물어보세요: 누구의 숫자이고, 언제 측정한 건가요?")
c.ex("B2", "单选", "C", "「最大的一波」는 11월 11일 피크에 대한 주장이지, 측정한 데이터가 아니에요.",
     "「最大的一波」在第6版里是什么? A. 数据 · B. 预报 · C. 说法", size=20.5, gap=10)
c.ex("B2", "完成句子", "数据", "shùjù — 측정한 숫자, 주장이 아니에요.",
     "买东西以前,先看___,再看广告。", instr="채우세요", size=20.5, gap=10)
c.ex("B2", "单选", "B", "데이터와 결제 페이지가 먼저, 헤드라인은 나중에.",
     "读新闻时,哪个做法最好? A. 只看标题 · B. 先看数据和结算页 · C. 只看评论", size=20.5, gap=10)
c.ex("B2", "完成句子", "预报", "yùbào — 예보는 예측일 뿐, 아직 사실이 아니에요.",
     "冷空气的温度是___,还没发生。", instr="채우세요", size=20.5, gap=10)
c.para("직접 해 보세요: 1쪽 달력 상자에서 「11月11日」는 날짜 — 데이터예요. 광고의 말은 주장이에요. 구분할 수 있나요?", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「他开心的去拿包裹」", "→ 「他开心地去拿包裹。」", "地 (de)는 동작이 어떻게 이루어지는지 나타내요."),
    ("「包裹来的很快」", "→ 「包裹来得很快。」", "得 (de)는 동사 + 정도를 연결해요: 来得快."),
    ("「我拿了两个包裹个」", "→ 「我拿了两个包裹。」", "순서: 수 + 양사 + 명사."),
    ("「总决赛在星期日11月15日凌晨3点」", "→ 「总决赛在11月15日,星期日凌晨3点。」", "시간은 큰 것 → 작은 것 순: 요일이 마지막."),
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
wt = "「先看取件码,再开柜门。」(코드를 확인하고 보관함을 여세요.) 틀 先…再… 가 행동 순서를 보여줘요."
wcn = "틀: 先 … 再 … — 먼저 X, 그다음 Y."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本周句式 · 문장 틀", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「你好!我住在北京。11月9日学校做了消防演练,我学会了走楼梯。双11我买了一本书,包裹两天就到了。周日凌晨,我想看S16总决赛!」"
lcn = "编辑部示例信,不是真实来信。VOL.2曾预告本期刊登真实来信和最佳作文;截至11月2日截稿,仍未收到,本期仍刊示例,继续征集。延期不是取消。편집자 주: VOL.2는 VOL.3에 실제 편지를 약속했지만, 11월 2일까지 도착하지 않았어요. 예문이 실려 있어요. 연기된 것이지, 취소된 게 아니에요."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "读者园地 · 독자 코너", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "本周金句 · 이번 주 문장(원문 그대로, 이번 호 기사에서)", 27, "sans", True, OLIVE)
quotes = [
    ("「双11的正日子」", "더블 11 당일 자체.", "p. 1"),
    ("「先看结算页,再决定买不买」", "결제 페이지를 확인하고 결정하세요.", "p. 2"),
    ("「提高自防自救能力」", "자기 보호와 자기 구조 능력을 높이자.", "p. 3"),
    ("「三支队进了八强」", "세 팀이 8강에 올랐어요.", "p. 4"),
    ("「输了就回家」", "지면 집으로 돌아가요.", "p. 4"),
    ("「老电影,新画面」", "오래된 영화, 새로운 화면.", "p. 5"),
    ("「快递的高峰分三波」", "소포 피크는 세 파도로 와요.", "p. 6"),
    ("「着火了不坐电梯」", "불이 나면 엘리베이터를 타지 마세요.", "p. 3"),
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
p.text(MX + 28, py + 44, "下期预告 · 다음 주(VOL.4)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "S16总决赛打完了,谁是冠军?包裹都到了吗?还有你们的来信和第8版最佳作文。下周见!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-ciyu.svg")
print("P7 saved, exercises so far:", len(REG))
