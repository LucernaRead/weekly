# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA　CULTURE", "A Lucerna", "A2 → B1　Finados: o dia da memória　Finados : le jour du souvenir")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("Finados: o dia em que o Brasil lembra", 32)
f.byline("Da redação da A Lucerna　Nível de leitura: A2 → B1")
f.para("No dia 2 de novembro, o Brasil para para lembrar. Finados — o Dia dos Fiéis Defuntos — é o dia em que as famílias visitam os cemitérios do país inteiro, do pequeno cemitério do interior ao grande cemitério da capital.")
f.para("O ritual é simples e antigo: limpar o túmulo, levar flores — sobretudo crisântemos, a flor de Finados —, acender uma vela e rezar. Nas igrejas e nos cemitérios, há missas o dia inteiro. Não é festa: é um dia calmo, de silêncio, de encontro e de memória.")
f.para("Cada família tem o seu jeito: uns levam a flor preferida de quem partiu, outros levam a comida de que ele gostava, outros só ficam um pouco em silêncio. O que não muda é o centro do dia: lembrar é um jeito de continuar perto.")
f.para("E Finados tem um vizinho famoso: no sábado, 31 de outubro, foi Halloween, com fantasias e doces. Dois dias, dois jeitos de olhar para a morte: um de festa, outro de silêncio — e os dois cabem na mesma semana.")
f.gloss("o túmulo = tombe · a flor = fleur · acender = allumer · rezar = prier · o silêncio = silence · a lembrança = souvenir.")
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
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "A SEMANA, DIA A DIA", 24, "sans", True, OLIVE)
yy3 += 52
for t in semana:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E você? Na sua cultura, como se lembram os mortos? Escreva duas frases em português e mande para a redação."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Dans votre culture, comment se souvient-on des morts ? Écrivez deux phrases et envoyez-les-nous.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E VOCÊ?　ET VOUS ?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Dans votre culture, comment se souvient-on des morts ? Écrivez deux phrases et envoyez-les-nous.", 20, "sans", False, GREY, CW - 44, 1.42)
ky3 = ey3 + eh + 26
kb = "o túmulo · a vela · o crisântemo · a missa · a lembrança · «descanse em paz» — seis palavras para um dia de silêncio."
kh = 62 + len(wrap(kb, "serif", False, 21.5, CW - 44)) * 30.5 + 16
p.rect(ix, ky3, CW, kh, fill=BOX)
yy3 = ky3 + 16
p.text(ix + 22, yy3 + 26, "PALAVRAS DE FINADOS", 22, "sans", True, OLIVE)
yy3 += 52
p.para(ix + 22, yy3 + 21, kb, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P3 col3 ends", ky3 + kh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EXERCÍCIOS　EXERCICES　PAGE 3", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Réponses page 8　niveaux mélangés — cherchez par numéro", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A　COMPREENSÃO", 25)
e.bridge("Lisez la page 3 et choisissez la bonne réponse.")
e.ex("A2", "单选", "B", "Finados est le jour du souvenir et du silence",
     "Finados é... A. um dia de festa e fantasia · B. o dia da memória e do silêncio · C. um dia de votação", size=20, gap=8)
e.ex("A2", "单选", "B", "Fleurs aux cimetières, surtout des chrysanthèmes",
     "As famílias levam aos cemitérios... A. presentes de Natal · B. flores, sobretudo crisântemos · C. fogos de artifício", size=20, gap=8)
e.ex("A2", "单选", "B", "Messes toute la journée, églises et cimetières",
     "Nas igrejas e nos cemitérios, há... A. shows de rock · B. missas o dia inteiro · C. feiras de livros", size=20, gap=8)
e.ex("A2", "单选", "C", "Halloween, c’était le samedi 31 octobre",
     "Halloween foi... A. no domingo 8 · B. na segunda 2 · C. no sábado, 31 de outubro", size=20, gap=8)
e.ex("B1", "单选", "A", "Se souvenir, c’est rester proche",
     "O texto diz que lembrar é... A. um jeito de continuar perto · B. uma festa · C. uma votação", size=20, gap=8)
e.head("B　AS PALAVRAS DO TEXTO", 25)
e.bridge("Complétez avec les mots de l’encadré.")
e.para("túmulo · vela · crisântemo · missa · silêncio · lembrança", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "完成句子", "túmulo", "túmulo = tombe",
     "As famílias limpam o ___.", instr="Compléter", size=20, gap=8)
e.ex("A2", "完成句子", "vela", "vela = bougie",
     "Acendem uma ___ em memória.", instr="Compléter", size=20, gap=8)
e.ex("A2", "完成句子", "crisântemo", "crisântemo = chrysanthème",
     "O ___ é a flor de Finados.", instr="Compléter", size=20, gap=8)
e.ex("A2", "完成句子", "missa", "missa = messe",
     "Na igreja, há ___ o dia inteiro.", instr="Compléter", size=20, gap=8)
e.ex("A2", "完成句子", "silêncio", "silêncio = silence",
     "Finados é um dia de ___.", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "lembrança", "lembrança = souvenir",
     "A ___ volta à mesa.", instr="Compléter", size=20, gap=8)
e.head("C　O PRETÉRITO PERFEITO", 25)
e.bridge("Complétez au pretérito perfeito.")
e.ex("B1", "完成句子", "visitaram", "visitar, passé elas : visitaram",
     "As famílias ___ (visitar) os cemitérios.", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "levaram", "levar, passé elas : levaram",
     "Elas ___ (levar) flores.", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "foi", "ser, passé ele : foi",
     "O sábado ___ (ser) de Halloween.", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "viveu", "viver, passé ele : viveu",
     "O Brasil ___ (viver) dois dias diferentes.", instr="Compléter", size=20, gap=8)
e.head("D　CONSTRUA AS FRASES", 25)
e.bridge("Formez des phrases avec les mots donnés.")
e.ex("B1", "造句", "Finados é um dia de silêncio.", "Sujet + é + attribut",
     "finados / é / um dia de silêncio → ___", instr="Former une phrase", size=20, gap=8)
e.ex("A2", "造句", "As famílias levam flores ao cemitério.", "Sujet + verbe + complément + lieu",
     "as famílias / levam / flores / ao cemitério → ___", instr="Former une phrase", size=20, gap=8)
e.ex("B1", "造句", "O Brasil lembra os seus mortos.", "Sujet + verbe + complément",
     "o Brasil / lembra / os seus mortos → ___", instr="Former une phrase", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · ESPORTE (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("ESPORTE　SPORT", "A Lucerna", "NÍVEL B1　O futebol da semana　La semaine du football")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("Semana de decisão: quem vai à final da Copa do Brasil?", 32)
f.byline("Da redação da A Lucerna　Nível de leitura: B1")
f.para("A pergunta da semana é simples: quem vai à final da Copa do Brasil? Quatro times, dois jogos de volta, um fim de semana. No sábado, 7, às 18h, o Atlético-MG recebe o Grêmio na Arena MRV. No domingo, 8, às 17h, o Vasco recebe o Palmeiras em São Januário.")
f.para("Os jogos de ida foram no domingo, 1º de novembro: Palmeiras × Vasco, às 16h, e Grêmio × Atlético-MG, às 18h30. Os quatro times chegam à volta com tudo em aberto: quem vencer no total dos dois jogos vai à final.")
f.para("E o Brasileirão não para: a rodada 34 tem jogo de segunda a sexta, de 2 a 6 de novembro. É a reta final do campeonato: cada ponto vale uma posição, cada gol vale uma história. No fim de semana, o país para para a Copa — e volta para o Brasileirão na semana que vem.")
f.para("Ontem, domingo 1º, já foi de Copa: os jogos de ida abriram as semifinais. Nesta semana, a volta fecha a conta. Sábado e domingo, o Brasil tem dois horários marcados: 18h e 17h.")
f.gloss("a ida = match aller · a volta = match retour · o finalista = finaliste · a decisão = match décisif · a rodada = journée de championnat.")
f.end_report()

# col 3: data box + e você (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 376, fill=BOX)
p.text(bx + 22, 240, "OS JOGOS DA SEMANA", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "Sáb 7, 18h — Atlético-MG × Grêmio, Arena MRV (volta). Dom 8, 17h — Vasco × Palmeiras, São Januário (volta). Ida, dom 1º — Palmeiras × Vasco, 16h; Grêmio × Atlético-MG, 18h30.", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 602
etvous = "E você? Para quem você torce na Copa do Brasil? Escreva duas frases em português e mande para a redação."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Quelle équipe soutenez-vous en Copa do Brasil ? Écrivez deux phrases et envoyez-les-nous.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "E VOCÊ?　ET VOUS ?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Quelle équipe soutenez-vous en Copa do Brasil ? Écrivez deux phrases et envoyez-les-nous.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "A SEMANA DO FUTEBOL　LA SEMAINE DU FOOTBALL", 26, "sans", True, OLIVE)
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
    p.text(MX + 18, yy + 29, d, 20.5, "sans", True, OLIVE)
    p.text(MX + 185, yy + 29, t, 20, "sans", False, GREY)
    p.text(MX + 430, yy + 29, m, 21, "serif", False, INK)
    yy += 44
tnote = "Atenção: os jogos de ida foram no domingo 1º; os de volta decidem os finalistas neste fim de semana. Os resultados da volta saem na próxima edição."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EXERCÍCIOS　EXERCICES　PAGE 4", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Réponses page 8　niveaux mélangés — cherchez par numéro", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A　COMPREENSÃO", 25)
e.bridge("Lisez la page 4 et choisissez la bonne réponse.")
e.ex("B1", "单选", "A", "Retour Atlético-MG × Grêmio : samedi 7, 18 h",
     "A volta de Atlético-MG × Grêmio é... A. no sábado 7, às 18h · B. no domingo 8 · C. no dia 1º", size=20, gap=8)
e.ex("B1", "单选", "B", "Retour Vasco × Palmeiras, dimanche 8",
     "Vasco × Palmeiras, a volta, é... A. no sábado, na Arena MRV · B. no domingo 8, às 17h, em São Januário · C. na segunda 2", size=20, gap=8)
e.ex("B1", "单选", "A", "Les matches aller ont eu lieu le dimanche 1er novembre",
     "Os jogos de ida foram... A. no domingo 1º · B. no sábado 7 · C. no domingo 8", size=20, gap=8)
e.ex("B1", "单选", "B", "La 34e journée a un match du lundi au vendredi",
     "A rodada 34 do Brasileirão... A. é só no domingo · B. tem jogo de segunda a sexta · C. já terminou", size=20, gap=8)
e.ex("B1", "单选", "A", "Va en finale qui gagne sur l’ensemble des deux matches",
     "Quem vai à final? A. quem vencer no total dos dois jogos · B. quem vencer a ida · C. quem tiver mais torcida", size=20, gap=8)
e.head("B　AS PALAVRAS", 25)
e.match_set("B1", "词汇配对",
            ["o finalista", "a ida", "a volta", "a rodada"],
            ["o segundo jogo de um confronto",
             "o time que chega à final",
             "o primeiro jogo de um confronto",
             "a jornada de jogos de um campeonato"],
            ["b", "c", "a", "d"],
            ["finalista = équipe qui atteint la finale : b", "ida = premier match d’une confrontation : c", "volta = deuxième match d’une confrontation : a", "rodada = journée d’un championnat : d"],
            instr="Associer")
e.head("C　COMPARATIVOS", 25)
e.bridge("Complétez avec la bonne forme comparative entre parenthèses.")
e.ex("B1", "完成句子", "mais", "Le retour décide de la finale : mais",
     "A volta é ___ decisiva do que a ida. (mais / menos)", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "mais", "18 > 16 : mais",
     "18h é ___ tarde do que 16h. (mais / menos)", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "mais", "17 < 18 : mais cedo",
     "17h é ___ cedo do que 18h. (mais / menos)", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "mais", "La 34e journée va du lundi au vendredi : mais",
     "O Brasileirão tem ___ jogos na semana do que a Copa: a rodada vai de segunda a sexta. (mais / menos)", instr="Compléter", size=20, gap=8)
e.head("D　O PRETÉRITO PERFEITO", 25)
e.bridge("Complétez les phrases au pretérito perfeito.")
e.ex("B1", "完成句子", "foram", "ser, passé pluriel : foram",
     "Os jogos de ida ___ (ser) no domingo 1º.", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "recebeu", "receber, passé ele : recebeu",
     "O Palmeiras ___ (receber) o Vasco na ida.", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "recebeu", "receber, passé ele : recebeu",
     "O Grêmio ___ (receber) o Atlético-MG na ida.", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "começou", "começar, passé ela : começou",
     "A rodada 34 ___ (começar) na segunda.", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "chegaram", "chegar, passé eles : chegaram",
     "Os times ___ (chegar) à volta com tudo em aberto.", instr="Compléter", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-esporte.svg")
print("P4 saved, exercises so far:", len(REG))
