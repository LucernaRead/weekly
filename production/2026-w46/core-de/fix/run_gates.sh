#!/bin/bash
# Re-gate runner for W46 DE fix round. Run AFTER all renders complete.
# Logs + JSONs land in hidden_files/w46/de-fix/.
set -u
GOAL=~/workspace/goals/lucernaread-social-media-operations
FIX=$GOAL/hidden_files/w46/de-fix
PY=$GOAL/tools/venv/bin/python
FILES=$GOAL/files
CORE_SVG=$FILES/weekly-report-w46-de-core/svg

run_gate() {
  local key="$1" dir="$2"
  echo "===== FREEZE $key ====="
  $PY $GOAL/tools/freeze.py diff --core-svg "$CORE_SVG" --edition-svg "$FILES/$dir/svg" \
    --strict-cjk --json "$FIX/freeze-$key.json" > "$FIX/freeze-$key.log" 2>&1
  echo "freeze exit=$? (see freeze-$key.log)"
  echo "===== P8 $key ====="
  $PY $GOAL/tools/p8.py compare --core-p8 "$CORE_SVG/p8-uebungen.svg" \
    --edition-p8 "$FILES/$dir/svg/p8-uebungen.svg" --total 150 \
    --json "$FIX/p8-$key.json" > "$FIX/p8-$key.log" 2>&1
  echo "p8 exit=$? (see p8-$key.log)"
  echo "===== OCCLUSION $key ====="
  $PY $GOAL/tools/occlusion_audit.py "$FILES/$dir/svg" --json "$FIX/occlusion-$key.json" > "$FIX/occlusion-$key.log" 2>&1
  echo "occlusion exit=$? (see occlusion-$key.log)"
}

for spec in "core:weekly-report-w46-de-core" "en:weekly-report-w46-de-en" "es:weekly-report-w46-de-es" \
  "fr:weekly-report-w46-de-fr" "it:weekly-report-w46-de-it" "ja:weekly-report-w46-de-ja" \
  "ko:weekly-report-w46-de-ko" "nl:weekly-report-w46-de-nl" "pt:weekly-report-w46-de-pt" \
  "ru:weekly-report-w46-de-ru" "zh-cn:weekly-report-w46-de-zh-cn" "zh-tw:weekly-report-w46-de-zh-tw"; do
  key="${spec%%:*}"; dir="${spec#*:}"
  run_gate "$key" "$dir"
done

echo "===== COUNTS ====="
cp $GOAL/hidden_files/w46/de-proofread-gates/count_exercises.py $FIX/count_exercises_run.py
$PY $FIX/count_exercises_run.py $FIX/counts.json > $FIX/counts.log 2>&1
echo "counts exit=$?"

echo "===== PDF TEXT ====="
$PY $FIX/pdf_text_check.py > $FIX/pdf-text.log 2>&1
echo "pdf-text exit=$?"
echo "ALL GATES DONE"
