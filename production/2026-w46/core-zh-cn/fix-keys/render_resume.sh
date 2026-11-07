#!/bin/bash
# Resume after the first render_all.sh session was dropped mid-KO-webpdf.
# KO: run.py + render.py already done (TOTAL 150, new print PDF) — only
# webpdf + textmd remain. NL/PT/RU: full sequence.
set -u
ROOT=~/workspace/goals/lucernaread-social-media-operations
OUT=$ROOT/hidden_files/w46/zh-cn-fix-keys
PY=$ROOT/tools/venv/bin/python

echo "===== ko (webpdf+textmd only) ====="
cd "$ROOT/tools" || exit 1
./venv/bin/python webpdf.py ../files/weekly-report-w46-zh-cn-ko/svg ../files/weekly-report-w46-zh-cn-ko/Lucerna-VOL3-KO-web.pdf 2>&1 | tee "$OUT/render-ko-webpdf.log"
cd "$ROOT/hidden_files/weekly-report-w46-zh-cn-ko-build" || exit 1
python3 ../w46/textmd.py 2026-w46-zh-cn-ko "$ROOT/files/weekly-report-w46-zh-cn-ko/2026-w46-zh-cn-ko.text.md" 2>&1 | tee "$OUT/render-ko-textmd.log"
echo "===== ko DONE ====="

declare -A BUILD=( [nl]=weekly-report-w46-zh-cn-nl-build [pt]=weekly-report-w46-zh-cn-pt-build [ru]=weekly-report-w46-zh-cn-ru-build )
declare -A PDF=( [nl]=Lucerna-VOL3-NL-web.pdf [pt]=Lucerna-VOL3-PT-web.pdf [ru]=Lucerna-VOL3-RU-web.pdf )
for lang in nl pt ru; do
  echo "===== $lang ====="
  cd "$ROOT/hidden_files/${BUILD[$lang]}" || exit 1
  echo "--- run.py ---"
  $PY run.py 2>&1 | tee "$OUT/render-$lang-run.log"
  echo "--- render.py ---"
  $PY render.py 2>&1 | tee "$OUT/render-$lang-render.log"
  echo "--- webpdf.py ---"
  cd "$ROOT/tools" || exit 1
  ./venv/bin/python webpdf.py "../files/weekly-report-w46-zh-cn-$lang/svg" "../files/weekly-report-w46-zh-cn-$lang/${PDF[$lang]}" 2>&1 | tee "$OUT/render-$lang-webpdf.log"
  echo "--- textmd.py ---"
  cd "$ROOT/hidden_files/${BUILD[$lang]}" || exit 1
  python3 ../w46/textmd.py "2026-w46-zh-cn-$lang" "$ROOT/files/weekly-report-w46-zh-cn-$lang/2026-w46-zh-cn-$lang.text.md" 2>&1 | tee "$OUT/render-$lang-textmd.log"
  echo "===== $lang DONE ====="
done
echo "RESUME RENDERS DONE"
