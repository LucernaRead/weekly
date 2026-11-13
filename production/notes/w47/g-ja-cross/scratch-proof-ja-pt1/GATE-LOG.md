# GATE-LOG — 2026-w47-ja-pt 第一轮独立校对机械门（叶子，2026-11-11）

工作目录 `~/workspace/weekly-git`（clone，main）。只读生产目录与
`hidden_files/w47/scratch-fanout-ja/`；笔记写于
`hidden_files/w47/scratch-proof-ja-pt1/`。未改任何源码/成品，未跑
insert.py / lint --write，未 git add/commit/push/reset/stash。

开工探针（双通才动手）：`echo probe | git -C ~/workspace/weekly-git
hash-object -w --stdin` 成功（da0c4eb8…）；在
`hidden_files/w47/scratch-proof-ja-pt1/.probe` 真实写盘成功。

## 1. 身份复核
- 印刷 PDF `Lucerna-VOL4-JA-PT.pdf`：
  29,103,006 字节，
  SHA-256 `5e7542bc94e191e418fd49326676523e545aeb3eb2363d48c19c1cc6dcb33e56`
  ——与任务单/KIT 登记值一致。
- 网页 PDF `Lucerna-VOL4-JA-PT-web.pdf`：
  4,485,027 字节，
  SHA-256 `499149398ebed4848a02b2e8efcaaf9bbbbfe1c97effe651ffde8029d8a6629c`
  ——与任务单/KIT 登记值一致。
- `pdfinfo`：两 PDF 均为 8 页，1462.5 × 2025 pt，Producer pypdf。

## 2. U+2019 回归 + §1.1 grep（8 个 SVG）
- U+2019：p1–p8 逐个 0，总数 0。U+0027 直撇号：0。
- `·`：8 个 SVG 皆 0。纸色 `#fbfaf6` 每页 1×；旧 `#f7f1e2` 0×；
  禁用色（#b3a06a/#a4553a/#2c2822）0×。
- 页脚 `Página N de 8` 每页 1×（N=1..8）。
- VOL（仅 `<text>` 元）：VOL.4 共 10 处（P1×3，P2–P8 各 1）；
  VOL.5 共 3 处（P4×1，P7×2）；VOL.3 共 1 处（P4 前号注，与核心逐字节相同）。
- 刊头 `Lucerna` 196px；P1 头条 56px；P1 绿条标题 36px。
- 徽章（SVG 文本元精确计数）：P1 A2 11/B1 2/B2 1；P2 A2 15；
  P3 A2 7/B1 8；P4 B1 18；P5 B1 18；P6 B2 18；P7 A2 4/B1 4/B2 4；
  P8 A2 9/B1 22/B2 4——与核心版逐页逐级完全相同。
- 输出：`gates/u2019.txt`、`gates/s11-grep.txt`。

## 3. p8 门（tools/p8.py，tools/venv/bin/python）
- extract（pt P8 SVG，--total 150）：noted set 150/150，exit 0。
  输出：`gates/pt-p8.json`。
- compare（core P8 SVG vs pt P8 SVG，--total 150）：status CLEAN，
  missing=[]，extra_count=0，uncertain=[]，keydiff=[137, 138, 139, 140]，
  exit 0。输出：`gates/pt-p8compare.json`。
- 4 条 keydiff 逐条核对题干（E 组日文原文）与葡文答案，全部正确
  （137 Ni-no-tori 19 Nov；138 vinho novo 19 Nov；
  139 nomeações 5 Nov；140 verificar datas previstas e situação atual），
  注分别为 Ver página 2/3/5/6，与核心对照页一致。

## 4. 几何遮挡审计（tools/occlusion_audit.py）
- `tools/venv/bin/python tools/occlusion_audit.py <pt svg dir> --json gates/pt-occlusion.json`
  exit 0；自检 OK（6 类 BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 全触发，
  干净对照静默）；**0 flags**。输出：`gates/pt-occlusion.json/.log`。
- 补充浅色框溢出扫描（自写几何检查，仅作补充）：8 页唯一真溢出为
  P2 词框 `prósperos`（见 PROOF-NOTE D1）；其余 3 处候选为 ≤0.7px
  量测噪声，核心版同位置亦同。

## 5. freeze（直接 sha256 比对，8/8）
- 构建解释器：`/home/hatch/workspace/weekly-git/tools/venv/bin/python`
  （Python 3.12.3，Pillow 13.0.0），与 KIT §9 构建命令
  `tools/venv/bin/python run.py` 相同。
- 方法：`cp -a` 成品目录到 `rerun/`（仅删 cards/两 PDF/__pycache__），
  在副本内跑 `run.py`，sha256 对比 8 个 SVG。
- run.py exit 0；FLOW OVERFLOW / HEAD TOO WIDE 0 次；
  registry：TOTAL 150，by level {A2: 48, B1: 73, B2: 29}，
  by page {1: 10, 2: 18, 3: 18, 4: 18, 5: 18, 6: 18, 7: 12, 8: 38}，
  by type {completar: 50, escolha múltipla: 51, relacionar: 12,
  construção de frases: 8, verdadeiro/falso: 11, cloze: 13,
  tradução: 4, escrita: 1}，model chars 154；
  P8-keys 流末 col 3 y=2397（底 2540）。
- SVG sha256：8/8 IDENTICAL。输出：`gates/rerun-run.log`、
  `gates/sha-shipped.txt`、`gates/sha-rerun.txt`。

## 6. print/web 文字层一致
- `pdftotext` 印刷版与网页版：各 46,976 字节，`cmp` 逐字节相同。
  网页 PDF 4,485,027 字节（< 7 MB）。输出：`gates/print.txt`、`gates/web.txt`。

## 7. P8 字号（PyMuPDF，印刷 PDF p.8）
- 最小 9.975pt（162 spans，答案）≥ 9.75pt 底线；
  次小 10.35pt（79 spans，题干）——与 adjudication 一致，未动；
  其余 10.875/11.25/11.625/12.75/13.5/14.25/14.625/15.375/15.75/
  17.25/18.0/18.75/34.5pt 各若干 spans。

## 8. 全文对照与残留扫描
- 核心↔葡文 `.text.md` 全文 diff：359 行核心行 → 379 行葡文行，
  全部改动只在讲解层，日文正文/题干/选项零改动。
  输出：`gates/textdiff-core-pt.txt`。
- CJK 字符集差分（文本 + SVG）：葡文版新增 CJK 字符 0；
  被替换字符全为核心简体中文讲解层。
- 定向扫描：吉伊卡哇 0、参考答案 0、酉之市 0、提名 0、双人滑 0、
  流行语 0、劳动感谢日 0、见赏期 0；`解禁日` 11 处全为日文正文/题干/
  译注词头。`ryuuryuu` / `Chiikawa` 均按规定出现。
- 金句 8 条：空白压缩后计数 8× 恰为 2。
- 题号：文本题干 138 个独立编号 + 3 组四项合题（25–28、43–46、
  141–144），与核心版逐字相同；registry 总数 150。

## 9. 目视
- 从印刷 PDF 重渲染 8 页（pdftoppm -r 100，`render-print/p-1.png`～`p-8.png`）
  逐版目视 + 网页 P1/P8（`render-web/wp1-1.png`、`wp8-8.png`）目视：
  除 D1（P2 词框 `prósperos` 溢出）外无溢出/重叠/压页脚/豆腐块。
- P2 词框局部 2× 裁图：`gates/p2-words-crop.png`。

## 10. 缺口说明
- 任务单点名的 `hidden_files/w47/scratch-fanout-ja/FANOUT-REPORT-ja.md`
  与 `map-pt.json` 在校对时不在盘上（该目录仅含 ko agent 文件），
  未动用；221 键机制改以全文 diff + CJK 差分 + p8 compare 的结果验证。
  其余任务单所列核查要点均已执行完毕。
