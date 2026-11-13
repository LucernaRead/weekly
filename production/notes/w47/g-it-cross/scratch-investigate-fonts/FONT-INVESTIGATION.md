# W47 字体调查 — FONT-INVESTIGATION.md

**调查员**：字体调查子代理（subagent），2026-11-11
**范围**：只调查，不修不改。不改机制代码、不重渲染生产文件、不 commit、不 push。全部验证写在 goals 侧 scratch：
`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-investigate-fonts/`
**探针**：`git hash-object -w --stdin` 通（`9daeafb9…`）；goals 侧 scratch 写文件通；TMPDIR 指向 goals 侧 `tmp/`。
**当前 VM**：2026-11-11 11:25 UTC 重启（调查时 `up 10 min`）；pt-ko 构建与 proof1 均在上一台 VM（04:25 boot）上跑。

---

## 结论总览

| 问题 | 结论 |
|---|---|
| **Q1 pt-ko O1 字体度量漂移** | **(i) 漂移源已找到**。不是交付后环境变了，而是**同一台机器上有两个 Python/Pillow/FreeType 栈，量同一字体得数不同**。pt-ko 的 run1/run2/run3 是用 **系统 python3（Pillow 10.2.0 / FreeType 2.13.2）**跑的；freeze 工具、proof1、以及本次全部复跑用的都是 **tools/venv（Pillow 13.0.0 / 内置 FreeType 2.14.3）**，后者把韩语词间空格量宽约 +1.11px（20px 字号），导致 4 处韩语断行变化。系统 python3 复跑与交付 SVG **8/8 字节一致**，已证实。重建安全**当且仅当**用交付时那个解释器（系统 python3）；用 venv 重建会悄悄改写 4 处断行，必须当作版式变更重校。 |
| **Q2 讲解层字体违反 SOP §1.1** | **全家族级，属实**。机制在 `svglib.py`：`kind="sans"` 的分支从不查 Newsreader/Noto Sans，任何落在 Noto Sans CJK 字符集里的字符（含全部拉丁字母、西里尔字母）都直接判为 `Noto Sans CJK (SC/JP/TC/KR)`。抽查 8 个已建家族的拉丁读者版，讲解层拉丁元素一律是 CJK SC/JP/TC/KR 而非 Newsreader；俄语读者版（非 ru 目标）讲解层也是 CJK SC 而非 Noto Sans。es/nl/ja 三族 W47 尚无一版建成，结论来自机制（其 core svglib 的 sans 链与 en 完全相同；ja/ko core 甚至完全没有 Newsreader）。已发 W43/W45/W46 的 PDF 字体表同样证实（见 §Q2.4）。 |

---

## Q1 — pt-ko O1：漂移源与重建安全性

### Q1.1 结论：(i) 找到漂移源，重建有条件安全

- **漂移源**：双解释器栈。交付 SVG 由系统 python3 建成；全部复跑（freeze、proof1 direct-run、本次 3 次复跑）由 venv python 建成。两个栈量同一字体文件得数不同。
- **重建安全条件**：用 `/usr/bin/python3`（Pillow 10.2.0 / FreeType 2.13.2）重跑 `run.py`，与交付 SVG **8/8 字节一致**（本次在 scratch 副本实测，见 Q1.3）。用 `tools/venv/bin/python` 重建**不安全**——会在无任何源码改动的情况下改写 P2/P3/P4/P7 四处韩语断行 + 每页 1–5 处右对齐/居中元素坐标 ±1–5.4px（proof1 的 freeze 0/8 与此完全一致）。
- **不是交付后漂移**：freeze 工具在构建当天 05:17–05:19（run1 05:14 之后、run2 05:20 之前）就已经 0/8，且其 build-copy 产物与 proof1 11:02 的复跑、本次 11:35 后的复跑**字节完全一致**。字体文件、包版本在交付前后没有证据显示变化（见 Q1.4 排除清单）。KIT 记录的构建命令（`tools/venv/bin/python -u run.py`）与实测不符——实际跑 run1–run3 的是系统 python3（或等效栈）；KIT 此处记录有误，须更正。

### Q1.2 时间线（UTC，2026-11-11）

| 时间 | 事件 | 结果 |
|---|---|---|
| 04:25 | VM 开机（构建与 proof1 共用的那台） | — |
| 05:13:48–49 | 全部 `.py` 写入版目录（仅 gates.py/make_gates.py 在 05:17:05–06） | 源码定稿 |
| 05:14:10 | ko-run1（版目录内） | 交付 SVG 的第一版 |
| 05:17–05:19 | freeze 工具 baseline：复制版目录到 `ko-freeze1/build-copy` 重跑 | **0/8**（与交付不同；build-copy 产物存留至今） |
| 05:20:27 | ko-run2（版目录内） | 哈希 = 交付 SVG（`ko-svg-run2.txt`） |
| 05:22:18–37 | ko-run3 / 交付 SVG 落盘；05:22:37 run3 日志 | 交付件 |
| 05:37 | WEEKLY-KIT.md 写入（称 build 命令为 venv python，称 DIRECT 8/8） | 记录 |
| 11:02 | proof1 direct-run（scratch 副本，两次） | 两次彼此字节一致，与交付 **8/8 不同** |
| 11:25 | **VM 替换重启** | 本次调查在新 VM 上 |
| 11:35 后 | 本次复跑（venv ×2、系统 python3 ×1、pt-fr/en-fr 抽查） | 见 Q1.3 |

关键点：**同一 boot、同一 venv、同一源码**，05:14/05:20/05:22 在版目录内跑得交付字节，05:17 在副本里跑得另一组字节——变量不在时间、不在 VM、不在源码，只在**调用解释器**。

### Q1.3 复现矩阵（本次实测，scratch 副本，只写 goals 侧）

| 复跑 | 解释器 | 与交付 SVG | 与 proof1 direct-run / freeze build-copy |
|---|---|---|---|
| freeze build-copy（构建时，05:17） | venv（freeze 工具调 `sys.executable`） | 0/8 | —（基准） |
| proof1 direct-run ×2（11:02） | venv | 0/8 | 与 freeze build-copy **8/8 字节一致** |
| 本次 run-nocache（`cp -r` 副本） | venv Pillow 13.0.0 / FreeType 2.14.3 | 0/8 | 8/8 一致 |
| 本次 run-withcache（`cp -rp` 副本，含版目录原 `__pycache__`） | venv | 0/8 | 8/8 一致 |
| **本次 run-syspy（`cp -r` 副本）** | **系统 python3 Pillow 10.2.0 / FreeType 2.13.2** | **8/8 字节一致** | — |
| pt-fr 抽查（venv） | venv | 8/8 一致 | —（pt-ko 是孤例，见 Q1.5） |
| en-fr 抽查（venv） | venv | 8/8 一致 | — |

复跑产物在 `scratch-investigate-fonts/run-nocache/`、`run-withcache/`、`run-syspy/`、`blast-2026-w47-pt-fr/`、`blast-2026-w47-en-fr/`（均为 scratch，未动生产文件）。

### Q1.4 决定性测量：同一字符串，两个栈得数不同

测量的是交付 SVG 里真实元素的字符串（`svglib.text_w` / PIL `getlength`，NotoSansCJK-Regular.ttc，第 2 号子字体 SC，20px）：

| 字符串 | venv 量宽 | 系统 python3 量宽 | 差 | 交付 SVG 隐含宽度 |
|---|---|---|---|---|
| 页脚 `정답은 8면　수준이 섞여 있어요. 번호로 정답을 찾으세요`（20px，右对齐 RIGHT=1862） | 472.9375 | **468.5** | 4.4375 | 1862−1393.5 = **468.5** ✓ 系统栈 |
| P3 行 `당신 나라에는 자유를 위해 싸운 영웅이 있나요`（20px，限宽 378.5） | **383.28125**（>378.5，断行把 `요` 挤到下行） | 376.625（≤378.5，交付断行） | 6.65625 | ≤378.5 ✓ 系统栈 |
| P1 `1면을 읽고 바른 답을 고르세요　정답은 8면`（20px，右对齐） | 363.546875 | **359.109375** | 4.4375 | 1862−1502.9 = **359.1** ✓ 系统栈 |

分解（逐字元量测，两个栈**完全相同**：韩文音节 18.40625px、ASCII 空格 4.484375px、U+3000 20.0px、数字 `8` 11.09375px、`.` 5.5625px；且 5 个 TTC 子字体 JP/KR/SC/TC/HK 量这三个串得数**完全相同**）：

- 差只出现在**整串量测**：venv 栈在每个「韩文音节–ASCII 空格–韩文音节」边界上多加 **约 +1.10938px（20px 字号，≈55.5 字体单位）**，系统栈加 0。
- 验算：页脚串有 4 个此类边界 → 4×1.109375 = 4.4375 ✓；P3 串有 6 个 → 6×1.109375 = 6.65625 ✓；P1 串有 4 个 → 4.4375 ✓。不触发的边界：空格后接数字（`은 8`）、空格前是句号（`. 번호`）、U+3000 前后——均不加。
- layout_engine（raqm/basic）在同一栈内得数相同——差异不在排版引擎选择，而在 Pillow 13.0.0/ FreeType 2.14.3 与 Pillow 10.2.0 / FreeType 2.13.2 之间整串量测的边界调整处理不同（逐字 advances 相同，成串后的成对调整不同）。
- 因此 proof1 的“决定性证据”（现字体下 P3 行 383.28px > 378.5px）恰好是 venv 栈的量测值，不是字体变了，而是**量尺换了**。

### Q1.5 影响范围：只有 pt-ko 一版

- 全 W47 的 freeze 日志：73+ 条 `baseline: 8/8`，仅 1 条 `0/8`（即 pt-ko 的 ko-freeze1.log）；KIT 里仅 pt-ko 一处提到 `TOOL 0/8`。
- 抽查：pt-fr、en-fr 用 venv 复跑均为 8/8 与交付一致。
- 所以双栈问题只影响 **2026-w47-pt-ko 一版**（其 run1–run3 走了系统 python3；同家族其他版走 venv）。须注意：别的版若也曾用系统 python3 跑过而 freeze 记录缺失，不在本调查的抽查内——但现有 freeze 日志无第二例。

### Q1.6 排除清单（拿了证据的）

| 候选原因 | 证据 | 结论 |
|---|---|---|
| 字体文件被换/被更新 | `dpkg -V fonts-noto-cjk` 干净（文件与包内一致）；`fonts-noto-cjk 1:20230817+repack1-3`；四个 TTC 的 SHA-256 已录（附录）；全部 5 个子字体量测试串得数相同；字体文件 mtime 为 1970-01-01（包内时间戳，无参考价值，改以 dpkg 校验+哈希为准） | 排除 |
| fc-cache / fontconfig | SVG 构建只走 PIL 直接读 TTC 绝对路径，不经过 fontconfig；fc-cache 只影响 webpdf/CairoSVG 的 PDF 侧，不影响 SVG 坐标 | 排除（与 SVG 漂移无关） |
| freetype / Pillow 系统包被升级 | venv 的 Pillow 13.0.0（`_imagingft*.so` mtime 2026-10-22，远早于构建）；系统 Pillow 10.2.0，libfreetype6 2.13.2+dfsg-1ubuntu0.2；`/var/log/dpkg.log` 只剩 94 字节（VM 替换后重建，无旧历史）——但构建当天 05:17 的 freeze 已 0/8，证明分歧在构建时已存在，不需要事后升级来解释 | 排除（事后变化无证据、也不需要） |
| `.py` 源码在交付后被改 | 版目录 `.py` 与 freeze build-copy 的 `.py` **字节全同**（14 个文件逐一 `cmp`）；mtime 均早于 SVG 落盘 | 排除 |
| `__pycache__` 陈旧字节码 | 版目录 4 个 `.pyc` 的 code object 与源码 fresh-compile **逐项一致**（co_code、consts、linetable 均等；furniture/tables_ko 仅行号表外无差异——实测 co_linetable 也相等，属同码）；且带版目录原 `__pycache__` 的复跑仍得 copy 字节，freeze（无 `__pycache__`）与 proof（11:02 新编 `.pyc`）亦然——四种缓存状态结果相同 | 排除 |
| 哈希种子 / 字典序 | 两次跨进程复跑彼此字节一致；三次不同 scratch 路径复跑字节一致 | 排除 |
| VM 替换 | proof1 与构建在同一 boot（04:25）上，结果已不同；本次在新 boot（11:25）上复跑，结果与 proof1 的字节一致 | 排除 |
| 输出路径字符串 | 三个不同 scratch 路径的复跑结果相同；版目录与副本唯一内容差异是 `.text.md`（构建后导出，非输入） | 排除 |
| Newsreader weight 200 翻转 | 见 Q1.7——**不是同类机制** | 排除 |

> 注：`run-nocache` 一次复跑名不副实——`cp -rp` 保留属主失败返回非零，`&&` 链跳过了随后的 `rm -rf __pycache__`，该副本实际带了版目录原 `__pycache__`。结论不受影响（带缓存与不带缓存的复跑结果相同，上表已如实列出）。

### Q1.7 webpdf.py 的 Newsreader weight 200 是同类吗？不是

- `tools/webpdf.py`（commit 40963281）把 fontconfig 查询写死为 `:weight=200`（bold）/`:weight=100`（常规），并在注释里写明这是针对 CairoSVG 按 weight 100/200 请求字体的实测 workaround。映射是**代码里写死的**，不是运行时浮动的。
- 实测今日 `fc-match`：`Newsreader:weight=100` → Newsreader-Regular；`:weight=200` → Newsreader-SemiBold；`Noto Sans:weight=100` → NotoSans-Medium；`:weight=200` → NotoSans-Bold。Newsreader 三个文件（Regular/SemiBold/Italic）mtime 均为 2026-11-07 05:00，早于 pt-ko 构建，无 Bold/Medium 面可供“翻转”命中。
- 只有**新装一个 Newsreader 字重面**（如 Bold 700 或 Medium 500）才会改变 fontconfig 的就近匹配——那是环境变更类风险，可用 `fc-match` 一秒核查，与 Q1 的双栈量测分歧不是同类。且 webpdf 只影响 PDF 文字层字体选择，**不影响 SVG 几何**，解释不了 freeze 0/8。

### Q1.8 修复方案（只给方案，不决策）

1. **定一个正典构建解释器并写进 SOP/KIT**：实际标准是 venv（W47 除 pt-ko 外全部 8/8 都走它；AGENTS.md 也规定工具走 `tools/venv/bin/python`）。系统 python3 今后不准用于构建。
2. **pt-ko 一次性改基**：用 venv 重跑 pt-ko 一次（接受 4 处韩语断行变化 + 坐标移动），把它当作一次**版式变更**，按 SOP §8.4 从头再做一轮全量校对——反正 D1/D5–D8 的修复本来就要重建+重校，两件事并作一次。改基后 pt-ko 与全网口径一致，O1 关闭。
3. **KIT 更正**：pt-ko WEEKLY-KIT.md 里构建命令的记录与实测不符（写的是 venv，实际是系统 python3），须更正；同时把 `freeze.py baseline` 的解释器与 Pillow/FreeType 版本写进 KIT（工具输出里目前没有版本信息）。
4. **防复发（轻量）**：在 freeze 门或构建脚本开头加一行版本断言——`python -c "import PIL; assert PIL.__version__ == '13.0.0'"` 之类，跑错解释器直接失败而不是悄悄出数。另建议 freeze 工具在 baseline 报告里打印 `sys.executable`、Pillow、FreeType 版本（目前只打 8/8 与否）。
5. **不建议的路**：不要反向把全网改回系统 python3 来迁就 pt-ko（系统栈是非正典、无锁定的；且 venv 是 SOP 规定的工具链）。

---

## Q2 — 讲解层字体违反 SOP §1.1

### Q2.1 SOP 依据（SOP.md §1.1 字体表）

> | 刊别、讲解层、栏目小字、页眉页脚 | **拉丁读者语言用 Newsreader；俄语读者用 Noto Sans；中日韩读者用 Noto Sans CJK（按字形选）** | 500 / 700 |

另：`不用思源宋体自带的拉丁字形排西文。`

### Q2.2 机制定位（已核实到函数级）

**唯一决定点：每版目录的 `svglib.py` → `_char_font(ch, kind, bold, italic)` 的 `kind="sans"` 分支。**

```python
# core-en / core-de / core-es / core-fr / core-it / core-nl / core-pt / core-zh-cn 的 svglib.py（同一模板）
def _char_font(ch, kind, bold, italic=False):
    ...
    if cp in _CMAP["sans_b" if bold else "sans"]:   # "sans" = NotoSansCJK-*.ttc 的 cmap
        return "sans"                                # -> _FAMILY["sans"] = "Noto Sans CJK SC"
    return "deja"
```

- 拉丁字母、西里尔字母、数字、常用标点**都在** Noto Sans CJK 的 cmap 里 → 讲解层（`kind="sans"`：栏目头 `section_head`、讲解、图注、页眉页脚、题干小字）里所有拉丁/西里尔字符都被判为 `sans`，以 `Noto Sans CJK SC/JP/TC/KR` 发出。`_char_font` 的 sans 分支**从不查 Newsreader，也从不查 Noto Sans**，且函数根本不知道读者语——SVG 里没有任何按读者语选字体的参数。
- 唯一例外是 **core-ru 变体**：`_CYR = range(0x0400, 0x0530)`，西里尔字符先判 `sans_noto` → `Noto Sans`（注释明确引 SOP“俄语读者用 Noto Sans”）——但这条分支是**按字符所属文字**而不是按读者语，且只存在于 **ru 目标**的版里。非 ru 目标的俄语读者版（如 en-ru）用的是 en 模板，没有这条分支（实测 en-ru 的 svglib 与 core-en **md5 完全相同**）。
- **fan-out 安装变体的环节**：各家族的 `build_edition.py` 从 `core-<目标>` 复制源码后，按读者语改写 `svglib.py`——但只有 **it 家族的脚本**有完整变体逻辑（`scratch-fanout-it/build_edition.py:112–150`：读者 ru→整份复制 core-ru svglib；zh-tw→整份复制 core-zh-tw svglib；ja/ko→字符串替换 `_sc_index`→`_jp/_kr_index` 并改 `_FAMILY`，ja 另移植 kinsoku 断行块；其余读者→“core-it as-is (Latin)”）。**fr 脚本**是全量照抄 core-fr，不装任何变体（实测 fr-zh-tw 与 fr-es 的 svglib **diff 0 行**）；en/de 脚本在对应路径下无此变体段（en-ru 未装 ru 变体是直接证据）。所以变体安装本身就是**补丁式、不统一**的。
- **ja/ko 目标是另一代 svglib**：`core-ja`/`core-ko` 的 `svglib.py` 里 **0 处出现 "Newsreader"**，`text()` 是单字体直出（`fam = family or ("Noto Serif CJK JP/KR" if serif else "Noto Sans CJK JP/KR")`），没有 per-char 字体拆分。ja/ko 目标的版里一切文字（含拉丁文）都只能是 CJK JP/KR。
- **变体覆盖实测**（W47 全部 89 份版内 svglib）：TC 只在 de/en/it-zh-tw 与 zh-tw 目标的 12 版；JP 只在 de/en/it-ja 3 版；KR 只在 it-ko 与 ko 目标的 9 版；其余组合一律 SC。fr 家族的 zh-tw/ja/ko/ru 读者版全部是 SC 原样。

### Q2.3 范围表（W47 已交付 SVG 实测）

每版统计：元素总数（按 font-family）、含拉丁字母且字体为 `Noto Sans CJK*` 的元素数（讲解层违规的直接量）、西里尔字母在 CJK Sans 里的元素数。`it-fr` 一行复现任务书数字（每页 69–106 个）。

| 目标族 | 抽查版（读者） | Noto Sans CJK* 元素总数 | 含拉丁字母且在 CJK Sans 里 | 每页 CJK Sans 元素数 | 结论 |
|---|---|---|---|---|---|
| en | en-fr（fr） | 666（SC） | **545** / 1533 | 64–157 | 违规：拉丁讲解层 = SC |
| es | —（W47 零版建成） | 机制同 en（core-es svglib 与 core-en 同构，已逐行比对 `_char_font`/`_FAMILY`） | — | — | 未建成，机制上必违规 |
| it | it-fr（fr） | 638（SC） | **497** / 1418 | **69–106** | 违规（任务书示例复现） |
| pt | pt-fr（fr） | 644（SC） | **503** / 1413 | 64–105 | 违规 |
| ru | ru-fr（fr） | 919（SC）+ Noto Sans 397（西里尔正文） | **432** / 771 | 88–137 | 违规：拉丁讲解层 = SC（西里尔正文走 Noto Sans 是对的） |
| nl | —（W47 零版建成） | 机制同 en（core-nl 同构） | — | — | 未建成，机制上必违规 |
| de | de-fr（fr） | 787（SC） | **637** / 1555 | 68–214 | 违规 |
| fr | fr-es（es） | 691（SC） | **565** / 1498 | 60–199 | 违规 |
| ja | —（W47 零版建成） | core-ja 为旧式单字体 svglib，无 Newsreader | — | — | 未建成，机制上必违规（且无法只改 sans 链，见 Q2.5） |
| ko | ko-fr（fr） | 622（KR） | **409** / 757 | —（全页 KR，无 Newsreader） | 违规：拉丁讲解层 = KR |
| zh-tw | zh-tw-fr（fr） | 763（TC） | **621** / 945 | —（全页 TC 体系） | 违规：拉丁讲解层 = TC |

读者侧抽查（同一机制的另一面）：

| 抽查版（读者） | 含拉丁字母且在 CJK Sans 里 | 西里尔字母在 CJK Sans 里 | 结论 |
|---|---|---|---|
| en-ru（ru 读者） | 395 | **303 / 352** | 违规：俄语讲解层 = SC，应为 Noto Sans |
| pt-ru（ru 读者） | 357 | **255 / 904** | 违规（同上） |
| pt-ko（ko 读者） | 345（多为拉丁标签/数字） | — | 韩语讲解层 = SC ✓ 合规；拉丁片段仍是 SC（同一违规类） |
| it-ja（ja 读者） | 344（拉丁标签） | — | 日语讲解层 = JP ✓ 合规；拉丁片段仍是 JP |
| fr-zh-tw（zh-tw 读者） | 439 | — | 中文讲解层用的却是 **SC 字形而非 TC**（“按字形选”次级违规；fr 脚本没装 TC 变体） |
| en-de / de-en（拉丁读者） | 534 / 637 | — | 违规 |

**范围结论**：拉丁读者——**已建成的 8 族全中**，es/nl/ja 三族未建但机制必中；俄语读者——**非 ru 目标的版全中**（只有 ru 目标版内的西里尔 sans 走了 Noto Sans）；中日韩读者——本体合规，唯 zh-tw 读者在未装 TC 变体的家族（fr 已实测；en/de/it 已装 TC）里拿到 SC 字形。

### Q2.4 已发周（W43/W45/W46）的旁证——PDF 字体表

生产 SVG 已清（W43/W45 为 0、W46 为 1 个 svg 目录），改查 `issues/` 里已发 web PDF 的内嵌字体（`pdffonts`，子集字体按页计）：

| PDF | Newsreader | NotoSansCJKSC | 备注 |
|---|---|---|---|
| W46 it-fr | **0** | Regular 8 + Bold 8 | 连意大利正文都是 CJK——it 族 W46 用的是前 Newsreader 代 svglib |
| W43 it-fr | **0** | Regular 8 + Bold 8 | 同上（旧代） |
| W46 en-fr | Regular 8 | Regular 8 + Bold 8 | 拉丁正文已是 Newsreader；sans 仍是 CJK（违规成立） |
| W46 de-fr | Regular 8 | Regular 8 + Bold 8 | 同上 |
| W45 it-fr | Regular 9 | Regular 8 + Bold 8 | 拉丁正文已是 Newsreader；sans 仍是 CJK（违规成立） |
| W45 en-ru | Regular 8 | Regular 8 + Bold 8 | 同上；Noto Sans（非 CJK）**0**——俄语讲解层也是 CJK SC |

结论：已发三周的 sans 违规与 W47 同源。附加发现：**各周/各族的 svglib 代际不一致**（W43/W46 的 it 族连拉丁正文都未迁到 Newsreader，而 W45 it-fr 与 W46 en/de 已迁）——Tier B 定价须按版核代际，不能假设全网同一代。

### Q2.5 修复方案（只给方案，不决策）

**最小改动点（两个，各 1 处）：**

1. **`svglib.py` 的 `_char_font`（正典模板在 `core-en/svglib.py`；10 个拉丁/CJK 目标族共用同一模板，md5 有 14 版相同）**：在 `kind="sans"` 分支里按读者语加两条优先规则，两条都复用已加载的字体文件、零新依赖——
   - 拉丁读者：拉丁字母/数字/常用标点 → 现有 `news`/`news_b` 类（Newsreader Regular 400 / SemiBold 600，本来就是 serif 链已加载的 `_NEWS`/`_NEWS_B`）；其余字符（CJK/符号）保持现有 `sans`→CJK 路径。
   - 俄语读者：西里尔字符 → 新增 `sans_noto` 类（`/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf` + `-Bold.ttf`，core-ru 变体已在用的同一文件和同一 `_FAMILY` 键名）；其余字符保持现有路径。
   - 中日韩读者：不动（现有变体逻辑已覆盖）。
   - 读者语的传入：沿用 fan-out 已有的变体安装手法——`build_edition.py` 在复制后按读者语改写 `svglib.py`（it 脚本已有该段，fr/en/de 没有）。**但必须先统一**：今天变体逻辑只存在于 it 脚本、且各族行为不一（fr 全不装、en 不装 ru），若只在 it 脚本里修，别的家族仍漏。建议把变体安装收敛到一处共享入口（或至少 12 份脚本同步改），不要再出现第 13 种行为。
2. **`core-ja` / `core-ko` 的 svglib 换代**：这两族是旧式单字体 `text()`，没有 per-char 的 `_runs`/`_char_font` 拆分机制——只改 sans 链修不了。须把新式 svglib（per-char 拆分）移植过去，或把 sans 分支移植进旧式。工作量高于其他 10 族。

**字重缺口（须知，不阻断）**：SOP 要讲解层 500/700。Newsreader 只装了 Regular 400 / SemiBold 600 / Italic 400——500 只能以 400 代、700 以 600 代（serif 的 bold 今天已是这么代的，600）；Noto Sans 则有 Medium 500 与 Bold 700 齐全，且 webpdf 的 `:weight=100` 查询对 `Noto Sans` 恰好解到 Medium——俄语读者可精确命中 500/700，拉丁读者只能近似。是否接受近似，需协调员定。

**不用动的地方**：`tools/webpdf.py` 不用改（`fc-match` 实测：Newsreader 100→Regular、200→SemiBold；Noto Sans 100→Medium、200→Bold；SVG 里写什么字体，PDF 就嵌什么子集）；网站封面（`tools/cover.mjs` + cover.json）不受影响（封面不读 SVG 字体）；lead 动图/次图不受影响。

### Q2.6 成本估计（两档）

计价基准（W47 实测行为）：一版 = svglib 改 + `run.py` 重建 + `render.py` + `webpdf.py` + gates 16/16 + occlusion + p8 + freeze + **按 SOP §8.4 独立全量重校**（版式变了，必须重读全版；pt-ko proof1 的机械门+通读约 1–1.5 小时 agent 时间）+ 重新 insert/commit/push。每版约 1.5–2 agent-小时，其中重校占大头。并行度按用户既定 16 线。

**A 档——只修 W47 在制品：78 版重做**

- 重做 78 版：de/en/fr/it/pt/ru 各 10 版、ko 8 版、zh-tw 9 版、zh-cn 1 版。52 版未建（es 11、nl 11、ja 11、ko 3、zh-tw 1、zh-cn 9、de/en/fr/it/pt/ru 各 1）——**直接带修复出生，无返工**。
- 工作量 ≈ 78 × 1.5–2 = **120–155 agent-小时**（另加机制开发：svglib 分支 + 各族 build 脚本收敛 + ja/ko 换代，约 0.5–1 天；再加 pilot 一版先行验证）。16 线并行下纯工时约 8–10 小时，含修补往返现实约 **2–4 个日历日**。
- 风险：Newsreader 的拉丁 advances 与 Noto Sans CJK SC 差异大（词、行全部重排；讲解段落与 P8 答案流可能变长），**少数版可能顶穿盒/页**（P8 答案流最紧），每撞一处加一次缩内容+重校循环；另 Q1 的解释器定夺必须先于重建，否则新基线建在错栈上。

**B 档——连 W43/W45/W46 已发版一并重渲：390 版**

- 在 A 档之外再加 390 版：W43/W45/W46 各 130 版。工作量 ≈ 390 × 1.5–2 = **600–780 agent-小时**，16 线并行纯工时约 40–50 小时，现实约 **1.5–2.5 日历周**。
- 额外成本（A 档没有）：① 三周的生产 SVG 本地已清，须从 `production/<week>/<slug>/` 源码重 fan-out、重建（不是重跑现成产物）；② 每周 12 个 bundle、共 36 个 bundle 的重新 insert/commit/push（含 lint `--write` 重生成 index.json）；③ 全部 web PDF 的 SHA/字节改变，站点重新拉取；④ **代际差异**：W43/W46 的 it 族等版用的是前 Newsreader 代 svglib（Q2.4），只修 sans 不够，须逐版核代际后再定修法——B 档开工前须先扫三周的 PDF 字体表定代际清单（约半天）。
- 风险与 A 档同类、乘以 390；另有回归风险：已发版重校须逐版过 proof（不可抽样，这是 SOP §8 的硬门）。

**不决策**：A 档还是 B 档、以及“拉丁讲解层 500/700 用 400/600 近似是否接受”，由协调员带回定。

---

## 附录 A — Q1 证据：文件与版本（实测值）

- 字体文件：`NotoSansCJK-Regular.ttc` SHA-256 `b76b0433203017ca80401b2ee0dd69350349871c4b19d504c34dbdd80541690a`；`-Bold.ttc` `faa5f3656a78b2e2d450d27fe8382c778bc2b6bb5ea29c986664a6a435056ceb`；`NotoSerifCJK-Regular.ttc` `93069d8e9e45d515cc421c971a79e6a5777704b348e36a9ef86578bf58adef77`；`-Bold.ttc` `9d3c0d769c703cfe41c49cbe2b14d4718e26545593dc247485486335b783fe94`。包 `fonts-noto-cjk 1:20230817+repack1-3`，`dpkg -V` 干净。Newsreader（`~/.local/share/fonts/`，2026-11-07 05:00 装）：Regular `6b2cf033392e0d88885d6e2984fe5c37ad68651b914b25fe8590e4cd0523ac55`；SemiBold `bc6f3dfb189cdbbdde2107c0f55aa2bc916cfa065bd1d5bea4881e1b9dbbcfae`；Italic `d7099a6854bd8330eaa832e7fa9b218ef54e26f308f5a9d0db876344fffb9462`。
- 解释器栈：venv `tools/venv/bin/python` — Pillow 13.0.0、fontTools 4.68.0、内置 FreeType 2.14.3、HarfBuzz 14.5.0、raqm 0.11.0（`_imagingft` 链接 `pillow.libs/libfreetype-57f805ba.so.6.20.6`；`.so` mtime 2026-10-22）；系统 `/usr/bin/python3` — Pillow 10.2.0、fontTools 4.46.0、系统 FreeType 2.13.2（libfreetype6 2.13.2+dfsg-1ubuntu0.2）、raqm 0.10.1。
- 交付 pt-ko SVG SHA（版目录 `production/2026-w47/2026-w47-pt-ko/svg/`）：p1 `e64d09ee2aa8…`、p2 `f8d08b3f2217…`、p3 `c8196a8ddac7…`、p4 `ead8bba4840f…`、p5 `84937b5d70ad…`、p6 `a9f5a5266cdf…`、p7 `296c954d02b9…`、p8 `e5622ce723f0…`（全 64 位见 `scratch-proof-pt-ko1/svg-edition.sha256`）。
- 复跑对照 SHA（venv 栈产物）：p1 `6e9404b1a541…`、p2 `380757c8303f…`、p3 `7453831afc62…`、p4 `53cdc1a0d231…`、p5 `a4615aeb740a…`、p6 `798c280759f3…`、p7 `d664f756ae12…`、p8 `a67984bedb53…`（见 `scratch-proof-pt-ko1/svg-direct.sha256` 与本次 `run-*/svg/`）。
- `RIGHT`：`bslib4.py:12` 的算式 `MX + 4*CW + 3*GUT` 得 **1862**（行尾注释写的 1885 是算错的注释，代码本身无错；本次全部宽度验算以 1862 为准）。

## 附录 B — Q2 证据文件与命令

- 抽查脚本：`scratch-investigate-fonts/tmp/q2_survey.py`、`q2_survey2.py`（扫 SVG 内 `<text>` 的 font-family 与文字语种）。
- 机制文件：`production/2026-w47/core-en/svglib.py`（正典模板）、`core-ru/svglib.py`（西里尔分支）、`core-ja`/`core-ko/svglib.py`（旧式，无 Newsreader）；`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-it/build_edition.py:112–150`（变体安装）、`scratch-fanout-fr/build_edition.py:30–60`（全量照抄）。
- SOP：`SOP.md §1.1` 字体表（刊别/讲解层/栏目小字/页眉页脚行）。
- 字体可用性：`NotoSans-Regular/Bold/Italic/BoldItalic/Medium.ttf` 均在 `/usr/share/fonts/truetype/noto/`；`fc-match "Noto Sans:weight=100"` → Medium，`:weight=200` → Bold。

## 未决/待核（本次未做，不影响结论）

1. de 家族 fan-out 脚本的变体逻辑未读到（`scratch-fanout-de/build_edition.py` 存在但本次未逐行核对；de 族实测行为与 en/fr 一致：TC/JP/KR 变体均有，ru 变体未见）。
2. es/nl/ja 三族 W47 零版建成——Q2 对它们的结论是机制推断（core svglib 同构），不是 SVG 实测；待首版建成后用同一抽查脚本复核。
3. Q1 的 FreeType 内部机制只定性到“成串量测的边界调整在两栈间不同”（逐字 advances 相同，basic/raqm 引擎在同一栈内得数相同），未深入 FreeType 2.14.3 相对 2.13.2 的具体改动点——对定夺无影响，未深挖。
4. 本次调查未动生产文件；`run-*/svg/` 等复跑产物与 `tmp/` 下的量测脚本均只在 goals 侧 scratch 内，留作复核证据。
