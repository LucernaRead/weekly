# GATE-LOG — W47 ja-ko proof1 机械门独立重跑记录

复校员 proof1；2026-11-11 08:22–08:31 UTC。工具：`~/workspace/weekly-git/tools/venv/bin/python`。
交付物目录（只读，未改动）：`~/workspace/weekly-git/production/2026-w47/fanout-ja/2026-w47-ja-ko/`。
重建在笔记目录内副本 `build-copy/` 进行（`*.py` + `svg/` + `assets/` 复制件），交付 SVG/PDF 未触碰。

## 探针
- PROBE1：`git hash-object -w --stdin </dev/null` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，OK。
- PROBE2：笔记目录写 `probe.txt`，OK。`df`：/home/hatch 46G 可用。全程无 EDQUOT。

## 成品核实
- print `Lucerna-VOL4-JA-KO.pdf`：28,189,461 B，sha256 `fbcfe840f569ff521fb4aed509a441b8375a01b792f329fdc0a0bda2689437bc`，8 页。
- web `Lucerna-VOL4-JA-KO-web.pdf`：4,550,459 B（< 7 MB），sha256 `d52edd4e6be8a2b3fa7c3115155e07e6cde028aa7dceaa723fea34bb365c27ac`，8 页。
  （任务所给两枚 SHA 与实测互换，见 PROOF-NOTE §0。）
- `2026-w47-ja-ko.text.md` 47,721 B；`ABSTRACT.txt` 296 B；`WEEKLY-KIT.md` 10,695 B。

## 门 1 — run.py（freeze 重建，build-copy 内）
- run1：exit 0；`FLOW OVERFLOW`/`HEAD TOO WIDE` 0 条；`TOTAL 150`；by level A2 48 / B1 73 / B2 29；
  by page 10/18/18/18/18/18/12/38；by type 빈칸 채우기 50 / 객관식 51 / 연결하기 12 / 문장 만들기 8 /
  참-거짓 11 / 빈칸 객관식 13 / 번역 4 / 작문 1。日志 `proof-run1.log`。
- run2：exit 0；`proof-run2.log`。
- freeze：`proof-sha-run1.txt` vs `proof-sha-run2.txt` diff 空 → **8/8 相同**。
- 交付比对：`proof-sha-run1.txt` vs `proof-sha-delivered.txt`（交付 SVG 实测）diff 空 →
  **交付 SVG 与重建 8/8 相同**。

## 门 2 — occlusion_audit.py（交付 SVG 目录）
- 命令：`tools/occlusion_audit.py --json proof-occlusion.json <edition>/svg`
- exit 0；日志：`selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent`
  + `<svgdir>: 0 flags`。JSON：`flag_count: 0`，`flags: []`。→ **0 flags**。
- （首次误传 8 个 SVG 路径被 argparse 拒，exit 2；按 `--help` 改传目录重跑。工具本身无问题。）

## 门 3 — p8.py
- extract：`tools/p8.py extract --p8 <edition>/svg/p8-tesuto.svg --total 150 --json proof-p8.json`，
  exit 0；`noted set = 150 of 150`，编号 1–150 连续无缺重。→ **150/150**。
- compare：`tools/p8.py compare --core-p8 <core>/svg/p8-tesuto.svg --edition-p8 <edition>/svg/p8-tesuto.svg --total 150 --json proof-p8compare.json`，
  exit 0；`status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 140]`。
  （首次漏 `--total` 被 argparse 拒，exit 2；补参重跑。）
- 注：compare 只比对键值（key token），不覆盖注文 prose；prose 已人工全核，见 PROOF-NOTE §1/§3.3。

## 门 4 — 文字层一致
- `pdftotext`（plain）：print 47,997 B、web 47,997 B，`cmp` 逐字节一致。
- `pdftotext -layout`：print 91,656 B、web 91,656 B，`cmp` 逐字节一致。
- P8 最小字号（PyMuPDF，print PDF p.8）：9.975pt；次档 10.35pt（题干）。

## 门 5 — text.md 导出一致
- 用 builder 的 `export-textmd-ko.py`（OUT 改指本目录 `reexport-text.md`）重导出：
  `wrote reexport-text.md 47721 bytes; 1330 text lines`；与交付 `2026-w47-ja-ko.text.md` diff 空 →
  **逐字节一致**。KIT“1330 行”为该脚本 text 行数；文件行 1357（含 17 空行与页眉），口径不同，非错误。

## 门 6 — 专项扫描（本轮自写探针，证据 `scan1.txt`）
- 弯引号/弯撇 U+201C/U+201D/U+2019/U+2018：8 SVG + 9 py + text.md + ABSTRACT.txt + KIT + 双 PDF 文字层 **全 0**。
- 罗马字：`Fujiryūga` / `Fujiryōga` / `Fujiryuga` / `Fujiryoga` / `Umi-no-umi` 全版 **0 处**；
  韩文 `후지류가`：P8 SVG 5 处 + text.md 5 处 + content34.py 3 处 + content7.py 1 处 + content8.py 1 处；
  `후지료가` 0 处；`우미노우미`：P8 #48 + content34.py（正确）；
  `기하라 류치`：content56.py/P8 SVG/text.md 各 1 处；`기하라 류이치` 0 处。
- 中文残留：`吉伊卡哇`/`参考答案`/`酉之市`/`提名` 0；`写`×11/`今年`×11 皆为冻结日文（写真/今年）；
  fan-out 未引入任何核心所无之汉字字符（程序核验 0 个）。
- §1.1：纸 `#fbfaf6` 1×/页、旧纸 `#f7f1e2` 0×、`·` 0×、禁金色 0×；刊头 196px；页码行 `제 N 면 / 총 8 면` 1×/页；
  VOL.4 ×10、VOL.5 ×3、VOL.3 ×1（冻结日文“前号（VOL.3）”，指上期）。
- 几何实测：P7 teaser 末基线 2438.14（墨底 ≈2444，页脚 2580）；P8 答案 4 列末基线 2514.92 / 2513.42 / 2530.35 / 2350.48
  （皆 < 2540 底线）；P8 练习流最末基线 1239.37（底线 1252）；P2 四词卡 gloss 单行基线 1752.06（框底 1768）。

## 门 7 — 目视
- print 卡 p1–p8 全读：无溢出/重叠/压页脚/豆腐块。web PDF p1、p8 渲染对照 print 卡一致，无豆腐块。
- 唯一可见版式瑕疵：P5「あなたは？」框韩语提示末行仅一个 `.`（SVG y=1530.37），见 PROOF-NOTE D3。

## 结论
- 机械门：**全部通过**（run 0 溢出、freeze 8/8、occlusion 0、p8 150/150 + CLEAN、文字层一致、text.md 导出一致）。
- 内容：**3 条缺陷**（PROOF-NOTE D1/D2/D3），须修后按 SOP §8.4 从头再做一轮全量校对。
