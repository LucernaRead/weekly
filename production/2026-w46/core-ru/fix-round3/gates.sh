#!/bin/bash
# W46 RU Round 3 re-gates — IT EDITION ONLY. Outputs to hidden_files/w46/ru-fix-round3/.
# Does NOT rebuild other editions' web PDFs, does NOT touch weekly-git/index.json.
set -u
GOAL=~/workspace/goals/lucernaread-social-media-operations
PY=$GOAL/tools/venv/bin/python
W46=$GOAL/hidden_files/w46
R3=$W46/ru-fix-round3
LOG=$R3/logs/ru-fix-round3-gates.log
: > $LOG
ED=weekly-report-w46-ru-it
echo "=== WEBPDF CHECK it (existing artifacts, webpdf.py already run) ===" | tee -a $LOG
pb=$(pdftotext "$GOAL/files/$ED/Lucerna-VOL3-IT.pdf" - 2>/dev/null | wc -c)
wb=$(pdftotext "$GOAL/files/$ED/Lucerna-VOL3-IT-web.pdf" - 2>/dev/null | wc -c)
pdftotext "$GOAL/files/$ED/Lucerna-VOL3-IT.pdf" /tmp/r3_p.txt 2>/dev/null
pdftotext "$GOAL/files/$ED/Lucerna-VOL3-IT-web.pdf" /tmp/r3_w.txt 2>/dev/null
same="NO"; cmp -s <(tr -s '[:space:]' ' ' < /tmp/r3_p.txt) <(tr -s '[:space:]' ' ' < /tmp/r3_w.txt) && same="YES"
psz=$(stat -c %s "$GOAL/files/$ED/Lucerna-VOL3-IT.pdf"); wsz=$(stat -c %s "$GOAL/files/$ED/Lucerna-VOL3-IT-web.pdf")
pages=$(pdfinfo "$GOAL/files/$ED/Lucerna-VOL3-IT-web.pdf" 2>/dev/null | awk '/^Pages:/{print $2}')
echo "WEBPDF $ED pages=$pages print=${psz}B web=${wsz}B pdftotext_print=${pb} web=${wb} identical=${same}" | tee -a $LOG
pdffonts "$GOAL/files/$ED/Lucerna-VOL3-IT-web.pdf" 2>/dev/null | tee -a $LOG
echo "=== OCCLUSION it ===" | tee -a $LOG
(cd $GOAL/tools && ./venv/bin/python occlusion_audit.py ../files/$ED --json ../hidden_files/w46/ru-fix-round3/occlusion-round3-it.json >> $LOG 2>&1)
echo "occlusion exit=$?" | tee -a $LOG
echo "=== CHECK_CORE it ===" | tee -a $LOG
(cd $GOAL/hidden_files/weekly-report-w46-ru-it-build && $PY check_core.py $GOAL/files/$ED >> $LOG 2>&1)
echo "check_core exit=$?" | tee -a $LOG
echo "=== P8 EXTRACT CORE ===" | tee -a $LOG
(cd $GOAL/tools && ./venv/bin/python p8.py extract --p8 ../files/weekly-report-w46-ru-core/svg/p8-test.svg --total 150 >> $LOG 2>&1)
echo "p8-extract exit=$?" | tee -a $LOG
echo "=== P8 COMPARE it ===" | tee -a $LOG
(cd $GOAL/tools && ./venv/bin/python p8.py compare --core-dir ../files/weekly-report-w46-ru-core --edition-dir ../files/$ED --target ru --json ../hidden_files/w46/ru-fix-round3/p8-round3-it.json >> $LOG 2>&1)
echo "p8 exit=$?" | tee -a $LOG
cat $R3/p8-round3-it.json | tee -a $LOG
echo "=== FREEZE DIFF it ===" | tee -a $LOG
(cd $GOAL/tools && ./venv/bin/python freeze.py diff --core-svg ../files/weekly-report-w46-ru-core/svg --edition-svg ../files/$ED/svg --json ../hidden_files/w46/ru-fix-round3/freeze-round3-it.json >> $LOG 2>&1)
echo "freeze exit=$?" | tee -a $LOG
echo "=== FREEZE WORD ANALYSIS it ===" | tee -a $LOG
$PY $W46/ru-fix/freeze_word_analysis.py $GOAL/files/weekly-report-w46-ru-core/svg $GOAL/files/$ED/svg it > $R3/logs/word-analysis-it.txt 2>&1
echo "word-analysis exit=$?" | tee -a $LOG
tail -n 12 $R3/logs/word-analysis-it.txt | tee -a $LOG
echo "=== P6 CHART it ===" | tee -a $LOG
$PY $W46/ru-fix/chart_check.py $GOAL/files/$ED >> $LOG 2>&1
echo "chart exit=$?" | tee -a $LOG
echo "GATES DONE" | tee -a $LOG
