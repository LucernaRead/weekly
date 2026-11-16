# -*- coding: utf-8 -*-
"""Render the W46 ZH-TW weekly: svg/ -> cards/ PNG (1950px) -> print PDF
(cairosvg+pypdf). The web PDF is built separately with tools/webpdf.py
(text layer required); this script does NOT produce the old JPEG web PDF.
"""
import os, io, glob, sys, time, tempfile
import importlib


def _import_cairosvg(deadline_s=60, interval_s=2):
    """EPERM-fix (2026-11-10, ZH-TW-W46-PT-RENDER-EPERM-DIAGNOSIS §6 fix 1a).

    `import cairosvg` probes tempfile at import time (cairocffi ->
    ctypes.util.find_library -> tempfile.NamedTemporaryFile). During the
    machine-wide write() EPERM fault that probe fails with
    FileNotFoundError even though the import itself is side-effect-free,
    so retry it across the fault's healthy seconds. Bounded: raises the
    last error after deadline_s. On failure the partially-imported
    modules are dropped from sys.modules and tempfile.tempdir reset so
    the next attempt re-probes from scratch.
    """
    started = time.monotonic()
    last = None
    while True:
        try:
            return importlib.import_module("cairosvg")
        except OSError as e:
            last = e
            for name in [m for m in list(sys.modules)
                         if m == "cairosvg" or m.startswith(
                             ("cairosvg.", "cairocffi", "cairocffi."))]:
                del sys.modules[name]
            tempfile.tempdir = None
            if time.monotonic() - started >= deadline_s:
                raise
            try:
                print(f"import cairosvg failed ({e}); retrying...",
                      file=sys.stderr, flush=True)
            except OSError:
                pass  # stderr write failed too; the retry loop continues
            time.sleep(interval_s)
    raise last  # unreachable; the loop raises or returns


cairosvg = _import_cairosvg()
from PIL import Image
from pypdf import PdfWriter, PdfReader

BASE = os.path.dirname(os.path.abspath(__file__))
SVGS = sorted(glob.glob(os.path.join(BASE, "svg", "*.svg")))
assert len(SVGS) == 8, SVGS

os.makedirs(os.path.join(BASE, "cards"), exist_ok=True)
png_paths = []
for s in SVGS:
    name = os.path.splitext(os.path.basename(s))[0] + ".png"
    out = os.path.join(BASE, "cards", name)
    cairosvg.svg2png(url=s, write_to=out, output_width=1950, output_height=2700)
    png_paths.append(out)
    print("card:", name, flush=True)

# print PDF from per-page PDFs
writer = PdfWriter()
for s in SVGS:
    data = cairosvg.svg2pdf(url=s)
    reader = PdfReader(io.BytesIO(data))
    for pg in reader.pages:
        writer.add_page(pg)
print_pdf = os.path.join(BASE, "Lucerna-VOL3-PT.pdf")
with open(print_pdf, "wb") as fh:
    writer.write(fh)
print("print PDF:", print_pdf, os.path.getsize(print_pdf), flush=True)

# web PDF via tools/webpdf.py (vector text layer, SOP appendix 4)
# EPERM-fix (2026-11-10, diagnosis §6 fix 1b): webpdf.py's first write is
# tempfile.mkdtemp (tools/webpdf.py:201), which fails the same way during
# the machine-wide write fault (attempt 1 died on its first SVG-rewrite
# write). Retry the whole subprocess, bounded to 60 s; each attempt gets
# a fresh tempdir, so a retry is safe. tools/webpdf.py itself is NOT
# edited — the retry lives here, on the render side.
import subprocess, sys
web_pdf = os.path.join(BASE, "Lucerna-VOL3-PT-web.pdf")
tools = os.path.expanduser("~/workspace/weekly-git/tools")
webpdf_cmd = [sys.executable, os.path.join(tools, "webpdf.py"),
              os.path.join(BASE, "svg"), web_pdf]
r = None
_started = time.monotonic()
_attempt = 0
while True:
    _attempt += 1
    try:
        r = subprocess.run(webpdf_cmd, capture_output=True, text=True)
    except OSError as e:
        r = None
        print(f"webpdf.py spawn failed (attempt {_attempt}): {e}",
              file=sys.stderr, flush=True)
    if r is not None and r.returncode == 0:
        break
    if r is not None:
        print(f"webpdf.py failed (attempt {_attempt}, rc={r.returncode}):",
              file=sys.stderr, flush=True)
        print(r.stdout, flush=True)
        print(r.stderr, file=sys.stderr, flush=True)
    if time.monotonic() - _started >= 60:
        break
    time.sleep(2)
print(r.stdout if r is not None else "", flush=True)
print(r.stderr if r is not None else "", file=sys.stderr, flush=True)
if r is None or r.returncode != 0:
    raise SystemExit(f"webpdf.py failed: "
                     f"{r.returncode if r is not None else 'spawn-OSError'} "
                     f"after {_attempt} attempt(s) in 60 s")
print("web PDF:", web_pdf, os.path.getsize(web_pdf), flush=True)
print("web PDF: build separately with tools/webpdf.py -> Lucerna-VOL3-PT-web.pdf", flush=True)
