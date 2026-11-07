#!/usr/bin/env python3
"""Resume zh-tw fallback one-by-one inserts after the 20:11Z driver died
post-es-landing (no process, no OK/BATCH line; es fully landed as
329d215+fb96584). Reuses insert_driver.fallback_per_edition (the SOP
fallback path). The bundle attempt is NOT repeated: it already failed
12 push attempts for this target (46a94d7, 'push too big / tunnel').
"""
import os
import sys

sys.path.insert(0, os.path.expanduser(
    "~/workspace/goals/lucernaread-social-media-operations/hidden_files/w46"))
import insert_driver  # noqa: E402

seed_map = insert_driver.seeds()
done, failed = insert_driver.fallback_per_edition("zh-tw", seed_map)
remote = insert_driver.git("ls-remote", "origin", "main").split()[0]
local = insert_driver.git("rev-parse", "HEAD")
insert_driver.log(
    f"BATCH zh-tw: fallback-resume done={done} failed={failed} "
    f"local={local[:8]} remote={remote[:8]} match={remote == local} "
    f"index_editions={len(insert_driver.index_slugs())}")
sys.exit(1 if (failed or remote != local) else 0)
