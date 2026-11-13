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
p.text(MX, 92, "VOL. 4　QUARTA EDIÇÃO", 17, "sans", True, OLIVE, spacing=1.7)
p.text(975, 92, "TODA SEMANA EM PORTUGUÊS　Elke week　Het Portugees dat Brazilië leest", 17, "sans", False, GREY, anchor="middle", spacing=1.7)
p.text(RIGHT, 92, "SEMANA DE 16 A 22 DE NOVEMBRO DE 2026", 17, "sans", False, GREY, anchor="end", spacing=1.7)
p.text(975, 262, "A Lucerna", 196, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "PORTUGEES WEEKBLAD　VOL.4　CONSCIÊNCIA NEGRA　GABARITO DO ENEM　A FINAL DA COPA", 32, "serif", True, OLIVE, anchor="middle", spacing=0)
p.text(975, 372, "TEKSTEN IN HET PORTUGEES　UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS", 16, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)

# band
p.rect(MX, 470, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 30, 524, "O FERIADÃO!", 46, "sans", True, ONCLOTH)
p.text(MX + 30, 568, "Sexta, 20 de novembro: o feriado da Consciência Negra abre um fim de semana de três dias.", 25, "serif", False, "#cac8ba")
p.text(RIGHT - 30, 524, "een driedaags weekend", 27, "sans", True, GOOSE, anchor="end")
p.text(RIGHT - 30, 568, "Vrijdag 20 november　Dag van het Zwarte Bewustzijn, nationale feestdag", 18, "sans", False, GOOSE, anchor="end")

# ---- headline (span cols 0-2) ----
hy = 590
p.text(MX, hy + 26, "A NOTÍCIA　Hoofdverhaal", 17, "sans", True, OLIVE)
hy = p.para(MX, hy + 92, "Consciência Negra: sexta é feriado em todo o país", 53, "serif", True, INK, 1323, 1.06)
p.text(MX, hy + 28, "Da redação da A Lucerna　Nível de leitura: A2", 17, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Sexta, 20 de novembro, é feriado nacional: o Dia Nacional de Zumbi e da Consciência Negra. A data lembra a morte de Zumbi dos Palmares, em 1695, líder do Quilombo dos Palmares. Como cai numa sexta, o feriado abre um fim de semana de três dias — de 20 a 22 de novembro.", size=24)
f.para("É feriado em todo o país desde a Lei nº 14.759, de 2023, que vale em todos os estados e municípios. A data é de memória e reflexão: a história e a cultura afro-brasileiras, e o combate ao racismo. Nas escolas, a semana tem rodas de conversa, capoeira, samba e leituras sobre Palmares.", size=24)
f.para("E a semana é também a semana do gabarito: no domingo 15, milhões de estudantes fazem o segundo dia do Enem — Ciências da Natureza e Matemática, das 13h30 às 18h30. Depois da prova, começa a espera: o gabarito oficial do Inep sai até o 10º dia útil depois do segundo dia — até o fim de novembro (páginas 5 e 6).", size=24)
f.para("No futebol, a final está decidida: Grêmio e Palmeiras jogam a decisão da Copa do Brasil no dia 6 de dezembro, no Mané Garrincha, em Brasília. O Grêmio empatou por 1 a 1 com o Atlético-MG no sábado 7, e o Palmeiras venceu o Vasco nos pênaltis, por 5 a 4, no domingo 8 (página 4).", size=24)
f.para("E o Brasileirão volta: depois da pausa para a Seleção, a rodada 35 termina na quarta 18 e na quinta 19 — e no sábado 21, às 16h30, Palmeiras × Flamengo, o jogo que pode decidir o título. Boa leitura — e bom feriadão!", size=24)
f.bridge("Trefwoorden｜a consciência bewustzijn, geweten · o feriadão een driedaags weekend · o gabarito antwoordmodel · a decisão de finale.")
f.box("A SEMANA EM NÚMEROS　In cijfers", [
    ("20 — o dia do feriado: sexta, 20 de novembro (vrijdag 20 november, feestdag)", "serif", False, INK, 20, 1.35),
    ("1695 — o ano da morte de Zumbi dos Palmares (Zumbi stierf in 1695)", "serif", False, INK, 20, 1.35),
    ("2023 — o ano da lei do feriado nacional (wet van 2023: nationale feestdag)", "serif", False, INK, 20, 1.35),
    ("3 — os dias do feriadão: de 20 a 22 de novembro (lang weekend van 3 dagen: 20–22 november)", "serif", False, INK, 20, 1.35),
], tsize=20)
f.head("AGORA VOCÊ　Nu jij", 25)
f.ex("A2", "Maak de zin af", "consciência", "consciência = bewustzijn, geweten (Dag van het Zwarte Bewustzijn)",
     "O dia 20 é o Dia da ___ Negra.", size=19.5, gap=6)
f.ex("A2", "Maak de zin af", "feriado", "feriado = feestdag",
     "O dia 20 é ___ nacional.", size=19.5, gap=6)
f.ex("A2", "Maak de zin af", "sexta", "sexta = Vrijdag",
     "Em 2026, o dia 20 cai numa ___.", size=19.5, gap=6)
f.ex("A2", "Maak de zin af", "três", "Drie vrije dagen: 20, 21 en 22",
     "O feriadão tem ___ dias.", size=19.5, gap=6)
f.ex("A2", "Maak de zin af", "6", "De finale is op 6 december",
     "A final da Copa é no dia ___ de dezembro.", size=19.5, gap=6)
f.ex("B1", "Maak de zin af", "decidem", "decidir, tegenwoordige tijd, vorm van eles: decidem",
     "Grêmio e Palmeiras ___ a Copa no dia 6 de dezembro.", size=19.5, gap=6)
f.end_report()

# ---- a semana, dia a dia (col 3) ----
gx, gw = COLX[3], CW
gy = 588
semana = ["Seg 16 — começa a semana do feriado e do gabarito.",
          "Ter 17 — Singapura × Brasil, às 7h, amistoso da Seleção.",
          "Qua 18 — Brasileirão: Cruzeiro × Palmeiras, às 20h30.",
          "Qui 19 — Brasileirão: São Paulo × Fluminense, às 21h30.",
          "Sex 20 — Consciência Negra: feriado nacional.",
          "Sáb 21 — Palmeiras × Flamengo, às 16h30: o jogo do título.",
          "Dom 22 — fim do feriadão; a Black Friday chega na sexta, 27."]
LHS = 21.5 * 1.35  # day-item line height; the box height MUST count the full
# per-item drawing cost (top offset 8 + lines*LHS + bottom gap 6) — the old
# formula counted only lines*30.5+12 and hid the last item behind the box below.
sh = 104 + sum(8 + len(wrap(t, "serif", False, 21.5, gw - 44)) * LHS + 6 for t in semana) + 16
p.rect(gx, gy, gw, sh, fill=BOX)
p.text(gx + 22, gy + 40, "A SEMANA, DIA A DIA", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "16 a 22 de novembro", 19, "sans", False, GREY)
yy = gy + 104
for t in semana:
    yy = p.para(gx + 22, yy + 8, t, 21.5, "serif", False, INK, gw - 44, 1.35) + 6
print("P1 col3 semana ends", gy + sh)

# ---- conteúdo (col 3) ----
sy = gy + sh + 26
p.rect(gx, sy, gw, 340, fill="#f0eee5")
p.text(gx + 22, sy + 40, "NESTA EDIÇÃO　In dit nummer", 24, "sans", True, OLIVE)
som = [
    ("Pág. 2", "Feriado e feriadão", "A2"),
    ("Pág. 3", "Zumbi e Palmares", "A2→B1"),
    ("Pág. 4", "A final da Copa", "B1"),
    ("Pág. 5", "Depois do Enem", "B1"),
    ("Pág. 6", "O gabarito explicado", "B2"),
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
my = sy + 340 + 26
p.text(gx, my + 24, "A PALAVRA DA SEMANA", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, OLIVE, 2)
p.text(gx, my + 76, "« consciência »", 21.5, "serif", False, INK, italic=True)
wy = p.para(gx, my + 108, "saber e lembrar — de si, da história e dos outros.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, wy + 10, "consciência = bewustzijn, geweten: weten en herinneren.", 19, "sans", False, GREY, gw, 1.35)
print("P1 col3 ends", wy + 60)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "capoeira.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "Roda de capoeira no Rio de Janeiro, em gravura de Johann Moritz Rugendas (Voyage pittoresque dans le Brésil, Paris, 1835): jogo, dança e resistência — a cultura afro-brasileira no centro desta edição. (Página 3)",
        "Gravura: Johann Moritz Rugendas / Wikimedia Commons — Domínio público")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2300, tag="P1-tv")
f2.head("A SEMANA EM DOIS TEMPOS", 25)
f2.para("Sexta, 20: o feriado abre o fim de semana. Sábado, 21: Palmeiras × Flamengo, às 16h30. Domingo, 22: o feriadão termina — e a Black Friday chega na sexta, 27.", 21.5)
f2.para("Na segunda, 16, começa a espera: os cursinhos publicam as suas respostas na noite do dia 15; o oficial do Inep sai até o fim do mês.", 21.5)
f2.end_report()
# col 3 EM POUCAS PALAVRAS — fix1 (2026-11-11): box 436->474 (+38).
# Last line 'em Brasília. (Página 4)' baseline 2327.6 sat 17.6px below the
# old bottom 2310; pt-es PIL ink run reaches 2342 (inktonderkant +33, incl. the quiz
# rule/title crowding the scan band — the spill line's own glyphs end
# ~2332, descender 'g' +4px). +38 puts the bottom at 2348: +6px clear of
# the pt-es ink measure, ~+16px clear of the spill line's own ink bottom.
# Quiz section below shifts by the same +38 (qy 2312->2350); quiz flow
# (max block 138.4px) still fits: top 2404 + 138.4 = 2542.4 <= 2560.
bx = COLX[3]
p.rect(bx, 1874, CW, 474, fill=BOX)
p.text(bx + 22, 1914, "EM POUCAS PALAVRAS　KORTOM", 20, "sans", True, OLIVE)
brefs = [
    ("O FERIADO", "Sexta, 20: Dia Nacional de Zumbi e da Consciência Negra, feriado nacional — um fim de semana de três dias. (Página 3)"),
    ("O GABARITO", "Depois do segundo dia do Enem, no domingo 15: o gabarito oficial sai até o fim de novembro. (Página 6)"),
    ("O FUTEBOL", "Grêmio e Palmeiras na final da Copa do Brasil: a decisão é no dia 6 de dezembro, em Brasília. (Página 4)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, OLIVE)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# fix1 (2026-11-11): qy 2312->2350, same +38 as the flash box above.
qy = 2350
p.hline(MX, RIGHT, qy, OLIVE, 2)
p.text(MX, qy + 36, "QUIZ RELÂMPAGO　Bliksemquiz", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Lees de voorpagina en kies het juiste antwoord　Antwoorden op pagina 8", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2560, tag="P1-quiz")
qf.ex("A2", "Meerkeuze", "B", "De Dag van het Zwarte Bewustzijn is op 20 november",
      "O feriado da Consciência Negra é... A. no dia 15 · B. no dia 20 · C. no dia 27", size=21)
qf.ex("A2", "Meerkeuze", "B", "In 2026 is 20 november een vrijdag",
      "Em 2026, o dia 20 de novembro cai... A. num domingo · B. numa sexta · C. numa segunda", size=21)
qf.ex("A2", "Meerkeuze", "C", "De finale: Grêmio × Palmeiras",
      "A final da Copa do Brasil é entre... A. Grêmio e Vasco · B. Atlético-MG e Palmeiras · C. Grêmio e Palmeiras", size=21)
qf.ex("A2", "Meerkeuze", "B", "De officiële antwoorden verschijnen vóór eind november",
      "O gabarito oficial do Enem sai... A. no dia da prova · B. até o fim de novembro · C. em janeiro", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-capa.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · VIDA (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("VIDA　Dagelijks leven", "A Lucerna", "NÍVEL A2　O feriado e o feriadão　De feestdag en het lange weekend")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("Sexta, 20 de novembro: o feriado e o feriadão", 32)
f.byline("Da redação da A Lucerna　Nível de leitura: A2")
f.para("Sexta, 20 de novembro, é feriado nacional: o Dia Nacional de Zumbi e da Consciência Negra. O que fecha e o que abre no feriado? As escolas e os escritórios públicos fecham. O comércio segue o horário de feriado — e os ônibus e trens podem rodar em horário reduzido. Antes de sair, confira o transporte.")
f.para("O feriadão tem três dias: sexta, 20, sábado, 21, e domingo, 22. Para quem trabalha de segunda a sexta, são três dias de descanso seguidos — sem trabalhar e sem pressa. Na segunda, 23, tudo volta ao normal: não há ponte nem folga extra.")
f.para("E a semana tem programação: rodas de capoeira, samba, feiras de livros e exposições sobre a história afro-brasileira. Nas escolas, a semana é de leituras e conversas sobre Zumbi dos Palmares e o Quilombo dos Palmares.")
f.para("Novembro é também o Novembro Azul, a campanha de prevenção do câncer de próstata — um mês para lembrar o exame e a conversa com o médico. E no comércio, a contagem para a Black Friday: é na sexta, dia 27, uma semana depois do feriado.")
f.head("E O COMÉRCIO NO FERIADO?", 25)
f.para("No feriado, muitas lojas de rua fecham e os shoppings abrem em horário especial. Antes de sair, confira o horário da sua cidade — e, se vai comprar na Black Friday, compare os preços antes: o desconto começa na propaganda, não na etiqueta.", 23.5)
f.box("PARA NÃO ERRAR　Ezelsbruggetje", [
    ("«Confira o transporte, guarde o documento e aproveite o feriadão.» Três passos e o fim de semana fica tranquilo: no feriado, confira também o horário do comércio.", "serif", False, INK, 21.5, 1.4),
], tsize=21)
f.gloss("o feriadão een driedaags weekend · a folga vrije tijd · a programação programma · o transporte vervoer · aproveitar goed benutten · a etiqueta prijskaartje.")
f.end_report()

# col 3: facts + e você? (sequential, measured)
ix = COLX[3]
facts = ["O dia 20 lembra a morte de Zumbi dos Palmares, em 1695.",
         "É feriado nacional desde a Lei nº 14.759, de 2023.",
         "Em 2026, o feriado cai numa sexta — feriadão de três dias."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 38
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "VOCÊ SABIA?", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E você? No seu país, há um feriado que lembra a luta contra a escravidão? Escreva duas frases em português e mande para a redação: as melhores saem na página 7, «Cartas dos leitores»."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Is er in jouw land een feestdag die de strijd tegen de slavernij herdenkt? Schrijf twee zinnen en stuur ze op.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E VOCÊ?　Vertel over jezelf", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Is er in jouw land een feestdag die de strijd tegen de slavernij herdenkt? Schrijf twee zinnen en stuur ze op.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- O feriadão, dia a dia: 4 day boxes ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, OLIVE, 2)
p.text(MX, dy + 28, "O FERIADÃO, DIA A DIA　Het lange weekend, dag voor dag", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "Três dias, uma semana　Drie vrije dagen, een week gepland", 20, "sans", False, GREY, anchor="end")
times = [
    ("SEX 20", "o feriado começa", "Vrijdag 20 november, feestdag"),
    ("SÁB 21", "Palmeiras × Flamengo, às 16h30", "Zaterdag 16:30 de kraker Palmeiras–Flamengo"),
    ("DOM 22", "o fim do feriadão", "Op zondag eindigt het lange weekend"),
    ("SEG 23", "tudo volta ao normal", "Op maandag wordt alles weer normaal"),
]
for i, (t, lab, cn) in enumerate(times):
    bx = COLX[i]
    p.rect(bx, dy + 52, CW, 150, fill=BOX)
    p.text(bx + 22, dy + 116, t, 32, "serif", True, OLIVE)
    yy = p.para(bx + 152, dy + 92, lab, 21.5, "serif", False, INK, CW - 174, 1.36)
    p.para(bx + 152, yy + 20, cn, 19, "sans", False, GREY, CW - 174, 1.3)
p.para(MX, dy + 234, "Atenção: o feriado é nacional, mas cada cidade tem as suas regras para o comércio e o transporte. Confira o horário local antes de sair — e aproveite a sexta para descansar.", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P2 exercises ----
ey = dy + 282
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EXERCÍCIOS　OEFENINGEN VAN PAGINA 2", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antwoorden op pagina 8　De niveaus lopen door elkaar — zoek de antwoorden op nummer", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A　COMPREENSÃO", 22)
e.bridge("Lees het artikel op pagina 2 en kies het juiste antwoord.")
e.ex("A2", "Meerkeuze", "B", "De Dag van het Zwarte Bewustzijn is op 20 november",
     "O feriado da Consciência Negra é... A. no dia 15 · B. no dia 20 · C. no dia 27", size=20, gap=8)
e.ex("A2", "Meerkeuze", "B", "In 2026 is 20 november een vrijdag",
     "Em 2026, o feriado cai... A. numa segunda · B. numa sexta · C. num domingo", size=20, gap=8)
e.ex("A2", "Meerkeuze", "B", "Drie vrije dagen: 20, 21 en 22",
     "O feriadão dura... A. dois dias · B. três dias · C. cinco dias", size=20, gap=8)
e.ex("A2", "Meerkeuze", "B", "Op de feestdag rijden er mogelijk minder bussen",
     "No feriado, o transporte... A. para sempre · B. pode rodar em horário reduzido · C. é grátis", size=20, gap=8)
e.ex("A2", "Meerkeuze", "B", "Black Friday is op 27 november",
     "A Black Friday é... A. no dia 20 · B. no dia 27 · C. no dia 15", size=20, gap=8)
e.head("B　O PRESENTE", 22)
e.bridge("Vul de tegenwoordige tijd van het werkwoord in.")
e.ex("A2", "Maak de zin af", "cai", "cair, tegenwoordige tijd, vorm van ele: cai",
     "O feriado ___ (cair) numa sexta-feira.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Maak de zin af", "dura", "durar, tegenwoordige tijd, vorm van ele: dura",
     "O feriadão ___ (durar) três dias.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Maak de zin af", "descansamos", "descansar, tegenwoordige tijd, vorm van nós: descansamos",
     "Nós ___ (descansar) no feriado.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Maak de zin af", "abrem", "abrir, tegenwoordige tijd, vorm van elas: abrem",
     "As lojas ___ (abrir) em horário especial.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Maak de zin af", "aproveita", "aproveitar, tegenwoordige tijd, vorm van você: aproveita",
     "Você ___ (aproveitar) o feriadão?", instr="Vul in", size=20, gap=8)
e.head("C　COMPLETE COM OS NÚMEROS", 22)
e.bridge("Vul de cijfers van pagina 1 en 2 in.")
e.ex("A2", "Maak de zin af", "3", "20, 21 en 22: in totaal 3 dagen",
     "O feriadão tem ___ dias.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Maak de zin af", "1695", "Zumbi stierf in 1695",
     "Zumbi morreu em ___ .", instr="Vul in", size=20, gap=8)
e.ex("B1", "Maak de zin af", "2023", "De wet van 2023 maakte er een nationale feestdag van",
     "A Lei nº 14.759 é de ___ .", instr="Vul in", size=20, gap=8)
e.ex("A2", "Maak de zin af", "27", "Black Friday is op 27 november",
     "A Black Friday é no dia ___ de novembro.", instr="Vul in", size=20, gap=8)
e.head("D　AS PALAVRAS", 22)
e.match_set("A2", "Woordenschat koppelen",
            ["o feriadão", "a folga", "a programação", "aproveitar"],
            ["um fim de semana longo com feriado",
             "o tempo livre sem trabalho",
             "a lista de eventos da semana",
             "usar bem um tempo livre"],
            ["a", "b", "c", "d"],
            ["feriadão=een lang weekend met een feestdag a", "folga=vrije tijd zonder werk b", "programação=het programma van de week c", "aproveitar=goed gebruikmaken van vrije tijd d"],
            instr="Koppel")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-vida.svg")
print("P2 saved, exercises so far:", len(REG))
