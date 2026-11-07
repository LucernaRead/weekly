#!/usr/bin/env python3
import os, re, html, json
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files")
OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/ru-proofread-gates-round2")
EDS = ["core", "de", "en", "es", "fr", "it", "ja", "ko", "nl", "pt", "zh-tw"]
TEXT_RE = re.compile(r'<text([^>]*)>(.*?)</text>', re.S)
ATTR_RE = re.compile(r'([\w-]+)="([^"]*)"')
def parse(path):
    s = open(path, encoding="utf-8").read()
    out = []
    for attrs, inner in TEXT_RE.findall(s):
        a = dict(ATTR_RE.findall(attrs))
        t = html.unescape(re.sub(r"<[^>]+>", "", inner))
        try:
            x = float(a.get("x", "0")); y = float(a.get("y", "0"))
        except ValueError:
            x = y = 0.0
        out.append({"x": x, "y": y, "size": a.get("font-size", "?"),
                    "fill": a.get("fill", "?"), "fam": a.get("font-family", "?"), "text": t})
    return out
def ed_dir(ed):
    return os.path.join(BASE, "weekly-report-w46-ru-" + ed)
p8keys = {}
for ed in EDS:
    nodes = parse(os.path.join(ed_dir(ed), "svg", "p8-test.svg"))
    keys = {}
    for n in nodes:
        m = re.match(r"^(\d{1,3})\.\s+(.+)$", n["text"].strip())
        if m and str(n["size"]) in ("13.0", "13"):
            keys[int(m.group(1))] = m.group(2)
    p8keys[ed] = keys
    print(ed, "p8 key lines:", len(keys), "range:", min(keys) if keys else None, max(keys) if keys else None)
json.dump({k: {str(i): v for i, v in d.items()} for k, d in p8keys.items()},
          open(os.path.join(OUT, "p8-keys-extracted.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
for ed in EDS:
    print("---", ed, "75-78:", {i: p8keys[ed].get(i) for i in (75, 76, 77, 78)})
for ed in EDS:
    nodes = parse(os.path.join(ed_dir(ed), "svg", "p5-molodezh.svg"))
    words = [n["text"] for n in nodes if re.match(r"^7[5-8]\.\s", n["text"].strip())]
    opts = [n["text"] for n in nodes if re.match(r"^[a-d]\.\s", n["text"].strip())]
    print("P5", ed, "words=", words, "opts=", opts)
for ed in EDS:
    for pg, yy in (("p3-kultura.svg", 2564.45), ("p4-sport.svg", 2553.45)):
        nodes = parse(os.path.join(ed_dir(ed), "svg", pg))
        home = [n for n in nodes if abs(n["x"] - 65) < 1 and abs(n["y"] - yy) < 1.5]
        col2 = [n for n in nodes if abs(n["x"] - 527) < 1 and 1600 <= n["y"] <= 1800]
        print("D2", ed, pg, "HOME=", [(n["text"], n["size"], n["fill"]) for n in home],
              "COL2TOP=", [(round(n["y"], 1), n["text"][:60]) for n in col2])
print("==== ORPHAN SCAN ====")
orphans = []
for ed in EDS:
    for p in range(1, 9):
        fn = sorted(f for f in os.listdir(os.path.join(ed_dir(ed), "svg")) if f.startswith("p%d-" % p))[0]
        nodes = parse(os.path.join(ed_dir(ed), "svg", fn))
        for i, n in enumerate(nodes):
            if n["x"] in (527.0, 989.0, 1451.0) and 1600 <= n["y"] <= 1800 and str(n["size"]) == "20.5":
                prev = nodes[i - 1] if i > 0 else None
                prev_is_home = prev is not None and prev["x"] == 65.0 and prev["y"] > 2400
                print("CAND", ed, "p%d" % p, "y=", n["y"], "x=", n["x"], "prev_home=", prev_is_home,
                      "prev=", repr(prev["text"][:50]) if prev else None, "text=", repr(n["text"]))
                if prev_is_home:
                    orphans.append((ed, p, n["text"]))
print("ORPHANS:", orphans)
OPEN = "\uff08(\uff3b\uff5b\u3008\u300a\u300c\u300e\u3010"
CLOSE_START = "\uff09)\uff3d\uff5d\u3009\u300b\u300d\u300f\u3011\u3001\u3002\uff1b\uff1a\uff0c\uff0e\u30fb!\uff01?\uff1f"
print("==== KINSOKU SCAN ====")
hits = []
for ed in EDS:
    for p in range(1, 9):
        fn = sorted(f for f in os.listdir(os.path.join(ed_dir(ed), "svg")) if f.startswith("p%d-" % p))[0]
        for n in parse(os.path.join(ed_dir(ed), "svg", fn)):
            t = n["text"].strip()
            if t and t[-1] in OPEN:
                hits.append((ed, p, "END-OPEN", t)); print("HIT", ed, p, "END-OPEN", repr(t))
            if t and t[0] in CLOSE_START:
                hits.append((ed, p, "START-CLOSE", t)); print("HIT", ed, p, "START-CLOSE", repr(t))
print("KINSOKU HITS:", len(hits))
nodes = parse(os.path.join(ed_dir("ja"), "svg", "p8-test.svg"))
for n in nodes:
    if "\u6a21\u7bc4\u6587" in n["text"] or "\u4f5c\u6587" in n["text"]:
        print("JA HNOTE:", n["x"], n["y"], n["size"], repr(n["text"]))
json.dump(hits, open(os.path.join(OUT, "kinsoku-hits.json"), "w", encoding="utf-8"), ensure_ascii=False)
