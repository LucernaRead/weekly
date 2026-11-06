# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-it-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · GIOVANI (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("GIOVANI · 청년", "La Lucerna", "LIVELLO B1 · Lucca Comics e il cinema dei giovani · 루카 코믹스와 청년 영화")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-main")
f.title("Lucca si prepara: tra una settimana è Comics & Games", 37)
f.byline("Dalla redazione de La Lucerna · Livello di lettura: B1")
f.para("Manca una settimana all'evento giovane più grande d'Italia: Lucca Comics & Games. La 60ª edizione, con il tema «Legacy», apre mercoledì 28 ottobre e chiude domenica 1° novembre, il giorno di Ognissanti.")
f.para("I numeri sono da record: al massimo 80.000 visitatori al giorno dentro le mura di Lucca. I biglietti costano da 26,50 a 34,50 euro; l'abbonamento per i cinque giorni costa 95 euro.")
f.para("Questa è la settimana dei preparativi: il termine per ricevere il braccialetto a casa è scaduto il 16 ottobre, e ora i fan preparano i cosplay, studiano le code e organizzano il viaggio. Per molti giovani è la festa più importante dell'autunno.")
f.para("E per chi resta a Roma? La Festa del Cinema ha una sezione per i giovani: Alice nella città. Giovedì 22 ottobre: la presentazione dell'app Rome City of Film e le serate di cinema muto alla Casa del Cinema — film di cento anni fa, grandi anche senza parole.")
f.para("Tra i titoli di cui parlano i giornali: un documentario sulla sciatrice Federica Brignone e la serie VisionQuest con Paul Bettany. Molte sono anteprime: film che il pubblico vede per la prima volta.")
f.box("IL PIANO DELLA SETTIMANA", [
    ("1. Finisci il cosplay: manca una settimana(코스프레 완성하기: 일주일 남았어요)", "serif", False, INK, 21, 1.36),
    ("2. Controlla il braccialetto e il biglietto(팔찌와 티켓 확인하기)", "serif", False, INK, 21, 1.36),
    ("3. Studia la mappa di Lucca e le code(루카 지도와 줄 서기 살펴보기)", "serif", False, INK, 21, 1.36),
    ("4. Giovedì: serata di cinema muto a Roma(목요일: 로마 무성 영화의 밤)", "serif", False, INK, 21, 1.36),
    ("5. Domenica: ultimo giorno della Festa del Cinema(일요일: 영화제 마지막 날)", "serif", False, INK, 21, 1.36),
])
f.gloss("il braccialetto 팔찌 (입장권) · la coda 줄 · l'anteprima 시사회 · muto 소리 없는 / 무성 영화의예요.")
f.end_report()

# col 3: chaplin image + facts + e tu? + coffee box (sequential)
ix = COLX[3]
image(p, "chaplin.jpg", ix, 200, CW, 300)
cy3 = caption(p, ix, 500, CW, "Charlie Chaplin in «La febbre dell'oro» (1925): cento anni fa il cinema era muto. Giovedì 22 ottobre, alla Casa del Cinema di Roma, una serata è dedicata ai film muti.",
              "Foto: Wikimedia Commons — dominio pubblico")
facts = ["60ª edizione, tema «Legacy»: dal 28 ottobre al 1° novembre.",
         "Massimo 80.000 visitatori al giorno, dentro le mura di Lucca.",
         "Biglietti: 26,50–34,50 €; abbonamento di 5 giorni: 95 €."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "LUCCA IN NUMERI", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E tu? Vai a Lucca o resti a guardare film? Scrivi due frasi in italiano."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("루카에 가요, 아니면 집에서 영화를 봐요? 두 문장을 써서 보내 주세요.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E TU? · 내 이야기", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "루카에 가요, 아니면 집에서 영화를 봐요? 두 문장을 써서 보내 주세요.", 20, "sans", False, GREY, CW - 44, 1.42)
ky3 = ey3 + eh + 26
kb = ("Secondo Google, nel 2026 le ricerche italiane sul caffè non sono mai state così alte: l'espresso resta il numero uno, la moka resta amatissima in Italia, e crescono il flat white e il latte d'avena. "
      "Record anche per le ricerche sulla «skincare coreana», la cura della pelle in stile coreano.")
kh = 62 + len(wrap(kb, "serif", False, 21.5, CW - 44)) * 30.5 + 16
p.rect(ix, ky3, CW, kh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ky3 + 16
p.text(ix + 22, yy3 + 26, "COSA CERCANO GLI ITALIANI", 22, "sans", True, OLIVE)
yy3 += 52
p.para(ix + 22, yy3 + 21, kb, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P5 col3 ends", ky3 + kh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ESERCIZI · 제 5 면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면 · 문제는 레벨이 섞여 있을 수 있어요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · COMPRENSIONE", 25)
e.expl("5면 기사를 읽고 알맞은 답을 고르세요.")
e.ex("B1", "객관식", "B", "루카 코믹스는 60회째예요",
     "Lucca Comics & Games è alla sua... A. 50ª edizione · B. 60ª edizione · C. 21ª edizione", size=20, gap=8)
e.ex("B1", "객관식", "B", "10월 28일 수요일에 열려요",
     "Il festival di Lucca apre... A. il 25 ottobre · B. il 28 ottobre · C. il 1° novembre", size=20, gap=8)
e.ex("B1", "객관식", "C", "5일 이용권은 95유로예요",
     "L'abbonamento per cinque giorni costa... A. 34,50 € · B. 80 € · C. 95 €", size=20, gap=8)
e.ex("B1", "객관식", "A", "Alice nella città는 청년 섹션이에요",
     "Alice nella città è... A. una sezione per i giovani · B. un'app · C. un film muto", size=20, gap=8)
e.ex("B1", "객관식", "A", "팔찌 자택 배송 마감은 10월 16일이었어요",
     "Il termine per il braccialetto a casa è scaduto... A. il 16 ottobre · B. il 22 ottobre · C. il 28 ottobre", size=20, gap=8)
e.head("B · LE PAROLE DEL TESTO", 25)
e.expl("상자 안의 단어로 빈칸을 채우세요. 주의: 복수형으로 바꿔야 하는 단어도 있어요.")
e.para("cosplay · braccialetto · coda · anteprima · muto · abbonamento", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "문장 완성", "braccialetto", "braccialetto = 팔찌",
     "Per entrare a Lucca serve il ___ al polso.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "anteprima", "anteprima = 시사회",
     "Un film visto per la prima volta dal pubblico è un'___.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "muti", "muti = 소리 없는 (남성 복수)",
     "I film di cento anni fa sono ___: senza parole.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "abbonamento", "abbonamento = 이용권/정기권",
     "Con l'___ di cinque giorni entri sempre.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "coda", "coda = 줄, 대기 줄",
     "Davanti ai padiglioni c'è sempre una lunga ___.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "cosplay", "cosplay = 코스프레 의상",
     "Molti fan preparano un ___ da indossare a Lucca.", instr="빈칸 채우기", size=20, gap=8)
e.head("C · IL FUTURO", 25)
e.expl("단순 미래 (futuro semplice)로 완성하세요.")
e.ex("B1", "문장 완성", "prepareremo", "preparare의 미래형 noi: prepareremo",
     "Domani noi ___ (preparare) i cosplay.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B2", "문장 완성", "andrò", "andare의 미래형은 불규칙해요: andrò",
     "La prossima settimana io ___ (andare) a Lucca.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B2", "문장 완성", "ci saranno", "esserci의 미래형: ci saranno (있을 거예요)",
     "A Lucca ___ (esserci) migliaia di giovani.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "chiuderà", "chiudere의 미래형: chiuderà",
     "Il festival di Lucca ___ (chiudere) il 1° novembre.", instr="빈칸 채우기", size=20, gap=8)
e.head("D · VERO O FALSO?", 25)
e.ex("B1", "읽기 판단", "Vero", "하루 최대 8만 명이에요",
     "A Lucca entrano al massimo 80.000 visitatori al giorno. Vero o falso?", instr="판단", size=20, gap=8)
e.ex("B1", "읽기 판단", "Vero", "무성 영화의 밤은 Casa del Cinema에서 열려요",
     "Le serate di cinema muto sono alla Casa del Cinema. Vero o falso?", instr="판단", size=20, gap=8)
e.ex("B2", "읽기 판단", "Falso", "espresso가 여전히 커피 검색 1위예요",
     "L'espresso non è più la ricerca numero uno sul caffè. Vero o falso?", instr="판단", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-giovani.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · APPROFONDIMENTO (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("APPROFONDIMENTO · 심층", "La Lucerna", "LIVELLO B2 · La manovra 2027 · 2027년 예산안")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1520, tag="P6-main")
f.title("La manovra 2027: perché il voto slitta al 28 ottobre", 37)
f.byline("Dalla redazione de La Lucerna · Livello di lettura: B2 · La politica nazionale italiana")
f.para("È la storia politica italiana della settimana: la manovra, la legge di bilancio per il 2027. Lunedì 19 ottobre i leader della coalizione si sono incontrati a Palazzo Chigi, a Roma. Ma il voto del Consiglio dei ministri non arriva venerdì 23 ottobre, come previsto: slitta a mercoledì 28 ottobre circa.")
f.para("Perché il rinvio? Il punto difficile è il contributo di circa 5 miliardi di euro chiesto a banche e assicurazioni. La cifra è nel Documento programmatico di bilancio (il DPB), il piano che l'Italia ha mandato a Bruxelles il 15 ottobre.")
f.para("Il DPB pubblica le previsioni per il 2027: la crescita è stimata a +0,8% e il deficit è al 3,4% del PIL, il prodotto interno lordo. Sono previsioni, non risultati: numeri che descrivono un piano, non ancora la realtà.")
f.para("Dove vanno i soldi? Il piano prevede circa 5 miliardi per le famiglie e le spese sociali e circa 3,4 miliardi per aiutare le imprese. In totale, la manovra vale circa 23,5 miliardi di euro.")
f.para("Per il lettore, la lezione è una: leggi le date e le fonti. Un voto previsto non è un voto fatto: una previsione non è un dato finale. Mercoledì 28 ottobre sapremo se il Consiglio dei ministri approva il testo — La Lucerna lo racconterà nel prossimo numero.")
f.gloss("la manovra 예산안 · il rinvio 연기 · i miliardi 10억 (단위) · il deficit 적자 · la previsione 전망이에요.")
f.end_report()

# col 3: timeline + leggere i numeri (sequential, measured)
bx = COLX[3]
p.rect(bx, 200, CW, 640, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 240, "LA STRADA DELLA MANOVRA", 22, "sans", True, OLIVE)
steps = [
    ("15 OTT.", "L'Italia manda a Bruxelles il DPB, il documento con il piano di bilancio."),
    ("19 OTT.", "Vertice della coalizione a Palazzo Chigi: il testo non è ancora pronto."),
    ("23 OTT.", "La data prevista per il voto del Consiglio dei ministri — ma slitta."),
    ("28 OTT.", "La nuova data attesa per il voto (circa): la decisione arriva la prossima settimana."),
]
sy3 = 282
for w, t in steps:
    p.text(bx + 22, sy3 + 21, w, 20, "sans", True, BRICK)
    sy3 = p.para(bx + 164, sy3 + 21, t, 21, "serif", False, INK, CW - 186, 1.4) + 16
by3 = 866
bb = ("Davanti a un numero politico, fai tre domande: chi lo pubblica? Quando? "
      "È una previsione o un dato finale? Senza queste tre risposte, una cifra dice poco.")
bh = 62 + len(wrap(bb, "serif", False, 21.5, CW - 44)) * 30.5 + 16
p.rect(bx, by3, CW, bh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = by3 + 16
p.text(bx + 22, yy3 + 26, "LEGGERE I NUMERI", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, bb, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P6 col3 ends", by3 + bh)

# ---- DPB chart (published figures, honestly captioned) ----
gy = 1566
p.hline(MX, RIGHT, gy - 18, GOLD, 2)
p.text(MX, gy + 10, "LE CIFRE DEL DPB · DPB의 숫자 (Documento programmatico di bilancio, 15 ottobre 2026)", 26, "sans", True, OLIVE)
dpb = [("Banche e assicurazioni (contributo chiesto)", 5.0),
       ("Famiglie e spese sociali", 5.0),
       ("Aiuto alle imprese", 3.4)]
bx1, bw_, bhh = MX, 2 * CW + GUT, 322
p.rect(bx1, gy + 28, bw_, bhh, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx1 + 22, gy + 68, "TRE VOCI DEL PIANO · miliardi di euro", 21, "sans", True, INK)
yy = gy + 96
for lab, v in dpb:
    p.text(bx1 + 22, yy + 24, lab, 20, "serif", True, INK)
    labw = text_w(lab, "serif", True, 20)
    p.rect(bx1 + 40 + labw, yy + 6, v * 34, 22, fill=OLIVE)
    p.text(bx1 + 58 + labw + v * 34, yy + 24, f"{v:.1f}".replace(".", ",") + " miliardi", 20.5, "serif", False, INK)
    yy += 38
p.para(bx1 + 22, gy + bhh - 62, "Tre voci pubblicate nel DPB del 15 ottobre — non è il totale della manovra (circa 23,5 miliardi).", 17.5, "sans", False, GREY, bw_ - 44, 1.3)
# right box: percentages
bx2 = COLX[2]
p.rect(bx2, gy + 28, bw_, bhh, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx2 + 22, gy + 68, "LE PREVISIONI 2027 · 2027년 전망", 21, "sans", True, INK)
p.para(bx2 + 22, gy + 118, "Crescita stimata: +0,8%", 23, "serif", True, INK, bw_ - 44, 1.35)
p.para(bx2 + 22, gy + 158, "Deficit: 3,4% del PIL", 23, "serif", True, INK, bw_ - 44, 1.35)
p.para(bx2 + 22, gy + 198, "Sono previsioni del piano, non dati finali: il futuro si scrive con i numeri che arrivano dopo.", 19.5, "serif", False, INK, bw_ - 44, 1.4)
p.para(bx2 + 22, gy + bhh - 62, "Fonte: DPB, documento mandato a Bruxelles il 15 ottobre 2026.", 17.5, "sans", False, GREY, bw_ - 44, 1.3)

# ---- P6 exercises ----
ey = 1930
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ESERCIZI · 제 6 면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면 · 문제는 레벨이 섞여 있을 수 있어요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · LEGGERE IL GRAFICO", 25)
e.expl("위의 두 도표를 보고 알맞은 답을 고르세요.")
e.ex("B2", "객관식", "B", "은행과 보험사에 요구하는 부담금은 약 50억 유로예요",
     "Il contributo chiesto a banche e assicurazioni è di... A. 3,4 miliardi · B. 5 miliardi · C. 23,5 miliardi", size=18, gap=2)
e.ex("B2", "객관식", "A", "가정과 사회 지출은 약 50억 유로예요",
     "Per le famiglie e le spese sociali il piano prevede... A. 5 miliardi · B. 3,4 miliardi · C. 0,8 miliardi", size=18, gap=2)
e.ex("B2", "객관식", "B", "5 + 5 + 3,4 = 13,4 (합계가 아니에요)",
     "Le tre voci del grafico, insieme, fanno... A. 10 miliardi · B. 13,4 miliardi · C. 23,5 miliardi", size=18, gap=2)
e.ex("B2", "객관식", "A", "5 − 3,4 = 1,6",
     "La differenza tra le famiglie (5) e le imprese (3,4) è... A. 1,6 miliardi · B. 2,6 miliardi · C. 8,4 miliardi", size=18, gap=2)
e.ex("B2", "객관식", "B", "2027년 성장 전망은 +0,8%예요",
     "La crescita prevista per il 2027 è... A. +3,4% · B. +0,8% · C. +5%", size=18, gap=2)
e.ex("B2", "객관식", "A", "적자는 GDP의 3,4%예요",
     "Il deficit previsto è il... A. 3,4% del PIL · B. 34% del PIL · C. 0,8% del PIL", size=18, gap=2)
e.head("B · COMPRENSIONE", 25)
e.ex("B2", "객관식", "B", "표결은 약 10월 28일로 미뤄졌어요",
     "Il voto del Consiglio dei ministri... A. è già avvenuto il 19 ottobre · B. slitta a circa il 28 ottobre · C. è cancellato", size=18, gap=2)
e.ex("B2", "객관식", "A", "어려운 부분은 은행과 보험사의 부담금이에요",
     "Il punto difficile della manovra è... A. il contributo di banche e assicurazioni · B. il nome della legge · C. la data del voto", size=18, gap=2)
e.ex("B2", "객관식", "A", "DPB는 10월 15일에 브뤼셀로 보냈어요",
     "Il DPB è stato mandato a Bruxelles... A. il 15 ottobre · B. il 19 ottobre · C. il 28 ottobre", size=18, gap=2)
e.ex("B2", "객관식", "B", "이 숫자들은 최종 결과가 아니라 전망이에요",
     "Le cifre del DPB sono... A. risultati finali · B. previsioni · C. errori di stampa", size=18, gap=2)
e.head("C · IL CONGIUNTIVO", 25)
e.ex("B2", "문장 완성", "slitti", "è possibile che + 접속법 slitti",
     "È possibile che il voto ___ (slittare) ancora.", instr="빈칸 채우기", size=18, gap=2)
e.ex("B2", "문장 완성", "controllino", "bisogna che + 접속법 controllino",
     "Bisogna che i lettori ___ (controllare) sempre la fonte.", instr="빈칸 채우기", size=18, gap=2)
e.ex("B2", "문장 완성", "riunisce", "scrivono che 뒤에는 사실을 쓰니 직설법 riunisce를 써요",
     "I giornali scrivono che il Consiglio si ___ (riunire) mercoledì 28.", instr="빈칸 채우기", size=18, gap=2)
e.ex("B2", "문장 완성", "sia", "è importante che + 접속법 sia",
     "È importante che la manovra ___ (essere) chiara per tutti.", instr="빈칸 채우기", size=18, gap=2)
e.head("D · LE PAROLE DEL DIBATTITO", 25)
e.expl("상자 안의 단어로 빈칸을 채우세요: manovra · rinvio · miliardo · previsione")
e.ex("B2", "문장 완성", "manovra", "manovra = 예산안",
     "La legge di bilancio si chiama anche la ___.", instr="빈칸 채우기", size=18, gap=2)
e.ex("B2", "문장 완성", "miliardo", "un miliardo = 10억",
     "Un ___ è mille milioni di euro.", instr="빈칸 채우기", size=18, gap=2)
e.ex("B2", "문장 완성", "rinvio", "rinvio = 연기",
     "Il voto arriva più tardi del previsto: è un ___.", instr="빈칸 채우기", size=18, gap=2)
e.ex("B2", "문장 완성", "previsione", "previsione = 전망",
     "Un numero che descrive il futuro, non il presente, è una ___.", instr="빈칸 채우기", size=18, gap=2)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-approfondimento.svg")
print("P6 saved, exercises so far:", len(REG))
