# -*- coding: utf-8 -*-
import re, html, json, hashlib, base64, os
from collections import Counter

BASE = "/home/hatch/workspace/goals/lucernaread-social-media-operations/files"
ED = BASE + "/weekly-report-w45-zh-tw-pt/svg"
CO = BASE + "/weekly-report-w45-zhtw-core/svg"
W43 = BASE + "/weekly-report-zh-tw-pt/svg"
OUT = "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-tw-pt-proof/work"

TEXT_RE = re.compile(r"<text[^>]*>(.*?)</text>", re.S)
TAG_RE = re.compile(r"<text([^>]*)>(.*?)</text>", re.S)

def texts(path):
    s = open(path, encoding="utf-8").read()
    return [html.unescape(re.sub(r"<[^>]+>", "", c)) for c in TEXT_RE.findall(s)]

def raw(path):
    return open(path, encoding="utf-8").read()

def alltexts(d):
    out = []
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".svg"):
            out += texts(os.path.join(d, fn))
    return out

# ---- P7 golden sentences ----
# P7 phrase strips: in P7 SVG, phrases are quoted with 「」 and followed by a
# page tag like 'p. 1'. Extract quoted sentences from edition P7 and core P7,
# count occurrences issue-wide (bare + bracketed forms) in each edition.
def quoted(s):
    return re.findall(r"「([^」]+)」", s)
for label, d in [("core", CO), ("edition", ED)]:
    p7 = texts(os.path.join(d, "p7-lang.svg"))
    qs = []
    for t in p7:
        qs += quoted(t)
    print(f"--- P7 quoted sentences {label}: {len(qs)}")
    all_t = " ".join(alltexts(d))
    for q in qs:
        bare = all_t.count(q)
        print(f"   count={bare} :: {q[:60]}")
    # page tags near phrases: print texts containing 'p. ' in P7
    tags = [t for t in p7 if re.search(r"p\.\s*\d", t)]
    print(f"   P7 page-tag texts {label}: {tags[:12]}")

# ---- Images: payload hashes + geometry + credits ----
IMG_RE = re.compile(r"<image([^>]*)>", re.S)
def images(path):
    s = raw(path)
    out = []
    for m in IMG_RE.finditer(s):
        attrs = m.group(1)
        href = re.search(r"(?:xlink:href|href)=\"([^\"]+)\"", attrs)
        x = re.search(r'\bx="([^"]+)"', attrs)
        y = re.search(r'\by="([^"]+)"', attrs)
        w = re.search(r'\bwidth="([^"]+)"', attrs)
        h = re.search(r'\bheight="([^"]+)"', attrs)
        data = href.group(1) if href else ""
        if data.startswith("data:"):
            payload = data.split(",", 1)[1]
            digest = hashlib.sha256(base64.b64decode(payload)).hexdigest()[:16]
        else:
            digest = "EXTERNAL:" + data[:60]
        out.append((x.group(1) if x else None, y.group(1) if y else None,
                    w.group(1) if w else None, h.group(1) if h else None, digest))
    return out
for fn in sorted(os.listdir(CO)):
    ci, ei = images(os.path.join(CO, fn)), images(os.path.join(ED, fn))
    print(f"images {fn}: core={ci} edition={ei} identical={ci == ei}")
# credits
for label, d in [("core", CO), ("edition", ED)]:
    for fn in ["p1-front.svg", "p2-life.svg", "p4-sport.svg", "p5-youth.svg"]:
        for t in texts(os.path.join(d, fn)):
            if "Photo:" in t:
                print(f"credit {label} {fn}: {t}")

# ---- Chart bars: rect widths on P4/P6 ----
RECT_RE = re.compile(r"<rect([^>]*)>", re.S)
def rects(path):
    s = raw(path)
    out = []
    for m in RECT_RE.finditer(s):
        a = m.group(1)
        def g(k):
            mm = re.search(r'\b' + k + r'="([^"]+)"', a)
            return mm.group(1) if mm else None
        out.append((g("x"), g("y"), g("width"), g("height"), g("fill")))
    return out
for label, d in [("core", CO), ("edition", ED)]:
    for fn in ["p4-sport.svg", "p6-deep.svg"]:
        rs = rects(os.path.join(d, fn))
        # chart bars: wide rects with brick/olive fills; print distinct widths of large rects
        big = sorted(set((r[2], r[4]) for r in rs if r[2] and float(r[2]) >= 100))
        print(f"bars {label} {fn}: {big}")

# ---- Furniture: badge element on P1s ----
def badge(path):
    s = raw(path)
    # find text elements containing badge-like strings
    for m in TAG_RE.finditer(s):
        attrs, inner = m.group(1), html.unescape(re.sub(r"<[^>]+>", "", m.group(2)))
        if "TEXTOS EM" in inner or "繁體中文正文" in inner or "繁體中文版" in inner and "VOL" in inner:
            print(f"  badge-candidate: attrs={attrs.strip()[:220]} :: {inner[:120]}")
    return
for label, path in [("core P1", CO + "/p1-front.svg"), ("W43pt P1", W43 + "/p1-front.svg"), ("edition P1", ED + "/p1-front.svg")]:
    print(f"--- badge {label}")
    badge(path)
# footers + page lines + separators + gloss prefix on all pages
for label, d in [("core", CO), ("edition", ED), ("W43pt", W43)]:
    print(f"--- furniture strings {label}")
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".svg"):
            continue
        for t in texts(os.path.join(d, fn)):
            if "Lucerna ·" in t or re.match(r"^Página \d+ de \d+$", t.strip()) or re.match(r"^第 \d+ 頁$", t.strip()) or re.match(r"^— Página \d+ —$", t.strip()) or re.match(r"^— 第 \d+ 頁 —$", t.strip()):
                print(f"   {fn}: {t}")

# ---- Residual Latin: bilingual nodes + English blacklist ----
EN_WORDS = ["work it out", "understand", "complete the", "read and answer", "true or false",
            "fill in", "match", "write", "example", "question", "answer", "please", "choose",
            "listen", "speak", "learn", "study", "festival", "weather", "travel", "school"]
# blacklist scan: whole-word English dictionary-ish list applied to all nodes,
# then adjudicate hits manually in output
BL = re.compile(r"\b(understood|understand|complete|questions|answers|example|exercise|festival|weather|travel|school|friend|family|morning|evening|yesterday|tomorrow|because|however|therefore|although|through|between|another|people|student|teacher|language|chinese|english|portuguese)\b", re.I)
for label, d in [("edition", ED)]:
    print(f"--- residual Latin {label}")
    for fn in sorted(os.listdir(d)):
        for t in texts(os.path.join(d, fn)):
            # bilingual node: contains CJK and ' · ' with Latin segment
            if "·" in t and re.search(r"[\u2e80-\u9fff]", t):
                lat = re.findall(r"·\s*([^·]+)", t)
                for seg in lat:
                    seg = seg.strip()
                    if re.search(r"[A-Za-z]", seg):
                        print(f"   BILING {fn}: {t[:130]}")
                        break
            for m in BL.finditer(t):
                print(f"   BL {fn}: {m.group(0)!r} :: {t[:120]}")

# ---- P6 gloss + content8 note in render ----
for t in texts(os.path.join(ED, "p6-deep.svg")):
    if "plus" in t.lower() or "Three" in t:
        print("P6 gloss node:", t[:200])
for t in texts(os.path.join(ED, "p8-test.svg")):
    if "138." in t or "IA dentro" in t:
        print("P8-138 node:", t[:160])
