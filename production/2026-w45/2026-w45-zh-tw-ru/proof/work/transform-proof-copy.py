# -*- coding: utf-8 -*-
"""W45 zh-tw x RU fan-out transform (EN explanation layer -> RU).

Usage: python3 transform.py <build_dir> <edition_dir>
  build_dir   : copy of the zh-tw core build (content*.py, bslib4.py, render.py)
  edition_dir : delivery dir, e.g. .../files/weekly-report-w45-zh-tw-ru

Design (README rules #11/#17/#18, transform-first discipline):
- Plain literal replacements with a per-pair occurrence assertion (count > 0,
  and the count is printed). No AST byte-offset splicing; f-string fragments
  are replaced with bare text, never repr literals.
- Path repointing is tolerant: if the core path is already gone (main build
  was repointed by hand before the first transform run), the edition path
  must already be present, otherwise fail.
- Target Traditional Chinese text is NEVER touched: every pair below is an
  English explanation string, a furniture string, or a P8 note. Keys are
  byte-identical except that P8 note strings (4th reg_ex argument) change.
- CJK safety: Russian strings keep the core English string's CJK characters
  at the same positions/counts, or drop them. No new CJK character is
  introduced, and no ASCII , : ; ? ! is placed directly adjacent to a CJK
  character (svglib _fw would convert it to a fullwidth CJK-range char).
"""
import os
import sys

BUILD = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
EDITION = sys.argv[2] if len(sys.argv) > 2 else os.path.expanduser(
    "~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-tw-ru")
CORE_DIR = "weekly-report-w45-zhtw-core"
ED_DIR = "weekly-report-w45-zh-tw-ru"

PAIRS = []  # (file, old, new)


def add(f, old, new):
    PAIRS.append((f, old, new))


# ---------------- bslib4.py (furniture + gloss prefix) ----------------
add("bslib4.py",
    "Lucerna · 繁體中文週報 VOL.2 · 繁體中文正文 · 英語講解 · Traditional Chinese text · English explanations",
    "Lucerna · КИТАЙСКИЙ (ТРАДИЦИОННЫЙ) ЕЖЕНЕДЕЛЬНИК VOL.2 · ТЕКСТЫ НА КИТАЙСКОМ (ТРАДИЦИОННОМ) · ОБЪЯСНЕНИЯ НА РУССКОМ")
add("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"Страница {n} из {total}"')
add("bslib4.py", '"Notes｜" + s', '"Пояснение — " + s')

# ---------------- content12.py : P1 + P2 ----------------
F = "content12.py"
add(F, "繁體中文正文 · 英語講解 — Traditional Chinese text · Explanations in English · the edition for English-speaking readers",
    "ТЕКСТЫ НА КИТАЙСКОМ (ТРАДИЦИОННОМ) · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ")
add(F, "Staff report · Source: event organisers' press release (Oct 23) and event FAQ",
    "Сообщение редакции · Источник: пресс-релиз организаторов (23 октября) и FAQ мероприятия")
add(F, "Hong Kong FinTech Week x StartmeupHK 2026 opens Monday (Nov 2) and runs to Friday (Nov 6). The main conference and exhibition are at the Hong Kong Convention and Exhibition Centre on Nov 2-3, with 100+ community events through the week. Expect 45,000+ people from 120+ economies, 1,000+ speakers and 800+ exhibitors and start-ups.",
    "Неделя финансовых технологий Гонконга x StartmeupHK 2026 открывается в понедельник (2 ноября) и продлится до пятницы (6 ноября). Главная конференция и выставка пройдут в Гонконгском выставочном центре 2–3 ноября, а в течение недели состоится более 100 общественных мероприятий. Ожидается более 45 000 человек из более чем 120 экономик, более 1 000 спикеров и более 800 экспонентов и стартапов.")
add(F, "The Taipei International Travel Fair (ITF) opens Friday (Nov 6) at noon at the Nangang Exhibition Center and runs to Monday (Nov 9): 123 countries and cities, 1,600 booths, a daily 14:00 mascot parade and travel talks.",
    "Тайбэйская международная туристическая ярмарка (ITF) открывается в пятницу (6 ноября) в полдень в Выставочном центре Нанган и продлится до понедельника (9 ноября): 123 страны и города, 1 600 стендов, ежедневный парад маскотов в 14:00 и лекции о путешествиях.")
add(F, "本週大事 · This week", "本週大事 · Эта неделя")
add(F, "本週一詞 · Word of the week", "本週一詞 · Слово недели")
add(F, "「金融科技」 — fintech: using technology to run financial services, like paying by phone or scanning a code to pay.",
    "「金融科技」 — финтех: технологии в финансовых услугах — например, оплата телефоном или по коду.")
add(F, "快速測驗 · Quick quiz", "快速測驗 · Быстрый тест")
add(F, "FinTech Week opens on Monday, Nov 2.", "Неделя финтеха открывается в понедельник, 2 ноября.")
add(F, "The main conference is at the Hong Kong Convention and Exhibition Centre.", "Главная конференция проходит в Гонконгском выставочном центре.")
add(F, "More than 45,000 people are expected.", "Ожидается более 45 000 человек.")
add(F, "The travel fair opens Friday, Nov 6, at noon.", "Ярмарка открывается в пятницу, 6 ноября, в полдень.")
add(F, "標題填空 · Headline words", "標題填空 · Слова из заголовков")
add(F, "Participants come from 120+ economies.", "Участники приедут из более чем 120 экономик.")
add(F, "More than 800 exhibitors and start-ups take part.", "Участвуют более 800 экспонентов и стартапов.")
add(F, "The travel fair gathers 123 countries and cities.", "Ярмарка собирает 123 страны и города.")
add(F, "The travel fair has 1,600 booths.", "На ярмарке 1 600 стендов.")
add(F, "Saturday, Nov 7 is the Start of Winter solar term.", "Суббота, 7 ноября, — начало зимы по солнечному календарю.")
add(F, "The travel fair runs to Monday, Nov 9.", "Ярмарка продлится до понедельника, 9 ноября.")
add(F, "生活 · Life", "生活 · Жизнь")
add(F, "第 2 版 · 天氣、泡湯、旅展與雙11 · Weather, hot springs, the travel fair and 11.11",
    "第 2 版 · 天氣、泡湯、旅展與雙11 · Погода, горячие источники, ярмарка и 11.11")
add(F, "The northeast monsoon cools northern Taiwan, and Saturday (Nov 7) is Lidong, the Start of Winter: the day winter begins in the 24 solar terms. Many people mark it with a hot, nourishing pot meal.",
    "Северо-восточный муссон охлаждает север Тайваня, а суббота (7 ноября) — Лидун, начало зимы: день, с которого по 24 солнечным терминам начинается зима. Многие отмечают его горячим питательным блюдом из котла.")
add(F, "Autumn and winter are for hot springs and hiking. The travel fair's trail encyclopaedia collects 56 routes, and the 6 Greenways stamp challenge covers the Tamsui-Kavalan, Raknus Selu, Mountain-to-Sea, Centenary, Indigenous and Sugar-Rail trails.",
    "Осень и зима — время горячих источников и походов. Энциклопедия маршрутов ярмарки собирает 56 маршрутов, а испытание с печатями «6 зелёных дорог» охватывает маршруты Тамсуй—Кавалан, Ракнус-Сэлу, «От гор к морю», Столетний, Коренной и Сахарный.")
add(F, "練習例子 · Practice example", "練習例子 · Пример для практики")
add(F, "Practice numbers: NT$2,400 + NT$1,600 = NT$4,000, exactly her budget — so she can buy both.",
    "Числа для практики: NT$2 400 + NT$1 600 = NT$4 000 — ровно по бюджету, так что она может купить обе вещи.")
add(F, "讀懂了嗎? · Did you get it?", "讀懂了嗎? · Поняли?")
add(F, "Lidong, the Start of Winter, is Saturday, Nov 7.", "Лидун, начало зимы, — суббота, 7 ноября.")
add(F, "The northeast monsoon cools northern Taiwan.", "Северо-восточный муссон охлаждает север Тайваня.")
add(F, "The trail encyclopaedia collects 56 routes.", "Энциклопедия маршрутов собирает 56 маршрутов.")
add(F, "The stamp challenge has 6 Greenways.", "В испытании с печатями — 6 зелёных дорог.")
add(F, "Double 11 falls on Wednesday, Nov 11.", "День 11.11 выпадает на среду, 11 ноября.")
add(F, "Before paying, check tax, delivery and returns.", "Перед оплатой проверьте налог, доставку и возврат.")
add(F, "A hot pot meal marks Lidong: 進補.", "Горячее блюдо из котла к Лидуну — это 進補.")
add(F, "Check the jacket: mornings and evenings are cool.", "Проверьте куртку: утром и вечером прохладно.")
add(F, "Autumn and winter are good for hot springs.", "Осень и зима хороши для горячих источников.")
add(F, "Collect stamps on the 6 Greenways.", "Собирайте печати на 6 зелёных дорогах.")
add(F, "Set a budget before Double 11 shopping.", "Определите бюджет перед покупками 11.11.")
add(F, "The Tamsui-Kavalan Trail is one of the 6 Greenways.", "Маршрут Тамсуй—Кавалан — одна из 6 зелёных дорог.")
add(F, "算一算 · Work it out", "算一算 · Посчитайте")
add(F, "2,400 + 1,600 = 4,000, exactly the budget.", "2 400 + 1 600 = 4 000 — ровно по бюджету.")
add(F, "The budget is 4,000 and the total is 4,000: nothing over.", "Бюджет — 4 000, итог — 4 000: превышения нет.")
add(F, "立冬 — the Start of Winter solar term.", "立冬 — солнечный термин начала зимы.")
add(F, "進補 — eating nourishing hot food for winter.", "進補 — питательная горячая еда к зиме.")
add(F, "泡湯 — soaking in a hot spring.", "泡湯 — купание в горячем источнике.")
add(F, "集章 — collecting stamps at set points.", "集章 — сбор печатей в установленных местах.")
add(F, "事實框 · This week's facts", "事實框 · Факты недели")
add(F, "你呢? · Over to you", "你呢? · А вы?")
add(F, "What hot pot would you eat for Lidong? What is in your Double 11 cart?",
    "Какое блюдо из котла вы съели бы к Лидуну? Что лежит в вашей корзине 11.11?")
add(F, "封王優惠 · Champion deals", "封王優惠 · Чемпионские скидки")

# ---------------- content34.py : P3 + P4 ----------------
F = "content34.py"
add(F, "文化 · Culture", "文化 · Культура")
add(F, "第 3 版 · 立冬、鋼雕與沙雕落幕 · Lidong, steel art and the sand festival finale",
    "第 3 版 · 立冬、鋼雕與沙雕落幕 · Лидун, стальное искусство и финал песчаного фестиваля")
add(F, "Lidong is the first solar term of winter: winter begins. People mark it with hot pot dishes like ginger duck, lamb hotpot and sesame chicken — warming food before the cold months.",
    "Лидун — первый солнечный термин зимы: зима начинается. Его отмечают горячими блюдами из котла — уткой с имбирём, бараниной и курицей с кунжутом — согревающей едой перед холодными месяцами.")
add(F, "Kaohsiung's International Steel Sculpture Festival (Oct 23-Nov 22) turns warehouses, factories, the harbour and streets into a stage — SUPER STAGE — with an international forum on making, design and art in daily life.",
    "Международный фестиваль стальной скульптуры в Гаосюне (23 октября — 22 ноября) превращает склады, заводы, гавань и улицы в сцену — SUPER STAGE — с международным форумом о производстве, дизайне и искусстве в повседневной жизни.")
add(F, "The Fulong International Sand Sculpture Art Festival closed Oct 26 after its 19th season (May 29-Oct 26): 40+ sculptures by 15+ artists, built from Fulong's golden sand around film characters from Jurassic World, Shrek, Kung Fu Panda and Back to the Future.",
    "Международный фестиваль песчаной скульптуры в Фулуне закрылся 26 октября после 19-го сезона (29 мая — 26 октября): более 40 скульптур от более чем 15 художников, построенных из золотого песка Фулуна по мотивам персонажей фильмов «Мир юрского периода», «Шрек», «Кунг-фу Панда» и «Назад в будущее».")
add(F, "讀懂了嗎? · Did you get it?", "讀懂了嗎? · Поняли?")
add(F, "Lidong means winter begins.", "Лидун означает начало зимы.")
add(F, "Ginger duck is a typical Lidong dish.", "Утка с имбирём — обычное блюдо к Лидуну.")
add(F, "The steel festival runs Oct 23-Nov 22.", "Фестиваль стали проходит 23 октября — 22 ноября.")
add(F, "The venues include Pier-2's Penglai B3 warehouse.", "Среди площадок — склад B3 Пэнлай в Пир-2.")
add(F, "The sand festival closed on Oct 26.", "Песчаный фестиваль закрылся 26 октября.")
add(F, "The sand festival made 40+ sculptures.", "На песчаном фестивале создали более 40 скульптур.")
add(F, "Lidong is a solar term (節氣).", "Лидун — солнечный термин (節氣).")
add(F, "Sesame chicken is a Lidong dish.", "Курица с кунжутом — блюдо к Лидуну.")
add(F, "Steel is Kaohsiung's material and memory.", "Сталь — материал и память Гаосюна.")
add(F, "Hamasen Railway Park is a venue.", "Железнодорожный парк Хамасэн — одна из площадок.")
add(F, "Fulong's sand is golden.", "Песок Фулуна — золотой.")
add(F, "Jurassic World is one of the film characters.", "«Мир юрского периода» — один из персонажей фильмов.")
add(F, "May 29-31 (3) + Jun 30 + Jul 31 + Aug 31 + Sep 30 + Oct 26 = 151 days.",
    "29–31 мая (3) + 30 июня + 31 июля + 31 августа + 30 сентября + 26 октября = 151 день.")
add(F, "Oct 23-31 (9) + Nov 22 = 31 days.", "23–31 октября (9) + 22 ноября = 31 день.")
add(F, "算一算 · Work it out", "算一算 · Посчитайте")
add(F, "立冬 — the first solar term of winter.", "立冬 — первый солнечный термин зимы.")
add(F, "進補 — nourishing food before winter.", "進補 — питательная еда перед зимой.")
add(F, "鋼雕 — sculpture made of steel.", "鋼雕 — скульптура из стали.")
add(F, "沙雕 — sculpture built from sand.", "沙雕 — скульптура из песка.")
add(F, "節氣小表 · Solar terms", "節氣小表 · Солнечные термины")
add(F, "你呢? · Over to you", "你呢? · А вы?")
add(F, "Have you seen the Fulong sand sculptures? Which film character would you most want to see in sand?",
    "Вы видели песчаные скульптуры Фулуна? Какого киноперсонажа вы больше всего хотели бы увидеть в песке?")
add(F, "鋼雕行程 · Plan your visit", "鋼雕行程 · План посещения")
add(F, "體育 · Sport", "體育 · Спорт")
add(F, "第 4 版 · 台灣大賽封王 · The Taiwan Series is decided", "第 4 版 · 台灣大賽封王 · Тайваньская серия решена")
add(F, "Staff report · Source: TSNA sports news, Oct 26", "Сообщение редакции · Источник: спортивные новости TSNA, 26 октября")
add(F, "The Wei Chuan Dragons beat the CTBC Brothers 6-0 in Game 6 (Oct 26, Taipei Dome) to win the 2026 Taiwan Series 4-2 — the first-ever Dragons-Brothers final and the Dragons' 6th title. Starter C.C. Mercedes threw 8 shutout innings and was named Series MVP.",
    "«Вэйцюань Драгонс» обыграли «CTBC Бразерс» со счётом 6:0 в шестой игре (26 октября, Тайбэй Доум) и выиграли Тайваньскую серию 2026 со счётом 4:2 — первый в истории финал «Драгонс»—«Бразерс» и шестой титул «Драгонс». Стартовый питчер Си Си Мерседес провёл 8 сухих иннингов и был назван самым ценным игроком серии.")
add(F, "棒球詞卡 · Baseball words", "棒球詞卡 · Бейсбольные слова")
add(F, "Four words: 完封 (shutout), 封王 (clinching the title), 全壘打 (home run), MVP (most valuable player).",
    "Четыре слова: 完封 (сухая игра), 封王 (завоевание титула), 全壘打 (хоум-ран), MVP (самый ценный игрок).")
add(F, "第六戰得分走勢 · Game 6 runs by inning — bars drawn in proportion to runs",
    "第六戰得分走勢 · Игра 6: очки по иннингам — столбики пропорциональны очкам")
add(F, "Note: the Dragons did not bat in the bottom of the 9th — leading 6-0 after the top of the 9th, the game was over. 1 + 5 = 6.",
    "Примечание: «Драгонс» не били в нижней половине 9-го иннинга — ведя 6:0 после верхней половины 9-го, игра завершилась. 1 + 5 = 6.")
add(F, "The Dragons won Game 6, 6-0.", "«Драгонс» выиграли шестую игру со счётом 6:0.")
add(F, "The series ended 4-2 to the Dragons.", "Серия завершилась со счётом 4:2 в пользу «Драгонс».")
add(F, "Mercedes threw 8 shutout innings.", "Мерседес провёл 8 сухих иннингов.")
add(F, "Mercedes was named Series MVP.", "Мерседес был назван самым ценным игроком серии.")
add(F, "The Dragons' 6th title in team history.", "Шестой титул «Драгонс» в истории команды.")
add(F, "Three shutouts in one series is a first.", "Три сухие игры в одной серии — впервые.")
add(F, "Game 6 was played at the Taipei Dome.", "Шестая игра прошла в Тайбэй Доуме.")
add(F, "A shutout: the other side scores zero.", "Сухая игра: соперник не набрал ни одного очка.")
add(F, "Winning the title is 封王.", "Завоевание титула — это 封王.")
add(F, "A ball hit out of the park is a home run.", "Мяч, выбитый за пределы поля, — хоум-ран.")
add(F, "Mercedes allowed 1 run in 14 innings.", "Мерседес пропустил 1 очко за 14 иннингов.")
add(F, "The Dragons scored 5 runs in the 8th inning.", "«Драгонс» набрали 5 очков в 8-м иннинге.")
add(F, "看圖答題 · Read the chart", "看圖答題 · Читаем график")
add(F, "The 8th inning: 5 runs, the biggest bar.", "8-й иннинг: 5 очков — самый большой столбик.")
add(F, "1 + 5 = 6 runs in total.", "1 + 5 = 6 очков всего.")
add(F, "完封 — a shutout: the other side scores zero.", "完封 — сухая игра: соперник не набрал ни одного очка.")
add(F, "封王 — clinching the championship.", "封王 — завоевание чемпионства.")
add(F, "全壘打 — a home run.", "全壘打 — хоум-ран.")
add(F, "安打 — a base hit.", "安打 — хит.")
add(F, "系列賽小檔 · Series file", "系列賽小檔 · Досье серии")
add(F, "Which team do you support? Have you ever watched a baseball game live?",
    "За какую команду вы болеете? Вы когда-нибудь смотрели бейсбол вживую?")

# ---------------- content56.py : P5 + P6 ----------------
F = "content56.py"
add(F, "青年 · Youth", "青年 · Молодёжь")
add(F, "第 5 版 · 天母萬聖節回顧、旅展攻略 · Halloween recap and the travel-fair game plan",
    "第 5 版 · 天母萬聖節回顧、旅展攻略 · Итоги Хэллоуина в Тяньму и план ярмарки")
add(F, "Tianmu's Halloween (Oct 25-26, postponed from Oct 24 by the typhoon): the Oct 25 night parade marched from Shin Kong Mitsukoshi Tianmu along Zhongcheng Road to Dayeh Takashimaya, and the Oct 26 main event ran 13:00-20:00 at Tianmu Sports Park, with 250 shops giving treats and 4,500 pumpkin buckets from three department stores.",
    "Хэллоуин в Тяньму (25–26 октября, перенесён с 24 октября из-за тайфуна): ночной парад 25 октября прошёл от универмага «Синьгуан Саньюэ» в Тяньму по улице Чжунчэн до «Дае Такасимая», а главное событие 26 октября проходило с 13:00 до 20:00 в спортивном парке Тяньму: 250 магазинов раздавали угощения и 4 500 тыквенных ведёрок от трёх универмагов.")
add(F, "Travel-fair game plan: watch the shows first (Yamagata flower-hat dance, Korea's JUMP taekwondo-comedy show, the daily 14:00 mascot parade), then compare prices — budget fares often exclude checked baggage, so add that cost before you decide.",
    "План ярмарки: сначала посмотрите шоу (танец с цветочными шляпами Ямагаты, шоу тхэквондо-комедии «JUMP» из Кореи, ежедневный парад маскотов в 14:00), затем сравните цены — бюджетные тарифы часто не включают зарегистрированный багаж, так что добавьте эту стоимость, прежде чем решать.")
add(F, "練習例子 · Practice example", "練習例子 · Пример для практики")
add(F, "Practice numbers: NT$6,200 − NT$1,200 = NT$5,000, exactly his budget.",
    "Числа для практики: NT$6 200 − NT$1 200 = NT$5 000 — ровно по бюджету.")
add(F, "讀懂了嗎? · Did you get it?", "讀懂了嗎? · Поняли?")
add(F, "The night parade marched on Sunday, Oct 25, at 19:00.", "Ночной парад прошёл в воскресенье, 25 октября, в 19:00.")
add(F, "The main event ran 13:00-20:00 at Tianmu Sports Park.", "Главное событие проходило с 13:00 до 20:00 в спортивном парке Тяньму.")
add(F, "250 shops gave treats.", "250 магазинов раздавали угощения.")
add(F, "4,500 pumpkin buckets were given out.", "Было роздано 4 500 тыквенных ведёрок.")
add(F, "The mascot parade runs daily at 14:00.", "Парад маскотов проходит ежедневно в 14:00.")
add(F, "Budget fares often exclude checked baggage.", "Бюджетные тарифы часто не включают зарегистрированный багаж.")
add(F, "The parade marched along Zhongcheng Road.", "Парад прошёл по улице Чжунчэн.")
add(F, "The Tamagotchi 30th anniversary collaboration.", "Совместный проект к 30-летию Тамагочи.")
add(F, "The Yamagata flower-hat dance performs on stage.", "На сцене выступает танец с цветочными шляпами Ямагаты.")
add(F, "Set a budget before Double 11.", "Определите бюджет перед 11.11.")
add(F, "Add baggage fees before comparing fares.", "Добавьте стоимость багажа, прежде чем сравнивать тарифы.")
add(F, "List your cart first, then delete what you do not need.", "Сначала составьте список корзины, затем удалите ненужное.")
add(F, "算一算 · Work it out", "算一算 · Посчитайте")
add(F, "6,200 − 1,200 = 5,000, exactly the budget.", "6 200 − 1 200 = 5 000 — ровно по бюджету.")
add(F, "The parade starts at 19:00; the main event the next day at 13:00.", "Парад начинается в 19:00; главное событие на следующий день — в 13:00.")
add(F, "討糖 — trick-or-treating.", "討糖 — выпрашивание угощений.")
add(F, "踩街 — parading through the streets in costume.", "踩街 — шествие по улицам в костюмах.")
add(F, "南瓜桶 — a pumpkin bucket for treats.", "南瓜桶 — тыквенное ведёрко для угощений.")
add(F, "打卡 — checking in with a photo on social media.", "打卡 — отметка с фото в соцсетях.")
add(F, "天母時間表 · Tianmu schedule", "天母時間表 · Расписание Тяньму")
add(F, "你呢? · Over to you", "你呢? · А вы?")
add(F, "Have you ever worn a Halloween costume? Which character would you most want to be?",
    "Вы когда-нибудь надевали костюм на Хэллоуин? Каким персонажем вы больше всего хотели бы стать?")
add(F, "旅展表演 · Stage shows", "旅展表演 · Выступления")
add(F, "深讀 · Deep read", "深讀 · Глубокое чтение")
add(F, "第 6 版 · 金融科技週深讀 + 讀圖表 · FinTech in depth, and reading a chart",
    "第 6 版 · 金融科技週深讀 + 讀圖表 · Финтех глубже и чтение графика")
add(F, "Staff report · Source: event organisers' press release (Oct 23) and event FAQ",
    "Сообщение редакции · Источник: пресс-релиз организаторов (23 октября) и FAQ мероприятия")
add(F, "Three plus signs: Finance+ (finance plus technology), AI+ (artificial intelligence inside banks, investment and insurance) and global expansion (helping start-ups sell worldwide). The scale — 45,000+ people, 120+ economies, 1,000+ speakers, 800+ exhibitors and start-ups, 30+ delegations, 100+ community events — shows fintech is now a whole-city topic.",
    "Три знака «плюс»: «Финансы+» (финансы плюс технологии), «ИИ+» (искусственный интеллект в банках, инвестициях и страховании) и глобальная экспансия (помощь стартапам в продажах по всему миру). Масштаб — более 45 000 человек, более 120 экономик, более 1 000 спикеров, более 800 экспонентов и стартапов, более 30 делегаций, более 100 общественных мероприятий — показывает, что финтех теперь тема всего города.")
add(F, "旅展每日開放時數 · ITF opening hours per day — bars drawn in proportion to hours",
    "旅展每日開放時數 · Ярмарка: часы работы по дням — столбики пропорциональны часам")
add(F, "Source: published fair hours (Nov 6: 12:00-18:00; Nov 7-9: 10:00-18:00). Total: 30 hours.",
    "Источник: опубликованные часы работы ярмарки (6 ноября: 12:00–18:00; 7–9 ноября: 10:00–18:00). Всего: 30 часов.")
add(F, "看圖答題 · Read the chart", "看圖答題 · Читаем график")
add(F, "Nov 6 is the shortest day: 6 hours.", "6 ноября — самый короткий день: 6 часов.")
add(F, "Nov 8 runs 10:00-18:00: 8 hours.", "8 ноября работает 10:00–18:00: 8 часов.")
add(F, "6 + 8 + 8 + 8 = 30 hours in total.", "6 + 8 + 8 + 8 = 30 часов всего.")
add(F, "Nov 6 opens at noon, not 10:00.", "6 ноября открывается в полдень, а не в 10:00.")
add(F, "深讀測驗 · Deep-read quiz", "深讀測驗 · Глубокий тест")
add(F, "Finance+ means finance plus technology.", "«Финансы+» означает финансы плюс технологии.")
add(F, "AI helps read data, spot risks and answer clients.", "ИИ помогает читать данные, замечать риски и отвечать клиентам.")
add(F, "Global expansion means selling products worldwide.", "Глобальная экспансия означает продажи по всему миру.")
add(F, "More than 1,000 speakers take part.", "Участвуют более 1 000 спикеров.")
add(F, "The main conference runs Nov 2-3.", "Главная конференция проходит 2–3 ноября.")
add(F, "Community events number 100+ through the week.", "Общественных мероприятий за неделю — более 100.")
add(F, "Payments is one of the main-conference topics.", "Платежи — одна из тем главной конференции.")
add(F, "Digital assets is a main-conference topic.", "Цифровые активы — тема главной конференции.")
add(F, "Insurtech is a main-conference topic.", "Иншуртех — тема главной конференции.")
add(F, "The week connects start-ups with the world.", "Неделя связывает стартапы с миром.")
add(F, "Total opening hours: 30.", "Всего часов работы: 30.")
add(F, "Nov 6 opens at noon (12:00).", "6 ноября открывается в полдень (12:00).")
add(F, "The travel fair has 1,600 booths.", "На ярмарке 1 600 стендов.")
add(F, "More than 45,000 people are expected.", "Ожидается более 45 000 человек.")
add(F, "數字一覽 · By the numbers", "數字一覽 · Цифры")
add(F, "比價提醒 · Compare carefully", "比價提醒 · Сравнивайте цены")
add(F, "Example from press reports (Oct 20): Cathay Pacific Taipei-Tokyo return from NT$13,433 including tax, book by Nov 13. Always compare with baggage fees added — and check the live booking result, as prices vary by date.",
    "Пример из сообщений прессы (20 октября): обратный билет «Катай Пасифик» Тайбэй—Токио от NT$13 433 с налогами, бронирование до 13 ноября. Всегда сравнивайте с добавленной стоимостью багажа и проверяйте результат живого бронирования: цены зависят от даты.")

# ---------------- content7.py : P7 ----------------
F = "content7.py"
add(F, "語言 · Language focus", "語言 · Языковой фокус")
add(F, "語言聚焦 · 三個級別,三個主題 · Three levels, three topics", "語言聚焦 · 三個級別,三個主題 · Три уровня, три темы")
add(F, "A2 · 展會的話 · Fair words", "A2 · 展會的話 · Слова о ярмарке")
add(F, "This week's fairs give you four useful words: 旅展 (travel fair), 攤位 (booth), 集章 (stamp-collecting) and 吉祥物大遊行 (mascot parade). Learn them once, and the whole travel fair makes sense.",
    "Четыре полезных слова этой недели: 旅展 (туристическая ярмарка), 攤位 (стенд), 集章 (сбор печатей) и 吉祥物大遊行 (парад маскотов). Выучите их — и вся ярмарка станет понятной.")
add(F, "Four fair words: 旅展, 攤位, 集章, 吉祥物大遊行.", "Четыре слова о ярмарке: 旅展, 攤位, 集章, 吉祥物大遊行.")
add(F, "旅展 is short for 旅行展覽會 (travel exhibition). A 攤位 is one stall inside the fair; the Taipei fair has 1,600 of them. 集章 means collecting stamps at set points — collect all six Greenway stamps and you win a prize.",
    "旅展 — сокращение от 旅行展覽會 (туристическая выставка). 攤位 — стенд внутри ярмарки; на тайбэйской их 1 600. 集章 — сбор печатей: соберите все шесть — и получите приз.")
add(F, "A booth inside the fair is a 攤位.", "Стенд внутри ярмарки — это 攤位.")
add(F, "The mascot parade runs daily at 14:00.", "Парад маскотов проходит ежедневно в 14:00.")
add(F, "Collecting stamps at set points is 集章.", "Сбор печатей в установленных местах — это 集章.")
add(F, "The travel fair is at the Nangang Exhibition Center.", "Ярмарка проходит в Выставочном центре Нанган.")
add(F, "Practise: 「旅展幾點開門？」 ('What time does the fair open?') — Friday opens at noon, other days at 10:00.",
    "Практика: 「旅展幾點開門？」 («Во сколько открывается ярмарка?») — в пятницу в полдень, в остальные дни в 10:00.")
add(F, "B1 · 球賽與節氣 · Games & seasons", "B1 · 球賽與節氣 · Игры и сезоны")
add(F, "Sport and seasons share this week's headlines. Group the words and they stick: winning （封王、完封） and winter （立冬、進補）.",
    "Спорт и сезоны делят заголовки этой недели. Сгруппируйте слова — и они запомнятся: победа （封王、完封） и зима （立冬、進補）.")
add(F, "Group the words: winning (封王/完封), winter (立冬/進補).", "Сгруппируйте слова: победа (封王/完封), зима (立冬/進補).")
add(F, "封王 means clinching the championship; 完封 means shutting the other side out, 0 runs. 立冬 is the solar term that starts winter; 進補 is eating nourishing hot food before the cold months.",
    "封王 означает завоевание чемпионства; 完封 означает сухую игру — соперник не набрал ни одного очка. 立冬 — солнечный термин, начинающий зиму; 進補 — питательная горячая еда перед холодными месяцами.")
add(F, "Winning the title is 封王.", "Завоевание титула — это 封王.")
add(F, "完封 means the other side scores zero.", "完封 означает, что соперник не набрал ни одного очка.")
add(F, "Lidong starts winter.", "Лидун начинает зиму.")
add(F, "Ginger duck is a Lidong dish.", "Утка с имбирём — блюдо к Лидуну.")
add(F, "Memory trick: learn 封王 first, then the way it was won （完封）, then the season it happened in （立冬）.",
    "Приём: сначала 封王 — затем как победа одержана （完封）, затем сезон （立冬）.")
add(F, "B2 · 港台說法 · Local talk", "B2 · 港台說法 · Местная речь")
add(F, "Taiwan and Hong Kong each have their own way of saying things. This week: 打卡 (check in with a photo), 討糖 (trick-or-treat), 踩街 (street parade in costume) and 泡湯 (soak in a hot spring).",
    "Тайвань и Гонконг говорят по-своему. На этой неделе: 打卡 (отметка с фото), 討糖 (выпрашивание угощений), 踩街 (шествие по улицам в костюмах) и 泡湯 (купание в горячем источнике).")
add(F, "Four local words from this issue: 打卡, 討糖, 踩街, 泡湯.", "Четыре местных слова из этого номера: 打卡, 討糖, 踩街, 泡湯.")
add(F, "打卡 started as clocking in at work, but at a fair or festival it means posting a photo to say 'I was here'. 討糖 is what children say at shops at Halloween; 踩街 is the costumed parade itself; 泡湯 is the autumn pleasure of a hot-spring bath.",
    "打卡 начиналось как отметка на работе, а на ярмарке — публикация фото «я был здесь». 討糖 — слова детей в магазинах на Хэллоуин; 踩街 — сам парад в костюмах; 泡湯 — осенняя ванна в горячем источнике.")
add(F, "At a festival, 打卡 means posting a photo to say you were there.", "На фестивале 打卡 означает публикацию фото со смыслом «вы были там».")
add(F, "Trick-or-treating is 討糖.", "Выпрашивание угощений — это 討糖.")
add(F, "踩街 is a costumed street parade.", "踩街 — шествие по улицам в костюмах.")
add(F, "Soaking in a hot spring is 泡湯.", "Купание в горячем источнике — это 泡湯.")
add(F, "You don't need many local sayings — learn four and every outing feels closer.",
    "Четырёх выражений хватит — и каждая прогулка станет ближе.")
add(F, "完勝 means winning big; 完封 means the other side scored zero.", "完勝 — крупная победа; 完封 — ноль у соперника.")
add(F, "Lidong starts winter; the Solstice is the shortest day. Different terms.", "Лидун начинает зиму, а солнцестояние — самый короткий день.")
add(F, "Check the city: FinTech Week opens in Hong Kong, not Taipei.", "Проверьте город: финтех-неделя — в Гонконге, не в Тайбэе.")
add(F, "易錯診所 · Error clinic", "易錯診所 · Клиника ошибок")
add(F, "「先去集章，再去看表演。」 — the frame 先…再… gives the order of two actions: first X, then Y. Make your own: 先比價，再結帳 (compare prices first, then pay).",
    "「先去集章，再去看表演。」 — 先…再…: сначала X, потом Y. Придумайте своё: 先比價，再結帳 (сначала сравните цены, потом платите).")
add(F, "Frame: 先…再… — first X, then Y. Make your own sentence with it.", "Конструкция 先…再… — сначала X, потом Y. Составьте своё предложение.")
add(F, "本週句式 · Sentence frame", "本週句式 · Конструкция недели")
add(F, "An editor's example letter — not a real one. Deferral notice: VOL.1 promised real letters and best page-8 writing from this issue; none publishable had arrived by press time, so the example stays and the invitation stays open.",
    "Пример от редакции — не настоящее письмо. VOL.1 обещал настоящие письма и лучшие сочинения с 8-й страницы с этого номера, но пригодного не поступило: пример остаётся — пишите нам!")
add(F, "讀者園地 · Readers' corner", "讀者園地 · Уголок читателя")
add(F, "本週金句 · Phrases of the week — word for word from this issue's articles",
    "本週金句 · Фразы недели — слово в слово из статей этого номера")
add(F, "Pay by phone, scan to pay, buy insurance online — that is fintech.", "Плати телефоном, сканируй для оплаты, покупай страховку онлайн — это и есть финтех.")
add(F, "123 countries and cities, 1,600 booths.", "123 страны и города, 1 600 стендов.")
add(F, "Buy what you need; don't buy a pile of things you won't use just for a discount.",
    "Покупайте нужное; не покупайте кучу ненужного только ради скидки.")
add(F, "In Kaohsiung, even steel can become a stage.", "В Гаосюне даже сталь может стать сценой.")
add(F, "Fulong's summer came to an end on October 26.", "Лето Фулуна завершилось 26 октября.")
add(F, "A 6-0 shutout of the Brothers, and the Dragons threw the red ribbons.", "Сухая победа 6:0 над «Бразерс» — и «Драгонс» бросают красные ленты.")
add(F, "250 shops giving treats together.", "250 магазинов вместе раздают угощения.")
add(F, "On the fair's first day the doors open only at noon.", "В первый день ярмарки двери открываются только в полдень.")
add(F, '"p. 1"', '"Страница 1"')
add(F, '"p. 2"', '"Страница 2"')
add(F, '"p. 3"', '"Страница 3"')
add(F, '"p. 4"', '"Страница 4"')
add(F, '"p. 5"', '"Страница 5"')
add(F, '"p. 6"', '"Страница 6"')
add(F, "下期預告 · Next week (VOL.3)", "下期預告 · На следующей неделе (VOL.3)")

# ---------------- content8.py : P8 ----------------
F = "content8.py"
add(F, "測驗與答案 · Test & keys", "測驗與答案 · Тест и ответы")
add(F, "第 8 版 · 本週大測驗 + 全部答案 · This week's test and every answer key",
    "第 8 版 · 本週大測驗 + 全部答案 · Большой тест недели и все ответы")
add(F, "A · 判斷對錯 · True or false", "A · 判斷對錯 · Правда или ложь")
add(F, "FinTech Week opens Monday, Nov 2.", "Неделя финтеха открывается в понедельник, 2 ноября.")
add(F, "Lidong is Nov 7, not Nov 6.", "Лидун — 7 ноября, а не 6 ноября.")
add(F, "The Dragons won the series 4-2.", "«Драгонс» выиграли серию со счётом 4:2.")
add(F, "Game 6 ended 6-0, not 6-3.", "Шестая игра завершилась со счётом 6:0, а не 6:3.")
add(F, "The sand festival closed Oct 26.", "Песчаный фестиваль закрылся 26 октября.")
add(F, "The travel fair opens at noon on Nov 6, not 10:00.", "Ярмарка открывается в полдень 6 ноября, а не в 10:00.")
add(F, "B · 本週大測驗 · The big quiz", "B · 本週大測驗 · Большой тест")
add(F, "The main conference is Nov 2-3.", "Главная конференция проходит 2–3 ноября.")
add(F, "The travel fair runs to Monday, Nov 9.", "Ярмарка продлится до понедельника, 9 ноября.")
add(F, "The steel festival runs to Nov 22.", "Фестиваль стали продлится до 22 ноября.")
add(F, "The night parade marched Oct 25 at 19:00.", "Ночной парад прошёл 25 октября в 19:00.")
add(F, "Double 11 is Wednesday, Nov 11.", "День 11.11 — среда, 11 ноября.")
add(F, "Mercedes allowed 1 run in 14 innings.", "Мерседес пропустил 1 очко за 14 иннингов.")
add(F, "The mascot parade runs daily at 14:00.", "Парад маскотов проходит ежедневно в 14:00.")
add(F, "The trail encyclopaedia collects 56 routes.", "Энциклопедия маршрутов собирает 56 маршрутов.")
add(F, "Total opening hours: 6 + 8 + 8 + 8 = 30.", "Всего часов работы: 6 + 8 + 8 + 8 = 30.")
add(F, "The stamp challenge covers 6 Greenways.", "Испытание с печатями охватывает 6 зелёных дорог.")
add(F, "Fintech: technology running financial services.", "Финтех: технологии в финансовых услугах.")
add(F, "Lidong starts winter.", "Лидун начинает зиму.")
add(F, "A shutout: the other side scores zero.", "Сухая игра: соперник не набрал ни одного очка.")
add(F, "Winning the title is 封王.", "Завоевание титула — это 封王.")
add(F, "Trick-or-treating is 討糖.", "Выпрашивание угощений — это 討糖.")
add(F, "Collecting stamps is 集章.", "Сбор печатей — это 集章.")
add(F, "The travel fair is at the Nangang Exhibition Center.", "Ярмарка проходит в Выставочном центре Нанган.")
add(F, "Pier-2 hosts the steel festival.", "Фестиваль стали проходит в Пир-2.")
add(F, "Global expansion: selling products worldwide.", "Глобальная экспансия: продажи по всему миру.")
add(F, "AI inside finance is 人工智慧＋.", "ИИ в финансах — это 人工智慧＋.")
add(F, "D · 讀一讀,答一答 · Read and answer", "D · 讀一讀,答一答 · Читаем и отвечаем")
add(F, "He goes to the travel fair on Friday at noon.", "В пятницу в полдень он идёт на ярмарку.")
add(F, "The parade is at 14:00.", "Парад — в 14:00.")
add(F, "A set of 4 coupons costs 4,100 (list price 8,200).", "Набор из 4 купонов стоит 4 100 (цена по прайсу — 8 200).")
add(F, "He eats ginger duck for Lidong on Saturday.", "В субботу к Лидуну он ест утку с имбирём.")
add(F, "Order: fair, then Lidong pot, then the coupon set for a buffet.", "Порядок: ярмарка, потом блюдо из котла к Лидуну, потом набор купонов на шведский стол.")
add(F, "E · 情景說話 · Say it in context", "E · 情景說話 · Скажи в контексте")
add(F, "The travel fair opens Friday at noon.", "Ярмарка открывается в пятницу в полдень.")
add(F, "Lidong is the first solar term of winter.", "Лидун — первый солнечный термин зимы.")
add(F, "A shutout means the other side scores zero.", "Сухая игра означает, что соперник не набрал ни одного очка.")
add(F, "The mascot parade is at 14:00 daily.", "Парад маскотов — ежедневно в 14:00.")
add(F, "Compare prices first, then pay: 先比價，再結帳.", "Сначала сравните цены, потом платите: 先比價，再結帳.")
add(F, "F · 寫一寫 · Writing", "F · 寫一寫 · Письмо")
add(F, "Writing — there is no single right answer. A {NCHARS}-character model follows.",
    "Письмо — единственно правильного ответа нет. Ниже — образец на {NCHARS} знаков.")
add(F, "Open task - the model answer is printed in section F above ({NCHARS} characters)",
    "(Открытое задание — образец выше, в разделе F ({NCHARS} знаков))")
add(F, "Model answer: ", "Образец ответа: ")
add(F, "答案 · Answer keys — in page order, with a short English note for every item",
    "答案 · Ответы — по страницам: к каждому ответу — короткое пояснение на русском")
add(F, "All notes in English · ✓ = the writing model", "Все примечания на русском · ✓ = образец письма")
add(F, "— Page {pg} —", "— СТРАНИЦА {pg} —")

# ---------------- global instruction words (order matters) ----------------
# "Fill in" hits both section heads and instr= arguments in every file;
# "Match" hits only instr= arguments. "Writing" is handled last so the
# F head (already replaced above) and the F glossline are untouched.
for _f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    add(_f, "Fill in", "Заполните")
for _f in ["content12.py", "content34.py", "content56.py"]:
    add(_f, "Match", "Сопоставьте")
add("content8.py", "Writing", "Напишите")


def main():
    cache = {}

    def read(f):
        if f not in cache:
            with open(os.path.join(BUILD, f), encoding="utf-8") as fh:
                cache[f] = fh.read()
        return cache[f]

    def write(f, text):
        with open(os.path.join(BUILD, f), "w", encoding="utf-8") as fh:
            fh.write(text)
        cache[f] = text

    # Path repointing (tolerant: core path may already be replaced).
    for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py", "render.py"]:
        text = read(f)
        if CORE_DIR in text:
            text = text.replace(CORE_DIR, ED_DIR)
            print(f"repoint {f}: core -> edition dir")
        elif ED_DIR not in text:
            raise SystemExit(f"FAIL path repoint {f}: neither core nor edition dir present")
        write(f, text)
    text = read("render.py")
    if '"Lucerna-VOL2.pdf"' in text:
        text = text.replace('"Lucerna-VOL2.pdf"', '"Lucerna-VOL2-RU.pdf"')
        print("repoint render.py: print PDF name")
    if '"Lucerna-VOL2-web.pdf"' in text:
        text = text.replace('"Lucerna-VOL2-web.pdf"', '"Lucerna-VOL2-RU-web.pdf"')
        print("repoint render.py: web PDF name")
    write("render.py", text)

    total = 0
    for (f, old, new) in PAIRS:
        text = read(f)
        n = text.count(old)
        if n == 0:
            raise SystemExit(f"FAIL {f}: old string not found (count 0): {old[:100]!r}")
        if old == new:
            raise SystemExit(f"FAIL {f}: old == new: {old[:80]!r}")
        text = text.replace(old, new)
        write(f, text)
        total += 1
        print(f"ok {f} x{n}: {old[:60]!r} -> {new[:60]!r}")
    _layout_fixes()
    print(f"TRANSFORM DONE: {total} pairs applied to {BUILD} for {EDITION}")



# ---------------- layout fixes (folded, transform-first) ----------------
# P2 Over-to-you box: Russian question wraps one line deeper than English
# (audit: ink 1326.4 > border 1322.0). Grow the box 230 -> 250 and shift the
# Champion-deals box below it +20 (DE W45 precedent, scoped to P2 by the
# unique Chinese question + by3 line that only P2 has).
# P7 readers box: last Russian line's ink sits 6.5px below the formula
# border (audit: ink 1751.9 > border 1745.4). Add 10px to the formula tail.
def _layout_fixes():
    import os as _os
    _b = BUILD
    _p = _os.path.join(_b, "content12.py")
    _t = open(_p, encoding="utf-8").read()
    _old = ('p.rect(rx, by + 488, CW, 230, fill="#f1ead6", stroke=LINE, sw=1.4)\n'
            'yy = by + 488 + 18\n'
            'p.text(rx + 22, yy + 26, "你呢? · А вы?", 25, "sans", True, OLIVE); yy += 54\n'
            'yy = p.para(rx + 22, yy + 24, "立冬你想吃什麼鍋?雙11你的購物車裡有什麼?", 22.5, "serif", False, INK, CW - 44, 1.36) + 4\n'
            'p.para(rx + 22, yy + 21, "Какое блюдо из котла вы съели бы к Лидуну? Что лежит в вашей корзине 11.11?", 20, "sans", False, GREY, CW - 44, 1.3)\n'
            'by3 = by + 488 + 230 + 18')
    _new = ('p.rect(rx, by + 488, CW, 250, fill="#f1ead6", stroke=LINE, sw=1.4)\n'
            'yy = by + 488 + 18\n'
            'p.text(rx + 22, yy + 26, "你呢? · А вы?", 25, "sans", True, OLIVE); yy += 54\n'
            'yy = p.para(rx + 22, yy + 24, "立冬你想吃什麼鍋?雙11你的購物車裡有什麼?", 22.5, "serif", False, INK, CW - 44, 1.36) + 4\n'
            'p.para(rx + 22, yy + 21, "Какое блюдо из котла вы съели бы к Лидуну? Что лежит в вашей корзине 11.11?", 20, "sans", False, GREY, CW - 44, 1.3)\n'
            'by3 = by + 488 + 250 + 18')
    assert _t.count(_old) == 1, "P2 OT box block not unique/found"
    open(_p, "w", encoding="utf-8").write(_t.replace(_old, _new))
    print("layout: P2 OT box 230 -> 250, champion box +20")
    _p7 = _os.path.join(_b, "content7.py")
    _t7 = open(_p7, encoding="utf-8").read()
    _old7 = 'len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26'
    _new7 = 'len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 36'
    assert _t7.count(_old7) == 1, "P7 readers lh tail not found"
    open(_p7, "w", encoding="utf-8").write(_t7.replace(_old7, _new7))
    print("layout: P7 readers box formula tail +26 -> +36")


if __name__ == "__main__":
    main()
