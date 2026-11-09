# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("EXERCISES & ANSWERS　練習と解答", "The Lucerna", "FINAL TEST　総合評価　Answers at the bottom of this page 解答はこのページの下に")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1485, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "B", "11月11日は水曜日"),
    ("A2", "A", "poppy = ポピー"),
    ("B1", "C", "silence = 沈黙・黙とう"),
    ("A2", "B", "eleven = 11"),
    ("A2", "A", "パドジー、黄色いクマの子"),
    ("A2", "C", "will + 動詞の原形 know"),
    ("B1", "B", "be going to → is going"),
    ("B1", "A", "still = 今も"),
]
cnums = [reg_ex(lv, "空所補充", k, nt) for lv, k, nt in cloze_defs]
bf.head("A　CLOZE　空所補充", 24, gap=8)
bf.para(f"Maya is sixteen. On ({cnums[0]})___, November 11, she wears a red ({cnums[1]})___ to school. At eleven o'clock, the whole school stands in ({cnums[2]})___ for two minutes. « ({cnums[3]})___, eleven, eleven », says her teacher. On Friday, Maya bakes cakes for ({cnums[4]})___, the yellow bear. « When ({cnums[5]})___ we know the total ? » asks Maya. « On Friday night », says her mother. « On Sunday, Maya is ({cnums[6]})___ to watch the game from Munich — and the poppy will ({cnums[7]})___ be on her coat. »", 21.5)
bf.bridge("選択肢：")
for n, (lv, _k, _nt), opts in zip(cnums, cloze_defs, [
    "A. Monday · B. Wednesday · C. Friday",
    "A. poppy · B. hat · C. ticket",
    "A. noise · B. music · C. silence",
    "A. Ten · B. Eleven · C. Twelve",
    "A. Pudsey · B. Scrooge · C. Dickens",
    "A. do · B. are · C. will",
    "A. goes · B. going · C. go",
    "A. still · B. never · C. soon",
]):
    bf.para(f"{n}. [{lv}] {opts}", 19.5, "sans", False, INK, 1.32, 2)

# ---- B. single choice ----
bf.head("B　MULTIPLE CHOICE　選択", 24, gap=8)
mcq = [
    ("A2", "B", "11時 = eleven o'clock", "The silence begins at 11 a.m. In words : ... A. ten o'clock · B. eleven o'clock · C. twelve o'clock"),
    ("A2", "A", "we → wear（原形）", "On Wednesday, we ___ a poppy. A. wear · B. wears · C. wearing"),
    ("B1", "B", "起きたことは wrote を使う", "Dickens ___ the story in 1843. A. writes · B. wrote · C. writing"),
    ("B1", "B", "than → 比較級 bigger", "The Allianz Arena is ___ than most NFL stadiums. A. big · B. bigger · C. biggest"),
    ("B2", "A", "despite + 名詞：雨にもかかわらず", "___ the rain, the ceremony went on all morning. A. Despite · B. Because · C. Unless"),
    ("B2", "A", "whether = 〜かどうか", "Nobody knows ___ this year will be faster. A. whether · B. what · C. who"),
    ("A2", "A", "未来形 will + 動詞の原形", "The film ___ on Friday, November 13. A. will open · B. will opened · C. will opens"),
    ("B1", "A", "be going to + 動詞の原形 watch", "They are going to ___ the game on Sunday. A. watch · B. watches · C. watched"),
    ("B1", "C", "challenge yourself = チャレンジしてみよう", "« Challenge yourself » means... A. the show is over · B. voting is closed · C. take on a challenge"),
]
for lv, k, nt, body in mcq:
    bf.ex(lv, "選択", k, nt, body, size=20.5, gap=8)

# ---- C. reading ----
bf.head("C　READING　読解", 24, gap=8)
bf.para("On Wednesday morning, Tom, a teacher from Manchester, finished his breakfast and walked to school early. At eleven o'clock, the whole school stood still for two minutes. There was no sound in the hall. « We remember them », said Tom, quietly. In the afternoon, his class baked 26 cakes for Children in Need, and a poppy box stood by the door. On Friday night, Tom watched the appeal show with his family — and Pudsey was, as always, yellow and smiling.", 21.5)
read_qs = [
    ("A2", "B", "本文では a teacher from Manchester", "Tom is... A. a nurse · B. a teacher · C. a driver"),
    ("A2", "B", "全校で2分間の黙とう", "At eleven o'clock, the school... A. sang · B. stood still for two minutes · C. went home"),
    ("B1", "A", "クラスはケーキを26個焼いた", "His class baked... A. 26 cakes · B. 11 cakes · C. 13 cakes", ),
    ("B1", "B", "パドジーはいつも通り黄色い", "On Friday night, Pudsey was... A. red · B. yellow and smiling · C. asleep"),
]
for lv, k, nt, body in read_qs:
    bf.ex(lv, "読解", k, nt, body, size=20.5, gap=8)

# ---- D. sentence building ----
bf.head("D　SENTENCES　文の完成と書きかえ", 24, gap=8)
d_items = [
    ("A2", "On Friday, they will watch the appeal show.", "will + 動詞の原形",
     "Will future : « On Friday, they (watch) the appeal show. » → ___"),
    ("B1", "The guns fell silent in 1918.", "fall → fell（不規則変化）",
     "Past simple : « The guns (fall) silent in 1918. »"),
    ("B1", "bigger", "big → bigger（比較級）",
     "Comparative : « The arena is ___ (big) than most stadiums. »"),
    ("B2", "Whether", "whether が「〜かどうか」の節を導く",
     "Whether : « ___ this year will be faster, nobody knows yet. »"),
]
for lv, k, nt, body in d_items:
    bf.ex(lv, "文の完成", k, nt, body, size=20.5, gap=8)

# ---- E. translation ----
bf.head("E　TRANSLATION　翻訳", 24, gap=8)
e_items = [
    ("B2", "忍耐は制度の一部であり、制度の失敗ではない。", "part of = 一部；not a failure = 失敗ではない",
     "Translate : « Patience is part of the system, not a failure of it. »"),
    ("A2", "11月11日水曜日の午前11時、イギリスは2分間の黙とうをささげる。", "at 11 a.m.；two minutes of silence",
     "訳しなさい：At 11 a.m. on Wednesday, November 11, Britain holds two minutes of silence."),
    ("B1", "今週の日曜日、NFLはミュンヘンで試合をする。", "on Sunday；in Munich",
     "訳しなさい：On Sunday, the NFL plays in Munich."),
    ("B1", "すべての国が同じ名前で呼んでいるわけではない。", "not every = すべての〜ではない；call = 〜と呼ぶ",
     "Translate : « Not every country calls it by the same name. »"),
]
for lv, k, nt, body in e_items:
    bf.ex(lv, "翻訳", k, nt, body, size=20.5, gap=8)

# ---- F. matching ----
bf.head("F　WORDS　語彙の組み合わせ", 24, gap=8)
bf.match_set("B1", "語彙マッチング",
             ["a silence", "an armistice", "a runoff", "a miser"],
             ["the second vote, when no one wins a majority",
              "a quiet time with no speaking",
              "an agreement to stop fighting",
              "a person who loves money and hates spending it"],
             ["b", "c", "a", "d"],
             ["silence = 沈黙・黙とう b", "armistice = 休戦協定 c", "runoff = 決選投票 a", "miser = けちん坊 d"],
             instr="語と意味を結ぶ")

# ---- G. dialogue (register first) ----
dlg_defs = [
    ("A2", "ticket", "ticket = チケット"),
    ("A2", "line", "line = 行列（アメリカ英語）"),
    ("A2", "scarf", "scarf = マフラー"),
    ("A2", "anthem", "anthem = 国歌・賛歌"),
    ("B1", "Sunday", "試合は11月15日日曜日"),
]
gnums = [reg_ex(lv, "会話補完", k, nt) for lv, k, nt in dlg_defs]
bf.head("G　DIALOGUE　会話補完", 24, gap=8)
bf.para(f"— Good morning ! Is this the way to the Allianz Arena ? — Yes, welcome. May I see your ({gnums[0]})___ ? — Here it is. Is the ({gnums[1]})___ long ? — No, five minutes only. It is my first NFL game. What do I do with the ({gnums[2]})___ ? — Wear it with pride, and cheer for the Lions. — And the famous ({gnums[3]})___ ? — Two anthems, one game. Enjoy Munich. — I will ! See you on ({gnums[4]})___ ! — Have a good day.", 20.5)
bf.para("Levels : 145–148 [A2] · 149 [B1]", 19.5, "sans", False, GREY, 1.32, 2)
bf.end_report()

# ---- writing strip ----
wy = 1500
p.hline(MX, RIGHT, wy - 14, OLIVE, 2)
reg_ex("B1", "作文", "自由記述 — 要点は作文の枠内、模範文は8ページの作文枠の中", "要点ごとに採点")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H　WRITING　作文 [B1]", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Write a short text (80 to 100 words) : « My Wednesday, November 11 ». Tell us : did you stand still at eleven, what did you wear, what did you watch on Friday — and one sentence about the game in Munich on Sunday. The best texts will appear in VOL.4 (page 7, « Readers' Corner »).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 190, "英語で80〜100語で書こう：「私の11月11日水曜日」。11時にじっと立っていたか、何を身につけたか、金曜日に何を見たか、そして日曜日のミュンヘンの試合について1文。", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 276, fill=BOX)
p.text(mx2 + 22, wy + 38, "MODEL　模範文", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "On Wednesday, November 11, our school stopped for two minutes. At eleven o'clock, the hall went quiet, and I thought about the soldiers of the First World War. In the evening, we watched the news from London, and my mother wore her poppy at dinner. On Friday, we baked 26 cakes for Children in Need, and Pudsey smiled from the television. On Sunday, we watched the game from Munich. It was a week of silence, kindness and sport — and I slept well, because I had remembered.", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 312
p.hline(MX, RIGHT, ky - 12, OLIVE, 2)
p.text(MX, ky + 26, "ANSWERS　全解答と解説（1–8ページ）", 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2560, tag="P8-keys")
PRINT_NOTES = [8, 9, 15, 23, 31, 32, 37, 39, 48, 50, 55, 57, 67, 68, 72, 82, 83, 84, 85, 86, 87, 89, 90, 92, 103, 104, 106, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]
from itertools import groupby
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— {pg} ページ —", 17, "sans", True, OLIVE, 1.28, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"] and (pg == 8 or e["n"] in PRINT_NOTES):
            s += f" ({e['note']})"
        parts.append(s)
    kf.para(" · ".join(parts), 15.5, "sans", False, INK, 1.3, 9)
kf.end_report()
p.foot(8)
p.save(f"{OUT}/p8-exercices.svg")
print("P8 saved, TOTAL exercises:", len(REG))
