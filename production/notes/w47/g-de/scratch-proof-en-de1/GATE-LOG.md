# GATE-LOG — W47 en-de proof1（重建版）门禁日志

- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-en-de1/`
- 送审目录：`~/workspace/weekly-git/production/2026-w47/2026-w47-en-de/`（只读）
- 解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Python 3.12.3）
- TMPDIR：`.../scratch-proof-en-de1/tmp/`
- 全部门禁均由本校对员在本轮新跑（v1 的 `gates/verify.log` / `gates-part1.log` / `gates-part2.log` 为本轮实际输出；`prev-round-old-build/` 内为上一轮旧版文件，不可与本轮混淆）
- 时间：2026-11-11 13:20–14:30 UTC；中途一次服务重启（约 13:24–13:25），已落盘的日志无损，渲染中断后补跑

## 0. 开工探针（双通）

```
echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin
→ da0c4eb8d9a48d171a33574b380752e183286751   （OK）
goals 侧 scratch 真写文件 → OK（探针文件事后已删）
/dev/null 开工时为普通文件（写成功）；重启后恢复为字符设备 crw-rw-rw- 1,3
磁盘：/home 67G 可用；/tmp 503M 可用；本轮未遇 EDQUOT
```

## 1. 身份核对（本轮命令实测）

```
sha256sum The-Lucerna-VOL4-en-de.pdf        → fe02ab1d9ba41e7a22651be02bda3612b66b54f2c521e12ab0ab5ca6797be5e1  29,331,212 B  ✓
sha256sum The-Lucerna-VOL4-en-de.web.pdf    → 19e166e03f28e813a8418189f20c1ddd31635f6621fbb182268e552c5302e6e5  2,414,462 B  ✓
sha256sum 2026-w47-en-de.text.md           → 0aad0d2c8118bd6dab2f08170425f8ada595b5a397ba0d77511cffdd12c1e5e1  52,568 B  ✓
pdfinfo 两 PDF：Pages 8，Page size 1462.5 x 2025 pts
```
全部与任务/KIT 登记一致，方可开工。核心 en：印 PDF SHA `b484e007…566` = KIT 登记 = re-proof 记录；8 个 SVG SHA 与 `scratch-reproof-core-en1` GATE-LOG 逐个一致（p1 a9a8deaf…、p2 97974716…、p3 efb83ce7…、p4 aa6a515c…、p5 a6a515cd…、p6 76922564…、p7 da908af6…、p8 2f9a0334…）。

## 2. 机械门全套（RC 均 0，见 gates/*.log）

### 2.1 瘦复制重建（gates/rebuild/）

同一源码的瘦复制（删除输出、复制 9 个源文件 + 全量 assets/）在笔记目录内重跑，不碰送审目录：

```
run.py RC=0；OVERFLOW / TOO WIDE 0 次；TOTAL 150；MODEL 82 词
7/7 individual SVG hashes 与送审 SVG 逐字节一致，第八个亦同 → 8/8 字节一致
```
等效 freeze baseline（整树复制因磁盘配额风险未跑的替代方案，做法与 proof1/proof2/fix1 相同）。注意：首次尝试 RC=1，因只拷了 moth 图、缺 `assets/capitolo.jpg`（`assets/lucerna-moth.svg` / `capitol.jpg` 未首拷）——补全 assets 后 RC=0。

### 2.2 遮挡审计 `occlusion_audit.py`（gates/occlusion.log、occlusion.json）

- selftest OK；**0 flags**。

### 2.3 P8 提取与对照（gates/p8-extract*.log、p8-compare.json）

- noted set = 60/150，core 与本版同一集合。
- compare：**CLEAN**；missing=[]、extra_count=0、uncertain=[]。
- keydiff=[137, 138, 139, 140, 150]（预期内：德语翻译键 + Q150 写作题短标签，与 W46 en-de 相同）。

### 2.4 keycheck（gates/keycheck.log）

- registry vs P8 提取 exact 149/150，唯一例外 Q150。
- registry vs core：145/150（差异仅 137–140、150）。
- Q38–41=[b, a, d, c]；Q125=A；Q46=A；Q52=hosted；Q55=won；Q82/83/84=B/C/A；键 150 条齐全。

### 2.5 freeze diff（gates/freeze-diff.log、freeze-diff.json）

vs core：P1 +32/−34、P2 +42/−54、P3 +25/−23、P4 +24/−22、P5 +24/−22、P6 +25/−21、P7 +64/−55、P8 +99/−99；新增 CJK 合计 9 个、全部 U+3000。

### 2.6 印/网文字层（gates/printweb.log）

- 两版各 47,406 字符；token 多重集差 0/0；逐页 byte-identical 8/8（4783 / 5783 / 5277 / 5731 / 4657 / 5592 / 6081 / 9502 B）。
- 网页版 2,414,462 B < 7 MB。

### 2.7 check_s11.py（gates/check_s11.log）

- **ALL PASS**；色集与 core 相同（19=19）；徽章色 A2 #5c6e30 / B1 #46581f / B2 #37402f。
- P8 最小字号 13.5 pt（SVG）；Q113–120 选项级 [A2]、Q145–149 Levels、H WRITING `Schreiben [B1]` 均在版。

### 2.8 标题超框扫（gates/boxtitle.log、boxtitle-svg.log）

- 源扫 12/12 fit（最紧 ODD SOCKS +15.2）；SVG 扫 18/18 fit，0 overflows。
- P3 `HAYMITCH'S GAMES　Spiele` 317.5 px，+87.0（旧版 443.6，−39.1 已修复）。

### 2.9 creambox 典范扫（gates/creambox-all.log）

- RC=0，0 OVERFLOW，32 盒全部 inside-only clearance 为正。
- 最紧：P2 AND YOU? +5.0（desc −1.0 启发式，详见 §3）；P1 SEARCHES +12.0（desc +6.3）；P2 DID YOU KNOW +14.3；P7-TOOLBOX 内 +47.7、desc +41.6。

### 2.10 verify_ed.py（gates/verify.log）

- **VERIFY ALL PASS**：Q39 a、Q40 d、notes mentor=a / arena=d、Q46 2025、Q52 hosted、Q55 won、Q125 A 4–1、无滞留 Ashes 表述、text.md 150 答案、"Arsenal are winning!"、P8 最小 PDF 字号 10.12 pt ≥ 9.75、SVG 零真实 CJK。
- 注：`verify.log` 尾部另有与新 core 比对的 verify3 运行时日志（同一文件内分段），不冲突。

## 3. 必验项独立脚本（gates/*.log、*.json）

### 3.1 P2 AND YOU? 真墨重测（gates/ink_check2.py、ink_check2.log、render/crop-p2-andyou.png）

v1 脚本有扫描窗口/取框 bug（取错盒、扫描越过盒底抓到下方正文 y=1583 的墨迹），已废弃；v2 重写后重测：

```
末行基线 y=1539.85，盒底 1544.9，米色底缘在 y=1544~1545 之间
深色真墨（lum<120）最低行 y=1543（x=1488–1493，g 降部）→ 距盒底 +1 px
抗锯齿边缘（与米色差 >25）最低行 y=1544 → 触及最后一行米色，不出盒
裁决：启发式 desc −1.0 px 为假警报；g 降部完整在盒内。PASS（全版最紧盒）
```
裁图目视确认降部在米色内。

### 3.2 P3 HAYMITCH 真墨重测（同 ink_check2.py，render/crop-p3-haymitch.png）

```
标题 x=1457.5，基线 y=893，23 pt；盒 x=1439.5、宽 422.5，右缘 1862
最右深色真墨 x=1772 → clearance +90.0 px；带顶真墨 y=875，盒顶 856 → +19.0 px
裁图目视：标题居盒内、两侧留白充足。PASS
```

### 3.3 150 题三源一致（gates/verify3.py、verify3-run.log、verify3.log、verify3.json）

registry 键 vs text.md 答案 vs P8 提取键：**0 不一致**（Q150 短标签例外已注）。分版 P1 10 / P2 17 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 39；分级 A2 62 / B1 66 / B2 22。

同脚本附验：Q38–41 四方一致（SVG 题干/选项、registry 键、text.md 注记、P8 提取）；孤儿标点 SVG 8 页独行 。/”/“/：/–/— 均 0，印刷文本按行亦 0；D1 回归（8 条出处行全部 x=538.5，见 PROOF-NOTE §必验 1）；fix1 两串 present、旧串全域 0 命中；金句 8/8 逐字命中印刷文本；禁词 0 命中；VOL.4 ×12 / VOL.5 ×8 / VOL.3 ×3；徽章 LV 填充矩形 16/15/16/16/16/19/13/23 == core == KIT；U+2019 总数 0；真实 CJK 仅非可见 moth `<title>`；字体统计 Newsreader 1022 / Noto Sans CJK SC 655 / Noto Serif CJK SC 27 / DejaVu Sans 4 / UnifrakturMaguntia 1。

### 3.4 旧版对比（gates/oldnew-diff.log、svg-text-diff.log）

旧版 = fix1/proof2 版（SHA `6f82363a…`，备份于 `scratch-fanout-en2/backup/2026-w47-en-de/`）：

```
像素差（110 dpi）：P1 0.99%、P2 1.64%、P3 0.04%（bbox (1956,1001)–(2180,1029) = HAYMITCH 标题区）、
P4 17.80%（Ashes 重写）、P5 0.18%、P6 0.00%、P7 8.71%、P8 0.38%
SVG 可见文本差：P1 +8/−8、P2 +5/−5、P3 +1/−1、P4 +57/−41、P5 +3/−3、P6 +0/−0、P7 +9/−7、P8 +11/−11
registry 差：恰 7 条 — Q39 d→a、Q40 a→d、Q46 注记（Fri 21 Nov 2025）、Q52 hosts→hosted、
Q55 sold→won、Q84 注记 bekannt gegeben（P6 桥接，落在 P8 答案区）、Q125 C→A
text.md 差：120 行，全部为同一重建变化；无 P6 正文 hunk（与 P6 0 变化一致）
```
全部变化可归因于重建修复处，无意外变化。

### 3.5 日期核验（`date -d`，America/Toronto）

Nov 3 Tue、Nov 8 Sun、Nov 9 Mon、Nov 10 Tue、Nov 16 Mon、Nov 18 Wed、Nov 19 Thu、Nov 20 Fri、Nov 21 Sat、Nov 22 Sun、Nov 26 Thu、Nov 27 Fri、Dec 1 Tue；另 Fri 2025-11-21、Thu 2026-01-08、Sun 2026-11-15。全部与正文一致。

## 4. 手工全文与目视

- text.md 全文 1305 行逐行读完（`muse.read` 分段 1–1305，含答案附录 1001–1305；P8 对话词库另以 grep 核 `p8-test.svg`：row/film/popcorn/show/Friday 各现 1 次，含在词库中；`screening` 0 次——本版词库无此词，无影响）。
- 渲染：`pdftoppm` 110 dpi，`render/p-1.png`～`p-8.png`、`render/w-1.png`～`w-8.png`（16 张，重启后补齐 p-5..p-8 与全部 w 页）。8 页印刷版逐版目视 + 8 页网页版逐版目视，结论：无溢出/重叠/截断/豆腐；印网逐页一致。
- ABSTRACT.txt：699 B，德文单行，0 ASCII 双引号；相对旧版 `geprüften`→`verkündeten`、Ashes 条改为一年前回顾 4–1 已核实。

## 5. 事故与异常记录

1. 服务重启（约 13:24–13:25 UTC）：`pdftoppm` 渲染中断（当时只出 p-1..p-4）；第二批门禁日志已全部落盘，无损失。重启后补跑 p-5..p-8 及全部网页版渲染，16 张齐全。`/dev/null` 在重启后恢复为字符设备。
2. 瘦复制重建首次 RC=1：只拷了 moth 图、缺 `assets/capitolo.jpg`——补全 assets 后 RC=0。
3. `ink_check.py` v1 有扫描窗口/取框 bug（取错盒、扫描越过盒底抓到下方正文墨迹），已废弃；v2（`ink_check2.py`）修正后重测，结论以 v2 为准。
4. `git status` 显示 `issues/2026-w43/...` 有他 agent 在途的修改——非本轮所动；本版目录始终只有 `?? production/2026-w47/2026-w47-en-de/` 一项未跟踪；本轮未做任何 git 写操作（探针 `git hash-object -w` 除外）。

## 6. 门禁汇总（结论）

run.py RC=0 · occlusion 0 · p8 extract 150/150 + compare CLEAN · freeze 8/8 字节一致 · 印/网文字层逐页 byte-identical 8/8 · P8 最小字号 13.5 pt（SVG）/ 10.12 pt（PDF）· keycheck 150/150（Q150 短标签例外）· creambox 32 盒 0 OVERFLOW · boxtitle 12/12 + 18/18 · verify_ed ALL PASS · 150 题三源 0 不一致 · 8 版双版目视通过 · 孤儿标点 0 · D1 回归通过 · fix1 两处文案落版 · HAYMITCH 真墨 +90.0 px · AND YOU? 真墨在盒内（启发式 −1.0 px 为假警报）。

**结论 (a) 定稿，零缺陷。**
