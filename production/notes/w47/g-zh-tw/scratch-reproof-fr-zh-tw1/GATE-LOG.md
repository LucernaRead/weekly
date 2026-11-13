# GATE-LOG — 2026-W47 fr-zh-tw re-proof（fix1 重建版独立复校，全部门禁实跑记录）

复校员 re-proof（与 fix1 修复员、与 proof1/proof2 均不同人），2026-11-11。
解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）；
TMPDIR 全程指向本 scratch 下 `tmp/`（系统 /tmp 未用）。正典 creambox：
`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py`。
所用运行命令与输出均列于下；KIT 自述数值一律不采信，只认以下本人实跑结果。
Scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-fr-zh-tw1/`
结论见同目录 `PROOF-NOTE.md`；本文件只记门禁实跑。生产目录零写入；core-fr 只读。
另：开工前读过 `~/workspace/weekly-git/AGENTS.md`（内容仓指南；本次只复校、不入库、无冲突）。

## §0 身份与探针

- 探针：`/dev/null` 存在；`echo test | git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，rc=0（与 proof2/fix1 同值）。
- SHA/字节核对（`sha256sum` + `stat`，开工与收工各一次，一致；与任务书预期逐一相同）：
  印 PDF 30,551,088 B `baf81d03…908b8e18` ✓；网 PDF 2,552,857 B `2766f3ed…48d212` ✓；
  text.md 45,992 B `e5c8c1cd…cf3a2` ✓。
- 核心 core-fr 三件复核前后一致，未变（fix4 定稿）：印 `a30af667…5a9d`（30,446,975 B）、
  网 `56f50ca8…e141`（2,241,835 B）、文 `52024e02…63df`（46,471 B）。
- git 状态：`?? production/2026-w47/2026-w47-fr-zh-tw/` 与 `?? production/2026-w47/core-fr/`，
  均为未入仓新目录，无修改记录；本次未 commit、未 push。

## §1 run.py + 确定性重建（scratch 副本）

命令：版目录完整拷贝至 scratch `build-copy`，删 svg 后在其中运行 run.py（`build-reproof.log`）。
- run.py：rc=0，`P8 saved, TOTAL exercises: 150`，`TOTAL 150`，`ALL DONE`，`FLOW OVERFLOW` /
  `HEAD TOO WIDE` / `NOSPACE` 出现 0 次。by level `{'A2': 53, 'B1': 75, 'B2': 22}`；
  by page `{1: 10, 2: 15, 3: 18, 4: 18, 5: 17, 6: 18, 7: 12, 8: 42}`；by type：
  完成句子 49 / 单选 26 / 句型转换 7 / 词汇配对 21 / 阅读判断 5 / 图表读数 6 / 跟练 8 /
  改错 4 / 完形填空 8 / 阅读理解 5 / 翻译 5 / 对话补全 5 / 写作 1。
- 重建 SVG 与现盘 SVG：`cmp` **8/8 IDENTICAL**（p1–p8 全同）：
  `bc9050c8 / b46154cf / 22af3699 / b4d0e944 / a1981b77 / 81a3f8ff / 087855db / 7b8c6116`
  （P4 `b4d0e944` 为 fix1 新哈希，其余 7 页与修前逐字节相同，见 §11）。

## §2 独立门禁 14/14 PASS（`gates-reproof.json`，日志 `gates-reproof.log`）

`proof_gates.py`（proof2 `proof_gates.py` 的同款复刻，仅改写输出路径与本次 build 日志；
gate 1 读本次 scratch 重建日志，不读 builder 日志；gate 13 用 fix1 scratch 的 `check_mcq.py` 副本）。

| 门 | 结果 |
|---|---|
| run | PASS：exit 0，零溢出；TOTAL 150（见 §1） |
| occlusion（`tools/occlusion_audit.py`，不用 --selftest） | PASS：0 flags，selftest OK（`occlusion-reproof.json`，`flag_count: 0`） |
| p8_extract（`tools/p8.py extract --total 150`） | PASS：keys 150/150，printed notes 121/150（`p8-reproof.json`） |
| p8_compare（vs core P8 SVG，直接读 `p8compare-reproof.json` 本体） | PASS：**CLEAN**，total 150，core_count 121 = edition_count 121，missing []，extra []，uncertain []，**keydiff [150]** |
| source_freeze | PASS：content*.py / bslib4.py / svglib.py / run.py 与核心字节相同；render.py 仅 BASE+PDF 名差异 |
| string_freeze | PASS：全部非 CJK 核心串按页存活；0 核心 E 残留；0 未入账 CJK；1 串因翻译 E 值豁免（核心 `stem_e1` 前缀 `Traduisez : `） |
| text_layer | PASS：印/网 pdftotext 逐字节一致（101,440 B）；web 2,552,857 B < 7MB；print 30,551,088 B（`print-reproof.txt` / `web-reproof.txt`） |
| p8_font | PASS：P8 最小字号 **11.625pt** ≥ 9.75pt（亦 ≥ 本任务 10pt 下限） |
| scans | PASS：U+2019=0，U+00B7=0，gold=0，旧纸色=0，#fbfaf6 ×8 |
| chips | PASS：134 total [10, 12, 18, 15, 14, 15, 12, 38] |
| keycheck（vs `core-fr/final-fr-p8.json`） | PASS：150 键仅 Q150 不同（`開放題` vs 核心 `开放题`），核心 150 键 / 抽取 150 键 |
| mcq（`check_mcq.py`） | PASS：bodies 45，rendered lines **1441**，DEFECTS: 0，UNLOCATED: 0（`mcq-reproof.log`；1441 vs proof2 的 1442，相差 1 行即 D3 注释由 2 行变 1 行，吻合） |
| widths | PASS：31 单行串全部在预算内；4 组共行对均 ≤1757 |
| band_spans（印刷 PDF span 实测，1920 单位口径） | PASS：FR title ends 1236.9，band_r1 starts 1405.0，FR sub ends 837.2，band_r2 starts 1571.4 |

注：text_layer 101,440 B vs proof2 的 101,463 B（−23 B）为 P4 注释删 2 字后的行重排所致；
印/网逐字节一致，逐页比对见 §5。

## §3 freeze 标准核心比对 8/8 + freeze diff

- 标准核心比对（`tools/freeze.py baseline --build production/2026-w47/core-fr --core-svg production/2026-w47/core-fr/svg --out <本目录>/freeze-core`，`freeze-core.log`）：
  **baseline: 8/8 SVGs byte-identical**（p1 `6aad8b4b…`、p2 `5709e000…`、p3 `7828cfe3…`、p4 `7e46e630…`、
  p5 `fff2a8d3…`、p6 `7af7cf3c…`、p7 `75237d67…`、p8 `5bee4d44…`，与 fix1 记录逐一相同）；
  `core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)`，rc=0。
  `--build` 指 core-fr 的 build 目录、`--core-svg` 指 core-fr 的 svg 目录，路径正确，
  非版内自比对（版内自比对另见 §1 确定性重建 8/8）。
- freeze diff（core vs edition，`freeze-diff.log` / `freeze-diff.json`，rc=0）：新增 CJK 合计 **971 字符**
  （proof2 为 973；差 −2 恰为 D3 删去的「決賽」二字；p4 89→87，其余各页与 proof2 相同：
  p1 79、p2 93、p3 54、p5 76、p6 79（含 U+3000 ×1）、p7 139、p8 364（含 U+3000 ×10））。

## §4 occlusion 真实审计 — 0 标记

命令：`tools/venv/bin/python tools/occlusion_audit.py --json <scratch>/occlusion-reproof.json svg/`（cwd=版目录，未传 `--selftest`）。
输出：`0 flags`，rc=0；`occlusion-reproof.json`：`flag_count: 0`，`flags: []`。
（工具另打印一行自检阳性对照通过——为工具内置输出，非 `--selftest` 调用。）

## §5 印/网文字层逐页一致 + P8 字号

- `pdftotext -layout -f N -l N` 逐页比对（`textlayer/`，`cmp`）：P1–P8 **全部 IDENTICAL**
  （12,492 / 10,406 / 10,620 / 12,790 / 11,703 / 12,383 / 11,780 / 19,266 B，与 fix1 记录逐一相同）。
  P4 印/网均含新注 `大師賽結果與杜林名單見本版正文。` 各 1 次、旧句 0 次。
- 全文 `pdftotext -layout` 印 vs 网逐字节一致（101,440 B，见 §2 text_layer）。
- P8 最小字号：fitz 实测 **11.625pt**（§2 p8_font 门；亦见 §7 verify_ed_fr 同值），≥ 10pt。
- 网 PDF 未重渲覆盖交付件：交付网 PDF 收工 SHA 仍为 `2766f3ed…`（§0）；铁律——网 PDF SHA/字节不可复现，
  本次只比文字层，未以重渲件比对 SHA。

## §6 D3 独立重测（自写 `d3_verify_reproof.py`，`d3-verify-reproof.log`，rc=0，D3 VERDICT: PASS）

- 源码：`expl.py:122` 现为 `"chiffres_note": "大師賽結果與杜林名單見本版正文。"`。
- 宽度（`svglib.text_w`，serif 21.5，与 `content34.py:168` 的 `p.para(..., 21.5, "serif", ..., CW - 44)` 口径一致；
  栏宽 = 422.5 − 44 = 378.5 px）：新句 **344.0 px**（余量 +34.5），旧句 387.0 px（超 +8.5）——
  与任务书预期 344.0 px 一致，单行容纳。
- P4 SVG：新注为**单一** `<text x="1461.5" y="520.0" font-size="21.5">大師賽結果與杜林名單見本版正文。</text>`
  （句号附于句末）；基线 y=550.53（±1.0）上元素 **0 个**；P4 独立 `。` 元素 **0 个**。
- 全版孤儿标点扫（全部 8 页 SVG，纯标点 `<text>`）：仅 2 处，均为核心继承行首 `—`（P4 y=623.13、P6 y=653.69，x=1007.0），见 §8。
- 其余「決賽」未动：`diff expl.py.pre-fix expl.py` 恰 2 行（仅 122 行一增一删）；
  `expl.py` 内「決賽」出现 16 → 15（仅删 122 行一处）；`date_22:119`、`g2:39`、`mots_tennis:138`、
  `teaser_note`、`writing_instr` 等其余 15 处（行）全部未动；`content34.py` 等其他文件未动。
- `.text.md`：新句 1 次、旧句 0 次。
- 渲染证据：300 dpi 裁切 `png/p4-note-crop.png`（SVG 坐标 x 1420–1880、y 490–600）——
  单行完整，句号行内；全页 150 dpi `png/p4.png` 同一位置亦无孤儿句号。

## §7 verify_ed_fr + check_s11（fr 适配版，本人实跑）

- `verify_ed_fr.py`（`verify_ed_fr-reproof.log`，rc=0）：**ALL verify_ed_fr CHECKS PASS**——
  text.md 答案解析 150/150；P8 抽取键 150/150；vs 核心仅 Q150 不同；text.md vs P8 抽取 0 mismatch（Q150 除外）；
  Q150 写作键 `開放題`；Q148 三重核对全过（content8.py 键+题干、P8 SVG 基线拼接题干无 `du`、抽取键）；
  P8 最小字号（PDF 口径）11.625pt ≥ 9.75pt。
- `check_s11.py zh-tw`（`check_s11-reproof.log`，rc=0）：**ALL §1.1/P8 CHECKS PASS**——
  色集 core 19 = edition 19，extra none、missing none；徽章色 A2/B1/B2 均在；
  P8 SVG 最小字号 15.5；Q113–120 选项行在；Q120 chip OK #37402f（B2，与核心一致）；
  ÉCRITURE 头在；Q113–116 完形空、117–119 单选号、145–149 完形空均在。

## §8 孤儿标点全扫 + Q148 + 填空线（`check_extra.py zh-tw reproof`，`check_extra-reproof.log` / `extra-reproof.json`，EXTRA PASS）

- 孤儿元素：total=2，**new=0**，inherited=2（P4 y=623.13 `—`、P6 y=653.69 `—`，核心继承行首破折号），
  **remnant=0**（P4 `。` 残留已随本次修复消失），shared_baseline=0。
- 填空线：core 与 zh-tw 完全相同 3 条——P3 (538.5, 1864.7)、P3 (538.5, 1997.4)、P8 (989.0, 843.0)，ok=True。
  Q36/Q37 y 档 +0，Q130 与核心分毫不差（与 proof2 同）。
- Q148：stem_ok=True，key_in_content8=True，extracted=`devant le`。

## §9 creambox 规范扫描（33 盒，`creambox-reproof.log`）+ P2 desc-clear −2.2 真墨复核

- 33 盒。7 条 naive `clearance -` 行全部判定为**下一标题误报**（BELOW-WINDOW +24.0/+37.0，下一节标题首行；
  `LE MOT DE LA SEMAINE` −24.0、`LA SEMAINE EN CHIFFRES` −37.0、`À VOUS !` −37.0 ×3、
  `IL EST PRÉVU QUE + SUBJONCTIF` −37.0、`LE DÉBAT` −37.0，与 proof2 同类）。
- **P7 盒 `y=1878 bottom=2258.0`**：末基线 2233.3，clearance **+24.7**，desc-clear **+18.8**；
  P7-TOOLBOX 汇总：4 盒，最小盒内清除 +24.7，最小 desc-clear +18.8。P7 干净。
- 唯一 inside-only desc-clear 负值：P2 ET VOUS 盒（y=974，bottom=1279.6），末行
  `說說你的11月19日：用法語寫兩句寄來。` 基线 1275.8，clearance +3.8，desc-clear **−2.2**。
  本人 PIL 真墨复核（`cards/p2-vie.png`，1950×2700，与 SVG 同坐标，阈值 L<200）：
  该行真墨行为 y 1258..1277，**墨底 1277，盒内余白 +2.6**；y≥1280 墨量 **0 px**。
  fitz span bbox y1=1281.5 为字体度量填充，非真实墨迹。**desc-clear −2.2 为误报，无漫出。**
  （其余各页盒内最小清除量均为正，与 proof2 一致。）

## §10 盒标题真墨 + 溢出横扫（spill_sweep，`spill_sweep-reproof.log` / `spill_sweep.json`）

- `spill_sweep.py`（fitz span 真实墨迹 bbox，真 SVG 坐标 1950×2700）：findings=25，
  **全部为 `below_box_baseline`**（下一节标题/下一盒标题，与 proof2 的 25 条同类同坐标，
  含 P1 `LES DATES` 其自身日期盒内标题、P7 `LA SEMAINE PROCHAINE` +58.0 等）。
- **盒右缘溢出 0、页右缘溢出 0**（spill_sweep.json 计数：`below_box_baseline: 25`，其余 kind 0）。
  occlusion 0 与 boxtitle_rc 0 对此类是空信号，故本项以 PIL/fitz 真墨为准，结论：无盒标题真墨溢出。
- rc=1 仅因 findings 存在（脚本口径），非失败；25 条已逐条核对为误报。

## §11 回归复验

### D1 — 简体残留（opencc s2t 逐字扫，本人实跑，`simplified-residue-reproof.json`）

- 8 页 SVG + `expl.py` + `.text.md` 全部 CJK 字：**简体字 0 个**（`{}`）。
- `expl.py` 全文：`准`（U+51C6）**0 个**、`準`（U+6E96）**2 个**（`zoom_note:120`、`n_vf1:230`，均为「獲準」）；
  `.text.md` 同：`準` 2、`准` 0。D1 仍修好。

### D2 — 行首孤字 。×3（目视逐一确认）

- P2 gloss 框：`註｜virgule 逗號　voter 投票　fêter 慶祝。` 单行完整，句号行内（`png/p2.png`）。
- P2 ET VOUS 框：`說說你的11月19日：用法語寫兩句寄來。` 单行完整（`png/p2.png`；另见 §9 真墨复核）。
- P3 ZOOM 框：`1951年獲準提前售酒、1985年定為11月第三個星期四、2026年是75週年。` 2 行，
  句号落第 2 行行末（`png/p3.png`）。
- 孤儿扫 new=0（§8），三处旧址均无孤儿。D2 仍修好，新增 0。

### SVG 回归（哈希比对）

- vs fix1 修前备份（`scratch-fix-fr-zh-tw1/svg.pre-fix.sha`）：**仅 P4 不同**
  （`5af79c73` → `b4d0e944`），其余 7 页逐字节一致。
- vs #1 备份（`scratch-refanout-fr2/backup-old/`）：P2（7e372c72→b46154cf）、P3（f3280832→22af3699）、
  P8（86da3308→7b8c6116）变——为 proof2 轮 D1/D2/Q148 修复；P4 变——为本次 D3 修复；
  P1、P5、P6、P7 字节相同。改动页与修复项一一对应，无多余改动。
- `expl.py` diff vs 修前恰 1 行（§6）；`ABSTRACT.txt` 修前 SHA 与 fix1 记录相同，未动。

### Q148 / Q130 / Q36/Q37

- Q148：键 `content8.py:170`（`"devant le"`）+ P8 抽取键 148 = `devant le` + `.text.md` 答案区
  `148. devant le（電影院門口）`，三重一致；题干无 `du`（§7 verify_ed_fr）。
- Q130：P8 抽取键 = 核心键 = `Le Sénat va voter mercredi.`，与核心分毫不差。
- Q36/Q37：抽取键与核心逐字相同（`On ne boit pas d'alcool avant 18 ans.` /
  `Le beaujolais n'est pas un vin blanc.`），y 档 +0（§8）。

## §12 D5 字体普查（只记录，不判定；`d5-font-census-reproof.json`）

- 本版：Newsreader 931、Noto Sans CJK SC 654、Noto Serif CJK SC 114、DejaVu Sans 4、UnifrakturMaguntia 1；
  CJK 字体 768 段中纯拉丁 362 段。
- 核心对照（同一方法）：Newsreader 936、Noto Sans CJK SC 660、Noto Serif CJK SC 115、DejaVu Sans 4、
  UnifrakturMaguntia 1；CJK 字体 775 段中纯拉丁 361 段。
- 差量小且均可解释（读者语译文换行导致的同文分段差异；proof2 记的 `selon moi＝` 全角等号等同类）。
  与 proof2 的计数口径略异（Serif CJK 114 vs 115，系 `<text>` 元素计数口径差），结论一致：无新增内容。
  D5 只记录不判。

## §13 150 题逐题手验（`.text.md` 1,087 行全文通读 + 三源交叉）

- `.text.md` 全文 1,087 行通读：150 题题干/选项/答案/注记逐题核对题干事实与文章内容，
  繁体注记逐条核对语法与译义。**150 键全部正确。**
- 三源交叉（P8 抽取键 / text.md 答案区 / 核心 P8 键）：150/150 一致，仅 Q150 不同（写作键 `開放題` vs 核心 `开放题`）；
  text.md 答案区 150 条全解析、0 缺失、0 实 mismatch；带注记答案 121 条，与 P8 抽取注记数 121/150 一致（§7）。
- key-vs-stem 适配逐项手核（Q73 教训专项）：配对题 Q22–25（vote/décision、vin primeur/jeune、déchet/jeter、finale/dernier match）、
  Q49–52（forfait/blessure、tableau/liste、tirage/sort、trêve/pause）、Q73–76（prequel/avants、bande-annonce/présente、
  seconde main/acheter、atelier/répare）、Q85–88（sénateur/élu、rejeter/dire non、vote/décision、commission/prépare）、
  Q140–144（sénateur/vainqueur/tirage/primeur/déchet）全部适配正确；
  单复数配合逐一验——Q113 `propose`（Le cinéma 单数）、Q114 `aimé`（avoir 无配合）、Q115 `jouent`（Les Bleus 复数）、
  Q116 `écrit`（il 单数）、Q120 `irais`（si + 未完成过去时 → 条件式）、Q121 `semble`、Q122 `reçoit`、
  Q103 `rejetée`（la première partie 阴性配合）、Q107 虚拟式 `examine`（无 s）、Q106 `vote`（Sénat 单数）；
  翻译题 Q135–139 逐句验中法对应（135 看决赛=学法语、136 比较级 plus vite、137 depuis + 星期、138 futur proche + préparer、
  139 ne...pas encore）；Q11–14 日期填空无 `le`（`vote mercredi 18 novembre`）与本期正文体例一致（P1/P2 正文多处
  `jeudi 19 novembre` 同式），非缺陷。
- 抽查：Q26 注记与 P3 ZOOM 同事实（已为 `準`）；Q53 `plus vite`、Q64 `Lukas Dhont`（`Dont` 全版 0 次）；
  Q80 `458–0`、Q83 `9 déc`、Q84 `26 nov`（50 天期限）均与 P6 行事历一致；Q109 `lundi`（16 日星期一）、
  Q110 `Beaujeu`、Q117 `dimanche 15`、Q125–129 阅读理解均与原文一致。
- 人名逐一核对法文原文：東特（Dhont）、梅諾謝（Ménochet）、菲斯（Fils）、海米奇（Haymitch）、勞倫斯（Lawrence）、
  斯米亞（Smia）、梅杜爾（Meddour）、史考特·湯瑪斯（Scott Thomas）、吉茲（Guiz）、梅里愛（Méliès）、多雷（Doré）、
  廣重（Hiroshige）、阿特熱（Atget）、莫羅（Moreau）；台湾用法杜林、薄酒萊、藍軍。
- 徽章 134（10/12/18/15/14/15/12/38）；U+2019=0、U+00B7=0；卷号 VOL.4 各处一致；
  页脚 8 页均为「講解繁體中文」，P1 徽章「法語正文　繁體中文講解 — 給繁體中文讀者的版本」。

## §14 目视

- 8 页逐页目视（印刷 PDF 150 dpi，`png/p1.png`–`p8.png`）：**零问题**——P1 band_r1（法文标题止 1236.9、
  读者带起 1405.0）无重叠；各页无溢出、无遮挡、无截断；P7 披露框 2 行完整在奶油盒内；P8 对话区、答案流、写作框完整。
- D3 300 dpi 裁切目视确认（`png/p4-note-crop.png`，§6）；D2 三处修复点在整页目视中确认（§11）。
- 网页 PDF 抽查（`png/web-p1.png` / `png/web-p7.png`，100 dpi）：与印刷版布局、图片一致；印/网 token 差 0（§5）。

## 观察项（非缺陷，仅备查；与 proof2 同，核心继承）

- O1：P4 y=623.13、P6 y=653.69 行首 `—`（x=1007.0）为行首破折号，与后文同基线（如 `— 好球！`），核心继承，非视觉孤儿。
- O2：P7 披露行 2 行首为 `；`、P8 答案流续行行首为 `）`，均与核心同位同文，核心继承断行，不计入本版。
- O3：Q130 / P3 Q36 / Q37 孤行填空线与核心同位（§8），观察类。
- O4：band_spans 门所用 1920 单位系历史口径（SVG 实为 1950×2700，真值 = 读数 ×1.015625；净空真值更大，结论不变）。

## 结论

机械门 14/14 + freeze 8/8 + 确定性重建 8/8 + creambox 33 盒 + spill sweep 真墨 0 溢出 +
三源交叉 150/150 + 150 题逐题手验全部通过，**缺陷 0 项**，故结论 **(a) 零缺陷可定稿**。
D3（P4 孤儿 。）已修好并独立实测确认；D1、D2 回归仍修好；Q148 已落地；D5 只记录不判。
