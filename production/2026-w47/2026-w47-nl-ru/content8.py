# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · TOETS EN ANTWOORDEN =================
CURPAGE[0] = 8
p = BSPage4()
p.band("TOETS EN ANTWOORDEN　ТЕСТ И ОТВЕТЫ", "De Lucerna", "Страница 8　De grote toets van de week + alle antwoorden")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　VUL DE KRONIEK IN", 21, OLIVE, 5)
f.ex("B1", "Выбор в тексте", "B", "Германия — Нидерланды, понедельник, в Берлине",
     "Duitsland – Nederland is op maandag in ___. (A. Amsterdam · B. Berlijn)", size=13.8, gap=0)
f.ex("B1", "Выбор в тексте", "B", "У Нидерландов и Греции по 8 очков",
     "Nederland en Griekenland hebben allebei ___ punten. (A. 5 · B. 8)", size=13.8, gap=0)
f.ex("B1", "Выбор в тексте", "A", "Нидерланды забили 7 голов",
     "Nederland maakte ___ doelpunten in vier wedstrijden. (A. 7 · B. 5)", size=13.8, gap=0)
f.ex("B1", "Выбор в тексте", "B", "Pakjesavond — в декабре",
     "Pakjesavond is op ___ december. (A. november · B. december)", size=13.8, gap=0)
f.ex("B1", "Выбор в тексте", "B", "Новости Синтерклааса в 18:00",
     "Het Sinterklaasjournaal is elke dag om ___ uur. (A. 12:00 · B. 18:00)", size=13.8, gap=0)
f.ex("B1", "Выбор в тексте", "B", "Robinson идёт на RTL 4",
     "Expeditie Robinson is te zien op ___. (A. NPO 3 · B. RTL 4)", size=13.8, gap=0)
f.ex("B1", "Выбор в тексте", "B", "В подарке-сюрпризе есть стихотворение",
     "Bij een surprise hoort een ___. (A. liedje · B. gedicht)", size=13.8, gap=0)
f.ex("B1", "Выбор в тексте", "B", "groepswinst = победа в группе",
     "«De groepswinst» betekent ___. (A. de laatste plaats · B. de eerste plaats in de groep)", size=13.8, gap=0)
f.head("B　ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "Выбор ответа", "A", "Новости Синтерклааса идут каждый день в 18:00",
     "Het Sinterklaasjournaal is elke dag om... A. 18:00 uur · B. 12:00 uur · C. 20:00 uur", size=13.8, gap=0)
f.ex("A2", "Выбор ответа", "B", "Граве стоит на реке Маас",
     "Grave ligt aan... A. de Amstel · B. de Maas · C. de Rijn", size=13.8, gap=0)
f.ex("A2", "Выбор ответа", "B", "Прибытие в Амстердам — 88-е по счёту",
     "De intocht in Amsterdam was de... A. 26e editie · B. 88e editie · C. 30e editie", size=13.8, gap=0)
f.ex("B1", "Выбор ответа", "A", "«Het diner» опубликован в 2009 году",
     "Het diner van Herman Koch is uit... A. 2009 · B. 2026 · C. 2017", size=13.8, gap=0)
f.ex("B1", "Выбор ответа", "B", "Германия проиграла дома Греции 0–1",
     "Duitsland verloor thuis met 0–1 van... A. Servië · B. Griekenland · C. Nederland", size=13.8, gap=0)
f.ex("B1", "Выбор ответа", "B", "ПСВ лидирует в Эредивизи с 26 очками",
     "PSV staat bovenaan in de Eredivisie met ___ punten. A. 25 · B. 26 · C. 8", size=13.8, gap=0)
f.ex("B2", "Выбор ответа", "B", "Традиция живёт, пока её празднуют",
     "Een traditie leeft als... A. ze oud is · B. mensen haar blijven vieren · C. ze op televisie is", size=13.8, gap=0)
f.ex("B1", "Выбор ответа", "C", "13-й тур Эредивизи — 21–22 ноября",
     "Speelronde 13 is op... A. 13 en 14 november · B. 16 november · C. 21 en 22 november", size=13.8, gap=0)
f.head("C　LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Daan woont in Rotterdam. Op maandag 16 november kijkt hij om 20:45 uur naar Duitsland – Nederland in Berlijn. Elke dag kijkt hij om 18:00 uur naar het Sinterklaasjournaal. Zaterdag 21 november kijkt hij naar NEC – PSV. Zondag zet hij zijn schoen met een wortel en een verlanglijstje. Op zondagavond kijkt hij ook naar Expeditie Robinson.", 15, lh=1.3, split=False)
f.ex("A2", "Выбор ответа", "B", "Даан живёт в Роттердаме",
     "Waar woont Daan? A. in Grave · B. in Rotterdam · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "Выбор ответа", "B", "В понедельник он смотрит Германия — Нидерланды",
     "Wat doet Daan op maandag 16 november? A. Hij kijkt naar Robinson · B. Hij kijkt naar Duitsland – Nederland · C. Hij leest Het diner", size=13.8, gap=0)
f.ex("A2", "Выбор ответа", "B", "Он кладёт в башмак морковку и список желаний",
     "Wat zit er in de schoen van Daan? A. een boek · B. een wortel en een verlanglijstje · C. een lampion", size=13.8, gap=0)
f.ex("B1", "Выбор ответа", "B", "Он смотрит новости каждый день в 18:00",
     "Wanneer kijkt Daan naar het Sinterklaasjournaal? A. om 12:00 uur · B. om 18:00 uur · C. om 20:00 uur", size=13.8, gap=0)
f.head("D　MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "Составление предложения", "Het Sinterklaasjournaal begint om 18:00 uur.", "П + Г + время",
     "het sinterklaasjournaal / begint / om 18:00 uur → ___", instr="Составление предложения", size=13.8, gap=0)
f.ex("B1", "Составление предложения", "Wij zetten onze schoen bij de deur.", "П + Г + Д + место",
     "wij / zetten / onze schoen / bij de deur → ___", instr="Составление предложения", size=13.8, gap=0)
f.ex("B1", "Составление предложения", "Oranje speelt maandag in Berlijn.", "П + Г + вр. + место",
     "oranje / speelt / maandag / in berlijn → ___", instr="Составление предложения", size=13.8, gap=0)
f.ex("B1", "Составление предложения", "Ik zet mijn schoen met een wortel.", "П + Г + Д + обр.",
     "ik / zet / mijn schoen / met een wortel → ___", instr="Составление предложения", size=13.8, gap=0)
f.head("E　VERTAAL", 21, OLIVE, 5)
f.ex("A2", "Перевод", "Новости Синтерклааса идут каждый день в 18:00.", "Сравни со статьёй на странице 3",
     "Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="Переведите на русский", size=13.8, gap=0)
f.ex("B1", "Перевод", "Двое первых выходят в четвертьфинал.", "Оригинальное предложение со страницы 4 · kwartfinale = четвертьфинал",
     "De nummers één en twee gaan naar de kwartfinales. → ___", instr="Переведите на русский", size=13.8, gap=0)
f.ex("B1", "Перевод", "De intocht in Amsterdam was de 88e editie.", "88-й",
     "Прибытие в Амстердам — 88-е по счёту. → ___", instr="Переведите на голландский", size=13.8, gap=0)
f.ex("B2", "Перевод", "Ik maak een surprise met een kort gedicht.", "surprise (фикс.)",
     "Я делаю сюрприз с небольшим стихотворением. → ___", instr="Переведите на голландский", size=13.8, gap=0)
f.head("F　WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "Сопоставление",
            ["het journaal", "de groepswinst", "de schoen", "het gedicht"],
            ["een klein versje bij een cadeau",
             "een dagelijks nieuwsprogramma op televisie",
             "de eerste plaats in de groep",
             "die staat 's avonds bij de deur"],
            ["b", "c", "d", "a"],
            ["journaal — новости b", "groepswinst=победа в группе c", "schoen = ботинок d", "gedicht=стихотворение a"],
            instr="Сопоставьте пары слов")
f.head("G　DIALOOG BIJ DE SCHOEN", 21, OLIVE, 5)
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
f.head("H　SCHRIJF ZELF", 21, OLIVE, 5)
MODELO = ("Maandag 16 november speelt Oranje in Berlijn tegen Duitsland. "
          "Ik kijk om 20:45 uur naar NPO 3. "
          "Elke dag kijk ik om 18:00 uur naar het Sinterklaasjournaal. "
          "Op woensdag schrijf ik een gedicht voor mijn surprise. "
          "Zaterdag kijk ik naar NEC – PSV. "
          "Zondag zet ik mijn schoen met een wortel en een verlanglijstje. "
          "Zondagavond kijk ik naar Expeditie Robinson. "
          "Daarna is het bijna pakjesavond, op zaterdag 5 december. "
          "Ik hoop op een boek. "
          "Wat een week vol voetbal en licht!")
NWORDS = len(MODELO.split())
f.bridge(f"Задание на сочинение (без единственного ответа); образцовый текст ({NWORDS} слов) ниже.")
f.ex("B1", "Сочинение", "(открытое задание, образцовый текст ниже)", f"Образцовый текст см. в разделе H ({NWORDS} слов)",
     "«Mijn week met Oranje en Sinterklaas» Schrijf 80–100 woorden: wat doe jij deze week, kijk jij naar Duitsland – Nederland, en zet jij je schoen?", instr="Сочинение", size=13.8, gap=0)
f.para("Tekstmodel: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()
print("P8-ex flow ended col", f.ci, "y", round(f.y, 1), "(bottom 1252)")

# ---- P8 photo (W47: every page carries a public-domain image) ----
# Placed in the final exercise column, below the flow, only if it fits
# above the answers rule at y=1264 (image + caption must end by 1252).
if f.ci == 3 and f.y + 16 + 200 + 78 <= 1252:
    _px = COLX[f.ci]
    _py = f.y + 16
    image(p, "pen.jpg", _px, _py, CW, 200)
    _cy = caption(p, _px, _py + 200, CW, "Een vulpen op een schrift. Schrijf je opstel eerst met de hand — dan in het net.",
                  "Foto: Aaron Burden / Unsplash — CC0")
    print("P8 photo placed at", _px, _py, "ends", _cy)
else:
    print("!! P8 photo NOT placed: flow ended col", f.ci, "y", round(f.y, 1))

# ================= ANTWOORDEN =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "ANTWOORDEN　ОТВЕТЫ — по страницам: найдите свой номер", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "У каждого ответа — короткое пояснение на русском　✓ отмечает письменное задание", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PAGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Сочинение":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.5, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-toets.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("model words:", NWORDS)
