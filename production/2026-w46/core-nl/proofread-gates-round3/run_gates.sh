#!/bin/bash
# Round 3 independent gates. Run from tools dir with ./venv/bin/python.
set -u
G=~/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/nl-proofread-gates-round3
F=~/workspace/goals/lucernaread-social-media-operations/files
cd ~/workspace/goals/lucernaread-social-media-operations/tools
PY=./venv/bin/python
{
echo "=== FREEZE: core self-diff ==="
$PY freeze.py diff --core-svg $F/weekly-report-w46-nl-core/svg --edition-svg $F/weekly-report-w46-nl-core/svg --json $G/freeze-core-self.json; echo "exit=$?"
for ed in de en es fr it pt ru; do
  echo "=== FREEZE strict: $ed ==="
  $PY freeze.py diff --core-svg $F/weekly-report-w46-nl-core/svg --edition-svg $F/weekly-report-w46-nl-$ed/svg --strict-cjk --json $G/freeze-$ed.json; echo "exit=$?"
done
for ed in ja ko zh-tw; do
  echo "=== FREEZE: $ed ==="
  $PY freeze.py diff --core-svg $F/weekly-report-w46-nl-core/svg --edition-svg $F/weekly-report-w46-nl-$ed/svg --json $G/freeze-$ed.json; echo "exit=$?"
done
echo "=== P8 core extract ==="
$PY p8.py extract --p8 $F/weekly-report-w46-nl-core/svg/p8-toets.svg --total 150 --json $G/p8-core.json; echo "exit=$?"
for ed in de en es fr it ja ko pt ru zh-tw; do
  echo "=== P8 compare: $ed ==="
  $PY p8.py compare --core-p8 $F/weekly-report-w46-nl-core/svg/p8-toets.svg --edition-p8 $F/weekly-report-w46-nl-$ed/svg/p8-toets.svg --total 150 --json $G/p8-$ed.json; echo "exit=$?"
  $PY p8.py extract --p8 $F/weekly-report-w46-nl-$ed/svg/p8-toets.svg --total 150 --json $G/p8-extract-$ed.json; echo "extract exit=$?"
done
} 2>&1 | tee $G/gates-freeze-p8.log
{
echo "=== OCCLUSION selftest ==="
$PY occlusion_audit.py --selftest; echo "exit=$?"
for ed in core de en es fr it ja ko pt ru zh-tw; do
  echo "=== OCCLUSION alone: $ed ==="
  $PY occlusion_audit.py $F/weekly-report-w46-nl-$ed/svg --json $G/occlusion-$ed.json; echo "exit=$?"
done
for ed in de en es fr it ja ko pt ru zh-tw; do
  echo "=== OCCLUSION vs-core: $ed ==="
  $PY occlusion_audit.py $F/weekly-report-w46-nl-$ed/svg --core $F/weekly-report-w46-nl-core/svg --json $G/occlusion-$ed-vs-core.json; echo "exit=$?"
done
} 2>&1 | tee $G/gates-occlusion.log
echo DONE
