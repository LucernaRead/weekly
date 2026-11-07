# -*- coding: utf-8 -*-
"""W45 ES core -> ES x ZH-TW fan-out transform for the BUILD COPY ONLY.

Literal replacements only (README #17/#18): each quoted literal is replaced
whole, with the occurrence count across the listed files asserted before
replacing. No AST byte-offset splicing; value maps use bare text, never
repr literals. Spanish target-language text is never a replacement target,
EXCEPT the explanation layer itself: notes, glosses, box titles, furniture
and the P8 E-section re-aiming (W43 ESxZH-TW KIT section 2 precedent: keys
137/138 re-aimed to ZH-TW, stems 139/140 re-aimed to ZH-TW, keys 139/140
byte-identical Spanish, apparatus key 150 per the same precedent).
Pure-form derivations, the P7 clinic's Spanish middle comments, the Ana
letter body + attribution stay byte-identical: frozen target text.
Furniture copied verbatim from shipped W43 ESxZH-TW
(files/weekly-report-es-zh-tw + its build dir), VOL.1 -> VOL.2 only.
Where the tools README #20 generic description and the W43 shipped
same-pairing edition differ, W43 shipped wins: here they agree (ES core
carries a native subtitle slot at y=372; the badge replaces it in place
at 19.5pt BRICK, per W43 ESxZH-TW KIT section 3).
Explanation strings are written in Taiwan usage throughout (連假 for the
puente, 範本 for the model text, 三房, 合約, 週 for week, 計畫, 螢幕-style
terms where they occur); each pair below was reviewed against the Spanish
it explains, not dumped from a raw converter.
On any COUNT MISMATCH: restore the build copy from
hidden_files/weekly-report-w45-es-build and re-run this script from scratch.
"""
import pathlib, sys

B = pathlib.Path('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-es-zh-tw-build')
FILES = ['content12.py', 'content34.py', 'content56.py', 'content7.py', 'content8.py', 'bslib4.py']

def rep(files, old, new, expect=None):
    total = 0
    for fn in files:
        p = B / fn
        t = p.read_text(encoding='utf-8')
        cnt = t.count(old)
        total += cnt
        if cnt:
            p.write_text(t.replace(old, new), encoding='utf-8')
    if expect is not None and total != expect:
        print(f'COUNT MISMATCH: {old!r} found {total}, expected {expect}'); sys.exit(1)
    return total

MAP = [
    ('1. El lunes 2: descanso y familia — o viaje, si tu comunidad hace puente（周一：休息陪家人；若你那里连休，就去旅行）', '1. El lunes 2: descanso y familia — o viaje, si tu comunidad hace puente（週一：休息陪家人；若你那裡連假，就去旅行）', 1),
    ('10 月 2 日议会否决两项住房法令', '10 月 2 日議會否決兩項住房法令', 1),
    ('10 月 5 日解散议会并召集大选', '10 月 5 日解散議會並召集大選', 1),
    ('11 月 2 日你那里放假吗？连休你做什么：旅行、休息还是看球？写两句西班牙语寄给编辑部。', '11 月 2 日你那裡放假嗎？連假你做什麼：旅行、休息還是看球？寫兩句西班牙語寄給編輯部。', 2),
    ('11 月 2 日周一', '11 月 2 日週一', 1),
    ('11 月 2 日周一九个自治区放假，其他地区照常上班。', '11 月 2 日週一九個自治區放假，其他地區照常上班。', 1),
    ('11 月 8 日周日', '11 月 8 日週日', 1),
    ('11 月 8 日周日，马德里有两场约会：15:30 的 NFL 和 21:00 的马竞对巴萨。', '11 月 8 日週日，馬德里有兩場約會：15:30 的 NFL 和 21:00 的馬競對巴薩。', 1),
    ('2. El sábado 7: Valencia–Real Madrid, 21:00, en Mestalla（周六晚：瓦伦西亚对皇马）', '2. El sábado 7: Valencia–Real Madrid, 21:00, en Mestalla（週六晚：瓦倫西亞對皇馬）', 1),
    ('27 — días faltan el lunes 2 para las elecciones del domingo 29（距 29 日大选 27 天）', '27 — días faltan el lunes 2 para las elecciones del domingo 29（距 29 日大選 27 天）', 1),
    ('29 日是周日', '29 日是週日', 1),
    ('3. El domingo 8, 15:30: la NFL en el Bernabéu（周日下午：NFL 马德里站）', '3. El domingo 8, 15:30: la NFL en el Bernabéu（週日下午：NFL 馬德里站）', 1),
    ('4. El domingo 8, 21:00: Atlético–Barça en el Metropolitano（周日晚：马竞对巴萨）', '4. El domingo 8, 21:00: Atlético–Barça en el Metropolitano（週日晚：馬競對巴薩）', 1),
    ('5. Y el lunes 9: vuelta a clase y al trabajo; la campaña empieza el viernes 13（返校返工；竞选 13 日开始）', '5. Y el lunes 9: vuelta a clase y al trabajo; la campaña empieza el viernes 13（返校返工；競選 13 日開始）', 1),
    ('55,7 — % que cita la vivienda como el principal problema, según el CIS de octubre（CIS 十月数据）', '55,7 — % que cita la vivienda como el principal problema, según el CIS de octubre（CIS 十月數據）', 1),
    ('9 — comunidades donde el lunes 2 de noviembre es fiesta（11 月 2 日放假的自治区）', '9 — comunidades donde el lunes 2 de noviembre es fiesta（11 月 2 日放假的自治區）', 1),
    ('A FONDO · 深读', 'A FONDO · 深讀', 1),
    ('A2 → B1 · La semana pasada: tres noches de otoño · 上周的三个秋夜', 'A2 → B1 · La semana pasada: tres noches de otoño · 上週的三個秋夜', 1),
    ('AHORA TÚ · 即学即练', 'AHORA TÚ · 即學即練', 1),
    ('Ana 只看 NFL；晚上看马竞–巴萨的是 Pablo', 'Ana 只看 NFL；晚上看馬競–巴薩的是 Pablo', 1),
    ('Aunque 后接陈述式（已知事实）', 'Aunque 後接陳述式（已知事實）', 1),
    ('BREVES · 快讯', 'BREVES · 快訊', 1),
    ('CADA SEMANA EN ESPAÑOL · 每周一期 · 读西班牙人正在读的西班牙语', 'CADA SEMANA EN ESPAÑOL · 每週一期 · 讀西班牙人正在讀的西班牙語', 1),
    ('CIS 十月调查：住房 55,7%', 'CIS 十月調查：住房 55,7%', 1),
    ('CIS 里 PP 22,2%', 'CIS 裡 PP 22,2%', 1),
    ('CIS 里 PSOE 第一（34%）', 'CIS 裡 PSOE 第一（34%）', 1),
    ('CULTURA · 文化', 'CULTURA · 文化', 1),
    ('Castanyada 吃 panellets', 'Castanyada 吃 panellets', 1),
    ('Castanyada 吃烤栗子、红薯和 panellets', 'Castanyada 吃烤栗子、紅薯和 panellets', 1),
    ('Castanyada 在加泰罗尼亚', 'Castanyada 在加泰羅尼亞', 1),
    ('DANA 纪念是 2024 年风暴两周年', 'DANA 紀念是 2024 年風暴兩週年', 1),
    ('DANA 纪念活动在 10 月 29 日周四', 'DANA 紀念活動在 10 月 29 日週四', 2),
    ('DEPORTE · 体育', 'DEPORTE · 體育', 1),
    ('Domingo 8 — NFL en el Bernabéu, 15:30; Atlético–Barça, 21:00（周日 NFL 马德里站＋马竞对巴萨）', 'Domingo 8 — NFL en el Bernabéu, 15:30; Atlético–Barça, 21:00（週日 NFL 馬德里站＋馬競對巴薩）', 1),
    ('EJERCICIOS Y RESPUESTAS · 练习与答案', 'EJERCICIOS Y RESPUESTAS · 練習與答案', 1),
    ('EJERCICIOS · 第 2 版练习', 'EJERCICIOS · 第 2 版練習', 1),
    ('EJERCICIOS · 第 3 版练习', 'EJERCICIOS · 第 3 版練習', 1),
    ('EJERCICIOS · 第 4 版练习', 'EJERCICIOS · 第 4 版練習', 1),
    ('EJERCICIOS · 第 5 版练习', 'EJERCICIOS · 第 5 版練習', 1),
    ('EJERCICIOS · 第 6 版练习', 'EJERCICIOS · 第 6 版練習', 1),
    ('EL CALENDARIO · 本周日历', 'EL CALENDARIO · 本週日曆', 1),
    ('EL PLAN DEL PUENTE · 连休计划', 'EL PLAN DEL PUENTE · 連假計畫', 1),
    ('EN ESTA EDICIÓN · 本期目录', 'EN ESTA EDICIÓN · 本期目錄', 1),
    ('ERRORES TÍPICOS · 常见错误', 'ERRORES TÍPICOS · 常見錯誤', 1),
    ('El Bernabéu ___ (原形 acoger) un partido de la NFL.', 'El Bernabéu ___ (原形 acoger) un partido de la NFL.', 1),
    ('FRASES DE LA SEMANA · 本周金句（逐字摘自本期文章）', 'FRASES DE LA SEMANA · 本週金句（逐字摘自本期文章）', 1),
    ('JUVENTUD · 青年', 'JUVENTUD · 青年', 1),
    ('Jueves 5 — Europa League: Real Sociedad–Lyon, 18:45（周四皇家社会欧联对里昂）', 'Jueves 5 — Europa League: Real Sociedad–Lyon, 18:45（週四皇家社會歐聯對里昂）', 1),
    ('LA NOTICIA · 头条', 'LA NOTICIA · 頭條', 1),
    ('LA PALABRA · 本周生词', 'LA PALABRA · 本週生詞', 1),
    ('LA PRÓXIMA SEMANA · 下期预告 (VOL.3)', 'LA PRÓXIMA SEMANA · 下期預告 (VOL.3)', 1),
    ('LA SEMANA EN CIFRAS · 数字看本周', 'LA SEMANA EN CIFRAS · 數字看本週', 1),
    ('LA SEMANA EUROPEA Y LA JORNADA 12 · 欧战周与联赛第 12 轮', 'LA SEMANA EUROPEA Y LA JORNADA 12 · 歐戰週與聯賽第 12 輪', 1),
    ('LENGUA · 语言', 'LENGUA · 語言', 1),
    ('LOS DÍAS DE LA SEMANA · 这样说日期', 'LOS DÍAS DE LA SEMANA · 這樣說日期', 1),
    ('Lunes 2 — puente en nueve comunidades; las candidaturas proclamadas llegan al BOE el martes 3（周一九地连休；周二《官方公报》公布正式候选名单）', 'Lunes 2 — puente en nueve comunidades; las candidaturas proclamadas llegan al BOE el martes 3（週一九地連假；週二《官方公報》公佈正式候選名單）', 1),
    ('Martes 3 — Champions: Barça–Aston Villa, Atlético–Bayern, Villarreal–PSG（周二欧冠三场西甲球队比赛）', 'Martes 3 — Champions: Barça–Aston Villa, Atlético–Bayern, Villarreal–PSG（週二歐冠三場西甲球隊比賽）', 1),
    ('Miércoles 4 — Champions: AEK–Real Madrid, 18:45（周三皇马客场对雅典 AEK）', 'Miércoles 4 — Champions: AEK–Real Madrid, 18:45（週三皇馬客場對雅典 AEK）', 1),
    ('NFL 马德里站周日 15:30', 'NFL 馬德里站週日 15:30', 1),
    ('NFL 马德里站周日 15:30 开球', 'NFL 馬德里站週日 15:30 開球', 1),
    ('NFL 马德里站周日下午', 'NFL 馬德里站週日下午', 1),
    ('NFL 马德里站是伯纳乌第二场 NFL 比赛', 'NFL 馬德里站是伯納烏第二場 NFL 比賽', 1),
    ('NIVEL A2 · El puente del lunes 2 · 11 月 2 日的连休', 'NIVEL A2 · El puente del lunes 2 · 11 月 2 日的連假', 1),
    ('NIVEL B1 · Europa primero, el domingo a las 21:00 · 欧战在先，周日晚九点', 'NIVEL B1 · Europa primero, el domingo a las 21:00 · 歐戰在先，週日晚九點', 1),
    ('NIVEL B1 · La NFL en Madrid · NFL 来到马德里', 'NIVEL B1 · La NFL en Madrid · NFL 來到馬德里', 1),
    ('NIVEL B2 · La vivienda decide la campaña · 住房决定选战', 'NIVEL B2 · La vivienda decide la campaña · 住房決定選戰', 1),
    ('QUIZ RELÁMPAGO · 闪电问答', 'QUIZ RELÁMPAGO · 閃電問答', 1),
    ('RESPUESTAS · 参考答案 — 按版面分页排列，找到题号即可', 'RESPUESTAS · 參考答案 — 按版面分頁排列，找到題號即可', 1),
    ('Samaín 是加利西亚古老节日', 'Samaín 是加利西亞古老節日', 1),
    ('Samaín 是加利西亚古节，不是万圣节译名', 'Samaín 是加利西亞古節，不是萬聖節譯名', 1),
    ('Sábado 7 — Valencia–Real Madrid, 21:00, en Mestalla（周六瓦伦西亚对皇马）', 'Sábado 7 — Valencia–Real Madrid, 21:00, en Mestalla（週六瓦倫西亞對皇馬）', 1),
    ('VIDA · 生活', 'VIDA · 生活', 1),
    ('Viernes 6 — Liga, jornada 12: Sevilla–Alavés, 21:00（周五联赛第 12 轮开球）', 'Viernes 6 — Liga, jornada 12: Sevilla–Alavés, 21:00（週五聯賽第 12 輪開球）', 1),
    ('a las nueve = 在九点', 'a las nueve = 在九點', 1),
    ('acoger = 承办', 'acoger = 承辦', 1),
    ('acoger = 承办（伯纳乌承办 NFL）', 'acoger = 承辦（伯納烏承辦 NFL）', 1),
    ('acoger 变位 → acoge', 'acoger 變位 → acoge', 1),
    ('actos de memoria 纪念活动', 'actos de memoria 紀念活動', 1),
    ('alquiler = 租金', 'alquiler = 租金', 1),
    ('anochecer=天黑 c', 'anochecer=天黑 c', 1),
    ('bueno 的比较级是 mejor', 'bueno 的比較級是 mejor', 1),
    ('bueno 的比较级是 mejor（不用 más）', 'bueno 的比較級是 mejor（不用 más）', 1),
    ('calabaza = 南瓜', 'calabaza = 南瓜', 1),
    ('castañas asadas 烤栗子', 'castañas asadas 烤栗子', 1),
    ('cementerio = 墓地', 'cementerio = 墓地', 1),
    ('comunidad=自治区 d', 'comunidad=自治區 d', 1),
    ('creo que + 陈述式 es', 'creo que + 陳述式 es', 1),
    ('creo que 表肯定，用陈述式 es。', 'creo que 表肯定，用陳述式 es。', 1),
    ('disfraz = 化装服装', 'disfraz = 化裝服裝', 2),
    ('el emparrillado = 美式足球场', 'el emparrillado = 美式足球場', 1),
    ('el emparrillado 美式足球场（烤架形场地） · el himno 国歌 · el touchdown 达阵得分 · la calabaza 南瓜。', 'el emparrillado 美式足球場（烤架形場地） · el himno 國歌 · el touchdown 達陣得分 · la calabaza 南瓜。', 1),
    ('el lunes 2 de noviembre 连休', 'el lunes 2 de noviembre 連假', 1),
    ('el lunes → es（单数）', 'el lunes → es（單數）', 1),
    ('es importante que + 虚拟式 sea', 'es importante que + 虛擬式 sea', 1),
    ('es necesario que + 虚拟式 baje', 'es necesario que + 虛擬式 baje', 1),
    ('es necesario que、para que、ojalá 后用虚拟式；creo que 后用陈述式。', 'es necesario que、para que、ojalá 後用虛擬式；creo que 後用陳述式。', 1),
    ('es posible que + 虚拟式 tenga', 'es posible que + 虛擬式 tenga', 1),
    ('estadio = 体育场', 'estadio = 體育場', 1),
    ('festivo 放假的 · el puente 连休 · la comunidad 自治区 · anochecer 天黑 · el horario de invierno 冬令时。', 'festivo 放假的 · el puente 連假 · la comunidad 自治區 · anochecer 天黑 · el horario de invierno 冬令時。', 1),
    ('festivo=放假的 a', 'festivo=放假的 a', 1),
    ('firmar = 签（合同）', 'firmar = 籤（合約）', 1),
    ('ganó 2–1 = 以 2–1 获胜', 'ganó 2–1 = 以 2–1 獲勝', 1),
    ('gente 是单数集合名词，动词用单数。', 'gente 是單數集合名詞，動詞用單數。', 1),
    ('himno = 国歌', 'himno = 國歌', 2),
    ('indecisos = 未决定者', 'indecisos = 未決定者', 1),
    ('ir 的过去时是 fueron', 'ir 的過去時是 fueron', 1),
    ('jornada=轮次 b', 'jornada=輪次 b', 1),
    ('junta electoral=选举委员会 a', 'junta electoral=選舉委員會 a', 1),
    ('la jornada 轮次 · recortar la distancia 缩小分差 · recibir 主场迎战 · visitar 客场挑战 · el Metropolitano 马竞主场。', 'la jornada 輪次 · recortar la distancia 縮小分差 · recibir 主場迎戰 · visitar 客場挑戰 · el Metropolitano 馬競主場。', 1),
    ('lunes 2 – domingo 8 de noviembre · 11 月 2 日周一至 8 日周日', 'lunes 2 – domingo 8 de noviembre · 11 月 2 日週一至 8 日週日', 1),
    ('lunes 是单数，动词用 es。', 'lunes 是單數，動詞用 es。', 1),
    ('malo 的比较级是 peor', 'malo 的比較級是 peor', 1),
    ('marcar dos goles = 进两球', 'marcar dos goles = 進兩球', 1),
    ('margen de error = 误差范围', 'margen de error = 誤差範圍', 1),
    ('margen de error=误差范围 b', 'margen de error=誤差範圍 b', 1),
    ('mejor 本身就是比较级，不加 más。', 'mejor 本身就是比較級，不加 más。', 1),
    ('muchísimos partidos 比赛很多', 'muchísimos partidos 比賽很多', 1),
    ('mudanza = 搬家', 'mudanza = 搬家', 1),
    ('muestra = 样本（5.025 人）', 'muestra = 樣本（5.025 人）', 1),
    ('muestra=样本 d', 'muestra=樣本 d', 1),
    ('más + cara（房价更高）', 'más + cara（房價更高）', 1),
    ('más + importante（马竞–巴萨更重要）', 'más + importante（馬競–巴薩更重要）', 1),
    ('más mejor 是错误说法', 'más mejor 是錯誤說法', 1),
    ('ojalá + 虚拟式：baje', 'ojalá + 虛擬式：baje', 1),
    ('para que + 虚拟式 sea', 'para que + 虛擬式 sea', 1),
    ('para que + 虚拟式（目的）', 'para que + 虛擬式（目的）', 1),
    ('precampaña = 竞选预热期：正式竞选前的几周。本期就是 precampaña；竞选 13 日周五开始。', 'precampaña = 競選預熱期：正式競選前的幾週。本期就是 precampaña；競選 13 日週五開始。', 2),
    ('primera derrota liguera = 联赛首败', 'primera derrota liguera = 聯賽首敗', 1),
    ('puente=三天连休 b', 'puente=三天連假 b', 1),
    ('recibir=主场迎战 a', 'recibir=主場迎戰 a', 1),
    ('recortar = 缩小分差', 'recortar = 縮小分差', 1),
    ('recortar=缩小分差 c', 'recortar=縮小分差 c', 1),
    ('sobrio 克制的 · el homenaje 纪念表彰 · el disfraz 服装（化装） · el boniato 红薯 · el cementerio 墓地。', 'sobrio 克制的 · el homenaje 紀念表彰 · el disfraz 服裝（化裝） · el boniato 紅薯 · el cementerio 墓地。', 1),
    ('sondeo = 民调', 'sondeo = 民調', 1),
    ('sondeo=民调 c', 'sondeo=民調 c', 1),
    ('tan + alta + como（同样高）', 'tan + alta + como（同樣高）', 1),
    ('tener que = 必须', 'tener que = 必須', 1),
    ('touchdown = 达阵得分', 'touchdown = 達陣得分', 1),
    ('tres habitaciones = 三居室', 'tres habitaciones = 三房', 1),
    ('va a + 原形', 'va a + 原形', 1),
    ('vamos a + 原形', 'vamos a + 原形', 1),
    ('van a + 原形', 'van a + 原形', 1),
    ('vas a + 原形', 'vas a + 原形', 1),
    ('visitar=客场挑战 d', 'visitar=客場挑戰 d', 1),
    ('¿Y TÚ? · 说说你自己', '¿Y TÚ? · 說說你自己', 4),
    ('¿cuánto cuesta? 多少钱', '¿cuánto cuesta? 多少錢', 1),
    ('“竞选预热期”：正式竞选前的几周。', '「競選預熱期」：正式競選前的幾週。', 1),
    ('一次民调就是一张带误差的照片，拍于某一天。', '一次民調就是一張帶誤差的照片，拍於某一天。', 1),
    ('万圣节之夜在周六 31 日', '萬聖節之夜在週六 31 日', 1),
    ('三个节日，同一个秋夜。', '三個節日，同一個秋夜。', 1),
    ('三夜之后周一有人连休有人上班', '三夜之後週一有人連假有人上班', 1),
    ('主语 + 动词 + 地点', '主語 + 動詞 + 地點', 1),
    ('九个自治区周一放假', '九個自治區週一放假', 1),
    ('五大看点，不编数字：全在本期里讲清。', '五大看點，不編數字：全在本期裡講清。', 1),
    ('伯纳乌承办一场 NFL 比赛。→ ___', '伯納烏承辦一場 NFL 比賽。→ ___', 1),
    ('伯纳乌把草皮换成烤架形球场：美式足球来到马德里。', '伯納烏把草皮換成烤架形球場：美式足球來到馬德里。', 1),
    ('住房是 55.7% 的西班牙人的首要问题。', '住房是 55.7% 的西班牙人的首要問題。', 1),
    ('住房是选战的决定性议题', '住房是選戰的決定性議題', 1),
    ('住房是首要问题（55,7%）', '住房是首要問題（55,7%）', 1),
    ('你最喜欢哪一夜：29 日、31 日还是 1 日？31 日你吃了什么？写两句寄来。', '你最喜歡哪一夜：29 日、31 日還是 1 日？31 日你吃了什麼？寫兩句寄來。', 2),
    ('你看过美式足球比赛吗？你更喜欢足球还是美式足球？写两句寄来。', '你看過美式足球比賽嗎？你更喜歡足球還是美式足球？寫兩句寄來。', 2),
    ('写作', '寫作', 3),
    ('写作题（无唯一答案）；范文（84 词）见下。', '寫作題（無唯一答案）；範本（84 詞）見下。', 1),
    ('冬令时第二周，天黑得早', '冬令時第二週，天黑得早', 1),
    ('判断', '判斷', 8),
    ('判断对错', '判斷對錯', 8),
    ('加泰罗尼亚周一是工作日', '加泰羅尼亞週一是工作日', 2),
    ('动词第二位', '動詞第二位', 1),
    ('单选', '單選', 47),
    ('句型转换', '句型轉換', 10),
    ('名单已提交：现在各党开始撰写纲领。', '名單已提交：現在各黨開始撰寫綱領。', 1),
    ('周一在九个自治区是假日。', '週一在九個自治區是假日。', 1),
    ('周一放假的自治区有 9 个', '週一放假的自治區有 9 個', 3),
    ('周二欧冠三场西甲球队比赛', '週二歐冠三場西甲球隊比賽', 1),
    ('周日 21:00 你看哪一场？马竞主场谁赢？写两句西班牙语寄来。', '週日 21:00 你看哪一場？馬競主場誰贏？寫兩句西班牙語寄來。', 2),
    ('周日 21:00 马竞–巴萨', '週日 21:00 馬競–巴薩', 1),
    ('周日上演马竞–巴萨', '週日上演馬競–巴薩', 1),
    ('周日下午还有 NFL 马德里站', '週日下午還有 NFL 馬德里站', 1),
    ('周日家属去墓地献花', '週日家屬去墓地獻花', 1),
    ('周日我们看 NFL 和马竞–巴萨。', '週日我們看 NFL 和馬競–巴薩。', 1),
    ('地点在前，动词第二', '地點在前，動詞第二', 1),
    ('填空', '填空', 42),
    ('大选在 11 月 29 日', '大選在 11 月 29 日', 3),
    ('大选在 11 月 29 日周日', '大選在 11 月 29 日週日', 1),
    ('姆巴佩进了两球', '姆巴佩進了兩球', 1),
    ('孟加拉虎对猎鹰', '孟加拉虎對獵鷹', 1),
    ('完形单选', '完形單選', 13),
    ('完成句子', '完成句子', 48),
    ('对照原文', '對照原文', 2),
    ('把句子改成过去时（pretérito indefinido）。', '把句子改成過去時（pretérito indefinido）。', 1),
    ('把词和释义配对', '把詞和釋義配對', 3),
    ('把词组成正确的句子。', '把詞組成正確的句子。', 1),
    ('改写', '改寫', 10),
    ('日期格式：el lunes 2 de noviembre；星期、月份小写；1 号说 el uno。', '日期格式：el lunes 2 de noviembre；星期、月份小寫；1 號說 el uno。', 1),
    ('时间在前', '時間在前', 1),
    ('时间在前，动词第二', '時間在前，動詞第二', 1),
    ('月份小写', '月份小寫', 1),
    ('月份小写：noviembre', '月份小寫：noviembre', 1),
    ('本周五大看点 · Para entender la semana', '本週五大看點 · Para entender la semana', 1),
    ('本报只刊登 CIS 这一组数据并注明来源日期', '本報只刊登 CIS 這一組數據並註明來源日期', 1),
    ('本期头条 · 详见第 2、6 版', '本期頭條 · 詳見第 2、6 版', 1),
    ('标题概括两地对比', '標題概括兩地對比', 1),
    ('每个图表都必须标明来源。→ ___', '每個圖表都必須標明來源。→ ___', 1),
    ('每月 1 号说 el uno', '每月 1 號說 el uno', 1),
    ('每题附一句中文简析 · 带 ✓ 的为范文题', '每題附一句中文簡析 · 帶 ✓ 的為範本題', 1),
    ('比较级 más…que、tan…como；bueno→mejor、malo→peor；绝不说 más mejor。', '比較級 más…que、tan…como；bueno→mejor、malo→peor；絕不說 más mejor。', 1),
    ('民调是带误差的具体某天的照片', '民調是帶誤差的具體某天的照片', 1),
    ('用 ir a + 原形动词改写句子，表示“将要”。', '用 ir a + 原形動詞改寫句子，表示「將要」。', 1),
    ('用括号里词的比较级或 -ísimo 形式填空。', '用括號裡詞的比較級或 -ísimo 形式填空。', 1),
    ('用方框里的词填空。', '用方框裡的詞填空。', 1),
    ('用方框里的词填空。注意：有的词要变位。', '用方框裡的詞填空。注意：有的詞要變位。', 1),
    ('用方框里的词填空：sondeo · muestra · indecisos · margen de error', '用方框裡的詞填空：sondeo · muestra · indecisos · margen de error', 1),
    ('用正确的日期形式补全句子。', '用正確的日期形式補全句子。', 1),
    ('疑问词在句首', '疑問詞在句首', 1),
    ('皇马 2–1 赢下国家德比', '皇馬 2–1 贏下國家德比', 1),
    ('皇马在诺坎普 2–1 获胜：这是巴萨本赛季联赛首败。', '皇馬在諾坎普 2–1 獲勝：這是巴薩本賽季聯賽首敗。', 1),
    ('看上面两张图，选出正确答案。', '看上面兩張圖，選出正確答案。', 1),
    ('竞选 11 月 13 日开始', '競選 11 月 13 日開始', 2),
    ('第 8 版 · La gran prueba de la semana + todas las respuestas', '第 8 版 · La gran prueba de la semana + todas las respuestas', 1),
    ('第 {n} 版 / 共 {total} 版', '第 {n} 版 / 共 {total} 版', 1),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', '答案見第 8 版 · 題目可跨級混排，按題號找答案', 5),
    ('给逝者带花 flores', '給逝者帶花 flores', 1),
    ('编辑部说明：截至本期截稿，未收到真实读者来信与第 8 版最佳作文，故本期登载编辑部示例信，承诺顺延至 VOL.3。欢迎来信！', '編輯部說明：截至本期截稿，未收到真實讀者來信與第 8 版最佳作文，故本期登載編輯部示例信，承諾順延至 VOL.3。歡迎來信！', 1),
    ('美国国歌由 Momsen 演唱，不是 Sáinz-Villegas', '美國國歌由 Momsen 演唱，不是 Sáinz-Villegas', 1),
    ('美式足球用手打、四次进攻', '美式足球用手打、四次進攻', 1),
    ('翻译', '翻譯', 8),
    ('范文见本版 H 区（84 词）', '範本見本版 H 區（84 詞）', 1),
    ('补全动词的现在时形式。', '補全動詞的現在時形式。', 1),
    ('西 班 牙 语 周 报 · VOL.2 · LA VIVIENDA · EL PUENTE · EL FÚTBOL', '西 班 牙 語 週 報 · VOL.2 · LA VIVIENDA · EL PUENTE · EL FÚTBOL', 1),
    ('西班牙国歌由吉他手演奏', '西班牙國歌由吉他手演奏', 1),
    ('讲解｜la cuenta atrás 倒计时 · disolver las Cortes 解散议会 · el decreto 法令 · la candidatura 候选人名单。', '譯注｜la cuenta atrás 倒數計時 · disolver las Cortes 解散議會 · el decreto 法令 · la candidatura 候選人名單。', 1),
    ('词汇配对', '詞彙配對', 3),
    ('译注｜', '譯註｜', 1),
    ('语言聚焦 · Tres niveles, tres herramientas · 三个级别，三件工具', '語言聚焦 · Tres niveles, tres herramientas · 三個級別，三件工具', 1),
    ('诸圣节 11 月 1 日', '諸聖節 11 月 1 日', 1),
    ('诸圣节 11 月 1 日落在周日', '諸聖節 11 月 1 日落在週日', 1),
    ('诸圣节在 11 月 1 日，不是 10 月 31 日', '諸聖節在 11 月 1 日，不是 10 月 31 日', 1),
    ('读头版，选出正确答案 · 答案见第 8 版', '讀頭版，選出正確答案 · 答案見第 8 版', 1),
    ('读第 2 版文章，选出正确答案。', '讀第 2 版文章，選出正確答案。', 1),
    ('读第 3 版文章，判断对错。', '讀第 3 版文章，判斷對錯。', 1),
    ('读第 4 版文章，选出正确答案。', '讀第 4 版文章，選出正確答案。', 1),
    ('读第 5 版文章，选出正确答案。', '讀第 5 版文章，選出正確答案。', 1),
    ('调查在 10 月 1–6 日进行', '調查在 10 月 1–6 日進行', 1),
    ('距大选还有 27 天 · 住房决定选战', '距大選還有 27 天 · 住房決定選戰', 1),
    ('选出正确答案。', '選出正確答案。', 1),
    ('造句', '造句', 14),
    ('间接疑问用 si', '間接疑問用 si', 1),
    ('首场 NFL 伯纳乌赛在 2025 年 11 月 16 日', '首場 NFL 伯納烏賽在 2025 年 11 月 16 日', 1),
    ('马德里在放假名单里', '馬德里在放假名單裡', 1),
    ('马竞–巴萨与 NFL 都在周日', '馬競–巴薩與 NFL 都在週日', 1),
    ('马竞–巴萨周日 21:00', '馬競–巴薩週日 21:00', 1),
    ('马竞–巴萨周日 21:00 开球', '馬競–巴薩週日 21:00 開球', 1),
    ('（开放题，范文如下）', '（開放題，範本如下）', 1),
]

# P8 head lines are furniture (W43 verbatim), not plain conversions: drop them
# from MAP so the furniture reps below see the originals.
MAP = [m for m in MAP if m[0] not in (
    'RESPUESTAS · 参考答案 — 按版面分页排列，找到题号即可',
    '每题附一句中文简析 · 带 ✓ 的为范文题')]

for old, new, expect in MAP:
    rep(FILES, '"' + old + '"', '"' + new + '"', expect)

# ---- furniture, verbatim from shipped W43 ESxZH-TW (VOL.1 -> VOL.2 only) ----
rep(['bslib4.py'],
    '"La Lucerna · 西班牙语周报 VOL.2 · LUCERNA SPANISH WEEKLY"',
    '"La Lucerna · 西班牙語週報 VOL.2 · 正文西班牙語 · 講解繁體中文"', 1)
# P1 badge: replaces the core subtitle line in its y=372 slot, in place.
rep(['content12.py'],
    'p.text(975, 372, "EL PERIÓDICO SEMANAL PARA APRENDER — LA VIDA REAL, EN ESPAÑOL, DESDE ESPAÑA", 19, "sans", False, GREY, anchor="middle")',
    'p.text(975, 372, "西班牙語正文 · 繁體中文講解 — 給繁體中文讀者的版本", 19.5, "sans", True, BRICK, anchor="middle")', 1)
# P8 head, W43 verbatim.
rep(['content8.py'],
    'p.text(MX, 1302, "RESPUESTAS · 参考答案 — 按版面分页排列，找到题号即可", 25, "sans", True, OLIVE)',
    'p.text(MX, 1302, "RESPUESTAS · 全部答案與簡析（第 1–8 版）", 25, "sans", True, OLIVE)', 1)
rep(['content8.py'],
    'p.text(RIGHT, 1302, "每题附一句中文简析 · 带 ✓ 的为范文题", 19.5, "sans", False, GREY, anchor="end")',
    'p.text(RIGHT, 1302, "每題附一句中文簡析 · 帶 ✓ 的為範本題", 19.5, "sans", False, GREY, anchor="end")', 1)
# P8 separator, W43 column form.
rep(['content8.py'], 'f"— PÁGINA {pg} —"', 'f"— 第 {pg} 版 —"', 1)
# Function rename (definition + 20 calls), W43 column form.
rep(['bslib4.py'], 'def bridge(self', 'def expl(self', 1)
rep(FILES, '.bridge(', '.expl(', 20)
# Operative-code comments with Chinese text, same conversion.
rep(['content7.py'],
    '# 盒高 = 绘制循环精确模拟（W43 回补修法：逐项模拟，不用平均行高）',
    '# 盒高 = 繪製循環精確模擬（W43 回補修法：逐項模擬，不用平均行高）', 1)
# svglib: TC face (W43 column four changes) + docstring + one comment character.
rep(['svglib.py'], '"""SVG weekly-paper builder: PIL-measured text layout + line-art illustrations."""',
    '"""SVG weekly builder: PIL-measured text layout + line-art illustrations."""', 1)
rep(['svglib.py'], 'def _sc_index(path):', 'def _tc_index(path):', 1)
rep(['svglib.py'], 'if f.getname()[0].endswith("SC"):', 'if f.getname()[0].endswith("TC"):', 1)
rep(['svglib.py'], '_IDX = {p: _sc_index(p) for p in (_SERIF, _SERIF_B, _SANS, _SANS_B)}',
    '_IDX = {p: _tc_index(p) for p in (_SERIF, _SERIF_B, _SANS, _SANS_B)}', 1)
rep(['svglib.py'], 'fam = family or ("Noto Serif CJK SC" if kind == "serif" else "Noto Sans CJK SC")',
    'fam = family or ("Noto Serif CJK TC" if kind == "serif" else "Noto Sans CJK TC")', 1)
rep(['svglib.py'], 'for 重阳.', 'for 重陽.', 1)
# Render filenames: native-code suffix, W45 fan-out sibling pattern.
rep(['render.py'], '"La-Lucerna-VOL2.pdf"', '"La-Lucerna-VOL2-ZH-TW.pdf"', 1)
rep(['render.py'], '"La-Lucerna-VOL2-web.pdf"', '"La-Lucerna-VOL2-ZH-TW-web.pdf"', 1)
print('TRANSFORM DONE')
