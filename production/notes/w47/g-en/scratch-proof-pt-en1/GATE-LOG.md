# GATE-LOG — 2026-W47 pt-en 第一轮独立复校（叶子）

- 校对员：叶子；时间：2026-11-11 02:28–07:40 EST
- 复校对象：`production/2026-w47/2026-w47-pt-en/`（未改任何成品；run.py 重跑在 scratch 副本内进行）
- 构建解释器（与 KIT §7 一致）：`tools/venv/bin/python`，Python 3.12.3，Pillow 13.0.0（系统 python3 为 Pillow 10.2.0，未使用）
- 本日志只记机械门实测结果；内容校对见 `PROOF-NOTE.md`。

## 探针（开工硬门禁，双通）

- `echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin` → 成功（`da0c4eb8d9a48d171a33574b380752e183286751`）
- scratch 写盘探针（`scratch-proof-pt-en1/.probe`）→ 成功

## 身份核对（自算完整 SHA-256，与 KIT 逐字比对）

| 文件 | 字节 | SHA-256（完整） | KIT 比对 |
|---|---|---|---|
| `A-Lucerna-VOL4.pdf`（印刷） | 12,932,446 | `8d2b58152bc0969151f8a7ab8becb0976221efdc62cac0d3cce877de8f160e4a` | 一致 |
| `A-Lucerna-VOL4-web.pdf`（网页） | 1,102,770 | `40bc2f444dbc31fbf0ef49643f1f81da13c134cab5ba0ec0a3ea804574a5e49c` | 一致 |

两 PDF 均为 8 页，1462.5×2025 pt。

## 机械门结果

| # | 门 | 命令（venv python） | 结果 |
|---|---|---|---|
| 1 | gates.py | `gates.py`（版目录内） | RC=0，**16/16 PASS，FAILURES: none**。要点：footer+page 8/8；P7 金句 8 条各 2 次+英译+页码；披露 5 项全 True；图片+出处 5/5；P1 头条 41 字符（≤56）；P7 金句区 max baseline 2382.17（< 2404）；词表注 29 项全在 |
| 2 | occlusion | `tools/occlusion_audit.py production/2026-w47/2026-w47-pt-en --json gates/en-occlusion-pt-en1.json` | RC=0，自检阳性对照 6 类全触发、干净对照静默；**0 flags** |
| 3 | p8 extract | `tools/p8.py extract --p8 …/svg/p8-avaliacao.svg --total 150` | RC=0，**150/150**（题号 1–150 全集） |
| 4 | p8 compare | `tools/p8.py compare --core-dir production/2026-w47/core-pt --edition-dir production/2026-w47/2026-w47-pt-en --target pt --total 150` | RC=0，**CLEAN**，missing=[]，extra_count=0，keydiff=[137, 138]（仅翻译题答案，已人工验正确） |
| 5 | freeze baseline | `tools/freeze.py baseline --build production/2026-w47/2026-w47-pt-en --core-svg …/svg --out gates/en-freeze-pt-en1` | RC=0，**8/8 SVGs byte-identical**（repointed files: none）；核心 SVG 复核未被改写 |
| 6 | freeze diff | `tools/freeze.py diff --core-svg production/2026-w47/core-pt/svg --edition-svg …/svg` | RC=0，新增 CJK 共 9 个，**全部为 U+3000**（P1 2、其余每页 1）；新增汉字 0。核心 CJK 167/210/166/173/228/138/401/1285 → 英版 21/17/13/15/14/16/13/15 |
| 7 | print/web 文字层 | `check_final_proof.py`（check_final.py 的副本，输出改写至本目录） | RC=0，页数 8/8；词数 print=8502 / web=8502；**词多重集 diff 0**；pdftotext 印刷 46,043 B / 网页 46,049 B（差 6 B 为提取换行差异，词集相同） |
| 8 | P8 答案字号 | 同上 | 答案区 187 spans、1,539 词；**最小字号 9.75pt**（恰为 §1.1 下限）；区内 span 尺寸 {9.75, 10.5, 14.625, 18.75} |
| 9 | run.py 重跑 | scratch 副本 `rerun/2026-w47-pt-en` 内 `run.py` | **RC=0，零 FLOW OVERFLOW / 零 HEAD TOO WIDE**；TOTAL 150（A2 48 / B1 71 / B2 31；分版 10/18/18/18/18/18/12/38）；重建 8 个 SVG 与 shipped 版**逐字节一致 8/8** |
| 10 | U+2019 全扫 | 8 个 SVG 文本扫描 | **总数 0** |
| 11 | CJK 残留全扫 | 8 个 SVG 逐字符扫描 | 渲染文本内中文字符 0；仅 U+3000 家具分隔符 + P1 冻结蛾标 `<title>Lucerna 三色蛾</title>`（与核心逐字相同，不渲染）；`.text.md` CJK 0 |
| 12 | 徽章逐页计数 | 8 个 SVG 徽章色+题号提取 vs 核心 | 逐页同数同级（含分组徽章 P2 25–28 A2、P4 52–55 B1、P8 141–144 B2）；分级总计 A2 48 / B1 71 / B2 31 |

## 备注

- freeze diff 首次调用误用 `--core-dir/--edition-dir` 被 CLI 拒绝（RC=2），改用正确的 `--core-svg/--edition-svg` 后通过；工具本身无问题。
- occlusion 首次调用在版目录内用相对路径 `production/...` 报错（路径不存在），改在仓根以正确相对路径重跑后通过；工具本身无问题。
- check_final.py 直接跑会把 JSON 写回共享 scratch-fanout-pt（会覆盖 builder 的 en-*.json），故复制一份到本目录跑，输出落在 `scratch-proof-pt-en1/`（`en-textdiff.json`、`en-p8size.json`）。
- 本轮机械门全部通过；内容层缺陷（3 类轻微）见 `PROOF-NOTE.md` §1，不属于机械门范畴。
