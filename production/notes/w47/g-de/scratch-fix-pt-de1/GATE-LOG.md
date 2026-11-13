# GATE-LOG — 2026-W47 pt-de fix1（D4 返修，全部门禁实跑记录）

返修员 fix1，2026-11-11。工具链：`~/workspace/weekly-git/tools/venv/bin/python`
（Python 3.12.3 / Pillow 13.0.0 / FreeType 2.14.3）；TMPDIR 全程指向 scratch 下 `tmp/`（系统 /tmp 未用）。
正典 creambox：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py`
（md5 `ee7a55d8b2057cf4ad42a97bb1197383`，与 proof1/proof2 所用同一文件）。
所用运行命令与输出均列于下；KIT 自述数值一律不采信，只认以下本人实跑结果。
Scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-pt-de1/`
修法与结论见同目录 `FIX-LOG.md`；本文件只记门禁实跑。

## §0 身份与探针

- 探针：`ls -la /dev/null` 存在（crw-rw-rw-，1, 3）；`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` →
  `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，RC=0（与 proof1/proof2 同值）；
  scratch 写 `probe-write.txt`（`ok`）成功。
- SHA/字节核对（`sha256sum` + `stat`，开工与收工各一次）：开工印 PDF 12,938,914 B `77243c72…e6284a` ✓；
  网 PDF 1,147,629 B `56eb92d0…13b84b` ✓；text.md 37,907 B `519ab0de…d784305` ✓。与任务完全一致。
  收工：印 PDF 12,938,912 B `b8a738de…a513d`；网 PDF 1,147,636 B `2cad3d1b…83e69`；
  text.md 37,907 B `519ab0de…d784305`（不变）。
- 核心 HEAD：开工 `c0382fa7`（含 `d2b0e182` core-pt fix2 为祖先）；版目录 git 状态
  `?? production/2026-w47/2026-w47-pt-de/`（未入仓）；`core-pt/` 无修改（无 `M`）。
  本次未 commit、未 push。
- SOP：仓库根 `SOP.md` 摘要与仓库 `AGENTS.md` 已读。proof2 记录（PROOF-NOTE.md + GATE-LOG.md，
  `scratch-proof-pt-de2/`）已读；FANOUT-REPORT-pt.md（`scratch-refanout-pt/`）§1/§2/§6 +
  本版 `WEEKLY-KIT.md` 已读。

## §1 run.py + render.py + gates.py（生产目录内重建）

命令（`cd production/2026-w47/2026-w47-pt-de`，依次运行，日志在 scratch）：
`run.py`（`run.log`）、`render.py`（`render.log`）、`gates.py`（`gates.log`）。
- run.py：RC=0，`P8 saved, TOTAL exercises: 150`，`TOTAL 150`，`ALL DONE`，`OVERFLOW` 0 行。
  by level `{'A2': 48, 'B1': 71, 'B2': 31}`；by page `{1: 10, 2: 18, 3: 18, 4: 18, 5: 18, 6: 18, 7: 12, 8: 38}`；
  by type：Sätze vervollständigen 61 / Multiple Choice 49 / Wortschatz-Zuordnung 12 / Satzbildung 7 /
  Richtig oder falsch 3 / Lückentext mit Auswahl 13 / Übersetzung 4 / Schreiben 1；model words 88。
- render.py：RC=0，8 张卡片；印 PDF 12,938,912 B（修前 12,938,914 B）。
- gates.py：16 处 `[PASS]`，`FAILURES: none`，RC=0。
- textmd.py（`scratch-fanout-pt/textmd.py`，core zh-cn text.md → 本版；`textmd.log`）：
  RC=0，`changed lines: 51 of 535`（与 refanout 同数），text.md SHA 与修前逐字节一致
  （`519ab0de…`，37,907 B）。
- webpdf.py（生产目录内正典命令，`webpdf.log`）：RC=0，
  `WROTE …/A-Lucerna-VOL4-web.pdf: 1147636 bytes, 48068 text bytes`。

## §2 freeze baseline（8/8，两路）+ freeze diff

- 核心 freeze（`--build` 真核心 core-pt，`--core-svg` 核心 svg）：
  `tools/freeze.py baseline --build production/2026-w47/core-pt --core-svg production/2026-w47/core-pt/svg --out <scratch>/freeze-core`
  → `freeze-core.log`：`baseline: 8/8 SVGs byte-identical`，核心哈希与 proof2 一致
  （bd87a867…a7b7a661，p8 a7b7a661）；`core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)`，RC=0。
- 版 freeze：`--build` 版目录、`--core-svg` 版 svg → `freeze-ed.log`：
  `baseline: 8/8 SVGs byte-identical`，RC=0。
  字节哈希：p1 **6ced52ce**（修前 f988db96，唯一改变页）、p2 613f558b、p3 c33752e6、
  p4 af3e206b、p5 d146ca3d、p6 dd562a7a、p7 2d53f697、p8 a4447964——p2–p8 与 proof2 修前
  基线逐字节一致。
- freeze diff（core vs edition，`freeze-diff.log` / `freeze-diff.json`）：RC=0；
  每页 +26…+196 / −22…−752 串；新增 CJK 共 9 个，全部为 U+3000 家具分隔符（P1: 2，其余每页 1）。

## §3 occlusion 审计 — 0 标记（附盲区说明）

命令：`tools/venv/bin/python tools/occlusion_audit.py production/2026-w47/2026-w47-pt-de/svg --json <scratch>/occlusion.json`
输出：`production/2026-w47/2026-w47-pt-de/svg: 0 flags`，RC=0。
（工具另打印一行自检阳性对照通过——为工具内置输出，非 `--selftest` 调用；本次未传 `--selftest`。）
**盲区**：同 proof2 所述，BOXTITLE 检查只看带描边或 fill `#2c2822` 的矩形，
无描边奶油框（`fill="#f0eee5"`）根本不在检查之列——D4 因此未被审计发现。
本次验收不依赖 occlusion，改以 §4 的 boxtitle 真墨 + PDF 像素双法复测。

## §4 框标题横向实测 — D4 已修复，E1/E2 原位

1. 修前基线（`boxtitle-ink-pre.log`，与 proof2 逐值一致）：
   NESTA 墨迹右缘 1863.5（−1.5）；EM POUCAS +0.5；A SEMANA EM NÚMEROS +1.5；OVERFLOW 1 处。
2. 修前宽度探针（`width_probe.py`，PIL 真墨）：(a) `Diese Ausgabe` 1826.5（+35.5）；
   (b) 23pt 1846.5（+15.5）；(c) 左移 8 1855.5（+6.5）。选用 (a)。
3. 修后 `boxtitle_core.py`（PIL advance，`boxtitle.log`）：
   NESTA `title_w=364.6 right=1826.1 clear=+35.9`；OVERFLOW 0 处。
4. 修后本人 PIL 真墨水实测（`boxtitle_ink.py`，`boxtitle-ink.log`）：31 框标题，
   OVERFLOW 0 处。NESTA 墨迹右缘 **1826.5，clear +35.5**；
   最紧其余：EM POUCAS +0.5（墨迹 1861.5）、A SEMANA EM NÚMEROS +1.5（墨迹 1410.0）、
   P2 `Palmeiras × Flamengo, às` +22.5、P4 HINWEIS 框 +24.5、P7 ERROS COMUNS +28.5。
5. 交付印 PDF 像素实测（`pixel_boxtitle_pdf.py` 200dpi，`pixel-boxtitle-pdf.log`）：
   NESTA 墨迹右缘 **1826.9，clear +34.6**；EM POUCAS 1862.4（与修前同值）；
   A SEMANA EM NÚMEROS 1408.3（clear +2.9）；A SEMANA, DIA A DIA 1731.4（+130.1）。
6. 交付印 PDF 像素复核（`pixel_compare.py` 96dpi + 卡片对照，`pixel-compare.log`）：
   印 PDF：NESTA 墨迹 1827（clear +34）；卡片：1824（clear +37）——卡片与 PDF 现一致
   （修前卡片不溢出、PDF 溢出，渲染器间约 5 单位差已不构成问题）；EM POUCAS 印 1862 /
   卡片 1858（修前同口径）。
7. 目视：300dpi 原生裁图 `visual/crop-p1-nesta-pdf300.png`——`Diese Ausgabe` 末字 `e`
   完整在奶油框内，右端距框缘约 35 单位；`visual/crop-p1-poucas-pdf300.png`——
   末字 `E` 完整、右缘贴框边（与修前一致）。

## §5 正典 creambox 全版扫描 + diag — 31 框；D1/D2/D3 已修复、无回归

命令：正典 `creambox.py svg/*.svg`（`creambox.log`）+ `creambox_diag.py svg/*.svg`
（`creambox-diag.log`），RC 均为 0。
（注：首版误传目录参数得 IsADirectoryError，已纠正为 `svg/*.svg` 展开重跑；两日志均为重跑版。）
- 31 框 OWN 真墨余量全部为正，最小 **+2.1**（P2 `Palmeiras–Flamengo-Duell`，墨底 1765.9，框底 1768.0）。
- D1：P1 闪讯框（y=1874，bottom=2348.0）末行 `em Brasília. (Página 4)` 基线 2327.6，
  墨底 2332.6，墨余 **+15.4**。修复存活 ✓。
- D2：P3 日程框（y=200，bottom=551.0）末行 `16h30.` 基线 540.6，墨底 540.9，墨余 **+10.1** ✓。
- D3：P6 时间线框（y=200，bottom=854.0）末行 `Página do Participante.` 基线 840.8，
  墨底 846.0，墨余 **+8.0** ✓。
- 5 处 below-window 负 clearance（−32.0 ×1、−37.0 ×2、−42.0 ×2）均为已知假阳性：
  下块标题/段落（P1 `AGORA VOCÊ…` +37.0、P2 `Atenção:…` +32.0、P3 `UM DIA, DOIS SENTIDOS` +37.0、
  P6 `EXERCÍCIOS　SEITE 6 ÜBUNGEN` +42.0 ×2），creambox-diag 判 owner-rect=NONE，与修前同。
- 6 处 inside-only desc-clear 负值（−0.3…−1.1）均为误报（`creambox.log:99,156,191,228,237,335`，
  与修前同行）：diag 真墨复测墨迹底 ≈ 基线 +0.2–0.5（无降部字母），墨余 +4.8–5.4，无漫出。
- P7-TOOLBOX 汇总（`creambox.log:361`）：3 框，min inside clearance +5.1，min desc-clear −0.9；
  diag 真墨余量：ERROS +24.6、A PALAVRA +4.8、CARTAS +5.9。

## §6 p8 / keycheck / sweep / gloss

- `tools/p8.py extract --p8 svg/p8-avaliacao.svg --total 150`：`noted set = 150 of 150`，RC=0（`p8-extract.json`）。
- `tools/p8.py compare --core-p8 core-pt/svg/p8-avaliacao.svg --edition-p8 svg/p8-avaliacao.svg --total 150`：
  `status CLEAN, total 150, core 150, edition 150, keydiff [137, 138], missing []`，RC=0（`p8-compare.json`）。
- keycheck（`keycheck.log`，`keycheck-150.json` 写在本 scratch 内——脚本按自身所在目录写出，
  本次用的 scratch 副本，故未覆盖 refanout 的同名文件）：`REG entries: 150; p8extract keys: 150; exact match: 149/150`；
  唯一 MISMATCH：`n=150 page=8 type=Schreiben: key='(offene Aufgabe — Mustertext unten)' extracted='✓'`（预期）。RC=0。
- sweep（`sweep.log`）：box-vs-hline flags 0；bridges found 20；bridge orphans **2**；
  bridge widows **0**；RC=0。2 个 orphans 均为 `Ergänzen Sie mit den Wörtern aus dem Kasten.`
  （content34.py:85、content56.py:79），候选坐标 P3/P5 行 1 `(88.0, 2564.45)`、行 2 `Kasten. (538.5, 1696.5)`——
  与修前备份 SVG 坐标逐字节相同（proof1 O4，KIT 已注明，核心流式排版行为）。
- gloss（`gloss.log`）：P4 gloss 框 rect#0 x=989.0 y=270.48 w=422.5 h=175.4 bottom=445.88，
  4 行，末行 `pausa die Pause · a taça Pokal.` 右余 +101.5、底余 +42.7；
  `GLOSS VERDICT: lines=4 last-line right clear +101.5 last-line bottom clear +42.7 overflow=no`。
  渲染 `o título Titel`（第 3 行 `decisão das Finale · o título Titel · a`）。D5 完好。

## §7 印/网文字层、字号、孤儿标点、D5 字体

- 网 PDF scratch 重渲（`web-rerender.pdf`，`webpdf-scratch.log`）：1,147,639 B（生产网 PDF 1,147,636 B），
  SHA 不同（重渲 `be50b91a…` vs 交付 `2cad3d1b…`——网 PDF SHA 逐次浮动，为任务预告的预期现象）；
  文字层逐页与交付网 PDF 一致（8/8 页，见下）。交付网 PDF 未被 scratch 文件覆盖（生产网 PDF
  由 §1 的正典 `webpdf.py` 原地命令生成，收工 SHA 仍为 `2cad3d1b…`）。
- `pdftotext -layout` 印 vs 生产网：逐字节一致，111,358 B（修前 111,362 B，差 4 字节为标题
  删去 `In ` 的文本所致；`print.txt` / `web.txt`，cmp 通过）。
  fitz 逐页比对（`text_compare.py`）：8/8 页 print-bytes == web-bytes
  （5366/4598/4280/4919/4599/4536/5215/13489；P1 5370→5366 为标题少一词所致）。
  对 scratch 重渲网 PDF 同为 8/8 一致。
- check_final（`check-final.log`）：`pages print=8 web=8`；`words print=8435 web=8435 multiset-diff=0`
  （修前 8,436；差 1 为标题删去的 `In` 一词）；P8 answer-region span sizes [9.75, 10.5, 14.625, 18.75]，min 9.75。
- minfont（`minfont.log`）：`P8 min effective font size = 9.75 pt (n=380)`；`below 9.75pt: 0`。
- 斜体 span（fitz）：印 1 = 网 1，文本同为 `« consciência »`（生产网与 scratch 网皆然）。
- 孤儿标点（`orphan_scan.py`，`orphan.log`）：SVG 全部 `<text>` 行首扫描（1,637 行）——
  以 `, . ; : ! ? » ) ] }` 开头或仅为标点的行 **0** 条。
- text.md：按行迭代 534 行（KIT 附录称 535 行；refanout `de-gates.json` 亦为 534——计数口径差，非缺陷）；
  CJK 扫描：除 U+3000 分隔符与 P1 `<title>` 元数据外为 0（沿用 proof2 口径，本次未重扫——
  text.md 与修前逐字节一致）。

## §8 check_s11 / verify_ed（pt 适配版，见 FIX-LOG §8 说明）

pt 系无此二脚本的现成版本（proof1/proof2 scratch 均无；现存副本均为 en 系，
硬编码 core-en/en slug/en 内容检查，无法在 pt-de 上运行）。本次在自家 scratch 写了
pt 适配版（en 原版未动），按 `de` 运行：
- `check_s11_pt.py`（`check-s11.log`）：RC=0，`ALL §1.1/P8 CHECKS PASS`。
  色集 core 21 = edition 21，extra/missing 均为 none；徽章色 A2/B1/B2 齐全；
  P8 最小 SVG 字号 13.0 单位（= 9.75pt）；P8 芯片数/色与核心一致（35：B1 24 / A2 8 / B2 3）；
  题号文本 113–119 + 145–149 与 `120.` 齐全；`ESCREVA VOCÊ` 在位。
  4 处芯片 y 位移（同 x、同色）为德语排版流所致，P8 SVG 与修前基线逐字节一致（a4447964），
  属修前既有，非本次改动所致。
- `verify_ed_pt.py`（`verify-ed.log`）：RC=0，`ALL pt-de fix1 VERIFICATIONS PASS`（23/23）。
  含：D4 源两处 + SVG + PIL 真墨（1826.5 ≤1858）+ PDF 像素 200dpi（1826.9 ≤1858）；
  E1 +0.5、E2 +1.5 均原位；D1/D2/D3 源码行（474 / +58 / 654）在位 + creambox 实测
  （+15.4 / +10.1 / +8.0）；Q137/138 德语键逐字一致、Q150 `✓`；text.md SHA 不变；
  两 PDF 各 8 页。

## §9 registry 重 dump（pt 系等价物）

pt 系 run.py 不写 `registry.json`（核实：core-pt/pt-de 均无此文件，run.py/bslib4.py 内无
`registry.json` 引用；该文件只存在于 en 系版本）。本次重 dump 的 pt 系等价物：
- `p8-extract.json`（150 键登记，150/150）；
- `keycheck-150.json`（REG 150 × 提取 150，149/150）；
- `de-gates.json`（本 scratch 内全部门禁汇总，见 FIX-LOG §7 总表）；
- `de-textdiff.json` / `de-p8size.json`（check_final 写出：multiset diff 0 / P8 min 9.75pt）。

## §10 目视（印 PDF 渲染，130dpi，`visual/p-1.png`…`p-8.png` + 300dpi 裁图）

- P1：NESTA 标题 `Diese Ausgabe` 收在奶油框内，距右缘约 35 单位；D1 闪讯框末行在框内；
  EM POUCAS 末字 `E` 完整贴框边（E1 原位）；其余刊头、头条、数字框、日程框、quiz 均干净。
- P2：四格日程框、`Atenção:` 注、练习 11–28 干净；中部留白为版式固有（与修前同）。
- P3：D2 日程框末行 `16h30.` 在框内；`Kasten.` 孤字 + `B AS PALAVRAS DO TEXTO` 栏目标题落栏底（O4，既有）。
- P4：gloss 框 `o título Titel` 4 行在框内；赛程表、注、练习 A–D 干净；`B AS PALAVRAS` 栏目标题落栏底（O4，既有）。
- P5：Q73 题干 `Depois da prova, começa a ___.` 与 P5 正文原句一致；照片+出处干净；
  `Kasten.` 孤字（O4）；中部留白为版式固有。
- P6：D3 时间线框 `JAN. 2027 … Página do Participante.` 在框内；图表柱 10 天 : 5 天 = 2:1；
  D 节桥接 `Kasten: prazo · dia útil · coerência · chute` 同栏连续、完好。
- P7：三栏语法、ERROS COMUNS、A PALAVRA、CARTAS、Os Lusíadas 图、FRASES DA SEMANA（8 句，
  含 `(wörtlich aus dieser Ausgabe)`）、VOL.5 预告栏均干净；末引言行距预告栏有余量。
- P8：A–H 节 113–150 齐全；RESPOSTAS 键（含 `150. ✓ Siehe den Mustertext… (88 Wörter)`）干净；
  Mané Garrincha 照片+出处干净；无重叠可见。
- 目视新缺陷：0。

## 附：输出文件（本 scratch 目录）

- `FIX-LOG.md`（修法 + 修后 SHA + 门禁总表）、`GATE-LOG.md`（本文件）
- `de-gates.json`（全部门禁汇总）、`keycheck-150.json`、`p8-extract.json`、`p8-compare.json`、
  `freeze-diff.json`、`de-textdiff.json`、`de-p8size.json`、`de-textmd-diff.json`
- `run.log`、`gates.log`、`render.log`、`webpdf.log`、`webpdf-scratch.log`、`textmd.log`、
  `freeze-core.log`、`freeze-ed.log`、`freeze-diff.log`、`occlusion.log` + `occlusion.json`、
  `p8-extract.log` + `p8-compare.log`、`creambox.log`、`creambox-diag.log`、`boxtitle.log`、
  `boxtitle-ink.log` + `boxtitle-ink-pre.log` + `boxtitle_ink.py`、`keycheck.log`、`sweep.log`、
  `print.txt`、`web.txt`、`minfont.log`、`check-final.log`、`gloss.log`、`orphan.log`、
  `pixel-boxtitle-pdf.log`、`pixel-compare.log`、`check-s11.log`、`verify-ed.log`
- `width_probe.py`、`pixel_boxtitle_pdf.py`、`pixel_compare.py`、`orphan_scan.py`、`visual.py`、
  `check_s11_pt.py`、`verify_ed_pt.py`、`text_compare.py`
- `web-rerender.pdf`（scratch 重渲网 PDF；交付网 PDF 未动）
- `visual/`（`p-1.png`…`p-8.png`、`crop-p1-nesta-pdf300.png`、`crop-p1-poucas-pdf300.png`）
- `freeze-core/`、`freeze-pt-de/`（freeze baseline 工作区）
- `probe-write.txt`、`tmp/`
