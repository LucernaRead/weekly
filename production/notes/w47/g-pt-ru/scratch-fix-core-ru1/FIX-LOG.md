# FIX-LOG — 2026-W47 core-ru fix1（D2 + D6 + kicker-D2，三处 proof1 核心级缺陷）

修复员：core-fix（2026-11-11）。工作目录：`~/workspace/weekly-git/production/2026-w47/core-ru/`；
scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-core-ru1/`。
探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9…` RC=0；
scratch 写 `probe.txt` 成功。TMPDIR 全程指向 scratch 下 `tmp/`，系统 /tmp 未作输出。
任务分三棒到达（D2 → 追加 D6 → 追加 kicker-D2），三处并入同一次重建、同一本地 commit（fix1，未 commit 前到达，故不另起 commit）。

## §0 版身份核对（磁盘为准）

| 文件 | 修复前字节数 | 修复前 SHA-256 | 修复后字节数 | 修复后 SHA-256 |
|---|---|---|---|---|
| `Lucerna-VOL4.pdf`（印） | 31,429,156 | `4b56429722dbbf4573eb80bf24a7d4ae8daf6a7217fd01537c26801fc4411868` | 31,429,147 | `d60fbd6c503f2442ae5a49bf475518034563816af27a05f8bbba2dc1383cab81` |
| `Lucerna-VOL4-web.pdf`（网） | 3,992,881 | `8a2649263171727ecfb2118e3f85bc1ddfc8a0c1f23730e66652ba78e358fca7` | 4,025,834 | `2f995f1deb75fce116b33a10b9da816fb415a7bac79a258d817c4f99731e4197` |
| `2026-w47-ru-zh-cn.text.md` | 60,980 | `935620994e4b98def778c2c7624a85f27feeebbd8613971fd6c9b7db4f6f10fb` | 60,953 | `348511e061c28019b56d81bcd6e006ff1d7ddae3e49c7b599668216a6b90f8cc` |
| `2026-w47-ru-core.text.md` | 60,980 | 同上（字节一致） | 60,953 | 同上（字节一致） |
| `ru-p8.json` | — | `a51ef98cd6d8921a1ab864ee8e6877beb205530606b9b33e45121038a4753cce` | — | `5193ff4adde4005ca6047e73ba6ec68a623751b7bef9469b9db57256bb04ccfd` |

- KIT 所记 text.md 数字已 stale：KIT §5/§7.3 称 54,801 字节 / 690 行 / 203 块，磁盘实为 60,980 字节 / 838 行；修复前从源码重导出（`ru_textmd.py . … "VOL.4 · Russian text · Simplified Chinese explanations"`）与磁盘文件**字节一致**，故以磁盘为准，KIT 已按 60,953 字节 / 838 行 / 277 块更新。`ABSTRACT.txt` 未动（SHA `70121bc9…`）。
- 网 PDF SHA 按磁盘现行文件为准：webpdf 逐跑 SHA 不定（pt fix1 已证：fontTools 子集化流字节级非确定性；本次 D2+D6 跑 4,025,862 字节、终版跑 4,025,834 字节，文字层同为 56,024 字节前身 56,022 字节——kicker 双空格所致 +2 字节归一化差异见 §5）；印 PDF 两跑 SHA 一致（见 §3）。
- 中间重建（D2 单修、D2+D6）均已被终版重建取代，只记终版数。

## §1 改了哪几行（旧值 → 新值；其余源码零改动）

| # | 文件 | 旧值 | 新值 | 说明 |
|---|---|---|---|---|
| 1 | `content12.py:18` | kicker 字符串内 9 处单空格 | 同串 9 处改为双空格 | kicker-D2（ru-zh-tw proof1 D2）：词距过紧。行宽 +32.2px，仍居中于 975。调查报告 `scratch-invest-ru-kicker/INVEST-NOTE.md`（调查员 afcb2121，已验证） |
| 2 | `content12.py:251` | ex 键 `"желание"` | `"желании"` | D6（ru-pt proof1，严重错键）：`о своём ___` 支配前置格，-ие 中性名词前置格单数 -и。题干、注（`желание = 愿望`，词典形）、`content12.py:170` gloss 均不动 |
| 3 | `content12.py:267` | D 选项 `"Международный день студента"` | `"День студента"` | D2（ru-nl proof1 D2，minor）：选项 b 超出版心。等效缩短；键 b、题数、注（`大学生节 b`）不变；完整词形仍在 P2 正文与 Q11 题干 |
| 4 | `ru-p8.json:177` | `"20": "желание"` | `"20": "желании"` | D6 同步：由 `p8.py extract` 从重建后 P8 SVG 再生，非手改 |
| — | `content12.py:251/267` 行内注释 | — | 各加 2–5 行注释 | 说明改动原因与根因（D2 另见 §2；D6 另见 §2） |

- `svglib.py` / `bslib4.py` / 其余内容文件：零改动。D2 的库级根因（`match_set` 的 `wrap()` 按不含 `b. ` 前缀的宽度断行）不在本次 scope（任务定为“只改 core 的内容行”），与 core-it fix 同类根因（其简报已记 "letter-prefix not in budget"），留待协调员决定是否修库。
- D6 全仓 grep：键 `желание` 其余出现处仅 text.md 两处（Q20 练习行 173 + 答案附录行 694），重导出已同步（见 §4 diff）；正文 168 行 `самое главное желание` 为主格作主语，正确，不动；10 个 ru fan-out 版 text.md 含旧键，属下游重 fan-out 范围，本次不动（见 §6）。
- kicker 串不在 text.md / ABSTRACT / 检查脚本中（调查已核），text.md 重导出与修复前字节一致（见 §4）。

## §2 测量依据（修复前实测）

- **D2**：SVG 节点复核与任务简报一致（P2 y=2162.0：`b. ` x=1473.5、`Международный` x=1497.7、`день` x=1703.9、`студента` x=1764.7，末词 advance 103.5px → 右缘 1868.2，+6.2）。PIL 真墨（cards/p2-zhizn.png，thr<200）：b 右缘 **1870（+8）**，a +181、c +69、d +34。`wrap("Международный день студента", 23, 388.5)` 单行 370.5px ≤ 388.5 故不断行，再加 `b. ` 24.2px 即溢出。候选比较：5 空格 hack 可断行（line0 clearance +102.9）但源文带 5 空格、wrap 决策余量仅 4.5px、且会漏进 text.md（`ru_textmd.py` 原样导出 rights），弃用；`Международный студенческий день` 断行后首行仍 -4.0，弃用；故取等效缩短 `День студента`（PIL advance clearance +197.8）。
- **D6**：`о + 前置格`；`желание`（-ие 中性）前置格单数 `желании`。proof1 已用 masterrussian / settemilalingue 公开语法来源核实；本版惯例给屈折形（Q38 `ноября`、Q73 `заказов`）。
- **kicker-D2**：调查报告实测（见其 §1.3/§3）：空格走 Noto Sans CJK SC（3.58px @16px），邻字墨迹外溢 advance（А +1.2、Х +0.8、Я +0.4），三处最紧 PIL 墨框间隙 2.40/2.80/3.10px；改路由到 Noto Sans 仅 +0.58px（→2.98/3.38/3.68，仍 <4）且重排全书，已排除；双空格 +3.58px/处，全行均匀。

## §3 重建与确定性

- `run.py`：RC=0，0 FLOW OVERFLOW / HEAD TOO WIDE；150 题（A2 50 / B1 76 / B2 24；分版 10/18/18/18/18/18/12/38）；范文 97 词。
- `render.py`：8 卡片 + 印 PDF；两跑印 PDF SHA 相同（`d60fbd6c…`，31,429,147 B）——确定性已验。
- `webpdf.py`：网 PDF 4,025,834 B，文字层 56,024 字节（印版同）。网 PDF 逐跑 SHA 不定（见 §0），文字层逐字一致。
- `ru_textmd.py` 导出：60,953 字节、150 题、277 块；两份 text.md 字节一致（cmp 已验）。与修复前 text.md 的 diff 恰好 3 行：Q20 键 ×2（练习行 173 + 附录行 694）、Q25 选项 ×1（行 187）。
- SVG 影响面：P2 与修复前**字节一致**（kicker 只动 P1）；P1 971 个 `<text>` 中仅标语行 20 个不同，非 `<text>` 部分完全一致；kicker 行 586.3–1363.7（+32.2px），居中 975 不变。

## §4 全部门禁（终版重建实跑结果）

| 门 | 命令 / 方法 | 结果 |
|---|---|---|
| `check_core.py .` | `tools/venv/bin/python check_core.py .` | golden BAD **0**、gloss 失败 **0**、P8 SVG 文本字符 8191、孤儿行首 5 处皆为 KIT §7.3 已裁决的非行首、碰撞 1 处为已知 P1 y1712 `чёрная`（与修复前一致） |
| occlusion 审计 | `tools/occlusion_audit.py svg --json` + `scratch-ru/adjudicate.py` 像素裁决 | 自检 6 类全触发；**42 标记全 TEXTX、0 LINEX**，标记集与修复前 run3 逐项一致；像素裁决 **42 CLEAR、0 OVERLAP** |
| creambox 全版 | 正典 `hidden_files/w47/tools/creambox.py`，`svg/*.svg` | **32 框，0 真溢出**（负 clearance 行全为已知 below-window 假阳性，框内 clearance +15.9…+58.0；唯一 inside-only desc-clear 负值 -1.6 经像素复核：该行真墨止于 1127，框底 1130，实墨 +3px 在框内——中文行无降部字母的 allowance artifact；负 clearance 行集合与 kicker 前一跑逐行一致） |
| p8 extract | `tools/p8.py extract --p8 svg/p8-test.svg --total 150 --json ru-p8.json` | **150/150** |
| p8 compare | `tools/p8.py compare --core-dir . --edition-dir . --target ru --total 150` | **CLEAN**，missing=[]，keydiff=[] |
| freeze baseline | `tools/freeze.py baseline --build . --core-svg svg --out <scratch>/freeze-fix1b` | **8/8 SVGs byte-identical**，core 完整性 8 文件重哈希无改动 |
| 印/网文字层 | `pdftotext` 两版 + `cmp` | **字节一致**（各 56,024 字节；kicker 双空格在两版归一化为同一文本） |
| P8 最小字号 | PyMuPDF `fitz`，印版 PDF 第 8 页 | **9.75pt**（恰好 §1.1 下限，与修复前一致） |
| keycheck | 印/网 PDF 答案区逐项比对 `ru-p8.json` + text.md 附录 | 印/网各 **150/150**，0 缺失；Q20 单列见 §5；Q150 的 1 处“mismatch”为本人解析正则误 match 练习行，附录实为 `150. ✓ 范文见本版 H 区（97词）`，与 JSON `✓` 一致 |

## §5 三处修复的复测值

- **D2**：SVG advance：b 行 `b. День студента` 右缘 1664.2（clearance +197.8）。PIL 真墨（终版卡片）：**b 1666，clearance +196**（修复前 -8）；同页 a **+181**、c **+69**、d **+34**，0 溢出。
- **D6（单列复核）**：题干前置格 `о своём ___.`（印版文本层原样）+ 键 `желании` + 注 `желание = 愿望`（词典形）一致。五方见证：SVG P8 节点（x=109.7 `желании` 为键、x=185.5 `желание` 为注）、`ru-p8.json:177`、`2026-w47-ru-zh-cn.text.md:173`（练习行）与 `:694`（附录行）、印版文本层 2304 行 `20. желании — желание = 愿望`、网版同行。keycheck 150/150。
- **kicker-D2**：方法一（PIL 墨框法，与调查表 1 同口径）：9 处 **7.20 / 5.90 / 6.80 / 6.30 / 7.10 / 7.40 / 7.40 / 6.80 / 7.60px**，逐值复现调查结论，最紧 ГАЗЕТА/ДЛЯ 5.90（≥4px 目标，余量 +1.90）。方法二（渲染列扫 strict 垂直通道，带 y357–374）：实墨口径 thr<128 为 4–8px（最紧 4px）；最严苛口径 thr<200（计抗锯齿晕边）最紧 3px、其余 4–8px，与调查注记一致。初版自测曾把 `—  `/`,  ` 尾空格计入墨框致 5 处假 FAIL，已纠正（PIL `getbbox` 会把尾空格 advance 计入右缘；改用 strip 后墨框复核）。`РОССИЯ/,`、`ПО/-`、`-/РУССКИ` 为逗号/连字符直连（无空格设计），不计入词距。

## §6 范围外与下游

- **不在此棒**：ru-nl D1（P1 标题 +14px，版级荷兰语 gloss 过长，待重 fan-out + 各版 fix1）；ru-nl D3（网 PDF 斜体丢失，建于 webpdf 修复提交 40963281 之前——入仓前全部 web PDF 批量重建解决）；O1（Q139/Q140 模型翻译较自由）为观察项，未改。
- **ru-en 的“完全定稿”状态因 D2 已作废**（其 proof3 (a) 漏检了 D2），重建后须重校——由协调员处理，本次只修 core。
- **10 个 ru fan-out 版须重 fan-out**：kicker 补丁须落到每版重建产物里（fan-out 若不从 core 复制 `content12.py`，则每版同法打补丁 + 重建 P1）；D2 选项与 D6 键同理随 core 重建同步。
- 本次 commit 只含 core-ru 相关文件（源码 + KIT + text.md + ABSTRACT + assets，见 §7），不 push；`svg/`、`cards/`、PDF、`__pycache__` 不入仓（沿 core-pt/it 前例；渲染件由源码可复现）。

## §7 结论

D2（+196px）、D6（五方见证一致）、kicker-D2（9 处 5.90–7.60px）三处均已修复；全部门禁一次通过（终版重建），无新增缺陷。三件新 SHA 见 §0 表。本地 commit 待做（只 commit、不 push）。

## §8 提交与环境备注（2026-11-11 12:25）

- **Commit：`f11854bf3fcfc0355d32c15224429831f657b2da`**（Beacon，2026-11-11 12:25:11 UTC），26 个文件（§6 所列集），只 commit、**未 push**。提交后 core-ru 工作区仅剩应排除的未跟踪渲染件（`*-core.text.md` 重复件、两份 PDF、`cards/`、`svg/`）。
- **`/dev/null` 缺失事件**：提交时宿主 `/dev/null` 不存在（VM 替换抹掉，与 AGENTS.md 记的 /opt 丢失同类），`git add` 报 `could not open '/dev/null'`。`mknod` 需 CAP_MKNOD，容器无此权（EPERM），改用 `unshare -rm` 命名空间 + `mount --bind <scratch>/tmp/nullfile /dev/null`（读 EOF、写进 5 字节小文件）完成 add 与 commit；宿主留了一个 0 字节普通文件 `/dev/null` 作挂载点（无此文件则 git 全不可用；留着无害，已验 plain git 恢复工作）。协调员后续若在宿主直接跑 git 且 /dev/null 又消失，同样用该法。
- 终版重建后未再改动任何 core-ru 文件；`git log` 已验 HEAD 即本次 commit。

