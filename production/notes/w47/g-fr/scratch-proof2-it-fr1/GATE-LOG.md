# GATE-LOG — W47 it-fr proof2（重扩散新版，独立重跑）

- 版：`production/2026-w47/2026-w47-it-fr/`（核心 fix3 `36bdec2e`）
- 工具：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0）
- 环境：`PYTHONDONTWRITEBYTECODE=1`；`TMPDIR=<scratch>/tmp`
- scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof2-it-fr1/`
- 探针：`git hash-object -w /dev/null` 成功（e69de29bb2…）；scratch 真实写盘成功。

## 0. SHA 核对（开工 + 收工两次）

| 文件 | sha256 | 字节 | 开工 | 收工 |
|---|---|---|---|---|
| `La-Lucerna-VOL4-FR.pdf` | `6e393b3d385c606443c82b7813ddfae2623b9ee2fff128690247f1f2f0fcf00f` | 14,034,074 | ✓ | ✓ |
| `La-Lucerna-VOL4-FR-web.pdf` | `7276c70ff46caf931ba761ec3ca36f7b8ee467c1c1d22931f460eaa81596b77f` | 1,290,987 | ✓ | ✓ |
| `2026-w47-it-fr.text.md` | `a634057bfdf97f0c29492ba769c96213a6540ef15f8a1cbf17bc88ed51dc92f7` | 56,538 | ✓ | ✓ |

KIT §7 所载印/网 SHA 与字节数一致；文本 SHA 与 FANOUT-REPORT-it.md 所载一致。

## 1. run.py（`run-rebuild.log`，scratch 副本内运行）

- RC=0；TOTAL 150；levels A2 47 / B1 70 / B2 33；
  pages 10/18/18/18/18/18/12/38；model text 99 words。
- 0 FLOW OVERFLOW / 0 HEAD TOO WIDE / 0 NOSPACE（grep 计数 0）。
- flow 末端（均在界内）：P1 settimana 1250.24；P1-quiz 2491/2540；
  P2 col3 1350.6；P3 col3 1290.6；P4 col3 1140.45（= core 1140）；
  P5 col3 1249.75；P6 col3 1096.5；P7 col3 1673.0；
  P8-ex 870/1332；P8-keys 2514/2552。**PASS**

## 2. SVG 重建 8/8 字节一致

- scratch 副本 `run.py` 重建后 `sha256sum -c shipped-svg.sha256`：
  p1–p8 全部 OK。**PASS**

## 3. 重渲印 PDF 与交付逐字节相同

- scratch 副本 render.py（BASE 重定向）RC=0；
  重渲 `render/La-Lucerna-VOL4-FR-rerender.pdf` sha256
  `6e393b3d385c606443c82b7813ddfae2623b9ee2fff128690247f1f2f0fcf00f`，
  14,034,074 B，`cmp` 通过。**PASS**

## 4. freeze 核心 baseline 8/8（`freeze-baseline.log`）

- `tools/freeze.py baseline --build <edition> --core-svg <edition>/svg --out <scratch>/freeze-out`：
  `baseline: 8/8 SVGs byte-identical`（p1 874b2129…/p2 8bfcedce…/
  p3 617cf701…/p4 b7637046…/p5 9abdc25c…/p6 723d688d…/p7 c98aca07…/
  p8 94b069ae…）；`core integrity: shipped core SVGs unchanged`。
  运行时 Pillow 13.0.0 / FreeType 2.14.3。**PASS**

## 5. freeze diff（gates.py 内，见 `gates/gates-fr.log`）

- fragments explained：unexplained_add=[] unexplained_rem=[]（P1–P7）。
- 报告 present：pages 1–8。
- strict-cjk：added_cjk={'\\u3000': 8}，non_space={}。**PASS**

## 6. occlusion（gates.py 内）

- `tools/occlusion_audit.py`（selftest OK）：0 flags。**PASS**
- 注：occlusion 对无边框奶油盒横向溢出是盲的，本版另以门 7 像素扫裁决，
  不以此门为据。

## 7. 奶油盒 PIL 真墨像素扫（`cream-scan.log`，`cream_scan.py`）

- 29 个无边框奶油盒（#f0eee5）逐盒像素扫：全部 PASS，无墨越界。
- 最薄：P1 LA SETTIMANA 盒（x=1439.5, y=588）margin-R=0 px
  （字墨触边，见 PROOF-NOTE O1）；其余 +7 至 +189 px。
- 四个表修标题像素实测：D1 +7–8 px；D2 0 px；D3 +9 px；D4 +110–111 px。
- `measure_built.py fr` 交叉核对（PIL 方法值）：D1 +4.5 / D2 +5.5 /
  D3 +8.5 / D4 +111.5，ALL PASS——但像素真相与 PIL 值差约 ±5 px，
  裁决以像素为准（见 PROOF-NOTE“方法发现”）。**PASS**

## 8. spill：0

- build 日志 0 溢出（门 1）+ 全部 flow 末端在界内（门 1）+ 奶油盒像素扫
  29/29（门 7）+ occlusion 0（门 6）。**PASS**

## 9. 孤儿扫

- 粗扫误报 90（徽章/标签/标题/图表值）已逐项排除；
  精扫（Newsreader 正文流 + P8 键列表逐行重建）：**0 处栏断孤儿**。
- 仅 1 处行内独词换行：P8 Q139 第二行 `domicile`（p8 y=2187，
  判定见 PROOF-NOTE O3，非缺陷）。**PASS**

## 10. p8 extract 150/150（gates.py 内）

- `tools/p8.py extract` noted=150，rc=0。**PASS**

## 11. p8 compare（gates.py 内）

- `tools/p8.py compare` vs core：verdict=CLEAN，
  **keydiff 实测 [137, 138, 139]**（重定向的读者句键，与预期一致；
  Q140 键为意语句、与核心相同故无 diff，正确）。
- 另：150-key 审计 vs core `.text.md`：keys 1–150 match
  （除 137–139 与写作题外）；notes match translations.py
  （除 137–140 与写作题外；9 条冻结注释为意语变位/算术，字节一致、无 CJK）。**PASS**

## 12. P8 最小字号 ≥9.75pt

- P8 SVG 最小 font-size 13.0 px = 9.75 pt（§1.1 下限）。**PASS**

## 13. §1.1 视觉规范

- paper #fbfaf6 present；no gold/brick/near-black（hits=[]）；
  VOL.4 ×9；VOL.5 text nodes=3（仅预览/披露/交叉引用三处合法）；
  badge colours A2 #5c6e30 / B1 #46581f / B2 #37402f 齐全；
  no double outer frame（full-page rects=0）。**PASS**
- 注：`·` 总计 148 处，位于选项串/注释表内（核心同式）。

## 14. 印/网文字层一致（gates.py 内；web PDF 未重渲）

- pdftotext 词多重集：print 8012 / web 8012 词，字符多重集相等。
- web PDF 1,290,987 B < 7 MB；print PDF 14,034,074 B；
  两 PDF 均为 8 页，1462.5×2025 pt。**PASS**

## 15. text.md validate

- forward-miss 0 / reverse-miss 0（fr footer 正则 `Page \d+ sur 8`）。
  1317 行，150 题。**PASS**

## 16. 日期星期全验

- `TZ=Europe/Rome date -d`：Nov 6 周五、7 周六、8 周日、9 周一、
  12 周四、15 周日、16 周一、17 周二、19 周四、20 周五、21 周六、
  22 周日、23 周一、24 周二、29 周日、Dec 2 周三、Dec 6 周日、
  Dec 31 周四。文中全部星期主张逐项正确。**PASS**

## 17. 标题数实测

- `##` 页标题 8；文章头条 6；全大写标题行 27（含赛果日标 5、时间线
  标签 4），盒标题 proper 18。任一自然口径均不为 56——“56 titles”
  为幻数，非本版计数。**记录**

## 18. 全文精读与看图

- `.text.md` 1317 行通读：意语层 freeze 0 unexplained；8 金句各 ×2；
  150 key/note 逐题复核；法语层无拼写/性数/变位/标点错误；
  Q137–140 标签本地化，无 `「翻譯」` 残留；禁用词 0；非 U+3000
  CJK/西里尔 0；99 词范文逐词数过 = 99。
- 8 版逐版看图：联系表 + P1/P7/P8 全页 + D2/Q139 裁图；无溢出、
  重叠、压页脚、tofu、图片错位。**PASS**

## 19. gates.py 20 门（独立重跑，`gates/gates-fr.log`）

```
PASS occlusion 0 flags
PASS p8 extract noted count (150)
PASS p8 compare vs core (CLEAN, keydiffs=[137, 138, 139])
PASS freeze diff fragments explained (0 unexplained)
PASS freeze diff report present (pages 1-8)
PASS freeze strict-cjk (only U+3000 x8)
PASS print/web text multiset identical (8012/8012, chars_equal=True)
PASS web PDF < 7MB (1290987)
PASS print PDF size sane (14034074)
PASS P8 min font >= 13px (min=13.0)
PASS paper #fbfaf6 present
PASS no gold/brick/near-black
PASS no VOL.5 in furniture (3 nodes)
PASS VOL.4 present (count=9)
PASS badge colours A2/B1/B2
PASS no double outer frame (0)
PASS textmd validate (0/0)
PASS answers count 150 (150/150)
PASS keys 1-150 match core (except 137-139, writing)
PASS notes match translations.py (except 137-140 + writing)
GATES ALL PASS — 20/20, 0 FAIL
```

## 总评

全部门禁通过。结论 (a) 零缺陷，可定稿。两处最薄点已在 PROOF-NOTE
O1–O3 中以像素实测与渲染证据记录在案，均不构成缺陷。
