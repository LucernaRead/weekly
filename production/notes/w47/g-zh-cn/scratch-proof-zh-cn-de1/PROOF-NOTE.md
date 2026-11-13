# PROOF-NOTE — 2026-W47 zh-cn × de (proof1, 独立校对)

- 版：`production/2026-w47/2026-w47-zh-cn-de/`（fan-out #3 重建版，VOL.4）
- 校对员：proof1（与重建者不同人），2026-11-11 16:47–17:20 UTC
- 工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-zh-cn-de1/`
- 解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）

## 结论：(b) 有缺陷，不可定稿 — 2 项缺陷，见下

其余全部机械门禁与 150 题手验均通过。两项缺陷均为德语改写引入的重排问题，
核心（proof3 (a) 定稿）对应位置干净，须修后重建、重跑全门禁、再校对。

## SHA 实测（开工前与收尾后两次核对一致）

| 文件 | 字节 | SHA-256 实测 | 预期 | |
|---|---|---|---|---|
| `Lucerna-VOL4-DE.pdf`（印） | 44,829,975 | `e6ed50ab8eedb82c249aee9a9ce5e6ed61d0b06bc2060c79c9cdb94957ac424b` | 一致 | |
| `Lucerna-VOL4-DE-web.pdf`（网） | 2,732,464 | `7fb396f13ece42b771beb722811e4ab8df8bb2f9971cf2380e3f06d7e83535e5` | 一致 | |
| `2026-w47-zh-cn-de.text.md`（文） | 50,637 | `8940ba88e92d70eb6d54e4759657d187b451e259b1633bb92f9d475e97075b0a` | 一致 | |

核心 core-zh-cn 对照（只读核对）：印 `c34f5a54e491a085ea3e19a986748938dda79294b90d154a8e746f54a9eb05aa` /
41,763,115 B；网 `6b7a12f517749738de2028569556be326aabe00ab556ac3ec8e59cc936a263d9` /
2,632,446 B；文 `23fb62bd7763c59392c05ba7e03f64ad8f521352d464d6ac293d2190c4d0bf04` /
49,435 B。均与任务预期一致。

---

## 缺陷 #1 — P2 日历盒标题真墨越过奶油盒右缘（G6，实测缺陷）

- 位置：P2 “本周生活小日历　Kalender der Woche” 盒标题，`svg/p2-shenghuo.svg`
- 源码行：`content12.py:187` — `f.box("本周生活小日历　Kalender der Woche", [`
- 实测值（PIL 真墨，Noto Sans CJK SC Bold 23pt，与渲染同款字体）：
  盒 `x=989.0, w=422.5` → 右缘 **1411.5**；标题起笔 `x=1007.0`，
  真墨右缘 **1418.0** → **越过可见边 6.5px**。
  其余 34 个奶油盒标题最小余量 14.5px（P1 数字盒），本标题是唯一负值。
- 渲染证据（印 PDF 150dpi 渲染，`scratch-proof-zh-cn-de1/png/p2-cal-title.png`）：
  标题行暗像素最右达 svg x=**1416.5**（盒外 5.0px；盒外暗像素 92 个），
  目视：奶油底在 “Woch**e**” 的 h/e 之间结束，末尾 “e” 落在纸白底上。
  同文件 `png/p2.png`（P2 全页）亦可见。
- 对照：核心同盒标题 “本周生活小日历　This week's dates” 真墨右缘 1389.5，
  盒内余量 22px，干净。德语标题过长是 fan-out 引入。
- 与重建报告的关系：#3 报告称该标题已修（“Diese Woche im Kalender”→
  “Kalender der Woche”）且 “21 px clear of the valley photo”——后者属实
  （墨最右 1418.0，山谷照左缘 1439.5，相距 21.5px），但修点未彻底：
  标题仍越过**自家盒边**。非相对首轮备份的回归（#2 标题更长），
  而是修后残留；按门禁标准“墨越过可见边即缺陷”，仍判缺陷。
- 修复方向（供重建者定）：再缩短德语标题（须省 ≥6.5px 真墨，
  如 “Wochenkalender”）或降字号，修后重测本门。

## 缺陷 #2 — P1 数字盒 “》” 孤儿在行首（G8，CJK 孤儿标点）

- 位置：P1 “数字看本周　Diese Woche in Zahlen” 盒第 3 行，`svg/p1-touiban.svg`
- 源码行：`content12.py:51` —
  `("21. Nov., Samstag — der neue Film 《试探》 startet", "serif", False, INK, 20, 1.35)`
- 实测值（SVG 文本 run）：y=1339.3 行以 `《试探` 结尾（无 》），
  y=1366.3 行以孤立的 `》` 起头，后接 ` startet`：
  - `y=1339.3, x=556.5: '21. Nov., Samstag — der neue Film '`；`x=874.6: '《试探'`
  - `y=1366.3, x=556.5: '》'`；`x=576.5: ' '`；`x=581.4: 'startet'`
- 渲染证据：`scratch-proof-zh-cn-de1/png/p1-numbers-box.png`（P1 全页 `png/p1.png` 亦可见）——
  两行读作 “21. Nov., Samstag — der neue Film 《试探 / 》 startet”，
  闭合书名号独占行首。
- 对照：核心同行断为 “Nov 21, Saturday — the new film 《试探》 / opens”，
  无孤儿。德语 “startet” 比 “opens” 长，换行点移位致 《 试探 》 被劈开，
  是 fan-out 引入。
- 修复方向（供重建者定）：缩短该行德语（如去 “der neue”），使 《试探》 不跨行。

---

## 通过的门禁（实测值见 GATE-LOG.md）

1. **run.py（scratch 副本）**：rc=0，TOTAL 150（A2 56 / B1 69 / B2 25；
   页 10/18/18/18/18/18/12/38），0 溢出；重建 SVG 与盘上 8/8 字节一致。
2. **freeze**：核心 baseline 8/8（rc=0，core 完整性确认）；
   `freeze.py diff --strict-cjk` TOTAL 新增 CJK **0**（rc=0）。
   **P1 badge 缺陷已修**：P1 badge 实测为拉丁-only
   `CHINESISCHER TEXT　ERKLÄRUNGEN AUF DEUTSCH`（`content12.py:24`），
   全版 `德语讲解` 0 次；freeze-diff 各页新增 CJK 均为 0。
   CJK 净减量已逐项解释：P1 −16 = badge 拉丁化（−11）+ 页脚本地化（−5）；
   P2–P8 各 −5 = 页脚 “第N版／共8版”→“Seite N von 8”（fr 版同为
   “Page 2 sur 8”，标准 fan-out 行为）。
3. **occlusion 真实审计**：rc=0，**0 flags**（selftest OK，各类全触发）；
   `occlusion.json` 本体 `flag_count: 0`。img-overlap 扫描 0 hits。
   p8 extract 150/150；**p8 compare CLEAN**（`p8-compare.json` 本体
   `status: "CLEAN"`，missing/extra/uncertain/keydiff 均空）。
4. **印/网文字层**：8/8 页 token 差 0（P1 356/356 … P8 1706/1706，
   posdiff 0，msdiff 0）；pdftotext 印/网各 44,739 B。
   P8 答区最小字号 **9.98pt**（中位 9.98pt，370 spans；SVG 字号 13.3px × 0.75 换算
   = 9.975pt，名义 10pt）——与**核心同值 9.98pt**（371 spans），非缺陷。
5. **150 题逐题手验**（`items-150.txt`，逐行读过 Q1–Q150）：
   - 题干：AST 提取 150 题干，与核心逐项比对 **0 差异**；
     5 个 content 文件共 393 处替换行，仅 badge 1 处 CJK 变化，
     其余只改英文→德语讲解层；`bslib4.py` 仅页脚与 “Notes｜”→“Hinweise｜”；
     `svglib.py` 与核心 0 差异。
   - 键：REG 键与核心 **0 差异**（level/type/page 亦 0 差异）；
     P8 印出键与核心 **0 差异**（keydiff=[]）。
   - **keycheck**：P8 印出键 vs REG 键仅 **Q150 不同**（REG `(开放题，范文如下)`，
     P8 印 `✓`）——与核心一致，是设计（P8 表头 “✓ = die Schreibaufgabe”），非缺陷。
   - 题干–键配对逐题核过，全部合理；德语注记 150/150 均为正确翻译。
     范文实测 138 字（与 `(138 Zeichen)` 一致），范文中文与核心逐字相同。
   - **D4/D5 三处限定同步落地**：P4 正文 `content34.py:130`
     “第一次在全球总决赛的BO5里打赢T1”（全球总决赛限定）与 Q56 题干一致；
     `:131` “GEN在S16一场没输”；`事实`栏 `:160` “GEN今年 — 淘汰赛一局没输”
     与核心逐字相同；P1 版头/截稿行（决赛未赛、冠军下期报）与核心一致，
     德语译文无矛盾（“bei Redaktionsschluss noch nicht gespielt”）。
6. **水平盒标题真墨**（gate67.py，PIL 真墨 + anchor 处理 + 分栏分组）：
   35 盒，标题仅缺陷 #1 一处；其余最小余量 14.5px（P1）。页缘墨溢出 0。
7. **溢出横扫**（同脚本）：盒内行横向溢出仅缺陷 #1 一处；
   基线落在盒外的溢出行 **0** 候选。
8. **引号/孤儿/禁词/繁体**：
   - 弯引号成对：`《》` 5/5、1/1、23/23、20/20；`「」` P7 29/29；
     `“”` 1/1（P3）、2/2（text.md）；`（）`/`()` 全部成对。U+2019 全版 0。
   - CJK 孤儿标点（gate8b.py）：本版 31 处，核心 26 处；除缺陷 #2 外，
     全部是核心同款的已接受换行形态（gloss 行首/行尾 “—”“·”、
     选项行尾 “·”、分隔行 “— Seite N —”；另 P1 y=682 “，” 为分组器伪影，
     真实视行以 “BLG” 起头）。已逐项与核心同位置比对。
   - 禁词/残留：text-only 扫描 `SOP/TBD/TODO/FIXME/Lorem/Photo:/Notes/Ukraine/
     俄乌/战争/proofread/Read & choose/Practice example/This week/Answers on page 8`
     全部 0（SVG base64 内的假阳性已排除）。
   - 填空/改写键：150 题内已核（见上）；Q150 范文 120–180 字要求内（138 字）。
   - opencc 全版扫描（SVG 文本 + text.md）：**繁体字 0 例**。
9. **重建报告修点复验**：
   - P4 Hinweise 框：德语前缀 “Hinweise｜” 实测 **6 行**（基线 595.86–744.5，
     框底 792.21，余量足；feature 流止于 y=804）——修点存活 ✓。
   - P8 keys：末端 y=2521.9（< 2560），最末键行基线 2523.7 —— 存活 ✓。
   - P2 日历标题：已改 “Kalender der Woche” 但**仍越盒边**（缺陷 #1）——修点未彻底。
   - P7 下期预告：条底 **2583.3**（< 页脚线 2596），图止 1889.3 —— 存活 ✓。
   - D5 字体问题（只记录不判）：重建报告、EDITION-RECORD、WEEKLY-KIT 与
     fanout scratch 中均未找到 “D5” 相关记录（全目录 grep 仅命中 SVG 内 base64 噪声）；
     实测 P5 字体分布与核心一致（同 family/size 集合，仅 15.5px 图注 run 2→1
     与 20.5px run 9→8，系德语重排 run 数变化，无字体改动）。如协调员所指 “D5”
     另有所指，请指出具体位置。
   - §1.1：纸色 #fbfaf6 ×8，无金色，描边 rect 0，VOL.5 出现 1 次为 P7 下期预告
     （与核心一致）；P8 芯片 A2 11 / B1 24 / B2 3 = 核心。
   - 目视：P1–P8 印 PDF 全页逐页读过（`png/p1.png`–`p8.png`，150dpi 渲染），
     除上述 2 缺陷外无版式/图文问题。

## 过程披露（须协调员知晓）

- 校对前两轮 `run.py` 重建因重定向失误（源文件用 `~/…` 波浪路径，
  替换式只认 `/home/hatch/…` 绝对路径）误写进**生产版 SVG 目录**
  （2026-11-11 16:48–16:50 UTC 两次，8 个 SVG mtime 更新）。
  事后验证：正确重定向的 scratch 重建与盘上 SVG **8/8 字节一致**；
  P2–P8 哈希与重建者 #3 前备份记录逐字节相同，P1 仅差 badge 修复的预期变化；
  印/网/text.md 三 SHA 在事发前与收尾后两次核对均与预期一致，
  内容文件（*.py）mtime 未变。**生产内容字节未变，仅 SVG mtime 变了**，
  但仍请协调员复核三 SHA（已在本报告给出实测值）。
- 网 PDF 未重渲（铁律：SHA 不可复现，只比文字层）；全部重建/复验均在
  scratch 目录内完成，未覆盖任何交付件；core-zh-cn 只读，未写。

## 修复建议（供重建者，修后须重建 + 全门禁 + 再校对）

1. `content12.py:187` 日历标题再缩短（省 ≥6.5px 真墨）或降字号，
   重测 gate67 至余量 >0。
2. `content12.py:51` 数字盒第 3 行缩短德语，使 《试探》 不跨行，
   重测 gate8b 至 “》” 行首 0 处。
