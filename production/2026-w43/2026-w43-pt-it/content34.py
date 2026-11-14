# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA　CULTURA", "A Lucerna", "A2 → B1　A volta da guitarra　Il ritorno della chitarra")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("A guitarra voltou: o som que o Brasil procura", 32)
f.byline("Da redação da A Lucerna　Nível de leitura: A2 → B1")
f.para("Durante muitos anos, a guitarra perdeu espaço no Brasil. Um estudo publicado nesta semana, com 22 anos de dados do Google, conta a história inteira: as buscas por «guitarra» caíram 74% entre 2004 e 2021. Ano após ano, o instrumento elétrico ficava mais silencioso.")
f.para("Mas a história mudou. Desde 2021, as buscas por guitarra crescem todos os anos: no total, já subiram 53%. Em 2026, a guitarra chegou a 75% do volume de buscas do violão — o instrumento mais brasileiro de todos. A guitarra elétrica e o violão acústico, outra vez lado a lado.")
f.para("Por quê? Os jovens descobrem bandas antigas nos vídeos curtos, compram a primeira guitarra e aprendem com aulas na internet. E há o ritual da semana: na sexta-feira, o país inteiro assiste ao debate na TV. No Brasil, a música e a televisão moram na mesma casa: a família se reúne, comenta, canta junto.")
f.gloss("a busca = la ricerca · cair = scendere · crescer = crescere · o volume = il volume · lado a lado = fianco a fianco.")
f.head("DOIS INSTRUMENTOS, UM PAÍS", 24)
f.para("O violão é o instrumento da roda de amigos, da praia e do samba. A guitarra é o som do rock e dos grandes shows. Nesta semana, os dois dividem a mesma notícia: o Brasil voltou a procurar música — e a procurar com as mãos.")
f.para("Na página 5, outra votação famosa da semana: a enquete de A Fazenda. Mas antes, uma pergunta para você, leitor: qual é o instrumento da sua vida?")
f.end_report()

# col 3: violão image + facts + e você + django image (sequential)
ix = COLX[3]
image(p, "violao.jpg", ix, 200, CW, 250)
cy3 = caption(p, ix, 450, CW, "Um músico toca violão na Praça do Marco Zero, no Recife: o violão é o instrumento mais brasileiro — e, em 2026, a guitarra chegou a 75% das suas buscas.",
              "Foto: Wikimedia Commons — CC0")
facts = ["−74%: a queda das buscas por «guitarra» entre 2004 e 2021.",
         "+53%: o crescimento acumulado das buscas desde 2021.",
         "75%: o volume da guitarra comparado ao do violão em 2026."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "A GUITARRA EM NÚMEROS", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E você? Você toca algum instrumento — ou quer aprender? Escreva duas frases em português e mande para a redação."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Suoni uno strumento — o vuoi imparare? Scrivi due frasi e mandale.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E VOCÊ?　E TU?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Suoni uno strumento — o vuoi imparare? Scrivi due frasi e mandale.", 20, "sans", False, GREY, CW - 44, 1.42)
ay3 = ey3 + eh + 22
image(p, "django.jpg", ix, ay3, CW, 150)
acy = caption(p, ix, ay3 + 150, CW, "Django Reinhardt (1910–1953), um dos maiores guitarristas da história, em foto de William P. Gottlieb: a guitarra que o mundo procura outra vez.",
              "Foto: William P. Gottlieb / Wikimedia Commons — domínio público")
print("P3 col3 ends", acy)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EXERCÍCIOS　ESERCIZI", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Risposte a pagina 8　Esercizi mescolati per livello: cerca il numero", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A　COMPREENSÃO", 25)
e.expl("Leggi l'articolo di pagina 3 e scegli la risposta giusta.")
e.ex("A2", "单选", "B", "tra il 2004 e il 2021 le ricerche sono scese del 74%",
     "Entre 2004 e 2021, as buscas por «guitarra»... A. cresceram 53% · B. caíram 74% · C. ficaram iguais", size=20, gap=8)
e.ex("A2", "单选", "A", "dal 2021 crescono ogni anno",
     "Desde 2021, as buscas por guitarra... A. crescem todos os anos · B. caem todos os anos · C. pararam", size=20, gap=8)
e.ex("B1", "单选", "C", "nel 2026, il 75% del volume del violão",
     "Em 2026, a guitarra chegou a... A. 53% do violão · B. 100% do violão · C. 75% do volume do violão", size=20, gap=8)
e.ex("B1", "单选", "B", "i giovani scoprono vecchie band nei video brevi",
     "Os jovens descobrem bandas antigas... A. no rádio do carro · B. nos vídeos curtos · C. nos jornais de papel", size=20, gap=8)
e.ex("B1", "单选", "A", "il violão è lo strumento «più brasiliano»",
     "O instrumento «mais brasileiro de todos» é... A. o violão · B. a guitarra · C. o piano", size=20, gap=8)
e.head("B　AS PALAVRAS DO TEXTO", 25)
e.expl("Completa con le parole del riquadro.")
e.para("guitarra · violão · busca · volume · banda · instrumento", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "完成句子", "guitarra", "guitarra elétrica = la chitarra elettrica",
     "A ___ elétrica é o som do rock.", instr="Completa", size=20, gap=8)
e.ex("A2", "完成句子", "violão", "violão acústico = la chitarra acustica",
     "O ___ acústico é o instrumento da roda de amigos.", instr="Completa", size=20, gap=8)
e.ex("B1", "完成句子", "busca", "busca = la ricerca",
     "Uma ___ no Google mostra o que o país quer saber.", instr="Completa", size=20, gap=8)
e.ex("B1", "完成句子", "volume", "volume de buscas = il volume di ricerche",
     "O ___ de buscas da guitarra cresce desde 2021.", instr="Completa", size=20, gap=8)
e.ex("A2", "完成句子", "banda", "banda = la band, il gruppo",
     "Os jovens descobrem uma ___ antiga nos vídeos.", instr="Completa", size=20, gap=8)
e.ex("B1", "完成句子", "instrumento", "instrumento = lo strumento",
     "O piano também é um ___ musical.", instr="Completa", size=20, gap=8)
e.head("C　O PRETÉRITO PERFEITO", 25)
e.expl("Completa al pretérito perfeito (passato remoto).")
e.ex("B1", "完成句子", "caíram", "cair, passato remoto (elas): caíram",
     "As buscas ___ (cair) 74% entre 2004 e 2021.", instr="Completa", size=20, gap=8)
e.ex("B1", "完成句子", "cresceram", "crescer, passato remoto (elas): cresceram",
     "Depois de 2021, as buscas ___ (crescer) todos os anos.", instr="Completa", size=20, gap=8)
e.ex("B1", "完成句子", "chegou", "chegar, passato remoto (ela): chegou",
     "Em 2026, a guitarra ___ (chegar) a 75% do violão.", instr="Completa", size=20, gap=8)
e.ex("B1", "完成句子", "mudou", "mudar, passato remoto (ela): mudou",
     "A história ___ (mudar) depois de 2021.", instr="Completa", size=20, gap=8)
e.head("D　CONSTRUA AS FRASES", 25)
e.expl("Forma frasi corrette con le parole date.")
e.ex("B1", "造句", "A guitarra voltou a crescer.", "soggetto + voltou a + infinito",
     "a guitarra / voltou / a crescer → ___", instr="Forma la frase", size=20, gap=8)
e.ex("A2", "造句", "O violão é o instrumento mais brasileiro.", "soggetto + é + predicato",
     "o violão / é / o instrumento mais brasileiro → ___", instr="Forma la frase", size=20, gap=8)
e.ex("B1", "造句", "O Brasil voltou a procurar música.", "soggetto + voltou a + infinito",
     "o Brasil / voltou / a procurar música → ___", instr="Forma la frase", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · ESPORTE (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("ESPORTE　SPORT", "A Lucerna", "NÍVEL B1　O futebol da semana　La settimana del calcio")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("Semana de decisão: adeus à Sul-Americana, vem aí a Copa do Brasil", 32)
f.byline("Da redação da A Lucerna　Nível de leitura: B1")
f.para("A terça-feira foi de festa e de lágrimas no Maracanã. O Vasco jogou a volta da semifinal da Copa Sul-Americana contra o Boca Juniors. Na ida, em Buenos Aires, o Vasco tinha vencido por 1 a 0. Mas na volta, o Boca fez 3 a 1 — e o Vasco está fora da competição.")
f.para("Os gols contam a noite: Di Lollo abriu o placar e Merentiel ampliou ainda no primeiro tempo. Puma Rodríguez diminuiu para o Vasco no segundo tempo, mas Paredes, no fim, fechou o 3 a 1. No total dos dois jogos: 3 a 2 para o Boca. Mais de 66 mil torcedores estavam no estádio.")
f.para("Agora, o Vasco pensa na Copa do Brasil. Na terça-feira, a CBF confirmou a arbitragem das semifinais: Anderson Daronco apita Palmeiras × Vasco, e Davi Lacerda comanda Grêmio × Atlético-MG. Os jogos de ida são no domingo, 1º de novembro: o futebol brasileiro não para — nem na semana da eleição.")
f.gloss("a ida = l'andata · a volta = il ritorno · o placar = il risultato · ampliar = allargare il vantaggio · a arbitragem = gli arbitri.")
f.end_report()

# col 3: data box + e você (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 376, fill=BOX)
p.text(bx + 22, 240, "O JOGO EM NÚMEROS", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "Vasco 1 × 3 Boca Juniors · Maracanã · terça-feira, 20 de outubro. Ida: Boca 0 × 1 Vasco. Total (agregado): 3 × 2 para o Boca. Público: 66.026 torcedores. O Boca está na final da Sul-Americana.", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 602
etvous = "E você? Para quem você torce? Escreva duas frases em português e mande para a redação."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Per quale squadra fai il tifo? Scrivi due frasi e mandale.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "E VOCÊ?　E TU?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Per quale squadra fai il tifo? Scrivi due frasi e mandale.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "A SEMANA DO FUTEBOL　LA SETTIMANA DEL CALCIO", 26, "sans", True, OLIVE)
rows = [
    ("Ter 20.10", "Sul-Americana", "Vasco 1 × 3 Boca Juniors — o Vasco está eliminado"),
    ("Sáb 24.10", "Brasileirão", "Vasco × Corinthians, em São Januário, às 18h30"),
    ("Dom 1º.11", "Copa do Brasil", "Palmeiras × Vasco, às 16h — ida da semifinal"),
    ("Dom 1º.11", "Copa do Brasil", "Grêmio × Atlético-MG, às 18h30 — ida da semifinal"),
    ("Sáb 7.11", "Copa do Brasil", "Atlético-MG × Grêmio, às 18h — jogo de volta"),
    ("Dom 8.11", "Copa do Brasil", "Vasco × Palmeiras, às 17h — jogo de volta"),
]
yy = ty + 16
for i, (d, t, m) in enumerate(rows):
    p.rect(MX, yy, RIGHT - MX, 44, fill="#f4efe0" if i % 2 == 0 else "#efe8d2")
    p.text(MX + 18, yy + 29, d, 20.5, "sans", True, OLIVE)
    p.text(MX + 185, yy + 29, t, 20, "sans", False, GREY)
    p.text(MX + 430, yy + 29, m, 21, "serif", False, INK)
    yy += 44
tnote = "Atenção: as semifinais da Copa do Brasil são em novembro. Nesta semana, a CBF confirmou só a arbitragem — os jogos ainda não começaram."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EXERCÍCIOS　ESERCIZI", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Risposte a pagina 8　Esercizi mescolati per livello: cerca il numero", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A　COMPREENSÃO", 25)
e.expl("Leggi l'articolo di pagina 4 e scegli la risposta giusta.")
e.ex("B1", "单选", "A", "al ritorno il Boca vince 3 a 1",
     "O jogo de volta, no Maracanã, terminou... A. Vasco 1 × 3 Boca · B. Vasco 3 × 1 Boca · C. 1 × 1", size=20, gap=8)
e.ex("B1", "单选", "B", "all'andata il Vasco vince 1 a 0",
     "No jogo de ida, em Buenos Aires... A. o Boca venceu por 1 a 0 · B. o Vasco venceu por 1 a 0 · C. foi 0 a 0", size=20, gap=8)
e.ex("B1", "单选", "C", "totale 3 a 2: il Boca è in finale",
     "No total dos dois jogos (agregado), o placar foi... A. 2 × 2 · B. 4 × 1 para o Vasco · C. 3 × 2 para o Boca", size=20, gap=8)
e.ex("B1", "单选", "B", "le semifinali di andata della Copa do Brasil: il 1º novembre",
     "Os jogos de ida da Copa do Brasil são... A. nesta semana · B. no dia 1º de novembro · C. em dezembro", size=20, gap=8)
e.ex("B1", "单选", "A", "Daronco arbitra Palmeiras × Vasco",
     "Quem apita Palmeiras × Vasco? A. Anderson Daronco · B. Davi Lacerda · C. César Tralli", size=20, gap=8)
e.head("B　AS PALAVRAS", 25)
e.match_set("B1", "词汇配对",
            ["o placar", "a ida", "a volta", "o agregado"],
            ["a soma dos resultados dos dois jogos",
             "o primeiro jogo de um confronto",
             "o resultado de um jogo, com os gols",
             "o segundo jogo de um confronto"],
            ["c", "b", "d", "a"],
            ["placar = il risultato, con i gol: c", "ida = la prima partita del confronto: b", "volta = la seconda partita del confronto: d", "agregado = la somma delle due partite: a"],
            instr="Abbina")
e.head("C　COMPARATIVOS", 25)
e.expl("Completa con la forma comparativa corretta tra parentesi.")
e.ex("B1", "完成句子", "mais", "al ritorno 4 gol, all'andata 1: mais",
     "A volta foi ___ emocionante do que a ida: quatro gols contra um. (mais / menos)", instr="Completa", size=20, gap=8)
e.ex("B1", "完成句子", "maior", "66.026 > 66.000: maior",
     "O público foi ___ do que 66 mil torcedores: eram 66.026. (maior / menor)", instr="Completa", size=20, gap=8)
e.ex("B1", "完成句子", "melhor", "il comparativo di bem è melhor (3–1 contro 0–1)",
     "O Boca jogou ___ na volta do que na ida. (melhor / pior)", instr="Completa", size=20, gap=8)
e.ex("B1", "完成句子", "menos", "Vasco 1 gol, Boca 3: menos",
     "O Vasco marcou ___ gols na volta (1) do que o Boca (3). (mais / menos)", instr="Completa", size=20, gap=8)
e.head("D　O PRETÉRITO PERFEITO", 25)
e.expl("Completa le frasi al pretérito perfeito (passato remoto).")
e.ex("B1", "完成句子", "venceu", "vencer, passato remoto (ele): venceu",
     "Na ida, o Vasco ___ (vencer) por 1 a 0.", instr="Completa", size=20, gap=8)
e.ex("B1", "完成句子", "perdeu", "perder, passato remoto (ele): perdeu",
     "Na volta, o Vasco ___ (perder) por 3 a 1.", instr="Completa", size=20, gap=8)
e.ex("B1", "完成句子", "fez", "fazer, passato remoto irregolare: fez",
     "O Boca ___ (fazer) três gols no Maracanã.", instr="Completa", size=20, gap=8)
e.ex("B1", "完成句子", "diminuiu", "diminuir, passato remoto (ele): diminuiu",
     "Puma Rodríguez ___ (diminuir) para o Vasco no segundo tempo.", instr="Completa", size=20, gap=8)
e.ex("B1", "完成句子", "confirmou", "confirmar, passato remoto (ela): confirmou",
     "Na terça-feira, a CBF ___ (confirmar) a arbitragem das semifinais.", instr="Completa", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-esporte.svg")
print("P4 saved, exercises so far:", len(REG))
