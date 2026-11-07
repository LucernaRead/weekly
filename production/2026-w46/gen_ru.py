# -*- coding: utf-8 -*-
"""Generate W46 NL x RU transform.py from the EN rep pairs (hidden_files/w46/en-reps.txt).
RU precedent (W45 NL x RU): type tokens TRANSLATED to Russian; instr words
localised; all four translation items carry instr="Перевод" (no direction
refinement). Badge REPLACES the strapline at y=372, 19.5pt BRICK. Target
name ГОЛЛАНДСКИЙ. P8 sizes stay at CORE values (Flow 2552, separators
14/1.16/2, keys 13.0/1.16/0.5) with the separator text СТРАНИЦА. bridge()
renamed to expl(); glosses/notes use ' — ' separators, P7 bridges '; '.
Disclosure variable keeps the name dt_zh (W45 RU precedent)."""
import re

REPFILE = "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/en-reps.txt"
lines = open(REPFILE, encoding="utf-8").read().splitlines()
pairs = []
i = 0
while i < len(lines):
    m = re.match(r"^(\S+)\tOLD\t(.*)$", lines[i])
    if not m:
        i += 1
        continue
    m2 = re.match(r"^(\S+)\tNEW\t(.*)$", lines[i + 1])
    assert m2 and m2.group(1) == m.group(1), (i, lines[i], lines[i + 1])
    pairs.append((m.group(1), m.group(2), m2.group(2)))
    i += 2
assert len(pairs) == 265, len(pairs)

RU_MAP = {
    "ELKE WEEK IN HET NEDERLANDS · EVERY WEEK · REAL DUTCH":
        "ELKE WEEK IN HET NEDERLANDS · ЧИТАЕМ ПО-ГОЛЛАНДСКИ",
    "SINTERKLAAS IS COMING": "СИНТЕРКЛААС УЖЕ ЕДЕТ",
    "This week: Sinterklaas comes to the Netherlands · see page 3":
        "На этой неделе: Синтерклаас приезжает в Нидерланды · см. страницу 3",
    'f.bridge("Note | de intocht = arrival · de stoomboot = steamboat · de lampion = lantern.")':
        'f.bridge("Пояснение — de intocht — прибытие · de stoomboot — пароход · de lampion — фонарик.")',
    "DE WEEK IN CIJFERS · IN NUMBERS": "DE WEEK IN CIJFERS · В ЦИФРАХ",
    " (9 Nov: Sinterklaas news)": " (9 нояб.: новости)",
    " (14 Nov: national arrival, Grave)": " (14 нояб.: Граве)",
    " (15 Nov: 88th)": " (15 нояб.: 88-й)",
    " (Fri 20:45)": " (пт 20:45)",
    "NU JIJ · YOUR TURN": "NU JIJ · ТВОЯ ОЧЕРЕДЬ",
    "The Sinterklaas news starts on 9 November": "Новости Синтерклааса начинаются 9 ноября",
    "The national arrival is in Grave": "Национальное прибытие — в Граве",
    "The Amsterdam arrival is on Sunday 15 November": "Прибытие в Амстердам — в воскресенье, 15 ноября",
    "St Martin's Day is on Wednesday 11 November": "День святого Мартина — в среду, 11 ноября",
    "Netherlands–Greece kicks off at 20:45": "Нидерланды — Греция, начало в 20:45",
    "Plural subject, so zetten": "Множественное число → zetten.",
    "· THIS WEEK": "· НА ЭТОЙ НЕДЕЛЕ",
    "Agenda van de week · THIS WEEK'S EVENTS": "Agenda van de week · СОБЫТИЯ НЕДЕЛИ",
    "See pages 2–4 for all dates and times.": "Все даты и время — на страницах 2–4.",
    "IN DEZE EDITIE · IN THIS ISSUE": "IN DEZE EDITIE · В ЭТОМ НОМЕРЕ",
    "«The intocht»: Sinterklaas arrives in a town by boat, then on horseback, in a festive parade.":
        "«De intocht»: праздничное прибытие в город.",
    "IN HET KORT · IN BRIEF": "IN HET KORT · КОРОТКО",
    "BLIKSEMQUIZ · LIGHTNING QUIZ": "BLIKSEMQUIZ · МОЛНИЕНОСНЫЙ ТЕСТ",
    "Read page 1, choose the right answer · answers on page 8":
        "Прочитай страницу 1, выбери правильный ответ · ответы на странице 8",
    "The Sinterklaas news starts on Monday 9 November": "Новости Синтерклааса начинаются в понедельник, 9 ноября",
    "The Amsterdam arrival is the 88th edition": "Прибытие в Амстердам — 88-е по счёту",
    'p.band("LEVEN · LIFE", "De Lucerna", "NIVEAU A2 · Sint-Maarten: lichtjes en liedjes · St Martin\'s Day: lanterns and songs")':
        'p.band("LEVEN · ЖИЗНЬ", "De Lucerna", "NIVEAU A2 · Sint-Maarten: lichtjes en liedjes · День святого Мартина: фонарики и песни")',
    "ZO ONTHOUD JE HET · REMEMBER": "ZO ONTHOUD JE HET · ЗАПОМНИ",
    'f.gloss("de lampion = lantern · delen = to share · de mantel = cloak, coat · de bedelaar = beggar · het erfgoed = heritage · het ledlampje = little LED light.")':
        'f.gloss("de lampion — фонарик · delen — делиться · de mantel — плащ · de bedelaar — нищий · het erfgoed — наследие · het ledlampje — светодиодная лампочка.")',
    "On 11 November, will you go singing door to door with a lantern, or would you rather watch the Sinterklaas news? Write two sentences in Dutch and send them to the editors.":
        "11 ноября ты пойдёшь петь от двери к двери с фонариком или лучше посмотришь новости Синтерклааса? Напиши два предложения по-голландски и пришли в редакцию.",
    "EN JIJ? · AND YOU?": "EN JIJ? · А ТЫ?",
    "SINT-MAARTEN IN VIER WOORDEN · FOUR KEY WORDS": "SINT-MAARTEN IN VIER WOORDEN · ЧЕТЫРЕ КЛЮЧЕВЫХ СЛОВА",
    "Wat hoort bij het feest? · Which words belong to the festival?":
        "Wat hoort bij het feest? · Какие слова относятся к празднику?",
    "a paper lantern, with an LED light inside": "бумажный фонарик, внутри светодиодная лампочка",
    "sharing: giving half a cloak to a beggar": "делиться: отдать половину плаща нищему",
    "St Martin's city, on the heritage list": "город святого Мартина, в списке наследия",
    "singing St Martin's songs door to door": "петь песни святого Мартина от двери к двери",
    "OEFENINGEN · EXERCISES ON PAGE 2": "OEFENINGEN · УПРАЖНЕНИЯ НА СТРАНИЦЕ 2",
    "Answers on page 8 · levels are mixed; find your number": "Ответы на странице 8 · уровни смешаны; ищи свой номер",
    'e.bridge("Read the article on page 2 and choose the right answer.")':
        'e.bridge("Прочитай статью на странице 2 и выбери правильный ответ.")',
    "Children go door to door with lanterns": "Дети ходят от двери к двери с фонариками",
    "Martinus gave half his cloak to a beggar": "Мартин отдал половину своего плаща нищему",
    "Utrecht is St Martin's city": "Утрехт — город святого Мартина",
    "A lantern takes an LED light, not a candle": "В фонарик ставят светодиодную лампочку, а не свечу",
    'e.bridge("Fill in with words from page 2.")': 'e.bridge("Заполни словами со страницы 2.")',
    "St Martin's Day is on 11 November": "День святого Мартина — 11 ноября",
    "lampion = lantern (de)": "lampion — фонарик (de)",
    "delen = to share": "delen — делиться",
    "mantel = cloak (de)": "mantel — плащ (de)",
    "St Martin's city is Utrecht": "Город святого Мартина — Утрехт",
    'e.bridge("Fill in with the song words and the safety tip.")':
        'e.bridge("Заполни словами песни и советом по безопасности.")',
    "Song words: my little light may shine": "Слова песни: мой огонёк может светить",
    "Lanterns shine brightest when it is dark": "Фонарики светят ярче всего, когда темно",
    "An LED light is safe": "Светодиодная лампочка безопасна",
    "Pakjesavond is on 5 December": "Пакьесавонд — 5 декабря",
    '["lampion = lantern b", "delen = to share a", "mantel = cloak d", "erfgoed = heritage c"]':
        '["lampion — фонарик b", "delen — делиться a", "mantel — плащ d", "erfgoed — наследие c"]',
    'instr="Match word to meaning"': 'instr="Сопоставьте пары слов"',
    "HET NIEUWS · TOP STORY": "HET NIEUWS · ГЛАВНАЯ НОВОСТЬ",
    # EN fix-(f) shortened forms
    "mijn schoen = my shoe.": "mijn schoen — мой ботинок.",
    "Fixed phrase: langs de deuren.": "Устойчивое выражение: langs de deuren.",
    "Verb first after the als-clause: ben ik blij.": "Глагол первым после als: ben ik blij.",
    "schoen zetten = to put out your shoe, with a carrot and a drawing inside.":
        "schoen zetten — поставить ботинок, с морковкой и рисунком внутри.",
    'dt_en = "No real letters or best page-8 texts at press time — example; promise to VOL.4."':
        'dt_zh = "Настоящих писем и лучших сочинений со страницы 8 пока нет — печатаем пример; обещание — в VOL.4."',
    "WEEKBLAD IN HET NEDERLANDS · VOL.3 · SINTERKLAAS · SINT-MAARTEN · ORANJE":
        "ГОЛЛАНДСКИЙ ЕЖЕНЕДЕЛЬНИК · VOL.3 · СИНТЕРКЛААС · СИНТ-МАРТЕН · ОРАНЬЕ",
}
RU_MAP.update({
    'p.band("CULTUUR · CULTURE", "De Lucerna", "NIVEAU A2 → B1 · Sinterklaasjournaal en Het diner · The Sinterklaas news and Het diner")':
        'p.band("CULTUUR · КУЛЬТУРА", "De Lucerna", "NIVEAU A2 → B1 · Sinterklaasjournaal en Het diner · Новости Синтерклааса и «Het diner»")',
    'f.gloss("het journaal = news programme · de flessenpost = message in a bottle · de burgemeester = mayor · de stoet = procession · de leeskring = reading club.")':
        'f.gloss("het journaal — новости · de flessenpost — письмо в бутылке · de burgemeester — мэр · de stoet — шествие · de leeskring — читательский кружок.")',
    "OEFENINGEN · EXERCISES ON PAGE 3": "OEFENINGEN · УПРАЖНЕНИЯ НА СТРАНИЦЕ 3",
    'e.bridge("Read the article on page 3 and choose the right answer.")':
        'e.bridge("Прочитай статью на странице 3 и выбери правильный ответ.")',
    "The Sinterklaas news is on every day at 18:00": "Новости Синтерклааса идут каждый день в 18:00",
    "The Amsterdam boat leaves De Omval at 10:15": "Амстердамский корабль отходит от Де Омвал в 10:15",
    "Het diner was written by Herman Koch": "«Het diner» написал Герман Кох",
    "Het diner is free to pick up at the library": "«Het diner» можно бесплатно взять в библиотеке",
    'e.bridge("Fill in with the words from the box.")': 'e.bridge("Заполни словами из рамки.")',
    "journaal = news programme": "journaal — новости",
    "burgemeester = mayor": "burgemeester — мэр",
    "stoet = procession": "stoet — шествие",
    "flessenpost = message in a bottle": "flessenpost — письмо в бутылке",
    "leeskring = reading club": "leeskring — читательский кружок",
    'e.bridge("Complete with the present perfect. Watch the auxiliaries hebben/zijn.")':
        'e.bridge("Заполни в перфекте. Следи за вспомогательными глаголами hebben/zijn.")',
    "beginnen takes zijn: is begonnen": "beginnen требует zijn: is begonnen",
    "vinden perfectum: heeft gevonden": "vinden в перфекте: heeft gevonden",
    "aankomen takes zijn: is aangekomen": "aankomen требует zijn: is aangekomen",
    "lezen perfectum: hebben gelezen": "lezen в перфекте: hebben gelezen",
    'e.bridge("Work it out: answer with the numbers from page 3.")':
        'e.bridge("Посчитай: ответь числами со страницы 3.")',
    "From 9 to 14 November is 5 days": "С 9 по 14 ноября — 5 дней",
    "From 9 to 15 November is 6 days": "С 9 по 15 ноября — 6 дней",
    "The Grave programme, 12:00–16:00, lasts 4 hours": "Программа в Граве, 12:00–16:00, длится 4 часа",
    "Het diner is from 2009: 17 years ago in 2026": "«Het diner» — 2009 года: 17 лет назад в 2026 году",
    'p.band("SPORT", "De Lucerna", "NIVEAU B1 · Oranje en de Nations League · Oranje and the Nations League")':
        'p.band("SPORT · СПОРТ", "De Lucerna", "NIVEAU B1 · Oranje en de Nations League · Оранье и Лига наций")',
    'f.gloss("de groepsfase = group stage · de kwartfinale = quarter-final · ongeslagen = unbeaten · de interland = international match · de stand = the table.")':
        'f.gloss("de groepsfase — групповой этап · de kwartfinale — четвертьфинал · ongeslagen — непобеждённый · de interland — международный матч · de stand — турнирная таблица.")',
    "OEFENINGEN · EXERCISES ON PAGE 4": "OEFENINGEN · УПРАЖНЕНИЯ НА СТРАНИЦЕ 4",
    'e.bridge("Read the article on page 4 and choose the right answer.")':
        'e.bridge("Прочитай статью на странице 4 и выбери правильный ответ.")',
    "Netherlands–Greece, Friday 20:45, in Amsterdam": "Нидерланды — Греция, пятница 20:45, в Амстердаме",
    "The Netherlands and Greece both have 8 points": "У Нидерландов и Греции по 8 очков",
    "The Netherlands scored more goals in the group (7 to 5)": "Нидерланды забили в группе больше голов: 7 против 5",
    "Germany–Netherlands, Monday, in Berlin": "Германия — Нидерланды, понедельник, в Берлине",
    "Eredivisie matchday 13 is on 21–22 November": "13-й тур Эредивизи — 21–22 ноября",
    'e.bridge("Fill in with the words from the box. Watch the verb forms.")':
        'e.bridge("Заполни словами из рамки. Следи за формами глаголов.")',
    "groepsfase = group stage": "groepsfase — групповой этап",
    "kwartfinale plural: kwartfinales": "kwartfinale, множественное число: kwartfinales",
    "ongeslagen = unbeaten": "ongeslagen — непобеждённый",
    "stand = the table": "stand — турнирная таблица",
    "interland = international match": "interland — международный матч",
    'e.bridge("Complete with the past tense or the perfect tense.")':
        'e.bridge("Заполни в прошедшем времени или в перфекте.")',
    "spelen past tense: speelde": "spelen в прошедшем: speelde",
    "winnen past tense: won": "winnen в прошедшем: won",
    "maken past tense: maakte": "maken в прошедшем: maakte",
    "komen perfectum takes zijn": "komen в перфекте требует zijn",
    "True: Netherlands–Greece, Friday 20:45": "Верно: Нидерланды — Греция, пятница 20:45",
    "False: Serbia are bottom with 0 points": "Неверно: Сербия последняя с 0 очками",
    "False: Eredivisie matchday 13 is on 21–22 November": "Неверно: 13-й тур Эредивизи — 21–22 ноября",
    "True: PSV beat Willem II 7–0": "Верно: ПСВ обыграл «Виллем II» 7:0",
    'p.band("JONGEREN · YOUNG PEOPLE", "De Lucerna", "NIVEAU B1 · Robinson, de schoen en het verlanglijstje · Robinson, the shoe and the wish list")':
        'p.band("JONGEREN · МОЛОДЁЖЬ", "De Lucerna", "NIVEAU B1 · Robinson, de schoen en het verlanglijstje · Робинсон, ботинок и список желаний")',
    " (watch on RTL 4, Sunday 20:00)": " (смотри на RTL 4, воскресенье 20:00)",
    " (watch the trials: points are won there)": " (смотри испытания: очки зарабатываются там)",
    " (guess with friends who stays longest)": " (угадай с друзьями, кто продержится дольше)",
    " (then put out your shoe, wish list inside)": " (потом поставь ботинок, список внутри)",
    'f.gloss("het verlanglijstje = wish list · de verslaggever = reporter · de proef = trial, challenge · stemmen = to vote · de aflevering = episode.")':
        'f.gloss("het verlanglijstje — список желаний · de verslaggever — репортёр · de proef — испытание · stemmen — голосовать · de aflevering — выпуск.")',
    "On Sunday, do you watch Expeditie Robinson, or would you rather put out your shoe with a wish list? Write two sentences in Dutch and send them in.":
        "В воскресенье ты смотришь «Expeditie Robinson» или лучше поставишь ботинок со списком желаний? Напиши два предложения по-голландски и пришли.",
    "OEFENINGEN · EXERCISES ON PAGE 5": "OEFENINGEN · УПРАЖНЕНИЯ НА СТРАНИЦЕ 5",
    'e.bridge("Read the article on page 5 and choose the right answer.")':
        'e.bridge("Прочитай статью на странице 5 и выбери правильный ответ.")',
    "Robinson is on every Sunday at 20:00 on RTL 4": "«Робинсон» идёт каждое воскресенье в 20:00 на RTL 4",
    "19 contestants": "19 участников",
    "The show is filmed on a desert island in Malaysia": "Шоу снимают на необитаемом острове в Малайзии",
    "The contestants spend 34 days on the island": "Участники проводят на острове 34 дня",
    "A wish list goes in the shoe": "Список желаний кладут в ботинок",
    "verlanglijstje = wish list (het)": "verlanglijstje — список желаний (het)",
    "verslaggever = reporter (de)": "verslaggever — репортёр (de)",
    "proef = trial, challenge (de)": "proef — испытание (de)",
    "stemmen = to vote": "stemmen — голосовать",
    "aflevering = episode": "aflevering — выпуск",
    "kandidaat plural: kandidaten": "kandidaat, множественное число: kandidaten",
    'e.bridge("Use gaan + infinitive to talk about the future.")':
        'e.bridge("Говори о будущем с gaan + инфинитив.")',
    "gaat winnen = will win (just a guess)": "gaat winnen — выиграет (только догадка)",
    "wij → gaan + infinitive kijken": "wij → gaan + инфинитив kijken",
    "hij → gaat zetten": "hij → gaat zetten",
    "zij (plural) → gaan schrijven": "zij (множественное число) → gaan schrijven",
    "True: the show started on 1 November": "Верно: шоу началось 1 ноября",
    "False: the show is filmed in Malaysia": "Неверно: шоу снимают в Малайзии",
    "False: the carrot in the shoe is for the horse": "Неверно: морковка в ботинке — для лошади",
    'p.band("VERDIEPING · IN DEPTH", "De Lucerna", "NIVEAU B2 · Sint-Maarten of Halloween? · St Martin\'s Day or Halloween?")':
        'p.band("VERDIEPING · РАЗБОР", "De Lucerna", "NIVEAU B2 · Sint-Maarten of Halloween? · День святого Мартина или Хэллоуин?")',
    'f.gloss("de traditie = tradition · griezelen = to scare, to spook · de belangstelling = interest · de achteruitgang = decline · de deskundige = expert.")':
        'f.gloss("de traditie — традиция · griezelen — пугать · de belangstelling — интерес · de achteruitgang — упадок · de deskundige — эксперт.")',
    "Practice data: invented numbers for practice only, not a real survey. Question: what do you do around 11 November? (100 young people)":
        "Учебные данные: выдуманные числа, не настоящий опрос. Вопрос: что ты делаешь около 11 ноября? (100 молодых людей)",
    "DE GRAFIEK · PRACTICE DATA": "DE GRAFIEK · УЧЕБНЫЕ ДАННЫЕ",
    "VOOR OF TEGEN? · FOR OR AGAINST?": "VOOR OF TEGEN? · ЗА ИЛИ ПРОТИВ",
    "OEFENINGEN · EXERCISES ON PAGE 6": "OEFENINGEN · УПРАЖНЕНИЯ НА СТРАНИЦЕ 6",
    'e.bridge("Answer from the chart on page 6 (practice data).")':
        'e.bridge("Ответь по графику на странице 6 (учебные данные).")',
    "40 young people walk with a lantern": "40 молодых людей идут с фонариком",
    "25 celebrate Halloween": "25 празднуют Хэллоуин",
    "40 + 20 = 60": "40 + 20 = 60",
    "15 stay at home": "15 остаются дома",
    "The chart counts 100 people: 40+25+20+15": "В графике 100 человек: 40+25+20+15",
    'e.bridge("Read the article on page 6 and choose the right answer.")':
        'e.bridge("Прочитай статью на странице 6 и выбери правильный ответ.")',
    "In 2025, 26% of Dutch people celebrated Halloween": "В 2025 году 26% голландцев праздновали Хэллоуин",
    "The two surveys use different definitions, so they cannot be compared directly":
        "Два опроса используют разные определения, поэтому их нельзя сравнивать напрямую",
    "Interest in St Martin's Day increased (Stengs, 2025)": "Интерес ко Дню святого Мартина вырос (Стенгс, 2025)",
    "Halloween is about spooking; St Martin's Day is about sharing": "Хэллоуин — это пугать; День святого Мартина — делиться",
    "A tradition lives on when people keep celebrating it": "Традиция живёт, пока люди продолжают её праздновать",
    'e.bridge("Put the words in the right order to make sentences.")':
        'e.bridge("Поставь слова в правильном порядке, чтобы получились предложения.")',
    "traditie = tradition (de)": "traditie — традиция (de)",
    "griezelen = to scare, to spook": "griezelen — пугать",
    "belangstelling = interest (de)": "belangstelling — интерес (de)",
    "achteruitgang = decline (de)": "achteruitgang — упадок (de)",
    "Subject + verb + complement + place": "Подлежащее + глагол + дополнение + место",
    "Subject + verb + manner + place": "Подлежащее + глагол + образ действия + место",
    "The als-clause comes last": "Придаточное с als стоит в конце",
    "kiezen + hoeft niet + explanation": "kiezen + hoeft niet + объяснение",
})
RU_MAP.update({
    'p.band("TAAL · LANGUAGE", "De Lucerna", "Language focus · Drie niveaus, drie gereedschappen · Three levels, three tools")':
        'p.band("TAAL · ЯЗЫК", "De Lucerna", "Язык в фокусе · Drie niveaus, drie gereedschappen · Три уровня, три инструмента")',
    'a.bridge("de stoomboot = steamboat; de intocht = the festive arrival; de schoen zetten = to put out your shoe; de lampion = lantern.")':
        'a.bridge("de stoomboot — пароход; de intocht — праздничное прибытие; de schoen zetten — поставить ботинок; de lampion — фонарик.")',
    "de stoomboot = steamboat": "de stoomboot — пароход",
    "The intocht is Sinterklaas's festive arrival": "Intocht — это праздничное прибытие Синтерклааса",
    "lampion = lantern": "lampion — фонарик",
    'b.bridge("schoentje = little shoe; lichtje = little light; cadeautje = little present. -je means small and affectionate.")':
        'b.bridge("schoentje — ботиночек; lichtje — огонёчек; cadeautje — подарочек. -je означает «маленький» и ласково.")',
    "schoen + -tje: schoentje": "schoen + -tje: schoentje",
    "licht + -je: lichtje": "licht + -je: lichtje",
    "cadeau + -tje: cadeautje": "cadeau + -tje: cadeautje",
    '"-je means small and affectionate, not always really small"':
        '"-je означает «маленький» и ласково, не всегда очень маленький"',
    'c.bridge("Als… = If… / When…; als het donker wordt = when it gets dark; als Sinterklaas komt = when Sinterklaas comes.")':
        'c.bridge("Als… — если… / когда…; als het donker wordt — когда темнеет; als Sinterklaas komt — когда приходит Синтерклаас.")',
    '"Als… = If… / When…"': '"Als… — если… / когда…"',
    '"An als-clause is a condition, not a question"': '"Придаточное с als — условие, а не вопрос"',
    '"The verb comes first in the main clause: gaat de lampion aan"':
        '"Глагол стоит первым в главном предложении: gaat de lampion aan"',
    '"Als Oranje wint… = If Oranje win…"': '"Als Oranje wint… — если Оранье выиграет…"',
    "PAS OP! · ERROR CLINIC": "PAS OP! · КЛИНИКА ОШИБОК",
    '"Sinterklaas is a name, so it takes no article."': '"Sinterklaas — имя, без артикля."',
    '"Putting out your shoe takes mijn schoen (my shoe)."': '"mijn schoen — мой ботинок."',
    '"The fixed phrase is langs de deuren (plural)."': '"Устойчивое выражение: langs de deuren."',
    '"After the als-clause, the main-clause verb comes first: ben ik blij."': '"Глагол первым: ben ik blij."',
    "HET WOORD · WORD OF THE WEEK": "HET WOORD · СЛОВО НЕДЕЛИ",
    '"schoen zetten = to put out your shoe: put your shoe by the door, with a carrot and a drawing inside, for Sinterklaas."':
        '"schoen zetten — поставить ботинок: поставить ботинок у двери, с морковкой и рисунком внутри, для Синтерклааса."',
    'len(wrap(dt_en, "sans", False, 20, CW - 44))': 'len(wrap(dt_zh, "sans", False, 20, CW - 44))',
    'p.para(bx + 22, yy3 + 20, dt_en, 20, "sans", False, GREY, CW - 44, 1.42) + 10':
        'p.para(bx + 22, yy3 + 20, dt_zh, 20, "sans", False, GREY, CW - 44, 1.42) + 10',
    '"Editors\' example — send yours for VOL.4!"':
        '"Пример редакции — присылай свои!"',
    "ZINNEN VAN DE WEEK · PHRASES OF THE WEEK (VERBATIM FROM THIS ISSUE)":
        "ZINNEN VAN DE WEEK · ФРАЗЫ НЕДЕЛИ (ДОСЛОВНО ИЗ ЭТОГО НОМЕРА)",
    "On Monday 9 November, the Sinterklaas news starts on television.":
        "В понедельник, 9 ноября, новости Синтерклааса начинаются по телевизору.",
    "One day later, Sunday 15 November: the Amsterdam arrival, 88th edition.":
        "Днём позже, в воскресенье, 15 ноября: прибытие в Амстердам, 88-е по счёту.",
    "St Martin's Day is the festival of sharing: sharing light, food and attention.":
        "День святого Мартина: делиться светом, едой, вниманием.",
    "On Saturday 14 November, Sinterklaas officially arrives in Grave.":
        "В субботу, 14 ноября, Синтерклаас официально прибывает в Граве.",
    "On Friday 13 November, Oranje play Greece at home.":
        "В пятницу, 13 ноября, Оранье играет дома против Греции.",
    "Every Sunday at 20:00, Expeditie Robinson is on RTL 4.":
        "Каждое воскресенье в 20:00 «Expeditie Robinson» идёт на RTL 4.",
    "St Martin's Day is an old tradition in the Netherlands.":
        "День святого Мартина — старая традиция в Нидерландах.",
    "A tradition lives on when people keep celebrating it.":
        "Традиция живёт, пока люди продолжают её праздновать.",
    "VOLGENDE WEEK · NEXT WEEK (VOL.4)": "VOLGENDE WEEK · СЛЕДУЮЩАЯ НЕДЕЛЯ (VOL.4)",
    'p.band("TOETS EN ANTWOORDEN · TEST AND ANSWERS", "De Lucerna", "Page 8 · De grote toets van de week + alle antwoorden")':
        'p.band("TOETS EN ANTWOORDEN · ТЕСТ И ОТВЕТЫ", "De Lucerna", "Страница 8 · De grote toets van de week + alle antwoorden")',
    "Robinson is on RTL 4": "«Робинсон» идёт на RTL 4",
    "St Martin's Day is the festival of sharing.": "День святого Мартина — праздник того, чтобы делиться.",
    "St Martin's Day is the festival of sharing": "День святого Мартина — праздник того, чтобы делиться",
    "Subject + verb + time": "Подлежащее + глагол + время",
    "Subject + verb + object + place": "Подлежащее + глагол + дополнение + место",
    "Subject + verb + time + opponent": "Подлежащее + глагол + время + соперник",
    "Watch the ordinal 88e": "Обрати внимание на порядковое 88e",
    "schoen zetten is a fixed expression": "schoen zetten — устойчивое выражение",
    '["journaal = news programme b", "intocht = the festive arrival d", "lampion = lantern a", "delen = to share c"]':
        '["journaal — новости b", "intocht — праздничное прибытие d", "lampion — фонарик a", "delen — делиться c"]',
    "schoen = shoe": "schoen — ботинок",
    "wortel = carrot (for the horse)": "wortel — морковка (для лошади)",
    "verlanglijstje = wish list": "verlanglijstje — список желаний",
    "cadeautje = little present": "cadeautje — подарочек",
    "18:00 = the Sinterklaas news time": "18:00 — время новостей Синтерклааса",
    "Sanne lives in Utrecht": "Санне живёт в Утрехте",
    "On Wednesday she joins the St Martin's parade": "В среду она присоединяется к шествию святого Мартина",
    "She puts a carrot and a wish list in her shoe": "Она кладёт в ботинок морковку и список желаний",
    "She watches the Sinterklaas news every day at 18:00": "Она смотрит новости Синтерклааса каждый день в 18:00",
    "Het diner was published in 2009": "«Het diner» опубликован в 2009 году",
    "Sinterklaas receives the key to the city at the Maritime Museum":
        "Синтерклаас получает ключ от города в Морском музее",
    "Pakjesavond is on Saturday 5 December": "Пакьесавонд — в субботу, 5 декабря",
    "Grave lies on the river Maas": "Граве стоит на реке Маас",
    "Compare with the page 3 article": "Сравни со статьёй на странице 3",
    "Original sentence from page 2 · delen = to share": "Оригинальное предложение со страницы 2 · delen — делиться",
    '"Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="Translate into English"':
        '"Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="Перевод"',
    '"Sint-Maarten is het feest van het delen. → ___", instr="Translate into English"':
        '"Sint-Maarten is het feest van het delen. → ___", instr="Перевод"',
    '"The arrival in Amsterdam is the 88th edition. → ___", instr="Translate into Dutch"':
        '"Прибытие в Амстердам — 88-е по счёту. → ___", instr="Перевод"',
    '"I put out my shoe, with a wish list inside. → ___", instr="Translate into Dutch"':
        '"Я ставлю ботинок, внутри список желаний. → ___", instr="Перевод"',
    '"(open task, model text below)"': '"(открытое задание, образцовый текст ниже)"',
    "Writing task (no single answer); model text ({NWORDS} words) below.":
        "Задание на сочинение (без единственного ответа); образцовый текст ({NWORDS} слов) ниже.",
    "See the model text in section H ({NWORDS} words)":
        "Образцовый текст см. в разделе H ({NWORDS} слов)",
    "ANTWOORDEN · ANSWER KEY — grouped by page: find your number":
        "ANTWOORDEN · КЛЮЧ ОТВЕТОВ — найди свой номер",
    "Every answer has a short note in English · ✓ marks the writing task":
        "Каждый ответ с заметкой на русском · ✓ — сочинение",
    "schoen zetten = to put out your shoe": "schoen zetten — поставить ботинок",
    "Netherlands–Greece kicks off at 20:45 on Friday": "Нидерланды — Греция, начало в пятницу в 20:45",
    "The Sinterklaas news is on every day at 18:00.": "Новости Синтерклааса идут каждый день в 18:00.",
    "The Sinterklaas news starts on Monday 9 November.": "Новости Синтерклааса начинаются в понедельник, 9 ноября.",
    "hij → gaat zetten": "hij → gaat zetten",
    "40 + 20 = 60": "40 + 20 = 60",
})

# pairs that need special handling
SKIP_IDX = {0, 1, 2, 3, 4, 5, 6, 8, 9, 11}
BADGE_IDX = 14
# pair 7: identity rep on the post-loop Сочинение check form
# pairs 8, 9, 10: P8 sizes stay at CORE values; only the separator TEXT
#   changes (PAGINA -> СТРАНИЦА), handled by the furniture rep below
# pair 13: subtitle — Russian line via map lookup

hdr = '''# -*- coding: utf-8 -*-
"""One-off fan-out transform: W46 NL core (Chinese explanations) -> NL x RU.
Line-literal replacements only, each asserted. Run once from this dir.
Dutch target text, keys (except re-aimed 137/138), facts, images: untouched.
Furniture per the W43/W45 NL x RU registry: badge REPLACES strapline y=372
(19.5pt bold BRICK), footer ГОЛЛАНДСКИЙ ЕЖЕНЕДЕЛЬНИК, gloss prefix
Пояснение —, P8 sizes at CORE values with СТРАНИЦА separators. Type tokens
TRANSLATED to Russian; instr words localised; all four translation items
carry instr="Перевод". bridge() renamed to expl(); glosses/notes use ' — ',
P7 bridges '; '. Disclosure variable keeps the name dt_zh (W45 RU).
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
R = []

def rep(f, old, new):
    R.append((f, old, new))

def rep_opt(f, old, new):
    R.append((f, old, new, True))

# ---------- global path (content files) ----------
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    rep(f, "weekly-report-w46-nl-core/svg", "weekly-report-w46-nl-ru/svg")

# ---------- types + instr (instrs FIRST, cloze before plain choice) ----------
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    rep_opt(f, 'instr="填空"', 'instr="Заполните пропуск"')
    rep_opt(f, 'instr="判断"', 'instr="Верно или нет?"')
    rep_opt(f, 'instr="造句"', 'instr="Составление предложения"')
    rep_opt(f, 'instr="写作"', 'instr="Сочинение"')
    rep_opt(f, 'instr="翻译"', 'instr="Перевод"')
    rep_opt(f, "完形单选", "Выбор в тексте")
    rep_opt(f, "完成句子", "Дополнение предложения")
    rep_opt(f, "词汇配对", "Сопоставление")
    rep_opt(f, "判断对错", "Верно или неверно")
    rep_opt(f, "单选", "Выбор ответа")
    rep_opt(f, "造句", "Составление предложения")
    rep_opt(f, "翻译", "Перевод")
    rep_opt(f, "写作", "Сочинение")

# ---------- furniture ----------
rep("render.py", "weekly-report-w46-nl-core", "weekly-report-w46-nl-ru")
rep("render.py", "De-Lucerna-VOL3.pdf", "De-Lucerna-VOL3-RU.pdf")
rep_opt("render.py", "Render the NL weekly VOL.3", "Render the NL x RU weekly VOL.3")
rep_opt("run.py", "Run the IT weekly", "Run the NL x RU weekly")
rep("bslib4.py", "De Lucerna · 荷兰语周报 VOL.3 · LUCERNA DUTCH WEEKLY",
     "De Lucerna · ГОЛЛАНДСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.3 · ТЕКСТЫ НА ГОЛЛАНДСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ")
rep("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"Страница {n} из {total}"')
rep("bslib4.py", "译注｜", "Пояснение — ")
rep("bslib4.py", "    def bridge(self, s, size=20.5, gap=9, fill=GREY):",
     "    def expl(self, s, size=20.5, gap=9, fill=GREY):")
rep("svglib.py", "for 重阳", "for Double Ninth")
rep("content8.py", 'af.para(f"— PAGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)',
     'af.para(f"— СТРАНИЦА {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)')
rep("content8.py", 'f.bridge(f"', 'f.expl(f"')

# ---------- literal replacements ----------
'''

tail = '''
# ---------- apply ----------
def main():
    failed = 0
    for item in R:
        f, old, new = item[0], item[1], item[2]
        opt = len(item) > 3
        path = os.path.join(HERE, f)
        txt = open(path, encoding="utf-8").read()
        n = txt.count(old)
        if n == 0 and not opt:
            failed += 1
            print(f"FAILED {f}: {old[:70]!r}")
        txt = txt.replace(old, new)
        open(path, "w", encoding="utf-8").write(txt)
    print("TOTAL replacements:", len(R), "FAILED:", failed)
    import re as _re
    cjk = 0
    for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py",
              "bslib4.py", "render.py", "run.py"]:
        for ln in open(os.path.join(HERE, f), encoding="utf-8"):
            if _re.search(r"[\\u4e00-\\u9fff]", ln):
                cjk += 1
    print(cjk)

if __name__ == "__main__":
    main()
'''

out = []
missing = []
for j, (f, old, new) in enumerate(pairs):
    if j in SKIP_IDX:
        continue
    if j == 7:
        form = 'if e_["type"] == "Сочинение":'
        out.append((f, form, form))
        continue
    if j == 10:
        out.append((f, old, 'af.para(txt, 13.0, lh=1.14, gap=0.3, split=False)'))
        continue
    if j == BADGE_IDX:
        badge = ('p.text(975, 372, "ТЕКСТЫ НА ГОЛЛАНДСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — '
                 'ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ", 19.5, "sans", True, BRICK, anchor="middle")')
        out.append((f, old, badge))
        continue
    if "题（无唯一答案）" in old or new.startswith("Writing task (no single answer)"):
        old = old.replace("writing题", "Сочинение题")
        out.append((f, old, RU_MAP[new].replace(".bridge(", ".expl(")))
        continue
    if 'instr="Translate' in old:
        old = old.replace('instr="Translate into English"', 'instr="Перевод"')
        old = old.replace('instr="Translate into Dutch"', 'instr="Перевод"')
        old = old.replace('instr="Translate"', 'instr="Перевод"')
    if "writing题" in old:
        raise SystemExit(f"unexpected writing-form old at pair {j}: {old!r}")
    if new in RU_MAP:
        val = RU_MAP[new].replace(".bridge(", ".expl(")
        out.append((f, old, val))
    elif len(new) > 1 and new.startswith('"') and new.endswith('"') and new[1:-1] in RU_MAP:
        out.append((f, old, '"' + RU_MAP[new[1:-1]].replace(".bridge(", ".expl(") + '"'))
    else:
        missing.append((j, f, new))
if missing:
    print("UNMAPPED:", len(missing))
    for j, f, new in missing:
        print(j, f, new)
    raise SystemExit(1)
seen = set()
ded = []
for p in out:
    if p in seen:
        continue
    seen.add(p)
    ded.append(p)
with open("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/transform_ru.py", "w", encoding="utf-8") as fh:
    fh.write(hdr)
    for f, old, new in ded:
        fh.write(f"rep({f!r}, {old!r}, {new!r})\n")
    fh.write(tail)
print("wrote", len(ded), "reps")
