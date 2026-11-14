# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTUUR (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTUUR　문화", "De Lucerna", "NIVEAU A2 → B1　Dutch Design Week en de herfstvakantie　디자인 위크와 가을 방학")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P3-feature")
f.title("Ontwerpen in Eindhoven: de Dutch Design Week", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: A2 → B1")
f.para("Negen dagen lang is Eindhoven de designhoofdstad van Nederland. De Dutch Design Week duurt van zaterdag 17 tot en met zondag 25 oktober. Het is de 26e editie, met als thema «R.A.W.». Ongeveer 2.500 ontwerpers laten hun werk zien: meubels, kleding, websites en dingen die nog geen naam hebben.")
f.para("Waar gaat het over? De ontwerpers werken met materialen: oud plastic wordt een stoel, en planten worden materiaal voor huizen. Dat werken met de natuur heet biodesign. Ook kunstmatige intelligentie (AI) helpt mee aan nieuwe vormen.")
f.para("Een normaal kaartje kost € 32,50; studenten betalen € 19,50. Wie jong is en van maken houdt, is hier op de goede plek: je mag veel dingen aanraken en vragen stellen aan de makers.")
f.head("EROPUIT IN DE HERFSTVAKANTIE", 22)
f.para("Geen school, wel musea: in de herfstvakantie organiseren musea extra activiteiten voor families. Het Limburgs Museum in Venlo heeft van 17 tot en met 25 oktober een speciaal vakantieprogramma, met een gratis familiedag op zaterdag 24 oktober.")
f.para("Let op: niet heel Nederland is vrij. De regio Noord had vorige week vakantie, van 10 tot en met 18 oktober; daar zitten de kinderen deze week weer gewoon in de klas. Alleen Midden en Zuid hebben nu herfstvakantie.")
f.para("Buiten is het ook mooi: het bos is geel en rood, en overal liggen kastanjes en eikels op de grond. Een wandeling in het herfstbos is het goedkoopste uitje van de week.")
f.gloss("de ontwerper 디자이너 · het materiaal 재료 · aanraken 만지다 · de kastanje 밤 · eropuit 나들이 가다.")
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
p.text(MX, ey + 28, "OEFENINGEN　제 3 면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면에　문제는 단계가 섞여 있어요, 번호로 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A　BEGRIJPEN", 25)
e.expl("3면 기사를 읽고 정답을 고르세요.")
e.ex("A2", "객관식", "B", "디자인 위크는 에인트호번에서 열려요",
     "De Dutch Design Week is in... A. Amsterdam · B. Eindhoven · C. Venlo", size=20, gap=8)
e.ex("A2", "객관식", "B", "17–25일, 모두 9일",
     "De Design Week duurt... A. vijf dagen · B. negen dagen · C. twee weken", size=20, gap=8)
e.ex("A2", "객관식", "A", "주제는 «R.A.W.»예요",
     "Het thema van dit jaar is... A. «R.A.W.» · B. «Natuur» · C. «30 jaar»", size=20, gap=8)
e.ex("B1", "객관식", "B", "biodesign은 식물 같은 자연 재료를 써요",
     "Biodesign werkt met... A. alleen oude meubels · B. planten en materialen uit de natuur · C. alleen websites", size=20, gap=8)
e.ex("B1", "객관식", "A", "무료 가족의 날은 토요일 10월 24일",
     "De gratis familiedag in Venlo is op... A. zaterdag 24 oktober · B. zondag 25 oktober · C. maandag 19 oktober", size=20, gap=8)
e.head("B　WOORDEN UIT DE TEKST", 25)
e.expl("상자 속 단어로 빈칸을 채우세요. 주의: 어떤 단어는 복수형으로 바꿔야 해요.")
e.para("ontwerper · materiaal · thema · aanraken · kastanjes · eropuit", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "문장 완성", "ontwerpers", "ontwerper 복수형: ontwerpers",
     "Ongeveer 2.500 ___ laten hun werk zien in Eindhoven.", instr="빈칸 채우기", size=20, gap=8)
e.ex("A2", "문장 완성", "thema", "thema = 주제(het)",
     "Het ___ van de Design Week is «R.A.W.».", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "materiaal", "materiaal = 재료",
     "Planten worden ___ voor nieuwe huizen.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "aanraken", "aanraken = 만지다",
     "Op de Design Week mag je veel dingen ___.", instr="빈칸 채우기", size=20, gap=8)
e.ex("A2", "문장 완성", "kastanjes", "kastanjes = 밤",
     "In het bos liggen ___ en eikels op de grond.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "eropuit", "eropuit = 나들이 가다",
     "In de vakantie gaan families ___: naar een museum of het bos.", instr="빈칸 채우기", size=20, gap=8)
e.head("C　HET PERFECTUM", 25)
e.expl("현재완료형으로 완성하세요. 조동사 hebben/zijn에 주의하세요.")
e.ex("B1", "문장 완성", "heeft gemaakt", "maken은 hebben 사용: heeft gemaakt",
     "De ontwerper ___ (maken) een stoel van oud plastic.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "zijn gegaan", "gaan은 zijn 사용: zijn gegaan",
     "Wij ___ (gaan) naar het museum in Venlo.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "heeft gezien", "zien 불규칙: heeft gezien",
     "Zij ___ (zien) het werk van 2.500 ontwerpers.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "zijn gekomen", "komen은 zijn 사용: zijn gekomen",
     "Veel families ___ (komen) naar Eindhoven.", instr="빈칸 채우기", size=20, gap=8)
e.head("D　REKENEN", 25)
e.expl("계산해 보세요: 3면의 숫자로 답하세요.")
e.ex("B1", "문장 완성", "9", "17일부터 25일까지 모두 9일",
     "De Design Week duurt van 17 tot en met 25 oktober: ___ dagen.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "24", "무료 가족의 날은 10월 24일",
     "De gratis familiedag in het Limburgs Museum is op zaterdag ___ oktober.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B2", "문장 완성", "71,50", "19,50 + 19,50 + 32,50 = 71,50",
     "Twee studenten en één volwassene kopen een kaartje. Samen betalen zij € ___.", instr="빈칸 채우기", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultuur.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT　스포츠", "De Lucerna", "NIVEAU B1　Europese week en de topper van zondag　유럽 대항전 주간과 일요일 빅매치")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P4-feature")
f.title("Europese week: PSV wint in Porto, zondag de topper", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: B1")
f.para("Wat een week voor het Nederlandse voetbal. Zes clubs spelen in Europa. PSV won dinsdag met 1–0 bij FC Porto in de Champions League: een kleine uitslag, maar drie grote punten.")
f.para("Op woensdag speelt Feyenoord in Sevilla tegen Real Betis. Op donderdag komen Ajax (thuis tegen Atalanta), AZ, NEC en FC Twente in actie. De uitslagen van woensdag en donderdag lees je volgende week: deze krant was toen al gedrukt.")
f.para("En dan zondag: de topper. PSV speelt thuis tegen Feyenoord, om 14:30 uur. Later op de middag speelt Sparta tegen Ajax, om 16:45 uur. Het is speelronde 10 van de Eredivisie — en de laatste dag van de herfstvakantie voor Midden en Zuid.")
f.para("Ook op Google is de Europese week groot: de zoekopdracht «uitslagen champions league» haalde dinsdag meer dan 1.000 zoekopdrachten in Nederland. Iedereen wil de uitslagen van alle clubs tegelijk zien.")
f.head("DE BALLON D'OR", 25)
f.para("Op internet praat iedereen over de Ballon d'Or: wie is de beste speler van het jaar? De namen van Yamal, Mbappé en Kane komen vaak voorbij. Maar er is nog geen winnaar: het is speculatie, geen nieuws. Wie is jouw favoriet?")
f.gloss("de uitslag 경기 결과 · winnen 이기다 · in actie komen 출전하다 · de speelronde 라운드 · de winnaar 승자.")
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
p.text(MX, ey + 28, "OEFENINGEN　제 4 면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면에　문제는 단계가 섞여 있어요, 번호로 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A　BEGRIJPEN", 25)
e.expl("4면 기사를 읽고 정답을 고르세요.")
e.ex("B1", "객관식", "B", "PSV가 원정에서 포르투를 1–0으로 이겼어요",
     "PSV won dinsdag... A. thuis met 1–0 · B. bij FC Porto met 1–0 · C. met 3–0 in Rotterdam", size=20, gap=8)
e.ex("B1", "객관식", "A", "페예노르트는 수요일 세비야에서 경기해요",
     "Feyenoord speelt op woensdag... A. in Sevilla · B. in Rotterdam · C. in Porto", size=20, gap=8)
e.ex("B1", "객관식", "B", "아약스는 목요일 아탈란타와 경기해요",
     "Ajax speelt donderdag... A. tegen Porto · B. tegen Atalanta · C. tegen Feyenoord", size=20, gap=8)
e.ex("B1", "객관식", "C", "빅매치는 일요일 14:30",
     "De topper PSV – Feyenoord is... A. op zaterdag om 14:30 · B. op zondag om 16:45 · C. op zondag om 14:30", size=20, gap=8)
e.ex("B1", "객관식", "B", "스파르타–아약스는 16:45 시작",
     "Sparta – Ajax begint om... A. 14:30 uur · B. 16:45 uur · C. 20:00 uur", size=20, gap=8)
e.head("B　WOORDEN UIT DE TEKST", 25)
e.expl("상자 속 단어로 빈칸을 채우세요.")
e.para("uitslag · winnaar · speelronde · in actie · thuis · speculatie", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "문장 완성", "uitslag", "uitslag = 경기 결과",
     "De ___ van Porto – PSV was 1–0.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "winnaar", "winnaar = 승자",
     "Er is nog geen ___ van de Ballon d'Or.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "speelronde", "speelronde = 라운드",
     "Het is ___ 10 van de Eredivisie.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "in actie", "in actie komen = 출전하다",
     "Op donderdag komen vier clubs ___.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "thuis", "thuis = 홈에서/집에서",
     "Ajax speelt donderdag ___ tegen Atalanta.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "speculatie", "speculatie = 추측",
     "De Ballon d'Or-verhalen zijn ___: er is nog geen winnaar.", instr="빈칸 채우기", size=20, gap=8)
e.head("C　VERLEDEN TIJD", 25)
e.expl("과거형이나 완료형으로 완성하세요.")
e.ex("B1", "문장 완성", "won", "winnen 과거형: won",
     "PSV ___ (winnen) dinsdag met 1–0 in Porto.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "heeft gewonnen", "perfectum：heeft gewonnen",
     "De club ___ (winnen) de wedstrijd in Porto.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "ging", "gaan 과거형: ging",
     "De bal ___ (gaan) in het doel: 1–0!", instr="빈칸 채우기", size=20, gap=8)
e.ex("B2", "문장 완성", "zijn gekomen", "komen의 완료형은 zijn 사용",
     "Veel supporters ___ (komen) naar het stadion.", instr="빈칸 채우기", size=20, gap=8)
e.head("D　WAAR OF NIET WAAR?", 25)
e.ex("B1", "참/거짓 판단", "Waar", "참: 원정에서 1–0 승리",
     "PSV won in de Champions League bij FC Porto. Waar of niet waar?", instr="참 / 거짓", size=20, gap=8)
e.ex("B1", "참/거짓 판단", "Niet waar", "거짓: 아직 승자가 없어요, 추측일 뿐이에요",
     "De Ballon d'Or heeft al een winnaar. Waar of niet waar?", instr="참 / 거짓", size=20, gap=8)
e.ex("B2", "참/거짓 판단", "Niet waar", "거짓: 세비야 원정이예요",
     "Feyenoord speelt woensdag thuis in Rotterdam. Waar of niet waar?", instr="참 / 거짓", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
