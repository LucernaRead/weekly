# -*- coding: utf-8 -*-
"""PT x JA fan-out transform for W45 (VOL.2).

Run ONCE on a fresh copy of hidden_files/weekly-report-w45-pt-build
(with svglib.py already replaced by the canonical JA svglib from the
W43 PT x JA build, md5 d73e23b365676c3618d7e060b835eb4d — the
canonical file itself is NEVER edited):
  1. cp -r weekly-report-w45-pt-build -> weekly-report-w45-pt-ja-build
     (excluding __pycache__); cp W43 PT-JA svglib.py over svglib.py
  2. python3 transform.py   (repoints OUT/BASE/PDF names + rewrites ONLY
     the explanation layer from Chinese into Japanese; Portuguese text is
     never touched — every replacement below is a Chinese-containing
     literal, a bilingual furniture line, or a P8 translation re-aim)
  3. <tools/venv>/python run.py && <tools/venv>/python render.py

Rules baked in (W43 PT x JA shipped precedent wins over README #20
generalisation wherever they differ):
  - gloss prefix "解説 — " (W43 PT-JA bslib4 line 197)
  - badge replaces the P1 strapline IN PLACE at y=372, 19.5pt bold BRICK
    (W43 PT-JA p1-capa.svg: x=975 y=372 19.5pt weight-700 #a4553a)
  - footer "A Lucerna · ポルトガル語週刊 VOL.2 · 本文はポルトガル語 · 解説は日本語"
  - page line "{n} ページ（全 {total} ページ）"
  - P8 separator "— {pg} ページ —"; RESPOSTAS head "RESPOSTAS · 全解答と解説
    （1–8ページ）"; P8 right line W43 JA verbatim
  - P8 dash style "N. key — note" (core is dash style; JA keeps it, no
    parens introduced anywhere in P8 notes)
  - typ registry strings translated to the W43 JA forms (文の完成 /
    穴埋め選択 / 選択問題 / 文を作る / 正誤判断 / 翻訳 / 語と意味を結ぶ /
    作文) and the P8 writing check adapted to type == "作文" — typ is
    never rendered, but the JA family form is kept for consistency
  - instr strings translated (空所補充 / 文を作る / 翻訳 / 作文 / 正誤 /
    語と意味を結ぶ) — instr IS rendered
  - P7 gold labels "Página N" kept byte-identical (W43 JA precedent +
    core-identical labels rule)
  - P7 readers' corner: Portuguese disclosure sentence verbatim (frozen);
    Japanese note carries the EXPLICIT invitation (imperative
    送ってください + VOL.3 publication promise); Japanese disclosure is
    the equivalent sentence of disc_pt (3 facts: no real letters, no
    best P8 essay, example + deferral to VOL.3)
  - P8 translation re-aims (W43 KIT pattern): 137/138 PT->JA keys;
    139/140 stems JA->PT with Portuguese keys byte-identical
  - shared-kanji retentions (valid Japanese, NOT residue): 文化
    (CULTURA band), 花 (gloss item) — listed in the KIT word-level scan
  - Japanese grammar terms use Japanese forms, never Chinese forms:
    現在形 / 過去形 / 未来形 / 接続法未来形 / 命令形 / 複数形 (never
    现在时 / 过去时 / 将来时 / 虚拟式将来 / 祈使式 / 复数 as bare terms)
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
FILES = ["bslib4.py", "content12.py", "content34.py", "content56.py",
         "content7.py", "content8.py", "render.py"]

# (old, new) — applied to every file in FILES (replace-all). Sorted by
# length descending at apply time so longer literals win over substrings.
REPLACEMENTS = [
    # ---- repointing ----
    ("weekly-report-w45-pt-core", "weekly-report-w45-pt-ja"),
    ("A-Lucerna-VOL2.pdf", "A-Lucerna-VOL2-JA.pdf"),
    ("A-Lucerna-VOL2-web.pdf", "A-Lucerna-VOL2-JA-web.pdf"),
    ('if e_["type"] == "写作":', 'if e_["type"] == "作文":'),
    # ---- bslib4 furniture ----
    ("A Lucerna · 葡萄牙语周报 VOL.2 · LUCERNA PORTUGUESE WEEKLY",
     "A Lucerna · ポルトガル語週刊 VOL.2 · 本文はポルトガル語 · 解説は日本語"),
    ('f"第 {n} 版 / 共 {total} 版"', 'f"{n} ページ（全 {total} ページ）"'),
    ('("译注｜" + s', '("解説 — " + s'),
    # ---- typ registry (W43 JA forms; never rendered) ----
    ('"完成句子"', '"文の完成"'),
    ('"完形单选"', '"穴埋め選択"'),
    ('"单选"', '"選択問題"'),
    ('"造句"', '"文を作る"'),
    ('"判断对错"', '"正誤判断"'),
    ('"翻译"', '"翻訳"'),
    ('"词汇配对"', '"語と意味を結ぶ"'),
    ('"写作"', '"作文"'),
    # ---- instr (rendered) ----
    ('instr="填空"', 'instr="空所補充"'),
    ('instr="造句"', 'instr="文を作る"'),
    ('instr="翻译"', 'instr="翻訳"'),
    ('instr="写作"', 'instr="作文"'),
    ('instr="判断"', 'instr="正誤"'),
    ('instr="把词和释义配对"', 'instr="語と意味を結ぶ"'),
    # ---- P1 top furniture ----
    ("TODA SEMANA EM PORTUGUÊS · 每周一期 · 读巴西人正在读的葡萄牙语",
     "TODA SEMANA EM PORTUGUÊS · 毎週一号 · ブラジル人が読んでいるポルトガル語を読む"),
    ("葡 萄 牙 语 周 报 · VOL.2 · A SEMANA DO ENEM · FINADOS · O FUTEBOL DECIDE",
     "ポ ル ト ガ ル 語 週 刊 · VOL.2 · A SEMANA DO ENEM · FINADOS · O FUTEBOL DECIDE"),
    ('p.text(975, 372, "O JORNAL SEMANAL PARA APRENDER — O BRASIL DE VERDADE, EM PORTUGUÊS, DO BRASIL", 19, "sans", False, GREY, anchor="middle")',
     'p.text(975, 372, "ポルトガル語テキスト · 日本語の解説 — 日本語読者のための版", 19.5, "sans", True, BRICK, anchor="middle")'),
    ("全国高考周", "Enemの週"),
    ("11 月 2 日亡灵节连休 · 11 月 8 日高考第一天",
     "11月2日死者の日の連休 · 11月8日Enem初日"),
    ("A NOTÍCIA · 头条", "A NOTÍCIA · トップ記事"),
    ("讲解｜feriadão 连休长周末 · o portão 大门 · a redação 作文 · revisar 复习。",
     "解説 — feriadão 連休 · o portão 門 · a redação 小論文 · revisar 復習する。"),
    ("A SEMANA EM NÚMEROS · 数字", "A SEMANA EM NÚMEROS · 今週の数字"),
    ("12h — os portões abrem no domingo 8（周日 12 点开门）",
     "12h — os portões abrem no domingo 8（日曜日12時開門）"),
    ("13h — os portões fecham（13 点关门，过时不入）",
     "13h — os portões fecham（13時閉門、遅刻は入場不可）"),
    ("13h30–19h — a prova do dia 8（考试 13:30 至 19:00）",
     "13h30–19h — a prova do dia 8（試験13:30から19:00まで）"),
    ("5h30 — a duração da prova do dia 8（考试时长 5 小时半）",
     "5h30 — a duração da prova do dia 8（試験時間5時間半）"),
    ("AGORA VOCÊ · 即学即练", "AGORA VOCÊ · すぐ練習"),
    ("feriadão = 连休长周末", "feriadão = 連休"),
    ("portões = 大门（考场大门）", "portões = 門（試験会場の門）"),
    ("redação = 作文", "redação = 小論文"),
    ("13h30 开考（巴西利亚时间）", "13h30 試験開始（ブラジリア時間）"),
    ("19h 结束", "19h 終了"),
    ("revisar 现在时 eles 形式：revisam", "revisar 現在形 eles の形：revisam"),
    ("迟到不得入内：13 点后关门", "遅刻は入場不可：13時以降は閉門"),
    ("NESTA EDIÇÃO · 本期目录", "NESTA EDIÇÃO · 今号の目次"),
    ("“连休”：假期连着周末，一共三天。", "「連休」：休みが週末につながり、全部で3日間。"),
    ("EM POUCAS PALAVRAS · 快讯", "EM POUCAS PALAVRAS · 短報"),
    ("QUIZ RELÂMPAGO · 闪电问答", "QUIZ RELÂMPAGO · クイズ"),
    ("读头版，选出正确答案 · 答案见第 8 版",
     "トップ記事を読んで、正しい答えを選ぼう · 答えは8ページ"),
    ("连休从 10 月 31 日到 11 月 2 日", "連休は10月31日から11月2日まで"),
    ("13 点关门", "13時閉門"),
    ("第 1 天考作文、语言与人文", "初日は小論文・言語・人文科学"),
    ("次回合在 7 日和 8 日", "第2戦は7日と8日"),
    # ---- P2 ----
    ("VIDA · 生活", "VIDA · 暮らし"),
    ("PARA NÃO ERRAR · 口诀", "PARA NÃO ERRAR · 覚え方"),
    ("o feriadão 连休长周末 · o cemitério 墓园 · a vela 蜡烛 · o crisântemo 菊花 · a missa 弥撒 · conferir 核对。",
     "o feriadão 連休 · o cemitério 墓地 · a vela ろうそく · o crisântemo 菊 · a missa ミサ · conferir 確かめる。"),
    ("在你的国家，有纪念逝者的日子吗？那天家人们做什么？写两句寄来。",
     "あなたの国では、死者を偲ぶ日がありますか。その日、家族は何をしますか。2文を書いて送ってください。"),
    ("E VOCÊ? · 说说你自己", "E VOCÊ? · あなたは？"),
    ("OS HORÁRIOS DO DOMINGO 8 · 周日时间表", "OS HORÁRIOS DO DOMINGO 8 · 日曜日の時間表"),
    ("Um país, vários relógios · 一个国家，几个时区",
     "Um país, vários relógios · 一つの国、いくつもの時差"),
    ("周日 12 点开门", "日曜日12時開門"),
    ("13 点关门", "13時閉門"),
    ("13:30 开考", "13:30 試験開始"),
    ("19:00 结束", "19:00 終了"),
    ("EXERCÍCIOS · 第 2 版练习", "EXERCÍCIOS · 2ページの練習問題"),
    ("答案见第 8 版 · 题目可跨级混排，按题号找答案",
     "答えは8ページ · レベル混在の出題です。番号で答えを探してください"),
    ("读第 2 版文章，选出正确答案。", "2ページの記事を読んで、正しい答えを選んでください。"),
    ("亡灵节家人们去墓园献花", "死者の日、家族は墓地に花を供える"),
    ("确认卡显示考试地点", "確認カードに試験会場が載っている"),
    ("巴西没有夏令时，钟表不动", "ブラジルに夏時間はなく、時計は動かない"),
    ("补全动词的现在时形式。", "動詞の現在形を補ってください。"),
    ("ser 现在时 ela 形式：é", "ser 現在形 ela の形：é"),
    ("用第 1、2 版的数字填空。", "1・2ページの数字で空所を補ってください。"),
    ("12 点到 13 点 = 1 小时", "12時から13時 = 1時間"),
    ("13:30 至 19:00 = 5 个半小时", "13:30から19:00 = 5時間半"),
    ("5×60 + 30 = 330 分钟", "5×60 + 30 = 330分"),
    ("31 日、1 日、2 日 = 3 天", "31日、1日、2日 = 3日間"),
    ("feriadão=连着周末的假期 c", "feriadão=週末につながった休み c"),
    ("cemitério=墓碑所在的地方 b", "cemitério=墓石のある場所 b"),
    ("vela=点亮纪念的物品 d", "vela=偲んで灯すもの d"),
    ("crisântemo=亡灵节带去的花 a", "crisântemo=死者の日に持っていく花 a"),
    # ---- P3 ----
    ("A2 → B1 · Finados: o dia da memória · 亡灵节：怀念的日子",
     "A2 → B1 · Finados: o dia da memória · 死者の日：偲ぶ日"),
    ("o túmulo 墓碑 · a flor 花 · acender 点燃 · rezar 祈祷 · o silêncio 寂静 · a lembrança 怀念。",
     "o túmulo 墓石 · a flor 花 · acender 火をともす · rezar 祈る · o silêncio 静けさ · a lembrança 偲ぶこと。"),
    ("在你的文化里，人们怎样怀念逝者？写两句寄来。",
     "あなたの文化では、人々はどのように死者を偲びますか。2文を書いて送ってください。"),
    ("EXERCÍCIOS · 第 3 版练习", "EXERCÍCIOS · 3ページの練習問題"),
    ("读第 3 版文章，选出正确答案。", "3ページの記事を読んで、正しい答えを選んでください。"),
    ("亡灵节是怀念与安静的日子", "死者の日は偲びと静けさの日"),
    ("家人们带花去墓园，主要是菊花", "家族は墓地に花を持っていく、主に菊"),
    ("教堂和墓园整天都有弥撒", "教会と墓地では一日中ミサがある"),
    ("万圣节在 10 月 31 日周六", "ハロウィーンは10月31日土曜日"),
    ("怀念是继续亲近的方式", "偲ぶことは近くにい続ける方法"),
    ("用方框里的词填空。", "枠内の語を使って空所を補ってください。"),
    ("túmulo = 墓碑", "túmulo = 墓石"),
    ("vela = 蜡烛", "vela = ろうそく"),
    ("crisântemo = 菊花", "crisântemo = 菊"),
    ("missa = 弥撒", "missa = ミサ"),
    ("silêncio = 寂静", "silêncio = 静けさ"),
    ("lembrança = 怀念", "lembrança = 偲ぶこと"),
    ("用过去时（pretérito perfeito）补全。", "過去形（pretérito perfeito）で補ってください。"),
    ("visitar 过去时 elas 形式：visitaram", "visitar 過去形 elas の形：visitaram"),
    ("levar 过去时 elas 形式：levaram", "levar 過去形 elas の形：levaram"),
    ("ser 过去时 ele 形式：foi", "ser 過去形 ele の形：foi"),
    ("viver 过去时 ele 形式：viveu", "viver 過去形 ele の形：viveu"),
    ("把词组成正确的句子。", "語を並べて正しい文を作ってください。"),
    ("主语 + é + 表语", "主語 + é + 補語"),
    ("主语 + 动词 + 宾语 + 地点", "主語 + 動詞 + 目的語 + 場所"),
    ("主语 + 动词 + 宾语", "主語 + 動詞 + 目的語"),
    # ---- P4 ----
    ("ESPORTE · 体育", "ESPORTE · スポーツ"),
    ("NÍVEL B1 · O futebol da semana · 足球之周", "NÍVEL B1 · O futebol da semana · サッカーの週"),
    ("a ida 首回合 · a volta 次回合 · o finalista 决赛球队 · a decisão 决战 · a rodada 轮次。",
     "a ida 第1戦 · a volta 第2戦 · o finalista 決勝進出チーム · a decisão 決戦 · a rodada 節。"),
    ("你在巴西杯支持哪支球队？写两句寄来。",
     "ブラジルカップではどのチームを応援しますか。2文を書いて送ってください。"),
    ("A SEMANA DO FUTEBOL · 足球周历", "A SEMANA DO FUTEBOL · 今週のサッカー日程"),
    ("EXERCÍCIOS · 第 4 版练习", "EXERCÍCIOS · 4ページの練習問題"),
    ("读第 4 版文章，选出正确答案。", "4ページの記事を読んで、正しい答えを選んでください。"),
    ("次回合米内罗竞技 × 格雷米奥在周六 7 日 18 点",
     "第2戦アトレチコMG × グレミオは土曜日7日18時"),
    ("瓦斯科 × 帕尔梅拉斯次回合在周日 8 日 17 点，圣雅努阿里奥",
     "ヴァスコ × パルメイラス第2戦は日曜日8日17時、サン・ジャヌアリオ"),
    ("首回合在 11 月 1 日周日", "第1戦は11月1日日曜日"),
    ("第 34 轮周一到周五每天都有比赛", "第34節は月曜日から金曜日まで毎日試合がある"),
    ("两回合总比分胜者进决赛", "2戦合計の勝者が決勝へ進む"),
    ("finalista=进决赛的球队 b", "finalista=決勝へ進むチーム b"),
    ("ida=对决的第一场 c", "ida=対戦の第1戦 c"),
    ("volta=对决的第二场 a", "volta=対戦の第2戦 a"),
    ("rodada=一轮比赛 d", "rodada=1節の試合 d"),
    ("用括号里正确的比较形式填空。", "かっこ内の正しい比較の形で空所を補ってください。"),
    ("次回合决定决赛名额：mais", "第2戦が決勝進出を決める：mais"),
    ("第 34 轮周一到周五都有比赛：mais", "第34節は月曜日から金曜日まで試合がある：mais"),
    ("把句子补全成过去时（pretérito perfeito）。",
     "文を過去形（pretérito perfeito）で完成させてください。"),
    ("ser 过去时复数：foram", "ser 過去形複数：foram"),
    ("receber 过去时 ele 形式：recebeu", "receber 過去形 ele の形：recebeu"),
    ("começar 过去时 ela 形式：começou", "começar 過去形 ela の形：começou"),
    ("chegar 过去时 eles 形式：chegaram", "chegar 過去形 eles の形：chegaram"),
    # ---- P5 ----
    ("JOVENS · 青年", "JOVENS · 若者"),
    ("NÍVEL B1 · A reta final dos jovens · 冲刺周：年轻人的最后一周",
     "NÍVEL B1 · A reta final dos jovens · ラストスパートの週：若者の最後の一週間"),
    ("1. Confira o Cartão de Confirmação do Enem（核对高考确认卡）",
     "1. Confira o Cartão de Confirmação do Enem（Enemの確認カードを確かめる）"),
    ("2. Revise um pouco por dia, sem maratona（每天复习一点，不搞突击）",
     "2. Revise um pouco por dia, sem maratona（毎日少しずつ復習し、詰め込みはしない）"),
    ("3. Durma bem na véspera da prova（考前一晚睡好）",
     "3. Durma bem na véspera da prova（試験前夜はよく眠る）"),
    ("4. Separe documento e caneta preta no dia anterior（提前一天备好证件和黑笔）",
     "4. Separe documento e caneta preta no dia anterior（前日に身分証と黒ペンを用意する）"),
    ("5. Domingo 8: chegue antes das 12h（周日 8 日：12 点前到达）",
     "5. Domingo 8: chegue antes das 12h（日曜日8日：12時前に着く）"),
    ("a reta final 最后冲刺 · a véspera 前夕 · a maratona 突击马拉松 · separar 准备好 · a cabeça 头脑、状态。",
     "a reta final ラストスパート · a véspera 前夜 · a maratona 詰め込み勉強 · separar 用意する · a cabeça 頭、心の状態。"),
    ("重要考试前一晚，你的计划是复习还是休息？写两句寄来。",
     "大事な試験の前夜、復習しますか、休息しますか。2文を書いて送ってください。"),
    ("EXERCÍCIOS · 第 5 版练习", "EXERCÍCIOS · 5ページの練習問題"),
    ("读第 5 版文章，选出正确答案。", "5ページの記事を読んで、正しい答えを選んでください。"),
    ("冲刺周在 11 月 8 日周日结束", "ラストスパートの週は11月8日日曜日に終わる"),
    ("每天复习一点", "毎日少しずつ復習する"),
    ("提前一天备好证件和黑笔", "前日に身分証と黒ペンを用意する"),
    ("第 2 天考自然科学与数学", "第2日は自然科学と数学"),
    ("11 月 3 日周二各州议会结束休会", "11月3日火曜日、各州議会が休会を終える"),
    ("用方框里的词填空。注意：有的词要变成复数。",
     "枠内の語を使って空所を補ってください。注意：複数形に変える語もあります。"),
    ("reta final = 最后冲刺阶段", "reta final = ラストスパートの時期"),
    ("inscrito 配合复数：inscritos", "inscrito 複数への一致：inscritos"),
    ("véspera = 前夕", "véspera = 前夜"),
    ("maratona = 突击马拉松", "maratona = 詰め込み勉強"),
    ("local = 地点", "local = 場所"),
    ("separar 祈使式：separe", "separar 命令形：separe"),
    ("用将来时（futuro do presente）补全。", "未来形（futuro do presente）で補ってください。"),
    ("fazer 将来时 eles 不规则形式：farão", "fazer 未来形 eles の不規則形：farão"),
    ("mostrar 将来时：mostrará", "mostrar 未来形：mostrará"),
    ("sair 将来时复数：sairão", "sair 未来形複数：sairão"),
    ("chegar 将来时：chegará", "chegar 未来形：chegará"),
    ("错：考前突击不是好计划，每天复习一点才好",
     "誤り：前夜の詰め込みは良い計画ではなく、毎日少しずつ復習するのが良い"),
    ("对：13:30 至 19:00", "正しい：13:30から19:00"),
    # ---- P6 ----
    ("APROFUNDAMENTO · 深读", "APROFUNDAMENTO · 深掘り"),
    ("NÍVEL B2 · O Enem explicado · 高考详解", "NÍVEL B2 · O Enem explicado · Enemを解説"),
    ("os portões 大门 · a segunda chamada 补考、第二次入场 · conferir 核对 · a correria 匆忙。",
     "os portões 門 · a segunda chamada 追試、2回目の入場 · conferir 確かめる · a correria あわただしさ。"),
    ("O DOMINGO 8 EM NÚMEROS · 11 月 8 日的数字 (horários oficiais do Inep)",
     "O DOMINGO 8 EM NÚMEROS · 11月8日の数字 (horários oficiais do Inep)"),
    ("EXERCÍCIOS · 第 6 版练习", "EXERCÍCIOS · 6ページの練習問題"),
    ("看上面两张图，选出正确答案。", "上の2つの図を見て、正しい答えを選んでください。"),
    ("大门开放 60 分钟", "門の開放は60分"),
    ("关门到开考之间等 30 分钟", "閉門から試験開始まで30分待つ"),
    ("考试 330 分钟", "試験は330分"),
    ("中午到 19 点 = 7 小时", "正午から19時 = 7時間"),
    ("图表数字是 Inep 官方时间", "図の数字はInepの公式時間"),
    ("高考分 8 日和 15 日两个周日", "Enemは8日と15日の2つの日曜日"),
    ("13 点后到场不得入内", "13時以降の到着は入場不可"),
    ("根据句子意思，补全正确的动词形式。",
     "文の意味に合わせて、正しい動詞の形を補ってください。"),
    ("将来时：começará", "未来形：começará"),
    ("quem + 虚拟式将来：chegar", "quem + 接続法未来形：chegar"),
    ("现在时：fecham", "現在形：fecham"),
    ("现在时：pede", "現在形：pede"),
    ("用方框里的词填空：portões · segunda chamada · local · conferir",
     "枠内の語で空所を補ってください：portões · segunda chamada · local · conferir"),
    ("portões = 大门", "portões = 門"),
    ("segunda chamada = 补考、第二次入场", "segunda chamada = 追試、2回目の入場"),
    ("祈使式：confira", "命令形：confira"),
    # ---- P7 ----
    ("LÍNGUA · 语言", "LÍNGUA · ことば"),
    ("聚焦语言 · Três níveis, três ferramentas · 三个级别，三件工具",
     "ことばに注目 · Três níveis, três ferramentas · 3つのレベル、3つの道具"),
    ("提问句：que horas（几点）+ 动词；onde fica 问地点；conferir 的 eu 形式不规则：confiro",
     "疑問文：que horas（何時）+ 動詞；onde fica は場所を尋ねる；conferir の eu の形は不規則：confiro"),
    ("conferir：eu → confiro（不规则）", "conferir：eu → confiro（不規則）"),
    ("onde 问地点", "onde は場所を尋ねる"),
    ("讲一周的事用过去时（pretérito perfeito）；revisar 规则（revisei）；chegar/dormir 的过去时注意重音。",
     "一週間のことを話すには過去形（pretérito perfeito）；revisar は規則変化（revisei）；chegar/dormir の過去形はアクセントに注意。"),
    ("revisar 过去时：revisei", "revisar 過去形：revisei"),
    ("chegar 过去时：chegou", "chegar 過去形：chegou"),
    ("dormir 过去时：dormiu", "dormir 過去形：dormiu"),
    ("chegaram 是 chegar 的过去时复数", "chegaram は chegar の過去形複数"),
    ("quando、se、quem 后用虚拟式将来：tiver、for、chegar（周日假设）。",
     "quando、se、quem の後ろは接続法未来形：tiver、for、chegar（日曜日の仮定）。"),
    ("quem + 虚拟式将来：tiver", "quem + 接続法未来形：tiver"),
    ("quando + 虚拟式将来：chegar", "quando + 接続法未来形：chegar"),
    ("se + ser 的虚拟式将来：for", "se + ser の接続法未来形：for"),
    ("quando + 未来 → 虚拟式将来 for", "quando + 未来 → 接続法未来形 for"),
    ("高考用黑笔，蓝笔不行。", "Enemは黒ペンで、青ペンはだめ。"),
    ("13 点关门，13:30 到就晚了。", "13時閉門、13:30に着いては遅い。"),
    ("考前一夜突击没用，睡好才记得住。", "詰め込みより、よく眠る方が覚えられる。"),
    ("连休是 10 月 31 日到 11 月 2 日，共三天。", "連休は10月31日〜11月2日の3日間。"),
    ("ERROS COMUNS · 常见错误", "ERROS COMUNS · よくある間違い"),
    ("feriadão = 连休长周末，共三天。", "feriadão = 連休、全部で3日間。"),
    ("A PALAVRA · 本周生词", "A PALAVRA · 今週の単語"),
    ("编辑部示例，非真实来信。真实来信请寄编辑部，下期见！",
     "編集部の作例です。あなたの手紙を送ってください。VOL.3に掲載します！"),
    ("编辑部说明：上期承诺的真实来信与最佳作文截稿时未收到，本期仍刊示例，顺延至下期。",
     "編集部注：VOL.1で約束した実際の手紙と最優秀作文は締切までに届かず、本号は例文を掲載し、約束はVOL.3へ延期します。"),
    ("FRASES DA SEMANA · 本周金句（逐字摘自本期文章）",
     "FRASES DA SEMANA · 今週のフレーズ（今号の記事から逐語引用）"),
    ("从连休到考试：高考周。", "連休から試験へ：Enemの週。"),
    ("许多人旅行、探亲、去墓园献花。", "多くの人が旅行し、家族を訪ね、墓地に花を供える。"),
    ("亡灵节是怀念的日子。", "死者の日は偲ぶ日。"),
    ("怀念是继续亲近的方式。", "偲ぶことは近くにい続ける方法。"),
    ("每一分值一个名次，每一球值一个故事。", "1点が順位に値し、1ゴールが物語に値する。"),
    ("睡得好，记得牢。", "よく眠ると、よく覚えていられる。"),
    ("先做容易的，再做难的。", "まず易しいものから、次に難しいものへ。"),
    ("核对确认卡、睡好、早到。", "確認カードを確かめ、よく眠り、早く着く。"),
    ("A PRÓXIMA SEMANA · 下期预告 (VOL.3)", "A PRÓXIMA SEMANA · 次号予告 (VOL.3)"),
    # ---- P8 ----
    ("AVALIAÇÃO E RESPOSTAS · 练习与答案", "AVALIAÇÃO E RESPOSTAS · 評価と解答"),
    ("第 8 版 · A grande prova da semana + todas as respostas",
     "8 ページ · A grande prova da semana + todas as respostas"),
    ("第 1 天在 11 月 8 日", "初日は11月8日"),
    ("亡灵节在 11 月 2 日", "死者の日は11月2日"),
    ("瓦斯科 × 帕尔梅拉斯次回合在 8 日", "ヴァスコ × パルメイラス第2戦は8日"),
    ("连休共 3 天", "連休は全部で3日間"),
    ("考试时长 5 个半小时", "試験時間は5時間半"),
    ("第 2 天在 11 月 15 日", "第2日は11月15日"),
    ("确认卡是高考的文件", "確認カードはEnemの書類"),
    ("米内罗竞技 × 格雷米奥次回合在 MRV 竞技场",
     "アトレチコMG × グレミオ第2戦はMRVアリーナ"),
    ("第 34 轮周一到周五都有比赛", "第34節は月曜日から金曜日まで試合がある"),
    ("亡灵节家人们带花", "死者の日、家族は花を持っていく"),
    ("万圣节在 10 月 31 日周六", "ハロウィーンは10月31日土曜日"),
    ("330 是考试的分钟数", "330は試験の分数"),
    ("亡灵节又称诸圣灵魂日", "死者の日はポルトガル語で諸聖霊魂日ともいう"),
    ("卢卡斯住在贝洛奥里藏特", "ルーカスはベロオリゾンテに住んでいる"),
    ("连休里他休息并每天复习一点", "連休中、彼は休み、毎日少しずつ復習する"),
    ("前一晚他备好证件和黑笔、早睡", "前夜、彼は身分証と黒ペンを用意し、早く寝る"),
    ("他 11 点到达考场", "彼は11時に試験会場に着く"),
    ("时间词在前", "時を表す語が前に来る"),
    ("疑问词组在句首", "疑問詞句が文頭に来る"),
    # P8 translation re-aims: 137/138 PT->JA keys; 139/140 JA stems, PT keys frozen
    ("11 月 8 日周日是高考的第一天。", "11月8日日曜日はEnemの初日です。"),
    ("对照第 6 版标题", "6ページの見出しと対照"),
    ("周日前核对确认卡。", "日曜日の前に確認カードを確かめよう。"),
    ("Confira = 请核对", "Confira = 確かめること"),
    ("“连休是 10 月 31 日到 11 月 2 日。” → ___",
     "「連休は10月31日から11月2日までです。」 → ___"),
    ("feriadão = 连休", "feriadão = 連休"),
    ("你到达时，请出示带照片的证件。 → ___",
     "「着いたら、写真付きの身分証を提示してください。」 → ___"),
    ("虚拟式将来 chegar + 祈使 apresente", "接続法未来形 chegar + 命令形 apresente"),
    ("feriadão=连着周末的假期 b", "feriadão=週末につながった休み b"),
    ("portão=考场入口 d", "portão=試験会場の入口 d"),
    ("reta final=考前最后一周 a", "reta final=試験前最後の一週間 a"),
    ("segunda chamada=关门后的再入场（高考没有） c",
     "segunda chamada=閉門後の再入場（Enemにはない） c"),
    ("documento com foto 带照片的证件", "documento com foto 写真付きの身分証"),
    ("seção = 考场分区（房间）", "seção = 試験会場の区画（部屋）"),
    ("大门 13 点关闭", "門は13時に閉まる"),
    ("考试 13:30 开始", "試験は13:30に始まる"),
    ("obrigado = 谢谢", "obrigado = ありがとう"),
    ("写作题（无唯一答案）；范文（{NWORDS} 词）见下。",
     "作文問題（唯一の答えはない）；模範文（{NWORDS} 語）は下記。"),
    ("（开放题，范文如下）", "（自由問題、模範文は下記）"),
    ("范文见本版 H 区（{NWORDS} 词）", "模範文は本ページ H 欄（{NWORDS} 語）"),
    ("RESPOSTAS · 参考答案 — 按版面分页排列，找到题号即可",
     "RESPOSTAS · 全解答と解説（1–8ページ）"),
    ("每题附一句中文简析 · 带 ✓ 的为范文题",
     "各問に日本語の一言解説 · ✓印は模範文のある問題"),
    ('f"— PÁGINA {pg} —"', 'f"— {pg} ページ —"'),
]

# NOTE: "13 点关门" is listed twice above (P1 quiz + P2 table share the
# same JA); replace-all makes the duplicate harmless. Same for
# "确认卡显示考试地点" (P2/P6/P8 share one JA).

def main():
    ordered = sorted(REPLACEMENTS, key=lambda p: -len(p[0]))
    # dedupe identical (old, new) pairs, keep first
    seen, uniq = set(), []
    for old, new in ordered:
        if (old, new) in seen:
            continue
        seen.add((old, new))
        uniq.append((old, new))
    for fname in FILES:
        path = os.path.join(HERE, fname)
        text = open(path, encoding="utf-8").read()
        orig = text
        for old, new in uniq:
            if old in text:
                text = text.replace(old, new)
        if text != orig:
            open(path, "w", encoding="utf-8").write(text)
            print(f"updated {fname}")
    # assertion pass: every old string must be gone from every file
    # (except strings intentionally kept: none — all olds are Chinese
    # or repoint literals that must vanish)
    missing = []
    for old, new in uniq:
        for fname in FILES:
            text = open(os.path.join(HERE, fname), encoding="utf-8").read()
            if old in text:
                missing.append((fname, old))
    if missing:
        print("STILL PRESENT (must be 0):")
        for fname, old in missing:
            print(f"  {fname}: {old!r}")
        raise SystemExit(1)
    print("transform OK: all", len(uniq), "replacements applied, 0 old strings remain")

if __name__ == "__main__":
    main()
