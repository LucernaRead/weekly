#!/bin/bash
# Round 3 re-gates for de-zh-cn ONLY (W46 DE). Core dir is the unfixed
# Round 2 duplicate: freeze/p8 diffs vs core are EXPECTED to show the
# P8 re-wrap (added CJK must stay 0; p8 keydiff [140] is the fix itself).
# Logs + JSONs land in hidden_files/w46/de-fix-round3/.
set -u
GOAL=~/workspace/goals/lucernaread-social-media-operations
FIX=$GOAL/hidden_files/w46/de-fix-round3
PY=$GOAL/tools/venv/bin/python
FILES=$GOAL/files
CORE_SVG=$FILES/weekly-report-w46-de-core/svg
ED_SVG=$FILES/weekly-report-w46-de-zh-cn/svg

echo "===== FREEZE zh-cn vs core (unfixed duplicate) ====="
$PY $GOAL/tools/freeze.py diff --core-svg "$CORE_SVG" --edition-svg "$ED_SVG" \
  --strict-cjk --json "$FIX/freeze-zh-cn.json" > "$FIX/freeze-zh-cn.log" 2>&1
echo "freeze exit=$?"
echo "===== P8 zh-cn vs core ====="
$PY $GOAL/tools/p8.py compare --core-p8 "$CORE_SVG/p8-uebungen.svg" \
  --edition-p8 "$ED_SVG/p8-uebungen.svg" --total 150 \
  --json "$FIX/p8-zh-cn.json" > "$FIX/p8-zh-cn.log" 2>&1
echo "p8 exit=$?"
echo "===== OCCLUSION zh-cn ====="
$PY $GOAL/tools/occlusion_audit.py "$ED_SVG" --json "$FIX/occlusion-zh-cn.json" > "$FIX/occlusion-zh-cn.log" 2>&1
echo "occlusion exit=$?"
echo "===== COUNTS (proofreader script, zh-cn) ====="
cp $GOAL/hidden_files/w46/de-proofread-gates/count_exercises.py $FIX/count_exercises_run.py
$PY $FIX/count_exercises_run.py $FIX/counts.json > $FIX/counts.log 2>&1
echo "counts exit=$?"
echo "ALL ROUND3 GATES DONE"
