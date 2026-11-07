#!/bin/bash
# Re-render all 10 W46 zh-cn editions from source after the D3/D4 registry fix.
set -u
ROOT=~/workspace/goals/lucernaread-social-media-operations
OUT=$ROOT/hidden_files/w46/zh-cn-fix-keys
PY=$ROOT/tools/venv/bin/python
declare -A BUILD=( [en]=weekly-report-w46-zhcn-build [de]=weekly-report-w46-zh-cn-de-build [es]=weekly-report-w46-zh-cn-es-build [fr]=weekly-report-w46-zh-cn-fr-build [it]=weekly-report-w46-zh-cn-it-build [ja]=weekly-report-w46-zh-cn-ja-build [ko]=weekly-report-w46-zh-cn-ko-build [nl]=weekly-report-w46-zh-cn-nl-build [pt]=weekly-report-w46-zh-cn-pt-build [ru]=weekly-report-w46-zh-cn-ru-build )
declare -A PDF=( [en]=Lucerna-VOL3-web.pdf [de]=Lucerna-VOL3-DE-web.pdf [es]=Lucerna-VOL3-ES-web.pdf [fr]=Lucerna-VOL3-FR-web.pdf [it]=Lucerna-VOL3-IT-web.pdf [ja]=Lucerna-VOL3-JA-web.pdf [ko]=Lucerna-VOL3-KO-web.pdf [nl]=Lucerna-VOL3-NL-web.pdf [pt]=Lucerna-VOL3-PT-web.pdf [ru]=Lucerna-VOL3-RU-web.pdf )
for lang in en de es fr it ja ko nl pt ru; do
  echo "===== $lang ====="
  cd "$ROOT/hidden_files/${BUILD[$lang]}" || exit 1
  echo "--- run.py ---"
  $PY run.py 2>&1 | tee "$OUT/render-$lang-run.log"
  echo "--- render.py ---"
  $PY render.py 2>&1 | tee "$OUT/render-$lang-render.log"
  echo "--- webpdf.py ---"
  cd "$ROOT/tools" || exit 1
  ./venv/bin/python webpdf.py "../files/weekly-report-w46-zh-cn-$([ "$lang" = en ] && echo core || echo "$lang")/svg" "../files/weekly-report-w46-zh-cn-$([ "$lang" = en ] && echo core || echo "$lang")/${PDF[$lang]}" 2>&1 | tee "$OUT/render-$lang-webpdf.log"
  echo "--- textmd.py ---"
  cd "$ROOT/hidden_files/${BUILD[$lang]}" || exit 1
  python3 ../w46/textmd.py "2026-w46-zh-cn-$lang" "$ROOT/files/weekly-report-w46-zh-cn-$([ "$lang" = en ] && echo core || echo "$lang")/2026-w46-zh-cn-$lang.text.md" 2>&1 | tee "$OUT/render-$lang-textmd.log"
  echo "===== $lang DONE ====="
done
echo "ALL RENDERS DONE"
