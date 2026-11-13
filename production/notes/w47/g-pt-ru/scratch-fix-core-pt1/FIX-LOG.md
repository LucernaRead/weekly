# FIX-LOG — 2026-W47 core-pt fix1（重开修复 D1/D2/D3 + D7）

修复员：core-fix（2026-11-11）。工作目录：`~/workspace/weekly-git/production/2026-w47/core-pt/`；
scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-core-pt1/`。
探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9…` RC=0；
scratch 写 `probe.txt` 成功。TMPDIR 全程指向 scratch 下 `tmp/`，系统 /tmp 未作输出
（一次误写 `/tmp/nonexistent` 已随手删除，见 §7）。
正典 creambox：`hidden_files/w47/tools/creambox.py`，md5 `ee7a55d8b2057cf4ad42a97bb1197383` ✓。

## §0 版身份核对（磁盘为准，修复前）

| 文件 | 修复前字节数 | 修复前 SHA-256 | 修复后字节数 | 修复后 SHA-256 |
|---|---|---|---|---|
| `A-Lucerna-VOL4.pdf`（印） | 25,311,626 | `f1ca8a2a65c2d10c4b989ba86613f6847166fbc01f6dfb4f80e86ba9b5353cab` | 25,311,644 | `98f44af82f82df7c7fec1014fff7098d0448bf775b2aeda484f2e69233235181` |
| `A-Lucerna-VOL4-web.pdf`（网） | 1,571,251 | `520bebfd720e44649869c2a7a38c13be6ec19020bc4fe5e71412c29c851ecb4b` | 1,608,359 | `d1d26cd70823e83e6165268b055b481981cd5cc3bdcffaec40042f7bf28a521f` |
| `2026-w47-pt-zh-cn.text.md` | 36,876 | `9dd550b6d7d19703ce6643357e9aad3f5367dfc40379bd41d56db999fd36afbe` | 36,876（未动） | 同左 |

- KIT 核对：印 PDF 字节数与 KIT §6 一致（25,311,626）；网 PDF 磁盘 1,571,251 与 KIT 所记
  1,571,215（§6）/ 1,571,245（第 3 轮）均差 36/6 字节——KIT 所记网 PDF 尺寸已 stale，
  本次按磁盘实测更新。文案、题键、字数：修复前后一字未动（text.md SHA 不变）。
- 本次收到的 follow-up 两则均已并入：D1 量按墨底口径更正为 +38；新增 D7。

## §1 改了哪几行（旧值 → 新值；文案不动）

| # | 文件 | 旧值 | 新值 | 说明 |
|---|---|---|---|---|
| 1 | `content12.py:131` | `p.rect(bx, 1874, CW, 436, fill=BOX)` | `p.rect(bx, 1874, CW, 474, fill=BOX)` | D1 框高 +38，框底 2310→2348 |
| 2 | `content12.py:144` | `qy = 2312` | `qy = 2350` | D1 框下 quiz 区随动 +38（分隔线/标题/流同移，2px 间隙不变） |
| 3 | `content34.py:40` | P3 日程框 `sh = 62 + sum(...) + 32` | `+ 58` | D2 框高 +26，框底 525→551；框下 E VOCÊ/PALAVRAS 框随 sh 下移 |
| 4 | `content56.py:132` | `p.rect(bx, 200, CW, 640, fill=BOX)` | `p.rect(bx, 200, CW, 654, fill=BOX)` | D3 框高 +14，框底 840→854；下框顶 866 不动 |
| 5 | `bslib4.py:Flow.para` | 无 `max_w` 参数 | 新增可选 `max_w=None`（默认栏宽，行为不变） | D7 重排用：范文段 wrap 宽收窄 |
| 6 | `content8.py` | `f.para("Texto modelo: " + MODELO, 15, lh=1.3, split=False)` | 同上 + `max_w=395` | D7：范文重排，字号 15、88 词、文案不动 |

- 中途自查纠错：第一次 edit 曾误删 `bx = COLX[3]` 一行，致 run.py 报 `NameError`；
  当即补回，未重建、无残留。本次 6 处以外无任何源文件改动。

## §2 测量依据（定量前的实测）

- **D1 量口径辨析**：pt-de 基线 +17.6px；pt-es 墨迹行 2311–2342（墨底 +33px）。
  本人复测 core 卡片：末行自身墨迹行 2313–2332（`g` 降部尾），墨底 2332，即框底外 +22px；
  pt-es 的 2311–2342 是扫描带（基线±40）并入了 quiz 分隔线（y=2312，整行 423 暗像素）
  与 quiz 标题字顶（~2330 起，基线 2348），非末行自身墨底。PIL 字体度量佐证：
  Newsreader 20px `em Brasília. (Página 4)` 墨底 = 基线 +5.0px（2332.6）。
  无论按 +22（真墨底）还是 +33（pt-es 口径），+38 均满足墨底 clearance ≥+5px：
  2348−2332 = +16（真墨底）；2348−2342 = +6（pt-es 口径）。
- **D2**：墨迹行 526–540，墨底 540（无降部字母，墨底 = 基线 −0.6）；框底 525 → +15px；
  +26 → 框底 551，墨底 clearance +11px。
- **D3**：墨迹行 …–845，墨底 845（`g`/`p` 降部）；框底 840 → +5px；
  +14 → 框底 854，墨底 clearance +9px。
- **D7 根因**：Cairo 渲染 Newsreader 比 PIL 量宽约 +3%（单行对照：PIL 420.6px →
  Cairo 墨右缘 1876，+15.5px；其余行 +7.5…+12.5px）。贪婪 wrap 按 PIL 量宽填满
  422.5px 栏宽即溢出；只缩字号无效（重排后行仍填满）。故以 max_w=395 重排：
  最紧行 PIL 387.0px，预测渲染墨右缘 ~1841；实测见 §5。

## §3 重建与确定性

- `run.py`：RC=0，无 `FLOW OVERFLOW` / `!!`；150 题（A2 48 / B1 71 / B2 31；
  分版 10/18/18/18/18/18/12/38）；范文 88 词。
- `render.py`：8 卡片 + 印 PDF；两跑印 PDF SHA 相同
  （`98f44af8…`，25,311,644 B）——确定性已验。
- `webpdf.py`：网 PDF 1,608,359 B，文字层 44,481 字节。网 PDF 逐跑 SHA 不定
  （run1 `62cecb77…`、run2 `9ab6ba98…`、run3 `d1d26cd7…`；首异字节在二进制流深处，
  无 CreationDate/ModDate，应为 fontTools 子集化流的字节级非确定性）；文字层三跑一致。
  任务只要求印 PDF 确定性，网 PDF 以磁盘现行文件 SHA 为准（§0 表）。
  另：新网 PDF 比旧的大 37KB（1,571,251 → 1,608,359），字形子集未变，
  应为 webpdf 渲染/子集版本差异；文字层逐字相同，不影响门禁。

## §4 全部门禁（实跑结果）

| 门 | 命令 / 方法 | 结果 |
|---|---|---|
| gates_core.py | `tools/venv/bin/python gates_core.py` | **16/16 PASS**，FAILURES: none（同基线碰撞 0；页框墨迹穿越 0，最小边距 L/R/T/B = 47.0/47.9/35.0/33.0；P6 图表覆盖 0%；P7 引言 8 条各 2×；P1 头条 41 字符） |
| occlusion 审计 | `tools/occlusion_audit.py <core> --json` | 自检阳性对照 6 类全触发；**0 flags** |
| creambox 全版 | 正典 creambox.py，`svg/*.svg` | **31 框，0 真溢出**（§5；其余 BELOW-WINDOW 仅 6 处已知假阳性 +32…+42px 下块标题；inside-only desc-clear 负值 6 处均为已知误报：中文行/“2027.”无降部字母，PIL 墨底 = 基线 −1px） |
| p8 extract | `tools/p8.py extract --total 150` | **150/150** |
| p8 compare | `tools/p8.py compare --core-dir <core> --edition-dir <core> --target pt --total 150` | **CLEAN**，missing=[]，keydiff=[] |
| freeze baseline | `tools/freeze.py baseline --build . --core-svg svg --out <scratch>/freeze-fix1` | **8/8 SVGs byte-identical**，core 完整性 8 文件重哈希无改动 |
| freeze diff | `tools/freeze.py diff --core-svg svg --edition-svg svg` | +0/−0，新增 CJK 0 |
| freeze_direct | （任务原列） | **无此子命令**：`tools/freeze.py` 仅 baseline/diff（已核 `--help`/源码）；以 baseline 8/8 + diff 自比为 freeze 证据，不拦停 |
| keycheck | 印 PDF RESPOSTAS 与 text.md 逐项比对 | **150/150**：149 项逐字一致；Q150 仅 ✓ 标记提取 artifact（`print-p8.txt:578` 有 `150. ✓ 范文见本版 H 区（88 词）`，与 pt-de 同类 artifact） |
| boxtitle PIL 实测 | SVG 标题 PIL 墨框 + PNG 渲染墨迹，31 框逐个 | **31/31 在框内**：PIL 最小余量 +20.5px；PNG 渲染最小余量 **+13px**（P2 gloss 框），0 溢出 |
| 印/网文字层比对 | pdftotext 两版 | 各 44,481 字节、7,263 词，**词多重集差 0**；8 页，1462.5×2025pt |
| P8 最小字号 | PyMuPDF span，全版 | **10.12pt**（全版最小亦为 10.12pt，仅在 P8），高于 SOP §1.1 下限 9.75pt |
| 弯引号扫描 | 印/网 pdftotext | U+201C/U+201D 各 **3**（P7 gloss 1 对 + E139/E140 两对，印/网一致）；U+2019 **0**；«» 各 40 |

## §5 回归实测（PIL 真墨，逐值）

| 缺陷 | 末行 | 修复前墨底 / 框底 | 修复后框底 | 修复后墨底 | **墨底 clearance** | creambox（基线口径） | 2× 裁切目视 |
|---|---|---|---|---|---|---|---|
| D1 | `em Brasília. (Página 4)`（20px，基线 2327.6） | 2332 / 2310（+22） | 2348 | 2332（墨迹行 2313–2332；2333–2348 无墨） | **+16px** | inside-only +20.4，desc-clear +14.4 | 框内，框底下有奶油余量，quiz 线不再穿字 |
| D2 | `16h30.`（21.5px，基线 540.6） | 540 / 525（+15） | 551 | 540（墨迹行 526–540） | **+11px** | +10.4，desc-clear +3.9（该行无降部字母，0.30em allowance 为保守值；真墨 clearance +11） | 框内，E VOCÊ 框下有干净间隙 |
| D3 | `Página do Participante.`（21px，基线 840.8） | 845 / 840（+5） | 854 | 845（墨迹行 …–845，降部尾 841–845 各 4–12 暗像素） | **+9px** | +13.2，desc-clear +6.9 | 框内，降部不触边 |
| D7 | 范文 10 行（15pt） | 墨右缘 1864 / 1876，超 1862（+2/+14） | —（栏宽 422.5 不变，wrap 改 395） | 10 行墨右缘 1722–1840 | 距 1862 余量 **−22…−140px**（最紧 −22） | — | 行末距栏边有明显余白 |

## §6 三框下方元素核查（无挤压、无新重叠）

- D1：quiz 分隔线 2350（框底 2348，间隙 2px，与修前相同）；quiz 标题基线 2386；
  quiz 流末 y=2559（底线 2560，无 FLOW OVERFLOW）；P1-tv 流末 2249 不变；页脚横线 2596。
- D2：E VOCÊ 框顶 551→577（间隙 26px 不变）；PALAVRAS 框随移；P3 col3 末 1077，
  练习横线 1620——无挤压。
- D3：LER OS NÚMEROS 框顶 866 不动（间隙 26→12px）；P6 col3 末 1066 不变。
- D7：P8 练习流末 y=878.9、图末 1238.35 均与修前相同（重排仍 10 行）；图高 250 不变。
- 全版重扫：creambox 0 真溢出；occlusion 0 flags；gates 碰撞/穿越 0（见 §4）。

## §7 备注与未决

- KIT：本次更新未沿用“invisible in the render”一说（core-pt KIT 全文 grep 无此语；
  D1 在 FIX-LOG/KIT §8b 记为可见整行溢出，实测为据）。KIT §6 网 PDF 尺寸已按磁盘更新（§0）。
- `__pycache__` 与 svg/cards/PDF 不入仓（W46 core-pt 348 个已入仓文件含 0 个 svg/cards/pdf/png；
  渲染件由源码可复现）。本次 commit 只含源码 + KIT + text.md + ABSTRACT + assets。
- 误操作：一次把 webpdf 输出路径写成 `/tmp/nonexistent`（/tmp 写了 1.6MB 文件），
  已随手删除，未留残余；其余全程 TMPDIR 均在 scratch 下。
- pt 家庭其余 proof1 仍在跑：本次提交时未再收到新的核心级 follow-up；如后续有，
  协调员另派，本次修复不覆盖。

## §8 结论

D1/D2/D3/D7 四处均已修复，PIL 真墨 clearance 分别为 **+16 / +11 / +9px**（框底口径）
与 D7 最紧行距栏边 **22px**；全部门禁一次通过，无新增缺陷。三件新 SHA 见 §0 表。
本地 commit 待做（只 commit、不 push）。
