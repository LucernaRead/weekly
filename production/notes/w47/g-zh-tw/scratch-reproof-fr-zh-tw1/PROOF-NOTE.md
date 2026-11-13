# PROOF-NOTE — W47 fr-zh-tw（法语核心 × 繁中读者版）独立复校 re-proof（fix1 重建版）

- 复校员：独立复校（与 fix1 修复员、与 proof1/proof2 均不同人），2026-11-11
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-fr-zh-tw1/`
- 结论：**(a) 零缺陷可定稿** — 缺陷清单为空。proof2 的唯一缺陷 D3 已修好并独立实测确认；
  D1、D2 回归仍修好；Q148 已落地；其余机械门全过；150 题逐题手验全部正确。
- 生产文件只读：复校期间未改任何生产文件，未 commit、未 push。确定性重建在沙盒副本中进行。
  复核前后三件 SHA 逐一相同；核心 core-fr 三件 SHA 与 proof2 的 fix4 记录逐一相同，未变。

## 身份核对（开工前与收工后两次实测，一致；与任务书先验值逐一相同）

| 文件 | 字节 | SHA-256 |
|---|---|---|
| `La-Lucerna-VOL4-fr-zh-tw.pdf`（印刷） | 30,551,088 | `baf81d032effddc59da8f9f8a97028aebab51b58c10f5432870dccce908b8e18` |
| `La-Lucerna-VOL4-fr-zh-tw-web.pdf`（网页） | 2,552,857 | `2766f3ed492f84349159ad3fb33f87c48291256495ca997e4b7518187d48d212` |
| `2026-w47-fr-zh-tw.text.md` | 45,992 | `e5c8c1cd50f04b7a67bf03403f6d0361d6bfd03ad975946895f0477dc8acf3a2` |

核心 core-fr 对照 SHA（fix4 定稿，复核前后各测一次，未变）：
- 印 `La-Lucerna-VOL4.pdf`：`a30af667b25929984c34cf2af621c0b15a3072f4db55a14e507d3682ace25a9d`（30,446,975 B）
- 网 `La-Lucerna-VOL4-web.pdf`：`56f50ca8ab7ec912408bb4eda77c5a1a36eb7cc2639f09400584a6166d58e141`（2,241,835 B）
- 文 `2026-w47-fr-zh-cn.text.md`：`52024e024d32ca22c32287c7954d05e2bae9480dd75448b65169bb4899d063df`（46,471 B）

## 缺陷清单

**无缺陷。**（以下为已核实修好与全部通过的检查项，非缺陷。）

## 已核实修好（proof2 缺陷 D3，独立重测，不照抄 fix1 数字）

### D3 — P4 孤儿句号 。 → 已修

- 位置：`expl.py:122`（`chiffres_note`），`svg/p4-sport.svg` y=520。
- 改动：仅 122 行一处，删「決賽」二字（`diff expl.py.pre-fix expl.py` 恰 2 行）；
  其余「決賽」出现处（`date_22:119`、`g2:39` 等）全部未动，`expl.py` 内「決賽」16 → 15。
- 实测量值（自写 `d3_verify_reproof.py`，`svglib.text_w`，serif 21.5，与 `content34.py:168` 的
  `p.para(..., 21.5, "serif", ..., CW - 44)` 宽度口径一致；栏宽 422.5−44 = **378.5 px**）：
  - 新句 `大師賽結果與杜林名單見本版正文。` = **344.0 px**（余量 +34.5），单行容纳，无孤儿 。；
    旧句 387.0 px（超 +8.5），与修前实测一致。
  - P4 SVG：新注为**单一** `<text x="1461.5" y="520.0" font-size="21.5">…。</text>`（句号附于句末）；
    基线 y=550.53（±1.0）上元素 **0 个**；P4 独立 `。` 元素 **0 个**。
  - `.text.md`：新句 1 次、旧句 0 次；印/网 P4 文字层均含新注 1 次、旧句 0 次。
- 渲染证据：300 dpi 裁切 `png/p4-note-crop.png`（SVG 坐标 x 1420–1880、y 490–600）——
  单行完整，句号行内；全页 150 dpi `png/p4.png` 同一位置亦无孤儿句号。
- 全版孤儿扫：新增真孤儿 **0**；全版孤儿元素仅 2 个（P4 y=623.13 `—`、P6 y=653.69 `—` 为核心继承行首破折号）。

## 已核实修好（proof1 缺陷回归，逐项目视+量测）

### D1 — 简体残留 准 → 已修

- 全版 opencc `s2t` 逐字扫描（8 页 SVG + `expl.py` + `.text.md`）：**简体字 0 个**
  （`simplified-residue-reproof.json` 为 `{}`）。
- `expl.py` 全文：`准`（U+51C6）0 个、`準`（U+6E96）2 个（`zoom_note:120`、`n_vf1:230`，均为「獲準」）。
- P3 ZOOM 框与 P8 第 26 题注记均已为「獲準」（P3 整页目视 `png/p3.png` 可见「獲準」）。

### D2 — 行首孤字 。×3 → 已修，新增 0

- 孤儿扫新增真孤儿 **0**（GATE-LOG §8）；三处旧址逐一目视确认（整页 150 dpi）：
  - P2 gloss 框：`註｜virgule 逗號　voter 投票　fêter 慶祝。` 单行完整，句号行内。
  - P2 ET VOUS 框：`說說你的11月19日：用法語寫兩句寄來。` 单行完整。
  - P3 ZOOM 框：`1951年獲準提前售酒、1985年定為11月第三個星期四、2026年是75週年。` 2 行，句号落第 2 行行末。

### Q148 — 已落地，三重核对全部通过

- 键：`content8.py:170`（`"devant le"`）+ P8 extract 键 148 = `devant le` + `.text.md` 答案区 `148. devant le（電影院門口）`。
- 题干：`content8.py:176` 为 `On se retrouve ({gnums[3]})___ cinéma ?`（无 `du`）；P8 SVG 对话区
  （基线拼接：`...On se retrouve` y=1292.76 + `(148)___ cinéma ? — Oui, à 19 h 30. Bon` y=1324.68）含 `On se retrouve` + `cinéma ?`，
  且全页无 `du cinéma`；P8 全页目视：`(148)___ cinéma ?`、答案区 `148. devant le` 均正确。

### 回归对照（与 fix1 修前备份 + #1 备份）

- SVG 逐页哈希 vs fix1 修前（`svg.pre-fix.sha`）：**仅 P4 不同**（`5af79c73` → `b4d0e944`），其余 7 页逐字节一致。
- vs #1 备份 `scratch-refanout-fr2/backup-old/`：P2、P3、P8 变（D1+D2+Q148，proof2 轮修复），P4 变（本次 D3 修复），
  P1、P5、P6、P7 字节相同。改动页与修复项一一对应，无多余改动。
- `expl.py` diff vs 修前恰 1 行；`ABSTRACT.txt` 未动；其余文件未动（本次复校零写入）。

## 其余手验（150 题逐题核对，无问题）

- `.text.md` 全文 1,087 行通读：150 题题干/选项/答案/注记逐题核对题干事实与文章内容，繁体注记逐条核对语法与译义。**150 键全部正确。**
  - 三源交叉（P8 抽取键 / text.md 答案区 / 核心 P8 键）：150/150 一致，仅 Q150 不同（写作键 `開放題` vs 核心 `开放题`）；
    text.md 答案区 150 条全解析、0 缺失、0 实 mismatch；带注记答案 121 条，与 P8 抽取注记数 121/150 一致。
  - Q73 教训专项（key-vs-stem 适配逐项手核，三源一致也可能同错）：配对题逐一验适配——Q22–25（vote/décision、vin primeur/jeune、déchet/jeter、finale/dernier match）、Q49–52（forfait/blessure、tableau/liste、tirage/sort、trêve/pause）、Q73–76（prequel/avants、bande-annonce/présente、seconde main/acheter、atelier/répare）、Q85–88（sénateur/élu、rejeter/dire non、vote/décision、commission/prépare）、Q140–144（sénateur/vainqueur/tirage/primeur/déchet）全部适配正确；单复数配合逐一验——Q113 `propose`（Le cinéma 单数）、Q114 `aimé`（avoir 无配合）、Q115 `jouent`（Les Bleus 复数）、Q116 `écrit`（il 单数）、Q120 `irais`（si + 未完成过去时 → 条件式）、Q121 `semble`、Q122 `reçoit`、Q103 `rejetée`（la première partie 阴性配合）、Q107 虚拟式 `examine`（无 s）、Q106 `vote`（Sénat 单数）；翻译题 Q135–139 逐句验中法对应（135 看决赛=学法语、136 比较级 plus vite、137 depuis + 星期、138 futur proche + préparer、139 ne...pas encore）；Q11–14 日期填空无 `le`（`vote mercredi 18 novembre`）与本期正文体例一致（P1/P2 正文多处 `jeudi 19 novembre` 同式），非缺陷。
  - 抽查示例：Q26 注记与 P3 ZOOM 同事实（已为 `準`）；Q53 `plus vite`、Q64 `Lukas Dhont`（text.md 3 处，`Dont` 全版 0 次）；Q80 `458–0`、Q83 `9 déc`、Q84 `26 nov`（50 天期限）均与 P6 行事历一致；Q109 `lundi`（16 日星期一）、Q110 `Beaujeu`、Q117 `dimanche 15`、Q125–129 阅读理解均与原文一致。
  - 人名逐一核对法文原文：東特（Dhont）、梅諾謝（Ménochet）、菲斯（Fils）、海米奇（Haymitch）、勞倫斯（Lawrence）、斯米亞（Smia）、梅杜爾（Meddour）、史考特·湯瑪斯（Scott Thomas）、吉茲（Guiz）、梅里愛（Méliès）、多雷（Doré）、廣重（Hiroshige）、阿特熱（Atget）、莫羅（Moreau）；台湾用法杜林、薄酒萊、藍軍。
- 8 页逐页目视（印刷 PDF 150 dpi；另抽查网页 PDF P1、P7，100 dpi）：零问题——P1 band_r1（法文标题止 1236.9、读者带起 1405.0）无重叠；各页无溢出、无遮挡、无截断；P7 披露框 2 行完整在奶油盒内；P8 对话区、答案流、写作框完整。
- P7 读者园地奶油盒（独立实测裁定，干净）：盒 `y=1878 h=380` 底 2258.0；披露段 2 行，末基线 2233.3，creambox inside-only 清除 **+24.7**、desc-clear **+18.8**；PIL 真墨（fitz span bbox，真 SVG 坐标）：末行墨底 2238.9，**盒内余白 19.1 px**；其下为白纸间隙与深绿带（起于 2270.0）。无溢出。
- P2 ET VOUS 盒 desc-clear −2.2（唯一 inside-only 负值）独立真墨复核：`cards/p2-vie.png` PIL 实测，该行墨底 y=1277，盒底 1279.6，**真墨余白 +2.6**，y≥1280 墨量 0 px——fitz bbox y1=1281.5 为字体度量填充，非真实墨迹，**误报，无漫出**。
- 孤行填空线（观察类，核心继承，不判）：Q130 (989.0, 843.0) 与核心分毫不差；P3 Q36/Q37 (538.5, 1864.7/1997.4) 与核心同位，y 档 +0（与核心同）。未修核心、未判。
- 徽章 134（10/12/18/15/14/15/12/38）；P8 最小字号 11.625pt；U+2019=0、U+00B7=0；印/网文字层逐页一致（101,440 B，token 差 0）；卷号 VOL.4 各处一致；页脚 8 页均为「講解繁體中文」，P1 徽章「法語正文　繁體中文講解 — 給繁體中文讀者的版本」。
- 盒标题 PIL 真墨扫（spill_sweep.py，fitz span 真实墨迹 bbox，非 advance）：奶油盒右缘溢出 **0**、页右缘溢出 **0**；基线落在盒外的行 25 条，全部裁定为下一节标题/下一盒标题误报（与 proof2 同类同坐标），无真溢出。

## 记录项（不计入本版判定）

### R2 — D5 字体（全周级已知待定项，如实记录，不判）

- 实测（与核心同一方法普查）：8 页 SVG 字体——`Newsreader` 931 段、`Noto Sans CJK SC` 654 段、`Noto Serif CJK SC` 114 段、`DejaVu Sans` 4 段（P7 ✗ 标记，合理）、`UnifrakturMaguntia` 1 段（刊头黑体）。
- 其中 768 段 CJK 字体中 **362 段为纯拉丁文**（核心对照：775 段中 361 段）。本版与核心的差量小且均可解释（译文换行导致的同文分段差异，含 `selon moi＝` 全角等号 vs 核心半角 `=` 的读者语排版差）。无新增内容。

## 观察项（非缺陷，仅备查；与 proof2 同，核心继承）

- O1（旧）：P4 y=623.13、P6 y=653.69 行首 `—`（x=1007.0）为行首破折号，与后文同基线（如 `— 好球！`），核心继承，非视觉孤儿。
- O2（旧）：P7 披露行 2 行首为 `；`、P8 答案流续行行首为 `）`，均与核心同位同文，核心继承断行，不计入本版。
- O3：Q130 / P3 Q36 / Q37 孤行填空线与核心同位（见上），观察类。
- O4：band_spans 门所用 1920 单位系历史口径（SVG 实为 1950×2700，真值 = 读数 ×1.015625；净空真值更大，结论不变）。

## 参考

- 门禁明细：同目录 `GATE-LOG.md`、`gates-reproof.json`
- fix1 记录：`hidden_files/w47/scratch-fix-fr-zh-tw1/FIX-LOG.md`（仅作开工核对参考，结论均为本人独立重跑）
- proof2 记录：`hidden_files/w47/scratch-proof-fr-zh-tw2/PROOF-NOTE.md`（D1/D2/Q148 回归核对口径来源）
- 证据图：同目录 `png/`（p1–p8 印刷版 150 dpi、`p4-note-crop.png` 300 dpi D3 裁切、`web-p1.png` / `web-p7.png`）
