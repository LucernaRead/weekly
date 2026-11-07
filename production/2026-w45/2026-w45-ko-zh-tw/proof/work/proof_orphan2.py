# -*- coding: utf-8 -*-
"""Orphan wrap analysis v2 (fixed): mid-word = break with NO space in the
original text between the two chars (adjacent original indices); dom by
character counts, not run counts; dedup by (text, last)."""
import re, os, sys, json
GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
WORK = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(WORK, "reg-ed"))
os.chdir(os.path.join(WORK, "reg-ed"))
import svglib as sv
orig_wrap = sv.wrap
records = []
def rec_wrap(text, kind, bold, size, max_w):
    lines = orig_wrap(text, kind, bold, size, max_w)
    records.append(dict(text=text, lines=list(lines)))
    return lines
sv.wrap = rec_wrap
import bslib4
if hasattr(bslib4, "wrap"): bslib4.wrap = rec_wrap
import runpy
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    runpy.run_path(f, run_name="__main__")
NO_START = set("。、，．！？：；）」』】ー…‥・)]}〉》.,!?%:;\"")
def is_hangul(ch): return "\uac00" <= ch <= "\ud7a3"
def is_han(ch): return "\u4e00" <= ch <= "\u9fff"
def dom(text):
    h = sum(1 for ch in text if is_hangul(ch)); c = sum(1 for ch in text if is_han(ch))
    if h > 0 and h >= c: return "KO"
    if c > 0: return "ZH"
    return "OTHER"
no_start_res = []; splits = []; lone = []
for r in records:
    d = dom(r["text"]); lines = r["lines"]
    if len(lines) < 2: continue
    for ln in lines[1:]:
        if ln and ln[0] in NO_START:
            no_start_res.append(dict(dom=d, text=r["text"], line=ln))
    # nospace sequence with original indices
    seq = [(ch, i) for i, ch in enumerate(r["text"]) if not ch.isspace()]
    joined = "".join(re.sub(r"\s+", "", ln) for ln in lines)
    if joined != "".join(ch for ch, _ in seq):
        continue
    pos = 0
    for a, b in zip(lines, lines[1:]):
        la = len(re.sub(r"\s+", "", a))
        if 0 < pos + la < len(seq):
            ch_before, idx_before = seq[pos + la - 1]
            ch_after, idx_after = seq[pos + la]
            if is_hangul(ch_before) and is_hangul(ch_after) and idx_after == idx_before + 1:
                j = pos + la
                while j < len(seq) and is_hangul(seq[j][0]) and (j == pos + la or seq[j][1] == seq[j - 1][1] + 1):
                    j += 1
                tail = j - (pos + la)
                if tail >= 3:
                    splits.append(dict(dom=d, text=r["text"], prev_line=a, next_line=b, tail=tail))
        pos += la
    last = lines[-1].strip()
    if len(last) <= 3:
        lone.append(dict(dom=d, text=r["text"], last=last))
def dedup(lst, key):
    seen = set(); out = []
    for x in lst:
        k = key(x)
        if k not in seen: seen.add(k); out.append(x)
    return out
R = dict(wrap_calls=len(records),
         nostart_residuals=dedup(no_start_res, lambda x: (x["text"], x["line"])),
         splits_tail_ge3=dedup(splits, lambda x: (x["text"], x["prev_line"], x["next_line"])),
         splits_ko=[x for x in dedup(splits, lambda x: (x["text"], x["prev_line"], x["next_line"])) if x["dom"] == "KO"],
         lone_dedup=dedup(lone, lambda x: (x["text"], x["last"])),
         lone_ko=dedup([x for x in lone if x["dom"] == "KO"], lambda x: (x["text"], x["last"])),
         lone_zh=dedup([x for x in lone if x["dom"] == "ZH"], lambda x: (x["text"], x["last"])))
json.dump(R, open(os.path.join(WORK, "proof_orphan2.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("wrap_calls:", R["wrap_calls"])
print("nostart_residuals dedup:", len(R["nostart_residuals"]))
for x in R["nostart_residuals"]: print("  NSR:", x)
print("splits tail>=3 dedup:", len(R["splits_tail_ge3"]), "KO:", len(R["splits_ko"]))
for x in R["splits_ko"]: print("  SPLIT-KO:", x)
print("lone dedup total:", len(R["lone_dedup"]), "KO:", len(R["lone_ko"]), "ZH:", len(R["lone_zh"]))
for x in R["lone_ko"]: print("  LONE-KO:", repr(x["last"]), "from:", x["text"][:60])
for x in R["lone_zh"]: print("  LONE-ZH:", repr(x["last"]), "from:", x["text"][:60])
