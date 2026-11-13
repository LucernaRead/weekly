# PROGRESS — fr-ru fix-ru2 (coordinator #4 repair worker)

- Started 2026-11-13 ~01:25 UTC. Scope: 5 gate defects (occlusion P1 + boxtitle P3/P4/P5/P6)
  + B1 answer 141 `vainqueur = чемпион` → `победитель`. Edition 2026-w47-fr-ru ONLY.
- Coordination: fr-family worker (scratch-fix-fr-family1/) had NOT started as of
  01:24 UTC (dir absent, no process touching fr-ru). I go first; if it starts
  later it must build on top of my state, not overwrite it.
- Pre-fix SHAs (gate-final, 2026-11-13 00:23–00:42 UTC):
  print La-Lucerna-VOL4-fr-ru.pdf 1aa7c71d7f2e / 17,222,306 B
  web   La-Lucerna-VOL4-fr-ru-web.pdf 85c45f1cff46 / 1,773,870 B
  text  2026-w47-fr-ru.text.md 028cb8c2d4b0 / 50,495 B
- Fixes (each deletes exactly one word, verified by measure3.py against the
  edition's own svglib ink math; all reproduce gate numbers exactly):
  1. P1 occlusion: content12.py:28 headline `ALCARAZ GAGNE PARIS, LE SÉNAT VOTE MERCREDI`
     → `ALCARAZ GAGNE PARIS, LE SÉNAT VOTE` (drop MERCREDI; day stays in article/date box).
     Ink ends 1124.0, clearance +178.5px vs audit gloss start 1302.5.
  2. P3 boxtitle: expl.py head_zoom `ZOOM　LES DATES EN CHIFFRES` → `ZOOM　DATES EN CHIFFRES`.
     Ink over -44.4px (was +7.6).
  3. P4 boxtitle: content34.py:158 f.box `LES PHRASES DU COMMENTATEUR`
     → `PHRASES DU COMMENTATEUR`. Ink over -15.5px (was +36.5).
  4. P5 boxtitle: expl.py head_cine `LE CINÉМА DU MERCREDI　КИНО`
     → `CINÉМА DU MERCREDI　КИНО`. Ink over -16.2px (was +21.3).
  5. P6 boxtitle: expl.py head_3dates `TROIS DATES POUR COMPRENDRE`
     → `DATES POUR COMPRENDRE`. Ink over -57.5px (was +24.5).
  6. B1: expl.py m_p8b `vainqueur = чемпион　b` → `vainqueur = победитель　b`
     (unifies with P1 gloss `un vainqueur победитель`).
- Status: [x] measured [x] source edits [x] text.md re-export+diff (exactly 6 lines)
  [x] rebuild [x] full gates (FAILFLAG=0; see GATE-LOG-fix-ru2.md) [x] KIT update.
  DONE 2026-11-13 ~01:35 UTC. NO commit / NO push.
- New SHAs: print af7d37bc0a56 / 17,222,281 B; web f6e82ee074cf / 1,773,854 B;
  text ae0a0429047a / 50,475 B.
- Coordination note for the fr-family worker: this fix-ru2 build (01:27 UTC) is
  the current fr-ru state. Any family work on fr-ru must start from these
  post-fix sources/SHAs, not from your 01:20 pre-shas snapshot, and must not
  overwrite these 6 fixes.
