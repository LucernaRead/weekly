# -*- coding: utf-8 -*-
"""DE x JA fan-out transform for W46 DE core build copy.
Generated from the EN pair table + tr-ja.py. German body text is
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
    rep(f, "weekly-report-w46-de-core", "weekly-report-w46-de-ja", 1)

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
    '"Die Lucerna · ドイツ語週刊 VOL.3 · 本文はドイツ語 · 解説は日本語"', 1)
rep("bslib4.py", 'f"\u7b2c {n} \u7248 / \u5171 {total} \u7248"', 'f"{n} ページ（全 {total} ページ）"', 1)
rep("bslib4.py", '"\u8bd1\u6ce8\uff5c" + s', '"解説 — " + s', 1)

# ================= content12.py =================
C12 = [
    ('WÖCHENTLICH AUF DEUTSCH · 每周一期 · 读德国人正在读的德语', 'WÖCHENTLICH AUF DEUTSCH · 毎週一号 · ドイツ人が読んでいるドイツ語を読む'),
    ('德 语 周 报 · VOL.3 · 国 家 队 · 圣 马 丁 · NFL', 'ド イ ツ 語 週 刊 · VOL.3 · 代 表 · 聖マルティン · NFL'),
    ('p.text(975, 372, "DIE WOCHENZEITUNG FÜR LERNENDE — DAS ECHTE LEBEN, AUF DEUTSCH, AUS DEUTSCHLAND", 19, "sans", False, GREY, anchor="middle")', 'p.text(975, 372, "ドイツ語テキスト · 日本語の解説 — 日本語読者のための版", 19.5, "sans", True, BRICK, anchor="middle")'),
    ('本周国家队周 · 圣马丁节与 NFL', '代表週間 · 聖マルティンとNFL'),
    ('详见第 4 版 · Seite 4', '4ページ参照'),
    ('DIE TOPMELDUNG · 头条', 'DIE TOPMELDUNG · トップ記事'),
    ('讲解｜die Länderspielpause 国家队比赛间歇期 · das Viertelfinale 四分之一决赛 · ausverkauft 售罄。', '解説 — die Länderspielpause＝代表戦中断期間 · das Viertelfinale＝準々決勝 · ausverkauft＝完売。'),
    ('DIE WOCHE IN ZAHLEN · 数字看本周', 'DIE WOCHE IN ZAHLEN · 数字'),
    ('5 — Punkte hat Deutschland nach vier Spielen in der Nations League（四轮过后德国队 5 分）', '5 — Punkte hat Deutschland nach vier Spielen in der Nations League（ドイツは4試合で勝ち点5）'),
    ('11.11 — um 11.11 Uhr beginnt die Karnevalssession in Köln（11 点 11 分狂欢季开幕）', '11.11 — um 11.11 Uhr beginnt die Karnevalssession in Köln（カーニバル・シーズンは11時11分に開幕）'),
    ('15.30 — um 15.30 Uhr beginnt das NFL-Spiel in München（周日 15 点 30 分 NFL 开球）', '15.30 — um 15.30 Uhr beginnt das NFL-Spiel in München（NFLの試合は日曜15時30分開始）'),
    ('JETZT ÜBEN · 即学即练', 'JETZT ÜBEN · 練習しましょう'),
    ('国家队比赛周', '代表戦中断の週'),
    ('塞尔维亚首都', 'セルビアの首都'),
    ('狂欢季 11 点 11 分开幕', 'カーニバルは11時11分に開幕'),
    ('NFL 在慕尼黑', 'ミュンヘンのNFL'),
    ('四轮 5 分', '4試合で勝ち点5'),
    ('周日是纪念日', '日曜日は追悼の日'),
    ('圣马丁节 11 月 11 日', '聖マルティンの日は11月11日'),
    ('11 月 11 日是星期三', '11月11日は水曜日'),
    ('本周大问题 · Die Fragen der Woche', '大きな問い · Die Fragen der Woche'),
    ('德国本周最热议的五个问题。', '今週ドイツをにぎわせる5つの問い。'),
    ('IN DIESER AUSGABE · 本期目录', 'IN DIESER AUSGABE · 目次'),
    ('空场比赛（无观众）。详见第 4 版。', '観客のいない試合。4ページ参照。'),
    ('KURZ & GUT · 快讯', 'KURZ & GUT · 短く'),
    ('BLITZQUIZ · 闪电问答', 'BLITZQUIZ · 早押しクイズ'),
    ('读头版，选出正确答案 · 答案见第 8 版', '1ページを読んで正しい答えを選びましょう · 答えは8ページ'),
    ('周五客战塞尔维亚', '金曜日にセルビアでアウェー戦'),
    ('NFL 下午 3 点半开球', 'NFLは15時30分開始'),
    ('纪念日在周日', '追悼の日は日曜日'),
    ('LEBEN · 生活', 'LEBEN · 生活'),
    ('LEVEL A2 · Der 11. November & der Alltag · 11 月 11 日与日常生活', 'LEVEL A2 · Der 11. November & der Alltag · 11月11日と日常生活'),
    ('der Jeck 狂欢者（科隆方言） · die fünfte Jahreszeit 第五个季节（狂欢季） · die Laterne 灯笼 · der Weckmann 面人面包 · die Martinsgans 圣马丁鹅。', 'der Jeck＝カーニバルの浮かれ者（ケルン方言） · die fünfte Jahreszeit＝第5の季節（カーニバル） · die Laterne＝ランタン · der Weckmann＝パン人形 · die Martinsgans＝聖マルティンのガチョウ。'),
    ('DER 11. NOVEMBER · 11 月 11 日', 'DER 11. NOVEMBER'),
    ('你过狂欢节还是圣马丁节？写两句德语寄来。', 'カーニバルと聖マルティン、どちらを祝いますか。ドイツ語で2文書きましょう。'),
    ('UND SIE? · 说说你自己', 'UND SIE? · あなたは？'),
    ('MARTIN IN KÜRZE · 圣马丁简讯', 'MARTIN IN KÜRZE · 概要'),
    ('RECHNEN WIR MAL · 算一算', 'RECHNEN WIR MAL · 計算してみよう'),
    ('Die Uhrzeiten der Woche · 本周时刻', 'Die Uhrzeiten der Woche · 今週の時刻'),
    ('注意：11 月 11 日是工作日。去科隆要早到：老城很挤，晚上街道属于提灯笼的孩子们。', '注意：11月11日は平日です。ケルンには早めに着きましょう。旧市街は混み、夕方はランタンを持った子どもたちの街になります。'),
    ('ÜBUNGEN · 第 2 版练习', 'ÜBUNGEN · 2ページの練習'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', '答えは8ページ · レベルは混ざっています。番号で答えを探しましょう'),
    ('看第 2 版文章，用时间填空。', '2ページの記事を読んで、時刻を書き入れましょう。'),
    ('WDR 10 点半直播', 'WDRは10時30分から生中継'),
    ('Weckmann 是面人面包', 'ヴェックマンはパン人形'),
    ('11 月 11 日不是法定假日', '11月11日は祝日ではない'),
    ('圣马丁鹅配红甘蓝和丸子', '赤キャベツと団子添えの聖マルティンのガチョウ'),
    ('改成 Perfekt 现在完成时。', 'Perfekt（現在完了）で書きかえましょう。'),
    ('读第 2 版文章，选出正确答案。', '2ページの記事を読んで、正しい答えを選びましょう。'),
    ('Jeck=狂欢者 c', 'Jeck=カーニバルの浮かれ者 c'),
    ('Laterne=灯笼 a', 'Laterne=ランタン a'),
    ('Weckmann=面人面包 b', 'Weckmann=パン人形 b'),
    ('Martinsgans=圣马丁鹅 d', 'Martinsgans=聖マルティンのガチョウ d'),
]
rep_all("content12.py", C12)

# ================= content34.py =================
C34 = [
    ('KULTUR · 文化', 'KULTUR · 文化'),
    ('A2 → B1 · St. Martin, Karneval & Rückblick · 圣马丁、狂欢节与回顾', 'A2 → B1 · St. Martin, Karneval & Rückblick · 聖マルティン、カーニバル、振り返り'),
    ('der Bettler 乞丐 · der Mantel 斗篷 · das Geschnatter 鹅叫声 · der Gänsestall 鹅棚 · das Dreigestirn 狂欢节三人组。', 'der Bettler＝物乞い · der Mantel＝マント · das Geschnatter＝ガーガー鳴くこと · der Gänsestall＝ガチョウ小屋 · das Dreigestirn＝カーニバルの三役。'),
    ('ST. MARTIN · 圣马丁', 'ST. MARTIN · 聖マルティン'),
    ('die Laterne — 灯笼', 'die Laterne — ランタン'),
    ('der Mantel — 斗篷', 'der Mantel — マント'),
    ('die Gans — 鹅', 'die Gans — ガチョウ'),
    ('der Weckmann — 面人面包', 'der Weckmann — パン人形'),
    ('das Martinsfeuer — 圣马丁篝火', 'das Martinsfeuer — 聖マルティンの焚き火'),
    ('das Kostüm — 服装', 'das Kostüm — 衣装'),
    ('MARTINSWÖRTER · 圣马丁词汇', 'MARTINSWÖRTER · 聖マルティン'),
    ('UND SIE? · 说说你自己', 'UND SIE? · あなたは？'),
    ('你做过灯笼吗？你们国家的孩子唱什么歌？写两句德语寄来。', 'ランタンを作ったことがありますか。ドイツ語で2文書こう。'),
    ('DER TIPP · 编辑部建议', 'DER TIPP · 助言'),
    ('ÜBUNGEN · 第 3 版练习', 'ÜBUNGEN · 3ページの練習'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', '答えは8ページ · レベルは混ざっています。番号で答えを探しましょう'),
    ('读第 3 版文章，判断对错。', '3ページの記事を読みましょう。正しいか間違いか？'),
    ('传说马丁是罗马士兵', '伝説ではマルティンはローマ兵だった'),
    ('传说鹅叫声暴露了他', '伝説ではガチョウが居場所をばらした'),
    ('纪念日 11 月 11 日', '記念日は11月11日'),
    ('截稿时 11 月 3–8 日结果未知', '11月3～8日の結果は締め切り時点で不明'),
    ('狂欢季 11 点 11 分开幕', 'カーニバルは11時11分に開幕'),
    ('用方框里的词填空。', '枠の単語で完成させましょう。'),
    ('斗篷分给乞丐', '物乞いと分け合ったマント'),
    ('纸灯笼', '紙のランタン'),
    ('圣马丁鹅', '聖マルティンのガチョウ'),
    ('圣马丁鹅配红甘蓝和丸子', '赤キャベツと団子添えの聖マルティンのガチョウ'),
    ('狂欢节服装', 'カーニバルの衣装'),
    ('游行在篝火处结束', '行列は焚き火で終わる'),
    ('选出正确答案。', '正しい答えを選びましょう。'),
    ('马丁后来成为图尔主教', 'マルティンは後にトゥールの司教になった'),
    ('灯笼游行常在前后晚上举行', 'ランタン行列は前後の夕方に行われることが多い'),
    ('VOL.4 报道 11 月 3–8 日结果', 'VOL.4で11月3～8日の結果を伝える'),
    ('把词组成正确的句子。', '単語を正しい文に並べましょう。'),
    ('主谓宾顺序', '主語・動詞・目的語の順'),
    ('时间状语开头，动词第二位', '時間表現が先、動詞は2番目'),
    ('地点开头，动词第二位', '場所が先、動詞は2番目'),
    ('SPORT · 体育', 'SPORT · スポーツ'),
    ('LEVEL B1 · Nationalelf & NFL · 国家队与 NFL', 'LEVEL B1 · Nationalelf & NFL · 代表チームとNFL'),
    ('das Geisterspiel 空场比赛 · das Hinspiel 首回合 · ausverkauft 售罄 · der Star 明星 · gewinnen 获胜。', 'das Geisterspiel＝無観客試合 · das Hinspiel＝第1戦 · ausverkauft＝完売 · der Star＝スター · gewinnen＝勝つ。'),
    ('你更爱看足球还是美式橄榄球？贝尔格莱德谁赢？写两句德语寄来。', 'サッカーとアメフト、どちらが勝つ？ドイツ語で2文！'),
    ('DER SPIELPLAN · 本周与下周赛程', 'DER SPIELPLAN · 今週と来週'),
    ('ÜBUNGEN · 第 4 版练习', 'ÜBUNGEN · 4ページの練習'),
    ('读第 4 版文章，选出正确答案。', '4ページの記事を読んで、正しい答えを選びましょう。'),
    ('德国 5 分，荷兰希腊各 8 分', 'ドイツ5点、オランダとギリシャは各8点'),
    ('主教练 11 月 5 日公布名单', '監督は11月5日に代表を発表する'),
    ('贝尔格莱德空场', 'ベオグラードの空っぽのスタジアム'),
    ('首回合德国 2:0 胜塞尔维亚', 'ドイツは第1戦でセルビアに2-0で勝った'),
    ('NFL 慕尼黑赛售罄', 'ミュンヘンのNFLの試合は完売'),
    ('Geisterspiel=空场比赛 b', 'Geisterspiel=無観客試合 b'),
    ('Hinspiel=首回合 a', 'Hinspiel=第1戦 a'),
    ('Ausrüster=装备赞助商 c', 'Ausrüster=ユニフォーム提供社 c'),
    ('ausverkauft=售罄 d', 'ausverkauft=完売 d'),
    ('用比较级完成句子（括号里是原级）。', '比較級で完成させましょう（かっこ内は原級）。'),
    ('viel → mehr（荷兰 8 分多于德国 5 分）', 'viel → mehr（オランダは8点、ドイツの5点より多い）'),
    ('spät → später（15:30 晚于 11:11）', 'spät → später（15時30分は11時11分より遅い）'),
    ('leise → leiser（空场比主场安静）', 'leise → leiser（空っぽのスタジアムはホームゲームより静か）'),
    ('früh → früher（11 月 5 日早于 11 月 13 日）', 'früh → früher（11月5日は11月13日より早い）'),
    ('看上面的赛程表，选出正确答案。', '上の対戦表を見て、正しい答えを選びましょう。'),
    ('塞尔维亚–德国周五 20:45', 'セルビア対ドイツは金曜20時45分'),
    ('NFL 周日 15:30', 'NFLは日曜15時30分'),
    ('德国–荷兰周一 20:45', 'ドイツ対オランダは月曜20時45分'),
    ('拜仁–科隆周五 20:30', 'バイエルン対ケルンは金曜20時30分'),
    ('沙尔克–斯图加特周六 17:30', 'シャルケ対シュトゥットガルトは土曜17時30分'),
]
rep_all("content34.py", C34)

# ================= content56.py =================
C56 = [
    ('JUGEND · 青年', 'JUGEND · 若者'),
    ('LEVEL B1 · Laternen, Lieder & Schule · 灯笼、歌曲与学校', 'LEVEL B1 · Laternen, Lieder & Schule · ランタン、歌、学校'),
    ('basteln 制作 · der Pausenhof 课间操场 · sich verkleiden 乔装打扮 · die Stimmung 气氛 · der Pirat 海盗。', 'basteln＝作る · der Pausenhof＝校庭 · sich verkleiden＝仮装する · die Stimmung＝雰囲気 · der Pirat＝海賊。'),
    ('SCHULWOCHE · 开学周', 'SCHULWOCHE · 学校'),
    ('die Laterne — 灯笼', 'die Laterne — ランタン'),
    ('basteln — 制作', 'basteln — 作る'),
    ('das Lied — 歌曲', 'das Lied — 歌'),
    ('das Kostüm — 服装', 'das Kostüm — 衣装'),
    ('der Umzug — 游行', 'der Umzug — 行列'),
    ('der Stern — 星星', 'der Stern — 星'),
    ('MARTINSWÖRTER · 圣马丁词汇', 'MARTINSWÖRTER · 聖マルティン'),
    ('UND SIE? · 说说你自己', 'UND SIE? · あなたは？'),
    ('你小时候做过灯笼吗？11 月你唱哪首歌？写两句德语寄来。', '子どもの頃ランタンを作りましたか。ドイツ語で2文！'),
    ('DER WOCHENPLAN DER REDAKTION · 编辑部一周计划', 'DER WOCHENPLAN DER REDAKTION · 編集部の1週間'),
    ('ÜBUNGEN · 第 5 版练习', 'ÜBUNGEN · 5ページの練習'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', '答えは8ページ · レベルは混ざっています。番号で答えを探しましょう'),
    ('读第 5 版文章，选出正确答案。', '5ページの記事を読んで、正しい答えを選びましょう。'),
    ('11 月 9 日全德复课', '学校は11月9日にどこでも再開'),
    ('孩子们做纸灯笼', '子どもたちは紙のランタンを作る'),
    ('纸灯笼', '紙のランタン'),
    ('上午狂欢，下午圣马丁', '午前はカーニバル、午後は聖マルティン'),
    ('NFL 周日在电视上', '日曜はテレビでNFL'),
    ('周五看国家队比赛', '金曜に代表チームを見る'),
    ('用方框里的词填空。', '枠の単語で完成させましょう。'),
    ('做灯笼', 'ランタンを作ること'),
    ('唱圣马丁歌曲', '聖マルティンの歌を歌うこと'),
    ('狂欢节服装', 'カーニバルの衣装'),
    ('灯笼游行', 'ランタン行列'),
    ('灯笼上的星星', 'ランタンの星'),
    ('用 weil 连接两个句子（动词放句末）。', '2文をweilでつなげましょう（動詞は文末へ）。'),
    ('weil 句动词置尾', 'weilの文では動詞は文末'),
    ('ist 置尾', 'istは文末へ'),
    ('will 置尾', 'willは文末へ'),
    ('beginnt 置尾', 'beginntは文末へ'),
    ('判断对错。', '正しいか間違いか？'),
    ('11 月 9 日巴伐利亚也复课', 'バイエルンも11月9日に再開'),
    ('灯笼游行在晚上', 'ランタン行列は夕方'),
    ('孩子们唱圣马丁歌曲', '子どもたちは聖マルティンの歌を歌う'),
    ('VERTIEFUNG · 深读', 'VERTIEFUNG · 深読み'),
    ('LEVEL B2 · Volkstrauertag & Stromsteuer · 纪念日与电力税', 'LEVEL B2 · Volkstrauertag & Stromsteuer · 追悼の日と電気税'),
    ('gedenken 纪念 · die Kranzniederlegung 献花圈 · der stille Tag 安静日 · die Verbundenheit 联系 · die Versöhnung 和解。', 'gedenken＝追悼する · Kranzniederlegung＝献花 · stille Tag＝静かな日 · Verbundenheit＝絆 · Versöhnung＝和解。'),
    ('DIE ZAHLEN · 本周数字', 'DIE ZAHLEN · 数字'),
    ('纪念日：纪念需要安静——对此几乎人人赞同。电力税：降多少尚未确定。两者都关系到几乎每个家庭。', '追悼の日：追悼には静けさが必要——ほぼ全員が同意。電気税：どれだけ下がるかはまだ未定。どちらもほぼすべての家庭に関わる。'),
    ('ZWEI SONNTAGE IM NOVEMBER · 十一月的两个周日', 'ZWEI SONNTAGE IM NOVEMBER · 11月の2つの日曜日'),
    ('WAS INTERESSIERT DIE LESER? · 读者最关心什么？', 'WAS INTERESSIERT DIE LESER? · 読者の関心は？'),
    ('("Nations League und NFL", 46, "足球")', '("Nations League und NFL", 46, "サッカー")'),
    ('("St. Martin und Karneval", 34, "节日")', '("St. Martin und Karneval", 34, "祭り")'),
    ('("Volkstrauertag und Gedenken", 20, "纪念")', '("Volkstrauertag und Gedenken", 20, "追悼")'),
    ('ÜBUNGSDATEN · 练习数据 — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage.（本图数字为编辑部练习示例，非真实调查。）', 'ÜBUNGSDATEN · 練習用データ — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage.（練習用データであり、実際の調査ではありません。）'),
    ('ÜBUNGEN · 第 6 版练习', 'ÜBUNGEN · 6ページの練習'),
    ('看上面的练习图表，选出正确答案。', '上の練習用グラフを使いましょう。'),
    ('46% 足球最受关注', 'サッカーが46％で首位'),
    ('节日 34% 第二', '祭りが34％で2位'),
    ('纪念 20% 最小', '追悼が20％で最少'),
    ('纪念 20%', '追悼20％'),
    ('读第 6 版深读文章，选出正确答案。', '6ページの記事を読みましょう。'),
    ('11 月 15 日纪念日', '追悼の日は11月15日'),
    ('ZDF 13 点半直播纪念仪式', 'ZDFは13時30分から生中継'),
    ('家庭电力税 2.05 欧分', '家庭の電気税は2.05セント'),
    ('2027 年预算 11 月 27 日表决', '2027年度予算の採決は11月27日'),
    ('用括号里的形式填空。', 'かっこ内の形で書き入れましょう。'),
    ('被动：wird + Partizip II', '受動態：wird＋過去分詞'),
    ('ob 引导间接疑问句', 'obは間接疑問を導く'),
    ('献花圈仪式', '献花式'),
    ('为和平与和解', '平和と和解のために'),
    ('德奥联系', 'ドイツとオーストリアの絆'),
    ('纪念受害者', '犠牲者を追悼すること'),
]
rep_all("content56.py", C56)

# ================= content7.py =================
C7 = [
    ('SPRACHE · 语言', 'SPRACHE · ことば'),
    ('A2 → B2 · Sätze der Woche & Fehlerklinik · 本周金句与纠错诊所', 'A2 → B2 · Sätze der Woche & Fehlerklinik · 今週の文と誤りクリニック'),
    ('本版专攻语言：三节小课、本期金句（全部摘自本期文章原文）、纠错诊所和读者来信。', 'このページはことばづくしです。3つの短いレッスン、今週の文（すべて今号の記事から一字一句引用）、誤りクリニック、読者の手紙。'),
    ('BEISPIELE · 例句', 'BEISPIELE · 例'),
    ('被动：wird + Partizip II', '受動態：wird＋過去分詞'),
    ('复数：werden', '複数：werden'),
    ('werden + 原形表将来', 'werden＋不定詞で未来'),
    ('被动语态', '受動態'),
    ('lang → länger（夜晚比白天长）', 'lang → länger（夜は昼より長い）'),
    ('weil 引导原因', 'weilは理由を導く'),
    ('weil 句动词置尾', 'weilの文では動詞は文末'),
    ('länger als = 比……更长', 'länger als＝～より長い'),
    ('„Länger als sonst“ heißt... A. 比平时更长 · B. 和平时一样 · C. 比平时更短', '„Länger als sonst“の意味は… A. いつもより長い · B. いつもと同じ · C. いつもより短い'),
    ('ob 引导间接疑问', 'obは間接疑問を導く'),
    ('Es ist fraglich, ob ... = 是否还难说', 'Es ist fraglich, ob ...＝～かどうか疑わしい'),
    ('dass 句动词置尾', 'dassの文では動詞は文末'),
    ('礼貌表达观点', '丁寧に意見を言う方法'),
    ('11.11 Uhr = 11 点 11 分', '11.11 Uhr＝11時11分'),
    ('vor leeren Rängen = 空场，没有观众', 'vor leeren Rängen＝無観客'),
    ('Es wird gespielt. = 比赛将进行（被动）', 'Es wird gespielt.＝試合が行われる'),
    ('Meiner Meinung nach ... = 在我看来……', 'Meiner Meinung nach＝私の意見では'),
    ('Ich finde, dass ... = 我觉得……', 'Ich finde, dass＝～と思う'),
    ('Es ist fraglich, ob ... = 是否……还难说', 'Es ist fraglich, ob ...＝～かどうか疑わしい'),
    ('DER WERKZEUGKASTEN · 工具箱', 'DER WERKZEUGKASTEN'),
    ('label = "Ein Beispiel der Redaktion!"', 'label = "編集部による例です！"'),
    ('编辑部示例，非真实来信：截稿时未收到真实来信或习作，见 VOL.4。请寄来您的习作，优秀者刊登于 VOL.4。', '編集部の例であり、本物の手紙ではありません。締め切りまでに本物の手紙は届いていませんでした。VOL.4へお送りください！'),
    ('LESERBRIEFE · 读者来信', 'LESERBRIEFE · 読者の手紙'),
    ('NOCH EIN WORT · 再学一词', 'NOCH EIN WORT · もう一言'),
    ('«das Geisterspiel»（Seite 4）: ein Spiel ohne Zuschauer im Stadion. 空场比赛。', '«das Geisterspiel» (Seite 4) : ein Spiel ohne Zuschauer im Stadion. 無観客試合：観客のいない試合。'),
    ('SÄTZE DER WOCHE · 本周金句', 'SÄTZE DER WOCHE · 今週の文'),
    ('原文摘录，逐字引自本期文章 · 括号内为出处', '今号の記事から一字一句引用 · 出典はかっこ内'),
    ('德甲休战——但国家队要比赛。', 'ブンデスリーガは中断する——しかし代表チームは試合をする。'),
    ('11 点 11 分，科隆新一季狂欢季开幕。', '11時11分、ケルンで新しいカーニバル・シーズンが始まる。'),
    ('他的纪念日是 11 月 11 日。', '彼の記念日は11月11日である。'),
    ('书包收拾好了，操场上又热闹起来。', 'かばんは詰められ、校庭は再びにぎやかだ。'),
    ('十一月黑暗，但并不安静：它歌唱、发光、庆祝。', '11月は暗いが、静かではない。歌い、輝き、祝う。'),
    ('比赛售罄，RTL 现场直播。', '試合は完売、RTLが生中継する。'),
    ('这里的纪念意味着：停下来、记住——并为和平与和解挺身而出。', 'ここで追悼とは、立ち止まり、思い出し——平和と和解のために立ち上がることである。'),
    ('周日，全国一片安静。', '日曜日、国は静かだ。'),
    ('FEHLERKLINIK · 纠错诊所', 'FEHLERKLINIK · 誤りクリニック'),
    ('学习者最常犯的四个错 · 先自己改，再看答案', '学習者が最もよくする4つの誤り · まず直してから確認しましょう'),
    ('动词第二位：主语不在句首时，动词仍居第二。', '動詞は2番目：主語が最初でなくても、動詞は2番目のまま。'),
    ('halb zwölf = 十一点半（zwölf 之前）。', 'halb zwölf＝11時30分、zwölfの30分前。'),
    ('Perfekt 中 Partizip II 放句末。', 'Perfektでは過去分詞は文末へ。'),
    ('ob 从句动词放句末。', 'obの文では動詞は文末へ。'),
    ('IN DER NÄCHSTEN AUSGABE · 下期预告 (VOL.4)', 'IN DER NÄCHSTEN AUSGABE · 次号（VOL.4）'),
]
rep_all("content7.py", C7)

# ================= content8.py =================
C8 = [
    ('ÜBUNGEN & ANTWORTEN · 练习与答案', 'ÜBUNGEN & ANTWORTEN · 練習と答え'),
    ('SCHLUSSTEST · 综合评估 · Alle Antworten unten auf dieser Seite 答案在本版下方', 'SCHLUSSTEST · 最終テスト · Alle Antworten unten auf dieser Seite — 答えはすべてこのページの下部に'),
    ('beginnt（第三人称单数）', 'beginnt(3人称単数)'),
    ('bastelt（第三人称单数）', 'bastelt(3人称単数)'),
    ('geht（第三人称单数）', 'geht(3人称単数)'),
    ('singt（第三人称单数）', 'singt(3人称単数)'),
    ('schaut（第三人称单数）', 'schaut(3人称単数)'),
    ('sieht（第三人称单数）', 'sieht(3人称単数)'),
    ('erzählt（第三人称单数）', 'erzählt(3人称単数)'),
    ('A · LÜCKENTEXT · 完形填空', 'A · LÜCKENTEXT · 穴埋め'),
    ('选项：', '選択肢：'),
    ('B · WISSENSFRAGEN · 综合问答', 'B · WISSENSFRAGEN · クイズ'),
    ('狂欢季 11 点 11 分开幕', 'カーニバルは11時11分に開幕'),
    ('周五客战塞尔维亚', '金曜日にセルビアでアウェー戦'),
    ('NFL 周日 15:30', 'NFLは日曜15時30分'),
    ('纪念日 11 月 15 日', '追悼の日は11月15日'),
    ('家庭电力税 2.05 欧分', '家庭の電気税は2.05セント'),
    ('主教练 11 月 5 日公布名单', '監督は11月5日に代表を発表する'),
    ('ZDF 13 点半直播纪念仪式', 'ZDFは13時30分から生中継'),
    ('亡灵主日 11 月 22 日', 'Totensonntagは11月22日'),
    ('C · LESEVERSTEHEN · 阅读理解', 'C · LESEVERSTEHEN · 読解'),
    ('周三做灯笼', '水曜日にランタンを作ること'),
    ('周五看德国队', '金曜日にドイツを見ること'),
    ('D · SÄTZE BAUEN · 造句', 'D · SÄTZE BAUEN · 文作り'),
    ('时间状语，动词第二位', '時間表現、動詞は2番目'),
    ('主谓宾顺序', '主語・動詞・目的語の順'),
    ('时间状语开头，动词第二位', '時間表現が先、動詞は2番目'),
    ('地点时间开头，动词第二位', '場所と時間が先、動詞は2番目'),
    ('E · ÜBERSETZEN · 翻译', 'E · ÜBERSETZEN · 翻訳'),
    ('狂欢节 11 点 11 分在科隆开幕。', 'カーニバルは11時11分にケルンで開幕する。'),
    ('beginnen = 开始', 'beginnen＝始まる'),
    ('Der Karneval beginnt um 11.11 Uhr in Köln.（译成中文）', 'Der Karneval beginnt um 11.11 Uhr in Köln.（日本語に訳しましょう）'),
    ('我周三做一个灯笼。', '水曜日にランタンを作ります。'),
    ('basteln = 制作', 'basteln＝作る'),
    ('Ich bastle am Mittwoch eine Laterne.（译成中文）', 'Ich bastle am Mittwoch eine Laterne.（日本語に訳しましょう）'),
    ('学校 11 月 9 日又开学了。', '学校は11月9日に再開した。'),
    ('wieder begonnen = 又开始', 'wieder begonnen＝再開した'),
    ('Die Schule hat am 9. November wieder begonnen.（译成中文）', 'Die Schule hat am 9. November wieder begonnen.（日本語に訳しましょう）'),
    ('看比赛 = das Spiel schauen', '試合を見る＝das Spiel schauen'),
    ('"我周日看 NFL 比赛。（译成德语）", instr="翻译"', '"日曜日にNFLの試合を見ます。（ドイツ語に訳しましょう）", instr="ドイツ語に訳す"'),
    ('F · WÖRTER PAAREN · 词汇配对', 'F · WÖRTER PAAREN · 単語ペア'),
    ('Mantel=斗篷 b', 'Mantel=マント b'),
    ('Laterne=灯笼 a', 'Laterne=ランタン a'),
    ('Geisterspiel=空场比赛 d', 'Geisterspiel=無観客試合 d'),
    ('Versöhnung=和解 c', 'Versöhnung=和解 c'),
    ('singst（第二人称单数）', 'singst(2人称単数)'),
    ('macht（第二人称复数）', 'macht(2人称複数)'),
    ('essen（第一人称复数）', 'essen(1人称複数)'),
    ('machst（第二人称单数）', 'machst(2人称単数)'),
    ('schaue（第一人称单数）', 'schaue(1人称単数)'),
    ('G · DIALOG · 对话补全', 'G · DIALOG · 対話の補完'),
    ('开放题 — 要点见写作框，范文在第 8 版写作框内', '自由課題 — 作文の枠のポイントに沿いましょう。模範文はこのページの枠の中にあります'),
    ('按要点给分', '挙げられたポイントで採点されます'),
    ('H · SCHREIBEN · 写作', 'H · SCHREIBEN · 作文'),
    ('用德语写 80–100 词：《我的十一月的一周》。写清做什么手工、看哪几场比赛、和谁一起，并写一句关于圣马丁节或纪念日的话。', 'ドイツ語で80～100語で書きましょう。「11月の私の1週間」。何を作るか、どの試合を誰と見るか——そして聖マルティンの日か追悼の日について1文加えましょう。'),
    ('MUSTER · 范文（84 Wörter）', 'MUSTER · 模範文（84 Wörter）'),
    ('ANTWORTEN · 全部答案与简析（第 1–8 版）', 'ANTWORTEN · 答えと解説（1～8ページ）'),
]
rep_all("content8.py", C8)

# ---------- P8 keys ----------
rep("content8.py", 'kf.para(f"— \u7b2c {pg} \u7248 —", 17, "sans", True, OLIVE, 1.28, 3)',
    'kf.para(f"— {pg} ページ —", 17, "sans", True, OLIVE, 1.28, 3)', 1)
rep("content8.py", 's += f"\uff08{e[\'note\']}\uff09"',
    's += f" ({e[\'note\']})"', 1)
rep("content8.py", 'kf.para(" · ".join(parts), 14.5, "sans", False, INK, 1.3, 9)',
    'kf.para(" · ".join(parts), 13.0, "sans", False, INK, 1.16, 9)', 1)

# ---------- generic value maps ----------
TYPEMAP = [('完成句子', '文完成'), ('单选', '選択肢'), ('句型转换', '文の書き換え'), ('词汇配对', '単語ペア'), ('判断对错', '正誤判断'), ('完形填空', '穴埋め'), ('造句', '文作り'), ('对话补全', '対話の補完'), ('翻译', '翻訳'), ('写作', '作文')]
INSTRMAP = [('instr="填空"', 'instr="空所補充"'), ('instr="改写"', 'instr="書きかえ"'), ('instr="判断"', 'instr="正誤"'), ('instr="造句"', 'instr="文を作る"'), ('instr="翻译"', 'instr="翻訳"'), ('instr="把词和释义配对"', 'instr="語と意味を結ぶ"')]
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
exempt = ['KULTUR · 文化', 'LEBEN · 生活', 'Versöhnung=和解 c']
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
