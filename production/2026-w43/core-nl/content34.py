# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTUUR (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTUUR　文化", "De Lucerna", "NIVEAU A2 → B1　Dutch Design Week en de herfstvakantie　设计周与秋假")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P3-feature")
f.title("Ontwerpen in Eindhoven: de Dutch Design Week", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: A2 → B1")
f.para("Negen dagen lang is Eindhoven de designhoofdstad van Nederland. De Dutch Design Week duurt van zaterdag 17 tot en met zondag 25 oktober. Het is de 26e editie, met als thema «R.A.W.». Ongeveer 2.500 ontwerpers laten hun werk zien: meubels, kleding, websites en dingen die nog geen naam hebben.")
f.para("Waar gaat het over? De ontwerpers werken met materialen: oud plastic wordt een stoel, en planten worden materiaal voor huizen. Dat werken met de natuur heet biodesign. Ook kunstmatige intelligentie (AI) helpt mee aan nieuwe vormen.")
f.para("Een normaal kaartje kost € 32,50; studenten betalen € 19,50. Wie jong is en van maken houdt, is hier op de goede plek: je mag veel dingen aanraken en vragen stellen aan de makers.")
f.head("EROPUIT IN DE HERFSTVAKANTIE", 25)
f.para("Geen school, wel musea: in de herfstvakantie organiseren musea extra activiteiten voor families. Het Limburgs Museum in Venlo heeft van 17 tot en met 25 oktober een speciaal vakantieprogramma, met een gratis familiedag op zaterdag 24 oktober.")
f.para("Let op: niet heel Nederland is vrij. De regio Noord had vorige week vakantie, van 10 tot en met 18 oktober; daar zitten de kinderen deze week weer gewoon in de klas. Alleen Midden en Zuid hebben nu herfstvakantie.")
f.para("Buiten is het ook mooi: het bos is geel en rood, en overal liggen kastanjes en eikels op de grond. Een wandeling in het herfstbos is het goedkoopste uitje van de week.")
f.gloss("de ontwerper 设计师 · het materiaal 材料 · aanraken 触摸 · de kastanje 栗子 · eropuit 出门游玩。")
f.end_report()

# col 3: two images + facts box (sequential, measured)
ix = COLX[3]
image(p, "kinderdijk.jpg", ix, 200, CW, 250)
cy3 = caption(p, ix, 450, CW, "De molens van Kinderdijk: een klassiek uitje in de herfstvakantie. Veel families gaan deze week eropuit.",
              "Foto: Nationaal Archief / Wikimedia Commons — CC0")
image(p, "herfstbos.jpg", ix, cy3 + 22, CW, 236)
cy3b = caption(p, ix, cy3 + 22 + 236, CW, "Het herfstbos: geel en rood, met kastanjes op de grond.",
               "Foto: Vovogov90 / Wikimedia Commons — CC0")
facts = ["26e editie van de Dutch Design Week, thema «R.A.W.»",
         "Ongeveer 2.500 ontwerpers in Eindhoven.",
         "Kaartjes: € 32,50; studenten € 19,50."]
sy3 = cy3b + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "DDW IN CIJFERS", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P3 col3 ends", sy3 + sh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "OEFENINGEN　第3版练习", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案见第8版　题目可跨级混排，按题号找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A　BEGRIJPEN", 25)
e.bridge("读第 3 版文章，选出正确答案。")
e.ex("A2", "单选", "B", "设计周在埃因霍温",
     "De Dutch Design Week is in... A. Amsterdam · B. Eindhoven · C. Venlo", size=20, gap=8)
e.ex("A2", "单选", "B", "17–25 日共 9 天",
     "De Design Week duurt... A. vijf dagen · B. negen dagen · C. twee weken", size=20, gap=8)
e.ex("A2", "单选", "A", "主题是《R.A.W.》",
     "Het thema van dit jaar is... A. «R.A.W.» · B. «Natuur» · C. «30 jaar»", size=20, gap=8)
e.ex("B1", "单选", "B", "biodesign 用植物等自然材料",
     "Biodesign werkt met... A. alleen oude meubels · B. planten en materialen uit de natuur · C. alleen websites", size=20, gap=8)
e.ex("B1", "单选", "A", "免费家庭日在周六 10 月 24 日",
     "De gratis familiedag in Venlo is op... A. zaterdag 24 oktober · B. zondag 25 oktober · C. maandag 19 oktober", size=20, gap=8)
e.head("B　WOORDEN UIT DE TEKST", 25)
e.bridge("用方框里的词填空。注意：有的词要变成复数。")
e.para("ontwerper · materiaal · thema · aanraken · kastanjes · eropuit", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "完成句子", "ontwerpers", "ontwerper 复数：ontwerpers",
     "Ongeveer 2.500 ___ laten hun werk zien in Eindhoven.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "thema", "thema = 主题（het）",
     "Het ___ van de Design Week is «R.A.W.».", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "materiaal", "materiaal = 材料",
     "Planten worden ___ voor nieuwe huizen.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "aanraken", "aanraken = 触摸",
     "Op de Design Week mag je veel dingen ___.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "kastanjes", "kastanjes = 栗子",
     "In het bos liggen ___ en eikels op de grond.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "eropuit", "eropuit = 出门游玩",
     "In de vakantie gaan families ___: naar een museum of het bos.", instr="填空", size=20, gap=8)
e.head("C　HET PERFECTUM", 25)
e.bridge("用现在完成时补全，注意助动词 hebben/zijn。")
e.ex("B1", "完成句子", "heeft gemaakt", "maken 用 hebben：heeft gemaakt",
     "De ontwerper ___ (maken) een stoel van oud plastic.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "zijn gegaan", "gaan 用 zijn：zijn gegaan",
     "Wij ___ (gaan) naar het museum in Venlo.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "heeft gezien", "zien 不规则：heeft gezien",
     "Zij ___ (zien) het werk van 2.500 ontwerpers.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "zijn gekomen", "komen 用 zijn：zijn gekomen",
     "Veel families ___ (komen) naar Eindhoven.", instr="填空", size=20, gap=8)
e.head("D　REKENEN", 25)
e.bridge("算一算：用第 3 版的数字回答。")
e.ex("B1", "完成句子", "9", "17 日到 25 日共 9 天",
     "De Design Week duurt van 17 tot en met 25 oktober: ___ dagen.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "24", "免费家庭日在 10 月 24 日",
     "De gratis familiedag in het Limburgs Museum is op zaterdag ___ oktober.", instr="填空", size=20, gap=8)
e.ex("B2", "完成句子", "71,50", "19,50 + 19,50 + 32,50 = 71,50",
     "Twee studenten en één volwassene kopen een kaartje. Samen betalen zij € ___.", instr="填空", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultuur.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT　体育", "De Lucerna", "NIVEAU B1　Europese week en de topper van zondag　欧战周与周日焦点战")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P4-feature")
f.title("Europese week: PSV wint in Porto, zondag de topper", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: B1")
f.para("Wat een week voor het Nederlandse voetbal. Zes clubs spelen in Europa. PSV won dinsdag met 1–0 bij FC Porto in de Champions League: een kleine uitslag, maar drie grote punten.")
f.para("Op woensdag speelt Feyenoord in Sevilla tegen Real Betis. Op donderdag komen Ajax (thuis tegen Atalanta), AZ, NEC en FC Twente in actie. De uitslagen van woensdag en donderdag lees je volgende week: deze krant was toen al gedrukt.")
f.para("En dan zondag: de topper. PSV speelt thuis tegen Feyenoord, om 14:30 uur. Later op de middag speelt Sparta tegen Ajax, om 16:45 uur. Het is speelronde 10 van de Eredivisie — en de laatste dag van de herfstvakantie voor Midden en Zuid.")
f.para("Ook op Google is de Europese week groot: de zoekopdracht «uitslagen champions league» haalde dinsdag meer dan 1.000 zoekopdrachten in Nederland. Iedereen wil de uitslagen van alle clubs tegelijk zien.")
f.head("DE BALLON D'OR", 25)
f.para("Op internet praat iedereen over de Ballon d'Or: wie is de beste speler van het jaar? De namen van Yamal, Mbappé en Kane komen vaak voorbij. Maar er is nog geen winnaar: het is speculatie, geen nieuws. Wie is jouw favoriet?")
f.gloss("de uitslag 比分 · winnen 赢 · in actie komen 上场、出战 · de speelronde 轮次 · de winnaar 获胜者。")
f.end_report()

# col 3: image + programme box (sequential, measured)
ix = COLX[3]
image(p, "elftal1912.jpg", ix, 200, CW, 250)
cy3 = caption(p, ix, 450, CW, "Het Nederlands elftal in 1912. Voetbal is al meer dan honderd jaar de sport van Nederland.",
              "Foto: Spaarnestad Photo / Wikimedia Commons — publiek domein")
facts = ["Dinsdag 20 oktober: FC Porto – PSV 0–1 (Champions League).",
         "Woensdag 21 oktober: Real Betis – Feyenoord (in Sevilla).",
         "Donderdag 22 oktober: Ajax – Atalanta; ook AZ, NEC en FC Twente spelen.",
         "Zondag 25 oktober: PSV – Feyenoord (14:30) en Sparta – Ajax (16:45)."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32 + 30
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "HET PROGRAMMA", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P4 col3 ends", sy3 + sh)

# ---- P4 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "OEFENINGEN　第4版练习", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案见第8版　题目可跨级混排，按题号找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A　BEGRIJPEN", 25)
e.bridge("读第 4 版文章，选出正确答案。")
e.ex("B1", "单选", "B", "PSV 客场 1–0 赢波尔图",
     "PSV won dinsdag... A. thuis met 1–0 · B. bij FC Porto met 1–0 · C. met 3–0 in Rotterdam", size=20, gap=8)
e.ex("B1", "单选", "A", "费耶诺德周三在塞维利亚比赛",
     "Feyenoord speelt op woensdag... A. in Sevilla · B. in Rotterdam · C. in Porto", size=20, gap=8)
e.ex("B1", "单选", "B", "阿贾克斯周四对亚特兰大",
     "Ajax speelt donderdag... A. tegen Porto · B. tegen Atalanta · C. tegen Feyenoord", size=20, gap=8)
e.ex("B1", "单选", "C", "焦点战在周日 14:30",
     "De topper PSV – Feyenoord is... A. op zaterdag om 14:30 · B. op zondag om 16:45 · C. op zondag om 14:30", size=20, gap=8)
e.ex("B1", "单选", "B", "斯巴达–阿贾克斯 16:45 开始",
     "Sparta – Ajax begint om... A. 14:30 uur · B. 16:45 uur · C. 20:00 uur", size=20, gap=8)
e.head("B　WOORDEN UIT DE TEKST", 25)
e.bridge("用方框里的词填空。")
e.para("uitslag · winnaar · speelronde · in actie · thuis · speculatie", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "完成句子", "uitslag", "uitslag = 比分",
     "De ___ van Porto – PSV was 1–0.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "winnaar", "winnaar = 获胜者",
     "Er is nog geen ___ van de Ballon d'Or.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "speelronde", "speelronde = 轮次",
     "Het is ___ 10 van de Eredivisie.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "in actie", "in actie komen = 上场、出战",
     "Op donderdag komen vier clubs ___.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "thuis", "thuis = 在主场/在家",
     "Ajax speelt donderdag ___ tegen Atalanta.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "speculatie", "speculatie = 猜测",
     "De Ballon d'Or-verhalen zijn ___: er is nog geen winnaar.", instr="填空", size=20, gap=8)
e.head("C　VERLEDEN TIJD", 25)
e.bridge("用过去时或完成时补全。")
e.ex("B1", "完成句子", "won", "winnen 过去时：won",
     "PSV ___ (winnen) dinsdag met 1–0 in Porto.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "heeft gewonnen", "perfectum：heeft gewonnen",
     "De club ___ (winnen) de wedstrijd in Porto.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "ging", "gaan 过去时：ging",
     "De bal ___ (gaan) in het doel: 1–0!", instr="填空", size=20, gap=8)
e.ex("B2", "完成句子", "zijn gekomen", "komen 的 perfectum 用 zijn",
     "Veel supporters ___ (komen) naar het stadion.", instr="填空", size=20, gap=8)
e.head("D　WAAR OF NIET WAAR?", 25)
e.ex("B1", "判断对错", "Waar", "对：客场 1–0 获胜",
     "PSV won in de Champions League bij FC Porto. Waar of niet waar?", instr="判断", size=20, gap=8)
e.ex("B1", "判断对错", "Niet waar", "错：还没有获胜者，只是猜测",
     "De Ballon d'Or heeft al een winnaar. Waar of niet waar?", instr="判断", size=20, gap=8)
e.ex("B2", "判断对错", "Niet waar", "错：是在塞维利亚客场",
     "Feyenoord speelt woensdag thuis in Rotterdam. Waar of niet waar?", instr="判断", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
