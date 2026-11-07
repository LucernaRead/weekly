#!/bin/bash
# W46 zh-tw fix re-render: run.py + render.py for core + 9 fan-outs, logs to zh-tw-fix/
G=~/workspace/goals/lucernaread-social-media-operations
FIX=$G/hidden_files/w46/zh-tw-fix
PY=$G/tools/venv/bin/python
cd $G/tools || exit 1
render_one() {
  code=$1; build=$2
  log=$FIX/render-$code.log
  echo "===== $code : $build =====" > "$log"
  $PY ../hidden_files/$build/run.py >> "$log" 2>&1; rc1=$?
  $PY ../hidden_files/$build/render.py >> "$log" 2>&1; rc2=$?
  echo "run.py rc=$rc1 render.py rc=$rc2" >> "$log"
  grep -E "TOTAL|by level|by page|by type|FLOW OVERFLOW|HEAD TOO WIDE|WRAP WIDTH|teaser ends|col3 ends" "$log" | tail -n 12
  echo "--- $code rc1=$rc1 rc2=$rc2"
}
render_one en weekly-report-w46-zhtw-build
for c in de es fr it ja ko nl pt ru; do render_one $c weekly-report-w46-zh-tw-$c-build; done
echo "ALL RENDER DONE"
