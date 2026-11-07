#!/bin/bash
# Rebuild W46 RU fan-outs round 3 (disc/geometry/orphan fixes). Sequential.
GOAL=~/workspace/goals/lucernaread-social-media-operations
PY=$GOAL/tools/venv/bin/python
W46=$GOAL/hidden_files/w46
CORE=$GOAL/hidden_files/weekly-report-w46-ru-build
for n in en de fr pt ja ko zh-tw; do
  echo "=== $n ==="
  cd $W46 && $PY ru-transform.py $n > $W46/ru-$n-transform3.log 2>&1
  echo "$n transform exit=$?"
  B=$GOAL/hidden_files/weekly-report-w46-ru-$n-build
  cp $CORE/check_core.py $B/check_core.py
  cd $B && $PY run.py > $W46/ru-$n-run3.log 2>&1
  echo "$n run exit=$? overflow=$(grep -c 'OVERFLOW\|TOO WIDE' $W46/ru-$n-run3.log)"
  $PY render.py >> $W46/ru-$n-run3.log 2>&1
  echo "$n render exit=$?"
done
echo "ALL REBUILDS DONE"
