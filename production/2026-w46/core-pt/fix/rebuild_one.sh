#!/bin/bash
# Rebuild ONE PT fan-out edition from a pristine copy of the core build dir
# + its (fixed) staged transform.py / gates.py. Usage: rebuild_one.sh <lang>
# <lang> in de en es fr it ko nl ru zh-cn. Exits non-zero on any step failure.
set -u
LANG="$1"
BASE=~/workspace/goals/lucernaread-social-media-operations
HIDDEN="$BASE/hidden_files"
FIX="$HIDDEN/w46/pt-fix"
LOGDIR="$FIX/logs"
CORE_BUILD="$HIDDEN/weekly-report-w46-pt-build"
ED_BUILD="$HIDDEN/weekly-report-w46-pt-$LANG-build"
PY="$BASE/tools/venv/bin/python"

if [ "$LANG" = "zh-cn" ]; then
  # zh-cn transform is unchanged: stage the live copy first (idempotent)
  mkdir -p "$FIX/stage/zh-cn"
  cp "$ED_BUILD/transform.py" "$FIX/stage/zh-cn/transform.py"
  cp "$ED_BUILD/gates.py" "$FIX/stage/zh-cn/gates.py"
fi

echo "=== rebuild $LANG: fresh copy of core build dir ==="
rm -rf "$ED_BUILD"
cp -r "$CORE_BUILD" "$ED_BUILD"
rm -rf "$ED_BUILD/__pycache__"
if [ "$LANG" != "zh-cn" ]; then rm -f "$ED_BUILD/gates_core.py"; fi
cp "$FIX/stage/$LANG/transform.py" "$ED_BUILD/transform.py"
cp "$FIX/stage/$LANG/gates.py" "$ED_BUILD/gates.py"

cd "$ED_BUILD" || exit 1
echo "=== transform.py ==="
"$PY" transform.py > "$LOGDIR/$LANG-transform.log" 2>&1; rc=$?
tail -n 12 "$LOGDIR/$LANG-transform.log"
[ $rc -ne 0 ] && { echo "TRANSFORM FAILED rc=$rc"; exit $rc; }
echo "=== run.py ==="
"$PY" run.py > "$LOGDIR/$LANG-run.log" 2>&1; rc=$?
cat "$LOGDIR/$LANG-run.log"
[ $rc -ne 0 ] && { echo "RUN FAILED rc=$rc"; exit $rc; }
grep -i "FLOW OVERFLOW\|HEAD TOO WIDE" "$LOGDIR/$LANG-run.log" && { echo "OVERFLOW WARNING PRESENT"; exit 1; }
echo "=== render.py ==="
"$PY" render.py > "$LOGDIR/$LANG-render.log" 2>&1; rc=$?
cat "$LOGDIR/$LANG-render.log"
[ $rc -ne 0 ] && { echo "RENDER FAILED rc=$rc"; exit $rc; }
echo "=== gates.py ==="
"$PY" gates.py > "$LOGDIR/$LANG-gates.log" 2>&1; rc=$?
cat "$LOGDIR/$LANG-gates.log"
[ $rc -ne 0 ] && { echo "GATES FAILED rc=$rc"; exit $rc; }
echo "REBUILD $LANG OK"
