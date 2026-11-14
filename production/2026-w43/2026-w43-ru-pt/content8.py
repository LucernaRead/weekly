# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · ТЕСТ И ОТВЕТЫ =================
CURPAGE[0] = 8
p = BSPage4()
p.band("ТЕСТ И ОТВЕТЫ　Teste e respostas", "Lucerna", "PÁGINA 8　Большой тест недели + все ответы")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　ХРОНИКА НЕДЕЛИ", 21, OLIVE, 5)
f.ex("B1", "Cloze", "A", "Primeira neve: de 21 a 23",
     "Первый снег в Москве ждут 21–23 ___. (A. октября · B. ноября)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "As férias começam em 24 de outubro",
     "Каникулы начинаются в субботу ___ октября. (A. 24 · B. 26)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "O Dia do Liceu é 19 de outubro",
     "День лицеиста — ___ октября. (A. 19 · B. 18)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "Quatro contos",
     "В четверг в кино выходят ___ сказки. (A. три · B. четыре)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "O dérbi é no domingo",
     "Дерби ЦСКА — «Спартак» будет в ___. (A. воскресенье · B. пятницу)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "O ingresso custa 900 rublos",
     "Билет на UNDR Halloween стоит ___ рублей. (A. 900 · B. 500)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "O Dia da Unidade é 4 de novembro",
     "4 ноября — День народного ___. (A. единства · B. отца)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "Os pneus se trocam a +5…+7 graus",
     "Резину меняют при температуре плюс пять — ___ градусов. (A. семь · B. десять)", size=13.8, gap=0)
f.head("B　ОБЩИЕ ВОПРОСЫ", 21, OLIVE, 5)
f.ex("A2", "Escolha múltipla", "A", "O Dia dos Pais foi em 18 de outubro",
     "Когда был День отца? A. 18 октября · B. 19 октября · C. 28 октября", size=13.8, gap=0)
f.ex("A2", "Escolha múltipla", "B", "Abriu em 1811, há 215 anos",
     "Сколько лет назад открылся лицей? A. 200 · B. 215 · C. 100", size=13.8, gap=0)
f.ex("A2", "Escolha múltipla", "C", "O «Зенит» tem 24 pontos",
     "У какой команды 24 очка? A. «Динамо» · B. «Спартак» · C. «Зенит»", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "A", "A 12.ª rodada começa na sexta",
     "Когда начинается 12-й тур? A. в пятницу, 23 октября · B. в воскресенье · C. в понедельник", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "A", "O concurso vai desde 1.º de outubro",
     "Конкурс костюмов в Reels идёт с... A. 1 октября · B. 22 октября · C. 31 октября", size=13.8, gap=0)
f.ex("A2", "Escolha múltipla", "B", "O Dia dos Avós é 28 de outubro",
     "Когда День бабушек и дедушек? A. 25 октября · B. 28 октября · C. 4 ноября", size=13.8, gap=0)
f.ex("B2", "Escolha múltipla", "A", "As férias recomendadas vão até 3 de novembro",
     "Каникулы по рекомендации министерства заканчиваются... A. 3 ноября · B. 4 ноября · C. 26 октября", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "B", "Encerram a temporada da dátcha",
     "Что делают дачники в конце октября? A. открывают сезон · B. закрывают дачный сезон · C. покупают дачу", size=13.8, gap=0)
f.head("C　ЧИТАЙТЕ И ОТВЕЧАЙТЕ", 21, OLIVE, 5)
f.para("Антон учится в школе в Москве. На этой неделе он каждый день смотрит прогноз погоды: он очень ждёт первый снег. В пятницу у Антона последний учебный день, а в субботу начинаются каникулы. В воскресенье он будет смотреть дерби с папой: они болеют за «Спартак». А в четверг Антон пойдёт с классом в кино — на новую сказку.", 15, lh=1.3, split=False)
f.ex("A2", "Escolha múltipla", "B", "Antón olha a previsão do tempo",
     "Что Антон смотрит каждый день? A. телевизор · B. прогноз погоды · C. таблицу", size=13.8, gap=0)
f.ex("A2", "Escolha múltipla", "B", "O último dia de aula é sexta",
     "Когда у Антона последний учебный день? A. в четверг · B. в пятницу · C. в субботу", size=13.8, gap=0)
f.ex("A2", "Escolha múltipla", "C", "Torcem pelo «Спартак»",
     "За кого болеют Антон и его папа? A. за ЦСКА · B. за «Динамо» · C. за «Спартак»", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "A", "Na quinta vai ao cinema",
     "Куда Антон пойдёт в четверг? A. в кино · B. на дачу · C. на футбол", size=13.8, gap=0)
f.head("D　СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 21, OLIVE, 5)
f.ex("A2", "Construção de frases", "Первый снег может выпасть на этой неделе.", "sujeito + grupo verbal + tempo",
     "первый снег / может выпасть / на этой неделе → ___", instr="Forme a frase", size=13.8, gap=0)
f.ex("A2", "Construção de frases", "Мы ждём первый снег.", "sujeito + verbo + objeto",
     "мы / ждём / первый снег → ___", instr="Forme a frase", size=13.8, gap=0)
f.ex("B1", "Construção de frases", "В воскресенье будет главное дерби.", "tempo na frente, verbo em segundo",
     "в воскресенье / будет / главное дерби → ___", instr="Forme a frase", size=13.8, gap=0)
f.ex("B1", "Construção de frases", "Ученики отдыхают двенадцать дней.", "sujeito + verbo + duração",
     "ученики / отдыхают / двенадцать дней → ___", instr="Forme a frase", size=13.8, gap=0)
f.head("E　ПЕРЕВЕДИТЕ", 21, OLIVE, 5)
f.ex("A2", "Tradução", "No domingo, o CSKA joga contra o Spartak.", "Ver a página 4",
     "В воскресенье ЦСКА играет со «Спартаком». → ___", instr="Traduza para o português", size=13.8, gap=0)
f.ex("B1", "Tradução", "Os meteorologistas prometem neve com chuva para o fim de outubro.", "мокрый снег = neve com chuva",
     "Синоптики обещают мокрый снег в конце октября. → ___", instr="Traduza para o português", size=13.8, gap=0)
f.ex("B1", "Tradução", "В субботу начинаются каникулы — всего двенадцать дней.", "atenção ao caso: двенадцать дней",
     "As férias começam no sábado: doze dias no total. → ___", instr="Traduza para o russo", size=13.8, gap=0)
f.ex("B2", "Tradução", "Поздравляю папу с Днём отца!", "поздравляю + с + instrumental",
     "Desejo ao papai um feliz Dia dos Pais! → ___", instr="Traduza para o russo", size=13.8, gap=0)
f.head("F　СЛОВА НЕДЕЛИ", 21, OLIVE, 5)
f.match_set("B2", "Associação de palavras",
            ["похолодает", "рекомендация", "единоличный лидер", "шиномонтаж"],
            ["место, где меняют резину на машине",
             "команда, которая одна на первом месте",
             "станет холодно",
             "совет, а не приказ"],
            ["c", "d", "b", "a"],
            ["vai esfriar c", "recomendação d", "líder isolado b", "borracharia a"],
            instr="Associe")
f.head("G　ДИАЛОГ В КИНО", 21, OLIVE, 5)
f.ex("B1", "Cloze", "A", "два билета = dois ingressos",
     "— Здравствуйте! Два ___ на «Морозко», пожалуйста. (A. билета · B. костюма)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "o dia 22 é quinta-feira",
     "— На какой день? — На ___, 22 октября. (A. четверг · B. пятницу)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "é um conto (filme infantil)",
     "— Хорошо. А фильм для детей? — Да, это ___. (A. сказка · B. дерби)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "до встречи = até logo",
     "— Спасибо! До ___ в четверг! (A. встречи · B. утра)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "хорошего просмотра = bom filme!",
     "— До встречи! Хорошего ___! (A. фильма · B. просмотра)", size=13.8, gap=0)
f.head("H　НАПИШИТЕ САМИ", 21, OLIVE, 5)
MODELO = ("Мои каникулы начинаются в субботу, 24 октября, и длятся двенадцать дней. "
          "Сначала я буду спать долго и отдыхать дома. "
          "В воскресенье мы с папой будем смотреть дерби: ЦСКА играет со «Спартаком». "
          "В понедельник мы поедем к бабушке и дедушке в деревню: там уже холодно, и, может быть, будет первый снег. "
          "В среду, 28 октября, я поздравлю бабушку и дедушку с их праздником. "
          "А 31 октября я надену костюм и пойду на Хэллоуин с друзьями. "
          "Я очень жду эти дни! Вот такие каникулы!")
NWORDS = len(MODELO.split())
f.expl(f"Exercício de escrita (sem resposta única); o texto modelo ({NWORDS} palavras) vem logo abaixo.")
f.ex("B1", "Escrita", "(pergunta aberta — texto modelo abaixo)", f"O texto modelo está na seção H desta página ({NWORDS} palavras)",
     "«Мои каникулы» Напишите 80–100 слов: когда начинаются ваши каникулы, что вы будете делать и куда поедете?", instr="Escreva", size=13.8, gap=0)
f.para("Пример: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= ОТВЕТЫ =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "ОТВЕТЫ　Respostas — por página: procure o seu número", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Cada resposta tem uma nota breve em português　✓ = exercício com texto modelo", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— СТРАНИЦА {pg} —", 13.3, "sans", True, OLIVE, lh=1.13, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Escrita":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.0, lh=1.13, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-test.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("by type", dict(Counter(e["type"] for e in REG)))
print("model words:", NWORDS)
