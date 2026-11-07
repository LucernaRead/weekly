#!/bin/bash
# Retry loop for W45 ko-nl PDF push ONLY (insert.py already exited after STEP FAILED).
# NEVER re-run insert.py for this slug: metadata 46400d69 is landed, PDF commit 55351353
# exists locally with parent 46400d69. This loop only pushes 55351353:main.
cd ~/workspace/weekly-git || exit 1
TARGET=55351353ce4ea01533fa1c9d7e4ccc31f3be6738
for i in $(seq 1 60); do
  REMOTE=$(timeout 60 git ls-remote origin main | awk '{print $1}')
  if [ "$REMOTE" = "$TARGET" ]; then echo "VERIFIED ls-remote == $TARGET on check $i"; break; fi
  echo "attempt $i: pushing $TARGET (remote=$REMOTE)"
  timeout 150 git push origin "$TARGET:main" || true
  sleep 25
done
REMOTE=$(timeout 60 git ls-remote origin main | awk '{print $1}')
echo "final remote=$REMOTE local=$(git rev-parse HEAD)"
if [ "$REMOTE" = "$TARGET" ]; then echo "SUCCESS ko-nl PDF landed"; else echo "NOT LANDED after loop"; fi
