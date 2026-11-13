# GATE-LOG — Lucerna Weekly 2026-W47 · nl-es re-proof（机械门自跑结果）

版：`production/2026-w47/2026-w47-nl-es/`（fix1 同步后版）。全部命令用 `tools/venv/bin/python`
（Pillow 13.0.0 / FreeType 2.14.3）或系统 `pdftotext`；输出均在
`hidden_files/w47/scratch-reproof-nl-es1/`；TMPDIR 指向该 scratch；`PYTHONDONTWRITEBYTECODE=1`。
生产目录只读：开工/收工快照逐字节一致（见 §8）。

## 0. 开工探针与三 SHA

| 检查 | 命令 / 证据 | 结果 |
|---|---|---|
| 磁盘探针 | `git -C ~/workspace/weekly-git hash-object -w /dev/null` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，rc=0 |
| scratch 写文件 | `probe.txt`（真实文件） | 成功；`df` 可用 58G |
| 印 PDF | `sha256sum De-Lucerna-VOL4-nl-es.pdf` | `e6c28566…233a8e5`，12,669,546 B，与任务一致 |
| 网 PDF | `sha256sum De-Lucerna-VOL4-nl-es-web.pdf` | `55e8489d…577ad0b`，1,616,170 B，与任务一致 |
| 文 | `sha256sum 2026-w47-nl-es.text.md` | `44fc3d5c…19d00eb`，47,649 B，与任务一致 |

## 1. fix1 源码 10 处在位核对

`bslib4.py:21` `NOTE_RIGHT = RIGHT - 10`；`content12.py:147`、`:214`、`:235`；
`content34.py:50`、`:147`；`content56.py:65`、`:153`（字号 23）、`:183`；
`content8.py:133`。字符串均未动。
**行号出入**：任务写第 5 处家具行在 `content56.py:180`，实际在 `:183`（`# fix1 … 5 of 5` 注释一致）。

## 2. run.py（scratch 副本内重跑，不动生产）

- 命令：复制生产目录到 `scratch-reproof-nl-es1/repro/`（删 svg/cards/`__pycache__`/`*.pdf`），
  `tools/venv/bin/python run.py` → `run-reproof.log`。
- 结果：**rc=0，TOTAL 150**；by page 10/18/18/18/18/18/12/38；A2 46 / B1 73 / B2 31；
  `grep -i "overflow|too wide|error|warn"` 无输出；`flow[P8-keys] ended col 3/3 y=2518 (bottom 2560)`；
  model words 81。
- 重建 8 SVG 与生产 SVG **逐字节一致**（p1–p8 全部 IDENTICAL）。

## 3. p8 门

- `tools/p8.py compare --core-dir ../production/2026-w47/core-nl --edition-dir ../production/2026-w47/2026-w47-nl-es --target nl --total 150` → `p8-compare.log`，rc=0：
  `core 150 noted / edition 150 noted / status: CLEAN missing=[] extra_count=0 uncertain=[] keydiff=[137, 138]`。
- 复核路：`p8.py compare --core-p8 …/core-nl/svg/p8-toets.svg --edition-p8 …/2026-w47-nl-es/svg/p8-toets.svg --total 150` → `p8-compare2.log`，rc=0，结果相同。
- `p8.py extract --p8 …/2026-w47-nl-es/svg/p8-toets.svg --total 150` → `p8-extract.json/log`：
  noted set = 150 of 150。
- P8 字号（交付印 PDF，PyMuPDF spans）：最小 **10.12pt**，383 spans，0 个 <10pt → `p8-fontsize.log`。
  全版最小字号：P1–P5/P7 11.62pt，P6 12.75pt，P8 10.12pt。

## 4. freeze 门

- `tools/freeze.py diff --core-svg ../production/2026-w47/core-nl/svg --edition-svg ../production/2026-w47/2026-w47-nl-es/svg --json freeze-diff.json` → `freeze-diff.log`，**rc=0**：
  p1 +26/−48，p2 +43/−36，p3 +30/−27，p4 +29/−26，p5 +39/−43，p6 +36/−30，p7 +46/−44，p8 +180/−677；
  新增 CJK **仅 U+3000 ×7**（P2–P8 各 1）。
- `tools/freeze.py baseline --build ../production/2026-w47/core-nl --core-svg ../production/2026-w47/core-nl/svg --out scratch-reproof-nl-es1/freeze-baseline` → `freeze-baseline.log`，**rc=0**：
  **8/8 SVGs byte-identical**（p1 `7edd158d…` … p8 `caffbab8…`）；core integrity：shipped core SVGs unchanged；
  build-copy 内 8 个 SVG 与 `core-nl/svg` 逐一核对一致（核心版，非本版自比）。

## 5. occlusion 审计

- `tools/occlusion_audit.py --selftest` → `occlusion-selftest.log`，rc=0：
  planted classes fired {BOXTITLE: 1, COVER: 1, EDGE: 1, FOOTER: 1, LINEX: 1, TEXTX: 1}；clean controls silent。
- `tools/occlusion_audit.py ../production/2026-w47/2026-w47-nl-es --json occlusion.json` → `occlusion.log`，**rc=0：0 flags**。
  （0 flags → 无需逐项 6× 裁切图裁定。）

## 6. 交付印 PDF 光栅边缘扫描（决定性测量）

### 6a. 600dpi（fix1 同方法：RGB max<180，最右暗像素左缘，SCALE=6.25）

- 脚本 `edge600_reproof.py` → `edge600.json/log`（逐页流式渲染，增量 JSON）。
- 9 带与 fix1 `edge-after.json` **逐值一致**：D1 1849.44、D2 P1 1856.16、D2 P2 1855.68、
  D3 P2–P6 1853.92（×5）、D3 P8 1854.08；整页（不含页脚）P1 1862.24、P2–P8 1861.92。

### 6b. 300dpi 独立交叉（灰度 <128，最右暗像素右缘）

- 脚本 `edge_scan_reproof.py` → `edge-print.json/log`：D1 1849.52、D2 P1 1856.24、D2 P2 1855.92、
  D3 家具行 1854.32、D3 P8 1854.32；整页 P1 1862.64、P2–P8 1862.32。
  与 6a 相差 0.08–0.40px，属像素取位约定差（300dpi 右缘约定 +0.24），非真实差异。
- 同方法扫核心印 PDF → `edge-core.json/log`：P1 1862.64、P2–P8 1862.32，与本版逐值相同（设计边对照）。

### 6c. P1 1862.24 成分解剖

- y50–100：刊头日期行末字（SVG x=1434.6 起锚；PIL getbbox 右 362.75 + 字距 1.7×38=64.6 → 预测 1861.95，
  光栅 1862.24，差 0.29px）。
- y400–450：hline y=420（x2=1862.0），窄带 1861.92。
- y450–600：深绿满栏条 rect y=470–588（右缘 1862.0），1862.32。
- y1500–1800 / y2100–2400：照片/奶油盒右缘 1862.0，1862.0。
- 左缘 87.68（系统性，核心亦同）。

## 7. 盒标题逐一复测

- 脚本 `boxtitle_reproof.py` → `boxtitle.json/log`。
- 定义：奶油底框（fill `#f0eee5`）内首行文字；P1–P7 共 **26 框 / 26 标题 / 0 无标题框**；P8 无奶油框。
- 光栅（交付印 PDF，300dpi，<128，标题 y 带 × 框 x 范围）：全部在框内，最小余量 **+12.58px**（D1）；
  其余 ≥ +18.34px；全表见 PROOF-NOTE 附录 A。PIL 真墨交叉验证余量全部 ≥ +16.0px。
- 全量 PIL 墨缘扫描（1,638 文本节点）：16 标记全为 LEFT+0.2（墨左 87.8，系统性）；
  RIGHT / PAGE / FOOTER 标记 0；奶油盒底容纳 0 标记。

## 8. 网/印文字层

- `pdftotext -layout` 印 → `print.txt`（106,408 B），网 → `web.txt`（106,408 B）；
  `diff` → `web-vs-print.diff`：**0 行**；raw 路 `web-vs-print-raw.diff`：**0 行**。
- 印 pdftotext 46,815 B = 网 46,815 B（与 KIT 一致）。

## 9. Delta 六处 + 150 题 + 全文

- D6/D7/D8/D10 wrap 区间复算 → `delta-reverify.log`：D6 329.5–425.5（中点 377.5）、
  D7 414.5–424.5（419.5）、D8 349.5–392.0（370.75）、D10 319.5–405.5（362.5），均连续、在内。
- D11：事实行 3/3/3/2/3=14 行，sh 重算 **638.0** = `content34.py:134`；盒下 7px 带交付印 PDF 探针 **0 暗像素**（最小灰度 249）。
- D9：Q140 三源一致（见 PROOF-NOTE §5）。
- 150 题：REG 导出（`registry.json`，重跑导出，150 条 1–150 无缺重）；
  text.md `Respuesta:` 142 + 配对 `(Respuesta x)` 8 = 150 键全解析，`答案：` 0，CJK 表意字 0，U+3000 59；
  P8 印出键 150/150；**三源逐题 0 不一致**（`keycheck*.log`；首版正则误把题干当键，已修正重算）。
- 题干 vs 核心 SVG 文本：140/150 逐字出现；余 10 项为配对项分栏（核心与本版同状）与 Q139/Q140 翻译方向源句（按设计）。
- 孤儿扫描：14 候选均为合法破折号续行/对话/分隔头，真孤儿 0；基线出页 0。
- Q150 模型文：印出 P8 81 词，与 text.md 逐字一致。
- 目视：生产 `cards/` P1–P8 逐页查看，干净（P1/P6/P8/D1/D2 重点页 + P2/P3/P4/P5/P7 全页）。

## 10. 生产零写入核对

- `snapshot-before.sha256` vs `snapshot-after.sha256`（各 42 文件）：`diff` 无输出，**生产逐字节一致**。
- `git status` 的 `2026-w47-nl-es/` 未跟踪状态为开工前即有（尚未入仓），非本人写入。
- 未 commit、未 push、未重渲染交付 web PDF；全部重建/重渲染只在 `scratch-reproof-nl-es1/repro/` 内。
