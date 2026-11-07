import re, json, hashlib, os
G = "/home/hatch/workspace/goals/lucernaread-social-media-operations"
ED = f"{G}/files/weekly-report-w45-zh-tw-es/svg"
CO = f"{G}/files/weekly-report-w45-zhtw-core/svg"
W43 = f"{G}/files/weekly-report-zh-tw-es/svg"
NAMES = ["p1-front","p2-life","p3-culture","p4-sport","p5-youth","p6-deep","p7-lang","p8-test"]

def texts(d, n):
    t = open(f"{d}/{n}.svg", encoding="utf-8").read()
    return re.findall(r"<text[^>]*>(.*?)</text>", t)

def cjkset(d, n=None):
    s = set()
    names = NAMES if n is None else [n]
    for nm in names:
        for tx in texts(d, nm):
            s |= {c for c in tx if "\u4e00" <= c <= "\u9fff"}
    return s

out = {}
# 1. pins
for f in ["Lucerna-VOL2-ES.pdf","Lucerna-VOL2-ES-web.pdf"]:
    p = f"{G}/files/weekly-report-w45-zh-tw-es/{f}"
    out[f] = {"bytes": os.path.getsize(p), "sha": hashlib.sha256(open(p,"rb").read()).hexdigest()}
for n in NAMES:
    p = f"{ED}/{n}.svg"
    out[f"svg-{n}"] = {"bytes": os.path.getsize(p), "sha": hashlib.sha256(open(p,"rb").read()).hexdigest()}

# 2. union gate
union = cjkset(W43) | cjkset(CO)
ed = cjkset(ED)
out["union"] = {"union": len(union), "edition": len(ed), "outside": sorted(ed - union)}
# simplified-only spot list over edition target text: check chars
spot = list("邮说国龙马发")
out["spot"] = {c: sum(1 for nm in NAMES for tx in texts(ED, nm) if c in tx) for c in spot}
# broader: simplified-only chars that are NOT in union? outside already covers. Also check
# simplified-only candidates present in edition text at all
simp_only = "邮说国龙马发国语话车门风云头发长发对台"
out["spot2"] = {c: sum(1 for nm in NAMES for tx in texts(ED, nm) if c in tx) for c in sorted(set(simp_only))}

# 3. P8 key lines fullwidth parens
p8 = texts(ED, "p8-test")
keylines = [t for t in p8 if re.match(r"^\d+\.", t.strip())]
out["p8_keylines"] = {"n": len(keylines), "fw_paren_lines": [t[:120] for t in keylines if "（" in t or "）" in t]}
out["p8_key138"] = [t for t in keylines if t.strip().startswith("138.")]
out["p8_key150"] = [t for t in keylines if t.strip().startswith("150.")]
# P6 AI note + P5 AI? search all pages
for nm in NAMES:
    for t in texts(ED, nm):
        if "La IA" in t or "AI helps" in t or "AI inside" in t:
            out.setdefault("ai_forms", []).append((nm, t[:200]))

# 4. badge: find P1 text nodes with TEXTOS / core badge
for d, lab in [(ED,"ed"),(CO,"core"),(W43,"w43")]:
    nodes = texts(d, "p1-front")
    out[f"badge_{lab}"] = [t for t in nodes if "TEXTOS" in t or "CHINO TRADICIONAL" in t or "繁體中文正文" in t or "Explanations in English" in t][:4]
# raw svg attrs for badge node: find <text ...>TEXTOS...
for d, lab in [(ED,"ed"),(CO,"core"),(W43,"w43")]:
    raw = open(f"{d}/p1-front.svg", encoding="utf-8").read()
    m = re.findall(r"<text[^>]*>([^<]*(?:TEXTOS|繁體中文正文)[^<]*)</text>", raw)
    out[f"badge_raw_{lab}"] = m
    # also get the full text tag for badge line
    m2 = re.findall(r"(<text[^>]*>[^<]*TEXTOS[^<]*</text>)", raw)
    out[f"badge_tag_{lab}"] = m2[:1]

# 5. footer + separators + gloss prefix
for d, lab in [(ED,"ed"),(CO,"core"),(W43,"w43")]:
    foots = set()
    for nm in NAMES:
        for t in texts(d, nm):
            if "Página" in t or "SEMANARIO" in t or "VOL." in t and "Lucerna" in t:
                foots.add(t)
    out[f"footer_{lab}"] = sorted(foots)[:6]
for nm in NAMES:
    for t in texts(ED, nm):
        if "Página" in t and "—" in t:
            out.setdefault("seps", []).append((nm, t))
    for t in texts(ED, nm):
        if t.startswith("Nota —"):
            out.setdefault("gloss_prefix_hits", []).append((nm, t[:80]))
# 6. residual english heads
for nm in NAMES:
    for t in texts(ED, nm):
        if "Work it out" in t or "Baseball words" in t:
            out.setdefault("english_heads_remaining", []).append((nm, t))
        if t.strip().startswith("Calcula") or "Palabras de béisbol" in t:
            out.setdefault("fixed_heads", []).append((nm, t[:120]))

# 7. readers corner: P7 nodes containing disclosure keywords
p7 = texts(ED, "p7-lang")
out["p7_disclosure_es"] = [t for t in p7 if "invitaci" in t or "publicable" in t or "ninguna" in t]
out["p7_disclosure_tw"] = [t for t in p7 if "延期披露" in t or "你的來信" in t]
p7c = texts(CO, "p7-lang")
out["p7_disclosure_tw_core"] = [t for t in p7c if "延期披露" in t or "你的來信" in t]
p7w = texts(W43, "p7-lang")
out["p7_disclosure_es_w43"] = [t for t in p7w if "invitaci" in t or "publicable" in t or "ninguna" in t or "ejemplo" in t]

# 8. P7 teaser end: need y coords - parse text elements with y attr near footer
for d, lab in [(ED,"ed")]:
    raw = open(f"{d}/p7-lang.svg", encoding="utf-8").read()
    els = re.findall(r'<text[^>]*y="([\d.]+)"[^>]*>([^<]*)</text>', raw)
    ys = [(float(y), t) for y, t in els if float(y) > 2400]
    out["p7_high_y"] = ys[-15:]

# 9. images: payload hashes per page (base64 hrefs)
def payloads(d, n):
    raw = open(f"{d}/{n}.svg", encoding="utf-8").read()
    return sorted(hashlib.sha256(b.encode()).hexdigest() for b in re.findall(r"data:image/[^;]+;base64,([A-Za-z0-9+/=]+)", raw))
for nm in NAMES:
    a, b = payloads(ED, nm), payloads(CO, nm)
    out[f"img_{nm}"] = {"ed": a, "core": b, "identical": a == b}
# credits
for nm in NAMES:
    for t in texts(ED, nm):
        if "Photo:" in t or "Wikimedia" in t:
            out.setdefault("credits", []).append((nm, t))

# 10. P7 golden sentences: read core P7? Golden sentences are in edition P7 strip; get P7 nodes
out["p7_all"] = p7
json.dump(out, open(f"{G}/hidden_files/w45/zh-tw-es-proof/work/analyze1.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps({k: v for k, v in out.items() if k != "p7_all"}, ensure_ascii=False, indent=1)[:6000])
print("P7 nodes:", len(p7))
