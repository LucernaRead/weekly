# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LÍNGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LÍNGUA　ЯЗЫК", "A Lucerna", "Três níveis, três ferramentas　Три уровня, три инструмента")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　PERGUNTAS E O PRESENTE", 24)
a.para("Para perguntar o essencial da semana: «Que horas começa a prova?» — que horas + verbo no presente. E, para lugares, «Onde fica o meu local?» — onde fica.", 21.5)
a.para("E conferir é especial na primeira pessoa: eu confiro, você confere, ele confere. Nós conferimos, eles conferem.", 21.5)
a.bridge("Вопросы: que horas (во сколько) + глагол; onde fica спрашивает, где место; conferir неправилен в форме eu: confiro.")
a.ex("A2", "Дополните предложение", "confiro", "conferir: eu → confiro (неправильный)",
     "Eu ___ (conferir) o cartão.", instr="Заполните", size=20.5, gap=10)
a.ex("A2", "Дополните предложение", "confere", "conferir: você → confere",
     "Você ___ (conferir) o local antes de sair.", instr="Заполните", size=20.5, gap=10)
a.ex("A2", "Дополните предложение", "termina", "terminar: ela → termina",
     "Que horas ___ (terminar) a prova do dia 15?", instr="Заполните", size=20.5, gap=10)
a.ex("A2", "Выбор ответа", "B", "onde спрашивает о месте",
     "«___ fica o meu local?» A. Que horas · B. Onde · C. Quando", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　O PRETÉRITO PERFEITO", 24)
b.para("Para contar a semana, usamos o pretérito perfeito: o Grêmio venceu, Maurício marcou, o candidato chegou. Vencer é regular: eu venci, ele venceu.", 21.5)
b.para("E o modelo é simples: marcar → marcou; chegar → chegou; dormir → dormiu. Atenção ao acento: saíram, caíram.", 21.5)
b.bridge("Чтобы рассказать о неделе, используем прошедшее время (pretérito perfeito); vencer правильный (venceu); следи за ударением в прошедшем времени marcar, chegar и dormir.")
b.ex("B1", "Дополните предложение", "venceu", "vencer, прошедшее время: venceu",
     "O Grêmio ___ (vencer) por 2 a 0.", instr="Заполните", size=20.5, gap=10)
b.ex("B1", "Дополните предложение", "marcou", "marcar, прошедшее время: marcou",
     "Maurício ___ (marcar) o gol do Palmeiras.", instr="Заполните", size=20.5, gap=10)
b.ex("B1", "Дополните предложение", "chegou", "chegar, прошедшее время: chegou",
     "O candidato ___ (chegar) cedo.", instr="Заполните", size=20.5, gap=10)
b.ex("B1", "Выбор ответа", "B", "venceram — прошедшее время, множественное число, от vencer",
     "«Os times ___ a ida com vantagem.» A. vence · B. venceram · C. vencemos", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　O FUTURO DO SUBJUNTIVO", 24)
c.para("Depois de «quando», «se» e «quem», o futuro pede o subjuntivo: «Quando você chegar, apresente o documento.» «Quem tiver o cartão, confere o local.»", 21.5)
c.para("É o tempo da página 6: regras e condições. Ter → tiver; ser → for; chegar → chegar (regular). Não confunda com o presente: é a gramática das hipóteses sobre o domingo.", 21.5)
c.bridge("После quando, se и quem — будущее сослагательного наклонения: tiver, for, chegar — грамматика воскресных гипотез.")
c.ex("B2", "Дополните предложение", "tiver", "quem + будущее сослагательного наклонения: tiver",
     "Quem ___ (ter) o cartão confere o local antes do domingo.", instr="Заполните", size=20.5, gap=10)
c.ex("B2", "Дополните предложение", "chegar", "quando + будущее сослагательного наклонения: chegar",
     "Quando você ___ (chegar) ao local, apresente o documento.", instr="Заполните", size=20.5, gap=10)
c.ex("B2", "Дополните предложение", "for", "se + будущее сослагательного наклонения от ser: for",
     "Se o seu local ___ (ser) novo, saia mais cedo de casa.", instr="Заполните", size=20.5, gap=10)
c.ex("B2", "Выбор ответа", "B", "quando + будущее → будущее сослагательного наклонения for",
     "«Quando ___ domingo, o país faz a prova.» A. é · B. for · C. seja", size=20.5, gap=10)
c.end_report()

# ---- col 3: erros comuns + a palavra + cartas ----
bx = COLX[3]
errs = [
    ("«Vou fazer o Enem de caneta azul.»", "→ «De caneta preta.» A caneta do Enem é preta.", "Только чёрная ручка — синяя не подойдёт."),
    ("«Chego às 13h30, na hora da prova.»", "→ «Chego antes das 13h.» Os portões fecham às 13h.", "Закрытие в 13:00 — в 13:30 уже поздно."),
    ("«No dia 15, a prova termina às 19h.»", "→ «Termina às 18h30.» Às 19h, só no dia 8.", "15-го экзамен заканчивается в 18:30; 19:00 — это 8-е."),
    ("«O feriado dá folga na segunda.»", "→ «O feriado cai num domingo.» Não há folga extra.", "Праздник выпадает на воскресенье, в понедельник выходного нет."),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 198
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ERROS COMUNS　Частые ошибки", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 22
wt = "« proclamação »: o ato de anunciar — em 1889, o fim da monarquia e o começo da República."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("proclamação = провозглашение; в 1889 году монархия закончилась, а республика началась.", "sans", False, 20, CW - 44)) * 29 + 30
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "A PALAVRA　Слово недели", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "proclamação = провозглашение; в 1889 году монархия закончилась, а республика началась.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 22
lt = "«Vou fazer o segundo dia no domingo 15. Já conferi o cartão. Boa prova!» — EXEMPLO DA REDAÇÃO"
# W46 disclosure: VOL.2 promised real letters + best P8 texts for VOL.3; none had
# arrived by press time, so the labeled editor's example stands and the promise
# carries to VOL.4. No letters/texts fabricated; labeling kept verbatim in form.
disc_pt = "Nota da redação: as cartas reais e os melhores textos prometidos no VOL.2 não chegaram até o fechamento — fica o exemplo, e a promessa passa para o VOL.4."
disc_ru = "Примечание: настоящих писем и лучших текстов из VOL.2 не пришло. Пример остаётся, обещание — в VOL.4."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Пример редакции — не настоящее письмо. Присылайте письма!", "sans", False, 20, CW - 44)) * 29 + 10 + len(wrap(disc_pt, "serif", False, 21.5, CW - 44)) * 30.5 + 10 + len(wrap(disc_ru, "sans", False, 19.5, CW - 44)) * 29 + 22
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "CARTAS DOS LEITORES", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 20, "Пример редакции — не настоящее письмо. Присылайте письма!", 20, "sans", False, GREY, CW - 44, 1.42)
yy3 = p.para(bx + 22, yy3 + 10, disc_pt, 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(bx + 22, yy3 + 10, disc_ru, 19.5, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frases da semana (verbatim from this issue) ----
fy = max(1712, ly + lh + 14)
p.hline(MX, RIGHT, fy - 2, OLIVE, 2)  # rule below the CARTAS box (fy-14 cut the last line)
p.text(MX, fy + 24, "FRASES DA SEMANA　ФРАЗЫ НЕДЕЛИ (дословно из этого номера)", 27, "sans", True, OLIVE)
quotes = [
    ("«Dois domingos, um feriado: o Brasil faz o segundo dia do Enem»", "Два воскресенья, один праздник: Бразилия сдаёт второй день Enem.", "Página 1"),
    ("«A prova e o feriado chegam no mesmo dia»", "Экзамен и праздник приходят в один день.", "Página 1"),
    ("«o feriado não muda o relógio»", "Праздник не переводит часы.", "Página 2"),
    ("«A monarquia acabou»", "Монархия закончилась.", "Página 3"),
    ("«quem vai à final da Copa do Brasil?»", "Кто выйдет в финал Кубка Бразилии?", "Página 4"),
    ("«quem dorme bem lembra melhor»", "Хорошо спишь — лучше помнишь.", "Página 5"),
    ("«primeiro as fáceis, depois as difíceis»", "Сначала лёгкие, потом трудные.", "Página 6"),
    ("«Confira o cartão, durma bem, chegue cedo»", "Проверь карту, выспись, приходи рано.", "Página 2"),
]
colw = (RIGHT - MX - GUT) // 2
fr_end = 0  # lowest Frases translation end (adaptive band)
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 88
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    fr_end = max(fr_end, p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35))

# ---- próxima semana ----
py = max(2404, fr_end - 12)  # adaptive: keep the band clear of the Frases translations
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "A PRÓXIMA SEMANA　НА СЛЕДУЮЩЕЙ НЕДЕЛЕ (VOL.4)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "Sexta, 20 de novembro: o feriado da Consciência Negra. E os finalistas da Copa do Brasil, os gabaritos do Enem e as suas cartas e os melhores textos da página 8. Até segunda!", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lingua.svg")
print("P7 saved, exercises so far:", len(REG))
