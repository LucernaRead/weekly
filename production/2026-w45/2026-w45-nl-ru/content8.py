# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-ru/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · TOETS EN ANTWOORDEN =================
CURPAGE[0] = 8
p = BSPage4()
p.band("TOETS EN ANTWOORDEN · ТЕСТ И ОТВЕТЫ", "De Lucerna", "Страница 8 · De grote toets van de week + alle antwoorden")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · VUL DE KRONIEK IN", 21, OLIVE, 5)
f.ex("B1", "Выбор в тексте", "B", "Неделя климата — до 8 ноября",
     "De Klimaatweek duurt van 2 tot en met ___ november. (A. 7 · B. 8)", size=13.8, gap=0)
f.ex("B1", "Выбор в тексте", "B", "Куворден раздаёт 200 деревьев и кустарников",
     "Coevorden deelt ___ bomen en struiken uit. (A. 100 · B. 200)", size=13.8, gap=0)
f.ex("B1", "Выбор в тексте", "B", "Ночь музеев — 7 ноября",
     "Museumnacht is op zaterdag ___ november. (A. 6 · B. 7)", size=13.8, gap=0)
f.ex("B1", "Выбор в тексте", "B", "Твенте — Аякс: начало в 13:30",
     "Twente – Ajax begint om ___ uur. (A. 11:15 · B. 13:30)", size=13.8, gap=0)
f.ex("B1", "Выбор в тексте", "A", "Аякс выиграл у Аталанты 2–0",
     "Ajax won van Atalanta met ___. (A. 2–0 · B. 4–1)", size=13.8, gap=0)
f.ex("B1", "Выбор в тексте", "A", "Робинсон начался в ноябре",
     "Expeditie Robinson begon op 1 ___. (A. november · B. oktober)", size=13.8, gap=0)
f.ex("B1", "Выбор в тексте", "B", "Код «оранжевый»: погода опасна",
     "Code oranje betekent: het weer is ___. (A. veilig · B. gevaarlijk)", size=13.8, gap=0)
f.ex("B1", "Выбор в тексте", "B", "meedoen — участвовать",
     "«Meedoen» betekent ___. (A. weggaan · B. deelnemen)", size=13.8, gap=0)
f.head("B · ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "Выбор ответа", "A", "Неделя климата началась в понедельник, 2 ноября",
     "De Klimaatweek begint op... A. maandag 2 november · B. dinsdag 3 november · C. zaterdag 7 november", size=13.8, gap=0)
f.ex("A2", "Выбор ответа", "B", "Место раздачи — Звелло",
     "De bomen in Coevorden worden uitgedeeld in... A. Amsterdam · B. Zweeloo · C. Rotterdam", size=13.8, gap=0)
f.ex("A2", "Выбор ответа", "B", "Crossing Border — в Гааге",
     "Crossing Border is in... A. Amsterdam · B. Den Haag · C. Utrecht", size=13.8, gap=0)
f.ex("B1", "Выбор ответа", "A", "PAN — в выставочном центре RAI",
     "PAN Amsterdam is in... A. de RAI · B. het Rijksmuseum · C. de Jaarbeurs", size=13.8, gap=0)
f.ex("B1", "Выбор ответа", "B", "Реал Бетис выиграл у Фейеноорда 1–0",
     "Real Betis – Feyenoord eindigde... A. 0–0 · B. 1–0 · C. 0–1", size=13.8, gap=0)
f.ex("B1", "Выбор ответа", "B", "После 10 туров у Аякса 21 очко",
     "Na 10 ronden heeft Ajax ___ punten. A. 24 · B. 21 · C. 20", size=13.8, gap=0)
f.ex("B2", "Выбор ответа", "B", "Усталость от предупреждений: слишком много предупреждений — меньше внимания",
     "Waarschuwingsmoeheid betekent... A. moe van het weer · B. minder opletten door te veel waarschuwingen · C. een nieuwe code", size=13.8, gap=0)
f.ex("B1", "Выбор ответа", "C", "На барахолке в Зандаме около 250 прилавков",
     "De Snuffelmarkt in Zaandam heeft zo'n ___ kramen. A. 70 · B. 200 · C. 250", size=13.8, gap=0)
f.head("C · LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Daan woont in Coevorden. Op zaterdag 7 november gaat hij naar de Fair Groen in Zweeloo en haalt hij een gratis struik op. 's Avonds kijkt hij naar de foto's van Museumnacht in Amsterdam — zelf gaat hij niet, want zondag speelt zijn club Twente tegen Ajax om 13:30 uur. En in de Klimaatweek fietst Daan elke dag naar school, ook als het regent.", 15, lh=1.3, split=False)
f.ex("A2", "Выбор ответа", "B", "Даан живёт в Кувордене",
     "Waar woont Daan? A. in Zweeloo · B. in Coevorden · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "Выбор ответа", "B", "В субботу он забрал бесплатный кустарник",
     "Wat haalt Daan op zaterdag op? A. een fiets · B. een gratis struik · C. een kaartje", size=13.8, gap=0)
f.ex("A2", "Выбор ответа", "B", "В воскресенье Твенте играет с Аяксом",
     "Waarom gaat Daan zaterdagavond niet naar Amsterdam? A. Hij heeft geen kaartje · B. Zondag speelt Twente tegen Ajax · C. Hij houdt niet van musea", size=13.8, gap=0)
f.ex("B1", "Выбор ответа", "B", "В Неделю климата он каждый день ездит в школу на велосипеде",
     "Wat doet Daan in de Klimaatweek? A. Hij rijdt elke dag met de auto · B. Hij fietst elke dag naar school · C. Hij blijft thuis", size=13.8, gap=0)
f.head("D · MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "Составление предложения", "De Klimaatweek begint op maandag.", "Подлежащее + глагол + время",
     "de klimaatweek / begint / op maandag → ___", instr="Составление предложения", size=13.8, gap=0)
f.ex("B1", "Составление предложения", "Wij planten een boom in de tuin.", "Подлежащее + глагол + дополнение + место",
     "wij / planten / een boom / in de tuin → ___", instr="Составление предложения", size=13.8, gap=0)
f.ex("B1", "Составление предложения", "Twente speelt zondag tegen Ajax.", "Подлежащее + глагол + время + соперник",
     "twente / speelt / zondag / tegen ajax → ___", instr="Составление предложения", size=13.8, gap=0)
f.ex("B1", "Составление предложения", "Ik doe mee aan de Klimaatweek.", "Отделяемая часть mee — в конце предложения",
     "ik / doe / mee / aan de klimaatweek → ___", instr="Составление предложения", size=13.8, gap=0)
f.head("E · VERTAAL", 21, OLIVE, 5)
f.ex("A2", "Перевод", "Неделя климата длится семь дней.", "См. заголовок на странице 1",
     "De Klimaatweek duurt zeven dagen. → ___", instr="Перевод", size=13.8, gap=0)
f.ex("B1", "Перевод", "Код «оранжевый» означает: приготовьтесь.", "Фраза со страницы 2 · bereid je voor — приготовьтесь",
     "Code oranje betekent: bereid je voor. → ___", instr="Перевод", size=13.8, gap=0)
f.ex("B1", "Перевод", "Museumnacht duurt van 19:00 uur tot 02:00 uur.", "Обратите внимание на конструкцию van...tot...",
     "Ночь музеев длится с 19:00 до 02:00. → ___", instr="Перевод", size=13.8, gap=0)
f.ex("B2", "Перевод", "Ik doe mee aan de Klimaatweek.", "meedoen — отделяемый глагол",
     "Я участвую в Неделе климата. → ___", instr="Перевод", size=13.8, gap=0)
f.head("F · WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "Сопоставление слов",
            ["het klimaat", "meedoen", "de waarschuwing", "vastzetten"],
            ["een bericht over gevaarlijk weer",
             "deelnemen, erbij zijn",
             "het weer en de natuur over een lange tijd",
             "losse spullen stevig maken"],
            ["c", "b", "a", "d"],
            ["klimaat — климат, c", "meedoen — участвовать, b", "waarschuwing — предупреждение, a", "vastzetten — закреплять, d"],
            instr="Сопоставьте пары слов")
f.head("G · DIALOOG BIJ DE BOMEN", 21, OLIVE, 5)
f.ex("B1", "Выбор в тексте", "A", "boom — дерево",
     "— Goedemiddag! Ik kom voor een ___. (A. boom · B. fiets)", size=13.8, gap=0)
f.ex("B1", "Выбор в тексте", "A", "struik — кустарник",
     "— Natuurlijk. Wilt u een boom of een ___? (A. struik · B. auto)", size=13.8, gap=0)
f.ex("B1", "Выбор в тексте", "A", "planten — сажать",
     "— Een struik, graag. En waar moet ik hem ___? (A. planten · B. kopen)", size=13.8, gap=0)
f.ex("B1", "Выбор в тексте", "B", "zachte — мягкая (почва)",
     "— In de tuin, in de ___ grond. (A. harde · B. zachte)", size=13.8, gap=0)
f.ex("B1", "Выбор в тексте", "A", "Раздача длится до 16:00",
     "— De uitdeling duurt tot ___ uur. (A. 16:00 · B. 20:00)", size=13.8, gap=0)
f.head("H · SCHRIJF ZELF", 21, OLIVE, 5)
MODELO = ("Maandag 2 november begint de Klimaatweek in Nederland. "
          "Ik doe mee: ik fiets elke dag naar school en ik zet de verwarming één graad lager. "
          "Op zaterdag 7 november ga ik met mijn vader naar Coevorden, want daar deelt de gemeente gratis bomen uit. "
          "Wij nemen een struik mee voor onze tuin. "
          "'s Avonds kijken wij op televisie naar de foto's van Museumnacht in Amsterdam. "
          "Zondag kijken wij naar Twente tegen Ajax. "
          "Mijn zus plant ook een boom op haar balkon. "
          "Wat een week voor het klimaat!")
NWORDS = len(MODELO.split())
f.expl(f"Письменное задание (единственного ответа нет); образец ({NWORDS} слов) — ниже.")
f.ex("B1", "Сочинение", "(открытый вопрос — образец ниже)", f"Образец — в разделе H этой страницы ({NWORDS} слов)",
     "«Jouw week in de Klimaatweek» Schrijf 80–100 woorden: wat doe jij in de Klimaatweek, plant jij iets, fiets jij, en kijk jij naar Museumnacht of voetbal?", instr="Сочинение", size=13.8, gap=0)
f.para("Tekstmodel: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= ANTWOORDEN =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "ANTWOORDEN · ОТВЕТЫ — по страницам: ищите по номеру", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "К каждой задаче — пояснение · ✓ — сочинение с образцом", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— СТРАНИЦА {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Сочинение":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.0, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-toets.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("model words:", NWORDS)
