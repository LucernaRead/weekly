# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · CAPA (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 2　SEGUNDA EDIÇÃO", 17, "sans", True, OLIVE, spacing=1.7)
p.text(975, 92, "TODA SEMANA EM PORTUGUÊS　毎週一号　ブラジル人が読んでいるポルトガル語を読む", 17, "sans", False, GREY, anchor="middle", spacing=1.7)
p.text(RIGHT, 92, "SEMANA DE 2 A 8 DE NOVEMBRO DE 2026", 17, "sans", False, GREY, anchor="end", spacing=1.7)
p.text(975, 262, "A Lucerna", 196, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "ポルトガル語週刊　VOL.2　A SEMANA DO ENEM　FINADOS　O FUTEBOL DECIDE", 36, "serif", True, OLIVE, anchor="middle", spacing=4)
p.text(975, 372, "ポルトガル語テキスト　日本語の解説 — 日本語読者のための版", 16, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)

# band
p.rect(MX, 470, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 30, 524, "A SEMANA DO ENEM!", 46, "sans", True, ONCLOTH)
p.text(MX + 30, 568, "De segunda a domingo, o Brasil revisa, descansa e faz a prova.", 25, "serif", False, "#cac8ba")
p.text(RIGHT - 30, 524, "Enemの週", 27, "sans", True, GOOSE, anchor="end")
p.text(RIGHT - 30, 568, "11月2日死者の日の連休　11月8日Enem初日", 18, "sans", False, GOOSE, anchor="end")

# ---- headline (span cols 0-2) ----
hy = 590
p.text(MX, hy + 26, "A NOTÍCIA　トップ記事", 17, "sans", True, OLIVE)
hy = p.para(MX, hy + 92, "Do feriadão à prova: a semana do Enem", 53, "serif", True, INK, 1323, 1.06)
p.text(MX, hy + 28, "Da redação da A Lucerna　Nível de leitura: A2", 17, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Começa na segunda-feira, 2 de novembro, feriado de Finados, e termina no domingo, 8 de novembro, com o primeiro dia do Enem. Entre um dia e outro, o país inteiro vive a mesma semana: descansar, revisar e fazer a prova.", size=24)
f.para("O feriadão abre a semana: sábado, 31 de outubro, domingo, 1º de novembro, e segunda-feira, 2, feriado nacional. Muita gente viaja, visita a família e vai ao cemitério levar flores. Para quem faz o Enem, o feriadão é também um fim de semana de revisão: um pouco por dia, sem maratona.", size=24)
f.para("No domingo, 8 de novembro, é o primeiro dia do Enem 2026. Os portões abrem às 12h e fecham às 13h, no horário de Brasília. A prova começa às 13h30 e vai até as 19h: são cinco horas e meia de redação, Linguagens e Ciências Humanas. Mais de 5 milhões de estudantes estão inscritos.", size=24)
f.para("E o futebol não para: a rodada 34 do Brasileirão tem jogo de segunda a sexta, e as semifinais da Copa do Brasil se decidem no fim de semana — sábado, Atlético-MG × Grêmio, e domingo, Vasco × Palmeiras (página 4). O sábado, 31, foi de Halloween, e o domingo, 1º, teve os jogos de ida da Copa do Brasil.", size=24)
f.para("Esta é a segunda edição da A Lucerna em português: toda semana, o Brasil de verdade, com clareza e honestidade. Boa prova — e boa leitura!", size=24)
f.bridge("解説 — feriadão 連休 · o portão 門 · a redação 小論文 · revisar 復習する。")
f.box("A SEMANA EM NÚMEROS　今週の数字", [
    ("12h — os portões abrem no domingo 8（日曜日12時開門）", "serif", False, INK, 20, 1.35),
    ("13h — os portões fecham（13時閉門、遅刻は入場不可）", "serif", False, INK, 20, 1.35),
    ("13h30–19h — a prova do dia 8（試験13:30から19:00まで）", "serif", False, INK, 20, 1.35),
    ("5h30 — a duração da prova do dia 8（試験時間5時間半）", "serif", False, INK, 20, 1.35),
])
f.head("AGORA VOCÊ　すぐ練習", 25)
f.ex("A2", "文の完成", "feriadão", "feriadão = 連休",
     "A semana começa com o ___ de Finados.", size=19.5, gap=6)
f.ex("A2", "文の完成", "portões", "portões = 門（試験会場の門）",
     "No domingo 8, os ___ abrem às 12h.", size=19.5, gap=6)
f.ex("A2", "文の完成", "redação", "redação = 小論文",
     "A prova do dia 8 tem ___, Linguagens e Ciências Humanas.", size=19.5, gap=6)
f.ex("A2", "文の完成", "13h30", "13h30 試験開始（ブラジリア時間）",
     "A prova começa às ___.", size=19.5, gap=6)
f.ex("A2", "文の完成", "19h", "19h 終了",
     "A prova vai até as ___.", size=19.5, gap=6)
f.ex("B1", "文の完成", "revisam", "revisar 現在形 eles の形：revisam",
     "Os estudantes ___ (revisar) um pouco por dia.", size=19.5, gap=6)
f.end_report()

# ---- os horários do domingo 8 (col 3) ----
gx, gw = COLX[3], CW
gy = 588
p.rect(gx, gy, gw, 700, fill=BOX)
p.text(gx + 22, gy + 40, "OS HORÁRIOS", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "DO DOMINGO 8", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Enem, dia 8　horário de Brasília", 19, "sans", False, GREY)
hor = [
    ("12h", "os portões abrem"),
    ("13h", "os portões fecham"),
    ("13h30", "a prova começa"),
    ("19h", "a prova termina"),
]
byy = gy + 150
for t, lab in hor:
    p.text(gx + 22, byy + 28, t, 30, "serif", True, OLIVE)
    p.text(gx + 150, byy + 28, lab, 21.5, "serif", False, INK)
    byy += 92
p.text(gx + 22, byy + 16, "Chegue cedo: depois das 13h,", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "ninguém mais entra.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 76, "遅刻は入場不可：13時以降は閉門", 19, "sans", False, GREY)

# ---- conteúdo (col 3) ----
sy = 1312
p.rect(gx, sy, gw, 340, fill="#f0eee5")
p.text(gx + 22, sy + 40, "NESTA EDIÇÃO　今号の目次", 24, "sans", True, OLIVE)
som = [
    ("Pág. 2", "O feriadão e a revisão", "A2"),
    ("Pág. 3", "Finados, o dia da memória", "A2→B1"),
    ("Pág. 4", "O futebol decide", "B1"),
    ("Pág. 5", "A reta final dos jovens", "B1"),
    ("Pág. 6", "O Enem explicado", "B2"),
    ("Pág. 7", "Frases da semana", "A2→B2"),
    ("Pág. 8", "Exercícios e respostas", "todos"),
]
yy = sy + 84
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, OLIVE)
    p.text(gx + 88, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 40

# ---- palavra da semana (col 3) ----
my = 1652
p.text(gx, my + 24, "A PALAVRA DA SEMANA", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, OLIVE, 2)
p.text(gx, my + 76, "« feriadão »", 21.5, "serif", False, INK, italic=True)
wy = p.para(gx, my + 108, "um feriado grudado no fim de semana — três dias.", 21.5, "serif", False, INK, gw, 1.4)
wy2 = p.para(gx, wy + 10, "「連休」：休みが週末につながり、全部で3日間。", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, max(1844, wy2 - 16), LINE, 1.2)  # adaptive: keep the rule clear of a 2-line weekly-word gloss
iy = 1874
ix, iw = span_x(0, 2)
image(p, "estudo.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "Estudantes em uma biblioteca: para os mais de 5 milhões de inscritos no Enem, o feriadão é um fim de semana de revisão — um pouco por dia, sem maratona. (Página 5)",
        "Foto: Gary Todd / Wikimedia Commons — CC0")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2300, tag="P1-tv")
f2.head("A SEMANA EM DOIS DOMINGOS", 25)
f2.para("Domingo 1º: os jogos de ida da Copa do Brasil. Domingo 8: o primeiro dia do Enem. Entre um domingo e outro, o Brasil revisa, descansa e joga.", 22.5)
f2.para("No sábado, 31 de outubro, foi Halloween: festas à fantasia em todo o país — e, para os candidatos, a última festa antes da prova.", 22.5)
f2.end_report()
# col 3 EM POUCAS PALAVRAS
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX)
p.text(bx + 22, 1914, "EM POUCAS PALAVRAS　短報", 24, "sans", True, OLIVE)
brefs = [
    ("O FERIADÃO", "Segunda, 2: Finados, feriado nacional — feriadão de 31 a 2. (Página 2)"),
    ("O ENEM", "Domingo, 8: primeiro dia — redação, Linguagens e Humanas. (Página 6)"),
    ("O FUTEBOL", "Sábado e domingo: os jogos de volta da Copa do Brasil decidem os finalistas. (Página 4)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, OLIVE)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- quiz relâmpago ----
qy = 2312
p.hline(MX, RIGHT, qy, OLIVE, 2)
p.text(MX, qy + 36, "QUIZ RELÂMPAGO　クイズ", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "トップ記事を読んで、正しい答えを選ぼう　答えは8ページ", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2560, tag="P1-quiz")
qf.ex("A2", "選択問題", "B", "連休は10月31日から11月2日まで",
      "O feriadão vai... A. de 2 a 4 de novembro · B. de 31 de outubro a 2 de novembro · C. de 8 a 15 de novembro", size=21)
qf.ex("A2", "選択問題", "B", "13時閉門",
      "Os portões do Enem fecham às... A. 12h · B. 13h · C. 13h30", size=21)
qf.ex("A2", "選択問題", "C", "初日は小論文・言語・人文科学",
      "No dia 8, a prova tem... A. só Matemática · B. só redação · C. redação, Linguagens e Ciências Humanas", size=21)
qf.ex("A2", "選択問題", "B", "第2戦は7日と8日",
      "Os jogos de volta da Copa do Brasil são... A. no dia 1º · B. nos dias 7 e 8 · C. no dia 15", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-capa.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · VIDA (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("VIDA　暮らし", "A Lucerna", "NÍVEL A2　Finados e revisão: o feriadão do Brasil")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("Finados e revisão: o feriadão do Brasil", 32)
f.byline("Da redação da A Lucerna　Nível de leitura: A2")
f.para("Segunda-feira, 2 de novembro, é Finados, feriado nacional. Com o sábado, 31, e o domingo, 1º, o país ganha um feriadão de três dias: muita gente viaja para ver a família, e muita gente fica em casa para descansar.")
f.para("Finados é o dia da memória: famílias visitam os cemitérios, levam flores — sobretudo crisântemos —, acendem velas e participam de missas. É um dia calmo, de lembrança e de encontro: os vivos cuidam do lugar dos mortos, e as histórias voltam à mesa.")
f.para("Para os candidatos do Enem, o feriadão tem outro nome: revisão. O plano da semana é simples — revisar um pouco por dia, dormir bem e conferir o Cartão de Confirmação, o documento que mostra o local da prova. Quem confere antes não se perde no dia.")
f.para("E atenção ao relógio do domingo 8: os portões abrem às 12h e fecham às 13h. Chegue cedo, leve documento com foto e caneta preta, e desligue o celular. A prova é longa — cinco horas e meia — e começa às 13h30.")
f.para("No Brasil, não há horário de verão desde 2019: ninguém muda o relógio nesta semana. O horário do Enem é o de Brasília — confira o fuso da sua cidade.")
f.head("E SE EU CHEGAR TARDE?", 25)
f.para("Se você chegar depois das 13h, os portões já fecharam — e não há segunda chamada. Por isso o plano é sair cedo: o domingo 8 não aceita atraso. Melhor chegar cedo e esperar do que correr no último minuto.", 23.5)
f.box("PARA NÃO ERRAR　覚え方", [
    ("«Confira o cartão, durma bem, chegue cedo.» Três passos e o domingo fica tranquilo: o resto é com a prova.", "serif", False, INK, 21.5, 1.4),
])
f.gloss("o feriadão 連休 · o cemitério 墓地 · a vela ろうそく · o crisântemo 菊 · a missa ミサ · conferir 確かめる。")
f.end_report()

# col 3: facts + e você? (sequential, measured)
ix = COLX[3]
facts = ["O feriadão vai de sábado, 31 de outubro, a segunda, 2 de novembro.",
         "Finados: visitas aos cemitérios, flores, velas e missas.",
         "Domingo 8: portões 12h–13h, prova 13h30–19h, horário de Brasília."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "VOCÊ SABIA?", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E você? No seu país, há um dia de lembrar os mortos? O que as famílias fazem nesse dia? Escreva duas frases em português e mande para a redação: as melhores saem na página 7, «Cartas dos leitores»."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("あなたの国では、死者を偲ぶ日がありますか。その日、家族は何をしますか。2文を書いて送ってください。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E VOCÊ?　あなたは？", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "あなたの国では、死者を偲ぶ日がありますか。その日、家族は何をしますか。2文を書いて送ってください。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- Os horários do domingo 8: 4 time boxes ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, OLIVE, 2)
p.text(MX, dy + 28, "OS HORÁRIOS DO DOMINGO 8　日曜日の時間表", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "Um país, vários relógios　一つの国、いくつもの時差", 20, "sans", False, GREY, anchor="end")
times = [
    ("12h", "os portões abrem", "日曜日12時開門"),
    ("13h", "os portões fecham", "13時閉門"),
    ("13h30", "a prova começa", "13:30 試験開始"),
    ("19h", "a prova termina", "19:00 終了"),
]
for i, (t, lab, cn) in enumerate(times):
    bx = COLX[i]
    p.rect(bx, dy + 52, CW, 150, fill=BOX)
    p.text(bx + 22, dy + 116, t, 40, "serif", True, OLIVE)
    yy = p.para(bx + 152, dy + 92, lab, 21.5, "serif", False, INK, CW - 174, 1.36)
    p.para(bx + 152, yy + 20, cn, 19, "sans", False, GREY, CW - 174, 1.3)
p.para(MX, dy + 234, "Atenção: o horário é o de Brasília. Quem faz a prova em outro fuso deve conferir a hora local: o portão fecha às 13h de Brasília, e não há atraso.", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P2 exercises ----
ey = dy + 282
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EXERCÍCIOS　2ページの練習問題", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答えは8ページ　レベル混在の出題です。番号で答えを探してください", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A　COMPREENSÃO", 25)
e.bridge("2ページの記事を読んで、正しい答えを選んでください。")
e.ex("A2", "選択問題", "B", "連休は10月31日から11月2日まで",
     "O feriadão vai... A. de 2 a 5 de novembro · B. de 31 de outubro a 2 de novembro · C. de 8 a 15 de novembro", size=20, gap=8)
e.ex("A2", "選択問題", "B", "死者の日、家族は墓地に花を供える",
     "Em Finados, as famílias... A. compram presentes de Natal · B. visitam os cemitérios e levam flores · C. votam para presidente", size=20, gap=8)
e.ex("A2", "選択問題", "B", "確認カードに試験会場が載っている",
     "O Cartão de Confirmação mostra... A. a nota do aluno · B. o local da prova · C. o resultado final", size=20, gap=8)
e.ex("A2", "選択問題", "B", "13時閉門",
     "Os portões fecham às... A. 12h · B. 13h · C. 19h", size=20, gap=8)
e.ex("A2", "選択問題", "A", "ブラジルに夏時間はなく、時計は動かない",
     "Nesta semana, o relógio no Brasil... A. não muda · B. volta uma hora · C. avança uma hora", size=20, gap=8)
e.head("B　O PRESENTE", 25)
e.bridge("動詞の現在形を補ってください。")
e.ex("A2", "文の完成", "confere", "conferir：ele → confere",
     "O candidato ___ (conferir) o cartão.", instr="空所補充", size=20, gap=8)
e.ex("A2", "文の完成", "abre", "abrir：ele → abre",
     "O portão ___ (abrir) às 12h.", instr="空所補充", size=20, gap=8)
e.ex("A2", "文の完成", "levamos", "levar：nós → levamos",
     "Nós ___ (levar) documento com foto.", instr="空所補充", size=20, gap=8)
e.ex("A2", "文の完成", "começa", "começar：ela → começa",
     "A prova ___ (começar) às 13h30.", instr="空所補充", size=20, gap=8)
e.ex("A2", "文の完成", "é", "ser 現在形 ela の形：é",
     "A missa de Finados ___ (ser) um momento calmo.", instr="空所補充", size=20, gap=8)
e.head("C　COMPLETE COM OS NÚMEROS", 25)
e.bridge("1・2ページの数字で空所を補ってください。")
e.ex("A2", "文の完成", "1", "12時から13時 = 1時間",
     "Os portões ficam abertos ___ hora.", instr="空所補充", size=20, gap=8)
e.ex("A2", "文の完成", "5", "13:30から19:00 = 5時間半",
     "A prova dura ___ horas e meia.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "330", "5×60 + 30 = 330分",
     "De 13h30 a 19h são ___ minutos.", instr="空所補充", size=20, gap=8)
e.ex("A2", "文の完成", "3", "31日、1日、2日 = 3日間",
     "O feriadão tem ___ dias.", instr="空所補充", size=20, gap=8)
e.head("D　AS PALAVRAS", 25)
e.match_set("A2", "語と意味を結ぶ",
            ["o feriadão", "o cemitério", "a vela", "o crisântemo"],
            ["a flor que as famílias levam a Finados",
             "o lugar onde ficam os túmulos",
             "um feriado grudado no fim de semana",
             "o objeto que dá luz e se acende em memória"],
            ["c", "b", "d", "a"],
            ["feriadão=週末につながった休み c", "cemitério=墓石のある場所 b", "vela=偲んで灯すもの d", "crisântemo=死者の日に持っていく花 a"],
            instr="語と意味を結ぶ")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-vida.svg")
print("P2 saved, exercises so far:", len(REG))
