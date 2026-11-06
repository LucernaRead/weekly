# -*- coding: utf-8 -*-
"""JA core (VOL.2, Chinese explanations) -> JA x DE edition transform.

Re-runnable: reads the PRISTINE W45 JA core build, applies exact-literal
replacements (whole strings, never AST byte offsets, never byte slicing),
and writes the edition build into this directory. Fix rounds edit THIS
file, then re-run: transform.py -> run.py (one process) -> render.py.

Frozen: every Japanese article/stem/option/letter/figure string is copied
byte-identical. Only the explanation layer changes: Chinese notes/glosses/
headers/instructions -> German, per the W43 JA x DE shipped precedent
(files/weekly-report-ja-de). Masthead geometry follows the W43 JA x DE
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
    "files/weekly-report-w45-ja-de")
CANON_SVGLIB_MD5 = "d73e23b365676c3618d7e060b835eb4d"

# (old, new) applied in order. Longer strings first where one contains another.
GLOBAL = [
    # --- output repoint ---
    ("weekly-report-w45-ja-core", "weekly-report-w45-ja-de"),
    # --- registry type names / instructions (W43 JA x EN wording) ---
    ('instr="造句"', 'instr="Satz bilden"'),
    ('instr="翻译"', 'instr="Übersetzen"'),
    ('instr="写作"', 'instr="Schreiben"'),
    ('instr="判断"', 'instr="Richtig/Falsch"'),
    ('instr="填空"', 'instr="Ausfüllen"'),
    ('instr="把词和释义配对"', 'instr="Wörter zuordnen"'),
    ('instr="把活动和地点·时间配对"', 'instr="Ereignisse den Orten und Daten zuordnen"'),
    ('"完形单选"', '"Lückentext"'),
    ('"单选"', '"Multiple Choice"'),
    ('"完成句子"', '"Ausfüllen"'),
    ('"词汇配对"', '"Zuordnen"'),
    ('"造句"', '"Satzbau"'),
    ('"判断对错"', '"Richtig/Falsch"'),
    ('"翻译"', '"Übersetzen"'),
    ('"写作"', '"Schreiben"'),
    # --- shared furniture ---
    ('"あなたは？ · 说说你自己"', '"あなたは？ · Sie sind dran"'),
    ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
     '"Antworten auf Seite 8 · Stufen gemischt — nach Nummer suchen"'),
]

# Answer-note translations. One German rendering per distinct core note;
# duplicates share the rendering (correct: same note -> same meaning).
NOTES = [
    ("文化日在11月3日（周二）", "Der Kulturtag ist am 3. November (Dienstag)"),
    ("读书周到11月9日（周一）", "Die Lesewoche läuft bis zum 9. November (Montag)"),
    ("見頃＝最佳观赏期", "見頃 = beste Laubzeit"),
    ("立冬＝冬天的开始", "立冬 = der Winteranfang"),
    ("神户灯光秀从7日（周六）开始", "Die Beleuchtung in Kobe beginnt am 7. (Samstag)"),
    ("文化日全国都有文化活动", "Kulturtag: Kultur im ganzen Land"),
    ("立冬在11月7日（周六）", "立冬 ist am 7. November (Samstag)"),
    ("灯光秀在神户开始", "Die Beleuchtung beginnt in Kobe"),
    ("「ゆる」＝无理をしない", "「ゆる」 = sich nicht zwingen"),
    ("鍋の食卓は去年の1.5倍", "Nabe-Essen sind 1,5-mal so häufig wie letztes Jahr"),
    ("発表は10月21日", "Die Ankündigung war am 21. Oktober"),
    ("11月から1月まで気温は平年より高い",
     "November–Januar: wärmer als im Durchschnitt"),
    ("服と食事の話題はnoteのまとめによるもの",
     "Kleidung und Essen: aus der note-Rundschau"),
    ("ゆる＝轻松、不勉强", "ゆる = locker, ohne Zwang"),
    ("蒸し器＝蒸笼", "蒸し器 = ein Dampfgarer"),
    ("整える＝调理、调养", "整える = in Ordnung bringen"),
    ("鍋＝一锅菜", "鍋 = ein Eintopf"),
    ("鍋の材料が1か月早く並んだ", "Nabe-Zutaten kamen einen Monat früher"),
    ("気象庁の予報は10月20日", "Die JMA-Prognose war am 20. Oktober"),
    ("サクサクdeコパンが1,300万食を超えた",
     "サクサクdeコパン überschritt 13 Millionen Portionen"),
    ("ゆる＝轻松 b", "ゆる = locker b"),
    ("蒸し器＝蒸笼 a", "蒸し器 = Dampfgarer a"),
    ("麻辣湯＝辛いスープ d", "麻辣湯 = scharfes Suppengericht d"),
    ("予報＝天気の予想 c", "予報 = Wettervorhersage c"),
    ("杉并的活动是家庭管弦乐队", "Die Veranstaltung in Suginami ist ein Familienorchester"),
    ("传统工艺展在石川县立美术馆",
     "Kunsthandwerksausstellung im Ishikawa-Kunstmuseum"),
    ("传统工艺展到11月8日", "Die Ausstellung läuft bis zum 8. November"),
    ("灯光秀在金泽城和兼六园", "Beleuchtung: Burg Kanazawa und Kenrokuen"),
    ("市場＝集市", "市場 = Markt"),
    ("工芸＝工艺", "工芸 = Kunsthandwerk"),
    ("陶器＝陶瓷", "陶器 = Keramik"),
    ("工艺展到11月8日（周日）", "Die Ausstellung läuft bis zum 8. November (Sonntag)"),    ("金箔＝金箔", "金箔 = Blattgold"),
    ("主语＋时间", "Subjekt + Zeit"),
    ("地点＋で＋あります", "Ort + で + あります"),
    ("见たい＝想看", "見たい = sehen wollen"),
    ("和家人一起", "zusammen mit der Familie"),
    ("文化の日＝11月3日 b", "文化の日 = 3. November b"),
    ("工芸展＝美術館 c", "工芸展 = Museum c"),
    ("オーケストラ＝杉並 d", "オーケストラ = Suginami d"),
    ("ライトアップ＝金沢城 a", "ライトアップ = Burg Kanazawa a"),
    ("第1战软银3-1胜DeNA", "Spiel 1: SoftBank schlug DeNA 3:1"),
    ("第2战逆转的是筒香的3分本垒打", "Tsutsugos 3-Punkte-Homerun wendete Spiel 2"),
    ("2连胜开局的是软银", "SoftBank startete mit zwei Siegen in Folge"),
    ("2连胜开局的夺冠率是73%", "Teams mit 2:0-Start gewinnen in 73 % der Fälle den Titel"),
    ("2024年夺冠的是DeNA", "DeNA gewann 2024 den Titel"),
    ("第1战软银得3分", "SoftBank erzielte 3 Punkte in Spiel 1"),
    ("第2战软银得4分", "SoftBank erzielte 4 Punkte in Spiel 2"),
    ("第1战打到延长11局", "Spiel 1 ging über 11 Innings"),
    ("第2战打到延长10局", "Spiel 2 ging über 10 Innings"),
    ("夺冠率73%", "Titelquote 73 %"),
    ("延長＝比赛延长", "延長 = Verlängerung"),
    ("第1战观众33,388人", "Spiel 1: 33.388 Zuschauer"),
    ("第2战观众33,432人", "Spiel 2: 33.432 Zuschauer"),
    ("相川监督说「4场胜负之战」", "Trainer Aikawa sprach vom Kampf um vier Siege"),
    ("第1戦は土よう日です", "Spiel 1 war an einem Samstag"),
    ("ソフトバンクが2連勝しました", "SoftBank gewann zweimal in Folge"),
    ("第2戦も延長戦でした", "Auch Spiel 2 ging in die Verlängerung"),
    ("2024年はDeNAが優勝しました", "DeNA gewann 2024"),
    ("万圣节在10月31日（周六）", "Halloween war am 31. Oktober (Samstag)"),
    ("涩谷禁酒时间是18时到5时", "Shibuya: Alkoholverbot 18:00–05:00 Uhr"),
    ("乱扔垃圾罚款2,000日元", "Weggeworfener Müll kostet 2.000 Yen Strafe"),
    ("化妆活动在池袋", "Das Cosplay-Festival ist in Ikebukuro"),
    ("工艺展到11月8日（周日）", "Die Ausstellung läuft bis zum 8. November (Sonntag)"),
    ("横滨中区民祭在11月8日（周日）", "Bürgerfest Naka, Yokohama, 8. November (Sonntag)"),
    ("万圣节在10月31日", "Halloween war am 31. Oktober"),
    ("禁酒从18时开始", "Das Verbot beginnt um 18:00 Uhr"),
    ("禁酒到早上5时", "Das Verbot läuft bis 05:00 Uhr"),
    ("横滨祭典在11月8日", "Das Yokohama-Festival ist am 8. November"),
    ("夜里路上不能喝酒", "Nachts kein Trinken auf der Straße"),
    ("ゴミの罰金は今年6月からです", "Die Müllstrafe gilt seit Juni dieses Jahres"),
    ("コスプレフェスは池袋です", "Das Cosplay-Festival ist in Ikebukuro"),
    ("ハロウィンは10月31日（土）", "Halloween war am 31. Oktober (Samstag)"),
    ("飲むことができません＝不能喝", "飲むことができません = nicht trinken können"),
    ("守って、〜しましょう", "守って + 〜しましょう = Regeln einhalten, los!"),
    ("フェンスの中＝围栏里面", "フェンスの中 = innerhalb des Zauns"),
    ("活动从10月30日到11月1日", "Das Festival lief vom 30. Oktober bis 1. November"),
    ("11月から1月まで気温は平年より高い",
     "November–Januar: wärmer als im Durchschnitt"),
    ("雨が多いのは太平洋側", "Auf der Pazifikseite regnet es mehr"),
    ("九州の旅の検索は去年のほぼ2倍",
     "Kyushu-Reisen: Suche fast verdoppelt"),
    ("1回の旅の予算は下がった", "Das Budget pro Reise sank"),
    ("鳴子峡の見頃は10月31日から11月8日の週末",
     "Naruko-Schlucht: Höhepunkt 31. Oktober bis 8. November"),
    ("图中最受欢迎的是近处的满足感", "Grafik-Top: Zufriedenheit in der Nähe"),
    ("近场满足感38%", "Zufriedenheit in der Nähe: 38 %"),
    ("温泉27%", "Heiße Quellen: 27 %"),
    ("红叶21%与美食14%之差为7", "Laub 21 % minus Essen 14 % ist 7"),
    ("38+27=65", "38 + 27 = 65"),
    ("四项合计100%", "Alle vier ergeben zusammen 100 %"),
    ("立冬在11月7日", "立冬 ist am 7. November"),
    ("神户灯光秀到12月28日", "Die Beleuchtung in Kobe läuft bis zum 28. Dezember"),
    ("九州旅行搜索约为去年的2倍",
     "Die Suche nach Kyushu-Reisen hat sich fast verdoppelt"),
    ("气象厅预报在10月20日", "Die JMA-Prognose war am 20. Oktober"),
    ("11月は平年より暖かい予報です", "November: wärmer als im Durchschnitt"),
    ("九州の旅の検索は増えました", "Die Suche nach Kyushu-Reisen stieg"),
    ("グラフは練習用データです", "Die Grafik zeigt Übungsdaten"),
    ("读书周从10月27日（周二）开始", "Die Lesewoche begann am 27. Oktober (Dienstag)"),
    ("读书周到11月9日", "Die Lesewoche läuft bis zum 9. November"),
    ("口号是「静かだけど、冒険中。」", "Der Slogan lautet 「静かだけど、冒険中。」"),
    ("图书馆活动有图书介绍", "Bibliothek: Bücher werden vorgestellt"),
    ("見頃＝红叶最美的时候", "見頃 = wenn das Laub am schönsten ist"),
    ("紅葉狩り＝去看红叶", "紅葉狩り = losziehen, um das Laub zu sehen"),
    ("ライトアップ＝夜里用灯光照亮", "ライトアップ = nachts anstrahlen"),
    ("落葉＝落叶", "落葉 = gefallenes Laub"),
    ("1.5倍＝比去年多50%", "1.5倍 = 50 % mehr als letztes Jahr"),
    ("73%≈4人中的3人", "73 % ≈ 3 von 4"),
    ("サクサクdeコパンが1,300万食", "サクサクdeコパン erreichte 13 Millionen Portionen"),
    ("日本大赛第1战在10月24日（周六）", "Spiel 1 der Japan Series war am 24. Oktober (Samstag)"),
    ("第2战软银4-3获胜", "Spiel 2: SoftBank gewann 4:3"),
    ("神户灯光秀从7日开始", "Die Beleuchtung in Kobe beginnt am 7."),
    ("2连胜开局的夺冠率73%", "Titelquote bei 2:0-Start: 73 %"),
    ("气象厅预报气温高于往年", "Die JMA-Prognose: wärmer als im Durchschnitt"),
    ("九州旅行搜索约为去年的2倍",
     "Die Suche nach Kyushu-Reisen hat sich fast verdoppelt"),
    ("美香周二和家人去金泽", "Am Dienstag fährt Mika mit ihrer Familie nach Kanazawa"),
    ("在金泽看传统工艺展和灯光秀",
     "In Kanazawa: Ausstellung und Beleuchtung"),
    ("周六和朋友去神户", "Am Samstag fährt sie mit Freunden nach Kobe"),
    ("读书周想借2本书", "Für die Lesewoche will sie 2 Bücher ausleihen"),
    ("主语＋时间＋地点＋动词", "Subjekt + Zeit + Ort + Verb"),
    ("场所用「で」", "「で」 für den Ort"),
    ("2连胜开局", "zwei Siege in Folge"),
    ("見頃＝最佳观赏期 b", "見頃 = beste Laubzeit b"),
    ("鍋＝一锅菜 d", "鍋 = Eintopf d"),
    ("落葉＝落叶 a", "落葉 = gefallenes Laub a"),
    ("予算＝预算 c", "予算 = Budget c"),
    ("見せてください＝请出示", "見せてください = bitte zeigen"),
    ("借りられます＝能借（可能形）", "借りられます = ausleihen können (Potentialform)"),
    ("读书周到11月9日（第7版）", "Die Lesewoche läuft bis zum 9. November (Seite 7)"),
    ("「紅葉の本」受欢迎", "「紅葉の本」 ist beliebt"),
    ("どういたしまして＝不客气", "どういたしまして = gern geschehen"),
    ("对照第3版", "Siehe Seite 3"),
    ("对照第5版", "Siehe Seite 5"),
    ("对照第7版", "Siehe Seite 7"),
    ("对照第6版（神户的灯光秀）", "Siehe Seite 6 (Kobe-Beleuchtung)"),
]

# Per-file furniture / gloss / structural replacements.
PER_FILE = {
    "bslib4.py": [
        ('("译注｜" + s,', '("Anm. — " + s,'),
        ('"Lucerna · 日语周报 VOL.2 · LUCERNA JAPANESE WEEKLY"',
         '"Lucerna · JAPANISCHE WOCHENZEITUNG VOL.2 · TEXT AUF JAPANISCH · ERKLÄRUNGEN AUF DEUTSCH"'),
        ('f"第 {n} 版 / 共 {total} 版"', 'f"Seite {n} von {total}"'),
    ],
    "content12.py": [
        # P1 masthead -> W43 JA x EN shipped geometry
        ('p.text(975, 262, "Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")',
         'p.text(975, 248, "Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")'),
        ('p.text(975, 330, "日本語版 · VOL.2 · 文化の日 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")',
         'p.text(975, 316, "日本語版 · VOL.2 · 文化の日 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")\n'
         'p.text(975, 356, "JAPANISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER", 19, "sans", True, BRICK, anchor="middle")'),
        ('p.text(975, 372, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")',
         'p.text(975, 390, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")'),
        ('p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)',
         'p.hline(MX, RIGHT, 406, INK, 3); p.hline(MX, RIGHT, 413, INK, 1.2)'),
        ('"毎週、日本語で · 每周一期 · 日本人が読んでいる日本語を読む"',
         '"毎週、日本語で · Jede Woche neu · 日本人が読んでいる日本語を読む"'),
        ('"周二是文化日"', '"Dienstag ist Kulturtag"'),
        ('"节日过后，红叶周末到来 · 详见第 3 版"',
         '"Nach dem Feiertag kommt das Herbstlaub-Wochenende · Siehe Seite 3"'),
        ('"トップニュース · 头条"', '"トップニュース · Topmeldung"'),
        ('"祝日 节假日 · 見頃 最佳观赏期 · 暦 历法 · お届けします 为您送上。"',
         '"祝日 Feiertag · 見頃 beste Laubzeit · 暦 Kalender · お届けします für Sie bringen."'),
        ('"数字で見る今週 · 数字看本周"', '"数字で見る今週 · Woche in Zahlen"'),
        ('"今すぐ練習 · 即学即练"', '"今すぐ練習 · Jetzt üben"'),
        ('"这四个话题，都是本期报纸的主题。"',
         '"Das sind die vier Themen dieser Ausgabe."'),
        ('"来源与日期见各篇文章，非精确统计"',
         '"Quellen und Daten: Artikel, keine Statistik"'),
        ('"この号の内容 · 本期目录"', '"この号の内容 · In dieser Ausgabe"'),
        ('"今週のことば · 本周单词"', '"今週のことば · Wort der Woche"'),
        ('"ゆる＝ 轻松、不勉强。"', '"ゆる = locker, ohne Zwang."'),
        ('"短いニュース · 快讯"', '"短いニュース · Kurznachrichten"'),
        ('"クイズ · 闪电问答"', '"クイズ · Kurzquiz"'),
        ('"读头版，选出正确答案 · 答案见第 8 版"',
         '"Titelseite lesen und wählen · Antworten Seite 8"'),
        # P2
        ('"レベル A2 · ゆる整え食と暖かい11月 · 轻松食养与暖和的11月"',
         '"レベル A2 · ゆる整え食と暖かい11月 · Sanftes Essen und ein warmer November"'),
        ('"蒸す 蒸 · 並ぶ 摆上货架 · 食卓 餐桌 · 超える 超过。"',
         '"蒸す dämpfen · 並ぶ in die Läden kommen · 食卓 Esstisch · 超える übersteigen."'),
        ('"予報 预报 · 平年 往年平均 · 季節風 季风 · 話題 话题 · 値上がり 涨价。"',
         '"予報 Prognose · 平年 Durchschnittsjahr · 季節風 saisonaler Wind · 話題 Thema · 値上がり Preisanstieg."'),
        ('"你呢？寒冷的日子想吃什么锅？写两句日语寄来。"',
         '"Und Sie? Welchen Nabe möchten Sie an einem kalten Tag essen? Schreiben Sie zwei Sätze auf Japanisch und schicken Sie sie ein!"'),
        ('"季節のことば · 季节词语"', '"季節のことば · Wörter der Jahreszeit"'),
        ('"ゆる整え食の4つの言葉 · 关于轻松食养的四个词"',
         '"ゆる整え食の4つの言葉 · Vier Wörter für sanftes Essen"'),
        ('"一锅菜"', '"ein Eintopf"'),
        ('"蒸笼"', '"ein Dampfgarer"'),
        ('"轻松、不勉强"', '"locker, ohne Zwang"'),
        ('"调理、调养"', '"Körper und Geist in Ordnung bringen"'),
        ('"練習 · 第 2 版练习"', '"練習 · Übungen Seite 2"'),
    ],
    "content34.py": [
        ('"レベル A2→B1 · 文化の日と金沢 · 文化日与金泽"',
         '"レベル A2→B1 · 文化の日と金沢 · Kulturtag und Kanazawa"'),
        ('"市場 市场 · 工芸 工艺 · 光 灯光 · 楽しむ 享受。"',
         '"市場 Markt · 工芸 Kunsthandwerk · 光 Licht · 楽しむ genießen."'),
        ('"陶器 陶瓷 · 漆器 漆器 · 染物 染色织物 · 金箔 金箔。"',
         '"陶器 Keramik · 漆器 Lackwaren · 染物 gefärbte Textilien · 金箔 Blattgold."'),
        ('"你呢？文化日想去参加什么文化活动？写两句日语寄来。"',
         '"Und Sie? Zu welcher Kulturveranstaltung möchten Sie am Kulturtag gehen? Schreiben Sie zwei Sätze auf Japanisch und schicken Sie sie ein!"'),
        ('"練習 · 第 3 版练习"', '"練習 · Übungen Seite 3"'),
        ('"レベル B1 · 日本シリーズ横浜の2試合 · 日本大赛横滨两场"',
         '"レベル B1 · 日本シリーズ横浜の2試合 · Die Japan Series: zwei Spiele in Yokohama"'),
        ('"延長 延长赛 · 逆転 逆转 · 同点 平分 · 優勝率 夺冠率。"',
         '"延長 Verlängerung · 逆転 Aufholjagd · 同点 Gleichstand · 優勝率 Titelquote."'),
        ('"総括 总结 · 締め切り 截稿 · 確認する 核实。"',
         '"総括 Rückblick · 締め切り Redaktionsschluss · 確認する bestätigen."'),
        ('"日本シリーズの日程 · 大赛日程"', '"日本シリーズの日程 · Spielplan"'),
        ('"横浜の2試合の記録 · 横滨两场比赛的记录"',
         '"横浜の2試合の記録 · Die zwei Yokohama-Spiele im Überblick"'),
        ('"練習 · 第 4 版练习"', '"練習 · Übungen Seite 4"'),
    ],
    "content56.py": [
        ('"若者・エンタメ · 青年"', '"若者・エンタメ · Jugend"'),
        ('"レベル B1 · ハロウィンと秋まつり · 万圣节与秋日祭典"',
         '"レベル B1 · ハロウィンと秋まつり · Halloween und Herbstfeste"'),
        ('"罰金 罚款 · 像 雕像 · 仮装 变装 · 守る 遵守。"',
         '"罰金 Geldstrafe · 像 Statue · 仮装 Verkleidung · 守る einhalten."'),
        ('"祭り 节日 · 週末 周末 · 話題 话题。"',
         '"祭り Fest · 週末 Wochenende · 話題 Thema."'),
        ('"你呢？秋日祭典上想做什么？写两句日语寄来。"',
         '"Und Sie? Was möchten Sie auf einem Herbstfest tun? Schreiben Sie zwei Sätze auf Japanisch und schicken Sie sie ein!"'),
        ('"練習 · 第 5 版练习"', '"練習 · Übungen Seite 5"'),
        ('"レベル B2 · 暖かい11月と秋の旅 · 暖和的11月与秋日旅行"',
         '"レベル B2 · 暖かい11月と秋の旅 · Ein warmer November und Herbstreisen"'),
        ('"予算 预算 · 満足 满足 · 観測 观测 · 追いかける 追赶。"',
         '"予算 Budget · 満足 Zufriedenheit · 観測 Beobachtung · 追いかける verfolgen."'),
        ('"グラフを読もう · 读图表"', '"グラフを読もう · Diagramm lesen"'),
        ('"練習用データ · 练习数据"', '"練習用データ · Übungsdaten"'),
        ('"練習 · 第 6 版练习"', '"練習 · Übungen Seite 6"'),
    ],
    "content7.py": [
        ('"ことば · 语言"', '"ことば · Sprache"'),
        ('"言語フォーカス · 三つのレベル、三つのテーマ · 三个级别，三个主题"',
         '"言語フォーカス · 三つのレベル、三つのテーマ · Drei Stufen, drei Themen"'),
        ('"読書週間 读书周 · 紹介 介绍 · 読み聞かせ 朗读。"',
         '"読書週間 Lesewoche · 紹介 Vorstellung · 読み聞かせ Vorlesen."'),
        ('"見頃 最佳观赏期 · 紅葉狩り 看红叶出游 · 落葉 落叶"',
         '"見頃 beste Laubzeit · 紅葉狩り Laubschau · 落葉 gefallenes Laub"'),
        ('"〜倍 倍 · 〜% 百分之〜 · 〜万食 万份。"',
         '"〜倍 -mal · 〜% Prozent · 〜万食 zehntausend Portionen."'),
        ('"まちがい診療所 · 易错诊所"', '"まちがい診療所 · Fehlerklinik"'),
        ('"有「昨日」时要用过去式。"', '"Mit 「昨日」 gilt die Vergangenheit."'),
        ('"动词名词化时要加「こと」。"',
         '"Mit 「こと」 wird das Verb zum Nomen."'),
        ('"地点用「か所」来数。"', '"Orte zählt man mit 「か所」."'),
        ('"动作发生的场所用「で」。"',
         '"Für den Ort einer Handlung steht 「で」."'),
        ('"今週のフレーム · 本周句式"', '"今週のフレーム · Muster der Woche"'),
        ('"句式拆解：轻松地调理身心。"',
         '"Zerlegung: Körper und Geist sanft in Ordnung bringen."'),
        ('"読者の手紙 · 读者园地"', '"読者の手紙 · Leserecke"'),
        # Readers' corner: coordinator ruling — the Japanese disclosure line
        # (ld) must NOT serve as the operative disclosure for German
        # readers, and the Chinese disclosure (lcn) is the core's
        # reader-native layer. Both are replaced by ONE German
        # disclosure stating the 3 facts + an explicit invitation.
        ('ld = "※この手紙は編集部の例です。締め切りまでに、本当の読者の手紙と第8版の作文の優秀作は届きませんでした。VOL.3に載せます。"',
         'ld_de = "Beispielbrief, kein echter Brief. Bis zum Redaktionsschluss '
         'keine echten Briefe und keine besten Seite-8-Aufsätze; beides '
         'erscheint in VOL.3. Schickt uns eure Briefe auf Japanisch — '
         'ausgewählte Briefe erscheinen in VOL.3!"'),
        ('lcn = "编辑部示例信，非真实来信。截至截稿，未收到真实来信与第8版最佳作文；VOL.3将刊登收到的来信与佳作。"\n',
         ''),
        ('lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld, "serif", False, 20.5, CW - 44)) * 29 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26 + 16',
         'lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld_de, "sans", False, 20, CW - 44)) * 29 + 26 + 16'),
        ('yy3 = p.para(bx + 22, yy3 + 20, ld, 20.5, "serif", False, GREY, CW - 44, 1.42) + 10\n'
         'p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)',
         'p.para(bx + 22, yy3 + 20, ld_de, 20, "sans", False, GREY, CW - 44, 1.42)'),
        ('"今週のフレーズ · 本周金句（逐字摘自本期文章）"',
         '"今週のフレーズ · Sätze der Woche (wörtlich aus dieser Ausgabe)"'),
        ('"文化日是11月3日星期二。"', '"Der Kulturtag ist Dienstag, der 3. November."'),
        ('"这是一个慢慢地、轻松调理的日本11月。"',
         '"Es ist ein langsamer, sanft geordneter japanischer November."'),
        ('"所谓ゆる，就是不勉强、慢慢来的意思。"',
         '"ゆる heißt: sich nicht zwingen, es langsam angehen."'),
        ('"火锅食材提前一个月上架了。"',
         '"Nabe-Zutaten kamen einen Monat früher in die Läden."'),
        ('"可以同时欣赏传统工艺、红叶与灯光。"',
         '"Man kann traditionelles Handwerk, Herbstlaub und Lichter gemeinsam genießen."'),
        ('"软银以两连胜开局。"', '"SoftBank startete mit zwei Siegen in Folge."'),
        ('"遵守规则，过一个快乐的万圣节吧。"',
         '"Haltet euch an die Regeln und habt ein fröhliches Halloween!"'),
        ('"去看红叶的人可以自北向南追赶最佳观赏期。"',
         '"Wer das Laub sehen will, kann der besten Zeit von Norden nach Süden folgen."'),
        ('"第1面"', '"S.1"'),
        ('"第2面"', '"S.2"'),
        ('"第3面"', '"S.3"'),
        ('"第4面"', '"S.4"'),
        ('"第5面"', '"S.5"'),
        ('"第6面"', '"S.6"'),
        ('"来週 · 下期预告 (VOL.3)"', '"来週 · Nächste Woche (VOL.3)"'),
    ],
    "content8.py": [
        ('"テストと答え · 练习与答案"', '"テストと答え · Test und Antworten"'),
        # E zone re-aim JA<->ZH -> JA<->DE (W43 JA x DE pattern)
        ('"文化日是11月3日。"', '"Der Kulturtag ist am 3. November."'),
        ('"乱扔垃圾，要罚2,000日元。"', '"Wer Müll wegwirft, zahlt 2.000 Yen Strafe."'),
        ('"读书周从10月27日开始。→ ___"', '"Die Lesewoche beginnt am 27. Oktober. → ___"'),
        ('"我想去神户看红叶灯光秀。→ ___"',
         '"Ich möchte in Kobe die Herbstlaub-Beleuchtung sehen. → ___"'),
        ('f"写作题（无唯一答案）；范文（{NCHARS} 字）见下。"',
         'f"Schreibaufgabe (keine einzige richtige Antwort); der Mustertext ({NCHARS} Zeichen) steht unten."'),
        ('"（开放题，范文如下）"', '"(offene Aufgabe — Mustertext unten)"'),
        ('f"范文见本版 H 区（{NCHARS} 字）"',
         'f"Mustertext in Abschnitt H auf dieser Seite ({NCHARS} Zeichen)"'),
        ('"答え · 参考答案 — 按版面分页排列，找到题号即可"',
         '"答え · Antworten — nach Seiten geordnet; einfach die Nummer suchen"'),
        ('"每题附一句中文简析 · 带 ✓ 的为范文题"',
         '"Kurze deutsche Notiz bei jeder Antwort · ✓ = Mustertext-Aufgabe"'),
        ('f"— 第{pg}面 —"', 'f"— Seite {pg} —"'),
    ],
    "render.py": [
        ('"Lucerna-VOL2.pdf"', '"Lucerna-VOL2-DE.pdf"'),
        ('"Lucerna-VOL2-web.pdf"', '"Lucerna-VOL2-DE-web.pdf"'),
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
