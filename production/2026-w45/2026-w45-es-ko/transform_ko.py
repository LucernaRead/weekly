# -*- coding: utf-8 -*-
"""W45 ES core -> ES x KO fan-out transform (assertion-checked literal replacements).

Rules honoured (tools/README #17/#18, #20 shipped-wins note):
- Whole-line / exact unique literal splicing only, never AST byte offsets.
- Value maps use bare text, never repr literals.
- Applied longest-first per file so a short literal inside a longer literal
  is never clobbered (e.g. "大选在 11 月 29 日" inside "...周日" form).
- Short tokens (type names, instr labels) are replaced in their QUOTED form
  ("单选") so they cannot leak into longer sentences containing the same
  characters ("用方框里的词填空。" is untouched by the instr="填空" pair).
- Type names follow the shipped W43 ESxKO precedent (translated in code,
  1:1 counts): 完成句子->문장 완성, 单选->객관식, 完形单选->빈칸 채우기,
  词汇配对->단어 짝짓기, 判断对错->읽기 판단, 造句->문장 만들기,
  句型转换->문장 바꾸기, 翻译->번역, 写作->쓰기 (incl. the content8
  type check, which therefore reads == "쓰기").
- Furniture is verbatim from the shipped W43 ESxKO edition (VOL.1->VOL.2
  only): badge INSERTED at y=574, 22pt BRICK, strapline y=372 kept frozen.
  README #20's generic claim (ES cores carry a free subtitle slot at
  y=372, badge replaces it in place at 19.5pt) does NOT match the shipped
  W43 ESxKO SVG, where y=372 is the frozen Spanish strapline and the
  badge is inserted at 574 -- shipped SVG wins; see WEEKLY-KIT.md.
- The single Spanish-body punctuation change: the P7 letter attribution
  full-width parens become ASCII parens (words unchanged), as in W45
  ESxEN ruling 2. Everything else Spanish is byte-frozen.
- Idempotent: a pair whose NEW form is already present is SKIPped.

Run from this directory: python3 transform_ko.py
Then: python3 run.py  (single process; never import a content module alone)
Then: python3 render.py
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
EDITION_DIR = "weekly-report-w45-es-ko"
CORE_DIR = "weekly-report-w45-es-core"

# ---- quoted short tokens (type names + instr labels), applied per file ----
TOKENS = [
    ('"完成句子"', '"문장 완성"'),
    ('"完形单选"', '"빈칸 채우기"'),
    ('"词汇配对"', '"단어 짝짓기"'),
    ('"判断对错"', '"읽기 판단"'),
    ('"句型转换"', '"문장 바꾸기"'),
    ('"单选"', '"객관식"'),
    ('"造句"', '"문장 만들기"'),
    ('"翻译"', '"번역"'),
    ('"写作"', '"쓰기"'),
    ('instr="填空"', 'instr="빈칸 채우기"'),
    ('instr="判断"', 'instr="참 / 거짓"'),
    ('instr="改写"', 'instr="바꿔 쓰기"'),
    ('instr="把词和释义配对"', 'instr="단어와 뜻 짝짓기"'),
]

PAIRS = {}

PAIRS["bslib4.py"] = [
    ('"La Lucerna · 西班牙语周报 VOL.2 · LUCERNA SPANISH WEEKLY"',
     '"La Lucerna · 스페인어 주간지 VOL.2 · 텍스트는 스페인어 · 해설은 한국어"'),
    ('f"第 {n} 版 / 共 {total} 版"', 'f"제 {n} 면 / 총 {total} 면"'),
    ('("译注｜" + s', '("해설 — " + s'),
]

PAIRS["content12.py"] = [
    ('p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)\n\n# band',
     'p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)\np.text(975, 574, "스페인어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판", 22, "sans", True, BRICK, anchor="middle")\n\n# band'),
    ('"CADA SEMANA EN ESPAÑOL · 每周一期 · 读西班牙人正在读的西班牙语"',
     '"CADA SEMANA EN ESPAÑOL · 매주 발행 · 스페인이 읽는 스페인어"'),
    ('"西 班 牙 语 周 报 · VOL.2 · LA VIVIENDA · EL PUENTE · EL FÚTBOL"',
     '"스페인어 주간지 · VOL.2 · LA VIVIENDA · EL PUENTE · EL FÚTBOL"'),
    ('"距大选还有 27 天 · 住房决定选战"', '"29-N까지 27일 · 주택이 승부를 정해요"'),
    ('"本期头条 · 详见第 2、6 版"', '"이번 호 헤드라인 · 2, 6면 참조"'),
    ('"LA NOTICIA · 头条"', '"LA NOTICIA · 헤드라인"'),
    ('"讲解｜la cuenta atrás 倒计时 · disolver las Cortes 解散议会 · el decreto 法令 · la candidatura 候选人名单。"',
     '"해설 — la cuenta atrás 카운트다운 · disolver las Cortes 의회 해산 · el decreto 법령 · la candidatura 후보 명단."'),
    ('"LA SEMANA EN CIFRAS · 数字看本周"', '"LA SEMANA EN CIFRAS · 이번 주 숫자"'),
    ('"27 — días faltan el lunes 2 para las elecciones del domingo 29（距 29 日大选 27 天）"',
     '"27 — días faltan el lunes 2 para las elecciones del domingo 29 (29일 선거까지 27일 남았어요)"'),
    ('"9 — comunidades donde el lunes 2 de noviembre es fiesta（11 月 2 日放假的自治区）"',
     '"9 — comunidades donde el lunes 2 de noviembre es fiesta (11월 2일에 쉬는 9개 자치주예요)"'),
    ('"55,7 — % que cita la vivienda como el principal problema, según el CIS de octubre（CIS 十月数据）"',
     '"55,7 — % que cita la vivienda como el principal problema, según el CIS de octubre (10월 CIS 조사)"'),
    ('"AHORA TÚ · 即学即练"', '"AHORA TÚ · 바로 연습해요"'),
    ('"大选在 11 月 29 日周日"', '"선거는 11월 29일 일요일이에요"'),
    ('"住房是选战的决定性议题"', '"주택이 선거운동의 결정적 주제예요"'),
    ('"周一放假的自治区有 9 个"', '"월요일에 쉬는 자치주는 9곳이에요"'),
    ('"马竞–巴萨周日 21:00 开球"', '"아틀레티코–바르사는 일요일 21:00에 시작해요"'),
    ('"NFL 马德里站周日 15:30 开球"', '"마드리드 NFL 경기는 일요일 15:30에 시작해요"'),
    ('"本周五大看点 · Para entender la semana"', '"이번 주 다섯 가지 핵심 · Para entender la semana"'),
    ('"五大看点，不编数字：全在本期里讲清。"', '"다섯 가지 핵심, 숫자 조작 없어요."'),
    ('"EN ESTA EDICIÓN · 本期目录"', '"EN ESTA EDICIÓN · 이번 호 차례"'),
    ('"“竞选预热期”：正式竞选前的几周。"', '"‘선거 전 기간’이에요: 공식 선거운동 전 몇 주예요."'),
    ('"BREVES · 快讯"', '"BREVES · 단신"'),
    ('"QUIZ RELÁMPAGO · 闪电问答"', '"QUIZ RELÁMPAGO · 번개 퀴즈"'),
    ('"读头版，选出正确答案 · 答案见第 8 版"', '"1면을 읽고 정답을 고르세요 · 답은 8면에"'),
    ('"大选在 11 月 29 日"', '"선거는 11월 29일이에요"'),
    ('"NFL 马德里站周日下午"', '"마드리드 NFL 경기는 일요일 오후예요"'),
    ('"马竞–巴萨周日 21:00"', '"아틀레티코–바르사는 일요일 21:00예요"'),
    ('"VIDA · 生活"', '"VIDA · 생활"'),
    ('"NIVEL A2 · El puente del lunes 2 · 11 月 2 日的连休"',
     '"NIVEL A2 · El puente del lunes 2 · 11월 2일 연휴"'),
    ('"EL CALENDARIO · 本周日历"', '"EL CALENDARIO · 이번 주 일정"'),
    ('"Lunes 2 — puente en nueve comunidades; las candidaturas proclamadas llegan al BOE el martes 3（周一九地连休；周二《官方公报》公布正式候选名单）"',
     '"Lunes 2 — puente en nueve comunidades; las candidaturas proclamadas llegan al BOE el martes 3 (월요일 9곳 연휴, 화요일 관보 확정 후보)"'),
    ('"Martes 3 — Champions: Barça–Aston Villa, Atlético–Bayern, Villarreal–PSG（周二欧冠三场西甲球队比赛）"',
     '"Martes 3 — Champions: Barça–Aston Villa, Atlético–Bayern, Villarreal–PSG (화요일 챔피언스리그 스페인 팀 3경기)"'),
    ('"Miércoles 4 — Champions: AEK–Real Madrid, 18:45（周三皇马客场对雅典 AEK）"',
     '"Miércoles 4 — Champions: AEK–Real Madrid, 18:45 (수요일 레알 마드리드, 아테네 AEK 원정)"'),
    ('"Jueves 5 — Europa League: Real Sociedad–Lyon, 18:45（周四皇家社会欧联对里昂）"',
     '"Jueves 5 — Europa League: Real Sociedad–Lyon, 18:45 (목요일 저녁 레알 소시에다드, 유로파리그 리옹전)"'),
    ('"Viernes 6 — Liga, jornada 12: Sevilla–Alavés, 21:00（周五联赛第 12 轮开球）"',
     '"Viernes 6 — Liga, jornada 12: Sevilla–Alavés, 21:00 (금요일 리그 12라운드 시작)"'),
    ('"Sábado 7 — Valencia–Real Madrid, 21:00, en Mestalla（周六瓦伦西亚对皇马）"',
     '"Sábado 7 — Valencia–Real Madrid, 21:00, en Mestalla (토요일 발렌시아 대 레알 마드리드)"'),
    ('"Domingo 8 — NFL en el Bernabéu, 15:30; Atlético–Barça, 21:00（周日 NFL 马德里站＋马竞对巴萨）"',
     '"Domingo 8 — NFL en el Bernabéu, 15:30; Atlético–Barça, 21:00 (일요일 NFL + 아틀레티코–바르사)"'),
    ('"festivo 放假的 · el puente 连休 · la comunidad 自治区 · anochecer 天黑 · el horario de invierno 冬令时。"',
     '"festivo 공휴일인 · el puente 연휴 · la comunidad 자치주 · anochecer 어두워지다 · el horario de invierno 겨울 시간."'),
    ('"11 月 2 日你那里放假吗？连休你做什么：旅行、休息还是看球？写两句西班牙语寄给编辑部。"',
     '"11월 2일에 여러분 동네는 쉬어요? 연휴에는 무엇을 해요: 여행, 휴식, 축구 관람? 스페인어로 두 문장 써서 편집부로 보내 주세요."'),
    ('"¿Y TÚ? · 说说你自己"', '"¿Y TÚ? · 여러분은요?"'),
    ('"LOS DÍAS DE LA SEMANA · 这样说日期"', '"LOS DÍAS DE LA SEMANA · 날짜 말하기"'),
    ('"lunes 2 – domingo 8 de noviembre · 11 月 2 日周一至 8 日周日"',
     '"lunes 2 – domingo 8 de noviembre · 11월 2일 월요일부터 8일 일요일까지"'),
    ('"EJERCICIOS · 第 2 版练习"', '"EJERCICIOS · 2면 연습"'),
    ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
     '"답은 8면에 · 문제는 급이 섞여 있어요, 번호로 찾으세요"'),
    ('"用正确的日期形式补全句子。"', '"바른 날짜 형식으로 문장을 완성하세요."'),
    ('"补全动词的现在时形式。"', '"동사의 현재형으로 문장을 완성하세요."'),
    ('"读第 2 版文章，选出正确答案。"', '"2면 글을 읽고 정답을 고르세요."'),
    ('"11 月 2 日周一"', '"11월 2일 월요일"'),
    ('"11 月 8 日周日"', '"11월 8일 일요일"'),
    ('"每月 1 号说 el uno"', '"매월 1일은 el uno라고 해요"'),
    ('"月份小写"', '"달은 소문자로 써요"'),
    ('"el lunes → es（单数）"', '"el lunes → es (단수)"'),
    ('"九个自治区周一放假"', '"아홉 개 자치주가 월요일에 쉬어요"'),
    ('"诸圣节 11 月 1 日落在周日"', '"모든 성인의 날 11월 1일은 일요일이에요"'),
    ('"加泰罗尼亚周一是工作日"', '"카탈루냐에서는 월요일이 근무일이에요"'),
    ('"冬令时第二周，天黑得早"', '"겨울 시간 두 번째 주, 일찍 어두워져요"'),
    ('"puente=三天连休 b"', '"puente = 사흘 연휴 (b)"'),
    ('"festivo=放假的 a"', '"festivo = 공휴일인 (a)"'),
    ('"anochecer=天黑 c"', '"anochecer = 어두워지다 (c)"'),
    ('"comunidad=自治区 d"', '"comunidad = 자치주 (d)"'),
]

PAIRS["content34.py"] = [
    ('"CULTURA · 文化"', '"CULTURA · 문화"'),
    ('"A2 → B1 · La semana pasada: tres noches de otoño · 上周的三个秋夜"',
     '"A2 → B1 · La semana pasada: tres noches de otoño · 지난주의 세 가을 밤"'),
    ('"sobrio 克制的 · el homenaje 纪念表彰 · el disfraz 服装（化装） · el boniato 红薯 · el cementerio 墓地。"',
     '"sobrio 절제된 · el homenaje 추모 · el disfraz 의상(변장) · el boniato 고구마 · el cementerio 묘지."'),
    ('"你最喜欢哪一夜：29 日、31 日还是 1 日？31 日你吃了什么？写两句寄来。"',
     '"가장 좋아하는 밤은 어느 밤이에요: 29일, 31일, 1일? 31일에는 무엇을 먹었어요? 두 문장 써서 보내 주세요."'),
    ('"¿Y TÚ? · 说说你自己"', '"¿Y TÚ? · 여러분은요?"'),
    ('"EJERCICIOS · 第 3 版练习"', '"EJERCICIOS · 3면 연습"'),
    ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
     '"답은 8면에 · 문제는 급이 섞여 있어요, 번호로 찾으세요"'),
    ('"读第 3 版文章，判断对错。"', '"3면 글을 읽고 참인지 거짓인지 판단하세요."'),
    ('"DANA 纪念活动在 10 月 29 日周四"', '"DANA 추모 행사는 10월 29일 목요일이에요"'),
    ('"Castanyada 吃烤栗子、红薯和 panellets"', '"카스타냐에서는 군밤, 고구마, 파넬레츠를 먹어요"'),
    ('"Samaín 是加利西亚古节，不是万圣节译名"', '"사마인은 갈리시아의 옛 축제예요, 핼러윈 번역명이 아니에요"'),
    ('"诸圣节在 11 月 1 日，不是 10 月 31 日"', '"모든 성인의 날은 11월 1일이에요, 10월 31일이 아니에요"'),
    ('"周日家属去墓地献花"', '"일요일에 가족들이 묘지에 꽃을 가져가요"'),
    ('"用方框里的词填空。"', '"상자 속 단어로 빈칸을 채우세요."'),
    ('"给逝者带花 flores"', '"돌아가신 분께 꽃을 가져가요, flores"'),
    ('"cementerio = 墓地"', '"cementerio = 묘지"'),
    ('"castañas asadas 烤栗子"', '"castañas asadas = 군밤"'),
    ('"disfraz = 化装服装"', '"disfraz = 변장 의상"'),
    ('"actos de memoria 纪念活动"', '"actos de memoria = 추모 행사"'),
    ('"选出正确答案。"', '"정답을 고르세요."'),
    ('"DANA 纪念是 2024 年风暴两周年"', '"DANA 추모는 2024년 폭풍 2주기예요"'),
    ('"Castanyada 在加泰罗尼亚"', '"카스타냐는 카탈루냐에서 해요"'),
    ('"Samaín 是加利西亚古老节日"', '"사마인은 갈리시아의 아주 오래된 축제예요"'),
    ('"三夜之后周一有人连休有人上班"', '"세 밤 뒤 월요일에는 연휴인 사람도, 일하는 사람도 있어요"'),
    ('"把词组成正确的句子。"', '"단어를 바른 문장으로 만드세요."'),
    ('"动词第二位"', '"동사는 두 번째에 와요"'),
    ('"时间在前，动词第二"', '"시간이 앞에 와요, 동사는 두 번째예요"'),
    ('"地点在前，动词第二"', '"장소가 앞에, 동사는 두 번째예요"'),
    ('"间接疑问用 si"', '"간접 의문문에는 si를 써요"'),
    ('"DEPORTE · 体育"', '"DEPORTE · 스포츠"'),
    ('"NIVEL B1 · Europa primero, el domingo a las 21:00 · 欧战在先，周日晚九点"',
     '"NIVEL B1 · Europa primero, el domingo a las 21:00 · 유럽 대회 먼저, 일요일 밤 9시"'),
    ('"la jornada 轮次 · recortar la distancia 缩小分差 · recibir 主场迎战 · visitar 客场挑战 · el Metropolitano 马竞主场。"',
     '"la jornada 라운드 · recortar la distancia 격차 줄이기 · recibir 홈에서 맞다 · visitar 원정으로 가다 · el Metropolitano 메트로폴리타노(아틀레티코 홈구장)."'),
    ('"周日 21:00 你看哪一场？马竞主场谁赢？写两句西班牙语寄来。"',
     '"일요일 21:00에 어느 경기를 봐요? 아틀레티코 홈구장 메트로폴리타노에서는 누가 이길까요? 스페인어로 두 문장 써서 보내 주세요."'),
    ('"LA SEMANA EUROPEA Y LA JORNADA 12 · 欧战周与联赛第 12 轮"',
     '"LA SEMANA EUROPEA Y LA JORNADA 12 · 유럽 주간과 리그 12라운드"'),
    ('"EJERCICIOS · 第 4 版练习"', '"EJERCICIOS · 4면 연습"'),
    ('"读第 4 版文章，选出正确答案。"', '"4면 글을 읽고 정답을 고르세요."'),
    ('"皇马 2–1 赢下国家德比"', '"레알 마드리드가 2–1로 엘 클라시코를 이겼어요"'),
    ('"姆巴佩进了两球"', '"음바페가 두 골을 넣었어요"'),
    ('"周二欧冠三场西甲球队比赛"', '"화요일 챔피언스리그 스페인 팀 3경기예요"'),
    ('"周日 21:00 马竞–巴萨"', '"일요일 21:00 아틀레티코–바르사예요"'),
    ('"周日下午还有 NFL 马德里站"', '"일요일 오후에는 마드리드 NFL 경기도 있어요"'),
    ('"jornada=轮次 b"', '"jornada = 라운드 (b)"'),
    ('"recibir=主场迎战 a"', '"recibir = 홈에서 맞다 (a)"'),
    ('"visitar=客场挑战 d"', '"visitar = 원정 가다 (d)"'),
    ('"recortar=缩小分差 c"', '"recortar = 격차 줄이기 (c)"'),
    ('"用括号里词的比较级或 -ísimo 形式填空。"', '"괄호 속 단어들을 비교급이나 -ísimo 형태로 바꿔 빈칸을 채우세요."'),
    ('"más + importante（马竞–巴萨更重要）"', '"más + importante (아틀레티코–바르사전이 더 중요해요)"'),
    ('"muchísimos partidos 比赛很多"', '"muchísimos partidos = 아주 많은 경기"'),
    ('"malo 的比较级是 peor"', '"malo의 비교급은 peor예요"'),
    ('"bueno 的比较级是 mejor"', '"bueno의 비교급은 mejor예요"'),
    ('"把句子改成过去时（pretérito indefinido）。"', '"문장을 과거형으로 바꾸세요. (pretérito indefinido)"'),
    ('"ir 的过去时是 fueron"', '"ir의 과거형은 fueron예요"'),
]

PAIRS["content56.py"] = [
    ('"JUVENTUD · 青年"', '"JUVENTUD · 청소년"'),
    ('"NIVEL B1 · La NFL en Madrid · NFL 来到马德里"',
     '"NIVEL B1 · La NFL en Madrid · 마드리드에 온 NFL"'),
    ('"EL PLAN DEL PUENTE · 连休计划"', '"EL PLAN DEL PUENTE · 연휴 계획"'),
    ('"1. El lunes 2: descanso y familia — o viaje, si tu comunidad hace puente（周一：休息陪家人；若你那里连休，就去旅行）"',
     '"1. El lunes 2: descanso y familia — o viaje, si tu comunidad hace puente (월요일: 휴식과 가족, 연휴면 여행)"'),
    ('"2. El sábado 7: Valencia–Real Madrid, 21:00, en Mestalla（周六晚：瓦伦西亚对皇马）"',
     '"2. El sábado 7: Valencia–Real Madrid, 21:00, en Mestalla (토요일 밤: 발렌시아 대 레알 마드리드)"'),
    ('"3. El domingo 8, 15:30: la NFL en el Bernabéu（周日下午：NFL 马德里站）"',
     '"3. El domingo 8, 15:30: la NFL en el Bernabéu (일요일 오후: 베르나베우 NFL)"'),
    ('"4. El domingo 8, 21:00: Atlético–Barça en el Metropolitano（周日晚：马竞对巴萨）"',
     '"4. El domingo 8, 21:00: Atlético–Barça en el Metropolitano (일요일 밤 늦은 시간 메트로폴리타노 아틀레티코–바르사)"'),
    ('"5. Y el lunes 9: vuelta a clase y al trabajo; la campaña empieza el viernes 13（返校返工；竞选 13 日开始）"',
     '"5. Y el lunes 9: vuelta a clase y al trabajo; la campaña empieza el viernes 13 (개학·복귀, 선거운동은 13일 시작)"'),
    ('"el emparrillado 美式足球场（烤架形场地） · el himno 国歌 · el touchdown 达阵得分 · la calabaza 南瓜。"',
     '"el emparrillado 미식축구장(그릴) · el himno 국가 · el touchdown 터치다운 · la calabaza 호박."'),
    ('"你看过美式足球比赛吗？你更喜欢足球还是美式足球？写两句寄来。"',
     '"미식축구 경기를 본 적이 있어요? 축구와 미식축구 중 어느 쪽을 더 좋아해요? 두 문장 써서 보내 주세요."'),
    ('"¿Y TÚ? · 说说你自己"', '"¿Y TÚ? · 여러분은요?"'),
    ('"El Bernabéu ___ (原形 acoger) un partido de la NFL."',
     '"El Bernabéu ___ (원형 acoger) un partido de la NFL."'),
    ('"EJERCICIOS · 第 5 版练习"', '"EJERCICIOS · 5면 연습"'),
    ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
     '"답은 8면에 · 문제는 급이 섞여 있어요, 번호로 찾으세요"'),
    ('"读第 5 版文章，选出正确答案。"', '"5면 글을 읽고 정답을 고르세요."'),
    ('"NFL 马德里站周日 15:30"', '"마드리드 NFL 경기는 일요일 15:30예요"'),
    ('"孟加拉虎对猎鹰"', '"벵골스와 팰컨스 경기예요"'),
    ('"西班牙国歌由吉他手演奏"', '"스페인 국가는 기타리스트가 연주해요"'),
    ('"首场 NFL 伯纳乌赛在 2025 年 11 月 16 日"', '"베르나베우 첫 NFL 경기는 2025년 11월 16일이에요"'),
    ('"美式足球用手打、四次进攻"', '"미식축구는 손으로 하고, 네 번의 공격 기회가 있어요"'),
    ('"用方框里的词填空。注意：有的词要变位。"', '"상자 속 단어로 빈칸을 채우세요. 주의: 어떤 단어는 활용해야 해요."'),
    ('"estadio = 体育场"', '"estadio = 경기장"'),
    ('"himno = 国歌"', '"himno = 국가"'),
    ('"acoger 变位 → acoge"', '"acoger 활용 → acoge"'),
    ('"touchdown = 达阵得分"', '"touchdown = 터치다운"'),
    ('"calabaza = 南瓜"', '"calabaza = 호박"'),
    ('"disfraz = 化装服装"', '"disfraz = 변장 의상"'),
    ('"用 ir a + 原形动词改写句子，表示“将要”。"', '"ir a + 동사 원형으로 ‘~할 것’을 나타내세요."'),
    ('"vamos a + 原形"', '"vamos a + 원형"'),
    ('"va a + 原形"', '"va a + 원형"'),
    ('"vas a + 原形"', '"vas a + 원형"'),
    ('"van a + 原形"', '"van a + 원형"'),
    ('"NFL 马德里站是伯纳乌第二场 NFL 比赛"', '"베르나베우 NFL 경기는 마드리드 두 번째예요"'),
    ('"美国国歌由 Momsen 演唱，不是 Sáinz-Villegas"', '"미국 국가는 몸센이 불러요, 사인스-빌레가스가 아니에요"'),
    ('"万圣节之夜在周六 31 日"', '"핼러윈 밤은 토요일 31일이에요"'),
    ('"A FONDO · 深读"', '"A FONDO · 심층"'),
    ('"NIVEL B2 · La vivienda decide la campaña · 住房决定选战"',
     '"NIVEL B2 · La vivienda decide la campaña · 주택이 선거운동을 정해요"'),
    ('"EJERCICIOS · 第 6 版练习"', '"EJERCICIOS · 6면 연습"'),
    ('"看上面两张图，选出正确答案。"', '"위 두 도표를 보고 정답을 고르세요."'),
    ('"CIS 里 PSOE 第一（34%）"', '"CIS에서 PSOE가 1위예요 (34%)"'),
    ('"CIS 里 PP 22,2%"', '"CIS에서 PP는 22,2%예요"'),
    ('"住房是首要问题（55,7%）"', '"주택이 가장 큰 문제예요 (55,7%)"'),
    ('"调查在 10 月 1–6 日进行"', '"조사는 10월 1–6일에 했어요"'),
    ('"本报只刊登 CIS 这一组数据并注明来源日期"', '"이 신문은 CIS 자료 하나만 싣고 출처와 날짜를 밝혀요"'),
    ('"10 月 2 日议会否决两项住房法令"', '"10월 2일에 의회가 주택 법령 두 개를 부결했어요"'),
    ('"10 月 5 日解散议会并召集大选"', '"10월 5일에 의회를 해산하고 선거를 소집했어요"'),
    ('"民调是带误差的具体某天的照片"', '"여론조사는 오차가 있는, 특정 하루의 사진이에요"'),
    ('"竞选 11 月 13 日开始"', '"선거운동은 11월 13일에 시작해요"'),
    ('"es posible que + 虚拟式 tenga"', '"es posible que + 접속법 tenga"'),
    ('"es importante que + 虚拟式 sea"', '"es importante que + 접속법 sea"'),
    ('"para que + 虚拟式（目的）"', '"para que + 접속법 (목적)"'),
    ('"Aunque 后接陈述式（已知事实）"', '"Aunque 뒤에는 직설법 (이미 아는 사실)"'),
    ('"用方框里的词填空：sondeo · muestra · indecisos · margen de error"',
     '"상자 속 단어로 빈칸을 채우세요: sondeo · muestra · indecisos · margen de error"'),
    ('"sondeo = 民调"', '"sondeo = 여론조사"'),
    ('"muestra = 样本（5.025 人）"', '"muestra = 표본 (5.025명)"'),
    ('"indecisos = 未决定者"', '"indecisos = 미결정자"'),
    ('"margen de error = 误差范围"', '"margen de error = 오차 범위"'),
]

PAIRS["content7.py"] = [
    ('"LENGUA · 语言"', '"LENGUA · 언어"'),
    ('"语言聚焦 · Tres niveles, tres herramientas · 三个级别，三件工具"',
     '"언어 집중 · Tres niveles, tres herramientas · 세 단계, 세 가지 도구"'),
    ('"日期格式：el lunes 2 de noviembre；星期、月份小写；1 号说 el uno。"',
     '"날짜 형식: el lunes 2 de noviembre예요. 요일과 달은 소문자로 쓰고, 1일은 el uno라고 해요."'),
    ('"el lunes 2 de noviembre 连休"', '"el lunes 2 de noviembre = 연휴예요"'),
    ('"29 日是周日"', '"29일은 일요일이에요"'),
    ('"月份小写：noviembre"', '"달은 소문자: noviembre"'),
    ('"比较级 más…que、tan…como；bueno→mejor、malo→peor；绝不说 más mejor。"',
     '"비교급은 más…que, tan…como예요. bueno→mejor, malo→peor예요. más mejor라고 절대 말하지 않아요."'),
    ('"más + cara（房价更高）"', '"más + cara (집값이 더 높아요)"'),
    ('"tan + alta + como（同样高）"', '"tan + alta + como (똑같이 높아요)"'),
    ('"bueno 的比较级是 mejor（不用 más）"', '"bueno의 비교급은 mejor예요 (más는 붙이지 않아요)"'),
    ('"más mejor 是错误说法"', '"más mejor는 틀린 말이에요"'),
    ('"es necesario que、para que、ojalá 后用虚拟式；creo que 后用陈述式。"',
     '"es necesario que, para que, ojalá 뒤에는 접속법을 써요. creo que 뒤에는 직설법을 써요."'),
    ('"es necesario que + 虚拟式 baje"', '"es necesario que + 접속법 baje"'),
    ('"para que + 虚拟式 sea"', '"para que + 접속법 sea"'),
    ('"creo que + 陈述式 es"', '"creo que + 직설법 es"'),
    ('"ojalá + 虚拟式：baje"', '"ojalá + 접속법: baje"'),
    ('"lunes 是单数，动词用 es。"', '"lunes는 단수예요, 동사는 es를 써요."'),
    ('"mejor 本身就是比较级，不加 más。"', '"mejor 자체가 비교급이라 más를 붙이지 않아요."'),
    ('"gente 是单数集合名词，动词用单数。"', '"gente는 단수 집합 명사예요, 동사는 단수예요."'),
    ('"creo que 表肯定，用陈述式 es。"', '"creo que는 확신이라 직설법 es를 써요."'),
    ('"ERRORES TÍPICOS · 常见错误"', '"ERRORES TÍPICOS · 자주 하는 실수"'),
    ('"precampaña = 竞选预热期：正式竞选前的几周。本期就是 precampaña；竞选 13 日周五开始。"',
     '"precampaña = 선거 전 기간: 공식 선거운동 전 몇 주예요. 이번 호 자체가 precampaña예요. 선거운동은 13일 금요일에 시작해요."'),
    ('"LA PALABRA · 本周生词"', '"LA PALABRA · 이번 주 단어"'),
    ('— Ana （ejemplo, escrito por la redacción）', '— Ana (ejemplo, escrito por la redacción)'),
    ('"编辑部说明：截至本期截稿，未收到真实读者来信与第 8 版最佳作文，故本期登载编辑部示例信，承诺顺延至 VOL.3。欢迎来信！"',
     '"편집부 알림: 마감 때까지 실제 편지와 8면 최고 글이 없어서 예시 편지를 실어요. 약속은 VOL.3으로 이어져요. 편지 보내 주세요!"'),
    ('"FRASES DE LA SEMANA · 本周金句（逐字摘自本期文章）"',
     '"FRASES DE LA SEMANA · 이번 주 문장 (이번 호 글에서 그대로 뽑았어요)"'),
    ('"名单已提交：现在各党开始撰写纲领。"', '"명단이 제출됐어요. 이제 각 당이 강령을 쓰기 시작해요."'),
    ('"11 月 2 日周一九个自治区放假，其他地区照常上班。"', '"11월 2일 월요일에는 9개 자치주가 쉬고, 다른 지역은 평소처럼 일해요."'),
    ('"三个节日，同一个秋夜。"', '"세 축제, 하나의 가을 밤이에요."'),
    ('"皇马在诺坎普 2–1 获胜：这是巴萨本赛季联赛首败。"', '"레알 마드리드가 캄 노우에서 2–1로 이겼어요. 바르사의 이번 시즌 리그 첫 패배예요."'),
    ('"伯纳乌把草皮换成烤架形球场：美式足球来到马德里。"', '"베르나베우는 잔디를 그릴 모양 구장으로 바꿨어요. 미식축구가 마드리드에 왔어요."'),
    ('"住房是 55.7% 的西班牙人的首要问题。"', '"주택은 스페인 사람 55.7%의 가장 큰 문제예요."'),
    ('"一次民调就是一张带误差的照片，拍于某一天。"', '"여론조사 한 번은 오차가 있는 사진 한 장, 특정 하루에 찍은 사진이에요."'),
    ('"11 月 8 日周日，马德里有两场约会：15:30 的 NFL 和 21:00 的马竞对巴萨。"',
     '"11월 8일 일요일, 마드리드에는 두 가지 약속이 있어요: 15:30 NFL과 21:00 아틀레티코–바르사."'),
    ('"LA PRÓXIMA SEMANA · 下期预告 (VOL.3)"', '"LA PRÓXIMA SEMANA · 다음 호 예고 (VOL.3)"'),
]

PAIRS["content8.py"] = [
    ('"EJERCICIOS Y RESPUESTAS · 练习与答案"', '"EJERCICIOS Y RESPUESTAS · 연습과 답"'),
    ('"第 8 版 · La gran prueba de la semana + todas las respuestas"',
     '"제 8면 · La gran prueba de la semana + todas las respuestas"'),
    ('"ganó 2–1 = 以 2–1 获胜"', '"ganó 2–1 = 2–1로 이겼어요"'),
    ('"marcar dos goles = 进两球"', '"marcar dos goles = 두 골을 넣었어요"'),
    ('"primera derrota liguera = 联赛首败"', '"primera derrota liguera = 리그 첫 패배"'),
    ('"recortar = 缩小分差"', '"recortar = 격차를 줄이다"'),
    ('"acoger = 承办（伯纳乌承办 NFL）"', '"acoger = 개최하다 (베르나베우가 NFL을 개최해요)"'),
    ('"el emparrillado = 美式足球场"', '"el emparrillado = 미식축구장"'),
    ('"周日上演马竞–巴萨"', '"일요일에 아틀레티코–바르사가 열려요"'),
    ('"himno = 国歌"', '"himno = 국가"'),
    ('"DANA 纪念活动在 10 月 29 日周四"', '"DANA 추모 행사는 10월 29일 목요일이에요"'),
    ('"周一放假的自治区有 9 个"', '"월요일에 쉬는 자치주는 9곳이에요"'),
    ('"大选在 11 月 29 日"', '"선거는 11월 29일이에요"'),
    ('"竞选 11 月 13 日开始"', '"선거운동은 11월 13일에 시작해요"'),
    ('"诸圣节 11 月 1 日"', '"모든 성인의 날은 11월 1일이에요"'),
    ('"马竞–巴萨与 NFL 都在周日"', '"아틀레티코–바르사와 NFL이 모두 일요일이에요"'),
    ('"Castanyada 吃 panellets"', '"카스타냐에서는 파넬레츠를 먹어요"'),
    ('"CIS 十月调查：住房 55,7%"', '"10월 CIS 조사: 주택 55,7%"'),
    ('"马德里在放假名单里"', '"마드리드는 휴일 명단에 있어요"'),
    ('"加泰罗尼亚周一是工作日"', '"카탈루냐에서는 월요일이 근무일이에요"'),
    ('"Ana 只看 NFL；晚上看马竞–巴萨的是 Pablo"', '"아나는 NFL만, 밤 아틀레티코–바르사는 파블로예요"'),
    ('"标题概括两地对比"', '"제목이 두 지역 대비를 요약해요"'),
    ('"主语 + 动词 + 地点"', '"주어 + 동사 + 장소"'),
    ('"时间在前"', '"시간이 앞에 와요"'),
    ('"a las nueve = 在九点"', '"a las nueve = 9시에"'),
    ('"疑问词在句首"', '"의문사가 문장 맨 앞에 와요"'),
    ('"周一在九个自治区是假日。"', '"월요일은 아홉 개 자치주에서 공휴일이에요."'),
    ('"对照原文"', '"원문과 대조해 보세요"'),
    ('"周日我们看 NFL 和马竞–巴萨。"', '"일요일에 우리는 NFL과 아틀레티코–바르사를 봐요."'),
    ('"acoger = 承办"', '"acoger = 개최하다"'),
    ('"伯纳乌承办一场 NFL 比赛。→ ___"', '"베르나베우는 NFL 경기를 개최해요. → ___"'),
    ('"tener que = 必须"', '"tener que = 반드시 해야 해요"'),
    ('"每个图表都必须标明来源。→ ___"', '"모든 도표는 출처를 밝혀야 해요. → ___"'),
    ('"sondeo=民调 c"', '"sondeo = 여론조사 (c)"'),
    ('"muestra=样本 d"', '"muestra = 표본 (d)"'),
    ('"margen de error=误差范围 b"', '"margen de error = 오차 범위 (b)"'),
    ('"junta electoral=选举委员会 a"', '"junta electoral = 선거관리위원회 (a)"'),
    ('"alquiler = 租金"', '"alquiler = 임대료"'),
    ('"tres habitaciones = 三居室"', '"tres habitaciones = 방 세 개"'),
    ('"¿cuánto cuesta? 多少钱"', '"¿cuánto cuesta? = 얼마예요?"'),
    ('"firmar = 签（合同）"', '"firmar = 서명하다 (계약)"'),
    ('"mudanza = 搬家"', '"mudanza = 이사"'),
    ('"写作题（无唯一答案）；范文（84 词）见下。"',
     '"쓰기 문제예요 (정답은 하나가 아니에요). 모범 답안 (84단어)은 아래에 있어요."'),
    ('"（开放题，范文如下）"', '"(열린 문제 — 모범 답안은 아래에 있어요)"'),
    ('"范文见本版 H 区（84 词）"', '"모범 답안은 이 면 H 구역에 있어요 (84단어)"'),
    ('"RESPUESTAS · 参考答案 — 按版面分页排列，找到题号即可"',
     '"RESPUESTAS · 정답 — 면별로 나누어 실었어요, 번호로 찾으세요"'),
    ('"每题附一句中文简析 · 带 ✓ 的为范文题"',
     '"문제마다 한국어 해설 한 줄 · ✓ 표시는 모범 답안 문제예요"'),
    ('f"— PÁGINA {pg} —"', 'f"— 제 {pg} 면 —"'),
]

# FIXUP (after PAIRS+TOKENS): shorten our own Korean strings that overflow
# under the BUILD toolchain's metrics (tools venv PIL 13; system PIL 10.2
# measures ~3px narrower, so borderline strings must be checked with venv).
# F1: P7 errs mejor note wraps to 2 lines under venv (391.4px > 390px box),
# growing col 3 by one line and pushing the preview box bottom to 2584.6,
# across the footer rule at 2580. Shortened form is 355.5px, 1 line, and
# restores the core preview geometry exactly (bottom 2558.08).
FIXUP_PAIRS = {
    "content7.py": [
        ('"mejor 자체가 비교급이라 más를 붙이지 않아요."',
         '"mejor 자체가 비교급이라 más는 안 붙여요."'),
    ],
    "content12.py": [
        # F2: P1 CINCO CLAVES subtitle inks to 1898.2, past the col-3 box
        # border at 1885 (occlusion BOXTITLE, NEW vs core). Shortened form
        # inks to 362.1px (start 1473 -> right 1835.1), clearing the border.
        ('"이번 주 다섯 가지 핵심 · Para entender la semana"',
         '"다섯 가지 핵심 · Para entender la semana"'),
    ],
}

# render.py / svglib.py repointing + non-rendered comment
REPOINTS = [
    ("render.py", CORE_DIR, EDITION_DIR),
    ("render.py", '"La-Lucerna-VOL2.pdf"', '"La-Lucerna-VOL2-KO.pdf"'),
    ("render.py", '"La-Lucerna-VOL2-web.pdf"', '"La-Lucerna-VOL2-KO-web.pdf"'),
    ("svglib.py", "for 重阳.", "for Double Ninth."),
]


def apply_pairs(fname, pairs, require=True, final_forms=None):
    path = os.path.join(HERE, fname)
    src = open(path, encoding="utf-8").read()
    # longest first; tokens last (quoted short forms are substring-safe)
    ordered = sorted(pairs, key=lambda p: -len(p[0]))
    for old, new in ordered:
        # already applied: either the direct new form is present, or a
        # later FIXUP already rewrote it to its final form
        final = (final_forms or {}).get(new)
        if old not in src and (new in src or (final and final in src)):
            print(f"{fname}: SKIP already applied :: {old[:60]}")
            continue
        n = src.count(old)
        if n == 0 and not require:
            print(f"{fname}: SKIP absent token :: {old[:60]}")
            continue
        assert n >= 1, f"{fname}: NOT FOUND (0x): {old[:120]}"
        src = src.replace(old, new)
        print(f"{fname}: x{n} :: {old[:60]}")
    open(path, "w", encoding="utf-8").write(src)


def main():
    # map each PAIRS new form to its FIXUP final form (per file), so a
    # re-run after FIXUP still recognises the pair as applied
    final_forms = {}
    for fname, pairs in FIXUP_PAIRS.items():
        for old, new in pairs:
            final_forms.setdefault(fname, {})[old] = new
    for fname, pairs in PAIRS.items():
        apply_pairs(fname, pairs, final_forms=final_forms.get(fname))
    for fname, pairs in [("bslib4.py", []), ("content12.py", TOKENS),
                         ("content34.py", TOKENS), ("content56.py", TOKENS),
                         ("content7.py", TOKENS), ("content8.py", TOKENS)]:
        if pairs:
            # a token legitimately absent from a file (e.g. no cloze items
            # on P1/P2) is a skip, not a failure
            apply_pairs(fname, pairs, require=False)
    for fname, pairs in FIXUP_PAIRS.items():
        apply_pairs(fname, pairs)
    for fname, old, new in REPOINTS:
        path = os.path.join(HERE, fname)
        src = open(path, encoding="utf-8").read()
        if new in src and old not in src:
            print(f"{fname}: SKIP repoint :: {old[:60]}")
            continue
        n = src.count(old)
        assert n >= 1, f"{fname}: REPOINT NOT FOUND: {old[:120]}"
        src = src.replace(old, new)
        open(path, "w", encoding="utf-8").write(src)
        print(f"{fname}: repoint x{n} :: {old[:60]}")
    # OUT repointing in every content module (all expanduser forms)
    for fname in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        path = os.path.join(HERE, fname)
        src = open(path, encoding="utf-8").read()
        if EDITION_DIR in src and CORE_DIR not in src:
            print(f"{fname}: SKIP OUT already repointed")
            continue
        assert CORE_DIR in src, f"{fname}: OUT core path missing"
        src = src.replace(CORE_DIR, EDITION_DIR)
        open(path, "w", encoding="utf-8").write(src)
        print(f"{fname}: OUT -> {EDITION_DIR}")
    print("TRANSFORM DONE")


if __name__ == "__main__":
    main()
