#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Round 2 independent extraction: exercise stems+options per page and P8 keys.
Reads SVG <text> elements in FILE ORDER (column-major as emitted).
An item starts at a level badge (A2/B1/B2) followed by a number token N. or N–M.
Accumulates following texts until the next item start / page footer.
P8 answer section parsed separately (after the '답 ·' header line).
No build sources read. No files written outside the gates dir (argv outdir)."""
import re, os, sys, json
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files")
EDITIONS = {
 "zh-cn": "weekly-report-w46-ko-core",
 "de": "weekly-report-w46-ko-de", "en": "weekly-report-w46-ko-en",
 "es": "weekly-report-w46-ko-es", "fr": "weekly-report-w46-ko-fr",
 "it": "weekly-report-w46-ko-it", "ja": "weekly-report-w46-ko-ja",
 "nl": "weekly-report-w46-ko-nl", "pt": "weekly-report-w46-ko-pt",
 "ru": "weekly-report-w46-ko-ru", "zh-tw": "weekly-report-w46-ko-zh-tw",
}
PAGES = ["p1-pyoji.svg","p2-saenghwal.svg","p3-munhwa.svg","p4-seupocheu.svg",
         "p5-cheongnyeon.svg","p6-gipi.svg","p7-mal.svg","p8-siheom.svg"]
TEXT_RE = re.compile(r'<text x="([^"]+)" y="([^"]+)"([^>]*)>([^<]*)</text>')
NUM_RE = re.compile(r"^(\d+)(?:–(\d+))?\.$")
LEVELS = {"A2","B1","B2"}

def texts_of(path):
    s = open(path, encoding="utf-8").read()
    return [(float(x), float(y), t) for x, y, _, t in TEXT_RE.findall(s)]

def parse_page(edir, pg):
    els = texts_of(os.path.join(edir, "svg", pg))
    items = []
    cur = None
    in_answers = False
    for x, y, t in els:
        ts = t.strip()
        if pg == "p8-siheom.svg" and ts.startswith("답 ·"):
            in_answers = True
        if in_answers:
            continue
        # badge + number pattern: badge element, then number element next
        if ts in LEVELS:
            cur = {"level": ts, "num": None, "parts": [], "page": pg}
            items.append(cur)
            continue
        if cur is not None and cur["num"] is None and NUM_RE.match(ts):
            cur["num"] = ts
            continue
        if cur is not None and cur["num"] is not None:
            # a new section header in same column would be mistaken; stop on footer
            if y > 2580:
                cur = None
                continue
            # type label like 填空/造句/翻译/把词和说明配对 is part of header, keep as label
            cur["parts"].append(ts)
    # drop badge-only orphans (no number) and footer-only
    out = []
    for it in items:
        if it["num"] is None:
            continue
        out.append({"level": it["level"], "num": it["num"],
                    "text": " ".join(p for p in it["parts"] if p).strip(),
                    "page": pg})
    return out

def parse_p8_answers(edir):
    els = texts_of(os.path.join(edir, "svg", "p8-siheom.svg"))
    ans = {}
    started = False
    for x, y, t in els:
        ts = t.strip()
        if ts.startswith("답 ·"):
            started = True
            continue
        if not started or y > 2580:
            continue
        m = re.match(r"^(\d+)\.\s+(.*)$", ts)
        if m:
            ans[int(m.group(1))] = m.group(2).strip()
    return ans

def main(outdir):
    os.makedirs(outdir, exist_ok=True)
    all_data = {}
    for code, d in EDITIONS.items():
        edir = os.path.join(BASE, d)
        items = []
        for pg in PAGES:
            items.extend(parse_page(edir, pg))
        ans = parse_p8_answers(edir)
        all_data[code] = {"items": items, "answers": ans,
                          "n_items": len(items), "n_answers": len(ans)}
        with open(os.path.join(outdir, f"exercises-{code}.txt"), "w", encoding="utf-8") as f:
            for it in items:
                key = ans.get(int(it["num"].rstrip(".").split("–")[0])) if "–" not in it["num"] else "RANGE"
                f.write(f"[{it['page']}] {it['level']} {it['num']} {it['text']}  || P8KEY: {key}\n")
            f.write("\n--- P8 ANSWERS ---\n")
            for n in sorted(ans):
                f.write(f"{n}. {ans[n]}\n")
    json.dump(all_data, open(os.path.join(outdir, "exercises-all.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    for code, d in all_data.items():
        nums = sorted(int(i["num"].rstrip(".").split("–")[0]) for i in d["items"])
        print(code, "items:", d["n_items"], "answers:", d["n_answers"],
              "first/last:", nums[:3], nums[-3:], "missing:", [n for n in range(1, 151) if n not in nums and n not in (26,27,28,44,45,46,62,63,64,142,143,144)])

if __name__ == "__main__":
    main(sys.argv[1])
