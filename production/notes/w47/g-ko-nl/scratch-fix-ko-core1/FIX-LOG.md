# FIX LOG — W47 core-ko fix1 (run 11)

- 任务：core-ko 已定稿（run 10），ko-en / ko-de 两轮 fan-out proof1 共同查出核心层缺陷 D2/D3/D4，修核心、全家重扩。本轮只修 D2、D3、D4；不碰 fan-out 各版、不碰 textmd.py、不碰其他家庭。
- 对象：`production/2026-w47/core-ko/`（run 10，印刷 `Lucerna-VOL4.pdf` 46,232,169 B，SHA-256 `7b004b36066254d7e1e25e92fb81c39428df36a28af182c2b1ad2ab1545aeb5e`；网版 `Lucerna-VOL4-web.pdf` 4,232,790 B，SHA-256 `e9c1ca0ce22d31ed36ee70469a839ed09f7eca60e1bbd05a6b179b5dc818fbfa`；text.md 26,014 B / 333 项）。任务书所称 `Lucerna-VOL4-KO-ZH-CN.pdf` 为仓内 slug 命名，盘上实为 `Lucerna-VOL4.pdf`（字节数与 KIT 一致，已核实）。
- 依据：SOP.md §8 + §1.1 全文、AGENTS.md、协调员 brief（`hidden_files/w47/briefs/brief-coordinator.md`，注：任务书所写 `~/workspace/weekly-git/hidden_files/...` 路径不存在，实际位置在 goals hidden_files/w47/briefs/ 下，已按实读）、`scratch-proof-ko-en1/PROOF-NOTE.md`、`scratch-proof-ko-de1/PROOF-NOTE.md`。
- 探针（开工）：`git hash-object -w` 正常（e69de29b…，空输入）；笔记目录 `scratch-fix-ko-core1/` 可写（PROBE.txt 已写）；`df` 显示 /home/hatch 可用 45G。未遇 EDQUOT。
- 环境锁定（沿用 run 10 结论，KIT fix #15）：构建（run.py / check_core / check_gloss / textmd）一律 `/usr/bin/python3`（PIL 10.2.0）；渲染（render.py）与 webpdf 用 `tools/venv/bin/python`（cairosvg/fontTools）。freeze 门亦用 `/usr/bin/python3`（与 build 同解释器）。
- 未跑 insert.py、lint --write，未做任何 git 写操作。叶子，未派 subagent。

## 动手前逐字核实（全部属实）

- D2：`grep -n '어디예요'` — `content12.py:157` 与 `content34.py:199` 均为 `한국시리즈에서 우승한 팀은 어디예요? A. 삼성 · B. kt wiz · C. LG`。어디 问地点，不问哪支队。答案 A. 삼성 两处皆无误，只改题面疑问词。
- D3：`grep -n '시리즈 시리즈'` — `content34.py:201` 为 `한국시리즈 시리즈 전적은 어떻게 돼요? A. 3승 2패 · B. 3연승 · C. 4승 1패`。答案 C. 4승 1패 无误，只改题面。
- D4：`grep -rn '수능 후에 김치의 날이 와요' production/2026-w47/core-ko --include='*.py'` 只命中两处：`content7.py:80`（`wt` 框架例句 `'수능 후에 김치의 날이 와요.'`）与 `content7.py:130`（金句 #7 `「수능 후에 김치의 날이 와요」…(7면)`）。P1–P6 任何文章均无此句，违反 SOP §4（P7 金句必须摘自本期自己的文章）。
- D4 替换句核实：`수능이 끝나면 일요일 11월 22일에는 김치의 날이 와요` 逐字见于 `content12.py:39` P1 lead_para（`f.lead_para(...)`，P1 头条首段）与 `2026-w47-ko-zh-cn.text.md:27`。所在页确为 P1，故金句出处标注改为 (1면)。其余 7 条金句不动。
- ko-en fix1 的 D2 也用同一句，已另行知会（本轮只负责 core）。

## 修复（改前 → 改后）

### D2 — 疑问词 어디 → 어느 팀（两处同步）
- `content12.py:157`（P1 ex 10，A2 单选，答案 A. 삼성 不变）：
  - 改前：`한국시리즈에서 우승한 팀은 어디예요? A. 삼성 · B. kt wiz · C. LG`
  - 改后：`한국시리즈에서 우승한 팀은 어느 팀이에요? A. 삼성 · B. kt wiz · C. LG`
- `content34.py:199`（P4 ex 47，B1 单选，答案 A. 삼성 不变）：
  - 改前：`한국시리즈에서 우승한 팀은 어디예요? A. 삼성 · B. kt wiz · C. LG`
  - 改后：`한국시리즈에서 우승한 팀은 어느 팀이에요? A. 삼성 · B. kt wiz · C. LG`

### D3 — 시리즈 重复删除
- `content34.py:201`（P4 ex 48，B1 单选，答案 C. 4승 1패 不变）：
  - 改前：`한국시리즈 시리즈 전적은 어떻게 돼요? A. 3승 2패 · B. 3연승 · C. 4승 1패`
  - 改后：`한국시리즈 전적은 어떻게 돼요? A. 3승 2패 · B. 3연승 · C. 4승 1패`

### D4 — P7 金句 #7 换为 P1 原文（两处同步，出处 (7면) → (1면)）
- `content7.py:80`（`wt` 框架例句）：
  - 改前：`「〜 후에」 — '수능 후에 김치의 날이 와요.' 나중에 하는 일을 말할 때 쓰는 틀이에요. 물어볼 때는 '〜 후에 뭐 해요?'라고 해요.`
  - 改后：`「〜 후에」 — '수능이 끝나면 일요일 11월 22일에는 김치의 날이 와요.' 나중에 하는 일을 말할 때 쓰는 틀이에요. 물어볼 때는 '〜 후에 뭐 해요?'라고 해요.`
- `content7.py:130`（金句 #7，中文释义 `高考之后就是泡菜日。` 不变，仍贴切）：
  - 改前：`("「수능 후에 김치의 날이 와요」", "高考之后就是泡菜日。", "7면")`
  - 改后：`("「수능이 끝나면 일요일 11월 22일에는 김치의 날이 와요」", "高考之后就是泡菜日。", "1면")`

## 重建（run 11）

构建（全部 `/usr/bin/python3`，PIL 10.2.0；渲染/webpdf 用 `tools/venv/bin/python`）：

- `run.py` → `build-run11.log`：exit 0，**0 FLOW OVERFLOW / 0 HEAD TOO WIDE**；TOTAL **150**（A2 51 / B1 72 / B2 27；逐页 10/18/18/18/18/18/12/38）。P1-headline flow 终点 y=1814（与 run 10 同），P4-ex 终点 y=2053（同），P7 col3 ends 1805.7（同——框架例句虽加长 12 字，折行数不变），P7 photo ends 1631.8（同），P7 teaser ends 2547.7（页脚线 2580，余 32.3px，同 run 10）。
- `render.py`（venv）→ `render-run11.log`：8 张 cards + 印刷 PDF。
- `tools/webpdf.py svg/ Lucerna-VOL4-web.pdf`（venv）→ `webpdf-run11.log`：exit 0，49,451 文本字节。
- `textmd.py . 2026-w47-ko-zh-cn 2026-w47-ko-zh-cn.text.md "Lucerna Korean Weekly VOL.4 — Korean text, Chinese explanations (2026-W47)"`（系统 python3）→ `textmd-run11.log`：8 页，333 项（项数不变）。
- SVG 哈希（`svg-hashes-run11.txt`）：仅 p1/p4/p7 变——p1 `00227ca1…`、p4 `d997631e…`、p7 `14b7cf13…`；p2/p3/p5/p6/p8 与 run 10 逐字节同（`faf9e3c5…` / `b447a559…` / `09f7fc23…` / `d45b0355…` / `e88f7d42…`）。
- 旧句全版清零：8 个 SVG 中 `어디예요` / `시리즈 시리즈` / `수능 후에 김치의 날이 와요` 出现 0 次；新句：P7 新句在 p7 文本节点中恰好 2 次（框架例句折两行 + 金句 #7 单行），`어느 팀이에요` 2 次（P1+P4），`한국시리즈 전적은` 1 次（P4）。
- 目视：4 张改动处放大裁图（`work/p1-ex10.png`、`p4-ex47-48.png`、`p7-frame.png`、`p7-phrase7.png`）全部干净——题面单行/正常折行、无溢出、无压线；P7 整版（`cards/p7-mal.png`）目视无溢出/重叠/压页脚，金句 #7 右栏单行 + `(1면)`，框架例句框内 4 行完整。

## 新双 PDF 字节数 / SHA（run 11，最终成品）

| 文件 | 字节数 | SHA-256 |
|---|---|---|
| 印刷 `Lucerna-VOL4.pdf`（run 10：46,232,169 B）| **46,232,227 B**（+58） | `53bf14edeca05f9db56e699b5d826f50c320eebcce200c4b876b394de21a2f27` |
| 网版 `Lucerna-VOL4-web.pdf`（run 10：4,232,790 B）| **4,232,878 B**（+88，< 7 MB） | `9592945ae188dc8e50394fcab1ded155baaff63161bcf0b5f7ecbc6898c43bc7` |
| text.md `2026-w47-ko-zh-cn.text.md`（run 10：26,014 B / 333 项）| **26,048 B**（+34）/ 333 项 | `ba1b80f8edabc76eac398e34e80718254e1e584966a39a7c5a9a504b5fe9dda3` |

## 机械门（全绿，详见 GATE-LOG.md）

- occlusion 审计：venv 与系统 python3 各 **0 flags**（自检 6 类全触发）。
- p8 extract：**150/150**；p8 compare（core 对自身）：**CLEAN**（missing=[] extra_count=0 keydiff=[]）。
- freeze baseline（`/usr/bin/python3`，与 build 同解释器）：**8/8 逐字节一致**，core integrity 确认 shipped SVG 未变。首次跑 2 秒即异常退出 120 且日志为空（进程被外部中断，无文件损坏）；原样重跑一次即 8/8，逐文件 OK，产物在 `freeze-run11/svg/`。freeze diff run10→run11：仅 p1/p4/p7 有字符串增减（p1 +2/−2，p4 +4/−4，p7 +6/−6；其余 5 页 +0/−0），新增 CJK 全为新句字（끝/일/월/면/는/나 + 어느 팀이에요 的 이/에/팀/느），无任何计划外字符串。
- 文字层：print 与 web 各 **49,451 字节，逐字节一致**（`cmp` 通过；run 10 为 49,379，+72 来自三处加长题面/例句）。
- U+2019 全扫：SVG 8 页 + text.md + ABSTRACT.txt 均为 **0**（U+201C/U+201D 同为 0）。
- check_core（系统 python3）：gloss fails **0**，P7 金句 **8/8 verbatim**（新 #7 已通过工具核验为 P1 原文），orphan issues **0**，日期全对。check_gloss：10 项，与 run 10 日志逐字节同（已裁定类，未变）。
- P8 答案区最小字号 9.975pt（162 spans，与 run 10 同；P8 未改）。

## 未动项

- 未碰 fan-out 各版、未碰 textmd.py、未碰其他家庭；WEEKLY-KIT.md 未改（本轮记录以本 FIX-LOG 为准，KIT 由协调员/后续轮次统一更新）。
- 未跑 insert.py、lint --write，未做任何 git 写操作。工作树内 W43/W45 的脏改动为其他线预先存在，本轮未碰。
- 叶子，未派 subagent。本轮交付后待协调员另派核心 re-proof 与全家重扩。
