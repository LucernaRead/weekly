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
p.text(975, 92, "ELKE WEEK IN HET NEDERLANDS　每週一期　讀荷蘭人正在讀的荷蘭語", 17, "sans", False, GREY, anchor="middle", spacing=1.7)
p.text(RIGHT, 92, "WEEK VAN 16 TOT EN MET 22 NOVEMBER 2026", 17, "sans", False, GREY, anchor="end", spacing=1.7)
p.text(975, 262, "De Lucerna", 196, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "荷 語 週 報　VOL.4　ORANJE　SINTERKLAAS　PAKJESAVOND", 36, "serif", True, OLIVE, anchor="middle", spacing=8)
p.text(975, 372, "DE WEKELIJKSE KRANT OM NEDERLANDS TE LEREN — HET ECHTE NEDERLAND, IN HET NEDERLANDS", 16, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)

# band
p.rect(MX, 470, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 30, 524, "VANAVOND IN BERLIJN!", 46, "sans", True, ONCLOTH)
p.text(MX + 30, 568, "Oranje speelt maandag tegen Duitsland — de beslissing in groep 2.", 25, "serif", False, "#cac8ba")
p.text(RIGHT - 30, 524, "今晚柏林：荷蘭對德國", 27, "sans", True, GOOSE, anchor="end")
p.text(RIGHT - 30, 568, "本週：橙衣軍團決戰德國　詳見第4版", 18, "sans", False, GOOSE, anchor="end")

# ---- headline (span cols 0-2) ----
hy = 590
p.text(MX, hy + 26, "HET NIEUWS　頭條", 17, "sans", True, OLIVE)
hy = p.para(MX, hy + 92, "Vanavond in Berlijn: Oranje tegen Duitsland", 53, "serif", True, INK, 1323, 1.06)
p.text(MX, hy + 28, "Van de redactie van De Lucerna　Leesniveau: A2", 17, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Op maandag 16 november speelt Oranje in Berlijn tegen Duitsland. De wedstrijd begint om 20:45 uur in het Olympiastadion en is live te zien op NPO 3. Het is de laatste wedstrijd in de groep — en de beslissing in groep 2.")
f.para("Na vier wedstrijden staan Nederland en Griekenland samen bovenaan met 8 punten. Duitsland heeft 5 punten, Servië heeft 0 punten. Nederland staat eerste, omdat het meer doelpunten maakte: 7 tegen 5. De nummers één en twee van de groep gaan naar de kwartfinales in maart 2027.")
f.para("Vrijdag speelden Oranje en Duitsland hun vijfde wedstrijd: Oranje thuis tegen Griekenland, in de Johan Cruijff ArenA in Amsterdam, en Duitsland uit in Belgrado tegen Servië. Maandagavond in Berlijn valt de beslissing: wie wint de groep?")
f.para("Afgelopen weekend kwam Sinterklaas aan in Nederland. Zaterdag 14 november was de landelijke intocht in Grave, aan de Maas in Noord-Brabant: rond 12:00 uur meerde de stoomboot aan bij de Maaskade, live op NPO 3. Een dag later, op zondag 15 november, was de intocht in Amsterdam: de 88e editie.")
f.para("Na de intocht begint de tijd van de schoen: kinderen zetten hun schoen bij de deur, met een wortel voor het paard en een verlanglijstje erin. Pakjesavond, de avond met de grote cadeaus, is dit jaar op zaterdag 5 december — over negentien dagen.")
f.bridge("講解｜de groepswinst 小組第一 · de kwartfinale 八強賽 · de intocht 進城 · het verlanglijstje 願望清單。")
f.box("DE WEEK IN CIJFERS　數字看本週", [
    ("16 — november: Duitsland – Nederland in Berlijn（11 月 16 日：德國–荷蘭在柏林）", "serif", False, INK, 20, 1.35),
    ("20:45 — de aftrap（20:45：柏林奧林匹克體育場開球）", "serif", False, INK, 20, 1.35),
    ("8 — punten: Nederland en Griekenland bovenaan（8 分：荷蘭與希臘並列榜首）", "serif", False, INK, 20, 1.35),
    ("5 — december: pakjesavond, over 19 dagen（12 月 5 日：收禮夜，還有 19 天）", "serif", False, INK, 20, 1.35),
])
f.head("NU JIJ　即學即練", 25)
f.ex("A2", "完成句子", "20:45", "德國–荷蘭週一 20:45 開球",
     "Duitsland – Nederland begint maandag om ___ uur.", size=19.5, gap=6)
f.ex("A2", "完成句子", "Berlijn", "比賽在柏林",
     "Oranje speelt maandag in ___ tegen Duitsland.", size=19.5, gap=6)
f.ex("A2", "完成句子", "8", "荷蘭和希臘都是 8 分",
     "Nederland en Griekenland hebben allebei ___ punten.", size=19.5, gap=6)
f.ex("A2", "完成句子", "15", "阿姆斯特丹進城在 11 月 15 日週日",
     "De intocht in Amsterdam was op zondag ___ november.", size=19.5, gap=6)
f.ex("A2", "完成句子", "5", "收禮夜在 12 月 5 日",
     "Pakjesavond is op zaterdag ___ december.", size=19.5, gap=6)
f.ex("B1", "完成句子", "maakte", "荷蘭進了 7 球",
     "Nederland ___ (maken) 7 doelpunten in vier wedstrijden.", size=19.5, gap=6)
f.end_report()

# ---- deze week agenda (col 3) ----
gx, gw = COLX[3], CW
gy = 588
p.rect(gx, gy, gw, 700, fill=BOX)
p.text(gx + 22, gy + 40, "DEZE WEEK", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "　本週日程", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Agenda van de week　本週大事", 19, "sans", False, GREY)
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
p.text(gx + 22, byy + 76, "本週日程見第2–5版文章", 19, "sans", False, GREY)

# ---- inhoud (col 3) ----
sy = 1312
p.rect(gx, sy, gw, 340, fill="#f0eee5")
p.text(gx + 22, sy + 40, "IN DEZE EDITIE　本期目錄", 24, "sans", True, OLIVE)
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
p.para(gx, wy + 26, "「小組第一」：小組第一，晉級八強賽。", 19, "sans", False, GREY, gw, 1.35)

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
p.text(bx + 22, 1914, "IN HET KORT　快訊", 24, "sans", True, OLIVE)
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
p.text(MX, qy + 36, "BLIKSEMQUIZ　閃電問答", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "讀頭版，選出正確答案　答案見第8版", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2560, tag="P1-quiz")
qf.ex("A2", "單選", "B", "德國–荷蘭週一 20:45 開球",
      "Duitsland – Nederland begint om... A. 18:00 uur · B. 20:45 uur · C. 12:00 uur", size=21)
qf.ex("A2", "單選", "B", "比賽在柏林奧林匹克體育場",
      "Oranje speelt maandag in... A. Amsterdam · B. Berlijn · C. Zeist", size=21)
qf.ex("A2", "單選", "C", "荷蘭和希臘都是 8 分",
      "Nederland en Griekenland hebben... A. 5 punten · B. 7 punten · C. 8 punten", size=21)
qf.ex("A2", "單選", "B", "收禮夜在 12 月 5 日週六",
      "Pakjesavond is op... A. 11 november · B. 5 december · C. 15 november", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-voorpagina.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · LEVEN (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("LEVEN　生活", "De Lucerna", "NIVEAU A2　De schoen en pakjesavond　鞋子與收禮夜")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("De schoen staat klaar: aftellen naar pakjesavond", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: A2")
f.para("Sinterklaas is er! Afgelopen weekend kwam hij aan in Grave en in Amsterdam. Nu begint de tijd van de schoen: kinderen zetten 's avonds hun schoen bij de deur, met een wortel voor het paard en een tekening of een verlanglijstje erin. 's Nachts komt Sinterklaas met een klein cadeautje.")
f.para("De wortel is voor het paard van Sinterklaas, Ozosnel. De tekening is voor Sinterklaas zelf. En het verlanglijstje? Dat is een lijst met wensen: wat wil je het liefst hebben? Schrijf het in het Nederlands — Sinterklaas leest Nederlands.")
f.para("Vorige week woensdag was het Sint-Maarten: kinderen liepen met lampionnen zingend langs de deuren. Nu is het licht van de lampion doorgegeven aan de schoen: twee feesten van licht en geven, in twee weken.")
f.para("Op zaterdag 5 december is het pakjesavond: de avond met de grote cadeaus. Veel families maken dan een surprise: een cadeau in een gekke verpakking, met een gedicht erbij. Een gedicht is een klein versje — grappig, lief of een beetje plagend. Nog negentien dagen tot pakjesavond: tijd om te knutselen en te dichten.")
f.para("En het Sinterklaasjournaal? Dat is er elke dag om 18:00 uur op NPO Zapp. Kinderen volgen hoe Sinterklaas en zijn Pieten zich voorbereiden op pakjesavond.")
f.head("DRIE DINGEN VOOR 5 DECEMBER", 23)  # D5: 25→23 — HEAD TOO WIDE after D5 (core-nl defect, same line)
f.para("Eén: zet je schoen, met een wortel en een verlanglijstje. Twee: schrijf een gedicht — kort is ook goed. Drie: maak een surprise: verstop het cadeau in iets geks.")
f.box("ZO ONTHOUD JE HET　口訣", [
    ("«De schoen staat klaar: een wortel voor het paard, een lijstje voor de Sint.» En pakjesavond is op 5 december.", "serif", False, INK, 21.5, 1.4),
])
f.gloss("de schoen 鞋子 · de wortel 胡蘿蔔 · het verlanglijstje 願望清單 · de surprise 偽裝禮物 · het gedicht 詩。")
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
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("你會放鞋子加願望清單，還是更愛為收禮夜寫首詩？寫兩句荷蘭語寄給編輯部。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "EN JIJ?　說說你自己", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "你會放鞋子加願望清單，還是更愛為收禮夜寫首詩？寫兩句荷蘭語寄給編輯部。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- pakjesavond row: 4 boxes ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, OLIVE, 2)
p.text(MX, dy + 28, "PAKJESAVOND IN VIER WOORDEN　四個關鍵詞", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "Wat hoort bij pakjesavond?　哪些詞屬於收禮夜", 20, "sans", False, GREY, anchor="end")
codes = [
    ("SCHOEN", "de schoen", "晚上放在門口，等聖誕老人來"),
    ("WORTEL", "voor het paard", "胡蘿蔔是給聖誕老人的馬的"),
    ("LIJSTJE", "het verlanglijstje", "願望清單：寫下你最想要的東西"),
    ("GEDICHT", "het versje", "小詩：幽默、溫馨或帶點調侃"),
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
p.text(MX, ey + 28, "OEFENINGEN　第2版練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案見第8版　題目可跨級混排，按題號找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A　BEGRIJPEN", 25)
e.bridge("讀第 2 版文章，選出正確答案。")
e.ex("A2", "單選", "B", "聖誕老人上週末抵達赫拉弗和阿姆斯特丹",
     "Sinterklaas kwam afgelopen weekend aan in... A. Utrecht · B. Grave en Amsterdam · C. Spanje", size=20, gap=8)
e.ex("A2", "單選", "B", "鞋裡放胡蘿蔔是給馬的",
     "De wortel in de schoen is voor... A. Sinterklaas · B. het paard · C. de Piet", size=20, gap=8)
e.ex("A2", "單選", "C", "收禮夜在 12 月 5 日",
     "Pakjesavond is op... A. 11 november · B. 15 november · C. 5 december", size=20, gap=8)
e.ex("A2", "單選", "A", "surprise 是偽裝起來的禮物",
     "Een surprise is... A. een cadeau in een gekke verpakking · B. een liedje · C. een lampion", size=20, gap=8)
e.ex("A2", "單選", "B", "聖誕老人新聞每天 18:00",
     "Het Sinterklaasjournaal is elke dag om... A. 12:00 uur · B. 18:00 uur · C. 20:00 uur", size=20, gap=8)
e.head("B　WOORDEN", 25)
e.bridge("用第 2 版的詞填空。")
e.ex("A2", "完成句子", "schoen", "schoen = 鞋子",
     "Kinderen zetten hun ___ bij de deur.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "wortel", "wortel = 胡蘿蔔",
     "In de schoen zit een ___ voor het paard.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "verlanglijstje", "verlanglijstje = 願望清單",
     "Op het ___ staan drie wensen.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "gedicht", "gedicht = 詩",
     "Bij de surprise hoort een ___.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "5", "收禮夜在 12 月 5 日",
     "Pakjesavond is op ___ december.", instr="填空", size=20, gap=8)
e.head("C　SCHOEN EN GEDICHT", 25)
e.bridge("用第 2 版的數字和名字填空。")
e.ex("A2", "完成句子", "Ozosnel", "聖誕老人的馬叫 Ozosnel",
     "Het paard van Sinterklaas heet ___.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "19", "11 月 16 日到 12 月 5 日是 19 天",
     "Van 16 november tot 5 december: ___ dagen.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "18:00", "聖誕老人新聞 18:00",
     "Het Sinterklaasjournaal is om ___ uur.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "december", "收禮夜在 12 月",
     "Pakjesavond is in ___.", instr="填空", size=20, gap=8)
e.head("D　WOORDEN", 25)
e.match_set("A2", "詞彙配對",
            ["de schoen", "de wortel", "het verlanglijstje", "het gedicht"],
            ["een lijst met wensen voor Sinterklaas",
             "een klein versje bij een cadeau",
             "eten voor Sinterklaas' paard",
             "die staat 's avonds bij de deur"],
            ["d", "c", "a", "b"],
            ["schoen = 鞋子 d", "wortel = 胡蘿蔔 c", "verlanglijstje = 願望清單 a", "gedicht = 詩 b"],
            instr="把詞和釋義配對")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-leven.svg")
print("P2 saved, exercises so far:", len(REG))
