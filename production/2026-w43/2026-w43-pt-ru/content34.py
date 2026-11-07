# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-pt-ru/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA · Культура", "A Lucerna", "A2 → B1 · A volta da guitarra · Возвращение гитары")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("A guitarra voltou: o som que o Brasil procura", 37)
f.byline("Da redação da A Lucerna · Nível de leitura: A2 → B1")
f.para("Durante muitos anos, a guitarra perdeu espaço no Brasil. Um estudo publicado nesta semana, com 22 anos de dados do Google, conta a história inteira: as buscas por «guitarra» caíram 74% entre 2004 e 2021. Ano após ano, o instrumento elétrico ficava mais silencioso.")
f.para("Mas a história mudou. Desde 2021, as buscas por guitarra crescem todos os anos: no total, já subiram 53%. Em 2026, a guitarra chegou a 75% do volume de buscas do violão — o instrumento mais brasileiro de todos. A guitarra elétrica e o violão acústico, outra vez lado a lado.")
f.para("Por quê? Os jovens descobrem bandas antigas nos vídeos curtos, compram a primeira guitarra e aprendem com aulas na internet. E há o ritual da semana: na sexta-feira, o país inteiro assiste ao debate na TV. No Brasil, a música e a televisão moram na mesma casa: a família se reúne, comenta, canta junto.")
f.gloss("a busca = поиск · cair = падать · crescer = расти · o volume = объём · lado a lado = рядом, вместе.")
f.head("DOIS INSTRUMENTOS, UM PAÍS", 25)
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
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "A GUITARRA EM NÚMEROS", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E você? Você toca algum instrumento — ou quer aprender? Escreva duas frases em português e mande para a redação."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Играете на инструменте? Хотите научиться? Напишите две фразы.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E VOCÊ? · А вы?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Играете на инструменте? Хотите научиться? Напишите две фразы.", 20, "sans", False, GREY, CW - 44, 1.42)
ay3 = ey3 + eh + 22
image(p, "django.jpg", ix, ay3, CW, 150)
acy = caption(p, ix, ay3 + 150, CW, "Django Reinhardt (1910–1953), um dos maiores guitarristas da história, em foto de William P. Gottlieb: a guitarra que o mundo procura outra vez.",
              "Foto: William P. Gottlieb / Wikimedia Commons — domínio público")
print("P3 col3 ends", acy)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EXERCÍCIOS · Упражнения страницы 3", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Ответы на странице 8 · Уровни перемешаны — ищите по номеру задания", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · COMPREENSÃO", 25)
e.expl("Прочитайте статью на странице 3 и выберите правильный ответ.")
e.ex("A2", "Выбор ответа", "B", "В 2004–2021 годах запросы упали на 74%",
     "Entre 2004 e 2021, as buscas por «guitarra»... A. cresceram 53% · B. caíram 74% · C. ficaram iguais", size=20, gap=8)
e.ex("A2", "Выбор ответа", "A", "С 2021 года растут каждый год",
     "Desde 2021, as buscas por guitarra... A. crescem todos os anos · B. caem todos os anos · C. pararam", size=20, gap=8)
e.ex("B1", "Выбор ответа", "C", "В 2026 году — 75% от violão",
     "Em 2026, a guitarra chegou a... A. 53% do violão · B. 100% do violão · C. 75% do volume do violão", size=20, gap=8)
e.ex("B1", "Выбор ответа", "B", "Молодёжь открывает старые группы в коротких видео",
     "Os jovens descobrem bandas antigas... A. no rádio do carro · B. nos vídeos curtos · C. nos jornais de papel", size=20, gap=8)
e.ex("B1", "Выбор ответа", "A", "violão — «самый бразильский» инструмент",
     "O instrumento «mais brasileiro de todos» é... A. o violão · B. a guitarra · C. o piano", size=20, gap=8)
e.head("B · AS PALAVRAS DO TEXTO", 25)
e.expl("Вставьте слова из рамки.")
e.para("guitarra · violão · busca · volume · banda · instrumento", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "Вставьте слово", "guitarra", "guitarra elétrica = электрогитара",
     "A ___ elétrica é o som do rock.", instr="Вставьте", size=20, gap=8)
e.ex("A2", "Вставьте слово", "violão", "violão acústico = акустическая гитара",
     "O ___ acústico é o instrumento da roda de amigos.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Вставьте слово", "busca", "busca = поиск",
     "Uma ___ no Google mostra o que o país quer saber.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Вставьте слово", "volume", "volume de buscas = объём запросов",
     "O ___ de buscas da guitarra cresce desde 2021.", instr="Вставьте", size=20, gap=8)
e.ex("A2", "Вставьте слово", "banda", "banda = группа",
     "Os jovens descobrem uma ___ antiga nos vídeos.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Вставьте слово", "instrumento", "instrumento = инструмент",
     "O piano também é um ___ musical.", instr="Вставьте", size=20, gap=8)
e.head("C · O PRETÉRITO PERFEITO", 25)
e.expl("Дополните в прошедшем времени (pretérito perfeito).")
e.ex("B1", "Вставьте слово", "caíram", "cair, прош. время, форма elas: caíram",
     "As buscas ___ (cair) 74% entre 2004 e 2021.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Вставьте слово", "cresceram", "crescer, прош. время, форма elas: cresceram",
     "Depois de 2021, as buscas ___ (crescer) todos os anos.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Вставьте слово", "chegou", "chegar, прош. время, форма ela: chegou",
     "Em 2026, a guitarra ___ (chegar) a 75% do violão.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Вставьте слово", "mudou", "mudar, прош. время, форма ela: mudou",
     "A história ___ (mudar) depois de 2021.", instr="Вставьте", size=20, gap=8)
e.head("D · CONSTRUA AS FRASES", 25)
e.expl("Составьте из слов правильные предложения.")
e.ex("B1", "Составьте предложение", "A guitarra voltou a crescer.", "Подл. + voltou a + инфинитив",
     "a guitarra / voltou / a crescer → ___", instr="Составьте", size=20, gap=8)
e.ex("A2", "Составьте предложение", "O violão é o instrumento mais brasileiro.", "Подл. + é + именная часть",
     "o violão / é / o instrumento mais brasileiro → ___", instr="Составьте", size=20, gap=8)
e.ex("B1", "Составьте предложение", "O Brasil voltou a procurar música.", "Подл. + voltou a + инфинитив",
     "o Brasil / voltou / a procurar música → ___", instr="Составьте", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · ESPORTE (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("ESPORTE · Спорт", "A Lucerna", "NÍVEL B1 · O futebol da semana · Футбольная неделя")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("Semana de decisão: adeus à Sul-Americana, vem aí a Copa do Brasil", 37)
f.byline("Da redação da A Lucerna · Nível de leitura: B1")
f.para("A terça-feira foi de festa e de lágrimas no Maracanã. O Vasco jogou a volta da semifinal da Copa Sul-Americana contra o Boca Juniors. Na ida, em Buenos Aires, o Vasco tinha vencido por 1 a 0. Mas na volta, o Boca fez 3 a 1 — e o Vasco está fora da competição.")
f.para("Os gols contam a noite: Di Lollo abriu o placar e Merentiel ampliou ainda no primeiro tempo. Puma Rodríguez diminuiu para o Vasco no segundo tempo, mas Paredes, no fim, fechou o 3 a 1. No total dos dois jogos: 3 a 2 para o Boca. Mais de 66 mil torcedores estavam no estádio.")
f.para("Agora, o Vasco pensa na Copa do Brasil. Na terça-feira, a CBF confirmou a arbitragem das semifinais: Anderson Daronco apita Palmeiras × Vasco, e Davi Lacerda comanda Grêmio × Atlético-MG. Os jogos de ida são no domingo, 1º de novembro: o futebol brasileiro não para — nem na semana da eleição.")
f.gloss("a ida = первый матч · a volta = ответный матч · o placar = счёт · ampliar = увеличивать (разрыв в счёте) · a arbitragem = назначение судей.")
f.end_report()

# col 3: data box + e você (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 376, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 240, "O JOGO EM NÚMEROS", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "Vasco 1 × 3 Boca Juniors · Maracanã · terça-feira, 20 de outubro. Ida: Boca 0 × 1 Vasco. Total (agregado): 3 × 2 para o Boca. Público: 66.026 torcedores. O Boca está na final da Sul-Americana.", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 602
etvous = "E você? Para quem você torce? Escreva duas frases em português e mande para a redação."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("За какую команду вы болеете? Напишите две фразы и пришлите нам.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "E VOCÊ? · А вы?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "За какую команду вы болеете? Напишите две фразы и пришлите нам.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "A SEMANA DO FUTEBOL · Футбольный календарь", 26, "sans", True, OLIVE)
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
    p.text(MX + 18, yy + 29, d, 20.5, "sans", True, BRICK)
    p.text(MX + 185, yy + 29, t, 20, "sans", False, GREY)
    p.text(MX + 430, yy + 29, m, 21, "serif", False, INK)
    yy += 44
tnote = "Atenção: as semifinais da Copa do Brasil são em novembro. Nesta semana, a CBF confirmou só a arbitragem — os jogos ainda não começaram."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EXERCÍCIOS · Упражнения страницы 4", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Ответы на странице 8 · Уровни перемешаны — ищите по номеру задания", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A · COMPREENSÃO", 25)
e.expl("Прочитайте статью на странице 4 и выберите правильный ответ.")
e.ex("B1", "Выбор ответа", "A", "В ответном матче «Бока» выиграла 3:1",
     "O jogo de volta, no Maracanã, terminou... A. Vasco 1 × 3 Boca · B. Vasco 3 × 1 Boca · C. 1 × 1", size=20, gap=8)
e.ex("B1", "Выбор ответа", "B", "В первом матче «Васко» выиграл 1:0",
     "No jogo de ida, em Buenos Aires... A. o Boca venceu por 1 a 0 · B. o Vasco venceu por 1 a 0 · C. foi 0 a 0", size=20, gap=8)
e.ex("B1", "Выбор ответа", "C", "Общий счёт 3:2, «Бока» — в финале",
     "No total dos dois jogos (agregado), o placar foi... A. 2 × 2 · B. 4 × 1 para o Vasco · C. 3 × 2 para o Boca", size=20, gap=8)
e.ex("B1", "Выбор ответа", "B", "Первые полуфиналы Кубка Бразилии — 1 ноября",
     "Os jogos de ida da Copa do Brasil são... A. nesta semana · B. no dia 1º de novembro · C. em dezembro", size=20, gap=8)
e.ex("B1", "Выбор ответа", "A", "Матч «Палмейрас» × «Васко» судит Даронко",
     "Quem apita Palmeiras × Vasco? A. Anderson Daronco · B. Davi Lacerda · C. César Tralli", size=20, gap=8)
e.head("B · AS PALAVRAS", 25)
e.match_set("B1", "Сопоставление",
            ["o placar", "a ida", "a volta", "o agregado"],
            ["a soma dos resultados dos dois jogos",
             "o primeiro jogo de um confronto",
             "o resultado de um jogo, com os gols",
             "o segundo jogo de um confronto"],
            ["c", "b", "d", "a"],
            ["placar = результат матча с голами c", "ida = первый матч противостояния b", "volta = второй матч противостояния d", "agregado = сумма результатов двух матчей a"],
            instr="Соедините пары")
e.head("C · COMPARATIVOS", 25)
e.expl("Заполните пропуски правильной сравнительной формой из скобок.")
e.ex("B1", "Вставьте слово", "mais", "В ответном матче 4 гола > 1 в первом: mais",
     "A volta foi ___ emocionante do que a ida: quatro gols contra um. (mais / menos)", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Вставьте слово", "maior", "66.026 > 66.000: maior",
     "O público foi ___ do que 66 mil torcedores: eram 66.026. (maior / menor)", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Вставьте слово", "melhor", "Степень bem — melhor (3:1 против 0:1)",
     "O Boca jogou ___ na volta do que na ida. (melhor / pior)", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Вставьте слово", "menos", "У «Васко» 1 гол < 3 у «Боки»: menos",
     "O Vasco marcou ___ gols na volta (1) do que o Boca (3). (mais / menos)", instr="Вставьте", size=20, gap=8)
e.head("D · O PRETÉRITO PERFEITO", 25)
e.expl("Дополните предложения в прошедшем времени (pretérito perfeito).")
e.ex("B1", "Вставьте слово", "venceu", "vencer, прош. время, форма ele: venceu",
     "Na ida, o Vasco ___ (vencer) por 1 a 0.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Вставьте слово", "perdeu", "perder, прош. время, форма ele: perdeu",
     "Na volta, o Vasco ___ (perder) por 3 a 1.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Вставьте слово", "fez", "fazer, прош. время, неправильная форма: fez",
     "O Boca ___ (fazer) três gols no Maracanã.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Вставьте слово", "diminuiu", "diminuir, прош. время, форма ele: diminuiu",
     "Puma Rodríguez ___ (diminuir) para o Vasco no segundo tempo.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Вставьте слово", "confirmou", "confirmar, прош. время, форма ela: confirmou",
     "Na terça-feira, a CBF ___ (confirmar) a arbitragem das semifinais.", instr="Вставьте", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-esporte.svg")
print("P4 saved, exercises so far:", len(REG))
