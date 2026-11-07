#!/bin/bash
# W46 zh-tw fix re-gates: freeze baseline (core) + freeze diff (fan-outs, --strict-cjk)
# + p8 compare + occlusion audit (selftest + per-edition + NEW vs core) + webpdf + text.md
# Logs + JSONs to hidden_files/w46/zh-tw-fix/gates/
G=~/workspace/goals/lucernaread-social-media-operations
FIX=$G/hidden_files/w46/zh-tw-fix
OUT=$FIX/gates
PY=$G/tools/venv/bin/python
mkdir -p $OUT
cd $G/tools || exit 1
echo "=== occlusion selftest ===" | tee $OUT/gates.log
$PY occlusion_audit.py --selftest 2>&1 | tee -a $OUT/gates.log
echo "=== freeze baseline (core reproduction) ===" | tee -a $OUT/gates.log
$PY freeze.py baseline --build ../hidden_files/weekly-report-w46-zhtw-build --core-svg ../files/weekly-report-w46-zhtw-core/svg --out scratch/fix-baseline-w46-zhtw-core > $OUT/freeze-baseline.log 2>&1; echo "baseline rc=$?" | tee -a $OUT/gates.log
tail -n 15 $OUT/freeze-baseline.log | tee -a $OUT/gates.log
for c in de es fr it ja ko nl pt ru; do
  echo "=== $c freeze diff --strict-cjk ===" | tee -a $OUT/gates.log
  $PY freeze.py diff --core-svg ../files/weekly-report-w46-zhtw-core/svg --edition-svg ../files/weekly-report-w46-zh-tw-$c/svg --strict-cjk --json $OUT/freeze-$c.json > $OUT/freeze-$c.txt 2>&1; echo "freeze-$c rc=$?" | tee -a $OUT/gates.log
  cat $OUT/freeze-$c.txt | tee -a $OUT/gates.log
  echo "=== $c p8 compare ===" | tee -a $OUT/gates.log
  $PY p8.py compare --core-dir ../files/weekly-report-w46-zhtw-core --edition-dir ../files/weekly-report-w46-zh-tw-$c --target zh-tw --json $OUT/p8-$c.json > $OUT/p8-$c.txt 2>&1; echo "p8-$c rc=$?" | tee -a $OUT/gates.log
  cat $OUT/p8-$c.txt | tee -a $OUT/gates.log
  echo "=== $c occlusion ===" | tee -a $OUT/gates.log
  $PY occlusion_audit.py ../files/weekly-report-w46-zh-tw-$c --json $OUT/occlusion-$c.json > $OUT/occlusion-$c.txt 2>&1; echo "occlusion-$c rc=$?" | tee -a $OUT/gates.log
  cat $OUT/occlusion-$c.txt | tee -a $OUT/gates.log
  echo "=== $c occlusion NEW vs core ===" | tee -a $OUT/gates.log
  $PY occlusion_audit.py ../files/weekly-report-w46-zh-tw-$c --core ../files/weekly-report-w46-zhtw-core --json $OUT/occlusion-new-$c.json > $OUT/occlusion-new-$c.txt 2>&1; echo "occlusion-new-$c rc=$?" | tee -a $OUT/gates.log
  cat $OUT/occlusion-new-$c.txt | tee -a $OUT/gates.log
done
echo "=== core (en) p8 extract + occlusion ===" | tee -a $OUT/gates.log
$PY p8.py extract --p8 ../files/weekly-report-w46-zhtw-core/svg/p8-test.svg --total 150 --json $OUT/p8-en.json > $OUT/p8-en.txt 2>&1; echo "p8-en rc=$?" | tee -a $OUT/gates.log
cat $OUT/p8-en.txt | tee -a $OUT/gates.log
$PY occlusion_audit.py ../files/weekly-report-w46-zhtw-core --json $OUT/occlusion-en.json > $OUT/occlusion-en.txt 2>&1; echo "occlusion-en rc=$?" | tee -a $OUT/gates.log
cat $OUT/occlusion-en.txt | tee -a $OUT/gates.log
echo "GATES PART 1 DONE"
