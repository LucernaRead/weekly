# FIX-LOG — 2026-W47 core-pt fix2（P4 译注 `o título 冠军` → `o título 冠军头衔`，re-proof D5）

修复员：core-fix（2026-11-11）。工作目录：`~/workspace/weekly-git/production/2026-w47/core-pt/`；
scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-core-pt2/`。
探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9…` RC=0；
scratch 写 `PROBE.txt` 成功。TMPDIR 全程指向 scratch 下 `tmp/`，系统 /tmp 未作输出。
构建解释器全程 `tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）——未用系统 python3
跑任何构建或复测（追加约束）。
正典 creambox：`hidden_files/w47/tools/creambox.py`，md5 `ee7a55d8b2057cf4ad42a97bb1197383` ✓。

## §0 版身份核对（磁盘为准，修复前）

| 文件 | 修复前字节数 | 修复前 SHA-256 | 修复后字节数 | 修复后 SHA-256 |
|---|---|---|---|---|
| `A-Lucerna-VOL4.pdf`（印） | 25,311,644 | `98f44af82f82df7c7fec1014fff7098d0448bf775b2aeda484f2e69233235181` | 25,312,258 | `4b58f4dfec2245f77dbb57b53c58cbab4913fdc85e4cf8566d706d4d3ec141b6` |
| `A-Lucerna-VOL4-web.pdf`（网） | 1,608,359 | `d1d26cd70823e83e6165268b055b481981cd5cc3bdcffaec40042f7bf28a521f` | 1,609,033 | `9f2d70e5404a964d303182faae69b4884e46dbcc168a632323fb2bff61a2a7b5` |
| `2026-w47-pt-zh-cn.text.md` | 36,876 | `9dd550b6d7d19703ce6643357e9aad3f5367dfc40379bd41d56db999fd36afbe` | 36,882（仅 215 行） | `3cd3793f198a40d8c4b895275bbce9c6593168eeb93ae2e7fea7ce0e7f4fbce2` |

- 修复前三件磁盘值与 fix1 记录的修复后值逐字一致（基线已核）。
- KIT §6 已按磁盘更新：网 PDF 1,609,033 B / SHA `9f2d70e5…`；印 PDF 25,312,258 B /
  SHA `4b58f4df…`；text.md 36,882 B / SHA `3cd3793f…`；freeze  bullet 更新为工具直报 8/8。
- 工作树内他人的改动（`2026-w47-it-es`、`core-nl/content34.py`、`fanout-nl`、`tools/*.py`、
  `issues/2026-w43/*`）均未碰；本次 commit 只含 core-pt 三文件（见 §7）。

## §1 改了哪一行（旧值 → 新值）

| # | 文件 | 旧值 | 新值 | 说明 |
|---|---|---|---|---|
| 1 | `content34.py:134` | `… · o título 冠军 · a pausa …` | `… · o título 冠军头衔 · a pausa …` | D5：P4 gloss 译注消歧，只加“头衔”二字 |
| 2 | `2026-w47-pt-zh-cn.text.md:215` | `*译注｜… o título 冠军 · a pausa …*` | `*译注｜… o título 冠军头衔 · a pausa …*` | 由导出器重生成同步更新（未手改），全文件仅此一行改动 |

- 改动依据（协调员已从磁盘核实）：文中 `o título` 凡 9 处皆指头衔/冠军
  （`o sexto título`、`o título de construtores`、`o jogo do título` 等），“人”义无一处成立；
  歧义已实证传播到 8 个 fanout 版（fr champion、de Meister、es campeón、it campione、
  nl kampioen、ru чемпион、ja 優勝者、ko 우승者——各版 text.md 已核实；fanout 版修正不在本轮，
  协调员另行处理）。
- 除上表两处外无任何源文件改动。文案其余、题键、字数结构不动。

## §2 text.md 导出路径（未手改的证据）

- 仓库与 scratch 均无 pt 专用 text.md 导出器；`tools/` 无文本导出器；`tools/insert.py`
  称 text.md “exported from the source manuscript”；仓库 `AGENTS.md` 规则 4：正文由生产源导出，
  **绝不从 PDF 倒抽**。pt KIT 第 3 轮注称其 text.md 行曾手改同步——正是任务禁用的绕过。
- 既定先例（其余核心）：记录桩导出器——core-en `scratch-en/make_textmd_w47.py`、core-de
  （预修导出与已入仓版逐字节同 SHA 验证）、core-it `export_w47_textmd.py`。
  本轮依同法新建 `scratch-fix-core-pt2/make_textmd_pt.py`：以桩 `bslib4` 替换执行 content 文件，
  记录每条渲染字符串（真实 `svglib.wrap`/`text_w`，同 venv PIL/字体，故 Flow y/栏位数学与真构建一致），
  再按从源码调用与已入仓 text.md 逐行比对恢复的版式规则拼合（规则全写于文件 docstring）。
- **验证（改源码前）**：导出器输出与修前已入仓 text.md **逐字节相同**（36,876 B，
  SHA `9dd550b6d7d19703ce6643357e9aad3f5367dfc40379bd41d56db999fd36afbe`，`export-pre.log` 记
  MATCHES PRE-FIX；scratch 保留该份预修导出副本）。桩 Flow 的 P8 流末 y=878.9、栏 3/3，
  与真构建完全一致；150 题（A2 48 / B1 71 / B2 31；分版 10/18/18/18/18/18/12/38），范文 88 词。
- **改后重导出**：同一导出器写 core 内 text.md，`git diff` 仅 215 行一处改动（+“头衔”二字，+6 字节）。
  导出器留于 goals 侧 scratch（同 core-en/de/it 先例），不入仓。

## §3 重建与确定性

- `run.py`：RC=0，无 `FLOW OVERFLOW` / `!!`；150 题（A2 48 / B1 71 / B2 31；
  分版 10/18/18/18/18/18/12/38）；范文 88 词；P8 练习流末 y=878.9、图末 1238.35（与 fix1 相同）。
- `render.py`：8 卡片 + 印 PDF；**三跑印 PDF SHA 相同**
  （`4b58f4df…`，25,312,258 B）——确定性已验。
- `webpdf.py`：网 PDF 1,609,033 B，文字层 44,487 字节。网 PDF 逐跑 SHA 不定
  （fontTools 子集化流的字节级非确定性，见 fix1 FIX-LOG §3）；本次以磁盘现行文件 SHA 为准（§0 表）。
  文字层比 fix1 的 44,481 字节多 6 字节 = 新增“头衔”二字（UTF-8 6 字节），一致。

## §4 全部门禁（实跑结果）

| 门 | 命令 / 方法 | 结果 |
|---|---|---|
| gates_core.py | `tools/venv/bin/python gates_core.py` | **16/16 PASS**，FAILURES: none（同基线碰撞 0；页框墨迹穿越 0，最小边距 L/R/T/B = 47.0/47.9/35.0/33.0；P6 图表覆盖 0%；P7 引言 8 条各 2×；P1 头条 41 字符） |
| occlusion 审计 | `tools/occlusion_audit.py . --json <scratch>/occlusion-fix2.json` | 自检阳性对照 6 类全触发；**0 flags** |
| creambox 全版 | 正典 creambox.py，`svg/*.svg` | **31 框，0 真溢出**（§5；其余 BELOW-WINDOW 仅 6 处已知假阳性 +32…+42px 下块标题；inside-only desc-clear 负值 6 处均为已知误报：中文行/“2027.”无降部字母，PIL 墨底 = 基线 −1px） |
| p8 extract | `tools/p8.py extract --p8 svg/p8-avaliacao.svg --total 150` | **150/150** |
| p8 compare | `tools/p8.py compare --core-dir . --edition-dir . --target pt --total 150` | **CLEAN**，missing=[]，keydiff=[] |
| freeze baseline | `tools/freeze.py baseline --build . --core-svg svg --out <scratch>/freeze-fix2` | **8/8 SVGs byte-identical**（repointed files: none；venv Pillow 13.0.0 / FreeType 2.14.3；core 完整性 8 文件重哈希无改动） |
| freeze diff | `tools/freeze.py diff --core-svg svg --edition-svg svg` | +0/−0，新增 CJK 0 |
| freeze_direct | （任务原列） | **无此子命令**：`tools/freeze.py` 仅 baseline/diff；以 baseline 8/8 + diff 自比为 freeze 证据，不拦停 |
| keycheck | 印 PDF RESPOSTAS（-layout 单版抽取）与 text.md 附录逐项比对 | **150/150**：149 项正则逐字一致；Q140 因版式换行（“— 祈使式…”折到下一行）手工核对逐字一致；Q150 仅 ✓ 标记提取 artifact（`150. ✓ 范文见本版 H 区（88 词）`，与 fix1 同类 artifact） |
| 印/网文字层比对 | pdftotext 两版 | 各 44,487 字节、7,263 词，**逐字相同**（词多重集差 0）；8 页，1462.5×2025pt |
| P8 最小字号 | PyMuPDF span，全版 | **10.12pt**（全版最小亦为 10.12pt，仅在 P8），高于 SOP §1.1 下限 9.75pt |
| 弯引号扫描 | 印/网 pdftotext | U+201C/U+201D 各 **3**（P7 gloss 1 对 + E139/E140 两对，印/网一致）；U+2019 **0**；«» 各 40 |

## §5 P4 gloss 盒实测（重点）与 fix1 四项回归

### D5：P4 gloss 盒（x=989，y=270.48，w=422.5，h=145.675；内宽 386.5px）

| 行 | 修前 PIL 宽 | 修后 PIL 宽 | 修后内宽余量 | 末行 |
|---|---|---|---|---|
| L1 `译注｜o agregado 总比分 · os pênaltis` | 367.7 | 367.7 | +18.8 | — |
| L2 `点球大战 · a decisão 决赛 · o título 冠` | 370.7 | 370.7 | +15.8 | — |
| L3 `军头衔 · a pausa 休整期 · a taça 奖杯。` | 342.4 | 383.4 | **+3.1** | 末行 |

- **未新增换行**：修前修后均为 3 行（真实 `svglib.wrap` 量测，20.5px sans，内宽 386.5px）。
  两字只落在末行 L3：PIL 宽 342.4 → 383.4px（+41.0px），内宽余量 44.1 → **+3.1px**。
- 纵向余量不变：末行基线 368.4、框底 416.2，creambox clearance **+47.7px**
  （desc-clear +41.6）——与修前相同（任务所称“现余量 +47.7px”即此口径）。
- Cairo 渲染 PNG 实测（`p4-fix2.png`，cairosvg 1950×2700，与 render.py 同参数）：
  L1/L2/L3 墨右缘 1381/1383/1387，距框右缘 1411.5 余 **30.5/28.5/24.5px**；
  墨底 372、距框底 **44.2px**。注：此 sans 文本 Cairo 实测并不比 PIL 宽
  （L3 PIL 预测右缘 1390.4，实测 1387）——fix1 D7 的“+3%”是 Newsreader serif 的实测，
  不适用于此框；以渲染实测为准，框内，无溢出。

### 回归：fix1 四项（PNG 真墨，与 fix1 §5 值比对）

| 缺陷 | 末行 | 修复后框底 | 修复后墨底 | **墨底 clearance** | creambox（基线口径） |
|---|---|---|---|---|---|
| D1 | `em Brasília. (Página 4)`（20px，基线 2327.6） | 2348 | 2331（墨迹行 2313–2331） | **+17px**（fix1 +16；阈值差 1px，无回退） | inside-only +20.4，desc-clear +14.4 |
| D2 | `16h30.`（21.5px，基线 540.6） | 551 | 540（墨迹行 526–540） | **+11px**（与 fix1 一致） | +10.4，desc-clear +3.9 |
| D3 | `Página do Participante.`（21px，基线 840.8） | 854 | 845（墨迹行 …–845，降部尾 841–845） | **+9px**（与 fix1 一致） | +13.2，desc-clear +6.9 |
| D7 | 范文 10 行（15pt） | —（栏宽 422.5 不变，wrap 395 不变） | 10 行墨右缘 1722–1840 | 距 1862 余量 **22…140px**（最紧 22px，与 fix1 一致） | — |

## §6 其他核查

- P8 练习流末 y=878.9、图末 1238.35、图高 250 均与 fix1 相同；全版重扫：creambox 0 真溢出；
  occlusion 0 flags；gates 碰撞/穿越 0（见 §4）。
- `__pycache__` 与 svg/cards/PDF 不入仓（W46 core-pt 348 个已入仓文件含 0 个 svg/cards/pdf/png；
  渲染件由源码可复现）。本次 commit 只含源码 + KIT + text.md（§7）。
- 导出器 `make_textmd_pt.py` 与本日志、导出前后日志（`export-pre.log`、`export-post.log`）、
  门禁日志均留于 goals 侧 scratch，不入仓。

## §7 commit（只 commit、不 push）

- Commit：`d2b0e182af264d0d5196f04a752d362b6eb4baad`（本地，未 push；`main...origin/main [ahead 1]`）。
  前一 HEAD 为 `f11854bf`（core-ru fix1，另一修复员的 commit；本次提交时 HEAD 由 fix1 的
  `4b688318` 前进至此，本次改动文件无重叠）。首次 commit 曾因仓库 index 锁（另一进程正在提交）
  失败，查无残留锁文件、无运行中 git 进程后重提成功；未删锁文件。
- 包含文件（仅此 3 个）：
  - `production/2026-w47/core-pt/content34.py`（134 行一处改动）
  - `production/2026-w47/core-pt/2026-w47-pt-zh-cn.text.md`（215 行一处改动）
  - `production/2026-w47/core-pt/WEEKLY-KIT.md`（§6 尺寸/SHA + §8c fix2 条目）

## §8 结论

D5 已修复：`o título 冠军` → `o título 冠军头衔`，源码一处、text.md 一处（导出器重生成，
改前逐字节复现验证通过）；P4 gloss 盒仍 3 行，末行渲染墨迹距框右缘 24.5px、纵向余量 +47.7px，
无换行、无溢出；fix1 四项 D1/D2/D3/D7 回归值与 fix1 一致（D1 +17px  vs +16px 为阈值差，无回退）；
全部门禁一次通过，无新增缺陷。三件新 SHA 见 §0 表。本地 commit 已做（`d2b0e182`，只 commit、不 push）。
