#!/bin/bash
# W46 IT fan-out gates: occlusion, p8 compare, freeze diff, Han scan, web PDF.
# Usage: bash hidden_files/w46/gate.sh <lang>  (lang = en|de|fr|es|pt|nl|ru|ja|ko|zh-tw)
# Appends to hidden_files/w46/it-gates.log. Exits nonzero on any gate failure.
set -u
cd ~/workspace/goals/lucernaread-social-media-operations || exit 1
L="$1"
ED="files/weekly-report-w46-it-$L"
LOG="hidden_files/w46/it-gates.log"
PY="tools/venv/bin/python"
fail=0
{
echo "================ $L ================"
echo "--- occlusion ---"
$PY tools/occlusion_audit.py "$ED/svg" 2>&1 | tail -20
echo "--- p8 compare ---"
$PY tools/p8.py compare --core-p8 files/weekly-report-w46-it-core/svg/p8-valutazione.svg --edition-p8 "$ED/svg/p8-valutazione.svg" --total 150 --json "hidden_files/w46/it-$L-p8.json" 2>&1 | tail -3
echo "--- freeze diff ---"
$PY tools/freeze.py diff --core-svg files/weekly-report-w46-it-core/svg --edition-svg "$ED/svg" --json "hidden_files/w46/it-$L-freeze.json" 2>&1 | tail -10
echo "--- Han chars in edition SVGs (raw grep count) ---"
grep -rhoP '[\x{4e00}-\x{9fff}]' "$ED/svg" | sort | uniq -c | sort -rn | head -20
echo "--- web PDF ---"
$PY tools/webpdf.py "$ED/svg" "$ED/La-Lucerna-VOL3-$(echo $L | tr a-z A-Z | sed 's/ZH-TW/ZHTW/')-web.pdf" 2>&1 | tail -1
ls -l "$ED"/*.pdf
python3 -c "
import subprocess,glob
fs=sorted(glob.glob('$ED/*.pdf'))
ts={}
for f in fs:
    ts[f]=len(subprocess.run(['pdftotext',f,'-'],capture_output=True).stdout)
print('pdftotext bytes:',ts)
print('WEB==PRINT:', len(set(ts.values()))==1)
"
} 2>&1 | tee -a "$LOG"
echo "gate script done for $L (review $LOG)"
