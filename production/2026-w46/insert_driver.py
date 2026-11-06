#!/usr/bin/env python3
"""Serialized W46 insert driver: runs tools/insert.py --bundle, one target
per run, ONE commit per bundle (user order 2026-11-03: a bundle = one
target's whole native set as one commit; never one commit per edition,
never metadata/PDF split commits, never one commit for the whole week).

Fallback (user order 2026-11-03, same day): if the bundle is still too
big to push — i.e. the bundle commit is made but the push never verifies
after the retry loop — reset the unpushed bundle commit and insert the
target's editions ONE BY ONE (per-edition insert.py calls, serialized,
stop on first failure). A bundle that fails BEFORE the commit (render /
lint) leaves a clean tree and falls back the same way; any other repo
state stops the run for manual recovery.
- FR-target editions are ALLOWED (F-MAIL cleared 2026-11-03: reader
  letters arrive only when the user sends them directly; no mail from him
  means no submissions — the FR editions ship with the disclosed editorial
  example).
"""
import json, os, re, subprocess, sys, time

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
FILES = os.path.join(GOAL, "files")
REPO = os.path.expanduser("~/workspace/weekly-git")
TOOLS = os.path.join(GOAL, "tools")
LOG = os.path.join(GOAL, "hidden_files", "w46", "insert-run-119.log")
ORDER = ["en", "de", "fr", "es", "it", "pt", "nl", "ru", "ja", "ko", "zh-cn", "zh-tw"]
FR_SEED_RECORDED = ("Lundi 9 novembre, le Sénat ouvre la discussion sur le budget "
    "de la Sécurité sociale pour 2027. Le texte arrive dans la version du "
    "gouvernement : le 23 octobre, les députés avaient rejeté la partie "
    "« recettes » par 115 voix contre 1, et la partie « dépenses » n'avait "
    "pas été examinée.")
FALLBACK_CORE = {
    ("en", "zh-cn"): "weekly-report-w46-en-core",
    ("it", "zh-cn"): "weekly-report-w46-it-core",
    ("ja", "zh-cn"): "weekly-report-w46-ja-core",
    ("ko", "zh-cn"): "weekly-report-w46-ko-core",
    ("nl", "zh-cn"): "weekly-report-w46-nl-core",
    ("ru", "zh-cn"): "weekly-report-w46-ru-core",
    ("zh-cn", "en"): "weekly-report-w46-zh-cn-core",
    ("zh-tw", "en"): "weekly-report-w46-zhtw-core",
}

def log(msg):
    line = f"{time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())} {msg}"
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write(line + "\n")

def split2(ex):
    parts = re.split(r"(?<=[。！？])|(?<=[.!?])\s+", ex.strip())
    return [p for p in parts if p]

def seeds():
    items = {it["source_lang"]: it for it in json.load(
        open(os.path.join(GOAL, "hidden_files", "w46", "cover-w46-build",
                          "headlines-w46.json"), encoding="utf-8"))}
    out = {lang: " ".join(split2(items[lang]["excerpt"])[:2]) for lang in ORDER}
    assert out["fr"] == FR_SEED_RECORDED, "FR seed derivation drifted from recorded excerpt"
    return out

def index_slugs():
    idx = json.load(open(os.path.join(REPO, "index.json"), encoding="utf-8"))
    return {e["slug"] for e in idx["editions"]}

def git(*args):
    return subprocess.run(["git"] + list(args), cwd=REPO,
                          capture_output=True, text=True).stdout.strip()

def natives(target):
    return [n for n in ORDER if n != target
            and not (target == "zh-cn" and n == "zh-tw")
            and not (target == "zh-tw" and n == "zh-cn")]

def edition_dir(target, native):
    dedicated = f"weekly-report-w46-{target}-{native}"
    if os.path.isdir(os.path.join(FILES, dedicated)):
        return dedicated
    fb = FALLBACK_CORE.get((target, native))
    assert fb, f"no dedicated dir and no sanctioned fallback for {target}-{native}"
    assert os.path.isdir(os.path.join(FILES, fb)), f"fallback dir missing: {fb}"
    return fb

def fallback_per_edition(target, seed_map):
    """One-by-one inserts for the target's remaining editions. Returns
    (done, failed_slug_or_None)."""
    slugs = index_slugs()
    done, failed = 0, None
    for i, native in enumerate(natives(target)):
        slug = f"2026-w46-{target}-{native}"
        edir = edition_dir(target, native)
        dest = os.path.join(REPO, "issues", "2026-w46", slug)
        if os.path.exists(dest):
            have = {f for f in os.listdir(dest)}
            complete = (f"{slug}.md" in have and f"{slug}.pdf" in have
                        and f"{slug}.text.md" in have and slug in slugs)
            if complete:
                log(f"SKIP {slug}: already fully present in repo, verified (md+pdf+text.md+index)")
                continue
            log(f"STOP {slug}: PARTIALLY present in repo ({sorted(have)}), manual recovery needed")
            failed = slug
            break
        argv = ["python3", os.path.join(TOOLS, "insert.py"),
                "--week", "2026-W46", "--target", target, "--native", native,
                "--edition-dir", os.path.join(FILES, edir)]
        if i == 0:
            argv += ["--vol", "3", "--exercises", "150",
                     "--seed-excerpt", seed_map[target]]
        log(f"START {slug} dir={edir} {'SEED' if i == 0 else 'sibling'} (fallback one-by-one)")
        p = subprocess.run(argv, capture_output=True, text=True, cwd=TOOLS)
        for ln in (p.stdout + p.stderr).strip().splitlines()[-6:]:
            log(f"  | {ln}")
        if p.returncode != 0:
            log(f"FAIL {slug} rc={p.returncode} — driver stopping")
            failed = slug
            break
        slugs = index_slugs()
        assert slug in slugs, f"{slug} missing from index after insert"
        log(f"OK {slug} (index now {len(slugs)} editions)")
        done += 1
    return done, failed

def main():
    if len(sys.argv) < 2:
        print("usage: insert_driver.py <target>  (e.g. en, de, fr)", file=sys.stderr)
        return 2
    target = sys.argv[1]
    assert target in ORDER, f"unknown target {target}"
    seed_map = seeds()
    before = len(index_slugs())
    argv = ["python3", os.path.join(TOOLS, "insert.py"),
            "--week", "2026-W46", "--target", target, "--bundle",
            "--vol", "3", "--exercises", "150",
            "--seed-excerpt", seed_map[target]]
    log(f"START bundle {target} (one commit for the whole native set)")
    p = subprocess.run(argv, capture_output=True, text=True, cwd=TOOLS)
    for ln in (p.stdout + p.stderr).strip().splitlines()[-8:]:
        log(f"  | {ln}")
    remote = git("ls-remote", "origin", "main").split()[0]
    local = git("rev-parse", "HEAD")
    if p.returncode == 0 and remote == local:
        log(f"BATCH {target}: bundle done, index {before} -> {len(index_slugs())} editions, "
            f"local={local[:8]} remote={remote[:8]} match=True")
        return 0
    # Bundle did not land. Decide from repo state, then fall back one-by-one.
    ahead = git("rev-list", "--count", f"{remote}..HEAD")
    dirty = git("status", "--porcelain")
    if p.returncode == 0 and remote != local:
        log(f"BUNDLE-STATE: insert.py reported success but remote != local "
            f"(local={local[:8]} remote={remote[:8]}) — falling back only after state check")
    if ahead == "1" and "bundle" in git("log", "-1", "--format=%s"):
        log(f"BUNDLE-STATE: unpushed bundle commit {local[:8]} (push too big / tunnel) — "
            f"resetting to remote {remote[:8]} and falling back to one-by-one inserts")
        r = subprocess.run(["git", "reset", "--hard", remote], cwd=REPO,
                           capture_output=True, text=True)
        if r.returncode != 0:
            log(f"STOP: reset failed: {r.stdout} {r.stderr}")
            return 1
    elif ahead == "0" and not dirty:
        log("BUNDLE-STATE: clean tree, HEAD == remote — bundle failed before committing; falling back to one-by-one inserts")
    else:
        log(f"STOP: unexpected repo state after bundle failure (ahead={ahead}, "
            f"dirty={dirty[:200]!r}, local={local[:8]}, remote={remote[:8]}) — manual recovery needed")
        return 1
    done, failed = fallback_per_edition(target, seed_map)
    remote = git("ls-remote", "origin", "main").split()[0]
    local = git("rev-parse", "HEAD")
    log(f"BATCH {target}: fallback done={done} failed={failed} "
        f"local={local[:8]} remote={remote[:8]} match={remote == local} "
        f"index_editions={len(index_slugs())}")
    if failed or remote != local:
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
