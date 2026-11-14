# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA　문화", "La Lucerna", "A2 → B1　Le sagre d'autunno　가을 음식 축제")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("Le sagre d'autunno: il tartufo bianco è il re", 32)
f.byline("Dalla redazione de La Lucerna　Livello di lettura: A2 → B1")
f.para("In autunno, l'Italia mangia fuori casa. Nei paesi e nelle città è la stagione delle sagre: feste di piazza con i prodotti della terra. Il re della stagione è il tartufo bianco, il fungo più prezioso d'Italia.")
f.para("Ad Alba, in Piemonte, la Fiera del Tartufo Bianco è aperta dal 10 ottobre al 6 dicembre: quasi due mesi di mercati, profumi e piatti speciali. La fiera è iniziata sabato 10 ottobre e chiude domenica 6 dicembre.")
f.para("Questo fine settimana, sabato 24 e domenica 25 ottobre, Montaione, in Toscana, celebra la sua festa del tartufo. E a Bagolino, in Lombardia, il weekend è del formaggio Bagòss: un formaggio di montagna dal nome difficile e dal sapore forte.")
f.para("Sempre sabato 24 ottobre apre a Volterra Volterragusto, una festa dei sapori della Toscana. E ovunque, nelle piazze, si trovano le castagne arrosto: l'autunno italiano ha il profumo della castagna calda.")
f.gloss("il tartufo 트러플 · la sagra 음식 축제/시장 · il profumo 향기 · arrosto 구운 · la pittrice 여성 화가예요.")
f.head("UNA GRANDE PITTRICE A FIRENZE", 22)
f.para("Mercoledì 21 ottobre apre a Firenze, al Museo degli Innocenti, la mostra «Artemisia Gentileschi a Firenze». Artemisia (1593–1656 circa) è una delle pittrici più famose del Seicento: le sue donne sono forti, coraggiose e vive.")
f.para("La mostra resta aperta fino al 4 aprile 2027 e presenta anche due opere di Caravaggio, il grande maestro della luce e dell'ombra. La pittura antica diventa notizia di questa settimana perché la mostra apre proprio mercoledì.")
f.end_report()

# col 3: truffle image + facts + e tu? (sequential)
ix = COLX[3]
image(p, "tartufo.jpg", ix, 200, CW, 265)
cy3 = caption(p, ix, 465, CW, "Un tartufo bianco, il fungo più prezioso d'Italia. Ad Alba la fiera dura dal 10 ottobre al 6 dicembre; questo weekend, festa del tartufo anche a Montaione.",
              "Foto: Wikimedia Commons — dominio pubblico")
facts = ["Alba: la Fiera del Tartufo Bianco dura dal 10 ottobre al 6 dicembre.",
         "Montaione (Toscana): festa del tartufo, sabato 24 e domenica 25 ottobre.",
         "Bagolino (Lombardia): weekend del formaggio Bagòss, il 24 e 25 ottobre."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "LE SAGRE DEL WEEKEND", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E tu? Qual è il piatto dell'autunno nel tuo paese? Scrivi due frasi in italiano e mandale alla redazione."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("여러분의 고향에서는 가을에 무엇을 먹어요? 두 문장을 써서 보내 주세요.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E TU?　내 이야기", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "여러분의 고향에서는 가을에 무엇을 먹어요? 두 문장을 써서 보내 주세요.", 20, "sans", False, GREY, CW - 44, 1.42)
ay3 = ey3 + eh + 22
image(p, "artemisia.jpg", ix, ay3, CW, 165)
acy = caption(p, ix, ay3 + 165, CW, "Artemisia Gentileschi, «Giuditta decapita Oloferne» (versione di Napoli). A Firenze, la sua mostra apre mercoledì 21 ottobre.",
              "Foto: Wikimedia Commons — dominio pubblico")
print("P3 col3 ends", acy)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ESERCIZI　제 3 면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면　문제는 레벨이 섞여 있을 수 있어요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P3-ex")
e.head("A　COMPRENSIONE", 25)
e.expl("3면 기사를 읽고 알맞은 답을 고르세요.")
e.ex("A2", "객관식", "B", "화이트 트러플 축제는 알바에서 열려요",
     "La Fiera del Tartufo Bianco è a... A. Bagolino · B. Alba · C. Volterra", size=20, gap=8)
e.ex("A2", "객관식", "C", "알바 트러플 축제는 12월 6일에 막을 내려요",
     "La fiera di Alba chiude... A. il 25 ottobre · B. il 1° novembre · C. il 6 dicembre", size=20, gap=8)
e.ex("A2", "객관식", "B", "바골리노는 Bagòss 치즈 주말이에요",
     "A Bagolino, il weekend è del... A. tartufo · B. formaggio Bagòss · C. vino", size=20, gap=8)
e.ex("B1", "객관식", "A", "아르테미시아 전시는 10월 21일 수요일에 열려요",
     "La mostra su Artemisia apre... A. mercoledì 21 ottobre · B. sabato 24 ottobre · C. domenica 25 ottobre", size=20, gap=8)
e.ex("B1", "객관식", "B", "전시에는 카라바조 작품도 두 점 있어요",
     "Nella mostra ci sono anche opere di... A. Leonardo · B. Caravaggio · C. Michelangelo", size=20, gap=8)
e.head("B　LE PAROLE DEL TESTO", 25)
e.expl("상자 안의 단어로 빈칸을 채우세요.")
e.para("tartufo · sagra · profumo · castagne · pittrice · formaggio", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "문장 완성", "tartufo", "tartufo = 트러플",
     "Il ___ bianco è il fungo più prezioso d'Italia.", instr="빈칸 채우기", size=20, gap=8)
e.ex("A2", "문장 완성", "sagra", "sagra = 지역 음식 축제",
     "Una ___ è una festa di piazza con i prodotti della terra.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "profumo", "profumo = 향기",
     "L'autunno ha il ___ della castagna calda.", instr="빈칸 채우기", size=20, gap=8)
e.ex("A2", "문장 완성", "castagne", "castagne arrosto = 군밤 (복수)",
     "Nelle piazze si trovano le ___ arrosto.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "pittrice", "pittrice = 여성 화가",
     "Artemisia è una grande ___ del Seicento.", instr="빈칸 채우기", size=20, gap=8)
e.ex("A2", "문장 완성", "formaggio", "formaggio = 치즈",
     "Il Bagòss è un ___ di montagna.", instr="빈칸 채우기", size=20, gap=8)
e.head("C　IL PASSATO PROSSIMO", 25)
e.expl("passato prossimo (근과거)로 완성하세요. 조동사 avere / essere에 주의하세요.")
e.ex("B1", "문장 완성", "è iniziata", "iniziare는 essere를 써요. 여성형으로 맞춘 è iniziata",
     "La fiera ___ (iniziare) il 10 ottobre.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "abbiamo visitato", "visitare는 avere를 써요: abbiamo visitato",
     "Noi ___ (visitare) la mostra di Artemisia.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "è andato", "andare는 essere를 써요: è andato",
     "Marco ___ (andare) alla sagra sabato.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "hanno aperto", "aprire는 avere를 써요: hanno aperto",
     "Le sagre ___ (aprire) il fine settimana.", instr="빈칸 채우기", size=20, gap=8)
e.head("D　COSTRUISCI LE FRASI", 25)
e.expl("단어를 배열해 알맞은 문장을 만드세요.")
e.ex("B1", "문장 만들기", "La fiera è iniziata il 10 ottobre.", "주어 + essere + 과거분사 + 날짜",
     "la fiera / è iniziata / il 10 ottobre → ___", instr="문장 만들기", size=20, gap=8)
e.ex("A2", "문장 만들기", "A Bagolino il formaggio è il re.", "장소가 앞에, 주어가 뒤에 와요",
     "a Bagolino / il formaggio / è il re → ___", instr="문장 만들기", size=20, gap=8)
e.ex("B1", "문장 만들기", "La mostra resta aperta fino ad aprile.", "resta aperta = 계속 열려 있는 것",
     "la mostra / resta aperta / fino ad aprile → ___", instr="문장 만들기", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT　스포츠", "La Lucerna", "LIVELLO B1　La Serie A e l'Europa　세리에 A와 유럽 대회")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("L'ottava giornata: Napoli–Roma e Inter–Fiorentina", 32)
f.byline("Dalla redazione sportiva de La Lucerna　Livello di lettura: B1")
f.para("È una settimana di grande calcio. Mercoledì sera l'Inter gioca in Champions League a San Siro contro lo Shakhtar Donetsk (21:00), e giovedì l'Atalanta è in trasferta ad Amsterdam contro l'Ajax, in Conference League. Attenzione: queste partite si giocano dopo la chiusura del giornale — qui sono una presentazione, senza risultati.")
f.para("Poi arriva l'ottava giornata di Serie A, da venerdì 23 a domenica 25 ottobre. La partita più attesa è sabato 24 ottobre alle 18:00: Napoli–Roma, la grande sfida tra il Sud e la capitale.")
f.para("Domenica 25 ottobre, alle 12:30, l'Inter incontra la Fiorentina a San Siro. È una partita speciale: è la prima della domenica con l'ora solare. Chi guarda la partita a pranzo ha già dormito un'ora in più.")
f.para("E dall'America arriva il basket: la stagione NBA comincia questa settimana, e anche in Italia si cercano notizie su Spurs–Thunder, la partita di Wembanyama (ricerca in crescita su Google Trends in Italia, istantanea di martedì).")
f.gloss("la giornata 라운드 · la sfida 강팀 대결 · la presentazione 경기 전 소개 · in trasferta 원정 경기예요.")
f.end_report()

# col 3: data box + e tu? (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 436, fill=BOX)
p.text(bx + 22, 240, "LE PARTITE DA SEGNARE", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "Mercoledì 21 ottobre, 21:00 · Inter – Shakhtar Donetsk (Champions League, San Siro) — si gioca dopo la chiusura del giornale. Giovedì 22 ottobre · Ajax – Atalanta (Conference League, Amsterdam) — presentazione. Sabato 24 ottobre, 18:00 · Napoli – Roma (Serie A, 8ª giornata). Domenica 25 ottobre, 12:30 · Inter – Fiorentina (Serie A) — la prima partita con l'ora solare.", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 662
etvous = "E tu? Quale partita guardi questo fine settimana? Scrivi due frasi in italiano."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("이번 주말에는 어떤 경기를 봐요? 이탈리아어로 두 문장을 써서 보내 주세요.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "E TU?　내 이야기", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "이번 주말에는 어떤 경기를 봐요? 이탈리아어로 두 문장을 써서 보내 주세요.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "LA SETTIMANA DEL CALCIO　축구 주간", 26, "sans", True, OLIVE)
rows = [
    ("Mer 21.10", "21:00 · Champions", "Inter – Shakhtar Donetsk (San Siro) — partita della sera, dopo la chiusura del giornale"),
    ("Gio 22.10", "Conference League", "Ajax – Atalanta (Amsterdam) — presentazione, senza risultato"),
    ("Ven–Dom", "Serie A · 8ª giornata", "L'ottava giornata si gioca da venerdì 23 a domenica 25 ottobre"),
    ("Sab 24.10", "18:00 · Serie A", "Napoli – Roma — la partita più attesa del weekend"),
    ("Dom 25.10", "12:30 · Serie A", "Inter – Fiorentina — prima partita con l'ora solare"),
]
yy = ty + 16
for i, (d, t, m) in enumerate(rows):
    p.rect(MX, yy, RIGHT - MX, 44, fill="#f4efe0" if i % 2 == 0 else "#efe8d2")
    p.text(MX + 18, yy + 29, d, 20.5, "sans", True, OLIVE)
    p.text(MX + 185, yy + 29, t, 20, "sans", False, GREY)
    p.text(MX + 430, yy + 29, m, 21, "serif", False, INK)
    yy += 44
tnote = "Attenzione: le partite di mercoledì e giovedì finiscono dopo la chiusura di questa edizione — per questo qui sono presentazioni, senza risultati."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ESERCIZI　제 4 면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면　문제는 레벨이 섞여 있을 수 있어요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P4-ex")
e.head("A　COMPRENSIONE", 25)
e.expl("4면 기사를 읽고 알맞은 답을 고르세요.")
e.ex("B1", "객관식", "B", "인테르는 수요일에 샤흐타르 도네츠크와 맞붙어요",
     "L'Inter gioca mercoledì contro... A. l'Ajax · B. lo Shakhtar Donetsk · C. la Roma", size=20, gap=8)
e.ex("B1", "객관식", "B", "나폴리–로마 경기는 토요일 18:00예요",
     "Napoli–Roma si gioca... A. venerdì · B. sabato alle 18:00 · C. domenica a mezzanotte", size=20, gap=8)
e.ex("B1", "객관식", "A", "일요일 첫 표준시 경기예요",
     "Inter–Fiorentina è speciale perché... A. è la prima partita con l'ora solare · B. è una finale · C. si gioca di notte", size=20, gap=8)
e.ex("B1", "객관식", "C", "아탈란타는 목요일에 암스테르담으로 원정을 가요",
     "L'Atalanta gioca giovedì... A. a San Siro · B. a Roma · C. ad Amsterdam", size=20, gap=8)
e.ex("B1", "객관식", "B", "수요일과 목요일 경기는 미리보기만 하고 결과는 없어요",
     "Le partite di mercoledì e giovedì, in questo giornale, sono... A. risultati finali · B. presentazioni senza risultati · C. cancellate", size=20, gap=8)
e.head("B　LE PAROLE", 25)
e.match_set("B1", "단어 짝짓기",
            ["la giornata", "la sfida", "la trasferta", "San Siro"],
            ["lo stadio dell'Inter e del Milan, a Milano",
             "una partita importante tra due squadre forti",
             "ciascuna delle parti del campionato, una dopo l'altra",
             "la partita fuori casa, nella città degli avversari"],
            ["c", "b", "d", "a"],
            ["giornata=리그의 한 라운드 c", "sfida=강팀들의 대결 b", "trasferta=원정 경기 d", "San Siro=밀라노의 산 시로 경기장 a"],
            instr="단어와 뜻 짝짓기")
e.head("C　I COMPARATIVI", 25)
e.expl("괄호 안 단어의 비교급으로 빈칸을 채우세요 (일정은 표를 보세요).")
e.ex("B1", "문장 완성", "più tardi", "18:00가 12:30보다 늦어요: più tardi",
     "Napoli–Roma comincia ___ di Inter–Fiorentina. (tardi)", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "più presto", "12:30가 18:00보다 빨라요: più presto",
     "La partita di domenica comincia ___ di quella di sabato. (presto)", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "più bella", "più + bella, 이번 주 가장 아름다운 경기 (주관적 평가)",
     "Per i tifosi, Napoli–Roma è la partita ___ del weekend. (bella)", instr="빈칸 채우기", size=20, gap=8)
e.ex("B2", "문장 전환", "meglio", "bene의 비교급은 불규칙한 meglio예요",
     "L'Inter gioca bene. → L'Inter gioca ___ (bene).", instr="빈칸 채우기", size=20, gap=8)
e.head("D　IL PASSATO DELLO SPORT", 25)
e.expl("passato prossimo로 완성하세요.")
e.ex("B1", "문장 완성", "ha vinto", "vincere: ha vinto",
     "La mia squadra ___ (vincere) la partita di ieri.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "ha pareggiato", "pareggiare: ha pareggiato",
     "La mia squadra ___ (pareggiare) 1–1.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B2", "문장 완성", "sono arrivati", "arrivare는 essere를 써요. 복수 sono arrivati",
     "I tifosi ___ (arrivare) allo stadio alle cinque.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "abbiamo guardato", "guardare는 avere를 써요: abbiamo guardato",
     "Noi ___ (guardare) la partita in televisione.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "ha preso", "prendere의 분사는 preso예요: ha preso",
     "Il portiere ___ (prendere) un gol al 90°.", instr="빈칸 채우기", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
