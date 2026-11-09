# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA　文化", "A Lucerna", "A2 → B1　Finados: o dia da memória　死者の日：偲ぶ日")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("Finados: o dia em que o Brasil lembra", 32)
f.byline("Da redação da A Lucerna　Nível de leitura: A2 → B1")
f.para("No dia 2 de novembro, o Brasil para para lembrar. Finados — o Dia dos Fiéis Defuntos — é o dia em que as famílias visitam os cemitérios do país inteiro, do pequeno cemitério do interior ao grande cemitério da capital.")
f.para("O ritual é simples e antigo: limpar o túmulo, levar flores — sobretudo crisântemos, a flor de Finados —, acender uma vela e rezar. Nas igrejas e nos cemitérios, há missas o dia inteiro. Não é festa: é um dia calmo, de silêncio, de encontro e de memória.")
f.para("Cada família tem o seu jeito: uns levam a flor preferida de quem partiu, outros levam a comida de que ele gostava, outros só ficam um pouco em silêncio. O que não muda é o centro do dia: lembrar é um jeito de continuar perto.")
f.para("E Finados tem um vizinho famoso: no sábado, 31 de outubro, foi Halloween, com fantasias e doces. Dois dias, dois jeitos de olhar para a morte: um de festa, outro de silêncio — e os dois cabem na mesma semana.")
f.gloss("o túmulo 墓石 · a flor 花 · acender 火をともす · rezar 祈る · o silêncio 静けさ · a lembrança 偲ぶこと。")
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
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("あなたの文化では、人々はどのように死者を偲びますか。2文を書いて送ってください。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E VOCÊ?　あなたは？", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "あなたの文化では、人々はどのように死者を偲びますか。2文を書いて送ってください。", 20, "sans", False, GREY, CW - 44, 1.42)
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
p.text(MX, ey + 28, "EXERCÍCIOS　3ページの練習問題", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答えは8ページ　レベル混在の出題です。番号で答えを探してください", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A　COMPREENSÃO", 25)
e.bridge("3ページの記事を読んで、正しい答えを選んでください。")
e.ex("A2", "選択問題", "B", "死者の日は偲びと静けさの日",
     "Finados é... A. um dia de festa e fantasia · B. o dia da memória e do silêncio · C. um dia de votação", size=20, gap=8)
e.ex("A2", "選択問題", "B", "家族は墓地に花を持っていく、主に菊",
     "As famílias levam aos cemitérios... A. presentes de Natal · B. flores, sobretudo crisântemos · C. fogos de artifício", size=20, gap=8)
e.ex("A2", "選択問題", "B", "教会と墓地では一日中ミサがある",
     "Nas igrejas e nos cemitérios, há... A. shows de rock · B. missas o dia inteiro · C. feiras de livros", size=20, gap=8)
e.ex("A2", "選択問題", "C", "ハロウィーンは10月31日土曜日",
     "Halloween foi... A. no domingo 8 · B. na segunda 2 · C. no sábado, 31 de outubro", size=20, gap=8)
e.ex("B1", "選択問題", "A", "偲ぶことは近くにい続ける方法",
     "O texto diz que lembrar é... A. um jeito de continuar perto · B. uma festa · C. uma votação", size=20, gap=8)
e.head("B　AS PALAVRAS DO TEXTO", 25)
e.bridge("枠内の語を使って空所を補ってください。")
e.para("túmulo · vela · crisântemo · missa · silêncio · lembrança", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "文の完成", "túmulo", "túmulo = 墓石",
     "As famílias limpam o ___.", instr="空所補充", size=20, gap=8)
e.ex("A2", "文の完成", "vela", "vela = ろうそく",
     "Acendem uma ___ em memória.", instr="空所補充", size=20, gap=8)
e.ex("A2", "文の完成", "crisântemo", "crisântemo = 菊",
     "O ___ é a flor de Finados.", instr="空所補充", size=20, gap=8)
e.ex("A2", "文の完成", "missa", "missa = ミサ",
     "Na igreja, há ___ o dia inteiro.", instr="空所補充", size=20, gap=8)
e.ex("A2", "文の完成", "silêncio", "silêncio = 静けさ",
     "Finados é um dia de ___.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "lembrança", "lembrança = 偲ぶこと",
     "A ___ volta à mesa.", instr="空所補充", size=20, gap=8)
e.head("C　O PRETÉRITO PERFEITO", 25)
e.bridge("過去形（pretérito perfeito）で補ってください。")
e.ex("B1", "文の完成", "visitaram", "visitar 過去形 elas の形：visitaram",
     "As famílias ___ (visitar) os cemitérios.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "levaram", "levar 過去形 elas の形：levaram",
     "Elas ___ (levar) flores.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "foi", "ser 過去形 ele の形：foi",
     "O sábado ___ (ser) de Halloween.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "viveu", "viver 過去形 ele の形：viveu",
     "O Brasil ___ (viver) dois dias diferentes.", instr="空所補充", size=20, gap=8)
e.head("D　CONSTRUA AS FRASES", 25)
e.bridge("語を並べて正しい文を作ってください。")
e.ex("B1", "文を作る", "Finados é um dia de silêncio.", "主語 + é + 補語",
     "finados / é / um dia de silêncio → ___", instr="文を作る", size=20, gap=8)
e.ex("A2", "文を作る", "As famílias levam flores ao cemitério.", "主語 + 動詞 + 目的語 + 場所",
     "as famílias / levam / flores / ao cemitério → ___", instr="文を作る", size=20, gap=8)
e.ex("B1", "文を作る", "O Brasil lembra os seus mortos.", "主語 + 動詞 + 目的語",
     "o Brasil / lembra / os seus mortos → ___", instr="文を作る", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · ESPORTE (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("ESPORTE　スポーツ", "A Lucerna", "NÍVEL B1　O futebol da semana　サッカーの週")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("Semana de decisão: quem vai à final da Copa do Brasil?", 32)
f.byline("Da redação da A Lucerna　Nível de leitura: B1")
f.para("A pergunta da semana é simples: quem vai à final da Copa do Brasil? Quatro times, dois jogos de volta, um fim de semana. No sábado, 7, às 18h, o Atlético-MG recebe o Grêmio na Arena MRV. No domingo, 8, às 17h, o Vasco recebe o Palmeiras em São Januário.")
f.para("Os jogos de ida foram no domingo, 1º de novembro: Palmeiras × Vasco, às 16h, e Grêmio × Atlético-MG, às 18h30. Os quatro times chegam à volta com tudo em aberto: quem vencer no total dos dois jogos vai à final.")
f.para("E o Brasileirão não para: a rodada 34 tem jogo de segunda a sexta, de 2 a 6 de novembro. É a reta final do campeonato: cada ponto vale uma posição, cada gol vale uma história. No fim de semana, o país para para a Copa — e volta para o Brasileirão na semana que vem.")
f.para("Ontem, domingo 1º, já foi de Copa: os jogos de ida abriram as semifinais. Nesta semana, a volta fecha a conta. Sábado e domingo, o Brasil tem dois horários marcados: 18h e 17h.")
f.gloss("a ida 第1戦 · a volta 第2戦 · o finalista 決勝進出チーム · a decisão 決戦 · a rodada 節。")
f.end_report()

# col 3: data box + e você (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 376, fill=BOX)
p.text(bx + 22, 240, "OS JOGOS DA SEMANA", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "Sáb 7, 18h — Atlético-MG × Grêmio, Arena MRV (volta). Dom 8, 17h — Vasco × Palmeiras, São Januário (volta). Ida, dom 1º — Palmeiras × Vasco, 16h; Grêmio × Atlético-MG, 18h30.", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 602
etvous = "E você? Para quem você torce na Copa do Brasil? Escreva duas frases em português e mande para a redação."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("ブラジルカップではどのチームを応援しますか。2文を書いて送ってください。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "E VOCÊ?　あなたは？", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "ブラジルカップではどのチームを応援しますか。2文を書いて送ってください。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "A SEMANA DO FUTEBOL　今週のサッカー日程", 26, "sans", True, OLIVE)
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
p.text(MX, ey + 28, "EXERCÍCIOS　4ページの練習問題", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答えは8ページ　レベル混在の出題です。番号で答えを探してください", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A　COMPREENSÃO", 25)
e.bridge("4ページの記事を読んで、正しい答えを選んでください。")
e.ex("B1", "選択問題", "A", "第2戦アトレチコMG × グレミオは土曜日7日18時",
     "A volta de Atlético-MG × Grêmio é... A. no sábado 7, às 18h · B. no domingo 8 · C. no dia 1º", size=20, gap=8)
e.ex("B1", "選択問題", "B", "ヴァスコ × パルメイラス第2戦は日曜日8日17時、サン・ジャヌアリオ",
     "Vasco × Palmeiras, a volta, é... A. no sábado, na Arena MRV · B. no domingo 8, às 17h, em São Januário · C. na segunda 2", size=20, gap=8)
e.ex("B1", "選択問題", "A", "第1戦は11月1日日曜日",
     "Os jogos de ida foram... A. no domingo 1º · B. no sábado 7 · C. no domingo 8", size=20, gap=8)
e.ex("B1", "選択問題", "B", "第34節は月曜日から金曜日まで毎日試合がある",
     "A rodada 34 do Brasileirão... A. é só no domingo · B. tem jogo de segunda a sexta · C. já terminou", size=20, gap=8)
e.ex("B1", "選択問題", "A", "2戦合計の勝者が決勝へ進む",
     "Quem vai à final? A. quem vencer no total dos dois jogos · B. quem vencer a ida · C. quem tiver mais torcida", size=20, gap=8)
e.head("B　AS PALAVRAS", 25)
e.match_set("B1", "語と意味を結ぶ",
            ["o finalista", "a ida", "a volta", "a rodada"],
            ["o segundo jogo de um confronto",
             "o time que chega à final",
             "o primeiro jogo de um confronto",
             "a jornada de jogos de um campeonato"],
            ["b", "c", "a", "d"],
            ["finalista=決勝へ進むチーム b", "ida=対戦の第1戦 c", "volta=対戦の第2戦 a", "rodada=1節の試合 d"],
            instr="語と意味を結ぶ")
e.head("C　COMPARATIVOS", 25)
e.bridge("かっこ内の正しい比較の形で空所を補ってください。")
e.ex("B1", "文の完成", "mais", "第2戦が決勝進出を決める：mais",
     "A volta é ___ decisiva do que a ida. (mais / menos)", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "mais", "18 > 16：mais",
     "18h é ___ tarde do que 16h. (mais / menos)", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "mais", "17 < 18：mais cedo",
     "17h é ___ cedo do que 18h. (mais / menos)", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "mais", "第34節は月曜日から金曜日まで試合がある：mais",
     "O Brasileirão tem ___ jogos na semana do que a Copa: a rodada vai de segunda a sexta. (mais / menos)", instr="空所補充", size=20, gap=8)
e.head("D　O PRETÉRITO PERFEITO", 25)
e.bridge("文を過去形（pretérito perfeito）で完成させてください。")
e.ex("B1", "文の完成", "foram", "ser 過去形複数：foram",
     "Os jogos de ida ___ (ser) no domingo 1º.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "recebeu", "receber 過去形 ele の形：recebeu",
     "O Palmeiras ___ (receber) o Vasco na ida.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "recebeu", "receber 過去形 ele の形：recebeu",
     "O Grêmio ___ (receber) o Atlético-MG na ida.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "começou", "começar 過去形 ela の形：começou",
     "A rodada 34 ___ (começar) na segunda.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "chegaram", "chegar 過去形 eles の形：chegaram",
     "Os times ___ (chegar) à volta com tudo em aberto.", instr="空所補充", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-esporte.svg")
print("P4 saved, exercises so far:", len(REG))
