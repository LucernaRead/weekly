# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-pt-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · JOVENS (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band('JOVENS · 청년', "A Lucerna", 'NÍVEL B1 · A Fazenda, o Enem e os planos dos jovens · 리얼리티, Enem, 젊은이들의 계획')

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-main")
f.title("Duas votações e uma prova: a semana dos jovens", 37)
f.byline("Da redação da A Lucerna · Nível de leitura: B1")
f.para("A semana dos jovens brasileiros tem três datas. A primeira é da televisão: em A Fazenda 18, o reality da Record, Catherine Bascoy, Gabriel Torres e Thaíde disputam a Prova do Fazendeiro nesta quarta-feira, 21 de outubro. Na internet, a enquete já corre: quem fica e quem sai do jogo?")
f.para("A segunda data é do estudo. Faltam menos de três semanas para o Enem 2026: as provas são nos domingos 8 e 15 de novembro, e mais de 5 milhões de estudantes estão inscritos. Neste mês, o Inep libera o Cartão de Confirmação, o documento que mostra o local da prova de cada aluno. É a reta final: revisar, descansar e conferir o endereço — como na eleição, quem confere antes não se perde no dia.")
f.para("A terceira data é um termômetro. Depois do primeiro turno, as buscas por «como morar fora do Brasil» cresceram 40%, segundo um levantamento com dados do Google. É um comportamento de busca, não um dado de emigração: mostra uma pergunta que muitos jovens fazem nesta semana — ficar ou partir?")
f.box("O PLANO DA RETA FINAL", [
    ('1. Confira o Cartão de Confirmação do Enem (Enem 확인 카드를 확인하세요)', "serif", False, INK, 21, 1.36),
    ('2. Revise um pouco por dia, sem maratona (조금씩 복습, 벼락치기 없이)', "serif", False, INK, 21, 1.36),
    ('3. Durma bem na véspera da prova (시험 전날 밤 푹 자기)', "serif", False, INK, 21, 1.36),
    ('4. Separe documento e caneta no dia anterior (하루 전에 신분증과 펜 준비)', "serif", False, INK, 21, 1.36),
    ('5. Domingo 25: vote (se você vota) e descanse (일요일 25일: 투표하고 쉬기)', "serif", False, INK, 21, 1.36),
])
f.gloss('a enquete (시청자) 투표, 여론조사 · a reta final 막바지 · o levantamento 조사, 통계 · a véspera 전날.')
f.end_report()

# col 3: study image + facts + e você + mega-sena box (sequential)
ix = COLX[3]
image(p, "estudo.jpg", ix, 200, CW, 272)
cy3 = caption(p, ix, 472, CW, "Estudantes em uma biblioteca: para os mais de 5 milhões de inscritos no Enem, é a reta final — provas nos dias 8 e 15 de novembro.",
              "Foto: Gary Todd / Wikimedia Commons — CC0")
facts = ["Mais de 5 milhões de inscritos no Enem 2026 (Inep).",
         "Provas do Enem: domingos 8 e 15 de novembro.",
         "+40%: as buscas por «como morar fora do Brasil» depois do 1º turno."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "OS JOVENS EM NÚMEROS", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E você? Qual é o seu plano para o ano que vem: estudar, trabalhar, viajar? Escreva duas frases em português."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap('내년 계획은 무엇인가요? 공부, 일, 여행? 두 문장을 써서 보내 주세요.', "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, 'E VOCÊ? · 여러분 이야기', 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, '내년 계획은 무엇인가요? 공부, 일, 여행? 두 문장을 써서 보내 주세요.', 20, "sans", False, GREY, CW - 44, 1.42)
ky3 = ey3 + eh + 26
kb = ("Num agregador de tendências, na terça-feira, 20 de outubro, «mega-sena» aparecia como a busca número um do Brasil. É um dado de agregador, não do feed oficial do Google — mas a lição fica: em semana de eleição, o brasileiro também sonha com a loteria.")
kh = 62 + len(wrap(kb, "serif", False, 21.5, CW - 44)) * 30.5 + 16
p.rect(ix, ky3, CW, kh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ky3 + 16
p.text(ix + 22, yy3 + 26, "E A MEGA-SENA?", 22, "sans", True, OLIVE)
yy3 += 52
p.para(ix + 22, yy3 + 21, kb, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P5 col3 ends", ky3 + kh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, 'EXERCÍCIOS · 제5면 연습 문제', 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, '정답은 8면에 · 등급이 섞인 문제예요. 번호로 찾으세요', 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · COMPREENSÃO", 25)
e.expl('5면 글을 읽고 맞는 답을 고르세요.')
e.ex("B1", '객관식', "B", 'Prova do Fazendeiro는 수요일 21일이에요',
     "A Prova do Fazendeiro de A Fazenda 18 é... A. na sexta-feira · B. na quarta-feira, 21 · C. no domingo, 25", size=20, gap=8)
e.ex("B1", '객관식', "C", 'Enem은 11월 8일과 15일이에요',
     "As provas do Enem 2026 são nos dias... A. 25 de outubro e 1º de novembro · B. 1º e 8 de novembro · C. 8 e 15 de novembro", size=20, gap=8)
e.ex("B1", '객관식', "A", '지원자가 500만 명이 넘어요',
     "O Enem 2026 tem... A. mais de 5 milhões de inscritos · B. 500 mil inscritos · C. 5 milhões de seções", size=20, gap=8)
e.ex("B1", '객관식', "B", '확인 카드는 시험 장소를 알려 줘요',
     "O Cartão de Confirmação mostra... A. a nota do aluno · B. o local da prova · C. o resultado final", size=20, gap=8)
e.ex("B1", '객관식', "C", '"해외에서 사는 법" 검색이 40% 늘었어요',
     "Depois do primeiro turno, cresceram 40% as buscas por... A. «guitarra» · B. «mega-sena» · C. «como morar fora do Brasil»", size=20, gap=8)
e.head("B · AS PALAVRAS DO TEXTO", 25)
e.expl('상자 속 단어로 채우세요. 복수형으로 바꿀 단어도 있어요.')
e.para("enquete · reta final · inscrito · véspera · levantamento · local", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", '문장 완성', "enquete", 'enquete = 시청자 투표/조사',
     "Na internet, a ___ pergunta quem fica no jogo.", instr='빈칸 채우기', size=20, gap=8)
e.ex("B1", '문장 완성', "inscritos", 'inscrito 복수형 맞춤: inscritos',
     "Mais de 5 milhões de estudantes estão ___ no Enem.", instr='빈칸 채우기', size=20, gap=8)
e.ex("B1", '문장 완성', "reta final", 'reta final = 막바지 단계',
     "Outubro é a ___ dos estudos: falta pouco para a prova.", instr='빈칸 채우기', size=20, gap=8)
e.ex("B1", '문장 완성', "véspera", 'véspera = 전날',
     "Na ___ da prova, o melhor é dormir cedo.", instr='빈칸 채우기', size=20, gap=8)
e.ex("B1", '문장 완성', "levantamento", 'levantamento = 조사, 통계',
     "Um ___ com dados do Google mediu as buscas.", instr='빈칸 채우기', size=20, gap=8)
e.ex("B1", '문장 완성', "local", 'local = 장소',
     "Confira o ___ da sua prova no cartão.", instr='빈칸 채우기', size=20, gap=8)
e.head("C · O FUTURO DO PRESENTE", 25)
e.expl('미래형(futuro do presente)으로 채우세요.')
e.ex("B1", '문장 완성', "farão", 'fazer 미래형 eles 불규칙 형태: farão',
     "Os estudantes ___ (fazer) a prova em novembro.", instr='빈칸 채우기', size=20, gap=8)
e.ex("B1", '문장 완성', "mostrará", 'mostrar 미래형: mostrará',
     "O cartão ___ (mostrar) o local da prova.", instr='빈칸 채우기', size=20, gap=8)
e.ex("B2", '문장 완성', "disputarão", 'disputar 미래형 복수: disputarão',
     "Três participantes ___ (disputar) a prova na quarta-feira.", instr='빈칸 채우기', size=20, gap=8)
e.ex("B2", '문장 완성', "ficará", 'ficar 미래형: ficará',
     "«Quem ___ (ficar) no jogo?» pergunta a enquete.", instr='빈칸 채우기', size=20, gap=8)
e.head("D · VERDADEIRO OU FALSO?", 25)
e.ex("B1", '진위 판단', "Verdadeiro", '확인 카드는 10월에 나와요',
     "O Cartão de Confirmação sai neste mês de outubro. Verdadeiro ou falso?", instr='참 / 거짓', size=20, gap=8)
e.ex("B1", '진위 판단', "Falso", '거짓: 검색 행동일 뿐 이민 자료가 아니에요',
     "As buscas por «morar fora» são um dado oficial de emigração. Verdadeiro ou falso?", instr='참 / 거짓', size=20, gap=8)
e.ex("B2", '진위 판단', "Verdadeiro", '참: 두 가지 "투표"가 같은 주에 있어요',
     "Na mesma semana, o Brasil vota no presidente e na enquete de um reality. Verdadeiro ou falso?", instr='참 / 거짓', size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jovens.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · APROFUNDAMENTO (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band('APROFUNDAMENTO · 심층', "A Lucerna", 'NÍVEL B2 · O segundo turno, explicado · 결선 투표 해설')

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1520, tag="P6-main")
f.title("O segundo turno: como o Brasil escolhe o presidente", 37)
f.byline("Da redação da A Lucerna · Nível de leitura: B2 · A política nacional brasileira")
f.para("No primeiro turno, no dia 4 de outubro, nenhum candidato à Presidência conseguiu mais da metade dos votos válidos. Por isso a Constituição manda repetir a disputa: é o segundo turno, neste domingo, 25 de outubro, só com os dois candidatos mais votados — Lula (PT) e Flávio Bolsonaro (PL).")
f.para("A regra é a maioria absoluta: vence quem tiver mais votos válidos no domingo. O mesmo acontece com os governadores em seis estados e no Distrito Federal, onde também ninguém venceu na primeira rodada.")
f.para("A campanha da última semana tem um centro: o debate. O calendário dos debates mostra o desenho da reta final — a Band fez o seu no domingo, 18 de outubro, às 20h; os debates da Record (11 de outubro) e do pool do SBT (15 de outubro) foram cancelados; e o último encontro é o da TV Globo, na sexta-feira, 23, depois do Jornal Nacional, com mediação de César Tralli e os dois candidatos convidados. Na mesma sexta-feira, termina a propaganda eleitoral gratuita.")
f.para("E os números? Cuidado com a confusão da semana: as porcentagens que circulam — eleições +900%, presidente +250%, multa eleitoral +350% — são dados de busca do Google, publicados antes e depois do primeiro turno. Interesse de busca não é intenção de voto: medir cliques não é medir urnas. Nesta edição, a A Lucerna não publica nenhuma porcentagem como se fosse pesquisa eleitoral.")
f.gloss('os votos válidos 유효표 · a maioria absoluta 절대다수 · vencer 이기다 · a campanha 선거 운동 · a intenção de voto 투표 의향.')
f.end_report()

# col 3: timeline + ler os números (sequential, measured)
bx = COLX[3]
p.rect(bx, 200, CW, 640, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 240, "O CAMINHO ATÉ A URNA", 22, "sans", True, OLIVE)
steps = [
    ("4 OUT.", "Primeiro turno: nenhum candidato passa da metade dos votos válidos."),
    ("18 OUT.", "Debate da Band, às 20h, no primeiro domingo da reta final."),
    ("23 OUT.", "Último debate, na TV Globo, depois do Jornal Nacional; fim da propaganda gratuita."),
    ("25 OUT.", "Segundo turno: votação das 8h às 17h, hora de Brasília."),
]
sy3 = 282
for w, t in steps:
    p.text(bx + 22, sy3 + 21, w, 20, "sans", True, BRICK)
    sy3 = p.para(bx + 164, sy3 + 21, t, 21, "serif", False, INK, CW - 186, 1.4) + 16
by3 = 866
bb = ("Diante de uma porcentagem, faça três perguntas: quem publica? Quando? "
      "É busca, voto ou pesquisa? Sem essas respostas, um número diz pouco.")
bh = 62 + len(wrap(bb, "serif", False, 21.5, CW - 44)) * 30.5 + 16
p.rect(bx, by3, CW, bh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = by3 + 16
p.text(bx + 22, yy3 + 26, "LER OS NÚMEROS", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, bb, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P6 col3 ends", by3 + bh)

# ---- search-data charts (Google data, honestly captioned) ----
gy = 1566
p.hline(MX, RIGHT, gy - 18, GOLD, 2)
p.text(MX, gy + 10, 'AS BUSCAS DO 1º TURNO · 1차 투표 전후의 검색 증가 (dados do Google)', 26, "sans", True, OLIVE)
bw_ = 2 * CW + GUT
# left box: Google panel, 7 Oct
bx1 = MX
p.rect(bx1, gy + 28, bw_, 322, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx1 + 22, gy + 68, "O PAINEL DO GOOGLE · painel de 7 de outubro", 21, "sans", True, INK)
painel = [("eleições", 900), ("presidente", 250)]
yy = gy + 100
for lab, v in painel:
    p.text(bx1 + 22, yy + 24, lab, 20, "serif", True, INK)
    labw = text_w(lab, "serif", True, 20)
    p.rect(bx1 + 40 + labw, yy + 6, v * 0.37, 22, fill=OLIVE)
    p.text(bx1 + 58 + labw + v * 0.37, yy + 24, f"+{v}%", 20.5, "serif", False, INK)
    yy += 44
p.para(bx1 + 22, gy + 218, "Crescimento do interesse de busca contra a semana anterior ao primeiro turno. É comportamento de busca — não é intenção de voto.", 19.5, "serif", False, INK, bw_ - 44, 1.4)
p.para(bx1 + 22, gy + 322 - 34, "Fonte: Google, dados publicados depois do 1º turno.", 17.5, "sans", False, GREY, bw_ - 44, 1.3)
# right box: voters' questions (Google via UOL)
bx2 = COLX[2]
p.rect(bx2, gy + 28, bw_, 322, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx2 + 22, gy + 68, "AS PERGUNTAS DO ELEITOR · mais buscas", 21, "sans", True, INK)
perg = [("que horas começa a votação?", 550), ("multa eleitoral", 350), ("seção eleitoral", 350)]
yy = gy + 100
for lab, v in perg:
    p.text(bx2 + 22, yy + 24, lab, 20, "serif", True, INK)
    labw = text_w(lab, "serif", True, 20)
    p.rect(bx2 + 40 + labw, yy + 6, v * 0.37, 22, fill=GOLD)
    p.text(bx2 + 58 + labw + v * 0.37, yy + 24, f"+{v}%", 20.5, "serif", False, INK)
    yy += 40
p.para(bx2 + 22, gy + 230, "As perguntas práticas do eleitor também explodiram nas buscas: horário, multa e o lugar de votar.", 19.5, "serif", False, INK, bw_ - 44, 1.4)
p.para(bx2 + 22, gy + 322 - 34, "Fonte: dados do Google publicados pela imprensa (UOL).", 17.5, "sans", False, GREY, bw_ - 44, 1.3)

# ---- P6 exercises ----
ey = 1930
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, 'EXERCÍCIOS · 제6면 연습 문제', 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, '정답은 8면에 · 등급이 섞인 문제예요. 번호로 찾으세요', 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · LER OS GRÁFICOS", 25)
e.expl('위 두 그림을 보고 맞는 답을 고르세요.')
e.ex("B2", '객관식', "B", '가장 많이 는 것은 eleições, +900%예요',
     "No painel do Google, a busca que mais cresceu foi... A. presidente, +250% · B. eleições, +900% · C. multa eleitoral, +350%", size=17, gap=0)
e.ex("B2", '객관식', "A", '«presidente»는 +250% 늘었어요',
     "A busca «presidente» cresceu... A. +250% · B. +900% · C. +350%", size=17, gap=0)
e.ex("B2", '객관식', "C", '"투표가 몇 시에 시작하나요?"가 +550% 늘었어요',
     "A pergunta «que horas começa a votação?» cresceu... A. +300% · B. +350% · C. +550%", size=17, gap=0)
e.ex("B2", '객관식', "A", '350 + 350 = 700 포인트',
     "«Multa eleitoral» (+350%) e «seção eleitoral» (+350%), juntas, somam... A. 700 pontos · B. 350 pontos · C. 900 pontos", size=17, gap=0)
e.ex("B2", '객관식', "B", "900 − 250 = 650",
     "A diferença entre «eleições» (+900%) e «presidente» (+250%) é de... A. 1.150 · B. 650 · C. 450", size=17, gap=0)
e.ex("B2", '객관식', "B", '검색 관심도는 투표 의향이 아니에요',
     "Os dados do painel são... A. uma pesquisa eleitoral oficial · B. interesse de busca, não intenção de voto · C. o resultado da eleição", size=17, gap=0)
e.head("B · COMPREENSÃO", 25)
e.ex("B2", '객관식', "B", '아무도 유효표 과반을 얻지 못했기 때문이에요',
     "O segundo turno existe porque... A. o 1º turno foi cancelado · B. nenhum candidato passou da metade dos votos válidos · C. os debates acabaram", size=17, gap=0)
e.ex("B2", '객관식', "A", '유효표를 더 많이 얻은 사람이 이겨요',
     "No segundo turno, vence... A. quem tiver mais votos válidos · B. quem vencer o debate · C. quem tiver mais buscas no Google", size=17, gap=0)
e.ex("B2", '객관식', "B", '6개 주와 연방구에 주지사 결선 투표가 있어요',
     "Além da Presidência, há segundo turno para governador em... A. todos os estados · B. seis estados e no DF · C. dois estados", size=17, gap=0)
e.ex("B2", '객관식', "C", 'Record와 SBT pool 토론이 취소됐어요',
     "Na reta final, os debates cancelados foram... A. o da Globo e o da Band · B. só o da Band · C. o da Record e o do pool do SBT", size=17, gap=0)
e.head("C · OS TEMPOS DO TEXTO", 25)
e.expl('문장 뜻에 맞게 올바른 동사형으로 채우세요.')
e.ex("B2", '문장 완성', "vencerá", '미래형: vencerá',
     "No domingo, ___ (vencer) o candidato com mais votos válidos.", instr='빈칸 채우기', size=17, gap=0)
e.ex("B2", '문장 완성', "tiver", 'quem 뒤 미래 가정법: tiver',
     "Vence quem ___ (ter) mais votos válidos.", instr='빈칸 채우기', size=17, gap=0)
e.ex("B2", '문장 완성', "foram", '과거형 복수: foram cancelados',
     "Os debates da Record e do SBT ___ (ser) cancelados.", instr='빈칸 채우기', size=17, gap=0)
e.ex("B2", '문장 완성', "termina", '현재형: termina',
     "Na sexta-feira, ___ (terminar) a propaganda eleitoral gratuita.", instr='빈칸 채우기', size=17, gap=0)
e.head("D · AS PALAVRAS DO DEBATE", 25)
e.expl('상자 속 단어로 채우세요: segundo turno · maioria absoluta · votos válidos · intenção de voto')
e.ex("B2", '문장 완성', "segundo turno", 'segundo turno = 결선 투표',
     "A disputa final entre os dois mais votados é o ___.", instr='빈칸 채우기', size=17, gap=0)
e.ex("B2", '문장 완성', "votos válidos", 'votos válidos = 유효표 (백표와 무효표는 빼요)',
     "Só contam os ___: brancos e nulos ficam fora.", instr='빈칸 채우기', size=17, gap=0)
e.ex("B2", '문장 완성', "maioria absoluta", 'maioria absoluta = 절대다수',
     "Vencer com mais da metade é vencer por ___.", instr='빈칸 채우기', size=17, gap=0)
e.ex("B2", '문장 완성', "intenção de voto", '검색량으로는 투표 의향을 잴 수 없어요',
     "Busca no Google não mede ___.", instr='빈칸 채우기', size=17, gap=0)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-aprofundamento.svg")
print("P6 saved, exercises so far:", len(REG))
