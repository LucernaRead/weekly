"""JA x NL derivation note: this transform was generated from
the sibling W45 JA x EN transform (same OLD strings, NEW
strings rendered in Dutch). W43 JA x NL precedent governs
furniture: badge/footer/page-line/gloss-prefix/section heads
verbatim from files/weekly-report-ja-nl; masthead geometry
wordmark 248 / subtitle 316 / badge 356 19pt / tagline 390 /
rules 406/413 / band 424 (W43 JA x NL measured; the README #20
generalization's 262 wordmark is NOT followed for this pair).
P8 band right "Pagina 8" follows W43 JA x NL (JA x EN kept the
frozen Japanese label). E-zone instructions are directional
(W43 JA x NL), unlike JA x EN's plain Translate.

JA core (VOL.2, Chinese explanations) -> JA x NL edition transform.

Re-runnable: reads the PRISTINE W45 JA core build, applies exact-literal
replacements (whole strings, never AST byte offsets, never byte slicing),
and writes the edition build into this directory. Fix rounds edit THIS
file, then re-run: transform.py -> run.py (one process) -> render.py.

Frozen: every Japanese article/stem/option/letter/figure string is copied
byte-identical. Only the explanation layer changes: Chinese notes/glosses/
headers/instructions -> Dutch, per the W43 JA x NL shipped precedent
(files/weekly-report-ja-en). Masthead geometry follows the W43 JA x NL
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
    "files/weekly-report-w45-ja-nl")
CANON_SVGLIB_MD5 = "d73e23b365676c3618d7e060b835eb4d"

# (old, new) applied in order. Longer strings first where one contains another.
GLOBAL = [
    # --- output repoint ---
    ("weekly-report-w45-ja-core", "weekly-report-w45-ja-nl"),
    # --- registry type names / instructions (W43 JA x NL wording) ---
    ('instr="造句"', 'instr="Bouw een zin"'),
    ('instr="翻译"', 'instr="Vertaal"'),
    ('instr="写作"', 'instr="Schrijven"'),
    ('instr="判断"', 'instr="Waar of onwaar?"'),
    ('instr="填空"', 'instr="Vul in"'),
    ('instr="把词和释义配对"', 'instr="Koppel woorden aan betekenissen"'),
    ('instr="把活动和地点·时间配对"', 'instr="Koppel activiteiten aan plaatsen en tijden"'),
    ('"完形单选"', '"gatentekst"'),
    ('"单选"', '"meerkeuze"'),
    ('"完成句子"', '"zinnen aanvullen"'),
    ('"词汇配对"', '"combineren"'),
    ('"造句"', '"zinnen bouwen"'),
    ('"判断对错"', '"waar of onwaar"'),
    ('"翻译"', '"vertalen"'),
    ('"写作"', '"schrijven"'),
    # --- shared furniture ---
    ('"あなたは？ · 说说你自己"', '"あなたは？ · En jij?"'),
    ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
     '"Antwoorden op pagina 8 · Niveaus gemengd: zoek je nummer op"'),
]

# Answer-note translations. One Dutch rendering per distinct core note;
# duplicates share the rendering (correct: same note -> same meaning).
NOTES = [
    ("文化日在11月3日（周二）", "Cultuurdag is op 3 november (dinsdag)"),
    ("读书周到11月9日（周一）", "De Leesweek loopt tot 9 november (maandag)"),
    ("見頃＝最佳观赏期", "見頃 = mooiste periode om te kijken"),
    ("立冬＝冬天的开始", "立冬 = het begin van de winter"),
    ("神户灯光秀从7日（周六）开始", "De verlichting in Kobe begint op 7 november (zaterdag)"),
    ("文化日全国都有文化活动", "Op Cultuurdag overal culturele activiteiten"),
    ("立冬在11月7日（周六）", "立冬 is op 7 november (zaterdag)"),
    ("灯光秀在神户开始", "De verlichting in Kobe begint"),
    ("「ゆる」＝无理をしない", "「ゆる」 = jezelf niet forceren"),
    ("鍋の食卓は去年の1.5倍", "Nabe-avonden zijn 1,5 keer zoveel als vorig jaar"),
    ("発表は10月21日", "De aankondiging was op 21 oktober"),
    ("11月から1月まで気温は平年より高い",
     "Temperaturen november–januari hoger dan gemiddeld"),
    ("服と食事の話題はnoteのまとめによるもの",
     "De kleding- en eettips komen uit het note-overzicht"),
    ("ゆる＝轻松、不勉强", "ゆる = ontspannen, jezelf niet forceren"),
    ("蒸し器＝蒸笼", "蒸し器 = een stoommandje"),
    ("整える＝调理、调养", "整える = in orde brengen"),
    ("鍋＝一锅菜", "鍋 = een eenpansgerecht"),
    ("鍋の材料が1か月早く並んだ", "Nabe-ingrediënten lagen een maand eerder in de winkels"),
    ("気象庁の予報は10月20日", "De JMA-voorspelling was op 20 oktober"),
    ("サクサクdeコパンが1,300万食を超えた",
     "サクサクdeコパン passeerde 13 miljoen porties"),
    ("ゆる＝轻松 b", "ゆる = ontspannen b"),
    ("蒸し器＝蒸笼 a", "蒸し器 = stoommandje a"),
    ("麻辣湯＝辛いスープ d", "麻辣湯 = pittige soep d"),
    ("予報＝天気の予想 c", "予報 = weersvoorspelling c"),
    ("杉并的活动是家庭管弦乐队", "Het evenement in Suginami is een familieorkest"),
    ("传统工艺展在石川县立美术馆",
     "De ambachtstentoonstelling is in het Ishikawa Prefectural Museum of Art"),
    ("传统工艺展到11月8日", "De tentoonstelling loopt tot 8 november"),
    ("灯光秀在金泽城和兼六园", "De verlichting is bij Kasteel Kanazawa en Kenrokuen"),
    ("市場＝集市", "市場 = markt"),
    ("工芸＝工艺", "工芸 = ambacht"),
    ("陶器＝陶瓷", "陶器 = aardewerk"),
    ("工艺展到11月8日（周日）", "De tentoonstelling loopt tot 8 november (zondag)"),    ("金箔＝金箔", "金箔 = bladgoud"),
    # FIX5 B-1: P8 #37 bare note (P3 exercise, key 8) — previously missing from
    # NOTES; distinct from #32's （周日） note above and from the 传统… note.
    ("工艺展到11月8日", "De tentoonstelling loopt tot 8 november"),
    ("主语＋时间", "onderwerp + tijd"),
    ("地点＋で＋あります", "plaats + で + あります"),
    ("见たい＝想看", "見たい = willen zien"),
    ("和家人一起", "samen met familie"),
    ("文化の日＝11月3日 b", "文化の日 = 3 november b"),
    ("工芸展＝美術館 c", "工芸展 = museum c"),
    ("オーケストラ＝杉並 d", "オーケストラ = Suginami d"),
    ("ライトアップ＝金沢城 a", "ライトアップ = Kasteel Kanazawa a"),
    ("第1战软银3-1胜DeNA", "Wedstrijd 1: SoftBank won met 3–1 van DeNA"),
    ("第2战逆转的是筒香的3分本垒打", "Tsutsugo's homerun van 3 punten bracht in wedstrijd 2 de ommekeer"),
    ("2连胜开局的是软银", "SoftBank begon met twee zeges op rij"),
    ("2连胜开局的夺冠率是73%", "Teams met een 2–0-start worden in 73% kampioen"),
    ("2024年夺冠的是DeNA", "In 2024 werd DeNA kampioen"),
    ("第1战软银得3分", "In wedstrijd 1 scoorde SoftBank 3 punten"),
    ("第2战软银得4分", "In wedstrijd 2 scoorde SoftBank 4 punten"),
    ("第1战打到延长11局", "Wedstrijd 1 duurde tot de 11e inning"),
    ("第2战打到延长10局", "Wedstrijd 2 duurde tot de 10e inning"),
    ("夺冠率73%", "Kampioenspercentage 73%"),
    ("延長＝比赛延长", "延長 = verlenging"),
    ("第1战观众33,388人", "Wedstrijd 1: 33.388 toeschouwers"),
    ("第2战观众33,432人", "Wedstrijd 2: 33.432 toeschouwers"),
    ("相川监督说「4场胜负之战」", "Manager Aikawa sprak van een strijd om vier zeges"),
    ("第1戦は土よう日です", "Wedstrijd 1 was op zaterdag"),
    ("ソフトバンクが2連勝しました", "SoftBank won twee keer op rij"),
    ("第2戦も延長戦でした", "Wedstrijd 2 ging ook naar verlenging"),
    ("2024年はDeNAが優勝しました", "In 2024 won DeNA de titel"),
    ("万圣节在10月31日（周六）", "Halloween was op 31 oktober (zaterdag)"),
    ("涩谷禁酒时间是18时到5时", "In Shibuya geldt het drinkverbod op straat van 18.00 tot 5.00 uur"),
    ("乱扔垃圾罚款2,000日元", "Afval op straat gooien kost een boete van 2.000 yen"),
    ("化妆活动在池袋", "Het verkleedfestival is in Ikebukuro"),
    ("工艺展到11月8日（周日）", "De tentoonstelling loopt tot 8 november (zondag)"),
    ("横滨中区民祭在11月8日（周日）", "Het Naka-festival in Yokohama is op 8 november (zondag)"),
    ("万圣节在10月31日", "Halloween was op 31 oktober"),
    ("禁酒从18时开始", "Het verbod begint om 18.00 uur"),
    ("禁酒到早上5时", "Het verbod loopt tot 5.00 uur 's ochtends"),
    ("横滨祭典在11月8日", "Het festival in Yokohama is op 8 november"),
    ("夜里路上不能喝酒", "'s Nachts mag je niet op straat drinken"),
    ("ゴミの罰金は今年6月からです", "De afvalboete geldt sinds juni van dit jaar"),
    ("コスプレフェスは池袋です", "Het verkleedfestival is in Ikebukuro"),
    ("ハロウィンは10月31日（土）", "Halloween was op 31 oktober (zaterdag)"),
    ("飲むことができません＝不能喝", "飲むことができません = niet mogen drinken"),
    ("守って、〜しましょう", "守って + 〜しましょう = regels volgen, laten we…"),
    ("フェンスの中＝围栏里面", "フェンスの中 = binnen het hek"),
    ("活动从10月30日到11月1日", "Het festival duurde van 30 oktober tot 1 november"),
    ("11月から1月まで気温は平年より高い",
     "Temperaturen november–januari hoger dan gemiddeld"),
    ("雨が多いのは太平洋側", "De Pacifische kant krijgt meer regen"),
    ("九州の旅の検索は去年のほぼ2倍",
     "Zoekopdrachten voor Kyushu-reizen zijn bijna verdubbeld ten opzichte van vorig jaar"),
    ("1回の旅の予算は下がった", "Het budget per reis is gedaald"),
    ("鳴子峡の見頃は10月31日から11月8日の週末",
     "Naruko-kloof is op haar mooist in het weekend van 31 oktober tot 8 november"),
    ("图中最受欢迎的是近处的满足感", "Het populairste antwoord in de grafiek is voldoening dichtbij"),
    ("近场满足感38%", "Voldoening dichtbij: 38%"),
    ("温泉27%", "Onsen: 27%"),
    ("红叶21%与美食14%之差为7", "Bladeren 21% min eten 14% is 7"),
    ("38+27=65", "38 + 27 = 65"),
    ("四项合计100%", "Alle vier samen zijn 100%"),
    ("立冬在11月7日", "立冬 is op 7 november"),
    ("神户灯光秀到12月28日", "De verlichting in Kobe loopt tot 28 december"),
    ("九州旅行搜索约为去年的2倍",
     "Zoekopdrachten voor Kyushu-reizen zijn ongeveer twee keer zoveel als vorig jaar"),
    ("气象厅预报在10月20日", "De JMA-voorspelling was op 20 oktober"),
    ("11月は平年より暖かい予報です", "November wordt naar verwachting warmer dan gemiddeld"),
    ("九州の旅の検索は増えました", "Zoekopdrachten voor Kyushu-reizen zijn toegenomen"),
    ("グラフは練習用データです", "De grafiek bevat oefengegevens"),
    ("读书周从10月27日（周二）开始", "De Leesweek begon op 27 oktober (dinsdag)"),
    ("读书周到11月9日", "De Leesweek loopt tot 9 november"),
    ("口号是「静かだけど、冒険中。」", "De slogan is 「静かだけど、冒険中。」"),
    ("图书馆活动有图书介绍", "Het bibliotheekevenement biedt boekintroducties"),
    ("見頃＝红叶最美的时候", "見頃 = wanneer de bladeren het mooist zijn"),
    ("紅葉狩り＝去看红叶", "紅葉狩り = herfstbladeren gaan bekijken"),
    ("ライトアップ＝夜里用灯光照亮", "ライトアップ = 's nachts met licht verlichten"),
    ("落葉＝落叶", "落葉 = gevallen bladeren"),
    ("1.5倍＝比去年多50%", "1,5 keer = 50% meer dan vorig jaar"),
    ("73%≈4人中的3人", "73% ≈ 3 op de 4"),
    ("サクサクdeコパンが1,300万食", "サクサクdeコパン bereikte 13 miljoen porties"),
    ("日本大赛第1战在10月24日（周六）", "Japan Series wedstrijd 1 was op 24 oktober (zaterdag)"),
    ("第2战软银4-3获胜", "Wedstrijd 2: SoftBank won met 4–3"),
    ("神户灯光秀从7日开始", "De verlichting in Kobe begint op de 7e"),
    ("2连胜开局的夺冠率73%", "Kampioenspercentage bij een 2–0-start: 73%"),
    ("气象厅预报气温高于往年", "Het JMA voorspelt temperaturen boven het gemiddelde"),
    ("九州旅行搜索约为去年的2倍",
     "Zoekopdrachten voor Kyushu-reizen zijn ongeveer twee keer zoveel als vorig jaar"),
    ("美香周二和家人去金泽", "Op dinsdag gaat Mika met haar familie naar Kanazawa"),
    ("在金泽看传统工艺展和灯光秀",
     "In Kanazawa bekijkt ze de ambachtstentoonstelling en de verlichting"),
    ("周六和朋友去神户", "Op zaterdag gaat ze met vrienden naar Kobe"),
    ("读书周想借2本书", "Voor de Leesweek wil ze 2 boeken lenen"),
    ("主语＋时间＋地点＋动词", "onderwerp + tijd + plaats + werkwoord"),
    ("场所用「で」", "Gebruik 「で」 voor een plaats"),
    ("2连胜开局", "beginnen met twee zeges op rij"),
    ("見頃＝最佳观赏期 b", "見頃 = mooiste periode b"),
    ("鍋＝一锅菜 d", "鍋 = eenpansgerecht d"),
    ("落葉＝落叶 a", "落葉 = gevallen bladeren a"),
    ("予算＝预算 c", "予算 = budget c"),
    ("見せてください＝请出示", "見せてください = alstublieft laten zien"),
    ("借りられます＝能借（可能形）", "借りられます = kunnen lenen (mogelijkheidsvorm)"),
    ("读书周到11月9日（第7版）", "De Leesweek loopt tot 9 november (pagina 7)"),
    ("「紅葉の本」受欢迎", "「紅葉の本」 is populair"),
    ("どういたしまして＝不客气", "どういたしまして = graag gedaan"),
    ("对照第3版", "Zie pagina 3"),
    ("对照第5版", "Zie pagina 5"),
    ("对照第7版", "Zie pagina 7"),
    ("对照第6版（神户的灯光秀）", "Zie pagina 6 (de verlichting in Kobe)"),
]

# Per-file furniture / gloss / structural replacements.
PER_FILE = {
    "bslib4.py": [
        ('("译注｜" + s,', '("Uitleg — " + s,'),
        ('"Lucerna · 日语周报 VOL.2 · LUCERNA JAPANESE WEEKLY"',
         '"Lucerna · JAPANS WEEKBLAD VOL.2 · TEKSTEN IN HET JAPANS · UITLEG IN HET NEDERLANDS"'),
        ('f"第 {n} 版 / 共 {total} 版"', 'f"Pagina {n} van {total}"'),
    ],
    "content12.py": [
        ('instr="把词和释义配对"', 'instr="Combineer"'),
        # P1 masthead -> W43 JA x NL shipped geometry
        ('p.text(975, 262, "Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")',
         'p.text(975, 248, "Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")'),
        ('p.text(975, 330, "日本語版 · VOL.2 · 文化の日 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")',
         'p.text(975, 316, "日本語版 · VOL.2 · 文化の日 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")\n'
         'p.text(975, 356, "TEKSTEN IN HET JAPANS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS", 19, "sans", True, OLIVE, anchor="middle")'),
        ('p.text(975, 372, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")',
         'p.text(975, 390, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")'),
        ('p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)',
         'p.hline(MX, RIGHT, 406, INK, 3); p.hline(MX, RIGHT, 413, INK, 1.2)'),
        ('"毎週、日本語で · 每周一期 · 日本人が読んでいる日本語を読む"',
         '"毎週、日本語で · Elke week · 日本人が読んでいる日本語を読む"'),
        ('"周二是文化日"', '"Dinsdag is het Cultuurdag"'),
        ('"节日过后，红叶周末到来 · 详见第 3 版"',
         '"Na de feestdag komt het herfstbladerenweekend · zie pagina 3"'),
        ('"トップニュース · 头条"', '"トップニュース · Hoofdnieuws"'),
        ('"祝日 节假日 · 見頃 最佳观赏期 · 暦 历法 · お届けします 为您送上。"',
         '"祝日 feestdag · 見頃 mooiste periode · 暦 kalender · お届けします om aan u te bezorgen."'),
        ('"数字で見る今週 · 数字看本周"', '"数字で見る今週 · In cijfers"'),
        ('"今すぐ練習 · 即学即练"', '"今すぐ練習 · Meteen oefenen"'),
        ('"这四个话题，都是本期报纸的主题。"',
         '"Deze vier onderwerpen bepalen dit nummer."'),
        ('"来源与日期见各篇文章，非精确统计"',
         '"Data in de artikelen; geen exacte cijfers"'),
        ('"この号の内容 · 本期目录"', '"この号の内容 · In dit nummer"'),
        ('"今週のことば · 本周单词"', '"今週のことば · Woord van de week"'),
        ('"ゆる＝ 轻松、不勉强。"', '"ゆる = ontspannen, jezelf niet forceren."'),
        ('"短いニュース · 快讯"', '"短いニュース · Kort nieuws"'),
        ('"クイズ · 闪电问答"', '"クイズ · Bliksemquiz"'),
        ('"读头版，选出正确答案 · 答案见第 8 版"',
         '"Lees de voorpagina en kies · Antwoorden op pagina 8"'),
        # P2
        ('"レベル A2 · ゆる整え食と暖かい11月 · 轻松食养与暖和的11月"',
         '"レベル A2 · ゆる整え食と暖かい11月 · Rustig eten en een warme november"'),
        ('"蒸す 蒸 · 並ぶ 摆上货架 · 食卓 餐桌 · 超える 超过。"',
         '"蒸す stomen · 並ぶ in de winkels liggen · 食卓 de eettafel · 超える passeren."'),
        ('"予報 预报 · 平年 往年平均 · 季節風 季风 · 話題 话题 · 値上がり 涨价。"',
         '"予報 voorspelling · 平年 een gemiddeld jaar · 季節風 seizoenswind · 話題 onderwerp · 値上がり prijsstijgingen."'),
        ('"你呢？寒冷的日子想吃什么锅？写两句日语寄来。"',
         '"En jij? Welke nabe wil je eten op een koude dag? Schrijf twee zinnen in het Japans en stuur ze op."'),
        ('"季節のことば · 季节词语"', '"季節のことば · Seizoenswoorden"'),
        ('"ゆる整え食の4つの言葉 · 关于轻松食养的四个词"',
         '"ゆる整え食の4つの言葉 · Vier woorden voor rustig eten"'),
        ('"一锅菜"', '"een eenpansgerecht"'),
        ('"蒸笼"', '"een stoommandje"'),
        ('"轻松、不勉强"', '"ontspannen, jezelf niet forceren"'),
        ('"调理、调养"', '"lichaam en geest in orde brengen"'),
        ('"練習 · 第 2 版练习"', '"練習 · Oefeningen van pagina 2"'),
    ],
    "content34.py": [
        ('"レベル A2→B1 · 文化の日と金沢 · 文化日与金泽"',
         '"レベル A2→B1 · 文化の日と金沢 · Cultuurdag en Kanazawa"'),
        ('"市場 市场 · 工芸 工艺 · 光 灯光 · 楽しむ 享受。"',
         '"市場 markt · 工芸 ambacht · 光 licht · 楽しむ genieten."'),
        ('"陶器 陶瓷 · 漆器 漆器 · 染物 染色织物 · 金箔 金箔。"',
         '"陶器 aardewerk · 漆器 lakwerk · 染物 geverfde stoffen · 金箔 bladgoud."'),
        ('"你呢？文化日想去参加什么文化活动？写两句日语寄来。"',
         '"En jij? Aan welk cultureel evenement wil je meedoen op Cultuurdag? Schrijf twee zinnen in het Japans en stuur ze op."'),
        ('"練習 · 第 3 版练习"', '"練習 · Oefeningen van pagina 3"'),
        ('"レベル B1 · 日本シリーズ横浜の2試合 · 日本大赛横滨两场"',
         '"レベル B1 · 日本シリーズ横浜の2試合 · De Japan Series: twee wedstrijden in Yokohama"'),
        ('"延長 延长赛 · 逆転 逆转 · 同点 平分 · 優勝率 夺冠率。"',
         '"延長 verlenging · 逆転 ommekeer · 同点 gelijke stand · 優勝率 kampioenspercentage."'),
        ('"総括 总结 · 締め切り 截稿 · 確認する 核实。"',
         '"総括 overzicht · 締め切り deadline · 確認する controleren."'),
        ('"日本シリーズの日程 · 大赛日程"', '"日本シリーズの日程 · Schema"'),
        ('"横浜の2試合の記録 · 横滨两场比赛的记录"',
         '"横浜の2試合の記録 · De twee wedstrijden in Yokohama, op een rij"'),
        ('"練習 · 第 4 版练习"', '"練習 · Oefeningen van pagina 4"'),
    ],
    "content56.py": [
        ('"若者・エンタメ · 青年"', '"若者・エンタメ · Jongeren"'),
        ('"レベル B1 · ハロウィンと秋まつり · 万圣节与秋日祭典"',
         '"レベル B1 · ハロウィンと秋まつり · Halloween en herfstfestivals"'),
        ('"罰金 罚款 · 像 雕像 · 仮装 变装 · 守る 遵守。"',
         '"罰金 boete · 像 standbeeld · 仮装 verkleden · 守る je houden aan."'),
        ('"祭り 节日 · 週末 周末 · 話題 话题。"',
         '"祭り festival · 週末 weekend · 話題 onderwerp."'),
        ('"你呢？秋日祭典上想做什么？写两句日语寄来。"',
         '"En jij? Wat wil je doen op een herfstfestival? Schrijf twee zinnen in het Japans en stuur ze op."'),
        ('"練習 · 第 5 版练习"', '"練習 · Oefeningen van pagina 5"'),
        ('"レベル B2 · 暖かい11月と秋の旅 · 暖和的11月与秋日旅行"',
         '"レベル B2 · 暖かい11月と秋の旅 · Een warme november en herfstreizen"'),
        ('"予算 预算 · 満足 满足 · 観測 观测 · 追いかける 追赶。"',
         '"予算 budget · 満足 voldoening · 観測 waarneming · 追いかける najagen."'),
        ('"グラフを読もう · 读图表"', '"グラフを読もう · Lees de grafiek"'),
        ('"練習用データ · 练习数据"', '"練習用データ · Oefengegevens"'),
        ('"練習 · 第 6 版练习"', '"練習 · Oefeningen van pagina 6"'),
    ],
    "content7.py": [
        ('"ことば · 语言"', '"ことば · Taal"'),
        ('"言語フォーカス · 三つのレベル、三つのテーマ · 三个级别，三个主题"',
         '"言語フォーカス · 三つのレベル、三つのテーマ · Drie niveaus, drie thema’s"'),
        ('"読書週間 读书周 · 紹介 介绍 · 読み聞かせ 朗读。"',
         '"読書週間 Leesweek · 紹介 introductie · 読み聞かせ voorlezen."'),
        ('"見頃 最佳观赏期 · 紅葉狩り 看红叶出游 · 落葉 落叶"',
         '"見頃 mooiste periode · 紅葉狩り herfstbladeren bekijken · 落葉 gevallen bladeren"'),
        ('"〜倍 倍 · 〜% 百分之〜 · 〜万食 万份。"',
         '"〜倍 keer · 〜% procent · 〜万食 tienduizend porties."'),
        ('"まちがい診療所 · 易错诊所"', '"まちがい診療所 · Foutenkliniek"'),
        ('"有「昨日」时要用过去式。"', '"Gebruik bij 「昨日」 de verleden tijd."'),
        ('"动词名词化时要加「こと」。"',
         '"Voeg 「こと」 toe om van een werkwoord een zelfstandig naamwoord te maken."'),
        ('"地点用「か所」来数。"', '"Tel plaatsen met 「か所」."'),
        ('"动作发生的场所用「で」。"',
         '"Gebruik 「で」 voor de plaats waar een handeling gebeurt."'),
        ('"今週のフレーム · 本周句式"', '"今週のフレーム · De zin van de week"'),
        ('"句式拆解：轻松地调理身心。"',
         '"Uitleg: lichaam en geest rustig in orde brengen."'),
        ('"読者の手紙 · 读者园地"', '"読者の手紙 · Lezershoek"'),
        # Readers' corner: coordinator ruling — the Japanese disclosure line
        # (ld) must NOT serve as the operative disclosure for Dutch
        # readers, and the Chinese disclosure (lcn) is the core's
        # reader-native layer. Both are replaced by ONE Dutch
        # disclosure stating the 3 facts + an explicit invitation.
        ('ld = "※この手紙は編集部の例です。締め切りまでに、本当の読者の手紙と第8版の作文の優秀作は届きませんでした。VOL.3に載せます。"',
         'ld_nl = "Voorbeeldbrief, geen echte brief. Er waren nog geen echte brieven of beste '
         'P8-opstellen binnen; beide verschijnen '
         'in VOL.3. Stuur je Japanse brief op — gekozen brieven '
         'komen in VOL.3!"'),
        ('lcn = "编辑部示例信，非真实来信。截至截稿，未收到真实来信与第8版最佳作文；VOL.3将刊登收到的来信与佳作。"\n',
         ''),
        ('lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld, "serif", False, 20.5, CW - 44)) * 29 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26 + 16',
         'lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld_nl, "sans", False, 20, CW - 44)) * 29 + 26 + 16'),
        ('yy3 = p.para(bx + 22, yy3 + 20, ld, 20.5, "serif", False, GREY, CW - 44, 1.42) + 10\n'
         'p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)',
         'p.para(bx + 22, yy3 + 20, ld_nl, 20, "sans", False, GREY, CW - 44, 1.42)'),
        ('"今週のフレーズ · 本周金句（逐字摘自本期文章）"',
         '"今週のフレーズ · Zinnen van de week (letterlijk uit dit nummer)"'),
        ('"文化日是11月3日星期二。"', '"Cultuurdag is op dinsdag 3 november."'),
        ('"这是一个慢慢地、轻松调理的日本11月。"',
         '"Dit is een langzame, rustig geordende Japanse november."'),
        ('"所谓ゆる，就是不勉强、慢慢来的意思。"',
         '"Yuru betekent: jezelf niet forceren, het rustig aan doen."'),
        ('"火锅食材提前一个月上架了。"',
         '"Nabe-ingrediënten lagen een maand eerder in de winkels."'),
        ('"可以同时欣赏传统工艺、红叶与灯光。"',
         '"Je kunt traditionele ambachten, herfstbladeren en verlichting tegelijk beleven."'),
        ('"软银以两连胜开局。"', '"SoftBank begon met twee zeges op rij."'),
        ('"遵守规则，过一个快乐的万圣节吧。"',
         '"Houd je aan de regels en vier een fijne Halloween."'),
        ('"去看红叶的人可以自北向南追赶最佳观赏期。"',
         '"Wie herfstbladeren gaat bekijken, kan van noord naar zuid de mooiste periode volgen."'),
        ('"第1面"', '"Pagina 1"'),
        ('"第2面"', '"Pagina 2"'),
        ('"第3面"', '"Pagina 3"'),
        ('"第4面"', '"Pagina 4"'),
        ('"第5面"', '"Pagina 5"'),
        ('"第6面"', '"Pagina 6"'),
        ('"来週 · 下期预告 (VOL.3)"', '"来週 · Volgend nummer (VOL.3)"'),
    ],
    "content8.py": [
        ('instr="把词和释义配对"', 'instr="Combineer"'),
        ('"第 8 面 · 週の大きなテスト + 全ての答え"', '"Pagina 8 · 週の大きなテスト + 全ての答え"'),
        ('"テストと答え · 练习与答案"', '"テストと答え · Toets en antwoorden"'),
        # E zone re-aim JA<->ZH -> JA<->EN (W43 JA x NL pattern)
        ('"文化日是11月3日。"', '"Cultuurdag is op 3 november."'),
        ('"乱扔垃圾，要罚2,000日元。"', '"Wie afval op straat gooit, krijgt een boete van 2.000 yen."'),
        ('"读书周从10月27日开始。→ ___"', '"De Leesweek begint op 27 oktober. → ___"'),
        ('"我想去神户看红叶灯光秀。→ ___"',
         '"Ik wil naar Kobe om de herfstverlichting te zien. → ___"'),
        ('f"写作题（无唯一答案）；范文（{NCHARS} 字）见下。"',
         'f"Schrijfopdracht (geen enig juist antwoord); de voorbeeldtekst ({NCHARS} tekens) staat hieronder."'),
        ('"（开放题，范文如下）"', '"(open opdracht — voorbeeldtekst hieronder)"'),
        ('f"范文见本版 H 区（{NCHARS} 字）"',
         'f"Voorbeeldtekst in deel H van deze pagina ({NCHARS} tekens)"'),
        ('"答え · 参考答案 — 按版面分页排列，找到题号即可"',
         '"答え · Antwoorden — gegroepeerd per pagina: zoek je nummer op"'),
        ('"每题附一句中文简析 · 带 ✓ 的为范文题"',
         '"Bij elk antwoord een korte notitie in het Nederlands · ✓ = de vraag met de voorbeeldtekst"'),
        ('f"— 第{pg}面 —"', 'f"— Pagina {pg} —"'),
    ],
    "render.py": [
        ('"Lucerna-VOL2.pdf"', '"Lucerna-VOL2-NL.pdf"'),
        ('"Lucerna-VOL2-web.pdf"', '"Lucerna-VOL2-NL-web.pdf"'),
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

    # NL post-pass: directional E-zone instructions. content8.py holds
    # exactly the four translation items (verified: core has exactly
    # four instr="翻译"); the two items whose "→ ___" prompt is a Dutch
    # sentence (139/140) translate INTO Japanese, the two whose prompt
    # is Japanese (137/138) translate INTO Dutch.
    import re as _re
    _c8 = open(os.path.join(HERE, "content8.py"), encoding="utf-8").read()
    _lines = _c8.split("\n")
    _n_nl = _n_ja = 0
    for _i, _ln in enumerate(_lines):
        if 'instr="Vertaal"' in _ln and "→ ___" in _ln:
            _m = _re.search(r'"([^"]*) → ___"', _ln)
            assert _m, _ln
            _first = _m.group(1)[:1]
            if _first.isascii() and _first.isalpha():
                _lines[_i] = _ln.replace('instr="Vertaal"',
                                          'instr="Vertaal naar het Japans"')
                _n_ja += 1
            else:
                _lines[_i] = _ln.replace('instr="Vertaal"',
                                          'instr="Vertaal naar het Nederlands"')
                _n_nl += 1
    assert (_n_nl, _n_ja) == (2, 2), (_n_nl, _n_ja)
    open(os.path.join(HERE, "content8.py"), "w", encoding="utf-8").write(
        "\n".join(_lines))
    print("E-zone directional instr: 2x Nederlands, 2x Japans")
    print("OUT dir:", EDITION)


if __name__ == "__main__":
    main()
