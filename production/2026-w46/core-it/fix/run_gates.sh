#!/bin/bash
# Re-run ALL shared gates on all 11 W46 IT editions after fixes.
# Outputs to hidden_files/w46/it-fix/. Usage: bash run_gates.sh
BASE=~/workspace/goals/lucernaread-social-media-operations
G="$BASE/hidden_files/w46/it-fix"
cd "$BASE/tools"
PY=./venv/bin/python
CORE="$BASE/files/weekly-report-w46-it-core"
declare -A DIRS=( [de]=weekly-report-w46-it-de [en]=weekly-report-w46-it-en [es]=weekly-report-w46-it-es [fr]=weekly-report-w46-it-fr [ja]=weekly-report-w46-it-ja [ko]=weekly-report-w46-it-ko [nl]=weekly-report-w46-it-nl [pt]=weekly-report-w46-it-pt [ru]=weekly-report-w46-it-ru [zh-cn]=weekly-report-w46-it-core [zh-tw]=weekly-report-w46-it-zh-tw )
for n in de en es fr ja ko nl pt ru zh-cn zh-tw; do
  ED="$BASE/files/${DIRS[$n]}"
  echo "===== $n ($ED) ====="
  echo "--- freeze ---"
  $PY freeze.py diff --core-svg "$CORE/svg" --edition-svg "$ED/svg" --json "$G/freeze-$n.json" 2>&1 | tee "$G/freeze-$n.log"
  echo "--- p8 ---"
  $PY p8.py compare --core-dir "$CORE" --edition-dir "$ED" --target it --json "$G/p8-$n.json" 2>&1 | tee "$G/p8-$n.log"; echo "p8 exit=$?"
  echo "--- occlusion ---"
  $PY occlusion_audit.py "$ED/svg" --json "$G/occlusion-$n.json" 2>&1 | tee "$G/occlusion-$n.log"; echo "occl exit=$?"
done
echo GATESDONE
