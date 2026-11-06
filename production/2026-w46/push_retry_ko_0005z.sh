#!/bin/bash
# W46 push-retry loop, ko PDF commit d1fed7b (spawn ~00:03Z Nov 5). Only this commit, 12 attempts, ~270s intervals.
REPO="$HOME/workspace/weekly-git"
LOG="$HOME/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/insert-run-119.log"
COMMIT="d1fed7ba782b024e0af70c114b76af08b0538f2c"
cd "$REPO" || exit 1
for i in $(seq 1 12); do
  echo "$(date -u '+%Y-%m-%d %H:%M:%S UTC') RECOVERY-COORD(00:05Z spawn) push-retry(ko-PDF) loop START attempt $i/12: commit d1fed7b" >> "$LOG"
  START=$(date +%s)
  OUT=$(timeout 180 git push origin main 2>&1)
  RC=$?
  END=$(date +%s)
  SIG=$(printf '%s' "$OUT" | tr '\r\n' ' ' | tr -s ' ')
  echo "$(date -u '+%Y-%m-%d %H:%M:%S UTC') RECOVERY-COORD(00:05Z spawn) push retry(ko-PDF) $i: git push origin main rc=$RC sig=\"$SIG\" (~$((END-START))s)" >> "$LOG"
  REMOTE=$(timeout 60 git ls-remote origin main 2>/dev/null | awk '{print $1}')
  echo "$(date -u '+%Y-%m-%d %H:%M:%S UTC') RECOVERY-COORD(00:05Z spawn) after retry(ko-PDF) $i: ls-remote=$REMOTE" >> "$LOG"
  if [ "$RC" -eq 0 ] && [ "$REMOTE" = "$COMMIT" ]; then
    echo "$(date -u '+%Y-%m-%d %H:%M:%S UTC') RECOVERY-COORD(00:05Z spawn) LANDED on attempt $i: ls-remote=$COMMIT" >> "$LOG"
    break
  fi
  if [ "$i" -lt 12 ]; then
    sleep 270
  fi
done
echo "$(date -u '+%Y-%m-%d %H:%M:%S UTC') RECOVERY-COORD(00:05Z spawn) push-retry(ko-PDF) loop DONE (12 attempts or landed early)" >> "$LOG"
