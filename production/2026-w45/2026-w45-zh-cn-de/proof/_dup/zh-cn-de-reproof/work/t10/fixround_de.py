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
Also encoded here (Gate 10 fix, 2026-10-28): the P8-keys overflow fix
(11 exercise-note shortenings, two literals occurring in both the test
pages and the P8 keys, so 13 occurrences), the P8 test-glossline
shortening, and the #109 colon fix (ASCII ':' after CJK '」' is converted
by svglib to full-width '：', which broke strict-CJK; reworded to avoid
the colon). These were first applied as direct source edits before the
second render; they are now encoded below as R2 so that transform +
fixround alone reproduce the delivered SVGs (Gate 10). R2 runs after R
and asserts each replacement count, like R.
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

# R2: fix-round-1 tightenings (Gate 10, 2026-10-28). Exact unique
# literals, bare text (the glossline pair is a plain string so that
# {NCHARS} stays a literal placeholder, per tools README #18).
R2 = [
    ("Die Vorverkäufe von Taobao und Tmall begannen am 15. Okt.",
     "Vorverkauf bei Taobao und Tmall ab 15. Okt."),
    ("Die Spot-Verkäufe von Taobao und Tmall begannen am 20. Okt.",
     "Spot-Verkauf bei Taobao und Tmall ab 20. Okt."),
    ("Ein Journalist interviewt Menschen und schreibt Nachrichten.",
     "Journalist: interviewt und schreibt Nachrichten."),
    ("jìzhě — ein Journalist interviewt und schreibt Nachrichten.",
     "jìzhě — Journalist: interviewt, schreibt Nachrichten."),
    ("Das Finale beginnt um 03:00 Uhr Pekinger Zeit am 15. Nov.",
     "Finale: 15. Nov., 03:00 Uhr Pekinger Zeit."),
    ("piàofáng — Einnahmen aus dem Kartenverkauf, etwa 1,192 Mio. Yuan.",
     "piàofáng — Kartenverkauf, etwa 1,192 Mio. Yuan."),
    ("Am 24.–25. Okt. hatte jede Vorstellung im Schnitt 2 Zuschauer.",
     "24.–25. Okt.: im Schnitt 2 Zuschauer je Vorstellung."),
    ("Mit 直降 ist der Preis an der Kasse der Preis, den Sie zahlen.",
     "Mit 直降 ist der Kassenpreis der Zahlpreis."),
    ("「最低价」 ist eine Werbebehauptung, keine gemessenen Daten.",
     "「最低价」 ist Werbung, keine gemessenen Daten."),
    ("Spot-Ware wird sofort versandt, keine Vorverkaufswartezeit.",
     "Spot-Ware: sofort versandt, keine Vorverkaufswartezeit."),
    ("Schreiben — es gibt keine einzige richtige Antwort. Es folgt ein Mustertext mit {NCHARS} Zeichen.",
     "Schreiben — keine einzige richtige Antwort. Ein Mustertext mit {NCHARS} Zeichen folgt."),
]

def main():
    texts = {f: open(f, encoding="utf-8").read() for f in FILES}
    for old, new in R:
        n = sum(t.count(old) for t in texts.values())
        assert n >= 1, f"NOT FOUND: {old!r}"
        for f in FILES:
            texts[f] = texts[f].replace(old, new)
        print(f"  {n:3d}x  {old[:70]}")
    for old, new in R2:
        n = sum(t.count(old) for t in texts.values())
        assert n >= 1, f"NOT FOUND (R2): {old!r}"
        for f in FILES:
            texts[f] = texts[f].replace(old, new)
        print(f"  R2 {n:3d}x  {old[:70]}")
    for f in FILES:
        open(f, "w", encoding="utf-8").write(texts[f])
    print("fix round applied")

if __name__ == "__main__":
    main()
