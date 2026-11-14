# A Lucerna VOL.2 — Edición PT × ES (W45)

- **Emparejamiento**: texto en portugués (brasileño) + explicaciones en español — la edición para los lectores hispanohablantes.
- **Semana**: 2026-W45 · Semana del 2 al 8 de noviembre de 2026 · VOL.2
- **Fuente**: edición núcleo PT × zh-CN (`files/weekly-report-w45-pt-core/`, VOL.2). El texto portugués está **congelado**: solo se reescribió la capa de explicación, en español nativo y completo (glosas, notas de gramática, instrucciones y la totalidad de las notas de respuesta de la página 8).
- **Directorio de build**: `hidden_files/weekly-report-w45-pt-es-build/` (copia del build del núcleo + `transform.py`, única fuente de todos los cambios). La copia sin modificar reprodujo primero los 8 SVG entregados del núcleo **byte a byte** (freeze.py baseline 8/8, véase abajo).

## Specs

- 8 páginas, 1950×2700, 4 columnas, marfil cálido #f7f1e2, acentos verde oliva oscuro / rojo ladrillo #a4553a.
- **150 ejercicios** — A2 49 · B1 70 · B2 31; por página 10/18/18/18/18/18/12/38. Registro (n.º, página, nivel, tipo) **idéntico** al núcleo en n.º/página/nivel; los nombres de tipo se localizaron al español (véase § Tipos) sin cambiar ningún tipo semántico.
- Tipos: completar la frase 61 · opción múltiple 49 · emparejar vocabulario 12 · construir frases 7 · verdadero o falso 3 · cloze 13 · traducción 4 · escritura 1.
- Escritura: texto modelo 93 palabras (contado desde el render: `Texto modelo: …`, 93; coincide con la indicación 80–100 del enunciado).
- Masthead: **A Lucerna**. Línea de edición de la página 1: «SEMANARIO EN PORTUGUÉS · VOL.2 · A SEMANA DO ENEM · FINADOS · O FUTEBOL DECIDE» (38 pt; a 40 pt medía 1876 px > 1820, a 38 pt mide 1782 px).
- **Distintivo página 1** (rojo ladrillo #a4553a, en negrita, en el hueco del strapline del núcleo, exactamente como la edición W43 PT × ES): «TEXTOS EN PORTUGUÉS · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES» (1052,9 px ≤ 1820).
- Franja superior página 1: «TODA SEMANA EM PORTUGUÊS · CADA SEMANA · EL PORTUGUÉS QUE LEE BRASIL» (cadena española reutilizada verbatim de W43 PT × ES); banda negra a la derecha: «SEMANA DEL ENEM» / «2 nov: puente de Finados · 8 nov: día 1 del Enem».
- **Pies de página (8 páginas)**: «A Lucerna · SEMANARIO PORTUGUÉS VOL.2 · TEXTO EN PORTUGUÉS · EXPLICACIONES EN ESPAÑOL» y «Página N de 8».
- Prefijo de las cajas de glosas: «Nota — ». Separador P8: «— PÁGINA N —». **P8 conserva el estilo guion del núcleo W45** (`N. clave — nota`, escritura `N. ✓ nota`), igual que la edición hermana W45 PT × EN; el estilo paréntesis de W43 PT × ES pertenecía al aparato del núcleo W43 y no se traslada (véase § Desviaciones frente a W43).
- Glosas: P2 6 · P3 6 · P4 5 · P5 5 · P6 4 = **26**, 1:1 con el núcleo, contadas partiendo la cadena `gloss()` por `·` (no por ` · `, lección README #21); las 26 sobreviven en el render.

## P7: definiciones congeladas, solo la glosa se localiza

- La frase de definición portuguesa de la caja «A PALAVRA» (« feriadão »: sábado, domingo e segunda — três dias de descanso.) se conserva **verbatim**; solo la glosa pasa al español («feriadão = el puente festivo.»). La misma regla rige para todas las lenguas (criterio general: la definición en la lengua meta no se traduce).
- **Citas P7**: las 8 citas aparecen exactamente 2× en la edición (artículo + caja), con etiquetas de página (1, 1, 2, 3, 4, 5, 6, 2) correctas y traducción española en la caja.
- **Rincón de los lectores (sin invención)**: la carta impresa es el **ejemplo de la redacción** del núcleo, sin firma ni lector ficticio. La página lleva: (1) la etiqueta «Ejemplo de la redacción, no una carta real. ¡Envíanos tu carta! Las mejores se publicarán en el VOL.3.» — invitación explícita en imperativo con promesa de publicación en VOL.3 (la línea de avance de la semana NO cuenta como invitación y no se usa como tal); (2) la revelación aplazada con los 3 hechos — no llegaron cartas reales, no llegó el mejor texto de la página 8, el ejemplo queda y la promesa pasa al VOL.3 — **en portugués original** (disc_pt, verbatim del núcleo) **y en frase española equivalente** (disc_es). No hay lectores, cartas, nombres ni citas inventadas en ninguna página.

## Registro de diferencias de claves (ES vs núcleo)

Claves **impresas** idénticas salvo los 2 ítems de traducción PT→ES (reorientación legal: la clave debe estar en la lengua del lector):

| # | Tipo | Núcleo (zh-CN) | Esta edición (ES) |
|---|------|----------------|--------------------|
| 137 | Traducir (PT→lector) | clave = traducción china de la frase PT | clave = «El domingo 8 de noviembre es el primer día del Enem.» — nota «Véase el titular de la página 6» |
| 138 | Traducir (PT→lector) | clave = traducción china de la frase PT | clave = «Comprueba tu tarjeta antes del domingo.» — nota «Confira = comprueba» |

Los ítems 139/140 (lector→PT) conservan la clave portuguesa del núcleo y solo cambian el enunciado al español («El puente festivo va del 31 de octubre al 2 de noviembre.» → «O feriadão é de 31 de outubro a 2 de novembro.»; «Cuando llegues, presenta tu documento con foto.» → «Quando você chegar, apresente o documento com foto.»). La clave de registro del ítem 150 (escritura, no impresa: la línea impresa usa `✓`) pasa de la clave china del núcleo a «(pregunta abierta)»; su nota impresa es «el texto modelo está en la sección H: 93 palabras».

## Keydiffs de p8.py: adjudicación ítem por ítem

`p8.py compare` → **CLEAN 150=150**, keydiff [2, 4, 101, 137, 138, 146]:

- **137, 138 — redirecciones reales y legales** (véase la tabla anterior).
- **2, 4, 101, 146 — artefactos de la rama paréntesis del extractor, NO diferencias reales.** Confrontación byte a byte de la clave impresa (extraída del SVG):
  - 2: núcleo `portões` = edición `portões` (línea impresa: `2. portões — portões = las puertas (las del lugar del examen)`).
  - 4: núcleo `13h30` = edición `13h30` (`4. 13h30 — 13h30: el examen empieza (hora de Brasilia)`).
  - 101: núcleo `confiro` = edición `confiro` (`101. confiro — conferir: eu → confiro (irregular)`).
  - 146: núcleo `A` = edición `A` (`146. A — sección = la zona del examen (la sala)`).
  - Mecanismo: `detect_note` trata como estilo paréntesis cualquier línea cuyo grupo paréntesis de media anchura quede al final de la nota; las notas españolas usan paréntesis de media anchura `(…)`, mientras que las del núcleo usan paréntesis de anchura completa `（…）` que esa rama no reconoce. Por eso el núcleo extrae limpio y la edición no, con claves impresas idénticas. No se tocó `tools/p8.py` (el veredicto ya es CLEAN y el keydiff es informativo); la adjudicación queda registrada aquí para la relectura.

## Rondas de arreglo (con baselines sha256 previas en el build)

- **Ronda 1** (baseline `build-round1-baseline.sha`): 150/150 ejercicios, niveles y páginas exactos, 93 palabras, cero FLOW OVERFLOW / HEAD TOO WIDE. Auditoría: edición 9 flags / núcleo 0 / NEW 9 — todos reales, todos en P7: la pila de la columna 3 terminaba en y=2027,5 y empujaba las citas 3.ª/4.ª fila bajo la banda oscura «A PRÓXIMA SEMANA» y hasta la banda del pie.
- **Ronda 2** (baseline `build-round2-baseline.sha`): acortadas las 4 notas de la clínica de errores a una línea cada una (118 px) y la glosa de la caja de la palabra a una línea (29 px) → columna 3 en y=1880,5; espaciado de citas 128→104. Auditoría: 1 flag — BOXTITLE real: el descendente de la glosa de la palabra presionaba el borde 0,6 px (tinta 1283,1 > borde 1282,5).
- **Ronda 3** (baseline `build-round3-baseline.sha` = estado final): almohadilla inferior de la caja de la palabra 20→30 (misma receta que W45 PT × EN). Auditoría final: **0 flags**; columna 3 en y=1890,5; última línea de traducción de cita ≈ y=2380, libre de la banda de avance (2404).
- Todas las ediciones de ronda van sincronizadas en `transform.py` (ningún arreglo quedó solo en un archivo de contenido); cada re-render pasó por el driver único `run.py` en un solo proceso (registro compartido). Reproducibilidad verificada: `transform.py` sobre una copia prístina del build del núcleo reproduce los 7 fuentes (bslib4, content12/34/56/7/8, render.py) **byte a byte**.

## Auditorías (puertas SOP, pasada final)

- **Congelación**: freeze.py baseline del núcleo 8/8 byte-idéntico (p1 0dc8089d…, p2 56db3aa8…, p3 82f6fc3a…, p4 c5647cf6…, p5 92e86020…, p6 e6097473…, p7 a72cb75a…, p8 82630480…); SVGs del núcleo re-hasheados sin cambios tras el build. freeze.py diff: **CJK añadido = 0 en las 8 páginas** (núcleo 156/177/153/148/223/118/357/1123 → edición 0); toda la diferencia de cadenas clasificada como capa española / mobiliario de emparejamiento / ítems documentados; imágenes byte a byte idénticas (hash P1 fd231e77993f09e0 en núcleo y edición).
- **Geometría**: occlusion_audit.py (autotest previo OK, 6 clases): **edición 0 / núcleo 0 / NEW 0**. Escaneo de colisiones en la misma línea base: 0. Cruces de marco por tinta: 0 (márgenes mínimos I/D/A/B = 23,0/13,0/30,0/31,0). Escaneo del borde derecho por ADVANCE: 0 cruces. Cobertura de etiquetas del gráfico P6 por el método de tinta anclada en la línea base (PIL getbbox, anchor ls): todas < 30 % (prova 0,0 · portões abertos 0,0 · 60 min 0,0 · espera 0,0 · 30 min 0,0 · 330 min 0,0). Cruces título-de-caja/borde: 0 (incluido en la auditoría). Máxima línea base de claves P8: 2547,7 < fondo de flujo 2552 < regla del pie 2580.
- **P8**: compare CLEAN 150=150 (véase la adjudicación anterior); conjunto de notas impresas igual (EXTRA_ONLY: ninguno); notas P8 íntegramente en español.
- **Conteo independiente desde los SVG** (`gates.py`, `gates-final.log`, FAILURES: none): expansión chip+número por página = 150 ejercicios, niveles 49/70/31, unión 1..150 sin huecos ni duplicados; claves P8 agrupadas por página = 10/18/18/18/18/18/12/38; palabras del modelo desde el render = 93; distintivo, pie y línea de página 8/8; residuo chino por página = 0; término intermedio prohibido (forma china) = 0 en papel, KIT y código.
- **Hechos y calendario 2026** (heredados del núcleo, sin cambios): 2 nov = lunes (Finados), 3 nov = martes (vuelven las asambleas), 7 nov = sábado, 8 nov = domingo (Enem día 1), 15 nov = domingo (Enem día 2, solo avance). Sin resultados ni clasificaciones: los partidos de vuelta aún no se han jugado (la página 4 dice «resultados en la próxima edición»).
- **Aritmética re-verificada**: 60 + 30 + 330 = 420; 5×60 + 30 = 330; mediodía a 19h = 7 horas.

## Desviaciones frente a W43 PT × ES (la edición ya publicada del mismo emparejamiento)

1. **VOL.2** en lugar de VOL.1 (cambio de semana/núcleo, no una decisión).
2. **P8 en estilo guion del núcleo W45** en lugar del estilo paréntesis de W43 (decisión de familia W45 + precedente de la hermana W45 PT × EN; `p8.py` cubre ambos estilos; compare CLEAN).
3. **Línea de edición P1 a 38 pt** (W43: 36 pt) — medida: a 40 pt del núcleo desborda (1876 px); a 38 pt mide 1782 px.
4. **Nombres de tipo localizados al español** (W43 conservaba los nombres chinos como metadatos). Los tipos nunca se imprimen; el registro semántico es idéntico.
5. **Caja de la palabra con almohadilla inferior 30 y espaciado de citas 104** (geometría del núcleo W45, sin equivalente en W43).
6. **Rincón de los lectores con revelación aplazada** (disc_pt + disc_es): heredado del núcleo VOL.2 (corrección FIX1); W43 VOL.1 no tenía esa brecha de promesa.
7. **Sin desviación**: distintivo, pie, línea de página, prefijo «Nota — », franja superior española, títulos «BREVE» / «QUIZ RÁPIDO» / «CUÉNTANOS» y formato de notas de emparejamiento (`palabra = glosa: letra`) son verbatim de W43 PT × ES.

## Corrección del constructor (lectura propia de las 8 tarjetas)

Las 8 tarjetas leídas página a página: ortografía y acentuación del español, concordancia, cada nota contra su enunciado, mobiliario y distintivo de emparejamiento en las 8 páginas, etiquetas del gráfico P6 íntegramente visibles, citas P7 íntegramente visibles sobre la banda de avance, claves P8 íntegramente visibles sobre la regla del pie. Sin problemas pendientes tras la ronda 3.

## Entregables

- `svg/` ×8, `cards/` ×8 (1950×2700)
- PDF de impresión: `Lucerna-VOL2-ES.pdf` — 3.471.166 bytes, sha256 `83fa3515fbfefd9f2b84ec31f425808e6420a250aaffbcc5fe4ed9c0088ddc06`
- PDF web: `Lucerna-VOL2-ES-web.pdf` — 3.494.583 bytes (< 10 MB), sha256 `892eb78d9e91e7fd5865082abe05e90e01b37108d9be1f18bb3c77e1d5d64762`

- D5 rebuild (2026-11-14, see D5 rebuild section at the end of this KIT) + F-A fix (2026-11-14, D36, see F-A fix section at the end of this KIT): print master `A-Lucerna-VOL2-pt-es.pdf` **2279787 B** · sha256 `5ab8f976742ff018d86ccd9d41e453c3b37a99616bd0ad7e094bd07be6498421`; render-web `A-Lucerna-VOL2-pt-es-web.pdf` **3112573 B** · sha256 `703d95bb9cbc5637bbb395ba23c5b8b394cbae192e48576e9dd7799498bda964`; web (issues-type) `2026-w45-pt-es.web.pdf` **761152 B** · sha256 `74eccc8e2c6257c5d338ca71cdc127a8c84adf2ff0eacada1641243555897d64` (< 7 MB); text.md differs from the shipped version by exactly 2 lines (F-A fix, D36 + D34 typo, D34; sha256 `ad15135b8dc9ca5838bc181222dee33ecb404f43faaae2d8f9f4816472cab7e2`, 31980 B; run2 value was BYTE-IDENTICAL, 31983 B, `b34b54658ce011002747336e4da5b1a24a3d93a9c96819a7d4b8bac204e247ba`). Pre-D5 KIT pins above are D1-era values, already expired before this rebuild.
- `ABSTRACT.txt` (una línea, sin comillas ASCII dobles, en español)

## Reproducción

```
cd hidden_files/weekly-report-w45-pt-es-build
<tools/venv>/bin/python transform.py   # desde una copia prístina del build del núcleo; reproduce los 7 fuentes byte a byte
<tools/venv>/bin/python run.py         # genera los SVG en files/weekly-report-w45-pt-es/svg/
<tools/venv>/bin/python render.py      # tarjetas + PDF de impresión + PDF web
<tools/venv>/bin/python gates.py       # batería de puertas del constructor (FAILURES: none)
```

Intérpretes (ambos, run.py y render.py): `tools/venv/bin/python` — Python 3.12.3, Pillow 13.0.0, cairosvg 2.9.1, pypdf 6.21.2. El python3 del sistema (también 3.12.3, Pillow 10.2.0) no tiene cairosvg y no se usó; sus métricas PIL difieren, por lo que no debe usarse para re-renderizar.

Entrega: solo repositorio GitHub cuando se inserte (Discord en pausa por instrucción del usuario). Estado del constructor: **builder-complete** (la aprobación final exige la relectura independiente, no realizada aquí).

## D5 rebuild (2026-11-14, D5-only)

SOP §1.1 font fix: the explanation layer's Latin letters move from Noto Sans CJK to Newsreader (SemiBold). No commit, no push — insertion is done by the closer after an independent re-proof. Work log: `hidden_files/d5-redo/scratch-2026-w45-pt/logs/2026-w45-pt-es/`; per-edition report: `production/notes/2026-w45/g-pt/scratch-d5-rebuild-pt/D5-REPORT-2026-w45-pt-es.md`.

**Install**: core landed with `apply_variant.py --patch-core pt --week 2026-w45` (production `core-pt/svglib.py`, `_D5_READER = "latin"` — the core template, inert per D24); this edition installed with `apply_variant.py --svglib patched/2026-w45-pt-es/svglib.py --target pt --reader es --week 2026-w45`, `_D5_READER = "latin"` (--check dry-run clean, RC 0); routing unit test `test_d5_routing.py` FAILURES: 0; fix2 block kept (5 occurrences).

**Baseline** (pre-fix production build): run TOTAL 150, 0 warnings; print/web/issued text layers 33208 = 33208 = 33208 chars, multiset diff 0; baseline web PDF 837975 B; print PDF 2778311 B (`5daec56ce7f66171…`); pre-fix census D5 Latin 493, Cyrillic 0, curly in CJK 0; baseline P8 noted 150/150.

**Defects and fixes** (run1: 5 items, sizes only, no wording changed):

- P1-tv head `A SEMANA EM DOIS DOMINGOS`: content12.py:124 `f2.head` 25→22
- P2-ex head `C　COMPLETE COM OS NÚMEROS`: content12.py:255 `e.head` 25→22
- P1 `EN CIFRAS` box: content12.py:48 `f.box` close, `tsize` 20→19
- P1 `EN ESTA EDICIÓN`: content12.py:89 `p.text` 24→21
- P1 `BREVE`: content12.py:131 `p.text` 24→23

P8: 240→240 lines, footer slack 45.3→45.3 px.

**Gates run2** (17 gates; family gates.py via the runner (see the D5 report §G17); the scripted G17 call is unrunnable (stale paths)) — **ALL-GREEN (17/17 gates)**: run TOTAL 150, 0 warnings; head_check 0 defects; d5 census 0/0/0 (curly_total=2, all in Newsreader); render RC=0; webpdf RC=0 (761154 B < 7 MB); occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN, keydiff=[137, 138] (the registered reader-language keys); freeze baseline 8/8; freeze diff added CJK chars 0 (added Latin strings 247, run splits); spill 0; boxtitle 0 DEFECT (27 titles); edge 0 TOUCH 0 NEAR; creambox PASS 0 defects; text layer print=web 33208 chars, multiset diff 0; textmd carryover 1/1 residual (svg 33208 = md 33208 tokens; the single residual is the known issued-md typo `domingo 15` vs `8`, all 11 editions — needs coordinator ruling); masthead gap (D18) 45.7 px PASS; census_quotes 0 defective; G17 runner verdict: no D5 content defect (all patched-only findings are run-split measurement artifacts).

**New deliverables**: print master `A-Lucerna-VOL2-pt-es.pdf` 2279787 B (`5ab8f976742ff018…`); render-web `A-Lucerna-VOL2-pt-es-web.pdf` 3112573 B (`703d95bb9cbc5637…`); web (issues-type) `2026-w45-pt-es.web.pdf` 761152 B (`74eccc8e2c6257c5…`); text.md differs from the shipped version by exactly 1 line (F-A fix, D36; `0be17947c1b1dd1e…`, 31981 B). Still 150 exercises.

**Exporter note**: pt has no `.text.md` exporter (verified: no textmd/export/derive files in any production pt dir; `transform.py` in pt-de/pt-fr is a content fan-out transform, not a textmd exporter). The issued `issues/2026-w45/2026-w45-pt-es/2026-w45-pt-es.text.md` is carried over BYTE-IDENTICAL; content identity is verified by `verify_textmd.py` carryover jointly with gate 15 (print=web text layer diff 0). Live tool md5 `6dc093c207b0d72b6d387c04e46066f2` (W45-calibrated 2026-11-14; see the family report).

## F-A fix (2026-11-14, D36 — reproof finding F-A)

Reproof (`FAMILY-W45-PT-REPROOF.md` §8) found P7 B1 bridge sentence wrongly said chegar/dormir (chegou, dormiu) take an accent — neither word carries one. Fix: minimal edit at `content7.py:35` (nl: `b.expl`), verb names chegar/dormir → sair/cair, examples chegou/dormiu → saíram/caíram; sentence structure and all other words unchanged. PT original line 34 (`Atenção ao acento: saíram, caíram.`) untouched. The other 5 editions (ja/ko/ru/zh-cn/zh-tw) were not touched — their line only vaguely says "note the accent" and is not a finding.

**Fix gates** (in `fix/`, `GATES-SUMMARY.txt`): run TOTAL 150, 0 warnings; head_check 0 defects; d5 census 0/0/0; render RC=0; webpdf RC=0 (761152 B < 7 MB); occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN, keydiff=[137, 138]; freeze baseline 8/8; freeze diff added CJK chars 0 (added Latin strings 250 (run2 247; +3 is the new F-A words sair/cair/saíram/caíram as added run strings, expected)); spill 0; boxtitle 0 DEFECT (27 titles); edge 0 TOUCH 0 NEAR; creambox PASS 0 defects (P8 240→240，slack 45.3→45.3); text layer print=web 33204 chars, multiset diff 0; print-vs-issued multiset diff 22 = exactly the F-A character delta (9 new vs 13 old, verified by `pdftotext` counters); textmd carryover vs NEW text.md **1/1 residual** (only the known D34 typo `domingo 15` vs `8`); carryover vs ISSUED md 5/5 (D34 + the 4 F-A tokens); masthead gap (D18) 45.7 px PASS; census_quotes 0 defective. G17 runner (en/es/nl): fix runner log byte-identical to the builder patched runner log after path normalisation. Fix verdict carries the expected 15a red (the对照 is the issued edition); acceptance is by diff content, not verdict wording.

**Fix deliverables**: print master `A-Lucerna-VOL2-pt-es.pdf` 2279787 B (`5ab8f976742ff018d86ccd9d41e453c3b37a99616bd0ad7e094bd07be6498421`); render-web `A-Lucerna-VOL2-pt-es-web.pdf` 3112573 B (`703d95bb9cbc5637bbb395ba23c5b8b394cbae192e48576e9dd7799498bda964`); web (issues-type) `2026-w45-pt-es.web.pdf` 761152 B (`74eccc8e2c6257c5d338ca71cdc127a8c84adf2ff0eacada1641243555897d64`); new text.md `2026-w45-pt-es.text.md.new` 31980 B (`ad15135b8dc9ca5838bc181222dee33ecb404f43faaae2d8f9f4816472cab7e2`) — issued text.md with the identical 2-line substitutions at lines 352 (F-A) and 34 (D34) (pt has no text.md exporter; see Exporter note). P7 visually checked on the rendered print PDF (100 dpi): new bridge sentence complete, no overflow or collision; de full page checked. Fixed `content7.py` propagated to BOTH `production/2026-w45/2026-w45-pt-es/content7.py` and `patched/2026-w45-pt-es/content7.py`; `diff -q` confirms production == patched == fix. F-B (D34 typo, 11 issued `.text.md` line 34) fixed by the closer on the delivered files with re-pin (see D5-pin line).
