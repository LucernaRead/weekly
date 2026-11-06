# -*- coding: utf-8 -*-
"""W45 IT core -> IT x JA fan-out transform for the BUILD COPY ONLY.

Literal replacements only (tools README #17): each rep() fails loudly if
its old string is absent, so a typo can never silently skip a translation.
Italian target-language text is never a replacement target; only the
explanation layer (Chinese notes/bridges/titles/furniture) and the P8
E-section re-aiming change. Registry exercise-type names stay in Chinese
(never printed anywhere, W43 IT x JA / W45 IT x EN precedent) so the
registry stays byte-comparable with the core; the P8 writing type check
therefore also stays. Furniture follows the shipped W43 IT x JA SVGs
(badge replaces the (975,372) tagline call, 20pt BRICK; footer; page
line; gloss prefix "解説 — "; P8 separators "— N ページ —"), which
outrank the generic rules in tools README #20. bridge() is renamed to
expl() following the W43 IT x JA precedent (definition + all calls).
"""

import pathlib, sys

B = pathlib.Path('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-it-ja-build')
C12, C34, C56, C7, C8, BS, SV = 'content12.py', 'content34.py', 'content56.py', 'content7.py', 'content8.py', 'bslib4.py', 'svglib.py'
ALL = [C12, C34, C56, C7, C8]

def rep(files, old, new, expect=None):
    total = 0
    for fn in files:
        p = B / fn
        t = p.read_text(encoding='utf-8')
        c = t.count(old)
        total += c
        if c:
            p.write_text(t.replace(old, new), encoding='utf-8')
    if expect is not None and total != expect:
        print(f'COUNT MISMATCH: {old!r} found {total}, expected {expect}'); sys.exit(1)
    if total == 0:
        print(f'NOT FOUND: {old!r}'); sys.exit(1)
    return total

# ---------- repoint OUT + render names (copy only; core untouched) ----------
rep(ALL, 'weekly-report-w45-it-core', 'weekly-report-w45-it-ja', 5)
rep(['render.py'], 'weekly-report-w45-it-core', 'weekly-report-w45-it-ja', 1)
rep(['render.py'], 'La-Lucerna-VOL2-web.pdf', 'La-Lucerna-VOL2-JA-web.pdf', 1)
rep(['render.py'], 'La-Lucerna-VOL2.pdf', 'La-Lucerna-VOL2-JA.pdf', 1)
rep(['render.py'], 'Render the IT weekly', 'Render the IT x JA edition', 1)

# ---------- bslib4 furniture (W43 IT x JA shipped strings, VOL.2) ----------
rep([BS], '"La Lucerna · 意大利语周报 VOL.2 · LUCERNA ITALIAN WEEKLY"',
    '"La Lucerna · イタリア語週刊 VOL.2 · 本文はイタリア語 · 解説は日本語"', 1)
rep([BS], 'f"第 {n} 版 / 共 {total} 版"', 'f"{n} ページ（全 {total} ページ）"', 1)
rep([BS], '"译注｜" + s', '"解説 — " + s', 1)

# ---------- P1 masthead + pairing badge (W43 IT x JA: badge replaces the
# (975,372) tagline call, 20pt BRICK centred; the Italian strapline there
# is furniture, replaced exactly as in the W43 shipped precedent) ----------
rep([C12], '"OGNI SETTIMANA IN ITALIANO · 每周一期 · 读意大利人正在读的意大利语"',
    '"OGNI SETTIMANA IN ITALIANO · 毎週一号 · イタリア人が読んでいるイタリア語を読む"', 1)
rep([C12], '"意 大 利 语 周 报 · VOL.2 · IL PRIMO FREDDO · IL PANETTONE · LA SERIE A"',
    '"イ タ リ ア 語 週 刊 · VOL.2 · IL PRIMO FREDDO · IL PANETTONE · LA SERIE A"', 1)
rep([C12], 'p.text(975, 372, "IL GIORNALE SETTIMANALE PER IMPARARE — L\'ITALIA VERA, IN ITALIANO, DALL\'ITALIA", 19, "sans", False, GREY, anchor="middle")',
    'p.text(975, 372, "イタリア語テキスト · 日本語の解説 — 日本語読者のための版", 20, "sans", True, BRICK, anchor="middle")', 1)
rep([C12], 'p.text(RIGHT - 30, 522, "初寒之周 · 详见第 2 版", 21, "sans", False, "#b3a06a", anchor="end")',
    'p.text(RIGHT - 30, 522, "初寒の週 · 詳しくは2ページ", 21, "sans", False, "#b3a06a", anchor="end")', 1)
rep([C12], 'p.text(RIGHT - 30, 478, "本周迎来第一场寒冷", 24, "sans", True, "#b3a06a", anchor="end")',
    'p.text(RIGHT - 30, 478, "今週、最初の寒さが到来", 24, "sans", True, "#b3a06a", anchor="end")', 1)
rep([C12], '"LA NOTIZIA · 头条"', '"LA NOTIZIA · トップニュース"', 1)
rep([C12], '"讲解｜il primo freddo 第一场寒冷 · il versante adriatico 亚得里亚海一侧 · la previsione 预报 · assaggi 品尝。"',
    '"解説 — il primo freddo 初寒 · il versante adriatico アドリア海側 · la previsione 予報 · assaggi 試食。"', 1)
rep([C12], '"LA SETTIMANA IN CIFRE · 数字看本周"', '"LA SETTIMANA IN CIFRE · 数字で見る今週"', 1)
rep([C12], '（可能下初雪的海拔）', '（初雪の可能性がある標高）', 1)
rep([C12], '（米兰文化论坛 50 多场活动）', '（ミラノ文化フォーラム50超の催し）', 1)
rep([C12], '（参加米兰潘妮托尼决赛的国家数）', '（ミラノのパネットーネ決勝参加国数）', 1)
rep([C12], '（本周末意甲第 11 轮）', '（今週末のセリエA第11節）', 1)
rep([C12], '"ADESSO TU · 即学即练"', '"ADESSO TU · さあ練習"', 1)
rep([C12], '"本周日程 · Cosa succede, giorno per giorno"', '"今週 · Cosa succede, giorno per giorno"', 1)
rep([C12], '"日程以各活动日历为准，时间可能有变。"', '"日程は各イベントのカレンダー通り。"', 1)
rep([C12], '"IN QUESTO NUMERO · 本期目录"', '"IN QUESTO NUMERO · 目次"', 1)
rep([C12], '"“第一场寒冷”：温和秋天后的第一波寒冷。"', '"「il primo freddo」：穏やかな秋の後の寒さ。"', 1)
rep([C12], '"IN BREVE · 快讯"', '"IN BREVE · 速報"', 1)
rep([C12], '"QUIZ LAMPO · 闪电问答"', '"QUIZ LAMPO · 速答クイズ"', 1)
rep([C12], '"读头版，选出正确答案 · 答案见第 8 版"', '"1ページを読んで、正しい答えを選ぶ · 答えは8ページ"', 1)

# ---------- band titles / subs ----------
rep([C12], '"VITA · 生活"', '"VITA · 生活"', 1)
rep([C12], '"LIVELLO A2 · Il primo freddo e il 2 novembre · 初寒与追思日"',
    '"LIVELLO A2 · Il primo freddo e il 2 novembre · 初寒と死者の日"', 1)
rep([C34], '"CULTURA · 文化"', '"CULTURA · 文化"', 1)
rep([C34], '"A2 → B1 · Panettone, torrone e musei aperti · 甜点与博物馆"',
    '"A2 → B1 · Panettone, torrone e musei aperti · スイーツと美術館"', 1)
rep([C34], '"SPORT · 体育"', '"SPORT · スポーツ"', 1)
rep([C34], '"LIVELLO B1 · La Serie A e l\'Europa · 意甲与欧战"',
    '"LIVELLO B1 · La Serie A e l\'Europa · セリエAと欧州戦"', 1)
rep([C56], '"GIOVANI · 青年"', '"GIOVANI · 青年"', 1)
rep([C56], '"LIVELLO B1 · Dopo Lucca: cultura, cinema e weekend · 卢卡之后"',
    '"LIVELLO B1 · Dopo Lucca: cultura, cinema e weekend · ルッカの後で"', 1)
rep([C56], '"APPROFONDIMENTO · 深读"', '"APPROFONDIMENTO · 深掘り"', 1)
rep([C56], '"LIVELLO B2 · Leggere le previsioni · 怎样读天气预报"',
    '"LIVELLO B2 · Leggere le previsioni · 天気予報の読み方"', 1)
rep([C7], '"LINGUA · 语言"', '"LINGUA · 言語"', 1)
rep([C7], '"聚焦语言 · Tre livelli, tre strumenti · 三个级别，三件工具"',
    '"言語フォーカス · Tre livelli, tre strumenti · 3つのレベル、3つの道具"', 1)
rep([C8], '"VALUTAZIONE E RISPOSTE · 练习与答案"', '"VALUTAZIONE E RISPOSTE · 演習と答え"', 1)
rep([C8], '"第 8 版 · La grande prova della settimana + tutte le risposte"',
    '"8 ページ · La grande prova della settimana + tutte le risposte"', 1)

# ---------- section heads / shared apparatus ----------
rep(ALL, '"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
    '"答えは8ページ · レベル混合出題、番号で答えを探す"', 5)
rep(ALL, '"E TU? · 说说你自己"', '"E TU? · あなたは？"')
rep([C12], '"ESERCIZI · 第 2 版练习"', '"ESERCIZI · 2ページの練習"', 1)
rep([C34], '"ESERCIZI · 第 3 版练习"', '"ESERCIZI · 3ページの練習"', 1)
rep([C34], '"ESERCIZI · 第 4 版练习"', '"ESERCIZI · 4ページの練習"', 1)
rep([C56], '"ESERCIZI · 第 5 版练习"', '"ESERCIZI · 5ページの練習"', 1)
rep([C56], '"ESERCIZI · 第 6 版练习"', '"ESERCIZI · 6ページの練習"', 1)
rep([C12], '"IL 2 NOVEMBRE · 追思日"', '"IL 2 NOVEMBRE · 死者の日"', 1)
rep([C34], '"LA SETTIMANA DEL CALCIO · 足球周"', '"LA SETTIMANA DEL CALCIO · サッカーの週"', 1)
rep([C56], '"LE MINIME DI ESEMPIO · 练习用示例最低温 (DATI INVENTATI PER L\'ESERCIZIO)"',
    '"LE MINIME DI ESEMPIO · 練習用の最低気温の例 (DATI INVENTATI PER L\'ESERCIZIO)"', 1)
rep([C56], '"PROBABILITÀ · 概率"', '"PROBABILITÀ · 確率"', 1)

# ---------- bridges (printed grey sans; renamed to expl() at the end) ----------
rep([C12], '"发稿时表决结果尚未确认，详见第 6 版。"',
    '"発行時点で投票結果は未確認。詳しくは6ページ。"', 1)
rep([C12], '"用意大利语补全句子。"', '"イタリア語で文を完成させましょう。"', 1)
rep([C12], '"补全动词的现在时形式。"', '"動詞の現在形で補いましょう。"', 1)
rep([C12], '"读第 2 版文章，选出正确答案。"', '"2ページの記事を読んで、正しい答えを選びましょう。"', 1)
rep([C34], '"读第 3 版文章，选出正确答案。"', '"3ページの記事を読んで、正しい答えを選びましょう。"', 1)
rep([C34], '"用方框里的词填空。"', '"枠の中の語で空所を補いましょう。"', 1)
rep([C34], '"用 passato prossimo（近过去时）补全，注意助动词 avere / essere。"',
    '"passato prossimo（近過去）で補いましょう。助動詞avere / essereに注意。"', 1)
rep([C34], '"把词组成正确的句子。"', '"語を並べて正しい文を作りましょう。"', 1)
rep([C34], '"读第 4 版文章，选出正确答案。"', '"4ページの記事を読んで、正しい答えを選びましょう。"', 1)
rep([C34], '"用括号里词的比较级填空（数据看赛程表）。"',
    '"かっこの語の比較級で補いましょう（データは日程表参照）。"', 1)
rep([C34], '"用 passato prossimo 补全。"', '"passato prossimoで補いましょう。"', 1)
rep([C56], '"读第 5 版文章，选出正确答案。"', '"5ページの記事を読んで、正しい答えを選びましょう。"', 1)
rep([C56], '"用方框里的词填空。注意：有的词要变成复数。"',
    '"枠の中の語で空所を補いましょう。複数形にする語もあります。"', 1)
rep([C56], '"用将来时（futuro semplice）补全。"', '"未来形（futuro semplice）で補いましょう。"', 1)
rep([C56], '"发稿时 10 月 28 日表决结果尚未确认：本期只写预期日期、争议点和 DPB 数字，不写结果。"',
    '"発行時点で10月28日の投票結果は未確認：今号は予定日、論点、DPBの数字のみを載せ、結果は載せていません。"', 1)
rep([C56], '"看上面的练习图表，选出正确答案。"', '"上の練習用グラフを見て、正しい答えを選びましょう。"', 1)
rep([C56], '"用方框里的词填空：probabilità · media · bollettino · modello"',
    '"枠の中の語で空所を補いましょう：probabilità · media · bollettino · modello"', 1)
rep([C7], '"天气用无人称动词（第三人称单数）；“我冷”说 ho freddo，“外面冷”说 fa freddo。"',
    '"文法ポイント — 天気は非人称動詞（三人称単数）。「寒い」は ho freddo、「外は寒い」は fa freddo。"', 1)
rep([C7], '"讲过去用近过去时：arrivare/andare 等用 essere，分词配合性数；avere 的分词不变。"',
    '"文法ポイント — 過去は近過去：arrivare/andareなどはessere、分詞は性・数に一致。avereの分詞は不変化。"', 1)
rep([C7], '"è probabile che / è possibile che / bisogna che 后用虚拟式；so che、scrivono che 后用陈述式。"',
    '"文法ポイント — è probabile che / è possibile che / bisogna che の後は接続法。so che、scrivono che の後は直説法。"', 1)

# ---------- gloss() argument strings (counts must stay 1:1 with the core) ----------
rep([C12], '"il cappotto 大衣 · la sciarpa 围巾 · i guanti 手套 · a strati 分层穿衣 · il termosifone 暖气片 · il crisantemo 菊花"',
    '"il cappotto コート · la sciarpa マフラー · i guanti 手袋 · a strati 重ね着 · il termosifone 暖房 · il crisantemo 菊"', 1)
rep([C34], '"il panettone 米兰圣诞面包 · il torrone 牛轧糖 · l\'assaggio 品尝 · la bancarella 摊位 · il cantiere 施工现场/修复工地。"',
    '"il panettone パネットーネ · il torrone トローネ · l\'assaggio 試食 · la bancarella 屋台 · il cantiere 工事現場"', 1)
rep([C34], '"la giornata 轮次 · la presentazione 赛前介绍 · gli spalti 看台 · la sera 晚上。"',
    '"la giornata 節 · la presentazione 事前紹介 · gli spalti 観客席 · la sera 夜"', 1)
rep([C56], '"il cosplay 角色扮演服装 · gratuito 免费的 · il documentario 纪录片 · lo schermo 银幕。"',
    '"il cosplay コスプレ衣装 · gratuito 無料の · il documentario ドキュメンタリー · lo schermo 画面"', 1)
rep([C56], '"la probabilità 概率 · la media 平均值 · il modello 模型/预报模式 · il bollettino 公报/预报 · aggiornare 更新。"',
    '"la probabilità 確率 · la media 平均値 · il modello 予報モデル · il bollettino 予報 · aggiornare 更新する"', 1)

# ---------- P1/P2/P3/P4/P5 box parentheticals + E TU notes ----------
rep([C56], '（周二：米兰文化论坛开幕）', '（火曜：ミラノ文化フォーラム開幕）', 1)
rep([C56], '（周三至周四：欧战直播）', '（水曜～木曜：欧州戦中継）', 1)
rep([C56], '（周五准备周末）', '（金曜：週末の準備）', 1)
rep([C56], '（周六：米兰或克雷莫纳品尝）', '（土曜：ミラノかクレモナで試食）', 1)
rep([C56], '（周日：意甲与返程）', '（日曜：セリエAと帰路）', 1)
rep([C12], '"初寒来了你穿什么：大衣、围巾还是手套？写两句意大利语寄给编辑部。"',
    '"初寒が来たら何を着ますか：コート、マフラー、手袋？イタリア語で2文書いて編集部へ送りましょう。"', 2)
rep([C34], '"你更喜欢传统潘妮托尼还是巧克力味的？写两句寄来。"',
    '"伝統的なパネットーネとチョコレート味、どちらが好きですか？2文書いて送りましょう。"', 2)
rep([C34], '"周日晚上你看哪场比赛？写两句意大利语寄来。"',
    '"日曜の夜、どの試合を見ますか？イタリア語で2文書いて送りましょう。"', 2)
rep([C56], '"卢卡之后你去哪：文化论坛、电影还是美食节？写两句寄来。"',
    '"ルッカの後、どこへ行きますか：文化フォーラム、映画、それとも食の祭り？2文書いて送りましょう。"', 2)

# ---------- P2 FRASE box: title size 19 (W45 IT x EN precedent; 23pt overflows) ----------
rep([C12], 'f.box("LA FRASE PER RICORDARE · 口诀", [\n    ("«Fa freddo, copriti bene!» Così dicono le nonne italiane: quando arriva il primo freddo, il consiglio è uno solo — vestirsi bene, a strati.", "serif", False, INK, 21.5, 1.4),\n])',
    'f.box("LA FRASE PER RICORDARE · 覚え方", [\n    ("«Fa freddo, copriti bene!» Così dicono le nonne italiane: quando arriva il primo freddo, il consiglio è uno solo — vestirsi bene, a strati.", "serif", False, INK, 21.5, 1.4),\n], tsize=19)', 1)

# ---------- P7: errori notes (terse, each verified 1 wrapped line at 19.5pt,
# holding the core's col3 geometry exactly) ----------
rep([C7], '"fa 后面的 freddo 永远不变。"', '"faの後のfreddoは不変化。"', 1)
rep([C7], '"nevicare 只用第三人称单数。"', '"nevicareは三人称単数のみ。"', 1)
rep([C7], '"预报给的是概率，不是确定性。"', '"予報は確率、確実性ではない。"', 1)
rep([C7], '"gente 是单数，动词形容词用单数阴性。"', '"genteは単数女性名詞。"', 1)
rep([C7], '"ERRORI TIPICI · 常见错误"', '"ERRORI TIPICI · よくある間違い"', 1)
# P7 parola: Italian definition sentence is FROZEN verbatim; only the gloss
# line below it is localised into Japanese.
rep([C7], '"LA PAROLA · 本周生词"', '"LA PAROLA · 今週の言葉"', 1)
rep([C7], '"assaggio = 品尝。本周见第 3 版：潘妮托尼决赛上观众可以免费品尝。"',
    '"assaggio = 試食。第3ページ：パネットーネ決勝で観客は無料で試食できます。"', 2)
# P7 letters: Italian letter text frozen verbatim, including its
# "(esempio della redazione)" label. The Japanese note states all three
# disclosure facts (no real letters yet, no best page-8 essay yet, the
# sample stands in and both are promised for VOL.3) plus an explicit
# imperative invitation with a VOL.3 publication promise. Per the
# coordinator clarification, NO new Italian disclosure sentence is
# written (the core has none, W43 has none, IT x DE has none); the
# frozen Italian elements (letter, label, VOL.3 preview promise) stand
# with this Japanese disclosure. Verified 3 wrapped lines at 20pt, the
# core note's line count, so col3 still ends at y=1673.
rep([C7], '"这是编辑部示例信，非真实来信。来信请寄编辑部，VOL.3 刊登真实来信与第 8 版最佳作文！"',
    '"編集部の例文です。本物の手紙も8ページの優秀作文も未着で、約束はVOL.3へ。手紙を送ってください。VOL.3に掲載します！"', 2)
rep([C7], '"FRASI DELLA SETTIMANA · 本周金句（逐字摘自本期文章）"',
    '"FRASI DELLA SETTIMANA · 今週の名文（今号の記事からそのまま引用）"', 1)
rep([C7], '"第一场真正的寒冷到来了。"', '"季節最初の本物の寒さがやってきた。"', 1)
rep([C7], '"这不是确定性，而是概率。"', '"確実性ではなく、確率だ。"', 1)
rep([C7], '"11 月 2 日是追思日。"', '"11月2日は死者の日だ。"', 1)
rep([C7], '"天冷，穿暖和点！"', '"寒いから、暖かくして！"', 1)
rep([C7], '"观众可以免费品尝。"', '"観客は無料で試食できる。"', 1)
rep([C7], '"足球不会因为第一场寒冷而停下。"', '"サッカーは最初の寒さでは止まらない。"', 1)
rep([C7], '"文化继续。"', '"文化は続く。"', 1)
rep([C7], '"高概率不等于确定性。"', '"高い確率も確実性ではない。"', 1)
rep([C7], '"LA PROSSIMA SETTIMANA · 下期预告 (VOL.3)"', '"LA PROSSIMA SETTIMANA · 次号予告 (VOL.3)"', 1)

# ---------- printed instructions (instr= values sit beside exercise numbers;
# W43 IT x JA precedent forms) ----------
rep(ALL, 'instr="填空"', 'instr="空所補充"')
rep(ALL, 'instr="造句"', 'instr="文を作る"')
rep(ALL, 'instr="判断"', 'instr="正誤"')
rep(ALL, 'instr="把词和释义配对"', 'instr="語と意味を結ぶ"')
rep(ALL, 'instr="写作"', 'instr="作文"')
# P8 E-section instructions, per item direction (W43 IT x JA ruling: same
# item numbers as IT x EN — 137/138/139 re-aimed to Japanese, 140 re-aimed
# to Italian)
rep([C8], 'f.ex("A2", "翻译", "周一第一场寒冷来了。", "对照原文",\n     "Lunedì arriva il primo freddo. → ___", instr="翻译"',
    'f.ex("A2", "翻译", "月曜日に最初の寒さがやってきます。", "原文と照らしましょう。",\n     "Lunedì arriva il primo freddo. → ___", instr="日本語に翻訳"', 1)
rep([C8], 'f.ex("B1", "翻译", "观众可以免费品尝。", "assaggiare gratis = 免费品尝",\n     "Il pubblico può assaggiare gratis. → ___", instr="翻译"',
    'f.ex("B1", "翻译", "観客は無料で試食できます。", "assaggiare gratis = 無料で試食",\n     "Il pubblico può assaggiare gratis. → ___", instr="日本語に翻訳"', 1)
rep([C8], 'f.ex("B1", "翻译", "周日晚上，佛罗伦萨对尤文图斯。", "si gioca = 进行比赛",\n     "Domenica sera si gioca Fiorentina–Juventus. → ___", instr="翻译"',
    'f.ex("B1", "翻译", "日曜の夜、フィオレンティーナ対ユヴェントス。", "si gioca = 試合が行われる",\n     "Domenica sera si gioca Fiorentina–Juventus. → ___", instr="日本語に翻訳"', 1)
rep([C8], 'f.ex("B2", "翻译", "Ogni previsione deve essere chiara.", "dovere = 必须",\n     "每个预报都必须清楚。→ ___", instr="翻译"',
    'f.ex("B2", "翻译", "Ogni previsione deve essere chiara.", "dovere = ～しなければならない",\n     "すべての予報は明確でなければならない。→ ___", instr="イタリア語に翻訳"', 1)

# ---------- exercise notes, pages 1-2 ----------
rep([C12], '"il primo freddo = 第一场寒冷"', '"il primo freddo = 初寒"', 1)
rep([C12], '"la prima neve leggera = 初雪"', '"la prima neve leggera = 初雪"', 1)
rep([C12], '"文化论坛与潘妮托尼决赛都在米兰"', '"フォーラムとパネットーネ決勝はどちらもミラノで"', 1)
rep([C12], '"克雷莫纳的节日叫 Festa del Torrone"', '"クレモナの祭りはFesta del Torrone"', 1)
rep([C12], '"previsioni = 预报（复数）"', '"previsioni = 予報（複数）"', 1)
rep([C12], '"第一场寒冷在周一 11 月 2 日到来"', '"初寒は月曜11月2日に到来"', 1)
rep([C12], '"初雪在 1300–1500 米左右"', '"初雪は1300～1500メートル付近で"', 1)
rep([C12], '"潘妮托尼决赛在米兰"', '"パネットーネ決勝はミラノで"', 1)
rep([C12], '"意甲第 11 轮周日收官"', '"セリエA第11節は日曜に閉幕"', 2)
rep([C12], '"cappotto = 大衣"', '"cappotto = コート"', 1)
rep([C12], '"sciarpa = 围巾"', '"sciarpa = マフラー"', 1)
rep([C12], '"guanti = 手套（复数）"', '"guanti = 手袋（複数）"', 1)
rep([C12], '"crisantemi = 菊花（复数）"', '"crisantemi = 菊（複数）"', 1)
rep([C12], '"termosifoni = 暖气片（复数）"', '"termosifoni = 暖房（複数）"', 1)
rep([C12], '"fare freddo：fa freddo（天气）"', '"fare freddo：fa freddo（天気）"', 1)
rep([C12], '"mettere：io → metto"', '"mettere：io → metto"', 1)
rep([C12], '"portare：loro → portano"', '"portare：loro → portano"', 1)
rep([C12], '"guardare：loro → guardano"', '"guardare：loro → guardano"', 1)
rep([C12], '"restare：la scuola → resta（lei）"', '"restare：la scuola → resta（lei）"', 1)
rep([C12], '"11 月 2 日是追思日"', '"11月2日は死者の日"', 1)
rep([C12], '"追思日的花是菊花"', '"死者の日の花は菊"', 1)
rep([C12], '"分层穿衣：a strati"', '"重ね着：a strati"', 1)
rep([C12], '"诸圣节今年是周日、无连休"', '"諸聖人の日は今年日曜で、連休なし"', 1)
rep([C12], '"cappotto=御寒大衣 c"', '"cappotto = 防寒コート、c"', 1)
rep([C12], '"sciarpa=围巾 d"', '"sciarpa = マフラー、d"', 1)
rep([C12], '"crisantemo=十一月的花 a"', '"crisantemo = 11月の花、a"', 1)
rep([C12], '"termosifone=暖气片 b"', '"termosifone = 暖房、b"', 1)

# ---------- exercise notes, pages 3-4 ----------
rep([C34], '"潘妮托尼决赛在米兰"', '"パネットーネ決勝はミラノで"', 1)
rep([C34], '"克雷莫纳牛轧糖节到 11 月 22 日"', '"クレモナのトローネ祭りは11月22日まで"', 1)
rep([C34], '"潘妮托尼决赛有 19 国糕点师"', '"パネットーネ決勝には19か国の菓子職人"', 1)
rep([C34], '"文化论坛 11 月 3 日周二开幕"', '"文化フォーラムは11月3日火曜に開幕"', 1)
rep([C34], '"阿尔巴松露节到 12 月 6 日"', '"アルバのトリュフ祭りは12月6日まで"', 1)
rep([C34], '"panettone = 米兰圣诞面包"', '"panettone = ミラノのクリスマス菓子"', 1)
rep([C34], '"torrone = 牛轧糖"', '"torrone = トローネ"', 1)
rep([C34], '"assaggio = 品尝"', '"assaggio = 試食"', 1)
rep([C34], '"bancarella = 摊位"', '"bancarella = 屋台"', 1)
rep([C34], '"mandorle = 杏仁（复数）"', '"mandorle = アーモンド（複数）"', 1)
rep([C34], '"tartufo = 松露"', '"tartufo = トリュフ"', 1)
rep([C34], '"arrivare 用 essere：è arrivato"', '"arrivareはessere：è arrivato"', 1)
rep([C34], '"assaggiare 用 avere：abbiamo assaggiato"', '"assaggiareはavere：abbiamo assaggiato"', 1)
rep([C34], '"andare 用 essere，复数 sono andati"', '"andareはessere、複数sono andati"', 1)
rep([C34], '"aprire 用 avere：ha aperto"', '"aprireはavere：ha aperto"', 1)
rep([C34], '"主语 + essere + 地点 + 日期"', '"主語 + essere + 場所 + 日付"', 1)
rep([C34], '"地点在前，主语在后"', '"場所が前、主語が後"', 1)
rep([C34], '"dura fino a = 持续到"', '"dura fino a = ～まで続く"', 1)
rep([C34], '"意甲第 11 轮周日收官"', '"セリエA第11節は日曜に閉幕"', 1)
rep([C34], '"周日晚上佛罗伦萨对尤文图斯"', '"日曜の夜フィオレンティーナ対ユヴェントス"', 1)
rep([C34], '"欧战第 4 轮在 11 月 3–5 日"', '"欧州戦第4節は11月3～5日"', 1)
rep([C34], '"欧战比赛只作前瞻、无结果"', '"欧州戦は展望のみ、結果なし"', 1)
rep([C34], '"国米对科莫在圣西罗"', '"インテル対コモはサン・シーロで"', 1)
rep([C34], '"giornata=联赛的一轮 c"', '"giornata = リーグの一節、c"', 1)
rep([C34], '"presentazione=赛前介绍 b"', '"presentazione = 事前紹介、b"', 1)
rep([C34], '"spalti=看台 a"', '"spalti = 観客席、a"', 1)
rep([C34], '"sera=晚上 d"', '"sera = 夜、d"', 1)
rep([C34], '"周日晚上的比赛晚于周五的：più tardi"', '"日曜夜の試合は金曜より遅い：più tardi"', 1)
rep([C34], '"周五的比赛早于周日的：più presto"', '"金曜の試合は日曜より早い：più presto"', 1)
rep([C34], '"più + bella 周日晚最美（主观评价）"', '"più + bella 日曜夜が一番美しい（主観的評価）"', 1)
rep([C34], '"bene 的比较级是不规则的 meglio"', '"beneの比較級は不規則なmeglio"', 1)
rep([C34], '"vincere：ha vinto"', '"vincere：ha vinto"', 1)
rep([C34], '"pareggiare：ha pareggiato"', '"pareggiare：ha pareggiato"', 1)
rep([C34], '"arrivare 用 essere，复数 sono arrivati"', '"arrivareはessere、複数sono arrivati"', 1)
rep([C34], '"guardare 用 avere：abbiamo guardato"', '"guardareはavere：abbiamo guardato"', 1)
rep([C34], '"prendere 的分词是 preso：ha preso"', '"prendereの分詞はpreso：ha preso"', 1)

# ---------- exercise notes, pages 5-6 ----------
rep([C56], '"卢卡漫画节是第 60 届"', '"ルッカ・コミックスは第60回"', 1)
rep([C56], '"文化论坛 11 月 3 日开幕"', '"文化フォーラムは11月3日に開幕"', 1)
rep([C56], '"民俗电影节在佛罗伦萨"', '"民族映画祭はフィレンツェで"', 2)
rep([C56], '"文化论坛有 50 多场活动"', '"文化フォーラムは50超の催し"', 2)
rep([C56], '"卢卡漫画节主题是 Legacy"', '"ルッカ・コミックスのテーマはLegacy"', 1)
rep([C56], '"armadio = 衣柜"', '"armadio = 洋服だんす"', 1)
rep([C56], '"gratuiti = 免费的（阳性复数）"', '"gratuiti = 無料の（男性複数）"', 1)
rep([C56], '"documentario = 纪录片"', '"documentario = ドキュメンタリー"', 1)
rep([C56], '"schermo = 银幕"', '"schermo = 画面"', 1)
rep([C56], '"castagne arrosto 烤栗子（复数）"', '"castagne arrosto = 焼き栗（複数）"', 1)
rep([C56], '"cosplay = 角色扮演服装"', '"cosplay = コスプレ衣装"', 1)
rep([C56], '"andare 将来时 noi：andremo"', '"andareの未来形noi：andremo"', 1)
rep([C56], '"esserci 将来时：ci sarà（将有）"', '"esserciの未来形：ci sarà（～があるだろう）"', 1)
rep([C56], '"guardare 将来时 noi：guarderemo"', '"guardareの未来形noi：guarderemo"', 1)
rep([C56], '"durare 将来时：durerà"', '"durareの未来形：durerà"', 1)
rep([C56], '"卢卡漫画节到 11 月 8 日才结束是错的"', '"ルッカ・コミックスが11月8日に終わるのは誤り"', 1)
rep([C56], '"示例数据中最冷的是都灵 3°"', '"例示データで最も寒いのはトリノ3°"', 1)
rep([C56], '"示例数据中最暖的是那不勒斯 12°"', '"例示データで最も暖かいのはナポリ12°"', 1)
# '12 − 9 = 3' and '4 + 5 = 9' are language-neutral arithmetic, kept verbatim.
rep([C56], '"图表数据是练习用的、不是真实预报"', '"グラフのデータは練習用で、本物の予報ではない"', 1)
rep([C56], '"高概率不等于确定"', '"高い確率も確実性ではない"', 1)
rep([C56], '"预报基于 ECMWF 等模型"', '"予報はECMWFなどのモデルに基づく"', 1)
rep([C56], '"预报会变，因为大气变化快"', '"予報は変わる、大気が速く変化するため"', 1)
rep([C56], '"DPB 于 10 月 15 日送布鲁塞尔"', '"DPBは10月15日にブリュッセルへ送付"', 1)
rep([C56], '"2027 增长预测 +0,8%"', '"2027年の成長予測 +0,8%"', 1)
rep([C56], '"è probabile che + 虚拟式 piova"', '"è probabile che + 接続法 piova"', 1)
rep([C56], '"è possibile che + 虚拟式 nevichi"', '"è possibile che + 接続法 nevichi"', 1)
rep([C56], '"bisogna che + 虚拟式 controllino"', '"bisogna che + 接続法 controllino"', 1)
rep([C56], '"è importante che + 虚拟式 sia"', '"è importante che + 接続法 sia"', 1)
rep([C56], '"probabilità = 概率"', '"probabilità = 確率"', 1)
rep([C56], '"media = 平均值"', '"media = 平均値"', 1)
rep([C56], '"bollettino = 预报公报"', '"bollettino = 予報公報"', 1)
rep([C56], '"modello = 预报模型"', '"modello = 予報モデル"', 1)

# ---------- exercise notes, page 7 ----------
rep([C7], '"piovere 天气动词：piove"', '"piovere 気象動詞：piove"', 1)
rep([C7], '"fa freddo = 天气冷"', '"fa freddo = 天気が寒い"', 1)
rep([C7], '"nevicare：nevica"', '"nevicare：nevica"', 1)
rep([C7], '"“我冷”说 ho freddo"', '"「寒い」は ho freddo"', 1)
rep([C7], '"arrivare 用 essere：è arrivato"', '"arrivareはessere：è arrivato"', 1)
rep([C7], '"assaggiare 用 avere"', '"assaggiareはavere"', 1)
rep([C7], '"andare 用 essere，复数 sono andati"', '"andareはessere、複数sono andati"', 1)
rep([C7], '"aprire 用 avere + 不变分词"', '"aprireはavere + 不変化分詞"', 1)
rep([C7], '"è probabile che + 虚拟式 piova"', '"è probabile che + 接続法 piova"', 1)
rep([C7], '"è possibile che + 虚拟式 nevichi"', '"è possibile che + 接続法 nevichi"', 1)
rep([C7], '"bisogna che + 虚拟式 sia"', '"bisogna che + 接続法 sia"', 1)
rep([C7], '"so che + 陈述式 arriva"', '"so che + 直説法 arriva"', 1)

# ---------- exercise notes, page 8 ----------
rep([C8], '"primo freddo = 第一场寒冷"', '"primo freddo = 初寒"', 1)
rep([C8], '"追思日在 11 月 2 日"', '"死者の日は11月2日"', 1)
rep([C8], '"文化论坛在米兰开幕"', '"文化フォーラムはミラノで開幕"', 1)
rep([C8], '"潘妮托尼决赛在周六日"', '"パネットーネ決勝は土曜と日曜"', 1)
rep([C8], '"牛轧糖节在克雷莫纳"', '"トローネ祭りはクレモナで"', 1)
rep([C8], '"意甲第 11 轮周日收官：chiude"', '"セリエA第11節は日曜に閉幕：chiude"', 1)
rep([C8], '"佛罗伦萨对尤文图斯在周日晚上"', '"フィオレンティーナ対ユヴェントスは日曜の夜"', 1)
rep([C8], '"民俗电影节在佛罗伦萨"', '"民族映画祭はフィレンツェで"', 1)
rep([C8], '"初雪在 1300–1500 米左右"', '"初雪は1300～1500メートル付近で"', 1)
rep([C8], '"追思日的花是菊花"', '"死者の日の花は菊"', 1)
rep([C8], '"潘妮托尼决赛有 19 国糕点师"', '"パネットーネ決勝には19か国の菓子職人"', 1)
rep([C8], '"文化论坛有 50 多场活动"', '"文化フォーラムは50超の催し"', 1)
rep([C8], '"阿尔巴松露节到 12 月 6 日"', '"アルバのトリュフ祭りは12月6日まで"', 1)
rep([C8], '"DPB 于 10 月 15 日送出"', '"DPBは10月15日に送付"', 1)
rep([C8], '"概率不等于确定"', '"確率は確実性ではない"', 1)
rep([C8], '"卢卡漫画节 11 月 1 日闭幕"', '"ルッカ・コミックスは11月1日に閉幕"', 1)
rep([C8], '"Giulia 去米兰潘妮托尼决赛"', '"Giuliaはミラノのパネットーネ決勝へ"', 1)
rep([C8], '"Paolo 周六去牛轧糖节"', '"Paoloは土曜にトローネ祭りへ"', 1)
rep([C8], '"传统潘妮托尼是 Giulia 品尝的"', '"伝統的なパネットーネはGiuliaが試食したもの"', 1)
rep([C8], '"标题概括两个城市、两个节日"', '"タイトルは2都市と2つの祭りをまとめる"', 1)
rep([C8], '"时间词在前"', '"時間の語が前"', 1)
rep([C8], '"主语 + essere + 地点 + 日期"', '"主語 + essere + 場所 + 日付"', 1)
rep([C8], '"疑问词组在句首"', '"疑問の語句が文頭"', 1)
rep([C8], '"主语 + 动词 + 时间"', '"主語 + 動詞 + 時間"', 1)
rep([C8], '"probabilità=可能性 d"', '"probabilità = 可能性、d"', 1)
rep([C8], '"media=平均值 a"', '"media = 平均値、a"', 1)
rep([C8], '"bollettino=预报公报 b"', '"bollettino = 予報公報、b"', 1)
rep([C8], '"modello=预报模型 c"', '"modello = 予報モデル、c"', 1)
rep([C8], '"torrone = 牛轧糖"', '"torrone = トローネ"', 1)
rep([C8], '"mandorle 杏仁"', '"mandorle = アーモンド"', 1)
rep([C8], '"quanto costa? 多少钱"', '"quanto costa? = いくらですか"', 1)
rep([C8], '"pagare con carta 刷卡"', '"pagare con carta = カードで払う"', 1)
rep([C8], '"牛轧糖节持续到 11 月 22 日"', '"トローネ祭りは11月22日まで"', 1)
# P8 H writing bridge + writing item (key is not printed for writing items;
# the note is printed as "150. ✓ <note>").
rep([C8], 'f.bridge(f"写作题（无唯一答案）；范文（{NWORDS} 词）见下。")',
    'f.bridge(f"作文問題（答えは一つではない）；模範文（{NWORDS} 語）は下です。")', 1)
rep([C8], '"（开放题，范文如下）"', '"（自由作文、模範文は以下）"', 1)
rep([C8], 'f"范文见本版 H 区（{NWORDS} 词）"', 'f"模範文は本ページ H 欄（{NWORDS} 語）"', 1)
# P8 answer-key titles (W43 IT x JA shipped strings; separators JA form)
rep([C8], '"RISPOSTE · 参考答案 — 按版面分页排列，找到题号即可"',
    '"RISPOSTE · 全解答と解説（1–8ページ）"', 1)
rep([C8], '"每题附一句中文简析 · 带 ✓ 的为范文题"',
    '"各問に日本語の短い解説つき · ✓ は模範文のある問題"', 1)
rep([C8], 'f"— PAGINA {pg} —"', 'f"— {pg} ページ —"', 1)

# ---------- bridge -> expl rename (W43 IT x JA precedent; LAST, so the
# f.bridge(...) string reps above still match) ----------
rep([BS], 'def bridge(', 'def expl(', 1)
rep(ALL, '.bridge(', '.expl(', 22)


# ---------- FIX ROUND 2 (round-1 audit + orphan scan) ----------
# (a) P1 cifre box title overflowed its box (ink right 995.5 > border
# 961) and grazed col3 text: shorten the Japanese tail to the W43 IT x JA
# precedent form "数字で今週" (verified < 412px slot at 22pt bold).
rep([C12], '"LA SETTIMANA IN CIFRE · 数字で見る今週"', '"LA SETTIMANA IN CIFRE · 数字で今週"', 1)
# (b) P3 E TU note stranded "ょう。" at a line start (small-kana orphan;
# canonical NO_START does not cover small kana): shorten the question so
# the note wraps to 2 clean lines (wrap-verified, no bad line starts).
rep([C34], '"伝統的なパネットーネとチョコレート味、どちらが好きですか？2文書いて送りましょう。"',
    '"伝統的なパネットーネとチョコレート味、どちらが好き？2文書いて送りましょう。"', 2)
# (c) P5 E TU note stranded "ォーラム…" at a line start (small-katakana
# orphan after "文化フ"): reword the head so the note wraps to 2 clean
# lines (wrap-verified, no bad line starts).
rep([C56], '"ルッカの後、どこへ行きますか：文化フォーラム、映画、それとも食の祭り？2文書いて送りましょう。"',
    '"ルッカの後、どこへ：文化フォーラム、映画、食の祭り？2文書いて送りましょう。"', 2)

print('TRANSFORM COMPLETE')
