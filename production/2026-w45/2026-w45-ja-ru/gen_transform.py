# -*- coding: utf-8 -*-
"""Generate transform.py for JA x RU from the JA x FR transform tables.

The FR transform is the proven table for this exact core (same old strings,
same scoped-note machinery). This generator reuses its OLD strings verbatim
and translates every NEW string FR -> RU via FR2RU below; any FR new string
without a RU translation aborts loudly (no silent passthrough). Masthead
badge / readers-corner code lines are replaced by OLD-string match because
their NEW strings are multi-line code, not plain text.
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))
FR = "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-ja-fr-build/transform.py"

RU_BADGE = ("p.text(975, 316, \"日本語版 · VOL.2 · 文化の日 · 紅葉 · 読書週間\", 40, \"serif\", True, INK, anchor=\"middle\")\n"
            "p.text(975, 356, \"ТЕКСТЫ НА ЯПОНСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ\", 19, \"sans\", True, BRICK, anchor=\"middle\")")
LD_RU = ("ld_ru = \"Пример от редакции, а не настоящее письмо. Настоящих писем и лучших сочинений со страницы 8 "
         "к сроку не пришло: всё появится в VOL.3. Пришлите своё письмо на японском — "
         "лучшие письма выйдут в VOL.3!\"")
LH_RU = ("lh = 62 + len(wrap(lt, \"serif\", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld_ru, \"sans\", False, 20, CW - 44)) * 29 + 26 + 16")
PARA_RU = "p.para(bx + 22, yy3 + 20, ld_ru, 20, \"sans\", False, GREY, CW - 44, 1.42)"

SPECIAL_OLD = {
    "p.text(975, 330, \"日本語版 · VOL.2 · 文化の日 · 紅葉 · 読書週間\", 40, \"serif\", True, INK, anchor=\"middle\")": RU_BADGE,
    "ld = \"※この手紙は編集部の例です。締め切りまでに、本当の読者の手紙と第8版の作文の優秀作は届きませんでした。VOL.3に載せます。\"": LD_RU,
    "lh = 62 + len(wrap(lt, \"serif\", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld, \"serif\", False, 20.5, CW - 44)) * 29 + 12 + len(wrap(lcn, \"sans\", False, 20, CW - 44)) * 29 + 26 + 16": LH_RU,
    "yy3 = p.para(bx + 22, yy3 + 20, ld, 20.5, \"serif\", False, GREY, CW - 44, 1.42) + 10\np.para(bx + 22, yy3 + 20, lcn, 20, \"sans\", False, GREY, CW - 44, 1.42)": PARA_RU,
}

FR2RU = {
    # structural
    "weekly-report-w45-ja-fr": "weekly-report-w45-ja-ru",
    "Lucerna-VOL2-FR.pdf": "Lucerna-VOL2-RU.pdf",
    "Lucerna-VOL2-FR-web.pdf": "Lucerna-VOL2-RU-web.pdf",
    '"Lucerna-VOL2-FR.pdf"': '"Lucerna-VOL2-RU.pdf"',
    '"Lucerna-VOL2-FR-web.pdf"': '"Lucerna-VOL2-RU-web.pdf"',
    # GLOBAL types / instructions
    'instr="Formez la phrase"': 'instr="Составьте предложение"',
    'instr="Traduisez"': 'instr="Переведите"',
    'instr="Rédaction"': 'instr="Сочинение"',
    'instr="Vrai ou faux ?"': 'instr="Верно или неверно?"',
    'instr="Complétez"': 'instr="Вставьте слово"',
    'instr="Associez mot et définition"': 'instr="Соотнесите пары"',
    'instr="Événement, lieu et date"': 'instr="Событие, место и дата"',
    '"Texte à trous"': '"Текст с пропусками"',
    '"Choix multiple"': '"Выбор ответа"',
    '"Compléter"': '"Дополните предложение"',
    '"Appariement"': '"Соотнесите пары"',
    '"Former une phrase"': '"Составьте предложение"',
    '"Vrai ou faux"': '"Верно или неверно"',
    '"Traduction"': '"Перевод"',
    '"Rédaction"': '"Сочинение"',
    '"あなたは？ · À vous la parole"': '"あなたは？ · А вы?"',
    '"Réponses page 8 · niveaux mélangés, cherchez par numéro"': '"Ответы на странице 8 · уровни перемешаны, ищите по номеру"',
    # bslib furniture
    '("Note — " + s,': '("Пояснение — " + s,',
    '"Lucerna · HEBDOMADAIRE JAPONAIS VOL.2 · TEXTE EN JAPONAIS · EXPLICATIONS EN FRANÇAIS"': '"Lucerna · ЯПОНСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.2 · ТЕКСТЫ НА ЯПОНСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ"',
    'f"Page {n} sur {total}"': 'f"Страница {n} из {total}"',
    # code-only masthead lines (geometry, not language): identity
    'p.text(975, 248, "Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")': 'p.text(975, 248, "Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")',
    'p.text(975, 390, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")': 'p.text(975, 390, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")',
    'p.hline(MX, RIGHT, 406, INK, 3); p.hline(MX, RIGHT, 413, INK, 1.2)': 'p.hline(MX, RIGHT, 406, INK, 3); p.hline(MX, RIGHT, 413, INK, 1.2)',
    # content12
    '"毎週、日本語で · Chaque semaine · 日本人が読んでいる日本語を読む"': '"毎週、日本語で · Каждую неделю · 日本人が読んでいる日本語を読む"',
    '"Mardi, c\'est la Journée de la culture"': '"Вторник — День культуры"',
    '"Après le jour férié, le week-end des érables arrive · Voir page 3"': '"После праздника — выходные клёнов · См. страницу 3"',
    '"トップニュース · À la une"': '"トップニュース · Главные новости"',
    '"祝日 jour férié · 見頃 le meilleur moment · 暦 calendrier · お届けします vous apporter."': '"祝日 праздник · 見頃 лучшее время · 暦 календарь · お届けします представляем вам."',
    '"数字で見る今週 · En chiffres"': '"数字で見る今週 · В цифрах"',
    '"今すぐ練習 · À vous de jouer"': '"今すぐ練習 · Попробуйте сами"',
    '"Ces quatre sujets structurent ce numéro."': '"Эти четыре темы — основа номера."',
    '"Dates dans les articles ; chiffres approximatifs"': '"Даты — в статьях, цифры приблизительные"',
    '"この号の内容 · Dans ce numéro"': '"この号の内容 · В этом номере"',
    '"今週のことば · Le mot de la semaine"': '"今週のことば · Слово недели"',
    '"ゆる = détendu, sans se forcer."': '"ゆる = спокойно, без напряжения."',
    '"短いニュース · En bref"': '"短いニュース · Коротко"',
    '"クイズ · Quiz éclair"': '"クイズ · Блиц-викторина"',
    '"Lisez la une et choisissez · réponses page 8"': '"Прочитайте первую страницу и выберите · ответы на странице 8"',
    '"レベル A2 · ゆる整え食と暖かい11月 · Cuisine douce et un novembre doux"': '"レベル A2 · ゆる整え食と暖かい11月 · Мягкая еда и тёплый ноябрь"',
    '"蒸す cuire à la vapeur · 並ぶ apparaître en rayon · 食卓 la table du dîner · 超える dépasser."': '"蒸す готовить на пару · 並ぶ появляться на полках · 食卓 обеденный стол · 超える превышать."',
    '"予報 prévisions · 平年 une année moyenne · 季節風 vent saisonnier · 話題 sujet · 値上がり hausses de prix."': '"予報 прогноз · 平年 средний год · 季節風 сезонный ветер · 話題 тема · 値上がり рост цен."',
    '"Et vous ? Par un jour froid, quel nabe aimeriez-vous manger ? Écrivez deux phrases en japonais et envoyez-les-nous."': '"А вы? В холодный день какой набэ вы хотели бы съесть? Напишите два предложения по-японски и пришлите нам."',
    '"季節のことば · Les mots de saison"': '"季節のことば · Слова сезона"',
    '"ゆる整え食の4つの言葉 · Quatre mots pour une cuisine douce"': '"ゆる整え食の4つの言葉 · Четыре слова о мягкой еде"',
    '"un plat en pot unique"': '"блюдо в одном котле"',
    '"un panier vapeur"': '"бамбуковая пароварка"',
    '"détendu, sans se forcer"': '"спокойно, без напряжения"',
    '"mettre le corps et l\'esprit en ordre"': '"приводить тело и душу в порядок"',
    '"練習 · Exercices · page 2"': '"練習 · Упражнения · страница 2"',
    # content34
    '"レベル A2→B1 · 文化の日と金沢 · La Journée de la culture et Kanazawa"': '"レベル A2→B1 · 文化の日と金沢 · День культуры и Канадзава"',
    '"市場 marché · 工芸 artisanat · 光 lumière · 楽しむ apprécier."': '"市場 рынок · 工芸 ремёсла · 光 свет · 楽しむ наслаждаться."',
    '"陶器 poterie · 漆器 laque · 染物 textiles teints · 金箔 feuille d\'or."': '"陶器 керамика · 漆器 лак · 染物 крашеные ткани · 金箔 сусальное золото."',
    '"Et vous ? À quel événement culturel aimeriez-vous aller pour la Journée de la culture ? Écrivez deux phrases en japonais et envoyez-les-nous."': '"А вы? На какое культурное событие вы хотели бы пойти в День культуры? Напишите два предложения по-японски и пришлите нам."',
    '"練習 · Exercices · page 3"': '"練習 · Упражнения · страница 3"',
    '"レベル B1 · 日本シリーズ横浜の2試合 · Les Japan Series : deux matchs à Yokohama"': '"レベル B1 · 日本シリーズ横浜の2試合 · Японская серия: два матча в Иокогаме"',
    '"延長 manches supplémentaires · 逆転 retournement · 同点 égalité · 優勝率 taux de titre."': '"延長 дополнительные иннинги · 逆転 перелом · 同点 ничья · 優勝率 процент титулов."',
    '"総括 bilan · 締め切り date limite · 確認する vérifier."': '"総括 итоги · 締め切り срок сдачи · 確認する проверить."',
    '"日本シリーズの日程 · Calendrier"': '"日本シリーズの日程 · Расписание"',
    '"横浜の2試合の記録 · Les deux matchs de Yokohama, en chiffres"': '"横浜の2試合の記録 · Два матча в Иокогаме в цифрах"',
    '"練習 · Exercices · page 4"': '"練習 · Упражнения · страница 4"',
    # content56
    '"若者・エンタメ · Jeunesse"': '"若者・エンタメ · Молодёжь"',
    '"レベル B1 · ハロウィンと秋まつり · Halloween et fêtes d\'automne"': '"レベル B1 · ハロウィンと秋まつり · Хэллоуин и осенние фестивали"',
    '"罰金 amende · 像 statue · 仮装 déguisement · 守る respecter."': '"罰金 штраф · 像 статуя · 仮装 костюм · 守る соблюдать."',
    '"祭り fête · 週末 week-end · 話題 sujet."': '"祭り фестиваль · 週末 выходные · 話題 тема."',
    '"Et vous ? Que voudriez-vous faire à une fête d\'automne ? Écrivez deux phrases en japonais et envoyez-les-nous."': '"А вы? Что бы вы хотели делать на осеннем фестивале? Напишите два предложения по-японски и пришлите нам."',
    '"練習 · Exercices · page 5"': '"練習 · Упражнения · страница 5"',
    '"レベル B2 · 暖かい11月と秋の旅 · Un novembre doux et les voyages d\'automne"': '"レベル B2 · 暖かい11月と秋の旅 · Тёплый ноябрь и осенние поездки"',
    '"予算 budget · 満足 satisfaction · 観測 observation · 追いかける poursuivre."': '"予算 бюджет · 満足 удовольствие · 観測 наблюдение · 追いかける следовать."',
    '"グラフを読もう · Lire le graphique"': '"グラフを読もう · Читаем график"',
    '"練習用データ · Données d\'exercice"': '"練習用データ · Учебные данные"',
    '"練習 · Exercices · page 6"': '"練習 · Упражнения · страница 6"',
    # content7
    '"ことば · Langue"': '"ことば · Язык"',
    '"言語フォーカス · 三つのレベル、三つのテーマ · Trois niveaux, trois thèmes"': '"言語フォーカス · 三つのレベル、三つのテーマ · Три уровня, три темы"',
    '"読書週間 Semaine de la lecture · 紹介 présentation · 読み聞かせ lecture à voix haute."': '"読書週間 Неделя чтения · 紹介 презентация · 読み聞かせ чтение вслух."',
    '"見頃 le meilleur moment · 紅葉狩り sorties pour voir les feuilles · 落葉 feuilles tombées"': '"見頃 лучшее время · 紅葉狩り поездки смотреть листву · 落葉 опавшая листва"',
    '"〜倍 fois · 〜% pour cent · 〜万食 dizaines de milliers de portions."': '"〜倍 раз · 〜% процентов · 〜万食 десятков тысяч порций."',
    '"まちがい診療所 · Erreurs fréquentes"': '"まちがい診療所 · Частые ошибки"',
    '"Avec 「昨日」, employez le passé."': '"С 「昨日」 — прошедшее время."',
    '"「こと」 nominalise le verbe."': '"С глаголом нужно 「こと」."',
    '"Comptez les lieux avec 「か所」."': '"Места считайте с помощью 「か所」."',
    '"Employez 「で」 pour le lieu de l\'action."': '"Для места действия используйте 「で」."',
    '"今週のフレーム · Modèle de phrase"': '"今週のフレーム · Образец фразы"',
    '"Décomposition : remettre doucement le corps et l\'esprit en ordre."': '"Разбор: мягко навести порядок в себе."',
    '"読者の手紙 · Le courrier des lecteurs"': '"読者の手紙 · Письма читателей"',
    '"今週のフレーズ · Les phrases de la semaine (extraits mot pour mot de ce numéro)"': '"今週のフレーズ · Фразы недели (дословно из этого номера)"',
    '"La Journée de la culture, c\'est mardi 3 novembre."': '"День культуры — вторник, 3 ноября."',
    '"C\'est un novembre japonais lent et doux."': '"Это медленный, размеренный японский ноябрь."',
    '"ゆる veut dire ne pas se forcer, prendre son temps."': '"«ゆる» значит не напрягаться, не торопиться."',
    '"Les ingrédients pour nabe sont apparus en magasin un mois plus tôt."': '"Ингредиенты для набэ появились в магазинах на месяц раньше."',
    '"On peut apprécier ensemble artisanat traditionnel, feuilles d\'automne et lumières."': '"Можно одновременно наслаждаться традиционными ремёслами, осенней листвой и подсветкой."',
    '"SoftBank a commencé par deux victoires d\'affilée."': '"«СофтБанк» начал с двух побед подряд."',
    '"Respectez les règles et passez un joyeux Halloween."': '"Соблюдайте правила — и пусть Хэллоуин будет весёлым!"',
    '"Ceux qui vont voir les feuilles peuvent poursuivre la plus belle période du nord au sud."': '"Едущие смотреть листву следуют за её пиком с севера на юг."',
    '"p. 1"': '"Страница 1"',
    '"p. 2"': '"Страница 2"',
    '"p. 3"': '"Страница 3"',
    '"p. 4"': '"Страница 4"',
    '"p. 5"': '"Страница 5"',
    '"p. 6"': '"Страница 6"',
    '"来週 · La semaine prochaine (VOL.3)"': '"来週 · На следующей неделе (VOL.3)"',
    # content8
    '"テストと答え · Test et réponses"': '"テストと答え · Тест и ответы"',
    '"La Journée de la culture, c\'est le 3 novembre."': '"День культуры — 3 ноября."',
    '"Jeter des déchets coûte 2 000 yens d\'amende."': '"За брошенный мусор — штраф 2 000 иен."',
    '"La Semaine de la lecture commence le 27 octobre. → ___"': '"Неделя чтения начинается 27 октября. → ___"',
    '"Je veux aller à Kobe voir les illuminations des érables. → ___"': '"Я хочу поехать в Кобе посмотреть подсветку клёнов. → ___"',
    'f"Exercice d\'écriture (pas de réponse unique) ; le modèle ({NCHARS} caractères) est ci-dessous."': 'f"Задание на сочинение (единственного ответа нет); образец ({NCHARS} знаков) — ниже."',
    '"(question ouverte — modèle ci-dessous)"': '"(открытое задание — образец ниже)"',
    'f"Modèle dans la section H de cette page ({NCHARS} caractères)"': 'f"Образец — в разделе H этой страницы ({NCHARS} знаков)"',
    '"答え · Réponses — classées par page, cherchez le numéro"': '"答え · Ответы — сгруппированы по страницам: ищите свой номер"',
    '"Une courte explication en français pour chaque réponse · ✓ = exercice avec modèle"': '"Короткое объяснение по-русски к каждому ответу · ✓ = задание с образцом"',
    'f"— Page {pg} —"': 'f"— СТРАНИЦА {pg} —"',
    # NOTES (FR -> RU)
    "La Journée de la culture, c'est le 3 novembre (mardi)": "День культуры — 3 ноября (вторник)",
    "La Semaine de la lecture dure jusqu'au 9 novembre (lundi)": "Неделя чтения — до 9 ноября (понедельник)",
    "見頃 = le meilleur moment": "見頃 = лучшее время",
    "立冬 = le début de l'hiver": "立冬 = начало зимы",
    "Les illuminations de Kobe commencent le 7 (samedi)": "Подсветка в Кобе начинается 7-го (в субботу)",
    "La Journée de la culture propose des événements culturels dans tout le pays": "В День культуры мероприятия проходят по всей стране",
    "立冬, c'est le 7 novembre (samedi)": "立冬 — 7 ноября (суббота)",
    "Les illuminations commencent à Kobe": "Подсветка начинается в Кобе",
    "「ゆる」 = ne pas se forcer": "「ゆる」 = не напрягаться",
    "Les dîners nabe : 1,5 fois plus que l'an dernier": "Ужины с набэ: в 1,5 раза больше, чем в прошлом году",
    "L'annonce date du 21 octobre": "Объявление — 21 октября",
    "Les températures sont au-dessus des moyennes de novembre à janvier": "Температура с ноября по январь выше средней",
    "Les sujets mode et cuisine viennent de la synthèse note": "Темы моды и еды — из подборки note",
    "ゆる = détendu, sans se forcer": "ゆる = спокойно, без напряжения",
    "蒸し器 = un panier vapeur": "蒸し器 = бамбуковая пароварка",
    "整える = mettre en ordre": "整える = приводить в порядок",
    "鍋 = un plat cuisiné dans un seul pot": "鍋 = блюдо в одном котле",
    "Les ingrédients pour nabe sont apparus un mois plus tôt": "Ингредиенты для набэ появились на месяц раньше",
    "Les prévisions de la JMA datent du 20 octobre": "Прогноз Японского метеоагентства — от 20 октября",
    "サクサクdeコパン a dépassé 13 millions de portions": "サクサクdeコパン — больше 13 миллионов порций",
    "ゆる = détendu b": "ゆる = спокойно b",
    "蒸し器 = panier vapeur a": "蒸し器 = пароварка a",
    "麻辣湯 = soupe épicée d": "麻辣湯 = острый суп d",
    "予報 = prévisions météo c": "予報 = прогноз погоды c",
    "L'événement de Suginami est un orchestre familial": "Событие в Сугинами — семейный оркестр",
    "L'exposition d'artisanat : musée d'art d'Ishikawa": "Выставка ремёсел: Художественный музей Исикавы",
    "L'exposition dure jusqu'au 8 novembre": "Выставка — до 8 ноября",
    "L'exposition dure jusqu'au 8 novembre (dimanche)": "Выставка — до 8 ноября (воскресенье)",
    "Les illuminations : château de Kanazawa et Kenrokuen": "Подсветка: замок Канадзава и Кэнрокуэн",
    "市場 = marché": "市場 = рынок",
    "工芸 = artisanat": "工芸 = ремёсла",
    "陶器 = poterie": "陶器 = керамика",
    "金箔 = feuille d'or": "金箔 = сусальное золото",
    "sujet + temps": "подлежащее + время",
    "lieu + で + あります": "место + で + あります",
    "見たい = vouloir voir": "見たい = хотеть увидеть",
    "en famille": "с семьёй",
    "文化の日 = 3 novembre b": "文化の日 = 3 ноября b",
    "工芸展 = musée c": "工芸展 = музей c",
    "オーケストラ = Suginami d": "オーケストラ = Сугинами d",
    "ライトアップ = château de Kanazawa a": "ライトアップ = замок Канадзава a",
    "Match 1 : SoftBank bat DeNA 3–1": "Матч 1: «СофтБанк» — «Ди-Эн-Эй» 3–1",
    "Le home run de 3 points de Tsutsugo a renversé le match 2": "Трёхочковый хоум-ран Цуцуго перевернул матч 2",
    "SoftBank a commencé par deux victoires d'affilée": "«СофтБанк» начал с двух побед подряд",
    "Mener 2–0, c'est gagner le titre dans 73 % des cas": "Старт 2–0 даёт титул в 73 % случаев",
    "DeNA a remporté le titre en 2024": "«Ди-Эн-Эй» выиграла титул в 2024 году",
    "SoftBank a marqué 3 points au match 1": "«СофтБанк» набрал 3 очка в матче 1",
    "SoftBank a marqué 4 points au match 2": "«СофтБанк» набрал 4 очка в матче 2",
    "Le match 1 est allé jusqu'à la 11e manche": "Матч 1 дошёл до 11-го иннинга",
    "Le match 2 est allé jusqu'à la 10e manche": "Матч 2 дошёл до 10-го иннинга",
    "Taux de titre : 73 %": "Процент титулов: 73 %",
    "延長 = le match qui se prolonge": "延長 = затянувшийся матч",
    "Public du match 1 : 33 388": "Зрители матча 1: 33 388",
    "Public du match 2 : 33 432": "Зрители матча 2: 33 432",
    "L'entraîneur Aikawa : un combat en quatre victoires": "Тренер Аикава: борьба за четыре победы",
    "Le match 1 avait lieu samedi": "Матч 1 был в субботу",
    "SoftBank a gagné deux fois d'affilée": "«СофтБанк» выиграл дважды подряд",
    "Le match 2 est aussi allé en manches supplémentaires": "Матч 2 тоже ушёл в дополнительные иннинги",
    "DeNA a gagné en 2024": "«Ди-Эн-Эй» выиграла в 2024 году",
    "Halloween, c'était le 31 octobre (samedi)": "Хэллоуин — 31 октября (суббота)",
    "L'interdiction de boire à Shibuya : de 18 h à 5 h": "Запрет на питьё в Сибуе: с 18 до 5 часов",
    "Jeter des déchets coûte 2 000 yens d'amende": "За брошенный мусор — штраф 2 000 иен",
    "Le festival de cosplay a lieu à Ikebukuro": "Косплей-фестиваль — в Икэбукуро",
    "Le festival de Naka a lieu le 8 novembre (dimanche)": "Фестиваль Нака — 8 ноября (воскресенье)",
    "Halloween, c'était le 31 octobre": "Хэллоуин — 31 октября",
    "L'interdiction commence à 18 h": "Запрет начинается в 18 часов",
    "L'interdiction court jusqu'à 5 h": "Запрет действует до 5 часов",
    "Le festival de Yokohama a lieu le 8 novembre": "Фестиваль в Иокогаме — 8 ноября",
    "Pas d'alcool dans la rue la nuit": "Ночью на улице пить нельзя",
    "L'amende pour déchets date de juin de cette année": "Штраф за мусор — с июня этого года",
    "Le festival a duré du 30 octobre au 1er novembre": "Фестиваль проходил с 30 октября по 1 ноября",
    "Le côté Pacifique reçoit plus de pluie": "На тихоокеанской стороне дождей больше",
    "Voyages à Kyushu : recherches presque doublées en un an": "Поездки на Кюсю: запросов почти вдвое больше, чем год назад",
    "Le budget par voyage a baissé": "Бюджет одной поездки снизился",
    "Les gorges de Naruko sont au plus beau le week-end du 31 octobre au 8 novembre": "Ущелье Наруко прекраснее всего в выходные 31 октября — 8 ноября",
    "La première réponse du graphique est la satisfaction de proximité": "Первый ответ графика — удовольствие от близкого отдыха",
    "Satisfaction de proximité : 38 %": "Удовольствие от близкого отдыха: 38 %",
    "Sources chaudes : 27 %": "Горячие источники: 27 %",
    "Feuilles 21 % moins gastronomie 14 % = 7": "Листва 21 % минус еда 14 % = 7",
    "38 + 27 = 65": "38 + 27 = 65",
    "Les quatre totalisent 100 %": "Все четыре — 100 %",
    "立冬, c'est le 7 novembre": "立冬 — 7 ноября",
    "Les illuminations de Kobe durent jusqu'au 28 décembre": "Подсветка в Кобе — до 28 декабря",
    "Voyages à Kyushu : presque deux fois plus que l'an dernier": "Поездки на Кюсю: почти вдвое больше, чем в прошлом году",
    "Les prévisions de la JMA : plus chaud que la moyenne": "Прогноз Японского метеоагентства: теплее среднего",
    "Novembre s'annonce plus chaud que la moyenne": "Ноябрь ожидается теплее среднего",
    "Les recherches de voyages à Kyushu ont augmenté": "Запросов о поездках на Кюсю стало больше",
    "Le graphique présente des données d'exercice": "На графике — учебные данные",
    "La Semaine de la lecture commence le 27 octobre (mardi)": "Неделя чтения начинается 27 октября (вторник)",
    "La Semaine de la lecture dure jusqu'au 9 novembre": "Неделя чтения — до 9 ноября",
    "Le slogan est 「静かだけど、冒険中。」": "Девиз: 「静かだけど、冒険中。」",
    "Bibliothèque : des présentations de livres": "Библиотека: презентации книг",
    "見頃 = quand les feuilles sont les plus belles": "見頃 = когда листва красивее всего",
    "紅葉狩り = sortir voir les feuilles": "紅葉狩り = ехать смотреть листву",
    "ライトアップ = illuminer la nuit": "ライトアップ = подсвечивать ночью",
    "落葉 = feuilles tombées": "落葉 = опавшая листва",
    "1.5倍 = 50 % de plus que l'an dernier": "1.5倍 = на 50 % больше, чем в прошлом году",
    "73 % ≈ 3 sur 4": "73 % ≈ 3 из 4",
    "サクサクdeコパン a atteint 13 millions de portions": "サクサクdeコパン — 13 миллионов порций",
    "Le match 1 des Japan Series : le 24 octobre (samedi)": "Матч 1 Японской серии: 24 октября (суббота)",
    "Match 2 : SoftBank gagne 4–3": "Матч 2: «СофтБанк» выигрывает 4–3",
    "Les illuminations de Kobe commencent le 7": "Подсветка в Кобе начинается 7-го",
    "Taux de titre pour un départ à 2–0 : 73 %": "Процент титулов при старте 2–0: 73 %",
    "Mardi, Mika va à Kanazawa avec sa famille": "Во вторник Мика едет в Канадзаву с семьёй",
    "À Kanazawa : l'exposition d'artisanat et les illuminations": "В Канадзаве: выставка ремёсел и подсветка",
    "Samedi, elle va à Kobe avec des amis": "В субботу она едет в Кобе с друзьями",
    "Elle veut emprunter 2 livres pour la Semaine de la lecture": "На Неделю чтения она хочет взять 2 книги",
    "sujet + temps + lieu + verbe": "подлежащее + время + место + глагол",
    "employez 「で」 pour le lieu": "для места используйте 「で」",
    "commencer par deux victoires d'affilée": "начать с двух побед подряд",
    "見頃 = le meilleur moment b": "見頃 = лучшее время b",
    "鍋 = plat en pot unique d": "鍋 = блюдо в одном котле d",
    "落葉 = feuilles tombées a": "落葉 = опавшая листва a",
    "予算 = budget c": "予算 = бюджет c",
    "見せてください = veuillez montrer": "見せてください = покажите, пожалуйста",
    "借りられます = pouvoir emprunter (forme potentielle)": "借りられます = можно взять (потенциальная форма)",
    "La Semaine de la lecture : jusqu'au 9 novembre (page 7)": "Неделя чтения: до 9 ноября (страница 7)",
    "「紅葉の本」 est populaire": "「紅葉の本」 популярна",
    "どういたしまして = je vous en prie": "どういたしまして = не за что",
    "Voir page 3": "См. страницу 3",
    "Voir page 5": "См. страницу 5",
    "Voir page 7": "См. страницу 7",
    "Voir page 6": "См. страницу 6",
    "フェンスの中 = à l'intérieur de la clôture": "フェンスの中 = внутри ограды",
    "守って + 〜しましょう = respectez les règles, et…": "守って + 〜しましょう = соблюдайте правила, и…",
    "飲むことができません = ne pas pouvoir boire": "飲むことができません = нельзя пить",
    "": "",
}

HEADER = '''# -*- coding: utf-8 -*-
"""JA core (VOL.2, Chinese explanations) -> JA x RU edition transform.

Re-runnable: reads the PRISTINE W45 JA core build, applies exact-literal
replacements (whole strings, never AST byte offsets, never byte slicing),
and writes the edition build into this directory. Fix rounds edit THIS
file, then re-run: transform.py -> run.py (one process) -> render.py.

Frozen: every Japanese article/stem/option/letter/figure string is copied
byte-identical. Only the explanation layer changes: Chinese notes/glosses/
headers/instructions -> Russian, per the W43 JA x RU shipped precedent
(files/weekly-report-ja-ru). Masthead geometry follows the W43 JA x RU
shipped SVG exactly (wordmark 248, edition 316, badge 356 19pt BRICK,
tagline 390, rules 406/413, dark band 424) — the W43 same-pairing geometry
wins over the core position (wordmark 262) and over the FR sibling's
olive badge colour. P7 phrase page tags follow W43 JA x RU: (Страница N).
"""
import hashlib
import os
import re
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
CORE = os.path.expanduser(
    "~/workspace/goals/lucernaread-social-media-operations/"
    "hidden_files/weekly-report-w45-ja-build")
EDITION = os.path.expanduser(
    "~/workspace/goals/lucernaread-social-media-operations/"
    "files/weekly-report-w45-ja-ru")
CANON_SVGLIB_MD5 = "d73e23b365676c3618d7e060b835eb4d"

# (old, new) applied in order. Longer strings first where one contains another.
'''


def main():
    spec = importlib.util.spec_from_file_location("frt", FR)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    fr_src = open(FR, encoding="utf-8").read()
    tail = fr_src[fr_src.index("def apply_pairs"):]
    out = [HEADER]
    out.append("GLOBAL = [")
    for old, new in m.GLOBAL:
        assert old in SPECIAL_OLD or new in FR2RU, f"GLOBAL untranslated: {new!r}"
        out.append(f"    ({old!r}, {SPECIAL_OLD.get(old, FR2RU.get(new, new))!r}),")
    out.append("]\n")
    out.append("NOTES = [")
    for old, new in m.NOTES:
        assert new in FR2RU, f"NOTES untranslated: {new!r}"
        out.append(f"    ({old!r}, {FR2RU[new]!r}),")
    out.append("]\n")
    out.append("PER_FILE = {")
    for fname, pairs in m.PER_FILE.items():
        out.append(f"    {fname!r}: [")
        for old, new in pairs:
            if old in SPECIAL_OLD:
                ru = SPECIAL_OLD[old]
            else:
                assert new in FR2RU, f"PER_FILE {fname} untranslated: {new!r}"
                ru = FR2RU[new]
            out.append(f"        ({old!r}, {ru!r}),")
        out.append("    ],")
    out.append("}\n")
    out.append(tail)
    open(os.path.join(HERE, "transform.py"), "w", encoding="utf-8").write("\n".join(out))
    print("transform.py written")


if __name__ == "__main__":
    main()
