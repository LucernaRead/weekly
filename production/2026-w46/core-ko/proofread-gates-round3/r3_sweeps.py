#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Round 3 same-class sweeps from RENDERED text (extraction JSON + P8 keys).
(a) Doubling: every item whose stem contains '___' — suffix = Hangul run
    right after '___'; flag iff the P8 key (first token) endswith suffix.
(b) Quotatives: every '이라고/라고' in stems (reconstructed with key) and
    in ALL rendered prose text; batchim rule on the preceding syllable.
Reads only the Round 3 extraction JSON + p8keys-now JSONs."""
import json, os, re
GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
R3 = os.path.join(GOAL, "hidden_files", "w46", "ko-proofread-gates-round3")
ex = json.load(open(os.path.join(R3, "exercises-all.json"), encoding="utf-8"))
keys = {c: json.load(open(os.path.join(R3, "p8keys-now", c + ".json"), encoding="utf-8"))["keys"]
        for c in ex}

def batchim(syl):
    o = ord(syl)
    return (o - 0xAC00) % 28 != 0 if 0xAC00 <= o <= 0xD7A3 else None

def first_key(k):
    # P8 key strings are like "밀렸어요 — note" or "A — note" or bare key
    m = re.match(r"^(.*?)(?:\s+[—–-]\s+|\s*\(.*)$", k)
    return (m.group(1) if m else k).strip()

# (a) doubling, core stems (Korean stems identical across editions — verify)
core_items = ex["zh-cn"]["items"]
fill = [it for it in core_items if "___" in it["text"]]
print("fill stems (core):", len(fill))
flags = []
for it in fill:
    n = int(it["num"].rstrip(".").split("–")[0])
    key = first_key(keys["zh-cn"][str(n)])
    m = re.search(r"___([\uac00-\ud7a3]+)", it["text"])
    if m:
        suf = m.group(1)
        if key.endswith(suf):
            flags.append((n, it["text"], key, suf))
print("doubling flags:", flags)
# stem identity across editions for fill items: compare only the sentence
# containing the blank (extraction interleaves following-column furniture,
# which legitimately differs by native language — cf. Round 2 artefact note)
for code in ex:
    if code == "zh-cn":
        continue
    mine = {it["num"]: it["text"] for it in ex[code]["items"]}
    for it in fill:
        t = mine[it["num"]]
        kor = re.sub(r"^[^\uac00-\ud7a3]+", "", it["text"])
        i = kor.find("___")
        j = kor.find(".", i)
        stem_sent = kor[:j + 1] if j > 0 else kor
        assert stem_sent in t, (code, it["num"], stem_sent, t)
print("fill stems byte-identical (blank sentence) in all 11 editions: OK")

# (b) quotatives in stems
print("\nquotative stems:")
for it in core_items:
    if "이라고" in it["text"] or "라고" in it["text"]:
        n = int(it["num"].rstrip(".").split("–")[0])
        key = first_key(keys["zh-cn"][str(n)])
        recon = it["text"].replace("___", key)
        print(" ", it["num"], repr(it["text"]), "| key:", key, "| recon:", repr(recon))
        # find particle in recon, check preceding syllable
        for mm in re.finditer(r"(이라고|라고)", recon):
            prev = recon[mm.start()-1] if mm.start() > 0 else ""
            print("    particle", mm.group(1), "prev syllable", prev,
                  "batchim:", batchim(prev), "-> correct:",
                  ("이라고" if batchim(prev) else "라고") == mm.group(1))

# (b2) quotatives in all rendered prose: from fix-verification JSON quot nodes (core)
fv = json.load(open(os.path.join(R3, "fix-verification.json"), encoding="utf-8"))
seen = set()
print("\nall rendered quotative nodes (core, dedup by text):")
for pg, x, y, t in fv["zh-cn"]["quot_nodes"]:
    if t in seen:
        continue
    seen.add(t)
    print(" ", pg, repr(t))
