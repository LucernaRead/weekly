#!/bin/bash
# Re-gate ONE edition on final artifacts: freeze diff vs core, p8 compare,
# occlusion audit. Usage: gates_one.sh <lang> ; logs+JSONs to pt-fix/gates/.
set -u
LANG="$1"
BASE=~/workspace/goals/lucernaread-social-media-operations
G="$BASE/hidden_files/w46/pt-fix/gates"
PY="$BASE/tools/venv/bin/python"
ED="$BASE/files/weekly-report-w46-pt-$LANG"
CORE_SVG="$BASE/files/weekly-report-w46-pt-core/svg"
echo "=== freeze diff $LANG ==="
"$PY" "$BASE/tools/freeze.py" diff --core-svg "$CORE_SVG" --edition-svg "$ED/svg" --json "$G/freeze-pt-$LANG.json" > "$G/freeze-pt-$LANG.log" 2>&1; echo "freeze rc=$?"
cat "$G/freeze-pt-$LANG.log"
echo "=== p8 compare $LANG ==="
"$PY" "$BASE/tools/p8.py" compare --core-dir "$BASE/files/weekly-report-w46-pt-core" --edition-dir "$ED" --target pt --total 150 --json "$G/p8-pt-$LANG.json" > "$G/p8-pt-$LANG.log" 2>&1; echo "p8 rc=$?"
cat "$G/p8-pt-$LANG.log"
echo "=== occlusion $LANG ==="
"$PY" "$BASE/tools/occlusion_audit.py" "$ED/svg" --json "$G/occlusion-pt-$LANG.json" > "$G/occlusion-pt-$LANG.log" 2>&1; echo "occlusion rc=$?"
cat "$G/occlusion-pt-$LANG.log"
echo "GATES $LANG DONE"
