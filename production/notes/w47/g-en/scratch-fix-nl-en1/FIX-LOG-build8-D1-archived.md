# FIX-LOG — W47 nl-en fix1 (proof1 D1 + 同类残留)

- 版：`2026-w47-nl-en`（荷兰语目标语 × 英语读者），VOL.4，刊期 2026-11-16–2026-11-22
- 任务：修 proof1 (b) 唯一缺陷 D1；整版重渲染；全部机械门重跑；更新 KIT / record 的交付物 SHA 与门禁记录
- 工作目录：`~/workspace/weekly-git/production/2026-w47/fanout-nl/2026-w47-nl-en/`（只动此目录 + 本笔记目录；未碰 core-nl、其他家庭、tools/、issues/；未跑 insert.py / lint --write；无任何 git 写操作）
- 日志目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-nl-en1/`

## 0. 开工探针（2026-11-11 07:59 UTC）

- `git hash-object -w` 小文件：成功（`c4b82938c3a39fd8ec5762c339240e6c87d1e1b1`）
- 在 hidden_files/w47/ 真实写文件：成功（`scratch-fix-nl-en1/PROBE.txt`）
- 磁盘：`/home/hatch` 可用 46G，无 EDQUOT。探针通过后才动手。
- 注意：任务所写的 brief 路径 `~/workspace/weekly-git/hidden_files/w47/briefs/brief-coordinator.md`
  不存在；实际 brief 在 `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/briefs/brief-coordinator.md`，已读全文。SOP.md 已读全文。

## 1. 身份核验（修前，盘上实测）

| 文件 | 字节 | SHA-256 | 与任务登记 |
|---|---|---|---|
| `De-Lucerna-VOL4-nl-en.pdf`（印刷，build 7） | 12,690,133 | `0b4dc8c0e19b72a0d753842bdec7775064481a0b4b37bb88f66fa4aa5199f2e7` | 一致 |
| `De-Lucerna-VOL4-nl-en-web.pdf`（网页，build 7） | 1,576,939 | `477dd85dc87cda7ffa5ff71a5e5b15a5dcc33ff3db8d2ed49a8654f8a2cb8de6` | 一致 |

## 2. 缺陷核实（修前，自己在盘上核实属实）

- D1 属实：`content7.py` 第 92 行（wrap 行数计算）与第 101 行（渲染调用）各有 1 个 U+2019，
  字符串 `Editor’s example, not a real letter. Send yours — we print them in VOL.5!`；
  `svg/p7-taal.svg` U+2019 ×1；`.text.md` 第 366 行 U+2019 ×1；印刷 PDF 文字层 P7 U+2019 ×1。
  与 proof 笔记一致。
- 全版弯引号初扫（`content*.py`、`svg/*.svg`、`.text.md`、`svglib.py`、`bslib4.py`、`render.py`、`run.py`、`ABSTRACT.txt`）：
  - U+2019：`content7.py` ×2（上两行），其余 0
  - U+201C/U+201D：`content12.py` 第 113 行各 ×1，字符串 `“Group win”: first place in the group, straight to the quarter-finals.`（P1 本周一词英文释义，Noto Sans CJK SC 19pt，读者可见）
  - U+2018/U+201A/U+201E/U+2032/U+2033：全版 0
  - P1 渲染裁图核实：弯双引号呈宽字形，`“Group win” :` 冒号前有明显空隙——与 D1 同一缺陷类，按任务授权一并修复。
  - 其余观察项 O1–O7 一律未动。

## 3. 改动（只改 2 个文件，3 处字符串）

| 文件 | 行 | 改动 |
|---|---|---|
| `content7.py` | 92、101 | `Editor’s` → `Editor's`（U+2019 → U+0027，各 1 处，共 2 处；双引号字面量内，直接替换） |
| `content12.py` | 113 | `“Group win”` → `"Group win"`（U+201C/U+201D → U+0022；字符串改用单引号字面量包裹——直接替换会产生 `""Group win"...` 语法错误，修复时先写出该错误并立即以单引号字面量纠正，`py_compile` 通过） |

- 其余文件（core、其他版、tools/）未动。`«»`（U+00AB/BB，如 P7 `«de groepswinst»`、P8 103 题）为目标语原文引号写法、核心继承，不在弯引号修复范围，未动。

## 4. 重渲染（build 8，全量）

- `run.py` rc=0：TOTAL 150（逐页 10/18/18/18/18/18/12/38；A2 46 / B1 73 / B2 31；范文 81 词）；OVERFLOW / TOO WIDE / WARNING 计数 0；P7 col3 仍 ends 1927.5（行数未变）
- `render.py` rc=0：8 张 cards + print PDF 12,665,899 B
- `webpdf.py` rc=0：web PDF 1,574,228 B，45,409 text bytes
- `export_fanout.py . en` rc=0：`.text.md` 45,074 B；142 单题行 + 2 match headers + 8 match items = 150；8 golden；6 gloss
- 日志：`en-build8.log`、`en-render8.log`、`en-webpdf8.log`、`en-export8.log`（本目录）

## 5. 新交付物（build 8）

| 文件 | 字节 | SHA-256 |
|---|---|---|
| `De-Lucerna-VOL4-nl-en.pdf`（印刷） | 12,665,899 | `2cc431f2572abad8790d1b99d6211d3aa87a5278a4052f3f0810dd6d764b0b58` |
| `De-Lucerna-VOL4-nl-en-web.pdf`（网页） | 1,574,228 | `0fc6232bbe2bd8d3794169d83b4c233df519845f07eef1f9f35e2fdada2f6d18` |
| `2026-w47-nl-en.text.md` | 45,074 | `1d69f5edc43e217bfa5d9e032d3c8c6666460a37ee163d0f0db18b1bebeba45b` |

- `.text.md` 字节变化 −6，与字符替换一致（`’` 3B→1B ×1；`“”` 6B→2B ×1 对）。

## 6. 修后复扫（弯引号，须为 0）

- 源码 + SVG + `.text.md`（U+2018/U+2019/U+201C/U+201D/U+201A/U+201E/U+2032/U+2033）：**0**
- 印刷 PDF 文字层：**0**；网页 PDF 文字层：**0**
- `.text.md` 第 366 行现为 `Editor's example, ...`；第 45 行现为 `"Group win": ...`；SVG p7 `Editor's` 已同步。

## 7. 目视核实（build 8 印刷 PDF 重渲染裁图）

- P1 gloss：`"Group win":` 直引号紧贴，冒号前无宽空隙。修好。
- P7 BRIEVEN 框：`Editor's example, not a real letter. Send yours — we print them in VOL.5!` 直撇号紧贴 s，无 "Editor' s" 断裂；框底仍在 ZINNEN 规则线上方。修好。
- （目视仅针对两处修复点；全量 8 版复校由第二轮校对员做，本人不做复校。）

## 8. 记录更新

- `WEEKLY-KIT.md`（版目录）：§4 增加 fix1 条目（item 7）；§6 交付物改为 build 8 字节/SHA；§7 改为 build 8 门禁记录 + 弯引号扫查 + 目视核实；顺带纠正 O1 指出的一处 KIT 记录笔误（P7 token 数 935 → 实测 915，`en-gates7.log` 与 proof 重跑均为 915，非成品问题）。
- `scratch-fanout-nl/en.md`（nl-en 家族的 builder record；该版无独立 `EDITION-RECORD.md` 文件，故更新此处）：增加 Fix1 节，Gates / Deliverables 改为 build 8，状态改为待第二轮全量复校。
- 机械门详见 `GATE-LOG.md`（本目录）。

## 9. 结论

D1 已修；同类残留 P1 弯双引号已按授权一并修掉并列明；整版重渲染完成；U+2019 全版复扫为 0；全部机械门 9/9 绿（见 GATE-LOG.md）。待协调员另派第二轮全量复校。
