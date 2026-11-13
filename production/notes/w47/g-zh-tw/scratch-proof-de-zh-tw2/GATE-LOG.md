# GATE-LOG — 2026-W47 de-zh-tw proof2 机械门记录

- 版：`production/2026-w47/2026-w47-de-zh-tw/`，fix1 重建版（content7.py:76 pad 90→110）
- 工具：`tools/occlusion_audit.py`、`tools/p8.py`、`tools/freeze.py`（`tools/venv/bin/python`）；`boxtitle.py`、`freeze_direct.py`、`keycheck.py` 位于本目录（由 `hidden_files/w47/scratch-fanout-de/` 复制；`tr_zh-tw.py`、`stub_svg.py`、`stub_bslib.py`、`cjk_inventory.json` 由 `scratch-fix-de-zh-tw-toolbox/` 复制，仅供读入，未改动）；`creambox.py` 由 fix1 目录复制；`quote_pixel.py` 为本轮新写（de-en proof2 D1/D2 方法复现，见 §13）
- 全部日志与 JSON 在本目录 `gates/`；渲染件在 `renders/`（100 dpi，2032×2813；200 dpi 4063×5625）
- 探针：每次写盘前 `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` 成功；写盘均在 workspace scratch 目录，`TMPDIR=<scratch>/tmp`；/tmp 未用

## 1. 身份核对（SHA，开工与收尾两次一致）

| 文件 | 大小 | SHA-256（盘上核对一致） |
|---|---|---|
| `Die-Lucerna-VOL4-de-zh-tw.pdf` | 23,048,426 B | `74faeb9d898e254cd3f27a675063739701a9e40e387bde4b3622be5b7f240545` |
| `Die-Lucerna-VOL4-de-zh-tw-web.pdf` | 2,343,141 B | `352ead22cee3fc77c56aa5d036015ba3e309679848cbf722a5e11d22ceb296b9` |
| `2026-w47-de-zh-tw.text.md` | 49,092 B，1,185 行 | `fe62ddb59ac6ee2b2c474c7d11019295652e95e3c6bbd22b138fb4c7e798b0f9` |

两 PDF 均为 8 页，1462.5 × 2025 pt。text.md SHA 与 proof1 版相同（字节一致，零内容变化）。

## 2. fix1 核实（content7.py:76 + creambox）

- 源码：`content7.py:76` 为 `+ 110`（注释：pad 110 恢复 core-de 值；算式：清除量 = pad − 90.8）。
- `creambox.py` 全版扫查（`gates/creambox-full.log`；P7 单页 `gates/creambox-p7.log`）：

```
P7 col-3 rail:
  box y=330 bottom=774.0 last baseline 754.8 clearance +19.2 | 工具箱（末条 '是否……尚未確定'）
  box y=790 bottom=1314.5 last baseline 1304.4 clearance +10.1 | LESERBRIEFE（不变）
  box y=1330 bottom=1480.5 last baseline 1437.6 clearance +42.9 | NOCH EIN WORT（止 1480.5，距 1548 线 67.5px）
```

- 原始 rect 复核（P7 SVG）：工具盒 `<rect x="1439.5" y="330" height="444.0">` → 底 774.0；LESERBRIEFE `y="790.0" height="524.5"` → 底 1314.5；NOCH EIN WORT `y="1330.5" height="150"` → 底 1480.5。
- 全版其余负清除量行均为匹配器已知误报（与 fix1 修复前同位同值）：P1 −37.0（`JETZT ÜBEN`）、−24.0（`DAS WORT DER WOCHE`）；P7 BEISPIELE −35.0×3（题号 101./105./109. 在盒下 35px 处）。其余全部为正（+10.1 ~ +47.7）。

## 3. occlusion 审计 — 0 flags（`gates/occlusion.log`）

```
selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent
…/2026-w47-de-zh-tw/svg: 0 flags
```

## 4. p8 extract — 150/150（`gates/p8extract.log/.json`）

```
…/svg/p8-uebungen.svg: noted set = 150 of 150 (parse: joined)
  set: [1 … 150]
```

## 5. p8 compare（vs core-de）— CLEAN（`gates/p8compare.log/.json`）

```
core    …/core-de/svg/p8-uebungen.svg: 150 noted
edition …/2026-w47-de-zh-tw/svg/p8-uebungen.svg: 150 noted
status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 150]
```

keydiff 说明（见 PROOF-NOTE §4）：Q137–139「譯成繁體中文」键合法不同；Q150 开放写作任务。

## 6. freeze diff — exit 0（`gates/freeze-diff.log/.json`）

```
p1: +33 strings / -40 strings; CJK core 189 -> edition 198; added CJK chars: 109
p2: +30 strings / -30 strings; CJK core 221 -> edition 202; added CJK chars: 89
p3: +35 strings / -35 strings; CJK core 208 -> edition 227; added CJK chars: 135
p4: +21 strings / -21 strings; CJK core 174 -> edition 161; added CJK chars: 80
p5: +36 strings / -35 strings; CJK core 210 -> edition 207; added CJK chars: 121
p6: +31 strings / -31 strings; CJK core 243 -> edition 233; added CJK chars: 109
p7: +56 strings / -57 strings; CJK core 434 -> edition 402; added CJK chars: 174
p8: +141 strings / -132 strings; CJK core 1434 -> edition 1348; added CJK chars: 511
TOTAL added CJK characters: 1328
```

与 proof1 逐页一致。

## 7. freeze_direct — 渲染 8/8 PASS（`gates/freeze-direct.log/.json`）

```
unaccounted removed: 1; unaccounted added: 3
  REMOVED x1: 'Noto Serif CJK SC'
  ADDED x1: 'Noto Sans CJK TC'
  ADDED x1: 'Noto Serif CJK TC'
  ADDED x1: 'TC'
  p1: frozen=151 (core 191 / edition 184) sha8=54c9b51e PASS
  p2: frozen=164 (core 194 / edition 194) sha8=2db0dd83 PASS
  p3: frozen=206 (core 241 / edition 241) sha8=ad74f280 PASS
  p4: frozen=166 (core 187 / edition 187) sha8=df1bebf7 PASS
  p5: frozen=182 (core 217 / edition 218) sha8=b42a8c3d PASS
  p6: frozen=176 (core 207 / edition 207) sha8=babfe417 PASS
  p7: frozen=170 (core 227 / edition 226) sha8=9dc31873 PASS
  p8: frozen=191 (core 323 / edition 332) sha8=961dd98a PASS
source level: FAIL; rendered: 8/8
```

源层级 "FAIL" 仅为 4 条预期内 TC 字体切换串（与 proof1/fix1 相同）；渲染层 sha8 与 proof1/fix1 全 8 页逐项一致（P7 9dc31873 不变——冻结文本未动，只动盒几何）。脚本 RC=1 系源层级 FAIL 所致，属预期（同 proof1）。

## 8. boxtitle（400.5 px 预算）— 7/7 PASS（`gates/boxtitle.log`）

```
[PASS] 'DIE STILLE WOCHE　寧靜的一週' sz=24 w=363.6 budget=400.5
[PASS] 'WEIHNACHTSWÖRTER　聖誕' sz=24 w=333.4 budget=400.5
[PASS] 'DER TIPP　編輯小提示' sz=24 w=252.7 budget=400.5
[PASS] 'ADVENTSWÖRTER　將臨期詞彙' sz=24 w=355.4 budget=400.5
[PASS] 'DER WERKZEUGKASTEN　工具箱' sz=23 w=361.9 budget=400.5
[PASS] 'LESERBRIEFE　讀者來信' sz=23 w=267.3 budget=400.5
[PASS] 'NOCH EIN WORT　再說一句' sz=22 w=287.1 budget=400.5
box titles: 7/7 fit
```

## 9. keycheck — 149/150 exact（`gates/keycheck.log`、`keycheck-150.json`）

```
REG entries: 150; p8extract keys: 150
exact match: 149/150
  MISMATCH n=150 page=8 type=寫作: key='開放任務 — 依寫作框中的要點進行' extracted='開放任務'
```

唯一不匹配为提取器截断；完整键已在 P8 SVG 内验实（`150. 開放任務 — 依寫作框中的要點進行（按所列要點評分）`），非缺陷。

## 10. 印/网文字层比对（`gates/print-*.txt`、`web-*.txt`）

- 印版与网页文字层各 49,905 B；逐页字节数相同：P1 4712 / P2 4738 / P3 6030 / P4 5349 / P5 5340 / P6 5346 / P7 5349 / P8 13041。
- 逐词多重集逐页相同（tokens：717 / 729 / 918 / 843 / 794 / 799 / 730 / 1740）。
- `-raw` 规整化后逐字节相同：48,777 B 两边相等（`gates/print-raw.txt` = `gates/web-raw.txt`）。

## 11. Q34 专项

- 新题干 `Am Montag öffnet in Köln der erste ___.`：content34.py、P3 SVG、text.md、印版文字层、网页文字层各 1×。
- 旧复数题干 `Am Montag öffnen in Köln die ersten ___.`：上述全部位置 0×。
- key `Weihnachtsmarkt` 不变。

## 12. 弯引号全扫（8 个 SVG + text.md + content*.py + 两版 PDF 文字层）

- SVG(8)：U+201C ×33、U+201E ×33、U+00AB ×6、U+00BB ×6、U+201D 0、U+2019 0。
- text.md：同上（33/33、6/6、0/0）。
- content*.py + helpers：201C ×26、201E ×26、00AB ×6、00BB ×6、201D 0、2019 0（7 对 „…" 由家具/生成层产生，不在 content 源内）。
- 印版文字层与网页文字层：201C ×33、201E ×33、201D 0、2019 0。

## 13. 追加测量：de-en D1/D2 闭引号宽体类（`gates/quote-pixel.log`，`quote_pixel.py` + `gates/spots-p8.json` / `spots-p5.json`）

方法：200 dpi 印刷 PDF，单连续窗口像素墨列分析（阈值 <128，0.36 pt/px）；字符 advance 框取自 PyMuPDF rawdict；闭引号墨列以其起点落在 advance 框内（减 1 像素）为准。首版重叠判据曾把 Q67 前一字母 `s` 的墨列误算进引号——已修正并重测，两版数值一致（H 1.80、Q67 1.08、对话 1.44、P5 1.80pt）。

```
H close » (Newsreader 16.12pt) [font=Newsreader16pt-Regular size=16.12pt]
   ink runs (pt): [(640.0, 643.96), (645.04, 651.88), (653.68, 660.88), (662.68, 664.84)]
   prev ink end=651.88 | quote ink=[(653.68, 660.88)] | next ink start=662.68
   GAP BEFORE quote = 1.8pt = 0.11em | GAP AFTER = 1.8pt | PASS (<=0.2em)
Q67 close » (NotoSansCJKtc 9.94pt) [font=NotoSansCJKtc-Regular size=9.94pt]
   ink runs (pt): [(520.0, 523.6), (524.68, 529.36), (530.44, 534.4), (535.48, 539.44), (543.04, 544.84), (546.28, 550.24)]
   prev ink end=534.4 | quote ink=[(535.48, 539.44)] | next ink start=543.04
   GAP BEFORE quote = 1.08pt = 0.11em | GAP AFTER = 3.6pt | PASS (<=0.2em)
P8 dialogue close “ (Newsreader 14.62pt control)
   GAP BEFORE quote = 1.44pt = 0.1em | GAP AFTER = 1.08pt | PASS
P5 title close “ (Newsreader 18.0pt control)
   GAP BEFORE quote = 1.8pt = 0.1em | GAP AFTER = 2.16pt | PASS
```

- H 框指示行字体为 Newsreader（SVG 21.5pt；PDF span `Newsreader16pt-Regular` 16.12pt），不是 sans。
- Q67 注字体为 `NotoSansCJKtc-Regular` 9.94pt；闭引号为 U+00BB »（advance 4.76pt，墨迹起于框内 0.63pt 处，贴左缘），不是 de-en 的 U+201C 全宽字元。
- 200 dpi 裁切目视：`renders/crop-p8-hbox-200dpi.png`、`crop-p8-key67-200dpi.png` 均贴紧，无可见断开。
- 结论：de-en D1/D2 缺陷类在本版**不复现**，两处均 ≤0.2em，已测通过。

## 14. P8 最小字号

- 印版与网页 PDF 均为 9.94 pt（PyMuPDF span 最小值；P8 max 34.5 pt），≥ 9.75 pt 下限。

## 15. chips 独立计数（SVG 徽章节点 `rx="2.7"`）

- 合计 141 = P1 10 / P2 15 / P3 18 / P4 15 / P5 18 / P6 18 / P7 12 / P8 35。

## 16. 禁词（印版文字层，全部 0）

Le Lucerna、The Lucerna、VOL.3、VOL.2、Geisterspiel、Karneval、Volkstrauertag、NFL、American Football、11.11、Tankrabatt、14,04、Hart aber fair、Klassiker、Allerheiligen、8,35、ZEW。

## 17. 繁體字形审计

- 渲染文本（8 SVG + text.md）简体专属字扫描：NONE（扫描表含 为/国/学/读/说/请/还/过/这/进/运/连/长/门/间/开/关/见/话/译/护/圣/诞/历/愿/里/复/并/乐/义/发/头/凤/龙/龟/丽/达/迟/卢/罗/玛/苏/尔/纳/图/画/应/当/无/从/让/认/识/实/对/广/庆/节/观/现/点/电/车/马/风/飞/饭/馆/鸡/欢/难/轻/万/亿/惊/忆/录/剧 等；`常` 仅见于 平常/常見——简繁同形，已从误报中剔除）。
- SVG 内不同 CJK 共 419 字；TC 形 為/國/學/讀/說/請/還/過/這/進/運/連/長/門/間/開/關/見/話/譯/護/聖/誕/曆/願/裡/複/並 全部在位。

## 18. 字体嵌入（`gates/pdffonts-print.log` / `pdffonts-web.log`）

- 两 PDF 全部字体 emb=yes。网页版已嵌 `LucernaNewsreader-Italic`（对象 40；proof1 缺 Italic 备注已解决）；`LucernaNewsreader-Bold` 有多个子集条目，属 webpdf 子集化行为，渲染正常。

## 19. 日期/星期（`date`，Europe/Berlin）

- 2026-11-03 周二、11-04 周三、11-05 周四、11-06 周五、11-07 周六、11-08 周日、11-13 周五、11-16 周一、11-17 周二、11-18 周三、11-20 周五、11-22 周日、11-24 周二、11-25 周三、11-26 周四、11-27 周五、11-29 周日、12-01 周二、12-23 周三——与正文声称全部一致。

## 20. 渲染记录

- 印刷版 8 页：`renders/print-p-1.png` … `print-p-8.png`（pdftoppm 100 dpi，2032×2813；PIL 校验全部通过）。
- 网页版：`renders/web-p1-1.png`、`renders/web-p8-8.png`（100 dpi）。
- 200 dpi：`renders/print-p5-200dpi-5.png`、`print-p7-200dpi-7.png`、`print-p8-200dpi-8.png`（4063×5625）；裁切 `crop-p8-hbox-200dpi.png`、`crop-p8-key67-200dpi.png`、`crop-p7-toolbox-200dpi.png`、`crop-p7-col3bottom-200dpi.png`。
- /tmp 未用（开工时 /tmp 仅 2% 已用，仍按任务要求全程用 scratch TMPDIR）；未动他人文件。

## 21. 门禁汇总

| 门 | 结论 |
|---|---|
| occlusion | 0 flags ✓ |
| p8 extract | 150/150 ✓ |
| p8 compare | CLEAN ✓ |
| freeze diff | exit 0 ✓ |
| freeze_direct | 渲染 8/8 PASS ✓（源层仅预期 TC 字体串） |
| creambox P7 | 工具盒 +19.2 / LESERBRIEFE +10.1 / NOCH EIN WORT 止 1480.5 ✓ |
| Q34 | 新 1× / 旧 0×（五处） ✓ |
| 弯引号 | „…" 33 对、«…» 6 对 ✓ |
| 闭引号宽体加测 | H 0.11em / Q67 0.11em，两处 PASS ✓ |
| P8 最小字号 | 9.94 pt ✓ |
| boxtitle | 7/7 ✓ |
| keycheck | 149/150（Q150 为提取器 artifact，已验实）✓ |
| 印/网文字层 | 内容同一 ✓ |
| 繁體字形 | 渲染文本干净 ✓ |
| text.md | 与 proof1 版字节一致 ✓ |
