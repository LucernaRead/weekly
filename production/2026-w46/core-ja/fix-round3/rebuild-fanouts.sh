#!/bin/bash
# W46 JA Round-3 fix rebuild: all 10 fan-outs from the fixed core build.
# Adapted from hidden_files/w46/ja-fix/rebuild-fanouts.sh; logs under ja-fix-round3.
# Logs: hidden_files/w46/ja-fix-round3/render-logs/<code>-{transform,run,render}.log
set -u
GOAL=~/workspace/goals/lucernaread-social-media-operations
PY=$GOAL/tools/venv/bin/python
LOGS=$GOAL/hidden_files/w46/ja-fix-round3/render-logs
SUM=$LOGS/rebuild-summary.txt
: > "$SUM"
for code in de en es fr it ko nl pt ru; do
  BD=$GOAL/hidden_files/weekly-report-w46-ja-$code-build
  echo "=== $code transform ===" >> "$SUM"
  (cd "$BD" && $PY transform.py > "$LOGS/$code-transform.log" 2>&1); echo "transform exit=$?" >> "$SUM"
  echo "=== $code run ===" >> "$SUM"
  (cd "$BD" && $PY run.py > "$LOGS/$code-run.log" 2>&1); echo "run exit=$?" >> "$SUM"
  grep -E "^P[0-9] saved|TOTAL|by level|by page|model chars" "$LOGS/$code-run.log" >> "$SUM" || true
  echo "overflow warnings: $(grep -c 'FLOW OVERFLOW\|HEAD TOO WIDE' "$LOGS/$code-run.log")" >> "$SUM"
  echo "=== $code render ===" >> "$SUM"
  (cd "$BD" && $PY render.py > "$LOGS/$code-render.log" 2>&1); echo "render exit=$?" >> "$SUM"
  tail -n 2 "$LOGS/$code-render.log" >> "$SUM"
done
echo "=== zh-tw gen ===" >> "$SUM"
(cd $GOAL/hidden_files/w46 && python3 gen_ja_zhtw.py > "$LOGS/zh-tw-gen.log" 2>&1); echo "gen exit=$?" >> "$SUM"
cat "$LOGS/zh-tw-gen.log" >> "$SUM"
BD=$GOAL/hidden_files/weekly-report-w46-ja-zh-tw-build
echo "=== zh-tw run ===" >> "$SUM"
(cd "$BD" && $PY run.py > "$LOGS/zh-tw-run.log" 2>&1); echo "run exit=$?" >> "$SUM"
grep -E "^P[0-9] saved|TOTAL|by level|by page|model chars" "$LOGS/zh-tw-run.log" >> "$SUM" || true
echo "overflow warnings: $(grep -c 'FLOW OVERFLOW\|HEAD TOO WIDE' "$LOGS/zh-tw-run.log")" >> "$SUM"
echo "=== zh-tw render ===" >> "$SUM"
(cd "$BD" && $PY render.py > "$LOGS/zh-tw-render.log" 2>&1); echo "render exit=$?" >> "$SUM"
tail -n 2 "$LOGS/zh-tw-render.log" >> "$SUM"
echo REBUILD-DONE >> "$SUM"
