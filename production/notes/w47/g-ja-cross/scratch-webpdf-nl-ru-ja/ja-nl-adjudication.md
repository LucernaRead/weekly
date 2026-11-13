# ja-nl FAIL-TEXT-MISMATCH adjudication — 2026-11-12 ~00:10 UTC

Dead worker 5881b265 left ja-nl as FAIL-TEXT-MISMATCH (detail-ja.tsv).
Line-level diff of ja-nl.print.txt vs ja-nl.web.txt (both 869 lines):

    7c7
    <   Lucerna   VOL.4         ... (3 spaces after "Lucerna")
    >   Lucerna    VOL.4        ... (4 spaces after "Lucerna")

That is the ONLY differing line. Sorted-line diff and non-blank sorted-line
diff both show only that one line, differing by a single space in the
masthead. Zero content lines missing, zero altered.

Verdict: OK-with-note — pdftotext `-layout` inter-word spacing artifact,
not a content defect. Same adjudication class as the ko-zh sibling worker
(results.tsv: zh-tw-de/es/fr adjudicated OK-with-note for extraction-order
reordering + 1 blank line, zero content missing/altered).

detail-ja.tsv ja-nl row status updated to OK-with-note with this signature.
