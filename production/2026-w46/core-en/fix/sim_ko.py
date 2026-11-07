import sys, os, runpy, re
from itertools import groupby
BD = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-en-ko-build")
sys.path.insert(0, BD)
os.chdir(BD)
for f in ["content12.py","content34.py","content56.py","content7.py","content8.py"]:
    runpy.run_path(os.path.join(BD,f), run_name="__main__")
import bslib4
from svglib import wrap, text_w

PRINT_NOTES = [8, 9, 15, 23, 31, 32, 37, 39, 48, 50, 55, 57, 67, 68, 72, 82, 83, 84, 85, 86, 87, 89, 90, 92, 103, 104, 106, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]

def build_paras(reg, overrides=None):
    paras = {}
    for pg, grp in groupby(reg, key=lambda e: e["page"]):
        parts = []
        for e in grp:
            ee = dict(e)
            if overrides and ee["n"] in overrides:
                ee["note"] = overrides[ee["n"]]
            s = f"{ee['n']}. {ee['key']}"
            if ee["note"] and (pg == 8 or ee["n"] in PRINT_NOTES):
                s += f" ({ee['note']})"
            parts.append(s)
        paras[pg] = " · ".join(parts)
    return paras

def tokenize(text):
    tokens, buf = [], ""
    for ch in text:
        if ord(ch) < 0x2E80 and ch != " ":
            buf += ch
        else:
            if buf: tokens.append(buf); buf = ""
            tokens.append(ch)
    if buf: tokens.append(buf)
    return tokens

def wrap_tokens(text, kind, bold, size, max_w):
    toks = tokenize(text)
    lines, cur, cur_toks = [], "", []
    for tok in toks:
        trial = cur + tok
        if text_w(trial, kind, bold, size) <= max_w or not cur.strip():
            cur = trial; cur_toks.append(tok)
        else:
            lines.append((cur.rstrip(), list(cur_toks)))
            cur = tok.lstrip() if tok == " " else tok
            cur_toks = [cur] if cur else []
    if cur.strip():
        lines.append((cur.rstrip(), list(cur_toks)))
    return lines

def scan(text, label):
    lines = wrap_tokens(text, "sans", False, 15.5, 434)
    # word runs: consecutive tokens with no " " token between; track per-line token lists
    # Build global token stream with line index per token
    splits = []
    # reconstruct: for each line, tokens; a run continues across lines if prev line's last token != " " and next line's first token != " "
    for i in range(len(lines)-1):
        lt, nt = lines[i][1], lines[i+1][1]
        if not lt or not nt: continue
        if lt[-1] == " " or nt[0] == " ": continue
        # mid-run break: find run start (walk back) and run end (walk fwd) in token stream
        # tail = tokens of this run on next line until a space token or run end
        tail_toks = []
        for t in nt:
            if t == " ": break
            tail_toks.append(t)
        tail_str = "".join(tail_toks)
        tail_syl = sum(1 for ch in tail_str if 0xAC00 <= ord(ch) <= 0xD7A3)
        head_str = "".join(lt)
        splits.append((i, tail_syl, head_str[-12:], tail_str[:12]))
    return lines, splits

paras = build_paras(bslib4.REG)
for pg in (5, 8):
    lines, splits = scan(paras[pg], f"p{pg}")
    print(f"=== page {pg}: {len(lines)} lines, splits={len(splits)}")
    for i, ts, h, t in splits:
        flag = "S3" if ts >= 3 else "ok"
        print(f"  line{i}->{i+1} tail={ts} [{flag}] ...{h!r} | {t!r}")

# candidates
cands1 = {
 "C1 가": "갈라쇼가 솔퍼드에서 생방송돼요",
 "C2 모금": "모금 갈라쇼는 솔퍼드에서 생방송돼요",
 "C3 영국": "갈라쇼는 영국 솔퍼드에서 생방송돼요",
}
cands2 = {
 "D1 동안": "전교생이 2분 동안 묵념해요",
 "D2 모두": "전교생 모두 2분간 묵념해요",
 "D5 온": "온 전교생이 2분간 묵념해요",
 "D6 조용히": "전교생이 2분간 조용히 묵념해요",
 "D3 묵념을": "전교생이 2분간 묵념을 해요",
}
# entry numbers: find them
for e in bslib4.REG:
    if e["note"] in ("갈라쇼는 솔퍼드에서 생방송돼요", "전교생이 2분간 묵념해요"):
        print("ENTRY", e["n"], e["page"], repr(e["note"]))
print("--- candidates for #68 (page 5 para) ---")
for name, note in cands1.items():
    p2 = build_paras(bslib4.REG, {68: note})
    lines, splits = scan(p2[5], "c")
    s3 = [s for s in splits if s[1] >= 3]
    print(f"{name}: lines={len(lines)} splits={[(s[1], s[3]) for s in splits]} S3={len(s3)}")
print("--- candidates for #130 (page 8 para) ---")
for name, note in cands2.items():
    p2 = build_paras(bslib4.REG, {130: note})
    lines, splits = scan(p2[8], "c")
    s3 = [s for s in splits if s[1] >= 3]
    print(f"{name}: lines={len(lines)} splits={[(s[1], s[3]) for s in splits]} S3={len(s3)}")
