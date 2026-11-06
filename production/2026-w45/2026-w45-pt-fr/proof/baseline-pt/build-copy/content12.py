# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/pt-fr-proof/baseline-pt/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · CAPA (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 2 · SEGUNDA EDIÇÃO", 23, "sans", True, OLIVE)
p.text(975, 92, "TODA SEMANA EM PORTUGUÊS · 每周一期 · 读巴西人正在读的葡萄牙语", 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "SEMANA DE 2 A 8 DE NOVEMBRO DE 2026", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, GOLD, 1.6)
p.text(975, 262, "A Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "葡 萄 牙 语 周 报 · VOL.2 · A SEMANA DO ENEM · FINADOS · O FUTEBOL DECIDE", 40, "serif", True, INK, anchor="middle")
p.text(975, 372, "O JORNAL SEMANAL PARA APRENDER — O BRASIL DE VERDADE, EM PORTUGUÊS, DO BRASIL", 19, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)

# band
p.rect(MX, 424, RIGHT - MX, 118, fill=DARK)
p.text(MX + 30, 478, "A SEMANA DO ENEM!", 36, "sans", True, "#f3edda")
p.text(MX + 30, 522, "De segunda a domingo, o Brasil revisa, descansa e faz a prova.", 23, "serif", False, "#e8dfc8")
p.text(RIGHT - 30, 478, "全国高考周", 24, "sans", True, "#b3a06a", anchor="end")
p.text(RIGHT - 30, 522, "11 月 2 日亡灵节连休 · 11 月 8 日高考第一天", 21, "sans", False, "#b3a06a", anchor="end")

# ---- headline (span cols 0-2) ----
hy = 580
p.text(MX, hy + 26, "A NOTÍCIA · 头条", 22, "sans", True, BRICK)
hy = p.para(MX, hy + 92, "Do feriadão à prova: a semana do Enem", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 28, "Da redação da A Lucerna · Nível de leitura: A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Começa na segunda-feira, 2 de novembro, feriado de Finados, e termina no domingo, 8 de novembro, com o primeiro dia do Enem. Entre um dia e outro, o país inteiro vive a mesma semana: descansar, revisar e fazer a prova.", size=24)
f.para("O feriadão abre a semana: sábado, 31 de outubro, domingo, 1º de novembro, e segunda-feira, 2, feriado nacional. Muita gente viaja, visita a família e vai ao cemitério levar flores. Para quem faz o Enem, o feriadão é também um fim de semana de revisão: um pouco por dia, sem maratona.", size=24)
f.para("No domingo, 8 de novembro, é o primeiro dia do Enem 2026. Os portões abrem às 12h e fecham às 13h, no horário de Brasília. A prova começa às 13h30 e vai até as 19h: são cinco horas e meia de redação, Linguagens e Ciências Humanas. Mais de 5 milhões de estudantes estão inscritos.", size=24)
f.para("E o futebol não para: a rodada 34 do Brasileirão tem jogo de segunda a sexta, e as semifinais da Copa do Brasil se decidem no fim de semana — sábado, Atlético-MG × Grêmio, e domingo, Vasco × Palmeiras (página 4). O sábado, 31, foi de Halloween, e o domingo, 1º, teve os jogos de ida da Copa do Brasil.", size=24)
f.para("Esta é a segunda edição da A Lucerna em português: toda semana, o Brasil de verdade, com clareza e honestidade. Boa prova — e boa leitura!", size=24)
f.bridge("讲解｜feriadão 连休长周末 · o portão 大门 · a redação 作文 · revisar 复习。")
f.box("A SEMANA EM NÚMEROS · 数字", [
    ("12h — os portões abrem no domingo 8（周日 12 点开门）", "serif", False, INK, 20, 1.35),
    ("13h — os portões fecham（13 点关门，过时不入）", "serif", False, INK, 20, 1.35),
    ("13h30–19h — a prova do dia 8（考试 13:30 至 19:00）", "serif", False, INK, 20, 1.35),
    ("5h30 — a duração da prova do dia 8（考试时长 5 小时半）", "serif", False, INK, 20, 1.35),
])
f.head("AGORA VOCÊ · 即学即练", 25)
f.ex("A2", "完成句子", "feriadão", "feriadão = 连休长周末",
     "A semana começa com o ___ de Finados.", size=19.5, gap=6)
f.ex("A2", "完成句子", "portões", "portões = 大门（考场大门）",
     "No domingo 8, os ___ abrem às 12h.", size=19.5, gap=6)
f.ex("A2", "完成句子", "redação", "redação = 作文",
     "A prova do dia 8 tem ___, Linguagens e Ciências Humanas.", size=19.5, gap=6)
f.ex("A2", "完成句子", "13h30", "13h30 开考（巴西利亚时间）",
     "A prova começa às ___.", size=19.5, gap=6)
f.ex("A2", "完成句子", "19h", "19h 结束",
     "A prova vai até as ___.", size=19.5, gap=6)
f.ex("B1", "完成句子", "revisam", "revisar 现在时 eles 形式：revisam",
     "Os estudantes ___ (revisar) um pouco por dia.", size=19.5, gap=6)
f.end_report()

# ---- os horários do domingo 8 (col 3) ----
gx, gw = COLX[3], CW
gy = 580
p.rect(gx, gy, gw, 700, fill=BOX, stroke=LINE, sw=1.4)
p.text(gx + 22, gy + 40, "OS HORÁRIOS", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "DO DOMINGO 8", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Enem, dia 8 · horário de Brasília", 19, "sans", False, GREY)
hor = [
    ("12h", "os portões abrem"),
    ("13h", "os portões fecham"),
    ("13h30", "a prova começa"),
    ("19h", "a prova termina"),
]
byy = gy + 150
for t, lab in hor:
    p.text(gx + 22, byy + 28, t, 30, "serif", True, OLIVE)
    p.text(gx + 150, byy + 28, lab, 21.5, "serif", False, INK)
    byy += 92
p.text(gx + 22, byy + 16, "Chegue cedo: depois das 13h,", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "ninguém mais entra.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 76, "迟到不得入内：13 点后关门", 19, "sans", False, GREY)

# ---- conteúdo (col 3) ----
sy = 1312
p.rect(gx, sy, gw, 340, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(gx + 22, sy + 40, "NESTA EDIÇÃO · 本期目录", 24, "sans", True, OLIVE)
som = [
    ("Pág. 2", "O feriadão e a revisão", "A2"),
    ("Pág. 3", "Finados, o dia da memória", "A2→B1"),
    ("Pág. 4", "O futebol decide", "B1"),
    ("Pág. 5", "A reta final dos jovens", "B1"),
    ("Pág. 6", "O Enem explicado", "B2"),
    ("Pág. 7", "Frases da semana", "A2→B2"),
    ("Pág. 8", "Exercícios e respostas", "todos"),
]
yy = sy + 84
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, BRICK)
    p.text(gx + 88, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 40

# ---- palavra da semana (col 3) ----
my = 1652
p.text(gx, my + 24, "A PALAVRA DA SEMANA", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, GOLD, 2)
y2 = p.para(gx, my + 76, "« feriadão » : um feriado grudado no fim de semana — três dias.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, y2 + 28, "“连休”：假期连着周末，一共三天。", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "estudo.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "Estudantes em uma biblioteca: para os mais de 5 milhões de inscritos no Enem, o feriadão é um fim de semana de revisão — um pouco por dia, sem maratona. (Página 5)",
        "Foto: Gary Todd / Wikimedia Commons — CC0")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2290, tag="P1-tv")
f2.head("A SEMANA EM DOIS DOMINGOS", 25)
f2.para("Domingo 1º: os jogos de ida da Copa do Brasil. Domingo 8: o primeiro dia do Enem. Entre um domingo e outro, o Brasil revisa, descansa e joga.", 22.5)
f2.para("No sábado, 31 de outubro, foi Halloween: festas à fantasia em todo o país — e, para os candidatos, a última festa antes da prova.", 22.5)
f2.end_report()
# col 3 EM POUCAS PALAVRAS
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 1914, "EM POUCAS PALAVRAS · 快讯", 24, "sans", True, OLIVE)
brefs = [
    ("O FERIADÃO", "Segunda, 2: Finados, feriado nacional — feriadão de 31 a 2. (Página 2)"),
    ("O ENEM", "Domingo, 8: primeiro dia — redação, Linguagens e Humanas. (Página 6)"),
    ("O FUTEBOL", "Sábado e domingo: os jogos de volta da Copa do Brasil decidem os finalistas. (Página 4)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, BRICK)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- quiz relâmpago ----
qy = 2312
p.hline(MX, RIGHT, qy, GOLD, 2)
p.text(MX, qy + 36, "QUIZ RELÂMPAGO · 闪电问答", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "读头版，选出正确答案 · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", "单选", "B", "连休从 10 月 31 日到 11 月 2 日",
      "O feriadão vai... A. de 2 a 4 de novembro · B. de 31 de outubro a 2 de novembro · C. de 8 a 15 de novembro", size=21)
qf.ex("A2", "单选", "B", "13 点关门",
      "Os portões do Enem fecham às... A. 12h · B. 13h · C. 13h30", size=21)
qf.ex("A2", "单选", "C", "第 1 天考作文、语言与人文",
      "No dia 8, a prova tem... A. só Matemática · B. só redação · C. redação, Linguagens e Ciências Humanas", size=21)
qf.ex("A2", "单选", "B", "次回合在 7 日和 8 日",
      "Os jogos de volta da Copa do Brasil são... A. no dia 1º · B. nos dias 7 e 8 · C. no dia 15", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-capa.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · VIDA (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("VIDA · 生活", "A Lucerna", "NÍVEL A2 · Finados e revisão: o feriadão do Brasil")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("Finados e revisão: o feriadão do Brasil", 37)
f.byline("Da redação da A Lucerna · Nível de leitura: A2")
f.para("Segunda-feira, 2 de novembro, é Finados, feriado nacional. Com o sábado, 31, e o domingo, 1º, o país ganha um feriadão de três dias: muita gente viaja para ver a família, e muita gente fica em casa para descansar.")
f.para("Finados é o dia da memória: famílias visitam os cemitérios, levam flores — sobretudo crisântemos —, acendem velas e participam de missas. É um dia calmo, de lembrança e de encontro: os vivos cuidam do lugar dos mortos, e as histórias voltam à mesa.")
f.para("Para os candidatos do Enem, o feriadão tem outro nome: revisão. O plano da semana é simples — revisar um pouco por dia, dormir bem e conferir o Cartão de Confirmação, o documento que mostra o local da prova. Quem confere antes não se perde no dia.")
f.para("E atenção ao relógio do domingo 8: os portões abrem às 12h e fecham às 13h. Chegue cedo, leve documento com foto e caneta preta, e desligue o celular. A prova é longa — cinco horas e meia — e começa às 13h30.")
f.para("No Brasil, não há horário de verão desde 2019: ninguém muda o relógio nesta semana. O horário do Enem é o de Brasília — confira o fuso da sua cidade.")
f.head("E SE EU CHEGAR TARDE?", 25)
f.para("Se você chegar depois das 13h, os portões já fecharam — e não há segunda chamada. Por isso o plano é sair cedo: o domingo 8 não aceita atraso. Melhor chegar cedo e esperar do que correr no último minuto.", 23.5)
f.box("PARA NÃO ERRAR · 口诀", [
    ("«Confira o cartão, durma bem, chegue cedo.» Três passos e o domingo fica tranquilo: o resto é com a prova.", "serif", False, INK, 21.5, 1.4),
])
f.gloss("o feriadão 连休长周末 · o cemitério 墓园 · a vela 蜡烛 · o crisântemo 菊花 · a missa 弥撒 · conferir 核对。")
f.end_report()

# col 3: facts + e você? (sequential, measured)
ix = COLX[3]
facts = ["O feriadão vai de sábado, 31 de outubro, a segunda, 2 de novembro.",
         "Finados: visitas aos cemitérios, flores, velas e missas.",
         "Domingo 8: portões 12h–13h, prova 13h30–19h, horário de Brasília."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "VOCÊ SABIA?", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E você? No seu país, há um dia de lembrar os mortos? O que as famílias fazem nesse dia? Escreva duas frases em português e mande para a redação: as melhores saem na página 7, «Cartas dos leitores»."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("在你的国家，有纪念逝者的日子吗？那天家人们做什么？写两句寄来。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E VOCÊ? · 说说你自己", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "在你的国家，有纪念逝者的日子吗？那天家人们做什么？写两句寄来。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- Os horários do domingo 8: 4 time boxes ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, GOLD, 2)
p.text(MX, dy + 28, "OS HORÁRIOS DO DOMINGO 8 · 周日时间表", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "Um país, vários relógios · 一个国家，几个时区", 20, "sans", False, GREY, anchor="end")
times = [
    ("12h", "os portões abrem", "周日 12 点开门"),
    ("13h", "os portões fecham", "13 点关门"),
    ("13h30", "a prova começa", "13:30 开考"),
    ("19h", "a prova termina", "19:00 结束"),
]
for i, (t, lab, cn) in enumerate(times):
    bx = COLX[i]
    p.rect(bx, dy + 52, CW, 150, fill=BOX, stroke=LINE, sw=1.4)
    p.text(bx + 22, dy + 116, t, 40, "serif", True, OLIVE)
    yy = p.para(bx + 152, dy + 92, lab, 21.5, "serif", False, INK, CW - 174, 1.36)
    p.para(bx + 152, yy + 20, cn, 19, "sans", False, GREY, CW - 174, 1.3)
p.para(MX, dy + 234, "Atenção: o horário é o de Brasília. Quem faz a prova em outro fuso deve conferir a hora local: o portão fecha às 13h de Brasília, e não há atraso.", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P2 exercises ----
ey = dy + 282
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EXERCÍCIOS · 第 2 版练习", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案见第 8 版 · 题目可跨级混排，按题号找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A · COMPREENSÃO", 25)
e.bridge("读第 2 版文章，选出正确答案。")
e.ex("A2", "单选", "B", "连休从 10 月 31 日到 11 月 2 日",
     "O feriadão vai... A. de 2 a 5 de novembro · B. de 31 de outubro a 2 de novembro · C. de 8 a 15 de novembro", size=20, gap=8)
e.ex("A2", "单选", "B", "亡灵节家人们去墓园献花",
     "Em Finados, as famílias... A. compram presentes de Natal · B. visitam os cemitérios e levam flores · C. votam para presidente", size=20, gap=8)
e.ex("A2", "单选", "B", "确认卡显示考试地点",
     "O Cartão de Confirmação mostra... A. a nota do aluno · B. o local da prova · C. o resultado final", size=20, gap=8)
e.ex("A2", "单选", "B", "13 点关门",
     "Os portões fecham às... A. 12h · B. 13h · C. 19h", size=20, gap=8)
e.ex("A2", "单选", "A", "巴西没有夏令时，钟表不动",
     "Nesta semana, o relógio no Brasil... A. não muda · B. volta uma hora · C. avança uma hora", size=20, gap=8)
e.head("B · O PRESENTE", 25)
e.bridge("补全动词的现在时形式。")
e.ex("A2", "完成句子", "confere", "conferir：ele → confere",
     "O candidato ___ (conferir) o cartão.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "abre", "abrir：ele → abre",
     "O portão ___ (abrir) às 12h.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "levamos", "levar：nós → levamos",
     "Nós ___ (levar) documento com foto.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "começa", "começar：ela → começa",
     "A prova ___ (começar) às 13h30.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "é", "ser 现在时 ela 形式：é",
     "A missa de Finados ___ (ser) um momento calmo.", instr="填空", size=20, gap=8)
e.head("C · COMPLETE COM OS NÚMEROS", 25)
e.bridge("用第 1、2 版的数字填空。")
e.ex("A2", "完成句子", "1", "12 点到 13 点 = 1 小时",
     "Os portões ficam abertos ___ hora.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "5", "13:30 至 19:00 = 5 个半小时",
     "A prova dura ___ horas e meia.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "330", "5×60 + 30 = 330 分钟",
     "De 13h30 a 19h são ___ minutos.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "3", "31 日、1 日、2 日 = 3 天",
     "O feriadão tem ___ dias.", instr="填空", size=20, gap=8)
e.head("D · AS PALAVRAS", 25)
e.match_set("A2", "词汇配对",
            ["o feriadão", "o cemitério", "a vela", "o crisântemo"],
            ["a flor que as famílias levam a Finados",
             "o lugar onde ficam os túmulos",
             "um feriado grudado no fim de semana",
             "o objeto que dá luz e se acende em memória"],
            ["c", "b", "d", "a"],
            ["feriadão=连着周末的假期 c", "cemitério=墓碑所在的地方 b", "vela=点亮纪念的物品 d", "crisântemo=亡灵节带去的花 a"],
            instr="把词和释义配对")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-vida.svg")
print("P2 saved, exercises so far:", len(REG))
