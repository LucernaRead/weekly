# GATE-LOG — W47 fr-it proof2（re-fanout #2 独立复校）

复校：2026-11-11。解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）。
工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr-it2/`。
生产文件只读；决定性重建在 goals 侧副本 `build-copy/2026-w47-fr-it/` 内跑。

## 身份核对（磁盘 SHA-256，复校前 = 复校后，未变）

- 印 `La-Lucerna-VOL4-fr-it.pdf` 17,415,873 B `2a47495b00bda39a108420b1986bf214946220952b6f9c8b4bd47e842e5632f6` ✓
- 网 `La-Lucerna-VOL4-fr-it-web.pdf` 1,696,726 B `8957acb69bb9342957c0c20a2f61412f0386beb721cdb076fbfa493bcd58b3ab` ✓
- `2026-w47-fr-it.text.md` 46,617 B `fac32b0bbf28a1b1a7a7365620de5348501fa49b7295816414522bd85ca25919` ✓
- 核心印 30,446,975 B `a30af667b25929984c34cf2af621c0b15a3072f4db55a14e507d3682ace25a9d` ✓
- 核心网 2,241,835 B `56f50ca8ab7ec912408bb4eda77c5a1a36eb7cc2639f09400584a6166d58e141` ✓
- 核心 text.md 46,471 B `52024e024d32ca22c32287c7954d05e2bae9480dd75448b65169bb4899d063df` ✓

## freeze（标准口径）

- `tools/freeze.py baseline --build production/2026-w47/core-fr --core-svg production/2026-w47/core-fr/svg`：**8/8 byte-identical**，核心三件复核未变。见 `freeze-baseline.log`。
- `tools/freeze.py diff --core-svg … --edition-svg …`：p1 +25/-23，p2 +37/-33，p3 +35/-44，p4 +45/-49，p5 +39/-42，p6 +29/-30，p7 +41/-34，p8 +124/-123；新增 CJK 仅 U+3000 ×10（p2 1、p8 9）。见 `freeze-diff.log` / `freeze-diff.json`。

## 15 门独立复跑（gates.py it proof2，exit 0）

见 `it/gates-proof2.log` / `it/gates-proof2.json`；重建日志 `build-proof2.log` / `build-proof2-rerun.log`（副本内跑；生产 SVG 哈希复核未变）。
唯一改动：freeze_direct 改为 goals 侧副本重建（proof1 前例；生产目录内绝不重跑 `run.py`）。

```
PASS run: exit 0, zero overflow/wide; TOTAL 150
by level {'A2': 53, 'B1': 75, 'B2': 22}
by page {1: 10, 2: 15, 3: 18, 4: 18, 5: 17, 6: 18, 7: 12, 8: 42}
PASS occlusion: 0 flags, selftest OK
PASS p8_extract: keys 150/150, printed notes 121/150
PASS p8_compare: CLEAN, keydiff [150] (writing key only)
PASS source_freeze: content/bslib/svglib/run byte-identical to core; render.py differs only in BASE+PDF name
PASS string_freeze: all non-CJK core strings survive per page; 0 core-E survivors; 0 unaccounted CJK chars; 1 strings excused as translated E values
PASS freeze_direct: two builds sha256 8/8 identical: ['aa3ae078', 'f541b51c', '52b4baf0', '249b0d98', 'a91995f1', '76cc6f87', '12eb2907', '64d1ba48']
PASS text_layer: print/web pdftotext byte-equal (106161 B); web 1696726 B < 7MB; print 17415873 B
PASS p8_font: P8 min font 11.625pt >= 9.75pt
PASS scans: U+2019=0, U+00B7=0, gold=0, old paper=0, #fbfaf6 x8
PASS chips: 134 total [10, 12, 18, 15, 14, 15, 12, 38]
PASS keycheck: 150 keys vs core: only Q150 differs (writing key) — 150 core keys, 150 extracted
PASS mcq: bodies: 45  rendered lines: 1478
PASS widths: 31 single-line strings all within budget
PASS band_spans: FR title ends 1236.9, band_r1 starts 1307.6, FR sub ends 837.2, band_r2 starts 1481.2
GATES 15/15 PASS
```

## 附加门（本复校独立跑）

- **check_extra**（`it/extra-proof2.log`，修正后检测器）：orphan total=0 new=0 inherited=0 remnant=0 shared_baseline=0；blank lines it P3 (538.5, 1894.4)/(538.5, 2027.1)（+30）、P8 (989.0, 843.0)（与核心同）；Q148 stem_ok + key_in_content8 + extracted `devant le`。**EXTRA PASS**。
- **creambox**（规范版，`creambox-proof2.log`）：exit 0；33 盒；7 处负 clearance 全为下一栏目标题假阳性（盒内 clearance +47.7/+48.0/+48.5）；P7 披露盒末基线 2233.3、clearance +24.7、desc-clear +18.8。
- **PIL P7**（`pil-p7-proof2.log`）：末行灰墨 svg y 2237.3；间隙 2258–2270 零墨。
- **spill / boxtitle**（`spill-boxtitle-proof2.log`）：33 盒；盒底 +60 px 内盒外行 11 行全为粗体标题，正文续行溢出 0；33 盒标题 PIL 真墨溢出 0。**SPILL/BOXTITLE PASS**（注：首版 sweep 因整页纸底 rect 导致空转，已排除纸底 rect 后重跑，结论为真扫描）。
- **check_s11_it**（`check-s11-proof2.log`，fr 改编版；fr scratch 里找到的 check_s11.py 均为 en-family 脚本不可用，见 PROOF-NOTE §3）：36 项 PASS，含纸色/色集与核心一致、VOL、徽章、P8 字号。**CHECK_S11 PASS**。
- **verify_ed_it**（`verify-ed-proof2.log`，fr-it 专用）：24 项 PASS，含 D1/D2/D3/Q148/text.md 答案键（答案块解析 150 键，与 registry 逐项一致，Q150 除外）。**VERIFY_ED PASS**（注：首版 text.md 答案正则误用 en 格式，0 命中；已按 fr-it 实际格式 `N. KEY (nota)` + U+3000 拼接修正后重跑通过）。
- **keycheck registry vs P8 extract**：150/150 键，仅 Q150 形态不同（registry 长注记 vs extract 短键 `Domanda aperta`）；registry vs core 亦仅 Q150 不同。
- **occlusion**（真实命令，无 `--selftest`；`occlusion-proof2.json/log`）：0 flags，selftest OK。

## 150 题手验

- `key-stem-check.txt`：123 题 `text.md` 题干 + 键 + 注记逐题核对；5 组配对题取 `content*.py` 的 `match_set` 左右列逐对验语义；对话题 145–149 取 P8 SVG 对话全文逐句验；Q150 写作题例外。**150/150 适配。**

## 回归（#1 备份）

- SVG 页哈希：仅 P5/P7/P8 变，其余 5 页逐字节相同。
- 文本层行级 diff：P5 恰 2 行、P7 恰披露注记 3→2 行、P8 恰 2 行。
- 源码 diff：`expl.py` 恰 2 行、`content8.py` 恰 2 行，其余源码与 `ABSTRACT.txt` 全部相同。

## 目视

- `png/pg-1.png` … `png/pg-8.png`（100 dpi，印刷 PDF）；`png/p7-courrier-bottom-300dpi.png`；`png/p5-wordlist-300dpi.png`；`png/p8-dialogue-300dpi.png`。
- P1–P8 零问题；P7 披露框、P5 词表、P8 对话三处修复均经 300 dpi 目视确认。

## 字体调查（D5，已知全周待定项，记录）

- 8 SVG：Noto Sans CJK SC 690 / Newsreader 944 / Noto Serif CJK SC 74（皆 U+3000 run）/ UnifrakturMaguntia 1 / DejaVu Sans 4（P7 ✗）。较 proof1 的 691 少 1 个，系删去的披露中句带走一个 sans 元素。

## 结论

(a) 零缺陷，可定稿。缺陷清单：无。
