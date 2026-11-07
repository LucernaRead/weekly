#!/usr/bin/env python3
# Independent W45 ESxRU proof: re-measure rendered SVGs only.
import re, html, json, hashlib, glob, os
from collections import Counter
B = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = f"{B}/files/weekly-report-w45-es-ru/svg"
CO = f"{B}/files/weekly-report-w45-es-core/svg"
W43 = f"{B}/files/weekly-report-es-ru/svg"
OUT = f"{B}/hidden_files/w45/es-ru-proof"
TEXT_RE = re.compile(r"<text[^>]*>(.*?)</text>", re.S)
ATTR_RE = re.compile(r'<text([^>]*)>(.*?)</text>', re.S)

def texts(path):
    s = open(path, encoding="utf-8").read()
    return [html.unescape(re.sub(r"<[^>]+>", "", c)) for c in TEXT_RE.findall(s)]
def raw(path):
    return open(path, encoding="utf-8").read()
def elems(path):
    s = raw(path)
    out = []
    for m in ATTR_RE.finditer(s):
        a = dict(re.findall(r'([\w-]+)="([^"]*)"', m.group(1)))
        out.append((a, html.unescape(re.sub(r"<[^>]+>", "", m.group(2)))))
    return out

pages = ["p1-portada","p2-vida","p3-cultura","p4-deporte","p5-juventud","p6-afondo","p7-lengua","p8-ejercicios"]

# --- 1. Latin token multiset diff (Latin-1 letters + digits sequences; Cyrillic/CJK excluded by charset)
LAT = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9]+(?:[.,][0-9]+)?")
def latin_counter(ts):
    c = Counter()
    for t in ts:
        for tok in LAT.findall(t):
            # skip tokens that are part of a Cyrillic-mixed string? LAT charset already excludes Cyrillic chars;
            # but a token like '9' inside Russian text counts -- same as builder method (they reported 9 x2).
            c[tok] += 1
    return c
tokdiff = {}
for p in pages:
    cc, ec = latin_counter(texts(f"{CO}/{p}.svg")), latin_counter(texts(f"{ED}/{p}.svg"))
    removed = {k: cc[k]-ec[k] for k in cc if cc[k] > ec[k]}
    added = {k: ec[k]-cc[k] for k in ec if ec[k] > cc[k]}
    tokdiff[p] = {"removed": removed, "added": added}
json.dump(tokdiff, open(f"{OUT}/token-diff.json","w"), ensure_ascii=False, indent=1)
for p in pages:
    print(p, "REMOVED:", tokdiff[p]["removed"])
    print(p, "ADDED:", tokdiff[p]["added"])

# --- Página 4 frozen ref
for label, d in [("CORE", CO), ("ED", ED)]:
    ts = texts(f"{d}/p1-portada.svg")
    hits = [t for t in ts if "Página" in t or "Páginas" in t]
    print(label, "P1 Página-bearing texts:", hits)
print("ED raw count '(Página 4)':", raw(f"{ED}/p1-portada.svg").count("(Página 4)"),
      "CORE:", raw(f"{CO}/p1-portada.svg").count("(Página 4)"))
print("ED raw count 'Страница 4':", raw(f"{ED}/p1-portada.svg").count("Страница 4"))

# --- P8 dash parse (independent of p8.py): join wrapped answer lines
def p8_keys(path):
    ts = texts(path)
    # find first separator header '— СТРАНИЦА 1 —' / core '— PÁGINA 1 —'
    start = None
    for i, t in enumerate(ts):
        if re.match(r"^—\s*(?:PÁGINA|СТРАНИЦА)\s+1\s*—$", t.strip()):
            start = i; break
    assert start is not None, "no P8 start"
    seg = ts[start:-2]  # drop 2 footer lines (same convention as p8.py)
    # rebuild stream: headers become separators; numbered items start with 'N. '
    stream = []
    for t in seg:
        if re.match(r"^—\s*(?:PÁGINA|СТРАНИЦА)\s+\d+\s*—$", t.strip()):
            stream.append("\n@@SEP@@\n")
        else:
            stream.append(t)
    blob = " ".join(stream)
    parts = re.split(r"(?=\b\d{1,3}\.\s)", blob)
    keys = {}
    for part in parts:
        m = re.match(r"(\d{1,3})\.\s(.*)", part.strip(), re.S)
        if not m: continue
        n, body = int(m.group(1)), re.sub(r"\s+", " ", m.group(2)).strip()
        # strip trailing separator marker
        body = body.replace("@@SEP@@", "").strip()
        if " — " in body:
            key = body.split(" — ", 1)[0].strip()
        elif body.startswith("✓"):
            key = "✓"
        else:
            key = body
        keys[n] = body  # full body for comparison; key computed separately below
    return keys
ck, ek = p8_keys(f"{CO}/p8-ejercicios.svg"), p8_keys(f"{ED}/p8-ejercicios.svg")
print("P8 counts:", len(ck), len(ek), "numbers continuous:", sorted(ck)==list(range(1,151)), sorted(ek)==list(range(1,151)))
def dashkey(body):
    body = body.strip()
    if body.startswith("✓"): return "✓"
    if " — " in body: return body.split(" — ", 1)[0].strip()
    return body
kd = {}
for n in range(1, 151):
    if dashkey(ck[n]) != dashkey(ek[n]):
        kd[n] = (dashkey(ck[n]), dashkey(ek[n]))
print("P8 dash-key diffs:", json.dumps(kd, ensure_ascii=False, indent=1))
# full-body equality per number (note changes show here)
fulldiff = [n for n in range(1,151) if ck[n] != ek[n]]
print("P8 full-body diffs count:", len(fulldiff), fulldiff)
json.dump({"dashkey_diffs": kd, "fullbody_diffs": fulldiff,
           "core": ck, "ed": ek}, open(f"{OUT}/p8-dash.json","w"), ensure_ascii=False, indent=1)
# 139/140 keys byte-equal? 150 form?
for n in (139, 140, 150, 137, 138):
    print(f"  #{n} CORE key={dashkey(ck[n])!r} ED key={dashkey(ek[n])!r} ED full={ek[n]!r}")

# --- Gloss counts: strings containing 'Пояснение — ' / core '说明' prefix? Use rendered gloss boxes:
# Gloss items live in text elements whose content contains '·' separators in the gloss boxes.
# Robust: find all text elements; gloss box texts are those following a 'Пояснение' prefix element?
# Instead: count by the builder's stated method -- split the RENDERED gloss string on '·'.
# Identify gloss strings: in ED, texts starting with 'Пояснение —'; in CO, the gloss strings are the
# Chinese-annotated strings. Simplest verifiable proxy: count '·' separators inside gloss-box elements.
# Gloss boxes are <text> elements with the gloss prefix; their full string is one element per box in SVG?
for label, d, prefix in [("CORE", CO, None), ("ED", ED, "Пояснение")]:
    print(f"--- gloss {label} ---")
    for p in pages[:5]:
        els = elems(f"{d}/{p}.svg")
        if prefix:
            g = [t for a, t in els if t.strip().startswith(prefix)]
            print(p, "prefix texts:", len(g), "items by · split:", [len(t.split("·")) for t in g], "total items:", sum(len(t.split("·")) for t in g))
            for t in g: print("   ", repr(t[:160]))
        else:
            # core: gloss strings contain CJK + '·'? print texts containing '·' with CJK
            g = [t for a, t in els if "·" in t and re.search(r"[\u4e00-\u9fff]", t)]
            print(p, "CJK+· texts:", len(g), "items:", sum(len(t.split("·")) for t in g))
            for t in g: print("   ", repr(t[:160]))

# --- Images: data-URI payload hashes
def img_hashes(path):
    s = raw(path)
    out = []
    for m in re.finditer(r'<image[^>]*xlink:href="data:([^;]+);base64,([^"]+)"', s):
        out.append((m.group(1), hashlib.sha256(m.group(2).encode()).hexdigest()[:16], len(m.group(2))))
    return out
for p in pages:
    ci, ei = img_hashes(f"{CO}/{p}.svg"), img_hashes(f"{ED}/{p}.svg")
    print(p, "images core==ed:", ci == ei, ci, ei)

# --- P7 quotes x2 + page labels
for label, d, labpat in [("CORE", CO, r"\(Página (\d)\)"), ("ED", ED, r"\(Страница (\d)\)")]:
    ts = texts(f"{d}/p7-lengua.svg")
    labs = Counter()
    for t in ts:
        for m in re.finditer(labpat, t): labs[int(m.group(1))] += 1
    print(label, "P7 labels:", dict(sorted(labs.items())))
    # quote sentences: take core P7 article sentences? Instead count each ED P7 text element that also appears in another page
    # Simpler: builder claim is 8 sentences x2 across all 8 SVGs. Check via core: sentences in P7 that appear on other pages.
# quote check: for each text element on ED p7 that is a long Spanish sentence, count occurrences across all ED SVGs
all_ed = {p: texts(f"{ED}/{p}.svg") for p in pages}
# Spanish quote sentences are the 8 long sentences in the P7 FRASES table: identify by length>60 and Latin-only-ish
from collections import Counter as C2
cnt = C2()
for p in pages:
    for t in all_ed[p]:
        cnt[t] += 1
# candidate quotes: texts appearing exactly twice, long, Spanish, on p7 + one other page
cands = [(t, c) for t, c in cnt.items() if c == 2 and len(t) > 60 and re.search(r"[A-Za-zÀ-ÿ]", t) and not re.search(r"[\u0400-\u04ff\u4e00-\u9fff]", t)]
print("P7-candidate x2 long Spanish texts:", len(cands))
for t, c in sorted(cands): print("  ", repr(t[:120]))
# also check the split-label defect: any text element '(Страница' without closing, or '5)' orphan
for p in pages:
    for a, t in elems(f"{ED}/{p}.svg"):
        if "Страница" in t and not re.search(r"\(Страница \d\)", t):
            print("  SPLIT-LABEL SUSPECT", p, repr(t))
# P7 quote5 gloss single line? find gloss containing 'американский футбол'
for a, t in elems(f"{ED}/p7-lengua.svg"):
    if "американский футбол" in t: print("  P7 football gloss:", repr(t), "attrs:", a)

# --- Exercise counts & levels per page
for label, d in [("CORE", CO), ("ED", ED)]:
    print(f"--- levels {label} ---")
    tot = Counter()
    for p in pages:
        els = elems(f"{d}/{p}.svg")
        lv = Counter(t.strip() for a, t in els if t.strip() in ("A2", "B1", "B2"))
        tot.update(lv)
        print(" ", p, dict(lv), "sum", sum(lv.values()))
    print("  TOTAL", dict(tot), sum(tot.values()))

# --- P7 reader section: dump all P7 texts containing reader-section markers
print("--- P7 reader section (ED) ---")
for a, t in elems(f"{ED}/p7-lengua.svg"):
    if any(k in t for k in ["Ana", "Примечание редакции", "писем", "VOL.3", "пример", "читател"]):
        print("  ", repr(t))
print("--- P7 reader section (CORE, for contrast) ---")
for a, t in elems(f"{CO}/p7-lengua.svg"):
    if any(k in t for k in ["Ana", "编者", "来信", "VOL.3", "示例", "读者"]):
        print("  ", repr(t))
# invitation hunt across ALL ED pages: any imperative invitation to send letters?
print("--- invitation hunt ED (all pages) ---")
for p in pages:
    for a, t in elems(f"{ED}/{p}.svg"):
        if re.search(r"присылай|напишите нам|отправьте|жд[её]м ваших|приглашаем|делитесь|расскажите нам", t, re.I):
            print("  ", p, repr(t))
# also dump full P7 text list for manual reader-section read
json.dump({p: texts(f"{ED}/{p}.svg") for p in pages}, open(f"{OUT}/ed-texts.json","w"), ensure_ascii=False, indent=1)

# --- CJK / orphan / forbidden scans on delivered SVGs
CJK = re.compile(r"[\u2e80-\u9fff\u3040-\u30ff\U0000ac00-\U0000d7af\uff00-\uffef]")
for p in pages:
    s = raw(f"{ED}/{p}.svg")
    chars = CJK.findall(s)
    print(p, "CJK chars:", CJK and Counter(chars))
    print("   forbidden term count:", s.count("桥接"))
    # orphan line starts: each <text> element content start
    orph = [t for t in texts(f"{ED}/{p}.svg") if t and t[0] in ".,;:!?%)»”"]
    print("   orphan-start texts:", orph)
# PDF text scan for forbidden term + CJK presence (via pdftotext if available)
print("--- build-tree non-rendered CJK check ---")
for f in ["content7.py", "svglib.py"]:
    path = f"{B}/hidden_files/weekly-report-w45-es-ru-build/{f}"
    s = open(path, encoding="utf-8").read()
    print(f, "CJK chars:", Counter(CJK.findall(s)))
    for i, line in enumerate(s.splitlines(), 1):
        if CJK.search(line): print(f"   line {i}: {line.strip()[:120]}")
for f in sorted(glob.glob(f"{B}/hidden_files/w45-es-ru-transform.py")):
    s = open(f, encoding="utf-8").read()
    print(f, "forbidden-term count:", s.count("桥接"))

# --- Furniture triple: ED vs W43
def find_texts(d, p, needle):
    return [(a, t) for a, t in elems(f"{d}/{p}.svg") if needle in t]
print("--- furniture ED vs W43 ---")
checks = [
    ("badge P1", "p1-portada", "ТЕКСТЫ НА ИСПАНСКОМ"),
    ("footer", "p1-portada", "ИСПАНСКИЙ ЕЖЕНЕДЕЛЬНИК"),
    ("top band", "p1-portada", "CADA SEMANA EN ESPAÑOL"),
    ("masthead line", "p1-portada", "ИСПАНСКИЙ ЕЖЕНЕДЕЛЬНИК · VOL"),
    ("gloss prefix P2", "p2-vida", "Пояснение"),
    ("P8 sep", "p8-ejercicios", "СТРАНИЦА"),
    ("section VIDA", "p2-vida", "VIDA"),
    ("section CULTURA", "p3-cultura", "CULTURA"),
    ("section DEPORTE", "p4-deporte", "DEPORTE"),
    ("section JUVENTUD", "p5-juventud", "JUVENTUD"),
    ("section A FONDO", "p6-afondo", "A FONDO"),
    ("section LENGUA", "p7-lengua", "LENGUA"),
    ("section EJERCICIOS", "p8-ejercicios", "EJERCICIOS"),
]
for name, p, needle in checks:
    e = [(a, t) for a, t in elems(f"{ED}/{p}.svg") if needle in t]
    w = [(a, t) for a, t in elems(f"{W43}/{p}.svg") if needle in t]
    print(f"{name}: ED={[(a.get('x'),a.get('y'),a.get('font-size'),a.get('font-weight'),t) for a,t in e]}")
    print(f"   W43={[(a.get('x'),a.get('y'),a.get('font-size'),a.get('font-weight'),t) for a,t in w]}")
# footers all pages
for p in pages:
    ef = [t for a, t in elems(f"{ED}/{p}.svg") if "ИСПАНСКИЙ ЕЖЕНЕДЕЛЬНИК" in t or "Страница" in t and "из 8" in t]
    wf = [t for a, t in elems(f"{W43}/{p}.svg") if "ИСПАНСКИЙ ЕЖЕНЕДЕЛЬНИК" in t or "Страница" in t and "из 8" in t]
    print(p, "ED footer-ish:", ef, "| W43:", wf)
# badge geometry ED vs W43
for label, d in [("ED", ED), ("W43", W43)]:
    for a, t in elems(f"{d}/p1-portada.svg"):
        if "ТЕКСТЫ НА ИСПАНСКОМ" in t: print(label, "badge attrs:", a, repr(t))
