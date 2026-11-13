# W47 zh-tw 家族 P7 金句修复日志（SOP §8 循环修复）

- 修复工人：W47 zh-tw 家庭修复工人。开工 2026-11-12 ~12:59 EST。
- 问题来源：独立重校 PROOF-NOTE（`hidden_files/w47/scratch-reproof-w47-zh-tw/PROOF-NOTE.md`）第 1 条，低严重度，10 版共有，已由协调员独立核实属实。
- 问题：P7「本週金句」第 8 条引文作「迪士尼聖誕，從11月17日開始」，删去了 P5 原句句首「香港」二字（原句「香港迪士尼聖誕，從11月17日開始，一直放到明年1月3日……」，core text.md:2593 行；P7 引文 core text.md:4827 行附近），与栏眉 "word for word from this issue's articles" 声明不符。其余 7 条已核对为逐字引用。
- 修复：10 版 P7 第 8 条引文恢复为「香港迪士尼聖誕，從11月17日開始」（只补「香港」二字，不动其余文字与各版英文/读者语翻译）。
- 范围：`production/2026-w47/` 下 core-zh-tw（= zh-tw-en）+ 9 fan-out（zh-tw-de/es/fr/it/ja/ko/nl/pt/ru），共 10 版。不碰其他家庭、其他周。不 commit、不 push、不 lint。
- 源头：各版 P7 中文引文不共用——每版自有 `content7.py:128`（引文行）与 `checks.py:19`（8 条逐字引文自检清单，同为该引文串）；10 版 × 2 文件各改 1 处，共 20 处。P5 原句（`content56.py:18`）本身已含「香港」，不动。各版读者语译文行不动。
- 渲染：`~/workspace/weekly-git/tools/venv/bin/python`，每版 `run.py` → `render.py` → `tools/webpdf.py` → text.md；门禁脚本 `fix_build_gates.sh`（本目录）。
- text.md 说明：交付的 text.md 并非 `export_zhtw_textmd.py` 的原始输出（ builder 曾把卷头多行 `<text>` 节点合并为单行；原始导出与交付文件差约 249 B 排版量）。因此 text.md 取 D5 stage0 备份（SHA 与 PROOF-NOTE 修前实测逐版一致）恢复后只改引文所在 1 行；并以修前/修后两份原始导出互差仅该 1 行为交叉验证。
- 接替记录（2026-11-12 ~15:50Z，第三任工人 e718edf9）：开工核对——6 版已做版盘上 SHA 与本表一致；ko 版实为上一任 run_rest3.sh 已跑完 ALL-GREEN（15:30:38Z，`run_all.log` 有据），交接状误写为待做，ko 行/KIT/干跑已由本任补全。nl 版曾出现双实例并发（上一任 run_rest3.sh 的 15:39 孤儿进程未随重启死亡 + 本任 run_rest4.sh 15:42 新实例同跑同版），本任已杀双实例及 run_rest4.sh 驱动，改由 `run_clean_nl_pt_ru.sh` 单实例顺序重跑 nl/pt/ru（幂等，15:47:55Z 起）。ja SIMP_ONLY 误报已在本日志书面定性（见「逐版门禁复核」）。
- 完成记录（2026-11-12 16:17Z）：10/10 版全部重渲染+门禁+KIT+干跑完成。门禁 9 版 ALL-GREEN，ja 仅 SIMP_ONLY 误报一项（已定性，见上）。磁盘终态 94G 未触门限。未 commit、未 push、未跑 lint、未碰其他家庭/其他周。

## 改前/改后尺寸 + SHA（前 12）

修前值 = PROOF-NOTE 实测（本任务开工重测一致）；修后值 = 本次重渲染盘上实测。
印 PDF 为确定性构建（两跑 SHA 相同）；网 PDF 每次重跑 SHA 都不同（fontTools 子集化随机标签，±数 B），以本次交付文件为准。

| 版 | 印 PDF 改前（字节 / SHA12） | 印 PDF 改后（字节 / SHA12） | 网 PDF 改前（字节 / SHA12） | 网 PDF 改后（字节 / SHA12） | text.md 改前（字节 / SHA12） | text.md 改后（字节 / SHA12） |
|---|---|---|---|---|---|---|
| core-zh-tw | 11194932 / 332ed38d5cd2 | 11195126 / 27afa3281b1d | 1897929 / 8fa6efdf1bdc | 1898131 / 45d076003801 | 49798 / 09e083e10da2 | 49804 / 9b8b5295ddd8 |
| zh-tw-de | 11195908 / 1b1f0f0370c1 | 11196101 / 2a22bcdaa8ca | 1903427 / f430e390f495 | 1903630 / a67ffad91835 | 51814 / 85584db99a9e | 51820 / 8187f6196326 |
| zh-tw-es | 11193961 / e9d3ac05473f | 11194154 / 25216239cbf9 | 1902094 / 2ec0065257c1 | 1902298 / f8c0086a1a66 | 52246 / 59439c7db9e1 | 52252 / e8a36b7996f6 |
| zh-tw-fr | 11191465 / 384fd32e70c8 | 11191659 / 47320e77d6f1 | 1899091 / 64439f145cce | 1899287 / 233658513953 | 52470 / 673943a0de31 | 52476 / a2df8892d632 |
| zh-tw-it | 11187632 / b4a3fdfc5868 | 11187826 / 0cdf05fef852 | 1895530 / 39898950b0d0 | 1895728 / 3ed32974c27d | 51685 / 48e04f1540a9 | 51691 / 788ed6f6600c |
| zh-tw-ja | 16365732 / 1f61f431d75e | 16365954 / dbbe03ab27b3 | 2447140 / 94b53a518bb0 | 2447388 / 660f93940fe8 | 53753 / e03a56ad7254 | 53759 / 6e5b4b81e131 |
| zh-tw-ko | 12718866 / 0fe4589f6fe8 | 12719179 / e49ab5fee582 | 2134058 / e298e577bf0b | 2134244 / 7419fee9eedf | 53916 / a44ba8cbb74f | 53922 / 0215bc2cf6a6 |
| zh-tw-nl | 11189525 / 1e24a8deb37b | 11189718 / 20ad418b233c | 1898551 / 9461e8bad39b | 1898763 / d28897aea142 | 50596 / a3662561fff3 | 50602 / 487127dd7d72 |
| zh-tw-pt | 11197823 / b036790928ce | 11198017 / 7c59676c6ef0 | 1906989 / ad03afe2ccb9 | 1907201 / 90caf45fab41 | 51492 / 02387ce2dd5e | 51498 / 542bfae121e5 |
| zh-tw-ru | 11366251 / d80b9ee5df60 | 11366471 / eb3fd9aae5e2 | 2070745 / d255e31ad059 | 2070994 / 16a6d20a755e | 62492 / 2fb4b97ef37d | 62498 / ea9c1514df96 |

注：text.md 改后字节 = 改前 + 6（「香港」二字 UTF-8 各 3 字节），每版只改引文行 1 行（`diff` 修前备份 vs 修后 = 4 行：`N c N` + `<` 旧行 + `---` + `>` 新行）。

## 逐版门禁复核（详见 `logs/<slug>/GATES-SUMMARY.txt`）

7 版已验（core/de/es/fr/it/ja/ko）：除 ja 外 OVERALL 皆 ALL-GREEN；ja 仅 checks.py 一项 SIMP_ONLY 误报（见下「ja SIMP_ONLY 误报说明」），其余全绿。共同 profile：run.py RC=0 TOTAL=150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；head_check 0 缺陷；仅 p7-lang.svg 变化；quote-check 固定引文 2 处（P5+P7）、裸引文 0；occlusion 0 flags（自检 6 类全触发）；p8 extract 150/150、compare CLEAN keydiff=[]；freeze baseline 8/8；freeze diff vs 修前新增 CJK 恰 {香:1, 港:1}；spill 0、boxtitle 0 DEFECT、edge 0 TOUCH/0 NEAR、creambox PASS、D5 普查 PASS、引号普查 0 缺陷字；textcheck-adapted PASS（印/网文字层多重集差 0，修前→修后印层仅 +香/港）；text.md diff 恰 4 行、新鲜导出修前/修后 diff 恰 4 行。

| 版 | P8 行数（修前→修后）/ 距页脚余量 | checks | OVERALL | 门禁日志 |
|---|---|---|---|---|
| core-zh-tw | 123→123 / 37.3px | PASS | ALL-GREEN | `logs/core-zh-tw/GATES-SUMMARY.txt` |
| zh-tw-de | 160→160 / 36.7px | PASS | ALL-GREEN | `logs/2026-w47-zh-tw-de/GATES-SUMMARY.txt` |
| zh-tw-es | 144→144 / 36.3px | PASS | ALL-GREEN | `logs/2026-w47-zh-tw-es/GATES-SUMMARY.txt` |
| zh-tw-fr | 152→152 / 35.3px | PASS | ALL-GREEN | `logs/2026-w47-zh-tw-fr/GATES-SUMMARY.txt` |
| zh-tw-it | 150→150 / 50.3px | PASS | ALL-GREEN | `logs/2026-w47-zh-tw-it/GATES-SUMMARY.txt` |
| zh-tw-ja | 126→126 / 50.3px | FAIL（仅 SIMP_ONLY 误报） | HAS-FAILURES（仅此一项） | `logs/2026-w47-zh-tw-ja/GATES-SUMMARY.txt` |
| zh-tw-ko | 119→119 / 50.8px | PASS | ALL-GREEN | `logs/2026-w47-zh-tw-ko/GATES-SUMMARY.txt` |
| zh-tw-nl | 158→158 / 36.3px | PASS | ALL-GREEN | `logs/2026-w47-zh-tw-nl/GATES-SUMMARY.txt` |
| zh-tw-pt | 126→126 / 35.3px | PASS | ALL-GREEN | `logs/2026-w47-zh-tw-pt/GATES-SUMMARY.txt` |
| zh-tw-ru | 172→172 / 35.7px | PASS | ALL-GREEN | `logs/2026-w47-zh-tw-ru/GATES-SUMMARY.txt` |

### ja SIMP_ONLY 误报说明（`checks.py` 第 28 行）

- 现象：ja 版 `checks.py` 报 `SIMP_ONLY_HITS ['国', '学']`，`CHECKS FAIL`（RC=1）。其余 8 条引文皆 2× PASS、两图核对皆 PASS。
- 定性：误报，与本次修复无关。`simp_only` 字符集是按繁體中文目标语文本设计的简体字扫描；ja 版的读者语层是日文，`国`/`学`是正常日文汉字——命中源为 P3 日文讲解句「高雄国際鋼雕芸術祭」（`content34.py:24`，`国際`）及日文词中的 `学`，均不在本次改动文件内。
- 证据：修前 SVG 快照（`prefix-svg/2026-w47-zh-tw-ja-svg/`）同样报 `SIMP_ONLY_HITS ['国', '学']`，修前修后同一组；本次修复只改 P7 引文（`香港`二字），未动 P3。KIT（ja）已记此误报。
- 结论：ja 版除此一项外全绿，交付有效；不改 `checks.py`（跨版工具逻辑，不属本次修复范围）。

## KIT 更新记录

- core-zh-tw、zh-tw-de/es/fr/it/ja：`update_kit_3.py` 已更新（PDFs 行 + Text layer 行（fan-out）+ Text export 行 + Build history 修复条目；每版 PDFs 行注 D5 交付值与 P7 修复增量）。
- zh-tw-ko：`update_kit_4.py` 已更新（同上；pdftotext 修前 D5 实测 50,139 / 50,140——网版修前值 50,140 由修后 50,146 − 6 推得，印/网多重集差为 0 且修后印/网差 1 B 与他版同一 artifact 一致；P8 119 行、余量 50.8px）。
- zh-tw-nl：`update_kit_5.py` 已更新（PDFs 行 + Text layer 行 + Text export 行 + Build history 修复条目；pdftotext 修前 D5 实测 46,937 / 46,938，修后 46,943 / 46,944；P8 158 行、余量 36.3px）。异常记录：KIT 文件 mtime 为 16:02:41Z，本任 16:02:50Z 的 `update_kit_5.py` 调用因“已更新”断言失败——即文件在本任调用前 10 秒已被一次未识别的 `update_kit_5.py` 成功运行写入；内容已逐项核对与盘上实测修后值一致（印 11,189,718 B / 20ad418b233c…、网 1,898,763 B / d28897aea142…、text.md 50,602 B / 487127dd7d72…），无误。断言守卫正常工作，未重复写入。
- zh-tw-pt：KIT 已更新（PDFs 行 + Text layer 行 + Text export 行 + Build history 修复条目；pdftotext 修前 D5 实测 47,876 / 47,877，修后 47,882 / 47,883；P8 126 行、余量 35.3px）。同 nl：KIT 文件 mtime 16:12:26Z，本任未运行 pt 的 KIT 脚本——系协调侧在门禁变绿后即时补写（与 nl 16:02:41Z 同一模式）；内容已逐项核对与盘上实测修后值一致，无误。`update_kit_5.py` 的 DATA 已补 pt 一条备查（再跑会因“已更新”断言拒绝，属守卫正常工作）。
- zh-tw-ru：`update_kit_5.py` 已更新（PDFs 行 + Text layer 行 + Text export 行 + Build history 修复条目；pdftotext 修前 D5 实测 58,548 / 58,549，修后 58,554 / 58,555；P8 172 行、余量 35.7px）。

## text.md 干跑核对（ru 家导出器陷阱，2026-11-12 补充指令）

- 背景：ru 家发现重导出 text.md 会丢标题行——其导出器 `ru_textmd.py do_p_text` 只收 sans 粗体 ≥24pt 标题，D5 后缩到 22/23pt 的框题会被丢掉；ru 家逐版干跑到 /tmp、diff 修前文件、原位置逐字回补。
- zh-tw 核查结论：**本陷阱不适用于 zh-tw**。zh-tw 导出器 `export_zhtw_textmd.py` 无任何字号/字体阈值——逐个输出每个非空 `<text>` 节点（仅跳过独立 `Lucerna` 刊头字标节点）。且本修复从不落盘新鲜导出：交付 text.md = D5 stage0 备份（与修前交付文件逐字节一致）+ 仅引文行 1 行改动，脚本断言修前/修后 diff 恰为 4 行。
- 干跑验证（每版：新鲜导出修后 SVG → `logs/<slug>/textmd-fresh-post.md`，与修前交付文件比非空白字符多重集；脚本 `dryrun_check2.py`，本目录）：
  - core/de/es/fr/it（5 版已验）：fresh-only 恰为 {香:1, 港:1}；pre-only 仅为 `Lucerna` × 8（导出器按设计跳过的 8 处页脚独立刊头字标；交付文件页脚行内含 Lucerna，不受影响）——**无任何标题行被丢**。新鲜导出与交付文件的行式差异全系 D5 后 `<text>` 节点拆分（同一行视觉文字拆成多节点）+ 卷头合并排版所致，字符内容无差。
  - 10 版全部已验（见下表）；nl/pt/ru 由本任补验，结论与前 7 版一致。

| 版 | 干跑 fresh-only | 干跑 pre-only | 结论 |
|---|---|---|---|
| core-zh-tw | {香:1, 港:1} | `Lucerna` × 8 | 无丢行 |
| zh-tw-de | {香:1, 港:1} | `Lucerna` × 8 | 无丢行 |
| zh-tw-es | {香:1, 港:1} | `Lucerna` × 8 | 无丢行 |
| zh-tw-fr | {香:1, 港:1} | `Lucerna` × 8 | 无丢行 |
| zh-tw-it | {香:1, 港:1} | `Lucerna` × 8 | 无丢行 |
| zh-tw-ja | {香:1, 港:1} | `Lucerna` × 8 | 无丢行（另：checks.py SIMP_ONLY 误报，见下） |
| zh-tw-ko | {香:1, 港:1} | `Lucerna` × 8 | 无丢行 |
| zh-tw-nl | {香:1, 港:1} | `Lucerna` × 8 | 无丢行 |
| zh-tw-pt | {香:1, 港:1} | `Lucerna` × 8 | 无丢行 |
| zh-tw-ru | {香:1, 港:1} | `Lucerna` × 8 | 无丢行 |

## 顺手项

- `svglib.py` 注释 "exactly 2 glyphs in this edition" 已过期：该注释位于 `svglib.py:121`，不在本次改动的任何文件内（本次只改 `content7.py` / `checks.py`），按任务指令不管，不另开文件。

## 收尾（2026-11-12，10 版全部完成）

- 交接：首任（77323d3e）做完 core 并启动 `run_all.sh`，运行时重启中断于 es 门禁中；第二任接手核实 core/de 已绿、es 源头已改但未渲染完，重起 `run_rest.sh`（es）、`run_rest2.sh`（it–ru），完成 es/fr/it/ja/ko；运行时第二次重启杀死 `run_rest2.sh` 于 ko 门禁后，第二任重起 `run_rest3.sh`（ko–ru），完成 ko；其间父线第三次派发又一工人（run_rest4.sh），两循环一度在 nl 上竞跑——第二任主动停掉己方循环（run_rest3.sh + 其 nl 门禁）并让第三任独跑，第三任清理重复后重跑 nl（15:47:55Z）并完成 nl/pt/ru。最终 10 版门禁、KIT、FIX-LOG 三表全部闭合，FIX-LOG 全文 0 个 TBD；收尾盘上复核：10 版印/网/text.md 尺寸+SHA 前 12 与本表逐项一致（ALL-MATCH）。
- 磁盘：收尾 94G 已用（门限 100G，全程未触发）。
- 未 commit、未 push、未跑 lint；`svglib.py` 未动。
