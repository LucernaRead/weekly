#!/bin/bash
# Gates part 2: rowcheck S1, measurements, PDF text-layer checks, freeze baseline.
set -u
ROOT=~/workspace/goals/lucernaread-social-media-operations
G=$ROOT/hidden_files/w46/zh-cn-fix-keys/gates
mkdir -p "$G"
PY=$ROOT/tools/venv/bin/python
: > "$G/summary-part2.txt"

# --- rowcheck section 1 (section 2 crashes on hardcoded NL P6 filename: expected N/A) ---
cd "$ROOT/hidden_files/w46" || exit 1
declare -A BUILD=( [en]=weekly-report-w46-zhcn-build [de]=weekly-report-w46-zh-cn-de-build [es]=weekly-report-w46-zh-cn-es-build [fr]=weekly-report-w46-zh-cn-fr-build [it]=weekly-report-w46-zh-cn-it-build [ja]=weekly-report-w46-zh-cn-ja-build [ko]=weekly-report-w46-zh-cn-ko-build [nl]=weekly-report-w46-zh-cn-nl-build [pt]=weekly-report-w46-zh-cn-pt-build [ru]=weekly-report-w46-zh-cn-ru-build )
for lang in en de es fr it ja ko nl pt ru; do
  if [ "$lang" = en ]; then ED=../files/weekly-report-w46-zh-cn-core/svg; else ED=../files/weekly-report-w46-zh-cn-$lang/svg; fi
  $PY rowcheck.py "$ED" dummy "$ROOT/hidden_files/weekly-report-w46-zhcn-build" "$ROOT/hidden_files/${BUILD[$lang]}" > "$G/rowcheck-$lang.log" 2>&1
  echo "rowcheck $lang exit=$? (S2 crash expected)" >> "$G/summary-part2.txt"
  head -n 9 "$G/rowcheck-$lang.log" >> "$G/summary-part2.txt"
done

# --- measurements ---
$PY "$ROOT/hidden_files/w46/zh-cn-fix-keys/measure_gates.py" > "$G/measure.log" 2>&1
echo "measure exit=$?" >> "$G/summary-part2.txt"
cat "$G/measure.log" >> "$G/summary-part2.txt"

# --- PDF checks ---
: > "$G/pdf-checks.txt"
for lang in en de es fr it ja ko nl pt ru; do
  if [ "$lang" = en ]; then ED=$ROOT/files/weekly-report-w46-zh-cn-core; WP=Lucerna-VOL3-web.pdf; PP=Lucerna-VOL3.pdf; else ED=$ROOT/files/weekly-report-w46-zh-cn-$lang; WP=Lucerna-VOL3-$(echo $lang | tr a-z A-Z)-web.pdf; PP=Lucerna-VOL3-$(echo $lang | tr a-z A-Z).pdf; fi
  pdftotext "$ED/$WP" "$G/pdftotext-web-$lang.txt" 2>/dev/null
  pdftotext "$ED/$PP" "$G/pdftotext-print-$lang.txt" 2>/dev/null
  wb=$(wc -c < "$G/pdftotext-web-$lang.txt"); pb=$(wc -c < "$G/pdftotext-print-$lang.txt")
  ws=$(stat -c %s "$ED/$WP"); ps=$(stat -c %s "$ED/$PP")
  wpages=$(pdfinfo "$ED/$WP" 2>/dev/null | awk '/^Pages:/{print $2}')
  ppages=$(pdfinfo "$ED/$PP" 2>/dev/null | awk '/^Pages:/{print $2}')
  if cmp -s "$G/pdftotext-web-$lang.txt" "$G/pdftotext-print-$lang.txt"; then ident="IDENTICAL"; else ident="DIFFER"; fi
  echo "$lang web=${ws}B pages=${wpages} text=${wb}B | print=${ps}B pages=${ppages} text=${pb}B | web-vs-print: $ident | web<=7MB: $([ "$ws" -le 7340032 ] && echo YES || echo NO)" >> "$G/pdf-checks.txt"
done
cat "$G/pdf-checks.txt" >> "$G/summary-part2.txt"

# --- freeze baseline (core reproduction proof) ---
$PY $ROOT/tools/freeze.py baseline --build "$ROOT/hidden_files/weekly-report-w46-zhcn-build" --core-svg "$ROOT/files/weekly-report-w46-zh-cn-core/svg" --out "$G/freeze-baseline" --json "$G/freeze-baseline.json" > "$G/freeze-baseline.log" 2>&1
echo "freeze baseline exit=$?" >> "$G/summary-part2.txt"
tail -n 5 "$G/freeze-baseline.log" >> "$G/summary-part2.txt"
echo "GATES PART 2 DONE"
