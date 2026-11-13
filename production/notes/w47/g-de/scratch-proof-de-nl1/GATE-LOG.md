# GATE-LOG — 2026-W47 de-nl · proof1

探针（开工前）：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin`
→ `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，RC 0；写盘探针
`scratch-proof-de-nl1/probe.txt` 成功。写 PROOF-NOTE 前重探：同上，RC 0。
磁盘：`df` 77–78G 可用，无 EDQUOT。

## SHA 核对

```
cd production/2026-w47/2026-w47-de-nl
sha256sum Die-Lucerna-VOL4-de-nl.pdf Die-Lucerna-VOL4-de-nl-web.pdf 2026-w47-de-nl.text.md
→ 8f47eea85f54067532cad3e21ba74d3ed98133a3eabc5605dcb34ca3cca8d6d6  print  (10,964,699 B) ✓
→ be22a1b5beda4dcaaeccbcffcb7a122e01bb3f92a488d896fd261808ffc34551  web    (1,553,854 B) ✓
→ e904fb3d7ee18a72c1316f8693f39436ff9390648261d6fbad18afcfb7fc848e  text.md (49,403 B) ✓
```
RC 0，三者均与任务给定相符。

## 文本层提取

```
pdftotext -layout print → work/print.txt (114,746 B)
pdftotext -layout web   → work/web.txt   (114,746 B)
pdftotext -layout core  → work/core.txt  (111,693 B)
pdftotext (default) print → 50,192 B ; web → 50,194 B ; 词集相同
pdftotext -raw print/web → 各 47,634 B；归一化后逐字相同
```
RC 0。

## occlusion_audit.py（独立重跑）

```
tools/venv/bin/python tools/occlusion_audit.py production/2026-w47/2026-w47-de-nl/svg
→ selftest OK: planted classes fired {BOXTITLE, COVER, EDGE, FOOTER, LINEX, TEXTX};
  clean controls silent
→ production/2026-w47/2026-w47-de-nl/svg: 0 flags
RC 0
```

## p8.py（独立重跑）

```
tools/venv/bin/python tools/p8.py compare --core-p8 production/2026-w47/core-de/svg/p8-uebungen.svg \
  --edition-p8 production/2026-w47/2026-w47-de-nl/svg/p8-uebungen.svg --total 150
→ core 150 noted / edition 150 noted
→ status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 150]
RC 0
tools/venv/bin/python tools/p8.py extract --p8 <edition>/svg/p8-uebungen.svg --total 150 --json work/p8extract.json
→ noted set = 150 of 150 (parse: joined)
RC 0
```

## freeze.py diff（独立重跑）

```
tools/venv/bin/python tools/freeze.py diff --core-svg production/2026-w47/core-de/svg \
  --edition-svg production/2026-w47/2026-w47-de-nl/svg --json work/freeze.json
→ p1 +31/-44, p2 +34/-31, p3 +43/-46, p4 +25/-21, p5 +40/-44, p6 +35/-32, p7 +61/-77, p8 +145/-137
→ TOTAL added CJK characters: 7 （全为 U+3000，P2–P8 各 1，P1 0）
RC 0
```

## keycheck.py（独立重跑，builder 脚本 + 自采 p8extract.json）

```
tools/venv/bin/python keycheck.py nl <edition-dir> work/
→ REG entries: 150; p8extract keys: 150
→ exact match: 149/150
→ MISMATCH n=150 (schrijven): key='Open opdracht — volg de punten in het schrijfblok'
  extracted='Open opdracht' （提取器截断，预期）
→ wrote work/keycheck-150.json
RC 0
```

## boxtitle.py nl（独立重跑）

```
tools/venv/bin/python boxtitle.py nl
→ 7/7 [PASS]：DIE STILLE WOCHE 372.7 / WEIHNACHTSWÖRTER 347.1 / DER TIPP 356.5 /
  ADVENTSWÖRTER 319.4 / DER WERKZEUGKASTEN 395.5 / LESERBRIEFE 380.4 / NOCH EIN WORT 362.0
  （预算 400.5）
RC 0
```

## Q34 / 弯标点 / CJK 扫描（python 直接计数，见 PROOF-NOTE §5–§6）

- 新题干 `Am Montag öffnet in Köln der erste ___.`：content34.py 1、text.md 1、
  p3 SVG 1、印刷文本层 1、网页文本层 1；旧题干 `Am Montag öffnen in Köln die ersten ___.`：0。
- U+201D = 0、U+2019 = 0（8 SVG + text.md + 源码）；U+201C = 33，U+201E = 33，
  逐一配对且全在德语引文内；直撇号 `'` 全版 0 处。
- CJK：U+3000 ×146 + moth 标志 title 内 `三色蛾` 3 字（非渲染文本）。

## abutting 扫描（d2scan-full.py 改写 de-nl 路径，work/d2scan-de-nl.py）

```
tools/venv/bin/python d2scan-de-nl.py
→ abutting pairs scanned: 54
→ worst web gap: 0.00 pt (1, 12.75, 'VOL.', ' ', 0.0)
→ gaps >0.5pt: 0
```
补充：印刷 vs 网页逐行/逐跨度宽度比对（1,850 行）：Newsreader 行宽差 >0.5 pt
共 61 行（见 PROOF-NOTE §7）；Noto 跨度差 0.00%。tools/webpdf.py 已含
`:weight=200`/`:weight=100` 补丁（第 94–98 行）。

## 日期核实

```
for d in 2026-11-13 2026-11-16 2026-11-17 2026-11-18 2026-11-20 2026-11-22 2026-11-27 2026-11-29
→ Fri 13 / Mon 16 / Tue 17 / Wed 18 / Fri 20 / Sun 22 / Fri 27 / Sun 29
```
RC 0。

## MUSTER 词数

```
whitespace split: 84 词（与标注 84 一致）
```
