# -*- coding: utf-8 -*-
"""W45 zh-tw core -> zh-tw x ja fan-out transform.

Value-map only: whole-line or exact-literal replacements with an
assertion after each one (README #17: no AST byte offsets; #18: bare
text for f-string fragments, never repr literals). Target-language
(Traditional) strings are NEVER touched: every `old` below is an
English explanation-layer string, furniture string, or OUT path.
Usage: python3 transform.py <build-copy-dir> [edition-root-literal]
Default edition root: the delivery dir.
"""
import os, sys

BUILD = sys.argv[1]
ROOT = sys.argv[2] if len(sys.argv) > 2 else "~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-tw-ja"
LOG = []


def rep(fn, old, new, expect=None):
    p = os.path.join(BUILD, fn)
    s = open(p, encoding="utf-8").read()
    n = s.count(old)
    if expect is not None:
        assert n == expect, f"{fn}: {old[:60]!r} found {n}, expected {expect}"
    else:
        assert n >= 1, f"{fn}: NOT FOUND {old[:60]!r}"
    open(p, "w", encoding="utf-8").write(s.replace(old, new))
    LOG.append(f"{fn}: x{n} :: {old[:44]}")
    return n


def repoint(fn, var, subpath):
    """Whole-line OUT/BASE replacement (Gate-10 rule: replace the whole
    expanduser(...) call, never splice a temp dir inside the prefix)."""
    p = os.path.join(BUILD, fn)
    lines = open(p, encoding="utf-8").read().split("\n")
    done = 0
    for i, ln in enumerate(lines):
        if ln.startswith(var + " = os.path.expanduser("):
            lines[i] = f'{var} = os.path.expanduser("{ROOT}{subpath}")'
            done += 1
    assert done == 1, f"{fn}: {var} line found {done} times"
    open(p, "w", encoding="utf-8").write("\n".join(lines))
    LOG.append(f"{fn}: repointed {var} -> {ROOT}{subpath}")


for fn in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    repoint(fn, "OUT", "/svg")
repoint("render.py", "BASE", "")

# ---------------- bslib4 furniture (W43 zh-tw-ja precedent) ----------------
rep("bslib4.py", "Lucerna · 繁體中文週報 VOL.2 · 繁體中文正文 · 英語講解 · Traditional Chinese text · English explanations",
    "Lucerna · 中国語（繁体字）週刊 VOL.2 · 本文は中国語（繁体字） · 解説は日本語", 1)
rep("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"{n} ページ（全 {total} ページ）"', 1)
rep("bslib4.py", "Notes｜", "解説 — ", 1)

# ---------------- content12: P1 + P2 ----------------
rep("content12.py", "繁體中文正文 · 英語講解 — Traditional Chinese text · Explanations in English · the edition for English-speaking readers",
    "中国語（繁体字）テキスト · 日本語の解説 — 日本語読者のための版", 1)
rep("content12.py", "Staff report · Source: event organisers' press release (Oct 23) and event FAQ",
    "本紙スタッフ · 出典：主催者のプレスリリース（10月23日）とイベントFAQ", 1)
rep("content12.py", "Hong Kong FinTech Week x StartmeupHK 2026 opens Monday (Nov 2) and runs to Friday (Nov 6). The main conference and exhibition are at the Hong Kong Convention and Exhibition Centre on Nov 2-3, with 100+ community events through the week. Expect 45,000+ people from 120+ economies, 1,000+ speakers and 800+ exhibitors and start-ups.",
    "香港フィンテックウィーク×StartmeupHK 2026は11月2日（月）に開幕し、11月6日（金）まで開催。メインカンファレンスと展示会は11月2～3日に香港コンベンション・アンド・エキシビション・センターで開催され、週を通して100以上のコミュニティイベントがある。参加者は120以上の国と地域から45,000人以上、講演者1,000人以上、出展者とスタートアップ800以上が見込まれる。", 1)
rep("content12.py", "The Taipei International Travel Fair (ITF) opens Friday (Nov 6) at noon at the Nangang Exhibition Center and runs to Monday (Nov 9): 123 countries and cities, 1,600 booths, a daily 14:00 mascot parade and travel talks.",
    "台北国際旅展（ITF）は11月6日（金）正午に南港展覧館で開幕し、11月9日（月）まで開催：123の国と都市、1,600のブース、毎日14時のマスコットパレードと旅行講座がある。", 1)
rep("content12.py", "本週大事 · This week", "本週大事 · 今週の主な出来事", 1)
rep("content12.py", "本週一詞 · Word of the week", "本週一詞 · 今週の言葉", 1)
rep("content12.py", "「金融科技」 — fintech: using technology to run financial services, like paying by phone or scanning a code to pay.",
    "「金融科技」 — フィンテック：電話での送金やコード決済のように、テクノロジーで金融サービスを動かすこと。", 1)
rep("content12.py", "快速測驗 · Quick quiz", "快速測驗 · クイッククイズ", 1)
rep("content12.py", "FinTech Week opens on Monday, Nov 2.", "フィンテックウィークは11月2日（月）に開幕。", 1)
rep("content12.py", "The main conference is at the Hong Kong Convention and Exhibition Centre.", "メインカンファレンスは香港コンベンション・エキシビション・センターで開催。", 1)
rep("content12.py", "More than 45,000 people are expected.", "45,000人以上の参加が見込まれる。", 1)
rep("content12.py", "The travel fair opens Friday, Nov 6, at noon.", "旅展は11月6日（金）の正午に開幕。", 1)
rep("content12.py", "標題填空 · Headline words", "標題填空 · 見出しの言葉", 1)
rep("content12.py", "Participants come from 120+ economies.", "参加者は120以上の国と地域から集まる。", 1)
rep("content12.py", "More than 800 exhibitors and start-ups take part.", "800以上の出展者とスタートアップが参加。", 1)
rep("content12.py", "The travel fair gathers 123 countries and cities.", "旅展には123の国と都市が集まる。", 1)
rep("content12.py", "The travel fair has 1,600 booths.", "旅展には1,600のブースがある。", 1)
rep("content12.py", "Saturday, Nov 7 is the Start of Winter solar term.", "11月7日（土）は立冬、冬の始まりの節気。", 1)
rep("content12.py", "The travel fair runs to Monday, Nov 9.", "旅展は11月9日（月）まで開催。", 1)
rep("content12.py", "生活 · Life", "生活 · 暮らし", 1)
rep("content12.py", "第 2 版 · 天氣、泡湯、旅展與雙11 · Weather, hot springs, the travel fair and 11.11",
    "第 2 版 · 天氣、泡湯、旅展與雙11 · 天気・温泉・旅展とダブルイレブン", 1)
rep("content12.py", "The northeast monsoon cools northern Taiwan, and Saturday (Nov 7) is Lidong, the Start of Winter: the day winter begins in the 24 solar terms. Many people mark it with a hot, nourishing pot meal.",
    "北東モンスーンが台湾北部を涼しくし、11月7日（土）は立冬、二十四節気で冬が始まる日。人々は温かく体に良い鍋料理でこの日を祝う。", 1)
rep("content12.py", "Autumn and winter are for hot springs and hiking. The travel fair's trail encyclopaedia collects 56 routes, and the 6 Greenways stamp challenge covers the Tamsui-Kavalan, Raknus Selu, Mountain-to-Sea, Centenary, Indigenous and Sugar-Rail trails.",
    "秋と冬は温泉とハイキングの季節。旅展の歩道百科には56のルートが収録され、6つのグリーンウェイのスタンプチャレンジは淡蘭古道、樟之細路、山海圳、百年大圳、原民古道、糖鐵國家綠道をカバーする。", 1)
rep("content12.py", "練習例子 · Practice example", "練習例子 · 練習の例", 1)
rep("content12.py", "Practice numbers: NT$2,400 + NT$1,600 = NT$4,000, exactly her budget — so she can buy both.",
    "計算：2,400台湾ドル + 1,600台湾ドル = 4,000台湾ドル、ちょうど予算通り — 両方買える。", 1)
rep("content12.py", "讀懂了嗎? · Did you get it?", "讀懂了嗎? · 読めたかな？", 1)
rep("content12.py", "Lidong, the Start of Winter, is Saturday, Nov 7.", "立冬（冬の始まり）は11月7日（土）。", 1)
rep("content12.py", "The northeast monsoon cools northern Taiwan.", "北東モンスーンが台湾北部を涼しくする。", 1)
rep("content12.py", "The trail encyclopaedia collects 56 routes.", "歩道百科には56のルートが収録されている。", 1)
rep("content12.py", "The stamp challenge has 6 Greenways.", "スタンプチャレンジは6つのグリーンウェイからなる。", 1)
rep("content12.py", "Double 11 falls on Wednesday, Nov 11.", "ダブルイレブンは11月11日（水）。", 1)
rep("content12.py", "Before paying, check tax, delivery and returns.", "支払う前に、税金・配送料・返品を確認すること。", 1)
rep("content12.py", "填一填 · Fill in", "填一填 · 埋めてみよう", 1)
rep("content12.py", "A hot pot meal marks Lidong: 進補.", "鍋料理で祝う立冬：進補。", 1)
rep("content12.py", "Check the jacket: mornings and evenings are cool.", "朝晩は涼しいので上着を確認。", 1)
rep("content12.py", "Autumn and winter are good for hot springs.", "秋と冬は温泉にぴったりの季節。", 1)
rep("content12.py", "Collect stamps on the 6 Greenways.", "6つのグリーンウェイでスタンプを集める。", 1)
rep("content12.py", "Set a budget before Double 11 shopping.", "ダブルイレブンの買い物の前に予算を決める。", 1)
rep("content12.py", "The Tamsui-Kavalan Trail is one of the 6 Greenways.", "淡蘭古道は6つのグリーンウェイの一つ。", 1)
rep("content12.py", "算一算 · Work it out", "算一算 · 計算してみよう", 1)
rep("content12.py", "2,400 + 1,600 = 4,000, exactly the budget.", "2,400 + 1,600 = 4,000、ちょうど予算通り。", 1)
rep("content12.py", "The budget is 4,000 and the total is 4,000: nothing over.", "予算4,000に対し合計も4,000：超過なし。", 1)
rep("content12.py", "立冬 — the Start of Winter solar term.", "立冬 — 冬の始まりの節気。", 1)
rep("content12.py", "進補 — eating nourishing hot food for winter.", "進補 — 冬に備えて体に良い温かいものを食べること。", 1)
rep("content12.py", "泡湯 — soaking in a hot spring.", "泡湯 — 温泉につかること。", 1)
rep("content12.py", "集章 — collecting stamps at set points.", "集章 — 決められた場所でスタンプを集めること。", 1)
rep("content12.py", 'instr="Match"', 'instr="語と意味を結ぶ"', 1)
rep("content12.py", 'instr="Fill in"', 'instr="空所補充"', 12)
rep("content12.py", "事實框 · This week's facts", "事實框 · 今週のファクト", 1)
rep("content12.py", "你呢? · Over to you", "你呢? · あなたは？", 1)
rep("content12.py", "What hot pot would you eat for Lidong? What is in your Double 11 cart?",
    "立冬にはどんな鍋を食べたいですか。ダブルイレブンのカートの中身は何ですか。", 1)
rep("content12.py", "封王優惠 · Champion deals", "封王優惠 · 優勝セール", 1)

# ---------------- content34: P3 + P4 ----------------
rep("content34.py", "文化 · Culture", "文化 · 文化", 1)
rep("content34.py", "第 3 版 · 立冬、鋼雕與沙雕落幕 · Lidong, steel art and the sand festival finale",
    "第 3 版 · 立冬、鋼雕與沙雕落幕 · 立冬・鉄の彫刻と砂の祭典の閉幕", 1)
rep("content34.py", "Lidong is the first solar term of winter: winter begins. People mark it with hot pot dishes like ginger duck, lamb hotpot and sesame chicken — warming food before the cold months.",
    "立冬は冬の最初の節気：冬が始まる。人々は薑母鴨、羊肉爐、麻油雞のような鍋料理で祝う — 寒い季節の前に体を温める食事。", 1)
rep("content34.py", "Kaohsiung's International Steel Sculpture Festival (Oct 23-Nov 22) turns warehouses, factories, the harbour and streets into a stage — SUPER STAGE — with an international forum on making, design and art in daily life.",
    "高雄国際鉄彫刻祭（10月23日～11月22日）は倉庫・工場・港・街を舞台に変える — SUPER STAGE — ものづくり・デザイン・日常生活の中のアートをテーマにした国際フォーラム付き。", 1)
rep("content34.py", "The Fulong International Sand Sculpture Art Festival closed Oct 26 after its 19th season (May 29-Oct 26): 40+ sculptures by 15+ artists, built from Fulong's golden sand around film characters from Jurassic World, Shrek, Kung Fu Panda and Back to the Future.",
    "福隆国際サンドスカルプチャーアートフェスティバルは第19シーズン（5月29日～10月26日）の後、10月26日に閉幕：15人以上のアーティストによる40以上の彫刻。福隆の金色の砂で作られ、ジュラシック・ワールド、シュレック、カンフー・パンダ、バック・トゥ・ザ・フューチャーの映画キャラクターが登場。", 1)
rep("content34.py", "讀懂了嗎? · Did you get it?", "讀懂了嗎? · 読めたかな？", 2)
rep("content34.py", "Lidong means winter begins.", "立冬は冬の始まりを意味する。", 1)
rep("content34.py", "Ginger duck is a typical Lidong dish.", "薑母鴨は立冬の代表的な料理。", 1)
rep("content34.py", "The steel festival runs Oct 23-Nov 22.", "鉄の彫刻祭は10月23日から11月22日まで。", 1)
rep("content34.py", "The venues include Pier-2's Penglai B3 warehouse.", "会場には駁二蓬萊区B3倉庫が含まれる。", 1)
rep("content34.py", "The sand festival closed on Oct 26.", "砂の祭典は10月26日に閉幕。", 1)
rep("content34.py", "The sand festival made 40+ sculptures.", "砂の祭典では40以上の彫刻が作られた。", 1)
rep("content34.py", "填一填 · Fill in", "填一填 · 埋めてみよう", 2)
rep("content34.py", "Lidong is a solar term (節氣).", "立冬は節気の一つ。", 1)
rep("content34.py", "Sesame chicken is a Lidong dish.", "麻油雞は立冬の料理。", 1)
rep("content34.py", "Steel is Kaohsiung's material and memory.", "鉄は高雄の素材であり記憶でもある。", 1)
rep("content34.py", "Hamasen Railway Park is a venue.", "哈瑪星鉄道園区は会場の一つ。", 1)
rep("content34.py", "Fulong's sand is golden.", "福隆の砂は金色。", 1)
rep("content34.py", "Jurassic World is one of the film characters.", "ジュラシック・ワールドは映画キャラクターの一つ。", 1)
rep("content34.py", "算一算 · Work it out", "算一算 · 計算してみよう", 1)
rep("content34.py", "May 29-31 (3) + Jun 30 + Jul 31 + Aug 31 + Sep 30 + Oct 26 = 151 days.",
    "5月29～31日（3日）+ 6月30日 + 7月31日 + 8月31日 + 9月30日 + 10月26日 = 151日。", 1)
rep("content34.py", "Oct 23-31 (9) + Nov 22 = 31 days.", "10月23～31日（9日）+ 11月22日 = 31日。", 1)
rep("content34.py", "立冬 — the first solar term of winter.", "立冬 — 冬の最初の節気。", 1)
rep("content34.py", "進補 — nourishing food before winter.", "進補 — 冬の前に体を養う食事。", 1)
rep("content34.py", "鋼雕 — sculpture made of steel.", "鋼雕 — 鉄で作られた彫刻。", 1)
rep("content34.py", "沙雕 — sculpture built from sand.", "沙雕 — 砂で作られた彫刻。", 1)
rep("content34.py", "節氣小表 · Solar terms", "節氣小表 · 二十四節気表", 1)
rep("content34.py", "你呢? · Over to you", "你呢? · あなたは？", 2)
rep("content34.py", "Have you seen the Fulong sand sculptures? Which film character would you most want to see in sand?",
    "福隆の砂の彫刻を見たことがありますか。砂で見てみたい映画キャラクターはどれですか。", 1)
rep("content34.py", "鋼雕行程 · Plan your visit", "鋼雕行程 · 見学プラン", 1)
rep("content34.py", "體育 · Sport", "體育 · スポーツ", 1)
rep("content34.py", "第 4 版 · 台灣大賽封王 · The Taiwan Series is decided", "第 4 版 · 台灣大賽封王 · 台湾シリーズ優勝決定", 1)
rep("content34.py", "Staff report · Source: TSNA sports news, Oct 26", "本紙スタッフ · 出典：TSNAスポーツニュース（10月26日）", 1)
rep("content34.py", "The Wei Chuan Dragons beat the CTBC Brothers 6-0 in Game 6 (Oct 26, Taipei Dome) to win the 2026 Taiwan Series 4-2 — the first-ever Dragons-Brothers final and the Dragons' 6th title. Starter C.C. Mercedes threw 8 shutout innings and was named Series MVP.",
    "味全龍は第6戦（10月26日、台北ドーム）で中信兄弟に6対0で勝利し、2026年台湾シリーズを4勝2敗で制した — 史上初の龍象対決であり、龍の6度目の優勝。先発のC.C.メルセデスは8イニングを無失点に抑え、シリーズMVPに選ばれた。", 1)
rep("content34.py", "棒球詞卡 · Baseball words", "棒球詞卡 · 野球ことばカード", 1)
rep("content34.py", "Four words: 完封 (shutout), 封王 (clinching the title), 全壘打 (home run), MVP (most valuable player).",
    "4つの言葉：完封（シャットアウト）、封王（優勝決定）、全壘打（ホームラン）、MVP（最優秀選手）。", 1)
rep("content34.py", "第六戰得分走勢 · Game 6 runs by inning — bars drawn in proportion to runs",
    "第六戰得分走勢 · 第6戦のイニング別得点 — バーは得点に比例", 1)
rep("content34.py", "Note: the Dragons did not bat in the bottom of the 9th — leading 6-0 after the top of the 9th, the game was over. 1 + 5 = 6.",
    "注：ドラゴンズは9回裏の攻撃なし — 9回表終了時点で6対0とリードし、試合終了。1 + 5 = 6。", 1)
rep("content34.py", "The Dragons won Game 6, 6-0.", "ドラゴンズは第6戦に6対0で勝利。", 1)
rep("content34.py", "The series ended 4-2 to the Dragons.", "シリーズはドラゴンズの4勝2敗で決着。", 1)
rep("content34.py", "Mercedes threw 8 shutout innings.", "メルセデスは8イニングを無失点に抑えた。", 1)
rep("content34.py", "Mercedes was named Series MVP.", "メルセデスはシリーズMVPに選ばれた。", 1)
rep("content34.py", "The Dragons' 6th title in team history.", "ドラゴンズ史上6度目の優勝。", 1)
rep("content34.py", "Three shutouts in one series is a first.", "1シリーズで3度の完封は史上初。", 1)
rep("content34.py", "Game 6 was played at the Taipei Dome.", "第6戦は台北ドームで行われた。", 1)
rep("content34.py", "A shutout: the other side scores zero.", "完封：相手の得点がゼロのこと。", 1)
rep("content34.py", "Winning the title is 封王.", "優勝することを封王という。", 1)
rep("content34.py", "A ball hit out of the park is a home run.", "場外へ打ったボールがホームラン。", 1)
rep("content34.py", "Mercedes allowed 1 run in 14 innings.", "メルセデスは14イニングで1失点のみ。", 1)
rep("content34.py", "The Dragons scored 5 runs in the 8th inning.", "ドラゴンズは8回に5点を取った。", 1)
rep("content34.py", "看圖答題 · Read the chart", "看圖答題 · グラフを読もう", 1)
rep("content34.py", "The 8th inning: 5 runs, the biggest bar.", "8回：5点で最も大きなバー。", 1)
rep("content34.py", "1 + 5 = 6 runs in total.", "1 + 5 = 合計6点。", 1)
rep("content34.py", "完封 — a shutout: the other side scores zero.", "完封 — 完封：相手の得点ゼロ。", 1)
rep("content34.py", "封王 — clinching the championship.", "封王 — 優勝を決めること。", 1)
rep("content34.py", "全壘打 — a home run.", "全壘打 — ホームラン。", 1)
rep("content34.py", "安打 — a base hit.", "安打 — ヒット。", 1)
rep("content34.py", 'instr="Match"', 'instr="語と意味を結ぶ"', 2)
rep("content34.py", 'instr="Fill in"', 'instr="空所補充"', 12)
rep("content34.py", "系列賽小檔 · Series file", "系列賽小檔 · シリーズ記録", 1)
rep("content34.py", "Which team do you support? Have you ever watched a baseball game live?",
    "どのチームを応援していますか。野球の試合を生で見たことがありますか。", 1)

# ---------------- content56: P5 + P6 ----------------
rep("content56.py", "青年 · Youth", "青年 · 若者", 1)
rep("content56.py", "第 5 版 · 天母萬聖節回顧、旅展攻略 · Halloween recap and the travel-fair game plan",
    "第 5 版 · 天母萬聖節回顧、旅展攻略 · 天母ハロウィーン回顧と旅展攻略", 1)
rep("content56.py", "Tianmu's Halloween (Oct 25-26, postponed from Oct 24 by the typhoon): the Oct 25 night parade marched from Shin Kong Mitsukoshi Tianmu along Zhongcheng Road to Dayeh Takashimaya, and the Oct 26 main event ran 13:00-20:00 at Tianmu Sports Park, with 250 shops giving treats and 4,500 pumpkin buckets from three department stores.",
    "天母のハロウィーン（10月25～26日、台風のため10月24日から延期）：10月25日の夜のパレードは新光三越台北天母店から忠誠路に沿って大葉高島屋まで行進し、10月26日のメインイベントは天母運動公園で13時から20時まで開催。250の店がお菓子を配り、3つのデパートから4,500個のパンプキンバケツが配られた。", 1)
rep("content56.py", "Travel-fair game plan: watch the shows first (Yamagata flower-hat dance, Korea's JUMP taekwondo-comedy show, the daily 14:00 mascot parade), then compare prices — budget fares often exclude checked baggage, so add that cost before you decide.",
    "旅展攻略：まずショーを見る（山形花笠舞、韓国のJUMPによるテコンドー・コメディショー、毎日14時のマスコットパレード）、それから価格を比べる — 格安運賃には預け荷物が含まれないことが多いので、決める前にその料金を加えること。", 1)
rep("content56.py", "練習例子 · Practice example", "練習例子 · 練習の例", 1)
rep("content56.py", "Practice numbers: NT$6,200 − NT$1,200 = NT$5,000, exactly his budget.",
    "計算：6,200台湾ドル − 1,200台湾ドル = 5,000台湾ドル、ちょうど予算通り。", 1)
rep("content56.py", "讀懂了嗎? · Did you get it?", "讀懂了嗎? · 読めたかな？", 1)
rep("content56.py", "The night parade marched on Sunday, Oct 25, at 19:00.", "夜のパレードは10月25日（日）19時に行進。", 1)
rep("content56.py", "The main event ran 13:00-20:00 at Tianmu Sports Park.", "メインイベントは天母運動公園で13時から20時まで開催。", 1)
rep("content56.py", "250 shops gave treats.", "250の店がお菓子を配った。", 1)
rep("content56.py", "4,500 pumpkin buckets were given out.", "4,500個のパンプキンバケツが配られた。", 1)
rep("content56.py", "The mascot parade runs daily at 14:00.", "マスコットパレードは毎日14時に開催。", 1)
rep("content56.py", "Budget fares often exclude checked baggage.", "格安運賃には預け荷物が含まれないことが多い。", 1)
rep("content56.py", "填一填 · Fill in", "填一填 · 埋めてみよう", 2)
rep("content56.py", "The parade marched along Zhongcheng Road.", "パレードは忠誠路に沿って行進。", 1)
rep("content56.py", "The Tamagotchi 30th anniversary collaboration.", "たまごっち30周年コラボレーション。", 1)
rep("content56.py", "The Yamagata flower-hat dance performs on stage.", "山形花笠舞がステージで披露される。", 1)
rep("content56.py", "Set a budget before Double 11.", "ダブルイレブンの前に予算を決める。", 1)
rep("content56.py", "Add baggage fees before comparing fares.", "運賃を比べる前に手荷物料金を加えること。", 1)
rep("content56.py", "List your cart first, then delete what you do not need.", "まずカートをリストアップし、不要なものを削除すること。", 1)
rep("content56.py", "算一算 · Work it out", "算一算 · 計算してみよう", 1)
rep("content56.py", "6,200 − 1,200 = 5,000, exactly the budget.", "6,200 − 1,200 = 5,000、ちょうど予算通り。", 1)
rep("content56.py", "The parade starts at 19:00; the main event the next day at 13:00.", "パレードは19時スタート、メインイベントは翌日13時スタート。", 1)
rep("content56.py", "討糖 — trick-or-treating.", "討糖 — トリック・オア・トリート（お菓子をもらうこと）。", 1)
rep("content56.py", "踩街 — parading through the streets in costume.", "踩街 — 仮装して街をパレードすること。", 1)
rep("content56.py", "南瓜桶 — a pumpkin bucket for treats.", "南瓜桶 — お菓子入れのパンプキンバケツ。", 1)
rep("content56.py", "打卡 — checking in with a photo on social media.", "打卡 — 写真付きでSNSにチェックインすること。", 1)
rep("content56.py", "天母時間表 · Tianmu schedule", "天母時間表 · 天母スケジュール", 1)
rep("content56.py", "你呢? · Over to you", "你呢? · あなたは？", 1)
rep("content56.py", "Have you ever worn a Halloween costume? Which character would you most want to be?",
    "ハロウィーンの仮装をしたことがありますか。なりたいキャラクターはどれですか。", 1)
rep("content56.py", "旅展表演 · Stage shows", "旅展表演 · ステージショー", 1)
rep("content56.py", "深讀 · Deep read", "深讀 · 深く読む", 1)
rep("content56.py", "第 6 版 · 金融科技週深讀 + 讀圖表 · FinTech in depth, and reading a chart",
    "第 6 版 · 金融科技週深讀 + 讀圖表 · フィンテックを深く読む・グラフを読む", 1)
rep("content56.py", "Staff report · Source: event organisers' press release (Oct 23) and event FAQ",
    "本紙スタッフ · 出典：主催者のプレスリリース（10月23日）とイベントFAQ", 1)
rep("content56.py", "Three plus signs: Finance+ (finance plus technology), AI+ (artificial intelligence inside banks, investment and insurance) and global expansion (helping start-ups sell worldwide). The scale — 45,000+ people, 120+ economies, 1,000+ speakers, 800+ exhibitors and start-ups, 30+ delegations, 100+ community events — shows fintech is now a whole-city topic.",
    "3つのプラス：金融＋（金融とテクノロジー）、AI＋（銀行・投資・保険の中のAI）、グローバル展開（スタートアップが世界へ売る手伝い）。規模 — 45,000人以上、120以上の国と地域、1,000人以上の講演者、800以上の出展者とスタートアップ、30以上の代表団、100以上のコミュニティイベント — は、フィンテックが今や街全体の話題であることを示している。", 1)
rep("content56.py", "旅展每日開放時數 · ITF opening hours per day — bars drawn in proportion to hours",
    "旅展每日開放時數 · 旅展の1日あたり開場時間 — バーは時間に比例", 1)
rep("content56.py", "Source: published fair hours (Nov 6: 12:00-18:00; Nov 7-9: 10:00-18:00). Total: 30 hours.",
    "出典：発表された開場時間（11月6日：12:00–18:00、11月7～9日：10:00–18:00）。合計30時間。", 1)
rep("content56.py", "看圖答題 · Read the chart", "看圖答題 · グラフを読もう", 1)
rep("content56.py", "Nov 6 is the shortest day: 6 hours.", "11月6日が最も短い日：6時間。", 1)
rep("content56.py", "Nov 8 runs 10:00-18:00: 8 hours.", "11月8日は10時から18時まで：8時間。", 1)
rep("content56.py", "6 + 8 + 8 + 8 = 30 hours in total.", "6 + 8 + 8 + 8 = 合計30時間。", 1)
rep("content56.py", "Nov 6 opens at noon, not 10:00.", "11月6日は10時ではなく正午に開場。", 1)
rep("content56.py", "深讀測驗 · Deep-read quiz", "深讀測驗 · 深読みクイズ", 1)
rep("content56.py", "Finance+ means finance plus technology.", "金融＋は金融にテクノロジーを加えること。", 1)
rep("content56.py", "AI helps read data, spot risks and answer clients.", "AIはデータを見て、リスクを見つけ、顧客の質問に答える手伝いをする。", 1)
rep("content56.py", "Global expansion means selling products worldwide.", "グローバル展開は製品を世界中で売ること。", 1)
rep("content56.py", "More than 1,000 speakers take part.", "1,000人以上の講演者が参加。", 1)
rep("content56.py", "The main conference runs Nov 2-3.", "メインカンファレンスは11月2～3日に開催。", 1)
rep("content56.py", "Community events number 100+ through the week.", "コミュニティイベントは週を通して100以上。", 1)
rep("content56.py", "Payments is one of the main-conference topics.", "支付はメインカンファレンスのテーマの一つ。", 1)
rep("content56.py", "Digital assets is a main-conference topic.", "數位資產はメインカンファレンスのテーマの一つ。", 1)
rep("content56.py", "Insurtech is a main-conference topic.", "保險科技はメインカンファレンスのテーマの一つ。", 1)
rep("content56.py", "The week connects start-ups with the world.", "この週はスタートアップと世界をつなぐ。", 1)
rep("content56.py", "Total opening hours: 30.", "合計開場時間：30時間。", 1)
rep("content56.py", "Nov 6 opens at noon (12:00).", "11月6日は正午（12時）に開場。", 1)
rep("content56.py", "The travel fair has 1,600 booths.", "旅展には1,600のブースがある。", 1)
rep("content56.py", "More than 45,000 people are expected.", "45,000人以上の参加が見込まれる。", 1)
rep("content56.py", "數字一覽 · By the numbers", "數字一覽 · 数字で見る", 1)
rep("content56.py", "比價提醒 · Compare carefully", "比價提醒 · 価格比較の注意", 1)
rep("content56.py", "Example from press reports (Oct 20): Cathay Pacific Taipei-Tokyo return from NT$13,433 including tax, book by Nov 13. Always compare with baggage fees added — and check the live booking result, as prices vary by date.",
    "報道（10月20日）による例：キャセイパシフィック航空の台北－東京往復は税込み13,433台湾ドルから、購入期限は11月13日。手荷物料金を加えて比べること。価格は日によって変わるため、実際の予約結果を確認すること。", 1)
rep("content56.py", 'instr="Match"', 'instr="語と意味を結ぶ"', 1)
rep("content56.py", 'instr="Fill in"', 'instr="空所補充"', 14)

# ---------------- content7: P7 ----------------
rep("content7.py", "語言 · Language focus", "語言 · ことばの焦点", 1)
rep("content7.py", "語言聚焦 · 三個級別,三個主題 · Three levels, three topics",
    "語言聚焦 · 三個級別,三個主題 · 3つのレベル、3つのテーマ", 1)
rep("content7.py", "A2 · 展會的話 · Fair words", "A2 · 展會的話 · 展示会のことば", 1)
rep("content7.py", "This week's fairs give you four useful words: 旅展 (travel fair), 攤位 (booth), 集章 (stamp-collecting) and 吉祥物大遊行 (mascot parade). Learn them once, and the whole travel fair makes sense.",
    "今週の展示会から、役立つ言葉を4つ紹介する：旅展（旅行展覧会）、攤位（ブース）、集章（スタンプ集め）、吉祥物大遊行（マスコットパレード）。一度覚えれば、旅展全体が理解できる。", 1)
rep("content7.py", "Four fair words: 旅展, 攤位, 集章, 吉祥物大遊行.", "展示会の言葉4つ：旅展、攤位、集章、吉祥物大遊行。", 1)
rep("content7.py", "旅展 is short for 旅行展覽會 (travel exhibition). A 攤位 is one stall inside the fair; the Taipei fair has 1,600 of them. 集章 means collecting stamps at set points — collect all six Greenway stamps and you win a prize.",
    "旅展は旅行展覽會（旅行展覧会）の略。攤位は展示会の中の一つの出店で、台北の旅展には1,600もある。集章は決められた場所でスタンプを集めることで、6つのグリーンウェイのスタンプを全部集めると賞品がもらえる。", 1)
rep("content7.py", "A booth inside the fair is a 攤位.", "展示会の中のブースが攤位。", 1)
rep("content7.py", "The mascot parade runs daily at 14:00.", "マスコットパレードは毎日14時に開催。", 1)
rep("content7.py", "Collecting stamps at set points is 集章.", "決められた場所でスタンプを集めることが集章。", 1)
rep("content7.py", "The travel fair is at the Nangang Exhibition Center.", "旅展は南港展覧館で開催。", 1)
rep("content7.py", "Practise: 「旅展幾點開門？」 ('What time does the fair open?') — Friday opens at noon, other days at 10:00.",
    "練習：「旅展幾點開門？」（旅展は何時に開きますか）— 金曜日は正午開場、他の日は10時開場。", 1)
rep("content7.py", "B1 · 球賽與節氣 · Games & seasons", "B1 · 球賽與節氣 · 試合と季節", 1)
rep("content7.py", "Sport and seasons share this week's headlines. Group the words and they stick: winning （封王、完封） and winter （立冬、進補）.",
    "スポーツと季節が今週の見出しを分け合っている。言葉をグループにすると覚えやすい：勝利（封王、完封）と冬（立冬、進補）。", 1)
rep("content7.py", "Group the words: winning (封王/完封), winter (立冬/進補).", "言葉をグループに：勝利（封王／完封）、冬（立冬／進補）。", 1)
rep("content7.py", "封王 means clinching the championship; 完封 means shutting the other side out, 0 runs. 立冬 is the solar term that starts winter; 進補 is eating nourishing hot food before the cold months.",
    "封王は優勝を決めること、完封は相手を無得点に抑えること（0点）。立冬は冬を始める節気、進補は寒い季節の前に体に良い温かいものを食べること。", 1)
rep("content7.py", "Winning the title is 封王.", "優勝することを封王という。", 1)
rep("content7.py", "完封 means the other side scores zero.", "完封は相手の得点がゼロという意味。", 1)
rep("content7.py", "Lidong starts winter.", "立冬は冬の始まり。", 1)
rep("content7.py", "Ginger duck is a Lidong dish.", "薑母鴨は立冬の代表的な料理。", 1)
rep("content7.py", "Memory trick: learn 封王 first, then the way it was won （完封）, then the season it happened in （立冬）.",
    "覚え方のコツ：まず封王を覚え、次にその勝ち方（完封）、そしてそれが起きた季節（立冬）を覚える。", 1)
rep("content7.py", "B2 · 港台說法 · Local talk", "B2 · 港台說法 · 台湾・香港の言い方", 1)
rep("content7.py", "Taiwan and Hong Kong each have their own way of saying things. This week: 打卡 (check in with a photo), 討糖 (trick-or-treat), 踩街 (street parade in costume) and 泡湯 (soak in a hot spring).",
    "台湾と香港にはそれぞれ独自の言い方がある。今週は：打卡（写真付きチェックイン）、討糖（トリック・オア・トリート）、踩街（仮装した街のパレード）、泡湯（温泉につかること）。", 1)
rep("content7.py", "Four local words from this issue: 打卡, 討糖, 踩街, 泡湯.", "今号の現地の言葉4つ：打卡、討糖、踩街、泡湯。", 1)
rep("content7.py", "打卡 started as clocking in at work, but at a fair or festival it means posting a photo to say 'I was here'. 討糖 is what children say at shops at Halloween; 踩街 is the costumed parade itself; 泡湯 is the autumn pleasure of a hot-spring bath.",
    "打卡はもともと出勤の打刻だったが、展示会や祭りでは写真を投稿して「ここに来た」と伝える意味になる。討糖はハロウィーンに子どもが店で言う言葉、踩街は仮装したパレードそのもの、泡湯は秋の楽しみの温泉浴。", 1)
rep("content7.py", "At a festival, 打卡 means posting a photo to say you were there.", "祭りでは、打卡は写真を投稿して来たことを伝える意味。", 1)
rep("content7.py", "Trick-or-treating is 討糖.", "トリック・オア・トリートが討糖。", 1)
rep("content7.py", "踩街 is a costumed street parade.", "踩街は仮装した街のパレード。", 1)
rep("content7.py", "Soaking in a hot spring is 泡湯.", "温泉につかってくつろぐことが泡湯。", 1)
rep("content7.py", "You don't need many local sayings — learn four and every outing feels closer.",
    "現地の言い回しをたくさん覚える必要はない — 4つ覚えれば、どのお出かけも身近に感じられる。", 1)
rep("content7.py", "易錯診所 · Error clinic", "易錯診所 · 間違いクリニック", 1)
rep("content7.py", "完勝 means winning big; 完封 means the other side scored zero.", "完勝は大勝ちの意味、完封は相手の得点がゼロの意味。", 1)
rep("content7.py", "Lidong starts winter; the Solstice is the shortest day. Different terms.", "立冬は冬の始まり、冬至は昼が最も短い日。別の節気。", 1)
rep("content7.py", "Check the city: FinTech Week opens in Hong Kong, not Taipei.", "都市を確認：フィンテックウィークは台北ではなく香港で開幕。", 1)
rep("content7.py", "本週句式 · Sentence frame", "本週句式 · 今週の文型", 1)
rep("content7.py", "「先去集章，再去看表演。」 — the frame 先…再… gives the order of two actions: first X, then Y. Make your own: 先比價，再結帳 (compare prices first, then pay).",
    "「先去集章，再去看表演。」 — 文型「先…再…」は2つの動作の順序を示す：まずX、それからY。自分で作ってみよう：先比價，再結帳（まず価格を比べ、それから支払う）。", 1)
rep("content7.py", "Frame: 先…再… — first X, then Y. Make your own sentence with it.",
    "文型：先…再… — まずX、それからY。この文型で自分の文を作ってみよう。", 1)
rep("content7.py", "讀者園地 · Readers' corner", "讀者園地 · 読者の広場", 1)
rep("content7.py", "An editor's example letter — not a real one. Deferral notice: VOL.1 promised real letters and best page-8 writing from this issue; none publishable had arrived by press time, so the example stays and the invitation stays open.",
    "これは編集部の例文で、本物の投書ではない。VOL.1は今号から本物の手紙と第8版の優秀作文を掲載するとしたが、締切までに掲載できる投書がなく、例文を掲載し、募集は続けている。あなたの手紙を次号でお待ちしています。", 1)
# Readers'-corner box: the core's height formula runs ~8px short of the
# rendered last-line ink (audit BOXTITLE on the 7-line draft). Shortened
# disclosure (6 lines) + bottom pad 26 -> 42 keeps ink inside the border
# with margin and keeps the P7 teaser clear of the 2580 footer rule.
rep("content7.py", "len(wrap(lcn, \"sans\", False, 20, CW - 44)) * 29 + 26",
    "len(wrap(lcn, \"sans\", False, 20, CW - 44)) * 29 + 42", 1)
rep("content7.py", "本週金句 · Phrases of the week — word for word from this issue's articles",
    "本週金句 · 今週のフレーズ — 本文から一字一句そのまま", 1)
rep("content7.py", "Pay by phone, scan to pay, buy insurance online — that is fintech.",
    "電話で支払い、スキャンで支払い、オンラインで保険を買う — それがフィンテック。", 1)
rep("content7.py", "123 countries and cities, 1,600 booths.", "123の国と都市、1,600のブース。", 1)
rep("content7.py", "Buy what you need; don't buy a pile of things you won't use just for a discount.",
    "必要なものを買うこと。割引のためだけに使わないものを山ほど買わないこと。", 1)
rep("content7.py", "In Kaohsiung, even steel can become a stage.", "高雄では、鉄でさえ舞台になる。", 1)
rep("content7.py", "Fulong's summer came to an end on October 26.", "福隆の夏は10月26日に終わりを迎えた。", 1)
rep("content7.py", "A 6-0 shutout of the Brothers, and the Dragons threw the red ribbons.",
    "兄弟に6対0の完封勝利、そして龍は赤いリボンを投げた。", 1)
rep("content7.py", "250 shops giving treats together.", "250の店が一緒にお菓子を配る。", 1)
rep("content7.py", "On the fair's first day the doors open only at noon.", "旅展の初日は正午にしか開場しない。", 1)
rep("content7.py", "下期預告 · Next week (VOL.3)", "下期預告 · 次号予告（VOL.3）", 1)
rep("content7.py", 'instr="Fill in"', 'instr="空所補充"', 6)

# ---------------- content8: P8 ----------------
rep("content8.py", "測驗與答案 · Test & keys", "測驗與答案 · テストと答え", 1)
rep("content8.py", "第 8 版 · 本週大測驗 + 全部答案 · This week's test and every answer key",
    "第 8 版 · 本週大測驗 + 全部答案 · 今週のテストと全解答", 1)
rep("content8.py", "A · 判斷對錯 · True or false", "A · 判斷對錯 · 正しいか間違いか", 1)
rep("content8.py", "FinTech Week opens Monday, Nov 2.", "フィンテックウィークは11月2日（月）に開幕。", 1)
rep("content8.py", "Lidong is Nov 7, not Nov 6.", "立冬は11月6日ではなく11月7日。", 1)
rep("content8.py", "The Dragons won the series 4-2.", "ドラゴンズはシリーズに4勝2敗で勝利。", 2)
rep("content8.py", "Game 6 ended 6-0, not 6-3.", "第6戦は6対3ではなく6対0で終了。", 1)
rep("content8.py", "The sand festival closed Oct 26.", "砂の祭典は10月26日に閉幕。", 1)
rep("content8.py", "The travel fair opens at noon on Nov 6, not 10:00.", "旅展は11月6日、10時ではなく正午に開場。", 1)
rep("content8.py", "B · 本週大測驗 · The big quiz", "B · 本週大測驗 · 総合クイズ", 1)
rep("content8.py", "The main conference is Nov 2-3.", "メインカンファレンスは11月2～3日。", 1)
rep("content8.py", "The travel fair runs to Monday, Nov 9.", "旅展は11月9日（月）まで開催。", 1)
rep("content8.py", "The steel festival runs to Nov 22.", "鉄の彫刻祭は11月22日まで。", 1)
rep("content8.py", "The night parade marched Oct 25 at 19:00.", "夜のパレードは10月25日19時に行進。", 1)
rep("content8.py", "Double 11 is Wednesday, Nov 11.", "ダブルイレブンは11月11日（水）。", 1)
rep("content8.py", "Mercedes allowed 1 run in 14 innings.", "メルセデスは14イニングで1失点のみ。", 1)
rep("content8.py", "The mascot parade runs daily at 14:00.", "マスコットパレードは毎日14時に開催。", 1)
rep("content8.py", "The trail encyclopaedia collects 56 routes.", "歩道百科には56のルートが収録されている。", 1)
rep("content8.py", "Total opening hours: 6 + 8 + 8 + 8 = 30.", "合計開場時間：6 + 8 + 8 + 8 = 30。", 1)
rep("content8.py", "The stamp challenge covers 6 Greenways.", "スタンプチャレンジの対象は6つのグリーンウェイ。", 1)
rep("content8.py", "C · 完成句子 · Fill in", "C · 完成句子 · 文を完成させよう", 1)
rep("content8.py", "Fintech: technology running financial services.", "フィンテック：テクノロジーで動く金融サービス。", 1)
rep("content8.py", "Lidong starts winter.", "立冬は冬の始まり。", 1)
rep("content8.py", "A shutout: the other side scores zero.", "完封：相手の得点がゼロのこと。", 1)
rep("content8.py", "Winning the title is 封王.", "優勝することを封王という。", 1)
rep("content8.py", "Trick-or-treating is 討糖.", "トリック・オア・トリートが討糖。", 1)
rep("content8.py", "Collecting stamps is 集章.", "スタンプを集めることが集章。", 1)
rep("content8.py", "The travel fair is at the Nangang Exhibition Center.", "旅展は南港展覧館で開催。", 1)
rep("content8.py", "Pier-2 hosts the steel festival.", "駁二が鉄の彫刻祭の会場。", 1)
rep("content8.py", "Global expansion: selling products worldwide.", "グローバル展開：製品を世界中で売ること。", 1)
rep("content8.py", "AI inside finance is 人工智慧＋.", "金融の中のAIは人工智慧＋。", 1)
rep("content8.py", "D · 讀一讀,答一答 · Read and answer", "D · 讀一讀,答一答 · 読んで答えよう", 1)
rep("content8.py", "He goes to the travel fair on Friday at noon.", "彼は金曜日の正午に旅展へ行く。", 1)
rep("content8.py", "The parade is at 14:00.", "パレードは14時。", 1)
rep("content8.py", "A set of 4 coupons costs 4,100 (list price 8,200).", "4枚セットのクーポンは4,100（定価8,200）。", 1)
rep("content8.py", "He eats ginger duck for Lidong on Saturday.", "彼は土曜日の立冬に薑母鴨を食べる。", 1)
rep("content8.py", "Order: fair, then Lidong pot, then the coupon set for a buffet.", "順序：旅展、次に立冬の鍋、それからビュッフェのクーポンセット。", 1)
rep("content8.py", "E · 情景說話 · Say it in context", "E · 情景說話 · 会話の場面", 1)
rep("content8.py", "The travel fair opens Friday at noon.", "旅展は金曜日の正午に開幕。", 1)
rep("content8.py", "Lidong is the first solar term of winter.", "立冬は冬の最初の節気。", 1)
rep("content8.py", "A shutout means the other side scores zero.", "完封は相手の得点がゼロという意味。", 1)
rep("content8.py", "The mascot parade is at 14:00 daily.", "マスコットパレードは毎日14時。", 1)
rep("content8.py", "Compare prices first, then pay: 先比價，再結帳.", "まず価格を比べ、それから支払う：先比價，再結帳。", 1)
rep("content8.py", "F · 寫一寫 · Writing", "F · 寫一寫 · 書いてみよう", 1)
rep("content8.py", 'f.glossline(f"Writing — there is no single right answer. A {NCHARS}-character model follows.")',
    'f.glossline(f"作文 — 正解は一つだけではありません。{NCHARS}字のモデル解答が続きます。")', 1)
rep("content8.py", 'f"Open task - the model answer is printed in section F above ({NCHARS} characters)"',
    'f"開放課題 — モデル解答は上のF欄に掲載({NCHARS}字)"', 1)
rep("content8.py", 'instr="Writing"', 'instr="作文"', 1)
rep("content8.py", 'f.para("Model answer: " + MODELO', 'f.para("モデル解答：" + MODELO', 1)
rep("content8.py", "答案 · Answer keys — in page order, with a short English note for every item",
    "答案 · 全解答と解説（1–8ページ）", 1)
rep("content8.py", "All notes in English · ✓ = the writing model", "解説はすべて日本語 · ✓ = 作文の課題", 1)
rep("content8.py", 'f"— Page {pg} —"', 'f"— {pg} ページ —"', 1)
rep("content8.py", 'instr="Fill in"', 'instr="空所補充"', 10)

print(f"transform OK: {len(LOG)} replacements")
for line in LOG:
    print("  ", line)
