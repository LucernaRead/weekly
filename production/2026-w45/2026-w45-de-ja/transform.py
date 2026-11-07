# -*- coding: utf-8 -*-
"""DE x JA fan-out transform for W45 DE core build copy.
Rules: whole-line or exact-unique-literal replacements with count
assertions; value maps (types/instr) use bare text, never repr.
German body text is NEVER touched: every `old` below is a Chinese
explanation-layer string, a bilingual furniture string, or a generic
type/instr token. Run once from the build dir copy.
Furniture follows the shipped W43 DE x JA forms (KIT section 3),
VOL.2: badge 19.5pt BRICK at (975,372), footer, page line, gloss
prefix, P8 separator, half-width P8 note parens, 13.0/1.16 keys.
"""
import os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
LOG = []

def rep(fname, old, new, expect=None):
    p = os.path.join(BASE, fname)
    s = open(p, encoding="utf-8").read()
    n = s.count(old)
    if expect is not None:
        assert n == expect, f"{fname}: {old!r} count {n} != {expect}"
    else:
        assert n >= 1, f"{fname}: {old!r} not found"
    LOG.append(f"{fname}: {n}x {old!r} -> {new!r}")
    open(p, "w", encoding="utf-8").write(s.replace(old, new))

def rep_all(fname, pairs):
    for old, new in pairs:
        rep(fname, old, new)

# ---------- OUT repoint (1 per content file) ----------
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    rep(f, "weekly-report-w45-de-core", "weekly-report-w45-de-ja", 1)

# ---------- bslib4: furniture + gloss prefix (W43 DE x JA shipped forms, VOL.2) ----------
rep("bslib4.py",
    '"Die Lucerna · 德语周报 VOL.2 · LUCERNA GERMAN WEEKLY"',
    '"Die Lucerna · ドイツ語週刊 VOL.2 · 本文はドイツ語 · 解説は日本語"', 1)
rep("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"{n} ページ（全 {total} ページ）"', 1)
rep("bslib4.py", '"译注｜" + s', '"解説 — " + s', 1)

# ---------- shared furniture strings ----------
SHARED = [
    ("UND SIE? · 说说你自己", "UND SIE? · あなたは？"),
    ("FERIENWECHSEL · 假期交接", "FERIENWECHSEL · 休暇の交代"),
    ("答案见第 8 版 · 题目可跨级混排，按题号找答案",
     "答えは8ページ · レベルは混ざっています。番号で答えを探してください"),
    ("BEISPIELE · 例句", "BEISPIELE · 例文"),
]
for f in ["content12.py", "content34.py", "content56.py"]:
    for old, new in SHARED:
        p = os.path.join(BASE, f)
        if old in open(p, encoding="utf-8").read():
            rep(f, old, new)

# ================= content12 (P1 + P2) =================
C12 = [
    ("WÖCHENTLICH AUF DEUTSCH · 每周一期 · 读德国人正在读的德语",
     "WÖCHENTLICH AUF DEUTSCH · 毎週一号 · ドイツ人が読んでいるドイツ語を読む"),
    ("德 语 周 报 · VOL.2 · 足 球 周 · 油 价 · 护 理",
     "ド イ ツ 語 週 刊 · VOL.2 · サ ッ カ ー 週 間 · 燃 料 割 引 · 介 護"),
    # P1 subtitle slot -> W43 shipped JA badge, verbatim, 19.5pt bold BRICK
    ('p.text(975, 372, "DIE WOCHENZEITUNG FÜR LERNENDE — DAS ECHTE LEBEN, AUF DEUTSCH, AUS DEUTSCHLAND", 19, "sans", False, GREY, anchor="middle")',
     'p.text(975, 372, "ドイツ語テキスト · 日本語の解説 — 日本語読者のための版", 19.5, "sans", True, BRICK, anchor="middle")'),
    ("本周足球周 · 欧冠欧联德甲连轴转", "今週はサッカー週間"),
    ("详见第 4 版 · Seite 4", "詳しくは4ページ · Seite 4"),
    ("DIE TOPMELDUNG · 头条", "DIE TOPMELDUNG · トップニュース"),
    ("讲解｜die Englische Woche 一周双赛 · der Spieltag 比赛日 · empfangen 主场迎战 · die Bundesliga 德甲。",
     "解説 — die Englische Woche サッカー週間 · der Spieltag 試合日 · empfangen ホームで迎える · die Bundesliga ブンデスリーガ。"),
    ("DIE WOCHE IN ZAHLEN · 数字看本周", "DIE WOCHE IN ZAHLEN · 今週の数字"),
    ("9 — Spiele hat der 9. Spieltag der Bundesliga（德甲第 9 轮共 9 场比赛）",
     "9 — Spiele hat der 9. Spieltag der Bundesliga（第9節は9試合）"),
    ("6 — deutsche Teams spielen in Europa（6 支德国球队出战欧战）",
     "6 — deutsche Teams spielen in Europa（ドイツの6チームが欧州で戦う）"),
    ("14,04 — Cent pro Liter beträgt der Tankrabatt（每升油减税 14.04 欧分）",
     "14,04 — Cent pro Liter beträgt der Tankrabatt（1リットル14.04セント減税）"),
    ("JETZT ÜBEN · 即学即练", "JETZT ÜBEN · すぐ練習"),
    ("一周双赛", "サッカー週間"),
    ("多特主场迎战贝蒂斯", "ドルトムントがベティスを迎える"),
    ("欧联在周四", "ヨーロッパリーグは木曜"),
    ("周五汉堡–门兴开轮", "金曜ハンブルク–グラートバッハで開幕"),
    ("第 9 轮共 9 场", "第9節は9試合"),
    ("减税到 12 月 31 日", "減税は12月31日まで"),
    ("拜仁周二客战马竞", "バイエルンは火曜アトレティコとアウェーで対戦"),
    ("霍芬海姆欧联客战水晶宫", "ホッフェンハイムはヨーロッパリーグでクリスタル・パレスとアウェーで対戦"),
    ("本周大问题 · Die Fragen der Woche", "今週の大きな問い · Die Fragen der Woche"),
    ("德国本周最热议的五个问题。", "今週ドイツで最も話題の五つの問い。"),
    ("IN DIESER AUSGABE · 本期目录", "IN DIESER AUSGABE · 今号の内容"),
    ("油价减税（加油折扣）。详见第 2 版。", "燃料割引。詳しくは2ページ。"),
    ("KURZ & GUT · 快讯", "KURZ & GUT · ショートニュース"),
    ("BLITZQUIZ · 闪电问答", "BLITZQUIZ · クイッククイズ"),
    ("读头版，选出正确答案 · 答案见第 8 版", "1ページを読んで正しい答えを選ぼう · 答えは8ページ"),
    # P2
    ("LEBEN · 生活", "LEBEN · 暮らし"),
    ("LEVEL A2 · Tankrabatt, Stromsteuer & Pflege · 油价、电力税与护理",
     "LEVEL A2 · Tankrabatt, Stromsteuer & Pflege · 燃料割引、電気税と介護"),
    ("der Tankrabatt 油价减税 · die Zapfsäule 加油机 · die Energiesteuer 能源税 · die Mehrwertsteuer 增值税 · der Angehörige 亲属。",
     "der Tankrabatt 燃料割引 · die Zapfsäule 給油機 · die Energiesteuer エネルギー税 · die Mehrwertsteuer 付加価値税 · der Angehörige 家族。"),
    ("AN DER ZAPFSÄULE · 加油机旁", "AN DER ZAPFSÄULE · 給油所で"),
    ("你开车吗？你那里的油价是多少？写两句德语寄来。",
     "車を運転しますか。あなたの町のガソリンはいくらですか。二文送ってください。"),
    ("ZEW IN KÜRZE · ZEW 指数简讯", "ZEW IN KÜRZE · ZEW短信"),
    ("RECHNEN WIR MAL · 算一算", "RECHNEN WIR MAL · 計算してみよう"),
    ("Die Zahlen der Woche · 本周数字", "Die Zahlen der Woche · 今週の数字"),
    ("注意：减的是税，定价的是油站。出发前比比价。",
     "注意：下がるのは税金、値段を決めるのは給油所です。出かける前に値段を比べましょう。"),
    ("ÜBUNGEN · 第 2 版练习", "ÜBUNGEN · 2ページの練習"),
    ("看第 2 版文章，用数字填空。", "2ページの記事を読んで、数字で空所を埋めよう。"),
    ("每升减税 14.04 欧分", "1リットルあたり14.04セント減税"),
    ("50 升省约 8.35 欧元", "50リットルで約8.35ユーロ節約"),
    ("减税到 2026 年底", "減税は2026年末まで"),
    ("国家少收约 25 亿欧元", "国は約25億ユーロの税収を手放す"),
    ("加油机旁的实际降幅", "給油所での実際の値下げ幅"),
    ("改成 Perfekt 现在完成时。", "Perfekt（現在完了）に書きかえよう。"),
    ("beschließen → beschlossen", "beschließen → beschlossen"),
    ("fallen 用 sein", "fallen は sein を使う"),
    ("tanken → getankt", "tanken → getankt"),
    ("weitergeben 可分动词", "weitergeben は分離動詞"),
    ("ZEW 预期下降", "ZEW景気期待は低下"),
    ("读第 2 版文章，选出正确答案。", "2ページの記事を読んで、正しい答えを選ぼう。"),
    ("减的是能源税", "下がるのはエネルギー税"),
    ("油站定价", "給油所が値段を決める"),
    ("联盟党与社民党", "連合と社民党"),
    ("家属居家护理", "家族が家で介護する"),
    ("Tankrabatt=油价减税 b", "Tankrabatt = 燃料割引 b"),
    ("Zapfsäule=加油机 d", "Zapfsäule = 給油機 d"),
    ("Mehrwertsteuer=增值税 a", "Mehrwertsteuer = 付加価値税 a"),
    ("Angehörige=亲属 c", "Angehörige = 家族 c"),
]
rep_all("content12.py", C12)

# ================= content34 (P3 + P4) =================
C34 = [
    ("KULTUR · 文化", "KULTUR · 文化"),
    ("A2 → B1 · Ferienwechsel & Herbst · 假期交接与秋天",
     "A2 → B1 · Ferienwechsel & Herbst · 休暇の交代と秋"),
    ("der Ferienwechsel 假期交接 · die Schülerin 女学生 · der Ausflug 短途出游 · der Advent 将临期 · die Lesung 朗读会。",
     "der Ferienwechsel 休暇の交代 · die Schülerin 女子生徒 · der Ausflug 日帰り旅行 · der Advent 待降節 · die Lesung 朗読会。"),
    ("der Nebel — 雾", "der Nebel — 霧"),
    ("das Laub — 落叶", "das Laub — 落ち葉"),
    ("der Kürbis — 南瓜", "der Kürbis — かぼちゃ"),
    ("die Kerze — 蜡烛", "die Kerze — ろうそく"),
    ("der Spaziergang — 散步", "der Spaziergang — 散歩"),
    ("die Lesung — 朗读会", "die Lesung — 朗読会"),
    ("HERBSTWÖRTER · 秋天词汇", "HERBSTWÖRTER · 秋の単語"),
    ("秋天你比夏天读得多吗？你的床头现在放着哪本书？写两句德语寄来。",
     "秋は夏よりたくさん読みますか。枕元の本は何ですか。二文送ってください。"),
    ("DER TIPP · 编辑部建议", "DER TIPP · 編集部のヒント"),
    ("ÜBUNGEN · 第 3 版练习", "ÜBUNGEN · 3ページの練習"),
    ("读第 3 版文章，判断对错。", "3ページの記事を読んで、正誤を判断しよう。"),
    ("BW 周一起复课", "バーデン＝ヴュルテンベルクは月曜から再開"),
    ("巴伐利亚本周仍在放假", "バイエルンは今週まだ休暇中"),
    ("诸圣节 11 月 1 日", "諸聖人の日は11月1日"),
    ("10 月 31 日也是宗教改革日（九个州）", "10月31日は宗教改革の日でもある（九つの州）"),
    ("诸圣节商店关门", "諸聖人の日は店が閉まる"),
    ("用方框里的词填空。", "枠の中の単語で空所を埋めよう。"),
    ("假期交接", "休暇の交代"),
    ("去山区短途出游", "山への日帰り旅行"),
    ("图书馆的朗读会", "図書館での朗読会"),
    ("将临期在 11 月筹划", "待降節は11月に計画する"),
    ("湖面上的雾", "湖の上の霧"),
    ('e.bridge("选出正确答案。")', 'e.bridge("正しい答えを選ぼう。")'),
    ("BW 假期已结束", "バーデン＝ヴュルテンベルクの休暇は終わった"),
    ("安静的节日", "静かな祝日"),
    ("诸圣节扫墓", "諸聖人の日の墓参り"),
    ("白天短所以夜晚长", "日が短いので夜が長い"),
    ("把词组成正确的句子。", "単語を正しい文に並べよう。"),
    ("时间地点开头，动词第二位", "時間と場所が先、動詞は二番目"),
    ("数量时间状语，动词第二位", "時間の句が先、動詞は二番目"),
    ("主谓宾顺序", "主語・動詞・目的語の順"),
    ("bleiben + geschlossen", "bleiben + geschlossen"),
    # P4
    ("SPORT · 体育", "SPORT · スポーツ"),
    ("LEVEL B1 · Europapokal & Bundesliga · 欧战与德甲",
     "LEVEL B1 · Europapokal & Bundesliga · 欧州カップとブンデスリーガ"),
    ("die Englische Woche 一周双赛 · auswärts 客场 · empfangen 主场迎战 · der Favorit 夺冠热门 · eröffnen 揭开序幕。",
     "die Englische Woche サッカー週間 · auswärts アウェーで · empfangen ホームで迎える · der Favorit 優勝候補 · eröffnen 開幕する。"),
    ("本周你支持谁？周六焦点战谁赢？写两句德语寄给编辑部。",
     "今週は誰を応援しますか。土曜の試合は誰が勝ちますか。二文送ってください。"),
    ("DER 9. SPIELTAG · 第 9 轮赛程", "DER 9. SPIELTAG · 第9節の日程"),
    ("ÜBUNGEN · 第 4 版练习", "ÜBUNGEN · 4ページの練習"),
    ("读第 4 版文章，选出正确答案。", "4ページの記事を読んで、正しい答えを選ぼう。"),
    ("拜仁周二客战马竞", "バイエルンは火曜アトレティコとアウェーで対戦"),
    ("斯图加特 18:45 开球", "シュトゥットガルトは18:45キックオフ"),
    ("多特主场迎战贝蒂斯", "ドルトムントがベティスを迎える"),
    ("霍芬海姆欧联客战水晶宫", "ホッフェンハイムはヨーロッパリーグでクリスタル・パレスとアウェーで対戦"),
    ("周六焦点战斯图加特–不来梅", "土曜の注目試合はシュトゥットガルト–ブレーメン"),
    ("Englische Woche=一周双赛 a", "Englische Woche = サッカー週間 a"),
    ("auswärts=客场 b", "auswärts = アウェーで b"),
    ("Favorit=热门 c", "Favorit = 優勝候補 c"),
    ("eröffnen=揭开序幕 d", "eröffnen = 開幕する d"),
    ("用比较级完成句子（括号里是原级）。", "比較級で文を完成させよう（かっこ内は原級）。"),
    ("schwer → schwerer", "schwer → schwerer"),
    ("spät → später（19:30 最晚）", "spät → später（19:30が最も遅い）"),
    ("viel → mehr（球迷想要更多）", "viel → mehr（ファンはもっと見たい）"),
    ("früh → früher（18:45 早于 21:00）", "früh → früher（18:45は21:00より早い）"),
    ("看上面的赛程表，选出正确答案。", "上の日程表を見て、正しい答えを選ぼう。"),
    ("汉堡–门兴周五 20:30", "ハンブルク–グラートバッハは金曜20:30"),
    ("斯图加特–不来梅周六 18:30", "シュトゥットガルト–ブレーメンは土曜18:30"),
    ("霍芬海姆–沙尔克周日 19:30", "ホッフェンハイム–シャルケは日曜19:30"),
    ("弗赖堡–柏林联周日 17:30", "フライブルク–ウニオンは日曜17:30"),
    ("欧联周四霍芬海姆 18:45", "ヨーロッパリーグ木曜、ホッフェンハイムは18:45"),
]
rep_all("content34.py", C34)

# ================= content56 (P5 + P6) =================
C56 = [
    ("JUGEND · 青年", "JUGEND · 若者"),
    ("LEVEL B1 · Zurück in die Schule · 重返校园",
     "LEVEL B1 · Zurück in die Schule · 学校へ戻る"),
    ("der Pausenhof 课间操场 · die Klassenarbeit 课堂测验 · das Referat 课堂报告 · ausschlafen 睡懒觉 · die Probe 排练。",
     "der Pausenhof 休み時間の校庭 · die Klassenarbeit 授業内テスト · das Referat 授業での発表 · ausschlafen 朝寝坊する · die Probe 稽古。"),
    ("der Pausenhof — 课间操场", "der Pausenhof — 休み時間の校庭"),
    ("die Klassenarbeit — 课堂测验", "die Klassenarbeit — 授業内テスト"),
    ("das Referat — 课堂报告", "das Referat — 授業での発表"),
    ("der Rucksack — 书包", "der Rucksack — リュック"),
    ("ausschlafen — 睡懒觉", "ausschlafen — 朝寝坊する"),
    ("die Probe — 排练", "die Probe — 稽古"),
    ("SCHULWÖRTER · 校园词汇", "SCHULWÖRTER · 学校の単語"),
    ("你的学校假期后哪天开学？第一节是什么课？写两句德语寄来。",
     "あなたの学校は休暇明けいつ始まりましたか。最初の授業は何でしたか。ドイツ語で二文送ってください。"),
    ("DER WOCHENPLAN DER REDAKTION · 编辑部一周计划",
     "DER WOCHENPLAN DER REDAKTION · 編集部の一週間"),
    ("ÜBUNGEN · 第 5 版练习", "ÜBUNGEN · 5ページの練習"),
    ("读第 5 版文章，选出正确答案。", "5ページの記事を読んで、正しい答えを選ぼう。"),
    ("BW 11 月 2 日开学", "バーデン＝ヴュルテンベルクは11月2日に再開"),
    ("巴伐利亚假期未结束", "バイエルンの休暇はまだ終わっていない"),
    ("开学周有课堂测验", "新学期の週に授業内テストがある"),
    ("Referat = 课堂报告", "Referat = 授業での発表"),
    ("巴伐利亚学生周五可去球场", "バイエルンの生徒は金曜に競技場へ行ける"),
    ("课间操场上玩", "休み時間の校庭で遊ぶ"),
    ("数学课堂测验", "数学の授業内テスト"),
    ("报告要读三本书", "発表のために三冊読む"),
    ("假期可以睡懒觉", "休暇中は朝寝坊できる"),
    ("圣诞演出的第一次排练", "クリスマス劇の最初の稽古"),
    ("书包里有本子铅笔", "リュックの中にノートと鉛筆"),
    ("用 weil 连接两个句子（动词放句末）。", "weil で二つの文をつなげよう（動詞は文末へ）。"),
    ("weil 句动词置尾", "weil の文では動詞が文末へ"),
    ("ist 置尾", "ist が文末へ"),
    ("muss 置尾", "muss が文末へ"),
    ("liegen 置尾", "liegen が文末へ"),
    ("判断对错。", "正誤を判断しよう。"),
    ("BW 11 月 2 日复课", "バーデン＝ヴュルテンベルクは11月2日に再開"),
    ("全德假期并未都结束", "ドイツ全土で休暇が終わったわけではない"),
    ("开学周有测验与报告", "新学期の週にテストと発表がある"),
    # P6
    ("VERTIEFUNG · 深读", "VERTIEFUNG · 深読み"),
    ("LEVEL B2 · Pflege & Stromsteuer · 护理与电力税",
     "LEVEL B2 · Pflege & Stromsteuer · 介護と電気税"),
    ("der Angehörige 亲属 · die Pflegeversicherung 护理保险 · der Pflegedienst 护理服务机构 · die Stagnation 停滞 · der Aufschwung 复苏。",
     "der Angehörige 家族 · die Pflegeversicherung 介護保険 · der Pflegedienst 訪問介護サービス · die Stagnation 停滞 · der Aufschwung 回復。"),
    ("DIE ZAHLEN · 本周数字", "DIE ZAHLEN · 今週の数字"),
    ("护理：在家护理需要更多帮助——对此政界仍在争论。电力税：降多少尚未确定。两者都花钱，都关系到几乎每个家庭。",
     "介護：家での介護にもっと助けが必要です——政界ではまだ議論中です。電気税：どれだけ下がるかは未定です。どちらもお金がかかり、ほぼすべての家庭に関わります。"),
    ("PRO & CONTRA · 正方与反方 — die Argumente der Debatte",
     "PRO & CONTRA · 賛成と反対 — die Argumente der Debatte"),
    ("WER PFLEGT ZU HAUSE? · 谁在家护理？", "WER PFLEGT ZU HAUSE? · 家で介護するのは誰？"),
    # NOTE: bare chart labels are translated LAST (see end of C56): the
    # exercise notes below contain them as substrings.
    ("ÜBUNGSDATEN · 练习数据 — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage.（本图数字为编辑部练习示例，非真实调查。）",
     "ÜBUNGSDATEN · 練習データ — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage.（この図の数字は編集部の練習例であり、本物の調査ではありません。）"),
    ("ÜBUNGEN · 第 6 版练习", "ÜBUNGEN · 6ページの練習"),
    ("看上面的练习图表，选出正确答案。", "上の練習グラフを見て、正しい答えを選ぼう。"),
    ("68% 家属护理", "68% 家族の介護"),
    ("专业上门 20% 第二", "訪問介護 20% が第2位"),
    ("68+20=88", "68+20=88"),
    ("养老院 12% 最小", "介護施設 12% が最小"),
    ("养老院 12%", "介護施設 12%"),
    ("68+20+12=100", "68+20+12=100"),
    ("读第 6 版深读文章，选出正确答案。", "6ページの深読み記事を読んで、正しい答えを選ぼう。"),
    ("10 月 26 日节目讨论居家护理", "10月26日の番組は家での介護を議論した"),
    ("据 ARD《Hart aber fair》10 月 26 日节目，600 多万人需要护理",
     "ARD『Hart aber fair』10月26日の番組によれば、600万人以上が介護を必要としている"),
    ("家属居家护理", "家族が家で介護する"),
    ("据 ARD《Hart aber fair》10 月 26 日节目，约 1000 万人护理亲属",
     "ARD『Hart aber fair』10月26日の番組によれば、約1000万人が家族を介護している"),
    ("用括号里的形式填空。", "かっこ内の形で空所を埋めよう。"),
    ("被动：wird + Partizip II", "受動態：wird + Partizip II"),
    ("ob 引导间接疑问句", "ob が間接疑問文を導く"),
    ("steigen → steigt", "steigen → steigt"),
    ("sagen 过去时 sagte", "sagen の過去形 sagte"),
    ("用方框里的词填空。", "枠の中の単語で空所を埋めよう。"),
    ("护理保险出更多钱", "介護保険がもっとお金を出す"),
    ("亲属居家护理", "家族が家で介護する"),
    ("走出停滞", "停滞から抜け出す"),
    ("复苏尚未自我维持", "回復はまだ自立していない"),
    # Bare chart labels LAST: full exercise notes above contain them.
    ("家属护理", "家族の介護"),
    ("专业上门", "訪問介護"),
    ("住养老院", "介護施設"),
]
rep_all("content56.py", C56)

# ================= content7 (P7) =================
C7 = [
    ("SPRACHE · 语言", "SPRACHE · 言語"),
    ("BEISPIELE · 例句", "BEISPIELE · 例文"),
    ("A2 → B2 · Sätze der Woche & Fehlerklinik · 本周金句与纠错诊所",
     "A2 → B2 · Sätze der Woche & Fehlerklinik · 今週の文と間違いクリニック"),
    ("本版专攻语言：三节小课、本期金句（全部摘自本期文章原文）、纠错诊所和读者来信。",
     "このページは言語が専門です。三つの小さなレッスン、今週の文（すべて今号の記事原文からの引用）、間違いクリニック、読者の手紙があります。"),
    ("被动：wird + Partizip II", "受動態：wird + Partizip II"),
    ("复数：werden", "複数：werden"),
    ("werden + 原形表将来", "werden + 不定詞で未来を表す"),
    ("被动语态", "受動態"),
    ("spät → später（19:30 最晚）", "spät → später（19:30が最も遅い）"),
    ("weil 引导原因", "weil が理由を導く"),
    ("weil 句动词置尾", "weil の文では動詞が文末へ"),
    ("länger als = 比……更长", "länger als = ……より長い"),
    ("A. 比平时更长 · B. 和平时一样 · C. 比平时更短",
     "A. いつもより長い · B. いつもと同じ · C. いつもより短い"),
    ("ob 引导间接疑问", "ob が間接疑問を導く"),
    ("Es ist fraglich, ob ... = 是否还难说", "Es ist fraglich, ob ... = ……か疑わしい"),
    ("dass 句动词置尾", "dass の文では動詞が文末へ"),
    ("礼貌表达观点", "丁寧な意見の言い方"),
    ("14,04 Cent = 每升 14.04 欧分", "14,04 Cent = 1リットル14.04セント"),
    ("rund 8,35 Euro = 大约省 8.35 欧元", "rund 8,35 Euro = 約8.35ユーロ節約"),
    ("Es wird gespielt. = 比赛将进行（被动）", "Es wird gespielt. = 試合が行われる"),
    ("Meiner Meinung nach ... = 在我看来……", "Meiner Meinung nach = 私の意見では"),
    ("Ich finde, dass ... = 我觉得……", "Ich finde, dass = 私は……と思う"),
    ("Es ist fraglich, ob ... = 是否……还难说", "Es ist fraglich, ob = ……か疑わしい"),
    ("DER WERKZEUGKASTEN · 工具箱", "DER WERKZEUGKASTEN · 道具箱"),
    ("LESERBRIEFE · 读者来信", "LESERBRIEFE · 読者の手紙"),
    ("NOCH EIN WORT · 再学一词", "NOCH EIN WORT · もう一語"),
    ("«der Tankrabatt»（Seite 2）: die gesenkte Steuer auf Benzin und Diesel. 油价减税。",
     "«der Tankrabatt»（Seite 2）: die gesenkte Steuer auf Benzin und Diesel. 燃料割引。"),
    ("SÄTZE DER WOCHE · 本周金句", "SÄTZE DER WOCHE · 今週の文"),
    ("原文摘录，逐字引自本期文章 · 括号内为出处", "今号の記事からの一字一句の引用 · かっこ内は出典"),
    ("连续四个足球之夜，然后是整周末联赛。", "四夜連続のサッカー、そして週末いっぱいのリーグ戦。"),
    ("汽油和柴油的能源税每升降低 14.04 欧分。", "ガソリンとディーゼルのエネルギー税が1リットルあたり14.04セント下がります。"),
    ("加 50 升油，大约省 8.35 欧元。", "50リットル給油すると、約8.35ユーロ節約できます。"),
    ("秋假过后，学校又开学了。", "秋休みの後、学校がまた始まりました。"),
    ("白天短，夜晚长。", "日は短く、夜は長い。"),
    ("德国球队的两场艰难客场之战。", "ドイツのチームの二つの厳しいアウェー戦。"),
    ("德国经济正在缓慢走出停滞，但复苏还不能自我维持。",
     "ドイツ経済はゆっくりと停滞から抜け出しつつありますが、回復はまだ自立していません。"),
    ("缓慢向好——但不会自动变好。", "ゆっくりと上向いている——しかし、ひとりでに良くなるわけではありません。"),
    ("FEHLERKLINIK · 纠错诊所", "FEHLERKLINIK · 間違いクリニック"),
    ("学习者最常犯的四个错 · 先自己改，再看答案",
     "学習者が最もよくする四つの間違い · まず自分で直してから答えを見よう"),
    ("动词第二位：主语不在句首时，动词仍居第二。",
     "動詞第二位：主語が文頭になくても、動詞は二番目に置きます。"),
    ("halb acht = 七点半（acht 之前）。", "halb acht = 7時半（acht の30分前）。"),
    ("Perfekt 中 Partizip II 放句末。", "Perfekt では Partizip II を文末に置きます。"),
    ("ob 从句动词放句末。", "ob の従属文では動詞を文末に置きます。"),
    ("IN DER NÄCHSTEN AUSGABE · 下期预告 (VOL.3)", "IN DER NÄCHSTEN AUSGABE · 次号予告 (VOL.3)"),
]
rep_all("content7.py", C7)

# P7 readers box: German label/defer/reader/invite strings are FROZEN and
# stay untouched. The Chinese note becomes two Japanese paras: a facts
# note (editors' example; no real letters; no best page-8 writing; the
# promise carries to VOL.3) + an explicit imperative invitation with a
# publication promise. Mirrors the DE x EN structural edit.
p7 = open(os.path.join(BASE, "content7.py"), encoding="utf-8").read()
OLD_RH = ('rh = 62 + 30 + len(wrap(label, "sans", True, 20, CW - 44)) * 29 \\\n'
          '    + len(wrap(defer, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \\\n'
          '    + len(wrap(reader, "serif", False, 21, CW - 44)) * 30 + 8 \\\n'
          '    + len(wrap(invite, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \\\n'
          '    + len(wrap(chinese, "sans", False, 19.5, CW - 44)) * 28 + 40 + 16')
assert OLD_RH in p7, "core rh block not found"
NEW_RH = ('rh = 62 + 30 + len(wrap(label, "sans", True, 20, CW - 44)) * 29 \\\n'
          '    + len(wrap(defer, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \\\n'
          '    + len(wrap(reader, "serif", False, 21, CW - 44)) * 30 + 8 \\\n'
          '    + len(wrap(invite, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \\\n'
          '    + len(wrap(note_ja, "sans", False, 19.5, CW - 44)) * 28 + 8 \\\n'
          '    + len(wrap(invite_ja, "serif", False, 20.5, CW - 44)) * 29.5 + 40 + 32')
rep("content7.py", OLD_RH, NEW_RH, 1)
rep("content7.py",
    '# NOTE (fix1): the +16 corrects the readers-box formula\'s per-paragraph\n'
    '# transition undercount (each drawn para adds its size on top of the\n'
    '# formula\'s +8 gap); without it the last Chinese line was painted over by\n'
    '# the word box below (occlusion COVER flag on the first fix1 render).',
    '# NOTE (JA fan-out): 6 paras in the readers box (label, defer, reader,\n'
    '# invite, note_ja, invite_ja); trailing +32 follows the DE x EN final\n'
    '# form (core fix1 +16, plus +16 for the added sixth para).', 1)
rep("content7.py",
    'chinese = "编辑部示例，非真实来信：截稿时未收到真实来信或习作，见 VOL.3。请寄来您的习作，优秀者刊登于 VOL.3。"',
    'note_ja = "編集部の例です。本物のお便りも第8ページの最優秀作文も届きませんでした。"\n'
    'invite_ja = "お便りと第8ページの作文を送ってください！優秀作はVOL.3に掲載します。"', 1)
rep("content7.py",
    'p.para(ix + 22, yy3 + 19.5, chinese, 19.5, "sans", False, GREY, CW - 44, 1.42)',
    'yy3 = p.para(ix + 22, yy3 + 19.5, note_ja, 19.5, "sans", False, GREY, CW - 44, 1.42) + 8\n'
    'p.para(ix + 22, yy3 + 20.5, invite_ja, 20.5, "serif", False, INK, CW - 44, 1.42)', 1)

# ================= content8 (P8) =================
C8 = [
    ("ÜBUNGEN & ANTWORTEN · 练习与答案", "ÜBUNGEN & ANTWORTEN · 練習と答え"),
    ("SCHLUSSTEST · 综合评估 · Alle Antworten unten auf dieser Seite 答案在本版下方",
     "SCHLUSSTEST · 総合テスト · Alle Antworten unten auf dieser Seite — 答えはこのページの下にあります"),
    ("spielt（第三人称单数）", "spielt（3人称単数）"),
    ("beginnt（第三人称单数）", "beginnt（3人称単数）"),
    ("kauft（第三人称单数）", "kauft（3人称単数）"),
    ("schnitzt 雕刻南瓜", "schnitzt = かぼちゃを彫る"),
    ("schläft（第三人称单数）", "schläft（3人称単数）"),
    ("Tankrabatt 油价减税", "Tankrabatt = 燃料割引"),
    ("geht（第三人称单数）", "geht（3人称単数）"),
    ("erzählt（第三人称单数）", "erzählt（3人称単数）"),
    ("A · LÜCKENTEXT · 完形填空", "A · LÜCKENTEXT · 穴埋め"),
    ("选项：", "選択肢："),
    ("B · WISSENSFRAGEN · 综合问答", "B · WISSENSFRAGEN · 総合問題"),
    ("减税到 2026 年 12 月 31 日", "減税は2026年12月31日まで"),
    ("拜仁周二客战马竞", "バイエルンは火曜アトレティコとアウェーで対戦"),
    ("霍芬海姆欧联客战水晶宫", "ホッフェンハイムはヨーロッパリーグでクリスタル・パレスとアウェーで対戦"),
    ("BW 假期已结束", "バーデン＝ヴュルテンベルクの休暇は終わった"),
    ("ZEW 预期 28.1", "ZEW景気期待は28.1"),
    ("周五汉堡–门兴开轮", "金曜ハンブルク–グラートバッハで開幕"),
    ("10 月 26 日节目讨论居家护理", "10月26日の番組は家での介護を議論した"),
    ("诸圣节 11 月 1 日", "諸聖人の日は11月1日"),
    ("C · LESEVERSTEHEN · 阅读理解", "C · LESEVERSTEHEN · 読解"),
    ("halb acht = 7:30", "halb acht = 7:30"),
    ("周二看拜仁客战马竞", "火曜にバイエルンのアトレティコ戦を見る"),
    ("周六买南瓜", "土曜にかぼちゃを買う"),
    ("霍芬海姆–沙尔克周日 19:30", "ホッフェンハイム–シャルケは日曜19:30"),
    ("D · SÄTZE BAUEN · 造句", "D · SÄTZE BAUEN · 文作り"),
    ("时间状语，动词第二位", "時間の句が先、動詞は二番目"),
    ("主谓宾顺序", "主語・動詞・目的語の順"),
    ("时间状语开头，动词第二位", "時間の句が先、動詞は二番目"),
    ("地点开头，动词第二位", "場所が先、動詞は二番目"),
    ("E · ÜBERSETZEN · 翻译", "E · ÜBERSETZEN · 翻訳"),
    # E prompts: DE->JA direction marker (3x); keys re-aimed below.
    ("（译成中文）", "（日本語訳）"),
    # E keys 137-139: DE->JA re-aimed (keys change language by definition);
    # the 140 key stays German, only its prompt changes (below).
    ('"油价减税持续到十二月。"', '"燃料割引は12月まで続きます。"'),
    ('"我周二看足球。"', '"私は火曜にサッカーを見ます。"'),
    ('"学校又开学了。"', '"学校がまた始まりました。"'),
    ("laufen = 持续", "laufen = 続く"),
    ("schauen = 看", "schauen = 見る"),
    ("wieder begonnen = 又开始", "wieder begonnen = また始まった"),
    ("多睡一小时 = eine Stunde länger schlafen", "1時間長く寝る = eine Stunde länger schlafen"),
    ("F · WÖRTER PAAREN · 词汇配对", "F · WÖRTER PAAREN · 単語ペア"),
    ("Tankrabatt=油价减税 b", "Tankrabatt = 燃料割引 b"),
    ("Pflege=护理 d", "Pflege = 介護 d"),
    ("Advent=将临期 a", "Advent = 待降節 a"),
    ("Pausenhof=课间操场 c", "Pausenhof = 休み時間の校庭 c"),
    ("G · DIALOG · 对话补全", "G · DIALOG · 対話の補完"),
    ("schaust（第二人称单数）", "schaust（2人称単数）"),
    ("siehst（第二人称单数）", "siehst（2人称単数）"),
    ("kochen（第一人称复数）", "kochen（1人称複数）"),
    ("machst（第二人称单数）", "machst（2人称単数）"),
    ("gehe（第一人称单数）", "gehe（1人称単数）"),
    ("开放题 — 要点见写作框，范文在第 8 版写作框内",
     "自由作文 — ポイントは作文の枠、模範はこのページの作文枠の中"),
    ("按要点给分", "ポイントごとに採点"),
    ("H · SCHREIBEN · 写作", "H · SCHREIBEN · 作文"),
    ("用德语写 80–100 词：《我的足球周》。写清看哪几场比赛、和谁一起、看球时吃什么，并写一句关于油价减税或护理的话。",
     "ドイツ語で80–100語で書きましょう。『私のサッカー週間』。どの試合を見るか、誰と一緒に見るか、観戦中に何を食べるかを書き、燃料割引か介護について一文加えましょう。優秀な作文はVOL.3に掲載します。"),
    ("MUSTER · 范文（84 Wörter）", "MUSTER · 模範文（84 Wörter）"),
    ("ANTWORTEN · 全部答案与简析（第 1–8 版）", "ANTWORTEN · 全解答と解説（1–8ページ）"),
]
rep_all("content8.py", C8)
# E item 140: prompt becomes Japanese + (ドイツ語訳) marker; key stays German.
rep("content8.py", '"我周日多睡一小时。（译成德语）"',
    '"私は日曜に1時間長く寝ます。（ドイツ語訳）"', 1)
# ---------- generic value maps (bare text) ----------
TYPEMAP = [("完成句子", "文完成"), ("单选", "選択肢"),
           ("句型转换", "文の書き換え"), ("词汇配对", "単語ペア"),
           ("判断对错", "正誤判断"), ("完形填空", "穴埋め"),
           ("造句", "文作り"), ("对话补全", "対話の補完"),
           ("翻译", "翻訳"), ("写作", "作文")]
INSTRMAP = [('instr="填空"', 'instr="空所補充"'),
            ('instr="改写"', 'instr="書きかえ"'),
            ('instr="判断"', 'instr="正誤"'),
            ('instr="造句"', 'instr="文を作る"'),
            ('instr="翻译"', 'instr="翻訳"'),
            ('instr="把词和释义配对"', 'instr="語と意味を結ぶ"')]
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    for old, new in INSTRMAP + TYPEMAP:  # instr tokens first: TYPEMAP would corrupt instr="翻译"
        pth = os.path.join(BASE, f)
        n = open(pth, encoding="utf-8").read().count(old)
        if n == 0:
            LOG.append(f"{f}: 0x {old!r} (absent, skipped)")
        else:
            rep(f, old, new)
# P8 keys: W43 DE x JA shipped form — half-width parens, 13.0pt/1.16 keys,
# Japanese page separators.
rep("content8.py", 'kf.para(f"— 第 {pg} 版 —", 17, "sans", True, OLIVE, 1.28, 3)',
    'kf.para(f"— {pg} ページ —", 17, "sans", True, OLIVE, 1.28, 3)', 1)
rep("content8.py", 's += f"（{e[\'note\']}）"', 's += f" ({e[\'note\']})"', 1)
rep("content8.py", 'kf.para(" · ".join(parts), 14.5, "sans", False, INK, 1.3, 9)',
    'kf.para(" · ".join(parts), 13.0, "sans", False, INK, 1.16, 9)', 1)

print("\n".join(LOG))
print(f"TOTAL replacements: {len(LOG)}")
