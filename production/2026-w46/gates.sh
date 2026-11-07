#!/bin/bash
# Fan-out gates for one NL edition. Usage:
#   gates.sh <native> <build-dir-name> [--strict-cjk] [--ko] [--ja]
# Appends all outputs to hidden_files/w46/nl-gates.log and prints a summary.
# Assumes the edition was already built (run.py + render.py done).
set -u
NATIVE="$1"; BUILD="$2"; shift 2
STRICT=""; KO=""; JA=""
for a in "$@"; do case "$a" in --strict-cjk) STRICT="--strict-cjk";; --ko) KO=1;; --ja) JA=1;; esac; done
G=~/workspace/goals/lucernaread-social-media-operations
ED="$G/files/weekly-report-w46-nl-$NATIVE"
CORE="$G/files/weekly-report-w46-nl-core"
LOG="$G/hidden_files/w46/nl-gates.log"
PY="$G/tools/venv/bin/python"
{
echo "===== NL x $NATIVE — $(date -u +%Y-%m-%dT%H:%M:%SZ) ====="
echo "--- occlusion_audit (edition + NEW vs core) ---"
(cd "$G/tools" && ./venv/bin/python occlusion_audit.py "../files/weekly-report-w46-nl-$NATIVE" --core ../files/weekly-report-w46-nl-core; echo "occlusion exit=$?")
echo "--- freeze diff ${STRICT} ---"
(cd "$G/tools" && ./venv/bin/python freeze.py diff --core-svg ../files/weekly-report-w46-nl-core/svg --edition-svg "../files/weekly-report-w46-nl-$NATIVE/svg" $STRICT; echo "freeze exit=$?")
echo "--- p8 compare ---"
(cd "$G/tools" && ./venv/bin/python p8.py compare --core-dir ../files/weekly-report-w46-nl-core --edition-dir "../files/weekly-report-w46-nl-$NATIVE" --target nl; echo "p8 exit=$?")
echo "--- rowcheck (same-baseline + chart GRAZE + gloss counts) ---"
$PY "$G/hidden_files/w46/rowcheck.py" "$ED/svg" "$CORE/svg" "$G/hidden_files/weekly-report-w46-nl-build" "$G/hidden_files/$BUILD"; echo "rowcheck exit=$?"
if [ -n "$KO" ]; then
echo "--- koscan (10-45 window) ---"
cp "$G/hidden_files/weekly-report-w45-nl-ko-build/koscan.py" "$G/hidden_files/w46/koscan.py"
$PY "$G/hidden_files/w46/koscan.py" "$ED/svg" "$G/hidden_files/$BUILD"; echo "koscan exit=$?"
fi
if [ -n "$JA" ]; then
echo "--- jascan (kinsoku line-starts + paren form) ---"
$PY - "$ED/svg" "$G/hidden_files/$BUILD" <<'PYEOF'
import glob, re, sys, os
NO_START=set("、。,.）〕］｝」』】〉》〗〙〛〕〉》)]!}?:;")
n=0
for p in sorted(glob.glob(os.path.join(sys.argv[1],"*.svg"))):
    for m in re.finditer(r'<text[^>]*>([^<]*)</text>', open(p,encoding="utf-8").read()):
        s=m.group(1)
        if s and s[0] in NO_START:
            print("LEAD", os.path.basename(p), repr(s[:30])); n+=1
print("kinsoku line-start hits:", n)
p8=open(os.path.join(sys.argv[1],"p8-toets.svg"),encoding="utf-8").read()
print("half-width ( in P8:", p8.count("("), "full-width （ in P8:", p8.count("（"))
PYEOF
fi
echo "--- web PDF ---"
ls -la "$ED"/*.pdf
} 2>&1 | tee -a "$LOG"
echo "LOGGED to $LOG"
