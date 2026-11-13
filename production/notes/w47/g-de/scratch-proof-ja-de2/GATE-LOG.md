# GATE-LOG — 2026-W47 ja-de 第二轮独立复校（叶子）

日期：2026-11-11。全部机械门由校对员自跑，使用共享工具；解释器一律 `tools/venv/bin/python`（Pillow 13.0.0；系统 python3 为 Pillow 10.2.0，未用于任何门）。

## 0. 开工探针（双通才动手）

- `echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin` → `da0c4eb8d9a48d171a33574b380752e183286751`，RC=0。
- `hidden_files/w47/scratch-proof-ja-de2/.probe` 真实写盘成功。

## 1. 身份复核

- 印刷 `Lucerna-VOL4-JA-DE.pdf`：29,102,625 字节，SHA-256 `2047035bdaa9f9ba82d4f2a6d2b5d7c4461e1442070ed5abacbe86d930001f39` —— 与 KIT §8a 登记逐字一致，与 fix1 称的值一致。
- 网页 `Lucerna-VOL4-JA-DE-web.pdf`：4,483,728 字节，SHA-256 `8db59bf122c73d895e9fe0d58da7e9f283f11ed1e76bc45aeb2be9a268a98f26` —— 与 KIT §8a 登记逐字一致，与 fix1 称的值一致。
- 两 PDF 各 8 页，1462.5 × 2025 pt。
- 原 SVG sha256：p1 `9d35b741564269d125db6a8266af80bf51725d0fd2eea59d75ace885ffee9ca6`；p2 `80f4964c3a188a7af9413e470e8f67ed879565a1496a1d07fa37afa05c5c77d1`；p3 `a42beb0b383714f3ab2b615209070b41cedeae1965726f8993f057cd2abd5085`；p4 `cfeaddb4a98f4323ad8327ffe1ebf5806cd312389fb88517fa2f5662423ecaed`；p5 `ff1ca67b828931677625be57abed8d85fadff8ffdcff4e04d8bfc571410c9c04`；p6 `2ff8500f168bd144e17b42d3d2c97d53ab51c7d54e7ea6567afed994582676fe`；p7 `3493886b3c75364682e2b630b821399750d12344b8e40989654757fa6c4bc505`；p8 `021ed40fe1098cc68805757cdd4bac08445771a84b731c34f04c4df382003cb5`。其中 p1–p6 与第一轮 GATE-LOG 记录逐个一致，p7/p8 与 KIT §8a 登记的新值一致。

## 2. run.py 重跑（exit 0，零溢出）

- 方法：整目录拷贝至 `hidden_files/w47/scratch-proof-ja-de2/rerun/` 后在拷贝中运行（原件未动）；`tools/venv/bin/python run.py`，日志 `rerun-log.txt`。
- 结果：exit 0；`FLOW OVERFLOW` / `HEAD TOO WIDE` 出现 0 次。
- 登记：TOTAL 150；by level A2 48 / B1 73 / B2 29；by page 1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38；by type Ausfüllen 50 / Auswahl 51 / Zuordnen 12 / Satz bilden 8 / Richtig/Falsch 11 / Lückentext 13 / Übersetzen 4 / Schreiben 1；model chars 154——与 KIT §1 一致。
- 几何断言复现：P7 col3 ends 1780.62；P7 teaser ends 2554.62（页脚 2580）；P8-ex ends col 3 y=561（底 1252）；P8-keys ends col 3 y=2382（底 2540）——与 KIT §7/§8a 一致。

## 3. freeze（直接 sha256 比对 8/8）

- 原 `svg/*.svg` vs 重跑 `rerun/svg/*.svg`：`diff` 无差异，**8/8 字节一致**（`sha-orig.txt` vs `sha-rerun.txt`）。
- 局限：与第一轮同——构建方所用解释器无记录（构建日志随 `hidden_files/w47/scratch-fanout-ja/` 缺失）；本次重跑用规范工具 `tools/venv/bin/python`（Pillow 13.0.0）。ko 家庭曾证实 Pillow 版本差可致 freeze 翻转——本版在规范解释器下 8/8 一致；构建方若用了其他 Pillow，本门无法代为背书。

## 4. occlusion 几何审计（0 flags）

- `tools/venv/bin/python tools/occlusion_audit.py production/2026-w47/fanout-ja/2026-w47-ja-de/svg --json hidden_files/w47/scratch-proof-ja-de2/de-occlusion-proof2.json`
- 自检：`selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent`
- 结论：`0 flags`，`flag_count: 0`。

## 5. p8 extract + compare

- `tools/p8.py extract --p8 …/svg/p8-tesuto.svg --total 150` → `noted set = 150 of 150`（`de-p8-proof2.json`）。
- `tools/p8.py compare --core-p8 …/core-ja/svg/p8-tesuto.svg --edition-p8 …/svg/p8-tesuto.svg --total 150` → `status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 140]`（`de-p8compare-proof2.json`）。
- keydiff 4 条键值（自 extract JSON 独立读出）：137 `Ni-no-tori ist am 19. November.`；138 `Der neue Wein erscheint am 19. November.`；139 `Die Schlagwort-Nominierungen wurden am 5. November bekannt gegeben.`；140 `Wer das Herbstlaub sehen will, sollte sowohl die Prognosedaten als auch die aktuelle Lage prüfen.`——与 KIT §7 登记逐字一致，原因均为 E 组答案由中文译成德文（已逐条对照 core 中文原文核实翻译正确）。
- 另核：key 51 提取值为 `C`（SVG 原文 `51. C — Der letzte Tag ist am 22. November (Sonntag)`；100 dpi 渲染图上 C 易误读为 2，已用 SVG 原文核实无误）。

## 6. print/web 文字层一致

- `pdftotext -layout` 两版：各 105,192 字节，`cmp` 字节一致（`print.txt` / `web.txt`）。

## 7. P8 字号（PyMuPDF，tools/venv）

- P8 字号分布（pt）：9.98×162、10.35×79、10.88×6、11.25×5、11.62×1、12.75×5、13.5×2、14.25×37、14.62×12、15.38×3、15.75×16、17.25×4、18.0×39、18.75×2、34.5×3。
- P8 最小 9.98pt（≥9.75pt 门槛；KIT 称 9.975pt，吻合）；题干 10.35pt 不动。
- 各版最小字号：P1 11.62、P2 12.75、P3 11.62、P4 12.75、P5 11.62、P6 12.75、P7 11.62、P8 9.98。

## 8. D1/D2/D3 回归 grep + §1.1 扫描

- 残留 grep（svg + text.md + content*.py）：`Fujiryūga` 0×、`Umi-no-umi` 0×、`im ます-Form` 0×。
- 改后形式：`Fujiryōga` 15×（svg p8 5、text.md 5、content 文件 5）、`Churanoumi` 3×（svg p8 1、text.md 1、content34.py 1）、`in der ます-Form` 3×（svg p7 1、text.md 1、content7.py 1）。
- U+2019：8 个 SVG 合计 0；text.md 0。ASCII 撇号 0×；德文弯引号 „ “ 0×。
- `·`：SVG 0×，text.md 0×。`#f7f1e2` 0×；`#fbfaf6` 每版 1×；`#c9a227`（金）0×。
- `Seite N von 8` 每版 1×；VOL.4：P1 3×、其余每版 1×；VOL.3 1×；VOL.5 3×（core 4×，差 1 处为 core 披露中文译注行的重复计数，见 PROOF-NOTE §3.5）。
- 徽章（本轮独立对 core 计数）：P1 14、P2 15、P3 15、P4 18、P5 18、P6 18、P7 12、P8 35——与 core 逐页完全一致。
- `吉伊卡哇` 0×；`参考答案 / 酉之市 / 提名 / 中文 / 中国 / 练习 / 答案 / 解释 / 单词 / 语法 / 阅读` 在 SVG 与 text.md 中均为 0×；de 引入汉字集合 − core 汉字集合 = 空集。
- `Chiikawa`：svg 4× + text 4×；`ryuuryuu`：svg 5× + text 5×。
- core↔de 全量 diff（`core-de-diff.txt`）：150 个差异块（359 行删、379 行增），全部为讲解层或版式家具；假名逐块核查仅 2 处“丢失”均为正当翻译（P3 图注 `パブリックドメイン`→`gemeinfrei`；P7 披露日文句+中文译注→单条德文披露）。

## 9. 目视

- 印刷 PDF 重新渲染（`pdftoppm -r 100`，`render-print/p-1.png`～`p-8.png`）：8 版逐版目视，无溢出、无重叠、无压页脚；P2 词卡 gloss 单行、P7 诊所第 4 条 `in der ます-Form`、P8 答案区 7 处修复注文均已目视确认。
- 网页 PDF P1/P8（`render-web/w-p1-1.png`、`w-p8-8.png`）：与印刷版同一版式、同一文字，干净。

## 10. 未能执行的核查（资料缺失，非跳过）

- `hidden_files/w47/scratch-fanout-ja/FANOUT-REPORT-ja.md` 不存在（整个 `scratch-fanout-ja/` 目录在 clone 中缺失），其顶部审计节与关键裁定备忘无法阅读；`map-de.json`（221 键）、`apply.py`、构建日志均不可得。
- 替代验证：KIT 全文 + core 全文 diff（150 差异块逐块审读，假名逐块核查）+ 字符集差分 + 全部共享工具自跑。221 键计数采信 KIT §9，以效果验证。
