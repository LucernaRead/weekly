#!/bin/bash
set -u
ROOT=~/workspace/goals/lucernaread-social-media-operations
G=$ROOT/hidden_files/w46/zh-cn-proofread-gates-round2
PY=$ROOT/tools/venv/bin/python
CORE_DIR=$ROOT/files/weekly-report-w46-zh-cn-core
SUMMARY=$G/gates-summary.txt
: > "$SUMMARY"
echo "=== occlusion selftest ===" | tee -a "$SUMMARY"
$PY $ROOT/tools/occlusion_audit.py --selftest > "$G/occlusion-selftest.log" 2>&1
echo "selftest exit=$?" | tee -a "$SUMMARY"
cat "$G/occlusion-selftest.log" | tee -a "$SUMMARY"
for lang in en de es fr it ja ko nl pt ru; do
  if [ "$lang" = en ]; then ED=$CORE_DIR; else ED=$ROOT/files/weekly-report-w46-zh-cn-$lang; fi
  echo "===== $lang : $ED =====" | tee -a "$SUMMARY"
  $PY $ROOT/tools/occlusion_audit.py "$ED" --json "$G/occlusion-$lang.json" > "$G/occlusion-$lang.log" 2>&1
  echo "occlusion exit=$? : $(tail -n 1 "$G/occlusion-$lang.log")" | tee -a "$SUMMARY"
  $PY $ROOT/tools/freeze.py diff --core-svg "$CORE_DIR/svg" --edition-svg "$ED/svg" --strict-cjk --json "$G/freeze-$lang.json" > "$G/freeze-$lang.log" 2>&1
  echo "freeze(strict-cjk) exit=$? : $(grep -iE 'added|TOTAL' "$G/freeze-$lang.log" | head -n 4 | tr '\n' ' ')" | tee -a "$SUMMARY"
  $PY $ROOT/tools/p8.py extract --p8 "$ED/svg/p8-ceyan.svg" --total 150 --json "$G/p8-extract-$lang.json" > "$G/p8-extract-$lang.log" 2>&1
  echo "p8 extract exit=$? : $(head -n 3 "$G/p8-extract-$lang.log" | tr '\n' ' ')" | tee -a "$SUMMARY"
  $PY $ROOT/tools/p8.py compare --core-p8 "$CORE_DIR/svg/p8-ceyan.svg" --edition-p8 "$ED/svg/p8-ceyan.svg" --total 150 --json "$G/p8-$lang.json" > "$G/p8-$lang.log" 2>&1
  echo "p8 compare exit=$? : $(head -n 3 "$G/p8-$lang.log" | tr '\n' ' ')" | tee -a "$SUMMARY"
done
echo "GATES DONE" | tee -a "$SUMMARY"
