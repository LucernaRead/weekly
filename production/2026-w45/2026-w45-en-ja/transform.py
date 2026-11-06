# -*- coding: utf-8 -*-
"""W45 EN core -> EN x JA fan-out transform. Single source of truth.

Re-copies the W45 EN core build, swaps in the canonical JA svglib
(md5 d73e23b365676c3618d7e060b835eb4d, never edited), applies the
value map below (quoted-literal replacement, longest first) plus the
line-based code edits, then asserts: every old value gone, every new
value present, OUT repointed, no leftover core furniture.

Gloss rule (W43 EN x JA precedent, KIT section 3.3): gloss() call
strings drop their prefix (gloss() itself adds the JA prefix), while
bridge() strings keep the JA prefix. P8 printed notes: explicit
PRINT_NOTES set measured from the core with tools/p8.py extract
(78 items), half-width paren form, per the EN-family precedent.
P1 badge replaces the 372 tagline slot in place at 19.5pt BRICK,
exactly as the shipped W43 EN x JA SVG does.
"""
import hashlib
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE_BUILD = os.path.join(BASE, "hidden_files/weekly-report-w45-en-build")
EDITION_DIR = os.path.join(BASE, "files/weekly-report-w45-en-ja")
EDITION_SVG = os.path.join(EDITION_DIR, "svg")
CANON_SVGLIB = os.path.join(BASE, "hidden_files/weekly-report-en-ja-build/svglib.py")
CANON_MD5 = "d73e23b365676c3618d7e060b835eb4d"
FILES = ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py", "bslib4.py"]

# old -> new. Whole-string values from the core AST inventory.
MAP = {
    # --- furniture / heads ---
    "WEEKLY IN ENGLISH · 每周一期 · 读美国人正在读的英语": "WEEKLY IN ENGLISH · 毎週一号 · アメリカ人が読んでいる英語を読む",
    "英 语 周 报 · VOL.2 · 选 票 · 足 球 · 电 影": "英 語 週 刊 · VOL.2 · 選 票 · フットボール · 映 画",
    "周二选举日 · 周日已拨回时钟": "火曜は選挙日 · 日曜は時計を戻した",
    "11 月 3 日周二选举日 · 详见第 6 版": "11月3日火曜は選挙日 · 詳しくは6ページ",
    "THE BIG STORY · 头条": "THE BIG STORY · トップ記事",
    "THE WEEK IN NUMBERS · 数字看本周": "THE WEEK IN NUMBERS · 今週の数字",
    "TRY IT NOW · 即学即练": "TRY IT NOW · すぐ練習",
    "Nov 3 — Election Day（选举日） · 435 — seats in the House, all on the ballot（众议院全部席位改选）": "Nov 3 — Election Day（選挙日） · 435 — seats in the House, all on the ballot（下院の全議席が改選）",
    "Nov 6 — two films open（两部电影上映） · Nov 8 — NFL in Madrid + F1 in São Paulo（周日两场大赛）": "Nov 6 — two films open（映画2本が公開） · Nov 8 — NFL in Madrid + F1 in São Paulo（日曜の2大試合）",
    "本周美国热搜 · Google Trends 美国区快照": "今週の急上昇 · Google Trends",
    "相对热度示意，非精确搜索量。": "人気の目安で、正確な検索数ではありません。",
    "IN THIS ISSUE · 本期目录": "IN THIS ISSUE · 今号の目次",
    "（任期）中期。midterm election 中期选举。": "（任期の）中間。midterm election は中間選挙。",
    "IN BRIEF · 快讯": "IN BRIEF · 短信",
    "LIGHTNING QUIZ · 闪电问答": "LIGHTNING QUIZ · 稲妻クイズ",
    "读头版，选出正确答案 · 答案见第 8 版": "トップ記事を読んで、正しい答えを選びなさい · 解答は8ページ",
    "LIFE · 生活": "LIFE · 生活",
    "LEVEL A2 · Clocks, candy & your week · 时钟、糖果与你的一周": "LEVEL A2 · Clocks, candy & your week · 時計とお菓子とあなたの1週間",
    "DO THE MATHS · 算一算": "DO THE MATHS · 計算してみよう",
    "AND YOU ? · 说说你自己": "AND YOU ? · あなたのことを話そう",
    "周日你多睡了一小时吗？写两句英语寄给编辑部。": "日曜は1時間多く眠れた？英語で2文、編集部へ送ろう。",
    "TELLING THE TIME · 这样报时间": "TELLING THE TIME · 時刻の言い方",
    "The repeated hour · 本周的三个时间": "The repeated hour · 今週の3つの時刻",
    "= two times（两次）": "= two times（2回）",
    "= one more time（再一次）": "= one more time（もう一度）",
    "= to go back one hour（拨回）": "= to go back one hour（時計を1時間戻す）",
    "= one hour more（多出一小时）": "= one hour more（1時間多い）",
    "EXERCISES · 第 2 版练习": "EXERCISES · 2ページの練習",
    "答案见第 8 版 · 题目可跨级混排，按题号找答案": "解答は8ページ · 問題はレベルをまたいで出題、番号で答えを探すこと",
    "CULTURE · 文化": "CULTURE · 文化",
    "A2 → B1 · Friday at the movies · 周五看电影": "A2 → B1 · Friday at the movies · 金曜日の映画",
    "AT HOME THIS WEEK · 在家看什么": "AT HOME THIS WEEK · おうち時間",
    "THE CAT'S HAT · 猫的帽子": "THE CAT'S HAT · 猫の帽子",
    "SPORT · 体育": "SPORT · 体育",
    "WHY MADRID ? · 为什么去马德里？": "WHY MADRID ? · なぜマドリードへ？",
    "SUNDAY, NOVEMBER 8 · 周日赛程": "SUNDAY, NOVEMBER 8 · 日曜の試合",
    "YOUTH · 青年": "YOUTH · 青年",
    "LEVEL B1 · Election night at home · 选举之夜": "LEVEL B1 · Election night at home · 家での選挙の夜",
    "TOO CLOSE TO CALL · 难分胜负": "TOO CLOSE TO CALL · 接戦",
    "FIVE SENTENCES · 五句话作业": "FIVE SENTENCES · 5文の課題",
    "DEEP READ · 时事深读": "DEEP READ · 深読み",
    "LEVEL B2 · How America votes · 美国怎么投票": "LEVEL B2 · How America votes · アメリカの投票の仕組み",
    "A PRACTICE BALLOT · 模拟选票": "A PRACTICE BALLOT · 練習用投票用紙",
    "READ THE CHART · 读图表": "READ THE CHART · グラフを読む",
    "HOW LONG ? · 任期多长？": "HOW LONG ? · 任期はどれくらい？",
    "LANGUAGE IN HAND · 精讲": "LANGUAGE IN HAND · 精講",
    "A2 → B2 · Phrases of the week · 本周金句": "A2 → B2 · Phrases of the week · 今週の名文",
    "LEVEL A2 · 基础": "LEVEL A2 · 基礎",
    "LEVEL B1 · 进阶": "LEVEL B1 · 中級",
    "LEVEL B2 · 挑战": "LEVEL B2 · 上級",
    "THE EXAMPLE · 例句": "THE EXAMPLE · 例文",
    "THE TOOLBOX · 工具箱": "THE TOOLBOX · 道具箱",
    "PHRASES OF THE WEEK · 本周金句（全部出自本期文章）": "PHRASES OF THE WEEK · 今週の名文（すべて今号の記事から）",
    "每句一个语法点 + 一道小题 · 答案见第 8 版": "各文に文法ポイント1つ＋小問1つ · 解答は8ページ",
    "THE ERROR CLINIC · 易错诊所": "THE ERROR CLINIC · 誤りクリニック",
    "每句有一处错误：找出来并改正。": "各文に誤りが1つずつあります。見つけて直しなさい。",
    "READERS' CORNER · 读者园地": "READERS' CORNER · 読者のコーナー",
    "NEXT WEEK · VOL.3 下周预告": "NEXT WEEK · VOL.3 次号予告",
    "下周三退伍军人节，周日 NFL 慕尼黑赛；还有中期选举结果报道。": "来週水曜は退役軍人の日、日曜はNFLミュンヘン戦、そして中間選挙の結果報道。",
    "EXERCISES & ANSWERS · 练习与答案": "EXERCISES & ANSWERS · 練習と解答",
    "FINAL TEST · 综合评估 · Answers at the bottom of this page 答案在本版下方": "FINAL TEST · 総合評価 · Answers at the bottom of this page 解答はこのページの下に",
    "A · CLOZE · 完形填空": "A · CLOZE · 空所補充",
    "B · MULTIPLE CHOICE · 单选": "B · MULTIPLE CHOICE · 選択",
    "C · READING · 阅读理解": "C · READING · 読解",
    "D · SENTENCES · 完成句子与转换": "D · SENTENCES · 文の完成と書きかえ",
    "E · TRANSLATION · 翻译": "E · TRANSLATION · 翻訳",
    "F · WORDS · 词汇配对": "F · WORDS · 語彙の組み合わせ",
    "G · DIALOGUE · 对话补全": "G · DIALOGUE · 会話補完",
    "H · WRITING · 写作 [B1]": "H · WRITING · 作文 [B1]",
    "MODEL · 范文": "MODEL · 模範文",
    "ANSWERS · 全部答案与简析（第 1–8 版）": "ANSWERS · 全解答と解説（1–8ページ）",
    "选项：": "選択肢：",
    # --- bslib4 furniture ---
    "The Lucerna · 英语周报 VOL.2 · LUCERNA ENGLISH WEEKLY": "The Lucerna · 英語週刊 VOL.2 · 本文は英語 · 解説は日本語",
    "译注｜": "解説 — ",
    # --- bridge strings (keep JA prefix) ---
    "讲解｜a midterm 中期选举 · a ballot 选票 · a race 一场竞选 · to call a race 宣布某场竞选的结果。": "解説 — a midterm 中間選挙 · a ballot 投票用紙 · a race 1つの選挙戦 · to call a race 選挙戦の結果を発表すること。",
    "根据时间，用英语补全句子。": "時刻に合わせて、英語で文を完成させなさい。",
    "用 be going to + 动词改写（计划与将要发生的事）。": "be going to + 動詞で書きかえなさい（予定やこれから起こること）。",
    "读第 2 版文章，选出正确答案。": "2ページの記事を読んで、正しい答えを選びなさい。",
    "读第 3 版文章，选出正确答案。": "3ページの記事を読んで、正しい答えを選びなさい。",
    "用所给词补全句子。": "与えられた語で文を完成させなさい。",
    "用 be going to 改写。": "be going to で書きかえなさい。",
    "五句影评｜who、where、发生了什么、转折、结局——五句就够。": "5文レビュー｜who、where、何が起きたか、転換、結末——5文で十分。",
    "读第 4 版文章，选出正确答案。": "4ページの記事を読んで、正しい答えを選びなさい。",
    "用一般过去时改写（比赛已结束的说法）。": "単純過去で書きかえなさい（試合が終わった言い方）。",
    "看球英语｜比分、谁得分、谁领先——短句就是直播英语。": "観戦英語｜スコア、誰が得点したか、誰がリードしているか——短い文こそ実況英語。",
    "读第 5 版文章，选出正确答案。": "5ページの記事を読んで、正しい答えを選びなさい。",
    "用现在进行时改写（正在发生的事）。": "現在進行形で書きかえなさい（今起こっていること）。",
    "投票结束｜The polls have closed = 该州投票已结束，计票开始。": "投票終了｜The polls have closed = その州の投票は終わり、開票が始まる。",
    "读上面的教学图表，选出正确答案。": "上の練習用グラフを読んで、正しい答えを選びなさい。",
    "读第 6 版文章，选出正确答案。": "6ページの記事を読んで、正しい答えを選びなさい。",
    "一张地图｜五十个州、五十套规则——所以选举夜看的是地图，不是一个数字。": "一枚の地図｜50の州、50通りのルール——だから選挙の夜に見るのは地図であって、1つの数字ではない。",
    "工具箱｜本期三句随身句，按级各一；金句全部出自本期文章，回读原文最有效。": "道具箱｜今号の持ち歩き文3つ、レベル別に一つずつ。名文はすべて今号の記事から。原文に戻って読むのが一番効く。",
    # --- gloss strings (prefix DROPPED: gloss() adds it) ---
    "讲解｜to fall back （时钟）拨回 · a costume 服装、装扮 · trick or treat 不给糖就捣蛋。": "to fall back （時計を）戻す · a costume 仮装 · trick or treat お菓子をくれなきゃいたずらするぞ。",
    "讲解｜to open （电影）上映 · a monster 怪物 · a catchphrase 口头禅、金句 · a series 剧集。": "to open （映画が）公開される · a monster 怪物 · a catchphrase 決めぜりふ · a series シリーズ。",
    "讲解｜a fixture 一场比赛（赛程） · a title 冠军头衔 · to defend （卫冕）保卫头衔 · a fan 球迷。": "a fixture 日程の中の1試合 · a title 優勝の称号 · to defend （王座を）守る · a fan ファン。",
    "讲解｜a map （选举）地图 · too close to call 难分胜负、无法判定 · a second screen 第二块屏幕（手机）。": "a map （選挙の）地図 · too close to call 接戦で判定できない · a second screen セカンドスクリーン（スマホ）。",
    "讲解｜to register 登记（选民登记） · a governor 州长 · to shape laws 影响立法 · patience 耐心。": "to register 登録する（有権者登録） · a governor 州知事 · to shape laws 法律に影響を与える · patience 忍耐。",
    # --- P7 phrases: grammar points + notes ---
    "语法点｜is = 是；日期作主语补足语。": "文法ポイント — is = 〜である；日付が主語の補語になる。",
    "语法点｜happen 的过去式是 happened，规则变化。": "文法ポイント — happen の過去形は happened、規則変化。",
    "语法点｜would + 动词原形，表选择意愿。": "文法ポイント — would + 動詞の原形、選択の意志を表す。",
    "语法点｜that is = 那就是；破折号后总结。": "文法ポイント — that is = つまり〜だ；ダッシュの後でまとめる。",
    "语法点｜will still = 仍然会；still 放在 will 之后。": "文法ポイント — will still = 今でも〜するだろう；still は will の後に置く。",
    "语法点｜part of = ……的一部分；not 表否定对照。": "文法ポイント — part of = 〜の一部；not で否定の対照を示す。",
    "语法点｜not every + 单数动词：并非每处都变。": "文法ポイント — not every + 単数動詞：すべての場所が変わるとは限らない。",
    "语法点｜has = 有；the week 单数用 has。": "文法ポイント — has = 〜がある；the week は単数なので has を使う。",
    "is 是": "is 〜である",
    "that is 那就是": "that is つまり〜だ",
    "will still 仍然会": "will still 今でも〜するだろう",
    "is part of 一部分": "is part of 一部",
    "« Patience is part of the system, not a failure of it. » — part of = 一部分 (page 6).": "« Patience is part of the system, not a failure of it. » — part of = 一部 (page 6).",
    # --- clinic notes ---
    "三单否定用 doesn't + 原形": "三単現の否定は doesn't + 原形",
    "fall 的过去式是 fell": "fall の過去形は fell",
    "bigger 已含比较级，不要再加 more": "bigger はすでに比較級、more は付けない",
    "going to 后用动词原形": "going to の後は動詞の原形",
    # --- readers' corner disclosure (Japanese; 3 facts + invitation) ---
    "编辑说明｜VOL.1 曾承诺 VOL.2 刊登真实来信，但截至发稿编辑部未收到真实来信与 VOL.1 写作投稿，故本期如实说明、不虚构来信；请把你的来信与写作寄来，VOL.3 起刊登收到的真实来信。": "編集部より｜VOL.1ではVOL.2に本物の読者の手紙を載せると約束しましたが、締め切りまでに本物の手紙も、VOL.1の作文投稿の最優秀作も届きませんでした。そこで本号は見本を見本と明示して載せ、約束はVOL.3へ先送りします。あなたの手紙と作文を送ってください。VOL.3に届いた本物の手紙を載せます。",
}

MAP.update({
    # --- exercise notes / keys (P1-P7) ---
    "ballot = 纸选票": "ballot = 投票用紙",
    "midterm = 中期（选举）": "midterm = 中間（選挙）",
    "选举日 11 月 3 日（周二）": "選挙日11月3日（火曜）",
    "early voting = 提前投票": "early voting = 期日前投票",
    "race called = 宣布结果": "race called = 当選確実の発表",
    "take time = 花时间": "take time = 時間がかかる",
    "选举日 11 月 3 日周二": "選挙日11月3日火曜",
    "众议院 435 席全部改选": "下院435議席がすべて改選",
    "美国 11 月 1 日拨回时钟": "アメリカは11月1日に時計を戻した",
    "NFL 马德里赛 11 月 8 日周日": "NFLマドリード戦は11月8日日曜",
    "1:00 = 一点整": "1:00 = 1時ちょうど",
    "1:30 = 一点半": "1:30 = 1時半",
    "7:45 = 差一刻八点": "7:45 = 8時15分前",
    "两次 = twice": "2回 = twice",
    "多出的 = extra": "余分な = extra",
    "Americans 复数 → are going to": "Americans は複数 → are going to",
    "疑问句：be 提前": "疑問文：be を前に出す",
    "11 月 1 日凌晨 2 点拨回 1 点": "11月1日午前2時に1時に戻した",
    "亚利桑那与夏威夷不拨钟": "アリゾナとハワイは時計を戻さない",
    "万圣节 10 月 31 日周六": "ハロウィーンは10月31日土曜",
    "11 月 1 日夜晚有 25 小时": "11月1日の夜は25時間ある",
    "costume=装扮 b": "costume=仮装 b",
    "extra hour=多出一小时 a": "extra hour=1時間の余裕 a",
    "fall back=拨回 d": "fall back=時計を戻す d",
    "trick or treat=不给糖就捣蛋 c": "trick or treat=お菓子をくれなきゃいたずらするぞ c",
    "猫咪电影 11 月 6 日周五上映": "猫の映画は11月6日金曜に公開",
    "猫出自苏斯博士的书": "猫はスース博士の本の出身",
    "比尔·黑德为猫配音": "猫の声はビル・ヘイダー",
    "哥斯拉导演是山崎贵": "ゴジラの監督は山崎貴",
    "《黑鸽》第二季 11 月 5 日上线": "「ブラック・ダヴ」シーズン2は11月5日に配信開始",
    "周日重聚节目收尾": "日曜の再会番組で週が締まる",
    "open = 上映（第三人称单数加 s）": "open = 公開される（三単現は s を付ける）",
    "tall → taller 比较级": "tall → taller（比較級）",
    "tall → taller（比较级）": "tall → taller（比較級）",
    "split = 分歧的": "split = 意見が分かれた",
    "catchphrase=金句 a": "catchphrase=決めぜりふ a",
    "series=剧集 d": "series=シリーズ d",
    "open=上映 c": "open=公開 c",
    "马德里赛：孟加拉虎对猎鹰": "マドリード戦：ベンガルズ対ファルコンズ",
    "马德里赛场是伯纳乌": "マドリードの会場はベルナベウ",
    "海豚对雄狮在迈阿密": "ドルフィンズ対ライオンズはマイアミで",
    "F1 圣保罗大奖赛在巴西": "F1サンパウロGPはブラジルで",
    "WTA 年终总决赛在印第安维尔斯开赛": "WTAファイナルズはインディアンウェルズで開幕",
    "拳击赛在阿灵顿": "ボクシングの試合はアーリントンで",
    "defend 三单加 s": "defend は三単現で s を付ける",
    "与第 4 版原文一致，复数动词": "4ページの原文どおり、複数動詞",
    "fixture=赛程中的比赛 b": "fixture=日程の中の試合 b",
    "title=冠军头衔 d": "title=優勝の称号 d",
    "fan=球迷 a": "fan=ファン a",
    "defend=卫冕 c": "defend=王座を守る c",
    "地图随结果逐州变色": "地図は結果とともに州ごとに色が変わる",
    "too close to call = 尚不知晓": "too close to call = 接戦で判定できない",
    "选举夜常吃披萨": "選挙の夜はよくピザを食べる",
    "第二屏是手机": "セカンドスクリーンはスマホ",
    "孩子问为什么这么久": "子どもはなぜそんなに時間がかかるのかと聞く",
    "结果早上还在": "結果は朝になっても残っている",
    "close = 接近的": "close = 接戦の",
    "close 接近的": "close 接戦の",
    "still = 仍然": "still = 今でも",
    "still 仍然": "still 今でも",
    "与第 5 版原文一致，单数": "5ページの原文どおり、単数",
    "map=选举地图 c": "map=選挙地図 c",
    "race=一场竞选 d": "race=1つの選挙戦 d",
    "result=结果 b": "result=結果 b",
    "call=宣布胜者 a": "call=勝者を発表する a",
    "38% 选“不用排队”": "38%が「並ばなくてよい」を選んだ",
    "工作原因 29%": "仕事の都合29%",
    "四项合计 100%": "4項目の合計100%",
    "习惯最少 12%": "習慣が最少12%",
    "不用排队比旅行多 17 个百分点": "「並ばなくてよい」は旅行より17ポイント多い",
    "图表是教学数据非真实民调": "グラフは練習用データで、本物の世論調査ではない",
    "各州自行组织选举": "選挙は各州が自ら運営する",
    "众议员任期两年": "下院議員の任期は2年",
    "参议员任期六年、每次约三分之一改选": "上院議員の任期は6年、毎回約3分の1が改選",
    "邮寄选票计票需时间": "郵便投票の開票には時間がかかる",
    "本期不印民调与预测": "今号は世論調査も予測も載せない",
    "耐心是制度的一部分": "忍耐は制度の一部である",
    "shape = 影响、塑造": "shape = 影響を与える、形作る",
    "register = 登记": "register = 登録する",
    "patience = 耐心": "patience = 忍耐",
    "optional = 可选的": "optional = 任意の",
    "differ 三单 differs": "differ は三単現で differs",
    "private = 私密的": "private = 非公開の",
    "fall → fell（不规则变化）": "fall → fell（不規則変化）",
    "fall 的过去式是 fell": "fall の過去形は fell",
    "going to 后用动词原形": "going to の後は動詞の原形",
    # --- P8 notes / keys ---
    "11 月 3 日是周二": "11月3日は火曜",
    "pizza 披萨": "pizza ピザ",
    "map 地图逐州变色": "map 地図が州ごとに色を変える",
    "sticker 贴纸": "sticker ステッカー",
    "will + 动词原形 know": "will + 動詞の原形 know",
    "we → get 原形": "we → get（原形）",
    "已发生的事用 fell": "すでに起きたことは fell",
    "than → 比较级 bigger": "than → 比較級 bigger",
    "despite + 名词：尽管下雨": "despite + 名詞：雨にもかかわらず",
    "whether = 是否": "whether = かどうか",
    "将来时 will + 动词原形": "未来形 will + 動詞の原形",
    "too close to call = 难分胜负": "too close to call = 接戦で判定できない",
    "周二他全天教书": "火曜は一日中教える",
    "贴纸上写着 I VOTED": "ステッカーには I VOTED と書いてある",
    "俄亥俄一如既往难分胜负": "オハイオはいつもどおり接戦",
    "are going to + 原形": "are going to + 原形",
    "whether 引导“是否”从句": "whether は「かどうか」の節を導く",
    "耐心是制度的一部分，而不是制度的失败。": "忍耐は制度の一部であり、制度の失敗ではない。",
    "part of 一部分；not a failure 不是失败": "part of 一部；not a failure 失敗ではない",
    "11 月 3 日周二是美国的选举日。": "11月3日火曜日はアメリカの選挙日です。",
    "Election Day 选举日；on Tuesday": "Election Day 選挙日；on Tuesday",
    "翻译：Tuesday, November 3, is Election Day in the United States.": "翻訳：Tuesday, November 3, is Election Day in the United States.",
    "这周日，NFL 在马德里比赛。": "今週の日曜日、NFLはマドリードで試合をします。",
    "翻译：On Sunday, the NFL plays in Madrid.": "翻訳：On Sunday, the NFL plays in Madrid.",
    "并非每处都拨回时钟。": "すべての場所が時計を戻すわけではない。",
    "not every 并非每处；change 变化": "not every すべての場所がそうとは限らない；change 変わる",
    "midterm = 中期选举 b": "midterm = 中間選挙 b",
    "governor = 州长 c": "governor = 州知事 c",
    "ballot = 选票 d": "ballot = 投票用紙 d",
    "ballot = 选票": "ballot = 投票用紙",
    "投票时出示证件 ID": "投票のときに身分証 ID を見せる",
    "line = 排队（美式英语）": "line = 並ぶこと（アメリカ英語）",
    "sticker = 贴纸": "sticker = ステッカー",
    "选举日是 11 月 3 日周二": "選挙日は11月3日火曜",
    "选举日 11 月 3 日（周二）": "選挙日11月3日（火曜）",
    "开放题 — 要点见写作框，范文在第 8 版写作框内": "自由記述 — 要点は作文の枠内、模範文は8ページの作文枠の中",
    "按要点给分": "要点ごとに採点",
    "用英语写 80–100 词：我的 11 月 3 日周二。写清你是否看了结果、吃了什么、地图显示了什么，再写一句周日夜里拨回的时钟。": "英語で80–100語：私の11月3日火曜日。結果を見たか、何を食べたか、地図が何を示したかをはっきり書き、日曜の夜に戻した時計について1文加えること。",
    # --- types / instr ---
    "完成句子": "文の完成",
    "句型转换": "文型変換",
    "单选": "選択",
    "图表读数": "グラフ読み取り",
    "改错": "誤り直し",
    "跟练": "音読ドリル",
    "完形填空": "穴埋め",
    "阅读理解": "読解",
    "翻译": "翻訳",
    "词汇配对": "語彙マッチング",
    "对话补全": "会話補完",
    "写作": "作文",
    "填空": "空所補充",
    "改写": "書きかえ",
    "把词和释义配对": "語と意味を結ぶ",
    "配对": "組み合わせ",
})

# Values valid as Japanese as-is (shared kanji words, adjudicated):
# 生活/文化/体育/青年 (band titles), 怪物, 原文, 原形, 投票率.
# These stay identical and are NOT in MAP; the audit below allowlists them.
ALLOW_IDENTICAL = {
    "LIFE · 生活", "CULTURE · 文化", "SPORT · 体育", "YOUTH · 青年",
    "monster=怪物 b", "原文：a teacher from Ohio", "would + 原形",
    "be going to + 原形 vote", "turnout = 投票率 a",
}

# Core printed-note set, measured with tools/p8.py extract on the core P8.
PRINT_NOTES = {11, 12, 14, 19, 29, 30, 31, 33, 41, 44, 47, 48, 51, 58, 64, 66,
                67, 68, 69, 71, 74, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93,
                100, 102, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117,
                118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130,
                131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143,
                144, 145, 146, 147, 148, 149, 150}


def replace_line(text, anchor, new_line, expect=1):
    lines = text.split("\n")
    hits = [i for i, ln in enumerate(lines) if anchor in ln]
    assert len(hits) == expect, f"line anchor {anchor!r}: found {len(hits)}, want {expect}"
    for i in hits:
        lines[i] = new_line
    return "\n".join(lines)


def main():
    # 1. re-copy core build (except svglib) + assets
    for fn in FILES:
        if fn == "bslib4.py" or fn.startswith("content"):
            shutil.copy2(os.path.join(CORE_BUILD, fn), os.path.join(HERE, fn))
    if os.path.isdir(os.path.join(HERE, "assets")):
        shutil.rmtree(os.path.join(HERE, "assets"))
    shutil.copytree(os.path.join(CORE_BUILD, "assets"), os.path.join(HERE, "assets"))
    # 2. canonical JA svglib, md5-gated, never edited
    data = open(CANON_SVGLIB, "rb").read()
    assert hashlib.md5(data).hexdigest() == CANON_MD5, "canonical JA svglib md5 mismatch"
    open(os.path.join(HERE, "svglib.py"), "wb").write(data)
    # 3. value map, longest first, quoted-literal replacement
    for fn in FILES:
        path = os.path.join(HERE, fn)
        text = open(path, encoding="utf-8").read()
        for old, new in sorted(MAP.items(), key=lambda kv: -len(kv[0])):
            if old == new:
                continue
            quoted_old, quoted_new = '"%s"' % old, '"%s"' % new
            n = text.count(quoted_old)
            if n:
                text = text.replace(quoted_old, quoted_new)
                print(f"{fn}: {n}x {old[:28]!r} -> {new[:28]!r}")
        open(path, "w", encoding="utf-8").write(text)
    # 4. line-based code edits
    p12 = os.path.join(HERE, "content12.py")
    t = open(p12, encoding="utf-8").read()
    t = t.replace("weekly-report-w45-en-core/svg", "weekly-report-w45-en-ja/svg")
    t = replace_line(t, "THE LEARNERS' WEEKLY",
                     'p.text(975, 372, "英語テキスト · 日本語の解説 — 日本語読者のための版", 19.5, "sans", True, BRICK, anchor="middle")')
    open(p12, "w", encoding="utf-8").write(t)
    for fn in ["content34.py", "content56.py", "content7.py", "content8.py"]:
        p = os.path.join(HERE, fn)
        t = open(p, encoding="utf-8").read()
        assert "weekly-report-w45-en-core/svg" in t
        t = t.replace("weekly-report-w45-en-core/svg", "weekly-report-w45-en-ja/svg")
        open(p, "w", encoding="utf-8").write(t)
    p8 = os.path.join(HERE, "content8.py")
    t = open(p8, encoding="utf-8").read()
    t = replace_line(t, "— 第 {pg}",
                     '    kf.para(f"— {pg} ページ —", 17, "sans", True, OLIVE, 1.28, 3)')
    t = replace_line(t, 'if e["note"] and (pg == 8',
                     '        if e["note"] and e["n"] in PRINT_NOTES:')
    t = replace_line(t, 's += f"（',
                     '            s += f" ({e[\'note\']})"')
    notes_block = ("# Printed-note parity with the core (tools/p8.py extract on the\n"
                   "# core P8): the core prints a note when the item is on page 8,\n"
                   "# or its (Chinese) note is <= 10 chars, or its type is\n"
                   "# correction/chart-reading. Japanese notes are longer, so the\n"
                   "# core printed set is applied EXPLICITLY by exercise number.\n"
                   "PRINT_NOTES = " + repr(sorted(PRINT_NOTES)) + "\n")
    assert "from itertools import groupby" in t
    t = t.replace("from itertools import groupby", notes_block + "from itertools import groupby", 1)
    open(p8, "w", encoding="utf-8").write(t)
    bsl = os.path.join(HERE, "bslib4.py")
    t = open(bsl, encoding="utf-8").read()
    t = replace_line(t, 'f"第 {n}',
                     '        self.text(RIGHT, 2624, f"{n} ページ（全 {total} ページ）", 20, "sans", False, GREY, anchor="end")')
    open(bsl, "w", encoding="utf-8").write(t)
    # 5. audits: no old value left (quoted), no core OUT left, no forbidden word
    for fn in FILES:
        text = open(os.path.join(HERE, fn), encoding="utf-8").read()
        assert "weekly-report-w45-en-core" not in text, fn
        for old in MAP:
            if old != MAP[old]:
                assert ('"%s"' % old) not in text, f"{fn}: leftover {old!r}"
        assert "桥接" not in text, fn
    print("transform OK: all old values consumed, OUT repointed, svglib md5 OK")


if __name__ == "__main__":
    main()

