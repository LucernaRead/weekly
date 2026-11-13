# GATE-LOG — 2026-W47 en-de 第一轮独立复校机械门记录（叶子）

- 版：`2026-w47-en-de`；解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Python 3.12.3；未用系统 python3）
- 日期：2026-11-11；命令均在 `~/workspace/weekly-git` 仓根或版目录下执行；输出存本目录 `gates/`。

## 0. 开工探针（双通）

- `echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin` → `da0c4eb8d9a48d171a33574b380752e183286751`，成功。
- 在 `hidden_files/w47/` 真实写小文件成功（`.probe`，后已删除）。

## 1. 身份核对

- `sha256sum`：
  - `The-Lucerna-VOL4-en-de.pdf`：29,330,795 字节，`6d91162fac10c81e59ec811362136cd69e4e535a5b7ad04b4b98c94d530d95ba` — 与 KIT 一致。
  - `The-Lucerna-VOL4-en-de.web.pdf`：2,377,924 字节，`e8c6746167d7351e0cda55427ec191da98af9112e94f281cf390e5488f28d751` — 与 KIT 一致。
- `pdfinfo`：两 PDF 均为 8 页、1462.5 × 2025 pt。

## 2. occlusion_audit.py

- 命令：`tools/venv/bin/python tools/occlusion_audit.py production/2026-w47/2026-w47-en-de/svg`
- 结果：`selftest OK: planted classes fired {...}; clean controls silent`；`0 flags`。**PASS**

## 3. p8.py extract

- 命令：`tools/venv/bin/python tools/p8.py extract --p8 production/2026-w47/2026-w47-en-de/svg/p8-test.svg --total 150 --json gates/p8-extract.json`
- 结果：`noted set = 60 of 150 (parse: joined)`，与 core 集合相同。**PASS**
- 追加核实（extract keys vs `registry.json`）：150/150 键齐全；唯一差异 Q150：印刷短标签 `Offene Aufgabe` vs registry 全文 `Offene Aufgabe — Stichpunkte im Schreibkasten; Mustertext im Kasten auf Seite 8`——与 core 短标签模式一致。

## 4. p8.py compare

- 命令：`tools/venv/bin/python tools/p8.py compare --core-p8 production/2026-w47/core-en/svg/p8-test.svg --edition-p8 production/2026-w47/2026-w47-en-de/svg/p8-test.svg --total 150 --json gates/p8-compare.json`
- 结果：`status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 140, 150]`。
- keydiff 逐条核实：137–140 为德语翻译键（KIT §2 登记的预期译文，逐字核对无误），150 为写作题短标签；与 W46 en-de 同样 keydiff。**PASS（预期内）**

## 5. freeze

### 5a. freeze.py baseline — 未能按原样完成（环境原因，非版缺陷）

- 命令：`tools/venv/bin/python tools/freeze.py baseline --build production/2026-w47/2026-w47-en-de --core-svg production/2026-w47/2026-w47-en-de/svg --out gates/freeze-final`
- 结果：写 `build-copy/svg/p3-culture.svg` 时 `OSError: [Errno 122] Disk quota exceeded` 中断。`df` 显示文件系统仍有 45G 空闲，属用户磁盘配额（EDQUOT）爆满，与 AGENTS.md 2026-11-10 记载的配额故障同一类。失败的 `freeze-final/`（50M，已删）是我方 scratch，不影响送审成品。
- 等效替代（同一解释器、同一构建源码）：将版目录的构建源（`*.py` + `assets/`，4.3M，不含 PDF/cards）瘦复制到 `gates/rebuild/`，在其中跑 `run.py`（见 §7），再对再生的 8 个 SVG 与送审 `svg/` 逐字节 sha256 比对。

### 5b. 直接 sha256 比对 8/8（等效 freeze baseline）

- `p1-front MATCH`、`p2-life MATCH`、`p3-culture MATCH`、`p4-sport MATCH`、`p5-youth MATCH`、`p6-deep MATCH`、`p7-lang MATCH`、`p8-test MATCH`。**8/8 MATCH**

### 5c. freeze.py diff（core vs edition，只读，通过）

- 命令：`tools/venv/bin/python tools/freeze.py diff --core-svg production/2026-w47/core-en/svg --edition-svg production/2026-w47/2026-w47-en-de/svg --json gates/freeze-diff.json`
- 结果（逐页 +串/−串）：P1 +32/−34、P2 +42/−54、P3 +25/−23、P4 +24/−22、P5 +24/−22、P6 +25/−21、P7 +66/−55、P8 +99/−99；新增 CJK 字符共 9 个，全部为 U+3000。
- 逐条抽查 added/removed 串：新增全部为德语讲解/家具或重排的 P8 答案行；删除的非 CJK 串全部为 core 的英文 gloss-box 片段（P1 数字框、P2 日历框、P1 刊头 strap）、重排的 P8 答案行与 “Translate:”→“Übersetze:”；无英文正文改动。**PASS**

## 6. print/web 文字层一致

- `pdftotext` 两版各 48,076 字节；token 多重集差 0/0；提取文本逐字节相同（sha `abe54433ab93a09c`）。
- web PDF 2,377,924 字节 < 7 MB。**PASS**

## 7. run.py 重跑

- 方式：在 `gates/rebuild/` 瘦复制内跑（见 §5a 说明；不在送审目录内重跑，以免触碰成品）。
- 命令：`tools/venv/bin/python run.py > run.log 2>&1`
- 结果：**exit 0**；`OVERFLOW`/`TOO WIDE` 出现 0 次；全部 flow 末端 y 在底线内：P1-headline 1723/1828、P1-countries 2298/2300、P1-quiz 2491/2560、P2-feature 1467/1540、P2-ex 2532/2560、P3-main 2014/2560、P3-col3 1619/2560、P4-main 1705/2560、P4-col3 1713/2560、P5-main 597/2560、P5-col3 1832/2560、P6-main 2016/2560、P6-col3 1256/2560、P7-main 1833/2560、P7-col3 2357/2560、P8-battery 1418/1555、P8-keys 2290/2560；`TOTAL exercises: 150`；`MODEL words: 82`。**PASS**

## 8. 其他量化核查（本轮自跑，非工具门）

- U+2019 全扫 8 个 SVG：每文件 0，总数 **0**。
- P8 最小字号：`svg/p8-test.svg` font-size 最小值 **13.5pt**（≥ 9.75pt）。
- 徽章：de 与 core 逐页一致（P1 16、P2 15、P3 16、P4 16、P5 16、P6 19、P7 13、P8 23）。
- registry：150 条，A2 62 / B1 66 / B2 22，分版与 KIT 一致；与 core 比 keys 仅差 137–140、150（预期），levels 零差异。
- 可见文本零真实 CJK（仅 U+3000 分隔符；唯一 CJK 字符为非可见 moth `<title>` 三色蛾）。
- model 文 82 词（alphanumeric-token 计）。
- text.md 51,989 字节；ABSTRACT.txt 628 字节、零 ASCII 双引号。

## 门总汇

| 门 | 结果 |
|---|---|
| occlusion（tools/venv） | 0 flags，selftest OK |
| p8 extract | 60/150 noted set，与 core 相同 |
| p8 compare | CLEAN，keydiff 仅 137–140、150（预期） |
| p8 keys vs registry | 150/150（仅 Q150 短标签） |
| freeze 直接 sha256 | 8/8 MATCH（等效瘦复制重跑；原 freeze baseline 因磁盘配额中断，见 §5a） |
| freeze diff | 新增 CJK 仅 9 个 U+3000；无英文正文改动 |
| print/web 文字层 | 各 48,076 字节，差 0/0，字节相同 |
| run.py 重跑 | exit 0，零溢出，150 题，MODEL 82 词 |

机械门全部通过；但目视复校发现 1 条版式缺陷（PROOF-NOTE.md D1：P7 金句出处行孤立到第 3 栏顶部），故本轮结论为 (b) 缺陷清单，非零问题。
