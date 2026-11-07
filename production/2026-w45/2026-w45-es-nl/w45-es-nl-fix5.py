# -*- coding: utf-8 -*-
"""Fix 5: P7 col-3 compression (EN KIT §3.7 precedent). NL col 3 ran 87px
taller than the core (word note 4 lines vs 3, disclosure 5 vs 3), pushing
the VOL.3 preview onto the footer (occlusion TEXTX, real defect). Word
note 4 -> 3 lines and disclosure 5 -> 3 lines restore the core geometry
exactly (col3 ends 1820.08, preview title 2484.08). Disclosure keeps all
three facts: no real letters, no best page-8 texts, example printed with
the promise carried to VOL.3."""
import pathlib, sys
B = pathlib.Path('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-es-nl-build')
def rep(fn, old, new, expect):
    p = B / fn
    t = p.read_text(encoding='utf-8')
    c = t.count(old)
    if c != expect:
        print(f'COUNT MISMATCH {fn}: found {c}, expected {expect}'); sys.exit(1)
    p.write_text(t.replace(old, new), encoding='utf-8')
    print(f'{fn}: trimmed x{c}')
rep('content7.py', 'precampaña = de precampagne: de weken vóór de officiële campagne. Dit hele nummer is precampaña; de campagne begint vrijdag de 13e.',
    'precampaña = de precampagne, vóór de campagne. Dit nummer is precampaña; de campagne start vrijdag de 13e.', 2)
rep('content7.py', 'Opmerking van de redactie: bij het ter perse gaan waren er geen echte brieven of beste pagina-8-teksten binnen; daarom drukken we deze voorbeeldbrief af en de belofte schuift door naar VOL.3.',
    'Opmerking: geen echte brieven of beste pagina-8-teksten; daarom een voorbeeldbrief. Belofte: VOL.3.', 1)
print('FIX5 OK')
