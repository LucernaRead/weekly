# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zhtw-vol1/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P7 · language focus
CURPAGE[0] = 7
p = BSPage4()
p.band("語言 · Language focus", "Lucerna", "語言聚焦 · 三個級別,三個主題 · Three levels, three topics")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 天氣的話 · Weather words", 24)
a.para("Typhoon week fills the news with weather words — learn the six you will see most: 海上颱風警報 (sea warning), 陸上颱風警報 (land warning), 共伴效應 (joint effect), 外圍環流 (outer circulation), 豪雨 (torrential rain), 停班停課 (work and school suspended).", 21.5)
a.glossline("Six weather words run this week's news — learn them once, read all week.")
a.para("Warnings come in two kinds: a 海上警報 (sea warning) first, while the typhoon is still at sea; a 陸上警報 (land warning) as it nears land. Rain heavier than 大雨 is 豪雨 (torrential rain).", 21.5)
a.ex("A2", "完成句子", "海上", "A sea warning comes first, while the typhoon is still at sea.",
     "颱風還在海上,先發佈___颱風警報。", instr="Fill in", size=20.5, gap=10)
a.ex("A2", "單選", "A", "停班停課 means work and school are suspended.",
     "「停班停課」是什麼意思?", opts=["A. 不上班、不上課", "B. 提早一小時下班", "C. 換到別天上班"], size=20.5, gap=10)
a.ex("A2", "完成句子", "豪", "豪雨 (háo) is heavier than 大雨.",
     "比大雨還大的雨,叫___雨。", instr="Fill in", size=20.5, gap=10)
a.ex("A2", "單選", "A", "The typhoon's outer circulation (外圍環流) brings rain.",
     "颱風的外圍___會帶來雨。", opts=["A. 環流", "B. 警報", "C. 假期"], size=20.5, gap=10)
a.para("Practise: 「明天會停班停課嗎？」 ('Will work and school be off tomorrow?') — check your city's announcement.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 日子與節日 · Holidays", 24)
b.para("This week's days are special. Group the words and they stick: days off （連假、補假）, travel （疏運）, and festival fun （登高、討糖、星光大道）.", 21.5)
b.glossline("Group the words: days off (連假/補假), travel (疏運), festival fun (登高/討糖/星光大道).")
b.para("連假 is a run of days off in a row; when a holiday falls on a weekend and a weekday is given off instead, that extra day is a 補假； and the extra trains and buses laid on to carry everyone out and home are the 疏運.", 21.5)
b.ex("B1", "完成句子", "補假", "A make-up day off: 補假.",
     "假日逢週日,週一多放一天,叫___。", instr="Fill in", size=20.5, gap=10)
b.ex("B1", "單選", "A", "疏運 = extra transport for the holiday rush.",
     "「疏運」是連假時做什麼?", opts=["A. 加開班次載客", "B. 賣紀念票", "C. 修馬路"], size=20.5, gap=10)
b.ex("B1", "完成句子", "討糖", "討糖 is the Taiwanese way to say trick-or-treat.",
     "萬聖節,小朋友去店家___(要糖果)。", instr="Fill in", size=20.5, gap=10)
b.ex("B1", "單選", "A", "The red-carpet part of an awards night is the 星光大道.",
     "頒獎典禮走紅毯的部分叫?", opts=["A. 星光大道", "B. 人氣獎", "C. 疏運大道"], size=20.5, gap=10)
b.para("Memory trick: learn 連假 first, then the crowds it moves （疏運） and the extra day it adds （補假）.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 在地說法 · Local talk", 24)
c.para("Taiwan and Hong Kong each have their own way of saying things. In Taiwan, Threads is nicknamed 「脆」; a good post is saved with 「留友看」 — 'keep it for friends to see'; and a compliment scored in zhuyin symbols is a 「ㄅ級分」.", 21.5)
c.glossline("Three Taiwan internet coinages — all from a May 2026 PopDaily round-up of the year's memes, not this week's news.")
c.para("In Hong Kong, Halloween is 「哈囉喂」; hot pot is 「打邊爐」; cheap and tasty is 「抵食」; crabs are weighed in 「両」, and the food festival's tokens are 「品味券」.", 21.5)
c.ex("B2", "單選", "A", "In Taiwan, Threads is nicknamed 脆 (crisp).",
     "台灣人把 Threads 暱稱作什麼?", opts=["A. 脆", "B. 脆餅", "C. 推特兒"], size=20.5, gap=10)
c.ex("B2", "完成句子", "留友", "留友看 — save it so friends can read it too.",
     "看到好文,先存起來「___看」。", instr="Fill in", size=20.5, gap=10)
c.ex("B2", "單選", "A", "哈囉喂 is Hong Kong's Halloween.",
     "「哈囉喂」是香港人怎麼說哪個節日?", opts=["A. 萬聖節", "B. 聖誕節", "C. 重陽節"], size=20.5, gap=10)
c.ex("B2", "完成句子", "品味", "The festival's coupons are 品味券 (tasting tokens).",
     "美酒佳餚巡禮換飲品小食的券,叫___券。", instr="Fill in", size=20.5, gap=10)
c.para("You don't need many local sayings — learn five and every chat feels closer.", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「台風來了」", "→「颱風來了」", "Taiwan writes 颱風; 台風 is the Japanese kanji spelling."),
    ("「我買了四兩的蟹」", "→「我買了四両的蟹」", "Crabs are weighed in 両 (taels); 兩 is the everyday 'two', as in 兩隻蟹 (two crabs)."),
    ("「天氣慢慢的變涼」", "→「天氣慢慢地變涼」", "地 (de) marks how an action happens, before the verb."),
    ("「我明天放四天假去玩」", "→「我請了四天假去玩」", "請假 = ask for leave yourself; 放假 = the holiday is given to everyone."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易錯診所 · Error clinic", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「先看警報，再決定出不出門。」 — the frame 先…再… gives the order of two actions: first X, then Y. It is made for typhoon week: 先查公告，再改行程 (check the notices first, then change your plans)."
wcn = "Frame: 先…再… — first X, then Y. Make your own sentence with it."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本週句式 · Sentence frame", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「編輯好:重陽節我跟阿公去登高,他走得比我還快!晚上我們吃大閘蟹,蟹黃真的好多。下週我想去看台灣大賽。——台北小讀者(編輯範例)」"
lcn = "An editor's example letter — not a real one. VOL.2 will print real readers' letters and the best page-8 writing!"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "讀者園地 · Readers' corner", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "本週金句 · Phrases of the week — word for word from this issue's articles", 27, "sans", True, OLIVE)
quotes = [
    ("「路徑還有變數,會不會登陸,還沒有人知道」", "The track can still change; nobody knows yet if it will make landfall.", "p. 1"),
    ("「請四天假,換九天連假」", "Four days of leave, nine days off.", "p. 2"),
    ("「登高望遠,人也精神了」", "Climb high, look far — and feel refreshed.", "p. 3"),
    ("「農曆九月吃蟹乸,農曆十月吃蟹公」", "Female crabs in the 9th lunar month, males in the 10th.", "p. 3"),
    ("「先贏四場的隊伍,就是今年的總冠軍」", "The first team to four wins is this year's champion.", "p. 4"),
    ("「颱風改了日期,卻改不了大家過節的心情」", "The typhoon changed the date, not the festive mood.", "p. 5"),
    ("「三百四十多個攤位,把世界搬到海邊」", "340-plus booths move the world to the harbour.", "p. 6"),
    ("「星期五、六的晚上,今年第一次開到凌晨一時」", "Friday and Saturday nights run to 1 a.m. for the first time.", "p. 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, en, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 146
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, en + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 146 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "下期預告 · Next week (VOL.2)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "台灣大賽冠軍出爐!美酒佳餚巡禮開幕直擊,天母搞什麼鬼主活動、福隆沙雕最後一天,還有你們的來信和第 8 版最佳作文。下週見!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-lang.svg")
print("P7 saved, exercises so far:", len(REG))
