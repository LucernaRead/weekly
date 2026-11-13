# GATE-LOG — 2026-W47 ja-it, 第二轮独立复校机械门全套（2026-11-11）

构建/门禁解释器一律 `tools/venv/bin/python`（Python 3.12.3）。门禁文件在本目录
（`scratch-proof-ja-it2/`）。本轮全部机械门均为独立重跑，不采信第一轮/fix-1 的门结果。

## 0. 开工探针与身份

| 检查 | 结果 |
|---|---|
| `git hash-object -w` 小文件 | 成功（`da0c4eb8…`） |
| 写盘探针 `scratch-proof-ja-it2/probe.txt` | 成功；磁盘 46 GB 可用 |
| 印刷 PDF 字节/SHA | 29,099,163 B / `8ed65a83d1795577f7ca83f47009f917af18c23adcd7cb1b0b335d86d690f15c`，与任务书一致 |
| 网页 PDF 字节/SHA | 4,476,985 B / `d8af211a19b8a216d4bdba9048ca47a56d4fd628346b4c5dd63741306825805a`，与任务书一致 |
| text.md | 46,678 B / 1378 行 |

## 1. 整期重建（freeze）

| 步骤 | 结果 | 日志 |
|---|---|---|
| `run.py` runA | rc 0；FLOW OVERFLOW / HEAD TOO WIDE 0；登记 150（A2 48 / B1 73 / B2 29；分版 10/18/18/18/18/18/12/38；范文 154 字） | `build-runA.log` |
| `run.py` runB（freeze 同解释器） | rc 0；0 溢出 | `build-runB.log` |
| freeze：runA vs runB SVG sha256 | **8/8 相同** | `sha-runA.txt` / `sha-runB.txt` |
| runA vs 交付前快照 | **逐字节相同**（重建未改动任何交付件） | `/tmp/ja-it2-svg-pre.txt` 对照 |
| 构建日志流止位置 | P7 teaser 止 2528.1（页脚 2580，52px 余量）；P8-ex 流止 col 3 y=561（底 1252）；P8-keys 流止 col 3 y=2442（底 2540，98px 余量） | `build-runA.log` |

未重跑 `render.py` / `webpdf.py`（会覆写已交付的双 PDF；交付件哈希已与任务书核对一致，
且 SVG 重建逐字节相同已证明构建可复现）。

## 2. 全套机械门

| 门 | 工具/方法 | 结果 | 文件 |
|---|---|---|---|
| Occlusion | `tools/occlusion_audit.py <edition>/svg` | selftest OK（6 类全触发，干净对照静默）；**0 flags** | `it-occlusion-proof2.json`、`occlusion-proof2.log` |
| P8 extract | `tools/p8.py extract --p8 svg/p8-tesuto.svg --total 150` | **150/150**（parse: lines） | `it-p8-proof2.json`、`p8extract-proof2.log` |
| P8 compare | `tools/p8.py compare --core-p8 production/2026-w47/core-ja/svg/p8-tesuto.svg --edition-p8 … --total 150` | **CLEAN**；missing=[] extra_count=0 uncertain=[]；keydiff **恰为 [137, 138, 139, 140]** | `it-p8compare-proof2.json`、`p8compare-proof2.log` |
| 文字层双版一致 | `pdftotext`（默认 + `-layout` 两版提取）print 与 web 分别提取后 `cmp` | **逐字节一致**：默认提取各 47,002 B；`-layout` 各 106,304 B | — |
| P8 最小字号 | PyMuPDF（tools venv）取 P8 全部 span | **9.975pt**（167 spans）≥ 9.75pt；次档 10.35pt（79 spans，题干冻结值） | — |
| U+2019 全扫 | `.py` + 8 SVG + text.md + KIT 逐字符计数 | **U+2019 0**（SVG 内 U+0027 共 29 处，均为正常撇号） | — |
| §1.1 grep | 8 SVG | 纸 `#fbfaf6` 1×/页（共 8×）；旧 `#f7f1e2` 0×；`·` 0×；`Pagina N di 8` 1×/页；刊头 196px 1×（P1）；徽章 A2 #5c6e30 / B1 #46581f / B2 #37402f | — |
| text.md validator | `export-textmd-it.py` 重导出到隔离目录后 `cmp` | **逐字节相同**（46,678 B） | `textmd-export-proof2.log` |
| 修前→修后 text.md diff | `diff` fix-1 scratch `textmd-pre.txt` vs 交付 text.md | **恰好 6 行**（1263/1264、1269、1278、1332、1338） | — |
| freeze diff | `tools/freeze.py diff --core-svg core-ja/svg --edition-svg … --strict-cjk` | rc=1，净增 CJK 15 字——逐字裁定为工具误报（见 PROOF-NOTE O1）：9× U+3000 + ノミネート 5 字（P8 注 107 回显题干词）+ 楽 1 字（P8 注 58 回显千秋楽）；每页 CJK 数均低于核心，无新增目标语文本 | `freeze-diff-proof2.json`、`freeze-diff-proof2.log` |
| 徽章计数 | SVG 文本节点精确计数 | A2 46 / B1 72 / B2 27（合计 145）；+3 组配对题共用徽章 = 登记 48/73/29，完全 reconciled | — |
| VOL 计数 | SVG 文本 grep（`-o` 计数，含跨节点） | VOL.4 10×（8 页脚 + P1 2×）；VOL.3 1×；VOL.5 **4×**（3 连续 + P4 1 跨节点） | — |

## 3. fix-1 回归（grep 证据）

| 检查 | 结果 |
|---|---|
| 旧拼写 `Fujiryūga` / `Umi-no-umi`（content*.py + svg/ + text.md） | **0 / 0** |
| 旧拼写（双 PDF pdftotext 文字层） | **0 / 0** |
| 新拼写 P8 SVG | `Fujiryōga` **5×**、`Chura-no-umi` **1×** |
| 新拼写每层（py / SVG / text.md） | 各 5× / 1×；双 PDF 文字层各 5× / 1× |
| 罗马字独立核实 | 藤凌駕=ふじりょうが（ozumo.jp 引日本相撲協会公式 profile；日刊スポーツ 2025-10-01）；美ノ海=ちゅらのうみ（日刊スポーツ 2018-05-30、2018-06-24）。两处新拼写均正确，旧形确为错读 |

## 4. 8 版目视（印刷 PDF 重新渲染，100 dpi；另网页 PDF P1/P8 渲染对照）

- P1：无溢出/重叠/压页脚；头条、热搜榜、目录、快讯、图片与图注齐全。
- P2 / P3 / P5 / P6 / P7：无溢出/重叠/压页脚；P6 图表柱长与 38/24/22/16 成比例，练习数据标注在位；
  P7 诊所/框架/披露/预告/金句齐全，teaser 在页脚之上收束。P2/P3/P5/P6/P7 中部空白带与 P4 `(VOL.`
  跨栏为继承自已定稿核心版的外观（PROOF-NOTE O5），本版内无动作。
- P8：答案区 6 处新拼写均已印出（48 Chura-no-umi；49/54/63/111/116 Fujiryōga），无溢出、无重叠、
  末行在页脚之上；图片（Arashiyama 寺）与图注/出处齐全；150 键逐题验算全对。
- 网页 P1/P8 渲染与印刷版逐项一致，无 tofu；无新缺陷发现。

## 5. 结论

- 全套机械门全绿（strict-CJK 一项为已裁定的工具误报，见 O1）；150 键复核全对；8 版目视无缺陷；
  fix-1 的 6 处改动逐项核对全部改对，罗马字经独立公开来源核实正确。
- **结论：(a) 零问题，可定稿。**
- 未改任何源码/成品：`run.py` 两次重建输出的 SVG 与交付前快照逐字节相同；未跑 insert.py、
  未跑 lint --write，未做任何 git 写操作；工作只在 fanout-ja-it 目录（只读）与本 scratch 目录。
