# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-pt-it/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA · CULTURA", "A Lucerna", "A2 → B1 · Proclamação da República: 137 anni")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("Proclamação da República: 137 anos de Brasil", 37)
f.byline("Da redação da A Lucerna · Nível de leitura: A2 → B1")
f.para("Em 15 de novembro de 1889, tropas comandadas pelo marechal Deodoro da Fonseca tomaram o governo no Rio de Janeiro, então a capital do país. A monarquia acabou: o imperador Dom Pedro II foi deposto e partiu para o exílio. Deodoro assumiu o governo provisório e se tornou o primeiro presidente do Brasil.")
f.para("A data virou feriado nacional: a Proclamação da República está na lista da Lei nº 662, de 1949, ao lado do 1º de janeiro, do 1º de maio e do 7 de setembro. É um feriado para todo o país — nenhuma cidade pode transformá-lo em dia útil.")
f.para("O que muda em 137 anos? A República é a forma do Estado: o presidente é eleito, o poder tem prazo, e as leis valem para todos. Para quem aprende português, a data traz palavras úteis: república, presidente, eleição, voto, constituição.")
f.para("E neste ano a data cai num domingo — o mesmo domingo do Enem. Não há ponte nem folga extra: quem não trabalha no domingo descansa como sempre; quem faz a prova estuda como sempre. Na página 2, a rotina do domingo 15. Na página 5, a semana dos jovens. Mas antes, uma pergunta: no seu país, há um feriado que lembra o começo da república?")
f.gloss("a monarquia = monarchia · a república = repubblica · o marechal = maresciallo · o exílio = esilio · o governo = governo · a lei = legge.")
f.head("UM DOMINGO, DOIS SENTIDOS", 25)
f.para("Domingo é dia de prova e dia de feriado: silêncio na sala de aula e memória na história. O Brasil faz as duas coisas no mesmo dia — e o português aprende os dois vocabulários: «13h30, caneta preta» de um lado, «15 de novembro de 1889» do outro.")
f.para("Na página 6, os números do segundo domingo.")
f.end_report()

# col 3: calendar box + e você + words box (sequential)
ix = COLX[3]
semana = ["Seg 9 — começa a semana do segundo dia do Enem.",
          "Qua 11 — 11.11: o dia das promoções no comércio eletrônico.",
          "Sáb 14 — Japão × Brasil, às 7h15; Mirassol × Atlético-MG, às 18h30.",
          "Dom 15 — Enem, dia 2; feriado da Proclamação da República."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in semana) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "A SEMANA, DIA A DIA", 24, "sans", True, OLIVE)
yy3 += 52
for t in semana:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E você? No seu país, há um feriado que lembra o começo da república? Escreva duas frases em português e mande para a redação."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Nel tuo paese c’è una festa per la fondazione della repubblica? Scrivi due frasi e mandacele.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E VOCÊ? · E TU?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Nel tuo paese c’è una festa per la fondazione della repubblica? Scrivi due frasi e mandacele.", 20, "sans", False, GREY, CW - 44, 1.42)
ky3 = ey3 + eh + 26
kb = "a república · o presidente · a eleição · o voto · a constituição · «proclamar» — seis palavras para um feriado de 137 anos."
kh = 62 + len(wrap(kb, "serif", False, 21.5, CW - 44)) * 30.5 + 16
p.rect(ix, ky3, CW, kh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ky3 + 16
p.text(ix + 22, yy3 + 26, "PALAVRAS DA REPÚBLICA", 22, "sans", True, OLIVE)
yy3 += 52
p.para(ix + 22, yy3 + 21, kb, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P3 col3 ends", ky3 + kh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EXERCÍCIOS · ESERCIZI PAGINA 3", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Risposte a pagina 8 · Livelli mescolati: cerca per numero", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · COMPREENSÃO", 25)
e.bridge("Leggi pagina 3 e scegli la risposta giusta.")
e.ex("A2", "Scelta multipla", "B", "La Proclamazione della Repubblica è avvenuta il 15 novembre 1889",
     "A Proclamação da República foi... A. em 1949 · B. em 15 de novembro de 1889 · C. em 1822", size=20, gap=8)
e.ex("A2", "Scelta multipla", "B", "Deodoro è diventato il primo presidente del Brasile",
     "Deodoro da Fonseca... A. foi o último imperador · B. se tornou o primeiro presidente · C. escreveu a Lei nº 662", size=20, gap=8)
e.ex("A2", "Scelta multipla", "B", "Una festa nazionale che nessuna città può trasformare in giorno lavorativo",
     "A Proclamação é um feriado... A. só do Rio · B. nacional, para todo o país · C. só das escolas", size=20, gap=8)
e.ex("A2", "Scelta multipla", "C", "Nel 2026 la festa cade di domenica",
     "Em 2026, o feriado cai... A. na segunda · B. na sexta · C. num domingo", size=20, gap=8)
e.ex("B1", "Scelta multipla", "A", "In repubblica il presidente è eletto e il potere ha un limite di tempo",
     "Na República, o presidente... A. é eleito e o poder tem prazo · B. governa para sempre · C. é escolhido pelo imperador", size=20, gap=8)
e.head("B · AS PALAVRAS DO TEXTO", 25)
e.bridge("Completa con le parole del riquadro.")
e.para("monarquia · república · marechal · exílio · governo · lei", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "Completare la frase", "monarquia", "monarquia = monarchia",
     "Em 1889, acabou a ___.", instr="Completa", size=20, gap=8)
e.ex("A2", "Completare la frase", "república", "república = repubblica",
     "O Brasil virou uma ___.", instr="Completa", size=20, gap=8)
e.ex("A2", "Completare la frase", "marechal", "marechal = maresciallo",
     "Deodoro era ___.", instr="Completa", size=20, gap=8)
e.ex("A2", "Completare la frase", "exílio", "exílio = esilio",
     "Dom Pedro II partiu para o ___.", instr="Completa", size=20, gap=8)
e.ex("A2", "Completare la frase", "governo", "governo = governo",
     "Deodoro assumiu o ___ provisório.", instr="Completa", size=20, gap=8)
e.ex("B1", "Completare la frase", "lei", "lei = legge",
     "A data está na lista da ___ nº 662.", instr="Completa", size=20, gap=8)
e.head("C · O PRETÉRITO PERFEITO", 25)
e.bridge("Completa al passato (pretérito perfeito).")
e.ex("B1", "Completare la frase", "tomaram", "tomar, passato, forma elas: tomaram",
     "As tropas ___ (tomar) o governo.", instr="Completa", size=20, gap=8)
e.ex("B1", "Completare la frase", "acabou", "acabar, passato, forma ela: acabou",
     "A monarquia ___ (acabar) em 1889.", instr="Completa", size=20, gap=8)
e.ex("B1", "Completare la frase", "foi", "ser, passato, forma ele: foi",
     "Dom Pedro II ___ (ser) deposto.", instr="Completa", size=20, gap=8)
e.ex("B1", "Completare la frase", "assumiu", "assumir, passato, forma ele: assumiu",
     "Deodoro ___ (assumir) o governo.", instr="Completa", size=20, gap=8)
e.head("D · CONSTRUA AS FRASES", 25)
e.bridge("Metti le parole nell’ordine giusto.")
e.ex("B1", "Formare frasi", "A Proclamação da República é um feriado nacional.", "Soggetto + é + predicato",
     "a proclamação / é / um feriado nacional → ___", instr="Forma una frase", size=20, gap=8)
e.ex("A2", "Formare frasi", "Deodoro foi o primeiro presidente do Brasil.", "Soggetto + verbo + predicato",
     "deodoro / foi / o primeiro presidente / do brasil → ___", instr="Forma una frase", size=20, gap=8)
e.ex("B1", "Formare frasi", "O Brasil virou uma república em 1889.", "Soggetto + verbo + oggetto + tempo",
     "o brasil / virou / uma república / em 1889 → ___", instr="Forma una frase", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · ESPORTE (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("ESPORTE · SPORT", "A Lucerna", "LIVELLO B1 · La settimana del calcio")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("As voltas decidem os finalistas da Copa", 37)
f.byline("Da redação da A Lucerna · Nível de leitura: B1")
f.para("A pergunta da semana é a mesma da semana passada — agora com respostas na ida: quem vai à final da Copa do Brasil? No domingo, 1º de novembro, o Grêmio venceu o Atlético-MG por 2 a 0, na Arena do Grêmio, com gols de Carlos Vinícius e Noriega. No mesmo dia, o Palmeiras venceu o Vasco por 1 a 0, no Nubank Parque, com gol de Maurício.")
f.para("A volta é neste fim de semana: no sábado, 7, às 18h, o Atlético-MG recebe o Grêmio na Arena MRV. O Atlético precisa vencer por três gols para passar direto; uma vitória por dois gols leva a decisão para os pênaltis. No domingo, 8, às 17h, o Vasco recebe o Palmeiras em São Januário: o Palmeiras passa com um empate; o Vasco precisa vencer por dois gols.")
f.para("A final é em jogo único, no dia 6 de dezembro, no Mané Garrincha, em Brasília. Até lá, o Brasileirão faz uma pausa: a rodada 35 só tem um jogo nesta semana — sábado, 14, às 18h30, Mirassol × Atlético-MG. Os outros nove jogos são nos dias 18 e 19, depois da Data Fifa.")
f.para("E a Data Fifa é no outro lado do mundo: a Seleção joga em Singapura — sábado, 14, às 7h15, contra o Japão, e terça, 17, às 7h, contra Singapura, no Estádio Nacional. O técnico Carlo Ancelotti convocou 26 jogadores para os dois últimos amistosos do ano. Os resultados da volta da Copa e os finalistas saem na próxima edição.")
f.gloss("a ida = la gara d’andata · a volta = la gara di ritorno · o gol = il gol · o pênalti = il rigore · a pausa = la pausa · o amistoso = l’amichevole.")
f.end_report()

# col 3: data box + e você (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 376, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 240, "OS JOGOS DA SEMANA", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "Ida, dom 1º — Grêmio 2 × 0 Atlético-MG; Palmeiras 1 × 0 Vasco. Volta, sáb 7, 18h — Atlético-MG × Grêmio, Arena MRV. Volta, dom 8, 17h — Vasco × Palmeiras, São Januário. Final — 6 de dezembro, Mané Garrincha, Brasília.", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 602
etvous = "E você? Para quem você torce na Copa do Brasil — e quem chega à final? Escreva duas frases em português e mande para a redação."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Quale squadra tifi nella Copa do Brasil, e chi andrà in finale? Scrivi due frasi e mandacele.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "E VOCÊ? · E TU?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Quale squadra tifi nella Copa do Brasil, e chi andrà in finale? Scrivi due frasi e mandacele.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "A SEMANA DO FUTEBOL · LA SETTIMANA DEL CALCIO", 26, "sans", True, OLIVE)
rows = [
    ("Dom 1º.11", "Copa do Brasil", "Grêmio 2 × 0 Atlético-MG — jogo de ida, Arena do Grêmio"),
    ("Dom 1º.11", "Copa do Brasil", "Palmeiras 1 × 0 Vasco — jogo de ida, Nubank Parque"),
    ("Sáb 7.11", "Copa do Brasil", "Atlético-MG × Grêmio, às 18h, Arena MRV — jogo de volta"),
    ("Dom 8.11", "Copa do Brasil", "Vasco × Palmeiras, às 17h, São Januário — jogo de volta"),
    ("Sáb 14.11", "Brasileirão", "Mirassol × Atlético-MG, às 18h30 — rodada 35 (os outros: 18 e 19)"),
    ("Sáb 14.11", "Seleção", "Japão × Brasil, às 7h15, em Singapura — amistoso (Singapura: 17, às 7h)"),
]
yy = ty + 16
for i, (d, t, m) in enumerate(rows):
    p.rect(MX, yy, RIGHT - MX, 44, fill="#f4efe0" if i % 2 == 0 else "#efe8d2")
    p.text(MX + 18, yy + 29, d, 20.5, "sans", True, BRICK)
    p.text(MX + 185, yy + 29, t, 20, "sans", False, GREY)
    p.text(MX + 430, yy + 29, m, 21, "serif", False, INK)
    yy += 44
tnote = "Nota: esta edição fechou em 2 de novembro. Os jogos de volta (7 e 8) ainda não tinham acontecido — os resultados e os finalistas saem na próxima edição."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EXERCÍCIOS · ESERCIZI PAGINA 4", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Risposte a pagina 8 · Livelli mescolati: cerca per numero", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A · COMPREENSÃO", 25)
e.bridge("Leggi pagina 4 e scegli la risposta giusta.")
e.ex("B1", "Scelta multipla", "A", "All’andata il Grêmio ha battuto l’Atlético-MG 2 a 0",
     "Na ida, Grêmio × Atlético-MG foi... A. 2 a 0 para o Grêmio · B. 1 a 0 para o Atlético · C. 0 a 0", size=20, gap=8)
e.ex("B1", "Scelta multipla", "B", "Il Palmeiras ha battuto il Vasco 1 a 0, gol di Maurício",
     "Na ida, Palmeiras × Vasco foi... A. 0 a 0 · B. 1 a 0 para o Palmeiras · C. 2 a 0 para o Vasco", size=20, gap=8)
e.ex("B1", "Scelta multipla", "A", "Il ritorno Atlético-MG × Grêmio è sabato 7 alle 18",
     "A volta de Atlético-MG × Grêmio é... A. no sábado 7, às 18h · B. no domingo 8 · C. no dia 1º", size=20, gap=8)
e.ex("B1", "Scelta multipla", "B", "La finale: una sola partita, il 6 dicembre, al Mané Garrincha",
     "A final da Copa do Brasil é... A. em dois jogos · B. em jogo único, no dia 6 de dezembro · C. no dia 15", size=20, gap=8)
e.ex("B1", "Scelta multipla", "A", "La 35ª giornata ha una sola partita questa settimana: Mirassol × Atlético-MG",
     "Na rodada 35, nesta semana... A. só há um jogo: Mirassol × Atlético-MG · B. há dez jogos · C. não há jogos", size=20, gap=8)
e.head("B · AS PALAVRAS", 25)
e.match_set("B1", "Abbinare il lessico",
            ["o gol", "a ida", "a volta", "o pênalti"],
            ["o segundo jogo de um confronto",
             "o ponto marcado na rede",
             "a cobrança da marca dos onze metros",
             "o primeiro jogo de um confronto"],
            ["b", "d", "a", "c"],
            ["gol = il punto segnato nella rete (b)", "ida = la prima partita di uno scontro (d)", "volta = la seconda partita di uno scontro (a)", "pênalti = il tiro dal dischetto (c)"],
            instr="Abbina")
e.head("C · COMPARATIVOS", 25)
e.bridge("Completa con la forma comparativa giusta tra parentesi.")
e.ex("B1", "Completare la frase", "mais", "2 > 0: mais",
     "Dois gols são ___ do que zero gols. (mais / menos)", instr="Completa", size=20, gap=8)
e.ex("B1", "Completare la frase", "mais", "3 > 2: mais",
     "Três gols são ___ do que dois gols. (mais / menos)", instr="Completa", size=20, gap=8)
e.ex("B1", "Completare la frase", "mais", "17 < 18: mais cedo",
     "17h é ___ cedo do que 18h. (mais / menos)", instr="Completa", size=20, gap=8)
e.ex("B1", "Completare la frase", "menos", "5 ore < 5,5 ore: menos",
     "Cinco horas são ___ do que cinco horas e meia. (mais / menos)", instr="Completa", size=20, gap=8)
e.head("D · O PRETÉRITO PERFEITO", 25)
e.bridge("Completa le frasi al passato (pretérito perfeito).")
e.ex("B1", "Completare la frase", "venceu", "vencer, passato, forma ele: venceu",
     "O Grêmio ___ (vencer) por 2 a 0.", instr="Completa", size=20, gap=8)
e.ex("B1", "Completare la frase", "marcaram", "marcar, passato, forma eles: marcaram",
     "Carlos Vinícius e Noriega ___ (marcar) os gols.", instr="Completa", size=20, gap=8)
e.ex("B1", "Completare la frase", "marcou", "marcar, passato, forma ele: marcou",
     "Maurício ___ (marcar) o gol do Palmeiras.", instr="Completa", size=20, gap=8)
e.ex("B1", "Completare la frase", "convocou", "convocar, passato, forma ele: convocou",
     "Ancelotti ___ (convocar) 26 jogadores.", instr="Completa", size=20, gap=8)
e.ex("B1", "Completare la frase", "foram", "ser, passato, plurale: foram",
     "Os jogos de ida ___ (ser) no domingo 1º.", instr="Completa", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-esporte.svg")
print("P4 saved, exercises so far:", len(REG))
