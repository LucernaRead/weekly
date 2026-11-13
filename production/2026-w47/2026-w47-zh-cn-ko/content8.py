# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-zh-cn-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · 测验与答案 =================
CURPAGE[0] = 8
p = BSPage4()
p.band("测验与答案　시험과 정답", "Lucerna", "第8版　本周大测验 + 全部答案　이번 주 큰 시험과 모든 정답")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1300, tag="P8-ex")
f.head("A　判断对错　옳은지 틀린지", 24, OLIVE, 5)
f.ex("A2", "完形单选", "A", "소설(小雪)은 11월 22일입니다.",
     "小雪在11月22日。(A. 对 · B. 错)", size=17.5, gap=0)
f.ex("A2", "完形单选", "B", "小雪는 24절기 중 20번째이지, 20번째 소설이 아니다.",
     "今年是第20个小雪节气。(A. 对 · B. 错)", size=17.5, gap=0)
f.ex("A2", "完形单选", "B", "소포 피크는 세 파도로 와요, 한 파도가 아니에요.",
     "快递高峰只有一波。(A. 对 · B. 错)", size=17.5, gap=0)
f.ex("B1", "完形单选", "A", "GEN은 결승에 올랐지만 IG는 오르지 못했다.",
     "GEN进了决赛。(A. 对 · B. 错)", size=17.5, gap=0)
f.ex("B1", "完形单选", "A", "준결승은 06:00 베이징 시간에 시작합니다.",
     "半决赛在北京时间早上6点开始。(A. 对 · B. 错)", size=17.5, gap=0)
f.ex("B1", "完形单选", "B", "《试探》은 2026년 11월 21일 개봉하는 새 영화입니다.",
     "《试探》是2019年的电影。(A. 对 · B. 错)", size=17.5, gap=0)
f.ex("B1", "完形单选", "A", "《试探》은 11월 21일 개봉합니다.",
     "《试探》11月21日上映。(A. 对 · B. 错)", size=17.5, gap=0)
f.ex("B1", "完形单选", "B", "독서의 달은 11월 1일에 시작했어요, 9일이 아니에요.",
     "深圳读书月11月9日开幕。(A. 对 · B. 错)", size=17.5, gap=0)
f.head("B　本周大测验　이번 주 큰 시험", 24, OLIVE, 5)
f.ex("A2", "单选", "B", "결승은 11월 15일 03:00 베이징 시간에 시작해요.",
     "决赛在北京时间哪天？ A. 11月14日凌晨3点 · B. 11月15日凌晨3点 · C. 11月8日早上6点", size=17.5, gap=0)
f.ex("A2", "单选", "A", "BLG는 준결승에서 T1을 3-1로 이겼다.",
     "半决赛，BLG打赢了哪个队？ A. T1 · B. DK · C. IG", size=17.5, gap=0)
f.ex("B1", "单选", "B", "IG는 8강전에서 TES를 3-1로 이겼다.",
     "四分之一决赛，IG打赢了哪个队？ A. GEN · B. TES · C. LYON", size=17.5, gap=0)
f.ex("B1", "单选", "B", "22일 합계는 139억 3800만 개입니다.",
     "22天快递总数是多少？ A. 7.77亿件 · B. 139.38亿件 · C. 6.34亿件", size=17.5, gap=0)
f.ex("B1", "单选", "B", "하루 최다는 7억 7700만 개였다.",
     "单日最高是多少？ A. 139.38亿件 · B. 7.77亿件 · C. 6.34亿件", size=17.5, gap=0)
f.ex("B1", "单选", "A", "《试探》 주연은 Feng Shaofeng.",
     "《试探》的主演是谁？ A. 冯绍峰 · B. 刘德华 · C. 朱塞佩·托纳托雷", size=17.5, gap=0)
f.ex("B1", "单选", "B", "문화의 밤은 11월 14일.",
     "文化馆之夜在哪天？ A. 11月7日 · B. 11月14日 · C. 11月1日", size=17.5, gap=0)
f.ex("B1", "单选", "A", "小雪는 24절기 중 20번째입니다.",
     "小雪是第几个节气？ A. 第20个 · B. 第24个 · C. 第2个", size=17.5, gap=0)
f.ex("B1", "单选", "A", "첫 번째 기후는 虹藏不见입니다.",
     "小雪三候的第一候是什么？ A. 虹藏不见 · B. 天气上升 · C. 闭塞而成冬", size=17.5, gap=0)
f.ex("B1", "单选", "A", "결승은 BLG 대 GEN입니다.",
     "决赛的两个队是？ A. BLG和GEN · B. IG和T1 · C. TES和DK", size=17.5, gap=0)
f.head("C　完成句子　문장 완성", 24, OLIVE, 5)
f.ex("A2", "完成句子", "小雪", "소설(小雪)은 11월 22일입니다.",
     "11月22日是___。", instr="채우세요", size=17.5, gap=0)
f.ex("A2", "完成句子", "15", "S16 결승은 11월 15일, 베이징 시간.",
     "决赛在11月___日凌晨3点。", instr="채우세요", size=17.5, gap=0)
f.ex("B1", "完成句子", "T1", "BLG는 준결승에서 T1을 3-1로 이겼다.",
     "半决赛，BLG 3比1打赢了___。", instr="채우세요", size=17.5, gap=0)
f.ex("A2", "完成句子", "139.38", "22일 합계는 139.38억 개입니다.",
     "22天快递总数是___亿件。", instr="채우세요", size=17.5, gap=0)
f.ex("B1", "完成句子", "21", "《试探》은 11월 21일 개봉합니다.",
     "《试探》11月___日上映。", instr="채우세요", size=17.5, gap=0)
f.ex("B1", "完成句子", "20", "小雪는 24절기 중 20번째입니다.",
     "小雪是第___个节气。", instr="채우세요", size=17.5, gap=0)
f.ex("B2", "完成句子", "7.77", "하루 최다는 7.77억 개였다.",
     "单日最高是___亿件。", instr="채우세요", size=17.5, gap=0)
f.ex("A2", "完成句子", "14", "문화의 밤은 11월 14일.",
     "文化馆之夜在11月___日。", instr="채우세요", size=17.5, gap=0)
f.ex("B1", "完成句子", "GEN", "결승은 BLG 대 GEN입니다.",
     "决赛是BLG对___。", instr="채우세요", size=17.5, gap=0)
f.ex("B1", "完成句子", "冷", "소설이 지나면 날씨가 더 추워진다.",
     "小雪之后，天气会更___。", instr="채우세요", size=17.5, gap=0)
f.head("D　读一读，答一答　읽고 답하기", 24, OLIVE, 5)
f.para("小林住在深圳。11月8日星期日早上6点，小林看了半决赛，GEN 3比0打赢了IG。11月11日星期三，小林在网上买的书到了，他用取件码打开快递柜，拿到了包裹。11月14日星期六晚上，小林和妈妈一起去文化馆，亲手摸了摸古籍。11月15日星期日凌晨3点，他想早起看S16总决赛，BLG对GEN。", 19.5, lh=1.3, split=False)
f.ex("A2", "单选", "A", "샤오린은 선전에 살아요.",
     "小林住在哪里？ A. 深圳 · B. 北京 · C. 广州", size=17.5, gap=0)
f.ex("A2", "单选", "A", "11월 8일에 그는 준결승을 봤다.",
     "11月8日，小林看了什么？ A. 半决赛 · B. 期中考试 · C. 运动会", size=17.5, gap=0)
f.ex("B1", "单选", "B", "그는 온라인으로 책을 샀어요.",
     "他买了什么？ A. 毛衣 · B. 书 · C. 帽子", size=17.5, gap=0)
f.ex("B1", "单选", "B", "그는 어머니와 문화센터에 갔어요.",
     "他和谁一起去文化馆？ A. 爸爸 · B. 妈妈 · C. 老师", size=17.5, gap=0)
f.ex("B2", "单选", "A", "순서: 준결승, 다음 소포, 다음 문화관.",
     "这段话的顺序是什么？ A. 先看半决赛，再拿包裹，再去文化馆 · B. 先去文化馆，再看半决赛 · C. 先拿包裹，再看半决赛", size=17.5, gap=0)
f.ex("B1", "完成句子", "深圳", "샤오린은 선전에 살아요.",
     "小林住在___。", instr="채우세요", size=17.5, gap=0)
f.head("E　情景说话　대화에서", 24, OLIVE, 5)
f.ex("B1", "完形单选", "A", "코드를 확인하고 보관함을 여세요.",
     "— 包裹到了，怎么办？ — 先看___，再开柜门。(A. 取件码 · B. 电影票)", size=17.5, gap=0)
f.ex("B1", "完形单选", "A", "소설이 지나면 옷을 더 입고 감기에 걸리지 마세요.",
     "— 小雪之后，怎么办？ — 多穿一件，别___。(A. 着凉 · B. 熬夜)", size=17.5, gap=0)
f.ex("B2", "完形单选", "A", "6쪽 규칙: 데이터가 먼저, 광고는 나중에.",
     "— 这条新闻说单日最高7.77亿件，可信吗？ — 先看___，再看广告。(A. 数据 · B. 评论)", size=17.5, gap=0)
f.head("F　写一写　작문", 24, OLIVE, 5)
MODELO = ("这一周是小雪那一周。星期日凌晨3点，我想早起看S16总决赛，BLG对GEN。"
          "星期一，我的包裹到了，我用取件码打开快递柜，拿到了书。"
          "星期六，我和妈妈一起去看电影《试探》，故事很有意思。"
          "星期日是小雪，天气更冷了，我加了一件厚外套。这一周，又忙又开心，天冷了，我要多穿衣服，不着凉。")
NCHARS = len(MODELO.replace(" ", ""))
f.glossline(f"작문에는 단 하나의 정답이 없습니다. {NCHARS}자 모범 답안이 이어집니다.")
f.ex("B1", "写作", "(开放题，范文如下)", f"자유 과제 — 모범 답안은 위 F 부분에 있습니다({NCHARS}자)",
     "写一写《小雪那一周》：S16决赛、包裹、小雪，这一周你做了什么？写 120~180 字。", instr="쓰기", size=17.5, gap=0)
f.para("모델 답안: " + MODELO, 18.5, lh=1.3, split=False)
f.end_report()
print("P8 test flow ends col/y:", f.ci, round(f.y, 1))
# ---- P8 image (writing) in the free space at the bottom of col 3 ----
iy8 = f.y + 24
image(p, "writing.jpg", COLX[3], iy8, CW, 210)
cy8 = caption(p, COLX[3], iy8 + 210, CW, "写一写：先想一想，再下笔。（资料图）",
              "사진: Tookapic — CC0 (Wikimedia Commons)")
print("P8 image ends", round(cy8, 1))

# ================= keys =================
p.hline(MX, RIGHT, 1320, OLIVE, 2)
p.text(MX, 1358, "答案　정답 — 쪽별, 모든 답에 설명 포함", 25, "sans", True, OLIVE)
p.text(RIGHT, 1358, "모든 설명은 한국어로　✓ = 작문 과제", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1384, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— {pg}쪽 —", 13.3, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "写作":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.3, lh=1.16, gap=0, split=False)
af.end_report()
print("P8 keys flow ends col/y:", af.ci, round(af.y, 1))
p.foot(8)
p.save(f"{OUT}/p8-ceyan.svg")
print("P8 saved, exercises total:", len(REG))
from collections import Counter
print("levels:", Counter(e_["level"] for e_ in REG))
print("writing model chars:", NCHARS)
