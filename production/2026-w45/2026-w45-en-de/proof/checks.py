#!/usr/bin/env python3
# Independent ENxDE proof checks. Reads only; writes only into this proof dir.
import html, json, os, re, sys
from collections import Counter
from PIL import ImageFont

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = os.path.join(BASE, "files/weekly-report-w45-en-de")
CO = os.path.join(BASE, "files/weekly-report-w45-en-core")
W43 = os.path.join(BASE, "files/weekly-report-en-de")
OUT = os.path.join(BASE, "hidden_files/w45/en-de-proof")
os.makedirs(OUT, exist_ok=True)

TEXT_RE = re.compile(r"<text([^>]*)>(.*?)</text>", re.S)
ATTR_RE = re.compile(r'([\w-]+)="([^"]*)"')
CJK_RE = re.compile(r"[\u2e80-\u9fff\u3040-\u30ff\uac00-\ud7af\uff00-\uffef]")

def load(path):
    s = open(path, encoding="utf-8").read()
    out = []
    for a, c in TEXT_RE.findall(s):
        attrs = dict(ATTR_RE.findall(a))
        out.append({"x": float(attrs.get("x", 0)), "y": float(attrs.get("y", 0)),
                    "size": float(attrs.get("font-size", 0)),
                    "fam": attrs.get("font-family", ""),
                    "bold": attrs.get("font-weight") == "700",
                    "anchor": attrs.get("text-anchor", "start"),
                    "text": html.unescape(re.sub(r"<[^>]+>", "", c))})
    return out, s

PAGES = ["p1-front", "p2-life", "p3-culture", "p4-sport", "p5-jeunesse", "p6-politique", "p7-langue", "p8-exercices"]
ed, co = {}, {}
for p in PAGES:
    ed[p], _ = load(os.path.join(ED, "svg", p + ".svg"))
    co[p], _ = load(os.path.join(CO, "svg", p + ".svg"))

def cjk_count(texts):
    return sum(1 for t in texts for ch in t["text"] if CJK_RE.match(ch))
def fw_count(texts):
    return sum(t["text"].count("（") + t["text"].count("）") for t in texts)
def banned(texts):
    return sum(t["text"].count("桥接") for t in texts)

print("== A. CJK / fullwidth parens / 桥接 (edition SVGs) ==")
for p in PAGES:
    print(f"{p}: CJK={cjk_count(ed[p])} FWparens={fw_count(ed[p])} 桥接={banned(ed[p])} texts={len(ed[p])}")
for name, path in [("KIT", os.path.join(ED, "WEEKLY-KIT.md")), ("ABSTRACT", os.path.join(ED, "ABSTRACT.txt"))]:
    s = open(path, encoding="utf-8").read()
    print(f"{name}: CJK={sum(1 for ch in s if CJK_RE.match(ch))} FWparens={s.count('（')+s.count('）')} 桥接={s.count('桥接')} bytes={len(s.encode())} ascii_dquote={s.count(chr(34))}")

print("\n== B. Removed-string classification (freeze diff JSON) ==")
diff = json.load(open(os.path.join(OUT, "freeze-diff-proof.json")))
FURN = ["THE LEARNERS' WEEKLY", "WEEKLY IN ENGLISH · 每周", "The Lucerna · 英语周报", "第 1 版", "第 2 版", "第 3 版", "第 4 版", "第 5 版", "第 6 版", "第 7 版", "第 8 版"]
def has_latin(s):
    return bool(re.search(r"[A-Za-z]", s))
def is_punct_frag(s):
    return not re.search(r"[A-Za-z\u4e00-\u9fff]", s)
unclass = []
with open(os.path.join(OUT, "removed-strings.txt"), "w", encoding="utf-8") as f:
    for pg in sorted(diff["pages"], key=int):
        page = diff["pages"][pg]
        f.write(f"\n===== P{pg} removed {len(page['removed_strings'])} =====\n")
        ed_words = re.findall(r"[A-Za-z0-9'’\-]+", " ".join(t["text"] for t in ed[PAGES[int(pg)-1]]))
        ed_seq = " ".join(ed_words)
        for r in page["removed_strings"]:
            s = r["text"]
            if CJK_RE.search(s):
                cls = "a-CJK-bearing"
            elif any(x in s for x in FURN):
                cls = "b-furniture"
            elif is_punct_frag(s):
                cls = "d-punct-frag"
            else:
                # c: rewrap fragment? word sequence of s appears in edition page word stream
                words = re.findall(r"[A-Za-z0-9'’\-]+", s)
                if words and " ".join(words) in ed_seq:
                    cls = "c-rewrap(whole-seq-in-edition)"
                elif words:
                    # check each word appears and s is a fragment of a longer core sentence:
                    # fragment if s is substring of some core text concatenation with neighbours
                    cls = "c?-fragment-candidate"
                    unclass.append((pg, s))
                else:
                    cls = "?"
                    unclass.append((pg, s))
            f.write(f"[P{pg}][{cls}] {s!r}\n")
print("unclassified/fragment-candidates:", len(unclass))
for pg, s in unclass:
    print(f"  P{pg}: {s!r}")

print("\n== C. P8 extracts ==")
sys.path.insert(0, os.path.join(BASE, "tools"))
import subprocess
for label, svg in [("core", os.path.join(CO, "svg/p8-exercices.svg")), ("edition", os.path.join(ED, "svg/p8-exercices.svg"))]:
    subprocess.run([sys.executable, os.path.join(BASE, "tools/p8.py"), "extract", "--p8", svg, "--total", "150",
                    "--json", os.path.join(OUT, f"p8-extract-{label}.json")], capture_output=True, text=True)
ce = json.load(open(os.path.join(OUT, "p8-extract-core.json")))
ee = json.load(open(os.path.join(OUT, "p8-extract-edition.json")))
print("core extract keys:", list(ce.keys()))
print("edition extract keys:", list(ee.keys()))
# dump structure sample to file
with open(os.path.join(OUT, "p8-extract-summary.txt"), "w", encoding="utf-8") as f:
    f.write(json.dumps({"core": ce, "edition": ee}, ensure_ascii=False, indent=1)[:20000])

print("\n== D. Gloss (rendered SVG reassembly) ==")
def gloss_of(texts):
    res = []
    for i, t in enumerate(texts):
        if t["text"].startswith("Anmerkung | "):
            parts = [t["text"][len("Anmerkung | "):]]
            j = i + 1
            while j < len(texts):
                n = texts[j]
                if n["x"] == t["x"] and n["size"] == t["size"] and abs((n["y"] - texts[j-1]["y"]) - 29.725) < 1.0:
                    parts.append(n["text"]); j += 1
                else:
                    break
            joined = " ".join(parts)
            res.append((t["text"][:20], joined, [x.strip() for x in joined.split("·") if x.strip()]))
    return res
def gloss_core(texts):
    # core gloss boxes start with 讲解｜ ; same reassembly by x/size/step
    res = []
    for i, t in enumerate(texts):
        if t["text"].startswith("讲解"):
            parts = [re.sub(r"^讲解｜", "", t["text"])]
            j = i + 1
            while j < len(texts):
                n = texts[j]
                if n["x"] == t["x"] and n["size"] == t["size"]:
                    parts.append(n["text"]); j += 1
                else:
                    break
            joined = " ".join(parts)
            res.append((joined, [x.strip() for x in joined.split("·") if x.strip()]))
    return res
for p in ["p2-life", "p3-culture", "p4-sport", "p5-jeunesse", "p6-politique"]:
    g = gloss_of(ed[p])
    gc = gloss_core(co[p])
    print(f"{p} edition gloss boxes={len(g)} items={[len(x[2]) for x in g]} core boxes={len(gc)} items={[len(x[1]) for x in gc]}")
    for _, joined, items in g:
        print(f"   ED: {joined}")
        print(f"   items: {items}")
    for joined, items in gc:
        print(f"   CO: {joined} -> {len(items)}")

print("\n== E. P7 golden sentences / definitions / structure ==")
GOLD = [
    ("Tuesday, November 3, is Election Day in the United States.", "p.1", "A2"),
    ("The hour from 1 to 2 happened twice.", "p.2", "A2"),
    ("Which film would you choose?", "p.3", "B1"),
    ("Two games, two continents, one league — that is the modern NFL.", "p.4", "B1"),
    ("The results will still be there in the morning.", "p.5", "B2"),
    ("Patience is part of the system, not a failure of it.", "p.6", "B2"),
    ("Not every place changes.", "p.2", "A2"),
    ("One Sunday is not enough — good thing the week has seven days.", "p.4", "B1"),
]
p7ed = " ".join(t["text"] for t in ed["p7-langue"])
p7co = " ".join(t["text"] for t in co["p7-langue"])
for sent, pg, lv in GOLD:
    print(f"gold {sent[:40]!r}: edition_count={p7ed.count(sent)} core_count={p7co.count(sent)}")
# P7: count occurrences of each golden sentence across whole edition (article + P7 = 2x)
for sent, pg, lv in GOLD:
    ce_count = sum(1 for p in PAGES for t in ed[p] if sent in t["text"])
    cc_count = sum(1 for p in PAGES for t in co[p] if sent in t["text"])
    print(f"  whole-edition text-node hits {sent[:30]!r}: edition={ce_count} core={cc_count}")
# P7 section heads presence
for head in ["PHRASES OF THE WEEK", "ERROR CLINIC", "READERS' CORNER", "NEXT WEEK"]:
    print(f"P7 head {head}: ed={[t['text'] for t in ed['p7-langue'] if head in t['text']]} co={[t['text'] for t in co['p7-langue'] if head in t['text']]}")

print("\n== F. Readers corner ==")
for label, texts in [("edition", ed["p7-langue"]), ("core", co["p7-langue"])]:
    joined = " ".join(t["text"] for t in texts)
    print(f"--- {label} ---")
    for needle in ["On Sunday, I slept one hour more", "M. L.", "Chicago", "Anmerkung der Redaktion"]:
        print(f"  {needle!r}: count={joined.count(needle)}")
# edition disclosure reassembled: find Anmerkung der Redaktion para lines (size 20 sans, consecutive)
texts = ed["p7-langue"]
for i, t in enumerate(texts):
    if t["text"].startswith("Anmerkung der Redaktion"):
        lines = [t["text"]]
        j = i + 1
        while j < len(texts) and texts[j]["size"] == 20 and texts[j]["x"] == t["x"]:
            lines.append(texts[j]["text"]); j += 1
        print(f"disclosure lines={len(lines)} x={t['x']} size={t['size']}")
        for ln in lines:
            print(f"  DISC: {ln}")
        print(f"  reassembled: {' '.join(lines)}")
        # box: find rects near? print surrounding rect info from raw svg later
        break

print("\n== G. Furniture / W43 comparison ==")
w43 = {}
for p in PAGES:
    try:
        w43[p], _ = load(os.path.join(W43, "svg", p + ".svg"))
    except Exception as e:
        print("W43 load fail", p, e)
def find(texts, needle):
    return [t["text"] for t in texts if needle in t["text"]]
for needle in ["ENGLISCHER TEXT · DEUTSCHE ERKLÄRUNGEN", "The Lucerna · ENGLISH WEEKLY VOL.2", "Anmerkung | ", "— Seite "]:
    print(f"{needle!r}: ed-P1={[t for t in find(ed['p1-front'], needle)]} w43-P1={[t for t in find(w43.get('p1-front', []), needle)]}")
for p in PAGES:
    print(f"{p} footer ed={[t['text'] for t in ed[p] if t['text'].startswith('The Lucerna ·')]} w43={[t['text'] for t in w43.get(p, []) if t['text'].startswith('The Lucerna ·')]} pageline ed={[t['text'] for t in ed[p] if t['text'].startswith('Seite ')]} w43={[t['text'] for t in w43.get(p, []) if t['text'].startswith('Seite ')]}")
print("P8 separators ed:", [t["text"] for t in ed["p8-exercices"] if t["text"].startswith("— Seite")])
print("P8 separators w43:", [t["text"] for t in w43.get("p8-exercices", []) if t["text"].startswith("— Seite")])
print("P8 D head ed:", [t["text"] for t in ed["p8-exercices"] if t["text"].startswith("D ·")])
print("P8 D head w43:", [t["text"] for t in w43.get("p8-exercices", []) if t["text"].startswith("D ·")])
print("P8 writing-key form ed:", [t["text"] for t in ed["p8-exercices"] if "Offene Aufgabe" in t["text"] or "Stichpunkte" in t["text"]])
print("P8 writing-key form w43:", [t["text"] for t in w43.get("p8-exercices", []) if "Offene Aufgabe" in t["text"] or "Stichpunkte" in t["text"]])

print("\n== H. Model text word count ==")
def model_words(texts):
    # find MODEL section: texts after a text containing MODEL
    joined_lines = [t["text"] for t in texts]
    for i, t in enumerate(joined_lines):
        if "MODEL" in t:
            print(f"  MODEL head at line {i}: {t!r}; following: {joined_lines[i+1:i+6]}")
    return None
model_words(ed["p8-exercices"]); model_words(co["p8-exercices"])
# direct: search for 'My Tuesday' title
for label, texts in [("ed", ed["p8-exercices"]), ("co", co["p8-exercices"])]:
    for i, t in enumerate(texts):
        if "My Tuesday" in t["text"]:
            print(f"{label} model title line {i}: {t}")
            for j in range(i+1, min(i+12, len(texts))):
                print(f"   {label} +{j-i}: {texts[j]['text']!r} size={texts[j]['size']}")
            break
print("DONE")
