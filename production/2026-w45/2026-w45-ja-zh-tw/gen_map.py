# -*- coding: utf-8 -*-
"""One-time MAP generator for JA x ZH-TW W45 (NOT a fix-round file).

Input: hand-classified OLD literals (type C/G/M/H, see below).
  C = pure Chinese text -> whole-literal conversion.
  G = gloss/expl rows joined by " · ": first whitespace token of each
      segment is the Japanese headword (kept byte-identical), the rest
      is Chinese (converted).
  M = mixed furniture joined by " · ": a segment containing kana, or
      exactly "来週", is Japanese (kept); other segments are Chinese.
  H = hand-written Traditional form (bypasses conversion).
Conversion = OpenCC s2twp, then Taiwan/family overrides in order:
  数据 -> 數據 (not s2twp 資料; W43 same-pairing usage),
  读书周 -> 讀書週 (s2twp keeps 讀書周),
  weekday 週X -> 星期X (X in 一二三四五六日; matches the P7 phrase
      translation's existing 星期二 and the W43 same-pairing 星期六),
  单词 -> 單字 (not s2twp 單詞; W43 same-pairing usage),
  日元 -> 日圓 (Taiwan currency usage; W43 same-pairing usage),
  quote restore: 「靜かだけど、冒険中。」 -> 「静かだけど、冒険中。」
      (the slogan quote inside a Chinese note stays Japanese).
Entries whose conversion is identical are dropped as NOOP (listed for
review: shared-glyph Chinese or Japanese-neutral strings).
Output: map.json (old -> new, non-noop only) + map_review.txt (all).
Fix rounds after round 1 edit transform.py directly, NOT this file.
"""
import json
import os
import re

import opencc

HERE = os.path.dirname(os.path.abspath(__file__))
CORE = os.path.expanduser(
    "~/workspace/goals/lucernaread-social-media-operations/"
    "hidden_files/weekly-report-w45-ja-build")
FILES = ["content12.py", "content34.py", "content56.py", "content7.py",
         "content8.py"]
CC = opencc.OpenCC("s2twp")


def has_kana(s):
    return any(0x3040 <= ord(c) <= 0x30FF for c in s)


def overrides(old, new):
    if "数据" in old:
        new = new.replace("資料", "數據")
    if "读书周" in old:
        new = new.replace("讀書周", "讀書週")
    new = re.sub(r"週([一二三四五六日])", r"星期\1", new)
    if "单词" in old:
        new = new.replace("單詞", "單字")
    if "日元" in old:
        new = new.replace("日元", "日圓")
    if "「静かだけど、冒険中。」" in old:
        new = new.replace("「靜かだけど、冒険中。」",
                          "「静かだけど、冒険中。」")
    return new


def conv_c(old):
    return overrides(old, CC.convert(old))


def conv_g(old):
    parts = []
    for seg in old.split(" · "):
        if " " in seg:
            head, rest = seg.split(" ", 1)
            parts.append(head + " " + overrides(old, CC.convert(rest)))
        else:
            parts.append(seg)
    return " · ".join(parts)


def conv_m(old):
    parts = []
    for seg in old.split(" · "):
        if has_kana(seg) or seg == "来週":
            parts.append(seg)
        else:
            parts.append(overrides(old, CC.convert(seg)))
    return " · ".join(parts)


# (old, type); H entries carry their new form as a third element.
RAW = [
    # ---- C: pure Chinese (notes, keys, stems, instr, typ, CN paras) ----
    ("文化日在11月3日（周二）", "C"),
    ("读书周到11月9日（周一）", "C"),
    ("見頃＝最佳观赏期", "C"),
    ("立冬＝冬天的开始", "C"),
    ("神户灯光秀从7日（周六）开始", "C"),
    ("文化日全国都有文化活动", "C"),
    ("立冬在11月7日（周六）", "C"),
    ("灯光秀在神户开始", "C"),
    ("「ゆる」＝无理をしない", "C"),
    ("ゆる＝轻松、不勉强", "C"),
    ("蒸し器＝蒸笼", "C"),
    ("整える＝调理、调养", "C"),
    ("鍋＝一锅菜", "C"),
    ("ゆる＝轻松 b", "C"),
    ("蒸し器＝蒸笼 a", "C"),
    ("杉并的活动是家庭管弦乐队", "C"),
    ("传统工艺展在石川县立美术馆", "C"),
    ("工艺展到11月8日（周日）", "C"),
    ("灯光秀在金泽城和兼六园", "C"),
    ("市場＝集市", "C"),
    ("陶器＝陶瓷", "C"),
    ("工艺展到11月8日", "C"),
    ("主语＋时间", "C"),
    ("地点＋で＋あります", "C"),
    ("见たい＝想看", "C"),
    ("第1战软银3-1胜DeNA", "C"),
    ("第2战逆转的是筒香的3分本垒打", "C"),
    ("2连胜开局的是软银", "C"),
    ("2连胜开局的夺冠率是73%", "C"),
    ("2024年夺冠的是DeNA", "C"),
    ("第1战软银得3分", "C"),
    ("第2战软银得4分", "C"),
    ("第1战打到延长11局", "C"),
    ("第2战打到延长10局", "C"),
    ("夺冠率73%", "C"),
    ("延長＝比赛延长", "C"),
    ("第1战观众33,388人", "C"),
    ("第2战观众33,432人", "C"),
    ("相川监督说「4场胜负之战」", "C"),
    ("万圣节在10月31日（周六）", "C"),
    ("涩谷禁酒时间是18时到5时", "C"),
    ("乱扔垃圾罚款2,000日元", "C"),
    ("化妆活动在池袋", "C"),
    ("横滨中区民祭在11月8日（周日）", "C"),
    ("万圣节在10月31日", "C"),
    ("禁酒从18时开始", "C"),
    ("禁酒到早上5时", "C"),
    ("横滨祭典在11月8日", "C"),
    ("夜里路上不能喝酒", "C"),
    ("フェンスの中＝围栏里面", "C"),
    ("活动从10月30日到11月1日", "C"),
    ("图中最受欢迎的是近处的满足感", "C"),
    ("近场满足感38%", "C"),
    ("温泉27%", "C"),
    ("红叶21%与美食14%之差为7", "C"),
    ("四项合计100%", "C"),
    ("神户灯光秀到12月28日", "C"),
    ("九州旅行搜索约为去年的2倍", "C"),
    ("气象厅预报在10月20日", "C"),
    ("读书周从10月27日（周二）开始", "C"),
    ("读书周到11月9日", "C"),
    ("口号是「静かだけど、冒険中。」", "C"),
    ("图书馆活动有图书介绍", "C"),
    ("見頃＝红叶最美的时候", "C"),
    ("紅葉狩り＝去看红叶", "C"),
    ("ライトアップ＝夜里用灯光照亮", "C"),
    ("落葉＝落叶", "C"),
    ("日本大赛第1战在10月24日（周六）", "C"),
    ("第2战软银4-3获胜", "C"),
    ("神户灯光秀从7日开始", "C"),
    ("传统工艺展到11月8日", "C"),
    ("气象厅预报气温高于往年", "C"),
    ("美香周二和家人去金泽", "C"),
    ("在金泽看传统工艺展和灯光秀", "C"),
    ("周六和朋友去神户", "C"),
    ("读书周想借2本书", "C"),
    ("主语＋时间＋地点＋动词", "C"),
    ("场所用「で」", "C"),
    ("2连胜开局", "C"),
    ("对照第3版", "C"),
    ("对照第5版", "C"),
    ("对照第7版", "C"),
    ("对照第6版（神户的灯光秀）", "C"),
    ("見せてください＝请出示", "C"),
    ("读书周到11月9日（第7版）", "C"),
    ("「紅葉の本」受欢迎", "C"),
    ("どういたしまして＝不客气", "C"),
    ("見頃＝最佳观赏期 b", "C"),
    ("鍋＝一锅菜 d", "C"),
    ("落葉＝落叶 a", "C"),
    ("予算＝预算 c", "C"),
    ("乱扔垃圾，要罚2,000日元。", "C"),
    ("读书周从10月27日开始。→ ___", "C"),
    ("我想去神户看红叶灯光秀。→ ___", "C"),
    ("（开放题，范文如下）", "C"),
    ("范文见本版 H 区（{NCHARS} 字）", "C"),
    ("写作题（无唯一答案）；范文（{NCHARS} 字）见下。", "C"),
    ("单选", "C"),
    ("完形单选", "C"),
    ("判断对错", "C"),
    ("词汇配对", "C"),
    ("翻译", "C"),
    ("写作", "C"),
    ("把词和释义配对", "C"),
    ("把活动和地点·时间配对", "C"),
    ("判断", "C"),
    ("这四个话题，都是本期报纸的主题。", "C"),
    ("来源与日期见各篇文章，非精确统计", "C"),
    ("读头版，选出正确答案 · 答案见第 8 版", "C"),
    ("你呢？寒冷的日子想吃什么锅？写两句日语寄来。", "C"),
    ("你呢？文化日想去参加什么文化活动？写两句日语寄来。", "C"),
    ("你呢？秋日祭典上想做什么？写两句日语寄来。", "C"),
    ("有「昨日」时要用过去式。", "C"),
    ("动词名词化时要加「こと」。", "C"),
    ("地点用「か所」来数。", "C"),
    ("动作发生的场所用「で」。", "C"),
    ("句式拆解：轻松地调理身心。", "C"),
    ("编辑部示例信，非真实来信。截至截稿，未收到真实来信与第8版最佳作文；VOL.3将刊登收到的来信与佳作。", "C"),
    ("文化日是11月3日星期二。", "C"),
    ("这是一个慢慢地、轻松调理的日本11月。", "C"),
    ("所谓ゆる，就是不勉强、慢慢来的意思。", "C"),
    ("火锅食材提前一个月上架了。", "C"),
    ("可以同时欣赏传统工艺、红叶与灯光。", "C"),
    ("软银以两连胜开局。", "C"),
    ("遵守规则，过一个快乐的万圣节吧。", "C"),
    ("去看红叶的人可以自北向南追赶最佳观赏期。", "C"),
    ("ゆる＝ 轻松、不勉强。", "C"),
    ("答案见第 8 版 · 题目可跨级混排，按题号找答案", "C"),
    ("每题附一句中文简析 · 带 ✓ 的为范文题", "C"),
    ("周二是文化日", "C"),
    ("节日过后，红叶周末到来 · 详见第 3 版", "C"),
    ("一锅菜", "C"),
    ("蒸笼", "C"),
    ("轻松、不勉强", "C"),
    ("调理、调养", "C"),
    # ---- G: gloss / P7 expl rows ----
    ("祝日 节假日 · 見頃 最佳观赏期 · 暦 历法 · お届けします 为您送上。", "G"),
    ("蒸す 蒸 · 並ぶ 摆上货架 · 食卓 餐桌 · 超える 超过。", "G"),
    ("予報 预报 · 平年 往年平均 · 季節風 季风 · 話題 话题 · 値上がり 涨价。", "G"),
    ("市場 市场 · 工芸 工艺 · 光 灯光 · 楽しむ 享受。", "G"),
    ("陶器 陶瓷 · 漆器 漆器 · 染物 染色织物 · 金箔 金箔。", "G"),
    ("延長 延长赛 · 逆転 逆转 · 同点 平分 · 優勝率 夺冠率。", "G"),
    ("総括 总结 · 締め切り 截稿 · 確認する 核实。", "G"),
    ("罰金 罚款 · 像 雕像 · 仮装 变装 · 守る 遵守。", "G"),
    ("祭り 节日 · 週末 周末 · 話題 话题。", "G"),
    ("予算 预算 · 満足 满足 · 観測 观测 · 追いかける 追赶。", "G"),
    ("読書週間 读书周 · 紹介 介绍 · 読み聞かせ 朗读。", "G"),
    ("見頃 最佳观赏期 · 紅葉狩り 看红叶出游 · 落葉 落叶", "G"),
    ("〜倍 倍 · 〜% 百分之〜 · 〜万食 万份。", "G"),
    # ---- M: mixed furniture ----
    ("トップニュース · 头条", "M"),
    ("数字で見る今週 · 数字看本周", "M"),
    ("今すぐ練習 · 即学即练", "M"),
    ("この号の内容 · 本期目录", "M"),
    ("今週のことば · 本周单词", "M"),
    ("短いニュース · 快讯", "M"),
    ("クイズ · 闪电问答", "M"),
    ("レベル A2 · ゆる整え食と暖かい11月 · 轻松食养与暖和的11月", "M"),
    ("あなたは？ · 说说你自己", "M"),
    ("季節のことば · 季节词语", "M"),
    ("ゆる整え食の4つの言葉 · 关于轻松食养的四个词", "M"),
    ("練習 · 第 2 版练习", "M"),
    ("練習 · 第 3 版练习", "M"),
    ("練習 · 第 4 版练习", "M"),
    ("練習 · 第 5 版练习", "M"),
    ("練習 · 第 6 版练习", "M"),
    ("レベル A2→B1 · 文化の日と金沢 · 文化日与金泽", "M"),
    ("スポーツ · 体育", "M"),
    ("レベル B1 · 日本シリーズ横浜の2試合 · 日本大赛横滨两场", "M"),
    ("日本シリーズの日程 · 大赛日程", "M"),
    ("横浜の2試合の記録 · 横滨两场比赛的记录", "M"),
    ("若者・エンタメ · 青年", "M"),
    ("レベル B1 · ハロウィンと秋まつり · 万圣节与秋日祭典", "M"),
    ("レベル B2 · 暖かい11月と秋の旅 · 暖和的11月与秋日旅行", "M"),
    ("グラフを読もう · 读图表", "M"),
    ("練習用データ · 练习数据", "M"),
    ("ことば · 语言", "M"),
    ("言語フォーカス · 三つのレベル、三つのテーマ · 三个级别，三个主题", "M"),
    ("まちがい診療所 · 易错诊所", "M"),
    ("今週のフレーム · 本周句式", "M"),
    ("読者の手紙 · 读者园地", "M"),
    ("今週のフレーズ · 本周金句（逐字摘自本期文章）", "M"),
    ("来週 · 下期预告 (VOL.3)", "M"),
    ("テストと答え · 练习与答案", "M"),
    # ---- H: hand-written forms ----
    ("答え · 参考答案 — 按版面分页排列，找到题号即可", "H",
     "答え · 參考答案 — 依版面分版排列，找到題號即可"),
    ("工芸＝工艺", "H", "工芸＝工藝"),
    ("第1面", "H", "第1版"),
    ("第2面", "H", "第2版"),
    ("第3面", "H", "第3版"),
    ("第4面", "H", "第4版"),
    ("第5面", "H", "第5版"),
    ("第6面", "H", "第6版"),
]

CONV = {"C": conv_c, "G": conv_g, "M": conv_m}
texts = {}
for fn in FILES:
    texts[fn] = open(os.path.join(CORE, fn), encoding="utf-8").read()

out = {}
review = []
for entry in RAW:
    old, typ = entry[0], entry[1]
    if typ == "H":
        new = entry[2]
    else:
        new = CONV[typ](old)
    qold = '"' + old + '"'
    cnt = sum(t.count(qold) for t in texts.values())
    per = {fn: texts[fn].count(qold) for fn in FILES if texts[fn].count(qold)}
    if new == old:
        review.append(f"NOOP [{typ}] cnt={cnt} {per} :: {old!r}")
        continue
    if "周" in new:
        review.append(f"WARN-周-left [{typ}] cnt={cnt} :: {old!r} -> {new!r}")
    assert old not in out, f"duplicate old: {old!r}"
    out[old] = new
    review.append(f"[{typ}] cnt={cnt} {per} :: {old!r} -> {new!r}")
    assert cnt >= 1, f"OLD NEVER OCCURS (quoted): {old!r}"

with open(os.path.join(HERE, "map.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
with open(os.path.join(HERE, "map_review.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(review) + "\n")
print(f"MAP entries: {len(out)}, NOOP: {len(review)-len(out)}")
print(f"wrote map.json + map_review.txt")
