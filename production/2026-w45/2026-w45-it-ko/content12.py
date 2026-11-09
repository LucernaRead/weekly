# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · PRIMA PAGINA (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 2　SECONDA EDIZIONE", 17, "sans", True, OLIVE, spacing=1.7)
p.text(975, 92, "WEEKLY IN ITALIAN　매주 발행　이탈리아가 읽는 이탈리아어", 17, "sans", False, GREY, anchor="middle", spacing=1.7)
p.text(RIGHT, 92, "SETTIMANA DAL 2 ALL'8 NOVEMBRE 2026", 17, "sans", False, GREY, anchor="end", spacing=1.7)
p.text(975, 262, "La Lucerna", 196, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "이탈리아어 주간지　VOL.2　IL PRIMO FREDDO　IL PANETTONE　LA SERIE A", 36, "serif", True, OLIVE, anchor="middle", spacing=9.0)
p.text(975, 372, "IL GIORNALE SETTIMANALE PER IMPARARE — L'ITALIA VERA, IN ITALIANO, DALL'ITALIA", 16, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)

# band
p.rect(MX, 470, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 30, 524, "ARRIVA IL PRIMO FREDDO!", 46, "sans", True, ONCLOTH)
p.text(MX + 30, 568, "La settimana in cui l'Italia si copre: freddo, piogge e la prima neve in montagna.", 25, "serif", False, "#cac8ba")
p.text(RIGHT - 30, 524, "이번 주 첫 추위가 찾아와요", 27, "sans", True, GOOSE, anchor="end")
p.text(RIGHT - 30, 568, "첫 추위의 주　2면 참고", 18, "sans", False, GOOSE, anchor="end")

# ---- headline (span cols 0-2) ----
hy = 580
p.text(MX, hy + 26, "LA NOTIZIA　헤드라인", 17, "sans", True, OLIVE)
hy = p.para(MX, hy + 92, "Arriva il primo freddo: l'Italia si copre e si mette a tavola", 53, "serif", True, INK, 1323, 1.06)
p.text(MX, hy + 28, "Dalla redazione de La Lucerna　Livello di lettura: A2", 17, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Lunedì 2 novembre l'Italia cambia faccia: arriva il primo freddo vero della stagione, con piogge sul versante adriatico e la prima neve leggera in montagna, intorno ai 1.300–1.500 metri.")
f.para("Le previsioni parlano di un novembre più freddo della media. Non è una certezza, è una probabilità: a pagina 6 impariamo a leggerle senza paura.")
f.para("Il freddo, però, non ferma l'Italia: martedì 3 novembre apre a Milano il Forum Cultura, con più di 50 eventi tra musei e biblioteche, e nel fine settimana il paese si mette a tavola.")
f.para("Sabato 7 e domenica 8 novembre, a Milano, c'è la finale della Coppa del Mondo del Panettone, con pasticceri da 19 paesi; a Cremona apre la Festa del Torrone, fino al 22 novembre.")
f.para("E lo sport chiude la settimana: l'undicesima giornata di Serie A si gioca da venerdì 6 a domenica 8 novembre, con Genoa–Milan, Inter–Como e Fiorentina–Juventus domenica 8 novembre.")
f.para("Questa è la seconda edizione de La Lucerna in italiano: ogni settimana leggiamo l'Italia vera con te. Benvenuti al freddo!")
f.bridge("해설 — il primo freddo = 첫 추위 · il versante adriatico = 아드리아해 쪽 · la previsione = 예보 · assaggi = 맛보기예요.")
f.box("LA SETTIMANA IN CIFRE　이번 주", [
    ("1.300–1.500 — i metri di quota dove può cadere la prima neve leggera (초설이 내릴 수 있는 고도예요)", "serif", False, INK, 20.5, 1.35),
    ("50+ — gli eventi del Forum Cultura di Milano, dal 3 all'8 novembre (밀라노 문화 포럼 50개 이상 행사예요)", "serif", False, INK, 20.5, 1.35),
    ("19 — i paesi dei pasticceri alla finale del Panettone a Milano (밀라노 파네토네 결승 참가국 수예요)", "serif", False, INK, 20.5, 1.35),
    ("11ª — la giornata di Serie A del fine settimana (이번 주말 세리에 A 11라운드예요)", "serif", False, INK, 20.5, 1.35),
])
f.head("ADESSO TU　바로 연습", 25)
f.ex("A2", "문장 완성", "freddo", "il primo freddo = 첫 추위",
     "Lunedì 2 novembre arriva il primo ___ vero della stagione.", size=20, gap=7)
f.ex("A2", "문장 완성", "neve", "la prima neve leggera = 초설",
     "In montagna può cadere la prima ___ leggera.", size=20, gap=7)
f.ex("A2", "문장 완성", "Milano", "문화 포럼과 파네토네 결승은 모두 밀라노에서 열려요",
     "Il Forum Cultura apre martedì a ___.", size=20, gap=7)
f.ex("A2", "문장 완성", "Torrone", "크레모나 축제는 Festa del Torrone예요",
     "A Cremona apre la Festa del ___.", size=20, gap=7)
f.ex("A2", "문장 완성", "domenica", "세리에 A 11라운드는 일요일에 끝나요",
     "Genoa–Milan, Inter–Como e Fiorentina–Juventus si giocano ___ 8 novembre.", size=20, gap=7)
f.ex("B1", "문장 완성", "previsioni", "previsioni = 예보 (복수)",
     "Le ___ parlano di un novembre più freddo della media.", size=20, gap=7)
f.end_report()

# ---- la settimana (col 3) ----
gx, gw = COLX[3], CW
gy = 588
p.rect(gx, gy, gw, 700, fill=BOX)
p.text(gx + 22, gy + 40, "LA SETTIMANA", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "GIORNO PER GIORNO", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "이번 주 일정　Cosa succede, giorno per giorno", 19, "sans", False, GREY)
sett = [
    "LUN 2 — Commemorazione dei defunti; scuole chiuse in alcune regioni.",
    "MAR 3 — Apre il Forum Cultura a Milano; in serata, le coppe europee.",
    "MER–GIO 4–5 — Quarta giornata delle coppe europee.",
    "VEN 6 — Apre l'11ª giornata di Serie A.",
    "SAB 7 — Finale del Panettone a Milano; apre il Torrone a Cremona.",
    "DOM 8 — Serie A, 11ª giornata: le tre grandi di domenica.",
]
byy = gy + 150
for t in sett:
    byy = p.para(gx + 22, byy + 16, t, 20, "serif", False, INK, gw - 44, 1.36) + 6
p.text(gx + 22, byy + 16, "Le date sono quelle del calendario", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "degli eventi; gli orari possono cambiare.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 76, "일정은 각 행사 달력 기준이에요. 시간이 바뀔 수 있어요.", 16.5, "sans", False, GREY)

# ---- sommario (col 3) ----
sy = 1312
p.rect(gx, sy, gw, 340, fill="#f0eee5")
p.text(gx + 22, sy + 40, "IN QUESTO NUMERO　이번 호 차례", 24, "sans", True, OLIVE)
som = [
    ("Pag. 2", "Il freddo e il 2 novembre", "A2"),
    ("Pag. 3", "Panettone e torrone", "A2→B1"),
    ("Pag. 4", "La Serie A", "B1"),
    ("Pag. 5", "Dopo Lucca, i giovani", "B1"),
    ("Pag. 6", "Leggere le previsioni", "B2"),
    ("Pag. 7", "Frasi della settimana", "A2→B2"),
    ("Pag. 8", "Esercizi e risposte", "tutti"),
]
yy = sy + 84
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, OLIVE)
    p.text(gx + 88, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 40

# ---- parola della settimana (col 3) ----
my = 1652
p.text(gx, my + 24, "LA PAROLA DELLA SETTIMANA", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, OLIVE, 2)
p.text(gx, my + 76, "« il primo freddo »", 21.5, "serif", False, INK, italic=True)
y2 = p.para(gx, my + 108, "il primo freddo serio dopo un autunno mite. Questa settimana ha un programma: cultura, dolci, calcio.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, y2 + 4, "'첫 추위': 온화한 가을 뒤 첫 추위예요.", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1864, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
p.rect(ix, iy, iw, 320, fill=BOX)
illus_frost(p, ix + iw // 2 - 70, iy + 80, 2.0)
caption(p, ix, iy + 320, iw,
        "Il fiocco di neve: la prima neve leggera può cadere in montagna, intorno ai 1.300–1.500 metri. In pianura, per ora, arriva solo il freddo — e la voglia di dolci caldi. (Pagina 2)",
        "Disegno della redazione")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2300, tag="P1-freddo")
f2.head("IL FREDDO È ARRIVATO", 25)
f2.para("Giornate più corte, la prima neve in montagna, i musei che aprono le porte e le piazze che profumano di dolci: l'Italia di novembre mostra questa settimana tutto il suo programma.", 22.5)
f2.para("Il suo regalo per i lettori è un weekend di assaggi. Prendilo — e continua a leggere a pagina 2!", 22.5)
f2.end_report()
# col 3 IN BREVE
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX)
p.text(bx + 22, 1914, "IN BREVE　단신", 24, "sans", True, OLIVE)
brefs = [
    ("FREDDO", "Lunedì 2 novembre arriva il primo freddo: piogge adriatiche, neve in montagna. (Pagina 2)"),
    ("CULTURA", "Il Forum Cultura apre martedì 3 novembre: più di 50 eventi. (Pagina 5)"),
    ("DOLCI", "Weekend: finale del Panettone a Milano, Torrone a Cremona. (Pagina 3)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, OLIVE)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- quiz lampo ----
qy = 2312
p.hline(MX, RIGHT, qy, OLIVE, 2)
p.text(MX, qy + 36, "QUIZ LAMPO　번개 퀴즈", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "1면을 읽고 알맞은 답을 고르세요　정답은 8면", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2560, tag="P1-quiz")
qf.ex("A2", "객관식", "A", "첫 추위는 월요일 11월 2일에 찾아와요",
      "Il primo freddo arriva... A. lunedì 2 novembre · B. sabato 7 novembre · C. domenica 1° novembre", size=21)
qf.ex("A2", "객관식", "B", "초설은 1,300–1,500m쯤에 내려요",
      "La prima neve leggera può cadere intorno ai... A. 500 metri · B. 1.300–1.500 metri · C. 3.000 metri", size=21)
qf.ex("A2", "객관식", "C", "파네토네 결승은 밀라노에서 열려요",
      "La finale della Coppa del Mondo del Panettone è a... A. Cremona · B. Firenze · C. Milano", size=21)
qf.ex("A2", "객관식", "B", "세리에 A 11라운드는 일요일에 끝나요",
      "L'undicesima giornata di Serie A chiude... A. venerdì · B. domenica · C. lunedì", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-prima.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · VITA (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("VITA　생활", "La Lucerna", "LIVELLO A2　Il primo freddo e il 2 novembre　첫 추위와 추모의 날")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("Il primo freddo: come ci si veste e che cosa si mangia", 32)
f.byline("Dalla redazione de La Lucerna　Livello di lettura: A2")
f.para("Il primo freddo si sente subito: la mattina l'aria è pungente, la sera il buio arriva presto. Allora gli italiani tirano fuori dall'armadio il cappotto, la sciarpa e i guanti. Vestirsi «a strati» è la regola: una maglia, un maglione e, sopra, il cappotto.")
f.para("In casa si accendono i termosifoni. La sera, la cucina profuma di zuppe e di castagne arrosto: il freddo porta con sé i piatti caldi dell'autunno. E al mattino, prima di uscire, tutti guardano il cielo — e il telefono, per le previsioni.")
f.para("Il lunedì di questa settimana è un giorno speciale: il 2 novembre è la Commemorazione dei defunti, il giorno in cui gli italiani ricordano le persone care che non ci sono più. Molti portano i crisantemi al cimitero: è il fiore di novembre.")
f.para("E la scuola? Il 2 novembre è festa in Calabria, Campania, Emilia-Romagna, Sardegna, Sicilia, Umbria, Valle d'Aosta e Trento; in Veneto le scuole sono chiuse dal 30 ottobre al 2 novembre, e a Bolzano la sospensione dura dal 2 all'8 novembre. In altre regioni, invece, è un lunedì normale.")
f.head("E LA SETTIMANA SCORSA?", 25)
f.para("La settimana scorsa si è chiusa con due appuntamenti attesi: la 60ª edizione di Lucca Comics & Games, dal 28 ottobre al 1° novembre, e la festa di Ognissanti, domenica 1° novembre. Quest'anno Ognissanti è caduta di domenica: niente ponte, come avevamo previsto nel VOL.1.", 23.5)
f.para("Anche la manovra, la legge di bilancio, era attesa al voto intorno al 28 ottobre: il punto difficile resta il contributo di banche e assicurazioni. Al momento di andare in stampa, l'esito non era ancora confermato: ne parliamo a pagina 6.", 23.5)
f.bridge("인쇄할 때 표결 결과는 아직 확인되지 않았어요. 6면을 보세요.")
f.box("LA FRASE PER RICORDARE　암기문장", [
    ("«Fa freddo, copriti bene!» Così dicono le nonne italiane: quando arriva il primo freddo, il consiglio è uno solo — vestirsi bene, a strati.", "serif", False, INK, 21.5, 1.4),
])
f.gloss("il cappotto 외투 · la sciarpa 목도리 · i guanti 장갑 · a strati 겹쳐 입기 · il termosifone 난방기 · il crisantemo 국화")
f.end_report()

# col 3: facts + e tu? (sequential, measured)
ix = COLX[3]
facts = ["Il primo freddo porta piogge sul versante adriatico e neve leggera in montagna, intorno ai 1.300–1.500 metri.",
         "Il 2 novembre è la Commemorazione dei defunti: il fiore del giorno è il crisantemo.",
         "In alcune regioni il 2 novembre è festa per le scuole; in altre è un lunedì normale."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "LO SAPEVI?", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E tu? Che cosa metti quando arriva il primo freddo: cappotto, sciarpa o guanti? Scrivi due frasi in italiano e mandale alla redazione: le migliori escono nel VOL.3 (pagina 7, «Lettere dei lettori»)."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("첫 추위가 오면 무엇을 입어요: 외투, 목도리, 장갑? 이탈리아어로 두 문장을 써서 편집부로 보내 주세요.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E TU?　내 이야기", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "첫 추위가 오면 무엇을 입어요: 외투, 목도리, 장갑? 이탈리아어로 두 문장을 써서 편집부로 보내 주세요.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- Il 2 novembre wide box ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, OLIVE, 2)
p.text(MX, dy + 28, "IL 2 NOVEMBRE　추모의 날", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "Un giorno di memoria, in tutta Italia", 20, "sans", False, GREY, anchor="end")
p.para(MX, dy + 72, "Il 2 novembre, il giorno dopo Ognissanti, gli italiani vanno al cimitero con i crisantemi: fiori bianchi, gialli e viola per ricordare chi non c'è più. È un giorno silenzioso, di famiglia. Le scuole, in molte regioni, restano chiuse — e il lunedì comincia piano, con il primo freddo.", 22.5, "serif", False, INK, RIGHT - MX, 1.45)
p.para(MX, dy + 196, "Attenzione alla parola: «defunto» è una parola gentile per dire «morto». «Commemorazione» vuol dire «ricordo insieme»: si commemora una persona, si ricorda un giorno.", 21, "serif", False, INK, RIGHT - MX, 1.45)

# ---- P2 exercises ----
ey = dy + 282
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ESERCIZI　제 2 면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면　문제는 레벨이 섞여 있을 수 있어요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P2-ex")
e.head("A　CHE COSA SERVE?", 25)
e.bridge("이탈리아어로 문장을 완성하세요.")
e.ex("A2", "문장 완성", "cappotto", "cappotto = 외투",
     "Quando fa freddo, metto il ___.", instr="빈칸 채우기", size=20, gap=8)
e.ex("A2", "문장 완성", "sciarpa", "sciarpa = 목도리",
     "Per il collo, metto la ___.", instr="빈칸 채우기", size=20, gap=8)
e.ex("A2", "문장 완성", "guanti", "guanti = 장갑 (복수)",
     "Per le mani, metto i ___.", instr="빈칸 채우기", size=20, gap=8)
e.ex("A2", "문장 완성", "crisantemi", "crisantemi = 국화 (복수)",
     "Il 2 novembre portiamo i ___ al cimitero.", instr="빈칸 채우기", size=20, gap=8)
e.ex("A2", "문장 완성", "termosifoni", "termosifoni = 난방기 (복수)",
     "In casa si accendono i ___.", instr="빈칸 채우기", size=20, gap=8)
e.head("B　IL PRESENTE", 25)
e.bridge("동사의 현재형으로 빈칸을 채우세요.")
e.ex("A2", "문장 완성", "fa", "fare freddo: fa freddo (날씨)",
     "La mattina ___ freddo.", instr="빈칸 채우기", size=20, gap=8)
e.ex("A2", "문장 완성", "metto", "mettere: io → metto",
     "Io ___ il cappotto prima di uscire.", instr="빈칸 채우기", size=20, gap=8)
e.ex("A2", "문장 완성", "portano", "portare: loro → portano",
     "Molti italiani ___ i crisantemi al cimitero.", instr="빈칸 채우기", size=20, gap=8)
e.ex("A2", "문장 완성", "guardano", "guardare: loro → guardano",
     "Tutti ___ il cielo prima di uscire.", instr="빈칸 채우기", size=20, gap=8)
e.ex("A2", "문장 완성", "resta", "restare: la scuola → resta (lei)",
     "In molte regioni, la scuola ___ chiusa il 2 novembre.", instr="빈칸 채우기", size=20, gap=8)
e.head("C　COMPRENSIONE", 25)
e.bridge("2면 기사를 읽고 알맞은 답을 고르세요.")
e.ex("A2", "객관식", "B", "11월 2일은 추모의 날이에요",
     "Il 2 novembre è... A. Ognissanti · B. la Commemorazione dei defunti · C. il primo giorno di scuola", size=20, gap=8)
e.ex("A2", "객관식", "A", "추모의 날 꽃은 국화예요",
     "Il fiore del 2 novembre è... A. il crisantemo · B. la rosa · C. il tulipano", size=20, gap=8)
e.ex("A2", "객관식", "C", "겹쳐 입기: a strati",
     "Vestirsi «a strati» vuol dire... A. vestirsi di nero · B. vestirsi in fretta · C. mettere più strati, uno sopra l'altro", size=20, gap=8)
e.ex("B1", "객관식", "B", "올해 만성절은 일요일이라 연휴가 없어요",
     "Ognissanti, quest'anno, è caduta... A. di lunedì · B. di domenica · C. di sabato", size=20, gap=8)
e.head("D　LE PAROLE DEL FREDDO", 25)
e.match_set("A2", "단어 짝짓기",
            ["il cappotto", "la sciarpa", "il crisantemo", "il termosifone"],
            ["il fiore di novembre, per il 2 novembre",
             "il calorifero di casa, che si accende d'inverno",
             "il vestito lungo e pesante per il freddo",
             "la striscia di lana per il collo"],
            ["c", "d", "a", "b"],
            ["cappotto=추위 막는 외투 c", "sciarpa=목도리 d", "crisantemo=11월의 꽃 a", "termosifone=난방기 b"],
            instr="단어와 뜻 짝짓기")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-vita.svg")
print("P2 saved, exercises so far:", len(REG))
