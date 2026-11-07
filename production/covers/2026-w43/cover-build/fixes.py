#!/usr/bin/env python3
"""Hand fixes for W43 teasers: fragments/empties from v3 extraction, each
rewritten from the source edition abstract (no new facts, no boilerplate).
Plus first-letter capitalization for complete clauses that lost their
sentence-initial word, and the two cross-script cells (W45 precedent:
teaser in the READER's script, composed from the story excerpt/headline).
Note: the W43 zh-tw excerpt writes the typhoon name as 昌皮; the W43
headline writes 薔琵 — the cross-script simplified cell uses the headline
form 薔琵/蔷琵."""
import json

P = '/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w43/cover-build/teasers.json'
d = json.load(open(P, encoding='utf-8'))
T = d['teasers']

CAP = [('de','en'), ('de','es'), ('de','it'), ('de','zh-cn'), ('ru','de')]
for r, s in CAP:
    t = T[r][s]
    assert t and t[0].islower(), (r, s, t[:50])
    T[r][s] = t[0].upper() + t[1:]

FIX = {
('en','fr'): "The passage à l'heure d'hiver on Sunday, when France recule d'une heure, the vacances de la Toussaint with their chrysanthèmes, and Halloween as it is actually marked in France. Further pages follow the présidentielle 2027 sondages, Victor Wembanyama, and fans awaiting GTA VI.",
('en','it'): "Italy returns to l'ora solare, lancette indietro, and a second thread explains the Manovra 2027, the legge di bilancio then being debated.",
('en','ru'): "«Первый снег» sets the scene for an issue on autumn life in Russia and the long New Year holidays ahead — twelve days of новогодние каникулы to plan for.",
('de','nl'): "Herbstferien (herfstvakantie), die Dutch Design Week in Eindhoven mit dem Thema R.A.W. und die 30. Ausgabe des Amsterdam Dance Event. Außerdem die Winterzeit (wintertijd) mit der Merkregel „Voorjaar vooruit, najaar achteruit“ — im Frühjahr vor, im Herbst zurück — sowie Expeditie Robinson und das Topspiel PSV gegen Feyenoord.",
('de','pt'): "Die Stichwahl (segundo turno) am 25. Oktober — mit Anleitungen zum Wählen, der App e-Título und der elektronischen Wahlurne (urna eletrônica). Dazu das letzte TV-Duell auf Globo, die ENEM-Prüfungen im November, die Realityshow A Fazenda, die Rückkehr der Gitarre in den Suchtrends und das Halbfinale der Copa Sul-Americana, Vasco gegen Boca.",
('de','ru'): "„Der erste Schnee“ eröffnet die russische Herbstausgabe mit dem ersten Schnee der Saison und blickt voraus auf die langen Neujahrsferien, zwölf Tage am Stück, die in Russland schon jetzt geplant werden.",
('en','ja'): "The opening of the Japan Series — Yokohama DeNA against Fukuoka SoftBank, Game 1 on 24 October at 18:30 — as autumn deepens across Japan.",
('en','ko'): "Korea between seasons: Typhoon Champi approaching in the forecasts, autumn foliage at its 단풍 peak, and the 수능 countdown week for students nationwide.",
('en','pt'): "The segundo turno of the eleições on 25 October, explained step by step — como votar, the e-Título app and the urna eletrônica — after the final debate on Globo. Other pages look ahead to the ENEM in November, follow A Fazenda and the Copa Sul-Americana semi-final between Vasco and Boca, and note the guitar's return in search trends.",
('en','zh-cn'): "Double 11 tail-payment week, when Tmall shoppers paid their 付尾款 balances from 20:00 on 20 October. Inside: hairy crabs （大闸蟹） in season, with prices tracked at Beijing's Xinfadi market, plus the solar term 霜降 on 23 October and a look back at 重阳.",
('en','zh-tw'): "A week shaped by Typhoon 薔琵 and the northeast monsoon. Sports pages cover Game 1 of the 台灣大賽, the Wei Chuan Dragons' 3:0 win before a full house of 40,000, while culture pages follow the 61st Golden Bell Awards （金鐘獎） on 23–24 October, Hong Kong's 重陽 holiday and the Wine & Dine festival.",
('es','nl'): "Las vacaciones de otoño, la Dutch Design Week de Eindhoven con su tema R.A.W. y la trigésima edición del Amsterdam Dance Event. También explica el paso al horario de invierno con el dicho «en primavera adelante, en otoño atrás», y cierra con el reality Expeditie Robinson y el clásico PSV–Feyenoord.",
('nl','fr'): "De late herfst: zondag gaat Frankrijk over op de wintertijd en gaat de klok een uur terug, gevolgd door de Toussaint met de herfstvakantie en chrysanten, en Halloween in Frankrijk. Ook aan bod: de presidentsverkiezingen van 2027 en de laatste peilingen, basketballer Victor Wembanyama en het door fans langverwachte GTA VI.",
('pt','fr'): "Em pleno outono francês: no domingo, os relógios recuam uma hora com a chegada do horário de inverno, e a Toussaint se aproxima com suas férias escolares e crisântemos. A edição comenta ainda o Halloween na França, as pesquisas para a eleição presidencial de 2027, Victor Wembanyama e a espera dos fãs por GTA VI. Reculer é a palavra da semana.",
('ru','en'): "Самая насыщенная неделя американской осени: открывается досрочное голосование, проходит матч открытия сезона NBA, где 76ers обыграли Knicks со счётом 106–100, в пятницу стартует Мировая серия (Brewers против Rays) и гонка «Формулы-1» в Остине, а также седьмая неделя NFL. Отдельные материалы — о расходах на Хэллоуин (13,5 млрд долларов), индексации Social Security COLA на 3,6 % к 2027 году и переводе часов: в США 1 ноября, в Европе уже в это воскресенье.",
('ru','es'): "Одно воскресенье — три события: перевод часов на зимнее время, воскресный El Clásico в 21:00 и этап «Формулы-1» в Остине.",
('ru','fr'): "Глубокая осень: в воскресенье Франция переходит на зимнее время («on recule d’une heure» — слово недели reculer), впереди каникулы Дня всех святых с их хризантемами и французский Хэллоуин. Политика представлена опросами перед президентскими выборами 2027 года — два тура и намерения избирателей, спорт — Виктором Вембаньямой, а поп-культура — ожиданиями фанатов GTA VI.",
('ru','it'): "В Италии неделя проходит под знаком лишнего часа сна: возвращается зимнее время ora solare, стрелки переводят назад, а парламент обсуждает бюджетный закон Manovra 2027 — legge di bilancio.",
('ru','ja'): "Неделя Японской серии: в субботу, 24 октября, в 18:30 первый матч сыграют Yokohama DeNA и Fukuoka SoftBank, и бейсбольное противостояние задаёт рамку всему номеру на фоне углубляющейся осени.",
('ru','ko'): "К Корее приближается тайфун Чампи — пока на стадии прогноза; осенняя листва в эти дни достигает пика окраски, а старшеклассники живут в режиме обратного отсчёта до экзамена сунын.",
('ru','pt'): "Воскресенье в Бразилии — день решения: неделя второго тура выборов, с инструкциями, как голосовать, что такое e-Título и как работает электронная урна urna eletrônica, а также с финальными теледебатами на Globo. В номере также ноябрьский экзамен ENEM, телешоу A Fazenda, возвращение моды на гитару и полуфинал Кубка Южной Америки Vasco — Boca.",
('ru','zh-cn'): "Неделя финальных платежей: 20 октября в 20:00 на Tmall открылась оплата остатков по предзаказам «Двойного одиннадцатого». В номере также прилавки с волосатым крабом 大闸蟹 и цены рынка Синьфади, сезонный рубеж 霜降 23 октября и ретроспектива праздника 重阳.",
('ru','zh-tw'): "Сильный тайфун Цянпи (薔琵) вместе с северо-восточным муссоном задаёт погоду недели на Тайване. Первый матч Тайваньской серии: Wei Chuan Dragons победили 3:0 при полных трибунах — 40 000 зрителей. В выпуске также 61-я церемония премии «Золотой колокол» (金鐘獎) 23–24 октября, гонконгский выходной на праздник 重陽 и фестиваль еды и вина Wine & Dine.",
('zh-tw','zh-cn'): "雙11「付尾款」週：大閘蟹、霜降與購物節預熱。",
('zh-cn','zh-tw'): "强台蔷琵压境，周五、周六风雨最大，东北季风、台湾大赛与金钟奖同在本周。",
}
for (r, s), t in FIX.items():
    T[r][s] = t

json.dump(d, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'applied {len(CAP)} capitalizations + {len(FIX)} hand fixes')

# re-flag: only boilerplate markers + empties + fragments count now
BAD = ['150','A2','B2','Übungen','esercizi','oefeningen','graded','MISSING','<<']
n = 0
for R in sorted(T):
    for S in sorted(T[R]):
        t = T[R][S]
        flags = []
        if len(t) < 10: flags.append('EMPTY/SHORT')
        for b in BAD:
            if b in t: flags.append(f'HAS:{b}')
        if t and t[0].islower(): flags.append('LOWER-START')
        if flags:
            n += 1
            print(f'{R}/{S} [{",".join(flags)}] {t[:150]}')
print('remaining flagged:', n)
