# GATE-LOG — 2026-W47 pt-de re-proof（fix1 重建版独立复校，全部门禁实跑记录）

复校员 re-proof，2026-11-11。工具链：`~/workspace/weekly-git/tools/venv/bin/python`
（Python 3.12.3 / Pillow 13.0.0）；TMPDIR 全程指向 scratch 下 `tmp/`（系统 /tmp 未用）。
正典 creambox：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py`
（与 proof1/proof2/fix1 所用同一文件）。所用运行命令与输出均列于下；KIT 自述数值一律不采信，
只认以下本人实跑结果。Scratch：
`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-pt-de1/`
结论见同目录 `PROOF-NOTE.md`；本文件只记门禁实跑。生产目录零写入。

## §0 身份与探针

- 探针：`ls -la /dev/null` 存在（crw-rw-rw-，1, 3）；`echo test | git hash-object -w --stdin` →
  `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，RC=0（与 proof1/proof2/fix1 同值）。
- SHA/字节核对（`sha256sum` + `stat`，开工与收工各一次，一致）：
  印 PDF 12,938,912 B `b8a738de…a513d` ✓；网 PDF 1,147,636 B `2cad3d1b…83e69` ✓；
  text.md 37,907 B `519ab0de…d784305` ✓（与修前逐字节相同）。与任务预期完全一致。
- 核心 HEAD：`c0382fa7`；版目录 git 状态 `?? production/2026-w47/2026-w47-pt-de/`（未入仓）；
  `core-pt/` 只读，未动。本次未 commit、未 push。

## §1 run.py + render/gates（scratch 副本）

命令：`cp -r` 版目录至 scratch `build-copy`，删 svg 后在其中运行 run.py（`run.log`）；
gates.py 在同一 build-copy 内运行（`gates.log`）。
- run.py：RC=0，`P8 saved, TOTAL exercises: 150`，`TOTAL 150`，`ALL DONE`，`OVERFLOW` 0 行。
  by level `{'A2': 48, 'B1': 71, 'B2': 31}`；by page `{1: 10, 2: 18, 3: 18, 4: 18, 5: 18, 6: 18, 7: 12, 8: 38}`；
  by type：Sätze vervollständigen 61 / Multiple Choice 49 / Wortschatz-Zuordnung 12 / Satzbildung 7 /
  Richtig oder falsch 3 / Lückentext mit Auswahl 13 / Übersetzung 4 / Schreiben 1；model words 88。
- 重建 SVG 与现盘 SVG：`cmp` 8/8 IDENTICAL（p1–p8 全同）。
- gates.py：16 处 `[PASS]`，`FAILURES: none`，RC=0。

## §2 freeze baseline（8/8，两路）+ freeze diff

- 核心 freeze（`--build` 真核心 core-pt，`--core-svg` 核心 svg）：
  `tools/freeze.py baseline --build production/2026-w47/core-pt --core-svg production/2026-w47/core-pt/svg --out <scratch>/freeze-core`
  → `freeze-core.log`：`baseline: 8/8 SVGs byte-identical`，核心哈希与 proof2 一致
  （bd87a867…a7b7a661，p8 a7b7a661）；`core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)`，RC=0。
- 版 freeze：`--build` 版目录、`--core-svg` 版 svg → `freeze-ed.log`：
  `baseline: 8/8 SVGs byte-identical`，RC=0。
  字节哈希：p1 **6ced52ce**、p2 613f558b、p3 c33752e6、p4 af3e206b、p5 d146ca3d、p6 dd562a7a、p7 2d53f697、p8 a4447964。
- freeze diff（core vs edition，正确语法 `--core-svg … --edition-svg … --json`；首版误传 `--out` 得 rc=2，已纠正重跑）：
  `freeze-diff.log` / `freeze-diff.json`，RC=0；新增 CJK 共 9 个，全部为 U+3000 家具分隔符（P1: 2，其余每页 1）。

## §3 occlusion 审计 — 0 标记（附盲区说明）

命令：`tools/venv/bin/python tools/occlusion_audit.py production/2026-w47/2026-w47-pt-de/svg --json <scratch>/occlusion.json`
输出：`production/2026-w47/2026-w47-pt-de/svg: 0 flags`，RC=0；`occlusion.json`：`"flag_count": 0`。
（工具另打印一行自检阳性对照通过——为工具内置输出，非 `--selftest` 调用；本次未传 `--selftest`。）
**盲区**：同 proof2 所述，BOXTITLE 检查只看带描边或 fill `#2c2822` 的矩形，
无描边奶油框（`fill="#f0eee5"`）根本不在检查之列。本次验收不依赖 occlusion，改以 §4 的 boxtitle 真墨 + PDF 像素双法复测。

## §4 框标题横向实测 — D4 已修复，E1/E2 原位

1. 源码核对：`content12.py:89` `"NESTA EDIÇÃO　Diese Ausgabe"`；`tables_de.py:139` `"本期目录": "Diese Ausgabe"`；
   本版 `*.py` grep `In dieser Ausgabe` RC=1（0 处）。
2. 本人 PIL 真墨实测（`boxtitle_ink.py`，`boxtitle-ink.log`）：31 框标题，OVERFLOW 0 处。
   NESTA 墨迹右缘 **1826.5，clear +35.5**（框右缘 1862.0，合格 ≤1858）；
   EM POUCAS 1861.5（+0.5）、A SEMANA EM NÚMEROS 1410.0（+1.5），均与修前同值。
3. PIL advance（`boxtitle_core.py`，`boxtitle.log`）：NESTA `title_w=364.6 right=1826.1 clear=+35.9`；OVERFLOW 0 处。
4. 交付印 PDF 像素实测（`pixel_boxtitle_pdf.py` 200dpi，`pixel-boxtitle-pdf.log`）：
   NESTA 墨迹右缘 **1826.9，clear +34.6**；EM POUCAS 1862.4（与修前同值）；
   A SEMANA EM NÚMEROS 1408.3（clear +2.9）。脚本内标题标签仍写旧串 `In dieser Ausgabe`，
   但测量带取实际渲染标题行，测得值即新标题实测值。
5. 目视：300dpi 原生裁图 `visual/crop-p1-nesta-pdf300.png`——`Diese Ausgabe` 末字 `e` 完整在奶油框内，
   右端距框缘约 35 单位。

## §5 正典 creambox 全版扫描 + diag — 31 框；D1/D2/D3 存活

命令：正典 `creambox.py svg/*.svg`（`creambox.log`）+ `creambox_diag.py svg/*.svg`
（`creambox-diag.log`），RC 均为 0。
- 31 框 OWN 真墨余量全部为正，最小 **+2.1**（P2 `Palmeiras–Flamengo-Duell`，墨底 1765.9，框底 1768.0）。
- D1：P1 闪讯框（y=1874，bottom=2348.0）末行 `em Brasília. (Página 4)` 基线 2327.6，
  墨底 2332.6，墨余 **+15.4**。修复存活 ✓。
- D2：P3 日程框（y=200，bottom=551.0）末行 `16h30.` 基线 540.6，墨底 540.9，墨余 **+10.1** ✓。
- D3：P6 时间线框（y=200，bottom=854.0）末行 `Página do Participante.` 基线 840.8，
  墨底 846.0，墨余 **+8.0** ✓。
- 5 处 below-window 负 clearance（−32.0 ×1、−37.0 ×2、−42.0 ×2）均为已知假阳性：
  下块标题/段落（P1 `AGORA VOCÊ…` +37.0、P2 `Atenção:…` +32.0、P3 `UM DIA, DOIS SENTIDOS` +37.0、
  P6 `EXERCÍCIOS　SEITE 6 ÜBUNGEN` +42.0 ×2），creambox-diag 判 owner-rect=NONE，与修前同。
- 6 处 inside-only desc-clear 负值（−0.3…−1.1）均为误报，与修前同行：
  diag 真墨复测墨迹底 ≈ 基线 +0.2–0.5（无降部字母），墨余 +4.8–5.4，无漫出。
- P7-TOOLBOX 汇总（`creambox.log`）：3 框，min inside clearance +5.1，min desc-clear −0.9；
  diag 真墨余量：ERROS +24.6、A PALAVRA +4.8、CARTAS +5.9。

## §6 p8 / keycheck / sweep / gloss

- `tools/p8.py extract --p8 svg/p8-avaliacao.svg --total 150 --json <scratch>/p8-extract.json`：
  `noted set = 150 of 150`，RC=0（`p8-extract.log`）。
- `tools/p8.py compare --core-p8 core-pt/svg/p8-avaliacao.svg --edition-p8 svg/p8-avaliacao.svg --total 150 --json <scratch>/p8-compare.json`：
  `status CLEAN, total 150, core 150, edition 150, keydiff [137, 138], missing []`，RC=0。
  （直接读 `p8-compare.json` 本体核实；gates.json 的 p8 extra "?" 未采信。）
- keycheck（`keycheck.log`，`keycheck-150.json` 写在本 scratch 内——脚本按自身所在目录写出，
  本次用的 scratch 副本，故未覆盖他人文件）：`REG entries: 150; p8extract keys: 150; exact match: 149/150`；
  唯一 MISMATCH：`n=150 page=8 type=Schreiben: key='(offene Aufgabe — Mustertext unten)' extracted='✓'`（预期）。RC=0。
- sweep（`sweep.log`）：box-vs-hline flags 0；bridges found 20；bridge orphans **2**；
  bridge widows **0**；RC=0。2 个 orphans 均为 `Ergänzen Sie mit den Wörtern aus dem Kasten.`
  （content34.py:85、content56.py:79），候选坐标 P3/P5 行 1 `(88.0, 2564.45)`、行 2 `Kasten. (538.5, 1696.5)`——
  与修前备份 SVG 坐标逐字节相同（proof1 O4，KIT 已注明，核心流式排版行为）。
- gloss（`gloss.log`）：P4 gloss 框 rect#0 x=989.0 y=270.48 w=422.5 h=175.4 bottom=445.88，
  4 行，末行 `pausa die Pause · a taça Pokal.` 右余 +101.5、底余 +42.7；
  `GLOSS VERDICT: lines=4 last-line right clear +101.5 last-line bottom clear +42.7 overflow=no`。
  渲染 `o título Titel`（第 3 行）。D5 完好。

## §7 印/网文字层、字号、孤儿标点、D5 字体

- 网 PDF scratch 重渲（`web-rerender.pdf`，`webpdf-scratch.log`）：1,147,640 B（生产网 PDF 1,147,636 B），
  SHA 不同（重渲 vs 交付，为任务预告的预期现象——fontTools 嵌时间戳）；
  文字层逐页与交付网 PDF 一致（`cmp web-rerender.txt web.txt` 通过）。交付网 PDF 未被 scratch 文件覆盖（收工 SHA 仍为 `2cad3d1b…`）。
- `pdftotext -layout` 印 vs 生产网：逐字节一致，111,358 B（修前 111,362 B，差 4 字节为标题删去 `In ` 的文本所致；
  `print.txt` / `web.txt`，cmp 通过）。
  fitz 逐页比对（`text_compare.py`，`textdiff.log`）：8/8 页 print-bytes == web-bytes
  （5366/4598/4280/4919/4599/4536/5215/13489；P1 5370→5366 为标题少一词所致）。
  对 scratch 重渲网 PDF 同为 8/8 一致。
- check_final（`check-final.log`）：`pages print=8 web=8`；`words print=8435 web=8435 multiset-diff=0`
  （修前 8,436；差 1 为标题删去的 `In` 一词）；P8 answer-region span sizes [9.75, 10.5, 14.625, 18.75]，min 9.75。
- minfont（`minfont.log`）：`P8 min effective font size = 9.75 pt (n=380)`；`below 9.75pt: 0`。
- 斜体 span（fitz）：印 1 = 网 1，文本同为 `« consciência »`。
- 孤儿标点（`orphan_scan.py`，`orphan.log`）：SVG 全部 `<text>` 行首扫描（1,637 行）——
  以 `, . ; : ! ? » ) ] }` 开头或仅为标点的行 **0** 条。
- 弯引号/CJK/禁词（exec 内联扫描）：text.md `«` 40 = `»` 40，`“` 2 = `”` 2，单弯引号 0；
  SVG `«` 40 = `»` 40，无失衡文件；text.md CJK 字符 0；SVG 非 U+3000 CJK 仅 3 字（`三色蛾`，
  位于 P1 logo `<title>Lucerna 三色蛾</title>` 元数据内，非渲染正文，core-pt 8 页 SVG 亦同款）；
  text.md 内 `简体/繁体/中文/TODO/XXX/Lorem` 均为 0。
- D5 字体（只记录不判）：P5 印 PDF 4 个内嵌字体子集
  （`NGCYSB+NotoSansCJKsc-Regular`、`UIKPPO+Newsreader16pt-Regular`、`WRUMGD+Newsreader16pt-Regular`、
  `YCHKXS+NotoSansCJKsc-Bold`；即 3 个字体族）。

## §8 溢出横扫（gate 7，本人新写 sweep_overflow.py）

方法：189 个矩形 × 1,637 行文本逐一 PIL 真墨核算；凡墨迹与任一矩形垂直重叠且横向/纵向越过矩形边 >0.5 单位即标记，
另标墨迹越过内容边 88.0/1862.0 的行。结果：13 标记（`sweep-overflow.log`）。
同脚本扫 core-pt 得 **逐项相同的 13 处**（`sweep-overflow-core.log`，同文本、同数值，仅家具串中德/中文不同），
**本版新增溢出 0**：
- 12 处 PAGE-LEFT：左对齐标题大写字母字形侧边距伸出内容边 88.0 仅 1.0 单位（墨迹 87.0），核心同款，设计固有。
- 1 处 V-SPILL：P8 `A　COMPLETE A CRÔNICA`（墨底 202.0 vs 刊头带底 182.0）——本人脚本窗口过宽的假阳性，
  该标题基线 y=202 在刊头带（88,72,1774×110）之下，本就不属于该框；核心同款。

## §9 回归复验（修前基线比对）

- 以 proof2 修前基线为准（`scratch-proof-pt-de2/build-copy/svg/` + freeze 哈希 f988db96…a4447964）：
  仅 **p1 不同**（f988db96 → 6ced52ce，即 D4 标题一处），**p2–p8 cmp 逐字节一致**（7/7）。
- 任务括号所指 `scratch-refanout-pt/backup-old/` 是第一轮备份（core-pt fix2 重 fanout 之前）：
  其 p2/p5/p7 与现盘相同，p3/p4/p6/p8 各差 1 行（SVG 为单行文件）——那是 D1/D2/D3 核心修复本身，
  非 fix1 回归；以 proof2 基线为准才是 fix1 前后比对的正确口径。
  （注：中途一次 `cmp` 因路径多写一层 `/svg` 误报全异，已纠正重跑，上述为纠正后的结果。）
- D1/D2/D3 源码行与实测见 §5（474 / +58 / 654；+15.4 / +10.1 / +8.0）；E1（+0.5）/E2（+1.5）见 §4，未动。

## §10 check_s11 / verify_ed（pt 适配版）

pt 系无此二脚本的现成版本（现存副本均为 en 系硬编码，不可用）。沿用 fix1 在其 scratch 写的 pt 适配版
（en 原版未动），按 `de` 运行：
- `check_s11_pt.py`（`check-s11.log`）：RC=0，`ALL §1.1/P8 CHECKS PASS`。
  色集 core 21 = edition 21，extra/missing 均为 none；徽章色 A2/B1/B2 齐全；
  P8 最小 SVG 字号 13.0 单位（= 9.75pt）；P8 芯片数/色与核心一致（35：B1 24 / A2 8 / B2 3）；
  题号文本 113–119 + 145–149 与 `120.` 齐全；`ESCREVA VOCÊ` 在位。
  芯片位置与核心差 8 处（fix1 记 4 处，计数口径差），P8 SVG 与修前基线逐字节一致（a4447964），
  属修前既有德语排版流位移，非本次改动所致。
- `verify_ed_pt.py`（`verify-ed.log`）：RC=0，`ALL pt-de fix1 VERIFICATIONS PASS`（23/23）。
  含：D4 源两处 + SVG + PIL 真墨（1826.5 ≤1858）+ PDF 像素 200dpi（1826.9 ≤1858）；
  E1 +0.5、E2 +1.5 均原位；D1/D2/D3 源码行（474 / +58 / 654）在位 + creambox 实测
  （+15.4 / +10.1 / +8.0）；Q137/138 德语键逐字一致、Q150 `✓`；text.md SHA 不变；两 PDF 各 8 页。

## §11 150 题手验与目视

- text.md 535 行通读；keycheck 机械比对 149/150（仅 #150）；Respostas 节键与各页练习键逐项一致；
  范文重数 88 词（实测 88）。逐题结论见 PROOF-NOTE.md（Q73、Q83–87、Q120、Q125、Q137–140、
  Q141–149 等全部正确；Q125 外部核实结论沿用 proof1）。
- 目视（印 PDF 渲染，130dpi，`visual/p-1.png`…`p-8.png` + 300dpi 裁图）：无新缺陷；
  所见均为已知接受项（O4 `Kasten.` 孤字 P3/P5、`B AS PALAVRAS` 栏目标题落栏底、P2/P5 中部版式留白、E1 贴框边）。

## 附：输出文件（本 scratch 目录）

- `PROOF-NOTE.md`（结论 + 三 SHA 实测 + 缺陷清单——无缺陷）、`GATE-LOG.md`（本文件）
- `de-textdiff.json`、`de-p8size.json`（check_final 写出：multiset diff 0 / P8 min 9.75pt）
- `keycheck-150.json`、`p8-extract.json`、`p8-compare.json`、`freeze-diff.json`、`occlusion.json`
- `run.log`、`gates.log`、`freeze-core.log`、`freeze-ed.log`、`freeze-diff.log`、`occlusion.log`、
  `p8-extract.log` + `p8-compare.log`、`creambox.log`、`creambox-diag.log`、`boxtitle-ink.log`、
  `keycheck.log`、`sweep.log`、`sweep-overflow.log` + `sweep-overflow-core.log`、`print.txt`、`web.txt`、
  `textdiff.log`、`minfont.log`、`check-final.log`、`gloss.log`、`orphan.log`、`pixel-boxtitle-pdf.log`、
  `check-s11.log`、`verify-ed.log`、`webpdf-scratch.log`
- `sweep_overflow.py`（gate 7 新写）、`boxtitle_ink.py`、`boxtitle_core.py`、`pixel_boxtitle_pdf.py`、
  `pixel_compare.py`、`orphan_scan.py`、`check_s11_pt.py`、`verify_ed_pt.py`、`text_compare.py`、
  `keycheck_core.py`、`creambox_diag.py`、`sweep_de.py`、`minfont.py`、`gloss_probe.py`、`check_final.py`
  （除 `sweep_overflow.py` 外均为 fix1/proof2 scratch 的未改动副本）
- `web-rerender.pdf`（scratch 重渲网 PDF；交付网 PDF 未动）、`web-rerender.txt`
- `visual/`（`p-1.png`…`p-8.png`、`crop-p1-nesta-pdf300.png`）
- `freeze-core/`、`freeze-pt-de/`（freeze baseline 工作区）、`build-copy/`（run.py/gates.py 重建副本）、`tmp/`
