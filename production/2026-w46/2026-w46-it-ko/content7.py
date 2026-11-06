# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-it-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LINGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LINGUA · 언어", "La Lucerna", "언어 집중 · Tre livelli, tre strumenti · 세 단계, 세 가지 도구")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · IL FUTURO", 24)
a.para("Per i piani della settimana usiamo il futuro semplice: andremo a Cuneo, assaggeremo il vino nuovo, guarderemo Italia–Francia. Le forme sono regolari: andare → andrò, assaggiare → assaggerò, guardare → guarderò.", 21.5)
a.para("E per il tempo: ci sarà il sole di San Martino, durerà tre giorni. Il verbo è durare, regolare.", 21.5)
a.bridge("미래형으로 계획 말하기: andremo, assaggeremo, guarderemo.")
a.ex("A2", "문장 완성", "andremo", "andare의 미래형 noi: andremo",
     "Mercoledì noi ___ (andare) a Cuneo.", instr="빈칸 채우기", size=20.5, gap=10)
a.ex("A2", "문장 완성", "assaggeremo", "assaggiare 미래형 noi: assaggeremo",
     "Noi ___ (assaggiare) il vino nuovo.", instr="빈칸 채우기", size=20.5, gap=10)
a.ex("A2", "문장 완성", "guarderemo", "guardare의 미래형 noi: guarderemo",
     "Giovedì noi ___ (guardare) Italia–Francia.", instr="빈칸 채우기", size=20.5, gap=10)
a.ex("A2", "객관식", "B", "durerà는 durare의 미래형",
     "L'estate di San Martino... A. dura tre giorni · B. durerà tre giorni · C. durava tre giorni", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · IL PASSATO PROSSIMO", 24)
b.para("Per raccontare il weekend usiamo il passato prossimo: ausiliare + participio. Con essere — per verbi come arrivare e andare — il participio cambia con la persona: è arrivato (il treno), sono andati (i visitatori).", 21.5)
b.para("Con avere: abbiamo assaggiato, ha aperto. Il participio con avere non cambia.", 21.5)
b.bridge("과거 이야기는 근과거를 써요: arrivare, andare 같은 동사는 essere를 쓰고 분사는 성과 수에 맞춰요. avere의 분사는 변하지 않아요.")
b.ex("B1", "문장 완성", "è arrivato", "arrivare는 essere를 써요: è arrivato",
     "Il Treno Storico ___ (arrivare) a Cremona.", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "문장 완성", "abbiamo assaggiato", "assaggiare는 avere를 써요",
     "Noi ___ (assaggiare) il torrone a Cremona.", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "문장 완성", "sono andati", "andare는 essere를 써요. 복수 sono andati",
     "I visitatori ___ (andare) a Perugia.", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "객관식", "B", "aprire는 avere + 변하지 않는 분사를 써요",
     "Perugia ___ Eurochocolate. A. è aperta · B. ha aperto · C. sono aperti", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · IL CONGIUNTIVO", 24)
c.para("Con «è probabile che», «è possibile che» e «bisogna che» usiamo il congiuntivo: piova (piovere), nevichi (nevicare), sia (essere). È la grammatica della probabilità, la stessa di pagina 6.", 21.5)
c.para("Ma dopo «so che» e «i giornali scrivono che» resta l'indicativo: il sole torna, la Festa del Torrone è a Cremona. Opinioni sì, fatti con l'indicativo.", 21.5)
c.bridge("è probabile che, è possibile che, bisogna che 뒤에는 접속법을 써요. so che, scrivono che 뒤에는 직설법을 써요.")
c.ex("B2", "문장 완성", "piova", "è probabile che + 접속법 piova",
     "È probabile che domani ___ (piovere) in pianura.", instr="빈칸 채우기", size=20.5, gap=10)
c.ex("B2", "문장 완성", "nevichi", "è possibile che + 접속법 nevichi",
     "È possibile che in montagna ___ (nevicare) nel weekend.", instr="빈칸 채우기", size=20.5, gap=10)
c.ex("B2", "문장 완성", "sia", "bisogna che + 접속법 sia",
     "Bisogna che la cifra ___ (essere) chiara per tutti.", instr="빈칸 채우기", size=20.5, gap=10)
c.ex("B2", "객관식", "B", "so che + 직설법: torna",
     "«So che il sole...» A. torni · B. torna · C. tornare", size=20.5, gap=10)
c.end_report()

# ---- col 3: errori tipici + parola + lettori ----
bx = COLX[3]
errs = [
    ("«Fa freddi.»", "→ «Fa freddo.» Dopo fa, freddo non cambia mai: è invariabile.", "fa 뒤의 freddo는 절대 변하지 않는다"),
    ("«È probabile che piove.»", "→ «È probabile che piova.» Dopo è probabile che serve il congiuntivo.", "è probabile che 뒤에는 접속법"),
    ("«Ieri ho andato a Cremona.»", "→ «Ieri sono andato a Cremona.» Andare vuole essere, non avere.", "andare는 essere를 조동사로 쓴다"),
    ("«Il mosto diventano vino.»", "→ «Il mosto diventa vino.» Mosto è singolare, il verbo è singolare.", "mosto는 단수, 동사도 단수"),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 194
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ERRORI TIPICI · 자주 하는 실수", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 26
wt = "« il mosto » è il succo d'uva prima che diventi vino. Questa settimana vive a pagina 2, a San Martino."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("mosto = 포도즙/새 와인. 2면 참조: 성 마르티노 축일에 포도즙은 와인이 된다.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "LA PAROLA · 이번 주 단어", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "mosto = 포도즙/새 와인. 2면 참조: 성 마르티노 축일에 포도즙은 와인이 된다.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 26
lt = "«Ciao! Questa settimana la redazione assaggia il vino nuovo e le castagne, e guarda Italia–Francia in televisione. E voi? Scriveteci!» — esempio della redazione"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("이것은 편집부 예시이며 실제 편지가 아니다. 마감 당시 실제 편지와 8면 최우수 작문은 도착하지 않았다. 약속은 VOL.4로 이어진다. 편집부에 편지를 보내 주세요.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "LETTERE DEI LETTORI", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "이것은 편집부 예시이며 실제 편지가 아니다. 마감 당시 실제 편지와 8면 최우수 작문은 도착하지 않았다. 약속은 VOL.4로 이어진다. 편집부에 편지를 보내 주세요.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frasi della settimana (verbatim from this issue) ----
fy = 1700
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "FRASI DELLA SETTIMANA · 이번 주 문장 (이번 호 기사에서 그대로)", 27, "sans", True, OLIVE)
quotes = [
    ("«tre giorni di sole dopo il primo freddo»", "첫 추위 뒤 사흘간 맑음.", "Pagina 1"),
    ("«il sole tornò a splendere»", "태양이 다시 빛났다.", "Pagina 1"),
    ("«Il cinema che sceglie da che parte stare»", "입장을 선택하는 영화.", "Pagina 2"),
    ("«Due notti azzurre, alle 20.45»", "두 번의 파란 밤, 20시 45분.", "Pagina 1"),
    ("«arriva anche il Treno Storico Arlecchino»", "역사 열차 알레키노도 온다.", "Pagina 3"),
    ("«le due partite di questa settimana sono decisive»", "이번 주 두 경기는 결정적이다.", "Pagina 4"),
    ("«un libro in mano, un film negli occhi»", "손에는 책 한 권, 눈에는 영화 한 편.", "Pagina 5"),
    ("«approvato dal governo non vuol dire già legge»", "정부 승인이 곧 법률이라는 뜻은 아니다.", "Pagina 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 158
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- prossima settimana ----
py = 2404
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "LA PROSSIMA SETTIMANA · 다음 주 예고 (VOL.4)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "Domenica 22 novembre: chiude la Festa del Torrone a Cremona. La Serie A torna il 21–23 novembre, con i risultati dell'11ª giornata. E poi: le vostre lettere vere e i testi migliori della pagina 8. A lunedì!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lingua.svg")
print("P7 saved, exercises so far:", len(REG))
