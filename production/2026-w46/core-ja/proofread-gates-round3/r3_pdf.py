# Round 3 independent PDF verification: sizes, page counts, pdftotext web vs print.
import glob, os, subprocess, json
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files")
EDITIONS = [("zh-cn", "weekly-report-w46-ja-core", "Lucerna-VOL3"),
            ("de", "weekly-report-w46-ja-de", "Lucerna-VOL3-DE"),
            ("en", "weekly-report-w46-ja-en", "Lucerna-VOL3-EN"),
            ("es", "weekly-report-w46-ja-es", "Lucerna-VOL3-ES"),
            ("fr", "weekly-report-w46-ja-fr", "Lucerna-VOL3-FR"),
            ("it", "weekly-report-w46-ja-it", "Lucerna-VOL3-IT"),
            ("ko", "weekly-report-w46-ja-ko", "Lucerna-VOL3-KO"),
            ("nl", "weekly-report-w46-ja-nl", "Lucerna-VOL3-NL"),
            ("pt", "weekly-report-w46-ja-pt", "Lucerna-VOL3-PT"),
            ("ru", "weekly-report-w46-ja-ru", "Lucerna-VOL3-RU"),
            ("zh-tw", "weekly-report-w46-ja-zh-tw", "Lucerna-VOL3-ZHTW")]
out = {}
for code, d, stem in EDITIONS:
    web = os.path.join(BASE, d, stem + "-web.pdf")
    prn = os.path.join(BASE, d, stem + ".pdf")
    def txt(pdf):
        r = subprocess.run(["pdftotext", pdf, "-"], capture_output=True)
        return r.stdout
    w, p = txt(web), txt(prn)
    from pypdf import PdfReader
    wp, pp = len(PdfReader(web).pages), len(PdfReader(prn).pages)
    out[code] = {"web_bytes": os.path.getsize(web), "print_bytes": os.path.getsize(prn),
                 "web_pages": wp, "print_pages": pp,
                 "web_text_bytes": len(w), "print_text_bytes": len(p),
                 "web_eq_print": w == p, "web_le_7mb": os.path.getsize(web) <= 7 * 1024 * 1024}
    print(code, out[code])
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "pdf-round3.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("wrote pdf-round3.json")
