# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE FOCUS =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LANGUAGE IN HAND　精講", "The Lucerna", "A2 → B2　Phrases of the week　本週金句")

cA = Flow(p, [(COLX[0], CW)], 200, 1150, tag="P7-A2")
cA.head("LEVEL A2　基礎", 27)
cA.head("FALLING BACK", 24)
cA.para("« The clocks fell back. » Fall back = to go back one hour. The past is fell back, not « falled back ». The repeated hour on November 1 is the example of the week (page 2).", 22.5)
cA.head("GOING TO + VERB", 24)
cA.para("For a plan : « She is going to vote on Tuesday. » be + going to + the verb, with no change. It is the friendliest future in English — use it for every plan of the week.", 22.5)
cA.box("THE EXAMPLE　例句", [
    ("« Americans are going to vote on Tuesday. » — the election story, from page 1.", "serif", False, INK, 21.5, 1.42),
])
cA.end_report()

cB = Flow(p, [(COLX[1], CW)], 200, 1150, tag="P7-B1")
cB.head("LEVEL B1　進階", 27)
cB.head("COMPARATIVES", 24)
cB.para("Short adjective + -er + than : « The Bernabéu is bigger than most stadiums. » Long adjective : more + adjective : « more convenient ». And good becomes better — never « more good ». Page 4 is full of them.", 22.5)
cB.head("THE PAST SIMPLE", 24)
cB.para("Regular verbs add -ed : changed, watched. Irregular verbs change : fall → fell, go → went, choose → chose. Use it for what is already finished — the clocks that fell back on November 1, and the « as-if-finished » retellings on page 4. The November 3 election and the November 8 games are still to come at press time, so their results are not past yet.", 22.5)
cB.box("THE EXAMPLE　例句", [
    ("« The clocks fell back on Sunday, November 1. » — fall → fell (page 2).", "serif", False, INK, 21.5, 1.42),
])
cB.end_report()

cC = Flow(p, [(COLX[2], CW)], 200, 1150, tag="P7-B2")
cC.head("LEVEL B2　挑戰", 27)
cC.head("HEADLINE PRESENT", 24)
cC.para("Headlines speak of yesterday in the present : « America votes », « Bengals play in Madrid ». The present simple makes old news feel live. Read the front page again and find three.", 22.5)
cC.head("WHETHER = IF ?", 24)
cC.para("« Nobody knows whether the race is called yet. » Whether introduces an open question inside a sentence — more elegant than if, and safe everywhere. It is the word for election-night uncertainty.", 22.5)
cC.box("THE EXAMPLE　例句", [
    ("« Patience is part of the system, not a failure of it. » — part of = 一部分 (page 6).", "serif", False, INK, 21.5, 1.42),
])
cC.end_report()

cD = Flow(p, [(COLX[3], CW)], 200, 1150, tag="P7-tools")
cD.head("THE TOOLBOX　工具箱", 27)
cD.para("Three sentences to keep in your pocket, one for each level :", 22.5)
cD.para("A2 — « It is one o'clock — again ! »", 22.5, "serif", True, OLIVE)
cD.para("B1 — « The clocks fell back on Sunday. »", 22.5)
cD.para("B2 — « Nobody knows whether the race is called yet. »", 22.5, "serif", True, OLIVE)
cD.para("And the newspaper reflex : every phrase of the week comes from an article of this issue. Re-read the article, and the phrase becomes easy.", 22.5)
cD.expl("工具箱｜本期三句隨身句，按級各一；金句全部出自本期文章，回讀原文最有效。")
cD.end_report()

# --- phrases of the week ---
py = 1210
p.hline(MX, RIGHT, py - 14, OLIVE, 2)
p.text(MX, py + 26, "PHRASES OF THE WEEK　本週金句（全部出自本期文章）", 27, "sans", True, OLIVE)
p.text(RIGHT, py + 26, "每句一個語法點 + 一道小題　答案見第8版", 20, "sans", False, GREY, anchor="end")
pf = Flow(p, [(COLX[i], CW) for i in range(4)], py + 52, 1830, tag="P7-phrases")
phrases = [
    ("« Tuesday, November 3, is Election Day in the United States. » (page 1)",
     "語法點｜is = 是；日期作主語補足語。",
     "A2", "Election Day ___ on Tuesday, November 3. (be)", "is", "is 是"),
    ("« The hour from 1 to 2 happened twice. » (page 2)",
     "語法點｜happen 過去式是 happened，規則變化。",
     "A2", "The hour ___ twice on Sunday. (happen)", "happened", "happen → happened"),
    ("« Which film would you choose ? » (page 3)",
     "語法點｜would + 動詞原形，表選擇意願。",
     "B1", "Which film ___ you choose ? (would)", "would", "would + 原形"),
    ("« Two games, two continents, one league — that is the modern NFL. » (page 4)",
     "語法點｜that is = 那就是；破折號後總結。",
     "B1", "That ___ the modern NFL. (be)", "is", "that is 那就是"),
    ("« The results will still be there in the morning. » (page 5)",
     "語法點｜will still = 仍然會；still 放在 will 之後。",
     "B2", "The results ___ still be there. (will)", "will", "will still 仍然會"),
    ("« Patience is part of the system, not a failure of it. » (page 6)",
     "語法點｜part of = ……的一部分；not 表否定。",
     "B2", "Patience ___ part of the system. (be)", "is", "is part of 一部分"),
    ("« Not every place changes. » (page 2)",
     "語法點｜not every + 單數動詞：並非每處都變。",
     "A2", "Not every place ___ . (change)", "changes", "not every → changes"),
    ("« One Sunday is not enough — good thing the week has seven days. » (page 4)",
     "語法點｜has = 有；the week 單數用 has。",
     "B1", "The week ___ seven days. (have)", "has", "have → has"),
]
for sent, point, lv, q, key, note in phrases:
    pf.para(sent, 20.5, "serif", True, INK, 1.34, 3)
    pf.expl(point, 19, 4)
    pf.ex(lv, "跟練", key, note, q, size=20.5)
pf.end_report()

# --- bottom: clinic (left) + readers' corner & teaser (right) ---
by7 = 1870
p.hline(MX, RIGHT, by7 - 14, OLIVE, 2)
cf = Flow(p, [(COLX[0], CW), (COLX[1], CW)], by7 + 8, 2268, tag="P7-clinic")
cf.head("THE ERROR CLINIC　易錯診所", 25)
cf.expl("每句有一處錯誤：找出來並改正。")
cf.ex("A2", "改錯", "He doesn't like voting early.", "三單否定用 doesn't + 原形",
     "✗ « He don't like voting early. »", instr="改錯", size=22.5)
cf.ex("A2", "改錯", "Yesterday the clocks fell back.", "fall 的過去式是 fell",
     "✗ « Yesterday the clocks falled back. »", instr="改錯", size=22.5)
cf.ex("B1", "改錯", "This game is bigger than last week's.", "bigger 已含比較級，不要再加 more",
     "✗ « This game is more bigger than last week's. »", instr="改錯", size=22.5)
cf.ex("B1", "改錯", "She is going to watch the film on Friday.", "going to 後用動詞原形",
     "✗ « She is going to watches the film on Friday. »", instr="改錯", size=22.5)
cf.end_report()

rx, rw = span_x(2, 2)
p.rect(rx, by7 + 8, rw, 300, fill=BOX)
p.text(rx + 24, by7 + 48, "READERS' CORNER　讀者園地", 24, "sans", True, OLIVE)
p.para(rx + 24, by7 + 86, "« On Sunday, I slept one hour more — and I still woke up late ! » — M. L., a reader in Chicago (editor's example : no real reader letters had arrived when this issue went to press, so the example stays, honestly labeled)", 21.5, "serif", False, INK, rw - 48, 1.42)
p.para(rx + 24, by7 + 206, "編輯說明｜截至發稿，編輯部未收到真實來信，也沒有收到可刊登的 VOL.1 寫作投稿；本期園地所刊為編輯部示例，刊登真實來信的承諾順延至 VOL.3。請把你的來信與寫作寄來，VOL.3 起刊登收到的真實來信。", 20, "sans", False, GREY, rw - 48, 1.4)
ty7 = by7 + 332
p.rect(rx, ty7, rw, 2560 - ty7, fill=CLOTH)
p.text(rx + 24, ty7 + 46, "NEXT WEEK　VOL.3 下週預告", 24, "sans", True, ONCLOTH)
p.para(rx + 24, ty7 + 84, "Wednesday, November 11 : Veterans Day. Sunday, November 15 : the NFL in Munich. And the midterm results, reported — who won, and what changes.", 21.5, "serif", False, "#cac8ba", rw - 48, 1.45)
p.para(rx + 24, ty7 + 218, "下週三退伍軍人節，週日 NFL 慕尼黑賽；還有中期選舉結果報導。", 20, "sans", False, GOOSE, rw - 48, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-langue.svg")
print("P7 saved, exercises so far:", len(REG))
