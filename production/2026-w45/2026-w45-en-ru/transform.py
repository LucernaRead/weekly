# -*- coding: utf-8 -*-
"""W45 EN core -> EN x RU fan-out transform.

Line/literal-based splicing only (never AST byte offsets). Every pair
asserts its occurrence count; the run aborts before writing anything if
any pair misses. Fix rounds append new pairs here and re-run from a
fresh copy of the core build (never hand-edit content files alone).

Furniture follows the W43 EN x RU shipped edition (KIT section 3):
badge in the strapline slot (y=372, 19.5pt bold brick), footer with
ANGLIJSKIJ EZHE NEDELNIK, page line, gloss prefix, P8 separators,
P7 heads and P8 short heads all from that shipped edition.
"""
import os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))
CORE_SVG = "~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-en-core/svg"
ED_SVG = "~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-en-ru/svg"

# (filename, old, new, expected_count; None = replace-all, must occur >= 1)
R = [
    # ---- bslib4: footer + page line + gloss prefix (W43 EN x RU furniture) ----
    ("bslib4.py", '"The Lucerna · 英语周报 VOL.2 · LUCERNA ENGLISH WEEKLY"',
     '"The Lucerna · АНГЛИЙСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.2 · ТЕКСТЫ НА АНГЛИЙСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ"', 1),
    ("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"Страница {n} из 8"', 1),
    ("bslib4.py", '("译注｜" + s, "sans", False, GREY, 20.5, 1.45)',
     '("Пояснение — " + s, "sans", False, GREY, 20.5, 1.45)', 1),
    # ---- type labels (registry only; never printed on the page) ----
    # Scoped with a trailing comma so bilingual section heads (which contain
    # the same word without a comma) are handled by their own full-string pairs.
    ("content12.py", '"完成句子", ', '"Дополнить предложения", ', 11),
    ("content12.py", '"单选", ', '"Выбрать ответ", ', 8),
    ("content12.py", '"句型转换", ', '"Перестроить", ', 4),
    ("content12.py", '"词汇配对",\n', '"Подобрать пары",\n', 1),
    ("content34.py", '"完成句子", ', '"Дополнить предложения", ', 8),
    ("content34.py", '"单选", ', '"Выбрать ответ", ', 12),
    ("content34.py", '"句型转换", ', '"Перестроить", ', 8),
    ("content34.py", '"词汇配对",\n', '"Подобрать пары",\n', 2),
    ("content56.py", '"完成句子", ', '"Дополнить предложения", ', 10),
    ("content56.py", '"单选", ', '"Выбрать ответ", ', 12),
    ("content56.py", '"句型转换", ', '"Перестроить", ', 4),
    ("content56.py", '"词汇配对",\n', '"Подобрать пары",\n', 1),
    ("content56.py", '"图表读数", ', '"Прочитать диаграмму", ', 6),
    ("content7.py", '"跟练", ', '"Потренироваться", ', 1),
    ("content7.py", ', "改错", ', ', "Исправить", ', 4),
    ("content8.py", '"完形填空", ', '"Заполнить пропуски", ', 1),
    ("content8.py", '"单选", ', '"Выбрать ответ", ', 1),
    ("content8.py", '"阅读理解", ', '"Понять текст", ', 1),
    ("content8.py", '"完成句子", ', '"Дополнить предложения", ', 1),
    ("content8.py", '"翻译", ', '"Перевести", ', 1),
    ("content8.py", '"词汇配对",\n', '"Подобрать пары",\n', 1),
    ("content8.py", '"对话补全", ', '"Дополнить диалог", ', 1),
    ("content8.py", ', "写作", ', ', "Сочинение", ', 1),
    # ---- instr labels (printed small grey after the number) ----
    ("content12.py", 'instr="填空"', 'instr="Заполни"', None),
    ("content12.py", 'instr="改写"', 'instr="Перепиши"', None),
    ("content12.py", 'instr="把词和释义配对"', 'instr="Подбери пары"', None),
    ("content34.py", 'instr="填空"', 'instr="Заполни"', None),
    ("content34.py", 'instr="改写"', 'instr="Перепиши"', None),
    ("content34.py", 'instr="把词和释义配对"', 'instr="Подбери пары"', None),
    ("content56.py", 'instr="填空"', 'instr="Заполни"', None),
    ("content56.py", 'instr="改写"', 'instr="Перепиши"', None),
    ("content56.py", 'instr="把词和释义配对"', 'instr="Подбери пары"', None),
    ("content7.py", 'instr="改错"', 'instr="Исправь"', None),
    ("content8.py", 'instr="配对"', 'instr="Подбери пары"', None),
    # ---- shared instruction bridges ----
    ("content12.py", '"读第 2 版文章，选出正确答案。"', '"Прочитай статью на стр. 2 и выбери правильный ответ."', 1),
    ("content34.py", '"读第 3 版文章，选出正确答案。"', '"Прочитай статью на стр. 3 и выбери правильный ответ."', 1),
    ("content34.py", '"读第 4 版文章，选出正确答案。"', '"Прочитай статью на стр. 4 и выбери правильный ответ."', 1),
    ("content56.py", '"读第 5 版文章，选出正确答案。"', '"Прочитай статью на стр. 5 и выбери правильный ответ."', 1),
    ("content56.py", '"读第 6 版文章，选出正确答案。"', '"Прочитай статью на стр. 6 и выбери правильный ответ."', 1),
    ("content34.py", '"用所给词补全句子。"', '"Дополни предложения данными словами."', 2),
    ("content56.py", '"用所给词补全句子。"', '"Дополни предложения данными словами."', 2),
    ("content12.py", '"根据时间，用英语补全句子。"', '"Дополни предложения по-английски, глядя на время."', 1),
    ("content12.py", '"用 be going to + 动词改写（计划与将要发生的事）。"', '"Перепиши с be going to + глагол (планы и то, что произойдёт)."', 1),
    ("content34.py", '"用 be going to 改写。"', '"Перепиши с be going to."', 1),
    ("content34.py", '"用一般过去时改写（比赛已结束的说法）。"', '"Перепиши в простом прошедшем времени (матчи уже закончились)."', 1),
    ("content56.py", '"用现在进行时改写（正在发生的事）。"', '"Перепиши в настоящем длительном времени (то, что происходит сейчас)."', 1),
    ("content56.py", '"读上面的教学图表，选出正确答案。"', '"Прочитай учебную диаграмму выше и выбери правильный ответ."', 1),
]

R += [
    # ================= P1 =================
    ("content12.py", '"WEEKLY IN ENGLISH · 每周一期 · 读美国人正在读的英语"',
     '"WEEKLY IN ENGLISH · КАЖДУЮ НЕДЕЛЮ · АНГЛИЙСКИЙ, КОТОРЫЙ ЧИТАЕТ АМЕРИКА"', 1),
    ("content12.py", '"英 语 周 报 · VOL.2 · 选 票 · 足 球 · 电 影"',
     '"АНГЛИЙСКИЙ ЕЖЕНЕДЕЛЬНИК · VOL.2 · ВЫБОРЫ · ФУТБОЛ · КИНО"', 1),
    # badge replaces the strapline slot (W43 EN x RU geometry: y=372, 19.5pt bold brick)
    ("content12.py", 'p.text(975, 372, "THE LEARNERS\' WEEKLY — REAL LIFE, IN ENGLISH, FROM AMERICA", 19, "sans", False, GREY, anchor="middle")',
     'p.text(975, 372, "ТЕКСТЫ НА АНГЛИЙСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ", 19.5, "sans", True, BRICK, anchor="middle")', 1),
    ("content12.py", '"周二选举日 · 周日已拨回时钟"', '"Вторник — день выборов · В воскресенье часы перевели назад"', 1),
    ("content12.py", '"11 月 3 日周二选举日 · 详见第 6 版"', '"День выборов, вторник 3 ноября · Стр. 6"', 1),
    ("content12.py", '"THE BIG STORY · 头条"', '"THE BIG STORY · Главная тема"', 1),
    ("content12.py", '"讲解｜a midterm 中期选举 · a ballot 选票 · a race 一场竞选 · to call a race 宣布某场竞选的结果。"',
     '"a midterm: промежуточные выборы · a ballot: бюллетень · a race: предвыборная гонка · to call a race: объявить итог гонки."', 1),
    ("content12.py", '"THE WEEK IN NUMBERS · 数字看本周"', '"THE WEEK IN NUMBERS · Неделя в цифрах"', 1),
    ("content12.py", '"Nov 3 — Election Day（选举日） · 435 — seats in the House, all on the ballot（众议院全部席位改选）"',
     '"Nov 3 — Election Day (день выборов) · 435 — seats in the House, all on the ballot (все места в Палате представителей переизбираются)"', 1),
    ("content12.py", '"Nov 6 — two films open（两部电影上映） · Nov 8 — NFL in Madrid + F1 in São Paulo（周日两场大赛）"',
     '"Nov 6 — two films open (две премьеры) · Nov 8 — NFL in Madrid + F1 in São Paulo (два больших матча в воскресенье)"', 1),
    ("content12.py", '"TRY IT NOW · 即学即练"', '"TRY IT NOW · Попробуй сразу"', 1),
    ("content12.py", '"ballot = 纸选票"', '"ballot = бюллетень"', 1),
    ("content12.py", '"midterm = 中期（选举）"', '"midterm = промежуточные (выборы)"', 1),
    ("content12.py", '"选举日 11 月 3 日（周二）"', '"день выборов, вторник 3 ноября"', 1),
    ("content12.py", '"early voting = 提前投票"', '"early voting = досрочное голосование"', 1),
    ("content12.py", '"race called = 宣布结果"', '"race called = итог объявлен"', 1),
    ("content12.py", '"take time = 花时间"', '"take time = занимать время"', 1),
    ("content12.py", '"本周美国热搜 · Google Trends 美国区快照"', '"Что ищут в США · Снимок Google Trends США"', 1),
    ("content12.py", '"相对热度示意，非精确搜索量。"', '"Относительный интерес, а не точные цифры."', 1),
    ("content12.py", '"IN THIS ISSUE · 本期目录"', '"IN THIS ISSUE · В этом номере"', 1),
    ("content12.py", '"（任期）中期。midterm election 中期选举。"', '"Середина срока: midterm election."', 1),
    ("content12.py", '"IN BRIEF · 快讯"', '"IN BRIEF · Коротко"', 1),
    ("content12.py", '"LIGHTNING QUIZ · 闪电问答"', '"LIGHTNING QUIZ · Блиц-опрос"', 1),
    ("content12.py", '"读头版，选出正确答案 · 答案见第 8 版"', '"Прочитай первую страницу и выбери правильный ответ · Ответы на стр. 8"', 1),
    ("content12.py", '"选举日 11 月 3 日周二"', '"день выборов, вторник 3 ноября"', 1),
    ("content12.py", '"众议院 435 席全部改选"', '"все 435 мест в Палате переизбираются"', 1),
    ("content12.py", '"美国 11 月 1 日拨回时钟"', '"США перевели часы назад 1 ноября"', 1),
    ("content12.py", '"NFL 马德里赛 11 月 8 日周日"', '"матч NFL в Мадриде, воскресенье 8 ноября"', 1),
    # ================= P2 =================
    ("content12.py", 'p.band("LIFE · 生活", "The Lucerna", "LEVEL A2 · Clocks, candy & your week · 时钟、糖果与你的一周")',
     'p.band("LIFE · Жизнь", "The Lucerna", "LEVEL A2 · Clocks, candy & your week · Часы, конфеты и твоя неделя")', 1),
    ("content12.py", '"DO THE MATHS · 算一算"', '"DO THE MATHS · Посчитай"', 1),
    ("content12.py", '"讲解｜to fall back （时钟）拨回 · a costume 服装、装扮 · trick or treat 不给糖就捣蛋。"',
     '"to fall back (о часах) переводить назад · a costume костюм · trick or treat «сладость или гадость»."', 1),
    ("content12.py", '"周日你多睡了一小时吗？写两句英语寄给编辑部。"', '"В воскресенье ты спал на час дольше? Напиши в редакцию два предложения по-английски."', 2),
    ("content12.py", '"AND YOU ? · 说说你自己"', '"AND YOU ? · А ты?"', 1),
    ("content12.py", '"TELLING THE TIME · 这样报时间"', '"TELLING THE TIME · Как называть время"', 1),
    ("content12.py", '"The repeated hour · 本周的三个时间"', '"The repeated hour · Три времени недели"', 1),
    ("content12.py", '"= two times（两次）"', '"= two times (дважды)"', 1),
    ("content12.py", '"= one more time（再一次）"', '"= one more time (ещё раз)"', 1),
    ("content12.py", '"= to go back one hour（拨回）"', '"= to go back one hour (перевести назад)"', 1),
    ("content12.py", '"= one hour more（多出一小时）"', '"= one hour more (на час больше)"', 1),
    ("content12.py", '"EXERCISES · 第 2 版练习"', '"EXERCISES · Упражнения стр. 2"', 1),
    ("content12.py", '"答案见第 8 版 · 题目可跨级混排，按题号找答案"', '"Ответы на стр. 8 · Упражнения разных уровней; ищи по номеру"', 1),
    ("content12.py", '"1:00 = 一点整"', '"1:00 = ровно час"', 1),
    ("content12.py", '"1:30 = 一点半"', '"1:30 = половина второго"', 1),
    ("content12.py", '"7:45 = 差一刻八点"', '"7:45 = без четверти восемь"', 1),
    ("content12.py", '"两次 = twice"', '"дважды = twice"', 1),
    ("content12.py", '"多出的 = extra"', '"лишний = extra"', 1),
    ("content12.py", '"Americans 复数 → are going to"', '"Americans, мн. ч. → are going to"', 1),
    ("content12.py", '"疑问句：be 提前"', '"вопрос: be в начале"', 1),
    ("content34.py", '"疑问句：be 提前"', '"вопрос: be в начале"', 1),
    ("content12.py", '"11 月 1 日凌晨 2 点拨回 1 点"', '"1 ноября, с 2 часов на 1 час"', 1),
    ("content12.py", '"亚利桑那与夏威夷不拨钟"', '"Аризона и Гавайи часы не переводят"', 1),
    ("content12.py", '"万圣节 10 月 31 日周六"', '"Хэллоуин, суббота 31 октября"', 1),
    ("content12.py", '"11 月 1 日夜晚有 25 小时"', '"ночь 1 ноября длится 25 часов"', 1),
    ("content12.py", '"costume=装扮 b"', '"costume=костюм b"', 1),
    ("content12.py", '"extra hour=多出一小时 a"', '"extra hour=лишний час a"', 1),
    ("content12.py", '"fall back=拨回 d"', '"fall back=перевести назад d"', 1),
    ("content12.py", '"trick or treat=不给糖就捣蛋 c"', '"trick or treat=«сладость или гадость» c"', 1),
]

R += [
    # ================= P3 =================
    ("content34.py", 'p.band("CULTURE · 文化", "The Lucerna", "A2 → B1 · Friday at the movies · 周五看电影")',
     'p.band("CULTURE · Культура", "The Lucerna", "A2 → B1 · Friday at the movies · В пятницу — в кино")', 1),
    ("content34.py", '"AT HOME THIS WEEK · 在家看什么"', '"AT HOME THIS WEEK · Что смотреть дома"', 1),
    ("content34.py", '"讲解｜to open （电影）上映 · a monster 怪物 · a catchphrase 口头禅、金句 · a series 剧集。"',
     '"to open (о фильме) выйти в прокат · a monster чудовище · a catchphrase крылатая фраза · a series сериал."', 1),
    ("content34.py", '"猫咪电影 11 月 6 日周五上映"', '"фильм про Кота выходит в пятницу 6 ноября"', 1),
    ("content34.py", '"猫出自苏斯博士的书"', '"Кот — из книги доктора Сьюза"', 1),
    ("content34.py", '"比尔·黑德为猫配音"', '"Кота озвучивает Билл Хейдер"', 1),
    ("content34.py", '"哥斯拉导演是山崎贵"', '"режиссёр «Годзиллы» — Такаси Ямадзаки"', 1),
    ("content34.py", '"《黑鸽》第二季 11 月 5 日上线"', '"второй сезон «Чёрных голубей» выходит 5 ноября"', 1),
    ("content34.py", '"周日重聚节目收尾"', '"воскресный выпуск-воссоединение завершает неделю"', 1),
    ("content34.py", '"open = 上映（第三人称单数加 s）"', '"open = выйти в прокат (3-е лицо ед. ч. + s)"', 1),
    ("content34.py", '"tall → taller 比较级"', '"tall → taller, сравнительная степень"', 1),
    ("content34.py", '"loud → louder"', '"loud → louder"', 1),
    ("content34.py", '"split = 分歧的"', '"split = расколотый"', 1),
    ("content34.py", '"monster=怪物 b"', '"monster=чудовище b"', 1),
    ("content34.py", '"catchphrase=金句 a"', '"catchphrase=крылатая фраза a"', 1),
    ("content34.py", '"series=剧集 d"', '"series=сериал d"', 1),
    ("content34.py", '"open=上映 c"', '"open=выйти в прокат c"', 1),
    ("content34.py", '"THE CAT\'S HAT · 猫的帽子"', '"THE CAT\'S HAT · Шляпа Кота"', 1),
    ("content34.py", '"五句影评｜who、where、发生了什么、转折、结局——五句就够。"',
     '"Пять фраз рецензии: кто, где, что случилось, поворот, финал — пяти хватит."', 1),
    # ================= P4 =================
    ("content34.py", 'p.band("SPORT · 体育", "The Lucerna", "LEVEL B1 · NFL · F1 · NASCAR · WTA · Boxing")',
     'p.band("SPORT · Спорт", "The Lucerna", "LEVEL B1 · NFL · F1 · NASCAR · WTA · Boxing")', 1),
    ("content34.py", '"WHY MADRID ? · 为什么去马德里？"', '"WHY MADRID ? · Почему Мадрид?"', 1),
    ("content34.py", '"讲解｜a fixture 一场比赛（赛程） · a title 冠军头衔 · to defend （卫冕）保卫头衔 · a fan 球迷。"',
     '"a fixture матч по расписанию · a title чемпионский титул · to defend (о чемпионе) защищать титул · a fan болельщик."', 1),
    ("content34.py", '"马德里赛：孟加拉虎对猎鹰"', '"Мадрид: «Бенгалс» против «Фэлконс»"', 1),
    ("content34.py", '"马德里赛场是伯纳乌"', '"стадион в Мадриде — «Бернабеу»"', 1),
    ("content34.py", '"海豚对雄狮在迈阿密"', '"«Долфинс» против «Лайонс» в Майами"', 1),
    ("content34.py", '"F1 圣保罗大奖赛在巴西"', '"Гран-при Сан-Паулу «Формулы-1» в Бразилии"', 1),
    ("content34.py", '"WTA 年终总决赛在印第安维尔斯开赛"', '"Итоговый турнир WTA начинается в Индиан-Уэлсе"', 1),
    ("content34.py", '"拳击赛在阿灵顿"', '"бокс — в Арлингтоне"', 1),
    ("content34.py", '"defend 三单加 s"', '"defend, 3-е лицо ед. ч. + s"', 1),
    ("content34.py", '"与第 4 版原文一致，复数动词"', '"как в статье на стр. 4, глагол во мн. ч."', 1),
    ("content34.py", '"big → bigger"', '"big → bigger"', 1),
    ("content34.py", '"fast → faster"', '"fast → faster"', 1),
    ("content34.py", '"fixture=赛程中的比赛 b"', '"fixture=матч по расписанию b"', 1),
    ("content34.py", '"title=冠军头衔 d"', '"title=чемпионский титул d"', 1),
    ("content34.py", '"fan=球迷 a"', '"fan=болельщик a"', 1),
    ("content34.py", '"defend=卫冕 c"', '"defend=защищать титул c"', 1),
    ("content34.py", '"play → played"', '"play → played"', 1),
    ("content34.py", '"watch → watched"', '"watch → watched"', 1),
    ("content34.py", '"follow → followed"', '"follow → followed"', 1),
    ("content34.py", '"choose → chose"', '"choose → chose"', 1),
    ("content34.py", '"SUNDAY, NOVEMBER 8 · 周日赛程"', '"SUNDAY, NOVEMBER 8 · Воскресенье"', 1),
    ("content34.py", '"看球英语｜比分、谁得分、谁领先——短句就是直播英语。"',
     '"Язык матча: счёт, кто забил, кто ведёт — короткие фразы, как в прямом эфире."', 1),
    # ================= P5 =================
    ("content56.py", 'p.band("YOUTH · 青年", "The Lucerna", "LEVEL B1 · Election night at home · 选举之夜")',
     'p.band("YOUTH · Молодёжь", "The Lucerna", "LEVEL B1 · Election night at home · Ночь выборов дома")', 1),
    ("content56.py", '"TOO CLOSE TO CALL · 难分胜负"', '"TOO CLOSE TO CALL · Равная борьба"', 1),
    ("content56.py", '"讲解｜a map （选举）地图 · too close to call 难分胜负、无法判定 · a second screen 第二块屏幕（手机）。"',
     '"a map (о выборах) карта · too close to call слишком равная борьба, итог неясен · a second screen второй экран (телефон)."', 1),
    ("content56.py", '"地图随结果逐州变色"', '"карта меняет цвет штат за штатом"', 1),
    ("content56.py", '"too close to call = 尚不知晓"', '"too close to call = итог ещё неизвестен"', 1),
    ("content56.py", '"选举夜常吃披萨"', '"в ночь выборов часто едят пиццу"', 1),
    ("content56.py", '"第二屏是手机"', '"второй экран — телефон"', 1),
    ("content56.py", '"孩子问为什么这么久"', '"дети спрашивают, почему так долго"', 1),
    ("content56.py", '"结果早上还在"', '"результаты будут и утром"', 1),
    ("content56.py", '"close = 接近的"', '"close = равный"', 1),
    ("content56.py", '"still = 仍然"', '"still = всё ещё"', 1),
    ("content56.py", '"与第 5 版原文一致，单数"', '"как в статье на стр. 5, ед. ч."', 2),
    ("content56.py", '"map=选举地图 c"', '"map=карта выборов c"', 1),
    ("content56.py", '"race=一场竞选 d"', '"race=гонка d"', 1),
    ("content56.py", '"result=结果 b"', '"result=результат b"', 1),
    ("content56.py", '"call=宣布胜者 a"', '"call=объявить победителя a"', 1),
    ("content56.py", '"change → is changing"', '"change → is changing"', 1),
    ("content56.py", '"send → are sending"', '"send → are sending"', 1),
    ("content56.py", '"watch → are watching"', '"watch → are watching"', 1),
    ("content56.py", '"wait → is waiting"', '"wait → is waiting"', 1),
    ("content56.py", '"FIVE SENTENCES · 五句话作业"', '"FIVE SENTENCES · Пять предложений"', 1),
    ("content56.py", '"投票结束｜The polls have closed = 该州投票已结束，计票开始。"',
     '"Голосование окончено: The polls have closed = в этом штате голосование завершено, начинается подсчёт."', 1),
    # ================= P6 =================
    ("content56.py", 'p.band("DEEP READ · 时事深读", "The Lucerna", "LEVEL B2 · How America votes · 美国怎么投票")',
     'p.band("DEEP READ · Глубокое чтение", "The Lucerna", "LEVEL B2 · How America votes · Как голосует Америка")', 1),
    ("content56.py", '"A PRACTICE BALLOT · 模拟选票"', '"A PRACTICE BALLOT · Пробный бюллетень"', 1),
    ("content56.py", '"讲解｜to register 登记（选民登记） · a governor 州长 · to shape laws 影响立法 · patience 耐心。"',
     '"to register зарегистрироваться (регистрация избирателей) · a governor губернатор · to shape laws влиять на законы · patience терпение."', 1),
    ("content56.py", '"READ THE CHART · 读图表"', '"READ THE CHART · Читай диаграмму"', 1),
    ("content56.py", '"38% 选“不用排队”"', '"38% выбирают «без очереди»"', 1),
    ("content56.py", '"工作原因 29%"', '"работа — 29%"', 1),
    ("content56.py", '"四项合计 100%"', '"в сумме четыре пункта — 100%"', 1),
    ("content56.py", '"习惯最少 12%"', '"привычка — всего 12%"', 1),
    ("content56.py", '"不用排队比旅行多 17 个百分点"', '"«без очереди» опережает «поездки» на 17 пунктов"', 1),
    ("content56.py", '"图表是教学数据非真实民调"', '"диаграмма — учебный материал, а не настоящий опрос"', 1),
    ("content56.py", '"各州自行组织选举"', '"каждый штат сам организует выборы"', 1),
    ("content56.py", '"众议员任期两年"', '"депутаты служат два года"', 1),
    ("content56.py", '"参议员任期六年、每次约三分之一改选"', '"сенаторы служат шесть лет; около трети переизбирается каждый раз"', 1),
    ("content56.py", '"邮寄选票计票需时间"', '"подсчёт голосов по почте занимает время"', 1),
    ("content56.py", '"本期不印民调与预测"', '"в этом номере нет опросов и прогнозов"', 1),
    ("content56.py", '"耐心是制度的一部分"', '"терпение — часть системы"', 1),
    ("content56.py", '"shape = 影响、塑造"', '"shape = влиять, формировать"', 1),
    ("content56.py", '"register = 登记"', '"register = зарегистрироваться"', 1),
    ("content56.py", '"patience = 耐心"', '"patience = терпение"', 1),
    ("content56.py", '"optional = 可选的"', '"optional = необязательный"', 1),
    ("content56.py", '"differ 三单 differs"', '"differ, 3-е лицо ед. ч.: differs"', 1),
    ("content56.py", '"private = 私密的"', '"private = тайный"', 1),
    ("content56.py", '"HOW LONG ? · 任期多长？"', '"HOW LONG ? · Срок полномочий"', 1),
    ("content56.py", '"一张地图｜五十个州、五十套规则——所以选举夜看的是地图，不是一个数字。"',
     '"Одна карта: пятьдесят штатов — пятьдесят правил; поэтому в ночь выборов смотрят на карту, а не на одно число."', 1),
]

R += [
    # ================= P7 =================
    ("content7.py", 'p.band("LANGUAGE IN HAND · 精讲", "The Lucerna", "A2 → B2 · Phrases of the week · 本周金句")',
     'p.band("LANGUAGE IN HAND · Разбор", "The Lucerna", "A2 → B2 · Phrases of the week · Фразы недели")', 1),
    ("content7.py", '"LEVEL A2 · 基础"', '"LEVEL A2 · База"', 1),
    ("content7.py", '"LEVEL B1 · 进阶"', '"LEVEL B1 · Средний"', 1),
    ("content7.py", '"LEVEL B2 · 挑战"', '"LEVEL B2 · Сложный"', 1),
    ("content7.py", '"THE EXAMPLE · 例句"', '"THE EXAMPLE · Пример"', 3),
    # B2 example box: quoted English sentence verbatim; only the gloss localised.
    ("content7.py", '"« Patience is part of the system, not a failure of it. » — part of = 一部分 (page 6)."',
     '"« Patience is part of the system, not a failure of it. » — part of = часть (page 6)."', 1),
    ("content7.py", '"THE TOOLBOX · 工具箱"', '"THE TOOLBOX · Инструменты"', 1),
    ("content7.py", '"工具箱｜本期三句随身句，按级各一；金句全部出自本期文章，回读原文最有效。"',
     '"Три фразы на каждый день, по одной на уровень; все фразы недели — из статей этого номера: перечитай оригинал, и они запомнятся."', 1),
    ("content7.py", '"PHRASES OF THE WEEK · 本周金句（全部出自本期文章）"', '"PHRASES OF THE WEEK · Фразы недели"', 1),
    ("content7.py", '"每句一个语法点 + 一道小题 · 答案见第 8 版"', '"К каждой фразе — грамматика и вопрос · Ответы на стр. 8"', 1),
    # phrase grammar points: W43 EN x RU phrase slot renders them with the
    # GRAMMATIKA prefix (verified in the shipped W43 P7 SVG).
    ("content7.py", '"语法点｜is = 是；日期作主语补足语。"', '"Грамматика — is = быть; дата — именная часть сказуемого."', 1),
    ("content7.py", '"语法点｜happen 的过去式是 happened，规则变化。"', '"Грамматика — прошедшее время happen — happened, правильное образование."', 1),
    ("content7.py", '"语法点｜would + 动词原形，表选择意愿。"', '"Грамматика — would + инфинитив выражает предпочтение."', 1),
    ("content7.py", '"语法点｜that is = 那就是；破折号后总结。"', '"Грамматика — that is = то есть; после тире — итог."', 1),
    ("content7.py", '"语法点｜will still = 仍然会；still 放在 will 之后。"', '"Грамматика — will still = всё ещё; still стоит после will."', 1),
    ("content7.py", '"语法点｜part of = ……的一部分；not 表否定对照。"', '"Грамматика — part of = часть; not даёт противопоставление."', 1),
    ("content7.py", '"语法点｜not every + 单数动词：并非每处都变。"', '"Грамматика — not every + глагол в ед. ч.: меняется не всё."', 1),
    ("content7.py", '"语法点｜has = 有；the week 单数用 has。"', '"Грамматика — has = иметь; the week в ед. ч. требует has."', 1),
    ("content7.py", '"is 是"', '"is = быть"', 1),
    ("content7.py", '"would + 原形"', '"would + инфинитив"', 1),
    ("content7.py", '"that is 那就是"', '"that is = то есть"', 1),
    ("content7.py", '"will still 仍然会"', '"will still = всё ещё"', 1),
    ("content7.py", '"is part of 一部分"', '"is part of = часть"', 1),
    ("content7.py", '"THE ERROR CLINIC · 易错诊所"', '"THE ERROR CLINIC · Ошибки"', 1),
    ("content7.py", '"每句有一处错误：找出来并改正。"', '"В каждой фразе одна ошибка: найди и исправь её."', 1),
    ("content7.py", '"三单否定用 doesn\'t + 原形"', '"отрицание в 3-м лице: doesn\'t + инфинитив"', 1),
    ("content7.py", '"fall 的过去式是 fell"', '"прошедшее время fall — fell"', 1),
    ("content7.py", '"bigger 已含比较级，不要再加 more"', '"bigger уже сравнительная степень: more не нужно"', 1),
    ("content7.py", '"going to 后用动词原形"', '"после going to — инфинитив"', 1),
    ("content7.py", '"READERS\' CORNER · 读者园地"', '"READERS\' CORNER · Уголок читателя"', 1),
    # Readers' corner: the English letter paragraph is FROZEN verbatim (core's own
    # honestly-labelled example). Only the Chinese disclosure paragraph is localised:
    # it states the 3 facts (no real letters / no best VOL.1 p.8 text / example +
    # promise deferred to VOL.3) plus an explicit imperative invitation.
    ("content7.py", '"编辑说明｜VOL.1 曾承诺 VOL.2 刊登真实来信，但截至发稿编辑部未收到真实来信与 VOL.1 写作投稿，故本期如实说明、不虚构来信；请把你的来信与写作寄来，VOL.3 起刊登收到的真实来信。"',
     '"Примечание редакции: в VOL.1 было обещано публиковать настоящие письма в VOL.2, но к сдаче номера редакция не получила ни настоящих писем, ни лучшего сочинения с 8-й страницы VOL.1; мы ничего не выдумываем, а пример остаётся помеченным. Присылайте ваши письма и сочинения! В VOL.3 мы опубликуем полученные письма."', 1),
    ("content7.py", '"NEXT WEEK · VOL.3 下周预告"', '"NEXT WEEK · VOL.3 · Анонс"', 1),
    ("content7.py", '"下周三退伍军人节，周日 NFL 慕尼黑赛；还有中期选举结果报道。"',
     '"В среду — День ветеранов; в воскресенье — матч NFL в Мюнхене; а также итоги промежуточных выборов."', 1),
    # ================= P8 =================
    ("content8.py", 'p.band("EXERCISES & ANSWERS · 练习与答案", "The Lucerna", "FINAL TEST · 综合评估 · Answers at the bottom of this page 答案在本版下方")',
     'p.band("EXERCISES & ANSWERS · Упражнения и ответы", "The Lucerna", "FINAL TEST · Итоговый тест · Answers at the bottom of this page · Ответы внизу этой страницы")', 1),
    ("content8.py", '"11 月 3 日是周二"', '"3 ноября — вторник"', 1),
    ("content8.py", '"pizza 披萨"', '"pizza = пицца"', 1),
    ("content8.py", '"map 地图逐州变色"', '"карта меняет цвет штат за штатом"', 1),
    ("content8.py", '"close 接近的"', '"close = равный"', 1),
    ("content8.py", '"sticker 贴纸"', '"sticker = наклейка"', 1),
    ("content8.py", '"will + 动词原形 know"', '"will + инфинитив: know"', 1),
    ("content8.py", '"still 仍然"', '"still = всё ещё"', 1),
    ("content8.py", '"选项："', '"Варианты:"', 1),
    # P8 heads use the W43 EN x RU short forms.
    ("content8.py", '"A · CLOZE · 完形填空"', '"A · CLOZE · Пропуски"', 1),
    ("content8.py", '"B · MULTIPLE CHOICE · 单选"', '"B · MULTIPLE CHOICE · Выбор"', 1),
    ("content8.py", '"C · READING · 阅读理解"', '"C · READING · Понимание текста"', 1),
    ("content8.py", '"D · SENTENCES · 完成句子与转换"', '"D · SENTENCES · Предложения"', 1),
    ("content8.py", '"E · TRANSLATION · 翻译"', '"E · TRANSLATION · Перевод"', 1),
    ("content8.py", '"F · WORDS · 词汇配对"', '"F · WORDS · Пары слов"', 1),
    ("content8.py", '"G · DIALOGUE · 对话补全"', '"G · DIALOGUE · Диалог"', 1),
    ("content8.py", '"H · WRITING · 写作 [B1]"', '"H · WRITING · Письмо [B1]"', 1),
    ("content8.py", '"we → get 原形"', '"we → get, инфинитив"', 1),
    ("content8.py", '"已发生的事用 fell"', '"о случившемся — fell"', 1),
    ("content8.py", '"than → 比较级 bigger"', '"than → сравнительная степень: bigger"', 1),
    ("content8.py", '"despite + 名词：尽管下雨"', '"despite + существительное: несмотря на дождь"', 1),
    ("content8.py", '"whether = 是否"', '"whether = ли"', 1),
    ("content8.py", '"将来时 will + 动词原形"', '"будущее время: will + инфинитив"', 1),
    ("content8.py", '"be going to + 原形 vote"', '"be going to + инфинитив: vote"', 1),
    ("content8.py", '"too close to call = 难分胜负"', '"too close to call = итог неясен"', 1),
    ("content8.py", '"原文：a teacher from Ohio"', '"в тексте: a teacher from Ohio"', 1),
    ("content8.py", '"周二他全天教书"', '"во вторник он преподаёт весь день"', 1),
    ("content8.py", '"贴纸上写着 I VOTED"', '"на наклейке написано I VOTED"', 1),
    ("content8.py", '"俄亥俄一如既往难分胜负"', '"Огайо, как всегда, слишком равный"', 1),
    ("content8.py", '"are going to + 原形"', '"are going to + инфинитив"', 1),
    ("content8.py", '"fall → fell（不规则变化）"', '"fall → fell, неправильный глагол"', 1),
    ("content8.py", '"tall → taller（比较级）"', '"tall → taller, сравнительная степень"', 1),
    ("content8.py", '"whether 引导“是否”从句"', '"whether вводит придаточное с «ли»"', 1),
    # E translation items: core keys are reader-language translations of English
    # sentences; 137/140 carry an English instruction (frozen "Translate :"),
    # 138/139 a native one (localised to "Perevedi:" below). Keys in Russian.
    ("content8.py", '"耐心是制度的一部分，而不是制度的失败。"', '"Терпение — часть системы, а не её провал."', 1),
    ("content8.py", '"part of 一部分；not a failure 不是失败"', '"part of = часть; not a failure = не провал"', 1),
    ("content8.py", '"11 月 3 日周二是美国的选举日。"', '"Вторник, 3 ноября, — день выборов в США."', 1),
    ("content8.py", '"Election Day 选举日；on Tuesday"', '"Election Day = день выборов; on Tuesday"', 1),
    ("content8.py", '"翻译：Tuesday, November 3, is Election Day in the United States."',
     '"Переведи: Tuesday, November 3, is Election Day in the United States."', 1),
    ("content8.py", '"这周日，NFL 在马德里比赛。"', '"В это воскресенье NFL играет в Мадриде."', 1),
    ("content8.py", '"on Sunday；in Madrid"', '"on Sunday; in Madrid"', 1),
    ("content8.py", '"翻译：On Sunday, the NFL plays in Madrid."', '"Переведи: On Sunday, the NFL plays in Madrid."', 1),
    ("content8.py", '"并非每处都拨回时钟。"', '"Не везде часы переводят назад."', 1),
    ("content8.py", '"not every 并非每处；change 变化"', '"not every = не везде; change = меняться"', 1),
    ("content8.py", '"midterm = 中期选举 b"', '"midterm = промежуточные выборы b"', 1),
    ("content8.py", '"governor = 州长 c"', '"governor = губернатор c"', 1),
    ("content8.py", '"ballot = 选票 d"', '"ballot = бюллетень d"', 1),
    ("content8.py", '"turnout = 投票率 a"', '"turnout = явка a"', 1),
    ("content8.py", '"投票时出示证件 ID"', '"покажи удостоверение, когда голосуешь"', 1),
    ("content8.py", '"line = 排队（美式英语）"', '"line = очередь, американский английский"', 1),
    ("content8.py", '"ballot = 选票"', '"ballot = бюллетень"', 1),
    ("content8.py", '"sticker = 贴纸"', '"sticker = наклейка"', 1),
    ("content8.py", '"选举日是 11 月 3 日周二"', '"день выборов — вторник 3 ноября"', 1),
    # writing item 150: key is explanation-layer text, not frozen English.
    ("content8.py", '"开放题 — 要点见写作框，范文在第 8 版写作框内"', '"Открытый вопрос: критерии — в рамке сочинения; образец — в рамке на этой странице"', 1),
    ("content8.py", '"按要点给分"', '"Оценка по пунктам"', 1),
    ("content8.py", '"MODEL · 范文"', '"MODEL · Образец"', 1),
    ("content8.py", '"用英语写 80–100 词：我的 11 月 3 日周二。写清你是否看了结果、吃了什么、地图显示了什么，再写一句周日夜里拨回的时钟。"',
     '"Напиши по-английски 80–100 слов о своём вторнике 3 ноября: результаты, еда, карта и одно предложение о часах, переведённых назад в ночь на воскресенье."', 1),
    ("content8.py", '"ANSWERS · 全部答案与简析（第 1–8 版）"', '"ANSWERS · Все ответы с пояснениями (стр. 1–8)"', 1),
    # P8 key block: W43 EN x RU family uses half-width parens with a space
    # (core: full-width).
    ("content8.py", 'kf.para(f"— 第 {pg} 版 —", 17, "sans", True, OLIVE, 1.28, 3)',
     'kf.para(f"— СТРАНИЦА {pg} —", 17, "sans", True, OLIVE, 1.28, 3)', 1),
    ("content8.py", 's += f"（{e[\'note\']}）"', 's += f" ({e[\'note\']})"', 1),
    # Printed-note set must equal the core's exactly (78). Russian notes are
    # longer than the Chinese notes the len<=10 rule was calibrated for, so
    # the set is pinned explicitly (W43 EN x RU PRINT_NOTES precedent;
    # same 39 P1-P7 numbers as the EN x ES pin, core set identical).
    ("content8.py", 'if e["note"] and (pg == 8 or len(e["note"]) <= 10 or e["type"] in ("改错", "图表读数")):',
     'NOTAS_EXTRA = {11, 12, 14, 19, 29, 30, 31, 33, 41, 44, 47, 48, 51, 58, 64, 66, 67, 68, 69, 71, 74, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93, 100, 102, 107, 108, 109, 110, 111}\n        if e["note"] and (pg == 8 or e["n"] in NOTAS_EXTRA):', 1),
]

R += [
    # ---- fix round 2 (geometry audit + flow overflows, all PIL-measured) ----
    # P1 headline band: the Russian subtitle on the headline baseline overlapped
    # the frozen headline ink by 179.8px (same-baseline class). Short form starts
    # at 1362.3, clearing headline ink end 1243.8 by 118px (24pt bold measured).
    ("content12.py", '"Вторник — день выборов · В воскресенье часы перевели назад"', '"Вторник — выборы · Часы переведены"', 1),
    # P1 NUMBERS box: title 501.5px wide overflowed the 398px box inner; short
    # form measures 384.9. Line-1 gloss cut drops the line from 4 wraps to 3,
    # so the box (308.7+12=320.7) fits col 2 remainder (~344) instead of
    # spilling to col 3 and pushing TRY IT NOW onto the row-B feature.
    ("content12.py", '"THE WEEK IN NUMBERS · Неделя в цифрах"', '"THE WEEK IN NUMBERS · Цифры"', 1),
    ("content12.py", '(все места в Палате представителей переизбираются)', '(все места переизбираются)', 1),
    # searches subtitle overflowed the col-3 box (424 > 390 inner at 19pt).
    ("content12.py", '"Что ищут в США · Снимок Google Trends США"', '"Что ищут в США · Google Trends"', 1),
    # P2-ex cascade: A bridge wrapped to 2 lines (core: 1), pushing item 15 out
    # of col 1 and cascading the match set off the page. Short form: 399.9/434.
    ("content12.py", '"Дополни предложения по-английски, глядя на время."', '"Дополни по-английски, глядя на время."', 1),
    # C bridges wrapped to 2 lines (core: 1); uniform short form on all pages
    # (398.3/434) restores the core column-break pattern on P2 and adds slack
    # elsewhere; wording identical across pages.
    ("content12.py", '"Прочитай статью на стр. 2 и выбери правильный ответ."', '"Прочитай статью стр. 2 и выбери ответ."', 1),
    ("content34.py", '"Прочитай статью на стр. 3 и выбери правильный ответ."', '"Прочитай статью стр. 3 и выбери ответ."', 1),
    ("content34.py", '"Прочитай статью на стр. 4 и выбери правильный ответ."', '"Прочитай статью стр. 4 и выбери ответ."', 1),
    ("content56.py", '"Прочитай статью на стр. 5 и выбери правильный ответ."', '"Прочитай статью стр. 5 и выбери ответ."', 1),
    ("content56.py", '"Прочитай статью на стр. 6 и выбери правильный ответ."', '"Прочитай статью стр. 6 и выбери ответ."', 1),
    # Box titles over their 398px box inner (23pt bold measured):
    ("content34.py", '"AT HOME THIS WEEK · Что смотреть дома"', '"AT HOME THIS WEEK · Дома"', 1),
    ("content34.py", '"SUNDAY, NOVEMBER 8 · Воскресенье"', '"SUNDAY, NOVEMBER 8 · Воскрес."', 1),
    ("content56.py", '"TOO CLOSE TO CALL · Равная борьба"', '"TOO CLOSE TO CALL · Равная"', 1),
    ("content56.py", '"FIVE SENTENCES · Пять предложений"', '"FIVE SENTENCES · Пять фраз"', 1),
    ("content56.py", '"A PRACTICE BALLOT · Пробный бюллетень"', '"A PRACTICE BALLOT · Бюллетень"', 1),
    # P6-main HEAD TOO WIDE (flow head): short form measures 413.3/434.
    ("content56.py", '"READ THE CHART · Читай диаграмму"', '"READ THE CHART · График"', 1),
    # P8 battery over its bottom by 28px (E-139 wraps on the longer native
    # instruction, as in EN x ES R2): tighten the four E gaps 11 -> 4.
    ("content8.py", 'bf.ex(lv, "Перевести", k, nt, body, size=20.5)',
     'bf.ex(lv, "Перевести", k, nt, body, size=20.5, gap=4)', 1),
]

R += [
    # ---- fix round 3 (supplemental edgescan) ----
    # P1 searches note advance-right 1897 crossed the col-3 box border (1885);
    # dropping one particle brings it to ~1877 (ink lower still).
    ("content12.py", '"Относительный интерес, а не точные цифры."', '"Относительный интерес, не точные цифры."', 1),
]

CJK = re.compile(r"[\u4e00-\u9fff]")

def main():
    cache = {}
    for fname, old, new, exp in R:
        p = os.path.join(BASE, fname)
        if p not in cache:
            cache[p] = open(p, encoding="utf-8").read()
        s = cache[p]
        n = s.count(old)
        if exp is None:
            assert n >= 1, f"NOT FOUND {fname}: {old[:70]}"
        else:
            assert n == exp, f"COUNT {fname}: {old[:70]} found {n} expected {exp}"
        cache[p] = s.replace(old, new)
    # repoint OUT paths to the edition dir
    for fname in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        p = os.path.join(BASE, fname)
        s = cache[p]
        assert CORE_SVG in s, f"OUT not found in {fname}"
        cache[p] = s.replace(CORE_SVG, ED_SVG)
    for p, s in cache.items():
        open(p, "w", encoding="utf-8").write(s)
        print("wrote", os.path.basename(p))
    # post-conditions on transformed sources
    for fname in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py", "bslib4.py"]:
        s = open(os.path.join(BASE, fname), encoding="utf-8").read()
        assert not CJK.search(s), f"CJK remains in {fname}"
        assert "｜" not in s, f"fullwidth bar remains in {fname}"
    print("transform OK: no CJK, no fullwidth bar in transformed sources")

if __name__ == "__main__":
    main()
