#!/bin/bash
# Slow-retry ONLY commit 140a204 (zh-tw-pt web PDF) after driver died.
# 12 attempts, ~270s intervals, log every attempt to insert-run-119.log.
LOG="$HOME/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/insert-run-119.log"
REPO="$HOME/workspace/weekly-git"
COMMIT="140a20477e86d7ff060cc72cac677ddf28426256"
for i in $(seq 1 12); do
  echo "$(date -u '+%Y-%m-%d %H:%M:%S UTC') RECOVERY-COORD(21:56Z spawn) push-retry(pt-PDF) loop START attempt $i/12: commit 140a204" >> "$LOG"
  START=$(date +%s)
  OUT=$(cd "$REPO" && timeout 180 git push origin "$COMMIT:main" 2>&1)
  RC=$?
  ELAPSED=$(( $(date +%s) - START ))
  SIG=$(printf '%s' "$OUT" | tr '\n' ' ' | sed 's/  */ /g' | cut -c1-300)
  echo "$(date -u '+%Y-%m-%d %H:%M:%S UTC') RECOVERY-COORD(21:56Z spawn) push retry(pt-PDF) $i: git push origin 140a20477e86d7ff060cc72cac677ddf28426256:main rc=$RC sig=\"$SIG\" (~${ELAPSED}s)" >> "$LOG"
  REMOTE=$(cd "$REPO" && git ls-remote origin HEAD 2>/dev/null | awk '{print $1}')
  echo "$(date -u '+%Y-%m-%d %H:%M:%S UTC') RECOVERY-COORD(21:56Z spawn) after retry(pt-PDF) $i: ls-remote=$REMOTE" >> "$LOG"
  if [ "$REMOTE" = "$COMMIT" ]; then
    echo "$(date -u '+%Y-%m-%d %H:%M:%S UTC') RECOVERY-COORD(21:56Z spawn) LANDED on attempt $i: ls-remote=$REMOTE" >> "$LOG"
    break
  fi
  if [ "$i" -lt 12 ]; then sleep 270; fi
done
echo "$(date -u '+%Y-%m-%d %H:%M:%S UTC') RECOVERY-COORD(21:56Z spawn) push-retry(pt-PDF) loop DONE (12 attempts or landed early)" >> "$LOG"
