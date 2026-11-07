#!/bin/bash
G=~/workspace/goals/lucernaread-social-media-operations
FIX=$G/hidden_files/w46/zh-tw-fix
OUT=$FIX/gates
PY=$G/tools/venv/bin/python
cd $G/tools || exit 1
run_occl() {
  c=$1; dir=$2
  echo "=== $c occlusion ===" | tee -a $OUT/gates.log
  $PY occlusion_audit.py $dir --json $OUT/occlusion-$c.json > $OUT/occlusion-$c.txt 2>&1; echo "occlusion-$c rc=$?" | tee -a $OUT/gates.log
  cat $OUT/occlusion-$c.txt | tee -a $OUT/gates.log
  echo "=== $c occlusion NEW vs core ===" | tee -a $OUT/gates.log
  $PY occlusion_audit.py $dir --core ../files/weekly-report-w46-zhtw-core --json $OUT/occlusion-new-$c.json > $OUT/occlusion-new-$c.txt 2>&1; echo "occlusion-new-$c rc=$?" | tee -a $OUT/gates.log
  cat $OUT/occlusion-new-$c.txt | tee -a $OUT/gates.log
}
run_occl nl ../files/weekly-report-w46-zh-tw-nl
for c in pt ru; do
  echo "=== $c freeze diff --strict-cjk ===" | tee -a $OUT/gates.log
  $PY freeze.py diff --core-svg ../files/weekly-report-w46-zhtw-core/svg --edition-svg ../files/weekly-report-w46-zh-tw-$c/svg --strict-cjk --json $OUT/freeze-$c.json > $OUT/freeze-$c.txt 2>&1; echo "freeze-$c rc=$?" | tee -a $OUT/gates.log
  cat $OUT/freeze-$c.txt | tee -a $OUT/gates.log
  echo "=== $c p8 compare ===" | tee -a $OUT/gates.log
  $PY p8.py compare --core-dir ../files/weekly-report-w46-zhtw-core --edition-dir ../files/weekly-report-w46-zh-tw-$c --target zh-tw --json $OUT/p8-$c.json > $OUT/p8-$c.txt 2>&1; echo "p8-$c rc=$?" | tee -a $OUT/gates.log
  cat $OUT/p8-$c.txt | tee -a $OUT/gates.log
  run_occl $c ../files/weekly-report-w46-zh-tw-$c
done
echo "=== core (en) p8 extract + occlusion ===" | tee -a $OUT/gates.log
$PY p8.py extract --p8 ../files/weekly-report-w46-zhtw-core/svg/p8-test.svg --total 150 --json $OUT/p8-en.json > $OUT/p8-en.txt 2>&1; echo "p8-en rc=$?" | tee -a $OUT/gates.log
cat $OUT/p8-en.txt | tee -a $OUT/gates.log
$PY occlusion_audit.py ../files/weekly-report-w46-zhtw-core --json $OUT/occlusion-en.json > $OUT/occlusion-en.txt 2>&1; echo "occlusion-en rc=$?" | tee -a $OUT/gates.log
cat $OUT/occlusion-en.txt | tee -a $OUT/gates.log
echo "GATES REST DONE"
