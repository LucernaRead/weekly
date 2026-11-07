# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-pt-nl/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA · CULTUUR", "A Lucerna", "A2 → B1 · Finados: o dia da memória · Finados: de dag van de herinnering")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("Finados: o dia em que o Brasil lembra", 37)
f.byline("Da redação da A Lucerna · Nível de leitura: A2 → B1")
f.para("No dia 2 de novembro, o Brasil para para lembrar. Finados — o Dia dos Fiéis Defuntos — é o dia em que as famílias visitam os cemitérios do país inteiro, do pequeno cemitério do interior ao grande cemitério da capital.")
f.para("O ritual é simples e antigo: limpar o túmulo, levar flores — sobretudo crisântemos, a flor de Finados —, acender uma vela e rezar. Nas igrejas e nos cemitérios, há missas o dia inteiro. Não é festa: é um dia calmo, de silêncio, de encontro e de memória.")
f.para("Cada família tem o seu jeito: uns levam a flor preferida de quem partiu, outros levam a comida de que ele gostava, outros só ficam um pouco em silêncio. O que não muda é o centro do dia: lembrar é um jeito de continuar perto.")
f.para("E Finados tem um vizinho famoso: no sábado, 31 de outubro, foi Halloween, com fantasias e doces. Dois dias, dois jeitos de olhar para a morte: um de festa, outro de silêncio — e os dois cabem na mesma semana.")
f.gloss("o túmulo = het graf · a flor = de bloem · acender = aansteken · rezar = bidden · o silêncio = de stilte · a lembrança = de herinnering.")
f.head("DOIS DIAS, DOIS JEITOS", 25)
f.para("Halloween é barulho, fantasia e doce. Finados é silêncio, flor e vela. O Brasil vive os dois em três dias — e o português aprende os dois vocabulários: «doce ou travessura?» de um lado, «descanse em paz» do outro.")
f.para("Na página 2, o feriadão inteiro. Na página 5, a reta final dos jovens. Mas antes, uma pergunta para você, leitor: na sua cultura, como se lembram os mortos?")
f.end_report()

# col 3: calendar box + e você + words box (sequential)
ix = COLX[3]
semana = ["Seg 2 — Finados, feriado nacional.",
          "Ter 3 — as assembleias estaduais voltam do recesso.",
          "Sáb 7 — Atlético-MG × Grêmio, a volta da semifinal.",
          "Dom 8 — Enem, dia 1; Vasco × Palmeiras, a volta."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in semana) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "A SEMANA, DIA A DIA", 24, "sans", True, OLIVE)
yy3 += 52
for t in semana:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E você? Na sua cultura, como se lembram os mortos? Escreva duas frases em português e mande para a redação."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Hoe herdenken mensen in jouw cultuur de doden? Schrijf twee zinnen en stuur ze op.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E VOCÊ? · EN JIJ?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Hoe herdenken mensen in jouw cultuur de doden? Schrijf twee zinnen en stuur ze op.", 20, "sans", False, GREY, CW - 44, 1.42)
ky3 = ey3 + eh + 26
kb = "o túmulo · a vela · o crisântemo · a missa · a lembrança · «descanse em paz» — seis palavras para um dia de silêncio."
kh = 62 + len(wrap(kb, "serif", False, 21.5, CW - 44)) * 30.5 + 16
p.rect(ix, ky3, CW, kh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ky3 + 16
p.text(ix + 22, yy3 + 26, "PALAVRAS DE FINADOS", 22, "sans", True, OLIVE)
yy3 += 52
p.para(ix + 22, yy3 + 21, kb, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P3 col3 ends", ky3 + kh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EXERCÍCIOS · OEFENINGEN", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antwoorden op pagina 8 · niveaus gemengd: zoek op nummer", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · COMPREENSÃO", 25)
e.expl("Uitleg — Lees het artikel op pagina 3 en kies het juiste antwoord.")
e.ex("A2", "Meerkeuze", "B", "Finados is een dag van herinnering en stilte",
     "Finados é... A. um dia de festa e fantasia · B. o dia da memória e do silêncio · C. um dia de votação", size=20, gap=8)
e.ex("A2", "Meerkeuze", "B", "Families nemen bloemen mee naar begraafplaatsen, vooral chrysanten",
     "As famílias levam aos cemitérios... A. presentes de Natal · B. flores, sobretudo crisântemos · C. fogos de artifício", size=20, gap=8)
e.ex("A2", "Meerkeuze", "B", "In kerken en op begraafplaatsen zijn er de hele dag missen",
     "Nas igrejas e nos cemitérios, há... A. shows de rock · B. missas o dia inteiro · C. feiras de livros", size=20, gap=8)
e.ex("A2", "Meerkeuze", "C", "Halloween was op zaterdag 31 oktober",
     "Halloween foi... A. no domingo 8 · B. na segunda 2 · C. no sábado, 31 de outubro", size=20, gap=8)
e.ex("B1", "Meerkeuze", "A", "Herinneren is een manier om dichtbij te blijven",
     "O texto diz que lembrar é... A. um jeito de continuar perto · B. uma festa · C. uma votação", size=20, gap=8)
e.head("B · AS PALAVRAS DO TEXTO", 25)
e.expl("Uitleg — Vul de woorden uit het kader in.")
e.para("túmulo · vela · crisântemo · missa · silêncio · lembrança", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "Voltooi de zin", "túmulo", "túmulo = het graf",
     "As famílias limpam o ___.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Voltooi de zin", "vela", "vela = de kaars",
     "Acendem uma ___ em memória.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Voltooi de zin", "crisântemo", "crisântemo = de chrysant",
     "O ___ é a flor de Finados.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Voltooi de zin", "missa", "missa = de mis",
     "Na igreja, há ___ o dia inteiro.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Voltooi de zin", "silêncio", "silêncio = de stilte",
     "Finados é um dia de ___.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "lembrança", "lembrança = de herinnering",
     "A ___ volta à mesa.", instr="Vul in", size=20, gap=8)
e.head("C · O PRETÉRITO PERFEITO", 25)
e.expl("Uitleg — Vul de verleden tijd (pretérito perfeito) in.")
e.ex("B1", "Voltooi de zin", "visitaram", "visitar, verleden tijd (elas): visitaram",
     "As famílias ___ (visitar) os cemitérios.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "levaram", "levar, verleden tijd (elas): levaram",
     "Elas ___ (levar) flores.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "foi", "ser, verleden tijd (ele): foi",
     "O sábado ___ (ser) de Halloween.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "viveu", "viver, verleden tijd (ele): viveu",
     "O Brasil ___ (viver) dois dias diferentes.", instr="Vul in", size=20, gap=8)
e.head("D · CONSTRUA AS FRASES", 25)
e.expl("Uitleg — Zet de woorden in de juiste volgorde.")
e.ex("B1", "Bouw de zin", "Finados é um dia de silêncio.", "Onderwerp + é + gezegde",
     "finados / é / um dia de silêncio → ___", instr="Bouw de zin", size=20, gap=8)
e.ex("A2", "Bouw de zin", "As famílias levam flores ao cemitério.", "Onderwerp + werkwoord + voorwerp + plaats",
     "as famílias / levam / flores / ao cemitério → ___", instr="Bouw de zin", size=20, gap=8)
e.ex("B1", "Bouw de zin", "O Brasil lembra os seus mortos.", "Onderwerp + werkwoord + voorwerp",
     "o Brasil / lembra / os seus mortos → ___", instr="Bouw de zin", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · ESPORTE (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("ESPORTE · SPORT", "A Lucerna", "NÍVEL B1 · O futebol da semana · de voetbalweek")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("Semana de decisão: quem vai à final da Copa do Brasil?", 37)
f.byline("Da redação da A Lucerna · Nível de leitura: B1")
f.para("A pergunta da semana é simples: quem vai à final da Copa do Brasil? Quatro times, dois jogos de volta, um fim de semana. No sábado, 7, às 18h, o Atlético-MG recebe o Grêmio na Arena MRV. No domingo, 8, às 17h, o Vasco recebe o Palmeiras em São Januário.")
f.para("Os jogos de ida foram no domingo, 1º de novembro: Palmeiras × Vasco, às 16h, e Grêmio × Atlético-MG, às 18h30. Os quatro times chegam à volta com tudo em aberto: quem vencer no total dos dois jogos vai à final.")
f.para("E o Brasileirão não para: a rodada 34 tem jogo de segunda a sexta, de 2 a 6 de novembro. É a reta final do campeonato: cada ponto vale uma posição, cada gol vale uma história. No fim de semana, o país para para a Copa — e volta para o Brasileirão na semana que vem.")
f.para("Ontem, domingo 1º, já foi de Copa: os jogos de ida abriram as semifinais. Nesta semana, a volta fecha a conta. Sábado e domingo, o Brasil tem dois horários marcados: 18h e 17h.")
f.gloss("a ida = de heenwedstrijd · a volta = de return · o finalista = de finalist · a decisão = de beslissing · a rodada = de speelronde.")
f.end_report()

# col 3: data box + e você (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 376, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 240, "OS JOGOS DA SEMANA", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "Sáb 7, 18h — Atlético-MG × Grêmio, Arena MRV (volta). Dom 8, 17h — Vasco × Palmeiras, São Januário (volta). Ida, dom 1º — Palmeiras × Vasco, 16h; Grêmio × Atlético-MG, 18h30.", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 602
etvous = "E você? Para quem você torce na Copa do Brasil? Escreva duas frases em português e mande para a redação."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Voor welk team ben jij in de Copa do Brasil? Schrijf twee zinnen en stuur ze op.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "E VOCÊ? · EN JIJ?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Voor welk team ben jij in de Copa do Brasil? Schrijf twee zinnen en stuur ze op.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "A SEMANA DO FUTEBOL · DE VOETBALKALENDER", 26, "sans", True, OLIVE)
rows = [
    ("Seg 2 – Sex 6", "Brasileirão", "Rodada 34: um jogo por dia, de segunda a sexta"),
    ("Dom 1º.11", "Copa do Brasil", "Palmeiras × Vasco, às 16h — jogo de ida (já jogado)"),
    ("Dom 1º.11", "Copa do Brasil", "Grêmio × Atlético-MG, às 18h30 — jogo de ida (já jogado)"),
    ("Sáb 7.11", "Copa do Brasil", "Atlético-MG × Grêmio, às 18h, Arena MRV — jogo de volta"),
    ("Dom 8.11", "Copa do Brasil", "Vasco × Palmeiras, às 17h, São Januário — jogo de volta"),
    ("Ter 3.11", "Fora do campo", "As assembleias estaduais voltam do recesso eleitoral"),
]
yy = ty + 16
for i, (d, t, m) in enumerate(rows):
    p.rect(MX, yy, RIGHT - MX, 44, fill="#f4efe0" if i % 2 == 0 else "#efe8d2")
    p.text(MX + 18, yy + 29, d, 20.5, "sans", True, BRICK)
    p.text(MX + 185, yy + 29, t, 20, "sans", False, GREY)
    p.text(MX + 430, yy + 29, m, 21, "serif", False, INK)
    yy += 44
tnote = "Atenção: os jogos de ida foram no domingo 1º; os de volta decidem os finalistas neste fim de semana. Os resultados da volta saem na próxima edição."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EXERCÍCIOS · OEFENINGEN", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antwoorden op pagina 8 · niveaus gemengd: zoek op nummer", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A · COMPREENSÃO", 25)
e.expl("Uitleg — Lees het artikel op pagina 4 en kies het juiste antwoord.")
e.ex("B1", "Meerkeuze", "A", "De return Atlético-MG × Grêmio is op zaterdag 7 november om 18h",
     "A volta de Atlético-MG × Grêmio é... A. no sábado 7, às 18h · B. no domingo 8 · C. no dia 1º", size=20, gap=8)
e.ex("B1", "Meerkeuze", "B", "De return Vasco × Palmeiras is op zondag 8 november om 17h, in São Januário",
     "Vasco × Palmeiras, a volta, é... A. no sábado, na Arena MRV · B. no domingo 8, às 17h, em São Januário · C. na segunda 2", size=20, gap=8)
e.ex("B1", "Meerkeuze", "A", "De heenwedstrijden waren op zondag 1 november",
     "Os jogos de ida foram... A. no domingo 1º · B. no sábado 7 · C. no domingo 8", size=20, gap=8)
e.ex("B1", "Meerkeuze", "B", "Speelronde 34 heeft van maandag tot vrijdag wedstrijden",
     "A rodada 34 do Brasileirão... A. é só no domingo · B. tem jogo de segunda a sexta · C. já terminou", size=20, gap=8)
e.ex("B1", "Meerkeuze", "A", "Wie over twee wedstrijden wint, bereikt de finale",
     "Quem vai à final? A. quem vencer no total dos dois jogos · B. quem vencer a ida · C. quem tiver mais torcida", size=20, gap=8)
e.head("B · AS PALAVRAS", 25)
e.match_set("B1", "Woorden koppelen",
            ["o finalista", "a ida", "a volta", "a rodada"],
            ["o segundo jogo de um confronto",
             "o time que chega à final",
             "o primeiro jogo de um confronto",
             "a jornada de jogos de um campeonato"],
            ["b", "c", "a", "d"],
            ["finalista = het team dat de finale bereikt (b)", "ida = de eerste wedstrijd van een tweeluik (c)", "volta = de tweede wedstrijd van een tweeluik (a)", "rodada = een speelronde (d)"],
            instr="Combineer")
e.head("C · COMPARATIVOS", 25)
e.expl("Uitleg — Vul de juiste vergrotende trap tussen haakjes in.")
e.ex("B1", "Voltooi de zin", "mais", "De return beslist wie de finale haalt: mais",
     "A volta é ___ decisiva do que a ida. (mais / menos)", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "mais", "18 > 16: mais",
     "18h é ___ tarde do que 16h. (mais / menos)", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "mais", "17 < 18: mais cedo",
     "17h é ___ cedo do que 18h. (mais / menos)", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "mais", "Speelronde 34 loopt van maandag tot vrijdag: mais",
     "O Brasileirão tem ___ jogos na semana do que a Copa: a rodada vai de segunda a sexta. (mais / menos)", instr="Vul in", size=20, gap=8)
e.head("D · O PRETÉRITO PERFEITO", 25)
e.expl("Uitleg — Maak de zinnen af in de verleden tijd (pretérito perfeito).")
e.ex("B1", "Voltooi de zin", "foram", "ser, verleden tijd (meervoud): foram",
     "Os jogos de ida ___ (ser) no domingo 1º.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "recebeu", "receber, verleden tijd (ele): recebeu",
     "O Palmeiras ___ (receber) o Vasco na ida.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "recebeu", "receber, verleden tijd (ele): recebeu",
     "O Grêmio ___ (receber) o Atlético-MG na ida.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "começou", "começar, verleden tijd (ela): começou",
     "A rodada 34 ___ (começar) na segunda.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "chegaram", "chegar, verleden tijd (eles): chegaram",
     "Os times ___ (chegar) à volta com tudo em aberto.", instr="Vul in", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-esporte.svg")
print("P4 saved, exercises so far:", len(REG))
