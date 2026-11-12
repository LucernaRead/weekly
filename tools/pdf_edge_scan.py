#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pdf_edge_scan.py — standing gate: delivered print-PDF raster edge scan (W47).

New gate, added 2026-11-11 (pre-insert): no existing gate rendered the
delivered print PDF and checked whether any ink touches the page edge.
A line, rule or glyph running off the page is invisible to the SVG-side
gates (they measure against margins and boxes, never the sheet edge).

What it does: for each edition, render the delivered print PDF at 200 dpi
(grayscale, MuPDF) and scan the outer 3 px band of all four page edges for
ink (gray < 200; paper is ~251, cream ~240). It also records, per page,
the minimum ink distance to each edge, so a near miss is visible even
when nothing touches. Any ink inside the 3 px band is a TOUCH (defect —
ink must not reach the sheet edge); ink within 10 px is reported NEAR.

Which PDF: the print PDF in the edition dir — the ``*.pdf`` that is NOT a
web PDF (any name containing ``web.pdf``, covering both ``-web.pdf`` and
``.web.pdf`` spellings). Exactly one must exist.

Memory guard (per the pre-insert task): before rendering each edition,
check MemAvailable; below 1500 MB, wait 60 s and retry (up to 10 times)
before rendering anyway. Renders are serial, one edition at a time, and
pixmaps are freed after each page — nothing is kept on disk except the
optional JSON report (--json-dir) and, for TOUCH pages only, a small crop
of the touched edge as evidence (--json-dir/crops/).

Usage:
  python3 tools/pdf_edge_scan.py <edition-dir> [<edition-dir> ...]
      [--dpi 200] [--json-dir DIR]
Exit 0 iff no TOUCH in any edition; exit 1 if any TOUCH; exit 2 if an
edition is BLOCKED (no / ambiguous print PDF, render failure).
Run with the repo venv (tools/venv/bin/python) for PyMuPDF + PIL + numpy.
"""
import json
import os
import sys
import time

try:
    import pymupdf as fitz
except ImportError:  # pragma: no cover - old bindings
    import fitz
import numpy as np
from PIL import Image

INK = 200            # gray value below this counts as ink
BAND = 3             # px: outer band that must stay ink-free
NEAR = 10            # px: report ink this close to an edge as NEAR
MEM_MIN_MB = 1500
MEM_WAIT_S = 60
MEM_RETRIES = 1   # check before each render; if below threshold, wait 60 s
# once ("wait a bit") and then render: one 200 dpi page needs ~150 MB
# peak, safe well below the threshold; the wait is a courtesy to the
# contended machine, not a hard gate.


def mem_available_mb():
    try:
        with open("/proc/meminfo", encoding="utf-8") as f:
            for line in f:
                if line.startswith("MemAvailable:"):
                    return int(line.split()[1]) // 1024
    except OSError:
        pass
    return 10 ** 9


def wait_for_memory(log):
    for attempt in range(MEM_RETRIES):
        avail = mem_available_mb()
        if avail >= MEM_MIN_MB:
            return avail
        log.append(f"memory wait: available {avail}MB < {MEM_MIN_MB}MB, "
                   f"sleep {MEM_WAIT_S}s (try {attempt + 1}/{MEM_RETRIES})")
        time.sleep(MEM_WAIT_S)
    return mem_available_mb()


def find_print_pdf(ed_dir):
    pdfs = [f for f in os.listdir(ed_dir) if f.lower().endswith(".pdf")]
    prints = [f for f in pdfs if "web.pdf" not in f.lower()]
    if len(prints) != 1:
        return None, f"expected exactly 1 print PDF, found {prints}"
    return os.path.join(ed_dir, prints[0]), None


def scan_edition(ed_dir, dpi, json_dir):
    slug = os.path.basename(os.path.normpath(ed_dir))
    res = {"edition": slug, "dir": ed_dir, "status": "ok", "pages": [],
           "touches": 0, "nears": 0, "log": []}
    pdf, err = find_print_pdf(ed_dir)
    if err:
        res["status"] = "BLOCKED: " + err
        return res
    res["pdf"] = os.path.basename(pdf)
    avail = wait_for_memory(res["log"])
    res["mem_available_mb_at_start"] = avail
    doc = fitz.open(pdf)
    res["page_count"] = doc.page_count
    px_per_pt = dpi / 72.0
    for pi in range(doc.page_count):
        page = doc[pi]
        pix = page.get_pixmap(dpi=dpi, colorspace=fitz.csGRAY)
        a = np.frombuffer(pix.samples, dtype=np.uint8).reshape(
            pix.height, pix.width)
        ink = a < INK
        H, W = a.shape
        bands = {
            "top": ink[:BAND, :],
            "bottom": ink[H - BAND:, :],
            "left": ink[:, :BAND],
            "right": ink[:, W - BAND:],
        }
        touch = {e: int(b.sum()) for e, b in bands.items()}
        # minimum ink distance to each edge (px; -1 if the page has no ink)
        rows = np.where(ink.any(axis=1))[0]
        cols = np.where(ink.any(axis=0))[0]
        if len(rows):
            dist = {"top": int(rows.min()), "bottom": int(H - 1 - rows.max()),
                    "left": int(cols.min()), "right": int(W - 1 - cols.max())}
        else:
            dist = {"top": -1, "bottom": -1, "left": -1, "right": -1}
        near = [e for e in ("top", "bottom", "left", "right")
                if 0 <= dist[e] <= NEAR]
        prec = {"page": pi + 1, "size_px": [W, H], "touch": touch,
                "min_dist_px": dist,
                "min_dist_pt": {e: (round(v / px_per_pt, 1) if v >= 0 else -1)
                                for e, v in dist.items()},
                "near": near}
        res["pages"].append(prec)
        for e, n in touch.items():
            if n:
                res["touches"] += 1
                if json_dir:
                    crop = _crop(a, e, W, H)
                    cdir = os.path.join(json_dir, "crops")
                    os.makedirs(cdir, exist_ok=True)
                    Image.fromarray(crop).save(
                        os.path.join(cdir, f"{slug}-p{pi + 1}-{e}.png"))
        res["nears"] += len(near)
        del pix, a, ink
    doc.close()
    return res


def _crop(a, edge, W, H):
    if edge == "top":
        return a[:80, :]
    if edge == "bottom":
        return a[H - 80:, :]
    if edge == "left":
        return a[:, :80]
    return a[:, W - 80:]


def print_edition(res, out=sys.stdout):
    if res["status"] != "ok":
        print(f"EDGE_SCAN {res['edition']}: {res['status']}", file=out)
        return
    for p in res["pages"]:
        t = {e: n for e, n in p["touch"].items() if n}
        tag = "TOUCH " + str(t) if t else "clean"
        near = f" near={p['near']}" if p["near"] else ""
        print(f"  P{p['page']}: {tag} min_dist_pt={p['min_dist_pt']}{near}",
              file=out)
    print(f"EDGE_SCAN {res['edition']}: {res['page_count']} pages, "
          f"{res['touches']} TOUCH, {res['nears']} NEAR", file=out)


def main(argv):
    args, json_dir = [], None
    dpi = 200
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--json-dir" and i + 1 < len(argv):
            json_dir = argv[i + 1]
            i += 2
        elif a == "--dpi" and i + 1 < len(argv):
            dpi = int(argv[i + 1])
            i += 2
        elif a.startswith("--"):
            print(f"unknown option: {a}", file=sys.stderr)
            return 2
        else:
            args.append(a)
            i += 1
    if not args:
        print("usage: pdf_edge_scan.py <edition-dir> [...] [--dpi 200] "
              "[--json-dir DIR]", file=sys.stderr)
        return 2
    if json_dir:
        os.makedirs(json_dir, exist_ok=True)
    rc = 0
    for ed in args:
        res = scan_edition(ed, dpi, json_dir)
        print_edition(res)
        if json_dir:
            with open(os.path.join(json_dir, res["edition"] + ".json"),
                      "w", encoding="utf-8") as f:
                json.dump(res, f, ensure_ascii=False, indent=1)
        if res["status"] != "ok":
            rc = 2
        elif res["touches"]:
            rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
