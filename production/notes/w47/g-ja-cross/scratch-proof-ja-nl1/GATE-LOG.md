# GATE-LOG — 2026-W47-ja-nl 第一轮独立复校（叶子，2026-11-11）

## 开工探针（双通，07:41 UTC）

- `echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin` → 成功
  （`da0c4eb8d9a48d171a33574b380752e183286751`）。
- `hidden_files/w47/scratch-proof-ja-nl1/.probe` 真实写盘成功。

## 身份核对（08:00 前）

- 印刷 PDF `Lucerna-VOL4-JA-NL.pdf`：29,099,171 B，
  SHA-256 `c18c551af2249561000dd50821d4e9646597c5a2cdccf316b02ee38128d40a19`——与 KIT 登记逐字一致。
- 网页 PDF `Lucerna-VOL4-JA-NL-web.pdf`：4,476,557 B，
  SHA-256 `e0678a4b892ff07080d48a51b2f8b7c9ee109916752df537849000370ad9cb81`——与 KIT 登记逐字一致。
- 双 PDF 各 8 页。

## 机械门（全套自跑，解释器均为 `tools/venv/bin/python`——与构建同一解释器，KIT §9）

| 门 | 命令 / 方法 | 结果 |
|---|---|---|
| run.py 重跑 #1 | `tools/venv/bin/python run.py`（版目录内） | exit 0；FLOW OVERFLOW 0；HEAD TOO WIDE 0；`P8 saved, TOTAL exercises: 150`；级别 A2 48 / B1 73 / B2 29；分版 10/18/18/18/18/18/12/38；题型 zinnen aanvullen 50 / meerkeuze 51 / combineren 12 / zinnen bouwen 8 / waar of onwaar 11 / gatentekst 13 / vertalen 4 / schrijven 1。日志 `proof-run1.log` |
| run.py 重跑 #2 | 同上 | exit 0；溢出 0；统计与 #1 完全一致。日志 `proof-run2.log` |
| 冻结 | 开工前 / #1 后 / #2 后三组 `sha256sum svg/*.svg` | 8/8 逐字节一致（`svg-sha-pre/run1/run2.txt`，diff 无输出） |
| 几何审计 | `tools/occlusion_audit.py <svgdir> --json proof-occlusion.json` | exit 0；自检 OK（6 类 BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX  planted 对照全触发，干净对照静默）；**0 flags** |
| P8 提取 | `tools/p8.py extract --p8 svg/p8-tesuto.svg --total 150` | exit 0；noted set **150/150**（1–150 全） |
| P8 比对 | `tools/p8.py compare --core-p8 core-ja/svg/p8-tesuto.svg --edition-p8 svg/p8-tesuto.svg --total 150` | exit 0；**CLEAN**；missing=[] extra_count=0 uncertain=[]；keydiff=**[137, 138, 139, 140]**（逐条核实：四条均为预期内 JA→NL 翻译，见 PROOF-NOTE.md） |
| 文字层 | `pdftotext` 印版 vs 网版 + `cmp` | **逐字节一致**，各 45,989 B |
| P8 最小字号 | PyMuPDF 取 P8 全部 span 字号 | **9.975pt**（次档 10.35pt = 题干，冻结值）；≥ SOP §1.1 下限 9.75pt |
| U+2019 | `grep -c` 8 SVG + text.md + content*.py | 全 **0** |
| §1.1 grep | 8 SVG | 纸色 `#fbfaf6` 1×/页；旧 `#f7f1e2` 0；`·` 0；金色 0；刊头 196px；P1 头条 56px = 42pt；页码行 `Pagina N van 8` 1×/页；徽章色 A2 `#5c6e30` / B1 `#46581f` / B2 `#37402f` 齐全（A2 徽章数 P1 10 / P2 15 / P3 7 / P7 4 / P8 9，与题面徽章一致） |
| 练习注册表 | run.py 输出（上） | TOTAL 150；级别/分版/题型与 KIT 登记逐项一致 |

## 目视与全文核查（非机械门，见 PROOF-NOTE.md）

- 印刷 PDF 重新渲染 8 页逐页目视（`render/p1.png`–`p8.png`，不采信 builder 卡片图）；
  网页 PDF P1/P8 目视（`render/web-p1.png`、`web-p8.png`）；P2 词条区 200 dpi 放大（印版+网版）。
- text.md 1379 行全文通读；150 题逐题验算（题干—正文—答案键）；金句 8 条逐字比对；
  P8 注文人名人工逐条核对公开来源（スポーツ報知/日刊スポーツ）。
- 中文残留扫描、禁词扫描、VOL 计数、图片署名核对：结果见 PROOF-NOTE.md。

## 结论

机械门**全部通过**；但目视+人工核查发现 **3 条缺陷（D1/D2/D3）**，详见 PROOF-NOTE.md。
按 SOP §8.4，**本版不能按零问题定稿**，须返修后从头再做一轮全量校对。
