# Proofreader verdict — W46 FR family, Round 1

Independent proofreader (did not build the editions). Report-only; no edition file was edited.
Issue week 2026-11-09 – 2026-11-15. VOL.4. 150 exercises verified present (stems 1–149 + writing item 150; keys cover all 150).

## Gates re-run independently by the proofreader (builder logs not trusted)

All outputs in `hidden_files/w46/fr-proofread-gates/` (prefix `proofreader-*`):

- **Freeze** (`freeze.py diff` vs core SVGs), 2026-11-03T00:12:09Z — `proofreader-freeze-all.log`, 11 JSONs, `proofreader-freeze-adjudication.txt`: PASS as adjudicated for all 11. P1–P7: every removed string contains CJK except two punctuation-only fragments (`。`, `）。`); no French body text removed. P8 removed-no-CJK fragments are re-wrapped answer-key lines only, settled by p8 compare. Added CJK = 0 for de/en/es/it/nl/pt/ru; JA +2,277 / KO +2,456 = native explanation layers (expected); ZH-TW +1,012 = traditional forms vs simplified core. fr-zh-cn: 0 differences on all 8 pages. Residue scans: no Chinese in Latin/RU editions; no Hanja in KO; JA simplified-only hits are legitimate shinjitai; ZH-TW simplified-only scan found only shared glyphs.
- **P8** (`p8.py compare`), 2026-11-03T00:13Z — `proofreader-p8-all.log`: CLEAN for all 11. 116 noted in core and each edition, missing=[], extra=0, uncertain=[]. keydiff=[145] for all except fr-zh-cn keydiff=[]. Core noted set 121/150.
- **Occlusion** (`occlusion_audit.py`), 2026-11-03T00:13–00:14Z — `proofreader-occlusion-all.log`, 12 JSONs: selftest OK every run; **0 flags** for core + all 11 editions.
- **PDFs** (pypdf, 2026-11-03): all 11 editions have print + web PDFs, 8 pages each, extractable text present, web text bytes = print text bytes within each edition, all web PDFs < 7 MB (max 2.4 MB, zh-tw).
- **Visual round** (2026-11-03): all 96 rendered cards viewed (core + 11 editions × 8 pages) at ~950px. No overflow, overlap, footer intrusion, or image/credit misplacement. One reflow observation checked and cleared: fr-zh-tw P2 moves the line "novembre se lit comme une phrase" from the article (col. 3) into the "LA SEMAINE EN CHIFFRES" box (SVG y=1518.335 vs core x=989 y=223.5); no text lost or added, no collision, meaning preserved — not a defect.

## Round 1 defects (all open)

- **D1 — ALL 11 editions. P3, item 37.** Stem: `(plus) La foire est à Paris. → ___`. P8 key: `La foire n'est plus à Paris.` The correction presupposes the fair was previously in Paris; the issue places the fair in Dieppe throughout. Factually correct negation is `ne...pas`. Fix: change the operator or reword the stem.
- **D2 — Item 135 stem/key mismatch in fr-it, fr-nl, fr-pt, fr-ru, fr-ja, fr-ko.** Printed French key (all editions): `Lire un programme, c'est déjà comprendre la France.` Stems in these 6 mean "A programme explains France" (IT `Un programma spiega la Francia.`; NL `Een programma legt Frankrijk uit.`; PT `Um programa explica a França.`; RU `Программа объясняет Францию.`; JA `番組がフランスを説明する。`; KO `프로그램이 프랑스를 설명한다.`). A faithful translation of any of these differs from the printed key. Faithful stems in the other 5 (EN/DE/ES/zh-cn/zh-tw) accepted.
- **D3 — P4 gloss `familier` wrong sense in fr-ja, fr-ko, fr-ru, fr-zh-tw.** Text occurrence: `les noms des villes deviennent familiers` ("become familiar"). Glosses: JA `familier くだけた`, KO `familier 구어체`, RU `familier разговорное`, ZH-TW `familier 口語` (all = informal/colloquial). Correct sense in the other editions (DE `vertraut`, EN `familiar`, ES `familiar`, IT `familiare`, NL `familiair`, PT `familiar`, zh-cn `熟悉的`).
- **Flag F-MAIL — mailbox premise UNVERIFIED, all 11 editions (pre-insert coordinator check, not a text defect).** Disclosure wording IS present and consistent in all 11 (French label `Exemple de la rédaction (ce texte n'est pas une lettre de lecteur)`, French note `Note de la rédaction: aucun texte du VOL.3 n'était arrivé au moment de mettre sous presse. Le VOL.5 reprendra la promesse.`, plus a native-language note to the same effect). The underlying claim (no real submissions arrived) could not be verified by builder or proofreader (no mailbox access). Coordinator must verify mailbox state before insert — covering submissions of any vintage (W45 promise also covered VOL.2) — and replace the example/disclosure if real letters exist.

W45-promises handling verified against `hidden_files/w46/w45-promises.md`: Paris Masters results correctly deferred (no results invented; Sinner withdrawal corrected); budget-vote self-correction present and consistent; 18 Nov Senate vote only as hedged `est prévu` (confirmed by schedule reporting); readers' corner uses the labelled editorial example, no fabricated reader. External spot-checks (Sinner 6 Oct season end; 115–1 vote 23 Oct; Dieppe 56th fair 14–15 Nov; Paris Photo 29th ed. 12–15 Nov; Senate solemn vote 18 Nov) all confirmed the KIT sourcing. Level-count claim (A2 52 / B1 75 / B2 23) not independently reproducible from the printed artifact — unverified internal metadata, not a defect.

## Verdicts — Round 1: FAIL for all 11 editions

| Slug | Open defects | Verdict |
|---|---|---|
| 2026-w46-fr-de | D1 | FAIL (Round 1) |
| 2026-w46-fr-en | D1 | FAIL (Round 1) |
| 2026-w46-fr-es | D1 | FAIL (Round 1) |
| 2026-w46-fr-it | D1, D2 | FAIL (Round 1) |
| 2026-w46-fr-ja | D1, D2, D3 | FAIL (Round 1) |
| 2026-w46-fr-ko | D1, D2, D3 | FAIL (Round 1) |
| 2026-w46-fr-nl | D1, D2 | FAIL (Round 1) |
| 2026-w46-fr-pt | D1, D2 | FAIL (Round 1) |
| 2026-w46-fr-ru | D1, D2, D3 | FAIL (Round 1) |
| 2026-w46-fr-zh-cn | D1 | FAIL (Round 1) |
| 2026-w46-fr-zh-tw | D1, D3 | FAIL (Round 1) |

Flag F-MAIL applies to every edition as a pre-insert coordinator check. No edition may ship until D1–D3 are fixed, the editions are fully re-rendered, and a full zero-issue proofread round (Round 2) is completed.
