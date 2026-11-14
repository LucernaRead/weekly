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
a.head("A2　DIRE L'ORA E IL PRESENTE", 24)
a.para("Per dire l'ora: «È l'una», ma «Sono le due, le tre…». «E mezza» è +30 minuti (2:30); «meno un quarto», −15 (2:45).", 21.5)
a.para("E dormire è regolare: dormo, dormi, dorme, dormiamo. Svegliarsi è riflessivo: mi sveglio, si sveglia.", 21.5)
a.expl("시각을 말할 때 '1시'만 è를 써요. dormire는 규칙 변화, svegliarsi는 재귀 동사예요.")
a.ex("A2", "문장 완성", "Sono", "10시는 Sono를 써요 (È는 l'una만)",
     "___ le dieci di sera. Comincia il film.", instr="빈칸 채우기", size=20.5, gap=10)
a.ex("A2", "문장 완성", "dorme", "dormire: lui → dorme",
     "Mio fratello ___ (dormire) fino alle undici domenica.", instr="빈칸 채우기", size=20.5, gap=10)
a.ex("A2", "문장 완성", "si sveglia", "svegliarsi: lei → si sveglia",
     "Lei ___ (svegliarsi) alle otto.", instr="빈칸 채우기", size=20.5, gap=10)
a.ex("A2", "객관식", "B", "e mezza = 30분",
     "«Sono le due e mezza» sono le... A. 2:15 · B. 2:30 · C. 2:45", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　IL PASSATO PROSSIMO", 24)
b.para("Per raccontare il weekend usiamo il passato prossimo: ausiliare + participio. Con avere: ho visitato, abbiamo guardato.", 21.5)
b.para("Con essere — per verbi di movimento come andare e arrivare — il participio cambia con la persona: sono andato / sono andata, è iniziata (la fiera).", 21.5)
b.expl("주말 이야기를 할 때는 근과거를 써요: avere + 과거분사. andare, arrivare 같은 이동 동사는 essere를 쓰고, 분사는 성과 수에 맞춰요.")
b.ex("B1", "문장 완성", "è iniziata", "iniziare는 essere를 써요. 여성형 è iniziata",
     "La fiera ___ (iniziare) il 10 ottobre.", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "문장 완성", "abbiamo visitato", "visitare는 avere를 써요",
     "Noi ___ (visitare) la mostra mercoledì.", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "문장 완성", "è andato", "andare는 essere를 써요: è andato",
     "Marco ___ (andare) alla sagra con gli amici.", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "객관식", "B", "arrivare는 essere + 복수 일치를 써요",
     "I tifosi ___ allo stadio. A. hanno arrivato · B. sono arrivati · C. è arrivati", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　IL CONGIUNTIVO", 24)
c.para("Con «è possibile che», «bisogna che» e «è importante che» usiamo il congiuntivo: slitti (slittare), sia (essere), abbia (avere).", 21.5)
c.para("Ma dopo «so che» e «i giornali scrivono che» resta l'indicativo: il Consiglio si riunisce, la Festa chiude. È la grammatica della pagina 6: opinioni sì, fatti con l'indicativo.", 21.5)
c.expl("è possibile che / bisogna che / è importante che 뒤에는 접속법을 써요. so che, scrivono che 뒤에는 직설법을 써요.")
c.ex("B2", "문장 완성", "slitti", "è possibile che + 접속법 slitti",
     "È possibile che il voto ___ (slittare) ancora.", instr="빈칸 채우기", size=20.5, gap=10)
c.ex("B2", "문장 완성", "abbia", "bisogna che + 접속법 abbia",
     "Bisogna che ogni cifra ___ (avere) una fonte.", instr="빈칸 채우기", size=20.5, gap=10)
c.ex("B2", "문장 완성", "chiude", "so che + 직설법 chiude",
     "So che la Festa ___ (chiudere) domenica.", instr="빈칸 채우기", size=20.5, gap=10)
c.ex("B2", "객관식", "B", "è importante che + 접속법 sia",
     "«È importante che il grafico...» A. è chiaro · B. sia chiaro · C. essere chiaro", size=20.5, gap=10)
c.end_report()

# ---- col 3: errori tipici + parola + lettori ----
bx = COLX[3]
errs = [
    ("«Sono le una.»", "→ «È l'una.» Solo l'ora 1:00 usa è; le altre ore usano sono.", "1시만 è, 나머지는 sono예요."),
    ("«Ho andato a Lucca.»", "→ «Sono andato a Lucca.» Andare vuole l'ausiliare essere, non avere.", "조동사는 avere가 아니라 essere예요."),
    ("«Vado a il cinema.»", "→ «Vado al cinema.» A + il si uniscono: al. Anche: del, nel, sul, dal.", "a + il → al이에요. del, nel, sul, dal도 같아요."),
    ("«La gente sono contenti.»", "→ «La gente è contenta.» Gente è singolare, come un solo gruppo.", "gente는 단수예요. 단수 여성형으로 맞춰요."),
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
wt = "« l'anteprima » è la prima volta che il pubblico vede un film. Questa settimana la parola vive a pagina 5: alla Festa del Cinema, molte proiezioni sono anteprime."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("anteprima = 시사회예요. 5면에서 만나요: 영화제의 많은 상영이 시사회예요.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "LA PAROLA　이번 주 단어", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "anteprima = 시사회예요. 5면에서 만나요: 영화제의 많은 상영이 시사회예요.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 26
lt = "«Ciao! Sono Li e studio italiano a Pechino. Domenica dormo un'ora in più e poi guardo Inter–Fiorentina. Grazie per il giornale!» — Li (lettera di esempio, scritta dalla redazione)"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("이 편지는 편집부가 쓴 예시예요. VOL.2에는 실제 편지를 실어요. 편지를 보내 주세요!", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "LETTERE DEI LETTORI", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "이 편지는 편집부가 쓴 예시예요. VOL.2에는 실제 편지를 실어요. 편지를 보내 주세요!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frasi della settimana (verbatim from this issue) ----
fy = 1700
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "FRASI DELLA SETTIMANA　이번 주 문장 (이번 호 기사에서 그대로)", 27, "sans", True, OLIVE)
quotes = [
    ("«alle 03:00 l'orologio torna indietro di un'ora»", "03:00에 시계가 한 시간 뒤로 돌아가요.", "Pagina 1"),
    ("«È la ricerca numero uno in Italia»", "이탈리아에서 검색량 1위인 말이에요.", "Pagina 1"),
    ("«L'ora tra le 02:00 e le 03:00 arriva due volte nella stessa notte.»", "02:00부터 03:00까지 한 시간이 같은 밤에 두 번 와요.", "Pagina 2"),
    ("«In primavera avanti, in autunno indietro.»", "봄에는 앞으로, 가을에는 뒤로 돌려요.", "Pagina 2"),
    ("«Il re della stagione è il tartufo bianco»", "이 계절의 왕은 화이트 트러플이에요.", "Pagina 3"),
    ("«È una partita speciale: è la prima della domenica con l'ora solare.»", "이 경기는 특별해요: 일요일 첫 표준시 경기예요.", "Pagina 4"),
    ("«Molte sono anteprime: film che il pubblico vede per la prima volta.»", "많은 작품이 시사회예요: 관객이 처음 보는 영화예요.", "Pagina 5"),
    ("«Un voto previsto non è un voto fatto»", "'예정된' 표결은 이미 한 표결이 아니에요.", "Pagina 6"),
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
p.text(MX + 28, py + 44, "LA PROSSIMA SETTIMANA　다음 호 예고 (VOL.2)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "Mercoledì 28 ottobre: il voto sulla manovra a Roma. Dal 28 ottobre al 1° novembre: Lucca Comics & Games, la 60ª edizione. Domenica 1° novembre: Ognissanti — quest'anno cade di domenica, niente ponte. E poi: le vostre lettere e i testi migliori della pagina 8. A lunedì!", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lingua.svg")
print("P7 saved, exercises so far:", len(REG))
