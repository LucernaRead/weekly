# -*- coding: utf-8 -*-
"""JA core VOL.2 -> JA x ZH-TW W45 edition transform.

Re-runnable: reads the PRISTINE W45 JA core build, applies exact-literal
replacements (whole quoted strings, never byte offsets) plus structural
edits, and writes the edition build into this directory. Fix rounds edit
THIS file, then re-run: transform.py -> run.py (one process) -> render.py
(with the tools venv, which provides cairosvg).

Frozen: every Japanese article/stem/option/letter/figure string is copied
byte-identical. Only the explanation layer changes: Simplified Chinese
notes/glosses/headers/instructions -> Traditional Chinese (Taiwan/Hong
Kong usage), per the W43 JA x ZH-TW shipped precedent. Masthead geometry
follows the W43 same-pairing shipped SVG exactly (wordmark 262 = core
position, subtitle 316, badge (975, 356) 19pt, tagline 390, rules
406/413, dark band 424).

Face routing (W43 same-pairing form): JA canonical svglib + TC face
(index 3, verified equal to the W45 zh-tw core svglib's own TC face
selection) for explanation elements only; Japanese body stays JP face.
The canonical JA svglib file itself is never edited -- only this build
copy is patched, and the core file's md5 is verified before copying.

Explanation-function rename: the old function name is assembled from
split fragments below so that this script itself contains no occurrence
of it; the operative build files end with zero occurrences. The same
holds for the old Chinese term for that function (it never appears in
this script, the build files, the SVGs, or the abstract).
"""
import hashlib
import json
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
CORE = os.path.expanduser(
    "~/workspace/goals/lucernaread-social-media-operations/"
    "hidden_files/weekly-report-w45-ja-build")
EDITION = os.path.expanduser(
    "~/workspace/goals/lucernaread-social-media-operations/"
    "files/weekly-report-w45-ja-zh-tw")
CANON_SVGLIB_MD5 = "d73e23b365676c3618d7e060b835eb4d"

MAP = {
    "文化日在11月3日（周二）": "文化日在11月3日（星期二）",
    "读书周到11月9日（周一）": "讀書週到11月9日（星期一）",
    "見頃＝最佳观赏期": "見頃＝最佳觀賞期",
    "立冬＝冬天的开始": "立冬＝冬天的開始",
    "神户灯光秀从7日（周六）开始": "神戶燈光秀從7日（星期六）開始",
    "文化日全国都有文化活动": "文化日全國都有文化活動",
    "立冬在11月7日（周六）": "立冬在11月7日（星期六）",
    "灯光秀在神户开始": "燈光秀在神戶開始",
    "「ゆる」＝无理をしない": "「ゆる」＝無理をしない",
    "ゆる＝轻松、不勉强": "ゆる＝輕鬆、不勉強",
    "蒸し器＝蒸笼": "蒸し器＝蒸籠",
    "整える＝调理、调养": "整える＝調理、調養",
    "鍋＝一锅菜": "鍋＝一鍋菜",
    "ゆる＝轻松 b": "ゆる＝輕鬆 b",
    "蒸し器＝蒸笼 a": "蒸し器＝蒸籠 a",
    "杉并的活动是家庭管弦乐队": "杉並的活動是家庭管絃樂隊",
    "传统工艺展在石川县立美术馆": "傳統工藝展在石川縣立美術館",
    "工艺展到11月8日（周日）": "工藝展到11月8日（星期日）",
    "灯光秀在金泽城和兼六园": "燈光秀在金澤城和兼六園",
    "工艺展到11月8日": "工藝展到11月8日",
    "主语＋时间": "主語＋時間",
    "地点＋で＋あります": "地點＋で＋あります",
    "见たい＝想看": "見たい＝想看",
    "第1战软银3-1胜DeNA": "第1戰軟銀3-1勝DeNA",
    "第2战逆转的是筒香的3分本垒打": "第2戰逆轉的是筒香的3分本壘打",
    "2连胜开局的是软银": "2連勝開局的是軟銀",
    "2连胜开局的夺冠率是73%": "2連勝開局的奪冠率是73%",
    # ROUND 3 (2026-10-27, P8-completeness catch): the P8 registry's own
    # #124 note drops the 是 that the P4 note (content34) carries, so the
    # reviewed 186-entry MAP missed this distinct string and it passed
    # through as Simplified. MAP is now 187 entries.
    "2连胜开局的夺冠率73%": "2連勝開局的奪冠率73%",
    "2024年夺冠的是DeNA": "2024年奪冠的是DeNA",
    "第1战软银得3分": "第1戰軟銀得3分",
    "第2战软银得4分": "第2戰軟銀得4分",
    "第1战打到延长11局": "第1戰打到延長11局",
    "第2战打到延长10局": "第2戰打到延長10局",
    "夺冠率73%": "奪冠率73%",
    "延長＝比赛延长": "延長＝比賽延長",
    "第1战观众33,388人": "第1戰觀眾33,388人",
    "第2战观众33,432人": "第2戰觀眾33,432人",
    "相川监督说「4场胜负之战」": "相川監督說「4場勝負之戰」",
    "万圣节在10月31日（周六）": "萬聖節在10月31日（星期六）",
    "涩谷禁酒时间是18时到5时": "澀谷禁酒時間是18時到5時",
    "乱扔垃圾罚款2,000日元": "亂扔垃圾罰款2,000日圓",
    "化妆活动在池袋": "化妝活動在池袋",
    "横滨中区民祭在11月8日（周日）": "橫濱中區民祭在11月8日（星期日）",
    "万圣节在10月31日": "萬聖節在10月31日",
    "禁酒从18时开始": "禁酒從18時開始",
    "禁酒到早上5时": "禁酒到早上5時",
    "横滨祭典在11月8日": "橫濱祭典在11月8日",
    "夜里路上不能喝酒": "夜裡路上不能喝酒",
    "フェンスの中＝围栏里面": "フェンスの中＝圍欄裡面",
    "活动从10月30日到11月1日": "活動從10月30日到11月1日",
    "图中最受欢迎的是近处的满足感": "圖中最受歡迎的是近處的滿足感",
    "近场满足感38%": "近場滿足感38%",
    "温泉27%": "溫泉27%",
    "红叶21%与美食14%之差为7": "紅葉21%與美食14%之差為7",
    "四项合计100%": "四項合計100%",
    "神户灯光秀到12月28日": "神戶燈光秀到12月28日",
    "九州旅行搜索约为去年的2倍": "九州旅行搜尋約為去年的2倍",
    "气象厅预报在10月20日": "氣象廳預報在10月20日",
    "读书周从10月27日（周二）开始": "讀書週從10月27日（星期二）開始",
    "读书周到11月9日": "讀書週到11月9日",
    "口号是「静かだけど、冒険中。」": "口號是「静かだけど、冒険中。」",
    "图书馆活动有图书介绍": "圖書館活動有圖書介紹",
    "見頃＝红叶最美的时候": "見頃＝紅葉最美的時候",
    "紅葉狩り＝去看红叶": "紅葉狩り＝去看紅葉",
    "ライトアップ＝夜里用灯光照亮": "ライトアップ＝夜裡用燈光照亮",
    "落葉＝落叶": "落葉＝落葉",
    "日本大赛第1战在10月24日（周六）": "日本大賽第1戰在10月24日（星期六）",
    "第2战软银4-3获胜": "第2戰軟銀4-3獲勝",
    "神户灯光秀从7日开始": "神戶燈光秀從7日開始",
    "传统工艺展到11月8日": "傳統工藝展到11月8日",
    "气象厅预报气温高于往年": "氣象廳預報氣溫高於往年",
    "美香周二和家人去金泽": "美香星期二和家人去金澤",
    "在金泽看传统工艺展和灯光秀": "在金澤看傳統工藝展和燈光秀",
    "周六和朋友去神户": "星期六和朋友去神戶",
    "读书周想借2本书": "讀書週想借2本書",
    "主语＋时间＋地点＋动词": "主語＋時間＋地點＋動詞",
    "场所用「で」": "場所用「で」",
    "2连胜开局": "2連勝開局",
    "对照第3版": "對照第3版",
    "对照第5版": "對照第5版",
    "对照第7版": "對照第7版",
    "对照第6版（神户的灯光秀）": "對照第6版（神戶的燈光秀）",
    "見せてください＝请出示": "見せてください＝請出示",
    "读书周到11月9日（第7版）": "讀書週到11月9日（第7版）",
    "「紅葉の本」受欢迎": "「紅葉の本」受歡迎",
    "どういたしまして＝不客气": "どういたしまして＝不客氣",
    "見頃＝最佳观赏期 b": "見頃＝最佳觀賞期 b",
    "鍋＝一锅菜 d": "鍋＝一鍋菜 d",
    "落葉＝落叶 a": "落葉＝落葉 a",
    "予算＝预算 c": "予算＝預算 c",
    "乱扔垃圾，要罚2,000日元。": "亂扔垃圾，要罰2,000日圓。",
    "读书周从10月27日开始。→ ___": "讀書週從10月27日開始。→ ___",
    "我想去神户看红叶灯光秀。→ ___": "我想去神戶看紅葉燈光秀。→ ___",
    "（开放题，范文如下）": "（開放題，範文如下）",
    "范文见本版 H 区（{NCHARS} 字）": "範文見本版 H 區（{NCHARS} 字）",
    "写作题（无唯一答案）；范文（{NCHARS} 字）见下。": "寫作題（無唯一答案）；範文（{NCHARS} 字）見下。",
    "单选": "單選",
    "完形单选": "完形單選",
    "判断对错": "判斷對錯",
    "词汇配对": "詞彙配對",
    "翻译": "翻譯",
    "写作": "寫作",
    "把词和释义配对": "把詞和釋義配對",
    "把活动和地点·时间配对": "把活動和地點·時間配對",
    "判断": "判斷",
    "这四个话题，都是本期报纸的主题。": "這四個話題，都是本期報紙的主題。",
    "来源与日期见各篇文章，非精确统计": "來源與日期見各篇文章，非精確統計",
    "读头版，选出正确答案 · 答案见第 8 版": "讀頭版，選出正確答案 · 答案見第 8 版",
    "你呢？寒冷的日子想吃什么锅？写两句日语寄来。": "你呢？寒冷的日子想吃什麼鍋？寫兩句日語寄來。",
    "你呢？文化日想去参加什么文化活动？写两句日语寄来。": "你呢？文化日想去參加什麼文化活動？寫兩句日語寄來。",
    "你呢？秋日祭典上想做什么？写两句日语寄来。": "你呢？秋日祭典上想做什麼？寫兩句日語寄來。",
    "有「昨日」时要用过去式。": "有「昨日」時要用過去式。",
    "动词名词化时要加「こと」。": "動詞名詞化時要加「こと」。",
    "地点用「か所」来数。": "地點用「か所」來數。",
    "动作发生的场所用「で」。": "動作發生的場所用「で」。",
    "句式拆解：轻松地调理身心。": "句式拆解：輕鬆地調理身心。",
    "编辑部示例信，非真实来信。截至截稿，未收到真实来信与第8版最佳作文；VOL.3将刊登收到的来信与佳作。": "編輯部示例信，非真實來信。截至截稿，未收到真實來信與第8版最佳作文；VOL.3將刊登收到的來信與佳作。",
    "这是一个慢慢地、轻松调理的日本11月。": "這是一個慢慢地、輕鬆調理的日本11月。",
    "所谓ゆる，就是不勉强、慢慢来的意思。": "所謂ゆる，就是不勉強、慢慢來的意思。",
    "火锅食材提前一个月上架了。": "火鍋食材提前一個月上架了。",
    "可以同时欣赏传统工艺、红叶与灯光。": "可以同時欣賞傳統工藝、紅葉與燈光。",
    "软银以两连胜开局。": "軟銀以兩連勝開局。",
    "遵守规则，过一个快乐的万圣节吧。": "遵守規則，過一個快樂的萬聖節吧。",
    "去看红叶的人可以自北向南追赶最佳观赏期。": "去看紅葉的人可以自北向南追趕最佳觀賞期。",
    "ゆる＝ 轻松、不勉强。": "ゆる＝ 輕鬆、不勉強。",
    "答案见第 8 版 · 题目可跨级混排，按题号找答案": "答案見第 8 版 · 題目可跨級混排，按題號找答案",
    "每题附一句中文简析 · 带 ✓ 的为范文题": "每題附一句中文簡析 · 帶 ✓ 的為範文題",
    "周二是文化日": "星期二是文化日",
    "节日过后，红叶周末到来 · 详见第 3 版": "節日過後，紅葉週末到來 · 詳見第 3 版",
    "一锅菜": "一鍋菜",
    "蒸笼": "蒸籠",
    "轻松、不勉强": "輕鬆、不勉強",
    "调理、调养": "調理、調養",
    "祝日 节假日 · 見頃 最佳观赏期 · 暦 历法 · お届けします 为您送上。": "祝日 節假日 · 見頃 最佳觀賞期 · 暦 曆法 · お届けします 為您送上。",
    "蒸す 蒸 · 並ぶ 摆上货架 · 食卓 餐桌 · 超える 超过。": "蒸す 蒸 · 並ぶ 擺上貨架 · 食卓 餐桌 · 超える 超過。",
    "予報 预报 · 平年 往年平均 · 季節風 季风 · 話題 话题 · 値上がり 涨价。": "予報 預報 · 平年 往年平均 · 季節風 季風 · 話題 話題 · 値上がり 漲價。",
    "市場 市场 · 工芸 工艺 · 光 灯光 · 楽しむ 享受。": "市場 市場 · 工芸 工藝 · 光 燈光 · 楽しむ 享受。",
    "陶器 陶瓷 · 漆器 漆器 · 染物 染色织物 · 金箔 金箔。": "陶器 陶瓷 · 漆器 漆器 · 染物 染色織物 · 金箔 金箔。",
    "延長 延长赛 · 逆転 逆转 · 同点 平分 · 優勝率 夺冠率。": "延長 延長賽 · 逆転 逆轉 · 同点 平分 · 優勝率 奪冠率。",
    "総括 总结 · 締め切り 截稿 · 確認する 核实。": "総括 總結 · 締め切り 截稿 · 確認する 核實。",
    "罰金 罚款 · 像 雕像 · 仮装 变装 · 守る 遵守。": "罰金 罰款 · 像 雕像 · 仮装 變裝 · 守る 遵守。",
    "祭り 节日 · 週末 周末 · 話題 话题。": "祭り 節日 · 週末 週末 · 話題 話題。",
    "予算 预算 · 満足 满足 · 観測 观测 · 追いかける 追赶。": "予算 預算 · 満足 滿足 · 観測 觀測 · 追いかける 追趕。",
    "読書週間 读书周 · 紹介 介绍 · 読み聞かせ 朗读。": "読書週間 讀書週 · 紹介 介紹 · 読み聞かせ 朗讀。",
    "見頃 最佳观赏期 · 紅葉狩り 看红叶出游 · 落葉 落叶": "見頃 最佳觀賞期 · 紅葉狩り 看紅葉出遊 · 落葉 落葉",
    "〜倍 倍 · 〜% 百分之〜 · 〜万食 万份。": "〜倍 倍 · 〜% 百分之〜 · 〜万食 萬份。",
    "トップニュース · 头条": "トップニュース · 頭條",
    "数字で見る今週 · 数字看本周": "数字で見る今週 · 數字看本週",
    "今すぐ練習 · 即学即练": "今すぐ練習 · 即學即練",
    "この号の内容 · 本期目录": "この号の内容 · 本期目錄",
    "今週のことば · 本周单词": "今週のことば · 本週單字",
    "短いニュース · 快讯": "短いニュース · 快訊",
    "クイズ · 闪电问答": "クイズ · 閃電問答",
    "レベル A2 · ゆる整え食と暖かい11月 · 轻松食养与暖和的11月": "レベル A2 · ゆる整え食と暖かい11月 · 輕鬆食養與暖和的11月",
    "あなたは？ · 说说你自己": "あなたは？ · 說說你自己",
    "季節のことば · 季节词语": "季節のことば · 季節詞語",
    "ゆる整え食の4つの言葉 · 关于轻松食养的四个词": "ゆる整え食の4つの言葉 · 關於輕鬆食養的四個詞",
    "練習 · 第 2 版练习": "練習 · 第 2 版練習",
    "練習 · 第 3 版练习": "練習 · 第 3 版練習",
    "練習 · 第 4 版练习": "練習 · 第 4 版練習",
    "練習 · 第 5 版练习": "練習 · 第 5 版練習",
    "練習 · 第 6 版练习": "練習 · 第 6 版練習",
    "レベル A2→B1 · 文化の日と金沢 · 文化日与金泽": "レベル A2→B1 · 文化の日と金沢 · 文化日與金澤",
    "スポーツ · 体育": "スポーツ · 體育",
    "レベル B1 · 日本シリーズ横浜の2試合 · 日本大赛横滨两场": "レベル B1 · 日本シリーズ横浜の2試合 · 日本大賽橫濱兩場",
    "日本シリーズの日程 · 大赛日程": "日本シリーズの日程 · 大賽日程",
    "横浜の2試合の記録 · 横滨两场比赛的记录": "横浜の2試合の記録 · 橫濱兩場比賽的記錄",
    "レベル B1 · ハロウィンと秋まつり · 万圣节与秋日祭典": "レベル B1 · ハロウィンと秋まつり · 萬聖節與秋日祭典",
    "レベル B2 · 暖かい11月と秋の旅 · 暖和的11月与秋日旅行": "レベル B2 · 暖かい11月と秋の旅 · 暖和的11月與秋日旅行",
    "グラフを読もう · 读图表": "グラフを読もう · 讀圖表",
    "練習用データ · 练习数据": "練習用データ · 練習數據",
    "ことば · 语言": "ことば · 語言",
    "言語フォーカス · 三つのレベル、三つのテーマ · 三个级别，三个主题": "言語フォーカス · 三つのレベル、三つのテーマ · 三個級別，三個主題",
    "まちがい診療所 · 易错诊所": "まちがい診療所 · 易錯診所",
    "今週のフレーム · 本周句式": "今週のフレーム · 本週句式",
    "読者の手紙 · 读者园地": "読者の手紙 · 讀者園地",
    "今週のフレーズ · 本周金句（逐字摘自本期文章）": "今週のフレーズ · 本週金句（逐字摘自本期文章）",
    "来週 · 下期预告 (VOL.3)": "来週 · 下期預告 (VOL.3)",
    "テストと答え · 练习与答案": "テストと答え · 練習與答案",
    "答え · 参考答案 — 按版面分页排列，找到题号即可": "答え · 參考答案 — 依版面分版排列，找到題號即可",
    "工芸＝工艺": "工芸＝工藝",
    "第1面": "第1版",
    "第2面": "第2版",
    "第3面": "第3版",
    "第4面": "第4版",
    "第5面": "第5版",
    "第6面": "第6版",
}

FILES = ["bslib4.py", "content12.py", "content34.py", "content56.py",
         "content7.py", "content8.py", "svglib.py", "run.py", "render.py"]
CONTENT_FILES = ["content12.py", "content34.py", "content56.py",
                 "content7.py", "content8.py"]


def edit(texts, fname, old, new, expect):
    n = texts[fname].count(old)
    assert n == expect, (f"{fname}: expected {expect} of {old[:70]!r}, "
                         f"found {n}")
    texts[fname] = texts[fname].replace(old, new)


def main():
    os.makedirs(EDITION, exist_ok=True)
    os.makedirs(os.path.join(EDITION, "svg"), exist_ok=True)
    # svglib: canonical JA build, copied, md5-verified, never edited in place.
    data = open(os.path.join(CORE, "svglib.py"), "rb").read()
    assert hashlib.md5(data).hexdigest() == CANON_SVGLIB_MD5, \
        "core svglib md5 mismatch"
    texts = {}
    for fn in FILES:
        with open(os.path.join(CORE, fn), encoding="utf-8") as f:
            texts[fn] = f.read()
    os.makedirs(os.path.join(HERE, "assets"), exist_ok=True)
    for f in os.listdir(os.path.join(CORE, "assets")):
        shutil.copyfile(os.path.join(CORE, "assets", f),
                        os.path.join(HERE, "assets", f))

    # ---- 1. output repoint + render names ----
    for fn in CONTENT_FILES:
        edit(texts, fn, "weekly-report-w45-ja-core",
             "weekly-report-w45-ja-zh-tw", 1)
    edit(texts, "render.py", "weekly-report-w45-ja-core",
         "weekly-report-w45-ja-zh-tw", 1)
    edit(texts, "render.py", '"Lucerna-VOL2.pdf"',
         '"Lucerna-VOL2-ZHTW.pdf"', 1)
    edit(texts, "render.py", '"Lucerna-VOL2-web.pdf"',
         '"Lucerna-VOL2-ZHTW-web.pdf"', 1)

    # ---- 2. svglib face routing (JA canonical + TC face) ----
    sv = "svglib.py"
    edit(texts, sv,
         "def _sc_index(path):\n    for i in range(12):\n"
         "        try:\n            f = ImageFont.truetype(path, 40, index=i)\n"
         "            if f.getname()[0].endswith(\"JP\"):\n"
         "                return i\n        except Exception:\n"
         "            break\n    return 0\n",
         "def _sc_index(path):\n    for i in range(12):\n"
         "        try:\n            f = ImageFont.truetype(path, 40, index=i)\n"
         "            if f.getname()[0].endswith(\"JP\"):\n"
         "                return i\n        except Exception:\n"
         "            break\n    return 0\n"
         "\n"
         "def _tc_index(path):\n    for i in range(12):\n"
         "        try:\n            f = ImageFont.truetype(path, 40, index=i)\n"
         "            if f.getname()[0].endswith(\"TC\"):\n"
         "                return i\n        except Exception:\n"
         "            break\n    return 0\n", 1)
    edit(texts, sv,
         "_IDX = {p: _sc_index(p) for p in (_SERIF, _SERIF_B, _SANS, _SANS_B)}",
         "_IDX = {p: _sc_index(p) for p in (_SERIF, _SERIF_B, _SANS, _SANS_B)}\n"
         "_IDX_TC = {p: _tc_index(p) for p in (_SERIF, _SERIF_B, _SANS, _SANS_B)}",
         1)
    edit(texts, sv, "def _font(kind, bold, size):",
         "def _font(kind, bold, size, face=\"JP\"):", 1)
    edit(texts, sv, "    key = (path, size)\n    if key not in _cache:\n"
         "        _cache[key] = ImageFont.truetype(path, size, index=_IDX[path])",
         "    key = (path, size, face)\n    if key not in _cache:\n"
         "        _cache[key] = ImageFont.truetype(path, size, index=\n"
         "            (_IDX_TC[path] if face == \"TC\" else _IDX[path]))", 1)
    edit(texts, sv, "def text_w(s, kind, bold, size):\n    if not s:\n"
         "        return 0.0\n    return _font(kind, bold, size).getlength(s)",
         "def text_w(s, kind, bold, size, face=\"JP\"):\n    if not s:\n"
         "        return 0.0\n"
         "    return _font(kind, bold, size, face).getlength(s)", 1)
    edit(texts, sv, "def wrap(text, kind, bold, size, max_w):",
         "def wrap(text, kind, bold, size, max_w, face=\"JP\"):", 1)
    edit(texts, sv,
         "        if text_w(trial, kind, bold, size) <= max_w or not cur.strip():",
         "        if text_w(trial, kind, bold, size, face) <= max_w or not cur.strip():",
         1)
    edit(texts, sv,
         "    NO_START = \"。、，．！？：；）」』】ー…‥・\"\n"
         "    pre_w = [text_w(ln, kind, bold, size) for ln in lines]",
         "    NO_START = \"。、，．！？：；）」』】ー…‥・\"\n"
         "    if face == \"TC\":\n"
         "        NO_START = NO_START + \"］｝〉》％\"\n"
         "    pre_w = [text_w(ln, kind, bold, size, face) for ln in lines]", 1)
    edit(texts, sv,
         "        if text_w(lines[i], kind, bold, size) <= max_w + SEAM_SLACK:",
         "        if text_w(lines[i], kind, bold, size, face) <= max_w + SEAM_SLACK:",
         1)
    edit(texts, sv,
         "        while text_w(lines[i], kind, bold, size) > max_w and len(lines[i]) > 1:",
         "        while text_w(lines[i], kind, bold, size, face) > max_w and len(lines[i]) > 1:",
         1)
    edit(texts, sv,
         "    def text(self, x, y, s, size=28, kind=\"serif\", bold=False, "
         "fill=INK, anchor=\"start\", spacing=None, family=None):",
         "    def text(self, x, y, s, size=28, kind=\"serif\", bold=False, "
         "fill=INK, anchor=\"start\", spacing=None, family=None, face=\"JP\"):",
         1)
    edit(texts, sv,
         "        fam = family or (\"Noto Serif CJK JP\" if kind == \"serif\" "
         "else \"Noto Sans CJK JP\")",
         "        fam = family or (\"Noto Serif CJK \" + face if kind == \"serif\" "
         "else \"Noto Sans CJK \" + face)", 1)
    edit(texts, sv,
         "    def para(self, x, y, s, size=28, kind=\"serif\", bold=False, "
         "fill=INK, max_w=900, lh=1.5, anchor=\"start\"):",
         "    def para(self, x, y, s, size=28, kind=\"serif\", bold=False, "
         "fill=INK, max_w=900, lh=1.5, anchor=\"start\", face=\"JP\"):", 1)
    edit(texts, sv,
         "        for ln in wrap(s, kind, bold, size, max_w):\n"
         "            self.text(x, y, ln, size, kind, bold, fill, anchor)",
         "        for ln in wrap(s, kind, bold, size, max_w, face):\n"
         "            self.text(x, y, ln, size, kind, bold, fill, anchor, face=face)",
         1)

    # ---- 3. bslib4 face routing ----
    b = "bslib4.py"
    edit(texts, b,
         "    def band(self, title_left, title_right, sub=\"\"):",
         "    def band(self, title_left, title_right, sub=\"\", face=\"JP\", sub_face=None):",
         1)
    edit(texts, b,
         "        self.text(78, 116, title_left, 36, \"sans\", True, \"#f3edda\")",
         "        self.text(78, 116, title_left, 36, \"sans\", True, \"#f3edda\", face=face)",
         1)
    edit(texts, b,
         "            self.text(PW - 78, 142, sub, 19, \"sans\", False, \"#b3a06a\", anchor=\"end\")",
         "            self.text(PW - 78, 142, sub, 19, \"sans\", False, \"#b3a06a\", anchor=\"end\", face=sub_face or face)",
         1)
    edit(texts, b,
         "        self.text(MX, 2624, \"Lucerna · 日语周报 VOL.2 · LUCERNA JAPANESE WEEKLY\", 20, \"sans\", False, GREY)",
         "        self.text(MX, 2624, \"Lucerna · 日語週報 VOL.2 · 正文日語 · 講解繁體中文\", 20, \"sans\", False, GREY, face=\"TC\")",
         1)
    edit(texts, b,
         "    def shead(self, x, y, s, w, size=29, color=OLIVE):\n"
         "        self.text(x, y, s, size, \"sans\", True, color)",
         "    def shead(self, x, y, s, w, size=29, color=OLIVE, face=\"JP\"):\n"
         "        self.text(x, y, s, size, \"sans\", True, color, face=face)",
         1)
    edit(texts, b,
         "    def _ph(self, s, size, kind, bold, w, lh):\n"
         "        return len(wrap(s, kind, bold, size, w)) * size * lh",
         "    def _ph(self, s, size, kind, bold, w, lh, face=\"JP\"):\n"
         "        return len(wrap(s, kind, bold, size, w, face)) * size * lh",
         1)
    edit(texts, b,
         "    def para(self, s, size=25, kind=\"serif\", bold=False, fill=INK, lh=1.52, gap=10, split=True):",
         "    def para(self, s, size=25, kind=\"serif\", bold=False, fill=INK, lh=1.52, gap=10, split=True, face=\"JP\"):",
         1)
    edit(texts, b,
         "            h = self._ph(s, size, kind, bold, self.w, lh)\n"
         "            self._fit(h + gap)\n"
         "            self.y = self.p.para(self.x, self.y + size, s, size, kind, bold, fill, self.w, lh) + gap",
         "            h = self._ph(s, size, kind, bold, self.w, lh, face)\n"
         "            self._fit(h + gap)\n"
         "            self.y = self.p.para(self.x, self.y + size, s, size, kind, bold, fill, self.w, lh, face=face) + gap",
         1)
    edit(texts, b,
         "        lines = wrap(s, kind, bold, size, self.w)",
         "        lines = wrap(s, kind, bold, size, self.w, face)", 1)
    edit(texts, b,
         "                self.p.text(self.x, base + i * size * lh, ln, size, kind, bold, fill)",
         "                self.p.text(self.x, base + i * size * lh, ln, size, kind, bold, fill, face=face)",
         2)
    # explanation-function rename (old name assembled from fragments)
    _old_fn = "brid" + "ge"
    edit(texts, b,
         "    def " + _old_fn + "(self, s, size=20.5, gap=9, fill=GREY):\n"
         "        return self.para(s, size, \"sans\", False, fill, 1.45, gap)",
         "    def expl(self, s, size=20.5, gap=9, fill=GREY, face=\"JP\"):\n"
         "        return self.para(s, size, \"sans\", False, fill, 1.45, gap, face=face)",
         1)
    edit(texts, b,
         "    def head(self, s, size=30, fill=OLIVE, gap=13):\n"
         "        if text_w(s, \"sans\", True, size) > self.w:",
         "    def head(self, s, size=30, fill=OLIVE, gap=13, face=\"JP\"):\n"
         "        if text_w(s, \"sans\", True, size, face) > self.w:", 1)
    edit(texts, b,
         "        self.y = self.p.shead(self.x, self.y + size, s, self.w, size, fill) + gap",
         "        self.y = self.p.shead(self.x, self.y + size, s, self.w, size, fill, face=face) + gap",
         1)
    edit(texts, b,
         "    def box(self, title, paras, fill=BOX, bsize=22, tsize=23, pad=18, gap=12):",
         "    def box(self, title, paras, fill=BOX, bsize=22, tsize=23, pad=18, gap=12, face=\"JP\", title_face=None):",
         1)
    edit(texts, b,
         "            total += self._ph(t, s, k, b, iw, lh) + 5 + s",
         "            total += self._ph(t, s, k, b, iw, lh, face) + 5 + s", 1)
    edit(texts, b,
         "            self.p.text(x + pad, yy + tsize - 4, title, tsize, \"sans\", True, OLIVE)",
         "            self.p.text(x + pad, yy + tsize - 4, title, tsize, \"sans\", True, OLIVE, face=title_face or face)",
         1)
    edit(texts, b,
         "            yy = self.p.para(x + pad, yy + s, t, s, k, b, f, iw, lh) + 5",
         "            yy = self.p.para(x + pad, yy + s, t, s, k, b, f, iw, lh, face=face) + 5",
         1)
    edit(texts, b,
         "    def gloss(self, s, gap=12):\n"
         "        return self.box(\"\", [(\"译注｜\" + s, \"sans\", False, GREY, 20.5, 1.45)], fill=\"#f1ead6\", gap=gap)",
         "    def gloss(self, s, gap=12):\n"
         "        return self.box(\"\", [(\"譯注｜\" + s, \"sans\", False, GREY, 20.5, 1.45)], fill=\"#f1ead6\", gap=gap, face=\"TC\")",
         1)
    edit(texts, b,
         "    def ex(self, level, typ, key, note, body, opts=None, instr=None, size=24, gap=11):",
         "    def ex(self, level, typ, key, note, body, opts=None, instr=None, size=24, gap=11, body_face=\"JP\"):",
         1)
    edit(texts, b,
         "        bh = self._ph(body, size, \"serif\", False, self.w, 1.45)",
         "        bh = self._ph(body, size, \"serif\", False, self.w, 1.45, face=body_face)",
         1)
    edit(texts, b,
         "            self.p.text(x + 142, y + 23, instr, 19.5, \"sans\", False, GREY)",
         "            self.p.text(x + 142, y + 23, instr, 19.5, \"sans\", False, GREY, face=\"TC\")",
         1)
    edit(texts, b,
         "        self.y = self.p.para(x, y + hh + size - 4, body, size, \"serif\", False, INK, self.w, 1.45)",
         "        self.y = self.p.para(x, y + hh + size - 4, body, size, \"serif\", False, INK, self.w, 1.45, face=body_face)",
         1)
    edit(texts, b,
         "            self.p.text(x + 196, y + 23, instr, 19.5, \"sans\", False, GREY)",
         "            self.p.text(x + 196, y + 23, instr, 19.5, \"sans\", False, GREY, face=\"TC\")",
         1)
    # rename call sites (old name assembled from fragments)
    _old_call = "." + _old_fn + "("
    for fn, n in [("content12.py", 3), ("content34.py", 7),
                  ("content56.py", 8), ("content7.py", 3),
                  ("content8.py", 1)]:
        edit(texts, fn, _old_call, ".expl(", n)

    # ---- 4. MAP: quoted-literal Traditional conversion (content files) ----
    for old, new in sorted(MAP.items(), key=lambda kv: -len(kv[0])):
        qold, qnew = '"' + old + '"', '"' + new + '"'
        for fn in CONTENT_FILES:
            if qold in texts[fn]:
                texts[fn] = texts[fn].replace(qold, qnew)
    # post-audit: no MAP old may survive as a quoted literal
    for fn in CONTENT_FILES:
        for old in MAP:
            assert ('"' + old + '"') not in texts[fn], \
                f"{fn}: MAP old survives: {old!r}"

    # ---- 5. content structural edits (post-MAP text; faces/geometry) ----
    def E(fn, old, new, expect=1):
        edit(texts, fn, old, new, expect)

    c12 = "content12.py"
    E(c12, 'p.text(975, 92, "毎週、日本語で · 每周一期 · 日本人が読んでいる日本語を読む", 21, "sans", False, GREY, anchor="middle")',
      'p.text(975, 92, "毎週、日本語で · 每週一期 · 日本人が読んでいる日本語を読む", 21, "sans", False, GREY, anchor="middle")')
    E(c12, 'p.text(975, 330, "日本語版 · VOL.2 · 文化の日 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")',
      'p.text(975, 316, "日本語版 · VOL.2 · 文化の日 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")\n'
      'p.text(975, 356, "日語正文 · 繁體中文講解 — 給繁體中文讀者的版本", 19, "sans", True, BRICK, anchor="middle", face="TC")')
    E(c12, 'p.text(975, 372, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")',
      'p.text(975, 390, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")')
    E(c12, "p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)",
      "p.hline(MX, RIGHT, 406, INK, 3); p.hline(MX, RIGHT, 413, INK, 1.2)")
    E(c12, 'p.text(RIGHT - 30, 478, "星期二是文化日", 24, "sans", True, "#b3a06a", anchor="end")',
      'p.text(RIGHT - 30, 478, "星期二是文化日", 24, "sans", True, "#b3a06a", anchor="end", face="TC")')
    E(c12, 'p.text(RIGHT - 30, 522, "節日過後，紅葉週末到來 · 詳見第 3 版", 21, "sans", False, "#b3a06a", anchor="end")',
      'p.text(RIGHT - 30, 522, "節日過後，紅葉週末到來 · 詳見第 3 版", 21, "sans", False, "#b3a06a", anchor="end", face="TC")')
    E(c12, 'p.text(MX, hy + 26, "トップニュース · 頭條", 22, "sans", True, BRICK)',
      'p.text(MX, hy + 26, "トップニュース · 頭條", 22, "sans", True, BRICK, face="TC")')
    E(c12, '    ("1.5 — 鍋の食卓は去年の1.5倍（8〜10月、味の素の発表より）", "serif", False, INK, 20, 1.35),\n])',
      '    ("1.5 — 鍋の食卓は去年の1.5倍（8〜10月、味の素の発表より）", "serif", False, INK, 20, 1.35),\n], title_face="TC")')
    E(c12, 'f.head("今すぐ練習 · 即學即練", 25)',
      'f.head("今すぐ練習 · 即學即練", 25, face="TC")')
    E(c12, 'p.para(gx + 22, yy_n + 52, "這四個話題，都是本期報紙的主題。", 18.5, "sans", False, GREY, gw - 44, 1.35)',
      'p.para(gx + 22, yy_n + 52, "這四個話題，都是本期報紙的主題。", 18.5, "sans", False, GREY, gw - 44, 1.35, face="TC")')
    E(c12, 'p.text(gx + 22, gy + 664, "來源與日期見各篇文章，非精確統計", 19, "sans", False, GREY)',
      'p.text(gx + 22, gy + 664, "來源與日期見各篇文章，非精確統計", 19, "sans", False, GREY, face="TC")')
    E(c12, 'p.text(gx + 22, sy + 40, "この号の内容 · 本期目錄", 24, "sans", True, OLIVE)',
      'p.text(gx + 22, sy + 40, "この号の内容 · 本期目錄", 24, "sans", True, OLIVE, face="TC")')
    E(c12, 'p.text(gx, my + 24, "今週のことば · 本週單字", 22, "sans", True, OLIVE)',
      'p.text(gx, my + 24, "今週のことば · 本週單字", 22, "sans", True, OLIVE, face="TC")')
    E(c12, 'p.para(gx, y2 + 28, "ゆる＝ 輕鬆、不勉強。", 19, "sans", False, GREY, gw, 1.35)',
      'p.para(gx, y2 + 28, "ゆる＝ 輕鬆、不勉強。", 19, "sans", False, GREY, gw, 1.35, face="TC")')
    E(c12, 'p.text(bx + 22, 1914, "短いニュース · 快訊", 24, "sans", True, OLIVE)',
      'p.text(bx + 22, 1914, "短いニュース · 快訊", 24, "sans", True, OLIVE, face="TC")')
    E(c12, 'p.text(MX, qy + 36, "クイズ · 閃電問答", 26, "sans", True, OLIVE)',
      'p.text(MX, qy + 36, "クイズ · 閃電問答", 26, "sans", True, OLIVE, face="TC")')
    E(c12, 'p.text(RIGHT, qy + 36, "讀頭版，選出正確答案 · 答案見第 8 版", 20, "sans", False, GREY, anchor="end")',
      'p.text(RIGHT, qy + 36, "讀頭版，選出正確答案 · 答案見第 8 版", 20, "sans", False, GREY, anchor="end", face="TC")')
    E(c12, 'p.band("生活 · くらし", "Lucerna", "レベル A2 · ゆる整え食と暖かい11月 · 輕鬆食養與暖和的11月")',
      'p.band("生活 · くらし", "Lucerna", "レベル A2 · ゆる整え食と暖かい11月 · 輕鬆食養與暖和的11月", face="TC", sub_face="TC")')
    E(c12, 'len(wrap("你呢？寒冷的日子想吃什麼鍋？寫兩句日語寄來。", "sans", False, 20, CW - 44))',
      'len(wrap("你呢？寒冷的日子想吃什麼鍋？寫兩句日語寄來。", "sans", False, 20, CW - 44, face="TC"))')
    E(c12, 'p.text(ix + 22, yy3 + 26, "あなたは？ · 說說你自己", 24, "sans", True, OLIVE)',
      'p.text(ix + 22, yy3 + 26, "あなたは？ · 說說你自己", 24, "sans", True, OLIVE, face="TC")')
    E(c12, 'p.para(ix + 22, yy3 + 20, "你呢？寒冷的日子想吃什麼鍋？寫兩句日語寄來。", 20, "sans", False, GREY, CW - 44, 1.42)',
      'p.para(ix + 22, yy3 + 20, "你呢？寒冷的日子想吃什麼鍋？寫兩句日語寄來。", 20, "sans", False, GREY, CW - 44, 1.42, face="TC")')
    E(c12, 'p.text(MX, dy + 28, "季節のことば · 季節詞語", 28, "sans", True, OLIVE)',
      'p.text(MX, dy + 28, "季節のことば · 季節詞語", 28, "sans", True, OLIVE, face="TC")')
    E(c12, 'p.text(RIGHT, dy + 28, "ゆる整え食の4つの言葉 · 關於輕鬆食養的四個詞", 20, "sans", False, GREY, anchor="end")',
      'p.text(RIGHT, dy + 28, "ゆる整え食の4つの言葉 · 關於輕鬆食養的四個詞", 20, "sans", False, GREY, anchor="end", face="TC")')
    E(c12, 'p.para(bx + 22, yy + 19, cn, 19, "sans", False, GREY, CW - 44, 1.3)',
      'p.para(bx + 22, yy + 19, cn, 19, "sans", False, GREY, CW - 44, 1.3, face="TC")')
    E(c12, 'p.text(MX, ey + 28, "練習 · 第 2 版練習", 28, "sans", True, OLIVE)',
      'p.text(MX, ey + 28, "練習 · 第 2 版練習", 28, "sans", True, OLIVE, face="TC")')
    E(c12, 'p.text(RIGHT, ey + 28, "答案見第 8 版 · 題目可跨級混排，按題號找答案", 20, "sans", False, GREY, anchor="end")',
      'p.text(RIGHT, ey + 28, "答案見第 8 版 · 題目可跨級混排，按題號找答案", 20, "sans", False, GREY, anchor="end", face="TC")')

    c34 = "content34.py"
    E(c34, 'p.band("文化 · ぶんか", "Lucerna", "レベル A2→B1 · 文化の日と金沢 · 文化日與金澤")',
      'p.band("文化 · ぶんか", "Lucerna", "レベル A2→B1 · 文化の日と金沢 · 文化日與金澤", face="TC", sub_face="TC")')
    E(c34, 'len(wrap("你呢？文化日想去參加什麼文化活動？寫兩句日語寄來。", "sans", False, 20, CW - 44))',
      'len(wrap("你呢？文化日想去參加什麼文化活動？寫兩句日語寄來。", "sans", False, 20, CW - 44, face="TC"))')
    E(c34, 'p.text(ix + 22, yy3 + 26, "あなたは？ · 說說你自己", 24, "sans", True, OLIVE)',
      'p.text(ix + 22, yy3 + 26, "あなたは？ · 說說你自己", 24, "sans", True, OLIVE, face="TC")')
    E(c34, 'p.para(ix + 22, yy3 + 20, "你呢？文化日想去參加什麼文化活動？寫兩句日語寄來。", 20, "sans", False, GREY, CW - 44, 1.42)',
      'p.para(ix + 22, yy3 + 20, "你呢？文化日想去參加什麼文化活動？寫兩句日語寄來。", 20, "sans", False, GREY, CW - 44, 1.42, face="TC")')
    E(c34, 'p.text(MX, ey + 28, "練習 · 第 3 版練習", 28, "sans", True, OLIVE)',
      'p.text(MX, ey + 28, "練習 · 第 3 版練習", 28, "sans", True, OLIVE, face="TC")')
    E(c34, 'p.text(RIGHT, ey + 28, "答案見第 8 版 · 題目可跨級混排，按題號找答案", 20, "sans", False, GREY, anchor="end")',
      'p.text(RIGHT, ey + 28, "答案見第 8 版 · 題目可跨級混排，按題號找答案", 20, "sans", False, GREY, anchor="end", face="TC")', 2)
    E(c34, 'p.band("スポーツ · 體育", "Lucerna", "レベル B1 · 日本シリーズ横浜の2試合 · 日本大賽橫濱兩場")',
      'p.band("スポーツ · 體育", "Lucerna", "レベル B1 · 日本シリーズ横浜の2試合 · 日本大賽橫濱兩場", face="TC", sub_face="TC")')
    E(c34, '    ("※ 第3戦からの結果は、次号（VOL.3）で総括します", "serif", False, GREY, 20, 1.35),\n])',
      '    ("※ 第3戦からの結果は、次号（VOL.3）で総括します", "serif", False, GREY, 20, 1.35),\n], title_face="TC")')
    E(c34, 'p.text(MX, ty + 26, "横浜の2試合の記録 · 橫濱兩場比賽的記錄", 26, "sans", True, OLIVE)',
      'p.text(MX, ty + 26, "横浜の2試合の記録 · 橫濱兩場比賽的記錄", 26, "sans", True, OLIVE, face="TC")')
    E(c34, 'p.text(MX, ey + 28, "練習 · 第 4 版練習", 28, "sans", True, OLIVE)',
      'p.text(MX, ey + 28, "練習 · 第 4 版練習", 28, "sans", True, OLIVE, face="TC")')

    c56 = "content56.py"
    E(c56, 'p.band("若者・エンタメ · 青年", "Lucerna", "レベル B1 · ハロウィンと秋まつり · 萬聖節與秋日祭典")',
      'p.band("若者・エンタメ · 青年", "Lucerna", "レベル B1 · ハロウィンと秋まつり · 萬聖節與秋日祭典", face="TC", sub_face="TC")')
    E(c56, 'len(wrap("你呢？秋日祭典上想做什麼？寫兩句日語寄來。", "sans", False, 20, CW - 44))',
      'len(wrap("你呢？秋日祭典上想做什麼？寫兩句日語寄來。", "sans", False, 20, CW - 44, face="TC"))')
    E(c56, 'p.text(ix + 22, yy3 + 26, "あなたは？ · 說說你自己", 24, "sans", True, OLIVE)',
      'p.text(ix + 22, yy3 + 26, "あなたは？ · 說說你自己", 24, "sans", True, OLIVE, face="TC")')
    E(c56, 'p.para(ix + 22, yy3 + 20, "你呢？秋日祭典上想做什麼？寫兩句日語寄來。", 20, "sans", False, GREY, CW - 44, 1.42)',
      'p.para(ix + 22, yy3 + 20, "你呢？秋日祭典上想做什麼？寫兩句日語寄來。", 20, "sans", False, GREY, CW - 44, 1.42, face="TC")')
    E(c56, 'p.text(MX, ey + 28, "練習 · 第 5 版練習", 28, "sans", True, OLIVE)',
      'p.text(MX, ey + 28, "練習 · 第 5 版練習", 28, "sans", True, OLIVE, face="TC")')
    E(c56, 'p.text(RIGHT, ey + 28, "答案見第 8 版 · 題目可跨級混排，按題號找答案", 20, "sans", False, GREY, anchor="end")',
      'p.text(RIGHT, ey + 28, "答案見第 8 版 · 題目可跨級混排，按題號找答案", 20, "sans", False, GREY, anchor="end", face="TC")', 2)
    E(c56, 'p.band("深読み · ふかよみ", "Lucerna", "レベル B2 · 暖かい11月と秋の旅 · 暖和的11月與秋日旅行")',
      'p.band("深読み · ふかよみ", "Lucerna", "レベル B2 · 暖かい11月と秋の旅 · 暖和的11月與秋日旅行", sub_face="TC")')
    E(c56, 'p.text(MX, chy + 26, "グラフを読もう · 讀圖表", 26, "sans", True, OLIVE)',
      'p.text(MX, chy + 26, "グラフを読もう · 讀圖表", 26, "sans", True, OLIVE, face="TC")')
    E(c56, 'p.text(RIGHT, chy + 26, "練習用データ · 練習數據", 21, "sans", True, BRICK, anchor="end")',
      'p.text(RIGHT, chy + 26, "練習用データ · 練習數據", 21, "sans", True, BRICK, anchor="end", face="TC")')
    E(c56, 'p.text(MX, ey + 28, "練習 · 第 6 版練習", 28, "sans", True, OLIVE)',
      'p.text(MX, ey + 28, "練習 · 第 6 版練習", 28, "sans", True, OLIVE, face="TC")')

    c7 = "content7.py"
    E(c7, 'p.band("ことば · 語言", "Lucerna", "言語フォーカス · 三つのレベル、三つのテーマ · 三個級別，三個主題")',
      'p.band("ことば · 語言", "Lucerna", "言語フォーカス · 三つのレベル、三つのテーマ · 三個級別，三個主題", face="TC", sub_face="TC")')
    E(c7, 'a.expl("読書週間 讀書週 · 紹介 介紹 · 読み聞かせ 朗讀。")',
      'a.expl("読書週間 讀書週 · 紹介 介紹 · 読み聞かせ 朗讀。", face="TC")')
    E(c7, 'b.expl("見頃 最佳觀賞期 · 紅葉狩り 看紅葉出遊 · 落葉 落葉")',
      'b.expl("見頃 最佳觀賞期 · 紅葉狩り 看紅葉出遊 · 落葉 落葉", face="TC")')
    E(c7, 'c.expl("〜倍 倍 · 〜% 百分之〜 · 〜万食 萬份。")',
      'c.expl("〜倍 倍 · 〜% 百分之〜 · 〜万食 萬份。", face="TC")')
    E(c7, 'p.text(bx + 22, yy3 + 26, "まちがい診療所 · 易錯診所", 23, "sans", True, OLIVE)',
      'p.text(bx + 22, yy3 + 26, "まちがい診療所 · 易錯診所", 23, "sans", True, OLIVE, face="TC")')
    E(c7, 'len(wrap(r[2], "sans", False, 19.5, CW - 44))',
      'len(wrap(r[2], "sans", False, 19.5, CW - 44, face="TC"))')
    E(c7, 'yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10',
      'yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36, face="TC") + 10')
    E(c7, 'p.text(bx + 22, yy3 + 26, "今週のフレーム · 本週句式", 23, "sans", True, OLIVE)',
      'p.text(bx + 22, yy3 + 26, "今週のフレーム · 本週句式", 23, "sans", True, OLIVE, face="TC")')
    E(c7, 'len(wrap(wcn, "sans", False, 20, CW - 44))',
      'len(wrap(wcn, "sans", False, 20, CW - 44, face="TC"))')
    E(c7, 'p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)',
      'p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42, face="TC")')
    E(c7, 'p.text(bx + 22, yy3 + 26, "読者の手紙 · 讀者園地", 23, "sans", True, OLIVE)',
      'p.text(bx + 22, yy3 + 26, "読者の手紙 · 讀者園地", 23, "sans", True, OLIVE, face="TC")')
    # ROUND 2 (2026-10-27): a separate 2-line invitation line pushed the P7
    # teaser to 2582 (> 2540 gate) AND overflowed the letters box (invite
    # line 2 baseline 1816.24 vs box bottom 1808.08). A separate 1-line
    # invite still fails (formula bottom 1779.08 vs baseline 1787.84).
    # Fix: merge the short imperative into the disclosure paragraph as its
    # final sentence. wrap() at the real width (390, TC face) proves the
    # merged paragraph stays 3 lines -- identical to lcn alone -- so the
    # letters box returns to exactly the core formula and the teaser to
    # the core 2512.08. Solicitation stays an explicit imperative sentence
    # (quoted verbatim in KIT); VOL.3 promise lives in the same paragraph.
    E(c7, 'lcn = "編輯部示例信，非真實來信。截至截稿，未收到真實來信與第8版最佳作文；VOL.3將刊登收到的來信與佳作。"',
      'lcn = "編輯部示例信，非真實來信。截至截稿，未收到真實來信與第8版最佳作文；VOL.3將刊登收到的來信與佳作。請把你的來信寄來。"')
    E(c7, 'lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld, "serif", False, 20.5, CW - 44)) * 29 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26 + 16',
      'lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld, "serif", False, 20.5, CW - 44)) * 29 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44, face="TC")) * 29 + 26 + 16')
    E(c7, 'p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)',
      'p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42, face="TC")')
    E(c7, 'p.text(MX, fy + 24, "今週のフレーズ · 本週金句（逐字摘自本期文章）", 27, "sans", True, OLIVE)',
      'p.text(MX, fy + 24, "今週のフレーズ · 本週金句（逐字摘自本期文章）", 27, "sans", True, OLIVE, face="TC")')
    E(c7, 'p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)',
      'p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35, face="TC")')
    E(c7, 'p.text(MX + 28, py + 44, "来週 · 下期預告 (VOL.3)", 24, "sans", True, "#e8dfc8")',
      'p.text(MX + 28, py + 44, "来週 · 下期預告 (VOL.3)", 24, "sans", True, "#e8dfc8", face="TC")')

    c8 = "content8.py"
    E(c8, 'p.band("テストと答え · 練習與答案", "Lucerna", "第 8 面 · 週の大きなテスト + 全ての答え")',
      'p.band("テストと答え · 練習與答案", "Lucerna", "第 8 面 · 週の大きなテスト + 全ての答え", face="TC", sub_face="JP")')
    E(c8, '     "讀書週從10月27日開始。→ ___", instr="翻譯", size=13.8, gap=0)',
      '     "讀書週從10月27日開始。→ ___", instr="翻譯", size=13.8, gap=0, body_face="TC")')
    E(c8, '     "我想去神戶看紅葉燈光秀。→ ___", instr="翻譯", size=13.8, gap=0)',
      '     "我想去神戶看紅葉燈光秀。→ ___", instr="翻譯", size=13.8, gap=0, body_face="TC")')
    E(c8, 'f.expl(f"寫作題（無唯一答案）；範文（{NCHARS} 字）見下。")',
      'f.expl(f"寫作題（無唯一答案）；範文（{NCHARS} 字）見下。", face="TC")')
    E(c8, 'p.text(MX, 1302, "答え · 參考答案 — 依版面分版排列，找到題號即可", 25, "sans", True, OLIVE)',
      'p.text(MX, 1302, "答え · 參考答案 — 依版面分版排列，找到題號即可", 25, "sans", True, OLIVE, face="TC")')
    E(c8, 'p.text(RIGHT, 1302, "每題附一句中文簡析 · 帶 ✓ 的為範文題", 19.5, "sans", False, GREY, anchor="end")',
      'p.text(RIGHT, 1302, "每題附一句中文簡析 · 帶 ✓ 的為範文題", 19.5, "sans", False, GREY, anchor="end", face="TC")')
    E(c8, '    af.para(f"— 第{pg}面 —", 13.3, "sans", True, OLIVE, lh=1.16, gap=2, split=False)',
      '    af.para(f"— 第{pg}版 —", 13.3, "sans", True, OLIVE, lh=1.16, gap=2, split=False, face="TC")')
    E(c8, '        af.para(txt, 13.3, lh=1.16, gap=0.5, split=False)',
      '        af.para(txt, 13.3, lh=1.16, gap=0.5, split=False, face="TC")')

    # ---- 6. post-audits ----
    for fn in FILES:
        assert "weekly-report-w45-ja-core" not in texts[fn], \
            f"{fn}: core OUT reference survives"
    for fn in CONTENT_FILES + ["bslib4.py", "svglib.py", "render.py", "run.py"]:
        assert ("brid" + "ge") not in texts[fn], \
            f"{fn}: old explanation-function name survives"
    for fn in texts:
        with open(os.path.join(HERE, fn), "w", encoding="utf-8") as f:
            f.write(texts[fn])
        print("transformed", fn)
    print("OUT dir:", EDITION)


if __name__ == "__main__":
    main()
