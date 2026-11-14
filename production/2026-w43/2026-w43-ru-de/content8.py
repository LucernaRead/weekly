# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · ТЕСТ И ОТВЕТЫ =================
CURPAGE[0] = 8
p = BSPage4()
p.band("ТЕСТ И ОТВЕТЫ　Test und Antworten", "Lucerna", "SEITE 8　Большой тест недели + все ответы")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　ХРОНИКА НЕДЕЛИ", 21, OLIVE, 5)
f.ex("B1", "Lückentext", "A", "Fenster für den ersten Schnee: 21.–23.",
     "Первый снег в Москве ждут 21–23 ___. (A. октября · B. ноября)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Die Ferien beginnen am 24. Oktober",
     "Каникулы начинаются в субботу ___ октября. (A. 24 · B. 26)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Lyzeumstag ist der 19. Oktober",
     "День лицеиста — ___ октября. (A. 19 · B. 18)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "B", "Vier Märchenfilme",
     "В четверг в кино выходят ___ сказки. (A. три · B. четыре)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Das Derby ist am Sonntag",
     "Дерби ЦСКА — «Спартак» будет в ___. (A. воскресенье · B. пятницу)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Die Karte kostet 900 Rubel",
     "Билет на UNDR Halloween стоит ___ рублей. (A. 900 · B. 500)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Tag der Einheit ist der 4. November",
     "4 ноября — День народного ___. (A. единства · B. отца)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Reifenwechsel bei +5…+7 Grad",
     "Резину меняют при температуре плюс пять — ___ градусов. (A. семь · B. десять)", size=13.8, gap=0)
f.head("B　ОБЩИЕ ВОПРОСЫ", 21, OLIVE, 5)
f.ex("A2", "Ankreuzen", "A", "Vatertag war am 18. Oktober",
     "Когда был День отца? A. 18 октября · B. 19 октября · C. 28 октября", size=13.8, gap=0)
f.ex("A2", "Ankreuzen", "B", "1811 eröffnet, vor 215 Jahren",
     "Сколько лет назад открылся лицей? A. 200 · B. 215 · C. 100", size=13.8, gap=0)
f.ex("A2", "Ankreuzen", "C", "Zenit hat 24 Punkte",
     "У какой команды 24 очка? A. «Динамо» · B. «Спартак» · C. «Зенит»", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "A", "Spieltag 12 beginnt am Freitag",
     "Когда начинается 12-й тур? A. в пятницу, 23 октября · B. в воскресенье · C. в понедельник", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "A", "Der Wettbewerb läuft seit dem 1. Oktober",
     "Конкурс костюмов в Reels идёт с... A. 1 октября · B. 22 октября · C. 31 октября", size=13.8, gap=0)
f.ex("A2", "Ankreuzen", "B", "Großelterntag ist am 28. Oktober",
     "Когда День бабушек и дедушек? A. 25 октября · B. 28 октября · C. 4 ноября", size=13.8, gap=0)
f.ex("B2", "Ankreuzen", "A", "Die empfohlenen Ferien enden am 3. November",
     "Каникулы по рекомендации министерства заканчиваются... A. 3 ноября · B. 4 ноября · C. 26 октября", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "B", "Sie beenden die Datscha-Saison",
     "Что делают дачники в конце октября? A. открывают сезон · B. закрывают дачный сезон · C. покупают дачу", size=13.8, gap=0)
f.head("C　ЧИТАЙТЕ И ОТВЕЧАЙТЕ", 21, OLIVE, 5)
f.para("Антон учится в школе в Москве. На этой неделе он каждый день смотрит прогноз погоды: он очень ждёт первый снег. В пятницу у Антона последний учебный день, а в субботу начинаются каникулы. В воскресенье он будет смотреть дерби с папой: они болеют за «Спартак». А в четверг Антон пойдёт с классом в кино — на новую сказку.", 15, lh=1.3, split=False)
f.ex("A2", "Ankreuzen", "B", "Anton schaut sich die Wetterprognose an",
     "Что Антон смотрит каждый день? A. телевизор · B. прогноз погоды · C. таблицу", size=13.8, gap=0)
f.ex("A2", "Ankreuzen", "B", "Sein letzter Schultag ist der Freitag",
     "Когда у Антона последний учебный день? A. в четверг · B. в пятницу · C. в субботу", size=13.8, gap=0)
f.ex("A2", "Ankreuzen", "C", "Sie halten zu Spartak",
     "За кого болеют Антон и его папа? A. за ЦСКА · B. за «Динамо» · C. за «Спартак»", size=13.8, gap=0)
f.ex("B1", "Ankreuzen", "A", "Am Donnerstag geht er ins Kino",
     "Куда Антон пойдёт в четверг? A. в кино · B. на дачу · C. на футбол", size=13.8, gap=0)
f.head("D　СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 21, OLIVE, 5)
f.ex("A2", "Sätze bilden", "Первый снег может выпасть на этой неделе.", "Subjekt + Verbgruppe + Zeit",
     "первый снег / может выпасть / на этой неделе → ___", instr="Sätze bilden", size=13.8, gap=0)
f.ex("A2", "Sätze bilden", "Мы ждём первый снег.", "Subjekt + Verb + Objekt",
     "мы / ждём / первый снег → ___", instr="Sätze bilden", size=13.8, gap=0)
f.ex("B1", "Sätze bilden", "В воскресенье будет главное дерби.", "Die Zeit steht vorn, das Verb an zweiter Stelle",
     "в воскресенье / будет / главное дерби → ___", instr="Sätze bilden", size=13.8, gap=0)
f.ex("B1", "Sätze bilden", "Ученики отдыхают двенадцать дней.", "Subjekt + Verb + Dauer",
     "ученики / отдыхают / двенадцать дней → ___", instr="Sätze bilden", size=13.8, gap=0)
f.head("E　ПЕРЕВЕДИТЕ", 21, OLIVE, 5)
f.ex("A2", "Übersetzen", "Am Sonntag spielt ZSKA gegen Spartak.", "Vergleichen Sie Seite 4",
     "В воскресенье ЦСКА играет со «Спартаком». → ___", instr="Ins Deutsche übersetzen", size=13.8, gap=0)
f.ex("B1", "Übersetzen", "Die Wetterdienste versprechen Schneeregen für Ende Oktober.", "мокрый снег = Schneeregen",
     "Синоптики обещают мокрый снег в конце октября. → ___", instr="Ins Deutsche übersetzen", size=13.8, gap=0)
f.ex("B1", "Übersetzen", "В субботу начинаются каникулы — всего двенадцать дней.", "Achten Sie auf den Kasus: двенадцать дней",
     "Die Ferien beginnen am Samstag — insgesamt zwölf Tage. → ___", instr="Ins Russische übersetzen", size=13.8, gap=0)
f.ex("B2", "Übersetzen", "Поздравляю папу с Днём отца!", "поздравляю + с + Instrumental",
     "Ich wünsche meinem Papa alles Gute zum Vatertag! → ___", instr="Ins Russische übersetzen", size=13.8, gap=0)
f.head("F　СЛОВА НЕДЕЛИ", 21, OLIVE, 5)
f.match_set("B2", "Zuordnen",
            ["похолодает", "рекомендация", "единоличный лидер", "шиномонтаж"],
            ["место, где меняют резину на машине",
             "команда, которая одна на первом месте",
             "станет холодно",
             "совет, а не приказ"],
            ["c", "d", "b", "a"],
            ["wird kalt c", "Empfehlung d", "alleiniger Tabellenführer b", "Reifenservice a"],
            instr="Paare zuordnen")
f.head("G　ДИАЛОГ В КИНО", 21, OLIVE, 5)
f.ex("B1", "Lückentext", "A", "два билета = zwei Karten",
     "— Здравствуйте! Два ___ на «Морозко», пожалуйста. (A. билета · B. костюма)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Der 22. ist ein Donnerstag",
     "— На какой день? — На ___, 22 октября. (A. четверг · B. пятницу)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Es ist ein Märchenfilm",
     "— Хорошо. А фильм для детей? — Да, это ___. (A. сказка · B. дерби)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "до встречи = bis bald",
     "— Спасибо! До ___ в четверг! (A. встречи · B. утра)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "B", "хорошего просмотра = viel Spaß beim Film",
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
f.note(f"Schreibaufgabe (ohne eindeutige Lösung); der Mustertext ({NWORDS} Wörter) steht unten.")
f.ex("B1", "Schreiben", "(offene Aufgabe — Mustertext unten)", f"Der Mustertext steht in Abschnitt H dieser Seite ({NWORDS} Wörter)",
     "«Мои каникулы» Напишите 80–100 слов: когда начинаются ваши каникулы, что вы будете делать и куда поедете?", instr="Schreiben", size=13.8, gap=0)
f.para("Пример: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= ОТВЕТЫ =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "ОТВЕТЫ　Antworten — nach Seiten geordnet; suchen Sie Ihre Nummer", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Jede Antwort mit einer kurzen deutschen Anmerkung　✓ = Mustertext-Aufgabe", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— СТРАНИЦА {pg} —", 13.3, "sans", True, OLIVE, lh=1.13, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Schreiben":
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
