#!/usr/bin/env python3
"""Round 3 title-slot measurements: box-title font sans bold 23pt, slot 416px
(box x=1451 w=434, title x=1469). Measured with each edition's own svglib
(es/fr builds; nl/pt controls from their own builds)."""
import sys
BASE = '/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-en-%s-build'
import importlib
def measure(ed, strings):
    sys.path.insert(0, BASE % ed)
    import svglib
    importlib.reload(svglib)
    print(f"== {ed} build ==")
    for label, s in strings:
        w = svglib.text_w(s, "sans", True, 23)
        print(f"  {w:7.1f}px  {'OVERFLOW' if w > 416.0 else 'fits    '}  {label}: {s!r}")
    sys.path.pop(0)

measure('es', [("CURRENT es P3 title", "LA NOCHE DE SCROOGE"),
               ("PROPOSED es P3 title", "SCROOGE'S NIGHT · La noche"),
               ("full mixed (overflow control)", "SCROOGE'S NIGHT · La noche de Scrooge")])
measure('fr', [("CURRENT fr P3 title", "LA NUIT DE SCROOGE"),
               ("PROPOSED fr P3 title", "SCROOGE'S NIGHT · La nuit"),
               ("full mixed (overflow control)", "SCROOGE'S NIGHT · La nuit de Scrooge")])
measure('nl', [("SHIPPED nl P3 title (control)", "SCROOGE'S NIGHT · Scrooge-nacht")])
measure('pt', [("SHIPPED pt P3 title (control)", "SCROOGE'S NIGHT · A noite")])
print("SLOT = 416.0px")
