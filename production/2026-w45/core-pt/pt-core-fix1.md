# FIX1 — W45 Português core, VOL.2 (BRAZIL variant)

**Trigger:** independent proofread `hidden_files/w45/pt-core-independent-proof.md`
(2026-10-26), verdict 1 problem — NOT zero-problem, do not finalize yet.
**Scope:** exactly the 1 problem below. Nothing else changed: no new articles,
no new facts, no rewording beyond this fix, no changes to lead, images, credits,
or ABSTRACT. The proofreader's confirmed Nov 7 18h Arena MRV time (via Sportradar)
was left untouched, as instructed — no action needed on that item.

## Problem (PROMISE GAP, P7 readers' corner)

W43 VOL.1 promised "as suas cartas e os melhores textos da página 8" for VOL.2.
VOL.2 printed neither: it printed a labeled editor's example letter and
re-promised both items for VOL.3. The labeling itself was unambiguous
("— EXEMPLO DA REDAÇÃO" + "编辑部示例，非真实来信", no invented name) and was
NOT the problem; what was missing was the on-page deferral disclosure
(KIT-only disclosure does not satisfy the on-page standard, same standard as
EN/ES/NL this cycle). Parent decision (binding): disclose on the page, do NOT
fabricate letters or texts.

## Fix applied (in the P7 corner itself, `content7.py` letters box only)

Added an on-page disclosure directly below the existing example note, inside
the CARTAS DOS LEITORES box:

- PT (21.5 serif, 5 lines): "Nota da redação: as cartas reais e os melhores
  textos prometidos no VOL.1 não chegaram até o fechamento — fica o exemplo,
  e a promessa passa para o VOL.3."
- CN (19.5 sans, 2 lines): "编辑部说明：上期承诺的真实来信与最佳作文截稿时未收到，
  本期仍刊示例，顺延至下期。"

Existing labeling kept verbatim: example letter text, "— EXEMPLO DA REDAÇÃO",
and "编辑部示例，非真实来信。真实来信请寄编辑部，下期见！" are all unchanged.

## Reflow handling (P7 only, minimal)

- Letters box height 257.5 → 489.0 (box y 1304.5 → ends 1793.5).
- Disclosure last baseline 1772.23, i.e. 21.3 px of padding inside the box —
  fully inside, no overlap with the box border.
- Golden-sentences row pitch 158 → 128 (P7 only); last golden CN baseline
  2358.17, preview box top 2404 — clear.
- Footer, preview box, and all other pages untouched.

## Re-render + gates (full issue, after fix)

- `run.py` (all 5 content files) + `render.py`: 8 SVGs, 8 PNGs,
  `A-Lucerna-VOL2.pdf` (15,963,444 bytes, 8 pages),
  `A-Lucerna-VOL2-web.pdf` (3,292,156 bytes, 8 pages).
- Build warnings: FLOW OVERFLOW 0, HEAD TOO WIDE 0 (grep of a second full
  `run.py` pass: no matches).
- Exercises: 150 total, continuous 1–150; per page 10/18/18/18/18/18/12/38;
  levels A2 49 / B1 70 / B2 31; model essay 93 words; P8 noted set 150/150
  (`tools/p8.py extract --total 150`).
- Builder re-read of changed P7 (SVG text + rendered PNG): example letter,
  existing note, and disclosure all present and legible; no overlap; golden
  section and preview box clear; footer intact.
- Occlusion audit (`tools/occlusion_audit.py`, selftest first): selftest OK
  (all six planted classes fired, clean controls silent); edition run
  **0 flags** — nothing to adjudicate.
- Banned term check: "桥接" 0 hits across all 8 SVGs.

## Not done here (by design)

- No git push, no Discord post, no messages sent.
- No self-certification of finalization: a fresh full independent proof round
  is still required (SOP §8.4) and is for the parent to order.
