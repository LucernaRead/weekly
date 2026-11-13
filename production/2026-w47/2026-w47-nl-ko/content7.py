# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · TAAL (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("TAAL　언어", "De Lucerna", "언어에 집중　Drie niveaus, drie gereedschappen　세 단계, 세 가지 도구")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　VOETBALWOORDEN", 24)
a.para("De woorden van deze week horen bij het voetbal: de wedstrijd, de groepswinst, de kwartfinale en scoren. De wedstrijd is maandag in Berlijn: Duitsland tegen Nederland. De groepswinst is de eerste plaats in de groep.", 21.5)
a.para("En scoren: wie een doelpunt maakt, scoort. Nederland maakte 7 doelpunten in vier wedstrijden — meer dan Griekenland (5). Daarom staat Oranje bovenaan. Onthoud ook: de schoen staat klaar voor Sinterklaas.", 21.5)
a.bridge("de wedstrijd 경기; de groepswinst 조 우승; de kwartfinale 8강전; scoren 골을 넣다.", w=423.65)  # delta D7: width-scan window band 417.3-430.0px keeps the 2 lines; mid 423.65 (true upper edge 530.1)
a.ex("A2", "문장 완성", "wedstrijd", "de wedstrijd = 경기",
     "Duitsland – Nederland is een belangrijke ___.", instr="빈칸 채우기", size=20.5, gap=10)
a.ex("A2", "문장 완성", "groepswinst", "de groepswinst = 조 우승",
     "Wie pakt de ___ in groep 2?", instr="빈칸 채우기", size=20.5, gap=10)
a.ex("A2", "객관식", "B", "조 우승은 조 1위를 뜻해요",
     "«De groepswinst» is... A. een boek · B. de eerste plaats in de groep · C. een liedje", size=20.5, gap=10)
a.ex("A2", "문장 완성", "scoorde", "scoren의 과거형: scoorde",
     "Nederland ___ (scoren) 7 keer in vier wedstrijden.", instr="빈칸 채우기", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　DE VERLEDEN TIJD", 24)
b.para("Nederlands vertelt over het verleden met de verleden tijd: spelen wordt speelde, winnen wordt won, verliezen wordt verloor, maken wordt maakte. Voorbeeld: «PSV won met 2–5 van Cambuur.» «Feyenoord verloor met 5–3 bij Heerenveen.»", 21.5)
b.para("Let op: sommige werkwoorden zijn onregelmatig — winnen/won, verliezen/verloor. Andere zijn regelmatig: spelen/speelde, maken/maakte. Oefen met de uitslagen van deze week.", 21.5)
b.bridge("speelde 경기를 했다; won 이겼다; verloor 졌다; maakte 골을 넣었다. 과거형은 이미 일어난 일을 말한다.")
b.ex("B1", "문장 완성", "won", "winnen 과거형: won",
     "PSV ___ (winnen) met 2–5 van Cambuur.", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "문장 완성", "verloor", "verliezen의 과거형: verloor",
     "Feyenoord ___ (verliezen) met 5–3 bij Heerenveen.", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "문장 완성", "speelde", "spelen 과거형: speelde",
     "Ajax ___ (spelen) 2–2 tegen Twente.", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "객관식", "B", "won은 winnen의 과거형이에요",
     "«Won» is de verleden tijd van... A. spelen · B. winnen · C. verliezen", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　BIJZINNEN MET OMDAT", 24)
c.para("Met «omdat» zeg je waarom iets gebeurt: «Oranje staat bovenaan, omdat het meer doelpunten maakte.» «Sinterklaas komt 's nachts, omdat de kinderen dan slapen.» De bijzin met «omdat» staat achteraan; het werkwoord staat dan helemaal achteraan in de bijzin.", 21.5)
c.para("Voorbeeld: «Ik zet mijn schoen, omdat ik een cadeautje wil.» «Het feest verandert, omdat mensen anders vieren.» Een omdat-zin is geen vraag — het is een reden: dit gebeurt, omdat dat.", 21.5)
c.bridge("omdat ~이기 때문에; omdat het meer doelpunten maakte 골을 더 많이 넣었기 때문에; omdat ik een cadeautje wil 선물을 받고 싶기 때문에.")
c.ex("B2", "문장 완성", "omdat", "omdat = ~이기 때문에",
     "Oranje staat bovenaan, ___ het meer doelpunten maakte.", instr="빈칸 채우기", size=20.5, gap=10)
c.ex("B2", "객관식", "B", "omdat 절은 이유를 나타내지, 의문이 아니에요",
     "«Ik zet mijn schoen, omdat ik een cadeautje wil» is... A. een vraag · B. een reden · C. een bevel", size=20.5, gap=10)
c.ex("B2", "문장 완성", "wil", "동사는 omdat 절 끝에 와요: wil",
     "Ik zet mijn schoen, omdat ik een cadeautje ___.", instr="빈칸 채우기", size=20.5, gap=10)
c.ex("B2", "문장 완성", "maakte", "omdat 절에서 maakte가 맨 끝에 와요",
     "Oranje staat bovenaan, omdat het meer doelpunten ___.", instr="빈칸 채우기", size=20.5, gap=10)
c.end_report()

# ---- col 3: pas op + het woord + brieven ----
bx = COLX[3]
errs = [
    ("«De Oranje speelt maandag.»", "→ Fout: Oranje is een naam, zonder lidwoord: «Oranje speelt maandag.»", "오라녜는 고유명사라서 관사가 붙지 않아요."),
    ("«Ik zet een schoen.»", "→ «De schoen zetten» vraagt een bezittelijk woord: «Ik zet mijn schoen.»", "mijn schoen = 내 신발이에요."),
    ("«PSV winnen met 2–5.»", "→ De verleden tijd van winnen is won: «PSV won met 2–5.»", "winnen의 과거형은 won이에요."),
    ("«Omdat het regent, ik blijf thuis.»", "→ Na de omdat-zin staat het werkwoord vooraan: «... blijf ik thuis.»", "omdat 절 뒤에서는 본절 동사가 맨 앞에 와요: blijf ik thuis."),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 192
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "PAS OP!　실수 클리닉", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 18
wt = "«de groepswinst» betekent: de eerste plaats in de groep. Wie de groepswinst pakt, gaat als nummer één naar de kwartfinales."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("groepswinst = 조 우승: 조 1위, 1위가 8강전에 진출해요.", "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "HET WOORD　이번 주 단어", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "groepswinst = 조 우승: 조 1위, 1위가 8강전에 진출해요.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 18
lt = "«Hallo! Ik ben Anna en ik leer Nederlands. Maandag kijk ik naar Oranje tegen Duitsland — en daarna zet ik mijn schoen!» — Anna (voorbeeldbrief van de redactie)"
dt_nl = "Ter perse: nog geen echte brieven of beste pagina-8-teksten binnen — daarom dit voorbeeld; belofte naar VOL.5."
dt_zh = "마감까지 편지나 작문이 없어 예시를 실어요. 약속은 VOL.5로 이어져요."
dt_zh_w = 376.3  # delta D10: width-scan band 364.9-387.7px keeps the 2 lines; mid 376.3
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(dt_nl, "serif", False, 21.5, CW - 44)) * 30.5 + 10 + len(wrap(dt_zh, "sans", False, 20, dt_zh_w)) * 29 + 10 + len(wrap("편집부 예시 편지이며, 실제 편지가 아니에요. 여러분의 편지와 작문을 보내 주세요. VOL.5에 싣겠습니다!", "sans", False, 20, CW - 44)) * 29 + 34 + 50
# +50 measured correction carried from W45 Fix-1 (rendered spacing runs above formula).
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "BRIEVEN VAN LEZERS", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 21, dt_nl, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 20, dt_zh, 20, "sans", False, GREY, dt_zh_w, 1.42) + 10  # delta D10: dt_zh_w, see above
p.para(bx + 22, yy3 + 20, "편집부 예시 편지이며, 실제 편지가 아니에요. 여러분의 편지와 작문을 보내 주세요. VOL.5에 싣겠습니다!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- P7 photo (W47: every page carries a public-domain image) ----
ix7, iw7 = span_x(0, 2)
image(p, "boeken.jpg", ix7, 1580, iw7, 240)
cy7 = caption(p, ix7, 1820, iw7, "Boeken in een boekwinkel. In november leest heel Nederland Het diner — gratis in de bibliotheek.",
              "Foto: Cristina Gottardi / Unsplash — CC0")
print("P7 photo ends", cy7)

# ---- zinnen van de week (verbatim from this issue) ----
fy = 1951
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "ZINNEN VAN DE WEEK　이번 주 명문장(이번 호 기사에서 그대로)", 27, "sans", True, OLIVE)
quotes = [
    ("«Op maandag 16 november speelt Oranje in Berlijn tegen Duitsland»", "11월 16일 월요일, 오라녜는 베를린에서 독일과 맞붙어요.", "Pagina 1"),
    ("«Na vier wedstrijden staan Nederland en Griekenland samen bovenaan met 8 punten»", "네 경기를 마친 뒤 네덜란드와 그리스는 승점 8점으로 공동 선두에 있어요.", "Pagina 1"),
    ("«Op zaterdag 5 december is het pakjesavond: de avond met de grote cadeaus»", "12월 5일 토요일은 팍예스아폰트, 큰 선물의 밤이에요.", "Pagina 2"),
    ("«Op zaterdag 14 november kwam Sinterklaas officieel aan in Nederland»", "11월 14일 토요일, 신터클라스가 공식적으로 네덜란드에 도착했어요.", "Pagina 3"),
    ("«Nederland staat eerste, omdat het meer doelpunten maakte: 7 tegen 5»", "네덜란드가 1위인 것은 골을 더 많이 넣었기 때문이에요: 7 대 5.", "Pagina 4"),
    ("«Elke zondag om 20:00 uur is Expeditie Robinson te zien op RTL 4»", "매주 일요일 20:00에 Expeditie Robinson은 RTL 4에서 방송해요.", "Pagina 5"),
    ("«Sinterklaas is een oud feest in Nederland»", "신터클라스 축제는 네덜란드의 오래된 축제예요.", "Pagina 6"),
    ("«Een traditie leeft als mensen haar blijven vieren»", "전통은 사람들이 계속 기념할 때 살아남아요.", "Pagina 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 90 + (16 if (i % 4) >= 3 else 0)
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- volgende week ----
py = 2439
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "VOLGENDE WEEK　다음 주 예고(VOL.5)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "Dinsdag 24 november is er Europees voetbal: Real Madrid – PSV en Feyenoord – FC Porto. Zondag 29 november is het Feyenoord – Ajax. En zaterdag 5 december is het pakjesavond. Verder: jullie brieven en de beste teksten van pagina 8. Tot maandag!", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-taal.svg")
print("P7 saved, exercises so far:", len(REG))
