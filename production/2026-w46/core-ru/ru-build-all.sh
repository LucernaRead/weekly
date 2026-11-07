#!/bin/bash
# Rebuild W46 RU core + all fan-outs after the E3-key fix. Sequential.
GOAL=~/workspace/goals/lucernaread-social-media-operations
PY=$GOAL/tools/venv/bin/python
W46=$GOAL/hidden_files/w46
CORE=$GOAL/hidden_files/weekly-report-w46-ru-build

echo "=== CORE ==="
cd $CORE && $PY run.py > $W46/ru-core-run6.log 2>&1
echo "core run exit=$? overflow=$(grep -c 'OVERFLOW\|TOO WIDE' $W46/ru-core-run6.log)"
$PY render.py >> $W46/ru-core-run6.log 2>&1
echo "core render exit=$?"

for n in en de fr es it pt nl ja ko zh-tw; do
  echo "=== $n ==="
  cd $W46 && $PY ru-transform.py $n > $W46/ru-$n-transform.log 2>&1
  echo "$n transform exit=$?"
  B=$GOAL/hidden_files/weekly-report-w46-ru-$n-build
  cp $CORE/check_core.py $B/check_core.py
  cd $B && $PY run.py > $W46/ru-$n-run1.log 2>&1
  echo "$n run exit=$? overflow=$(grep -c 'OVERFLOW\|TOO WIDE' $W46/ru-$n-run1.log)"
  $PY render.py >> $W46/ru-$n-run1.log 2>&1
  echo "$n render exit=$?"
done
echo "ALL BUILDS DONE"
