# D5 重建 — it 家庭工作日志（工人 ccd7032a，接替 f87eedbb）

- 开工：2026-11-12 ~02:40 EST（07:40 UTC）。前任 f87eedbb 02:31 EST 被运行时重启打断（"restart drain in progress"）；9c8ec6e6 01:59 EST 被 cron 超时打断。
- 工作区沿用前任：`hidden_files/w47/scratch-d5-rebuild-it/`（gates.sh、logs/、baselines/、backups/、pre-rebuild-sha.txt）；本日志在 `scratch-d5-it/RUN-LOG.md`。
- 范围：core-it 核实 + 7 个 Latin/Russian fan-out（it-en/es/fr/de/nl/pt/ru）。CJK（it-ja/ko/zh-tw）不动——CJK-DECISION.md 已落地（§1 script-based、mode=cjk），等协调员另派。

## 接手时核实（core-it，2026-11-12 07:40 UTC）

- svglib.py 已装 D5（md5 ca7ad2d5…，含 _D5_READER="cjk" + fix2 路由；与正典模板路由代码逐字节一致待验）。
- 盘上印/网 PDF（06:56/06:58 UTC）= 第 2 轮重建产物，与 round2-core-it/ 副本 SHA 一致：
  印 d55aace3f6f3…（14,833,154 B）、网 d8bb30a0d23f7…（1,540,032 B）。
- 但第 2 轮门禁未全过：第 1 轮 gates（06:42–06:48）检出 boxtitle 2 DEFECT + creambox FAIL 2 defects（同 2 项：P1 '数字看本周' 右越 +42.6px、P4 'DOPO 11 GIORNATE' 右越 +16.8px；修前基线 boxtitle-pre 0 DEFECT，确为 D5 引入）；edge/freeze/textlayer 日志缺失（第 1 轮 gates 未跑完）。
- f87eedbb 第 3 轮已在源头修了这 2 项（content12.py tsize 20→17.5、content34.py 20→18.5，均带注释；另 content56.py P6 head 25→23，修第 1 轮 run.log 的 1 处 HEAD TOO WIDE），run3.log（07:29）TOTAL 150、0 FLOW OVERFLOW / 0 HEAD TOO WIDE；生产 svg/p1、p4 已是第 3 轮产物（p2/p3/p5–p8 与第 2 轮一致）。但 render3 被重启打断（render3.log 0 字节），**盘上 PDF 仍是第 2 轮（修前）产物，与当前 SVG 不一致**。
- KIT 仍记修前 SHA（印 c45fbe9f…/27,726,409 B、网 885830b7…/1,790,692 B），须同步。
- 结论：core-it 需补 render + webpdf + 全套门禁 + KIT 同步，不重建 run（SVG 已是第 3 轮；freeze 会验复现性）。

## core-it 第 4 轮（本任）
（待填）

## core-it 第 4 轮（本任）— 完成 ALL-GREEN
- run4: TOTAL 150、0 FLOW OVERFLOW / 0 HEAD TOO WIDE；8 SVG 与第 3 轮逐字节一致（复现性验讫）。
- render4 + webpdf4：印 f867980ae60d…（14,833,164 B）、网 aceaf1055042…（1,540,034 B）。
- gates4 ALL-GREEN：occlusion 0；p8 150/150、compare CLEAN keydiff=[]；census D5 0/0、curly_cjk 0（4 弯引号全在 Newsreader）；boxtitle 0 DEFECT（26 titles）；spill 0；creambox PASS 0 defects（P8 245→245 行、余量 45.4px）；edge 0 TOUCH/NEAR；freeze 8/8；freeze-diff 新增 CJK 0；印/网文字层逐字节等（38,103 字符）；text.md 不变 9eb9ee06…。
- KIT 已同步：§11 D5 rebuild（新 SHA/大小 + 门禁记录；§10 SHA 已作废并注明）。已删 round2-core-it/（19M）与 freeze-core-it/（33M）旧 build 副本。

## it-en — 完成 ALL-GREEN
- 修前普查：D5 拉丁 492、西里尔 0、弯引号 CJK 0（与 D5-CENSUS-130 一致）。
- 安装：apply_variant --target it --reader en（mode latin）；fix2 已有、保留；assert_routing FAILURES: 0。
- 第 1 轮：TOTAL 150，1 HEAD TOO WIDE（P6 `D　LE PAROLE DELLA MANOVRA`，与 core-it 同源）→ content56.py head 25→23。
- 第 2 轮：TOTAL 150、0 警告；门禁 FAILURES：boxtitle/creambox 6 DEFECT（P1 FIGURES +38.6、P1 CONTENTS +40.2、P2 LEARN +37.3、P4 DOPO 11 GIORNATE +16.8、P7 TYPICAL ERRORS +19.8、P7 WORD OF THE WEEK +23.5；余项全过）。
- 修：svglib text_w 量算（留 4px 余量、向下取 0.5pt）：两 f.box tsize 23→20.5、CONTENTS 24→21.5、DOPO 11 GIORNATE 21→19.5、P7 两标题 23→21.5。
- 第 3 轮：TOTAL 150、0 警告；gates3 ALL-GREEN（occlusion 0；p8 150/150、compare CLEAN keydiff=[137,138,139] 为预期读者语键；census 0/0/0；boxtitle 0 DEFECT；spill 0；creambox PASS 0 defects，P8 244→244 行、余量 45.4px；edge 0/0；freeze 8/8；新增 CJK 仅 U+3000×13；印/网文字层等，43,859 字符；text.md 不变 ad311b5b…）。
- 交付：印 6f0bbf408826…（13,497,072 B）、网 da29562db637…（1,215,817 B）、text.md ad311b5b…（55,183 B，不变）。
- KIT 已同步：§15 D5 rebuild。已删 freeze-2026-w47-it-en/（31M）。

## 范围扩展（2026-11-12 03:04 EST，协调员通知）
- 已读 CJK-DECISION.md 全文 + brief-d5-rebuild.md 全文。CJK 读者版（it-ja/ko/zh-tw）按字符分流、mode=cjk、与 latin 版同一套门禁；在 Latin/Russian 7 版做完后接做。
- 机制注意：(a) boxtitle 备份查找按版目录名取 slug——gates.sh 传的即 slug 命名的生产版目录，合规；(b) it-ko 的 freeze 门在 venv 下可能 ABORT（freeze.py 对 ko 路径要求 Pillow 10）——仅 freeze 这一步可用系统 python3 跑一次（先确认系统 python3 确有 Pillow 10；没有则上报，不绕门）；(c) 重建后 census_quotes 须为 0（KR 引号不扩展，裁定 §3）；(d) occlusion_audit.py 已含 §10 修复（裸 Noto Sans 量非 CJK 面）——已验 grep，en-ru 式 P8 误报不再修。
- 落盘批复溯源：core-it svglib 与 installer 在 pre-D5 备份上重跑的结果逐字节一致（--target it --reader zh-cn，mode cjk）——core-it 是 installer 安装，不是手写块。it-en、it-es 均由本任用 apply_variant.py 安装（installer）。手写变体块指 scratch-fanout-it/build_edition.py L112–145（ru 整拷 core-ru、zh-tw 整拷 core-zh-tw、ja/ko SC→JP/KR 改写 + kinsoku 移植）；该脚本本身本次未改（属落盘后续动作，由协调员另行安排；本任只负责各版用 installer 安装，并在汇报里注明来源）。
- it-ja/it-ko/it-zh-tw 的 CJK 基底（JP/KR/TC 面改写）来自该手写块，D5 安装时保留（installer 报 CJK index already JP/KR 即正常）；D5 路由本身一律 installer。

## it-es — 进行中
- 修前普查：D5 拉丁 494、西里尔 0、弯引号 CJK 0、curly_total 0（该版无弯引号）。
- 安装：apply_variant --target it --reader es（mode latin）；svglib 原为 pre-fix2（05e25a02），安装补了 fix2 + _QUOTE_CLS；assert_routing FAILURES: 0。
- 第 1 轮：TOTAL 150，2 HEAD TOO WIDE——P1 `ADESSO TU　AHORA TE TOCA A TI`（25pt 量宽 462.8，超栏 40.2）→ 22.5；P6 `D　LE PAROLE DELLA MANOVRA` → 23（与 core-it 同源）。
- 第 2 轮：TOTAL 150、0 警告；门禁 FAILURES：boxtitle/creambox 7 DEFECT（P1 LA SEMANA EN CIFRAS +216.6、P1 body +6.2、P1 SUMARIO +22.2、P2 PARA RECORDAR +165.3、P4 DOPO 11 GIORNATE +16.8、P7 ERRORES TÍPICOS +26.8、P7 PALABRA DE LA SEMANA +81.5；edge 1 NEAR、余项全过）。
- 量算发现：4 处修前已越框（旧 svglib 量宽：P1 box +134.7、P1 body +12.6、P2 box +99.3、P7b +17.5）——西语副标过长，D5 只是加重；3 处为 D5 新引入（SUMARIO、P4、P7a）。
- 修（量算 + 简报 §4 缩短副标/降字号）：P1 box 副标 LA SEMANA EN CIFRAS→EN CIFRAS、tsize 19.5（全文需 14.5pt，不取）；P1 body 19→18；SUMARIO 24→22.5；P2 box 副标 PARA RECORDAR→RECORDAR、tsize 18.5（全文需 16pt，不取）；P4 21→19.5；P7a 23→21；P7b 全文保留、23→18.5。
- 第 3 轮重建进行中（run3/render3/webpdf3/census_quotes），待门禁。

## it-es — 完成 ALL-GREEN
- 修前普查：D5 拉丁 494、西里尔 0、弯引号 CJK 0、curly_total 0。
- 安装：apply_variant --target it --reader es（mode latin）；原 svglib pre-fix2，安装补 fix2；assert_routing FAILURES: 0。
- 第 1 轮：TOTAL 150，2 HEAD TOO WIDE（P1 AHORA TE TOCA A TI 25→22.5；P6 LE PAROLE DELLA MANOVRA 25→23）。
- 第 2 轮：TOTAL 150、0 警告；门禁 7 DEFECT（P1 LA SEMANA EN CIFRAS +216.6、P1 body +6.2、P1 SUMARIO +22.2、P2 PARA RECORDAR +165.3、P4 +16.8、P7 ERRORES TÍPICOS +26.8、P7 PALABRA DE LA SEMANA +81.5；edge 1 NEAR）。
- 量算：4 处修前已越框（P1 box +134.7、P1 body +12.6、P2 box +99.3、P7b +17.5），3 处 D5 新引入。
- 修：P1 副标→EN CIFRAS、tsize 19.5；P1 body 19→18；SUMARIO 24→22.5；P2 副标→RECORDAR、tsize 18.5；P4 21→19.5；P7a 23→21；P7b 全文保留 23→18.5。
- 第 3 轮：TOTAL 150、0 警告；census_quotes 0 缺陷；gates3 ALL-GREEN（occlusion 0；p8 150/150、compare CLEAN keydiff=[137,138,139]；census 0/0/0；boxtitle 0 DEFECT；spill 0；creambox PASS 0 defects，P8 213→213 行、余量 56.6px；edge 0/0；freeze 8/8；新增 CJK 仅 U+3000×8；印/网文字层等，44,605 字符；text.md 不变 4fd5647e…）。
- 交付：印 5c703a6665d2…（13,497,643 B）、网 f602876a0f91…（1,216,392 B）、text.md 4fd5647e…（56,193 B，不变）。
- KIT 已同步：§13 D5 rebuild。附注：§12 的 SHA（印 6c299214…/网 c194c342…）与盘上修前记录（印 551f5fbd…/网 d5deb6ef…）不符，§12 修复前已滞后，以盘上为准已在 KIT 注明。已删 freeze-2026-w47-it-es/（31M）。

## it-fr — 完成 ALL-GREEN
- 修前普查：D5 拉丁 497、西里尔 0、弯引号 CJK 0、curly_total 0。
- 安装：apply_variant --target it --reader fr（mode latin）；原 svglib pre-fix2，安装补 fix2；assert_routing FAILURES: 0。
- 第 1 轮：TOTAL 150，1 HEAD TOO WIDE（P6 LE PAROLE DELLA MANOVRA 25→23；法语 P1 头 À TOI DE JOUER 能过）。
- 第 2 轮：TOTAL 150、0 警告；门禁 5 DEFECT（P1 CHIFFRES +53.6、P1 SOMMAIRE +45.2、P2 DEVISE +44.3、P4 +16.8、P7 MOT DE LA SEMAINE +29.5）。
- 量算：5 处全为 D5 新引入（修前余量 −4.7/−6.5/−8.0/−28.9/−27.2px）。
- 修：P1 box tsize 23→20、SOMMAIRE 24→21、P2 box tsize 23→20.5、P4 21→19.5、P7b 23→21（P7a ERREURS 不动）。
- 第 3 轮：TOTAL 150、0 警告；census_quotes 0 缺陷；gates3 ALL-GREEN（occlusion 0；p8 150/150、compare CLEAN keydiff=[137,138,139]；census 0/0/0；boxtitle 0 DEFECT；spill 0；creambox PASS 0 defects，P8 212→212 行、余量 56.6px；edge 0/0；freeze 8/8；新增 CJK 仅 U+3000×8；印/网文字层等，44,708 字符；text.md 不变 aca1356c…）。
- 交付：印 02e2b67cdb96…（13,496,942 B）、网 1b26c4d53d58…（1,215,685 B）、text.md aca1356c…（56,517 B，不变）。
- KIT 已同步：§13 D5 rebuild。附注：§12 网 PDF SHA（d8fe0ef5…）与盘上修前记录（c8813f43…）不符，以盘上为准已在 KIT 注明；印 SHA 一致。已删 freeze-2026-w47-it-fr/。

## 补充通知（2026-11-12 03:43 EST）：it-zh-tw P1 cifre 标题零余量（既有、非回归）
- 来源：tools 评审工人三重实测（TOOLS-MERGE-VERDICT.md 第 13 项）。it-zh-tw P1 cifre 标题真墨余量仅 +0.5px、advance 余量 +0.9px，渲染卡片最右暗列 957；core-it 同框余量 +169.5px，紧是 fan-out 加注所致；字号 +1pt 即溢出 16.5px。
- 处理：重建 it-zh-tw 时先量该标题余量；如已溢出按简报 §4 常规修法（缩短标题或降字号），不当新缺陷类；如未溢出，不动它。

## 2026-11-12 ~09:00 UTC — it-de DONE (round 3 ALL-GREEN)
- Round 2 gates: 5 boxtitle defects + 1 NEW occlusion LINEX (real, crop-verified: P7 divider y=1686 struck through 'VOL.5.' — gloss reflowed 3→4 lines, box bottom 1673→1702). Fixes: P1 box tsize 23→21, P2 box 23→20.5, P4 21→19.5, P7a 23→20.5, P7b 23→22.5, gloss content7.py:100/:106 20→19.5 (box back to 1673).
- Round 3: TOTAL 150, 0 warnings; gates ALL-GREEN (occlusion 0; p8 CLEAN keydiff [137,138,139]; census 0/0/0; boxtitle 0; spill 0; creambox PASS 0; edge 0/0; freeze 8/8; new CJK only U+3000×13; text layers equal 44,743 chars; text.md unchanged; census_quotes 0).
- Deliverables: print 36595214… 13,499,365 B; web e92b6b99… 1,218,125 B; text.md de0aa214… 56,662 B unchanged. KIT §15 added. freeze dir deleted. Installer route (apply_variant.py).

## 2026-11-12 ~09:20 UTC — it-nl DONE (round 3 ALL-GREEN)
- Pre-census: D5 Latin 503, curly 2 (Newsreader). Install mode latin, fix2 already present (md5 59d44590), routing 0 failures. Round 1: 1 HEAD TOO WIDE (P6 →23).
- Round 2 gates: 5 boxtitle defects (P1 CIJFERS +30.6, P1 INHOUD +4.2, P2 LEUS +16.3, P4 +16.8, P7 WOORD VAN DE WEEK +44.5); occlusion 0. Fixes: P1 box 23→21, sommario 24→23.5, P2 box 23→21.5, P4 21→19.5, P7b 23→20.5.
- Round 3: TOTAL 150, 0 warnings; gates ALL-GREEN (occlusion 0; p8 CLEAN keydiff [137,138,139]; census 0/0/0; boxtitle 0; spill 0; creambox PASS 0; edge 0/0; freeze 8/8; new CJK only U+3000×8; text layers equal 44,618 chars; text.md unchanged; census_quotes 0).
- Deliverables: print cbd50234… 13,495,361 B; web 35a4070d… 1,214,079 B; text.md b13ef7a7… 55,488 B unchanged. KIT §14 added. freeze dir deleted. Installer route.

## 2026-11-12 ~09:32 UTC — 紧急纠正通知自查（nl 家 build-copy 事故）
- 自查方法：对已完成 6 版 + 进行中 it-pt，直接在生产目录验印/网 PDF SHA、svglib.py 的 _D5_READER 出现次数、KIT 含新 SHA。
- 结果：全部在生产原地重建，无 build-copy 同步问题——core-it f867980a/aceaf105、it-en 6f0bbf40/da29562d、it-es 5c703a66/f602876a、it-fr 02e2b67c/1b26c4d5、it-de 36595214/e92b6b99、it-nl cbd50234/35a4070d，生产 SHA 与报告逐一相符；每版生产 svglib.py 均含 _D5_READER（各 5 处）；KIT 各含新印 SHA。it-pt 第 2 轮生产 PDF c8f5d0d2/c4a8614a 与报告相符，门禁待重跑。

## 2026-11-12 ~09:45 UTC — it-pt DONE (round 3 ALL-GREEN)
- Pre-census: D5 Latin 493, curly 0. svglib pre-fix2 (05e25a02); installer added fix2 + D5, routing 0 failures. Round 1: 2 HEAD TOO WIDE (P1 + P6, both →23).
- Round 2 gates: 4 boxtitle defects (P1 DADOS +16.6, P2 LEMA +26.3, P4 +16.8, P7 PALAVRA DA SEMANA +42.5); occlusion 0. Fixes: P1 box 23→21.5, P2 box 23→21, P4 21→19.5, P7b 23→20.5.
- Round 3: TOTAL 150, 0 warnings; gates ALL-GREEN (occlusion 0; p8 CLEAN keydiff [137,138,139]; census 0/0/0; boxtitle 0; spill 0; creambox PASS 0; edge 0/0; freeze 8/8; new CJK only U+3000; text layers equal 44,253 chars; text.md unchanged; census_quotes 0).
- Deliverables: print 30749b8d… 13,500,354 B; web ddb897ef… 1,219,136 B; text.md e01360ae… 55,718 B unchanged. KIT §13 added; noted KIT §12 SHAs (9910d536/f2e390f3) already stale vs disk record (724aa399/bb4c77c9), disk authoritative. freeze dir deleted. Installer route.
- Production self-check per coordinator correction notice: all 7 finished editions verified in place (production PDF SHAs = reported SHAs; production svglib.py each contains _D5_READER ×5; KIT contains new print SHA). No build-copy editions in this family.

## 2026-11-12 ~10:10 UTC — it-ru DONE (round 2 ALL-GREEN)
- Pre-census: D5 Latin 379, Cyrillic 0 in CJK (717 Noto Sans elements), curly 0. Install mode ru (removed pre-D5 Cyrillic lines, added fix2 + D5), routing 0 failures. Round 1: 0 HEAD TOO WIDE.
- Round 1 gates: 1 boxtitle defect (P1 НЕДЕЛЯ В ЦИФРАХ +113.5) + 1 creambox spill flag (P2 'по-итальянски в редакцию.'). Spill = TOOL FALSE POSITIVE, verified: whole E TU box moved down 20.15px (base bottom 1379.6 → patched 1399.75), line inside with identical 5.6px clearance, crop-verified. Root cause: d5_creambox_audit.py compared patched line vs BASE box bottom. Fixed the audit in BOTH copies (mechanism copy that gates.sh runs + promoted tools/ copy): spill now compares vs PATCHED box bottom. First fix landed in the wrong copy (tools/ only) — gates still failed; then fixed the mechanism copy and re-ran gates: flag cleared.
- Title fix: subtitle НЕДЕЛЯ В ЦИФРАХ → В ЦИФРАХ (cf. es/de/nl/pt short forms), tsize 23→22 (full title would need 17.5pt).
- Round 2: TOTAL 150, 0 warnings; gates ALL-GREEN (occlusion 0; p8 CLEAN keydiff [137,138,139]; census 0/0/0; boxtitle 0; spill 0; creambox PASS 0; edge 0/0; freeze 8/8; new CJK only U+3000; text layers equal 44,267 chars; text.md unchanged; census_quotes 0).
- Deliverables: print ead7a5ee… 13,752,905 B; web f3272028… 1,465,974 B; text.md 47c04715… 67,731 B unchanged. KIT §16 added. freeze dir deleted. Installer route.
- Latin/Russian family COMPLETE: core-it + it-en/es/fr/de/nl/pt/ru all ALL-GREEN, KIT synced, production verified in place. CJK next: it-ja, it-ko, it-zh-tw.

## 2026-11-12 ~10:40 UTC — it-ja 基线事故（已定位、可恢复）
- CJK 版无预建基线：baselines/ 与 backups/ 只有 Latin/Russian 7 版 + core-it。it-ja 重建前基线取自 refanout 备份 svglib（md5 7f57a4d1，与安装前实测一致）+ 生产 content（D-2 已合入）。
- 失误：把生产版拷到 scratch 跑 run.py/render.py 重建基线——两脚本的 BASE/OUT 是硬编码的生产路径，scratch 运行直接把生产 svg/ + 印 PDF + cards/ 写回了前 D5 状态（印 PDF SHA 变回 640a355a…）。网 PDF（cd6f6904…）与 text.md（5ac2ecf5…）未动。
- 挽回：前 D5 SVG 经印 PDF SHA 640a355a… 逐字节验证为真基线，已拷入 baselines/2026-w47-it-ja/svg/（+ 前 D5 svglib.py）；前 D5 SHA 已补入 pre-rebuild-sha.txt。随后在生产原地重跑 D5 恢复第 2 轮状态。教训：run.py/render.py 永远只在生产目录里跑，绝不在副本里跑。

## 2026-11-12 ~11:00 UTC — it-ja DONE (round 3 ALL-GREEN) — CJK 1/3
- Pre-census: D5 Latin 344, curly 0. Install mode cjk (fix2 added, CJK index already JP), routing 0 failures. Round 1: 1 HEAD TOO WIDE (P6 →23).
- Baseline: none existed for CJK. Reconstructed from refanout-backup svglib (md5 7f57a4d1) + production content; rebuilt print PDF SHA matched pre-D5 640a355a… byte-exactly. BUT run.py/render.py hardcode production paths — the scratch copy run overwrote production svg/print/cards with the pre-D5 build; restored by re-running D5 in place (print reproduced e4d57184… byte-identically). Baseline saved baselines/2026-w47-it-ja/ (svg + svglib + assets; creambox audit needs assets/ for the moth SVG or it crashes).
- Round 2 gates: 4 boxtitle defects (P1 数字で見る今週 +88.6, P1 今号の内容 +14.2, P2 覚えておこう +86.3, P4 +16.8); occlusion 0. Fixes (full JP text kept): P1 box 23→18.5, sommario 24→22.5, P2 box 23→18.5, P4 21→19.5.
- Gate calibration: freeze-diff vs core-it flagged the whole JP reader layer (3054 CJK chars) — wrong reference for CJK readers. gates.sh now takes an optional freeze-ref dir; CJK editions use their own pre-D5 baseline (same-slug before/after per freeze.py docstring). Re-gated: new-CJK-non-U3000 NONE.
- Round 3: TOTAL 150, 0 warnings; gates ALL-GREEN (occlusion 0; p8 CLEAN keydiff [137,138,139]; census 0/0/0; boxtitle 0; spill 0; creambox PASS 0; edge 0/0; freeze 8/8; freeze-diff vs baseline new CJK only U+3000; text layers equal 38,967 chars; text.md unchanged; census_quotes 0).
- Deliverables: print 52ed1322… 21,050,074 B; web 4f256d24… 1,697,194 B; text.md 5ac2ecf5… 58,165 B unchanged. KIT §13 added; noted KIT §12 web SHA (4f1bac2c…) already stale vs disk record (635856e8…), disk authoritative. freeze dir deleted. Installer route for D5 (JP base handwritten).

## 2026-11-12 ~11:15 UTC — it-ko DONE (round 3 ALL-GREEN) — CJK 2/3
- Baseline taken BEFORE install (production still pre-D5): svg + svglib + assets → baselines/2026-w47-it-ko/; pre-D5 SHAs → pre-rebuild-sha.txt. Pre-census: D5 Latin 343, curly_total 4 (2 Newsreader, 1 CJK KR = P1 "la vetta" quote, NOT a defect per CJK-DECISION §3). Install mode cjk (fix2 added, CJK index already KR), routing 0 failures. Round 1: 1 HEAD TOO WIDE (P6 →23).
- Round 2 gates: 4 boxtitle defects (P1 +38.5, P1 목차 +15.7, P2 +13.3, P4 +16.8); occlusion 0; freeze-diff vs baseline NONE; text-layer multiset_diff=1 (1 extra '\n' in print, sorted lines identical except one blank line — pdftotext artifact around the letter-spaced masthead). Fixes: P1 box subtitle → '숫자로 보는', tsize 23→20.5; sommario 24→22.5; P2 box subtitle → '기억해', tsize 23→22; P4 21→19.5.
- Gate calibration: gates.sh text-layer verdict now compares NON-WHITESPACE multisets (multiset_diff still printed). Freeze ran 8/8 under venv — no Pillow-10 exception needed (build ran under venv; the ko Pillow-10 concern is the core-ko family, not this edition).
- Round 3: TOTAL 150, 0 warnings; gates ALL-GREEN (occlusion 0; p8 CLEAN keydiff [137,138,139]; census 0/0/0, curly 4 all in Newsreader; boxtitle 0; spill 0; creambox PASS 0; edge 0/0; freeze 8/8; freeze-diff vs baseline new CJK only U+3000; text layers nonws-equal 39,300/39,299 chars; text.md unchanged; census_quotes 0).
- Deliverables: print 9815a52d… 15,803,764 B; web 35a222e5… 1,484,263 B; text.md d4d0c6c1… 57,326 B unchanged. KIT §13 added; noted KIT §12 web SHA (67bda0ac…) already stale vs disk record (a94090dc…), disk authoritative. freeze dir deleted. Installer route for D5 (KR base handwritten).

## 2026-11-12 ~11:30 UTC — it-zh-tw DONE (round 3 ALL-GREEN) — CJK 3/3, FAMILY COMPLETE
- Baseline taken BEFORE install: svg + svglib + assets → baselines/2026-w47-it-zh-tw/; pre-D5 SHAs → pre-rebuild-sha.txt. Pre-census: D5 Latin 352, curly 4 (all Newsreader). Install mode cjk (fix2 already present), routing 0 failures.
- P1 cifre zero-margin warning handled pre-emptively: pre-D5 margin +0.9px; D5 widens title to 447.1px (−42.6px). Fixed before round 1: tsize 23→20.5, full TC subtitle kept; round-2 gates confirmed no defect on this title.
- Round 1: 1 HEAD TOO WIDE (P6 →23). Round 2 gates: only P4 +16.8; everything else green (occlusion 0, freeze-diff vs baseline NONE, text layers equal, text.md unchanged).
- Round 3: TOTAL 150, 0 warnings; gates ALL-GREEN (occlusion 0; p8 CLEAN keydiff [137,138,139]; census 0/0/0; boxtitle 0; spill 0; creambox PASS 0; edge 0/0; freeze 8/8; freeze-diff vs baseline new CJK only U+3000; text layers equal 37,971 chars; text.md unchanged; census_quotes 0).
- Deliverables: print 78f1e78c… 14,906,567 B; web 4a4a3f58… 1,639,361 B; text.md c18ad203… 52,494 B unchanged. KIT §14 added. freeze dir deleted. Installer route for D5 (TC base handwritten).
- IT FAMILY COMPLETE: core-it + it-en/es/fr/de/nl/pt/ru/ja/ko/zh-tw = 11/11 ALL-GREEN, KIT synced, all production-verified in place.

## 2026-11-12 ~11:35 UTC — FINAL VERIFICATION (all 11 editions, in place)
- Per-edition check (production dir, not build-copy): print/web PDF SHA == reported SHA; svglib.py contains _D5_READER (5 occurrences, it-ru 4); KIT contains the new print SHA. Result: 11/11 OK. No freeze-* dirs remain. Disk 93G/150G.
- IT FAMILY COMPLETE: core-it + it-en/es/fr/de/nl/pt/ru/ja/ko/zh-tw, all ALL-GREEN, all KIT synced. No unfinished items. No commit, no push.
