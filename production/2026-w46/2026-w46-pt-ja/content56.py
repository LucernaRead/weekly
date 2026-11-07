# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-pt-ja/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · JOVENS (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JOVENS · 若者", "A Lucerna", "レベル B1 · 若者たちの最後の一週間")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-main")
f.title("A última semana: revisar Natureza e Matemática", 37)
f.byline("Da redação da A Lucerna · Nível de leitura: B1")
f.para("A semana dos jovens brasileiros tem um centro: o domingo 15. Para os mais de 5 milhões de inscritos no Enem, é a última semana antes de Ciências da Natureza e Matemática — 90 questões em cinco horas.")
f.para("O plano cabe em cinco linhas: conferir o Cartão de Confirmação, revisar um pouco por dia — biologia, física, química e matemática —, dormir bem na véspera, separar documento e caneta preta no dia anterior — e, no domingo, chegar cedo. Nada de maratona na véspera: quem dorme bem lembra melhor.")
f.para("E a semana tem mais: na quarta, 11, começam as promoções do 11.11 — a dica é comparar preços antes de comprar, porque a Black Friday é só no dia 27. No sábado, 14, o Brasil acorda cedo para a Seleção: Japão × Brasil, às 7h15, em Singapura.")
f.para("E Interlagos recebeu o Grande Prêmio de São Paulo, de 6 a 8 de novembro: 71 voltas no domingo, sem corrida sprint nesta edição. Agora é silêncio e revisão: a semana é para descansar o corpo e organizar a cabeça — e o domingo 15 decide a segunda metade da prova.")
f.box("O PLANO DA ÚLTIMA SEMANA", [
    ("1. Confira o Cartão de Confirmação do Enem（Enem 確認カードを確認）", "serif", False, INK, 21, 1.36),
    ("2. Revise um pouco por dia: Natureza e Matemática（毎日少し復習：自然科学と数学）", "serif", False, INK, 21, 1.36),
    ("3. Durma bem na véspera da prova（試験前夜はよく眠る）", "serif", False, INK, 21, 1.36),
    ("4. Separe documento e caneta preta no dia anterior（前日に身分証と黒ペンを用意）", "serif", False, INK, 21, 1.36),
    ("5. Domingo 15: chegue antes das 12h（日曜 15 日：12 時前に到着）", "serif", False, INK, 21, 1.36),
])
f.gloss("a natureza = 自然科学 · a matemática = 数学 · a maratona = 詰め込みマラソン · a véspera = 前夜 · comparar = 値段を比べる · a cabeça = 頭、調子。")
f.end_report()

# col 3: facts + e você + 11.11 box (sequential)
ix = COLX[3]
facts = ["Mais de 5 milhões de inscritos no Enem 2026 (Inep).",
         "Prova do dia 15: 13h30–18h30, cinco horas, 90 questões.",
         "Dia 20: Consciência Negra, feriado nacional (prévia)."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "OS JOVENS EM NÚMEROS", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E você? Na véspera de uma prova importante, você revisa até tarde ou dorme cedo? Escreva duas frases em português."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("大事な試験の前夜、遅くまで復習しますか、それとも早く寝ますか。2 文書いて送ってください。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E VOCÊ? · あなたは？", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "大事な試験の前夜、遅くまで復習しますか、それとも早く寝ますか。2 文書いて送ってください。", 20, "sans", False, GREY, CW - 44, 1.42)
ky3 = ey3 + eh + 26
kb = "Quarta, 11: o dia das promoções abre a temporada de ofertas. Compare preços, faça uma lista e não compre por impulso — a Black Friday é no dia 27."
kh = 62 + len(wrap(kb, "serif", False, 21.5, CW - 44)) * 30.5 + 16
p.rect(ix, ky3, CW, kh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ky3 + 16
p.text(ix + 22, yy3 + 26, "E O 11.11?", 22, "sans", True, OLIVE)
yy3 += 52
p.para(ix + 22, yy3 + 21, kb, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P5 col3 ends", ky3 + kh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EXERCÍCIOS · 5 ページの練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "解答は 8 ページ · レベル混合 — 番号で探すこと", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · COMPREENSÃO", 25)
e.bridge("5 ページの記事を読んで正しい答えを選ぼう。")
e.ex("B1", "選択問題", "B", "最後の一週間は 11 月 15 日（日）に終わる",
     "A última semana termina... A. na segunda 9 · B. no domingo 15 · C. no dia 20", size=20, gap=8)
e.ex("B1", "選択問題", "B", "毎日少し復習",
     "O plano da última semana inclui... A. maratona na véspera · B. revisar um pouco por dia · C. chegar às 13h30", size=20, gap=8)
e.ex("B1", "選択問題", "A", "前日に身分証と黒ペンを用意",
     "No dia anterior, o candidato separa... A. documento e caneta preta · B. só o celular · C. a roupa da festa", size=20, gap=8)
e.ex("B1", "選択問題", "B", "ブラックフライデーは 11 月 27 日",
     "A Black Friday é... A. no dia 11 · B. no dia 27 · C. no dia 15", size=20, gap=8)
e.ex("B1", "選択問題", "B", "11 月 14 日（土）ブラジル × 日本 7:15",
     "No sábado, 14, a Seleção joga... A. às 18h30 · B. às 7h15, contra o Japão · C. no domingo 15", size=20, gap=8)
e.head("B · AS PALAVRAS DO TEXTO", 25)
e.bridge("枠の中の言葉で埋めよう。注意：複数形にする言葉がある。")
e.para("última semana · inscrito · véspera · maratona · local · separar", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "文を完成させる", "última semana", "última semana = 最後の一週間",
     "A semana é a ___ antes da prova.", instr="空欄を埋める", size=20, gap=8)
e.ex("B1", "文を完成させる", "inscritos", "inscrito は複数形に合わせる：inscritos",
     "Mais de 5 milhões de estudantes estão ___ no Enem.", instr="空欄を埋める", size=20, gap=8)
e.ex("B1", "文を完成させる", "véspera", "véspera = 前夜",
     "Na ___ da prova, durma bem.", instr="空欄を埋める", size=20, gap=8)
e.ex("B1", "文を完成させる", "maratona", "maratona = 詰め込みマラソン",
     "Nada de ___ na véspera.", instr="空欄を埋める", size=20, gap=8)
e.ex("B1", "文を完成させる", "local", "local = 場所",
     "Confira o ___ da sua prova no cartão.", instr="空欄を埋める", size=20, gap=8)
e.ex("B1", "文を完成させる", "Separe", "separar 命令形：separe",
     "___ o documento no dia anterior.", instr="空欄を埋める", size=20, gap=8)
e.head("C · O FUTURO DO PRESENTE", 25)
e.bridge("未来形（futuro do presente）で補おう。")
e.ex("B1", "文を完成させる", "farão", "fazer 未来形 eles 不規則形：farão",
     "Os estudantes ___ (fazer) a prova no domingo.", instr="空欄を埋める", size=20, gap=8)
e.ex("B1", "文を完成させる", "mostrará", "mostrar 未来形：mostrará",
     "O cartão ___ (mostrar) o local da prova.", instr="空欄を埋める", size=20, gap=8)
e.ex("B2", "文を完成させる", "sairão", "sair 未来形複数：sairão",
     "Os finalistas ___ (sair) dos jogos de volta.", instr="空欄を埋める", size=20, gap=8)
e.ex("B2", "文を完成させる", "chegará", "chegar 未来形：chegará",
     "Quem ___ (chegar) cedo não perde a prova.", instr="空欄を埋める", size=20, gap=8)
e.head("D · VERDADEIRO OU FALSO?", 25)
e.ex("B1", "正誤判定", "Verdadeiro", "確認カードに試験会場が書かれている",
     "O Cartão de Confirmação mostra o local da prova. Verdadeiro ou falso?", instr="正しいか間違いか", size=20, gap=8)
e.ex("B1", "正誤判定", "Falso", "誤り：前夜の詰め込みは良い計画ではない。毎日少しずつが良い",
     "A maratona na véspera é o melhor plano. Verdadeiro ou falso?", instr="正しいか間違いか", size=20, gap=8)
e.ex("B2", "正誤判定", "Verdadeiro", "正しい：13:30 から 18:30",
     "No domingo 15, a prova vai de 13h30 a 18h30. Verdadeiro ou falso?", instr="正しいか間違いか", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jovens.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · APROFUNDAMENTO (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("APROFUNDAMENTO · 深読み", "A Lucerna", "レベル B2 · 第 2 の日曜日を解説")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1520, tag="P6-main")
f.title("O segundo domingo explicado: 90 questões, 300 minutos", 37)
f.byline("Da redação da A Lucerna · Nível de leitura: B2")
f.para("O Enem 2026 tem dois domingos: 8 e 15 de novembro. No dia 8, o primeiro: redação, Linguagens e Ciências Humanas, das 13h30 às 19h — cinco horas e meia. No dia 15, o segundo: Ciências da Natureza e Matemática, das 13h30 às 18h30 — cinco horas. Esta edição cobre o dia 15; o dia 8 já ficou para trás.")
f.para("O ritual do domingo 15 começa ao meio-dia: os portões abrem às 12h e fecham às 13h, no horário de Brasília. Quem chega depois das 13h não entra — não há segunda chamada. Leve documento com foto, caneta preta e o Cartão de Confirmação: ele mostra o seu local de prova.")
f.para("Mais de 5 milhões de estudantes estão inscritos. É muita gente para o mesmo horário: por isso o Inep pede que cada um confira o local antes do domingo. Quem confere antes não se perde no dia — e no feriado, confira também o transporte.")
f.para("E os números do domingo? Cinco horas são 300 minutos: 60 minutos para cada hora, vezes cinco. É tempo para ler com calma, calcular e revisar — sem correria. A regra de ouro do segundo dia: primeiro as fáceis, depois as difíceis, e tempo guardado para revisar no fim.")
f.gloss("os portões = 門 · a segunda chamada = 追試・2 度目の入場 · conferir = 確認する · a correria = あわただしさ。")
f.end_report()

# col 3: timeline + ler os números (sequential, measured)
bx = COLX[3]
p.rect(bx, 200, CW, 640, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 240, "O CAMINHO ATÉ A PROVA", 22, "sans", True, OLIVE)
steps = [
    ("9 NOV.", "Começa a semana do segundo dia do Enem."),
    ("11 NOV.", "11.11: o dia das promoções no comércio eletrônico."),
    ("14 NOV.", "Seleção × Japão, às 7h15; Mirassol × Atlético, às 18h30."),
    ("15 NOV.", "Enem, dia 2: Natureza e Matemática + feriado."),
    ("20 NOV.", "Consciência Negra, feriado nacional (prévia)."),
]
sy3 = 282
for w, t in steps:
    p.text(bx + 22, sy3 + 21, w, 20, "sans", True, BRICK)
    sy3 = p.para(bx + 164, sy3 + 21, t, 21, "serif", False, INK, CW - 186, 1.4) + 16
by3 = 866
bb = ("Diante de um número, faça três perguntas: quem publica? Quando? "
      "É busca, prova ou pesquisa? Sem essas respostas, um número diz pouco.")
bh = 62 + len(wrap(bb, "serif", False, 21.5, CW - 44)) * 30.5 + 16
p.rect(bx, by3, CW, bh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = by3 + 16
p.text(bx + 22, yy3 + 26, "LER OS NÚMEROS", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, bb, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P6 col3 ends", by3 + bh)

# ---- charts: o domingo 15 em minutos + dois domingos ----
gy = 1566
p.hline(MX, RIGHT, gy - 18, GOLD, 2)
p.text(MX, gy + 10, "O DOMINGO 15 EM NÚMEROS · 11 月 15 日の数字（Inep 公式時間）", 26, "sans", True, OLIVE)
bw_ = 2 * CW + GUT
# left box: o relógio do domingo (minutos)
bx1 = MX
p.rect(bx1, gy + 28, bw_, 322, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx1 + 22, gy + 68, "O RELÓGIO DO DOMINGO · do meio-dia às 18h30", 21, "sans", True, INK)
relog = [("portões abertos", 60), ("espera", 30), ("prova", 300)]
yy = gy + 100
for lab, v in relog:
    p.text(bx1 + 22, yy + 24, lab, 20, "serif", True, INK)
    labw = text_w(lab, "serif", True, 20)
    p.rect(bx1 + 40 + labw, yy + 6, v * 1.5, 22, fill=OLIVE)
    p.text(bx1 + 58 + labw + v * 1.5, yy + 24, f"{v} min", 20.5, "serif", False, INK)
    yy += 44
p.para(bx1 + 22, gy + 248, "Minutos do domingo 15: 60 + 30 + 300 = 390 minutos do meio-dia às 18h30.", 19.5, "serif", False, INK, bw_ - 44, 1.4)
p.para(bx1 + 22, gy + 322 - 34, "Fonte: horários oficiais do Inep para o dia 15.", 17.5, "sans", False, GREY, bw_ - 44, 1.3)
# right box: dois domingos
bx2 = COLX[2]
p.rect(bx2, gy + 28, bw_, 322, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx2 + 22, gy + 68, "DOIS DOMINGOS · uma prova", 21, "sans", True, INK)
doms = [
    "Dia 8 — redação, Linguagens, Humanas.",
    "Dia 8 — 13h30 às 19h, cinco horas e meia.",
    "Dia 15 — Natureza e Matemática.",
    "Dia 15 — 13h30 às 18h30, cinco horas.",
]
yy = gy + 100
for t in doms:
    p.text(bx2 + 22, yy + 24, t, 20, "serif", False, INK)
    yy += 40
p.para(bx2 + 22, gy + 322 - 34, "Fonte: Inep — as provas são nos dias 8 e 15.", 17.5, "sans", False, GREY, bw_ - 44, 1.3)

# ---- P6 exercises ----
ey = 1930
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EXERCÍCIOS · 6 ページの練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "解答は 8 ページ · レベル混合 — 番号で探すこと", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · LER OS GRÁFICOS", 25)
e.bridge("上の 2 つの図を見て正しい答えを選ぼう。")
e.ex("B2", "選択問題", "B", "門は 60 分間開いている",
     "No relógio do domingo, os portões ficam abertos... A. 30 minutos · B. 60 minutos · C. 300 minutos", size=17, gap=0)
e.ex("B2", "選択問題", "A", "閉門から試験開始までの待ち時間は 30 分",
     "A espera entre o fechamento e a prova é de... A. 30 minutos · B. 60 minutos · C. 300 minutos", size=17, gap=0)
e.ex("B2", "選択問題", "B", "試験は 300 分",
     "A prova dura... A. 60 minutos · B. 300 minutos · C. 390 minutos", size=17, gap=0)
e.ex("B2", "選択問題", "B", "60 + 30 + 300 = 390",
     "60 + 30 + 300 = ... A. 360 · B. 390 · C. 420", size=17, gap=0)
e.ex("B2", "選択問題", "B", "正午から 18:30 = 6 時間半",
     "Do meio-dia às 18h30 são... A. 5h · B. 6h30 · C. 7h", size=17, gap=0)
e.ex("B2", "選択問題", "A", "図の数字は Inep の公式時間",
     "Os números do gráfico são... A. horários oficiais do Inep · B. uma pesquisa eleitoral · C. buscas no Google", size=17, gap=0)
e.head("B · COMPREENSÃO", 25)
e.ex("B2", "選択問題", "B", "Enem は 8 日と 15 日の 2 つの日曜日に分かれる",
     "O Enem tem... A. um só domingo · B. dois domingos: 8 e 15 · C. três domingos", size=17, gap=0)
e.ex("B2", "選択問題", "B", "第 2 日は自然科学と数学",
     "No dia 15, a prova tem... A. redação · B. Natureza e Matemática · C. só Matemática", size=17, gap=0)
e.ex("B2", "選択問題", "B", "13 時を過ぎると入場できない",
     "Quem chega depois das 13h... A. entra atrasado · B. não entra · C. faz a prova no dia 8", size=17, gap=0)
e.ex("B2", "選択問題", "B", "確認カードに試験会場が書かれている",
     "O Cartão de Confirmação mostra... A. a nota · B. o local da prova · C. o gabarito", size=17, gap=0)
e.head("C · OS TEMPOS DO TEXTO", 25)
e.bridge("文の意味に合う正しい動詞の形で補おう。")
e.ex("B2", "文を完成させる", "começará", "未来形：começará",
     "No domingo, ___ (começar) a prova às 13h30.", instr="空欄を埋める", size=17, gap=0)
e.ex("B2", "文を完成させる", "chegar", "quem + 未来接続法：chegar",
     "Quem ___ (chegar) depois das 13h não entra.", instr="空欄を埋める", size=17, gap=0)
e.ex("B2", "文を完成させる", "fecham", "現在形：fecham",
     "Os portões ___ (fechar) às 13h.", instr="空欄を埋める", size=17, gap=0)
e.ex("B2", "文を完成させる", "pede", "現在形：pede",
     "O Inep ___ (pedir) que cada um confira o local.", instr="空欄を埋める", size=17, gap=0)
e.head("D · AS PALAVRAS DA PROVA", 25)
e.bridge("枠の中の言葉で埋めよう：portões · segunda chamada · local · conferir")
e.ex("B2", "文を完成させる", "portões", "portões = 門",
     "Os ___ abrem às 12h.", instr="空欄を埋める", size=17, gap=0)
e.ex("B2", "文を完成させる", "segunda chamada", "segunda chamada = 追試・2 度目の入場",
     "Não há ___ no Enem.", instr="空欄を埋める", size=17, gap=0)
e.ex("B2", "文を完成させる", "local", "local = 場所",
     "Confira o ___ da sua prova.", instr="空欄を埋める", size=17, gap=0)
e.ex("B2", "文を完成させる", "Confira", "命令形：confira",
     "___ o cartão antes do domingo.", instr="空欄を埋める", size=17, gap=0)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-aprofundamento.svg")
print("P6 saved, exercises so far:", len(REG))
