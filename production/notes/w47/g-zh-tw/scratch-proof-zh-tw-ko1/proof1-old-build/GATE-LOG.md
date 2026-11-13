# Gate log — W47 zh-tw × ko, proof1（机械门，全跑，输出留档）

- 版：`production/2026-w47/2026-w47-zh-tw-ko/`（繁體中文 × 韓語读者语）
- 交付物 SHA（开工前核对，全部机械门跑完后复核未变）：
  - 印刷 `Lucerna-VOL4-KO.pdf` 16,839,317 B / `e1e1b6a2056728809b5e9ccbdbb9988c0205396dac94f46eb2523d3a8ed7cd56`
  - 网页 `Lucerna-VOL4-KO-web.pdf` 2,310,716 B / `3150f83e128f75b6614ef3149c645e596de867dd92f4454feaeeaf888124175f`
  - `2026-w47-zh-tw-ko.text.md` 53,939 B / `f5b1943de93a838bcd5fcfdd16cce0cafbcdc89eff5e6176604ae6061e81ea99`
- 探针：开工前 `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` 成功
  （`9daeafb9864cf43055ae93beb0afd6c7d144bfa4`）；写盘前重探通过。
  目录 `scratch-proof-zh-tw-ko1/` 真实写盘通过（`.probe`、`gates/`、`baseline/` 均已写入）。

## 1. Occlusion 审计 — 0 flags ✅

- 命令：`tools/venv/bin/python tools/occlusion_audit.py production/2026-w47/2026-w47-zh-tw-ko/svg`
- 输出（`gates/occlusion.log`）：
  `selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent`
  `production/2026-w47/2026-w47-zh-tw-ko/svg: 0 flags`

## 2. P8 extract + compare — 150/150，CLEAN ✅

- extract：`tools/venv/bin/python tools/p8.py extract --p8 …/svg/p8-test.svg --total 150`
  → `noted set = 150 of 150`（`gates/p8-extract.log`）
- compare：`tools/venv/bin/python tools/p8.py compare --core-p8 production/2026-w47/core-zh-tw/svg/p8-test.svg --edition-p8 …/svg/p8-test.svg --total 150`
  → `core 150 noted / edition 150 noted / status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[]`
  （`gates/p8-compare.log`；注：首次误用 `--core/--edition` 触发了 argparse 的歧义选项报错，已按 `--help` 改用 `--core-p8/--edition-p8`）
- 人工另逐题核对 Q1–Q150 题面↔原文↔键，全部一致（见 PROOF-NOTE）。

## 3. Freeze — baseline 8/8，diff 已裁定 ✅

- baseline（正确调用，以本版自有 SVG 为参照）：
  `tools/venv/bin/python tools/freeze.py baseline --build production/2026-w47/2026-w47-zh-tw-ko --core-svg production/2026-w47/2026-w47-zh-tw-ko/svg --out scratch-proof-zh-tw-ko1/baseline`
  → `baseline: 8/8 SVGs byte-identical`，8 页逐一 OK；
  `core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)`（`gates/freeze-baseline.log`）
- baseline（误调一次，留档）：首次把 `--core-svg` 指成核心目录，得 `0/8`——属调用错误，
  因 fan-out 版的韩语层与英文核心本就不同；纠正后 8/8。另有一次服务重启中断，
  中断后只单次重跑，未硬锤。
- diff：`tools/venv/bin/python tools/freeze.py diff --core-svg production/2026-w47/core-zh-tw/svg --edition-svg …/svg --json gates/freeze-diff.json`
  - 逐页增/删：p1 +27/−28、p2 +36/−40、p3 +44/−49、p4 +39/−42、p5 +54/−47、p6 +31/−33、p7 +354/−121、p8 +189/−188
  - 新增 CJK 共 4,716 字，全部为韩文音节 + 家具标题/被注词汇/继承串；
    删除含汉字的串全部为双语家具（中文标题 + 英文注 → 中文 + 韩文）或含引词的英文答案注，
    外加核心已修复的「本週日」串（对照出 D1）与 BABYMONSTER 行（对照出 D2）。
    无简体字、无意外新增中文（`gates/freeze-diff.json`、`gates/freeze-diff.log`）。
- `checks.py`（本版自带）：`CHECKS PASS`——8 条金句各恰出现 2 次、SIMP_ONLY_HITS []、
  P4 bars [90.0, 450.0, 900.0]、P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43]。

## 4. 印/网文字层比对 ✅

- `pdftotext`：印刷 50,188 字节 / 网页 50,190 字节（`gates/print.txt`、`gates/web.txt`）。
- 字符多重集差：印刷独有 0、网页独有 2——仅 1 个换行 `\n` + 1 个空格，空白伪影，无字符缺失。
- 网页 PDF：8 页，1462.5 × 2025 pt，< 7 MB；P5 渲染抽查确认与印刷版同源同内容。

## 5. P8 最小字号 ✅

- PyMuPDF（tools/venv）：印刷与网页 PDF 的 P8 最小字号均为 **9.75pt**（最大 34.5pt），恰为 SOP §1.1 下限。
- P8 题干 13.8px = 10.35pt（核心既定裁决）；写作范文 142 字（120–180 区间内，已数过）。

## 6. 弯引号全扫 ✅

- text.md：U+201C 0、U+201D 0、U+2019 0、U+2018 0；ASCII 双引号 0；ASCII 单引号 1 处
  （text.md:670「Kanahei's Little Animals」，专名原名，正确）。
- 8 个 SVG：U+201C 0、U+2019 0（逐文件 grep）；每文件仅 1 行含 `"`，为 XML 声明行，非正文。

## 7. 其余核查

- VOL：VOL.4 全版；P7 的 VOL.3×2（延期披露所指上期）、VOL.5×1（下期预告）均正确；
  与核心 SVG 的 VOL 分布逐页一致。
- ABSTRACT.txt：单行 285 字、0 个 ASCII 双引号、韩语、含刊名/目标语/A2–B2/150题与真实主题。
- 8 张渲染卡片（`cards/p1-front.png` … `p8-test.png`）逐版目视：无溢出、无重叠、无压页脚；
  P3 栏顶「多年。」为跨栏续行、P5 跨栏残行均为正常报纸排版；P7 栏 3 与预告带距页脚线有余量（同 KIT 实测）。
- 外部事实抽查：主灯秀「12場」用 2026-11-11 官方时刻核实无误
  （每日 17:30–23:00，每整点/半点一次 → 12 档；22:00 为最后一场有声版，不影响计数）。
- 机械门跑完后复核：三交付物 SHA 与开工前一致，未改动任何源文件。

## 结论

机械门 6 项全绿；内容复校发现 8 项缺陷（PROOF-NOTE.md：D1、D2 高；M1、M2 中；
M3、M4 低；M5 极微），本版按 SOP §8 不可定稿，需重扩 + 重渲染 + 从头再复校一轮。
