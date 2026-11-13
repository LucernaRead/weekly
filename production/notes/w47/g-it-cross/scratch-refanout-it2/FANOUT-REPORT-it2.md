# FANOUT-REPORT-it2 — W47 it 全家重扩散 2（core D-2 fix）

- **任务**：从已定稿的新核心 core-it（D-2 fix + 核心复校 (a)，2026-11-11）重扩散全部 10 个 it fan-out 版（de/en/es/fr/ja/ko/nl/pt/ru/zh-tw）。**只重建，不 commit、不 push、不宣布任何版定稿**（重校由协调员另派）。
- **工作目录**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-refanout-it2/`（下文简称 `scratch-refanout-it2/`；机制在 `scratch-fanout-it/`）。解释器全程 `~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0）；`TMPDIR=<scratch>/tmp`；`PYTHONDONTWRITEBYTECODE=1`。
- **结论：10/10 建成，门禁全过，D-2 逐版验证全过，freeze 10/10 8/8，目视 80 页 0 缺陷。** 全部 10 版已写回生产目录，KIT 已更新（§12/§13）。未 commit、未 push。

## §1 新三 SHA 全表（2026-11-11，盘上实测；`scratch-refanout-it2/shas.txt`）

| 版 | 印 PDF（bytes / sha256） | 网 PDF（bytes / sha256） | 文 text.md（bytes / sha256） |
|---|---|---|---|
| de | 14,037,210 / `7952f4ff3b957ecbbbdd8be5701237b2fe43824160575ee8bc217baedfa5c7b8` | 1,297,238 / `65e262903bd0ee8fa82fa2d575f6225ec01c815c5551451ec964ee448c9a1ac0` | 56,662 / `de0aa214818e4ce2c25952323cd8cac781d72d89419130b2ffb96308dd2798c9` |
| en | 14,032,910 / `b0444f8a89fcd1df53941dd0e3774777f17cd238fc0f93fd519c8c680c468b17` | 1,291,136 / `b99776c00ae69f7b0b93264769677d9bd536bcd2993c8225c092b4614581e227` | 55,183 / `ad311b5bf59ae9eafc996834abba95d1f4bd899874043c605735d57cbbd7f917` |
| es | 14,033,619 / `6c299214601b4936dc5329cc72627919fe3b27b90f742298a2eae8cb03554769` | 1,291,397 / `c194c3421415c75ed089ced802aae069d6bbd6c3de10c9a4e694cac58c447862` | 56,193 / `4fd5647e2b7a13812b384963607bd67eda2c2c4fe6bd197b9b08bc08eee21643` |
| fr | 14,034,054 / `e80d4dd3eb4c512c7d0c84c29c10fad56b927dc85f2b76663dcd82fef68727f0` | 1,290,956 / `d8fe0ef50efcfe7d2641e7ca737b618d8c06a529c6e33c016557f242c8977054` | 56,517 / `aca1356c0c90526a7a621a399bc5ea9a75f9b635aae42662022217ddc01d5cad` |
| ja | 28,221,020 / `640a355a2943efe35b7c1437e1154a4012aa1ec51f18fff155fc7caa4e1c6666` | 1,901,668 / `4f1bac2c12b8762c187a60647fec578f187f9f5150a2b65cfca31b474f00ee3f` | 58,165 / `5ac2ecf5abb28bbc9f56c182572a9c7a7e4e93ae8b9c49b5468cc890e0ec16d7` |
| ko | 19,296,892 / `3125d4f36667155d5f10eb3522364513ba31bee72a4445f1e5ac90d74b28f87f` | 1,607,467 / `67bda0ac5dfd57c6dce140bc021e420044888d11c63dcb25426bb2e95becfef8` | 57,326 / `d4d0c6c1a0048b9f2fa3248c0b5868058a3599bf75d253188301f3ad0a5a8fa1` |
| nl | 14,034,396 / `a7edbb18d6cde81c3d9454d636ee4412c7f555c2aabc20665fa08c059d2a8a5e` | 1,291,725 / `d57398427d4dc493ea5104b3ab86343d83a5edd9e83093d3335baff4fb66fbb7` | 55,488 / `b13ef7a7abe07928207eedc182106368ac653d8a8fad49af2adf184a2c94906e` |
| pt | 14,036,607 / `9910d536048ae4975c6e1657827f299abab0d274819f881b648a56d513b65135` | 1,294,373 / `f2e390f31fc30d14ff08803244cc66749abafd2acdeb41763ba3800fc5f0d85e` | 55,718 / `e01360ae9c401d014a9e0a51779646845a112aac4e8afe912090269c6ffa7302` |
| ru | 14,180,915 / `966a9d10c033ed0297cef6d018b23a548dec2b016bc0eb3ecf61440ac2247666` | 1,441,240 / `db22fa31244bb4fe0a7649660a621aa15da22cda010eaad4fd0ff9e619ed0505` | 67,731 / `47c0471515d3b249855e33a290d0c4259ecce431995db45ac0ce926cf5a52b1d` |
| zh-tw | 27,779,699 / `96aa320738b09cf89c18fbb63789c38225017feb8969db98c1fedb44041d1531` | 2,074,045 / `1f5730490f765d75d9c1317c6ef65734ab8d9453541161b271591660b109a1a9` | 52,494 / `c18ad203cf49356079c4403e69b7366b1f36109963eadbcce17058da08dd8432` |

- **text.md 字节差（新 − 修前）**：10 版全部恰为 **−21**（de 56,683→56,662；en 55,204→55,183；es 56,214→56,193；fr 56,538→56,517；ja 58,186→58,165；ko 57,347→57,326；nl 55,509→55,488；pt 55,739→55,718；ru 67,752→67,731；zh-tw 52,515→52,494）——恰为 D-2 删去的 `andare → andrò, `（21 字节，含尾空格）加上 L18 `irregolare`→`regolare`（等长）的净差。词数亦各版 −3（删去的 `andare`、`→`、`andrò,` 三词；如 en 7931→7928，见 `gates-en.log`）。
- **修前生产三 SHA（历史，`scratch-refanout-it2/shas-pre.txt`，开工前盘上实测）**：de 印 `527b38ce…` / 网 `f9f4343b…` / 文 `36a11a8f…`；en 印 `70061d6a…` / 网 `d037ccdf…` / 文 `2168a652…`；es 印 `8b7547d3…` / 网 `efc1404b…` / 文 `64a8ac2f…`；fr 印 `6e393b3d…` / 网 `7276c70f…` / 文 `a634057b…`；ja 印 `279962b7…` / 网 `4df33c69…` / 文 `bf64b304…`；ko 印 `d5698327…` / 网 `85722a84…` / 文 `e9dbe371…`；nl 印 `2091448c…` / 网 `039ee0bb…` / 文 `0a044d4b…`；pt 印 `6f74ee92…` / 网 `f28a5635…` / 文 `2ce7bfe9…`；ru 印 `af980e26…` / 网 `3e10d785…` / 文 `8a49ce37…`；zh-tw 印 `79e51c53…` / 网 `a809a3a5…` / 文 `681dff47…`。完整 64 位值见 `shas-pre.txt`；各版 KIT 新节亦完整保留。

## §2 源核心（开工前逐字核对，任一不符即停——实际全部相符；收工重验仍一致）

- 印 `La-Lucerna-VOL4.pdf`：27,726,330 B / `e1f89922a2b09e66d7d132eeab12b2638528e737685fa85d70f41bb8d2d1255d`
- 网 `La-Lucerna-VOL4-web.pdf`：1,790,596 B / `09f2ef6696ad67e92e57ba161c8ba2e6b35753634fa21b7ce68ea029283d71ef`
- 文 `2026-w47-it-zh-cn.text.md`：52,655 B / `9eb9ee0662542e6ccf2814a2f2534fd64b62ad326de42e9cf83282092b5b6eed`
- 收工重验（本轮末）：三 SHA 与任务值逐字一致；`core-it/content7.py:17/:18` 仍为 D-2 新串。`core-it/` 全程只读，未写一字节。

## §3 D-2 改动与逐版验证（`scratch-refanout-it2/check-<lang>.json`，10/10 ALL PASS）

D-2 唯一核心变化（`core-it/content7.py`）：L17 规则形只举 assaggiare/guardare（删 `andare → andrò, `）；L18 改为「Il verbo è leggere, regolare al futuro: leggerò.」（已读 `scratch-fix-core-it-d2/FIX-LOG.md` 与 `scratch-reproof-core-it-d2/PROOF-NOTE.md`，核心复校 (a) 零缺陷）。每版必验（`check_refanout2.py`）：

1. `text.md:775/:777` 为两条新句（逐字比对，全 10 版通过）。
2. 旧串 `Le forme sono regolari: andare` 与 `irregolare al futuro: leggerò` 在该版 live 文件（content7.py、p7 SVG、text.md、两 PDF 文字层）均为 0。
3. **印/网 PDF P7 文字层含新串各 ×1、旧串 0**——纯拉丁改动对 freeze diff 与 p8 compare 不可见，此项为必备的文字层检查（PyMuPDF 词序，第 7 页）。注意：PDF 文字层把 `→` 粘到邻词上（`→assaggerò,`、`guardare→`），故新串 L17 按箭头归一化（`\s*→\s*` → `→`）后计数；此为检查脚本的修正（见 §8），非内容问题。另：`andare` 一词仍在 P7 出现一次——在 Q101 题干 `(andare)` 的原形提示里，与 D-2 旧串无关（旧串按整串检查为 0）。
4. 与修前生产版逐项 diff（`scratch-refanout-it2/backup/`，430 文件、SHA 校验通过）：**只许 P7 变化**——SVG p1–p6/p8 逐字节一致、cards p1–p6/p8 逐字节一致、text.md diff 恰为 (774,775) 与 (776,777) 两处 replace、content diff 恰为 `content7.py` 4 行（2 条 D-2 行）、p7 SVG 文本节点 diff 仅限 2 条 D-2 句的换行碎片（旧 9 节点 / 新 3 节点，皆为两句的子串；空节点计入）。两 PDF 因 P7 重建而变。
5. fix3 9 行 ×1、旧措辞 0；E 标签 content8.py:69/71/73/75 与 text.md:969/971/973/975 按各语种本地化标签；17 个表值 ×1；`translations.py` 240 条 × 10 语（构建计數断言 10/10 通过，未改动）。

| 版 | 门禁（`gates-<lang>.log`） | 文字层词数（印=网） | P7 col3 末端 | P8-keys 流末（底 2552） | freeze baseline |
|---|---|---|---|---|---|
| de | 20/20 ALL PASS | 7,781 | 1673.0 | 2514 | 8/8 |
| en | 20/20 ALL PASS | 7,928 | 1673.0 | 2514 | 8/8 |
| es | 20/20 ALL PASS | 7,998 | 1673.0 | 2529 | 8/8 |
| fr | 20/20 ALL PASS | 8,009 | 1673.0 | 2514 | 8/8 |
| ja | 19/19 ALL PASS | 6,746 | 1673.0 | 2546 | 8/8 |
| ko | 19/19 ALL PASS | 7,411 | 1673.0 | 2499 | 8/8 |
| nl | 20/20 ALL PASS | 7,885 | 1673.0 | 2529 | 8/8 |
| pt | 20/20 ALL PASS | 7,962 | 1673.0 | 2529 | 8/8 |
| ru | 20/20 ALL PASS | 7,587 | 1673.0 | 2529 | 8/8 |
| zh-tw | 19/19 ALL PASS | 6,829 | 1644.0 | 2484 | 8/8 |

拉丁/西里尔 7 版门禁分母为 20，CJK 3 版分母为 19（无 strict-CJK 项）。P4 col3 末端全版 1140.45（= 核心 1140）；P8-ex 流末全版 col 3 y=870（zh-tw 840）；P8 最小字号 13.0 px = 9.75 pt；网 PDF 全部 < 7 MB 且带文字层；occlusion 0 旗标；p8 extract 150/150、compare CLEAN（keydiff 仅 [137,138,139]）；印网文字层多重集一致；text.md 双向验证 0/0。

- **构建**：4 批顺序——en/de/es；fr/pt/nl；ru/ja/ko；zh-tw。run.py/render.py/webpdf.py 每版 rc=0、TOTAL 150、0 溢出（`scratch-fanout-it/<lang>/build1.log`）。构建日志中 P8-keys 流末逐版与预期一致（de/en/fr 2514，es/nl/pt/ru 2529，ja 2546，ko 2499，zh-tw 2484）。
- **freeze**：`tools/freeze.py baseline` 逐版 8/8 byte-identical（`scratch-refanout-it2/freeze-<lang>/`，`freeze-verify.txt` 累计 10 个 "8/8"），core integrity：发货 SVG 在 baseline 运行前后 8 文件重哈希一致。
- **目视**：10 张 2×4 拼图（`sheets/sheet-<lang>.png`，80 页）逐版看完，无溢出、无重叠、无裁切、无豆腐；已知核心模式原样保留（P3/P5 结构留白、ko/ja P5 换行后差异、ru 紧词距）。另 200 dpi 裁图 3 张：en P7 A2 栏、zh-tw P7 A2 栏、zh-tw P1 cifre 盒——两条 D-2 新句渲染干净，Q101–104 完好，zh-tw 桥句 `用將來時說計劃：andremo、assaggeremo、guarderemo、leggeremo。` 完好。

## §4 it-nl 间距手补丁（唯一真实手补丁，与上一轮相同）

- `content12.py:18` spacing 11.5 → 11.0（断言 count==1、替换后零 11.5 残留）；重跑 run.py/render.py/webpdf.py（rc 均为 0，TOTAL 150，日志 `nl-rerun-{run,render,webpdf}.log`）。
- 重跑前后 SHA 对比（`nl-prefixed-sha.txt` / `nl-postfixed-sha.txt`）：恰变 4 件——印 PDF、网 PDF、p1 SVG、p1 card；其余 15 件（含 text.md）逐字节不变。
- 刊头带复核（`occlusion_audit.py::ink_box`，4×）：左 **10.5**、右 **1873.7**（页宽 1950），左余 10.5、右余 76.3——与上一轮实测值完全一致，带在页内。
- `check_refanout2.py nl --spacing-fixed`：ALL PASS。

## §5 跟踪项：it-zh-tw P1 cifre 标题余量（proof2 O1）重测

- **PIL 真墨法**（复用 proof2 `sweep.py`，同一方法、同一脚本）：奶油盒 538.5..961.0，标题墨 556.5..960.0，余量 **+1.0 px**——与重扩散前实测值**逐字相同**（`LA SETTIMANA IN CIFRE　數字看本週`，23.0 pt bold；`sweep-zh-tw.log/txt`）。
- **像素法**（印 PDF P1，96 dpi 渲染，亮度 <140 为墨）：标题带内最右墨像素 x=959，盒右缘 961.0 → 余量 **+2.0 px**；proof2 报价 +1.4 px 是按其 960.5 盒缘口径（960.5−959.1），墨位置本身未变（959/960.0）。200 dpi 裁图目视（`pages-crop-p1-cifre-zh-tw.png`）：标题末字 `週` 完整在盒内，盒缘清晰。
- **结论**：余量未变，仍为全家最紧的一项；按 it-de/it-fr 已接受先例（墨恰触盒界、盒界外无墨）通过，下一轮重扩散仍须重测。

## §6 KIT 更新（`update_kits2.py`，10/10 与干跑逐字节一致）

- 每版 WEEKLY-KIT.md：§7 表头与印/网/文三行更新为新 SHA/字节；§8 整节替换为本轮门禁记录；追加新节——de/en/ru 为 **§13**（已有 §12 fix1），其余 7 版为 **§12**（"Re-fan-out (core D-2 fix)"，含新三 SHA + 修前生产三 SHA 历史 + D-2 确认 + P7-only diff + nl 间距注 / zh-tw 跟踪注）。
- 其余旧值一字未动：diff 验证——全部改动只在 §7 行、§8 块与新附节；de/en/ru 旧 §12 fix1 的 "was" 行原样保留；旧 §7 SHA（de/en/ru 为首次扩散值）仅存于旧节历史行。
- §8 纠正：上一轮 KIT §8 写 "added CJK: n/a (CJK reader language)"——对 7 个拉丁/西里尔版是错标（其实测值：de/en **×13**，es/fr/nl/pt/ru **×8**；ja/ko/zh-tw 才是 n/a）。本轮 §8 按实测更正；上一轮 KIT 未改（保存在 `backup/` 原样）。

## §7 中断与恢复（本轮实况）

- **运行时重启（21:41 UTC 左右）**：第一批后台会话被重启杀死，de 正在跑 webpdf——de 当时 run.py + render.py 已完成（TOTAL 150、印 PDF 14,037,210 B、8 cards），网 PDF 与 text.md 未生成；es 未开始；en 已完整。恢复：删 de 半成品目录、按同一机制整版重建（rc=0，text.md 56,662 B = 56,683−21 ✓），再建 es。其余批次改前台逐版跑，不再用后台批处理。
- **检查脚本修正**（`check_refanout2.py`，3 处，皆由首版 en 的 4 个初版 FAIL 暴露，均已验证为脚本问题、内容无误）：
  1. PDF 文字层 `→` 粘词：新串 L17 按箭头归一化后计数；旧串在两种归一化下均为 0。
  2. difflib 把相邻的两改行并为一个 replace opcode：content7 断言改为“改动区间恰为 17–18 行、rem/add 各 2 行且新旧串按序在位”。
  3. p7 节点 diff 的空文本节点：`l and l in pool` 把空节点判为不合规，改为允许空节点（空节点来自同段换行）。
- **KIT 更新脚本修正**（`update_kits2.py`，4 处，皆由干跑暴露）：
  1. "240 entries" 断言 ==1 改 ==2（每版 KIT 出现 2 次：L41 表注 + 导出修复注）。
  2. strict-cjk 正则 `\\\\u3000`（双反斜杠）改为 `\\u3000`（单反斜杠，与日志实况一致）——否则 7 个拉丁/西里尔版会错得 "n/a"（上一轮 KIT 正是这么错的）。
  3. §7 文本行正则改为吞整行（`.*` 收到行尾）并加 `count=1`：es 的 §7 文本行尾巴带旧文 SHA（`64a8ac…`），前缀替换会把它留下；de/en/ru 另有 §12 固定行带同名行，`count=1` 只换 §7 的第一处。另加断言“旧文 SHA 不在 §7”。
  4. §8 目视句改实话：本轮未逐字重读 1317 行 × 10 版——text.md 除 775/777 两行外与已校对的修前版逐字节一致，上一轮全文重读的结论对未变的 1315 行仍然成立，两改行逐字验证。

## §8 未做的事与待办

- 未 commit、未 push；未宣布任何版定稿。**重校待协调员另派**（本轮只重建）。
- `backup/`（430 文件，312M，SHA 校验通过）**在新 bundle 入仓前不得删**；入仓后按本地存储规矩清理。
- 上一轮 `prev-logs/`（346M）与本轮 `prev-logs/` 均保留：上一轮构建日志与 freeze-baseline 在其中。
- 磁盘：95G 已用 / 55G 空闲（150G 盘），无配额压力。
- 无工具改动：freeze.py / gates.py / build_edition.py / translations.py 均未改（translations.py 240 条 × 10 语，构建计數断言通过）。

## §9 证据文件（`scratch-refanout-it2/`）

- `FANOUT-REPORT-it2.md`（本文件）、`shas.txt`（新 30 SHA）、`shas-pre.txt`（修前 30 SHA）
- `check-<lang>.json`（10 份 D-2 检查全过）、`gates-<lang>.log`（10 份门禁）、`check-<lang>.log`
- `freeze-<lang>/`（10 份 baseline 8/8）、`freeze-<lang>.json`、`freeze-verify.txt`
- `sheets/sheet-<lang>.png`（10 张拼图）、`pages-crop-p7-a2-en.png`、`pages-crop-p7-a2-zh-tw.png`、`pages-crop-p1-cifre-zh-tw.png`
- `backup/`（修前 10 版）、`prev-logs/`（上一轮构建日志）、`nl-prefixed-sha.txt`、`nl-postfixed-sha.txt`、`nl-rerun-{run,render,webpdf}.log`
- `sweep-zh-tw.py` / `sweep-zh-tw.log` / `sweep-zh-tw.txt`（cifre 重测）、`update_kits2.py`、`check_refanout2.py`、`make_sheets.py`
- 构建日志：`scratch-fanout-it/<lang>/{build1,render1,webpdf1}.log`（本轮覆盖上一轮；上一轮的在 `prev-logs/`）
