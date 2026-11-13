# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-it-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA　문화", "La Lucerna", "A2 → B1　Torrone, cioccolato e tartufo　토로네, 초콜릿과 트러플")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("Due feste dolci chiudono in bellezza: torrone e cioccolato", 37)
f.byline("Dalla redazione de La Lucerna　Livello di lettura: A2 → B1")
f.para("Domenica 22 novembre chiude a Cremona la Festa del Torrone, la 29ª edizione, dal 7 al 22 novembre, con il tema «Il Confine»: sedici giorni, tre weekend, un solo dolce protagonista. Alle 11, al Palatorrone, il Torrone d'Oro va al produttore musicale Davide Simonetta, nato a Cremona.")
f.para("Il momento più atteso è il pomeriggio: alle 16 parte il corteo storico, con oltre centocinquanta figuranti in costumi rinascimentali, e alle 17, in piazza del Comune, arriva la rievocazione del matrimonio tra Bianca Maria Visconti e Francesco Sforza. Poi sbandieratori e giochi di fuoco, fino alle 18, quando al Palatorrone c'è il gran finale: «Il torrone va in brodo».")
f.para("La leggenda dice che il torrone nacque proprio per quelle nozze, il 25 ottobre 1441, con la forma del Torrazzo, la torre di Cremona: un dolce di albumi, zucchero, mandorle e miele.")
f.para("Lo stesso giorno, domenica 22 novembre, chiude a Perugia Eurochocolate, la 32ª edizione, dal 13 al 22 novembre, con il titolo «Fate dolci». La Regione ospite è la Calabria, con bergamotto, cedro, peperoncino e fichi; l'ospite del gran finale è il maestro Iginio Massari. E il tartufo bianco non va in vacanza: ad Alba, in Piemonte, la Fiera del Tartufo Bianco continua fino al 6 dicembre.")
f.gloss("il torrone 누가 · il corteo 행렬 · il figurante 출연자·엑스트라 · la rievocazione 역사 재현 · lo sbandieratore 기수.")
f.head("IL TORRAZZO E IL TORRONE", 25)
f.para("Il Torrazzo di Cremona è il campanile medievale in mattoni più alto d'Italia. La leggenda lo lega al torrone: un dolce nato da un matrimonio e diventato il simbolo della città. A Cremona, per sedici giorni, il torrone è dappertutto: nelle piazze, nei laboratori, nelle maxi costruzioni.", 23.5)
f.end_report()

# col 3: torrazzo image + facts + e tu? (sequential)
ix = COLX[3]
image(p, "torrazzo.jpg", ix, 200, CW, 300)
cy3 = caption(p, ix, 500, CW, "Il Torrazzo di Cremona: secondo la leggenda, il torrone ha la forma di questa torre — ed è nato per un matrimonio del 1441.",
              "Foto: Wikimedia Commons — CC0")
facts = ["Cremona, dom 22 novembre: corteo alle 16, rievocazione alle 17, gran finale alle 18.",
         "Perugia, dom 22 novembre: Eurochocolate chiude con Iginio Massari.",
         "Alba: la Fiera del Tartufo Bianco continua fino al 6 dicembre."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "IL WEEKEND DOLCE", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E tu? Preferisci il torrone o il cioccolato? Scrivi due frasi in italiano e mandale alla redazione."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("토로네와 초콜릿 중 어느 쪽이 더 좋나요? 두 문장을 써서 보내세요.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill=BOX)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E TU?　당신은요?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "토로네와 초콜릿 중 어느 쪽이 더 좋나요? 두 문장을 써서 보내세요.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ESERCIZI　3면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면　수준이 섞여 있습니다—번호로 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A　COMPRENSIONE", 25)
e.bridge("3면 기사를 읽고 정답을 고르세요.")
e.ex("A2", "객관식", "B", "토로네 축제는 11월 22일 일요일에 폐막",
     "La Festa del Torrone chiude... A. il 15 novembre · B. il 22 novembre · C. il 6 dicembre", size=20, gap=8)
e.ex("A2", "객관식", "C", "초콜릿 축제는 제32회",
     "Eurochocolate è alla sua... A. 29ª edizione · B. 67ª edizione · C. 32ª edizione", size=20, gap=8)
e.ex("A2", "객관식", "B", "재현극은 17시에 코무네 광장에서",
     "La rievocazione del matrimonio è... A. alle 11 · B. alle 17 · C. alle 20", size=20, gap=8)
e.ex("B1", "객관식", "A", "올해 유로초콜릿 주제는 “Fate dolci”",
     "Il titolo di Eurochocolate 2026 è... A. «Fate dolci» · B. «Il Confine» · C. «Finestrini»", size=20, gap=8)
e.ex("B1", "객관식", "B", "알바 트러플 축제는 12월 6일까지",
     "La Fiera del Tartufo Bianco di Alba chiude... A. il 22 novembre · B. il 6 dicembre · C. l'8 novembre", size=20, gap=8)
e.head("B　LE PAROLE DEL TESTO", 25)
e.bridge("상자 안의 단어로 빈칸을 채우세요.")
e.para("torrone · cioccolato · corteo · rievocazione · tartufo · mandorle", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "문장을 완성하세요", "torrone", "torrone = 누가",
     "A Cremona si festeggia il ___.", instr="빈칸 채우기", size=20, gap=8)
e.ex("A2", "문장을 완성하세요", "cioccolato", "cioccolato = 초콜릿",
     "A Perugia si festeggia il ___.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장을 완성하세요", "corteo", "corteo = 행렬",
     "Alle 16 parte il ___ storico in centro.", instr="빈칸 채우기", size=20, gap=8)
e.ex("A2", "문장을 완성하세요", "mandorle", "mandorle = 아몬드（복수）",
     "Il torrone è fatto di ___ e miele.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장을 완성하세요", "rievocazione", "rievocazione = 역사 재현",
     "Alle 17 c'è la ___ del matrimonio del 1441.", instr="빈칸 채우기", size=20, gap=8)
e.ex("A2", "문장을 완성하세요", "tartufo", "tartufo = 트러플",
     "Il ___ bianco è il fungo più prezioso d'Italia.", instr="빈칸 채우기", size=20, gap=8)
e.head("C　IL PASSATO PROSSIMO", 25)
e.bridge("근과거(passato prossimo)로 채우세요. 조동사 avere / essere에 주의하세요.")
e.ex("B1", "문장을 완성하세요", "è arrivato", "arrivare는 essere와 함께: è arrivato",
     "Il corteo ___ (arrivare) in piazza domenica.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장을 완성하세요", "abbiamo assaggiato", "assaggiare는 avere와 함께: abbiamo assaggiato",
     "Noi ___ (assaggiare) il torrone a Cremona.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장을 완성하세요", "sono andati", "andare는 essere와 함께, 복수 sono andati",
     "I visitatori ___ (andare) a Perugia per Eurochocolate.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장을 완성하세요", "ha chiuso", "chiudere는 avere와 함께: ha chiuso",
     "Perugia ___ (chiudere) Eurochocolate domenica.", instr="빈칸 채우기", size=20, gap=8)
e.head("D　COSTRUISCI LE FRASI", 25)
e.bridge("단어를 배열해 올바른 문장을 만드세요.")
e.ex("B1", "문장 만들기", "Eurochocolate chiude a Perugia il 22 novembre.", "주어 + 동사 + 장소 + 날짜",
     "Eurochocolate / chiude / a Perugia / il 22 novembre → ___", instr="문장 만들기", size=20, gap=8)
e.ex("A2", "문장 만들기", "A Cremona il torrone è il re.", "장소가 먼저, 주어가 뒤에",
     "a Cremona / il torrone / è il re → ___", instr="문장 만들기", size=20, gap=8)
e.ex("B1", "문장 만들기", "La fiera dura fino al 6 dicembre.", "dura fino a = ~까지 계속되다",
     "la fiera / dura / fino al 6 dicembre → ___", instr="문장 만들기", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT　스포츠", "La Lucerna", "LIVELLO B1　La Serie A e il tennis　세리에 A와 테니스")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("Lazio prima, Inter e Roma inseguono: i conti dell'11ª giornata", 37)
f.byline("Dalla redazione sportiva de La Lucerna　Livello di lettura: B1")
f.para("La Lazio è ancora prima in Serie A: il pareggio 1–1 a Napoli vale 29 punti, e la squadra di Gattuso è ancora imbattuta dopo 11 giornate. L'Inter vince 2–0 con il Como e sale a 28 punti, a un punto dalla vetta; la Roma batte 3–0 il Sassuolo e arriva a 27, con il miglior attacco del torneo, 31 gol.")
f.para("Il Milan vince 2–1 a Genova e prende il quarto posto, con 24 punti, davanti al Como, fermo a 23. Fiorentina e Juventus chiudono 2–2 al Franchi: i viola restano a 9 punti. In coda, l'Udinese perde 2–1 a Venezia ed è ultima, con 5 punti.")
f.para("La Serie A riparte sabato 21 novembre con la 12ª giornata, che si chiude lunedì 23: sabato la Lazio capolista gioca in casa con il Lecce, domenica sera, alle 20.45, c'è il big match Atalanta–Inter, a Bergamo. Lunedì sera, alle 20.45, Monza–Fiorentina chiude la giornata.")
f.para("Domenica 22 novembre si gioca anche la finale delle Nitto ATP Finals a Torino: otto campioni, due gironi e poi le semifinali. Il numero uno è Alexander Zverev, con Carlos Alcaraz tra i favoriti; l'Italia ha Flavio Cobolli, al debutto. Jannik Sinner, vincitore del 2025, non gioca: è fuori per infortunio.")
f.para("E la Nazionale? Le due notti azzurre — giovedì 12 novembre con la Francia e domenica 15 novembre con il Belgio — si sono giocate prima di questa edizione: i risultati e la classifica finale del girone saranno nel prossimo numero.")
f.gloss("la vetta 선두 · imbattuto 무패의 · il big match 빅 매치 · il girone 조 · il debutto 데뷔.")
f.end_report()

# col 3: tennis image + classifica + e tu? (sequential)
bx = COLX[3]
image(p, "tennis.jpg", bx, 200, CW, 110)
cy3 = caption(p, bx, 310, CW, "Il tennis di cent'anni fa: oggi le Finals si giocano a Torino, all'Inalpi Arena.",
              "Foto: Wikimedia Commons — dominio pubblico")
cb = cy3 + 24
p.rect(bx, cb, CW, 470, fill=BOX)
p.text(bx + 22, cb + 40, "LA CLASSIFICA　DOPO 11 GIORNATE", 19.5, "sans", True, OLIVE)  # D5 (2026-11-12): was 21, title ran +16.8px past the box; 19.5 fits (same defect as core-it)
classifica = [
    "1. Lazio — 29 punti",
    "2. Inter — 28 punti",
    "3. Roma — 27 punti",
    "4. Milan — 24 punti",
    "5. Como — 23 punti",
    "20. Udinese — 5 punti",
]
yy3 = cb + 78
for t in classifica:
    yy3 = p.para(bx + 22, yy3 + 21, t, 21, "serif", False, INK, CW - 44, 1.4) + 4
p.para(bx + 22, yy3 + 14, "La Lazio è ancora imbattuta; la Roma ha il miglior attacco, 31 gol.", 19, "sans", False, GREY, CW - 44, 1.35)
ey3 = cb + 470 + 26
etvous = "E tu? Quale partita guardi domenica sera? Scrivi due frasi in italiano."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("일요일 저녁에 어느 경기를 볼 건가요? 이탈리아어로 두 문장을 써서 보내세요.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill=BOX)
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "E TU?　당신은요?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "일요일 저녁에 어느 경기를 볼 건가요? 이탈리아어로 두 문장을 써서 보내세요.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- results table (full width, compact) ----
ty = 1140
p.text(MX, ty, "I RISULTATI DELL'11ª GIORNATA　11라운드 결과（11월 6~8일）", 26, "sans", True, OLIVE)
rows = [
    ("VEN 6.11", "Venezia – Udinese 2–1", ""),
    ("SAB 7.11", "Cagliari – Frosinone 1–0", "Torino – Lecce 1–1"),
    ("SAB 7.11", "Parma – Bologna 1–2", "Roma – Sassuolo 3–0"),
    ("DOM 8.11", "Napoli – Lazio 1–1", "Genoa – Milan 1–2　Monza – Atalanta 0–1"),
    ("DOM 8.11", "Inter – Como 2–0", "Fiorentina – Juventus 2–2"),
]
yy = ty + 16
for i, (d, m1, m2) in enumerate(rows):
    p.rect(MX, yy, RIGHT - MX, 62, fill=BOX if i % 2 == 0 else PAPER)
    p.text(MX + 18, yy + 29, d, 20, "sans", True, OLIVE)
    p.text(MX + 185, yy + 40, m1, 21, "serif", True, INK)
    p.text(MX + 700, yy + 40, m2, 21, "serif", False, INK)
    yy += 62
p.para(MX, yy + 26, "La 12ª giornata si gioca dal 21 al 23 novembre: Atalanta – Inter, ore 20.45, domenica 22 novembre, a Bergamo. I risultati delle due notti azzurre di Nations League saranno nel prossimo numero.", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ESERCIZI　4면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면　수준이 섞여 있습니다—번호로 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A　COMPRENSIONE", 25)
e.bridge("4면 기사를 읽고 정답을 고르세요.")
e.ex("B1", "객관식", "B", "라치오 29점으로 선두",
     "La prima in classifica ha... A. 28 punti · B. 29 punti · C. 27 punti", size=20, gap=8)
e.ex("B1", "객관식", "B", "인터가 코모를 2-0으로 이겼다",
     "L'Inter vince 2–0 con... A. la Roma · B. il Como · C. il Milan", size=20, gap=8)
e.ex("B1", "객관식", "A", "로마는 최다 득점 31골",
     "Il miglior attacco del torneo è... A. della Roma · B. della Lazio · C. del Milan", size=20, gap=8)
e.ex("B1", "객관식", "C", "우디네세는 5점으로 최하위",
     "L'ultima in classifica è... A. il Monza · B. il Venezia · C. l'Udinese", size=20, gap=8)
e.ex("B1", "객관식", "B", "빅 매치는 일요일 저녁 베르가모에서",
     "Atalanta–Inter si gioca... A. sabato · B. domenica sera · C. lunedì", size=20, gap=8)
e.head("B　LE PAROLE", 25)
e.match_set("B1", "단어 짝짓기",
            ["la vetta", "imbattuto", "il girone", "il debutto"],
            ["la prima volta in un torneo importante",
             "che non ha mai perso",
             "il gruppo di squadre in un torneo",
             "il primo posto in classifica, la cima"],
            ["d", "b", "c", "a"],
            ["vetta = 선두 d", "imbattuto = 무패의 b", "girone = 조 c", "debutto = 데뷔 a"],
            instr="단어와 뜻을 연결하세요")
e.head("C　I COMPARATIVI", 25)
e.bridge("비교급으로 채우세요（순위표를 보세요）.")
e.ex("B1", "문장을 완성하세요", "più", "라치오는 인터보다 승점이 많다: più",
     "La Lazio ha ___ punti dell'Inter. (molti)", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장을 완성하세요", "meno", "우디네세는 라치오보다 승점이 적다: meno",
     "L'Udinese ha ___ punti della Lazio. (pochi)", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장을 완성하세요", "più bella", "più + bella: 일요일 저녁이 가장 좋다（주관적 평가）",
     "Per i tifosi, la serata di domenica è la serata ___ del weekend. (bella)", instr="빈칸 채우기", size=20, gap=8)
e.ex("B2", "문형 변환", "meglio", "bene의 비교급은 불규칙형 meglio",
     "La Lazio gioca bene. → La Lazio gioca ___ (bene).", instr="빈칸 채우기", size=20, gap=8)
e.head("D　IL PASSATO DELLO SPORT", 25)
e.bridge("근과거(passato prossimo)로 채우세요.")
e.ex("B1", "문장을 완성하세요", "ha vinto", "vincere:ha vinto",
     "L'Inter ___ (vincere) 2–0 con il Como.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장을 완성하세요", "ha pareggiato", "pareggiare:ha pareggiato",
     "La Lazio ___ (pareggiare) 1–1 a Napoli.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B2", "문장을 완성하세요", "sono arrivati", "arrivare는 essere와 함께, 복수 sono arrivati",
     "I tifosi ___ (arrivare) allo stadio alle cinque.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장을 완성하세요", "abbiamo guardato", "guardare는 avere와 함께: abbiamo guardato",
     "Noi ___ (guardare) la partita in televisione.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장을 완성하세요", "ha preso", "prendere의 분사는 preso: ha preso",
     "Il portiere ___ (prendere) un gol al 90°.", instr="빈칸 채우기", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
