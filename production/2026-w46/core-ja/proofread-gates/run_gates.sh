#!/bin/bash
set -u
BASE=~/workspace/goals/lucernaread-social-media-operations
GATES=$BASE/hidden_files/w46/ja-proofread-gates
TOOLS=$BASE/tools
PY=$TOOLS/venv/bin/python
CORE=$BASE/files/weekly-report-w46-ja-core
declare -A DIRS=( [zh-cn]=weekly-report-w46-ja-core [de]=weekly-report-w46-ja-de [en]=weekly-report-w46-ja-en [es]=weekly-report-w46-ja-es [fr]=weekly-report-w46-ja-fr [it]=weekly-report-w46-ja-it [ko]=weekly-report-w46-ja-ko [nl]=weekly-report-w46-ja-nl [pt]=weekly-report-w46-ja-pt [ru]=weekly-report-w46-ja-ru [zh-tw]=weekly-report-w46-ja-zh-tw )
> $GATES/gates-run.log
for code in zh-cn de en es fr it ko nl pt ru zh-tw; do
  ed=$BASE/files/${DIRS[$code]}
  echo "=== $code freeze ===" >> $GATES/gates-run.log
  $PY $TOOLS/freeze.py diff --core-svg $CORE/svg --edition-svg $ed/svg --strict-cjk --json $GATES/freeze-$code.json >> $GATES/gates-run.log 2>&1; echo "freeze exit=$?" >> $GATES/gates-run.log
  echo "=== $code p8 ===" >> $GATES/gates-run.log
  $PY $TOOLS/p8.py compare --core-dir $CORE --edition-dir $ed --target ja --json $GATES/p8compare-$code.json >> $GATES/gates-run.log 2>&1; echo "p8 exit=$?" >> $GATES/gates-run.log
  echo "=== $code occlusion ===" >> $GATES/gates-run.log
  $PY $TOOLS/occlusion_audit.py $ed --json $GATES/occlusion-$code.json >> $GATES/gates-run.log 2>&1; echo "occlusion exit=$?" >> $GATES/gates-run.log
done
echo "=== core p8 extract ===" >> $GATES/gates-run.log
$PY $TOOLS/p8.py extract --p8 $CORE/svg/p8-tesuto.svg --total 150 --json $GATES/p8extract-core.json >> $GATES/gates-run.log 2>&1; echo "extract exit=$?" >> $GATES/gates-run.log
echo DONE
