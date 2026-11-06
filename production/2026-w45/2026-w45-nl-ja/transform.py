# -*- coding: utf-8 -*-
"""One-off fan-out transform: W45 NL core (Chinese explanations) -> NL x JA.
Line-literal replacements only, each counted. Run once from this dir.
Dutch target text, keys (except re-aimed E137/E138 + writing pointer E150),
facts, images: untouched. Furniture follows the shipped W43 NL x JA SVG
measurements (badge 19.5pt BRICK at y=372, footer, page line, gloss prefix
'解説 — ', P8 separator '— N ページ —'), NOT the generic tables.json text
(tables.json has no established JA-native furniture column).
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
R = []

def rep(f, old, new):
    R.append((f, old, new))

# ---------- global path / furniture ----------
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    rep(f, "weekly-report-w45-nl-core/svg", "weekly-report-w45-nl-ja/svg")
rep("render.py", "weekly-report-w45-nl-core", "weekly-report-w45-nl-ja")
rep("render.py", "De-Lucerna-VOL2.pdf", "De-Lucerna-VOL2-JA.pdf")
rep("render.py", "De-Lucerna-VOL2-web.pdf", "De-Lucerna-VOL2-JA-web.pdf")
rep("render.py", "Render the IT weekly", "Render the NL x JA weekly")
rep("run.py", "Run the IT weekly", "Run the NL x JA weekly")

# ---------- bslib4: footer + page line + gloss prefix + bridge->expl (W43 JA) ----------
rep("bslib4.py", "De Lucerna · 荷兰语周报 VOL.2 · LUCERNA DUTCH WEEKLY",
     "De Lucerna · オランダ語週刊 VOL.2 · 本文はオランダ語 · 解説は日本語")
rep("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"{n} ページ（全 {total} ページ）"')
rep("bslib4.py", "译注｜", "解説 — ")
rep("bslib4.py", "def bridge(self", "def expl(self")
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    rep(f, ".bridge(", ".expl(")

# ---------- types + instr (global; E-item directions per-line below) ----------
# order: instrs FIRST (else the bare type replacement would eat instr values),
# and cloze before plain choice.
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    rep(f, 'instr="填空"', 'instr="空所補充"')
    rep(f, 'instr="判断"', 'instr="正誤"')
    rep(f, 'instr="造句"', 'instr="文を作る"')
    rep(f, 'instr="写作"', 'instr="作文"')
    rep(f, "完形单选", "穴埋め選択")
    rep(f, "完成句子", "文の完成")
    rep(f, "词汇配对", "単語のペア")
    rep(f, "判断对错", "正誤判断")
    rep(f, "单选", "選択問題")
    rep(f, "造句", "文を作る")
    rep(f, "翻译", "翻訳")
    rep(f, "写作", "作文")
    rep(f, 'instr="把词和释义配对"', 'instr="語と意味を結ぶ"')
# E-item directions (per body line, after the global type pass left instr="翻訳")
rep("content8.py", '"De Klimaatweek duurt zeven dagen. → ___", instr="翻訳"',
     '"De Klimaatweek duurt zeven dagen. → ___", instr="日本語に訳す"')
rep("content8.py", '"Code oranje betekent: bereid je voor. → ___", instr="翻訳"',
     '"Code oranje betekent: bereid je voor. → ___", instr="日本語に訳す"')
rep("content8.py", '"博物馆之夜从晚上 19 点到凌晨 2 点。→ ___", instr="翻訳"',
     '"ミュージアムナハトは19時から深夜2時までです。→ ___", instr="オランダ語に訳す"')
rep("content8.py", '"我参加气候周。→ ___", instr="翻訳"',
     '"私は気候週間に参加する。→ ___", instr="オランダ語に訳す"')

# ---------- content12: P1 ----------
rep("content12.py", "ELKE WEEK IN HET NEDERLANDS · 每周一期 · 读荷兰人正在读的荷兰语",
     "ELKE WEEK IN HET NEDERLANDS · 毎週一号 · オランダ人が読んでいるオランダ語を読む")
rep("content12.py", "荷 兰 语 周 报 · VOL.2 · KLIMAATWEEK · MUSEUMNACHT · SPEELRONDE 12",
     "オ ラ ン ダ 語 週 刊 · VOL.2 · KLIMAATWEEK · MUSEUMNACHT · SPEELRONDE 12")
rep("content12.py", 'p.text(975, 372, "DE WEKELIJKSE KRANT OM NEDERLANDS TE LEREN — HET ECHTE NEDERLAND, IN HET NEDERLANDS", 19, "sans", False, GREY, anchor="middle")',
     'p.text(975, 372, "オランダ語テキスト · 日本語の解説 — 日本語読者のための版", 19.5, "sans", True, BRICK, anchor="middle")')
rep("content12.py", '"气候周"', '"気候週間"')
rep("content12.py", '"本周全国气候周 · 详见第 2 版"', '"全国で気候週間 · 詳しくは2ページ"')
rep("content12.py", '"HET NIEUWS · 头条"', '"HET NIEUWS · トップニュース"')
rep("content12.py", 'f.expl("讲解｜de Klimaatweek 气候周 · de boom planten 种树 · besparen 节约 · de waarschuwing 警告、预警。")',
     'f.expl("解説 — de Klimaatweek 気候週間 · de boom planten 植樹 · besparen 節約する · de waarschuwing 警報。")')
rep("content12.py", '"DE WEEK IN CIJFERS · 数字看本周"', '"DE WEEK IN CIJFERS · 数字で見る今週"')
rep("content12.py", "（气候周的天数）", "（気候週間の日数）")
rep("content12.py", "（周六科弗登发放的树木和灌木）", "（土曜日にコーフェルデンが配布する木と低木）")
rep("content12.py", "（博物馆之夜开放的博物馆，70 多家）", "（ミュージアムナハトに開館する美術館・博物館、70超）")
rep("content12.py", "（荷甲第 12 轮的比赛场数）", "（エールディヴィジ第12節の試合数）")
rep("content12.py", '"NU JIJ · 即学即练"', '"NU JIJ · すぐ練習"')
rep("content12.py", '"气候周 11 月 2–8 日"', '"気候週間 11月2–8日"')
rep("content12.py", '"科弗登发放 200 棵树木灌木"', '"コーフェルデンは200本の木と低木を配布"')
rep("content12.py", '"博物馆之夜在 11 月 7 日周六"', '"ミュージアムナハトは11月7日（土）"')
rep("content12.py", '"海伦芬–费耶诺德 11:15 开球"', '"ヘーレンフェーン–フェイエノールトは11:15開始"')
rep("content12.py", '"特温特–阿贾克斯 13:30 开球"', '"トゥウェンテ–アヤックスは13:30開始"')
rep("content12.py", '"· 本周日程"', '"· 今週の予定"')
rep("content12.py", '"Agenda van de week · 本周大事"', '"Agenda van de week · 今週の主な出来事"')
rep("content12.py", '"本周日程见第 2–4 版文章"', '"日程は2–4ページの記事に"')
rep("content12.py", '"IN DEZE EDITIE · 本期目录"', '"IN DEZE EDITIE · 今号の内容"')
rep("content12.py", '"“气候”：我们周围长期的天气与自然。气候周讲的就是我们的气候。"',
     '"「気候」とは、私たちの周りの長期的な天気と自然のこと。気候週間は私たちの気候についての週だ。"')
rep("content12.py", '"IN HET KORT · 快讯"', '"IN HET KORT · 速報"')
rep("content12.py", '"BLIKSEMQUIZ · 闪电问答"', '"BLIKSEMQUIZ · 早押しクイズ"')
rep("content12.py", '"读头版，选出正确答案 · 答案见第 8 版"', '"1ページを読んで正しい答えを選ぶ · 解答は8ページ"')
rep("content12.py", '"气候周共 7 天（11 月 2–8 日）"', '"気候週間は全7日間（11月2–8日）"')
rep("content12.py", '"博物馆之夜在阿姆斯特丹"', '"ミュージアムナハトはアムステルダムで"')
# ---------- content12: P2 ----------
rep("content12.py", 'p.band("LEVEN · 生活", "De Lucerna", "NIVEAU A2 · De Klimaatweek, stap voor stap · 一步一步讲气候周")',
     'p.band("LEVEN · 生活", "De Lucerna", "NIVEAU A2 · De Klimaatweek, stap voor stap · 気候週間を一歩ずつ")')
rep("content12.py", '"ZO ONTHOUD JE HET · 口诀"', '"ZO ONTHOUD JE HET · 覚え方"')
rep("content12.py", 'f.gloss("het klimaat 气候 · wortelen 生根 · besparen 节约 · de verwarming 暖气 · de waarschuwing 预警 · lokaal 当地的、本地的。")',
     'f.gloss("het klimaat 気候 · wortelen 根付く · besparen 節約する · de verwarming 暖房 · de waarschuwing 警報 · lokaal 地元の。")')
rep("content12.py", '"气候周你做什么？种树、节约能源还是骑车。写两句荷兰语寄给编辑部。"',
     '"気候週間、あなたは何をする？木を植える、エネルギーを節約する、それとも自転車に乗る？オランダ語で2文書いて編集部へ送ってください。"')
rep("content12.py", '"EN JIJ? · 说说你自己"', '"EN JIJ? · あなたは?"')
rep("content12.py", '"DE CODES VAN HET KNMI · 气象预警颜色"', '"DE CODES VAN HET KNMI · KNMIの警報カラー"')
rep("content12.py", '"Wat betekent elke kleur? · 每种颜色是什么意思"', '"Wat betekent elke kleur? · 各色の意味は?"')
rep("content12.py", '"天气可能危险，要当心"', '"危険な天気になるおそれ、注意"')
rep("content12.py", '"危险，做好准备"', '"危険、備えよ"')
rep("content12.py", '"非常危险，尽量待在室内"', '"非常に危険、なるべく屋内に"')
rep("content12.py", '"预警针对你所在的地区"', '"警報はあなたの地域向け"')
rep("content12.py", '"OEFENINGEN · 第 2 版练习"', '"OEFENINGEN · 2ページの練習"')
rep("content12.py", '"答案见第 8 版 · 题目可跨级混排，按题号找答案"', '"答えは8ページ · 問題はレベル混合、番号で探してください"')
rep("content12.py", 'e.expl("读第 2 版文章，选出正确答案。")', 'e.expl("2ページの記事を読んで正しい答えを選んでください。")')
rep("content12.py", '"气候周不做：更多开车"', '"気候週間でしないこと：車をもっと使う"')
rep("content12.py", '"红色预警：非常危险，待在室内"', '"赤警報：非常に危険、屋内にいよう"')
rep("content12.py", '"预警针对本地，不针对整个省"', '"警報は地域向けで、州全体向けではない"')
rep("content12.py", '"节约能源：暖气调低一度"', '"省エネ：暖房を1度下げる"')
rep("content12.py", 'e.expl("用第 2 版的词填空。")', 'e.expl("2ページの単語で空所を補充してください。")')
rep("content12.py", '"气候周 11 月 2–8 日共 7 天"', '"気候週間11月2–8日は全7日間"')
rep("content12.py", '"wortelen = 生根（复数主语）"', '"wortelen = 根付く（複数主語）"')
rep("content12.py", '"besparen = 节约"', '"besparen = 節約する"')
rep("content12.py", '"fiets = 自行车"', '"fiets = 自転車"')
rep("content12.py", '"发放地点在兹韦洛"', '"配布場所はズウェーロー"')
rep("content12.py", 'e.expl("用颜色代码和日期填空。")', 'e.expl("警報カラーと日付で空所を補充してください。")')
rep("content12.py", '"黄色代码：当心"', '"黄色警報：注意"')
rep("content12.py", '"橙色代码：危险"', '"オレンジ警報：危険"')
rep("content12.py", '"发放从 13:00 开始"', '"配布は13:00開始"')
rep("content12.py", '"气候周 11 月 8 日周日结束"', '"気候週間は11月8日（日）に終了"')
rep("content12.py", '["Klimaatweek=气候周 b", "besparen=节约 d", "waarschuwing=预警 a", "lokaal=本地的 c"]',
     '["Klimaatweek=気候週間 b", "besparen=節約する d", "waarschuwing=警報 a", "lokaal=地元の c"]')

# ---------- content34: P3 ----------
rep("content34.py", 'p.band("CULTUUR · 文化", "De Lucerna", "NIVEAU A2 → B1 · Museumnacht, boeken en kunst · 博物馆之夜、书籍与艺术")',
     'p.band("CULTUUR · 文化", "De Lucerna", "NIVEAU A2 → B1 · Museumnacht, boeken en kunst · ミュージアムナハト、本と芸術")')
rep("content34.py", 'f.gloss("het museum 博物馆 · de rondleiding 导览 · het tijdslot 时间段 · tweedehands 二手的 · de beurs 展会、集市。")',
     'f.gloss("het museum 博物館 · de rondleiding ガイドツアー · het tijdslot 時間枠 · tweedehands 中古の · de beurs 見本市・市場。")')
rep("content34.py", '"OEFENINGEN · 第 3 版练习"', '"OEFENINGEN · 3ページの練習"')
rep("content34.py", '"答案见第 8 版 · 题目可跨级混排，按题号找答案"', '"答えは8ページ · 問題はレベル混合、番号で探してください"')
rep("content34.py", 'e.expl("读第 3 版文章，选出正确答案。")', 'e.expl("3ページの記事を読んで正しい答えを選んでください。")')
rep("content34.py", '"博物馆之夜在 11 月 7 日周六"', '"ミュージアムナハトは11月7日（土）"')
rep("content34.py", '"博物馆开放到凌晨 2 点"', '"美術館・博物館は深夜2時まで開館"')
rep("content34.py", '"Crossing Border 在海牙"', '"クロッシング・ボーダーはデン・ハーグで"')
rep("content34.py", '"Crossing Border 结合书籍与音乐"', '"クロッシング・ボーダーは本と音楽を結ぶ"')
rep("content34.py", '"PAN 艺术博览会到 11 月 8 日"', '"PAN アートフェアは11月8日まで"')
rep("content34.py", 'e.expl("用方框里的词填空。注意：有的词要变成复数。")',
     'e.expl("枠内の単語で空所を補充してください。注意：複数形に変える単語もあります。")')
rep("content34.py", '"museum 复数：musea"', '"museum 複数形：musea"')
rep("content34.py", '"rondleiding = 导览"', '"rondleiding = ガイドツアー"')
rep("content34.py", '"tijdslot = 时间段"', '"tijdslot = 時間枠"')
rep("content34.py", '"tweedehands = 二手的"', '"tweedehands = 中古の"')
rep("content34.py", '"beurs = 展会、集市"', '"beurs = 見本市・市場"')
rep("content34.py", 'e.expl("用现在完成时补全，注意助动词 hebben/zijn。")',
     'e.expl("現在完了形で補充してください。助動詞 hebben/zijn に注意。")')
rep("content34.py", '"zijn 的 perfectum：zijn geweest"', '"zijn の完了形：zijn geweest"')
rep("content34.py", '"kopen 的 perfectum：hebben gekocht"', '"kopen の完了形：hebben gekocht"')
rep("content34.py", '"voorlezen 的 perfectum：hebben voorgelezen"', '"voorlezen の完了形：hebben voorgelezen"')
rep("content34.py", '"komen 用 zijn：zijn gekomen"', '"komen は zijn を使う：zijn gekomen"')
rep("content34.py", 'e.expl("算一算：用第 3 版的数字回答。")', 'e.expl("計算してください：3ページの数字で答えてください。")')
rep("content34.py", '"19:00 到 02:00 共 7 小时"', '"19:00から02:00までは7時間"')
rep("content34.py", '"11 月 1–8 日共 8 天"', '"11月1–8日は8日間"')
rep("content34.py", '"11 月 3–8 日共 6 天"', '"11月3–8日は6日間"')
rep("content34.py", '"250 的一半是 125"', '"250の半分は125"')
# ---------- content34: P4 ----------
rep("content34.py", 'p.band("SPORT · 体育", "De Lucerna", "NIVEAU B1 · Europese week en speelronde 12 · 欧战周与第 12 轮")',
     'p.band("SPORT · スポーツ", "De Lucerna", "NIVEAU B1 · Europese week en speelronde 12 · ヨーロッパ週間と第12節")')
rep("content34.py", 'f.gloss("de balans 成绩单、总结 · gelijkspelen 打平 · de speelronde 轮次 · de topper 焦点战 · de stand 积分榜。")',
     'f.gloss("de balans 成績のまとめ · gelijkspelen 引き分ける · de speelronde 節 · de topper 注目の一戦 · de stand 順位表。")')
rep("content34.py", '"OEFENINGEN · 第 4 版练习"', '"OEFENINGEN · 4ページの練習"')
rep("content34.py", 'e.expl("读第 4 版文章，选出正确答案。")', 'e.expl("4ページの記事を読んで正しい答えを選んでください。")')
rep("content34.py", '"阿贾克斯 2–0 赢亚特兰大"', '"アヤックスはアタランタに2–0で勝利"')
rep("content34.py", '"特温特 4–1 赢林肯红魔"', '"トゥウェンテはリンカーンに4–1で勝利"')
rep("content34.py", '"NEC 2–4 输给萨格勒布迪纳摩"', '"NEC はディナモ・ザグレブに2–4で敗北"')
rep("content34.py", '"皇家贝蒂斯 1–0 赢费耶诺德"', '"レアル・ベティスはフェイエノールトに1–0で勝利"')
rep("content34.py", '"10 轮后费耶诺德 24 分领跑"', '"10節後フェイエノールトは24点で首位"')
rep("content34.py", 'e.expl("用方框里的词填空。注意动词形式。")',
     'e.expl("枠内の単語で空所を補充してください。動詞の形に注意。")')
rep("content34.py", '"balans = 成绩单、总结"', '"balans = 成績のまとめ"')
rep("content34.py", '"gelijkspelen 过去时复数：speelden gelijk"', '"gelijkspelen の過去形複数：speelden gelijk"')
rep("content34.py", '"topper = 焦点战"', '"topper = 注目の一戦"')
rep("content34.py", '"stand = 积分榜"', '"stand = 順位表"')
rep("content34.py", '"doelpunt = 进球"', '"doelpunt = ゴール"')
rep("content34.py", 'e.expl("用过去时或完成时补全。")', 'e.expl("過去形または完了形で補充してください。")')
rep("content34.py", '"winnen 过去时：won"', '"winnen の過去形：won"')
rep("content34.py", '"gaan 过去时：ging"', '"gaan の過去形：ging"')
rep("content34.py", '"verliezen 过去时：verloor"', '"verliezen の過去形：verloor"')
rep("content34.py", '"komen 的 perfectum 用 zijn"', '"komen の完了形は zijn を使う"')
rep("content34.py", '"对：阿贾克斯 2–0 获胜"', '"正：アヤックスは2–0で勝利"')
rep("content34.py", '"错：NEC 2–4 输了"', '"誤：NEC は2–4で敗北"')
rep("content34.py", '"错：特温特–阿贾克斯 13:30；11:15 是海伦芬–费耶诺德"', '"誤：トゥウェンテ–アヤックスは13:30、11:15はヘーレンフェーン–フェイエノールト"')
rep("content34.py", '"对：10 轮后费耶诺德 24 分第一"', '"正：10節後フェイエノールトは24点で首位"')

# ---------- content56: P5 ----------
rep("content56.py", 'p.band("JONGEREN · 青年", "De Lucerna", "NIVEAU B1 · Robinson is begonnen, ADE en DDW voorbij · 荒岛节目开播、音乐节与设计周落幕")',
     'p.band("JONGEREN · 若者", "De Lucerna", "NIVEAU B1 · Robinson is begonnen, ADE en DDW voorbij · ロビンソン開幕、ADEとDDW閉幕")')
rep("content56.py", "（周日晚 20:00 在 RTL 4 收看）", "（日曜夜20:00にRTL 4で見る）")
rep("content56.py", "（注意比赛项目：分数在那里决出）", "（競技に注目：得点はそこで決まる）")
rep("content56.py", "（和朋友猜谁能留到最后）", "（友だちと最後まで残る人を予想）")
rep("content56.py", "（下周这里继续报道进展）", "（来週ここで続きを報道）")
rep("content56.py", 'f.gloss("het eiland 岛 · de proef 比赛项目、考验 · stemmen 投票 · de aflevering （一）集 · voorbij 过去了、结束了。")',
     'f.gloss("het eiland 島 · de proef 競技・試練 · stemmen 投票する · de aflevering （1）話 · voorbij 終わった。")')
rep("content56.py", '"你看《荒岛远征》吗，还是更爱自己出门活动？写两句荷兰语寄来。"',
     '"『エクスペディティ・ロビンソン』を見る？それとも自分で外に出かける方が好き？オランダ語で2文書いて送ってください。"')
rep("content56.py", '"EN JIJ? · 说说你自己"', '"EN JIJ? · あなたは?"')
rep("content56.py", '"OEFENINGEN · 第 5 版练习"', '"OEFENINGEN · 5ページの練習"')
rep("content56.py", '"答案见第 8 版 · 题目可跨级混排，按题号找答案"', '"答えは8ページ · 問題はレベル混合、番号で探してください"')
rep("content56.py", 'e.expl("读第 5 版文章，选出正确答案。")', 'e.expl("5ページの記事を読んで正しい答えを選んでください。")')
rep("content56.py", '"Robinson 在 11 月 1 日周日开始"', '"ロビンソンは11月1日（日）に開始"')
rep("content56.py", '"19 位参赛者"', '"19人の参加者"')
rep("content56.py", '"ADE 今年 30 年"', '"ADE は今年30年"')
rep("content56.py", '"设计周约 2.500 位设计师"', '"デザインウィークは約2,500人のデザイナー"')
rep("content56.py", '"ADE 与 DDW 在 10 月 25 日周日落幕"', '"ADE と DDW は10月25日（日）に閉幕"')
rep("content56.py", 'e.expl("用方框里的词填空。")', 'e.expl("枠内の単語で空所を補充してください。")')
rep("content56.py", '"eiland = 岛（het）"', '"eiland = 島（het）"')
rep("content56.py", '"proef = 比赛项目、考验（de）"', '"proef = 競技・試練（de）"')
rep("content56.py", '"stemmen = 投票"', '"stemmen = 投票する"')
rep("content56.py", '"aflevering = （一）集"', '"aflevering = （1）話"')
rep("content56.py", '"voorbij = 过去了、结束了"', '"voorbij = 終わった"')
rep("content56.py", '"kandidaat 复数：kandidaten"', '"kandidaat 複数形：kandidaten"')
rep("content56.py", 'e.expl("用 gaan + 不定式说将来。")', 'e.expl("gaan + 不定詞で未来を表してください。")')
rep("content56.py", '"gaat winnen = 会赢（只是猜测）"', '"gaat winnen = 勝つだろう（推測）"')
rep("content56.py", '"wij → gaan + 不定式 kijken"', '"wij → gaan + 不定詞 kijken"')
rep("content56.py", '"zij (复数) → gaan zoeken"', '"zij（複数）→ gaan zoeken"')
rep("content56.py", '"对：11 月 1 日开始"', '"正：11月1日に開始"')
rep("content56.py", '"错：ADE 今年 30 年"', '"誤：ADE は今年30年"')
rep("content56.py", '"错：10 月 25 日已落幕"', '"誤：10月25日に閉幕済み"')
# ---------- content56: P6 ----------
rep("content56.py", 'p.band("VERDIEPING · 深读", "De Lucerna", "NIVEAU B2 · De codes van het KNMI · 气象预警深度解读")',
     'p.band("VERDIEPING · 深掘り", "De Lucerna", "NIVEAU B2 · De codes van het KNMI · KNMIの警報を深掘り")')
rep("content56.py", 'f.gloss("de meteoroloog 气象学家 · waarschuwingsmoeheid 预警疲劳 · vastzetten 固定好 · het advies 建议、忠告 · de voorstander 支持者。")',
     'f.gloss("de meteoroloog 気象学者 · waarschuwingsmoeheid 警報疲れ · vastzetten 固定する · het advies 助言 · de voorstander 賛成者。")')
rep("content56.py", '"练习数据：虚构数字，仅供练习，非真实调查。问题：橙色预警时你会怎么做？（100 名年轻人）"',
     '"練習データ：架空の数字で、練習用です。本当の調査ではありません。質問：オレンジ警報のとき、あなたはどうする？（100人の若者）"')
rep("content56.py", '"DE GRAFIEK · 图表（练习数据）"', '"DE GRAFIEK · グラフ（練習データ）"')
rep("content56.py", '"VOOR OF TEGEN? · 正方还是反方"', '"VOOR OF TEGEN? · 賛成か反対か"')
rep("content56.py", '"OEFENINGEN · 第 6 版练习"', '"OEFENINGEN · 6ページの練習"')
rep("content56.py", 'e.expl("看第 6 版图表（练习数据）回答。")', 'e.expl("6ページのグラフ（練習データ）を見て答えてください。")')
rep("content56.py", '"45 名年轻人选择待在家里"', '"45人の若者が家にいることを選ぶ"')
rep("content56.py", '"25 人先看预警文字"', '"25人はまず警報の文章を読む"')
rep("content56.py", '"10 人不知道"', '"10人は分からない"')
rep("content56.py", '"图表共 100 人：45+25+20+10"', '"グラフは合計100人：45+25+20+10"')
rep("content56.py", 'e.expl("读第 6 版文章，选出正确答案。")', 'e.expl("6ページの記事を読んで正しい答えを選んでください。")')
rep("content56.py", '"以前预警针对整个省"', '"以前の警報は州全体向けだった"')
rep("content56.py", '"如今预警是本地的"', '"今の警報は地域向けだ"')
rep("content56.py", '"红色：非常危险，非必要不上路"', '"赤：非常に危険、必要がなければ外出しない"')
rep("content56.py", '"预警疲劳：警告太多导致不再注意"', '"警報疲れ：警報が多すぎて注意しなくなる"')
rep("content56.py", '"KNMI 说：看代码旁边的文字"', '"KNMI 曰く：コードの横の文章を見よ"')
rep("content56.py", '"lokaal = 本地的"', '"lokaal = 地域の"')
rep("content56.py", '"waarschuwingsmoeheid = 预警疲劳"', '"waarschuwingsmoeheid = 警報疲れ"')
rep("content56.py", '"vastzetten = 固定好"', '"vastzetten = 固定する"')
rep("content56.py", '"advies = 建议（het）"', '"advies = 助言（het）"')
rep("content56.py", 'e.expl("把词组成正确的句子。")', 'e.expl("単語を並べて正しい文を作ってください。")')
rep("content56.py", '"主语 + 动词 + 地点"', '"主語 + 動詞 + 場所"')
rep("content56.py", '"祈使句：动词在首位"', '"命令文：動詞が先頭に"')
rep("content56.py", '"weinig voor = 很少出现"', '"weinig voor = めったに起こらない"')
rep("content56.py", '"raakt + 宾语 + 方式"', '"raakt + 目的語 + 様態"')

# ---------- content7: P7 ----------
rep("content7.py", 'p.band("TAAL · 语言", "De Lucerna", "聚焦语言 · Drie niveaus, drie gereedschappen · 三个级别，三件工具")',
     'p.band("TAAL · 言語", "De Lucerna", "言語に注目 · Drie niveaus, drie gereedschappen · 3レベル、3つの道具")')
rep("content7.py", 'a.expl("het klimaat 气候（长期）；een boom planten 种树；besparen 节约；de waarschuwing 预警。")',
     'a.expl("het klimaat 気候（長期）；een boom planten 植樹；besparen 節約する；de waarschuwing 警報。")')
rep("content7.py", '"气候是长期的天气与自然"', '"気候とは長期的な天気と自然のこと"')
rep("content7.py", '"rood = blijf binnen"', '"rood = 屋内にいよう"')
rep("content7.py", 'b.expl("meedoen 参加：ik doe mee；opruimen 收拾：wij hebben opgeruimd；vastzetten 固定：zij zette vast。")',
     'b.expl("meedoen 参加する：ik doe mee；opruimen 片付ける：wij hebben opgeruimd；vastzetten 固定する：zij zette vast。")')
rep("content7.py", '"opruimen 的分词：opgeruimd"', '"opruimen の過去分詞：opgeruimd"')
rep("content7.py", '"vastzetten 过去时：zette vast"', '"vastzetten の過去形：zette vast"')
rep("content7.py", '"meedoen = 参加、参与"', '"meedoen = 参加する"')
rep("content7.py", 'c.expl("Ik vind dat… 我认为；Volgens mij… 依我看；Het lijkt me dat… 在我看来。")',
     'c.expl("Ik vind dat… ～だと思う；Volgens mij… 私見では；Het lijkt me dat… 私には～のように思える。")')
rep("content7.py", '"Volgens mij… = 依我看"', '"Volgens mij… = 私見では"')
rep("content7.py", '"Ik vind dat… 表达看法"', '"Ik vind dat… は意見を表す"')
rep("content7.py", '"Het lijkt me dat… = 在我看来"', '"Het lijkt me dat… = 私には～のように思える"')
rep("content7.py", '"气候是长期的天气自然，不是今天的天气。"', '"気候とは長期的な天気と自然のことで、今日の天気ではない。"')
rep("content7.py", '"Klimaatweek 是专名，首字母大写。"', '"Klimaatweek は固有名詞なので頭文字は大文字。"')
rep("content7.py", '"een 是单数：een boom；复数直接用 bomen。"', '"een は単数：een boom、複数はそのまま bomen。"')
rep("content7.py", '"omdat 从句后，主句动词在第二位：blijf ik thuis。"', '"omdat の従属節の後では、主節の動詞は2番目：blijf ik thuis。"')
rep("content7.py", '"PAS OP! · 易错诊所"', '"PAS OP! · 間違いクリニック"')
rep("content7.py", '"meedoen = 参加、参与：气候周全荷兰都参加。"', '"meedoen = 参加する：気候週間にはオランダ中が参加する。"')
rep("content7.py", '"HET WOORD · 本周生词"', '"HET WOORD · 今週の単語"')
# readers' corner: Dutch example + Dutch disclosure stay verbatim (frozen);
# the Chinese disclosure + invitation lines become Japanese.
rep("content7.py", 'dt_zh = "截稿时未收到真实来信或第 8 版最佳作文，刊登示例信，承诺顺延 VOL.3。"',
     'dt_ja = "締切時点で本物の手紙も8ページの優秀作文も届いていないため、例文を掲載し、約束はVOL.3へ引き継ぐ。"')
rep("content7.py", 'len(wrap(dt_zh, "sans", False, 20, CW - 44))', 'len(wrap(dt_ja, "sans", False, 20, CW - 44))')
rep("content7.py", 'p.para(bx + 22, yy3 + 20, dt_zh, 20, "sans", False, GREY, CW - 44, 1.42) + 10',
     'p.para(bx + 22, yy3 + 20, dt_ja, 20, "sans", False, GREY, CW - 44, 1.42) + 10')
rep("content7.py", '"编辑部示例信，非真实来信。欢迎寄来你的真实来信和第 8 版最佳作文，VOL.3 刊登！"',
     '"編集部の例文で、本物の手紙ではありません。あなたの本物の手紙と8ページの優秀作文を送ってください。VOL.3に掲載します！"')
rep("content7.py", '"ZINNEN VAN DE WEEK · 本周金句（逐字摘自本期文章）"',
     '"ZINNEN VAN DE WEEK · 今週の名文（本号の記事から逐語引用）"')
rep("content7.py", '"从 11 月 2 日周一到 8 日周日，荷兰是气候周。"', '"11月2日（月）から8日（日）まで、オランダは気候週間だ。"')
rep("content7.py", '"秋天是种树的最好时节。"', '"秋は植樹に最適の季節だ。"')
rep("content7.py", '"黄色意味着：当心，天气可能危险。"', '"黄色は「注意、危険な天気になるおそれ」という意味だ。"')
rep("content7.py", '"70 多家博物馆从晚上 19 点开放到凌晨 2 点。"', '"70を超える美術館・博物館が夜19時から深夜2時まで開いている。"')
rep("content7.py", '"阿贾克斯 10 月 22 日周四 2–0 战胜亚特兰大。"', '"アヤックスは10月22日（木）にアタランタに2–0で勝った。"')
rep("content7.py", '"11 月 1 日周日，《荒岛远征》在 RTL 4 开播，20 点。"', '"11月1日（日）、『エクスペディティ・ロビンソン』がRTL 4で20時に始まった。"')
rep("content7.py", '"预警代码不是禁令，而是一条建议。"', '"警報コードは禁止ではなく助言だ。"')
rep("content7.py", '"天气属于我们所有人，但对每个人的影响各不相同。"', '"天気は私たちみんなのものだが、影響は人それぞれ違う。"')
rep("content7.py", '"VOLGENDE WEEK · 下期预告 (VOL.3)"', '"VOLGENDE WEEK · 来週の予告 (VOL.3)"')
rep("content7.py", "Dutch + matching Chinese.", "Dutch + matching Japanese.")
# ---------- content8: P8 ----------
rep("content8.py", 'p.band("TOETS EN ANTWOORDEN · 练习与答案", "De Lucerna", "第 8 版 · De grote toets van de week + alle antwoorden")',
     'p.band("TOETS EN ANTWOORDEN · テストと解答", "De Lucerna", "8ページ · De grote toets van de week + alle antwoorden")')
rep("content8.py", '"气候周到 11 月 8 日"', '"気候週間は11月8日まで"')
rep("content8.py", '"科弗登发放 200 棵树木灌木"', '"コーフェルデンは200本の木と低木を配布"')
rep("content8.py", '"博物馆之夜在 11 月 7 日"', '"ミュージアムナハトは11月7日"')
rep("content8.py", '"特温特–阿贾克斯 13:30 开球"', '"トゥウェンテ–アヤックスは13:30開始"')
rep("content8.py", '"阿贾克斯 2–0 赢亚特兰大"', '"アヤックスはアタランタに2–0で勝利"')
rep("content8.py", '"Robinson 在 11 月开始"', '"ロビンソンは11月に開始"')
rep("content8.py", '"橙色预警：天气危险"', '"オレンジ警報：危険な天気"')
rep("content8.py", '"meedoen = 参加"', '"meedoen = 参加する"')
rep("content8.py", '"气候周 11 月 2 日周一开始"', '"気候週間は11月2日（月）に開始"')
rep("content8.py", '"发放地点在兹韦洛"', '"配布場所はズウェーロー"')
rep("content8.py", '"Crossing Border 在海牙"', '"クロッシング・ボーダーはデン・ハーグで"')
rep("content8.py", '"PAN 在 RAI 展览中心"', '"PAN は RAI で開催"')
rep("content8.py", '"皇家贝蒂斯 1–0 赢费耶诺德"', '"レアル・ベティスはフェイエノールトに1–0で勝利"')
rep("content8.py", '"10 轮后阿贾克斯 21 分"', '"10節後アヤックスは21点"')
rep("content8.py", '"预警疲劳：警告太多导致不再注意"', '"警報疲れ：警報が多すぎて注意しなくなる"')
rep("content8.py", '"扎安丹旧货市场约 250 个摊位"', '"ザーンダムの蚤の市は約250店"')
rep("content8.py", '"Daan 住在科弗登"', '"ダーンはコーフェルデン在住"')
rep("content8.py", '"他周六领了一棵免费灌木"', '"土曜日に無料の低木を受け取る"')
rep("content8.py", '"周日特温特对阿贾克斯"', '"日曜日はトゥウェンテ対アヤックス"')
rep("content8.py", '"气候周他每天骑车上学"', '"気候週間は毎日自転車で通学"')
rep("content8.py", '"主语 + 动词 + 时间"', '"主語 + 動詞 + 時間"')
rep("content8.py", '"主语 + 动词 + 宾语 + 地点"', '"主語 + 動詞 + 目的語 + 場所"')
rep("content8.py", '"主语 + 动词 + 时间 + 对手"', '"主語 + 動詞 + 時間 + 対戦相手"')
rep("content8.py", '"可分动词 mee 在句末"', '"分離動詞の mee は文末に"')
# E translation items: keys 137/138 re-aimed INTO Japanese (W43 JA precedent);
# 139/140 stems re-aimed, keys stay Dutch.
rep("content8.py", '"气候周持续七天。"', '"気候週間は7日間続く。"')
rep("content8.py", '"对照第 1 版头条"', '"1ページの見出し参照"')
rep("content8.py", '"橙色预警意味着：做好准备。"', '"オレンジ警報は「備えよ」という意味だ。"')
rep("content8.py", '"第 2 版原句 · bereid je voor 做好准备"', '"2ページの原文 · bereid je voor 備えよ"')
rep("content8.py", '"注意时间表达 van...tot..."', '"時間の表現 van...tot... に注意"')
rep("content8.py", '"meedoen 是可分动词"', '"meedoen は分離動詞"')
rep("content8.py", '["klimaat=气候 c", "meedoen=参加 b", "waarschuwing=预警 a", "vastzetten=固定好 d"]',
     '["klimaat=気候 c", "meedoen=参加する b", "waarschuwing=警報 a", "vastzetten=固定する d"]')
rep("content8.py", '"boom = 树"', '"boom = 木"')
rep("content8.py", '"struik = 灌木"', '"struik = 低木"')
rep("content8.py", '"planten = 种"', '"planten = 植える"')
rep("content8.py", '"zachte = 柔软的（土壤）"', '"zachte = 柔らかい（土）"')
rep("content8.py", '"发放到 16:00 结束"', '"配布は16:00まで"')
rep("content8.py", 'f.expl(f"作文题（无唯一答案）；范文（{NWORDS} 词）见下。")',
     'f.expl(f"作文問題（正解は一つではない）；模範文（{NWORDS}語）は下記。")')
rep("content8.py", '"（开放题，范文如下）"', '"（自由記述 — 模範文は以下）"')
rep("content8.py", 'f"范文见本版 H 区（{NWORDS} 词）"', 'f"模範文はこのページの H 欄（{NWORDS}語）"')
rep("content8.py", '"ANTWOORDEN · 参考答案 — 按版面分页排列，找到题号即可"',
     '"ANTWOORDEN · 全解答と解説（1–8ページ）"')
rep("content8.py", '"每题附一句中文简析 · 带 ✓ 的为范文题"',
     '"各問に日本語の解説つき · ✓ は模範文のある問題"')
rep("content8.py", 'af.para(f"— PAGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)',
     'af.para(f"— {pg} ページ —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)')

# ---------- FIX ROUND 1 (measured after first render; in transform so a
# from-scratch rerun reproduces the final build) ----------
def fix_round_1():
    # P2-ex overflow (match set needed 428 at y=2191, bottom 2580): tighten
    # P2 exercise spacing only (EN precedent: gaps 8->4, head gaps 13->8),
    # scoped to the P2-exercises segment of content12.py, and shorten the
    # first P2 bridge to one line (正しい答え -> 正解, same meaning).
    p = os.path.join(HERE, "content12.py")
    t = open(p, encoding="utf-8").read()
    a = t.index("# ---- P2 exercises ----")
    b = t.index("p.foot(2)")
    seg = t[a:b]
    n_gap = seg.count("size=20, gap=8")
    seg = seg.replace("size=20, gap=8", "size=20, gap=4")
    heads = 0
    for h in ['e.head("A · BEGRIJPEN", 25)', 'e.head("B · ACTIES", 25)',
              'e.head("C · CODES EN DATUMS", 25)', 'e.head("D · WOORDEN", 25)']:
        if h in seg:
            seg = seg.replace(h, h[:-1] + ", gap=8)")
            heads += 1
    t = t[:a] + seg + t[b:]
    if "2ページの記事を読んで正しい答えを選んでください。" in t:
        t = t.replace("2ページの記事を読んで正しい答えを選んでください。",
                      "2ページを読んで正解を選んでください。")
    open(p, "w", encoding="utf-8").write(t)
    print(f"FIX1 P2: {n_gap}x gap 8->4, {heads} heads gap->8, bridge1 -> 1 line")
    # P7 col3 stack ended 2043, crossing the zinnen gold rule (1937):
    # shorten the invitation 4->2 lines (imperative + VOL.3 promise kept),
    # label the example explicitly as the editors' in the disclosure
    # (dt_c, still 3 lines), trim two clinic notes to one line each
    # (Dutch right lines carry the full rule), tighten box gaps 18->8.
    p = os.path.join(HERE, "content7.py")
    t = open(p, encoding="utf-8").read()
    subs = [
        ('dt_ja = "締切時点で本物の手紙も8ページの優秀作文も届いていないため、例文を掲載し、約束はVOL.3へ引き継ぐ。"',
         'dt_ja = "締切時に本物の手紙と8ページの優秀作文はなく、編集部の例文を掲載。約束はVOL.3へ。"'),
        ('"編集部の例文で、本物の手紙ではありません。あなたの本物の手紙と8ページの優秀作文を送ってください。VOL.3に掲載します！"',
         '"あなたの本物の手紙と8ページの優秀作文を送ってください。VOL.3に掲載します！"'),
        ('"Klimaatweek は固有名詞なので頭文字は大文字。"',
         '"Klimaatweek は固有名詞だから大文字。"'),
        ('"een は単数：een boom、複数はそのまま bomen。"',
         '"een は単数、複数は bomen。"'),
        ("wy = 200 + eh + 18", "wy = 200 + eh + 8"),
        ("ly = wy + wh + 18", "ly = wy + wh + 8"),
    ]
    for old, new in subs:
        if old in t:
            t = t.replace(old, new)
        else:
            print(f"FIX1 P7 already applied (skip): {old[:40]!r}")
    open(p, "w", encoding="utf-8").write(t)
    print("FIX1 P7: invite 4->2 lines, disclosure labeled 編集部の例文 (3 lines), "
          "clinic notes 2->1 line x2, box gaps 18->8")

# ---------- FIX ROUND 2 (occlusion NEW flags on P1 after fix 1) ----------
def fix_round_2():
    # P1 word-of-the-week Japanese note ran 3 lines; its last line
    # (y=1897.6) fell inside the IN HET KORT box (top 1874) and overprinted
    # the box title. Core Chinese note is 2 lines ending y=1871.9.
    # Shorten the Japanese note to 2 lines (same meaning, tighter wording).
    p = os.path.join(HERE, "content12.py")
    t = open(p, encoding="utf-8").read()
    old = '"「気候」とは、私たちの周りの長期的な天気と自然のこと。気候週間は私たちの気候についての週だ。"'
    new = '"「気候」とは長期的な天気と自然のこと。気候週間は私たちの気候の週だ。"'
    if old in t:
        t = t.replace(old, new)
        open(p, "w", encoding="utf-8").write(t)
        print("FIX2 P1: word note 3->2 lines (last baseline back to 1871.9)")
    else:
        print("FIX2 P1 already applied (skip)")

# ---------- apply ----------
def main():
    zero = []
    for f, old, new in R:
        path = os.path.join(HERE, f)
        txt = open(path, encoding="utf-8").read()
        n = txt.count(old)
        if n == 0:
            zero.append((f, old[:70]))
        txt = txt.replace(old, new)
        open(path, "w", encoding="utf-8").write(txt)
        print(f"{f}: {n}x {old[:60]!r}")
    print("TOTAL replacements:", len(R))
    fix_round_1()
    fix_round_2()
    if zero:
        print("ZERO-MATCH replacements (must be adjudicated):")
        for f, old in zero:
            print("  ZERO", f, repr(old))

if __name__ == "__main__":
    main()
