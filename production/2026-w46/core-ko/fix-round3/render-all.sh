#!/bin/bash
# Round 3 re-render: run.py -> render.py -> tools/webpdf.py, sequentially,
# one edition at a time (one-process rule: run.py drives all content modules).
# Logs under hidden_files/w46/ko-fix-round3/render-logs/.
set -u
GOAL=~/workspace/goals/lucernaread-social-media-operations
W=$GOAL/hidden_files/w46/ko-fix-round3
LOGS=$W/render-logs
mkdir -p "$LOGS"
PY=$GOAL/tools/venv/bin/python
WEBPDF=$GOAL/tools/webpdf.py

run_edition() {
  local code="$1" build="$2" edir="$3" webname="$4"
  echo "===== $code : run.py ====="
  (cd "$GOAL/hidden_files/$build" && "$PY" run.py > "$LOGS/$code-run.log" 2>&1)
  echo "run.py exit=$?"
  grep -E "TOTAL|by level|by page" "$LOGS/$code-run.log"
  echo "===== $code : render.py ====="
  (cd "$GOAL/hidden_files/$build" && "$PY" render.py > "$LOGS/$code-render.log" 2>&1)
  echo "render.py exit=$?"
  echo "===== $code : webpdf.py ====="
  (cd "$GOAL/tools" && "$PY" "$WEBPDF" "../files/$edir/svg" "../files/$edir/$webname" > "$LOGS/$code-webpdf.log" 2>&1)
  echo "webpdf.py exit=$?"
  cat "$LOGS/$code-webpdf.log"
}

run_edition core weekly-report-w46-ko-build weekly-report-w46-ko-core Lucerna-VOL3-web.pdf
run_edition de weekly-report-w46-ko-de-build weekly-report-w46-ko-de Lucerna-VOL3-web.pdf
run_edition en weekly-report-w46-ko-en-build weekly-report-w46-ko-en Lucerna-VOL3-EN-web.pdf
run_edition es weekly-report-w46-ko-es-build weekly-report-w46-ko-es Lucerna-VOL3-ES-web.pdf
run_edition fr weekly-report-w46-ko-fr-build weekly-report-w46-ko-fr Lucerna-VOL3-FR-web.pdf
run_edition it weekly-report-w46-ko-it-build weekly-report-w46-ko-it Lucerna-VOL3-IT-web.pdf
run_edition ja weekly-report-w46-ko-ja-build weekly-report-w46-ko-ja Lucerna-VOL3-web.pdf
run_edition nl weekly-report-w46-ko-nl-build weekly-report-w46-ko-nl Lucerna-VOL3-NL-web.pdf
run_edition pt weekly-report-w46-ko-pt-build weekly-report-w46-ko-pt Lucerna-VOL3-web.pdf
run_edition ru weekly-report-w46-ko-ru-build weekly-report-w46-ko-ru Lucerna-VOL3-RU-web.pdf
run_edition zh-tw weekly-report-w46-ko-zh-tw-build weekly-report-w46-ko-zh-tw Lucerna-VOL3-ZHTW-web.pdf
echo RENDER-ALL-DONE
