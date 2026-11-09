# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · TOETS EN ANTWOORDEN =================
CURPAGE[0] = 8
p = BSPage4()
p.band('TOETS EN ANTWOORDEN　ТЕСТ И ОТВЕТЫ', "De Lucerna", 'Страница 8　De grote toets van de week + alle antwoorden')

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　VUL DE KRONIEK IN", 21, OLIVE, 5)
f.ex("B1", 'Выбор в тексте', "B", 'осенью часы переводят назад',
     "In de nacht van zaterdag op zondag gaat de klok één uur ___. (A. vooruit · B. achteruit)", size=13.8, gap=0)
f.ex("B1", 'Выбор в тексте', "A", 'каникулы в Миддене и Зёйде — до 25 октября',
     "De herfstvakantie van Midden en Zuid duurt tot en met zondag ___ oktober. (A. 25 · B. 18)", size=13.8, gap=0)
f.ex("B1", 'Выбор в тексте', "A", 'Неделя дизайна — в Эйндховене',
     "De Dutch Design Week is in ___. (A. Eindhoven · B. Amsterdam)", size=13.8, gap=0)
f.ex("B1", 'Выбор в тексте', "B", 'PSV выиграл в гостях у «Порту»',
     "PSV won in de Champions League bij ___. (A. Atalanta · B. FC Porto)", size=13.8, gap=0)
f.ex("B1", 'Выбор в тексте', "B", 'ADE в этом году — 30 лет',
     "ADE wordt dit jaar ___ jaar. (A. 25 · B. 30)", size=13.8, gap=0)
f.ex("B1", 'Выбор в тексте', "A", '«Робинзон» начинается в ноябре',
     "Expeditie Robinson begint op 1 ___. (A. november · B. oktober)", size=13.8, gap=0)
f.ex("B1", 'Выбор в тексте', "A", 'крупнейший запрос о часах — «wintertijd»',
     "De grootste zoekterm over de klok was «___». (A. wintertijd · B. klok vooruit)", size=13.8, gap=0)
f.ex("B1", 'Выбор в тексте', "B", "half drie = 2:30",
     "«Half drie» is ___. (A. 03:30 · B. 02:30)", size=13.8, gap=0)
f.head("B　ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", 'Выбор ответа', "B", 'зимнее время — в 03:00 ночи',
     "De wintertijd begint om... A. 02:00 uur · B. 03:00 uur · C. middernacht", size=13.8, gap=0)
f.ex("A2", 'Выбор ответа', "A", 'у региона Норд каникулы были 10–18 октября',
     "Welke regio had vakantie van 10 tot en met 18 oktober? A. Noord · B. Midden · C. Zuid", size=13.8, gap=0)
f.ex("A2", 'Выбор ответа', "C", 'студенческий билет — € 19,50',
     "Een studentenkaartje voor de DDW kost... A. € 32,50 · B. € 25,00 · C. € 19,50", size=13.8, gap=0)
f.ex("B1", 'Выбор ответа', "A", '«Фейеноорд» в среду — в Севилье',
     "Feyenoord speelt woensdag in... A. Sevilla · B. Porto · C. Eindhoven", size=13.8, gap=0)
f.ex("B1", 'Выбор ответа', "B", '«Спарта» — «Аякс» начинается в 16:45',
     "Sparta – Ajax begint zondag om... A. 14:30 uur · B. 16:45 uur · C. 20:00 uur", size=13.8, gap=0)
f.ex("B1", 'Выбор ответа', "B", '19 участников — нидерландцы и фламандцы',
     "De 19 kandidaten van Expeditie Robinson zijn... A. allemaal dj's · B. Nederlanders en Vlamingen · C. alleen sporters", size=13.8, gap=0)
f.ex("B2", 'Выбор ответа', "B", '6.600 запросов спрашивали про «вперёд» (наоборот)',
     "De 6.600 zoekopdrachten vroegen naar... A. achteruit · B. vooruit · C. wintertijd", size=13.8, gap=0)
f.ex("B1", 'Выбор ответа', "A", 'сервис отныне чётко показывает все доплаты',
     "Thuisbezorgd laat voortaan... A. alle extra kosten duidelijk zien · B. geen eten meer bezorgen · C. alleen kortingsbonnen zien", size=13.8, gap=0)
f.head("C　LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Sanne woont in Utrecht, in de regio Midden. Zij heeft de hele week herfstvakantie. Op woensdag gaat zij met haar zus naar Eindhoven, naar de Dutch Design Week. Zaterdagavond zet zij alle klokken in huis één uur achteruit — behalve haar telefoon, die doet het zelf. Zondag slaapt zij lang uit: het is de laatste dag van de vakantie.", 15, lh=1.3, split=False)
f.ex("A2", 'Выбор ответа', "B", 'Санне живёт в Утрехте',
     "Waar woont Sanne? A. in Venlo · B. in Utrecht · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", 'Выбор ответа', "B", 'в её регионе сейчас осенние каникулы',
     "Waarom heeft Sanne de hele week vrij? A. Zij is ziek · B. Het is herfstvakantie in haar regio · C. Zij werkt niet", size=13.8, gap=0)
f.ex("A2", 'Выбор ответа', "B", 'в субботу вечером она переводит часы',
     "Wat doet Sanne zaterdagavond? A. Zij gaat dansen · B. Zij zet de klokken achteruit · C. Zij pakt haar koffer", size=13.8, gap=0)
f.ex("B1", 'Выбор ответа', "C", 'телефон меняет время сам, вручную не нужно',
     "Welke klok zet Sanne NIET met de hand achteruit? A. de ovenklok · B. de wekker · C. haar telefoon", size=13.8, gap=0)
f.head("D　MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", 'Составление предложения', "De klok gaat één uur achteruit.", 'подлежащее + глагол + дополнение + направление',
     "de klok / gaat / één uur / achteruit → ___", instr='Составление предложения', size=13.8, gap=0)
f.ex("B1", 'Составление предложения', "Wij gaan zondag naar de topper.", 'подлежащее + глагол + время + место',
     "wij / gaan / zondag / naar de topper → ___", instr='Составление предложения', size=13.8, gap=0)
f.ex("B1", 'Составление предложения', "Hoe laat begint de wedstrijd?", 'вопросительная фраза — в начале',
     "hoe laat / begint / de wedstrijd / ? → ___", instr='Составление предложения', size=13.8, gap=0)
f.ex("B1", 'Составление предложения', "PSV won met 1–0 in Porto.", 'подлежащее + глагол + счёт + место',
     "psv / won / met 1–0 / in porto → ___", instr='Составление предложения', size=13.8, gap=0)
f.head("E　VERTAAL", 21, OLIVE, 5)
f.ex("A2", 'Перевод', 'В воскресенье часы переводят назад: спим на час дольше!', 'ср. заголовок на странице 1',
     "Zondag gaat de klok terug: een uur langer slapen! → ___", instr='Перевод', size=13.8, gap=0)
f.ex("B1", 'Перевод', 'Твой телефон и компьютер сами меняют время.', 'фраза со страницы 2 · veranderen — менять',
     "Je telefoon en je computer veranderen de tijd zelf. → ___", instr='Перевод', size=13.8, gap=0)
f.ex("B1", 'Перевод', "De Dutch Design Week is in Eindhoven.", 'следите за оборотом места in Eindhoven',
     'Неделя дизайна (Dutch Design Week) проходит в Эйндховене. → ___', instr='Перевод', size=13.8, gap=0)
f.ex("B2", 'Перевод', "Zondag heb ik een uur langer geslapen.", 'перфект: heb geslapen',
     'В воскресенье я спал на час дольше. → ___', instr='Перевод', size=13.8, gap=0)
f.head("F　WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", 'Сопоставление слов',
            ["de klok verzetten", "het ezelsbruggetje", "eropuit gaan", "bijslapen"],
            ["extra slapen om uit te rusten",
             "het huis uit gaan voor iets leuks",
             "een hulpmiddel om iets te onthouden",
             "de tijd op een klok veranderen"],
            ["d", "c", "b", "a"],
            ['verzetten = переводить часы d', 'ezelsbruggetje = запоминалка c', 'eropuit = выйти развлечься b', 'bijslapen = высыпаться a'],
            instr='Сопоставьте пары слов')
f.head("G　DIALOOG BIJ DE DDW", 21, OLIVE, 5)
f.ex("B1", 'Выбор в тексте', "B", 'kaartje = билет',
     "— Goedemorgen! Een ___ voor de Dutch Design Week, alstublieft. (A. ezelsbruggetje · B. kaartje)", size=13.8, gap=0)
f.ex("B1", 'Выбор в тексте', "A", 'student = студент (билет € 19,50)',
     "— Natuurlijk. Bent u ___? Studenten betalen € 19,50. (A. student · B. ontwerper)", size=13.8, gap=0)
f.ex("B1", 'Выбор в тексте', "B", 'tot hoe laat = до которого часа (открыто)',
     "— Ja! Hier is mijn studentenkaart. En tot hoe ___ zijn jullie open? (A. lang · B. laat)", size=13.8, gap=0)
f.ex("B1", 'Выбор в тексте', "A", 'veel plezier = приятного времяпрепровождения',
     "— Tot 18:00 uur. Veel ___ met de ontwerpen! (A. plezier · B. slaap)", size=13.8, gap=0)
f.ex("B1", 'Выбор в тексте', "B", 'tot ziens = до свидания',
     "— Dank u wel, tot ___! (A. straks · B. ziens)", size=13.8, gap=0)
f.head("H　SCHRIJF ZELF", 21, OLIVE, 5)
MODELO = ("Zondag 25 oktober word ik laat wakker: het is de laatste dag van mijn herfstvakantie. "
          "Ik heb een uur langer geslapen, want vannacht ging de klok achteruit. "
          "Na het ontbijt ga ik met mijn vrienden naar het bos; de bladeren zijn geel en rood. "
          "'s Middags kijken wij thuis naar PSV tegen Feyenoord op televisie. "
          "Mijn zus gaat naar Amsterdam voor ADE, maar ik blijf liever thuis met een boek. "
          "'s Avonds pak ik mijn tas voor school: morgen begint het gewone leven weer. "
          "Wat een week!")
NWORDS = len(MODELO.split())
f.expl(f"Письменное задание (единственного ответа нет); образец ({NWORDS} слов) — ниже.")
f.ex("B1", 'Сочинение', '(открытый вопрос — образец ниже)', f"Образец — в разделе H этой страницы ({NWORDS} слов)",
     "«Jouw zondag 25 oktober» Schrijf 80–100 woorden: wat doe jij op de laatste vakantiedag, hoe laat sta jij op, en wat doe jij 's middags?", instr='Сочинение', size=13.8, gap=0)
f.para("Tekstmodel: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= ANTWOORDEN =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, 'ANTWOORDEN　ОТВЕТЫ — по страницам: ищите по номеру', 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, 'К каждой задаче — пояснение　✓ — сочинение с образцом', 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— СТРАНИЦА {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == 'Сочинение':
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
