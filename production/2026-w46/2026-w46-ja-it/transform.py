# -*- coding: utf-8 -*-
"""JA core (VOL.3, Chinese explanations) -> JA x IT edition transform.

Re-runnable: reads the PRISTINE W46 JA core build, applies exact-literal
replacements (whole strings, never AST byte offsets), and writes the
edition build into this directory. Fix rounds edit THIS file, then
re-run: transform.py -> run.py (one process) -> render.py.

Frozen: every Japanese article/stem/option/letter/figure string is copied
byte-identical. Only the explanation layer changes: Chinese notes/glosses/
headers/instructions -> Italian, per the W45 JA x IT shipped precedent.
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
    "files/weekly-report-w46-ja-it")
CANON_SVGLIB_MD5 = "74177544422fe677639d769cd80499fb"

GLOBAL = [
    ("weekly-report-w46-ja-core", "weekly-report-w46-ja-it"),
    ('instr="造句"', 'instr="Costruisci una frase"'),
    ('instr="翻译"', 'instr="Traduci"'),
    ('instr="写作"', 'instr="Scrittura"'),
    ('instr="判断"', 'instr="Vero o falso?"'),
    ('instr="填空"', 'instr="Completa"'),
    ('instr="把词和释义配对"', 'instr="Abbina parola e senso"'),
    ('"完形单选"', '"completamento"'),
    ('"单选"', '"scelta multipla"'),
    ('"完成句子"', '"da completare"'),
    ('"词汇配对"', '"abbinamento"'),
    ('"造句"', '"costruzione di frasi"'),
    ('"判断对错"', '"vero/falso"'),
    ('"翻译"', '"traduzione"'),
    ('"写作"', '"scrittura"'),
    ('"あなたは？ · 说说你自己"', '"あなたは？ · Tocca a te"'),
    ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
     '"Risposte a pagina 8 · Livelli mescolati: trova il tuo numero"'),
]

NOTES = [
    ("1111中有4个1", "1111 ha quattro 1"),
    ("1111看起来像4根细棒", "1111 sembra quattro bastoncini sottili"),
    ("11月中旬以后进入见赏期的地点多比往年稍晚", "I luoghi che culminano dopo metà novembre sono per lo più in ritardo"),
    ("2026年没有三の酉", "Nel 2026 non c\'è San-no-tori"),
    ("3%≈100人中的3人", "3 % è circa 3 su 100"),
    ("34+26=60", "34 + 26 = 60"),
    ("4连胜夺冠", "Quattro vittorie di fila hanno portato il titolo"),
    ("4连胜＝4场比赛全胜", "vincere tutte e quattro le partite"),
    ("71%的家庭接受祈祷", "Il 71 % delle famiglie riceve una preghiera"),
    ("74%的家庭在照相馆拍照", "Il 74 % delle famiglie fa foto in studio"),
    ("Weathernews的预报在10月29日（周四）", "La previsione Weathernews era del 29 ottobre (giovedì)"),
    ("「千歳飴」受欢迎", "千歳飴 è popolare"),
    ("お参りします＝去参拜", "お参りします = andare a pregare"),
    ("お参り＝去神社参拜", "お参り = andare a pregare al santuario"),
    ("どういたしまして＝不客气", "どういたしまして = prego"),
    ("七五三是3岁5岁7岁孩子的庆祝活动", "Shichi-Go-San celebra i bambini di 3, 5 e 7 anni"),
    ("七五三是3岁、5岁、7岁孩子的庆祝活动", "Shichi-Go-San celebra i bambini di 3, 5 e 7 anni"),
    ("七五三的中心日在11月15日附近", "Shichi-Go-San si concentra intorno al 15 novembre"),
    ("七五三的中心日是11月15日（周日）", "Shichi-Go-San si concentra il 15 novembre (domenica)"),
    ("七五三的中心日是11月15日（第3版）", "Shichi-Go-San si concentra il 15 novembre (pagina 3)"),
    ("七五三的孩子去神社参拜", "I bambini di Shichi-Go-San vanno a pregare al santuario"),
    ("七五三的照片是全家的回忆", "Le foto di Shichi-Go-San sono un ricordo di famiglia"),
    ("七五三＝孩子的庆祝活动", "七五三 = una festa per bambini"),
    ("七五三＝3岁5岁7岁孩子的庆祝 b", "七五三 = una festa per bambini di 3, 5 e 7 anni b"),
    ("东京的红叶在11月29日（周日）前后", "Le foglie di Tokyo culminano intorno al 29 novembre (domenica)"),
    ("主语＋时间＋宾语＋动词", "soggetto + tempo + oggetto + verbo"),
    ("主语＋说明", "soggetto + descrizione"),
    ("九州场所在福冈国际中心举行", "Il torneo di Kyushu si tiene al Fukuoka Kokusai Center"),
    ("二の酉在11月19日（周四）", "Ni-no-tori è il 19 novembre (giovedì)"),
    ("分ける＝分享", "分ける = condividere"),
    ("前3场比赛连续打延长赛", "Le prime tre partite sono andate tutte agli inning supplementari"),
    ("前3场都是延长赛", "Le prime tre partite sono andate tutte agli inning supplementari"),
    ("千岁糖寄托长寿的愿望", "Chitose-ame porta un augurio di lunga vita"),
    ("千岁糖是红白相间的长糖", "Chitose-ame è una lunga caramella rossa e bianca"),
    ("千岁糖＝红白长糖", "lunga caramella rossa e bianca"),
    ("千歳飴＝红白长糖 a", "千歳飴 = lunga caramella rossa e bianca a"),
    ("千歳飴＝红白长糖 d", "千歳飴 = lunga caramella rossa e bianca d"),
    ("口号是「静かだけど、冒険中。」", "Lo slogan è 「静かだけど、冒険中。」"),
    ("周一读图书馆借的书", "Il lunedì legge un libro della biblioteca"),
    ("周三和朋友分享波奇", "Il mercoledì condivide i Pocky con gli amici"),
    ("周五去高尾山看红叶", "Il venerdì va sul monte Takao per le foglie"),
    ("周日和妹妹的七五三去神社", "La domenica va al santuario per lo Shichi-Go-San della sorella"),
    ("四项合计100%", "I quattro insieme fanno 100 %"),
    ("图表中最受欢迎的是山", "La montagna è in cima al grafico"),
    ("图表是真实调查结果", "Il grafico mostra veri risultati di un\'indagine"),
    ("在酉の市买熊手", "Comprare un kumade a Tori-no-ichi"),
    ("地点＋へ＋动词", "luogo + へ + verbo"),
    ("场所用「で」", "Usa 「で」 per il luogo"),
    ("大阪的红叶在12月4日（周五）前后", "Le foglie di Osaka culminano intorno al 4 dicembre (venerdì)"),
    ("宫岛的红叶从11月21日（周六）前后进入见赏期", "Le foglie di Miyajima culminano dal 21 novembre (sabato) circa"),
    ("宾语＋动词", "oggetto + verbo"),
    ("对照第2版", "Vedi pagina 2"),
    ("对照第3版", "Vedi pagina 3"),
    ("对照第6版（追赶见赏期）", "Vedi pagina 6 (a caccia della stagione migliore)"),
    ("对照第7版", "Vedi pagina 7"),
    ("山34%与神社26%之差为8", "Montagna 34 % meno santuari 26 % fa 8"),
    ("山占34%", "Montagna: 34 %"),
    ("岚山的红叶从11月23日（周一）前后进入见赏期", "Le foglie di Arashiyama culminano dal 23 novembre (lunedì) circa"),
    ("平成11年11月11日有6个1", "L\'11 novembre di Heisei 11 aveva sei 1"),
    ("思い出＝回忆", "思い出 = un ricordo"),
    ("接戦＝比分接近的比赛", "接戦 = una partita combattuta"),
    ("撮ります＝拍照", "撮ります = scattare una foto"),
    ("新小结是美ノ海", "Il nuovo komusubi è Umi-no-umi"),
    ("日本大赛第3战在10月27日（周二）", "La gara 3 delle Japan Series è stata il 27 ottobre (martedì)"),
    ("晴れ着＝庆祝日穿的衣服", "晴れ着 = abiti da festa"),
    ("波奇日从1999年开始", "Il giorno dei Pocky è iniziato nel 1999"),
    ("波奇日只买不分享是错的", "Il giorno dei Pocky non è solo comprare"),
    ("波奇日在11月11日", "Il giorno dei Pocky è l\'11 novembre"),
    ("波奇日在11月11日（周三）", "Il giorno dei Pocky è l\'11 novembre (mercoledì)"),
    ("波奇日定在11月11日因为细长的零食像数字1", "L\'11 novembre è stato scelto perché gli snack sottili assomigliano al numero 1"),
    ("波奇日是11月11日", "Il giorno dei Pocky è l\'11 novembre"),
    ("波奇日要和朋友分享零食", "Il giorno dei Pocky significa condividere snack con gli amici"),
    ("波奇＝巧克力细饼干", "bastoncino al cioccolato"),
    ("ポッキー＝巧克力细饼干 d", "ポッキー = bastoncino al cioccolato d"),
    ("渡す＝递给", "渡す = porgere"),
    ("照片长大后家人还会一起看", "La famiglia guarda ancora le foto quando i bambini sono grandi"),
    ("照相馆拍照的家庭是71%", "Famiglie che usano uno studio: 71 %"),
    ("熊手＝祈求生意兴隆的竹耙", "熊手 = rastrello fortunato per gli affari"),
    ("熊手＝竹耙吉祥物 b", "熊手 = rastrello fortunato b"),
    ("熊手＝竹耙吉祥物 c", "熊手 = rastrello fortunato c"),
    ("男孩在3岁和5岁庆祝，女孩在3岁和7岁", "I maschi festeggiano a 3 e 5 anni, le femmine a 3 e 7"),
    ("相扑场所到11月22日（周日）", "Il torneo di sumo dura fino al 22 novembre (domenica)"),
    ("神社占26%", "Santuari: 26 %"),
    ("第3战在横滨举行", "La gara 3 si è giocata a Yokohama"),
    ("第3战打到延长10局", "La gara 3 è arrivata al 10º inning"),
    ("第3战的再见本垒打是正木打出的", "Masaki ha battuto il fuoricampo decisivo della gara 3"),
    ("第3战软银2-1获胜", "Gara 3: SoftBank ha vinto 2-1"),
    ("第3战软银得2分", "SoftBank ha segnato 2 punti in gara 3"),
    ("第4战软银4-2获胜", "Gara 4: SoftBank ha vinto 4-2"),
    ("第4战软银得4分", "SoftBank ha segnato 4 punti in gara 4"),
    ("第5到第7战没有举行", "Le gare 5-7 non si sono giocate"),
    ("第5战也举行了", "Anche la gara 5 si è giocata"),
    ("系列赛MVP是正木智也", "L\'MVP della serie è Masaki Tomoya"),
    ("红叶见赏期从南向北移动是错的", "Che la stagione delle foglie vada da sud a nord è sbagliato"),
    ("细长的零食把人与人连接起来", "Gli snack sottili uniscono le persone"),
    ("西宫神社每年5000组以上参拜", "Oltre 5.000 gruppi all\'anno visitano il santuario Nishinomiya"),
    ("見頃＝最佳观赏期", "見頃 = la stagione migliore"),
    ("見頃＝最佳观赏期 c", "見頃 = la stagione migliore c"),
    ("读书周从10月27日（周二）开始", "La Settimana della Lettura è iniziata il 27 ottobre (martedì)"),
    ("读书周在11月9日（周一）结束", "La Settimana della Lettura finisce il 9 novembre (lunedì)"),
    ("读书周结束后阅读习惯仍继续", "L\'abitudine di leggere continua dopo la Settimana della Lettura"),
    ("调查对象是200个七五三家庭", "L\'indagine riguardava 200 famiglie di Shichi-Go-San"),
    ("调查显示11月上旬参拜占26%", "Le visite di inizio novembre erano il 26 % nell\'indagine"),
    ("调查显示71%的家庭在神社接受祈祷", "Il 71 % delle famiglie riceve una preghiera al santuario, dice l\'indagine"),
    ("调查显示74%的家庭在照相馆拍照", "Il 74 % delle famiglie fa foto in studio, dice l\'indagine"),
    ("调查显示参拜最多的是11月上旬（26%）", "Le visite culminano a inizio novembre (26 %), dice l\'indagine"),
    ("软银4连胜夺冠", "Quattro vittorie di fila per il titolo"),
    ("软银第13次夺冠", "Il 13º titolo di SoftBank"),
    ("酉の市二の酉在11月19日（周四）", "Il Ni-no-tori di Tori-no-ichi è il 19 novembre (giovedì)"),
    ("酉の市＝11月酉日集市 a", "酉の市 = una fiera nei giorni del gallo di novembre a"),
    ("预报日期是见赏期开始的参考标准", "Le date previste segnano l\'inizio della stagione migliore"),
    ("高尾山的红叶从11月13日（周五）前后进入见赏期", "Le foglie del monte Takao culminano dal 13 novembre (venerdì) circa"),
    ("高尾山的红叶从13日（周五）前后进入最佳观赏期", "Le foglie del monte Takao culminano dal 13 (venerdì) circa"),
    ("鸣子峡已经进入见赏期", "La gola di Naruko è già al meglio"),
    ("落葉＝落叶 a", "落葉 = foglie cadute a"),
    ("プリッツ＝咸味细饼干 c", "プリッツ = biscotto sottile salato c"),
]

PER_FILE = {
    "bslib4.py": [
        ('("译注｜" + s,', '("Nota — " + s,'),
        ('"Lucerna · 日语周报 VOL.3 · LUCERNA JAPANESE WEEKLY"',
         '"Lucerna · SETTIMANALE GIAPPONESE VOL.3 · TESTI IN GIAPPONESE · SPIEGAZIONI IN ITALIANO"'),
        ('f"第 {n} 版 / 共 {total} 版"', 'f"Pagina {n} di {total}"'),
    ],
    "content12.py": [
        ('p.text(975, 330, "日本語版 · VOL.3 · 七五三 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")',
         'p.text(975, 316, "日本語版 · VOL.3 · 七五三 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")\n'
         'p.text(975, 356, "TESTI IN GIAPPONESE · SPIEGAZIONI IN ITALIANO — L\'EDIZIONE PER I LETTORI ITALIANI", 19, "sans", True, BRICK, anchor="middle")'),
        ('p.text(975, 372, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")',
         'p.text(975, 390, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")'),
        ('p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)',
         'p.hline(MX, RIGHT, 406, INK, 3); p.hline(MX, RIGHT, 413, INK, 1.2)'),
        ('"毎週、日本語で · 每周一期 · 日本人が読んでいる日本語を読む"',
         '"毎週、日本語で · Ogni settimana · 日本人が読んでいる日本語を読む"'),
        ('"周日是七五三"', '"Domenica è Shichi-Go-San"'),
        ('"红叶最佳观赏期向南移动 · 详见第 6 版"',
         '"La stagione delle foglie va a sud · Vedi pagina 6"'),
        ('"トップニュース · 头条"', '"トップニュース · Notizia principale"'),
        ('"終わる 结束 · お参り 参拜 · 移る 移动 · 熊手 竹耙吉祥物。"',
         '"終わる finire · お参り visitare un santuario · 移る spostarsi · 熊手 rastrello fortunato."'),
        ('"数字で見る今週 · 数字看本周"', '"数字で見る今週 · Settimana in numeri"'),
        ('"今すぐ練習 · 即学即练"', '"今すぐ練習 · Esercitati ora"'),
        ('"来源与日期见各篇文章，非精确统计"',
         '"Date negli articoli; non statistiche esatte"'),
        ('"この号の内容 · 本期目录"', '"この号の内容 · In questo numero"'),
        ('"全部"', '"Tutti i livelli"'),
        ('"今週のことば · 本周单词"', '"今週のことば · Parola della settimana"'),
        ('"千歳飴＝ 七五三的红白长糖。"',
         '"千歳飴 = caramella di Shichi-Go-San."'),
        ('"短いニュース · 快讯"', '"短いニュース · Notizie brevi"'),
        ('"クイズ · 闪电问答"', '"クイズ · Quiz rapido"'),
        ('"读头版，选出正确答案 · 答案见第 8 版"',
         '"Leggi la prima pagina e scegli · Risposte a pagina 8"'),
        ('"レベル A2 · ポッキーの日と千歳飴 · 波奇日与千岁糖"',
         '"レベル A2 · ポッキーの日と千歳飴 · Giorno dei Pocky e chitose-ame"'),
        ('"細い 细长的 · 似ている 相似 · 分け合う 分享 · 塩味 咸味。"',
         '"細い sottile · 似ている assomigliare · 分け合う condividere · 塩味 salato."'),
        ('"願い 愿望 · 撮る 拍照 · 楽しむ 享受。"',
         '"願い un augurio · 撮る scattare una foto · 楽しむ godersi."'),
        ('"你呢？11月11日想和谁分享波奇？写两句日语寄来。"',
         '"Con chi ti piacerebbe condividere i Pocky l\'11 novembre? Scrivi due frasi in giapponese e mandale."'),
        ('"11月のことば · 11月词语"', '"11月のことば · Parole di novembre"'),
        ('"「1」の日と七五三の4つの言葉 · 关于“1”之日与七五三的四个词"',
         '"「1」の日と七五三の4つの言葉 · Quattro parole per il giorno degli 1 e Shichi-Go-San"'),
        ('"波奇巧克力棒"', '"bastoncino al cioccolato"'),
        ('"红白长糖"', '"lunga caramella rossa e bianca"'),
        ('"祈求生意兴隆的竹耙"', '"rastrello fortunato per gli affari"'),
        ('"最佳观赏期"', '"la stagione migliore"'),
        ('"練習 · 第 2 版练习"', '"練習 · Esercizi pagina 2"'),
    ],
    "content34.py": [
        ('"レベル A2→B1 · 七五三と酉の市 · 七五三与酉之市"',
         '"レベル A2→B1 · 七五三と酉の市 · Shichi-Go-San e Tori-no-ichi"'),
        ('"成長 成长 · 元気 健康 · 願い 愿望 · 日にち 日期。"',
         '"成長 crescita · 元気 in salute · 願い un augurio · 日にち la data."'),
        ('"商売繁盛 生意兴隆 · 縁起物 吉祥物 · 並ぶ 排列。"',
         '"商売繁盛 affari fiorenti · 縁起物 portafortuna · 並ぶ mettersi in fila."'),
        ('"你呢？七五三那天想拍什么样的照片？写两句日语寄来。"',
         '"Che tipo di foto ti piacerebbe fare a Shichi-Go-San? Scrivi due frasi in giapponese e mandale."'),
        ('"練習 · 第 3 版练习"', '"練習 · Esercizi pagina 3"'),
        ('"レベル B1 · 日本シリーズ4連勝 · 日本大赛四连胜"',
         '"レベル B1 · 日本シリーズ4連勝 · Quattro vittorie di fila alle Japan Series"'),
        ('"接戦 势均力敌的比赛 · サヨナラ 再见（致胜） · 連続 连续。"',
         '"接戦 partita combattuta · サヨナラ fuoricampo decisivo (sayonara) · 連続 di fila."'),
        ('"日本シリーズの記録 · 大赛记录"', '"日本シリーズの記録 · Bilancio"'),
        ('"前号 上一期 · 全部 全部。"', '"前号 il numero scorso · 全部 tutto."'),
        ('"大相撲九州場所が始まりました · 大相扑九州场所开幕"',
         '"大相撲九州場所が始まりました · Il torneo di sumo di Kyushu è iniziato"'),
        ('"練習 · 第 4 版练习"', '"練習 · Esercizi pagina 4"'),
    ],
    "content56.py": [
        ('"若者・エンタメ · 青年"', '"若者・エンタメ · Giovani"'),
        ('"レベル B1 · 11月11日の分かち合い · 11月11日的分享"',
         '"レベル B1 · 11月11日の分かち合い · Condivisione l\'11 novembre"'),
        ('"渡す 递给 · つなぐ 连接 · 送り合う 互相发送。"',
         '"渡す porgere · つなぐ collegare · 送り合う mandarsi."'),
        ('"思い出 回忆 · 大きくなる 长大。"',
         '"思い出 un ricordo · 大きくなる crescere."'),
        ('"你呢？想把波奇递给谁？写两句日语寄来。"',
         '"A chi ti piacerebbe porgere i Pocky? Scrivi due frasi in giapponese e mandale."'),
        ('"練習 · 第 5 版练习"', '"練習 · Esercizi pagina 5"'),
        ('"レベル B2 · 紅葉の見頃は南へ · 红叶最佳观赏期向南移动"',
         '"レベル B2 · 紅葉の見頃は南へ · La stagione delle foglie va a sud"'),
        ('"目安 标准 · 色づき 变色 · 変化 变化 · 準備 准备。"',
         '"目安 una guida · 色づき colorazione · 変化 cambiamento · 準備 preparazione."'),
        ('"グラフを読もう · 读图表"', '"グラフを読もう · Leggere il grafico"'),
        ('"練習用データ · 练习数据"', '"練習用データ · Dati di esercizio"'),
        ('"練習 · 第 6 版练习"', '"練習 · Esercizi pagina 6"'),
    ],
    "content7.py": [
        ('"ことば · 语言"', '"ことば · Lingua"'),
        ('"言語フォーカス · 三つのレベル、三つのテーマ · 三个级别，三个主题"',
         '"言語フォーカス · 三つのレベル、三つのテーマ · Tre livelli, tre temi"'),
        ('"読書週間 读书周 · 習慣 习惯 · 借りる 借。"',
         '"読書週間 Settimana della Lettura · 習慣 un\'abitudine · 借りる prendere in prestito."'),
        ('"七五三 七五三 · 千歳飴 千岁糖 · 晴れ着 盛装"',
         '"七五三 Shichi-Go-San · 千歳飴 chitose-ame · 晴れ着 abiti da festa"'),
        ('"〜連勝 连胜 · 〜% 百分之〜 · 〜組以上 组以上。"',
         '"〜連勝 vittorie di fila · 〜% per cento · 〜組以上 gruppi o più."'),
        ('"まちがい診療所 · 易错诊所"', '"まちがい診療所 · Clinica degli errori"'),
        ('"有「昨日」时要用过去式。"', '"Con 「昨日」, usa il passato."'),
        ('"动词名词化时要加「こと」。"',
         '"Aggiungi 「こと」 per fare un nome da un verbo."'),
        ('"得到东西的场所用「で」。"',
         '"Usa 「で」 per il luogo dove ricevi qualcosa."'),
        ('"看的场所用「で」。"', '"Usa 「で」 per il luogo dove guardi."'),
        ('"今週のフレーム · 本周句式"', '"今週のフレーム · La struttura"'),
        ('"句式拆解：追赶最佳观赏期。"',
         '"Analisi: a caccia della stagione migliore."'),
        ('"読者の手紙 · 读者园地"', '"読者の手紙 · Angolo dei lettori"'),
        ('ld = "※この手紙は編集部の例です。締め切りまでに、本当の読者の手紙と第8版の作文の優秀作は届きませんでした。VOL.4に載せます。"',
         'ld_it = "Esempio della redazione, non una vera lettera. Alla scadenza non '
         'erano arrivate lettere né composizioni; entrambe appariranno '
         'nel VOL.4. Mandateci la vostra lettera in giapponese: le scelte '
         'saranno pubblicate nel VOL.4!"'),
        ('lcn = "编辑部示例信，非真实来信。截至截稿，未收到真实来信与第8版最佳作文；VOL.4将刊登收到的来信与佳作。"\n',
         ''),
        ('lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld, "serif", False, 20.5, CW - 44)) * 29 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26 + 16',
         'lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld_it, "sans", False, 20, CW - 44)) * 29 + 26 + 16'),
        ('yy3 = p.para(bx + 22, yy3 + 20, ld, 20.5, "serif", False, GREY, CW - 44, 1.42) + 10\n'
         'p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)',
         'p.para(bx + 22, yy3 + 20, ld_it, 20, "sans", False, GREY, CW - 44, 1.42)'),
        ('"今週のフレーズ · 本周金句（逐字摘自本期文章）"',
         '"今週のフレーズ · Frasi della settimana (testuali, da questo numero)"'),
        ('"读书周在11月9日星期一结束。"', '"La Settimana della Lettura finisce lunedì 9 novembre."'),
        ('"11月15日星期日是七五三的中心日。"',
         '"Domenica 15 novembre è il cuore di Shichi-Go-San."'),
        ('"波奇与百力滋之日始于1999年。"', '"Il giorno di Pocky e Pretz è iniziato nel 1999."'),
        ('"千岁糖是寄托长寿愿望的糖果。"',
         '"Chitose-ame è la caramella dell\'augurio di lunga vita."'),
        ('"七五三是3岁、5岁和7岁孩子的庆祝活动。"',
         '"Shichi-Go-San celebra i bambini di 3, 5 e 7 anni."'),
        ('"软银以四连胜夺得日本第一。"',
         '"SoftBank ha preso il titolo del Giappone con quattro vittorie di fila."'),
        ('"11月11日是波奇日。"', '"L\'11 novembre è il giorno dei Pocky."'),
        ('"红叶的最佳观赏期从北向南移动。"',
         '"La stagione migliore delle foglie va da nord a sud."'),
        ('"第1面"', '"pag. 1"'),
        ('"第2面"', '"pag. 2"'),
        ('"第3面"', '"pag. 3"'),
        ('"第4面"', '"pag. 4"'),
        ('"第5面"', '"pag. 5"'),
        ('"第6面"', '"pag. 6"'),
        ('"来週 · 下期预告 (VOL.4)"', '"来週 · Prossimo numero (VOL.4)"'),
    ],
    "content8.py": [
        ('af.para(f"— 第{pg}面 —", 13.3, "sans", True, OLIVE, lh=1.16, gap=2, split=False)', 'af.para(f"— 第{pg}面 —", 12.9, "sans", True, OLIVE, lh=1.13, gap=2, split=False)'),
        ('af.para(txt, 13.3, lh=1.16, gap=0.5, split=False)', 'af.para(txt, 12.9, lh=1.13, gap=0.5, split=False)'),
        ('"テストと答え · 练习与答案"', '"テストと答え · Test e risposte"'),
        ('"七五三是11月15日。"', '"Shichi-Go-San è il 15 novembre."'),
        ('"波奇日从1999年开始。"', '"Il giorno dei Pocky è iniziato nel 1999."'),
        ('"读书周从10月27日开始。→ ___"',
         '"La Settimana della Lettura inizia il 27 ottobre. → ___"'),
        ('"去看红叶的人可以自北向南追赶最佳观赏期。→ ___"',
         '"Chi va a vedere le foglie può inseguire la stagione migliore da nord a sud. → ___"'),
        ('f"写作题（无唯一答案）；范文（{NCHARS} 字）见下。"',
         'f"Compito di scrittura (senza un\'unica risposta giusta); il testo modello ({NCHARS} caratteri) è sotto."'),
        ('"（开放题，范文如下）"', '"(compito aperto — testo modello sotto)"'),
        ('f"范文见本版 H 区（{NCHARS} 字）"',
         'f"Testo modello nella sezione H di questa pagina ({NCHARS} caratteri)"'),
        ('"答え · 参考答案 — 按版面分页排列，找到题号即可"',
         '"答え · Risposte — raggruppate per pagina; trova solo il tuo numero"'),
        ('"每题附一句中文简析 · 带 ✓ 的为范文题"',
         '"Una breve nota in italiano con ogni risposta · ✓ = l\'esercizio con testo modello"'),
        ('f"— 第{pg}面 —"', 'f"— PAGINA {pg} —"'),
    ],
    "render.py": [
        ('"Lucerna-VOL3.pdf"', '"Lucerna-VOL3-IT.pdf"'),
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
