#!/bin/bash
# Push-retry chunk for commit 929fa62518eb9953c1237eaa7228e745bd23aeb9:main
# Usage: push_retry_loop.sh <first> <last>  (1-based, this coordinator's numbering)
# Logs every attempt to insert-run-119.log with UTC timestamps.
# Exits 0 if landed (rc=0 AND ls-remote match), 1 if all attempts in chunk failed.
set -u
REPO="$HOME/workspace/weekly-git"
LOG="$HOME/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/insert-run-119.log"
SHA="929fa62518eb9953c1237eaa7228e745bd23aeb9"
FIRST="${1:?first attempt}"; LAST="${2:?last attempt}"
log() { printf '%s %s\n' "$(date -u +%Y-%m-%d\ %H:%M:%S\ UTC)" "$*" >> "$LOG"; echo "$*"; }
cd "$REPO" || exit 2
for i in $(seq "$FIRST" "$LAST"); do
  log "RECOVERY-COORD(17:06Z spawn) push-retry loop START attempt $i/12: commit ${SHA:0:8}"
  start=$(date +%s)
  out=$(timeout 180 git push origin "$SHA:main" 2>&1)
  rc=$?
  dur=$(( $(date +%s) - start ))
  sig=$(printf '%s' "$out" | tr '\n' ' ' | sed 's/  */ /g' | cut -c1-300)
  log "RECOVERY-COORD(17:06Z spawn) push retry $i: git push origin ${SHA}:main rc=$rc sig=\"$sig\" (~${dur}s)"
  remote=$(timeout 120 git ls-remote origin main 2>/dev/null | awk '{print $1}')
  log "RECOVERY-COORD(17:06Z spawn) after retry $i: ls-remote=$remote"
  if [ "$rc" -eq 0 ] && [ "$remote" = "$SHA" ]; then
    log "RECOVERY-COORD(17:06Z spawn) push-retry loop END: landed=1 sha=$SHA attempt=$i"
    exit 0
  fi
  if [ "$i" -lt "$LAST" ]; then
    sleep 270
  fi
done
log "RECOVERY-COORD(17:06Z spawn) push-retry chunk $FIRST-$LAST done, not landed"
exit 1
