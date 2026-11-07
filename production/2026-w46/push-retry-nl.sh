#!/bin/bash
# W46 recovery: slow-retry ONLY bf0e3af:main, 12 attempts, ~270s intervals.
# Detached (setsid/nohup) so a cancelled coordinator session still leaves a
# complete log + LANDED/STOPPED handoff in insert-run-119.log. Does NOTHING
# else: no driver, no new commits, never resets/amends bf0e3af.
LOG="$HOME/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/insert-run-119.log"
REPO="$HOME/workspace/weekly-git"
COMMIT="bf0e3af59baa92f69a2508e8bc5c80bb968777e3"
TAG="RECOVERY-COORD(22:59Z spawn)"
LANDED=0
for i in $(seq 1 12); do
  echo "$(date -u +'%Y-%m-%d %H:%M:%S UTC') $TAG push-retry(nl-PDF) loop START attempt $i/12: commit ${COMMIT:0:7}" >> "$LOG"
  START=$(date +%s)
  OUT=$(cd "$REPO" && timeout 420 git push origin "$COMMIT:main" 2>&1); RC=$?
  DUR=$(( $(date +%s) - START ))
  SIG=$(printf '%s' "$OUT" | tr '\r\n' ' ' | tr -s ' ' | cut -c1-300)
  echo "$(date -u +'%Y-%m-%d %H:%M:%S UTC') $TAG push retry(nl-PDF) $i: git push origin ${COMMIT:0:7}:main rc=$RC sig=\"$SIG\" (~${DUR}s)" >> "$LOG"
  REMOTE=$(cd "$REPO" && git ls-remote origin HEAD 2>/dev/null | awk '{print $1}')
  echo "$(date -u +'%Y-%m-%d %H:%M:%S UTC') $TAG after retry(nl-PDF) $i: ls-remote=$REMOTE" >> "$LOG"
  if [ "$REMOTE" = "$COMMIT" ]; then
    echo "$(date -u +'%Y-%m-%d %H:%M:%S UTC') $TAG LANDED on attempt $i: ls-remote=$COMMIT" >> "$LOG"
    LANDED=1
    break
  fi
  if [ "$i" -lt 12 ]; then sleep 270; fi
done
echo "$(date -u +'%Y-%m-%d %H:%M:%S UTC') $TAG push-retry(nl-PDF) loop DONE (12 attempts or landed early)" >> "$LOG"
if [ "$LANDED" -eq 0 ]; then
  # Final remote-verified counts for the STOPPED handoff (best effort, honest).
  COUNTS=$(cd "$REPO" && git show origin/main:index.json > /tmp/w46-final-index.json 2>/dev/null && python3 -c "
import json
d=json.load(open('/tmp/w46-final-index.json'))
eds=d['editions']; w46=[e for e in eds if str(e.get('slug','')).startswith('2026-w46-')]
print('index %d total / %d W46 / %d pdfInRepo=true' % (len(eds), len(w46), sum(1 for e in w46 if e.get('pdfInRepo'))))
" 2>/dev/null || echo "index unreadable")
  TREE=$(cd "$REPO" && git ls-tree -r origin/main -- issues/2026-w46 2>/dev/null | wc -l)
  PDFS=$(cd "$REPO" && git ls-tree -r origin/main -- issues/2026-w46 2>/dev/null | grep -c '\.pdf$' || true)
  REMOTE2=$(cd "$REPO" && git ls-remote origin HEAD 2>/dev/null | awk '{print $1}')
  echo "$(date -u +'%Y-%m-%d %H:%M:%S UTC') $TAG STOPPED: transport stayed dead — push-retry loop attempts 1-12 all failed (see per-attempt lines above, ~270s intervals); ls-remote stable $REMOTE2; remote-verified: $COUNTS; ls-tree issues/2026-w46 $TREE files / $PDFS PDFs; 0 W46 covers in repo; commit $COMMIT NOT reset/amended/discarded, still pending (zh-tw-nl PDF 1990345B + index flip), tree clean, 1 ahead of remote; driver NOT run, NO new commits stacked; REMAINS: zh-tw-nl PDF (this commit) + zh-tw ru/ja/ko editions + 12/12 covers; next: resume slow retries of THIS SAME COMMIT bf0e3af:main only, then one-by-one fallback for zh-tw ru/ja/ko skipping editions already fully present remotely (remote index + ls-tree, never local state alone), then covers; do NOT re-run a whole-bundle insert for zh-tw." >> "$LOG"
fi
