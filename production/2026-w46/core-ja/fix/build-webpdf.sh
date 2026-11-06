#!/bin/bash
# Build text-layer web PDFs for all 11 W46 JA editions via tools/webpdf.py only.
set -u
GOAL=~/workspace/goals/lucernaread-social-media-operations
PY=$GOAL/tools/venv/bin/python
LOGS=$GOAL/hidden_files/w46/ja-fix/render-logs
SUM=$LOGS/webpdf-summary.txt
: > "$SUM"
run_one() {
  local code=$1 dir=$2 out=$3
  echo "=== $code ===" >> "$SUM"
  (cd "$GOAL" && $PY tools/webpdf.py "files/$dir/svg" "files/$dir/$out" > "$LOGS/webpdf-$code.log" 2>&1)
  echo "webpdf exit=$?" >> "$SUM"
  cat "$LOGS/webpdf-$code.log" >> "$SUM"
  echo "size: $(stat -c%s "$GOAL/files/$dir/$out" 2>/dev/null)" >> "$SUM"
}
run_one zh-cn weekly-report-w46-ja-core Lucerna-VOL3-web.pdf
run_one de weekly-report-w46-ja-de Lucerna-VOL3-DE-web.pdf
run_one en weekly-report-w46-ja-en Lucerna-VOL3-EN-web.pdf
run_one es weekly-report-w46-ja-es Lucerna-VOL3-ES-web.pdf
run_one fr weekly-report-w46-ja-fr Lucerna-VOL3-FR-web.pdf
run_one it weekly-report-w46-ja-it Lucerna-VOL3-IT-web.pdf
run_one ko weekly-report-w46-ja-ko Lucerna-VOL3-KO-web.pdf
run_one nl weekly-report-w46-ja-nl Lucerna-VOL3-NL-web.pdf
run_one pt weekly-report-w46-ja-pt Lucerna-VOL3-PT-web.pdf
run_one ru weekly-report-w46-ja-ru Lucerna-VOL3-RU-web.pdf
run_one zh-tw weekly-report-w46-ja-zh-tw Lucerna-VOL3-ZHTW-web.pdf
echo WEBPDF-DONE >> "$SUM"
