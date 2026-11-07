# -*- coding: utf-8 -*-
"""PDF checks: web PDF size <= 7MB, pdftotext bytes > 0 (web + print),
normalised web/print text EQUAL, per edition. Prints one line per edition."""
import os, re, subprocess, sys

ROOT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
FILES = os.path.join(ROOT, "files")
ED = {"core": "weekly-report-w46-de-core", "en": "weekly-report-w46-de-en",
      "es": "weekly-report-w46-de-es", "fr": "weekly-report-w46-de-fr",
      "it": "weekly-report-w46-de-it", "ja": "weekly-report-w46-de-ja",
      "ko": "weekly-report-w46-de-ko", "nl": "weekly-report-w46-de-nl",
      "pt": "weekly-report-w46-de-pt", "ru": "weekly-report-w46-de-ru",
      "zh-cn": "weekly-report-w46-de-zh-cn", "zh-tw": "weekly-report-w46-de-zh-tw"}

def norm(b):
    t = b.decode("utf-8", "replace")
    t = re.sub(r"\s+", " ", t).strip()
    return t

fails = 0
for ed, d in ED.items():
    eddir = os.path.join(FILES, d)
    webs = [f for f in os.listdir(eddir) if f.endswith("-web.pdf")]
    prints = [f for f in os.listdir(eddir) if f.endswith("-print.pdf")] + \
             [f for f in os.listdir(eddir) if f.endswith(".pdf") and "-web" not in f and "-print" not in f]
    assert len(webs) == 1, (ed, webs)
    assert len(prints) >= 1, (ed, prints)
    web, pr = webs[0], prints[0]
    wp, pp = os.path.join(eddir, web), os.path.join(eddir, pr)
    wsize, psize = os.path.getsize(wp), os.path.getsize(pp)
    wt = subprocess.run(["pdftotext", "-layout", wp, "-"], capture_output=True).stdout
    pt = subprocess.run(["pdftotext", "-layout", pp, "-"], capture_output=True).stdout
    equal = norm(wt) == norm(pt)
    ok = wsize <= 7 * 1024 * 1024 and len(wt) > 0 and len(pt) > 0 and equal
    if not ok:
        fails += 1
    print("%s web=%s (%d bytes, pdftotext=%d) print=%s (%d bytes, pdftotext=%d) equal=%s %s"
          % (ed, web, wsize, len(wt), pr, psize, len(pt), equal, "PASS" if ok else "FAIL"))
print("PDF FAILURES: %d" % fails)
sys.exit(1 if fails else 0)
