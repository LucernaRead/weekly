# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · ТЕСТ И ОТВЕТЫ =================
CURPAGE[0] = 8
p = BSPage4()
p.band("ТЕСТ И ОТВЕТЫ　Test en antwoorden", "Lucerna", "PAGINA 8　Большой тест недели + все ответы")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　ХРОНИКА НЕДЕЛИ", 21, OLIVE, 5)
f.ex("B1", "Cloze-meerkeuze", "A", "Eerste sneeuw: 21–23 oktober",
     "Первый снег в Москве ждут 21–23 ___. (A. октября · B. ноября)", size=13.8, gap=0)
f.ex("B1", "Cloze-meerkeuze", "A", "De vakantie begint op 24 oktober",
     "Каникулы начинаются в субботу ___ октября. (A. 24 · B. 26)", size=13.8, gap=0)
f.ex("B1", "Cloze-meerkeuze", "A", "Lyceumdag: 19 oktober",
     "День лицеиста — ___ октября. (A. 19 · B. 18)", size=13.8, gap=0)
f.ex("B1", "Cloze-meerkeuze", "B", "Vier sprookjesfilms",
     "В четверг в кино выходят ___ сказки. (A. три · B. четыре)", size=13.8, gap=0)
f.ex("B1", "Cloze-meerkeuze", "A", "De derby is op zondag",
     "Дерби ЦСКА — «Спартак» будет в ___. (A. воскресенье · B. пятницу)", size=13.8, gap=0)
f.ex("B1", "Cloze-meerkeuze", "A", "Het kaartje kost 900 roebel",
     "Билет на UNDR Halloween стоит ___ рублей. (A. 900 · B. 500)", size=13.8, gap=0)
f.ex("B1", "Cloze-meerkeuze", "A", "Dag van de Nationale Eenheid: 4 november",
     "4 ноября — День народного ___. (A. единства · B. отца)", size=13.8, gap=0)
f.ex("B1", "Cloze-meerkeuze", "A", "Banden wisselen bij +5…+7 graden",
     "Резину меняют при температуре плюс пять — ___ градусов. (A. семь · B. десять)", size=13.8, gap=0)
f.head("B　ОБЩИЕ ВОПРОСЫ", 21, OLIVE, 5)
f.ex("A2", "Meerkeuze", "A", "Vaderdag: 18 oktober",
     "Когда был День отца? A. 18 октября · B. 19 октября · C. 28 октября", size=13.8, gap=0)
f.ex("A2", "Meerkeuze", "B", "Geopend in 1811, 215 jaar geleden",
     "Сколько лет назад открылся лицей? A. 200 · B. 215 · C. 100", size=13.8, gap=0)
f.ex("A2", "Meerkeuze", "C", "«Зенит» heeft 24 punten",
     "У какой команды 24 очка? A. «Динамо» · B. «Спартак» · C. «Зенит»", size=13.8, gap=0)
f.ex("B1", "Meerkeuze", "A", "Speelronde 12 begint op vrijdag",
     "Когда начинается 12-й тур? A. в пятницу, 23 октября · B. в воскресенье · C. в понедельник", size=13.8, gap=0)
f.ex("B1", "Meerkeuze", "A", "De wedstrijd loopt sinds 1 oktober",
     "Конкурс костюмов в Reels идёт с... A. 1 октября · B. 22 октября · C. 31 октября", size=13.8, gap=0)
f.ex("A2", "Meerkeuze", "B", "Grootouderdag: 28 oktober",
     "Когда День бабушек и дедушек? A. 25 октября · B. 28 октября · C. 4 ноября", size=13.8, gap=0)
f.ex("B2", "Meerkeuze", "A", "De aanbevolen vakantie loopt tot 3 november",
     "Каникулы по рекомендации министерства заканчиваются... A. 3 ноября · B. 4 ноября · C. 26 октября", size=13.8, gap=0)
f.ex("B1", "Meerkeuze", "B", "Ze sluiten het datsjaseizoen",
     "Что делают дачники в конце октября? A. открывают сезон · B. закрывают дачный сезон · C. покупают дачу", size=13.8, gap=0)
f.head("C　ЧИТАЙТЕ И ОТВЕЧАЙТЕ", 21, OLIVE, 5)
f.para("Антон учится в школе в Москве. На этой неделе он каждый день смотрит прогноз погоды: он очень ждёт первый снег. В пятницу у Антона последний учебный день, а в субботу начинаются каникулы. В воскресенье он будет смотреть дерби с папой: они болеют за «Спартак». А в четверг Антон пойдёт с классом в кино — на новую сказку.", 15, lh=1.3, split=False)
f.ex("A2", "Meerkeuze", "B", "Anton kijkt naar het weerbericht",
     "Что Антон смотрит каждый день? A. телевизор · B. прогноз погоды · C. таблицу", size=13.8, gap=0)
f.ex("A2", "Meerkeuze", "B", "Laatste schooldag op vrijdag",
     "Когда у Антона последний учебный день? A. в четверг · B. в пятницу · C. в субботу", size=13.8, gap=0)
f.ex("A2", "Meerkeuze", "C", "Zij zijn voor «Спартак»",
     "За кого болеют Антон и его папа? A. за ЦСКА · B. за «Динамо» · C. за «Спартак»", size=13.8, gap=0)
f.ex("B1", "Meerkeuze", "A", "Op donderdag naar de bioscoop",
     "Куда Антон пойдёт в четверг? A. в кино · B. на дачу · C. на футбол", size=13.8, gap=0)
f.head("D　СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 21, OLIVE, 5)
f.ex("A2", "Zinnen bouwen", "Первый снег может выпасть на этой неделе.", "onderwerp + werkwoordsgroep + tijd",
     "первый снег / может выпасть / на этой неделе → ___", instr="Vorm de zin", size=13.8, gap=0)
f.ex("A2", "Zinnen bouwen", "Мы ждём первый снег.", "onderwerp + werkwoord + lijdend voorwerp",
     "мы / ждём / первый снег → ___", instr="Vorm de zin", size=13.8, gap=0)
f.ex("B1", "Zinnen bouwen", "В воскресенье будет главное дерби.", "tijd vooraan, werkwoord tweede",
     "в воскресенье / будет / главное дерби → ___", instr="Vorm de zin", size=13.8, gap=0)
f.ex("B1", "Zinnen bouwen", "Ученики отдыхают двенадцать дней.", "onderwerp + werkwoord + duur",
     "ученики / отдыхают / двенадцать дней → ___", instr="Vorm de zin", size=13.8, gap=0)
f.head("E　ПЕРЕВЕДИТЕ", 21, OLIVE, 5)
f.ex("A2", "Vertaling", "Op zondag speelt CSKA tegen «Спартак».", "Zie pagina 4",
     "В воскресенье ЦСКА играет со «Спартаком». → ___", instr="Vertaal naar het Nederlands", size=13.8, gap=0)
f.ex("B1", "Vertaling", "De meteorologen beloven natte sneeuw voor eind oktober.", "мокрый снег = natte sneeuw",
     "Синоптики обещают мокрый снег в конце октября. → ___", instr="Vertaal naar het Nederlands", size=13.8, gap=0)
f.ex("B1", "Vertaling", "В субботу начинаются каникулы — всего двенадцать дней.", "let op de naamval: двенадцать дней",
     "De vakantie begint op zaterdag — twaalf dagen in totaal. → ___", instr="Vertaal naar het Russisch", size=13.8, gap=0)
f.ex("B2", "Vertaling", "Поздравляю папу с Днём отца!", "поздравляю + с + instrumentalis",
     "Ik feliciteer papa met Vaderdag! → ___", instr="Vertaal naar het Russisch", size=13.8, gap=0)
f.head("F　СЛОВА НЕДЕЛИ", 21, OLIVE, 5)
f.match_set("B2", "Woorden koppelen",
            ["похолодает", "рекомендация", "единоличный лидер", "шиномонтаж"],
            ["место, где меняют резину на машине",
             "команда, которая одна на первом месте",
             "станет холодно",
             "совет, а не приказ"],
            ["c", "d", "b", "a"],
            ["het wordt koud c", "advies d", "alleen aan kop b", "bandenservice a"],
            instr="Combineer")
f.head("G　ДИАЛОГ В КИНО", 21, OLIVE, 5)
f.ex("B1", "Cloze-meerkeuze", "A", "два билета = twee kaartjes",
     "— Здравствуйте! Два ___ на «Морозко», пожалуйста. (A. билета · B. костюма)", size=13.8, gap=0)
f.ex("B1", "Cloze-meerkeuze", "A", "De 22e is een donderdag",
     "— На какой день? — На ___, 22 октября. (A. четверг · B. пятницу)", size=13.8, gap=0)
f.ex("B1", "Cloze-meerkeuze", "A", "Het is een sprookjesfilm",
     "— Хорошо. А фильм для детей? — Да, это ___. (A. сказка · B. дерби)", size=13.8, gap=0)
f.ex("B1", "Cloze-meerkeuze", "A", "до встречи = tot ziens",
     "— Спасибо! До ___ в четверг! (A. встречи · B. утра)", size=13.8, gap=0)
f.ex("B1", "Cloze-meerkeuze", "B", "хорошего просмотра = veel kijkplezier",
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
f.expl(f"Schrijfopgave (geen uniek antwoord); de voorbeeldtekst ({NWORDS} woorden) staat hieronder.")
f.ex("B1", "Schrijven", "(open vraag — de voorbeeldtekst staat hieronder)", f"De voorbeeldtekst staat in deel H van deze pagina ({NWORDS} woorden)",
     "«Мои каникулы» Напишите 80–100 слов: когда начинаются ваши каникулы, что вы будете делать и куда поедете?", instr="Schrijf", size=13.8, gap=0)
f.para("Пример: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= ОТВЕТЫ =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "ОТВЕТЫ　Antwoorden — per pagina gerangschikt: zoek je nummer", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Bij elk antwoord een korte uitleg in het Nederlands　✓ = opgave met voorbeeldtekst", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— Pagina {pg} —", 13.3, "sans", True, OLIVE, lh=1.13, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Schrijven":
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
