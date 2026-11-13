# FIX-LOG — 2026-W47 pt-en 第二轮返修（D-B1/D-B2 盒标题真墨溢出）

- 返修员：fix1（第二轮返修；与 pt-en 重建者、proof1 校对员、第一轮返修员不同人）
- 时间：2026-11-11（EST）
- 对象：`production/2026-w47/2026-w47-pt-en/`（Portuguese target × English readers）
- 依据：任务书 + `scratch-proof-pt-en2/PROOF-NOTE.md` + `GATE-LOG.md`（结论 (b)）+ SOP §8 + WEEKLY-KIT.md §9 附录
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-pt-en1/`
- 红线遵守：未改 core-pt、未碰其他版；未 commit、未 push；未跑 insert.py、lint --write。

## 0. 开工探针与先验 SHA 核对

- 探针 1：`/dev/null` 存在（crw-rw-rw-）；仓库内 `git hash-object -w /dev/null` 成功（`e69de29b…`，rc=0）。注：首次在 `~` 下直接跑因不在 git 仓库内报 `fatal: not a git repository`（rc=128）；改在 `~/workspace/weekly-git` 内重探即通——探针失败未硬锤，按任务书停等重探处理。
- 探针 2：在本 scratch 目录真实写文件成功（`probe.txt`）。
- 先验 SHA 逐字一致（开工核对）：
  - 印 `A-Lucerna-VOL4.pdf`：12,932,439 B，`782e7cb9d9109f4282667fd6dde71ab981933fa5290a9cd4882aaa49322cca6d`
  - 网 `A-Lucerna-VOL4-web.pdf`：1,139,921 B，`e02cf58cbee4cf5daac47fccc9319faf8158b6b31523ba220794f415a5e9bb61`
  - 文 `2026-w47-pt-en.text.md`：37,333 B，`513326ffa497ca2b6714c1016eadbfaa2ac3447269b782749c968022e0e118ed`

## 1. 缺陷独立复测（修前，PIL 真墨，与 proof1 逐字一致）

- 用版内 `svglib._pil` + `getbbox anchor='ls'` 自写真墨探针（`measure_candidates.py`，与 proof1 的 `boxtitle_trueink.py` 同款数学）复测修前成品：
  - D-B1：P1 `A SEMANA EM NÚMEROS　In numbers`，元素 x=1007.0 y=823.18，23pt/700；真墨右缘 **1434.0**，盒右缘 1411.5，**clear −22.5**（advance 1433.5，−22.0）。任务书称真墨 1433.0/−21.5，与 proof1（1434.0/−22.5）差 1.0/0.5；本次独立实测与 proof1 逐字一致，以实测值为准。
  - D-B2：P7 `ERROS COMUNS　Common mistakes`，元素 x=1461.5 y=242，23pt/700；真墨右缘 **1876.5**，盒右缘 1862.0，**clear −14.5**（advance 同值）。与 proof1 逐字一致。
- 源头定位（均已核对行号）：D-B1 `content12.py:43`（`f.box(...)`，标题字号取 `Flow.box` 默认 `tsize=23`）；D-B2 `content7.py:82`（`p.text(..., 23, ...)`）。

## 2. 修法选型（实测候选，`measure_candidates.py` / `measure_candidates.log`）

- 候选实测（同一 PIL 真墨口径；要求修后墨迹右缘比盒右缘至少小 4 单位）：
  - (b) 23→22pt：D-B1 clear −3.5、D-B2 +3.5——两处均不满足 ≥+4，排除。
  - (b) 23→**21pt**：D-B1 墨迹右缘 1396.0、clear **+15.5**；D-B2 墨迹右缘 1840.5、clear **+21.5**——两处均满足，且为满足门槛的最小整数档。
  - (a) 缩短英文副标题（23pt）：D-B1 `… Numbers` +3.5（不满足 ≥+4）、`… In figures` +0.5、`… Stats` +49.5（措辞改 informal）；D-B2 `… Mistakes` +96.5、`… Common errors` +17.5。均须改动正文措辞并波及 text.md（标题出自 tables_en.py SEG 键 `数字`/`常见错误`，尚有他处共用风险待查），改动面大于 (b)。
  - (c) 整体左移：D-B1 需 ≥26 单位，标题 x=1007.0、盒左缘 989.0，左移 26 将使标题起点落到盒左缘之外（981 < 989），不可行；D-B2 需 ≥19 单位，移后左内边距仅剩 3 单位，版式劣化。排除。
- 决定：两处均选 **(b) 标题字号 23→21pt**——最小改动：措辞零改动、text.md 零改动（盒标题不在 text.md 内，已 grep 核实）、其余 29 个盒标题保持 23pt 不动、冻结 CJK 增量不变。

## 3. 改动清单（源码层，共 2 处）

| # | 缺陷 | 文件 | 行 | 改法 |
|---|---|---|---|---|
| 1 | D-B1 | `content12.py` | 43–48 | `f.box("A SEMANA EM NÚMEROS　In numbers", [...])` → `..., tsize=21)`（`Flow.box` 的 `tsize` 参数；默认 23） |
| 2 | D-B2 | `content7.py` | 82 | `p.text(bx + 22, yy3 + 26, "ERROS COMUNS　Common mistakes", 23, ...)` → 字号 `21` |

- 未动 `tables_en.py` / `transform.py` / `furniture.py` / `bslib4.py`；未动 core-pt；未动其他版。
- 注：`Flow.box` 的盒高含 `tsize+10`，21pt 使 P1 数字盒总高减 2（434.0→432.0），其后 flow 上移 2 单位，由 flow 机制消化，门禁复验；P7 为手算 `eh` 矩形，盒高不变，仅标题字形缩小，基线不变。

## 4. 重建（run.py → render.py → webpdf.py → text.md 重导 → registry 重 dump）

- `run.py`：rc=0，TOTAL 150（A2 48 / B1 71 / B2 31；分版 10/18/18/18/18/18/12/38；范文 88 词）；FLOW OVERFLOW 0，HEAD TOO WIDE 0；REGISTRY STATS 重 dump 见 `run-fix2.log`（TOTAL 150，by level/page/type 与修前一致）。（注：pt 家族无 `registry.json` 成品——core-pt 与 pt-de 均无 `dump_reg.py`/`registry.json`；pt-en 版目录亦无。en 家族的 `dump_reg.py` 是 en-core 专属脚本，其输出写进 en 家族 scratch，不属 pt 版。本轮 registry 重 dump 即 run.py 的 REGISTRY STATS + p8 extract 重 dump；未新建 `registry.json` 成品，不改版目录文件清单。）
- `render.py`：rc=0（日志 `render-fix2.log`）；印刷 PDF 12,932,441 B，8 页，1462.5×2025 pt，sha256 `7e235e4591c034815ed90bcc21cef48a3b40bb1eb39bb0ebb1c8f027fbcb2e42`。
- `webpdf.py`：rc=0（日志 `webpdf-fix2.log`）；1,139,917 B，46,071 text bytes，sha256 `aad718e1efccbbcf24f4a1d6ac05fbe1bc59bf3b431037384f5645896bd7fc6c`。
- `text.md` 重导（`textmd.py`，机制表 `scratch-fanout-pt`）：rc=0，534 行，CJK 0，题号 150/150；与修前 `.text.md` diff 0 行——SHA 仍为 `513326ffa497ca2b6714c1016eadbfaa2ac3447269b782749c968022e0e118ed`（37,333 B）。
- SVG 变化：仅 p1-capa / p7-lingua 两页哈希变；其余 6 页逐字节不变（`pre-svg-sha.txt` vs 新哈希）。
- 重渲比对（仅 scratch 副本，已删）：印 PDF 重渲 SHA 与交付逐字相同（`7e235e45…`）；网 PDF 重渲文字层与交付网 PDF 逐字节相同（110,438 B）；重渲印 PDF 文字层亦逐字节相同。生产 web PDF 未被比对步骤覆盖（重渲写进 scratch `web-rerender-fix2.pdf`）。

## 5. 交付物（修后三件）

- 印刷 PDF `A-Lucerna-VOL4.pdf`：**12,932,441 字节**，8 页，1462.5×2025 pt，sha256 `7e235e4591c034815ed90bcc21cef48a3b40bb1eb39bb0ebb1c8f027fbcb2e42`（修前 12,932,439 B，`782e7cb9…`）。
- 网页 PDF `A-Lucerna-VOL4-web.pdf`：**1,139,917 字节**，8 页，sha256 `aad718e1efccbbcf24f4a1d6ac05fbe1bc59bf3b431037384f5645896bd7fc6c`（修前 1,139,921 B，`e02cf58c…`）；文字层 110,438 B（修前 110,367 B；+71 B 为 P1 盒高减 2 单位后 `pdftotext -layout` 空格重排，词多重集 diff 仍为 0，词数仍为 8,507）。
- 文字 `2026-w47-pt-en.text.md`：**37,333 字节，534 行，不变**，sha256 `513326ffa497ca2b6714c1016eadbfaa2ac3447269b782749c968022e0e118ed`（与修前逐字节相同）。

## 6. D1/D2/D3 旧修复存活复验（修后逐项，`verify_ed-pt.py` 全绿）

| # | 修复 | 核实 | 结果 |
|---|---|---|---|
| D1 | P1 刊头标语 | `tables_en.py` 新标语 `The Portuguese that Brazil is reading` 在位；旧形 `The Portuguese Brazil is reading` 全版构建源 0 处；渲染 P1 文字层同值 | 存活 |
| D2 | P4 词表注 | `tables_en.py:36` `"冠军": "title"`；旧值 `champion` 0 处；渲染 P4 Note 行 `o título title` | 存活 |
| D3-56/57/58/102 | P8 注冒号 | P8 SVG 内 `3 > 1: mais`、`5 > 4: mais`、`16:30 < 17:00: mais cedo`、`cair numa sexta-feira: falls on a Friday` 各 1 处；旧形 0 处 | 存活 |
| 全版冒号复扫 | `:` 后直接接字母 | 8 个 SVG + text.md 均为 **0 处** | 存活 |
| p8 键 | 150 键 | 新旧 p8 extract JSON 对比：**0 处差异**（noted_set 150/150） | 存活 |

## 7. 机械门（全跑，见 GATE-LOG.md）

| 门 | 结果 |
|---|---|
| run.py | rc=0，TOTAL 150，0 溢出 |
| gates.py | **16/16 PASS，FAILURES: none** |
| occlusion 真实审计 | **0 flags**（自检 6 类全触发） |
| creambox（canonical）真墨 | **0 溢出**（31 OWN 末行，真墨底余最小 +2.1px）；canonical `desc-clear` 6 处 −0.9~−1.1 为 0.30×字号保守估计，同行真墨 +4.8/+4.9，修前亦然（GATE-LOG §2 裁决） |
| 全版盒标题横向 PIL 真墨重扫 | **31/31 0 溢出**；两修复处真墨余量 +15.5（D-B1）/+21.5（D-B2）；其余 29 标题最小 advance 余量 +22.2（与 proof1 相同） |
| spill sweep | box-vs-hline 0；bridges 20，orphans 0，widows 0 |
| p8 extract + compare | 150/150；CLEAN，keydiff [137, 138]（预期） |
| keycheck | **149/150**（仅 Q150 例外，预期） |
| freeze baseline（版 + 核心对照） | **8/8 + 8/8** byte-identical（`--build` = core-pt 构建目录，`--core-svg` = core-pt svg 目录） |
| freeze diff | 新增 CJK **9 个，全部 U+3000**（P1 2、其余每页 1）；新增汉字 0 |
| print/web 文本层比对 | `pdftotext -layout` 逐字节相同 110,438 B，逐页 8/8 相同；check_final 词多重集 diff 0（各 8,507 词） |
| check_s11（pt-adapted §1.1） | **ALL PASS**（rc=0）。注：无 pt 家族原版，en 家族版硬编码 core-en/en-* 无法运行；本轮写了 pt-adapted 等价脚本（`check_s11-pt.py`）。初版误植 en-core `(N)` 括号空白标记致 12 项误报——核查证实 core-pt 自身亦无该标记（pt P8 为 `N.` 编号项 + `___` 空白，核心与本版均为 21 处），已更正口径重跑全绿。 |
| verify_ed（pt-en fix verification） | **ALL PASS**（rc=0；D1/D2/D3 存活 + D-B1/D-B2 修后值 + text.md 不变 + 150 键不变；脚本 `verify_ed-pt.py`，因 en 家族版只验 en-core fix1 专属项） |
| P8 最小字号 | **9.75pt**，低于 9.75pt 0 处 |
| 孤儿标点全版重扫 | A 0、B 0、C 6（合法引导冒号）、D 0、E 1（Q38 `Sem ___ ,`，与核心同行逐字相同） |
| 8 页逐页目视 | 8/8 印版 + 网版 P1/P8 已目视；P1/P7 标题裁图确认两处修复入版；其余无新问题（GATE-LOG §6） |
| 重渲比对（scratch） | 印 PDF SHA 与交付逐字相同；网 PDF 文字层逐字节相同 |

## 8. KIT 更正

- WEEKLY-KIT.md §9 `boxtitle true-ink clear on all boxes` 一句改为如实记录（修前 2 处溢出 D-B1 −22.5 / D-B2 −14.5，修后 0 处；两处修后余量 +15.5 / +21.5）。
- KIT 内 `535 lines` 三处（L58、L94×2、L116）更正为 `534 lines`（实测 `wc -l` 与 gates.json `text_lines: 534` 一致）。
- 同附录的 `New files` 印/网 SHA 与字节数、“Gates”段的 `pdftotext` 字节数（110,367→110,438）同步更新为修后值，并追加 “Fix round 2” 记录段。
- 附注：`scratch-refanout-pt/FANOUT-REPORT-pt.md` §2 表格亦称 pt-en boxtitle "clear"——与 KIT §9 同源失实表述；该报告覆盖 10 个 pt 版、属共享重建报告，本轮只在 KIT 内更正并在此记录，供协调员决定是否同步修订报告。

## 9. 结论

- D-B1/D-B2 已在源头修掉（两处标题字号 23→21pt，措辞零改动），修后 PIL 真墨余量 **+15.5 / +21.5**，交付 PDF 像素裁图目视确认，全版 31 个盒标题 **0 溢出**；其余全部机械门、150 键、8 页目视均通过；D1/D2/D3 全部存活；text.md 字节不变。
- 按 SOP §8.4，定稿须经新一轮独立全量校对零问题；本轮为返修自查，不作定稿结论。第二轮复校由协调员另派。
- 本轮未作任何 git 提交；未改 core-pt、W43–W46、其他目标语家庭；版目录仍为未入仓新目录。
- 遗留待协调员定夺（非缺陷）：FANOUT-REPORT-pt.md §2 表格的 pt-en boxtitle "clear" 表述是否同步修订（见 §8 附注）；scratch `furniture.py` FURN[en] `badge372` 的 `EXPLICATIONS` 拼写 stale（fix1 已记，见 KIT §6，本轮未动）。

