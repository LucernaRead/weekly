#!/bin/bash
# W46 RU fix rebuild: core + all fan-outs, sequential. Logs to ru-fix/logs/.
set -u
GOAL=~/workspace/goals/lucernaread-social-media-operations
PY=$GOAL/tools/venv/bin/python
W46=$GOAL/hidden_files/w46
CORE=$GOAL/hidden_files/weekly-report-w46-ru-build
LOGDIR=$W46/ru-fix/logs
mkdir -p "$LOGDIR"
fail=0
echo "=== CORE ==="
cd $CORE && $PY run.py > $LOGDIR/ru-core-run.log 2>&1; echo "core run exit=$? overflow=$(grep -c 'OVERFLOW\|TOO WIDE' $LOGDIR/ru-core-run.log || true)"
$PY render.py >> $LOGDIR/ru-core-run.log 2>&1; echo "core render exit=$?"
grep -E "TOTAL|by level|by page|model words" $LOGDIR/ru-core-run.log | tail -n 6
for n in en de fr es it pt nl ja ko zh-tw; do
  echo "=== $n ==="
  cd $W46 && $PY ru-transform.py $n > $LOGDIR/ru-$n-transform.log 2>&1; echo "$n transform exit=$?"
  B=$GOAL/hidden_files/weekly-report-w46-ru-$n-build
  cp $CORE/check_core.py $B/check_core.py
  cd $B && $PY run.py > $LOGDIR/ru-$n-run.log 2>&1; echo "$n run exit=$? overflow=$(grep -c 'OVERFLOW\|TOO WIDE' $LOGDIR/ru-$n-run.log || true)"
  $PY render.py >> $LOGDIR/ru-$n-run.log 2>&1; echo "$n render exit=$?"
  grep -E "TOTAL|by level|by page|model words" $LOGDIR/ru-$n-run.log | tail -n 4
done
echo "ALL BUILDS DONE"
