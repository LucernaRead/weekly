# -*- coding: utf-8 -*-
"""keycheck for one rebuilt en edition:
 (a) registry keys vs P8-extracted keys (n=150 short-label exception);
 (b) edition registry keys vs core registry keys (stems are identical
     English, so keys must match 150/150).
"""
import json, os, re, sys

HOME = os.path.expanduser("~")
lang = sys.argv[1]
W = os.path.join(HOME, "workspace/weekly-git/production/2026-w47")
ED = os.path.join(W, f"2026-w47-en-{lang}")
SCR = os.path.join(HOME, "workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-en2/fanout", lang)
reg = json.load(open(os.path.join(ED, "registry.json"), encoding="utf-8"))
core = json.load(open(os.path.join(W, "core-en/registry.json"), encoding="utf-8"))
# The stored p8-extract.json goes stale after any delta rebuild: it still
# held Q73='speak' after the delta set the registry to 'up', so this check
# reported a 148/150 phantom mismatch (run-log L2503). Never trust the
# archive — always re-extract from the edition's LIVE P8 SVG first (and
# write it back, so the archive stays fresh as a side effect). Abort loudly
# if the re-extract fails; a silent fallback to the archive would re-admit
# the phantom.
import subprocess
VENV = os.path.join(HOME, "workspace/weekly-git/tools/venv/bin/python")
P8 = os.path.join(HOME, "workspace/weekly-git/tools/p8.py")
_ext_path = os.path.join(SCR, "p8-extract.json")
_r = subprocess.run([VENV, P8, "extract", "--p8",
                     os.path.join(ED, "svg", "p8-test.svg"), "--total", "150",
                     "--json", _ext_path], capture_output=True, text=True)
if _r.returncode != 0:
    print("FATAL: fresh p8 extract failed:", (_r.stdout + _r.stderr).strip()[-300:])
    sys.exit(2)
ext = json.load(open(_ext_path, encoding="utf-8"))
keys = ext["keys"]

def norm(s):
    return re.sub(r"\s+", " ", str(s)).strip()

exact, mismatch, exc = 0, [], []
for e in reg:
    n = e["n"]
    rk = norm(e["key"])
    pk = norm(keys.get(str(n), ""))
    if rk == pk:
        exact += 1
    elif n == 150 and (rk.startswith(pk) or pk in rk):
        exc.append(n)
    else:
        mismatch.append((n, rk, pk))
print(f"registry-vs-p8extract exact {exact}/150 exc={exc} mismatch={mismatch}")

corekeys = {e["n"]: e["key"] for e in core}
bad = [(e["n"], e["key"], corekeys[e["n"]]) for e in reg if e["key"] != corekeys[e["n"]]]
print(f"registry-keys-vs-core: {150 - len(bad)}/150 match; diff={bad}")
# matching sets vs stems: 38-41 must be b/a/d/c
m = {e["n"]: e["key"] for e in reg}
print("Q38-41:", [m[i] for i in (38, 39, 40, 41)], "expect ['b','a','d','c']")
print("Q125 key:", m[125], "expect A; Q46 key:", m[46], "expect A; Q52:", m[52], "expect hosted; Q55:", m[55], "expect won")
print("Q82/83/84 keys:", m[82], m[83], m[84])
# noted set vs core
print("noted set == core noted:",
      sorted(ext.get("noted_set", [])) == sorted(json.load(open(os.path.join(
          HOME, "workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-en/core-noted-set.json")))))
print("extract keys count:", len(keys), "missing vs registry:",
      sorted(set(range(1, 151)) - set(int(k) for k in keys)) or "none")
