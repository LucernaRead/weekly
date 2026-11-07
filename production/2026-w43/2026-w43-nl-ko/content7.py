# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-nl-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · TAAL (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("TAAL · 언어", "De Lucerna", "언어 집중 · Drie niveaus, drie gereedschappen · 세 단계, 세 가지 도구")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · DE KLOK EN HOE LAAT", 24)
a.para("Vraag: «Hoe laat is het?» Antwoord met kwart en half: kwart over twee (02:15), half drie (02:30), kwart voor drie (02:45). Let op: half drie is half vóór drie — dus half vóór het hele uur.", 21.5)
a.para("En de klok verzetten: in oktober gaat hij achteruit, in het voorjaar vooruit. Eén uur maar — maar iedereen praat erover.", 21.5)
a.expl("hoe laat는 시간을 묻는 말; half drie는 2:30이에요(세 시 반 시간 전); 10월에는 뒤로, 봄에는 앞으로 돌려요.")
a.ex("A2", "문장 완성", "kwart over drie", "kwart over drie = 3:15",
     "03:15 is ___.", instr="빈칸 채우기", size=20.5, gap=10)
a.ex("A2", "문장 완성", "half vier", "half vier = 3:30",
     "03:30 is ___.", instr="빈칸 채우기", size=20.5, gap=10)
a.ex("A2", "객관식", "B", "half vijf = 4:30(함정 문제)",
     "«Half vijf» is... A. 05:30 · B. 04:30 · C. 04:45", size=20.5, gap=10)
a.ex("A2", "문장 완성", "achteruit", "10월에는 시계를 뒤로 돌려요",
     "In oktober gaat de klok ___.", instr="빈칸 채우기", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · VAKANTIE EN VRIJE TIJD", 24)
b.para("In de herfstvakantie gaan families eropuit: naar een museum, het bos of een andere stad. En thuis bijslapen hoort er ook bij: een uur extra in bed is ook vakantie.", 21.5)
b.para("Werkwoorden van de week: eropuit gaan (ging, gegaan) en bijslapen (sliep bij, bijgeslapen). Let op: bijslapen is scheidbaar — «ik sliep zondag lekker bij».", 21.5)
b.expl("eropuit gaan 나들이 가다; bijslapen 부족한 잠 보충하기, 분리 동사예요: ik sliep bij.")
b.ex("B1", "문장 완성", "eropuit", "eropuit = 나들이 가다",
     "In de vakantie gaan wij ___: naar het bos en een museum.", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "문장 완성", "bijgeslapen", "bijslapen의 분사형: bijgeslapen",
     "Zondag heb ik lekker ___ (bijslapen).", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "문장 완성", "gingen", "gaan 과거 복수형: gingen",
     "Gisteren ___ (gaan) wij naar Eindhoven.", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "객관식", "A", "bijslapen = 부족한 잠 보충하기",
     "«Bijslapen» betekent... A. extra slapen om uit te rusten · B. vroeg opstaan · C. buiten slapen", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · RUZIE EN MENINGEN", 24)
c.para("Televisie geeft woorden voor ruzie: «een ruzie hebben met iemand», «het ergens niet mee eens zijn». Een sterke, informele zin is: «Dat slaat nergens op!» Dat betekent: dat is onzin. Gebruik hem voorzichtig — hij is informeel.", 21.5)
c.para("Een mening beleefd geven doe je zo: «Ik vind dat ...», «Volgens mij ...» of «Het lijkt me dat ...» Zo praat je mee over De Hanslers én over de klok.", 21.5)
c.expl("ruzie 다툼; slaat nergens op는 \"말도 안 돼요\"라는 구어 표현, 조심해서 쓰세요; Ik vind dat…는 공손하게 의견을 말하는 법이에요.")
c.ex("B2", "문장 완성", "ruzie", "ruzie = 다툼(de)",
     "Monique en Mike hebben ___ in de serie.", instr="빈칸 채우기", size=20.5, gap=10)
c.ex("B2", "객관식", "B", "Volgens mij…는 공손한 시작이에요",
     "Je begint je mening beleefd met... A. Dat slaat nergens op! · B. Volgens mij is dat goed. · C. Ruzie!", size=20.5, gap=10)
c.ex("B2", "문장 완성", "onzin", "onzin = 헛소리, 말도 안 되는 것",
     "«Dat slaat nergens op» betekent: dat is ___.", instr="빈칸 채우기", size=20.5, gap=10)
c.ex("B2", "문장 완성", "eens", "het eens zijn met iemand = 누군가에게 동의하다",
     "Ik ben het helemaal met je ___.", instr="빈칸 채우기", size=20.5, gap=10)
c.end_report()

# ---- col 3: pas op + het woord + brieven ----
bx = COLX[3]
errs = [
    ("«Half drie is 03:30.»", "→ Fout: half drie is 02:30. «Half» is vóór het uur, niet erna.", "half drie는 2:30이에요: half는 정각 앞이에요."),
    ("«De klok gaat voorruit.»", "→ «Vooruit» is één woord — en in oktober gaat de klok achteruit.", "vooruit는 한 단어예요; 그리고 10월에는 뒤로 돌려요."),
    ("«Ik loop naar de huisje.»", "→ Altijd «het» bij verkleinwoorden: «het huisje».", "지소형은 언제나 het를 써요: het huisje."),
    ("«Ik blijf thuis, omdat ik heb geen tijd.»", "→ Na «omdat» staat het werkwoord aan het einde: «... geen tijd heb.»", "omdat 절에서는 동사가 문장 끝으로 가요."),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 192
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "PAS OP! · 실수 클리닉", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 18
wt = "«eropuit» betekent: het huis uit gaan om iets leuks te doen — naar een museum, het bos of een festival. In de herfstvakantie gaat heel Nederland eropuit."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("eropuit = 나들이 가기: 박물관, 숲이나 축제에 가는 거예요.", "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "HET WOORD · 이번 주 단어", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "eropuit = 나들이 가기: 박물관, 숲이나 축제에 가는 거예요.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 18
lt = "«Hallo! Ik ben Chen en ik leer Nederlands in Beijing. In oktober slaap ik één uur langer — net als jullie!» — Chen (voorbeeldbrief van de redactie)"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("편집부가 만든 예시 편지예요, 실제 편지가 아니에요. VOL.2에는 실제 독자 편지와 8면 최고의 글을 실어요!", "sans", False, 20, CW - 44)) * 29 + 34
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "BRIEVEN VAN LEZERS", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "편집부가 만든 예시 편지예요, 실제 편지가 아니에요. VOL.2에는 실제 독자 편지와 8면 최고의 글을 실어요!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- zinnen van de week (verbatim from this issue) ----
fy = 1712
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "ZINNEN VAN DE WEEK · 이번 주 문장(이번호 기사에서 그대로)", 27, "sans", True, OLIVE)
quotes = [
    ("«De wintertijd begint — en iedereen slaapt een uur langer»", "겨울 시간이 시작돼요 — 모두가 한 시간 더 잘 수 있어요.", "Pagina 1"),
    ("«In het voorjaar gaat de klok vooruit, in het najaar achteruit»", "봄에는 시계를 앞으로, 가을에는 뒤로 돌려요.", "Pagina 2"),
    ("«Thuisbezorgd en Uber Eats stoppen met verborgen kosten»", "Thuisbezorgd와 Uber Eats가 숨은 비용을 없애요.", "Pagina 2"),
    ("«Ongeveer 2.500 ontwerpers laten hun werk zien»", "약 2,500명의 디자이너가 작품을 선보여요.", "Pagina 3"),
    ("«PSV won dinsdag met 1–0 bij FC Porto»", "PSV가 화요일 포르투에서 1–0으로 이겼어요.", "Pagina 4"),
    ("«Er komen meer dan 3.000 artiesten naar meer dan 200 locaties in de stad»", "3,000명이 넘는 아티스트가 도시의 200곳이 넘는 장소에 와요.", "Pagina 5"),
    ("«ongeveer 750.000 keer zochten Nederlanders naar de klokverandering»", "네덜란드인은 시간 변경을 약 750,000회 검색했어요.", "Pagina 6"),
    ("«Samen zijn dat 547.000 zoekopdrachten»", "둘을 합하면 547,000회의 검색이에요.", "Pagina 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 158
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- volgende week ----
py = 2404
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "VOLGENDE WEEK · 다음 호 예고 (VOL.2)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "Zondag 1 november begint Expeditie Robinson (20:00 uur, RTL 4): wie van de 19 kandidaten is de sterkste? Verder: de uitslagen van de Europese voetbalweek, de laatste verhalen van ADE en de Dutch Design Week, en jullie brieven en beste teksten van pagina 8. Tot maandag!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-taal.svg")
print("P7 saved, exercises so far:", len(REG))
