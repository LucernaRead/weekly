# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-en-ja/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE FOCUS =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LANGUAGE IN HAND · 精講", "The Lucerna", "A2 → B2 · Phrases of the week · 今週の名文")

cA = Flow(p, [(COLX[0], CW)], 200, 1150, tag="P7-A2")
cA.head("LEVEL A2 · 基礎", 27)
cA.head("ELEVEN ELEVEN", 24)
cA.para("« At eleven o'clock, we stop. » Eleven is the number of the week : the eleventh hour, the eleventh day, the eleventh month. Say it slowly : e-LEV-en. The silence starts at eleven — and the word is easy to remember, because the date is the word.", 22.5)
cA.head("WILL + VERB", 24)
cA.para("For a plan or a promise : « We will remember them. » will + the verb, with no change. It is the future of the week — use it for every promise of November 11.", 22.5)
cA.box("THE EXAMPLE · 例文", [
    ("« The silence will last two minutes. » — will + last (page 2).", "serif", False, INK, 21.5, 1.42),
])
cA.end_report()

cB = Flow(p, [(COLX[1], CW)], 200, 1150, tag="P7-B1")
cB.head("LEVEL B1 · 中級", 27)
cB.head("COMPARATIVES", 24)
cB.para("Short adjective + -er + than : « The Allianz Arena is bigger than most NFL stadiums. » Long adjective : more + adjective : « more convenient ». And good becomes better — never « more good ». The Allianz example is on page 4.", 22.5)
cB.head("THE PAST SIMPLE", 24)
cB.para("Regular verbs add -ed : remembered, watched. Irregular verbs change : write → wrote, go → went, choose → chose. Use it for what is already finished — Diwali, which was on November 8, and Bonfire Night, which was on November 5. The November 15 games are still to come at press time, so their results are not past yet.", 22.5)
cB.box("THE EXAMPLE · 例文", [
    ("« Dickens wrote the story in 1843. » — write → wrote (page 3).", "serif", False, INK, 21.5, 1.42),
])
cB.end_report()

cC = Flow(p, [(COLX[2], CW)], 200, 1150, tag="P7-B2")
cC.head("LEVEL B2 · 上級", 27)
cC.head("HEADLINE PRESENT", 24)
cC.para("Headlines speak in the present : « Munich waits for the NFL. » The present simple makes news feel live. Read the front page again and find three present-tense verbs.", 22.5)
cC.head("WHETHER = IF ?", 24)
cC.para("« Nobody knows whether this year will be faster or slower. » Whether introduces an open question inside a sentence — more elegant than if, and safe everywhere. It is the word for counting-week uncertainty.", 22.5)
cC.box("THE EXAMPLE · 例文", [
    ("« Patience is part of the system, not a failure of it. » — part of = 一部 (page 6).", "serif", False, INK, 21.5, 1.42),
])
cC.end_report()

cD = Flow(p, [(COLX[3], CW)], 200, 1150, tag="P7-tools")
cD.head("THE TOOLBOX · 道具箱", 27)
cD.para("Three sentences to keep in your pocket, one for each level :", 22.5)
cD.para("A2 — « At eleven o'clock — we stop. »", 22.5, "serif", True, OLIVE)
cD.para("B1 — « Dickens wrote the story in 1843.»", 22.5)
cD.para("B2 — « Nobody knows whether this year will be faster. »", 22.5, "serif", True, OLIVE)
cD.para("And the newspaper reflex : every phrase of the week comes from an article of this issue. Re-read the article, and the phrase becomes easy.", 22.5)
cD.bridge("道具箱｜今号の持ち歩き文3つ、レベル別に一つずつ。名文はすべて今号の記事から。原文に戻って読むのが一番効く。")
cD.end_report()

# --- phrases of the week ---
py = 1210
p.hline(MX, RIGHT, py - 14, GOLD, 2)
p.text(MX, py + 26, "PHRASES OF THE WEEK · 今週の名文（すべて今号の記事から）", 27, "sans", True, OLIVE)
p.text(RIGHT, py + 26, "各文に文法ポイント1つ＋小問1つ · 解答は8ページ", 20, "sans", False, GREY, anchor="end")
pf = Flow(p, [(COLX[i], CW) for i in range(4)], py + 52, 1830, tag="P7-phrases")
phrases = [
    ("« On Wednesday, November 11, at eleven o'clock in the morning, something quiet happens across the English-speaking world. » (page 1)",
     "文法ポイント — happen は三人称単数で -s がつく。",
     "A2", "Something quiet ___ across the world. (happen)", "happens", "happen → happens"),
    ("« At 11 a.m. on November 11, 1918, the guns of the First World War fell silent. » (page 1)",
     "文法ポイント — fall の過去形は fell。",
     "B1", "The guns ___ silent in 1918. (fall)", "fell", "fall → fell"),
    ("« For two minutes, nobody speaks. » (page 2)",
     "文法ポイント — nobody の後は単数動詞。",
     "A2", "For two minutes, nobody ___. (speak)", "speaks", "nobody → speaks"),
    ("« Christmas is still six weeks away. » (page 3)",
     "文法ポイント — is = 〜である；still = 今も。",
     "B1", "Christmas ___ still six weeks away. (be)", "is", "is = 今も〜である"),
    ("« One Sunday is not enough — good thing the week has seven days. » (page 4)",
     "文法ポイント — has = 〜がある；the week は単数なので has を使う。",
     "B1", "The week ___ seven days. (have)", "has", "have → has"),
    ("« The total will still be there in the morning — and so will the kindness. » (page 5)",
     "文法ポイント — will still = 今でも〜するだろう；still は will の後に置く。",
     "B2", "The total ___ still be there. (will)", "will", "will still = 今でも〜するだろう"),
    ("« Patience is part of the system, not a failure of it. » (page 6)",
     "文法ポイント — of = 〜の；part of = 〜の一部。",
     "B2", "Patience is part of the system, not a failure ___ it. (of)", "of", "of = 〜の"),
    ("« There were no results to print — and this paper invents none. » (page 6)",
     "文法ポイント — there were = there are の過去形。",
     "A2", "There ___ no results to print. (be)", "were", "there were = there are の過去形"),
]
for sent, point, lv, q, key, note in phrases:
    pf.para(sent, 20.5, "serif", True, INK, 1.34, 3)
    pf.bridge(point, 19, 4)
    pf.ex(lv, "音読ドリル", key, note, q, size=20.5)
pf.end_report()

# --- bottom: clinic (left) + readers' corner & teaser (right) ---
by7 = 1870
p.hline(MX, RIGHT, by7 - 14, GOLD, 2)
cf = Flow(p, [(COLX[0], CW), (COLX[1], CW)], by7 + 8, 2268, tag="P7-clinic")
cf.head("THE ERROR CLINIC · 誤りクリニック", 25)
cf.bridge("各文に誤りが1つずつあります。見つけて直しなさい。")
cf.ex("A2", "誤り直し", "He doesn't remember them.", "三単現の否定は doesn't + 原形",
     "✗ « He don't remember them. »", instr="誤り直し", size=22.5)
cf.ex("A2", "誤り直し", "Yesterday the guns fell silent.", "fall の過去形は fell",
     "✗ « Yesterday the guns falled silent. »", instr="誤り直し", size=22.5)
cf.ex("B1", "誤り直し", "This stadium is bigger than most.", "bigger はすでに比較級、more は付けない",
     "✗ « This stadium is more bigger than most. »", instr="誤り直し", size=22.5)
cf.ex("B1", "誤り直し", "She will watch the film on Friday.", "will の後は動詞の原形",
     "✗ « She will watches the film on Friday. »", instr="誤り直し", size=22.5)
cf.end_report()

rx, rw = span_x(2, 2)
p.rect(rx, by7 + 8, rw, 300, fill=BOX, stroke=LINE, sw=1.4)
p.text(rx + 24, by7 + 48, "READERS' CORNER · 読者のコーナー", 24, "sans", True, OLIVE)
p.para(rx + 24, by7 + 86, "« I wore a poppy all week, and I stood still at eleven. Two minutes felt very long — and very short, at the same time. » — an editor's example : no real reader letters had arrived when this issue went to press, so the example stands, honestly labeled", 21.5, "serif", False, INK, rw - 48, 1.42)
p.para(rx + 24, by7 + 206, "編集部より | VOL.2ではVOL.3に本物の読者レターを載せると約束したが、締め切りまでに本物のレターもVOL.2の作文投稿も編集部に届かなかったため、本号ではそのまま正直に伝え、レターをでっち上げることはしない。あなたのレターと作文を送ってほしい。VOL.4からは届いた本物のレターを載せる。", 20, "sans", False, GREY, rw - 48, 1.4)
ty7 = by7 + 332
p.rect(rx, ty7, rw, 2540 - ty7, fill=DARK)
p.text(rx + 24, ty7 + 46, "NEXT WEEK · VOL.4 来週の予告", 24, "sans", True, "#f3edda")
p.para(rx + 24, ty7 + 84, "The verified midterm results — who won, and what changes. The Ashes begin in Perth on Saturday, November 21. « The Hunger Games : Sunrise on the Reaping » opens on Friday, November 20. And your real letters, if they arrive.", 21.5, "serif", False, "#e8dfc8", rw - 48, 1.45)
p.para(rx + 24, ty7 + 218, "確認済みの中間選挙結果、11月21日のアッシュズ初戦、11月20日の『ハンガー・ゲーム』新作、そしてあなたの本物の読者レター。", 20, "sans", False, "#b3a06a", rw - 48, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-langue.svg")
print("P7 saved, exercises so far:", len(REG))
