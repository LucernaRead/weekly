#!/bin/bash
# Fresh slow-retry loop for commit 2724946 ONLY (zh-tw-it PDF + index flip).
# 12 attempts, ~270s intervals, log every attempt to insert-run-119.log.
LOG="$HOME/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/insert-run-119.log"
REPO="$HOME/workspace/weekly-git"
COMMIT="2724946bd9920c3e28bdbb774aa8e2e3d7eb11aa"
for i in $(seq 1 12); do
  echo "$(date -u '+%Y-%m-%d %H:%M:%S UTC') RECOVERY-COORD(21:56Z spawn) push-retry(it-PDF) loop START attempt $i/12: commit 2724946" >> "$LOG"
  START=$(date +%s)
  OUT=$(cd "$REPO" && timeout 120 git push origin "$COMMIT:main" 2>&1)
  RC=$?
  ELAPSED=$(( $(date +%s) - START ))
  SIG=$(printf '%s' "$OUT" | tr '\n' ' ' | sed 's/  */ /g' | cut -c1-300)
  echo "$(date -u '+%Y-%m-%d %H:%M:%S UTC') RECOVERY-COORD(21:56Z spawn) push retry(it-PDF) $i: git push origin 2724946bd9920c3e28bdbb774aa8e2e3d7eb11aa:main rc=$RC sig=\"$SIG\" (~${ELAPSED}s)" >> "$LOG"
  REMOTE=$(cd "$REPO" && git ls-remote origin HEAD 2>/dev/null | awk '{print $1}')
  echo "$(date -u '+%Y-%m-%d %H:%M:%S UTC') RECOVERY-COORD(21:56Z spawn) after retry(it-PDF) $i: ls-remote=$REMOTE" >> "$LOG"
  if [ "$REMOTE" = "$COMMIT" ]; then
    echo "$(date -u '+%Y-%m-%d %H:%M:%S UTC') RECOVERY-COORD(21:56Z spawn) LANDED on attempt $i: ls-remote=$REMOTE" >> "$LOG"
    break
  fi
  if [ "$i" -lt 12 ]; then sleep 270; fi
done
echo "$(date -u '+%Y-%m-%d %H:%M:%S UTC') RECOVERY-COORD(21:56Z spawn) push-retry(it-PDF) loop DONE (12 attempts or landed early)" >> "$LOG"
