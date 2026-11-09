# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA　CULTUUR", "A Lucerna", "A2 → B1　Proclamação da República: 137 jaar")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("Proclamação da República: 137 anos de Brasil", 32)
f.byline("Da redação da A Lucerna　Nível de leitura: A2 → B1")
f.para("Em 15 de novembro de 1889, tropas comandadas pelo marechal Deodoro da Fonseca tomaram o governo no Rio de Janeiro, então a capital do país. A monarquia acabou: o imperador Dom Pedro II foi deposto e partiu para o exílio. Deodoro assumiu o governo provisório e se tornou o primeiro presidente do Brasil.")
f.para("A data virou feriado nacional: a Proclamação da República está na lista da Lei nº 662, de 1949, ao lado do 1º de janeiro, do 1º de maio e do 7 de setembro. É um feriado para todo o país — nenhuma cidade pode transformá-lo em dia útil.")
f.para("O que muda em 137 anos? A República é a forma do Estado: o presidente é eleito, o poder tem prazo, e as leis valem para todos. Para quem aprende português, a data traz palavras úteis: república, presidente, eleição, voto, constituição.")
f.para("E neste ano a data cai num domingo — o mesmo domingo do Enem. Não há ponte nem folga extra: quem não trabalha no domingo descansa como sempre; quem faz a prova estuda como sempre. Na página 2, a rotina do domingo 15. Na página 5, a semana dos jovens. Mas antes, uma pergunta: no seu país, há um feriado que lembra o começo da república?")
f.gloss("a monarquia = monarchie · a república = republiek · o marechal = maarschalk · o exílio = ballingschap · o governo = regering · a lei = wet.")
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
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "A SEMANA, DIA A DIA", 24, "sans", True, OLIVE)
yy3 += 52
for t in semana:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E você? No seu país, há um feriado que lembra o começo da república? Escreva duas frases em português e mande para a redação."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Heeft jouw land een feestdag voor de stichting van de republiek? Schrijf twee zinnen en stuur ze op.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E VOCÊ?　EN JIJ?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Heeft jouw land een feestdag voor de stichting van de republiek? Schrijf twee zinnen en stuur ze op.", 20, "sans", False, GREY, CW - 44, 1.42)
ky3 = ey3 + eh + 26
kb = "a república · o presidente · a eleição · o voto · a constituição · «proclamar» — seis palavras para um feriado de 137 anos."
kh = 62 + len(wrap(kb, "serif", False, 21.5, CW - 44)) * 30.5 + 16
p.rect(ix, ky3, CW, kh, fill=BOX)
yy3 = ky3 + 16
p.text(ix + 22, yy3 + 26, "PALAVRAS DA REPÚBLICA", 22, "sans", True, OLIVE)
yy3 += 52
p.para(ix + 22, yy3 + 21, kb, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P3 col3 ends", ky3 + kh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EXERCÍCIOS　OEFENINGEN PAGINA 3", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antwoorden op pagina 8　Niveaus door elkaar: zoek op nummer", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A　COMPREENSÃO", 25)
e.bridge("Lees pagina 3 en kies het juiste antwoord.")
e.ex("A2", "Meerkeuze", "B", "De Proclamatie van de Republiek was op 15 november 1889",
     "A Proclamação da República foi... A. em 1949 · B. em 15 de novembro de 1889 · C. em 1822", size=20, gap=8)
e.ex("A2", "Meerkeuze", "B", "Deodoro werd de eerste president van Brazilië",
     "Deodoro da Fonseca... A. foi o último imperador · B. se tornou o primeiro presidente · C. escreveu a Lei nº 662", size=20, gap=8)
e.ex("A2", "Meerkeuze", "B", "Een landelijke feestdag die geen stad tot werkdag mag maken",
     "A Proclamação é um feriado... A. só do Rio · B. nacional, para todo o país · C. só das escolas", size=20, gap=8)
e.ex("A2", "Meerkeuze", "C", "In 2026 valt de feestdag op een zondag",
     "Em 2026, o feriado cai... A. na segunda · B. na sexta · C. num domingo", size=20, gap=8)
e.ex("B1", "Meerkeuze", "A", "In een republiek wordt de president gekozen en is de macht beperkt in tijd",
     "Na República, o presidente... A. é eleito e o poder tem prazo · B. governa para sempre · C. é escolhido pelo imperador", size=20, gap=8)
e.head("B　AS PALAVRAS DO TEXTO", 25)
e.bridge("Vul in met de woorden uit het kader.")
e.para("monarquia · república · marechal · exílio · governo · lei", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "Zin afmaken", "monarquia", "monarquia = monarchie",
     "Em 1889, acabou a ___.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Zin afmaken", "república", "república = republiek",
     "O Brasil virou uma ___.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Zin afmaken", "marechal", "marechal = maarschalk",
     "Deodoro era ___.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Zin afmaken", "exílio", "exílio = ballingschap",
     "Dom Pedro II partiu para o ___.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Zin afmaken", "governo", "governo = regering",
     "Deodoro assumiu o ___ provisório.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Zin afmaken", "lei", "lei = wet",
     "A data está na lista da ___ nº 662.", instr="Vul in", size=20, gap=8)
e.head("C　O PRETÉRITO PERFEITO", 25)
e.bridge("Vul in in de verleden tijd (pretérito perfeito).")
e.ex("B1", "Zin afmaken", "tomaram", "tomar, verleden tijd, eles-vorm: tomaram",
     "As tropas ___ (tomar) o governo.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Zin afmaken", "acabou", "acabar, verleden tijd, ela-vorm: acabou",
     "A monarquia ___ (acabar) em 1889.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Zin afmaken", "foi", "ser, verleden tijd, ele-vorm: foi",
     "Dom Pedro II ___ (ser) deposto.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Zin afmaken", "assumiu", "assumir, verleden tijd, ele-vorm: assumiu",
     "Deodoro ___ (assumir) o governo.", instr="Vul in", size=20, gap=8)
e.head("D　CONSTRUA AS FRASES", 25)
e.bridge("Zet de woorden in de juiste volgorde.")
e.ex("B1", "Zinnen maken", "A Proclamação da República é um feriado nacional.", "Onderwerp + é + gezegde",
     "a proclamação / é / um feriado nacional → ___", instr="Maak een zin", size=20, gap=8)
e.ex("A2", "Zinnen maken", "Deodoro foi o primeiro presidente do Brasil.", "Onderwerp + werkwoord + gezegde",
     "deodoro / foi / o primeiro presidente / do brasil → ___", instr="Maak een zin", size=20, gap=8)
e.ex("B1", "Zinnen maken", "O Brasil virou uma república em 1889.", "Onderwerp + werkwoord + lijdend voorwerp + tijd",
     "o brasil / virou / uma república / em 1889 → ___", instr="Maak een zin", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · ESPORTE (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("ESPORTE　SPORT", "A Lucerna", "NIVEAU B1　De voetbalweek")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("As voltas decidem os finalistas da Copa", 32)
f.byline("Da redação da A Lucerna　Nível de leitura: B1")
f.para("A pergunta da semana é a mesma da semana passada — agora com respostas na ida: quem vai à final da Copa do Brasil? No domingo, 1º de novembro, o Grêmio venceu o Atlético-MG por 2 a 0, na Arena do Grêmio, com gols de Carlos Vinícius e Noriega. No mesmo dia, o Palmeiras venceu o Vasco por 1 a 0, no Nubank Parque, com gol de Maurício.")
f.para("A volta é neste fim de semana: no sábado, 7, às 18h, o Atlético-MG recebe o Grêmio na Arena MRV. O Atlético precisa vencer por três gols para passar direto; uma vitória por dois gols leva a decisão para os pênaltis. No domingo, 8, às 17h, o Vasco recebe o Palmeiras em São Januário: o Palmeiras passa com um empate; o Vasco precisa vencer por dois gols.")
f.para("A final é em jogo único, no dia 6 de dezembro, no Mané Garrincha, em Brasília. Até lá, o Brasileirão faz uma pausa: a rodada 35 só tem um jogo nesta semana — sábado, 14, às 18h30, Mirassol × Atlético-MG. Os outros nove jogos são nos dias 18 e 19, depois da Data Fifa.")
f.para("E a Data Fifa é no outro lado do mundo: a Seleção joga em Singapura — sábado, 14, às 7h15, contra o Japão, e terça, 17, às 7h, contra Singapura, no Estádio Nacional. O técnico Carlo Ancelotti convocou 26 jogadores para os dois últimos amistosos do ano. Os resultados da volta da Copa e os finalistas saem na próxima edição.")
f.gloss("a ida = de heenwedstrijd · a volta = de terugwedstrijd · o gol = de goal · o pênalti = de penalty · a pausa = de pauze · o amistoso = de vriendschappelijke wedstrijd.")
f.end_report()

# col 3: data box + e você (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 376, fill=BOX)
p.text(bx + 22, 240, "OS JOGOS DA SEMANA", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "Ida, dom 1º — Grêmio 2 × 0 Atlético-MG; Palmeiras 1 × 0 Vasco. Volta, sáb 7, 18h — Atlético-MG × Grêmio, Arena MRV. Volta, dom 8, 17h — Vasco × Palmeiras, São Januário. Final — 6 de dezembro, Mané Garrincha, Brasília.", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 602
etvous = "E você? Para quem você torce na Copa do Brasil — e quem chega à final? Escreva duas frases em português e mande para a redação."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Welk team steun jij in de Copa do Brasil, en wie haalt de finale? Schrijf twee zinnen en stuur ze op.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "E VOCÊ?　EN JIJ?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Welk team steun jij in de Copa do Brasil, en wie haalt de finale? Schrijf twee zinnen en stuur ze op.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "A SEMANA DO FUTEBOL　DE VOETBALWEEK", 26, "sans", True, OLIVE)
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
    p.text(MX + 18, yy + 29, d, 20.5, "sans", True, OLIVE)
    p.text(MX + 185, yy + 29, t, 20, "sans", False, GREY)
    p.text(MX + 430, yy + 29, m, 21, "serif", False, INK)
    yy += 44
tnote = "Nota: esta edição fechou em 2 de novembro. Os jogos de volta (7 e 8) ainda não tinham acontecido — os resultados e os finalistas saem na próxima edição."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EXERCÍCIOS　OEFENINGEN PAGINA 4", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antwoorden op pagina 8　Niveaus door elkaar: zoek op nummer", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A　COMPREENSÃO", 25)
e.bridge("Lees pagina 4 en kies het juiste antwoord.")
e.ex("B1", "Meerkeuze", "A", "In de heenwedstrijd won Grêmio met 2-0 van Atlético-MG",
     "Na ida, Grêmio × Atlético-MG foi... A. 2 a 0 para o Grêmio · B. 1 a 0 para o Atlético · C. 0 a 0", size=20, gap=8)
e.ex("B1", "Meerkeuze", "B", "Palmeiras won met 1-0 van Vasco, doelpunt van Maurício",
     "Na ida, Palmeiras × Vasco foi... A. 0 a 0 · B. 1 a 0 para o Palmeiras · C. 2 a 0 para o Vasco", size=20, gap=8)
e.ex("B1", "Meerkeuze", "A", "De terugwedstrijd Atlético-MG × Grêmio is zaterdag 7 om 18 uur",
     "A volta de Atlético-MG × Grêmio é... A. no sábado 7, às 18h · B. no domingo 8 · C. no dia 1º", size=20, gap=8)
e.ex("B1", "Meerkeuze", "B", "De finale: één wedstrijd, op 6 december, in het Mané Garrincha",
     "A final da Copa do Brasil é... A. em dois jogos · B. em jogo único, no dia 6 de dezembro · C. no dia 15", size=20, gap=8)
e.ex("B1", "Meerkeuze", "A", "Speelronde 35 heeft deze week maar één wedstrijd: Mirassol × Atlético-MG",
     "Na rodada 35, nesta semana... A. só há um jogo: Mirassol × Atlético-MG · B. há dez jogos · C. não há jogos", size=20, gap=8)
e.head("B　AS PALAVRAS", 25)
e.match_set("B1", "Woordenschat koppelen",
            ["o gol", "a ida", "a volta", "o pênalti"],
            ["o segundo jogo de um confronto",
             "o ponto marcado na rede",
             "a cobrança da marca dos onze metros",
             "o primeiro jogo de um confronto"],
            ["b", "d", "a", "c"],
            ["gol = de treffer in het net (b)", "ida = de eerste wedstrijd van een tweeluik (d)", "volta = de tweede wedstrijd van een tweeluik (a)", "pênalti = de strafschop vanaf elf meter (c)"],
            instr="Koppel")
e.head("C　COMPARATIVOS", 25)
e.bridge("Vul de juiste vergelijkingsvorm tussen haakjes in.")
e.ex("B1", "Zin afmaken", "mais", "2 > 0: mais",
     "Dois gols são ___ do que zero gols. (mais / menos)", instr="Vul in", size=20, gap=8)
e.ex("B1", "Zin afmaken", "mais", "3 > 2: mais",
     "Três gols são ___ do que dois gols. (mais / menos)", instr="Vul in", size=20, gap=8)
e.ex("B1", "Zin afmaken", "mais", "17 < 18: mais cedo",
     "17h é ___ cedo do que 18h. (mais / menos)", instr="Vul in", size=20, gap=8)
e.ex("B1", "Zin afmaken", "menos", "5 uur < 5,5 uur: menos",
     "Cinco horas são ___ do que cinco horas e meia. (mais / menos)", instr="Vul in", size=20, gap=8)
e.head("D　O PRETÉRITO PERFEITO", 25)
e.bridge("Maak de zinnen af in de verleden tijd (pretérito perfeito).")
e.ex("B1", "Zin afmaken", "venceu", "vencer, verleden tijd, ele-vorm: venceu",
     "O Grêmio ___ (vencer) por 2 a 0.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Zin afmaken", "marcaram", "marcar, verleden tijd, eles-vorm: marcaram",
     "Carlos Vinícius e Noriega ___ (marcar) os gols.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Zin afmaken", "marcou", "marcar, verleden tijd, ele-vorm: marcou",
     "Maurício ___ (marcar) o gol do Palmeiras.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Zin afmaken", "convocou", "convocar, verleden tijd, ele-vorm: convocou",
     "Ancelotti ___ (convocar) 26 jogadores.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Zin afmaken", "foram", "ser, verleden tijd, meervoud: foram",
     "Os jogos de ida ___ (ser) no domingo 1º.", instr="Vul in", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-esporte.svg")
print("P4 saved, exercises so far:", len(REG))
