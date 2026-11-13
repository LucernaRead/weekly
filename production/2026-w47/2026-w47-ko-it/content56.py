# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · 청년 (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("청년　Giovani", "Lucerna", "레벨 B1　수능 주간과 예비소집　Settimana del CSAT e convocazione preliminare")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-feature")
f.title("수능 주간 — 예비소집부터 시험 날까지", 37)
f.byline("Lucerna 편집부　읽기 레벨: B1")
f.para("수요일 11월 18일에는 예비소집이 있어요. 목요일 11월 19일에는 수능이 있어요. 올해 수험생은 551,864명이에요. 지난해보다 2,310명 줄었어요. 시험장은 전국 85개 시험지구에 1,312곳이에요. 시험은 오전 8시 40분부터 오후 5시 45분까지예요.")
f.para("예비소집에서는 수험표를 받고 시험장을 확인해요. 모이는 시각과 장소는 학교마다 달라요. 원서접수증과 학교 공지를 확인하세요. 시험 당일에는 8시 10분까지 시험실에 들어가야 해요. 수험표를 잃어버리면 당일 아침 8시까지 시험장 관리본부에 신고하면 다시 받을 수 있어요.", w=414)
f.para("시험 날의 특별한 조치는 11월 19일에만 적용돼요. 회사와 관공서가 10시부터 일을 시작하고, 지하철이 더 자주 다니고, 영어 듣기 시간(13시 10분~13시 35분)에 비행기가 뜨거나 내리지 않는 것 — 모두 11월 19일의 일이에요. 이번 주(11월 16~22일)의 다른 날의 조치가 아니에요. 자세한 이야기는 6면에 있어요.")
f.gloss("줄다 = diminuire · 시험지구 = zona d'esame · 신고하다 = dichiarare · 관리본부 = ufficio d'esame")
f.box("이번 주 청년 숫자　Numeri giovani", [
    ("551,864명 — 올해 수험생 (지난해보다 2,310명 감소)", "serif", False, INK, 20.5, 1.4),
    ("1,312곳 — 전국 시험장 (85개 시험지구)", "serif", False, INK, 20.5, 1.4),
    ("8시 10분 — 시험 당일 입실 완료 시각", "serif", False, INK, 20.5, 1.4),
    ("12월 11일 — 성적 통지일 (금요일)", "serif", False, INK, 20.5, 1.4, 338),
])
f.head("수능이 끝나면", 25)
f.para("수능이 끝나면 수험생의 마음이 가벼워져요. 시험이 끝난 오후에는 친구와 이야기를 나누고, 맛있는 것을 먹어요. 성적은 12월 11일 금요일에 나와요. 결과가 나올 때까지는 푹 쉬는 것이 좋아요.")
f.gloss("가벼워지다 = sentirsi più leggero · 푹 = bene · 쉬다 = riposare")
f.head("김치의 날, 청년의 아이디어", 25)
f.para("11월 22일 일요일은 김치의 날이에요. 11월 20일 금요일 위킴 페스티벌에서는 '김치의 새로운 도전: 청년 아이디어와 과학기술의 만남'이라는 강연이 있어요. 청년의 아이디어가 김치의 미래를 이야기해요. 김치를 나누는 마음은 청년의 마음과 같아요.")
f.gloss("도전 = una sfida · 미래 = il futuro · 나누다 = condividere")
f.head("시험 전날의 하루", 25)
f.para("시험 전날에는 일찍 자요. 밤늦게까지 공부하면 아침에 피곤해져요. 준비물은 미리 챙겨요. 수험표와 신분증, 연필을 가방에 넣어요.")
f.para("아침밥은 꼭 먹어요. 밥을 먹어야 머리가 잘 돌아가요. 너무 많이 먹으면 졸려요. 평소 먹던 대로 먹는 것이 좋아요.")
f.gloss("피곤하다 = stanco · 졸리다 = assonnato · 평소 = di solito")
f.end_report()

# col 3: study image + 당신
ix = COLX[3]
image(p, "study.jpg", ix, 200, CW, 230)
cy3 = caption(p, ix, 430, CW, "도서관에서 공부하는 학생들. 수험생에게 가을은 가장 바쁜 계절이에요.",
              "사진: Gary Todd — CC0 (Wikimedia Commons) · 자료 사진")
ey3 = cy3 + 24
etvous = "당신은? 수능이 끝난 뒤에 가장 하고 싶은 일은 무엇이에요? 한국어로 두 문장 써서 보내 주세요."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("E tu? Che cosa vuoi fare soprattutto dopo il CSAT? Scrivi due frasi in coreano e inviaci.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "당신은?　E tu?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "E tu? Che cosa vuoi fare soprattutto dopo il CSAT? Scrivi due frasi in coreano e inviaci.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "연습　Esercizi p. 5", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Risposte a p. 8　I livelli possono mescolarsi; cerca per numero", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A　이해", 25)
e.glossline("5면의 글을 읽고 맞는 답을 고르세요.")
e.ex("B1", "Scelta multipla", "A", "La convocazione preliminare è mercoledì 18 nov.",
     "예비소집은 언제예요? A. 11월 18일 · B. 11월 19일 · C. 11월 22일", size=20, gap=7)
e.ex("B1", "Scelta multipla", "B", "Il CSAT inizia alle 8:40",
     "수능은 몇 시부터 시작해요? A. 8시 10분 · B. 8시 40분 · C. 10시", size=20, gap=7)
e.ex("B1", "Scelta multipla", "A", "Candidati quest'anno: 551 864",
     "올해 수험생은 몇 명이에요? A. 551,864명 · B. 1,312명 · C. 2,310명", size=20, gap=7)
e.ex("B1", "Scelta multipla", "B", "I risultati escono venerdì 11 dic.",
     "성적은 언제 나와요? A. 11월 19일 · B. 12월 11일 · C. 11월 28일", size=20, gap=7)
e.ex("B1", "Scelta multipla", "A", "Entra in aula entro le 8:10 il giorno dell'esame",
     "시험 당일 입실 완료 시각은 언제예요? A. 8시 10분 · B. 10시 · C. 13시 10분", size=20, gap=7)
e.head("B　말 넣기", 25)
e.glossline("빈칸에 알맞은 말을 넣으세요.")
e.ex("B1", "Completare", "예비소집", "Ritira il pass alla convocazione preliminare",
     "11월 18일 ___에서는 수험표를 받아요.", instr="Completare", size=20, gap=7)
e.ex("B1", "Completare", "수험표", "Ritira il pass e controlla la sede d'esame",
     "예비소집에서는 ___를 받고 시험장을 확인해요.", instr="Completare", size=20, gap=7)
e.ex("B1", "Completare", "2,310", "2 310 candidati in meno dell'anno scorso",
     "올해 수험생은 지난해보다 ___명 줄었어요.", instr="Completare", size=20, gap=7)
e.ex("B1", "Completare", "성적", "I risultati escono l'11 dic.",
     "___은 12월 11일 금요일에 나와요.", instr="Completare", size=20, gap=7)
e.ex("B1", "Completare", "8", "Tessera smarrita: da segnalare entro le 8",
     "수험표를 잃어버리면 당일 아침 ___시까지 신고하면 다시 받을 수 있어요.", instr="Completare", size=20, gap=7)
e.head("C　숫자와 날짜", 25)
e.glossline("5면의 숫자로 답하세요.")
e.ex("B1", "Completare", "551,864", "Candidati quest'anno: 551 864",
     "올해 수험생은 ___명이에요.", instr="Completare", size=20, gap=7)
e.ex("B1", "Completare", "1,312", "Sedi d'esame in tutto il paese: 1 312",
     "시험장은 전국에 ___곳이에요.", instr="Completare", size=20, gap=7)
e.ex("B1", "Completare", "85", "85 zone d'esame in tutto il paese",
     "시험지구는 전국에 ___개예요.", instr="Completare", size=20, gap=7, bw=354)
e.ex("B1", "Completare", "10", "Il giorno dell'esame, gli uffici aprono alle 10:00",
     "시험 날, 회사와 관공서는 ___시부터 일을 시작해요.", instr="Completare", size=20, gap=7, bw=354)
e.head("D　문장 만들기", 25)
e.glossline("말을 바른 순서로 놓아 문장을 만드세요.")
e.ex("B1", "Formare frasi", "수험생은 열심히 공부해요.", "Ordine delle parole: soggetto + avverbio + verbo",
     "수험생은 / 열심히 / 공부해요 → ___", instr="Formare frasi", size=20, gap=7)
e.ex("B1", "Formare frasi", "우리는 수험생을 응원해요.", "Soggetto + oggetto + verbo",
     "우리는 / 수험생을 / 응원해요 → ___", instr="Formare frasi", size=20, gap=7)
e.ex("B1", "Formare frasi", "비행기는 듣기 시간에 뜨지 않아요.", "Niente voli durante la prova d'ascolto",
     "비행기는 / 듣기 시간에 / 뜨지 않아요 → ___", instr="Formare frasi", size=20, gap=7)
e.ex("B1", "Formare frasi", "친구는 김치를 나눠 줘요.", "Un amico condivide il kimchi",
     "친구는 / 김치를 / 나눠 줘요 → ___", instr="Formare frasi", size=20, gap=7)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-cheongnyeon.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · 깊이 읽기 (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("깊이 읽기　Lettura approfondita", "Lucerna", "레벨 B2　예보에서 결과로 — 뉴스를 다시 읽는 법　Dalla previsione al risultato")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1180, tag="P6-feature")
f.title("예보에서 결과로 — 뉴스를 다시 읽는 법", 37)
f.byline("Lucerna 편집부　읽기 레벨: B2")
f.para("지난주 신문에는 예보와 발표가 많았어요. 이번 주 신문에는 결과가 있어요. 한국시리즈 일정은 '발표된 일정'이었어요. 이제 결과는 '삼성이 4승 1패로 우승했어요'예요. 발표가 결과로 바뀐 것이에요. 뉴스를 읽을 때는 발표인지 결과인지 나눠야 해요.", w=404)
f.para("단풍도 같아요. 산림청 예보는 내장산 절정을 11월 4일로 봤어요. 정읍시 전망은 11월 7~8일경이었어요. 예보 날짜가 지났어요. 실제 관측 절정은 날씨누리에서 확인해야 해요. 예보 날짜를 실제 관측 날짜처럼 말하면 안 돼요.")
f.para("숫자도 다시 읽어 봐요. 10월 16일 기준 배추 한 포기는 5,557원이었어요. 11월 9일 기준 김장비용은 199,456원이에요. 날짜가 다르면 가격도 달라요. 숫자를 읽을 때는 기준 날짜를 먼저 봐야 해요.")
f.para("수능은 아직 결과의 뉴스가 아니에요. 예비소집은 11월 18일, 수능은 11월 19일 — 정해진 일정이에요. 성적은 12월 11일에 나와요. 아직 나오지 않은 결과를 예상으로 채우면 안 돼요. 결과가 나오면 그때 전해요.")
f.gloss("바뀌다 = cambiare · 채우다 = compilare · 기준 날짜 = la data di riferimento · 아직 = ancora")
f.head("결과를 알 때", 25)
f.para("결과를 알 때는 결과를 분명히 말해요. 이 신문은 한국시리즈 결과를 점수와 함께 전했어요. 1차전 8대 7부터 5차전 12대 1까지, 다섯 경기의 점수가 모두 있어요.", w=374)
f.gloss("분명히 = chiaramente · 전하다 = riferire")
f.head("뉴스의 날짜 찾기", 25)
f.para("뉴스를 읽을 때는 제목보다 날짜를 먼저 봐요. 날짜가 있는 뉴스가 믿을 수 있어요.", w=374)
f.para("'예정'과 '확정'도 나눠야 해요. 예정은 아직 정해지지 않은 일, 확정은 정해진 일이에요. 예정된 일을 확정된 일처럼 읽으면 안 돼요.")
f.gloss("예정 = previsto · 확정 = confermato · 믿다 = credere")
f.end_report()

# ---- comparison table (cols 0-2) ----
ty = 1210
p.text(MX, ty + 26, "지난주와 이번 주, 한눈에 보기　La settimana scorsa e questa settimana a colpo d'occhio", 26, "sans", True, OLIVE)
p.hline(MX, COLX[2] + CW, ty + 40, OLIVE, 2)
rows = [
    ("구분", "지난주 (11월 9~15일)", "이번 주 (11월 16~22일)"),
    ("한국시리즈", "발표된 일정", "결과 나왔어요 (삼성 4–1)"),
    ("단풍", "예보 날짜", "예보 날짜 지났어요"),
    ("김장비용", "10월 16일 가격", "11월 9일 조사 199,456원"),
]
tw = [300, 512, 511.5]  # W47-KO fix3: sums to 1323.5 = 3-col span (old 1388 ran 36.5px into col 4 after the margin change)
yy = ty + 58
for r, (c0, c1, c2) in enumerate(rows):
    x0 = MX
    for j, cell in enumerate((c0, c1, c2)):
        hdr = (r == 0)
        p.rect(x0, yy, tw[j], 52, fill=CLOTH if hdr else (BOX if r % 2 else PAPER), stroke=LINE, sw=1.1)
        p.text(x0 + 18, yy + 35, cell, 21 if not hdr else 20, "sans" if hdr else "serif", hdr,
               ONCLOTH if hdr else INK)
        x0 += tw[j]
    yy += 52
p.para(MX, yy + 30, "표의 자료: aT 발표 (11월 10일) · KBO 결과 (11월 8일) — 날짜를 먼저 보세요.", 19.5, "serif", False, GREY, 1323.5, 1.4)

# col 3: how-to-read boxes (no image on P6)
ix = COLX[3]
howto = ["① 날짜를 봐요", "② 기준을 봐요", "③ 결과를 봐요"]
sy3 = 200 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in howto) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "수능 뉴스 읽는 법", 24, "sans", True, OLIVE)
yy3 += 52
for t in howto:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
dy3 = sy3 + sh + 26
dlist = ["D-3 — 11월 16일", "D-1 — 11월 18일", "D-데이 — 11월 19일", "김치의 날 — 11월 22일"]
sh2 = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in dlist) + 32
p.rect(ix, dy3, CW, sh2, fill="#f0eee5")
yy3 = dy3 + 16
p.text(ix + 22, yy3 + 26, "이번 달의 D-데이", 24, "sans", True, OLIVE)
yy3 += 52
for t in dlist:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P6 col3 ends", dy3 + sh2)

# ---- P6 exercises ----
ey = 1560
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "연습　Esercizi p. 6", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Risposte a p. 8　I livelli possono mescolarsi; cerca per numero", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A　표 읽기", 25)
e.glossline("6면의 표를 보고 맞는 답을 고르세요.")
e.ex("B2", "Scelta multipla", "B", "Questa settimana le Korean Series hanno un risultato",
     "이번 주의 한국시리즈는 뭐예요? A. 발표된 일정 · B. 결과 나왔어요 · C. 아직 몰라요", size=20, gap=7)
e.ex("B2", "Scelta multipla", "A", "Sondaggio del 9 nov.: il kimjang costa 199 456 won",
     "11월 9일 조사의 김장비용은 얼마예요? A. 199,456원 · B. 219,071원 · C. 54,980원", size=20, gap=7)
e.ex("B2", "Scelta multipla", "B", "Le date previste delle foglie sono passate",
     "단풍 예보 날짜는 어떻게 됐어요? A. 아직 안 지났어요 · B. 지났어요 · C. 내일이에요", size=20, gap=7)
e.ex("B2", "Scelta multipla", "C", "I risultati del CSAT escono l'11 dic.",
     "수능 성적은 언제 나와요? A. 11월 19일 · B. 11월 22일 · C. 12월 11일", size=20, gap=7)
e.ex("B2", "Scelta multipla", "A", "La settimana scorsa la Serie era solo un calendario",
     "지난주의 한국시리즈는 뭐였어요? A. 발표된 일정 · B. 결과 · C. 취소된 경기", size=20, gap=7)
e.head("B　이해", 25)
e.glossline("6면의 글을 읽고 맞는 답을 고르세요.")
e.ex("B2", "Scelta multipla", "A", "Gara 1: kt ha vinto 8-7",
     "한국시리즈 1차전은 어떻게 됐어요? A. kt 8대 7 승리 · B. 삼성 3대 2 승리 · C. 비로 취소", size=20, gap=7)
e.ex("B2", "Scelta multipla", "B", "Il servizio meteo osserva circa l'80%",
     "기상청 관측의 절정 기준은 뭐예요? A. 잎의 50% · B. 산 전체의 약 80% · C. 잎의 100%", size=20, gap=7)
e.ex("B2", "Scelta multipla", "A", "Un cavolo, 16 ott.: 5 557 won",
     "10월 16일 기준 배추 한 포기는 얼마예요? A. 5,557원 · B. 20,269원 · C. 54,980원", size=20, gap=7)
e.ex("B2", "Scelta multipla", "A", "La data di riferimento del sondaggio sul kimjang è il 9 nov.",
     "김장비용 조사의 기준 날짜는 언제예요? A. 11월 9일 · B. 10월 16일 · C. 11월 22일", size=20, gap=7)
e.ex("B2", "Scelta multipla", "A", "Candidati quest'anno: 551 864",
     "올해 수험생은 몇 명이에요? A. 551,864명 · B. 1,312명 · C. 3,271명", size=20, gap=7)
e.head("C　말 넣기", 25)
e.glossline("빈칸에 알맞은 말을 넣으세요.")
e.ex("B2", "Completare", "발표", "Un calendario pubblicato può cambiare",
     "한국시리즈 일정은 ___된 일정이었어요.", instr="Completare", size=20, gap=7)
e.ex("B2", "Completare", "결과", "I risultati arrivano solo dopo le partite",
     "___는 경기가 끝난 뒤에야 나와요.", instr="Completare", size=20, gap=7)
e.ex("B2", "Completare", "기준", "Le date differiscono perché i criteri differiscono",
     "날짜가 다른 이유는 ___이 다르기 때문이에요.", instr="Completare", size=20, gap=7)
e.ex("B2", "Completare", "날짜", "Quando leggi le notizie, controlla prima la data",
     "숫자를 읽을 때는 기준 ___를 먼저 봐야 해요.", instr="Completare", size=20, gap=7)
e.head("D　맞다 틀리다", 25)
e.glossline("문장이 맞으면 맞다, 틀리면 틀리다를 고르세요.")
e.ex("B2", "Vero o falso", "틀리다", "Le misure speciali valgono solo il 19 nov.",
     "특별 조치는 11월 16일부터 적용돼요. A. 맞다 · B. 틀리다", size=20, gap=7)
e.ex("B2", "Vero o falso", "맞다", "Samsung ha vinto il titolo 4-1",
     "삼성은 4승 1패로 우승했어요. A. 맞다 · B. 틀리다", size=20, gap=7)
e.ex("B2", "Vero o falso", "틀리다", "Le date previste non sono date osservate",
     "예보 날짜는 실제 관측 날짜와 항상 같아요. A. 맞다 · B. 틀리다", size=20, gap=7)
e.ex("B2", "Vero o falso", "맞다", "I risultati escono l'11 dic.",
     "성적은 12월 11일에 나와요. A. 맞다 · B. 틀리다", size=20, gap=7)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-gipi.svg")
print("P6 saved, exercises so far:", len(REG))
