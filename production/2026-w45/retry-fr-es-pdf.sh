#!/bin/bash
# Retry loop for W45 fr-es PDF push ONLY (insert.py already exited after STEP FAILED).
# NEVER re-run insert.py for this slug: metadata 48fe1371 is landed, PDF commit 818a38d6
# exists locally with parent 48fe1371. This loop only pushes 818a38d6:main.
cd ~/workspace/weekly-git || exit 1
TARGET=818a38d60aa02ddd9b4235db7c16cd60fa068ad0
for i in $(seq 1 60); do
  REMOTE=$(timeout 60 git ls-remote origin main | awk '{print $1}')
  if [ "$REMOTE" = "$TARGET" ]; then echo "VERIFIED ls-remote == $TARGET on check $i"; break; fi
  echo "attempt $i: pushing $TARGET (remote=$REMOTE)"
  timeout 150 git push origin "$TARGET:main" || true
  sleep 25
done
REMOTE=$(timeout 60 git ls-remote origin main | awk '{print $1}')
echo "final remote=$REMOTE local=$(git rev-parse HEAD)"
if [ "$REMOTE" = "$TARGET" ]; then echo "SUCCESS fr-es PDF landed"; else echo "NOT LANDED after loop"; fi
