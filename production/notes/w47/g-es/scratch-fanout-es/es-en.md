# 2026-w47-es-en — 工作记录

## ⚠️ QUOTA 事件（记在开头）
- 2026-11-10 渲染步骤：`> es-en-render.log` 重定向打开失败 `Disk quota exceeded`（render.py 未启动）。
- 检查：`df -h` 显示 /home/hatch 150G 总量，已用 105G，可用 46G（70%）——磁盘未满，属瞬时配额抖动，与本次任务早期的 mkdir 瞬时报错同类（那次重试即成，记为 MKDIR-OK）。
- 处理：不硬锤重试；仅改走 exec 直接回显（不写日志文件）重试一次渲染；若再遇配额错即停手上报。

## 应用
- `apply_fanout.py en`：476 次字面替换；1 处 manual 覆盖 harvest（"Después ___ (原形 enviar) el sobre." → "infinitive: enviar"）；leftover zh keys NONE；.py 内 CJK 残留 NONE（svglib.py 注释/docstring 除外）。
- 修复：首轮应用后 content34.py:93 与 content8.py:100 出现子串误替换（短 harvest 键先于长 manual 键改写）；已将两表合并后按最长优先一次替换，重跑后干净。diff 审：仅 PDF 名为结构性改动，其余全是讲解层；无新增 CJK 行。
- 另：gloss 前缀断言改为容忍（harvest 已先替换时跳过）。

## 构建
- build1：run rc=0，TOTAL 150；P8-keys 溢出 2 处（y=2590，超底线 2560 约 30px），其余全过。
  - 原因：英文答案注释比中文多 16 条真换行（核心仅 2 条）。
  - 修复：收紧 12 条注释（content34 ×6：#29/#31/#32/#33/#42/#56；content56 ×3：#68/#82/#88；content8 ×3：#136/#148/#149），均用 wrap() 实测为 1 行；保留与核心一致的换行（#43/#44/#137/#138/#139）。
- build2：run rc=0，零 OVERFLOW / TOO WIDE；P8-keys 终 y=2443（底线 2560，余 117px）；TOTAL 150（A2 50 / B1 72 / B2 28；各页 10/18/18/18/18/18/12/38）。

## 渲染（build3，接替者 2026-11-10）
- 开工探针双通：`git hash-object -w` rc=0；scratch-fanout-es/ 写文件 rc=0。/tmp 旧停工记录已失，以本记录为准。
- render.py rc=0：print `La-Lucerna-VOL4-es-en.pdf` 3,501,211 B；web 849,883 B，文字层 45,459 字节。
- 机械门（build3）：p8 extract 150/150；compare CLEAN（keydiff [137, 138]，翻译题重定向，W46 先例已裁定）；freeze 直接 sha256 8/8；pdftotext print=web 45,358 B 逐字节一致；P8 最小字号 10.125pt；occlusion **5 flags**：P1 LINEX（word gloss 二行墨迹压 y=1844 分隔线）、P7 FOOTER+LINEX+TEXTX（预览横幅底 2669.5 压页脚）、P8 TEXTX（RESPUESTAS 右注与天鹅图注重叠）。另全宽标点扫查发现 P7 来信 （）全宽括号（W46 先例：fan-out 改半角）。
- 修复（build3→build4）：P1 gloss 缩为一行（“two or more people discuss in public.”，18 单位）；P7 word-box 英 gloss 3→2 行、F-MAIL 英注 5→3 行（col3 终点 1931.5→1844.51，与核心一致）；P8 RESPUESTAS 头移至 y=1337、keys 流起 1363；来信括号改半角。
- build4：run rc=0，零 OVERFLOW；P8-keys 终 y=2569（见下）；渲染 rc=0；occlusion **0 flags**；p8 CLEAN；freeze 8/8；pdftotext 一致。目视 P1–P6 + bridge sweep 发现 **P2 C 导语孤行**（2 行 bridge 跨栏断裂，第二行 “correct answer.” 孤悬第 3 栏）+ box-vs-hline 扫查发现 **P5 “¿Y TÚ?” 框越线**（底 1638.55，越过 y=1608 练习分隔线 30px，“them in.” 悬在线下）+ P6 band 英 gloss 残缺（“Reading the campaign”）。
- 修复（build4→build5）：P2 C 导语缩为一行（“Read the article and choose the answer.”）；P5 “Your turn” 英译改为 3 行 19 单位（“Would you vote by post or in person? Black Friday: something useful, or a whim? Write two sentences and send them in.”，保留 useful/whim 与 send 指令；框底 1574.55）；P6 band 补全（“Reading the campaign: debates, programmes and polls”）。
- build5（终版）：run rc=0，零 OVERFLOW / TOO WIDE；TOTAL 150；P5 col3 1574.55，P7 col3 1844.51，P8-keys 终 y=2569（无 OVERFLOW 警告；末键 150 基线 2553.1、墨底 ~2557，距页脚线 2596 约 39px，目视干净，已裁定接受——见 KIT §6.8）；渲染 rc=0：print 3,500,745 B，web 849,020 B；occlusion **0 flags**；p8 CLEAN；bridge sweep 0 孤行；box-vs-hline 全版干净；freeze 直接 sha256 8/8；pdftotext print=web 45,339 B 逐字节一致；P8 最小字号复测 10.125pt。
- §1.1 实测：纸 #fbfaf6 ×8 版；金/砖红/近黑 0；徽章三色齐；刊头 196 单位=147pt；VOL.4 ×9、VOL.5 ×3（皆为下期预告正当引用）；P8 徽章 35 枚与核心一致（A2 11 / B1 21 / B2 3），Q113–150 徽章无缺。
- 注释词逐词计数（核心 §8.1 口径）：各版 Note 词在当版全文 ≥2 次（P5 la papeleta 词元 2 次：Note 1 + 词框 1）。
- .text.md：`2026-w47-es-en.text.md` 1,779 行（核心 extract_text2.py，仅改标题 slug），全文逐行读完（英层逐行核对、西文冻结同核心）；1–150 题号齐全；CJK 0；无 “12 de noviembre”。
- ABSTRACT.txt：英文一行、无 ASCII 双引号（刊名、目标语名、A2–B2、150 题、真实主题）。
- WEEKLY-KIT.md：已写（规格、逐版内容、实测、来源沿用核心、裁定 §6、复现命令、4 轮自校记录）。
- **本轮自查结论：零问题。es-en 完成，待独立复校。**
- PDF 终版：print 3,500,745 B，SHA-256 `e881ebb9c50efe590a97684962f848d8386abd24ca43504945ca9b45f7256b16`；web 849,020 B，SHA-256 `8ab8c66cc9c4e642b7d12c183423fef8c7a167aed338baaf91b6d92683696a77`。
