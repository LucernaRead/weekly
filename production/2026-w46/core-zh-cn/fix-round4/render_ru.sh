#!/bin/bash
# Round 4 (D6) RU-only re-render, adapted from zh-cn-fix-round3/render_all.sh (RU branch only).
set -u
ROOT=~/workspace/goals/lucernaread-social-media-operations
OUT=$ROOT/hidden_files/w46/zh-cn-fix-round4
PY=$ROOT/tools/venv/bin/python
cd "$ROOT/hidden_files/weekly-report-w46-zh-cn-ru-build" || exit 1
echo "--- run.py ---"
$PY run.py 2>&1 | tee "$OUT/render-ru-run.log"
echo "--- render.py ---"
$PY render.py 2>&1 | tee "$OUT/render-ru-render.log"
echo "--- webpdf.py ---"
cd "$ROOT/tools" || exit 1
./venv/bin/python webpdf.py "../files/weekly-report-w46-zh-cn-ru/svg" "../files/weekly-report-w46-zh-cn-ru/Lucerna-VOL3-RU-web.pdf" 2>&1 | tee "$OUT/render-ru-webpdf.log"
echo "--- textmd.py ---"
cd "$ROOT/hidden_files/weekly-report-w46-zh-cn-ru-build" || exit 1
python3 ../w46/textmd.py "2026-w46-zh-cn-ru" "$ROOT/files/weekly-report-w46-zh-cn-ru/2026-w46-zh-cn-ru.text.md" 2>&1 | tee "$OUT/render-ru-textmd.log"
echo "RU RENDER DONE"
