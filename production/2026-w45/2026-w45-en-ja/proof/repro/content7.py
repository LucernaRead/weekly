# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/en-ja-proof/repro/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE FOCUS =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LANGUAGE IN HAND · 精講", "The Lucerna", "A2 → B2 · Phrases of the week · 今週の名文")

cA = Flow(p, [(COLX[0], CW)], 200, 1150, tag="P7-A2")
cA.head("LEVEL A2 · 基礎", 27)
cA.head("FALLING BACK", 24)
cA.para("« The clocks fell back. » Fall back = to go back one hour. The past is fell back, not « falled back ». The repeated hour on November 1 is the example of the week (page 2).", 22.5)
cA.head("GOING TO + VERB", 24)
cA.para("For a plan : « She is going to vote on Tuesday. » be + going to + the verb, with no change. It is the friendliest future in English — use it for every plan of the week.", 22.5)
cA.box("THE EXAMPLE · 例文", [
    ("« Americans are going to vote on Tuesday. » — the election story, from page 1.", "serif", False, INK, 21.5, 1.42),
])
cA.end_report()

cB = Flow(p, [(COLX[1], CW)], 200, 1150, tag="P7-B1")
cB.head("LEVEL B1 · 中級", 27)
cB.head("COMPARATIVES", 24)
cB.para("Short adjective + -er + than : « The Bernabéu is bigger than most stadiums. » Long adjective : more + adjective : « more convenient ». And good becomes better — never « more good ». Page 4 is full of them.", 22.5)
cB.head("THE PAST SIMPLE", 24)
cB.para("Regular verbs add -ed : changed, watched. Irregular verbs change : fall → fell, go → went, choose → chose. Use it for what is already finished — the clocks that fell back on November 1, and the « as-if-finished » retellings on page 4. The November 3 election and the November 8 games are still to come at press time, so their results are not past yet.", 22.5)
cB.box("THE EXAMPLE · 例文", [
    ("« The clocks fell back on Sunday, November 1. » — fall → fell (page 2).", "serif", False, INK, 21.5, 1.42),
])
cB.end_report()

cC = Flow(p, [(COLX[2], CW)], 200, 1150, tag="P7-B2")
cC.head("LEVEL B2 · 上級", 27)
cC.head("HEADLINE PRESENT", 24)
cC.para("Headlines speak of yesterday in the present : « America votes », « Bengals play in Madrid ». The present simple makes old news feel live. Read the front page again and find three.", 22.5)
cC.head("WHETHER = IF ?", 24)
cC.para("« Nobody knows whether the race is called yet. » Whether introduces an open question inside a sentence — more elegant than if, and safe everywhere. It is the word for election-night uncertainty.", 22.5)
cC.box("THE EXAMPLE · 例文", [
    ("« Patience is part of the system, not a failure of it. » — part of = 一部 (page 6).", "serif", False, INK, 21.5, 1.42),
])
cC.end_report()

cD = Flow(p, [(COLX[3], CW)], 200, 1150, tag="P7-tools")
cD.head("THE TOOLBOX · 道具箱", 27)
cD.para("Three sentences to keep in your pocket, one for each level :", 22.5)
cD.para("A2 — « It is one o'clock — again ! »", 22.5, "serif", True, OLIVE)
cD.para("B1 — « The clocks fell back on Sunday. »", 22.5)
cD.para("B2 — « Nobody knows whether the race is called yet. »", 22.5, "serif", True, OLIVE)
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
    ("« Tuesday, November 3, is Election Day in the United States. » (page 1)",
     "文法ポイント — is = 〜である；日付が主語の補語になる。",
     "A2", "Election Day ___ on Tuesday, November 3. (be)", "is", "is 〜である"),
    ("« The hour from 1 to 2 happened twice. » (page 2)",
     "文法ポイント — happen の過去形は happened、規則変化。",
     "A2", "The hour ___ twice on Sunday. (happen)", "happened", "happen → happened"),
    ("« Which film would you choose ? » (page 3)",
     "文法ポイント — would + 動詞の原形、選択の意志を表す。",
     "B1", "Which film ___ you choose ? (would)", "would", "would + 原形"),
    ("« Two games, two continents, one league — that is the modern NFL. » (page 4)",
     "文法ポイント — that is = つまり〜だ；ダッシュの後でまとめる。",
     "B1", "That ___ the modern NFL. (be)", "is", "that is つまり〜だ"),
    ("« The results will still be there in the morning. » (page 5)",
     "文法ポイント — will still = 今でも〜するだろう；still は will の後に置く。",
     "B2", "The results ___ still be there. (will)", "will", "will still 今でも〜するだろう"),
    ("« Patience is part of the system, not a failure of it. » (page 6)",
     "文法ポイント — part of = 〜の一部；not で否定の対照を示す。",
     "B2", "Patience ___ part of the system. (be)", "is", "is part of 一部"),
    ("« Not every place changes. » (page 2)",
     "文法ポイント — not every + 単数動詞：すべての場所が変わるとは限らない。",
     "A2", "Not every place ___ . (change)", "changes", "not every → changes"),
    ("« One Sunday is not enough — good thing the week has seven days. » (page 4)",
     "文法ポイント — has = 〜がある；the week は単数なので has を使う。",
     "B1", "The week ___ seven days. (have)", "has", "have → has"),
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
cf.ex("A2", "誤り直し", "He doesn't like voting early.", "三単現の否定は doesn't + 原形",
     "✗ « He don't like voting early. »", instr="誤り直し", size=22.5)
cf.ex("A2", "誤り直し", "Yesterday the clocks fell back.", "fall の過去形は fell",
     "✗ « Yesterday the clocks falled back. »", instr="誤り直し", size=22.5)
cf.ex("B1", "誤り直し", "This game is bigger than last week's.", "bigger はすでに比較級、more は付けない",
     "✗ « This game is more bigger than last week's. »", instr="誤り直し", size=22.5)
cf.ex("B1", "誤り直し", "She is going to watch the film on Friday.", "going to の後は動詞の原形",
     "✗ « She is going to watches the film on Friday. »", instr="誤り直し", size=22.5)
cf.end_report()

rx, rw = span_x(2, 2)
p.rect(rx, by7 + 8, rw, 300, fill=BOX, stroke=LINE, sw=1.4)
p.text(rx + 24, by7 + 48, "READERS' CORNER · 読者のコーナー", 24, "sans", True, OLIVE)
p.para(rx + 24, by7 + 86, "« On Sunday, I slept one hour more — and I still woke up late ! » — M. L., a reader in Chicago (editor's example : no real reader letters had arrived when this issue went to press, so the example stays, honestly labeled)", 21.5, "serif", False, INK, rw - 48, 1.42)
p.para(rx + 24, by7 + 206, "編集部より｜VOL.1ではVOL.2に本物の読者の手紙を載せると約束しましたが、締め切りまでに本物の手紙も、VOL.1の作文投稿の最優秀作も届きませんでした。そこで本号は見本を見本と明示して載せ、約束はVOL.3へ先送りします。あなたの手紙と作文を送ってください。VOL.3に届いた本物の手紙を載せます。", 20, "sans", False, GREY, rw - 48, 1.4)
ty7 = by7 + 332
p.rect(rx, ty7, rw, 2540 - ty7, fill=DARK)
p.text(rx + 24, ty7 + 46, "NEXT WEEK · VOL.3 次号予告", 24, "sans", True, "#f3edda")
p.para(rx + 24, ty7 + 84, "Wednesday, November 11 : Veterans Day. Sunday, November 15 : the NFL in Munich. And the midterm results, reported — who won, and what changes.", 21.5, "serif", False, "#e8dfc8", rw - 48, 1.45)
p.para(rx + 24, ty7 + 218, "来週水曜は退役軍人の日、日曜はNFLミュンヘン戦、そして中間選挙の結果報道。", 20, "sans", False, "#b3a06a", rw - 48, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-langue.svg")
print("P7 saved, exercises so far:", len(REG))
