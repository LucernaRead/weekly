# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-ko-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · 청년 (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("청년 · Jeunesse", "Lucerna", "레벨 B1 · 수능 D-7 주간과 빼빼로데이 · La semaine D-7 du Suneung et le jour des Pepero")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-feature")
f.title("수능까지 일주일 — 마지막 정리, 온 나라의 응원", 37)
f.byline("Lucerna 편집부 · 읽기 레벨: B1")
f.para("목요일 11월 12일에는 수능까지 딱 일주일이 남아요. 수능은 11월 19일 목요일이에요. 올해 수험생은 551,864명이에요. 시험장은 전국에 1,312곳이에요. 고3 교실에서는 마지막 정리가 한창이에요.")
f.para("수능이 가까워지면 온 나라가 수험생을 응원해요. 시험장 앞에서는 '힘내세요!', '떨지 마세요!', '잘할 수 있어요!'라는 말이 가득해요. 합격을 비는 마음으로 찹쌀떡이나 엿을 선물하기도 해요. 끈끈한 음식은 '꼭 붙어라'는 뜻을 담고 있어요.", w=414)
f.para("그런데 조심해야 할 말이 있어요. 시험 날의 특별한 조치는 11월 19일에만 적용돼요. 회사와 관공서가 10시부터 일을 시작하고, 지하철이 더 자주 다니고, 영어 듣기 시간(13시 10분~13시 35분)에 비행기가 뜨거나 내리지 않는 것 — 모두 11월 19일의 일이에요. 이번 주(11월 9~15일)의 조치가 아니에요. 자세한 이야기는 6면에 있어요.")
f.gloss("정리 = rangement, révision · 끈끈하다 = collant · 합격 = réussite.")
f.head("예비소집 — 11월 18일 수요일", 25)
f.para("수능 전날인 11월 18일에는 예비소집이 있어요. 예비소집에서는 수험표를 받고 시험장을 확인해요. 모이는 시각과 장소는 원서접수증에 나와 있어요. 시험 당일에는 8시 10분까지 시험실에 들어가야 해요.", w=424)
f.para("수험표를 잃어버리면 당일 아침 8시까지 시험장 관리본부에 신고하면 다시 받을 수 있어요. 사진이 붙은 실물 신분증도 꼭 챙기세요. 휴대전화와 스마트워치 같은 전자기기는 시험 시간 전에 내야 해요.")
f.gloss("관리본부 = bureau de gestion · 신고하다 = déclarer · 챙기다 = préparer")
f.box("이번 주 청년 숫자 · Chiffres jeunes", [
    ("551,864명 — 올해 수험생", "serif", False, INK, 20.5, 1.4),
    ("1,312곳 — 전국 시험장", "serif", False, INK, 20.5, 1.4),
    ("8시 10분 — 시험 당일 입실 완료 시각", "serif", False, INK, 20.5, 1.4),
    ("13시 10분~13시 35분 — 11월 19일 영어 듣기 시간", "serif", False, INK, 20.5, 1.4, 338),
])
f.head("11월 11일, 청년의 빼빼로데이", 25)
f.para("11월 11일에는 친구에게 빼빼로를 나눠 줘요. 길고 가늰 과자 한 상자를 건네며 '날씬해지자'고 말하기도 해요. 요즘은 손편지와 함께 주는 사람도 많아요. 과자보다 마음이 더 중요해요.")
f.para("가래떡을 나누는 친구도 있어요. 우리 쌀로 만든 가래떡은 길고 하얘요. 농업인의 날의 뜻을 생각하며 가래떡을 먹는 거예요. 빼빼로와 가래떡, 둘 다 나누는 마음은 같아요.")
f.gloss("건네다 = tendre, remettre · 날씬해지다 = mincir · 하얗다 = blanc")
f.head("시험 전날의 하루", 25)
f.para("시험 전날에는 일찍 자요. 밤늦게까지 공부하면 아침에 피곤해져요. 준비물은 미리 챙겨요. 수험표와 신분증, 연필을 가방에 넣어요.")
f.para("아침밥은 꼭 먹어요. 밥을 먹어야 머리가 잘 돌아가요. 너무 많이 먹으면 졸려요. 평소 먹던 대로 먹는 것이 좋아요.")
f.gloss("피곤하다 = fatigué · 졸리다 = somnolent · 평소 = d'habitude")
f.end_report()

# col 3: study image + 당신
ix = COLX[3]
image(p, "study.jpg", ix, 200, CW, 230)
cy3 = caption(p, ix, 430, CW, "도서관에서 공부하는 학생들. 수험생에게 가을은 가장 바쁜 계절이에요.",
              "사진: Gary Todd — CC0 (Wikimedia Commons) · 자료 사진")
ey3 = cy3 + 24
etvous = "당신은? 수험생에게 해 주고 싶은 응원 한마디는 뭐예요? 한국어로 두 문장 써서 보내 주세요."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Et vous ? Quel mot d'encouragement voulez-vous dire aux candidats ? Écrivez deux phrases en coréen et envoyez-les-nous.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "당신은? · À vous", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Et vous ? Quel mot d'encouragement voulez-vous dire aux candidats ? Écrivez deux phrases en coréen et envoyez-les-nous.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "연습 · Exercices page 5", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Réponses page 8 · Les niveaux sont mélangés, cherchez le numéro", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · 이해", 25)
e.glossline("5면의 글을 읽고 맞는 답을 고르세요.")
e.ex("B1", "Choix multiple", "A", "Le 12 novembre, c'est D-7",
     "11월 12일에는 수능까지 며칠이 남아요? A. 7일 · B. 10일 · C. 4일", size=20, gap=7)
e.ex("B1", "Choix multiple", "B", "Le Suneung a lieu le jeudi 19 novembre",
     "수능은 며칠에 있어요? A. 11월 12일 · B. 11월 19일 · C. 11월 28일", size=20, gap=7)
e.ex("B1", "Choix multiple", "A", "La convocation préliminaire a lieu le mercredi 18 novembre",
     "예비소집은 언제예요? A. 11월 18일 · B. 11월 19일 · C. 11월 12일", size=20, gap=7)
e.ex("B1", "Choix multiple", "B", "Le jour de l'examen, être en salle avant 8 h 10",
     "시험 당일 입실 완료 시각은 언제예요? A. 10시 · B. 8시 10분 · C. 13시 10분", size=20, gap=7)
e.ex("B1", "Choix multiple", "A", "Le jour des Pepero, on partage les fins bâtonnets",
     "빼빼로데이에는 무엇을 나눠 줘요? A. 길고 가늰 과자 · B. 가래떡만 · C. 김치", size=20, gap=7)
e.head("B · 말 넣기", 25)
e.glossline("빈칸에 알맞은 말을 넣으세요.")
e.ex("B1", "Compléter", "응원", "Tout le pays encourage les candidats",
     "온 나라가 수험생을 ___해요.", instr="Complétez", size=20, gap=7)
e.ex("B1", "Compléter", "예비소집", "Retirer sa convocation à la réunion préliminaire",
     "11월 18일 ___에서는 수험표를 받아요.", instr="Complétez", size=20, gap=7)
e.ex("B1", "Compléter", "선물", "On offre tteok de riz gluant et yeot en souhaitant la réussite",
     "합격을 비는 마음으로 찹쌀떡이나 엿을 ___하기도 해요.", instr="Complétez", size=20, gap=7, bw=424)
e.ex("B1", "Compléter", "신분증", "Une pièce d'identité physique avec photo",
     "사진이 붙은 실물 ___도 꼭 챙기세요.", instr="Complétez", size=20, gap=7)
e.ex("B1", "Compléter", "가래떡", "Le jour des garaetteok, on partage des garaetteok",
     "가래떡데이에는 ___을 나눠요.", instr="Complétez", size=20, gap=7)
e.head("C · 숫자와 날짜", 25)
e.glossline("5면의 숫자로 답하세요.")
e.ex("B1", "Compléter", "551,864", "Candidats cette année : 551 864",
     "올해 수험생은 ___명이에요.", instr="Complétez", size=20, gap=7)
e.ex("B1", "Compléter", "1,312", "Centres d'examen dans tout le pays : 1 312",
     "시험장은 전국에 ___곳이에요.", instr="Complétez", size=20, gap=7)
e.ex("B1", "Compléter", "10", "Le jour de l'examen, les bureaux ouvrent à 10 h",
     "시험 날, 회사와 관공서는 ___시부터 일을 시작해요.", instr="Complétez", size=20, gap=7, bw=354)
e.ex("B1", "Compléter", "18", "La convocation préliminaire a lieu le 18 novembre",
     "예비소집은 11월 ___일에 있어요.", instr="Complétez", size=20, gap=7)
e.head("D · 문장 만들기", 25)
e.glossline("말을 바른 순서로 놓아 문장을 만드세요.")
e.ex("B1", "Former une phrase", "수험생은 열심히 공부해요.", "Ordre : sujet + adverbe + verbe",
     "수험생은 / 열심히 / 공부해요 → ___", instr="Former une phrase", size=20, gap=7)
e.ex("B1", "Former une phrase", "우리는 수험생을 응원해요.", "Ordre : sujet + objet + verbe",
     "우리는 / 수험생을 / 응원해요 → ___", instr="Former une phrase", size=20, gap=7)
e.ex("B1", "Former une phrase", "비행기는 듣기 시간에 뜨지 않아요.", "Pendant l'écoute, aucun avion ne décolle ni n'atterrit",
     "비행기는 / 듣기 시간에 / 뜨지 않아요 → ___", instr="Former une phrase", size=20, gap=7)
e.ex("B1", "Former une phrase", "친구는 빼빼로를 나눠 줘요.", "Les amis partagent des Pepero",
     "친구는 / 빼빼로를 / 나눠 줘요 → ___", instr="Former une phrase", size=20, gap=7)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-cheongnyeon.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · 깊이 읽기 (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("깊이 읽기 · Lecture approfondie", "Lucerna", "레벨 B2 · 예보와 발표를 읽는 법 · Comment lire les prévisions et les annonces")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1180, tag="P6-feature")
f.title("예보와 발표를 읽는 법 — 날짜, 기준, 결과를 나누세요", 37)
f.byline("Lucerna 편집부 · 읽기 레벨: B2")
f.para("이번 주 신문에는 예보와 발표가 많아요. 단풍 예보, 한국시리즈 발표 일정, 수능 날짜 — 읽을 때는 세 가지를 나눠야 해요. 날짜, 기준, 결과예요. 날짜는 언제인지, 기준은 무엇으로 잰 것인지, 결과는 이미 나온 것인지 아직인지 — 세 가지를 섞으면 뉴스를 잘못 읽게 돼요.", w=404)
f.para("단풍부터 봐요. 산림청 예보는 잎의 50%를 기준으로 해요. 기상청 관측은 산 전체의 약 80%를 기준으로 해요. 기준이 다르면 날짜도 달라져요. 내장산은 산림청 예보 11월 4일, 공단 예보 11월 11일이에요. 어느 날짜가 '진짜'인지 물을 때는 기준부터 물어보세요.")
f.para("발표와 결과도 달라요. 한국시리즈 일정은 '발표된 일정'이에요. 플레이오프가 5차전까지 가고 이동일이 하루 필요해서, 처음 발표는 11월 2일 시작이었지만 바뀐 발표는 11월 3일 시작이에요. 발표는 바뀔 수 있어요. 결과는 경기가 끝난 뒤에야 나와요. 이 신문이 마감한 11월 2일에는 1차전 결과조차 없었어요.")
f.para("숫자도 읽는 법이 있어요. 올해 수험생은 551,864명, 시험장은 1,312곳이에요. 큰 숫자는 나라 전체의 규모를 보여줘요. 숫자가 크다고 해서 개인의 시험이 더 어려워지는 것은 아니에요. 내 시험장은 1,312곳 중 한 곳일 뿐이에요.")
f.para("그래서 뉴스를 읽을 때는 날짜를 먼저 보세요. '예보'인지 '관측'인지, '발표'인지 '결과'인지도 보세요. 날짜와 기준과 결과를 나누면, 뉴스가 훨씬 쉽게 읽혀요.", w=394)
f.gloss("재다 = mesurer · 규모 = ampleur · 섞다 = mélanger, confondre")
f.head("결과를 모를 때", 25)
f.para("결과를 모를 때는 모른다고 말하는 것이 정직해요. 이 신문은 한국시리즈 결과를 모른다고 분명히 말했어요. 모르는 결과를 예상으로 채우면 독자를 속이게 돼요.", w=374)
f.gloss("정직하다 = honnête · 채우다 = remplir · 속이다 = tromper")
f.head("뉴스의 날짜 찾기", 25)
f.para("뉴스를 읽을 때는 제목보다 날짜를 먼저 봐요. 날짜가 있는 뉴스가 믿을 수 있어요.", w=374)
f.para("'예정'과 '확정'도 나눠야 해요. 예정은 아직 정해지지 않은 일, 확정은 정해진 일이에요. 예정된 일을 확정된 일처럼 읽으면 안 돼요.")
f.gloss("예정 = prévu · 확정 = confirmé · 믿다 = croire.")
f.end_report()

# ---- comparison table (cols 0-2) ----
ty = 1210
p.text(MX, ty + 26, "이번 주와 시험 날, 한눈에 보기 · Cette semaine et le jour de l'examen, en un coup d'œil", 26, "sans", True, OLIVE)
p.hline(MX, COLX[2] + CW, ty + 40, GOLD, 2)
rows = [
    ("구분", "이번 주 (11월 9~15일)", "시험 날 (11월 19일)"),
    ("날짜 세기", "D-10 ~ D-4", "D-데이"),
    ("분위기", "카운트다운", "시험 당일"),
    ("특별 조치", "없어요 (평상시)", "있어요 (10시 출근 등)"),
]
tw = [300, 544, 544]
yy = ty + 58
for r, (c0, c1, c2) in enumerate(rows):
    x0 = MX
    for j, cell in enumerate((c0, c1, c2)):
        hdr = (r == 0)
        p.rect(x0, yy, tw[j], 52, fill=DARK if hdr else (BOX if r % 2 else "#f1ead6"), stroke=LINE, sw=1.1)
        p.text(x0 + 18, yy + 35, cell, 21 if not hdr else 20, "sans" if hdr else "serif", hdr,
               "#f3edda" if hdr else INK)
        x0 += tw[j]
    yy += 52
p.para(MX, yy + 30, "표의 자료: 교육부 발표 (10월 20일) — 조치는 11월 19일에만 적용돼요. 이번 주에는 특별 조치가 없어요.", 19.5, "serif", False, GREY, 1388, 1.4)

# col 3: how-to-read boxes (no image on P6)
ix = COLX[3]
howto = ["① 날짜를 봐요", "② 기준을 봐요", "③ 결과를 봐요"]
sy3 = 200 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in howto) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "수능 뉴스 읽는 법", 24, "sans", True, OLIVE)
yy3 += 52
for t in howto:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
dy3 = sy3 + sh + 26
dlist = ["D-10 — 11월 9일", "D-7 — 11월 12일", "D-4 — 11월 15일", "D-데이 — 11월 19일"]
sh2 = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in dlist) + 32
p.rect(ix, dy3, CW, sh2, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = dy3 + 16
p.text(ix + 22, yy3 + 26, "이번 달의 D-데이", 24, "sans", True, OLIVE)
yy3 += 52
for t in dlist:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P6 col3 ends", dy3 + sh2)

# ---- P6 exercises ----
ey = 1560
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "연습 · Exercices page 6", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Réponses page 8 · Les niveaux sont mélangés, cherchez le numéro", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · 표 읽기", 25)
e.glossline("6면의 표를 보고 맞는 답을 고르세요.")
e.ex("B2", "Choix multiple", "B", "Cette semaine, le compte à rebours va de D-10 à D-4",
     "이번 주의 날짜 세기는 뭐예요? A. D-데이 · B. D-10 ~ D-4 · C. D-1", size=20, gap=7)
e.ex("B2", "Choix multiple", "A", "Le jour de l'examen, il y a des mesures spéciales",
     "시험 날의 특별 조치는 있어요? A. 있어요 · B. 없어요 · C. 아직 몰라요", size=20, gap=7)
e.ex("B2", "Choix multiple", "B", "Cette semaine, pas de mesures spéciales",
     "이번 주의 특별 조치는 있어요? A. 있어요 · B. 없어요 · C. 10시 출근만 있어요", size=20, gap=7)
e.ex("B2", "Choix multiple", "C", "Le jour de l'examen, c'est le D-day",
     "시험 날의 날짜 세기는 뭐예요? A. D-10 · B. D-7 · C. D-데이", size=20, gap=7)
e.ex("B2", "Choix multiple", "A", "Cette semaine, l'ambiance est au compte à rebours",
     "이번 주의 분위기는 뭐예요? A. 카운트다운 · B. 시험 당일 · C. 방학", size=20, gap=7)
e.head("B · 이해", 25)
e.glossline("6면의 글을 읽고 맞는 답을 고르세요.")
e.ex("B2", "Choix multiple", "A", "Le critère du Service des forêts : 50 % des feuilles",
     "산림청의 절정 기준은 뭐예요? A. 잎의 50% · B. 산 전체의 80% · C. 첫눈이 오는 날", size=20, gap=7)
e.ex("B2", "Choix multiple", "B", "Le service météo observe environ 80 %",
     "기상청 관측의 절정 기준은 뭐예요? A. 잎의 50% · B. 산 전체의 약 80% · C. 잎의 100%", size=20, gap=7)
e.ex("B2", "Choix multiple", "A", "L'ouverture des Korean Series est repoussée au 3 novembre",
     "바뀐 한국시리즈 시작일은 언제예요? A. 11월 3일 · B. 11월 2일 · C. 11월 9일", size=20, gap=7)
e.ex("B2", "Choix multiple", "A", "Candidats cette année : 551 864",
     "올해 수험생은 몇 명이에요? A. 551,864명 · B. 1,312명 · C. 3,271명", size=20, gap=7)
e.ex("B2", "Choix multiple", "B", "Centres d'examen dans tout le pays : 1 312",
     "시험장은 전국에 몇 곳이에요? A. 551,864곳 · B. 1,312곳 · C. 3,271곳", size=20, gap=7)
e.head("C · 말 넣기", 25)
e.glossline("빈칸에 알맞은 말을 넣으세요.")
e.ex("B2", "Compléter", "기준", "Les dates diffèrent car les critères diffèrent",
     "날짜가 다른 이유는 ___이 다르기 때문이에요.", instr="Complétez", size=20, gap=7)
e.ex("B2", "Compléter", "발표", "Un calendrier annoncé peut changer",
     "한국시리즈 일정은 ___된 일정이에요.", instr="Complétez", size=20, gap=7)
e.ex("B2", "Compléter", "결과", "Les résultats n'arrivent qu'après les matches",
     "___는 경기가 끝난 뒤에야 나와요.", instr="Complétez", size=20, gap=7)
e.ex("B2", "Compléter", "규모", "Les grands chiffres montrent l'ampleur nationale",
     "큰 숫자는 나라 전체의 ___를 보여줘요.", instr="Complétez", size=20, gap=7)
e.head("D · 맞다 틀리다", 25)
e.glossline("문장이 맞으면 맞다, 틀리면 틀리다를 고르세요.")
e.ex("B2", "Vrai ou faux", "틀리다", "Les mesures spéciales ne s'appliquent que le 19 novembre",
     "특별 조치는 11월 9일부터 적용돼요. A. 맞다 · B. 틀리다", size=20, gap=7)
e.ex("B2", "Vrai ou faux", "맞다", "Le 12 novembre, c'est D-7",
     "11월 12일은 D-7예요. A. 맞다 · B. 틀리다", size=20, gap=7)
e.ex("B2", "Vrai ou faux", "틀리다", "Une date prévue n'est pas une date observée",
     "예보 날짜는 실제 관측 날짜와 항상 같아요. A. 맞다 · B. 틀리다", size=20, gap=7)
e.ex("B2", "Vrai ou faux", "맞다", "Si l'on ne connaît pas le résultat, il faut le dire",
     "결과를 모를 때는 모른다고 말하는 것이 정직해요. A. 맞다 · B. 틀리다", size=20, gap=7)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-gipi.svg")
print("P6 saved, exercises so far:", len(REG))
