# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-ko-pt/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 말 공부 (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("말 공부 · Língua", "Lucerna", "언어 포커스 · 세 가지 레벨, 세 가지 주제 · Três níveis, três temas")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 날씨의 말", 24)
a.para("태풍 소식을 읽을 때 자주 보는 말이 있어요. '북상하다'는 북쪽으로 올라가다예요. 태풍이 가는 길을 '진로'라고 해요.", 21.5)
a.para("태풍이 가까이 와서 비와 바람이 강해지는 곳은, 태풍의 '영향권'에 들어요. 영향권 소식은 기상청에서 자주 확인하세요.", 21.5)
a.expl("영향권 = zona de influência · 가까이 = perto, ao se aproximar")
a.ex("A2", "Complete a frase", "북상하고", "북상하다 = avançar para o norte",
     "태풍이 북쪽으로 올라가고 있어요. = 태풍이 ___ 있어요.", instr="Complete", size=20.5, gap=10)
a.ex("A2", "Escolha múltipla", "A", "진로 = o caminho que o tufão segue",
     "'진로'는 무슨 뜻이에요? A. 태풍이 가는 길 · B. 태풍의 이름 · C. 바람의 속도", size=20.5, gap=10)
a.ex("A2", "Complete a frase", "최신", "최신 = o mais recente",
     "나가기 전에 ___ 소식을 확인하세요.", instr="Complete", size=20.5, gap=10)
a.ex("A2", "Escolha múltipla", "A", "Na zona de influência, a chuva e o vento ficam mais fortes",
     "영향권에 든 곳은 어떻게 돼요? A. 비와 바람이 강해져요 · B. 눈이 와요 · C. 아주 더워져요", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 날짜 세는 말", 24)
b.para("한국에서는 중요한 날까지 남은 날짜를 'D-29'처럼 써요. 오늘이 10월 21일, 수능이 11월 19일이니까 오늘이 D-29예요.", 21.5)
b.para("내일이 바로 그날이면 D-1, 오늘이 바로 그날이면 D-데이예요. 달력에서 날짜를 셀 때 자주 쓰는 말이에요.", 21.5)
b.expl("남다 = restar, faltar · 바로 = exatamente")
b.ex("B1", "Complete a frase", "D-29", "Faltam 29 dias para o exame = D-29",
     "수능까지 29일이 남았어요. 오늘이 ___예요.", instr="Complete", size=20.5, gap=10)
b.ex("B1", "Escolha múltipla", "B", "D-1 = amanhã",
     "D-1은 무슨 뜻이에요? A. 어제 · B. 내일 · C. 오늘", size=20.5, gap=10)
b.ex("B1", "Complete a frase", "7", "Uma semana = 7 dias = D-7",
     "일주일이 남았어요. = D-___", instr="Complete", size=20.5, gap=10)
b.ex("B1", "Escolha múltipla", "A", "O D-day é o próprio dia",
     "맞는 말은 어느 것이에요? A. D-데이는 바로 그날이에요 · B. D-29는 29일이 지났어요 · C. D-1은 일주일 전이에요", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 예보 읽는 법", 24)
c.para("예보를 읽을 때는 날짜와 함께 '기준'을 봐야 해요. 산림청은 잎의 50%, 웨더아이는 산 전체의 80%를 절정의 기준으로 해요.", 21.5)
c.para("기준이 다르면 날짜도 달라져요. 그래서 소식을 읽을 때 '어떤 기준인가요?'를 먼저 생각하세요. (6면)", 21.5)
c.expl("기준 = critério · 먼저 확인하다 = verificar primeiro")
c.ex("B2", "Complete a frase", "기준", "Os critérios são diferentes (pág. 6)",
     "두 날짜가 다른 이유는 ___이 다르기 때문이에요.", instr="Complete", size=20.5, gap=10)
c.ex("B2", "Escolha múltipla", "A", "O critério florestal: 50% das folhas",
     "산림청의 절정 기준은 뭐예요? A. 잎의 50% · B. 산 전체의 80% · C. 첫눈이 오는 날", size=20.5, gap=10)
c.ex("B2", "Complete a frase", "절정", "절정 = o momento mais bonito",
     "단풍이 가장 아름다운 때를 ___이라고 해요.", instr="Complete", size=20.5, gap=10)
c.ex("B2", "Escolha múltipla", "B", "Leia a previsão junto com o critério e a data",
     "예보를 읽을 때 먼저 볼 것은 뭐예요? A. 날짜만 · B. 기준과 날짜 · C. 사진", size=20.5, gap=10)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「저는 학교에서 갔어요」", "→ '가다' 앞에서는 '에'예요: '학교에 갔어요'. '에서'는 행동이 있는 곳이에요.", "Vai-se a um lugar com «에»; «에서» indica o lugar da ação."),
    ("「할수 있어요」", "→ 띄어 써요: '할 수 있어요'. '수'는 혼자 한 칸으로 써요.", "Em «할 수 있어요», «수» vai separado."),
    ("「책를 읽어요」", "→ 받침이 있으면 '을'이에요: '책을 읽어요'.", "Com batchim usa-se «을»; sem batchim, «를»."),
    ("「저는 학생이에요. 이름은 민준입니다」", "→ 한 글에서는 문체를 하나로 해요: '이름은 민준이에요'.", "Em um texto, um só estilo de fala."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "실수 병원 · A clínica dos erros", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「〜까지 ○일 남았어요」 — '수능까지 29일 남았어요.' 날짜를 셀 때 쓰는 틀이에요. 물어볼 때는 '〜까지 얼마 남았어요?'라고 해요."
wcn = "A estrutura: «faltam ○ dias para ~». Para perguntar: «〜까지 얼마 남았어요?»"
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "이번 주의 틀 · A frase-modelo", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「안녕하세요. 저는 대학생이에요. 금요일에 하늘공원에 가요. 억새가 보고 싶어요. 일요일에는 야구 플레이오프를 봐요!」 — 독자 편지의 예"
lcn = "Carta de exemplo da redação, não é uma carta de verdade. O VOL.2 publicará cartas de verdade e a melhor redação da pág. 8!"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "독자의 편지 · Cartas dos leitores", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "이번 주의 문장 · Frases da semana (ao pé da letra, desta edição)", 27, "sans", True, OLIVE)
quotes = [
    ("「경로는 아직 바뀔 수 있어요」", "A trajetória ainda pode mudar.", "1면"),
    ("「자세한 소식은 4면에 있어요」", "Os detalhes estão na pág. 4.", "1면"),
    ("「나가기 전에 기상청의 최신 소식을 꼭 확인하세요」", "Antes de sair, confira sem falta as últimas notícias da agência de meteorologia.", "2면"),
    ("「시험까지 29일이 남았어요」", "Faltam 29 dias para o exame.", "2면"),
    ("「이번 주 금요일이 마지막 날이에요」", "Esta sexta-feira é o último dia.", "3면"),
    ("「경기 결과는 다음 주 신문에서 알려 드릴게요」", "Os resultados sairão no jornal da próxima semana.", "4면"),
    ("「작은 캐릭터가 큰 사랑을 받고 있어요」", "Um personagem pequeno recebe um grande carinho.", "5면"),
    ("「두 날짜는 모두 맞을 수 있어요」", "As duas datas podem estar certas.", "6면"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 150
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 150 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "다음 주 · Na próxima semana (VOL.2)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "준플레이오프 결과와 플레이오프 소식을 전해요. 태풍 참피는 어디로 갔을까요? 실제 진로를 확인해요. 단풍은 절정이 됐을까요? 10월 31일 할로윈 소식도 있어요. 여러분의 편지와 8면 쓰기 우수작도 실어요. 기대해 주세요!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-mal.svg")
print("P7 saved, exercises so far:", len(REG))
