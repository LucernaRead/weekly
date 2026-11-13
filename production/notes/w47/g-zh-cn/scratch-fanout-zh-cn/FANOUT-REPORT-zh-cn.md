# FANOUT-REPORT zh-cn — W47（第 1 棒，叶子）

## 任务出入（先写清）

任务原文说 zh-cn 核心的读者是 zh-cn，fan-out 10 版（en/de/fr/es/it/pt/nl/ru/ja/ko）。
三处证据一致反对，按 W46 盘点 + brief + 核心 KIT 执行：**核心读者是 en**，
fan-out **9 版：de、fr、es、it、pt、nl、ru、ja、ko**（en 是核心读者故跳过；
zh-cn×zh-cn 同语版 lint 会拦；总数 10 与 W46 盘点相符）。本报告按 9 版记。

## 状态总览（2026-11-11，UTC 约 08:00）

| 版 | 状态 | 双 PDF | 门禁 | 备注 |
|---|---|---|---|---|
| de | **阻塞：磁盘配额**（P8 已修，待重跑构建） | — | run.py RC=0 TOTAL 150；P8 溢出已修未重验实盘 | 见下 |
| fr | 未开始 | — | — | |
| es | 未开始 | — | — | |
| it | 未开始 | — | — | |
| pt | 未开始 | — | — | |
| nl | 未开始 | — | — | |
| ru | 未开始 | — | — | |
| ja | 未开始 | — | — | |
| ko | 未开始 | — | — | |

**完成：0/9 版。** 共享底座已全部落地（见下），de 版卡在配额。

## 阻塞详情（de）

- 约 2026-11-11 07:52 UTC，`p8sim.py` 写 `svg/p1-touiban.svg`（~820KB）报
  `OSError: [Errno 122] Disk quota exceeded`。
- `df`：/home/hatch 150G 总、105G 已用、**45G 可用**——不是磁盘满，是配额
  （EDQUOT；与 2026-11-10 教训一致：须真删东西，可清已入仓的旧
  weekly-* worktree，每约 1.3G；**不在本棒权限内**，须协调员/主 agent 清）。
- 小写仍通：2.4KB 状态文件、7–15KB 的 .py 改写均成功；820KB 写失败。
  据此判断余量在 15KB–820KB 之间，`run.py`（8 个 SVG 共 ~5.7MB）与
  `render.py`（cards PNG + ~41MB 印刷 PDF）现阶段必失败，故未重试。
- 详见 `de/STATUS-BLOCKED.md`。

## de 版已完成的工作

- `transform.py de` 通过：289 行日志，276 ENTRIES + 4 FSTRINGS 全应用。
- 徽章 532.4px（止于 x=620.4 ≤ 888）；页脚间隙 961px；U+2019 全扫 0（.py 层）。
- `run.py` RC=0，TOTAL 150（A2 56 / B1 69 / B2 25；按版 10/18/18/18/18/18/12/38）。
- 唯一溢出 P8-keys：总高 4817.3 vs 容量 4704，超 113.3px；`p8sim.py`
  模拟与实测完全一致。11 条注记串缩短（13 题 2 行→1 行）已落进版内
  content 文件（13 处替换），零写盘模式重验 **0 溢出，末端 y=2521.9，
  余量 38.1px**。盘上 SVG 仍是缩短前的 07:51 旧件，须配额恢复后重生成。

## 共享底座（已落地，不受阻塞影响）

- `tables.py`：276 ENTRIES + 4 FSTRINGS；覆盖断言 276/276（translate ∪
  harvested 减去已注明排除：P1 欢迎词、页脚、3 条 f-string 片段等）；
  最长优先消费模拟 0 未消费；每条九语齐全、无 ASCII `"`、无 U+2019、无换行。
- `fresh.py`：227 条原始，12 处跨文件重复（值全一致）去重后 213 唯一。
- `harvested.json`：W46 收获 63 源，57 条九语齐全；6 条 `p. N` 已按 W46
  前例补 fr/ja/ko/nl 的 `p. N` 原样；`Notes｜` 覆盖为 W47 ｜ 形。
- `transform.py`：已验证可用（de 通过，含删 3 个核心旧件、不拷 cards/）。
- `p8sim.py`：P8 keys 精确模拟器（同 wrap + Flow 数学），支持
  `--no-save` 零写盘模式与 overrides what-if。
- `gen_tables.py`：合并 + 断言 + 模拟生成器，可重跑。

## 恢复后待办（精确）

1. 协调员清配额（清已入仓的旧 weekly-* worktree 或其他已推快照）后，
   探针：写一个 ~1MB 文件确认大写恢复，再动手。
2. de：`run.py`（须 0 溢出）→ `render.py` → `tools/webpdf.py` →
   改编 `export_core.py` 出 `.text.md`（标题 `# 2026-w47-zh-cn-de`）→
   全部机械门（measure、verify TOTAL 150、occlusion 0 flags、p8 抽取
   150/150 且 compare CLEAN、freeze 直接比对 8/8、print/web 文字层一致、
   P8 最小字号 ≥9.75pt、U+2019 扫 0、8 版目视零问题、150 键逐题复核）→
   版内 `WEEKLY-KIT.md` + `de/EDITION-RECORD.md`（门禁日志 + 150 键表）。
3. 按 fr、es、it、pt、nl、ru、ja、ko 顺序逐版：transform → measure →
   build → 门禁 → 目视 → 记录。每版自查零问题才算完成。
4. 终报：9 版逐版一行 + 共性问题 + 核心读者 en 与任务原文出入。

## 关键路径

- scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-zh-cn/`
- 版目录：`~/workspace/weekly-git/production/2026-w47/2026-w47-zh-cn-<lang>/`
- 解释器：`~/workspace/weekly-git/tools/venv/bin/python`（PIL 13.0.0；绝不用系统 python3）

## 第 2 棒补充（2026-11-11，UTC 约 08:00–08:58）

### de 版：SVG 已定稿，卡在配额抖动，只剩最后一轮重建
- 配额断续：08:00/08:54 探针通过，08:52/08:57 探针与写盘失败（EDQUOT；df 105G 已用 / 45G 空闲）。
- run-de-7.log RC=0 TOTAL 150，0 溢出 0 警告；occlusion 0 flags；图片重叠扫描 0 处。
- 5 处缺陷已修进版内文件 + fresh.py（共享表已重跑，276 条 0 缺 0 余）：
  P8 D-head 字号 24→22；P1 截稿行缩短；P4 Hinweise 框 7 行→6 行；P2 "Practice example"
  反向翻译已纠（9 语全改）；P2 日历标题改 "Kalender der Woche"；P7 下期预告条行距 120→112
  （条底 2615.3→2583.3，页脚清）。详情见 de/STATUS-BLOCKED-2.md。
- 目视：P1–P7 通过；P8 待看（cards 未重渲）。
- 待办（恢复后）：render → webpdf → export → 终验（freeze 8/8、p8 CLEAN、文字层差 0、
  P8 字号、U+2019、泄漏）→ P8 目视 → WEEKLY-KIT.md + de/EDITION-RECORD.md。

| 版 | 状态 | 双 PDF | 门禁 | 备注 |
|---|---|---|---|---|
| de | **阻塞：配额抖动**（SVG 定稿，待重建 PDF） | 旧件 | SVG 门禁全绿 | 见 de/STATUS-BLOCKED-2.md |
| fr | 未开始 | — | — | |
| es | 未开始 | — | — | |
| it | 未开始 | — | — | |
| pt | 未开始 | — | — | |
| nl | 未开始 | — | — | |
| ru | 未开始 | — | — | |
| ja | 未开始 | — | — | |
| ko | 未开始 | — | — | |

**完成：0/9 版。** fr 及之后未开始（de 收尾优先于开新版）。

## 第 3 棒（2026-11-11，UTC 约 12:30–16:00）

### de 版审计结论（#3，12:32 UTC）

协调员 12:30 UTC 磁盘实测三件 SHA 与在盘文件逐字节核对一致。结论：**不合格**。

1. 印 PDF（08:51）早于 P7 下期预告修复（`content7.py` 08:54，行距 120→112）：已渲染条底 2615.3，越页脚线 2596。
2. 网 PDF + text.md（08:42）早于 P2/P7 修复，且为 webpdf 补丁前产物（无 Newsreader-Italic）。
3. SVG 为定稿（08:55，run-de-7 RC=0 TOTAL 150）。
4. 第四缺陷：badge strict-CJK 失败——`freeze.py diff --strict-cjk` 新增 CJK = 1（`德` ×1，P1 badge “德语讲解”），SOP 要求 0；W46 zh-cn-de KIT 有同一失效模式与拉丁-only 修复先例。

就地修好：badge 改拉丁-only（de/fr/es/it/pt/nl 拉丁半句原文照录，ja/ko 用 W46 措辞、分隔符 `·`→U+3000）；#2 的 3 处 de 值修复从版文件同步回 `fresh.py`；全套重建（run/render/webpdf/export）+ 全部门禁重跑。最终 de：印 44,829,975 B `e6ed50ab…`、网 2,732,464 B `7fb396f1…`、text.md 50,637 B `8940ba88…`；门禁 11/11 全过，strict-CJK 0，泄漏 0。详见 de/EDITION-RECORD.md。

### 其余 9 版全部完成（10/10）

en 为 identity 版（SVG 与 core 逐字节同，印 PDF 与 core 同 SHA；网 PDF 仅差斜体补丁）。fr/es/it/pt/nl/ru/ja/ko 各修表+版文件后重跑全绿。

| 版 | 印 PDF | 网 PDF | text.md | ABSTRACT | 门禁 | 备注 |
|---|---|---|---|---|---|---|
| de | 44,829,975 `e6ed50ab…65a60` | 2,732,464 `7fb396f1…368` | 50,637 `8940ba88…75b0a` | 305 | 11/11 | 审计后重建；badge 拉丁-only |
| en | 41,763,115 `c34f5a54…05aa`（= core） | 2,652,440 `0e339b6d…5075` | 49,435 `23fb62bd…0bf04`（= core） | 556 | 11/11 | identity；网 PDF 仅斜体补丁差 |
| fr | 42,504,783 `f00a276e…27f4` | 2,663,754 `b7e43796…845c` | 51,829 `fb72ed29…80b` | 333 | 11/11 | 11 处修复（头/日历/P8×8/P4 gloss/P2 词卡） |
| es | 44,799,104 `f05d6126…2508` | 2,723,559 `249ee578…0437` | 51,175 `edc045da…7f482` | 335 | 11/11 | 12 处修复（头/lcn/P4 gloss/日历/P8×7+Q150） |
| it | 41,730,134 `d1ae6f87…a001` | 2,641,804 `75dec91a…a512` | 50,958 `f954151f…ecc4` | 319 | 11/11 | 9 处修复（A 头×5/D 头/日历/P8×6） |
| pt | 41,734,759 `2286485f…4859c` | 2,647,093 `030f52fb…c76fa` | 50,846 `9207974b…4cb71` | 331 | 11/11 | 4 处修复（P4 头/P7 A2 头/lcn/日历） |
| nl | 44,049,080 `f660072c…42e4b` | 2,703,048 `495594dc…efac` | 50,082 `41aa9a39…df2c` | 316 | 11/11 | 12 处修复（头/日历/lcn/诊所行/P8×7） |
| ru | 33,572,611 `7cd883dd…b19b93` | 2,486,444 `ab0aaf10…34f6` | 60,515 `f722ad0f…cd3d` | 426 | 11/11 | 22 处修复；P8 打包分析；P4 gloss 门禁后补修 |
| ja | 36,336,862 `c395a505…4353b6` | 2,900,721 `c620b9ee…ba65a` | 52,444 `68d850ea…dd5e4` | 315 | 11/11 | 守恒门；繁体片名×3；小假名 NO_START |
| ko | 36,966,399 `7a664d88…a3ce` | 2,818,175 `64085a3e…0cdcc` | 52,732 `cce71e99…c904` | 314 | 11/11 | 汉字增量 0/8 页；假名预扫 0 |

（SHA 为前 16 位缩写；完整 SHA 见各版 EDITION-RECORD.md 与 WEEKLY-KIT.md。fr ABSTRACT 由 332 B 补尾换行至 333 B，与其余各版一致。）

### 通用核验（十版一致）

- `run.py` RC=0 TOTAL 150（A2 56 / B1 69 / B2 25；页 10/18/18/18/18/18/12/38），0 溢出；P7 下期预告条底、P8 keys 尾均在 2596/2560 内。
- `gates-zhcn.py` 11/11 全过：occlusion 0、img_overlap 0、p8 extract 150/150、p8 compare CLEAN、freeze_sha256 8/8、印/网文字层 8/8 posdiff 0 msdiff 0、P8 答区最小字号 9.98pt、chips A2 11/B1 24/B2 3 = core、U+2019 0、§1.1 干净。
- strict-CJK：de/en/fr/es/it/pt/nl/ru 均为 0；ja 4648、ko 4040 为预期值（解释层本身为日/韩文），分别由汉字 run 守恒（ja：仅 2 处缺失，均为 badge 家具）与汉字增量 0/8 页（ko）裁决。
- 泄漏扫描（275 源）：十版均为 0 真泄漏；仅 IDENTICAL 渲染（`体育　Sport`、`悬疑 = suspense, b`）。
- 本周金句 8 条各 2 次（正文 + P7）：十版全过。
- 目视：每版 P1/P2/P4/P5/P7/P8 逐页读过（印 PDF 110dpi 渲染），零缺陷。P3/P6 自 transform 起未动。

### 本棒发现的关键问题与教训（写回工具/流程用）

1. **ru P8 打包陷阱（最重要）：** 9 条笔记共省 138.9px 总高，keys 尾仍钉在 2604.2——末列溢出时尾 y = BOTTOM + h(Q150)，前三列省再多也动不了它。必须把 Q150 本身压到 1L，并用 `p8sim.py` overrides 做 what-if 选出能移动列界的组合（ru：Q88/Q107 移列界 + Q145/Q149/Q150）。**`p8sim.py` 的 overrides 路径必须是绝对路径**——它会 `chdir` 进版目录，相对路径在内容跑完后才报 FileNotFoundError，前两次 what-if 实际都没生效（白跑）。
2. **ru P4 gloss 量测 ошиб：** 用英文 “Notes｜” 前缀量得 6 行，实际前缀是 11 字符的 “Примечания｜”，真 7 行、框底 821.9 盖住 GEN，（93%），门禁第一轮才抓到。教训：gloss 永远用该版自己的前缀量，绝不用英文前缀。
3. **ja 繁体片名：** Q76/Q94/Q97 的片名被译成繁体/日式汉字（我們僅有一次的人生 / 珠穆朗瑪：雲中彼岸），与正文 P5 简体片名不一致；守恒检查是唯一抓到它的门。已改回简体。
4. **ko 双11 不用改：** 预扫发现 ko 表里两处 双11（写作提示 + 双11词语卡头），但汉字增量实测 0/8 页——core P8 已有对应汉字计数；共享表的写法没问题，W46 的 “더블 11” 替换先例不适用。
5. **wcn 实串陷阱：** ru 的句式框注是 “Конструкция: …”，不是按规律猜的 “Структура: …”——第一次修复脚本在 fresh/harvested 里都 SKIP，表 diff 只有 15/16 条才发现。修前先 grep 实串，勿凭规律拼。
6. **fr ABSTRACT 尾换行：** fr 文件缺尾换行（332 B），其余九版均为表值 + “\n”；已补为 333 B 统一。
7. **VM 重启中断恢复：** ru 重建链被重启杀在 webpdf 写入前（日志停在字体列表、无 WROTE 行），网 PDF/text.md/门禁均未完成；凭磁盘 SHA + 日志尾行确认中断点后重跑三步。另：ru webpdf 实际日志为 webpdf-ru.log（15:01，初版）、webpdf-ru-2.log（15:25，664 B，中断）、webpdf-ru-3.log（15:31，727 B，成功重跑）。

### 缺陷类小结（本棒 6 版新修，fr/es 沿用 #3 前半段记录）

- 头超长：it A 头×5 + D 头；pt P4 C 头 + P7 A2 头；nl P4 C 头 + P8 D 头；ru A 头×5 + P4 C 头 + P8 D 头（俄语最宽，候选逐一实测）。
- P7 下期预告压页脚：es/pt（lcn 减 1 行）、nl（lcn + 诊所行各减 1 行，2641.82→2586.30）、ru（wcn + 诊所行×2 各减 1 行，2670.82→2588.78）。
- P2 日历标题进山谷照：it/pt/nl（各缩短）；ru/ja/ko 天生合。
- P2 词卡例句 2 行出框：fr、ru 各 1 张；其余版实测均为 1 行。
- P4 注释框 7 行盖 GEN，：fr/de/ru（ru 详见上）；it/pt/nl/ja/ko 6 行天然合。
- P8 keys 溢出：fr/es/it/nl/ru（ru 两轮，见打包陷阱）；pt/ja/ko 天生合。

### 交付物

- 十版成品：`production/2026-w47/2026-w47-zh-cn-{de,en,fr,es,it,pt,nl,ru,ja,ko}/`（8 SVG + 印/网 PDF + .text.md + ABSTRACT.txt + WEEKLY-KIT.md，KIT 均为本棒重写版）。
- 每版 EDITION-RECORD.md + 全套日志在 scratch 各语子目录（`it/`、`pt/`、`nl/`、`ru/`、`ja/`、`ko/`；de/en/fr/es 沿用既有）。
- 共享工具：`conserve_ja.py`（ja 汉字 run 守恒）、`hanzi_ko.py`（ko 汉字增量）、`p8-overrides-ru2.json`（ru what-if 组合）。
- 共享表：`tables.py` 276 条 + 4 FSTRINGS，最终状态 0 缺 0 余 0 未消费；全部修复均已进表（表能精确复现每版）。

**完成：10/10 版。** 未 commit、未 push、未 insert、未跑 lint。独立校对仍欠母线。
