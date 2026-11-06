#!/usr/bin/env python3
# Independent width measurement with the build library's own font metrics.
# Box-title font: Noto Sans CJK SC, 23pt, bold (svglib _font("sans", True, 23)).
# Slot: box x=1451 w=434 -> right edge 1885; title x=1469 -> 416px to edge.
import sys
sys.path.insert(0, '/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-en-build')
from svglib import text_w, _font
f = _font("sans", True, 23)
def w(s): return text_w(s, "sans", True, 23)
def ink(s):
    l,t,r,b = f.getbbox(s); return r-l
SLOT = 416.0
cases = [
 ("B1 shipped es", "HOW LONG ? · ¿Cuánto dura?"),
 ("B1 shipped pt", "HOW LONG ? · Quanto dura?"),
 ("B1 shipped ru", "HOW LONG ? · Каков срок?"),
 ("B1 shipped it (precedent)", "HOW LONG ? · Quanto dura?"),
 ("B1 full es (verdict proposal, house space)", "HOW LONG ? · ¿Cuánto dura el mandato?"),
 ("B1 full es (no house space)", "HOW LONG? · ¿Cuánto dura el mandato?"),
 ("B1 full pt (house space)", "HOW LONG ? · Quanto dura o mandato?"),
 ("B1 full pt (no house space)", "HOW LONG? · Quanto dura o mandato?"),
 ("B1 full ru (house space)", "HOW LONG ? · Каков срок полномочий?"),
 ("B1 full ru (no house space)", "HOW LONG? · Каков срок полномочий?"),
 ("B1 alt es: duration of term?", "HOW LONG ? · ¿Cuánto dura el cargo?"),
 ("B1 alt ru: genitive?", "HOW LONG ? · Каков срок полномочий"),
 ("M4 shipped nl", "SCROOGE'S NIGHT · Scrooge-nacht"),
 ("M4 shipped pt", "SCROOGE'S NIGHT · A noite"),
 ("M4 shipped de", "SCROOGE'S NIGHT · Scrooge-Nacht"),
 ("M4 shipped it", "SCROOGE'S NIGHT · La notte"),
 ("M4 full-caps nl", "SCROOGE'S NIGHT · DE NACHT VAN SCROOGE"),
 ("M4 full-caps pt", "SCROOGE'S NIGHT · A NOITE DE SCROOGE"),
 ("M4 mixed full nl", "SCROOGE'S NIGHT · De nacht van Scrooge"),
 ("M4 mixed full pt", "SCROOGE'S NIGHT · A noite de Scrooge"),
 ("M4 orig nl alone", "DE NACHT VAN SCROOGE"),
 ("M4 orig pt alone", "A NOITE DE SCROOGE"),
 ("M4 es candidate", "SCROOGE'S NIGHT · La noche de Scrooge"),
 ("M4 fr candidate", "SCROOGE'S NIGHT · La nuit de Scrooge"),
 ("M4 es/fr shipped", "LA NOCHE DE SCROOGE"),
 ("M4 fr shipped", "LA NUIT DE SCROOGE"),
 ("M4 es full-caps", "SCROOGE'S NIGHT · LA NOCHE DE SCROOGE"),
 ("M4 fr full-caps", "SCROOGE'S NIGHT · LA NUIT DE SCROOGE"),
 ("M4 COMING SOON es (control, fits)", "COMING SOON · Próximamente"),
 ("M4 longest shipped B1?", "HOW LONG ? · Wie lange im Amt?"),
]
for name, s in cases:
    print(f"{w(s):7.1f}px advance  ink {ink(s):7.1f}px  {'OVERFLOW' if w(s)>SLOT else 'fits    '}  {name}: {s!r}")
print("SLOT =", SLOT)
# Also verify: longest shipped box titles on P6/P3 across editions (from extraction) widths
