# -*- coding: utf-8 -*-
"""W45 EN core -> EN x KO fan-out transform. Single source of truth.

Re-copies the W45 EN core build, applies the value map below
(quoted-literal replacement, longest first) plus line-based code edits,
then asserts: every old value gone, OUT repointed, no Han characters
left in content*/bslib, no full-width CJK punctuation left, no forbidden
word. Furniture follows the shipped W43 EN x KO edition
(files/weekly-report-en-ko), NOT the README #20 generalisation:
badge replaces the 372 tagline slot in place at 19.5pt BRICK; footer
'The Lucerna · 영어 주간지 VOL.2 · 텍스트는 영어 · 해설은 한국어';
page line '제 {n} 면 / 총 {total} 면'; gloss prefix '해설 — ';
P8 separator '— 제 {pg} 면 —'; P8 notes half-width paren form with an
explicit PRINT_NOTES set measured from the core with tools/p8.py
extract (78 items); section heads 'ENGLISH HEAD · Korean short name';
P7 page labels stay English '(page N)' verbatim; gloss() call strings
drop their prefix (gloss() itself adds '해설 — ').

P7 word-box / phrase rule: English definition sentences and phrase
originals are verbatim; only gloss/explanation is localised to Korean.
Readers' Corner: the core's existing English letter paragraph is kept
verbatim (it is already honestly labelled in English); the disclosure
paragraph itself is Korean stating the 3 facts (no real letters, no
best VOL.1 P8 composition, example + promise deferred to VOL.3) plus an
explicit Korean imperative invitation with a VOL.3 promise. No new
English disclosure sentence is invented (the core has none).
"""
import os
import re
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE_BUILD = os.path.join(BASE, "hidden_files/weekly-report-w45-en-build")
EDITION_DIR = os.path.join(BASE, "files/weekly-report-w45-en-ko")
FILES = ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py", "bslib4.py"]

MAP = {
    # --- furniture / masthead ---
    "WEEKLY IN ENGLISH · 每周一期 · 读美国人正在读的英语": "WEEKLY IN ENGLISH · 매주 발행 · 미국이 읽는 영어",
    "英 语 周 报 · VOL.2 · 选 票 · 足 球 · 电 影": "영어 주간지 · VOL.2 · 투표 · 축구 · 영화",
    "周二选举日 · 周日已拨回时钟": "화요일 선거일 · 일요일 시계 되돌림",
    "11 月 3 日周二选举日 · 详见第 6 版": "11월 3일 화요일 선거일 · 6면 참조",
    "The Lucerna · 英语周报 VOL.2 · LUCERNA ENGLISH WEEKLY": "The Lucerna · 영어 주간지 VOL.2 · 텍스트는 영어 · 해설은 한국어",
    "译注｜": "해설 — ",
    # --- P1 ---
    "THE BIG STORY · 头条": "THE BIG STORY · 헤드라인",
    "讲解｜a midterm 中期选举 · a ballot 选票 · a race 一场竞选 · to call a race 宣布某场竞选的结果。": "해설 — a midterm 중간선거 · a ballot 투표용지 · a race 선거전 · to call a race 선거전 결과를 발표하다.",
    "THE WEEK IN NUMBERS · 数字看本周": "THE WEEK IN NUMBERS · 숫자",
    "TRY IT NOW · 即学即练": "TRY IT NOW · 바로 연습",
    "ballot = 纸选票": "ballot = 투표용지",
    "midterm = 中期（选举）": "midterm = 중간(선거)",
    "选举日 11 月 3 日（周二）": "선거일 11월 3일(화요일)",
    "early voting = 提前投票": "early voting = 사전투표",
    "race called = 宣布结果": "race called = 결과 발표",
    "take time = 花时间": "take time = 시간이 걸리다",
    "本周美国热搜 · Google Trends 美国区快照": "이번 주 미국 인기 검색 · Google Trends 스냅샷",
    "相对热度示意，非精确搜索量。": "상대적 인기 표시예요, 정확한 수치 아니에요.",
    "IN THIS ISSUE · 本期目录": "IN THIS ISSUE · 이번 호 목차",
    "（任期）中期。midterm election 中期选举。": "(임기) 중간. midterm election 중간선거.",
    "IN BRIEF · 快讯": "IN BRIEF · 단신",
    "LIGHTNING QUIZ · 闪电问答": "LIGHTNING QUIZ · 번개 퀴즈",
    "读头版，选出正确答案 · 答案见第 8 版": "1면을 읽고 정답을 고르세요 · 정답은 8면에",
    "选举日 11 月 3 日周二": "선거일 11월 3일 화요일",
    "众议院 435 席全部改选": "하원 435석 전원 교체",
    "美国 11 月 1 日拨回时钟": "미국 11월 1일 시계 되돌림",
    "NFL 马德里赛 11 月 8 日周日": "NFL 마드리드 경기 11월 8일 일요일",
    "Nov 3 — Election Day（选举日） · 435 — seats in the House, all on the ballot（众议院全部席位改选）": "Nov 3 — Election Day(선거일) · 435 — seats in the House, all on the ballot(하원 전 의석 교체)",
    "Nov 6 — two films open（两部电影上映） · Nov 8 — NFL in Madrid + F1 in São Paulo（周日两场大赛）": "Nov 6 — two films open(영화 두 편 개봉) · Nov 8 — NFL in Madrid + F1 in São Paulo(일요일 두 큰 경기)",
    # --- P2 ---
    "LIFE · 生活": "LIFE · 생활",
    "LEVEL A2 · Clocks, candy & your week · 时钟、糖果与你的一周": "LEVEL A2 · Clocks, candy & your week · 시계, 사탕과 여러분의 한 주",
    "DO THE MATHS · 算一算": "DO THE MATHS · 계산해 보기",
    "讲解｜to fall back （时钟）拨回 · a costume 服装、装扮 · trick or treat 不给糖就捣蛋。": "to fall back (시계) 되돌리다 · a costume 의상 · trick or treat 과자 안 주면 장난칠 거야.",
    "AND YOU ? · 说说你自己": "AND YOU ? · 여러분은요?",
    "周日你多睡了一小时吗？写两句英语寄给编辑部。": "일요일에 한 시간 더 잤나요? 편집부로 영어 두 문장을 보내 주세요.",
    "TELLING THE TIME · 这样报时间": "TELLING THE TIME · 시간 말하기",
    "The repeated hour · 本周的三个时间": "The repeated hour · 이번 주의 세 시각",
    "EXERCISES · 第 2 版练习": "EXERCISES · 2면 연습",
    "答案见第 8 版 · 题目可跨级混排，按题号找答案": "정답은 8면에 · 문제는 단계를 넘나들어요, 번호로 정답을 찾으세요",
    "根据时间，用英语补全句子。": "시각을 보고 영어 문장을 완성하세요.",
    "1:00 = 一点整": "1:00 = 한 시 정각",
    "1:30 = 一点半": "1:30 = 한 시 반",
    "7:45 = 差一刻八点": "7:45 = 여덟 시 15분 전",
    "两次 = twice": "두 번 = twice",
    "多出的 = extra": "남는 = extra",
    "用 be going to + 动词改写（计划与将要发生的事）。": "be going to + 동사로 바꿔 쓰세요(계획을 말할 때).",
    "Americans 复数 → are going to": "Americans 복수 → are going to",
    "疑问句：be 提前": "의문문: be 앞으로",
    "读第 2 版文章，选出正确答案。": "2면 기사를 읽고 정답을 고르세요.",
    "11 月 1 日凌晨 2 点拨回 1 点": "11월 1일 새벽 2시에 1시로 되돌림",
    "亚利桑那与夏威夷不拨钟": "애리조나와 하와이는 시계를 안 돌려요",
    "万圣节 10 月 31 日周六": "핼러윈 10월 31일 토요일",
    "11 月 1 日夜晚有 25 小时": "11월 1일 밤은 25시간",
    "= two times（两次）": "= two times(두 번)",
    "= one more time（再一次）": "= one more time(한 번 더)",
    "= to go back one hour（拨回）": "= to go back one hour(한 시간 되돌리기)",
    "= one hour more（多出一小时）": "= one hour more(한 시간 더)",
    "costume=装扮 b": "costume=의상 b",
    "extra hour=多出一小时 a": "extra hour=한 시간 더 a",
    "fall back=拨回 d": "fall back=되돌리다 d",
    "trick or treat=不给糖就捣蛋 c": "trick or treat=과자 안 주면 장난칠 거야 c",
    # --- shared type / instr labels ---
    "完成句子": "문장 완성",
    "单选": "객관식",
    "词汇配对": "단어 짝짓기",
    "句型转换": "문장 바꾸기",
    "填空": "빈칸 채우기",
    "改写": "바꿔 쓰기",
    "把词和释义配对": "단어와 뜻 짝짓기",
    "改错": "오류 고치기",
    "图表读数": "도표 읽기",
    "阅读理解": "읽기 이해",
    "跟练": "따라 연습",
    "翻译": "번역",
    "写作": "쓰기",
    "配对": "짝짓기",
    "完形填空": "빈칸 채우기",
    "用所给词补全句子。": "주어진 단어로 문장을 완성하세요.",
    # --- P3 ---
    "CULTURE · 文化": "CULTURE · 문화",
    "A2 → B1 · Friday at the movies · 周五看电影": "A2 → B1 · Friday at the movies · 금요일 영화",
    "AT HOME THIS WEEK · 在家看什么": "AT HOME THIS WEEK · 집에서 볼 것",
    "讲解｜to open （电影）上映 · a monster 怪物 · a catchphrase 口头禅、金句 · a series 剧集。": "to open (영화) 개봉하다 · a monster 괴물 · a catchphrase 유행어, 명대사 · a series 시리즈.",
    "读第 3 版文章，选出正确答案。": "3면 기사를 읽고 정답을 고르세요.",
    "猫咪电影 11 月 6 日周五上映": "고양이 영화 11월 6일 금요일 개봉",
    "猫出自苏斯博士的书": "고양이는 닥터 수스 책에서 왔어요",
    "比尔·黑德为猫配音": "헤이더가 목소리를 맡아요",
    "哥斯拉导演是山崎贵": "고질라 감독은 야마자키 다카시예요",
    "《黑鸽》第二季 11 月 5 日上线": "블랙 다브 시즌 2 11월 5일 공개",
    "周日重聚节目收尾": "일요일 재결합 프로그램으로 마무리",
    "open = 上映（第三人称单数加 s）": "open = 개봉하다(3인칭 단수는 s 추가)",
    "tall → taller 比较级": "tall → taller 비교급",
    "split = 分歧的": "split = 의견이 갈린",
    "用 be going to 改写。": "be going to로 바꿔 쓰세요.",
    "monster=怪物 b": "monster=괴물 b",
    "catchphrase=金句 a": "catchphrase=명대사 a",
    "series=剧集 d": "series=시리즈 d",
    "open=上映 c": "open=개봉하다 c",
    "THE CAT'S HAT · 猫的帽子": "THE CAT'S HAT · 고양이 모자",
    "五句影评｜who、where、发生了什么、转折、结局——五句就够。": "다섯 문장 평｜who, where, 무슨 일, 반전, 결말 — 다섯 문장이면 돼요.",
    # --- P4 ---
    "SPORT · 体育": "SPORT · 스포츠",
    "WHY MADRID ? · 为什么去马德里？": "WHY MADRID ? · 왜 마드리드일까?",
    "讲解｜a fixture 一场比赛（赛程） · a title 冠军头衔 · to defend （卫冕）保卫头衔 · a fan 球迷。": "a fixture 경기(일정 속 한 경기) · a title 우승 타이틀 · to defend 타이틀 지키기 · a fan 팬.",
    "读第 4 版文章，选出正确答案。": "4면 기사를 읽고 정답을 고르세요.",
    "马德里赛：孟加拉虎对猎鹰": "마드리드 경기: 벵골스 대 팰컨스",
    "马德里赛场是伯纳乌": "마드리드 경기장은 베르나베우예요",
    "海豚对雄狮在迈阿密": "돌핀스 대 라이언스, 마이애미에서",
    "F1 圣保罗大奖赛在巴西": "F1 상파울루 그랑프리는 브라질에서",
    "WTA 年终总决赛在印第安维尔斯开赛": "WTA 파이널스, 인디언웰스에서 개막",
    "拳击赛在阿灵顿": "복싱 경기는 알링턴에서",
    "defend 三单加 s": "defend 3인칭 단수 + s",
    "与第 4 版原文一致，复数动词": "4면 원문과 같아요, 복수 동사",
    "fixture=赛程中的比赛 b": "fixture=일정 속 경기 b",
    "title=冠军头衔 d": "title=우승 타이틀 d",
    "fan=球迷 a": "fan=팬 a",
    "defend=卫冕 c": "defend=타이틀 지키기 c",
    "用一般过去时改写（比赛已结束的说法）。": "일반 과거형으로 바꿔 쓰세요(끝난 경기 말하기).",
    "SUNDAY, NOVEMBER 8 · 周日赛程": "SUNDAY, NOVEMBER 8 · 일요일",
    "看球英语｜比分、谁得分、谁领先——短句就是直播英语。": "경기 영어｜점수, 누가 득점했는지, 누가 앞서는지 — 짧은 문장이 생중계 영어예요.",
    # --- P5 ---
    "YOUTH · 青年": "YOUTH · 청년",
    "LEVEL B1 · Election night at home · 选举之夜": "LEVEL B1 · Election night at home · 선거의 밤",
    "TOO CLOSE TO CALL · 难分胜负": "TOO CLOSE TO CALL · 접전",
    "讲解｜a map （选举）地图 · too close to call 难分胜负、无法判定 · a second screen 第二块屏幕（手机）。": "a map (선거) 지도 · too close to call 승부를 알 수 없음, 판단 불가 · a second screen 두 번째 화면(휴대전화).",
    "读第 5 版文章，选出正确答案。": "5면 기사를 읽고 정답을 고르세요.",
    "地图随结果逐州变色": "지도는 결과에 따라 주마다 색이 바뀌어요",
    "too close to call = 尚不知晓": "too close to call = 아직 몰라요",
    "选举夜常吃披萨": "선거의 밤에는 흔히 피자를 먹어요",
    "第二屏是手机": "두 번째 화면 = 폰",
    "孩子问为什么这么久": "아이들은 왜 이렇게 오래 걸리는지 물어요",
    "结果早上还在": "결과는 아침에도 그대로 있어요",
    "close = 接近的": "close = 가까운",
    "still = 仍然": "still = 여전히",
    "与第 5 版原文一致，单数": "5면 원문과 같아요, 단수",
    "map=选举地图 c": "map=선거 지도 c",
    "race=一场竞选 d": "race=선거전 d",
    "result=结果 b": "result=결과 b",
    "call=宣布胜者 a": "call=승자 발표 a",
    "用现在进行时改写（正在发生的事）。": "현재진행형으로 바꿔 쓰세요(지금 일어나는 일).",
    "FIVE SENTENCES · 五句话作业": "FIVE SENTENCES · 다섯 문장 과제",
    "投票结束｜The polls have closed = 该州投票已结束，计票开始。": "투표 종료｜The polls have closed = 그 주 투표가 끝나고 개표가 시작돼요.",
    # --- P6 ---
    "DEEP READ · 时事深读": "DEEP READ · 시사 심층",
    "LEVEL B2 · How America votes · 美国怎么投票": "LEVEL B2 · How America votes · 미국은 어떻게 투표할까",
    "A PRACTICE BALLOT · 模拟选票": "A PRACTICE BALLOT · 연습용 투표",
    "讲解｜to register 登记（选民登记） · a governor 州长 · to shape laws 影响立法 · patience 耐心。": "to register 등록하다(유권자 등록) · a governor 주지사 · to shape laws 법률에 영향을 주다 · patience 인내심.",
    "READ THE CHART · 读图表": "READ THE CHART · 도표 읽기",
    "读上面的教学图表，选出正确答案。": "위의 연습용 도표를 읽고 정답을 고르세요.",
    "38% 选“不用排队”": "38% '줄 서지 않아도 돼요' 선택",
    "工作原因 29%": "일 때문 29%",
    "四项合计 100%": "네 항목 합계 100%",
    "习惯最少 12%": "습관이 가장 적어요 12%",
    "不用排队比旅行多 17 个百分点": "줄 서지 않아도 돼요가 여행보다 17%포인트 많아요",
    "图表是教学数据非真实民调": "도표는 연습용 자료예요, 실제 조사가 아니에요",
    "读第 6 版文章，选出正确答案。": "6면 기사를 읽고 정답을 고르세요.",
    "各州自行组织选举": "각 주가 스스로 선거를 주관해요",
    "众议员任期两年": "하원 의원 임기는 2년이에요",
    "参议员任期六年、每次约三分之一改选": "상원 의원 임기는 6년, 매번 약 3분의 1씩 교체돼요",
    "邮寄选票计票需时间": "우편 투표 개표에는 시간이 걸려요",
    "本期不印民调与预测": "이번 호에는 여론조사와 예측을 싣지 않아요",
    "耐心是制度的一部分": "인내는 제도의 일부",
    "shape = 影响、塑造": "shape = 영향을 주다, 만들다",
    "register = 登记": "register = 등록하다",
    "patience = 耐心": "patience = 인내심",
    "optional = 可选的": "optional = 선택 사항인",
    "differ 三单 differs": "differ 3인칭 단수 differs",
    "private = 私密的": "private = 비공개로",
    "HOW LONG ? · 任期多长？": "HOW LONG ? · 임기는 얼마나?",
    "一张地图｜五十个州、五十套规则——所以选举夜看的是地图，不是一个数字。": "한 장의 지도｜쉰 개 주, 쉰 가지 규칙 — 그래서 선거의 밤에 보는 건 지도가 되지, 숫자가 아니에요.",
# --- P7 ---
"LANGUAGE IN HAND · 精讲": "LANGUAGE IN HAND · 정밀 해설",
"A2 → B2 · Phrases of the week · 本周金句": "A2 → B2 · Phrases of the week · 이번 주의 명문장",
"LEVEL A2 · 基础": "LEVEL A2 · 기초",
"THE EXAMPLE · 例句": "THE EXAMPLE · 예문",
"LEVEL B1 · 进阶": "LEVEL B1 · 중급",
"LEVEL B2 · 挑战": "LEVEL B2 · 도전",
"THE TOOLBOX · 工具箱": "THE TOOLBOX · 도구 상자",
"工具箱｜本期三句随身句，按级各一；金句全部出自本期文章，回读原文最有效。": "도구 상자 — 이번 호 휴대 문장 세 개, 단계마다 하나; 명문장은 전부 이번 호 기사에서 왔어요. 원문을 다시 읽는 게 가장 효과적이에요.",
"PHRASES OF THE WEEK · 本周金句（全部出自本期文章）": "PHRASES OF THE WEEK · 이번 주의 명문장(전부 이번 호 기사에서)",
"每句一个语法点 + 一道小题 · 答案见第 8 版": "문장마다 문법 포인트 하나 + 작은 문제 하나 · 정답은 8면에",
"THE ERROR CLINIC · 易错诊所": "THE ERROR CLINIC · 오류 클리닉",
"每句有一处错误：找出来并改正。": "문장마다 오류가 하나씩 있어요: 찾아서 고치세요.",
"三单否定用 doesn't + 原形": "3인칭 단수 부정에는 doesn't + 동사원형",
"fall 的过去式是 fell": "fall의 과거형은 fell예요",
"bigger 已含比较级，不要再加 more": "bigger에는 이미 비교급이 들어 있어요, more를 더하지 마세요",
"going to 后用动词原形": "going to 뒤에는 동사원형",
"READERS' CORNER · 读者园地": "READERS' CORNER · 독자 코너",
"编辑说明｜VOL.1 曾承诺 VOL.2 刊登真实来信，但截至发稿编辑部未收到真实来信与 VOL.1 写作投稿，故本期如实说明、不虚构来信；请把你的来信与写作寄来，VOL.3 起刊登收到的真实来信。": "편집부 알림｜VOL.1에서는 VOL.2에 실제 편지를 싣겠다고 약속했지만, 발행 때까지 실제 편지도 VOL.1 쓰기 투고도 도착하지 않았어요. 편지를 지어내지 않고 예시를 싣습니다. 여러분의 편지와 쓰기를 보내 주세요. VOL.3부터 실제 편지를 싣겠습니다.",
"NEXT WEEK · VOL.3 下周预告": "NEXT WEEK · VOL.3 다음 호 예고",
"下周三退伍军人节，周日 NFL 慕尼黑赛；还有中期选举结果报道。": "다음 주 수요일 재향군인의 날, 일요일 NFL 뮌헨 경기, 그리고 중간선거 결과 보도.",
"语法点｜is = 是；日期作主语补足语。": "문법 포인트 — is = 이다; 날짜가 주어 보어로 쓰여요.",
"is 是": "is = 이다",
"语法点｜happen 的过去式是 happened，规则变化。": "문법 포인트 — happen의 과거형은 happened, 규칙 변화예요.",
"语法点｜would + 动词原形，表选择意愿。": "문법 포인트 — would + 동사원형, 선택 의지예요.",
"would + 原形": "would + 원형",
"语法点｜that is = 那就是；破折号后总结。": "문법 포인트 — that is = 그게 바로; 대시 뒤에 요약해요.",
"that is 那就是": "that is = 그게 바로",
"语法点｜will still = 仍然会；still 放在 will 之后。": "문법 포인트 — will still = 여전히 ~할 것이다; still은 will 뒤에 와요.",
"will still 仍然会": "will still = 여전히 ~할 것이다",
"语法点｜part of = ……的一部分；not 表否定对照。": "문법 포인트 — part of = ~의 일부분; not은 부정 대조를 나타내요.",
"is part of 一部分": "is part of = 일부분",
"语法点｜not every + 单数动词：并非每处都变。": "문법 포인트 — not every + 단수 동사: 모든 곳이 바뀌는 건 아니에요.",
"语法点｜has = 有；the week 单数用 has。": "문법 포인트 — has = 가지다; the week은 단수라서 has를 써요.",
"« Patience is part of the system, not a failure of it. » — part of = 一部分 (page 6).": "« Patience is part of the system, not a failure of it. » — part of = 일부분 (page 6).",
# --- P8 ---
"EXERCISES & ANSWERS · 练习与答案": "EXERCISES & ANSWERS · 연습과 정답",
"FINAL TEST · 综合评估 · Answers at the bottom of this page 答案在本版下方": "FINAL TEST · 종합 평가 · Answers at the bottom of this page · 정답은 이 면 아래쪽에",
"A · CLOZE · 完形填空": "A · CLOZE · 빈칸 채우기",
"选项：": "선택지:",
"B · MULTIPLE CHOICE · 单选": "B · MULTIPLE CHOICE · 객관식",
"C · READING · 阅读理解": "C · READING · 읽기 이해",
"D · SENTENCES · 完成句子与转换": "D · SENTENCES · 문장 완성과 바꾸기",
"E · TRANSLATION · 翻译": "E · TRANSLATION · 번역",
"F · WORDS · 词汇配对": "F · WORDS · 단어 짝짓기",
"G · DIALOGUE · 对话补全": "G · DIALOGUE · 대화 완성",
"对话补全": "대화 완성",
"still 仍然": "still 여전히",
"H · WRITING · 写作 [B1]": "H · WRITING · 쓰기 [B1]",
"MODEL · 范文": "MODEL · 모범 답안",
"ANSWERS · 全部答案与简析（第 1–8 版）": "ANSWERS · 모든 정답과 간단한 설명(1–8면)",
"11 月 3 日是周二": "11월 3일은 화요일이에요",
"pizza 披萨": "pizza 피자",
"map 地图逐州变色": "map 지도 주마다 색 변화",
"close 接近的": "close 가까운",
"sticker 贴纸": "sticker 스티커",
"will + 动词原形 know": "will + 동사원형 know",
"we → get 原形": "we → get 원형",
"已发生的事用 fell": "이미 일어난 일에는 fell",
"than → 比较级 bigger": "than → 비교급 bigger",
"despite + 名词：尽管下雨": "despite + 명사: 비에도 불구하고",
"whether = 是否": "whether = ~인지",
"将来时 will + 动词原形": "미래형 will + 동사원형",
"be going to + 原形 vote": "be going to + 원형 vote",
"too close to call = 难分胜负": "too close to call = 승부를 알 수 없음",
"原文：a teacher from Ohio": "원문: a teacher from Ohio",
"周二他全天教书": "화요일에는 하루 종일 가르쳐요",
"贴纸上写着 I VOTED": "스티커에는 I VOTED라고 쓰여 있어요",
"俄亥俄一如既往难分胜负": "오하이오는 언제나처럼 승부를 알 수 없어요",
"are going to + 原形": "are going to + 원형",
"fall → fell（不规则变化）": "fall → fell(불규칙 변화)",
"tall → taller（比较级）": "tall → taller(비교급)",
"whether 引导“是否”从句": "whether는 '~인지' 절을 이끌어요",
"耐心是制度的一部分，而不是制度的失败。": "인내는 제도의 일부예요, 실패가 아니에요.",
"part of 一部分；not a failure 不是失败": "part of = 일부분; not a failure = 실패가 아님",
"11 月 3 日周二是美国的选举日。": "11월 3일 화요일은 미국의 선거일이에요.",
"Election Day 选举日；on Tuesday": "Election Day = 선거일; on Tuesday = 화요일에",
"翻译：Tuesday, November 3, is Election Day in the United States.": "번역: Tuesday, November 3, is Election Day in the United States.",
"这周日，NFL 在马德里比赛。": "일요일에 NFL이 마드리드에서 경기를 해요.",
"on Sunday；in Madrid": "on Sunday = 일요일에; in Madrid = 마드리드에서",
"翻译：On Sunday, the NFL plays in Madrid.": "번역: On Sunday, the NFL plays in Madrid.",
"并非每处都拨回时钟。": "모든 곳이 시계를 되돌리는 건 아니에요.",
"not every 并非每处；change 变化": "not every = 모든 ~가 아니다; change = 바뀌다",
"midterm = 中期选举 b": "midterm = 중간선거 b",
"governor = 州长 c": "governor = 주지사 c",
"ballot = 选票 d": "ballot = 투표용지 d",
"turnout = 投票率 a": "turnout = 투표율 a",
"投票时出示证件 ID": "투표할 때 신분증 ID 제시",
"line = 排队（美式英语）": "line = 줄 서기(미국식 영어)",
"ballot = 选票": "ballot = 투표용지",
"sticker = 贴纸": "sticker = 스티커",
"选举日是 11 月 3 日周二": "선거일 = 11월 3일 화요일",
"开放题 — 要点见写作框，范文在第 8 版写作框内": "열린 문제 — 기준은 쓰기 칸에, 모범 답안은 8면 쓰기 칸 안에",
"按要点给分": "기준 항목대로 채점해요",
"用英语写 80–100 词：我的 11 月 3 日周二。写清你是否看了结果、吃了什么、地图显示了什么，再写一句周日夜里拨回的时钟。": "영어로 80–100단어 쓰기: 나의 11월 3일 화요일. 결과를 봤는지, 무엇을 먹었는지, 지도가 무엇을 보여줬는지, 그리고 일요일 밤에 되돌린 시계에 대해 한 문장을 쓰세요.",
}

# Core printed-note set, measured with tools/p8.py extract on the core P8
# (78 items). Korean notes are longer, so the core printed set is applied
# EXPLICITLY by exercise number (EN-family precedent).
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


HAN = re.compile(r"[\u4e00-\u9fff]")
FULLWIDTH_PUNCT = set("。，；：、（）《》「」『』？！")


def main():
    # 1. re-copy core build + assets + svglib (byte-identical to W43 EN x KO svglib)
    for fn in FILES:
        shutil.copy2(os.path.join(CORE_BUILD, fn), os.path.join(HERE, fn))
    import hashlib
    data = open(os.path.join(CORE_BUILD, "svglib.py"), "rb").read()
    assert hashlib.md5(data).hexdigest() == "0703a8814abe388f131c89f3d7ffb946", "core svglib md5 mismatch"
    open(os.path.join(HERE, "svglib.py"), "wb").write(data)
    if os.path.isdir(os.path.join(HERE, "assets")):
        shutil.rmtree(os.path.join(HERE, "assets"))
    shutil.copytree(os.path.join(CORE_BUILD, "assets"), os.path.join(HERE, "assets"))
    # 2. value map, longest first, quoted-literal replacement
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
    # 3. line-based code edits
    for fn in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        p = os.path.join(HERE, fn)
        t = open(p, encoding="utf-8").read()
        assert "weekly-report-w45-en-core/svg" in t, fn
        t = t.replace("weekly-report-w45-en-core/svg", "weekly-report-w45-en-ko/svg")
        open(p, "w", encoding="utf-8").write(t)
    p12 = os.path.join(HERE, "content12.py")
    t = open(p12, encoding="utf-8").read()
    t = replace_line(t, "THE LEARNERS' WEEKLY",
                     'p.text(975, 372, "영어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판", 19.5, "sans", True, BRICK, anchor="middle")')
    open(p12, "w", encoding="utf-8").write(t)
    p8 = os.path.join(HERE, "content8.py")
    t = open(p8, encoding="utf-8").read()
    t = replace_line(t, "— 第 {pg}",
                     '    kf.para(f"— 제 {pg} 면 —", 17, "sans", True, OLIVE, 1.28, 3)')
    t = replace_line(t, 'if e["note"] and (pg == 8',
                     '        if e["note"] and e["n"] in PRINT_NOTES:')
    t = replace_line(t, 's += f"（',
                     '            s += f" ({e[\'note\']})"')
    notes_block = ("# Printed-note parity with the core (tools/p8.py extract on the\n"
                   "# core P8): the core prints a note when the item is on page 8,\n"
                   "# or its (Chinese) note is <= 10 chars, or its type is\n"
                   "# correction/chart-reading. Korean notes are longer, so the\n"
                   "# core printed set is applied EXPLICITLY by exercise number.\n"
                   "PRINT_NOTES = " + repr(sorted(PRINT_NOTES)) + "\n")
    assert "from itertools import groupby" in t
    t = t.replace("from itertools import groupby", notes_block + "from itertools import groupby", 1)
    open(p8, "w", encoding="utf-8").write(t)
    bsl = os.path.join(HERE, "bslib4.py")
    t = open(bsl, encoding="utf-8").read()
    t = replace_line(t, 'f"第 {n}',
                     '        self.text(RIGHT, 2624, f"제 {n} 면 / 총 {total} 면", 20, "sans", False, GREY, anchor="end")')
    open(bsl, "w", encoding="utf-8").write(t)
    # 4. audits: no old value left (quoted), no core OUT left, no Han chars,
    #    no full-width CJK punctuation, no forbidden word in operative code
    for fn in FILES:
        text = open(os.path.join(HERE, fn), encoding="utf-8").read()
        assert "weekly-report-w45-en-core" not in text, fn
        for old in MAP:
            if old != MAP[old]:
                assert ('"%s"' % old) not in text, f"{fn}: leftover {old!r}"
        assert "桥接" not in text, fn
        hans = HAN.findall(text)
        assert not hans, f"{fn}: Han chars left: {hans[:10]}"
        bad = sorted(set(text) & FULLWIDTH_PUNCT)
        assert not bad, f"{fn}: full-width punct left: {bad}"
    print("transform OK: all old values consumed, OUT repointed, no Han/full-width punct")


if __name__ == "__main__":
    main()
