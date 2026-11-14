# A Lucerna VOL.1 — Edición PT × ES (W43)

- **Emparejamiento**: texto en portugués (brasileño) + explicaciones en español — la edición para los lectores hispanohablantes.
- **Semana**: 2026-W43 · Semana de 19 a 25 de outubro de 2026 · VOL.1
- **Fuente**: edición núcleo PT × zh-CN (`files/weekly-report-pt-vol1/`, archivos entregados tras las correcciones geométricas P7/P8 de la auditoría del programa). El texto portugués está **congelado**: solo se reescribió la capa de explicación, en español nativo y completo (glosas, notas de gramática, instrucciones y la totalidad de las notas de respuesta de la página 8).
- **Directorio de build**: `hidden_files/weekly-report-pt-es-build/` (copia del build del núcleo). La copia sin modificar reprodujo primero los 8 SVG entregados del núcleo **byte a byte** (verificado antes de cualquier cambio).

## Specs

- 8 páginas, 1950×2700, 4 columnas, marfil cálido #f7f1e2, acentos verde oliva oscuro / rojo ladrillo #a4553a.
- **150 ejercicios** — A2 44 · B1 75 · B2 31; por página 10/18/18/18/18/18/12/38. Registro (n.º, página, nivel, tipo) **idéntico** al núcleo, verificado por volcado de ambos registros.
- Masthead: **A Lucerna**. Línea de edición de la página 1: «SEMANARIO EN PORTUGUÉS · VOL.1 · O SEGUNDO TURNO · O DEBATE FINAL · O ENEM VEM AÍ» (36 pt, tinta medida 1742 px ≤ 1820).
- **Distintivo página 1** (rojo ladrillo #a4553a, en negrita, sustituye la línea de firma del núcleo): «TEXTOS EN PORTUGUÉS · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES» (1053 px ≤ 1820).
- Franja superior página 1: «TODA SEMANA EM PORTUGUÊS · CADA SEMANA · EL PORTUGUÉS QUE LEE BRASIL»; banda negra a la derecha: «DOMINGO, DÍA DE DECISIÓN» / «La segunda vuelta presidencial · ver la página 6».
- **Pies de página (8 páginas)**: «A Lucerna · SEMANARIO PORTUGUÉS VOL.1 · TEXTO EN PORTUGUÉS · EXPLICACIONES EN ESPAÑOL» y «Página N de 8».
- Prefijo de las cajas de glosas: «Nota — ». Tipografía de respuestas: espacio antes de cada paréntesis de nota, paréntesis de media anchura únicamente; ninguna nota contiene paréntesis internos.

## Registro de diferencias de claves (ES vs núcleo — solo difieren los ítems documentados)

El cuerpo de las respuestas es idéntico al núcleo en 147 de 150 ítems. Diferencias, todas en la capa del lector:

| # | Tipo | Núcleo (zh-CN) | Esta edición (ES) |
|---|------|----------------|--------------------|
| 137 | Traducir (PT→lengua del lector) | clave = traducción china de la frase PT | clave = «El domingo, Brasil vuelve a las urnas.» — nota «(titular de la página 1)» |
| 138 | Traducir (PT→lengua del lector) | clave = traducción china de la frase PT | clave = «Comprueba tu lugar de votación antes de salir de casa.» — nota «(Confira = comprueba)» |
| 139 | Traducir — **instrucción reorientada** | PT→chino | instrucción en español: «Las búsquedas de «guitarra» crecieron un 53 %.» → respuesta en portugués «As buscas por guitarra cresceram 53%.» (cuerpo PT idéntico al núcleo) |
| 140 | Traducir — **instrucción reorientada** | PT→chino | instrucción en español: «Cuando llegues, comprueba tu sección.» → respuesta en portugués «Quando você chegar, confira a seção.» (cuerpo PT idéntico al núcleo) |
| 150 | Escribir — línea de aparato | clave de aparato en chino en el núcleo | clave de aparato «(pregunta abierta)»; la línea impresa usa la nota «✓ (el texto modelo está en la sección H: 92 palabras)» |

Ninguna otra clave difiere (verificado por volcado programático de los dos registros: n.º/página/nivel/tipo idénticos en los 150; claves byte a byte salvo los 3 ítems anteriores). Los tipos de ejercicio en el código （完成句子/单选/词汇配对/造句/判断对错/完形单选/翻译/写作） son metadatos de registro, nunca impresos — idénticos en todas las ediciones hermanas.

## Acortamientos de ajuste (solo capa española — texto portugués y geometría del núcleo intactos)

Detectados durante el build por las auditorías geométricas y de flujo; corregidos acortando el aparato español:

1. **P6, flujo de ejercicios**: la capa española empujaba el ítem n.º 100 por debajo de la regla del pie (chip en y=2602). Acortadas 3 instrucciones: A «Mira los gráficos y elige la respuesta.», C «Completa con la forma verbal correcta.», D «Usa: segundo turno · maioria absoluta · votos válidos · intenção de voto» → el flujo P6 termina en y=2519, idéntico al núcleo.
2. **P8, flujo de claves**: ~17 notas acortadas (claves intactas) para que el flujo de respuestas termine en y=2444 (núcleo: 2397), con margen sobre la banda del pie (2580).
3. **P7, columna 3 → citas ocultas (defecto real, atrapado por la auditoría)**: las notas españolas alargaban la pila de la columna 3 (fin en y=1838,5 frente a 1722 en el núcleo), lo que empujaba la 4.ª fila de citas (n.º 4 y n.º 8) bajo la banda oscura «A PRÓXIMA SEMANA» — cubiertas al 100 % en la primera pasada de auditoría, invisibles en el render (verificado visualmente en la tarjeta). Acortadas: nota de la carta («Carta de ejemplo. ¡En el VOL.2, cartas reales y los mejores textos!»), glosa de «urna» («urna: la máquina de votar; también, el acto entero: …»), nota del error n.º 2 («ojo: en portugués, em + a = na.») y nota del error n.º 1 («assistir pide a: assistir ao debate.») → la pila vuelve a y=1721,5 (≈ núcleo 1722) y las 8 citas quedan visibles sobre la banda.
4. **P1, título de caja «EM POUCAS PALAVRAS · EN BREVE»**: cruzaba el borde derecho de su caja por 3,1 px (auditoría de títulos). Título: «EM POUCAS PALAVRAS · BREVE» — 0 cruces tras el arreglo.

Espaciado tipográfico: espacio añadido antes de las glosas entre paréntesis de las cajas P1 (×3) y P5 (×5), donde el núcleo no llevaba espacio antes del paréntesis de anchura completa y el español lo exige.

## Auditorías (puertas SOP)

- **Auditoría geométrica de oclusión** (orden de pintura, métricas de fuente real PIL, cajas de línea **expandidas en media anchura de trazo**; script validado primero sobre un control sintético positivo que disparó las 4 clases COVER/LINEX/FOOTER/EDGE): **0 flags** en las 8 páginas en la pasada final. Auditoría de títulos de caja contra sus bordes: **0 cruces**. Auditoría texto-texto: 1 artefacto de modelo en P1 (banda de tinta conservadora del wordmark de 168 pt contra la línea de edición) — adjudicado no-defecto por inspección visual de la tarjeta (aire claro entre ambos).
- **Congelación del texto portugués**: diff multiconjunto de nodos de texto página a página contra el núcleo — cada diferencia clasificada como capa de explicación española, mobiliario de emparejamiento o ítem documentado (§ registro de claves); las cargas de imagen son byte a byte idénticas en las 8 páginas; **CJK = 0** en los 8 SVG.
- **Citas P7**: verificación programática — las 8 citas son extractos contiguos textuales de sus páginas etiquetadas (1, 1, 2, 3, 4, 5, 6, 2).
- **Hechos y calendario 2026** (verificado con `date`): 19 oct = lunes, 20 = martes, 21 = miércoles, 23 = viernes, 24 = sábado, 25 = domingo (segunda vuelta), 31 oct = sábado, 1 nov = domingo (semifinales de la Copa do Brasil, en **noviembre**), 2 nov = lunes (Finados), 7 nov = sábado, 8 y 15 nov = domingos (Enem). Ningún porcentaje de encuesta: solo interés de búsqueda de Google, rotulado como tal en la página.
- **Aritmética re-verificada**: 982+514+431+312 = 2.239; 350+350 = 700; 900−250 = 650; agregado Boca 3×2.

## Corrección del constructor (prueba completa propia)

Las 8 tarjetas renderizadas leídas página a página: ortografía y acentuación del español, concordancia, cada nota contra su enunciado, mobiliario y distintivo de emparejamiento en las 8 páginas. Sin problemas pendientes tras los arreglos de § Acortamientos.

## Relectura independiente (puerta SOP §8) — COMPLETADA: PASS (cero problemas tras 1 corrección)

Revisor independiente (no construyó esta edición), 2026-10-21. Método: registros de ambas ediciones regenerados desde los builds en copias aisladas y comparados programáticamente; diff multiconjunto de nodos de texto página a página contra el núcleo; re-derivación propia de las 150 claves desde el texto portugués impreso; auditoría geométrica propia (orden de pintura, métricas PIL de la fuente real, cajas de línea expandidas en media anchura de trazo, control sintético positivo con las 5 clases COVER/LINEX/FOOTER/EDGE/TITLE disparadas); las 8 tarjetas vistas página a página.

- **Congelación**: los 150 ítems coinciden en n.º/página/nivel/tipo; las claves difieren del núcleo en **exactamente 3** ítems (#137/#138 claves de traducción al español — fieles a los enunciados PT impresos en la pág. 8 — y #150 aparato). Todo el diff de texto se clasifica como capa española / mobiliario de emparejamiento / ítems documentados / artefactos de corte de línea. CJK y demás escrituras ajenas en los SVG finales: **0** (texto y bytes crudos). Cargas de imagen byte a byte idénticas al núcleo en las 8 páginas; créditos presentes junto a cada imagen colocada (P1 TSE; P3 Recife CC0 + Gottlieb DP; P5 Gary Todd CC0).
- **Claves re-derivadas**: 150/150 correctas contra artículos, gráficos y aritmética (982+514+431+312=2.239; 350+350=700; 900−250=650; agregado 3×2 Boca; modelo de redacción = 92 palabras con la convención de conteo del núcleo).
- **P7**: las 8 citas ocurren exactamente 2× en la edición (artículo + caja), extractos contiguos literales, etiquetas de página (1, 1, 2, 3, 4, 5, 6, 2) correctas; en la tarjeta, la 4.ª fila de citas queda totalmente visible sobre la banda «A PRÓXIMA SEMANA» (tinta hasta y=2382; la banda empieza en y=2404).
- **Calendario 2026** verificado con `date`: debate vie 23 oct; segunda vuelta dom 25 oct; Prova mié 21 oct; semifinales de Copa do Brasil dom 1 nov (**noviembre**); Finados lun 2 nov; Enem dom 8 y 15 nov. Ningún porcentaje de encuesta: todas las cifras porcentuales son interés de búsqueda de Google, rotulado como tal en la página (P1, P6, notas #88/#100/#127).
- **Geometría (auditoría propia)**: COVER 0 · LINEX 0 · EDGE 0 en las 8 páginas; invasores de la banda del pie (y>2580, excluidas las dos líneas del propio pie, con baselines idénticas al núcleo: y=2624) 0; cruces título-de-caja/borde 0; ítem #100 de P6 termina en y≈2499, libre de la regla del pie.
- **DEFECTO ENCONTRADO Y CORREGIDO (solo capa española)**: la nota de la clave n.º 114 decía «4.352 colegios nuevos» — las 4.352 secciones **cambiaron de dirección**, no son colegios nuevos (cf. notas #3/#9/#21, correctas). Corregido en `content8.py` → «4.352 colegios cambiaron de dirección», re-renderizado completo y **segunda pasada entera desde cero: cero problemas** (diff total contra la versión previa = solo esa línea; P1–P7 byte a byte idénticas; registros de nuevo idénticos salvo los 3 ítems documentados). Los pins de PDF de abajo son los de la versión corregida.
- Término intermedio prohibido (forma china e inglesa): 0 en papel, KIT y código.

## Entregables

- `svg/` ×8, `cards/` ×8 (1950×2700)
- PDF de impresión: `Lucerna-VOL1-ES.pdf` — 6.451.744 bytes, sha256 `d8ebd539ba05186f36f3185743825b248f0479df32ef48ca62b5a31d8b3ea808` (versión corregida, véase la relectura independiente)
- PDF web: `Lucerna-VOL1-ES-web.pdf` — 3.695.581 bytes (< 10 MB), sha256 `e011eba1aa2cf7a4cfbd9d6194c0b413c8b27241090d337885a922fbc8b5bbfa` (versión corregida, véase la relectura independiente)
- D5 rebuild (2026-11-13–14, see D5 rebuild section at the end of this KIT): print master `A-Lucerna-VOL1-pt-es.pdf` **5355970 B** · sha256 `3568dfd15445409963501c7e17c6c931ded6fb5cc5c741d6316c9860cd8dba49`; render-web `A-Lucerna-VOL1-pt-es-web.pdf` **3313052 B** · sha256 `ae29c303f92c3298f4defbcd001fc9241f4648964b39b63330e941300d649854`; web (issues-type) `2026-w43-pt-es.web.pdf` **643328 B** · sha256 `aa6596cc9a2bd8d26a44b92676a182b202dfbdf1ea9e10865353145922ed8532` (< 7 MB); text.md byte-identical to the shipped version (sha256 `cd6a35c12e75ac2fe59c4872795e9dcbd8008a76e387c713aa2a3c8079fbad47`). Pre-D5 KIT pins above (print 6,451,744 B (sha256 `d8ebd539…`); render-web 3,695,581 B (sha256 `e011eba1…`)) are D1-era values, already expired before this rebuild (toolchain drift: Bold/Italic subset split in tools/webpdf.py commit 40963281).

## Reproducción

```
cd hidden_files/weekly-report-pt-es-build
/tmp/wp-venv/bin/python run.py      # genera los SVG en files/weekly-report-pt-es/svg/
/tmp/wp-venv/bin/python render.py  # tarjetas + PDF de impresión + PDF web
/tmp/wp-venv/bin/python audit_pt_fr.py ../../files/weekly-report-pt-es/svg   # auditoría geométrica (nombre heredado del script hermano)
```

Entrega: solo repositorio GitHub cuando se inserte (Discord en pausa por instrucción del usuario).

## D5 rebuild (2026-11-13–14, D5-only)

SOP §1.1 font fix: the explanation layer's Latin letters move from Noto Sans CJK to Newsreader (SemiBold). No commit, no push — insertion is done by the closer after an independent re-proof. Work log: `hidden_files/d5-redo/scratch-2026-w43-pt/logs/2026-w43-pt-es/`; per-edition report: `production/notes/2026-w43/g-pt/scratch-d5-rebuild-pt/D5-REPORT-2026-w43-pt-es.md`.

**Install**: core landed with `apply_variant.py --patch-core pt --week 2026-w43` (production `core-pt/svglib.py`, `_D5_READER = "latin"` — the core template); this edition installed with `apply_variant.py --svglib patched/2026-w43-pt-es/svglib.py --target pt --reader es --week 2026-w43`, `_D5_READER = "latin"` (--check dry-run clean, RC 0); routing unit test `test_d5_routing.py` FAILURES: 0; fix2 block kept (5 occurrences).

**Baseline** (pre-fix production build): run TOTAL 150, 0 warnings; print/web/issued text layers 43,511 = 43,511 = 43,511 chars, multiset diff 0; baseline web PDF 719,186 B; print PDF 5,855,981 B (`831306a0…`); pre-fix census D5 Latin 491, Cyrillic 0, curly in CJK 0; baseline P8 noted 150/150.

**Defects and fixes** (run1: 5 items, sizes only, no wording changed):

- P2-ex head `C　COMPLETE COM OS NÚMEROS`: content12.py:256 `e.head` 25→22
- P3-main head `DOIS INSTRUMENTOS, UM PAÍS`: content34.py:21 `f.head` 25→24
- P1 `CIFRAS` box: content12.py:47 `f.box` close, `tsize` 23→21
- P1 `EN ESTA EDICIÓN`: content12.py:90 `p.text` 24→21
- P1 `BREVE`: content12.py:132 `p.text` 24→22

P8: 204→204 lines, footer slack 57.4→57.4 px.

**Gates run2** (16 gates; no family gates.py for pt) — **ALL-GREEN (16/16 gates)**: run TOTAL 150, 0 warnings; head_check 0 defects; d5 census 0/0/0 (curly_total=0); render RC=0; webpdf RC=0 (643,328 B < 7 MB); occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN, keydiff=[137, 138] (the registered reader-language keys); freeze baseline 8/8; freeze diff added CJK chars 0 (added Latin strings 253, run splits); spill 0; boxtitle 0 DEFECT (26 titles); edge 0 TOUCH 0 NEAR; creambox PASS 0 defects; text layer print=web 99,285 chars, multiset diff 0; textmd carryover PASS 0/0 (svg 5254 = md 5254 tokens); masthead gap (D18) 39.0 px PASS; census_quotes 0 defective.

**New deliverables**: print master `A-Lucerna-VOL1-pt-es.pdf` 5,355,970 B (`3568dfd1…`); render-web `A-Lucerna-VOL1-pt-es-web.pdf` 3,313,052 B (`ae29c303…`); web (issues-type) `2026-w43-pt-es.web.pdf` 643,328 B (`aa6596cc…`); text.md byte-identical to the shipped version (`cd6a35c1…`). Still 150 exercises.

**Exporter note**: pt has no `.text.md` exporter (verified: the `ru_textmd.py` trial differed by 757 lines). The issued `issues/2026-w43/2026-w43-pt-es/2026-w43-pt-es.text.md` is carried over BYTE-IDENTICAL; content identity is verified by `verify_textmd.py` carryover jointly with gate 15 (print=web text layer diff 0).
