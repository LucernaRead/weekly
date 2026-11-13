# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · AVALIAÇÃO E RESPOSTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("AVALIAÇÃO E RESPOSTAS　Тест и ответы", "A Lucerna", "СТРАНИЦА 8　Большой тест недели + все ответы")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETE A CRÔNICA", 22, OLIVE, 5)
f.ex("B1", "Выбери один ответ", "A", "Пятница, 20 ноября, — национальный праздник",
     "Sexta, 20 de novembro, é ___ no Brasil. (A. feriado nacional · B. dia útil)", size=14.5, gap=0)
f.ex("B1", "Выбери один ответ", "A", "Праздник чтит память Зумби дос Палмареса",
     "O feriado lembra a morte de ___ . (A. Zumbi dos Palmares · B. Deodoro da Fonseca)", size=14.5, gap=0)
f.ex("B1", "Выбери один ответ", "B", "В 2026 году праздник выпадает на пятницу",
     "Em 2026, o feriado cai numa ___ . (A. segunda · B. sexta)", size=14.5, gap=0)
f.ex("B1", "Выбери один ответ", "A", "Финал Кубка Бразилии — 6 декабря",
     "A final da Copa do Brasil é no dia ___ de dezembro. (A. 6 · B. 15)", size=14.5, gap=0)
f.ex("B1", "Выбери один ответ", "B", "Финал: Гремио × Палмейрас",
     "Na final, jogam Grêmio e ___ . (A. Vasco · B. Palmeiras)", size=14.5, gap=0)
f.ex("B1", "Выбери один ответ", "A", "Официальные ответы — до конца ноября",
     "O gabarito oficial sai até o ___ de novembro. (A. fim · B. dia 8)", size=14.5, gap=0)
f.ex("B1", "Выбери один ответ", "A", "Второй день Enem — 15 ноября",
     "O segundo dia do Enem foi no domingo ___ . (A. 15 · B. 8)", size=14.5, gap=0)
f.ex("B1", "Выбери один ответ", "B", "Экзамен второго дня длится 5 часов",
     "No dia 15, a prova dura ___ horas. (A. três · B. cinco)", size=14.5, gap=0)
f.head("B　PERGUNTAS GERAIS", 22, OLIVE, 5)
f.ex("A2", "Выбери один ответ", "B", "Закон 2023 года: 20 ноября — национальный праздник",
     "A Lei nº 14.759, de 2023... A. criou o dia 20 · B. fez do dia 20 feriado nacional · C. acabou com o feriado", size=14.5, gap=0)
f.ex("B1", "Выбери один ответ", "A", "Гремио прошёл дальше 3–1 по сумме двух матчей",
     "O Grêmio passou à final com... A. 3 a 1 no total · B. 2 a 2 no total · C. 1 a 0 no total", size=14.5, gap=0)
f.ex("B1", "Выбери один ответ", "B", "Пенальти 5–4: Палмейрас идёт дальше",
     "Nos pênaltis, o Palmeiras venceu por... A. 4 a 3 · B. 5 a 4 · C. 6 a 5", size=14.5, gap=0)
f.ex("B1", "Выбери один ответ", "B", "Норрис выиграл Гран-при Сан-Паулу",
     "O Grande Prêmio de São Paulo foi vencido por... A. Verstappen · B. Norris · C. Hadjar", size=14.5, gap=0)
f.ex("B1", "Выбери один ответ", "A", "36-й тур: Палмейрас × Фламенго в субботу, 21-го",
     "A rodada 36 tem Palmeiras × Flamengo no... A. sábado 21 · B. domingo 22 · C. dia 15", size=14.5, gap=0)
f.ex("A2", "Выбери один ответ", "B", "Капоэйра — афробразильское искусство боя и музыки",
     "A capoeira é... A. um jogo de cartas · B. uma arte afro-brasileira de luta e música · C. um prato típico", size=14.5, gap=0)
f.ex("B2", "Выбери один ответ", "A", "10 это число рабочих дней до официальных ответов",
     "O número 10, na página 6, mede... A. os dias úteis até o gabarito · B. os gols da final · C. os feriados", size=14.5, gap=0)
f.ex("B1", "Выбери один ответ", "A", "Палмарес был в Алагоасе",
     "O Quilombo dos Palmares ficava... A. em Alagoas · B. no Rio · C. em São Paulo", size=14.5, gap=0)
f.head("C　LEIA E RESPONDA", 22, OLIVE, 5)
f.para("Rafael mora em Salvador. Na sexta, 20, ele não trabalha: é feriado nacional. De manhã, ele vai a uma roda de capoeira no Pelourinho. À tarde, ele lê sobre Zumbi e Palmares e escreve duas frases em português. No sábado, 21, ele assiste a Palmeiras × Flamengo na televisão. No domingo, 22, ele descansa e prepara a semana: na segunda, ele volta ao trabalho e confere o gabarito extraoficial do Enem.", 15.5, lh=1.3, split=False)
f.ex("A2", "Выбери один ответ", "B", "Рафаэл живёт в Салвадоре",
     "Onde mora Rafael? A. no Rio · B. em Salvador · C. em Brasília", size=14.5, gap=0)
f.ex("A2", "Выбери один ответ", "B", "В пятницу он идёт на роду капоэйры",
     "Na sexta, 20, Rafael... A. trabalha · B. vai a uma roda de capoeira · C. faz o Enem", size=14.5, gap=0)
f.ex("A2", "Выбери один ответ", "A", "В субботу он смотрит Палмейрас × Фламенго",
     "No sábado, 21, Rafael assiste... A. a Palmeiras × Flamengo · B. ao Enem · C. a uma aula", size=14.5, gap=0)
f.ex("A2", "Выбери один ответ", "B", "В понедельник он сверяет неофициальные ответы",
     "Na segunda, Rafael confere... A. o gabarito oficial · B. o gabarito extraoficial · C. a nota final", size=14.5, gap=0)
f.head("D　CONSTRUA AS FRASES", 22, OLIVE, 5)
f.ex("A2", "Составление предложений", "Sexta é feriado nacional.", "Слово времени стоит первым",
     "sexta / é / feriado nacional → ___", instr="Составление предложений", size=14.5, gap=0)
f.ex("B1", "Составление предложений", "O Grêmio empatou por 1 a 1.", "Подлежащее + глагол + способ",
     "o grêmio / empatou / por 1 a 1 → ___", instr="Составление предложений", size=14.5, gap=0)
f.ex("B1", "Составление предложений", "Quando sair o gabarito, confira as respostas.", "придаточное времени + главное предложение",
     "quando / sair / o gabarito / confira / as respostas → ___", instr="Составление предложений", size=14.5, gap=0)
f.ex("B1", "Составление предложений", "O Brasil lembra Zumbi em 20 de novembro.", "Подлежащее + глагол + дополнение + время",
     "o brasil / lembra / zumbi / em 20 de novembro → ___", instr="Составление предложений", size=14.5, gap=0)
f.head("E　TRADUZA", 22, OLIVE, 5)
f.ex("A2", "Перевод", "Пятница, 20 ноября, — национальный праздник.", "Смотри заголовок на странице 1",
     "Sexta, 20 de novembro, é feriado nacional. → ___", instr="Перевод", size=14.5, gap=0)
f.ex("B1", "Перевод", "Палмейрас выиграл 5–4 по пенальти.", "nos pênaltis = в серии пенальти",
     "O Palmeiras venceu nos pênaltis por 5 a 4. → ___", instr="Перевод", size=14.5, gap=0)
f.ex("B1", "Перевод", "O gabarito oficial sai até o fim de novembro.", "oficial = официальный",
     "“Официальные ответы будут опубликованы до конца ноября.” → ___", instr="Перевод", size=14.5, gap=0)
f.ex("B2", "Перевод", "Anote as suas respostas e confira quando sair o gabarito oficial.", "повелительное наклонение + quando-придаточное",
     "“Запиши свои ответы и сверь их, когда выйдут официальные.” → ___", instr="Перевод", size=14.5, gap=0)
f.head("F　AS PALAVRAS DA SEMANA", 22, OLIVE, 5)
f.match_set("B2", "Соедините слова",
            ["a consciência", "o gabarito", "o feriadão", "o agregado"],
            ["o placar dos dois jogos somados",
             "um fim de semana de três dias com feriado",
             "o saber e a memória de uma história",
             "as respostas oficiais das questões objetivas"],
            ["c", "d", "b", "a"],
            ["consciência=знать и помнить c", "gabarito=официальные ответы на вопросы с выбором d", "feriadão=трёхдневные выходные с праздником b", "agregado=общий счёт двух матчей a"],
            instr="Соедините")
f.head("G　DIÁLOGO NA BILHETERIA", 22, OLIVE, 5)
f.ex("B1", "Выбери один ответ", "A", "Стадион Мане Гарринча",
     "— O jogo é no ___ Garrincha. (A. Mané · B. Maracanã)", size=14.5, gap=0)
f.ex("B1", "Выбери один ответ", "A", "Гремио идёт за шестым титулом",
     "— O Grêmio busca o ___ título. (A. sexto · B. primeiro)", size=14.5, gap=0)
f.ex("B1", "Выбери один ответ", "A", "Палмейрас идёт за пятым титулом",
     "— E o Palmeiras busca o ___ . (A. quinto · B. décimo)", size=14.5, gap=0)
f.ex("B1", "Выбери один ответ", "A", "Билеты продаются онлайн",
     "— Os ingressos estão à venda ___ internet. (A. na · B. no)", size=14.5, gap=0)
f.ex("B1", "Выбери один ответ", "A", "obrigado = спасибо",
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
f.bridge(f"Письменное задание; образец текста ({NWORDS} слов) — ниже.")
f.ex("B1", "Письмо", "(открытое задание — образец ниже)", f"Смотри образец текста в разделе H ({NWORDS} слов)",
     "«O seu feriadão de 20 a 22 de novembro» Escreva 80–100 palavras: o que você faz na sexta, no sábado e no domingo, e o que a data de 20 de novembro lembra.", instr="Письмо", size=14.5, gap=0)
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
p.text(MX, 1302, "RESPOSTAS　Ответы — по страницам; найди свой номер", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Краткое пояснение к каждому ответу　✓ — образец письма", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Письмо":
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
