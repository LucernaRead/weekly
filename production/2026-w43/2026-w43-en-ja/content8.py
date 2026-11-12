# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band('EXERCISES & ANSWERS　練習と解答', "The Lucerna", 'FINAL TEST　総合テスト　Answers at the bottom of this page 解答はこのページの下に')

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1485, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "C", '10月31日はハロウィーン'),
    ("A2", "A", 'carve かぼちゃランタンを彫る'),
    ("B1", "B", 'neither...nor 〜でもなく…でもない'),
    ("A2", "A", 'costume ハロウィーンの仮装'),
    ("A2", "B", 'she は三単現 → wears'),
    ("A2", "B", 'trick or treat でお菓子をもらう'),
    ("B1", "A", 'will + 動詞の原形 fall'),
    ("B1", "C", "be going to → is going"),
]
cnums = [reg_ex(lv, '穴埋め', k, nt) for lv, k, nt in cloze_defs]
bf.head('A　CLOZE　穴埋め', 24)
bf.para(f"Maya is twelve. On Saturday, October 31, it is ({cnums[0]})___. In the morning, she helps her father ({cnums[1]})___ a pumpkin on the porch. « ({cnums[2]})___ rain nor cold can stop us », laughs her mother. In the evening, Maya puts on her ({cnums[3]})___ : she ({cnums[4]})___ a gold crown, like a Greek goddess. She takes her bag and goes from house to house : « Trick or treat ! » The neighbours give her ({cnums[5]})___. At nine o'clock, the street is quiet — and in the night, the clocks will ({cnums[6]})___ back : one more hour of sleep ! Tomorrow, Maya is ({cnums[7]})___ to sleep late, very late.", 21.5)
bf.expl('選択肢：')
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
bf.head('B　MULTIPLE CHOICE　選択', 24)
mcq = [
    ("A2", "B", "9:15 = a quarter past nine", "The game starts at 9:15. In words : ... A. a quarter to nine · B. a quarter past nine · C. half past nine"),
    ("A2", "A", 'we → get 原形', "On Sunday, we ___ an extra hour of sleep. A. get · B. gets · C. getting"),
    ("B1", "B", '終わった試合には won を使う', "The 76ers ___ the game 106–100. A. win · B. won · C. wins"),
    ("B1", "B", 'than → 比較級 hotter', "Austin is ___ than Milwaukee in October. A. hot · B. hotter · C. hottest"),
    ("B2", "A", 'despite + 名詞：雨にもかかわらず', "___ the rain, the parade went on all evening. A. Despite · B. Because · C. Unless"),
    ("B2", "A", 'whether = 〜かどうか', "Nobody knows ___ the Brewers will win the Series. A. whether · B. what · C. who"),
    ("A2", "A", '過去のことは過去形 opened を使う', "Early voting in Texas ___ on Monday. A. opened · B. open · C. opens"),
    ("B1", "A", 'be going to + 原形 cast', "She is going to ___ her ballot on Saturday. A. cast · B. casts · C. casted"),
]
for lv, k, nt, body in mcq:
    bf.ex(lv, '選択', k, nt, body, size=20.5)

# ---- C. reading ----
bf.head('C　READING　読解', 24)
bf.para("On Monday morning, Rosa Delgado, a nurse from Houston, finished her night work at six o'clock. She did not go home to sleep. She drove to the early-voting place near the hospital and joined a short line. « On November 3, I work all day », she explains. « Today, I have time. » Ten minutes later, her ballot was in the box, and a sticker on her jacket said : I VOTED EARLY. By Friday, October 30, when early voting ends in Texas, millions of Texans will do the same.", 21.5)
read_qs = [
    ("A2", "B", '本文：a nurse from Houston', "Rosa is... A. a teacher · B. a nurse · C. a driver"),
    ("A2", "B", '11月3日、彼女は一日中働く', "She voted early because on November 3 she... A. travels · B. works all day · C. sleeps"),
    ("B1", "A", 'ステッカーには I VOTED EARLY とある', "Her sticker said... A. I VOTED EARLY · B. VOTE ON TUESDAY · C. TEXAS FIRST"),
    ("B1", "B", 'テキサスの期日前投票は10月30日まで', "Early voting in Texas ends on... A. October 19 · B. October 30 · C. November 3"),
]
for lv, k, nt, body in read_qs:
    bf.ex(lv, '読解', k, nt, body, size=20.5)

# ---- D. sentence building ----
bf.head('D　SENTENCES　文の完成と変換', 24)
d_items = [
    ("A2", "On Saturday, they are going to carve a pumpkin.", 'are going to + 動詞の原形',
     "Be going to : « On Saturday, they (carve) a pumpkin. » → ___"),
    ("B1", "The Knicks raised their first banner since 1973.", 'raise → raised（規則変化）',
     "Past simple : « The Knicks (raise) their first banner since 1973. »"),
    ("B1", "scarier", 'scary → scarier（y を i に変えて er）',
     "Comparative : « My costume is ___ (scary) than yours. »"),
    ("B2", "Whether", 'whether が「〜かどうか」の節を導く',
     "Whether : « ___ the parade will happen, nobody knows. »"),
]
for lv, k, nt, body in d_items:
    bf.ex(lv, '文の完成', k, nt, body, size=20.5)

# ---- E. translation ----
bf.head('E　TRANSLATION　翻訳', 24)
e_items = [
    ("B2", '投票はもはや一日だけのことではなく、一つの季節である。', 'no longer もう〜ない',
     "Translate : « Voting is no longer a day ; it is a season. »"),
    ("A2", "The 76ers won the game 106–100.", 'win → won ; スコア 106–100',
     '翻訳：76ersが106対100で試合に勝った。'),
    ("B1", "This year, early voting opened on Monday.", 'open → opened ; on Monday',
     '翻訳：今年の期日前投票は月曜日に始まった。'),
    ("B1", 'どちらの球団もワールドシリーズで優勝したことがない。', 'neither は「両方とも〜ない」；has ever won は現在完了',
     "Translate : « Neither club has ever won the Series. »"),
]
for lv, k, nt, body in e_items:
    bf.ex(lv, '翻訳', k, nt, body, size=20.5)

# ---- F. matching ----
bf.head('F　WORDS　語彙の組み合わせ', 24)
bf.match_set("B1", '語彙マッチング',
             ["a midterm", "an incumbent", "a margin", "turnout"],
             ["the number of people who vote", "an election in the middle of a president's term",
              "the person who holds the job now", "the difference between two results"],
             ["b", "c", "d", "a"],
             ['midterm = 中間選挙 b', 'incumbent = 現職 c', 'margin = 差 d', 'turnout = 投票率 a'],
             instr='組み合わせ')

# ---- G. dialogue (register first) ----
dlg_defs = [
    ("A2", "ID", '投票では身分証（ID）を見せる'),
    ("A2", "line", 'line = 列（米語）'),
    ("A2", "ballot", 'ballot = 投票用紙'),
    ("A2", "sticker", 'sticker = ステッカー'),
    ("B1", "November", '選挙日は11月3日'),
]
gnums = [reg_ex(lv, '会話補完', k, nt) for lv, k, nt in dlg_defs]
bf.head('G　DIALOGUE　会話補完', 24)
bf.para(f"— Good morning ! Is this the early-voting place ? — Yes, welcome. May I see your ({gnums[0]})___ ? — Here it is. Is the ({gnums[1]})___ long today ? — No, five minutes only. Yesterday it was very long ! — Good. It is my first early vote. What do I do with the ({gnums[2]})___ ? — Mark your choices, check them twice, then put it in the box. — Thank you. And the famous ({gnums[3]})___ ? Everybody has one on their jacket. — The sticker ! Here it is : « I VOTED ». Wear it with pride. — I will ! See you on ({gnums[4]})___ 3rd, in the results ! — Ha ! Have a good day.", 21.5)
bf.end_report()

# ---- writing strip ----
wy = 1500
p.hline(MX, RIGHT, wy - 14, OLIVE, 2)
reg_ex("B1", '作文', '自由記述 — 要点は作文の枠内、模範文は8ページの作文枠の中', '要点ごとに採点')
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, 'H　WRITING　作文', 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Write a short text (80 to 100 words) : « My Saturday, October 31 ». Tell us : your costume, your street, the candy, the pumpkins — and one sentence about the clocks that fall back in the night. The best texts will appear in VOL.2 (page 7, « Readers' Corner »).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 190, '英語で80–100語で書く：私の10月31日（土曜日）。仮装、通り、お菓子、かぼちゃを書き、夜に時計を戻すことにも一文触れる。', 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 276, fill=BOX)
p.text(mx2 + 22, wy + 38, 'MODEL　模範文', 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "On Saturday, October 31, our street becomes a small Halloween town. In the morning, I carve a pumpkin with my father and we put a candle inside. At six o'clock, I wear my pirate costume and take my bag. House after house, I say « Trick or treat ! » and the neighbours smile and give me candy. My bag is heavy at nine o'clock ! In the night, the clocks fall back, so I sleep one hour more on Sunday. It is my favourite weekend of the autumn.", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 312
p.hline(MX, RIGHT, ky - 12, OLIVE, 2)
p.text(MX, ky + 26, 'ANSWERS　全解答と解説（1–8ページ）', 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2560, tag="P8-keys")
# Printed-note parity with the core (see WEEKLY-KIT): the core build prints a
# note when the item is on page 8, or its (Chinese) note is <= 10 chars, or its
# type is correction/chart-reading. Japanese notes are longer, so the core's
# printed set is applied EXPLICITLY by exercise number: the set of items whose
# notes print here is identical to the core's printed set (62 items).
PRINT_NOTES = {11, 14, 15, 19, 35, 36, 40, 42, 49, 65, 74, 82, 83, 84, 85, 86,
               87, 89, 101, 106, 108, 109, 110, 111, 112, 113, 114, 115, 116,
               117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129,
               130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142,
               143, 144, 145, 146, 147, 148, 149}
from itertools import groupby
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— {pg} ページ —", 17, "sans", True, OLIVE, 1.28, 3)
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
