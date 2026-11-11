#!/bin/bash
# es gates after render.py (run from ~ ; venv python)
set -u
V=~/workspace/weekly-git/tools/venv/bin/python
ED=~/workspace/weekly-git/production/2026-w47/2026-w47-en-ru
CORE=~/workspace/weekly-git/production/2026-w47/core-en
S=~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-en/ru
T=~/workspace/weekly-git/tools
echo "== dump_reg =="
$V $ED/dump_reg.py > $S/dump_reg.log 2>&1; echo "dump_reg RC=$?"
# dump_reg.py writes the FRESH registry to scratch-fanout-en2/fanout/ru/registry.json
# (NOT $S/registry.json — that copy went stale: gates.sh once copied a 04:39
# pre-refanout registry over the edition registry and broke make_textmd,
# run-log L2366). Refresh BOTH copies from the real dump location:
REGDUMP=/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-en2/fanout/ru/registry.json
cp $REGDUMP $S/registry.json
cp $REGDUMP $ED/registry.json
$V -c "import json; r=json.load(open('$S/registry.json')); print('registry total', len(r)); from collections import Counter; print('per page', sorted(Counter(e['page'] for e in r).items())); print('levels', Counter(e['level'] for e in r))"
echo "== occlusion =="
$V $T/occlusion_audit.py $ED/svg --json $S/occlusion.json > $S/occlusion.log 2>&1; echo "occlusion RC=$?"; tail -2 $S/occlusion.log
echo "== p8 extract (core + fr) =="
$V $T/p8.py extract --p8 $CORE/svg/p8-test.svg --total 150 --json $S/p8-extract-core.json > $S/p8-extract-core.log 2>&1; echo "core extract RC=$?"
$V $T/p8.py extract --p8 $ED/svg/p8-test.svg --total 150 --json $S/p8-extract.json > $S/p8-extract.log 2>&1; echo "fr extract RC=$?"
$V $T/p8.py compare --core-p8 $CORE/svg/p8-test.svg --edition-p8 $ED/svg/p8-test.svg --total 150 --json $S/p8-compare.json > $S/p8-compare.log 2>&1; echo "compare RC=$?"; cat $S/p8-compare.log; cat $S/p8-compare.json
echo "== p8 extract vs registry =="
$V - "$S" <<'EOF'
import json, sys
S = sys.argv[1]
ex = json.load(open(f"{S}/p8-extract.json"))
reg = json.load(open(f"{S}/registry.json"))
keys = sorted(int(k) for k in ex.get("keys", {}).keys()) if isinstance(ex.get("keys"), dict) else []
print("extract keys:", len(keys), "registry:", len(reg))
print("missing vs registry:", sorted(set(range(1, 151)) - set(keys)) or "none")
print("noted set == core noted:", sorted(ex.get("noted_set", [])) == sorted(json.load(open("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-en/core-noted-set.json"))))
EOF
echo "== freeze baseline =="
$V $T/freeze.py baseline --build $CORE --core-svg $CORE/svg --out $S/freeze-final > $S/freeze.log 2>&1; echo "freeze baseline RC=$?"; cat $S/freeze.log
echo "== freeze direct sha (baseline re-render vs shipped core) =="
$V - <<'EOF'
import hashlib, os, glob
core = "/home/hatch/workspace/weekly-git/production/2026-w47/core-en/svg"
copy = "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-en/ru/freeze-final/build-copy/svg"
ok = 0
for f in sorted(glob.glob(core + "/*.svg")):
    n = os.path.basename(f)
    c = os.path.join(copy, n)
    if not os.path.exists(c):
        print("MISSING in copy:", n); continue
    a = hashlib.sha256(open(f, "rb").read()).hexdigest()
    b = hashlib.sha256(open(c, "rb").read()).hexdigest()
    print(("MATCH " if a == b else "DIFF  ") + n)
    ok += (a == b)
print(f"direct sha256: {ok}/8")
EOF
echo "== freeze diff =="
$V $T/freeze.py diff --core-svg $CORE/svg --edition-svg $ED/svg --json $S/freeze-diff.json > $S/freeze-diff.log 2>&1; echo "freeze diff RC=$?"; cat $S/freeze-diff.log
echo "== webpdf =="
$V $T/webpdf.py $ED/svg $ED/The-Lucerna-VOL4-en-ru.web.pdf > $S/webpdf.log 2>&1; echo "webpdf RC=$?"; tail -3 $S/webpdf.log
echo "== print/web text diff =="
$V - <<'EOF'
import subprocess, collections
def toks(pdf):
    t = subprocess.run(["pdftotext", pdf, "-"], capture_output=True, text=True).stdout
    return collections.Counter(t.split()), len(t)
pc = wc = None
for name, pdf in [("print", "/home/hatch/workspace/weekly-git/production/2026-w47/2026-w47-en-ru/The-Lucerna-VOL4-en-ru.pdf"),
                  ("web", "/home/hatch/workspace/weekly-git/production/2026-w47/2026-w47-en-ru/The-Lucerna-VOL4-en-ru.web.pdf")]:
    c, n = toks(pdf)
    print(name, "chars", n, "distinct tokens", len(c))
    if name == "print": pc = c
    else: wc = c
print("token multiset diff total:", sum((pc - wc).values()) + sum((wc - pc).values()))
print("only in print:", list((pc - wc).items())[:10])
print("only in web:", list((wc - pc).items())[:10])
EOF
echo "== print pdf sha/size =="
sha256sum $ED/The-Lucerna-VOL4-en-ru.pdf; stat -c %s $ED/The-Lucerna-VOL4-en-ru.pdf $ED/The-Lucerna-VOL4-en-ru.web.pdf
echo "== text.md =="
$V $S/make_textmd_w47.py > $S/textmd.log 2>&1; echo "textmd RC=$?"; tail -4 $S/textmd.log
echo DONE
