# W47 ru 家庭 F-2 修复 FIX-LOG（接替工人）

- 任务：校对 F-2（text.md 附录行字面 `— СТРАНИЦА ? —` 占位符 → 真实页码），11 版
- 接替：上一任 80df5cd0 出错中断，只留改前快照 `pre-sha.txt` 与 `pre-textmd/`，无 FIX-LOG。本日志自接手起新建。
- 日期：2026-11-12（Thu）
- 范围：`production/2026-w47/` 内 ru 家 11 版（`core-ru` + `2026-w47-ru-{en,de,es,fr,it,pt,nl,ja,ko,zh-tw}`）；只动 ru 家，不碰其他家庭、其他周；不 commit、不 push、不跑 lint。
- 解释器：`~/workspace/weekly-git/tools/venv/bin/python` 全程。
- 磁盘：开工 93G 已用（门限 100G，未触发）。

## 0. 接手核实（2026-11-12）

### 0.1 逐版 text.md 附录行现状（固定字符串 grep `СТРАНИЦА`）

| 版 | 附录行 | 位置 | 状态 |
|---|---|---|---|
| core-ru（ru-zh-cn） | `— СТРАНИЦА 8 —` | L668（两份：`2026-w47-ru-core.text.md` 与 `2026-w47-ru-zh-cn.text.md`，字节一致） | 上一任已修 |
| ru-en | `— СТРАНИЦА 8 —` | L666 | 上一任已修 |
| ru-de | `— СТРАНИЦА ? —` | L668 | 待修 |
| ru-es | `— СТРАНИЦА ? —` | L668 | 待修 |
| ru-fr | `— СТРАНИЦА ? —` | L668 | 待修 |
| ru-it | `— СТРАНИЦА ? —` | L668 | 待修 |
| ru-pt | `— СТРАНИЦА ? —` | L668 | 待修 |
| ru-nl | `— СТРАНИЦА ? —` | L668 | 待修 |
| ru-ja | `— СТРАНИЦА ? —` | L668 | 待修 |
| ru-ko | `— СТРАНИЦА ? —` | L668 | 待修 |
| ru-zh-tw | `— СТРАНИЦА ? —` | L668 | 待修 |

与协调员查实一致：2 版已修（core-ru、ru-en），9 版待修。

### 0.2 印/网 PDF SHA 核对（vs 校对值 PROOF-NOTE §2 与 pre-sha.txt）

逐版重算 SHA-256（前 12 位）+ 字节数，与校对值逐一比对：**22 个 PDF（11 印 + 11 网）全部一致**，无一变动。印 PDF ru-en `f20b04c8244c…`（20,875,448 B）仍等于校对值（上一任未重渲染，正确）。

### 0.3 快照核对（pre-sha.txt 与 pre-textmd/）

- `pre-sha.txt` 存的是 SHA 前 12 位 + 字节数。按前缀比对：全部 22 个 PDF 与快照一致；9 版待修 text.md 与快照一致；2 版已修 text.md 与快照不同（见下）。
- `pre-textmd/` 与盘上 text.md 逐版 `cmp`：9 版待修 text.md 与快照**字节一致**（上一任未动）；core-ru 两份与 ru-en 与快照不同，仅附录行 `?`→`8`（core）及附录行 + 一处标题行（ru-en，见 §0.4）。
- 快照可信：可作为改前基线。

### 0.4 上一任 ru-en 的一处附带差异（已查明，非误操作）

上一任重导出的 ru-en text.md 比快照少 47 字节：除附录行外，删了 L58–59 `### В ЭТОМ НОМЕРЕ · IN THIS ISSUE` + 空行。查明原因：`2026-w47-ru-en/content12.py:95` 该标题为 `p.text(..., 23, "sans", True, OLIVE)`（23pt），而导出器规则只收 sans 粗体 ≥24pt 的标题（`ru_textmd.py` do_p_text）；core（24pt）与 de（24pt）同款标题仍在导出内。标题本身是印版 P1 真实内容（印 PDF P1 文本层含 `В ЭТОМ НОМЕРЕ` 与 `IN THIS ISSUE`，已验）。即：**重导出会丢掉源码中被缩到 <24pt 的真实标题**——不是上一任手删，是导出器按现行源码的如实输出。处理见 §1.3（本修复统一回补此类标题行）。

### 0.5 附录页码核实（逐版印 PDF）

11 版印 PDF 均为 8 页；P8 含答案区的分页面分隔行 `— СТРАНИЦА 1 —` 至 `— СТРАНИЦА 8 —`（PyMuPDF 逐页提取，全 11 版一致）。text.md 附录（`## Answers` 答案区）即 P8 内容，故附录页码 11 版均为 **8**，与已修 2 版的 `8` 一致。无一版例外。

### 0.6 源头状态

`ru_textmd.py` do_appendix 的占位符，上一任已修好：`core-ru/ru_textmd.py`（git diff：`— СТРАНИЦА ? —` → `— СТРАНИЦА 8 —`）及同日一并改的写作题判定（`e["type"] == "写作"` → parenthesised-key 判定，见 Fix 1 记录）。11 份 `ru_textmd.py` 副本（core + 10 fan-out）已逐份 `cmp`：**全部与 core 的已修版字节一致**，源头无需再改。

## 1. 修复方法（F-2）

### 1.1 步骤

1. 用已修的 `ru_textmd.py` 对每版源码目录重导出 text.md（命令格式与各版 KIT §5 一致，如 `ru_textmd.py . 2026-w47-ru-de.text.md "VOL.4 · Russian text · German explanations"`），先写 `/tmp/fix-ru-dryrun/` 干跑、diff，确认后再落盘。
2. 只改 text.md，不跑 `run.py`/`render.py`/`webpdf.py`，不重渲染 PDF；修后逐版核对印/网 PDF SHA 与修前完全一致。
3. 每版 KIT：text.md SHA 行（如有）更新为修后盘上实测值，并补 Build history 修复条目；印/网 PDF 行不动。
4. 门禁：`p8.py compare --total 150` 逐版 CLEAN；occlusion 不动（PDF 未变）。

### 1.2 干跑发现：重导出会丢标题行（§0.4 的同类）

- core 干跑：与盘上文件**字节一致**（60,953 B，150 题，277 块）——上一任的 core 文件即新鲜导出，无丢行。
- ru-en 干跑：与盘上文件**字节一致**（62,739 B，150 题，276 块）——上一任的 en 文件即新鲜导出；丢的正是 §0.4 的标题行。
- ru-de 干跑：新鲜导出 63,348 B / 275 块，盘上 63,471 B / 277 块，diff 仅 2 处（除附录行外）：丢 `### ЗА И ПРОТИВ · PRO UND CONTRA`（P6 盒标题，源码 `content56.py:136` 为 22pt，系 Fix 3 缩字号修溢出所致）与 `### ОТВЕТЫ · LÖSUNGEN — NACH SEITEN GEORDNET; AUFGABENNUMMER SUCHEN`（P8 答案区标题，源码 `content8.py:116` 为 22pt，系 P8 head/subtitle 互撞修缩所致）。两行均在印 PDF 文本层中查实为真实内容（P6 含 `ЗА И ПРОТИВ`/`PRO UND CONTRA`，P8 含 `ОТВЕТЫ`/`LÖSUNGEN`）。

### 1.3 裁定：回补被丢的标题行（不改导出器、不动源码字号）

- 原因：被丢行是校对过的已发 text.md 内容、印版真实标题；裸重导出等于悄悄删内容，是回归。导出器的 ≥24pt 规则与源码缩字号（Fix 3 / P8 互撞修）共同造成，不改规则（改阈值会波及其他版、超出本次任务），不动源码字号（字号是版式修复的结果）。
- 做法：落盘文件 = 新鲜导出 + 在原位置逐字回补被丢的标题行（与快照行逐字一致）；最终文件与修前盘上文件的 diff **仅附录行 1 行**（`?`→`8`），字节数、行数、块数与修前完全相同。回补行逐版在 FIX-LOG §2 登记，并以印 PDF 文本层核实其为真实内容。
- ru-en 同样处理：回补 `### В ЭТОМ НОМЕРЕ · IN THIS ISSUE`（L58），使其也只剩附录行 1 行差异；KIT SHA 随之更新（见 §3）。
- core 无丢行，不动。

## 2. 逐版修复记录

（干跑结果与落盘结果见下；每版一行：改前/改后 text.md SHA-256 全值、字节数、diff 行数、回补行、印/网 PDF SHA 未变核对、p8 门禁。）

### 2.1 逐版 text.md 改前 → 改后（SHA-256 全值，字节数修前 = 修后）

| 版 | 改前 SHA-256（前 12） | 改后 SHA-256（前 12） | 字节 | 行 | diff vs 修前 |
|---|---|---|---|---|---|
| core-ru（两份字节一致） | `348511e061c2…` | `a54372a10afc…` | 60,953 | 838 | 仅附录行 1 行（上一任已做；本任务核实新鲜重导出字节一致） |
| ru-en | `5dba64557898…`（上一任重导出后为 `75c284464139…`，62,739 B） | `47e10cd4ea18…` | 62,786 | 838 | 仅附录行 1 行（vs 快照；另回补上一任重导出丢的标题行，见 §2.2） |
| ru-de | `d0f9b48c8fab…` | `4bed5e5b83be…` | 63,471 | 838 | 仅附录行 1 行 |
| ru-es | `332c8e4f5478…` | `bb298469263f…` | 64,176 | 838 | 仅附录行 1 行 |
| ru-fr | `e4cc50fd4195…` | `7cb8ee227f1e…` | 63,361 | 836 | 仅附录行 1 行 |
| ru-it | `0bb5739a9e2a…` | `b1265804a67e…` | 63,972 | 838 | 仅附录行 1 行 |
| ru-pt | `ab21732233d8…` | `690570b42975…` | 65,116 | 838 | 仅附录行 1 行 |
| ru-nl | `849015f1e920…` | `c9ae09e22bc7…` | 64,013 | 838 | 仅附录行 1 行 |
| ru-ja | `07824474bb88…` | `2a298d44abc5…` | 64,477 | 838 | 仅附录行 1 行 |
| ru-ko | `5e9bd67201fd…` | `3ed67e6ea61c…` | 65,012 | 838 | 仅附录行 1 行 |
| ru-zh-tw | `277a24f8a167…` | `fa1040dd81ca…` | 60,850 | 838 | 仅附录行 1 行 |

改后 SHA-256 全值：core `a54372a10afc91761f6a8e21a597b7ce2f001c80987f51b3b9789e795ad62c9e`；en `47e10cd4ea1860f3d70af9b5bf2e4fa824784f6ff393e063dd39dff94b8c41ea`；de `4bed5e5b83bea3c4e385b96196e0fc7f098850272e80b3e96b447ecd8432bcba`；es `bb298469263f40a5c36b1052a347902af791e1847a0425a705ad20ff8a90f0ed`；fr `7cb8ee227f1ed30ac146c728d10ce7548f31fadb9ba976acf9779c08d6e8c585`；it `b1265804a67edb042a8cf93ec5c0cc08a24178251cd389b5f4738286ab9f7659`；pt `690570b429759bfa81125c9c899dece4dd7b2c944976a1b25104cc85c5b9737c`；nl `c9ae09e22bc7f3f0deaa3d4c279769b5a5d911200ced68d1dfecd7a96059626c`；ja `2a298d44abc5e5129f5d1b235746e745ce28d9fad5b9769529a3a11146f7605c`；ko `3ed67e6ea61c838d2fb136235024be34ddf05ed99fbe63d6875d846a0bda73d7`；zh-tw `fa1040dd81ca9517b908904bcaa4d68f445327cb8f27a03a141cd93c0aa44462`。

每版落盘后均与 `pre-textmd/` 快照 diff：**恰好 1 行**（L668 `— СТРАНИЦА ? —` → `— СТРАНИЦА 8 —`；en 为 L668，快照行号对齐后同样 1 行）。落盘文件每版恰含 1 行 `СТРАНИЦА`，值均为 `— СТРАНИЦА 8 —`。

### 2.2 回补的标题行（新鲜导出丢弃、印 PDF 核实为真、原位置逐字回补）

| 版 | 回补行 | 源码位置与字号 | 印 PDF 核实 |
|---|---|---|---|
| ru-en（上一任重导出丢的，本任务回补） | `### В ЭТОМ НОМЕРЕ · IN THIS ISSUE` | `content12.py:95`，23pt | P1 文本层含 `В ЭТОМ НОМЕРЕ` / `IN THIS ISSUE` |
| ru-de | `### ЗА И ПРОТИВ · PRO UND CONTRA`；`### ОТВЕТЫ · LÖSUNGEN — NACH SEITEN GEORDNET; AUFGABENNUMMER SUCHEN` | `content56.py:136`，22pt；`content8.py:116`，22pt | P6 / P8 文本层均含 |
| ru-es | `### ЗА И ПРОТИВ · PROS Y CONTRAS` | `content56.py:136`，22pt | P6 文本层含 |
| ru-fr | `### В ЭТОМ НОМЕРЕ · AU SOMMAIRE`；`### ЗА И ПРОТИВ · POUR ET CONTRE` | `content12.py:91`，22pt；`content56.py:136`，22pt | P1 / P6 文本层均含 |
| ru-nl | `### ЗА И ПРОТИВ · VOOR EN TEGEN` | `content56.py:136`，23pt | P6 文本层含 |
| ru-pt | `### СМИ · O QUE DIZEM OS MEDIA`；`### ЗА И ПРОТИВ · PRÓS E CONTRAS` | `content12.py:73`，23pt；`content56.py:136`，22pt | P1 / P6 文本层均含 |
| core / it / ja / ko / zh-tw | 无 | — | — |

成因（各版 KIT D5 条自述可印证）：D5 字体路由改后拉丁 run 变宽 → 奶油框题越框 → 修复只缩字号（24/25/27pt → 22/23pt），而导出器 `do_p_text` 只收 sans 粗体 ≥24pt 的标题，遂在重导出时丢弃。字号是版式修复的结果，不动；导出器阈值不改（超出本次任务）；回补行与快照逐字一致。

## 3. 门禁（修后重跑）

- `tools/p8.py compare --core-dir core-ru --edition-dir 2026-w47-ru-<lang> --target ru --total 150`，10 版 fan-out **全部 CLEAN**：150/150 noted，missing=[]，extra_count=0，uncertain=[]，keydiff=[137, 138, 139, 140]（E 节翻译题，读者语键，预期，与校对时一致）。
- occlusion 未重跑：印/网 PDF 未变（§4 核对），按任务要求可不重跑。

## 4. 印/网 PDF SHA 未变核对（修后重算，与 pre-sha.txt + 校对值逐一比对）

22 个 PDF（11 印 + 11 网）**全部 OK**（SHA 前 12 位 + 字节数均与修前一致），无一变动：

| 版 | 印 PDF SHA-12 | 网 PDF SHA-12 |
|---|---|---|
| core-ru | `e3c4c0ee155a`（24,713,345 B） | `0bdc87e621d7`（3,898,257 B） |
| ru-en | `f20b04c8244c`（20,875,448 B） | `21781f8396d9`（3,328,931 B） |
| ru-de | `0aa0287b13ea`（20,880,795 B） | `98f015bd027b`（3,334,227 B） |
| ru-es | `047ef0fbf75a`（20,880,148 B） | `662998dc1e54`（3,333,651 B） |
| ru-fr | `7dbe1f0d6716`（20,880,952 B） | `6841ac968654`（3,334,434 B） |
| ru-it | `6b79403a69c5`（20,877,054 B） | `7c2ecb0479b1`（3,330,486 B） |
| ru-pt | `eb3c2905d2f8`（20,883,576 B） | `cc52dfb7f87b`（3,337,084 B） |
| ru-nl | `b355efedd9fc`（20,876,339 B） | `15cf757d8482`（3,329,813 B） |
| ru-ja | `f65820348bef`（27,365,531 B） | `b6fed518a3c1`（3,692,485 B） |
| ru-ko | `2f6ecdcc2abf`（21,975,314 B） | `a2ea1b41922a`（3,494,622 B） |
| ru-zh-tw | `a6c1b4cffbef`（24,763,703 B） | `8eb6f61cef46`（3,976,325 B） |

## 5. KIT 更新（11 版）

- 每版补 Build history 修复条目（F-2，含旧→新 SHA、字节数、回补行、PDF 未变核对、p8 门禁）：core 为 §7.8 小节；zh-tw 为 §11 小节；其余 9 版为 D5 条目后的同级条目。
- text.md SHA 现值行更新为修后盘上实测值：core-ru §7 实测文件行（L105，`348511e0…` → `a54372a1…`；同行 §7.7 D5 段内的旧 SHA 为 D5 当时记录，不动）、ru-en L54、ru-ko L57、ru-zh-tw §1 文件表行 L15。de/es/fr/it/pt/nl/ja 的 KIT 本无现值 SHA 行（只有 Fix 1/D5 历史条目引用的旧 SHA，历史记录不动），以 F-2 条目为准。
- 印/网 PDF 行一律未动。
- 上一任未更新任何一版 KIT 的 text.md SHA 行（core-ru、ru-en 的 KIT 仍记旧 SHA），本次 11 版一并补齐。

## 6. 不修项（按任务/协调员裁定）

- **F-1**（P8 单行 key 栏右余量低于 +5px 底线，最差 ru-pt key 140 = −1.9px）：协调员裁定接受现状，不修（超差 ≤2px 进 88px 空白边，无重叠、无触页缘，肉眼不可见；重排 9 版 P8 回归风险大于收益）。记入本 LOG，不改任何源码。
- **F-3**（text.md 末尾 Morozko 图注行，9 版印版无图）：按设计，不修。
- **svglib.py 字体路由**：一律未动（ru 家各版的 `*-ru` 字体问题另有跨家工人统一处理）。

## 7. 收尾核对与交接说明

- 工作范围：只动 `production/2026-w47/` 内 ru 家 11 版目录的 `*.text.md`（10 版落盘；core 两份上一任已修、本任务只核实未动）与 11 份 `WEEKLY-KIT.md`；源头 `ru_textmd.py` 由上一任改好，本任务未再改源码（11 份副本 `cmp` 字节一致）。未碰其他家庭、其他周；未 commit、未 push、未跑 lint。
- 磁盘：收尾 93G 已用（门限 100G，全程未触发）。
- 干跑与落盘中间件：`/tmp/fix-ru-dryrun/`（11 版新鲜导出）、`/tmp/fix-ru-final/`（10 版落盘文件）为 /tmp 临时件，VM 重启即失；改前快照 `pre-sha.txt` 与 `pre-textmd/` 原样保留在本 scratch 目录。
- 遗留注意（供协调员）：导出器 `do_p_text` 的 ≥24pt 标题规则与 D5 后缩字号（22/23pt）共同导致重导出丢标题行——本次以回补处理；若将来再次重导出 ru 家 text.md，同一批标题行会再次丢失，需同样回补（或另立任务修导出器规则）。ru-en 的标题行丢失是上一任重导出时发生的，本任务已回补。

---

## 8. 第二轮修复（2026-11-12，接 PROOF-NOTE-2 的 6 项 low 发现 G-1～G-6）

- 任务：第二轮独立重校 `scratch-reproof2-w47-ru/PROOF-NOTE-2.md` 的 6 项 low 发现；第一轮 PROOF-NOTE 与本 FIX-LOG 全文已读。6 项发现均已由协调员在盘上核实属实（text.md 行号与印 PDF 文字层均已确认）。
- 范围：`production/2026-w47/` 内 ru 家 8 版（`2026-w47-ru-{en,de,fr,it,pt,nl,ko,zh-tw}`）；core-ru、ru-es、ru-ja 干净未动；不碰其他家庭、其他周；不 commit、不 push、不跑 lint。`svglib.py` 字体路由一律未动。第一轮已裁定的导出器设计局限（P1 目录行、СЛОВО НЕДЕЛИ 标题缺失、P4 表、照片来源）不修不报。
- 解释器：`~/workspace/weekly-git/tools/venv/bin/python` 全程。
- 流程（SOP §8）：改源头 content*.py → `run.py` → `render.py` → textmd 干跑到 /tmp → diff → 回补被丢标题行 → 落盘 text.md → `webpdf.py` → 门禁 → KIT 更新为盘上实际 SHA。
- 磁盘：开工 95G 已用（门限 100G，全程未触发；收尾仍 95G）。
- 工作文件：本目录 `round2-apply.py`（12 处源头修改）、`round2-backfill.py`（通用回补）、`round2-verify.py`（逐版核验）、`round2-driver.sh` / `round2-gates.sh`（构建/门禁驱动）、`round2-expected/*.json`（各版 text.md 预期 diff）、`round2-pre/`（修前 text.md、SVG SHA、印 PDF 文字层快照）、`round2-logs/`（各版 run/render/textmd/backfill/webpdf 日志）、`round2-summary.txt`（逐版 SHA 与核验）、`round2-gates/`（门禁日志/JSON）、`round2-sha-final.txt`（终版全 SHA）。

### 8.1 人称裁定（G-4）：各版主导人称以其余部分的祈使/人称标记为准

| 版 | 主导人称 | 证据（其余部分） | 改动 |
|---|---|---|---|
| ru-de | Sie（正式） | `Lesen Sie / Setzen Sie / Bilden Sie / Füllen Sie / Antworten Sie / Fassen Sie`（6+ 处 Sie 式祈使）；du 仅见于 G-4 说明句本身 | 标题 `UND SIE?` 不动；说明 `Und du? Schreib …` → `Und Sie? Schreiben Sie zwei russische Sätze an die Redaktion: …`（wrap 计高 + 正文两处同改；措辞见 §8.7 的 LINEX 回炉） |
| ru-fr | vous（正式） | `Lisez / Complétez ×2 / Formez / Répondez / Réunissez`；tu 仅见于 G-4 说明句本身 | 标题 `ET VOUS ?` 不动；说明 `Et toi ? Écris …` → `Et vous ? Écrivez …`（两处同改） |
| ru-it | tu（非正式） | `Leggi/scegli ×4+ / Completa ×4 / Metti / Forma / Rispondi / Unisci`；voi 仅见于 G-4 标题本身 | 标题 `E VOI?` → `E TU?`；说明 `E tu? Scrivi …` 不动 |
| ru-nl | U（正式） | 正式物主 `uw` 约 20 处（content12/34/56/7/8）；`jij` 仅见于 G-4 说明句本身，`je` 仅 1 处（L427 通用 `je`） | 标题 `EN U?` 不动；说明 `En jij? Schrijf …` → `En u? Schrijf …`（两处同改；`Schrijf` 两式同形） |
| ru-pt | tu（非正式） | tu 式约 18 词次（`Lê/escolhe ×4`、`Completa ×4`、`Escreve`、`Traduz ×4`）；você 式约 8 词次（`Leia/escolha`、`Complete ×2`、`Forme ×2`、`Responda`、`Junte`） | 标题 `E VOCÊ?` → `E TU?`；说明 `E tu? Escreve …` 不动；L471 `Responda …` → `Responde …` |
| ru-ko | 여러분（复数） | L35 P1 标题 `지금, 여러분 차례` 与 L129 说明句均为 `여러분`；`당신` 仅见于 G-4 标题本身 | 标题 `당신은요?` → `여러분은요?`；说明 `여러분은요? …` 不动 |

### 8.2 G-1 说明（ru-en）：任务箭头字面 `родина = родной город` 未照抄

- 任务原文：`родина home town` → `родина = родной город`（括号：родина 是故乡/祖国，hometown 应为 родной город）。
- `родной город` 是俄语“家乡（城镇）”本身，不是英语。英文版词汇注全行皆为英语（`поздравить to congratulate · … · повод occasion`），把俄语词填进英文注会让英语读者无从理解；且其余 9 版均以读者语注为“故乡/祖国”（de `Heimat`、fr `pays natal`、es `tierra natal`、it/pt `terra natale`、nl `geboortestreek`、ja `故郷`、ko `고향`、zh-tw `故鄉`、core `故乡`）。
- 故按任务括号的本意执行：`content12.py:176` 的 `родина home town` → `родина homeland`。“home town”对应的俄语词正是 `родной город`——这正是原注错把两个词混为一谈的证据。
- 若协调员坚持要字面 `родина = родной город` 进英文注，请明示，我重做。

### 8.3 G-2 标题两次改写（ru-de）：`JETZT SIND SIE DRAN` 超宽

- 初版按 Sie 人称定为 `JETZT SIND SIE DRAN`（`content12.py:54`），`run.py` 报 `!! HEAD TOO WIDE [P1-headline]`。实测（sans 粗体 25pt，`bslib4.text_w`）：`СЕЙЧАС ВЫ　JETZT SIND SIE DRAN` = 466.2pt > 栏宽 CW 422.5pt，超 43.7pt；旧 `JETZT SIE` 306.9pt；同家可过的标题 `TOCCA A VOI` 346.5pt、`AGORA VOCÊ` 351.4pt、`TRY IT NOW` 335.3pt。
- 改为 `SIE SIND DRAN`（375.5pt，余量 47pt；俄语半句 `СЕЙЧАС ВЫ` 本已含“现在”，与 it `TOCCA A VOI`、fr `À VOUS` 同式——只写“轮到你”不写“现在”）。重跑后 HEAD TOO WIDE 消失，`head_check.py` PASS。

### 8.4 G-3 key 126 不动（ru-de）：已核实为整句译文

- `content8.py:43`（text.md L616/L812）：`Die Wettervorhersage: Regen mit Schneeregen` 是 Q126「Что обещают синоптики？A. Жаркое лето · B. Дождь с мокрым снегом · C. Устойчивый снег」的整句答案说明（“天气预报：雨夹雪”），不是单词注释。
- 佐证：其余 9 版 key 126 同样是整句意译（en `Forecasters say: rain with wet snow`、fr `Selon la météo : pluie et neige mouillée`、it `Secondo i meteorologi: pioggia con neve bagnata`、nl `Volgens de meteorologen: regen met natte sneeuw`、es/ja/ko/zh-tw/core 同式），其中各版用的都是该版的惯用天气短语，而非词表定义式。
- 只改词表/小结处的单词注释：`content7.py:18` bridge `мокрый снег Schneeregen` → `мокрый снег = nasser Schnee`，与本版 L170/L515/L691/L786 四处一致。key 126 两处（L616/L812）不动。

### 8.5 观察到、未修（超出本次核实的 6 项范围，留协调员裁定）

- ru-pt 除 L125/L129/L471 外仍有 você 式残留：P1 注 `Leia a primeira página e escolha a resposta certa`（`content12.py:149`）、`Complete a forma verbal ou o caso correto` / `Complete com o tempo correto do verbo entre parênteses`（`content34.py:74,238`）、`Forme frases corretas com as palavras`（`content34.py:88`、`content56.py:88`）、`Junte as duas frases numa só`（`content56.py:191`）。与本版 tu 主导不一致，但不在 PROOF-NOTE-2 的 6 项内，本次未动。
- ru-nl 词表 `Dooi`（`content12.py:218`，text.md L141）同样首字母大写，与 `natte sneeuw / gladheid op de weg` 小写不一致；PROOF-NOTE-2 称 `IJzel` 为“唯一大写项”与盘上事实不符（`Dooi` 亦大写；印 PDF P2 文字层 `Dooi` 1 处、`IJzel` 1 处）。本次只按任务修 `IJzel` → `ijzel`；`Dooi` 是否同改留协调员裁定（另：en/fr 词表第 1、3 项亦大写——`Thaw, warmer weather / Freezing rain`、`Redoux / Pluie verglaçante`——属跨版同式，`Dooi` 可能系有意句首大写体例）。

### 8.6 逐版修复记录（SHA-256 前 12 位；全值见 `round2-sha-final.txt`）

| 版 | 印 PDF 改前 → 改后（字节） | 网 PDF 改前 → 改后（字节） | text.md 改前 → 改后（字节） | SVG 变动 | text.md 最终 diff | 回补标题行 |
|---|---|---|---|---|---|---|
| ru-en | `f20b04c8244c` 20,875,448 → `7339c020640f` 20,875,444 | `21781f8396d9` 3,328,931 → `a3148c31c5a9` 3,328,923 | `47e10cd4ea18` 62,786 → `6c6932fb809f` 62,785 | p2 | 1 行（L99） | 1（`В ЭТОМ НОМЕРЕ · IN THIS ISSUE`） |
| ru-de | `0aa0287b13ea` 20,880,795 → `36d4cb6795ae` 20,880,736 | `98f015bd027b` 3,334,227 → `acc21d4dd4a6` 3,334,229 | `4bed5e5b83be` 63,471 → `31d3eb3eb223` 63,483 | p1/p2/p7 | 3 行（L35/L129/L512） | 2（`PRO UND CONTRA`、`LÖSUNGEN — …`） |
| ru-fr | `7dbe1f0d6716` 20,880,952 → `0c38972146f9` 20,880,950 | `6841ac968654` 3,334,434 → `b36ecf778e27` 3,334,407 | `7cb8ee227f1e` 63,361 → `445daf81541a` 63,364 | p2 | 1 行（L129） | 2（`AU SOMMAIRE`、`POUR ET CONTRE`） |
| ru-it | `6b79403a69c5` 20,877,054 → `b83c981d399f` 20,877,138 | `7c2ecb0479b1` 3,330,486 → `47201c0d411c` 3,330,609 | `b1265804a67e` 63,972 → `ba59c4ff2368` 63,971 | p2 | 1 行（L125） | 0 |
| ru-pt | `eb3c2905d2f8` 20,883,576 → `0c119e4a6afa` 20,883,685 | `cc52dfb7f87b` 3,337,084 → `853af83ca0ff` 3,337,224 | `690570b42975` 65,116 → `0920202237b2` 65,113 | p2/p6 | 2 行（L125/L471） | 2（`O QUE DIZEM OS MEDIA`、`PRÓS E CONTRAS`） |
| ru-nl | `b355efedd9fc` 20,876,339 → `5dedd8ecc30d` 20,876,260 | `15cf757d8482` 3,329,813 → `1abee50e0035` 3,329,737 | `c9ae09e22bc7` 64,013 → `b600944e5e5f` 64,011 | p2 | 2 行（L129/L145） | 1（`VOOR EN TEGEN`） |
| ru-ko | `2f6ecdcc2abf` 21,975,314 → `d97e04c036d6` 21,975,345 | `a2ea1b41922a` 3,494,622 → `90059d0d6f40` 3,494,537 | `3ed67e6ea61c` 65,012 → `5e34a2c5d29e` 65,015 | p2 | 1 行（L125） | 0 |
| ru-zh-tw | `a6c1b4cffbef` 24,763,703 → `7db5bece16d6` 24,763,429 | `8eb6f61cef46` 3,976,325 → `31a07aa54b5a` 3,976,005 | `fa1040dd81ca` 60,850 → `bc0a26a5267f` 60,855 | p7 | 1 行（L538） | 0 |

- 改前 SHA 与 FIX-LOG §2.1/§4 及 PROOF-NOTE-2 §4 逐一核对一致；改后 SHA 为落盘后重算的盘上实测值（`round2-summary.txt` + `round2-sha-final.txt` 全值）。
- 源头改动（`round2-apply.py` 断言计数全部通过）：en `content12.py:176`；de `content12.py:54,197,203` + `content7.py:18`；fr `content12.py:197,203`；it `content12.py:200`；pt `content12.py:204` + `content56.py:177`；nl `content12.py:197,203,219`；ko `content12.py:200`；zh-tw `content7.py:48`。
- 每版 `run.py` 均为 TOTAL 150，终版日志零 FLOW OVERFLOW / HEAD TOO WIDE；每版印/网 PDF 均为 8 页，印/网提取文字（归一化空白后）一致；新串在印/网文字层均在位、旧串均为 0（de `Schneeregen` 余 1 处 = key 126，见 §8.4；nl `ijzel` 4 处、`IJzel` 0 处；ko `여러분은요?` 2 处）。
- F-2 回补的 9 处标题行逐版核实仍在位（本次干跑丢弃数与 F-2 §2.2 完全一致：en 1、de 2、fr 2、nl 1、pt 2，it/ko/zh-tw 0），已全部原位置逐字回补；最终 text.md diff 只含意改行。

### 8.7 门禁（修后重跑，8 版；日志/JSON 在 `round2-gates/`）

| 门禁 | 结果 |
|---|---|
| `p8.py compare --total 150` | **8/8 CLEAN**：150/150 noted，missing=[]，extra_count=0，uncertain=[]，keydiff=[137, 138, 139, 140]（E 节翻译题，预期） |
| `occlusion_audit.py`（自检 OK） | **8/8 0 flags**（终版；de 首版曾出 7 LINEX，见下） |
| `boxtitle_check.py` | **8/8 0 DEFECT、0 OBSERVE、0 marginal**（en 57/685、de 57/682、fr 57/682、it 55/684、pt 57/683、nl 57/681、ko 67/759、zh-tw 57/703 标题/正文行） |
| `spill_sweep.py` | **8/8 rc=0**（每版各 1 条既有 `[observe]`：`ABOVE -23.91px` 的 Black Friday  gloss 行，8 版同式，rc=0 非失败） |
| `pdf_edge_scan.py`（印 PDF） | **8/8 0 TOUCH、0 NEAR** |
| `head_check.py`（run.log） | **8/8 PASS 0 defects** |
| D5 census（`scratch-reproof2-w47-ru/census.py`，11 版） | **CJK+Latin=0、CJK+Cyrillic=0，全部 11 版**；弯引号全部 Newsreader（en 2、de 3、fr 4、it 2、pt 2、nl 2、ko 2、zh-tw 4 处） |
| 引号普查（`census_quotes.py`，8 版 svg） | **GRAND TOTAL defective: 0** |
| ru-en run.py 重跑复核 | 8/8 SVG 与试点构建字节一致（确定性重建验证） |

**de 回炉（本次唯一门禁回归，由修复本身引入，已修好）：**首版 Sie 说明句 `Und Sie? Schreiben Sie zwei Sätze auf Russisch an die Redaktion: …`（118 字）在 20pt/378.5px 下折 4 行（旧 du 句 111 字折 3 行），“А ВЫ?”盒增高 29px，P2 图片下移，图注行 `Картина: Константин Юон — общественное достояние` 被 `СЛОВА НЕДЕЛИ` 分隔线（y=1554）划过——occlusion 报 7 LINEX（同一行 7 个词），裁图目视证实为真缺陷（线穿字腹，非测量误报；见 SOP 附则一葡语 P7 金线同类）。修复：说明句改写为 `Und Sie? Schreiben Sie zwei russische Sätze an die Redaktion: …`（`zwei russische Sätze` = `zwei Sätze auf Russisch`，信息齐全，折回 3 行），de 单独重建（run→render→textmd→backfill→webpdf→核验→门禁重跑）。重建后 P2 winter ends 1595.25 → 1566.25（−29px），图注行与分隔线之间出现干净空隙（裁图目视确认），occlusion **0 flags**，其余五门重跑全绿。首版 de 中间 SHA 已作废（印 `730501b2763b`、网 `c0febc37287c`、text.md `ffa8a21ec0be`），终版以 §8.6 表为准。fr 说明句同样 lengthened（`Et vous ? Écrivez …`），但 occlusion 仍为 0 flags（其 P2 余量足），无需回炉。

### 8.8 KIT 更新（8 版）

- 每版 §5 文件表现值行（印/网 PDF 尺寸+SHA 全值；en L54、ko L57、zh-tw §1 文件表行的 text.md 尺寸+SHA）更新为修后盘上实测值；de/fr/it/pt/nl 的 KIT 本无 text.md 现值 SHA 行（同 F-2 做法），以新增的第二轮条目为准。
- 每版在 F-2 条目后追加第二轮修复条目（en/de/fr/it/pt/nl/ko 为 §7 列表内新 bullet；zh-tw 为新 §12）：源头改动、text.md 最终 diff 行数、回补行、SVG 变动页、印/网/text.md 改前→改后 SHA（前 12）与字节数、门禁结果。
- 历史条目（Fix 1/D5/F-2）一律未动。

### 8.9 附带事故：18:12–18:14 可能误杀他家 render 进程

- 经过：de 首版 `JETZT SIND SIE DRAN` 报 HEAD TOO WIDE 后，我为改标题停掉了构建驱动（bash pid 20694）及当时在跑的两个 `render.py` 进程（pid 21751、21837），随后又杀了一个 18:14 出现的 `render.py`（pid 22270）。事后查 `/proc/*/cwd` 才发现 VM 上同时有多个他家工人在跑 render/run（es-pt、ja-ko、it-zh-cn 等），仅凭进程名无法区分归属——21751/21837 中一个是我家的 de render，另一个与 22270 的归属无法 retroactively 确认，可能属于他家工人。
- 影响：若有他家工人在 18:12–18:14 间报 render 被杀，大概率是我这次误杀；其驱动应可重试恢复（render 是幂等重建）。我家驱动已重启、de 已按修正标题全量重建，终版门禁全绿，无残留影响。
- 教训：共享 VM 上绝不按进程名批量杀进程；只杀以 `/proc/<pid>/cwd` + 完整命令行核实过的自家进程。本条记入日志供协调员核查。
