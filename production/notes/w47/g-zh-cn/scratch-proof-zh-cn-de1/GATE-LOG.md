# GATE-LOG — 2026-W47 zh-cn × de (proof1)

校对员 proof1，2026-11-11 16:47–17:20 UTC。解释器：`~/workspace/weekly-git/tools/venv/bin/python`
（Pillow 13.0.0 / FreeType 2.14.3）。TMPDIR = 本 scratch 目录。
全部命令与原始日志均在本目录；文件名按本目录实际文件。

## 0. 探针与 SHA（开工前）

- `echo test | git hash-object -w --stdin`：首次在 ~ 下失败 rc=128（`fatal: not a git repository`，
  非 /dev/null 问题；/dev/null 存在）；在 `~/workspace/weekly-git` 内重探 **rc=0**，
  出 `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`。磁盘：91G/150G 已用，59G 可用（配额已恢复）。
- 三 SHA（开工前与收尾后两次核对一致）：
  - 印 `e6ed50ab8eedb82c249aee9a9ce5e6ed61d0b06bc2060c79c9cdb94957ac424b` / 44,829,975 B ✓
  - 网 `7fb396f13ece42b771beb722811e4ab8df8bb2f9971cf2380e3f06d7e83535e5` / 2,732,464 B ✓
  - 文 `8940ba88e92d70eb6d54e4759657d187b451e259b1633bb92f9d475e97075b0a` / 50,637 B ✓
- 核心对照：印 `c34f5a54e491a085ea3e19a986748938dda79294b90d154a8e746f54a9eb05aa` / 41,763,115 B；
  网 `6b7a12f517749738de2028569556be326aabe00ab556ac3ec8e59cc936a263d9` / 2,632,446 B；
  文 `23fb62bd7763c59392c05ba7e03f64ad8f521352d464d6ac293d2190c4d0bf04` / 49,435 B。

## 1. run.py（scratch 副本）— PASS

- 方法：`*.py + assets` 拷至 `repro/`，OUT 重定向为 `repro/svg`（sed 替换波浪路径），
  `run.py`（`run-proof1.log`）。
- 结果：**rc=0，TOTAL 150**（A2 56 / B1 69 / B2 25；页 10/18/18/18/18/18/12/38；
  类型：完成句子 68 / 单选 50 / 词汇配对 20 / 完形单选 11 / 写作 1）；
  日志 grep overflow/warn/error/traceback **0 命中**。
- 重建 SVG 与盘上 8/8 字节一致（cmp 全 MATCH；SHA 列表 diff 空）：
  p1 `eb00af5d…` p2 `d129d1b4…` p3 `4115835a…` p4 `6c73abc4…` p5 `e34dd96e…`
  p6 `44a7a95e…` p7 `d82b8b66…` p8 `bb46bd5d…`（全长见 `run-proof1.log` 末尾核对段）。
- 附注：前两次重建因重定向失误误写生产 SVG 目录（见 PROOF-NOTE 过程披露）；
  字节验证如上，内容未变。

## 2. freeze — PASS

- `freeze.py baseline --build production/2026-w47/core-zh-cn --core-svg …/core-zh-cn/svg --out freeze-out`
  → **rc=0，baseline 8/8**（`freeze-baseline.log`；repointed 6 文件；core 完整性确认，
  8 文件重哈希未变）。
- `freeze.py diff --core-svg core-zh-cn/svg --edition-svg …-de/svg --strict-cjk --json freeze-diff.json`
  → **rc=0，TOTAL 新增 CJK 0**（`freeze-diff.log`）：
  P1 886→870 / P2 1065→1060 / P3 864→859 / P4 772→767 / P5 969→964 /
  P6 912→907 / P7 753→748 / P8 1125→1120，各页新增 CJK 均为 0。
  净减量解释（`cjk-delta.txt`）：P1 −16 = badge 拉丁化 −11 + 页脚本地化 −5；
  P2–P8 各 −5 = 页脚 “第N版／共8版”→“Seite N von 8”。
- **badge 复核**：P1 badge 文本 `CHINESISCHER TEXT　ERKLÄRUNGEN AUF DEUTSCH`
 （`content12.py:24`）；全版 `德语讲解` 0 次；strict-CJK 缺陷**已修**。
- build-copy 证据说明：baseline 的 `--build` 指 core-zh-cn 构建目录，
  `--core-svg` 指 core-zh-cn 的 svg 目录（标准核心比对，正确路径）；
  版内自比对另做于门 1（repro vs 盘上 8/8）。

## 3. occlusion / p8 — PASS

- `occlusion_audit.py <edition>/svg --json occlusion.json`（真实审计，非 --selftest）
  → **rc=0，0 flags**；`occlusion.json` 本体 `{"flag_count": 0, "flags": []}`；
  自检行：`selftest OK: planted classes fired {BOXTITLE, COVER, EDGE, FOOTER, LINEX, TEXTX}`。
- img-overlap 扫描（text ink vs `<image>` 矩形，gates-zhcn 同款逻辑）：**0 hits**。
- `p8.py extract --p8 svg/p8-ceyan.svg --total 150` → **rc=0，150/150**（`p8-extract.json`）。
- `p8.py compare --core-p8 … --edition-p8 … --total 150` → **rc=0，CLEAN**；
  `p8-compare.json` 本体：`status: "CLEAN"`，missing=[] extra=[] uncertain=[]
  keydiff=[]（gates.json 的 p8 extra "?" 为误读，以此本体为准）。
- keycheck（REG 键 vs 核心 / P8 印出键 vs REG 键，`reg-*.json` + `p8-extract*.json`）：
  REG 键 vs 核心 0 差异；P8 印出键 vs 核心 0 差异（keydiff=[]）；
  P8 印出键 vs REG 键**仅 Q150 不同**（REG `(开放题，范文如下)` vs P8 `✓`，
  与核心一致，设计）；level/type/page 0 差异；注记 150/150 为德语翻译。
- P8 芯片：A2 11 / B1 24 / B2 3 = 核心。

## 4. 印/网文字层 + P8 字号 — PASS（附注）

- PyMuPDF 逐页 token 比较（`fitz`，sort=True）：8/8 页，**posdiff 0，msdiff 0**：
  P1 356/356 / P2 352/352 / P3 263/263 / P4 333/333 / P5 267/267 /
  P6 327/327 / P7 502/502 / P8 1706/1706。
- `pdftotext`：印 44,739 B，网 44,739 B（均非空）。
- P8 答区字号（y ≥ 1328×0.75 的 spans）：**min 9.98pt，median 9.98pt，370 spans**；
  核心对照同为 min 9.98pt（371 spans）；SVG 字号 13.3px（441 处）× 0.75 = 9.975pt，
  名义 10pt。任务 “≥10pt” 按此实测值与核心同值判定通过（非缺陷）。

## 5. 150 题逐题手验 — PASS（`items-150.txt`）

- 方法：AST 提取 150 题干（`extract_stems.py` → `stems-edition.json` /
  `stems-core.json`），与 REG（`reg-edition.json` / `reg-core.json`，
  两版各跑 `dump_reg.py` 得出）逐项对齐；逐行人工读过 Q1–Q150 的题干/键/德语注记。
- 题干 vs 核心：**0 差异**；源 diff：5 文件 393 处替换行，CJK 变化仅 badge 1 处；
  `bslib4.py` 仅页脚 + “Notes｜”→“Hinweise｜”；`svglib.py` 与核心 0 差异。
- 键 vs 核心：0 差异；题干–键配对逐题合理；德语注记正确。
  范文：138 字实测（`len` 去空格前后均为 138），与 `(138 Zeichen)` 一致，
  中文与核心逐字相同。
- D4/D5 限定：P4 `content34.py:130` 全球总决赛限定、`131` GEN 在S16一场没输、
  `:160` “GEN今年 — 淘汰赛一局没输”均与核心逐字相同；Q56 题干含全球总决赛限定，
  键 T1；P1 截稿行与核心一致。

## 6. 水平盒标题真墨（gate67.py）— 1 项缺陷（见 PROOF-NOTE 缺陷 #1）

- 方法：PIL 真墨（edition 自身 svglib 的分 run 字体加载；anchor middle/end 已处理；
  按栏分组，v1 跨栏合并假阳性已修正），35 个奶油盒（fill #f0eee5）。
- 结果：**G6 标题标志 1 处**：P2 “本周生活小日历　Kalender der Woche”，
  真墨右缘 1418.0 vs 盒右缘 1411.5，**越过 6.5px**（`gate67.log` / `gate67.json`）。
  其余最小余量 14.5px（P1 数字盒）、18.5px（P5）、23.5px（P5）。
  页缘墨溢出 0。

## 7. 溢出横扫（gate67.py）— 除 #1 外 0

- 盒内行横向溢出：仅缺陷 #1 一处（G7a 1 处，与 G6 同行）。
- 基线落在盒外的溢出行：**0 候选**（G7b）。

## 8. 引号 / 孤儿 / 禁词 / 繁体 — 1 项缺陷（见 PROOF-NOTE 缺陷 #2）

- 弯引号成对：`《》` 5/5、1/1、23/23、20/20；`「」` P7 29/29；`“”` P3 1/1、
  text.md 2/2；`（）`/`()` 全部成对。U+2019：9 文件均为 0。
- CJK 孤儿标点（`gate8b.py` + 核心对照 `gate8b-core.log`）：本版 31 处，
  核心 26 处；除缺陷 #2 外均为核心同款已接受形态。**缺陷 #2：P1 y=1366.3
  行首孤立 `》`（“》 startet”）**，核心同位置干净（“《试探》 / opens”）。
- 禁词/残留（text-only 扫描，排除 SVG base64 假阳性）：
  SOP/TBD/TODO/FIXME/Lorem/Photo:/Notes/Ukraine/俄乌/战争/proofread/
  “Read & choose”/“Practice example”/“This week”/“Answers on page 8” 全部 0。
- 填空/改写键：150 题内已核（门 5）；Q150 范文在 120–180 字内。
- opencc 全版扫描（venv `opencc`，t2s 比对；SVG 文本 + text.md）：**繁体字 0 例**。

## 9. 重建报告修点复验 — 3 存活 / 1 未彻底

- P4 Hinweise 框：德语前缀 “Hinweise｜” 实测 **6 行**（基线 595.86、625.6、655.3、
  685.0、714.8、744.5；框 `y=557.36 h=234.85` 底 792.21；feature 流止 y=804）✓ 存活。
- P8 keys：`run-proof1.log` “P8 keys flow ends col/y: 3 2521.9”（< 2560）；
  最末键行基线 2523.7；页脚外最大 y=2624 仅页脚 ✓ 存活。
- P2 日历标题：已改 “Kalender der Woche”，但**仍越盒边 6.5px（缺陷 #1）**——未彻底。
- P7 下期预告：`run-proof1.log` “P7 teaser ends 2583.3”（< 页脚线 2596），图止 1889.3 ✓ 存活。
- D5 字体问题（只记录不判）：重建报告 / EDITION-RECORD / WEEKLY-KIT / fanout 全目录
  grep “D5” 无相关记录（仅 SVG base64 噪声）；实测 P5 字体分布与核心一致
  （同 family/size 集合；15.5px 图注 run 2→1、20.5px run 9→8 系德语重排所致）。
- §1.1：纸色 #fbfaf6 ×8，无金色，描边 rect 0，VOL.5=1（P7 下期预告，与核心一致）。

## 目视

- 印 PDF 150dpi 全页渲染 `png/p1.png`–`p8.png`（+ `png/view/` 降采样版）逐页读过；
  除缺陷 #1（`png/p2-cal-title.png` 裁图：盒外暗像素 92，最右 1416.5）、
  缺陷 #2（`png/p1-numbers-box.png` 裁图）外无版式/图文问题。
  P3/P5/P6 与核心同结构，未见新增问题。
