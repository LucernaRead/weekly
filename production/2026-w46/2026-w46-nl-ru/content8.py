# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-nl-ru/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · TOETS EN ANTWOORDEN =================
CURPAGE[0] = 8
p = BSPage4()
p.band("TOETS EN ANTWOORDEN · ТЕСТ И ОТВЕТЫ", "De Lucerna", "Страница 8 · De grote toets van de week + alle antwoorden")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · VUL DE KRONIEK IN", 21, OLIVE, 5)
f.ex("B1", "Выбор в тексте", "B", "Новости Синтерклааса начинаются 9 ноября",
     "Het Sinterklaasjournaal begint op 9 ___. (A. oktober · B. november)", size=13.8, gap=0)
f.ex("B1", "Выбор в тексте", "B", "Национальное прибытие — в Граве",
     "De landelijke intocht is in ___. (A. Amsterdam · B. Grave)", size=13.8, gap=0)
f.ex("B1", "Выбор в тексте", "B", "Прибытие в Амстердам — 88-е по счёту",
     "De intocht in Amsterdam is de ___ editie. (A. 26e · B. 88e)", size=13.8, gap=0)
f.ex("B1", "Выбор в тексте", "B", "Нидерланды — Греция, начало в 20:45",
     "Oranje – Griekenland begint om ___ uur. (A. 18:00 · B. 20:45)", size=13.8, gap=0)
f.ex("B1", "Выбор в тексте", "A", "День святого Мартина — 11 ноября",
     "Sint-Maarten is op 11 ___. (A. november · B. december)", size=13.8, gap=0)
f.ex("B1", "Выбор в тексте", "B", "«Робинсон» идёт на RTL 4",
     "Expeditie Robinson is te zien op ___. (A. NPO 3 · B. RTL 4)", size=13.8, gap=0)
f.ex("B1", "Выбор в тексте", "B", "День святого Мартина — праздник того, чтобы делиться",
     "Sint-Maarten is het feest van het ___. (A. griezelen · B. delen)", size=13.8, gap=0)
f.ex("B1", "Выбор в тексте", "B", "schoen zetten — поставить ботинок",
     "«De schoen zetten» betekent ___. (A. schoenen kopen · B. je schoen neerzetten)", size=13.8, gap=0)
f.head("B · ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "Выбор ответа", "A", "Новости Синтерклааса идут каждый день в 18:00",
     "Het Sinterklaasjournaal is elke dag om... A. 18:00 uur · B. 12:00 uur · C. 20:00 uur", size=13.8, gap=0)
f.ex("A2", "Выбор ответа", "B", "Граве стоит на реке Маас",
     "Grave ligt aan... A. de Amstel · B. de Maas · C. de Rijn", size=13.8, gap=0)
f.ex("A2", "Выбор ответа", "B", "Синтерклаас получает ключ от города в Морском музее",
     "In Amsterdam krijgt Sinterklaas de sleutel bij... A. de Stopera · B. het Scheepvaartmuseum · C. het Leidseplein", size=13.8, gap=0)
f.ex("B1", "Выбор ответа", "A", "«Het diner» опубликован в 2009 году",
     "Het diner van Herman Koch is uit... A. 2009 · B. 2026 · C. 2017", size=13.8, gap=0)
f.ex("B1", "Выбор ответа", "B", "У Нидерландов и Греции по 8 очков",
     "Na vier wedstrijden hebben Nederland en Griekenland ___ punten. A. 5 · B. 8 · C. 0", size=13.8, gap=0)
f.ex("B1", "Выбор ответа", "B", "Германия — Нидерланды, понедельник, в Берлине",
     "Duitsland – Nederland is op maandag in... A. Amsterdam · B. Berlijn · C. Zeist", size=13.8, gap=0)
f.ex("B2", "Выбор ответа", "B", "Традиция живёт, пока люди продолжают её праздновать",
     "Een traditie leeft als... A. ze oud is · B. mensen haar blijven vieren · C. ze op televisie is", size=13.8, gap=0)
f.ex("B1", "Выбор ответа", "C", "Пакьесавонд — в субботу, 5 декабря",
     "Pakjesavond is op... A. 11 november · B. 14 november · C. 5 december", size=13.8, gap=0)
f.head("C · LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Sanne woont in Utrecht. Op woensdag 11 november loopt zij met een lampion mee in de Sint Maarten Parade en zingt zij bij elke deur. Elke dag kijkt zij om 18:00 uur naar het Sinterklaasjournaal. Zaterdag kijkt zij op televisie naar de intocht in Grave. Zondag zet zij haar schoen met een wortel en een verlanglijstje. Vrijdag kijkt zij naar Oranje tegen Griekenland.", 15, lh=1.3, split=False)
f.ex("A2", "Выбор ответа", "B", "Санне живёт в Утрехте",
     "Waar woont Sanne? A. in Grave · B. in Utrecht · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "Выбор ответа", "B", "В среду она присоединяется к шествию святого Мартина",
     "Wat doet Sanne op woensdag 11 november? A. Ze kijkt naar Oranje · B. Ze loopt mee in de Sint Maarten Parade · C. Ze leest Het diner", size=13.8, gap=0)
f.ex("A2", "Выбор ответа", "B", "Она кладёт в ботинок морковку и список желаний",
     "Wat zit er in de schoen van Sanne? A. een boek · B. een wortel en een verlanglijstje · C. een lampion", size=13.8, gap=0)
f.ex("B1", "Выбор ответа", "B", "Она смотрит новости Синтерклааса каждый день в 18:00",
     "Wanneer kijkt Sanne naar het Sinterklaasjournaal? A. om 12:00 uur · B. om 18:00 uur · C. om 20:00 uur", size=13.8, gap=0)
f.head("D · MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "Составление предложения", "Het Sinterklaasjournaal begint op maandag.", "Подлежащее + глагол + время",
     "het sinterklaasjournaal / begint / op maandag → ___", instr="Составление предложения", size=13.8, gap=0)
f.ex("B1", "Составление предложения", "Wij zetten onze schoen bij de deur.", "Подлежащее + глагол + дополнение + место",
     "wij / zetten / onze schoen / bij de deur → ___", instr="Составление предложения", size=13.8, gap=0)
f.ex("B1", "Составление предложения", "Oranje speelt vrijdag tegen Griekenland.", "Подлежащее + глагол + время + соперник",
     "oranje / speelt / vrijdag / tegen griekenland → ___", instr="Составление предложения", size=13.8, gap=0)
f.ex("B1", "Составление предложения", "Ik loop met een lampion langs de deuren.", "Подлежащее + глагол + образ действия + место",
     "ik / loop / met een lampion / langs de deuren → ___", instr="Составление предложения", size=13.8, gap=0)
f.head("E · VERTAAL", 21, OLIVE, 5)
f.ex("A2", "Перевод", "Новости Синтерклааса идут каждый день в 18:00.", "Сравни со статьёй на странице 3",
     "Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="Перевод", size=13.8, gap=0)
f.ex("B1", "Перевод", "День святого Мартина — праздник того, чтобы делиться.", "Оригинальное предложение со страницы 2 · delen — делиться",
     "Sint-Maarten is het feest van het delen. → ___", instr="Перевод", size=13.8, gap=0)
f.ex("B1", "Перевод", "De intocht in Amsterdam is de 88e editie.", "Обрати внимание на порядковое 88e",
     "Прибытие в Амстердам — 88-е по счёту. → ___", instr="Перевод", size=13.8, gap=0)
f.ex("B2", "Перевод", "Ik zet mijn schoen met een verlanglijstje.", "schoen zetten — устойчивое выражение",
     "Я ставлю ботинок, внутри список желаний. → ___", instr="Перевод", size=13.8, gap=0)
f.head("F · WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "Сопоставление",
            ["het journaal", "de intocht", "de lampion", "delen"],
            ["een papieren lichtje voor 11 november",
             "een dagelijks nieuwsprogramma op televisie",
             "licht en eten geven aan anderen",
             "de feestelijke aankomst van Sinterklaas"],
            ["b", "d", "a", "c"],
            ["journaal — новости b", "intocht — праздничное прибытие d", "lampion — фонарик a", "delen — делиться c"],
            instr="Сопоставьте пары слов")
f.head("G · DIALOOG BIJ DE SCHOEN", 21, OLIVE, 5)
f.ex("B1", "Выбор в тексте", "A", "schoen — ботинок",
     "— Mama, waar moet mijn ___? (A. schoen · B. boek)", size=13.8, gap=0)
f.ex("B1", "Выбор в тексте", "A", "wortel — морковка (для лошади)",
     "— Bij de deur, met een ___ voor het paard. (A. wortel · B. lampion)", size=13.8, gap=0)
f.ex("B1", "Выбор в тексте", "A", "verlanglijstje — список желаний",
     "— En mijn ___ erin? (A. verlanglijstje · B. journaal)", size=13.8, gap=0)
f.ex("B1", "Выбор в тексте", "B", "cadeautje — подарочек",
     "— Ja. Sinterklaas brengt 's nachts een ___. (A. mantel · B. cadeautje)", size=13.8, gap=0)
f.ex("B1", "Выбор в тексте", "A", "18:00 — время новостей Синтерклааса",
     "— Eerst kijken we om ___ uur naar het Sinterklaasjournaal. (A. 18:00 · B. 20:45)", size=13.8, gap=0)
f.head("H · SCHRIJF ZELF", 21, OLIVE, 5)
MODELO = ("Maandag 9 november begint het Sinterklaasjournaal. "
          "Ik kijk elke dag om 18:00 uur naar NPO Zapp. "
          "Op woensdag 11 november loop ik met een lampion langs de deuren en zing ik een liedje. "
          "Vrijdag kijk ik naar Oranje tegen Griekenland. "
          "Zaterdag kijk ik naar de intocht in Grave op televisie. "
          "Zondag vaart Sinterklaas in Amsterdam. "
          "Daarna zet ik mijn schoen met een wortel en een verlanglijstje. "
          "Ik hoop op een boek. "
          "Maandag 16 november speelt Oranje in Berlijn tegen Duitsland. "
          "Ik kijk ook dan. "
          "Wat een week vol licht!")
NWORDS = len(MODELO.split())
f.expl(f"Задание на сочинение (без единственного ответа); образцовый текст ({NWORDS} слов) ниже.")
f.ex("B1", "Сочинение", "(открытое задание, образцовый текст ниже)", f"Образцовый текст см. в разделе H ({NWORDS} слов)",
     "«Mijn week met Sinterklaas» Schrijf 80–100 woorden: wat doe jij deze week, loop jij met een lampion, kijk jij naar het Sinterklaasjournaal, en zet jij je schoen?", instr="Сочинение", size=13.8, gap=0)
f.para("Tekstmodel: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= ANTWOORDEN =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "ANTWOORDEN · КЛЮЧ ОТВЕТОВ — найди свой номер", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Каждый ответ с заметкой на русском · ✓ — сочинение", 19.5, "sans", False, GREY, anchor="end")
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
        af.para(txt, 13.0, lh=1.14, gap=0.3, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-toets.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("model words:", NWORDS)
