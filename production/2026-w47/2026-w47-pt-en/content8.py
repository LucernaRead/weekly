# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · AVALIAÇÃO E RESPOSTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("AVALIAÇÃO E RESPOSTAS　Test and answers", "A Lucerna", "PAGE 8　The big test of the week + all the answers")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETE A CRÔNICA", 22, OLIVE, 5)
f.ex("B1", "Cloze", "A", "Friday 20 November is a national holiday",
     "Sexta, 20 de novembro, é ___ no Brasil. (A. feriado nacional · B. dia útil)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "The holiday remembers Zumbi dos Palmares",
     "O feriado lembra a morte de ___ . (A. Zumbi dos Palmares · B. Deodoro da Fonseca)", size=14.5, gap=0)
f.ex("B1", "Cloze", "B", "In 2026 the holiday falls on a Friday",
     "Em 2026, o feriado cai numa ___ . (A. segunda · B. sexta)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "The Copa do Brasil final is on 6 December",
     "A final da Copa do Brasil é no dia ___ de dezembro. (A. 6 · B. 15)", size=14.5, gap=0)
f.ex("B1", "Cloze", "B", "The final: Grêmio × Palmeiras",
     "Na final, jogam Grêmio e ___ . (A. Vasco · B. Palmeiras)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "The official answer key comes out by the end of November",
     "O gabarito oficial sai até o ___ de novembro. (A. fim · B. dia 8)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "The second day of the Enem is on 15 November",
     "O segundo dia do Enem foi no domingo ___ . (A. 15 · B. 8)", size=14.5, gap=0)
f.ex("B1", "Cloze", "B", "The second day's exam lasts 5 hours",
     "No dia 15, a prova dura ___ horas. (A. três · B. cinco)", size=14.5, gap=0)
f.head("B　PERGUNTAS GERAIS", 22, OLIVE, 5)
f.ex("A2", "Multiple choice", "B", "The 2023 law made 20 November a national holiday",
     "A Lei nº 14.759, de 2023... A. criou o dia 20 · B. fez do dia 20 feriado nacional · C. acabou com o feriado", size=14.5, gap=0)
f.ex("B1", "Multiple choice", "A", "Grêmio went through 3–1 on aggregate",
     "O Grêmio passou à final com... A. 3 a 1 no total · B. 2 a 2 no total · C. 1 a 0 no total", size=14.5, gap=0)
f.ex("B1", "Multiple choice", "B", "Penalties 5–4: Palmeiras go through",
     "Nos pênaltis, o Palmeiras venceu por... A. 4 a 3 · B. 5 a 4 · C. 6 a 5", size=14.5, gap=0)
f.ex("B1", "Multiple choice", "B", "Norris won the São Paulo Grand Prix",
     "O Grande Prêmio de São Paulo foi vencido por... A. Verstappen · B. Norris · C. Hadjar", size=14.5, gap=0)
f.ex("B1", "Multiple choice", "A", "Round 36: Palmeiras × Flamengo on Saturday the 21st",
     "A rodada 36 tem Palmeiras × Flamengo no... A. sábado 21 · B. domingo 22 · C. dia 15", size=14.5, gap=0)
f.ex("A2", "Multiple choice", "B", "Capoeira is an Afro-Brazilian art of fighting and music",
     "A capoeira é... A. um jogo de cartas · B. uma arte afro-brasileira de luta e música · C. um prato típico", size=14.5, gap=0)
f.ex("B2", "Multiple choice", "A", "10 is the number of working days until the answer key",
     "O número 10, na página 6, mede... A. os dias úteis até o gabarito · B. os gols da final · C. os feriados", size=14.5, gap=0)
f.ex("B1", "Multiple choice", "A", "Palmares was in Alagoas",
     "O Quilombo dos Palmares ficava... A. em Alagoas · B. no Rio · C. em São Paulo", size=14.5, gap=0)
f.head("C　LEIA E RESPONDA", 22, OLIVE, 5)
f.para("Rafael mora em Salvador. Na sexta, 20, ele não trabalha: é feriado nacional. De manhã, ele vai a uma roda de capoeira no Pelourinho. À tarde, ele lê sobre Zumbi e Palmares e escreve duas frases em português. No sábado, 21, ele assiste a Palmeiras × Flamengo na televisão. No domingo, 22, ele descansa e prepara a semana: na segunda, ele volta ao trabalho e confere o gabarito extraoficial do Enem.", 15.5, lh=1.3, split=False)
f.ex("A2", "Multiple choice", "B", "Rafael lives in Salvador",
     "Onde mora Rafael? A. no Rio · B. em Salvador · C. em Brasília", size=14.5, gap=0)
f.ex("A2", "Multiple choice", "B", "On Friday he goes to a capoeira roda",
     "Na sexta, 20, Rafael... A. trabalha · B. vai a uma roda de capoeira · C. faz o Enem", size=14.5, gap=0)
f.ex("A2", "Multiple choice", "A", "On Saturday he watches Palmeiras × Flamengo",
     "No sábado, 21, Rafael assiste... A. a Palmeiras × Flamengo · B. ao Enem · C. a uma aula", size=14.5, gap=0)
f.ex("A2", "Multiple choice", "B", "On Monday he checks the unofficial answer key",
     "Na segunda, Rafael confere... A. o gabarito oficial · B. o gabarito extraoficial · C. a nota final", size=14.5, gap=0)
f.head("D　CONSTRUA AS FRASES", 22, OLIVE, 5)
f.ex("A2", "Sentence building", "Sexta é feriado nacional.", "The time word comes first",
     "sexta / é / feriado nacional → ___", instr="Sentence building", size=14.5, gap=0)
f.ex("B1", "Sentence building", "O Grêmio empatou por 1 a 1.", "Subject + verb + manner",
     "o grêmio / empatou / por 1 a 1 → ___", instr="Sentence building", size=14.5, gap=0)
f.ex("B1", "Sentence building", "Quando sair o gabarito, confira as respostas.", "time clause + main clause",
     "quando / sair / o gabarito / confira / as respostas → ___", instr="Sentence building", size=14.5, gap=0)
f.ex("B1", "Sentence building", "O Brasil lembra Zumbi em 20 de novembro.", "Subject + verb + object + time",
     "o brasil / lembra / zumbi / em 20 de novembro → ___", instr="Sentence building", size=14.5, gap=0)
f.head("E　TRADUZA", 22, OLIVE, 5)
f.ex("A2", "Translation", "Friday 20 November is a national holiday.", "See the page 1 headline",
     "Sexta, 20 de novembro, é feriado nacional. → ___", instr="Translation", size=14.5, gap=0)
f.ex("B1", "Translation", "Palmeiras won 5–4 in the shoot-out.", "nos pênaltis = in the shoot-out",
     "O Palmeiras venceu nos pênaltis por 5 a 4. → ___", instr="Translation", size=14.5, gap=0)
f.ex("B1", "Translation", "O gabarito oficial sai até o fim de novembro.", "oficial = official",
     "“The official answer key comes out by the end of November.” → ___", instr="Translation", size=14.5, gap=0)
f.ex("B2", "Translation", "Anote as suas respostas e confira quando sair o gabarito oficial.", "imperative anote/confira + quando clause",
     "“Write down your answers and check them when the official key comes out.” → ___", instr="Translation", size=14.5, gap=0)
f.head("F　AS PALAVRAS DA SEMANA", 22, OLIVE, 5)
f.match_set("B2", "Vocabulary matching",
            ["a consciência", "o gabarito", "o feriadão", "o agregado"],
            ["o placar dos dois jogos somados",
             "um fim de semana de três dias com feriado",
             "o saber e a memória de uma história",
             "as respostas oficiais das questões objetivas"],
            ["c", "d", "b", "a"],
            ["consciência=knowing and remembering c", "gabarito=the official answers to the multiple-choice questions d", "feriadão=a three-day weekend with a holiday b", "agregado=the aggregate score over two legs a"],
            instr="Match the pairs")
f.head("G　DIÁLOGO NA BILHETERIA", 22, OLIVE, 5)
f.ex("B1", "Cloze", "A", "The Mané Garrincha stadium",
     "— O jogo é no ___ Garrincha. (A. Mané · B. Maracanã)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "Grêmio chase a sixth title",
     "— O Grêmio busca o ___ título. (A. sexto · B. primeiro)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "Palmeiras chase a fifth title",
     "— E o Palmeiras busca o ___ . (A. quinto · B. décimo)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "Tickets are sold online",
     "— Os ingressos estão à venda ___ internet. (A. na · B. no)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "obrigado = thank you",
     "— Boa final! — Muito ___! (A. obrigado · B. tarde)", size=14.5, gap=0)
f.head("H　ESCREVA VOCÊ", 22, OLIVE, 5)
MODELO = ("Sexta, 20 de novembro, acordo sem despertador: é feriado nacional. "
          "De manhã, leio sobre Zumbi e Palmares e escrevo duas frases em português. "
          "À tarde, vou a uma roda de capoeira no bairro e ouço histórias de resistência. "
          "No sábado, assisto a Palmeiras × Flamengo na televisão, com a família. "
          "No domingo, descanso, preparo a semana e confiro o gabarito extraoficial do Enem. "
          "Na segunda, volto ao trabalho com calma: o feriadão foi curto, mas a memória fica. "
          "O dia 20 lembra a luta e a cultura afro-brasileiras.")
NWORDS = len(MODELO.split())
f.bridge(f"Writing task (no single correct answer); the model text ({NWORDS} words) is below.")
f.ex("B1", "Writing", "(open task — model text below)", f"See the model text in section H of this page ({NWORDS} words)",
     "«O seu feriadão de 20 a 22 de novembro» Escreva 80–100 palavras: o que você faz na sexta, no sábado e no domingo, e o que a data de 20 de novembro lembra.", instr="Writing", size=14.5, gap=0)
f.para("Texto modelo: " + MODELO, 15, lh=1.3, split=False, max_w=395)  # fix1 D7 (2026-11-11): wrap at 395, not the full 422.5 column — Cairo renders Newsreader ~3% wider than PIL measures, so two lines crossed the column edge 1862 (+2/+14px). Words, size (15) and 88-word count unchanged; worst line PIL 387.0, predicted rendered ink right ~1841.
f.end_report()
print("P8 exercises end y:", f.y, "col:", f.ci)

# ---- P8 image: the final stadium (col 3, below the exercises flow) ----
# The exercise flow fills cols 0-2 to the bottom; only its last column has
# free space below f.y, so the image goes there, positioned dynamically.
iy8 = (f.y + 12) if f.ci == 3 else 190
img_h = min(250, 1150 - iy8)
assert img_h >= 150, f"P8 image has no room: f.y={f.y} ci={f.ci}"
image(p, "garrincha.jpg", COLX[3], iy8, CW, img_h)
cap_end = caption(p, COLX[3], iy8 + img_h, CW,
        "O estádio Mané Garrincha, em Brasília: a final é no dia 6 de dezembro.",
        "Foto: Luis Dantas — Domínio público")
print("P8 image ends ~", cap_end)

# ================= RESPOSTAS =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "RESPOSTAS　Answer key — grouped by page; find your number", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "One short note per answer　✓ marks the writing model", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Writing":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13, lh=1.12, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-avaliacao.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("model words:", NWORDS)
