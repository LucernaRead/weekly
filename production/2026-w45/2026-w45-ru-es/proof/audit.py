# -*- coding: utf-8 -*-
"""Independent RUxES W45 proofread audit (proofreader's own script, not builder's).
Reads ONLY shipped files + build code for gloss counts; writes nothing outside proof dir."""
import os, re, sys, hashlib, json
from collections import Counter
from xml.etree import ElementTree as ET

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE = BASE + "/files/weekly-report-w45-ru-core/svg"
ED = BASE + "/files/weekly-report-w45-ru-es/svg"
W43 = BASE + "/files/weekly-report-ru-es/svg"
COREB = BASE + "/hidden_files/weekly-report-w45-ru-build"
EDB = BASE + "/hidden_files/weekly-report-w45-ru-es-build"
PAGES = ["p1-pervaya", "p2-zhizn", "p3-kultura", "p4-sport",
         "p5-molodezh", "p6-razbor", "p7-yazyk", "p8-test"]
NS = "{http://www.w3.org/2000/svg}"
CYR = re.compile(r"[А-Яа-яЁё]+")
CJK = re.compile(r"[\u4e00-\u9fff\u3400-\u4dbf\uf900-\ufaff]")

def texts(path):
    root = ET.parse(path).getroot()
    out = []
    for el in root.iter():
        if el.tag.replace(NS, "") == "text":
            out.append({"t": "".join(el.itertext()), "x": el.get("x"),
                        "y": el.get("y"), "fs": el.get("font-size"),
                        "fill": el.get("fill"), "fw": el.get("font-weight"),
                        "anchor": el.get("text-anchor")})
    return out

def elements(path, tag):
    root = ET.parse(path).getroot()
    return [el for el in root.iter() if el.tag.replace(NS, "") == tag]

print("== 2a Cyrillic token multiset per page (core vs edition) ==")
cyr_ok = True
for p in PAGES:
    ct, et = Counter(), Counter()
    for d in texts(f"{CORE}/{p}.svg"): ct.update(CYR.findall(d["t"]))
    for d in texts(f"{ED}/{p}.svg"): et.update(CYR.findall(d["t"]))
    diff_c, diff_e = dict(ct - et), dict(et - ct)
    ok = not diff_c and not diff_e
    cyr_ok &= ok
    print(f"{p}: core={sum(ct.values())} ed={sum(et.values())} equal={ok} "
          f"core-only={diff_c} ed-only={diff_e}")
print("CYRILLIC ALL EQUAL:", cyr_ok)

print("\n== 2b CJK accounting ==")
for p in PAGES:
    cc = sum(len(CJK.findall(d["t"])) for d in texts(f"{CORE}/{p}.svg"))
    ec = sum(len(CJK.findall(d["t"])) for d in texts(f"{ED}/{p}.svg"))
    print(f"{p}: core CJK chars={cc} edition CJK chars={ec}")
ed_cjk_total = sum(len(CJK.findall(d["t"])) for p in PAGES for d in texts(f"{ED}/{p}.svg"))
print("EDITION TOTAL CJK:", ed_cjk_total)

print("\n== 3 P8 independent dash-parse (join wrapped continuations) ==")
def p8_answers(path):
    """fs 13.0 answer texts in doc order; numbered item starts new answer,
    following non-numbered, non-separator texts are continuations (joined with space)."""
    ans = {}
    cur = None
    for d in texts(path):
        if d["fs"] != "13.0":
            continue
        t = d["t"]
        m = re.match(r"^(\d+)\.\s*(.*)$", t)
        if m:
            cur = int(m.group(1))
            ans[cur] = m.group(2)
        elif t.startswith("— ") and t.endswith(" —"):
            cur = None  # page separator
        elif cur is not None:
            ans[cur] += " " + t
    return ans

core_a, ed_a = p8_answers(f"{CORE}/p8-test.svg"), p8_answers(f"{ED}/p8-test.svg")
print(f"core answers={len(core_a)} edition answers={len(ed_a)} "
      f"missing={sorted(set(core_a)-set(ed_a))} extra={sorted(set(ed_a)-set(core_a))}")
def dash_key(s):
    return s.split(" — ", 1)[0] if " — " in s else None
keydiff = []
for n in sorted(set(core_a) & set(ed_a)):
    ck, ek = dash_key(core_a[n]), dash_key(ed_a[n])
    if ck is not None and ek is not None and ck != ek:
        keydiff.append(n)
print("dash-parse keydiff (keys differing where both have dash form):", keydiff)
for n in [83, 137, 138, 139, 140, 148, 150]:
    print(f"  {n} CORE: {core_a.get(n)!r}")
    print(f"  {n} ED  : {ed_a.get(n)!r}")
    if n in (139, 140):
        print(f"     139/140 key byte-identical: {dash_key(core_a[n]) == dash_key(ed_a[n])}")
    if n in (83, 148):
        print(f"     printed key identical: {dash_key(core_a[n]) == dash_key(ed_a[n])}")
# P8 answer flow end: max y among fs13.0 answer texts (excluding separators fs13.3)
for label, path in [("CORE", f"{CORE}/p8-test.svg"), ("ED", f"{ED}/p8-test.svg")]:
    ys = [float(d["y"]) for d in texts(path) if d["fs"] == "13.0"]
    print(f"P8 {label} max answer-text y = {max(ys):.2f} (rule at 2580)")

print("\n== 3b P8 model text (section H) word count, edition ==")
for label, path in [("CORE", f"{CORE}/p8-test.svg"), ("ED", f"{ED}/p8-test.svg")]:
    ts = texts(path)
    # model text: Russian paragraph(s) in section H; locate by heading H proximity:
    # print all texts with y > 2400 on p8 for inspection
    print(f"-- {label} p8 texts y>2400 --")
    for d in ts:
        if d["y"] and float(d["y"]) > 2400:
            print("   ", repr(d["t"][:150]), "y=", d["y"], "fs=", d["fs"])

print("\n== 5a gloss counts (split on U+00B7 itself, build code) ==")
for label, bdir in [("CORE", COREB), ("ED", EDB)]:
    total_calls, total_items, per = 0, 0, {}
    for f in ["content12.py", "content34.py", "content56.py"]:
        src = open(f"{bdir}/{f}", encoding="utf-8").read()
        counts = []
        for m in re.finditer(r"gloss\((.*?)\)\s*$", src, re.M):
            arg = m.group(1)
            # arg is a quoted string literal; eval safely via ast
            import ast
            try:
                s = ast.literal_eval(arg)
            except Exception:
                s = arg
            counts.append(len([x for x in s.split("·") if x.strip() != ""]))
        per[f] = counts
        total_calls += len(counts); total_items += sum(counts)
    print(f"{label}: calls={total_calls} items={total_items} per-file={per}")

print("\n== 5b image payloads byte-identical (per page) ==")
for p in PAGES:
    def imgs(path):
        out = []
        for el in elements(path, "image"):
            href = el.get("{http://www.w3.org/1999/xlink}href") or el.get("href") or ""
            out.append((el.get("x"), el.get("y"), el.get("width"), el.get("height"),
                        hashlib.sha256(href.encode("utf-8")).hexdigest()[:16] if href.startswith("data:") else href,
                        len(href)))
        return out
    ci, ei = imgs(f"{CORE}/{p}.svg"), imgs(f"{ED}/{p}.svg")
    print(f"{p}: core images={len(ci)} edition images={len(ei)} payload-identical={ci == ei}")
    if ci != ei:
        print("   core:", ci); print("   ed  :", ei)

print("\n== 5c P7 golden sentences: 8 P7 quotes, count across whole issue ==")
gold = []
for d in texts(f"{ED}/p7-yazyk.svg"):
    if d["y"] in ("1857", "2002", "2147", "2292") and d["t"].startswith("«"):
        gold.append(d["t"])
print(f"golden sentences found on ED P7: {len(gold)}")
for g in gold:
    print("  ", repr(g))
for label, svgdir in [("CORE", CORE), ("ED", ED)]:
    joined = []
    for p in PAGES:
        page_text = " ".join(d["t"] for d in texts(f"{svgdir}/{p}.svg"))
        joined.append(page_text)
    whole = " ".join(joined)
    whole_norm = re.sub(r"\s+", " ", whole)
    counts = [whole_norm.count(re.sub(r"\s+", " ", g)) for g in gold]
    print(f"{label} occurrence counts (whitespace-normalised whole-issue): {counts} all==2: {all(c == 2 for c in counts)}")
    # also raw (no normalisation) for reference
    print(f"   raw counts: {[whole.count(g) for g in gold]}")

print("\n== 6/7 badge + P7 geometry (raw element dump, see separate badge script) ==")
print("deferred to badge.py for PIL ink measurement")
