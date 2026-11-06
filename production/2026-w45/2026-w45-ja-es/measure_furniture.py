# -*- coding: utf-8 -*-
"""Three-way furniture measurement: W43 JA x ES vs W45 JA core vs this
W45 JA x ES edition. Measures P1 masthead geometry (wordmark, edition
line, badge, tagline, rules, dark band) + footers/page lines on all pages
from the shipped SVGs. Usage: measure_furniture.py"""
import os, re, sys
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools"))
from occlusion_audit import ink_box, parse_attrs
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
EDITIONS = {
    "W43-ja-es": "files/weekly-report-ja-es/svg",
    "W45-core": "files/weekly-report-w45-ja-core/svg",
    "W45-ja-es": "files/weekly-report-w45-ja-es/svg",
}
for name, rel in EDITIONS.items():
    p1 = open(os.path.join(BASE, rel, "p1-hyoushi.svg"), encoding="utf-8").read()
    nodes = re.findall(r'<text([^>]*)>([^<]*)</text>', p1)
    print(f"== {name} P1 masthead ==")
    for attrs, s in nodes:
        a = parse_attrs(attrs)
        if s.strip() in ("Lucerna",) or "TEXTOS EN JAPONÉS" in s or "TEXT IN JAPANESE" in s \
                or "日本語版" in s or "日本語を学ぶ人のための週刊新聞" in s:
            ib = ink_box(s.replace("&amp;", "&"), a.get("font-family", ""), float(a.get("font-size", 20)),
                         a.get("font-weight", "") == "700", float(a.get("x", 0)), float(a.get("y", 0)),
                         a.get("text-anchor", "start"))
            print(f"  y={a.get('y')} size={a.get('font-size')} weight={a.get('font-weight')} fill={a.get('fill')} "
                  f"ink=({ib[0]:.1f}..{ib[2]:.1f}) width={ib[2]-ib[0]:.1f} :: {s[:80]!r}")
    rules = re.findall(r'<line x1="(\d+)" y1="([\d.]+)" x2="(\d+)" y2="([\d.]+)" stroke="([^"]*)" stroke-width="([^"]*)"/>', p1)
    for x1, y1, x2, y2, st, sw in rules:
        if float(y1) < 600:
            print(f"  rule y={y1} stroke={st} w={sw} x={x1}..{x2}")
    bands = re.findall(r'<rect x="(\d+)" y="(\d+)" width="(\d+)" height="(\d+)" fill="#2c2822"', p1)
    print(f"  dark bands: {bands[:3]}")
    print(f"== {name} footers (all pages) ==")
    for pg in ["p1-hyoushi.svg", "p2-kurashi.svg", "p8-tesuto.svg"]:
        t = open(os.path.join(BASE, rel, pg), encoding="utf-8").read()
        for attrs, s in re.findall(r'<text([^>]*)>([^<]*)</text>', t):
            a = parse_attrs(attrs)
            if a.get("y") == "2624":
                print(f"  {pg} :: {s!r}")
