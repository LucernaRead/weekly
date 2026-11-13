# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · VOORPAGINA (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL.4", 17, "sans", True, OLIVE, spacing=1.7)
p.text(975, 92, "ELKE WEEK IN HET NEDERLANDS　每周一期　读荷兰人正在读的荷兰语", 17, "sans", False, GREY, anchor="middle", spacing=1.7)
p.text(RIGHT, 92, "WEEK VAN 16 TOT EN MET 22 NOVEMBER 2026", 17, "sans", False, GREY, anchor="end", spacing=1.7)
p.text(975, 262, "De Lucerna", 196, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "荷兰语周报　VOL.4　ORANJE　SINTERKLAAS　PAKJESAVOND", 36, "serif", True, OLIVE, anchor="middle", spacing=8)
p.text(975, 372, "DE WEKELIJKSE KRANT OM NEDERLANDS TE LEREN — HET ECHTE NEDERLAND, IN HET NEDERLANDS", 16, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)

# band
p.rect(MX, 470, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 30, 524, "VANAVOND IN BERLIJN!", 46, "sans", True, ONCLOTH)
p.text(MX + 30, 568, "Oranje speelt maandag tegen Duitsland — de beslissing in groep 2.", 25, "serif", False, "#cac8ba")
p.text(RIGHT - 30, 524, "今晚柏林：荷兰对德国", 27, "sans", True, GOOSE, anchor="end")
p.text(RIGHT - 30, 568, "本周：橙衣军团决战德国　详见第4版", 18, "sans", False, GOOSE, anchor="end")

# ---- headline (span cols 0-2) ----
hy = 590
p.text(MX, hy + 26, "HET NIEUWS　头条", 17, "sans", True, OLIVE)
hy = p.para(MX, hy + 92, "Vanavond in Berlijn: Oranje tegen Duitsland", 53, "serif", True, INK, 1323, 1.06)
p.text(MX, hy + 28, "Van de redactie van De Lucerna　Leesniveau: A2", 17, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Op maandag 16 november speelt Oranje in Berlijn tegen Duitsland. De wedstrijd begint om 20:45 uur in het Olympiastadion en is live te zien op NPO 3. Het is de laatste wedstrijd in de groep — en de beslissing in groep 2.")
f.para("Na vier wedstrijden staan Nederland en Griekenland samen bovenaan met 8 punten. Duitsland heeft 5 punten, Servië heeft 0 punten. Nederland staat eerste, omdat het meer doelpunten maakte: 7 tegen 5. De nummers één en twee van de groep gaan naar de kwartfinales in maart 2027.")
f.para("Vrijdag speelden Oranje en Duitsland hun vijfde wedstrijd: Oranje thuis tegen Griekenland, in de Johan Cruijff ArenA in Amsterdam, en Duitsland uit in Belgrado tegen Servië. Maandagavond in Berlijn valt de beslissing: wie wint de groep?")
f.para("Afgelopen weekend kwam Sinterklaas aan in Nederland. Zaterdag 14 november was de landelijke intocht in Grave, aan de Maas in Noord-Brabant: rond 12:00 uur meerde de stoomboot aan bij de Maaskade, live op NPO 3. Een dag later, op zondag 15 november, was de intocht in Amsterdam: de 88e editie.")
f.para("Na de intocht begint de tijd van de schoen: kinderen zetten hun schoen bij de deur, met een wortel voor het paard en een verlanglijstje erin. Pakjesavond, de avond met de grote cadeaus, is dit jaar op zaterdag 5 december — over negentien dagen.")
f.bridge("讲解｜de groepswinst 小组头名 · de kwartfinale 四分之一决赛 · de intocht 入城式 · het verlanglijstje 愿望单。")
f.box("DE WEEK IN CIJFERS　数字看本周", [
    ("16 — november: Duitsland – Nederland in Berlijn（11 月 16 日：德国–荷兰在柏林）", "serif", False, INK, 20, 1.35),
    ("20:45 — de aftrap（20:45：柏林奥林匹克体育场开球）", "serif", False, INK, 20, 1.35),
    ("8 — punten: Nederland en Griekenland bovenaan（8 分：荷兰与希腊并列榜首）", "serif", False, INK, 20, 1.35),
    ("5 — december: pakjesavond, over 19 dagen（12 月 5 日：收礼夜，还有 19 天）", "serif", False, INK, 20, 1.35),
])
f.head("NU JIJ　即学即练", 25)
f.ex("A2", "完成句子", "20:45", "德国–荷兰周一 20:45 开球",
     "Duitsland – Nederland begint maandag om ___ uur.", size=19.5, gap=6)
f.ex("A2", "完成句子", "Berlijn", "比赛在柏林",
     "Oranje speelt maandag in ___ tegen Duitsland.", size=19.5, gap=6)
f.ex("A2", "完成句子", "8", "荷兰与希腊同积 8 分",
     "Nederland en Griekenland hebben allebei ___ punten.", size=19.5, gap=6)
f.ex("A2", "完成句子", "15", "阿姆斯特丹入城式在 11 月 15 日周日",
     "De intocht in Amsterdam was op zondag ___ november.", size=19.5, gap=6)
f.ex("A2", "完成句子", "5", "收礼夜在 12 月 5 日",
     "Pakjesavond is op zaterdag ___ december.", size=19.5, gap=6)
f.ex("B1", "完成句子", "maakte", "Nederland maakte 7 球",
     "Nederland ___ (maken) 7 doelpunten in vier wedstrijden.", size=19.5, gap=6)
f.end_report()

# ---- deze week agenda (col 3) ----
gx, gw = COLX[3], CW
gy = 588
p.rect(gx, gy, gw, 700, fill=BOX)
p.text(gx + 22, gy + 40, "DEZE WEEK", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "　本周日程", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Agenda van de week　本周大事", 19, "sans", False, GREY)
gt = [
    ("MA 16", "Oranje – Duitsland, 20:45"),
    ("ZA 21", "Eredivisie: NEC – PSV"),
    ("ZA 21", "Feyenoord – Excelsior"),
    ("ZO 22", "Ajax – ADO Den Haag"),
    ("ZO 22", "Robinson, 20:00 uur"),
]
byy = gy + 150
for i, (lab, vol) in enumerate(gt):
    p.text(gx + 22, byy + 22, lab, 20, "serif", True, OLIVE)
    p.text(gx + 110, byy + 22, vol, 20, "serif", False, INK)
    byy += 62
p.text(gx + 22, byy + 16, "Alle data en tijden staan ook", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "in de artikelen op pagina 2–5.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 76, "本周日程见第2–5版文章", 19, "sans", False, GREY)

# ---- inhoud (col 3) ----
sy = 1312
p.rect(gx, sy, gw, 340, fill="#f0eee5")
p.text(gx + 22, sy + 40, "IN DEZE EDITIE　本期目录", 24, "sans", True, OLIVE)
som = [
    ("Pag. 2", "De schoen en pakjesavond", "A2"),
    ("Pag. 3", "Sinterklaas is er!", "A2→B1"),
    ("Pag. 4", "Oranje: de beslissing", "B1"),
    ("Pag. 5", "Robinson en surprises", "B1"),
    ("Pag. 6", "Oud feest, nieuwe wensen", "B2"),
    ("Pag. 7", "Drie gereedschappen", "A2→B2"),
    ("Pag. 8", "Oefeningen en antwoorden", "alle"),
]
yy = sy + 84
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, OLIVE)
    p.text(gx + 88, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 40

# ---- woord van de week (col 3) ----
my = 1652
p.text(gx, my + 24, "HET WOORD VAN DE WEEK", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, OLIVE, 2)
p.text(gx, my + 76, "«de groepswinst»", 21.5, "serif", False, INK, italic=True)
wy = p.para(gx, my + 108, "de eerste plaats in de groep: als nummer één naar de kwartfinales.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, wy + 26, "“小组头名”：小组第一，晋级四分之一决赛。", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1853, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "westertoren.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "De Westertoren in Amsterdam. Zondag 15 november voer Sinterklaas over de Amstel naar het Scheepvaartmuseum en reed hij daarna te paard naar het Leidseplein. (Pagina 3)",
        "Foto: Wim van Rossem / Anefo, Nationaal Archief — CC0")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2300, tag="P1-extra")
f2.head("NA DE INTOCHT: DE SCHOEN", 25)
f2.para("Na de intocht mag de schoen: kinderen zetten 's avonds hun schoen bij de deur, met een wortel voor het paard en een verlanglijstje erin. 's Nachts komt Sinterklaas met een klein cadeautje.", 22.5)
f2.para("Pakjesavond, de avond met de grote cadeaus — en met surprises en gedichten — is dit jaar op zaterdag 5 december.", 22.5)
f2.end_report()
# col 3 IN HET KORT
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX)
p.text(bx + 22, 1914, "IN HET KORT　快讯", 24, "sans", True, OLIVE)
brefs = [
    ("ORANJE · P.4", "Maandag in Berlijn tegen Duitsland, 20:45 uur, NPO 3."),
    ("SINTERKLAAS · P.3", "Zaterdag intocht in Grave; zondag de 88e intocht in Amsterdam."),
    ("EREDIVISIE · P.4", "Zaterdag 21 november: NEC – PSV en Feyenoord – Excelsior."),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, OLIVE)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- quiz bliksem ----
qy = 2312
p.hline(MX, RIGHT, qy, OLIVE, 2)
p.text(MX, qy + 36, "BLIKSEMQUIZ　闪电问答", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "读头版，选出正确答案　答案见第8版", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2560, tag="P1-quiz")
qf.ex("A2", "单选", "B", "德国–荷兰周一 20:45 开球",
      "Duitsland – Nederland begint om... A. 18:00 uur · B. 20:45 uur · C. 12:00 uur", size=21)
qf.ex("A2", "单选", "B", "比赛在柏林奥林匹克体育场",
      "Oranje speelt maandag in... A. Amsterdam · B. Berlijn · C. Zeist", size=21)
qf.ex("A2", "单选", "C", "荷兰与希腊同积 8 分",
      "Nederland en Griekenland hebben... A. 5 punten · B. 7 punten · C. 8 punten", size=21)
qf.ex("A2", "单选", "B", "收礼夜在 12 月 5 日周六",
      "Pakjesavond is op... A. 11 november · B. 5 december · C. 15 november", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-voorpagina.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · LEVEN (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("LEVEN　生活", "De Lucerna", "NIVEAU A2　De schoen en pakjesavond　鞋子与收礼夜")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("De schoen staat klaar: aftellen naar pakjesavond", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: A2")
f.para("Sinterklaas is er! Afgelopen weekend kwam hij aan in Grave en in Amsterdam. Nu begint de tijd van de schoen: kinderen zetten 's avonds hun schoen bij de deur, met een wortel voor het paard en een tekening of een verlanglijstje erin. 's Nachts komt Sinterklaas met een klein cadeautje.")
f.para("De wortel is voor het paard van Sinterklaas, Ozosnel. De tekening is voor Sinterklaas zelf. En het verlanglijstje? Dat is een lijst met wensen: wat wil je het liefst hebben? Schrijf het in het Nederlands — Sinterklaas leest Nederlands.")
f.para("Vorige week woensdag was het Sint-Maarten: kinderen liepen met lampionnen zingend langs de deuren. Nu is het licht van de lampion doorgegeven aan de schoen: twee feesten van licht en geven, in twee weken.")
f.para("Op zaterdag 5 december is het pakjesavond: de avond met de grote cadeaus. Veel families maken dan een surprise: een cadeau in een gekke verpakking, met een gedicht erbij. Een gedicht is een klein versje — grappig, lief of een beetje plagend. Nog negentien dagen tot pakjesavond: tijd om te knutselen en te dichten.")
f.para("En het Sinterklaasjournaal? Dat is er elke dag om 18:00 uur op NPO Zapp. Kinderen volgen hoe Sinterklaas en zijn Pieten zich voorbereiden op pakjesavond.")
f.head("DRIE DINGEN VOOR 5 DECEMBER", 23)  # D5: 25pt -> 23pt — Newsreader SemiBold advance 451.8px > col 422.5 (HEAD TOO WIDE); 23pt = 415.6px. Text unchanged.
f.para("Eén: zet je schoen, met een wortel en een verlanglijstje. Twee: schrijf een gedicht — kort is ook goed. Drie: maak een surprise: verstop het cadeau in iets geks.")
f.box("ZO ONTHOUD JE HET　口诀", [
    ("«De schoen staat klaar: een wortel voor het paard, een lijstje voor de Sint.» En pakjesavond is op 5 december.", "serif", False, INK, 21.5, 1.4),
])
f.gloss("de schoen 鞋子 · de wortel 胡萝卜 · het verlanglijstje 愿望单 · de surprise 伪装礼物 · het gedicht 诗。")
f.end_report()

# col 3: image + facts + en jij (sequential, measured)
ix = COLX[3]
image(p, "sint-oud.jpg", ix, 200, CW, 272)
cy3 = caption(p, ix, 472, CW, "Sinterklaas te paard in Amsterdam (oude foto uit het archief). Zondag 15 november reed hij na de intocht te paard door de stad naar het Leidseplein.",
              "Foto: Anefo, Nationaal Archief — CC0")
facts = ["Pakjesavond: zaterdag 5 december, over negentien dagen.",
         "De schoen: 's avonds bij de deur, met een wortel en een verlanglijstje.",
         "Een surprise is een cadeau in een gekke verpakking, met een gedicht erbij."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 40
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "WIST JE DAT?", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "En jij? Zet jij je schoen met een wortel en een verlanglijstje, of schrijf je liever een gedicht voor pakjesavond? Schrijf twee zinnen in het Nederlands en stuur ze naar de redactie: de mooiste komen in VOL.5 (pagina 7, «Brieven van lezers»)."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("你会放鞋子加愿望单，还是更爱为收礼夜写首诗？写两句荷兰语寄给编辑部。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "EN JIJ?　说说你自己", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "你会放鞋子加愿望单，还是更爱为收礼夜写首诗？写两句荷兰语寄给编辑部。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- pakjesavond row: 4 boxes ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, OLIVE, 2)
p.text(MX, dy + 28, "PAKJESAVOND IN VIER WOORDEN　四个关键词", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "Wat hoort bij pakjesavond?　哪些词属于收礼夜", 20, "sans", False, GREY, anchor="end")
codes = [
    ("SCHOEN", "de schoen", "晚上放在门口，等圣诞老人来"),
    ("WORTEL", "voor het paard", "胡萝卜是给圣诞老人的马的"),
    ("LIJSTJE", "het verlanglijstje", "愿望单：写下你最想要的东西"),
    ("GEDICHT", "het versje", "小诗：幽默、温馨或带点调侃"),
]
for i, (t, lab, cn) in enumerate(codes):
    bx = COLX[i]
    p.rect(bx, dy + 52, CW, 150, fill=BOX)
    p.text(bx + 22, dy + 110, t, 32, "serif", True, OLIVE)
    lx = bx + 22 + text_w(t, "serif", True, 32) + 14
    lw = bx + CW - 22 - lx
    yy = p.para(lx, dy + 92, lab, 21.5, "serif", False, INK, lw, 1.36)
    p.para(lx, yy + 20, cn, 19, "sans", False, GREY, lw, 1.3)
p.para(MX, dy + 234, "Let op: schrijf je gedicht in het Nederlands — Sinterklaas leest Nederlands. Meer over de intocht lees je op pagina 3.", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P2 exercises ----
ey = dy + 282
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "OEFENINGEN　第2版练习", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案见第8版　题目可跨级混排，按题号找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A　BEGRIJPEN", 25)
e.bridge("读第 2 版文章，选出正确答案。")
e.ex("A2", "单选", "B", "圣诞老人上周末抵达赫拉弗和阿姆斯特丹",
     "Sinterklaas kwam afgelopen weekend aan in... A. Utrecht · B. Grave en Amsterdam · C. Spanje", size=20, gap=8)
e.ex("A2", "单选", "B", "鞋里放胡萝卜是给马的",
     "De wortel in de schoen is voor... A. Sinterklaas · B. het paard · C. de Piet", size=20, gap=8)
e.ex("A2", "单选", "C", "收礼夜在 12 月 5 日",
     "Pakjesavond is op... A. 11 november · B. 15 november · C. 5 december", size=20, gap=8)
e.ex("A2", "单选", "A", "surprise 是伪装起来的礼物",
     "Een surprise is... A. een cadeau in een gekke verpakking · B. een liedje · C. een lampion", size=20, gap=8)
e.ex("A2", "单选", "B", "圣诞老人新闻每天 18:00",
     "Het Sinterklaasjournaal is elke dag om... A. 12:00 uur · B. 18:00 uur · C. 20:00 uur", size=20, gap=8)
e.head("B　WOORDEN", 25)
e.bridge("用第 2 版的词填空。")
e.ex("A2", "完成句子", "schoen", "schoen = 鞋子",
     "Kinderen zetten hun ___ bij de deur.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "wortel", "wortel = 胡萝卜",
     "In de schoen zit een ___ voor het paard.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "verlanglijstje", "verlanglijstje = 愿望单",
     "Op het ___ staan drie wensen.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "gedicht", "gedicht = 诗",
     "Bij de surprise hoort een ___.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "5", "收礼夜在 12 月 5 日",
     "Pakjesavond is op ___ december.", instr="填空", size=20, gap=8)
e.head("C　SCHOEN EN GEDICHT", 25)
e.bridge("用第 2 版的数字和名字填空。")
e.ex("A2", "完成句子", "Ozosnel", "圣诞老人的马叫 Ozosnel",
     "Het paard van Sinterklaas heet ___.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "19", "11 月 16 日到 12 月 5 日是 19 天",
     "Van 16 november tot 5 december: ___ dagen.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "18:00", "圣诞老人新闻 18:00",
     "Het Sinterklaasjournaal is om ___ uur.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "december", "收礼夜在 12 月",
     "Pakjesavond is in ___.", instr="填空", size=20, gap=8)
e.head("D　WOORDEN", 25)
e.match_set("A2", "词汇配对",
            ["de schoen", "de wortel", "het verlanglijstje", "het gedicht"],
            ["een lijst met wensen voor Sinterklaas",
             "een klein versje bij een cadeau",
             "eten voor Sinterklaas' paard",
             "die staat 's avonds bij de deur"],
            ["d", "c", "a", "b"],
            ["schoen=鞋子 d", "wortel=胡萝卜 c", "verlanglijstje=愿望单 a", "gedicht=诗 b"],
            instr="把词和释义配对")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-leven.svg")
print("P2 saved, exercises so far:", len(REG))
