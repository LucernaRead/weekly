# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-en-zh-tw/svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("EXERCISES & ANSWERS · 練習與答案", "The Lucerna", "FINAL TEST · 綜合評估 · Answers at the bottom of this page 答案在本版下方")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1485, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "C", "10 月 31 日是萬聖節"),
    ("A2", "A", "carve 雕刻南瓜燈"),
    ("B1", "B", "neither...nor 既不…也不…"),
    ("A2", "A", "costume 萬聖節裝扮"),
    ("A2", "B", "she 三單 → wears"),
    ("A2", "B", "trick or treat 換來糖果"),
    ("B1", "A", "will + 動詞原形 fall"),
    ("B1", "C", "be going to → is going"),
]
cnums = [reg_ex(lv, "完形填空", k, nt) for lv, k, nt in cloze_defs]
bf.head("A · CLOZE · 完形填空", 24)
bf.para(f"Maya is twelve. On Saturday, October 31, it is ({cnums[0]})___. In the morning, she helps her father ({cnums[1]})___ a pumpkin on the porch. « ({cnums[2]})___ rain nor cold can stop us », laughs her mother. In the evening, Maya puts on her ({cnums[3]})___ : she ({cnums[4]})___ a gold crown, like a Greek goddess. She takes her bag and goes from house to house : « Trick or treat ! » The neighbours give her ({cnums[5]})___. At nine o'clock, the street is quiet — and in the night, the clocks will ({cnums[6]})___ back : one more hour of sleep ! Tomorrow, Maya is ({cnums[7]})___ to sleep late, very late.", 21.5)
bf.expl("選項：")
for n, opts in zip(cnums, [
    "A. Christmas · B. Easter · C. Halloween",
    "A. carve · B. eat · C. sell",
    "A. Both · B. Neither · C. Also",
    "A. costume · B. uniform · C. pyjamas",
    "A. wear · B. wears · C. wearing",
    "A. money · B. candy · C. flowers",
    "A. fall · B. falls · C. falling",
    "A. goes · B. go · C. going",
]):
    bf.para(f"{n}. {opts}", 19.5, "sans", False, INK, 1.32, 2)

# ---- B. single choice ----
bf.head("B · MULTIPLE CHOICE · 單選", 24)
mcq = [
    ("A2", "B", "9:15 = a quarter past nine", "The game starts at 9:15. In words : ... A. a quarter to nine · B. a quarter past nine · C. half past nine"),
    ("A2", "A", "we → get 原形", "On Sunday, we ___ an extra hour of sleep. A. get · B. gets · C. getting"),
    ("B1", "B", "已結束的比賽用 won", "The 76ers ___ the game 106–100. A. win · B. won · C. wins"),
    ("B1", "B", "than → 比較級 hotter", "Austin is ___ than Milwaukee in October. A. hot · B. hotter · C. hottest"),
    ("B2", "A", "despite + 名詞：儘管下雨", "___ the rain, the parade went on all evening. A. Despite · B. Because · C. Unless"),
    ("B2", "A", "whether = 是否", "Nobody knows ___ the Brewers will win the Series. A. whether · B. what · C. who"),
    ("A2", "A", "過去的事用過去式 opened", "Early voting in Texas ___ on Monday. A. opened · B. open · C. opens"),
    ("B1", "A", "be going to + 原形 cast", "She is going to ___ her ballot on Saturday. A. cast · B. casts · C. casted"),
]
for lv, k, nt, body in mcq:
    bf.ex(lv, "單選", k, nt, body, size=20.5)

# ---- C. reading ----
bf.head("C · READING · 閱讀理解", 24)
bf.para("On Monday morning, Rosa Delgado, a nurse from Houston, finished her night work at six o'clock. She did not go home to sleep. She drove to the early-voting place near the hospital and joined a short line. « On November 3, I work all day », she explains. « Today, I have time. » Ten minutes later, her ballot was in the box, and a sticker on her jacket said : I VOTED EARLY. By Friday, October 30, when early voting ends in Texas, millions of Texans will do the same.", 21.5)
read_qs = [
    ("A2", "B", "原文：a nurse from Houston", "Rosa is... A. a teacher · B. a nurse · C. a driver"),
    ("A2", "B", "11 月 3 日她全天上班", "She voted early because on November 3 she... A. travels · B. works all day · C. sleeps"),
    ("B1", "A", "貼紙上寫著 I VOTED EARLY", "Her sticker said... A. I VOTED EARLY · B. VOTE ON TUESDAY · C. TEXAS FIRST"),
    ("B1", "B", "德州提前投票 10 月 30 日結束", "Early voting in Texas ends on... A. October 19 · B. October 30 · C. November 3"),
]
for lv, k, nt, body in read_qs:
    bf.ex(lv, "閱讀理解", k, nt, body, size=20.5)

# ---- D. sentence building ----
bf.head("D · SENTENCES · 完成句子與轉換", 24)
d_items = [
    ("A2", "On Saturday, they are going to carve a pumpkin.", "are going to + 原形",
     "Be going to : « On Saturday, they (carve) a pumpkin. » → ___"),
    ("B1", "The Knicks raised their first banner since 1973.", "raise → raised（規則變化）",
     "Past simple : « The Knicks (raise) their first banner since 1973. »"),
    ("B1", "scarier", "scary → scarier（y 變 i 再加 er）",
     "Comparative : « My costume is ___ (scary) than yours. »"),
    ("B2", "Whether", "whether 引導「是否」子句",
     "Whether : « ___ the parade will happen, nobody knows. »"),
]
for lv, k, nt, body in d_items:
    bf.ex(lv, "完成句子", k, nt, body, size=20.5)

# ---- E. translation ----
bf.head("E · TRANSLATION · 翻譯", 24)
e_items = [
    ("B2", "投票不再是一天的事情，而是一個季節。", "no longer 不再",
     "Translate : « Voting is no longer a day ; it is a season. »"),
    ("A2", "The 76ers won the game 106–100.", "win → won；比數 106–100",
     "翻譯：76 人隊以 106 比 100 贏得了比賽。"),
    ("B1", "This year, early voting opened on Monday.", "open → opened；on Monday",
     "翻譯：今年的提前投票在星期一開始。"),
    ("B1", "兩家俱樂部都從未贏過世界大賽。", "neither 否定「兩家都不」；has ever won 現在完成時",
     "Translate : « Neither club has ever won the Series. »"),
]
for lv, k, nt, body in e_items:
    bf.ex(lv, "翻譯", k, nt, body, size=20.5)

# ---- F. matching ----
bf.head("F · WORDS · 詞彙配對", 24)
bf.match_set("B1", "詞彙配對",
             ["a midterm", "an incumbent", "a margin", "turnout"],
             ["the number of people who vote", "an election in the middle of a president's term",
              "the person who holds the job now", "the difference between two results"],
             ["b", "c", "d", "a"],
             ["midterm = 中期選舉 b", "incumbent = 現任者 c", "margin = 差距 d", "turnout = 投票率 a"],
             instr="配對")

# ---- G. dialogue (register first) ----
dlg_defs = [
    ("A2", "ID", "投票時出示證件 ID"),
    ("A2", "line", "line = 排隊（美式英語）"),
    ("A2", "ballot", "ballot = 選票"),
    ("A2", "sticker", "sticker = 貼紙"),
    ("B1", "November", "選舉日是 11 月 3 日"),
]
gnums = [reg_ex(lv, "對話補全", k, nt) for lv, k, nt in dlg_defs]
bf.head("G · DIALOGUE · 對話補全", 24)
bf.para(f"— Good morning ! Is this the early-voting place ? — Yes, welcome. May I see your ({gnums[0]})___ ? — Here it is. Is the ({gnums[1]})___ long today ? — No, five minutes only. Yesterday it was very long ! — Good. It is my first early vote. What do I do with the ({gnums[2]})___ ? — Mark your choices, check them twice, then put it in the box. — Thank you. And the famous ({gnums[3]})___ ? Everybody has one on their jacket. — The sticker ! Here it is : « I VOTED ». Wear it with pride. — I will ! See you on ({gnums[4]})___ 3rd, in the results ! — Ha ! Have a good day.", 21.5)
bf.end_report()

# ---- writing strip ----
wy = 1500
p.hline(MX, RIGHT, wy - 14, GOLD, 2)
reg_ex("B1", "寫作", "開放題 — 要點見寫作框，範本在第 8 版寫作框內", "按要點給分")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H · WRITING · 寫作", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Write a short text (80 to 100 words) : « My Saturday, October 31 ». Tell us : your costume, your street, the candy, the pumpkins — and one sentence about the clocks that fall back in the night. The best texts will appear in VOL.2 (page 7, « Readers' Corner »).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 190, "用英語寫 80–100 詞：我的 10 月 31 日星期六。寫清裝扮、街道、糖果、南瓜，再寫一句夜裡撥回的時鐘。", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 276, fill=BOX, stroke=LINE, sw=1.4)
p.text(mx2 + 22, wy + 38, "MODEL · 範文", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "On Saturday, October 31, our street becomes a small Halloween town. In the morning, I carve a pumpkin with my father and we put a candle inside. At six o'clock, I wear my pirate costume and take my bag. House after house, I say « Trick or treat ! » and the neighbours smile and give me candy. My bag is heavy at nine o'clock ! In the night, the clocks fall back, so I sleep one hour more on Sunday. It is my favourite weekend of the autumn.", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 312
p.hline(MX, RIGHT, ky - 12, GOLD, 2)
p.text(MX, ky + 26, "ANSWERS · 全部答案與簡析（第 1–8 版）", 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2545, tag="P8-keys")
# Printed-note set: the core prints 62 notes under its length rule
# (len(note) <= 10, calibrated for its compact notes). This edition forces
# exactly the core's printed set, listed explicitly (derived from the
# shipped core P8 with tools/p8.py extract and cross-checked by simulating
# the core rule on the core registry: identical 62 numbers), and prints in
# the EN family's fan-out form " (note)" (half-width parens, leading space),
# as in the shipped EN x ES build's content8.py.
PRINT_NOTES = {11, 14, 15, 19, 35, 36, 40, 42, 49, 65, 74, 82, 83, 84, 85,
               86, 87, 89, 101, 106, 108, 109, 110, 111, 112, 113, 114, 115,
               116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127,
               128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139,
               140, 141, 142, 143, 144, 145, 146, 147, 148, 149}
from itertools import groupby
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— 第 {pg} 版 —", 17, "sans", True, OLIVE, 1.28, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"] and e["n"] in PRINT_NOTES:
            s += f" ({e['note']})"
        parts.append(s)
    kf.para(" · ".join(parts), 15.5, "sans", False, INK, 1.3, 9)
kf.end_report()
p.foot(8)
p.save(f"{OUT}/p8-exercices.svg")
print("P8 saved, TOTAL exercises:", len(REG))
