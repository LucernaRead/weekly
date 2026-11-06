#!/bin/bash
# Slow push-retry loop for pending commit fcf87e8f (zh-cn-it PDF).
# Resumable: attempt numbers continue from lines already in the log.
cd ~/workspace/weekly-git || exit 1
LOG=~/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/insert-run-119.log
TARGET=fcf87e8ffa1bb06164d2c42f8cf28900f8825138
DONE=$(grep -c "git push origin fcf87e8f:main rc=" "$LOG" || true)
for k in 1 2 3 4 5 6 7 8 9 10 11; do
  i=$((DONE + k))
  [ "$i" -gt 12 ] && break
  sleep 270
  START=$(date +%s)
  OUT=$(git push origin fcf87e8f:main 2>&1); RC=$?
  END=$(date +%s)
  SIG=$(echo "$OUT" | tr '\n' ' ' | sed 's/  */ /g' | head -c 300)
  printf '%s RECOVERY-COORD push retry %s: git push origin fcf87e8f:main rc=%s sig="%s" (~%ss)\n' "$(date -u '+%Y-%m-%d %H:%M:%S UTC')" "$i" "$RC" "$SIG" "$((END-START))" >> "$LOG"
  REMOTE=$(git ls-remote origin HEAD 2>/dev/null | awk '{print $1}')
  printf '%s RECOVERY-COORD after retry %s: ls-remote=%s\n' "$(date -u '+%Y-%m-%d %H:%M:%S UTC')" "$i" "$REMOTE" >> "$LOG"
  echo "retry $i rc=$RC remote=$REMOTE"
  if [ "$REMOTE" = "$TARGET" ]; then echo "LANDED on retry $i"; exit 0; fi
done
REMOTE=$(git ls-remote origin HEAD 2>/dev/null | awk '{print $1}')
if [ "$REMOTE" = "$TARGET" ]; then echo "LANDED"; exit 0; fi
echo "NOT-LANDED after 12"
exit 1
