# -*- coding: utf-8 -*-
"""Independent orphan scan for W45 KO x ZH-TW.
Part A: rendered-line window scan (own code) over shipped SVGs.
Part B: wrap-record run in my scratch copy of the edition build (reg-ed),
  analysing recorded svglib.wrap() calls: NO_START residuals, KO mid-word
  splits with tail >=3 syllables, lone finals <=3 chars, split by script
  dominance. Writes proof_orphan.json + summary."""
import re, os, sys, json, html
from collections import Counter

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = os.path.join(GOAL, "files/weekly-report-w45-ko-zh-tw/svg")
WORK = os.path.dirname(os.path.abspath(__file__))
PAGES = ["p1-pyoji", "p2-saenghwal", "p3-munhwa", "p4-seupocheu",
         "p5-cheongnyeon", "p6-gipi", "p7-mal", "p8-siheom"]
NO_START = set("。、，．！？：；）」』】ー…‥・)]}〉》.,!?%:;\"")

def parse(path):
    s = open(path, encoding="utf-8").read(); out = []
    for m in re.finditer(r"<text\s([^>]*)>(.*?)</text>", s, re.S):
        a, b = m.group(1), re.sub(r"<[^>]+>", "", m.group(2)); b = html.unescape(b)
        def g(k):
            mm = re.search(k + r'="([^"]*)"', a); return mm.group(1) if mm else ""
        out.append(dict(x=float(g("x") or 0), y=float(g("y") or 0),
                        size=float(g("font-size") or 0), fam=g("font-family"), t=b))
    return out

# ---- Part A: window scan ----
win_flags = []; nostart_lines = []
for pg in PAGES:
    texts = parse(os.path.join(ED, pg + ".svg"))
    # group by x (same column) sorted by y
    byx = {}
    for t in texts: byx.setdefault(round(t["x"], 1), []).append(t)
    for x, lst in byx.items():
        lst.sort(key=lambda z: z["y"])
        for a, b in zip(lst, lst[1:]):
            dy = b["y"] - a["y"]
            if 10 <= dy <= 45 and b["t"] and b["t"][0] in NO_START:
                win_flags.append(dict(page=pg, x=x, dy=round(dy, 2), prev=a["t"], line=b["t"]))
    for t in texts:
        if t["t"] and t["t"][0] in NO_START:
            nostart_lines.append(dict(page=pg, x=t["x"], y=t["y"], line=t["t"]))
R = dict(window_flags=win_flags, window_flag_count=len(win_flags),
         nostart_starting_lines=nostart_lines)

# ---- Part B: wrap-record run ----
sys.path.insert(0, os.path.join(WORK, "reg-ed"))
os.chdir(os.path.join(WORK, "reg-ed"))
import svglib as sv
orig_wrap = sv.wrap
records = []
def rec_wrap(text, kind, bold, size, max_w):
    lines = orig_wrap(text, kind, bold, size, max_w)
    records.append(dict(text=text, lines=list(lines), kind=kind, size=size))
    return lines
sv.wrap = rec_wrap
try:
    import bslib4
    if hasattr(bslib4, "wrap"): bslib4.wrap = rec_wrap
except Exception as e:
    R["bslib_patch_note"] = str(e)
import runpy
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    runpy.run_path(f, run_name="__main__")
R["wrap_calls_recorded"] = len(records)
HANGUL = re.compile(r"[\uac00-\ud7a3]")
HAN = re.compile(r"[\u4e00-\u9fff]")

def dom(text):
    h = len(HANGUL.findall(text)); c = len(HAN.findall(text))
    if h > 0 and h >= c: return "KO"
    if c > 0: return "ZH"
    return "OTHER"

no_start_res = []; splits = []; lone = []
for r in records:
    d = dom(r["text"])
    lines = r["lines"]
    if len(lines) < 2: continue
    for ln in lines[1:]:
        if ln and ln[0] in NO_START:
            no_start_res.append(dict(dom=d, text=r["text"][:60], line=ln))
    # mid-word splits: reconstruct char sequence ignoring spaces
    seq = re.sub(r"\s+", "", r["text"])
    joined = "".join(re.sub(r"\s+", "", ln) for ln in lines)
    if joined != seq:
        continue  # wrap dropped/added something else; skip split analysis for safety
    pos = 0
    for a, b in zip(lines, lines[1:]):
        la = len(re.sub(r"\s+", "", a))
        # char before break and after break in seq
        if pos + la < len(seq) and pos + la > 0:
            before, after = seq[pos + la - 1], seq[pos + la]
            if HANGUL.match(before) and HANGUL.match(after):
                # tail: Hangul run starting at break
                m = HANGUL.match(seq, pos + la)
                # run length: consecutive Hangul from break until non-Hangul
                j = pos + la
                while j < len(seq) and HANGUL.match(seq[j]): j += 1
                tail = j - (pos + la)
                if tail >= 3:
                    splits.append(dict(dom=d, text=r["text"][:80], prev_line=a, next_line=b, tail=tail))
        pos += la
    last = lines[-1].strip()
    if len(last) <= 3:
        lone.append(dict(dom=d, text=r["text"], last=last, nlines=len(lines)))
R["nostart_residuals"] = no_start_res
R["ko_splits_tail_ge3"] = [s for s in splits if s["dom"] == "KO"]
R["all_splits_tail_ge3"] = splits
R["lone_finals"] = lone
R["lone_ko"] = [x for x in lone if x["dom"] == "KO"]
R["lone_zh"] = [x for x in lone if x["dom"] == "ZH"]
json.dump(R, open(os.path.join(WORK, "proof_orphan.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("window_flags:", len(win_flags))
print("nostart_starting_lines:", len(nostart_lines))
for x in nostart_lines: print("  NS:", x)
print("wrap_calls:", len(records))
print("nostart_residuals:", len(no_start_res))
for x in no_start_res: print("  NSR:", x)
print("splits tail>=3 (all):", len(splits), "KO:", len([s for s in splits if s["dom"] == "KO"]))
for x in splits: print("  SPLIT:", x)
print("lone finals total:", len(lone), "KO:", len(R["lone_ko"]), "ZH:", len(R["lone_zh"]))
for x in lone: print("  LONE:", x["dom"], repr(x["last"]), "from:", x["text"][:70])
