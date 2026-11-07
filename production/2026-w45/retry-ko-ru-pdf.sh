#!/bin/bash
# Retry loop for W45 ko-ru PDF push ONLY (insert.py already exited after STEP FAILED).
# NEVER re-run insert.py for this slug: metadata ee3eec59 is landed, PDF commit dc984234
# exists locally with parent ee3eec59. This loop only pushes dc984234:main.
cd ~/workspace/weekly-git || exit 1
TARGET=dc984234caf5cb4306875b38ca402667789c5f9b
for i in $(seq 1 60); do
  REMOTE=$(timeout 60 git ls-remote origin main | awk '{print $1}')
  if [ "$REMOTE" = "$TARGET" ]; then echo "VERIFIED ls-remote == $TARGET on check $i"; break; fi
  echo "attempt $i: pushing $TARGET (remote=$REMOTE)"
  timeout 150 git push origin "$TARGET:main" || true
  sleep 25
done
REMOTE=$(timeout 60 git ls-remote origin main | awk '{print $1}')
echo "final remote=$REMOTE local=$(git rev-parse HEAD)"
if [ "$REMOTE" = "$TARGET" ]; then echo "SUCCESS ko-ru PDF landed"; else echo "NOT LANDED after loop"; fi
