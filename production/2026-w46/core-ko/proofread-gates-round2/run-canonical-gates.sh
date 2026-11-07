#!/bin/bash
# Round 2 canonical re-gates. Run from tools/ dir with venv python.
set -u
G=~/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/ko-proofread-gates-round2
B=~/workspace/goals/lucernaread-social-media-operations/files
PY=./venv/bin/python
cd ~/workspace/goals/lucernaread-social-media-operations/tools || exit 1
echo "=== freeze baseline ==="
$PY freeze.py baseline --build ../hidden_files/weekly-report-w46-ko-build \
  --core-svg ../files/weekly-report-w46-ko-core/svg --out "$G/freeze-baseline" >"$G/freeze-baseline.log" 2>&1
echo "baseline exit=$?"
cat "$G/freeze-baseline.log"
for E in de en es fr it ja nl pt ru zh-tw; do
  D=weekly-report-w46-ko-$E
  $PY freeze.py diff --core-svg ../files/weekly-report-w46-ko-core/svg \
    --edition-svg ../files/$D/svg --json "$G/freeze-$E.json" >"$G/freeze-$E.log" 2>&1
  echo "freeze $E exit=$?"
done
echo "=== p8 compares (target ko) ==="
$PY p8.py compare --core-dir ../files/weekly-report-w46-ko-core \
  --edition-dir ../files/weekly-report-w46-ko-core --target ko --json "$G/p8-core.json" >"$G/p8-core.log" 2>&1
echo "p8 core exit=$?"
for E in de en es fr it ja nl pt ru zh-tw; do
  D=weekly-report-w46-ko-$E
  $PY p8.py compare --core-dir ../files/weekly-report-w46-ko-core \
    --edition-dir ../files/$D --target ko --json "$G/p8-$E.json" >"$G/p8-$E.log" 2>&1
  echo "p8 $E exit=$?"
done
echo "=== occlusion ==="
$PY occlusion_audit.py --selftest >"$G/occlusion-selftest.log" 2>&1
echo "selftest exit=$?"
for D in weekly-report-w46-ko-core weekly-report-w46-ko-de weekly-report-w46-ko-en weekly-report-w46-ko-es weekly-report-w46-ko-fr weekly-report-w46-ko-it weekly-report-w46-ko-ja weekly-report-w46-ko-nl weekly-report-w46-ko-pt weekly-report-w46-ko-ru weekly-report-w46-ko-zh-tw; do
  S=${D#weekly-report-w46-ko-}
  [ "$S" = "core" ] && S=zh-cn
  $PY occlusion_audit.py ../files/$D --json "$G/occlusion-$S.json" >"$G/occlusion-$S.log" 2>&1
  echo "occlusion $S exit=$?"
done
echo DONE
