# -*- coding: utf-8 -*-
"""JA core (VOL.2, Chinese explanations) -> JA x EN edition transform.

Re-runnable: reads the PRISTINE W45 JA core build, applies exact-literal
replacements (whole strings, never AST byte offsets, never byte slicing),
and writes the edition build into this directory. Fix rounds edit THIS
file, then re-run: transform.py -> run.py (one process) -> render.py.

Frozen: every Japanese article/stem/option/letter/figure string is copied
byte-identical. Only the explanation layer changes: Chinese notes/glosses/
headers/instructions -> English, per the W43 JA x EN shipped precedent
(files/weekly-report-ja-en). Masthead geometry follows the W43 JA x EN
shipped SVG exactly (wordmark 248, edition 316, badge 356, tagline 390,
rules 406/413, dark band 424).
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
    "files/weekly-report-w45-ja-en")
CANON_SVGLIB_MD5 = "d73e23b365676c3618d7e060b835eb4d"

# (old, new) applied in order. Longer strings first where one contains another.
GLOBAL = [
    # --- output repoint ---
    ("weekly-report-w45-ja-core", "weekly-report-w45-ja-en"),
    # --- registry type names / instructions (W43 JA x EN wording) ---
    ('instr="造句"', 'instr="Build a sentence"'),
    ('instr="翻译"', 'instr="Translate"'),
    ('instr="写作"', 'instr="Writing"'),
    ('instr="判断"', 'instr="True or false?"'),
    ('instr="填空"', 'instr="Fill in"'),
    ('instr="把词和释义配对"', 'instr="Match words to meanings"'),
    ('instr="把活动和地点·时间配对"', 'instr="Match events to places and dates"'),
    ('"完形单选"', '"cloze"'),
    ('"单选"', '"multiple choice"'),
    ('"完成句子"', '"fill-in"'),
    ('"词汇配对"', '"matching"'),
    ('"造句"', '"sentence building"'),
    ('"判断对错"', '"true/false"'),
    ('"翻译"', '"translation"'),
    ('"写作"', '"writing"'),
    # --- shared furniture ---
    ('"あなたは？ · 说说你自己"', '"あなたは？ · Your turn"'),
    ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
     '"Answers on page 8 · Levels are mixed — find your number"'),
]

# Answer-note translations. One English rendering per distinct core note;
# duplicates share the rendering (correct: same note -> same meaning).
NOTES = [
    ("文化日在11月3日（周二）", "Culture Day is November 3 (Tuesday)"),
    ("读书周到11月9日（周一）", "Reading Week runs to November 9 (Monday)"),
    ("見頃＝最佳观赏期", "見頃 = best viewing season"),
    ("立冬＝冬天的开始", "立冬 = the start of winter"),
    ("神户灯光秀从7日（周六）开始", "The Kobe illuminations start on the 7th (Saturday)"),
    ("文化日全国都有文化活动", "Culture Day brings cultural events nationwide"),
    ("立冬在11月7日（周六）", "立冬 is November 7 (Saturday)"),
    ("灯光秀在神户开始", "The illuminations start in Kobe"),
    ("「ゆる」＝无理をしない", "「ゆる」 = not forcing it"),
    ("鍋の食卓は去年の1.5倍", "Nabe dinners are 1.5 times last year's"),
    ("発表は10月21日", "The announcement was October 21"),
    ("11月から1月まで気温は平年より高い",
     "Temperatures are above average from November to January"),
    ("服と食事の話題はnoteのまとめによるもの",
     "The clothing and food topics come from the note roundup"),
    ("ゆる＝轻松、不勉强", "ゆる = relaxed, not forcing it"),
    ("蒸し器＝蒸笼", "蒸し器 = a steamer basket"),
    ("整える＝调理、调养", "整える = to put in order"),
    ("鍋＝一锅菜", "鍋 = a one-pot dish"),
    ("鍋の材料が1か月早く並んだ", "Nabe ingredients appeared a month early"),
    ("気象庁の予報は10月20日", "The JMA forecast was October 20"),
    ("サクサクdeコパンが1,300万食を超えた",
     "サクサクdeコパン passed 13 million servings"),
    ("ゆる＝轻松 b", "ゆる = relaxed b"),
    ("蒸し器＝蒸笼 a", "蒸し器 = steamer basket a"),
    ("麻辣湯＝辛いスープ d", "麻辣湯 = spicy soup dish d"),
    ("予報＝天気の予想 c", "予報 = weather forecast c"),
    ("杉并的活动是家庭管弦乐队", "The Suginami event is a family orchestra"),
    ("传统工艺展在石川县立美术馆",
     "The craft exhibition is at the Ishikawa Prefectural Museum of Art"),
    ("传统工艺展到11月8日", "The exhibition runs to November 8"),
    ("灯光秀在金泽城和兼六园", "The light-up is at Kanazawa Castle and Kenrokuen"),
    ("市場＝集市", "市場 = market"),
    ("工芸＝工艺", "工芸 = craft"),
    ("陶器＝陶瓷", "陶器 = pottery"),
    ("工艺展到11月8日（周日）", "The exhibition runs to November 8 (Sunday)"),    ("金箔＝金箔", "金箔 = gold leaf"),
    # FIX5 B-1: P8 #37 bare note (P3 exercise, key 8) — previously missing from
    # NOTES; distinct from #32's （周日） note above and from the 传统… note.
    ("工艺展到11月8日", "The exhibition runs to November 8"),
    ("主语＋时间", "subject + time"),
    ("地点＋で＋あります", "place + で + あります"),
    ("见たい＝想看", "見たい = want to see"),
    ("和家人一起", "together with family"),
    ("文化の日＝11月3日 b", "文化の日 = November 3 b"),
    ("工芸展＝美術館 c", "工芸展 = museum c"),
    ("オーケストラ＝杉並 d", "オーケストラ = Suginami d"),
    ("ライトアップ＝金沢城 a", "ライトアップ = Kanazawa Castle a"),
    ("第1战软银3-1胜DeNA", "Game 1: SoftBank beat DeNA 3–1"),
    ("第2战逆转的是筒香的3分本垒打", "Tsutsugo's 3-run homer turned Game 2 around"),
    ("2连胜开局的是软银", "SoftBank started with two straight wins"),
    ("2连胜开局的夺冠率是73%", "Teams starting 2–0 win the title 73% of the time"),
    ("2024年夺冠的是DeNA", "DeNA won the title in 2024"),
    ("第1战软银得3分", "SoftBank scored 3 in Game 1"),
    ("第2战软银得4分", "SoftBank scored 4 in Game 2"),
    ("第1战打到延长11局", "Game 1 went to 11 innings"),
    ("第2战打到延长10局", "Game 2 went to 10 innings"),
    ("夺冠率73%", "Title rate 73%"),
    ("延長＝比赛延长", "延長 = the game going long"),
    ("第1战观众33,388人", "Game 1 crowd: 33,388"),
    ("第2战观众33,432人", "Game 2 crowd: 33,432"),
    ("相川监督说「4场胜负之战」", "Manager Aikawa spoke of a four-win fight"),
    ("第1戦は土よう日です", "Game 1 was on Saturday"),
    ("ソフトバンクが2連勝しました", "SoftBank won two straight"),
    ("第2戦も延長戦でした", "Game 2 also went to extra innings"),
    ("2024年はDeNAが優勝しました", "DeNA won in 2024"),
    ("万圣节在10月31日（周六）", "Halloween was October 31 (Saturday)"),
    ("涩谷禁酒时间是18时到5时", "Shibuya's street-drinking ban runs 18:00 to 05:00"),
    ("乱扔垃圾罚款2,000日元", "Littering costs a 2,000-yen fine"),
    ("化妆活动在池袋", "The cosplay festival is in Ikebukuro"),
    ("工艺展到11月8日（周日）", "The exhibition runs to November 8 (Sunday)"),
    ("横滨中区民祭在11月8日（周日）", "The Naka Ward festival is November 8 (Sunday)"),
    ("万圣节在10月31日", "Halloween was October 31"),
    ("禁酒从18时开始", "The ban starts at 18:00"),
    ("禁酒到早上5时", "The ban runs to 05:00"),
    ("横滨祭典在11月8日", "The Yokohama festival is November 8"),
    ("夜里路上不能喝酒", "No drinking on the street at night"),
    ("ゴミの罰金は今年6月からです", "The litter fine dates from June this year"),
    ("コスプレフェスは池袋です", "The cosplay festival is in Ikebukuro"),
    ("ハロウィンは10月31日（土）", "Halloween was October 31 (Saturday)"),
    ("飲むことができません＝不能喝", "飲むことができません = cannot drink"),
    ("守って、〜しましょう", "守って + 〜しましょう = follow the rules, and let's…"),
    ("フェンスの中＝围栏里面", "フェンスの中 = inside the fence"),
    ("活动从10月30日到11月1日", "The festival ran October 30 to November 1"),
    ("11月から1月まで気温は平年より高い",
     "Temperatures are above average from November to January"),
    ("雨が多いのは太平洋側", "The Pacific side gets more rain"),
    ("九州の旅の検索は去年のほぼ2倍",
     "Kyushu travel searches nearly doubled year on year"),
    ("1回の旅の予算は下がった", "The budget per trip fell"),
    ("鳴子峡の見頃は10月31日から11月8日の週末",
     "Naruko Gorge peaks over the October 31 – November 8 weekend"),
    ("图中最受欢迎的是近处的满足感", "The chart's top answer is nearby satisfaction"),
    ("近场满足感38%", "Nearby satisfaction: 38%"),
    ("温泉27%", "Hot springs: 27%"),
    ("红叶21%与美食14%之差为7", "Leaves 21% minus food 14% is 7"),
    ("38+27=65", "38 + 27 = 65"),
    ("四项合计100%", "All four add up to 100%"),
    ("立冬在11月7日", "立冬 is November 7"),
    ("神户灯光秀到12月28日", "The Kobe light-up runs to December 28"),
    ("九州旅行搜索约为去年的2倍",
     "Kyushu travel searches are nearly twice last year's"),
    ("气象厅预报在10月20日", "The JMA forecast was October 20"),
    ("11月は平年より暖かい予報です", "November is forecast warmer than average"),
    ("九州の旅の検索は増えました", "Kyushu travel searches rose"),
    ("グラフは練習用データです", "The chart is practice data"),
    ("读书周从10月27日（周二）开始", "Reading Week started October 27 (Tuesday)"),
    ("读书周到11月9日", "Reading Week runs to November 9"),
    ("口号是「静かだけど、冒険中。」", "The slogan is 「静かだけど、冒険中。」"),
    ("图书馆活动有图书介绍", "The library event is book introductions"),
    ("見頃＝红叶最美的时候", "見頃 = when the leaves look their best"),
    ("紅葉狩り＝去看红叶", "紅葉狩り = going out to see the leaves"),
    ("ライトアップ＝夜里用灯光照亮", "ライトアップ = lighting up at night"),
    ("落葉＝落叶", "落葉 = fallen leaves"),
    ("1.5倍＝比去年多50%", "1.5倍 = 50% more than last year"),
    ("73%≈4人中的3人", "73% ≈ 3 in 4"),
    ("サクサクdeコパンが1,300万食", "サクサクdeコパン reached 13 million servings"),
    ("日本大赛第1战在10月24日（周六）", "Japan Series Game 1 was October 24 (Saturday)"),
    ("第2战软银4-3获胜", "Game 2: SoftBank won 4–3"),
    ("神户灯光秀从7日开始", "The Kobe light-up starts on the 7th"),
    ("2连胜开局的夺冠率73%", "Title rate for 2–0 starts: 73%"),
    ("气象厅预报气温高于往年", "The JMA forecast: warmer than average"),
    ("九州旅行搜索约为去年的2倍",
     "Kyushu travel searches are nearly twice last year's"),
    ("美香周二和家人去金泽", "On Tuesday Mika goes to Kanazawa with her family"),
    ("在金泽看传统工艺展和灯光秀",
     "In Kanazawa she sees the craft exhibition and the light-up"),
    ("周六和朋友去神户", "On Saturday she goes to Kobe with friends"),
    ("读书周想借2本书", "She wants to borrow 2 books for Reading Week"),
    ("主语＋时间＋地点＋动词", "subject + time + place + verb"),
    ("场所用「で」", "use 「で」 for place"),
    ("2连胜开局", "starting with two straight wins"),
    ("見頃＝最佳观赏期 b", "見頃 = best viewing season b"),
    ("鍋＝一锅菜 d", "鍋 = one-pot dish d"),
    ("落葉＝落叶 a", "落葉 = fallen leaves a"),
    ("予算＝预算 c", "予算 = budget c"),
    ("見せてください＝请出示", "見せてください = please show"),
    ("借りられます＝能借（可能形）", "借りられます = can borrow (potential form)"),
    ("读书周到11月9日（第7版）", "Reading Week runs to November 9 (page 7)"),
    ("「紅葉の本」受欢迎", "「紅葉の本」 is popular"),
    ("どういたしまして＝不客气", "どういたしまして = you're welcome"),
    ("对照第3版", "See page 3"),
    ("对照第5版", "See page 5"),
    ("对照第7版", "See page 7"),
    ("对照第6版（神户的灯光秀）", "See page 6 (Kobe illuminations)"),
]

# Per-file furniture / gloss / structural replacements.
PER_FILE = {
    "bslib4.py": [
        ('("译注｜" + s,', '("Note — " + s,'),
        ('"Lucerna · 日语周报 VOL.2 · LUCERNA JAPANESE WEEKLY"',
         '"Lucerna · JAPANESE WEEKLY VOL.2 · Japanese text · English explanations"'),
        ('f"第 {n} 版 / 共 {total} 版"', 'f"Page {n} of {total}"'),
    ],
    "content12.py": [
        # P1 masthead -> W43 JA x EN shipped geometry
        ('p.text(975, 262, "Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")',
         'p.text(975, 248, "Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")'),
        ('p.text(975, 330, "日本語版 · VOL.2 · 文化の日 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")',
         'p.text(975, 316, "日本語版 · VOL.2 · 文化の日 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")\n'
         'p.text(975, 356, "TEXT IN JAPANESE · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS", 19, "sans", True, OLIVE, anchor="middle")'),
        ('p.text(975, 372, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")',
         'p.text(975, 390, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")'),
        ('p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)',
         'p.hline(MX, RIGHT, 406, INK, 3); p.hline(MX, RIGHT, 413, INK, 1.2)'),
        ('"毎週、日本語で · 每周一期 · 日本人が読んでいる日本語を読む"',
         '"毎週、日本語で · Weekly · 日本人が読んでいる日本語を読む"'),
        ('"周二是文化日"', '"Tuesday is Culture Day"'),
        ('"节日过后，红叶周末到来 · 详见第 3 版"',
         '"After the holiday, the autumn-leaf weekend arrives · See page 3"'),
        ('"トップニュース · 头条"', '"トップニュース · Top story"'),
        ('"祝日 节假日 · 見頃 最佳观赏期 · 暦 历法 · お届けします 为您送上。"',
         '"祝日 holiday · 見頃 best viewing season · 暦 calendar · お届けします to bring to you."'),
        ('"数字で見る今週 · 数字看本周"', '"数字で見る今週 · Week in numbers"'),
        ('"今すぐ練習 · 即学即练"', '"今すぐ練習 · Practice now"'),
        ('"这四个话题，都是本期报纸的主题。"',
         '"These four topics shape this issue."'),
        ('"来源与日期见各篇文章，非精确统计"',
         '"Dates in articles; not exact statistics"'),
        ('"この号の内容 · 本期目录"', '"この号の内容 · In this issue"'),
        ('"今週のことば · 本周单词"', '"今週のことば · Word of the week"'),
        ('"ゆる＝ 轻松、不勉强。"', '"ゆる = relaxed, not forcing it."'),
        ('"短いニュース · 快讯"', '"短いニュース · News in brief"'),
        ('"クイズ · 闪电问答"', '"クイズ · Quick quiz"'),
        ('"读头版，选出正确答案 · 答案见第 8 版"',
         '"Read the front page and choose · Answers on page 8"'),
        # P2
        ('"レベル A2 · ゆる整え食と暖かい11月 · 轻松食养与暖和的11月"',
         '"レベル A2 · ゆる整え食と暖かい11月 · Gentle food and a warm November"'),
        ('"蒸す 蒸 · 並ぶ 摆上货架 · 食卓 餐桌 · 超える 超过。"',
         '"蒸す to steam · 並ぶ to appear on shelves · 食卓 the dinner table · 超える to pass."'),
        ('"予報 预报 · 平年 往年平均 · 季節風 季风 · 話題 话题 · 値上がり 涨价。"',
         '"予報 forecast · 平年 an average year · 季節風 seasonal wind · 話題 topic · 値上がり price rises."'),
        ('"你呢？寒冷的日子想吃什么锅？写两句日语寄来。"',
         '"What about you? On a cold day, what nabe would you like to eat? Write two sentences in Japanese and send them in."'),
        ('"季節のことば · 季节词语"', '"季節のことば · Words of the season"'),
        ('"ゆる整え食の4つの言葉 · 关于轻松食养的四个词"',
         '"ゆる整え食の4つの言葉 · Four words for gentle eating"'),
        ('"一锅菜"', '"a one-pot dish"'),
        ('"蒸笼"', '"a steamer basket"'),
        ('"轻松、不勉强"', '"relaxed, not forcing it"'),
        ('"调理、调养"', '"to put body and mind in order"'),
        ('"練習 · 第 2 版练习"', '"練習 · Page 2 exercises"'),
    ],
    "content34.py": [
        ('"レベル A2→B1 · 文化の日と金沢 · 文化日与金泽"',
         '"レベル A2→B1 · 文化の日と金沢 · Culture Day and Kanazawa"'),
        ('"市場 市场 · 工芸 工艺 · 光 灯光 · 楽しむ 享受。"',
         '"市場 market · 工芸 craft · 光 light · 楽しむ to enjoy."'),
        ('"陶器 陶瓷 · 漆器 漆器 · 染物 染色织物 · 金箔 金箔。"',
         '"陶器 pottery · 漆器 lacquerware · 染物 dyed textiles · 金箔 gold leaf."'),
        ('"你呢？文化日想去参加什么文化活动？写两句日语寄来。"',
         '"What about you? What cultural event would you like to go to on Culture Day? Write two sentences in Japanese and send them in."'),
        ('"練習 · 第 3 版练习"', '"練習 · Page 3 exercises"'),
        ('"レベル B1 · 日本シリーズ横浜の2試合 · 日本大赛横滨两场"',
         '"レベル B1 · 日本シリーズ横浜の2試合 · The Japan Series: two games in Yokohama"'),
        ('"延長 延长赛 · 逆転 逆转 · 同点 平分 · 優勝率 夺冠率。"',
         '"延長 extra innings · 逆転 comeback · 同点 tie · 優勝率 title rate."'),
        ('"総括 总结 · 締め切り 截稿 · 確認する 核实。"',
         '"総括 roundup · 締め切り deadline · 確認する to confirm."'),
        ('"日本シリーズの日程 · 大赛日程"', '"日本シリーズの日程 · Series schedule"'),
        ('"横浜の2試合の記録 · 横滨两场比赛的记录"',
         '"横浜の2試合の記録 · The two Yokohama games, on record"'),
        ('"練習 · 第 4 版练习"', '"練習 · Page 4 exercises"'),
    ],
    "content56.py": [
        ('"若者・エンタメ · 青年"', '"若者・エンタメ · Youth"'),
        ('"レベル B1 · ハロウィンと秋まつり · 万圣节与秋日祭典"',
         '"レベル B1 · ハロウィンと秋まつり · Halloween and autumn festivals"'),
        ('"罰金 罚款 · 像 雕像 · 仮装 变装 · 守る 遵守。"',
         '"罰金 fine · 像 statue · 仮装 dressing up · 守る to follow."'),
        ('"祭り 节日 · 週末 周末 · 話題 话题。"',
         '"祭り festival · 週末 weekend · 話題 topic."'),
        ('"你呢？秋日祭典上想做什么？写两句日语寄来。"',
         '"What about you? What would you like to do at an autumn festival? Write two sentences in Japanese and send them in."'),
        ('"練習 · 第 5 版练习"', '"練習 · Page 5 exercises"'),
        ('"レベル B2 · 暖かい11月と秋の旅 · 暖和的11月与秋日旅行"',
         '"レベル B2 · 暖かい11月と秋の旅 · A warm November and autumn travel"'),
        ('"予算 预算 · 満足 满足 · 観測 观测 · 追いかける 追赶。"',
         '"予算 budget · 満足 satisfaction · 観測 observation · 追いかける to chase."'),
        ('"グラフを読もう · 读图表"', '"グラフを読もう · Reading the chart"'),
        ('"練習用データ · 练习数据"', '"練習用データ · Practice data"'),
        ('"練習 · 第 6 版练习"', '"練習 · Page 6 exercises"'),
    ],
    "content7.py": [
        ('"ことば · 语言"', '"ことば · Language"'),
        ('"言語フォーカス · 三つのレベル、三つのテーマ · 三个级别，三个主题"',
         '"言語フォーカス · 三つのレベル、三つのテーマ · Three levels, three themes"'),
        ('"読書週間 读书周 · 紹介 介绍 · 読み聞かせ 朗读。"',
         '"読書週間 Reading Week · 紹介 introduction · 読み聞かせ reading aloud."'),
        ('"見頃 最佳观赏期 · 紅葉狩り 看红叶出游 · 落葉 落叶"',
         '"見頃 best viewing season · 紅葉狩り leaf-viewing outings · 落葉 fallen leaves"'),
        ('"〜倍 倍 · 〜% 百分之〜 · 〜万食 万份。"',
         '"〜倍 times · 〜% percent · 〜万食 ten-thousand servings."'),
        ('"まちがい診療所 · 易错诊所"', '"まちがい診療所 · Error clinic"'),
        ('"有「昨日」时要用过去式。"', '"With 「昨日」, use the past tense."'),
        ('"动词名词化时要加「こと」。"',
         '"Add 「こと」 to turn a verb into a noun phrase."'),
        ('"地点用「か所」来数。"', '"Count places with 「か所」."'),
        ('"动作发生的场所用「で」。"',
         '"Use 「で」 for the place where an action happens."'),
        ('"今週のフレーム · 本周句式"', '"今週のフレーム · Frame of the week"'),
        ('"句式拆解：轻松地调理身心。"',
         '"Breakdown: gently putting body and mind in order."'),
        ('"読者の手紙 · 读者园地"', '"読者の手紙 · Readers\' corner"'),
        # Readers' corner: coordinator ruling — the Japanese disclosure line
        # (ld) must NOT serve as the operative disclosure for English
        # readers, and the Chinese disclosure (lcn) is the core's
        # reader-native layer. Both are replaced by ONE English
        # disclosure stating the 3 facts + an explicit invitation.
        ('ld = "※この手紙は編集部の例です。締め切りまでに、本当の読者の手紙と第8版の作文の優秀作は届きませんでした。VOL.3に載せます。"',
         'ld_en = "Editor\'s sample, not a real letter. No real letters or best '
         'Page 8 compositions had arrived by the deadline; both will appear '
         'in VOL.3. Send us your letter in Japanese — selected letters will '
         'be printed in VOL.3!"'),
        ('lcn = "编辑部示例信，非真实来信。截至截稿，未收到真实来信与第8版最佳作文；VOL.3将刊登收到的来信与佳作。"\n',
         ''),
        ('lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld, "serif", False, 20.5, CW - 44)) * 29 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26 + 16',
         'lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld_en, "sans", False, 20, CW - 44)) * 29 + 26 + 16'),
        ('yy3 = p.para(bx + 22, yy3 + 20, ld, 20.5, "serif", False, GREY, CW - 44, 1.42) + 10\n'
         'p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)',
         'p.para(bx + 22, yy3 + 20, ld_en, 20, "sans", False, GREY, CW - 44, 1.42)'),
        ('"今週のフレーズ · 本周金句（逐字摘自本期文章）"',
         '"今週のフレーズ · Phrases of the week (verbatim from this issue)"'),
        ('"文化日是11月3日星期二。"', '"Culture Day is Tuesday, November 3."'),
        ('"这是一个慢慢地、轻松调理的日本11月。"',
         '"It is a slow, gently ordered Japanese November."'),
        ('"所谓ゆる，就是不勉强、慢慢来的意思。"',
         '"ゆる means not forcing it, taking it slowly."'),
        ('"火锅食材提前一个月上架了。"',
         '"Nabe ingredients appeared in shops a month early."'),
        ('"可以同时欣赏传统工艺、红叶与灯光。"',
         '"You can enjoy traditional crafts, autumn leaves, and lights together."'),
        ('"软银以两连胜开局。"', '"SoftBank started with two straight wins."'),
        ('"遵守规则，过一个快乐的万圣节吧。"',
         '"Follow the rules and have a happy Halloween."'),
        ('"去看红叶的人可以自北向南追赶最佳观赏期。"',
         '"Leaf-viewers can chase the best season from north to south."'),
        ('"第1面"', '"p.1"'),
        ('"第2面"', '"p.2"'),
        ('"第3面"', '"p.3"'),
        ('"第4面"', '"p.4"'),
        ('"第5面"', '"p.5"'),
        ('"第6面"', '"p.6"'),
        ('"来週 · 下期预告 (VOL.3)"', '"来週 · Next issue (VOL.3)"'),
    ],
    "content8.py": [
        ('"テストと答え · 练习与答案"', '"テストと答え · Test and answers"'),
        # E zone re-aim JA<->ZH -> JA<->EN (W43 JA x EN pattern)
        ('"文化日是11月3日。"', '"Culture Day is November 3."'),
        ('"乱扔垃圾，要罚2,000日元。"', '"If you drop litter, the fine is 2,000 yen."'),
        ('"读书周从10月27日开始。→ ___"', '"Reading Week starts on October 27. → ___"'),
        ('"我想去神户看红叶灯光秀。→ ___"',
         '"I want to go to Kobe to see the autumn-leaf illuminations. → ___"'),
        ('f"写作题（无唯一答案）；范文（{NCHARS} 字）见下。"',
         'f"Writing task (no single correct answer); the model text ({NCHARS} characters) is below."'),
        ('"（开放题，范文如下）"', '"(open task — model text below)"'),
        ('f"范文见本版 H 区（{NCHARS} 字）"',
         'f"Model text in section H on this page ({NCHARS} characters)"'),
        ('"答え · 参考答案 — 按版面分页排列，找到题号即可"',
         '"答え · Answers — grouped by page; just find your number"'),
        ('"每题附一句中文简析 · 带 ✓ 的为范文题"',
         '"A short English note with every answer · ✓ = the model-text item"'),
        ('f"— 第{pg}面 —"', 'f"— Page {pg} —"'),
    ],
    "render.py": [
        ('"Lucerna-VOL2.pdf"', '"Lucerna-VOL2-EN.pdf"'),
        ('"Lucerna-VOL2-web.pdf"', '"Lucerna-VOL2-EN-web.pdf"'),
    ],
}


def apply_pairs(text, pairs, fname):
    seen = set()
    for old, new in pairs:
        if old in seen:
            continue
        seen.add(old)
        n = text.count(old)
        assert n >= 1, f"{fname}: replacement source missing: {old!r}"
        text = text.replace(old, new)
    return text


def apply_soft(text, pairs):
    seen = set()
    for old, new in pairs:
        if old in seen:
            continue
        seen.add(old)
        text = text.replace(old, new)
    return text


def apply_notes_scoped(text, note_map):
    """Replace note strings ONLY where they are note arguments.

    Bare substring replacement is FORBIDDEN for notes: several notes are
    prefixes/substrings of frozen Japanese stems and article sentences
    (e.g. note "2024年はDeNAが優勝しました" vs stem "...ました。";
    note "グラフは練習用データです" vs the frozen chart para), and a
    global replace corrupted frozen text in round 1. Two scoped sites:
    (a) the 4th quoted argument of any .ex(...) call;
    (b) a bracket-list line whose every string is a note (match_set notes
    lists; lefts/rights/keys lines never satisfy this).
    """
    def ex_sub(m):
        note = m.group(2)
        if note in note_map:
            return m.group(1) + note_map[note] + m.group(3)
        return m.group(0)
    text = re.sub(r'(\.ex\("[^"]*",\s*"[^"]*",\s*"[^"]*",\s*")([^"]*)(")',
                  ex_sub, text)

    def list_sub(m):
        inner = m.group(2)
        strs = re.findall(r'"([^"]*)"', inner)
        if strs and all(s in note_map for s in strs):
            out = inner
            for s in strs:
                out = out.replace('"%s"' % s, '"%s"' % note_map[s], 1)
            return m.group(1) + out + m.group(3)
        return m.group(0)
    text = re.sub(r'(?m)^(\s*\[)(.*)(\],\s*)$', list_sub, text)
    return text


def quoted_strings(text):
    return set(re.findall(r'"([^"]*)"', text))


def main():
    os.makedirs(EDITION, exist_ok=True)
    os.makedirs(os.path.join(EDITION, "svg"), exist_ok=True)
    # svglib: canonical JA build, copied verbatim, md5-verified, never edited.
    src_svg = os.path.join(CORE, "svglib.py")
    data = open(src_svg, "rb").read()
    assert hashlib.md5(data).hexdigest() == CANON_SVGLIB_MD5, "svglib md5 mismatch"
    shutil.copyfile(src_svg, os.path.join(HERE, "svglib.py"))
    # run.py: verbatim copy (one-process driver).
    shutil.copyfile(os.path.join(CORE, "run.py"), os.path.join(HERE, "run.py"))
    # assets: verbatim copies (images + credits).
    os.makedirs(os.path.join(HERE, "assets"), exist_ok=True)
    for f in os.listdir(os.path.join(CORE, "assets")):
        shutil.copyfile(os.path.join(CORE, "assets", f),
                        os.path.join(HERE, "assets", f))
    # NOTE replacements: dict (deduped). Order: NOTES scoped FIRST (note
    # arguments only), then structural PER_FILE, then GLOBAL types/instr.
    # PER_FILE after NOTES because PER_FILE owns whole lines that share
    # words with notes (e.g. the season-word tuple "一锅菜" vs note
    # "鍋＝一锅菜"); GLOBAL last because it owns the P8 writing bridge's
    # neighbours only via PER_FILE lines.
    note_map = dict(NOTES)
    fnames = ["bslib4.py", "content12.py", "content34.py", "content56.py",
              "content7.py", "content8.py", "render.py"]
    # Pre-audit: every GLOBAL source must occur in >=1 core file, and
    # every NOTE key must occur as an EXACT quoted string (a real note
    # argument, not a substring of a frozen sentence).
    core_texts = {f: open(os.path.join(CORE, f), encoding="utf-8").read()
                  for f in fnames}
    for old, _ in GLOBAL:
        assert any(old in t for t in core_texts.values()), \
            f"transform table source never occurs in core: {old!r}"
    core_quoted = set()
    for t in core_texts.values():
        core_quoted |= quoted_strings(t)
    for old in note_map:
        assert old in core_quoted, \
            f"note key never occurs as an exact quoted string: {old!r}"
    for fname in fnames:
        text = core_texts[fname]
        text = apply_notes_scoped(text, note_map)
        text = apply_pairs(text, PER_FILE.get(fname, []), fname)
        text = apply_soft(text, GLOBAL)
        open(os.path.join(HERE, fname), "w", encoding="utf-8").write(text)
        print("transformed", fname)
    # Post-audit: no GLOBAL source may survive as a substring, and no
    # NOTE key may survive as an exact quoted string (substrings inside
    # frozen stems, e.g. "...ました。" stems, legitimately remain).
    for fname in fnames:
        out = open(os.path.join(HERE, fname), encoding="utf-8").read()
        for old, _ in GLOBAL:
            assert old not in out, f"{fname}: un-replaced source remains: {old!r}"
        out_quoted = quoted_strings(out)
        for old in note_map:
            assert old not in out_quoted, \
                f"{fname}: un-replaced note remains: {old!r}"
    print("OUT dir:", EDITION)


if __name__ == "__main__":
    main()
