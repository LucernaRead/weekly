#!/bin/bash
# Round 4 independent gates — fresh re-run on FINAL artifacts. No fix-worker JSON accepted.
set -u
ROOT=~/workspace/goals/lucernaread-social-media-operations
GATE=$ROOT/hidden_files/w46/zh-cn-proofread-gates-round4
TOOLS=$ROOT/tools
PY=$TOOLS/venv/bin/python
CORE=$ROOT/files/weekly-report-w46-zh-cn-core
ED=$ROOT/files/weekly-report-w46-zh-cn-ru
mkdir -p "$GATE"
exec > "$GATE/run_gates_r4.out" 2>&1
echo "=== occlusion selftest (standalone) ==="
$PY $TOOLS/occlusion_audit.py --selftest; echo "selftest exit=$?"
echo "=== occlusion RU (full edition) ==="
$PY $TOOLS/occlusion_audit.py "$ED" --json "$GATE/occlusion-ru.json" > "$GATE/occlusion-ru.log" 2>&1; echo "occlusion exit=$?"
cat "$GATE/occlusion-ru.log"
echo "=== freeze core vs RU --strict-cjk ==="
$PY $TOOLS/freeze.py diff --core-svg "$CORE/svg" --edition-svg "$ED/svg" --strict-cjk --json "$GATE/freeze-ru.json" > "$GATE/freeze-ru.log" 2>&1; echo "freeze exit=$?"
cat "$GATE/freeze-ru.log"
echo "=== p8 extract RU ==="
$PY $TOOLS/p8.py extract --p8 "$ED/svg/p8-ceyan.svg" --total 150 --json "$GATE/p8-extract-ru.json" > "$GATE/p8-extract-ru.log" 2>&1; echo "p8 extract exit=$?"
cat "$GATE/p8-extract-ru.log"
echo "=== p8 compare core vs RU ==="
$PY $TOOLS/p8.py compare --core-p8 "$CORE/svg/p8-ceyan.svg" --edition-p8 "$ED/svg/p8-ceyan.svg" --total 150 --json "$GATE/p8-ru.json" > "$GATE/p8-ru.log" 2>&1; echo "p8 compare exit=$?"
cat "$GATE/p8-ru.log"
echo "ALL GATES DONE"
