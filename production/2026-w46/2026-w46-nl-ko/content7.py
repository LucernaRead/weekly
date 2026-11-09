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
a.head("A2　SINTERKLAASWOORDEN", 24)
a.para("De woorden van deze week horen bij Sinterklaas: de stoomboot, de intocht, de schoen zetten en de lampion. De stoomboot brengt Sinterklaas uit Spanje. De intocht is zijn feestelijke aankomst in een stad.", 21.5)
a.para("En de schoen: na de intocht zetten kinderen hun schoen bij de deur, met een wortel voor het paard. 's Nachts komt Sinterklaas met een cadeautje. Onthoud ook: Sint-Maarten is het feest van het delen.", 21.5)
a.bridge("de stoomboot 증기선; de intocht 축제 도착; de schoen zetten 신발 내놓기; de lampion 등롱.")
a.ex("A2", "문장 완성", "stoomboot", "de stoomboot = 증기선",
     "Sinterklaas komt met de ___ uit Spanje.", instr="빈칸 채우기", size=20.5, gap=10)
a.ex("A2", "문장 완성", "schoen", "schoen zetten = 신발 내놓기",
     "Na de intocht zetten kinderen hun ___.", instr="빈칸 채우기", size=20.5, gap=10)
a.ex("A2", "객관식", "B", "intocht는 신터클라스의 축제 도착이에요",
     "«De intocht» is... A. een boek · B. de feestelijke aankomst van Sinterklaas · C. een liedje", size=20.5, gap=10)
a.ex("A2", "문장 완성", "lampion", "lampion = 등롱",
     "Op Sint-Maarten lopen kinderen met een ___.", instr="빈칸 채우기", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　VERKLEINWOORDEN", 24)
b.para("Nederlands maakt graag kleine woorden met -je: de schoen wordt het schoentje, het licht wordt het lichtje, het cadeau wordt het cadeautje. Klein betekent hier: lief, klein of gezellig — niet altijd echt klein.", 21.5)
b.para("Let op de spelling: de medeklinker verdubbelt soms, maar niet altijd — het is het boekje, het worteltje, het liedje. En na -ing komt -tje: de lampion wordt het lampionnetje. Oefen met de woorden van deze week.", 21.5)
b.bridge("schoentje 작은 신발; lichtje 작은 불빛; cadeautje 작은 선물. -je는 작고 애정 어린 뜻이에요.")
b.ex("B1", "문장 완성", "schoentje", "schoen + -tje: schoentje",
     "Zet je ___ bij de deur, met een wortel erin.", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "문장 완성", "lichtje", "licht + -je: lichtje",
     "«Elf november is de dag, dat mijn ___ branden mag.»", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "문장 완성", "cadeautje", "cadeau + -tje: cadeautje",
     "Sinterklaas brengt een ___ in de schoen.", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "객관식", "B", "-je는 작고 애정 어린 뜻이에요, 항상 실제로 작은 것은 아니에요",
     "Een verkleinwoord met -je betekent... A. altijd heel klein · B. klein, lief of gezellig · C. heel groot", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　ZINNEN MET ALS", 24)
c.para("Met «als» zeg je wanneer iets gebeurt: «Als het donker wordt, gaan de kinderen op pad.» «Als Sinterklaas komt, staat de schoen klaar.» De bijzin met «als» staat eerst; daarna komt het werkwoord op plaats 1 in de hoofdzin.", 21.5)
c.para("Voorbeeld: «Als Oranje wint, gaat Nederland naar de kwartfinales.» «Als het regent, loop ik toch met mijn lampion.» Een als-zin is geen vraag — het is een voorwaarde: dit gebeurt, dan dat.", 21.5)
c.bridge("Als… = 만약… / ~할 때; als het donker wordt = 어두워지면; als Sinterklaas komt = 신터클라스가 오면.")
c.ex("B2", "문장 완성", "Als", "Als… = 만약… / ~할 때",
     "___ het donker wordt, gaan de kinderen op pad.", instr="빈칸 채우기", size=20.5, gap=10)
c.ex("B2", "객관식", "B", "als 절은 조건이지, 질문이 아니에요",
     "«Als Sinterklaas komt, staat de schoen klaar» is... A. een vraag · B. een voorwaarde · C. een bevel", size=20.5, gap=10)
c.ex("B2", "문장 완성", "gaat", "주절에서는 동사가 먼저 와요: gaat de lampion aan",
     "Als het donker wordt, ___ de lampion aan.", instr="빈칸 채우기", size=20.5, gap=10)
c.ex("B2", "문장 완성", "wint", "Als Oranje wint… = 오라녜가 이기면…",
     "Als Oranje ___, gaat Nederland naar de kwartfinales.", instr="빈칸 채우기", size=20.5, gap=10)
c.end_report()

# ---- col 3: pas op + het woord + brieven ----
bx = COLX[3]
errs = [
    ("«De Sinterklaas komt zaterdag.»", "→ Fout: Sinterklaas is een naam, zonder lidwoord: «Sinterklaas komt zaterdag.»", "Sinterklaas는 이름이라서 관사가 없어요."),
    ("«Ik zet de schoen.»", "→ «De schoen zetten» vraagt een bezittelijk woord: «Ik zet mijn schoen.»", "mijn schoen = 내 신발이에요."),
    ("«Kinderen lopen langs de deur.»", "→ Het is een vaste uitdrukking: «langs de deuren» (meervoud).", "고정 표현: langs de deuren."),
    ("«Als Sinterklaas komt, ik ben blij.»", "→ Na de als-zin staat het werkwoord vooraan: «... ben ik blij.»", "als 절 뒤에서는 동사가 먼저 와요: ben ik blij."),
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
wt = "«de schoen zetten» betekent: je schoen neerzetten, met een wortel en een tekening erin, voor Sinterklaas."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("schoen zetten = 신발 내놓기: 당근과 그림을 넣어 두는 거예요.", "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "HET WOORD　이번 주 단어", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "schoen zetten = 신발 내놓기: 당근과 그림을 넣어 두는 거예요.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 18
lt = "«Hallo! Ik ben Anna en ik leer Nederlands. Op 11 november loop ik met een lampion langs de deuren!» — Anna (voorbeeldbrief van de redactie)"
dt_nl = "Ter perse: nog geen echte brieven of beste pagina-8-teksten binnen — daarom dit voorbeeld; belofte naar VOL.4."
dt_zh = "실제 편지와 최고 작문이 없어 예시를 싣고, 약속은 VOL.4로 이어져요."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(dt_nl, "serif", False, 21.5, CW - 44)) * 30.5 + 10 + len(wrap(dt_zh, "sans", False, 20, CW - 44)) * 29 + 10 + len(wrap("편집부 예시예요. 여러분의 편지와 작문을 보내 주세요!", "sans", False, 20, CW - 44)) * 29 + 34 + 50
# +50 measured correction carried from W45 Fix-1 (rendered spacing runs above formula).
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "BRIEVEN VAN LEZERS", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 21, dt_nl, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 20, dt_zh, 20, "sans", False, GREY, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "편집부 예시예요. 여러분의 편지와 작문을 보내 주세요!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- zinnen van de week (verbatim from this issue) ----
fy = 1951
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "ZINNEN VAN DE WEEK　이번 주 금문장(본문에서 그대로 가져왔어요)", 27, "sans", True, OLIVE)
quotes = [
    ("«Op maandag 9 november begint het Sinterklaasjournaal op televisie»", "11월 9일 월요일에 신터클라스 뉴스가 TV에서 시작해요.", "Pagina 1"),
    ("«Een dag later, op zondag 15 november, is de intocht in Amsterdam: de 88e editie»", "그다음 날인 11월 15일 일요일: 암스테르담 도착, 88회째예요.", "Pagina 1"),
    ("«Daarom is Sint-Maarten het feest van het delen: licht delen, eten delen, aandacht delen»", "성 마르틴의 날은 나눔의 축제예요: 빛과 음식과 관심을 나누어요.", "Pagina 2"),
    ("«Op zaterdag 14 november komt Sinterklaas officieel aan in Grave»", "11월 14일 토요일에 신터클라스는 흐라버에 공식적으로 도착해요.", "Pagina 3"),
    ("«Op vrijdag 13 november speelt Oranje thuis tegen Griekenland»", "11월 13일 금요일에 오라녜는 홈에서 그리스와 경기를 해요.", "Pagina 4"),
    ("«Elke zondag om 20:00 uur is Expeditie Robinson te zien op RTL 4»", "매주 일요일 20:00에 Expeditie Robinson은 RTL 4에서 방송해요.", "Pagina 5"),
    ("«Sint-Maarten is een oude traditie in Nederland»", "성 마르틴의 날은 네덜란드의 오래된 전통이에요.", "Pagina 6"),
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
p.text(MX + 28, py + 44, "VOLGENDE WEEK　다음 호 예고 (VOL.4)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "Maandag 16 november speelt Oranje in Berlijn tegen Duitsland — de uitslag lees je volgende week. Zaterdag 5 december is het pakjesavond. Verder: jullie brieven en de beste teksten van pagina 8. Tot maandag!", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-taal.svg")
print("P7 saved, exercises so far:", len(REG))
