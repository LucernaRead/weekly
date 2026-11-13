# GATE-LOG — 2026-W47 · ko → fr · proof1 机械门实跑证据

复校员独立实跑，不信 KIT，只信自己跑的结果。freeze baseline/diff 与
run.py/check_core/check_gloss/textmd 一律用系统 python3（/usr/bin/python3，
Pillow 10.2.0 / FreeType 2.13.2）；render/webpdf 可走 venv（cairosvg/fontTools）。
TMPDIR 全程指向本 scratch 下 `tmp/`。
工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ko-fr1/`。
源码见 `gates/` 下各日志与 `visual/` 下各 PNG（`p1.png`…`p8.png`、`web-p1.png`、
`web-p8.png`、`zoom-p2/p3/p5-envoyez.png`）。

## §0 身份核对（磁盘为准）与探针

- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` →
  `76d189aef4a5bb2b3b4f3c0bb3e1dc96ff86b0c9`，RC=0；goals 侧 scratch 写入探针文件成功；
  `/dev/null` 在位；开工前 `git status` 仅 `?? production/2026-w47/2026-w47-ko-fr/` 与
  `?? production/2026-w47/core-ko/`（fan-out #3 未提交，与任务所述一致）。
- 印 PDF `Lucerna-VOL4-KO-FR.pdf`：SHA `e4db2a54a97f2d4a0c5f949617d7760055832e3096076599d15c16e40d98bdc2`，
  45,468,252 字节——**与任务一致**（开工与收尾两次核对一致）。
- 网 PDF `Lucerna-VOL4-KO-FR-web.pdf`：SHA `a5f712d25aa52a65d967bba45966bffe22d39b231098b37924cd0f0458c0cbc9`，
  4,022,321 字节——**与任务一致**（开工与收尾两次核对一致；只核落盘 SHA，未重渲染）。
- text.md `2026-w47-ko-fr.text.md`：SHA `4e5487a69ec8c6584f90d9674f16775696daf55cb892af88203c700f6c59f378`，
  35,275 字节——**与任务一致**（开工与收尾两次核对一致）。
- 核心 ko（run 11，08:40 落盘）8 个 SVG 开工/收尾哈希一致，未变：
  P1 `00227ca12f0319be…`、P2 `faf9e3c530f200b1…`、P3 `b447a559c6f8d61d…`、
  P4 `d997631ea586a9c8…`、P5 `09f7fc23850a1deb…`、P6 `d45b03557f02f47a…`、
  P7 `14b7cf136254b1cd…`、P8 `e88f7d421d621f92…`（全哈希见 `core-svg-hashes-before.txt`
  与 `core-svg-hashes-after.txt`）；核心 text.md SHA `da1d3a323f7c83eb95fe989e59f56ca6a706282c443f20cc5792c3f73468181a`
  与核心 KIT 一致。核心只读核查，未重建。

## §1 run.py（系统 python3，scratch 副本）

- 将版目录完整复制到 `work/ed-ko-fr/`（去 `__pycache__` 与 `cards/`），在副本内跑
  `/usr/bin/python3 run.py` → `gates/run.log`，**rc=0**，0 FLOW OVERFLOW / HEAD TOO WIDE，
  TOTAL **150**（A2 51 / B1 72 / B2 27；按页 10/18/18/18/18/18/12/38；
  按类型 Compléter 48、Choix multiple 52、Apparier 16、Transformer 4、Faire des phrases 8、
  Vrai ou faux 4、Texte à trous 13、Traduire 4、Écrire 1；范文 169 字；
  P2-feature ends 1531、P8-keys ends 2426、P7 teaser 2510.22）。
- 重建的 8 个 SVG 与交付 SVG **字节一致**（`gates/run-svg-hashes.txt` vs `edition-svg-hashes.txt`，diff 空）。

## §2 印 PDF 重渲染（venv，仅 scratch 副本）

- 在同一副本内跑 `tools/venv/bin/python render.py` → `gates/render-pdf.log`，rc=0。
- 重渲染印 PDF：45,468,252 字节，SHA `e4db2a54a97f2d4a0c5f949617d7760055832e3096076599d15c16e40d98bdc2`——
  **与交付印 PDF 字节一致**。重渲染产物（cards + 副本内两 PDF）已按 builder 惯例删除，日志与哈希留存；生产目录的印 PDF 未动。

## §3 freeze / freeze diff（系统 python3）

- `tools/freeze.py baseline --build production/2026-w47/core-ko --core-svg …/core-ko/svg --out gates/freeze-baseline`：
  **8/8 SVGs byte-identical**，工具自报 8/8（逐文件 OK 行；`gates/freeze-baseline.log`；
  重建产物在 `gates/freeze-baseline/svg/`）。core integrity：运行前后核心 SVG 重哈希未变。
  运行时打印：`/usr/bin/python3 | Pillow 10.2.0 | FreeType 2.13.2`。
  （按 ko 家庭铁律未在 venv 下跑 freeze——venv 的 Pillow 13 会按守卫豁免 ABORT rc=2，那是预期行为。）
- `tools/freeze.py diff --core-svg core-ko/svg --edition-svg ko-fr/svg`（`gates/freeze-diff.log/json`）：
  各页 +17~+174 / −15~−167 串；**新增 CJK 共 7，全为 U+3000**（每页 1 个，页脚分隔符）。
  即全部新增内容只属于法语讲解层，韩文串无新增。

## §4 occlusion audit（tools/occlusion_audit.py）

- 命令：`./tools/venv/bin/python tools/occlusion_audit.py <edition>/svg --core <core-ko>/svg --json gates/occlusion.json`
- 结果：**0 flags**（edition 与 core 均为 0，NEW vs core 0）；selftest 通过（6 类 planted flags 全触发，clean 对照静默）。RC=0。`gates/occlusion.log`。
- 局限（已知）：该工具不覆盖无边框奶油盒标题横向溢出与 `<image>` 遮挡——本版前者由 §5 PIL 真墨水排除，后者由 8 页目视覆盖。

## §5 正典 creambox.py 全版扫描 + Et vous 盒 PIL 真墨水复核

- 命令：`/usr/bin/python3 <goals>/hidden_files/w47/tools/creambox.py <edition>/svg/*.svg` → `gates/creambox-all.log`（361 行，49 个盒）。
- 结果：全部**盒内行（inside-only）clearance 为正**，最小 +5.7；**P7 toolbox**：3 个盒，min inside clearance **+12.5**，min desc-clear **+6.5**。
- 20 条 BELOW-WINDOW 行（+26..+44）全部为盒下相邻标题/表行/表注，逐条裁定假阳性：
  P1 `지금 바로 연습`（+37.0）、`이번 주의 말`（+34.0）、quiz 导语（+44.0）；P2 `김장 나눔`/`겨울 밥상`（+37.0）、D-day strip  mnemonic（+26.0）；
  P3 `김장을 담그는 날`/`김치, 어떻게 먹어요`/`늦가을 산책의 옷차림`（+37.0）；P4 `야구장의 응원`/`결과가 나온 경기`（+37.0）；
  P5 `수능이 끝나면`/`김치의 날, 청년의 아이디어`/`시험 전날의 하루`（+37.0）；P6 `결과를 알 때`/`뉴스의 날짜 찾기`（+37.0）、
  表格行标签 `단풍`/`예보 날짜`/`예보 날짜 지났어요`（+35.0，下一表行）、表源注（+30.0，表下注文）。
- 3 处 inside-only desc-clear **−0.3**（P2/P3/P5 Et vous ? 盒末行 `envoyez-les-nous.`，基线 y=1221.24/1531.99/847.24，盒底 1226.9/1537.7/852.9）：
  为公式假象——creambox 假设 0.30×字号降部（20px→6px），而 PIL 真墨水实测该行 Noto Sans CJK KR 20px 的 `y`
  实际降部 5px（`gates/ink-envoyez.log`：`getbbox(anchor="ls")` bottom=+5，三盒一致），真墨水底缘在盒底内
  **+0.66 / +0.71 / +0.66 px**；300 dpi 像素裁图（`visual/zoom-p2/p3/p5-envoyez.png`，`gates/pixelscan-envoyez.log`）
  目视确认降部在盒内、盒下留有奶油空隙。紧配合、非缺陷（ko-es 先例标准：真墨 ≥ +0.1 即在盒内）。

## §6 boxtitle 8/8（系统 python3）

- `boxtitle-ko.py <edition>`（读版内 content 文件的 `box()` 标题 + P7 col-3 `p.text` 标题，用版内 `svglib.text_w` 量，预算 386.5px）→ `gates/boxtitle.log`，**8/8 通过**：
  326.9 / 256.9 / 360.4 / 323.7 / 379.1（`이번 주 청년 숫자　Chiffres jeunesse`，最紧，余 7.4px）/
  327.0 / 275.9（`이번 주의 틀　La structure`，#2 已缩短）/ 369.5 px。

## §7 p8 extract / compare（显式 --total 150）

- `tools/p8.py extract --p8 <edition>/svg/p8-siheom.svg --total 150`：**noted set = 150 of 150**。RC=0。`gates/p8-extract.{log,json}`。
- `tools/p8.py compare --core-p8 core-ko/svg/p8-siheom.svg --edition-p8 <edition>/svg/p8-siheom.svg --total 150`：
  **CLEAN**，core 150 noted / edition 150 noted，missing=[]，extra_count=0，uncertain=[]，**keydiff=[137, 138]**。RC=0。`gates/p8-compare.{log,json}`。
- keydiff 裁决：137、138 为 E 节翻译题（KO→FR），键合法重定向到读者语；键本身逐字正确
  （137 `11월 22일은 김치의 날이에요.` → `Le 22 nov., c'est le Jour du kimchi.`，注 Voir p. 2；
  138 `삼성이 12년 만에 우승했어요.` → `Samsung a gagné le titre après 12 ans.`，注 Voir p. 4）。
  139（法→韩 `11월 18일은 예비소집이에요.`，注 Voir p. 5）、140（→ `일요일에는 가족과 김치를 나눠 먹어요.`，注 Voir la partie C, p. 8）键与核心一致。

## §8 keycheck 150/150（独立脚本，三源手验）

- 自写 `keycheck.py`（AST 解析版内 content*.py 的 `.ex`/`.match_set` 得 REG 150 项，与 p8 extract 的键逐项比对）→ `gates/keycheck.{log,json,txt}`：
  **exact 149，trunc-ok 1（#150 `✓`，预期，与核心一致），BAD 0**。
- 手验方法：text.md 全文通读 + 印 PDF 8 页目视 + REG 题干逐条重推（`gates/reg-stems.txt` 全表）。
  配对题字母对照印刷版 a–d 列表（P2 D：25-d、26-a、27-c、28-b；P3：43-b、44-a、45-d、46-c；
  P4：61-c、62-d、63-a、64-b；P8 F：141-b、142-c、143-a、144-d，均与印刷顺序一致）。
  算术重算（19 天、1 天、4 小时、17 年、65、100）；范文计词 169（150–200 内，逐字计数，`gates/sweeps.log`）。
  P7 金句 8 条逐字出自本期正文，页码标注逐一核实正确（2면/1면/4면/2면/3면/6면/1면/6면，`gates/p7phrases.log`）。
- 重复题干说明：#12=#8、#13=#9、#18=#22、#74=#37 等逐字重复——与核心 ko 源文件逐字相同
  （逐项比对核心 content12/34/56/7/8.py），为核心原文设计；text.md 导出按去重规则只列一次，
  census（§10）0 缺失。

## §9 check_core / check_gloss（系统 python3，scratch 副本）

- 自写 `check-edition.py`（复制核心 check 脚本，ED/BUILD 指到本版，gloss 前缀 `译注` → `Note — `，strip 改为 len(prefix)）→ `gates/check-fr.log`，**rc=0**：
  gloss fails **0**；P7 phrases **8/8 verbatim**（含核心 D4 新句 #7 `수능이 끝나면 일요일 11월 22일에는 김치의 날이 와요`）；
  orphan issues **0**；dates 全部正确（2026-11-16 Mon → D-3、11-18 Wed → D-1、11-19 Thu → D-day、11-22 Sun → 김치의 날；
  Nov 16 周一、Nov 18 周三、Nov 19 周四、Nov 22 周日、Nov 28 周六）。
- `check_gloss.py`：gloss fails **0**。

## §10 textmd 重导出 + census

- 在 scratch 副本内跑 `/usr/bin/python3 textmd.py . 2026-w47-ko-fr <scratch>/gates/textmd-reexport.md "Lucerna Korean Weekly VOL.4 — Korean text, French explanations (2026-W47)"` →
  `gates/textmd.log`，rc=0，pages [1..8]，items **449**；重导出与交付 text.md **字节一致**（`cmp` 通过）。
- `census.py <edition>/text.md <edition>` → `gates/census.log`，rc=0：ex/match items 166，**0 missing**；D6 0 missing。
- 449 vs 核心 452 的三项对账（见 PROOF-NOTE）：`Tout`（is_prose 丢弃；P1 SVG 在 (1840.0, 1600.0) anchor=end 存在；核心平行项 `全部` 保留）、
  `lcn2`、`lko`（按设计移除，本版 P7 只留 1 行法语 disclosure）。

## §11 印/网文字层比对

- `pdftotext`（plain）印版与网版各 **52,304 字节，字节一致**（`cmp` rc 0；`gates/print-plain.txt` vs `gates/web-plain.txt`）；
  `pdftotext -layout` 各 108,403 字节，字节一致（`gates/print.txt` vs `gates/web.txt`）。
- 网 PDF 8 页（PyMuPDF 确认）；只核落盘 SHA，**未重渲染**（webpdf 字节不可复现，铁律遵守）。
- 网 PDF −2,439 B 算术核对：4,024,760（#2，KIT 记载）− 4,022,321（今）= 2,439 ✓；文字层 52,232 → 52,304 = +72 ✓。

## §12 斜体 + P8 最小字号实测（PyMuPDF，双 PDF）

- 全书 span 扫描（`gates/minfont-italic.log`）：印版与网版均为 1,703 spans，最小字号 **9.98 pt**；
  P8 answers 区域（y≥976pt，即 1302/2700）170 spans，165 @ 9.98pt + 5 @ 12.75pt——与 KIT 的 9.975pt 一致（取整差），≥ 9.75pt 合规。
- italic span：印版 **0**，网版 **0**——印版自身无斜体，网版无丢失；nl-ko 的 D5 斜体丢失类在本版不复现。
  SVG `<text>` 的 `font-style="italic"` 亦为 0（`gates/sweeps.log`）。

## §13 弯引号 / 孤儿标点 / 字符全扫（XML 解析，绝不用 grep 扫 SVG）

- SVG 全 1,503 个 `<text>` 行：U+201C/U+201D/U+2019/U+201E 全部为 **0**（Frame 「」 修好）；
  text.md 同四项全部为 **0**；text.md U+0027 ×61（韩语单引号 + 法语省音，全为直引号，合规）；
  SVG 与 text.md 的 Han 字符（U+4E00–U+9FFF）均为 **0**；SVG U+3000 ×124（分隔符），text.md U+3000 ×0；
  text.md `___` ×75，与核心 text.md 的 75 处逐字相同（KIT 所称“23 处”为 KIT 笔误，非版面缺陷）。
- 孤儿标点全扫（`gates/sweeps.log`）：独行 `.` **0**、独行右引号（」/』/”/»）**0**、
  行首孤儿标点（`)]}.,!?%:;`）**0**、独行 `:`/`：`**0**、独行 `–`/`—`/`-` **0**；`..` 双句号：SVG 0、text.md 0（核心亦 0）。
- `Tout`：P1 SVG 唯一一处，x=1840.0, y=1600.0, 18px, anchor=end（右缘 1840，版心内）；text.md 0 处（is_prose quirk，见 PROOF-NOTE）。
- 法语层英语残留扫描：` the / and / with / for / of / in / is / are ` 在 SVG 文本中均为 0 命中。

## §14 §1.1 风格审计（style11-ko.py，核心 vs 本版逐页）

- `gates/style11.log`，rc=0，**OK**：paper `#fbfaf6` 计数逐页与核心一致（P1 1、P2 1、P3 1、P4 4、P5 1、P6 4、P7 1、P8 1）；
  VOL.4 逐页一致（P1 2、其余 1）；`·` 逐页一致（13/21/20/14/20/31/17/38）；P1 未知色与核心逐色一致
  （照片标题色 `#34483a` 等，同一组）；hanzi **0**；U+2019 **0**；P7 VOL.5 3→2（按设计，`lko` 行移除）。

## §15 ABSTRACT.txt

- 378 字节、单行（1 个尾换行）、ASCII 双引号 0 个、法语（`gates/sweeps.log`）：
  含 `Lucerna Korean Weekly VOL.4`、CSAT、Jour du kimchi、Samsung 首冠、examen d'histoire、feuillages、
  `niveaux A2 à B2`、`150 exercices`。通过。

## §16 目视（150 dpi 自渲染，印版 8 页 + 网版 P1/P8）

- `visual/p1.png`…`p8.png`（印版）、`visual/web-p1.png`、`visual/web-p8.png`（网版与印版一致）：
  8 页逐页目视——无溢出/重叠/压页脚/图片问题；P7 照片未遮 col-4 两盒（「이번 주의 틀」「독자의 편지」完整）；
  P4 梯形图第 4 盒在幅内、P6 比较表右缘在幅内；P1 drop cap、moth、单线 masthead rule 正确；
  8 张图片均带目标语图说 + CC0/PD 出处，图说诚实（P1 秋日为资料照片、P2 明确“不是 김장 사진”、P3 Cézanne 注明画作）。
- P1 quiz #10、P4 #47/#48、P7 frame/金句 #7 的新核心内容在渲染中目视确认（§2 承接项）；P7 Frame 盒「」形目视确认。

## 附：工具与方法备注

- 绝不用 `grep` 扫 SVG 原文：SVG 含巨大 base64 图片数据；一律用 Python 按 `<text>` 元素解析。本轮一次误用 `grep Tout` 命中 base64 blob（~200KB 输出），已废弃该做法，改用 XML 解析重核。
- PIL `font.getbbox` 默认 anchor 是 `"la"`，bb[3] 为 ascender+descent，不是基线以下降部；本轮真墨水降部一律用 `anchor="ls"`（`gates/ink-envoyez.log`）。
- 200 dpi/300 dpi 像素扫描只渲染窄条带 clip，不整页并行渲染。
- `textmd.py` 需 4 个实参（build_dir、slug、out_path、title），无参跑报 `IndexError`（首次误跑已记录，非门禁失败）。
- `check-edition.py` 与 `keycheck.py` 为本轮自写（方法复用 fan-out-ko3 的同类脚本，代码与输出均在本 scratch 内，可独立重跑）。
