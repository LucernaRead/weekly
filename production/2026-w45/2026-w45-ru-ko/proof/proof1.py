#!/usr/bin/env python3
"""Independent RUxKO W45 proof script 1: freeze/Cyrillic/Han/P8-dashparse."""
import re, json, hashlib, collections, sys
from xml.etree import ElementTree as ET

BASE = "/home/hatch/workspace/goals/lucernaread-social-media-operations/files"
CORE = f"{BASE}/weekly-report-w45-ru-core/svg"
ED = f"{BASE}/weekly-report-w45-ru-ko/svg"
W43 = f"{BASE}/weekly-report-ru-ko/svg"
PAGES = ["p1-pervaya","p2-zhizn","p3-kultura","p4-sport","p5-molodezh","p6-razbor","p7-yazyk","p8-test"]

def texts(path):
    t = open(path, encoding="utf-8").read()
    # strip tags -> text nodes only (SVG <text> contents); use regex on text elements
    out = []
    for m in re.finditer(r"<text[^>]*>(.*?)</text>", t, re.S):
        s = re.sub(r"<[^>]+>", "", m.group(1))
        s = s.replace("&amp;","&").replace("&lt;","<").replace("&gt;",">").replace("&quot;",'"').replace("&apos;","'")
        out.append(s)
    return out, t

CYR = re.compile(r"[\u0400-\u04FF]+")
HAN = re.compile(r"[\u4E00-\u9FFF]")
HANG = re.compile(r"[\uAC00-\uD7A3\u1100-\u11FF\u3130-\u318F]")

print("== 1. Cyrillic token multiset per page (core vs edition) ==")
for p in PAGES:
    ct,_ = texts(f"{CORE}/{p}.svg"); et,_ = texts(f"{ED}/{p}.svg")
    cc = collections.Counter(tok for s in ct for tok in CYR.findall(s))
    ec = collections.Counter(tok for s in et for tok in CYR.findall(s))
    diff_c = cc - ec; diff_e = ec - cc
    print(f"{p}: core_tokens={sum(cc.values())} ed_tokens={sum(ec.values())} core-only={dict(diff_c)} ed-only={dict(diff_e)}")

print("\n== 1b. Han chars in edition rendered text per page ==")
for p in PAGES:
    et, raw = texts(f"{ED}/{p}.svg")
    joined = "".join(et)
    print(f"{p}: Han_in_text={len(HAN.findall(joined))} Hangul_in_text={len(HANG.findall(joined))} Han_in_raw_svg={len(HAN.findall(raw))}")

print("\n== 1c. freeze-diff removed strings without Han (must be only 8 separators) ==")
d = json.load(open("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/ru-ko-proof/freeze-diff.json"))
all_removed_no_han = []
for pg, v in d["pages"].items():
    for e in v["removed_strings"]:
        s = e["text"] if isinstance(e, dict) else e
        if not HAN.search(s):
            all_removed_no_han.append((pg, s))
print(f"removed-no-Han count={len(all_removed_no_han)}")
for pg, s in all_removed_no_han: print(f"  p{pg}: {s!r}")
print("cjk_added_total sum:", sum(d["cjk_added_total"].values()))
non_hangul_added = {ch: n for ch, n in d["cjk_added_total"].items() if not HANG.match(ch)}
print("added-CJK chars NOT Hangul:", non_hangul_added)

print("\n== 2. P8 dash-parse (key = before first ' — ') ==")
def p8_lines(path):
    ts, _ = texts(path)
    return ts
core_ts = p8_lines(f"{CORE}/p8-test.svg")
ed_ts = p8_lines(f"{ED}/p8-test.svg")
# P8 answer lines: lines starting with N. pattern
pat = re.compile(r"^(\d+)\.\s*(.*)$")
def keymap(ts):
    m = {}
    for s in ts:
        mm = pat.match(s.strip())
        if mm:
            num = int(mm.group(1)); rest = mm.group(2)
            if " — " in rest:
                key, note = rest.split(" — ", 1)
            else:
                key, note = rest, ""
            m[num] = (key, note)
    return m
ck, ek = keymap(core_ts), keymap(ed_ts)
print(f"core numbered lines={len(ck)} edition={len(ek)} missing={sorted(set(ck)-set(ek))} extra={sorted(set(ek)-set(ck))}")
keydiffs = [n for n in sorted(set(ck)&set(ek)) if ck[n][0] != ek[n][0]]
print("dash-parse keydiffs:", keydiffs)
for n in keydiffs:
    print(f"  {n}: core key={ck[n][0]!r} note={ck[n][1]!r}")
    print(f"      ed   key={ek[n][0]!r} note={ek[n][1]!r}")
for n in (83, 148, 139, 140):
    print(f"  check {n}: core={ck.get(n)} ed={ek.get(n)}")
# 150 writing apparatus: find line containing 84
for s in ed_ts:
    if "84" in s: print("  ed line w/84:", repr(s))
print("  core total numbered:", len(ck), "ed total:", len(ek))
# raw occurrences of '150.' lines
print("  ed 150 entry:", ek.get(150))
print("  core 150 entry:", ck.get(150))
