# FIX-LOG — 2026-W47 zh-cn-fr fix1（D-1 ~ D-4，2026-11-11）

- 修复员：fix1；版：`production/2026-w47/2026-w47-zh-cn-fr/`（简体中文目标 × 法语读者，VOL.4）
- 依据：proof1（2026-11-11 17:31 UTC 盘验）结论 (b)，4 项缺陷全部是法语串加长后未收口的回归
- 工作区：`~/workspace/weekly-git/production/2026-w47/2026-w47-zh-cn-fr/`
- 记录目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-zh-cn-fr1/`
- 解释器：一律 `~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）
- 未 commit、未 push；待独立校对员 re-proof，本人不定稿。

## 0. 开工核对（修前三 SHA，与任务书逐字一致）

| 件 | SHA-256 | 字节 |
|---|---|---|
| 印 `Lucerna-VOL4-FR.pdf` | `f00a276e9d3366f6220df0acfc7e3f7b5573209f349d8fb380dc7a42252027f4` | 42,504,783 |
| 网 `Lucerna-VOL4-FR-web.pdf` | `b7e43796dbe39674e42910eb37c56b20e45bd223e797bb3999560ee8d516845c` | 2,663,754 |
| 文 `2026-w47-zh-cn-fr.text.md` | `fb72ed2964225edb7f51599047012d0501499f41cb80543ec67d01753473080b` | 51,829 |

- 修前横扫复现（`sweep.py`，proof1 同款，`sweep-before.log`）：3 flags，与 proof1 数值逐字一致 —— D-1 墨右缘 978.8 > 盒 961.0（超 17.8）；D-2 1869.5 > 1862.0（超 7.5）；D-3 1414.8 > 1411.5（超 3.2）。
- 修前 SVG 哈希见 `svg-before.sha256`；`ABSTRACT.txt` 333 B，末字节 `\n` 在位（修后未动，见 §5）。

## 1. 四缺陷的修法（仅 `content12.py` 4 处，其余源码一字不动）

修法原则：D-1/D-2/D-3 用“最小降字号、文字零改动”收口（候选量测见 `measure_candidates.py` / `measure_candidates.log`，PIL 真墨 + advance 交叉验证）；D-4 按任务书建议缩短其前法语段。

| # | 源码行 | 改动 | 实测量测（修前 → 修后，PIL 真墨） |
|---|---|---|---|
| D-1 | `content12.py:47` P1 数字盒标题 | `f.box(..., tsize=23)` → `tsize=21`；标题文字 `数字看本周　Cette semaine en chiffres` 不动 | 墨右缘 978.5 → **942.0**（盒 961.0），余量 **+19.0 px**（核心同位 +20.2；任务标准 ≥ +5）。修前 advance 422.2；21pt advance 385.5 |
| D-2 | `content12.py:88` P1 截稿行 | 字号 `19` → `18`；文字 `Bouclage : 10 nov. — la finale pas encore jouée` 不动 | 墨右缘 1869.5 → **1848.5**（盒 1862.0），余量 **+13.5 px**（核心 +10.2；≥ +5）。SVG 实测：单 run，`font-size="18"`，x=1461.5，y=1252 |
| D-3 | `content12.py:187` P2 日历盒标题 | `f.box(..., tsize=23)` → `tsize=22`；标题文字 `本周生活小日历　Dates de la semaine` 不动 | 墨右缘 1415.0 → **1397.0**（盒 1411.5），余量 **+14.5 px**（核心 +22.0；≥ +5）。SVG 实测：单 run，`font-size="22"`，x=1007.0，y=236 |
| D-4 | `content12.py:50` P1 数字盒第 3 项 | `le nouveau film 《试探》 sort` → `le film 《试探》 sort`（删 `nouveau `，事实内容不变） | `wrap()` 20pt/内宽 386.5：修前 2 行（`21 nov., samedi — le nouveau film 《试探` / `》 sort`）；修后 **1 行**（`21 nov., samedi — le film 《试探》 sort`，advance 349.9 ≤ 386.5）。SVG 实测：同一基线 y=1337.265 四 run 连成整句，无行首 `》` |

- 未动：`bslib4.py`、`svglib.py`、`render.py`、`run.py`、`content34/56/7/8.py`、`WEEKLY-KIT.md`（mtime 仍 2026-11-11 14:07）、`ABSTRACT.txt`（333 B，尾换行在位）、核心 `core-zh-cn/` 全目录（freeze baseline 同步验证核心 SVG 未变）。
- 铁律①：全部重建输出重定向均用 scratch 内绝对路径（`$SCRATCH/*.log`），运行前核对目标在 scratch 内；无相对/波浪路径重定向。

## 2. 重建（整版全套，日志均在 scratch 内）

- `run.py`（`run-fix1.log`）：rc=0，**TOTAL 150**（A2 56 / B1 69 / B2 25；按版 10/18/18/18/18/18/12/38，与修前一致），`FLOW OVERFLOW` / `HEAD TOO WIDE` 计数 0；P7 teaser ends 2588.78；P8 keys flow ends 2537.2。
- `render.py`（`render-fix1.log`）：rc=0，cards 8/8，印 PDF 42,504,769 B。
- `tools/webpdf.py svg <绝对路径>/Lucerna-VOL4-FR-web.pdf`（`webpdf-fix1.log`）：rc=0，网 PDF 2,663,732 B（< 7 MB），45,540 text bytes，724 distinct chars。
- `export_fr.py`（`export-fix1.log`）：rc=0，recorded 1050 strings，registry 150，写出 51,821 B。
  - 导出器验证：先以修前源码副本（`orig-copy/`，4 行还原）跑同一导出器，逐字节复现修前 text.md（SHA `fb72ed29…` 全串一致，`export-origcheck.log` / `textmd-orig-check.md`），再以修后源码导出。
  - text.md diff（修前 → 修后，`diff textmd.before.md`）：**仅 1 行**——第 53 行 `21 nov., samedi — le nouveau film 《试探》 sort` → `le film 《试探》 sort`（−8 B = 删 `nouveau ` 8 个 ASCII 字符，吻合）。

## 3. 修后三 SHA（新交付件，本次重建产生）

| 件 | SHA-256 | 字节 |
|---|---|---|
| 印 `Lucerna-VOL4-FR.pdf` | `097c8818a56d955e509d5beeae51b3ef6b879b582003f3192dccb82905c68b8e` | 42,504,769 |
| 网 `Lucerna-VOL4-FR-web.pdf` | `467527f24998e7af8738670b8b99af3d444893f950b198e3dabf077ef9ac0573` | 2,663,732 |
| 文 `2026-w47-zh-cn-fr.text.md` | `e125a9d1b75bb02ca922dcbcb73ac012714270d1e3c3ec22c50a68d1aecc12e6` | 51,821 |

- 收工时重验三 SHA，全串与上表一致。网 PDF SHA 不可复现，只比文字层（见 §4）。

## 4. SVG 变化清单（只应有 P1、P2 变化）

| 页 | 修前 SHA（前 12） | 修后 SHA（前 12） | 结论 |
|---|---|---|---|
| P1 `p1-touiban.svg` | `4f5d9f9d10c3` | `56d78e96d0f3` | 变（D-1/D-2/D-4） |
| P2 `p2-shenghuo.svg` | `0d7c0e65328b` | `5ca342707007` | 变（D-3） |
| P3 `p3-wenhua.svg` | `5db4f742a3ab` | `5db4f742a3ab` | 字节不变 |
| P4 `p4-tiyu.svg` | `0b3dbf1fb92d` | `0b3dbf1fb92d` | 字节不变 |
| P5 `p5-qingnian.svg` | `c6790a13a69d` | `c6790a13a69d` | 字节不变 |
| P6 `p6-shendu.svg` | `7e46d0222b80` | `7e46d0222b80` | 字节不变 |
| P7 `p7-ciyu.svg` | `93c295b11d74` | `93c295b11d74` | 字节不变 |
| P8 `p8-ceyan.svg` | `fd2c40759b88` | `fd2c40759b88` | 字节不变 |

- 完整前后 SHA 见 `svg-before.sha256` / `svg-after-run.sha256`。

## 5. 四缺陷修后验证（PIL 真墨 + advance 交叉，像素为准；渲染裁图留证）

| # | PIL 真墨（sweep 复跑，`sweep-after.json`） | 渲染像素（`cards/*.png`，1950×2700，1:1 坐标） | 目视裁图 |
|---|---|---|---|
| D-1 | 墨右缘 942.0，余 **+19.0** | 墨右缘 939，余 +22 | `crop-d1-title.png`：标题末 `s` 在盒内，盒边在右留有奶油空地 |
| D-2 | 0 flags（sweep 全刊 0 处越盒）；advance 墨右缘 1848.5，余 +13.5；渲染像素墨右缘 1846，余 +16 | `crop-d2-pressline.png`：`é` 在盒内，右侧奶油空地清晰 | — |
| D-3 | 墨右缘 1397.0，余 **+14.5** | 墨右缘 1397，余 +14.5（与 PIL 一致） | `crop-d3-title.png`：标题末 `e` 在盒内 |
| D-4 | SVG run 检查：`》 sort` 行首孤儿 0；孤儿扫描（`orphan_scan.py`，proof1 门 8 同法，按基线+栏位分组）**0 orphans**（`orphan-fix1.json`） | `crop-d4-item3.png`：`21 nov., samedi — le film 《试探》 sort` 单行完整，无孤儿 | — |

- 全刊横扫（`sweep-after.log`）：8 页，texts 3285，containers 181，flags **0**（修前 3）；179 个容器标题最小正余量现为 D-1/D-3 修后值以外，P5 `这一周的高频词　Mots de la semaine` +6.0 不变。

## 6. 门禁逐项实测值（详见 GATE-LOG.md）

- `gates-zhcn.py` **11/11 ALL PASS**（`gates-fix1.log` / `gates-fr.json`）
- freeze baseline（核心）：rc=0，**8/8** 字节一致，核心完整性确认
- freeze diff `--strict-cjk`：rc=0，**新增 CJK 0**（8 页全 0；CJK 计数与 proof1 逐字一致：870/1060/859/767/964/907/742/1118）
- p8 compare：**CLEAN**（`p8compare-fix1.json`；missing/extra/uncertain/keydiff 全空）
- 印/网文字层：8/8 页 token 位置差 0、多重集差 0；`pdftotext` 印/网均为 45,540 B
- P8 最小字号：9.98 pt（≥ 9.75；与修前 9.975 同值，核心设计取整，未动）
- 150 键复核：REG 150 行与 proof1 `reg-fr.json` 逐行一致；LOG 仅 1 处差异（即 D-4 改动）；P8 印出键与 proof1 逐键一致；Q150 开放题 `✓` 与修前一致
- “绝不动”复验：P4 注释框所在 P4 SVG 字节不变（框底 792.2 恒成立）；P8 keys 尾 2537.2；P7 预告条底 2588.78；ABSTRACT 333 B 尾换行；badge（strict-CJK 新增 0）；核心 D4/D5 措辞未动（印 PDF 计数未重跑，但改动文件只含上述 4 处，D4/D5 所在 `content34.py` / P1 正文段未动，且 freeze CJK 计数与 proof1 全同）

## 7. 结论

(a) 修完自验全过。四缺陷全部收口，门禁 11/11 + freeze 8/8 + strict-CJK 0 + p8 CLEAN + 印/网文字层 8/8 差 0 + 150 键无回归，SVG 变化仅 P1/P2。
