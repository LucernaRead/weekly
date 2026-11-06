# -*- coding: utf-8 -*-
"""PT core (zh explanations) -> PT x KO fan-out transform for W46 VOL.3.

Run inside the already-copied build dir. Every replacement is an exact
literal match (longest strings first); missing literals warn. The final
pass asserts no Chinese source literal survives (KO explanations
legitimately use Hangul; adjudication is via freeze diff).
Frozen Portuguese text, the P7 example letter (lt), the PT disclosure
(disc_pt) and the P7 quote strings + page tags are never touched.
P1 subtitle (330) and badge (372) lines are replaced whole (size/color).
Subtitle size 38pt is measured (40pt overflows the page frame).
P7 geometry keeps the core values (KO text is compact); P8 keeps the
core 13.5pt answers size; the P8 separator stays Portuguese.
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
        t = t.replace('weekly-report-w46-pt-core', 'weekly-report-w46-pt-ko')
        save(fn, t)
t = load('render.py')
t = sub(t, 'A-Lucerna-VOL3.pdf', 'Lucerna-VOL3-KO.pdf', 'render.py')
save('render.py', t)

# ---------- 1. bslib4 furniture ----------
t = load('bslib4.py')
t = sub(t, 'A Lucerna · 葡萄牙语周报 VOL.3 · LUCERNA PORTUGUESE WEEKLY',
        'A Lucerna · 포르투갈어 주간지 VOL.3 · 텍스트는 포르투갈어 · 해설은 한국어', 'bslib4.py')
t = sub(t, 'f"第 {n} 版 / 共 {total} 版"', 'f"제 {n} 면 / 총 {total} 면"', 'bslib4.py')
t = sub(t, '("译注｜" + s', '("해설 — " + s', 'bslib4.py')
save('bslib4.py', t)

# ---------- 2. P1 masthead lines (whole-line) ----------
t = load('content12.py')
t = line_replace(t, 'p.text(975, 330,',
    'p.text(975, 330, "포르투갈어 주간지 · VOL.3 · ENEM, DIA 2 · PROCLAMAÇÃO DA REPÚBLICA · O FUTEBOL DECIDE", 38, "serif", True, INK, anchor="middle")',
    'content12.py')
t = line_replace(t, 'p.text(975, 372,',
    'p.text(975, 372, "포르투갈어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판", 19.5, "sans", True, BRICK, anchor="middle")',
    'content12.py')
save('content12.py', t)

# ---------- 3. type / instr labels ----------
INSTR = [
    ('instr="造句"', 'instr="문장 만들기"'),
    ('instr="翻译"', 'instr="번역하기"'),
    ('instr="判断"', 'instr="맞는지 틀린지"'),
    ('instr="写作"', 'instr="쓰기"'),
    ('instr="填空"', 'instr="빈칸 채우기"'),
    ('instr="把词和释义配对"', 'instr="단어와 뜻 연결하기"'),
]
TYP = [
    ('"完成句子"', '"문장 완성하기"'),
    ('"词汇配对"', '"어휘 연결하기"'),
    ('"判断对错"', '"정오 판단"'),
    ('"完形单选"', '"빈칸 채우기"'),
    ('"单选"', '"객관식"'),
    ('"造句"', '"문장 만들기"'),
    ('"翻译"', '"번역"'),
    ('"写作"', '"작문"'),
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
    ('NÍVEL A2 · Prova e feriado no mesmo domingo', '수준 A2 · 시험과 공휴일이 같은 일요일'),
    ('A2 → B1 · Proclamação da República: 137 anos · 共和国宣言 137 周年', 'A2 → B1 · Proclamação da República: 137년'),
    ('NÍVEL B1 · O futebol da semana · 足球之周', '수준 B1 · 이번 주 축구'),
    ('NÍVEL B1 · A última semana dos jovens · 最后一周：年轻人的冲刺', '수준 B1 · 젊은이들의 마지막 한 주'),
    ('NÍVEL B2 · O segundo domingo explicado · 第二个周日详解', '수준 B2 · 두 번째 일요일 해설'),
    ('聚焦语言 · Três níveis, três ferramentas · 三个级别，三件工具', 'Três níveis, três ferramentas · 세 단계, 세 가지 도구'),
    ('第 8 版 · A grande prova da semana + todas as respostas', '8면 · 이번 주의 큰 시험 + 모든 정답'),
    # top strip / kickers
    ('TODA SEMANA EM PORTUGUÊS · 每周一期 · 读巴西人正在读的葡萄牙语', 'TODA SEMANA EM PORTUGUÊS · 브라질이 읽는 포르투갈어를 매주'),
    ('A NOTÍCIA · 头条', 'A NOTÍCIA · 톱기사'),
    ('VIDA · 生活', 'VIDA · 생활'),
    ('CULTURA · 文化', 'CULTURA · 문화'),
    ('ESPORTE · 体育', 'ESPORTE · 스포츠'),
    ('JOVENS · 青年', 'JOVENS · 청년'),
    ('APROFUNDAMENTO · 深读', 'APROFUNDAMENTO · 심층 읽기'),
    ('LÍNGUA · 语言', 'LÍNGUA · 언어'),
    ('AVALIAÇÃO E RESPOSTAS · 练习与答案', 'AVALIAÇÃO E RESPOSTAS · 평가와 정답'),
    # P1
    ('高考第二天', 'ENEM 둘째 날'),
    ('11 月 15 日第二场考试 · 共和国宣言日假期', '11월 15일: 두 번째 시험일 · 공화국 선포 기념 공휴일'),
    ('讲解｜a proclamação 宣布、宣告 · o feriado 假日 · a natureza 自然科学 · a matemática 数学。', '핵심 단어 | a proclamação = 선포 · o feriado = 공휴일 · a natureza = 자연과학 · a matemática = 수학.'),
    ('A SEMANA EM NÚMEROS · 数字', 'A SEMANA EM NÚMEROS · 숫자로 보는 한 주'),
    ('12h — os portões abrem no domingo 15（周日 12 点开门）', '12h — os portões abrem no domingo 15（일요일 12시 개문）'),
    ('13h — os portões fecham（13 点关门，过时不入）', '13h — os portões fecham（13시 폐문, 지각하면 입장 불가）'),
    ('13h30–18h30 — a prova do dia 15（考试 13:30 至 18:30）', '13h30–18h30 — a prova do dia 15（15일 시험, 13:30~18:30）'),
    ('90 — as questões do dia 15: 45 + 45（90 道题：45 + 45）', '90 — as questões do dia 15: 45 + 45（90문제: 45 + 45）'),
    ('AGORA VOCÊ · 即学即练', 'AGORA VOCÊ · 이제 당신 차례'),
    ('proclamação = 宣布（共和国宣言）', 'proclamação = 선포（공화국 선포）'),
    ('proclamação = 宣布（共和国宣言）。', 'proclamação = 선포（공화국 선포）。'),
    ('feriado = 假日', 'feriado = 공휴일'),
    ('portões = 大门（考场大门）', 'portões = 정문（시험장 정문）'),
    ('18h30 结束', '18시 30분 종료'),
    ('90 道题', '90문제'),
    ('fazer 现在时 eles 形式：fazem', 'fazer 현재형 eles형: fazem'),
    ('迟到不得入内：13 点后关门', '13시가 지나면 들어갈 수 없어요.'),
    ('NESTA EDIÇÃO · 本期目录', 'NESTA EDIÇÃO · 이번 호 차례'),
    ('EM POUCAS PALAVRAS · 快讯', 'EM POUCAS PALAVRAS · 단신'),
    ('QUIZ RELÂMPAGO · 闪电问答', 'QUIZ RELÂMPAGO · 번개 퀴즈'),
    ('读头版，选出正确答案 · 答案见第 8 版', '1면을 읽고 고르세요 · 정답은 8면'),
    ('共和国宣言日在 11 月 15 日', '공화국 선포의 날은 11월 15일'),
    ('13 点关门', '13시 폐문'),
    ('第 2 天考自然科学与数学', '둘째 날은 자연과학과 수학'),
    ('18:30 结束', '18:30 종료'),
    # P2
    ('PARA NÃO ERRAR · 口诀', 'PARA NÃO ERRAR · 외우는 요령'),
    ('a proclamação 宣布 · o feriado 假日 · a natureza 自然科学 · a matemática 数学 · conferir 核对 · a escala 排班。', 'a proclamação = 선포 · o feriado = 공휴일 · a natureza = 자연과학 · a matemática = 수학 · conferir = 확인하다 · a escala = 근무표.'),
    ('在你的国家，落在周日的假日会在周一补休吗？写两句寄来。', '당신 나라에서는 일요일에 겹친 공휴일을 월요일에 쉴 수 있나요? 두 문장을 써서 보내 주세요.'),
    ('E VOCÊ? · 说说你自己', 'E VOCÊ? · 당신은요?'),
    ('OS HORÁRIOS DO DOMINGO 15 · 周日时间表', 'OS HORÁRIOS DO DOMINGO 15 · 15일 일요일 시간표'),
    ('Um país, vários relógios · 一个国家，几个时区', 'Um país, vários relógios · 한 나라, 여러 개의 시계'),
    ('周日 12 点开门', '일요일 12시 개문'),
    ('13:30 开考', '13:30 시험 시작'),
    ('EXERCÍCIOS · 第 2 版练习', 'EXERCÍCIOS · 2면 연습 문제'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', '정답은 8면 · 수준이 섞여 있어요. 번호로 찾으세요'),
    ('读第 2 版文章，选出正确答案。', '2면 기사를 읽고 정답을 고르세요.'),
    ('假日落在周日，周一不补休', '공휴일이 일요일에 겹쳐도 월요일에 쉬지 않아요'),
    # P7-clinic/.text.md variant of the line above: the source carries a trailing 。 (F-2/F-3).
    ('假日落在周日，周一不补休。', '공휴일이 일요일에 겹쳐도 월요일에 쉬지 않아요.'),
    ('确认卡显示考试地点', '확인 카드에 시험 장소가 나와요'),
    ('巴西没有夏令时，钟表不动', '브라질에는 서머타임이 없어요. 시계는 그대로예요'),
    ('补全动词的现在时形式。', '동사의 현재형으로 완성하세요.'),
    ('用第 1、2 版的数字填空。', '1·2면의 숫자로 채우세요.'),
    ('12 点到 13 点 = 1 小时', '12시부터 13시 = 1시간'),
    ('13:30 至 18:30 = 5 小时', '13:30부터 18:30 = 5시간'),
    ('5×60 = 300 分钟', '5×60 = 300분'),
    ('proclamação=宣布一个变化 b', 'proclamação = 변화를 선포하는 것 (b)'),
    ('feriado=法律规定的休息日 c', 'feriado = 법으로 정한 휴일 (c)'),
    ('natureza=生命、物理与化学的科学 d', 'natureza = 생명·물리·화학의 과학 (d)'),
    ('matemática=数字与图形的科学 a', 'matemática = 수와 도형의 과학 (a)'),
    ('把词和释义配对', '단어와 뜻을 연결하세요'),
]
REPL += [
    # P3
    ('a monarquia 君主制 · a república 共和国 · o marechal 元帅 · o exílio 流亡 · o governo 政府 · a lei 法律。', 'a monarquia = 군주제 · a república = 공화국 · o marechal = 원수 · o exílio = 망명 · o governo = 정부 · a lei = 법률.'),
    ('在你的国家，有纪念共和国建立的假日吗？写两句寄来。', '당신 나라에는 공화국 건국을 기념하는 공휴일이 있나요? 두 문장을 써서 보내 주세요.'),
    ('EXERCÍCIOS · 第 3 版练习', 'EXERCÍCIOS · 3면 연습 문제'),
    ('读第 3 版文章，选出正确答案。', '3면 기사를 읽고 정답을 고르세요.'),
    ('共和国宣言在 1889 年 11 月 15 日', '공화국 선포는 1889년 11월 15일'),
    ('德奥多罗成为巴西第一任总统', '데오도루가 브라질 초대 대통령이 되었어요'),
    ('全国性假日，任何城市都不能改为工作日', '전국적인 공휴일. 어떤 도시도 근무일로 바꿀 수 없어요'),
    ('2026 年假日落在周日', '2026년에는 공휴일이 일요일에 겹쳐요'),
    ('共和国里总统由选举产生、任期有限', '공화국에서는 대통령이 선거로 뽑히고 임기에 제한이 있어요'),
    ('用方框里的词填空。', '네모 안의 단어로 채우세요.'),
    ('monarquia = 君主制', 'monarquia = 군주제'),
    ('república = 共和国', 'república = 공화국'),
    ('marechal = 元帅', 'marechal = 원수'),
    ('exílio = 流亡', 'exílio = 망명'),
    ('governo = 政府', 'governo = 정부'),
    ('lei = 法律', 'lei = 법률'),
    ('用过去时（pretérito perfeito）补全。', '과거형(pretérito perfeito)으로 완성하세요.'),
    ('tomar 过去时 elas 形式：tomaram', 'tomar 과거형 elas형: tomaram'),
    ('acabar 过去时 ela 形式：acabou', 'acabar 과거형 ela형: acabou'),
    ('ser 过去时 ele 形式：foi', 'ser 과거형 ele형: foi'),
    ('assumir 过去时 ele 形式：assumiu', 'assumir 과거형 ele형: assumiu'),
    ('把词组成正确的句子。', '단어를 올바른 순서로 배열하세요.'),
    ('主语 + é + 表语', '주어 + é + 보어'),
    ('主语 + 动词 + 表语', '주어 + 동사 + 보어'),
    ('主语 + 动词 + 宾语 + 时间', '주어 + 동사 + 목적어 + 시간'),
    # P4
    ('a ida 首回合 · a volta 次回合 · o gol 进球 · o pênalti 点球 · a pausa 休整期 · o amistoso 友谊赛。', 'a ida = 1차전 · a volta = 2차전 · o gol = 골 · o pênalti = 페널티킥 · a pausa = 휴식기 · o amistoso = 친선 경기.'),
    ('你在巴西杯支持哪支球队？谁能进决赛？写两句寄来。', '코파 두 브라지우에서는 어느 팀을 응원하세요? 결승에는 누가 오를까요? 두 문장을 써서 보내 주세요.'),
    ('A SEMANA DO FUTEBOL · 足球周历', 'A SEMANA DO FUTEBOL · 축구 주간'),
    ('EXERCÍCIOS · 第 4 版练习', 'EXERCÍCIOS · 4면 연습 문제'),
    ('读第 4 版文章，选出正确答案。', '4면 기사를 읽고 정답을 고르세요.'),
    ('首回合格雷米奥 2 比 0 战胜米内罗竞技', '1차전, 그레미우가 아틀레치쿠 MG를 2대 0으로 이겼어요'),
    ('帕尔梅拉斯 1 比 0 战胜瓦斯科，毛里西奥进球', '파우메이라스가 바스쿠를 1대 0으로 이겼어요. 마우리시우가 득점했어요'),
    ('次回合米内罗竞技 × 格雷米奥在周六 7 日 18 点', '2차전 아틀레치쿠 MG × 그레미우는 토요일 7일 18시'),
    ('决赛 12 月 6 日单场，在马内·加林查', '결승은 12월 6일 단판 승부, 마네 가힌샤에서'),
    ('第 35 轮本周只有一场：米拉索尔 × 米内罗竞技', '35라운드는 이번 주 한 경기뿐: 미라솔 × 아틀레치쿠 MG'),
    ('gol=射入球网的得分 b', 'gol = 골대에 넣은 득점 (b)'),
    ('ida=对决的第一场 d', 'ida = 대결의 첫 번째 경기 (d)'),
    ('volta=对决的第二场 a', 'volta = 대결의 두 번째 경기 (a)'),
    ('pênalti=十一米点的罚球 c', 'pênalti = 11m 지점에서의 슛 (c)'),
    ('用括号里正确的比较形式填空。', '괄호 안의 올바른 비교 형태로 채우세요.'),
    ('5 小时 < 5.5 小时：menos', '5시간 < 5.5시간: menos'),
    ('把句子补全成过去时（pretérito perfeito）。', '문장을 과거형(pretérito perfeito)으로 완성하세요.'),
    ('vencer 过去时 ele 形式：venceu', 'vencer 과거형 ele형: venceu'),
    ('marcar 过去时 eles 形式：marcaram', 'marcar 과거형 eles형: marcaram'),
    ('marcar 过去时 ele 形式：marcou', 'marcar 과거형 ele형: marcou'),
    ('convocar 过去时 ele 形式：convocou', 'convocar 과거형 ele형: convocou'),
    ('ser 过去时复数：foram', 'ser 과거형 복수: foram'),
    # P5
    ('1. Confira o Cartão de Confirmação do Enem（核对高考确认卡）', '1. Confira o Cartão de Confirmação do Enem（Enem 확인 카드를 확인하세요）'),
    ('2. Revise um pouco por dia: Natureza e Matemática（每天复习一点：自然科学与数学）', '2. Revise um pouco por dia: Natureza e Matemática（매일 조금씩 복습: 자연과학과 수학）'),
    ('3. Durma bem na véspera da prova（考前一晚睡好）', '3. Durma bem na véspera da prova（시험 전날 밤은 푹 자세요）'),
    ('4. Separe documento e caneta preta no dia anterior（提前一天备好证件和黑笔）', '4. Separe documento e caneta preta no dia anterior（전날 준비）'),
    ('5. Domingo 15: chegue antes das 12h（周日 15 日：12 点前到达）', '5. Domingo 15: chegue antes das 12h（일요일 15일: 12시 전에 도착하세요）'),
    ('a natureza 自然科学 · a matemática 数学 · a maratona 突击马拉松 · a véspera 前夕 · comparar 比较价格 · a cabeça 头脑、状态。', 'a natureza = 자연과학 · a matemática = 수학 · a maratona = 벼락치기 마라톤 · a véspera = 전날 밤 · comparar = 가격을 비교하다 · a cabeça = 머리, 컨디션.'),
    ('重要考试前一晚，你是复习到很晚还是早睡？写两句寄来。', '중요한 시험 전날 밤, 늦게까지 복습하세요, 아니면 일찍 주무세요? 두 문장을 써서 보내 주세요.'),
    ('EXERCÍCIOS · 第 5 版练习', 'EXERCÍCIOS · 5면 연습 문제'),
    ('读第 5 版文章，选出正确答案。', '5면 기사를 읽고 정답을 고르세요.'),
    ('最后一周在 11 月 15 日周日结束', '마지막 한 주는 11월 15일 일요일에 끝나요'),
    ('每天复习一点', '매일 조금씩 복습하기'),
    ('提前一天备好证件和黑笔', '전날에 신분증과 검은 펜 준비하기'),
    ('黑五在 11 月 27 日', '블랙프라이데이는 11월 27일'),
    ('11 月 14 日周六巴西 × 日本 7:15', '11월 14일 토요일 브라질 × 일본 7:15'),
    ('用方框里的词填空。注意：有的词要变成复数。', '네모 안의 단어로 채우세요. 주의: 복수형으로 바꿀 단어가 있어요.'),
    ('última semana = 最后一周', 'última semana = 마지막 한 주'),
    ('inscrito 配合复数：inscritos', 'inscrito는 복수형에 맞추어요: inscritos'),
    ('véspera = 前夕', 'véspera = 전날 밤'),
    ('maratona = 突击马拉松', 'maratona = 벼락치기 마라톤'),
    ('local = 地点', 'local = 장소'),
    ('separar 祈使式：separe', 'separar 명령형: separe'),
    ('用将来时（futuro do presente）补全。', '미래형(futuro do presente)으로 완성하세요.'),
    ('fazer 将来时 eles 不规则形式：farão', 'fazer 미래형 eles 불규칙형: farão'),
    ('mostrar 将来时：mostrará', 'mostrar 미래형: mostrará'),
    ('sair 将来时复数：sairão', 'sair 미래형 복수: sairão'),
    ('chegar 将来时：chegará', 'chegar 미래형: chegará'),
    ('错：考前突击不是好计划，每天复习一点才好', '틀렸어요: 전날 벼락치기는 좋은 계획이 아니에요. 매일 조금씩이 좋아요'),
    ('对：13:30 至 18:30', '맞아요: 13:30부터 18:30까지'),
    # P6
    ('os portões 大门 · a segunda chamada 补考、第二次入场 · conferir 核对 · a correria 匆忙。', 'os portões = 정문 · a segunda chamada = 보충 시험 / 두 번째 입장 · conferir = 확인하다 · a correria = 허둥지둥.'),
    ('O DOMINGO 15 EM NÚMEROS · 11 月 15 日的数字 (horários oficiais do Inep)', 'O DOMINGO 15 EM NÚMEROS · 11월 15일의 숫자 (Inep 공식 시간)'),
    ('EXERCÍCIOS · 第 6 版练习', 'EXERCÍCIOS · 6면 연습 문제'),
    ('看上面两张图，选出正确答案。', '위의 두 그림을 보고 정답을 고르세요.'),
    ('大门开放 60 分钟', '정문은 60분 동안 열려 있어요'),
    ('关门到开考之间等 30 分钟', '폐문부터 시험 시작까지 기다리는 시간은 30분'),
    ('考试 300 分钟', '시험은 300분'),
    ('中午到 18:30 = 6 个半小时', '정오부터 18:30 = 6시간 반'),
    ('图表数字是 Inep 官方时间', '그림의 숫자는 Inep 공식 시간'),
    ('高考分 8 日和 15 日两个周日', 'Enem은 8일과 15일, 두 일요일에 나뉘어요'),
    ('13 点后到场不得入内', '13시가 지나면 들어갈 수 없어요'),
    ('根据句子意思，补全正确的动词形式。', '문장의 뜻에 맞는 올바른 동사 형태로 완성하세요.'),
    ('将来时：começará', '미래형: começará'),
    ('quem + 虚拟式将来：chegar', 'quem + 미래 접속법: chegar'),
    ('现在时：fecham', '현재형: fecham'),
    ('现在时：pede', '현재형: pede'),
    ('用方框里的词填空：portões · segunda chamada · local · conferir', '네모 안의 단어로 채우세요: portões · segunda chamada · local · conferir'),
    ('portões = 大门', 'portões = 정문'),
    ('segunda chamada = 补考、第二次入场', 'segunda chamada = 보충 시험 / 두 번째 입장'),
    ('祈使式：confira', '명령형: confira'),
    # P7
    ('提问句：que horas（几点）+ 动词；onde fica 问地点；conferir 的 eu 形式不规则：confiro', '의문문: que horas(몇 시) + 동사. onde fica는 장소를 묻어요. conferir의 eu형은 불규칙: confiro.'),
    ('conferir：eu → confiro（不规则）', 'conferir: eu → confiro(불규칙)'),
    ('onde 问地点', 'onde는 장소를 물어요'),
    ('讲一周的事用过去时（pretérito perfeito）；vencer 规则（venceu）；marcar/chegar/dormir 的过去时注意重音。', '한 주의 일을 말할 때는 과거형(pretérito perfeito)을 써요. vencer는 규칙적(venceu). marcar·chegar·dormir의 과거형 강세에 주의하세요.'),
    ('vencer 过去时：venceu', 'vencer 과거형: venceu'),
    ('marcar 过去时：marcou', 'marcar 과거형: marcou'),
    ('chegar 过去时：chegou', 'chegar 과거형: chegou'),
    ('venceram 是 vencer 的过去时复数', 'venceram은 vencer의 과거형 복수예요'),
    ('quando、se、quem 后用虚拟式将来：tiver、for、chegar（周日假设）。', 'quando·se·quem 뒤에는 미래 접속법: tiver·for·chegar(일요일 가정의 문법).'),
    ('quem + 虚拟式将来：tiver', 'quem + 미래 접속법: tiver'),
    ('quando + 虚拟式将来：chegar', 'quando + 미래 접속법: chegar'),
    ('se + ser 的虚拟式将来：for', 'se + ser의 미래 접속법: for'),
    ('quando + 未来 → 虚拟式将来 for', 'quando + 미래 → 미래 접속법 for'),
    ('高考用黑笔，蓝笔不行。', '검은 펜만 써요. 파란 펜은 안 돼요.'),
    ('13 点关门，13:30 到就晚了。', '13시 폐문. 13:30에 오면 늦어요.'),
    ('15 日考试 18:30 结束，19 点是 8 日的时间。', '15일 시험은 18:30에 끝나요. 8일은 19시 종료.'),
    ('ERROS COMUNS · 常见错误', 'ERROS COMUNS · 흔한 실수'),
    ('proclamação = 宣布；1889 年君主制结束、共和国开始。', 'proclamação = 선포. 1889년, 군주제가 끝나고 공화국이 시작되었어요.'),
    ('A PALAVRA · 本周生词', 'A PALAVRA · 이번 주 단어'),
    ('编辑部说明：上期（VOL.2）承诺的真实来信与最佳作文截稿时未收到，本期仍刊示例，顺延至下期（VOL.4）。', '편집부 알림: VOL.2에서 약속한 실제 편지와 최고의 작문은 마감 때까지 오지 않았어요. 이번 호에는 예시를 싣고, 약속은 VOL.4로 이어져요.'),
    ('编辑部示例，非真实来信。真实来信请寄编辑部，下期见！', '편집부 예시예요, 실제 편지가 아니에요. 편지를 편집부로 보내 주세요!'),
    ('FRASES DA SEMANA · 本周金句（逐字摘自本期文章）', 'FRASES DA SEMANA · 이번 주의 명문장(이 호 기사에서 그대로 인용)'),
    ('两个周日、一个假日：巴西迎来高考第二天。', '두 번의 일요일, 하나의 공휴일: 브라질은 Enem 둘째 날을 맞이해요.'),
    ('考试和假日在同一天到来。', '시험과 공휴일이 같은 날에 와요.'),
    ('假日不改变时钟。', '공휴일은 시계를 바꾸지 않아요.'),
    ('君主制结束了。', '군주제는 끝났어요.'),
    ('谁能进巴西杯决赛？', '코파 두 브라지우 결승에는 누가 오를까요?'),
    ('睡得好，记得牢。', '잠을 잘 자면 잘 기억해요.'),
    ('先做容易的，再做难的。', '쉬운 것부터, 그다음에 어려운 것.'),
    ('核对确认卡、睡好、早到。', '확인 카드를 확인하고, 푹 자고, 일찍 오세요.'),
    ('A PRÓXIMA SEMANA · 下期预告 (VOL.4)', 'A PRÓXIMA SEMANA · 다음 주 예고 (VOL.4)'),
    # P8
    ('第 2 天在 11 月 15 日', '둘째 날은 11월 15일'),
    ('第 1 天在 11 月 8 日', '첫째 날은 11월 8일'),
    ('确认卡是高考的文件', '확인 카드는 Enem 서류예요'),
    ('共和国宣言日在 11 月 15 日', '공화국 선포의 날은 11월 15일'),
    ('瓦斯科 × 帕尔梅拉斯次回合在 8 日', '바스쿠 × 파우메이라스 2차전은 8일'),
    ('第二天共 90 道题', '둘째 날은 모두 90문제'),
    ('考试时长 5 小时', '시험 시간은 5시간'),
    ('米内罗竞技 × 格雷米奥次回合在 MRV 竞技场', '아틀레치쿠 MG × 그레미우 2차전은 MRV 아레나'),
    ('第 35 轮本周只有一场，在 14 日', '35라운드는 이번 주 한 경기뿐, 14일'),
    ('共和国宣言在 1889 年', '공화국 선포는 1889년'),
    ('11.11 是促销日', '11.11은 세일의 날'),
    ('300 是考试的分钟数', '300은 시험의 분 단위 시간'),
    ('德奥多罗是第一任总统', '데오도루는 초대 대통령'),
    ('玛丽娜住在圣保罗', '마리나는 상파울루에 살아요'),
    ('她每天复习一点自然科学', '그녀는 매일 조금씩 자연과학을 복습해요'),
    ('前一晚她备好证件和黑笔、早睡', '전날 밤, 신분증과 검은 펜을 준비하고 일찍 자요'),
    ('她 11:30 到达考场', '그녀는 11:30에 시험장에 도착해요'),
    ('时间词在前', '시간 말이 앞에 와요'),
    ('主语 + 动词 + 宾语 + 地点', '주어 + 동사 + 목적어 + 장소'),
    ('疑问词组在句首', '의문 어구가 문장 맨 앞에 와요'),
    ('主语 + 动词 + 宾语', '주어 + 동사 + 목적어'),
    ('11 月 15 日周日是高考的第二天。', '11월 15일 일요일은 Enem 둘째 날이에요.'),
    ('对照第 6 版标题', '6면 제목과 대조하세요'),
    ('周日前核对确认卡。', '일요일 전에 확인 카드를 확인하세요.'),
    ('Confira = 请核对', 'Confira = 확인하세요'),
    ('“假日落在周日。” → ___', '“공휴일이 일요일에 겹쳐요.” → ___'),
    ('虚拟式将来 chegar + 祈使 apresente', '미래 접속법 chegar + 명령형 apresente'),
    ('你到达时，请出示带照片的证件。 → ___', '도착하면 사진이 있는 신분증을 보여 주세요. → ___'),
    ('proclamação=宣布一个变化 b', 'proclamação = 변화를 선포하는 것 (b)'),
    ('portão=考场入口 d', 'portão = 시험장 입구 (d)'),
    ('república=1889 年后的国家形式 a', 'república = 1889년 이후의 국가 형태 (a)'),
    ('segunda chamada=关门后的再入场（高考没有） c', 'segunda chamada = 폐문 후 재입장(Enem에는 없어요) (c)'),
    ('documento com foto 带照片的证件', 'documento com foto = 사진이 있는 신분증'),
    ('seção = 考场分区（房间）', 'seção = 시험실(구역)'),
    ('大门 13 点关闭', '정문은 13시에 닫혀요'),
    ('考试 18:30 结束', '시험은 18:30에 끝나요'),
    ('obrigado = 谢谢', 'obrigado = 고마워요'),
    ('写作题（无唯一答案）；范文（{NWORDS} 词）见下。', '작문 문제(유일한 정답 없음). 모범 답안({NWORDS}단어)은 아래에 있어요.'),
    ('（开放题，范文如下）', '(열린 문제, 모범 답안은 아래)'),
    ('范文见本版 H 区（{NWORDS} 词）', '모범 답안은 이 면 H란({NWORDS}단어)'),
    ('RESPOSTAS · 参考答案 — 按版面分页排列，找到题号即可', 'RESPOSTAS · 정답 — 면별로 배열했어요. 번호를 찾으세요'),
    ('每题附一句中文简析 · 带 ✓ 的为范文题', '각 문제에 한 줄 해설 · ✓는 작문 문제'),
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

# ---------- 5. disclosure rename + word-box pad ----------
t = load('content7.py')
assert t.count('disc_cn') == 3, f"content7.py disc_cn count {t.count('disc_cn')}"
t = t.replace('disc_cn', 'disc_ko')
old_wh = 'len(wrap("proclamação = 선포. 1889년, 군주제가 끝나고 공화국이 시작되었어요.", "sans", False, 20, CW - 44)) * 29 + 20'
assert t.count(old_wh) == 1, 'word-box pad line not found'
t = t.replace(old_wh, 'len(wrap("proclamação = 선포. 1889년, 군주제가 끝나고 공화국이 시작되었어요.", "sans", False, 20, CW - 44)) * 29 + 30')
save('content7.py', t)

t = load('content12.py')
old_box = '    ("90 — as questões do dia 15: 45 + 45（90문제: 45 + 45）", "serif", False, INK, 20, 1.35),\n])'
assert t.count(old_box) == 1, 'numbers box close not found'
t = t.replace(old_box, old_box[:-2] + '], tsize=20)')
save('content12.py', t)

# ---------- 5b. P7 geometry (KO translations run longer than core) ----------
t = load('content7.py')
t = sub(t, 'fy = max(1712, ly + lh + 44)', 'fy = max(1712, ly + lh + 30)', 'content7.py')
t = sub(t, 'cyq = fy + 66 + (i % 4) * 108', 'cyq = fy + 66 + (i % 4) * 94', 'content7.py')
save('content7.py', t)

# ---------- 5c. FIX F-1 (Round 1 proofread): fullwidth colon in P8 notes ----------
# The 10 note strings below are pure Portuguese (no CJK gloss) inherited from
# the core register with U+FF1A (：). In Latin-script editions they must use
# an ASCII colon, matching neighbouring notes (e.g. item 101). CJK editions
# (ja/zh-cn/zh-tw) legitimately keep ： inside CJK glosses, so this block is
# present ONLY in the 8 Latin-script transforms. Runs after the REPL loop.
for _fn, _old, _new in [
    ("content12.py", "conferir：ele → confere", "conferir: ele → confere"),
    ("content12.py", "abrir：ele → abre", "abrir: ele → abre"),
    ("content12.py", "levar：nós → levamos", "levar: nós → levamos"),
    ("content12.py", "começar：ela → começa", "começar: ela → começa"),
    ("content12.py", "terminar：ela → termina", "terminar: ela → termina"),
    ("content34.py", "2 > 0：mais", "2 > 0: mais"),
    ("content34.py", "3 > 2：mais", "3 > 2: mais"),
    ("content34.py", "17 < 18：mais cedo", "17 < 18: mais cedo"),
    ("content7.py", "conferir：você → confere", "conferir: você → confere"),
    ("content7.py", "terminar：ela → termina", "terminar: ela → termina"),
]:
    _t = load(_fn)
    _t = sub(_t, _old, _new, _fn)
    save(_fn, _t)

# ---------- 5d. FIX F-3 geometry (Round 1): clinic gloss width ----------
# The item-4 Korean gloss + "." overflows CW-44 by 1.44 px, orphaning the "."
# on its own line. Widen ONLY the gloss wrap/para to CW-40 (right margin
# 22 px -> 18 px, still inside the box). The other three glosses wrap
# identically at CW-40 (verified by measurement), so only this line changes
# (2 lines -> 1) and eh/wy recompute consistently from the same formula.
t = load('content7.py')
_old_eh = 'len(wrap(r[2], "sans", False, 19.5, CW - 44))'
assert t.count(_old_eh) == 1, 'clinic eh gloss wrap not found'
t = t.replace(_old_eh, 'len(wrap(r[2], "sans", False, 19.5, CW - 40))')
_old_para = 'yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10'
assert t.count(_old_para) == 1, 'clinic gloss para not found'
t = t.replace(_old_para, _old_para.replace('CW - 44', 'CW - 40'))
save('content7.py', t)

# ---------- 6. verify: every REPL source literal is gone ----------
for fn in ['bslib4.py', 'content12.py', 'content34.py', 'content56.py', 'content7.py', 'content8.py']:
    t = load(fn)
    left = [old for old, _new in REPL if old != _new and old in t and old not in _new]
    assert not left, f'{fn}: untranslated literals remain: {left[:5]}'
    print(f'{fn}: all REPL literals translated OK')
print('TRANSFORM COMPLETE')
