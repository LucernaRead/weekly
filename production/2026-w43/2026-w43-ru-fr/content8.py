# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-ru-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · ТЕСТ И ОТВЕТЫ =================
CURPAGE[0] = 8
p = BSPage4()
p.band("ТЕСТ И ОТВЕТЫ · Test et réponses", "Lucerna", "PAGE 8 · Большой тест недели + все ответы")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · ХРОНИКА НЕДЕЛИ", 21, OLIVE, 5)
f.ex("B1", "Cloze", "A", "La première neige : du 21 au 23",
     "Первый снег в Москве ждут 21–23 ___. (A. октября · B. ноября)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "Les vacances commencent le 24 octobre",
     "Каникулы начинаются в субботу ___ октября. (A. 24 · B. 26)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "La journée du lycéen est le 19 octobre",
     "День лицеиста — ___ октября. (A. 19 · B. 18)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "Quatre contes",
     "В четверг в кино выходят ___ сказки. (A. три · B. четыре)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "Le derby a lieu dimanche",
     "Дерби ЦСКА — «Спартак» будет в ___. (A. воскресенье · B. пятницу)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "Le billet coûte 900 roubles",
     "Билет на UNDR Halloween стоит ___ рублей. (A. 900 · B. 500)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "La Journée de l'unité nationale est le 4 novembre",
     "4 ноября — День народного ___. (A. единства · B. отца)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "On change les pneus à +5…+7 degrés",
     "Резину меняют при температуре плюс пять — ___ градусов. (A. семь · B. десять)", size=13.8, gap=0)
f.head("B · ОБЩИЕ ВОПРОСЫ", 21, OLIVE, 5)
f.ex("A2", "Choix", "A", "La fête des pères était le 18 octobre",
     "Когда был День отца? A. 18 октября · B. 19 октября · C. 28 октября", size=13.8, gap=0)
f.ex("A2", "Choix", "B", "Ouvert en 1811, il y a 215 ans",
     "Сколько лет назад открылся лицей? A. 200 · B. 215 · C. 100", size=13.8, gap=0)
f.ex("A2", "Choix", "C", "Le Zénith a 24 points",
     "У какой команды 24 очка? A. «Динамо» · B. «Спартак» · C. «Зенит»", size=13.8, gap=0)
f.ex("B1", "Choix", "A", "La 12e journée commence vendredi",
     "Когда начинается 12-й тур? A. в пятницу, 23 октября · B. в воскресенье · C. в понедельник", size=13.8, gap=0)
f.ex("B1", "Choix", "A", "Le concours court depuis le 1er octobre",
     "Конкурс костюмов в Reels идёт с... A. 1 октября · B. 22 октября · C. 31 октября", size=13.8, gap=0)
f.ex("A2", "Choix", "B", "La journée des grands-parents est le 28 octobre",
     "Когда День бабушек и дедушек? A. 25 октября · B. 28 октября · C. 4 ноября", size=13.8, gap=0)
f.ex("B2", "Choix", "A", "Les vacances recommandées finissent le 3 novembre",
     "Каникулы по рекомендации министерства заканчиваются... A. 3 ноября · B. 4 ноября · C. 26 октября", size=13.8, gap=0)
f.ex("B1", "Choix", "B", "Ils clôturent la saison à la datcha",
     "Что делают дачники в конце октября? A. открывают сезон · B. закрывают дачный сезон · C. покупают дачу", size=13.8, gap=0)
f.head("C · ЧИТАЙТЕ И ОТВЕЧАЙТЕ", 21, OLIVE, 5)
f.para("Антон учится в школе в Москве. На этой неделе он каждый день смотрит прогноз погоды: он очень ждёт первый снег. В пятницу у Антона последний учебный день, а в субботу начинаются каникулы. В воскресенье он будет смотреть дерби с папой: они болеют за «Спартак». А в четверг Антон пойдёт с классом в кино — на новую сказку.", 15, lh=1.3, split=False)
f.ex("A2", "Choix", "B", "Anton regarde les prévisions météo",
     "Что Антон смотрит каждый день? A. телевизор · B. прогноз погоды · C. таблицу", size=13.8, gap=0)
f.ex("A2", "Choix", "B", "Son dernier jour de classe est vendredi",
     "Когда у Антона последний учебный день? A. в четверг · B. в пятницу · C. в субботу", size=13.8, gap=0)
f.ex("A2", "Choix", "C", "Ils soutiennent le Spartak",
     "За кого болеют Антон и его папа? A. за ЦСКА · B. за «Динамо» · C. за «Спартак»", size=13.8, gap=0)
f.ex("B1", "Choix", "A", "Jeudi, il va au cinéma",
     "Куда Антон пойдёт в четверг? A. в кино · B. на дачу · C. на футбол", size=13.8, gap=0)
f.head("D · СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 21, OLIVE, 5)
f.ex("A2", "Phrases", "Первый снег может выпасть на этой неделе.", "Sujet + groupe verbal + moment",
     "первый снег / может выпасть / на этой неделе → ___", instr="Former la phrase", size=13.8, gap=0)
f.ex("A2", "Phrases", "Мы ждём первый снег.", "Sujet + verbe + objet",
     "мы / ждём / первый снег → ___", instr="Former la phrase", size=13.8, gap=0)
f.ex("B1", "Phrases", "В воскресенье будет главное дерби.", "Le moment d'abord, le verbe en deuxième position",
     "в воскресенье / будет / главное дерби → ___", instr="Former la phrase", size=13.8, gap=0)
f.ex("B1", "Phrases", "Ученики отдыхают двенадцать дней.", "Sujet + verbe + durée",
     "ученики / отдыхают / двенадцать дней → ___", instr="Former la phrase", size=13.8, gap=0)
f.head("E · ПЕРЕВЕДИТЕ", 21, OLIVE, 5)
f.ex("A2", "Traduction", "Le dimanche, le CSKA joue contre le Spartak.", "Comparez page 4",
     "В воскресенье ЦСКА играет со «Спартаком». → ___", instr="Traduire en français", size=13.8, gap=0)
f.ex("B1", "Traduction", "Les services météo promettent de la neige fondante pour la fin octobre.", "мокрый снег = la neige fondante",
     "Синоптики обещают мокрый снег в конце октября. → ___", instr="Traduire en français", size=13.8, gap=0)
f.ex("B1", "Traduction", "В субботу начинаются каникулы — всего двенадцать дней.", "Attention au cas : двенадцать дней",
     "Les vacances commencent samedi — douze jours en tout. → ___", instr="Traduire en russe", size=13.8, gap=0)
f.ex("B2", "Traduction", "Поздравляю папу с Днём отца!", "поздравляю + с + instrumental",
     "Je souhaite à mon papa une bonne fête des pères ! → ___", instr="Traduire en russe", size=13.8, gap=0)
f.head("F · СЛОВА НЕДЕЛИ", 21, OLIVE, 5)
f.match_set("B2", "Appariement",
            ["похолодает", "рекомендация", "единоличный лидер", "шиномонтаж"],
            ["место, где меняют резину на машине",
             "команда, которая одна на первом месте",
             "станет холодно",
             "совет, а не приказ"],
            ["c", "d", "b", "a"],
            ["il fera froid c", "une recommandation d", "le seul leader b", "le montage de pneus a"],
            instr="Associer")
f.head("G · ДИАЛОГ В КИНО", 21, OLIVE, 5)
f.ex("B1", "Cloze", "A", "два билета = deux billets",
     "— Здравствуйте! Два ___ на «Морозко», пожалуйста. (A. билета · B. костюма)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "Le 22 est un jeudi",
     "— На какой день? — На ___, 22 октября. (A. четверг · B. пятницу)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "C'est un conte de fées",
     "— Хорошо. А фильм для детей? — Да, это ___. (A. сказка · B. дерби)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "до встречи = à bientôt",
     "— Спасибо! До ___ в четверг! (A. встречи · B. утра)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "хорошего просмотра = bon film",
     "— До встречи! Хорошего ___! (A. фильма · B. просмотра)", size=13.8, gap=0)
f.head("H · НАПИШИТЕ САМИ", 21, OLIVE, 5)
MODELO = ("Мои каникулы начинаются в субботу, 24 октября, и длятся двенадцать дней. "
          "Сначала я буду спать долго и отдыхать дома. "
          "В воскресенье мы с папой будем смотреть дерби: ЦСКА играет со «Спартаком». "
          "В понедельник мы поедем к бабушке и дедушке в деревню: там уже холодно, и, может быть, будет первый снег. "
          "В среду, 28 октября, я поздравлю бабушку и дедушку с их праздником. "
          "А 31 октября я надену костюм и пойду на Хэллоуин с друзьями. "
          "Я очень жду эти дни! Вот такие каникулы!")
NWORDS = len(MODELO.split())
f.expl(f"Exercice d'écriture (sans solution unique) ; le texte modèle ({NWORDS} mots) est ci-dessous.")
f.ex("B1", "Rédaction", "(Question ouverte — texte modèle ci-dessous)", f"Le texte modèle se trouve dans la section H de cette page ({NWORDS} mots)",
     "«Мои каникулы» Напишите 80–100 слов: когда начинаются ваши каникулы, что вы будете делать и куда поедете?", instr="Écrire", size=13.8, gap=0)
f.para("Пример: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= ОТВЕТЫ =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "ОТВЕТЫ · Réponses — classées par page ; cherchez votre numéro", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Chaque réponse avec une courte note en français · ✓ = exercice à texte modèle", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— СТРАНИЦА {pg} —", 13.3, "sans", True, OLIVE, lh=1.13, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Rédaction":
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
