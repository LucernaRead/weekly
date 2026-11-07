#!/bin/bash
# Round 3 .text.md regeneration via core textmd.py (AST source export).
# Title derived from each existing header (first line minus one leading
# '# '), so headers stay byte-identical to pre-fix. Backups already in
# pre-fix/textmd-backup/ (taken before any edit). Asserts header verbatim.
set -u
GOAL=~/workspace/goals/lucernaread-social-media-operations
W=$GOAL/hidden_files/w46/ko-fix-round3
PY=python3
LOG=$W/textmd-regen.log
: > "$LOG"
declare -A BUILD=( [zh-cn]=weekly-report-w46-ko-build [de]=weekly-report-w46-ko-de-build
  [en]=weekly-report-w46-ko-en-build [es]=weekly-report-w46-ko-es-build
  [fr]=weekly-report-w46-ko-fr-build [it]=weekly-report-w46-ko-it-build
  [ja]=weekly-report-w46-ko-ja-build [nl]=weekly-report-w46-ko-nl-build
  [pt]=weekly-report-w46-ko-pt-build [ru]=weekly-report-w46-ko-ru-build
  [zh-tw]=weekly-report-w46-ko-zh-tw-build )
declare -A EDIR=( [zh-cn]=weekly-report-w46-ko-core [de]=weekly-report-w46-ko-de
  [en]=weekly-report-w46-ko-en [es]=weekly-report-w46-ko-es [fr]=weekly-report-w46-ko-fr
  [it]=weekly-report-w46-ko-it [ja]=weekly-report-w46-ko-ja [nl]=weekly-report-w46-ko-nl
  [pt]=weekly-report-w46-ko-pt [ru]=weekly-report-w46-ko-ru [zh-tw]=weekly-report-w46-ko-zh-tw )
for code in zh-cn de en es fr it ja nl pt ru zh-tw; do
  slug="2026-w46-ko-$code"
  out="$GOAL/files/${EDIR[$code]}/$slug.text.md"
  first4=$(head -n 4 "$W/pre-fix/textmd-backup/$slug.text.md")
  title=$(head -n 1 "$W/pre-fix/textmd-backup/$slug.text.md" | sed 's/^# //')
  oldbytes=$(wc -c < "$W/pre-fix/textmd-backup/$slug.text.md")
  $PY "$GOAL/hidden_files/weekly-report-w46-ko-build/textmd.py" \
    "$GOAL/hidden_files/${BUILD[$code]}" "$slug" "$out" "$title" >> "$LOG" 2>&1
  echo "$slug exit $? wrote $out" >> "$LOG"
  newfirst4=$(head -n 4 "$out")
  if [ "$first4" = "$newfirst4" ]; then echo "  header verbatim OK; old bytes $oldbytes new bytes $(wc -c < "$out")" >> "$LOG";
  else echo "  HEADER MISMATCH $slug" >> "$LOG"; fi
done
cat "$LOG"
echo TEXTMD-DONE
