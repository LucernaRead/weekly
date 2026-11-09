# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LÍNGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LÍNGUA　语言", "A Lucerna", "聚焦语言　Três níveis, três ferramentas　三个级别，三件工具")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　PERGUNTAS E O PRESENTE", 24)
a.para("Para perguntar o essencial da semana: «Que horas começa a votação?» — que horas + verbo no presente. E, para lugares, «Onde fica a minha seção?» — onde fica.", 21.5)
a.para("E conferir é especial na primeira pessoa: eu confiro, você confere, ele confere. Nós conferimos, eles conferem.", 21.5)
a.bridge("提问句：que horas（几点）+ 动词；onde fica 问地点；conferir 的 eu 形式不规则：confiro")
a.ex("A2", "完成句子", "confiro", "conferir：eu → confiro（不规则）",
     "Eu ___ (conferir) a minha seção no aplicativo.", instr="填空", size=20.5, gap=10)
a.ex("A2", "完成句子", "confere", "conferir：você → confere",
     "Você ___ (conferir) o local antes de sair.", instr="填空", size=20.5, gap=10)
a.ex("A2", "完成句子", "começa", "começar：ela → começa",
     "Que horas ___ (começar) a votação?", instr="填空", size=20.5, gap=10)
a.ex("A2", "单选", "B", "onde 问地点",
     "«___ fica a minha seção?» A. Que horas · B. Onde · C. Quando", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　O PRETÉRITO PERFEITO", 24)
b.para("Para contar a semana, usamos o pretérito perfeito: o Vasco venceu, o Boca fez, a CBF confirmou. Fazer é irregular: eu fiz, ele fez.", 21.5)
b.para("E os verbos em -ir têm o modelo de diminuir: ele diminuiu, eles diminuíram. Atenção ao acento: caíram, saíram.", 21.5)
b.bridge("讲一周的事用过去时（pretérito perfeito）；fazer 不规则（fez）；-ir 动词如 diminuiu，注意重音 caíram。")
b.ex("B1", "完成句子", "venceu", "vencer 过去时：venceu",
     "O Vasco ___ (vencer) o jogo de ida.", instr="填空", size=20.5, gap=10)
b.ex("B1", "完成句子", "fez", "fazer 过去时：fez",
     "O Boca ___ (fazer) três gols na volta.", instr="填空", size=20.5, gap=10)
b.ex("B1", "完成句子", "confirmou", "confirmar 过去时：confirmou",
     "A CBF ___ (confirmar) a arbitragem na terça.", instr="填空", size=20.5, gap=10)
b.ex("B1", "单选", "B", "caíram 是 cair 的过去时复数",
     "As buscas por guitarra ___ entre 2004 e 2021. A. cai · B. caíram · C. caímos", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　O FUTURO DO SUBJUNTIVO", 24)
c.para("Depois de «quando», «se» e «quem», o futuro pede o subjuntivo: «Quando você chegar, confira a seção.» «Quem tiver mais votos, vence.»", 21.5)
c.para("É o tempo da página 6: regras e condições. Ter → tiver; ser → for; chegar → chegar (regular). Não confunda com o presente: é a gramática das hipóteses sobre o domingo.", 21.5)
c.bridge("quando、se、quem 后用虚拟式将来：tiver、for、chegar（周日假设）。")
c.ex("B2", "完成句子", "tiver", "quem + 虚拟式将来：tiver",
     "Vence quem ___ (ter) mais votos válidos.", instr="填空", size=20.5, gap=10)
c.ex("B2", "完成句子", "chegar", "quando + 虚拟式将来：chegar",
     "Quando você ___ (chegar) à seção, apresente o documento.", instr="填空", size=20.5, gap=10)
c.ex("B2", "完成句子", "for", "se + ser 的虚拟式将来：for",
     "Se o seu local ___ (ser) novo, saia mais cedo de casa.", instr="填空", size=20.5, gap=10)
c.ex("B2", "单选", "B", "quando + 未来 → 虚拟式将来 for",
     "«Quando ___ domingo, o país vota.» A. é · B. for · C. seja", size=20.5, gap=10)
c.end_report()

# ---- col 3: erros comuns + a palavra + cartas ----
bx = COLX[3]
errs = [
    ("«Vou assistir o debate.»", "→ «Vou assistir ao debate.» Assistir (ver) pede a: ao jogo, ao debate.", "assistir（观看）要加介词 a：assistir ao debate。"),
    ("«Vou votar en la urna.»", "→ «Vou votar na urna.» En e la são espanhol; em português, em + a = na.", "en/la 是西班牙语；葡语 em+a 缩合为 na。"),
    ("«O debate foi esquisito!»", "→ Cuidado: esquisito é estranho, raro — não é «delicioso» como em espanhol.", "esquisito 在葡语里是“奇怪”，不是西语里的“美味”。"),
    ("«Eu voto, mais meu irmão não.»", "→ «Eu voto, mas meu irmão não.» Mas = porém; mais = quantidade.", "mas 是“但是”；mais 是“更多”。"),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 178
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ERROS COMUNS　常见错误", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 22
wt = "« urna » é a máquina onde o eleitor digita o número e confirma o voto — e todo o processo de votar: «voltar às urnas», «as urnas abrem às 8h»."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("urna = 电子投票箱；也引申为整个投票：voltar às urnas（再次去投票）、as urnas abrem（投票站开放）。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "A PALAVRA　本周生词", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "urna = 电子投票箱；也引申为整个投票：voltar às urnas（再次去投票）、as urnas abrem（投票站开放）。", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 22
lt = "«Olá! Sou Mei e estudo português em Xangai. Domingo acordo cedo para ver o resultado. Obrigado pelo jornal!» — Mei (carta de exemplo, escrita pela redação)"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("编辑部示例信，非真实来信。VOL.2 将刊登真实来信和第 8 版最佳作文！", "sans", False, 20, CW - 44)) * 29 + 34
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "CARTAS DOS LEITORES", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "编辑部示例信，非真实来信。VOL.2 将刊登真实来信和第 8 版最佳作文！", 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frases da semana (verbatim from this issue) ----
fy = max(1712, ly + lh + 44)
p.hline(MX, RIGHT, fy - 2, OLIVE, 2)  # rule below the CARTAS box (fy-14 cut the last line)
p.text(MX, fy + 24, "FRASES DA SEMANA　本周金句（逐字摘自本期文章）", 27, "sans", True, OLIVE)
quotes = [
    ("«Domingo é dia de decisão: o Brasil volta às urnas»", "周日是决定之日：巴西重返投票站。", "Página 1"),
    ("«confira o seu local no aplicativo e-Título antes de sair de casa»", "出门前，在 e-Título 里核对你的投票地点。", "Página 1"),
    ("«o Brasil não tem horário de verão»", "巴西没有夏令时。", "Página 2"),
    ("«a guitarra chegou a 75% do volume de buscas do violão»", "吉他的搜索量达到了 violão 的 75%。", "Página 3"),
    ("«No total dos dois jogos: 3 a 2 para o Boca»", "两回合总比分：3 比 2，博卡胜。", "Página 4"),
    ("«quem confere antes não se perde no dia»", "提前核对的人，当天不会迷路。", "Página 5"),
    ("«Interesse de busca não é intenção de voto»", "搜索热度不是投票意向。", "Página 6"),
    ("«Confira a seção, leve o documento, chegue no horário.»", "核对投票站、带好证件、准时到达。", "Página 2"),
]
colw = (RIGHT - MX - GUT) // 2
fr_end = 0  # lowest Frases translation end (adaptive band)
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 158
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    fr_end = max(fr_end, p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35))

# ---- próxima semana ----
py = max(2404, fr_end - 12)  # adaptive: keep the band clear of the Frases translations
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "A PRÓXIMA SEMANA　下期预告 (VOL.2)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "Sábado 31 de outubro: Halloween. Domingo 1º de novembro: as semifinais da Copa do Brasil. Segunda-feira, 2 de novembro: Finados, feriado nacional — um feriadão de três dias. E nos domingos 8 e 15: o Enem. Mais: as suas cartas e os melhores textos da página 8. Até segunda!", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lingua.svg")
print("P7 saved, exercises so far:", len(REG))
