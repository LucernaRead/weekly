# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · JONGEREN (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JONGEREN · 청소년", "De Lucerna", "NIVEAU B1 · Robinson is begonnen, ADE en DDW voorbij · 로빈슨 시작, ADE와 DDW 폐막")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-main")
f.title("Expeditie Robinson is begonnen!", 37)
f.byline("Van de redactie van De Lucerna · Leesniveau: B1")
f.para("Zondag 1 november begon Expeditie Robinson op RTL 4, om 20:00 uur. Negentien kandidaten leven op een onbewoond eiland. De eerste aflevering is geweest — nu begint het echte spel: vuur maken, eten zoeken, proeven winnen.")
f.para("De kandidaten slapen buiten en moeten alles zelf doen. Wie een proef verliest, kan naar huis worden gestemd. Wie het langst blijft, wint de expeditie. De kandidaten komen uit Nederland en Vlaanderen, en ze kennen elkaar nog niet allemaal.")
f.para("Twee festivals zijn intussen voorbij. ADE en de Dutch Design Week sloten allebei op zondag 25 oktober. ADE werd dertig jaar, met meer dan 3.000 artiesten op meer dan 200 locaties in Amsterdam. De Design Week in Eindhoven toonde werk van ongeveer 2.500 ontwerpers.")
f.para("Wat blijft er over? De muziek van ADE, de ideeën van de Design Week — en de vraag wie Robinson wint. Daarover lees je volgende week meer. En deze week is er genoeg te doen: het is Klimaatweek, dus ga naar buiten, plant iets groens of fiets naar de Snuffelmarkt in Zaandam.")
f.head("JONGEREN EN HET KLIMAAT", 25)
f.para("Jongeren doen veel in de Klimaatweek: fietsen in plaats van rijden, tweedehands kopen in plaats van nieuw, minder plastic gebruiken. Kleine keuzes, zeggen klimaatclubs, maar als miljoenen jongeren ze maken, tellen ze op.")
f.box("ZO KIJK JE ROBINSON", [
    ("1. Kijk zondag om 20:00 uur op RTL 4(일요일 저녁 8시에 RTL 4에서 보세요)", "serif", False, INK, 21, 1.36),
    ("2. Let op de proeven: daar worden de punten verdeeld(미션에 주목하세요: 점수는 거기서 갈려요)", "serif", False, INK, 21, 1.36),
    ("3. Raad met vrienden wie het langst blijft(친구들과 누가 가장 오래 남을지 맞혀 보세요)", "serif", False, INK, 21, 1.36),
    ("4. Volgende week lees je hier hoe het verder ging(다음 주에 여기서 후속 소식을 읽을 수 있어요)", "serif", False, INK, 21, 1.36),
])
f.gloss("het eiland 섬 · de proef 미션 · stemmen 투표하다 · de aflevering (한) 회 · voorbij 끝나다.")
f.end_report()

# col 3: facts + en jij (sequential, measured; no photo this page)
ix = COLX[3]
facts = ["Expeditie Robinson: 19 kandidaten; start zondag 1 november, 20:00 uur, RTL 4.",
         "ADE 30 jaar: meer dan 3.000 artiesten, meer dan 200 locaties; gesloten zondag 25 oktober.",
         "Dutch Design Week: ongeveer 2.500 ontwerpers; gesloten zondag 25 oktober."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "JONGEREN IN CIJFERS", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "En jij? Kijk jij naar Expeditie Robinson, of doe je liever zelf iets buiten? Schrijf twee zinnen in het Nederlands en stuur ze naar de redactie."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("로빈슨을 보세요, 아니면 직접 밖에 나가서 활동하는 쪽이 더 좋아요? 네덜란드어 문장 두 개를 써서 보내 주세요.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "EN JIJ? · 여러분은요", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "로빈슨을 보세요, 아니면 직접 밖에 나가서 활동하는 쪽이 더 좋아요? 네덜란드어 문장 두 개를 써서 보내 주세요.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "OEFENINGEN · 5면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면 · 문제는 수준이 섞여 있어요, 번호로 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · BEGRIJPEN", 25)
e.bridge("5면 기사를 읽고 정답을 고르세요.")
e.ex("B1", "객관식", "B", "로빈슨은 11월 1일 일요일에 시작했어요",
     "Expeditie Robinson begon op... A. zondag 25 oktober · B. zondag 1 november · C. woensdag 21 oktober", size=20, gap=8)
e.ex("B1", "객관식", "A", "참가자는 19명이에요",
     "Expeditie Robinson heeft ___ kandidaten. A. 19 · B. 30 · C. 200", size=20, gap=8)
e.ex("B1", "객관식", "C", "ADE는 올해 30주년이에요",
     "ADE werd dit jaar... A. 25 jaar · B. 26 jaar · C. 30 jaar", size=20, gap=8)
e.ex("B1", "객관식", "B", "디자인 위크에는 약 2,500명의 디자이너가 참여했어요",
     "De Design Week toonde werk van ongeveer... A. 250 ontwerpers · B. 2.500 ontwerpers · C. 3.000 ontwerpers", size=20, gap=8)
e.ex("B1", "객관식", "A", "ADE와 디자인 위크는 10월 25일 일요일에 끝났어요",
     "ADE en de Design Week sloten op... A. zondag 25 oktober · B. zondag 1 november · C. zaterdag 7 november", size=20, gap=8)
e.head("B · WOORDEN UIT DE TEKST", 25)
e.bridge("네모 안의 단어로 채우세요.")
e.para("eiland · proef · stemmen · aflevering · voorbij · kandidaat", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "문장 완성", "eiland", "eiland = 섬(중성 명사)",
     "Robinson speelt op een onbewoond ___.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "proef", "proef = 미션(여성 명사)",
     "Wie een ___ verliest, kan naar huis gaan.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "stemmen", "stemmen = 투표하다",
     "De kandidaten ___ wie naar huis moet.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "aflevering", "aflevering = (한) 회",
     "De eerste ___ was zondag 1 november.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "voorbij", "voorbij = 끝났어요",
     "ADE is ___: het festival is afgelopen.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "kandidaten", "kandidaat 복수형: kandidaten",
     "Er zijn 19 ___ op het eiland.", instr="빈칸 채우기", size=20, gap=8)
e.head("C · DE TOEKOMST MET GAAN", 25)
e.bridge("gaan + 부정사로 미래를 말하세요.")
e.ex("B1", "문장 완성", "gaat winnen", "gaat winnen = 이길 거예요(그냥 추측이에요)",
     "Wie ___ (winnen) Expeditie Robinson, denk je?", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "gaan kijken", "wij → gaan + 부정사 kijken",
     "Wij ___ (kijken) zondag naar de nieuwe aflevering.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "gaat praten", "hij → gaat praten",
     "Hij ___ (praten) morgen met vrienden over de proef.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "gaan zoeken", "zij(복수) → gaan zoeken",
     "De kandidaten ___ (zoeken) morgen eten op het eiland.", instr="빈칸 채우기", size=20, gap=8)
e.head("D · WAAR OF NIET WAAR?", 25)
e.ex("B1", "참/거짓 판단", "Waar", "맞아요: 11월 1일에 시작했어요",
     "Expeditie Robinson begon op 1 november. Waar of niet waar?", instr="참 / 거짓", size=20, gap=8)
e.ex("B1", "참/거짓 판단", "Niet waar", "틀렸어요: ADE는 올해 30주년이에요",
     "ADE werd dit jaar 26 jaar. Waar of niet waar?", instr="참 / 거짓", size=20, gap=8)
e.ex("B2", "참/거짓 판단", "Niet waar", "틀렸어요: 10월 25일에 이미 끝났어요",
     "De Design Week is nog bezig. Waar of niet waar?", instr="참 / 거짓", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jongeren.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · VERDIEPING (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("VERDIEPING · 심층", "De Lucerna", "NIVEAU B2 · De codes van het KNMI · KNMI 경보 코드 심층 해설")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P6-main")
f.title("Geel, oranje, rood: hoe werken de codes?", 37)
f.byline("Van de redactie van De Lucerna · Leesniveau: B2")
f.para("Het KNMI waarschuwt Nederland al jaren met kleuren. Maar de waarschuwingen zijn veranderd: vroeger golden ze voor een hele provincie, nu zijn ze lokaal. Dat betekent: jouw stad kan code oranje hebben, terwijl het twintig kilometer verderop rustig is.")
f.para("Waarom lokaal? Omdat het weer lokaal is. Een zware bui kan over één stad vallen en de buurstad overslaan. Een waarschuwing voor een hele provincie waarschuwt dan mensen die niets merken — en die letten de volgende keer minder op. Meteorologen noemen dat waarschuwingsmoeheid.")
f.para("De kleuren zelf zijn simpel. Geel: het weer kan gevaarlijk zijn, let op. Oranje: het weer ís gevaarlijk, bereid je voor — zet losse spullen vast, rijd voorzichtig. Rood: het weer is zeer gevaarlijk, ga niet de weg op als het niet moet. Rood komt weinig voor.")
f.para("Het systeem heeft ook kritiek: sommige mensen vinden de codes verwarrend — wat is het verschil tussen geel en oranje als je toch naar buiten moet? Het KNMI antwoordt: kijk altijd naar de tekst bij de code, niet alleen naar de kleur. De tekst zegt wat er écht gebeurt, waar en wanneer.")
f.para("Voor jou als lezer is de les duidelijk. Een code is geen verbod, maar een advies. Lees de waarschuwing, kijk naar je eigen plaats en beslis zelf. En in de Klimaatweek past dat goed. Het weer is van ons allemaal, maar het raakt ons allemaal anders.")
f.head("VOOR OF TEGEN LOKAAL?", 25)
f.para("Voorstanders zeggen: lokaal is eerlijker, want alleen wie het treft, wordt gewaarschuwd. Tegenstanders zeggen: lokaal is verwarrend, want de buurstad heeft een andere kleur. Het KNMI houdt vast aan lokaal: beter precies dan algemeen, zeggen de meteorologen.")
f.gloss("de meteoroloog 기상학자 · waarschuwingsmoeheid 경보 피로 · vastzetten 고정하기 · het advies 조언 · de voorstander 찬성론자.")
f.end_report()

# col 3: OEFENDATA chart + pro/contra box (sequential, measured)
ix = COLX[3]
rows = [
    ("Ik blijf thuis", "45", 180),
    ("Ik kijk eerst naar de tekst", "25", 100),
    ("Ik ga toch naar buiten", "20", 80),
    ("Ik weet het niet", "10", 40),
]
cap = "OEFENDATA — verzonnen cijfers om mee te oefenen, geen echte enquête. Vraag: wat doe jij bij code oranje? (100 jongeren)"
capcn = "연습용 데이터예요: 가상의 숫자라서 실제 설문 조사가 아니에요. 질문: 주황색 경보 때 어떻게 할 거예요? (젊은이 100명)"
ch = 62 + len(rows) * 58 + 14 + len(wrap(cap, "serif", False, 19, CW - 44)) * 27 + 6 + len(wrap(capcn, "sans", False, 18.5, CW - 44)) * 26 + 18
p.rect(ix, 200, CW, ch, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(ix + 22, yy3 + 26, "DE GRAFIEK · 그래프(연습용 데이터)", 24, "sans", True, OLIVE)
yy3 += 58
for lab, val, bw in rows:
    p.text(ix + 22, yy3 + 20, lab, 19.5, "serif", True, INK)
    p.text(ix + CW - 22, yy3 + 20, val, 19.5, "sans", True, BRICK, anchor="end")
    p.rect(ix + 22, yy3 + 30, bw, 18, fill=OLIVE)
    yy3 += 58
yy3 += 14
yy3 = p.para(ix + 22, yy3 + 19, cap, 19, "serif", False, GREY, CW - 44, 1.36)
yy3 = p.para(ix + 22, yy3 + 18.5, capcn, 18.5, "sans", False, GREY, CW - 44, 1.32) + 6
print("P6 chart ends", 200 + ch, "content to", yy3)
by6 = 200 + ch + 26
bt = [
    ("Voor lokaal: alleen wie het treft, wordt gewaarschuwd.", "serif", False, INK, 21, 1.4),
    ("Tegen lokaal: de buurstad heeft een andere kleur — verwarrend.", "serif", False, INK, 21, 1.4),
    ("De krant kiest niet: lees de tekst bij de code, niet alleen de kleur. En jij?", "serif", False, INK, 21, 1.4),
]
bh = 62 + sum(len(wrap(t, "serif", False, 21, CW - 44)) * 29.5 + 8 for t, *_ in bt) + 16 + 30
p.rect(ix, by6, CW, bh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = by6 + 16
p.text(ix + 22, yy3 + 26, "VOOR OF TEGEN? · 찬반 토론", 21, "sans", True, OLIVE)
yy3 += 52
for t, k, b, fl, s, lh in bt:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21, "serif", False, INK, CW - 44, 1.4) + 8
print("P6 col3 ends", by6 + bh)

# ---- P6 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "OEFENINGEN · 6면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면 · 문제는 수준이 섞여 있어요, 번호로 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · LEES DE GRAFIEK", 25)
e.bridge("6면 그래프(연습용 데이터)를 보고 답하세요.")
e.ex("B2", "문장 완성", "45", "45명의 젊은이가 집에 머무르기로 했어요",
     "Bij code oranje blijft ___ van de 100 jongeren thuis.", instr="빈칸 채우기", size=21.5, gap=9)
e.ex("B2", "문장 완성", "25", "25명은 먼저 경보 글을 읽어 봐요",
     "___ jongeren kijken eerst naar de tekst.", instr="빈칸 채우기", size=21.5, gap=9)
e.ex("B2", "문장 완성", "70", "45 + 25 = 70",
     "Thuis blijven en eerst de tekst lezen samen: ___ jongeren.", instr="빈칸 채우기", size=21.5, gap=9)
e.ex("B2", "문장 완성", "10", "10명은 모르겠다고 했어요",
     "___ jongeren weten het niet.", instr="빈칸 채우기", size=21.5, gap=9)
e.ex("B2", "문장 완성", "100", "그래프 전체 100명: 45+25+20+10",
     "De grafiek telt in totaal ___ jongeren.", instr="빈칸 채우기", size=21.5, gap=9)
e.head("B · BEGRIJPEN", 25)
e.bridge("6면 기사를 읽고 정답을 고르세요.")
e.ex("B2", "객관식", "B", "예전에는 경보가 한 주 전체를 대상으로 했어요",
     "Vroeger golden waarschuwingen voor... A. één stad · B. een hele provincie · C. het hele land", size=21.5, gap=9)
e.ex("B2", "객관식", "B", "요즘 경보는 지역 단위예요",
     "Tegenwoordig zijn waarschuwingen... A. voor het hele land · B. lokaal · C. alleen voor de kust", size=21.5, gap=9)
e.ex("B2", "객관식", "C", "빨간색: 매우 위험해요, 꼭 필요하지 않으면 외출하지 마세요",
     "Code rood betekent... A. let op · B. bereid je voor · C. zeer gevaarlijk, ga niet de weg op", size=21.5, gap=9)
e.ex("B2", "객관식", "A", "경보 피로: 경보가 너무 많아서 주의를 덜 기울이게 돼요",
     "Waarschuwingsmoeheid is... A. moe van waarschuwingen, dus minder opletten · B. moe van het weer · C. een nieuwe code", size=21.5, gap=9)
e.ex("B2", "객관식", "B", "KNMI는 코드 옆의 글자를 보라고 해요",
     "Het KNMI zegt: kijk niet alleen naar de kleur, maar naar... A. de wind · B. de tekst bij de code · C. de televisie", size=21.5, gap=9)
e.head("C · WOORDEN", 25)
e.bridge("네모 안의 단어로 채우세요.")
e.para("lokaal · waarschuwingsmoeheid · vastzetten · advies", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B2", "문장 완성", "lokaal", "lokaal = 현지의",
     "De waarschuwing geldt voor jouw eigen stad: ze is ___.", instr="빈칸 채우기", size=21.5, gap=9)
e.ex("B2", "문장 완성", "waarschuwingsmoeheid", "waarschuwingsmoeheid = 경보 피로",
     "Wie te vaak onnodig wordt gewaarschuwd, krijgt ___.", instr="빈칸 채우기", size=21.5, gap=9)
e.ex("B2", "문장 완성", "vastzetten", "vastzetten = 고정하기",
     "Bij code oranje moet je losse spullen ___.", instr="빈칸 채우기", size=21.5, gap=9)
e.ex("B2", "문장 완성", "advies", "advies = 조언(중성 명사)",
     "Een code is geen verbod, maar een ___.", instr="빈칸 채우기", size=21.5, gap=9)
e.head("D · MAAK DE ZINNEN", 25)
e.bridge("단어를 모아 올바른 문장을 만드세요.")
e.ex("B2", "문장 만들기", "De waarschuwing geldt voor jouw stad.", "주어 + 동사 + 장소",
     "de waarschuwing / geldt / voor jouw stad → ___", instr="문장 만들기", size=21.5, gap=9)
e.ex("B2", "문장 만들기", "Kijk altijd naar de tekst bij de code.", "명령문: 동사가 앞에 와요",
     "kijk / altijd / naar de tekst / bij de code → ___", instr="문장 만들기", size=21.5, gap=9)
e.ex("B2", "문장 만들기", "Rood komt weinig voor.", "weinig voor = 좀처럼 나타나지 않다",
     "rood / komt / weinig / voor → ___", instr="문장 만들기", size=21.5, gap=9)
e.ex("B2", "문장 만들기", "Het weer raakt ons allemaal anders.", "raakt + 목적어 + 방식",
     "het weer / raakt / ons / allemaal anders → ___", instr="문장 만들기", size=21.5, gap=9)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-verdieping.svg")
print("P6 saved, exercises so far:", len(REG))
