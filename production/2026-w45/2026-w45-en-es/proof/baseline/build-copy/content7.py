# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/en-es-proof/baseline/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE FOCUS =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LANGUAGE IN HAND · 精讲", "The Lucerna", "A2 → B2 · Phrases of the week · 本周金句")

cA = Flow(p, [(COLX[0], CW)], 200, 1150, tag="P7-A2")
cA.head("LEVEL A2 · 基础", 27)
cA.head("FALLING BACK", 24)
cA.para("« The clocks fell back. » Fall back = to go back one hour. The past is fell back, not « falled back ». The repeated hour on November 1 is the example of the week (page 2).", 22.5)
cA.head("GOING TO + VERB", 24)
cA.para("For a plan : « She is going to vote on Tuesday. » be + going to + the verb, with no change. It is the friendliest future in English — use it for every plan of the week.", 22.5)
cA.box("THE EXAMPLE · 例句", [
    ("« Americans are going to vote on Tuesday. » — the election story, from page 1.", "serif", False, INK, 21.5, 1.42),
])
cA.end_report()

cB = Flow(p, [(COLX[1], CW)], 200, 1150, tag="P7-B1")
cB.head("LEVEL B1 · 进阶", 27)
cB.head("COMPARATIVES", 24)
cB.para("Short adjective + -er + than : « The Bernabéu is bigger than most stadiums. » Long adjective : more + adjective : « more convenient ». And good becomes better — never « more good ». Page 4 is full of them.", 22.5)
cB.head("THE PAST SIMPLE", 24)
cB.para("Regular verbs add -ed : changed, watched. Irregular verbs change : fall → fell, go → went, choose → chose. Use it for what is already finished — the clocks that fell back on November 1, and the « as-if-finished » retellings on page 4. The November 3 election and the November 8 games are still to come at press time, so their results are not past yet.", 22.5)
cB.box("THE EXAMPLE · 例句", [
    ("« The clocks fell back on Sunday, November 1. » — fall → fell (page 2).", "serif", False, INK, 21.5, 1.42),
])
cB.end_report()

cC = Flow(p, [(COLX[2], CW)], 200, 1150, tag="P7-B2")
cC.head("LEVEL B2 · 挑战", 27)
cC.head("HEADLINE PRESENT", 24)
cC.para("Headlines speak of yesterday in the present : « America votes », « Bengals play in Madrid ». The present simple makes old news feel live. Read the front page again and find three.", 22.5)
cC.head("WHETHER = IF ?", 24)
cC.para("« Nobody knows whether the race is called yet. » Whether introduces an open question inside a sentence — more elegant than if, and safe everywhere. It is the word for election-night uncertainty.", 22.5)
cC.box("THE EXAMPLE · 例句", [
    ("« Patience is part of the system, not a failure of it. » — part of = 一部分 (page 6).", "serif", False, INK, 21.5, 1.42),
])
cC.end_report()

cD = Flow(p, [(COLX[3], CW)], 200, 1150, tag="P7-tools")
cD.head("THE TOOLBOX · 工具箱", 27)
cD.para("Three sentences to keep in your pocket, one for each level :", 22.5)
cD.para("A2 — « It is one o'clock — again ! »", 22.5, "serif", True, OLIVE)
cD.para("B1 — « The clocks fell back on Sunday. »", 22.5)
cD.para("B2 — « Nobody knows whether the race is called yet. »", 22.5, "serif", True, OLIVE)
cD.para("And the newspaper reflex : every phrase of the week comes from an article of this issue. Re-read the article, and the phrase becomes easy.", 22.5)
cD.bridge("工具箱｜本期三句随身句，按级各一；金句全部出自本期文章，回读原文最有效。")
cD.end_report()

# --- phrases of the week ---
py = 1210
p.hline(MX, RIGHT, py - 14, GOLD, 2)
p.text(MX, py + 26, "PHRASES OF THE WEEK · 本周金句（全部出自本期文章）", 27, "sans", True, OLIVE)
p.text(RIGHT, py + 26, "每句一个语法点 + 一道小题 · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")
pf = Flow(p, [(COLX[i], CW) for i in range(4)], py + 52, 1830, tag="P7-phrases")
phrases = [
    ("« Tuesday, November 3, is Election Day in the United States. » (page 1)",
     "语法点｜is = 是；日期作主语补足语。",
     "A2", "Election Day ___ on Tuesday, November 3. (be)", "is", "is 是"),
    ("« The hour from 1 to 2 happened twice. » (page 2)",
     "语法点｜happen 的过去式是 happened，规则变化。",
     "A2", "The hour ___ twice on Sunday. (happen)", "happened", "happen → happened"),
    ("« Which film would you choose ? » (page 3)",
     "语法点｜would + 动词原形，表选择意愿。",
     "B1", "Which film ___ you choose ? (would)", "would", "would + 原形"),
    ("« Two games, two continents, one league — that is the modern NFL. » (page 4)",
     "语法点｜that is = 那就是；破折号后总结。",
     "B1", "That ___ the modern NFL. (be)", "is", "that is 那就是"),
    ("« The results will still be there in the morning. » (page 5)",
     "语法点｜will still = 仍然会；still 放在 will 之后。",
     "B2", "The results ___ still be there. (will)", "will", "will still 仍然会"),
    ("« Patience is part of the system, not a failure of it. » (page 6)",
     "语法点｜part of = ……的一部分；not 表否定对照。",
     "B2", "Patience ___ part of the system. (be)", "is", "is part of 一部分"),
    ("« Not every place changes. » (page 2)",
     "语法点｜not every + 单数动词：并非每处都变。",
     "A2", "Not every place ___ . (change)", "changes", "not every → changes"),
    ("« One Sunday is not enough — good thing the week has seven days. » (page 4)",
     "语法点｜has = 有；the week 单数用 has。",
     "B1", "The week ___ seven days. (have)", "has", "have → has"),
]
for sent, point, lv, q, key, note in phrases:
    pf.para(sent, 20.5, "serif", True, INK, 1.34, 3)
    pf.bridge(point, 19, 4)
    pf.ex(lv, "跟练", key, note, q, size=20.5)
pf.end_report()

# --- bottom: clinic (left) + readers' corner & teaser (right) ---
by7 = 1870
p.hline(MX, RIGHT, by7 - 14, GOLD, 2)
cf = Flow(p, [(COLX[0], CW), (COLX[1], CW)], by7 + 8, 2268, tag="P7-clinic")
cf.head("THE ERROR CLINIC · 易错诊所", 25)
cf.bridge("每句有一处错误：找出来并改正。")
cf.ex("A2", "改错", "He doesn't like voting early.", "三单否定用 doesn't + 原形",
     "✗ « He don't like voting early. »", instr="改错", size=22.5)
cf.ex("A2", "改错", "Yesterday the clocks fell back.", "fall 的过去式是 fell",
     "✗ « Yesterday the clocks falled back. »", instr="改错", size=22.5)
cf.ex("B1", "改错", "This game is bigger than last week's.", "bigger 已含比较级，不要再加 more",
     "✗ « This game is more bigger than last week's. »", instr="改错", size=22.5)
cf.ex("B1", "改错", "She is going to watch the film on Friday.", "going to 后用动词原形",
     "✗ « She is going to watches the film on Friday. »", instr="改错", size=22.5)
cf.end_report()

rx, rw = span_x(2, 2)
p.rect(rx, by7 + 8, rw, 300, fill=BOX, stroke=LINE, sw=1.4)
p.text(rx + 24, by7 + 48, "READERS' CORNER · 读者园地", 24, "sans", True, OLIVE)
p.para(rx + 24, by7 + 86, "« On Sunday, I slept one hour more — and I still woke up late ! » — M. L., a reader in Chicago (editor's example : no real reader letters had arrived when this issue went to press, so the example stays, honestly labeled)", 21.5, "serif", False, INK, rw - 48, 1.42)
p.para(rx + 24, by7 + 206, "编辑说明｜VOL.1 曾承诺 VOL.2 刊登真实来信，但截至发稿编辑部未收到真实来信与 VOL.1 写作投稿，故本期如实说明、不虚构来信；请把你的来信与写作寄来，VOL.3 起刊登收到的真实来信。", 20, "sans", False, GREY, rw - 48, 1.4)
ty7 = by7 + 332
p.rect(rx, ty7, rw, 2540 - ty7, fill=DARK)
p.text(rx + 24, ty7 + 46, "NEXT WEEK · VOL.3 下周预告", 24, "sans", True, "#f3edda")
p.para(rx + 24, ty7 + 84, "Wednesday, November 11 : Veterans Day. Sunday, November 15 : the NFL in Munich. And the midterm results, reported — who won, and what changes.", 21.5, "serif", False, "#e8dfc8", rw - 48, 1.45)
p.para(rx + 24, ty7 + 218, "下周三退伍军人节，周日 NFL 慕尼黑赛；还有中期选举结果报道。", 20, "sans", False, "#b3a06a", rw - 48, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-langue.svg")
print("P7 saved, exercises so far:", len(REG))
