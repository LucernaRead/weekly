# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA　Cultura", "A Lucerna", "A2 → B1　Zumbi e Palmares: a história do 20 de novembro")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW)], 200, 1560, tag="P3-main")
f.title("Zumbi e Palmares: a história do 20 de novembro", 32)
f.byline("Da redação da A Lucerna　Nível de leitura: A2 → B1")
f.para("Em 20 de novembro de 1695, morre Zumbi dos Palmares, o último grande líder do Quilombo dos Palmares, em Alagoas. A data virou o Dia Nacional de Zumbi e da Consciência Negra: em 2011, a Lei nº 12.519 criou o dia e, em 2023, a Lei nº 14.759 fez dele feriado nacional.")
f.para("Palmares foi o maior quilombo do Brasil: no século XVII, milhares de africanos escravizados que fugiam formaram uma comunidade livre na Serra da Barriga. Zumbi nasceu em Palmares e defendeu o quilombo por anos contra as tropas coloniais.")
f.para("O que a data celebra? A resistência, a história e a cultura afro-brasileiras — a capoeira, o samba, a culinária, a literatura. E também a reflexão: o combate ao racismo continua, todos os dias.")
f.para("E por que 20 de novembro? Porque é o dia da morte de Zumbi. O Brasil lembra o líder para não esquecer a história: sem memória, não há futuro. Na página 2, o feriadão; na página 5, a semana dos jovens.")
f.gloss("o quilombo un villaggio di schiavi fuggiti · a resistência la resistenza · escravizado persona schiavizzata · o líder il leader · a memória la memoria · o combate la lotta.")
f.head("UM DIA, DOIS SENTIDOS", 25)
f.para("Um feriado é descanso — e memória. No dia 20, o Brasil descansa e lembra: a liberdade que Palmares defendeu é a mesma que o país celebra hoje, na capoeira, no samba e nas ruas.")
f.end_report()

# col 2: Zumbi painting (portrait, natural aspect 713x960 -> 340x458)
zx = COLX[2]
image(p, "zumbi.jpg", zx + 41, 200, 340, 458)
caption(p, zx, 200 + 458, CW,
        "Zumbi dos Palmares, em pintura de Antônio Parreiras (1927): o líder do quilombo, na mata, com a sua arma.",
        "Pintura: Antônio Parreiras / Wikimedia Commons — Domínio público")

# col 3: calendar box + e você + words box (sequential)
ix = COLX[3]
semana = ["Seg 16 — começa a semana do feriado.",
          "Ter 17 — Singapura × Brasil, às 7h.",
          "Sex 20 — o feriado da Consciência Negra.",
          "Sáb 21 — Palmeiras × Flamengo, às 16h30."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in semana) + 58  # fix1 (2026-11-11): +26 (was +32). Last line '16h30.' sat 15.6px BELOW the old bottom 525; +26 gives ink-bottom clearance ~+11px. Boxes below (ey3/ky3) derive from sh and shift down with it.
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "A SEMANA, DIA A DIA", 24, "sans", True, OLIVE)
yy3 += 52
for t in semana:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E você? No seu país, há um herói ou uma heroína que lutou pela liberdade? Escreva duas frases em português e mande para a redação."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Nel tuo paese, c'è un eroe o un'eroina che ha lottato per la libertà? Scrivi due frasi e inviale.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E VOCÊ?　Parla di te", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Nel tuo paese, c'è un eroe o un'eroina che ha lottato per la libertà? Scrivi due frasi e inviale.", 20, "sans", False, GREY, CW - 44, 1.42)
ky3 = ey3 + eh + 26
kb = "a consciência · o quilombo · a resistência · Zumbi · Palmares · «resistir» — seis palavras para um feriado de memória."
kh = 62 + len(wrap(kb, "serif", False, 21.5, CW - 44)) * 30.5 + 16
p.rect(ix, ky3, CW, kh, fill=BOX)
yy3 = ky3 + 16
p.text(ix + 22, yy3 + 26, "PALAVRAS DA MEMÓRIA", 22, "sans", True, OLIVE)
yy3 += 52
p.para(ix + 22, yy3 + 21, kb, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P3 col3 ends", ky3 + kh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EXERCÍCIOS　ESERCIZI DI PAGINA 3", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Risposte a pagina 8　I livelli sono misti — cerca le risposte per numero", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A　COMPREENSÃO", 25)
e.bridge("Leggi l'articolo di pagina 3 e scegli la risposta corretta.")
e.ex("A2", "Scelta multipla", "C", "Zumbi morì il 20 novembre 1695",
     "Zumbi dos Palmares morreu... A. em 1889 · B. em 2011 · C. em 20 de novembro de 1695", size=20, gap=8)
e.ex("A2", "Scelta multipla", "A", "Palmares era in Alagoas",
     "O Quilombo dos Palmares ficava... A. em Alagoas · B. no Rio · C. em São Paulo", size=20, gap=8)
e.ex("A2", "Scelta multipla", "B", "La legge del 2023 ha reso il 20 novembre festa nazionale",
     "A Lei nº 14.759, de 2023... A. criou o dia 20 · B. fez do dia 20 feriado nacional · C. acabou com o feriado", size=20, gap=8)
e.ex("A2", "Scelta multipla", "B", "Palmares era il quilombo più grande del Brasile",
     "Palmares foi... A. uma cidade portuguesa · B. o maior quilombo do Brasil · C. um time de futebol", size=20, gap=8)
e.ex("B1", "Scelta multipla", "A", "Questo giorno commemora la resistenza, la storia e la cultura afro-brasiliana",
     "O dia 20 celebra... A. a resistência e a cultura afro-brasileira · B. a Proclamação da República · C. o Enem", size=20, gap=8)
e.head("B　AS PALAVRAS DO TEXTO", 25)
e.bridge("Completa con le parole del riquadro.")
e.para("quilombo · resistência · escravizado · líder · memória · combate", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "Completa la frase", "quilombo", "quilombo = un villaggio di schiavi fuggiti",
     "Palmares foi o maior ___ do Brasil.", instr="Completa", size=20, gap=8)
e.ex("A2", "Completa la frase", "resistência", "resistência = la resistenza",
     "O dia 20 celebra a ___ do povo negro.", instr="Completa", size=20, gap=8)
e.ex("A2", "Completa la frase", "escravizados", "escravizado concordanza al plurale: escravizados",
     "Milhares de africanos ___ fugiam e formavam quilombos.", instr="Completa", size=20, gap=8)
e.ex("A2", "Completa la frase", "líder", "líder = il leader",
     "Zumbi foi o último grande ___ de Palmares.", instr="Completa", size=20, gap=8)
e.ex("A2", "Completa la frase", "memória", "memória = la memoria",
     "Sem ___ , não há futuro.", instr="Completa", size=20, gap=8)
e.ex("B1", "Completa la frase", "combate", "combate = la lotta",
     "O ___ ao racismo continua todos os dias.", instr="Completa", size=20, gap=8)
e.head("C　O PRETÉRITO PERFEITO", 25)
e.bridge("Completa al passato prossimo (pretérito perfeito).")
e.ex("B1", "Completa la frase", "morreu", "morrer, passato, forma di ele: morreu",
     "Zumbi ___ (morrer) em 20 de novembro de 1695.", instr="Completa", size=20, gap=8)
e.ex("B1", "Completa la frase", "nasceu", "nascer, passato, forma di ele: nasceu",
     "Zumbi ___ (nascer) em Palmares.", instr="Completa", size=20, gap=8)
e.ex("B1", "Completa la frase", "defendeu", "defender, passato, forma di ele: defendeu",
     "Zumbi ___ (defender) o quilombo por anos.", instr="Completa", size=20, gap=8)
e.ex("B1", "Completa la frase", "formaram", "formar, passato, forma di eles: formaram",
     "Os fugitivos ___ (formar) uma comunidade livre.", instr="Completa", size=20, gap=8)
e.head("D　CONSTRUA AS FRASES", 25)
e.bridge("Ordina le parole per formare frasi.")
e.ex("B1", "Costruzione di frasi", "O dia 20 de novembro é feriado nacional.", "soggetto + é + attributo",
     "o dia 20 / é / feriado nacional → ___", instr="Costruzione di frasi", size=20, gap=8)
e.ex("A2", "Costruzione di frasi", "Zumbi foi o líder de Palmares.", "soggetto + verbo + attributo",
     "zumbi / foi / o líder / de palmares → ___", instr="Costruzione di frasi", size=20, gap=8)
e.ex("B1", "Costruzione di frasi", "Palmares foi o maior quilombo do Brasil.", "soggetto + verbo + attributo",
     "palmares / foi / o maior quilombo / do brasil → ___", instr="Costruzione di frasi", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · ESPORTE (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("ESPORTE　Sport", "A Lucerna", "NÍVEL B1　A final da Copa do Brasil　La finale della Coppa del Brasile è decisa")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("Grêmio e Palmeiras decidem a Copa do Brasil", 32)
f.byline("Da redação da A Lucerna　Nível de leitura: B1")
f.para("A pergunta da semana passada tem resposta: quem vai à final da Copa do Brasil? No sábado, 7, o Grêmio empatou por 1 a 1 com o Atlético-MG, na Arena MRV, e passou com 3 a 1 no total: havia vencido a ida por 2 a 0, em Porto Alegre. Renan Lodi abriu o placar para o Atlético e Carlos Vinícius empatou para o Grêmio.")
f.para("No domingo, 8, o Vasco venceu o Palmeiras por 2 a 1, em São Januário — mas o Palmeiras havia vencido a ida por 1 a 0, e o agregado ficou em 2 a 2. Nos pênaltis, o Palmeiras venceu por 5 a 4 e foi à final. Foi a segunda semifinal decidida nos detalhes: um empate que bastou, e uma disputa de pênaltis.")
f.para("A final é em jogo único, no dia 6 de dezembro, no Mané Garrincha, em Brasília. O Grêmio busca o sexto título — e joga a décima final da sua história. O Palmeiras busca o quinto título da Copa do Brasil. Quem ganha, levanta a taça e garante vaga na próxima Libertadores.")
f.para("E o Brasileirão volta depois da pausa: a rodada 35 termina na quarta, 18, e na quinta, 19 — Cruzeiro × Palmeiras e Flamengo × Athletico-PR na quarta; Vasco × Internacional e São Paulo × Fluminense na quinta. No sábado, 21, às 16h30, Palmeiras × Flamengo: o jogo que pode decidir o título. E em Interlagos, no domingo 8, Lando Norris venceu o Grande Prêmio de São Paulo, com Verstappen em segundo e Hadjar em terceiro; a Mercedes garantiu o título de construtores.")
f.gloss("o agregado il punteggio complessivo · os pênaltis la serie dei rigori · a decisão la finale · o título titolo · a pausa la pausa · a taça il trofeo.")
f.end_report()

# col 3: data box + e você (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 376, fill=BOX)
p.text(bx + 22, 240, "OS FINALISTAS", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "Ida, dom 1º — Grêmio 2 × 0 Atlético-MG; Palmeiras 1 × 0 Vasco. Volta, sáb 7 — Atlético-MG 1 × 1 Grêmio (total 3 × 1). Volta, dom 8 — Vasco 2 × 1 Palmeiras (total 2 × 2; pênaltis 5 × 4). Final — 6 de dezembro, Mané Garrincha, Brasília.", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 602
etvous = "E você? Na final, Grêmio ou Palmeiras — para quem você torce? Escreva duas frases em português e mande para a redação."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("In finale, tifi Grêmio o Palmeiras? Scrivi due frasi e inviale.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "E VOCÊ?　Parla di te", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "In finale, tifi Grêmio o Palmeiras? Scrivi due frasi e inviale.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "A SEMANA DO FUTEBOL　La settimana del calcio", 26, "sans", True, OLIVE)
rows = [
    ("Sáb 7.11", "Copa do Brasil", "Atlético-MG 1 × 1 Grêmio — a volta; o Grêmio passa com 3 × 1 no total"),
    ("Dom 8.11", "Copa do Brasil", "Vasco 2 × 1 Palmeiras — a volta; nos pênaltis, 5 × 4 para o Palmeiras"),
    ("Dom 8.11", "Fórmula 1", "Norris vence em Interlagos; Verstappen é 2º, Hadjar é 3º"),
    ("Qua 18.11", "Brasileirão", "Cruzeiro × Palmeiras, às 20h30 — rodada 35; Flamengo × Athletico-PR, às 20h30"),
    ("Qui 19.11", "Brasileirão", "Vasco × Internacional, às 19h30; São Paulo × Fluminense, às 21h30"),
    ("Sáb 21.11", "Brasileirão", "Palmeiras × Flamengo, às 16h30, Nubank Parque — o jogo do título"),
]
yy = ty + 16
for i, (d, t, m) in enumerate(rows):
    p.rect(MX, yy, RIGHT - MX, 44, fill="#f4efe0" if i % 2 == 0 else "#efe8d2")
    p.text(MX + 18, yy + 29, d, 20.5, "sans", True, OLIVE)
    p.text(MX + 185, yy + 29, t, 20, "sans", False, GREY)
    p.text(MX + 430, yy + 29, m, 21, "serif", False, INK)
    yy += 44
tnote = "Nota: esta edição fechou em 10 de novembro. Os jogos de 14 a 22 ainda não tinham acontecido — os resultados saem na próxima edição."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EXERCÍCIOS　ESERCIZI DI PAGINA 4", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Risposte a pagina 8　I livelli sono misti — cerca le risposte per numero", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A　COMPREENSÃO", 25)
e.bridge("Leggi l'articolo di pagina 4 e scegli la risposta corretta.")
e.ex("B1", "Scelta multipla", "A", "Al ritorno, il Grêmio ha pareggiato 1–1 con l'Atlético-MG e si è qualificato 3–1 nel complessivo",
     "Na volta, Atlético-MG × Grêmio foi... A. 1 a 1, e o Grêmio passou com 3 a 1 no total · B. 2 a 0 para o Atlético · C. 0 a 0", size=20, gap=8)
e.ex("B1", "Scelta multipla", "B", "Il Vasco ha vinto il ritorno 2–1, ma il complessivo era 2–2 e il Palmeiras si è qualificato ai rigori",
     "Na volta, Vasco × Palmeiras foi... A. 1 a 0 para o Palmeiras · B. 2 a 1 para o Vasco, e o Palmeiras passou nos pênaltis · C. 0 a 0", size=20, gap=8)
e.ex("B1", "Scelta multipla", "B", "Rigori 5–4: il Palmeiras si qualifica",
     "Nos pênaltis, o Palmeiras venceu por... A. 4 a 3 · B. 5 a 4 · C. 6 a 5", size=20, gap=8)
e.ex("B1", "Scelta multipla", "B", "La finale si gioca in gara unica il 6 dicembre, al Mané Garrincha",
     "A final da Copa do Brasil é... A. em dois jogos · B. em jogo único, no dia 6 de dezembro · C. no dia 15", size=20, gap=8)
e.ex("B1", "Scelta multipla", "A", "Norris ha vinto il Gran Premio di San Paolo, Verstappen secondo",
     "O Grande Prêmio de São Paulo foi vencido por... A. Lando Norris · B. Max Verstappen · C. Isack Hadjar", size=20, gap=8)
e.head("B　AS PALAVRAS", 25)
e.match_set("B1", "Abbinare il lessico",
            ["o agregado", "a volta", "os pênaltis", "a taça"],
            ["o segundo jogo de um confronto",
             "o placar dos dois jogos somados",
             "o prêmio do campeão",
             "a disputa da marca dos onze metros"],
            ["b", "a", "d", "c"],
            ["agregado=i due punteggi sommati b", "volta=la partita di ritorno di un confronto a", "pênaltis=la serie dei rigori d", "taça=il trofeo del campione c"],
            instr="Abbina")
e.head("C　COMPARATIVOS", 25)
e.bridge("Completa con la forma comparativa corretta tra parentesi.")
e.ex("B1", "Completa la frase", "mais", "3 > 1:mais",
     "Três gols são ___ do que um gol. (mais / menos)", instr="Completa", size=20, gap=8)
e.ex("B1", "Completa la frase", "mais", "5 > 4:mais",
     "Cinco pênaltis são ___ do que quatro. (mais / menos)", instr="Completa", size=20, gap=8)
e.ex("B1", "Completa la frase", "mais", "16:30 < 17:00:mais cedo",
     "16h30 é ___ cedo do que 17h. (mais / menos)", instr="Completa", size=20, gap=8)
e.ex("B1", "Completa la frase", "menos", "2 giorni < 7 giorni: menos",
     "Dois dias são ___ do que uma semana. (mais / menos)", instr="Completa", size=20, gap=8)
e.head("D　O PRETÉRITO PERFEITO", 25)
e.bridge("Completa le frasi al passato prossimo (pretérito perfeito).")
e.ex("B1", "Completa la frase", "empatou", "empatar, passato, forma di ele: empatou",
     "O Grêmio ___ (empatar) por 1 a 1.", instr="Completa", size=20, gap=8)
e.ex("B1", "Completa la frase", "venceu", "vencer, passato, forma di ele: venceu",
     "O Vasco ___ (vencer) por 2 a 1.", instr="Completa", size=20, gap=8)
e.ex("B1", "Completa la frase", "abriu", "abrir, passato, forma di ele: abriu",
     "Renan Lodi ___ (abrir) o placar.", instr="Completa", size=20, gap=8)
e.ex("B1", "Completa la frase", "garantiu", "garantir, passato, forma di ela: garantiu",
     "A Mercedes ___ (garantir) o título de construtores.", instr="Completa", size=20, gap=8)
e.ex("B1", "Completa la frase", "foram", "ser passato, plurale: foram",
     "Os jogos de volta ___ (ser) no fim de semana.", instr="Completa", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-esporte.svg")
print("P4 saved, exercises so far:", len(REG))
