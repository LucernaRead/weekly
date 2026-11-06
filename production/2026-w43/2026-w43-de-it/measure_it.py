# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import text_w, wrap

# (label, string, kind, bold, size, budget_px)
CHECKS = [
    ("P1 strap 46 serif bold centered (<=1820)", "SETTIMANALE TEDESCO · VOL.1 · OROLOGI · VACANZE · BRINA", "serif", True, 46, 1820),
    ("P1 badge 20 sans bold centered (<=1820)", "TESTI IN TEDESCO · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI", "sans", True, 20, 1820),
    ("P1 topstrip mid 21 sans (centered; half-budget 480 => <=960)", "WÖCHENTLICH AUF DEUTSCH · OGNI SETTIMANA · IL TEDESCO CHE LEGGONO I TEDESCHI", "sans", False, 21, 960),
    ("P1 band right1 24 bold (German line ends?)", "Domenica si riporta l'orologio indietro", "sans", True, 24, 700),
    ("P1 band right2 21 (<=700)", "La notte di 25 ore · pagina 2", "sans", False, 21, 700),
    ("P1 band German main 36 bold (start of right texts must be > end)", "SONNTAG WIRD DIE UHR ZURÜCKGESTELLT — EINE STUNDE LÄNGER SCHLAFEN!", "sans", True, 36, 9999),
    ("footer left 20 sans (<=1350)", "Die Lucerna · SETTIMANALE TEDESCO VOL.1 · TESTI IN TEDESCO · SPIEGAZIONI IN ITALIANO", "sans", False, 20, 1350),
    ("footer right 20 sans", "Pagina 8 di 8", "sans", False, 20, 200),
    ("Fragen subtitle 19 sans (<=412)", "Le domande delle guide tedesche", "sans", False, 19, 412),
    ("Fragen closing 19 sans (<=412)", "Le guide di tutto il paese rispondono.", "sans", False, 19, 412),
    ("band title P8 36 bold (<=1000)", "ÜBUNGEN & ANTWORTEN · Esercizi e risposte", "sans", True, 36, 1000),
    ("band sub P8 19 sans (<=950)", "SCHLUSSTEST · Prova finale · Tutte le risposte in fondo a questa pagina", "sans", False, 19, 950),
    ("band title P6 36 bold", "VERTIEFUNG · Approfondimento", "sans", True, 36, 1000),
    ("band sub P7 19 sans (<=1050)", "A2 → B2 · Sätze der Woche & Fehlerklinik · Frasi della settimana e clinica degli errori", "sans", False, 19, 1050),
    ("band sub P2 19 sans (<=1050)", "LEVEL A2 · Die Uhr, der Frost & die Reifen · Orologi, brina e pneumatici", "sans", False, 19, 1050),
    ("band sub P4 19 sans (<=1050)", "LEVEL B1 · Champions League & Bundesliga · Champions League e Bundesliga", "sans", False, 19, 1050),
    ("ex header right 20 sans (<=1050)", "Risposte a pagina 8 · I livelli si mescolano: cerca ogni risposta per numero", "sans", False, 20, 1050),
    ("ex header left 28 bold (<=700)", "ÜBUNGEN · Esercizi della pagina 2", "sans", True, 28, 700),
    ("quiz header right 20 sans (<=1100)", "Leggi la prima pagina e scegli la risposta giusta · Risposte a pagina 8", "sans", False, 20, 1100),
    ("P2 clock hdr right 20 sans (<=800)", "Die Zeiten der Woche · Tutte le ore della settimana", "sans", False, 20, 800),
    ("P2 clock note1 21 sans (<=495)", "= 2.30 Uhr! (non le 3.30!)", "sans", False, 21, 495),
    ("P2 clock note2 21 sans (<=495)", "= 7.45 Uhr (le otto meno un quarto)", "sans", False, 21, 495),
    ("P2 clock note3 21 sans (<=495)", "= 8.15 Uhr (le otto e un quarto)", "sans", False, 21, 495),
    ("P6 chart title 26 bold (<=1820)", "WAS MACHEN DIE DEUTSCHEN MIT DER EXTRA STUNDE? · Cosa fanno i tedeschi con l'ora in più?", "sans", True, 26, 1820),
    ("P6 UEBUNGSDATEN 19.5 sans single line (<=1820)", "ÜBUNGSDATEN · DATI DI PRATICA — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage. (Dati di pratica della redazione, non un sondaggio vero.)", "sans", False, 19.5, 1820),
    ("P6 Samstag title 24 bold (<=1332)", "DER SAMSTAG-PLAN DER REDAKTION · Il piano del sabato", "sans", True, 24, 1332),
    ("P6 ProContra title 24 bold (<=1332)", "PRO & CONTRA · Pro e contro — die Argumente der Debatte", "sans", True, 24, 1332),
    ("P7 phrases hdr right 20 sans (<=950)", "Citazioni letterali dagli articoli di questo numero · la fonte tra parentesi", "sans", False, 20, 950),
    ("P7 clinic hdr right 20 sans (<=950)", "I quattro errori più frequenti · Correggili prima tu, poi guarda la risposta", "sans", False, 20, 950),
    ("P7 toolbox title 23 bold (<=412)", "DER WERKZEUGKASTEN · Gli strumenti", "sans", True, 23, 412),
    ("P7 readers title 23 bold (<=412)", "LESERBRIEFE · Le vostre lettere", "sans", True, 23, 412),
    ("P8 keys head 26 bold (<=1820)", "ANTWORTEN · TUTTE LE RISPOSTE CON NOTE (PAGINE 1–8)", "sans", True, 26, 1820),
    ("P8 head G 24 bold (<=434)", "G · DIALOG · Completa il dialogo", "sans", True, 24, 434),
    ("P8 head F 24 bold (<=434)", "F · WÖRTER PAAREN · Abbina le parole", "sans", True, 24, 434),
    ("P8 head D 24 bold (<=434)", "D · SÄTZE BAUEN · Costruisci frasi", "sans", True, 24, 434),
    ("P1 zahlen title 23 bold (<=398)", "DIE WOCHE IN ZAHLEN · In cifre", "sans", True, 23, 398),
    ("P2 Merksatz title 23 bold (<=398)", "DER MERKSATZ · Il trucco", "sans", True, 23, 398),
    ("P4 Spieltag title 26 bold (<=1820)", "DER 7. SPIELTAG · La 7ª giornata", "sans", True, 26, 1820),
    ("P7 teaser title 24 bold (<=1300)", "IN DER NÄCHSTEN AUSGABE · Nel prossimo numero (VOL.2)", "sans", True, 24, 1300),
]
bad = 0
for label, s, kind, bold, size, budget in CHECKS:
    w = text_w(s, kind, bold, size)
    flag = "OK " if w <= budget else "OVER"
    if w > budget: bad += 1
    print(f"{flag} {w:7.1f} / {budget}  {label}")

# P7 phrases geometry: quote lines (serif bold 20.5, CW=434), translation lines (sans 19, CW=434)
print("\n--- P7 phrase geometry (tag_y must be < next row start / clinic hline 1968) ---")
phrases = [
    ("Die Nacht hat dann 25 Stunden, und alle dürfen eine Stunde länger schlafen.", "Quella notte ha 25 ore, e tutti possono dormire un'ora in più."),
    ("Im Frühjahr stellt man die Gartenmöbel VOR das Haus — im Herbst stellt man sie ZURÜCK ins Haus.", "In primavera i mobili da giardino vanno DAVANTI alla casa; in autunno tornano DENTRO. (il trucco)"),
    ("Wer vom 26. bis 29. Oktober einen geschnitzten Kürbis abgibt, bekommt für den 31. Oktober ein Freiticket für ein Kind.", "Zucca intagliata consegnata dal 26 al 29 ottobre: ingresso gratis per un bambino il 31."),
    ("Borussia Dortmund gewann am Dienstagabend 2:1 bei Sabah FK in Baku.", "Il Borussia Dortmund ha vinto 2:1 martedì sera a Baku contro il Sabah FK."),
    ("Man wählt ein Buch, ohne es zu kennen.", "Si sceglie un libro senza conoscerlo. (l'appuntamento al buio della biblioteca)"),
    ("84 Prozent von ihnen wollten die Umstellung abschaffen.", "L'84% di loro voleva abolire il cambio dell'ora."),
    ("Die Stunde von 2.00 bis 3.00 Uhr gibt es in dieser Nacht zweimal.", "Quella notte, l'ora dalle 2.00 alle 3.00 appare due volte."),
    ("Aber die Regierungen der Mitgliedstaaten wurden sich nicht einig — und so blieb alles, wie es ist.", "Ma i governi degli Stati membri non si sono messi d'accordo — e tutto è rimasto com'era."),
]
for i, (q, t) in enumerate(phrases):
    row_top = 1520 + 56 + (i // 4) * 204
    qlines = len(wrap("„" + q + "“", "serif", True, 20.5, 434))
    tlines = len(wrap(t, "sans", False, 19, 434))
    t_y = row_top + 21 + (qlines - 1) * 28.3 + 36
    tag_y = t_y + (tlines - 1) * 25.6 + 30
    limit = 1520 + 56 + 204 if i < 4 else 1968
    print(f"phrase {i+1}: qlines={qlines} tlines={tlines} tag_y={tag_y:.0f} limit={limit} {'OK' if tag_y < limit else 'OVER'}")
print("\nOVER count:", bad)
