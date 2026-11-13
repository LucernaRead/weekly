# GATE-LOG — 2026-W47 pt-en 第二轮独立复校（proof2）

- 校对员：proof2；时间：2026-11-11 03:07–约 09:30 EST
- 复校对象：`production/2026-w47/2026-w47-pt-en/`（未改任何成品；run.py 重跑在 freeze 工具的 build-copy 内进行）
- 构建解释器（与 KIT §7 一致）：`tools/venv/bin/python`，Python 3.12.3
- 本日志只记机械门实测结果；内容校对见 `PROOF-NOTE.md`。

## 探针（开工硬门禁，双通）

- `echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin` → 成功（`8b0b10080458b0f2c039983021e26688ce794d49`）
- scratch 写盘探针（`hidden_files/w47/probe-pt-en2.txt`）→ 成功（已删除）

## 身份核对（自算完整 SHA-256，与任务书逐字比对）

| 文件 | 字节 | SHA-256（完整） | 任务书比对 |
|---|---|---|---|
| `A-Lucerna-VOL4.pdf`（印刷） | 12,932,451 | `0146a4202b015f44659b4bba067a7411f90891cb640085dee5fec2010bd06af1` | 一致 |
| `A-Lucerna-VOL4-web.pdf`（网页） | 1,102,777 | `a974ef7ccf7c879f58e3626d874d9ce18e3da5f2a35faef43717e81706254c80` | 一致 |

两 PDF 均为 8 页，1462.5×2025 pt。

## 机械门结果

| # | 门 | 命令（venv python） | 结果 |
|---|---|---|---|
| 1 | gates.py | `gates.py`（版目录内） | RC=0，**16/16 PASS，FAILURES: none**。要点：footer+page 8/8；P7 金句 8 条各 2 次+英译+页码；披露 5 项全 True；图片+出处 5/5；P1 头条 41 字符（≤56）；P7 金句区 max baseline 2382.17（< 2404）；词表注 29 项全在 |
| 2 | occlusion | `tools/occlusion_audit.py production/2026-w47/2026-w47-pt-en --json gates/en-occlusion-pt-en2.json` | RC=0，自检阳性对照 6 类全触发、干净对照静默；**0 flags** |
| 3 | p8 extract | `tools/p8.py extract --p8 …/svg/p8-avaliacao.svg --total 150` | RC=0，**150/150**（题号 1–150 全集） |
| 4 | p8 compare | `tools/p8.py compare --core-dir production/2026-w47/core-pt --edition-dir production/2026-w47/2026-w47-pt-en --target pt --total 150` | RC=0，**CLEAN**，missing=[]，extra_count=0，keydiff=[137, 138]（仅翻译题答案，已人工验正确） |
| 5 | freeze baseline | `tools/freeze.py baseline --build production/2026-w47/2026-w47-pt-en --core-svg production/2026-w47/2026-w47-pt-en/svg --out gates/en-freeze-pt-en2b` | RC=0，**8/8 SVGs byte-identical**（repointed files: none）；核心 SVG 复核未被改写 |
| 6 | freeze diff | `tools/freeze.py diff --core-svg production/2026-w47/core-pt/svg --edition-svg …/svg` | RC=0，新增 CJK 共 9 个，**全部为 U+3000**（P1 2、其余每页 1）；新增汉字 0。核心 CJK 167/210/166/173/228/138/401/1285 → 英版 21/17/13/15/14/16/13/15 |
| 7 | print/web 文字层 | `check_final_proof.py`（第一轮脚本的副本，输出改写至本目录） | RC=0，页数 8/8；词数 print=8507 / web=8507；**词多重集 diff 0**；pdftotext -layout 印刷 110,249 B / 网页 110,380 B（差值仅为提取换行差异，词集相同；webpdf 口径文字层 46,073 B） |
| 8 | P8 答案字号 | 同上 | 答案区 187 spans、1,543 词；**最小字号 9.75pt**（恰为 §1.1 下限）；区内 span 尺寸 {9.75, 10.5, 14.625, 18.75} |
| 9 | run.py 重跑 | freeze build-copy 内 `run.py` | **RC=0，零 FLOW OVERFLOW / 零 HEAD TOO WIDE**；TOTAL 150（A2 48 / B1 71 / B2 31；分版 10/18/18/18/18/18/12/38） |
| 10 | U+2019 全扫 | 8 个 SVG 文本扫描 | **总数 0** |
| 11 | CJK 残留全扫 | 8 个 SVG 逐字符扫描 | 渲染文本内中文字符 0；仅 U+3000 家具分隔符 + P1 冻结蛾标 `<title>Lucerna 三色蛾</title>`（与核心逐字相同，不渲染）；`.text.md` 内 6 处 U+FF5C 为冻结 `Note｜` 标签格式（见 PROOF-NOTE O2） |
| 12 | 徽章逐页计数 | 8 个 SVG 徽章标签文本提取 vs 核心 | 逐页同数同级（P1 10/3/1、P2 14/1、P3 10/8、P4 15 B1、P5 15/3、P6 18 B2、P7 4/4/4、P8 8/24/3）；P1 `#46581f` 填充数差 1 系家具行拆分所致，非徽章（见 PROOF-NOTE O7） |
| 13 | 冒号复扫 | 8 个 SVG `:` 后接字母 | **0 处**（仅有的 5 处 `:i` 命中均为 base64 图片数据）；时刻写法已排除 |
| 14 | VOL 核对 | 8 个 SVG | `VOL.4` 9 次 + 顶条 `VOL. 4` 1 次；`VOL.3` 2 次（均 P7 披露内）；`VOL.5` 3 次（均 P7 披露/预告内）；无错印期号 |
| 15 | .text.md 校验 | 行数/题号/双空格/改动行 | 534 行（KIT 称 535，见 PROOF-NOTE O1）、题号 150/150、双空格 0 行；第 215 行 `o título title`；旧串 `o título champion` 0 处；D1 标语不在 .text.md 内（与 fix1 说明一致） |
| 16 | ABSTRACT.txt | 单行/引号/事实 | 561 字节，1 行，无 ASCII 双引号，事实与本期一致 |
| 17 | 范文字数 | `.text.md` 独立计数 | **88 词**，与 Q150 标注一致 |

## 回归核查（D1/D2/D3，源表 + SVG 双重核实）

| 处 | 新串 | 旧串残留 |
|---|---|---|
| D1 P1 标语 | `The Portuguese that Brazil is reading`（SVG 1 处；`tables_en.py:197` 同值） | 0 |
| D2 P4 词表注 | `o título title`（SVG 1 处；`tables_en.py:36` `"冠军": "title"`） | 0 |
| D3-56 | `3 > 1: mais` | 0 |
| D3-57 | `5 > 4: mais` | 0 |
| D3-58 | `16:30 < 17:00: mais cedo` | 0 |
| D3-102 | `cair numa sexta-feira: falls on a Friday` | 0 |

两份 `tables_en.py`（版目录副本 + scratch-fanout-pt 机制表）逐字节一致（`diff -q` 通过）。本轮新 p8 extract JSON 与 fix1 的新 extract JSON 逐字段比对**零差异**。

## 备注

- freeze baseline 首次调用误将 `--core-svg` 指向 core-pt 的 SVG 目录，得 0/8（该参数的含义是「待比对的已发货 SVG」，对 fan-out 版应指向本版自己的 svg 目录）；改指本版 svg 目录后重跑为 **8/8**。两次日志均保留（`freeze-pt-en2.log` 为误指记录，`freeze-pt-en2b.log` 为正确重跑）。
- 本轮机械门全部通过；内容层 0 缺陷，见 `PROOF-NOTE.md` §5。8 项观察项（O1–O8）均不计缺陷。
- 本轮未修改任何成品；全部校对证据在 `scratch-proof-pt-en2/`（`gates/` 日志与 JSON、`render/` 10 张全新渲染图、freeze 重跑副本 `gates/en-freeze-pt-en2b/`、`en-textdiff.json`、`en-p8size.json`）。
