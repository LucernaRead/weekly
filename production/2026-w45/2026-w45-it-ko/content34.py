# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-it-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA · 문화", "La Lucerna", "A2 → B1 · Panettone, torrone e musei aperti · 디저트와 박물관")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("Il weekend più dolce: panettone a Milano, torrone a Cremona", 37)
f.byline("Dalla redazione de La Lucerna · Livello di lettura: A2 → B1")
f.para("Il freddo porta con sé la voglia di dolci. Sabato 7 e domenica 8 novembre, a Milano, c'è la finale della Coppa del Mondo del Panettone: pasticceri da 19 paesi si sfidano con il dolce simbolo di Milano, e il pubblico può assaggiare gratis. Due le categorie in gara: il panettone tradizionale e il panettone al cioccolato.")
f.para("Lo stesso fine settimana apre a Cremona la Festa del Torrone, che dura fino al 22 novembre: bancarelle, degustazioni e musica nella città dei violini. Il torrone è un dolce antico, di mandorle e miele — e Cremona ne è la capitale.")
f.para("E il tartufo bianco non va in vacanza: ad Alba, in Piemonte, la Fiera del Tartufo Bianco continua fino al 6 dicembre, con mercati e piatti speciali. Il re dell'autunno resta in tavola anche con il primo freddo.")
f.para("Per chi ama la cultura, la settimana comincia martedì 3 novembre a Milano con il Forum Cultura: più di 50 eventi e aperture straordinarie di musei e biblioteche. Si comincia con il cantiere di restauro della Sala delle Asse al Castello Sforzesco, la GAM e Palazzo Morando; nel fine settimana il Forum si sposta alla Bovisa, al sito della Goccia.")
f.gloss("il panettone 밀라노 크리스마스 빵 · il torrone 토로네 · l'assaggio 맛보기 · la bancarella 노점 · il cantiere 공사 현장/복원 현장예요.")
f.head("IL TARTUFO RESTA IN TAVOLA", 25)
f.para("La Fiera di Alba è aperta dal 10 ottobre: quasi due mesi di profumi e piatti speciali. Con il freddo, il tartufo bianco diventa ancora più prezioso — e i ristoranti lo servono con pasta, uova e risotti.", 23.5)
f.end_report()

# col 3: truffle image + facts + e tu? (sequential)
ix = COLX[3]
image(p, "tartufo.jpg", ix, 200, CW, 265)
cy3 = caption(p, ix, 465, CW, "Un tartufo bianco, il fungo più prezioso d'Italia. Ad Alba la fiera dura fino al 6 dicembre; con il primo freddo, il tartufo è ancora più prezioso.",
              "Foto: Wikimedia Commons — dominio pubblico")
facts = ["Milano, 7–8 novembre: finale della Coppa del Mondo del Panettone, degustazioni gratuite.",
         "Cremona, 7–22 novembre: Festa del Torrone, bancarelle e musica.",
         "Alba: la Fiera del Tartufo Bianco continua fino al 6 dicembre."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "IL WEEKEND DOLCE", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E tu? Preferisci il panettone tradizionale o quello al cioccolato? Scrivi due frasi in italiano e mandale alla redazione."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("전통 파네토네와 초콜릿 파네토네 중 어느 쪽이 더 좋아요? 두 문장을 써서 보내 주세요.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E TU? · 내 이야기", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "전통 파네토네와 초콜릿 파네토네 중 어느 쪽이 더 좋아요? 두 문장을 써서 보내 주세요.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ESERCIZI · 제 3 면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면 · 문제는 레벨이 섞여 있을 수 있어요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · COMPRENSIONE", 25)
e.bridge("3면 기사를 읽고 알맞은 답을 고르세요.")
e.ex("A2", "객관식", "B", "파네토네 결승은 밀라노에서 열려요",
     "La finale della Coppa del Mondo del Panettone è a... A. Cremona · B. Milano · C. Alba", size=20, gap=8)
e.ex("A2", "객관식", "C", "크레모나 토로네 축제는 11월 22일까지 이어져요",
     "La Festa del Torrone dura fino al... A. 6 dicembre · B. 8 novembre · C. 22 novembre", size=20, gap=8)
e.ex("A2", "객관식", "B", "파네토네 결승에는 19개국 제빵사가 참가해요",
     "Alla finale del Panettone partecipano pasticceri da... A. 5 paesi · B. 19 paesi · C. 50 paesi", size=20, gap=8)
e.ex("B1", "객관식", "A", "문화 포럼은 11월 3일 화요일에 열려요",
     "Il Forum Cultura apre... A. martedì 3 novembre · B. sabato 7 novembre · C. lunedì 2 novembre", size=20, gap=8)
e.ex("B1", "객관식", "B", "알바 트러플 축제는 12월 6일에 끝나요",
     "La Fiera del Tartufo Bianco di Alba chiude... A. il 22 novembre · B. il 6 dicembre · C. l'8 novembre", size=20, gap=8)
e.head("B · LE PAROLE DEL TESTO", 25)
e.bridge("상자 안의 단어로 빈칸을 채우세요。")
e.para("panettone · torrone · assaggio · bancarella · tartufo · mandorle", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "문장 완성", "panettone", "panettone = 밀라노 크리스마스 빵",
     "Il ___ è il dolce simbolo di Milano.", instr="빈칸 채우기", size=20, gap=8)
e.ex("A2", "문장 완성", "torrone", "torrone = 토로네",
     "A Cremona si festeggia il ___.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "assaggio", "assaggio = 맛보기",
     "Alla finale del Panettone, il pubblico può fare un ___ gratis.", instr="빈칸 채우기", size=20, gap=8)
e.ex("A2", "문장 완성", "bancarella", "bancarella = 노점",
     "Alla festa ci sono tante ___ con i dolci.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "mandorle", "mandorle = 아몬드 (복수)",
     "Il torrone è fatto di ___ e miele.", instr="빈칸 채우기", size=20, gap=8)
e.ex("A2", "문장 완성", "tartufo", "tartufo = 트러플",
     "Il ___ bianco è il fungo più prezioso d'Italia.", instr="빈칸 채우기", size=20, gap=8)
e.head("C · IL PASSATO PROSSIMO", 25)
e.bridge("passato prossimo (근과거)로 완성하세요. 조동사 avere / essere에 주의하세요.")
e.ex("B1", "문장 완성", "è arrivato", "arrivare는 essere를 써요: è arrivato",
     "Il primo freddo ___ (arrivare) lunedì.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "abbiamo assaggiato", "assaggiare는 avere를 써요: abbiamo assaggiato",
     "Noi ___ (assaggiare) il panettone a Milano.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "sono andati", "andare는 essere를 써요. 복수 sono andati",
     "I pasticceri ___ (andare) a Milano per la finale.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "ha aperto", "aprire는 avere를 써요: ha aperto",
     "Cremona ___ (aprire) la Festa del Torrone sabato.", instr="빈칸 채우기", size=20, gap=8)
e.head("D · COSTRUISCI LE FRASI", 25)
e.bridge("단어를 배열해 알맞은 문장을 만드세요.")
e.ex("B1", "문장 만들기", "La finale è a Milano il 7 novembre.", "주어 + essere + 장소 + 날짜",
     "la finale / è a Milano / il 7 novembre → ___", instr="문장 만들기", size=20, gap=8)
e.ex("A2", "문장 만들기", "A Cremona il torrone è il re.", "장소가 앞에, 주어가 뒤에 와요",
     "a Cremona / il torrone / è il re → ___", instr="문장 만들기", size=20, gap=8)
e.ex("B1", "문장 만들기", "La fiera dura fino al 6 dicembre.", "dura fino a = ~까지 이어져요",
     "la fiera / dura / fino al 6 dicembre → ___", instr="문장 만들기", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT · 스포츠", "La Lucerna", "LIVELLO B1 · La Serie A e l'Europa · 세리에 A와 유럽 대회")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("L'undicesima giornata: Genoa–Milan, Inter–Como, Fiorentina–Juventus", 37)
f.byline("Dalla redazione sportiva de La Lucerna · Livello di lettura: B1")
f.para("È una settimana di grande calcio. Da martedì 3 a giovedì 5 novembre si gioca la quarta giornata delle coppe europee: Champions League, Europa League e Conference League. Attenzione: queste partite si giocano dopo la chiusura del giornale — qui sono una presentazione, senza risultati.")
f.para("Poi arriva l'undicesima giornata di Serie A, da venerdì 6 a domenica 8 novembre. La giornata chiude domenica 8 novembre con tre partite grandi: Genoa–Milan, Inter–Como e Fiorentina–Juventus, la sera a Firenze.")
f.para("Domenica è anche il giorno del freddo sugli spalti: chi va allo stadio mette sciarpa e guanti, come a pagina 2. Ma il calcio non si ferma per il primo freddo — anzi, con il freddo le partite della sera diventano ancora più belle, sotto le luci.")
f.para("E per chi segue i giovani: anche le squadre giovani giocano nel weekend. Il consiglio della redazione è uno solo: scegli una partita, guarda il calendario e non perderti la domenica sera a Firenze.")
f.gloss("la giornata 라운드 · la presentazione 경기 전 소개 · gli spalti 관중석 · la sera 저녁예요.")
f.end_report()

# col 3: data box + e tu? (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 436, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 240, "LE PARTITE DA SEGNARE", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "Martedì 3 – giovedì 5 novembre · Coppe europee, 4ª giornata — si giocano dopo la chiusura del giornale. Venerdì 6 – domenica 8 novembre · Serie A, 11ª giornata. Domenica 8 novembre · Genoa – Milan; Inter – Como; Fiorentina – Juventus (sera, a Firenze).", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 662
etvous = "E tu? Quale partita guardi domenica sera? Scrivi due frasi in italiano."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("일요일 저녁에는 어떤 경기를 봐요? 이탈리아어로 두 문장을 써서 보내 주세요.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "E TU? · 내 이야기", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "일요일 저녁에는 어떤 경기를 봐요? 이탈리아어로 두 문장을 써서 보내 주세요.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "LA SETTIMANA DEL CALCIO · 축구 주간", 26, "sans", True, OLIVE)
rows = [
    ("Mar–Gio", "Coppe europee · 4ª giornata", "Champions, Europa e Conference League: presentazione, senza risultati"),
    ("Ven–Dom", "Serie A · 11ª giornata", "L'undicesima giornata si gioca da venerdì 6 a domenica 8 novembre"),
    ("Dom 8.11", "Serie A", "Genoa – Milan — domenica, a Genova"),
    ("Dom 8.11", "Serie A", "Inter – Como — a San Siro, a Milano"),
    ("Dom 8.11", "Serie A · sera", "Fiorentina – Juventus — la sera, a Firenze"),
]
yy = ty + 16
for i, (d, t, m) in enumerate(rows):
    p.rect(MX, yy, RIGHT - MX, 44, fill="#f4efe0" if i % 2 == 0 else "#efe8d2")
    p.text(MX + 18, yy + 29, d, 20.5, "sans", True, BRICK)
    p.text(MX + 185, yy + 29, t, 20, "sans", False, GREY)
    p.text(MX + 470, yy + 29, m, 21, "serif", False, INK)
    yy += 44
tnote = "Attenzione: le partite europee di martedì–giovedì e le partite di Serie A del weekend si giocano dopo la chiusura di questa edizione — per questo qui sono presentazioni, senza risultati."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ESERCIZI · 제 4 면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면 · 문제는 레벨이 섞여 있을 수 있어요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A · COMPRENSIONE", 25)
e.bridge("4면 기사를 읽고 알맞은 답을 고르세요.")
e.ex("B1", "객관식", "B", "세리에 A 11라운드는 일요일에 끝나요",
     "L'undicesima giornata di Serie A chiude... A. venerdì · B. domenica 8 novembre · C. lunedì", size=20, gap=8)
e.ex("B1", "객관식", "B", "일요일 저녁 피오렌티나–유벤투스 경기예요",
     "Domenica sera, a Firenze, si gioca... A. Inter–Como · B. Fiorentina–Juventus · C. Genoa–Milan", size=20, gap=8)
e.ex("B1", "객관식", "A", "유럽 대회 4라운드는 11월 3–5일이에요",
     "La quarta giornata delle coppe europee si gioca... A. dal 3 al 5 novembre · B. dal 6 all'8 novembre · C. il 2 novembre", size=20, gap=8)
e.ex("B1", "객관식", "C", "유럽 대회 경기는 미리보기만 하고 결과는 없어요",
     "Le partite europee, in questo giornale, sono... A. risultati finali · B. cancellate · C. presentazioni senza risultati", size=20, gap=8)
e.ex("B1", "객관식", "B", "인테르–코모 경기는 산 시로에서 열려요",
     "Inter–Como si gioca... A. a Firenze · B. a San Siro · C. a Genova", size=20, gap=8)
e.head("B · LE PAROLE", 25)
e.match_set("B1", "단어 짝짓기",
            ["la giornata", "la presentazione", "gli spalti", "la sera"],
            ["il posto del pubblico allo stadio, con le gradinate",
             "il racconto prima della partita, senza risultati",
             "ciascuna delle parti del campionato, una dopo l'altra",
             "la parte del giorno dopo il tramonto, con le luci accese"],
            ["c", "b", "a", "d"],
            ["giornata=리그의 한 라운드 c", "presentazione=경기 전 소개 b", "spalti=관중석 a", "sera=저녁 d"],
            instr="단어와 뜻 짝짓기")
e.head("C · I COMPARATIVI", 25)
e.bridge("괄호 안 단어의 비교급으로 빈칸을 채우세요 (일정은 표를 보세요).")
e.ex("B1", "문장 완성", "più tardi", "일요일 저녁 경기는 금요일보다 늦어요: più tardi",
     "Le partite di domenica sera cominciano ___ di quelle di venerdì. (tardi)", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "più presto", "금요일 경기는 일요일보다 빨라요: più presto",
     "Le partite di venerdì cominciano ___ di quelle di domenica. (presto)", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "più bella", "più + bella, 일요일 저녁이 가장 아름다워요 (주관적 평가)",
     "Per i tifosi, la domenica sera è la serata ___ del weekend. (bella)", instr="빈칸 채우기", size=20, gap=8)
e.ex("B2", "문장 전환", "meglio", "bene의 비교급은 불규칙한 meglio예요",
     "L'Inter gioca bene. → L'Inter gioca ___ (bene).", instr="빈칸 채우기", size=20, gap=8)
e.head("D · IL PASSATO DELLO SPORT", 25)
e.bridge("passato prossimo로 완성하세요.")
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
