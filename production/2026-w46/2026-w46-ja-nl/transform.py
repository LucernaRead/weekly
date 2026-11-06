# -*- coding: utf-8 -*-
"""JA core (VOL.3, Chinese explanations) -> JA x NL edition transform.

Re-runnable: reads the PRISTINE W46 JA core build, applies exact-literal
replacements (whole strings, never AST byte offsets), and writes the
edition build into this directory. Fix rounds edit THIS file, then
re-run: transform.py -> run.py (one process) -> render.py.

Frozen: every Japanese article/stem/option/letter/figure string is copied
byte-identical. Only the explanation layer changes: Chinese notes/glosses/
headers/instructions -> Dutch, per the W45 JA x NL shipped precedent.
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
    "files/weekly-report-w46-ja-nl")
CANON_SVGLIB_MD5 = "74177544422fe677639d769cd80499fb"

GLOBAL = [
    ("weekly-report-w46-ja-core", "weekly-report-w46-ja-nl"),
    ('instr="造句"', 'instr="Bouw een zin"'),
    ('instr="翻译"', 'instr="Vertaal"'),
    ('instr="写作"', 'instr="Schrijven"'),
    ('instr="判断"', 'instr="Waar of onwaar?"'),
    ('instr="填空"', 'instr="Vul in"'),
    ('instr="把词和释义配对"', 'instr="Koppel woord en betekenis"'),
    ('"完形单选"', '"gatentekst"'),
    ('"单选"', '"meerkeuze"'),
    ('"完成句子"', '"invullen"'),
    ('"词汇配对"', '"combineren"'),
    ('"造句"', '"zinnen bouwen"'),
    ('"判断对错"', '"waar/onwaar"'),
    ('"翻译"', '"vertalen"'),
    ('"写作"', '"schrijven"'),
    ('"あなたは？ · 说说你自己"', '"あなたは？ · Jouw beurt"'),
    ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
     '"Antwoorden op pagina 8 · Niveaus door elkaar — zoek je nummer"'),
]

NOTES = [
    ("1111中有4个1", "1111 heeft vier enen"),
    ("1111看起来像4根细棒", "1111 lijkt op vier dunne stokjes"),
    ("11月中旬以后进入见赏期的地点多比往年稍晚", "Plekken die na half november pieken, zijn meestal later dan gemiddeld"),
    ("2026年没有三の酉", "Er is geen San-no-tori in 2026"),
    ("3%≈100人中的3人", "3 % is ongeveer 3 op 100"),
    ("34+26=60", "34 + 26 = 60"),
    ("4连胜夺冠", "Vier zeges op rij brachten de titel"),
    ("4连胜＝4场比赛全胜", "alle vier wedstrijden winnen"),
    ("71%的家庭接受祈祷", "71 % van de gezinnen krijgt een gebed"),
    ("74%的家庭在照相馆拍照", "74 % van de gezinnen laat foto\'s maken in een studio"),
    ("Weathernews的预报在10月29日（周四）", "De voorspelling van Weathernews was van 29 oktober (donderdag)"),
    ("「千歳飴」受欢迎", "千歳飴 is populair"),
    ("お参りします＝去参拜", "お参りします = gaan bidden"),
    ("お参り＝去神社参拜", "お参り = naar een schrijn gaan om te bidden"),
    ("どういたしまして＝不客气", "どういたしまして = graag gedaan"),
    ("七五三是3岁5岁7岁孩子的庆祝活动", "Shichi-Go-San viert kinderen van 3, 5 en 7 jaar"),
    ("七五三是3岁、5岁、7岁孩子的庆祝活动", "Shichi-Go-San viert kinderen van 3, 5 en 7 jaar"),
    ("七五三的中心日在11月15日附近", "Shichi-Go-San draait omstreeks 15 november"),
    ("七五三的中心日是11月15日（周日）", "Shichi-Go-San draait om 15 november (zondag)"),
    ("七五三的中心日是11月15日（第3版）", "Shichi-Go-San draait om 15 november (pagina 3)"),
    ("七五三的孩子去神社参拜", "Shichi-Go-San-kinderen gaan naar een schrijn om te bidden"),
    ("七五三的照片是全家的回忆", "Shichi-Go-San-foto\'s zijn een familieherinnering"),
    ("七五三＝孩子的庆祝活动", "七五三 = een feest voor kinderen"),
    ("七五三＝3岁5岁7岁孩子的庆祝 b", "七五三 = een feest voor kinderen van 3, 5 en 7 jaar b"),
    ("东京的红叶在11月29日（周日）前后", "De bladeren in Tokio pieken rond 29 november (zondag)"),
    ("主语＋时间＋宾语＋动词", "onderwerp + tijd + voorwerp + werkwoord"),
    ("主语＋说明", "onderwerp + beschrijving"),
    ("九州场所在福冈国际中心举行", "Het Kyushu-toernooi is in het Fukuoka Kokusai Center"),
    ("二の酉在11月19日（周四）", "Ni-no-tori is 19 november (donderdag)"),
    ("分ける＝分享", "分ける = delen"),
    ("前3场比赛连续打延长赛", "De eerste drie wedstrijden gingen allemaal naar extra innings"),
    ("前3场都是延长赛", "De eerste drie wedstrijden gingen allemaal naar extra innings"),
    ("千岁糖寄托长寿的愿望", "Chitose-ame draagt een wens voor een lang leven"),
    ("千岁糖是红白相间的长糖", "Chitose-ame is een lang rood-wit snoepje"),
    ("千岁糖＝红白长糖", "lang rood-wit snoepje"),
    ("千歳飴＝红白长糖 a", "千歳飴 = lang rood-wit snoepje a"),
    ("千歳飴＝红白长糖 d", "千歳飴 = lang rood-wit snoepje d"),
    ("口号是「静かだけど、冒険中。」", "De slogan is 「静かだけど、冒険中。」"),
    ("周一读图书馆借的书", "Op maandag leest hij een bibliotheekboek"),
    ("周三和朋友分享波奇", "Op woensdag deelt hij Pocky met vrienden"),
    ("周五去高尾山看红叶", "Op vrijdag gaat hij naar de berg Takao voor de bladeren"),
    ("周日和妹妹的七五三去神社", "Op zondag gaat hij naar een schrijn voor de Shichi-Go-San van zijn zus"),
    ("四项合计100%", "De vier samen zijn 100 %"),
    ("图表中最受欢迎的是山", "Bergen staan bovenaan de grafiek"),
    ("图表是真实调查结果", "De grafiek toont echte enquêteresultaten"),
    ("在酉の市买熊手", "Een kumade kopen op Tori-no-ichi"),
    ("地点＋へ＋动词", "plaats + へ + werkwoord"),
    ("场所用「で」", "Gebruik 「で」 voor de plaats"),
    ("大阪的红叶在12月4日（周五）前后", "De bladeren in Osaka pieken rond 4 december (vrijdag)"),
    ("宫岛的红叶从11月21日（周六）前后进入见赏期", "De bladeren op Miyajima pieken vanaf ongeveer 21 november (zaterdag)"),
    ("宾语＋动词", "voorwerp + werkwoord"),
    ("对照第2版", "Zie pagina 2"),
    ("对照第3版", "Zie pagina 3"),
    ("对照第6版（追赶见赏期）", "Zie pagina 6 (de beste tijd achterna)"),
    ("对照第7版", "Zie pagina 7"),
    ("山34%与神社26%之差为8", "Bergen 34 % min heiligdommen 26 % is 8"),
    ("山占34%", "Bergen: 34 %"),
    ("岚山的红叶从11月23日（周一）前后进入见赏期", "De bladeren in Arashiyama pieken vanaf ongeveer 23 november (maandag)"),
    ("平成11年11月11日有6个1", "11 november van Heisei 11 had zes enen"),
    ("思い出＝回忆", "思い出 = een herinnering"),
    ("接戦＝比分接近的比赛", "接戦 = een spannende wedstrijd"),
    ("撮ります＝拍照", "撮ります = een foto maken"),
    ("新小结是美ノ海", "De nieuwe komusubi is Umi-no-umi"),
    ("日本大赛第3战在10月27日（周二）", "Wedstrijd 3 van de Japan Series was op 27 oktober (dinsdag)"),
    ("晴れ着＝庆祝日穿的衣服", "晴れ着 = feestkleding"),
    ("波奇日从1999年开始", "Pocky-dag begon in 1999"),
    ("波奇日只买不分享是错的", "Pocky-dag gaat niet alleen om kopen"),
    ("波奇日在11月11日", "Pocky-dag is 11 november"),
    ("波奇日在11月11日（周三）", "Pocky-dag is 11 november (woensdag)"),
    ("波奇日定在11月11日因为细长的零食像数字1", "11 november is gekozen omdat de dunne snacks op het cijfer 1 lijken"),
    ("波奇日是11月11日", "Pocky-dag is 11 november"),
    ("波奇日要和朋友分享零食", "Pocky-dag betekent snacks delen met vrienden"),
    ("波奇＝巧克力细饼干", "stokje met chocola"),
    ("ポッキー＝巧克力细饼干 d", "ポッキー = stokje met chocola d"),
    ("渡す＝递给", "渡す = overhandigen"),
    ("照片长大后家人还会一起看", "Het gezin bekijkt de foto\'s nog als de kinderen groot zijn"),
    ("照相馆拍照的家庭是71%", "Gezinnen die een studio gebruiken: 71 %"),
    ("熊手＝祈求生意兴隆的竹耙", "熊手 = gelukshark voor bloeiende zaken"),
    ("熊手＝竹耙吉祥物 b", "熊手 = gelukshark b"),
    ("熊手＝竹耙吉祥物 c", "熊手 = gelukshark c"),
    ("男孩在3岁和5岁庆祝，女孩在3岁和7岁", "Jongens vieren met 3 en 5, meisjes met 3 en 7"),
    ("相扑场所到11月22日（周日）", "Het sumotoernooi duurt tot 22 november (zondag)"),
    ("神社占26%", "Schrijnen: 26 %"),
    ("第3战在横滨举行", "Wedstrijd 3 werd gespeeld in Yokohama"),
    ("第3战打到延长10局", "Wedstrijd 3 ging naar de 10e inning"),
    ("第3战的再见本垒打是正木打出的", "Masaki sloeg de beslissende homerun in wedstrijd 3"),
    ("第3战软银2-1获胜", "Wedstrijd 3: SoftBank won met 2-1"),
    ("第3战软银得2分", "SoftBank scoorde 2 in wedstrijd 3"),
    ("第4战软银4-2获胜", "Wedstrijd 4: SoftBank won met 4-2"),
    ("第4战软银得4分", "SoftBank scoorde 4 in wedstrijd 4"),
    ("第5到第7战没有举行", "Wedstrijden 5 tot 7 werden niet gespeeld"),
    ("第5战也举行了", "Wedstrijd 5 werd ook gespeeld"),
    ("系列赛MVP是正木智也", "De MVP van de serie is Masaki Tomoya"),
    ("红叶见赏期从南向北移动是错的", "Dat het bladseizoen van zuid naar noord gaat, is fout"),
    ("细长的零食把人与人连接起来", "De dunne snacks verbinden mensen"),
    ("西宫神社每年5000组以上参拜", "Meer dan 5.000 groepen per jaar bezoeken de Nishinomiya-schrijn"),
    ("見頃＝最佳观赏期", "見頃 = de beste kijktijd"),
    ("見頃＝最佳观赏期 c", "見頃 = de beste kijktijd c"),
    ("读书周从10月27日（周二）开始", "De Leesweek begon op 27 oktober (dinsdag)"),
    ("读书周在11月9日（周一）结束", "De Leesweek eindigt op 9 november (maandag)"),
    ("读书周结束后阅读习惯仍继续", "De leesgewoonte gaat door na de Leesweek"),
    ("调查对象是200个七五三家庭", "De enquête omvatte 200 Shichi-Go-San-gezinnen"),
    ("调查显示11月上旬参拜占26%", "Bezoeken begin november waren 26 % in de enquête"),
    ("调查显示71%的家庭在神社接受祈祷", "71 % van de gezinnen krijgt een gebed in de schrijn, zegt de enquête"),
    ("调查显示74%的家庭在照相馆拍照", "74 % van de gezinnen laat foto\'s maken in een studio, zegt de enquête"),
    ("调查显示参拜最多的是11月上旬（26%）", "Bezoeken pieken begin november (26 %), zegt de enquête"),
    ("软银4连胜夺冠", "Vier zeges op rij voor de titel"),
    ("软银第13次夺冠", "De 13e titel van SoftBank"),
    ("酉の市二の酉在11月19日（周四）", "De Ni-no-tori van Tori-no-ichi is 19 november (donderdag)"),
    ("酉の市＝11月酉日集市 a", "酉の市 = een markt op de hanendagen van november a"),
    ("预报日期是见赏期开始的参考标准", "Voorspelde data markeren het begin van de beste tijd"),
    ("高尾山的红叶从11月13日（周五）前后进入见赏期", "De bladeren van de berg Takao pieken vanaf ongeveer 13 november (vrijdag)"),
    ("高尾山的红叶从13日（周五）前后进入最佳观赏期", "De bladeren van de berg Takao pieken vanaf ongeveer de 13e (vrijdag)"),
    ("鸣子峡已经进入见赏期", "De Naruko-kloof is al op zijn best"),
    ("落葉＝落叶 a", "落葉 = gevallen bladeren a"),
    ("プリッツ＝咸味细饼干 c", "プリッツ = zout dun koekje c"),
]

PER_FILE = {
    "bslib4.py": [
        ('("译注｜" + s,', '("Uitleg — " + s,'),
        ('"Lucerna · 日语周报 VOL.3 · LUCERNA JAPANESE WEEKLY"',
         '"Lucerna · JAPANS WEEKBLAD VOL.3 · TEKSTEN IN HET JAPANS · UITLEG IN HET NEDERLANDS"'),
        ('f"第 {n} 版 / 共 {total} 版"', 'f"Pagina {n} van {total}"'),
    ],
    "content12.py": [
        ('p.text(975, 330, "日本語版 · VOL.3 · 七五三 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")',
         'p.text(975, 316, "日本語版 · VOL.3 · 七五三 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")\n'
         'p.text(975, 356, "TEKSTEN IN HET JAPANS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS", 19, "sans", True, BRICK, anchor="middle")'),
        ('p.text(975, 372, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")',
         'p.text(975, 390, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")'),
        ('p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)',
         'p.hline(MX, RIGHT, 406, INK, 3); p.hline(MX, RIGHT, 413, INK, 1.2)'),
        ('"毎週、日本語で · 每周一期 · 日本人が読んでいる日本語を読む"',
         '"毎週、日本語で · Elke week · 日本人が読んでいる日本語を読む"'),
        ('"周日是七五三"', '"Zondag is Shichi-Go-San"'),
        ('"红叶最佳观赏期向南移动 · 详见第 6 版"',
         '"Het bladseizoen gaat naar het zuiden · Zie pagina 6"'),
        ('"トップニュース · 头条"', '"トップニュース · Hoofdnieuws"'),
        ('"終わる 结束 · お参り 参拜 · 移る 移动 · 熊手 竹耙吉祥物。"',
         '"終わる eindigen · お参り een schrijn bezoeken · 移る verplaatsen · 熊手 gelukshark."'),
        ('"数字で見る今週 · 数字看本周"', '"数字で見る今週 · De week in cijfers"'),
        ('"今すぐ練習 · 即学即练"', '"今すぐ練習 · Oefen nu"'),
        ('"来源与日期见各篇文章，非精确统计"',
         '"Data in de artikelen; geen exacte cijfers"'),
        ('"この号の内容 · 本期目录"', '"この号の内容 · In dit nummer"'),
        ('"全部"', '"Alle niveaus"'),
        ('"今週のことば · 本周单词"', '"今週のことば · Woord van de week"'),
        ('"千歳飴＝ 七五三的红白长糖。"',
         '"千歳飴 = rood-wit snoepje van Shichi-Go-San."'),
        ('"短いニュース · 快讯"', '"短いニュース · Kort nieuws"'),
        ('"クイズ · 闪电问答"', '"クイズ · Snelle quiz"'),
        ('"读头版，选出正确答案 · 答案见第 8 版"',
         '"Lees de voorpagina en kies · Antwoorden op pagina 8"'),
        ('"レベル A2 · ポッキーの日と千歳飴 · 波奇日与千岁糖"',
         '"レベル A2 · ポッキーの日と千歳飴 · Pocky-dag en chitose-ame"'),
        ('"細い 细长的 · 似ている 相似 · 分け合う 分享 · 塩味 咸味。"',
         '"細い dun · 似ている lijken op · 分け合う delen · 塩味 zout."'),
        ('"願い 愿望 · 撮る 拍照 · 楽しむ 享受。"',
         '"願い een wens · 撮る een foto maken · 楽しむ genieten."'),
        ('"你呢？11月11日想和谁分享波奇？写两句日语寄来。"',
         '"Met wie wil je op 11 november Pocky delen? Schrijf twee zinnen in het Japans en stuur ze in."'),
        ('"11月のことば · 11月词语"', '"11月のことば · Novemberwoorden"'),
        ('"「1」の日と七五三の4つの言葉 · 关于“1”之日与七五三的四个词"',
         '"「1」の日と七五三の4つの言葉 · Vier woorden voor de dag van de enen en Shichi-Go-San"'),
        ('"波奇巧克力棒"', '"stokje met chocola"'),
        ('"红白长糖"', '"lang rood-wit snoepje"'),
        ('"祈求生意兴隆的竹耙"', '"gelukshark voor bloeiende zaken"'),
        ('"最佳观赏期"', '"de beste kijktijd"'),
        ('"練習 · 第 2 版练习"', '"練習 · Oefeningen pagina 2"'),
    ],
    "content34.py": [
        ('"レベル A2→B1 · 七五三と酉の市 · 七五三与酉之市"',
         '"レベル A2→B1 · 七五三と酉の市 · Shichi-Go-San en Tori-no-ichi"'),
        ('"成長 成长 · 元気 健康 · 願い 愿望 · 日にち 日期。"',
         '"成長 groei · 元気 gezond · 願い een wens · 日にち de datum."'),
        ('"商売繁盛 生意兴隆 · 縁起物 吉祥物 · 並ぶ 排列。"',
         '"商売繁盛 bloeiende zaken · 縁起物 geluksbrenger · 並ぶ in de rij staan."'),
        ('"你呢？七五三那天想拍什么样的照片？写两句日语寄来。"',
         '"Wat voor foto wil je maken met Shichi-Go-San? Schrijf twee zinnen in het Japans en stuur ze in."'),
        ('"練習 · 第 3 版练习"', '"練習 · Oefeningen pagina 3"'),
        ('"レベル B1 · 日本シリーズ4連勝 · 日本大赛四连胜"',
         '"レベル B1 · 日本シリーズ4連勝 · Vier zeges op rij in de Japan Series"'),
        ('"接戦 势均力敌的比赛 · サヨナラ 再见（致胜） · 連続 连续。"',
         '"接戦 spannende wedstrijd · サヨナラ beslissende homerun (sayonara) · 連続 op rij."'),
        ('"日本シリーズの記録 · 大赛记录"', '"日本シリーズの記録 · Balans"'),
        ('"前号 上一期 · 全部 全部。"', '"前号 het vorige nummer · 全部 alles."'),
        ('"大相撲九州場所が始まりました · 大相扑九州场所开幕"',
         '"大相撲九州場所が始まりました · Het sumotoernooi van Kyushu is begonnen"'),
        ('"練習 · 第 4 版练习"', '"練習 · Oefeningen pagina 4"'),
    ],
    "content56.py": [
        ('"若者・エンタメ · 青年"', '"若者・エンタメ · Jongeren"'),
        ('"レベル B1 · 11月11日の分かち合い · 11月11日的分享"',
         '"レベル B1 · 11月11日の分かち合い · Delen op 11 november"'),
        ('"渡す 递给 · つなぐ 连接 · 送り合う 互相发送。"',
         '"渡す overhandigen · つなぐ verbinden · 送り合う elkaar sturen."'),
        ('"思い出 回忆 · 大きくなる 长大。"',
         '"思い出 een herinnering · 大きくなる opgroeien."'),
        ('"你呢？想把波奇递给谁？写两句日语寄来。"',
         '"Aan wie wil je Pocky geven? Schrijf twee zinnen in het Japans en stuur ze in."'),
        ('"練習 · 第 5 版练习"', '"練習 · Oefeningen pagina 5"'),
        ('"レベル B2 · 紅葉の見頃は南へ · 红叶最佳观赏期向南移动"',
         '"レベル B2 · 紅葉の見頃は南へ · Het bladseizoen gaat naar het zuiden"'),
        ('"目安 标准 · 色づき 变色 · 変化 变化 · 準備 准备。"',
         '"目安 een richtlijn · 色づき verkleuring · 変化 verandering · 準備 voorbereiding."'),
        ('"グラフを読もう · 读图表"', '"グラフを読もう · De grafiek lezen"'),
        ('"練習用データ · 练习数据"', '"練習用データ · Oefendata"'),
        ('"練習 · 第 6 版练习"', '"練習 · Oefeningen pagina 6"'),
    ],
    "content7.py": [
        ('"ことば · 语言"', '"ことば · Taal"'),
        ('"言語フォーカス · 三つのレベル、三つのテーマ · 三个级别，三个主题"',
         '"言語フォーカス · 三つのレベル、三つのテーマ · Drie niveaus, drie thema\'s"'),
        ('"読書週間 读书周 · 習慣 习惯 · 借りる 借。"',
         '"読書週間 Leesweek · 習慣 een gewoonte · 借りる lenen."'),
        ('"七五三 七五三 · 千歳飴 千岁糖 · 晴れ着 盛装"',
         '"七五三 Shichi-Go-San · 千歳飴 chitose-ame · 晴れ着 feestkleding"'),
        ('"〜連勝 连胜 · 〜% 百分之〜 · 〜組以上 组以上。"',
         '"〜連勝 zeges op rij · 〜% procent · 〜組以上 groepen of meer."'),
        ('"まちがい診療所 · 易错诊所"', '"まちがい診療所 · Foutenkliniek"'),
        ('"有「昨日」时要用过去式。"', '"Gebruik met 「昨日」 de verleden tijd."'),
        ('"动词名词化时要加「こと」。"',
         '"Voeg 「こと」 toe om van een werkwoord een zelfstandig naamwoord te maken."'),
        ('"得到东西的场所用「で」。"',
         '"Gebruik 「で」 voor de plaats waar je iets krijgt."'),
        ('"看的场所用「で」。"', '"Gebruik 「で」 voor de plaats waar je kijkt."'),
        ('"今週のフレーム · 本周句式"', '"今週のフレーム · Kader van de week"'),
        ('"句式拆解：追赶最佳观赏期。"',
         '"Uitleg: de beste kijktijd achterna."'),
        ('"読者の手紙 · 读者园地"', '"読者の手紙 · Lezershoek"'),
        ('ld = "※この手紙は編集部の例です。締め切りまでに、本当の読者の手紙と第8版の作文の優秀作は届きませんでした。VOL.4に載せます。"',
         'ld_nl = "Voorbeeld van de redactie, geen echte brief. Tot de deadline '
         'kwamen er geen echte brieven en geen beste opstellen; beide '
         'verschijnen in VOL.4. Stuur ons je brief in het Japans: de '
         'gekozen brieven worden afgedrukt in VOL.4!"'),
        ('lcn = "编辑部示例信，非真实来信。截至截稿，未收到真实来信与第8版最佳作文；VOL.4将刊登收到的来信与佳作。"\n',
         ''),
        ('lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld, "serif", False, 20.5, CW - 44)) * 29 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26 + 16',
         'lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld_nl, "sans", False, 20, CW - 44)) * 29 + 26 + 16'),
        ('yy3 = p.para(bx + 22, yy3 + 20, ld, 20.5, "serif", False, GREY, CW - 44, 1.42) + 10\n'
         'p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)',
         'p.para(bx + 22, yy3 + 20, ld_nl, 20, "sans", False, GREY, CW - 44, 1.42)'),
        ('"今週のフレーズ · 本周金句（逐字摘自本期文章）"',
         '"今週のフレーズ · Zinnen van de week (letterlijk uit dit nummer)"'),
        ('"读书周在11月9日星期一结束。"', '"De Leesweek eindigt op maandag 9 november."'),
        ('"11月15日星期日是七五三的中心日。"',
         '"Zondag 15 november is het hart van Shichi-Go-San."'),
        ('"波奇与百力滋之日始于1999年。"', '"Pocky- en Pretz-dag begon in 1999."'),
        ('"千岁糖是寄托长寿愿望的糖果。"',
         '"Chitose-ame is het snoepje van de wens voor een lang leven."'),
        ('"七五三是3岁、5岁和7岁孩子的庆祝活动。"',
         '"Shichi-Go-San viert kinderen van 3, 5 en 7 jaar."'),
        ('"软银以四连胜夺得日本第一。"',
         '"SoftBank pakte de Japanse titel met vier zeges op rij."'),
        ('"11月11日是波奇日。"', '"11 november is Pocky-dag."'),
        ('"红叶的最佳观赏期从北向南移动。"',
         '"De beste bladtijd gaat van noord naar zuid."'),
        ('"第1面"', '"p. 1"'),
        ('"第2面"', '"p. 2"'),
        ('"第3面"', '"p. 3"'),
        ('"第4面"', '"p. 4"'),
        ('"第5面"', '"p. 5"'),
        ('"第6面"', '"p. 6"'),
        ('"来週 · 下期预告 (VOL.4)"', '"来週 · Volgend nummer (VOL.4)"'),
    ],
    "content8.py": [
        ('af.para(f"— 第{pg}面 —", 13.3, "sans", True, OLIVE, lh=1.16, gap=2, split=False)', 'af.para(f"— 第{pg}面 —", 12.9, "sans", True, OLIVE, lh=1.13, gap=2, split=False)'),
        ('af.para(txt, 13.3, lh=1.16, gap=0.5, split=False)', 'af.para(txt, 12.9, lh=1.13, gap=0.5, split=False)'),
        ('"テストと答え · 练习与答案"', '"テストと答え · Test en antwoorden"'),
        ('"七五三是11月15日。"', '"Shichi-Go-San is 15 november."'),
        ('"波奇日从1999年开始。"', '"Pocky-dag begon in 1999."'),
        ('"读书周从10月27日开始。→ ___"',
         '"De Leesweek begint op 27 oktober. → ___"'),
        ('"去看红叶的人可以自北向南追赶最佳观赏期。→ ___"',
         '"Wie de bladeren gaat bekijken, kan de beste tijd achterna gaan van noord naar zuid. → ___"'),
        ('f"写作题（无唯一答案）；范文（{NCHARS} 字）见下。"',
         'f"Schrijfopdracht (geen enkel juist antwoord); de modeltekst ({NCHARS} tekens) staat hieronder."'),
        ('"（开放题，范文如下）"', '"(open opdracht — modeltekst hieronder)"'),
        ('f"范文见本版 H 区（{NCHARS} 字）"',
         'f"Modeltekst in deel H op deze pagina ({NCHARS} tekens)"'),
        ('"答え · 参考答案 — 按版面分页排列，找到题号即可"',
         '"答え · Antwoorden — per pagina gegroepeerd; zoek gewoon je nummer"'),
        ('"每题附一句中文简析 · 带 ✓ 的为范文题"',
         '"Een korte Nederlandse toelichting bij elk antwoord · ✓ = de opdracht met modeltekst"'),
        ('f"— 第{pg}面 —"', 'f"— Pagina {pg} —"'),
    ],
    "render.py": [
        ('"Lucerna-VOL3.pdf"', '"Lucerna-VOL3-NL.pdf"'),
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
