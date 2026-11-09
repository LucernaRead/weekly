# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · JOVENS (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JOVENS　若者", "A Lucerna", "NÍVEL B1　A reta final dos jovens　ラストスパートの週：若者の最後の一週間")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-main")
f.title("A reta final: revisar, descansar, fazer a prova", 32)
f.byline("Da redação da A Lucerna　Nível de leitura: B1")
f.para("A semana dos jovens brasileiros tem um centro: o domingo 8. Para os mais de 5 milhões de inscritos no Enem, é a reta final — a última semana de revisão antes da redação, de Linguagens e de Ciências Humanas.")
f.para("O plano da reta final cabe em cinco linhas: conferir o Cartão de Confirmação, revisar um pouco por dia, dormir bem na véspera, separar documento e caneta preta no dia anterior — e, no domingo, chegar cedo. Nada de maratona na véspera: quem dorme bem lembra melhor.")
f.para("E a semana tem mais: na terça, 3, as assembleias estaduais voltam do recesso; no sábado e no domingo, a Copa do Brasil decide os finalistas. O Brasil estuda de dia e torce à noite.")
f.para("No sábado, 31 de outubro, foi Halloween: a última festa antes da prova para muita gente. Agora é silêncio e revisão: o feriadão é para descansar o corpo e organizar a cabeça.")
f.box("O PLANO DA RETA FINAL", [
    ("1. Confira o Cartão de Confirmação do Enem（Enemの確認カードを確かめる）", "serif", False, INK, 21, 1.36),
    ("2. Revise um pouco por dia, sem maratona（毎日少しずつ復習し、詰め込みはしない）", "serif", False, INK, 21, 1.36),
    ("3. Durma bem na véspera da prova（試験前夜はよく眠る）", "serif", False, INK, 21, 1.36),
    ("4. Separe documento e caneta preta no dia anterior（前日に身分証と黒ペンを用意する）", "serif", False, INK, 21, 1.36),
    ("5. Domingo 8: chegue antes das 12h（日曜日8日：12時前に着く）", "serif", False, INK, 21, 1.36),
])
f.gloss("a reta final ラストスパート · a véspera 前夜 · a maratona 詰め込み勉強 · separar 用意する · a cabeça 頭、心の状態。")
f.end_report()

# col 3: facts + e você + copa box (sequential)
ix = COLX[3]
facts = ["Mais de 5 milhões de inscritos no Enem 2026 (Inep).",
         "Prova do dia 8: 13h30–19h, cinco horas e meia.",
         "Dia 15: o segundo dia — Natureza e Matemática (prévia)."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "OS JOVENS EM NÚMEROS", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E você? Qual é o seu plano para a véspera de uma prova importante: revisar ou descansar? Escreva duas frases em português."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("大事な試験の前夜、復習しますか、休息しますか。2文を書いて送ってください。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E VOCÊ?　あなたは？", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "大事な試験の前夜、復習しますか、休息しますか。2文を書いて送ってください。", 20, "sans", False, GREY, CW - 44, 1.42)
ky3 = ey3 + eh + 26
kb = "No fim de semana, o Brasil troca o livro pela bola: sábado, Atlético-MG × Grêmio; domingo, Vasco × Palmeiras. Estudar de dia, torcer à noite — a semana cabe nos dois."
kh = 62 + len(wrap(kb, "serif", False, 21.5, CW - 44)) * 30.5 + 16
p.rect(ix, ky3, CW, kh, fill=BOX)
yy3 = ky3 + 16
p.text(ix + 22, yy3 + 26, "E A COPA?", 22, "sans", True, OLIVE)
yy3 += 52
p.para(ix + 22, yy3 + 21, kb, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P5 col3 ends", ky3 + kh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EXERCÍCIOS　5ページの練習問題", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答えは8ページ　レベル混在の出題です。番号で答えを探してください", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A　COMPREENSÃO", 25)
e.bridge("5ページの記事を読んで、正しい答えを選んでください。")
e.ex("B1", "選択問題", "B", "ラストスパートの週は11月8日日曜日に終わる",
     "A reta final termina... A. na segunda 2 · B. no domingo 8 · C. no dia 15", size=20, gap=8)
e.ex("B1", "選択問題", "B", "毎日少しずつ復習する",
     "O plano da reta final inclui... A. maratona na véspera · B. revisar um pouco por dia · C. chegar às 13h30", size=20, gap=8)
e.ex("B1", "選択問題", "A", "前日に身分証と黒ペンを用意する",
     "No dia anterior, o candidato separa... A. documento e caneta preta · B. só o celular · C. a roupa da festa", size=20, gap=8)
e.ex("B1", "選択問題", "B", "第2日は自然科学と数学",
     "O segundo dia do Enem (dia 15) tem... A. redação · B. Natureza e Matemática · C. só Linguagens", size=20, gap=8)
e.ex("B1", "選択問題", "B", "11月3日火曜日、各州議会が休会を終える",
     "Na terça, 3, ... A. é o Enem · B. as assembleias voltam do recesso · C. é a final da Copa", size=20, gap=8)
e.head("B　AS PALAVRAS DO TEXTO", 25)
e.bridge("枠内の語を使って空所を補ってください。注意：複数形に変える語もあります。")
e.para("reta final · inscrito · véspera · maratona · local · separar", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "文の完成", "reta final", "reta final = ラストスパートの時期",
     "A semana é a ___ dos estudos.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "inscritos", "inscrito 複数への一致：inscritos",
     "Mais de 5 milhões de estudantes estão ___ no Enem.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "véspera", "véspera = 前夜",
     "Na ___ da prova, durma bem.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "maratona", "maratona = 詰め込み勉強",
     "Nada de ___ na véspera.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "local", "local = 場所",
     "Confira o ___ da sua prova no cartão.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "Separe", "separar 命令形：separe",
     "___ o documento no dia anterior.", instr="空所補充", size=20, gap=8)
e.head("C　O FUTURO DO PRESENTE", 25)
e.bridge("未来形（futuro do presente）で補ってください。")
e.ex("B1", "文の完成", "farão", "fazer 未来形 eles の不規則形：farão",
     "Os estudantes ___ (fazer) a prova no domingo.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "mostrará", "mostrar 未来形：mostrará",
     "O cartão ___ (mostrar) o local da prova.", instr="空所補充", size=20, gap=8)
e.ex("B2", "文の完成", "sairão", "sair 未来形複数：sairão",
     "Os finalistas ___ (sair) dos jogos de volta.", instr="空所補充", size=20, gap=8)
e.ex("B2", "文の完成", "chegará", "chegar 未来形：chegará",
     "Quem ___ (chegar) cedo não perde a prova.", instr="空所補充", size=20, gap=8)
e.head("D　VERDADEIRO OU FALSO?", 25)
e.ex("B1", "正誤判断", "Verdadeiro", "確認カードに試験会場が載っている",
     "O Cartão de Confirmação mostra o local da prova. Verdadeiro ou falso?", instr="正誤", size=20, gap=8)
e.ex("B1", "正誤判断", "Falso", "誤り：前夜の詰め込みは良い計画ではなく、毎日少しずつ復習するのが良い",
     "A maratona na véspera é o melhor plano. Verdadeiro ou falso?", instr="正誤", size=20, gap=8)
e.ex("B2", "正誤判断", "Verdadeiro", "正しい：13:30から19:00",
     "No domingo 8, a prova vai de 13h30 a 19h. Verdadeiro ou falso?", instr="正誤", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jovens.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · APROFUNDAMENTO (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("APROFUNDAMENTO　深掘り", "A Lucerna", "NÍVEL B2　O Enem explicado　Enemを解説")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1520, tag="P6-main")
f.title("O Enem explicado: dois domingos, uma prova", 32)
f.byline("Da redação da A Lucerna　Nível de leitura: B2")
f.para("O Enem 2026 tem dois domingos: 8 e 15 de novembro. No dia 8, o primeiro: redação, Linguagens e Ciências Humanas, das 13h30 às 19h — cinco horas e meia. No dia 15, o segundo: Ciências da Natureza e Matemática. Esta edição cobre o dia 8; o dia 15 é a prévia da próxima semana.")
f.para("O ritual do domingo 8 começa ao meio-dia: os portões abrem às 12h e fecham às 13h, no horário de Brasília. Quem chega depois das 13h não entra — não há segunda chamada. Leve documento com foto, caneta preta e o Cartão de Confirmação: ele mostra o seu local de prova.")
f.para("Mais de 5 milhões de estudantes estão inscritos. É muita gente para o mesmo horário: por isso o Inep pede que cada um confira o local antes do domingo. Quem confere antes não se perde no dia.")
f.para("E os números do domingo? Cinco horas e meia são 330 minutos: 60 minutos para cada hora, mais 30. É tempo para ler com calma, escrever a redação e revisar — sem correria. A regra de ouro do Enem: primeiro as fáceis, depois as difíceis, e a redação com tempo guardado.")
f.gloss("os portões 門 · a segunda chamada 追試、2回目の入場 · conferir 確かめる · a correria あわただしさ。")
f.end_report()

# col 3: timeline + ler os números (sequential, measured)
bx = COLX[3]
p.rect(bx, 200, CW, 640, fill=BOX)
p.text(bx + 22, 240, "O CAMINHO ATÉ A PROVA", 22, "sans", True, OLIVE)
steps = [
    ("2 NOV.", "Finados: feriadão de revisão, um pouco por dia."),
    ("3 NOV.", "As assembleias estaduais voltam do recesso."),
    ("8 NOV.", "Enem, dia 1: portões 12h–13h, prova 13h30–19h."),
    ("15 NOV.", "Enem, dia 2 (prévia): Natureza e Matemática."),
]
sy3 = 282
for w, t in steps:
    p.text(bx + 22, sy3 + 21, w, 20, "sans", True, OLIVE)
    sy3 = p.para(bx + 164, sy3 + 21, t, 21, "serif", False, INK, CW - 186, 1.4) + 16
by3 = 866
bb = ("Diante de um número, faça três perguntas: quem publica? Quando? "
      "É busca, prova ou pesquisa? Sem essas respostas, um número diz pouco.")
bh = 62 + len(wrap(bb, "serif", False, 21.5, CW - 44)) * 30.5 + 16
p.rect(bx, by3, CW, bh, fill="#f0eee5")
yy3 = by3 + 16
p.text(bx + 22, yy3 + 26, "LER OS NÚMEROS", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, bb, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P6 col3 ends", by3 + bh)

# ---- charts: o domingo 8 em minutos + dois domingos ----
gy = 1566
p.hline(MX, RIGHT, gy - 18, OLIVE, 2)
p.text(MX, gy + 10, "O DOMINGO 8 EM NÚMEROS　11月8日の数字 (horários oficiais do Inep)", 26, "sans", True, OLIVE)
bw_ = 2 * CW + GUT
# left box: o relógio do domingo (minutos)
bx1 = MX
p.rect(bx1, gy + 28, bw_, 322, fill=BOX)
p.text(bx1 + 22, gy + 68, "O RELÓGIO DO DOMINGO　do meio-dia às 19h", 21, "sans", True, INK)
relog = [("portões abertos", 60), ("espera", 30), ("prova", 330)]
yy = gy + 100
for lab, v in relog:
    p.text(bx1 + 22, yy + 24, lab, 20, "serif", True, INK)
    labw = text_w(lab, "serif", True, 20)
    p.rect(bx1 + 40 + labw, yy + 6, v * 1.5, 22, fill=OLIVE)
    p.text(bx1 + 58 + labw + v * 1.5, yy + 24, f"{v} min", 20.5, "serif", False, INK)
    yy += 44
p.para(bx1 + 22, gy + 248, "Minutos do domingo 8: 60 + 30 + 330 = 420 minutos do meio-dia às 19h.", 19.5, "serif", False, INK, bw_ - 44, 1.4)
p.para(bx1 + 22, gy + 322 - 34, "Fonte: horários oficiais do Inep para o dia 8.", 17.5, "sans", False, GREY, bw_ - 44, 1.3)
# right box: dois domingos
bx2 = COLX[2]
p.rect(bx2, gy + 28, bw_, 322, fill=BOX)
p.text(bx2 + 22, gy + 68, "DOIS DOMINGOS　uma prova", 21, "sans", True, INK)
doms = [
    "Dia 8 — redação, Linguagens, Humanas.",
    "Dia 8 — 13h30 às 19h, cinco horas e meia.",
    "Dia 15 — Natureza e Matemática (prévia).",
    "Dia 15 — a cobertura sai na próxima edição.",
]
yy = gy + 100
for t in doms:
    p.text(bx2 + 22, yy + 24, t, 20, "serif", False, INK)
    yy += 40
p.para(bx2 + 22, gy + 322 - 34, "Fonte: Inep — as provas são nos dias 8 e 15.", 17.5, "sans", False, GREY, bw_ - 44, 1.3)

# ---- P6 exercises ----
ey = 1930
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EXERCÍCIOS　6ページの練習問題", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答えは8ページ　レベル混在の出題です。番号で答えを探してください", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A　LER OS GRÁFICOS", 25)
e.bridge("上の2つの図を見て、正しい答えを選んでください。")
e.ex("B2", "選択問題", "B", "門の開放は60分",
     "No relógio do domingo, os portões ficam abertos... A. 30 minutos · B. 60 minutos · C. 330 minutos", size=17, gap=0)
e.ex("B2", "選択問題", "A", "閉門から試験開始まで30分待つ",
     "A espera entre o fechamento e a prova é de... A. 30 minutos · B. 60 minutos · C. 330 minutos", size=17, gap=0)
e.ex("B2", "選択問題", "B", "試験は330分",
     "A prova dura... A. 60 minutos · B. 330 minutos · C. 420 minutos", size=17, gap=0)
e.ex("B2", "選択問題", "B", "60 + 30 + 330 = 420",
     "60 + 30 + 330 = ... A. 390 · B. 420 · C. 360", size=17, gap=0)
e.ex("B2", "選択問題", "C", "正午から19時 = 7時間",
     "Do meio-dia às 19h são... A. 5h30 · B. 6h · C. 7h", size=17, gap=0)
e.ex("B2", "選択問題", "A", "図の数字はInepの公式時間",
     "Os números do gráfico são... A. horários oficiais do Inep · B. uma pesquisa eleitoral · C. buscas no Google", size=17, gap=0)
e.head("B　COMPREENSÃO", 25)
e.ex("B2", "選択問題", "B", "Enemは8日と15日の2つの日曜日",
     "O Enem tem... A. um só domingo · B. dois domingos: 8 e 15 · C. três domingos", size=17, gap=0)
e.ex("B2", "選択問題", "B", "初日は小論文・言語・人文科学",
     "No dia 8, a prova tem... A. Natureza e Matemática · B. redação, Linguagens e Humanas · C. só redação", size=17, gap=0)
e.ex("B2", "選択問題", "B", "13時以降の到着は入場不可",
     "Quem chega depois das 13h... A. entra atrasado · B. não entra · C. faz a prova no dia 15", size=17, gap=0)
e.ex("B2", "選択問題", "B", "確認カードに試験会場が載っている",
     "O Cartão de Confirmação mostra... A. a nota · B. o local da prova · C. o gabarito", size=17, gap=0)
e.head("C　OS TEMPOS DO TEXTO", 25)
e.bridge("文の意味に合わせて、正しい動詞の形を補ってください。")
e.ex("B2", "文の完成", "começará", "未来形：começará",
     "No domingo, ___ (começar) a prova às 13h30.", instr="空所補充", size=17, gap=0)
e.ex("B2", "文の完成", "chegar", "quem + 接続法未来形：chegar",
     "Quem ___ (chegar) depois das 13h não entra.", instr="空所補充", size=17, gap=0)
e.ex("B2", "文の完成", "fecham", "現在形：fecham",
     "Os portões ___ (fechar) às 13h.", instr="空所補充", size=17, gap=0)
e.ex("B2", "文の完成", "pede", "現在形：pede",
     "O Inep ___ (pedir) que cada um confira o local.", instr="空所補充", size=17, gap=0)
e.head("D　AS PALAVRAS DA PROVA", 25)
e.bridge("枠内の語で空所を補ってください：portões · segunda chamada · local · conferir")
e.ex("B2", "文の完成", "portões", "portões = 門",
     "Os ___ abrem às 12h.", instr="空所補充", size=17, gap=0)
e.ex("B2", "文の完成", "segunda chamada", "segunda chamada = 追試、2回目の入場",
     "Não há ___ no Enem.", instr="空所補充", size=17, gap=0)
e.ex("B2", "文の完成", "local", "local = 場所",
     "Confira o ___ da sua prova.", instr="空所補充", size=17, gap=0)
e.ex("B2", "文の完成", "Confira", "命令形：confira",
     "___ o cartão antes do domingo.", instr="空所補充", size=17, gap=0)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-aprofundamento.svg")
print("P6 saved, exercises so far:", len(REG))
