#!/bin/bash
# Detached retry loop for KO web-PDF commit 0de705d (insert.py aborted before step (e)).
# Lives under the workspace (NOT /tmp: /tmp is wiped between turns and kills detached loops).
# Breaks when remote main == 0de705de43300c0a835bf8af3c8473c6c5b945a5. Never re-run insert.py for KO.
LOG=~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/push_ko_pdf.log
echo "LOOP START $(date -u +%FT%TZ)" >> "$LOG"
cd ~/workspace/weekly-git || exit 1
for i in $(seq 1 60); do
  timeout 150 git push origin 0de705de43300c0a835bf8af3c8473c6c5b945a5:main >> "$LOG" 2>&1
  R=$(git ls-remote origin main | awk '{print $1}')
  echo "attempt $i remote=$R" >> "$LOG"
  if [ "$R" = "0de705de43300c0a835bf8af3c8473c6c5b945a5" ]; then echo "PUSH OK attempt $i" >> "$LOG"; break; fi
  sleep 25
done
