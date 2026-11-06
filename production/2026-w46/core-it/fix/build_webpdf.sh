#!/bin/bash
BASE=~/workspace/goals/lucernaread-social-media-operations
PY=$BASE/tools/venv/bin/python
FIX=$BASE/hidden_files/w46/it-fix
declare -A WEB=( [core]=La-Lucerna-VOL3-web.pdf [de]=La-Lucerna-VOL3-DE-web.pdf [en]=La-Lucerna-VOL3-EN-web.pdf [es]=La-Lucerna-VOL3-ES-web.pdf [fr]=La-Lucerna-VOL3-FR-web.pdf [ja]=La-Lucerna-VOL3-JA-web.pdf [ko]=La-Lucerna-VOL3-KO-web.pdf [nl]=La-Lucerna-VOL3-NL-web.pdf [pt]=La-Lucerna-VOL3-PT-web.pdf [ru]=La-Lucerna-VOL3-RU-web.pdf [zh-tw]=La-Lucerna-VOL3-ZHTW-web.pdf )
for code in core de en es fr ja ko nl pt ru zh-tw; do
  ED=$BASE/files/weekly-report-w46-it-$code
  echo "===== $code ====="
  $PY $BASE/tools/webpdf.py "$ED/svg" "$ED/${WEB[$code]}" > $FIX/webpdf-$code.log 2>&1; echo "webpdf-$code exit=$?"
  tail -n 4 $FIX/webpdf-$code.log
done
echo WEBDONE
