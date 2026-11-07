#!/bin/bash
LOG="$HOME/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/insert-run-119.log"
REPO="$HOME/workspace/weekly-git"
COMMIT="2724946bd9920c3e28bdbb774aa8e2e3d7eb11aa"
cd "$REPO" || exit 1
for i in $(seq 1 12); do
  echo "$(date -u '+%Y-%m-%d %H:%M:%S UTC') RECOVERY-COORD(20:57Z spawn) push-retry(it-PDF) loop START attempt $i/12: commit 2724946" >> "$LOG"
  START=$(date +%s)
  OUT=$(git push origin "$COMMIT:main" 2>&1); RC=$?
  END=$(date +%s); DUR=$((END-START))
  SIG=$(printf '%s' "$OUT" | tr '\r\n' ' ' | sed 's/  */ /g' | cut -c1-300)
  echo "$(date -u '+%Y-%m-%d %H:%M:%S UTC') RECOVERY-COORD(20:57Z spawn) push retry(it-PDF) $i: git push origin $COMMIT:main rc=$RC sig=\"$SIG\" (~${DUR}s)" >> "$LOG"
  REMOTE=$(git ls-remote origin HEAD 2>/dev/null | awk '{print $1}')
  echo "$(date -u '+%Y-%m-%d %H:%M:%S UTC') RECOVERY-COORD(20:57Z spawn) after retry(it-PDF) $i: ls-remote=${REMOTE:-EMPTY/FLAKE}" >> "$LOG"
  if [ "$REMOTE" = "$COMMIT" ]; then
    echo "$(date -u '+%Y-%m-%d %H:%M:%S UTC') RECOVERY-COORD(20:57Z spawn) LANDED: commit 2724946 now remote HEAD (attempt $i/12)" >> "$LOG"
    break
  fi
  if [ "$i" -lt 12 ]; then sleep 270; fi
done
echo "$(date -u '+%Y-%m-%d %H:%M:%S UTC') RECOVERY-COORD(20:57Z spawn) push-retry(it-PDF) loop DONE (12 attempts or landed early)" >> "$LOG"
