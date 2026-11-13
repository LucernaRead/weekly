# W47 core-fr fix4 复校门禁日志（proof4，独立重跑）

工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-core-fr4/`
（TMPDIR 指向该目录；repo 侧未写任何文件；未 commit、未 push。）
核心源：`~/workspace/weekly-git/production/2026-w47/core-fr/`；工具 Python：`~/workspace/weekly-git/tools/venv/bin/python`。
开工/收尾 SHA 均与任务书一致且未变（见 PROOF-NOTE §一）。

## 1. 探针

- `ls /dev/null` 存在；`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，通。
- 工作区真实写文件：`probe.txt`（`probe-ok`）。
- 磁盘：`df` 66G 空闲（复校期间无配额事件）。

## 2. run.py

- 命令：`tools/venv/bin/python run.py`（核心目录内）
- rc=0，日志零 `WARN/overflow/exceed/error/traceback`。
- TOTAL 150（A2 53 / B1 75 / B2 22；分版 10/15/18/18/17/18/12/42）；P8 battery 终值 1428/1485，keys 流 2046/2560。
- 重跑后 8 页 SVG 哈希与 `final-fr-freeze.json` 逐项相同（确定性重建）。
- 产物：`run-proof4.log`

## 3. freeze.py baseline

- 命令：`tools/venv/bin/python ~/workspace/weekly-git/tools/freeze.py baseline --build . --core-svg svg --out <work>/freeze-proof4 --json <work>/freeze-proof4.json`（核心目录内）
- rc=0，`baseline: 8/8 SVGs byte-identical`，`ok: 8`；核心 SVG 跑后重哈希未变。
- 各页（前 16 位）：p1 `6aad8b4bcdfb975c`、p2 `5709e000bbd7b4d1`、p3 `7828cfe331187278`、p4 `7e46e630eb6b75aa`、p5 `fff2a8d3d7acdaab`、p6 `7af7cf3c240f222b`、p7 `75237d672f20f44b`、p8 `5bee4d4473bfc8a7`（core = produced）。
- 产物：`freeze-proof4.json`、`freeze-proof4.log`、`freeze-proof4/build-copy/svg/*.svg`（8 页产出 SVG 已验与 JSON 一致；其中冗余的 PDF/卡片/素材复本已删，工作区由 50M 减至 7.2M）。

## 4. occlusion_audit.py

- 命令：`tools/venv/bin/python ~/workspace/weekly-git/tools/occlusion_audit.py <core>/svg/`
- rc=0；自检 `selftest OK: planted classes fired {BOXTITLE, COVER, EDGE, FOOTER, LINEX, TEXTX}; clean controls silent`；`0 flags`。
- 产物：`occlusion-proof4.log`

## 5. p8.py extract + compare（本次留存逐字 compare JSON）

- `p8.py extract --p8 svg/p8-exercices.svg --total 150 --json p8-extract-proof4.json`：rc=0，`noted set = 121 of 150 (parse: joined)`。
- `p8.py compare --core-p8 svg/p8-exercices.svg --edition-p8 svg/p8-exercices.svg --total 150 --json p8-compare-proof4.json`：rc=0，`status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[]`（121/121）。
- 独立核对：extract 注记集 == `final-fr-p8.json` 注记集（121 项逐项相同）；extract 键表 150/150 == frozen 键表（含 Q148 `devant le`）。
- 产物：`p8-extract-proof4.json`、`p8-extract-proof4.log`、`p8-compare-proof4.json`、`p8-compare-proof4.log`

## 6. check_mcq.py

- 命令：`tools/venv/bin/python <goals>/hidden_files/w47/scratch-fr/check_mcq.py .`（核心目录内）
- rc=0；`bodies: 45  rendered lines: 1448`；`DEFECTS: 0`；`UNLOCATED: 0`。
- 产物：`check-mcq-proof4.log`

## 7. 印/网文字层 + 网页版检查

- `pdftotext -layout La-Lucerna-VOL4.pdf print-proof4.txt` / `pdftotext -layout La-Lucerna-VOL4-web.pdf web-proof4.txt`：各 102,978 字节；`cmp` 通过，**逐字节一致**。
- `pdffonts`：两 PDF 各 43 个字体对象，全部 `emb=yes sub=yes`；网 PDF 含 `LucernaNewsreader-Bold` ×8 与 `LucernaNewsreader-Italic` ×1 子集（D5 数量见 PROOF-NOTE §六）。
- 网 PDF 2,241,835 B（< 7 MB），8 页，页尺寸与印版同为 1462.5 x 2025 pts。
- 网页版渲染目视：`pdftoppm -png -r 100` P4/P8。
  - P4：注记单行在位、无豆腐块、无字体缺失；Q44–48 选项整组完整；基线独行 `— `一行如旧。
  - P8：对白 `(148)___ cinéma ?` 与答案 `148. devant le（电影院门口）` 在位、无豆腐块、无字体缺失；徽章、写作框、范文、插图均干净。
- 产物：`print-proof4.txt`、`web-proof4.txt`、`web-p4-proof4-4.png`、`web-p8-proof4-8.png`

## 8. 自写综合核验 verify-proof4.py（新鲜代码，非复用 fix4 脚本）

- 命令：`tools/venv/bin/python <work>/verify-proof4.py`（内含 run.py 进程内重跑取新鲜 REG）
- rc=0；**42 项 PASS，0 FAIL**。覆盖：
  - A) Q148：源码行号/键/题干、`.text.md` 1039/1083 行、P8 SVG 对白+答案节点、旧措辞 0 处、REG 映射与 `gnums[3]=148`；
  - B) P4：`expl.py:123`、注记单元素（y=520，实测 344.0px < 378.5px，旧串 387.0px）、旧注记 0 处、8 页对 fix3 build-copy `(x, y, 文本)` 集合比对（仅 P4 去 2 入 1、P8 换 4 行，其余 6 页 0 改动）；
  - C) 孤儿标点 sweep 0；P4/P6 独行 `— ` 与 fix3 基线坐标相同；
  - D) 键四源 150/150、注记三源 121/121、29 道无注题确无印出注；
  - E) 题干 150/150 在 REG 所在页 SVG（含配对组、完形/对白段落、翻译、写作）；
  - F) 徽章 134（50/65/19）；G) §1.1 抽查全过；H) creambox 0 违规；I) P8 最小字号 11.62pt；J) 金句 8/8 逐字。
- 产物：`verify-proof4.py`、`verify-proof4.log`
- 注：脚本初版两个 checker artifact 已修正并全量重跑（RÉPONSES 末条 150 的正则漏检→改分段解析；注记跨元素换行空格→去空白比对；P4 注记宽度误用 sans 15.5px→按元素真实字体 Noto Serif CJK SC 21.5px 重计 344.0px）。详见 PROOF-NOTE §七.3。

## 9. “next Sunday”冻结规则

- `grep -rn "next Sunday"` 于 core-fr 全源码 + `tools/tables.py`：**0 命中**，无适用对象。

## 10. 未做事项

- 未 commit、未 push；未改 repo 侧任何文件（`run.py`/`freeze.py` 重跑均为确定性重建，SVG/PDF SHA 收尾复测未变）。
- 未审 fr 各版（fanout）遗留问题；仅在 PROOF-NOTE §九单列转 re-fanout #2 的提醒。

## 产物清单（工作区内）

| 文件 | 内容 |
|---|---|
| `PROOF-NOTE.md` | 结论 (a) 定稿零缺陷 + 逐项证据 + 缺陷清单（零缺陷）+ 转 re-fanout 提醒 |
| `GATE-LOG.md` | 本文件 |
| `probe.txt` | 开工探针 |
| `run-proof4.log` | run.py |
| `freeze-proof4.json` / `freeze-proof4.log` / `freeze-proof4/build-copy/svg/*.svg` | freeze 8/8 |
| `occlusion-proof4.log` | occlusion 0 flags |
| `p8-extract-proof4.json` / `p8-extract-proof4.log` | p8 extract 121/150 |
| `p8-compare-proof4.json` / `p8-compare-proof4.log` | p8 compare CLEAN（逐字 JSON） |
| `check-mcq-proof4.log` | check_mcq 0/0 |
| `print-proof4.txt` / `web-proof4.txt` | 印/网文字层（逐字节一致） |
| `web-p4-proof4-4.png` / `web-p8-proof4-8.png` | 网页版 P4/P8 渲染目视 |
| `verify-proof4.py` / `verify-proof4.log` | 自写综合核验（42 PASS / 0 FAIL） |
