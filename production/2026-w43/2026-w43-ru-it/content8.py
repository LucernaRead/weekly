# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · ТЕСТ И ОТВЕТЫ =================
CURPAGE[0] = 8
p = BSPage4()
p.band("ТЕСТ И ОТВЕТЫ　Test e risposte", "Lucerna", "PAGINA 8　Большой тест недели + все ответы")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　ХРОНИКА НЕДЕЛИ", 21, OLIVE, 5)
f.ex("B1", "Cloze", "A", "Prima neve: dal 21 al 23",
     "Первый снег в Москве ждут 21–23 ___. (A. октября · B. ноября)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "Le vacanze iniziano il 24 ottobre",
     "Каникулы начинаются в субботу ___ октября. (A. 24 · B. 26)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "La Festa del Liceale è il 19 ottobre",
     "День лицеиста — ___ октября. (A. 19 · B. 18)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "Quattro fiabe",
     "В четверг в кино выходят ___ сказки. (A. три · B. четыре)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "Il derby è domenica",
     "Дерби ЦСКА — «Спартак» будет в ___. (A. воскресенье · B. пятницу)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "Il biglietto costa 900 rubli",
     "Билет на UNDR Halloween стоит ___ рублей. (A. 900 · B. 500)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "La Giornata dell'Unità Nazionale è il 4 novembre",
     "4 ноября — День народного ___. (A. единства · B. отца)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "Le gomme si cambiano a +5…+7 gradi",
     "Резину меняют при температуре плюс пять — ___ градусов. (A. семь · B. десять)", size=13.8, gap=0)
f.head("B　ОБЩИЕ ВОПРОСЫ", 21, OLIVE, 5)
f.ex("A2", "Scelta multipla", "A", "La Festa del Papà è stata il 18 ottobre",
     "Когда был День отца? A. 18 октября · B. 19 октября · C. 28 октября", size=13.8, gap=0)
f.ex("A2", "Scelta multipla", "B", "Aprì nel 1811, 215 anni fa",
     "Сколько лет назад открылся лицей? A. 200 · B. 215 · C. 100", size=13.8, gap=0)
f.ex("A2", "Scelta multipla", "C", "Lo Zenit ha 24 punti",
     "У какой команды 24 очка? A. «Динамо» · B. «Спартак» · C. «Зенит»", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "A", "La 12ª giornata inizia venerdì",
     "Когда начинается 12-й тур? A. в пятницу, 23 октября · B. в воскресенье · C. в понедельник", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "A", "Il concorso dura dal 1° ottobre",
     "Конкурс костюмов в Reels идёт с... A. 1 октября · B. 22 октября · C. 31 октября", size=13.8, gap=0)
f.ex("A2", "Scelta multipla", "B", "La Festa dei Nonni è il 28 ottobre",
     "Когда День бабушек и дедушек? A. 25 октября · B. 28 октября · C. 4 ноября", size=13.8, gap=0)
f.ex("B2", "Scelta multipla", "A", "Le vacanze raccomandate finiscono il 3 novembre",
     "Каникулы по рекомендации министерства заканчиваются... A. 3 ноября · B. 4 ноября · C. 26 октября", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "B", "Chiudono la stagione della dacia",
     "Что делают дачники в конце октября? A. открывают сезон · B. закрывают дачный сезон · C. покупают дачу", size=13.8, gap=0)
f.head("C　ЧИТАЙТЕ И ОТВЕЧАЙТЕ", 21, OLIVE, 5)
f.para("Антон учится в школе в Москве. На этой неделе он каждый день смотрит прогноз погоды: он очень ждёт первый снег. В пятницу у Антона последний учебный день, а в субботу начинаются каникулы. В воскресенье он будет смотреть дерби с папой: они болеют за «Спартак». А в четверг Антон пойдёт с классом в кино — на новую сказку.", 15, lh=1.3, split=False)
f.ex("A2", "Scelta multipla", "B", "Antón guarda le previsioni del tempo",
     "Что Антон смотрит каждый день? A. телевизор · B. прогноз погоды · C. таблицу", size=13.8, gap=0)
f.ex("A2", "Scelta multipla", "B", "L'ultimo giorno di scuola è venerdì",
     "Когда у Антона последний учебный день? A. в четверг · B. в пятницу · C. в субботу", size=13.8, gap=0)
f.ex("A2", "Scelta multipla", "C", "Tifano Spartak",
     "За кого болеют Антон и его папа? A. за ЦСКА · B. за «Динамо» · C. за «Спартак»", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "A", "Giovedì va al cinema",
     "Куда Антон пойдёт в четверг? A. в кино · B. на дачу · C. на футбол", size=13.8, gap=0)
f.head("D　СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 21, OLIVE, 5)
f.ex("A2", "Frasi", "Первый снег может выпасть на этой неделе.", "Soggetto + gruppo verbale + tempo",
     "первый снег / может выпасть / на этой неделе → ___", instr="Forma la frase", size=13.8, gap=0)
f.ex("A2", "Frasi", "Мы ждём первый снег.", "Soggetto + verbo + complemento",
     "мы / ждём / первый снег → ___", instr="Forma la frase", size=13.8, gap=0)
f.ex("B1", "Frasi", "В воскресенье будет главное дерби.", "Prima il tempo, il verbo al secondo posto",
     "в воскресенье / будет / главное дерби → ___", instr="Forma la frase", size=13.8, gap=0)
f.ex("B1", "Frasi", "Ученики отдыхают двенадцать дней.", "Soggetto + verbo + durata",
     "ученики / отдыхают / двенадцать дней → ___", instr="Forma la frase", size=13.8, gap=0)
f.head("E　ПЕРЕВЕДИТЕ", 21, OLIVE, 5)
f.ex("A2", "Traduzione", "Domenica il CSKA gioca contro lo Spartak.", "Confronta con pagina 4",
     "В воскресенье ЦСКА играет со «Спартаком». → ___", instr="Traduci in italiano", size=13.8, gap=0)
f.ex("B1", "Traduzione", "I meteorologi promettono nevischio per fine ottobre.", "мокрый снег = nevischio",
     "Синоптики обещают мокрый снег в конце октября. → ___", instr="Traduci in italiano", size=13.8, gap=0)
f.ex("B1", "Traduzione", "В субботу начинаются каникулы — всего двенадцать дней.", "Attenzione al caso: двенадцать дней",
     "Le vacanze iniziano sabato: dodici giorni in tutto. → ___", instr="Traduci in russo", size=13.8, gap=0)
f.ex("B2", "Traduzione", "Поздравляю папу с Днём отца!", "поздравляю + с + strumentale",
     "Faccio gli auguri a papà per la Festa del Papà! → ___", instr="Traduci in russo", size=13.8, gap=0)
f.head("F　СЛОВА НЕДЕЛИ", 21, OLIVE, 5)
f.match_set("B2", "Abbinamento",
            ["похолодает", "рекомендация", "единоличный лидер", "шиномонтаж"],
            ["место, где меняют резину на машине",
             "команда, которая одна на первом месте",
             "станет холодно",
             "совет, а не приказ"],
            ["c", "d", "b", "a"],
            ["farà più freddo c", "una raccomandazione d", "la capolista solitaria b", "il gommista a"],
            instr="Abbina")
f.head("G　ДИАЛОГ В КИНО", 21, OLIVE, 5)
f.ex("B1", "Cloze", "A", "два билета = due biglietti",
     "— Здравствуйте! Два ___ на «Морозко», пожалуйста. (A. билета · B. костюма)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "Il 22 è giovedì",
     "— На какой день? — На ___, 22 октября. (A. четверг · B. пятницу)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "È una fiaba",
     "— Хорошо. А фильм для детей? — Да, это ___. (A. сказка · B. дерби)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "до встречи = arrivederci",
     "— Спасибо! До ___ в четверг! (A. встречи · B. утра)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "хорошего просмотра = buona visione!",
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
f.expl(f"Prova di composizione (senza soluzione unica); il testo modello ({NWORDS} parole) segue qui sotto.")
f.ex("B1", "Composizione", "(Domanda aperta — testo modello qui sotto)", f"Il testo modello è nella sezione H di questa pagina ({NWORDS} parole)",
     "«Мои каникулы» Напишите 80–100 слов: когда начинаются ваши каникулы, что вы будете делать и куда поедете?", instr="Scrivi", size=13.8, gap=0)
f.para("Пример: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= ОТВЕТЫ =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "ОТВЕТЫ　Risposte — in ordine di pagina: cerca il tuo numero", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Ogni risposta ha una breve nota in italiano　✓ = esercizio con testo modello", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— СТРАНИЦА {pg} —", 13.3, "sans", True, OLIVE, lh=1.13, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Composizione":
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
