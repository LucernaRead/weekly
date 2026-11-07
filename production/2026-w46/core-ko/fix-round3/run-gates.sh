#!/bin/bash
# Round 3 re-gates on final artifacts. Outputs under ko-fix-round3/gates/.
# p8 compare uses --target ko (the TARGET language code; Round 1's first
# invocation with --target <edition> failed with FileNotFoundError).
set -u
PY=./venv/bin/python
GOAL=~/workspace/goals/lucernaread-social-media-operations
G=$GOAL/hidden_files/w46/ko-fix-round3/gates
mkdir -p "$G"
cd "$GOAL/tools" || exit 1

echo "=== freeze baseline (core) ==="
$PY freeze.py baseline --build ../hidden_files/weekly-report-w46-ko-build \
  --core-svg ../files/weekly-report-w46-ko-core/svg --out "$G/freeze-baseline" > "$G/freeze-baseline.log" 2>&1
echo "freeze baseline exit=$?"; cat "$G/freeze-baseline.log"

for ed in de en es fr it ja nl pt ru zh-tw; do
  echo "=== freeze diff $ed ==="
  $PY freeze.py diff --core-svg ../files/weekly-report-w46-ko-core/svg \
    --edition-svg ../files/weekly-report-w46-ko-$ed/svg --json "$G/freeze-$ed.json" > "$G/freeze-$ed.log" 2>&1
  echo "freeze diff $ed exit=$?"; cat "$G/freeze-$ed.log"
done

for ed in core de en es fr it ja nl pt ru zh-tw; do
  echo "=== occlusion $ed ==="
  $PY occlusion_audit.py ../files/weekly-report-w46-ko-$ed --json "$G/occlusion-$ed.json" > "$G/occlusion-$ed.log" 2>&1
  echo "occlusion $ed exit=$?"; cat "$G/occlusion-$ed.log"
done
echo "=== occlusion selftest ==="
$PY occlusion_audit.py --selftest > "$G/occlusion-selftest.log" 2>&1
echo "selftest exit=$?"; cat "$G/occlusion-selftest.log"

echo "=== p8 extract core ==="
$PY p8.py extract --p8 ../files/weekly-report-w46-ko-core/svg/p8-siheom.svg --total 150 --json "$G/p8-core.json" > "$G/p8-core.log" 2>&1
echo "p8 core exit=$?"; cat "$G/p8-core.log"
for ed in de en es fr it ja nl pt ru zh-tw; do
  echo "=== p8 compare $ed ==="
  $PY p8.py compare --core-dir ../files/weekly-report-w46-ko-core \
    --edition-dir ../files/weekly-report-w46-ko-$ed --target ko --json "$G/p8-$ed.json" > "$G/p8-$ed.log" 2>&1
  echo "p8 $ed exit=$?"; cat "$G/p8-$ed.log"
done
echo GATES-DONE
