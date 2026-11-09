# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LÍNGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LÍNGUA　TAAL", "A Lucerna", "Três níveis, três ferramentas　Drie niveaus, drie instrumenten")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　PERGUNTAS E O PRESENTE", 24)
a.para("Para perguntar o essencial da semana: «Que horas começa a prova?» — que horas + verbo no presente. E, para lugares, «Onde fica o meu local?» — onde fica.", 21.5)
a.para("E conferir é especial na primeira pessoa: eu confiro, você confere, ele confere. Nós conferimos, eles conferem.", 21.5)
a.bridge("Vragen: que horas (hoe laat) + werkwoord; onde fica vraagt waar een plaats is; conferir is onregelmatig in de eu-vorm: confiro.")
a.ex("A2", "Zin afmaken", "confiro", "conferir: eu → confiro (onregelmatig)",
     "Eu ___ (conferir) o cartão.", instr="Vul in", size=20.5, gap=10)
a.ex("A2", "Zin afmaken", "confere", "conferir: você → confere",
     "Você ___ (conferir) o local antes de sair.", instr="Vul in", size=20.5, gap=10)
a.ex("A2", "Zin afmaken", "termina", "terminar: ela → termina",
     "Que horas ___ (terminar) a prova do dia 15?", instr="Vul in", size=20.5, gap=10)
a.ex("A2", "Meerkeuze", "B", "onde vraagt naar de plaats",
     "«___ fica o meu local?» A. Que horas · B. Onde · C. Quando", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　O PRETÉRITO PERFEITO", 24)
b.para("Para contar a semana, usamos o pretérito perfeito: o Grêmio venceu, Maurício marcou, o candidato chegou. Vencer é regular: eu venci, ele venceu.", 21.5)
b.para("E o modelo é simples: marcar → marcou; chegar → chegou; dormir → dormiu. Atenção ao acento: saíram, caíram.", 21.5)
b.bridge("Om de week te vertellen gebruiken we de verleden tijd (pretérito perfeito); vencer is regelmatig (venceu); let op de klemtoon in de verleden tijd van marcar, chegar en dormir.")
b.ex("B1", "Zin afmaken", "venceu", "vencer, verleden tijd: venceu",
     "O Grêmio ___ (vencer) por 2 a 0.", instr="Vul in", size=20.5, gap=10)
b.ex("B1", "Zin afmaken", "marcou", "marcar, verleden tijd: marcou",
     "Maurício ___ (marcar) o gol do Palmeiras.", instr="Vul in", size=20.5, gap=10)
b.ex("B1", "Zin afmaken", "chegou", "chegar, verleden tijd: chegou",
     "O candidato ___ (chegar) cedo.", instr="Vul in", size=20.5, gap=10)
b.ex("B1", "Meerkeuze", "B", "venceram is de verleden tijd, meervoud, van vencer",
     "«Os times ___ a ida com vantagem.» A. vence · B. venceram · C. vencemos", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　O FUTURO DO SUBJUNTIVO", 24)
c.para("Depois de «quando», «se» e «quem», o futuro pede o subjuntivo: «Quando você chegar, apresente o documento.» «Quem tiver o cartão, confere o local.»", 21.5)
c.para("É o tempo da página 6: regras e condições. Ter → tiver; ser → for; chegar → chegar (regular). Não confunda com o presente: é a gramática das hipóteses sobre o domingo.", 21.5)
c.bridge("Na quando, se en quem komt de futuro van de aanvoegende wijs: tiver, for, chegar — de grammatica van de zondagshypothesen.")
c.ex("B2", "Zin afmaken", "tiver", "quem + futuro van de aanvoegende wijs: tiver",
     "Quem ___ (ter) o cartão confere o local antes do domingo.", instr="Vul in", size=20.5, gap=10)
c.ex("B2", "Zin afmaken", "chegar", "quando + futuro van de aanvoegende wijs: chegar",
     "Quando você ___ (chegar) ao local, apresente o documento.", instr="Vul in", size=20.5, gap=10)
c.ex("B2", "Zin afmaken", "for", "se + futuro van de aanvoegende wijs van ser: for",
     "Se o seu local ___ (ser) novo, saia mais cedo de casa.", instr="Vul in", size=20.5, gap=10)
c.ex("B2", "Meerkeuze", "B", "quando + toekomst → futuro van de aanvoegende wijs for",
     "«Quando ___ domingo, o país faz a prova.» A. é · B. for · C. seja", size=20.5, gap=10)
c.end_report()

# ---- col 3: erros comuns + a palavra + cartas ----
bx = COLX[3]
errs = [
    ("«Vou fazer o Enem de caneta azul.»", "→ «De caneta preta.» A caneta do Enem é preta.", "Alleen zwarte pen — blauw mag niet."),
    ("«Chego às 13h30, na hora da prova.»", "→ «Chego antes das 13h.» Os portões fecham às 13h.", "Sluiting om 13 uur — 13:30 is te laat."),
    ("«No dia 15, a prova termina às 19h.»", "→ «Termina às 18h30.» Às 19h, só no dia 8.", "Op de 15e eindigt het examen om 18:30; 19 uur hoort bij de 8e."),
    ("«O feriado dá folga na segunda.»", "→ «O feriado cai num domingo.» Não há folga extra.", "De feestdag valt op zondag, maandag geen inhaal."),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 198
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ERROS COMUNS　PAS OP!", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 22
wt = "« proclamação »: o ato de anunciar — em 1889, o fim da monarquia e o começo da República."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("proclamação = proclamatie; in 1889 eindigde de monarchie en begon de republiek.", "sans", False, 20, CW - 44)) * 29 + 30
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "A PALAVRA　WOORD VAN DE WEEK", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "proclamação = proclamatie; in 1889 eindigde de monarchie en begon de republiek.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 22
lt = "«Vou fazer o segundo dia no domingo 15. Já conferi o cartão. Boa prova!» — EXEMPLO DA REDAÇÃO"
# W46 disclosure: VOL.2 promised real letters + best P8 texts for VOL.3; none had
# arrived by press time, so the labeled editor's example stands and the promise
# carries to VOL.4. No letters/texts fabricated; labeling kept verbatim in form.
disc_pt = "Nota da redação: as cartas reais e os melhores textos prometidos no VOL.2 não chegaram até o fechamento — fica o exemplo, e a promessa passa para o VOL.4."
disc_nl = "Opmerking van de redactie: de echte brieven en beste teksten uit VOL.2 waren nog niet binnen — het voorbeeld blijft, de belofte gaat naar VOL.4."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Voorbeeld van de redactie — geen echte brief. Stuur je brief op!", "sans", False, 20, CW - 44)) * 29 + 10 + len(wrap(disc_pt, "serif", False, 21.5, CW - 44)) * 30.5 + 10 + len(wrap(disc_nl, "sans", False, 19.5, CW - 44)) * 29 + 22
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "CARTAS DOS LEITORES", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 20, "Voorbeeld van de redactie — geen echte brief. Stuur je brief op!", 20, "sans", False, GREY, CW - 44, 1.42)
yy3 = p.para(bx + 22, yy3 + 10, disc_pt, 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(bx + 22, yy3 + 10, disc_nl, 19.5, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frases da semana (verbatim from this issue) ----
fy = max(1712, ly + lh + 14)
p.hline(MX, RIGHT, fy - 2, OLIVE, 2)  # rule below the CARTAS box (fy-14 cut the last line)
p.text(MX, fy + 24, "FRASES DA SEMANA　ZINNEN VAN DE WEEK (letterlijk uit dit nummer)", 27, "sans", True, OLIVE)
quotes = [
    ("«Dois domingos, um feriado: o Brasil faz o segundo dia do Enem»", "Twee zondagen, één feestdag: Brazilië maakt de tweede dag van de Enem.", "Página 1"),
    ("«A prova e o feriado chegam no mesmo dia»", "Het examen en de feestdag komen op dezelfde dag.", "Página 1"),
    ("«o feriado não muda o relógio»", "De feestdag verandert de klok niet.", "Página 2"),
    ("«A monarquia acabou»", "De monarchie is voorbij.", "Página 3"),
    ("«quem vai à final da Copa do Brasil?»", "Wie haalt de finale van de Copa do Brasil?", "Página 4"),
    ("«quem dorme bem lembra melhor»", "Goed slapen, beter onthouden.", "Página 5"),
    ("«primeiro as fáceis, depois as difíceis»", "Eerst de makkelijke, dan de moeilijke.", "Página 6"),
    ("«Confira o cartão, durma bem, chegue cedo»", "Controleer je kaart, slaap goed, kom vroeg.", "Página 2"),
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
p.text(MX + 28, py + 44, "A PRÓXIMA SEMANA　VOLGENDE WEEK (VOL.4)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "Sexta, 20 de novembro: o feriado da Consciência Negra. E os finalistas da Copa do Brasil, os gabaritos do Enem e as suas cartas e os melhores textos da página 8. Até segunda!", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lingua.svg")
print("P7 saved, exercises so far:", len(REG))
