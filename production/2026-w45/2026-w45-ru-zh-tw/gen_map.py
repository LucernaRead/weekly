# -*- coding: utf-8 -*-
"""Generate the Simplified->Traditional literal map for the RU x ZH-TW build.

Method: per-character standard conversion for the corpus chars, then
word-level Taiwan/HK usage overrides, then furniture verbatim overrides
from the shipped W43 RU x ZH-TW edition. The output map.json + review
file are inspected by hand before any file is transformed.
"""
import re, os, json

B = os.path.dirname(os.path.abspath(__file__))
FILES = ["content12.py", "content34.py", "content56.py", "content7.py",
         "content8.py", "bslib4.py", "svglib.py"]

PAIRS = (
    "万萬与與两兩为為么麼义義乐樂习習乱亂于於会會伦倫体體余餘"
    "兑兌关關养養写寫军軍几幾别別办辦动動区區单單历歷参參双雙"
    "变變号號团團图圖圣聖场場够夠头頭夹夾举舉学學实實宾賓对對"
    "将將尔爾属屬带帶广廣应應开開录錄态態战戰报報换換据據数數"
    "无無时時机機条條来來汇匯泽澤点點状狀玛瑪现現电電着著码碼"
    "确確离離简簡级級练練结結给給续續编編缩縮罗羅聪聰胜勝节節"
    "范範见見让讓讯訊讲講许許诊診词詞译譯详詳语語说說请請诺諾"
    "读讀调調谈談账賬购購贸貿赛賽车車转轉轮輪较較辈輩辑輯输輸"
    "达達过過这這连連选選释釋里裡销銷错錯长長闪閃问問间間队隊"
    "阳陽阵陣陆陸静靜页頁项項顺順顾顧预預题題邮郵"
    "个個后後周週组組价價该該"
)
assert len(PAIRS) % 2 == 0
CHARMAP = {}
for i in range(0, len(PAIRS), 2):
    sc, tc = PAIRS[i], PAIRS[i + 1]
    assert sc not in CHARMAP, sc
    CHARMAP[sc] = tc

WORD_OVERRIDES = [
    ("範文", "範本"),
    ("報道", "報導"),
    ("日歷", "日曆"),
]

# Furniture verbatim from shipped W43 RU x ZH-TW (old core segment -> new).
FURNITURE = {
    "КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · 俄语正文 · 中文讲解":
        "КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · 每週一期 · 讀俄羅斯人正在讀的俄語",
    "Lucerna · 俄语周报 VOL.2 · LUCERNA RUSSIAN WEEKLY":
        "Lucerna · 俄語週報 VOL.2 · 正文俄語 · 講解繁體中文",
    "ОТВЕТЫ · 参考答案 — 按版面分页排列，找到题号即可":
        "ОТВЕТЫ · 全部答案與簡析（第 1–8 版）",
    "СЛОВО НЕДЕЛИ · 本周单词": "СЛОВО НЕДЕЛИ · 本週單字",
}


def is_cjk(ch):
    o = ord(ch)
    return (0x4E00 <= o <= 0x9FFF) or (0x3400 <= o <= 0x4DBF)


def convert(seg):
    out = "".join(CHARMAP.get(c, c) for c in seg)
    for a, b in WORD_OVERRIDES:
        out = out.replace(a, b)
    return out


def main():
    mapping = {}   # old segment -> new segment (only when changed)
    kept = set()   # CJK chars kept as-is (identity glyphs)
    per_file = {}
    for fn in FILES:
        src = open(os.path.join(B, fn), encoding="utf-8").read()
        segs = re.findall(r'"((?:[^"\\\n]|\\.)*)"', src)
        cjk_segs = [s for s in segs if any(is_cjk(c) for c in s)]
        per_file[fn] = len(cjk_segs)
        for s in cjk_segs:
            for c in s:
                if is_cjk(c) and c not in CHARMAP:
                    kept.add(c)
            if s in FURNITURE:
                new = FURNITURE[s]
            else:
                new = convert(s)
            if new != s:
                if s in mapping and mapping[s] != new:
                    raise SystemExit(f"CONFLICT for {s!r}: {mapping[s]!r} vs {new!r}")
                mapping[s] = new
    print("per-file CJK segment counts:", per_file)
    print("mapped (changed) unique segments:", len(mapping))
    print("CJK chars kept as-is (must all be shared glyphs):")
    print("".join(sorted(kept)))
    with open(os.path.join(B, "map.json"), "w", encoding="utf-8") as f:
        json.dump(mapping, f, ensure_ascii=False, indent=1)
    with open(os.path.join(B, "map_review.txt"), "w", encoding="utf-8") as f:
        for old in sorted(mapping):
            f.write(f"{old}  ==>  {mapping[old]}\n")
    print("wrote map.json + map_review.txt")


if __name__ == "__main__":
    main()
