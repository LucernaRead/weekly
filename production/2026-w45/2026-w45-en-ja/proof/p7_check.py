# -*- coding: utf-8 -*-
"""P7 independent checks: 8 quotes verbatim + (page N), full-issue counts,
definition paragraphs English-only comparison."""
import glob, html, re, os

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")


def page_texts(d):
    out = []
    for f in sorted(glob.glob(d + "/*.svg")):
        src = open(f, encoding="utf-8").read()
        out.append(" ".join(html.unescape(m.group(1))
                            for m in re.finditer(r"<text[^>]*>([^<]*)</text>", src)))
    return out


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


QUOTES = [
    ("Tuesday, November 3, is Election Day in the United States.", 1),
    ("The hour from 1 to 2 happened twice.", 2),
    ("Which film would you choose ?", 3),
    ("Two games, two continents, one league — that is the modern NFL.", 4),
    ("The results will still be there in the morning.", 5),
    ("Patience is part of the system, not a failure of it.", 6),
    ("Not every place changes.", 2),
    ("One Sunday is not enough — good thing the week has seven days.", 4),
]

for label, d in [("CORE", BASE + "/files/weekly-report-w45-en-core/svg"),
                 ("EDITION", BASE + "/files/weekly-report-w45-en-ja/svg")]:
    pages = page_texts(d)
    full = norm(" ".join(pages))
    p7 = norm(pages[6])
    print("===", label)
    for q, pg in QUOTES:
        tagged = "« " + q + " » (page %d)" % pg
        # tags may wrap: also check with normalized full text
        print(f"  quote p{pg}: p7-tagged={'YES' if norm(tagged) in p7 or q in p7 else 'CHECK'} "
              f"full-count={full.count(norm(q))} p7-count={p7.count(norm(q))}")
    # definition paragraphs: English sentences from core P7 columns
    print("  P7 (page N) tags present:", sorted(set(re.findall(r"\(page \d\)", p7))))

# Definition English-only comparison: strip CJK/kana from P7, compare token streams
CJK = re.compile(r"[\u4e00-\u9fff\u3040-\u30ff]")


def english_only(d):
    src = open(d + "/p7-langue.svg", encoding="utf-8").read()
    texts = [html.unescape(m.group(1)) for m in re.finditer(r"<text[^>]*>([^<]*)</text>", src)]
    joined = norm(" ".join(texts))
    return norm(CJK.sub(" ", joined))


co = english_only(BASE + "/files/weekly-report-w45-en-core/svg")
ed = english_only(BASE + "/files/weekly-report-w45-en-ja/svg")
print("=== English-only P7 (CJK stripped) identical:", co == ed)
if co != ed:
    # show diff tokens
    import difflib
    for line in difflib.unified_diff(co.split(), ed.split(), lineterm="", n=1):
        print(line)
    print("--- core-only tail sample:", co[:200])
