# D5 de 家庭重建 — 工作日志（工人 ccd7032a-6bc1-2ac7-fc2d-58f3bfcf60b2 续做）

接替：90b6c3e1（2026-11-12 02:31 EST 被运行时重启打断，仅 "restart drain in progress"）；8f441a81（01:59 EST 被 cron 超时打断）。
范围：core-de（= de-zh-cn）+ 7 个 Latin/Russian fan-out（de-en/es/fr/it/nl/pt/ru）。CJK（de-ja/ko/zh-tw）不动——CJK-DECISION.md 已落地（script-based，mode=cjk），等协调员另派。
解释器：全程 `tools/venv/bin/python`。不 commit、不 push、不跑 lint --write。

## 接手时核实（2026-11-12 07:35 UTC 盘上状态）

- core-de D5 已装（svglib.py 含 _D5_READER='latin'，06:21 UTC；routing assert FAILURES: 0）。
- core-de 真实修前 D5 数 = **461**（census-production.json 06:19 UTC，修前 svg）；D5-CENSUS-130 所记 core-de 0 是普查撞上重建窗口、测到修后 svg 所致（其 d5-json/core-de.json 与修后 census-patched.json 逐数一致）。修后 census = 0。
- 三处 D5 新缺陷源修复已在盘上（run2/run3 已含）：content12.py:124 P1-fussball head 25→22pt；content12.py:43 P1 box tsize 21；content34.py:58 P3 词表标题 24→22pt。
- boxtitle（06:42）2 DEFECT + creambox（06:44）FAIL 2 是 run1（修前）输出上的数，run2/run3 后未重跑——须重跑确认。
- 网 PDF stale：06:58 run2 版（1,854,898 B，sha 97055e34…）；07:30 webpdf3 被打断，未写出（日志无 WROTE 行）。印 PDF 为 07:28 run3 版（11,769,608 B，sha 1244cfdd…）。
- KIT 未同步：仍为 build15（2026-11-11）数值（印 22,965,197 B / sha 49beffc4…；网 2,044,855 B / sha 9b63b413…）。
- 7 fan-out 均未装 D5（D5=0）；de-en svglib 已含 fix2（md5 4d95c2fb），其余 6 份 svglib 相同（md5 f1fc8c3a）且无 fix2。

## core-de

## core-de — DONE 2026-11-12 ~07:50 UTC

- 印 PDF `Die-Lucerna-VOL4-de.pdf` 11,769,608 B sha256 `1244cfdd3d3c…`（07:28 run3 版，未动）；网 PDF 已重建 07:45 UTC：1,854,893 B sha `5a8bdca420cf…`，50,386 text bytes（07:30 那次被打断未写出，旧网 PDF 为 06:58 run2 版 stale）。
- 全套门禁（本次重跑，scratch `scratch-d5-de/core-de/`）：run TOTAL 150 / HEAD TOO WIDE 0（head_check PASS）；D5 census PASS 0/0，quotes 缺陷 0（33 弯引号全在 Newsreader）；occlusion 0 flags；p8 extract 150/150，compare vs 修前基线 CLEAN；freeze baseline 8/8 byte-identical，diff added CJK 0；spill 0 SPILL；boxtitle 0 DEFECT（1 marginal P7 工具箱 +1.0px）；edge 0 TOUCH 0 NEAR；creambox PASS 0 defects（P8 223→222 行，余量 36.8px 不变）；印/网文字层 default 50,386 B、raw 49,377 B，词多重集相同、正规化文本完全相同。
- 三处 D5 缺陷源修复已在 run3 内（上一任所做，本次门禁证实已清）：P1 head 25→22pt、P1 box tsize 21、P3 词表标题 24→22pt。
- KIT 已同步：build16 数值（印/网 SHA+大小）+ §6b D5 门禁轮 + §7 D5 条目。`.text.md` SHA 不变（0952bc51…，内容未动）。
- 修前 D5 真实值 461（不是普查所记 0——普查撞上重建窗口测到修后 svg；已记入 KIT §6b）。
- freeze build 副本已删（27M），只留日志 + JSON。

## de-en — DONE 2026-11-12 ~08:10 UTC

- 修前基线：D5 637 拉丁，quotes 0，p8 150/150；印 sha c8904dea…（与 KIT 一致），网 sha 06030c9a…（与 KIT 所记 2c190c75… 不符——rebuild-6 网 PDF 重建后未同步 KIT，已记入 KIT §6b）。
- D5 安装：apply_variant --reader en（mode latin），routing assert 0 failures（fix2 保留）。
- run1 缺陷 8 项：HEAD TOO WIDE P1-fussball；boxtitle 6 DEFECT（P1 Numbers +13.8、P1 In this issue +27.5、P2 A quiet week +26.1、P3 Words +1.9、P5 Advent words +30.4、P7 Toolbox +23.0）；occlusion COVER 1（P4 gloss 3 行，sentences! 被表带盖 51%）。
- 修复：P1 head 25→22；P1 box tsize 22；sommaire/P2/P3/P5 标题 24→22；P7 Toolbox 23→21（22 仍超 4.2px）；P4 英文 gloss 删 "German" 一词改回 2 行（唯一文案改动；text.md 重导出，diff 恰一行 455）。
- run3 全过：TOTAL 150；census 0；occlusion 0；p8 CLEAN keydiff [137,138,139,150]；freeze 8/8，added CJK 0；spill 0；boxtitle 0 DEFECT（检出 46 标题；P7 21pt 标题低于检测下限，由 creambox + 直接量度验证，余量 14.2px）；edge 0；creambox PASS（P8 231→229 行，余量 33.6px）；印/网文字层 default 50,295 B 完全相同。
- 印 PDF 10,349,936 B sha ad95457c…；网 PDF 1,509,978 B sha 3be4943e…；text.md 49,658 B sha e0947980…。KIT 已同步（§5/§6b/§7）。freeze 副本已删。
- 经验：修标题优先 22pt（保 boxtitle 检测覆盖），22 不够才用 21pt；凡改 gloss 文案必重导出 text.md 并 diff 核对。

## de-es — DONE 2026-11-12 ~08:45 UTC

- 修前基线：D5 636 拉丁，quotes 0；印/网 SHA 与 KIT rebuild-6 记录一致（无 wave-2 差异）。
- D5 安装：apply_variant --reader es（mode latin），routing assert 0 failures。
- run1 缺陷 5 项：HEAD TOO WIDE ×2（P1-fussball；P8-battery `A　LÜCKENTEXT　Texto con huecos` 450.9px）；occlusion TEXTX ×1（P1 46pt 大标题与副标 `VUELVE LA BUNDESLIGA` 重叠 14.5×20.8px，en-fr 试点同类）；boxtitle 2 DEFECT（P1 En cifras +10.8、P3 Palabras +25.9）；creambox FAIL 2（同 2 项）。
- 修复：P1 head 25→22；副标 27→24（标题不动，留 26.2px 间隙）；P1 box tsize 22；P3 24→22；P8 battery 24→22。无文案改动。
- run2 全过：TOTAL 150；census 0；occlusion 0；p8 CLEAN keydiff [137,138,139,150]；freeze 8/8，added CJK 0；spill 0；boxtitle 0 DEFECT（48 标题，真 backup 对照）；edge 0；creambox PASS（P8 230→230 行，余量 33.6→32.6px）；印/网文字层 default 50,873 B、raw 49,805 B，完全相同。
- 印 PDF 10,354,187 B sha 93ad64f8…；网 PDF 1,514,229 B sha 3feadde5…；text.md 不变 sha 5f5ea69b…。KIT 已同步（§5/§6b/§7）。freeze 副本已删。

## de-fr — DONE 2026-11-12 ~09:20 UTC

- 修前基线：D5 637 拉丁，quotes 0；基线干净验证：baseline 副本 venv 重建 freeze 8/8 与交付 SVG 字节一致。印 SHA 与 KIT 一致（f5e68b46…）；网 SHA 与 KIT 不符（盘上 ae89ba2c… vs KIT 5262bfae…，rebuild-6 网 PDF 重建后未同步 KIT，已记入 KIT §6b）。
- D5 安装：apply_variant --reader fr（mode latin），routing assert 0 failures。D-01 stem 在此版修前已是新版。
- run1 缺陷 6 项：HEAD TOO WIDE ×2（P1-fussball；P8-battery `F　WÖRTER PAAREN　Associations` 444.5px）；occlusion TEXTX ×1（P1 大标题与副标 `RETOUR DE LA BUNDESLIGA` 重叠 66.8×20.8px，全家最宽）；boxtitle 3 DEFECT（P1 En chiffres +32.8、P1 Sommaire +7.5、P2 La semaine +7.1）；creambox FAIL 3（同 3 项）。
- 修复：P1 head 25→22；副标 27→22（留 10.7px 间隙，occlusion 复核 0）；P1 box tsize 21（22 仍超 14.0px）；sommaire/P2 24→22；P8 battery 24→22。无文案改动。
- run2 全过：TOTAL 150；census 0；occlusion 0；p8 CLEAN keydiff [137,138,139,150]；freeze 8/8，added CJK 0；spill 0；boxtitle 0 DEFECT（46 标题，1 marginal P7 Outils +1.0px——core 同值， pre-existing）；edge 0；creambox PASS（P8 233→234 行，余量 33.6px 不变）；印/网文字层 default 50,746 B 完全相同，raw 差恰 1 个空格（früh→ vs früh →，poppler 分组，非空格字符 39,966=39,966，零词字符丢失）。
- 印 PDF 10,352,360 B sha fef16b0b…；网 PDF 1,512,394 B sha e1517185…；text.md 不变 sha 3ef1934a…。KIT 已同步（§5/§6b/§7）。freeze 副本已删。

## de-it — DONE 2026-11-12 ~09:45 UTC

- 修前基线：D5 632 拉丁，quotes 0；基线干净验证：baseline 副本 venv 重建 freeze 8/8。印 SHA 与 KIT 一致（ca802fb8…）；网 SHA 与 KIT 不符（盘上 20321311… vs KIT 09fb2470…，同 de-en/de-fr 类问题，已记入 KIT §6b）。
- D5 安装：apply_variant --reader it（mode latin），routing assert 0 failures。
- run1 缺陷 6 项：HEAD TOO WIDE ×3（P1-fussball；P8-battery A `Testo con buchi` 433.3px、F `Abbinamenti` 450.9px）；occlusion 0（意语副标未撞大标题）；boxtitle 3 DEFECT（P1 Sommario +8.5、P7 Attrezzi +24.0、P7 Ancora una parola +17.6）；creambox FAIL 3（同 3 项）。
- 修复：P1 head 25→22；sommaire 24→22；Attrezzi 23→21；Ancora una parola 22→20（21 仅余 1.3px）；P8 A/F 24→22。无文案改动。
- run2 全过：TOTAL 150；census 0；occlusion 0；p8 CLEAN keydiff [137,138,139,150]；freeze 8/8，added CJK 0；spill 0；boxtitle 0 DEFECT（44 标题，0 marginal——2 个 20/21pt 标题在检测 floor 之下，以 creambox + 直接量度核验）；edge 0；creambox PASS（P8 230→229 行，余量 33.6px 不变）；印/网文字层 default 50,440 B、raw 49,385 B，两模式完全相同。
- 印 PDF 10,348,542 B sha 9316b647…；网 PDF 1,508,579 B sha 348a9389…；text.md 不变 sha 1594ba08…。KIT 已同步（§5/§6b/§7）。freeze 副本已删。

## de-nl — DONE 2026-11-12 ~10:15 UTC

- 修前基线：D5 636 拉丁，quotes 0；基线干净验证：baseline 副本 venv 重建 freeze 8/8。印 SHA 与 KIT 一致（55489de1…）；网 SHA 与 KIT 不符（盘上 56aeb8cd… vs KIT 4ed5b46e…，同类问题，已记入 KIT §6b）。
- D5 安装：apply_variant --reader nl（mode latin），routing assert 0 failures。
- run1 缺陷 6 项：HEAD TOO WIDE ×2（P1-fussball；P8-battery F `Combineren` 440.9px）；occlusion 0；boxtitle 4 DEFECT（P1 In cijfers +9.8、P1 In dit nummer +19.5、P2 Stille week +3.1、P7 Werktuig +39.0——全家最宽盒标题超限）；creambox FAIL 4（同 4 项）。
- 修复：P1 head 25→22；P1 box tsize 22；sommaire 22→20（21 仍超 0.6px；fix2 的 24→22 在 CJK Sans 下成立、Newsreader 下失效）；P2 24→22；Werktuig 23→20（21 仍超 0.3px）；P8 F 24→22。无文案改动。
- run2 全过：TOTAL 150；census 0；occlusion 0；p8 CLEAN keydiff [137,138,139,150]；freeze 8/8，added CJK 0；spill 0；boxtitle 0 DEFECT（44 标题，0 marginal——2 个 20pt 标题在检测 floor 之下，以 creambox + 直接量度核验）；edge 0；creambox PASS（P8 230→228 行，余量 33.6px 不变）；印/网文字层 default 50,067 B、raw 48,995 B，两模式完全相同。
- 印 PDF 10,347,054 B sha 0ca4821b…；网 PDF 1,507,082 B sha 0c9e0755…；text.md 不变 sha e904fb3d…。KIT 已同步（§5/§6b/§7）。freeze 副本已删。

## de-pt — DONE 2026-11-12 ~10:45 UTC

- 修前基线：D5 631 拉丁，quotes 0；基线干净验证：baseline 副本 venv 重建 freeze 8/8。印 SHA 与 KIT 一致（bfdc6e8f…）；网 SHA 与 KIT §5 不符（盘上 e723f2cb… vs §5 记录 e48265d3…；§7 Rebuild 5 节记的是正确值 e723f2cb…——§5 未同步，同类问题，已记入 KIT §6b）。
- D5 安装：apply_variant --reader pt（mode latin），routing assert 0 failures。
- run1 缺陷 8 项：HEAD TOO WIDE ×3（P1-fussball；P8-battery A `Preenchimento` 430.1px、F `Associações` 435.3px）；occlusion 0；boxtitle 5 DEFECT（P1 Em números +23.2、P3 Palavras +24.9、P7 Material +30.0、P7 Cartas +3.2、P7 Mais uma palavra +11.6）；creambox FAIL 5（同 5 项）。
- 修复：P1 head 25→22；P1 box tsize 21.5→20（21 仍超 13.0px；rebuild-5 的 23→21.5 在 CJK Sans 下成立、Newsreader 下失效）；P3 24→22；Material 23→21；Cartas 23→22；Mais 22→21；P8 A/F 24→22。无文案改动。
- run2 全过：TOTAL 150；census 0；occlusion 0；p8 CLEAN keydiff [137,138,139,150]；freeze 8/8，added CJK 0；spill 0；boxtitle 0 DEFECT（42 标题，0 marginal——3 个 20/21pt 标题在检测 floor 之下，以 creambox + 直接量度核验）；edge 0；creambox PASS（P8 232→227 行，余量 33.6px 不变）；印/网文字层 default 50,566 B、raw 49,495 B，两模式完全相同。
- 印 PDF 10,354,673 B sha b3ad2533…；网 PDF 1,514,691 B sha fb4c17fa…；text.md 不变 sha e2ee96eb…。KIT 已同步（§5/§6b/§7）。freeze 副本已删。

## 自查（2026-11-12 ~12:30 UTC，响应协调员紧急纠正通知）

- 通知所述 nl 工人事故（scratch build-copy 重建、未同步回生产、生产仍旧版）不适用于本家：本家全部 8 版（core-de + de-en/es/fr/it/nl/pt）均为生产目录原地重建（apply_variant、run.py、render.py、webpdf 均在 production/2026-w47/…/ 内执行；freeze 的 build-copy 是工具自带暂存、每次已删；scratch 下 baseline 只是修前快照）。
- 逐版核对生产实际状态（2026-11-12 12:30 UTC 实测）：7 版生产 svglib.py 均含 _D5_READER = "latin"；7 版生产印/网 PDF 共 14 个 SHA 与本日志报告逐一相符（core-de 1244cfdd…/5a8bdca4…、de-en ad95457c…/3be4943e…、de-es 93ad64f8…/3feadde5…、de-fr fef16b0b…/e1517185…、de-it 9316b647…/348a9389…、de-nl 0ca4821b…/0c9e0755…、de-pt b3ad2533…/fb4c17fa…）；7 版 KIT 均已含 D5 条目。无一版需返工同步。
- 此后每版报完成前仍按通知三项核对（生产印/网 SHA＝报告 SHA；生产 svglib.py 含 _D5_READER；KIT 已按生产实际 SHA 同步）。

## de-ru — DONE 2026-11-12 ~12:45 UTC

- 修前基线：D5 858（拉丁 482 + 西里尔 376），quotes 0；基线干净验证：baseline 副本 venv 重建 freeze 8/8。印 SHA 与 KIT 一致（237d36ae…）；网 SHA 与 KIT 不符（盘上 1a708f26… vs KIT 462f516d…，同类问题，已记入 KIT §6b）。
- D5 安装：apply_variant --reader ru（mode ru）。路由断言注意：复制来的 latin 版断言报 7 失败（_D5_READER==latin、拉丁→news），是断言本身不适用 ru 模式——按 svglib-d5.py 与 CJK-DECISION §2，ru 读者拉丁+西里尔均路由到 sans_noto（Noto Sans Medium 500 / Bold 700），这是 SOP 的 ru 读者规范（core-ru 对齐），不是缺陷。重写 ru 版断言（routing_assert_ru.py）后 ROUTING FAILURES: 0。
- run1 缺陷仅 1 项：occlusion COVER ×1（P4 Und Sie 俄语提示因常规西里尔在 Noto Sans 变宽 +1.8%，由 2 行折成 3 行，末行 `по-немецки!` 被结果表带遮 58%）。HEAD TOO WIDE 0、boxtitle 0 DEFECT（粗体西里尔变窄，48 标题与 3 个 P8 电池头全数 fit）。creambox PASS（P8 226→237 行，+11，与 en-ru 试点一致；余量 33.6px 不变）。
- 修复：P4 提示 20→19.5pt（eh 高度公式与 p.para 两处同改），折回基线的 2 行，P4 col3 止于 1156.02。无文案改动。
- run2 全过：TOTAL 150；census 0；occlusion 0；p8 extract 150/150，compare CLEAN keydiff [137,138,139,150]；freeze 8/8，added CJK 0；spill 0；boxtitle 0 DEFECT（48 标题，0 marginal）；edge 0；creambox PASS（n=556 median 0.999 bold 0.956/reg 1.018——ru 符号翻转）；印/网文字层 default 57,469 B、raw 56,407 B，两模式完全相同。en-ru 试点的 P8 键行互撞在此版未出现。
- 印 PDF 10,623,285 B sha 97941203…；网 PDF 1,769,729 B sha c0c23601…；text.md 不变 sha dee6697b…。KIT 已同步（§5/§6b/§7）。freeze 副本已删。
- Latin/Russian 读者版 7/7 全部完成（core-de + de-en/es/fr/it/nl/pt/ru）。

## de-ja — DONE 2026-11-12 ~13:20 UTC [CJK]

- 修前基线：D5 474 拉丁，quotes 0；基线干净验证：baseline 副本 venv 重建 freeze 8/8。印 SHA 与 KIT 一致（2638a6e6…）；网 SHA 与 KIT 不符（盘上 a4bbff2b… vs KIT 161f2dd0…，同类问题，已记入 KIT §3b）。
- D5 安装：apply_variant --reader ja（mode cjk；CJK index already JP——生产已做 SC→JP 改写，无 kinsoku 动作），routing assert 0 failures（cjk 适配版：_D5_READER=="cjk"，拉丁→news）。
- run1 缺陷 4 项：HEAD TOO WIDE ×1（仅 P1-fussball）；occlusion 0；boxtitle 3 DEFECT（P1 今号の内容 +7.5、P2 静かな一週間 +19.1、P5 待降節の言葉 +11.4）；creambox FAIL 3（同 3 项）。P1 盒标题与 P8 电池头均 fit。
- 修复：P1 head 25→22；3 标题 24→22。无文案改动。
- 过程教训：run2 与 4 处源码编辑同批发出，run2 跑了旧源（P2 标题仍 24pt，boxtitle/creambox 各剩 1 项）；重跑 run3 后 P2 标题 22pt、全门禁绿。run2 日志留作 run2-stale.log。今后编辑与重建分开发。
- run3 全过：TOTAL 150；census 0；occlusion 0；p8 CLEAN keydiff [137,138,139,150]；freeze 8/8，added CJK 0（added Latin 467——CJK 标题按文字分 run 拆分较多）；spill 0；boxtitle 0 DEFECT（52 标题，1 marginal P7 道具箱 +1.0px——core 同值，pre-existing）；edge 0；creambox PASS（P8 234→232 行，余量 33.6px 不变）；印/网文字层 default 52,775 B、raw 51,704 B，两模式完全相同。
- 印 PDF 15,963,826 B sha 03c71417…（原 23.9 MB：拉丁层脱离 CJK 面后内嵌字形子集大减）；网 PDF 1,935,168 B sha c460c72c…；text.md 不变 sha a59f7847…。KIT 已同步（§2/§3b/§6）。freeze 副本已删。

## de-ko — DONE 2026-11-12 ~13:45 UTC [CJK]

- 修前基线：D5 463 拉丁，quotes 0；基线干净验证：baseline 副本 venv 重建 freeze 8/8。印/网 SHA 与 KIT 均一致（5e34f31a…/d77adb82…）——继 de-es 之后第二版无网 SHA 漂移。
- D5 安装：apply_variant --reader ko（mode cjk；CJK index SC -> KR——安装器改写了 CJK 子字体；de-ja 则是 already JP），routing assert 0 failures（cjk 适配版）。
- run1 缺陷 4 项：HEAD TOO WIDE ×1（仅 P1-fussball）；occlusion 0；boxtitle 3 DEFECT（P1 이번 호 내용 +9.0、P3 크리스마스 +34.9——CJK 标题最宽超限、P7 도구 상자 +21.7）；creambox FAIL 3（同 3 项）。量度注意：boxtitle 旗标只给尾巴 run（내용/크리스마스/상자），须以完整标题实测——P1 全标题为 "IN DIESER AUSGABE　이번 호 내용"、P7 为 "DER WERKZEUGKASTEN　도구 상자"。
- 修复：P1 head 25→22；sommaire 24→22；P3 24→21（22 仅余 1.0px）；工具箱 23→21（22 仍超 3.7px）。无文案改动。编辑与重建分开发（de-ja 教训）。
- run2 全过：TOTAL 150；census 0；occlusion 0；p8 CLEAN keydiff [137,138,139,150]；freeze 8/8（venv 下直接通过，简报预警的 ko freeze ABORT 未触发，系统 python3 例外未用上），added CJK 0（added Latin 463）；spill 0；boxtitle 0 DEFECT（65 标题，0 marginal——2 个 21pt 标题在检测 floor 之下，以 creambox + 直接量度核验）；edge 0；creambox PASS（P8 232→233 行，余量 34.6px 不变）；印/网文字层 default 52,246 B、raw 51,160 B，两模式完全相同。
- 印 PDF 12,889,807 B sha 559a59cd…（原 15.9 MB）；网 PDF 1,789,607 B sha c63dbb54…；text.md 不变 sha fd2dbd04…。KIT 已同步（§2/§3b/§6）。freeze 副本已删。

## de-zh-tw — DONE 2026-11-12 ~14:15 UTC [CJK]

- 修前基线：D5 463 拉丁，quotes 0；基线干净验证：baseline 副本 venv 重建 freeze 8/8。印 SHA 与 KIT 一致（74faeb9d…）；网 SHA 与 KIT 不符（盘上 b4b82c51… vs KIT 352ead22…，同类问题，已记入 KIT §3b）。
- D5 安装：apply_variant --reader zh-tw（mode cjk；CJK TC 子字体），routing assert 0 failures（cjk 适配版）。
- run1 缺陷 2 项：HEAD TOO WIDE ×1（仅 P1-fussball）；occlusion 0；boxtitle 1 DEFECT（P1 數字看本週 +25.8）；creambox FAIL 1（同项）。P1 盒标题与 P8 电池头均 fit，是 de 家 CJK 三版中缺陷最少的一版。
- 修复：P1 head 25→22；P1 盒 tsize 23→21（22 仍超 7.0px；tsize 21 在 boxtitle 检测 floor 之下，以 creambox + 直接量度核验，392.8/404.5 余 11.7px）。无文案改动。编辑与重建分开发。
- run2 全过：TOTAL 150；census 0；occlusion 0；p8 CLEAN keydiff [137,138,139,150]；freeze 8/8，added CJK 0（added Latin 466）；spill 0；boxtitle 0 DEFECT（48 标题，1 marginal P7 工具箱 +1.0px——core 同值，pre-existing）；edge 0；creambox PASS（P8 232→233 行，余量 34.6→33.6px）；印/网文字层 default 49,821 B、raw 48,759 B，两模式完全相同。
- 印 PDF 11,838,985 B sha d51a66c6…（原 23.0 MB）；网 PDF 1,936,641 B sha 48edfb95…；text.md 不变 sha fe62ddb5…。KIT 已同步（§2/§3b/§9）。freeze 副本已删。

## 家族验收（2026-11-12 ~14:20 UTC）

- 11/11 版完成：core-de + de-en/es/fr/it/nl/pt/ru + de-ja/ko/zh-tw。全原地在生产目录重建。
- 三项验收逐版核对通过：生产印/网 PDF SHA = KIT 记录的 D5 值（逐版核对 11 版，全部一致）；生产 svglib.py 各含 _D5_READER 5 处；KIT 均已按生产实际 SHA 同步（§2/§3b/§6 或 §9）。
- 磁盘：93G 已用 / 150G（57G 空闲），未触 100G 门限。freeze 副本每版后已删。
- 未完成项：无。独立重校（SOP §8.4）由协调员另派。
