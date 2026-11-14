# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · 시험과 답 =================
CURPAGE[0] = 8
p = BSPage4()
p.band("시험과 답　Test et réponses", "Lucerna", "제8면　이번 주의 큰 시험 + 모든 답")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　이번 주 연표", 21, OLIVE, 5)
f.ex("B1", "Texte à trous", "A", "Champi est le typhon n° 30 de l'année",
     "태풍 참피는 제___호 태풍이에요. (A. 30 · B. 13)", size=13.8, gap=0)
f.ex("B1", "Texte à trous", "B", "Météo Corée a changé ses prévisions le 21",
     "기상청이 예보를 바꾼 날은 10월 ___일이에요. (A. 20 · B. 21)", size=13.8, gap=0)
f.ex("B1", "Texte à trous", "A", "Le Suneung est le jeudi 19 novembre",
     "수능은 11월 ___일이에요. (A. 19 · B. 29)", size=13.8, gap=0)
f.ex("B1", "Texte à trous", "A", "La Fête des herbes argentées dure jusqu'au 23 octobre",
     "서울억새축제는 10월 ___일까지예요. (A. 23 · B. 25)", size=13.8, gap=0)
f.ex("B1", "Texte à trous", "B", "Les séries éliminatoires commencent dimanche",
     "플레이오프는 ___요일에 시작해요. (A. 토 · B. 일)", size=13.8, gap=0)
f.ex("B1", "Texte à trous", "B", "À minuit, elle est montée à la 5e place",
     "엔믹스의 노래는 자정에 ___위까지 올라갔어요. (A. 34 · B. 5)", size=13.8, gap=0)
f.ex("B1", "Texte à trous", "A", "Sur la carte du Service des forêts, Seoraksan culmine le 20",
     "산림청 지도로 설악산 절정은 10월 ___일이에요. (A. 20 · B. 25)", size=13.8, gap=0)
f.ex("B1", "Texte à trous", "A", "Plus de 1,5 million de spectateurs pour Chiikawa",
     "치이카와 영화의 관객은 ___만 명이 넘어요. (A. 150 · B. 15)", size=13.8, gap=0)
f.head("B　일반 문제", 21, OLIVE, 5)
f.ex("A2", "Choix multiple", "A", "551 864 candidats cette année",
     "올해 수험생은 몇 명이에요? A. 551,864명 · B. 1,312명 · C. 75,000명", size=13.8, gap=0)
f.ex("B1", "Choix multiple", "B", "1 312 centres d'examen dans tout le pays",
     "시험장은 전국에 몇 곳이에요? A. 551,864곳 · B. 1,312곳 · C. 312곳", size=13.8, gap=0)
f.ex("B1", "Choix multiple", "A", "Des vents maximums de 59 mètres par seconde",
     "참피의 최대 풍속은 얼마예요? A. 초속 59미터 · B. 초속 30미터 · C. 905미터", size=13.8, gap=0)
f.ex("A2", "Choix multiple", "B", "Des émoticônes pour les 75 000 premiers",
     "청송 이모티콘은 몇 명까지 받을 수 있어요? A. 7,500명 · B. 75,000명 · C. 750,000명", size=13.8, gap=0)
f.ex("A2", "Choix multiple", "C", "Chiikawa était 3e des tendances Google le 17",
     "치이카와는 10월 17일 트렌드에서 몇 위였어요? A. 1위 · B. 5위 · C. 3위", size=13.8, gap=0)
f.ex("A2", "Choix multiple", "A", "La 25e Fête des herbes argentées de Séoul",
     "서울억새축제는 몇 회예요? A. 25회 · B. 20회 · C. 30회", size=13.8, gap=0)
f.ex("B1", "Choix multiple", "B", "Weatheri place le pic de Seoraksan au 25 octobre",
     "웨더아이와 국립공원공단의 설악산 절정은 며칠이에요? A. 10월 20일 · B. 10월 25일 · C. 11월 4일", size=13.8, gap=0)
f.ex("A2", "Choix multiple", "A", "Les Korean Series commencent le 2 novembre",
     "한국시리즈는 언제부터예요? A. 11월 2일 · B. 10월 25일 · C. 11월 19일", size=13.8, gap=0)
f.head("C　읽고 답하기", 21, OLIVE, 5)
f.para("민준이는 대학생이에요. 이번 주 금요일에 친구와 하늘공원에 가요. 억새축제의 마지막 날이에요. 토요일에는 집에서 태풍 소식을 봐요. 일요일에는 야구 플레이오프를 봐요. 민준이는 KIA를 응원해요.", 15, lh=1.3, split=False)
f.ex("A2", "Choix multiple", "B", "Minjun va au parc Haneul vendredi",
     "민준이는 금요일에 어디에 가요? A. 청송 · B. 하늘공원 · C. 제주도", size=13.8, gap=0)
f.ex("A2", "Choix multiple", "A", "Parce que c'est le dernier jour de la fête des herbes argentées",
     "금요일에 하늘공원에 왜 가요? A. 억새축제 마지막 날이라서 · B. 사과를 사려고 · C. 야구를 보려고", size=13.8, gap=0)
f.ex("A2", "Choix multiple", "B", "Samedi, il regarde les nouvelles du typhon à la maison",
     "토요일에 민준이는 무엇을 해요? A. 산에 가요 · B. 태풍 소식을 봐요 · C. 시험을 봐요", size=13.8, gap=0)
f.ex("B1", "Choix multiple", "C", "Minjun soutient KIA",
     "민준이는 어느 팀을 응원해요? A. LG · B. 삼성 · C. KIA", size=13.8, gap=0)
f.head("D　문장 만들기", 21, OLIVE, 5)
f.ex("A2", "Former une phrase", "저는 금요일에 하늘공원에 가요.", "Ordre : sujet + repère de temps + lieu + verbe",
     "저는 / 금요일에 / 하늘공원에 가요 → ___", instr="Former une phrase", size=13.8, gap=0)
f.ex("A2", "Former une phrase", "태풍이 북쪽으로 오고 있어요.", "북쪽으로 = vers le nord",
     "태풍이 / 북쪽으로 / 오고 있어요 → ___", instr="Former une phrase", size=13.8, gap=0)
f.ex("B1", "Former une phrase", "우리는 단풍을 보러 가요.", "보러 가요 = aller voir",
     "우리는 / 단풍을 / 보러 가요 → ___", instr="Former une phrase", size=13.8, gap=0)
f.ex("B1", "Former une phrase", "누나는 도서관에서 공부해요.", "에서 marque le lieu où se passe l'action",
     "누나는 / 도서관에서 / 공부해요 → ___", instr="Former une phrase", size=13.8, gap=0)
f.head("E　번역", 21, OLIVE, 5)
f.ex("A2", "Traduction", "La trajectoire du typhon peut encore changer.", "Voir page 1",
     "태풍의 경로는 아직 바뀔 수 있어요. → ___", instr="Traduire", size=13.8, gap=0)
f.ex("A2", "Traduction", "Il reste 29 jours avant l'examen.", "Voir page 2",
     "시험까지 29일이 남았어요. → ___", instr="Traduire", size=13.8, gap=0)
f.ex("B1", "Traduction", "주말에는 최신 날씨를 확인하세요.", "Voir page 1",
     "Merci de vérifier la météo la plus récente ce week-end. → ___", instr="Traduire", size=13.8, gap=0)
f.ex("B2", "Traduction", "저는 금요일에 하늘공원에 억새를 보러 가요.", "Voir page 3",
     "Vendredi, je vais au parc Haneul voir les herbes argentées. → ___", instr="Traduire", size=13.8, gap=0)
f.head("F　이번 주의 말", 21, OLIVE, 5)
f.match_set("B2", "Appariement",
            ["북상하다", "절정", "진로", "수험생"],
            ["시험을 보는 학생",
             "북쪽으로 올라가다",
             "가장 아름다운 때",
             "태풍이 가는 길"],
            ["b", "c", "d", "a"],
            ["북상하다 = monter vers le nord (b)", "절정 = le pic, le meilleur moment (c)", "진로 = trajectoire, parcours (d)", "수험생 = candidat à l'examen (a)"],
            instr="Associer")
f.head("G　도서관에서", 21, OLIVE, 5)
f.ex("B1", "Texte à trous", "A", "Le Suneung est le 19 novembre",
     "— 수능이 언제예요? — 11월 ___이에요. (A. 19일 · B. 21일)", size=13.8, gap=0)
f.ex("B1", "Texte à trous", "B", "Le matin de l'examen, les métros circulent plus souvent",
     "— 시험 날 아침에 지하철은요? — 더 자주 ___. (A. 쉬어요 · B. 다녀요)", size=13.8, gap=0)
f.ex("B1", "Texte à trous", "A", "Les avions n'atterrissent pas pendant l'épreuve d'écoute",
     "— 비행기는요? — 듣기 시간에는 뜨거나 ___ 않아요. (A. 내리지 · B. 보지)", size=13.8, gap=0)
f.ex("B1", "Texte à trous", "B", "D-29 = il reste 29 jours",
     "— D-29가 뭐예요? — 시험까지 29일이 ___ 뜻이에요. (A. 지났다는 · B. 남았다는)", size=13.8, gap=0)
f.ex("B1", "Texte à trous", "B", "Pour encourager : 힘내세요 ! (« Allez, courage ! »)",
     "— 응원 한마디 해 주세요. — ___! (A. 안녕히 가세요 · B. 힘내세요)", size=13.8, gap=0)
f.head("H　써 보기", 21, OLIVE, 5)
MODELO = ("나의 가을 주말은 야구와 단풍의 주말이에요. "
          "토요일 아침에는 먼저 태풍 소식을 확인해요. 바람이 강하면 밖에 나가지 않아요. "
          "오후에는 집에서 야구 플레이오프를 봐요. 저는 KIA를 응원해요. "
          "일요일에는 친구와 산에 가요. 단풍이 절정이라서 아주 예뻐요. "
          "사진을 많이 찍고 싶어요. 집에 돌아와서는 찍은 사진을 보고 짧은 일기를 써요. "
          "가을은 짧지만 재미있는 일이 많은 계절이에요.")
NCHARS = len(MODELO.replace(" ", ""))
f.expl(f"Exercice d'écriture (pas de réponse unique) ; le modèle ({NCHARS} caractères) est ci-dessous.")
f.ex("B1", "Rédaction", "(question ouverte — modèle ci-dessous)", f"Modèle dans la section H de cette page ({NCHARS} caractères)",
     "「나의 가을 주말」에 대해 150~200자로 쓰세요. 날씨, 야구, 단풍 중에서 하나를 고르세요.", instr="Écrire", size=13.8, gap=0)
f.para("예: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= 답 =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "답　Réponses — classées par page, cherchez le numéro", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Chaque réponse avec une courte note en français　✓ = exercice à texte modèle", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    head_txt = f"— 제{pg}면 —"
    first_ = by_page[pg][0]
    ftxt = f"{first_['n']}. {first_['key']} — {first_['note']}"
    if first_["type"] == "Rédaction":
        ftxt = f"{first_['n']}. ✓ {first_['note']}"
    # keep-with-next: a group heading must not be orphaned at a column foot —
    # if heading + its first key do not both fit in the current column, start
    # the group in the next column.
    need = (13.3 + af._ph(head_txt, 13.3, "sans", True, af.w, 1.16) + 2
            + af._ph(ftxt, 13.3, "serif", False, af.w, 1.16) + 0.5)
    if af.y + need > af.bottom and af.ci < len(af.cols) - 1:
        af.ci += 1
        af.y = af.top
    af.para(head_txt, 13.3, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
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
