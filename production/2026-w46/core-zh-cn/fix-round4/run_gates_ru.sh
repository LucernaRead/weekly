#!/bin/bash
# Round 4 RU-only re-gates on FINAL artifacts.
set -u
ROOT=~/workspace/goals/lucernaread-social-media-operations
G=$ROOT/hidden_files/w46/zh-cn-fix-round4/gates
mkdir -p "$G"
PY=$ROOT/tools/venv/bin/python
CORE_DIR=$ROOT/files/weekly-report-w46-zh-cn-core
ED=$ROOT/files/weekly-report-w46-zh-cn-ru
$PY $ROOT/tools/occlusion_audit.py --selftest > "$G/occlusion-selftest.log" 2>&1; echo "selftest exit=$?"
$PY $ROOT/tools/occlusion_audit.py "$ED" --json "$G/occlusion-ru.json" > "$G/occlusion-ru.log" 2>&1; echo "occlusion exit=$?"; tail -n 3 "$G/occlusion-ru.log"
$PY $ROOT/tools/freeze.py diff --core-svg "$CORE_DIR/svg" --edition-svg "$ED/svg" --strict-cjk --json "$G/freeze-ru.json" > "$G/freeze-ru.log" 2>&1; echo "freeze exit=$?"; tail -n 5 "$G/freeze-ru.log"
$PY $ROOT/tools/p8.py extract --p8 "$ED/svg/p8-ceyan.svg" --total 150 --json "$G/p8-extract-ru.json" > "$G/p8-extract-ru.log" 2>&1; echo "p8 extract exit=$?"; head -n 3 "$G/p8-extract-ru.log"
$PY $ROOT/tools/p8.py compare --core-p8 "$CORE_DIR/svg/p8-ceyan.svg" --edition-p8 "$ED/svg/p8-ceyan.svg" --total 150 --json "$G/p8-ru.json" > "$G/p8-ru.log" 2>&1; echo "p8 compare exit=$?"; head -n 3 "$G/p8-ru.log"
echo "GATES RU DONE"
