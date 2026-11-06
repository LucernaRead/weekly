#!/bin/bash
# Insert ONE W46 print cover (md + PDF only, no .html exists for W46).
# Usage: insert_cover_one.sh <lang>   e.g. en, zh-cn
# Stops (nonzero) on any unexpected state; never stacks an unverified commit.
set -u
LANG="$1"
REPO="$HOME/workspace/weekly-git"
FILES="$HOME/workspace/goals/lucernaread-social-media-operations/files"
LOG="$HOME/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/insert-run-119.log"
SRC="$FILES/cover-w46-$LANG"
DEST="$REPO/covers/2026-w46/2026-w46-cover-$LANG"
ts() { date -u '+%Y-%m-%d %H:%M:%S UTC'; }
log() { echo "$(ts) RECOVERY-COORD(00:05Z spawn) COVER $LANG: $*" | tee -a "$LOG"; }

cd "$REPO" || exit 1
# Preconditions: clean tree, HEAD == remote
if [ -n "$(git status --porcelain)" ]; then log "STOP dirty tree"; exit 1; fi
REMOTE_BEFORE=$(timeout 60 git ls-remote origin main 2>/dev/null | awk '{print $1}')
LOCAL_BEFORE=$(git rev-parse HEAD)
if [ "$REMOTE_BEFORE" != "$LOCAL_BEFORE" ]; then log "STOP local $LOCAL_BEFORE != remote $REMOTE_BEFORE"; exit 1; fi
if [ -e "$DEST" ]; then log "STOP dest already exists: $DEST"; exit 1; fi
# Source checks: md pin matches PDF, text layer present
PDF="$SRC/cover-w46-$LANG.pdf"
MD="$SRC/2026-w46-cover-$LANG.md"
[ -f "$PDF" ] && [ -f "$MD" ] || { log "STOP source files missing"; exit 1; }
BYTES=$(stat -c%s "$PDF"); SHA=$(sha256sum "$PDF" | awk '{print $1}')
grep -q "pdfBytes: $BYTES" "$MD" && grep -q "pdfSha256: \"$SHA\"" "$MD" || { log "STOP md pin mismatch bytes=$BYTES sha=$SHA"; exit 1; }
TXTBYTES=$(pdftotext "$PDF" - 2>/dev/null | wc -c)
[ "$TXTBYTES" -gt 0 ] || { log "STOP no text layer"; exit 1; }
log "source verified pdf bytes=$BYTES sha=$SHA textbytes=$TXTBYTES"

mkdir -p "$DEST"
cp "$MD" "$DEST/2026-w46-cover-$LANG.md"
cp "$PDF" "$DEST/cover-w46-$LANG.pdf"
log "copied md+pdf into $DEST"

node lint.mjs --write > /tmp/cover-lint-write-$LANG.log 2>&1; RCW=$?
tail -3 /tmp/cover-lint-write-$LANG.log | while read -r ln; do log "lint --write: $ln"; done
[ $RCW -eq 0 ] || { log "STOP lint --write rc=$RCW"; git status --porcelain; exit 1; }
node lint.mjs > /tmp/cover-lint-$LANG.log 2>&1; RCL=$?
tail -2 /tmp/cover-lint-$LANG.log | while read -r ln; do log "lint: $ln"; done
[ $RCL -eq 0 ] || { log "STOP lint rc=$RCL"; exit 1; }
# index.json must be untouched (no .html => cover not indexed); anything else unexpected stops us
CHANGED=$(git status --porcelain)
log "status after lint: $(echo "$CHANGED" | tr '\n' ';')"
echo "$CHANGED" | grep -q "index.json" && { log "STOP index.json changed unexpectedly"; exit 1; }
git add "$DEST/2026-w46-cover-$LANG.md" "$DEST/cover-w46-$LANG.pdf"
git commit -m "Add 2026-w46-cover-$LANG print cover" > /tmp/cover-commit-$LANG.log 2>&1; RCC=$?
[ $RCC -eq 0 ] || { log "STOP commit rc=$RCC"; cat /tmp/cover-commit-$LANG.log; exit 1; }
COMMIT=$(git rev-parse HEAD)
log "committed $COMMIT (1 PDF + md, no index change)"

# Push with retries; verify via ls-remote after each attempt
LANDED=0
for i in $(seq 1 6); do
  START=$(date +%s)
  OUT=$(timeout 180 git push origin main 2>&1); RC=$?
  DUR=$(( $(date +%s) - START ))
  SIG=$(printf '%s' "$OUT" | tr '\r\n' ' ' | tr -s ' ')
  log "push attempt $i/6 rc=$RC sig=\"$SIG\" (~${DUR}s)"
  REMOTE=$(timeout 60 git ls-remote origin main 2>/dev/null | awk '{print $1}')
  log "after push attempt $i: ls-remote=$REMOTE"
  if [ "$RC" -eq 0 ] && [ "$REMOTE" = "$COMMIT" ]; then LANDED=1; break; fi
  [ "$i" -lt 6 ] && sleep 120
done
[ "$LANDED" -eq 1 ] || { log "STOP push unverified after 6 attempts; commit $COMMIT left unpushed, NO further covers stacked"; exit 1; }
# Verify remote tree + remote index
TREE=$(timeout 60 git ls-tree -r origin/main -- "covers/2026-w46/2026-w46-cover-$LANG/" 2>/dev/null | wc -l)
log "verified: ls-remote=$COMMIT ls-tree cover files=$TREE"
timeout 60 git show origin/main:index.json > /tmp/cover-remote-index-$LANG.json 2>/dev/null
python3 -c "
import json,sys
idx=json.load(open('/tmp/cover-remote-index-$LANG.json'))
eds=[e for e in idx['editions'] if e['slug'].startswith('2026-w46-')]
print('remote index editions total=%d w46=%d pdfInRepo=%d covers=%d' % (len(idx['editions']), len(eds), sum(1 for e in eds if e.get('pdfInRepo')), len(idx.get('covers',[]))))
" | while read -r ln; do log "remote index: $ln"; done
log "COVER $LANG DONE landed=$COMMIT"
exit 0
