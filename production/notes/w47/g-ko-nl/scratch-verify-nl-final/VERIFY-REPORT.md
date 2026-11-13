# W47 nl 家 §8.4 终态核对报告（第二轮核对 / 终态核对员）

- 核对员：§8.4 终态核对员（与建造者、proof1/2/3 校对员、fix 工人、#4 核对员 37eaae1c 均不同）
- 核对时间：2026-11-13 ~07:12–07:20 UTC
- 依据：SOP §8 / §8.4 proofread-until-zero；只核对、不修复、不重建、不 commit、不 push、不跑 lint、不改生产
- 工作目录：`hidden_files/w47/scratch-verify-nl-final/`（本报告唯一产出；无渲染、无机械门禁重跑——见下）
- 磁盘：开工 `df -h` 97G / 150G（`df -k` 已用 101,698,524 KB，低于本次纠正后的停手线 104,857,600 KB）；收尾 97G，未触停手线。配额上限约 105G（df -h 口径），余量约 8G。
- 工具：只读核对全程只用 `sha256sum` / `stat` / `find` / `grep` / `git ls-files` / `git show`（只读）；未用系统 python3 以外的任何构建工具；未对生产路径跑任何 run.py/render.py。

## 总体结论：CLEAN

- 11 版全部核对有效、无需第二阶段重校：
  - 10 版（core-nl + nl-de/en/es/fr/it/ja/ko/pt/zh-tw）：最新核对为第三轮独立重校
    PROOF-NOTE-3（2026-11-12 18:34–18:50 UTC，结论 (a) 零问题），当前磁盘三 SHA
    与该轮指纹 30/30 一致 → VERIFIED CLEAN。
  - 1 版（nl-ru）：PROOF-NOTE-3 后 SHA 变过（*-ru 重建 + fix-nl-ru2），#4 核对员已做
    全新全量重校（scratch-verify-nl/VERIFY-REPORT.md §nl-ru，结论 (a) 零问题）；
    本轮复测磁盘三 SHA 与该重校记录 3/3 一致，且核对后生产无任何改动 → VERIFIED CLEAN。
- 第二阶段重校：0 版触发（无磁盘 SHA 与核对记录不符、无核对缺失），故未做全新重校、未渲染。
- 内容待修清单：无（0 项）。KIT wave-2 清单：W-1～W-5，与 #4 报告一致、无新增（只记录，不改 KIT）。
- fanout-nl/ 删除：不影响 nl 家定稿（见 §fanout-nl）。

## 枚举核对（数量与 run-log 一致）

生产目录 `production/2026-w47/` 下 nl 家共 11 版，与 run-log 所称一致：

- `core-nl`（版名 2026-w47-nl-zh-cn）+ 10 个 `2026-w47-nl-*` 目录：
  nl-de、nl-en、nl-es、nl-fr、nl-it、nl-ja、nl-ko、nl-pt、nl-ru、nl-zh-tw。
- 另有 10 个 `2026-w47-*-nl` 目录（de-nl、en-nl … zh-tw-nl）属其他目标语家（读者语 nl），
  不计入 nl 家；未纳入本次核对。

## 最新核对记录确认（逐版时效核对）

- 全家最新一轮完整重校：`scratch-reproof3-w47-nl/PROOF-NOTE-3.md`（2026-11-12 18:34–18:50 UTC，
  第三轮独立重校员，结论 (a) 零问题；指纹 33/33 与修复记录一致；机械门禁全绿：
  gates 10/10 ALL PASS、boxtitle 11 版 0 DEFECT、spill 11 版 0 SPILL、edge 11 版 0 TOUCH/NEAR、
  core occlusion 0 flags、core p8 150/150、D5 census 11 版 PASS、全家 ASCII 直引号 0）。
  `scratch-reproof-nl4/`、`scratch-reproof-nl5/` 的 PROOF-NOTE 均为 2026-11-11 的 core-nl
  单版 fix4/fix5 复校（(b)/(a)），已被 PROOF-NOTE-3 取代，非最新记录。
- nl-ru 例外：PROOF-NOTE-3 后印/网 SHA 变过——*-ru 重建（2026-11-12 23:43 UTC，
  印 `5541fc59…`）+ fix-nl-ru2 四处盒题降字号（2026-11-13 01:12–01:35 UTC，
  印 `d4f08158…`）。#4 核对员（工人 37eaae1c）已对此版做全新全量重校并记入
  `scratch-verify-nl/VERIFY-REPORT.md` §nl-ru（结论 (a) 零问题，0 新发现，观察项 O-1
  `de editie — раз` gloss 非缺陷；run-log L5134 协调员收录）。
- #4 核对后变动核查（2026-11-13 05:13 UTC 之后）：
  - `find production/2026-w47/core-nl production/2026-w47/2026-w47-nl-* -newermt '2026-11-13 05:13 UTC'` → 0 个文件。
  - run-log L5134–L5216（05:14–07:10 UTC，协调员 #5/#6）：内容只涉封面（图片重制、caption/alt
    补丁、页号核实）、es-ru F1 修复 + 第八轮重校、de round-3/round-4；无任何 nl 版生产改动。
  - ledger.md：最后 nl 相关条目止于 2026-11-12（ru 重建波次、U+201C 修复、网 PDF 重建）；
    05:13 UTC 后无 nl 条目。
  - 05:13 UTC 后新建的 scratch 目录（scratch-fix-esru-f1、scratch-reproof8-w47-esru、
    scratch-reproof-de-round3/round4、scratch-verify-{en,ko,it,ja,zh-cn}-final）均非 nl 版；
    无针对 nl 版的新建 fix/reproof 目录。

## SHA-12 表（磁盘实测 2026-11-13 ~07:15 UTC；印 / 网 / text.md）

| 版 | 印 PDF（SHA-12 / 字节） | 网 PDF（SHA-12 / 字节） | text.md（SHA-12 / 字节） | vs 最新核对 | 结论 |
|---|---|---|---|---|---|
| core-nl（nl-zh-cn） | `0c5d63b942d2` / 13,830,540 | `2b6f223eaff9` / 1,874,709 | `aa1f470353f9` / 44,087 | = PROOF-NOTE-3 | VERIFIED CLEAN |
| nl-de | `9032021929da` / 12,104,245 | `fbf0c25a503a` / 1,536,368 | `6825c35db04c` / 46,247 | = PROOF-NOTE-3 | VERIFIED CLEAN |
| nl-en | `7e35b073ade0` / 12,102,396 | `c7ffd6676cfa` / 1,534,493 | `e3273f300f42` / 45,136 | = PROOF-NOTE-3 | VERIFIED CLEAN |
| nl-es | `06f0e2e00aec` / 12,107,932 | `7025ce05d975` / 1,540,051 | `672bd4c0080c` / 47,648 | = PROOF-NOTE-3 | VERIFIED CLEAN |
| nl-fr | `08f57ec27d86` / 12,106,421 | `1b429a3ff61e` / 1,538,511 | `f1d1154442c4` / 47,744 | = PROOF-NOTE-3 | VERIFIED CLEAN |
| nl-it | `dc91af0aa78d` / 12,102,273 | `9eff96cf487a` / 1,534,364 | `e9880da2da99` / 47,194 | = PROOF-NOTE-3 | VERIFIED CLEAN |
| nl-ja | `b886a483f641` / 18,803,540 | `2b38c2547606` / 1,967,732 | `b7e5f5dc8b48` / 47,804 | = PROOF-NOTE-3 | VERIFIED CLEAN |
| nl-ko | `e7fa69a263fe` / 13,871,386 | `218aebe12b4b` / 1,791,786 | `e13db87160d1` / 47,576 | = PROOF-NOTE-3 | VERIFIED CLEAN |
| nl-pt | `e2fe3b3a9568` / 12,110,707 | `40c51869695b` / 1,542,854 | `67516e2163c8` / 47,365 | = PROOF-NOTE-3 | VERIFIED CLEAN |
| nl-ru | `d4f081587c7d` / 12,261,013 | `7a06f80d9238` / 1,674,522 | `dd1c0c087c46` / 57,909 | 印/网 ≠ PROOF-NOTE-3（`bb407a7b067e` / `1c13bb4f7311`），= #4 全新重校记录；文 = PROOF-NOTE-3 | VERIFIED CLEAN（#4 重校 (a) 仍有效） |
| nl-zh-tw | `3fd293bfef56` / 13,887,537 | `542c6f1bc8e2` / 1,976,266 | `bf1f627d1bbf` / 44,308 | = PROOF-NOTE-3 | VERIFIED CLEAN |

- mtime 佐证（证明后无改动）：10 版印/网/text.md mtime 均 ≤ 2026-11-12 18:19 UTC
  （早于 PROOF-NOTE-3 结束 18:50 UTC 的门禁收尾；fr text.md 2026-11-11 17:28 UTC）；
  nl-ru 印/网 mtime 2026-11-13 01:20/01:21 UTC、text.md 2026-11-12 16:15 UTC，
  均早于 #4 核对（05:13 UTC）。11 版 KIT mtime 最晚为 nl-ru 2026-11-13 01:27 UTC，
  同样早于 #4 核对。
- 33 个 SHA 与 #4 报告（scratch-verify-nl/VERIFY-REPORT.md）逐字节一致；
  与 PROOF-NOTE-3 指纹表 30/30 一致（nl-ru 印/网 2 项为已知的重建后新值，文 1 项一致）。

## KIT §7 核对（本人脚本实测，非转述 #4）

逐版核对 KIT「Files delivered」节记录的 SHA 与磁盘实测（脚本：对每版三件磁盘 SHA-12
在 KIT 全文 grep，定位命中行与所属小节）：

| 版 | 印 SHA | 网 SHA | text.md SHA | 备注 |
|---|---|---|---|---|
| core-nl | §7 无 SHA 行 | §7 无 SHA 行 | §7 无 SHA 行 | 三值仅见于 §18 D5 rebuild（L256/259），与磁盘一致（wave-2 W-1） |
| nl-de | ✓ 一致（L19） | ✓ 一致（L21） | ✓ 一致（L25） | — |
| nl-en | ✗ 陈旧 | ✗ 陈旧 | ✗ 陈旧 | §7 Deliverables 行（L52）仍为 round-2 fix 后值：印 `d87a5242…`/12,102,271 B、网 `db7a9ace…`/1,534,348 B、文 `9596c4ac…`/45,115 B；当前值只在 §12 D5 rebuild（L126），与磁盘一致（wave-2 W-2） |
| nl-es | ✓ 一致（L19） | ✓ 一致（L21） | ✓ 一致（L25） | — |
| nl-fr | ✓ 一致（L19） | ✓ 一致（L21） | §7 缺 text SHA 行（仅 47,744 B，L23） | 当前文 SHA 只在 D5/fix 节（L127/138）（wave-2 W-3） |
| nl-it | ✓ 一致（L19） | ✓ 一致（L23） | §7 只有旧值（L29：`f1d9e3f5…` pre-D5 / `62142f93…` 更早） | 当前文 SHA `e9880da2…` 只在 D5 节（L260）（wave-2 W-4） |
| nl-ja | ✓ 一致（L19） | ✓ 一致（L23） | §7 缺 text SHA 行（仅 47,804 B） | 当前文 SHA 只在 D5 节（L155）（wave-2 W-3 同类） |
| nl-ko | ✓ 一致（L19） | ✓ 一致（L22） | §7 缺 text SHA 行（仅 47,576 B） | 当前文 SHA 只在 D5 节（L143）（wave-2 W-3 同类） |
| nl-pt | ✓ 一致（L19） | ✓ 一致（L21） | §7 缺 text SHA 行（仅 47,365 B） | 当前文 SHA 只在 D5 节（L162）（wave-2 W-3 同类） |
| nl-ru | ✓ 一致（L19，已同步 fix 后值） | ✓ 一致（L21，已同步 fix 后值） | §7 缺 text SHA 行（仅 57,909 B，L23） | 当前文 SHA 在 D5/fix-nl-ru2 节（L158/167/178）（wave-2 W-3 同类） |
| nl-zh-tw | ✓ 一致（L21） | ✓ 一致（L27） | §7 只有 build-2 旧值（L36：`54d20ccd…`） | 当前文 SHA `bf1f627d…` 只在 fix 节（L199）（wave-2 W-5） |

Wave-2 清单汇总（KIT 记录口径，不改 KIT；不影响内容定稿；与 #4 报告逐项相同，无新增）：
- W-1：core-nl §7 无 SHA 行（当前值在 §18，与磁盘一致）。
- W-2：nl-en §7 三 SHA 全陈旧（round-2 fix 后未同步 Deliverables 行）。
- W-3：nl-fr / nl-ja / nl-ko / nl-pt / nl-ru §7 缺 text.md SHA 行（仅尺寸）。
- W-4：nl-it §7 text SHA 只有旧值（pre-D5 `f1d9e3f5…`）。
- W-5：nl-zh-tw §7 text SHA 只有 build-2 旧值（`54d20ccd…`）。

## fanout-nl/ 删除核查（跟进待查项）

- 事实：`production/2026-w47/fanout-nl/` 在磁盘上不存在（`ls` 报 No such file or directory）。
  `git ls-files`（只读）显示该目录下仍有 9 个被跟踪文件，均为 `.text.md`：
  nl-de、nl-en、nl-es、nl-fr、nl-it、nl-ja、nl-ko、nl-pt、nl-ru 各一（core-nl 与 nl-zh-tw
  从未在 fanout-nl/ 下）。
- 主目录核查：11 版 `.text.md` 全部在位——`production/2026-w47/core-nl/2026-w47-nl-zh-cn.text.md`
  与 `production/2026-w47/2026-w47-nl-*/2026-w47-nl-*.text.md` 各 431 行，
  SHA 与上表（即 PROOF-NOTE-3 / #4 重校记录）逐字节一致。
- 新旧对照（只读 `git show HEAD:fanout-nl/…` 与主目录逐版 diff）：被删的 9 份是**旧版**
  副本（430 行量级，缺失其后多轮修复内容，例如 nl-de 旧版 `IN DIESER AUSGABE`→新版 `AUSGABE`、
  nl-es/nl-fr 旧版缺失 `Stand Eredivisie na 12 ronden…` 一行、nl-ru 旧版 `16 ноября: Германия`→
  新版 `16 ноября: Германия – Нидерланды, Берлин`；nl-pt 差异最大，364 行 diff——旧版习题
  答案格式亦为更早形态）。主目录的 11 份是经 D5 重建、第二轮修复、*-ru 重建、fix-nl-ru2
  之后定稿的版本。
- 结论：fanout-nl/ 删除**不影响 nl 家定稿**——被删文件无任何独有内容（均为已被取代的旧版
  text.md 副本），权威的 `.text.md` 均在主目录且 SHA 与核对记录一致。run-log L4867 与
  ledger L1453 已有相同定性（搬家残留、内容在新址完好）。本项只报事实，未做任何修复
  （未恢复文件、未动 git 状态）。

## 待修清单

- 内容待修：无。nl 家 11/11 内容定稿（proofread-until-zero 达成，终态核对确认有效）。
- KIT wave-2：上表 W-1～W-5（记录口径，待 wave-2 统一处理）。
- 观察项 O-1（nl-ru `de editie — раз` gloss）：#4 已记为非缺陷、不派修；本轮无新观察。

## 附录：SHA-256 全值表（磁盘实测 2026-11-13 ~07:15 UTC）

| 版 | 印 PDF | 网 PDF | text.md |
|---|---|---|---|
| core-nl | `0c5d63b942d2a024694e87ba27b85b3eff0b3d411e78f9956094b5f2a4383be4` | `2b6f223eaff9afa7445c54b385213e8131eeddf11b9ae9a139388b32da7f940d` | `aa1f470353f9fa24bdec29028e596dd924387fe7d05956f208a57006025e2327` |
| nl-de | `9032021929da68607da8097bd50612aeec93f4b5de76d0e15e8757712172fb19` | `fbf0c25a503a8fb532b60dc60d1b95b265a00659df1c69afb334b6bddf299795` | `6825c35db04c62e1bec4f8f6e6a511597a17af0b02b17bc5260a560043575785` |
| nl-en | `7e35b073ade00c564981bfee31526d1f6306c86e9c9ff3ae58199a278f9426af` | `c7ffd6676cfa31798994f11af35a469485e6fefd1fa3a8e079c47c7aae3b0d95` | `e3273f300f42236a06faaddd3302b5be1a4a340adca285efdff19f2b23f3f316` |
| nl-es | `06f0e2e00aece0d687edf0540098e4cc8b6e4e4c62b451792a1be6cb11608874` | `7025ce05d97599d1910ab4e27f1e1c583ae86d43ef5d64a169b22bdb77ef0721` | `672bd4c0080c14ab11026a13ccdecf826bd759cc3f348c5751852386efe4684b` |
| nl-fr | `08f57ec27d8698c54be0ef79024048fec737ed4aabbfa8be68c1bb04b26c5fad` | `1b429a3ff61edb99348c4d29a790204565b07a173e966f340268af79b9c585bc` | `f1d1154442c4ea26fcc71dcf605704ab76a3555a2568bff521f158d974b5bc1a` |
| nl-it | `dc91af0aa78da597d0f3025087cd8695ccda1cb9ca454fc5445924e12bbe0059` | `9eff96cf487a6beb5e26413ac9683bf771aac12f0ef9d6c2eca1de5b399fbf93` | `e9880da2da990ad87348c650cc4f82637a108284d7929de2ed901019ef77ac0a` |
| nl-ja | `b886a483f64181624efef8f17c4d1a6d2e421571cf26c2de576f72b5682399b6` | `2b38c2547606d2a33b436cea4337acf4a93ddfbe4acdd93ef5533781d2755b7b` | `b7e5f5dc8b484da52b0a22493149d93f0bbd3a0aeb79deb56b2f28e017a80084` |
| nl-ko | `e7fa69a263fe85ef08205ac654e55e2333f590de5f6bd6f1ea73103150746bff` | `218aebe12b4ba140a0180cfdd3fcb2719547737f1e7c59682aca83a57fed231a` | `e13db87160d1477972824431d9f4e194f90f53a53b7954e659cc74484801f537` |
| nl-pt | `e2fe3b3a95686bd48e01a7975f62ee33bb821dd6a8a743c1a188bb8e6f119d37` | `40c51869695b80e165661c6adb9309c70341342d56d632c472a7ba18f9ace508` | `67516e2163c8c769ab9574b60b472c7d97706b3c4d89182bb95faa221513727a` |
| nl-ru | `d4f081587c7d85e155734d4008d191e8b6f009f50738b3370f966c311053002e` | `7a06f80d9238669ae1c8c1bfc848a2b814d9f0999e3e9f4c79b942dd17747dff` | `dd1c0c087c46f96afc0903c3bf534c7b281d97f3f1c1a6753a4e4813aad64228` |
| nl-zh-tw | `3fd293bfef564ea277f4f96495710f7391ad5204da659bdd43dc2ce3edfde693` | `542c6f1bc8e2f71b0cdf558e169dca3d1738e981919433c63182a304a44754ec` | `bf1f627d1bbf6387cb0f782e6ede2feb3fe18ffb48bd599ce3720be3238b9855` |
