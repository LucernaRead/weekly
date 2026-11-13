探针：`git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，RC=0；scratch 真实写文件 `probe.txt`（`fix-probe-20261111-210747`）OK。修前三 SHA 核对全对（印 14,180,887 B `f74bd657…57c3fd`；网 1,441,225 B `c35f390b…57d1f5`；text 67,687 B `d1b6ddb1…361e2`）。新三 SHA：印 14,180,929 B `af980e26fcb124773e0e3a5824e3ff742e6a72f8da50c8e53ab017418adf6200`；网 1,441,248 B `3e10d785bd1eab5318ef175a52bdebef89649622d1a7f53ea891b54b4f652cc9`；text 67,752 B `8a49ce37cc7df3ba92569243cd28b0286bee6651547f526c8cacdf112c5c895c`。D-1 修后 5 处实测：P6 NOTE gloss（7 行入盒）、Q100 注（text.md:763）、Q144 注（text.md:987）、P8 key 100（单行，列右余 77.9 px）、P8 key 144（单行，列右余 112.8 px）；旧形 «налоговая ставка» 在 SVG 平文 + text.md + 网 PDF 文字层全版 0 次。门禁：重建版与生产拷回后各跑一次 gates.py，均为 20/20 全绿（GATES ALL PASS）；freeze baseline 8/8，core 未动。未 commit、未 push。

# FIX-LOG — 2026-W47 it-ru D-1 (`scaglione` 误译) 修复


工作日期：2026-11-11。Scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-it-ru1/`（TMPDIR 全程指向其下 `tmp/`；系统 /tmp 未用于任何工作文件）。

## 0. 缺陷（proof2 (b) 唯一缺陷，见 `scratch-proof2-it-ru1/PROOF-NOTE.md` D-1）
- `scaglione`（税级/税档）被误译为 «налоговая ставка»（税率）。核心中文 `税级` 正确，英/德/法/西/葡/荷/日/韩 8 语全部正确，唯独俄语错。
- P6 正文自证：「第二档 Irpef 从 5 万扩到 5.5 万欧元」——档是收入区间，33% 才是税率；Q144 题干自相矛盾：题干定义 `un livello di reddito`（收入档位），答案注却写「налоговая ставка」。
- 3 个 `translations.py` 条目 → 5 处呈现：L805 P6 NOTE gloss（text.md:663）；L1782 Q100 注 + P8 key 100（text.md:763、1217）；L2080 Q144 注 + P8 key 144（text.md:987、1305）。

## 1. 候选词核实（修前）
首选 «ступень налоговой шкалы» 经核实为标准俄语「税级/税档」说法：
- 英俄词典（translate.academic.ru）明确给出：tax bracket — «ступень налоговой шкалы»；bracket of tax — «ступень налоговой шкалы в прогрессивном налогообложении»；income bracket — «ступень шкалы дохода»。
- 俄语税务用法一致：俄罗斯累进 НДФЛ 为 «пятиступенчатая шкала»（五档税级），每个 «ступень» 对应自己的 «налоговая ставка»（税率）—— ставка 是税率，不可能是档位（scienceforum.ru 论文：«Каждой ступени соответствует своя фиксированная налоговая ставка»）。
- «налоговая ставка» = 税率，是错的，绝无保留。5 处全 fit（见 §3），直接采用首选，无需 fallback（«ступень шкалы» / «налоговый разряд» 未启用）。

## 2. 源码修改（`scratch-fanout-it/translations.py`，以该文件为准）
- 改前备份：`translations.py.orig`（本 scratch 内）。diff = 恰好 3 行：
  - L805：`lo scaglione, налоговая ставка ·` → `lo scaglione, ступень налоговой шкалы ·`
  - L1782：`"ru": "scaglione = налоговая ставка"` → `"ru": "scaglione = ступень налоговой шкалы"`
  - L2080：`"ru": "scaglione = налоговая ставка, a"` → `"ru": "scaglione = ступень налоговой шкалы, a"`
- 改后 grep：旧形 0 处；其余 8 语 `scaglione` 译法未动（tax bracket / Steuerstufe / tranche fiscale / tramo fiscal / escalão fiscal / belastingschijf / 税率区分 / 세율 구간 全在）。

## 3. 宽度实测（修前，`measure_widths.py`，用本版 ru svglib `wrap()` + PIL Noto Serif）
- P8 key 100：`100. scaglione — scaglione = ступень налоговой шкалы`，serif 13 / 422.5 px 列，wrap = 1 行，单行宽 344.7 px（PIL 复核 353.0 px）；节点实测最末 run «шкалы» x=1287.4，右缘 1333.6，列右 1411.5，余 77.9 px。
- P8 key 144：`144. a — scaglione = ступень налоговой шкалы, a`，wrap = 1 行，单行宽 308.6 px（PIL 复核 316.7 px）；最末 run «шкалы, a» x=1689.0，右缘 1749.2，列右 1862.0，余 112.8 px。
- P8-keys flow 增量 +0.0 px（23 px 余量不动）；P6 NOTE gloss sans 20.5 / 386.5 px：6 → 7 行（+29.7 px），P6-main 流余量 171 px，够。
- 结论：首选长形式 5 处全 fit，直接用。

## 4. 全量重建（scratch 内，生产 SVG 绝不被重建过程直接写）
- 驱动：`rebuild.py` = `scratch-fanout-it/build_edition.py` 的副本，仅改三处指向：EDROOT → 本 scratch `rebuild/`；content `OUT` 与 render `BASE` 由 `~/workspace/weekly-git/production/…` 重定向为本 scratch 绝对路径（即 proof2 事故 #15 的陷阱点——原版 rep1 仍指向生产目录，本次已改掉；重建后逐项核对，生产 SVG 在重建期间未被触碰，见 §6）。日志目录亦重定向到本 scratch `rebuild-logs/`（不写回 fan-out 目录）。`PYTHONDONTWRITEBYTECODE=1`，不向生产写 `__pycache__`（事后核查：生产 `__pycache__` 无本次新文件）。
- `rebuild.py ru` RC=0，BUILD DONE（109 s）：table pass OK（无残留 CJK）；run.py RC=0，TOTAL 150，0 FLOW OVERFLOW / HEAD TOO WIDE / NOSPACE，ALL DONE；render.py RC=0；webpdf RC=0；`.text.md` 导出 67,752 B / 150 题。
- 流终值：P6-main 1349 → 1379/1520（与预估 +30 px 一致）；P8-keys 2529/2552 不变；其余流全与修前 log 逐项相同。
- 重建物 vs 生产旧版：仅 p6/p8 SVG 不同（其余 6 个 SVG byte-identical）；cards 仅 p6/p8 不同（其余 6 张 identical）；text.md diff 恰好 5 行（663/763/987/1217/1305）；content 文件 diff 除 OUT/BASE 路径行外，恰好 3 串（content56.py:126/:229、content8.py:85）。

## 5. 修后 5 处实测（重建 PDF 96 dpi 渲染 + SVG 节点 + 文字层）
| # | 呈现 | 实测 |
|---|---|---|
| 1 | P6 NOTE gloss（text.md:663） | 渲染 `pages/fix-p6-6.png` 目视：7 行全在 NOTE 盒内，末行 «процедура.» 在盒内，盒下与图表区间距干净，无溢出、无碰撞 |
| 2 | Q100 注（text.md:763） | `100. [B2 · …] — key: scaglione (scaglione = ступень налоговой шкалы)` |
| 3 | Q144 注（text.md:987） | `144. lo scaglione — un livello di reddito del sistema fiscale (key a · scaglione = ступень налоговой шкалы, a)`——题干「收入档位」与答案注「税级」不再自相矛盾 |
| 4 | P8 key 100（text.md:1217） | 渲染 `pages/fix-p8-8.png` + crop `pages/crop-key100.png` 目视：单行完整，右缘余 77.9 px |
| 5 | P8 key 144（text.md:1305） | 渲染 + crop `pages/crop-key144.png` 目视：单行完整，右缘余 112.8 px |
- 旧形清零：SVG 平文（去标签 + 空白折叠）8 页全 0；text.md 0；网 PDF 文字层（pdftotext）0；印 PDF 文字层 0。新形：SVG 平文 p6=1、p8=2；text.md 5 处；网/印 PDF 文字层各 3 处。
- 未动项核查：P1/P2 双语盒标题 text.md:45/:205 与修前逐字节相同，p1/p2 SVG byte-identical（STRADDLE 观察项 O-1/O-2 不重判、不动）；Q140 键仍为意大利语 «Ogni cifra deve essere chiara.»（正确行为，未动）；其余 8 语译法未动（§2）。

## 6. 拷回生产（全部验门通过后）
拷回文件（仅限受影响文件，共 10 个）：
- `svg/p6-approfondimento.svg`（新 SHA `a36aa3ce1eeab8f1f30412f149dbea22b1cff0f5c499a8751a912fd518f425e2`）、`svg/p8-valutazione.svg`（`6faa486ae94a6a512e530235b78e51bba977a2596e907552c420bd134c4a4165`）——与重建物 SHA 一致；其余 6 个 SVG 经 `shipped-svg.sha256` 复核仍为旧 SHA。
- `cards/p6-approfondimento.png`、`cards/p8-valutazione.png`（改动 SVG 的渲染卡片，保持一致）。
- `La-Lucerna-VOL4-RU.pdf`、`La-Lucerna-VOL4-RU-web.pdf`、`2026-w47-it-ru.text.md`（新三 SHA 见首行）。
- `content56.py`（:126、:229）、`content8.py`（:85）——仅改 3 串，生产 OUT 路径行保留；与重建副本 diff 仅 line 6（OUT）；content12/34/7 与重建副本 diff 亦仅 OUT 行；`render.py`/`bslib4.py`/`run.py`/`svglib.py` 未动。
- `WEEKLY-KIT.md` 追加 §12 Fix round 节（新旧三 SHA + D-1 修前/修后 + 候选记录）；§6 等旧值不动。
- 生产目录本次改动文件清单（`find -newermt` 复核）：上述 10 文件，无其他文件被改动。core-it 未动（freeze baseline 复核，见 GATE-LOG）。未 commit、未 push（版目录仍为 untracked 状态，与修前一致）。

## 7. 过程记录 / 注意事项
- gates.py 副本说明：proof2 的 `gates.py` 拷到本 scratch 后重定向（EDROOT→重建目录、SCRATCH→scratch-fanout-it 以取修后 translations.py）。重建版门禁运行时其 JSON 输出（p8-extract.json / p8-compare.json / freeze-diff.json）写进了 `scratch-fanout-it/ru/`，覆盖了首轮 fan-out 的同名中间 JSON（.log 文件未动；内容为可再生的中间产物，且现与修复后版本一致）。生产版门禁改用 `gates-prod.py`，输出定向到本 scratch `ru-prod/`，未再写 fan-out 目录。
- 一次手误：某条命令中误带 `cp content56.py /tmp/nonexistent`（无意写入系统 /tmp），发现后立即删除（`rm -f /tmp/nonexistent` 已验证不存在）。TMPDIR 其余全程指向本 scratch `tmp/`。
- 一次测量口径教训：SVG 平文统计必须先折叠空白——ru svglib 把空格拆成独立 run，直接去标签会留下多重空格，使 «ступень налоговой шкалы» 匹配不到（曾误报 p6/p8 新形 0）；以去标签 + `\s+` 折叠为准（与 proof2 的 flat 方法一致）。最终生产复核：p6=1、p8=2、旧形全 0。
- 翻译表备份 `translations.py.orig` 留在本 scratch，供 diff 复核。
