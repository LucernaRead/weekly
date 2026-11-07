# -*- coding: utf-8 -*-
"""JA core (VOL.3, Chinese explanations) -> JA x EN edition transform.

Re-runnable: reads the PRISTINE W46 JA core build, applies exact-literal
replacements (whole strings, never AST byte offsets), and writes the
edition build into this directory. Fix rounds edit THIS file, then
re-run: transform.py -> run.py (one process) -> render.py.

Frozen: every Japanese article/stem/option/letter/figure string is copied
byte-identical. Only the explanation layer changes: Chinese notes/glosses/
headers/instructions -> English, per the W45 JA x EN shipped precedent.
Masthead geometry per the W46 task + tools/README lesson 20: wordmark
stays at the CORE position y=262, subtitle 316, badge inserted at
(975,356) 19pt BRICK, strapline 390, rules 406/413, dark band 424.
"""
import hashlib
import os
import re
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
CORE = os.path.expanduser(
    "~/workspace/goals/lucernaread-social-media-operations/"
    "hidden_files/weekly-report-w46-ja-build")
EDITION = os.path.expanduser(
    "~/workspace/goals/lucernaread-social-media-operations/"
    "files/weekly-report-w46-ja-en")
CANON_SVGLIB_MD5 = "74177544422fe677639d769cd80499fb"

GLOBAL = [
    ("weekly-report-w46-ja-core", "weekly-report-w46-ja-en"),
    ('instr="造句"', 'instr="Build a sentence"'),
    ('instr="翻译"', 'instr="Translate"'),
    ('instr="写作"', 'instr="Writing"'),
    ('instr="判断"', 'instr="True or false?"'),
    ('instr="填空"', 'instr="Fill in"'),
    ('instr="把词和释义配对"', 'instr="Match words to meanings"'),
    ('"完形单选"', '"cloze"'),
    ('"单选"', '"multiple choice"'),
    ('"完成句子"', '"fill-in"'),
    ('"词汇配对"', '"matching"'),
    ('"造句"', '"sentence building"'),
    ('"判断对错"', '"true/false"'),
    ('"翻译"', '"translation"'),
    ('"写作"', '"writing"'),
    ('"あなたは？ · 说说你自己"', '"あなたは？ · Your turn"'),
    ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
     '"Answers on page 8 · Levels are mixed — find your number"'),
]

NOTES = [
    ("1111中有4个1", "1111 has four 1s"),
    ("1111看起来像4根细棒", "1111 looks like four thin sticks"),
    ("11月中旬以后进入见赏期的地点多比往年稍晚", "Places peaking after mid-November are mostly later than average"),
    ("2026年没有三の酉", "There is no San-no-tori in 2026"),
    ("3%≈100人中的3人", "3% is about 3 in 100"),
    ("34+26=60", "34 + 26 = 60"),
    ("4连胜夺冠", "Four straight wins took the title"),
    ("4连胜＝4场比赛全胜", "winning all four games"),
    ("71%的家庭接受祈祷", "71% of families receive a prayer"),
    ("74%的家庭在照相馆拍照", "74% of families take photos at a studio"),
    ("Weathernews的预报在10月29日（周四）", "The Weathernews forecast was October 29 (Thursday)"),
    ("「千歳飴」受欢迎", "千歳飴 is popular"),
    ("お参りします＝去参拜", "お参りします = to go and pray"),
    ("お参り＝去神社参拜", "お参り = going to a shrine to pray"),
    ("どういたしまして＝不客气", "どういたしまして = you're welcome"),
    ("七五三是3岁5岁7岁孩子的庆祝活动", "Shichi-Go-San celebrates children aged 3, 5 and 7"),
    ("七五三是3岁、5岁、7岁孩子的庆祝活动", "Shichi-Go-San celebrates children aged 3, 5 and 7"),
    ("七五三的中心日在11月15日附近", "Shichi-Go-San centres on about November 15"),
    ("七五三的中心日是11月15日（周日）", "Shichi-Go-San centres on November 15 (Sunday)"),
    ("七五三的中心日是11月15日（第3版）", "Shichi-Go-San centres on November 15 (page 3)"),
    ("七五三的孩子去神社参拜", "Shichi-Go-San children go to a shrine to pray"),
    ("七五三的照片是全家的回忆", "Shichi-Go-San photos are a family memory"),
    ("七五三＝孩子的庆祝活动", "七五三 = a celebration for children"),
    ("七五三＝3岁5岁7岁孩子的庆祝 b", "七五三 = a celebration for children aged 3, 5 and 7 · b"),
    ("东京的红叶在11月29日（周日）前后", "Tokyo's leaves peak around November 29 (Sunday)"),
    ("主语＋时间＋宾语＋动词", "subject + time + object + verb"),
    ("主语＋说明", "subject + description"),
    ("九州场所在福冈国际中心举行", "The Kyushu tournament is at the Fukuoka Kokusai Center"),
    ("二の酉在11月19日（周四）", "Ni-no-tori is November 19 (Thursday)"),
    ("分ける＝分享", "分ける = to share"),
    ("前3场比赛连续打延长赛", "The first three games all went to extra innings"),
    ("前3场都是延长赛", "The first three games all went to extra innings"),
    ("千岁糖寄托长寿的愿望", "Chitose-ame carries a wish for a long life"),
    ("千岁糖是红白相间的长糖", "Chitose-ame is a long red-and-white candy"),
    ("千岁糖＝红白长糖", "red-and-white long candy"),
    ("千歳飴＝红白长糖 a", "千歳飴 = red-and-white long candy · a"),
    ("千歳飴＝红白长糖 d", "千歳飴 = red-and-white long candy · d"),
    ("口号是「静かだけど、冒険中。」", "The slogan is 「静かだけど、冒険中。」"),
    ("周一读图书馆借的书", "On Monday he reads a library book"),
    ("周三和朋友分享波奇", "On Wednesday he shares Pocky with friends"),
    ("周五去高尾山看红叶", "On Friday he goes to Mt. Takao for the leaves"),
    ("周日和妹妹的七五三去神社", "On Sunday he goes to a shrine for his sister's Shichi-Go-San"),
    ("四项合计100%", "All four add up to 100%"),
    ("图表中最受欢迎的是山", "Mountains top the chart"),
    ("图表是真实调查结果", "The chart shows real survey results"),
    ("在酉の市买熊手", "Buying a kumade at Tori-no-ichi"),
    ("地点＋へ＋动词", "place + へ + verb"),
    ("场所用「で」", "Use 「で」 for place"),
    ("大阪的红叶在12月4日（周五）前后", "Osaka's leaves peak around December 4 (Friday)"),
    ("宫岛的红叶从11月21日（周六）前后进入见赏期", "Miyajima's leaves peak from around November 21 (Saturday)"),
    ("宾语＋动词", "object + verb"),
    ("对照第2版", "See page 2"),
    ("对照第3版", "See page 3"),
    ("对照第6版（追赶见赏期）", "See page 6 (chasing the best season)"),
    ("对照第7版", "See page 7"),
    ("山34%与神社26%之差为8", "Mountains 34% minus shrines 26% is 8"),
    ("山占34%", "Mountains: 34%"),
    ("岚山的红叶从11月23日（周一）前后进入见赏期", "Arashiyama's leaves peak from around November 23 (Monday)"),
    ("平成11年11月11日有6个1", "November 11, Heisei 11, had six 1s"),
    ("思い出＝回忆", "思い出 = a memory"),
    ("接戦＝比分接近的比赛", "接戦 = a close game"),
    ("撮ります＝拍照", "撮ります = to take a photo"),
    ("新小结是美ノ海", "The new komusubi is Umi-no-umi"),
    ("日本大赛第3战在10月27日（周二）", "Japan Series Game 3 was October 27 (Tuesday)"),
    ("晴れ着＝庆祝日穿的衣服", "晴れ着 = clothes for a celebration day"),
    ("波奇日从1999年开始", "Pocky Day started in 1999"),
    ("波奇日只买不分享是错的", "Pocky Day is not just about buying"),
    ("波奇日在11月11日", "Pocky Day is November 11"),
    ("波奇日在11月11日（周三）", "Pocky Day is November 11 (Wednesday)"),
    ("波奇日定在11月11日因为细长的零食像数字1", "November 11 was chosen because the thin snacks look like the number 1"),
    ("波奇日是11月11日", "Pocky Day is November 11"),
    ("波奇日要和朋友分享零食", "Pocky Day means sharing snacks with friends"),
    ("波奇＝巧克力细饼干", "a chocolate-coated stick"),
    ("ポッキー＝巧克力细饼干 d", "ポッキー = a chocolate-coated stick · d"),
    ("渡す＝递给", "渡す = to hand over"),
    ("照片长大后家人还会一起看", "The family still looks at the photos when the children are grown"),
    ("照相馆拍照的家庭是71%", "Families using a photo studio: 71%"),
    ("熊手＝祈求生意兴隆的竹耙", "熊手 = a lucky rake for thriving business"),
    ("熊手＝竹耙吉祥物 b", "熊手 = a lucky-rake charm · b"),
    ("熊手＝竹耙吉祥物 c", "熊手 = a lucky-rake charm · c"),
    ("男孩在3岁和5岁庆祝，女孩在3岁和7岁", "Boys celebrate at 3 and 5, girls at 3 and 7"),
    ("相扑场所到11月22日（周日）", "The sumo tournament runs to November 22 (Sunday)"),
    ("神社占26%", "Shrines: 26%"),
    ("第3战在横滨举行", "Game 3 was played in Yokohama"),
    ("第3战打到延长10局", "Game 3 went to the 10th inning"),
    ("第3战的再见本垒打是正木打出的", "Masaki hit the walk-off homer in Game 3"),
    ("第3战软银2-1获胜", "Game 3: SoftBank won 2–1"),
    ("第3战软银得2分", "SoftBank scored 2 in Game 3"),
    ("第4战软银4-2获胜", "Game 4: SoftBank won 4–2"),
    ("第4战软银得4分", "SoftBank scored 4 in Game 4"),
    ("第5到第7战没有举行", "Games 5 to 7 were not played"),
    ("第5战也举行了", "Game 5 was also played"),
    ("系列赛MVP是正木智也", "The Series MVP is Masaki Tomoya"),
    ("红叶见赏期从南向北移动是错的", "The leaf season moving south to north is wrong"),
    ("细长的零食把人与人连接起来", "The thin snacks connect people"),
    ("西宫神社每年5000组以上参拜", "Over 5,000 groups a year visit Nishinomiya Shrine"),
    ("見頃＝最佳观赏期", "見頃 = the best viewing season"),
    ("見頃＝最佳观赏期 c", "見頃 = the best viewing season · c"),
    ("读书周从10月27日（周二）开始", "Reading Week started October 27 (Tuesday)"),
    ("读书周在11月9日（周一）结束", "Reading Week ends November 9 (Monday)"),
    ("读书周结束后阅读习惯仍继续", "The reading habit goes on after Reading Week"),
    ("调查对象是200个七五三家庭", "The survey covered 200 Shichi-Go-San families"),
    ("调查显示11月上旬参拜占26%", "Early November visits were 26% in the survey"),
    ("调查显示71%的家庭在神社接受祈祷", "71% of families receive a shrine prayer, the survey says"),
    ("调查显示74%的家庭在照相馆拍照", "74% of families take photos at a studio, the survey says"),
    ("调查显示参拜最多的是11月上旬（26%）", "Visits peak in early November (26%), the survey says"),
    ("软银4连胜夺冠", "SoftBank won four straight to take the title"),
    ("软银第13次夺冠", "SoftBank's 13th title"),
    ("酉の市二の酉在11月19日（周四）", "Tori-no-ichi's Ni-no-tori is November 19 (Thursday)"),
    ("酉の市＝11月酉日集市 a", "酉の市 = a fair on the rooster days of November · a"),
    ("预报日期是见赏期开始的参考标准", "Forecast dates mark the start of the best season"),
    ("高尾山的红叶从11月13日（周五）前后进入见赏期", "Mt. Takao's leaves peak from around November 13 (Friday)"),
    ("高尾山的红叶从13日（周五）前后进入最佳观赏期", "Mt. Takao's leaves peak from around the 13th (Friday)"),
    ("鸣子峡已经进入见赏期", "Naruko Gorge is already at its best"),
    ("落葉＝落叶 a", "落葉 = fallen leaves · a"),
    ("プリッツ＝咸味细饼干 c", "プリッツ = a salty thin biscuit · c"),
]

PER_FILE = {
    "bslib4.py": [
        ('("译注｜" + s,', '("Note — " + s,'),
        ('"Lucerna · 日语周报 VOL.3 · LUCERNA JAPANESE WEEKLY"',
         '"Lucerna · JAPANESE WEEKLY VOL.3 · Japanese text · English explanations"'),
        ('f"第 {n} 版 / 共 {total} 版"', 'f"Page {n} of {total}"'),
    ],
    "content12.py": [
        ('p.text(975, 330, "日本語版 · VOL.3 · 七五三 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")',
         'p.text(975, 316, "日本語版 · VOL.3 · 七五三 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")\n'
         'p.text(975, 356, "TEXT IN JAPANESE · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS", 19, "sans", True, BRICK, anchor="middle")'),
        ('p.text(975, 372, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")',
         'p.text(975, 390, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")'),
        ('p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)',
         'p.hline(MX, RIGHT, 406, INK, 3); p.hline(MX, RIGHT, 413, INK, 1.2)'),
        ('"毎週、日本語で · 每周一期 · 日本人が読んでいる日本語を読む"',
         '"毎週、日本語で · Weekly · 日本人が読んでいる日本語を読む"'),
        ('"周日是七五三"', '"Sunday is Shichi-Go-San"'),
        ('"红叶最佳观赏期向南移动 · 详见第 6 版"',
         '"The leaf season moves south · See page 6"'),
        ('"トップニュース · 头条"', '"トップニュース · Top story"'),
        ('"終わる 结束 · お参り 参拜 · 移る 移动 · 熊手 竹耙吉祥物。"',
         '"終わる to end · お参り to visit a shrine · 移る to move · 熊手 a lucky rake."'),
        ('"数字で見る今週 · 数字看本周"', '"数字で見る今週 · Week in numbers"'),
        ('"今すぐ練習 · 即学即练"', '"今すぐ練習 · Practice now"'),
        ('"来源与日期见各篇文章，非精确统计"',
         '"Dates are in the articles; not exact statistics"'),
        ('"この号の内容 · 本期目录"', '"この号の内容 · In this issue"'),
        ('"全部"', '"All levels"'),
        ('"今週のことば · 本周单词"', '"今週のことば · Word of the week"'),
        ('"千歳飴＝ 七五三的红白长糖。"',
         '"千歳飴 = Shichi-Go-San\'s red-and-white candy."'),
        ('"短いニュース · 快讯"', '"短いニュース · News in brief"'),
        ('"クイズ · 闪电问答"', '"クイズ · Quick quiz"'),
        ('"读头版，选出正确答案 · 答案见第 8 版"',
         '"Read the front page and choose · Answers on page 8"'),
        ('"レベル A2 · ポッキーの日と千歳飴 · 波奇日与千岁糖"',
         '"レベル A2 · ポッキーの日と千歳飴 · Pocky Day and chitose-ame"'),
        ('"細い 细长的 · 似ている 相似 · 分け合う 分享 · 塩味 咸味。"',
         '"細い thin · 似ている to look like · 分け合う to share · 塩味 salty."'),
        ('"願い 愿望 · 撮る 拍照 · 楽しむ 享受。"',
         '"願い a wish · 撮る to take a photo · 楽しむ to enjoy."'),
        ('"你呢？11月11日想和谁分享波奇？写两句日语寄来。"',
         '"Who would you like to share Pocky with on November 11? Write two sentences in Japanese and send them in."'),
        ('"11月のことば · 11月词语"', '"11月のことば · November words"'),
        ('"「1」の日と七五三の4つの言葉 · 关于“1”之日与七五三的四个词"',
         '"「1」の日と七五三の4つの言葉 · Four words for the day of 1s and Shichi-Go-San"'),
        ('"波奇巧克力棒"', '"a chocolate-coated stick"'),
        ('"红白长糖"', '"red-and-white long candy"'),
        ('"祈求生意兴隆的竹耙"', '"a lucky rake for thriving business"'),
        ('"最佳观赏期"', '"the best viewing season"'),
        ('"練習 · 第 2 版练习"', '"練習 · Page 2 exercises"'),
    ],
    "content34.py": [
        ('"レベル A2→B1 · 七五三と酉の市 · 七五三与酉之市"',
         '"レベル A2→B1 · 七五三と酉の市 · Shichi-Go-San and Tori-no-ichi"'),
        ('"成長 成长 · 元気 健康 · 願い 愿望 · 日にち 日期。"',
         '"成長 growth · 元気 healthy · 願い a wish · 日にち the date."'),
        ('"商売繁盛 生意兴隆 · 縁起物 吉祥物 · 並ぶ 排列。"',
         '"商売繁盛 thriving business · 縁起物 a lucky charm · 並ぶ to line up."'),
        ('"你呢？七五三那天想拍什么样的照片？写两句日语寄来。"',
         '"What kind of photo would you like to take on Shichi-Go-San? Write two sentences in Japanese and send them in."'),
        ('"練習 · 第 3 版练习"', '"練習 · Page 3 exercises"'),
        ('"レベル B1 · 日本シリーズ4連勝 · 日本大赛四连胜"',
         '"レベル B1 · 日本シリーズ4連勝 · Four straight Japan Series wins"'),
        ('"接戦 势均力敌的比赛 · サヨナラ 再见（致胜） · 連続 连续。"',
         '"接戦 a close game · サヨナラ a walk-off (sayonara) · 連続 in a row."'),
        ('"日本シリーズの記録 · 大赛记录"', '"日本シリーズの記録 · Series record"'),
        ('"前号 上一期 · 全部 全部。"', '"前号 the last issue · 全部 all."'),
        ('"大相撲九州場所が始まりました · 大相扑九州场所开幕"',
         '"大相撲九州場所が始まりました · The Kyushu sumo tournament has begun"'),
        ('"練習 · 第 4 版练习"', '"練習 · Page 4 exercises"'),
    ],
    "content56.py": [
        ('"若者・エンタメ · 青年"', '"若者・エンタメ · Youth"'),
        ('"レベル B1 · 11月11日の分かち合い · 11月11日的分享"',
         '"レベル B1 · 11月11日の分かち合い · Sharing on November 11"'),
        ('"渡す 递给 · つなぐ 连接 · 送り合う 互相发送。"',
         '"渡す to hand over · つなぐ to connect · 送り合う to send each other."'),
        ('"思い出 回忆 · 大きくなる 长大。"',
         '"思い出 a memory · 大きくなる to grow up."'),
        ('"你呢？想把波奇递给谁？写两句日语寄来。"',
         '"Who would you like to hand Pocky to? Write two sentences in Japanese and send them in."'),
        ('"練習 · 第 5 版练习"', '"練習 · Page 5 exercises"'),
        ('"レベル B2 · 紅葉の見頃は南へ · 红叶最佳观赏期向南移动"',
         '"レベル B2 · 紅葉の見頃は南へ · The leaf season moves south"'),
        ('"目安 标准 · 色づき 变色 · 変化 变化 · 準備 准备。"',
         '"目安 a guide · 色づき colouring · 変化 change · 準備 preparation."'),
        ('"グラフを読もう · 读图表"', '"グラフを読もう · Reading the chart"'),
        ('"練習用データ · 练习数据"', '"練習用データ · Practice data"'),
        ('"練習 · 第 6 版练习"', '"練習 · Page 6 exercises"'),
    ],
    "content7.py": [
        ('"ことば · 语言"', '"ことば · Language"'),
        ('"言語フォーカス · 三つのレベル、三つのテーマ · 三个级别，三个主题"',
         '"言語フォーカス · 三つのレベル、三つのテーマ · Three levels, three themes"'),
        ('"読書週間 读书周 · 習慣 习惯 · 借りる 借。"',
         '"読書週間 Reading Week · 習慣 a habit · 借りる to borrow."'),
        ('"七五三 七五三 · 千歳飴 千岁糖 · 晴れ着 盛装"',
         '"七五三 Shichi-Go-San · 千歳飴 chitose-ame · 晴れ着 festive clothes"'),
        ('"〜連勝 连胜 · 〜% 百分之〜 · 〜組以上 组以上。"',
         '"〜連勝 straight wins · 〜% percent · 〜組以上 groups or more."'),
        ('"まちがい診療所 · 易错诊所"', '"まちがい診療所 · Error clinic"'),
        ('"有「昨日」时要用过去式。"', '"With 「昨日」, use the past tense."'),
        ('"动词名词化时要加「こと」。"',
         '"Add 「こと」 to turn a verb into a noun."'),
        ('"得到东西的场所用「で」。"',
         '"Use 「で」 for the place where you receive something."'),
        ('"看的场所用「で」。"', '"Use 「で」 for the place where you look."'),
        ('"今週のフレーム · 本周句式"', '"今週のフレーム · Frame of the week"'),
        ('"句式拆解：追赶最佳观赏期。"',
         '"Breakdown: chasing the best viewing season."'),
        ('"読者の手紙 · 读者园地"', '"読者の手紙 · Readers\' corner"'),
        ('ld = "※この手紙は編集部の例です。締め切りまでに、本当の読者の手紙と第8版の作文の優秀作は届きませんでした。VOL.4に載せます。"',
         'ld_en = "Editor\'s sample, not a real letter. No real letters or best '
         'Page 8 compositions had arrived by the deadline; both will appear '
         'in VOL.4. Send us your letter in Japanese — selected letters will '
         'be printed in VOL.4!"'),
        ('lcn = "编辑部示例信，非真实来信。截至截稿，未收到真实来信与第8版最佳作文；VOL.4将刊登收到的来信与佳作。"\n',
         ''),
        ('lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld, "serif", False, 20.5, CW - 44)) * 29 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26 + 16',
         'lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld_en, "sans", False, 20, CW - 44)) * 29 + 26 + 16'),
        ('yy3 = p.para(bx + 22, yy3 + 20, ld, 20.5, "serif", False, GREY, CW - 44, 1.42) + 10\n'
         'p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)',
         'p.para(bx + 22, yy3 + 20, ld_en, 20, "sans", False, GREY, CW - 44, 1.42)'),
        ('"今週のフレーズ · 本周金句（逐字摘自本期文章）"',
         '"今週のフレーズ · Phrases of the week (verbatim from this issue)"'),
        ('"读书周在11月9日星期一结束。"', '"Reading Week ends on Monday, November 9."'),
        ('"11月15日星期日是七五三的中心日。"',
         '"Sunday, November 15 is the heart of Shichi-Go-San."'),
        ('"波奇与百力滋之日始于1999年。"', '"Pocky and Pretz Day started in 1999."'),
        ('"千岁糖是寄托长寿愿望的糖果。"',
         '"Chitose-ame is the candy of the wish for a long life."'),
        ('"七五三是3岁、5岁和7岁孩子的庆祝活动。"',
         '"Shichi-Go-San celebrates children aged 3, 5 and 7."'),
        ('"软银以四连胜夺得日本第一。"',
         '"SoftBank took the Japan title with four straight wins."'),
        ('"11月11日是波奇日。"', '"November 11 is Pocky Day."'),
        ('"红叶的最佳观赏期从北向南移动。"',
         '"The best leaf season moves from north to south."'),
        ('"第1面"', '"p. 1"'),
        ('"第2面"', '"p. 2"'),
        ('"第3面"', '"p. 3"'),
        ('"第4面"', '"p. 4"'),
        ('"第5面"', '"p. 5"'),
        ('"第6面"', '"p. 6"'),
        ('"来週 · 下期预告 (VOL.4)"', '"来週 · Next issue (VOL.4)"'),
    ],
    "content8.py": [
        ('"テストと答え · 练习与答案"', '"テストと答え · Test and answers"'),
        ('"七五三是11月15日。"', '"Shichi-Go-San is November 15."'),
        ('"波奇日从1999年开始。"', '"Pocky Day started in 1999."'),
        ('"读书周从10月27日开始。→ ___"',
         '"Reading Week starts on October 27. → ___"'),
        ('"去看红叶的人可以自北向南追赶最佳观赏期。→ ___"',
         '"People going to see the leaves can chase the best season from north to south. → ___"'),
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
        ('"Lucerna-VOL3.pdf"', '"Lucerna-VOL3-EN.pdf"'),
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
    src_svg = os.path.join(CORE, "svglib.py")
    data = open(src_svg, "rb").read()
    assert hashlib.md5(data).hexdigest() == CANON_SVGLIB_MD5, "svglib md5 mismatch"
    shutil.copyfile(src_svg, os.path.join(HERE, "svglib.py"))
    shutil.copyfile(os.path.join(CORE, "run.py"), os.path.join(HERE, "run.py"))
    os.makedirs(os.path.join(HERE, "assets"), exist_ok=True)
    for f in os.listdir(os.path.join(CORE, "assets")):
        shutil.copyfile(os.path.join(CORE, "assets", f),
                        os.path.join(HERE, "assets", f))
    note_map = dict(NOTES)
    fnames = ["bslib4.py", "content12.py", "content34.py", "content56.py",
              "content7.py", "content8.py", "render.py"]
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
