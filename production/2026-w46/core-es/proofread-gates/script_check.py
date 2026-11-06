import re, glob, html, collections, json, os
def load_texts(path):
    s=open(path,encoding="utf-8").read()
    return [html.unescape(re.sub(r"<[^>]+>","",c)) for c in re.findall(r"<text[^>]*>(.*?)</text>", s, re.S)]
def edition_texts(code):
    out={}
    d=f"{os.path.expanduser('~')}/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-es-{code}/svg"
    for fn in sorted(glob.glob(d+"/*.svg")):
        pg=re.match(r"p(\d+)", os.path.basename(fn)).group(1)
        out[pg]=load_texts(fn)
    return out
# Simplified-only probe (codepoint-exact). Each entry: char, U+code, note
PROBE_ZHTW = "说这让读对国为发广长门见贝车马头电话语体简议证权观现实习练写买卖气间从没给还过进远点尔汉龙凤龟齐龄产严丽万与丰务东条劳时实处"
# note: 时/实/处 are shared? 时 U+65F6 is simplified of 時; 实 U+5B9E simplified of 實; 处 U+5904 simplified of 處. Keep but flag separately.
# For JA: subset that is never Japanese kanji
PROBE_JA = "说这让读对为发广长门见贝车马头电话语简议证权观实习练写买卖气间从没给还过进远点汉龙凤龟齐龄产严丽万与丰务条"
for code, probe in [("zh-tw", PROBE_ZHTW), ("ja", PROBE_JA)]:
    print(f"\n===== {code} Simplified-only probe (absolute counts) =====")
    ed=edition_texts(code)
    total=collections.Counter()
    contexts=[]
    for pg, strs in ed.items():
        for s in strs:
            for ch in probe:
                n=s.count(ch)
                if n:
                    total[ch]+=n
                    contexts.append((pg,ch,s))
    for ch,n in total.most_common():
        print(f"  U+{ord(ch):04X} {ch} x{n}")
        for pg,c,s in contexts:
            if c==ch:
                print(f"     P{pg}: {s[:140]}")
                break
    if not total: print("  (none)")
# Also: zh-tw edition — count Traditional-only marker chars to confirm conversion happened
print("\n===== zh-tw Traditional markers =====")
ed=edition_texts("zh-tw")
allstr="".join(s for v in ed.values() for s in v)
for ch in "說這讓讀對國為發廣長門見貝車馬頭電話語體簡議證權觀實現習練寫買賣氣間從沒給還過進遠點爾漢龍鳳龜齊齡產嚴麗萬與豐務東條":
    print(ch, allstr.count(ch), end="; ")
print()
print("\n===== ja: check for full-width parens / Simplified quote residue =====")
ed=edition_texts("ja"); allstr="".join(s for v in ed.values() for s in v)
for ch in ["（","）","“","”","说","让","对","为"]:
    print(repr(ch), allstr.count(ch))
print("\n===== ko: Hanzi + full-width paren counts =====")
ed=edition_texts("ko"); allstr="".join(s for v in ed.values() for s in v)
hanzi=[c for c in allstr if '\u4e00'<=c<='\u9fff']
print("Hanzi total", len(hanzi), collections.Counter(hanzi).most_common(20))
print("full-width parens", allstr.count("（"), allstr.count("）"))
print("\n===== zh-cn: Traditional-only residue check =====")
ed=edition_texts("zh-cn"); allstr="".join(s for v in ed.values() for s in v)
for ch in "說讓讀對國為發廣長門見貝車馬頭電話語體簡議證權觀實現習練寫買賣氣間從沒給還過進遠點爾漢龍鳳龜齊齡產嚴麗萬與豐務東條繁體":
    c=allstr.count(ch)
    if c: print(ch, c, end="; ")
print()
