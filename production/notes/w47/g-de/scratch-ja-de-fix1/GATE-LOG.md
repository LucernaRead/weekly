# GATE-LOG — 2026-W47 ja-de 第一轮返修（fix round 1）

日期：2026-11-11。全部机械门自跑，使用共享工具；解释器一律
`tools/venv/bin/python`（Pillow 13.0.0；与第一轮复校重跑所用解释器相同）。

## 0. 开工探针（双通才动手）

- `echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin` →
  `da0c4eb8d9a48d171a33574b380752e183286751`，RC=0。
- `hidden_files/w47/scratch-ja-de-fix1/.probe`（goals 目录）真实写盘成功。

## 1. 身份复核（修前旧版）

- 印刷 `Lucerna-VOL4-JA-DE.pdf`：29,102,629 字节，SHA-256
  `b5d66e17d9ac29b6362d934e65a254a1bb63df5ea00ed305ce1b362cea06a239` ——
  与任务给定一致。
- 网页 `Lucerna-VOL4-JA-DE-web.pdf`：4,483,732 字节，SHA-256
  `c55dd68cfcd6f0acc4cad79987a7ceb7fbe4c86d83cdf637c86c795497aff26a` ——
  与任务给定一致。
- 旧 SVG sha256 与复校 GATE-LOG §3 记录的 8 个值逐个一致（见
  `old-svg-sha.txt`）；旧版备份在 `old-svg/` 与 `old-pdf/`。

## 2. run.py ×2（exit 0，零溢出；freeze 8/8）

- `tools/venv/bin/python run.py`，日志 `build-fix1-run1.log` / `build-fix1-run2.log`。
- 结果：两次均 exit 0；`FLOW OVERFLOW` / `HEAD TOO WIDE` 出现 0 次。
- 登记：TOTAL 150；by level A2 48 / B1 73 / B2 29；by page 1:10, 2:18, 3:18,
  4:18, 5:18, 6:18, 7:12, 8:38；by type Ausfüllen 50 / Auswahl 51 /
  Zuordnen 12 / Satz bilden 8 / Richtig/Falsch 11 / Lückentext 13 /
  Übersetzen 4 / Schreiben 1——与 KIT §1 一致。
- freeze：run1 vs run2 SVG sha256（`fix1-sha-run1.txt` / `fix1-sha-run2.txt`），
  diff 无差异，**8/8 字节一致**（与构建相同解释器重跑）。
- 新旧 SVG 对比：p1–p6 与旧版字节一致；仅 p7、p8 变化；p7/p8 文本元素 diff
  恰为 7 处目标串（D1 ×5、D2 ×1、D3 ×1），无其他字符差异。
- 几何断言（与修前一致）：P7 col3 ends 1780.62；P7 teaser ends 2554.62
  （页脚 2580）；P8-ex ends col 3 y=561（底 1252）；P8-keys ends col 3
  y=2382（底 2540）。
- 新 SVG sha256：p7 `3493886b3c75364682e2b630b821399750d12344b8e40989654757fa6c4bc505`；
  p8 `021ed40fe1098cc68805757cdd4bac08445771a84b731c34f04c4df382003cb5`；
  p1–p6 与修前相同（见 `old-svg-sha.txt`）。

## 3. render.py + webpdf.py（全 rc 0）

- `tools/venv/bin/python render.py`（日志 `render-fix1.log`）：rc 0；
  8 cards PNG + print PDF。
- `tools/venv/bin/python tools/webpdf.py svg Lucerna-VOL4-JA-DE-web.pdf`
  （日志 `webpdf-fix1.log`）：rc 0；8 pages，596 distinct chars；
  `WROTE Lucerna-VOL4-JA-DE-web.pdf: 4483728 bytes, 46838 text bytes`。
- 新双 PDF（8 页，1462.5 × 2025 pt）：
  - 印刷 `Lucerna-VOL4-JA-DE.pdf`：29,102,625 字节，SHA-256
    `2047035bdaa9f9ba82d4f2a6d2b5d7c4461e1442070ed5abacbe86d930001f39`。
  - 网页 `Lucerna-VOL4-JA-DE-web.pdf`：4,483,728 字节（< 7 MB），SHA-256
    `8db59bf122c73d895e9fe0d58da7e9f283f11ed1e76bc45aeb2be9a268a98f26`。

## 4. occlusion 几何审计（0 flags）

- `tools/venv/bin/python tools/occlusion_audit.py production/2026-w47/fanout-ja/2026-w47-ja-de/svg --json …/de-occlusion-fix1.json`
- 自检：`selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent`
- 结论：`0 flags`，`flag_count: 0`。

## 5. p8 extract + compare

- `tools/p8.py extract --p8 …/svg/p8-tesuto.svg --total 150` →
  `noted set = 150 of 150`（`de-p8-fix1.json`）。
- `tools/p8.py compare --core-p8 …/core-ja/svg/p8-tesuto.svg --edition-p8 …/svg/p8-tesuto.svg --total 150` →
  `status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 140]`
  （`de-p8compare-fix1.json`）。
- 150 键逐题复核（旧 SVG vs 新 SVG 文本元素逐键比对）：150/150 键齐全；
  仅 keys [48, 49, 54, 63, 111, 116] 的简析文本不同（即 D1/D2 的 6 处），
  其余 144 条逐字一致；键值（`—` 之前的答案本身）差异 **0 条**。

## 6. print/web 文字层一致

- `pdftotext -layout` 两版（`print.txt` / `web.txt`）：各 105,192 字节，
  `cmp` 字节一致。（修前 105,188；+4 = D3 `im`→`in der`。）

## 7. P8 字号（PyMuPDF，tools/venv）

- P8 字号分布（pt）：9.98×162、10.35×79、10.88×6、11.25×5、11.62×1、
  12.75×5、13.5×2、14.25×37、14.62×12、15.38×3、15.75×16、17.25×4、
  18.0×39、18.75×2、34.5×3——与修前分布逐项一致。
- P8 最小 9.98pt（≥9.75pt 门槛）；题干 10.35pt 不动。
- 各版最小字号：P1 11.62、P2 12.75、P3 11.62、P4 12.75、P5 11.62、P6 12.75、
  P7 11.62、P8 9.98。

## 8. U+2019 回归 + §1.1 grep 审计

- U+2019：8 个 SVG 合计 0；text.md 0。ASCII 撇号 0×。
- `·`：SVG 0×，text.md 0×。`#f7f1e2` 0×；`#fbfaf6` 每版 1×；
  `#c9a227`（金）0×。`Seite N von 8` 每版 1×。
- 残留复扫（修后）：`Fujiryūga` / `Umi-no-umi` / `im ます-Form` 在
  content*.py + svg + text.md 中均为 0×；新串 `Fujiryōga` ×5、
  `Churanoumi` ×1、`in der ます-Form` ×1，位置与 D1/D2/D3 一一对应。

## 9. 目视

- 印刷 PDF 重新渲染（`pdftoppm -r 100`，`render-print/p-1.png`～`p-8.png`）：
  8 版逐版目视，无溢出、无重叠、无压页脚；P1–P6 与修前一致（SVG 字节一致）。
- 重点放大：P7 右栏裁图（`p7-rightcol.png`）——诊所第 4 条
  `Das Verb in der ます-Form beenden.` 清晰、单行、框内完整；
  P8 答案区裁图（`p8-answers-top.png` / `p8-answers.png`）——
  keys 48/49/54/63/111/116 新拼写逐条确认。
- 网页 PDF 未单独渲染目视（文字层与印刷版逐字节一致；上一轮已目视 P1/P8
  网页版且本次网页版仅由同一 SVG 重建）。

## 10. 未执行项（按任务红线，非跳过）

- 未跑 `insert.py`、`lint --write`；未 git add/commit/push/reset/stash。
- 未改 core-ja、W43–W46、其他目标语家庭、tools/。
- `map-de.json` / `apply.py` / `export-textmd-de.py` 本 clone 中不存在——
  修复直接落在 content*.py，text.md 为 surgical 替换（diff 验证仅 7 行变）；
  map 恢复后须把 7 处写回 map（见 KIT §9 NOTE）。

## 11. 工作文件

- 本目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-ja-de-fix1/`
- FIX-LOG.md、GATE-LOG.md（本文件）、`.probe`、旧版备份 `old-svg/`、`old-pdf/`、
  `old-svg-sha.txt`、`textmd-old.bak`、构建日志 `build-fix1-run1.log` /
  `build-fix1-run2.log`、`render-fix1.log`、`webpdf-fix1.log`、门禁输出
  `de-occlusion-fix1.json`、`occlusion-fix1.log`、`de-p8-fix1.json`、
  `de-p8compare-fix1.json`、`fix1-sha-run1.txt`、`fix1-sha-run2.txt`、
  文字层 `print.txt` / `web.txt`、渲染图 `render-print/`（p-1～p-8、
  p7-rightcol、p8-answers、p8-answers-top）。
