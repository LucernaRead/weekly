import glob, hashlib, os, subprocess, sys
from pathlib import Path
from pypdf import PdfWriter, PdfReader
import cairosvg

ROOT = Path.home()/"workspace/goals/lucernaread-social-media-operations"
SCRATCH = ROOT/"hidden_files/w46/fr-fix/scratch"
PY = str(ROOT/"tools/venv/bin/python")
# (edition dir suffix, build dir suffix, print pdf name, web pdf name, textmd name)
EDITIONS = [
    ("weekly-report-w46-fr-core", "weekly-report-w46-fr-build", "法语周报VOL4-大报版.pdf", "法语周报VOL4-网页版.pdf", "2026-w46-fr-zh-cn.text.md"),
    ("weekly-report-w46-fr-de", "weekly-report-w46-fr-de-build", "Le-Lucerna-VOL4-DE.pdf", "Le-Lucerna-VOL4-DE-web.pdf", "2026-w46-fr-de.text.md"),
    ("weekly-report-w46-fr-en", "weekly-report-w46-fr-en-build", "Le-Lucerna-VOL4-EN.pdf", "Le-Lucerna-VOL4-EN-web.pdf", "2026-w46-fr-en.text.md"),
    ("weekly-report-w46-fr-es", "weekly-report-w46-fr-es-build", "Le-Lucerna-VOL4-ES.pdf", "Le-Lucerna-VOL4-ES-web.pdf", "2026-w46-fr-es.text.md"),
    ("weekly-report-w46-fr-it", "weekly-report-w46-fr-it-build", "Le-Lucerna-VOL4-IT.pdf", "Le-Lucerna-VOL4-IT-web.pdf", "2026-w46-fr-it.text.md"),
    ("weekly-report-w46-fr-ja", "weekly-report-w46-fr-ja-build", "Le-Lucerna-VOL4-JA.pdf", "Le-Lucerna-VOL4-JA-web.pdf", "2026-w46-fr-ja.text.md"),
    ("weekly-report-w46-fr-ko", "weekly-report-w46-fr-ko-build", "Le-Lucerna-VOL4-KO.pdf", "Le-Lucerna-VOL4-KO-web.pdf", "2026-w46-fr-ko.text.md"),
    ("weekly-report-w46-fr-nl", "weekly-report-w46-fr-nl-build", "Le-Lucerna-VOL4-NL.pdf", "Le-Lucerna-VOL4-NL-web.pdf", "2026-w46-fr-nl.text.md"),
    ("weekly-report-w46-fr-pt", "weekly-report-w46-fr-pt-build", "Le-Lucerna-VOL4-PT.pdf", "Le-Lucerna-VOL4-PT-web.pdf", "2026-w46-fr-pt.text.md"),
    ("weekly-report-w46-fr-ru", "weekly-report-w46-fr-ru-build", "Le-Lucerna-VOL4-RU.pdf", "Le-Lucerna-VOL4-RU-web.pdf", "2026-w46-fr-ru.text.md"),
    ("weekly-report-w46-fr-zh-cn", "weekly-report-w46-fr-zh-cn-build", "Le-Lucerna-VOL4-ZH-CN.pdf", "Le-Lucerna-VOL4-ZH-CN-web.pdf", "2026-w46-fr-zh-cn.text.md"),
    ("weekly-report-w46-fr-zh-tw", "weekly-report-w46-fr-zh-tw-build", "Le-Lucerna-VOL4-ZH-TW.pdf", "Le-Lucerna-VOL4-ZH-TW-web.pdf", "2026-w46-fr-zh-tw.text.md"),
]
import os as _os
_only = _os.environ.get("FR_FIX_ONLY")
if _only:
    _keep = set(_only.split(","))
    EDITIONS = [e for e in EDITIONS if e[0] in _keep]
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def txtbytes(p):
    r = subprocess.run(["pdftotext", str(p), "-"], capture_output=True)
    assert r.returncode == 0, r.stderr
    return len(r.stdout)
def pages(p): return len(PdfReader(str(p)).pages)

for ed_dir, build_dir, print_name, web_name, textmd_name in EDITIONS:
    ed = ROOT/"files"/ed_dir
    sc = SCRATCH/ed_dir; sc.mkdir(parents=True, exist_ok=True)
    svgs = sorted(glob.glob(str(ed/"svg/*.svg")))
    assert len(svgs) == 8, (ed_dir, svgs)
    # cards
    for f in svgs:
        out = str(ed/"cards"/(Path(f).stem + ".png"))
        cairosvg.svg2png(url=f, write_to=out, output_width=1950)
    # print pdf
    w = PdfWriter()
    page_pdf = sc/"page.pdf"
    for f in svgs:
        cairosvg.svg2pdf(url=f, write_to=str(page_pdf))
        w.add_page(PdfReader(str(page_pdf)).pages[0])
    print_tmp = sc/"print-tmp.pdf"
    with open(print_tmp, "wb") as fh: w.write(fh)
    # web pdf
    r = subprocess.run([PY, str(ROOT/"tools/webpdf.py"), str(ed/"svg"), str(ed/web_name)], capture_output=True, text=True)
    assert r.returncode == 0, f"webpdf {ed_dir} failed: {r.stdout} {r.stderr}"
    # .text.md from source manuscript
    out_md = sc/"export.text.md"
    env = dict(os.environ, W46_BUILD_DIR=str(ROOT/"hidden_files"/build_dir), W46_OUT_MD=str(out_md))
    r = subprocess.run([PY, str(ROOT/"hidden_files/w46/text-export/export.py")], capture_output=True, text=True, env=env)
    assert r.returncode == 0, f"export {ed_dir} failed: {r.stdout} {r.stderr}"
    old = (ed/textmd_name).read_text(encoding="utf-8")
    assert "# Page 1" in old
    header = old.split("# Page 1")[0]
    body = out_md.read_text(encoding="utf-8")
    assert body.startswith("# Page 1")
    (ed/textmd_name).write_text(header + body, encoding="utf-8")
    # move print pdf into place
    (ed/print_name).write_bytes(print_tmp.read_bytes())
    # verify
    pp, wp = pages(ed/print_name), pages(ed/web_name)
    pt, wt = txtbytes(ed/print_name), txtbytes(ed/web_name)
    cards = sorted(glob.glob(str(ed/"cards/*.png")))
    print(f"{ed_dir}: cards={len(cards)} print={pp}pp { (ed/print_name).stat().st_size }B sha={sha(ed/print_name)[:12]} web={wp}pp {(ed/web_name).stat().st_size}B sha={sha(ed/web_name)[:12]} pdftotext print={pt} web={wt} equal={pt==wt} textmd={(ed/textmd_name).stat().st_size}B", flush=True)
    assert pp == 8 and wp == 8 and pt == wt and pt > 0 and (ed/web_name).stat().st_size < 7_000_000 and len(cards) == 8
print("FINISH ALL DONE")
