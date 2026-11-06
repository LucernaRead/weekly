# -*- coding: utf-8 -*-
"""Fix round for the W45 zh-cn x de build (builder self-check, before
independent proofread). Two classes, wording only, no frozen text touched:
  (a) 4 English strings missed by transform_de.py's table (found by a
      systematic shared-literal scan + a Latin-token scan of the render):
      P4 head 'Schedule work', P5 head 'Times & numbers', P6 head
      'Basket maths', P8 notes #125 and #135;
  (b) the solar-term name: transform_de.py rendered 立冬 as the English
      'Start of Winter' in German notes; the shipped W43 zh-cn-de
      precedent renders it 'Winteranfang' (content12.py:184,254), so all
      occurrences switch to 'Winteranfang' (with 'an Start of Winter'
      rephrased as 'zum Winteranfang').
Also recorded here: the P8-keys overflow fix (11 note tightenings) and
the P8 test-glossline shortening applied directly before the second
render, and the #109 colon fix (ASCII ':' after CJK '」' is converted
by svglib to full-width '：', which broke strict-CJK; reworded to avoid
the colon). Those three changes are already in the sources; this script
covers only (a)+(b) and asserts each replacement count.
"""
import glob, os

HERE = os.path.dirname(os.path.abspath(__file__))
FILES = sorted(glob.glob(os.path.join(HERE, "content*.py")))

R = [
    ("C · 读赛程 · Schedule work", "C · 读赛程 · Spielplan lesen"),
    ("C · 时间与数字 · Times & numbers", "C · 时间与数字 · Zeiten & Zahlen"),
    ("C · 练习篮子算一算 · Basket maths", "C · 练习篮子算一算 · Korbrechnen"),
    ("TES beat G2 on Oct 26.", "TES schlug G2 am 26. Okt."),
    ("shùzì — the AI film's characters are digital images.",
     "shùzì — die Figuren des KI-Films sind digitale Bilder."),
    ("an Start of Winter", "zum Winteranfang"),
    ("Start of Winter", "Winteranfang"),
]

def main():
    texts = {f: open(f, encoding="utf-8").read() for f in FILES}
    for old, new in R:
        n = sum(t.count(old) for t in texts.values())
        assert n >= 1, f"NOT FOUND: {old!r}"
        for f in FILES:
            texts[f] = texts[f].replace(old, new)
        print(f"  {n:3d}x  {old[:70]}")
    for f in FILES:
        open(f, "w", encoding="utf-8").write(texts[f])
    print("fix round applied")

if __name__ == "__main__":
    main()
