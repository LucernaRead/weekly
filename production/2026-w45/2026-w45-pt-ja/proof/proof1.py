#!/usr/bin/env python3
"""Independent PTxJA W45 proofread script 1: text extraction, latin tokens,
bridge-word scan, removed-string audit, JA word-level residual scan,
single-char scan, orphan/small-kana line-start scan, P7 definition, gloss,
golden sentences, exercise/level counts."""
import json, re, sys, unicodedata
from collections import Counter
from xml.etree import ElementTree as ET

GOAL = "/home/hatch/workspace/goals/lucernaread-social-media-operations"
ED = GOAL + "/files/weekly-report-w45-pt-ja/svg"
CO = GOAL + "/files/weekly-report-w45-pt-core/svg"
PAGES = ["p1-capa","p2-vida","p3-cultura","p4-esporte","p5-jovens","p6-aprofundamento","p7-lingua","p8-avaliacao"]

def texts(d, pg):
    t = ET.parse(f"{d}/{pg}.svg")
    out = []
    for el in t.iter():
        if el.tag.endswith("text") and el.text:
            out.append(el.text)
    return out

def alltexts(d):
    return {pg: texts(d, pg) for pg in PAGES}

ed = alltexts(ED); co = alltexts(CO)
edflat = [" ".join(v) for v in ed.values()]
coflat = [" ".join(v) for v in co.values()]

# ---- 1. bridge word ----
for name, blob in [("edition-svg", " ".join(edflat)), ("core-svg", " ".join(coflat))]:
    print(f"BRIDGE {name}: count={blob.count('桥接')}")
with open(GOAL+"/files/weekly-report-w45-pt-ja/WEEKLY-KIT.md", encoding="utf-8") as f:
    kit = f.read()
with open(GOAL+"/files/weekly-report-w45-pt-ja/ABSTRACT.txt", encoding="utf-8") as f:
    ab = f.read()
print(f"BRIDGE kit: {kit.count('桥接')} abstract: {ab.count('桥接')}")

# ---- 2. latin token multiset ----
LAT = re.compile(r"[A-Za-zÀ-ÿĀ-ſ0-9][A-Za-zÀ-ÿĀ-ſ0-9'’\-]*")
def lat_tokens(strs):
    c = Counter()
    for s in strs:
        for tok in LAT.findall(s):
            c[tok] += 1
    return c
ce, cc = Counter(), Counter()
for pg in PAGES:
    ce.update(lat_tokens(ed[pg])); cc.update(lat_tokens(co[pg]))
print(f"LATIN core_total={sum(cc.values())} edition_total={sum(ce.values())}")
diff = Counter()
for k in set(ce) | set(cc):
    d = ce[k]-cc[k]
    if d: diff[k] = d
print(f"LATIN distinct_diff_tokens={len(diff)}")
for k, d in sorted(diff.items(), key=lambda kv: -abs(kv[1])):
    print(f"  LATDIFF {k!r} {d:+d} (core {cc[k]} -> ed {ce[k]})")

# ---- 3. removed strings audit (from freeze diff json) ----
with open(GOAL+"/hidden_files/w45/pt-ja-proof/freeze-diff.json", encoding="utf-8") as f:
    fd = json.load(f)
print("FREEZE-DIFF-KEYS:", list(fd.keys())[:20])
print(json.dumps(fd, ensure_ascii=False)[:1500])

# ---- 4. JA word-level residual scan (own list) ----
blob = "\n".join(edflat)
# Chinese-specific words/phrases that must NOT appear as Chinese usage.
# Each is adjudicated by context: print every hit with surrounding context.
RESIDUAL = [
 # tense/grammar (Chinese forms)
 "过去时","现在时","将来时","虚拟式将来","祈使式","不定式","主语","宾语","表语","疑问词","复数","动词",
 "时态","考试","节日","墓园","决赛","证件","考场","题型","栏目",
 "高考","作文","确认卡","黑笔","开考","关门","大门","亡灵节","墓碑","蜡烛","菊花","弥撒","献花","怀念","寂静","祈祷","点燃",
 "首回合","次回合","决赛球队","决战","轮次","冲刺","前夕","突击","准备好","头脑",
 "生活","青年","体育","深读","语言","练习与答案","参考答案","简析","填空","造句","翻译","写作","判断","配对","完成句子",
 "单选","完形单选","目录","快讯","闪电问答","头条","本周生词","常见错误","本周金句","下期预告",
 "连休","复习","计划","时间表","迟到","规则","仪式","家庭记忆","万圣节","对照","逐日历",
 "次回合结果","州议会复会","足球","冲刺五步","两天制","分钟图","读数","诊所","金句","读者园地",
 "最佳作文","真实来信","截稿","顺延","承诺","征集",
 # simplified-only characters in shared words would be caught by char scan below; word list here is semantic
 "让","认","说","对","发","观","讲","读","欢","难","仅","汉","冯","龙","龟","齐","齿",
]
print("=== JA WORD-LEVEL RESIDUAL HITS ===")
hits = 0
for w in RESIDUAL:
    idx = 0
    while True:
        i = blob.find(w, idx)
        if i < 0: break
        print(f"  HIT {w!r} ...{blob[max(0,i-25):i+len(w)+25]!r}")
        hits += 1; idx = i + len(w)
print(f"RESIDUAL total_hits={hits} (each must be adjudicated; 0 = clean)")

# simplified-only glyph scan (chars that do not exist in Japanese joyo/standard usage)
SIMP_ONLY = set("连语说让认证备复发对观讲读欢难时际长马风电话车东头练仅汉冯龙龟齐齿为发过")
print("=== SIMPLIFIED-ONLY GLYPH HITS ===")
sh = 0
for pg in PAGES:
    for s in ed[pg]:
        for ch in s:
            if ch in SIMP_ONLY:
                print(f"  SIMP {pg} {ch!r} in {s!r}"); sh += 1
print(f"SIMP total={sh}")
# NOTE: several of these (时,发,对,读,长,风,电,话,车,东,头,练,马) ARE valid Japanese kanji;
# they are listed only to force explicit adjudication, not as automatic fails.
print("=== SINGLE-CHAR LEGAL-JA CHECK: chars present that single-char scans flag ===")
for w in ["現在形","目的語","場所","墓地","終了","不可","文化","数字"]:
    print(f"  LEGAL-WORD {w}: present={w in blob}")

# ---- 5. line-start orphan / small kana scan ----
SMALL = set("ぁぃぅぇぉっゃゅょァィゥェォッャュョ")
CLOSERS = set("、。）」』】〗》〕〉,.!?%:;\"'）」")
print("=== LINE-START SCAN (per <text> element start char) ===")
orph = 0
for pg in PAGES:
    for s in ed[pg]:
        st = s.strip()
        if st and (st[0] in SMALL or st[0] in CLOSERS):
            print(f"  ORPHAN {pg} {s!r}"); orph += 1
print(f"ORPHAN total={orph}")
print("=== P5 prompt lines ===")
for s in ed["p5-jovens"]:
    if "送ってください" in s or "前夜" in s:
        print(f"  P5 {s!r}")

# ---- 6. P7 definition verbatim ----
print("=== P7 feriadão definition ===")
for s in ed["p7-lingua"]:
    if "feriad" in s or "três dias" in s:
        print(f"  ED P7 {s!r}")
for s in co["p7-lingua"]:
    if "feriad" in s or "três dias" in s:
        print(f"  CO P7 {s!r}")

# ---- 7. exercise numbers / levels from SVG text ----
print("=== EXERCISE NUMBERS (P8 key lines + question markers) ===")
nums = set()
for pg in PAGES:
    for s in ed[pg]:
        m = re.match(r"\s*(\d{1,3})\.\s", s)
        if m: nums.add(int(m.group(1)))
print(f"  distinct leading-number items={len(nums)} min={min(nums)} max={max(nums)} missing={[n for n in range(1,151) if n not in nums]}")
for lvl in ["A2","B1","B2"]:
    cnt = sum(s.count(f"[{lvl}]") for pg in PAGES for s in ed[pg])
    print(f"  badge-string [{lvl}] occurrences in SVG text nodes: {cnt}")
