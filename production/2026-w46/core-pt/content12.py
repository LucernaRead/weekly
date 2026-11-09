# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · CAPA (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 3　TERCEIRA EDIÇÃO", 17, "sans", True, OLIVE, spacing=1.7)
p.text(975, 92, "TODA SEMANA EM PORTUGUÊS　每周一期　读巴西人正在读的葡萄牙语", 17, "sans", False, GREY, anchor="middle", spacing=1.7)
p.text(RIGHT, 92, "SEMANA DE 9 A 15 DE NOVEMBRO DE 2026", 17, "sans", False, GREY, anchor="end", spacing=1.7)
p.text(975, 262, "A Lucerna", 196, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "葡萄牙语周报　VOL.3　ENEM, DIA 2　PROCLAMAÇÃO DA REPÚBLICA　O FUTEBOL DECIDE", 34, "serif", True, OLIVE, anchor="middle", spacing=0)
p.text(975, 372, "O JORNAL SEMANAL PARA APRENDER — O BRASIL DE VERDADE, EM PORTUGUÊS, DO BRASIL", 16, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)

# band
p.rect(MX, 470, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 30, 524, "O SEGUNDO DOMINGO!", 46, "sans", True, ONCLOTH)
p.text(MX + 30, 568, "Domingo, 15 de novembro: a prova e o feriado chegam juntos.", 25, "serif", False, "#cac8ba")
p.text(RIGHT - 30, 524, "高考第二天", 27, "sans", True, GOOSE, anchor="end")
p.text(RIGHT - 30, 568, "11月15日第二场考试　共和国宣言日假期", 18, "sans", False, GOOSE, anchor="end")

# ---- headline (span cols 0-2) ----
hy = 590
p.text(MX, hy + 26, "A NOTÍCIA　头条", 17, "sans", True, OLIVE)
hy = p.para(MX, hy + 92, "Dois domingos, um feriado: o Brasil faz o segundo dia do Enem", 53, "serif", True, INK, 1323, 1.06)
p.text(MX, hy + 28, "Da redação da A Lucerna　Nível de leitura: A2", 17, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Domingo, 15 de novembro, é o segundo dia do Enem 2026 — e é também o feriado da Proclamação da República. A prova e o feriado chegam no mesmo dia: de manhã, o país acorda para a história; à tarde, mais de 5 milhões de estudantes fazem Ciências da Natureza e Matemática.", size=24)
f.para("Os portões abrem às 12h e fecham às 13h, no horário de Brasília. A prova começa às 13h30 e termina às 18h30: são cinco horas para 90 questões — 45 de Natureza e 45 de Matemática. No primeiro dia, 8 de novembro, foram redação, Linguagens e Ciências Humanas, até as 19h.", size=24)
f.para("A Proclamação da República completa 137 anos: em 15 de novembro de 1889, o marechal Deodoro da Fonseca pôs fim à monarquia e o Brasil virou república. O feriado é nacional, mas cai num domingo — e domingo não dá folga extra na segunda-feira (página 3).", size=24)
f.para("E o futebol decide: as semifinais da Copa do Brasil se resolvem neste fim de semana — sábado, 7, às 18h, Atlético-MG × Grêmio, na Arena MRV; domingo, 8, às 17h, Vasco × Palmeiras, em São Januário. Na ida, no dia 1º, o Grêmio venceu por 2 a 0 e o Palmeiras venceu por 1 a 0. Os finalistas saem na próxima edição (página 4).", size=24)
f.para("Esta é a terceira edição da A Lucerna em português: toda semana, o Brasil de verdade, com clareza e honestidade. Boa prova — e boa leitura!", size=24)
f.bridge("讲解｜a proclamação 宣布、宣告 · o feriado 假日 · a natureza 自然科学 · a matemática 数学。")
f.box("A SEMANA EM NÚMEROS　数字", [
    ("12h — os portões abrem no domingo 15（周日 12 点开门）", "serif", False, INK, 20, 1.35),
    ("13h — os portões fecham（13 点关门，过时不入）", "serif", False, INK, 20, 1.35),
    ("13h30–18h30 — a prova do dia 15（考试 13:30 至 18:30）", "serif", False, INK, 20, 1.35),
    ("90 — as questões do dia 15: 45 + 45（90 道题：45 + 45）", "serif", False, INK, 20, 1.35),
])
f.head("AGORA VOCÊ　即学即练", 25)
f.ex("A2", "完成句子", "proclamação", "proclamação = 宣布（共和国宣言）",
     "A ___ da República é no dia 15.", size=19.5, gap=6)
f.ex("A2", "完成句子", "feriado", "feriado = 假日",
     "O dia 15 é ___ nacional.", size=19.5, gap=6)
f.ex("A2", "完成句子", "portões", "portões = 大门（考场大门）",
     "No domingo 15, os ___ abrem às 12h.", size=19.5, gap=6)
f.ex("A2", "完成句子", "18h30", "18h30 结束",
     "A prova vai até as ___.", size=19.5, gap=6)
f.ex("A2", "完成句子", "90", "90 道题",
     "O dia 15 tem ___ questões.", size=19.5, gap=6)
f.ex("B1", "完成句子", "fazem", "fazer 现在时 eles 形式：fazem",
     "Os estudantes ___ (fazer) a prova no domingo.", size=19.5, gap=6)
f.end_report()

# ---- os horários do domingo 15 (col 3) ----
gx, gw = COLX[3], CW
gy = 588
p.rect(gx, gy, gw, 700, fill=BOX)
p.text(gx + 22, gy + 40, "OS HORÁRIOS", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "DO DOMINGO 15", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Enem, dia 15　horário de Brasília", 19, "sans", False, GREY)
hor = [
    ("12h", "os portões abrem"),
    ("13h", "os portões fecham"),
    ("13h30", "a prova começa"),
    ("18h30", "a prova termina"),
]
byy = gy + 150
for t, lab in hor:
    p.text(gx + 22, byy + 28, t, 30, "serif", True, OLIVE)
    p.text(gx + 150, byy + 28, lab, 21.5, "serif", False, INK)
    byy += 92
p.text(gx + 22, byy + 16, "Chegue cedo: depois das 13h,", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "ninguém mais entra.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 76, "迟到不得入内：13点后关门", 19, "sans", False, GREY)

# ---- conteúdo (col 3) ----
sy = 1312
p.rect(gx, sy, gw, 340, fill="#f0eee5")
p.text(gx + 22, sy + 40, "NESTA EDIÇÃO　本期目录", 24, "sans", True, OLIVE)
som = [
    ("Pág. 2", "Prova e feriado no domingo", "A2"),
    ("Pág. 3", "Proclamação: 137 anos", "A2→B1"),
    ("Pág. 4", "O futebol decide", "B1"),
    ("Pág. 5", "A semana dos jovens", "B1"),
    ("Pág. 6", "O domingo explicado", "B2"),
    ("Pág. 7", "Frases da semana", "A2→B2"),
    ("Pág. 8", "Exercícios e respostas", "todos"),
]
yy = sy + 84
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, OLIVE)
    p.text(gx + 88, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 40

# ---- palavra da semana (col 3) ----
my = 1652
p.text(gx, my + 24, "A PALAVRA DA SEMANA", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, OLIVE, 2)
p.text(gx, my + 76, "« proclamação »", 21.5, "serif", False, INK, italic=True)
wy = p.para(gx, my + 108, "o ato de anunciar uma mudança — em 1889, o fim da monarquia.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, wy + 10, "proclamação = 宣布（共和国宣言）。", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "estudo.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "Estudantes em uma biblioteca: no domingo 15, os mais de 5 milhões de inscritos no Enem fazem o segundo dia — Natureza e Matemática, das 13h30 às 18h30. (Página 6)",
        "Foto: Gary Todd / Wikimedia Commons — CC0")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2300, tag="P1-tv")
f2.head("DOIS FINS DE SEMANA", 25)
f2.para("Fim de semana 7–8: as voltas da Copa e o Grande Prêmio de São Paulo, em Interlagos — 71 voltas, sem sprint. Fim de semana 14–15: a Seleção no sábado e o Enem no domingo.", 21.5)
f2.para("Sábado, 14: Brasil × Japão às 7h15; Mirassol × Atlético às 18h30.", 21.5)
f2.end_report()
# col 3 EM POUCAS PALAVRAS
bx = COLX[3]
p.rect(bx, 1874, CW, 436, fill=BOX)
p.text(bx + 22, 1914, "EM POUCAS PALAVRAS　快讯", 24, "sans", True, OLIVE)
brefs = [
    ("O ENEM", "Domingo, 15: segundo dia — Natureza e Matemática, das 13h30 às 18h30. (Página 6)"),
    ("O FERIADO", "Domingo, 15: Proclamação da República, 137 anos — cai no domingo, sem folga extra. (Página 3)"),
    ("O FUTEBOL", "Sábado e domingo: as voltas da Copa do Brasil decidem os finalistas. (Página 4)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, OLIVE)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- quiz relâmpago ----
qy = 2312
p.hline(MX, RIGHT, qy, OLIVE, 2)
p.text(MX, qy + 36, "QUIZ RELÂMPAGO　闪电问答", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "读头版，选出正确答案　答案见第8版", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2560, tag="P1-quiz")
qf.ex("A2", "单选", "C", "共和国宣言日在 11 月 15 日",
      "A Proclamação da República é... A. no dia 8 · B. no dia 20 · C. no dia 15", size=21)
qf.ex("A2", "单选", "B", "13 点关门",
      "Os portões do Enem fecham às... A. 12h · B. 13h · C. 13h30", size=21)
qf.ex("A2", "单选", "C", "第 2 天考自然科学与数学",
      "No dia 15, a prova tem... A. redação · B. Linguagens e Humanas · C. Natureza e Matemática", size=21)
qf.ex("A2", "单选", "A", "18:30 结束",
      "No dia 15, a prova termina às... A. 18h30 · B. 19h · C. 12h", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-capa.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · VIDA (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("VIDA　生活", "A Lucerna", "NÍVEL A2　Prova e feriado no mesmo domingo")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("15 de novembro: prova e feriado no mesmo domingo", 32)
f.byline("Da redação da A Lucerna　Nível de leitura: A2")
f.para("Domingo, 15 de novembro, é um dia duplo no Brasil: é feriado nacional — a Proclamação da República — e é o segundo dia do Enem. Para quem faz a prova, o feriado não muda o relógio: os portões abrem às 12h e fecham às 13h, no horário de Brasília.")
f.para("O segundo dia tem 90 questões: 45 de Ciências da Natureza — biologia, física e química — e 45 de Matemática. São cinco horas de prova, das 13h30 às 18h30, meia hora a menos do que no primeiro dia. A dica é a mesma: chegue cedo, leve documento com foto e caneta preta, e desligue o celular.")
f.para("E o feriado? A Proclamação completa 137 anos e cai num domingo. Quem trabalha de segunda a sexta não ganha folga extra — a lei não transfere o feriado para a segunda-feira. Para quem tem escala no domingo, valem as regras do trabalho em feriado.")
f.para("No Brasil, não há horário de verão desde 2019: ninguém muda o relógio nesta semana. O horário do Enem é o de Brasília — confira o fuso da sua cidade. E confira o transporte: no feriado, ônibus e trens podem rodar em horário reduzido.")
f.para("A semana também é de Novembro Azul, a campanha de prevenção do câncer de próstata, e de promoções: no dia 11, o 11.11 abre a temporada de ofertas, antes da Black Friday, no dia 27.")
f.head("E SE EU CHEGAR TARDE?", 25)
f.para("Se você chegar depois das 13h, os portões já fecharam — e não há segunda chamada. O domingo 15 não aceita atraso: melhor chegar cedo e esperar do que correr no último minuto. E lembre: no segundo dia, a prova termina às 18h30, não às 19h.", 23.5)
f.box("PARA NÃO ERRAR　口诀", [
    ("«Confira o cartão, durma bem, chegue cedo.» Três passos e o domingo fica tranquilo: no feriado, confira também o transporte.", "serif", False, INK, 21.5, 1.4),
])
f.gloss("a proclamação 宣布 · o feriado 假日 · a natureza 自然科学 · a matemática 数学 · conferir 核对 · a escala 排班。")
f.end_report()

# col 3: facts + e você? (sequential, measured)
ix = COLX[3]
facts = ["O segundo dia do Enem é no domingo 15: Natureza e Matemática, 13h30–18h30.",
         "O feriado da Proclamação cai num domingo — sem folga extra na segunda.",
         "11.11: o dia das promoções abre a temporada da Black Friday (27)."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 38
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "VOCÊ SABIA?", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E você? No seu país, um feriado que cai no domingo dá folga na segunda? Escreva duas frases em português e mande para a redação: as melhores saem na página 7, «Cartas dos leitores»."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("在你的国家，落在周日的假日会在周一补休吗？写两句寄来。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E VOCÊ?　说说你自己", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "在你的国家，落在周日的假日会在周一补休吗？写两句寄来。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- Os horários do domingo 15: 4 time boxes ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, OLIVE, 2)
p.text(MX, dy + 28, "OS HORÁRIOS DO DOMINGO 15　周日时间表", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "Um país, vários relógios　一个国家，几个时区", 20, "sans", False, GREY, anchor="end")
times = [
    ("12h", "os portões abrem", "周日 12 点开门"),
    ("13h", "os portões fecham", "13 点关门"),
    ("13h30", "a prova começa", "13:30 开考"),
    ("18h30", "a prova termina", "18:30 结束"),
]
for i, (t, lab, cn) in enumerate(times):
    bx = COLX[i]
    p.rect(bx, dy + 52, CW, 150, fill=BOX)
    p.text(bx + 22, dy + 116, t, 40, "serif", True, OLIVE)
    yy = p.para(bx + 152, dy + 92, lab, 21.5, "serif", False, INK, CW - 174, 1.36)
    p.para(bx + 152, yy + 20, cn, 19, "sans", False, GREY, CW - 174, 1.3)
p.para(MX, dy + 234, "Atenção: o horário é o de Brasília. Quem faz a prova em outro fuso deve conferir a hora local: o portão fecha às 13h de Brasília, e não há atraso.", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P2 exercises ----
ey = dy + 282
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EXERCÍCIOS　第2版练习", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案见第8版　题目可跨级混排，按题号找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A　COMPREENSÃO", 25)
e.bridge("读第 2 版文章，选出正确答案。")
e.ex("A2", "单选", "B", "第 2 天考自然科学与数学",
     "No dia 15, a prova tem... A. redação · B. Natureza e Matemática · C. só Linguagens", size=20, gap=8)
e.ex("A2", "单选", "B", "假日落在周日，周一不补休",
     "O feriado de 15 de novembro... A. dá folga na segunda · B. cai num domingo, sem folga extra · C. muda o relógio", size=20, gap=8)
e.ex("A2", "单选", "B", "确认卡显示考试地点",
     "O Cartão de Confirmação mostra... A. a nota do aluno · B. o local da prova · C. o resultado final", size=20, gap=8)
e.ex("A2", "单选", "B", "18:30 结束",
     "No dia 15, a prova termina às... A. 19h · B. 18h30 · C. 13h", size=20, gap=8)
e.ex("A2", "单选", "A", "巴西没有夏令时，钟表不动",
     "Nesta semana, o relógio no Brasil... A. não muda · B. volta uma hora · C. avança uma hora", size=20, gap=8)
e.head("B　O PRESENTE", 25)
e.bridge("补全动词的现在时形式。")
e.ex("A2", "完成句子", "confere", "conferir：ele → confere",
     "O candidato ___ (conferir) o cartão.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "abre", "abrir：ele → abre",
     "O portão ___ (abrir) às 12h.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "levamos", "levar：nós → levamos",
     "Nós ___ (levar) documento com foto.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "começa", "começar：ela → começa",
     "A prova ___ (começar) às 13h30.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "termina", "terminar：ela → termina",
     "A prova ___ (terminar) às 18h30.", instr="填空", size=20, gap=8)
e.head("C　COMPLETE COM OS NÚMEROS", 25)
e.bridge("用第 1、2 版的数字填空。")
e.ex("A2", "完成句子", "1", "12 点到 13 点 = 1 小时",
     "Os portões ficam abertos ___ hora.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "5", "13:30 至 18:30 = 5 小时",
     "A prova dura ___ horas.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "300", "5×60 = 300 分钟",
     "De 13h30 a 18h30 são ___ minutos.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "90", "45 + 45 = 90",
     "O dia 15 tem ___ questões.", instr="填空", size=20, gap=8)
e.head("D　AS PALAVRAS", 25)
e.match_set("A2", "词汇配对",
            ["a proclamação", "o feriado", "a natureza", "a matemática"],
            ["a ciência dos números e das formas",
             "o ato de anunciar uma mudança",
             "um dia de descanso marcado por lei",
             "a ciência da vida, da física e da química"],
            ["b", "c", "d", "a"],
            ["proclamação=宣布一个变化 b", "feriado=法律规定的休息日 c", "natureza=生命、物理与化学的科学 d", "matemática=数字与图形的科学 a"],
            instr="把词和释义配对")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-vida.svg")
print("P2 saved, exercises so far:", len(REG))
