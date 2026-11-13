# W47 nl fan-out — build report (builder: fan-out builder, 2026-11-10/11)

Source: frozen core `production/2026-w47/core-nl/` (slug `2026-w47-nl-zh-cn`,
VOL.4, 2026-11-16–2026-11-22, 150 exercises). Target: the other 10 reader
languages, one edition at a time, self-checked to zero before the next.
Order: en → de → fr → es → it → pt → ru → ja → ko → zh-tw.
Output dirs: `production/2026-w47/fanout-nl/2026-w47-nl-<reader>/`
(not moved; coordinator decides later).

## Common pre-build fixes (all editions, explanation-layer only)

Pre-build sweep (`sweep.py`) found the same 5 defect classes in every
generated edition (gen_fanout had copied the core's 36/8 subtitle and
full-length glosses). Fixed per language with W46 precedents:
subtitle size/spacing, numbers-box title, numbers-box item parentheticals
(cliff: box must fit col 1, total ≤ 405px), P6 chart head, ZO ONTHOUD
title. zh-tw needed none of these (all measured in limits).
`p7check.py` (added 2026-11-11) found a 6th class: the P7 BRIEVEN box
overflowing past the ZINNEN rule (y=1937) in 9/10 editions (zh-tw clean
at 1898, core 1898) — fixed with W46-telegraphic short glosses; all 10
now end 1898–1928, above the rule.

## Per-edition rows

| edition | print PDF (bytes / sha256) | web PDF (bytes / sha256) | gates | visual | record |
|---|---|---|---|---|---|
| en | 12,690,133 / `0b4dc8c0…99f2e7` | 1,576,939 / `477dd85d…8de6` | ALL PASS (occl 0, p8 150/150 CLEAN, freeze 8/8, print/web 0/0, font 10.12pt, chips = core, §1.1 clean) | 8/8 clean | `en.md` |
| de | 12,669,843 / `0df8e614…d7fc13e` | 1,581,124 / `8859e18a…f8de64` | ALL PASS (occl 0, p8 150/150 CLEAN, freeze 8/8, print/web 0/0, font 10.12pt, chips = core, §1.1 clean) | 8/8 clean (P1 agenda gloss + P7 golden #2 fixed, see record) | `de.md` |
| fr | 12,704,394 / `e6db69e3…fb60a` | 1,577,894 / `d26a0b57…e5a0` | ALL PASS (occl 0, p8 150/150 CLEAN, freeze 8/8, print/web 0/0, font 10.12pt, chips = core, §1.1 clean) | 8/8 clean (P1 box jump + P8 overflow + 2 head spills fixed, see record) | `fr.md` |
| es | 12,669,477 / `47f15cc8…f0ec1` | 1,579,768 / `4b416858…fb20` | ALL PASS (occl 0, p8 150/150 CLEAN, freeze 8/8, print/web 0/0, font 10.12pt, chips = core, §1.1 clean) | 8/8 clean (P8 overflow fixed via 5 note shortenings; P6 head 401px marginal, invisible) | `es.md` |
| it | 12,715,556 / `a05cc4be…5ab3c` | 1,575,654 / `072c7f2e…01fe9` | ALL PASS (occl 0, p8 150/150 CLEAN, freeze 8/8, print/web 0/0, font 10.12pt, chips = core, §1.1 clean) | 8/8 clean (P8 overflow + P6 VOOR OF TEGEN head fix) | `it.md` |
| pt | 12,671,956 / `d70937d8…e4cc5` | 1,582,075 / `05faf026…658e` | ALL PASS (occl 0, p8 150/150 CLEAN, freeze 8/8, print/web 0/0, font 10.12pt, chips = core, §1.1 clean) | 8/8 clean (P8 overflow fixed via 5 note shortenings) | `pt.md` |
| ru | 12,718,342 / `d60da278…cd542` | 1,625,792 / `22ac256f…4c4` | ALL PASS (occl 0, p8 150/150 CLEAN, freeze 8/8, print/web 0/0, font 10.12pt, chips = core, §1.1 clean) | 8/8 clean (P8 structural overflow + P2 GEDICHT strip fix) | `ru.md` |
| ja | 26,049,268 / `af010c1f…61c1b1` | 2,119,188 / `07243a6b…d1d2f` | ALL PASS (occl 0, p8 150/150 CLEAN, freeze 8/8, print/web 0/0, font 10.12pt, chips = core, §1.1 clean) | 8/8 clean (build 1, no P8 overflow) | `ja.md` |
| ko | 17,281,555 / `d72e53eb…0fed8` | 1,884,427 / `a5b50f59…c119` | ALL PASS (occl 0, p8 150/150 CLEAN, freeze 8/8, print/web 0/0, font 10.12pt, chips = core, §1.1 clean) | 8/8 clean (build 1, no P8 overflow) | `ko.md` |
| zh-tw | 25,995,622 / `a2a86521…34c34cc` | 2,343,866 / `daab1ef2…929dc` | ALL PASS (occl 0, p8 150/150 CLEAN, freeze 8/8, print/web 0/0, font 10.12pt, chips = core, §1.1 clean) | 8/8 clean (build 1, no fixes needed) | `zh-tw.md` |
