# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · AVALIAÇÃO E RESPOSTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("AVALIAÇÃO E RESPOSTAS　연습과 정답", "A Lucerna", "8면　이번 주의 큰 시험 + 모든 정답")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETE A CRÔNICA", 22, OLIVE, 5)
f.ex("B1", "빈칸 고르기", "A", "11월 20일 금요일은 전국 공휴일이에요",
     "Sexta, 20 de novembro, é ___ no Brasil. (A. feriado nacional · B. dia útil)", size=14.5, gap=0)
f.ex("B1", "빈칸 고르기", "A", "공휴일은 줌비 두스 파우마리스를 기려요",
     "O feriado lembra a morte de ___ . (A. Zumbi dos Palmares · B. Deodoro da Fonseca)", size=14.5, gap=0)
f.ex("B1", "빈칸 고르기", "B", "2026년 공휴일은 금요일에 걸려요",
     "Em 2026, o feriado cai numa ___ . (A. segunda · B. sexta)", size=14.5, gap=0)
f.ex("B1", "빈칸 고르기", "A", "코파 두 브라지우 결승은 12월 6일이에요",
     "A final da Copa do Brasil é no dia ___ de dezembro. (A. 6 · B. 15)", size=14.5, gap=0)
f.ex("B1", "빈칸 고르기", "B", "결승: 그레미우 × 파우메이라스",
     "Na final, jogam Grêmio e ___ . (A. Vasco · B. Palmeiras)", size=14.5, gap=0)
f.ex("B1", "빈칸 고르기", "A", "공식 정답은 11월 말까지 발표돼요",
     "O gabarito oficial sai até o ___ de novembro. (A. fim · B. dia 8)", size=14.5, gap=0)
f.ex("B1", "빈칸 고르기", "A", "에넴 둘째 날은 11월 15일이에요",
     "O segundo dia do Enem foi no domingo ___ . (A. 15 · B. 8)", size=14.5, gap=0)
f.ex("B1", "빈칸 고르기", "B", "둘째 날 시험은 5시간이에요",
     "No dia 15, a prova dura ___ horas. (A. três · B. cinco)", size=14.5, gap=0)
f.head("B　PERGUNTAS GERAIS", 22, OLIVE, 5)
f.ex("A2", "하나 고르기", "B", "2023년 법으로 11월 20일이 전국 공휴일이 됐어요",
     "A Lei nº 14.759, de 2023... A. criou o dia 20 · B. fez do dia 20 feriado nacional · C. acabou com o feriado", size=14.5, gap=0)
f.ex("B1", "하나 고르기", "A", "그레미우는 합산 3–1로 올라갔어요",
     "O Grêmio passou à final com... A. 3 a 1 no total · B. 2 a 2 no total · C. 1 a 0 no total", size=14.5, gap=0)
f.ex("B1", "하나 고르기", "B", "승부차기 5–4: 파우메이라스가 올라갔어요",
     "Nos pênaltis, o Palmeiras venceu por... A. 4 a 3 · B. 5 a 4 · C. 6 a 5", size=14.5, gap=0)
f.ex("B1", "하나 고르기", "B", "노리스가 상파울루 그랑프리에서 우승했어요",
     "O Grande Prêmio de São Paulo foi vencido por... A. Verstappen · B. Norris · C. Hadjar", size=14.5, gap=0)
f.ex("B1", "하나 고르기", "A", "36라운드: 파우메이라스 × 플라멩구는 토요일 21일",
     "A rodada 36 tem Palmeiras × Flamengo no... A. sábado 21 · B. domingo 22 · C. dia 15", size=14.5, gap=0)
f.ex("A2", "하나 고르기", "B", "카포에이라는 아프로브라질 사람의 격투이자 음악 예술이에요",
     "A capoeira é... A. um jogo de cartas · B. uma arte afro-brasileira de luta e música · C. um prato típico", size=14.5, gap=0)
f.ex("B2", "하나 고르기", "A", "10 공식 정답까지의 평일 수예요",
     "O número 10, na página 6, mede... A. os dias úteis até o gabarito · B. os gols da final · C. os feriados", size=14.5, gap=0)
f.ex("B1", "하나 고르기", "A", "파우마리스는 알라고아스주에 있었어요",
     "O Quilombo dos Palmares ficava... A. em Alagoas · B. no Rio · C. em São Paulo", size=14.5, gap=0)
f.head("C　LEIA E RESPONDA", 22, OLIVE, 5)
f.para("Rafael mora em Salvador. Na sexta, 20, ele não trabalha: é feriado nacional. De manhã, ele vai a uma roda de capoeira no Pelourinho. À tarde, ele lê sobre Zumbi e Palmares e escreve duas frases em português. No sábado, 21, ele assiste a Palmeiras × Flamengo na televisão. No domingo, 22, ele descansa e prepara a semana: na segunda, ele volta ao trabalho e confere o gabarito extraoficial do Enem.", 15.5, lh=1.3, split=False)
f.ex("A2", "하나 고르기", "B", "하파에우는 사우바도르에 살아요",
     "Onde mora Rafael? A. no Rio · B. em Salvador · C. em Brasília", size=14.5, gap=0)
f.ex("A2", "하나 고르기", "B", "금요일에 그는 카포에이라 모임에 가요",
     "Na sexta, 20, Rafael... A. trabalha · B. vai a uma roda de capoeira · C. faz o Enem", size=14.5, gap=0)
f.ex("A2", "하나 고르기", "A", "토요일에 그는 파우메이라스를 봐요 × 플라멩구",
     "No sábado, 21, Rafael assiste... A. a Palmeiras × Flamengo · B. ao Enem · C. a uma aula", size=14.5, gap=0)
f.ex("A2", "하나 고르기", "B", "월요일에 그는 비공식 정답을 확인해요",
     "Na segunda, Rafael confere... A. o gabarito oficial · B. o gabarito extraoficial · C. a nota final", size=14.5, gap=0)
f.head("D　CONSTRUA AS FRASES", 22, OLIVE, 5)
f.ex("A2", "문장 만들기", "Sexta é feriado nacional.", "시간 말이 먼저 와요",
     "sexta / é / feriado nacional → ___", instr="문장 만들기", size=14.5, gap=0)
f.ex("B1", "문장 만들기", "O Grêmio empatou por 1 a 1.", "주어 + 동사 + 방법",
     "o grêmio / empatou / por 1 a 1 → ___", instr="문장 만들기", size=14.5, gap=0)
f.ex("B1", "문장 만들기", "Quando sair o gabarito, confira as respostas.", "시간 종속절 + 주절",
     "quando / sair / o gabarito / confira / as respostas → ___", instr="문장 만들기", size=14.5, gap=0)
f.ex("B1", "문장 만들기", "O Brasil lembra Zumbi em 20 de novembro.", "주어 + 동사 + 목적어 + 시간",
     "o brasil / lembra / zumbi / em 20 de novembro → ___", instr="문장 만들기", size=14.5, gap=0)
f.head("E　TRADUZA", 22, OLIVE, 5)
f.ex("A2", "번역", "11월 20일 금요일은 전국 공휴일이에요.", "1면 머리기사를 보세요",
     "Sexta, 20 de novembro, é feriado nacional. → ___", instr="번역", size=14.5, gap=0)
f.ex("B1", "번역", "파우메이라스는 승부차기에서 5–4로 이겼어요.", "nos pênaltis = 승부차기에서",
     "O Palmeiras venceu nos pênaltis por 5 a 4. → ___", instr="번역", size=14.5, gap=0)
f.ex("B1", "번역", "O gabarito oficial sai até o fim de novembro.", "oficial = 공식",
     "“공식 정답은 11월 말까지 발표돼요.” → ___", instr="번역", size=14.5, gap=0)
f.ex("B2", "번역", "Anote as suas respostas e confira quando sair o gabarito oficial.", "명령형 anote/confira + quando 종속절",
     "“자기 답을 적어 두고, 공식 정답이 나오면 확인해요.” → ___", instr="번역", size=14.5, gap=0)
f.head("F　AS PALAVRAS DA SEMANA", 22, OLIVE, 5)
f.match_set("B2", "어휘 연결하기",
            ["a consciência", "o gabarito", "o feriadão", "o agregado"],
            ["o placar dos dois jogos somados",
             "um fim de semana de três dias com feriado",
             "o saber e a memória de uma história",
             "as respostas oficiais das questões objetivas"],
            ["c", "d", "b", "a"],
            ["consciência=알기와 기억하기 c", "gabarito=객관식 공식 정답 d", "feriadão=공휴일이 낀 3일 주말 b", "agregado=두 경기 합산 점수 a"],
            instr="단어와 뜻 연결하기")
f.head("G　DIÁLOGO NA BILHETERIA", 22, OLIVE, 5)
f.ex("B1", "빈칸 고르기", "A", "마네 가힌샤 경기장",
     "— O jogo é no ___ Garrincha. (A. Mané · B. Maracanã)", size=14.5, gap=0)
f.ex("B1", "빈칸 고르기", "A", "그레미우는 여섯 번째 우승을 노려요",
     "— O Grêmio busca o ___ título. (A. sexto · B. primeiro)", size=14.5, gap=0)
f.ex("B1", "빈칸 고르기", "A", "파우메이라스는 다섯 번째 우승을 노려요",
     "— E o Palmeiras busca o ___ . (A. quinto · B. décimo)", size=14.5, gap=0)
f.ex("B1", "빈칸 고르기", "A", "표는 온라인으로 팔아요",
     "— Os ingressos estão à venda ___ internet. (A. na · B. no)", size=14.5, gap=0)
f.ex("B1", "빈칸 고르기", "A", "obrigado = 고마워요",
     "— Boa final! — Muito ___! (A. obrigado · B. tarde)", size=14.5, gap=0)
f.head("H　ESCREVA VOCÊ", 22, OLIVE, 5)
MODELO = ("Sexta, 20 de novembro, acordo sem despertador: é feriado nacional. "
          "De manhã, leio sobre Zumbi e Palmares e escrevo duas frases em português. "
          "À tarde, vou a uma roda de capoeira no bairro e ouço histórias de resistência. "
          "No sábado, assisto a Palmeiras × Flamengo na televisão, com a família. "
          "No domingo, descanso, preparo a semana e confiro o gabarito extraoficial do Enem. "
          "Na segunda, volto ao trabalho com calma: o feriadão foi curto, mas a memória fica. "
          "O dia 20 lembra a luta e a cultura afro-brasileiras.")
NWORDS = len(MODELO.split())
f.bridge(f"작문 과제（정답은 하나가 아니에요）. 모범 글（{NWORDS}단어）은 아래에 있어요.")
f.ex("B1", "작문", "（자유 과제 — 모범 글은 아래에 있어요）", f"모범 글은 이 페이지 H 부분에 있어요（{NWORDS}단어）",
     "«O seu feriadão de 20 a 22 de novembro» Escreva 80–100 palavras: o que você faz na sexta, no sábado e no domingo, e o que a data de 20 de novembro lembra.", instr="작문", size=14.5, gap=0)
f.para("Texto modelo: " + MODELO, 15, lh=1.3, split=False, max_w=395)  # fix1 D7 (2026-11-11): wrap at 395, not the full 422.5 column — Cairo renders Newsreader ~3% wider than PIL measures, so two lines crossed the column edge 1862 (+2/+14px). Words, size (15) and 88-word count unchanged; worst line PIL 387.0, predicted rendered ink right ~1841.
f.end_report()
print("P8 exercises end y:", f.y, "col:", f.ci)

# ---- P8 image: the final stadium (col 3, below the exercises flow) ----
# The exercise flow fills cols 0-2 to the bottom; only its last column has
# free space below f.y, so the image goes there, positioned dynamically.
iy8 = (f.y + 12) if f.ci == 3 else 190
img_h = min(250, 1150 - iy8)
assert img_h >= 150, f"P8 image has no room: f.y={f.y} ci={f.ci}"
image(p, "garrincha.jpg", COLX[3], iy8, CW, img_h)
cap_end = caption(p, COLX[3], iy8 + img_h, CW,
        "O estádio Mané Garrincha, em Brasília: a final é no dia 6 de dezembro.",
        "Foto: Luis Dantas — Domínio público")
print("P8 image ends ~", cap_end)

# ================= RESPOSTAS =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "RESPOSTAS　정답 — 페이지별로 정리돼 있어요. 번호를 찾으세요", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "정답마다 짧은 설명이 있어요　✓ 는 모범 글이에요", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "작문":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.5, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-avaliacao.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("model words:", NWORDS)
