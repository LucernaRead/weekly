# -*- coding: utf-8 -*-
"""Export <slug>.text.md from an ES-family edition's own SVG text layer
(source-side: the SVGs are the manuscript's direct output; never from a PDF).
Usage: es_textmd.py <svg-dir> <slug> <out-path>"""
import re, sys, os, html
svgdir, slug, out = sys.argv[1:4]
pages = ["p1-portada","p2-vida","p3-cultura","p4-deporte","p5-juventud","p6-afondo","p7-lengua","p8-ejercicios"]
names = ["Portada","Vida","Cultura","Deporte","Juventud","A fondo","Lengua","Ejercicios y respuestas"]
lines = [f"# {slug}", ""]
for pg, nm in zip(pages, names):
    t = open(os.path.join(svgdir, pg + ".svg"), encoding="utf-8").read()
    texts = [html.unescape(x) for x in re.findall(r"<text[^>]*>(.*?)</text>", t, re.S)]
    lines.append(f"## {nm}")
    lines.append("")
    for tx in texts:
        tx = tx.strip()
        if not tx:
            continue
        if tx.startswith("La Lucerna · ") and "VOL." in tx:
            continue
        if re.match(r"^(第 \d+ 版 / 共 8 版|Page \d+ of 8|Seite \d+ von 8|Page \d+ sur 8|Pagina \d+ di 8|Página \d+ de 8|Pagina \d+ van 8|Страница \d+ из 8|\d+ ページ（全 8 ページ）|제 \d+쪽 / 총 8쪽|第 \d+ 頁 / 共 8 頁)$", tx):
            continue
        if tx == "La Lucerna":
            continue
        lines.append(tx)
        lines.append("")
    lines.append("")
open(out, "w", encoding="utf-8").write("\n".join(lines))
print("wrote", out, os.path.getsize(out))
