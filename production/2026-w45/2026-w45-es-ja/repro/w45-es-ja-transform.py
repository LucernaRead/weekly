# -*- coding: utf-8 -*-
"""W45 ES x JA fan-out transform: Chinese explanation layer -> Japanese.
Applies exact-string / whole-line replacements to the build copy ONLY
(never the core build dir). Each replacement asserts its expected hit
count; the script aborts on any mismatch. Order matters: longer strings
before their substrings; type names before instr substrings that contain
them (e.g. 完形单选 before 单选, 判断对错 before 判断).
Furniture strings are verbatim from the shipped W43 ES x JA edition
(files/weekly-report-es-ja), VOL.1 -> VOL.2 only. Type/instr labels follow
the W43 ES x JA mapping 1:1. The canonical JA svglib (md5 d73e23b3...)
was copied whole into the build dir and is NOT touched by this script.
"""
import os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(BASE, "build")
cache = {}

def load(f):
    if f not in cache:
        cache[f] = open(os.path.join(BUILD, f), encoding="utf-8").read()
    return cache[f]

def r(f, old, new, n=1):
    s = load(f)
    c = s.count(old)
    assert c == n, f"{f}: {old!r} found {c} times, expected {n}"
    cache[f] = s.replace(old, new)

def save_all():
    for f, s in cache.items():
        open(os.path.join(BUILD, f), "w", encoding="utf-8").write(s)
    print("saved", sorted(cache))

# ---------- OUT repoint (core -> edition) ----------
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    r(f, "weekly-report-w45-es-core", "weekly-report-w45-es-ja")
r("render.py", "weekly-report-w45-es-core", "weekly-report-w45-es-ja")
r("render.py", "La-Lucerna-VOL2.pdf", "La-Lucerna-VOL2-JA.pdf")
r("render.py", "La-Lucerna-VOL2-web.pdf", "La-Lucerna-VOL2-JA-web.pdf")

# ---------- bslib4.py: furniture + bridge -> expl ----------
r("bslib4.py", '"La Lucerna · 西班牙语周报 VOL.2 · LUCERNA SPANISH WEEKLY"',
  '"La Lucerna · スペイン語週刊 VOL.2 · 本文はスペイン語 · 解説は日本語"')
r("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"{n} ページ（全 {total} ページ）"')
r("bslib4.py", '"译注｜" + s', '"解説 — " + s')
r("bslib4.py", "def bridge(", "def expl(")

# ---------- shared type / instr renames (W43 ES x JA mapping) ----------
def types(f, spec):
    for old, new, n in spec:
        r(f, old, new, n)

# content12: 完成句子16 单选8 词汇配对1 / 填空10 / 把词和释义配对1 / bridge4
types("content12.py", [
    ("完成句子", "文の完成", 16), ("单选", "選択問題", 8), ("词汇配对", "単語のペア", 1),
    ('instr="填空"', "instr=\"空所補充\"", 10),
    ('instr="把词和释义配对"', 'instr="語と意味を結ぶ"', 1),
    (".bridge(", ".expl(", 4),
])
# content34: 判断对错5 完成句子9 单选9 造句6(type+instr) 句型转换6 词汇配对1
# 填空9 判断5(instr, after 判断对错) 改写6 把词和释义配对1 / bridge7
# (bridge sentences containing 判断对错 / 选出正确答案。 first, so bare counts hold)
r("content34.py", "读第 3 版文章，判断对错。", "3ページの記事を読んで、正誤を判断してください。")
r("content34.py", "读第 4 版文章，选出正确答案。", "4ページの記事を読んで、正しい答えを選んでください。")
types("content34.py", [
    ("判断对错", "正誤判断", 5), ("完成句子", "文の完成", 9), ("单选", "選択問題", 9),
    ("造句", "文を作る", 6), ("句型转换", "文の書き換え", 6), ("词汇配对", "単語のペア", 1),
    ('instr="填空"', "instr=\"空所補充\"", 9), ('instr="判断"', 'instr="正誤"', 5),
    ('instr="改写"', 'instr="書きかえ"', 6),
    ('instr="把词和释义配对"', 'instr="語と意味を結ぶ"', 1),
    (".bridge(", ".expl(", 7),
])
# content56: 单选15 完成句子14 句型转换4 判断对错3 / 填空14 改写4 判断3 / bridge5
types("content56.py", [
    ("单选", "選択問題", 15), ("完成句子", "文の完成", 14), ("句型转换", "文の書き換え", 4),
    ("判断对错", "正誤判断", 3),
    ('instr="填空"', "instr=\"空所補充\"", 14), ('instr="改写"', 'instr="書きかえ"', 4),
    ('instr="判断"', 'instr="正誤"', 3),
    (".bridge(", ".expl(", 5),
])
# content7: 完成句子9 单选3 / 填空9 / bridge3
types("content7.py", [
    ("完成句子", "文の完成", 9), ("单选", "選択問題", 3),
    ('instr="填空"', "instr=\"空所補充\"", 9),
    (".bridge(", ".expl(", 3),
])
# content8: 完形单选13 (before 单选) 单选12 造句8(type+instr) 翻译8(type+instr)
# 写作2(type+instr) 词汇配对1 把词和释义配对1 / bridge1
# (writing bridge containing 写作 first, so the bare 写作 count holds)
r("content8.py", "写作题（无唯一答案）；范文（84 词）见下。", "作文問題（決まった答えはありません）。模範文（84語）は以下です。")
types("content8.py", [
    ("完形单选", "穴埋め選択", 13), ("单选", "選択問題", 12), ("造句", "文を作る", 8),
    ("翻译", "翻訳", 8), ("写作", "作文", 3), ("词汇配对", "単語のペア", 1),
    ('instr="把词和释义配对"', 'instr="語と意味を結ぶ"', 1),
    (".bridge(", ".expl(", 1),
])

# ---------- content12.py: P1 furniture + notes ----------
r("content12.py",
  'p.text(975, 92, "CADA SEMANA EN ESPAÑOL · 每周一期 · 读西班牙人正在读的西班牙语", 21, "sans", False, GREY, anchor="middle")',
  'p.text(975, 92, "CADA SEMANA EN ESPAÑOL · 毎週一号 · スペイン人が読んでいるスペイン語を読む", 21, "sans", False, GREY, anchor="middle")')
r("content12.py",
  'p.text(975, 330, "西 班 牙 语 周 报 · VOL.2 · LA VIVIENDA · EL PUENTE · EL FÚTBOL", 46, "serif", True, INK, anchor="middle")',
  'p.text(975, 330, "ス ペ イ ン 語 週 刊 · VOL.2 · LA VIVIENDA · EL PUENTE · EL FÚTBOL", 46, "serif", True, INK, anchor="middle")')
r("content12.py",
  'p.text(975, 372, "EL PERIÓDICO SEMANAL PARA APRENDER — LA VIDA REAL, EN ESPAÑOL, DESDE ESPAÑA", 19, "sans", False, GREY, anchor="middle")',
  'p.text(975, 372, "スペイン語テキスト · 日本語の解説 — 日本語読者のための版", 19.5, "sans", True, BRICK, anchor="middle")')
r("content12.py", "距大选还有 27 天 · 住房决定选战", "29-Nまであと27日 · 住宅が選挙戦を決める")
r("content12.py", "本期头条 · 详见第 2、6 版", "今号のトップ · 詳しくは2・6ページ")
r("content12.py", "LA NOTICIA · 头条", "LA NOTICIA · トップ記事")
r("content12.py",
  "讲解｜la cuenta atrás 倒计时 · disolver las Cortes 解散议会 · el decreto 法令 · la candidatura 候选人名单。",
  "解説 — la cuenta atrás カウントダウン · disolver las Cortes 議会を解散する · el decreto 政令 · la candidatura 候補者リスト。")
r("content12.py", "LA SEMANA EN CIFRAS · 数字看本周", "LA SEMANA EN CIFRAS · 今週の数字")
r("content12.py", "（距 29 日大选 27 天）", "（29日の選挙まで27日）")
r("content12.py", "（11 月 2 日放假的自治区）", "（11月2日に休みの自治州）")
r("content12.py", "（CIS 十月数据）", "（10月のCISデータ）")
r("content12.py", "AHORA TÚ · 即学即练", "AHORA TÚ · すぐ練習")
r("content12.py", "大选在 11 月 29 日周日", "選挙は11月29日（日）")
r("content12.py", "住房是选战的决定性议题", "住宅が選挙戦の決定的な争点")
r("content12.py", "周一放假的自治区有 9 个", "月曜に休みの自治州は9つ", 2)
r("content12.py", "马竞–巴萨周日 21:00 开球", "アトレティコ–バルサは日曜21:00キックオフ")
r("content12.py", "NFL 马德里站周日 15:30 开球", "NFLマドリード戦は日曜15:30キックオフ")
r("content12.py", "本周五大看点 · Para entender la semana", "五大見どころ · Para entender la semana")
r("content12.py", "五大看点，不编数字：全在本期里讲清。", "五大見どころ：数字は作らず今号で説明。")
r("content12.py", "EN ESTA EDICIÓN · 本期目录", "EN ESTA EDICIÓN · 今号の目次")
r("content12.py", "“竞选预热期”：正式竞选前的几周。", "「プレキャンペーン」：正式選挙戦の前数週間。")
r("content12.py", "BREVES · 快讯", "BREVES · 短報")
r("content12.py", "QUIZ RELÁMPAGO · 闪电问答", "QUIZ RELÁMPAGO · クイズ")
r("content12.py", "读头版，选出正确答案 · 答案见第 8 版", "トップ記事を読んで、正しい答えを選ぼう · 答えは8ページ")
r("content12.py", "大选在 11 月 29 日", "選挙は11月29日", 2)
r("content12.py", "NFL 马德里站周日下午", "NFLマドリード戦は日曜午後")
r("content12.py", "马竞–巴萨周日 21:00", "アトレティコ–バルサは日曜21:00")

# ---------- content12.py: P2 ----------
r("content12.py", 'p.band("VIDA · 生活"', 'p.band("VIDA · 暮らし"')
r("content12.py", "NIVEL A2 · El puente del lunes 2 · 11 月 2 日的连休", "NIVEL A2 · El puente del lunes 2 · 11月2日の連休")
r("content12.py", "EL CALENDARIO · 本周日历", "EL CALENDARIO · 今週のカレンダー")
r("content12.py", "（周一九地连休；周二《官方公报》公布正式候选名单）", "（月曜は9州で連休；火曜に官報で正式候補を発表）")
r("content12.py", "（周二欧冠三场西甲球队比赛）", "（火曜はCLでスペイン勢3試合）")
r("content12.py", "（周三皇马客场对雅典 AEK）", "（水曜はレアルがアテネでAEKと対戦）")
r("content12.py", "（周四皇家社会欧联对里昂）", "（木曜はレアル・ソシエダがELでリヨンと対戦）")
r("content12.py", "（周五联赛第 12 轮开球）", "（金曜はリーグ第12節が開幕）")
r("content12.py", "（周六瓦伦西亚对皇马）", "（土曜はバレンシア対レアル）")
r("content12.py", "（周日 NFL 马德里站＋马竞对巴萨）", "（日曜はNFLマドリード戦＋アトレティコ–バルサ）")
r("content12.py", "festivo 放假的 · el puente 连休 · la comunidad 自治区 · anochecer 天黑 · el horario de invierno 冬令时。",
  "festivo 休みの · el puente 連休 · la comunidad 自治州 · anochecer 日暮れ · el horario de invierno 冬時間。")
r("content12.py", "11 月 2 日你那里放假吗？连休你做什么：旅行、休息还是看球？写两句西班牙语寄给编辑部。",
  "11月2日、あなたの地域は休みですか？連休は何をしますか：旅行、休養、それともサッカー観戦？スペイン語で2文書いて編集部に送ってください。", 2)
r("content12.py", "¿Y TÚ? · 说说你自己", "¿Y TÚ? · あなたは？")
r("content12.py", "LOS DÍAS DE LA SEMANA · 这样说日期", "LOS DÍAS DE LA SEMANA · 日付の言い方")
r("content12.py", "lunes 2 – domingo 8 de noviembre · 11 月 2 日周一至 8 日周日", "lunes 2 – domingo 8 de noviembre · 11月2日（月）～8日（日）")
r("content12.py", "EJERCICIOS · 第 2 版练习", "EJERCICIOS · 2ページの練習")
r("content12.py", "答案见第 8 版 · 题目可跨级混排，按题号找答案", "答えは8ページ · レベル混合の問題もあります。番号で探してください")
r("content12.py", "用正确的日期形式补全句子。", "正しい日付の形で文を完成させてください。")
r("content12.py", "11 月 2 日周一", "11月2日（月）")
r("content12.py", "11 月 8 日周日", "11月8日（日）")
r("content12.py", "每月 1 号说 el uno", "毎月1日は el uno と言う")
r("content12.py", "月份小写", "月は小文字")
r("content12.py", "补全动词的现在时形式。", "動詞の現在形を補ってください。")
r("content12.py", "el lunes → es（单数）", "el lunes → es（単数）")
r("content12.py", "读第 2 版文章，选出正确答案。", "2ページの記事を読んで、正しい答えを選んでください。")
r("content12.py", "九个自治区周一放假", "月曜に休みの自治州は9つ")
r("content12.py", "诸圣节 11 月 1 日落在周日", "諸聖人の日11月1日は日曜")
r("content12.py", "加泰罗尼亚周一是工作日", "カタルーニャでは月曜は平日")
r("content12.py", "冬令时第二周，天黑得早", "冬時間2週目、日暮れが早い")
r("content12.py", "puente=三天连休 b", "puente=三日間の連休 b")
r("content12.py", "festivo=放假的 a", "festivo=休みの a")
r("content12.py", "anochecer=天黑 c", "anochecer=日暮れ c")
r("content12.py", "comunidad=自治区 d", "comunidad=自治州 d")

# ---------- content34.py: P3 ----------
r("content34.py", "A2 → B1 · La semana pasada: tres noches de otoño · 上周的三个秋夜",
  "A2 → B1 · La semana pasada: tres noches de otoño · 先週の秋の三夜")
r("content34.py", "sobrio 克制的 · el homenaje 纪念表彰 · el disfraz 服装（化装） · el boniato 红薯 · el cementerio 墓地。",
  "sobrio 控えめな · el homenaje 追悼の表彰 · el disfraz 仮装の衣装 · el boniato サツマイモ · el cementerio 墓地。")
r("content34.py", "你最喜欢哪一夜：29 日、31 日还是 1 日？31 日你吃了什么？写两句寄来。",
  "一番好きな夜はどれですか：29日、31日、それとも1日？31日は何を食べましたか？2文書いて送ってください。", 2)
r("content34.py", "¿Y TÚ? · 说说你自己", "¿Y TÚ? · あなたは？", 2)
r("content34.py", "EJERCICIOS · 第 3 版练习", "EJERCICIOS · 3ページの練習")
r("content34.py", "答案见第 8 版 · 题目可跨级混排，按题号找答案", "答えは8ページ · レベル混合の問題もあります。番号で探してください", 2)
r("content34.py", "DANA 纪念活动在 10 月 29 日周四", "DANA追悼行事は10月29日（木）")
r("content34.py", "Castanyada 吃烤栗子、红薯和 panellets", "Castanyadaでは焼き栗、サツマイモ、panelletsを食べる")
r("content34.py", "Samaín 是加利西亚古节，不是万圣节译名", "Samaínはガリシアの古い祭りで、ハロウィーンの訳名ではない")
r("content34.py", "诸圣节在 11 月 1 日，不是 10 月 31 日", "諸聖人の日は11月1日で、10月31日ではない")
r("content34.py", "周日家属去墓地献花", "日曜に家族が墓地へ花を供える")
r("content34.py", "用方框里的词填空。", "枠の中の語を使って空所を埋めてください。")
r("content34.py", "给逝者带花 flores", "故人に花を供える flores")
r("content34.py", "castañas asadas 烤栗子", "castañas asadas 焼き栗")
r("content34.py", "disfraz = 化装服装", "disfraz = 仮装の衣装")
r("content34.py", "actos de memoria 纪念活动", "actos de memoria 追悼行事")
r("content34.py", "选出正确答案。", "正しい答えを選んでください。")
r("content34.py", "DANA 纪念是 2024 年风暴两周年", "DANA追悼は2024年の嵐から2年")
r("content34.py", "Castanyada 在加泰罗尼亚", "Castanyadaはカタルーニャのもの")
r("content34.py", "Samaín 是加利西亚古老节日", "Samaínはガリシアの古い祭り")
r("content34.py", "三夜之后周一有人连休有人上班", "三夜のあとの月曜、連休の人も仕事の人もいる")
r("content34.py", "把词组成正确的句子。", "語を並べて正しい文を作ってください。")
r("content34.py", "动词第二位", "動詞は2番目")
r("content34.py", "时间在前，动词第二", "時間が前、動詞は2番目")
r("content34.py", "地点在前，动词第二", "場所が前、動詞は2番目")
r("content34.py", "间接疑问用 si", "間接疑問文には si を使う")

# ---------- content34.py: P4 ----------
r("content34.py", 'p.band("DEPORTE · 体育"', 'p.band("DEPORTE · スポーツ"')
r("content34.py", "NIVEL B1 · Europa primero, el domingo a las 21:00 · 欧战在先，周日晚九点",
  "NIVEL B1 · Europa primero, el domingo a las 21:00 · 欧州の試合が先、日曜21:00")
r("content34.py", "la jornada 轮次 · recortar la distancia 缩小分差 · recibir 主场迎战 · visitar 客场挑战 · el Metropolitano 马竞主场。",
  "la jornada 節 · recortar la distancia 点差を縮める · recibir ホームで迎える · visitar アウェーで戦う · el Metropolitano メトロポリターノ（アトレティコの本拠地）。")
r("content34.py", "周日 21:00 你看哪一场？马竞主场谁赢？写两句西班牙语寄来。",
  "日曜21:00、どちらの試合を見ますか？アトレティコのホームではどちらが勝ちますか？スペイン語で2文書いて送ってください。", 2)
r("content34.py", "LA SEMANA EUROPEA Y LA JORNADA 12 · 欧战周与联赛第 12 轮",
  "LA SEMANA EUROPEA Y LA JORNADA 12 · 欧州の試合週とリーグ第12節")
r("content34.py", "EJERCICIOS · 第 4 版练习", "EJERCICIOS · 4ページの練習")
r("content34.py", "皇马 2–1 赢下国家德比", "レアルが2–1でクラシコに勝利")
r("content34.py", "姆巴佩进了两球", "エムバペが2得点")
r("content34.py", "周二欧冠三场西甲球队比赛", "火曜はCLでスペイン勢3試合")
r("content34.py", "周日 21:00 马竞–巴萨", "日曜21:00はアトレティコ–バルサ")
r("content34.py", "周日下午还有 NFL 马德里站", "日曜午後にはNFLマドリード戦もある")
r("content34.py", "jornada=轮次 b", "jornada=節 b")
r("content34.py", "recibir=主场迎战 a", "recibir=ホームで迎える a")
r("content34.py", "visitar=客场挑战 d", "visitar=アウェーで戦う d")
r("content34.py", "recortar=缩小分差 c", "recortar=点差を縮める c")
r("content34.py", "用括号里词的比较级或 -ísimo 形式填空。", "括弧内の語の比較級または -ísimo の形で空所を埋めてください。")
r("content34.py", "más + importante（马竞–巴萨更重要）", "más + importante（アトレティコ–バルサのほうが重要）")
r("content34.py", "muchísimos partidos 比赛很多", "muchísimos partidos 試合がとても多い")
r("content34.py", "malo 的比较级是 peor", "malo の比較級は peor")
r("content34.py", "bueno 的比较级是 mejor", "bueno の比較級は mejor")
r("content34.py", "把句子改成过去时（pretérito indefinido）。", "文を過去形（pretérito indefinido）に変えてください。")
r("content34.py", "ir 的过去时是 fueron", "ir の過去形は fueron")

# ---------- content56.py: P5 ----------
r("content56.py", 'p.band("JUVENTUD · 青年"', 'p.band("JUVENTUD · 若者"')
r("content56.py", "NIVEL B1 · La NFL en Madrid · NFL 来到马德里", "NIVEL B1 · La NFL en Madrid · NFLがマドリードにやって来る")
r("content56.py", "EL PLAN DEL PUENTE · 连休计划", "EL PLAN DEL PUENTE · 連休の計画")
r("content56.py", "（周一：休息陪家人；若你那里连休，就去旅行）", "（月曜：休んで家族と過ごす；連休なら旅行へ）")
r("content56.py", "（周六晚：瓦伦西亚对皇马）", "（土曜夜：バレンシア対レアル）")
r("content56.py", "（周日下午：NFL 马德里站）", "（日曜午後：NFLマドリード戦）")
r("content56.py", "（周日晚：马竞对巴萨）", "（日曜夜：アトレティコ対バルサ）")
r("content56.py", "（返校返工；竞选 13 日开始）", "（学校・仕事へ戻る；選挙戦は13日に始まる）")
r("content56.py", "el emparrillado 美式足球场（烤架形场地） · el himno 国歌 · el touchdown 达阵得分 · la calabaza 南瓜。",
  "el emparrillado アメフト場（グリル形のフィールド） · el himno 国歌 · el touchdown タッチダウン · la calabaza カボチャ。")
r("content56.py", "你看过美式足球比赛吗？你更喜欢足球还是美式足球？写两句寄来。",
  "アメフトの試合を見たことがありますか？サッカーとアメフト、どちらが好きですか？2文書いて送ってください。", 2)
r("content56.py", "¿Y TÚ? · 说说你自己", "¿Y TÚ? · あなたは？")
r("content56.py", "EJERCICIOS · 第 5 版练习", "EJERCICIOS · 5ページの練習")
r("content56.py", "答案见第 8 版 · 题目可跨级混排，按题号找答案", "答えは8ページ · レベル混合の問題もあります。番号で探してください", 2)
r("content56.py", "读第 5 版文章，选出正确答案。", "5ページの記事を読んで、正しい答えを選んでください。")
r("content56.py", "NFL 马德里站周日 15:30", "NFLマドリード戦は日曜15:30")
r("content56.py", "孟加拉虎对猎鹰", "ベンガルズ対ファルコンズ")
r("content56.py", "西班牙国歌由吉他手演奏", "スペイン国歌はギターで演奏")
r("content56.py", "首场 NFL 伯纳乌赛在 2025 年 11 月 16 日", "ベルナベウ初のNFLは2025年11月16日")
r("content56.py", "美式足球用手打、四次进攻", "アメフトは手を使い、4回の攻撃がある")
r("content56.py", "用方框里的词填空。注意：有的词要变位。", "枠の中の語で空所を埋めてください。注意：活用する語もあります。")
r("content56.py", "estadio = 体育场", "estadio = スタジアム")
r("content56.py", "acoger 变位 → acoge", "acoger の活用 → acoge")
r("content56.py", "touchdown = 达阵得分", "touchdown = タッチダウン")
r("content56.py", "calabaza = 南瓜", "calabaza = カボチャ")
r("content56.py", "disfraz = 化装服装", "disfraz = 仮装の衣装")
r("content56.py", "用 ir a + 原形动词改写句子，表示“将要”。", "ir a + 原形の動詞で文を書きかえ、「これから〜する」を表してください。")
r("content56.py", "NFL 马德里站是伯纳乌第二场 NFL 比赛", "NFLマドリード戦はベルナベウ2回目のNFL")
r("content56.py", "美国国歌由 Momsen 演唱，不是 Sáinz-Villegas", "アメリカ国歌はMomsenが歌い、Sáinz-Villegasではない")
r("content56.py", "万圣节之夜在周六 31 日", "ハロウィーンの夜は土曜31日")

# ---------- content56.py: P6 ----------
r("content56.py", 'p.band("A FONDO · 深读"', 'p.band("A FONDO · 深掘り"')
r("content56.py", "NIVEL B2 · La vivienda decide la campaña · 住房决定选战", "NIVEL B2 · La vivienda decide la campaña · 住宅が選挙戦を決める")
r("content56.py", "EJERCICIOS · 第 6 版练习", "EJERCICIOS · 6ページの練習")
r("content56.py", "看上面两张图，选出正确答案。", "二つの図を見て、答えを選んでください。")
r("content56.py", "CIS 里 PSOE 第一（34%）", "CISではPSOEが1位（34%）")
r("content56.py", "CIS 里 PP 22,2%", "CISではPPが22,2%")
r("content56.py", "住房是首要问题（55,7%）", "住宅が最大の関心事（55,7%）")
r("content56.py", "调查在 10 月 1–6 日进行", "調査は10月1～6日に実施")
r("content56.py", "本报只刊登 CIS 这一组数据并注明来源日期", "本紙はCISのデータだけを載せ、出典と日付を明記する")
r("content56.py", "10 月 2 日议会否决两项住房法令", "10月2日に議会が住宅関連の政令2本を否決")
r("content56.py", "10 月 5 日解散议会并召集大选", "10月5日に議会を解散し総選挙を召集")
r("content56.py", "民调是带误差的具体某天的照片", "世論調査は誤差つきの、ある一日の写真")
r("content56.py", "竞选 11 月 13 日开始", "選挙戦は11月13日に始まる")
r("content56.py", "es posible que + 虚拟式 tenga", "es posible que + 接続法 tenga")
r("content56.py", "es importante que + 虚拟式 sea", "es importante que + 接続法 sea")
r("content56.py", "para que + 虚拟式（目的）", "para que + 接続法（目的）")
r("content56.py", "Aunque 后接陈述式（已知事实）", "Aunque の後は直説法（既知の事実）")
r("content56.py", "用方框里的词填空：sondeo · muestra · indecisos · margen de error",
  "枠の中の語で空所を埋めてください：sondeo · muestra · indecisos · margen de error")
r("content56.py", "sondeo = 民调", "sondeo = 世論調査")
r("content56.py", "muestra = 样本（5.025 人）", "muestra = 標本（5,025人）")
r("content56.py", "indecisos = 未决定者", "indecisos = 未定層")
r("content56.py", "margen de error = 误差范围", "margen de error = 誤差範囲")

# ---------- content7.py: P7 ----------
r("content7.py", 'p.band("LENGUA · 语言"', 'p.band("LENGUA · ことば"')
r("content7.py", "语言聚焦 · Tres niveles, tres herramientas · 三个级别，三件工具",
  "ことば特集 · Tres niveles, tres herramientas · 三つのレベル、三つの道具")
r("content7.py", "日期格式：el lunes 2 de noviembre；星期、月份小写；1 号说 el uno。",
  "日付の形：el lunes 2 de noviembre；曜日・月は小文字；1日は el uno と言う。")
r("content7.py", "el lunes 2 de noviembre 连休", "el lunes 2 de noviembre 連休")
r("content7.py", "29 日是周日", "29日は日曜")
r("content7.py", "月份小写：noviembre", "月は小文字：noviembre")
r("content7.py", "比较级 más…que、tan…como；bueno→mejor、malo→peor；绝不说 más mejor。",
  "比較級 más…que、tan…como；bueno→mejor、malo→peor；más mejor とは決して言わない。")
r("content7.py", "más + cara（房价更高）", "más + cara（住宅価格がより高い）")
r("content7.py", "tan + alta + como（同样高）", "tan + alta + como（同じくらい高い）")
r("content7.py", "bueno 的比较级是 mejor（不用 más）", "bueno の比較級は mejor（más は不要）")
r("content7.py", "más mejor 是错误说法", "más mejor は誤った言い方")
r("content7.py", "es necesario que、para que、ojalá 后用虚拟式；creo que 后用陈述式。",
  "es necesario que、para que、ojalá の後は接続法；creo que の後は直説法。")
r("content7.py", "es necesario que + 虚拟式 baje", "es necesario que + 接続法 baje")
r("content7.py", "para que + 虚拟式 sea", "para que + 接続法 sea")
r("content7.py", "creo que + 陈述式 es", "creo que + 直説法 es")
r("content7.py", "ojalá + 虚拟式：baje", "ojalá + 接続法：baje")
r("content7.py", "lunes 是单数，动词用 es。", "lunes は単数で、動詞は es。")
r("content7.py", "mejor 本身就是比较级，不加 más。", "mejor 自体が比較級で、más は不要。")
r("content7.py", "gente 是单数集合名词，动词用单数。", "gente は単数の集合名詞で、動詞も単数。")
r("content7.py", "creo que 表肯定，用陈述式 es。", "creo que は肯定を表し、直説法 es を使う。")
r("content7.py", "ERRORES TÍPICOS · 常见错误", "ERRORES TÍPICOS · よくある間違い")
r("content7.py", "precampaña = 竞选预热期：正式竞选前的几周。本期就是 precampaña；竞选 13 日周五开始。",
  "precampaña = プレキャンペーン：選挙戦前の数週間。今号は precampaña；選挙戦は13日（金）に始まる。", 2)
r("content7.py", "LA PALABRA · 本周生词", "LA PALABRA · 今週の単語")
r("content7.py", "编辑部说明：截至本期截稿，未收到真实读者来信与第 8 版最佳作文，故本期登载编辑部示例信，承诺顺延至 VOL.3。欢迎来信！",
  "編集部より：本物の手紙も最優秀作文も届かなかったため、見本の手紙を掲載します。約束はVOL.3へ。")
r("content7.py", "FRASES DE LA SEMANA · 本周金句（逐字摘自本期文章）", "FRASES DE LA SEMANA · 今週の文（今号の記事から一字一句そのまま）")
r("content7.py", "名单已提交：现在各党开始撰写纲领。", "リストは提出済み：今、各党は綱領を書き始めている。")
r("content7.py", "11 月 2 日周一九个自治区放假，其他地区照常上班。", "11月2日（月）は9つの自治州が休みで、ほかの地域は仕事の日。")
r("content7.py", "三个节日，同一个秋夜。", "三つの祭り、同じ秋の夜。")
r("content7.py", "皇马在诺坎普 2–1 获胜：这是巴萨本赛季联赛首败。", "レアルがカンプ・ノウで2–1の勝利：バルサの今季リーグ初黒星。")
r("content7.py", "伯纳乌把草皮换成烤架形球场：美式足球来到马德里。", "ベルナベウは芝をグリル形のフィールドに変える：アメフトがマドリードにやって来る。")
r("content7.py", "住房是 55.7% 的西班牙人的首要问题。", "住宅は55,7%のスペイン人にとって最大の関心事。")
r("content7.py", "一次民调就是一张带误差的照片，拍于某一天。", "世論調査とは、誤差つきの、ある一日の写真である。")
r("content7.py", "11 月 8 日周日，马德里有两场约会：15:30 的 NFL 和 21:00 的马竞对巴萨。",
  "11月8日（日）、マドリードには二つの約束がある：15:30のNFLと21:00のアトレティコ–バルサ。")
r("content7.py", "LA PRÓXIMA SEMANA · 下期预告 (VOL.3)", "LA PRÓXIMA SEMANA · 次号予告 (VOL.3)")

# ---------- content8.py: P8 ----------
r("content8.py", 'p.band("EJERCICIOS Y RESPUESTAS · 练习与答案"', 'p.band("EJERCICIOS Y RESPUESTAS · 練習と答え"')
r("content8.py", "第 8 版 · La gran prueba de la semana + todas las respuestas", "8ページ · La gran prueba de la semana + todas las respuestas")
r("content8.py", "ganó 2–1 = 以 2–1 获胜", "ganó 2–1 = 2–1で勝利")
r("content8.py", "marcar dos goles = 进两球", "marcar dos goles = 2得点する")
r("content8.py", "primera derrota liguera = 联赛首败", "primera derrota liguera = リーグ初黒星")
r("content8.py", "recortar = 缩小分差", "recortar = 点差を縮める")
r("content8.py", "acoger = 承办（伯纳乌承办 NFL）", "acoger = 開催する（ベルナベウでのNFL開催）")
r("content8.py", "el emparrillado = 美式足球场", "el emparrillado = アメフト場")
r("content8.py", "周日上演马竞–巴萨", "日曜はアトレティコ–バルサ戦")
r("content8.py", "周一放假的自治区有 9 个", "月曜に休みの自治州は9つ")
r("content8.py", "诸圣节 11 月 1 日", "諸聖人の日11月1日")
r("content8.py", "马竞–巴萨与 NFL 都在周日", "アトレティコ–バルサもNFLも日曜")
r("content8.py", "Castanyada 吃 panellets", "Castanyadaではpanelletsを食べる")
r("content8.py", "DANA 纪念活动在 10 月 29 日周四", "DANA追悼行事は10月29日（木）")
r("content8.py", "大选在 11 月 29 日", "選挙は11月29日")
r("content8.py", "CIS 十月调查：住房 55,7%", "CIS10月調査：住宅55,7%")
r("content8.py", "竞选 11 月 13 日开始", "選挙戦は11月13日に始まる")
r("content8.py", "马德里在放假名单里", "マドリードは休みのリストに入っている")
r("content8.py", "加泰罗尼亚周一是工作日", "カタルーニャでは月曜は平日")
r("content8.py", "Ana 只看 NFL；晚上看马竞–巴萨的是 Pablo", "AnaはNFLだけを見る；夜にアトレティコ–バルサを見るのはPablo")
r("content8.py", "标题概括两地对比", "見出しは二つの地域の対比をまとめる")
r("content8.py", "主语 + 动词 + 地点", "主語 + 動詞 + 場所")
r("content8.py", "时间在前", "時間が前")
r("content8.py", "a las nueve = 在九点", "a las nueve = 9時に")
r("content8.py", "疑问词在句首", "疑問詞は文頭に")
# translation items: ES->JA keys re-aimed (W43 #137/#138 pattern)
r("content8.py", "周一在九个自治区是假日。", "月曜日は9つの自治州で祝日です。")
r("content8.py", "周日我们看 NFL 和马竞–巴萨。", "日曜日はNFLとアトレティコ–バルサを見ます。")
r("content8.py", "对照原文", "原文を参照", 2)
# reverse items: JA stems re-aimed, Spanish keys frozen (W43 #139/#140 pattern)
r("content8.py", "伯纳乌承办一场 NFL 比赛。→ ___", "ベルナベウはNFLの試合を開催する。→ ___")
r("content8.py", "acoger = 承办", "acoger = 開催する")
r("content8.py", "每个图表都必须标明来源。→ ___", "どのグラフにも出典を明記しなければならない。→ ___")
r("content8.py", "tener que = 必须", "tener que = ～しなければならない")
r("content8.py", "sondeo=民调 c", "sondeo=世論調査 c")
r("content8.py", "muestra=样本 d", "muestra=標本 d")
r("content8.py", "margen de error=误差范围 b", "margen de error=誤差範囲 b")
r("content8.py", "junta electoral=选举委员会 a", "junta electoral=選挙管理委員会 a")
r("content8.py", "alquiler = 租金", "alquiler = 家賃")
r("content8.py", "tres habitaciones = 三居室", "tres habitaciones = 3部屋")
r("content8.py", "¿cuánto cuesta? 多少钱", "¿cuánto cuesta? いくらですか")
r("content8.py", "firmar = 签（合同）", "firmar = 署名する（契約に）")
r("content8.py", "mudanza = 搬家", "mudanza = 引っ越し")
r("content8.py", "（开放题，范文如下）", "（自由記述 — 模範文は以下）")
r("content8.py", "范文见本版 H 区（84 词）", "模範文はこのページの H 欄（84語）")
r("content8.py", "RESPUESTAS · 参考答案 — 按版面分页排列，找到题号即可", "RESPUESTAS · 全解答と解説（1–8ページ）")
r("content8.py", "每题附一句中文简析 · 带 ✓ 的为范文题", "各問に日本語の解説つき · ✓ は模範文のある問題")
r("content8.py", 'f"— PÁGINA {pg} —"', 'f"— {pg} ページ —"')

save_all()
print("transform OK")
