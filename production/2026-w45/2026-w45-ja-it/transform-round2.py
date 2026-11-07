# -*- coding: utf-8 -*-
"""JA core (VOL.2, Chinese explanations) -> JA x IT edition transform.

Re-runnable: reads the PRISTINE W45 JA core build, applies exact-literal
replacements (whole strings, never AST byte offsets, never byte slicing),
and writes the edition build into this directory. Fix rounds edit THIS
file, then re-run: transform.py -> run.py (one process) -> render.py.

Frozen: every Japanese article/stem/option/letter/figure string is copied
byte-identical. Only the explanation layer changes: Chinese notes/glosses/
headers/instructions -> Italian, per the W43 JA x IT shipped precedent
(files/weekly-report-ja-it). Masthead geometry follows the W43 JA x IT
shipped SVG exactly (wordmark 248, edition 316, badge 356, tagline 390,
rules 406/413, dark band 424); the task brief's 262 wordmark figure is
superseded by that W43 measurement, recorded in the KIT.

P8 #37 trap (content34.py:82): the core registers the P3 fill-in note as
the BARE string without a weekday suffix, key 8, stem
"展覧会は11月 ___ 日（日）までです。" — 2026-11-08 is a Sunday
(verified with date). The bare key is mapped EXPLICITLY below to the
Sunday-suffixed Italian form, identical to #32's rendering; it must never
be left to fall through untranslated.
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
    "files/weekly-report-w45-ja-it")
CANON_SVGLIB_MD5 = "d73e23b365676c3618d7e060b835eb4d"

# (old, new) applied in order. Longer strings first where one contains another.
GLOBAL = [
    # --- output repoint ---
    ("weekly-report-w45-ja-core", "weekly-report-w45-ja-it"),
    # --- registry type names / instructions (Italian wording) ---
    ('instr="造句"', 'instr="Costruisci la frase"'),
    ('instr="翻译"', 'instr="Traduci"'),
    ('instr="写作"', 'instr="Scrittura"'),
    ('instr="判断"', 'instr="Vero o falso?"'),
    ('instr="填空"', 'instr="Completa"'),
    ('instr="把词和释义配对"', 'instr="Abbina le parole ai significati"'),
    ('instr="把活动和地点·时间配对"', 'instr="Abbina eventi a luoghi e date"'),
    ('"完形单选"', '"cloze"'),
    ('"单选"', '"scelta multipla"'),
    ('"完成句子"', '"completamento"'),
    ('"词汇配对"', '"abbinamento"'),
    ('"造句"', '"costruzione di frasi"'),
    ('"判断对错"', '"vero/falso"'),
    ('"翻译"', '"traduzione"'),
    ('"写作"', '"scrittura"'),
    # --- shared furniture ---
    ('"あなたは？ · 说说你自己"', '"あなたは？ · Tocca a te"'),
    ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
     '"Risposte a pagina 8 · I livelli sono misti: cerca il numero"'),
]

# Answer-note translations. One Italian rendering per distinct core note;
# duplicates share the rendering (correct: same note -> same meaning).
NOTES = [
    ("文化日在11月3日（周二）", "La Festa della Cultura è il 3 novembre (martedì)"),
    ("读书周到11月9日（周一）", "La Settimana della Lettura dura fino al 9 novembre (lunedì)"),
    ("見頃＝最佳观赏期", "見頃 = il momento migliore per ammirare"),
    ("立冬＝冬天的开始", "立冬 = l'inizio dell'inverno"),
    ("神户灯光秀从7日（周六）开始", "Le luminarie di Kobe cominciano il 7 (sabato)"),
    ("文化日全国都有文化活动", "Eventi culturali in tutto il paese"),
    ("立冬在11月7日（周六）", "立冬 cade il 7 novembre (sabato)"),
    ("灯光秀在神户开始", "Le luminarie cominciano a Kobe"),
    ("「ゆる」＝无理をしない", "「ゆる」 = senza forzature"),
    ("鍋の食卓は去年の1.5倍", "Le cene con nabe sono 1,5 volte quelle dello scorso anno"),
    ("発表は10月21日", "L'annuncio è del 21 ottobre"),
    ("11月から1月まで気温は平年より高い",
     "Da novembre a gennaio: temperature sopra la media"),
    ("服と食事の話題はnoteのまとめによるもの",
     "Temi di abbigliamento e cibo dalla rassegna di note"),
    ("ゆる＝轻松、不勉强", "ゆる = rilassato, senza forzature"),
    ("蒸し器＝蒸笼", "蒸し器 = un cestello per la cottura a vapore"),
    ("整える＝调理、调养", "整える = rimettere in ordine"),
    ("鍋＝一锅菜", "鍋 = un piatto unico in pentola"),
    ("鍋の材料が1か月早く並んだ", "Gli ingredienti per il nabe sono apparsi un mese prima"),
    ("気象庁の予報は10月20日", "La previsione della JMA è del 20 ottobre"),
    ("サクサクdeコパンが1,300万食を超えた",
     "サクサクdeコパン ha superato i 13 milioni di porzioni"),
    ("ゆる＝轻松 b", "ゆる = rilassato b"),
    ("蒸し器＝蒸笼 a", "蒸し器 = cestello a vapore a"),
    ("麻辣湯＝辛いスープ d", "麻辣湯 = zuppa piccante d"),
    ("予報＝天気の予想 c", "予報 = previsione del tempo c"),
    ("杉并的活动是家庭管弦乐队", "L'evento di Suginami è un'orchestra di famiglia"),
    ("传统工艺展在石川县立美术馆",
     "Mostra di artigianato al Museo d'arte di Ishikawa"),
    ("传统工艺展到11月8日", "La mostra dura fino all'8 novembre"),
    ("灯光秀在金泽城和兼六园", "Le luminarie sono al castello di Kanazawa e a Kenrokuen"),
    ("市場＝集市", "市場 = mercato"),
    ("工芸＝工艺", "工芸 = artigianato"),
    ("陶器＝陶瓷", "陶器 = ceramica"),
    ("工艺展到11月8日（周日）", "La mostra dura fino all'8 novembre (domenica)"),
    ("金箔＝金箔", "金箔 = foglia d'oro"),
    # P8 #37 BARE note (P3 exercise, key 8) — explicit mapping to the
    # Sunday-suffixed form; distinct from #32's suffixed note above and
    # from the 传统… note. 2026-11-08 is a Sunday; the stem itself says
    # （日）. Never left bare.
    ("工艺展到11月8日", "La mostra dura fino all'8 novembre (domenica)"),
    ("主语＋时间", "soggetto + tempo"),
    ("地点＋で＋あります", "luogo + で + あります"),
    ("见たい＝想看", "見たい = voler vedere"),
    ("和家人一起", "insieme alla famiglia"),
    ("文化の日＝11月3日 b", "文化の日 = 3 novembre b"),
    ("工芸展＝美術館 c", "工芸展 = museo c"),
    ("オーケストラ＝杉並 d", "オーケストラ = Suginami d"),
    ("ライトアップ＝金沢城 a", "ライトアップ = castello di Kanazawa a"),
    ("第1战软银3-1胜DeNA", "Gara 1: SoftBank batte DeNA 3–1"),
    ("第2战逆转的是筒香的3分本垒打", "A ribaltare gara 2 è il fuoricampo da 3 punti di Tsutsugo"),
    ("2连胜开局的是软银", "A partire con due vittorie di fila è SoftBank"),
    ("2连胜开局的夺冠率是73%", "Chi parte 2–0 vince il titolo nel 73% dei casi"),
    ("2024年夺冠的是DeNA", "Nel 2024 ha vinto il titolo DeNA"),
    ("第1战软银得3分", "In gara 1 SoftBank ha segnato 3 punti"),
    ("第2战软银得4分", "In gara 2 SoftBank ha segnato 4 punti"),
    ("第1战打到延长11局", "Gara 1 è andata all'11º inning"),
    ("第2战打到延长10局", "Gara 2 è andata al 10º inning"),
    ("夺冠率73%", "Percentuale di titolo: 73%"),
    ("延長＝比赛延长", "延長 = la partita che si allunga"),
    ("第1战观众33,388人", "Pubblico di gara 1: 33.388"),
    ("第2战观众33,432人", "Pubblico di gara 2: 33.432"),
    ("相川监督说「4场胜负之战」", "Aikawa: una lotta per quattro vittorie"),
    ("第1戦は土よう日です", "Gara 1 era di sabato"),
    ("ソフトバンクが2連勝しました", "SoftBank ha vinto due volte di fila"),
    ("第2戦も延長戦でした", "Anche gara 2 è andata agli extra inning"),
    ("2024年はDeNAが優勝しました", "Nel 2024 DeNA ha vinto il titolo"),
    ("万圣节在10月31日（周六）", "Halloween era il 31 ottobre (sabato)"),
    ("涩谷禁酒时间是18时到5时", "Divieto di bere per strada a Shibuya: 18:00–05:00"),
    ("乱扔垃圾罚款2,000日元", "Buttare rifiuti costa una multa di 2.000 yen"),
    ("化妆活动在池袋", "Il festival del cosplay è a Ikebukuro"),
    ("横滨中区民祭在11月8日（周日）", "Festival del quartiere Naka: 8 novembre (domenica)"),
    ("万圣节在10月31日", "Halloween era il 31 ottobre"),
    ("禁酒从18时开始", "Il divieto comincia alle 18:00"),
    ("禁酒到早上5时", "Il divieto dura fino alle 05:00"),
    ("横滨祭典在11月8日", "Il festival di Yokohama è l'8 novembre"),
    ("夜里路上不能喝酒", "Di notte non si può bere per strada"),
    ("ゴミの罰金は今年6月からです", "La multa per i rifiuti è in vigore da giugno di quest'anno"),
    ("コスプレフェスは池袋です", "Il festival del cosplay è a Ikebukuro"),
    ("ハロウィンは10月31日（土）", "Halloween era il 31 ottobre (sabato)"),
    ("飲むことができません＝不能喝", "飲むことができません = non si può bere"),
    ("守って、〜しましょう", "守って + 〜しましょう = seguiamo le regole"),
    ("フェンスの中＝围栏里面", "フェンスの中 = dentro la recinzione"),
    ("活动从10月30日到11月1日", "Il festival si è svolto dal 30 ottobre al 1º novembre"),
    ("雨が多いのは太平洋側", "Sul lato del Pacifico piove di più"),
    ("九州の旅の検索は去年のほぼ2倍",
     "Ricerche di viaggi in Kyushu quasi raddoppiate"),
    ("1回の旅の予算は下がった", "Il budget per viaggio è sceso"),
    ("鳴子峡の見頃は10月31日から11月8日の週末",
     "Picco di Naruko Gorge: fine settimana 31 ottobre–8 novembre"),
    ("图中最受欢迎的是近处的满足感", "Nel grafico vince la soddisfazione vicina"),
    ("近场满足感38%", "Soddisfazione vicina: 38%"),
    ("温泉27%", "Terme: 27%"),
    ("红叶21%与美食14%之差为7", "Foglie 21% meno cibo 14% fa 7"),
    ("38+27=65", "38 + 27 = 65"),
    ("四项合计100%", "Le quattro voci sommano al 100%"),
    ("立冬在11月7日", "立冬 cade il 7 novembre"),
    ("神户灯光秀到12月28日", "Le luminarie di Kobe durano fino al 28 dicembre"),
    ("九州旅行搜索约为去年的2倍",
     "Ricerche di viaggi in Kyushu quasi doppie"),
    ("气象厅预报在10月20日", "La previsione della JMA è del 20 ottobre"),
    ("11月は平年より暖かい予報です", "Novembre è previsto più caldo della media"),
    ("九州の旅の検索は増えました", "Le ricerche di viaggi in Kyushu sono aumentate"),
    ("グラフは練習用データです", "Il grafico è un dato di esercitazione"),
    ("读书周从10月27日（周二）开始", "Settimana della Lettura dal 27 ottobre (martedì)"),
    ("读书周到11月9日", "La Settimana della Lettura dura fino al 9 novembre"),
    ("口号是「静かだけど、冒険中。」", "Lo slogan è 「静かだけど、冒険中。」"),
    ("图书馆活动有图书介绍", "L'evento in biblioteca è la presentazione di libri"),
    ("見頃＝红叶最美的时候", "見頃 = quando le foglie sono al loro meglio"),
    ("紅葉狩り＝去看红叶", "紅葉狩り = uscire ad ammirare le foglie"),
    ("ライトアップ＝夜里用灯光照亮", "ライトアップ = illuminare di notte"),
    ("落葉＝落叶", "落葉 = foglie cadute"),
    ("1.5倍＝比去年多50%", "1.5倍 = il 50% in più dello scorso anno"),
    ("73%≈4人中的3人", "73% ≈ 3 su 4"),
    ("サクサクdeコパンが1,300万食", "サクサクdeコパン ha raggiunto i 13 milioni di porzioni"),
    ("日本大赛第1战在10月24日（周六）", "Gara 1 delle Japan Series era il 24 ottobre (sabato)"),
    ("第2战软银4-3获胜", "Gara 2: SoftBank ha vinto 4–3"),
    ("神户灯光秀从7日开始", "Le luminarie di Kobe cominciano il 7"),
    ("2连胜开局的夺冠率73%", "Percentuale di titolo per chi parte 2–0: 73%"),
    ("气象厅预报气温高于往年", "La previsione della JMA: più caldo della media"),
    ("美香周二和家人去金泽", "Martedì Mika va a Kanazawa con la famiglia"),
    ("在金泽看传统工艺展和灯光秀", "A Kanazawa vede la mostra di artigianato e le luminarie"),
    ("周六和朋友去神户", "Sabato va a Kobe con gli amici"),
    ("读书周想借2本书", "Per la Settimana della Lettura: 2 libri in prestito"),
    ("主语＋时间＋地点＋动词", "soggetto + tempo + luogo + verbo"),
    ("场所用「で」", "usa 「で」 per il luogo"),
    ("2连胜开局", "partire con due vittorie di fila"),
    ("見頃＝最佳观赏期 b", "見頃 = momento migliore per ammirare b"),
    ("鍋＝一锅菜 d", "鍋 = piatto unico in pentola d"),
    ("落葉＝落叶 a", "落葉 = foglie cadute a"),
    ("予算＝预算 c", "予算 = budget c"),
    ("見せてください＝请出示", "見せてください = per favore, mostri"),
    ("借りられます＝能借（可能形）", "借りられます = prendere in prestito (potenziale)"),
    ("读书周到11月9日（第7版）", "Settimana della Lettura fino al 9 novembre (pagina 7)"),
    ("「紅葉の本」受欢迎", "「紅葉の本」 è popolare"),
    ("どういたしまして＝不客气", "どういたしまして = prego, di niente"),
    ("对照第3版", "Vedi pagina 3"),
    ("对照第5版", "Vedi pagina 5"),
    ("对照第7版", "Vedi pagina 7"),
    ("对照第6版（神户的灯光秀）", "Vedi pagina 6 (le luminarie di Kobe)"),
]

# Per-file furniture / gloss / structural replacements.
PER_FILE = {
    "bslib4.py": [
        ('("译注｜" + s,', '("Nota — " + s,'),
        ('"Lucerna · 日语周报 VOL.2 · LUCERNA JAPANESE WEEKLY"',
         '"Lucerna · SETTIMANALE GIAPPONESE VOL.2 · TESTI IN GIAPPONESE · SPIEGAZIONI IN ITALIANO"'),
        ('f"第 {n} 版 / 共 {total} 版"', 'f"Pagina {n} di {total}"'),
    ],
    "content12.py": [
        # P1 masthead -> W43 JA x IT shipped geometry
        ('p.text(975, 262, "Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")',
         'p.text(975, 248, "Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")'),
        ('p.text(975, 330, "日本語版 · VOL.2 · 文化の日 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")',
         'p.text(975, 316, "日本語版 · VOL.2 · 文化の日 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")\n'
         'p.text(975, 356, "TESTI IN GIAPPONESE · SPIEGAZIONI IN ITALIANO — L\'EDIZIONE PER I LETTORI ITALIANI", 19, "sans", True, OLIVE, anchor="middle")'),
        ('p.text(975, 372, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")',
         'p.text(975, 390, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")'),
        ('p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)',
         'p.hline(MX, RIGHT, 406, INK, 3); p.hline(MX, RIGHT, 413, INK, 1.2)'),
        ('"毎週、日本語で · 每周一期 · 日本人が読んでいる日本語を読む"',
         '"毎週、日本語で · Ogni settimana · 日本人が読んでいる日本語を読む"'),
        ('"周二是文化日"', '"Martedì è la Festa della Cultura"'),
        ('"节日过后，红叶周末到来 · 详见第 3 版"',
         '"Dopo la festa, arriva il fine settimana delle foglie · Vedi pagina 3"'),
        ('"トップニュース · 头条"', '"トップニュース · In primo piano"'),
        ('"祝日 节假日 · 見頃 最佳观赏期 · 暦 历法 · お届けします 为您送上。"',
         '"祝日 giorno festivo · 見頃 momento migliore per ammirare · 暦 calendario · お届けします per portarvi."'),
        ('"数字で見る今週 · 数字看本周"', '"数字で見る今週 · In numeri"'),
        ('"今すぐ練習 · 即学即练"', '"今すぐ練習 · Esercitati subito"'),
        ('"这四个话题，都是本期报纸的主题。"',
         '"Questi quattro temi danno forma al numero."'),
        ('"来源与日期见各篇文章，非精确统计"',
         '"Date negli articoli; non statistiche esatte"'),
        ('"この号の内容 · 本期目录"', '"この号の内容 · In questo numero"'),
        ('"今週のことば · 本周单词"', '"今週のことば · La parola della settimana"'),
        ('"ゆる＝ 轻松、不勉强。"', '"ゆる = rilassato, senza forzature."'),
        ('"短いニュース · 快讯"', '"短いニュース · Notizie in breve"'),
        ('"クイズ · 闪电问答"', '"クイズ · Quiz lampo"'),
        ('"读头版，选出正确答案 · 答案见第 8 版"',
         '"Leggi la prima pagina e scegli · Risposte a pagina 8"'),
        # P2
        ('"レベル A2 · ゆる整え食と暖かい11月 · 轻松食养与暖和的11月"',
         '"レベル A2 · ゆる整え食と暖かい11月 · Cibo delicato e un novembre caldo"'),
        ('"蒸す 蒸 · 並ぶ 摆上货架 · 食卓 餐桌 · 超える 超过。"',
         '"蒸す cuocere a vapore · 並ぶ apparire sugli scaffali · 食卓 la tavola · 超える superare."'),
        ('"予報 预报 · 平年 往年平均 · 季節風 季风 · 話題 话题 · 値上がり 涨价。"',
         '"予報 previsione · 平年 un anno medio · 季節風 vento stagionale · 話題 tema · 値上がり aumenti di prezzo."'),
        ('"你呢？寒冷的日子想吃什么锅？写两句日语寄来。"',
         '"E tu? In un giorno freddo, quale nabe vorresti mangiare? Scrivi due frasi in giapponese e inviale."'),
        ('"季節のことば · 季节词语"', '"季節のことば · Parole della stagione"'),
        ('"ゆる整え食の4つの言葉 · 关于轻松食养的四个词"',
         '"ゆる整え食の4つの言葉 · Quattro parole per mangiare con delicatezza"'),
        ('"一锅菜"', '"un piatto unico in pentola"'),
        ('"蒸笼"', '"un cestello a vapore"'),
        ('"轻松、不勉强"', '"rilassato, senza forzature"'),
        ('"调理、调养"', '"rimettere in ordine corpo e mente"'),
        ('"練習 · 第 2 版练习"', '"練習 · Esercizi di pagina 2"'),
    ],
    "content34.py": [
        ('"レベル A2→B1 · 文化の日と金沢 · 文化日与金泽"',
         '"レベル A2→B1 · 文化の日と金沢 · Festa della Cultura e Kanazawa"'),
        ('"市場 市场 · 工芸 工艺 · 光 灯光 · 楽しむ 享受。"',
         '"市場 mercato · 工芸 artigianato · 光 luce · 楽しむ godere."'),
        ('"陶器 陶瓷 · 漆器 漆器 · 染物 染色织物 · 金箔 金箔。"',
         '"陶器 ceramica · 漆器 lacca · 染物 tessuti tinti · 金箔 foglia d\'oro."'),
        ('"你呢？文化日想去参加什么文化活动？写两句日语寄来。"',
         '"E tu? A quale evento culturale vorresti andare per la Festa della Cultura? Scrivi due frasi in giapponese e inviale."'),
        ('"練習 · 第 3 版练习"', '"練習 · Esercizi di pagina 3"'),
        ('"レベル B1 · 日本シリーズ横浜の2試合 · 日本大赛横滨两场"',
         '"レベル B1 · 日本シリーズ横浜の2試合 · Japan Series: due gare a Yokohama"'),
        ('"延長 延长赛 · 逆転 逆转 · 同点 平分 · 優勝率 夺冠率。"',
         '"延長 extra inning · 逆転 rimonta · 同点 pareggio · 優勝率 percentuale di titolo."'),
        ('"総括 总结 · 締め切り 截稿 · 確認する 核实。"',
         '"総括 bilancio · 締め切り scadenza · 確認する verificare."'),
        ('"日本シリーズの日程 · 大赛日程"', '"日本シリーズの日程 · Calendario"'),
        ('"横浜の2試合の記録 · 横滨两场比赛的记录"',
         '"横浜の2試合の記録 · Le due gare di Yokohama, agli atti"'),
        ('"練習 · 第 4 版练习"', '"練習 · Esercizi di pagina 4"'),
    ],
    "content56.py": [
        ('"若者・エンタメ · 青年"', '"若者・エンタメ · Giovani"'),
        ('"レベル B1 · ハロウィンと秋まつり · 万圣节与秋日祭典"',
         '"レベル B1 · ハロウィンと秋まつり · Halloween e feste d\'autunno"'),
        ('"罰金 罚款 · 像 雕像 · 仮装 变装 · 守る 遵守。"',
         '"罰金 multa · 像 statua · 仮装 travestirsi · 守る rispettare."'),
        ('"祭り 节日 · 週末 周末 · 話題 话题。"',
         '"祭り festa · 週末 fine settimana · 話題 tema."'),
        ('"你呢？秋日祭典上想做什么？写两句日语寄来。"',
         '"E tu? Che cosa vorresti fare a una festa d\'autunno? Scrivi due frasi in giapponese e inviale."'),
        ('"練習 · 第 5 版练习"', '"練習 · Esercizi di pagina 5"'),
        ('"レベル B2 · 暖かい11月と秋の旅 · 暖和的11月与秋日旅行"',
         '"レベル B2 · 暖かい11月と秋の旅 · Un novembre caldo e viaggi d\'autunno"'),
        ('"予算 预算 · 満足 满足 · 観測 观测 · 追いかける 追赶。"',
         '"予算 budget · 満足 soddisfazione · 観測 osservazione · 追いかける inseguire."'),
        ('"グラフを読もう · 读图表"', '"グラフを読もう · Leggere il grafico"'),
        ('"練習用データ · 练习数据"', '"練習用データ · Dati di esercitazione"'),
        ('"練習 · 第 6 版练习"', '"練習 · Esercizi di pagina 6"'),
    ],
    "content7.py": [
        ('"ことば · 语言"', '"ことば · Lingua"'),
        ('"言語フォーカス · 三つのレベル、三つのテーマ · 三个级别，三个主题"',
         '"言語フォーカス · 三つのレベル、三つのテーマ · Tre livelli, tre temi"'),
        ('"読書週間 读书周 · 紹介 介绍 · 読み聞かせ 朗读。"',
         '"読書週間 Settimana della Lettura · 紹介 presentazione · 読み聞かせ lettura ad alta voce."'),
        ('"見頃 最佳观赏期 · 紅葉狩り 看红叶出游 · 落葉 落叶"',
         '"見頃 momento migliore per ammirare · 紅葉狩り gite per le foglie · 落葉 foglie cadute"'),
        ('"〜倍 倍 · 〜% 百分之〜 · 〜万食 万份。"',
         '"〜倍 volte · 〜% percento · 〜万食 decine di migliaia di porzioni."'),
        ('"まちがい診療所 · 易错诊所"', '"まちがい診療所 · Clinica degli errori"'),
        ('"有「昨日」时要用过去式。"', '"Con 「昨日」 si usa il passato."'),
        ('"动词名词化时要加「こと」。"',
         '"Aggiungi 「こと」 per rendere un verbo un sostantivo."'),
        ('"地点用「か所」来数。"', '"Conta i luoghi con 「か所」."'),
        ('"动作发生的场所用「で」。"',
         '"Usa 「で」 per il luogo in cui avviene un\'azione."'),
        ('"今週のフレーム · 本周句式"', '"今週のフレーム · La frase tipo"'),
        ('"句式拆解：轻松地调理身心。"',
         '"Scomposizione: rimettere in ordine corpo e mente con delicatezza."'),
        ('"読者の手紙 · 读者园地"', '"読者の手紙 · L\'angolo dei lettori"'),
        # Readers' corner: the Japanese disclosure line (ld) cannot serve
        # as the operative disclosure for Italian readers, and the
        # Chinese disclosure (lcn) is the core's reader-native layer.
        # Both are replaced by ONE Italian disclosure stating the 3
        # facts (sample, not a real letter; no real letters arrived;
        # no best Page 8 compositions arrived) + an explicit invitation
        # + the VOL.3 promise. The Japanese example letter (lt) itself
        # is frozen verbatim; the VOL.3 teaser below is untouched and
        # is NOT counted as the invitation.
        ('ld = "※この手紙は編集部の例です。締め切りまでに、本当の読者の手紙と第8版の作文の優秀作は届きませんでした。VOL.3に載せます。"',
         'ld_it = "Esempio della redazione, non una lettera vera. '
         'Entro la scadenza non sono arrivate vere lettere né i migliori testi di '
         'pagina 8; entrambi appariranno nel VOL.3. Scrivici in giapponese: '
         'le lettere scelte saranno pubblicate nel VOL.3!"'),
        ('lcn = "编辑部示例信，非真实来信。截至截稿，未收到真实来信与第8版最佳作文；VOL.3将刊登收到的来信与佳作。"\n',
         ''),
        ('lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld, "serif", False, 20.5, CW - 44)) * 29 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26 + 16',
         'lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld_it, "sans", False, 20, CW - 44)) * 29 + 26 + 16'),
        ('yy3 = p.para(bx + 22, yy3 + 20, ld, 20.5, "serif", False, GREY, CW - 44, 1.42) + 10\n'
         'p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)',
         'p.para(bx + 22, yy3 + 20, ld_it, 20, "sans", False, GREY, CW - 44, 1.42)'),
        ('"今週のフレーズ · 本周金句（逐字摘自本期文章）"',
         '"今週のフレーズ · Frasi della settimana (verbatim da questo numero)"'),
        ('"文化日是11月3日星期二。"', '"La Festa della Cultura è martedì 3 novembre."'),
        ('"这是一个慢慢地、轻松调理的日本11月。"',
         '"È un novembre giapponese lento, rimesso in ordine con delicatezza."'),
        ('"所谓ゆる，就是不勉强、慢慢来的意思。"',
         '"ゆる significa senza forzature, prendersela con calma."'),
        ('"火锅食材提前一个月上架了。"',
         '"Gli ingredienti per il nabe sono apparsi nei negozi un mese prima."'),
        ('"可以同时欣赏传统工艺、红叶与灯光。"',
         '"Si possono godere insieme artigianato tradizionale, foglie e luci."'),
        ('"软银以两连胜开局。"', '"SoftBank ha cominciato con due vittorie di fila."'),
        ('"遵守规则，过一个快乐的万圣节吧。"',
         '"Rispetta le regole e goditi un felice Halloween."'),
        ('"去看红叶的人可以自北向南追赶最佳观赏期。"',
         '"Chi va ad ammirare le foglie può inseguire il momento migliore da nord a sud."'),
        ('"第1面"', '"p.1"'),
        ('"第2面"', '"p.2"'),
        ('"第3面"', '"p.3"'),
        ('"第4面"', '"p.4"'),
        ('"第5面"', '"p.5"'),
        ('"第6面"', '"p.6"'),
        ('"来週 · 下期预告 (VOL.3)"', '"来週 · Prossimo numero (VOL.3)"'),
    ],
    "content8.py": [
        ('"テストと答え · 练习与答案"', '"テストと答え · Test e risposte"'),
        # E zone re-aim JA<->ZH -> JA<->IT (W43 JA x IT pattern):
        # E1/E2 keys (Chinese) become Italian; E3/E4 stems (Chinese)
        # become Italian; the Japanese keys/stems stay frozen.
        ('"文化日是11月3日。"', '"La Festa della Cultura è il 3 novembre."'),
        ('"乱扔垃圾，要罚2,000日元。"', '"Se butti i rifiuti, la multa è di 2.000 yen."'),
        ('"读书周从10月27日开始。→ ___"', '"La Settimana della Lettura comincia il 27 ottobre. → ___"'),
        ('"我想去神户看红叶灯光秀。→ ___"',
         '"Vorrei andare a Kobe a vedere le luminarie delle foglie. → ___"'),
        ('f"写作题（无唯一答案）；范文（{NCHARS} 字）见下。"',
         'f"Compito di scrittura (senza un\'unica risposta esatta); il testo modello ({NCHARS} caratteri) è qui sotto."'),
        ('"（开放题，范文如下）"', '"(compito aperto — testo modello qui sotto)"'),
        ('f"范文见本版 H 区（{NCHARS} 字）"',
         'f"Testo modello nella sezione H ({NCHARS} caratteri)"'),
        ('"答え · 参考答案 — 按版面分页排列，找到题号即可"',
         '"答え · Risposte — raggruppate per pagina: basta cercare il numero"'),
        ('"每题附一句中文简析 · 带 ✓ 的为范文题"',
         '"Una breve nota in italiano per ogni risposta · ✓ = la domanda con il testo modello"'),
        ('f"— 第{pg}面 —"', 'f"— PAGINA {pg} —"'),
    ],
    "render.py": [
        ('"Lucerna-VOL2.pdf"', '"Lucerna-VOL2-IT.pdf"'),
        ('"Lucerna-VOL2-web.pdf"', '"Lucerna-VOL2-IT-web.pdf"'),
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
    global replace corrupted frozen text in the sibling round 1. Two scoped sites:
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
