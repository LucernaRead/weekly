# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/pt-ru-proof/out-ru/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · CAPA (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 2 · SEGUNDA EDIÇÃO", 23, "sans", True, OLIVE)
p.text(975, 92, "TODA SEMANA EM PORTUGUÊS · КАЖДУЮ НЕДЕЛЮ · ПОРТУГАЛЬСКИЙ БРАЗИЛИИ", 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "SEMANA DE 2 A 8 DE NOVEMBRO DE 2026", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, GOLD, 1.6)
p.text(975, 262, "A Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "ПОРТУГАЛЬСКИЙ ЕЖЕНЕДЕЛЬНИК · VOL.2 · A SEMANA DO ENEM · FINADOS · O FUTEBOL DECIDE", 36, "serif", True, INK, anchor="middle")
p.text(975, 372, "ТЕКСТЫ НА ПОРТУГАЛЬСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ", 19, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)

# band
p.rect(MX, 424, RIGHT - MX, 118, fill=DARK)
p.text(MX + 30, 478, "A SEMANA DO ENEM!", 36, "sans", True, "#f3edda")
p.text(MX + 30, 522, "De segunda a domingo, o Brasil revisa, descansa e faz a prova.", 23, "serif", False, "#e8dfc8")
p.text(RIGHT - 30, 478, "НЕДЕЛЯ ENEM", 24, "sans", True, "#b3a06a", anchor="end")
p.text(RIGHT - 30, 522, "2 ноября — выходные на Финадос · 8 ноября — первый день Enem", 21, "sans", False, "#b3a06a", anchor="end")

# ---- headline (span cols 0-2) ----
hy = 580
p.text(MX, hy + 26, "A NOTÍCIA · Главная новость", 22, "sans", True, BRICK)
hy = p.para(MX, hy + 92, "Do feriadão à prova: a semana do Enem", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 28, "Da redação da A Lucerna · Nível de leitura: A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Começa na segunda-feira, 2 de novembro, feriado de Finados, e termina no domingo, 8 de novembro, com o primeiro dia do Enem. Entre um dia e outro, o país inteiro vive a mesma semana: descansar, revisar e fazer a prova.", size=24)
f.para("O feriadão abre a semana: sábado, 31 de outubro, domingo, 1º de novembro, e segunda-feira, 2, feriado nacional. Muita gente viaja, visita a família e vai ao cemitério levar flores. Para quem faz o Enem, o feriadão é também um fim de semana de revisão: um pouco por dia, sem maratona.", size=24)
f.para("No domingo, 8 de novembro, é o primeiro dia do Enem 2026. Os portões abrem às 12h e fecham às 13h, no horário de Brasília. A prova começa às 13h30 e vai até as 19h: são cinco horas e meia de redação, Linguagens e Ciências Humanas. Mais de 5 milhões de estudantes estão inscritos.", size=24)
f.para("E o futebol não para: a rodada 34 do Brasileirão tem jogo de segunda a sexta, e as semifinais da Copa do Brasil se decidem no fim de semana — sábado, Atlético-MG × Grêmio, e domingo, Vasco × Palmeiras (página 4). O sábado, 31, foi de Halloween, e o domingo, 1º, teve os jogos de ida da Copa do Brasil.", size=24)
f.para("Esta é a segunda edição da A Lucerna em português: toda semana, o Brasil de verdade, com clareza e honestidade. Boa prova — e boa leitura!", size=24)
f.expl("Пояснение — feriadão = длинные праздничные выходные · o portão = ворота · a redação = сочинение · revisar = повторять.")
f.box("A SEMANA EM NÚMEROS · Цифры", [
    ("12h — os portões abrem no domingo 8 (воскресенье 8-го: ворота открываются в 12h)", "serif", False, INK, 20, 1.35),
    ("13h — os portões fecham (в 13h ворота закрываются, опоздавших не пускают)", "serif", False, INK, 20, 1.35),
    ("13h30–19h — a prova do dia 8 (экзамен дня 8: с 13:30 до 19:00)", "serif", False, INK, 20, 1.35),
    ("5h30 — a duração da prova do dia 8 (экзамен дня 8 длится пять с половиной часов)", "serif", False, INK, 20, 1.35),
])
f.head("AGORA VOCÊ · Теперь вы", 25)
f.ex("A2", "Вставьте слово", "feriadão", "feriadão = длинные праздничные выходные",
     "A semana começa com o ___ de Finados.", size=19.5, gap=6)
f.ex("A2", "Вставьте слово", "portões", "portões = ворота (ворота экзаменационного центра)",
     "No domingo 8, os ___ abrem às 12h.", size=19.5, gap=6)
f.ex("A2", "Вставьте слово", "redação", "redação = сочинение",
     "A prova do dia 8 tem ___, Linguagens e Ciências Humanas.", size=19.5, gap=6)
f.ex("A2", "Вставьте слово", "13h30", "13h30: экзамен начинается (время Бразилиа)",
     "A prova começa às ___.", size=19.5, gap=6)
f.ex("A2", "Вставьте слово", "19h", "19h: экзамен заканчивается",
     "A prova vai até as ___.", size=19.5, gap=6)
f.ex("B1", "Вставьте слово", "revisam", "revisar, настоящее время, форма eles: revisam",
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
p.text(gx + 22, byy + 76, "Опоздавших не пускают после 13h", 19, "sans", False, GREY)

# ---- conteúdo (col 3) ----
sy = 1312
p.rect(gx, sy, gw, 340, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(gx + 22, sy + 40, "NESTA EDIÇÃO · В этом выпуске", 24, "sans", True, OLIVE)
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
p.para(gx, y2 + 28, "«Длинные выходные»: праздник и уик-энд.", 19, "sans", False, GREY, gw, 1.35)

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
p.text(bx + 22, 1914, "EM POUCAS PALAVRAS · Коротко", 24, "sans", True, OLIVE)
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
p.text(MX, qy + 36, "QUIZ RELÂMPAGO · Блиц-опрос", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Прочитайте первую полосу и выберите ответ · Ответы — страница 8", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", "Выбор ответа", "B", "Длинные выходные — с 31 октября по 2 ноября",
      "O feriadão vai... A. de 2 a 4 de novembro · B. de 31 de outubro a 2 de novembro · C. de 8 a 15 de novembro", size=21)
qf.ex("A2", "Выбор ответа", "B", "Ворота закрываются в 13h",
      "Os portões do Enem fecham às... A. 12h · B. 13h · C. 13h30", size=21)
qf.ex("A2", "Выбор ответа", "C", "День 1: сочинение, языки и гуманитарные науки",
      "No dia 8, a prova tem... A. só Matemática · B. só redação · C. redação, Linguagens e Ciências Humanas", size=21)
qf.ex("A2", "Выбор ответа", "B", "Ответные матчи — 7-го и 8-го",
      "Os jogos de volta da Copa do Brasil são... A. no dia 1º · B. nos dias 7 e 8 · C. no dia 15", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-capa.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · VIDA (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("VIDA · Жизнь", "A Lucerna", "NÍVEL A2 · Finados e revisão: o feriadão do Brasil · Финадос и повторение: длинные выходные Бразилии")

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
f.box("PARA NÃO ERRAR · Памятка", [
    ("«Confira o cartão, durma bem, chegue cedo.» Três passos e o domingo fica tranquilo: o resto é com a prova.", "serif", False, INK, 21.5, 1.4),
])
f.gloss("o feriadão = длинные праздничные выходные · o cemitério = кладбище · a vela = свеча · o crisântemo = хризантема · a missa = месса · conferir = проверять.")
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
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("В вашей стране есть день памяти умерших? Что делают семьи в этот день? Напишите две фразы по-португальски и пришлите в редакцию: лучшие появятся на странице 7.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E VOCÊ? · А вы?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "В вашей стране есть день памяти умерших? Что делают семьи в этот день? Напишите две фразы по-португальски и пришлите в редакцию: лучшие появятся на странице 7.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- Os horários do domingo 8: 4 time boxes ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, GOLD, 2)
p.text(MX, dy + 28, "OS HORÁRIOS DO DOMINGO 8 · Расписание воскресенья 8-го", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "Um país, vários relógios · Одна страна, несколько часовых поясов", 20, "sans", False, GREY, anchor="end")
times = [
    ("12h", "os portões abrem", "Ворота открываются в 12h"),
    ("13h", "os portões fecham", "Ворота закрываются в 13h"),
    ("13h30", "a prova começa", "Экзамен начинается в 13:30"),
    ("19h", "a prova termina", "Экзамен заканчивается в 19:00"),
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
p.text(MX, ey + 28, "EXERCÍCIOS · Упражнения страницы 2", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Ответы на странице 8 · Уровни перемешаны — ищите по номеру задания", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A · COMPREENSÃO", 25)
e.expl("Прочитайте статью на странице 2 и выберите правильный ответ.")
e.ex("A2", "Выбор ответа", "B", "Длинные выходные — с 31 октября по 2 ноября",
     "O feriadão vai... A. de 2 a 5 de novembro · B. de 31 de outubro a 2 de novembro · C. de 8 a 15 de novembro", size=20, gap=8)
e.ex("A2", "Выбор ответа", "B", "На Финадос семьи идут на кладбище с цветами",
     "Em Finados, as famílias... A. compram presentes de Natal · B. visitam os cemitérios e levam flores · C. votam para presidente", size=20, gap=8)
e.ex("A2", "Выбор ответа", "B", "Карточка подтверждения показывает место экзамена",
     "O Cartão de Confirmação mostra... A. a nota do aluno · B. o local da prova · C. o resultado final", size=20, gap=8)
e.ex("A2", "Выбор ответа", "B", "Ворота закрываются в 13h",
     "Os portões fecham às... A. 12h · B. 13h · C. 19h", size=20, gap=8)
e.ex("A2", "Выбор ответа", "A", "В Бразилии нет летнего времени: часы не переводят",
     "Nesta semana, o relógio no Brasil... A. não muda · B. volta uma hora · C. avança uma hora", size=20, gap=8)
e.head("B · O PRESENTE", 25)
e.expl("Вставьте глаголы в настоящем времени.")
e.ex("A2", "Вставьте слово", "confere", "conferir: ele → confere",
     "O candidato ___ (conferir) o cartão.", instr="Вставьте", size=20, gap=8)
e.ex("A2", "Вставьте слово", "abre", "abrir: ele → abre",
     "O portão ___ (abrir) às 12h.", instr="Вставьте", size=20, gap=8)
e.ex("A2", "Вставьте слово", "levamos", "levar: nós → levamos",
     "Nós ___ (levar) documento com foto.", instr="Вставьте", size=20, gap=8)
e.ex("A2", "Вставьте слово", "começa", "começar: ela → começa",
     "A prova ___ (começar) às 13h30.", instr="Вставьте", size=20, gap=8)
e.ex("A2", "Вставьте слово", "é", "ser, настоящее время, форма ela: é",
     "A missa de Finados ___ (ser) um momento calmo.", instr="Вставьте", size=20, gap=8)
e.head("C · COMPLETE COM OS NÚMEROS", 25)
e.expl("Заполните пропуски цифрами со страниц 1 и 2.")
e.ex("A2", "Вставьте слово", "1", "С 12h до 13h = 1 час",
     "Os portões ficam abertos ___ hora.", instr="Вставьте", size=20, gap=8)
e.ex("A2", "Вставьте слово", "5", "С 13:30 до 19:00 = пять с половиной часов",
     "A prova dura ___ horas e meia.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Вставьте слово", "330", "5×60 + 30 = 330 минут",
     "De 13h30 a 19h são ___ minutos.", instr="Вставьте", size=20, gap=8)
e.ex("A2", "Вставьте слово", "3", "31-е, 1-е, 2-е = 3 дня",
     "O feriadão tem ___ dias.", instr="Вставьте", size=20, gap=8)
e.head("D · AS PALAVRAS", 25)
e.match_set("A2", "Сопоставление",
            ["o feriadão", "o cemitério", "a vela", "o crisântemo"],
            ["a flor que as famílias levam a Finados",
             "o lugar onde ficam os túmulos",
             "um feriado grudado no fim de semana",
             "o objeto que dá luz e se acende em memória"],
            ["c", "b", "d", "a"],
            ["feriadão = праздник, слившийся с выходными (c)", "cemitério = место, где стоят надгробия (b)", "vela = то, что зажигают в память (d)", "crisântemo = цветок, который несут на Финадос (a)"],
            instr="Соедините пары")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-vida.svg")
print("P2 saved, exercises so far:", len(REG))
