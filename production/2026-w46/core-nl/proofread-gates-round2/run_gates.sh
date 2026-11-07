#!/bin/bash
# Round 2 independent re-gate: freeze + p8 + occlusion. Logs to round2 dir.
set -u
GOAL=~/workspace/goals/lucernaread-social-media-operations
OUT=$GOAL/hidden_files/w46/nl-proofread-gates-round2
TOOLS=$GOAL/tools
PY=$TOOLS/venv/bin/python
CORE=$GOAL/files/weekly-report-w46-nl-core/svg
cd $TOOLS
echo "=== FREEZE: core self-diff ===" | tee $OUT/gates-freeze-p8.log
$PY freeze.py diff --core-svg $CORE --edition-svg $CORE --json $OUT/freeze-core-self.json 2>&1 | tee -a $OUT/gates-freeze-p8.log; echo "exit=$?" | tee -a $OUT/gates-freeze-p8.log
for ed in de en es fr it pt ru; do
  echo "=== FREEZE strict: $ed ===" | tee -a $OUT/gates-freeze-p8.log
  $PY freeze.py diff --core-svg $CORE --edition-svg $GOAL/files/weekly-report-w46-nl-$ed/svg --strict-cjk --json $OUT/freeze-$ed.json 2>&1 | tee -a $OUT/gates-freeze-p8.log; echo "exit=$?" | tee -a $OUT/gates-freeze-p8.log
done
for ed in ja ko zh-tw; do
  echo "=== FREEZE non-strict: $ed ===" | tee -a $OUT/gates-freeze-p8.log
  $PY freeze.py diff --core-svg $CORE --edition-svg $GOAL/files/weekly-report-w46-nl-$ed/svg --json $OUT/freeze-$ed.json 2>&1 | tee -a $OUT/gates-freeze-p8.log; echo "exit=$?" | tee -a $OUT/gates-freeze-p8.log
done
echo "=== P8 core extract ===" | tee -a $OUT/gates-freeze-p8.log
$PY p8.py extract --p8 $CORE/p8-toets.svg --total 150 --json $OUT/p8-core.json 2>&1 | tee -a $OUT/gates-freeze-p8.log; echo "exit=$?" | tee -a $OUT/gates-freeze-p8.log
for ed in de en es fr it ja ko pt ru zh-tw; do
  echo "=== P8 compare: $ed ===" | tee -a $OUT/gates-freeze-p8.log
  $PY p8.py compare --core-p8 $CORE/p8-toets.svg --edition-p8 $GOAL/files/weekly-report-w46-nl-$ed/svg/p8-toets.svg --total 150 --json $OUT/p8-$ed.json 2>&1 | tee -a $OUT/gates-freeze-p8.log; echo "exit=$?" | tee -a $OUT/gates-freeze-p8.log
done
echo "=== OCCLUSION selftest ===" | tee $OUT/gates-occlusion.log
$PY occlusion_audit.py --selftest 2>&1 | tee -a $OUT/gates-occlusion.log; echo "exit=$?" | tee -a $OUT/gates-occlusion.log
for ed in core de en es fr it ja ko pt ru zh-tw; do
  echo "=== OCCLUSION alone: $ed ===" | tee -a $OUT/gates-occlusion.log
  $PY occlusion_audit.py $GOAL/files/weekly-report-w46-nl-$ed --json $OUT/occlusion-$ed.json 2>&1 | tee -a $OUT/gates-occlusion.log; echo "exit=$?" | tee -a $OUT/gates-occlusion.log
done
for ed in de en es fr it ja ko pt ru zh-tw; do
  echo "=== OCCLUSION vs-core: $ed ===" | tee -a $OUT/gates-occlusion.log
  $PY occlusion_audit.py $GOAL/files/weekly-report-w46-nl-$ed --core $GOAL/files/weekly-report-w46-nl-core --json $OUT/occlusion-$ed-vs-core.json 2>&1 | tee -a $OUT/gates-occlusion.log; echo "exit=$?" | tee -a $OUT/gates-occlusion.log
done
echo "ALL GATES DONE" | tee -a $OUT/gates-occlusion.log
