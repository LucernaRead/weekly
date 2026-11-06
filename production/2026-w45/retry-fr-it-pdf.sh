#!/bin/bash
# Retry loop for W45 fr-it PDF push ONLY (insert.py already exited after STEP FAILED).
# NEVER re-run insert.py for this slug: metadata af142083 is landed, PDF commit ca2fd2ec
# exists locally with parent af142083. This loop only pushes ca2fd2ec:main.
cd ~/workspace/weekly-git || exit 1
TARGET=ca2fd2ecbdb31ae10f6cb5c150f2b63d0adec274
for i in $(seq 1 60); do
  REMOTE=$(timeout 60 git ls-remote origin main | awk '{print $1}')
  if [ "$REMOTE" = "$TARGET" ]; then echo "VERIFIED ls-remote == $TARGET on check $i"; break; fi
  echo "attempt $i: pushing $TARGET (remote=$REMOTE)"
  timeout 150 git push origin "$TARGET:main" || true
  sleep 25
done
REMOTE=$(timeout 60 git ls-remote origin main | awk '{print $1}')
echo "final remote=$REMOTE local=$(git rev-parse HEAD)"
if [ "$REMOTE" = "$TARGET" ]; then echo "SUCCESS fr-it PDF landed"; else echo "NOT LANDED after loop"; fi
