# -*- coding: utf-8 -*-
"""W45 PT core (Simplified explanations) -> PT x ZH-TW fan-out, VOL.2.

Run inside the already-copied build dir (a copy of
hidden_files/weekly-report-w45-pt-build). Every replacement is an exact
literal match, longest strings first where one contains another, except
the line-anchored edits in step 5-6. Frozen Portuguese text, the P7
example letter (lt), the PT disclosure (disc_pt) and the P7 quote
strings + 'Pagina' tags are never touched.

Furniture follows the shipped W43 PT x ZH-TW edition
(files/weekly-report-pt-zh-tw), NOT the tools README generics and NOT
any W45 sibling: badge replaces the P1 y=372 line at 19.5pt bold BRICK
centered; footer 'A Lucerna . ZH-TW weekly VOL.2 . PT text . ZH-TW
explanations'; gloss prefix '譯注｜'; P8 separators '— 第 N 版 —';
P1 top strip and y=330 subtitle kept, in Traditional forms; the
explanation method is renamed bridge -> expl after the W43 pattern;
svglib switches SC face -> TC face (index, suffix, family names).
The explanation layer is written natively in Traditional Chinese for
Taiwan/Hong Kong readers (search -> 搜尋-style usage choices are made
per string below, not by a glyph table); Simplified-only glyphs must
not survive in the operative sources after this pass (checked by the
gates script, not by this file).
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))

def load(fn):
    with open(os.path.join(HERE, fn), encoding='utf-8') as f:
        return f.read()

def save(fn, txt):
    with open(os.path.join(HERE, fn), 'w', encoding='utf-8') as f:
        f.write(txt)

def sub(txt, old, new, expect=None, fn=''):
    n = txt.count(old)
    if expect is not None:
        assert n == expect, f'{fn}: {old!r} found {n}x, expected {expect}x'
    else:
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

# ---------- 0. OUT / BASE repoint ----------
for fn in FILES:
    t = load(fn)
    if 'weekly-report-w45-pt-core' in t:
        t = sub(t, 'weekly-report-w45-pt-core', 'weekly-report-w45-pt-zh-tw', fn=fn)
        save(fn, t)

# ---------- 1. bslib4 furniture (W43 PT x ZH-TW verbatim, VOL.2) ----------
t = load('bslib4.py')
t = sub(t, 'A Lucerna · 葡萄牙语周报 VOL.2 · LUCERNA PORTUGUESE WEEKLY',
        'A Lucerna · 葡萄牙語週報 VOL.2 · 正文葡萄牙語 · 講解繁體中文', 1, 'bslib4.py')
t = sub(t, '("译注｜" + s', '("譯注｜" + s', 1, 'bslib4.py')
t = sub(t, 'def bridge(self, s', 'def expl(self, s', 1, 'bslib4.py')
save('bslib4.py', t)

# ---------- 1b. bridge -> expl call sites (W43 rename) ----------
EXPECT_BRIDGE = {'content12.py': 4, 'content34.py': 7, 'content56.py': 6,
                 'content7.py': 3, 'content8.py': 1}
for fn, expect in EXPECT_BRIDGE.items():
    t = load(fn)
    t = sub(t, '.bridge(', '.expl(', expect, fn)
    save(fn, t)

# ---------- 2. svglib SC -> TC (W43 precedent, 4 spots) ----------
t = load('svglib.py')
t = sub(t, 'def _sc_index(', 'def _tc_index(', 1, 'svglib.py')
t = sub(t, 'endswith("SC")', 'endswith("TC")', 1, 'svglib.py')
t = sub(t, '_sc_index(p)', '_tc_index(p)', 1, 'svglib.py')
t = sub(t, 'Noto Serif CJK SC', 'Noto Serif CJK TC', 1, 'svglib.py')
t = sub(t, 'Noto Sans CJK SC', 'Noto Sans CJK TC', 1, 'svglib.py')
save('svglib.py', t)

# ---------- 3. explanation-layer mapping (longest first, all files) ----------
# Native Traditional wording per string. Shared-glyph strings (identical
# in both scripts, e.g. 完成句子 / 造句 / 填空 / 前夕) need no entry.
M = [
    # ---- P1 band / header ----
    ('TODA SEMANA EM PORTUGUÊS · 每周一期 · 读巴西人正在读的葡萄牙语',
     'TODA SEMANA EM PORTUGUÊS · 每週一期 · 讀巴西人正在讀的葡萄牙語'),
    ('葡 萄 牙 语 周 报 · VOL.2 · A SEMANA DO ENEM · FINADOS · O FUTEBOL DECIDE',
     '葡 萄 牙 語 週 報 · VOL.2 · A SEMANA DO ENEM · FINADOS · O FUTEBOL DECIDE'),
    ('11 月 2 日亡灵节连休 · 11 月 8 日高考第一天',
     '11 月 2 日亡靈節連休 · 11 月 8 日高考第一天'),
    ('全国高考周', '全國高考週'),
    ('讲解｜feriadão 连休长周末 · o portão 大门 · a redação 作文 · revisar 复习。',
     '講解｜feriadão 連休長週末 · o portão 大門 · a redação 作文 · revisar 複習。'),
    ('A SEMANA EM NÚMEROS · 数字', 'A SEMANA EM NÚMEROS · 數字'),
    ('12h — os portões abrem no domingo 8（周日 12 点开门）',
     '12h — os portões abrem no domingo 8（週日 12 點開門）'),
    ('13h — os portões fecham（13 点关门，过时不入）',
     '13h — os portões fecham（13 點關門，過時不入）'),
    ('13h30–19h — a prova do dia 8（考试 13:30 至 19:00）',
     '13h30–19h — a prova do dia 8（考試 13:30 至 19:00）'),
    ('5h30 — a duração da prova do dia 8（考试时长 5 小时半）',
     '5h30 — a duração da prova do dia 8（考試時長 5 個半小時）'),
    ('迟到不得入内：13 点后关门', '遲到不得入內：13 點後關門'),
    ('“连休”：假期连着周末，一共三天。', '「連休」：假期連著週末，一共三天。'),
    ('读头版，选出正确答案 · 答案见第 8 版', '讀頭版，選出正確答案 · 答案見第 8 版'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案',
     '答案見第 8 版 · 題目可跨級混排，按題號找答案'),
    ('E VOCÊ? · 说说你自己', 'E VOCÊ? · 說說你自己'),
    # ---- section heads / furniture labels ----
    ('A NOTÍCIA · 头条', 'A NOTÍCIA · 頭條'),
    ('AGORA VOCÊ · 即学即练', 'AGORA VOCÊ · 即學即練'),
    ('NESTA EDIÇÃO · 本期目录', 'NESTA EDIÇÃO · 本期目錄'),
    ('EM POUCAS PALAVRAS · 快讯', 'EM POUCAS PALAVRAS · 快訊'),
    ('QUIZ RELÂMPAGO · 闪电问答', 'QUIZ RELÂMPAGO · 閃電問答'),
    ('PARA NÃO ERRAR · 口诀', 'PARA NÃO ERRAR · 口訣'),
    ('OS HORÁRIOS DO DOMINGO 8 · 周日时间表', 'OS HORÁRIOS DO DOMINGO 8 · 週日時間表'),
    ('Um país, vários relógios · 一个国家，几个时区',
     'Um país, vários relógios · 一個國家，幾個時區'),
    ('A SEMANA DO FUTEBOL · 足球周历', 'A SEMANA DO FUTEBOL · 足球週曆'),
    ('ERROS COMUNS · 常见错误', 'ERROS COMUNS · 常見錯誤'),
    ('A PALAVRA · 本周生词', 'A PALAVRA · 本週生詞'),
    ('FRASES DA SEMANA · 本周金句（逐字摘自本期文章）',
     'FRASES DA SEMANA · 本週金句（逐字摘自本期文章）'),
    ('A PRÓXIMA SEMANA · 下期预告 (VOL.3)', 'A PRÓXIMA SEMANA · 下期預告 (VOL.3)'),
    ('AVALIAÇÃO E RESPOSTAS · 练习与答案', 'AVALIAÇÃO E RESPOSTAS · 練習與答案'),
    ('CULTURA · 文化', 'CULTURA · 文化'),
    ('ESPORTE · 体育', 'ESPORTE · 體育'),
    ('APROFUNDAMENTO · 深读', 'APROFUNDAMENTO · 深讀'),
    ('LÍNGUA · 语言', 'LÍNGUA · 語言'),
    ('A2 → B1 · Finados: o dia da memória · 亡灵节：怀念的日子',
     'A2 → B1 · Finados: o dia da memória · 亡靈節：懷念的日子'),
    ('NÍVEL B1 · O futebol da semana · 足球之周', 'NÍVEL B1 · O futebol da semana · 足球之週'),
    ('NÍVEL B1 · A reta final dos jovens · 冲刺周：年轻人的最后一周',
     'NÍVEL B1 · A reta final dos jovens · 衝刺週：年輕人的最後一週'),
    ('NÍVEL B2 · O Enem explicado · 高考详解', 'NÍVEL B2 · O Enem explicado · 高考詳解'),
    ('聚焦语言 · Três níveis, três ferramentas · 三个级别，三件工具',
     '聚焦語言 · Três níveis, três ferramentas · 三個級別，三件工具'),
    ('O DOMINGO 8 EM NÚMEROS · 11 月 8 日的数字 (horários oficiais do Inep)',
     'O DOMINGO 8 EM NÚMEROS · 11 月 8 日的數字 (horários oficiais do Inep)'),
    ('EXERCÍCIOS · 第 2 版练习', 'EXERCÍCIOS · 第 2 版練習'),
    ('EXERCÍCIOS · 第 3 版练习', 'EXERCÍCIOS · 第 3 版練習'),
    ('EXERCÍCIOS · 第 4 版练习', 'EXERCÍCIOS · 第 4 版練習'),
    ('EXERCÍCIOS · 第 5 版练习', 'EXERCÍCIOS · 第 5 版練習'),
    ('EXERCÍCIOS · 第 6 版练习', 'EXERCÍCIOS · 第 6 版練習'),
    ('RESPOSTAS · 参考答案 — 按版面分页排列，找到题号即可',
     'RESPOSTAS · 參考答案 — 按版面分頁排列，找到題號即可'),
    ('每题附一句中文简析 · 带 ✓ 的为范文题', '每題附一句中文簡析 · 帶 ✓ 的為範本題'),
    # ---- exercise type / instruction labels (longest first) ----
    ('完形单选', '完形單選'),
    ('词汇配对', '詞彙配對'),
    ('判断对错', '判斷對錯'),
    ('把词和释义配对', '把詞和釋義配對'),
    ('单选', '單選'),
    ('翻译', '翻譯'),
    ('写作', '寫作'),
    ('判断', '判斷'),
    # ---- bridges / instructions ----
    ('读第 2 版文章，选出正确答案。', '讀第 2 版文章，選出正確答案。'),
    ('读第 3 版文章，选出正确答案。', '讀第 3 版文章，選出正確答案。'),
    ('读第 4 版文章，选出正确答案。', '讀第 4 版文章，選出正確答案。'),
    ('读第 5 版文章，选出正确答案。', '讀第 5 版文章，選出正確答案。'),
    ('补全动词的现在时形式。', '補全動詞的現在時形式。'),
    ('用第 1、2 版的数字填空。', '用第 1、2 版的數字填空。'),
    ('用方框里的词填空。注意：有的词要变成复数。',
     '用方框裡的詞填空。注意：有的詞要變成複數。'),
    ('用方框里的词填空。', '用方框裡的詞填空。'),
    ('用过去时（pretérito perfeito）补全。', '用過去時（pretérito perfeito）補全。'),
    ('把词组成正确的句子。', '把詞組成正確的句子。'),
    ('用括号里正确的比较形式填空。', '用括號裡正確的比較形式填空。'),
    ('把句子补全成过去时（pretérito perfeito）。',
     '把句子補全成過去時（pretérito perfeito）。'),
    ('用将来时（futuro do presente）补全。', '用將來時（futuro do presente）補全。'),
    ('看上面两张图，选出正确答案。', '看上面兩張圖，選出正確答案。'),
    ('根据句子意思，补全正确的动词形式。', '根據句子意思，補全正確的動詞形式。'),
    ('用方框里的词填空：portões · segunda chamada · local · conferir',
     '用方框裡的詞填空：portões · segunda chamada · local · conferir'),
    ('提问句：que horas（几点）+ 动词；onde fica 问地点；conferir 的 eu 形式不规则：confiro',
     '提問句：que horas（幾點）+ 動詞；onde fica 問地點；conferir 的 eu 形式不規則：confiro'),
    ('讲一周的事用过去时（pretérito perfeito）；revisar 规则（revisei）；chegar/dormir 的过去时注意重音。',
     '講一週的事用過去時（pretérito perfeito）；revisar 規則（revisei）；chegar/dormir 的過去時注意重音。'),
    ('quando、se、quem 后用虚拟式将来：tiver、for、chegar（周日假设）。',
     'quando、se、quem 後用虛擬式將來：tiver、for、chegar（週日假設）。'),
    ('写作题（无唯一答案）；范文（', '寫作題（無唯一答案）；範本（'),
    (' 词）见下。', ' 詞）見下。'),
    ('范文见本版 H 区（', '範本見本版 H 區（'),
    (' 词）', ' 詞）'),
    ('（开放题，范文如下）', '（開放題，範本如下）'),
    # ---- P1/P2 notes ----
    ('feriadão = 连休长周末', 'feriadão = 連休長週末'),
    ('portões = 大门（考场大门）', 'portões = 大門（考場大門）'),
    ('13h30 开考（巴西利亚时间）', '13h30 開考（巴西利亞時間）'),
    ('19h 结束', '19h 結束'),
    ('revisar 现在时 eles 形式：revisam', 'revisar 現在時 eles 形式：revisam'),
    ('连休从 10 月 31 日到 11 月 2 日', '連休從 10 月 31 日到 11 月 2 日'),
    ('13 点关门', '13 點關門'),
    ('第 1 天考作文、语言与人文', '第 1 天考作文、語言與人文'),
    ('亡灵节家人们去墓园献花', '亡靈節家人們去墓園獻花'),
    ('确认卡显示考试地点', '確認卡顯示考試地點'),
    ('巴西没有夏令时，钟表不动', '巴西沒有夏令時，鐘錶不動'),
    ('ser 现在时 ela 形式：é', 'ser 現在時 ela 形式：é'),
    ('12 点到 13 点 = 1 小时', '12 點到 13 點 = 1 小時'),
    ('13:30 至 19:00 = 5 个半小时', '13:30 至 19:00 = 5 個半小時'),
    ('5×60 + 30 = 330 分钟', '5×60 + 30 = 330 分鐘'),
    ('feriadão=连着周末的假期 c', 'feriadão=連著週末的假期 c'),
    ('vela=点亮纪念的物品 d', 'vela=點亮紀念的物品 d'),
    ('crisântemo=亡灵节带去的花 a', 'crisântemo=亡靈節帶去的花 a'),
    ('周日 12 点开门', '週日 12 點開門'),
    ('13:30 开考', '13:30 開考'),
    ('19:00 结束', '19:00 結束'),
    ('在你的国家，有纪念逝者的日子吗？那天家人们做什么？写两句寄来。',
     '在你的國家，有紀念逝者的日子嗎？那天家人們做什麼？寫兩句寄來。'),
    ('o feriadão 连休长周末 · o cemitério 墓园 · a vela 蜡烛 · o crisântemo 菊花 · a missa 弥撒 · conferir 核对。',
     'o feriadão 連休長週末 · o cemitério 墓園 · a vela 蠟燭 · o crisântemo 菊花 · a missa 彌撒 · conferir 核對。'),
    # ---- P3 ----
    ('o túmulo 墓碑 · a flor 花 · acender 点燃 · rezar 祈祷 · o silêncio 寂静 · a lembrança 怀念。',
     'o túmulo 墓碑 · a flor 花 · acender 點燃 · rezar 祈禱 · o silêncio 寂靜 · a lembrança 懷念。'),
    ('在你的文化里，人们怎样怀念逝者？写两句寄来。',
     '在你的文化裡，人們怎樣懷念逝者？寫兩句寄來。'),
    ('亡灵节是怀念与安静的日子', '亡靈節是懷念與安靜的日子'),
    ('家人们带花去墓园，主要是菊花', '家人們帶花去墓園，主要是菊花'),
    ('教堂和墓园整天都有弥撒', '教堂和墓園整天都有彌撒'),
    ('万圣节在 10 月 31 日周六', '萬聖節在 10 月 31 日週六'),
    ('怀念是继续亲近的方式', '懷念是繼續親近的方式'),
    ('vela = 蜡烛', 'vela = 蠟燭'),
    ('missa = 弥撒', 'missa = 彌撒'),
    ('silêncio = 寂静', 'silêncio = 寂靜'),
    ('lembrança = 怀念', 'lembrança = 懷念'),
    ('visitar 过去时 elas 形式：visitaram', 'visitar 過去時 elas 形式：visitaram'),
    ('levar 过去时 elas 形式：levaram', 'levar 過去時 elas 形式：levaram'),
    ('ser 过去时 ele 形式：foi', 'ser 過去時 ele 形式：foi'),
    ('viver 过去时 ele 形式：viveu', 'viver 過去時 ele 形式：viveu'),
    ('主语 + 动词 + 宾语 + 地点', '主語 + 動詞 + 賓語 + 地點'),
    ('主语 + é + 表语', '主語 + é + 表語'),
    ('主语 + 动词 + 宾语', '主語 + 動詞 + 賓語'),
    # ---- P4 ----
    ('a ida 首回合 · a volta 次回合 · o finalista 决赛球队 · a decisão 决战 · a rodada 轮次。',
     'a ida 首回合 · a volta 次回合 · o finalista 決賽球隊 · a decisão 決戰 · a rodada 輪次。'),
    ('你在巴西杯支持哪支球队？写两句寄来。', '你在巴西盃支持哪支球隊？寫兩句寄來。'),
    ('次回合米内罗竞技 × 格雷米奥在周六 7 日 18 点',
     '次回合米內羅競技 × 格雷米奧在週六 7 日 18 點'),
    ('瓦斯科 × 帕尔梅拉斯次回合在周日 8 日 17 点，圣雅努阿里奥',
     '瓦斯科 × 帕爾梅拉斯次回合在週日 8 日 17 點，聖雅努阿里奧'),
    ('首回合在 11 月 1 日周日', '首回合在 11 月 1 日週日'),
    ('第 34 轮周一到周五每天都有比赛', '第 34 輪週一到週五每天都有比賽'),
    ('两回合总比分胜者进决赛', '兩回合總比分勝者進決賽'),
    ('finalista=进决赛的球队 b', 'finalista=進決賽的球隊 b'),
    ('ida=对决的第一场 c', 'ida=對決的第一場 c'),
    ('volta=对决的第二场 a', 'volta=對決的第二場 a'),
    ('rodada=一轮比赛 d', 'rodada=一輪比賽 d'),
    ('次回合决定决赛名额：mais', '次回合決定決賽名額：mais'),
    ('第 34 轮周一到周五都有比赛：mais', '第 34 輪週一到週五都有比賽：mais'),
    ('ser 过去时复数：foram', 'ser 過去時複數：foram'),
    ('receber 过去时 ele 形式：recebeu', 'receber 過去時 ele 形式：recebeu'),
    ('começar 过去时 ela 形式：começou', 'começar 過去時 ela 形式：começou'),
    ('chegar 过去时 eles 形式：chegaram', 'chegar 過去時 eles 形式：chegaram'),
    # ---- P5 ----
    ('a reta final 最后冲刺 · a véspera 前夕 · a maratona 突击马拉松 · separar 准备好 · a cabeça 头脑、状态。',
     'a reta final 最後衝刺 · a véspera 前夕 · a maratona 突擊馬拉松 · separar 準備好 · a cabeça 頭腦、狀態。'),
    ('重要考试前一晚，你的计划是复习还是休息？写两句寄来。',
     '重要考試前一晚，你的計畫是複習還是休息？寫兩句寄來。'),
    ('冲刺周在 11 月 8 日周日结束', '衝刺週在 11 月 8 日週日結束'),
    ('每天复习一点', '每天複習一點'),
    ('提前一天备好证件和黑笔', '提前一天備好證件和黑筆'),
    ('第 2 天考自然科学与数学', '第 2 天考自然科學與數學'),
    ('11 月 3 日周二各州议会结束休会', '11 月 3 日週二各州議會結束休會'),
    ('reta final = 最后冲刺阶段', 'reta final = 最後衝刺階段'),
    ('inscrito 配合复数：inscritos', 'inscrito 配合複數：inscritos'),
    ('maratona = 突击马拉松', 'maratona = 突擊馬拉松'),
    ('local = 地点', 'local = 地點'),
    ('用将来时（futuro do presente）补全。', '用將來時（futuro do presente）補全。'),
    ('fazer 将来时 eles 不规则形式：farão', 'fazer 將來時 eles 不規則形式：farão'),
    ('mostrar 将来时：mostrará', 'mostrar 將來時：mostrará'),
    ('sair 将来时复数：sairão', 'sair 將來時複數：sairão'),
    ('chegar 将来时：chegará', 'chegar 將來時：chegará'),
    ('错：考前突击不是好计划，每天复习一点才好', '錯：考前突擊不是好計畫，每天複習一點才好'),
    ('对：13:30 至 19:00', '對：13:30 至 19:00'),
    ('1. Confira o Cartão de Confirmação do Enem（核对高考确认卡）',
     '1. Confira o Cartão de Confirmação do Enem（核對高考確認卡）'),
    ('2. Revise um pouco por dia, sem maratona（每天复习一点，不搞突击）',
     '2. Revise um pouco por dia, sem maratona（每天複習一點，不搞突擊）'),
    ('4. Separe documento e caneta preta no dia anterior（提前一天备好证件和黑笔）',
     '4. Separe documento e caneta preta no dia anterior（提前一天備好證件和黑筆）'),
    ('5. Domingo 8: chegue antes das 12h（周日 8 日：12 点前到达）',
     '5. Domingo 8: chegue antes das 12h（週日 8 日：12 點前到達）'),
    # ---- P6 ----
    ('os portões 大门 · a segunda chamada 补考、第二次入场 · conferir 核对 · a correria 匆忙。',
     'os portões 大門 · a segunda chamada 補考、第二次入場 · conferir 核對 · a correria 匆忙。'),
    ('大门开放 60 分钟', '大門開放 60 分鐘'),
    ('关门到开考之间等 30 分钟', '關門到開考之間等 30 分鐘'),
    ('考试 330 分钟', '考試 330 分鐘'),
    ('中午到 19 点 = 7 小时', '中午到 19 點 = 7 小時'),
    ('图表数字是 Inep 官方时间', '圖表數字是 Inep 官方時間'),
    ('高考分 8 日和 15 日两个周日', '高考分 8 日和 15 日兩個週日'),
    ('13 点后到场不得入内', '13 點後到場不得入內'),
    ('将来时：começará', '將來時：começará'),
    ('quem + 虚拟式将来：chegar', 'quem + 虛擬式將來：chegar'),
    ('现在时：fecham', '現在時：fecham'),
    ('现在时：pede', '現在時：pede'),
    ('portões = 大门', 'portões = 大門'),
    ('segunda chamada = 补考、第二次入场', 'segunda chamada = 補考、第二次入場'),
    ('祈使式：confira', '祈使式：confira'),
    # ---- P7 ----
    ('conferir：eu → confiro（不规则）', 'conferir：eu → confiro（不規則）'),
    ('onde 问地点', 'onde 問地點'),
    ('revisar 过去时：revisei', 'revisar 過去時：revisei'),
    ('chegar 过去时：chegou', 'chegar 過去時：chegou'),
    ('dormir 过去时：dormiu', 'dormir 過去時：dormiu'),
    ('chegaram 是 chegar 的过去时复数', 'chegaram 是 chegar 的過去時複數'),
    ('quem + 虚拟式将来：tiver', 'quem + 虛擬式將來：tiver'),
    ('quando + 虚拟式将来：chegar', 'quando + 虛擬式將來：chegar'),
    ('se + ser 的虚拟式将来：for', 'se + ser 的虛擬式將來：for'),
    ('quando + 未来 → 虚拟式将来 for', 'quando + 未來 → 虛擬式將來 for'),
    ('高考用黑笔，蓝笔不行。', '高考用黑筆，藍筆不行。'),
    ('13 点关门，13:30 到就晚了。', '13 點關門，13:30 到就晚了。'),
    ('考前一夜突击没用，睡好才记得住。', '考前一夜突擊沒用，睡好才記得住。'),
    ('连休是 10 月 31 日到 11 月 2 日，共三天。', '連休是 10 月 31 日到 11 月 2 日，共三天。'),
    ('feriadão = 连休长周末，共三天。', 'feriadão = 連休長週末，共三天。'),
    ('编辑部示例，非真实来信。真实来信请寄编辑部，下期见！',
     '編輯部示例，非真實來信。真實來信請寄編輯部，下期見！'),
    ('编辑部说明：上期承诺的真实来信与最佳作文截稿时未收到，本期仍刊示例，顺延至下期。',
     '編輯部說明：上期承諾的真實來信與最佳作文截稿時未收到，本期仍刊示例，順延至 VOL.3。'),
    ('从连休到考试：高考周。', '從連休到考試：高考週。'),
    ('许多人旅行、探亲、去墓园献花。', '許多人旅行、探親、去墓園獻花。'),
    ('亡灵节是怀念的日子。', '亡靈節是懷念的日子。'),
    ('怀念是继续亲近的方式。', '懷念是繼續親近的方式。'),
    ('每一分值一个名次，每一球值一个故事。', '每一分值一個名次，每一球值一個故事。'),
    ('睡得好，记得牢。', '睡得好，記得牢。'),
    ('先做容易的，再做难的。', '先做容易的，再做難的。'),
    ('核对确认卡、睡好、早到。', '核對確認卡、睡好、早到。'),
    # ---- P8 ----
    ('亡灵节在 11 月 2 日', '亡靈節在 11 月 2 日'),
    ('瓦斯科 × 帕尔梅拉斯次回合在 8 日', '瓦斯科 × 帕爾梅拉斯次回合在 8 日'),
    ('连休共 3 天', '連休共 3 天'),
    ('考试时长 5 个半小时', '考試時長 5 個半小時'),
    ('确认卡是高考的文件', '確認卡是高考的文件'),
    ('米内罗竞技 × 格雷米奥次回合在 MRV 竞技场',
     '米內羅競技 × 格雷米奧次回合在 MRV 競技場'),
    ('第 34 轮周一到周五都有比赛', '第 34 輪週一到週五都有比賽'),
    ('亡灵节家人们带花', '亡靈節家人們帶花'),
    ('330 是考试的分钟数', '330 是考試的分鐘數'),
    ('亡灵节又称诸圣灵魂日', '亡靈節又稱諸聖靈魂日'),
    ('卢卡斯住在贝洛奥里藏特', '盧卡斯住在貝洛奧里藏特'),
    ('连休里他休息并每天复习一点', '連休裡他休息並每天複習一點'),
    ('前一晚他备好证件和黑笔、早睡', '前一晚他備好證件和黑筆、早睡'),
    ('他 11 点到达考场', '他 11 點到達考場'),
    ('时间词在前', '時間詞在前'),
    ('疑问词组在句首', '疑問詞組在句首'),
    ('11 月 8 日周日是高考的第一天。', '11 月 8 日週日是高考的第一天。'),
    ('对照第 6 版标题', '對照第 6 版標題'),
    ('周日前核对确认卡。', '週日前核對確認卡。'),
    ('Confira = 请核对', 'Confira = 請核對'),
    ('feriadão = 连休', 'feriadão = 連休'),
    ('“连休是 10 月 31 日到 11 月 2 日。” → ___',
     '「連休是 10 月 31 日到 11 月 2 日。」 → ___'),
    ('虚拟式将来 chegar + 祈使 apresente', '虛擬式將來 chegar + 祈使 apresente'),
    ('你到达时，请出示带照片的证件。 → ___', '你到達時，請出示帶照片的證件。 → ___'),
    ('feriadão=连着周末的假期 b', 'feriadão=連著週末的假期 b'),
    ('portão=考场入口 d', 'portão=考場入口 d'),
    ('reta final=考前最后一周 a', 'reta final=考前最後一週 a'),
    ('segunda chamada=关门后的再入场（高考没有） c',
     'segunda chamada=關門後的再入場（高考沒有） c'),
    ('documento com foto 带照片的证件', 'documento com foto 帶照片的證件'),
    ('seção = 考场分区（房间）', 'seção = 考場分區（房間）'),
    ('大门 13 点关闭', '大門 13 點關閉'),
    ('考试 13:30 开始', '考試 13:30 開始'),
    ('obrigado = 谢谢', 'obrigado = 謝謝'),
]

M.sort(key=lambda pair: -len(pair[0]))
for fn in ['content12.py', 'content34.py', 'content56.py', 'content7.py', 'content8.py']:
    t = load(fn)
    for old, new in M:
        if old in t:
            t = t.replace(old, new)
    save(fn, t)
# every mapping old must have fired somewhere
_all = ''.join(load(fn) for fn in ['content12.py', 'content34.py', 'content56.py', 'content7.py', 'content8.py'])
for old, new in M:
    assert new in _all, f'mapping never fired: {old!r} -> {new!r}'

# ---------- 4. P1 badge (W43 same-pairing slot/style) ----------
t = load('content12.py')
t = line_replace(t, 'p.text(975, 372,',
    'p.text(975, 372, "葡萄牙語正文 · 繁體中文講解 — 給繁體中文讀者的版本", 19.5, "sans", True, BRICK, anchor="middle")',
    'content12.py')
save('content12.py', t)

# ---------- 5. P8 separators (W43 same-pairing form) ----------
t = load('content8.py')
t = sub(t, 'f"— PÁGINA {pg} —"', 'f"— 第 {pg} 版 —"', 1, 'content8.py')
save('content8.py', t)

# ---------- 6. P7 readers-garden: disclosure + explicit invitation ----------
INV = '請把你的來信寄給編輯部，VOL.3 就刊登你的來信！'
t = load('content7.py')
# box height gains one invitation paragraph
t = sub(t, ' * 29 + 35',
        ' * 29 + 10 + len(wrap("' + INV + '", "sans", False, 19.5, CW - 44)) * 29 + 35',
        1, 'content7.py')
# disclosure paragraph keeps its line, invitation follows it
t = line_replace(t, 'p.para(bx + 22, yy3 + 10, disc_cn,',
    'yy3 = p.para(bx + 22, yy3 + 10, disc_cn, 19.5, "sans", False, GREY, CW - 44, 1.42)\n'
    'p.para(bx + 22, yy3 + 10, "' + INV + '", 19.5, "sans", False, GREY, CW - 44, 1.42)',
    'content7.py')
save('content7.py', t)

# ---------- 6b. P7 quote pitch 128 -> 96 (FIX round 1) ----------
# The taller letters box (invitation paragraph added) pushes the quote
# block down until its last row is covered by the preview box at y=2404
# (round-1 audit: 5 flags, all this one defect). Tightening the pitch
# to 96 follows the W45 PT x NL precedent for the same geometry.
t = load('content7.py')
t = line_replace(t, 'cyq = fy + 66 + (i % 4) * 128',
    '    cyq = fy + 66 + (i % 4) * 96  # ZH-TW: tightened from 128 so the taller letters box leaves the preview box clear',
    'content7.py')
save('content7.py', t)

# ---------- 7. final structural assertions ----------
for fn in ['content12.py', 'content34.py', 'content56.py', 'content7.py', 'content8.py']:
    t = load(fn)
    assert '.bridge(' not in t, f'{fn}: bridge call survived'
    assert 'weekly-report-w45-pt-core' not in t, f'{fn}: core OUT survived'
t = load('bslib4.py')
assert 'def bridge' not in t and 'def expl' in t
assert 'weekly-report-w45-pt-zh-tw' in load('render.py')
print('transform OK')
