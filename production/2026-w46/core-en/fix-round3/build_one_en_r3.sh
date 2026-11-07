#!/bin/bash
# Build one W46 EN-family edition (Round 3): run.py + render.py + webpdf.py + en_textmd.py
# Mirrors hidden_files/w46/en-fix/build_one_en.sh, logs into en-fix-round3/.
# Usage: build_one_en_r3.sh <native> <slug> "<label>"
set -u
ROOT=~/workspace/goals/lucernaread-social-media-operations
FIX=$ROOT/hidden_files/w46/en-fix-round3
NAT=$1; SLUG=$2; LABEL=$3
if [ "$NAT" = "core" ]; then BD=$ROOT/hidden_files/weekly-report-w46-en-build; ED=$ROOT/files/weekly-report-w46-en-core; else BD=$ROOT/hidden_files/weekly-report-w46-en-${NAT}-build; ED=$ROOT/files/weekly-report-w46-en-${NAT}; fi
PY=$ROOT/tools/venv/bin/python
echo "===== BUILD $NAT ($SLUG) ====="
cd "$BD" || exit 1
$PY run.py > "$FIX/$NAT-run.log" 2>&1; rc=$?; echo "run.py rc=$rc"
grep -E "FLOW OVERFLOW|HEAD TOO WIDE" "$FIX/$NAT-run.log" && echo "!! OVERFLOW WARNINGS PRESENT" || echo "no overflow warnings"
grep "TOTAL exercises" "$FIX/$NAT-run.log"
[ $rc -ne 0 ] && exit 1
$PY render.py > "$FIX/$NAT-render.log" 2>&1; rc=$?; echo "render.py rc=$rc"; cat "$FIX/$NAT-render.log"
[ $rc -ne 0 ] && exit 1
cd $ROOT/tools
./venv/bin/python webpdf.py "$ED/svg" "$ED/The-Lucerna-VOL3-web.pdf" > "$FIX/$NAT-webpdf.log" 2>&1; rc=$?; echo "webpdf rc=$rc"; cat "$FIX/$NAT-webpdf.log"
[ $rc -ne 0 ] && exit 1
$PY $ROOT/hidden_files/w46/en_textmd.py "$BD" "$ED/$SLUG.text.md" "$SLUG" "$LABEL" > "$FIX/$NAT-textmd.log" 2>&1; rc=$?; echo "textmd rc=$rc"; cat "$FIX/$NAT-textmd.log"
[ $rc -ne 0 ] && exit 1
echo "===== DONE $NAT ====="
