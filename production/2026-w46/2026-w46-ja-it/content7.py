# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-ja-it/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · ことば (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("ことば · Lingua", "Lucerna", "言語フォーカス · 三つのレベル、三つのテーマ · Tre livelli, tre temi")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 本と読書のことば", 24)
a.para("読書週間は、月よう日に終わりました。10月27日（火よう日）に始まり、9日（月よう日）まででした。今年のスローガンは『静かだけど、冒険中。』でした。", 21.5)
a.para("読書週間が終わっても、本を読む習慣は続きます。図書館で本を借りて、静かな場所で読みましょう。秋の夜は、本を読むのにいちばんいい季節です。", 21.5)
a.bridge("読書週間 Settimana della Lettura · 習慣 un'abitudine · 借りる prendere in prestito.")
a.ex("A2", "da completare", "9", "La Settimana della Lettura finisce il 9 novembre (lunedì)",
     "読書週間は11月 ___ 日で終わります。", instr="Completa", size=20.5, gap=10)
a.ex("A2", "da completare", "27", "La Settimana della Lettura è iniziata il 27 ottobre (martedì)",
     "読書週間は10月 ___ 日に始まりました。", instr="Completa", size=20.5, gap=10)
a.ex("A2", "scelta multipla", "B", "Lo slogan è 「静かだけど、冒険中。」",
     "今年のスローガンは？ A. 本の秋 · B. 静かだけど、冒険中。 · C. 紅葉の秋", size=20.5, gap=10)
a.ex("A2", "scelta multipla", "A", "L'abitudine di leggere continua dopo la Settimana della Lettura",
     "読書週間が終わっても、何が続きますか。 A. 本を読む習慣 · B. 野球の試合 · C. 鍋の料理", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 七五三のことば", 24)
b.para("七五三のことばを覚えましょう。『七五三』は、3歳と5歳と7歳の子どものお祝いです。『千歳飴』は、赤と白の長い飴です。『晴れ着』は、お祝いの日に着る服です。", 21.5)
b.para("『お参り』は、神社へ行って、頭を下げることです。『神社』は、神さまがいる場所です。家族といっしょに、神社へ行きましょう。", 21.5)
b.bridge("七五三 Shichi-Go-San · 千歳飴 chitose-ame · 晴れ着 abiti da festa")
b.ex("B1", "scelta multipla", "B", "Shichi-Go-San celebra i bambini di 3, 5 e 7 anni",
     "『七五三』の意味は？ A. 大人のお祝い · B. 3歳・5歳・7歳の子どものお祝い · C. お菓子の名前", size=20.5, gap=10)
b.ex("B1", "da completare", "千歳飴", "lunga caramella rossa e bianca",
     "赤と白の長い飴を「___」と言います。", instr="Completa", size=20.5, gap=10)
b.ex("B1", "scelta multipla", "C", "晴れ着 = abiti da festa",
     "『晴れ着』とは？ A. 毎日の服 · B. 寝る時の服 · C. お祝いの日に着る服", size=20.5, gap=10)
b.ex("B1", "da completare", "お参り", "お参り = andare a pregare al santuario",
     "神社へ行って、頭を下げることを「___」と言います。", instr="Completa", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 数字を読む", 24)
c.para("数字の読み方を練習しましょう。『4連勝』は、4試合とも勝つことです。『3%』は、100人のうち3人、という意味です。調査では、「11月15日」は3%でした。", 21.5)
c.para("『6つ』は、平成11年11月11日の「1」の数です。『5,000組以上』は、西宮神社の七五三参りの数です。5,000組より多い、という意味です。", 21.5)
c.bridge("〜連勝 vittorie di fila · 〜% per cento · 〜組以上 gruppi o più.")
c.ex("B2", "scelta multipla", "B", "vincere tutte e quattro le partite",
     "『4連勝』の意味は？ A. 4試合とも負ける · B. 4試合とも勝つ · C. 4試合引き分ける", size=20.5, gap=10)
c.ex("B2", "scelta multipla", "A", "3 % è circa 3 su 100",
     "『3%』は、100人のうち何人ですか。 A. 3人 · B. 30人 · C. 100人", size=20.5, gap=10)
c.ex("B2", "da completare", "6", "L'11 novembre di Heisei 11 aveva sei 1",
     "平成11年11月11日には、「1」が ___ つ並びました。（2面）", instr="Completa", size=20.5, gap=10)
c.ex("B2", "da completare", "5,000", "Oltre 5.000 gruppi all'anno visitano il santuario Nishinomiya",
     "西宮神社では、例年 ___ 組以上が七五三参りに来ます。（3面）", instr="Completa", size=20.5, gap=10)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「昨日、友達とポッキーを食べます」", "→ 『昨日』があるので過去形：『ポッキーを食べました』。", "Con 「昨日」, usa il passato."),
    ("「私の趣味は本を読むです」", "→ 『こと』が必要です：『本を読むことです』。", "Aggiungi 「こと」 per fare un nome da un verbo."),
    ("「神社に千歳飴をもらいます」", "→ もらう場所は『で』：『神社で千歳飴をもらいます』。", "Usa 「で」 per il luogo dove ricevi qualcosa."),
    ("「高尾山へ紅葉を見ます」", "→ 見る場所は『で』：『高尾山で紅葉を見ます』。", "Usa 「で」 per il luogo dove guardi."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "まちがい診療所 · Clinica degli errori", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "『見頃を追いかける』 — 見頃（いちばん美しい時）＋追いかける（後を追って行くこと）。北から南へ、紅葉の見頃を追いかけて行く、という意味です。"
wcn = "Analisi: a caccia della stagione migliore."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "今週のフレーム · La struttura", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「こんにちは。私は高校生です。読書週間には、図書館で本を3冊読みました。15日には、妹の七五三で神社へ行きます。」— 読者の手紙の例"
ld_it = "Esempio della redazione, non una vera lettera. Alla scadenza non erano arrivate lettere né composizioni; entrambe appariranno nel VOL.4. Mandateci la vostra lettera in giapponese: le scelte saranno pubblicate nel VOL.4!"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld_it, "sans", False, 20, CW - 44)) * 29 + 26 + 16
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "読者の手紙 · Angolo dei lettori", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, ld_it, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "今週のフレーズ · Frasi della settimana (testuali, da questo numero)", 27, "sans", True, OLIVE)
quotes = [
    ("「読書週間は、9日（月よう日）で終わります。」", "La Settimana della Lettura finisce lunedì 9 novembre.", "pag. 1"),
    ("「15日（日よう日）は、七五三の中心の日です。」", "Domenica 15 novembre è il cuore di Shichi-Go-San.", "pag. 1"),
    ("「『ポッキー＆プリッツの日』は、1999年に始まりました。」", "Il giorno di Pocky e Pretz è iniziato nel 1999.", "pag. 2"),
    ("「千歳飴は、長く生きてほしい、という願いのお菓子です。」", "Chitose-ame è la caramella dell'augurio di lunga vita.", "pag. 2"),
    ("「七五三は、3歳と5歳と7歳の子どものお祝いです。」", "Shichi-Go-San celebra i bambini di 3, 5 e 7 anni.", "pag. 3"),
    ("「ソフトバンクが4連勝で日本一になりました。」", "SoftBank ha preso il titolo del Giappone con quattro vittorie di fila.", "pag. 4"),
    ("「11月11日は、ポッキーの日です。」", "L'11 novembre è il giorno dei Pocky.", "pag. 5"),
    ("「紅葉の見頃は、北から南へ移ります。」", "La stagione migliore delle foglie va da nord a sud.", "pag. 6"),
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
p.text(MX + 28, py + 44, "来週 · Prossimo numero (VOL.4)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "酉の市は19日（木）に二の酉があります。相撲の千秋楽は22日（日）です。紅葉の見頃は、京都へ移ります。読者の手紙と第8版の作文の優秀作も載せます。お楽しみに！", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-kotoba.svg")
print("P7 saved, exercises so far:", len(REG))
