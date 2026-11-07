#!/bin/bash
# Round 3 independent gates — re-run, do not trust fix worker outputs.
set -u
ROOT=~/workspace/goals/lucernaread-social-media-operations
GATE=$ROOT/hidden_files/w46/zh-cn-proofread-gates-round3
TOOLS=$ROOT/tools
PY=$TOOLS/venv/bin/python
CORE=$ROOT/files/weekly-report-w46-zh-cn-core
mkdir -p "$GATE"
exec > "$GATE/run_gates_r3.out" 2>&1
echo "=== occlusion selftest ==="
$PY $TOOLS/occlusion_audit.py --selftest; echo "selftest exit=$?"
for lang in en de es fr it ja ko nl pt ru; do
  if [ "$lang" = en ]; then ED=$CORE; else ED=$ROOT/files/weekly-report-w46-zh-cn-$lang; fi
  echo "===== $lang : $ED ====="
  $PY $TOOLS/occlusion_audit.py "$ED" --json "$GATE/occlusion-$lang.json" > "$GATE/occlusion-$lang.log" 2>&1; echo "occlusion exit=$? : $(cat $GATE/occlusion-$lang.log | tail -c 300)"
  $PY $TOOLS/freeze.py diff --core-svg "$CORE/svg" --edition-svg "$ED/svg" --strict-cjk --json "$GATE/freeze-$lang.json" > "$GATE/freeze-$lang.log" 2>&1; echo "freeze(strict-cjk) exit=$? : $(head -c 1200 $GATE/freeze-$lang.log)"
  $PY $TOOLS/p8.py extract --p8 "$ED/svg/p8-ceyan.svg" --total 150 --json "$GATE/p8-extract-$lang.json" > "$GATE/p8-extract-$lang.log" 2>&1; echo "p8 extract exit=$? : $(head -c 300 $GATE/p8-extract-$lang.log)"
  $PY $TOOLS/p8.py compare --core-p8 "$CORE/svg/p8-ceyan.svg" --edition-p8 "$ED/svg/p8-ceyan.svg" --total 150 --json "$GATE/p8-$lang.json" > "$GATE/p8-$lang.log" 2>&1; echo "p8 compare exit=$? : $(head -c 400 $GATE/p8-$lang.log)"
done
echo "ALL GATES DONE"
