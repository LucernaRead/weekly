# -*- coding: utf-8 -*-
"""PT core (zh explanations) -> PT x JA fan-out transform for W46 VOL.3.

Run inside the already-copied build dir. Every replacement is an exact
literal match (longest strings first); missing literals warn. The final
pass asserts ZERO *Simplified-Chinese-only* residue is NOT applied here:
the JA explanation layer legitimately uses CJK characters (kanji/kana);
adjudication is via freeze diff (explanation-layer-only churn).
Frozen Portuguese text, the P7 example letter (lt), the PT disclosure
(disc_pt) and the P7 quote strings + page tags are never touched.
P1 subtitle (330) and badge (372) lines are replaced whole (size/color).
Subtitle size 36pt is measured (40pt overflows the page frame).
svglib.py is the W45 pt-ja JP-face + kinsoku build (copied, not edited).
P7 geometry keeps the core values (JA text is compact); P8 keeps the
core 13.5pt answers size; the P8 separator becomes Japanese.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))

def load(fn):
    with open(os.path.join(HERE, fn), encoding='utf-8') as f:
        return f.read()

def save(fn, txt):
    with open(os.path.join(HERE, fn), 'w', encoding='utf-8') as f:
        f.write(txt)

def sub(txt, old, new, fn=''):
    n = txt.count(old)
    assert n >= 1, f'{fn}: {old!r} not found'
    return txt.replace(old, new)

def line_replace(txt, anchor, newline, fn=''):
    lines = txt.split('\n')
    hits = [i for i, ln in enumerate(lines) if anchor in ln]
    assert len(hits) == 1, f'{fn}: anchor {anchor!r} hits {hits}'
    lines[hits[0]] = newline
    return '\n'.join(lines)

FILES = ['bslib4.py', 'content12.py', 'content34.py', 'content56.py',
         'content7.py', 'content8.py', 'render.py']

# ---------- 0. OUT / BASE repoint + print PDF name ----------
for fn in FILES:
    t = load(fn)
    if 'weekly-report-w46-pt-core' in t:
        t = t.replace('weekly-report-w46-pt-core', 'weekly-report-w46-pt-ja')
        save(fn, t)
t = load('render.py')
t = sub(t, 'A-Lucerna-VOL3.pdf', 'A-Lucerna-VOL3-JA.pdf', 'render.py')
save('render.py', t)

# ---------- 1. bslib4 furniture ----------
t = load('bslib4.py')
t = sub(t, 'A Lucerna · 葡萄牙语周报 VOL.3 · LUCERNA PORTUGUESE WEEKLY',
        'A Lucerna · ポルトガル語週刊 VOL.3 · 本文はポルトガル語 · 解説は日本語', 'bslib4.py')
t = sub(t, 'f"第 {n} 版 / 共 {total} 版"', 'f"{n} ページ（全 {total} ページ）"', 'bslib4.py')
t = sub(t, '("译注｜" + s', '("解説 — " + s', 'bslib4.py')
save('bslib4.py', t)

# ---------- 2. P1 masthead lines (whole-line) ----------
t = load('content12.py')
t = line_replace(t, 'p.text(975, 330,',
    'p.text(975, 330, "ポ ル ト ガ ル 語 週 刊 · VOL.3 · ENEM, DIA 2 · PROCLAMAÇÃO DA REPÚBLICA · O FUTEBOL DECIDE", 36, "serif", True, INK, anchor="middle")',
    'content12.py')
t = line_replace(t, 'p.text(975, 372,',
    'p.text(975, 372, "ポルトガル語テキスト · 日本語の解説 — 日本語読者のための版", 19.5, "sans", True, BRICK, anchor="middle")',
    'content12.py')
save('content12.py', t)

# ---------- 3. type / instr labels ----------
INSTR = [
    ('instr="造句"', 'instr="文を作る"'),
    ('instr="翻译"', 'instr="訳す"'),
    ('instr="判断"', 'instr="正しいか間違いか"'),
    ('instr="写作"', 'instr="書く"'),
    ('instr="填空"', 'instr="空欄を埋める"'),
    ('instr="把词和释义配对"', 'instr="言葉と意味を結ぶ"'),
]
TYP = [
    ('"完成句子"', '"文を完成させる"'),
    ('"词汇配对"', '"語彙のマッチング"'),
    ('"判断对错"', '"正誤判定"'),
    ('"完形单选"', '"空所補充"'),
    ('"单选"', '"選択問題"'),
    ('"造句"', '"文を作る"'),
    ('"翻译"', '"翻訳"'),
    ('"写作"', '"作文"'),
]
for fn in ['content12.py', 'content34.py', 'content56.py', 'content7.py', 'content8.py']:
    t = load(fn)
    for old, new in INSTR:
        if old in t:
            t = sub(t, old, new, fn=fn)
    for old, new in TYP:
        if old in t:
            t = sub(t, old, new, fn=fn)
    save(fn, t)

# ---------- 4. content replacements (global table, longest-first) ----------
REPL = [
    # bands
    ('NÍVEL A2 · Prova e feriado no mesmo domingo', 'レベル A2 · 試験と祝日が同じ日曜日'),
    ('A2 → B1 · Proclamação da República: 137 anos · 共和国宣言 137 周年', 'A2 → B1 · Proclamação da República：137 年'),
    ('NÍVEL B1 · O futebol da semana · 足球之周', 'レベル B1 · 今週のサッカー'),
    ('NÍVEL B1 · A última semana dos jovens · 最后一周：年轻人的冲刺', 'レベル B1 · 若者たちの最後の一週間'),
    ('NÍVEL B2 · O segundo domingo explicado · 第二个周日详解', 'レベル B2 · 第 2 の日曜日を解説'),
    ('聚焦语言 · Três níveis, três ferramentas · 三个级别，三件工具', 'Três níveis, três ferramentas · 3 つのレベル、3 つの道具'),
    ('第 8 版 · A grande prova da semana + todas as respostas', '8 ページ · 今週の大テスト + すべての解答'),
    # top strip / kickers
    ('TODA SEMANA EM PORTUGUÊS · 每周一期 · 读巴西人正在读的葡萄牙语', 'TODA SEMANA EM PORTUGUÊS · ブラジルが読むポルトガル語を、毎週'),
    ('A NOTÍCIA · 头条', 'A NOTÍCIA · トップ記事'),
    ('VIDA · 生活', 'VIDA · 生活'),
    ('CULTURA · 文化', 'CULTURA · 文化'),
    ('ESPORTE · 体育', 'ESPORTE · スポーツ'),
    ('JOVENS · 青年', 'JOVENS · 若者'),
    ('APROFUNDAMENTO · 深读', 'APROFUNDAMENTO · 深読み'),
    ('LÍNGUA · 语言', 'LÍNGUA · 言語'),
    ('AVALIAÇÃO E RESPOSTAS · 练习与答案', 'AVALIAÇÃO E RESPOSTAS · 評価と解答'),
    # P1
    ('高考第二天', 'ENEM 第 2 日'),
    ('11 月 15 日第二场考试 · 共和国宣言日假期', '11 月 15 日：第 2 の試験日 · 共和国宣言の祝日'),
    ('讲解｜a proclamação 宣布、宣告 · o feriado 假日 · a natureza 自然科学 · a matemática 数学。', 'キーワード | a proclamação = 宣言 · o feriado = 祝日 · a natureza = 自然科学 · a matemática = 数学。'),
    ('A SEMANA EM NÚMEROS · 数字', 'A SEMANA EM NÚMEROS · 数字で見る今週'),
    ('12h — os portões abrem no domingo 15（周日 12 点开门）', '12h — os portões abrem no domingo 15（日曜 12 時開門）'),
    ('13h — os portões fecham（13 点关门，过时不入）', '13h — os portões fecham（13 時閉門、遅刻は入場不可）'),
    ('13h30–18h30 — a prova do dia 15（考试 13:30 至 18:30）', '13h30–18h30 — a prova do dia 15（15 日の試験、13:30〜18:30）'),
    ('90 — as questões do dia 15: 45 + 45（90 道题：45 + 45）', '90 — as questões do dia 15: 45 + 45（90 問：45 + 45）'),
    ('AGORA VOCÊ · 即学即练', 'AGORA VOCÊ · さあ、あなたも'),
    ('proclamação = 宣布（共和国宣言）', 'proclamação = 宣言（共和国宣言）'),
    ('proclamação = 宣布（共和国宣言）。', 'proclamação = 宣言（共和国宣言）。'),
    ('feriado = 假日', 'feriado = 祝日'),
    ('portões = 大门（考场大门）', 'portões = 門（試験会場の門）'),
    ('18h30 结束', '18 時 30 分終了'),
    ('90 道题', '90 問'),
    ('fazer 现在时 eles 形式：fazem', 'fazer 現在形 eles 形：fazem'),
    ('迟到不得入内：13 点后关门', '13 時を過ぎると入場できない。'),
    ('NESTA EDIÇÃO · 本期目录', 'NESTA EDIÇÃO · 今号の目次'),
    ('EM POUCAS PALAVRAS · 快讯', 'EM POUCAS PALAVRAS · 短報'),
    ('QUIZ RELÂMPAGO · 闪电问答', 'QUIZ RELÂMPAGO · 速攻クイズ'),
    ('读头版，选出正确答案 · 答案见第 8 版', '1 面を読んで選ぼう · 解答は 8 ページ'),
    ('共和国宣言日在 11 月 15 日', '共和国宣言の日は 11 月 15 日'),
    ('13 点关门', '13 時に閉門'),
    ('第 2 天考自然科学与数学', '第 2 日は自然科学と数学'),
    ('18:30 结束', '18:30 終了'),
    # P2
    ('PARA NÃO ERRAR · 口诀', 'PARA NÃO ERRAR · 覚え方'),
    ('a proclamação 宣布 · o feriado 假日 · a natureza 自然科学 · a matemática 数学 · conferir 核对 · a escala 排班。', 'a proclamação = 宣言 · o feriado = 祝日 · a natureza = 自然科学 · a matemática = 数学 · conferir = 確認する · a escala = 勤務表。'),
    ('在你的国家，落在周日的假日会在周一补休吗？写两句寄来。', 'あなたの国では、日曜日に重なった祝日は月曜日に振り替えられますか。2 文書いて送ってください。'),
    ('E VOCÊ? · 说说你自己', 'E VOCÊ? · あなたは？'),
    ('OS HORÁRIOS DO DOMINGO 15 · 周日时间表', 'OS HORÁRIOS DO DOMINGO 15 · 15 日（日）の時間割'),
    ('Um país, vários relógios · 一个国家，几个时区', 'Um país, vários relógios · 一つの国、いくつもの時計'),
    ('周日 12 点开门', '日曜 12 時開門'),
    ('13:30 开考', '13:30 試験開始'),
    ('EXERCÍCIOS · 第 2 版练习', 'EXERCÍCIOS · 2 ページの練習'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', '解答は 8 ページ · レベル混合 — 番号で探すこと'),
    ('读第 2 版文章，选出正确答案。', '2 ページの記事を読んで正しい答えを選ぼう。'),
    ('假日落在周日，周一不补休', '祝日が日曜日に重なり、月曜の振替なし'),
    ('确认卡显示考试地点', '確認カードに試験会場が書かれている'),
    ('巴西没有夏令时，钟表不动', 'ブラジルに夏時間はない。時計は動かない'),
    ('补全动词的现在时形式。', '動詞の現在形で補おう。'),
    ('用第 1、2 版的数字填空。', '1・2 ページの数字で埋めよう。'),
    ('12 点到 13 点 = 1 小时', '12 時から 13 時 = 1 時間'),
    ('13:30 至 18:30 = 5 小时', '13:30 から 18:30 = 5 時間'),
    ('5×60 = 300 分钟', '5×60 = 300 分'),
    ('proclamação=宣布一个变化 b', 'proclamação = 変化を宣言すること (b)'),
    ('feriado=法律规定的休息日 c', 'feriado = 法律で定められた休日 (c)'),
    ('natureza=生命、物理与化学的科学 d', 'natureza = 生命・物理・化学の科学 (d)'),
    ('matemática=数字与图形的科学 a', 'matemática = 数と図形の科学 (a)'),
    ('把词和释义配对', '言葉と意味を結ぼう'),
]
REPL += [
    # P3
    ('a monarquia 君主制 · a república 共和国 · o marechal 元帅 · o exílio 流亡 · o governo 政府 · a lei 法律。', 'a monarquia = 君主制 · a república = 共和国 · o marechal = 元帥 · o exílio = 亡命 · o governo = 政府 · a lei = 法律。'),
    ('在你的国家，有纪念共和国建立的假日吗？写两句寄来。', 'あなたの国には、共和国の建国を記念する祝日がありますか。2 文書いて送ってください。'),
    ('EXERCÍCIOS · 第 3 版练习', 'EXERCÍCIOS · 3 ページの練習'),
    ('读第 3 版文章，选出正确答案。', '3 ページの記事を読んで正しい答えを選ぼう。'),
    ('共和国宣言在 1889 年 11 月 15 日', '共和国宣言は 1889 年 11 月 15 日'),
    ('德奥多罗成为巴西第一任总统', 'デオドロがブラジル初代大統領になった'),
    ('全国性假日，任何城市都不能改为工作日', '全国的な祝日。どの都市も平日に変えられない'),
    ('2026 年假日落在周日', '2026 年、祝日は日曜日に重なる'),
    ('共和国里总统由选举产生、任期有限', '共和国では大統領は選挙で選ばれ、任期に限りがある'),
    ('用方框里的词填空。', '枠の中の言葉で埋めよう。'),
    ('monarquia = 君主制', 'monarquia = 君主制'),
    ('república = 共和国', 'república = 共和国'),
    ('marechal = 元帅', 'marechal = 元帥'),
    ('exílio = 流亡', 'exílio = 亡命'),
    ('governo = 政府', 'governo = 政府'),
    ('lei = 法律', 'lei = 法律'),
    ('用过去时（pretérito perfeito）补全。', '過去形（pretérito perfeito）で補おう。'),
    ('tomar 过去时 elas 形式：tomaram', 'tomar 過去形 elas 形：tomaram'),
    ('acabar 过去时 ela 形式：acabou', 'acabar 過去形 ela 形：acabou'),
    ('ser 过去时 ele 形式：foi', 'ser 過去形 ele 形：foi'),
    ('assumir 过去时 ele 形式：assumiu', 'assumir 過去形 ele 形：assumiu'),
    ('把词组成正确的句子。', '言葉を正しい順番に並べよう。'),
    ('主语 + é + 表语', '主語 + é + 補語'),
    ('主语 + 动词 + 表语', '主語 + 動詞 + 補語'),
    ('主语 + 动词 + 宾语 + 时间', '主語 + 動詞 + 目的語 + 時間'),
    # P4
    ('a ida 首回合 · a volta 次回合 · o gol 进球 · o pênalti 点球 · a pausa 休整期 · o amistoso 友谊赛。', 'a ida = 第 1 戦 · a volta = 第 2 戦 · o gol = ゴール · o pênalti = PK · a pausa = 中断期間 · o amistoso = 親善試合。'),
    ('你在巴西杯支持哪支球队？谁能进决赛？写两句寄来。', 'コパ・ド・ブラジルではどのチームを応援しますか。決勝に進むのはどこでしょう。2 文書いて送ってください。'),
    ('A SEMANA DO FUTEBOL · 足球周历', 'A SEMANA DO FUTEBOL · サッカー週間'),
    ('EXERCÍCIOS · 第 4 版练习', 'EXERCÍCIOS · 4 ページの練習'),
    ('读第 4 版文章，选出正确答案。', '4 ページの記事を読んで正しい答えを選ぼう。'),
    ('首回合格雷米奥 2 比 0 战胜米内罗竞技', '第 1 戦、グレミオがアトレチコ MG に 2 対 0 で勝利'),
    ('帕尔梅拉斯 1 比 0 战胜瓦斯科，毛里西奥进球', 'パルメイラスがヴァスコに 1 対 0 で勝利、マウリシオが得点'),
    ('次回合米内罗竞技 × 格雷米奥在周六 7 日 18 点', '第 2 戦アトレチコ MG × グレミオは土曜 7 日 18 時'),
    ('决赛 12 月 6 日单场，在马内·加林查', '決勝は 12 月 6 日の一発勝負、マネ・ガリンシャで'),
    ('第 35 轮本周只有一场：米拉索尔 × 米内罗竞技', '第 35 節は今週 1 試合だけ：ミラソル × アトレチコ MG'),
    ('gol=射入球网的得分 b', 'gol = ネットに入れた得点 (b)'),
    ('ida=对决的第一场 d', 'ida = 対決の第 1 戦 (d)'),
    ('volta=对决的第二场 a', 'volta = 対決の第 2 戦 (a)'),
    ('pênalti=十一米点的罚球 c', 'pênalti = 11m 地点からのシュート (c)'),
    ('用括号里正确的比较形式填空。', 'かっこ内の正しい比較の形で埋めよう。'),
    ('5 小时 < 5.5 小时：menos', '5 時間 < 5.5 時間：menos'),
    ('把句子补全成过去时（pretérito perfeito）。', '文を過去形（pretérito perfeito）で完成させよう。'),
    ('vencer 过去时 ele 形式：venceu', 'vencer 過去形 ele 形：venceu'),
    ('marcar 过去时 eles 形式：marcaram', 'marcar 過去形 eles 形：marcaram'),
    ('marcar 过去时 ele 形式：marcou', 'marcar 過去形 ele 形：marcou'),
    ('convocar 过去时 ele 形式：convocou', 'convocar 過去形 ele 形：convocou'),
    ('ser 过去时复数：foram', 'ser 過去形複数：foram'),
    # P5
    ('1. Confira o Cartão de Confirmação do Enem（核对高考确认卡）', '1. Confira o Cartão de Confirmação do Enem（Enem 確認カードを確認）'),
    ('2. Revise um pouco por dia: Natureza e Matemática（每天复习一点：自然科学与数学）', '2. Revise um pouco por dia: Natureza e Matemática（毎日少し復習：自然科学と数学）'),
    ('3. Durma bem na véspera da prova（考前一晚睡好）', '3. Durma bem na véspera da prova（試験前夜はよく眠る）'),
    ('4. Separe documento e caneta preta no dia anterior（提前一天备好证件和黑笔）', '4. Separe documento e caneta preta no dia anterior（前日に身分証と黒ペンを用意）'),
    ('5. Domingo 15: chegue antes das 12h（周日 15 日：12 点前到达）', '5. Domingo 15: chegue antes das 12h（日曜 15 日：12 時前に到着）'),
    ('a natureza 自然科学 · a matemática 数学 · a maratona 突击马拉松 · a véspera 前夕 · comparar 比较价格 · a cabeça 头脑、状态。', 'a natureza = 自然科学 · a matemática = 数学 · a maratona = 詰め込みマラソン · a véspera = 前夜 · comparar = 値段を比べる · a cabeça = 頭、調子。'),
    ('重要考试前一晚，你是复习到很晚还是早睡？写两句寄来。', '大事な試験の前夜、遅くまで復習しますか、それとも早く寝ますか。2 文書いて送ってください。'),
    ('EXERCÍCIOS · 第 5 版练习', 'EXERCÍCIOS · 5 ページの練習'),
    ('读第 5 版文章，选出正确答案。', '5 ページの記事を読んで正しい答えを選ぼう。'),
    ('最后一周在 11 月 15 日周日结束', '最後の一週間は 11 月 15 日（日）に終わる'),
    ('每天复习一点', '毎日少し復習'),
    ('提前一天备好证件和黑笔', '前日に身分証と黒ペンを用意'),
    ('黑五在 11 月 27 日', 'ブラックフライデーは 11 月 27 日'),
    ('11 月 14 日周六巴西 × 日本 7:15', '11 月 14 日（土）ブラジル × 日本 7:15'),
    ('用方框里的词填空。注意：有的词要变成复数。', '枠の中の言葉で埋めよう。注意：複数形にする言葉がある。'),
    ('última semana = 最后一周', 'última semana = 最後の一週間'),
    ('inscrito 配合复数：inscritos', 'inscrito は複数形に合わせる：inscritos'),
    ('véspera = 前夕', 'véspera = 前夜'),
    ('maratona = 突击马拉松', 'maratona = 詰め込みマラソン'),
    ('local = 地点', 'local = 場所'),
    ('separar 祈使式：separe', 'separar 命令形：separe'),
    ('用将来时（futuro do presente）补全。', '未来形（futuro do presente）で補おう。'),
    ('fazer 将来时 eles 不规则形式：farão', 'fazer 未来形 eles 不規則形：farão'),
    ('mostrar 将来时：mostrará', 'mostrar 未来形：mostrará'),
    ('sair 将来时复数：sairão', 'sair 未来形複数：sairão'),
    ('chegar 将来时：chegará', 'chegar 未来形：chegará'),
    ('错：考前突击不是好计划，每天复习一点才好', '誤り：前夜の詰め込みは良い計画ではない。毎日少しずつが良い'),
    ('对：13:30 至 18:30', '正しい：13:30 から 18:30'),
    # P6
    ('os portões 大门 · a segunda chamada 补考、第二次入场 · conferir 核对 · a correria 匆忙。', 'os portões = 門 · a segunda chamada = 追試・2 度目の入場 · conferir = 確認する · a correria = あわただしさ。'),
    ('O DOMINGO 15 EM NÚMEROS · 11 月 15 日的数字 (horários oficiais do Inep)', 'O DOMINGO 15 EM NÚMEROS · 11 月 15 日の数字（Inep 公式時間）'),
    ('EXERCÍCIOS · 第 6 版练习', 'EXERCÍCIOS · 6 ページの練習'),
    ('看上面两张图，选出正确答案。', '上の 2 つの図を見て正しい答えを選ぼう。'),
    ('大门开放 60 分钟', '門は 60 分間開いている'),
    ('关门到开考之间等 30 分钟', '閉門から試験開始までの待ち時間は 30 分'),
    ('考试 300 分钟', '試験は 300 分'),
    ('中午到 18:30 = 6 个半小时', '正午から 18:30 = 6 時間半'),
    ('图表数字是 Inep 官方时间', '図の数字は Inep の公式時間'),
    ('高考分 8 日和 15 日两个周日', 'Enem は 8 日と 15 日の 2 つの日曜日に分かれる'),
    ('13 点后到场不得入内', '13 時を過ぎると入場できない'),
    ('根据句子意思，补全正确的动词形式。', '文の意味に合う正しい動詞の形で補おう。'),
    ('将来时：começará', '未来形：começará'),
    ('quem + 虚拟式将来：chegar', 'quem + 未来接続法：chegar'),
    ('现在时：fecham', '現在形：fecham'),
    ('现在时：pede', '現在形：pede'),
    ('用方框里的词填空：portões · segunda chamada · local · conferir', '枠の中の言葉で埋めよう：portões · segunda chamada · local · conferir'),
    ('portões = 大门', 'portões = 門'),
    ('segunda chamada = 补考、第二次入场', 'segunda chamada = 追試・2 度目の入場'),
    ('祈使式：confira', '命令形：confira'),
    # P7
    ('提问句：que horas（几点）+ 动词；onde fica 问地点；conferir 的 eu 形式不规则：confiro', '疑問文：que horas（何時）+ 動詞。onde fica は場所を尋ねる。conferir の eu 形は不規則：confiro。'),
    ('conferir：eu → confiro（不规则）', 'conferir：eu → confiro（不規則）'),
    ('onde 问地点', 'onde は場所を尋ねる'),
    ('讲一周的事用过去时（pretérito perfeito）；vencer 规则（venceu）；marcar/chegar/dormir 的过去时注意重音。', '一週間の出来事は過去形（pretérito perfeito）で語る。vencer は規則的（venceu）。marcar・chegar・dormir の過去形のアクセントに注意。'),
    ('vencer 过去时：venceu', 'vencer 過去形：venceu'),
    ('marcar 过去时：marcou', 'marcar 過去形：marcou'),
    ('chegar 过去时：chegou', 'chegar 過去形：chegou'),
    ('venceram 是 vencer 的过去时复数', 'venceram は vencer の過去形複数'),
    ('quando、se、quem 后用虚拟式将来：tiver、for、chegar（周日假设）。', 'quando・se・quem の後ろは未来接続法：tiver・for・chegar（日曜日の仮定の文法）。'),
    ('quem + 虚拟式将来：tiver', 'quem + 未来接続法：tiver'),
    ('quando + 虚拟式将来：chegar', 'quando + 未来接続法：chegar'),
    ('se + ser 的虚拟式将来：for', 'se + ser の未来接続法：for'),
    ('quando + 未来 → 虚拟式将来 for', 'quando + 未来 → 未来接続法 for'),
    ('高考用黑笔，蓝笔不行。', '黒ペンのみ。青は不可。'),
    ('13 点关门，13:30 到就晚了。', '13 時閉門。13:30 着では遅い。'),
    ('15 日考试 18:30 结束，19 点是 8 日的时间。', '15 日の試験は 18:30 終了。19 時は 8 日の時間。'),
    ('ERROS COMUNS · 常见错误', 'ERROS COMUNS · よくある間違い'),
    ('proclamação = 宣布；1889 年君主制结束、共和国开始。', 'proclamação = 宣言。1889 年、君主制が終わり共和国が始まった。'),
    ('A PALAVRA · 本周生词', 'A PALAVRA · 今週の単語'),
    ('编辑部说明：上期（VOL.2）承诺的真实来信与最佳作文截稿时未收到，本期仍刊示例，顺延至下期（VOL.4）。', '編集部注：VOL.2 で約束した実際の手紙と最優秀作文は締切までに届かず、本号は例文を掲載し、約束は VOL.4 へ延期します。'),
    ('编辑部示例，非真实来信。真实来信请寄编辑部，下期见！', '編集部の作例です。あなたの手紙を送ってください。'),
    ('FRASES DA SEMANA · 本周金句（逐字摘自本期文章）', 'FRASES DA SEMANA · 今週の名文句（本号の記事から逐語引用）'),
    ('两个周日、一个假日：巴西迎来高考第二天。', '二つの日曜日、一つの祝日：ブラジルは Enem 第 2 日を迎える。'),
    ('考试和假日在同一天到来。', '試験と祝日が同じ日にやって来る。'),
    ('假日不改变时钟。', '祝日は時計を変えない。'),
    ('君主制结束了。', '君主制は終わった。'),
    ('谁能进巴西杯决赛？', 'コパ・ド・ブラジルの決勝に進むのは誰か。'),
    ('睡得好，记得牢。', 'よく眠れば、よく覚えられる。'),
    ('先做容易的，再做难的。', 'まずやさしい問題、次に難しい問題。'),
    ('核对确认卡、睡好、早到。', '確認カードを確かめ、よく眠り、早く着こう。'),
    ('A PRÓXIMA SEMANA · 下期预告 (VOL.4)', 'A PRÓXIMA SEMANA · 来週の予告 (VOL.4)'),
    # P8
    ('第 2 天在 11 月 15 日', '第 2 日は 11 月 15 日'),
    ('第 1 天在 11 月 8 日', '第 1 日は 11 月 8 日'),
    ('确认卡是高考的文件', '確認カードは Enem の書類'),
    ('共和国宣言日在 11 月 15 日', '共和国宣言の日は 11 月 15 日'),
    ('瓦斯科 × 帕尔梅拉斯次回合在 8 日', 'ヴァスコ × パルメイラスの第 2 戦は 8 日'),
    ('第二天共 90 道题', '第 2 日は全部で 90 問'),
    ('考试时长 5 小时', '試験時間は 5 時間'),
    ('米内罗竞技 × 格雷米奥次回合在 MRV 竞技场', 'アトレチコ MG × グレミオの第 2 戦は MRV アリーナ'),
    ('第 35 轮本周只有一场，在 14 日', '第 35 節は今週 1 試合だけ、14 日'),
    ('共和国宣言在 1889 年', '共和国宣言は 1889 年'),
    ('11.11 是促销日', '11.11 はセールの日'),
    ('300 是考试的分钟数', '300 は試験の分数'),
    ('德奥多罗是第一任总统', 'デオドロは初代大統領'),
    ('玛丽娜住在圣保罗', 'マリーナはサンパウロに住んでいる'),
    ('她每天复习一点自然科学', '彼女は毎日少し自然科学を復習する'),
    ('前一晚她备好证件和黑笔、早睡', '前夜、身分証と黒ペンを用意し、早く寝る'),
    ('她 11:30 到达考场', '彼女は 11:30 に試験会場に着く'),
    ('时间词在前', '時間の言葉が前に来る'),
    ('主语 + 动词 + 宾语 + 地点', '主語 + 動詞 + 目的語 + 場所'),
    ('疑问词组在句首', '疑問の語句が文頭に来る'),
    ('主语 + 动词 + 宾语', '主語 + 動詞 + 目的語'),
    ('11 月 15 日周日是高考的第二天。', '11 月 15 日（日）は Enem の第 2 日です。'),
    ('对照第 6 版标题', '6 ページの見出しと対照'),
    ('周日前核对确认卡。', '日曜日の前に確認カードを確かめよう。'),
    ('Confira = 请核对', 'Confira = 確認しよう'),
    ('“假日落在周日。” → ___', '「祝日は日曜日に重なる。」→ ___'),
    ('虚拟式将来 chegar + 祈使 apresente', '未来接続法 chegar + 命令形 apresente'),
    ('你到达时，请出示带照片的证件。 → ___', '着いたら、写真付きの身分証を提示してください。→ ___'),
    ('proclamação=宣布一个变化 b', 'proclamação = 変化を宣言すること (b)'),
    ('portão=考场入口 d', 'portão = 試験会場の入口 (d)'),
    ('república=1889 年后的国家形式 a', 'república = 1889 年以後の国家形態 (a)'),
    ('segunda chamada=关门后的再入场（高考没有） c', 'segunda chamada = 閉門後の再入場（Enem にはない）(c)'),
    ('documento com foto 带照片的证件', 'documento com foto = 写真付き身分証'),
    ('seção = 考场分区（房间）', 'seção = 試験室（区画）'),
    ('大门 13 点关闭', '門は 13 時に閉まる'),
    ('考试 18:30 结束', '試験は 18:30 に終わる'),
    ('obrigado = 谢谢', 'obrigado = ありがとう'),
    ('写作题（无唯一答案）；范文（{NWORDS} 词）见下。', '作文問題（唯一の答えなし）。模範文（{NWORDS} 語）は下記。'),
    ('（开放题，范文如下）', '（自由問題、模範文は下記）'),
    ('范文见本版 H 区（{NWORDS} 词）', '模範文は本ページ H 欄（{NWORDS} 語）'),
    ('RESPOSTAS · 参考答案 — 按版面分页排列，找到题号即可', 'RESPOSTAS · 解答 — ページごとに配列。番号を探そう'),
    ('每题附一句中文简析 · 带 ✓ 的为范文题', '各問に一言の解説付き · ✓ は作文問題'),
]

for fn, reps in [('content12.py', REPL), ('content34.py', REPL),
                 ('content56.py', REPL), ('content7.py', REPL), ('content8.py', REPL)]:
    seen, ordered = set(), []
    for old, new in reps:
        if old not in seen:
            seen.add(old); ordered.append((old, new))
    reps = sorted(ordered, key=lambda r: -len(r[0]))
    t = load(fn)
    for old, new in reps:
        if old in t:
            t = sub(t, old, new, fn=fn)
        else:
            print(f'WARN {fn}: not found (skipped): {old[:60]!r}')
    save(fn, t)

# ---------- 5. disclosure rename + word-box pad + P8 separator ----------
t = load('content7.py')
assert t.count('disc_cn') == 3, f"content7.py disc_cn count {t.count('disc_cn')}"
t = t.replace('disc_cn', 'disc_ja')
old_wh = 'len(wrap("proclamação = 宣言。1889 年、君主制が終わり共和国が始まった。", "sans", False, 20, CW - 44)) * 29 + 20'
assert t.count(old_wh) == 1, 'word-box pad line not found'
t = t.replace(old_wh, 'len(wrap("proclamação = 宣言。1889 年、君主制が終わり共和国が始まった。", "sans", False, 20, CW - 44)) * 29 + 30')
save('content7.py', t)

t = load('content8.py')
t = line_replace(t, 'af.para(f"— PÁGINA {pg} —"',
    '    af.para(f"— {pg} ページ —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)',
    'content8.py')
save('content8.py', t)

t = load('content12.py')
old_box = '    ("90 — as questões do dia 15: 45 + 45（90 問：45 + 45）", "serif", False, INK, 20, 1.35),\n])'
assert t.count(old_box) == 1, 'numbers box close not found'
t = t.replace(old_box, old_box[:-2] + '], tsize=20)')
save('content12.py', t)

# ---------- 6. verify: every REPL source literal is gone ----------
# JA explanations legitimately use kanji/kana; the check is that no
# Chinese source literal from the REPL table survives untranslated.
for fn in ['bslib4.py', 'content12.py', 'content34.py', 'content56.py', 'content7.py', 'content8.py']:
    t = load(fn)
    left = [old for old, _new in REPL if old != _new and old in t and old not in _new]
    assert not left, f'{fn}: untranslated literals remain: {left[:5]}'
    print(f'{fn}: all REPL literals translated OK')
print('TRANSFORM COMPLETE')
