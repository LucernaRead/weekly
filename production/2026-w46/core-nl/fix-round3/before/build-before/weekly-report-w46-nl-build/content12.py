# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-nl-core/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · VOORPAGINA (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 3", 23, "sans", True, OLIVE)
p.text(975, 92, "ELKE WEEK IN HET NEDERLANDS · 每周一期 · 读荷兰人正在读的荷兰语", 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "WEEK VAN 9 TOT EN MET 15 NOVEMBER 2026", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, GOLD, 1.6)
p.text(975, 262, "De Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "荷 兰 语 周 报 · VOL.3 · SINTERKLAAS · SINT-MAARTEN · ORANJE", 40, "serif", True, INK, anchor="middle")
p.text(975, 372, "DE WEKELIJKSE KRANT OM NEDERLANDS TE LEREN — HET ECHTE NEDERLAND, IN HET NEDERLANDS", 19, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)

# band
p.rect(MX, 424, RIGHT - MX, 118, fill=DARK)
p.text(MX + 30, 478, "SINTERKLAAS KOMT ERAAN!", 36, "sans", True, "#f3edda")
p.text(MX + 30, 522, "Eerst het Sinterklaasjournaal, dan de intocht in Grave en in Amsterdam.", 23, "serif", False, "#e8dfc8")
p.text(RIGHT - 30, 478, "圣诞老人来了", 24, "sans", True, "#b3a06a", anchor="end")
p.text(RIGHT - 30, 522, "本周：圣诞老人来到荷兰 · 详见第 3 版", 21, "sans", False, "#b3a06a", anchor="end")

# ---- headline (span cols 0-2) ----
hy = 580
p.text(MX, hy + 26, "HET NIEUWS · 头条", 22, "sans", True, BRICK)
hy = p.para(MX, hy + 92, "Sinterklaas komt eraan: eerst Grave, dan Amsterdam", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 28, "Van de redactie van De Lucerna · Leesniveau: A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Op maandag 9 november begint het Sinterklaasjournaal op televisie. Elke dag om 18:00 uur volgen kinderen op NPO Zapp hoe Sinterklaas en zijn Pieten zich voorbereiden op de reis naar Nederland.")
f.para("Op zaterdag 14 november komt Sinterklaas officieel aan in Nederland. De landelijke intocht is dit jaar in Grave, een vestingstad aan de Maas in Noord-Brabant. Rond 12:00 uur meert de stoomboot aan bij de Maaskade. De intocht is live te zien op NPO 3.")
f.para("Een dag later, op zondag 15 november, is de intocht in Amsterdam: de 88e editie. De boot vertrekt om 10:15 uur bij De Omval en vaart over de Amstel naar het Scheepvaartmuseum. Daar krijgt Sinterklaas de sleutel van de stad. Daarna gaat hij te paard door de stad naar het Leidseplein.")
f.para("Eerder in de week, op woensdag 11 november, is het Sint-Maarten: kinderen gaan met lampionnen zingend langs de deuren (pagina 2). En op vrijdag 13 november speelt Oranje thuis tegen Griekenland (pagina 4).")
f.para("Na de intocht zetten kinderen hun schoen. Sinterklaas komt dan 's nachts met cadeautjes. Pakjesavond is dit jaar op zaterdag 5 december.")
f.bridge("讲解｜de intocht 入城式 · de stoomboot 蒸汽船 · aanmeren 靠岸 · de lampion 灯笼。")
f.box("DE WEEK IN CIJFERS · 数字看本周", [
    ("9 — november: het Sinterklaasjournaal begint（11 月 9 日：圣诞老人新闻开播）", "serif", False, INK, 20, 1.35),
    ("14 — november: de landelijke intocht in Grave（11 月 14 日：全国入城式在赫拉弗）", "serif", False, INK, 20, 1.35),
    ("15 — november: de intocht in Amsterdam, de 88e editie（11 月 15 日：阿姆斯特丹入城式，第 88 届）", "serif", False, INK, 20, 1.35),
    ("20:45 — uur: Oranje tegen Griekenland op vrijdag（20:45：荷兰队周五对阵希腊）", "serif", False, INK, 20, 1.35),
])
f.head("NU JIJ · 即学即练", 25)
f.ex("A2", "完成句子", "9", "圣诞老人新闻 11 月 9 日开播",
     "Het Sinterklaasjournaal begint op maandag ___ november.", size=19.5, gap=6)
f.ex("A2", "完成句子", "Grave", "全国入城式在赫拉弗",
     "De landelijke intocht is dit jaar in ___.", size=19.5, gap=6)
f.ex("A2", "完成句子", "15", "阿姆斯特丹入城式在 11 月 15 日周日",
     "De intocht in Amsterdam is op zondag ___ november.", size=19.5, gap=6)
f.ex("A2", "完成句子", "11", "圣马丁节在 11 月 11 日周三",
     "Sint-Maarten is op woensdag ___ november.", size=19.5, gap=6)
f.ex("A2", "完成句子", "20:45", "荷兰–希腊 20:45 开球",
     "Oranje tegen Griekenland begint vrijdag om ___ uur.", size=19.5, gap=6)
f.ex("B1", "完成句子", "zetten", "veel kinderen → zetten（复数）",
     "Na de intocht ___ (zetten) kinderen hun schoen.", size=19.5, gap=6)
f.end_report()

# ---- deze week agenda (col 3) ----
gx, gw = COLX[3], CW
gy = 580
p.rect(gx, gy, gw, 700, fill=BOX, stroke=LINE, sw=1.4)
p.text(gx + 22, gy + 40, "DEZE WEEK", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "· 本周日程", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Agenda van de week · 本周大事", 19, "sans", False, GREY)
gt = [
    ("MA 9", "Sinterklaasjournaal begint"),
    ("WO 11", "Sint-Maarten, lampionnen"),
    ("VR 13", "Oranje – Griekenland"),
    ("ZA 14", "Intocht in Grave"),
    ("ZO 15", "Intocht Amsterdam"),
]
byy = gy + 150
for i, (lab, vol) in enumerate(gt):
    p.text(gx + 22, byy + 22, lab, 20, "serif", True, BRICK)
    p.text(gx + 110, byy + 22, vol, 20, "serif", False, INK)
    byy += 62
p.text(gx + 22, byy + 16, "Alle data en tijden staan ook", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "in de artikelen op pagina 2–4.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 76, "本周日程见第 2–4 版文章", 19, "sans", False, GREY)

# ---- inhoud (col 3) ----
sy = 1312
p.rect(gx, sy, gw, 340, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(gx + 22, sy + 40, "IN DEZE EDITIE · 本期目录", 24, "sans", True, OLIVE)
som = [
    ("Pag. 2", "Sint-Maarten: licht en delen", "A2"),
    ("Pag. 3", "Sinterklaasjournaal", "A2→B1"),
    ("Pag. 4", "Oranje: beslissende week", "B1"),
    ("Pag. 5", "Robinson en de schoen", "B1"),
    ("Pag. 6", "Sint-Maarten of Halloween?", "B2"),
    ("Pag. 7", "Woorden van de week", "A2→B2"),
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
y2 = p.para(gx, my + 76, "«de intocht»: de feestelijke aankomst van Sinterklaas in een stad, met de boot en daarna te paard.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, y2 + 28, "“入城式”：圣诞老人乘船、随后骑马隆重进入一座城市。", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1853, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "westertoren.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "De Westertoren in Amsterdam. Zondag 15 november vaart Sinterklaas over de Amstel naar het Scheepvaartmuseum en rijdt hij daarna te paard naar het Leidseplein. (Pagina 3)",
        "Foto: Wim van Rossem / Anefo, Nationaal Archief — CC0")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2290, tag="P1-extra")
f2.head("NA DE INTOCHT: DE SCHOEN", 25)
f2.para("Na de intocht mag de schoen: kinderen zetten 's avonds hun schoen bij de deur, met een wortel voor het paard en een tekening voor Sinterklaas. 's Nachts komt Sinterklaas met een cadeautje.", 22.5)
f2.para("Pakjesavond, de avond met de grote cadeaus, is dit jaar op zaterdag 5 december.", 22.5)
f2.end_report()
# col 3 IN HET KORT
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 1914, "IN HET KORT · 快讯", 24, "sans", True, OLIVE)
brefs = [
    ("SINTERKLAAS · P.3", "Maandag Sinterklaasjournaal; zaterdag intocht in Grave."),
    ("SINT-MAARTEN · P.2", "Woensdag: kinderen met lampionnen langs de deuren."),
    ("ORANJE · P.4", "Vrijdag: Nederland – Griekenland, 20:45 uur, Amsterdam."),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, BRICK)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- quiz bliksem ----
qy = 2312
p.hline(MX, RIGHT, qy, GOLD, 2)
p.text(MX, qy + 36, "BLIKSEMQUIZ · 闪电问答", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "读头版，选出正确答案 · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", "单选", "B", "圣诞老人新闻 11 月 9 日周一开播",
      "Het Sinterklaasjournaal begint op... A. zaterdag 14 november · B. maandag 9 november · C. zondag 15 november", size=21)
qf.ex("A2", "单选", "B", "全国入城式在赫拉弗",
      "De landelijke intocht is in... A. Amsterdam · B. Grave · C. Utrecht", size=21)
qf.ex("A2", "单选", "C", "阿姆斯特丹入城式是第 88 届",
      "De intocht in Amsterdam is de... A. 26e editie · B. 30e editie · C. 88e editie", size=21)
qf.ex("A2", "单选", "B", "荷兰–希腊周五 20:45 开球",
      "Oranje – Griekenland begint om... A. 18:00 uur · B. 20:45 uur · C. 12:00 uur", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-voorpagina.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · LEVEN (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("LEVEN · 生活", "De Lucerna", "NIVEAU A2 · Sint-Maarten: lichtjes en liedjes · 圣马丁节：灯笼与歌声")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("Sint-Maarten: lichtjes in het donker", 37)
f.byline("Van de redactie van De Lucerna · Leesniveau: A2")
f.para("Op woensdag 11 november is het Sint-Maarten. Als het donker wordt, gaan kinderen met een lampion langs de deuren. Ze zingen een liedje en krijgen snoep of fruit. Het bekendste liedje begint zo: «Elf november is de dag, dat mijn lichtje branden mag.»")
f.para("Het feest gaat over Sint-Maarten, of Martinus. Volgens de legende sneed hij zijn mantel in tweeën en gaf hij de helft aan een bedelaar in de kou. Daarom is Sint-Maarten het feest van het delen: licht delen, eten delen, aandacht delen.")
f.para("Sint-Maarten wordt niet overal in Nederland even uitbundig gevierd. Sterke gebieden zijn het noorden, de stad Utrecht, Noord-Holland boven het IJ, Noord-Brabant en Limburg. In Utrecht, de stad van Sint-Maarten, staat de viering op de lijst van het immaterieel erfgoed. Daar lopen kinderen 's avonds «lichies lope»: met lampionnen zingend langs de deuren.")
f.para("Wil je meedoen? Maak zelf een lampion van papier en versier hem met vliegerpapier, zodat het licht er mooi doorheen schijnt. Gebruik een ledlampje op batterijen, nooit een kaarsje. En zing een liedje bij elke deur — dan is het feest compleet.")
f.para("Sint-Maarten valt dit jaar midden in de Sinterklaastijd: maandag begon het Sinterklaasjournaal en zaterdag komt Sinterklaas aan in Grave. Twee feesten van licht en geven, in één week.")
f.head("DRIE DINGEN VOOR 11 NOVEMBER", 25)
f.para("Eén: maak een lampion, met een ledlampje erin. Twee: leer een liedje, bijvoorbeeld «Elf november is de dag». Drie: ga zingend langs de deuren — en deel wat je krijgt.")
f.box("ZO ONTHOUD JE HET · 口诀", [
    ("«Sint-Maarten is het feest van het delen: licht, eten en aandacht.» En de lampion gaat aan als het donker wordt.", "serif", False, INK, 21.5, 1.4),
])
f.gloss("de lampion 灯笼 · delen 分享 · de mantel 斗篷、外套 · de bedelaar 乞丐 · het erfgoed 文化遗产 · het ledlampje LED 小灯。")
f.end_report()

# col 3: image + facts + en jij (sequential, measured)
ix = COLX[3]
image(p, "kinderdijk.jpg", ix, 200, CW, 272)
cy3 = caption(p, ix, 472, CW, "Molens bij Kinderdijk. In november wordt het vroeg donker — dan schijnen de lampionnen van Sint-Maarten extra fel.",
              "Foto: Nationaal Archief — CC0")
facts = ["Sint-Maarten: woensdag 11 november, 's avonds met lampionnen langs de deuren.",
         "De legende: Martinus sneed zijn mantel in tweeën voor een bedelaar.",
         "Utrecht is de stad van Sint-Maarten; de viering staat op de erfgoedlijst."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 40
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "WIST JE DAT?", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "En jij? Loop jij op 11 november met een lampion langs de deuren, of kijk je liever naar het Sinterklaasjournaal? Schrijf twee zinnen in het Nederlands en stuur ze naar de redactie: de mooiste komen in VOL.4 (pagina 7, «Brieven van lezers»)."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("11 月 11 日你会提灯笼挨家唱歌，还是爱看圣诞老人新闻？写两句荷兰语寄给编辑部。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "EN JIJ? · 说说你自己", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "11 月 11 日你会提灯笼挨家唱歌，还是爱看圣诞老人新闻？写两句荷兰语寄给编辑部。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- lichtjes row: 4 boxes ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, GOLD, 2)
p.text(MX, dy + 28, "SINT-MAARTEN IN VIER WOORDEN · 四个关键词", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "Wat hoort bij het feest? · 哪些词属于这个节日", 20, "sans", False, GREY, anchor="end")
codes = [
    ("LAMPION", "het lichtje", "纸灯笼，里面放 LED 灯"),
    ("LIEDJE", "het zingen", "挨家挨户唱圣马丁歌"),
    ("DELEN", "het geven", "分享：把斗篷分一半给乞丐"),
    ("UTRECHT", "de stad", "圣马丁的城市，列入遗产名录"),
]
for i, (t, lab, cn) in enumerate(codes):
    bx = COLX[i]
    p.rect(bx, dy + 52, CW, 150, fill=BOX, stroke=LINE, sw=1.4)
    p.text(bx + 22, dy + 110, t, 32, "serif", True, OLIVE)
    lx = bx + 22 + text_w(t, "serif", True, 32) + 14
    lw = bx + CW - 22 - lx
    yy = p.para(lx, dy + 92, lab, 21.5, "serif", False, INK, lw, 1.36)
    p.para(lx, yy + 20, cn, 19, "sans", False, GREY, lw, 1.3)
p.para(MX, dy + 234, "Let op: een lampion met een ledlampje is veilig — een kaarsje in papier is dat niet. Meer over Sint-Maarten en Halloween lees je op pagina 6.", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P2 exercises ----
ey = dy + 282
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "OEFENINGEN · 第 2 版练习", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案见第 8 版 · 题目可跨级混排，按题号找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A · BEGRIJPEN", 25)
e.bridge("读第 2 版文章，选出正确答案。")
e.ex("A2", "单选", "B", "圣马丁节在 11 月 11 日周三",
     "Sint-Maarten is op... A. maandag 9 november · B. woensdag 11 november · C. zaterdag 14 november", size=20, gap=8)
e.ex("A2", "单选", "B", "孩子们提着灯笼挨家唱歌",
     "Kinderen gaan langs de deuren met... A. een boek · B. een lampion · C. een fiets", size=20, gap=8)
e.ex("A2", "单选", "C", "马丁把斗篷分一半给乞丐",
     "Martinus gaf de helft van zijn mantel aan... A. een kind · B. Sinterklaas · C. een bedelaar", size=20, gap=8)
e.ex("A2", "单选", "B", "乌得勒支是圣马丁的城市",
     "De stad van Sint-Maarten is... A. Amsterdam · B. Utrecht · C. Grave", size=20, gap=8)
e.ex("A2", "单选", "B", "灯笼里用 LED 灯，不用蜡烛",
     "In een lampion hoort... A. een kaarsje · B. een ledlampje · C. een lucifer", size=20, gap=8)
e.head("B · WOORDEN", 25)
e.bridge("用第 2 版的词填空。")
e.ex("A2", "完成句子", "11", "圣马丁节在 11 月 11 日",
     "Sint-Maarten is op ___ november.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "lampion", "lampion = 灯笼（de）",
     "Kinderen lopen met een ___ langs de deuren.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "delen", "delen = 分享",
     "Sint-Maarten is het feest van het ___.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "mantel", "mantel = 斗篷（de）",
     "Martinus sneed zijn ___ in tweeën.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "Utrecht", "圣马丁的城市是乌得勒支",
     "De viering in ___ staat op de erfgoedlijst.", instr="填空", size=20, gap=8)
e.head("C · LIEDJE EN LICHT", 25)
e.bridge("用歌词和安全提示填空。")
e.ex("A2", "完成句子", "lichtje", "歌词：我的小灯可以亮了",
     "«Elf november is de dag, dat mijn ___ branden mag.»", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "donker", "天黑时灯笼格外亮",
     "Als het ___ wordt, gaan de kinderen op pad.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "ledlampje", "LED 灯安全",
     "Gebruik een ___ op batterijen, nooit een kaarsje.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "5", "收礼夜在 12 月 5 日",
     "Pakjesavond is op zaterdag ___ december.", instr="填空", size=20, gap=8)
e.head("D · WOORDEN", 25)
e.match_set("A2", "词汇配对",
            ["de lampion", "delen", "de mantel", "het erfgoed"],
            ["licht delen met anderen, eten delen",
             "een papieren lichtje voor 11 november",
             "wat een land bewaart uit het verleden",
             "een lange jas tegen de kou"],
            ["b", "a", "d", "c"],
            ["lampion=灯笼 b", "delen=分享 a", "mantel=斗篷 d", "erfgoed=文化遗产 c"],
            instr="把词和释义配对")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-leven.svg")
print("P2 saved, exercises so far:", len(REG))
