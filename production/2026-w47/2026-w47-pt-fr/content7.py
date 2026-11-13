# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LÍNGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LÍNGUA　Langue", "A Lucerna", "La langue en vedette　Três níveis, três ferramentas　Trois niveaux, trois outils")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　O FERIADO E AS DATAS", 24)
a.para("Para falar de um feriado, usamos «em» com a data: «em 20 de novembro». E, para o dia, «no dia 20». E o verbo da semana é «cair»: o feriado cai numa sexta — cair é o verbo dos feriados no calendário.", 21.5)
a.para("E «aproveitar» é o verbo do feriadão: eu aproveito, você aproveita, nós aproveitamos.", 21.5)
a.bridge("Pour parler d'un jour férié, on emploie em + la date (em 20 de novembro), no dia 20 ; cair signifie « tomber un jour » ; et les conjugaisons d'aproveitar.")
a.ex("A2", "Complétez la phrase", "em", "em + date : em 20 de novembro",
     "O feriado é ___ 20 de novembro.", instr="Complétez", size=20.5, gap=10)
a.ex("A2", "Complétez la phrase", "numa", "cair numa sexta-feira:tombe un vendredi",
     "O feriado cai ___ sexta-feira.", instr="Complétez", size=20.5, gap=10)
a.ex("A2", "Complétez la phrase", "é", "ser, présent, forme ele : é",
     "Que dia ___ (ser) o feriado?", instr="Complétez", size=20.5, gap=10)
a.ex("A2", "Choix multiple", "B", "aproveitar : forme nós aproveitamos",
     "«Nós ___ o feriadão.» A. aproveita · B. aproveitamos · C. aproveito", size=20.5, gap=10)
a.end_report()
a_end = a.y

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　O PRETÉRITO PERFEITO", 24)
b.para("Para contar o fim de semana da Copa, usamos o pretérito perfeito: o Grêmio empatou, o Vasco venceu, Norris venceu. Empatar é regular: eu empatei, ele empatou.", 21.5)
b.para("E o modelo é simples: abrir → abriu; garantir → garantiu; sair → saiu. Atenção ao acento: saíram, caíram.", 21.5)
b.bridge("Pour raconter le week-end de la Coupe, on emploie le pretérito perfeito ; empatar est régulier (empatou) ; attention à l'accent au passé d'abrir, garantir et sair.")
b.ex("B1", "Complétez la phrase", "empatou", "empatar passé : empatou",
     "O Grêmio ___ (empatar) por 1 a 1.", instr="Complétez", size=20.5, gap=10)
b.ex("B1", "Complétez la phrase", "venceu", "vencer passé : venceu",
     "O Vasco ___ (vencer) por 2 a 1.", instr="Complétez", size=20.5, gap=10)
b.ex("B1", "Complétez la phrase", "abriu", "abrir passé : abriu",
     "Renan Lodi ___ (abrir) o placar.", instr="Complétez", size=20.5, gap=10)
b.ex("B1", "Choix multiple", "B", "saíram est le passé, pluriel, de sair",
     "«Os finalistas ___ no fim de semana.» A. saem · B. saíram · C. sairão", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　O FUTURO DO SUBJUNTIVO", 24)
c.para("Depois de «quando», «se» e «quem», o futuro pede o subjuntivo: «Quando sair o gabarito, confira as respostas.» «Se a sua nota for boa, comemore.»", 21.5)
c.para("É o tempo da página 6: regras e condições. Sair → sair; ser → for; ter → tiver. Não confunda com o presente: é a gramática das hipóteses sobre o gabarito.", 21.5)
c.bridge("quando, se, quem prennent le futur du subjonctif : sair, for, tiver (la grammaire de l'attente du corrigé officiel).")
c.ex("B2", "Complétez la phrase", "sair", "quando + futur du subjonctif : sair",
     "Quando ___ (sair) o gabarito, confira as respostas.", instr="Complétez", size=20.5, gap=10)
c.ex("B2", "Complétez la phrase", "for", "se + ser futur du subjonctif : for",
     "Se a sua nota ___ (ser) boa, comemore.", instr="Complétez", size=20.5, gap=10)
c.ex("B2", "Complétez la phrase", "tiver", "quem + futur du subjonctif : tiver",
     "Quem ___ (ter) o cartão confere o local antes do domingo.", instr="Complétez", size=20.5, gap=10)
c.ex("B2", "Choix multiple", "B", "quando + l'avenir → futur du subjonctif sair",
     "«Quando ___ o gabarito, o país respira.» A. sai · B. sair · C. saia", size=20.5, gap=10)
c.end_report()

# ---- image under the A2 column: Os Lusíadas, 1572 ----
iy7 = a_end + 30
image(p, "lusiadas.jpg", COLX[0] + 81, iy7, 260, 392)
caption(p, COLX[0], iy7 + 392, CW,
        "A primeira edição de «Os Lusíadas», de Luís de Camões, Lisboa, 1572: a língua portuguesa impressa há mais de 450 anos.",
        "Domínio público / Wikimedia Commons")
print("P7 image ends ~", iy7 + 392 + 110)

# ---- col 3: erros comuns + a palavra + cartas ----
bx = COLX[3]
errs = [
    ("«O gabarito já saiu no domingo 15.»", "→ «Só o extraoficial.» O oficial do Inep sai até o fim de novembro.", "Le corrigé officiel ne sort qu'à la fin novembre."),
    ("«O feriado dá folga na segunda, 23.»", "→ «Não há folga extra.» O feriadão termina no domingo 22.", "Le long week-end se termine le dimanche ; pas de congé le lundi."),
    ("«O Palmeiras passou no tempo normal.»", "→ «Passou nos pênaltis, 5 a 4.» No tempo normal, o Vasco venceu por 2 a 1.", "Palmeiras s'est qualifié 5–4 aux tirs au but ; Vasco a gagné 2–1."),
    ("«O dia 20 cai num domingo.»", "→ «Cai numa sexta-feira.» O feriadão vai de 20 a 22.", "Le 20 novembre est un vendredi ; le long week-end va jusqu'au dimanche 22."),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 198
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ERROS COMUNS　Erreurs", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 22
wt = "« consciência »: saber e lembrar — de si, da história e dos outros. «Consciência Negra» é a memória da luta e da cultura afro-brasileiras."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("consciência = conscience, mémoire : la mémoire de la lutte et de la culture.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "A PALAVRA　Le mot de la semaine", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "consciência = conscience, mémoire : la mémoire de la lutte et de la culture.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 22
lt = "«Vou aproveitar o feriadão para ler sobre Zumbi. Bom feriado!» — EXEMPLO DA REDAÇÃO"
# W47 disclosure: VOL.3 promised real letters + best P8 texts for VOL.4; none had
# arrived by press time, so the labeled editor's example stands and the promise
# carries to VOL.5. No letters/texts fabricated; labeling kept verbatim in form.
disc_pt = "Nota da redação: as cartas reais e os melhores textos do VOL.3 não chegaram até o fechamento — fica o exemplo, e a promessa passa para o VOL.5."
disc_fr = "Note de la rédaction : ni lettres ni meilleurs textes du VOL.3 avant le bouclage — l'exemple reste, la promesse passe au VOL.5."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Exemple de la rédaction — pas une vraie lettre. Envoyez-nous vos lettres!", "sans", False, 20, CW - 44)) * 29 + 10 + len(wrap(disc_pt, "serif", False, 21.5, CW - 44)) * 30.5 + 10 + len(wrap(disc_fr, "sans", False, 19.5, CW - 44)) * 29 + 22
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "CARTAS DOS LEITORES", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 20, "Exemple de la rédaction — pas une vraie lettre. Envoyez-nous vos lettres!", 20, "sans", False, GREY, CW - 44, 1.42)
yy3 = p.para(bx + 22, yy3 + 10, disc_pt, 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(bx + 22, yy3 + 10, disc_fr, 19.5, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frases da semana (verbatim from this issue) ----
fy = max(1712, ly + lh + 16)
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "FRASES DA SEMANA　Les phrases de la semaine (extraites mot pour mot de ce numéro)", 27, "sans", True, OLIVE)
quotes = [
    ("«Consciência Negra: sexta é feriado em todo o país»", "Jour de la Conscience noire : jour férié national un vendredi.", "Página 1"),
    ("«o feriado abre um fim de semana de três dias»", "Le jour férié ouvre un week-end de trois jours.", "Página 1"),
    ("«Zumbi nasceu em Palmares»", "Zumbi est né à Palmares.", "Página 3"),
    ("«sem memória, não há futuro»", "Sans mémoire, il n'y a pas d'avenir.", "Página 3"),
    ("«o agregado ficou em 2 a 2»", "Le score cumulé est resté à 2–2.", "Página 4"),
    ("«a espera pelo gabarito»", "L'attente du corrigé officiel.", "Página 5"),
    ("«primeiro as fáceis, depois as difíceis»", "D'abord les faciles, puis les difficiles.", "Página 6"),
    ("«Confira o transporte, guarde o documento e aproveite o feriadão»", "Vérifiez les transports, préparez vos papiers, puis profitez bien du long week-end.", "Página 2"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 80
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- próxima semana ----
py = 2404
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "A PRÓXIMA SEMANA　La semaine prochaine (VOL.5)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "Sexta, 27 de novembro: a Black Friday. E o gabarito oficial do Enem, até o fim do mês — e a final da Copa se aproxima: dia 6 de dezembro, em Brasília. Até segunda!", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lingua.svg")
print("P7 saved, exercises so far:", len(REG))
