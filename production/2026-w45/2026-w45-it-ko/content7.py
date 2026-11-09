# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LINGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LINGUA　언어", "La Lucerna", "언어 집중　Tre livelli, tre strumenti　세 단계, 세 가지 도구")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　IL TEMPO CHE FA", 24)
a.para("Per il tempo usiamo verbi impersonali, sempre alla terza persona singolare: fa freddo, fa caldo, piove, nevica, c'è vento. Non si dice «sono freddo»: si dice «ho freddo» (io) e «fa freddo» (fuori).", 21.5)
a.para("E per vestirsi: metto il cappotto, metti la sciarpa, mette i guanti. Il verbo è mettere, regolare.", 21.5)
a.bridge("날씨는 무인칭 동사 (3인칭 단수)를 써요. '나는 추워요'는 ho freddo, '밖이 추워요'는 fa freddo예요.")
a.ex("A2", "문장 완성", "piove", "piovere 날씨 동사: piove",
     "Oggi ___ (piovere) sul versante adriatico.", instr="빈칸 채우기", size=20.5, gap=10)
a.ex("A2", "문장 완성", "fa", "fa freddo = 날씨가 추워요",
     "Fuori ___ freddo: metti il cappotto!", instr="빈칸 채우기", size=20.5, gap=10)
a.ex("A2", "문장 완성", "nevica", "nevicare: nevica",
     "In montagna ___ (nevicare) intorno ai 1.500 metri.", instr="빈칸 채우기", size=20.5, gap=10)
a.ex("A2", "객관식", "B", "'나는 추워요'는 ho freddo예요",
     "«Io ho freddo» vuol dire... A. fuori fa freddo · B. io sento freddo · C. nevica", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　IL PASSATO PROSSIMO", 24)
b.para("Per raccontare il freddo usiamo il passato prossimo: ausiliare + participio. Con essere — per verbi come arrivare e andare — il participio cambia con la persona: è arrivato (il freddo), sono andati (i pasticceri).", 21.5)
b.para("Con avere: abbiamo assaggiato, ha aperto. Il participio con avere non cambia.", 21.5)
b.bridge("과거 이야기는 근과거를 써요: arrivare, andare 같은 동사는 essere를 쓰고 분사는 성과 수에 맞춰요. avere의 분사는 변하지 않아요.")
b.ex("B1", "문장 완성", "è arrivato", "arrivare는 essere를 써요: è arrivato",
     "Il primo freddo ___ (arrivare) lunedì.", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "문장 완성", "abbiamo assaggiato", "assaggiare는 avere를 써요",
     "Noi ___ (assaggiare) il torrone a Cremona.", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "문장 완성", "sono andati", "andare는 essere를 써요. 복수 sono andati",
     "I pasticceri ___ (andare) a Milano.", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "객관식", "B", "aprire는 avere + 변하지 않는 분사를 써요",
     "Cremona ___ la Festa del Torrone. A. è aperta · B. ha aperto · C. sono aperti", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　IL CONGIUNTIVO", 24)
c.para("Con «è probabile che», «è possibile che» e «bisogna che» usiamo il congiuntivo: piova (piovere), nevichi (nevicare), sia (essere). È la grammatica della probabilità, la stessa di pagina 6.", 21.5)
c.para("Ma dopo «so che» e «i giornali scrivono che» resta l'indicativo: il freddo arriva, la finale è a Milano. Opinioni sì, fatti con l'indicativo.", 21.5)
c.bridge("è probabile che, è possibile che, bisogna che 뒤에는 접속법을 써요. so che, scrivono che 뒤에는 직설법을 써요.")
c.ex("B2", "문장 완성", "piova", "è probabile che + 접속법 piova",
     "È probabile che domani ___ (piovere) sul versante adriatico.", instr="빈칸 채우기", size=20.5, gap=10)
c.ex("B2", "문장 완성", "nevichi", "è possibile che + 접속법 nevichi",
     "È possibile che in montagna ___ (nevicare) nel weekend.", instr="빈칸 채우기", size=20.5, gap=10)
c.ex("B2", "문장 완성", "sia", "bisogna che + 접속법 sia",
     "Bisogna che la previsione ___ (essere) chiara per tutti.", instr="빈칸 채우기", size=20.5, gap=10)
c.ex("B2", "객관식", "B", "so che + 직설법 arriva",
     "«So che il freddo...» A. arrivi · B. arriva · C. arrivare", size=20.5, gap=10)
c.end_report()

# ---- col 3: errori tipici + parola + lettori ----
bx = COLX[3]
errs = [
    ("«Fa freddi.»", "→ «Fa freddo.» Dopo fa, freddo non cambia mai: è invariabile.", "fa 뒤의 freddo는 변하지 않아요."),
    ("«Ho nevicato ieri.»", "→ «Ha nevicato ieri.» Nevicare è impersonale: solo la terza persona singolare.", "nevicare는 3인칭 단수만 써요."),
    ("«Pioverà di sicuro.»", "→ «Potrebbe piovere.» Le previsioni danno probabilità, non certezze.", "예보는 확률이지, 확실한 게 아니에요."),
    ("«La gente sono infreddoliti.»", "→ «La gente è infreddolita.» Gente è singolare, come un solo gruppo.", "gente는 단수예요. 단수 여성형으로 써요."),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 194
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ERRORI TIPICI　자주 하는 실수", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 26
wt = "« l'assaggio » è la prova di un cibo: un piccolo pezzo per decidere se piace. Questa settimana vive a pagina 3, alla finale del Panettone."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("assaggio = 맛보기예요. 3면 파네토네 결승에서 무료로 맛봐요.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "LA PAROLA　이번 주 단어", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "assaggio = 맛보기예요. 3면 파네토네 결승에서 무료로 맛봐요.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 26
lt = "«Ciao! Sono Li, studio italiano a Pechino. Lunedì metto il cappotto e la sciarpa, sabato assaggio il panettone — almeno in foto!» — Li (esempio della redazione)"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("편집부 예시예요. 실제 편지도 8면 우수 작문도 아직 없어요. 편지를 보내 주세요! VOL.3에 실어요!", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "LETTERE DEI LETTORI", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "편집부 예시예요. 실제 편지도 8면 우수 작문도 아직 없어요. 편지를 보내 주세요! VOL.3에 실어요!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frasi della settimana (verbatim from this issue) ----
fy = 1700
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "FRASI DELLA SETTIMANA　이번 주 문장 (이번 호 기사에서 그대로)", 27, "sans", True, OLIVE)
quotes = [
    ("«arriva il primo freddo vero della stagione»", "첫 진짜 추위가 찾아왔어요.", "Pagina 1"),
    ("«Non è una certezza, è una probabilità»", "이건 확실한 게 아니라 확률이에요.", "Pagina 1"),
    ("«il 2 novembre è la Commemorazione dei defunti»", "11월 2일은 추모의 날이에요。", "Pagina 2"),
    ("«Fa freddo, copriti bene!»", "추우니 따뜻하게 입어요!", "Pagina 2"),
    ("«il pubblico può assaggiare gratis»", "관객이 무료로 맛볼 수 있어요.", "Pagina 3"),
    ("«il calcio non si ferma per il primo freddo»", "축구는 첫 추위 때문에 멈추지 않아요.", "Pagina 4"),
    ("«la cultura continua»", "문화는 계속돼요.", "Pagina 5"),
    ("«Una probabilità alta non è una certezza»", "높은 확률이 확실한 것은 아니에요.", "Pagina 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 158
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- prossima settimana ----
py = 2404
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "LA PROSSIMA SETTIMANA　다음 호 예고 (VOL.3)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "Lunedì 9 novembre: chiude il Festival dei Popoli a Firenze. La Festa del Torrone continua a Cremona fino al 22 novembre. E poi: le vostre lettere vere e i testi migliori della pagina 8. A lunedì!", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lingua.svg")
print("P7 saved, exercises so far:", len(REG))
