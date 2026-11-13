# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTUUR (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTUUR　문화", "De Lucerna", "NIVEAU A2 → B1　Sinterklaas is er!　신터클라스가 왔다!")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P3-feature")
f.title("Sinterklaas is er: Grave, Amsterdam en het journaal", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: A2 → B1")
f.para("Op zaterdag 14 november kwam Sinterklaas officieel aan in Nederland. De landelijke intocht was dit jaar in Grave, een vestingstad aan de Maas in Noord-Brabant. Rond 12:00 uur meerde de stoomboot aan bij de Maaskade. Burgemeester Marieke Moorman ontving Sinterklaas. Het programma duurde van 12:00 tot 16:00 uur en was live te zien op NPO 3.")
f.para("Een dag later voer Sinterklaas in Amsterdam: de boot vertrok om 10:15 uur bij De Omval en voer over de Amstel naar het Scheepvaartmuseum, waar hij rond 11:30 uur aankwam. Daar kreeg hij de sleutel van de stad. Om 13:00 uur begon de stoet te paard bij de Stopera, via het Rembrandtplein en de Utrechtsestraat naar het Leidseplein. Het was de 88e editie van de Amsterdamse intocht.")
f.para("Het Sinterklaasjournaal is er elke dag om 18:00 uur op NPO Zapp. Presentatrice Merel Westrik vertelt hoe de voorbereidingen gaan: de schoen, de verlanglijstjes en — over negentien dagen — pakjesavond op zaterdag 5 december.")
f.para("November is ook de maand van Heel Nederland Leest: heel Nederland leest dit jaar Het diner van Herman Koch, uit 2009. Het boek is gratis af te halen in de bibliotheek, ook als je geen lid bent. Er is ook een grootletterboek, een Makkelijk Lezen-editie, een e-book en een luisterboek. In bibliotheken zijn er leeskringen — ook voor mensen die Nederlands leren.")
f.head("LEZEN EN KIJKEN", 25)
f.para("Twee dingen in november: 's avonds om 18:00 uur het Sinterklaasjournaal kijken, en overdag een boek lezen. Neem Het diner mee naar huis en praat erover met vrienden: samen lezen is leuker dan alleen lezen.")
f.para("En wie zijn schoen zet, kan er een verlanglijstje in doen — of een tekening. Sinterklaas leest alles.")
f.gloss("de vestingstad 요새 도시 · ontvangen 맞이하다 · de sleutel 열쇠 · de editie 회 · de leeskring 독서 모임.")
f.end_report()

# col 3: image + facts box (sequential, measured)
ix = COLX[3]
image(p, "gracht.jpg", ix, 200, CW, 250)
cy3 = caption(p, ix, 450, CW, "Een boot in een Amsterdamse gracht. Zondag voer de stoomboot van Sinterklaas over de Amstel naar het Scheepvaartmuseum.",
              "Foto: W. Punt / Anefo, Nationaal Archief — CC0")
facts = ["Landelijke intocht: zaterdag 14 november, Grave, Maaskade, vanaf 12:00 uur op tv.",
         "Amsterdam: zondag 15 november, boot 10:15 uur, stoet 13:00 uur, 88e editie.",
         "Sinterklaasjournaal: elke dag 18:00 uur, NPO Zapp, met Merel Westrik.",
         "Heel Nederland Leest: Het diner, gratis in de bibliotheek, heel november."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 64
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "SINTERKLAAS IN CIJFERS", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P3 col3 ends", sy3 + sh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "OEFENINGEN　3면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면에　수준이 섞여 있으니 번호로 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A　BEGRIJPEN", 25)
e.bridge("3면 기사를 읽고 정답을 고르세요.")
e.ex("A2", "객관식", "B", "전국 도착은 흐라버에서 열려요",
     "De landelijke intocht was in... A. Amsterdam · B. Grave · C. Utrecht", size=20, gap=8)
e.ex("A2", "객관식", "B", "배는 12:00경 마스카더에 도착한다",
     "De stoomboot meerde aan om... A. 18:00 uur · B. 12:00 uur · C. 20:45 uur", size=20, gap=8)
e.ex("A2", "객관식", "C", "암스테르담 배는 10:15에 더 옴팔을 떠나요",
     "De boot in Amsterdam vertrok om... A. 12:00 uur · B. 13:00 uur · C. 10:15 uur", size=20, gap=8)
e.ex("A2", "객관식", "A", "암스테르담 도착은 88회째예요",
     "De intocht in Amsterdam was de... A. 88e editie · B. 26e editie · C. 30e editie", size=20, gap=8)
e.ex("A2", "객관식", "B", "『Het diner』는 도서관에서 무료로 가져갈 수 있어요",
     "Het diner is gratis af te halen in... A. de boekwinkel · B. de bibliotheek · C. het museum", size=20, gap=8)
e.head("B　WOORDEN UIT DE TEKST", 25)
e.bridge("상자 속 단어로 채우세요.")
e.para("vestingstad · ontvangen · sleutel · editie · leeskring", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "문장 완성", "vestingstad", "vestingstad = 요새 도시",
     "Grave is een oude ___ aan de Maas.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "ontving", "ontvangen의 과거형: ontving",
     "Burgemeester Moorman ___ Sinterklaas in Grave.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "sleutel", "sleutel = 열쇠",
     "Sinterklaas kreeg de ___ van de stad.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "editie", "editie = 회",
     "Het was de 88e ___ van de Amsterdamse intocht.", instr="빈칸 채우기", size=20, gap=8)
e.ex("A2", "문장 완성", "leeskring", "leeskring = 독서 모임",
     "In de bibliotheek is er een ___ over Het diner.", instr="빈칸 채우기", size=20, gap=8)
e.head("C　HET PERFECTUM", 25)
e.bridge("현재완료로 채우세요. 조동사 hebben/zijn에 주의하세요.", w=414.35)  # delta D6: width-scan band 405.0-423.7px keeps the 2 lines; mid 414.35
e.ex("B1", "문장 완성", "is aangekomen", "aankomen은 zijn을 써요: is aangekomen",
     "Sinterklaas ___ (aankomen) in Grave.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "heeft ontvangen", "ontvangen의 완료형: heeft ontvangen",
     "De burgemeester ___ (ontvangen) Sinterklaas.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "is gevaren", "varen은 zijn과 함께: is gevaren",
     "De boot ___ (varen) van De Omval naar het Scheepvaartmuseum.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "hebben gelezen", "lezen 완료형: hebben gelezen",
     "Veel mensen ___ (lezen) Het diner in november.", instr="빈칸 채우기", size=20, gap=8)
e.head("D　REKENEN", 25)
e.bridge("계산해 보세요: 3면 숫자로 답하세요.")
e.ex("B1", "문장 완성", "1", "11월 14일부터 15일까지는 1일",
     "Van zaterdag 14 tot zondag 15 november: ___ dag.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "4", "흐라버 프로그램 12:00–16:00은 4시간이에요",
     "Het programma in Grave duurde van 12:00 tot 16:00 uur: ___ uur.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "19", "11월 16일부터 12월 5일까지는 19일",
     "Van 16 november tot 5 december: ___ dagen.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B2", "문장 완성", "17", "『Het diner』는 2009년 작품: 2026년이면 17년 전이에요",
     "Het diner is uit 2009; in 2026 is dat ___ jaar geleden.", instr="빈칸 채우기", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultuur.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT　스포츠", "De Lucerna", "NIVEAU B1　Oranje en de Nations League　오라녜와 네이션스리그")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P4-feature")
f.title("Oranje: de beslissing in Berlijn", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: B1")
f.para("Op maandag 16 november speelt Oranje in Berlijn tegen Duitsland. De wedstrijd begint om 20:45 uur in het Olympiastadion en is live te zien op NPO 3. Het is de zesde en laatste wedstrijd in de groepsfase van de Nations League — en de beslissing in groep 2: de nummers één en twee gaan naar de kwartfinales in maart 2027.")
f.para("Na vier wedstrijden staan Nederland en Griekenland samen bovenaan met 8 punten. Duitsland heeft 5 punten, Servië heeft 0 punten. Nederland staat eerste, omdat het meer doelpunten maakte: 7 tegen 5. Oranje is nog ongeslagen: 1–1 thuis tegen Duitsland, 2–1 uit bij Servië, 2–2 uit bij Griekenland en 2–1 thuis tegen Servië.")
f.para("Duitsland moet winnen in Berlijn. De Duitsers verloren thuis met 0–1 van Griekenland, wonnen met 2–0 van Servië en speelden met 0–0 gelijk in Griekenland. Vrijdag speelde Duitsland in Belgrado tegen Servië; Oranje speelde vrijdag thuis tegen Griekenland. Maandagavond in Berlijn valt de beslissing.")
f.para("De Eredivisie begint zaterdag weer: speelronde 13 is op 21 en 22 november. Zaterdag speelt PSV om 16:30 uur uit bij NEC en speelt Feyenoord om 18:45 uur thuis tegen Excelsior. Zondag speelt Ajax om 14:30 uur thuis tegen ADO Den Haag en speelt FC Twente om 12:15 uur thuis tegen Willem II. Vóór de interlandperiode won PSV met 2–5 van Cambuur en werd het 5–3 bij Heerenveen – Feyenoord.")
f.head("DE STAND IN GROEP 2", 25)
f.para("Nederland 8 punten, Griekenland 8, Duitsland 5, Servië 0. Twee landen gaan door. Maandag in Berlijn is dus bijna een finale — de laatste wedstrijd van de groep.")
f.gloss("de groepswinst 조 우승 · de kwartfinale 8강전 · ongeslagen 무패 · de interland 국가대표 경기 · de stand 순위표.")
f.end_report()

# col 3: image + programme box (sequential, measured)
ix = COLX[3]
image(p, "elftal1912.jpg", ix, 200, CW, 250)
cy3 = caption(p, ix, 450, CW, "Het Nederlands elftal in 1912. Oranje speelt al meer dan honderd jaar in het oranje.",
              "Foto: Spaarnestad Photo / Wikimedia Commons — publiek domein")
facts = ["Maandag 16 november, 20:45 uur: Duitsland – Nederland, Berlijn, NPO 3.",
         "Stand na 4 wedstrijden: Nederland 8, Griekenland 8, Duitsland 5, Servië 0 punten.",
         "Speelronde 12: Heerenveen – Feyenoord 5–3; Cambuur – PSV 2–5; Twente – Ajax 2–2.",
         "Stand Eredivisie na 12 ronden: PSV 26, Feyenoord 25, Ajax 25 punten.",
         "Speelronde 13: zaterdag NEC – PSV 16:30 uur; Feyenoord – Excelsior 18:45 uur."]
sy3 = cy3 + 24
sh = 89 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32 + 30  # delta D11: top reserve 62 -> 89 = 16 (pad) + 52 (title block) + 21 (para y-offset); last line was 6.89px below the box
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
p.text(MX, ey + 28, "OEFENINGEN　4면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면에　수준이 섞여 있으니 번호로 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A　BEGRIJPEN", 25)
e.bridge("4면 기사를 읽고 정답을 고르세요.")
e.ex("B1", "객관식", "C", "독일–네덜란드, 월요일, 베를린",
     "Duitsland – Nederland is op... A. vrijdag 13 november · B. zaterdag 14 november · C. maandag 16 november", size=20, gap=8)
e.ex("B1", "객관식", "B", "네덜란드와 그리스는 둘 다 승점 8점이에요",
     "Na vier wedstrijden hebben Nederland en Griekenland... A. 5 punten · B. 8 punten · C. 0 punten", size=20, gap=8)
e.ex("B1", "객관식", "B", "독일은 홈에서 그리스에 0–1로 졌다",
     "Duitsland verloor thuis met 0–1 van... A. Servië · B. Griekenland · C. Nederland", size=20, gap=8)
e.ex("B1", "객관식", "B", "에레디비시 13라운드는 11월 21–22일이에요",
     "Speelronde 13 is op... A. 13 en 14 november · B. 21 en 22 november · C. 9 en 10 november", size=20, gap=8)
e.ex("B1", "객관식", "B", "PSV는 캄뷔르에 2–5로 이겼다",
     "PSV won met 2–5 van... A. Feyenoord · B. Cambuur · C. Ajax", size=20, gap=8)
e.head("B　WOORDEN UIT DE TEKST", 25)
e.bridge("상자 속 단어로 채우세요. 동사 형태에 주의하세요.")
e.para("groepswinst · kwartfinale · ongeslagen · interland · stand", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "문장 완성", "groepswinst", "groepswinst = 조 우승",
     "Maandag valt de beslissing om de ___.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "kwartfinales", "kwartfinale 복수형: kwartfinales",
     "De nummers één en twee gaan naar de ___.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "ongeslagen", "ongeslagen = 무패",
     "Oranje is nog ___ na vier wedstrijden.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "stand", "stand = 순위표",
     "Op de ___ staat Servië onderaan met 0 punten.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "interland", "interland = 국가대표 경기",
     "Na maandag is er geen ___ meer tot maart.", instr="빈칸 채우기", size=20, gap=8)
e.head("C　VERLEDEN TIJD", 25)
e.bridge("과거형이나 완료형으로 채우세요.")
e.ex("B1", "문장 완성", "speelde", "spelen 과거형: speelde",
     "Oranje ___ (spelen) 1–1 tegen Duitsland.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "won", "winnen 과거형: won",
     "PSV ___ (winnen) met 2–5 van Cambuur.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "verloor", "verliezen의 과거형: verloor",
     "Feyenoord ___ (verliezen) met 5–3 bij Heerenveen.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B2", "문장 완성", "speelden", "spelen의 과거형 복수: speelden",
     "Twente en Ajax ___ (spelen) 2–2 gelijk.", instr="빈칸 채우기", size=20, gap=8)
e.head("D　WAAR OF NIET WAAR?", 25)
e.ex("B1", "참/거짓 판단", "Waar", "참: 독일–네덜란드, 월요일 20:45",
     "Duitsland – Nederland begint maandag om 20:45 uur. Waar of niet waar?", instr="참 / 거짓", size=20, gap=8)
e.ex("B1", "참/거짓 판단", "Niet waar", "거짓: 세르비아는 승점 0점으로 최하위예요",
     "Servië heeft 8 punten in groep 2. Waar of niet waar?", instr="참 / 거짓", size=20, gap=8)
e.ex("B1", "참/거짓 판단", "Niet waar", "거짓: PSV는 26점으로 에레디비시 선두",
     "PSV staat onderaan in de Eredivisie. Waar of niet waar?", instr="참 / 거짓", size=20, gap=8)
e.ex("B1", "참/거짓 판단", "Waar", "참: 헤렌베인은 페예노르트에 5–3으로 이겼다",
     "Heerenveen won met 5–3 van Feyenoord. Waar of niet waar?", instr="참 / 거짓", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
