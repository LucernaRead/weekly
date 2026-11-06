#!/bin/bash
# Rebuild W46 RU fan-outs only (run2) after occlusion-fix map patch. Sequential.
GOAL=~/workspace/goals/lucernaread-social-media-operations
PY=$GOAL/tools/venv/bin/python
W46=$GOAL/hidden_files/w46
CORE=$GOAL/hidden_files/weekly-report-w46-ru-build
for n in en de fr es it pt nl ja ko zh-tw; do
  echo "=== $n ==="
  cd $W46 && $PY ru-transform.py $n > $W46/ru-$n-transform2.log 2>&1
  echo "$n transform exit=$?"
  B=$GOAL/hidden_files/weekly-report-w46-ru-$n-build
  cp $CORE/check_core.py $B/check_core.py
  cd $B && $PY run.py > $W46/ru-$n-run2.log 2>&1
  echo "$n run exit=$? overflow=$(grep -c 'OVERFLOW\|TOO WIDE' $W46/ru-$n-run2.log)"
  $PY render.py >> $W46/ru-$n-run2.log 2>&1
  echo "$n render exit=$?"
done
echo "ALL REBUILDS DONE"
