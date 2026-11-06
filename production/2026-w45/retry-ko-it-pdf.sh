#!/bin/bash
# Retry loop for W45 ko-it PDF push ONLY (insert.py already exited after STEP FAILED).
# NEVER re-run insert.py for this slug: metadata 1efa6278 is landed, PDF commit e90cf5fb
# exists locally with parent 1efa6278. This loop only pushes e90cf5fb:main.
cd ~/workspace/weekly-git || exit 1
TARGET=e90cf5fb25f156e53d296ea0450c8bacbfc1eeb3
for i in $(seq 1 60); do
  REMOTE=$(timeout 60 git ls-remote origin main | awk '{print $1}')
  if [ "$REMOTE" = "$TARGET" ]; then echo "VERIFIED ls-remote == $TARGET on check $i"; break; fi
  echo "attempt $i: pushing $TARGET (remote=$REMOTE)"
  timeout 150 git push origin "$TARGET:main" || true
  sleep 25
done
REMOTE=$(timeout 60 git ls-remote origin main | awk '{print $1}')
echo "final remote=$REMOTE local=$(git rev-parse HEAD)"
if [ "$REMOTE" = "$TARGET" ]; then echo "SUCCESS ko-it PDF landed"; else echo "NOT LANDED after loop"; fi
