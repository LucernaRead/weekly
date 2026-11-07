# -*- coding: utf-8 -*-
"""KO core (Chinese explanations) -> KO x EN fan-out transform, W45 VOL.2.

Method (tools README #17): whole-line / exact unique literal replacements
only, each asserted present before replacement; counts logged. No AST byte
offsets, no repr literals. Korean target text is never touched; only the
explanation layer (Chinese glosses, notes, furniture second halves, P8
notes) is rewritten in English. P8 E-zone is re-aimed KO<->EN (items
137/138 keys become English; 139/140 stems become English, keys stay
Korean). The P7 readers'-corner disclosure is rebuilt in English (see
LETTERS note below). P1 masthead geometry follows the W43 KO x EN
measured instance (subtitle 372->366, badge inserted y=394 17pt bold
olive, rules +20, dark band +9), NOT the README #20 20pt majority form.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# (old, new) per file; every old string must occur >= 1 time.
REPS = {
    "bslib4.py": [
        ("Lucerna · 韩语周报 VOL.2 · LUCERNA KOREAN WEEKLY",
         "Lucerna · KOREAN WEEKLY VOL.2 · Korean text · English explanations"),
        ('f"제 {n} 면 / 총 {total} 면"', 'f"Page {n} of {total}"'),
        ("译注｜", "Note — "),
    ],
    "content12.py": [
        ("매주 한국어로 · 每周一期 · 한국 사람이 읽는 한국어를 읽어요",
         "매주 한국어로 · A new issue every week · 한국 사람이 읽는 한국어를 읽어요"),
        ("톱 뉴스 · 头条", "톱 뉴스 · Top story"),
        ("입동 立冬、冬季开始 · 절정 最盛期、高峰 · 김장 腌过冬泡菜 · 상륙하다 登陆 · 온대저기압 温带气旋。",
         "입동 = ipdong, the start of winter · 절정 = peak, the height · 김장 = making kimchi for winter · 상륙하다 = to make landfall · 온대저기압 = extratropical cyclone"),
        ("숫자로 보는 이번 주 · 数字看本周", "숫자로 보는 이번 주 · This week in numbers"),
        ("지금 바로 연습 · 即学即练", "지금 바로 연습 · Practice now"),
        ("立冬在11月7日周六", "Ipdong falls on Saturday, Nov 7"),
        ("泡菜季＝腌过冬泡菜", "Kimjang = making kimchi for winter"),
        ("高考在11月19日周四", "The CSAT is on Thursday, Nov 19"),
        ("11月2日是D-17", "Nov 2 is D-17"),
        ("台风没有在韩国本土登陆", "The typhoon did not make landfall on the Korean mainland"),
        ("首尔报名窗口11月6日10–12点", "The Seoul sign-up window is Nov 6, 10-12"),
        ("这五个日期，是本期报纸的骨架。", "These five dates are the backbone of this issue."),
        ("이번 호의 내용 · 本期目录", "이번 호의 내용 · In this issue"),
        ("全部", "All"),
        ("이번 주의 말 · 本周词语", "이번 주의 말 · Word of the week"),
        ("입동 ＝ 立冬、冬季开始的节气。", "입동 = ipdong, the solar term that starts winter."),
        ("짧은 소식 · 快讯", "짧은 소식 · News in brief"),
        ("퀴즈 · 闪电问答", "퀴즈 · Lightning quiz"),
        ("读头版，选出正确答案 · 答案见第 8 版", "Read page 1, pick the right answer · Answers on page 8"),
        ("立冬＝冬季开始的节气", "Ipdong = the solar term that starts winter"),
        ("内藏山两个预报：11月4日与11月11日", "Naejangsan's two forecasts: Nov 4 and Nov 11"),
        ("10月25日首场比赛因雨推迟", "The Oct 25 first playoff game was rained off"),
        ("생활 · 生活", "생활 · Life"),
        ("泡菜季与过冬准备、韩史考试报名", "Kimjang and winter prep, Korean History exam sign-up"),
        ("절이다 用盐腌 · 버무리다 拌 · 난방 供暖 · 식탁 餐桌。",
         "절이다 = to salt-pickle · 버무리다 = to mix and season · 난방 = heating · 식탁 = dining table"),
        ("산불 山火 · 벌금 罚款 · 불씨 火星。",
         "산불 = wildfire · 벌금 = fine · 불씨 = spark"),
        ("한능검 접수 · 韩史考试报名", "한능검 접수 · Korean History exam sign-up"),
        ("아삭하다 脆脆的 · 김 蒸汽 · 깊어지다 变深。",
         "아삭하다 = crisp · 김 = steam · 깊어지다 = to deepen"),
        ("물려주다 传给 · 낡다 旧 · 두렵다 害怕。",
         "물려주다 = to hand down · 낡다 = worn out · 두렵다 = to fear"),
        ("겨울 준비 목록 · 过冬清单", "겨울 준비 목록 · Winter prep checklist"),
        ("묵직하다 沉甸甸的 · 앞치마 围裙 · 목록 清单。",
         "묵직하다 = heavy and solid · 앞치마 = apron · 목록 = list"),
        ("당신은? · 说说你自己", "당신은? · And you?"),
        ("你呢？为过冬做的第一件事是什么？写两句韩语寄来。",
         "And you? What is the first thing you do to get ready for winter? Write two sentences in Korean and send them in."),
        ("날짜 세는 말 · 数日子的说法", "날짜 세는 말 · Counting days"),
        ("用高考倒计时数日子的四个说法", "Four ways to count the days left until the CSAT"),
        ("11 月 2 日，还剩 17 天", "Nov 2, 17 days left"),
        ("11 月 7 日，还剩 12 天", "Nov 7, 12 days left"),
        ("11 月 18 日，就是明天", "Nov 18, tomorrow"),
        ("11 月 19 日，就是今天", "Nov 19, today itself"),
        ("연습 · 第 2 版练习", "연습 · Page 2 exercises"),
        ("答案见第 8 版 · 题目可跨级混排，按题号找答案",
         "Answers on page 8 · Items may mix levels; find them by number"),
        ("山火注意期从11月1日开始", "The wildfire caution period starts Nov 1"),
        ("带火进山最高罚30万韩元", "Taking fire into the mountains: fine up to 300,000 won"),
        ("韩史考试在11月28日周六", "The Korean History exam is Saturday, Nov 28"),
        ("首尔报名10点至12点", "Seoul sign-up, 10 to 12"),
        ("白菜用盐腌", "Cabbage is salt-pickled"),
        ("加入萝卜和调料拌匀", "Add radish and seasoning and mix"),
        ("过冬准备＝为冬天做准备", "Winter prep = getting ready for winter"),
        ("进山要小心火", "Be careful with fire in the mountains"),
        ("11月3日起开始报名", "Sign-up starts Nov 3"),
        ("山火注意期到12月15日", "The wildfire caution period ends Dec 15"),
        ("最高罚款30万韩元", "Maximum fine 300,000 won"),
        ("深化考试费27,000韩元", "Advanced-level fee 27,000 won"),
        ("11月6日13点起全国报名剩余名额", "From 13:00 on Nov 6, nationwide sign-up for remaining seats"),
        ("김장=腌过冬泡菜 a", "김장 = making kimchi for winter a"),
        ("월동 준비=准备过冬 c", "월동 준비 = getting ready for winter c"),
        ("산불조심=进山小心火 d", "산불조심 = being careful with fire in the mountains d"),
        ("한능검=韩国史考试简称 b", "한능검 = short for the Korean History exam b"),
        ("把词和说明配对", "Match the pairs"),
        ('instr="填空"', 'instr="Fill in"'),
        ("完成句子", "fill-in"),
        ("单选", "multiple choice"),
        ("词汇配对", "matching"),
    ],
    "content34.py": [
        ("문화 · 文化", "문화 · Culture"),
        ("红叶最后一周", "Last weekend of autumn foliage"),
        ("기관 机构 · 기준 标准 · 관측 观测 · 구간별 按路段。",
         "기관 = organisation · 기준 = criterion · 관측 = observation · 구간별 = by section of trail"),
        ("현장 现场 · 유명하다 有名 · 맛보다 品尝。",
         "현장 = on site · 유명하다 = to be famous · 맛보다 = to taste"),
        ("이용하다 利用 · 막히다 堵塞 · 예의 礼仪。",
         "이용하다 = to use · 막히다 = to be blocked · 예의 = manners"),
        ("겹쳐 입다 叠穿 · 미끄러지다 打滑 · 돌 石头。",
         "겹쳐 입다 = to layer clothes · 미끄러지다 = to slip · 돌 = stone"),
        ("단풍 구경 준비물 · 红叶观赏准备", "단풍 구경 준비물 · Leaf-viewing checklist"),
        ("你呢？想去看红叶的山是哪座？写两句韩语寄来。",
         "And you? Which mountain would you like to visit for the autumn leaves? Write two sentences in Korean and send them in."),
        ("연습 · 第 3 版练习", "연습 · Page 3 exercises"),
        ("答案见第 8 版 · 题目可跨级混排，按题号找答案",
         "Answers on page 8 · Items may mix levels; find them by number"),
        ("内藏山林业厅预报峰值11月4日", "Naejangsan Forestry Service forecast peak: Nov 4"),
        ("内藏山公园公团预报峰值11月11日", "Naejangsan parks agency forecast peak: Nov 11"),
        ("雪岳山实际观测峰值10月16日", "Seoraksan actual observed peak: Oct 16"),
        ("青松现场庆典11月4日至8日", "Cheongsong on-site festival, Nov 4-8"),
        ("没有官方的路段数值", "There are no official per-section figures"),
        ("红叶最美的时候叫절정", "The most beautiful autumn leaves are called 절정"),
        ("日期不同因为标准不同", "The dates differ because the criteria differ"),
        ("实际观测比预报早", "The actual observation was earlier than the forecasts"),
        ("现场庆典11月4日起", "The on-site festival starts Nov 4"),
        ("青松以苹果闻名", "Cheongsong is famous for apples"),
        ("内藏山林业厅预报4日", "Naejangsan Forestry Service forecast: the 4th"),
        ("内藏山公团预报11日", "Naejangsan parks agency forecast: the 11th"),
        ("月出山林业厅预报9日", "Wolchulsan Forestry Service forecast: the 9th"),
        ("雪岳山实际观测16日", "Seoraksan actual observation: the 16th"),
        ("내장산=两个预报之间 b", "내장산 = between the two forecasts b"),
        ("월출산=11月9日前夕 a", "월출산 = just before Nov 9 a"),
        ("북한산=11月4日之后、低路更晚 d", "북한산 = just after Nov 4; low trails later d"),
        ("설악산=实际观测10月16日 c", "설악산 = actual observation Oct 16 c"),
        ("把山和说明配对", "Match the mountain to its note"),
        ("스포츠 · 体育", "스포츠 · Sports"),
        ("秋季棒球消息", "Autumn baseball news"),
        ("연승 连胜 · 만루홈런 满垒本垒打 · 미뤄지다 推迟 · 마감하다 截稿。",
         "연승 = winning streak · 만루홈런 = grand slam · 미뤄지다 = to be postponed · 마감하다 = to close an issue"),
        ("흔들다 挥动 · 하나가 되다 融为一体。",
         "흔들다 = to wave · 하나가 되다 = to become one"),
        ("예상 预测。", "예상 = prediction"),
        ("한국시리즈까지의 길 · 通往韩国大赛之路", "한국시리즈까지의 길 · The road to the Korean Series"),
        ("연습 · 第 4 版练习", "연습 · Page 4 exercises"),
        ("半决赛胜队是KIA", "The semi-playoff winners are KIA"),
        ("第3场比分13比1", "Game 3 score: 13-1"),
        ("第3场在蚕室举行", "Game 3 was held in Jamsil"),
        ("季后赛首场因雨推迟", "The first playoff game was rained off"),
        ("公布的韩国大赛开始日11月2日", "The announced Korean Series start: Nov 2"),
        ("三连胜晋级", "Won three straight to advance"),
        ("首场比赛因雨推迟", "The first game was rained off"),
        ("10月26日变为温带气旋", "Became an extratropical cyclone on Oct 26"),
        ("kt在韩国大赛等候", "kt waits in the Korean Series"),
        ("이기다的过去式이겼어요", "Past form of 이기다: 이겼어요"),
        ("열리다的过去式열렸어요", "Past form of 열리다: 열렸어요"),
        ("미뤄지다的过去式미뤄졌어요", "Past form of 미뤄지다: 미뤄졌어요"),
        ("바뀌다的过去式바뀌었어요", "Past form of 바뀌다: 바뀌었어요"),
        ("준플레이오프=KIA三连胜 b", "준플레이오프 = KIA won three straight b"),
        ("플레이오프=KIA对三星 d", "플레이오프 = KIA vs Samsung d"),
        ("한국시리즈=kt在等候 a", "한국시리즈 = kt waits a"),
        ("온대저기압=台风10月26日变化 c", "온대저기압 = what the typhoon became on Oct 26 c"),
        ('instr="改写"', 'instr="Rewrite"'),
        ('instr="填空"', 'instr="Fill in"'),
        ("完成句子", "fill-in"),
        ("单选", "multiple choice"),
        ("词汇配对", "matching"),
        ("句型转换", "transformation"),
    ],
    "content56.py": [
        ("청년 · 青年", "청년 · Youth"),
        ("高考倒计时与万圣节", "CSAT countdown and Halloween"),
        ("정리 整理、复习 · 끈끈하다 粘粘的 · 합격 合格。",
         "정리 = tidying up, revision · 끈끈하다 = sticky · 합격 = passing"),
        ("중점 重点 · 배치하다 部署 · 통제하다 管制。",
         "중점 = focus · 배치하다 = to deploy · 통제하다 = to control"),
        ("이번 주 청년 숫자 · 本周青年数字", "이번 주 청년 숫자 · This week in youth numbers"),
        ("챙기다 准备好 · 졸리다 犯困 · 평소 平时。",
         "챙기다 = to pack, to prepare · 졸리다 = to feel sleepy · 평소 = usual"),
        ("비다 祈愿 · 피하다 避开 · 미끄럽다 滑。",
         "비다 = to wish, to pray · 피하다 = to avoid · 미끄럽다 = slippery"),
        ("你呢？想对考生说的一句加油是什么？写两句韩语寄来。",
         "And you? What cheer would you like to give the exam candidates? Write two sentences in Korean and send them in."),
        ("연습 · 第 5 版练习", "연습 · Page 5 exercises"),
        ("答案见第 8 版 · 题目可跨级混排，按题号找答案",
         "Answers on page 8 · Items may mix levels; find them by number"),
        ("11月7日是D-12", "Nov 7 is D-12"),
        ("高考在11月19日周四", "The CSAT is on Thursday, Nov 19"),
        ("听力时段飞机不起降", "No flights take off or land during listening"),
        ("首尔万圣节安全人员3,271人", "Seoul Halloween safety staff: 3,271"),
        ("梨泰院路10月31日管制", "Itaewon-ro closed on Oct 31"),
        ("全国为考生加油", "The whole country cheers the candidates"),
        ("倒计时仍在继续", "The countdown goes on"),
        ("怀着祈愿合格的心意赠送糯米糕、饴糖", "Given with a wish for success: glutinous rice cake and taffy"),
        ("首尔安全人员3,271人", "Seoul safety staff: 3,271"),
        ("今年考生551,864人", "This year's candidates: 551,864"),
        ("考场全国1,312处", "Test sites nationwide: 1,312"),
        ("考试日机关10点上班", "On exam day, offices start at 10"),
        ("梨泰院部署1,620人", "Itaewon deployment: 1,620"),
        ("语序：主语+副词+动词", "Word order: subject + adverb + verb"),
        ("主语+宾语+动词的语序", "Word order: subject + object + verb"),
        ("首尔管理14个地点", "Seoul manages 14 areas"),
        ("깊이 읽기 · 深读", "깊이 읽기 · In depth"),
        ("高考倒计时读法", "How to read the CSAT countdown"),
        ("짙어지다 变浓 · 규모 规模 · 섞다 混淆。",
         "짙어지다 = to thicken, deepen · 규모 = scale · 섞다 = to mix up"),
        ("겁이 나다 害怕 · 중요하다 重要。",
         "겁이 나다 = to feel scared · 중요하다 = to be important"),
        ("예정 预定 · 확정 确定 · 믿다 相信。",
         "예정 = scheduled · 확정 = confirmed · 믿다 = to trust"),
        ("이번 주와 시험 날, 한눈에 보기 · 本周与考试日一表看清",
         "이번 주와 시험 날, 한눈에 보기 · This week vs exam day at a glance"),
        ("연습 · 第 6 版练习", "연습 · Page 6 exercises"),
        ("本周倒计时D-17至D-12", "This week's countdown: D-17 to D-12"),
        ("考试日有特别措施", "Exam day has special measures"),
        ("本周没有特别措施", "This week has no special measures"),
        ("考试日就是D-day", "Exam day is D-day"),
        ("本周氛围是倒计时", "This week's mood is the countdown"),
        ("氛围在现在、本周", "The mood is now, this week"),
        ("特别措施只适用于11月19日", "Special measures apply only on Nov 19"),
        ("措施只适用于11月19日", "The measures apply only on Nov 19"),
        ("听力时段13:10～13:35", "Listening slot 13:10-13:35"),
        ("倒计时氛围在本周", "The countdown mood is this week's"),
        ("特别措施只适用于考试日", "Special measures apply only on exam day"),
        ("从D-17到D-12的一周", "The week from D-17 to D-12"),
        ("大数字显示全国规模", "Big numbers show the national scale"),
        ("听力时段飞机受管制", "Flights are restricted during listening"),
        ("本周是倒计时氛围", "This week is countdown mood"),
        ('instr="造句"', 'instr="Build a sentence"'),
        ('instr="填空"', 'instr="Fill in"'),
        ("完成句子", "fill-in"),
        ("单选", "multiple choice"),
        ("造句", "sentence building"),
        ("判断", "true/false"),
    ],
    "content7.py": [
        ("말 공부 · 语言", "말 공부 · Language"),
        ("三个级别，三个主题", "Three levels, three topics"),
        ("본격적 正式、全面 · 나다 度过。",
         "본격적 = full-scale, in earnest · 나다 = to get through"),
        ("남다 剩下 · 바로 正是、恰恰。",
         "남다 = to remain · 바로 = exactly, right"),
        ("짐작하다 推测 · 나누다 区分。",
         "짐작하다 = to guess · 나누다 = to tell apart"),
        ("立冬＝冬季开始的节气", "Ipdong = the solar term that starts winter"),
        ("泡菜季＝腌过冬泡菜", "Kimjang = making kimchi for winter"),
        ("过冬准备＝为冬天做准备", "Winter prep = getting ready for winter"),
        ("节气＝一年24个时节", "A solar term = one of 24 points in the year"),
        ("11月7日是D-12", "Nov 7 is D-12"),
        ("D-1＝明天", "D-1 = tomorrow"),
        ("11月2日是D-17", "Nov 2 is D-17"),
        ("D-day就是当天", "D-day is the day itself"),
        ("日期不同因标准不同（3版）", "The dates differ because the criteria differ (page 3)"),
        ("林业厅标准是叶子50%", "The Forestry Service criterion is 50% of leaves"),
        ("实际观测10月16日", "Actual observation: Oct 16"),
        ("预报要标准日期一起看", "Read a forecast with its criterion and date together"),
        ("실수 병원 · 易错诊所", "실수 병원 · Error clinic"),
        ("去某地用「에」，不用「를」。", "Use 「에」 for going somewhere, not 「를」."),
        ("「담그다」的过去式是「담갔어요」。", "The past form of 「담그다」 is 「담갔어요」."),
        ("数字与前面要留空格。", "Leave a space before a number."),
        ("助词只用一个。", "Use only one particle."),
        ("이번 주의 틀 · 本周句式", "이번 주의 틀 · Pattern of the week"),
        ("句式拆解：「从〜到〜」。提问：「〜부터 〜까지예요?」",
         "Pattern: 「from 〜 to 〜」. Ask: 「〜부터 〜까지예요?」"),
        ("독자의 편지 · 读者园地", "독자의 편지 · Readers' corner"),
        ("이번 주의 문장 · 本周金句（逐字摘自本期文章）",
         "이번 주의 문장 · Phrases of the week (verbatim from this issue)"),
        ("11 月 7 日是立冬。", "Nov 7 is Ipdong."),
        ("只能说是接近峰值的周末。", "It can only be called a near-peak weekend."),
        ("泡菜季就是腌过冬泡菜。", "Kimjang is making the kimchi eaten all winter."),
        ("离高考还剩 17 天，今天是 D-17。", "There are 17 days left until the CSAT. Today is D-17."),
        ("低处的路红得更晚。", "Low trails colour later."),
        ("KIA 虎三连胜战胜 LG 双子。", "The KIA Tigers beat the LG Twins three straight."),
        ("全国都在为考生加油。", "The whole country cheers the candidates."),
        ("先看日期。", "Look at the date first."),
        ("다음 주 · 下期预告 (VOL.3)", "다음 주 · Next week (VOL.3)"),
        ('instr="填空"', 'instr="Fill in"'),
        ("完成句子", "fill-in"),
        ("单选", "multiple choice"),
    ],
    "content8.py": [
        ("시험과 답 · 测验与答案", "시험과 답 · Test and answers"),
        ("立冬在11月7日周六", "Ipdong falls on Saturday, Nov 7"),
        ("高考在11月19日周四", "The CSAT is on Thursday, Nov 19"),
        ("韩史考试在11月28日周六", "The Korean History exam is Saturday, Nov 28"),
        ("青松现场庆典11月4日起", "Cheongsong on-site festival starts Nov 4"),
        ("KIA三连胜晋级", "Won three straight to advance"),
        ("汉拿山三角峰降雨415.5毫米", "Hallasan Samgakbong rainfall: 415.5 mm"),
        ("首尔万圣节安全人员3,271人", "Seoul Halloween safety staff: 3,271"),
        ("雪岳山实际观测峰值10月16日", "Seoraksan actual observed peak: Oct 16"),
        ("今年考生551,864人", "This year's candidates: 551,864"),
        ("考场全国1,312处", "Test sites nationwide: 1,312"),
        ("内藏山林业厅预报峰值11月4日", "Naejangsan Forestry Service forecast peak: Nov 4"),
        ("内藏山公团预报峰值11月11日", "Naejangsan parks agency forecast peak: Nov 11"),
        ("月出山林业厅预报峰值11月9日", "Wolchulsan Forestry Service forecast peak: Nov 9"),
        ("季后赛首场因雨推迟", "The first playoff game was rained off"),
        ("首尔报名窗口10点至12点", "Seoul sign-up, 10 to 12"),
        ("山火注意期到12月15日", "The wildfire caution period ends Dec 15"),
        ("智敏周六去内藏山", "Jimin goes to Naejangsan on Saturday"),
        ("周日帮忙腌泡菜", "Helps make kimchi on Sunday"),
        ("下周准备韩史考试", "Prepares for the Korean History exam next week"),
        ("智敏喜欢韩国史", "Jimin likes Korean history"),
        ("语序：主语+时间+场所+动词", "Word order: subject + time + place + verb"),
        ("主语+宾语+动词的语序", "Word order: subject + object + verb"),
        ("보러 가요 = 去看", "보러 가요 = to go to see"),
        ("动作场所用「에서」", "Use 「에서」 for the place of an action"),
        # E-zone re-aim KO<->EN: 137/138 keys to English; 139/140 stems to English.
        ('"11月7日是立冬。"', '"Nov 7 is Ipdong."'),
        ('"离高考还剩 12 天。"', '"There are 12 days left until the CSAT."'),
        ("对照第 1 版", "From page 1"),
        ("对照第 5 版", "From page 5"),
        ("对照第 6 版", "From page 6"),
        ("对照第 3 版", "From page 3"),
        ("特别措施只适用于11月19日。→ ___", "Special measures apply only on November 19. → ___"),
        ("我周六去内藏山看红叶。→ ___", "I go to Naejangsan on Saturday to see the autumn leaves. → ___"),
        ("입동=冬季开始的节气 a", "입동 = the solar term that starts winter a"),
        ("절정=最佳时期 b", "절정 = the best time b"),
        ("김장=腌过冬泡菜 c", "김장 = making kimchi for winter c"),
        ("온대저기압=台风10月26日变化 d", "온대저기압 = what the typhoon became on Oct 26 d"),
        ("把词和释义配对", "Match word to meaning"),
        ("周六去内藏山", "Goes to Naejangsan on Saturday"),
        ("泡菜季＝腌过冬泡菜", "Kimjang = making kimchi for winter"),
        ("首尔报名10点开始", "Seoul sign-up starts at 10"),
        ("日期不同因标准不同", "The dates differ because the criteria differ"),
        ("措施只适用于11月19日", "The measures apply only on Nov 19"),
        ("(开放题，范文如下)", "(open task — model text below)"),
        ("范文见本版 H 区（{NCHARS} 字）", "Model text in section H of this page ({NCHARS} characters)"),
        ("답 · 参考答案 — 按版面分页排列，找到题号即可",
         "답 · Answer key — grouped by page; find your item number"),
        ("每题附一句中文简析 · 带 ✓ 的为范文题",
         "Each item has a short English note · ✓ marks the model-writing item"),
        ('instr="翻译"', 'instr="Translate"'),
        ('instr="造句"', 'instr="Build a sentence"'),
        ('instr="写作"', 'instr="Write"'),
        ("完形单选", "cloze"),
        ("单选", "multiple choice"),
        ("造句", "sentence building"),
        ("词汇配对", "matching"),
        ("翻译", "translation"),
        ("写作", "writing"),
    ],
}

# P1 masthead geometry: W43 KO x EN measured instance.
# Core: subtitle y=372, rules 392/401, band y=424, band lines 478/522.
# EN:   subtitle y=366, badge y=394 17pt bold olive centred, rules 412/421,
#       band y=433, band lines 487/531. Headline block (hy=580) unmoved.
GEOM = [
    ('p.text(975, 372, "한국어를 배우는 사람을 위한 주간 신문 — 진짜 한국을, 한국어로", 19, "sans", False, GREY, anchor="middle")',
     'p.text(975, 366, "한국어를 배우는 사람을 위한 주간 신문 — 진짜 한국을, 한국어로", 19, "sans", False, GREY, anchor="middle")\n'
     'p.text(975, 394, "TEXT IN KOREAN · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS", 17, "sans", True, OLIVE, anchor="middle")'),
    ("p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)",
     "p.hline(MX, RIGHT, 412, INK, 3); p.hline(MX, RIGHT, 421, INK, 1.2)"),
    ("p.rect(MX, 424, RIGHT - MX, 118, fill=DARK)",
     "p.rect(MX, 433, RIGHT - MX, 118, fill=DARK)"),
    ('p.text(MX + 30, 478, "11월 7일은 입동이에요 — 겨울의 시작, 단풍의 끝", 36, "sans", True, "#f3edda")',
     'p.text(MX + 30, 487, "11월 7일은 입동이에요 — 겨울의 시작, 단풍의 끝", 36, "sans", True, "#f3edda")'),
    ('p.text(MX + 30, 522, "김장철이 열리고, 수능까지 12일이 남아요. 이번 주의 달력은 오른쪽을 보세요.", 23, "serif", False, "#e8dfc8")',
     'p.text(MX + 30, 531, "김장철이 열리고, 수능까지 12일이 남아요. 이번 주의 달력은 오른쪽을 보세요.", 23, "serif", False, "#e8dfc8")'),
    ('p.text(RIGHT - 30, 478, "立冬", 24, "sans", True, "#b3a06a", anchor="end")',
     'p.text(RIGHT - 30, 487, "START OF WINTER", 24, "sans", True, "#b3a06a", anchor="end")'),
    ('p.text(RIGHT - 30, 522, "立冬在 11 月 7 日周六 · 泡菜季开始", 21, "sans", False, "#b3a06a", anchor="end")',
     'p.text(RIGHT - 30, 531, "Ipdong falls on Saturday, Nov 7 · Kimjang season begins", 21, "sans", False, "#b3a06a", anchor="end")'),
]

# P7 readers'-corner disclosure, rebuilt in English. W43 KO x EN carried a
# single short English honesty line with no explicit solicitation; this
# edition's disclosure states all three facts explicitly (example, not a
# real letter; no real reader letters by press time; no best page 8
# writing by press time), carries the promise to VOL.3, and ends with an
# explicit imperative solicitation covering BOTH letters and page 8
# writing (so the solicitation scope does not rest on the teaser line,
# which names both but is not itself a solicitation). The Korean example
# letter (lt) is frozen verbatim; the core's Korean disclosure line (lko)
# is superseded by this English disclosure, following the W43 KO x EN
# English-only honesty-line precedent.
NEW_LCN = ("Editor's note: this is an example letter from the editors, not a "
           "real reader's letter. No real reader letters or best page 8 writing "
           "had arrived by press time, so the example stands and last issue's "
           "promise carries to VOL.3. Send us your letter and your page 8 writing "
           "— write two sentences in Korean and send them in!")


def apply_reps(fname, reps):
    path = os.path.join(HERE, fname)
    text = open(path, encoding="utf-8").read()
    for old, new in reps:
        n = text.count(old)
        assert n >= 1, f"{fname}: NOT FOUND: {old[:60]!r}"
        text = text.replace(old, new)
        print(f"  {fname}: x{n} {old[:44]!r} -> {new[:44]!r}")
    open(path, "w", encoding="utf-8").write(text)


def apply_letters():
    path = os.path.join(HERE, "content7.py")
    lines = open(path, encoding="utf-8").read().split("\n")
    out = []
    for ln in lines:
        s = ln.strip()
        if s.startswith('lcn = "'):
            out.append('lcn = "' + NEW_LCN + '"')
        elif s.startswith('lko = "') or s.startswith('lcn2 = "'):
            out.append("")  # superseded by the English disclosure
        elif s.startswith("lh = 62 + len(wrap(lt,"):
            out.append('lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26')
        elif ", lko, " in ln or ", lcn2, " in ln:
            out.append("")  # superseded draw calls
        else:
            out.append(ln)
    text = "\n".join(out)
    assert "lko" not in text and "lcn2" not in text, "letters restructure leftovers"
    assert NEW_LCN in text
    open(path, "w", encoding="utf-8").write(text)
    print("  content7.py: letters box rebuilt (lt frozen, English disclosure)")


def main():
    for fname, reps in REPS.items():
        print(f"== {fname}")
        apply_reps(fname, reps)
    print("== content12.py geometry")
    apply_reps("content12.py", GEOM)
    print("== content7.py letters")
    apply_letters()
    print("TRANSFORM DONE")


if __name__ == "__main__":
    main()

# ROUND 2 (after round-1 audit): English-layer shortenings only; no Korean
# text touched. (a) P1 gloss 5 lines -> 3 lines so the numbers box fits
# column 1 again (as in the core) and the drills return to column 2
# ending inside the 1828 headline bottom instead of spilling into row B.
# (b) Over-long dual box titles shortened (W43 KO x EN precedent: short
# English second halves) so title ink stays inside its box. (c) Calendar
# backbone line shortened to one line so it no longer collides with the
# fixed source line below it. (d) P7 disclosure 10 lines -> 8 lines so
# the VOL.3 teaser ends inside the 2540 content limit.
ROUND2 = {
    "content12.py": [
        ("입동 = ipdong, the start of winter · 절정 = peak, the height · 김장 = making kimchi for winter · 상륙하다 = to make landfall · 온대저기압 = extratropical cyclone",
         "입동 = ipdong · 절정 = peak · 김장 = kimchi-making · 상륙하다 = landfall · 온대저기압 = extratropical cyclone"),
        ("숫자로 보는 이번 주 · This week in numbers", "숫자로 보는 이번 주 · Numbers"),
        ("These five dates are the backbone of this issue.", "These five dates frame this issue."),
        ("한능검 접수 · Korean History exam sign-up", "한능검 접수 · Korean History sign-up"),
    ],
    "content34.py": [
        ("단풍 구경 준비물 · Leaf-viewing checklist", "단풍 구경 준비물 · Leaf-viewing list"),
    ],
    "content56.py": [
        ("이번 주 청년 숫자 · This week in youth numbers", "이번 주 청년 숫자 · Youth numbers"),
    ],
}


def apply_round2():
    for fname, reps in ROUND2.items():
        apply_reps(fname, reps)
    apply_letters()
    print("ROUND2 DONE")
