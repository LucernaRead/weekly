# -*- coding: utf-8 -*-
"""One-off fan-out transform: W45 NL core (Chinese explanations) -> NL x KO.
Line-literal / string-literal replacements only, each asserted.
Applied to a fresh copy of the core build dir; re-running on an already
transformed copy aborts (olds no longer found). Longest-first order so
short substrings (单选, 填空, 判断, 造句, 翻译, 写作, 气候周) never eat
longer sentences that contain them.
Dutch target text, keys (except re-aimed E137/E138), facts, images: untouched.
P7 word-box definition sentence stays Dutch verbatim; only its gloss is Korean.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
FILES = ["bslib4.py", "content12.py", "content34.py", "content56.py",
         "content7.py", "content8.py"]

M = {}
def m(old, new):
    assert old not in M, old
    M[old] = new

# ---------- gloss boxes ----------
m("de meteoroloog 气象学家 · waarschuwingsmoeheid 预警疲劳 · vastzetten 固定好 · het advies 建议、忠告 · de voorstander 支持者。",
  "de meteoroloog 기상학자 · waarschuwingsmoeheid 경보 피로 · vastzetten 고정하기 · het advies 조언 · de voorstander 찬성론자.")
m("het klimaat 气候 · wortelen 生根 · besparen 节约 · de verwarming 暖气 · de waarschuwing 预警 · lokaal 当地的、本地的。",
  "het klimaat 기후(날씨) · wortelen 뿌리내리다 · besparen 절약하다 · de verwarming 난방 · de waarschuwing 경보 · lokaal 현지의.")
m("het museum 博物馆 · de rondleiding 导览 · het tijdslot 时间段 · tweedehands 二手的 · de beurs 展会、集市。",
  "het museum 박물관 · de rondleiding 안내 투어 · het tijdslot 시간대 · tweedehands 중고의 · de beurs 박람회.")
m("de balans 成绩单、总结 · gelijkspelen 打平 · de speelronde 轮次 · de topper 焦点战 · de stand 积分榜。",
  "de balans 결산 · gelijkspelen 비기다 · de speelronde 라운드 · de topper 빅매치 · de stand 순위표.")
m("het eiland 岛 · de proef 比赛项目、考验 · stemmen 投票 · de aflevering （一）集 · voorbij 过去了、结束了。",
  "het eiland 섬 · de proef 미션 · stemmen 투표하다 · de aflevering (한) 회 · voorbij 끝나다.")
m("meedoen 参加：ik doe mee；opruimen 收拾：wij hebben opgeruimd；vastzetten 固定：zij zette vast。",
  "meedoen 참여하다: ik doe mee; opruimen 치우다: wij hebben de tuin opgeruimd; vastzetten 고정하다: zij zette vast.")
m("讲解｜de Klimaatweek 气候周 · de boom planten 种树 · besparen 节约 · de waarschuwing 警告、预警。",
  "해설 — de Klimaatweek 기후 주간 · de boom planten 나무 심기 · besparen 절약하기 · de waarschuwing 경고.")
m("het klimaat 气候（长期）；een boom planten 种树；besparen 节约；de waarschuwing 预警。",
  "het klimaat 기후(장기적인); een boom planten 나무 심기; besparen 절약하기; de waarschuwing 경보.")
m("Ik vind dat… 我认为；Volgens mij… 依我看；Het lijkt me dat… 在我看来。",
  "Ik vind dat… 저는 ~라고 생각해요; Volgens mij… 제 생각에는; Het lijkt me dat… ~인 것 같아요.")
m("meedoen = 参加、参与：气候周全荷兰都参加。",
  "meedoen = 참여하다: 기후 주간에는 모두가 참여해요.")

# ---------- furniture / bands / heads ----------
m("荷 兰 语 周 报 · VOL.2 · KLIMAATWEEK · MUSEUMNACHT · SPEELRONDE 12",
  "네덜란드어 주간지 · VOL.2 · 기후 주간 · 박물관의 밤 · 12라운드")
m("ELKE WEEK IN HET NEDERLANDS · 每周一期 · 读荷兰人正在读的荷兰语",
  "ELKE WEEK IN HET NEDERLANDS · 매주 발행 · 네덜란드인이 읽는 네덜란드어")
m("De Lucerna · 荷兰语周报 VOL.2 · LUCERNA DUTCH WEEKLY",
  "De Lucerna · 네덜란드어 주간지 VOL.2 · 텍스트는 네덜란드어 · 해설은 한국어")
m("第 {n} 版 / 共 {total} 版", "제 {n} 면 / 총 {total} 면")
m("译注｜", "해설 — ")
m("NIVEAU B1 · Robinson is begonnen, ADE en DDW voorbij · 荒岛节目开播、音乐节与设计周落幕",
  "NIVEAU B1 · Robinson is begonnen, ADE en DDW voorbij · 로빈슨 시작, ADE와 DDW 폐막")
m("NIVEAU A2 → B1 · Museumnacht, boeken en kunst · 博物馆之夜、书籍与艺术",
  "NIVEAU A2 → B1 · Museumnacht, boeken en kunst · 박물관의 밤, 책과 예술")
m("NIVEAU B1 · Europese week en speelronde 12 · 欧战周与第 12 轮",
  "NIVEAU B1 · Europese week en speelronde 12 · 유럽 대회 주간과 12라운드")
m("NIVEAU A2 · De Klimaatweek, stap voor stap · 一步一步讲气候周",
  "NIVEAU A2 · De Klimaatweek, stap voor stap · 기후 주간, 단계별로")
m("聚焦语言 · Drie niveaus, drie gereedschappen · 三个级别，三件工具",
  "언어에 집중 · Drie niveaus, drie gereedschappen · 세 단계, 세 가지 도구")
m("第 8 版 · De grote toets van de week + alle antwoorden",
  "8면 · De grote toets van de week + alle antwoorden")
m("NIVEAU B2 · De codes van het KNMI · 气象预警深度解读",
  "NIVEAU B2 · De codes van het KNMI · KNMI 경보 코드 심층 해설")
m("ANTWOORDEN · 参考答案 — 按版面分页排列，找到题号即可",
  "ANTWOORDEN · 정답 — 면별로 정리했어요, 번호로 찾으세요")
m("每题附一句中文简析 · 带 ✓ 的为范文题",
  "문제마다 짧은 해설이 있어요 · ✓ 표시는 모범 답안 문제예요")
m("TOETS EN ANTWOORDEN · 练习与答案", "TOETS EN ANTWOORDEN · 시험과 정답")
m("DE WEEK IN CIJFERS · 数字看本周", "DE WEEK IN CIJFERS · 숫자로 보기")
m("Agenda van de week · 本周大事", "Agenda van de week · 이번 주 일정")
m("答案见第 8 版 · 题目可跨级混排，按题号找答案",
  "정답은 8면 · 문제는 수준이 섞여 있어요, 번호로 찾으세요")
m("DE CODES VAN HET KNMI · 气象预警颜色", "DE CODES VAN HET KNMI · KNMI 경보 색깔")
m("Wat betekent elke kleur? · 每种颜色是什么意思", "Wat betekent elke kleur? · 각 색깔은 무슨 뜻일까요")
m("ZINNEN VAN DE WEEK · 本周金句（逐字摘自本期文章）", "ZINNEN VAN DE WEEK · 이번 주 금문장(본문에서 그대로 가져왔어요)")
m("VOLGENDE WEEK · 下期预告 (VOL.3)", "VOLGENDE WEEK · 다음 호 예고 (VOL.3)")
m("HET WOORD · 本周生词", "HET WOORD · 이번 주 단어")
m("PAS OP! · 易错诊所", "PAS OP! · 실수 클리닉")
m("DE GRAFIEK · 图表（练习数据）", "DE GRAFIEK · 그래프(연습용 데이터)")
m("VOOR OF TEGEN? · 正方还是反方", "VOOR OF TEGEN? · 찬반 토론")
m("ZO ONTHOUD JE HET · 口诀", "ZO ONTHOUD JE HET · 외우는 방법")
m("IN DEZE EDITIE · 本期目录", "IN DEZE EDITIE · 이번 호 안내")
m("BLIKSEMQUIZ · 闪电问答", "BLIKSEMQUIZ · 번개 퀴즈")
m("IN HET KORT · 快讯", "IN HET KORT · 간단 소식")
m("NU JIJ · 即学即练", "NU JIJ · 직접 해 보기")
m("HET NIEUWS · 头条", "HET NIEUWS · 헤드라인")
m("LEVEN · 生活", "LEVEN · 생활")
m("CULTUUR · 文化", "CULTUUR · 문화")
m("SPORT · 体育", "SPORT · 스포츠")
m("JONGEREN · 青年", "JONGEREN · 청소년")
m("VERDIEPING · 深读", "VERDIEPING · 심층")
m("TAAL · 语言", "TAAL · 언어")
m("EN JIJ? · 说说你自己", "EN JIJ? · 여러분은요")
m("· 本周日程", "· 이번 주 일정")
m("OEFENINGEN · 第 2 版练习", "OEFENINGEN · 2면 연습")
m("OEFENINGEN · 第 3 版练习", "OEFENINGEN · 3면 연습")
m("OEFENINGEN · 第 4 版练习", "OEFENINGEN · 4면 연습")
m("OEFENINGEN · 第 5 版练习", "OEFENINGEN · 5면 연습")
m("OEFENINGEN · 第 6 版练习", "OEFENINGEN · 6면 연습")

# ---------- P1 ----------
m("200 — de bomen en struiken die Coevorden zaterdag uitdeelt（周六科弗登发放的树木和灌木）",
  "200 — de bomen en struiken die Coevorden zaterdag uitdeelt(토요일에 주는 나무와 관목)")
m("9 — de wedstrijden van speelronde 12 in de Eredivisie（荷甲第 12 轮的比赛场数）",
  "9 — de wedstrijden van speelronde 12 in de Eredivisie(에레디비시 12라운드 경기 수)")
m("70+ — de musea die open zijn op Museumnacht（博物馆之夜开放的博物馆，70 多家）",
  "70+ — de musea die open zijn op Museumnacht(박물관의 밤에 문을 여는 박물관, 70곳 이상)")
m("7 — de dagen van de Klimaatweek（气候周的天数）", "7 — de dagen van de Klimaatweek(기후 주간의 일수)")
m("本周全国气候周 · 详见第 2 版", "온 나라가 함께하는 기후 주간 · 2면 참조")
m("本周日程见第 2–4 版文章", "일정은 2–4면 기사 참조")
m("读头版，选出正确答案 · 答案见第 8 版", "1면을 읽고 정답을 고르세요 · 정답은 8면")
m("“气候”：我们周围长期的天气与自然。气候周讲的就是我们的气候。",
  "«기후»: 우리 주변의 장기적인 날씨와 자연이에요. 기후 주간은 우리의 기후에 관한 주간이에요.")
m("气候周你做什么？种树、节约能源还是骑车。写两句荷兰语寄给编辑部。",
  "기후 주간에 여러분은 무엇을 할 거예요? 나무 심기, 에너지 절약, 자전거 타기. 네덜란드어 문장 두 개를 써서 편집부에 보내세요.")
m("气候周共 7 天（11 月 2–8 日）", "기후 주간은 모두 7일이에요(11월 2-8일)")
m("气候周 11 月 2–8 日共 7 天", "기후 주간 11월 2-8일은 모두 7일이에요")
m("气候周 11 月 2–8 日", "기후 주간 11월 2-8일")
m("气候周 11 月 8 日周日结束", "기후 주간은 11월 8일 일요일에 끝나요")
m("气候周到 11 月 8 日", "기후 주간은 11월 8일까지예요")
m("气候周 11 月 2 日周一开始", "기후 주간은 11월 2일 월요일에 시작해요")
m("气候周持续七天。", "기후 주간은 7일 동안 이어져요.")
m("气候周不做：更多开车", "기후 주간에 하지 않는 일: 자동차 더 타기")
m("气候周他每天骑车上学", "기후 주간에 그는 매일 자전거로 학교에 가요")
m("科弗登发放 200 棵树木灌木", "쿠포르던에서 나무와 관목 200그루를 나눠 줘요")
m("博物馆之夜在 11 月 7 日周六", "박물관의 밤은 11월 7일 토요일이에요")
m("博物馆之夜在阿姆斯特丹", "박물관의 밤은 암스테르담에서 열려요")
m("博物馆之夜在 11 月 7 日", "박물관의 밤은 11월 7일이에요")
m("博物馆之夜从晚上 19 点到凌晨 2 点。→ ___", "박물관의 밤은 저녁 7시부터 새벽 2시까지예요. → ___")
m("博物馆开放到凌晨 2 点", "박물관은 새벽 2시까지 문을 열어요")
m("特温特–阿贾克斯 13:30 开球", "트벤테-아약스 경기는 13:30에 시작해요")
m("海伦芬–费耶诺德 11:15 开球", "헤이렌베인-페예노르트 경기는 11:15에 시작해요")
m("发放地点在兹韦洛", "나눠 주는 곳은 즈벨로예요")
m("发放从 13:00 开始", "나눠 주기는 13:00부터 시작해요")
m("发放到 16:00 结束", "나눠 주기는 16:00에 끝나요")
m("红色预警：非常危险，待在室内", "빨간색 경보: 매우 위험해요, 실내에 머무르세요")
m("预警针对本地，不针对整个省", "경보는 지역 단위예요, 한 주 전체가 아니에요")
m("预警针对你所在的地区", "경보는 여러분이 사는 지역을 대상으로 해요")
m("天气可能危险，要当心", "날씨가 위험할 수 있으니 조심하세요")
m("危险，做好准备", "위험해요, 대비하세요")
m("非常危险，尽量待在室内", "매우 위험해요, 되도록 실내에 머무르세요")
m("节约能源：暖气调低一度", "에너지 절약: 난방을 1도 낮추기")
m("用第 2 版的词填空。", "2면 단어로 채우세요.")
m("用颜色代码和日期填空。", "색깔 코드와 날짜로 채우세요.")
m("读第 2 版文章，选出正确答案。", "2면 기사를 읽고 정답을 고르세요.")
m("读第 3 版文章，选出正确答案。", "3면 기사를 읽고 정답을 고르세요.")
m("读第 4 版文章，选出正确答案。", "4면 기사를 읽고 정답을 고르세요.")
m("读第 5 版文章，选出正确答案。", "5면 기사를 읽고 정답을 고르세요.")
m("读第 6 版文章，选出正确答案。", "6면 기사를 읽고 정답을 고르세요.")
m("用方框里的词填空。注意：有的词要变成复数。", "네모 안의 단어로 채우세요(복수형 주의).")
m("用方框里的词填空。注意动词形式。", "네모 안의 단어로 채우세요.")
m("用方框里的词填空。", "네모 안의 단어로 채우세요.")
m("用现在完成时补全，注意助动词 hebben/zijn。", "현재완료로 채우세요(조동사 hebben/zijn).")
m("用过去时或完成时补全。", "과거형이나 현재완료로 채우세요.")
m("用 gaan + 不定式说将来。", "gaan + 부정사로 미래를 말하세요.")
m("把词组成正确的句子。", "단어를 모아 올바른 문장을 만드세요.")
m("把词和释义配对", "단어와 뜻 짝짓기")
m("算一算：用第 3 版的数字回答。", "계산해 보세요: 3면 숫자로 답하세요.")
m("看第 6 版图表（练习数据）回答。", "6면 그래프(연습용 데이터)를 보고 답하세요.")
m("练习数据：虚构数字，仅供练习，非真实调查。问题：橙色预警时你会怎么做？（100 名年轻人）",
  "연습용 데이터예요: 가상의 숫자라서 실제 설문 조사가 아니에요. 질문: 주황색 경보 때 어떻게 할 거예요? (젊은이 100명)")
m("图表共 100 人：45+25+20+10", "그래프 전체 100명: 45+25+20+10")
m("45 名年轻人选择待在家里", "45명의 젊은이가 집에 머무르기로 했어요")
m("25 人先看预警文字", "25명은 먼저 경보 글을 읽어 봐요")
m("10 人不知道", "10명은 모르겠다고 했어요")
m("以前预警针对整个省", "예전에는 경보가 한 주 전체를 대상으로 했어요")
m("如今预警是本地的", "요즘 경보는 지역 단위예요")
m("红色：非常危险，非必要不上路", "빨간색: 매우 위험해요, 꼭 필요하지 않으면 외출하지 마세요")
m("预警疲劳：警告太多导致不再注意", "경보 피로: 경보가 너무 많아서 주의를 덜 기울이게 돼요")
m("KNMI 说：看代码旁边的文字", "KNMI는 코드 옆의 글자를 보라고 해요")
m("你看《荒岛远征》吗，还是更爱自己出门活动？写两句荷兰语寄来。",
  "로빈슨을 보세요, 아니면 직접 밖에 나가서 활동하는 쪽이 더 좋아요? 네덜란드어 문장 두 개를 써서 보내 주세요.")

# ---------- P3/P4 notes ----------
m("Crossing Border 在海牙", "크로싱 보더는 헤이그에 있어요")
m("Crossing Border 结合书籍与音乐", "크로싱 보더는 책과 음악을 결합해요")
m("PAN 艺术博览会到 11 月 8 日", "PAN 아트페어는 11월 8일까지예요")
m("PAN 在 RAI 展览中心", "PAN은 RAI 전시장에 있어요")
m("19:00 到 02:00 共 7 小时", "19:00부터 02:00까지 모두 7시간이에요")
m("11 月 1–8 日共 8 天", "11월 1-8일은 모두 8일이에요")
m("11 月 3–8 日共 6 天", "11월 3-8일은 모두 6일이에요")
m("250 的一半是 125", "250의 절반은 125예요")
m("museum 复数：musea", "museum 복수형: musea")
m("rondleiding = 导览", "rondleiding = 안내 투어")
m("tijdslot = 时间段", "tijdslot = 시간대")
m("tweedehands = 二手的", "tweedehands = 중고의")
m("beurs = 展会、集市", "beurs = 박람회")
m("zijn 的 perfectum：zijn geweest", "zijn의 perfectum: zijn geweest")
m("kopen 的 perfectum：hebben gekocht", "kopen의 perfectum: hebben gekocht")
m("voorlezen 的 perfectum：hebben voorgelezen", "voorlezen의 perfectum: hebben voorgelezen")
m("komen 用 zijn：zijn gekomen", "komen은 zijn과 함께 써요: zijn gekomen")
m("komen 的 perfectum 用 zijn", "komen의 perfectum은 zijn을 써요")
m("阿贾克斯 2–0 赢亚特兰大", "아약스가 아탈란타를 2-0으로 이겼어요")
m("特温特 4–1 赢林肯红魔", "트벤테가 링컨 레드임프스를 4-1로 이겼어요")
m("NEC 2–4 输给萨格勒布迪纳摩", "NEC는 디나모 자그레브에 2-4로 졌어요")
m("皇家贝蒂斯 1–0 赢费耶诺德", "레알 베티스가 페예노르트를 1-0으로 이겼어요")
m("10 轮后费耶诺德 24 分领跑", "10라운드 뒤 페예노르트가 24점으로 선두예요")
m("对：10 轮后费耶诺德 24 分第一", "맞아요: 10라운드 뒤 페예노르트가 24점으로 1위예요")
m("10 轮后阿贾克斯 21 分", "10라운드 뒤 아약스는 21점이에요")
m("balans = 成绩单、总结", "balans = 결산")
m("gelijkspelen 过去时复数：speelden gelijk", "gelijkspelen 과거형 복수: speelden gelijk")
m("topper = 焦点战", "topper = 빅매치")
m("stand = 积分榜", "stand = 순위표")
m("doelpunt = 进球", "doelpunt = 골")
m("winnen 过去时：won", "winnen 과거형: won")
m("gaan 过去时：ging", "gaan 과거형: ging")
m("verliezen 过去时：verloor", "verliezen 과거형: verloor")
m("对：阿贾克斯 2–0 获胜", "맞아요: 아약스가 2-0으로 이겼어요")
m("错：NEC 2–4 输了", "틀렸어요: NEC는 2-4로 졌어요")
m("错：特温特–阿贾克斯 13:30；11:15 是海伦芬–费耶诺德",
  "틀렸어요: 트벤테-아약스는 13:30에 시작해요")

# ---------- P5/P6 notes ----------
m("Robinson 在 11 月 1 日周日开始", "로빈슨은 11월 1일 일요일에 시작했어요")
m("Robinson 在 11 月开始", "로빈슨은 11월에 시작했어요")
m("19 位参赛者", "참가자는 19명이에요")
m("ADE 今年 30 年", "ADE는 올해 30주년이에요")
m("错：ADE 今年 30 年", "틀렸어요: ADE는 올해 30주년이에요")
m("设计周约 2.500 位设计师", "디자인 위크에는 약 2,500명의 디자이너가 참여했어요")
m("ADE 与 DDW 在 10 月 25 日周日落幕", "ADE와 디자인 위크는 10월 25일 일요일에 끝났어요")
m("错：10 月 25 日已落幕", "틀렸어요: 10월 25일에 이미 끝났어요")
m("eiland = 岛（het）", "eiland = 섬(중성 명사)")
m("proef = 比赛项目、考验（de）", "proef = 미션(여성 명사)")
m("stemmen = 投票", "stemmen = 투표하다")
m("aflevering = （一）集", "aflevering = (한) 회")
m("voorbij = 过去了、结束了", "voorbij = 끝났어요")
m("kandidaat 复数：kandidaten", "kandidaat 복수형: kandidaten")
m("gaat winnen = 会赢（只是猜测）", "gaat winnen = 이길 거예요(그냥 추측이에요)")
m("wij → gaan + 不定式 kijken", "wij → gaan + 부정사 kijken")
m("hij → gaat praten", "hij → gaat praten")
m("zij (复数) → gaan zoeken", "zij(복수) → gaan zoeken")
m("对：11 月 1 日开始", "맞아요: 11월 1일에 시작했어요")
m("1. Kijk zondag om 20:00 uur op RTL 4（周日晚 20:00 在 RTL 4 收看）",
  "1. Kijk zondag om 20:00 uur op RTL 4(일요일 저녁 8시에 RTL 4에서 보세요)")
m("2. Let op de proeven: daar worden de punten verdeeld（注意比赛项目：分数在那里决出）",
  "2. Let op de proeven: daar worden de punten verdeeld(미션에 주목하세요: 점수는 거기서 갈려요)")
m("3. Raad met vrienden wie het langst blijft（和朋友猜谁能留到最后）",
  "3. Raad met vrienden wie het langst blijft(친구들과 누가 가장 오래 남을지 맞혀 보세요)")
m("4. Volgende week lees je hier hoe het verder ging（下周这里继续报道进展）",
  "4. Volgende week lees je hier hoe het verder ging(다음 주에 여기서 후속 소식을 읽을 수 있어요)")
m("waarschuwingsmoeheid = 预警疲劳", "waarschuwingsmoeheid = 경보 피로")
m("lokaal = 本地的", "lokaal = 현지의")
m("vastzetten = 固定好", "vastzetten = 고정하기")
m("advies = 建议（het）", "advies = 조언(중성 명사)")
m("主语 + 动词 + 地点", "주어 + 동사 + 장소")
m("主语 + 动词 + 宾语 + 地点", "주어 + 동사 + 목적어 + 장소")
m("主语 + 动词 + 时间 + 对手", "주어 + 동사 + 시간 + 상대 팀")
m("主语 + 动词 + 时间", "주어 + 동사 + 시간")
m("祈使句：动词在首位", "명령문: 동사가 앞에 와요")
m("weinig voor = 很少出现", "weinig voor = 좀처럼 나타나지 않다")
m("raakt + 宾语 + 方式", "raakt + 목적어 + 방식")
m("可分动词 mee 在句末", "분리 동사 mee는 문장 끝에 와요")
m("meedoen 是可分动词", "meedoen은 분리 동사예요")
m("meedoen = 参加", "meedoen = 참여하다")
m("注意时间表达 van...tot...", "시간 표현 van...tot...에 주의하세요")
m("第 2 版原句 · bereid je voor 做好准备", "2면 원문 · bereid je voor는 대비하라는 뜻이에요")
m("对照第 1 版头条", "1면 헤드라인 참조")
m("橙色预警：天气危险", "주황색 경보: 날씨가 위험해요")
m("橙色预警意味着：做好准备。", "주황색 경보는 대비하라는 뜻이에요.")
m("我参加气候周。→ ___", "저는 기후 주간에 참여해요. → ___")
m("Klimaatweek=气候周 b", "Klimaatweek=기후 주간 b")
m("besparen=节约 d", "besparen=절약하다 d")
m("waarschuwing=预警 a", "waarschuwing=경보 a")
m("lokaal=本地的 c", "lokaal=현지의 c")
m("klimaat=气候 c", "klimaat=기후 c")
m("meedoen=参加 b", "meedoen=참여하다 b")
m("vastzetten=固定好 d", "vastzetten=고정하기 d")
m("wortelen = 生根（复数主语）", "wortelen = 뿌리내리다(복수 주어)")
m("besparen = 节约", "besparen = 절약하다")
m("fiets = 自行车", "fiets = 자전거")
m("boom = 树", "boom = 나무")
m("struik = 灌木", "struik = 관목")
m("planten = 种", "planten = 심다")
m("zachte = 柔软的（土壤）", "zachte = 부드러운(토양)")
m("Daan 住在科弗登", "단은 쿠포르던에 살아요")
m("他周六领了一棵免费灌木", "그는 토요일에 무료 관목 하나를 받아 갔어요")
m("周日特温特对阿贾克斯", "일요일에 트벤테 대 아약스 경기가 있어요")
m("扎安丹旧货市场约 250 个摊位", "잔담 벼룩시장에는 약 250개의 노점이 있어요")
m("（开放题，范文如下）", "(열린 문제, 모범 답안은 아래에)")
m("范文见本版 H 区（{NWORDS} 词）", "모범 답안은 이 면 H 구역에 있어요({NWORDS}단어)")
m("写作题（无唯一答案）；范文（{NWORDS} 词）见下。",
  "쓰기 문제예요(정답이 하나가 아니에요). 모범 답안({NWORDS}단어)은 아래에 있어요.")

# ---------- P7 ----------
m("气候是长期的天气与自然", "기후는 장기적인 날씨와 자연이에요")
m("气候是长期的天气自然，不是今天的天气。", "기후는 장기적인 날씨와 자연이지, 오늘 날씨가 아니에요.")
m("meedoen = 参加、参与", "meedoen = 참여하다")
m("Ik vind dat… 表达看法", "Ik vind dat… 생각을 말할 때 써요")
m("Het lijkt me dat… = 在我看来", "Het lijkt me dat… = 제 생각에는 ~인 것 같아요")
m("wij → planten", "wij → planten")
m("je → bespaar", "je → bespaar")
m("rood = blijf binnen", "rood = blijf binnen")
m("ik → doe mee", "ik → doe mee")
m("opruimen 的分词：opgeruimd", "opruimen의 과거분사: opgeruimd")
m("vastzetten 过去时：zette vast", "vastzetten 과거형: zette vast")
m("Volgens mij… = 依我看", "Volgens mij… = 제 생각에는")
m("Klimaatweek 是专名，首字母大写。", "Klimaatweek는 고유명사라서 첫 글자를 대문자로 써요.")
m("een 是单数：een boom；复数直接用 bomen。", "een은 단수예요: een boom, 복수는 그냥 bomen.")
m("omdat 从句后，主句动词在第二位：blijf ik thuis。",
  "omdat 절 뒤에서는 본문 동사가 2번 자리에 와요: blijf ik thuis.")
m("截稿时未收到真实来信或第 8 版最佳作文，刊登示例信，承诺顺延 VOL.3。",
  "마감 때까지 실제 독자 편지나 8면 최고 작문이 들어오지 않아서, 이 예시를 싣고 약속은 VOL.3으로 이어져요.")
m("编辑部示例信，非真实来信。欢迎寄来你的真实来信和第 8 版最佳作文，VOL.3 刊登！",
  "편집부 예시예요(실제 편지가 아니에요). 여러분의 실제 편지와 8면 최고 작문을 보내 주세요. VOL.3에 실어 드릴게요!")
m("从 11 月 2 日周一到 8 日周日，荷兰是气候周。", "11월 2일 월요일부터 8일 일요일까지 네덜란드는 기후 주간이에요.")
m("秋天是种树的最好时节。", "가을은 나무를 심기에 가장 좋은 계절이에요.")
m("黄色意味着：当心，天气可能危险。", "노란색은 주의하라는 뜻이에요. 날씨가 위험할 수 있어요.")
m("70 多家博物馆从晚上 19 点开放到凌晨 2 点。", "70곳이 넘는 박물관이 저녁 7시부터 새벽 2시까지 문을 열어요.")
m("阿贾克斯 10 月 22 日周四 2–0 战胜亚特兰大。", "아약스가 10월 22일 목요일에 아탈란타를 2-0으로 이겼어요.")
m("11 月 1 日周日，《荒岛远征》在 RTL 4 开播，20 点。", "11월 1일 일요일, 로빈슨이 RTL 4에서 저녁 8시에 시작했어요.")
m("预警代码不是禁令，而是一条建议。", "경보 코드는 금지령이 아니라 조언이에요.")
m("天气属于我们所有人，但对每个人的影响各不相同。", "날씨는 우리 모두의 것이지만, 우리 모두에게 다르게 다가와요.")

# ---------- type / instr labels (short strings LAST in effect: longest-first sort) ----------
m("完形单选", "빈칸 채우기")
m("完成句子", "문장 완성")
m("词汇配对", "단어 짝짓기")
m("判断对错", "참/거짓 판단")
m("单选", "객관식")
m("造句", "문장 만들기")
m("翻译", "번역")
m("写作", "쓰기")
m("填空", "빈칸 채우기")
m("判断", "참 / 거짓")
m("气候周", "기후 주간")

m("黄色代码：当心", "노란색 코드: 조심하세요")
m("橙色代码：危险", "주황색 코드: 위험해요")

# ---------- apply ----------
def apply_all():
    # paths first (exact substrings, asserted)
    path_pairs = []
    for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        path_pairs.append((f, "weekly-report-w45-nl-core/svg", "weekly-report-w45-nl-ko/svg"))
    for f, old, new in path_pairs:
        p = os.path.join(HERE, f)
        s = open(p, encoding="utf-8").read()
        assert s.count(old) >= 1, (f, old)
        open(p, "w", encoding="utf-8").write(s.replace(old, new))
        print("path", f, "->", new)
    # mapping, longest first
    for old in sorted(M, key=len, reverse=True):
        new = M[old]
        found = 0
        for f in FILES:
            p = os.path.join(HERE, f)
            s = open(p, encoding="utf-8").read()
            if old in s:
                found += s.count(old)
                open(p, "w", encoding="utf-8").write(s.replace(old, new))
        assert found >= 1, f"NOT FOUND: {old!r}"
        print(f"map x{found} :: {old[:40]!r} -> {new[:40]!r}")
    # special: P1 badge line (W43 NLxKO measured: y=372, 19.5pt sans bold BRICK)
    p = os.path.join(HERE, "content12.py")
    s = open(p, encoding="utf-8").read()
    old_badge = 'p.text(975, 372, "DE WEKELIJKSE KRANT OM NEDERLANDS TE LEREN — HET ECHTE NEDERLAND, IN HET NEDERLANDS", 19, "sans", False, GREY, anchor="middle")'
    new_badge = 'p.text(975, 372, "네덜란드어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판", 19.5, "sans", True, BRICK, anchor="middle")'
    assert old_badge in s, "badge line not found"
    open(p, "w", encoding="utf-8").write(s.replace(old_badge, new_badge))
    print("badge replaced")
    # special: P1 black-band right lines (Dutch frozen line replaced by KO furniture)
    s = open(p, encoding="utf-8").read()
    assert '"气候周"' not in s  # already mapped via 气候周 -> 기후 주간
    # special: P8 separator
    p8 = os.path.join(HERE, "content8.py")
    s = open(p8, encoding="utf-8").read()
    old_sep = 'af.para(f"— PAGINA {pg} —"'
    assert old_sep in s
    open(p8, "w", encoding="utf-8").write(s.replace(old_sep, 'af.para(f"— 제 {pg} 면 —"'))
    print("p8 separator replaced")
    # special: P8 translation-item directions (line-based, post-mapping)
    s = open(p8, encoding="utf-8").read()
    lines = s.split("\n")
    def fix_instr(marker, instr):
        n = 0
        for i, ln in enumerate(lines):
            if marker in ln and 'instr="번역"' in ln:
                lines[i] = ln.replace('instr="번역"', f'instr="{instr}"')
                n += 1
        assert n == 1, (marker, n)
    fix_instr("De Klimaatweek duurt zeven dagen.", "한국어로 번역")
    fix_instr("Code oranje betekent: bereid je voor.", "한국어로 번역")
    fix_instr("박물관의 밤은 저녁 7시부터", "네덜란드어로 번역")
    fix_instr("저는 기후 주간에 참여해요.", "네덜란드어로 번역")
    open(p8, "w", encoding="utf-8").write("\n".join(lines))
    print("p8 translate instrs fixed")
    # render.py repoint + names
    rp = os.path.join(HERE, "render.py")
    s = open(rp, encoding="utf-8").read()
    for old, new in [("weekly-report-w45-nl-core", "weekly-report-w45-nl-ko"),
                     ("De-Lucerna-VOL2.pdf", "De-Lucerna-VOL2-KO.pdf"),
                     ("De-Lucerna-VOL2-web.pdf", "De-Lucerna-VOL2-KO-web.pdf"),
                     ("Render the IT weekly", "Render the NL x KO weekly")]:
        assert old in s, old
        s = s.replace(old, new)
    open(rp, "w", encoding="utf-8").write(s)
    print("render.py repointed")
    # run.py docstring
    rp = os.path.join(HERE, "run.py")
    s = open(rp, encoding="utf-8").read()
    if "Run the IT weekly" in s:
        open(rp, "w", encoding="utf-8").write(s.replace("Run the IT weekly", "Run the NL x KO weekly"))
    print("done")

if __name__ == "__main__":
    apply_all()
