# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · JONGEREN (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JONGEREN　청소년", "De Lucerna", "NIVEAU B1　Robinson, de schoen en het verlanglijstje　로빈슨, 신발과 소원 목록")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-main")
f.title("Robinson op zondag — en de schoen staat klaar", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: B1")
f.para("Elke zondag om 20:00 uur is Expeditie Robinson te zien op RTL 4. Negentien bekende Nederlanders en Vlamingen leven 34 dagen op een onbewoond eiland in Maleisië. Nicolette Kluijver en Edson da Graça presenteren het programma, Camille Vanuxem is de verslaggever.")
f.para("De kandidaten slapen buiten en moeten alles zelf doen: vuur maken, eten zoeken, proeven winnen. Wie een proef verliest, kan naar huis worden gestemd. Wie het langst blijft, wint de expeditie. Het seizoen begon op zondag 1 november — en elke week wordt het spel harder.")
f.para("Deze week is zondag 15 november een drukke dag: overdag de intocht in Amsterdam, 's avonds een nieuwe aflevering van Robinson. En na de intocht mag de schoen. Ook jongeren zetten hun schoen — met een verlanglijstje erin, in plaats van alleen een tekening.")
f.para("Een verlanglijstje schrijven is ook Nederlands oefenen: schrijf in het Nederlands wat je wilt, waarom je het wilt en voor wie je het nog meer opschrijft. Sinterklaas leest Nederlands, zeggen kinderen — en de redactie ook.")
f.head("JONGEREN EN DE SCHOEN", 25)
f.para("De schoen zetten is niet alleen voor kleine kinderen. Jongeren zetten hun schoen met een wortel voor het paard, een tekening — of een verlanglijstje met drie wensen. Klein of groot, een wens op papier is het begin van Sinterklaas.")
f.box("ZO KIJK JE ROBINSON", [
    ("1. Kijk zondag om 20:00 uur op RTL 4 (일요일 20:00에 RTL 4에서 봐요)", "serif", False, INK, 21, 1.36),
    ("2. Let op de proeven: daar worden de punten verdeeld (트라이얼을 봐요: 점수는 거기서 결정돼요)", "serif", False, INK, 21, 1.36),
    ("3. Raad met vrienden wie het langst blijft (친구들과 누가 가장 오래 남을지 맞춰 봐요)", "serif", False, INK, 21, 1.36),
    ("4. Zet daarna je schoen: met een verlanglijstje erin (그다음에는 소원 목록을 넣은 신발을 내놓아요)", "serif", False, INK, 21, 1.36),
])
f.gloss("het verlanglijstje 소원 목록 · de verslaggever 리포터 · de proef 트라이얼, 도전 · stemmen 투표하다 · de aflevering 회차.")
f.end_report()

# col 3: facts + en jij (sequential, measured; no photo this page)
ix = COLX[3]
facts = ["Expeditie Robinson: 19 kandidaten; elke zondag 20:00 uur, RTL 4.",
         "34 dagen op een onbewoond eiland in Maleisië; presentatie: Nicolette Kluijver en Edson da Graça.",
         "Na de intocht (15 november) mag de schoen, met een wortel en een verlanglijstje."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 64
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "JONGEREN IN CIJFERS", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "En jij? Kijk jij zondag naar Expeditie Robinson, of zet je liever je schoen met een verlanglijstje? Schrijf twee zinnen in het Nederlands en stuur ze naar de redactie."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("일요일에는 Expeditie Robinson을 봐요, 아니면 소원 목록을 넣은 신발을 내놓을래요? 네덜란드어로 두 문장을 써서 보내 주세요.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "EN JIJ?　여러분은요?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "일요일에는 Expeditie Robinson을 봐요, 아니면 소원 목록을 넣은 신발을 내놓을래요? 네덜란드어로 두 문장을 써서 보내 주세요.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "OEFENINGEN　5면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면　문제는 수준이 섞여 있어요, 번호로 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A　BEGRIJPEN", 25)
e.bridge("5면 기사를 읽고 정답을 고르세요.")
e.ex("B1", "객관식", "B", "로빈슨은 매주 일요일 20:00에 RTL 4에서 방송해요",
     "Expeditie Robinson is elke zondag om... A. 18:00 uur · B. 20:00 uur · C. 12:00 uur", size=20, gap=8)
e.ex("B1", "객관식", "A", "참가자 19명",
     "Expeditie Robinson heeft ___ kandidaten. A. 19 · B. 34 · C. 88", size=20, gap=8)
e.ex("B1", "객관식", "C", "이 프로그램은 말레이시아의 무인도에서 촬영해요",
     "De kandidaten leven op een eiland in... A. Spanje · B. Grave · C. Maleisië", size=20, gap=8)
e.ex("B1", "객관식", "B", "참가자들은 섬에서 34일을 보내요",
     "De kandidaten blijven ___ dagen op het eiland. A. 19 · B. 34 · C. 88", size=20, gap=8)
e.ex("B1", "객관식", "A", "소원 목록은 신발 안에 들어가요",
     "Jongeren zetten hun schoen met... A. een verlanglijstje · B. een boek · C. een lampion", size=20, gap=8)
e.head("B　WOORDEN UIT DE TEKST", 25)
e.bridge("상자 속 단어로 채우세요.")
e.para("verlanglijstje · verslaggever · proef · stemmen · aflevering · kandidaat", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "문장 완성", "verlanglijstje", "verlanglijstje = 소원 목록 (het)",
     "In mijn schoen zit een ___ met drie wensen.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "verslaggever", "verslaggever = 리포터 (de)",
     "Camille Vanuxem is de ___ van het programma.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "proef", "proef = 트라이얼, 도전 (de)",
     "Wie een ___ verliest, kan naar huis gaan.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "stemmen", "stemmen = 투표하다",
     "De kandidaten ___ wie naar huis moet.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "aflevering", "aflevering = 회차",
     "Zondag is er een nieuwe ___ van Robinson.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "kandidaten", "kandidaat 복수형: kandidaten",
     "Er zijn 19 ___ op het eiland.", instr="빈칸 채우기", size=20, gap=8)
e.head("C　DE TOEKOMST MET GAAN", 25)
e.bridge("gaan + 부정사로 미래에 대해 말해 보세요.")
e.ex("B1", "문장 완성", "gaat winnen", "gaat winnen = 이길 거예요(그냥 추측)",
     "Wie ___ (winnen) Expeditie Robinson, denk je?", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "gaan kijken", "wij → gaan + 부정사 kijken",
     "Wij ___ (kijken) zondag naar de nieuwe aflevering.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "gaat zetten", "hij → gaat zetten",
     "Hij ___ (zetten) zondagavond zijn schoen.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "gaan schrijven", "zij (복수) → gaan schrijven",
     "De kinderen ___ (schrijven) een verlanglijstje.", instr="빈칸 채우기", size=20, gap=8)
e.head("D　WAAR OF NIET WAAR?", 25)
e.ex("B1", "참/거짓 판단", "Waar", "참: 이 프로그램은 11월 1일에 시작했어요",
     "Expeditie Robinson begon op 1 november. Waar of niet waar?", instr="참 / 거짓", size=20, gap=8)
e.ex("B1", "참/거짓 판단", "Niet waar", "거짓: 이 프로그램은 말레이시아에서 촬영해요",
     "Expeditie Robinson speelt in Spanje. Waar of niet waar?", instr="참 / 거짓", size=20, gap=8)
e.ex("B2", "참/거짓 판단", "Niet waar", "거짓: 신발 속 당근은 말을 위한 거예요",
     "De wortel in de schoen is voor Sinterklaas. Waar of niet waar?", instr="참 / 거짓", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jongeren.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · VERDIEPING (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("VERDIEPING　심층", "De Lucerna", "NIVEAU B2　Sint-Maarten of Halloween?　성 마르틴의 날이냐, 핼러윈이냐?")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P6-main")
f.title("Sint-Maarten of Halloween: moet je kiezen?", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: B2")
f.para("Sint-Maarten is een oude traditie in Nederland. Kinderen lopen al meer dan honderd jaar met lampionnen langs de deuren. Halloween is nieuwer in Nederland — en het groeit: volgens onderzoeksbureau Motivaction vierde in 2025 26 procent van de Nederlanders Halloween, tegenover 21 procent een jaar eerder.")
f.para("Maar let op de cijfers: de onderzoeken gebruiken verschillende definities en zijn daarom niet rechtstreeks vergelijkbaar. En een lege stoep betekent niet automatisch dat Sint-Maarten verdwijnt. In sommige plaatsen verplaatst de viering zich naar winkelcentra en georganiseerde optochten, waar kinderen samen langs deelnemende winkels lopen.")
f.para("Deskundigen zien Sint-Maarten niet verdwijnen. Antropoloog Irene Stengs van het Meertens Instituut zei in 2025 dat de belangstelling voor Sint-Maarten is toegenomen. Traditiedeskundige Ineke Strouken ziet geen duidelijke landelijke achteruitgang. Het feest verandert, zeggen zij — het verdwijnt niet.")
f.para("De twee feesten zijn ook anders. Halloween draait om griezelen en verkleden; Sint-Maarten draait om delen en aandacht voor anderen. Veel kinderen doen allebei: griezelen op 31 oktober, zingen op 11 november. Kiezen hoeft niet — het zijn twee feesten, in twee weken, met twee soorten licht.")
f.para("Een traditie leeft als mensen haar blijven vieren. Op straat, in het winkelcentrum of allebei: de lampion gaat aan als het donker wordt, en het liedje klinkt bij elke deur.")
f.head("VOOR OF TEGEN KIEZEN?", 25)
f.para("Voorstanders van kiezen zeggen: één feest is genoeg, anders wordt november één lange verkleedweek. Tegenstanders zeggen: feesten groeien naast elkaar, zoals talen naast elkaar groeien. De krant kiest niet: vier wat je viert — maar zing op 11 november in ieder geval één liedje.")
f.gloss("de traditie 전통 · griezelen 무섭게 하다 · de belangstelling 관심 · de achteruitgang 쇠퇴 · de deskundige 전문가.")
f.end_report()

# col 3: OEFENDATA chart + pro/contra box (sequential, measured)
ix = COLX[3]
rows = [
    ("Ik loop met een lampion", "40", 160),
    ("Ik vier Halloween", "25", 100),
    ("Ik doe allebei", "20", 80),
    ("Ik blijf thuis", "15", 60),
]
cap = "OEFENDATA — verzonnen cijfers om mee te oefenen, geen echte enquête. Vraag: wat doe jij rond 11 november? (100 jongeren)"
capcn = "연습용 데이터: 연습용으로 만든 숫자예요, 실제 조사가 아니에요. 질문: 11월 11일 즈음에 무엇을 해요? (청소년 100명)"
ch = 62 + len(rows) * 58 + 14 + len(wrap(cap, "serif", False, 19, CW - 44)) * 27 + 6 + len(wrap(capcn, "sans", False, 18.5, CW - 44)) * 26 + 18
p.rect(ix, 200, CW, ch, fill=BOX)
yy3 = 216
p.text(ix + 22, yy3 + 26, "DE GRAFIEK　그래프(연습용 데이터)", 24, "sans", True, OLIVE)
yy3 += 58
for lab, val, bw in rows:
    p.text(ix + 22, yy3 + 20, lab, 19.5, "serif", True, INK)
    p.text(ix + CW - 22, yy3 + 20, val, 19.5, "sans", True, OLIVE, anchor="end")
    p.rect(ix + 22, yy3 + 30, bw, 18, fill=OLIVE)
    yy3 += 58
yy3 += 14
yy3 = p.para(ix + 22, yy3 + 19, cap, 19, "serif", False, GREY, CW - 44, 1.36)
yy3 = p.para(ix + 22, yy3 + 18.5, capcn, 18.5, "sans", False, GREY, CW - 44, 1.32) + 6
print("P6 chart ends", 200 + ch, "content to", yy3)
by6 = 200 + ch + 26
bt = [
    ("Voor kiezen: één feest is genoeg in november.", "serif", False, INK, 21, 1.4),
    ("Tegen kiezen: feesten groeien naast elkaar, zoals talen.", "serif", False, INK, 21, 1.4),
    ("De krant kiest niet: vier wat je viert. En zing op 11 november één liedje. En jij?", "serif", False, INK, 21, 1.4),
]
bh = 62 + sum(len(wrap(t, "serif", False, 21, CW - 44)) * 29.5 + 8 for t, *_ in bt) + 16 + 30
p.rect(ix, by6, CW, bh, fill="#f0eee5")
yy3 = by6 + 16
p.text(ix + 22, yy3 + 26, "VOOR OF TEGEN?　찬반 토론", 21, "sans", True, OLIVE)
yy3 += 52
for t, k, b, fl, s, lh in bt:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21, "serif", False, INK, CW - 44, 1.4) + 8
print("P6 col3 ends", by6 + bh)

# ---- P6 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "OEFENINGEN　6면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면　문제는 수준이 섞여 있어요, 번호로 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A　LEES DE GRAFIEK", 25)
e.bridge("6면 그래프(연습용 데이터)에서 답하세요.")
e.ex("B2", "문장 완성", "40", "청소년 40명이 등롱을 들고 걸어요",
     "___ van de 100 jongeren lopen met een lampion.", instr="빈칸 채우기", size=21.5, gap=9)
e.ex("B2", "문장 완성", "25", "25명이 핼러윈을 기념해요",
     "___ jongeren vieren Halloween.", instr="빈칸 채우기", size=21.5, gap=9)
e.ex("B2", "문장 완성", "60", "40 + 20 = 60",
     "Lampion lopen en allebei samen: ___ jongeren.", instr="빈칸 채우기", size=21.5, gap=9)
e.ex("B2", "문장 완성", "15", "15명은 집에 있어요",
     "___ jongeren blijven thuis.", instr="빈칸 채우기", size=21.5, gap=9)
e.ex("B2", "문장 완성", "100", "그래프는 100명을 세요: 40+25+20+15",
     "De grafiek telt in totaal ___ jongeren.", instr="빈칸 채우기", size=21.5, gap=9)
e.head("B　BEGRIJPEN", 25)
e.bridge("6면 기사를 읽고 정답을 고르세요.")
e.ex("B2", "객관식", "B", "2025년에는 네덜란드 사람의 26%가 핼러윈을 기념했어요",
     "Volgens Motivaction vierde in 2025 ___ procent Halloween. A. 21 · B. 26 · C. 11", size=21.5, gap=9)
e.ex("B2", "객관식", "B", "두 조사는 정의가 달라서 직접 비교할 수 없어요",
     "De onderzoeken zijn... A. precies hetzelfde · B. niet rechtstreeks vergelijkbaar · C. allebei fout", size=21.5, gap=9)
e.ex("B2", "객관식", "C", "성 마르틴의 날에 대한 관심이 늘었어요(Stengs, 2025년)",
     "Irene Stengs zei in 2025 dat de belangstelling voor Sint-Maarten... A. verdween · B. gelijk bleef · C. is toegenomen", size=21.5, gap=9)
e.ex("B2", "객관식", "A", "핼러윈은 무섭게 하는 것이고, 성 마르틴의 날은 나누는 것이에요",
     "Halloween draait om griezelen; Sint-Maarten draait om... A. delen · B. voetbal · C. boeken", size=21.5, gap=9)
e.ex("B2", "객관식", "B", "전통은 사람들이 계속 기념할 때 살아남아요",
     "Een traditie leeft als... A. ze oud is · B. mensen haar blijven vieren · C. ze op televisie is", size=21.5, gap=9)
e.head("C　WOORDEN", 25)
e.bridge("상자 속 단어로 채우세요.")
e.para("traditie · griezelen · belangstelling · achteruitgang", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B2", "문장 완성", "traditie", "traditie = 전통 (de)",
     "Sint-Maarten is een oude ___.", instr="빈칸 채우기", size=21.5, gap=9)
e.ex("B2", "문장 완성", "griezelen", "griezelen = 무섭게 하다",
     "Met Halloween gaan kinderen ___ en zich verkleden.", instr="빈칸 채우기", size=21.5, gap=9)
e.ex("B2", "문장 완성", "belangstelling", "belangstelling = 관심 (de)",
     "De ___ voor Sint-Maarten is toegenomen.", instr="빈칸 채우기", size=21.5, gap=9)
e.ex("B2", "문장 완성", "achteruitgang", "achteruitgang = 쇠퇴 (de)",
     "Strouken ziet geen duidelijke landelijke ___.", instr="빈칸 채우기", size=21.5, gap=9)
e.head("D　MAAK DE ZINNEN", 25)
e.bridge("단어를 올바른 순서로 배열해 문장을 만드세요.")
e.ex("B2", "문장 만들기", "Sint-Maarten is een oude traditie in Nederland.", "주어·동사·보어·장소",
     "sint-maarten / is / een oude traditie / in nederland → ___", instr="문장 만들기", size=21.5, gap=9)
e.ex("B2", "문장 만들기", "De kinderen lopen met lampionnen langs de deuren.", "주어 + 동사 + 양태 + 장소",
     "de kinderen / lopen / met lampionnen / langs de deuren → ___", instr="문장 만들기", size=21.5, gap=9)
e.ex("B2", "문장 만들기", "Een traditie leeft als mensen haar blijven vieren.", "als 절은 마지막에 와요",
     "een traditie / leeft / als mensen haar blijven vieren → ___", instr="문장 만들기", size=21.5, gap=9)
e.ex("B2", "문장 만들기", "Kiezen hoeft niet: het zijn twee feesten.", "kiezen + hoeft niet + 설명",
     "kiezen / hoeft niet / het zijn twee feesten → ___", instr="문장 만들기", size=21.5, gap=9)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-verdieping.svg")
print("P6 saved, exercises so far:", len(REG))
