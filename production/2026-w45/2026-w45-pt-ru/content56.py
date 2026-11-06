# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-pt-ru/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · JOVENS (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JOVENS · Молодёжь", "A Lucerna", "NÍVEL B1 · A reta final dos jovens · Последний рывок молодёжи")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-main")
f.title("A reta final: revisar, descansar, fazer a prova", 37)
f.byline("Da redação da A Lucerna · Nível de leitura: B1")
f.para("A semana dos jovens brasileiros tem um centro: o domingo 8. Para os mais de 5 milhões de inscritos no Enem, é a reta final — a última semana de revisão antes da redação, de Linguagens e de Ciências Humanas.")
f.para("O plano da reta final cabe em cinco linhas: conferir o Cartão de Confirmação, revisar um pouco por dia, dormir bem na véspera, separar documento e caneta preta no dia anterior — e, no domingo, chegar cedo. Nada de maratona na véspera: quem dorme bem lembra melhor.")
f.para("E a semana tem mais: na terça, 3, as assembleias estaduais voltam do recesso; no sábado e no domingo, a Copa do Brasil decide os finalistas. O Brasil estuda de dia e torce à noite.")
f.para("No sábado, 31 de outubro, foi Halloween: a última festa antes da prova para muita gente. Agora é silêncio e revisão: o feriadão é para descansar o corpo e organizar a cabeça.")
f.box("O PLANO DA RETA FINAL", [
    ("1. Confira o Cartão de Confirmação do Enem (проверьте карточку подтверждения Enem)", "serif", False, INK, 21, 1.36),
    ("2. Revise um pouco por dia, sem maratona (повторяйте понемногу каждый день, без зубрёжки)", "serif", False, INK, 21, 1.36),
    ("3. Durma bem na véspera da prova (хорошо выспитесь накануне экзамена)", "serif", False, INK, 21, 1.36),
    ("4. Separe documento e caneta preta no dia anterior (заранее приготовьте документ и чёрную ручку)", "serif", False, INK, 21, 1.36),
    ("5. Domingo 8: chegue antes das 12h (в воскресенье 8-го: приходите до 12h)", "serif", False, INK, 21, 1.36),
])
f.gloss("a reta final = последний рывок · a véspera = канун · a maratona = ночная зубрёжка · separar = приготовить · a cabeça = голова, состояние.")
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
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Накануне важного экзамена ваш план — повторять или отдыхать? Напишите две фразы по-португальски и пришлите нам.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E VOCÊ? · А вы?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Накануне важного экзамена ваш план — повторять или отдыхать? Напишите две фразы по-португальски и пришлите нам.", 20, "sans", False, GREY, CW - 44, 1.42)
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
p.text(MX, ey + 28, "EXERCÍCIOS · Упражнения страницы 5", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Ответы на странице 8 · Уровни перемешаны — ищите по номеру задания", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · COMPREENSÃO", 25)
e.expl("Прочитайте статью на странице 5 и выберите правильный ответ.")
e.ex("B1", "Выбор ответа", "B", "Последний рывок заканчивается в воскресенье, 8 ноября",
     "A reta final termina... A. na segunda 2 · B. no domingo 8 · C. no dia 15", size=20, gap=8)
e.ex("B1", "Выбор ответа", "B", "Повторяйте понемногу каждый день",
     "O plano da reta final inclui... A. maratona na véspera · B. revisar um pouco por dia · C. chegar às 13h30", size=20, gap=8)
e.ex("B1", "Выбор ответа", "A", "Заранее приготовьте документ и чёрную ручку",
     "No dia anterior, o candidato separa... A. documento e caneta preta · B. só o celular · C. a roupa da festa", size=20, gap=8)
e.ex("B1", "Выбор ответа", "B", "День 2: естественные науки и математика",
     "O segundo dia do Enem (dia 15) tem... A. redação · B. Natureza e Matemática · C. só Linguagens", size=20, gap=8)
e.ex("B1", "Выбор ответа", "B", "Во вторник 3-го собрания штатов возвращаются с каникул",
     "Na terça, 3, ... A. é o Enem · B. as assembleias voltam do recesso · C. é a final da Copa", size=20, gap=8)
e.head("B · AS PALAVRAS DO TEXTO", 25)
e.expl("Заполните пропуски словами из рамки. Внимание: одно слово нужно поставить во множественное число.")
e.para("reta final · inscrito · véspera · maratona · local · separar", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "Вставьте слово", "reta final", "reta final = последний рывок",
     "A semana é a ___ dos estudos.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Вставьте слово", "inscritos", "inscrito во множественном числе: inscritos",
     "Mais de 5 milhões de estudantes estão ___ no Enem.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Вставьте слово", "véspera", "véspera = канун",
     "Na ___ da prova, durma bem.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Вставьте слово", "maratona", "maratona = ночная зубрёжка",
     "Nada de ___ na véspera.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Вставьте слово", "local", "local = место",
     "Confira o ___ da sua prova no cartão.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Вставьте слово", "Separe", "separar, повелительное наклонение: separe",
     "___ o documento no dia anterior.", instr="Вставьте", size=20, gap=8)
e.head("C · O FUTURO DO PRESENTE", 25)
e.expl("Дополните в будущем времени (futuro do presente).")
e.ex("B1", "Вставьте слово", "farão", "fazer, будущее время, неправильная форма eles: farão",
     "Os estudantes ___ (fazer) a prova no domingo.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Вставьте слово", "mostrará", "mostrar, будущее время: mostrará",
     "O cartão ___ (mostrar) o local da prova.", instr="Вставьте", size=20, gap=8)
e.ex("B2", "Вставьте слово", "sairão", "sair, будущее время, множественное число: sairão",
     "Os finalistas ___ (sair) dos jogos de volta.", instr="Вставьте", size=20, gap=8)
e.ex("B2", "Вставьте слово", "chegará", "chegar, будущее время: chegará",
     "Quem ___ (chegar) cedo não perde a prova.", instr="Вставьте", size=20, gap=8)
e.head("D · VERDADEIRO OU FALSO?", 25)
e.ex("B1", "Верно или нет", "Verdadeiro", "Карточка подтверждения показывает место экзамена",
     "O Cartão de Confirmação mostra o local da prova. Verdadeiro ou falso?", instr="Верно или нет?", size=20, gap=8)
e.ex("B1", "Верно или нет", "Falso", "Неверно: зубрёжка накануне — плохой план, лучше повторять понемногу каждый день",
     "A maratona na véspera é o melhor plano. Verdadeiro ou falso?", instr="Верно или нет?", size=20, gap=8)
e.ex("B2", "Верно или нет", "Verdadeiro", "Верно: с 13:30 до 19:00",
     "No domingo 8, a prova vai de 13h30 a 19h. Verdadeiro ou falso?", instr="Верно или нет?", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jovens.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · APROFUNDAMENTO (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("APROFUNDAMENTO · Разбор", "A Lucerna", "NÍVEL B2 · O Enem explicado · Enem: объяснение")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1520, tag="P6-main")
f.title("O Enem explicado: dois domingos, uma prova", 37)
f.byline("Da redação da A Lucerna · Nível de leitura: B2")
f.para("O Enem 2026 tem dois domingos: 8 e 15 de novembro. No dia 8, o primeiro: redação, Linguagens e Ciências Humanas, das 13h30 às 19h — cinco horas e meia. No dia 15, o segundo: Ciências da Natureza e Matemática. Esta edição cobre o dia 8; o dia 15 é a prévia da próxima semana.")
f.para("O ritual do domingo 8 começa ao meio-dia: os portões abrem às 12h e fecham às 13h, no horário de Brasília. Quem chega depois das 13h não entra — não há segunda chamada. Leve documento com foto, caneta preta e o Cartão de Confirmação: ele mostra o seu local de prova.")
f.para("Mais de 5 milhões de estudantes estão inscritos. É muita gente para o mesmo horário: por isso o Inep pede que cada um confira o local antes do domingo. Quem confere antes não se perde no dia.")
f.para("E os números do domingo? Cinco horas e meia são 330 minutos: 60 minutos para cada hora, mais 30. É tempo para ler com calma, escrever a redação e revisar — sem correria. A regra de ouro do Enem: primeiro as fáceis, depois as difíceis, e a redação com tempo guardado.")
f.gloss("os portões = ворота · a segunda chamada = пересдача, повторный вход · conferir = проверять · a correria = спешка.")
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
p.text(MX, gy + 10, "O DOMINGO 8 EM NÚMEROS · Цифры воскресенья 8-го (официальное время Inep)", 26, "sans", True, OLIVE)
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
p.text(MX, ey + 28, "EXERCÍCIOS · Упражнения страницы 6", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Ответы на странице 8 · Уровни перемешаны — ищите по номеру задания", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · LER OS GRÁFICOS", 25)
e.expl("Посмотрите на две диаграммы выше и выберите правильный ответ.")
e.ex("B2", "Выбор ответа", "B", "Ворота открыты 60 минут",
     "No relógio do domingo, os portões ficam abertos... A. 30 minutos · B. 60 minutos · C. 330 minutos", size=17, gap=0)
e.ex("B2", "Выбор ответа", "A", "Между закрытием и началом экзамена — 30 минут ожидания",
     "A espera entre o fechamento e a prova é de... A. 30 minutos · B. 60 minutos · C. 330 minutos", size=17, gap=0)
e.ex("B2", "Выбор ответа", "B", "Экзамен длится 330 минут",
     "A prova dura... A. 60 minutos · B. 330 minutos · C. 420 minutos", size=17, gap=0)
e.ex("B2", "Выбор ответа", "B", "60 + 30 + 330 = 420",
     "60 + 30 + 330 = ... A. 390 · B. 420 · C. 360", size=17, gap=0)
e.ex("B2", "Выбор ответа", "C", "С полудня до 19h = 7 часов",
     "Do meio-dia às 19h são... A. 5h30 · B. 6h · C. 7h", size=17, gap=0)
e.ex("B2", "Выбор ответа", "A", "Цифры диаграммы — официальное время Inep",
     "Os números do gráfico são... A. horários oficiais do Inep · B. uma pesquisa eleitoral · C. buscas no Google", size=17, gap=0)
e.head("B · COMPREENSÃO", 25)
e.ex("B2", "Выбор ответа", "B", "Enem проходит в два воскресенья: 8-го и 15-го",
     "O Enem tem... A. um só domingo · B. dois domingos: 8 e 15 · C. três domingos", size=17, gap=0)
e.ex("B2", "Выбор ответа", "B", "День 1: сочинение, языки и гуманитарные науки",
     "No dia 8, a prova tem... A. Natureza e Matemática · B. redação, Linguagens e Humanas · C. só redação", size=17, gap=0)
e.ex("B2", "Выбор ответа", "B", "Пришедших после 13h не пускают",
     "Quem chega depois das 13h... A. entra atrasado · B. não entra · C. faz a prova no dia 15", size=17, gap=0)
e.ex("B2", "Выбор ответа", "B", "Карточка подтверждения показывает место экзамена",
     "O Cartão de Confirmação mostra... A. a nota · B. o local da prova · C. o gabarito", size=17, gap=0)
e.head("C · OS TEMPOS DO TEXTO", 25)
e.expl("Вставьте правильную форму глагола по смыслу предложения.")
e.ex("B2", "Вставьте слово", "começará", "будущее время: começará",
     "No domingo, ___ (começar) a prova às 13h30.", instr="Вставьте", size=17, gap=0)
e.ex("B2", "Вставьте слово", "chegar", "quem + будущее сослагательное: chegar",
     "Quem ___ (chegar) depois das 13h não entra.", instr="Вставьте", size=17, gap=0)
e.ex("B2", "Вставьте слово", "fecham", "настоящее время: fecham",
     "Os portões ___ (fechar) às 13h.", instr="Вставьте", size=17, gap=0)
e.ex("B2", "Вставьте слово", "pede", "настоящее время: pede",
     "O Inep ___ (pedir) que cada um confira o local.", instr="Вставьте", size=17, gap=0)
e.head("D · AS PALAVRAS DA PROVA", 25)
e.expl("Заполните пропуски словами из рамки: portões · segunda chamada · local · conferir")
e.ex("B2", "Вставьте слово", "portões", "portões = ворота",
     "Os ___ abrem às 12h.", instr="Вставьте", size=17, gap=0)
e.ex("B2", "Вставьте слово", "segunda chamada", "segunda chamada = пересдача, повторный вход",
     "Não há ___ no Enem.", instr="Вставьте", size=17, gap=0)
e.ex("B2", "Вставьте слово", "local", "local = место",
     "Confira o ___ da sua prova.", instr="Вставьте", size=17, gap=0)
e.ex("B2", "Вставьте слово", "Confira", "повелительное наклонение: confira",
     "___ o cartão antes do domingo.", instr="Вставьте", size=17, gap=0)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-aprofundamento.svg")
print("P6 saved, exercises so far:", len(REG))
