# -*- coding: utf-8 -*-
"""DE x ZH-TW fan-out transform for W46 DE core build copy.
Generated from the EN pair table + tr-zh-tw.py. German body text is
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
    rep(f, "weekly-report-w46-de-core", "weekly-report-w46-de-zh-tw", 1)

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
    '"Die Lucerna · 德語週報 VOL.3 · 正文德語 · 講解繁體中文"', 1)
rep("bslib4.py", 'f"\u7b2c {n} \u7248 / \u5171 {total} \u7248"', 'f"第 {n} 版 / 共 {total} 版"', 1)
rep("bslib4.py", '"\u8bd1\u6ce8\uff5c" + s', '"譯注｜" + s', 1)

# ================= content12.py =================
C12 = [
    ('WÖCHENTLICH AUF DEUTSCH · 每周一期 · 读德国人正在读的德语', 'WÖCHENTLICH AUF DEUTSCH · 每週一期 · 讀德國人正在讀的德語'),
    ('德 语 周 报 · VOL.3 · 国 家 队 · 圣 马 丁 · NFL', '德 語 周 報 · VOL.3 · 國 家 隊 · 聖 馬 丁 · NFL'),
    ('p.text(975, 372, "DIE WOCHENZEITUNG FÜR LERNENDE — DAS ECHTE LEBEN, AUF DEUTSCH, AUS DEUTSCHLAND", 19, "sans", False, GREY, anchor="middle")', 'p.text(975, 372, "德語正文 · 繁體中文講解 — 給繁體中文讀者的版本", 19.5, "sans", True, BRICK, anchor="middle")'),
    ('本周国家队周 · 圣马丁节与 NFL', '本週國家隊周 · 聖馬丁節與 NFL'),
    ('详见第 4 版 · Seite 4', '詳見第 4 版 · Seite 4'),
    ('DIE TOPMELDUNG · 头条', 'DIE TOPMELDUNG · 頭條'),
    ('讲解｜die Länderspielpause 国家队比赛间歇期 · das Viertelfinale 四分之一决赛 · ausverkauft 售罄。', '講解｜die Länderspielpause 國家隊比賽間歇期 · das Viertelfinale 四分之一決賽 · ausverkauft 售罄。'),
    ('DIE WOCHE IN ZAHLEN · 数字看本周', 'DIE WOCHE IN ZAHLEN · 數字看本週'),
    ('5 — Punkte hat Deutschland nach vier Spielen in der Nations League（四轮过后德国队 5 分）', '5 — Punkte hat Deutschland nach vier Spielen in der Nations League（四輪過後德國隊 5 分）'),
    ('11.11 — um 11.11 Uhr beginnt die Karnevalssession in Köln（11 点 11 分狂欢季开幕）', '11.11 — um 11.11 Uhr beginnt die Karnevalssession in Köln（11 點 11 分狂歡季開幕）'),
    ('15.30 — um 15.30 Uhr beginnt das NFL-Spiel in München（周日 15 点 30 分 NFL 开球）', '15.30 — um 15.30 Uhr beginnt das NFL-Spiel in München（週日 15 點 30 分 NFL 開球）'),
    ('JETZT ÜBEN · 即学即练', 'JETZT ÜBEN · 即學即練'),
    ('国家队比赛周', '國家隊比賽周'),
    ('塞尔维亚首都', '塞爾維亞首都'),
    ('狂欢季 11 点 11 分开幕', '狂歡季 11 點 11 分開幕'),
    ('NFL 在慕尼黑', 'NFL 在慕尼黑'),
    ('四轮 5 分', '四輪 5 分'),
    ('周日是纪念日', '週日是紀念日'),
    ('圣马丁节 11 月 11 日', '聖馬丁節 11 月 11 日'),
    ('11 月 11 日是星期三', '11 月 11 日是星期三'),
    ('本周大问题 · Die Fragen der Woche', '本週大問題 · Die Fragen der Woche'),
    ('德国本周最热议的五个问题。', '德國本週最熱議的五個問題。'),
    ('IN DIESER AUSGABE · 本期目录', 'IN DIESER AUSGABE · 本期目錄'),
    ('空场比赛（无观众）。详见第 4 版。', '空場比賽（無觀衆）。詳見第 4 版。'),
    ('KURZ & GUT · 快讯', 'KURZ & GUT · 快訊'),
    ('BLITZQUIZ · 闪电问答', 'BLITZQUIZ · 閃電問答'),
    ('读头版，选出正确答案 · 答案见第 8 版', '讀頭版，選出正確答案 · 答案見第 8 版'),
    ('周五客战塞尔维亚', '週五客戰塞爾維亞'),
    ('NFL 下午 3 点半开球', 'NFL 下午 3 點半開球'),
    ('纪念日在周日', '紀念日在週日'),
    ('LEBEN · 生活', 'LEBEN · 生活'),
    ('LEVEL A2 · Der 11. November & der Alltag · 11 月 11 日与日常生活', 'LEVEL A2 · Der 11. November & der Alltag · 11 月 11 日與日常生活'),
    ('der Jeck 狂欢者（科隆方言） · die fünfte Jahreszeit 第五个季节（狂欢季） · die Laterne 灯笼 · der Weckmann 面人面包 · die Martinsgans 圣马丁鹅。', 'der Jeck 狂歡者（科隆方言） · die fünfte Jahreszeit 第五個季節（狂歡季） · die Laterne 燈籠 · der Weckmann 麪人麪包 · die Martinsgans 聖馬丁鵝。'),
    ('DER 11. NOVEMBER · 11 月 11 日', 'DER 11. NOVEMBER · 11 月 11 日'),
    ('你过狂欢节还是圣马丁节？写两句德语寄来。', '你過狂歡節還是聖馬丁節？寫兩句德語寄來。'),
    ('UND SIE? · 说说你自己', 'UND SIE? · 說說你自己'),
    ('MARTIN IN KÜRZE · 圣马丁简讯', 'MARTIN IN KÜRZE · 聖馬丁簡訊'),
    ('RECHNEN WIR MAL · 算一算', 'RECHNEN WIR MAL · 算一算'),
    ('Die Uhrzeiten der Woche · 本周时刻', 'Die Uhrzeiten der Woche · 本週時刻'),
    ('注意：11 月 11 日是工作日。去科隆要早到：老城很挤，晚上街道属于提灯笼的孩子们。', '注意：11 月 11 日是工作日。去科隆要早到：老城很擠，晚上街道屬於提燈籠的孩子們。'),
    ('ÜBUNGEN · 第 2 版练习', 'ÜBUNGEN · 第 2 版練習'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', '答案見第 8 版 · 題目可跨級混排，按題號找答案'),
    ('看第 2 版文章，用时间填空。', '看第 2 版文章，用時間填空。'),
    ('WDR 10 点半直播', 'WDR 10 點半直播'),
    ('Weckmann 是面人面包', 'Weckmann 是麪人麪包'),
    ('11 月 11 日不是法定假日', '11 月 11 日不是法定假日'),
    ('圣马丁鹅配红甘蓝和丸子', '聖馬丁鵝配紅甘藍和丸子'),
    ('改成 Perfekt 现在完成时。', '改成 Perfekt 現在完成時。'),
    ('读第 2 版文章，选出正确答案。', '讀第 2 版文章，選出正確答案。'),
    ('Jeck=狂欢者 c', 'Jeck=狂歡者 c'),
    ('Laterne=灯笼 a', 'Laterne=燈籠 a'),
    ('Weckmann=面人面包 b', 'Weckmann=麪人麪包 b'),
    ('Martinsgans=圣马丁鹅 d', 'Martinsgans=聖馬丁鵝 d'),
]
rep_all("content12.py", C12)

# ================= content34.py =================
C34 = [
    ('KULTUR · 文化', 'KULTUR · 文化'),
    ('A2 → B1 · St. Martin, Karneval & Rückblick · 圣马丁、狂欢节与回顾', 'A2 → B1 · St. Martin, Karneval & Rückblick · 聖馬丁、狂歡節與回顧'),
    ('der Bettler 乞丐 · der Mantel 斗篷 · das Geschnatter 鹅叫声 · der Gänsestall 鹅棚 · das Dreigestirn 狂欢节三人组。', 'der Bettler 乞丐 · der Mantel 斗篷 · das Geschnatter 鵝叫聲 · der Gänsestall 鵝棚 · das Dreigestirn 狂歡節三人組。'),
    ('ST. MARTIN · 圣马丁', 'ST. MARTIN · 聖馬丁'),
    ('die Laterne — 灯笼', 'die Laterne — 燈籠'),
    ('der Mantel — 斗篷', 'der Mantel — 斗篷'),
    ('die Gans — 鹅', 'die Gans — 鵝'),
    ('der Weckmann — 面人面包', 'der Weckmann — 麪人麪包'),
    ('das Martinsfeuer — 圣马丁篝火', 'das Martinsfeuer — 聖馬丁篝火'),
    ('das Kostüm — 服装', 'das Kostüm — 服裝'),
    ('MARTINSWÖRTER · 圣马丁词汇', 'MARTINSWÖRTER · 聖馬丁詞彙'),
    ('UND SIE? · 说说你自己', 'UND SIE? · 說說你自己'),
    ('你做过灯笼吗？你们国家的孩子唱什么歌？写两句德语寄来。', '你做過燈籠嗎？你們國家的孩子唱什麼歌？寫兩句德語寄來。'),
    ('DER TIPP · 编辑部建议', 'DER TIPP · 編輯部建議'),
    ('ÜBUNGEN · 第 3 版练习', 'ÜBUNGEN · 第 3 版練習'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', '答案見第 8 版 · 題目可跨級混排，按題號找答案'),
    ('读第 3 版文章，判断对错。', '讀第 3 版文章，判斷對錯。'),
    ('传说马丁是罗马士兵', '傳說馬丁是羅馬士兵'),
    ('传说鹅叫声暴露了他', '傳說鵝叫聲暴露了他'),
    ('纪念日 11 月 11 日', '紀念日 11 月 11 日'),
    ('截稿时 11 月 3–8 日结果未知', '截稿時 11 月 3–8 日結果未知'),
    ('狂欢季 11 点 11 分开幕', '狂歡季 11 點 11 分開幕'),
    ('用方框里的词填空。', '用方框裏的詞填空。'),
    ('斗篷分给乞丐', '斗篷分給乞丐'),
    ('纸灯笼', '紙燈籠'),
    ('圣马丁鹅', '聖馬丁鵝'),
    ('圣马丁鹅配红甘蓝和丸子', '聖馬丁鵝配紅甘藍和丸子'),
    ('狂欢节服装', '狂歡節服裝'),
    ('游行在篝火处结束', '遊行在篝火處結束'),
    ('选出正确答案。', '選出正確答案。'),
    ('马丁后来成为图尔主教', '馬丁後來成爲圖爾主教'),
    ('灯笼游行常在前后晚上举行', '燈籠遊行常在前後晚上舉行'),
    ('VOL.4 报道 11 月 3–8 日结果', 'VOL.4 報道 11 月 3–8 日結果'),
    ('把词组成正确的句子。', '把詞組成正確的句子。'),
    ('主谓宾顺序', '主謂賓順序'),
    ('时间状语开头，动词第二位', '時間狀語開頭，動詞第二位'),
    ('地点开头，动词第二位', '地點開頭，動詞第二位'),
    ('SPORT · 体育', 'SPORT · 體育'),
    ('LEVEL B1 · Nationalelf & NFL · 国家队与 NFL', 'LEVEL B1 · Nationalelf & NFL · 國家隊與 NFL'),
    ('das Geisterspiel 空场比赛 · das Hinspiel 首回合 · ausverkauft 售罄 · der Star 明星 · gewinnen 获胜。', 'das Geisterspiel 空場比賽 · das Hinspiel 首回合 · ausverkauft 售罄 · der Star 明星 · gewinnen 獲勝。'),
    ('你更爱看足球还是美式橄榄球？贝尔格莱德谁赢？写两句德语寄来。', '你更愛看足球還是美式橄欖球？貝爾格萊德誰贏？寫兩句德語寄來。'),
    ('DER SPIELPLAN · 本周与下周赛程', 'DER SPIELPLAN · 本週與下週賽程'),
    ('ÜBUNGEN · 第 4 版练习', 'ÜBUNGEN · 第 4 版練習'),
    ('读第 4 版文章，选出正确答案。', '讀第 4 版文章，選出正確答案。'),
    ('德国 5 分，荷兰希腊各 8 分', '德國 5 分，荷蘭希臘各 8 分'),
    ('主教练 11 月 5 日公布名单', '主教練 11 月 5 日公佈名單'),
    ('贝尔格莱德空场', '貝爾格萊德空場'),
    ('首回合德国 2:0 胜塞尔维亚', '首回合德國 2:0 勝塞爾維亞'),
    ('NFL 慕尼黑赛售罄', 'NFL 慕尼黑賽售罄'),
    ('Geisterspiel=空场比赛 b', 'Geisterspiel=空場比賽 b'),
    ('Hinspiel=首回合 a', 'Hinspiel=首回合 a'),
    ('Ausrüster=装备赞助商 c', 'Ausrüster=裝備贊助商 c'),
    ('ausverkauft=售罄 d', 'ausverkauft=售罄 d'),
    ('用比较级完成句子（括号里是原级）。', '用比較級完成句子（括號裏是原級）。'),
    ('viel → mehr（荷兰 8 分多于德国 5 分）', 'viel → mehr（荷蘭 8 分多於德國 5 分）'),
    ('spät → später（15:30 晚于 11:11）', 'spät → später（15:30 晚於 11:11）'),
    ('leise → leiser（空场比主场安静）', 'leise → leiser（空場比主場安靜）'),
    ('früh → früher（11 月 5 日早于 11 月 13 日）', 'früh → früher（11 月 5 日早於 11 月 13 日）'),
    ('看上面的赛程表，选出正确答案。', '看上面的賽程表，選出正確答案。'),
    ('塞尔维亚–德国周五 20:45', '塞爾維亞–德國週五 20:45'),
    ('NFL 周日 15:30', 'NFL 週日 15:30'),
    ('德国–荷兰周一 20:45', '德國–荷蘭週一 20:45'),
    ('拜仁–科隆周五 20:30', '拜仁–科隆週五 20:30'),
    ('沙尔克–斯图加特周六 17:30', '沙爾克–斯圖加特週六 17:30'),
]
rep_all("content34.py", C34)

# ================= content56.py =================
C56 = [
    ('JUGEND · 青年', 'JUGEND · 青年'),
    ('LEVEL B1 · Laternen, Lieder & Schule · 灯笼、歌曲与学校', 'LEVEL B1 · Laternen, Lieder & Schule · 燈籠、歌曲與學校'),
    ('basteln 制作 · der Pausenhof 课间操场 · sich verkleiden 乔装打扮 · die Stimmung 气氛 · der Pirat 海盗。', 'basteln 製作 · der Pausenhof 課間操場 · sich verkleiden 喬裝打扮 · die Stimmung 氣氛 · der Pirat 海盜。'),
    ('SCHULWOCHE · 开学周', 'SCHULWOCHE · 開學周'),
    ('die Laterne — 灯笼', 'die Laterne — 燈籠'),
    ('basteln — 制作', 'basteln — 製作'),
    ('das Lied — 歌曲', 'das Lied — 歌曲'),
    ('das Kostüm — 服装', 'das Kostüm — 服裝'),
    ('der Umzug — 游行', 'der Umzug — 遊行'),
    ('der Stern — 星星', 'der Stern — 星星'),
    ('MARTINSWÖRTER · 圣马丁词汇', 'MARTINSWÖRTER · 聖馬丁詞彙'),
    ('UND SIE? · 说说你自己', 'UND SIE? · 說說你自己'),
    ('你小时候做过灯笼吗？11 月你唱哪首歌？写两句德语寄来。', '你小時候做過燈籠嗎？11 月你唱哪首歌？寫兩句德語寄來。'),
    ('DER WOCHENPLAN DER REDAKTION · 编辑部一周计划', 'DER WOCHENPLAN DER REDAKTION · 編輯部一週計劃'),
    ('ÜBUNGEN · 第 5 版练习', 'ÜBUNGEN · 第 5 版練習'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', '答案見第 8 版 · 題目可跨級混排，按題號找答案'),
    ('读第 5 版文章，选出正确答案。', '讀第 5 版文章，選出正確答案。'),
    ('11 月 9 日全德复课', '11 月 9 日全德復課'),
    ('孩子们做纸灯笼', '孩子們做紙燈籠'),
    ('纸灯笼', '紙燈籠'),
    ('上午狂欢，下午圣马丁', '上午狂歡，下午聖馬丁'),
    ('NFL 周日在电视上', 'NFL 週日在電視上'),
    ('周五看国家队比赛', '週五看國家隊比賽'),
    ('用方框里的词填空。', '用方框裏的詞填空。'),
    ('做灯笼', '做燈籠'),
    ('唱圣马丁歌曲', '唱聖馬丁歌曲'),
    ('狂欢节服装', '狂歡節服裝'),
    ('灯笼游行', '燈籠遊行'),
    ('灯笼上的星星', '燈籠上的星星'),
    ('用 weil 连接两个句子（动词放句末）。', '用 weil 連接兩個句子（動詞放句末）。'),
    ('weil 句动词置尾', 'weil 句動詞置尾'),
    ('ist 置尾', 'ist 置尾'),
    ('will 置尾', 'will 置尾'),
    ('beginnt 置尾', 'beginnt 置尾'),
    ('判断对错。', '判斷對錯。'),
    ('11 月 9 日巴伐利亚也复课', '11 月 9 日巴伐利亞也復課'),
    ('灯笼游行在晚上', '燈籠遊行在晚上'),
    ('孩子们唱圣马丁歌曲', '孩子們唱聖馬丁歌曲'),
    ('VERTIEFUNG · 深读', 'VERTIEFUNG · 深讀'),
    ('LEVEL B2 · Volkstrauertag & Stromsteuer · 纪念日与电力税', 'LEVEL B2 · Volkstrauertag & Stromsteuer · 紀念日與電力稅'),
    ('gedenken 纪念 · die Kranzniederlegung 献花圈 · der stille Tag 安静日 · die Verbundenheit 联系 · die Versöhnung 和解。', 'gedenken 紀念 · die Kranzniederlegung 獻花圈 · der stille Tag 安靜日 · die Verbundenheit 聯繫 · die Versöhnung 和解。'),
    ('DIE ZAHLEN · 本周数字', 'DIE ZAHLEN · 本週數字'),
    ('纪念日：纪念需要安静——对此几乎人人赞同。电力税：降多少尚未确定。两者都关系到几乎每个家庭。', '紀念日：紀念需要安靜——對此幾乎人人贊同。電力稅：降多少尚未確定。兩者都關係到幾乎每個家庭。'),
    ('ZWEI SONNTAGE IM NOVEMBER · 十一月的两个周日', 'ZWEI SONNTAGE IM NOVEMBER · 十一月的兩個週日'),
    ('WAS INTERESSIERT DIE LESER? · 读者最关心什么？', 'WAS INTERESSIERT DIE LESER? · 讀者最關心什麼？'),
    ('("Nations League und NFL", 46, "足球")', '("Nations League und NFL", 46, "足球")'),
    ('("St. Martin und Karneval", 34, "节日")', '("St. Martin und Karneval", 34, "節日")'),
    ('("Volkstrauertag und Gedenken", 20, "纪念")', '("Volkstrauertag und Gedenken", 20, "紀念")'),
    ('ÜBUNGSDATEN · 练习数据 — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage.（本图数字为编辑部练习示例，非真实调查。）', 'ÜBUNGSDATEN · 練習數據 — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage.（本圖數字爲編輯部練習示例，非真實調查。）'),
    ('ÜBUNGEN · 第 6 版练习', 'ÜBUNGEN · 第 6 版練習'),
    ('看上面的练习图表，选出正确答案。', '看上面的練習圖表，選出正確答案。'),
    ('46% 足球最受关注', '46% 足球最受關注'),
    ('节日 34% 第二', '節日 34% 第二'),
    ('纪念 20% 最小', '紀念 20% 最小'),
    ('纪念 20%', '紀念 20%'),
    ('读第 6 版深读文章，选出正确答案。', '讀第 6 版深讀文章，選出正確答案。'),
    ('11 月 15 日纪念日', '紀念日 11 月 15 日'),
    ('ZDF 13 点半直播纪念仪式', 'ZDF 13 點半直播紀念儀式'),
    ('家庭电力税 2.05 欧分', '家庭電力稅 2.05 歐分'),
    ('2027 年预算 11 月 27 日表决', '2027 年預算 11 月 27 日表決'),
    ('用括号里的形式填空。', '用括號裏的形式填空。'),
    ('被动：wird + Partizip II', '被動：wird + Partizip II'),
    ('ob 引导间接疑问句', 'ob 引導間接疑問'),
    ('献花圈仪式', '獻花圈儀式'),
    ('为和平与和解', '爲和平與和解'),
    ('德奥联系', '德奧聯繫'),
    ('纪念受害者', '紀念受害者'),
]
rep_all("content56.py", C56)

# ================= content7.py =================
C7 = [
    ('SPRACHE · 语言', 'SPRACHE · 語言'),
    ('A2 → B2 · Sätze der Woche & Fehlerklinik · 本周金句与纠错诊所', 'A2 → B2 · Sätze der Woche & Fehlerklinik · 本週金句與糾錯診所'),
    ('本版专攻语言：三节小课、本期金句（全部摘自本期文章原文）、纠错诊所和读者来信。', '本版專攻語言：三節小課、本期金句（全部摘自本期文章原文）、糾錯診所和讀者來信。'),
    ('BEISPIELE · 例句', 'BEISPIELE · 例句'),
    ('被动：wird + Partizip II', '被動：wird + Partizip II'),
    ('复数：werden', '複數：werden'),
    ('werden + 原形表将来', 'werden + 原形表將來'),
    ('被动语态', '被動語態'),
    ('lang → länger（夜晚比白天长）', 'lang → länger（夜晚比白天長）'),
    ('weil 引导原因', 'weil 引導原因'),
    ('weil 句动词置尾', 'weil 句動詞置尾'),
    ('länger als = 比……更长', 'länger als = 比……更長'),
    ('„Länger als sonst“ heißt... A. 比平时更长 · B. 和平时一样 · C. 比平时更短', '„Länger als sonst“ heißt... A. 比平時更長 · B. 和平時一樣 · C. 比平時更短'),
    ('ob 引导间接疑问', 'ob 引導間接疑問'),
    ('Es ist fraglich, ob ... = 是否还难说', 'Es ist fraglich, ob ... = 是否還難說'),
    ('dass 句动词置尾', 'dass 句動詞置尾'),
    ('礼貌表达观点', '禮貌表達觀點'),
    ('11.11 Uhr = 11 点 11 分', '11.11 Uhr = 11 點 11 分'),
    ('vor leeren Rängen = 空场，没有观众', 'vor leeren Rängen = 空場，沒有觀衆'),
    ('Es wird gespielt. = 比赛将进行（被动）', 'Es wird gespielt. = 比賽將進行（被動）'),
    ('Meiner Meinung nach ... = 在我看来……', 'Meiner Meinung nach ... = 在我看來……'),
    ('Ich finde, dass ... = 我觉得……', 'Ich finde, dass ... = 我覺得……'),
    ('Es ist fraglich, ob ... = 是否……还难说', 'Es ist fraglich, ob ... = 是否……還難說'),
    ('DER WERKZEUGKASTEN · 工具箱', 'DER WERKZEUGKASTEN · 工具箱'),
    ('label = "Ein Beispiel der Redaktion!"', 'label = "Ein Beispiel der Redaktion!"'),
    ('编辑部示例，非真实来信：截稿时未收到真实来信或习作，见 VOL.4。请寄来您的习作，优秀者刊登于 VOL.4。', '編輯部示例，非真實來信：截稿時未收到真實來信或習作，見 VOL.4。請寄來您的習作，優秀者刊登於 VOL.4。'),
    ('LESERBRIEFE · 读者来信', 'LESERBRIEFE · 讀者來信'),
    ('NOCH EIN WORT · 再学一词', 'NOCH EIN WORT · 再學一詞'),
    ('«das Geisterspiel»（Seite 4）: ein Spiel ohne Zuschauer im Stadion. 空场比赛。', '«das Geisterspiel»（Seite 4）: ein Spiel ohne Zuschauer im Stadion. 空場比賽。'),
    ('SÄTZE DER WOCHE · 本周金句', 'SÄTZE DER WOCHE · 本週金句'),
    ('原文摘录，逐字引自本期文章 · 括号内为出处', '原文摘錄，逐字引自本期文章 · 括號內爲出處'),
    ('德甲休战——但国家队要比赛。', '德甲休戰——但國家隊要比賽。'),
    ('11 点 11 分，科隆新一季狂欢季开幕。', '11 點 11 分，科隆新一季狂歡季開幕。'),
    ('他的纪念日是 11 月 11 日。', '他的紀念日是 11 月 11 日。'),
    ('书包收拾好了，操场上又热闹起来。', '書包收拾好了，操場上又熱鬧起來。'),
    ('十一月黑暗，但并不安静：它歌唱、发光、庆祝。', '十一月黑暗，但並不安靜：它歌唱、發光、慶祝。'),
    ('比赛售罄，RTL 现场直播。', '比賽售罄，RTL 現場直播。'),
    ('这里的纪念意味着：停下来、记住——并为和平与和解挺身而出。', '這裏的紀念意味著：停下來、記住——併爲和平與和解挺身而出。'),
    ('周日，全国一片安静。', '週日，全國一片安靜。'),
    ('FEHLERKLINIK · 纠错诊所', 'FEHLERKLINIK · 糾錯診所'),
    ('学习者最常犯的四个错 · 先自己改，再看答案', '學習者最常犯的四個錯 · 先自己改，再看答案'),
    ('动词第二位：主语不在句首时，动词仍居第二。', '動詞第二位：主語不在句首時，動詞仍居第二。'),
    ('halb zwölf = 十一点半（zwölf 之前）。', 'halb zwölf = 十一點半（zwölf 之前）。'),
    ('Perfekt 中 Partizip II 放句末。', 'Perfekt 中 Partizip II 放句末。'),
    ('ob 从句动词放句末。', 'ob 從句動詞放句末。'),
    ('IN DER NÄCHSTEN AUSGABE · 下期预告 (VOL.4)', 'IN DER NÄCHSTEN AUSGABE · 下期預告 (VOL.4)'),
]
rep_all("content7.py", C7)

# ================= content8.py =================
C8 = [
    ('ÜBUNGEN & ANTWORTEN · 练习与答案', 'ÜBUNGEN & ANTWORTEN · 練習與答案'),
    ('SCHLUSSTEST · 综合评估 · Alle Antworten unten auf dieser Seite 答案在本版下方', 'SCHLUSSTEST · 綜合評估 · Alle Antworten unten auf dieser Seite 答案在本版下方'),
    ('beginnt（第三人称单数）', 'beginnt(第三人稱單數)'),
    ('bastelt（第三人称单数）', 'bastelt(第三人稱單數)'),
    ('geht（第三人称单数）', 'geht(第三人稱單數)'),
    ('singt（第三人称单数）', 'singt(第三人稱單數)'),
    ('schaut（第三人称单数）', 'schaut(第三人稱單數)'),
    ('sieht（第三人称单数）', 'sieht(第三人稱單數)'),
    ('erzählt（第三人称单数）', 'erzählt(第三人稱單數)'),
    ('A · LÜCKENTEXT · 完形填空', 'A · LÜCKENTEXT · 完形填空'),
    ('选项：', '選項：'),
    ('B · WISSENSFRAGEN · 综合问答', 'B · WISSENSFRAGEN · 綜合問答'),
    ('狂欢季 11 点 11 分开幕', '狂歡季 11 點 11 分開幕'),
    ('周五客战塞尔维亚', '週五客戰塞爾維亞'),
    ('NFL 周日 15:30', 'NFL 週日 15:30'),
    ('纪念日 11 月 15 日', '紀念日 11 月 15 日'),
    ('家庭电力税 2.05 欧分', '家庭電力稅 2.05 歐分'),
    ('主教练 11 月 5 日公布名单', '主教練 11 月 5 日公佈名單'),
    ('ZDF 13 点半直播纪念仪式', 'ZDF 13 點半直播紀念儀式'),
    ('亡灵主日 11 月 22 日', '亡靈主日 11 月 22 日'),
    ('C · LESEVERSTEHEN · 阅读理解', 'C · LESEVERSTEHEN · 閱讀理解'),
    ('周三做灯笼', '週三做燈籠'),
    ('周五看德国队', '週五看德國隊'),
    ('D · SÄTZE BAUEN · 造句', 'D · SÄTZE BAUEN · 造句'),
    ('时间状语，动词第二位', '時間狀語，動詞第二位'),
    ('主谓宾顺序', '主謂賓順序'),
    ('时间状语开头，动词第二位', '時間狀語開頭，動詞第二位'),
    ('地点时间开头，动词第二位', '地點時間開頭，動詞第二位'),
    ('E · ÜBERSETZEN · 翻译', 'E · ÜBERSETZEN · 翻譯'),
    ('狂欢节 11 点 11 分在科隆开幕。', '狂歡節 11 點 11 分在科隆開幕。'),
    ('beginnen = 开始', 'beginnen = 開始'),
    ('Der Karneval beginnt um 11.11 Uhr in Köln.（译成中文）', 'Der Karneval beginnt um 11.11 Uhr in Köln.（譯成中文）'),
    ('我周三做一个灯笼。', '我週三做一個燈籠。'),
    ('basteln = 制作', 'basteln = 製作'),
    ('Ich bastle am Mittwoch eine Laterne.（译成中文）', 'Ich bastle am Mittwoch eine Laterne.（譯成中文）'),
    ('学校 11 月 9 日又开学了。', '學校 11 月 9 日又開學了。'),
    ('wieder begonnen = 又开始', 'wieder begonnen = 又開始'),
    ('Die Schule hat am 9. November wieder begonnen.（译成中文）', 'Die Schule hat am 9. November wieder begonnen.（譯成中文）'),
    ('看比赛 = das Spiel schauen', '看比賽 = das Spiel schauen'),
    ('"我周日看 NFL 比赛。（译成德语）", instr="翻译"', '"我週日看 NFL 比賽。（譯成德語）", instr="翻譯"'),
    ('F · WÖRTER PAAREN · 词汇配对', 'F · WÖRTER PAAREN · 詞彙配對'),
    ('Mantel=斗篷 b', 'Mantel=斗篷 b'),
    ('Laterne=灯笼 a', 'Laterne=燈籠 a'),
    ('Geisterspiel=空场比赛 d', 'Geisterspiel=空場比賽 d'),
    ('Versöhnung=和解 c', 'Versöhnung=和解 c'),
    ('singst（第二人称单数）', 'singst(第二人稱單數)'),
    ('macht（第二人称复数）', 'macht(第二人稱複數)'),
    ('essen（第一人称复数）', 'essen(第一人稱複數)'),
    ('machst（第二人称单数）', 'machst(第二人稱單數)'),
    ('schaue（第一人称单数）', 'schaue(第一人稱單數)'),
    ('G · DIALOG · 对话补全', 'G · DIALOG · 對話補全'),
    ('开放题 — 要点见写作框，范文在第 8 版写作框内', '開放題 — 要點見寫作框，範文在第 8 版寫作框內'),
    ('按要点给分', '按要點給分'),
    ('H · SCHREIBEN · 写作', 'H · SCHREIBEN · 寫作'),
    ('用德语写 80–100 词：《我的十一月的一周》。写清做什么手工、看哪几场比赛、和谁一起，并写一句关于圣马丁节或纪念日的话。', '用德語寫 80–100 詞：《我的十一月的一週》。寫清做什麼手工、看哪幾場比賽、和誰一起，並寫一句關於聖馬丁節或紀念日的話。'),
    ('MUSTER · 范文（84 Wörter）', 'MUSTER · 範本（84 Wörter）'),
    ('ANTWORTEN · 全部答案与简析（第 1–8 版）', 'ANTWORTEN · 全部答案與簡析（第 1–8 版）'),
]
rep_all("content8.py", C8)

# ---------- P8 keys ----------
rep("content8.py", 'kf.para(f"— \u7b2c {pg} \u7248 —", 17, "sans", True, OLIVE, 1.28, 3)',
    'kf.para(f"— 第 {pg} 版 —", 17, "sans", True, OLIVE, 1.28, 3)', 1)
rep("content8.py", 's += f"\uff08{e[\'note\']}\uff09"',
    's += f" ({e[\'note\']})"', 1)
rep("content8.py", 'kf.para(" · ".join(parts), 14.5, "sans", False, INK, 1.3, 9)',
    'kf.para(" · ".join(parts), 14.5, "sans", False, INK, 1.3, 9)', 1)

# ---------- generic value maps ----------
TYPEMAP = [('完成句子', '完成句子'), ('单选', '單選'), ('句型转换', '句型轉換'), ('词汇配对', '詞彙配對'), ('判断对错', '判斷對錯'), ('完形填空', '完形填空'), ('造句', '造句'), ('对话补全', '對話補全'), ('翻译', '翻譯'), ('写作', '寫作')]
INSTRMAP = [('instr="填空"', 'instr="填空"'), ('instr="改写"', 'instr="改寫"'), ('instr="判断"', 'instr="判斷"'), ('instr="造句"', 'instr="造句"'), ('instr="翻译"', 'instr="翻譯"'), ('instr="把词和释义配对"', 'instr="把詞和釋義配對"')]
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
exempt = ['("Nations League und NFL", 46, "足球")', '11 月 11 日不是法定假日', '11 月 11 日是星期三', 'A · LÜCKENTEXT · 完形填空', 'BEISPIELE · 例句', 'D · SÄTZE BAUEN · 造句', 'DER 11. NOVEMBER · 11 月 11 日', 'DER WERKZEUGKASTEN · 工具箱', 'Hinspiel=首回合 a', 'JUGEND · 青年', 'KULTUR · 文化', 'LEBEN · 生活', 'Mantel=斗篷 b', 'NFL 在慕尼黑', 'Perfekt 中 Partizip II 放句末。', 'RECHNEN WIR MAL · 算一算', 'Versöhnung=和解 c', 'ausverkauft=售罄 d', 'beginnt 置尾', 'das Lied — 歌曲', 'der Mantel — 斗篷', 'der Stern — 星星', 'ist 置尾', 'label = "Ein Beispiel der Redaktion!"', 'will 置尾']
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
