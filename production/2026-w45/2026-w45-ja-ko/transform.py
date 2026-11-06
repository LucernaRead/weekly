# -*- coding: utf-8 -*-
"""JA core (VOL.2, Chinese explanations) -> JA x KO edition transform.

Re-runnable: reads the PRISTINE W45 JA core build, applies exact-literal
replacements (whole strings, never AST byte offsets, never byte slicing),
and writes the edition build into this directory. Fix rounds edit THIS
file, then re-run: transform.py -> run.py (one process) -> render.py.

Frozen: every Japanese article/stem/option/letter/figure string is copied
byte-identical, including the P7 column definition sentences (only the
gloss/bridge layer is localized). Only the explanation layer changes:
Chinese notes/glosses/headers/instructions -> Korean, per the W43 JA x KO
shipped precedent (files/weekly-report-ja-ko).

Masthead geometry: wordmark 262 -> 248 (W43 same-pairing JA x KO
precedent, which outranks the README #20 generalization; the #20 JA-family
wordmark note was written for JA x ZH-TW and cannot overturn this
pairing's own shipped precedent), subtitle 330 -> 316, badge INSERTED
at (975, 356) 19pt sans bold BRICK with the verbatim W43 JA x KO badge
string, slogan 372 -> 390, double rules 392/401 -> 406/413, dark band
stays at 424. Fix round (wordmark): 262 -> 248 only; subtitle 316,
badge 356, slogan 390, rules 406/413, band 424 already at W43 positions
and NOT moved.
"""
import hashlib
import os
import re
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
CORE = os.path.expanduser(
    "~/workspace/goals/lucernaread-social-media-operations/"
    "hidden_files/weekly-report-w45-ja-build")
EDITION = os.path.expanduser(
    "~/workspace/goals/lucernaread-social-media-operations/"
    "files/weekly-report-w45-ja-ko")
CANON_SVGLIB_MD5 = "d73e23b365676c3618d7e060b835eb4d"

# (old, new) applied in order. Longer strings first where one contains another.
GLOBAL = [
    # --- output repoint ---
    ("weekly-report-w45-ja-core", "weekly-report-w45-ja-ko"),
    # --- registry type names / instructions (W43 JA x KO wording) ---
    ('instr="造句"', 'instr="문장 만들기"'),
    ('instr="翻译"', 'instr="번역"'),
    ('instr="写作"', 'instr="쓰기"'),
    ('instr="判断"', 'instr="참 / 거짓"'),
    ('instr="填空"', 'instr="빈칸 채우기"'),
    ('instr="把词和释义配对"', 'instr="단어와 뜻 짝짓기"'),
    ('instr="把活动和地点·时间配对"', 'instr="행사와 장소·시간 짝짓기"'),
    ('"完形单选"', '"빈칸 객관식"'),
    ('"单选"', '"객관식"'),
    ('"完成句子"', '"문장 완성"'),
    ('"词汇配对"', '"단어 짝짓기"'),
    ('"造句"', '"문장 만들기"'),
    ('"判断对错"', '"읽기 판단"'),
    ('"翻译"', '"번역"'),
    ('"写作"', '"쓰기"'),
    # --- shared furniture ---
    ('"あなたは？ · 说说你自己"', '"あなたは？ · 여러분은요?"'),
    ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
     '"정답은 8면 · 레벨이 섞인 문제예요. 번호로 찾으세요"'),
]

# Answer-note translations. One Korean rendering per distinct core note;
# duplicates share the rendering (correct: same note -> same meaning).
NOTES = [
    ("文化日在11月3日（周二）", "문화의 날은 11월 3일(화)이에요"),
    ("读书周到11月9日（周一）", "독서 주간은 11월 9일(월)까지예요"),
    ("見頃＝最佳观赏期", "見頃 = 가장 보기 좋은 때"),
    ("立冬＝冬天的开始", "立冬 = 겨울의 시작"),
    ("神户灯光秀从7日（周六）开始", "고베 라이트업은 7일(토)부터 시작해요"),
    ("文化日全国都有文化活动", "문화의 날에는 전국에서 문화 행사가 열려요"),
    ("立冬在11月7日（周六）", "입동은 11월 7일(토)이에요"),
    ("灯光秀在神户开始", "라이트업은 고베에서 시작해요"),
    ("「ゆる」＝无理をしない", "「ゆる」 = 무리하지 않기"),
    ("鍋の食卓は去年の1.5倍", "나베 식탁은 지난해의 1.5배예요"),
    ("発表は10月21日", "발표는 10월 21일이었어요"),
    ("11月から1月まで気温は平年より高い", "11월부터 1월까지 기온은 평년보다 높아요"),
    ("服と食事の話題はnoteのまとめによるもの", "옷과 음식 화제는 note 정리에서 왔어요"),
    ("ゆる＝轻松、不勉强", "ゆる = 무리하지 않고 여유롭게"),
    ("蒸し器＝蒸笼", "蒸し器 = 찜기"),
    ("整える＝调理、调养", "整える = 몸과 마음을 다스리기"),
    ("鍋＝一锅菜", "鍋 = 한 솥 요리"),
    ("鍋の材料が1か月早く並んだ", "나베 재료가 한 달 일찍 진열됐어요"),
    ("気象庁の予報は10月20日", "기상청 예보는 10월 20일이었어요"),
    ("サクサクdeコパンが1,300万食を超えた", "사쿠사쿠de코판이 1,300만 끼를 넘었어요"),
    ("ゆる＝轻松 b", "ゆる = 무리하지 않고 여유롭게 b"),
    ("蒸し器＝蒸笼 a", "蒸し器 = 찜기 a"),
    ("麻辣湯＝辛いスープ d", "麻辣湯 = 매운 수프 요리 d"),
    ("予報＝天気の予想 c", "予報 = 날씨 예상 c"),
    ("杉并的活动是家庭管弦乐队", "스기나미 행사는 가족 오케스트라예요"),
    ("传统工艺展在石川县立美术馆", "전통 공예전은 이시카와 현립 미술관에 있어요"),
    ("传统工艺展到11月8日", "전통 공예전은 11월 8일까지예요"),
    ("灯光秀在金泽城和兼六园", "라이트업은 가나자와성과 겐로쿠엔에 있어요"),
    ("市場＝集市", "市場 = 시장"),
    ("工芸＝工艺", "工芸 = 공예"),
    ("陶器＝陶瓷", "陶器 = 도자기"),
    ("工艺展到11月8日（周日）", "전시는 11월 8일(일)까지예요"),
    ("金箔＝金箔", "金箔 = 금박"),
    # P8 #37 bare note (P3 exercise, key 8) — distinct from the suffixed
    # note above and from the 传统… note. Verified fact: the exhibition
    # runs to November 8, which is a Sunday in 2026 (P3 stem:
    # 展覧会は11月 ___ 日（日）までです。). The bare note itself carries
    # no weekday, so the Korean rendering keeps no weekday either,
    # mirroring the JA x EN fix-5 rendering.
    ("工艺展到11月8日", "전시는 11월 8일까지예요"),
    ("主语＋时间", "주어 + 시간"),
    ("地点＋で＋あります", "장소 + で + あります"),
    ("见たい＝想看", "見たい = 보고 싶다"),
    ("和家人一起", "가족과 함께"),
    ("文化の日＝11月3日 b", "文化の日 = 11월 3일 b"),
    ("工芸展＝美術館 c", "工芸展 = 미술관 c"),
    ("オーケストラ＝杉並 d", "オーケストラ = 스기나미 d"),
    ("ライトアップ＝金沢城 a", "ライトアップ = 가나자와성 a"),
    ("第1战软银3-1胜DeNA", "1차전은 소프트뱅크가 DeNA를 3-1로 이겼어요"),
    ("第2战逆转的是筒香的3分本垒打", "2차전을 뒤집은 것은 쓰쓰고의 3점 홈런이에요"),
    ("2连胜开局的是软银", "2연승으로 시작한 것은 소프트뱅크예요"),
    ("2连胜开局的夺冠率是73%", "2연승으로 시작한 팀의 우승 확률은 73%예요"),
    ("2024年夺冠的是DeNA", "2024년에 우승한 것은 DeNA예요"),
    ("第1战软银得3分", "1차전에서 소프트뱅크는 3점을 냈어요"),
    ("第2战软银得4分", "2차전에서 소프트뱅크는 4점을 냈어요"),
    ("第1战打到延长11局", "1차전은 연장 11회까지 갔어요"),
    ("第2战打到延长10局", "2차전은 연장 10회까지 갔어요"),
    ("夺冠率73%", "우승 확률 73%"),
    ("延長＝比赛延长", "延長 = 경기가 길어지기"),
    ("第1战观众33,388人", "1차전 관객 33,388명"),
    ("第2战观众33,432人", "2차전 관객 33,432명"),
    ("相川监督说「4场胜负之战」", "아이카와 감독은 「4번 이기는 싸움」이라고 했어요"),
    ("第1戦は土よう日です", "1차전은 토요일이에요"),
    ("ソフトバンクが2連勝しました", "소프트뱅크가 2연승했어요"),
    ("第2戦も延長戦でした", "2차전도 연장전이었어요"),
    ("2024年はDeNAが優勝しました", "2024년에는 DeNA가 우승했어요"),
    ("万圣节在10月31日（周六）", "할로윈은 10월 31일(토)이었어요"),
    ("涩谷禁酒时间是18时到5时", "시부야 길거리 음주는 18시부터 5시까지 안 돼요"),
    ("乱扔垃圾罚款2,000日元", "쓰레기를 버리면 벌금 2,000엔이에요"),
    ("化妆活动在池袋", "코스프레 축제는 이케부쿠로에 있어요"),
    ("横滨中区民祭在11月8日（周日）", "요코하마 나카구 축제는 11월 8일(일)이에요"),
    ("万圣节在10月31日", "할로윈은 10월 31일이었어요"),
    ("禁酒从18时开始", "음주 금지는 18시부터 시작해요"),
    ("禁酒到早上5时", "음주 금지는 아침 5시까지예요"),
    ("横滨祭典在11月8日", "요코하마 축제는 11월 8일이에요"),
    ("夜里路上不能喝酒", "밤에는 길에서 술을 마실 수 없어요"),
    ("ゴミの罰金は今年6月からです", "쓰레기 벌금은 올해 6월부터예요"),
    ("コスプレフェスは池袋です", "코스프레 축제는 이케부쿠로예요"),
    ("ハロウィンは10月31日（土）", "할로윈은 10월 31일(토)이었어요"),
    ("飲むことができません＝不能喝", "飲むことができません = 마실 수 없어요"),
    ("守って、〜しましょう", "守って + 〜しましょう = 규칙을 지키고, ~해요"),
    ("フェンスの中＝围栏里面", "フェンスの中 = 울타리 안"),
    ("活动从10月30日到11月1日", "행사는 10월 30일부터 11월 1일까지였어요"),
    ("雨が多いのは太平洋側", "비가 많은 곳은 태평양 쪽이에요"),
    ("九州の旅の検索は去年のほぼ2倍", "규슈 여행 검색은 지난해의 거의 2배예요"),
    ("1回の旅の予算は下がった", "한 번 여행의 예산은 줄었어요"),
    ("鳴子峡の見頃は10月31日から11月8日の週末", "나루코쿄의 절정은 10월 31일부터 11월 8일의 주말이에요"),
    ("图中最受欢迎的是近处的满足感", "그래프 1위는 가까운 곳에서의 만족이에요"),
    ("近场满足感38%", "가까운 곳에서의 만족 38%"),
    ("温泉27%", "온천 27%"),
    ("红叶21%与美食14%之差为7", "단풍 21%와 맛집 14%의 차이는 7"),
    ("38+27=65", "38 + 27 = 65"),
    ("四项合计100%", "네 항목 합계 100%"),
    ("立冬在11月7日", "입동은 11월 7일이에요"),
    ("神户灯光秀到12月28日", "고베 라이트업은 12월 28일까지예요"),
    ("九州旅行搜索约为去年的2倍", "규슈 여행 검색은 지난해의 거의 2배예요"),
    ("气象厅预报在10月20日", "기상청 예보는 10월 20일이었어요"),
    ("11月は平年より暖かい予報です", "11월은 평년보다 따뜻하다는 예보예요"),
    ("九州の旅の検索は増えました", "규슈 여행 검색은 늘었어요"),
    ("グラフは練習用データです", "그래프는 연습용 데이터예요"),
    ("读书周从10月27日（周二）开始", "독서 주간은 10월 27일(화)부터 시작했어요"),
    ("读书周到11月9日", "독서 주간은 11월 9일까지예요"),
    ("口号是「静かだけど、冒険中。」", "슬로건은 「静かだけど、冒険中。」예요"),
    ("图书馆活动有图书介绍", "도서관 행사는 책 소개예요"),
    ("見頃＝红叶最美的时候", "見頃 = 단풍이 가장 아름다울 때"),
    ("紅葉狩り＝去看红叶", "紅葉狩り = 단풍 구경 가기"),
    ("ライトアップ＝夜里用灯光照亮", "ライトアップ = 밤에 빛으로 비추기"),
    ("落葉＝落叶", "落葉 = 낙엽"),
    ("1.5倍＝比去年多50%", "1.5배 = 지난해보다 50% 많기"),
    ("73%≈4人中的3人", "73% ≈ 4명 중 3명"),
    ("サクサクdeコパンが1,300万食", "사쿠사쿠de코판이 1,300만 끼"),
    ("日本大赛第1战在10月24日（周六）", "일본시리즈 1차전은 10월 24일(토)이었어요"),
    ("第2战软银4-3获胜", "2차전은 소프트뱅크가 4-3으로 이겼어요"),
    ("神户灯光秀从7日开始", "고베 라이트업은 7일부터 시작해요"),
    ("2连胜开局的夺冠率73%", "2연승으로 시작한 팀의 우승 확률 73%"),
    ("气象厅预报气温高于往年", "기상청 예보는 평년보다 따뜻해요"),
    ("美香周二和家人去金泽", "미카는 화요일에 가족과 가나자와에 가요"),
    ("在金泽看传统工艺展和灯光秀", "가나자와에서 전통 공예전과 라이트업을 봐요"),
    ("周六和朋友去神户", "토요일에 친구와 고베에 가요"),
    ("读书周想借2本书", "독서 주간에 책 2권을 빌리고 싶어 해요"),
    ("主语＋时间＋地点＋动词", "주어 + 시간 + 장소 + 동사"),
    ("场所用「で」", "장소는 「で」를 써요"),
    ("2连胜开局", "2연승으로 시작하기"),
    ("見頃＝最佳观赏期 b", "見頃 = 가장 보기 좋은 때 b"),
    ("鍋＝一锅菜 d", "鍋 = 한 솥 요리 d"),
    ("落葉＝落叶 a", "落葉 = 낙엽 a"),
    ("予算＝预算 c", "予算 = 예산 c"),
    ("見せてください＝请出示", "見せてください = 보여 주세요"),
    ("借りられます＝能借（可能形）", "借りられます = 빌릴 수 있다(가능형)"),
    ("读书周到11月9日（第7版）", "독서 주간은 11월 9일까지(7면)"),
    ("「紅葉の本」受欢迎", "「紅葉の本」이 인기예요"),
    ("どういたしまして＝不客气", "どういたしまして = 천만에요"),
    ("对照第3版", "3면 참조"),
    ("对照第5版", "5면 참조"),
    ("对照第7版", "7면 참조"),
    ("对照第6版（神户的灯光秀）", "6면 참조(고베 라이트업)"),
]

# Per-file furniture / gloss / structural replacements.
PER_FILE = {
    "bslib4.py": [
        ('("译注｜" + s,', '("해설 — " + s,'),
        ('"Lucerna · 日语周报 VOL.2 · LUCERNA JAPANESE WEEKLY"',
         '"Lucerna · 일본어 주간지 VOL.2 · 텍스트는 일본어 · 해설은 한국어"'),
        ('f"第 {n} 版 / 共 {total} 版"', 'f"제 {n} 면 / 총 {total} 면"'),
    ],
    "content12.py": [
        # P1 masthead -> W43 JA x KO geometry (wordmark 262 -> 248 per
        # W43 same-pairing precedent; subtitle 316, badge 356, slogan 390,
        # rules 406/413, band 424 — all already at W43 positions, NOT moved).
        ('p.text(975, 262, "Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")',
         'p.text(975, 248, "Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")'),
        ('p.text(975, 330, "日本語版 · VOL.2 · 文化の日 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")',
         'p.text(975, 316, "日本語版 · VOL.2 · 文化の日 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")\n'
         'p.text(975, 356, "일본어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판", 19, "sans", True, BRICK, anchor="middle")'),
        ('p.text(975, 372, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")',
         'p.text(975, 390, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")'),
        ('p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)',
         'p.hline(MX, RIGHT, 406, INK, 3); p.hline(MX, RIGHT, 413, INK, 1.2)'),
        ('"毎週、日本語で · 每周一期 · 日本人が読んでいる日本語を読む"',
         '"毎週、日本語で · 매주 발행 · 日本人が読んでいる日本語を読む"'),
        ('"周二是文化日"', '"화요일은 문화의 날"'),
        ('"节日过后，红叶周末到来 · 详见第 3 版"',
         '"연휴 뒤 단풍 주말이 와요 · 자세한 것은 3면"'),
        ('"トップニュース · 头条"', '"トップニュース · 헤드라인"'),
        ('"祝日 节假日 · 見頃 最佳观赏期 · 暦 历法 · お届けします 为您送上。"',
         '"祝日 공휴일 · 見頃 가장 보기 좋은 때 · 暦 달력 · お届けします 전해 드려요."'),
        ('"数字で見る今週 · 数字看本周"', '"数字で見る今週 · 한 주의 숫자"'),
        ('"今すぐ練習 · 即学即练"', '"今すぐ練習 · 바로 연습"'),
        ('"这四个话题，都是本期报纸的主题。"',
         '"이 네 가지 주제가 이번 호 신문의 주제예요."'),
        ('"来源与日期见各篇文章，非精确统计"',
         '"날짜는 기사 참조 · 정확한 통계 아님"'),
        ('"この号の内容 · 本期目录"', '"この号の内容 · 이번 호 목차"'),
        ('"今週のことば · 本周单词"', '"今週のことば · 이번 주 단어"'),
        ('"ゆる＝ 轻松、不勉强。"', '"ゆる = 무리하지 않고, 여유롭게."'),
        ('"短いニュース · 快讯"', '"短いニュース · 짧은 소식"'),
        ('"クイズ · 闪电问答"', '"クイズ · 번개 퀴즈"'),
        ('"读头版，选出正确答案 · 答案见第 8 版"',
         '"1면을 읽고 알맞은 답을 고르세요 · 정답은 8면"'),
        # P2
        ('"レベル A2 · ゆる整え食と暖かい11月 · 轻松食养与暖和的11月"',
         '"レベル A2 · ゆる整え食と暖かい11月 · 가볍게 차리는 식탁과 따뜻한 11월"'),
        ('"蒸す 蒸 · 並ぶ 摆上货架 · 食卓 餐桌 · 超える 超过。"',
         '"蒸す 찌다 · 並ぶ 진열되다 · 食卓 식탁 · 超える 넘다."'),
        ('"予報 预报 · 平年 往年平均 · 季節風 季风 · 話題 话题 · 値上がり 涨价。"',
         '"予報 예보 · 平年 평년 · 季節風 계절풍 · 話題 화제 · 値上がり 가격 상승."'),
        # Reader prompt: the printed line AND the box-height wrap call
        # share this literal; replacing both keeps the box height honest
        # for the Korean line count (the core height formula wraps the
        # reader-language string).
        ('"你呢？寒冷的日子想吃什么锅？写两句日语寄来。"',
         '"여러분은요? 추운 날에는 어떤 나베를 먹고 싶어요? 일본어로 두 문장 써서 보내 주세요."'),
        ('"季節のことば · 季节词语"', '"季節のことば · 계절의 말"'),
        ('"ゆる整え食の4つの言葉 · 关于轻松食养的四个词"',
         '"ゆる整え食の4つの言葉 · 가볍게 차리는 식탁의 단어 네 개"'),
        ('"一锅菜"', '"한 솥 요리"'),
        ('"蒸笼"', '"찜기"'),
        ('"轻松、不勉强"', '"무리하지 않고 여유롭게"'),
        ('"调理、调养"', '"몸과 마음을 다스리기"'),
        ('"練習 · 第 2 版练习"', '"練習 · 2면 연습"'),
    ],
    "content34.py": [
        ('"レベル A2→B1 · 文化の日と金沢 · 文化日与金泽"',
         '"レベル A2→B1 · 文化の日と金沢 · 문화의 날과 가나자와"'),
        ('"市場 市场 · 工芸 工艺 · 光 灯光 · 楽しむ 享受。"',
         '"市場 시장 · 工芸 공예 · 光 빛 · 楽しむ 즐기다."'),
        ('"陶器 陶瓷 · 漆器 漆器 · 染物 染色织物 · 金箔 金箔。"',
         '"陶器 도자기 · 漆器 옻칠 그릇 · 染物 염색 직물 · 金箔 금박."'),
        ('"你呢？文化日想去参加什么文化活动？写两句日语寄来。"',
         '"여러분은요? 문화의 날에 어떤 문화 행사에 가고 싶어요? 일본어로 두 문장 써서 보내 주세요."'),
        ('"練習 · 第 3 版练习"', '"練習 · 3면 연습"'),
        ('"スポーツ · 体育"', '"スポーツ · 체육"'),
        ('"レベル B1 · 日本シリーズ横浜の2試合 · 日本大赛横滨两场"',
         '"レベル B1 · 日本シリーズ横浜の2試合 · 일본시리즈 요코하마 2경기"'),
        ('"延長 延长赛 · 逆転 逆转 · 同点 平分 · 優勝率 夺冠率。"',
         '"延長 연장전 · 逆転 역전 · 同点 동점 · 優勝率 우승 확률."'),
        ('"総括 总结 · 締め切り 截稿 · 確認する 核实。"',
         '"総括 정리 · 締め切り 마감 · 確認する 확인하다."'),
        ('"日本シリーズの日程 · 大赛日程"', '"日本シリーズの日程 · 시리즈 일정"'),
        ('"横浜の2試合の記録 · 横滨两场比赛的记录"',
         '"横浜の2試合の記録 · 요코하마 2경기 기록"'),
        ('"練習 · 第 4 版练习"', '"練習 · 4면 연습"'),
    ],
    "content56.py": [
        ('"若者・エンタメ · 青年"', '"若者・エンタメ · 청년"'),
        ('"レベル B1 · ハロウィンと秋まつり · 万圣节与秋日祭典"',
         '"レベル B1 · ハロウィンと秋まつり · 할로윈과 가을 축제"'),
        ('"罰金 罚款 · 像 雕像 · 仮装 变装 · 守る 遵守。"',
         '"罰金 벌금 · 像 동상 · 仮装 분장 · 守る 지키다."'),
        ('"祭り 节日 · 週末 周末 · 話題 话题。"',
         '"祭り 축제 · 週末 주말 · 話題 화제."'),
        ('"你呢？秋日祭典上想做什么？写两句日语寄来。"',
         '"여러분은요? 이번 가을 축제에서 무엇을 하고 싶어요? 일본어로 두 문장 써서 보내 주세요."'),
        ('"練習 · 第 5 版练习"', '"練習 · 5면 연습"'),
        ('"レベル B2 · 暖かい11月と秋の旅 · 暖和的11月与秋日旅行"',
         '"レベル B2 · 暖かい11月と秋の旅 · 따뜻한 11월과 가을 여행"'),
        ('"予算 预算 · 満足 满足 · 観測 观测 · 追いかける 追赶。"',
         '"予算 예산 · 満足 만족 · 観測 관측 · 追いかける 쫓다."'),
        ('"グラフを読もう · 读图表"', '"グラフを読もう · 그래프 읽기"'),
        ('"練習用データ · 练习数据"', '"練習用データ · 연습용 데이터"'),
        ('"練習 · 第 6 版练习"', '"練習 · 6면 연습"'),
    ],
    "content7.py": [
        ('"ことば · 语言"', '"ことば · 말 공부"'),
        ('"言語フォーカス · 三つのレベル、三つのテーマ · 三个级别，三个主题"',
         '"言語フォーカス · 三つのレベル、三つのテーマ · 세 가지 레벨, 세 가지 주제"'),
        ('"読書週間 读书周 · 紹介 介绍 · 読み聞かせ 朗读。"',
         '"読書週間 독서 주간 · 紹介 소개 · 読み聞かせ 읽어 주기."'),
        ('"見頃 最佳观赏期 · 紅葉狩り 看红叶出游 · 落葉 落叶"',
         '"見頃 가장 보기 좋은 때 · 紅葉狩り 단풍 구경 · 落葉 낙엽"'),
        ('"〜倍 倍 · 〜% 百分之〜 · 〜万食 万份。"',
         '"〜倍 배 · 〜% 퍼센트 · 〜万食 만 끼."'),
        ('"まちがい診療所 · 易错诊所"', '"まちがい診療所 · 실수 병원"'),
        ('"有「昨日」时要用过去式。"', '"「昨日」가 있으면 과거형을 써요."'),
        ('"动词名词化时要加「こと」。"', '"동사를 명사처럼 쓸 때는 「こと」가 필요해요."'),
        ('"地点用「か所」来数。"', '"장소는 「か所」로 세요."'),
        ('"动作发生的场所用「で」。"', '"동작이 일어나는 장소는 「で」를 써요."'),
        ('"今週のフレーム · 本周句式"', '"今週のフレーム · 이번 주의 틀"'),
        ('"句式拆解：轻松地调理身心。"', '"틀 풀이: 몸과 마음을 가볍게 다스리기."'),
        ('"読者の手紙 · 读者园地"', '"読者の手紙 · 독자의 편지"'),
        # Readers' corner: the Japanese disclosure line (ld) must NOT
        # serve as the operative disclosure for Korean readers, and the
        # core's Chinese disclosure (lcn) is the core's reader-native
        # layer. Both are replaced by ONE Korean disclosure stating all
        # 3 facts (editor's sample, not a real letter; no real letters
        # and no best Page-8 compositions had arrived by the deadline;
        # both carried to VOL.3) plus an explicit imperative invitation
        # with a VOL.3 printing promise. The VOL.3 teaser line is a
        # preview, not the invitation, and is not counted as one.
        ('ld = "※この手紙は編集部の例です。締め切りまでに、本当の読者の手紙と第8版の作文の優秀作は届きませんでした。VOL.3に載せます。"',
         'ld_ko = "편집부의 예시 편지예요, 실제 편지가 아니에요. 마감까지 실제 편지도 '
         '8면의 우수 작품도 도착하지 않았어요. 둘 다 VOL.3에 실을게요. 여러분의 편지를 '
         '일본어로 보내 주세요 — 뽑힌 편지는 VOL.3에 실어요!"'),
        ('lcn = "编辑部示例信，非真实来信。截至截稿，未收到真实来信与第8版最佳作文；VOL.3将刊登收到的来信与佳作。"\n',
         ''),
        ('lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld, "serif", False, 20.5, CW - 44)) * 29 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26 + 16',
         'lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld_ko, "sans", False, 20, CW - 44)) * 29 + 26 + 16'),
        ('yy3 = p.para(bx + 22, yy3 + 20, ld, 20.5, "serif", False, GREY, CW - 44, 1.42) + 10\n'
         'p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)',
         'p.para(bx + 22, yy3 + 20, ld_ko, 20, "sans", False, GREY, CW - 44, 1.42)'),
        ('"今週のフレーズ · 本周金句（逐字摘自本期文章）"',
         '"今週のフレーズ · 이번 주의 문장(이번호 기사에서 그대로)"'),
        ('"文化日是11月3日星期二。"', '"문화의 날은 11월 3일 화요일이에요."'),
        ('"这是一个慢慢地、轻松调理的日本11月。"',
         '"천천히, 가볍게 다스리는 일본의 11월이에요."'),
        ('"所谓ゆる，就是不勉强、慢慢来的意思。"',
         '"「ゆる」는 무리하지 않고 천천히 한다는 뜻이에요."'),
        ('"火锅食材提前一个月上架了。"',
         '"나베 재료가 한 달 일찍 진열되기 시작했어요."'),
        ('"可以同时欣赏传统工艺、红叶与灯光。"',
         '"전통 공예와 단풍과 빛을 함께 즐길 수 있어요."'),
        ('"软银以两连胜开局。"', '"소프트뱅크가 2연승으로 시작했어요."'),
        ('"遵守规则，过一个快乐的万圣节吧。"',
         '"규칙을 지켜서 즐거운 할로윈을 보내요."'),
        ('"去看红叶的人可以自北向南追赶最佳观赏期。"',
         '"단풍을 보러 가는 사람은 북쪽에서 남쪽으로 절정을 쫓아갈 수 있어요."'),
        ('"第1面"', '"p.1"'),
        ('"第2面"', '"p.2"'),
        ('"第3面"', '"p.3"'),
        ('"第4面"', '"p.4"'),
        ('"第5面"', '"p.5"'),
        ('"第6面"', '"p.6"'),
        ('"来週 · 下期预告 (VOL.3)"', '"来週 · 다음 주 예고 (VOL.3)"'),
    ],
    "content8.py": [
        ('"テストと答え · 练习与答案"', '"テストと答え · 시험과 정답"'),
        ('"第 8 面 · 週の大きなテスト + 全ての答え"',
         '"제 8 면 · 週の大きなテスト + 全ての答え"'),
        # E zone re-aim JA<->ZH -> JA<->KO (W43 JA x KO pattern):
        # #137/#138 keys become Korean; #139/#140 bodies become Korean
        # prompts with Japanese keys byte-identical to the core.
        ('"文化日是11月3日。"', '"문화의 날은 11월 3일이에요."'),
        ('"乱扔垃圾，要罚2,000日元。"', '"쓰레기를 버리면 벌금 2,000엔이에요."'),
        ('"读书周从10月27日开始。→ ___"', '"독서 주간은 10월 27일부터 시작해요.→ ___"'),
        ('"我想去神户看红叶灯光秀。→ ___"',
         '"고베의 단풍 라이트업을 보러 가고 싶어요.→ ___"'),
        ('f"写作题（无唯一答案）；范文（{NCHARS} 字）见下。"',
         'f"쓰기 문제예요(정답은 하나가 아니에요). 모범 답안({NCHARS}자)은 아래에 있어요."'),
        ('"（开放题，范文如下）"', '"(열린 문제 — 모범 답안은 아래에)"'),
        ('f"范文见本版 H 区（{NCHARS} 字）"',
         'f"모범 답안은 이 면 H 구역에 있어요({NCHARS}자)"'),
        ('"答え · 参考答案 — 按版面分页排列，找到题号即可"',
         '"答え · 정답 — 면별로 나누어 실었어요. 번호를 찾으세요"'),
        ('"每题附一句中文简析 · 带 ✓ 的为范文题"',
         '"답마다 한국어 한 줄 해설 · ✓ 표시는 모범 답안 문제예요"'),
        ('f"— 第{pg}面 —"', 'f"— 제 {pg} 면 —"'),
    ],
    "render.py": [
        ('"Lucerna-VOL2.pdf"', '"Lucerna-VOL2-KO.pdf"'),
        ('"Lucerna-VOL2-web.pdf"', '"Lucerna-VOL2-KO-web.pdf"'),
    ],
}


def apply_pairs(text, pairs, fname):
    seen = set()
    for old, new in pairs:
        if old in seen:
            continue
        seen.add(old)
        n = text.count(old)
        assert n >= 1, f"{fname}: replacement source missing: {old!r}"
        text = text.replace(old, new)
    return text


def apply_soft(text, pairs):
    seen = set()
    for old, new in pairs:
        if old in seen:
            continue
        seen.add(old)
        text = text.replace(old, new)
    return text


def apply_notes_scoped(text, note_map):
    """Replace note strings ONLY where they are note arguments.

    Bare substring replacement is FORBIDDEN for notes: several notes are
    prefixes/substrings of frozen Japanese stems and article sentences,
    and a global replace would corrupt frozen text. Two scoped sites:
    (a) the 4th quoted argument of any .ex(...) call;
    (b) a bracket-list line whose every string is a note (match_set notes
    lists; lefts/rights/keys lines never satisfy this).
    """
    def ex_sub(m):
        note = m.group(2)
        if note in note_map:
            return m.group(1) + note_map[note] + m.group(3)
        return m.group(0)
    text = re.sub(r'(\.ex\(\"[^\"]*\",\s*\"[^\"]*\",\s*\"[^\"]*\",\s*\")([^\"]*)(\")',
                  ex_sub, text)

    def list_sub(m):
        inner = m.group(2)
        strs = re.findall(r'\"([^\"]*)\"', inner)
        if strs and all(s in note_map for s in strs):
            out = inner
            for s in strs:
                out = out.replace('"%s"' % s, '"%s"' % note_map[s], 1)
            return m.group(1) + out + m.group(3)
        return m.group(0)
    text = re.sub(r'(?m)^(\s*\[)(.*)(\],\s*)$', list_sub, text)
    return text


def quoted_strings(text):
    return set(re.findall(r'\"([^\"]*)\"', text))


def main():
    os.makedirs(EDITION, exist_ok=True)
    os.makedirs(os.path.join(EDITION, "svg"), exist_ok=True)
    # svglib: canonical JA build, copied verbatim, md5-verified, never edited.
    src_svg = os.path.join(CORE, "svglib.py")
    data = open(src_svg, "rb").read()
    assert hashlib.md5(data).hexdigest() == CANON_SVGLIB_MD5, "svglib md5 mismatch"
    shutil.copyfile(src_svg, os.path.join(HERE, "svglib.py"))
    # run.py: verbatim copy (one-process driver).
    shutil.copyfile(os.path.join(CORE, "run.py"), os.path.join(HERE, "run.py"))
    # assets: verbatim copies (images + credits).
    os.makedirs(os.path.join(HERE, "assets"), exist_ok=True)
    for f in os.listdir(os.path.join(CORE, "assets")):
        shutil.copyfile(os.path.join(CORE, "assets", f),
                        os.path.join(HERE, "assets", f))
    # NOTE replacements: dict (deduped). Order: NOTES scoped FIRST (note
    # arguments only), then structural PER_FILE, then GLOBAL types/instr.
    note_map = dict(NOTES)
    fnames = ["bslib4.py", "content12.py", "content34.py", "content56.py",
              "content7.py", "content8.py", "render.py"]
    # Pre-audit: every GLOBAL source must occur in >=1 core file, and
    # every NOTE key must occur as an EXACT quoted string (a real note
    # argument, not a substring of a frozen sentence).
    core_texts = {f: open(os.path.join(CORE, f), encoding="utf-8").read()
                  for f in fnames}
    for old, _ in GLOBAL:
        assert any(old in t for t in core_texts.values()), \
            f"transform table source never occurs in core: {old!r}"
    core_quoted = set()
    for t in core_texts.values():
        core_quoted |= quoted_strings(t)
    for old in note_map:
        assert old in core_quoted, \
            f"note key never occurs as an exact quoted string: {old!r}"
    for fname in fnames:
        text = core_texts[fname]
        text = apply_notes_scoped(text, note_map)
        text = apply_pairs(text, PER_FILE.get(fname, []), fname)
        text = apply_soft(text, GLOBAL)
        open(os.path.join(HERE, fname), "w", encoding="utf-8").write(text)
        print("transformed", fname)
    # Post-audit: no GLOBAL source may survive as a substring, and no
    # NOTE key may survive as an exact quoted string (substrings inside
    # frozen stems legitimately remain).
    for fname in fnames:
        out = open(os.path.join(HERE, fname), encoding="utf-8").read()
        for old, _ in GLOBAL:
            assert old not in out, f"{fname}: un-replaced source remains: {old!r}"
        out_quoted = quoted_strings(out)
        for old in note_map:
            assert old not in out_quoted, \
                f"{fname}: un-replaced note remains: {old!r}"
    print("OUT dir:", EDITION)


if __name__ == "__main__":
    main()
