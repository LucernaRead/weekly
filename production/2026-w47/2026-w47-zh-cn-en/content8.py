# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-zh-cn-en/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · 测验与答案 =================
CURPAGE[0] = 8
p = BSPage4()
p.band("测验与答案　Test & keys", "Lucerna", "第8版　本周大测验 + 全部答案　This week's test and every answer key")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1300, tag="P8-ex")
f.head("A　判断对错　True or false", 24, OLIVE, 5)
f.ex("A2", "完形单选", "A", "Minor Snow (小雪) is on Nov 22.",
     "小雪在11月22日。(A. 对 · B. 错)", size=17.5, gap=0)
f.ex("A2", "完形单选", "B", "小雪 is the 20th solar term, not the 20th Minor Snow.",
     "今年是第20个小雪节气。(A. 对 · B. 错)", size=17.5, gap=0)
f.ex("A2", "完形单选", "B", "The parcel peak comes in three waves, not one.",
     "快递高峰只有一波。(A. 对 · B. 错)", size=17.5, gap=0)
f.ex("B1", "完形单选", "A", "GEN reached the final; IG did not.",
     "GEN进了决赛。(A. 对 · B. 错)", size=17.5, gap=0)
f.ex("B1", "完形单选", "A", "Semi-finals start at 06:00 Beijing time.",
     "半决赛在北京时间早上6点开始。(A. 对 · B. 错)", size=17.5, gap=0)
f.ex("B1", "完形单选", "B", "《试探》 opens on Nov 21, 2026; it is a new film.",
     "《试探》是2019年的电影。(A. 对 · B. 错)", size=17.5, gap=0)
f.ex("B1", "完形单选", "A", "《试探》 opens on Nov 21.",
     "《试探》11月21日上映。(A. 对 · B. 错)", size=17.5, gap=0)
f.ex("B1", "完形单选", "B", "Reading Month began on Nov 1, not Nov 9.",
     "深圳读书月11月9日开幕。(A. 对 · B. 错)", size=17.5, gap=0)
f.head("B　本周大测验　The big quiz", 24, OLIVE, 5)
f.ex("A2", "单选", "B", "The final starts at 03:00 Beijing time on Nov 15.",
     "决赛在北京时间哪天？ A. 11月14日凌晨3点 · B. 11月15日凌晨3点 · C. 11月8日早上6点", size=17.5, gap=0)
f.ex("A2", "单选", "A", "BLG beat T1 3–1 in the semi-final.",
     "半决赛，BLG打赢了哪个队？ A. T1 · B. DK · C. IG", size=17.5, gap=0)
f.ex("B1", "单选", "B", "IG beat TES 3–1 in the quarter-final.",
     "四分之一决赛，IG打赢了哪个队？ A. GEN · B. TES · C. LYON", size=17.5, gap=0)
f.ex("B1", "单选", "B", "The 22-day total is 139.38 billion items.",
     "22天快递总数是多少？ A. 7.77亿件 · B. 139.38亿件 · C. 6.34亿件", size=17.5, gap=0)
f.ex("B1", "单选", "B", "The highest single day was 777 million items.",
     "单日最高是多少？ A. 139.38亿件 · B. 7.77亿件 · C. 6.34亿件", size=17.5, gap=0)
f.ex("B1", "单选", "A", "《试探》 stars Feng Shaofeng.",
     "《试探》的主演是谁？ A. 冯绍峰 · B. 刘德华 · C. 朱塞佩·托纳托雷", size=17.5, gap=0)
f.ex("B1", "单选", "B", "The culture night is on Nov 14.",
     "文化馆之夜在哪天？ A. 11月7日 · B. 11月14日 · C. 11月1日", size=17.5, gap=0)
f.ex("B1", "单选", "A", "小雪 is the 20th solar term.",
     "小雪是第几个节气？ A. 第20个 · B. 第24个 · C. 第2个", size=17.5, gap=0)
f.ex("B1", "单选", "A", "The first phase is 虹藏不见.",
     "小雪三候的第一候是什么？ A. 虹藏不见 · B. 天气上升 · C. 闭塞而成冬", size=17.5, gap=0)
f.ex("B1", "单选", "A", "The final is BLG vs GEN.",
     "决赛的两个队是？ A. BLG和GEN · B. IG和T1 · C. TES和DK", size=17.5, gap=0)
f.head("C　完成句子　Complete", 24, OLIVE, 5)
f.ex("A2", "完成句子", "小雪", "Minor Snow (小雪) is on Nov 22.",
     "11月22日是___。", instr="Fill in", size=17.5, gap=0)
f.ex("A2", "完成句子", "15", "The S16 final is on Nov 15, Beijing time.",
     "决赛在11月___日凌晨3点。", instr="Fill in", size=17.5, gap=0)
f.ex("B1", "完成句子", "T1", "BLG beat T1 3–1 in the semi-final.",
     "半决赛，BLG 3比1打赢了___。", instr="Fill in", size=17.5, gap=0)
f.ex("A2", "完成句子", "139.38", "The 22-day total is 139.38亿件.",
     "22天快递总数是___亿件。", instr="Fill in", size=17.5, gap=0)
f.ex("B1", "完成句子", "21", "《试探》 opens on Nov 21.",
     "《试探》11月___日上映。", instr="Fill in", size=17.5, gap=0)
f.ex("B1", "完成句子", "20", "小雪 is the 20th solar term.",
     "小雪是第___个节气。", instr="Fill in", size=17.5, gap=0)
f.ex("B2", "完成句子", "7.77", "The highest single day was 7.77亿件.",
     "单日最高是___亿件。", instr="Fill in", size=17.5, gap=0)
f.ex("A2", "完成句子", "14", "The culture night is on Nov 14.",
     "文化馆之夜在11月___日。", instr="Fill in", size=17.5, gap=0)
f.ex("B1", "完成句子", "GEN", "The final is BLG vs GEN.",
     "决赛是BLG对___。", instr="Fill in", size=17.5, gap=0)
f.ex("B1", "完成句子", "冷", "After Minor Snow, the weather gets colder.",
     "小雪之后，天气会更___。", instr="Fill in", size=17.5, gap=0)
f.head("D　读一读，答一答　Read & answer", 24, OLIVE, 5)
f.para("小林住在深圳。11月8日星期日早上6点，小林看了半决赛，GEN 3比0打赢了IG。11月11日星期三，小林在网上买的书到了，他用取件码打开快递柜，拿到了包裹。11月14日星期六晚上，小林和妈妈一起去文化馆，亲手摸了摸古籍。11月15日星期日凌晨3点，他想早起看S16总决赛，BLG对GEN。", 19.5, lh=1.3, split=False)
f.ex("A2", "单选", "A", "Xiao Lin lives in Shenzhen.",
     "小林住在哪里？ A. 深圳 · B. 北京 · C. 广州", size=17.5, gap=0)
f.ex("A2", "单选", "A", "On Nov 8 he watched the semi-final.",
     "11月8日，小林看了什么？ A. 半决赛 · B. 期中考试 · C. 运动会", size=17.5, gap=0)
f.ex("B1", "单选", "B", "He bought a book online.",
     "他买了什么？ A. 毛衣 · B. 书 · C. 帽子", size=17.5, gap=0)
f.ex("B1", "单选", "B", "He went to the culture centre with his mother.",
     "他和谁一起去文化馆？ A. 爸爸 · B. 妈妈 · C. 老师", size=17.5, gap=0)
f.ex("B2", "单选", "A", "Order: semi-final, then parcel, then culture centre.",
     "这段话的顺序是什么？ A. 先看半决赛，再拿包裹，再去文化馆 · B. 先去文化馆，再看半决赛 · C. 先拿包裹，再看半决赛", size=17.5, gap=0)
f.ex("B1", "完成句子", "深圳", "Xiao Lin lives in Shenzhen.",
     "小林住在___。", instr="Fill in", size=17.5, gap=0)
f.head("E　情景说话　In conversation", 24, OLIVE, 5)
f.ex("B1", "完形单选", "A", "Check the pick-up code, then open the locker.",
     "— 包裹到了，怎么办？ — 先看___，再开柜门。(A. 取件码 · B. 电影票)", size=17.5, gap=0)
f.ex("B1", "完形单选", "A", "After Minor Snow, wear more and do not catch a chill.",
     "— 小雪之后，怎么办？ — 多穿一件，别___。(A. 着凉 · B. 熬夜)", size=17.5, gap=0)
f.ex("B2", "完形单选", "A", "Page 6's rule: data first, advertisement last.",
     "— 这条新闻说单日最高7.77亿件，可信吗？ — 先看___，再看广告。(A. 数据 · B. 评论)", size=17.5, gap=0)
f.head("F　写一写　Writing", 24, OLIVE, 5)
MODELO = ("这一周是小雪那一周。星期日凌晨3点，我想早起看S16总决赛，BLG对GEN。"
          "星期一，我的包裹到了，我用取件码打开快递柜，拿到了书。"
          "星期六，我和妈妈一起去看电影《试探》，故事很有意思。"
          "星期日是小雪，天气更冷了，我加了一件厚外套。这一周，又忙又开心，天冷了，我要多穿衣服，不着凉。")
NCHARS = len(MODELO.replace(" ", ""))
f.glossline(f"Writing — there is no single right answer. A {NCHARS}-character model follows.")
f.ex("B1", "写作", "(开放题，范文如下)", f"Open task - the model answer is printed in section F above ({NCHARS} characters)",
     "写一写《小雪那一周》：S16决赛、包裹、小雪，这一周你做了什么？写 120~180 字。", instr="Writing", size=17.5, gap=0)
f.para("Model answer: " + MODELO, 18.5, lh=1.3, split=False)
f.end_report()
print("P8 test flow ends col/y:", f.ci, round(f.y, 1))
# ---- P8 image (writing) in the free space at the bottom of col 3 ----
iy8 = f.y + 24
image(p, "writing.jpg", COLX[3], iy8, CW, 210)
cy8 = caption(p, COLX[3], iy8 + 210, CW, "写一写：先想一想，再下笔。（资料图）",
              "Photo: Tookapic — CC0 (Wikimedia Commons)")
print("P8 image ends", round(cy8, 1))

# ================= keys =================
p.hline(MX, RIGHT, 1320, OLIVE, 2)
p.text(MX, 1358, "答案　Answer keys — by page, with a note on every answer", 25, "sans", True, OLIVE)
p.text(RIGHT, 1358, "All notes in English　✓ = the writing task", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1384, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— Page {pg} —", 13.3, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
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
