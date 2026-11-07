# WEEKLY-KIT — Le Lucerna VOL.2 · FR × ES (texto en francés · explicaciones en español)

Semana del 19 al 25 de octubre de 2026 (W43) · 8 páginas · 1950×2700 · 4 columnas · papel marfil #f7f1e2
Build: `hidden_files/weekly-report-fr-es-build/` · Salida: `files/weekly-report-fr-es/`
Estado: construido y corregido por el constructor (ver registro de corrección); **corrección independiente: SUPERADA — una pasada completa con cero problemas (ver §8)**.
No insertado en el repositorio; no publicado en Discord (distribución en pausa).

## 1. IDENTIDAD

- Edición: el semanario de francés VOL.2 («深秋与节日» en la edición núcleo) reorientado a **lectores hispanohablantes**. Todos los artículos, titulares, enunciados y claves en francés son los de la edición núcleo congelada (`files/weekly-report-vol4/`); la capa de explicaciones completa (glosas, notas gramaticales, instrucciones, notas de respuesta) está reescrita nativamente en español.
- Cabecera: **Le Lucerna** (sin cambios).
- Insignia de emparejamiento, P1, rojo ladrillo #a4553a negrita, bajo la banda de cuenta atrás:
  « TEXTOS EN FRANCÉS · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES » (22 pt, medida 1183,5 px — cabe en la medida de 1820 px en una línea).
- Pies en las 8 páginas: « Le Lucerna · SEMANARIO FRANCÉS VOL.2 · TEXTO EN FRANCÉS · EXPLICACIONES EN ESPAÑOL » / « Página N de 8 ».
- Prefijo de glosa: « Nota — » en todo el número (método `expl()` de la biblioteca de composición).
- Palabras de instrucción: Completa / Reescribe / Corrige / Une.
- La cabecera secundaria de P1 reza « SEMANARIO EN FRANCÉS · VOL.2 · OTOÑO Y FIESTAS ».

## 2. MÉTODO

1. Copia de la construcción núcleo finalizada (`hidden_files/weekly-report-vol4-build/`) a `weekly-report-fr-es-build/`. Los directorios núcleo nunca se editaron.
2. **Prueba de base antes de cualquier cambio:** la copia sin modificar, con la salida redirigida a un directorio temporal, reprodujo los 8 SVG publicados del núcleo **byte a byte idénticos** (sha256, 8/8). Total del registro en la base: 145 ejercicios.
3. Reescritura exclusiva de la capa de explicaciones, archivo por archivo, mediante sustituciones exactas con conteo verificado; cabecera y pies desde la biblioteca. Salida → `files/weekly-report-fr-es/`; PDF renombrados `Lucerna-VOL2-ES.pdf` / `Lucerna-VOL2-ES-web.pdf`.
4. El término de capa intermedia prohibido no aparece en ningún sitio: ni en el periódico, ni en este KIT, ni en el código (grep sobre fuentes de construcción + SVG finales = 0 coincidencias, en cualquiera de sus formas).

## 3. TOTALES (medidos en la construcción final)

- Ejercicios: **145** — A2 55 · B1 65 · B2 25; por página 10/16/18/18/17/18/11/37. Idénticos al núcleo, ítem a ítem.
- Tipos (registro): los rótulos de tipo del registro son metadatos internos que no se imprimen; se conservan idénticos al registro núcleo para que la comparación ítem a ítem sea exacta. Todas las instrucciones impresas en el papel están en español.
- Texto visible: 46 606 caracteres (nodos de texto de los SVG concatenados).
- Notas impresas en P8: **67** — exactamente el mismo conjunto que imprimió la edición núcleo (ver §4).
- Registro de construcción: cero FLOW OVERFLOW. Un único HEAD TOO WIDE heredado (P4, titular francés « REGARDER UN MATCH EN FRANÇAIS », ya adjudicado en el registro de corrección del núcleo: se compone en dos líneas, completo y legible; es texto francés congelado y no se toca).

## 4. REGISTRO DE DIFERENCIAS DE CLAVES (contra el núcleo, completo)

Comparación programática de registros (n / página / nivel / tipo **idénticos en los 145**). Diferencias de clave: exactamente 5, todas de lengua del lector:

- **#71, #72, #73** — la respuesta modelo francesa queda intacta; solo el rótulo chino entre paréntesis pasa a « (respuesta modelo) ».
- **#132** — la clave era la traducción china de la frase francesa; ahora es la traducción española: « Leer una encuesta ya es participar en política. » El enunciado impreso pasa a « Traduce al español: « Lire un sondage, c'est déjà faire de la politique. » ».
- **#145** (escritura) — la clave era la línea de orientación en chino; ahora: « Pregunta abierta — los puntos están en el recuadro de escritura y el modelo, en el recuadro MODÈLE de esta página »; nota « se puntúa según los puntos ».

Enunciados reorientados (claves francesas byte a byte idénticas):

- **#133** « Traduce al francés: Es más alto que su hermano. »
- **#134** « Traduce al francés: Los alumnos están de vacaciones desde el sábado. »
- **#135** « Traduce al francés: Esta noche vamos a atrasar los relojes una hora. »

Notas del registro: 122 traducidas del chino al español; 23 ya eran francesas/latinas en el núcleo y quedan intactas; 0 notas con caracteres CJK en el registro final. Las 145 claves y las 67 notas impresas se localizaron todas en el texto renderizado de P8 (búsqueda programática, 0 ausencias). Presentación de claves en P8: paréntesis de medio ancho con un espacio antes, como en las demás ediciones de difusión.

## 5. VERIFICACIÓN DE DIFERENCIA CERO (texto francés)

- Nodos de texto: de los 1 630 nodos del núcleo, **1 283 aparecen byte a byte idénticos** en esta edición; todos los nodos diferentes se clasifican como capa de explicaciones / mobiliario de emparejamiento / partidas del §4.
- P1–P7: **cero nodos franceses del núcleo perdidos o alterados** (todo nodo solo-núcleo no idéntico contiene CJK, es decir, es puramente capa de explicaciones).
- P8: los únicos nodos franceses no idénticos son (a) los enunciados reorientados #132–#135, (b) el sufijo de respuesta modelo de #71–#73, (c) cambios de punto de corte de línea en los párrafos de claves, cuya identidad ítem a ítem está probada por la comparación de registros del §4.
- Cargas de imagen: byte a byte idénticas al núcleo en las 8 páginas (hash por página).
- Auditoría de lengua: caracteres CJK en los 8 SVG finales = **0** (capa de texto y bytes brutos).
- Fechas y días de semana reverificados contra el calendario real de 2026: sáb. 17 oct. (inicio de vacaciones), sáb. 24 oct., dom. 25 oct. (cambio de hora), sáb. 31 oct. (Halloween), dom. 1 nov. (Todos los Santos, festivo), lun. 2 nov. (vuelta a clase). Gráfico de práctica: 28+24+17+11+9+11 = 100 %.
- El avance del VOL.3 impreso por el núcleo (31 oct. Halloween, 1 nov. Todos los Santos, primera semana con horario de invierno) se traslada en español sin cambio de sustancia.

## 6. ADJUDICACIONES DE COMPOSICIÓN (solo redacción de la capa de explicaciones; ni geometría ni francés tocados)

- **P1, desbordamiento de flujo (FLOW OVERFLOW, col. 2, 109 px):** la glosa de portada y los paréntesis del recuadro EN CHIFFRES se comprimieron (glosa: 5→3 líneas; cifras: 3→2 y 4→3 líneas medidas con la métrica real). Reconstrucción posterior: cero desbordamientos. La glosa ya no repite « présidentielle » (cognado transparente para hispanohablantes); el resto de glosas se mantiene.
- **P6, titular demasiado ancho:** « LIRE LE GRAPHIQUE · LEER EL GRÁFICO » (561 px) → « LIRE LE GRAPHIQUE · EL GRÁFICO » (424,5 px ≤ 434).
- **P2, instrucción fuera de página (defecto real, hallado por la auditoría geométrica):** la instrucción del ejercicio de emparejamiento « Une cada palabra con su significado » llegaba a x=1971,9 (fuera del papel). Acortada a « Une palabra y definición » (220,2 px; extremo en x=1867, dentro del margen).
- **P2, recuadro ET VOUS (defecto real, hallado por la auditoría):** la nota española ocupaba 3 líneas frente a las 2 del núcleo y el recuadro cruzaba la línea dorada de la sección siguiente (y=1558). Nota resumida a 2 líneas conservando las tres ideas (¿se cambia la hora en tu país? / ¿a qué hora te levantas el domingo? / escríbenos); el recuadro vuelve a terminar en y=1548,95, la posición exacta del núcleo.
- **Titulares de recuadro medidos con la métrica de producción:** « LES MOTS DES FÊTES / DU SPORT / DES ÉCRANS / DU SCRUTIN · LÉXICO », « DATES À RETENIR · FECHAS », « ZOOM · TUMBAS DE ESCRITORES », « BOÎTE À OUTILS · RECURSOS », « CLINIQUE DES ERREURS · CLÍNICA » (430,2 ≤ 434) — todos dentro de su recuadro/columna.

## 7. AUDITORÍA GEOMÉTRICA DE OCLUSIÓN (addenda SOP + suplemento de líneas finas)

- Script: `hidden_files/weekly-report-fr-es-build/audit_fr_es.py` (con la construcción). Escaneo en orden de pintado de los SVG finales; banda de tinta = base −0,88 em … +0,30 em; anchos de la métrica de producción; cajas de forma expandidas en media anchura de trazo. Controles: (a) cobertura ≥30 %, (b) banda del pie (y>2580), (c) salida del papel, (d) línea posterior cruzando tinta, (e) solape texto–texto, (f) titular fuera de su recuadro.
- **Validación:** el control positivo sintético activa todas las clases (COVER, LINEX, FOOTER, TEXTX) y la página limpia queda en silencio.
- **Resultado sobre los SVG finales: 2 marcas, ambas adjudicadas no-defecto por píxeles:**
  1. P1 TEXTX — cabecera « Le Lucerna » (178 pt, letra gótica) contra la línea de subtítulo: artefacto de métrica (la fuente gótica se mide con métricas Noto). Medición de píxeles en la tarjeta: la tinta del logotipo termina en y≈244 y la del subtítulo empieza en y≈286 — **42 px de aire**. La misma marca existe en la auditoría del núcleo publicado.
  2. P4 TEXTX — « Le Lucerna » de la banda contra su subtítulo (4 %): geometría estándar de `band()`, idéntica en el núcleo (misma marca en su auditoría); sin contacto en la tarjeta.
- Cero coberturas, cero intrusiones en la banda del pie, cero salidas del papel, cero titulares fuera de recuadro en las 8 páginas. (Las dos marcas corregidas de P2 figuran en el §6; tras la corrección, P2 quedó en 0 marcas.)
- Las 8 tarjetas PNG se inspeccionaron página a página: sin texto cubierto, recortado o tachado; insignia, pies, recuadros y columnas de claves en su sitio.

## 8. REGISTRO DE CORRECCIÓN (pasada completa del constructor)

- Lectura completa de las 8 páginas renderizadas + texto extraído: cada glosa, instrucción, nota gramatical y las 145 notas de respuesta leídas contra su enunciado/artículo.
- Español revisado en ortografía, acentos, concordancia y puntuación (¿ ¡, comillas « », medio ancho en las claves de P8).
- Números reverificados: gráfico 100 %; 28 − 24 = 4 puntos; B+3=27 contra A−2=26; 28 + 24 = 52 %.
- Reproducibilidad: la construcción final regenera los 8 SVG entregados byte a byte.
- **Corrección independiente: SUPERADA (2026-10-21)** — revisor nuevo, una pasada completa con **cero problemas**; sin correcciones, sin re-renderizado. Verificación realizada:
  - **Registros regenerados desde el código de ambas construcciones y comparados ítem a ítem:** n/página/nivel/tipo idénticos en los 145; diferencias de clave exactamente las 5 del §4 (#71–#73 solo el rótulo « (respuesta modelo) »; #132 traducción española fiel a « Lire un sondage, c'est déjà faire de la politique. »; #145 orientación en español); notas: 122 modificadas, 23 idénticas (francés/latín del núcleo), 0 CJK en claves/notas del registro final. (Matiz registrado: la nota de #119 solo cambia en espaciado de paréntesis «（à+les）» → « (à + les) », dentro de las 122.)
  - **Diferencia cero de texto:** multiconjuntos de nodos por página contra el núcleo — en P1–P7 todo nodo solo-núcleo contiene CJK (cero francés perdido o alterado); en P8 los únicos nodos franceses no idénticos son los enunciados reorientados #132–#135, el sufijo de #71 y cambios de punto de corte en los párrafos de claves (identidad probada por el registro). Enunciados #133/#134/#135 impresos tal como documenta el §4, con claves francesas byte a byte idénticas.
  - **Claves rederivadas independientemente de los enunciados/artículos/gráfico: las 145 correctas** (incl. aritmética del gráfico 28+24+17+11+9+11 = 100 %; 28−24 = 4; B+3 = 27 contra A−2 = 26; A+B = 52 %). Totales: 145 — A2 55 · B1 65 · B2 25; por página 10/16/18/18/17/18/11/37; numeración 1–145 continua.
  - **Notas impresas en P8: 67** — el conjunto PRINT_NOTES coincide exactamente con el que produce la regla del núcleo aplicada a su propio registro; las 145 claves y las 67 notas localizadas en el texto renderizado de P8 (0 ausencias).
  - **Frases de la semana (P7):** conjunto, textos y etiquetas de página idénticos al núcleo; conteo de ocurrencias en el texto completo idéntico en ambas ediciones (2/2/1/1/1/2/1). **Avance VOL.3:** francés byte a byte idéntico al núcleo; sustancia sin cambios (31 oct. Halloween, 1 nov. Todos los Santos, primera semana de horario de invierno). Días de semana verificados contra el calendario real de 2026 (sáb. 17 y 24 y 31 oct.; dom. 25 oct. y 1 nov.; lun. 2 nov.; sáb. 24 oct. en el diálogo).
  - **Auditoría geométrica independiente** (implementación propia; control positivo sintético validado — COVER/LINEX/FOOTER/EDGE/BOXTITLE/TEXTX disparan y la página limpia queda en silencio): **COVER 0 · LINEX 0 · FOOTER 0 · EDGE 0 · BOXTITLE 0** en las 8 páginas. Únicas marcas: 2 TEXTX heredadas del núcleo, adjudicadas por píxeles como no-defectos — P1: la tinta del logotipo termina en y=265 y la de la línea de subtítulo empieza en y=285 (20 px de aire); P4 banda: tinta del título en filas 89–115 y del subtítulo en 128–141 (12 px de aire).
  - **Puntos de P2 corregidos por el constructor, reverificados:** la instrucción de emparejamiento « Une palabra y definición » termina en tinta en x=1865 (dentro del margen, borde de contenido 1885); el recuadro ET VOUS cierra en y=1548,95 (posición exacta del núcleo) y la línea dorada va en y=1558 — bandas de tinta separadas, sin contacto.
  - **Aviso HEAD TOO WIDE de P4:** aparece idéntico en el registro de construcción del núcleo; el titular francés congelado se compone completo y legible en la tarjeta.
  - **Imágenes:** cargas byte a byte idénticas al núcleo (P1 Hiroshige/LACMA, P2 Atget, P3 plancha de Blanco); créditos corresponden a las imágenes colocadas. **PDF web verificado por el revisor: 5 956 261 bytes (< 10 MB), sha256 9a0adcb652dd47d062c770c9a4250ed3aa4d65a760b3dade2ce89cfbfdfc9e7e.**
  - **CJK = 0** en los 8 SVG finales (texto y bytes brutos); **término de capa intermedia prohibido = 0** en papel, este KIT y código. Insignia de emparejamiento en P1 y pies con « Página N de 8 » en las 8 páginas; cabecera « Le Lucerna ». Las 8 tarjetas inspeccionadas visualmente: sin texto cubierto, recortado ni tachado.
  - **Conclusión: la edición queda final** y puede insertarse en el repositorio.

## 9. ENTREGABLES (este directorio)

- `svg/` — 8 SVG de página (p1-une … p8-exercices) · `cards/` — 8 PNG (1950×2700)
- `Lucerna-VOL2-ES.pdf` — PDF de impresión, 9 778 738 bytes · sha256 91f84f6427fc6d7fa79bdd6def9851f61de0f0b3bf9417bd0f539c787f2469f0
- `Lucerna-VOL2-ES-web.pdf` — PDF web (páginas JPEG q85), **5 956 261 bytes (< 10 MB)** · sha256 9a0adcb652dd47d062c770c9a4250ed3aa4d65a760b3dade2ce89cfbfdfc9e7e

## 10. REPRODUCCIÓN

```bash
cd hidden_files/weekly-report-fr-es-build
/tmp/wp-venv/bin/python -c "import content12, content34, content56, content7, content8"   # -> files/weekly-report-fr-es/svg/
/tmp/wp-venv/bin/python audit_fr_es.py --selftest        # el control positivo debe pasar
/tmp/wp-venv/bin/python audit_fr_es.py ../../files/weekly-report-fr-es/svg
# tarjetas + PDF: cairosvg por página (PNG 1950 + PDF), pypdf para el de impresión,
# páginas JPEG q85 para el web — mismo procedimiento que la edición núcleo.
```
Venv `/tmp/wp-venv` (cairosvg, pillow, pypdf). Nunca usar /opt/meta-chromium (se cuelga en esta VM).
