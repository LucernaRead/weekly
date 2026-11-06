# -*- coding: utf-8 -*-
"""Generate tr-zh-tw.py: convert the core (SC) strings from en-pairs.json
to TC with opencc s2t, keyed by the EN string. Manual overrides for the
badge line and the MUSTER label (W45 ZH-TW used 範本, not 範文)."""
import json, io, sys
sys.path.insert(0, "/home/hatch/workspace/goals/lucernaread-social-media-operations/tools/venv/lib/python3.12/site-packages")
from opencc import OpenCC

G = "/home/hatch/workspace/goals/lucernaread-social-media-operations"
cc = OpenCC("s2t")
pairs = json.load(open(f"{G}/hidden_files/w46/en-pairs.json", encoding="utf-8"))
# pairs: list of [old, new]; old = core SC string, new = EN string.
TR = {}
conflicts = []
for _lst, old, new in pairs:
    conv = cc.convert(old)
    if new in TR and TR[new] != conv:
        conflicts.append((new, TR[new], conv))
    TR[new] = conv
print("pairs:", len(pairs), "distinct EN keys:", len(TR), "conflicts:", len(conflicts))
for c in conflicts:
    print("CONFLICT:", c)

EN_BADGE = 'p.text(975, 372, "TEXT IN GERMAN · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS", 20, "sans", True, OLIVE, anchor="middle")'
TR[EN_BADGE] = 'p.text(975, 372, "德語正文 · 繁體中文講解 — 給繁體中文讀者的版本", 19.5, "sans", True, BRICK, anchor="middle")'
TR["MUSTER · Model text (84 words)"] = "MUSTER · 範本（84 Wörter）"

out = io.StringIO()
out.write("# -*- coding: utf-8 -*-\n\"\"\"ZH-TW translations: core SC strings converted to TC (opencc s2t),\nkeyed by the EN new-string. Badge + MUSTER hand-overridden (W45 forms).\"\"\"\nTR = {\n")
for k in sorted(TR, key=lambda s: s):
    out.write(f"{k!r}: {TR[k]!r},\n")
out.write("}\n\n")
out.write('''CFG = {
    "footer": '"Die Lucerna · 德語週報 VOL.3 · 正文德語 · 講解繁體中文"',
    "pageline": 'f"第 {n} 版 / 共 {total} 版"',
    "gloss_prefix": '"譯注｜" + s',
    "separator": "— 第 {pg} 版 —",
    "bracket": " ({e['note']})",
    "keys_size": (14.5, 1.3),
    "cjk_scan": False,
    "typemap": [("完成句子", "完成句子"), ("单选", "單選"),
                ("句型转换", "句型轉換"), ("词汇配对", "詞彙配對"),
                ("判断对错", "判斷對錯"), ("完形填空", "完形填空"),
                ("造句", "造句"), ("对话补全", "對話補全"),
                ("翻译", "翻譯"), ("写作", "寫作")],
    "instrmap": [('instr="填空"', 'instr="填空"'),
                 ('instr="改写"', 'instr="改寫"'),
                 ('instr="判断"', 'instr="判斷"'),
                 ('instr="造句"', 'instr="造句"'),
                 ('instr="翻译"', 'instr="翻譯"'),
                 ('instr="把词和释义配对"', 'instr="把詞和釋義配對"')],
}
''')
open(f"{G}/hidden_files/w46/tr-zh-tw.py", "w", encoding="utf-8").write(out.getvalue())
print("wrote tr-zh-tw.py")
# Watchlist: SC-only chars that must not survive, and context-sensitive TC chars to eyeball.
SC_WATCH = set("说读让练讲简这样还过这个为与头对应会来时间长门问题电话语学国家发后只干着里")
for k, v in TR.items():
    bad = [ch for ch in v if ch in SC_WATCH]
    if bad:
        print("SC-LEAK?", repr(k), "->", repr(v), "chars:", bad)
CTX = set("後發髮乾幹隻裏")
for k, v in TR.items():
    hit = [ch for ch in v if ch in CTX]
    if hit:
        print("CTX-CHECK:", repr(v))
