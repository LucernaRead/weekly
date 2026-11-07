# -*- coding: utf-8 -*-
"""PT core (zh explanations) -> PT x KO fan-out transform for W45 VOL.2.

Copies nothing: run this inside the already-copied build dir. Every
replacement is an exact literal match with an asserted occurrence count
(longest strings first where one contains another), except line-anchored
replacements (P1 edition/badge lines). After the pass, bslib4.py +
content*.py must contain ZERO CJK chars and zero full-width CJK
punctuation. Frozen Portuguese text, the P7 example letter (lt), the PT
disclosure (disc_pt) and the P7 quote strings + 'Página' tags are never
touched. Furniture follows the shipped W43 PT x KO edition
(files/weekly-report-pt-ko + its KIT section 3), VOL.1 -> VOL.2 only:
badge BRICK 19.5pt bold in the 372 slot, footer A Lucerna · 포르투갈어
주간지 VOL.2 · 텍스트는 포르투갈어 · 해설은 한국어, page line
제 N 면 / 총 8 면, gloss prefix 해설 — , P8 separator — 제 N 면 —,
dash-style P8 (core style, unchanged code). P7 word box: the Portuguese
definition sentence (wt) is frozen verbatim; only its gloss line is
localized to Korean. Type labels follow W43 PT x KO (빈칸 객관식 for
完形单选); instr labels likewise (빈칸 채우기 for 填空).
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
CJK = re.compile(r'[\u4e00-\u9fff]')
FWP = re.compile(r'[\uff08\uff09\uff1a]')  # full-width parens/colon

def load(fn):
    with open(os.path.join(HERE, fn), encoding="utf-8") as f:
        return f.read()

def save(fn, txt):
    with open(os.path.join(HERE, fn), "w", encoding="utf-8") as f:
        f.write(txt)

def sub(txt, old, new, fn=""):
    n = txt.count(old)
    assert n >= 1, f"{fn}: {old!r} not found"
    return txt.replace(old, new)

def line_replace(txt, anchor, newline, fn=""):
    lines = txt.split("\n")
    hits = [i for i, ln in enumerate(lines) if anchor in ln]
    assert len(hits) == 1, f"{fn}: anchor {anchor!r} hits {hits}"
    lines[hits[0]] = newline
    return "\n".join(lines)

FILES = ["bslib4.py", "content12.py", "content34.py", "content56.py",
         "content7.py", "content8.py", "render.py"]

# ---------- 0. OUT / BASE repoint (all files) ----------
for fn in FILES:
    t = load(fn)
    if 'weekly-report-w45-pt-core' in t:
        t = sub(t, 'weekly-report-w45-pt-core', 'weekly-report-w45-pt-ko', fn=fn)
        save(fn, t)

# render.py PDF names: W45 sibling pattern Lucerna-VOL2-KO
t = load('render.py')
t = sub(t, 'A-Lucerna-VOL2.pdf', 'Lucerna-VOL2-KO.pdf', 'render.py')
t = sub(t, 'A-Lucerna-VOL2-web.pdf', 'Lucerna-VOL2-KO-web.pdf', 'render.py')
save('render.py', t)

# ---------- 1. bslib4 furniture (W43 PT x KO, VOL.2) ----------
t = load('bslib4.py')
t = sub(t, 'A Lucerna · 葡萄牙语周报 VOL.2 · LUCERNA PORTUGUESE WEEKLY',
        'A Lucerna · 포르투갈어 주간지 VOL.2 · 텍스트는 포르투갈어 · 해설은 한국어', 'bslib4.py')
t = sub(t, 'f"第 {n} 版 / 共 {total} 版"', 'f"제 {n} 면 / 총 {total} 면"', 'bslib4.py')
t = sub(t, '("译注｜" + s', '("해설 — " + s', 'bslib4.py')
save('bslib4.py', t)

# ---------- 2. type / instr labels (instr first, then bare typ) ----------
INSTR = [
    ('instr="造句"', 'instr="문장 만들기"'),
    ('instr="翻译"', 'instr="번역"'),
    ('instr="判断"', 'instr="참 / 거짓"'),
    ('instr="写作"', 'instr="쓰기"'),
    ('instr="填空"', 'instr="빈칸 채우기"'),
    ('instr="把词和释义配对"', 'instr="단어와 뜻 짝짓기"'),
]
TYP = [
    ('"完成句子"', '"문장 완성"'),
    ('"词汇配对"', '"단어 짝짓기"'),
    ('"判断对错"', '"진위 판단"'),
    ('"完形单选"', '"빈칸 객관식"'),
    ('"单选"', '"객관식"'),
    ('"造句"', '"문장 만들기"'),
    ('"翻译"', '"번역"'),
    ('"写作"', '"쓰기"'),
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

# ---------- 3. content replacements (longest-first within each file) ----------
R12K = [
    ('o feriadão 连休长周末 · o cemitério 墓园 · a vela 蜡烛 · o crisântemo 菊花 · a missa 弥撒 · conferir 核对。', 'o feriadão 연휴가 긴 주말 · o cemitério 묘지 · a vela 초 · o crisântemo 국화 · a missa 미사 · conferir 확인하다.'),
    ('葡 萄 牙 语 周 报 · VOL.2 · A SEMANA DO ENEM · FINADOS · O FUTEBOL DECIDE', '포르투갈어 주간지 · VOL.2 · A SEMANA DO ENEM · FINADOS · O FUTEBOL DECIDE'),
    ('讲解｜feriadão 连休长周末 · o portão 大门 · a redação 作文 · revisar 复习。', '해설 — feriadão 연휴와 주말이 이어진 날들 · o portão 문 · a redação 작문 · revisar 복습하다.'),
    ('TODA SEMANA EM PORTUGUÊS · 每周一期 · 读巴西人正在读的葡萄牙语', 'TODA SEMANA EM PORTUGUÊS · 매주 발행 · 브라질이 읽는 포르투갈어'),
    ('12h — os portões abrem no domingo 8（周日 12 点开门）', '12h — os portões abrem no domingo 8 (일요일 12시에 열어요)'),
    ('13h30–19h — a prova do dia 8（考试 13:30 至 19:00）', '13h30–19h — a prova do dia 8 (시험은 13:30부터 19:00까지예요)'),
    ('5h30 — a duração da prova do dia 8（考试时长 5 小时半）', '5h30 — a duração da prova do dia 8 (시험 시간은 5시간 30분이에요)'),
    ('13h — os portões fecham（13 点关门，过时不入）', '13h — os portões fecham (13시에 닫아요, 늦으면 못 들어가요)'),
    ('Um país, vários relógios · 一个国家，几个时区', 'Um país, vários relógios · 하나의 나라, 여러 시간'),
    ('OS HORÁRIOS DO DOMINGO 8 · 周日时间表', 'OS HORÁRIOS DO DOMINGO 8 · 일요일 시간표'),
    ('在你的国家，有纪念逝者的日子吗？那天家人们做什么？写两句寄来。', '여러분 나라에도 돌아가신 분들을 기리는 날이 있어요? 그날 가족들은 무엇을 해요? 두 문장을 써서 보내 주세요.'),
    ('11 月 2 日亡灵节连休 · 11 月 8 日高考第一天', '11월 2일 연휴 · 11월 8일 엔엠 첫날'),
    ('revisar 现在时 eles 形式：revisam', 'revisar 현재형 eles 형태: revisam'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', '답은 8면에 · 수준이 섞여 있어요, 번호로 찾으세요'),
    ('A SEMANA EM NÚMEROS · 数字', 'A SEMANA EM NÚMEROS · 숫자'),
    ('EM POUCAS PALAVRAS · 快讯', 'EM POUCAS PALAVRAS · 단신'),
    ('连休从 10 月 31 日到 11 月 2 日', '연휴는 10월 31일부터 11월 2일까지예요'),
    ('conferir：ele → confere', 'conferir: ele → confere'),
    ('13:30 至 19:00 = 5 个半小时', '13:30부터 19:00까지 = 5시간 반'),
    ('QUIZ RELÂMPAGO · 闪电问答', 'QUIZ RELÂMPAGO · 번개 퀴즈'),
    ('读头版，选出正确答案 · 答案见第 8 版', '1면을 읽고 정답을 고르세요 · 답은 8면에'),
    ('EXERCÍCIOS · 第 2 版练习', 'EXERCÍCIOS · 2면 연습 문제'),
    ('começar：ela → começa', 'começar: ela → começa'),
    ('crisântemo=亡灵节带去的花 a', 'crisântemo=위령절에 가져가는 꽃 a'),
    ('NESTA EDIÇÃO · 本期目录', 'NESTA EDIÇÃO · 이번 호 차례'),
    ('PARA NÃO ERRAR · 口诀', 'PARA NÃO ERRAR · 요령'),
    ('levar：nós → levamos', 'levar: nós → levamos'),
    ('cemitério=墓碑所在的地方 b', 'cemitério=무덤이 있는 곳 b'),
    ('portões = 大门（考场大门）', 'portões = 문 (시험장 문)'),
    ('5×60 + 30 = 330 分钟', '5×60 + 30 = 330분'),
    ('31 日、1 日、2 日 = 3 天', '31일, 1일, 2일 = 3일'),
    ('feriadão=连着周末的假期 c', 'feriadão=주말과 이어진 연휴 c'),
    ('AGORA VOCÊ · 即学即练', 'AGORA VOCÊ · 바로 연습해요'),
    ('“连休”：假期连着周末，一共三天。', '“연휴”: 주말과 이어진 공휴일, 모두 3일이에요.'),
    ('12 点到 13 点 = 1 小时', '12시부터 13시까지 = 1시간'),
    ('feriadão = 连休长周末', 'feriadão = 연휴가 긴 주말'),
    ('13h30 开考（巴西利亚时间）', '13h30 개시 (브라질리아 시간)'),
    ('读第 2 版文章，选出正确答案。', '2면 글을 읽고 정답을 고르세요.'),
    ('abrir：ele → abre', 'abrir: ele → abre'),
    ('ser 现在时 ela 形式：é', 'ser 현재형 ela 형태: é'),
    ('E VOCÊ? · 说说你自己', 'E VOCÊ? · 여러분은요?'),
    ('迟到不得入内：13 点后关门', '늦게 오면 못 들어가요: 13시 이후에는 닫아요'),
    ('A NOTÍCIA · 头条', 'A NOTÍCIA · 헤드라인'),
    ('第 1 天考作文、语言与人文', '첫날은 작문, 언어, 인문이에요'),
    ('用第 1、2 版的数字填空。', '1, 2면의 숫자로 채우세요.'),
    ('vela=点亮纪念的物品 d', 'vela=기념하며 켜는 물건 d'),
    ('次回合在 7 日和 8 日', '2차전은 7일과 8일에 있어요'),
    ('redação = 作文', 'redação = 작문'),
    ('巴西没有夏令时，钟表不动', '브라질에는 서머타임이 없어요, 시계가 바뀌지 않아요'),
    ('亡灵节家人们去墓园献花', '위령절에 가족들은 묘지에 꽃을 가져가요'),
    ('补全动词的现在时形式。', '동사의 현재형으로 채우세요.'),
    ('VIDA · 生活', 'VIDA · 생활'),
    ('周日 12 点开门', '일요일 12시에 열어요'),
    ('确认卡显示考试地点', '확인 카드에 시험 장소가 나와요'),
    ('13:30 开考', '13:30에 시작해요'),
    ('19:00 结束', '19:00에 끝나요'),
    ('19h 结束', '19h 종료'),
    ('13 点关门', '13시에 문이 닫혀요'),
    ('全国高考周', '엔엠 주간'),
]

t = load('content12.py')
for old, new in R12K:
    t = sub(t, old, new, fn='content12.py')
save('content12.py', t)

R34K = [
    ('o túmulo 墓碑 · a flor 花 · acender 点燃 · rezar 祈祷 · o silêncio 寂静 · a lembrança 怀念。', 'o túmulo 무덤 · a flor 꽃 · acender 켜다 · rezar 기도하다 · o silêncio 고요 · a lembrança 추억.'),
    ('a ida 首回合 · a volta 次回合 · o finalista 决赛球队 · a decisão 决战 · a rodada 轮次。', 'a ida 1차전 · a volta 2차전 · o finalista 결승 진출 팀 · a decisão 결승전 · a rodada 라운드.'),
    ('A2 → B1 · Finados: o dia da memória · 亡灵节：怀念的日子', 'A2 → B1 · Finados: o dia da memória · 위령절: 추억의 날'),
    ('NÍVEL B1 · O futebol da semana · 足球之周', 'NÍVEL B1 · O futebol da semana · 이번 주의 축구'),
    ('瓦斯科 × 帕尔梅拉斯次回合在周日 8 日 17 点，圣雅努阿里奥', '바스쿠 × 파우메이라스 2차전은 일요일 8일 17시, 상 자누아리우예요'),
    ('把句子补全成过去时（pretérito perfeito）。', '문장을 과거형(pretérito perfeito)으로 채우세요.'),
    ('visitar 过去时 elas 形式：visitaram', 'visitar 과거형 elas 형태: visitaram'),
    ('用过去时（pretérito perfeito）补全。', '과거형(pretérito perfeito)으로 채우세요.'),
    ('次回合米内罗竞技 × 格雷米奥在周六 7 日 18 点', '2차전 아틀레치쿠 미네이루 × 그레미우는 토요일 7일 18시예요'),
    ('chegar 过去时 eles 形式：chegaram', 'chegar 과거형 eles 형태: chegaram'),
    ('A SEMANA DO FUTEBOL · 足球周历', 'A SEMANA DO FUTEBOL · 축구 주간 일정'),
    ('receber 过去时 ele 形式：recebeu', 'receber 과거형 ele 형태: recebeu'),
    ('começar 过去时 ela 形式：começou', 'começar 과거형 ela 형태: começou'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', '답은 8면에 · 수준이 섞여 있어요, 번호로 찾으세요'),
    ('levar 过去时 elas 形式：levaram', 'levar 과거형 elas 형태: levaram'),
    ('在你的文化里，人们怎样怀念逝者？写两句寄来。', '여러분 문화에서는 돌아가신 분들을 어떻게 추억해요? 두 문장을 써서 보내 주세요.'),
    ('viver 过去时 ele 形式：viveu', 'viver 과거형 ele 형태: viveu'),
    ('EXERCÍCIOS · 第 3 版练习', 'EXERCÍCIOS · 3면 연습 문제'),
    ('EXERCÍCIOS · 第 4 版练习', 'EXERCÍCIOS · 4면 연습 문제'),
    ('第 34 轮周一到周五都有比赛：mais', '34라운드는 월요일부터 금요일까지 경기가 있어요: mais'),
    ('ser 过去时 ele 形式：foi', 'ser 과거형 ele 형태: foi'),
    ('你在巴西杯支持哪支球队？写两句寄来。', '브라질 컵에서는 어느 팀을 응원해요? 두 문장을 써서 보내 주세요.'),
    ('finalista=进决赛的球队 b', 'finalista=결승에 가는 팀 b'),
    ('主语 + 动词 + 宾语 + 地点', '주어 + 동사 + 목적어 + 장소'),
    ('第 34 轮周一到周五每天都有比赛', '34라운드는 월요일부터 금요일까지 매일 경기가 있어요'),
    ('17 < 18：mais cedo', '17 < 18: mais cedo'),
    ('读第 3 版文章，选出正确答案。', '3면 글을 읽고 정답을 고르세요.'),
    ('万圣节在 10 月 31 日周六', '핼러윈은 10월 31일 토요일이었어요'),
    ('读第 4 版文章，选出正确答案。', '4면 글을 읽고 정답을 고르세요.'),
    ('E VOCÊ? · 说说你自己', 'E VOCÊ? · 여러분은요?'),
    ('crisântemo = 菊花', 'crisântemo = 국화'),
    ('首回合在 11 月 1 日周日', '1차전은 11월 1일 일요일이었어요'),
    ('ser 过去时复数：foram', 'ser 과거형 복수: foram'),
    ('家人们带花去墓园，主要是菊花', '가족들은 묘지에 꽃을 가져가요, 주로 국화예요'),
    ('lembrança = 怀念', 'lembrança = 추억'),
    ('volta=对决的第二场 a', 'volta=대결의 두 번째 경기 a'),
    ('用括号里正确的比较形式填空。', '괄호 안의 바른 비교 형태로 채우세요.'),
    ('次回合决定决赛名额：mais', '2차전이 결승 진출을 정해요: mais'),
    ('silêncio = 寂静', 'silêncio = 고요'),
    ('rodada=一轮比赛 d', 'rodada=한 라운드 경기 d'),
    ('CULTURA · 文化', 'CULTURA · 문화'),
    ('亡灵节是怀念与安静的日子', '위령절은 추억과 고요의 날이에요'),
    ('主语 + 动词 + 宾语', '주어 + 동사 + 목적어'),
    ('ESPORTE · 体育', 'ESPORTE · 스포츠'),
    ('ida=对决的第一场 c', 'ida=대결의 첫 경기 c'),
    ('18 > 16：mais', '18 > 16: mais'),
    ('教堂和墓园整天都有弥撒', '교회와 묘지에서는 하루 종일 미사가 있어요'),
    ('túmulo = 墓碑', 'túmulo = 무덤'),
    ('主语 + é + 表语', '주어 + é + 서술어'),
    ('两回合总比分胜者进决赛', '두 경기 합계 승자가 결승에 가요'),
    ('怀念是继续亲近的方式', '추억하는 것은 가까이 지내는 방법이에요'),
    ('missa = 弥撒', 'missa = 미사'),
    ('把词组成正确的句子。', '단어를 바르게 배열해 문장을 만드세요.'),
    ('用方框里的词填空。', '네모 안의 단어로 채우세요.'),
    ('vela = 蜡烛', 'vela = 초'),
]

t = load('content34.py')
for old, new in R34K:
    t = sub(t, old, new, fn='content34.py')
save('content34.py', t)

R56K = [
    ('a reta final 最后冲刺 · a véspera 前夕 · a maratona 突击马拉松 · separar 准备好 · a cabeça 头脑、状态。', 'a reta final 막바지 · a véspera 전날 밤 · a maratona 벼락치기 · separar 챙기다 · a cabeça 머리, 컨디션.'),
    ('os portões 大门 · a segunda chamada 补考、第二次入场 · conferir 核对 · a correria 匆忙。', 'os portões 문 · a segunda chamada 재입장, 두 번째 입장 · conferir 확인하다 · a correria 서두름.'),
    ('O DOMINGO 8 EM NÚMEROS · 11 月 8 日的数字 (horários oficiais do Inep)', 'O DOMINGO 8 EM NÚMEROS · 11월 8일의 숫자 (Inep 공식 시간)'),
    ('4. Separe documento e caneta preta no dia anterior（提前一天备好证件和黑笔）', '4. Separe documento e caneta preta no dia anterior (전날 신분증과 검은 펜을 챙기세요)'),
    ('2. Revise um pouco por dia, sem maratona（每天复习一点，不搞突击）', '2. Revise um pouco por dia, sem maratona (매일 조금씩 복습하세요, 벼락치기는 안 돼요)'),
    ('用方框里的词填空：portões · segunda chamada · local · conferir', '네모 안의 단어로 채우세요: portões · segunda chamada · local · conferir'),
    ('1. Confira o Cartão de Confirmação do Enem（核对高考确认卡）', '1. Confira o Cartão de Confirmação do Enem (엔엠 확인 카드를 확인하세요)'),
    ('5. Domingo 8: chegue antes das 12h（周日 8 日：12 点前到达）', '5. Domingo 8: chegue antes das 12h (일요일 8일: 12시 전에 도착하세요)'),
    ('NÍVEL B1 · A reta final dos jovens · 冲刺周：年轻人的最后一周', 'NÍVEL B1 · A reta final dos jovens · 막바지 주간: 청년들의 마지막 한 주'),
    ('3. Durma bem na véspera da prova（考前一晚睡好）', '3. Durma bem na véspera da prova (시험 전날 밤에 푹 주무세요)'),
    ('NÍVEL B2 · O Enem explicado · 高考详解', 'NÍVEL B2 · O Enem explicado · 엔엠 자세히 보기'),
    ('用将来时（futuro do presente）补全。', '미래형(futuro do presente)으로 채우세요.'),
    ('重要考试前一晚，你的计划是复习还是休息？写两句寄来。', '중요한 시험 전날 밤, 여러분 계획은 복습이에요, 휴식이에요? 두 문장을 써서 보내 주세요.'),
    ('fazer 将来时 eles 不规则形式：farão', 'fazer 미래형 eles 불규칙 형태: farão'),
    ('segunda chamada = 补考、第二次入场', 'segunda chamada = 재입장, 두 번째 입장'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', '답은 8면에 · 수준이 섞여 있어요, 번호로 찾으세요'),
    ('inscrito 配合复数：inscritos', 'inscrito 복수 일치: inscritos'),
    ('用方框里的词填空。注意：有的词要变成复数。', '네모 안의 단어로 채우세요. 주의: 어떤 단어는 복수형이 돼요.'),
    ('EXERCÍCIOS · 第 5 版练习', 'EXERCÍCIOS · 5면 연습 문제'),
    ('mostrar 将来时：mostrará', 'mostrar 미래형: mostrará'),
    ('错：考前突击不是好计划，每天复习一点才好', '틀렸어요: 전날 벼락치기는 좋은 계획이 아니에요, 매일 조금씩 복습하는 게 좋아요'),
    ('EXERCÍCIOS · 第 6 版练习', 'EXERCÍCIOS · 6면 연습 문제'),
    ('reta final = 最后冲刺阶段', 'reta final = 막바지 단계'),
    ('APROFUNDAMENTO · 深读', 'APROFUNDAMENTO · 심층'),
    ('quem + 虚拟式将来：chegar', 'quem + 접속법 미래: chegar'),
    ('11 月 3 日周二各州议会结束休会', '11월 3일 화요일에 주의회가 휴회를 마쳐요'),
    ('separar 祈使式：separe', 'separar 명령형: separe'),
    ('chegar 将来时：chegará', 'chegar 미래형: chegará'),
    ('冲刺周在 11 月 8 日周日结束', '막바지 주간은 11월 8일 일요일에 끝나요'),
    ('sair 将来时复数：sairão', 'sair 미래형 복수: sairão'),
    ('高考分 8 日和 15 日两个周日', '엔엠은 8일과 15일 두 일요일에 있어요'),
    ('根据句子意思，补全正确的动词形式。', '문장 뜻에 맞게 바른 동사 형태로 채우세요.'),
    ('读第 5 版文章，选出正确答案。', '5면 글을 읽고 정답을 고르세요.'),
    ('maratona = 突击马拉松', 'maratona = 벼락치기'),
    ('E VOCÊ? · 说说你自己', 'E VOCÊ? · 여러분은요?'),
    ('对：13:30 至 19:00', '맞았어요: 13:30부터 19:00까지예요'),
    ('中午到 19 点 = 7 小时', '정오부터 19시까지 = 7시간'),
    ('图表数字是 Inep 官方时间', '그래프 숫자는 Inep 공식 시간이에요'),
    ('看上面两张图，选出正确答案。', '위 두 그래프를 보고 정답을 고르세요.'),
    ('关门到开考之间等 30 分钟', '문이 닫힌 뒤 시험 시작까지 30분을 기다려요'),
    ('第 1 天考作文、语言与人文', '첫날은 작문, 언어, 인문이에요'),
    ('第 2 天考自然科学与数学', '둘째 날은 자연과학과 수학이에요'),
    ('véspera = 前夕', 'véspera = 전날 밤'),
    ('将来时：começará', '미래형: começará'),
    ('portões = 大门', 'portões = 문'),
    ('JOVENS · 青年', 'JOVENS · 청년'),
    ('提前一天备好证件和黑笔', '전날 신분증과 검은 펜을 챙겨요'),
    ('13 点后到场不得入内', '13시 이후에 도착하면 못 들어가요'),
    ('祈使式：confira', '명령형: confira'),
    ('local = 地点', 'local = 장소'),
    ('大门开放 60 分钟', '문이 60분 동안 열려 있어요'),
    ('现在时：fecham', '현재형: fecham'),
    ('确认卡显示考试地点', '확인 카드에 시험 장소가 나와요'),
    ('考试 330 分钟', '시험은 330분이에요'),
    ('现在时：pede', '현재형: pede'),
    ('每天复习一点', '매일 조금씩 복습해요'),
]

t = load('content56.py')
for old, new in R56K:
    t = sub(t, old, new, fn='content56.py')
save('content56.py', t)

R7K = [
    ('讲一周的事用过去时（pretérito perfeito）；revisar 规则（revisei）；chegar/dormir 的过去时注意重音。', '한 주 일을 말할 때는 과거형(pretérito perfeito)을 써요; revisar는 규칙적이에요(revisei); chegar/dormir의 과거형은 강세에 주의하세요.'),
    ('提问句：que horas（几点）+ 动词；onde fica 问地点；conferir 的 eu 形式不规则：confiro', '의문문: que horas (몇 시) + 동사; onde fica는 장소를 물어요; conferir의 eu 형태는 불규칙해요: confiro'),
    ('聚焦语言 · Três níveis, três ferramentas · 三个级别，三件工具', '언어 집중 · Três níveis, três ferramentas · 세 단계, 세 가지 도구'),
    ('quando、se、quem 后用虚拟式将来：tiver、for、chegar（周日假设）。', 'quando, se, quem 뒤에는 접속법 미래를 써요: tiver, for, chegar (일요일 가정).'),
    ('编辑部说明：上期承诺的真实来信与最佳作文截稿时未收到，本期仍刊示例，顺延至下期。', '편집부 알림: VOL.1에서 약속한 실제 편지와 최고의 작문은 마감 때까지 도착하지 않았어요. 이번 호에는 예시를 싣고, 약속은 VOL.3으로 이어져요.'),
    ('FRASES DA SEMANA · 本周金句（逐字摘自本期文章）', 'FRASES DA SEMANA · 이번 주 금문장 (이 판의 문장 그대로)'),
    ('A PRÓXIMA SEMANA · 下期预告 (VOL.3)', 'A PRÓXIMA SEMANA · 다음 주 예고 (VOL.3)'),
    ('连休是 10 月 31 日到 11 月 2 日，共三天。', '연휴는 10월 31일부터 11월 2일까지, 모두 3일이에요.'),
    ('conferir：eu → confiro（不规则）', 'conferir: eu → confiro (불규칙)'),
    ('编辑部示例，非真实来信。真实来信请寄编辑部，下期见！', '편집부 예시예요, 실제 편지가 아니에요. 여러분의 편지를 편집부로 보내 주세요! VOL.3에 실어요!'),
    ('chegaram 是 chegar 的过去时复数', 'chegaram은 chegar의 과거형 복수예요'),
    ('conferir：você → confere', 'conferir: você → confere'),
    ('quando + 未来 → 虚拟式将来 for', 'quando + 미래 → 접속법 미래 for'),
    ('quando + 虚拟式将来：chegar', 'quando + 접속법 미래: chegar'),
    ('feriadão = 连休长周末，共三天。', 'feriadão = 주말과 이어진 연휴, 모두 3일이에요.'),
    ('começar：ela → começa', 'começar: ela → começa'),
    ('revisar 过去时：revisei', 'revisar 과거형: revisei'),
    ('se + ser 的虚拟式将来：for', 'se + ser의 접속법 미래: for'),
    ('ERROS COMUNS · 常见错误', 'ERROS COMUNS · 흔한 실수'),
    ('quem + 虚拟式将来：tiver', 'quem + 접속법 미래: tiver'),
    ('13 点关门，13:30 到就晚了。', '13시에 문이 닫혀요, 13:30에 도착하면 늦어요.'),
    ('每一分值一个名次，每一球值一个故事。', '1점은 한 순위, 1골은 한 이야기예요.'),
    ('chegar 过去时：chegou', 'chegar 과거형: chegou'),
    ('dormir 过去时：dormiu', 'dormir 과거형: dormiu'),
    ('考前一夜突击没用，睡好才记得住。', '시험 전날 밤 벼락치기는 소용없어요, 푹 자야 기억이 나요.'),
    ('A PALAVRA · 本周生词', 'A PALAVRA · 이번 주 단어'),
    ('许多人旅行、探亲、去墓园献花。', '많은 사람들이 여행하고, 가족을 만나고, 묘지에 꽃을 가져가요.'),
    ('核对确认卡、睡好、早到。', '확인 카드를 확인하고, 푹 자고, 일찍 도착하세요.'),
    ('LÍNGUA · 语言', 'LÍNGUA · 언어'),
    ('高考用黑笔，蓝笔不行。', '엔엠에는 검은 펜을 써요, 파란 펜은 안 돼요.'),
    ('从连休到考试：高考周。', '연휴에서 시험까지: 엔엠 주간.'),
    ('怀念是继续亲近的方式。', '추억하는 것은 가까이 지내는 방법이에요.'),
    ('先做容易的，再做难的。', '쉬운 것부터, 어려운 것은 나중에.'),
    ('亡灵节是怀念的日子。', '위령절은 추억의 날이에요.'),
    ('onde 问地点', 'onde는 장소를 물어요'),
    ('睡得好，记得牢。', '푹 자면 잘 기억나요.'),
]

t = load('content7.py')
for old, new in R7K:
    t = sub(t, old, new, fn='content7.py')
save('content7.py', t)

R8K = [
    ('第 8 版 · A grande prova da semana + todas as respostas', '제8면 · A grande prova da semana + todas as respostas'),
    ('RESPOSTAS · 参考答案 — 按版面分页排列，找到题号即可', 'RESPOSTAS · 정답 — 면마다 나눠 실었어요, 번호로 찾으세요'),
    ('“连休是 10 月 31 日到 11 月 2 日。” → ___', '“연휴는 10월 31일부터 11월 2일까지예요.” → ___'),
    ('segunda chamada=关门后的再入场（高考没有） c', 'segunda chamada=문이 닫힌 뒤의 재입장 (엔엠에는 없어요) c'),
    ('AVALIAÇÃO E RESPOSTAS · 练习与答案', 'AVALIAÇÃO E RESPOSTAS · 평가와 정답'),
    ('写作题（无唯一答案）；范文（{NWORDS} 词）见下。', '쓰기 문제예요 (하나의 정답은 없어요); 모범 답안은 아래에 있어요 ({NWORDS} 단어).'),
    ('虚拟式将来 chegar + 祈使 apresente', '접속법 미래 chegar + 명령형 apresente'),
    ('documento com foto 带照片的证件', 'documento com foto 사진이 있는 신분증'),
    ('米内罗竞技 × 格雷米奥次回合在 MRV 竞技场', '아틀레치쿠 미네이루 × 그레미우 2차전은 MRV 경기장에서 있어요'),
    ('连休从 10 月 31 日到 11 月 2 日', '연휴는 10월 31일부터 11월 2일까지예요'),
    ('你到达时，请出示带照片的证件。 → ___', '도착하면 사진이 있는 신분증을 보여 주세요. → ___'),
    ('范文见本版 H 区（{NWORDS} 词）', '모범 답안은 이 면 H 칸에 있어요 ({NWORDS} 단어)'),
    ('每题附一句中文简析 · 带 ✓ 的为范文题', '각 답마다 짧은 해설이 있어요 · ✓는 모범 답안 문제예요'),
    ('瓦斯科 × 帕尔梅拉斯次回合在 8 日', '바스쿠 × 파우메이라스 2차전은 8일에 있어요'),
    ('reta final=考前最后一周 a', 'reta final=시험 전 마지막 한 주 a'),
    ('11 月 8 日周日是高考的第一天。', '11월 8일 일요일은 엔엠 첫날이에요.'),
    ('feriadão=连着周末的假期 b', 'feriadão=주말과 이어진 연휴 b'),
    ('主语 + 动词 + 宾语 + 地点', '주어 + 동사 + 목적어 + 장소'),
    ('第 2 天在 11 月 15 日', '둘째 날은 11월 15일이에요'),
    ('万圣节在 10 月 31 日周六', '핼러윈은 10월 31일 토요일이었어요'),
    ('seção = 考场分区（房间）', 'seção = 시험장 구역 (교실)'),
    ('第 1 天在 11 月 8 日', '첫날은 11월 8일이에요'),
    ('第 34 轮周一到周五都有比赛', '34라운드는 월요일부터 금요일까지 경기가 있어요'),
    ('前一晚他备好证件和黑笔、早睡', '전날 밤 그는 신분증과 검은 펜을 챙기고 일찍 자요'),
    ('亡灵节在 11 月 2 日', '위령절은 11월 2일이에요'),
    ('连休里他休息并每天复习一点', '연휴 동안 그는 쉬고 매일 조금씩 복습해요'),
    ('Confira = 请核对', 'Confira = 확인하세요'),
    ('feriadão = 连休', 'feriadão = 연휴'),
    ('portão=考场入口 d', 'portão=시험장 입구 d'),
    ('obrigado = 谢谢', 'obrigado = 고마워요'),
    ('主语 + 动词 + 宾语', '주어 + 동사 + 목적어'),
    ('考试时长 5 个半小时', '시험 시간은 5시간 반이에요'),
    ('330 是考试的分钟数', '330은 시험 분 수예요'),
    ('卢卡斯住在贝洛奥里藏特', '루카스는 벨루오리존치에 살아요'),
    ('考试 13:30 开始', '시험은 13:30에 시작해요'),
    ('亡灵节又称诸圣灵魂日', '위령절은 모든 충실한 영혼의 날이라고도 불러요'),
    ('他 11 点到达考场', '그는 11시에 시험장에 도착해요'),
    ('（开放题，范文如下）', '(열린 문제 — 모범 답안은 아래에 있어요)'),
    ('确认卡是高考的文件', '확인 카드는 엔엠 서류예요'),
    ('对照第 6 版标题', '6면 제목을 보세요'),
    ('周日前核对确认卡。', '일요일 전에 확인 카드를 확인하세요.'),
    ('大门 13 点关闭', '문은 13시에 닫혀요'),
    ('13:30 开考', '13:30에 시작해요'),
    ('亡灵节家人们带花', '위령절에 가족들은 꽃을 가져가요'),
    ('连休共 3 天', '연휴는 모두 3일이에요'),
    ('疑问词组在句首', '의문사구가 문장 앞에 와요'),
    ('13 点关门', '13시에 문이 닫혀요'),
    ('时间词在前', '시간 단어가 앞에 와요'),
]

t = load('content8.py')
for old, new in R8K:
    t = sub(t, old, new, fn='content8.py')
save('content8.py', t)

# ---------- 4. line-anchored + structural replacements ----------
t = load('content12.py')
# P1 edition line: 40pt measures 1603.7px < 1820 (W43 PT x KO kept 40pt)
t = line_replace(t, 'p.text(975, 330,',
    'p.text(975, 330, "포르투갈어 주간지 · VOL.2 · A SEMANA DO ENEM · FINADOS · O FUTEBOL DECIDE", 40, "serif", True, INK, anchor="middle")',
    'content12.py')
# P1 badge: W43 PT x KO verbatim, BRICK 19.5pt bold, 372 slot (replaces
# the masthead strapline line there, as the W45 PT x ES sibling did)
t = line_replace(t, 'p.text(975, 372,',
    'p.text(975, 372, "포르투갈어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판", 19.5, "sans", True, BRICK, anchor="middle")',
    'content12.py')
save('content12.py', t)

t = load('content7.py')
# rename the disclosure variable (definition, height formula, draw line)
assert t.count('disc_cn') == 3, f"content7.py disc_cn count {t.count('disc_cn')}"
t = t.replace('disc_cn', 'disc_ko')
save('content7.py', t)

t = load('content8.py')
# P8 answer-group separator: W43 PT x KO form (with spaces)
t = sub(t, 'f"— PÁGINA {pg} —"', 'f"— 제 {pg} 면 —"', 'content8.py')
save('content8.py', t)

# ---------- 5. verify: zero CJK + zero full-width CJK punctuation ----------
for fn in ['bslib4.py', 'content12.py', 'content34.py', 'content56.py', 'content7.py', 'content8.py']:
    t = load(fn)
    hits = CJK.findall(t)
    assert not hits, f'{fn}: {len(hits)} CJK chars remain, e.g. {hits[:10]}'
    fw = FWP.findall(t)
    assert not fw, f'{fn}: full-width punctuation remains: {fw[:10]}'
    print(f'{fn}: CJK 0 + full-width punct 0 OK')
print('TRANSFORM COMPLETE')

# ---------- 6. Round-2 fixes (KO -> KO, wrap-simulated; each verified CLEAN
#     by /tmp/sim_wrap.py / /tmp/sim_p8.py before adoption) ----------
def fix(fn, old, new):
    global _t
    t = load(fn)
    t = sub(t, old, new, fn=fn)
    save(fn, t)

# S3: P3 E VOCE prompt (추|억해요) -> 기려요 (tail-2 minor only)
fix('content34.py',
    '여러분 문화에서는 돌아가신 분들을 어떻게 추억해요? 두 문장을 써서 보내 주세요.',
    '여러분 문화에서는 돌아가신 분들을 어떻게 기려요? 두 문장을 써서 보내 주세요.')
# S1: P5 E VOCE prompt (stranded comma) -> comma-free rewrite
fix('content56.py',
    '중요한 시험 전날 밤, 여러분 계획은 복습이에요, 휴식이에요? 두 문장을 써서 보내 주세요.',
    '중요한 시험 전날 밤에는 복습해요? 쉬어요? 두 문장을 써서 보내 주세요.')
# S3: P5 plan item 2 (벼락|치기는) -> 복습해요/없어요 form (tail-2 minor only)
fix('content56.py',
    '2. Revise um pouco por dia, sem maratona (매일 조금씩 복습하세요, 벼락치기는 안 돼요)',
    '2. Revise um pouco por dia, sem maratona (매일 조금씩 복습해요, 벼락치기는 없어요)')
# S3: P5 plan item 4 (챙|기세요) -> 전날에 form (whole word on last line)
fix('content56.py',
    '4. Separe documento e caneta preta no dia anterior (전날 신분증과 검은 펜을 챙기세요)',
    '4. Separe documento e caneta preta no dia anterior (전날에 신분증과 검은 펜을 챙기세요)')
# S3: P6 gloss (확|인하다) -> drop second synonym (P8 note keeps full gloss)
fix('content56.py',
    'os portões 문 · a segunda chamada 재입장, 두 번째 입장 · conferir 확인하다 · a correria 서두름.',
    'os portões 문 · a segunda chamada 재입장 · conferir 확인하다 · a correria 서두름.')
# Stail: P7 clinic note 4 (에요.) -> single line
fix('content7.py',
    '연휴는 10월 31일부터 11월 2일까지, 모두 3일이에요.',
    '연휴는 10월 31일부터 11월 2일까지 3일이에요.')
# Stail: P7 word-box gloss (요.) -> single line (formula + draw lines both)
fix('content7.py',
    'feriadão = 주말과 이어진 연휴, 모두 3일이에요.',
    'feriadão = 주말과 이어진 3일 연휴예요.')
# Stail: P7 invitation (요!) -> keep full meaning, 2 lines (formula + draw)
fix('content7.py',
    '편집부 예시예요, 실제 편지가 아니에요. 여러분의 편지를 편집부로 보내 주세요! VOL.3에 실어요!',
    '편집부 예시예요, 실제 편지가 아니에요. 편지를 편집부로 보내 주세요! VOL.3에 실어요!')
# Stail: P7 disclosure (져요.) -> 오지 않았어요 form, 3 lines (formula + draw)
fix('content7.py',
    '편집부 알림: VOL.1에서 약속한 실제 편지와 최고의 작문은 마감 때까지 도착하지 않았어요. 이번 호에는 예시를 싣고, 약속은 VOL.3으로 이어져요.',
    '편집부 알림: VOL.1에서 약속한 실제 편지와 최고의 작문은 마감 때까지 오지 않았어요. 이번 호에는 예시를 싣고, 약속은 VOL.3으로 이어져요.')
# Stail: P8 item 45 note (장소 alone) -> compact form, content34 only
# (content8's identical note stays spaced: its item 134 wraps CLEAN)
fix('content34.py',
    '"주어 + 동사 + 목적어 + 장소"',
    '"주어+동사+목적어+장소"')
# Stail: P8 item 48 note (예요 alone) -> noun-phrase form, all facts kept
fix('content34.py',
    '바스쿠 × 파우메이라스 2차전은 일요일 8일 17시, 상 자누아리우예요',
    '바스쿠 × 파우메이라스 2차전: 8일 일요일 17시, 상 자누아리우')
# Stail: P8 item 123 note (어요 alone) -> MRV에서 form, single line
fix('content8.py',
    '아틀레치쿠 미네이루 × 그레미우 2차전은 MRV 경기장에서 있어요',
    '아틀레치쿠 미네이루 × 그레미우 2차전은 MRV에서 있어요')
# Stail: P8 item 139 note (연휴 alone) -> 연휴예요, last line 4 syllables
fix('content8.py',
    '"feriadão = 연휴"',
    '"feriadão = 연휴예요"')
print('ROUND-2 FIXES APPLIED')

# ---------- 6b. Round-3 layout fix (no content change) ----------
# P7 quotes still reached y=2417 into the preview box (2404) after the
# round-2 shrink (letters box still 59px taller than core: disc_ko 3 lines
# vs disc_cn 2). Tighten quote row pitch 128 -> 104 (W45 PT x ES precedent):
# last-row translation 2417 -> 2345, clear of the box; rows are 1 PT line +
# 1 translation line (row height 97 < 104), verified by occlusion audit.
t = load('content7.py')
t = line_replace(t, 'cyq = fy + 66',
    '    cyq = fy + 66 + (i % 4) * 104  # KO: tightened from 128 (ES precedent) so quotes clear the preview box',
    'content7.py')
save('content7.py', t)
print('ROUND-3 QUOTE SPACING APPLIED')
