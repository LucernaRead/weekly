# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA　문화", "A Lucerna", "A2 → B1　Zumbi e Palmares: a história do 20 de novembro")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW)], 200, 1560, tag="P3-main")
f.title("Zumbi e Palmares: a história do 20 de novembro", 32)
f.byline("Da redação da A Lucerna　Nível de leitura: A2 → B1")
f.para("Em 20 de novembro de 1695, morre Zumbi dos Palmares, o último grande líder do Quilombo dos Palmares, em Alagoas. A data virou o Dia Nacional de Zumbi e da Consciência Negra: em 2011, a Lei nº 12.519 criou o dia e, em 2023, a Lei nº 14.759 fez dele feriado nacional.")
f.para("Palmares foi o maior quilombo do Brasil: no século XVII, milhares de africanos escravizados que fugiam formaram uma comunidade livre na Serra da Barriga. Zumbi nasceu em Palmares e defendeu o quilombo por anos contra as tropas coloniais.")
f.para("O que a data celebra? A resistência, a história e a cultura afro-brasileiras — a capoeira, o samba, a culinária, a literatura. E também a reflexão: o combate ao racismo continua, todos os dias.")
f.para("E por que 20 de novembro? Porque é o dia da morte de Zumbi. O Brasil lembra o líder para não esquecer a história: sem memória, não há futuro. Na página 2, o feriadão; na página 5, a semana dos jovens.")
f.gloss("o quilombo 도망친 노예들의 마을 · a resistência 저항 · escravizado 노예가 된 사람 · o líder 지도자 · a memória 기억 · o combate 투쟁.")
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
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("당신 나라에는 자유를 위해 싸운 영웅이 있나요? 두 문장을 써서 보내 주세요.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E VOCÊ?　자기 얘기를 해 봐요", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "당신 나라에는 자유를 위해 싸운 영웅이 있나요? 두 문장을 써서 보내 주세요.", 20, "sans", False, GREY, CW - 44, 1.42)
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
p.text(MX, ey + 28, "EXERCÍCIOS　3면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면　수준이 섞여 있어요. 번호로 정답을 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A　COMPREENSÃO", 25)
e.bridge("3면 기사를 읽고 바른 답을 고르세요.")
e.ex("A2", "하나 고르기", "C", "줌비는 1695년 11월 20일에 돌아가셨어요",
     "Zumbi dos Palmares morreu... A. em 1889 · B. em 2011 · C. em 20 de novembro de 1695", size=20, gap=8)
e.ex("A2", "하나 고르기", "A", "파우마리스는 알라고아스주에 있었어요",
     "O Quilombo dos Palmares ficava... A. em Alagoas · B. no Rio · C. em São Paulo", size=20, gap=8)
e.ex("A2", "하나 고르기", "B", "2023년 법으로 11월 20일이 전국 공휴일이 됐어요",
     "A Lei nº 14.759, de 2023... A. criou o dia 20 · B. fez do dia 20 feriado nacional · C. acabou com o feriado", size=20, gap=8)
e.ex("A2", "하나 고르기", "B", "파우마리스는 브라질에서 가장 큰 킬롬부였어요",
     "Palmares foi... A. uma cidade portuguesa · B. o maior quilombo do Brasil · C. um time de futebol", size=20, gap=8)
e.ex("B1", "하나 고르기", "A", "이 날은 저항과 역사, 아프로브라질 문화를 기려요",
     "O dia 20 celebra... A. a resistência e a cultura afro-brasileira · B. a Proclamação da República · C. o Enem", size=20, gap=8)
e.head("B　AS PALAVRAS DO TEXTO", 25)
e.bridge("네모 안의 단어로 채워요.")
e.para("quilombo · resistência · escravizado · líder · memória · combate", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "문장을 완성하기", "quilombo", "quilombo = 도망친 노예들의 마을",
     "Palmares foi o maior ___ do Brasil.", instr="채우기", size=20, gap=8)
e.ex("A2", "문장을 완성하기", "resistência", "resistência = 저항",
     "O dia 20 celebra a ___ do povo negro.", instr="채우기", size=20, gap=8)
e.ex("A2", "문장을 완성하기", "escravizados", "escravizado 복수에 맞추기: escravizados",
     "Milhares de africanos ___ fugiam e formavam quilombos.", instr="채우기", size=20, gap=8)
e.ex("A2", "문장을 완성하기", "líder", "líder = 지도자",
     "Zumbi foi o último grande ___ de Palmares.", instr="채우기", size=20, gap=8)
e.ex("A2", "문장을 완성하기", "memória", "memória = 기억",
     "Sem ___ , não há futuro.", instr="채우기", size=20, gap=8)
e.ex("B1", "문장을 완성하기", "combate", "combate = 투쟁",
     "O ___ ao racismo continua todos os dias.", instr="채우기", size=20, gap=8)
e.head("C　O PRETÉRITO PERFEITO", 25)
e.bridge("과거형（pretérito perfeito）으로 채워요.")
e.ex("B1", "문장을 완성하기", "morreu", "morrer, 과거형, ele 형태: morreu",
     "Zumbi ___ (morrer) em 20 de novembro de 1695.", instr="채우기", size=20, gap=8)
e.ex("B1", "문장을 완성하기", "nasceu", "nascer, 과거형, ele 형태: nasceu",
     "Zumbi ___ (nascer) em Palmares.", instr="채우기", size=20, gap=8)
e.ex("B1", "문장을 완성하기", "defendeu", "defender, 과거형, ele 형태: defendeu",
     "Zumbi ___ (defender) o quilombo por anos.", instr="채우기", size=20, gap=8)
e.ex("B1", "문장을 완성하기", "formaram", "formar, 과거형, eles 형태: formaram",
     "Os fugitivos ___ (formar) uma comunidade livre.", instr="채우기", size=20, gap=8)
e.head("D　CONSTRUA AS FRASES", 25)
e.bridge("단어를 바른 순서로 늘어 문장을 만들어요.")
e.ex("B1", "문장 만들기", "O dia 20 de novembro é feriado nacional.", "주어 + é + 보어",
     "o dia 20 / é / feriado nacional → ___", instr="문장 만들기", size=20, gap=8)
e.ex("A2", "문장 만들기", "Zumbi foi o líder de Palmares.", "주어 + 동사 + 보어",
     "zumbi / foi / o líder / de palmares → ___", instr="문장 만들기", size=20, gap=8)
e.ex("B1", "문장 만들기", "Palmares foi o maior quilombo do Brasil.", "주어 + 동사 + 보어",
     "palmares / foi / o maior quilombo / do brasil → ___", instr="문장 만들기", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · ESPORTE (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("ESPORTE　스포츠", "A Lucerna", "NÍVEL B1　A final da Copa do Brasil　코파 두 브라지우 결승이 정해졌어요")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("Grêmio e Palmeiras decidem a Copa do Brasil", 32)
f.byline("Da redação da A Lucerna　Nível de leitura: B1")
f.para("A pergunta da semana passada tem resposta: quem vai à final da Copa do Brasil? No sábado, 7, o Grêmio empatou por 1 a 1 com o Atlético-MG, na Arena MRV, e passou com 3 a 1 no total: havia vencido a ida por 2 a 0, em Porto Alegre. Renan Lodi abriu o placar para o Atlético e Carlos Vinícius empatou para o Grêmio.")
f.para("No domingo, 8, o Vasco venceu o Palmeiras por 2 a 1, em São Januário — mas o Palmeiras havia vencido a ida por 1 a 0, e o agregado ficou em 2 a 2. Nos pênaltis, o Palmeiras venceu por 5 a 4 e foi à final. Foi a segunda semifinal decidida nos detalhes: um empate que bastou, e uma disputa de pênaltis.")
f.para("A final é em jogo único, no dia 6 de dezembro, no Mané Garrincha, em Brasília. O Grêmio busca o sexto título — e joga a décima final da sua história. O Palmeiras busca o quinto título da Copa do Brasil. Quem ganha, levanta a taça e garante vaga na próxima Libertadores.")
f.para("E o Brasileirão volta depois da pausa: a rodada 35 termina na quarta, 18, e na quinta, 19 — Cruzeiro × Palmeiras e Flamengo × Athletico-PR na quarta; Vasco × Internacional e São Paulo × Fluminense na quinta. No sábado, 21, às 16h30, Palmeiras × Flamengo: o jogo que pode decidir o título. E em Interlagos, no domingo 8, Lando Norris venceu o Grande Prêmio de São Paulo, com Verstappen em segundo e Hadjar em terceiro; a Mercedes garantiu o título de construtores.")
f.gloss("o agregado 합산 점수 · os pênaltis 승부차기 · a decisão 결승 · o título 우승/타이틀 · a pausa 쉬는 기간 · a taça 트로피.")
f.end_report()

# col 3: data box + e você (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 376, fill=BOX)
p.text(bx + 22, 240, "OS FINALISTAS", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "Ida, dom 1º — Grêmio 2 × 0 Atlético-MG; Palmeiras 1 × 0 Vasco. Volta, sáb 7 — Atlético-MG 1 × 1 Grêmio (total 3 × 1). Volta, dom 8 — Vasco 2 × 1 Palmeiras (total 2 × 2; pênaltis 5 × 4). Final — 6 de dezembro, Mané Garrincha, Brasília.", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 602
etvous = "E você? Na final, Grêmio ou Palmeiras — para quem você torce? Escreva duas frases em português e mande para a redação."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("결승에서는 그레미우와 파우메이라스 중 누구를 응원하세요? 두 문장을 써서 보내 주세요.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "E VOCÊ?　자기 얘기를 해 봐요", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "결승에서는 그레미우와 파우메이라스 중 누구를 응원하세요? 두 문장을 써서 보내 주세요.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "A SEMANA DO FUTEBOL　축구 일주일", 26, "sans", True, OLIVE)
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
p.text(MX, ey + 28, "EXERCÍCIOS　4면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면　수준이 섞여 있어요. 번호로 정답을 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A　COMPREENSÃO", 25)
e.bridge("4면 기사를 읽고 바른 답을 고르세요.")
e.ex("B1", "하나 고르기", "A", "2차전에서 그레미우는 아틀레치쿠 MG와 1–1로 비겼고, 합산 3–1로 올라갔어요",
     "Na volta, Atlético-MG × Grêmio foi... A. 1 a 1, e o Grêmio passou com 3 a 1 no total · B. 2 a 0 para o Atlético · C. 0 a 0", size=20, gap=8)
e.ex("B1", "하나 고르기", "B", "바스쿠는 2차전에서 2–1로 이겼지만, 합산은 2–2였고 파우메이라스가 승부차기로 올라갔어요",
     "Na volta, Vasco × Palmeiras foi... A. 1 a 0 para o Palmeiras · B. 2 a 1 para o Vasco, e o Palmeiras passou nos pênaltis · C. 0 a 0", size=20, gap=8)
e.ex("B1", "하나 고르기", "B", "승부차기 5–4: 파우메이라스가 올라갔어요",
     "Nos pênaltis, o Palmeiras venceu por... A. 4 a 3 · B. 5 a 4 · C. 6 a 5", size=20, gap=8)
e.ex("B1", "하나 고르기", "B", "결승은 12월 6일 단판, 마네 가힌샤에서 열려요",
     "A final da Copa do Brasil é... A. em dois jogos · B. em jogo único, no dia 6 de dezembro · C. no dia 15", size=20, gap=8)
e.ex("B1", "하나 고르기", "A", "노리스가 상파울루 그랑프리에서 우승했고, 페르스타펜이 2위였어요",
     "O Grande Prêmio de São Paulo foi vencido por... A. Lando Norris · B. Max Verstappen · C. Isack Hadjar", size=20, gap=8)
e.head("B　AS PALAVRAS", 25)
e.match_set("B1", "어휘 연결하기",
            ["o agregado", "a volta", "os pênaltis", "a taça"],
            ["o segundo jogo de um confronto",
             "o placar dos dois jogos somados",
             "o prêmio do campeão",
             "a disputa da marca dos onze metros"],
            ["b", "a", "d", "c"],
            ["agregado=두 경기 점수 합계 b", "volta=대결의 두 번째 경기 a", "pênaltis=11미터 지점에서의 승부 d", "taça=우승 트로피 c"],
            instr="단어와 뜻 연결하기")
e.head("C　COMPARATIVOS", 25)
e.bridge("괄호 안의 바른 비교 형태로 채워요.")
e.ex("B1", "문장을 완성하기", "mais", "3 > 1: mais",
     "Três gols são ___ do que um gol. (mais / menos)", instr="채우기", size=20, gap=8)
e.ex("B1", "문장을 완성하기", "mais", "5 > 4: mais",
     "Cinco pênaltis são ___ do que quatro. (mais / menos)", instr="채우기", size=20, gap=8)
e.ex("B1", "문장을 완성하기", "mais", "16:30 < 17:00: mais cedo",
     "16h30 é ___ cedo do que 17h. (mais / menos)", instr="채우기", size=20, gap=8)
e.ex("B1", "문장을 완성하기", "menos", "2일 < 7일: menos",
     "Dois dias são ___ do que uma semana. (mais / menos)", instr="채우기", size=20, gap=8)
e.head("D　O PRETÉRITO PERFEITO", 25)
e.bridge("문장을 과거형（pretérito perfeito）으로 완성하세요.")
e.ex("B1", "문장을 완성하기", "empatou", "empatar, 과거형, ele 형태: empatou",
     "O Grêmio ___ (empatar) por 1 a 1.", instr="채우기", size=20, gap=8)
e.ex("B1", "문장을 완성하기", "venceu", "vencer, 과거형, ele 형태: venceu",
     "O Vasco ___ (vencer) por 2 a 1.", instr="채우기", size=20, gap=8)
e.ex("B1", "문장을 완성하기", "abriu", "abrir, 과거형, ele 형태: abriu",
     "Renan Lodi ___ (abrir) o placar.", instr="채우기", size=20, gap=8)
e.ex("B1", "문장을 완성하기", "garantiu", "garantir, 과거형, ela 형태: garantiu",
     "A Mercedes ___ (garantir) o título de construtores.", instr="채우기", size=20, gap=8)
e.ex("B1", "문장을 완성하기", "foram", "ser 과거형, 복수: foram",
     "Os jogos de volta ___ (ser) no fim de semana.", instr="채우기", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-esporte.svg")
print("P4 saved, exercises so far:", len(REG))
