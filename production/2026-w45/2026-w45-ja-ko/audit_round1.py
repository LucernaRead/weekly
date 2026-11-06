# -*- coding: utf-8 -*-
"""JA x KO round-1 audit: P8 dual-path line comparison, gloss/phrase
counts, furniture geometry, image payloads, Han/punct inventories.
Run with the tools venv python (PIL for geometry helpers lives there,
though this script itself only parses SVG text)."""
import glob
import hashlib
import json
import os
import re
import sys

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE = os.path.join(BASE, "files/weekly-report-w45-ja-core/svg")
ED = os.path.join(BASE, "files/weekly-report-w45-ja-ko/svg")
BUILD = os.path.join(BASE, "hidden_files/weekly-report-w45-ja-ko-build")


def texts(path):
    src = open(path, encoding="utf-8").read()
    return [(float(m.group(1)), float(m.group(2)), m.group(3))
            for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)"[^>]*>([^<]*)</text>', src)]


def p8_items(path):
    """Answer-flow items: lines at y>=1328, grouped by leading 'N. '."""
    items = {}
    cur = None
    for x, y, t in texts(path):
        if y < 1328 or y >= 2580:
            continue
        s = t.strip()
        m = re.match(r"^(\d+)\.\s?(.*)$", s)
        if m and s.startswith(f"{m.group(1)}."):
            cur = int(m.group(1))
            items[cur] = m.group(2)
        elif cur is not None and s and not s.startswith("—"):
            items[cur] += s
    return items


def split_key_note(item):
    if " — " in item:
        k, n = item.split(" — ", 1)
        return k, n
    return item, ""


def norm(s):
    return re.sub(r"\s+", "", s)


print("=== P8 dual-path (wrapped-joined, whitespace-stripped) ===")
ci, ei = p8_items(os.path.join(CORE, "p8-tesuto.svg")), p8_items(os.path.join(ED, "p8-tesuto.svg"))
print("core items:", len(ci), "edition items:", len(ei),
      "missing:", sorted(set(ci) - set(ei)), "extra:", sorted(set(ei) - set(ci)))
identical, keydiff_true, prompt_loc = [], [], []
for n in sorted(ci):
    ck, cn = split_key_note(ci[n])
    ek, en = split_key_note(ei[n])
    if ci[n] == ei[n]:
        identical.append(n)
    if norm(ck) != norm(ek):
        keydiff_true.append((n, ck, ek))
    if n in (139, 140):
        prompt_loc.append((n, ck, ek, cn, en))
print("fully identical P8 lines (must be 0):", identical)
print("true key changes (expect 137, 138 only):")
for n, ck, ek in keydiff_true:
    print(f"  #{n}: core={ck!r} ed={ek!r}")
print("prompt-localization items 139/140 (keys must be identical):")
for n, ck, ek, cn, en in prompt_loc:
    print(f"  #{n}: key_equal={norm(ck)==norm(ek)} core_note={cn!r} ed_note={en!r}")
print("  #37 line:", ei.get(37))
print("  #150 line:", ei.get(150))

print("\n=== gloss counts (source gloss() strings, split on middle dot) ===")
for fname, pages in [("content12.py", [1, 2]), ("content34.py", [3, 4]), ("content56.py", [5, 6])]:
    for label, d in [("core", os.path.join(BASE, "hidden_files/weekly-report-w45-ja-build")),
                     ("ed", BUILD)]:
        src = open(os.path.join(d, fname), encoding="utf-8").read()
        gl = re.findall(r"\.gloss\((\"[^\"]*\")\)", src)
        counts = [len(s.strip('"').split("·")) for s in gl]
        print(f"  {fname} {label}: {len(gl)} gloss calls, items {counts} total {sum(counts)}")

print("\n=== P7 phrases (whitespace-stripped full-issue counts) ===")
full = ""
for f in sorted(glob.glob(os.path.join(ED, "*.svg"))):
    full += "".join(t for _, _, t in texts(f))
full_n = norm(full)
phrases = [
    "「文化の日は、11月3日（火よう日）です。」",
    "「ゆっくり、ゆるく整える日本の11月です。」",
    "「『ゆる』は、無理をしない、ゆっくり、という意味です。」",
    "「鍋の材料が1か月早く並び始めました。」",
    "「伝統工芸と紅葉と光を、いっしょに楽しむことができます。」",
    "「ソフトバンクが2連勝でスタートしました。」",
    "「ルールを守って、楽しいハロウィンにしましょう。」",
    "「紅葉を見に行く人は、北から南へ、見頃を追いかけることができます。」",
]
for p in phrases:
    bare = norm(p).replace(chr(0x300c), "").replace(chr(0x300d), "")
    print(f"  bare {bare[:20]}... x{full_n.count(bare)} (bracketed x{full_n.count(norm(p))})")
p7 = open(os.path.join(ED, "p7-kotoba.svg"), encoding="utf-8").read()
print("  P7 page tags in order:", re.findall(r"\(p\.\d\)", p7))

print("\n=== P1 furniture geometry (edition) ===")
p1 = open(os.path.join(ED, "p1-hyoushi.svg"), encoding="utf-8").read()
for m in re.finditer(r'<text ([^>]*)>([^<]*)</text>', p1):
    attrs, txt = m.group(1), m.group(2)
    if txt in ("Lucerna", "일본어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판") or \
            txt.startswith("日本語版 ·") or txt.startswith("日本語を学ぶ"):
        y = re.search(r'y="([^"]+)"', attrs).group(1)
        fs = re.search(r'font-size="([^"]+)"', attrs).group(1)
        fw = re.search(r'font-weight="([^"]+)"', attrs)
        fl = re.search(r'fill="([^"]+)"', attrs).group(1)
        print(f"  y={y} fs={fs} fw={fw.group(1) if fw else '-'} fill={fl} :: {txt[:60]}")
print("  dark band rect:", re.findall(r'<rect x="65" y="(\d+)" width="1820" height="118"', p1))
print("  rules:", sorted(set(re.findall(r'<line x1="65" y1="(\d+)" x2="1885"', p1)))[:6])
print("  footers:", sorted(set(re.findall(r">Lucerna · 일본어 주간지 VOL\.2[^<]*<", open(os.path.join(ED, "p1-hyoushi.svg"), encoding="utf-8").read()))))
for f in sorted(glob.glob(os.path.join(ED, "*.svg"))):
    s = open(f, encoding="utf-8").read()
    fo = re.findall(r'<text x="65" y="2624"[^>]*>([^<]*)</text>', s)
    pg = re.findall(r'<text x="1885" y="2624"[^>]*>([^<]*)</text>', s)
    print(f"  {os.path.basename(f)} footer={fo} page={pg}")
p8s = open(os.path.join(ED, "p8-tesuto.svg"), encoding="utf-8").read()
print("  P8 separators:", sorted(set(re.findall(r"— 제 \d 면 —", p8s))))
print("  gloss boxes (lines starting with prefix):", sum(1 for f in glob.glob(os.path.join(ED, "*.svg")) for _, _, t in texts(f) if t.startswith("해설 — ")))

print("\n=== image payloads (sha256 of base64 href per page) ===")
for f in sorted(glob.glob(os.path.join(ED, "*.svg"))):
    name = os.path.basename(f)
    ce = re.findall(r'href="data:image/[^;]+;base64,([^"]+)"', open(f, encoding="utf-8").read())
    cc = re.findall(r'href="data:image/[^;]+;base64,([^"]+)"', open(os.path.join(CORE, name), encoding="utf-8").read())
    print(f"  {name}: ed={len(ce)} core={len(cc)} payload_equal={[hashlib.sha256(a.encode()).hexdigest()[:12] == hashlib.sha256(b.encode()).hexdigest()[:12] for a, b in zip(ce, cc)]}")

print("\n=== Han / punct inventories (edition vs core, all pages) ===")
HAN = re.compile(r"[\u4e00-\u9fff]")
for label, d in [("core", CORE), ("ed", ED)]:
    alltxt = "".join(open(f, encoding="utf-8").read() for f in sorted(glob.glob(os.path.join(d, "*.svg"))))
    txts = "".join(t for f in sorted(glob.glob(os.path.join(d, "*.svg"))) for _, _, t in texts(f))
    print(f"  {label}: Han chars in text={len(HAN.findall(txts))} "
          f"fullwidth 。={txts.count(chr(0x3002))} （）={txts.count(chr(0xff08))+txts.count(chr(0xff09))} "
          f"｜={txts.count(chr(0xff5c))} half-paren()={txts.count('(')+txts.count(')')}")
ct = "".join(t for f in sorted(glob.glob(os.path.join(CORE, "*.svg"))) for _, _, t in texts(f))
et = "".join(t for f in sorted(glob.glob(os.path.join(ED, "*.svg"))) for _, _, t in texts(f))
print("  Han chars in edition text but not in core text charset:", sorted(set(HAN.findall(et)) - set(HAN.findall(ct))))
print("  Han chars in core text but not edition (removed apparatus):", sorted(set(HAN.findall(ct)) - set(HAN.findall(et)))[:60])

print("\n=== Han-bearing edition strings absent from core (adjudicate) ===")
core_strs = set(t.strip() for f in sorted(glob.glob(os.path.join(CORE, "*.svg"))) for _, _, t in texts(f))
for f in sorted(glob.glob(os.path.join(ED, "*.svg"))):
    for _, _, t in texts(f):
        s = t.strip()
        if s and HAN.search(s) and s not in core_strs:
            print(f"  {os.path.basename(f)} :: {s[:90]}")

print("\n=== max content y per page (excluding footer y=2624/line 2580) ===")
for f in sorted(glob.glob(os.path.join(ED, "*.svg"))):
    ys = [y for _, y, _ in texts(f) if y < 2580]
    print(f"  {os.path.basename(f)}: max_text_y={max(ys)}")
