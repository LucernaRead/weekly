# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/pt-ko-proof/reg-ko-copy/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · JOVENS (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JOVENS · 청년", "A Lucerna", "NÍVEL B1 · A reta final dos jovens · 막바지 주간: 청년들의 마지막 한 주")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-main")
f.title("A reta final: revisar, descansar, fazer a prova", 37)
f.byline("Da redação da A Lucerna · Nível de leitura: B1")
f.para("A semana dos jovens brasileiros tem um centro: o domingo 8. Para os mais de 5 milhões de inscritos no Enem, é a reta final — a última semana de revisão antes da redação, de Linguagens e de Ciências Humanas.")
f.para("O plano da reta final cabe em cinco linhas: conferir o Cartão de Confirmação, revisar um pouco por dia, dormir bem na véspera, separar documento e caneta preta no dia anterior — e, no domingo, chegar cedo. Nada de maratona na véspera: quem dorme bem lembra melhor.")
f.para("E a semana tem mais: na terça, 3, as assembleias estaduais voltam do recesso; no sábado e no domingo, a Copa do Brasil decide os finalistas. O Brasil estuda de dia e torce à noite.")
f.para("No sábado, 31 de outubro, foi Halloween: a última festa antes da prova para muita gente. Agora é silêncio e revisão: o feriadão é para descansar o corpo e organizar a cabeça.")
f.box("O PLANO DA RETA FINAL", [
    ("1. Confira o Cartão de Confirmação do Enem (엔엠 확인 카드를 확인하세요)", "serif", False, INK, 21, 1.36),
    ("2. Revise um pouco por dia, sem maratona (매일 조금씩 복습해요, 벼락치기는 없어요)", "serif", False, INK, 21, 1.36),
    ("3. Durma bem na véspera da prova (시험 전날 밤에 푹 주무세요)", "serif", False, INK, 21, 1.36),
    ("4. Separe documento e caneta preta no dia anterior (전날에 신분증과 검은 펜을 챙기세요)", "serif", False, INK, 21, 1.36),
    ("5. Domingo 8: chegue antes das 12h (일요일 8일: 12시 전에 도착하세요)", "serif", False, INK, 21, 1.36),
])
f.gloss("a reta final 막바지 · a véspera 전날 밤 · a maratona 벼락치기 · separar 챙기다 · a cabeça 머리, 컨디션.")
f.end_report()

# col 3: facts + e você + copa box (sequential)
ix = COLX[3]
facts = ["Mais de 5 milhões de inscritos no Enem 2026 (Inep).",
         "Prova do dia 8: 13h30–19h, cinco horas e meia.",
         "Dia 15: o segundo dia — Natureza e Matemática (prévia)."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "OS JOVENS EM NÚMEROS", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E você? Qual é o seu plano para a véspera de uma prova importante: revisar ou descansar? Escreva duas frases em português."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("중요한 시험 전날 밤에는 복습해요? 쉬어요? 두 문장을 써서 보내 주세요.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E VOCÊ? · 여러분은요?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "중요한 시험 전날 밤에는 복습해요? 쉬어요? 두 문장을 써서 보내 주세요.", 20, "sans", False, GREY, CW - 44, 1.42)
ky3 = ey3 + eh + 26
kb = "No fim de semana, o Brasil troca o livro pela bola: sábado, Atlético-MG × Grêmio; domingo, Vasco × Palmeiras. Estudar de dia, torcer à noite — a semana cabe nos dois."
kh = 62 + len(wrap(kb, "serif", False, 21.5, CW - 44)) * 30.5 + 16
p.rect(ix, ky3, CW, kh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ky3 + 16
p.text(ix + 22, yy3 + 26, "E A COPA?", 22, "sans", True, OLIVE)
yy3 += 52
p.para(ix + 22, yy3 + 21, kb, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P5 col3 ends", ky3 + kh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EXERCÍCIOS · 5면 연습 문제", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "답은 8면에 · 수준이 섞여 있어요, 번호로 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · COMPREENSÃO", 25)
e.bridge("5면 글을 읽고 정답을 고르세요.")
e.ex("B1", "객관식", "B", "막바지 주간은 11월 8일 일요일에 끝나요",
     "A reta final termina... A. na segunda 2 · B. no domingo 8 · C. no dia 15", size=20, gap=8)
e.ex("B1", "객관식", "B", "매일 조금씩 복습해요",
     "O plano da reta final inclui... A. maratona na véspera · B. revisar um pouco por dia · C. chegar às 13h30", size=20, gap=8)
e.ex("B1", "객관식", "A", "전날 신분증과 검은 펜을 챙겨요",
     "No dia anterior, o candidato separa... A. documento e caneta preta · B. só o celular · C. a roupa da festa", size=20, gap=8)
e.ex("B1", "객관식", "B", "둘째 날은 자연과학과 수학이에요",
     "O segundo dia do Enem (dia 15) tem... A. redação · B. Natureza e Matemática · C. só Linguagens", size=20, gap=8)
e.ex("B1", "객관식", "B", "11월 3일 화요일에 주의회가 휴회를 마쳐요",
     "Na terça, 3, ... A. é o Enem · B. as assembleias voltam do recesso · C. é a final da Copa", size=20, gap=8)
e.head("B · AS PALAVRAS DO TEXTO", 25)
e.bridge("네모 안의 단어로 채우세요. 주의: 어떤 단어는 복수형이 돼요.")
e.para("reta final · inscrito · véspera · maratona · local · separar", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "문장 완성", "reta final", "reta final = 막바지 단계",
     "A semana é a ___ dos estudos.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "inscritos", "inscrito 복수 일치: inscritos",
     "Mais de 5 milhões de estudantes estão ___ no Enem.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "véspera", "véspera = 전날 밤",
     "Na ___ da prova, durma bem.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "maratona", "maratona = 벼락치기",
     "Nada de ___ na véspera.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "local", "local = 장소",
     "Confira o ___ da sua prova no cartão.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "Separe", "separar 명령형: separe",
     "___ o documento no dia anterior.", instr="빈칸 채우기", size=20, gap=8)
e.head("C · O FUTURO DO PRESENTE", 25)
e.bridge("미래형(futuro do presente)으로 채우세요.")
e.ex("B1", "문장 완성", "farão", "fazer 미래형 eles 불규칙 형태: farão",
     "Os estudantes ___ (fazer) a prova no domingo.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "mostrará", "mostrar 미래형: mostrará",
     "O cartão ___ (mostrar) o local da prova.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B2", "문장 완성", "sairão", "sair 미래형 복수: sairão",
     "Os finalistas ___ (sair) dos jogos de volta.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B2", "문장 완성", "chegará", "chegar 미래형: chegará",
     "Quem ___ (chegar) cedo não perde a prova.", instr="빈칸 채우기", size=20, gap=8)
e.head("D · VERDADEIRO OU FALSO?", 25)
e.ex("B1", "진위 판단", "Verdadeiro", "확인 카드에 시험 장소가 나와요",
     "O Cartão de Confirmação mostra o local da prova. Verdadeiro ou falso?", instr="참 / 거짓", size=20, gap=8)
e.ex("B1", "진위 판단", "Falso", "틀렸어요: 전날 벼락치기는 좋은 계획이 아니에요, 매일 조금씩 복습하는 게 좋아요",
     "A maratona na véspera é o melhor plano. Verdadeiro ou falso?", instr="참 / 거짓", size=20, gap=8)
e.ex("B2", "진위 판단", "Verdadeiro", "맞았어요: 13:30부터 19:00까지예요",
     "No domingo 8, a prova vai de 13h30 a 19h. Verdadeiro ou falso?", instr="참 / 거짓", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jovens.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · APROFUNDAMENTO (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("APROFUNDAMENTO · 심층", "A Lucerna", "NÍVEL B2 · O Enem explicado · 엔엠 자세히 보기")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1520, tag="P6-main")
f.title("O Enem explicado: dois domingos, uma prova", 37)
f.byline("Da redação da A Lucerna · Nível de leitura: B2")
f.para("O Enem 2026 tem dois domingos: 8 e 15 de novembro. No dia 8, o primeiro: redação, Linguagens e Ciências Humanas, das 13h30 às 19h — cinco horas e meia. No dia 15, o segundo: Ciências da Natureza e Matemática. Esta edição cobre o dia 8; o dia 15 é a prévia da próxima semana.")
f.para("O ritual do domingo 8 começa ao meio-dia: os portões abrem às 12h e fecham às 13h, no horário de Brasília. Quem chega depois das 13h não entra — não há segunda chamada. Leve documento com foto, caneta preta e o Cartão de Confirmação: ele mostra o seu local de prova.")
f.para("Mais de 5 milhões de estudantes estão inscritos. É muita gente para o mesmo horário: por isso o Inep pede que cada um confira o local antes do domingo. Quem confere antes não se perde no dia.")
f.para("E os números do domingo? Cinco horas e meia são 330 minutos: 60 minutos para cada hora, mais 30. É tempo para ler com calma, escrever a redação e revisar — sem correria. A regra de ouro do Enem: primeiro as fáceis, depois as difíceis, e a redação com tempo guardado.")
f.gloss("os portões 문 · a segunda chamada 재입장 · conferir 확인하다 · a correria 서두름.")
f.end_report()

# col 3: timeline + ler os números (sequential, measured)
bx = COLX[3]
p.rect(bx, 200, CW, 640, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 240, "O CAMINHO ATÉ A PROVA", 22, "sans", True, OLIVE)
steps = [
    ("2 NOV.", "Finados: feriadão de revisão, um pouco por dia."),
    ("3 NOV.", "As assembleias estaduais voltam do recesso."),
    ("8 NOV.", "Enem, dia 1: portões 12h–13h, prova 13h30–19h."),
    ("15 NOV.", "Enem, dia 2 (prévia): Natureza e Matemática."),
]
sy3 = 282
for w, t in steps:
    p.text(bx + 22, sy3 + 21, w, 20, "sans", True, BRICK)
    sy3 = p.para(bx + 164, sy3 + 21, t, 21, "serif", False, INK, CW - 186, 1.4) + 16
by3 = 866
bb = ("Diante de um número, faça três perguntas: quem publica? Quando? "
      "É busca, prova ou pesquisa? Sem essas respostas, um número diz pouco.")
bh = 62 + len(wrap(bb, "serif", False, 21.5, CW - 44)) * 30.5 + 16
p.rect(bx, by3, CW, bh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = by3 + 16
p.text(bx + 22, yy3 + 26, "LER OS NÚMEROS", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, bb, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P6 col3 ends", by3 + bh)

# ---- charts: o domingo 8 em minutos + dois domingos ----
gy = 1566
p.hline(MX, RIGHT, gy - 18, GOLD, 2)
p.text(MX, gy + 10, "O DOMINGO 8 EM NÚMEROS · 11월 8일의 숫자 (Inep 공식 시간)", 26, "sans", True, OLIVE)
bw_ = 2 * CW + GUT
# left box: o relógio do domingo (minutos)
bx1 = MX
p.rect(bx1, gy + 28, bw_, 322, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx1 + 22, gy + 68, "O RELÓGIO DO DOMINGO · do meio-dia às 19h", 21, "sans", True, INK)
relog = [("portões abertos", 60), ("espera", 30), ("prova", 330)]
yy = gy + 100
for lab, v in relog:
    p.text(bx1 + 22, yy + 24, lab, 20, "serif", True, INK)
    labw = text_w(lab, "serif", True, 20)
    p.rect(bx1 + 40 + labw, yy + 6, v * 1.5, 22, fill=OLIVE)
    p.text(bx1 + 58 + labw + v * 1.5, yy + 24, f"{v} min", 20.5, "serif", False, INK)
    yy += 44
p.para(bx1 + 22, gy + 248, "Minutos do domingo 8: 60 + 30 + 330 = 420 minutos do meio-dia às 19h.", 19.5, "serif", False, INK, bw_ - 44, 1.4)
p.para(bx1 + 22, gy + 322 - 34, "Fonte: horários oficiais do Inep para o dia 8.", 17.5, "sans", False, GREY, bw_ - 44, 1.3)
# right box: dois domingos
bx2 = COLX[2]
p.rect(bx2, gy + 28, bw_, 322, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx2 + 22, gy + 68, "DOIS DOMINGOS · uma prova", 21, "sans", True, INK)
doms = [
    "Dia 8 — redação, Linguagens, Humanas.",
    "Dia 8 — 13h30 às 19h, cinco horas e meia.",
    "Dia 15 — Natureza e Matemática (prévia).",
    "Dia 15 — a cobertura sai na próxima edição.",
]
yy = gy + 100
for t in doms:
    p.text(bx2 + 22, yy + 24, t, 20, "serif", False, INK)
    yy += 40
p.para(bx2 + 22, gy + 322 - 34, "Fonte: Inep — as provas são nos dias 8 e 15.", 17.5, "sans", False, GREY, bw_ - 44, 1.3)

# ---- P6 exercises ----
ey = 1930
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EXERCÍCIOS · 6면 연습 문제", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "답은 8면에 · 수준이 섞여 있어요, 번호로 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · LER OS GRÁFICOS", 25)
e.bridge("위 두 그래프를 보고 정답을 고르세요.")
e.ex("B2", "객관식", "B", "문이 60분 동안 열려 있어요",
     "No relógio do domingo, os portões ficam abertos... A. 30 minutos · B. 60 minutos · C. 330 minutos", size=17, gap=0)
e.ex("B2", "객관식", "A", "문이 닫힌 뒤 시험 시작까지 30분을 기다려요",
     "A espera entre o fechamento e a prova é de... A. 30 minutos · B. 60 minutos · C. 330 minutos", size=17, gap=0)
e.ex("B2", "객관식", "B", "시험은 330분이에요",
     "A prova dura... A. 60 minutos · B. 330 minutos · C. 420 minutos", size=17, gap=0)
e.ex("B2", "객관식", "B", "60 + 30 + 330 = 420",
     "60 + 30 + 330 = ... A. 390 · B. 420 · C. 360", size=17, gap=0)
e.ex("B2", "객관식", "C", "정오부터 19시까지 = 7시간",
     "Do meio-dia às 19h são... A. 5h30 · B. 6h · C. 7h", size=17, gap=0)
e.ex("B2", "객관식", "A", "그래프 숫자는 Inep 공식 시간이에요",
     "Os números do gráfico são... A. horários oficiais do Inep · B. uma pesquisa eleitoral · C. buscas no Google", size=17, gap=0)
e.head("B · COMPREENSÃO", 25)
e.ex("B2", "객관식", "B", "엔엠은 8일과 15일 두 일요일에 있어요",
     "O Enem tem... A. um só domingo · B. dois domingos: 8 e 15 · C. três domingos", size=17, gap=0)
e.ex("B2", "객관식", "B", "첫날은 작문, 언어, 인문이에요",
     "No dia 8, a prova tem... A. Natureza e Matemática · B. redação, Linguagens e Humanas · C. só redação", size=17, gap=0)
e.ex("B2", "객관식", "B", "13시 이후에 도착하면 못 들어가요",
     "Quem chega depois das 13h... A. entra atrasado · B. não entra · C. faz a prova no dia 15", size=17, gap=0)
e.ex("B2", "객관식", "B", "확인 카드에 시험 장소가 나와요",
     "O Cartão de Confirmação mostra... A. a nota · B. o local da prova · C. o gabarito", size=17, gap=0)
e.head("C · OS TEMPOS DO TEXTO", 25)
e.bridge("문장 뜻에 맞게 바른 동사 형태로 채우세요.")
e.ex("B2", "문장 완성", "começará", "미래형: começará",
     "No domingo, ___ (começar) a prova às 13h30.", instr="빈칸 채우기", size=17, gap=0)
e.ex("B2", "문장 완성", "chegar", "quem + 접속법 미래: chegar",
     "Quem ___ (chegar) depois das 13h não entra.", instr="빈칸 채우기", size=17, gap=0)
e.ex("B2", "문장 완성", "fecham", "현재형: fecham",
     "Os portões ___ (fechar) às 13h.", instr="빈칸 채우기", size=17, gap=0)
e.ex("B2", "문장 완성", "pede", "현재형: pede",
     "O Inep ___ (pedir) que cada um confira o local.", instr="빈칸 채우기", size=17, gap=0)
e.head("D · AS PALAVRAS DA PROVA", 25)
e.bridge("네모 안의 단어로 채우세요: portões · segunda chamada · local · conferir")
e.ex("B2", "문장 완성", "portões", "portões = 문",
     "Os ___ abrem às 12h.", instr="빈칸 채우기", size=17, gap=0)
e.ex("B2", "문장 완성", "segunda chamada", "segunda chamada = 재입장, 두 번째 입장",
     "Não há ___ no Enem.", instr="빈칸 채우기", size=17, gap=0)
e.ex("B2", "문장 완성", "local", "local = 장소",
     "Confira o ___ da sua prova.", instr="빈칸 채우기", size=17, gap=0)
e.ex("B2", "문장 완성", "Confira", "명령형: confira",
     "___ o cartão antes do domingo.", instr="빈칸 채우기", size=17, gap=0)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-aprofundamento.svg")
print("P6 saved, exercises so far:", len(REG))
