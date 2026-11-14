# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · 시험과 답 =================
CURPAGE[0] = 8
p = BSPage4()
p.band("시험과 답　Teste e respostas", "Lucerna", "제8면　이번 주의 큰 시험 + 모든 답")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　이번 주 연표", 21, OLIVE, 5)
f.ex("B1", "Cloze", "A", "Champi é o tufão n.º 30 deste ano",
     "태풍 참피는 제___호 태풍이에요. (A. 30 · B. 13)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "A agência mudou a previsão no dia 21",
     "기상청이 예보를 바꾼 날은 10월 ___일이에요. (A. 20 · B. 21)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "O exame de admissão é quinta-feira, 19 de novembro",
     "수능은 11월 ___일이에요. (A. 19 · B. 29)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "A festa da erva-prateada vai até 23 de outubro",
     "서울억새축제는 10월 ___일까지예요. (A. 23 · B. 25)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "O playoff começa no domingo",
     "플레이오프는 ___요일에 시작해요. (A. 토 · B. 일)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "À meia-noite, subiu ao 5.º lugar",
     "엔믹스의 노래는 자정에 ___위까지 올라갔어요. (A. 34 · B. 5)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "No mapa do Serviço Florestal, Seoraksan culmina no dia 20",
     "산림청 지도로 설악산 절정은 10월 ___일이에요. (A. 20 · B. 25)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "Chiikawa passa de 1,5 milhão de espectadores",
     "치이카와 영화의 관객은 ___만 명이 넘어요. (A. 150 · B. 15)", size=13.8, gap=0)
f.head("B　일반 문제", 21, OLIVE, 5)
f.ex("A2", "Escolha múltipla", "A", "Este ano os candidatos são 551.864",
     "올해 수험생은 몇 명이에요? A. 551,864명 · B. 1,312명 · C. 75,000명", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "B", "Os locais de prova são 1.312 em todo o país",
     "시험장은 전국에 몇 곳이에요? A. 551,864곳 · B. 1,312곳 · C. 312곳", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "A", "Vento máximo de 59 metros por segundo",
     "참피의 최대 풍속은 얼마예요? A. 초속 59미터 · B. 초속 30미터 · C. 905미터", size=13.8, gap=0)
f.ex("A2", "Escolha múltipla", "B", "Emoticons para as primeiras 75.000 pessoas",
     "청송 이모티콘은 몇 명까지 받을 수 있어요? A. 7,500명 · B. 75,000명 · C. 750,000명", size=13.8, gap=0)
f.ex("A2", "Escolha múltipla", "C", "Chiikawa em 3.º nas tendências do dia 17",
     "치이카와는 10월 17일 트렌드에서 몇 위였어요? A. 1위 · B. 5위 · C. 3위", size=13.8, gap=0)
f.ex("A2", "Escolha múltipla", "A", "A 25.ª Festa da Erva-Prateada de Seul",
     "서울억새축제는 몇 회예요? A. 25회 · B. 20회 · C. 30회", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "B", "A Weatheri coloca o pico de Seoraksan em 25 de outubro",
     "웨더아이와 국립공원공단의 설악산 절정은 며칠이에요? A. 10월 20일 · B. 10월 25일 · C. 11월 4일", size=13.8, gap=0)
f.ex("A2", "Escolha múltipla", "A", "A Série Coreana começa em 2 de novembro",
     "한국시리즈는 언제부터예요? A. 11월 2일 · B. 10월 25일 · C. 11월 19일", size=13.8, gap=0)
f.head("C　읽고 답하기", 21, OLIVE, 5)
f.para("민준이는 대학생이에요. 이번 주 금요일에 친구와 하늘공원에 가요. 억새축제의 마지막 날이에요. 토요일에는 집에서 태풍 소식을 봐요. 일요일에는 야구 플레이오프를 봐요. 민준이는 KIA를 응원해요.", 15, lh=1.3, split=False)
f.ex("A2", "Escolha múltipla", "B", "Minjun vai na sexta-feira ao Parque Haneul",
     "민준이는 금요일에 어디에 가요? A. 청송 · B. 하늘공원 · C. 제주도", size=13.8, gap=0)
f.ex("A2", "Escolha múltipla", "A", "Porque é o último dia da festa da erva-prateada",
     "금요일에 하늘공원에 왜 가요? A. 억새축제 마지막 날이라서 · B. 사과를 사려고 · C. 야구를 보려고", size=13.8, gap=0)
f.ex("A2", "Escolha múltipla", "B", "No sábado, vê as notícias do tufão",
     "토요일에 민준이는 무엇을 해요? A. 산에 가요 · B. 태풍 소식을 봐요 · C. 시험을 봐요", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "C", "Minjun torce pelo KIA",
     "민준이는 어느 팀을 응원해요? A. LG · B. 삼성 · C. KIA", size=13.8, gap=0)
f.head("D　문장 만들기", 21, OLIVE, 5)
f.ex("A2", "Monte a frase", "저는 금요일에 하늘공원에 가요.", "Ordem: sujeito + tempo + lugar + verbo",
     "저는 / 금요일에 / 하늘공원에 가요 → ___", instr="Monte", size=13.8, gap=0)
f.ex("A2", "Monte a frase", "태풍이 북쪽으로 오고 있어요.", "북쪽으로 = para o norte",
     "태풍이 / 북쪽으로 / 오고 있어요 → ___", instr="Monte", size=13.8, gap=0)
f.ex("B1", "Monte a frase", "우리는 단풍을 보러 가요.", "보러 가요 = ir ver",
     "우리는 / 단풍을 / 보러 가요 → ___", instr="Monte", size=13.8, gap=0)
f.ex("B1", "Monte a frase", "누나는 도서관에서 공부해요.", "O lugar da ação com «에서»",
     "누나는 / 도서관에서 / 공부해요 → ___", instr="Monte", size=13.8, gap=0)
f.head("E　번역", 21, OLIVE, 5)
f.ex("A2", "Tradução", "A trajetória do tufão ainda pode mudar.", "Compare com a pág. 1",
     "태풍의 경로는 아직 바뀔 수 있어요. → ___", instr="Traduza", size=13.8, gap=0)
f.ex("A2", "Tradução", "Faltam 29 dias para o exame.", "Compare com a pág. 2",
     "시험까지 29일이 남았어요. → ___", instr="Traduza", size=13.8, gap=0)
f.ex("B1", "Tradução", "주말에는 최신 날씨를 확인하세요.", "Compare com a pág. 1",
     "No fim de semana, confira a previsão mais recente. → ___", instr="Traduza", size=13.8, gap=0)
f.ex("B2", "Tradução", "저는 금요일에 하늘공원에 억새를 보러 가요.", "Compare com a pág. 3",
     "Na sexta-feira, vou ao Parque Haneul ver a erva-prateada. → ___", instr="Traduza", size=13.8, gap=0)
f.head("F　이번 주의 말", 21, OLIVE, 5)
f.match_set("B2", "Associação",
            ["북상하다", "절정", "진로", "수험생"],
            ["시험을 보는 학생",
             "북쪽으로 올라가다",
             "가장 아름다운 때",
             "태풍이 가는 길"],
            ["b", "c", "d", "a"],
            ["북상하다 = avançar para o norte (b)", "절정 = o pico, o momento mais bonito (c)", "진로 = trajetória, rota (d)", "수험생 = candidato ao exame (a)"],
            instr="Associe")
f.head("G　도서관에서", 21, OLIVE, 5)
f.ex("B1", "Cloze", "A", "O exame de admissão é em 19 de novembro",
     "— 수능이 언제예요? — 11월 ___이에요. (A. 19일 · B. 21일)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "Na manhã da prova, o metrô passa mais vezes",
     "— 시험 날 아침에 지하철은요? — 더 자주 ___. (A. 쉬어요 · B. 다녀요)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "Durante a prova de escuta, os aviões não pousam",
     "— 비행기는요? — 듣기 시간에는 뜨거나 ___ 않아요. (A. 내리지 · B. 보지)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "D-29 = faltam 29 dias",
     "— D-29가 뭐예요? — 시험까지 29일이 ___ 뜻이에요. (A. 지났다는 · B. 남았다는)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "Para incentivar: «힘내세요» (força!)",
     "— 응원 한마디 해 주세요. — ___! (A. 안녕히 가세요 · B. 힘내세요)", size=13.8, gap=0)
f.head("H　써 보기", 21, OLIVE, 5)
MODELO = ("나의 가을 주말은 야구와 단풍의 주말이에요. "
          "토요일 아침에는 먼저 태풍 소식을 확인해요. 바람이 강하면 밖에 나가지 않아요. "
          "오후에는 집에서 야구 플레이오프를 봐요. 저는 KIA를 응원해요. "
          "일요일에는 친구와 산에 가요. 단풍이 절정이라서 아주 예뻐요. "
          "사진을 많이 찍고 싶어요. 집에 돌아와서는 찍은 사진을 보고 짧은 일기를 써요. "
          "가을은 짧지만 재미있는 일이 많은 계절이에요.")
NCHARS = len(MODELO.replace(" ", ""))
f.expl(f"É um exercício de escrita (não há uma única resposta certa). Abaixo há um exemplo de {NCHARS} caracteres.")
f.ex("B1", "Escrita", "(pergunta aberta — o modelo está abaixo)", f"O modelo está na seção H desta página ({NCHARS} caracteres)",
     "「나의 가을 주말」에 대해 150~200자로 쓰세요. 날씨, 야구, 단풍 중에서 하나를 고르세요.", instr="Escreva", size=13.8, gap=0)
f.para("예: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= 답 =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "답　Respostas — ordenadas por página, procure o número", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Cada resposta com uma breve nota em português　✓ = exercício com modelo", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— 제{pg}면 —", 13.3, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Escrita":
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
