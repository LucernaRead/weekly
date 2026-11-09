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
p.text(MX, 92, "VOL. 1　PRIMEIRA EDIÇÃO", 17, "sans", True, OLIVE, spacing=1.7)
p.text(975, 92, "TODA SEMANA EM PORTUGUÊS　CADA SEMANA　EL PORTUGUÉS QUE LEE BRASIL", 17, "sans", False, GREY, anchor="middle", spacing=1.7)
p.text(RIGHT, 92, "SEMANA DE 19 A 25 DE OUTUBRO DE 2026", 17, "sans", False, GREY, anchor="end", spacing=1.7)
p.text(975, 262, "A Lucerna", 196, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "SEMANARIO EN PORTUGUÉS　VOL.1　O SEGUNDO TURNO　O DEBATE FINAL　O ENEM VEM AÍ", 34, "serif", True, OLIVE, anchor="middle", spacing=0)
p.text(975, 372, "TEXTOS EN PORTUGUÉS　EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES", 16, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)

# band
p.rect(MX, 470, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 30, 524, "DOMINGO É DIA DE DECISÃO!", 46, "sans", True, ONCLOTH)
p.text(MX + 30, 568, "No domingo, 25 de outubro, o Brasil volta às urnas: é o segundo turno das eleições.", 25, "serif", False, "#cac8ba")
p.text(RIGHT - 30, 524, "DOMINGO, DÍA DE DECISIÓN", 27, "sans", True, GOOSE, anchor="end")
p.text(RIGHT - 30, 568, "La segunda vuelta presidencial　ver la página 6", 18, "sans", False, GOOSE, anchor="end")

# ---- headline (span cols 0-2) ----
hy = 590
p.text(MX, hy + 26, "A NOTÍCIA　EN PORTADA", 17, "sans", True, OLIVE)
hy = p.para(MX, hy + 92, "Domingo é dia de decisão: o Brasil volta às urnas", 53, "serif", True, INK, 1323, 1.06)
p.text(MX, hy + 28, "Da redação da A Lucerna　Nível de leitura: A2", 17, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Acontece tudo no domingo. No dia 25 de outubro, das 8h às 17h (hora de Brasília), os brasileiros voltam às urnas para o segundo turno das eleições. Na disputa pela Presidência, só dois nomes: Lula (PT) e Flávio Bolsonaro (PL). Em seis estados e no Distrito Federal, há também o segundo turno para governador.", size=24)
f.para("Mas atenção: o seu local de votação pode ser novo. O Tribunal Superior Eleitoral (TSE) mudou o endereço de 4.352 seções eleitorais para este segundo turno (a lista por estado está na página 2). A regra é simples: confira o seu local no aplicativo e-Título antes de sair de casa.", size=24)
f.para("A semana eleitoral tem um grande ritual de TV: na sexta-feira, 23 de outubro, a TV Globo transmite o último debate entre os candidatos, depois do Jornal Nacional, com mediação de César Tralli. Os dois candidatos foram convidados. Na mesma sexta-feira, termina a propaganda eleitoral gratuita.", size=24)
f.para("E o Brasil fora das urnas? Na terça-feira, o Vasco perdeu por 3 a 1 para o Boca Juniors e saiu da Copa Sul-Americana (página 4). Os jovens contam os dias para o Enem, em novembro (página 5). E a guitarra volta a crescer nas buscas (página 3).", size=24)
f.para("Esta é a primeira edição da A Lucerna em português: toda semana, o Brasil de verdade, com clareza e honestidade. Bem-vindos!", size=24)
f.expl("Nota — segundo turno = la segunda vuelta · seção eleitoral = el colegio electoral · conferir = comprobar, verificar.")
f.box("A SEMANA EM NÚMEROS　CIFRAS", [
    ("4.352 — as seções eleitorais que mudaram de endereço (los colegios electorales que cambiaron de dirección)", "serif", False, INK, 20, 1.35),
    ("499.248 — o total de seções eleitorais do país (el total de colegios electorales del país)", "serif", False, INK, 20, 1.35),
    ("8h–17h — o horário da votação de domingo (el horario de votación del domingo, hora de Brasília)", "serif", False, INK, 20, 1.35),
])
f.head("AGORA VOCÊ　AHORA TÚ", 25)
f.ex("A2", "完成句子", "segundo", "segundo turno = la segunda vuelta",
     "Domingo é o ___ turno das eleições.", size=19.5, gap=6)
f.ex("A2", "完成句子", "urnas", "voltar às urnas = volver a las urnas, ir a votar",
     "No domingo, os brasileiros voltam às ___.", size=19.5, gap=6)
f.ex("A2", "完成句子", "4.352", "4.352 colegios cambiaron de dirección",
     "O TSE mudou o endereço de ___ seções eleitorais.", size=19.5, gap=6)
f.ex("A2", "完成句子", "e-Título", "e-Título = el título electrónico de elector",
     "Confira o seu local de votação no aplicativo ___.", size=19.5, gap=6)
f.ex("A2", "完成句子", "debate", "debate = el debate televisado",
     "Na sexta-feira, a TV Globo transmite o último ___ entre os candidatos.", size=19.5, gap=6)
f.ex("B1", "完成句子", "mudaram", "mudar en pasado, forma de ellas: mudaram",
     "Muitas seções eleitorais ___ (mudar) de endereço para o segundo turno.", size=19.5, gap=6)
f.end_report()

# ---- as buscas da eleição (col 3) ----
gx, gw = COLX[3], CW
gy = 588
p.rect(gx, gy, gw, 700, fill=BOX)
p.text(gx + 22, gy + 40, "AS BUSCAS", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "DA ELEIÇÃO", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Brasil busca　as buscas no Google", 19, "sans", False, GREY)
gt = [
    ("eleições", "+900%", 250),
    ("que horas começa a votação?", "+550%", 153),
    ("multa eleitoral", "+350%", 97),
    ("seção eleitoral", "+350%", 97),
    ("presidente", "+250%", 69),
]
byy = gy + 150
for i, (lab, vol, bw) in enumerate(gt):
    p.text(gx + 22, byy + 22, f"{i+1}. {lab}", 19 if lab.startswith("que horas") else 21.5, "serif", True, INK)
    p.text(gx + gw - 22, byy + 22, vol, 20, "sans", True, OLIVE, anchor="end")
    p.rect(gx + 22, byy + 34, bw, 22, fill=OLIVE)
    byy += 92
p.text(gx + 22, byy + 16, "Dados do Google, em torno do 1º turno:", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "interesse de busca — não é voto.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 76, "Datos de Google: no es un voto.", 19, "sans", False, GREY)

# ---- conteúdo (col 3) ----
sy = 1312
p.rect(gx, sy, gw, 340, fill="#f0eee5")
p.text(gx + 22, sy + 40, "NESTA EDIÇÃO　EN ESTA EDICIÓN", 24, "sans", True, OLIVE)
som = [
    ("Pág. 2", "Como votar, passo a passo", "A2"),
    ("Pág. 3", "A volta da guitarra", "A2→B1"),
    ("Pág. 4", "O futebol da semana", "B1"),
    ("Pág. 5", "Fazenda, Enem e futuro", "B1"),
    ("Pág. 6", "O segundo turno explicado", "B2"),
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
p.text(gx, my + 76, "« seção eleitoral »", 21.5, "serif", False, INK, italic=True)
wy = p.para(gx, my + 108, "o lugar exato do seu voto — a escola, a sala, a urna.", 21.5, "serif", False, INK, gw, 1.4)
wy2 = p.para(gx, wy + 10, "«Sección electoral»: tu lugar de voto.", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, max(1844, wy2 - 16), LINE, 1.2)  # adaptive: keep the rule clear of a 2-line weekly-word gloss
iy = 1874
ix, iw = span_x(0, 2)
image(p, "urna.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "A urna eletrônica brasileira: é nela que o eleitor digita o número do candidato e confirma o voto. No domingo, o país inteiro vota das 8h às 17h, hora de Brasília. (Página 2)",
        "Foto: Tribunal Superior Eleitoral (TSE) — domínio público")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2300, tag="P1-tv")
f2.head("A SEMANA NA TV", 25)
f2.para("Sexta-feira à noite, o país para diante da TV: é o último debate presidencial, na Globo, depois do Jornal Nacional.", 22.5)
f2.para("Na quinta-feira, outro programa famoso decide um nome: a enquete de A Fazenda 18. Duas votações na mesma semana — uma decide o presidente, a outra decide quem continua no jogo. (Páginas 5 e 6)", 22.5)
f2.end_report()
# col 3 EM POUCAS PALAVRAS
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX)
p.text(bx + 22, 1914, "EM POUCAS PALAVRAS　BREVE", 24, "sans", True, OLIVE)
brefs = [
    ("O VOTO", "Domingo, das 8h às 17h: confira sua seção no e-Título antes de sair. (Página 2)"),
    ("O DEBATE", "Sexta-feira, 23, na TV Globo, depois do Jornal Nacional. (Página 6)"),
    ("O ENEM", "Falta pouco: as provas são nos dias 8 e 15 de novembro. (Página 5)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, OLIVE)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- quiz relâmpago ----
qy = 2312
p.hline(MX, RIGHT, qy, OLIVE, 2)
p.text(MX, qy + 36, "QUIZ RELÂMPAGO　QUIZ RÁPIDO", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Lee la portada y elige la respuesta correcta　Respuestas en la página 8", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2560, tag="P1-quiz")
qf.ex("A2", "单选", "B", "La segunda vuelta es el domingo 25 de octubre",
      "O segundo turno é... A. na sexta-feira, 23 · B. no domingo, 25 · C. no dia 8 de novembro", size=21)
qf.ex("A2", "单选", "A", "Votación de 8 h a 17 h, hora de Brasília",
      "A votação de domingo vai... A. das 8h às 17h · B. das 9h às 18h · C. o dia inteiro", size=21)
qf.ex("A2", "单选", "C", "4.352 colegios cambiaron de dirección",
      "Quantas seções eleitorais mudaram de endereço? A. 982 · B. 2.239 · C. 4.352", size=21)
qf.ex("A2", "单选", "B", "El último debate es el viernes 23",
      "O último debate presidencial é... A. no domingo · B. na sexta-feira · C. na terça-feira", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-capa.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · VIDA (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("VIDA　VIDA DIARIA", "A Lucerna", "NÍVEL A2　Como votar, passo a passo　Cómo votar, paso a paso")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("Como votar no domingo: o passo a passo tranquilo", 32)
f.byline("Da redação da A Lucerna　Nível de leitura: A2")
f.para("Votar no Brasil é obrigatório para quem tem entre 18 e 70 anos — e é simples, quando você sabe o caminho. Este é o passo a passo do domingo.")
f.para("Primeiro: confira o seu local de votação. Abra o aplicativo e-Título e veja a sua zona e a sua seção eleitoral. Lembre-se: 4.352 seções mudaram de endereço para o segundo turno. A seção da primeira rodada pode não ser a mesma de agora.")
f.para("Segundo: prepare o documento. Leve um documento oficial com foto — ou o próprio e-Título, que já mostra a sua foto. Terceiro: chegue no horário. As urnas abrem às 8h e fecham às 17h, no horário de Brasília. No Acre, por causa do fuso, a votação é das 6h às 15h no relógio local.")
f.para("Na seção, você apresenta o documento, digita o número do candidato na urna eletrônica e confirma. É rápido: a fila anda e o voto é secreto. Quem não pode votar no domingo precisa justificar a ausência — sem justificativa, há uma multa eleitoral.")
f.para("Um detalhe que confunde muita gente: o Brasil não tem horário de verão. Ele acabou em 2019 e não volta neste ano: no domingo, ninguém muda o relógio. (Na Europa, o relógio muda no mesmo fim de semana — aqui, não.)")
f.head("E SE EU NÃO VOTAR?", 25)
f.para("Se você não votar e não justificar, paga a multa eleitoral e fica com uma pendência no título de eleitor. A palavra «multa eleitoral» foi uma das buscas que mais cresceram no Google antes do primeiro turno: +350%. Melhor conferir tudo antes: local, documento e horário.", 23.5)
f.box("PARA NÃO ERRAR　LA REGLA", [
    ("«Confira a seção, leve o documento, chegue no horário.» Três passos e o domingo fica tranquilo: o resto é com a urna.", "serif", False, INK, 21.5, 1.4),
])
f.gloss("o título de eleitor = el título de elector · a zona eleitoral = la zona electoral · justificar = justificar la ausencia · a multa = la multa · obrigatório = obligatorio.")
f.end_report()

# col 3: facts + e você? (sequential, measured)
ix = COLX[3]
facts = ["A votação é das 8h às 17h, hora de Brasília; no Acre, das 6h às 15h no relógio local.",
         "4.352 seções mudaram de endereço: São Paulo (982), Minas Gerais (514), Rio de Janeiro (431) e Bahia (312).",
         "Quem tem entre 18 e 70 anos vota por obrigação; o documento precisa ter foto."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "VOCÊ SABIA?", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E você? No seu país, votar é obrigatório ou é uma escolha? Escreva duas frases em português e mande para a redação: as melhores saem no VOL.2 (página 7, «Cartas dos leitores»)."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("En tu país, ¿votar es obligatorio o una elección? Escribe dos frases en portugués y envíalas a la redacción.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E VOCÊ?　CUÉNTANOS", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "En tu país, ¿votar es obligatorio o una elección? Escribe dos frases en portugués y envíalas a la redacción.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- Os horários do domingo: 4 time boxes ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, OLIVE, 2)
p.text(MX, dy + 28, "OS HORÁRIOS DO DOMINGO　LOS HORARIOS DEL DOMINGO", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "Um país, vários relógios　Un país, varios relojes", 20, "sans", False, GREY, anchor="end")
times = [
    ("6h", "no Acre, as urnas abrem", "en Acre, abren (hora local)"),
    ("8h", "em Brasília, as urnas abrem", "en Brasília, abren"),
    ("15h", "no Acre, as urnas fecham", "en Acre, cierran (hora local)"),
    ("17h", "em Brasília, as urnas fecham", "en Brasília, cierran"),
]
for i, (t, lab, cn) in enumerate(times):
    bx = COLX[i]
    p.rect(bx, dy + 52, CW, 150, fill=BOX)
    p.text(bx + 22, dy + 116, t, 40, "serif", True, OLIVE)
    yy = p.para(bx + 128, dy + 92, lab, 21.5, "serif", False, INK, CW - 150, 1.36)
    p.para(bx + 128, yy + 20, cn, 19, "sans", False, GREY, CW - 150, 1.3)
p.para(MX, dy + 234, "Atenção aos fusos: o Brasil tem vários relógios, mas a regra do TSE é uma só — abrir e fechar no mesmo instante, às 8h e às 17h de Brasília.", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P2 exercises ----
ey = dy + 282
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EXERCÍCIOS　EJERCICIOS DE LA PÁGINA 2", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respuestas en la página 8　Niveles mezclados: busca tu número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A　OS PASSOS DO VOTO", 25)
e.expl("Lee el artículo de la página 2 y elige la respuesta correcta.")
e.ex("A2", "单选", "B", "El primer paso es comprobar el lugar de votación",
     "O primeiro passo do eleitor é... A. pagar a multa · B. conferir o local de votação · C. assistir ao debate", size=20, gap=8)
e.ex("A2", "单选", "A", "Se presenta un documento oficial con foto",
     "Na seção, o eleitor apresenta... A. um documento com foto · B. um comprovante de endereço · C. o celular de um amigo", size=20, gap=8)
e.ex("A2", "单选", "C", "Cierran a las 17 h, hora de Brasília",
     "As urnas fecham às... A. 15h em todo o país · B. 18h em Brasília · C. 17h, hora de Brasília", size=20, gap=8)
e.ex("A2", "单选", "B", "Quien no vota ni justifica paga una multa",
     "Quem não vota e não justifica... A. vota duas vezes no ano seguinte · B. paga uma multa · C. perde o título para sempre", size=20, gap=8)
e.ex("A2", "单选", "A", "Brasil no tiene horario de verano: el reloj no cambia",
     "No domingo, o relógio no Brasil... A. não muda · B. volta uma hora · C. avança uma hora", size=20, gap=8)
e.head("B　O PRESENTE", 25)
e.expl("Completa con la forma del presente.")
e.ex("A2", "完成句子", "confere", "conferir: ele → confere",
     "O eleitor ___ (conferir) o local no aplicativo.", instr="Completa", size=20, gap=8)
e.ex("A2", "完成句子", "abre", "abrir: ela → abre",
     "A seção ___ (abrir) às oito da manhã.", instr="Completa", size=20, gap=8)
e.ex("A2", "完成句子", "levamos", "levar: nós → levamos",
     "Nós ___ (levar) um documento com foto.", instr="Completa", size=20, gap=8)
e.ex("B1", "完成句子", "digita", "digitar: ele → digita",
     "Na urna, o eleitor ___ (digitar) o número do candidato.", instr="Completa", size=20, gap=8)
e.ex("A2", "完成句子", "fecha", "fechar: ela → fecha",
     "A votação ___ (fechar) às cinco da tarde.", instr="Completa", size=20, gap=8)
e.head("C　COMPLETE COM OS NÚMEROS", 25)
e.expl("Usa los números de las páginas 1 y 2.")
e.ex("A2", "完成句子", "4.352", "4.352 colegios cambiaron de dirección",
     "___ seções eleitorais mudaram de endereço.", instr="Completa", size=20, gap=8)
e.ex("A2", "完成句子", "982", "982 en São Paulo",
     "Em São Paulo, são ___ seções com endereço novo.", instr="Completa", size=20, gap=8)
e.ex("B1", "完成句子", "2.239", "982 + 514 + 431 + 312 = 2.239",
     "SP + MG + RJ + BA somam ___ seções novas.", instr="Completa", size=20, gap=8)
e.ex("A2", "完成句子", "17", "Termina a las 17 h de Brasília",
     "A votação termina às ___h, no horário de Brasília.", instr="Completa", size=20, gap=8)
e.head("D　AS PALAVRAS", 25)
e.match_set("A2", "词汇配对",
            ["a seção eleitoral", "a zona eleitoral", "justificar", "a multa"],
            ["o dinheiro que você paga por uma falta",
             "explicar por que você não votou",
             "a área da cidade onde você vota",
             "o lugar exato da sua urna"],
            ["d", "c", "b", "a"],
            ["seção = el lugar exacto de tu voto: d", "zona = la zona de la ciudad donde votas: c", "justificar = explicar por qué no votaste: b", "multa = el dinero que pagas por una falta: a"],
            instr="Relaciona")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-vida.svg")
print("P2 saved, exercises so far:", len(REG))
