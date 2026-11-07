#!/bin/bash
# W46 RU fix re-gates. JSONs/logs -> hidden_files/w46/ru-fix/ (builder/proofreader
# gate files in hidden_files/w46/ and ru-proofread-gates/ are NOT overwritten).
set -u
GOAL=~/workspace/goals/lucernaread-social-media-operations
PY=$GOAL/tools/venv/bin/python
W46=$GOAL/hidden_files/w46
FIX=$W46/ru-fix
LOG=$FIX/logs/ru-fix-gates.log
: > $LOG

webcheck() { # $1=edition dir $2=print pdf $3=web pdf
  local ed=$1
  local pb=$(pdftotext "$GOAL/files/$ed/$2" - 2>/dev/null | wc -c)
  local wb=$(pdftotext "$GOAL/files/$ed/$3" - 2>/dev/null | wc -c)
  local pchars=$(pdftotext "$GOAL/files/$ed/$2" - 2>/dev/null | tr -s '[:space:]' ' ' | wc -c)
  local wchars=$(pdftotext "$GOAL/files/$ed/$3" - 2>/dev/null | tr -s '[:space:]' ' ' | wc -c)
  local same="NO"
  pdftotext "$GOAL/files/$ed/$2" /tmp/ru_fix_p.txt 2>/dev/null
  pdftotext "$GOAL/files/$ed/$3" /tmp/ru_fix_w.txt 2>/dev/null
  if cmp -s <(tr -s '[:space:]' ' ' < /tmp/ru_fix_p.txt) <(tr -s '[:space:]' ' ' < /tmp/ru_fix_w.txt); then same="YES"; fi
  local psz=$(stat -c %s "$GOAL/files/$ed/$2")
  local wsz=$(stat -c %s "$GOAL/files/$ed/$3")
  local pages=$(pdfinfo "$GOAL/files/$ed/$3" 2>/dev/null | awk '/^Pages:/{print $2}')
  echo "WEBPDF $ed pages=$pages print=${psz}B web=${wsz}B pdftotext_print=${pb} web=${wb} normchars print=${pchars} web=${wchars} identical=${same}" | tee -a $LOG
}

declare -A SUF=( [core]="" [en]="EN" [de]="DE" [fr]="FR" [es]="ES" [it]="IT" [pt]="PT" [nl]="NL" [ja]="JA" [ko]="KO" [zh-tw]="ZH-TW" )
declare -A EDDIR=( [core]="weekly-report-w46-ru-core" [en]="weekly-report-w46-ru-en" [de]="weekly-report-w46-ru-de" [fr]="weekly-report-w46-ru-fr" [es]="weekly-report-w46-ru-es" [it]="weekly-report-w46-ru-it" [pt]="weekly-report-w46-ru-pt" [nl]="weekly-report-w46-ru-nl" [ja]="weekly-report-w46-ru-ja" [ko]="weekly-report-w46-ru-ko" [zh-tw]="weekly-report-w46-ru-zh-tw" )

for k in core en de fr es it pt nl ja ko zh-tw; do
  s=${SUF[$k]}; ed=${EDDIR[$k]}
  pdf="Lucerna-VOL3${s:+-$s}.pdf"; web="Lucerna-VOL3${s:+-$s}-web.pdf"
  echo "=== WEBPDF $k ===" | tee -a $LOG
  (cd $GOAL/tools && ./venv/bin/python webpdf.py ../files/$ed/svg ../files/$ed/$web >> $LOG 2>&1)
  echo "webpdf exit=$?" | tee -a $LOG
  webcheck $ed $pdf $web
done

for k in core en de fr es it pt nl ja ko zh-tw; do
  ed=${EDDIR[$k]}
  echo "=== OCCLUSION $k ===" | tee -a $LOG
  (cd $GOAL/tools && ./venv/bin/python occlusion_audit.py ../files/$ed --json ../hidden_files/w46/ru-fix/occlusion-fix-$k.json >> $LOG 2>&1)
  echo "occlusion exit=$?" | tee -a $LOG
done

for k in core en de fr es it pt nl ja ko zh-tw; do
  bdir="weekly-report-w46-ru-build"
  [ "$k" != "core" ] && bdir="weekly-report-w46-ru-$k-build"
  echo "=== CHECK_CORE $k ===" | tee -a $LOG
  (cd $GOAL/hidden_files/$bdir && $PY check_core.py $GOAL/files/${EDDIR[$k]} >> $LOG 2>&1)
  echo "check_core exit=$?" | tee -a $LOG
done

CORE_SVG=$GOAL/files/weekly-report-w46-ru-core/svg
for k in en de fr es it pt nl ja ko zh-tw; do
  ed=${EDDIR[$k]}
  echo "=== P8 COMPARE $k ===" | tee -a $LOG
  (cd $GOAL/tools && ./venv/bin/python p8.py compare --core-dir ../files/weekly-report-w46-ru-core --edition-dir ../files/$ed --target ru --json ../hidden_files/w46/ru-fix/p8-fix-$k.json >> $LOG 2>&1)
  echo "p8 exit=$?" | tee -a $LOG
  echo "=== FREEZE DIFF $k ===" | tee -a $LOG
  (cd $GOAL/tools && ./venv/bin/python freeze.py diff --core-svg $CORE_SVG --edition-svg ../files/$ed/svg --json ../hidden_files/w46/ru-fix/freeze-fix-$k.json >> $LOG 2>&1)
  echo "freeze exit=$?" | tee -a $LOG
  if [ "$k" = "ja" ] || [ "$k" = "ko" ] || [ "$k" = "zh-tw" ]; then
    echo "=== FREEZE STRICT-CJK $k ===" | tee -a $LOG
    (cd $GOAL/tools && ./venv/bin/python freeze.py diff --core-svg $CORE_SVG --edition-svg ../files/$ed/svg --strict-cjk --json ../hidden_files/w46/ru-fix/freeze-fix-$k-strict.json >> $LOG 2>&1)
    echo "freeze-strict exit=$? (1 = added CJK, adjudicated for native script; see word analysis)" | tee -a $LOG
  fi
  echo "=== FREEZE WORD ANALYSIS $k ===" | tee -a $LOG
  $PY $FIX/freeze_word_analysis.py $CORE_SVG $GOAL/files/$ed/svg $k >> $FIX/logs/word-analysis-$k.txt 2>&1
  echo "word-analysis exit=$? (see $FIX/logs/word-analysis-$k.txt)" | tee -a $LOG
done
echo "=== P8 EXTRACT CORE ===" | tee -a $LOG
(cd $GOAL/tools && ./venv/bin/python p8.py extract --p8 ../files/weekly-report-w46-ru-core/svg/p8-test.svg --total 150 >> $LOG 2>&1)
echo "p8-extract exit=$?" | tee -a $LOG
echo "GATES DONE" | tee -a $LOG
