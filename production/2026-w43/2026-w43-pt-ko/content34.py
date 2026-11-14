# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA　문화", "A Lucerna", "A2 → B1　A volta da guitarra　기타의 귀환")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("A guitarra voltou: o som que o Brasil procura", 32)
f.byline("Da redação da A Lucerna　Nível de leitura: A2 → B1")
f.para("Durante muitos anos, a guitarra perdeu espaço no Brasil. Um estudo publicado nesta semana, com 22 anos de dados do Google, conta a história inteira: as buscas por «guitarra» caíram 74% entre 2004 e 2021. Ano após ano, o instrumento elétrico ficava mais silencioso.")
f.para("Mas a história mudou. Desde 2021, as buscas por guitarra crescem todos os anos: no total, já subiram 53%. Em 2026, a guitarra chegou a 75% do volume de buscas do violão — o instrumento mais brasileiro de todos. A guitarra elétrica e o violão acústico, outra vez lado a lado.")
f.para("Por quê? Os jovens descobrem bandas antigas nos vídeos curtos, compram a primeira guitarra e aprendem com aulas na internet. E há o ritual da semana: na sexta-feira, o país inteiro assiste ao debate na TV. No Brasil, a música e a televisão moram na mesma casa: a família se reúne, comenta, canta junto.")
f.gloss('a busca 검색 · cair 떨어지다 · crescer 늘다 · o volume 양, 규모 · lado a lado 나란히.')
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
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap('악기를 연주하나요? 배우고 싶은 악기는요? 두 문장을 써서 보내 주세요.', "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E VOCÊ?　여러분 이야기", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, '악기를 연주하나요? 배우고 싶은 악기는요? 두 문장을 써서 보내 주세요.', 20, "sans", False, GREY, CW - 44, 1.42)
ay3 = ey3 + eh + 22
image(p, "django.jpg", ix, ay3, CW, 150)
acy = caption(p, ix, ay3 + 150, CW, "Django Reinhardt (1910–1953), um dos maiores guitarristas da história, em foto de William P. Gottlieb: a guitarra que o mundo procura outra vez.",
              "Foto: William P. Gottlieb / Wikimedia Commons — domínio público")
print("P3 col3 ends", acy)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EXERCÍCIOS　제3면 연습 문제", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면에　등급이 섞인 문제예요. 번호로 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A　COMPREENSÃO", 25)
e.expl('3면 글을 읽고 맞는 답을 고르세요.')
e.ex("A2", '객관식', "B", '2004–2021년 검색이 74% 줄었어요',
     "Entre 2004 e 2021, as buscas por «guitarra»... A. cresceram 53% · B. caíram 74% · C. ficaram iguais", size=20, gap=8)
e.ex("A2", '객관식', "A", '2021년부터 해마다 늘고 있어요',
     "Desde 2021, as buscas por guitarra... A. crescem todos os anos · B. caem todos os anos · C. pararam", size=20, gap=8)
e.ex("B1", '객관식', "C", '2026년에 violão의 75%에 도달했어요',
     "Em 2026, a guitarra chegou a... A. 53% do violão · B. 100% do violão · C. 75% do volume do violão", size=20, gap=8)
e.ex("B1", '객관식', "B", '젊은이들은 짧은 영상에서 옛 밴드를 발견해요',
     "Os jovens descobrem bandas antigas... A. no rádio do carro · B. nos vídeos curtos · C. nos jornais de papel", size=20, gap=8)
e.ex("B1", '객관식', "A", 'violão은 "가장 브라질다운" 악기예요',
     "O instrumento «mais brasileiro de todos» é... A. o violão · B. a guitarra · C. o piano", size=20, gap=8)
e.head("B　AS PALAVRAS DO TEXTO", 25)
e.expl('상자 속 단어로 빈칸을 채우세요.')
e.para("guitarra · violão · busca · volume · banda · instrumento", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", '문장 완성', "guitarra", 'guitarra elétrica 일렉트릭 기타',
     "A ___ elétrica é o som do rock.", instr='빈칸 채우기', size=20, gap=8)
e.ex("A2", '문장 완성', "violão", 'violão acústico 어쿠스틱 기타',
     "O ___ acústico é o instrumento da roda de amigos.", instr='빈칸 채우기', size=20, gap=8)
e.ex("B1", '문장 완성', "busca", 'busca = 검색',
     "Uma ___ no Google mostra o que o país quer saber.", instr='빈칸 채우기', size=20, gap=8)
e.ex("B1", '문장 완성', "volume", 'volume de buscas = 검색량',
     "O ___ de buscas da guitarra cresce desde 2021.", instr='빈칸 채우기', size=20, gap=8)
e.ex("A2", '문장 완성', "banda", 'banda = 밴드',
     "Os jovens descobrem uma ___ antiga nos vídeos.", instr='빈칸 채우기', size=20, gap=8)
e.ex("B1", '문장 완성', "instrumento", 'instrumento = 악기',
     "O piano também é um ___ musical.", instr='빈칸 채우기', size=20, gap=8)
e.head("C　O PRETÉRITO PERFEITO", 25)
e.expl('과거형(pretérito perfeito)으로 채우세요.')
e.ex("B1", '문장 완성', "caíram", 'cair 과거형 elas 형태: caíram',
     "As buscas ___ (cair) 74% entre 2004 e 2021.", instr='빈칸 채우기', size=20, gap=8)
e.ex("B1", '문장 완성', "cresceram", 'crescer 과거형 elas 형태: cresceram',
     "Depois de 2021, as buscas ___ (crescer) todos os anos.", instr='빈칸 채우기', size=20, gap=8)
e.ex("B1", '문장 완성', "chegou", 'chegar 과거형 ela 형태: chegou',
     "Em 2026, a guitarra ___ (chegar) a 75% do violão.", instr='빈칸 채우기', size=20, gap=8)
e.ex("B1", '문장 완성', "mudou", 'mudar 과거형 ela 형태: mudou',
     "A história ___ (mudar) depois de 2021.", instr='빈칸 채우기', size=20, gap=8)
e.head("D　CONSTRUA AS FRASES", 25)
e.expl('단어를 배열해 올바른 문장을 만드세요.')
e.ex("B1", '문장 만들기', "A guitarra voltou a crescer.", '주어 + voltou a + 원형',
     "a guitarra / voltou / a crescer → ___", instr='문장 만들기', size=20, gap=8)
e.ex("A2", '문장 만들기', "O violão é o instrumento mais brasileiro.", '주어 + é + 보어',
     "o violão / é / o instrumento mais brasileiro → ___", instr='문장 만들기', size=20, gap=8)
e.ex("B1", '문장 만들기', "O Brasil voltou a procurar música.", '주어 + voltou a + 원형 구',
     "o Brasil / voltou / a procurar música → ___", instr='문장 만들기', size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · ESPORTE (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("ESPORTE　스포츠", "A Lucerna", "NÍVEL B1　O futebol da semana　이번 주 축구")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("Semana de decisão: adeus à Sul-Americana, vem aí a Copa do Brasil", 32)
f.byline("Da redação da A Lucerna　Nível de leitura: B1")
f.para("A terça-feira foi de festa e de lágrimas no Maracanã. O Vasco jogou a volta da semifinal da Copa Sul-Americana contra o Boca Juniors. Na ida, em Buenos Aires, o Vasco tinha vencido por 1 a 0. Mas na volta, o Boca fez 3 a 1 — e o Vasco está fora da competição.")
f.para("Os gols contam a noite: Di Lollo abriu o placar e Merentiel ampliou ainda no primeiro tempo. Puma Rodríguez diminuiu para o Vasco no segundo tempo, mas Paredes, no fim, fechou o 3 a 1. No total dos dois jogos: 3 a 2 para o Boca. Mais de 66 mil torcedores estavam no estádio.")
f.para("Agora, o Vasco pensa na Copa do Brasil. Na terça-feira, a CBF confirmou a arbitragem das semifinais: Anderson Daronco apita Palmeiras × Vasco, e Davi Lacerda comanda Grêmio × Atlético-MG. Os jogos de ida são no domingo, 1º de novembro: o futebol brasileiro não para — nem na semana da eleição.")
f.gloss('a ida 1차전 · a volta 2차전 · o placar 스코어 · ampliar (점수 차를) 벌리다 · a arbitragem 심판 배정.')
f.end_report()

# col 3: data box + e você (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 376, fill=BOX)
p.text(bx + 22, 240, "O JOGO EM NÚMEROS", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "Vasco 1 × 3 Boca Juniors · Maracanã · terça-feira, 20 de outubro. Ida: Boca 0 × 1 Vasco. Total (agregado): 3 × 2 para o Boca. Público: 66.026 torcedores. O Boca está na final da Sul-Americana.", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 602
etvous = "E você? Para quem você torce? Escreva duas frases em português e mande para a redação."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap('응원하는 팀을 두 문장으로 써서 보내 주세요.', "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "E VOCÊ?　여러분 이야기", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, '응원하는 팀을 두 문장으로 써서 보내 주세요.', 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "A SEMANA DO FUTEBOL　축구 주간 일정", 26, "sans", True, OLIVE)
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
p.text(MX, ey + 28, "EXERCÍCIOS　제4면 연습 문제", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면에　등급이 섞인 문제예요. 번호로 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A　COMPREENSÃO", 25)
e.expl('4면 글을 읽고 맞는 답을 고르세요.')
e.ex("B1", '객관식', "A", '2차전에서 보카가 3대 1로 이겼어요',
     "O jogo de volta, no Maracanã, terminou... A. Vasco 1 × 3 Boca · B. Vasco 3 × 1 Boca · C. 1 × 1", size=20, gap=8)
e.ex("B1", '객관식', "B", '1차전에서 바스쿠가 1대 0으로 이겼어요',
     "No jogo de ida, em Buenos Aires... A. o Boca venceu por 1 a 0 · B. o Vasco venceu por 1 a 0 · C. foi 0 a 0", size=20, gap=8)
e.ex("B1", '객관식', "C", '합계 3대 2, 보카가 결승에 올라요',
     "No total dos dois jogos (agregado), o placar foi... A. 2 × 2 · B. 4 × 1 para o Vasco · C. 3 × 2 para o Boca", size=20, gap=8)
e.ex("B1", '객관식', "B", '브라질컵 준결승 1차전은 11월 1일이에요',
     "Os jogos de ida da Copa do Brasil são... A. nesta semana · B. no dia 1º de novembro · C. em dezembro", size=20, gap=8)
e.ex("B1", '객관식', "A", 'Daronco가 Palmeiras × Vasco 경기를 맡아요',
     "Quem apita Palmeiras × Vasco? A. Anderson Daronco · B. Davi Lacerda · C. César Tralli", size=20, gap=8)
e.head("B　AS PALAVRAS", 25)
e.match_set("B1", '단어 짝짓기',
            ["o placar", "a ida", "a volta", "o agregado"],
            ["a soma dos resultados dos dois jogos",
             "o primeiro jogo de um confronto",
             "o resultado de um jogo, com os gols",
             "o segundo jogo de um confronto"],
            ["c", "b", "d", "a"],
            ['placar=골이 포함된 결과 c', 'ida=맞대결의 첫 경기 b', 'volta=맞대결의 두 번째 경기 d', 'agregado=두 경기 결과의 합 a'],
            instr='단어와 뜻 짝짓기')
e.head("C　COMPARATIVOS", 25)
e.expl('괄호 속 올바른 비교급으로 채우세요.')
e.ex("B1", '문장 완성', "mais", '2차전 4골 > 1차전 1골: mais',
     "A volta foi ___ emocionante do que a ida: quatro gols contra um. (mais / menos)", instr='빈칸 채우기', size=20, gap=8)
e.ex("B1", '문장 완성', "maior", "66.026 > 66.000：maior",
     "O público foi ___ do que 66 mil torcedores: eram 66.026. (maior / menor)", instr='빈칸 채우기', size=20, gap=8)
e.ex("B1", '문장 완성', "melhor", 'bem의 비교급은 melhor예요 (3–1 대 0–1)',
     "O Boca jogou ___ na volta do que na ida. (melhor / pior)", instr='빈칸 채우기', size=20, gap=8)
e.ex("B1", '문장 완성', "menos", '바스쿠 1골 < 보카 3골: menos',
     "O Vasco marcou ___ gols na volta (1) do que o Boca (3). (mais / menos)", instr='빈칸 채우기', size=20, gap=8)
e.head("D　O PRETÉRITO PERFEITO", 25)
e.expl('문장을 과거형(pretérito perfeito)으로 완성해요.')
e.ex("B1", '문장 완성', "venceu", 'vencer 과거형 ele 형태: venceu',
     "Na ida, o Vasco ___ (vencer) por 1 a 0.", instr='빈칸 채우기', size=20, gap=8)
e.ex("B1", '문장 완성', "perdeu", 'perder 과거형 ele 형태: perdeu',
     "Na volta, o Vasco ___ (perder) por 3 a 1.", instr='빈칸 채우기', size=20, gap=8)
e.ex("B1", '문장 완성', "fez", 'fazer 과거형 불규칙: fez',
     "O Boca ___ (fazer) três gols no Maracanã.", instr='빈칸 채우기', size=20, gap=8)
e.ex("B1", '문장 완성', "diminuiu", 'diminuir 과거형 ele 형태: diminuiu',
     "Puma Rodríguez ___ (diminuir) para o Vasco no segundo tempo.", instr='빈칸 채우기', size=20, gap=8)
e.ex("B1", '문장 완성', "confirmou", 'confirmar 과거형 ela 형태: confirmou',
     "Na terça-feira, a CBF ___ (confirmar) a arbitragem das semifinais.", instr='빈칸 채우기', size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-esporte.svg")
print("P4 saved, exercises so far:", len(REG))
