# -*- coding: utf-8 -*-
"""Independent JA x RU W45 proof script #3: P8 keydiff, items, notes, gloss, P7 defs."""
import re, html, os, sys
sys.path.insert(0, "/home/hatch/workspace/goals/lucernaread-social-media-operations/tools")
import p8 as P8
BASE = "/home/hatch/workspace/goals/lucernaread-social-media-operations"
CO = BASE + "/files/weekly-report-w45-ja-core/svg/p8-tesuto.svg"
ED = BASE + "/files/weekly-report-w45-ja-ru/svg/p8-tesuto.svg"

ref, _ = P8.extract(CO, 150)
res, _ = P8.extract(ED, 150)
print("canonical extract how:", ref["_how"], res["_how"])
print("\n== KEYDIFF 21: core key vs RU key (method) ==")
for n in [1, 2, 5, 7, 8, 9, 29, 32, 65, 69, 78, 101, 113, 115, 117, 118, 137, 138, 140, 146, 147]:
    print(f"#{n} CORE key={ref[n]['key']!r} method={ref[n]['method']} | RU key={res[n]['key']!r} method={res[n]['method']}")
    print(f"     CORE seg={ref[n]['seg'][:120]!r}")
    print(f"     RU   seg={res[n]['seg'][:120]!r}")
print("\n== #139 (outside keydiff) ==")
for n in (139,):
    print(f"#{n} CORE key={ref[n]['key']!r} | RU key={res[n]['key']!r}")
    print(f"     CORE seg={ref[n]['seg'][:160]!r}")
    print(f"     RU   seg={res[n]['seg'][:160]!r}")
print("\n== #37 ==")
print("CORE:", ref[37], "\nRU:", res[37])

print("\n== ITEM RECONSTRUCTION (builder's p8_compare_items logic, re-implemented) ==")
def items(path):
    s = open(path, encoding="utf-8").read()
    ts = re.findall(r'<text[^>]*x="([\d.]+)"[^>]*y="([\d.]+)"[^>]*>([^<]*)</text>', s)
    out = {}; cur = None
    for x, y, t in ts:
        if float(y) <= 1328:
            continue
        if t.startswith("— ") and t.endswith(" —"):
            continue
        m = re.match(r"^(\d+)\.\s?(.*)$", t)
        if m:
            cur = int(m.group(1)); out[cur] = m.group(2)
        elif cur is not None:
            out[cur] += t
    return out
co_i, ed_i = items(CO), items(ED)
print(f"core items {len(co_i)} missing {[n for n in range(1,151) if n not in co_i]}")
print(f"ed items {len(ed_i)} missing {[n for n in range(1,151) if n not in ed_i]}")
ident = [n for n in range(1, 151) if co_i.get(n) == ed_i.get(n)]
print(f"identical full items ({len(ident)}): {ident}")
for n in ident:
    print(f"  IDENT #{n}: {co_i[n][:140]!r}")

print("\n== NOTE-TAIL equality (audit_geo 8b logic, re-implemented) ==")
def segs(path):
    s = open(path, encoding="utf-8").read()
    ts = [html.unescape(re.sub(r"<[^>]+>", "", c)) for c in re.findall(r"<text[^>]*>(.*?)</text>", s)]
    hdr = re.compile(r"^—\s*(.{0,24}?\d.{0,12}?)\s*—$")
    start = None
    for i, t in enumerate(ts):
        if hdr.match(t.strip()) and len(t.strip()) <= 34:
            start = i; break
    els = ts[start:-2]
    entries, cur = {}, None
    CJK2 = re.compile(r"[\u2e80-\u9fff\u3040-\u30ff\uac00-\ud7af\uff00-\uffef]")
    for t in els:
        if hdr.match(t.strip()):
            continue
        m = re.match(r"^\s*(\d{1,3})\.\s", t)
        if m:
            cur = int(m.group(1)); entries[cur] = t[m.end():]
        elif cur is not None:
            a, b = entries[cur], t
            entries[cur] = a + b if (CJK2.search(a[-1:]) or CJK2.search(b[:1])) else a + " " + b
    return {n: s.strip() for n, s in entries.items()}
co_s, ed_s = segs(CO), segs(ED)
def splitkey(seg):
    if " — " in seg:
        k, nn = seg.split(" — ", 1); return k.strip(), nn.strip()
    return seg.strip(), ""
leaks = []
for n in sorted(co_s):
    ck, cn = splitkey(co_s[n]); ek, en = splitkey(ed_s[n])
    if ck.startswith("✓") or ek.startswith("✓"):
        continue
    if cn == en and cn:
        leaks.append((n, cn))
print("identical note tails:", leaks if leaks else "NONE")
print("notes differing:", sum(1 for n in sorted(co_s) if splitkey(co_s[n])[1] != splitkey(ed_s[n])[1] and not splitkey(co_s[n])[0].startswith("✓")))

print("\n== GLOSS rendered per page: join prefix block, count '·' separators ==")
def gloss_blocks(path):
    s = open(path, encoding="utf-8").read()
    ts = []
    for m in re.finditer(r'<text([^>]*)>(.*?)</text>', s):
        ad = dict(re.findall(r'([\w-]+)="([^"]*)"', m.group(1)))
        ts.append((float(ad["x"]), float(ad["y"]), ad.get("font-size"), html.unescape(re.sub(r"<[^>]+>", "", m.group(2)))))
    return ts
for label, d, prefix in [("CORE", BASE + "/files/weekly-report-w45-ja-core/svg", None),
                         ("RU", BASE + "/files/weekly-report-w45-ja-ru/svg", "Пояснение")]:
    print("--", label)
    for pg in ["p1-hyoushi", "p2-kurashi", "p3-bunka", "p4-supotsu", "p5-wakamono", "p6-fukayomi"]:
        ts = gloss_blocks(os.path.join(d, pg + ".svg"))
        # RU: blocks start at prefix lines; continuation lines are the following text lines
        # until a line that starts a new section (heuristic: next line with x==65/93 and larger size
        # or a numbered exercise). Instead print all lines containing '·' after first prefix line region.
        if prefix:
            idxs = [i for i, t in enumerate(ts) if t[3].startswith(prefix)]
            blocks = []
            for k, i in enumerate(idxs):
                end = idxs[k + 1] if k + 1 < len(idxs) else len(ts)
                # continuation: lines after prefix line with same x and font-size, before next section:
                # gloss continuations are wrapped lines of the same paragraph: same x, same size.
                j = i + 1; parts = [ts[i][3]]
                while j < end:
                    x, y, fs, t = ts[j]
                    if x == ts[i][0] and fs == ts[i][2] and not re.match(r"^\d+\.", t):
                        parts.append(t); j += 1
                    else:
                        break
                blocks.append("".join(parts))
            tot = 0
            for b in blocks:
                # items = segments split by '·' after stripping prefix 'Пояснение — '
                body = b.split("— ", 1)[1] if "— " in b else b
                items_n = len(body.split("·"))
                tot += items_n
                print(f"   {pg} block items={items_n}: {b[:130]!r}")
            print(f"   {pg} TOTAL items={tot}")
        else:
            # core: print lines that look like gloss rows (contain ' · ' and a headword pattern)
            for x, y, fs, t in ts:
                if " · " in t and y > 1500:
                    print(f"   {pg} y={y} {t[:130]!r}")
