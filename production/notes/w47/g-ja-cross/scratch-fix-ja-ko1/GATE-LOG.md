# GATE-LOG — W47 ja-ko fix1 返修后门禁重跑记录

返修员 fix1；2026-11-11 UTC。工具：`~/workspace/weekly-git/tools/venv/bin/python`。
返修后成品目录：`~/workspace/weekly-git/production/2026-w47/fanout-ja/2026-w47-ja-ko/`。
本目录证据：`build-ko-fix1-run1/2.log`、`ko-sha-fix1-run1/2.txt`、`render-ko-fix1.log`、
`webpdf-ko-fix1.log`、`ko-occlusion-fix1.json/log`、`ko-p8-fix1.json/log`、
`ko-p8compare-fix1.json/log`、`scan1.txt`、`apply-ko-fix1(b).log`。

## 探针
- PROBE1：`git hash-object -w --stdin` → `da0c4eb8…`，OK。
- PROBE2：笔记目录写 `probe.txt`，OK。`df`：/home/hatch 45G 可用。全程仅在写
  EDITION-RECORD 时遇一次 EDQUOT（见 FIX-LOG §6；删本目录 4 份可复现 pdftotext
  中间件后重试一次即成功，未动他处）。

## 成品核实（fix1 新值）
- print `Lucerna-VOL4-JA-KO.pdf`：28,189,450 B，sha256
  `8c6b7566e6efe7d94beae5bf10b6382970a93b3b71708688d3d27dbb7f39f177`，8 页。
- web `Lucerna-VOL4-JA-KO-web.pdf`：4,550,444 B（< 7 MB），sha256
  `133f57264a824575af7336c6e1198c4992211fa45bf8c82d96dfd89e840f3368`，8 页。
- `2026-w47-ja-ko.text.md` 47,722 B（1329 text 行 / 1356 文件行）；`ABSTRACT.txt` 296 B；
  `WEEKLY-KIT.md` 12,408 B（§8 更新 + §11 F2 所致）。

## 门 1 — run.py（freeze，两次直跑）
- run1：exit 0；`FLOW OVERFLOW`/`HEAD TOO WIDE` 0 条；`TOTAL 150`；by level A2 48 / B1 73 / B2 29；
  by page 10/18/18/18/18/18/12/38；by type 빈칸 채우기 50 / 객관식 51 / 연결하기 12 / 문장 만들기 8 /
  참·거짓 11 / 빈칸 객관식 13 / 번역 4 / 작문 1；model chars 154。日志 `build-ko-fix1-run1.log`。
- run2：exit 0，0 溢出；`build-ko-fix1-run2.log`。
- freeze：`ko-sha-fix1-run1.txt` vs `ko-sha-fix1-run2.txt` diff 空 → **8/8 相同**。
- 交付比对：新 SHA vs proof1 `proof-sha-delivered.txt`：仅 p5、p8 两页变化，
  p1/p2/p3/p4/p6/p7 **逐字节一致**（变化面恰为 D3 与 D1/D2/#47 所在页）。

## 门 2 — occlusion_audit.py（新 SVG 目录）
- 命令：`tools/occlusion_audit.py --json ko-occlusion-fix1.json <edition>/svg`
- exit 0；日志：`selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent`
  + `<svgdir>: 0 flags`。JSON：`flag_count: 0`，`flags: []`。→ **0 flags**。

## 门 3 — p8.py
- extract：`tools/p8.py extract --p8 <edition>/svg/p8-tesuto.svg --total 150 --json ko-p8-fix1.json`，
  exit 0；`noted set = 150 of 150`，编号 1–150 连续无缺重。→ **150/150**。
- compare：`tools/p8.py compare --core-p8 <core>/svg/p8-tesuto.svg --edition-p8 <edition>/svg/p8-tesuto.svg --total 150 --json ko-p8compare-fix1.json`，
  exit 0；`status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 140]`。
- 注：compare 只比对键值，不覆盖注文 prose；prose 修复处（#47/#49/#54/#63/#80/#111/#116
  + D3 框）已逐项核对 text.md 行与 SVG 文本，见门 6/门 7。

## 门 4 — 文字层一致
- `pdftotext`（plain）：print 47,998 B、web 47,998 B，`cmp` 逐字节一致。
- `pdftotext -layout`：print 91,550 B、web 91,550 B，`cmp` 逐字节一致。
  （4 份提取文本在 EDQUOT 应急中已删，可由双 PDF 重提；字节数与一致性结论记于此。）
- P8 最小字号（PyMuPDF，print PDF p.8）：9.975pt；次档 10.35pt（题干）。

## 门 5 — text.md 导出一致
- `export-textmd-ko.py` 重跑：`wrote 2026-w47-ja-ko.text.md 47722 bytes; 1329 text lines`；
  前后 sha256 皆为 `b20d5bc6…` → **逐字节一致**。
  （行数由 1330→1329：D3 把 P5 框韩译由 3 行并为 2 行，少一行文本行，文件行 1357→1356。）

## 门 6 — 专项扫描（证据 `scan1.txt`；8 SVG + 9 py + text.md + ABSTRACT.txt + 双 PDF 文字层）
- `후지류가` **0**；`후지료가` 25（content 5 + text.md 5 + P8 SVG 5 + 双 PDF 文字层各 5）。
- `기하라 류치` **0**；`기하라 류이치` 5（content56 1 + text.md 1 + P8 SVG 1 + 双 PDF 文字层各 1）。
- 弯引号/弯撇 U+201C/U+201D/U+2019/U+2018：**全 0**。
- 中文残留：`吉伊卡哇`/`参考答案`/`酉之市`/`提名` **0**；#47 中文原文
  `首日战胜大之里的是义之富士` 与错键 `首日战胜大之里的是一之富士` **皆 0**；
  #47 韩文 `요시노후지는 1일째에 오노사토를 이겼어요` 5 处（content34 1 + text.md 1 + P8 SVG 1 + 双 PDF 文字层各 1）。
- `우미노우미` 5 处（正确，未动）；`치이카와` / `ryuuryuu` 如裁定；`Fujiryūga` / `Fujiryōga` 0。
- text.md 修复行（新行号）：47 L1245、49 L1247、54 L1252、63 L1261、80 L1279、111 L1313、116 L1319；
  D3 行 L641 `…써서 보내주세요.`。
- §1.1：纸 `#fbfaf6` 1×/页（8×）、旧纸 `#f7f1e2` 0×、`·` 0×、禁金色 0×；刊头 196px；
  页码行 `제 N 면 / 총 8 면` 1×/页；VOL.4 ×10、VOL.5 ×3、VOL.3 ×1（与 proof1 基线一致）。
- 几何实测：P5「あなたは？」框韩译 2 行（基线 y=1473.57/1501.97，无第 3 行孤悬句号），
  P5 col3 ends 1506.45（练习区起于 1580）；P7 teaser 末基线 2438.14；P8 答案 4 列末基线
  2514.92 / 2513.42 / 2530.35 / 2350.48（皆 < 2540）；P8 练习流最末基线 1239.37（底线 1252）。

## 门 7 — 目视
- print 卡 p5、p8 全读：P5「あなたは？」框韩译 2 行、句号贴在第 2 行末，无孤悬；
  P8 答案区 #47/#49/#54/#63/#80/#111/#116 皆为修正后韩文，无溢出/重叠/压页脚/豆腐块。
  其余六页 SVG 与 proof1 交付件逐字节一致，不再重读（proof1 目视结论继续有效）。

## 结论
- 机械门：**全部通过**（run 0 溢出、freeze 8/8、occlusion 0、p8 150/150 + CLEAN、文字层一致、text.md 导出一致）。
- 内容：D1/D2/D3 已修 + #47 键错字附带修复完成；待 proof2 从头再做一轮全量校对，零问题方可定稿。
