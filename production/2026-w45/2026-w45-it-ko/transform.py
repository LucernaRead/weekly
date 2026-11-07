# -*- coding: utf-8 -*-
"""IT x KO fan-out transform for the W45 IT core build copy.

Rules: counted exact-string replacements with sequential simulation
(substring-safe order: longer strings before their substrings, specifics
before globals); the simulation asserts every count BEFORE anything is
written, and aborts without writing on any mismatch. Italian body text is
NEVER touched: every `old` below is a Chinese explanation-layer string, a
bilingual furniture string, or a printed instruction token. Two P8
section-E keys are re-aimed (Chinese sentence -> Korean sentence), exactly
as the shipped W43 IT x KO did; all other keys are byte-identical.

Furniture follows the shipped W43 IT x KO SVG verbatim (no inserted badge
line, per that edition's adjudication: the y=372 slot carries the frozen
Italian tagline; pairing is carried by the top strip, serif line and
footer): footer VOL.2, page line, gloss prefix, P8 separators, band
titles, E TU? label, P8 header. P7 word-box rule: the Italian definition
sentence (wt) is byte-frozen; only the Korean gloss note below it is
localised. P7 readers' box: Italian letter byte-frozen incl. its
`(esempio della redazione)` tag; the disclosure below it is Korean and
states all three facts (no real letters, no best P8 writing yet,
example + promise deferred to VOL.3) plus an explicit imperative
invitation with a VOL.3 publication promise.

OUT repoint + render.py are handled first (direct, asserted), then the
counted simulation over the six operative files.
"""
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
FILES = ["bslib4.py", "content12.py", "content34.py",
         "content56.py", "content7.py", "content8.py"]


def rep_file(fname, old, new, expect):
    p = os.path.join(BASE, fname)
    s = open(p, encoding="utf-8").read()
    n = s.count(old)
    if n == 0 and s.count(new) >= 1:
        print(f"repoint {fname}: already applied, skipped")
        return
    assert n == expect, f"{fname}: {old!r} count {n} != {expect}"
    open(p, "w", encoding="utf-8").write(s.replace(old, new))
    print(f"repoint {fname}: {n}x {old!r}")


# ---------- OUT repoint ----------
for f in FILES[:0]:
    pass
for f in ["content12.py", "content34.py", "content56.py",
          "content7.py", "content8.py"]:
    rep_file(f, "weekly-report-w45-it-core", "weekly-report-w45-it-ko", 1)
rep_file("render.py", "weekly-report-w45-it-core",
         "weekly-report-w45-it-ko", 1)
rep_file("render.py", "La-Lucerna-VOL2-web.pdf",
         "La-Lucerna-VOL2-KO-web.pdf", 1)
rep_file("render.py", "La-Lucerna-VOL2.pdf",
         "La-Lucerna-VOL2-KO.pdf", 1)

# ---------- svglib docstring comment only (not rendered) ----------
rep_file("svglib.py", "for 重阳.", "for Double Ninth.", 1)

R = []


def A(old, new, n=1):
    R.append((old, new, n))


# ---------- bslib4 furniture (W43 IT x KO verbatim, VOL.2) ----------
A("La Lucerna · 意大利语周报 VOL.2 · LUCERNA ITALIAN WEEKLY",
  "La Lucerna · 이탈리아어 주간지 VOL.2 · 텍스트는 이탈리아어 · 해설은 한국어")
A("第 {n} 版 / 共 {total} 版", "제 {n} 면 / 총 {total} 면")
A("译注｜", "해설 — ")

# ---------- P1 ----------
A("OGNI SETTIMANA IN ITALIANO · 每周一期 · 读意大利人正在读的意大利语",
  "WEEKLY IN ITALIAN · 매주 발행 · 이탈리아가 읽는 이탈리아어")
A("意 大 利 语 周 报 · VOL.2 · IL PRIMO FREDDO · IL PANETTONE · LA SERIE A",
  "이탈리아어 주간지 · VOL.2 · IL PRIMO FREDDO · IL PANETTONE · LA SERIE A")
A("本周迎来第一场寒冷", "이번 주 첫 추위가 찾아와요")
A("初寒之周 · 详见第 2 版", "첫 추위의 주 · 2면 참고")
A("LA NOTIZIA · 头条", "LA NOTIZIA · 헤드라인")
A("讲解｜il primo freddo 第一场寒冷 · il versante adriatico 亚得里亚海一侧 · la previsione 预报 · assaggi 品尝。",
  "해설 — il primo freddo = 첫 추위 · il versante adriatico = 아드리아해 쪽 · la previsione = 예보 · assaggi = 맛보기예요.")
A("LA SETTIMANA IN CIFRE · 数字看本周", "LA SETTIMANA IN CIFRE · 숫자로 보는 이번 주")
A("1.300–1.500 — i metri di quota dove può cadere la prima neve leggera（可能下初雪的海拔）",
  "1.300–1.500 — i metri di quota dove può cadere la prima neve leggera (초설이 내릴 수 있는 고도예요)")
A("50+ — gli eventi del Forum Cultura di Milano, dal 3 all'8 novembre（米兰文化论坛 50 多场活动）",
  "50+ — gli eventi del Forum Cultura di Milano, dal 3 all'8 novembre (밀라노 문화 포럼 50개 이상 행사예요)")
A("19 — i paesi dei pasticceri alla finale del Panettone a Milano（参加米兰潘妮托尼决赛的国家数）",
  "19 — i paesi dei pasticceri alla finale del Panettone a Milano (밀라노 파네토네 결승 참가국 수예요)")
A("11ª — la giornata di Serie A del fine settimana（本周末意甲第 11 轮）",
  "11ª — la giornata di Serie A del fine settimana (이번 주말 세리에 A 11라운드예요)")
A("ADESSO TU · 即学即练", "ADESSO TU · 바로 연습")
A("il primo freddo = 第一场寒冷", "il primo freddo = 첫 추위")
A("la prima neve leggera = 初雪", "la prima neve leggera = 초설")
A("文化论坛与潘妮托尼决赛都在米兰", "문화 포럼과 파네토네 결승은 모두 밀라노에서 열려요")
A("克雷莫纳的节日叫 Festa del Torrone", "크레모나 축제는 Festa del Torrone예요")
A("previsioni = 预报（复数）", "previsioni = 예보 (복수)")
A("本周日程 · Cosa succede, giorno per giorno", "이번 주 일정 · Cosa succede, giorno per giorno")
A("日程以各活动日历为准，时间可能有变。", "일정은 각 행사 달력 기준이에요. 시간이 바뀔 수 있어요.")
A("IN QUESTO NUMERO · 本期目录", "IN QUESTO NUMERO · 이번 호 차례")
A("“第一场寒冷”：温和秋天后的第一波寒冷。", "'첫 추위': 온화한 가을 뒤 첫 추위예요.")
A("IN BREVE · 快讯", "IN BREVE · 단신")
A("QUIZ LAMPO · 闪电问答", "QUIZ LAMPO · 번개 퀴즈")
A("读头版，选出正确答案 · 答案见第 8 版", "1면을 읽고 알맞은 답을 고르세요 · 정답은 8면")
A("第一场寒冷在周一 11 月 2 日到来", "첫 추위는 월요일 11월 2일에 찾아와요")
A("初雪在 1300–1500 米左右", "초설은 1,300–1,500m쯤에 내려요", 2)
A("潘妮托尼决赛在米兰", "파네토네 결승은 밀라노에서 열려요", 2)

# ---------- P2 ----------
A("VITA · 生活", "VITA · 생활")
A("LIVELLO A2 · Il primo freddo e il 2 novembre · 初寒与追思日",
  "LIVELLO A2 · Il primo freddo e il 2 novembre · 첫 추위와 추모의 날")
A("发稿时表决结果尚未确认，详见第 6 版。", "인쇄할 때 표결 결과는 아직 확인되지 않았어요. 6면을 보세요.")
A("LA FRASE PER RICORDARE · 口诀", "LA FRASE PER RICORDARE · 암기 문장")
A("il cappotto 大衣 · la sciarpa 围巾 · i guanti 手套 · a strati 分层穿衣 · il termosifone 暖气片 · il crisantemo 菊花",
  "il cappotto 외투 · la sciarpa 목도리 · i guanti 장갑 · a strati 겹쳐 입기 · il termosifone 난방기 · il crisantemo 국화")
A("初寒来了你穿什么：大衣、围巾还是手套？写两句意大利语寄给编辑部。",
  "첫 추위가 오면 무엇을 입어요: 외투, 목도리, 장갑? 이탈리아어로 두 문장을 써서 편집부로 보내 주세요.", 2)
A("IL 2 NOVEMBRE · 追思日", "IL 2 NOVEMBRE · 추모의 날")
A("ESERCIZI · 第 2 版练习", "ESERCIZI · 제 2 면 연습")
A("用意大利语补全句子。", "이탈리아어로 문장을 완성하세요.")
A("cappotto = 大衣", "cappotto = 외투")
A("sciarpa = 围巾", "sciarpa = 목도리")
A("guanti = 手套（复数）", "guanti = 장갑 (복수)")
A("crisantemi = 菊花（复数）", "crisantemi = 국화 (복수)")
A("termosifoni = 暖气片（复数）", "termosifoni = 난방기 (복수)")
A("补全动词的现在时形式。", "동사의 현재형으로 빈칸을 채우세요.")
A("fare freddo：fa freddo（天气）", "fare freddo: fa freddo (날씨)")
A("读第 2 版文章，选出正确答案。", "2면 기사를 읽고 알맞은 답을 고르세요.")
A("11 月 2 日是追思日", "11월 2일은 추모의 날이에요", 2)
A("追思日的花是菊花", "추모의 날 꽃은 국화예요", 2)
A("分层穿衣：a strati", "겹쳐 입기: a strati")
A("诸圣节今年是周日、无连休", "올해 만성절은 일요일이라 연휴가 없어요")
A("cappotto=御寒大衣 c", "cappotto=추위 막는 외투 c")
A("sciarpa=围巾 d", "sciarpa=목도리 d")
A("crisantemo=十一月的花 a", "crisantemo=11월의 꽃 a")
A("termosifone=暖气片 b", "termosifone=난방기 b")

# ---------- P3 ----------
A("CULTURA · 文化", "CULTURA · 문화")
A("A2 → B1 · Panettone, torrone e musei aperti · 甜点与博物馆",
  "A2 → B1 · Panettone, torrone e musei aperti · 디저트와 박물관")
A("il panettone 米兰圣诞面包 · il torrone 牛轧糖 · l'assaggio 品尝 · la bancarella 摊位 · il cantiere 施工现场/修复工地。",
  "il panettone 밀라노 크리스마스 빵 · il torrone 토로네 · l'assaggio 맛보기 · la bancarella 노점 · il cantiere 공사 현장/복원 현장예요.")
A("你更喜欢传统潘妮托尼还是巧克力味的？写两句寄来。",
  "전통 파네토네와 초콜릿 파네토네 중 어느 쪽이 더 좋아요? 두 문장을 써서 보내 주세요.", 2)
A("ESERCIZI · 第 3 版练习", "ESERCIZI · 제 3 면 연습")
A("读第 3 版文章，选出正确答案。", "3면 기사를 읽고 알맞은 답을 고르세요.")
A("克雷莫纳牛轧糖节到 11 月 22 日", "크레모나 토로네 축제는 11월 22일까지 이어져요")
A("文化论坛 11 月 3 日周二开幕", "문화 포럼은 11월 3일 화요일에 열려요")
A("panettone = 米兰圣诞面包", "panettone = 밀라노 크리스마스 빵")
A("bancarella = 摊位", "bancarella = 노점")
A("mandorle = 杏仁（复数）", "mandorle = 아몬드 (복수)")
A("tartufo = 松露", "tartufo = 트러플")
A("用 passato prossimo（近过去时）补全，注意助动词 avere / essere。",
  "passato prossimo (근과거)로 완성하세요. 조동사 avere / essere에 주의하세요.")
A("assaggiare 用 avere：abbiamo assaggiato", "assaggiare는 avere를 써요: abbiamo assaggiato")
A("aprire 用 avere：ha aperto", "aprire는 avere를 써요: ha aperto")
A("把词组成正确的句子。", "단어를 배열해 알맞은 문장을 만드세요.")
A("地点在前，主语在后", "장소가 앞에, 주어가 뒤에 와요")
A("dura fino a = 持续到", "dura fino a = ~까지 이어져요")

# ---------- P4 ----------
A("SPORT · 体育", "SPORT · 스포츠")
A("LIVELLO B1 · La Serie A e l'Europa · 意甲与欧战",
  "LIVELLO B1 · La Serie A e l'Europa · 세리에 A와 유럽 대회")
A("la giornata 轮次 · la presentazione 赛前介绍 · gli spalti 看台 · la sera 晚上。",
  "la giornata 라운드 · la presentazione 경기 전 소개 · gli spalti 관중석 · la sera 저녁예요.")
A("周日晚上你看哪场比赛？写两句意大利语寄来。",
  "일요일 저녁에는 어떤 경기를 봐요? 이탈리아어로 두 문장을 써서 보내 주세요.", 2)
A("LA SETTIMANA DEL CALCIO · 足球周", "LA SETTIMANA DEL CALCIO · 축구 주간")
A("ESERCIZI · 第 4 版练习", "ESERCIZI · 제 4 면 연습")
A("读第 4 版文章，选出正确答案。", "4면 기사를 읽고 알맞은 답을 고르세요.")
A("周日晚上佛罗伦萨对尤文图斯", "일요일 저녁 피오렌티나–유벤투스 경기예요")
A("欧战第 4 轮在 11 月 3–5 日", "유럽 대회 4라운드는 11월 3–5일이에요")
A("欧战比赛只作前瞻、无结果", "유럽 대회 경기는 미리보기만 하고 결과는 없어요")
A("国米对科莫在圣西罗", "인테르–코모 경기는 산 시로에서 열려요")
A("giornata=联赛的一轮 c", "giornata=리그의 한 라운드 c")
A("presentazione=赛前介绍 b", "presentazione=경기 전 소개 b")
A("spalti=看台 a", "spalti=관중석 a")
A("sera=晚上 d", "sera=저녁 d")
A("用括号里词的比较级填空（数据看赛程表）。", "괄호 안 단어의 비교급으로 빈칸을 채우세요 (일정은 표를 보세요).")
A("周日晚上的比赛晚于周五的：più tardi", "일요일 저녁 경기는 금요일보다 늦어요: più tardi")
A("周五的比赛早于周日的：più presto", "금요일 경기는 일요일보다 빨라요: più presto")
A("più + bella 周日晚最美（主观评价）", "più + bella, 일요일 저녁이 가장 아름다워요 (주관적 평가)")
A("bene 的比较级是不规则的 meglio", "bene의 비교급은 불규칙한 meglio예요")
A("用 passato prossimo 补全。", "passato prossimo로 완성하세요.")
A("arrivare 用 essere，复数 sono arrivati", "arrivare는 essere를 써요. 복수 sono arrivati")
A("guardare 用 avere：abbiamo guardato", "guardare는 avere를 써요: abbiamo guardato")
A("prendere 的分词是 preso：ha preso", "prendere의 분사는 preso예요: ha preso")

# ---------- P5 ----------
A("GIOVANI · 青年", "GIOVANI · 청년")
A("LIVELLO B1 · Dopo Lucca: cultura, cinema e weekend · 卢卡之后",
  "LIVELLO B1 · Dopo Lucca: cultura, cinema e weekend · 루카 이후")
A("1. Martedì: il Forum Cultura apre a Milano（周二：米兰文化论坛开幕）",
  "1. Martedì: il Forum Cultura apre a Milano (화요일: 밀라노 문화 포럼 개막)")
A("2. Mercoledì–giovedì: le coppe europee in TV（周三至周四：欧战直播）",
  "2. Mercoledì–giovedì: le coppe europee in TV (수요일–목요일: 유럽 대회 중계)")
A("3. Venerdì: si prepara il weekend（周五准备周末）",
  "3. Venerdì: si prepara il weekend (금요일 주말 준비)")
A("4. Sabato: assaggi a Milano o a Cremona（周六：米兰或克雷莫纳品尝）",
  "4. Sabato: assaggi a Milano o a Cremona (토요일: 밀라노나 크레모나에서 맛보기)")
A("5. Domenica: Serie A e rientro（周日：意甲与返程）",
  "5. Domenica: Serie A e rientro (일요일: 세리에 A와 귀가)")
A("il cosplay 角色扮演服装 · gratuito 免费的 · il documentario 纪录片 · lo schermo 银幕。",
  "il cosplay 코스프레 의상 · gratuito 무료인 · il documentario 다큐멘터리 · lo schermo 스크린예요.")
A("卢卡之后你去哪：文化论坛、电影还是美食节？写两句寄来。",
  "루카 이후에는 어디로 가요: 문화 포럼, 영화, 음식 축제? 두 문장을 써서 보내 주세요.", 2)
A("ESERCIZI · 第 5 版练习", "ESERCIZI · 제 5 면 연습")
A("读第 5 版文章，选出正确答案。", "5면 기사를 읽고 알맞은 답을 고르세요.")
A("卢卡漫画节是第 60 届", "루카 코믹스는 60회째예요")
A("文化论坛 11 月 3 日开幕", "문화 포럼은 11월 3일에 열려요")
A("卢卡漫画节主题是 Legacy", "루카 코믹스 주제는 Legacy예요")
A("armadio = 衣柜", "armadio = 옷장")
A("gratuiti = 免费的（阳性复数）", "gratuiti = 무료인 (남성 복수)")
A("documentario = 纪录片", "documentario = 다큐멘터리")
A("schermo = 银幕", "schermo = 스크린")
A("castagne arrosto 烤栗子（复数）", "castagne arrosto = 군밤 (복수)")
A("cosplay = 角色扮演服装", "cosplay = 코스프레 의상")
A("andare 将来时 noi：andremo", "andare의 미래형 noi: andremo")
A("esserci 将来时：ci sarà（将有）", "esserci의 미래형: ci sarà (있을 거예요)")
A("guardare 将来时 noi：guarderemo", "guardare의 미래형 noi: guarderemo")
A("durare 将来时：durerà", "durare의 미래형: durerà")
A("卢卡漫画节到 11 月 8 日才结束是错的", "루카 코믹스가 11월 8일에 끝난다는 말은 틀렸어요")

# ---------- P6 ----------
A("APPROFONDIMENTO · 深读", "APPROFONDIMENTO · 심층")
A("LIVELLO B2 · Leggere le previsioni · 怎样读天气预报",
  "LIVELLO B2 · Leggere le previsioni · 일기예보 읽는 법")
A("发稿时 10 月 28 日表决结果尚未确认：本期只写预期日期、争议点和 DPB 数字，不写结果。",
  "인쇄할 때 10월 28일 표결 결과는 아직 확인되지 않았어요: 예상 날짜, 쟁점, DPB 숫자만 쓰고 결과는 없어요.")
A("la probabilità 概率 · la media 平均值 · il modello 模型/预报模式 · il bollettino 公报/预报 · aggiornare 更新。",
  "la probabilità 확률 · la media 평균값 · il modello 모형/예보 모형 · il bollettino 공보/예보 · aggiornare 업데이트예요.")
A("LE MINIME DI ESEMPIO · 练习用示例最低温 (DATI INVENTATI PER L'ESERCIZIO)",
  "LE MINIME DI ESEMPIO · 연습용 예시 최저 기온 (DATI INVENTATI PER L'ESERCIZIO)")
A("PROBABILITÀ · 概率", "PROBABILITÀ · 확률")
A("ESERCIZI · 第 6 版练习", "ESERCIZI · 제 6 면 연습")
A("看上面的练习图表，选出正确答案。", "위의 연습 도표를 보고 알맞은 답을 고르세요.")
A("示例数据中最冷的是都灵 3°", "예시 자료에서 가장 추운 곳은 토리노 3°예요")
A("示例数据中最暖的是那不勒斯 12°", "예시 자료에서 가장 따뜻한 곳은 나폴리 12°예요")
A("图表数据是练习用的、不是真实预报", "도표 자료는 연습용이지 실제 예보가 아니에요")
A("预报基于 ECMWF 等模型", "예보는 ECMWF 같은 모형을 바탕으로 해요")
A("预报会变，因为大气变化快", "예보는 대기가 빨리 변해서 바뀌어요")
A("DPB 于 10 月 15 日送布鲁塞尔", "DPB는 10월 15일에 브뤼셀로 보냈어요")
A("2027 增长预测 +0,8%", "2027년 성장 전망은 +0,8%예요")
A("bisogna che + 虚拟式 controllino", "bisogna che + 접속법 controllino")
A("è importante che + 虚拟式 sia", "è importante che + 접속법 sia")
A("用方框里的词填空：probabilità · media · bollettino · modello",
  "상자 안의 단어로 빈칸을 채우세요: probabilità · media · bollettino · modello")
A("probabilità = 概率", "probabilità = 확률")
A("media = 平均值", "media = 평균값")
A("bollettino = 预报公报", "bollettino = 예보 공보")
A("modello = 预报模型", "modello = 예보 모형")

# ---------- P7 (long strings before their substrings) ----------
A("LINGUA · 语言", "LINGUA · 언어")
A("聚焦语言 · Tre livelli, tre strumenti · 三个级别，三件工具",
  "언어 집중 · Tre livelli, tre strumenti · 세 단계, 세 가지 도구")
A("天气用无人称动词（第三人称单数）；“我冷”说 ho freddo，“外面冷”说 fa freddo。",
  "날씨는 무인칭 동사 (3인칭 단수)를 써요. '나는 추워요'는 ho freddo, '밖이 추워요'는 fa freddo예요.")
A("讲过去用近过去时：arrivare/andare 等用 essere，分词配合性数；avere 的分词不变。",
  "과거 이야기는 근과거를 써요: arrivare, andare 같은 동사는 essere를 쓰고 분사는 성과 수에 맞춰요. avere의 분사는 변하지 않아요.")
A("è probabile che / è possibile che / bisogna che 后用虚拟式；so che、scrivono che 后用陈述式。",
  "è probabile che, è possibile che, bisogna che 뒤에는 접속법을 써요. so che, scrivono che 뒤에는 직설법을 써요.")
A("ERRORI TIPICI · 常见错误", "ERRORI TIPICI · 자주 하는 실수")
A("fa 后面的 freddo 永远不变。", "fa 뒤의 freddo는 변하지 않아요.")
A("nevicare 只用第三人称单数。", "nevicare는 3인칭 단수만 써요.")
A("预报给的是概率，不是确定性。", "예보는 확률이지, 확실한 게 아니에요.")
A("gente 是单数，动词形容词用单数阴性。", "gente는 단수예요. 동사와 형용사는 단수 여성형으로 써요.")
A("LA PAROLA · 本周生词", "LA PAROLA · 이번 주 단어")
A("assaggio = 品尝。本周见第 3 版：潘妮托尼决赛上观众可以免费品尝。",
  "assaggio = 맛보기예요. 이번 주 3면에서 만나요: 파네토네 결승에서 관객이 무료로 맛볼 수 있어요.", 2)
A("这是编辑部示例信，非真实来信。来信请寄编辑部，VOL.3 刊登真实来信与第 8 版最佳作文！",
  "이 편지는 편집부 예시예요. 실제 독자 편지가 아니에요. 8면 우수 작문도 아직 없어요. 예시와 약속은 VOL.3으로 이어져요. 여러분의 편지를 보내 주세요! VOL.3에 실제 편지와 8면 우수 작문을 실어요!", 2)
A("FRASI DELLA SETTIMANA · 本周金句（逐字摘自本期文章）",
  "FRASI DELLA SETTIMANA · 이번 주 문장 (이번 호 기사에서 그대로)")
A("第一场真正的寒冷到来了。", "첫 진짜 추위가 찾아왔어요.")
A("这不是确定性，而是概率。", "이건 확실한 게 아니라 확률이에요.")
A("天冷，穿暖和点！", "추우니 따뜻하게 입어요!")
A("足球不会因为第一场寒冷而停下。", "축구는 첫 추위 때문에 멈추지 않아요.")
A("文化继续。", "문화는 계속돼요.")
A("高概率不等于确定性。", "높은 확률이 확실한 것은 아니에요.")
A("LA PROSSIMA SETTIMANA · 下期预告 (VOL.3)", "LA PROSSIMA SETTIMANA · 다음 호 예고 (VOL.3)")
A("piovere 天气动词：piove", "piovere 날씨 동사: piove")
A("fa freddo = 天气冷", "fa freddo = 날씨가 추워요")
A("“我冷”说 ho freddo", "'나는 추워요'는 ho freddo예요")
A("assaggiare 用 avere", "assaggiare는 avere를 써요")
A("aprire 用 avere + 不变分词", "aprire는 avere + 변하지 않는 분사를 써요")
A("bisogna che + 虚拟式 sia", "bisogna che + 접속법 sia")
A("so che + 陈述式 arriva", "so che + 직설법 arriva")

# ---------- P8 (shared strings already replaced above keep their counts) ----------
A("VALUTAZIONE E RISPOSTE · 练习与答案", "VALUTAZIONE E RISPOSTE · 연습과 정답")
A("第 8 版 · La grande prova della settimana + tutte le risposte",
  "제 8 면 · La grande prova della settimana + tutte le risposte")
A("primo freddo = 第一场寒冷", "primo freddo = 첫 추위")
A("追思日在 11 月 2 日", "추모의 날은 11월 2일이에요")
A("文化论坛在米兰开幕", "문화 포럼은 밀라노에서 열려요")
A("潘妮托尼决赛在周六日", "파네토네 결승은 토요일과 일요일이에요")
A("牛轧糖节在克雷莫纳", "토로네 축제는 크레모나에서 열려요")
A("意甲第 11 轮周日收官：chiude", "세리에 A 11라운드는 일요일에 끝나요: chiude")
A("佛罗伦萨对尤文图斯在周日晚上", "피오렌티나–유벤투스는 일요일 저녁에 열려요")
A("DPB 于 10 月 15 日送出", "DPB는 10월 15일에 보냈어요")
A("卢卡漫画节 11 月 1 日闭幕", "루카 코믹스는 11월 1일에 막을 내렸어요")
A("Giulia 去米兰潘妮托尼决赛", "Giulia는 밀라노 파네토네 결승에 가요")
A("Paolo 周六去牛轧糖节", "Paolo는 토요일에 토로네 축제에 가요")
A("传统潘妮托尼是 Giulia 品尝的", "전통 파네토네는 Giulia가 맛본 거예요")
A("标题概括两个城市、两个节日", "제목이 두 도시와 두 축제를 요약해요")
A("时间词在前", "시간 표현이 앞에 와요")
A("疑问词组在句首", "의문사구가 문장 앞에 와요")
A("主语 + 动词 + 时间", "주어 + 동사 + 시간 순이에요")
A("周一第一场寒冷来了。", "월요일에 첫 추위가 찾아왔어요.")
A("对照原文", "원문과 비교하세요")
A("assaggiare gratis = 免费品尝", "assaggiare gratis = 무료로 맛보기")
A("周日晚上，佛罗伦萨对尤文图斯。", "일요일 저녁, 피오렌티나–유벤투스 경기가 있어요.")
A("si gioca = 进行比赛", "si gioca = 경기가 열려요")
A("dovere = 必须", "dovere = 해야 해요")
A("每个预报都必须清楚。→ ___", "모든 예보는 분명해야 해요. → ___")
A("probabilità=可能性 d", "probabilità=가능성 d")
A("media=平均值 a", "media=평균값 a")
A("bollettino=预报公报 b", "bollettino=예보 공보 b")
A("modello=预报模型 c", "modello=예보 모형 c")
A("mandorle 杏仁", "mandorle 아몬드")
A("quanto costa? 多少钱", "quanto costa? = 얼마예요?")
A("pagare con carta 刷卡", "pagare con carta = 카드로 결제하기")
A("牛轧糖节持续到 11 月 22 日", "토로네 축제는 11월 22일까지 이어져요")
A("写作题（无唯一答案）；范文（{NWORDS} 词）见下。",
  "쓰기 문제예요 (정답이 하나만 있는 문제는 아니에요). 모범 답안 ({NWORDS}단어)은 아래에 있어요.")
A("（开放题，范文如下）", "(열린 문제예요. 모범 답안은 아래에 있어요)")
A("范文见本版 H 区（{NWORDS} 词）", "모범 답안은 이 면 H 구역에 있어요 ({NWORDS}단어)")
A("RISPOSTE · 参考答案 — 按版面分页排列，找到题号即可",
  "RISPOSTE · 정답 — 면별로 정리했어요. 번호를 찾으면 돼요")
A("每题附一句中文简析 · 带 ✓ 的为范文题",
  "문제마다 짧은 해설이 있어요 · ✓ 표시는 모범 답안 문제예요")
A("— PAGINA {pg} —", "— 제 {pg} 면 —")

# ---------- shared furniture (counts across files) ----------
A("答案见第 8 版 · 题目可跨级混排，按题号找答案",
  "정답은 8면 · 문제는 레벨이 섞여 있을 수 있어요", 5)
A("E TU? · 说说你自己", "E TU? · 내 이야기", 4)
A("把词和释义配对", "단어와 뜻 짝짓기", 3)
A("意甲第 11 轮周日收官", "세리에 A 11라운드는 일요일에 끝나요", 3)
A("民俗电影节在佛罗伦萨", "민속 영화제는 피렌체에서 열려요", 3)
A("文化论坛有 50 多场活动", "문화 포럼에는 50개가 넘는 행사가 있어요", 3)
A("潘妮托尼决赛有 19 国糕点师", "파네토네 결승에는 19개국 제빵사가 참가해요", 2)
A("阿尔巴松露节到 12 月 6 日", "알바 트러플 축제는 12월 6일에 끝나요", 2)
A("torrone = 牛轧糖", "torrone = 토로네", 2)
A("arrivare 用 essere：è arrivato", "arrivare는 essere를 써요: è arrivato", 2)
A("andare 用 essere，复数 sono andati", "andare는 essere를 써요. 복수 sono andati", 2)
A("主语 + essere + 地点 + 日期", "주어 + essere + 장소 + 날짜", 2)
A("è probabile che + 虚拟式 piova", "è probabile che + 접속법 piova", 2)
A("è possibile che + 虚拟式 nevichi", "è possibile che + 접속법 nevichi", 2)
A("观众可以免费品尝。", "관객이 무료로 맛볼 수 있어요.", 2)
A("高概率不等于确定", "높은 확률이 확실한 것은 아니에요")
A("概率不等于确定", "확률은 확실한 것과 달라요")
A("assaggio = 品尝", "assaggio = 맛보기")

# ---------- full-width-punctuation-only notes (family half-width form) ----------
A("mettere：io → metto", "mettere: io → metto")
A("portare：loro → portano", "portare: loro → portano")
A("guardare：loro → guardano", "guardare: loro → guardano")
A("restare：la scuola → resta（lei）", "restare: la scuola → resta (lei)")
A("vincere：ha vinto", "vincere: ha vinto")
A("pareggiare：ha pareggiato", "pareggiare: ha pareggiato")
A("nevicare：nevica", "nevicare: nevica")

# ---------- long bridge variants before the short box-bridge (substring order) ----------
A("用方框里的词填空。注意：有的词要变成复数。",
  "상자 안의 단어로 빈칸을 채우세요. 주의: 복수형으로 바꿔야 하는 단어도 있어요.")
A("用方框里的词填空。", "상자 안의 단어로 빈칸을 채우세요。")
A("用将来时（futuro semplice）补全。", "단순 미래 (futuro semplice)로 완성하세요。")

# ---------- globals LAST (type + instruction tokens) ----------
A("完形单选", "빈칸 채우기", 13)
A("完成句子", "문장 완성", 61)
A("词汇配对", "단어 짝짓기", 3)
A("句型转换", "문장 전환", 1)
A("判断对错", "읽기 판단", 3)
A("单选", "객관식", 48)
A("翻译", "번역", 8)
A("造句", "문장 만들기", 14)
A("填空", "빈칸 채우기", 56)
A("判断", "판단", 3)
A("写作", "쓰기", 3)


# ---------- FIX ROUND 1 (R0 audit findings; applied after the base phase) ----------
# R0: occlusion 4 NEW flags (P1 cifre title overflow + overlap, P2 frase
# title +1px over border, P7 FRASI rule through the letter box) and one
# Korean >=3-syllable tail split (P6 bridge). All fixes are wording-only
# and live here, not only in the content files.
R1 = [
    ("LA SETTIMANA IN CIFRE · 숫자로 보는 이번 주",
     "LA SETTIMANA IN CIFRE · 이번 주 숫자", 1),
    ("LA FRASE PER RICORDARE · 암기 문장",
     "LA FRASE PER RICORDARE · 암기문장", 1),
    ("assaggio = 맛보기예요. 이번 주 3면에서 만나요: 파네토네 결승에서 관객이 무료로 맛볼 수 있어요.",
     "assaggio = 맛보기예요. 3면 파네토네 결승에서 무료로 맛봐요.", 2),
    ("gente는 단수예요. 동사와 형용사는 단수 여성형으로 써요.",
     "gente는 단수예요. 단수 여성형으로 써요.", 1),
    ("이 편지는 편집부 예시예요. 실제 독자 편지가 아니에요. 8면 우수 작문도 아직 없어요. 예시와 약속은 VOL.3으로 이어져요. 여러분의 편지를 보내 주세요! VOL.3에 실제 편지와 8면 우수 작문을 실어요!",
     "편집부 예시예요. 실제 편지도 8면 우수 작문도 아직 없어요. 편지를 보내 주세요! VOL.3에 실어요!", 2),
    ("인쇄할 때 10월 28일 표결 결과는 아직 확인되지 않았어요: 예상 날짜, 쟁점, DPB 숫자만 쓰고 결과는 없어요.",
     "인쇄할 때 10월 28일 표결 결과는 아직 확인 안 됐어요: 예상 날짜, 쟁점, DPB 숫자만 쓰고 결과는 없어요.", 1),
]


# ---------- FIX ROUND 2 (R1 audit: 1 flag left) ----------
# P1 cifre box title still crossed its box border by 1.8px after round 1
# (ink 962.8 > border 961.0); drop one more word from the Korean suffix.
R2 = [
    ("LA SETTIMANA IN CIFRE · 이번 주 숫자",
     "LA SETTIMANA IN CIFRE · 이번 주", 1),
]


def main():
    texts = {}
    for f in FILES:
        with open(os.path.join(BASE, f), encoding="utf-8") as fh:
            texts[f] = fh.read()
    # Base phase: skipped when already applied (re-runs after fix rounds).
    base_marker = R[0][0]
    base_present = sum(t.count(base_marker) for t in texts.values()) > 0
    if base_present:
        for old, new, n in R:
            total = sum(t.count(old) for t in texts.values())
            if total != n:
                print(f"COUNT MISMATCH: expected {n}, found {total}: {old[:70]!r}")
                print("ABORT - nothing written (simulation only)")
                return 1
            for f in texts:
                texts[f] = texts[f].replace(old, new)
        print(f"base OK: {len(R)} counted replacements")
    else:
        print("base already applied, skipped")
    # Fix-round-1 phase: idempotent per pair (skip when already applied).
    applied = 0
    for old, new, n in R1:
        total = sum(t.count(old) for t in texts.values())
        if total == 0 and sum(t.count(new) for t in texts.values()) >= n:
            print(f"fix1 skip (already applied): {old[:50]!r}")
            continue
        if total != n:
            print(f"FIX1 COUNT MISMATCH: expected {n}, found {total}: {old[:70]!r}")
            print("ABORT - nothing written (simulation only)")
            return 1
        for f in texts:
            texts[f] = texts[f].replace(old, new)
        applied += 1
    print(f"fix1 OK: {applied} pairs applied, {len(R1) - applied} skipped")
    # Fix-round-2 phase (same idempotent pattern).
    applied2 = 0
    for old, new, n in R2:
        total = sum(t.count(old) for t in texts.values())
        if total == 0 and sum(t.count(new) for t in texts.values()) >= n:
            print(f"fix2 skip (already applied): {old[:50]!r}")
            continue
        if total != n:
            print(f"FIX2 COUNT MISMATCH: expected {n}, found {total}: {old[:70]!r}")
            print("ABORT - nothing written (simulation only)")
            return 1
        for f in texts:
            texts[f] = texts[f].replace(old, new)
        applied2 += 1
    print(f"fix2 OK: {applied2} pairs applied, {len(R2) - applied2} skipped")
    for f, t in texts.items():
        with open(os.path.join(BASE, f), "w", encoding="utf-8") as fh:
            fh.write(t)
    print(f"transform OK: base {len(R)} + fix1 {len(R1)} + fix2 {len(R2)} pairs, {len(FILES)} files")
    # post-conditions: no Han chars and no full-width CJK punctuation left
    # in the operative files (transform.py itself is excluded: it carries
    # the old-side search strings by design).
    for f in FILES:
        t = open(os.path.join(BASE, f), encoding="utf-8").read()
        han = sum(1 for ch in t if "\u4e00" <= ch <= "\u9fff")
        fw = sum(1 for ch in t if ch in "：（）")
        print(f"  {f}: Han={han} fullwidth-punct={fw}")
        assert han == 0 and fw == 0, f
    return 0


if __name__ == "__main__":
    sys.exit(main())
