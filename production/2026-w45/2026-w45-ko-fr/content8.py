# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ko-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · 시험과 답 =================
CURPAGE[0] = 8
p = BSPage4()
p.band("시험과 답 · Test et réponses", "Lucerna", "제8면 · 이번 주의 큰 시험 + 모든 답")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · 이번 주 연표", 21, OLIVE, 5)
f.ex("B1", "Texte à trous", "A", "L'Ipdong tombe le samedi 7 novembre",
     "입동은 11월 ___일이에요. (A. 7 · B. 8)", size=13.8, gap=0)
f.ex("B1", "Texte à trous", "A", "Le Suneung a lieu le jeudi 19 novembre",
     "수능은 11월 ___일이에요. (A. 19 · B. 29)", size=13.8, gap=0)
f.ex("B1", "Texte à trous", "A", "L'examen d'histoire a lieu le samedi 28 novembre",
     "한능검 시험은 11월 ___일이에요. (A. 28 · B. 6)", size=13.8, gap=0)
f.ex("B1", "Texte à trous", "A", "La fête de Cheongsong sur place commence le 4 novembre",
     "청송 현장 축제는 11월 ___일부터예요. (A. 4 · B. 3)", size=13.8, gap=0)
f.ex("B1", "Texte à trous", "A", "Trois victoires d'affilée",
     "KIA는 LG를 ___연승으로 이겼어요. (A. 3 · B. 2)", size=13.8, gap=0)
f.ex("B1", "Texte à trous", "A", "Pluie au Samgakbong du Hallasan : 415,5 mm",
     "한라산 삼각봉에 온 비는 ___밀리미터예요. (A. 415.5 · B. 415)", size=13.8, gap=0)
f.ex("B1", "Texte à trous", "A", "Séoul : 3 271 agents pour Halloween",
     "서울시 할로윈 안전 인력은 ___명이에요. (A. 3,271 · B. 1,620)", size=13.8, gap=0)
f.ex("B1", "Texte à trous", "A", "Pic observé à Seoraksan : 16 octobre",
     "설악산 실제 관측 절정은 10월 ___일이었어요. (A. 16 · B. 20)", size=13.8, gap=0)
f.head("B · 일반 문제", 21, OLIVE, 5)
f.ex("A2", "Choix multiple", "A", "Candidats cette année : 551 864",
     "올해 수험생은 몇 명이에요? A. 551,864명 · B. 1,312명 · C. 3,271명", size=13.8, gap=0)
f.ex("B1", "Choix multiple", "B", "Centres d'examen dans tout le pays : 1 312",
     "시험장은 전국에 몇 곳이에요? A. 551,864곳 · B. 1,312곳 · C. 312곳", size=13.8, gap=0)
f.ex("B1", "Choix multiple", "A", "Pic de Naejangsan selon le Service des forêts : 4 novembre",
     "내장산 산림청 예보의 절정은 언제예요? A. 11월 4일 · B. 11월 11일 · C. 11월 9일", size=13.8, gap=0)
f.ex("B1", "Choix multiple", "B", "Pic de Naejangsan selon l'Office des parcs : 11 novembre",
     "내장산 공단 예보의 절정은 언제예요? A. 11월 4일 · B. 11월 11일 · C. 11월 9일", size=13.8, gap=0)
f.ex("B1", "Choix multiple", "B", "Pic de Wolchulsan selon le Service des forêts : 9 novembre",
     "월출산 산림청 예보의 절정은 언제예요? A. 11월 4일 · B. 11월 9일 · C. 11월 11일", size=13.8, gap=0)
f.ex("B1", "Choix multiple", "A", "Le 1er match des play-offs reporté pour cause de pluie",
     "플레이오프 1차전이 미뤄진 이유는 뭐예요? A. 비 · B. 눈 · C. 정전", size=13.8, gap=0)
f.ex("B1", "Choix multiple", "A", "Inscriptions à Séoul de 10 h à 12 h",
     "한능검 서울 접수는 언제예요? A. 11월 6일 10시부터 12시까지 · B. 11월 3일 하루 종일 · C. 11월 10일 오후", size=13.8, gap=0)
f.ex("A2", "Choix multiple", "B", "La vigilance dure jusqu'au 15 décembre",
     "산불조심기간은 언제까지예요? A. 11월 7일까지 · B. 12월 15일까지 · C. 11월 19일까지", size=13.8, gap=0)
f.head("C · 읽고 답하기", 21, OLIVE, 5)
f.para("지민이는 대학생이에요. 이번 주 토요일에 친구와 내장산에 단풍을 보러 가요. 일요일에는 집에서 김장을 도와요. 다음 주에는 한능검 시험을 준비해요. 지민이는 한국사를 좋아해요.", 15, lh=1.3, split=False)
f.ex("A2", "Choix multiple", "B", "Jimin va à Naejangsan samedi",
     "지민이는 토요일에 어디에 가요? A. 청송 · B. 내장산 · C. 제주도", size=13.8, gap=0)
f.ex("A2", "Choix multiple", "A", "Dimanche, elle aide au kimjang",
     "일요일에 지민이는 무엇을 해요? A. 집에서 김장을 도와요 · B. 야구를 봐요 · C. 시험을 봐요", size=13.8, gap=0)
f.ex("A2", "Choix multiple", "B", "La semaine prochaine, elle prépare l'examen d'histoire",
     "다음 주에 지민이는 무엇을 준비해요? A. 수능 · B. 한능검 시험 · C. 사과축제", size=13.8, gap=0)
f.ex("B1", "Choix multiple", "C", "Jimin aime l'histoire de Corée",
     "지민이는 무엇을 좋아해요? A. 야구 · B. 사과 · C. 한국사", size=13.8, gap=0)
f.head("D · 문장 만들기", 21, OLIVE, 5)
f.ex("A2", "Former une phrase", "저는 토요일에 내장산에 가요.", "Ordre : sujet + temps + lieu + verbe",
     "저는 / 토요일에 / 내장산에 가요 → ___", instr="Former une phrase", size=13.8, gap=0)
f.ex("A2", "Former une phrase", "우리는 김장을 도와요.", "Ordre : sujet + objet + verbe",
     "우리는 / 김장을 / 도와요 → ___", instr="Former une phrase", size=13.8, gap=0)
f.ex("B1", "Former une phrase", "지민이는 단풍을 보러 가요.", "보러 가요 = aller voir",
     "지민이는 / 단풍을 / 보러 가요 → ___", instr="Former une phrase", size=13.8, gap=0)
f.ex("B1", "Former une phrase", "수험생은 도서관에서 공부해요.", "Le lieu de l'action prend « 에서 »",
     "수험생은 / 도서관에서 / 공부해요 → ___", instr="Former une phrase", size=13.8, gap=0)
f.head("E · 번역", 21, OLIVE, 5)
f.ex("A2", "Traduction", "Le 7 novembre, c'est l'Ipdong.", "Voir page 1",
     "11월 7일은 입동이에요. → ___", instr="Traduire", size=13.8, gap=0)
f.ex("A2", "Traduction", "Il reste 12 jours avant le Suneung.", "Voir page 5",
     "수능까지 12일이 남았어요. → ___", instr="Traduire", size=13.8, gap=0)
f.ex("B1", "Traduction", "특별 조치는 11월 19일에만 적용돼요.", "Voir page 6",
     "Les mesures spéciales ne s'appliquent que le 19 novembre. → ___", instr="Traduire", size=13.8, gap=0)
f.ex("B2", "Traduction", "저는 토요일에 내장산에 단풍을 보러 가요.", "Voir page 3",
     "Samedi, je vais à Naejangsan voir les feuillages. → ___", instr="Traduire", size=13.8, gap=0)
f.head("F · 이번 주의 말", 21, OLIVE, 5)
f.match_set("B2", "Appariement",
            ["입동", "절정", "김장", "온대저기압"],
            ["겨울의 첫 절기",
             "단풍이 가장 아름다운 때",
             "겨울 김치를 담그는 일",
             "참피가 10월 26일에 바뀐 것"],
            ["a", "b", "c", "d"],
            ["입동=le début de l'hiver a", "절정=le plus beau moment b", "김장=le kimchi de l'hiver c", "온대저기압=le typhon devenu cyclone le 26 octobre d"],
            instr="Associer")
f.head("G · 도서관에서", 21, OLIVE, 5)
f.ex("B1", "Texte à trous", "A", "Aller à Naejangsan samedi",
     "— 토요일에 어디에 가요? — ___에 가요. (A. 내장산 · B. 청송)", size=13.8, gap=0)
f.ex("B1", "Texte à trous", "A", "Kimjang = le kimchi de l'hiver",
     "— 김장은 뭐예요? — 겨울 ___를 담그는 일이에요. (A. 김치 · B. 사과)", size=13.8, gap=0)
f.ex("B1", "Texte à trous", "A", "Les inscriptions à Séoul commencent à 10 h",
     "— 한능검 서울 접수는 언제예요? — 11월 6일 ___부터예요. (A. 10시 · B. 13시)", size=13.8, gap=0, bw=334)
f.ex("B1", "Texte à trous", "A", "Les dates diffèrent car les critères diffèrent",
     "— 단풍 절정 날짜가 왜 달라요? — ___이 달라서예요. (A. 기준 · B. 날씨)", size=13.8, gap=0)
f.ex("B1", "Texte à trous", "A", "Les mesures ne s'appliquent que le 19 novembre",
     "— 수능 조치는 언제 적용돼요? — 11월 ___일에만 적용돼요. (A. 19 · B. 7)", size=13.8, gap=0, bw=354)
f.head("H · 써 보기", 21, OLIVE, 5)
MODELO = ("나의 겨울 준비는 김장부터 시작해요. "
          "토요일에는 가족과 함께 배추를 절이고 양념을 버무려요. "
          "일요일에는 두꺼운 이불을 꺼내고 겨울옷을 정리해요. "
          "단풍이 진 뒤에는 산보다 집이 좋아져요. "
          "따뜻한 국을 끓여 가족과 함께 먹어요. "
          "겨울이 와도 마음은 따뜻해요. 준비를 마치면 마음이 놓여요. "
          "저녁에는 가족과 함께 따뜻한 차를 마셔요. 겨울 준비가 끝나면 마음이 든든해져요.")
NCHARS = len(MODELO.replace(" ", ""))
f.glossline(f"쓰기 문제예요 (정답은 하나가 아니에요). 아래에 {NCHARS}자의 예가 있어요.")
f.ex("B1", "Rédaction", "(question ouverte — modèle ci-dessous)", f"Modèle dans la section H de cette page ({NCHARS} caractères)",
     "「나의 겨울 준비」에 대해 150~200자로 쓰세요. 김장, 월동 준비, 단풍 중에서 하나를 고르세요.", instr="Écrire", size=13.8, gap=0)
f.para("예: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= 답 =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "답 · Réponses — classées par page, cherchez le numéro", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Chaque réponse avec une courte note en français · ✓ = exercice à texte modèle", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— 제{pg}면 —", 13.3, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Rédaction":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.3, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-siheom.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("by type", dict(Counter(e["type"] for e in REG)))
print("model chars:", NCHARS)
