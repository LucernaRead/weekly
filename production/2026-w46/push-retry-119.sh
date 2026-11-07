#!/bin/bash
# W46 push-retry loop, run 119 (spawn 18:56Z). Same commit only, 12 attempts, ~270s intervals.
REPO="$HOME/workspace/weekly-git"
LOG="$HOME/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/insert-run-119.log"
COMMIT="929fa62518eb9953c1237eaa7228e745bd23aeb9"
cd "$REPO" || exit 1
for i in $(seq 1 12); do
  TS=$(date -u "+%Y-%m-%d %H:%M:%S UTC")
  echo "$TS RECOVERY-COORD(18:56Z spawn) push-retry loop START attempt $i/12: commit 929fa625" >> "$LOG"
  START=$(date +%s)
  OUT=$(timeout 120 git push origin "$COMMIT:main" 2>&1)
  RC=$?
  END=$(date +%s)
  SIG=$(printf '%s' "$OUT" | tr '\r\n' ' ' | tr -s ' ')
  echo "$TS RECOVERY-COORD(18:56Z spawn) push retry $i: git push origin $COMMIT:main rc=$RC sig=\"$SIG\" (~$((END-START))s)" >> "$LOG"
  REMOTE=$(timeout 60 git ls-remote origin main 2>/dev/null | awk '{print $1}')
  echo "$(date -u '+%Y-%m-%d %H:%M:%S UTC') RECOVERY-COORD(18:56Z spawn) after retry $i: ls-remote=$REMOTE" >> "$LOG"
  if [ "$RC" -eq 0 ] && [ "$REMOTE" = "$COMMIT" ]; then
    echo "$(date -u '+%Y-%m-%d %H:%M:%S UTC') RECOVERY-COORD(18:56Z spawn) LANDED: attempt $i rc=0, ls-remote matches $COMMIT — transport alive, loop stopping early" >> "$LOG"
    break
  fi
  if [ "$i" -lt 12 ]; then
    sleep 270
  fi
done
echo "$(date -u '+%Y-%m-%d %H:%M:%S UTC') RECOVERY-COORD(18:56Z spawn) push-retry loop DONE (12 attempts or landed early)" >> "$LOG"
