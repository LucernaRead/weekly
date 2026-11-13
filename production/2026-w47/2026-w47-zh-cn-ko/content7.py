# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-zh-cn-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 词语精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("词语　언어 포인트", "Lucerna", "语言聚焦　三个级别，三个主题　세 수준, 세 주제")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　决赛与包裹　결승과 소포", 24)
a.para("이번 주 단어: 决赛 (juésài, 결승), 冠军 (guànjūn, 우승자), 半决赛 (bànjuésài, 준결승), 到货 (dàohuò, 도착했다), 退换货 (tuìhuànhuò, 반품과 교환), 价保 (jiàbǎo, 가격 보호).", 21.5)
a.glossline("양사는 여전히 중요해요: 一个包裹 (소포 하나), 一部电影 (영화 한 편), 一场演练 (훈련 한 번).")
a.ex("A2", "完成句子", "个", "包裹 는 양사 个 gè 를 써요.",
     "我拿了___包裹。", instr="채우세요", size=20, gap=10)
a.ex("A2", "单选", "A", "决赛는 결승, 마지막 경기라는 뜻입니다.",
     "「决赛」是什么意思？ A. 最后一场比赛 · B. 第一场比赛 · C. 练习赛", size=20, gap=10)
a.ex("A2", "完成句子", "决赛", "juésài — 결승. 11월 15일 BLG 대 GEN.",
     "11月15日凌晨3点，BLG和GEN打___。", instr="채우세요", size=20, gap=10)
a.ex("A2", "单选", "A", "소포는 个 를 써요 — 只 나 条 가 아니에요.",
     "哪个说法对？ A. 一个包裹 · B. 一只包裹 · C. 一条包裹", size=20, gap=10)
a.para("하나 더 연습해 보세요. 「我的包裹到了吗？」(내 소포가 도착했나요?) 소포를 기다릴 때는 먼저 물어보고, 그다음 무인 택배함으로 가세요.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　时间与日期　시간과 날짜", 24)
b.para("중국어는 시간을 큰 것부터 작은 순으로 씁니다. 년, 월, 일, 요일, 때, 시간입니다. 이번 호의 예: 「11月15日星期日凌晨3点」(11월 15일 일요일 새벽 3시), 「11月22日星期日」(11월 22일 일요일), 「11月21日星期六」(11월 21일 토요일). 가장 큰 단위가 먼저, 순서가 어긋나지 않아요.", 21.5)
b.glossline("영어 «Sunday, Nov 22»는 11月22日星期日가 된다.")
b.ex("B1", "单选", "B", "凌晨 língchén — 자정 이후의 깊은 밤.",
     "「凌晨3点」是什么时候？ A. 下午3点 · B. 半夜3点 · C. 中午12点", size=20, gap=10)
b.ex("B1", "完成句子", "早上", "06:00은 早上 (아침)이에요 — 저녁이 아니에요.",
     "半决赛在北京时间11月8日___6点开始。（不是晚上）", instr="채우세요", size=20, gap=10)
b.ex("B1", "单选", "A", "큰 것부터 작은 순: 11월 22일 일요일.",
     "哪个顺序对？ A. 11月22日星期日 · B. 星期日11月22日 · C. 星期日小雪11月22日", size=20, gap=10)
b.ex("B1", "完成句子", "周日", "11월 22일은 일요일 — 周日.",
     "11月22日是星期日，也可以说___。小雪在这天。", instr="채우세요", size=20, gap=10)
b.para("단어 두 개 더: 凌晨 (língchén)은 자정 이후 새벽 전의 깊은 밤, 傍晚 (bàngwǎn)은 어두워지기 직전의 짧은 시간.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　读新闻　뉴스 읽기", 24)
c.para("이야기에 주장(说法)이 들어가면 세 종류의 문장을 나누세요. 주장(说法), 데이터(数据), 예보(预报)입니다. 6쪽이 예예요. 「没有爆掉」는 올해 소포에 대한 주장, 139.38억 개 합계는 보도된 데이터 — 이미 세어진 것, 추측이 아닙니다. 「第三波是最高峰」는 中通云仓의 예보 — 예상일 뿐, 아직 세지 않았습니다.", 21.5)
c.glossline("모든 숫자마다 물어보세요: 누구의 숫자이고, 언제 측정한 건가요?")
c.ex("B2", "单选", "A", "「139.38亿件」는 우정국의 최종 집계로, 이미 세어진 수입니다.",
     "「139.38亿件」在第6版里是什么？ A. 已经数完的事实 · B. 邮政局的预计 · C. 广告词", size=20, gap=10)
c.ex("B2", "完成句子", "数据", "shùjù — 측정한 숫자, 주장이 아니에요.",
     "买东西以前，先看___，再看广告。", instr="채우세요", size=20, gap=10)
c.ex("B2", "单选", "B", "데이터와 결제 페이지가 먼저, 헤드라인은 나중에.",
     "读新闻时，哪个做法最好？ A. 只看标题 · B. 先看数据和结算页 · C. 只看评论", size=20, gap=10)
c.ex("B2", "完成句子", "预报", "yùbào — 예보는 예측일 뿐, 아직 사실이 아니에요.",
     "「第三波是最高峰」是___，还没发生。", instr="채우세요", size=20, gap=10)
c.para("직접 해 보세요. 1쪽 달력 상자에서 「11月22日」는 날짜 — 데이터예요. 광고의 말은 주장이에요. 구분할 수 있나요?", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters + image ----
bx = COLX[3]
errs = [
    ("「他开心的去拿包裹」", "→ 「他开心地去拿包裹。」", "地 (de)는 동작이 어떻게 이루어지는지 나타내요."),
    ("「包裹来的很快」", "→ 「包裹来得很快。」", "得 (de)는 동사 + 정도를 연결해요: 来得快."),
    ("「我拿了两个包裹个」", "→ 「我拿了两个包裹。」", "순서: 수 + 양사 + 명사."),
    ("「总决赛在星期日11月15日凌晨3点」", "→ 「总决赛在11月15日，星期日凌晨3点。」", "시간은 큰 것 → 작은 것 순: 요일이 마지막."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易错诊所　오류 클리닉", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「先看预报，再决定穿什么。」先…再… 틀은 행동의 순서를 나타낸다."
wcn = "틀: 先 … 再 … — 먼저 X, 그다음 Y."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill=BOX)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本周句式　문장 틀", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「你好！我住在上海。11月9日半决赛，我看了BLG打T1，3比1，真好看！双11我买了一件外套，包裹两天就到了。你们呢？」"
lcn = "编辑部示例信，不是真实来信。VOL.3曾预告本期刊登真实来信和最佳作文；截至11月10日截稿，仍未收到，继续征集。延期不是取消。편집부 알림: VOL.3은 VOL.4에 진짜 편지를 싣겠다고 약속했지만 11월 10일까지 도착한 것이 없습니다. 연기일 뿐, 취소가 아닙니다."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "读者园地　독자 마당", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- P7 image (brush) below the letters box ----
iy7 = col3_end + 12
image(p, "brush.jpg", bx, iy7, CW, 130)
cy7 = caption(p, bx, iy7 + 130, CW, "毛笔（资料图）。写中文，先从一笔一画开始。",
              "사진: Mx. Granger — CC0 (Wikimedia Commons)")
img_end = cy7
print("P7 image ends", img_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, img_end + 44)
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "本周金句　이번 주 문장 (이번 호 기사에서 그대로)", 27, "sans", True, OLIVE)
quotes = [
    ("「决赛对阵GEN」", "결승: BLG 대 GEN.", "p. 1"),
    ("「包裹都到了吗」", "소포가 모두 도착했나요?", "p. 2"),
    ("「小雪气寒而将雪矣」", "소설: 공기가 차가워지고 눈이 온다.", "p. 3"),
    ("「两支中国队进了四强」", "중국 팀 두 팀이 준결승에 올랐다.", "p. 4"),
    ("「先看简介，再决定」", "먼저 줄거리를 읽고 나서 결정하세요.", "p. 5"),
    ("「无高峰，全高峰」", "하나의 피크가 아니다 — 매일 피크다.", "p. 6"),
    ("「先打开看一看，再确认收货」", "먼저 열고 확인한 뒤 수령을 확인하세요.", "p. 6"),
    ("「悦读深圳」", "선전에서 즐겁게 읽기 — 선전 독서의 달 주제.", "p. 3"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, en, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 120
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, en + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 120 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "下期预告　다음 주 (VOL.5)", 24, "sans", True, GOOSE)
p.para(MX + 28, py + 84, "S16总决赛打完了，谁是冠军？小雪之后，冬天怎么过？还有你们的来信和第8版最佳作文。下周见！", 21, "serif", False, ONCLOTH, RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-ciyu.svg")
print("P7 saved, exercises so far:", len(REG))
