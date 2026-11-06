# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-ja-nl/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · ことば (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("ことば · Taal", "Lucerna", "言語フォーカス · 三つのレベル、三つのテーマ · Drie niveaus, drie thema's")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 本と読書のことば", 24)
a.para("読書週間は、月よう日に終わりました。10月27日（火よう日）に始まり、9日（月よう日）まででした。今年のスローガンは『静かだけど、冒険中。』でした。", 21.5)
a.para("読書週間が終わっても、本を読む習慣は続きます。図書館で本を借りて、静かな場所で読みましょう。秋の夜は、本を読むのにいちばんいい季節です。", 21.5)
a.bridge("読書週間 Leesweek · 習慣 een gewoonte · 借りる lenen.")
a.ex("A2", "invullen", "9", "De Leesweek eindigt op 9 november (maandag)",
     "読書週間は11月 ___ 日で終わります。", instr="Vul in", size=20.5, gap=10)
a.ex("A2", "invullen", "27", "De Leesweek begon op 27 oktober (dinsdag)",
     "読書週間は10月 ___ 日に始まりました。", instr="Vul in", size=20.5, gap=10)
a.ex("A2", "meerkeuze", "B", "De slogan is 「静かだけど、冒険中。」",
     "今年のスローガンは？ A. 本の秋 · B. 静かだけど、冒険中。 · C. 紅葉の秋", size=20.5, gap=10)
a.ex("A2", "meerkeuze", "A", "De leesgewoonte gaat door na de Leesweek",
     "読書週間が終わっても、何が続きますか。 A. 本を読む習慣 · B. 野球の試合 · C. 鍋の料理", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 七五三のことば", 24)
b.para("七五三のことばを覚えましょう。『七五三』は、3歳と5歳と7歳の子どものお祝いです。『千歳飴』は、赤と白の長い飴です。『晴れ着』は、お祝いの日に着る服です。", 21.5)
b.para("『お参り』は、神社へ行って、頭を下げることです。『神社』は、神さまがいる場所です。家族といっしょに、神社へ行きましょう。", 21.5)
b.bridge("七五三 Shichi-Go-San · 千歳飴 chitose-ame · 晴れ着 feestkleding")
b.ex("B1", "meerkeuze", "B", "Shichi-Go-San viert kinderen van 3, 5 en 7 jaar",
     "『七五三』の意味は？ A. 大人のお祝い · B. 3歳・5歳・7歳の子どものお祝い · C. お菓子の名前", size=20.5, gap=10)
b.ex("B1", "invullen", "千歳飴", "lang rood-wit snoepje",
     "赤と白の長い飴を「___」と言います。", instr="Vul in", size=20.5, gap=10)
b.ex("B1", "meerkeuze", "C", "晴れ着 = feestkleding",
     "『晴れ着』とは？ A. 毎日の服 · B. 寝る時の服 · C. お祝いの日に着る服", size=20.5, gap=10)
b.ex("B1", "invullen", "お参り", "お参り = naar een schrijn gaan om te bidden",
     "神社へ行って、頭を下げることを「___」と言います。", instr="Vul in", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 数字を読む", 24)
c.para("数字の読み方を練習しましょう。『4連勝』は、4試合とも勝つことです。『3%』は、100人のうち3人、という意味です。調査では、「11月15日」は3%でした。", 21.5)
c.para("『6つ』は、平成11年11月11日の「1」の数です。『5,000組以上』は、西宮神社の七五三参りの数です。5,000組より多い、という意味です。", 21.5)
c.bridge("〜連勝 zeges op rij · 〜% procent · 〜組以上 groepen of meer.")
c.ex("B2", "meerkeuze", "B", "alle vier wedstrijden winnen",
     "『4連勝』の意味は？ A. 4試合とも負ける · B. 4試合とも勝つ · C. 4試合引き分ける", size=20.5, gap=10)
c.ex("B2", "meerkeuze", "A", "3 % is ongeveer 3 op 100",
     "『3%』は、100人のうち何人ですか。 A. 3人 · B. 30人 · C. 100人", size=20.5, gap=10)
c.ex("B2", "invullen", "6", "11 november van Heisei 11 had zes enen",
     "平成11年11月11日には、「1」が ___ つ並びました。（2面）", instr="Vul in", size=20.5, gap=10)
c.ex("B2", "invullen", "5,000", "Meer dan 5.000 groepen per jaar bezoeken de Nishinomiya-schrijn",
     "西宮神社では、例年 ___ 組以上が七五三参りに来ます。（3面）", instr="Vul in", size=20.5, gap=10)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「昨日、友達とポッキーを食べます」", "→ 『昨日』があるので過去形：『ポッキーを食べました』。", "Gebruik met 「昨日」 de verleden tijd."),
    ("「私の趣味は本を読むです」", "→ 『こと』が必要です：『本を読むことです』。", "Voeg 「こと」 toe om van een werkwoord een zelfstandig naamwoord te maken."),
    ("「神社に千歳飴をもらいます」", "→ もらう場所は『で』：『神社で千歳飴をもらいます』。", "Gebruik 「で」 voor de plaats waar je iets krijgt."),
    ("「高尾山へ紅葉を見ます」", "→ 見る場所は『で』：『高尾山で紅葉を見ます』。", "Gebruik 「で」 voor de plaats waar je kijkt."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "まちがい診療所 · Foutenkliniek", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "『見頃を追いかける』 — 見頃（いちばん美しい時）＋追いかける（後を追って行くこと）。北から南へ、紅葉の見頃を追いかけて行く、という意味です。"
wcn = "Uitleg: de beste kijktijd achterna."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "今週のフレーム · Kader van de week", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「こんにちは。私は高校生です。読書週間には、図書館で本を3冊読みました。15日には、妹の七五三で神社へ行きます。」— 読者の手紙の例"
ld_nl = "Voorbeeld van de redactie, geen echte brief. Tot de deadline kwamen er geen echte brieven en geen beste opstellen; beide verschijnen in VOL.4. Stuur ons je brief in het Japans: de gekozen brieven worden afgedrukt in VOL.4!"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld_nl, "sans", False, 20, CW - 44)) * 29 + 26 + 16
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "読者の手紙 · Lezershoek", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, ld_nl, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "今週のフレーズ · Zinnen van de week (letterlijk uit dit nummer)", 27, "sans", True, OLIVE)
quotes = [
    ("「読書週間は、9日（月よう日）で終わります。」", "De Leesweek eindigt op maandag 9 november.", "p. 1"),
    ("「15日（日よう日）は、七五三の中心の日です。」", "Zondag 15 november is het hart van Shichi-Go-San.", "p. 1"),
    ("「『ポッキー＆プリッツの日』は、1999年に始まりました。」", "Pocky- en Pretz-dag begon in 1999.", "p. 2"),
    ("「千歳飴は、長く生きてほしい、という願いのお菓子です。」", "Chitose-ame is het snoepje van de wens voor een lang leven.", "p. 2"),
    ("「七五三は、3歳と5歳と7歳の子どものお祝いです。」", "Shichi-Go-San viert kinderen van 3, 5 en 7 jaar.", "p. 3"),
    ("「ソフトバンクが4連勝で日本一になりました。」", "SoftBank pakte de Japanse titel met vier zeges op rij.", "p. 4"),
    ("「11月11日は、ポッキーの日です。」", "11 november is Pocky-dag.", "p. 5"),
    ("「紅葉の見頃は、北から南へ移ります。」", "De beste bladtijd gaat van noord naar zuid.", "p. 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 132
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 132 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "来週 · Volgend nummer (VOL.4)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "酉の市は19日（木）に二の酉があります。相撲の千秋楽は22日（日）です。紅葉の見頃は、京都へ移ります。読者の手紙と第8版の作文の優秀作も載せます。お楽しみに！", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-kotoba.svg")
print("P7 saved, exercises so far:", len(REG))
