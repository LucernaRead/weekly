# -*- coding: utf-8 -*-
"""DE x KO fan-out transform for W46 DE core build copy.
Generated from the EN pair table + tr-ko.py. German body text is
NEVER touched: every `old` is a Chinese explanation-layer string,
a bilingual furniture string, or a generic type/instr token.
Run once from the build dir copy."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
LOG = []

def rep(fname, old, new, expect=None):
    p = os.path.join(BASE, fname)
    s = open(p, encoding="utf-8").read()
    n = s.count(old)
    if expect is not None:
        assert n == expect, f"{fname}: {old!r} count {n} != {expect}"
    else:
        assert n >= 1, f"{fname}: {old!r} not found"
    LOG.append(f"{fname}: {n}x {old[:60]!r} -> {new[:60]!r}")
    open(p, "w", encoding="utf-8").write(s.replace(old, new))

def rep_all(fname, pairs):
    seen = set()
    for old, new in pairs:
        assert old not in seen, f"duplicate old in {fname}: {old!r}"
        seen.add(old)
    for old, new in sorted(pairs, key=lambda t: -len(t[0])):
        rep(fname, old, new)

# ---------- OUT repoint (1 per content file) ----------
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    rep(f, "weekly-report-w46-de-core", "weekly-report-w46-de-ko", 1)

# ---------- svglib docstring comment only (not rendered) ----------
pth = os.path.join(BASE, "svglib.py")
s = open(pth, encoding="utf-8").read()
if "for \u91cd\u9633." in s:
    rep("svglib.py", "for \u91cd\u9633.", "for Double Ninth.", 1)
else:
    LOG.append("svglib.py: no Double Ninth comment (already adapted), skipped")

# ---------- bslib4: furniture + gloss prefix ----------
rep("bslib4.py",
    '"Die Lucerna · \u5fb7\u8bed\u5468\u62a5 VOL.3 · LUCERNA GERMAN WEEKLY"',
    '"Die Lucerna · 독일어 주간지 VOL.3 · 텍스트는 독일어 · 해설은 한국어"', 1)
rep("bslib4.py", 'f"\u7b2c {n} \u7248 / \u5171 {total} \u7248"', 'f"제 {n} 면 / 총 {total} 면"', 1)
rep("bslib4.py", '"\u8bd1\u6ce8\uff5c" + s', '"해설 — " + s', 1)

# ================= content12.py =================
C12 = [
    ('WÖCHENTLICH AUF DEUTSCH · 每周一期 · 读德国人正在读的德语', 'WÖCHENTLICH AUF DEUTSCH · 매주 발행 · 독일이 읽는 독일어'),
    ('德 语 周 报 · VOL.3 · 国 家 队 · 圣 马 丁 · NFL', '독일어 주간지 · VOL.3 · 대표팀 · 성 마르틴 · NFL'),
    ('p.text(975, 372, "DIE WOCHENZEITUNG FÜR LERNENDE — DAS ECHTE LEBEN, AUF DEUTSCH, AUS DEUTSCHLAND", 19, "sans", False, GREY, anchor="middle")', 'p.text(975, 372, "독일어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판", 20, "sans", True, BRICK, anchor="middle")'),
    ('本周国家队周 · 圣马丁节与 NFL', '대표팀 주간 · 성 마르틴과 NFL'),
    ('详见第 4 版 · Seite 4', '4쪽 참조'),
    ('DIE TOPMELDUNG · 头条', 'DIE TOPMELDUNG · 톱 기사'),
    ('讲解｜die Länderspielpause 国家队比赛间歇期 · das Viertelfinale 四分之一决赛 · ausverkauft 售罄。', '해설 — Länderspielpause＝A매치 휴식 · Viertelfinale＝8강전 · ausverkauft＝매진'),
    ('DIE WOCHE IN ZAHLEN · 数字看本周', 'DIE WOCHE IN ZAHLEN · 숫자'),
    ('5 — Punkte hat Deutschland nach vier Spielen in der Nations League（四轮过后德国队 5 分）', '5 — Punkte hat Deutschland nach vier Spielen in der Nations League（독일은 4경기에서 승점 5점）'),
    ('11.11 — um 11.11 Uhr beginnt die Karnevalssession in Köln（11 点 11 分狂欢季开幕）', '11.11 — um 11.11 Uhr beginnt die Karnevalssession in Köln（카니발 시즌은 11시 11분에 개막）'),
    ('15.30 — um 15.30 Uhr beginnt das NFL-Spiel in München（周日 15 点 30 分 NFL 开球）', '15.30 — um 15.30 Uhr beginnt das NFL-Spiel in München（NFL 경기는 일요일 15시 30분에 시작）'),
    ('JETZT ÜBEN · 即学即练', 'JETZT ÜBEN · 지금 연습'),
    ('国家队比赛周', 'A매치 휴식 주간'),
    ('塞尔维亚首都', '세르비아의 수도'),
    ('狂欢季 11 点 11 分开幕', '카니발은 11시 11분에 개막'),
    ('NFL 在慕尼黑', '뮌헨의 NFL'),
    ('四轮 5 分', '4경기 승점 5점'),
    ('周日是纪念日', '일요일은 추모의 날'),
    ('圣马丁节 11 月 11 日', '성 마르틴의 날은 11월 11일'),
    ('11 月 11 日是星期三', '11월 11일은 수요일'),
    ('本周大问题 · Die Fragen der Woche', '큰 질문들 · Die Fragen der Woche'),
    ('德国本周最热议的五个问题。', '이번 주 독일을 달구는 다섯 가지 질문.'),
    ('IN DIESER AUSGABE · 本期目录', 'IN DIESER AUSGABE · 목차'),
    ('空场比赛（无观众）。详见第 4 版。', '관중 없는 경기. 4쪽 참조.'),
    ('KURZ & GUT · 快讯', 'KURZ & GUT · 짧게'),
    ('BLITZQUIZ · 闪电问答', 'BLITZQUIZ · 번개 퀴즈'),
    ('读头版，选出正确答案 · 答案见第 8 版', '1쪽을 읽고 정답을 고르세요 · 답은 8쪽'),
    ('周五客战塞尔维亚', '금요일 세르비아 원정'),
    ('NFL 下午 3 点半开球', 'NFL은 15시 30분 킥오프'),
    ('纪念日在周日', '추모의 날은 일요일'),
    ('LEBEN · 生活', 'LEBEN · 생활'),
    ('LEVEL A2 · Der 11. November & der Alltag · 11 月 11 日与日常生活', 'LEVEL A2 · Der 11. November & der Alltag · 11월 11일과 일상'),
    ('der Jeck 狂欢者（科隆方言） · die fünfte Jahreszeit 第五个季节（狂欢季） · die Laterne 灯笼 · der Weckmann 面人面包 · die Martinsgans 圣马丁鹅。', 'der Jeck＝카니발 축제꾼（쾰른 방언） · die fünfte Jahreszeit＝다섯 번째 계절（카니발） · die Laterne＝등불 · der Weckmann＝빵 인형 · die Martinsgans＝성 마르틴 거위。'),
    ('DER 11. NOVEMBER · 11 月 11 日', 'DER 11. NOVEMBER'),
    ('你过狂欢节还是圣马丁节？写两句德语寄来。', '카니발과 성 마르틴 중 무엇을 기념하나요? 독일어로 두 문장!'),
    ('UND SIE? · 说说你自己', 'UND SIE? · 당신은요?'),
    ('MARTIN IN KÜRZE · 圣马丁简讯', 'MARTIN IN KÜRZE · 요약'),
    ('RECHNEN WIR MAL · 算一算', 'RECHNEN WIR MAL · 계산해 봅시다'),
    ('Die Uhrzeiten der Woche · 本周时刻', 'Die Uhrzeiten der Woche · 이번 주의 시각'),
    ('注意：11 月 11 日是工作日。去科隆要早到：老城很挤，晚上街道属于提灯笼的孩子们。', '참고: 11월 11일은 평일입니다. 쾰른에는 일찍 도착하세요. 구시가지는 붐비고, 저녁에는 거리가 등불을 든 아이들의 차지가 됩니다.'),
    ('ÜBUNGEN · 第 2 版练习', 'ÜBUNGEN · 2쪽 연습'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', '답은 8쪽 · 수준이 섞여 있습니다. 번호로 답을 찾으세요'),
    ('看第 2 版文章，用时间填空。', '2쪽 기사를 읽고 시각을 채우세요.'),
    ('WDR 10 点半直播', 'WDR 10시 30분부터 생중계'),
    ('Weckmann 是面人面包', '벡만은 빵 인형'),
    ('11 月 11 日不是法定假日', '11월 11일은 공휴일이 아니다'),
    ('圣马丁鹅配红甘蓝和丸子', '적양배추와 만두를 곁들인 성 마르틴 거위'),
    ('改成 Perfekt 现在完成时。', 'Perfekt（현재완료）로 고쳐 쓰세요.'),
    ('读第 2 版文章，选出正确答案。', '2쪽 기사를 읽고 정답을 고르세요.'),
    ('Jeck=狂欢者 c', 'Jeck=카니발 축제꾼 c'),
    ('Laterne=灯笼 a', 'Laterne=등불 a'),
    ('Weckmann=面人面包 b', 'Weckmann=빵 인형 b'),
    ('Martinsgans=圣马丁鹅 d', 'Martinsgans=성 마르틴 거위 d'),
]
rep_all("content12.py", C12)

# ================= content34.py =================
C34 = [
    ('KULTUR · 文化', 'KULTUR · 문화'),
    ('A2 → B1 · St. Martin, Karneval & Rückblick · 圣马丁、狂欢节与回顾', 'A2 → B1 · St. Martin, Karneval & Rückblick · 성 마르틴, 카니발, 되돌아보기'),
    ('der Bettler 乞丐 · der Mantel 斗篷 · das Geschnatter 鹅叫声 · der Gänsestall 鹅棚 · das Dreigestirn 狂欢节三人组。', 'der Bettler＝거지 · der Mantel＝망토 · das Geschnatter＝꽥꽥거림 · der Gänsestall＝거위 우리 · das Dreigestirn＝카니발 삼두정。'),
    ('ST. MARTIN · 圣马丁', 'ST. MARTIN · 성 마르틴'),
    ('die Laterne — 灯笼', 'die Laterne — 등불'),
    ('der Mantel — 斗篷', 'der Mantel — 망토'),
    ('die Gans — 鹅', 'die Gans — 거위'),
    ('der Weckmann — 面人面包', 'der Weckmann — 빵 인형'),
    ('das Martinsfeuer — 圣马丁篝火', 'das Martinsfeuer — 성 마르틴 모닥불'),
    ('das Kostüm — 服装', 'das Kostüm — 의상'),
    ('MARTINSWÖRTER · 圣马丁词汇', 'MARTINSWÖRTER · 성 마르틴'),
    ('UND SIE? · 说说你自己', 'UND SIE? · 당신은요?'),
    ('你做过灯笼吗？你们国家的孩子唱什么歌？写两句德语寄来。', '등불을 만들어 본 적이 있나요? 독일어로 두 문장!'),
    ('DER TIPP · 编辑部建议', 'DER TIPP · 조언'),
    ('ÜBUNGEN · 第 3 版练习', 'ÜBUNGEN · 3쪽 연습'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', '답은 8쪽 · 수준이 섞여 있습니다. 번호로 답을 찾으세요'),
    ('读第 3 版文章，判断对错。', '3쪽 기사를 읽으세요. 맞나요, 틀렸나요?'),
    ('传说马丁是罗马士兵', '전설에 따르면 마르틴은 로마 병사였다'),
    ('传说鹅叫声暴露了他', '전설에 따르면 거위들이 그를 들켰다'),
    ('纪念日 11 月 11 日', '기념일은 11월 11일'),
    ('截稿时 11 月 3–8 日结果未知', '11월 3~8일 결과는 마감 시점에 미상'),
    ('狂欢季 11 点 11 分开幕', '카니발은 11시 11분에 개막'),
    ('用方框里的词填空。', '상자의 단어로 완성하세요.'),
    ('斗篷分给乞丐', '거지와 나눈 망토'),
    ('纸灯笼', '종이 등불'),
    ('圣马丁鹅', '성 마르틴 거위'),
    ('圣马丁鹅配红甘蓝和丸子', '적양배추와 만두를 곁들인 성 마르틴 거위'),
    ('狂欢节服装', '카니발 의상'),
    ('游行在篝火处结束', '행렬은 모닥불에서 끝난다'),
    ('选出正确答案。', '정답을 고르세요.'),
    ('马丁后来成为图尔主教', '마르틴은 나중에 투르의 주교가 되었다'),
    ('灯笼游行常在前后晚上举行', '등불 행렬은 전후 저녁에 열리는 경우가 많다'),
    ('VOL.4 报道 11 月 3–8 日结果', 'VOL.4에서 11월 3~8일 결과를 전한다'),
    ('把词组成正确的句子。', '단어를 올바른 문장으로 배열하세요.'),
    ('主谓宾顺序', '주어-동사-목적어 순서'),
    ('时间状语开头，动词第二位', '시간 표현이 먼저, 동사는 두 번째'),
    ('地点开头，动词第二位', '장소가 먼저, 동사는 두 번째'),
    ('SPORT · 体育', 'SPORT · 스포츠'),
    ('LEVEL B1 · Nationalelf & NFL · 国家队与 NFL', 'LEVEL B1 · Nationalelf & NFL · 대표팀과 NFL'),
    ('das Geisterspiel 空场比赛 · das Hinspiel 首回合 · ausverkauft 售罄 · der Star 明星 · gewinnen 获胜。', 'das Geisterspiel＝무관중 경기 · das Hinspiel＝1차전 · ausverkauft＝매진 · der Star＝스타 · gewinnen＝이기다。'),
    ('你更爱看足球还是美式橄榄球？贝尔格莱德谁赢？写两句德语寄来。', '축구와 미식축구, 누가 이길까요? 독일어로 두 문장!'),
    ('DER SPIELPLAN · 本周与下周赛程', 'DER SPIELPLAN · 이번 주와 다음 주'),
    ('ÜBUNGEN · 第 4 版练习', 'ÜBUNGEN · 4쪽 연습'),
    ('读第 4 版文章，选出正确答案。', '4쪽 기사를 읽고 정답을 고르세요.'),
    ('德国 5 分，荷兰希腊各 8 分', '독일 5점, 네덜란드와 그리스 각 8점'),
    ('主教练 11 月 5 日公布名单', '감독은 11월 5일에 명단을 발표한다'),
    ('贝尔格莱德空场', '베오그라드의 빈 경기장'),
    ('首回合德国 2:0 胜塞尔维亚', '독일은 1차전에서 세르비아를 2-0으로 이겼다'),
    ('NFL 慕尼黑赛售罄', '뮌헨 NFL 경기는 매진'),
    ('Geisterspiel=空场比赛 b', 'Geisterspiel=무관중 경기 b'),
    ('Hinspiel=首回合 a', 'Hinspiel=1차전 a'),
    ('Ausrüster=装备赞助商 c', 'Ausrüster=유니폼 공급사 c'),
    ('ausverkauft=售罄 d', 'ausverkauft=매진 d'),
    ('用比较级完成句子（括号里是原级）。', '비교급으로 완성하세요（괄호 안은 원급）。'),
    ('viel → mehr（荷兰 8 分多于德国 5 分）', 'viel → mehr（네덜란드는 8점, 독일의 5점보다 많다）'),
    ('spät → später（15:30 晚于 11:11）', 'spät → später（15시 30분은 11시 11분보다 늦다）'),
    ('leise → leiser（空场比主场安静）', 'leise → leiser（빈 경기장은 홈 경기보다 조용하다）'),
    ('früh → früher（11 月 5 日早于 11 月 13 日）', 'früh → früher（11월 5일은 11월 13일보다 이르다）'),
    ('看上面的赛程表，选出正确答案。', '위 경기 일정표를 보고 정답을 고르세요.'),
    ('塞尔维亚–德国周五 20:45', '세르비아-독일 금요일 20시 45분'),
    ('NFL 周日 15:30', 'NFL 일요일 15시 30분'),
    ('德国–荷兰周一 20:45', '독일-네덜란드 월요일 20시 45분'),
    ('拜仁–科隆周五 20:30', '바이에른-쾰른 금요일 20시 30분'),
    ('沙尔克–斯图加特周六 17:30', '샬케-슈투트가르트 토요일 17시 30분'),
]
rep_all("content34.py", C34)

# ================= content56.py =================
C56 = [
    ('JUGEND · 青年', 'JUGEND · 청소년'),
    ('LEVEL B1 · Laternen, Lieder & Schule · 灯笼、歌曲与学校', 'LEVEL B1 · Laternen, Lieder & Schule · 등불, 노래, 학교'),
    ('basteln 制作 · der Pausenhof 课间操场 · sich verkleiden 乔装打扮 · die Stimmung 气氛 · der Pirat 海盗。', 'basteln＝만들다 · der Pausenhof＝운동장 · sich verkleiden＝분장하다 · die Stimmung＝분위기 · der Pirat＝해적。'),
    ('SCHULWOCHE · 开学周', 'SCHULWOCHE · 학교'),
    ('die Laterne — 灯笼', 'die Laterne — 등불'),
    ('basteln — 制作', 'basteln — 만들다'),
    ('das Lied — 歌曲', 'das Lied — 노래'),
    ('das Kostüm — 服装', 'das Kostüm — 의상'),
    ('der Umzug — 游行', 'der Umzug — 행렬'),
    ('der Stern — 星星', 'der Stern — 별'),
    ('MARTINSWÖRTER · 圣马丁词汇', 'MARTINSWÖRTER · 성 마르틴'),
    ('UND SIE? · 说说你自己', 'UND SIE? · 당신은요?'),
    ('你小时候做过灯笼吗？11 月你唱哪首歌？写两句德语寄来。', '어릴 때 등불을 만들었나요? 독일어로 두 문장!'),
    ('DER WOCHENPLAN DER REDAKTION · 编辑部一周计划', 'DER WOCHENPLAN DER REDAKTION · 편집부의 한 주'),
    ('ÜBUNGEN · 第 5 版练习', 'ÜBUNGEN · 5쪽 연습'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', '답은 8쪽 · 수준이 섞여 있습니다. 번호로 답을 찾으세요'),
    ('读第 5 版文章，选出正确答案。', '5쪽 기사를 읽고 정답을 고르세요.'),
    ('11 月 9 日全德复课', '학교는 11월 9일에 모든 곳에서 다시 시작'),
    ('孩子们做纸灯笼', '아이들은 종이 등불을 만든다'),
    ('纸灯笼', '종이 등불'),
    ('上午狂欢，下午圣马丁', '오전에는 카니발, 오후에는 성 마르틴'),
    ('NFL 周日在电视上', '일요일 TV로 NFL'),
    ('周五看国家队比赛', '금요일에 대표팀 보기'),
    ('用方框里的词填空。', '상자의 단어로 완성하세요.'),
    ('做灯笼', '등불 만들기'),
    ('唱圣马丁歌曲', '성 마르틴 노래 부르기'),
    ('狂欢节服装', '카니발 의상'),
    ('灯笼游行', '등불 행렬'),
    ('灯笼上的星星', '등불 위의 별'),
    ('用 weil 连接两个句子（动词放句末）。', '두 문장을 weil로 연결하세요（동사는 맨 끝으로）。'),
    ('weil 句动词置尾', 'weil 절에서는 동사가 맨 끝으로'),
    ('ist 置尾', 'ist는 맨 끝으로'),
    ('will 置尾', 'will은 맨 끝으로'),
    ('beginnt 置尾', 'beginnt는 맨 끝으로'),
    ('判断对错。', '맞나요, 틀렸나요?'),
    ('11 月 9 日巴伐利亚也复课', '바이에른도 11월 9일에 복귀'),
    ('灯笼游行在晚上', '등불 행렬은 저녁에'),
    ('孩子们唱圣马丁歌曲', '아이들은 성 마르틴 노래를 부른다'),
    ('VERTIEFUNG · 深读', 'VERTIEFUNG · 심화 읽기'),
    ('LEVEL B2 · Volkstrauertag & Stromsteuer · 纪念日与电力税', 'LEVEL B2 · Volkstrauertag & Stromsteuer · 추모의 날과 전기세'),
    ('gedenken 纪念 · die Kranzniederlegung 献花圈 · der stille Tag 安静日 · die Verbundenheit 联系 · die Versöhnung 和解。', 'gedenken＝추모하다 · Kranzniederlegung＝헌화 · stille Tag＝조용한 날 · Verbundenheit＝유대 · Versöhnung＝화해。'),
    ('DIE ZAHLEN · 本周数字', 'DIE ZAHLEN · 숫자'),
    ('纪念日：纪念需要安静——对此几乎人人赞同。电力税：降多少尚未确定。两者都关系到几乎每个家庭。', '추모의 날: 추모에는 고요함이 필요하다——거의 모두가 동의한다. 전기세: 얼마나 내릴지는 아직 미정이다. 둘 다 거의 모든 가정에 영향을 미친다.'),
    ('ZWEI SONNTAGE IM NOVEMBER · 十一月的两个周日', 'ZWEI SONNTAGE IM NOVEMBER · 11월의 두 일요일'),
    ('WAS INTERESSIERT DIE LESER? · 读者最关心什么？', 'WAS INTERESSIERT DIE LESER? · 독자의 관심은?'),
    ('("Nations League und NFL", 46, "足球")', '("Nations League und NFL", 46, "축구")'),
    ('("St. Martin und Karneval", 34, "节日")', '("St. Martin und Karneval", 34, "축제")'),
    ('("Volkstrauertag und Gedenken", 20, "纪念")', '("Volkstrauertag und Gedenken", 20, "추모")'),
    ('ÜBUNGSDATEN · 练习数据 — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage.（本图数字为编辑部练习示例，非真实调查。）', 'ÜBUNGSDATEN · 연습용 자료 — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage.（연습용 자료이며 실제 설문 조사가 아닙니다.）'),
    ('ÜBUNGEN · 第 6 版练习', 'ÜBUNGEN · 6쪽 연습'),
    ('看上面的练习图表，选出正确答案。', '위 연습용 도표를 사용하세요.'),
    ('46% 足球最受关注', '축구가 46%로 선두'),
    ('节日 34% 第二', '축제가 34%로 2위'),
    ('纪念 20% 最小', '추모가 20%로 가장 적다'),
    ('纪念 20%', '추모 20%'),
    ('读第 6 版深读文章，选出正确答案。', '6쪽 기사를 읽으세요.'),
    ('11 月 15 日纪念日', '추모의 날은 11월 15일'),
    ('ZDF 13 点半直播纪念仪式', 'ZDF 13시 30분부터 생중계'),
    ('家庭电力税 2.05 欧分', '가정용 전기세는 2.05센트'),
    ('2027 年预算 11 月 27 日表决', '2027년 예산 표결은 11월 27일'),
    ('用括号里的形式填空。', '괄호 안의 형태로 채우세요.'),
    ('被动：wird + Partizip II', '수동태: wird＋과거분사'),
    ('ob 引导间接疑问句', 'ob는 간접의문문을 이끈다'),
    ('献花圈仪式', '헌화식'),
    ('为和平与和解', '평화와 화해를 위해'),
    ('德奥联系', '독일-오스트리아 유대'),
    ('纪念受害者', '희생자 추모'),
]
rep_all("content56.py", C56)

# ================= content7.py =================
C7 = [
    ('SPRACHE · 语言', 'SPRACHE · 언어'),
    ('A2 → B2 · Sätze der Woche & Fehlerklinik · 本周金句与纠错诊所', 'A2 → B2 · Sätze der Woche & Fehlerklinik · 이번 주의 문장과 오류 클리닉'),
    ('本版专攻语言：三节小课、本期金句（全部摘自本期文章原文）、纠错诊所和读者来信。', '이 페이지는 온통 언어입니다. 세 가지 짧은 수업, 이번 주의 문장들（이번 호 기사에서 한 글자도 빠짐없이 인용）, 오류 클리닉, 독자 편지.'),
    ('BEISPIELE · 例句', 'BEISPIELE · 예문'),
    ('被动：wird + Partizip II', '수동태: wird＋과거분사'),
    ('复数：werden', '복수: werden'),
    ('werden + 原形表将来', 'werden＋부정사로 미래'),
    ('被动语态', '수동태'),
    ('lang → länger（夜晚比白天长）', 'lang → länger（밤은 낮보다 길다）'),
    ('weil 引导原因', 'weil은 이유를 이끈다'),
    ('weil 句动词置尾', 'weil 절에서는 동사가 맨 끝으로'),
    ('länger als = 比……更长', 'länger als＝～보다 길다'),
    ('„Länger als sonst“ heißt... A. 比平时更长 · B. 和平时一样 · C. 比平时更短', '„Länger als sonst“의 뜻은… A. 평소보다 길다 · B. 평소와 같다 · C. 평소보다 짧다'),
    ('ob 引导间接疑问', 'ob는 간접의문문을 이끈다'),
    ('Es ist fraglich, ob ... = 是否还难说', 'Es ist fraglich, ob ...＝～인지 의심스럽다'),
    ('dass 句动词置尾', 'dass 절에서는 동사가 맨 끝으로'),
    ('礼貌表达观点', '정중하게 의견을 말하는 방법'),
    ('11.11 Uhr = 11 点 11 分', '11.11 Uhr＝11시 11분'),
    ('vor leeren Rängen = 空场，没有观众', 'vor leeren Rängen＝무관중'),
    ('Es wird gespielt. = 比赛将进行（被动）', 'Es wird gespielt.＝경기가 열린다'),
    ('Meiner Meinung nach ... = 在我看来……', 'Meiner Meinung nach＝제 생각에는'),
    ('Ich finde, dass ... = 我觉得……', 'Ich finde, dass＝～라고 생각한다'),
    ('Es ist fraglich, ob ... = 是否……还难说', 'Es ist fraglich, ob ...＝～인지 의심스럽다'),
    ('DER WERKZEUGKASTEN · 工具箱', 'DER WERKZEUGKASTEN'),
    ('label = "Ein Beispiel der Redaktion!"', 'label = "편집부의 예시입니다!"'),
    ('编辑部示例，非真实来信：截稿时未收到真实来信或习作，见 VOL.4。请寄来您的习作，优秀者刊登于 VOL.4。', '편집부의 예시이며 실제 편지가 아닙니다. 마감 시점까지 실제 편지는 도착하지 않았습니다. VOL.4로 보내 주세요!'),
    ('LESERBRIEFE · 读者来信', 'LESERBRIEFE · 독자 편지'),
    ('NOCH EIN WORT · 再学一词', 'NOCH EIN WORT · 한 마디 더'),
    ('«das Geisterspiel»（Seite 4）: ein Spiel ohne Zuschauer im Stadion. 空场比赛。', '«das Geisterspiel» (Seite 4) : ein Spiel ohne Zuschauer im Stadion. 무관중 경기: 관중 없는 경기.'),
    ('SÄTZE DER WOCHE · 本周金句', 'SÄTZE DER WOCHE · 이번 주의 문장'),
    ('原文摘录，逐字引自本期文章 · 括号内为出处', '이번 호 기사에서 한 글자도 빠짐없이 인용 · 출처는 괄호 안'),
    ('德甲休战——但国家队要比赛。', '분데스리가는 쉬지만——대표팀은 경기를 한다.'),
    ('11 点 11 分，科隆新一季狂欢季开幕。', '11시 11분, 쾰른에서 새 카니발 시즌이 시작된다.'),
    ('他的纪念日是 11 月 11 日。', '그의 기념일은 11월 11일이다.'),
    ('书包收拾好了，操场上又热闹起来。', '가방은 챙겨졌고, 운동장은 다시 시끄럽다.'),
    ('十一月黑暗，但并不安静：它歌唱、发光、庆祝。', '11월은 어둡지만 조용하지 않다. 노래하고, 빛나고, 축제를 연다.'),
    ('比赛售罄，RTL 现场直播。', '경기는 매진, RTL이 생중계한다.'),
    ('这里的纪念意味着：停下来、记住——并为和平与和解挺身而出。', '여기서 추모란 멈추고, 기억하고——평화와 화해를 위해 일어서는 것이다.'),
    ('周日，全国一片安静。', '일요일, 나라는 조용하다.'),
    ('FEHLERKLINIK · 纠错诊所', 'FEHLERKLINIK · 오류 클리닉'),
    ('学习者最常犯的四个错 · 先自己改，再看答案', '학습자가 가장 자주 하는 네 가지 실수 · 먼저 고치고 확인하세요'),
    ('动词第二位：主语不在句首时，动词仍居第二。', '동사는 두 번째: 주어가 처음이 아니어도 동사는 두 번째 자리를 지킨다.'),
    ('halb zwölf = 十一点半（zwölf 之前）。', 'halb zwölf＝11시 30분, zwölf의 30분 전.'),
    ('Perfekt 中 Partizip II 放句末。', 'Perfekt에서는 과거분사가 맨 끝으로 간다.'),
    ('ob 从句动词放句末。', 'ob 절에서는 동사가 맨 끝으로 간다.'),
    ('IN DER NÄCHSTEN AUSGABE · 下期预告 (VOL.4)', 'IN DER NÄCHSTEN AUSGABE · 다음 호（VOL.4）'),
]
rep_all("content7.py", C7)

# ================= content8.py =================
C8 = [
    ('ÜBUNGEN & ANTWORTEN · 练习与答案', 'ÜBUNGEN & ANTWORTEN · 연습과 답'),
    ('SCHLUSSTEST · 综合评估 · Alle Antworten unten auf dieser Seite 答案在本版下方', 'SCHLUSSTEST · 최종 테스트 · Alle Antworten unten auf dieser Seite — 모든 답은 이 페이지 하단에'),
    ('beginnt（第三人称单数）', 'beginnt(3인칭 단수)'),
    ('bastelt（第三人称单数）', 'bastelt(3인칭 단수)'),
    ('geht（第三人称单数）', 'geht(3인칭 단수)'),
    ('singt（第三人称单数）', 'singt(3인칭 단수)'),
    ('schaut（第三人称单数）', 'schaut(3인칭 단수)'),
    ('sieht（第三人称单数）', 'sieht(3인칭 단수)'),
    ('erzählt（第三人称单数）', 'erzählt(3인칭 단수)'),
    ('A · LÜCKENTEXT · 完形填空', 'A · LÜCKENTEXT · 빈칸 채우기'),
    ('选项：', '선택지:'),
    ('B · WISSENSFRAGEN · 综合问答', 'B · WISSENSFRAGEN · 퀴즈'),
    ('狂欢季 11 点 11 分开幕', '카니발은 11시 11분에 개막'),
    ('周五客战塞尔维亚', '금요일 세르비아 원정'),
    ('NFL 周日 15:30', 'NFL 일요일 15시 30분'),
    ('纪念日 11 月 15 日', '추모의 날은 11월 15일'),
    ('家庭电力税 2.05 欧分', '가정용 전기세는 2.05센트'),
    ('主教练 11 月 5 日公布名单', '감독은 11월 5일에 명단을 발표한다'),
    ('ZDF 13 点半直播纪念仪式', 'ZDF 13시 30분부터 생중계'),
    ('亡灵主日 11 月 22 日', 'Totensonntag는 11월 22일'),
    ('C · LESEVERSTEHEN · 阅读理解', 'C · LESEVERSTEHEN · 읽기'),
    ('周三做灯笼', '수요일에 등불 만들기'),
    ('周五看德国队', '금요일에 독일 보기'),
    ('D · SÄTZE BAUEN · 造句', 'D · SÄTZE BAUEN · 문장 만들기'),
    ('时间状语，动词第二位', '시간 표현, 동사는 두 번째'),
    ('主谓宾顺序', '주어-동사-목적어 순서'),
    ('时间状语开头，动词第二位', '시간 표현이 먼저, 동사는 두 번째'),
    ('地点时间开头，动词第二位', '장소와 시간이 먼저, 동사는 두 번째'),
    ('E · ÜBERSETZEN · 翻译', 'E · ÜBERSETZEN · 번역'),
    ('狂欢节 11 点 11 分在科隆开幕。', '카니발은 11시 11분에 쾰른에서 개막한다.'),
    ('beginnen = 开始', 'beginnen＝시작하다'),
    ('Der Karneval beginnt um 11.11 Uhr in Köln.（译成中文）', 'Der Karneval beginnt um 11.11 Uhr in Köln.（한국어로 번역하세요）'),
    ('我周三做一个灯笼。', '수요일에 등불을 만듭니다.'),
    ('basteln = 制作', 'basteln＝만들다'),
    ('Ich bastle am Mittwoch eine Laterne.（译成中文）', 'Ich bastle am Mittwoch eine Laterne.（한국어로 번역하세요）'),
    ('学校 11 月 9 日又开学了。', '학교는 11월 9일에 다시 시작했습니다.'),
    ('wieder begonnen = 又开始', 'wieder begonnen＝다시 시작했다'),
    ('Die Schule hat am 9. November wieder begonnen.（译成中文）', 'Die Schule hat am 9. November wieder begonnen.（한국어로 번역하세요）'),
    ('看比赛 = das Spiel schauen', '경기를 보다＝das Spiel schauen'),
    ('"我周日看 NFL 比赛。（译成德语）", instr="翻译"', '"일요일에 NFL 경기를 봅니다.（독일어로 번역하세요）", instr="독일어로 번역"'),
    ('F · WÖRTER PAAREN · 词汇配对', 'F · WÖRTER PAAREN · 단어 짝짓기'),
    ('Mantel=斗篷 b', 'Mantel=망토 b'),
    ('Laterne=灯笼 a', 'Laterne=등불 a'),
    ('Geisterspiel=空场比赛 d', 'Geisterspiel=무관중 경기 d'),
    ('Versöhnung=和解 c', 'Versöhnung=화해 c'),
    ('singst（第二人称单数）', 'singst(2인칭 단수)'),
    ('macht（第二人称复数）', 'macht(2인칭 복수)'),
    ('essen（第一人称复数）', 'essen(1인칭 복수)'),
    ('machst（第二人称单数）', 'machst(2인칭 단수)'),
    ('schaue（第一人称单数）', 'schaue(1인칭 단수)'),
    ('G · DIALOG · 对话补全', 'G · DIALOG · 대화 완성'),
    ('开放题 — 要点见写作框，范文在第 8 版写作框内', '열린 과제 — 쓰기 상자의 항목을 따르세요. 모범 답안은 이 페이지의 상자 안에 있습니다'),
    ('按要点给分', '나열된 항목에 따라 채점됩니다'),
    ('H · SCHREIBEN · 写作', 'H · SCHREIBEN · 쓰기'),
    ('用德语写 80–100 词：《我的十一月的一周》。写清做什么手工、看哪几场比赛、和谁一起，并写一句关于圣马丁节或纪念日的话。', '독일어로 80~100단어로 쓰세요. «11월의 나의 한 주». 무엇을 만드는지, 어떤 경기를 누구와 보는지 말하고——성 마르틴의 날이나 추모의 날에 대해 한 문장을 더하세요.'),
    ('MUSTER · 范文（84 Wörter）', 'MUSTER · 모범 답안 (84단어)'),
    ('ANTWORTEN · 全部答案与简析（第 1–8 版）', 'ANTWORTEN · 모든 답과 해설（1~8쪽）'),
]
rep_all("content8.py", C8)

# ---------- P8 keys ----------
rep("content8.py", 'kf.para(f"— \u7b2c {pg} \u7248 —", 17, "sans", True, OLIVE, 1.28, 3)',
    'kf.para(f"— 제 {pg} 면 —", 17, "sans", True, OLIVE, 1.28, 3)', 1)
rep("content8.py", 's += f"\uff08{e[\'note\']}\uff09"',
    's += f" ({e[\'note\']})"', 1)
rep("content8.py", 'kf.para(" · ".join(parts), 14.5, "sans", False, INK, 1.3, 9)',
    'kf.para(" · ".join(parts), 13.0, "sans", False, INK, 1.26, 9)', 1)

# ---------- generic value maps ----------
TYPEMAP = [('完成句子', '문장 완성'), ('单选', '객관식'), ('句型转换', '문장 전환'), ('词汇配对', '단어 짝짓기'), ('判断对错', '참-거짓 판단'), ('完形填空', '빈칸 채우기'), ('造句', '문장 만들기'), ('对话补全', '대화 완성'), ('翻译', '번역'), ('写作', '쓰기')]
INSTRMAP = [('instr="填空"', 'instr="빈칸"'), ('instr="改写"', 'instr="바꿔 쓰기"'), ('instr="判断"', 'instr="판단"'), ('instr="造句"', 'instr="문장 만들기"'), ('instr="翻译"', 'instr="번역"'), ('instr="把词和释义配对"', 'instr="단어와 뜻 짝짓기"')]
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    for old, new in INSTRMAP + TYPEMAP:
        pth = os.path.join(BASE, f)
        n = open(pth, encoding="utf-8").read().count(old)
        if n == 0:
            LOG.append(f"{f}: 0x {old!r} (absent, skipped)")
        else:
            rep(f, old, new)

# ---------- leak check: no original Chinese literal may remain ----------
import re
olds = [old for _, old, _ in [('C12', 'WÖCHENTLICH AUF DEUTSCH · 每周一期 · 读德国人正在读的德语', 'WÖCHENTLICH AUF DEUTSCH · ONE ISSUE A WEEK · THE GERMAN THAT GERMANS READ'), ('C12', '德 语 周 报 · VOL.3 · 国 家 队 · 圣 马 丁 · NFL', 'GERMAN WEEKLY · VOL.3 · NATIONAL TEAM · ST MARTIN · NFL'), ('C12', 'p.text(975, 372, "DIE WOCHENZEITUNG FÜR LERNENDE — DAS ECHTE LEBEN, AUF DEUTSCH, AUS DEUTSCHLAND", 19, "sans", False, GREY, anchor="middle")', 'p.text(975, 372, "TEXT IN GERMAN · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS", 20, "sans", True, OLIVE, anchor="middle")'), ('C12', '本周国家队周 · 圣马丁节与 NFL', 'NATIONAL WEEK · ST MARTIN & NFL'), ('C12', '详见第 4 版 · Seite 4', 'See page 4'), ('C12', 'DIE TOPMELDUNG · 头条', 'DIE TOPMELDUNG · Top story'), ('C12', '讲解｜die Länderspielpause 国家队比赛间歇期 · das Viertelfinale 四分之一决赛 · ausverkauft 售罄。', 'Notes — die Länderspielpause = international break · das Viertelfinale = quarter-final · ausverkauft = sold out.'), ('C12', 'DIE WOCHE IN ZAHLEN · 数字看本周', 'DIE WOCHE IN ZAHLEN · Numbers'), ('C12', '5 — Punkte hat Deutschland nach vier Spielen in der Nations League（四轮过后德国队 5 分）', '5 — Punkte hat Deutschland nach vier Spielen in der Nations League (Germany have 5 points after four games)'), ('C12', '11.11 — um 11.11 Uhr beginnt die Karnevalssession in Köln（11 点 11 分狂欢季开幕）', '11.11 — um 11.11 Uhr beginnt die Karnevalssession in Köln (the carnival session opens at 11.11)'), ('C12', '15.30 — um 15.30 Uhr beginnt das NFL-Spiel in München（周日 15 点 30 分 NFL 开球）', '15.30 — um 15.30 Uhr beginnt das NFL-Spiel in München (the NFL game kicks off at 15.30 on Sunday)'), ('C12', 'JETZT ÜBEN · 即学即练', 'JETZT ÜBEN · Practise now'), ('C12', '国家队比赛周', 'international break week'), ('C12', '塞尔维亚首都', 'capital of Serbia'), ('C12', '狂欢季 11 点 11 分开幕', 'carnival opens at 11.11'), ('C12', 'NFL 在慕尼黑', 'the NFL in Munich'), ('C12', '四轮 5 分', '5 points after four games'), ('C12', '周日是纪念日', 'Sunday is the remembrance day'), ('C12', '圣马丁节 11 月 11 日', "St Martin's Day is 11 November"), ('C12', '11 月 11 日是星期三', '11 November is a Wednesday'), ('C12', '本周大问题 · Die Fragen der Woche', 'Big questions · Die Fragen der Woche'), ('C12', '德国本周最热议的五个问题。', "Germany's five hot questions this week."), ('C12', 'IN DIESER AUSGABE · 本期目录', 'IN DIESER AUSGABE · In this issue'), ('C12', '空场比赛（无观众）。详见第 4 版。', 'A match with no spectators. See page 4.'), ('C12', 'KURZ & GUT · 快讯', 'KURZ & GUT · In brief'), ('C12', 'BLITZQUIZ · 闪电问答', 'BLITZQUIZ · Lightning quiz'), ('C12', '读头版，选出正确答案 · 答案见第 8 版', 'Read page 1 and choose the right answer · Answers on page 8'), ('C12', '周五客战塞尔维亚', 'away in Serbia on Friday'), ('C12', 'NFL 下午 3 点半开球', 'NFL kick-off at 3.30 pm'), ('C12', '纪念日在周日', 'the remembrance day is on Sunday'), ('C12', 'LEBEN · 生活', 'LEBEN · Life'), ('C12', 'LEVEL A2 · Der 11. November & der Alltag · 11 月 11 日与日常生活', 'LEVEL A2 · Der 11. November & der Alltag · 11 November and everyday life'), ('C12', 'der Jeck 狂欢者（科隆方言） · die fünfte Jahreszeit 第五个季节（狂欢季） · die Laterne 灯笼 · der Weckmann 面人面包 · die Martinsgans 圣马丁鹅。', "der Jeck = carnival reveller (Cologne dialect) · die fünfte Jahreszeit = the fifth season (carnival) · die Laterne = lantern · der Weckmann = bread man · die Martinsgans = St Martin's goose."), ('C12', 'DER 11. NOVEMBER · 11 月 11 日', 'DER 11. NOVEMBER'), ('C12', '你过狂欢节还是圣马丁节？写两句德语寄来。', 'Do you celebrate Karneval or St Martin? Write two German sentences!'), ('C12', 'UND SIE? · 说说你自己', 'UND SIE? · And you?'), ('C12', 'MARTIN IN KÜRZE · 圣马丁简讯', 'MARTIN IN KÜRZE · In brief'), ('C12', 'RECHNEN WIR MAL · 算一算', "RECHNEN WIR MAL · Let's calculate"), ('C12', 'Die Uhrzeiten der Woche · 本周时刻', "Die Uhrzeiten der Woche · This week's times"), ('C12', '注意：11 月 11 日是工作日。去科隆要早到：老城很挤，晚上街道属于提灯笼的孩子们。', 'Note: 11 November is a working day. Arrive early in Cologne: the old town is crowded, and in the evening the streets belong to the children with their lanterns.'), ('C12', 'ÜBUNGEN · 第 2 版练习', 'ÜBUNGEN · Page 2 exercises'), ('C12', '答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Answers on page 8 · Levels mix freely — find each answer by its number'), ('C12', '看第 2 版文章，用时间填空。', 'Read the page 2 article and fill in the times.'), ('C12', 'WDR 10 点半直播', 'WDR live from 10.30'), ('C12', 'Weckmann 是面人面包', 'a Weckmann is a bread man'), ('C12', '11 月 11 日不是法定假日', '11 November is not a public holiday'), ('C12', '圣马丁鹅配红甘蓝和丸子', "St Martin's goose with red cabbage and dumplings"), ('C12', '改成 Perfekt 现在完成时。', 'Rewrite in the Perfekt (present perfect).'), ('C12', '读第 2 版文章，选出正确答案。', 'Read the page 2 article and choose the right answer.'), ('C12', 'Jeck=狂欢者 c', 'Jeck=carnival reveller c'), ('C12', 'Laterne=灯笼 a', 'Laterne=lantern a'), ('C12', 'Weckmann=面人面包 b', 'Weckmann=bread man b'), ('C12', 'Martinsgans=圣马丁鹅 d', "Martinsgans=St Martin's goose d"), ('C34', 'KULTUR · 文化', 'KULTUR · Culture'), ('C34', 'A2 → B1 · St. Martin, Karneval & Rückblick · 圣马丁、狂欢节与回顾', 'A2 → B1 · St. Martin, Karneval & Rückblick · St Martin, carnival and a look back'), ('C34', 'der Bettler 乞丐 · der Mantel 斗篷 · das Geschnatter 鹅叫声 · der Gänsestall 鹅棚 · das Dreigestirn 狂欢节三人组。', 'der Bettler = beggar · der Mantel = cloak · das Geschnatter = cackling · der Gänsestall = goose shed · das Dreigestirn = carnival triumvirate.'), ('C34', 'ST. MARTIN · 圣马丁', 'ST. MARTIN · St Martin'), ('C34', 'die Laterne — 灯笼', 'die Laterne — lantern'), ('C34', 'der Mantel — 斗篷', 'der Mantel — cloak'), ('C34', 'die Gans — 鹅', 'die Gans — goose'), ('C34', 'der Weckmann — 面人面包', 'der Weckmann — bread man'), ('C34', 'das Martinsfeuer — 圣马丁篝火', "das Martinsfeuer — St Martin's bonfire"), ('C34', 'das Kostüm — 服装', 'das Kostüm — costume'), ('C34', 'MARTINSWÖRTER · 圣马丁词汇', 'MARTINSWÖRTER · St Martin'), ('C34', 'UND SIE? · 说说你自己', 'UND SIE? · And you?'), ('C34', '你做过灯笼吗？你们国家的孩子唱什么歌？写两句德语寄来。', 'Have you ever made a lantern? What songs do children sing in your country? Write two German sentences!'), ('C34', 'DER TIPP · 编辑部建议', "DER TIPP · Editors' tip"), ('C34', 'ÜBUNGEN · 第 3 版练习', 'ÜBUNGEN · Page 3 exercises'), ('C34', '答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Answers on page 8 · Levels mix freely — find each answer by its number'), ('C34', '读第 3 版文章，判断对错。', 'Read the page 3 article. Right or wrong?'), ('C34', '传说马丁是罗马士兵', 'legend says Martin was a Roman soldier'), ('C34', '传说鹅叫声暴露了他', 'legend says the geese gave him away'), ('C34', '纪念日 11 月 11 日', 'memorial day is 11 November'), ('C34', '截稿时 11 月 3–8 日结果未知', 'results of 3–8 November unknown at press time'), ('C34', '狂欢季 11 点 11 分开幕', 'carnival opens at 11.11'), ('C34', '用方框里的词填空。', 'Complete with the words from the box.'), ('C34', '斗篷分给乞丐', 'the cloak shared with the beggar'), ('C34', '纸灯笼', 'a paper lantern'), ('C34', '圣马丁鹅', "St Martin's goose"), ('C34', '圣马丁鹅配红甘蓝和丸子', "St Martin's goose with red cabbage and dumplings"), ('C34', '狂欢节服装', 'a carnival costume'), ('C34', '游行在篝火处结束', 'the procession ends at the bonfire'), ('C34', '选出正确答案。', 'Choose the right answer.'), ('C34', '马丁后来成为图尔主教', 'Martin later became bishop of Tours'), ('C34', '灯笼游行常在前后晚上举行', 'lantern processions often happen on nearby evenings'), ('C34', 'VOL.4 报道 11 月 3–8 日结果', 'VOL.4 will report the 3–8 November results'), ('C34', '把词组成正确的句子。', 'Put the words into a correct sentence.'), ('C34', '主谓宾顺序', 'subject–verb–object order'), ('C34', '时间状语开头，动词第二位', 'time phrase first, verb second'), ('C34', '地点开头，动词第二位', 'place first, verb second'), ('C34', 'SPORT · 体育', 'SPORT · Sport'), ('C34', 'LEVEL B1 · Nationalelf & NFL · 国家队与 NFL', 'LEVEL B1 · Nationalelf & NFL · National team and NFL'), ('C34', 'das Geisterspiel 空场比赛 · das Hinspiel 首回合 · ausverkauft 售罄 · der Star 明星 · gewinnen 获胜。', 'das Geisterspiel = ghost game · das Hinspiel = first leg · ausverkauft = sold out · der Star = star · gewinnen = to win.'), ('C34', '你更爱看足球还是美式橄榄球？贝尔格莱德谁赢？写两句德语寄来。', 'Football or American football? Who wins? Write two German sentences!'), ('C34', 'DER SPIELPLAN · 本周与下周赛程', 'DER SPIELPLAN · This week and next week'), ('C34', 'ÜBUNGEN · 第 4 版练习', 'ÜBUNGEN · Page 4 exercises'), ('C34', '读第 4 版文章，选出正确答案。', 'Read the page 4 article and choose the right answer.'), ('C34', '德国 5 分，荷兰希腊各 8 分', 'Germany 5 points, Netherlands and Greece 8 each'), ('C34', '主教练 11 月 5 日公布名单', 'the coach names the squad on 5 November'), ('C34', '贝尔格莱德空场', 'empty stadium in Belgrade'), ('C34', '首回合德国 2:0 胜塞尔维亚', 'Germany won the first leg 2–0 against Serbia'), ('C34', 'NFL 慕尼黑赛售罄', 'the Munich NFL game is sold out'), ('C34', 'Geisterspiel=空场比赛 b', 'Geisterspiel=ghost game b'), ('C34', 'Hinspiel=首回合 a', 'Hinspiel=first leg a'), ('C34', 'Ausrüster=装备赞助商 c', 'Ausrüster=kit supplier c'), ('C34', 'ausverkauft=售罄 d', 'ausverkauft=sold out d'), ('C34', '用比较级完成句子（括号里是原级）。', 'Complete with the comparative (the word in brackets is the positive form).'), ('C34', 'viel → mehr（荷兰 8 分多于德国 5 分）', "viel → mehr (the Netherlands have 8 points, more than Germany's 5)"), ('C34', 'spät → später（15:30 晚于 11:11）', 'spät → später (15.30 is later than 11.11)'), ('C34', 'leise → leiser（空场比主场安静）', 'leise → leiser (an empty stadium is quieter than a home game)'), ('C34', 'früh → früher（11 月 5 日早于 11 月 13 日）', 'früh → früher (5 November is earlier than 13 November)'), ('C34', '看上面的赛程表，选出正确答案。', 'Look at the fixture table above and choose the right answer.'), ('C34', '塞尔维亚–德国周五 20:45', 'Serbia–Germany on Friday at 20.45'), ('C34', 'NFL 周日 15:30', 'NFL on Sunday at 15.30'), ('C34', '德国–荷兰周一 20:45', 'Germany–Netherlands on Monday at 20.45'), ('C34', '拜仁–科隆周五 20:30', 'Bayern–Köln on Friday at 20.30'), ('C34', '沙尔克–斯图加特周六 17:30', 'Schalke–Stuttgart on Saturday at 17.30'), ('C56', 'JUGEND · 青年', 'JUGEND · Youth'), ('C56', 'LEVEL B1 · Laternen, Lieder & Schule · 灯笼、歌曲与学校', 'LEVEL B1 · Laternen, Lieder & Schule · Lanterns, songs and school'), ('C56', 'basteln 制作 · der Pausenhof 课间操场 · sich verkleiden 乔装打扮 · die Stimmung 气氛 · der Pirat 海盗。', 'basteln = to make, to craft · der Pausenhof = schoolyard · sich verkleiden = to dress up · die Stimmung = atmosphere · der Pirat = pirate.'), ('C56', 'SCHULWOCHE · 开学周', 'SCHULWOCHE · Back to school'), ('C56', 'die Laterne — 灯笼', 'die Laterne — lantern'), ('C56', 'basteln — 制作', 'basteln — to craft'), ('C56', 'das Lied — 歌曲', 'das Lied — song'), ('C56', 'das Kostüm — 服装', 'das Kostüm — costume'), ('C56', 'der Umzug — 游行', 'der Umzug — procession'), ('C56', 'der Stern — 星星', 'der Stern — star'), ('C56', 'MARTINSWÖRTER · 圣马丁词汇', 'MARTINSWÖRTER · St Martin'), ('C56', 'UND SIE? · 说说你自己', 'UND SIE? · And you?'), ('C56', '你小时候做过灯笼吗？11 月你唱哪首歌？写两句德语寄来。', 'Did you make a lantern as a child? What song do you sing in November? Write two German sentences!'), ('C56', 'DER WOCHENPLAN DER REDAKTION · 编辑部一周计划', "DER WOCHENPLAN DER REDAKTION · The editors' week"), ('C56', 'ÜBUNGEN · 第 5 版练习', 'ÜBUNGEN · Page 5 exercises'), ('C56', '答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Answers on page 8 · Levels mix freely — find each answer by its number'), ('C56', '读第 5 版文章，选出正确答案。', 'Read the page 5 article and choose the right answer.'), ('C56', '11 月 9 日全德复课', 'school restarts everywhere on 9 November'), ('C56', '孩子们做纸灯笼', 'children make paper lanterns'), ('C56', '纸灯笼', 'a paper lantern'), ('C56', '上午狂欢，下午圣马丁', 'carnival in the morning, St Martin in the afternoon'), ('C56', 'NFL 周日在电视上', 'the NFL on TV on Sunday'), ('C56', '周五看国家队比赛', 'watching the national team on Friday'), ('C56', '用方框里的词填空。', 'Complete with the words from the box.'), ('C56', '做灯笼', 'making lanterns'), ('C56', '唱圣马丁歌曲', 'singing St Martin songs'), ('C56', '狂欢节服装', 'a carnival costume'), ('C56', '灯笼游行', 'a lantern procession'), ('C56', '灯笼上的星星', 'the star on the lantern'), ('C56', '用 weil 连接两个句子（动词放句末）。', 'Join the two sentences with weil (the verb goes to the end).'), ('C56', 'weil 句动词置尾', 'in a weil clause the verb goes to the end'), ('C56', 'ist 置尾', 'ist goes to the end'), ('C56', 'will 置尾', 'will goes to the end'), ('C56', 'beginnt 置尾', 'beginnt goes to the end'), ('C56', '判断对错。', 'Right or wrong?'), ('C56', '11 月 9 日巴伐利亚也复课', 'Bavaria also back on 9 November'), ('C56', '灯笼游行在晚上', 'the lantern procession is in the evening'), ('C56', '孩子们唱圣马丁歌曲', 'children sing St Martin songs'), ('C56', 'VERTIEFUNG · 深读', 'VERTIEFUNG · Deep read'), ('C56', 'LEVEL B2 · Volkstrauertag & Stromsteuer · 纪念日与电力税', 'LEVEL B2 · Volkstrauertag & Stromsteuer · Remembrance day and electricity tax'), ('C56', 'gedenken 纪念 · die Kranzniederlegung 献花圈 · der stille Tag 安静日 · die Verbundenheit 联系 · die Versöhnung 和解。', 'gedenken = commemorate · die Kranzniederlegung = wreath-laying · der stille Tag = quiet day · Verbundenheit = bond · Versöhnung = reconciliation.'), ('C56', 'DIE ZAHLEN · 本周数字', 'DIE ZAHLEN · The numbers'), ('C56', '纪念日：纪念需要安静——对此几乎人人赞同。电力税：降多少尚未确定。两者都关系到几乎每个家庭。', 'Remembrance day: remembrance needs quiet — almost everyone agrees. Electricity tax: how much it falls is still open. Both affect nearly every household.'), ('C56', 'ZWEI SONNTAGE IM NOVEMBER · 十一月的两个周日', 'ZWEI SONNTAGE IM NOVEMBER · Two Sundays in November'), ('C56', 'WAS INTERESSIERT DIE LESER? · 读者最关心什么？', 'WAS INTERESSIERT DIE LESER? · What interests readers?'), ('C56', '("Nations League und NFL", 46, "足球")', '("Nations League und NFL", 46, "football")'), ('C56', '("St. Martin und Karneval", 34, "节日")', '("St. Martin und Karneval", 34, "festivals")'), ('C56', '("Volkstrauertag und Gedenken", 20, "纪念")', '("Volkstrauertag und Gedenken", 20, "remembrance")'), ('C56', 'ÜBUNGSDATEN · 练习数据 — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage.（本图数字为编辑部练习示例，非真实调查。）', 'ÜBUNGSDATEN · Practice data — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage. (Practice data from the editors, not a real survey.)'), ('C56', 'ÜBUNGEN · 第 6 版练习', 'ÜBUNGEN · Page 6 exercises'), ('C56', '看上面的练习图表，选出正确答案。', 'Use the practice chart above.'), ('C56', '46% 足球最受关注', 'football leads at 46%'), ('C56', '节日 34% 第二', 'festivals second at 34%'), ('C56', '纪念 20% 最小', 'remembrance smallest at 20%'), ('C56', '纪念 20%', 'remembrance 20%'), ('C56', '读第 6 版深读文章，选出正确答案。', 'Read the page 6 article.'), ('C56', '11 月 15 日纪念日', 'remembrance day is 15 November'), ('C56', 'ZDF 13 点半直播纪念仪式', 'ZDF live from 13.30'), ('C56', '家庭电力税 2.05 欧分', 'household electricity tax is 2.05 cents'), ('C56', '2027 年预算 11 月 27 日表决', '2027 budget vote on 27 November'), ('C56', '用括号里的形式填空。', 'Fill in with the form in brackets.'), ('C56', '被动：wird + Partizip II', 'passive: wird + past participle'), ('C56', 'ob 引导间接疑问句', 'ob introduces an indirect question'), ('C56', '献花圈仪式', 'a wreath-laying ceremony'), ('C56', '为和平与和解', 'for peace and reconciliation'), ('C56', '德奥联系', 'German–Austrian connectedness'), ('C56', '纪念受害者', 'remembering the victims'), ('C7', 'SPRACHE · 语言', 'SPRACHE · Language'), ('C7', 'A2 → B2 · Sätze der Woche & Fehlerklinik · 本周金句与纠错诊所', 'A2 → B2 · Sätze der Woche & Fehlerklinik · Sentences of the week & error clinic'), ('C7', '本版专攻语言：三节小课、本期金句（全部摘自本期文章原文）、纠错诊所和读者来信。', "This page is all about language: three short lessons, the sentences of the week (all quoted word for word from this issue's articles), the error clinic and readers' letters."), ('C7', 'BEISPIELE · 例句', 'BEISPIELE · Examples'), ('C7', '被动：wird + Partizip II', 'passive: wird + past participle'), ('C7', '复数：werden', 'plural: werden'), ('C7', 'werden + 原形表将来', 'werden + infinitive for the future'), ('C7', '被动语态', 'passive voice'), ('C7', 'lang → länger（夜晚比白天长）', 'lang → länger (the night is longer than the day)'), ('C7', 'weil 引导原因', 'weil introduces a reason'), ('C7', 'weil 句动词置尾', 'in a weil clause the verb goes to the end'), ('C7', 'länger als = 比……更长', 'länger als = longer than'), ('C7', '„Länger als sonst“ heißt... A. 比平时更长 · B. 和平时一样 · C. 比平时更短', '„Länger als sonst“ means... A. longer than usual · B. the same as usual · C. shorter than usual'), ('C7', 'ob 引导间接疑问', 'ob introduces an indirect question'), ('C7', 'Es ist fraglich, ob ... = 是否还难说', 'Es ist fraglich, ob ... = it is doubtful whether ...'), ('C7', 'dass 句动词置尾', 'in a dass clause the verb goes to the end'), ('C7', '礼貌表达观点', 'a polite way to give an opinion'), ('C7', '11.11 Uhr = 11 点 11 分', '11.11 Uhr = 11.11'), ('C7', 'vor leeren Rängen = 空场，没有观众', 'vor leeren Rängen = empty stadium'), ('C7', 'Es wird gespielt. = 比赛将进行（被动）', 'Es wird gespielt. = It will be played'), ('C7', 'Meiner Meinung nach ... = 在我看来……', 'Meiner Meinung nach = in my opinion'), ('C7', 'Ich finde, dass ... = 我觉得……', 'Ich finde, dass = I think that'), ('C7', 'Es ist fraglich, ob ... = 是否……还难说', 'Es ist fraglich, ob ... = doubtful whether'), ('C7', 'DER WERKZEUGKASTEN · 工具箱', 'DER WERKZEUGKASTEN · Toolbox'), ('C7', 'label = "Ein Beispiel der Redaktion!"', 'label = "An example from the editors!"'), ('C7', '编辑部示例，非真实来信：截稿时未收到真实来信或习作，见 VOL.4。请寄来您的习作，优秀者刊登于 VOL.4。', "Editors' example, not a real letter: no real letters had arrived by press time. Send us yours for VOL.4!"), ('C7', 'LESERBRIEFE · 读者来信', "LESERBRIEFE · Readers' letters"), ('C7', 'NOCH EIN WORT · 再学一词', 'NOCH EIN WORT · One more word'), ('C7', '«das Geisterspiel»（Seite 4）: ein Spiel ohne Zuschauer im Stadion. 空场比赛。', '«das Geisterspiel» (Seite 4): ein Spiel ohne Zuschauer im Stadion. A ghost game: a match with no spectators.'), ('C7', 'SÄTZE DER WOCHE · 本周金句', 'SÄTZE DER WOCHE · Sentences of the week'), ('C7', '原文摘录，逐字引自本期文章 · 括号内为出处', "Quoted word for word from this issue's articles · source in brackets"), ('C7', '德甲休战——但国家队要比赛。', 'The Bundesliga pauses — but the national team plays.'), ('C7', '11 点 11 分，科隆新一季狂欢季开幕。', 'At 11.11, the new carnival session begins in Cologne.'), ('C7', '他的纪念日是 11 月 11 日。', 'His memorial day is 11 November.'), ('C7', '书包收拾好了，操场上又热闹起来。', 'Bags are packed, schoolyards are loud again.'), ('C7', '十一月黑暗，但并不安静：它歌唱、发光、庆祝。', 'November is dark, but not quiet: it sings, shines and celebrates.'), ('C7', '比赛售罄，RTL 现场直播。', 'The game is sold out; RTL broadcasts live.'), ('C7', '这里的纪念意味着：停下来、记住——并为和平与和解挺身而出。', 'Here, remembrance means: pause, remember — and stand up for peace and reconciliation.'), ('C7', '周日，全国一片安静。', 'On Sunday, the country is quiet.'), ('C7', 'FEHLERKLINIK · 纠错诊所', 'FEHLERKLINIK · The error clinic'), ('C7', '学习者最常犯的四个错 · 先自己改，再看答案', 'Four mistakes learners make most often · correct them first, then check'), ('C7', '动词第二位：主语不在句首时，动词仍居第二。', 'Verb second: even when the subject is not first, the verb stays second.'), ('C7', 'halb zwölf = 十一点半（zwölf 之前）。', 'halb zwölf = 11.30, half an hour before zwölf.'), ('C7', 'Perfekt 中 Partizip II 放句末。', 'In the Perfekt, the past participle goes to the end.'), ('C7', 'ob 从句动词放句末。', 'In an ob-clause, the verb goes to the end.'), ('C7', 'IN DER NÄCHSTEN AUSGABE · 下期预告 (VOL.4)', 'IN DER NÄCHSTEN AUSGABE · Next issue (VOL.4)'), ('C8', 'ÜBUNGEN & ANTWORTEN · 练习与答案', 'ÜBUNGEN & ANTWORTEN · Exercises & answers'), ('C8', 'SCHLUSSTEST · 综合评估 · Alle Antworten unten auf dieser Seite 答案在本版下方', 'SCHLUSSTEST · Final test · Alle Antworten unten auf dieser Seite — all answers at the bottom of this page'), ('C8', 'beginnt（第三人称单数）', 'beginnt (3rd person singular)'), ('C8', 'bastelt（第三人称单数）', 'bastelt (3rd person singular)'), ('C8', 'geht（第三人称单数）', 'geht (3rd person singular)'), ('C8', 'singt（第三人称单数）', 'singt (3rd person singular)'), ('C8', 'schaut（第三人称单数）', 'schaut (3rd person singular)'), ('C8', 'sieht（第三人称单数）', 'sieht (3rd person singular)'), ('C8', 'erzählt（第三人称单数）', 'erzählt (3rd person singular)'), ('C8', 'A · LÜCKENTEXT · 完形填空', 'A · LÜCKENTEXT · Cloze'), ('C8', '选项：', 'Options:'), ('C8', 'B · WISSENSFRAGEN · 综合问答', 'B · WISSENSFRAGEN · Quiz'), ('C8', '狂欢季 11 点 11 分开幕', 'carnival opens at 11.11'), ('C8', '周五客战塞尔维亚', 'away in Serbia on Friday'), ('C8', 'NFL 周日 15:30', 'NFL on Sunday at 15.30'), ('C8', '纪念日 11 月 15 日', 'remembrance day is 15 November'), ('C8', '家庭电力税 2.05 欧分', 'household electricity tax is 2.05 cents'), ('C8', '主教练 11 月 5 日公布名单', 'the coach names the squad on 5 November'), ('C8', 'ZDF 13 点半直播纪念仪式', 'ZDF live from 13.30'), ('C8', '亡灵主日 11 月 22 日', 'Totensonntag is 22 November'), ('C8', 'C · LESEVERSTEHEN · 阅读理解', 'C · LESEVERSTEHEN · Reading'), ('C8', '周三做灯笼', 'making a lantern on Wednesday'), ('C8', '周五看德国队', 'watching Germany on Friday'), ('C8', 'D · SÄTZE BAUEN · 造句', 'D · SÄTZE BAUEN · Sentences'), ('C8', '时间状语，动词第二位', 'time phrase, verb second'), ('C8', '主谓宾顺序', 'subject–verb–object order'), ('C8', '时间状语开头，动词第二位', 'time phrase first, verb second'), ('C8', '地点时间开头，动词第二位', 'place and time first, verb second'), ('C8', 'E · ÜBERSETZEN · 翻译', 'E · ÜBERSETZEN · Translation'), ('C8', '狂欢节 11 点 11 分在科隆开幕。', 'The carnival opens at 11.11 in Cologne.'), ('C8', 'beginnen = 开始', 'beginnen = to begin'), ('C8', 'Der Karneval beginnt um 11.11 Uhr in Köln.（译成中文）', 'Der Karneval beginnt um 11.11 Uhr in Köln. (translate into English)'), ('C8', '我周三做一个灯笼。', 'I make a lantern on Wednesday.'), ('C8', 'basteln = 制作', 'basteln = to make, to craft'), ('C8', 'Ich bastle am Mittwoch eine Laterne.（译成中文）', 'Ich bastle am Mittwoch eine Laterne. (translate into English)'), ('C8', '学校 11 月 9 日又开学了。', 'School started again on 9 November.'), ('C8', 'wieder begonnen = 又开始', 'wieder begonnen = started again'), ('C8', 'Die Schule hat am 9. November wieder begonnen.（译成中文）', 'Die Schule hat am 9. November wieder begonnen. (translate into English)'), ('C8', '看比赛 = das Spiel schauen', 'to watch a game = das Spiel schauen'), ('C8', '"我周日看 NFL 比赛。（译成德语）", instr="翻译"', '"I watch the NFL game on Sunday. (translate into German)", instr="Translate into German"'), ('C8', 'F · WÖRTER PAAREN · 词汇配对', 'F · WÖRTER PAAREN · Matching'), ('C8', 'Mantel=斗篷 b', 'Mantel=cloak b'), ('C8', 'Laterne=灯笼 a', 'Laterne=lantern a'), ('C8', 'Geisterspiel=空场比赛 d', 'Geisterspiel=ghost game d'), ('C8', 'Versöhnung=和解 c', 'Versöhnung=reconciliation c'), ('C8', 'singst（第二人称单数）', 'singst (2nd person singular)'), ('C8', 'macht（第二人称复数）', 'macht (2nd person plural)'), ('C8', 'essen（第一人称复数）', 'essen (1st person plural)'), ('C8', 'machst（第二人称单数）', 'machst (2nd person singular)'), ('C8', 'schaue（第一人称单数）', 'schaue (1st person singular)'), ('C8', 'G · DIALOG · 对话补全', 'G · DIALOG · Dialogue'), ('C8', '开放题 — 要点见写作框，范文在第 8 版写作框内', 'Open task — follow the points in the writing box; the model text is in the box on this page'), ('C8', '按要点给分', 'Marked against the points listed'), ('C8', 'H · SCHREIBEN · 写作', 'H · SCHREIBEN · Writing'), ('C8', '用德语写 80–100 词：《我的十一月的一周》。写清做什么手工、看哪几场比赛、和谁一起，并写一句关于圣马丁节或纪念日的话。', "Write in German, 80–100 words: «My week in November». Say what you make, which games you watch and with whom — and add one sentence about St Martin's Day or the remembrance day."), ('C8', 'MUSTER · 范文（84 Wörter）', 'MUSTER · Model text (84 words)'), ('C8', 'ANTWORTEN · 全部答案与简析（第 1–8 版）', 'ANTWORTEN · All answers with notes (pages 1–8)')]]
exempt = []
olds = [o for o in olds if o not in exempt]
left = {}
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py", "bslib4.py"]:
    s = open(os.path.join(BASE, f), encoding="utf-8").read()
    for old in olds:
        if old in s:
            left.setdefault(f, []).append(old)
print("leftover original literals:", left if left else "NONE")
assert not left, "original literals remain after transform"

print("\n".join(LOG))
print(f"TOTAL replacements: {len(LOG)}")
