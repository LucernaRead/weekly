#!/bin/bash
# Round 2 independent re-gate driver. Read-only wrt edition files.
BASE=~/workspace/goals/lucernaread-social-media-operations
G=$BASE/hidden_files/w46/zh-tw-proofread-gates-round2
TOOLS=$BASE/tools
PY=$TOOLS/venv/bin/python
CORE=$BASE/files/weekly-report-w46-zhtw-core
LOG=$G/gates-round2.log
exec > >(tee -a "$LOG") 2>&1
echo "ROUND2 GATES START $(date -u +%FT%TZ)"
declare -A DIRS=( [en]=weekly-report-w46-zhtw-core [de]=weekly-report-w46-zh-tw-de [es]=weekly-report-w46-zh-tw-es [fr]=weekly-report-w46-zh-tw-fr [it]=weekly-report-w46-zh-tw-it [ja]=weekly-report-w46-zh-tw-ja [ko]=weekly-report-w46-zh-tw-ko [nl]=weekly-report-w46-zh-tw-nl [pt]=weekly-report-w46-zh-tw-pt [ru]=weekly-report-w46-zh-tw-ru )
for code in en de es fr it ja ko nl pt ru; do
  ED=$BASE/files/${DIRS[$code]}
  echo "===== FREEZE $code ====="
  $PY $TOOLS/freeze.py diff --core-svg $CORE/svg --edition-svg $ED/svg --strict-cjk --json $G/freeze-$code.json > $G/freeze-$code.txt 2>&1; echo "freeze-$code exit=$?"
  cat $G/freeze-$code.txt
  echo "===== P8 $code ====="
  $PY $TOOLS/p8.py compare --core-dir $CORE --edition-dir $ED --target zh-tw --total 150 --json $G/p8-$code.json > $G/p8-$code.txt 2>&1; echo "p8-$code exit=$?"
  cat $G/p8-$code.txt
done
echo "===== P8 CORE EXTRACT ====="
$PY $TOOLS/p8.py extract --p8 $CORE/svg/p8-test.svg --total 150 --json $G/p8-core-extract.json > $G/p8-core-extract.txt 2>&1; echo "p8-core-extract exit=$?"; cat $G/p8-core-extract.txt
for code in en de es fr it ja ko nl pt ru; do
  ED=$BASE/files/${DIRS[$code]}
  echo "===== OCCLUSION $code (standalone) ====="
  $PY $TOOLS/occlusion_audit.py $ED/svg --json $G/occlusion-$code.json > $G/occlusion-$code.txt 2>&1; echo "occlusion-$code exit=$?"
  tail -3 $G/occlusion-$code.txt
  echo "===== OCCLUSION $code (vs core, NEW flags) ====="
  $PY $TOOLS/occlusion_audit.py $ED/svg --core $CORE/svg --json $G/occlusion-new-$code.json > $G/occlusion-new-$code.txt 2>&1; echo "occlusion-new-$code exit=$?"
  tail -3 $G/occlusion-new-$code.txt
done
echo "ROUND2 GATES DONE $(date -u +%FT%TZ)"
