# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-nl-ja/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · VOORPAGINA (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 1 · EERSTE EDITIE", 23, "sans", True, OLIVE)
p.text(975, 92, 'ELKE WEEK IN HET NEDERLANDS · 毎週一号 · オランダ人が読んでいるオランダ語を読む', 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "WEEK VAN 19 TOT EN MET 25 OKTOBER 2026", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, GOLD, 1.6)
p.text(975, 262, "De Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, 'オ ラ ン ダ 語 週 刊 · VOL.1 · DE KLOK GAAT TERUG · HERFSTVAKANTIE · ADE WORDT 30', 40, "serif", True, INK, anchor="middle")
p.text(975, 372, "オランダ語テキスト · 日本語の解説 — 日本語読者のための版", 19.5, "sans", True, BRICK, anchor="middle")
p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)

# band
p.rect(MX, 424, RIGHT - MX, 118, fill=DARK)
p.text(MX + 30, 478, "ZONDAG GAAT DE KLOK TERUG!", 36, "sans", True, "#f3edda")
p.text(MX + 30, 522, "In de nacht van zaterdag op zondag begint de wintertijd: om 03:00 uur gaat de klok één uur achteruit.", 23, "serif", False, "#e8dfc8")
p.text(RIGHT - 30, 478, '日曜、時計を戻す', 24, "sans", True, "#b3a06a", anchor="end")
p.text(RIGHT - 30, 522, '冬時間スタート · 詳しくは2ページ', 21, "sans", False, "#b3a06a", anchor="end")

# ---- headline (span cols 0-2) ----
hy = 580
p.text(MX, hy + 26, 'HET NIEUWS · トップニュース', 22, "sans", True, BRICK)
hy = p.para(MX, hy + 92, "Een volle week: vakantie, design, dance — en een uur extra slaap", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 28, "Van de redactie van De Lucerna · Leesniveau: A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Het is een volle week in Nederland. De regio's Midden en Zuid hebben de hele week herfstvakantie: van zaterdag 17 tot en met zondag 25 oktober. De regio Noord was vorige week vrij; daar begint de school weer op maandag.", size=24)
f.para("En op de laatste vakantiedag gebeurt er iets bijzonders. In de nacht van zaterdag op zondag gaat de klok één uur achteruit: om 03:00 uur wordt het weer 02:00 uur. De wintertijd begint — en iedereen slaapt een uur langer.", size=24)
f.para("Cultuur is er ook genoeg. In Eindhoven is de Dutch Design Week: zo'n 2.500 ontwerpers tonen hun werk. En in Amsterdam danst de stad vijf dagen lang op het Amsterdam Dance Event — dertig jaar oud en groter dan ooit.", size=24)
f.para("Sportliefhebbers kijken naar zondag: PSV tegen Feyenoord om 14:30 uur en Sparta tegen Ajax om 16:45 uur. En wie zondagavond thuis blijft, kijkt misschien televisie — daarover meer op pagina 5.", size=24)
f.para("Dit is de eerste editie van De Lucerna in het Nederlands: elke week het echte Nederland, helder en eerlijk. Veel plezier met lezen!", size=24)
f.expl('解説 — de herfstvakantie 秋休み · achteruit 後ろへ（戻す）· de ontwerper デザイナー。')
f.box('DE WEEK IN CIJFERS · 数字で見る今週', [
    ('9 — de dagen van de Dutch Design Week in Eindhoven（アイントホーフェンのデザインウィークの日数）', "serif", False, INK, 20, 1.35),
    ('25 — de dag in oktober waarop de wintertijd begint（10月に冬時間が始まる日）', "serif", False, INK, 20, 1.35),
    ('30 — de jaren van het Amsterdam Dance Event（アムステルダム・ダンスイベントの年数）', "serif", False, INK, 20, 1.35),
    ('2.500 — de ontwerpers op de Dutch Design Week, ongeveer（概数：デザインウィークのデザイナー）', "serif", False, INK, 20, 1.35),
])
f.head('NU JIJ · さっそく練習', 25)
f.ex("A2", '文の完成', "herfstvakantie", 'herfstvakantie = 秋休み',
     "De regio's Midden en Zuid hebben de hele week ___.", size=19.5, gap=6)
f.ex("A2", '文の完成', "achteruit", 'achteruit = 後ろへ戻す',
     "In de nacht van zaterdag op zondag gaat de klok één uur ___.", size=19.5, gap=6)
f.ex("A2", '文の完成', "03:00", '03:00 → 02:00（冬時間）',
     "Om ___ uur wordt het weer 02:00 uur.", size=19.5, gap=6)
f.ex("A2", '文の完成', "Eindhoven", 'Dutch Design Week はアイントホーフェン',
     "De Dutch Design Week is in ___.", size=19.5, gap=6)
f.ex("A2", '文の完成', "dertig", 'dertig = 30（ADE 30年）',
     "Het Amsterdam Dance Event is dit jaar ___ jaar oud.", size=19.5, gap=6)
f.ex("B1", '文の完成', "slaapt", "slapen：iedereen → slaapt",
     "In de wintertijd ___ (slapen) iedereen een uur langer.", size=19.5, gap=6)
f.end_report()

# ---- topzoekopdrachten (col 3) ----
gx, gw = COLX[3], CW
gy = 580
p.rect(gx, gy, gw, 700, fill=BOX, stroke=LINE, sw=1.4)
p.text(gx + 22, gy + 40, "TOPZOEK-", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "OPDRACHTEN", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, 'オランダ人のGoogle検索 · zoeken op Google', 19, "sans", False, GREY)
gt = [
    ("de hanslers ruzie", "10.000+"),
    ("uitslagen champions league", "1.000+"),
    ("ade", "500+"),
    ("ballon d'or", "200+"),
    ("thuisbezorgd", "100+"),
]
byy = gy + 150
for i, (lab, vol) in enumerate(gt):
    p.text(gx + 22, byy + 22, f"{i+1}. {lab}", 20, "serif", True, INK)
    p.text(gx + gw - 22, byy + 22, vol, 20, "sans", True, BRICK, anchor="end")
    byy += 62
p.text(gx + 22, byy + 16, "Google Trends, dinsdag 20 oktober:", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "een momentopname; de aantallen zijn", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 68, "schattingen, geen exacte tellingen.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 102, '10月20日（火）のGoogleトレンド：推定値', 19, "sans", False, GREY)

# ---- inhoud (col 3) ----
sy = 1312
p.rect(gx, sy, gw, 340, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(gx + 22, sy + 40, 'IN DEZE EDITIE · 今号の内容', 24, "sans", True, OLIVE)
som = [
    ("Pag. 2", "De wintertijd, stap voor stap", "A2"),
    ("Pag. 3", "Design en herfstvakantie", "A2→B1"),
    ("Pag. 4", "Voetbal: Europa en de topper", "B1"),
    ("Pag. 5", "Dance, tv en Robinson", "B1"),
    ("Pag. 6", "Waarom googelt men de klok?", "B2"),
    ("Pag. 7", "Zinnen van de week", "A2→B2"),
    ("Pag. 8", "Oefeningen en antwoorden", "alle"),
]
yy = sy + 84
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, BRICK)
    p.text(gx + 88, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 40

# ---- woord van de week (col 3) ----
my = 1652
p.text(gx, my + 24, "HET WOORD VAN DE WEEK", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, GOLD, 2)
y2 = p.para(gx, my + 76, "«de klok verzetten»: de tijd op je klok veranderen — deze week één uur achteruit.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, y2 + 28, '「時計を動かす」：時計の時刻を変えること。今週は1時間戻す。', 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1853, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "westertoren.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "De Westertoren in Amsterdam. In de nacht van zaterdag op zondag gaat elke klok in Nederland één uur terug: om 03:00 uur wordt het 02:00 uur. (Pagina 2)",
        "Foto: Wim van Rossem / Anefo, Nationaal Archief — CC0")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2290, tag="P1-tv")
f2.head("DE WEEK OP TV", 25)
f2.para("Op televisie was er ruzie bij De Hanslers, de realityserie van SBS6: de zoekopdracht «de hanslers ruzie» was dinsdag de grootste van het land.", 22.5)
f2.para("En wie zondag na de sport nog energie heeft, danst in Amsterdam: het is de laatste avond van ADE. (Pagina's 4 en 5)", 22.5)
f2.end_report()
# col 3 IN HET KORT
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 1914, 'IN HET KORT · 速報', 24, "sans", True, OLIVE)
brefs = [
    ("DE KLOK", "Zondag wordt 03:00 uur weer 02:00 uur. Telefoons doen het zelf; de ovenklok niet. (Pagina 2)"),
    ("DE VAKANTIE", "Midden en Zuid zijn de hele week vrij. Noord gaat maandag weer naar school."),
    ("HET DESIGN", "Dutch Design Week in Eindhoven, tot en met zondag 25 oktober. (Pagina 3)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, BRICK)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- quiz bliksem ----
qy = 2312
p.hline(MX, RIGHT, qy, GOLD, 2)
p.text(MX, qy + 36, 'BLIKSEMQUIZ · クイズ', 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, 'トップ記事を読んで、正しい答えを選ぼう · 答えは8ページ', 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", '選択問題', "B", '冬時間は土曜から日曜の夜に始まる',
      "De wintertijd begint... A. op maandag · B. in de nacht van zaterdag op zondag · C. op vrijdag", size=21)
qf.ex("A2", '選択問題', "B", '時計を1時間戻す',
      "Om 03:00 uur gaat de klok... A. een uur vooruit · B. een uur achteruit · C. twee uur achteruit", size=21)
qf.ex("A2", '選択問題', "C", 'デザインウィークはアイントホーフェン',
      "De Dutch Design Week is in... A. Amsterdam · B. Rotterdam · C. Eindhoven", size=21)
qf.ex("A2", '選択問題', "A", '日曜14:30キックオフ',
      "PSV – Feyenoord begint zondag om... A. 14:30 uur · B. 16:45 uur · C. 20:00 uur", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-voorpagina.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · LEVEN (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band('LEVEN · 暮らし', "De Lucerna", 'NIVEAU A2 · De wintertijd, stap voor stap · 冬時間のしくみを一歩ずつ')

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("De wintertijd: een uur langer slapen", 37)
f.byline("Van de redactie van De Lucerna · Leesniveau: A2")
f.para("Eén keer per jaar krijgt Nederland een cadeau: een uur extra. In de nacht van zaterdag 24 op zondag 25 oktober gaat de klok één uur achteruit. Om 03:00 uur 's nachts wordt het weer 02:00 uur. De zomertijd is voorbij; de wintertijd begint.")
f.para("Hoe onthoud je de richting? Nederlanders gebruiken een ezelsbruggetje: «In het voorjaar gaat de klok vooruit, in het najaar achteruit.» Voorjaar is de lente, najaar is de herfst. Dus nu, in de herfst, gaat de klok terug.")
f.para("Niet alles gaat vanzelf. Je telefoon en je computer veranderen de tijd zelf. Maar de klok in de keuken, de wekker naast je bed en de ovenklok moet je met de hand verzetten. Vergeet ze niet: 's avonds wordt het nu vroeger donker.")
f.para("En de vakantie? De regio's Midden en Zuid hebben de hele week herfstvakantie, van zaterdag 17 tot en met zondag 25 oktober. De regio Noord had vakantie van 10 tot en met 18 oktober; daar begint de school weer op maandag 19 oktober. Let op: de data zijn adviesdata van de Rijksoverheid — scholen mogen een beetje afwijken.")
f.para("Tot slot: de nacht zelf is speciaal. Het uur van 02:00 tot 03:00 komt twee keer voor. Wie om half drie wakker wordt, weet dus niet of het de eerste of de tweede keer half drie is!")
f.para("Wordt het nu vroeger donker? Ja en nee: 's avonds is het eerder donker, maar 's ochtends is het eerder licht. De dag wordt niet korter — het licht schuift alleen een uur.")
f.para("Nederland doet dit niet alleen: in heel Europa gaat de klok in dezelfde nacht achteruit. Wie in het weekend naar Duitsland of Frankrijk reist, hoeft dus niets extra's te doen: overal is het even laat.")
f.head("ETEN BESTELLEN WORDT HELDER", 25)
f.para("Ander nieuws van dinsdag: Thuisbezorgd en Uber Eats stoppen met verborgen kosten. Wie eten bestelt, ziet voortaan vóór het betalen alle extra kosten duidelijk op het scherm. Miljoenen klanten krijgen een kortingsbon als compensatie, schrijven NU.nl en het AD.")
f.box('ZO ONTHOUD JE HET · 覚え方', [
    ("«Voorjaar vooruit, najaar achteruit.» En in de nacht van zaterdag op zondag geldt: één uur langer slapen.", "serif", False, INK, 21.5, 1.4),
])
f.gloss('het ezelsbruggetje 語呂合わせ · verzetten （時計を）動かす · de wekker 目覚まし時計 · de kortingsbon 割引券 · verborgen 隠れた · de ovenklok オーブンの時計。')
f.end_report()

# col 3: image + facts + en jij (sequential, measured)
ix = COLX[3]
image(p, "zakhorloge.jpg", ix, 200, CW, 272)
cy3 = caption(p, ix, 472, CW, "Een oud zakhorloge. Vroeger verzette iedereen de klok met de hand — nu doet de telefoon het meestal zelf.",
              "Foto: photo-nic.co.uk / Wikimedia Commons — CC0")
facts = ["De wintertijd begint op zondag 25 oktober om 03:00 uur; de klok gaat terug naar 02:00 uur.",
         "De herfstvakantie van Midden en Zuid duurt van 17 tot en met 25 oktober.",
         "De data van de schoolvakanties zijn adviesdata: scholen mogen afwijken."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "WIST JE DAT?", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "En jij? Wat doe jij met een uur extra: langer slapen, lezen of sporten? Schrijf twee zinnen in het Nederlands en stuur ze naar de redactie: de mooiste komen in VOL.2 (pagina 7, «Brieven van lezers»)."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap('1時間あまったら何をする？寝る、読書、それともスポーツ。オランダ語で2文書き、編集部へ送ってください。', "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, 'EN JIJ? · あなたの番', 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, '1時間あまったら何をする？寝る、読書、それともスポーツ。オランダ語で2文書き、編集部へ送ってください。', 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- Hoe laat is het? 4 time boxes ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, GOLD, 2)
p.text(MX, dy + 28, 'HOE LAAT IS HET? · 今、何時？', 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, 'De tijd zeggen als een Nederlander · オランダ人らしく時刻を言う', 20, "sans", False, GREY, anchor="end")
times = [
    ("02:15", "kwart over twee", '2時15分'),
    ("02:30", "half drie", '注意：2:30 で、3:30 ではない'),
    ("02:45", "kwart voor drie", '3時の15分前'),
    ("03:00", "drie uur", '冬時間が始まる時刻'),
]
for i, (t, lab, cn) in enumerate(times):
    bx = COLX[i]
    p.rect(bx, dy + 52, CW, 150, fill=BOX, stroke=LINE, sw=1.4)
    p.text(bx + 22, dy + 116, t, 40, "serif", True, OLIVE)
    yy = p.para(bx + 150, dy + 92, lab, 21.5, "serif", False, INK, CW - 172, 1.36)
    p.para(bx + 150, yy + 20, cn, 19, "sans", False, GREY, CW - 172, 1.3)
p.para(MX, dy + 234, "Let op de valkuil: «half drie» is half vóór drie — dus 02:30, niet 03:30. En de nacht van de wintertijd heeft het uur van 02:00 tot 03:00 twee keer!", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P2 exercises ----
ey = dy + 282
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, 'OEFENINGEN · 2 ページの練習', 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, '答えは8ページ · 問題はレベル混合、番号で探してください', 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A · BEGRIJPEN", 25)
e.expl('2ページの記事を読んで、正しい答えを選んでください。')
e.ex("A2", '選択問題', "B", '覚え方：najaar achteruit（秋は戻す）',
     "De klok gaat achteruit in... A. het voorjaar · B. het najaar · C. de zomer", size=20, gap=8)
e.ex("A2", '選択問題', "B", "03:00 → 02:00",
     "Om 03:00 uur wordt het... A. 04:00 uur · B. 02:00 uur · C. 03:30 uur", size=20, gap=8)
e.ex("A2", '選択問題', "C", 'オーブンの時計は手で直す',
     "Welke klok verandert NIET vanzelf? A. de telefoon · B. de computer · C. de ovenklok", size=20, gap=8)
e.ex("A2", '選択問題', "B", '北部地域は月曜から学校再開',
     "De regio Noord... A. heeft deze week vakantie · B. gaat maandag weer naar school · C. heeft vakantie tot 25 oktober", size=20, gap=8)
e.ex("A2", '選択問題', "B", '2社は隠れた費用をやめる',
     "Thuisbezorgd en Uber Eats... A. worden duurder · B. stoppen met verborgen kosten · C. stoppen met bezorgen", size=20, gap=8)
e.head("B · HOE LAAT?", 25)
e.expl('時刻をオランダ語で書いてください。')
e.ex("A2", '文の完成', "kwart over twee", "kwart over twee = 2:15",
     "02:15 is ___.", instr='空所補充', size=20, gap=8)
e.ex("A2", '文の完成', "half drie", 'half drie = 2:30（ひっかけ！）',
     "02:30 is ___.", instr='空所補充', size=20, gap=8)
e.ex("A2", '文の完成', "kwart voor drie", "kwart voor drie = 2:45",
     "02:45 is ___.", instr='空所補充', size=20, gap=8)
e.ex("A2", '文の完成', "drie uur", "午前3時（drie uur 's nachts）",
     "De wintertijd begint om ___ 's nachts.", instr='空所補充', size=20, gap=8)
e.ex("B1", '文の完成', "achteruit", 'achteruit = 後ろへ（戻す）',
     "Om 03:00 uur gaat de klok één uur ___.", instr='空所補充', size=20, gap=8)
e.head("C · CIJFERS EN DATUMS", 25)
e.expl('1、2ページの数字を使って空欄を埋めてください。')
e.ex("A2", '文の完成', "25", '10月25日の日曜日',
     "De wintertijd begint op zondag ___ oktober.", instr='空所補充', size=20, gap=8)
e.ex("A2", '文の完成', "17", '10月17日の土曜日に開始',
     "De herfstvakantie van Midden en Zuid begint op zaterdag ___ oktober.", instr='空所補充', size=20, gap=8)
e.ex("B1", '文の完成', "9", '17日から25日まで9日間',
     "De herfstvakantie van Midden en Zuid duurt ___ dagen (17 tot en met 25 oktober).", instr='空所補充', size=20, gap=8)
e.ex("B1", '文の完成', "2.500", '約2.500人のデザイナー（1ページ）',
     "Op de Dutch Design Week zijn ongeveer ___ ontwerpers.", instr='空所補充', size=20, gap=8)
e.head("D · WOORDEN", 25)
e.match_set("A2", '単語のペア',
            ["de klok verzetten", "het ezelsbruggetje", "de kortingsbon", "verborgen"],
            ["een zinnetje dat helpt om iets te onthouden",
             "de tijd op een klok veranderen",
             "niet zichtbaar, verstopt",
             "een bon voor korting bij een bestelling"],
            ["b", "a", "d", "c"],
            ['verzetten=時計を動かす b', 'ezelsbruggetje=語呂合わせ a', 'kortingsbon=割引券 d', 'verborgen=隠れた c'],
            instr='語と意味を結ぶ')
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-leven.svg")
print("P2 saved, exercises so far:", len(REG))
