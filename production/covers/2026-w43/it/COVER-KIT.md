# COVER-KIT — La Lucerna COVER, settimana W43 (19–25 ottobre 2026), lettori italiani

## Spec (SOP附则五)
- Weekly cover, non un'edizione regolare: 8 pagine, 1950×2700, sistema visivo
  del settimanale (avorio caldo #f7f1e2, verde oliva scuro, serif).
- Lingua del lettore: ITALIANO. Tutta la scrittura originale della copertina
  (titolo, introduzione, spiegazioni, etichette, guida alla lettura) è in italiano.
- Titoli ed estratti restano nelle loro lingue ORIGINALI, verbatim.
- Testata: "La Lucerna" (articolo italiano). La copertina NON ha un numero VOL
  proprio ed è marcata COVER (badge visibile in P1 e P8, richiamo nel piè di pagina).
  I VOL che compaiono in P8 sono quelli dei 12 settimanali principali elencati,
  come richiesto dallo spec per l'ultima pagina.
- Nessun subagent, nessun intervento su git.

## Le 12 fonti (ordine fisso, da cover-backfill/headlines-w43.json)
Materiale caricato verbatim dal JSON condiviso; titoli ed estratti NON sono stati
ri-estratti né modificati. Nessuna discrepanza JSON↔core riscontrata nel materiale usato
(il build carica il JSON programmaticamente; il testo del PDF è stato verificato
contro lo stesso JSON, vedi sotto).

| # | Lingua | Testata del core | VOL del core | Directory core |
|---|--------|------------------|--------------|----------------|
| 1 | en | The Lucerna | 1 | weekly-report-en-vol1 |
| 2 | de | Die Lucerna | 1 | weekly-report-de-vol1 |
| 3 | fr | Le Lucerna | 2 | weekly-report-vol4 |
| 4 | es | La Lucerna | 1 | weekly-report-es-vol1 |
| 5 | it | La Lucerna | 1 | weekly-report-it-vol1 |
| 6 | pt | A Lucerna | 1 | weekly-report-pt-vol1 |
| 7 | nl | De Lucerna | 1 | weekly-report-nl-vol1 |
| 8 | ru | Lucerna | 1 | weekly-report-ru-vol1 |
| 9 | ja | Lucerna | 1 | weekly-report-ja-vol1 |
| 10 | ko | Lucerna | 1 | weekly-report-ko-vol1 |
| 11 | zh-cn | Lucerna | 1 | weekly-report-zhcn-vol1 |
| 12 | zh-tw | Lucerna | 1 | weekly-report-zhtw-vol1 |

Etichette di lingua in italiano (tables.json, colonna IT): INGLESE, TEDESCO,
FRANCESE, SPAGNOLO, ITALIANO, PORTOGHESE, OLANDESE, RUSSO, GIAPPONESE, COREANO,
CINESE SEMPLIFICATO, CINESE TRADIZIONALE.

## Layout (8 pagine)
- P1: testata "La Lucerna" + badge COVER + "19–25 ottobre 2026" + titolo
  "Dodici lingue, una settimana" + introduzione generica (nessun fatto nuovo) +
  12 teaser in ordine fisso (etichetta + titolo verbatim, due colonne, lettura per righe)
  + riquadro "Come leggere questa copertina" (inquadramento generico, nessun fatto nuovo).
- P2: EN, DE. P3: FR, ES. P4: IT, PT. P5: NL, RU. P6: JA, KO. P7: zh-cn, zh-tw.
  Per ogni voce: etichetta di lingua, titolo verbatim, estratto verbatim, riquadro
  "Spiegazione" di 1–2 frasi in italiano. Regola rispettata: ogni affermazione delle
  spiegazioni è rintracciabile nel titolo + estratto di quella voce; nessun fatto
  esterno (es. la spiegazione EN parla solo del voto anticipato; la spiegazione DE
  riprende "undici Paesi" dal titolo; la spiegazione KO non collega il tifone Champi
  a nessun altro evento della settimana).
- P8: i 12 settimanali principali in ordine fisso: testata + VOL + titolo verbatim.

## Build
- Build dir: `hidden_files/cover-w43-it-build/` — `build.py` + `svglib.py`
  (copia del modulo del core IT; NESSUN modulo di contenuto del core importato) + `svg/`.
- SVG generati: p1-copertina, p2–p7-prime, p8-settimanali (1950×2700).
- PDF finale costruito SOLO con tools/webpdf.py (testo vettoriale, non JPEG):
  `La-Lucerna-COVER-W43.pdf`.

## Verifiche
- Revisione visiva (render PNG via CairoSVG, tutte e 8 le pagine): nessun overflow,
  nessun testo tagliato, nessun glifo mancante (latino, cirillico, giapponese,
  coreano, cinese semplificato e tradizionale rendono tutti correttamente),
  nessuna sovrapposizione dopo le correzioni sotto.
- Occlusion audit (`tools/occlusion_audit.py`, selftest OK):
  prima esecuzione (layout v1): 8 flag TEXTX (etichette sovrapposte ai titoli).
  Dopo le correzioni: **0 flag, exit 0**.
- PDF: 8 pagine, **352.550 byte** (< 7 MB), `pdftotext` = **8.584 byte** (non vuoto).
- Tutti e 12 i titoli si estraggono dal PDF alla lettera (confronto normalizzato
  spazi/punteggiatura: 12/12). Tutti e 12 gli estratti si estraggono alla lettera:
  8/8 per le lingue latine/cirilliche con confronto a spazi normalizzati; per le
  4 voci CJK (ja, ko, zh-cn, zh-tw) il confronto a spazi normalizzati mostra
  differenze SOLO dovute agli a-capo inseriti da pdftotext a metà frase (che in
  cinese/giapponese/coreano non hanno spazi tra parole) — il confronto senza
  spazi conferma 4/4 estratti verbatim.
- "VOL." compare nel testo del PDF SOLO nelle 12 righe di P8 (i VOL dei core),
  mai come numero proprio della copertina; "COVER" presente.

## Problemi trovati e corretti
1. Badge COVER sovrapposto alla testata (P1, P8): la testata da 150 px saliva fin
   sotto il badge. Fix: distanza testata–badge portata a 215 px (circa 47 px di
   luce tra badge e inchiostro della testata).
2. Etichette di lingua sovrapposte ai titoli (P2–P7): gap di 52 px insufficiente
   per titoli da 64 px. Fix: gap portato a 84 px; confermato visivamente e
   dall'audit (da 8 flag TEXTX a 0).
3. P1 con troppo vuoto in basso: aggiunti teaser a 44 px e riquadro guida alla
   lettura; P2–P7: avvio contenuti spostato a y=300 e gap tra voci portato a 110 px.
4. Primo tentativo di render PNG fallito: `cairosvg` non è nel Python di sistema —
   usato `tools/venv/bin/python` come da SOP/tools (nessun pacchetto installato).
