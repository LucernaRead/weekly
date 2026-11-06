#!/bin/bash
# Regenerate every <slug>.text.md from the source manuscript (ru_textmd.py AST
# walk of the build dirs), diff against the shipped file, and install only if
# the diff is limited to the intended fix lines. Headers preserved verbatim
# (title arg = existing H1 from ru_kit.py EDITIONS). Core file is generated
# once and copied to the zh-cn filename (byte-identical by task spec).
set -u
GOAL=~/workspace/goals/lucernaread-social-media-operations
PY=$GOAL/tools/venv/bin/python
W46=$GOAL/hidden_files/w46
FIX=$W46/ru-fix
TMP=$FIX/textmd-tmp
mkdir -p "$TMP"
LOG=$FIX/logs/textmd-regen.log
: > $LOG

gen() { # $1=key $2=build-dir $3=slug $4=title $5=writing_type
  $PY $W46/ru_textmd.py $GOAL/hidden_files/$2 $TMP/$3.text.md "$4" "$5" >> $LOG 2>&1
  echo "gen $1 exit=$? -> $TMP/$3.text.md" | tee -a $LOG
}

gen core weekly-report-w46-ru-build 2026-w46-ru-core "VOL.3 · Russian text · Simplified Chinese explanations" "写作"
gen en weekly-report-w46-ru-en-build 2026-w46-ru-en "VOL.3 · Russian text · English explanations" "writing"
gen de weekly-report-w46-ru-de-build 2026-w46-ru-de "VOL.3 · Russian text · German explanations" "Schreiben"
gen fr weekly-report-w46-ru-fr-build 2026-w46-ru-fr "VOL.3 · Russian text · French explanations" "Rédaction"
gen es weekly-report-w46-ru-es-build 2026-w46-ru-es "VOL.3 · Russian text · Spanish explanations" "Redacción"
gen it weekly-report-w46-ru-it-build 2026-w46-ru-it "VOL.3 · Russian text · Italian explanations" "Composizione"
gen pt weekly-report-w46-ru-pt-build 2026-w46-ru-pt "VOL.3 · Russian text · Portuguese explanations" "Escrita"
gen nl weekly-report-w46-ru-nl-build 2026-w46-ru-nl "VOL.3 · Russian text · Dutch explanations" "Schrijven"
gen ja weekly-report-w46-ru-ja-build 2026-w46-ru-ja "VOL.3 · Russian text · Japanese explanations" "作文"
gen ko weekly-report-w46-ru-ko-build 2026-w46-ru-ko "VOL.3 · Russian text · Korean explanations" "쓰기"
gen zh-tw weekly-report-w46-ru-zh-tw-build 2026-w46-ru-zh-tw "VOL.3 · Russian text · Traditional Chinese explanations" "寫作"

declare -A EDDIR=( [core]="weekly-report-w46-ru-core" [en]="weekly-report-w46-ru-en" [de]="weekly-report-w46-ru-de" [fr]="weekly-report-w46-ru-fr" [es]="weekly-report-w46-ru-es" [it]="weekly-report-w46-ru-it" [pt]="weekly-report-w46-ru-pt" [nl]="weekly-report-w46-ru-nl" [ja]="weekly-report-w46-ru-ja" [ko]="weekly-report-w46-ru-ko" [zh-tw]="weekly-report-w46-ru-zh-tw" )
for k in core en de fr es it pt nl ja ko zh-tw; do
  ed=${EDDIR[$k]}
  slug=2026-w46-ru-$k
  [ "$k" = "core" ] && slug=2026-w46-ru-core
  echo "=== DIFF $k ($ed/$slug.text.md) ===" | tee -a $LOG
  diff "$GOAL/files/$ed/$slug.text.md" "$TMP/$slug.text.md" | tee -a $LOG | head -n 60
  echo "diff lines: $(diff "$GOAL/files/$ed/$slug.text.md" "$TMP/$slug.text.md" | wc -l)" | tee -a $LOG
done
echo "DIFFS DONE — no files installed by this script; install after review." | tee -a $LOG
