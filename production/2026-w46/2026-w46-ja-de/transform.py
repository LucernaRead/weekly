# -*- coding: utf-8 -*-
"""JA core (VOL.3, Chinese explanations) -> JA x DE edition transform.

Re-runnable: reads the PRISTINE W46 JA core build, applies exact-literal
replacements (whole strings, never AST byte offsets), and writes the
edition build into this directory. Fix rounds edit THIS file, then
re-run: transform.py -> run.py (one process) -> render.py.

Frozen: every Japanese article/stem/option/letter/figure string is copied
byte-identical. Only the explanation layer changes: Chinese notes/glosses/
headers/instructions -> German, per the W45 JA x DE shipped precedent.
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
    "files/weekly-report-w46-ja-de")
CANON_SVGLIB_MD5 = "74177544422fe677639d769cd80499fb"

GLOBAL = [
    ("weekly-report-w46-ja-core", "weekly-report-w46-ja-de"),
    ('instr="造句"', 'instr="Satz bilden"'),
    ('instr="翻译"', 'instr="Übersetzen"'),
    ('instr="写作"', 'instr="Schreiben"'),
    ('instr="判断"', 'instr="Richtig/Falsch"'),
    ('instr="填空"', 'instr="Ausfüllen"'),
    ('instr="把词和释义配对"', 'instr="Wörter zuordnen"'),
    ('"完形单选"', '"Lückentext"'),
    ('"单选"', '"Multiple Choice"'),
    ('"完成句子"', '"Ausfüllen"'),
    ('"词汇配对"', '"Zuordnen"'),
    ('"造句"', '"Satzbau"'),
    ('"判断对错"', '"Richtig/Falsch"'),
    ('"翻译"', '"Übersetzen"'),
    ('"写作"', '"Schreiben"'),
    ('"あなたは？ · 说说你自己"', '"あなたは？ · Und du?"'),
    ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
     '"Antworten auf Seite 8 · Stufen gemischt — nach Nummer suchen"'),
]

NOTES = [
    ("1111中有4个1", "1111 hat vier Einsen"),
    ("1111看起来像4根细棒", "1111 sieht aus wie vier dünne Stäbchen"),
    ("11月中旬以后进入见赏期的地点多比往年稍晚", "Orte ab Mitte November sind meist später dran"),
    ("2026年没有三の酉", "2026 gibt es kein San-no-tori"),
    ("3%≈100人中的3人", "3 % sind etwa 3 von 100"),
    ("34+26=60", "34 + 26 = 60"),
    ("4连胜夺冠", "Vier Siege in Folge brachten den Titel"),
    ("4连胜＝4场比赛全胜", "alle vier Spiele gewonnen"),
    ("71%的家庭接受祈祷", "71 % der Familien erhalten ein Gebet"),
    ("74%的家庭在照相馆拍照", "74 % der Familien lassen Fotos im Studio machen"),
    ("Weathernews的预报在10月29日（周四）", "Die Weathernews-Prognose war vom 29. Oktober (Donnerstag)"),
    ("「千歳飴」受欢迎", "千歳飴 ist beliebt"),
    ("お参りします＝去参拜", "お参りします = zum Beten gehen"),
    ("お参り＝去神社参拜", "お参り = zum Beten zum Schrein gehen"),
    ("どういたしまして＝不客气", "どういたしまして = gern geschehen"),
    ("七五三是3岁5岁7岁孩子的庆祝活动", "Shichi-Go-San feiert Kinder von 3, 5 und 7 Jahren"),
    ("七五三是3岁、5岁、7岁孩子的庆祝活动", "Shichi-Go-San feiert Kinder von 3, 5 und 7 Jahren"),
    ("七五三的中心日在11月15日附近", "Shichi-Go-San findet um den 15. November statt"),
    ("七五三的中心日是11月15日（周日）", "Shichi-Go-San findet am 15. November (Sonntag) statt"),
    ("七五三的中心日是11月15日（第3版）", "Shichi-Go-San ist am 15. November (Seite 3)"),
    ("七五三的孩子去神社参拜", "Shichi-Go-San-Kinder gehen zum Beten zum Schrein"),
    ("七五三的照片是全家的回忆", "Shichi-Go-San-Fotos sind eine Familienerinnerung"),
    ("七五三＝孩子的庆祝活动", "七五三 = ein Fest für Kinder"),
    ("七五三＝3岁5岁7岁孩子的庆祝 b", "七五三 = ein Fest für Kinder von 3, 5 und 7 Jahren b"),
    ("东京的红叶在11月29日（周日）前后", "Tokios Laub erreicht um den 29. November (Sonntag) seinen Höhepunkt"),
    ("主语＋时间＋宾语＋动词", "Subjekt + Zeit + Objekt + Verb"),
    ("主语＋说明", "Subjekt + Beschreibung"),
    ("九州场所在福冈国际中心举行", "Das Kyushu-Turnier findet im Fukuoka Kokusai Center statt"),
    ("二の酉在11月19日（周四）", "Ni-no-tori ist am 19. November (Donnerstag)"),
    ("分ける＝分享", "分ける = teilen"),
    ("前3场比赛连续打延长赛", "Die ersten drei Spiele gingen alle in die Verlängerung"),
    ("前3场都是延长赛", "Die ersten drei Spiele gingen alle in die Verlängerung"),
    ("千岁糖寄托长寿的愿望", "Chitose-ame trägt den Wunsch nach einem langen Leben"),
    ("千岁糖是红白相间的长糖", "Chitose-ame ist ein langes rot-weißes Bonbon"),
    ("千岁糖＝红白长糖", "rot-weißes langes Bonbon"),
    ("千歳飴＝红白长糖 a", "千歳飴 = rot-weißes langes Bonbon a"),
    ("千歳飴＝红白长糖 d", "千歳飴 = rot-weißes langes Bonbon d"),
    ("口号是「静かだけど、冒険中。」", "Der Slogan lautet 「静かだけど、冒険中。」"),
    ("周一读图书馆借的书", "Am Montag liest er ein Buch aus der Bibliothek"),
    ("周三和朋友分享波奇", "Am Mittwoch teilt er Pocky mit Freunden"),
    ("周五去高尾山看红叶", "Am Freitag geht er auf den Berg Takao"),
    ("周日和妹妹的七五三去神社", "Am Sonntag geht er zum Schrein"),
    ("四项合计100%", "Alle vier ergeben zusammen 100 %"),
    ("图表中最受欢迎的是山", "Berge führen die Grafik an"),
    ("图表是真实调查结果", "Die Grafik zeigt echte Umfrageergebnisse"),
    ("在酉の市买熊手", "Einen Kumade auf dem Tori-no-ichi kaufen"),
    ("地点＋へ＋动词", "Ort + へ + Verb"),
    ("场所用「で」", "「で」 für den Ort"),
    ("大阪的红叶在12月4日（周五）前后", "Osakas Laub erreicht um den 4. Dezember (Freitag) seinen Höhepunkt"),
    ("宫岛的红叶从11月21日（周六）前后进入见赏期", "Miyajimas Laub erreicht ab um den 21. November (Samstag) seinen Höhepunkt"),
    ("宾语＋动词", "Objekt + Verb"),
    ("对照第2版", "Siehe Seite 2"),
    ("对照第3版", "Siehe Seite 3"),
    ("对照第6版（追赶见赏期）", "Siehe Seite 6"),
    ("对照第7版", "Siehe Seite 7"),
    ("山34%与神社26%之差为8", "Berge 34 % minus Schreine 26 % ergibt 8"),
    ("山占34%", "Berge: 34 %"),
    ("岚山的红叶从11月23日（周一）前后进入见赏期", "Arashiyamas Laub erreicht ab um den 23. November (Montag) seinen Höhepunkt"),
    ("平成11年11月11日有6个1", "Am 11. November im Jahr Heisei 11 gab es sechs Einsen"),
    ("思い出＝回忆", "思い出 = eine Erinnerung"),
    ("接戦＝比分接近的比赛", "接戦 = ein enges Spiel"),
    ("撮ります＝拍照", "撮ります = fotografieren"),
    ("新小结是美ノ海", "Der neue Komusubi ist Umi-no-umi"),
    ("日本大赛第3战在10月27日（周二）", "Spiel 3 der Japan Series war am 27. Oktober (Dienstag)"),
    ("晴れ着＝庆祝日穿的衣服", "晴れ着 = Kleidung für einen Festtag"),
    ("波奇日从1999年开始", "Der Pocky-Tag begann 1999"),
    ("波奇日只买不分享是错的", "Der Pocky-Tag ist nicht nur Kaufen"),
    ("波奇日在11月11日", "Der Pocky-Tag ist am 11. November"),
    ("波奇日在11月11日（周三）", "Der Pocky-Tag ist am 11. November (Mittwoch)"),
    ("波奇日定在11月11日因为细长的零食像数字1", "Gewählt, weil die Snacks wie die Ziffer 1 aussehen"),
    ("波奇日是11月11日", "Der Pocky-Tag ist am 11. November"),
    ("波奇日要和朋友分享零食", "Pocky-Tag heißt: Snacks mit Freunden teilen"),
    ("波奇＝巧克力细饼干", "Schokostange"),
    ("ポッキー＝巧克力细饼干 d", "ポッキー = Schokostange d"),
    ("渡す＝递给", "渡す = überreichen"),
    ("照片长大后家人还会一起看", "Die Familie sieht die Fotos auch später noch an"),
    ("照相馆拍照的家庭是71%", "Familien mit Fotostudio: 71 %"),
    ("熊手＝祈求生意兴隆的竹耙", "熊手 = Glücksrechen für gute Geschäfte"),
    ("熊手＝竹耙吉祥物 b", "熊手 = Glücksrechen b"),
    ("熊手＝竹耙吉祥物 c", "熊手 = Glücksrechen c"),
    ("男孩在3岁和5岁庆祝，女孩在3岁和7岁", "Jungen feiern mit 3 und 5, Mädchen mit 3 und 7"),
    ("相扑场所到11月22日（周日）", "Das Sumoturnier läuft bis zum 22. November (Sonntag)"),
    ("神社占26%", "Schreine: 26 %"),
    ("第3战在横滨举行", "Spiel 3 fand in Yokohama statt"),
    ("第3战打到延长10局", "Spiel 3 ging bis ins 10. Inning"),
    ("第3战的再见本垒打是正木打出的", "Masaki schlug den Walk-off-Homerun in Spiel 3"),
    ("第3战软银2-1获胜", "Spiel 3: SoftBank gewann 2:1"),
    ("第3战软银得2分", "SoftBank erzielte 2 Punkte in Spiel 3"),
    ("第4战软银4-2获胜", "Spiel 4: SoftBank gewann 4:2"),
    ("第4战软银得4分", "SoftBank erzielte 4 Punkte in Spiel 4"),
    ("第5到第7战没有举行", "Die Spiele 5 bis 7 fanden nicht statt"),
    ("第5战也举行了", "Spiel 5 fand auch statt"),
    ("系列赛MVP是正木智也", "MVP der Serie ist Masaki Tomoya"),
    ("红叶见赏期从南向北移动是错的", "Dass die Laubzeit von Süden nach Norden zieht, ist falsch"),
    ("细长的零食把人与人连接起来", "Die dünnen Snacks verbinden Menschen"),
    ("西宫神社每年5000组以上参拜", "Über 5.000 Gruppen im Jahr besuchen den Nishinomiya-Schrein"),
    ("見頃＝最佳观赏期", "見頃 = beste Laubzeit"),
    ("見頃＝最佳观赏期 c", "見頃 = beste Laubzeit c"),
    ("读书周从10月27日（周二）开始", "Die Lesewoche begann am 27. Oktober (Dienstag)"),
    ("读书周在11月9日（周一）结束", "Die Lesewoche endet am 9. November (Montag)"),
    ("读书周结束后阅读习惯仍继续", "Die Lesegewohnheit geht nach der Lesewoche weiter"),
    ("调查对象是200个七五三家庭", "Die Umfrage erfasste 200 Shichi-Go-San-Familien"),
    ("调查显示11月上旬参拜占26%", "Besuche Anfang November lagen in der Umfrage bei 26 %"),
    ("调查显示71%的家庭在神社接受祈祷", "71 % der Familien erhalten laut Umfrage ein Gebet im Schrein"),
    ("调查显示74%的家庭在照相馆拍照", "74 % lassen Fotos im Studio machen"),
    ("调查显示参拜最多的是11月上旬（26%）", "Besuche häufen sich Anfang November (26 %)"),
    ("软银4连胜夺冠", "Vier Siege in Folge zum Titel"),
    ("软银第13次夺冠", "SoftBanks 13. Titel"),
    ("酉の市二の酉在11月19日（周四）", "Ni-no-tori des Tori-no-ichi ist am 19. November (Donnerstag)"),
    ("酉の市＝11月酉日集市 a", "酉の市 = ein Fest an den Hahntagen im November a"),
    ("预报日期是见赏期开始的参考标准", "Prognosedaten markieren den Beginn der besten Zeit"),
    ("高尾山的红叶从11月13日（周五）前后进入见赏期", "Der Berg Takao erreicht seine Laubzeit ab um den 13. November (Freitag)"),
    ("高尾山的红叶从13日（周五）前后进入最佳观赏期", "Der Berg Takao erreicht seine Laubzeit ab um den 13. (Freitag)"),
    ("鸣子峡已经进入见赏期", "Die Naruko-Schlucht ist schon auf ihrem Höhepunkt"),
    ("落葉＝落叶 a", "落葉 = gefallenes Laub a"),
    ("プリッツ＝咸味细饼干 c", "プリッツ = salziges dünnes Gebäck c"),
]

PER_FILE = {
    "bslib4.py": [
        ('("译注｜" + s,', '("Anm. — " + s,'),
        ('"Lucerna · 日语周报 VOL.3 · LUCERNA JAPANESE WEEKLY"',
         '"Lucerna · JAPANISCHE WOCHENZEITUNG VOL.3 · TEXT AUF JAPANISCH · ERKLÄRUNGEN AUF DEUTSCH"'),
        ('f"第 {n} 版 / 共 {total} 版"', 'f"Seite {n} von {total}"'),
    ],
    "content12.py": [
        ('p.text(975, 330, "日本語版 · VOL.3 · 七五三 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")',
         'p.text(975, 316, "日本語版 · VOL.3 · 七五三 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")\n'
         'p.text(975, 356, "JAPANISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER", 19, "sans", True, BRICK, anchor="middle")'),
        ('p.text(975, 372, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")',
         'p.text(975, 390, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")'),
        ('p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)',
         'p.hline(MX, RIGHT, 406, INK, 3); p.hline(MX, RIGHT, 413, INK, 1.2)'),
        ('"毎週、日本語で · 每周一期 · 日本人が読んでいる日本語を読む"',
         '"毎週、日本語で · Jede Woche · 日本人が読んでいる日本語を読む"'),
        ('"周日是七五三"', '"Sonntag ist Shichi-Go-San"'),
        ('"红叶最佳观赏期向南移动 · 详见第 6 版"',
         '"Die Laubzeit zieht nach Süden · Siehe Seite 6"'),
        ('"トップニュース · 头条"', '"トップニュース · Topmeldung"'),
        ('"終わる 结束 · お参り 参拜 · 移る 移动 · 熊手 竹耙吉祥物。"',
         '"終わる enden · お参り zum Schrein gehen · 移る sich verlagern · 熊手 Glücksrechen."'),
        ('"数字で見る今週 · 数字看本周"', '"数字で見る今週 · Woche in Zahlen"'),
        ('"今すぐ練習 · 即学即练"', '"今すぐ練習 · Jetzt üben"'),
        ('"来源与日期见各篇文章，非精确统计"',
         '"Daten in den Artikeln; keine exakte Statistik"'),
        ('"この号の内容 · 本期目录"', '"この号の内容 · In dieser Ausgabe"'),
        ('"全部"', '"Alle Stufen"'),
        ('"今週のことば · 本周单词"', '"今週のことば · Wort der Woche"'),
        ('"千歳飴＝ 七五三的红白长糖。"',
         '"千歳飴 = rot-weißes Shichi-Go-San-Bonbon."'),
        ('"短いニュース · 快讯"', '"短いニュース · Kurznachrichten"'),
        ('"クイズ · 闪电问答"', '"クイズ · Kurzquiz"'),
        ('"读头版，选出正确答案 · 答案见第 8 版"',
         '"Lies die Titelseite und wähle · Antworten auf Seite 8"'),
        ('"レベル A2 · ポッキーの日と千歳飴 · 波奇日与千岁糖"',
         '"レベル A2 · ポッキーの日と千歳飴 · Pocky-Tag und Chitose-ame"'),
        ('"細い 细长的 · 似ている 相似 · 分け合う 分享 · 塩味 咸味。"',
         '"細い dünn · 似ている ähneln · 分け合う teilen · 塩味 salzig."'),
        ('"願い 愿望 · 撮る 拍照 · 楽しむ 享受。"',
         '"願い ein Wunsch · 撮る fotografieren · 楽しむ genießen."'),
        ('"你呢？11月11日想和谁分享波奇？写两句日语寄来。"',
         '"Mit wem möchtest du am 11. November Pocky teilen? Schreibe zwei Sätze auf Japanisch und schicke sie ein."'),
        ('"11月のことば · 11月词语"', '"11月のことば · Novemberwörter"'),
        ('"「1」の日と七五三の4つの言葉 · 关于“1”之日与七五三的四个词"',
         '"「1」の日と七五三の4つの言葉 · Vier Wörter zum Tag der Einsen und zu Shichi-Go-San"'),
        ('"波奇巧克力棒"', '"Schokostange"'),
        ('"红白长糖"', '"rot-weißes langes Bonbon"'),
        ('"祈求生意兴隆的竹耙"', '"Glücksrechen für gute Geschäfte"'),
        ('"最佳观赏期"', '"beste Laubzeit"'),
        ('"練習 · 第 2 版练习"', '"練習 · Übungen Seite 2"'),
    ],
    "content34.py": [
        ('"レベル A2→B1 · 七五三と酉の市 · 七五三与酉之市"',
         '"レベル A2→B1 · 七五三と酉の市 · Shichi-Go-San und Tori-no-ichi"'),
        ('"成長 成长 · 元気 健康 · 願い 愿望 · 日にち 日期。"',
         '"成長 Wachstum · 元気 gesund · 願い ein Wunsch · 日にち das Datum."'),
        ('"商売繁盛 生意兴隆 · 縁起物 吉祥物 · 並ぶ 排列。"',
         '"商売繁盛 blühende Geschäfte · 縁起物 Glücksbringer · 並ぶ sich anstellen."'),
        ('"你呢？七五三那天想拍什么样的照片？写两句日语寄来。"',
         '"Welches Foto möchtest du an Shichi-Go-San machen? Schreibe zwei Sätze auf Japanisch und schicke sie ein."'),
        ('"練習 · 第 3 版练习"', '"練習 · Übungen Seite 3"'),
        ('"レベル B1 · 日本シリーズ4連勝 · 日本大赛四连胜"',
         '"レベル B1 · 日本シリーズ4連勝 · Vier Siege in Folge in der Japan Series"'),
        ('"接戦 势均力敌的比赛 · サヨナラ 再见（致胜） · 連続 连续。"',
         '"接戦 ein enges Spiel · サヨナラ Walk-off (Sayonara) · 連続 in Folge."'),
        ('"日本シリーズの記録 · 大赛记录"', '"日本シリーズの記録 · Bilanz"'),
        ('"前号 上一期 · 全部 全部。"', '"前号 die letzte Ausgabe · 全部 alles."'),
        ('"大相撲九州場所が始まりました · 大相扑九州场所开幕"',
         '"大相撲九州場所が始まりました · Das Kyushu-Sumoturnier hat begonnen"'),
        ('"練習 · 第 4 版练习"', '"練習 · Übungen Seite 4"'),
    ],
    "content56.py": [
        ('"若者・エンタメ · 青年"', '"若者・エンタメ · Jugend"'),
        ('"レベル B1 · 11月11日の分かち合い · 11月11日的分享"',
         '"レベル B1 · 11月11日の分かち合い · Teilen am 11. November"'),
        ('"渡す 递给 · つなぐ 连接 · 送り合う 互相发送。"',
         '"渡す überreichen · つなぐ verbinden · 送り合う einander schicken."'),
        ('"思い出 回忆 · 大きくなる 长大。"',
         '"思い出 eine Erinnerung · 大きくなる groß werden."'),
        ('"你呢？想把波奇递给谁？写两句日语寄来。"',
         '"Wem möchtest du Pocky überreichen? Schreibe zwei Sätze auf Japanisch und schicke sie ein."'),
        ('"練習 · 第 5 版练习"', '"練習 · Übungen Seite 5"'),
        ('"レベル B2 · 紅葉の見頃は南へ · 红叶最佳观赏期向南移动"',
         '"レベル B2 · 紅葉の見頃は南へ · Die Laubzeit zieht nach Süden"'),
        ('"目安 标准 · 色づき 变色 · 変化 变化 · 準備 准备。"',
         '"目安 ein Anhaltspunkt · 色づき Verfärbung · 変化 Veränderung · 準備 Vorbereitung."'),
        ('"グラフを読もう · 读图表"', '"グラフを読もう · Diagramm lesen"'),
        ('"練習用データ · 练习数据"', '"練習用データ · Übungsdaten"'),
        ('"練習 · 第 6 版练习"', '"練習 · Übungen Seite 6"'),
    ],
    "content7.py": [
        ('"ことば · 语言"', '"ことば · Sprache"'),
        ('"言語フォーカス · 三つのレベル、三つのテーマ · 三个级别，三个主题"',
         '"言語フォーカス · 三つのレベル、三つのテーマ · Drei Stufen, drei Themen"'),
        ('"読書週間 读书周 · 習慣 习惯 · 借りる 借。"',
         '"読書週間 Lesewoche · 習慣 eine Gewohnheit · 借りる ausleihen."'),
        ('"七五三 七五三 · 千歳飴 千岁糖 · 晴れ着 盛装"',
         '"七五三 Shichi-Go-San · 千歳飴 Chitose-ame · 晴れ着 Festkleidung"'),
        ('"〜連勝 连胜 · 〜% 百分之〜 · 〜組以上 组以上。"',
         '"〜連勝 Siege in Folge · 〜% Prozent · 〜組以上 Gruppen oder mehr."'),
        ('"まちがい診療所 · 易错诊所"', '"まちがい診療所 · Fehlerklinik"'),
        ('"有「昨日」时要用过去式。"', '"Mit 「昨日」 steht die Vergangenheit."'),
        ('"动词名词化时要加「こと」。"',
         '"Füge 「こと」 hinzu, um aus einem Verb ein Nomen zu machen."'),
        ('"得到东西的场所用「で」。"',
         '"Für den Ort des Erhaltens steht 「で」."'),
        ('"看的场所用「で」。"', '"Für den Ort des Sehens steht 「で」."'),
        ('"今週のフレーム · 本周句式"', '"今週のフレーム · Muster der Woche"'),
        ('"句式拆解：追赶最佳观赏期。"',
         '"Zerlegung: der besten Laubzeit hinterherjagen."'),
        ('"読者の手紙 · 读者园地"', '"読者の手紙 · Leserecke"'),
        ('ld = "※この手紙は編集部の例です。締め切りまでに、本当の読者の手紙と第8版の作文の優秀作は届きませんでした。VOL.4に載せます。"',
         'ld_de = "Beispiel der Redaktion, kein echter Brief. Bis zum Redaktionsschluss '
         'trafen keine echten Briefe und keine besten Aufsätze ein; beides '
         'erscheint in VOL.4. Schickt uns euren Brief auf Japanisch — '
         'ausgewählte Briefe werden in VOL.4 abgedruckt!"'),
        ('lcn = "编辑部示例信，非真实来信。截至截稿，未收到真实来信与第8版最佳作文；VOL.4将刊登收到的来信与佳作。"\n',
         ''),
        ('lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld, "serif", False, 20.5, CW - 44)) * 29 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26 + 16',
         'lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld_de, "sans", False, 20, CW - 44)) * 29 + 26 + 16'),
        ('yy3 = p.para(bx + 22, yy3 + 20, ld, 20.5, "serif", False, GREY, CW - 44, 1.42) + 10\n'
         'p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)',
         'p.para(bx + 22, yy3 + 20, ld_de, 20, "sans", False, GREY, CW - 44, 1.42)'),
        ('"今週のフレーズ · 本周金句（逐字摘自本期文章）"',
         '"今週のフレーズ · Sätze der Woche (wörtlich aus dieser Ausgabe)"'),
        ('"读书周在11月9日星期一结束。"', '"Die Lesewoche endet am Montag, dem 9. November."'),
        ('"11月15日星期日是七五三的中心日。"',
         '"Sonntag, der 15. November, ist der Höhepunkt von Shichi-Go-San."'),
        ('"波奇与百力滋之日始于1999年。"', '"Der Pocky-und-Pretz-Tag begann 1999."'),
        ('"千岁糖是寄托长寿愿望的糖果。"',
         '"Chitose-ame ist das Bonbon des Wunsches nach einem langen Leben."'),
        ('"七五三是3岁、5岁和7岁孩子的庆祝活动。"',
         '"Shichi-Go-San feiert Kinder im Alter von 3, 5 und 7 Jahren."'),
        ('"软银以四连胜夺得日本第一。"',
         '"SoftBank holte den Japan-Titel mit vier Siegen in Folge."'),
        ('"11月11日是波奇日。"', '"Der 11. November ist Pocky-Tag."'),
        ('"红叶的最佳观赏期从北向南移动。"',
         '"Die beste Laubzeit zieht von Norden nach Süden."'),
        ('"第1面"', '"S. 1"'),
        ('"第2面"', '"S. 2"'),
        ('"第3面"', '"S. 3"'),
        ('"第4面"', '"S. 4"'),
        ('"第5面"', '"S. 5"'),
        ('"第6面"', '"S. 6"'),
        ('"来週 · 下期预告 (VOL.4)"', '"来週 · Nächste Woche (VOL.4)"'),
    ],
    "content8.py": [
        ('af.para(f"— 第{pg}面 —", 13.3, "sans", True, OLIVE, lh=1.16, gap=2, split=False)', 'af.para(f"— 第{pg}面 —", 12.9, "sans", True, OLIVE, lh=1.13, gap=2, split=False)'),
        ('af.para(txt, 13.3, lh=1.16, gap=0.5, split=False)', 'af.para(txt, 12.9, lh=1.13, gap=0.5, split=False)'),
        ('"テストと答え · 练习与答案"', '"テストと答え · Test und Antworten"'),
        ('"七五三是11月15日。"', '"Shichi-Go-San ist der 15. November."'),
        ('"波奇日从1999年开始。"', '"Der Pocky-Tag begann 1999."'),
        ('"读书周从10月27日开始。→ ___"',
         '"Die Lesewoche beginnt am 27. Oktober. → ___"'),
        ('"去看红叶的人可以自北向南追赶最佳观赏期。→ ___"',
         '"Wer die Blätter sehen geht, kann der besten Zeit von Norden nach Süden hinterherjagen. → ___"'),
        ('f"写作题（无唯一答案）；范文（{NCHARS} 字）见下。"',
         'f"Schreibaufgabe (keine einzige richtige Antwort); der Mustertext ({NCHARS} Zeichen) steht unten."'),
        ('"（开放题，范文如下）"', '"(offene Aufgabe — Mustertext unten)"'),
        ('f"范文见本版 H 区（{NCHARS} 字）"',
         'f"Mustertext in Abschnitt H auf dieser Seite ({NCHARS} Zeichen)"'),
        ('"答え · 参考答案 — 按版面分页排列，找到题号即可"',
         '"答え · Antworten — nach Seiten geordnet; einfach die Nummer suchen"'),
        ('"每题附一句中文简析 · 带 ✓ 的为范文题"',
         '"Eine kurze deutsche Notiz zu jeder Antwort · ✓ = die Aufgabe mit dem Mustertext"'),
        ('f"— 第{pg}面 —"', 'f"— Seite {pg} —"'),
    ],
    "render.py": [
        ('"Lucerna-VOL3.pdf"', '"Lucerna-VOL3-DE.pdf"'),
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
