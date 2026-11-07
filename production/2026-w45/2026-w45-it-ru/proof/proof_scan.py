#!/usr/bin/env python3
"""Independent IT x RU W45 proofread scans (read-only on deliverables + core + W43)."""
import re, sys, os, hashlib, json
from xml.etree import ElementTree as ET

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE = f"{BASE}/files/weekly-report-w45-it-core/svg"
ED = f"{BASE}/files/weekly-report-w45-it-ru/svg"
W43 = f"{BASE}/files/weekly-report-it-ru/svg"
PAGES = ["p1-prima","p2-vita","p3-cultura","p4-sport","p5-giovani","p6-approfondimento","p7-lingua","p8-valutazione"]
NS = {"s": "http://www.w3.org/2000/svg"}

def load_texts(path):
    tree = ET.parse(path)
    out = []
    for el in tree.iter():
        tag = el.tag.split("}")[-1]
        if tag == "text":
            txt = "".join(el.itertext())
            out.append({"x": el.get("x"), "y": el.get("y"), "fs": el.get("font-size"),
                        "anchor": el.get("text-anchor"), "fam": el.get("font-family"),
                        "weight": el.get("font-weight"), "text": txt})
    return out

def raw(path):
    return open(path, encoding="utf-8").read()

def all_ed_texts():
    return {p: load_texts(f"{ED}/{p}.svg") for p in PAGES}
def all_core_texts():
    return {p: load_texts(f"{CORE}/{p}.svg") for p in PAGES}

out = []
def sec(t):
    out.append("\n### " + t)
def line(s):
    out.append(s)

# ---- 1. banned term + CJK + bridge across edition SVGs
sec("1a banned-term/CJK scan (edition SVGs)")
for p in PAGES:
    s = raw(f"{ED}/{p}.svg")
    cjk = sum(1 for ch in s if "\u4e00" <= ch <= "\u9fff" or "\u3040" <= ch <= "\u30ff" or "\uac00" <= ch <= "\ud7a3")
    line(f"{p}: 桥接={s.count('桥接')} bridge={len(re.findall(r'bridge', s, re.I))} CJKchars={cjk}")
sec("1b banned term in KIT/ABSTRACT/PDFs (binary substring)")
for f in [f"{BASE}/files/weekly-report-w45-it-ru/WEEKLY-KIT.md",
          f"{BASE}/files/weekly-report-w45-it-ru/ABSTRACT.txt",
          f"{BASE}/files/weekly-report-w45-it-ru/La-Lucerna-VOL2-RU.pdf",
          f"{BASE}/files/weekly-report-w45-it-ru/La-Lucerna-VOL2-RU-web.pdf"]:
    b = open(f, "rb").read()
    line(f"{os.path.basename(f)}: 桥接-bytes={b.count('桥接'.encode())}")

# ---- freeze diff removed strings (from proof json)
sec("1c freeze-diff removed strings, full list (proof run)")
d = json.load(open(os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-ru-proof/freeze-diff-proof.json")))
# print structure keys
line("json keys: " + str(list(d.keys())[:10]))
print(json.dumps(d, ensure_ascii=False)[:2000], file=sys.stderr)

# ---- P7 word box
sec("2 P7 word box")
ce, ed = all_core_texts(), all_ed_texts()
def find(ts, pred):
    return [t for t in ts if pred(t["text"])]
for label, ts in [("CORE", ce["p7-lingua"]), ("ED", ed["p7-lingua"])]:
    line(f"--{label} guillemet-starting nodes:")
    for t in ts:
        if t["text"].startswith("«"):
            line(f"   y={t['y']} fs={t['fs']} {t['text']!r}")
    line(f"--{label} assaggio-gloss nodes:")
    for t in ts:
        if t["text"].startswith("assaggio"):
            line(f"   y={t['y']} {t['text']!r}")
    line(f"--{label} definition continuation nodes (è la prova / prova di):")
    for t in ts:
        if "prova di un cibo" in t["text"] or "decidere se piace" in t["text"] or "vive a pagina" in t["text"] or "Panettone" in t["text"]:
            line(f"   y={t['y']} {t['text']!r}")

sec("2b P7 golden sentences: quoted-form and inner-phrase counts, whole issue (core vs edition)")
# golden inner phrases: extract from core P7 FRASI section? Instead take the 8 RU translations' Italian originals:
# Strategy: list all «...» strings in core P7 and edition P7, and count occurrences across all 8 pages.
def page_text_str(ts_by_page):
    return {p: "\n".join(t["text"] for t in ts) for p, ts in ts_by_page.items()}
core_str = page_text_str(ce); ed_str = page_text_str(ed)
core_all = "\n".join(core_str.values()); ed_all = "\n".join(ed_str.values())
for label, ts in [("CORE", ce["p7-lingua"]), ("ED", ed["p7-lingua"])]:
    line(f"--{label} P7 guillemet lines in FRASI area (y>1686):")
    for t in ts:
        try: y = float(t["y"])
        except: continue
        if y > 1686 and ("«" in t["text"] or t["text"].strip().startswith("«")):
            line(f"   y={t['y']} {t['text']!r}")
sec("2c P7 quote tags in order (edition)")
tags = re.findall(r"\(Страница (\d+)\)", "\n".join(t["text"] for t in ed["p7-lingua"]))
line("edition P7 (Страница N) in node order: " + str(tags))
tags_core = re.findall(r"\(Pagina (\d+)\)|\(第(\d+)版\)|\(Страница (\d+)\)", "\n".join(t["text"] for t in ce["p7-lingua"]))
line("core P7 tag-ish matches: " + str(tags_core))
# core P7 FRASI tags: core native is Chinese; find parenthetical page refs near golden sentences
for t in ce["p7-lingua"]:
    if "第" in t["text"] and "版" in t["text"]:
        line(f"   CORE tag node y={t['y']} {t['text']!r}")

sec("2d golden inner-phrase 2x check (edition + core)")
# inner phrases = quoted Italian sentences on P7 (strip guillemets)
quoted_ed = [t["text"].strip().strip("«»") for t in ed["p7-lingua"] if t["text"].strip().startswith("«")]
line("edition P7 quoted nodes: " + str(quoted_ed))
for q in quoted_ed:
    inner = q.strip("«» ")
    line(f"  inner {inner!r}: core_all={core_all.count(inner)} ed_all={ed_all.count(inner)} quoted_core={core_all.count('«'+inner+'»')} quoted_ed={ed_all.count('«'+inner+'»')}")

sec("7 readers corner")
for label, ts in [("CORE", ce["p7-lingua"]), ("ED", ed["p7-lingua"])]:
    line(f"--{label} letter/disclosure area nodes:")
    for t in ts:
        if any(k in t["text"] for k in ["Ciao! Sono Li", "esempio della redazione", "Пример редакции", "Напишите нам", "настоящие", "лучшего текста", "VOL.3", "PROSSIMA", "СЛЕДУЮЩЕМ"]):
            line(f"   y={t['y']} {t['text']!r}")
# concatenated disclosure: find consecutive nodes in edition P7 letter box region
ed7 = ed["p7-lingua"]
for i, t in enumerate(ed7):
    if t["text"].startswith("Пример редакции"):
        line("disclosure concatenation (next 3 nodes): " + " | ".join(x["text"] for x in ed7[i:i+3]))
        line("joined: " + repr(" ".join(x["text"] for x in ed7[i:i+3])))

sec("3 P8 keydiff line-by-line (printed lines containing item numbers)")
import subprocess
# use p8 extract outputs
for label, path in [("CORE", f"{CORE}/p8-valutazione.svg"), ("ED", f"{ED}/p8-valutazione.svg")]:
    r = subprocess.run([sys.executable, f"{BASE}/tools/p8.py", "extract", "--p8", path, "--total", "150"],
                       capture_output=True, text=True)
    open(os.path.expanduser(f"~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-ru-proof/p8-extract-{label.lower()}.txt"), "w").write(r.stdout + r.stderr)
    line(f"--{label} extract exit={r.returncode} lines={len(r.stdout.splitlines())}")
    for ln in r.stdout.splitlines():
        m = re.match(r"\s*(6|13|14|15|16|20|38|58|71|74|77|102|137|138|139|140)\b", ln)
        if m:
            line(f"   {ln}")

sec("6 gloss: edition rendered gloss strings")
for p in PAGES:
    gs = [t["text"] for t in ed[p] if t["text"].startswith("Пояснение")]
    for g in gs:
        items = [x.strip() for x in g.split("·")]
        line(f"{p}: gloss-node items={len(items)} :: {g!r}")
    # also nodes containing Пояснение not at start
    for t in ed[p]:
        if "Пояснение" in t["text"] and not t["text"].startswith("Пояснение"):
            line(f"{p}: MID-gloss node {t['text']!r}")
sec("6b core gloss strings (Chinese native)")
for p in PAGES:
    for t in ce[p]:
        if "注释" in t["text"] or "注解" in t["text"] or "词汇" in t["text"]:
            line(f"CORE {p}: y={t['y']} {t['text']!r}")
sec("6c P1 bridge word list")
for label, ts in [("CORE", ce["p1-prima"]), ("ED", ed["p1-prima"])]:
    for t in ts:
        if "primo freddo" in t["text"] and "·" in t["text"]:
            line(f"{label} P1: {t['text']!r}")

sec("4 residual scan (all 8 edition SVGs, raw text)")
GER = ["Mailand", "Kostprobe", "Seite ", "HINWEIS", "ÜBUNGEN", "MERK", "LÖSUNGEN", "Wochenzeitung", "Erklärungen", "Leser", "Übung", "Antworten", "Wörter", "Sprach", "Italienischer Text", "Italienische"]
OTHER = ["Note — ", "Nota — ", "Uitleg — ", "Nota ·", "Page ", "Página", "PAGINA", "SEITE", "— Page", "— Página", "Exercises", "Exercices", "Ejercicios", "Exercícios", "Oefeningen", "Instru", "Écrivez", "Escribe", "Write ", "Fill in", "Complétez", "Remplissez"]
for p in PAGES:
    s = raw(f"{ED}/{p}.svg")
    hits = {}
    for w in GER + OTHER:
        c = s.count(w)
        if c: hits[w] = c
    line(f"{p}: {hits if hits else 'clean'}")
# Italian grammar strings that look German? check 'mettere: io' etc
sec("4b Italian grammar strings containing '->' etc (to distinguish)")
for p in PAGES:
    s = raw(f"{ED}/{p}.svg")
    for m in re.findall(r".{0,30}→.{0,20}", s):
        pass
    line(f"{p}: arrow-occurrences={s.count('→')}")

sec("8 badge three-way")
def badge_probe(path, label):
    ts = load_texts(path)
    s = raw(path)
    line(f"--{label}: badge-string present={('ТЕКСТЫ НА ИТАЛЬЯНСКОМ' in s)}")
    for t in ts:
        if "ТЕКСТЫ НА ИТАЛЬЯНСКОМ" in t["text"] or "TESTI IN" in t["text"] or "ИТАЛЬЯНСКОМ · ОБЪЯСНЕНИЯ" in t["text"]:
            line(f"   badge node x={t['x']} y={t['y']} fs={t['fs']} anchor={t['anchor']} weight={t['weight']} {t['text']!r}")
    # y=372 nodes
    for t in ts:
        try: y = float(t["y"])
        except: continue
        if abs(y - 372) < 3:
            line(f"   y~372 node x={t['x']} fs={t['fs']} {t['text']!r}")
    for t in ts:
        try: y = float(t["y"])
        except: continue
        if abs(y - 574) < 3:
            line(f"   y~574 node x={t['x']} fs={t['fs']} {t['text']!r}")
badge_probe(f"{W43}/p1-prima.svg", "W43 ITxRU P1")
badge_probe(f"{CORE}/p1-prima.svg", "W45 CORE P1")
badge_probe(f"{ED}/p1-prima.svg", "W45 RU P1")
sec("8b W43 P1 strapline-like lines: all text nodes y in [340,420] W43 vs core vs edition")
for label, path in [("W43", f"{W43}/p1-prima.svg"), ("CORE", f"{CORE}/p1-prima.svg"), ("ED", f"{ED}/p1-prima.svg")]:
    for t in load_texts(path):
        try: y = float(t["y"])
        except: continue
        if 340 <= y <= 420:
            line(f"{label} y={t['y']} x={t['x']} fs={t['fs']} {t['text']!r}")

sec("9 furniture vs W43 (string presence)")
W43S = {p: raw(f"{W43}/{p}.svg") for p in PAGES}
EDS = {p: raw(f"{ED}/{p}.svg") for p in PAGES}
checks = {
 "footer": "La Lucerna · ИТАЛЬЯНСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.2 · ТЕКСТЫ НА ИТАЛЬЯНСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ",
 "footer-W43": "La Lucerna · ИТАЛЬЯНСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.1 · ТЕКСТЫ НА ИТАЛЬЯНСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ",
 "page-line-p1": "Страница 1 из 8",
 "gloss-prefix": "Пояснение — ",
 "strap": "OGNI SETTIMANA IN ITALIANO · ИТАЛЬЯНСКИЙ, КОТОРЫЙ ЧИТАЮТ ИТАЛЬЯНЦЫ",
}
for k, v in checks.items():
    line(f"{k}: W43-any={any(v in s for s in W43S.values())} ED-pages={sum(1 for s in EDS.values() if v in s)}/8")
for n in range(1, 9):
    sep = f"— СТРАНИЦА {n} —"
    line(f"P8 sep {sep}: W43-P8={sep in W43S['p8-valutazione']} ED-P8={sep in EDS['p8-valutazione']}")
    pag = f"— PAGINA {n} —"
    line(f"   PAGINA form: W43-P8={pag in W43S['p8-valutazione']} ED-P8={pag in EDS['p8-valutazione']}")
# section heads + instruction words presence in ED
for h in ["VITA · ЖИЗНЬ", "CULTURA · КУЛЬТУРА", "SPORT · СПОРТ", "GIOVANI · МОЛОДЁЖЬ", "APPROFONDIMENTO · РАЗБОР", "LINGUA · ЯЗЫК",
          "Вставьте", "Составьте предложение", "Переведите", "Верно или нет", "Напишите", "Соедините пары", "E TU? · А ВЫ?"]:
    line(f"head/instr {h!r}: ED-pages={sum(1 for s in EDS.values() if h in s)} W43-pages={sum(1 for s in W43S.values() if h in s)}")

sec("10 images: embedded image payload hashes per page (core vs edition)")
for p in PAGES:
    def imghashes(s):
        hs = []
        for m in re.finditer(r"data:image/[^;]+;base64,([A-Za-z0-9+/=]+)", s):
            hs.append(hashlib.sha256(m.group(1).encode()).hexdigest()[:16] + f"({len(m.group(1))})")
        return hs
    ch, eh = imghashes(raw(f"{CORE}/{p}.svg")), imghashes(raw(f"{ED}/{p}.svg"))
    line(f"{p}: core={ch} ed={eh} equal={ch==eh}")
    # credit lines: nodes containing source-like strings
    for t in ed[p]:
        if any(k in t["text"] for k in ["Wikimedia", "Commons", "Fonte", "©", "CC0", "Public", "Автор", "Источник"]):
            line(f"   ED credit y={t['y']} {t['text']!r}")
    for t in ce[p]:
        if any(k in t["text"] for k in ["Wikimedia", "Commons", "Fonte", "©", "CC0", "来源"]):
            line(f"   CORE credit y={t['y']} {t['text']!r}")

sec("12 model text + levels placeholder (see separate count script)")
for label, ts in [("CORE", ce["p8-valutazione"]), ("ED", ed["p8-valutazione"])]:
    for i, t in enumerate(ts):
        if "Testo modello" in t["text"]:
            line(f"{label} model label y={t['y']} {t['text']!r}; following nodes:")
            for x in ts[i+1:i+12]:
                line(f"    y={x['y']} {x['text']!r}")

open(os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-ru-proof/scan1.txt"), "w").write("\n".join(out))
print(f"wrote {len(out)} lines")
