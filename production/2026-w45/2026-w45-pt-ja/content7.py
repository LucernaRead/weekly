# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LÍNGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LÍNGUA　ことば", "A Lucerna", "ことばに注目　Três níveis, três ferramentas　3つのレベル、3つの道具")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　PERGUNTAS E O PRESENTE", 24)
a.para("Para perguntar o essencial da semana: «Que horas começa a prova?» — que horas + verbo no presente. E, para lugares, «Onde fica o meu local?» — onde fica.", 21.5)
a.para("E conferir é especial na primeira pessoa: eu confiro, você confere, ele confere. Nós conferimos, eles conferem.", 21.5)
a.bridge("疑問文：que horas（何時）+ 動詞；onde fica は場所を尋ねる；conferir の eu の形は不規則：confiro")
a.ex("A2", "文の完成", "confiro", "conferir：eu → confiro（不規則）",
     "Eu ___ (conferir) o cartão.", instr="空所補充", size=20.5, gap=10)
a.ex("A2", "文の完成", "confere", "conferir：você → confere",
     "Você ___ (conferir) o local antes de sair.", instr="空所補充", size=20.5, gap=10)
a.ex("A2", "文の完成", "começa", "começar：ela → começa",
     "Que horas ___ (começar) a prova?", instr="空所補充", size=20.5, gap=10)
a.ex("A2", "選択問題", "B", "onde は場所を尋ねる",
     "«___ fica o meu local?» A. Que horas · B. Onde · C. Quando", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　O PRETÉRITO PERFEITO", 24)
b.para("Para contar a semana, usamos o pretérito perfeito: eu revisei, ele chegou, ele dormiu. Revisar é regular: eu revisei, ele revisou.", 21.5)
b.para("E o modelo é simples: chegar → chegou; dormir → dormiu; separar → separei. Atenção ao acento: saíram, caíram.", 21.5)
b.bridge("一週間のことを話すには過去形（pretérito perfeito）；revisar は規則変化（revisei）；chegar/dormir の過去形はアクセントに注意。")
b.ex("B1", "文の完成", "revisei", "revisar 過去形：revisei",
     "Eu ___ (revisar) um pouco por dia.", instr="空所補充", size=20.5, gap=10)
b.ex("B1", "文の完成", "chegou", "chegar 過去形：chegou",
     "O candidato ___ (chegar) cedo.", instr="空所補充", size=20.5, gap=10)
b.ex("B1", "文の完成", "dormiu", "dormir 過去形：dormiu",
     "Ele ___ (dormir) bem na véspera.", instr="空所補充", size=20.5, gap=10)
b.ex("B1", "選択問題", "B", "chegaram は chegar の過去形複数",
     "«Os times ___ à volta com tudo em aberto.» A. chega · B. chegaram · C. chegamos", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　O FUTURO DO SUBJUNTIVO", 24)
c.para("Depois de «quando», «se» e «quem», o futuro pede o subjuntivo: «Quando você chegar, apresente o documento.» «Quem tiver o cartão, confere o local.»", 21.5)
c.para("É o tempo da página 6: regras e condições. Ter → tiver; ser → for; chegar → chegar (regular). Não confunda com o presente: é a gramática das hipóteses sobre o domingo.", 21.5)
c.bridge("quando、se、quem の後ろは接続法未来形：tiver、for、chegar（日曜日の仮定）。")
c.ex("B2", "文の完成", "tiver", "quem + 接続法未来形：tiver",
     "Quem ___ (ter) o cartão confere o local antes do domingo.", instr="空所補充", size=20.5, gap=10)
c.ex("B2", "文の完成", "chegar", "quando + 接続法未来形：chegar",
     "Quando você ___ (chegar) ao local, apresente o documento.", instr="空所補充", size=20.5, gap=10)
c.ex("B2", "文の完成", "for", "se + ser の接続法未来形：for",
     "Se o seu local ___ (ser) novo, saia mais cedo de casa.", instr="空所補充", size=20.5, gap=10)
c.ex("B2", "選択問題", "B", "quando + 未来 → 接続法未来形 for",
     "«Quando ___ domingo, o país faz a prova.» A. é · B. for · C. seja", size=20.5, gap=10)
c.end_report()

# ---- col 3: erros comuns + a palavra + cartas ----
bx = COLX[3]
errs = [
    ("«Vou fazer o Enem de caneta azul.»", "→ «De caneta preta.» A caneta do Enem é preta.", "Enemは黒ペンで、青ペンはだめ。"),
    ("«Chego às 13h30, na hora da prova.»", "→ «Chego antes das 13h.» Os portões fecham às 13h.", "13時閉門、13:30に着いては遅い。"),
    ("«Vou revisar a noite inteira na véspera.»", "→ «Vou dormir bem na véspera.» Quem dorme lembra melhor.", "詰め込みより、よく眠る方が覚えられる。"),
    ("«O feriadão é de 2 a 5 de novembro.»", "→ «O feriadão é de 31 a 2.» Três dias: sábado, domingo e segunda.", "連休は10月31日〜11月2日の3日間。"),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 198
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ERROS COMUNS　よくある間違い", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 22
wt = "« feriadão »: sábado, domingo e segunda — três dias de descanso."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("feriadão = 連休、全部で3日間。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "A PALAVRA　今週の単語", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "feriadão = 連休、全部で3日間。", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 22
lt = "«Vou fazer o Enem no domingo 8. Já conferi o cartão. Boa prova!» — EXEMPLO DA REDAÇÃO"
# FIX1 (independent proof, Problem 1 — promise gap): on-page deferral disclosure.
# VOL.1 promised real letters + best P8 texts for VOL.2; none had arrived by press
# time, so the labeled editor's example stays and the promise carries to VOL.3.
# No letters/texts fabricated; existing labeling kept verbatim.
disc_pt = "Nota da redação: as cartas reais e os melhores textos prometidos no VOL.1 não chegaram até o fechamento — fica o exemplo, e a promessa passa para o VOL.3."
disc_cn = "編集部注：VOL.1で約束した実際の手紙と最優秀作文は締切までに届かず、本号は例文を掲載し、約束はVOL.3へ延期します。"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("編集部の作例です。あなたの手紙を送ってください。VOL.3に掲載します！", "sans", False, 20, CW - 44)) * 29 + 10 + len(wrap(disc_pt, "serif", False, 21.5, CW - 44)) * 30.5 + 10 + len(wrap(disc_cn, "sans", False, 19.5, CW - 44)) * 29 + 35
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "CARTAS DOS LEITORES", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 20, "編集部の作例です。あなたの手紙を送ってください。VOL.3に掲載します！", 20, "sans", False, GREY, CW - 44, 1.42)
yy3 = p.para(bx + 22, yy3 + 10, disc_pt, 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(bx + 22, yy3 + 10, disc_cn, 19.5, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frases da semana (verbatim from this issue) ----
fy = max(1712, ly + lh + 44)
p.hline(MX, RIGHT, fy - 2, OLIVE, 2)  # rule below the CARTAS box (fy-14 cut the last line)
p.text(MX, fy + 24, "FRASES DA SEMANA　今週のフレーズ（今号の記事から逐語引用）", 27, "sans", True, OLIVE)
quotes = [
    ("«Do feriadão à prova: a semana do Enem»", "連休から試験へ：Enemの週。", "Página 1"),
    ("«Muita gente viaja, visita a família e vai ao cemitério levar flores»", "多くの人が旅行し、家族を訪ね、墓地に花を供える。", "Página 1"),
    ("«Finados é o dia da memória»", "死者の日は偲ぶ日。", "Página 2"),
    ("«lembrar é um jeito de continuar perto»", "偲ぶことは近くにい続ける方法。", "Página 3"),
    ("«cada ponto vale uma posição, cada gol vale uma história»", "1点が順位に値し、1ゴールが物語に値する。", "Página 4"),
    ("«quem dorme bem lembra melhor»", "よく眠ると、よく覚えていられる。", "Página 5"),
    ("«primeiro as fáceis, depois as difíceis»", "まず易しいものから、次に難しいものへ。", "Página 6"),
    ("«Confira o cartão, durma bem, chegue cedo»", "確認カードを確かめ、よく眠り、早く着く。", "Página 2"),
]
colw = (RIGHT - MX - GUT) // 2
fr_end = 0  # lowest Frases translation end (adaptive band)
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 128  # FIX1: tightened from 158 so the taller letters box leaves the preview box clear
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    fr_end = max(fr_end, p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35))

# ---- próxima semana ----
py = max(2404, fr_end - 12)  # adaptive: keep the band clear of the Frases translations
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "A PRÓXIMA SEMANA　次号予告 (VOL.3)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "Domingo 15 de novembro: o segundo dia do Enem — Natureza e Matemática. E o feriado da Proclamação da República. Mais: as suas cartas e os melhores textos da página 8. Até segunda!", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lingua.svg")
print("P7 saved, exercises so far:", len(REG))
