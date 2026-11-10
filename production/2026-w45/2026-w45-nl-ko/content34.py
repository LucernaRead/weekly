# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTUUR (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTUUR　문화", "De Lucerna", "NIVEAU A2 → B1　Museumnacht, boeken en kunst　박물관의 밤, 책과 예술")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P3-feature")
f.title("Amsterdam blijft wakker: de Museumnacht", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: A2 → B1")
f.para("Zaterdagavond 7 november blijft Amsterdam wakker: het is Museumnacht, de 26e editie. Meer dan 70 musea zijn open van 19:00 uur 's avonds tot 02:00 uur 's nachts, met muziek, workshops en rondleidingen. Eén kaartje geeft toegang tot alle deelnemende musea.")
f.para("Let op: de Museumkaart geldt deze avond niet — je hebt een apart kaartje nodig. Populaire musea werken met tijdsloten: reserveer op tijd, anders sta je in de rij. Veel bezoekers gaan op de fiets van museum naar museum; er rijden ook extra nachtbussen.")
f.para("In Den Haag is het deze week Crossing Border Festival, van dinsdag tot en met zondag: schrijvers en muzikanten delen het podium. Literatuur en muziek horen bij elkaar, zeggen de organisatoren — een boek kan klinken als een lied, en een lied kan lezen als een verhaal.")
f.para("En de kunstbeurs PAN Amsterdam in de RAI loopt nog tot en met zondag 8 november: kunst, antiek en design uit alle eeuwen, van oud porselein tot nieuwe meubels.")
f.head("TWEEDEHANDS IS OOK CULTUUR", 25)
f.para("In Zaandam is op 7 en 8 november de Mega Snuffelmarkt, met zo'n 250 kramen vol tweedehands spullen: boeken, platen, kleding en speelgoed. Tweedehands kopen is ook klimaatvriendelijk: wat al bestaat, hoeft niet opnieuw gemaakt te worden.")
f.para("En wie na de markt nog energie heeft, fietst 's avonds naar Amsterdam: daar begint om 19:00 uur de Museumnacht.")
f.gloss("het museum 박물관 · de rondleiding 안내 투어 · het tijdslot 시간대 · tweedehands 중고의 · de beurs 박람회.")
f.end_report()

# col 3: image + facts box (sequential, measured)
ix = COLX[3]
image(p, "gracht.jpg", ix, 200, CW, 250)
cy3 = caption(p, ix, 450, CW, "Een boot in een Amsterdamse gracht. Tijdens Museumnacht fietst en vaart de stad de hele nacht door.",
              "Foto: W. Punt / Anefo, Nationaal Archief — CC0")
facts = ["26e editie van Museumnacht, zaterdag 7 november, 19:00–02:00 uur.",
         "Meer dan 70 musea doen mee; de Museumkaart geldt niet.",
         "PAN Amsterdam in de RAI, tot en met zondag 8 november."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "MUSEUMNACHT IN CIJFERS", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P3 col3 ends", sy3 + sh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "OEFENINGEN　3면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면　문제는 수준이 섞여 있어요, 번호로 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A　BEGRIJPEN", 25)
e.bridge("3면 기사를 읽고 정답을 고르세요.")
e.ex("A2", "객관식", "B", "박물관의 밤은 11월 7일 토요일이에요",
     "Museumnacht is op... A. vrijdag 6 november · B. zaterdag 7 november · C. zondag 8 november", size=20, gap=8)
e.ex("A2", "객관식", "B", "박물관은 새벽 2시까지 문을 열어요",
     "De musea zijn open tot... A. 24:00 uur · B. 02:00 uur · C. 19:00 uur", size=20, gap=8)
e.ex("A2", "객관식", "C", "크로싱 보더는 헤이그에 있어요",
     "Crossing Border is in... A. Amsterdam · B. Rotterdam · C. Den Haag", size=20, gap=8)
e.ex("A2", "객관식", "A", "크로싱 보더는 책과 음악을 결합해요",
     "Crossing Border combineert... A. boeken en muziek · B. voetbal en dans · C. film en eten", size=20, gap=8)
e.ex("A2", "객관식", "B", "PAN 아트페어는 11월 8일까지예요",
     "PAN Amsterdam loopt tot en met... A. zaterdag 7 november · B. zondag 8 november · C. maandag 9 november", size=20, gap=8)
e.head("B　WOORDEN UIT DE TEKST", 25)
e.bridge("네모 안의 단어로 채우세요(복수형 주의).")
e.para("museum · rondleiding · tijdslot · tweedehands · beurs", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "문장 완성", "musea", "museum 복수형: musea",
     "Op Museumnacht zijn meer dan 70 ___ open.", instr="빈칸 채우기", size=20, gap=8)
e.ex("A2", "문장 완성", "rondleiding", "rondleiding = 안내 투어",
     "Een ___ laat je de mooiste zalen zien.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "tijdslot", "tijdslot = 시간대",
     "Reserveer een ___ voor populaire musea.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "tweedehands", "tweedehands = 중고의",
     "Op de Snuffelmarkt koop je ___ spullen.", instr="빈칸 채우기", size=20, gap=8)
e.ex("A2", "문장 완성", "beurs", "beurs = 박람회",
     "PAN is een ___ voor kunst en antiek.", instr="빈칸 채우기", size=20, gap=8)
e.head("C　HET PERFECTUM", 25)
e.bridge("현재완료로 채우세요(조동사 hebben/zijn).")
e.ex("B1", "문장 완성", "zijn geweest", "zijn의 perfectum: zijn geweest",
     "De musea ___ (zijn) tot 02:00 uur open.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "hebben gekocht", "kopen의 perfectum: hebben gekocht",
     "Wij ___ (kopen) één kaartje voor alle musea.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "hebben voorgelezen", "voorlezen의 perfectum: hebben voorgelezen",
     "De schrijvers ___ (voorlezen) hun werk op het podium.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "zijn gekomen", "komen은 zijn과 함께 써요: zijn gekomen",
     "Veel bezoekers ___ (komen) met de fiets.", instr="빈칸 채우기", size=20, gap=8)
e.head("D　REKENEN", 25)
e.bridge("계산해 보세요: 3면 숫자로 답하세요.")
e.ex("B1", "문장 완성", "7", "19:00부터 02:00까지 모두 7시간이에요",
     "Museumnacht duurt van 19:00 tot 02:00 uur: ___ uur.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "8", "11월 1-8일은 모두 8일이에요",
     "PAN Amsterdam loopt van 1 tot en met 8 november: ___ dagen.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "6", "11월 3-8일은 모두 6일이에요",
     "Crossing Border duurt van dinsdag 3 tot en met zondag 8 november: ___ dagen.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B2", "문장 완성", "125", "250의 절반은 125예요",
     "De Snuffelmarkt heeft zo'n 250 kramen; de helft is ___.", instr="빈칸 채우기", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultuur.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT　스포츠", "De Lucerna", "NIVEAU B1　Europese week en speelronde 12　유럽 대회 주간과 12라운드")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P4-feature")
f.title("Europa: drie keer feest, twee keer verlies", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: B1")
f.para("De Europese week is voorbij — en de balans is drie keer feest, twee keer verlies. Ajax won donderdag 22 oktober met 2–0 van Atalanta in de Conference League. Twente won met 4–1 bij Lincoln Red Imps in Gibraltar. AZ won met 4–0 van Ararat-Armenia. NEC verloor: 2–4 bij Dinamo Zagreb.")
f.para("En woensdag 21 oktober verloor Feyenoord in de Champions League: Real Betis won met 1–0 in Sevilla, door een doelpunt van Isco in de 59e minuut. Feyenoord had wel meer balbezit, maar schoot te weinig op doel.")
f.para("In de Eredivisie was het zondag 25 oktober ook spannend: PSV en Feyenoord speelden 1–1 gelijk. Ajax won met 2–1 bij Sparta. En Twente won met 2–0 bij AZ. Na 10 ronden staat Feyenoord bovenaan met 24 punten, Ajax heeft 21, en PSV, Twente en AZ hebben elk 20 punten.")
f.para("Nu speelronde 12. Vrijdagavond: Willem II tegen PEC Zwolle (19:00 uur). Zaterdag: Fortuna tegen Telstar (15:30), ADO tegen Sparta (17:45) en Excelsior tegen Go Ahead Eagles (20:00). Zondag de topper: Heerenveen tegen Feyenoord (11:15) en Twente tegen Ajax (13:30), plus Cambuur tegen PSV, AZ tegen Groningen (15:45) en Utrecht tegen NEC (19:00).")
f.head("DE STAND NA 10 RONDEN", 25)
f.para("Feyenoord 24 punten, Ajax 21, PSV 20, Twente 20, AZ 20. Onderaan staan ADO en Telstar met 6 punten en Willem II met 2 punten. Maar er zijn nog 24 ronden te gaan: alles kan nog veranderen.")
f.gloss("de balans 결산 · gelijkspelen 비기다 · de speelronde 라운드 · de topper 빅매치 · de stand 순위표.")
f.end_report()

# col 3: image + programme box (sequential, measured)
ix = COLX[3]
image(p, "elftal1912.jpg", ix, 200, CW, 250)
cy3 = caption(p, ix, 450, CW, "Het Nederlands elftal in 1912. Voetbal is al meer dan honderd jaar de sport van Nederland.",
              "Foto: Spaarnestad Photo / Wikimedia Commons — publiek domein")
facts = ["Donderdag 22 oktober: Ajax – Atalanta 2–0; Twente – Lincoln 4–1; AZ – Ararat 4–0; Dinamo – NEC 4–2.",
         "Woensdag 21 oktober: Real Betis – Feyenoord 1–0.",
         "Zondag 25 oktober: PSV – Feyenoord 1–1; Sparta – Ajax 1–2; AZ – Twente 0–2.",
         "Speelronde 12: vrijdag Willem II – PEC; zondag Heerenveen – Feyenoord (11:15) en Twente – Ajax (13:30)."]
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
p.text(MX, ey + 28, "OEFENINGEN　4면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면　문제는 수준이 섞여 있어요, 번호로 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A　BEGRIJPEN", 25)
e.bridge("4면 기사를 읽고 정답을 고르세요.")
e.ex("B1", "객관식", "B", "아약스가 아탈란타를 2-0으로 이겼어요",
     "Ajax won donderdag met... A. 1–0 · B. 2–0 · C. 4–1", size=20, gap=8)
e.ex("B1", "객관식", "C", "트벤테가 링컨 레드임프스를 4-1로 이겼어요",
     "Twente won bij Lincoln met... A. 2–0 · B. 4–0 · C. 4–1", size=20, gap=8)
e.ex("B1", "객관식", "A", "NEC는 디나모 자그레브에 2-4로 졌어요",
     "NEC verloor met... A. 2–4 · B. 4–2 · C. 1–0", size=20, gap=8)
e.ex("B1", "객관식", "B", "레알 베티스가 페예노르트를 1-0으로 이겼어요",
     "Real Betis – Feyenoord eindigde... A. 0–0 · B. 1–0 · C. 0–1", size=20, gap=8)
e.ex("B1", "객관식", "B", "10라운드 뒤 페예노르트가 24점으로 선두예요",
     "Na 10 ronden staat Feyenoord... A. tweede · B. eerste met 24 punten · C. derde", size=20, gap=8)
e.head("B　WOORDEN UIT DE TEKST", 25)
e.bridge("네모 안의 단어로 채우세요.")
e.para("balans · gelijkspelen · topper · stand · doelpunt", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "문장 완성", "balans", "balans = 결산",
     "De ___ van de Europese week is: drie keer feest, twee keer verlies.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "speelden gelijk", "gelijkspelen 과거형 복수: speelden gelijk",
     "PSV en Feyenoord ___ (gelijkspelen): 1–1.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "topper", "topper = 빅매치",
     "Heerenveen – Feyenoord is de ___ van zondag.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "stand", "stand = 순위표",
     "Op de ___ staat Feyenoord bovenaan.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "doelpunt", "doelpunt = 골",
     "Isco maakte het enige ___ van Betis – Feyenoord.", instr="빈칸 채우기", size=20, gap=8)
e.head("C　VERLEDEN TIJD", 25)
e.bridge("과거형이나 현재완료로 채우세요.")
e.ex("B1", "문장 완성", "won", "winnen 과거형: won",
     "Ajax ___ (winnen) donderdag met 2–0.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "ging", "gaan 과거형: ging",
     "De bal ___ (gaan) in het doel: 1–0 voor Betis.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "verloor", "verliezen 과거형: verloor",
     "Feyenoord ___ (verliezen) met 1–0 in Sevilla.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B2", "문장 완성", "zijn gekomen", "komen의 perfectum은 zijn을 써요",
     "Veel supporters ___ (komen) naar het stadion.", instr="빈칸 채우기", size=20, gap=8)
e.head("D　WAAR OF NIET WAAR?", 25)
e.ex("B1", "참/거짓 판단", "Waar", "맞아요: 아약스가 2-0으로 이겼어요",
     "Ajax won donderdag met 2–0 van Atalanta. Waar of niet waar?", instr="참 / 거짓", size=20, gap=8)
e.ex("B1", "참/거짓 판단", "Niet waar", "틀렸어요: NEC는 2-4로 졌어요",
     "NEC won met 4–2 bij Dinamo Zagreb. Waar of niet waar?", instr="참 / 거짓", size=20, gap=8)
e.ex("B1", "참/거짓 판단", "Niet waar", "틀렸어요: 트벤테-아약스는 13:30에 시작해요",
     "Twente – Ajax is zondag om 11:15 uur. Waar of niet waar?", instr="참 / 거짓", size=20, gap=8)
e.ex("B1", "참/거짓 판단", "Waar", "맞아요: 10라운드 뒤 페예노르트가 24점으로 1위예요",
     "Feyenoord staat na 10 ronden bovenaan met 24 punten. Waar of niet waar?", instr="참 / 거짓", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
