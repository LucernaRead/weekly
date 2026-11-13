# GATE-LOG — 2026-W47 ja × zh-tw 第二轮全量复校（proof2，独立复校员）

- 版：`2026-w47-ja-zh-tw`，VOL.4，2026-11-16–22
- 证据目录：本目录（`hidden_files/w47/scratch-proof-ja-zh-tw2/`），`work/` 下为检查脚本与输出。
- 构建解释器：`tools/venv/bin/python`（仅用于只读门禁；未运行 run.py/render.py/webpdf.py，未重建）。
- 结论速览：**全部机械门通过；150 键复核通过；8 版目视干净。结论 (a) 零缺陷可定稿。**

## 0. 探针

| 步 | 命令 | 结果 |
|---|---|---|
| 开工探针 | `echo test \| git -C ~/workspace/weekly-git hash-object -w --stdin` | 成功，`9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，rc=0 |
| 写盘探针 | 在本目录写 `probe.txt`（`probe-ok`） | 成功 |
| 写盘前重探 | `echo test2 \| git -C ~/workspace/weekly-git hash-object -w --stdin` + 写 `probe2.txt` | 成功，`180cf8328022becee9aaa2577a8f84ea2b9f3827`，rc=0；`df` /home/hatch 77G 可用 |
| EDQUOT | 全程无 `Disk quota exceeded` | — |

## 1. SHA / 字节核对

| 命令 | 结果 |
|---|---|
| `sha256sum Lucerna-VOL4-JA-ZH-TW.pdf Lucerna-VOL4-JA-ZH-TW-web.pdf` + `stat` | print 26,034,639 B `a2640e158bf5c13e…`、web 4,788,063 B `00575aa2683794a1…`，与任务给定值逐字一致 |
| `sha256sum 2026-w47-ja-zh-tw.text.md` + `wc -l -c` | 44,361 B、1352 行、`8c18a0e9fb47b145108a23b1144cd58bd9f7e3fc20e7ec5575d1cb55bb3d5db0`（与 KIT §4 一致） |
| `pdfinfo` 双 PDF | 各 8 页，1462.5 x 2025 pts |

## 2. 文字层门

| 命令 | 结果 |
|---|---|
| `pdftotext`（无 `-layout`）双 PDF → `/tmp/proof2-print.txt`、`/tmp/proof2-web.txt`；`wc -c`；`cmp` | 各 **44,661 字节**，`cmp` 逐字节一致，rc=0 |
| `pdftotext -layout` 双 PDF（仅作页数/版式参考） | 各 82,086 字节（含空白对齐，非文字层字节数；不作为门禁依据） |

## 3. 冻结门（只读核实，未重跑 run.py）

| 命令 | 结果 |
|---|---|
| `diff zh-tw-sha-fix2-run1.txt zh-tw-sha-fix2-run2.txt`（fix2 证据） | 无输出，run1==run2 |
| checks4.py：当前 8 张 SVG 的 SHA256 vs `zh-tw-sha-fix2-run2.txt` | **8/8 MATCH** |

## 4. 几何遮挡审计（tools/occlusion_audit.py）

| 命令 | 结果 |
|---|---|
| `tools/venv/bin/python tools/occlusion_audit.py --selftest` | rc=0，自检 OK（6 类阳性对照 BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 各 1 触发，干净对照静默） |
| `tools/venv/bin/python tools/occlusion_audit.py production/2026-w47/fanout-ja/2026-w47-ja-zh-tw/svg --json work/occlusion-proof2.json` | rc=0，实审 **`svg: 0 flags`** |

## 5. P8 门（tools/p8.py）

| 命令 | 结果 |
|---|---|
| `tools/venv/bin/python tools/p8.py extract --p8 …/svg/p8-tesuto.svg --total 150 --json work/p8extract-proof2.json` | rc=0，**noted set = 150 of 150**，题号 1–150 连续 |
| `tools/venv/bin/python tools/p8.py compare --core-p8 production/2026-w47/core-ja/svg/p8-tesuto.svg --edition-p8 …/svg/p8-tesuto.svg --total 150 --json work/p8compare-proof2.json` | rc=0，**CLEAN**，missing=[] extra_count=0 uncertain=[]，**keydiff=[139, 140]**（KIT §11 F3 预期） |

## 6. 150 键逐键比对（checks5.py，自写文件脚本，非 heredoc）

| 命令 | 结果 |
|---|---|
| `python3 work/checks5.py`（text.md 答案行 vs p8 extract keys） | text.md 150 条、1–150 连续；键部差异 **1 条**——仅 key 150（text.md `✓ 範文見本版 H 區（154 字）` vs extract 仅取 `✓` 标记；SVG 原文含全句，grep 核实 1×），**实质差异 0 条** |
| 抽检点（text.md 全文） | 47 `A — 首日戰勝大之里的是義之富士`；115 `A — 大之里首日輸給了義之富士`；137/138/139/140 与 KIT §3 逐字一致 |

## 7. 弯标点 / 旧字 / 残留扫描（checks1.py）

| 扫描 | 范围 | 结果 |
|---|---|---|
| U+201C / U+201D / U+2019 | text.md + 8 SVG + content*.py + 双 PDF 文字层 | **各 0** |
| 「 / 」 | text.md + SVG | 各 84（成对） |
| `出來栄え` / `波亂` / `出來` / `一之富士` | 源码、text.md、SVG、双层 | **0** |
| `波乱` | 源码 4 / p4 SVG 4 / text.md 4 / 双层各 4 | 一致 |
| `出来栄え` | 源码 2（:19 正文、:20 注文） | text.md/SVG/双层为同位置行折断 `出来栄` + `え`（已逐字核实，见 PROOF-NOTE §1） |
| `義之富士` / `義ノ富士` | 双层 `義之富士` 各 2×；`義ノ富士` 双层各 2× | fix1 回归无误 |
| `参考答案` / `參考答案` / `吉伊卡哇` | text.md | 0 / 1 / 4（正确） |
| gloss headword 比对 | content12/34/56 共 10 条 gloss vs core | headword 全部相同，0 差异 |
| U+4F86 來 全版核查 | text.md | 仅中文读者语 + key 80 释义句（O1 观察项）；日文正文 `三浦璃来` 用 U+6765（2×） |
| §1.1 样式 | SVG + text.md | `#fbfaf6` 8×，`#f7f1e2` 0，`#c9a227`/`#8b4513` 0，`·` 0，页脚 8× |

## 8. 正文对照（checks2.py / checks3.py）

| 命令 | 结果 |
|---|---|
| checks2.py：OpenCC t2s（tools/venv）转换 ed text.md 后与 core text.md diff | 全部差异为 t2s 对日文汉字的转换噪声 + 已载明的家具差异（页脚、`(N面)`、间距、趋势行、P7 披露）；t2s 在 3 处（:193/:624/:862）输出 U+FFFD，经逐字核实为 OpenCC 转换 artifact，原文与核心逐字节相同 |
| checks3.py：原始 text.md ed vs core 逐行 diff + kana-run 比对 | 98 个 hunk；6 个“疑似不匹配”逐一人工复核，均为脚本把中文释义字并入 kana-run 的误报，日文部分逐字相同；其余 hunk 均为读者语/家具差异 |
| P7 金句逐字核查 | 9 条引句（8 条日文句 + `ryuuryuu`）在正文逐字出现；`『りくりゅう』は、フィギュアスケートのペアです。` 出处为 P7 本身 B1 段（:913–916），页注 (7面) 诚实，与核心一致 |
| 日期/星期核查 | `TZ=Asia/Tokyo date -d`：11/19 週四、11/22 週日、11/23 週一、11/5 週四、11/8 週日、12/1 週二、11/13 週五、11/21 週六、11/26 週四、12/12 週六、11/29 週日、11/7 週六、11/8 週日、11/9、11/10——与正文/题/键全部一致 |

## 9. Abutting / 字号 / 范文（checks4.py，PyMuPDF，tools/venv）

| 命令 | 结果 |
|---|---|
| checks4.py abutting 扫描（span 级相邻缺口，print vs web） | 双 PDF 各仅 1 处内部边界缺口 7.785pt（P1 目录行标题与右端 `A2→B2` 之间，分栏间距，数值逐字相同）；其余行内无 >0.5pt 缺口 |
| SVG italic 计数 | 8 页 `italic` 全 0——webpdf 斜体/字重类工具层风险在本版不存在 |
| P8 最小字号 | print P8：371 spans，最小 **9.975pt**，全部 ≥9.75pt，与 KIT 冻结值一致 |
| 范文字数 | H 区范文实测 **154 字**，与 `範文（154 字）` 一致 |

## 10. 8 版目视（cards/*.png，逐版看图）

| 版 | 结论 |
|---|---|
| P1–P8 | 全部干净，零问题（详见 PROOF-NOTE §7；P3/P4 修复点重点复核，P2/P6 跨栏续接为正常分栏） |

## 11. 未执行

未改任何源文件；未运行 run.py / render.py / webpdf.py / insert.py / lint --write；未 git add/commit/push/reset/stash；未碰 core-ja、其他版、其他周、tools/、issues/。
