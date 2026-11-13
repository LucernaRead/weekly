# GATE-LOG — W47 core-pt 独立复校（fix2 后，re-proof）

- 复校员：独立复校。日期：2026-11-11。对象：`production/2026-w47/core-pt/`，fix2 本地 commit `d2b0e182`（未 push）。
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-core-pt2/`；TMPDIR = 该目录下 `tmp/`。
- 本日志只记命令与结果；结论与缺陷见 `PROOF-NOTE.md`。

## §0 探针与 SHA

```
$ ls /dev/null
-rw-rw---- 1 root root 0 ... /dev/null            # 存在（非常规字符设备，但 git 可用）
$ echo test | git -C ~/workspace/weekly-git hash-object -w --stdin
9daeafb9864cf43055ae93beb0afd6c7d144bfa4          # 通
$ echo "probe-proof-core-pt2 ..." > hidden_files/w47/probe-proof-core-pt2.txt   # 写成功
$ cd production/2026-w47/core-pt && sha256sum A-Lucerna-VOL4.pdf A-Lucerna-VOL4-web.pdf 2026-w47-pt-zh-cn.text.md
4b58f4dfec2245f77dbb57b53c58cbab4913fdc85e4cf8566d706d4d3ec141b6  A-Lucerna-VOL4.pdf        (25,312,258 B) ✓ 与任务一致
9f2d70e5404a964d303182faae69b4884e46dbcc168a632323fb2bff61a2a7b5  A-Lucerna-VOL4-web.pdf    (1,609,033 B)  ✓
3cd3793f198a40d8c4b895275bbce9c6593168eeb93ae2e7fea7ce0e7f4fbce2  2026-w47-pt-zh-cn.text.md (36,882 B)    ✓
$ git show d2b0e182 --stat
2026-w47-pt-zh-cn.text.md | 2 +- ; WEEKLY-KIT.md | 15 ++++ ; content34.py | 2 +-   # 仅 3 文件
$ git show d2b0e182 -- .../content34.py .../2026-w47-pt-zh-cn.text.md
仅第 134 行 / 第 215 行：`o título 冠军` -> `o título 冠军头衔`（余文案不动）
$ python -c regex: content34.py 与 text.md 中裸 `o título 冠军(?!头衔)` 各 0 处，全形各 1 处
$ git log --oneline -3 -- production/2026-w47/core-pt/  -> 最新为 d2b0e182；d2b0e182 为 HEAD 祖先
$ git status --porcelain <core-pt 三跟踪文件>  -> 空（相对 fix2 提交干净）
```

## §1 gates_core.py — 16/16 PASS

```
$ tools/venv/bin/python gates_core.py   (cwd: production/2026-w47/core-pt)
> gates.log
[PASS] P1 VOL.4 + week dates :: top strip
[PASS] P1 subtitle topics :: subtitle line
[PASS] footer+page line 8/8 :: VOL.4 ZH footer + page line on all pages
[PASS] no VOL.3 edition label residue :: VOL.3 may appear only as the cited promising issue in the P7 disclosure
[PASS] press-time note + final named :: P4 press-time note present; final date named
[PASS] P1 masthead lines fit 1820 :: {330: 319.2, 372: 682.7}
[PASS] same-baseline ink collisions = 0 :: 0 collisions
[PASS] page-frame ink crossings = 0 :: 0 crossings | min margins L/R/T/B = [47.0, 47.9, 35.0, 33.0]
[PASS] P6 chart-label coverage <30% :: [('dias úteis', 0.0), ('10 dias', 0.0), ('fins de semana e feriado', 0.0), ('5 dias', 0.0)]
[PASS] gloss items enumerated :: {2: 6, 3: 6, 4: 6, 5: 6, 6: 5} total 29
[PASS] gloss headwords survive in render :: 0 missing
[PASS] P7 quotes 2x + page tag + ZH on P7 :: 8 quotes; all (2, True, True)
[PASS] readers corner disclosure :: PT/ZH verbatim True, ZH example label True, VOL.5 carry True
[PASS] images embedded + credits 5/5
[PASS] P7 quotes clear of preview box :: max quote-region baseline 2373.17
[PASS] P1 headline <= 56 non-space chars :: 41 chars
FAILURES: none
```

## §2 occlusion audit — 0 flags

```
$ tools/venv/bin/python tools/occlusion_audit.py <core>/svg --json <scratch>/occlusion.json
selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent
<core>/svg: 0 flags
occlusion.json: {"flag_count": 0, "flags": []}
```
注：审计对“文本溢出自盒底 / 盒题横向溢出”有盲区——相关项以 §4 的 PIL 真墨为准，不以此门代证。

## §3 creambox.py 全版扫描 — 31 盒，0 真溢出

```
$ md5sum hidden_files/w47/tools/creambox.py
ee7a55d8b2057cf4ad42a97bb1197383      # 正典，与 proof1 核对一致；未用窄带 creambox_check.py 作证据
$ tools/venv/bin/python hidden_files/w47/tools/creambox.py <core>/svg/*.svg > creambox-all.log
rc=0；31 盒（inside-only 口径）
```
逐盒裁定（BELOW-WINDOW 6 处全为已知假阳性类；desc-clear 负值 6 处全为中文/数字末行）：

| 页 | 盒 | inside-only | BELOW-WINDOW | 裁定 |
|---|---|---|---|---|
| P1 | y=786 | +45.0 | +37.0 `AGORA VOCÊ 即学即练`（下块标题） | 假阳性 |
| P1 | y=588 | +51.0 | — | 通过 |
| P1 | y=1238 | +16.0 / desc +9.7 | — | 通过 |
| P1 | y=1874 **D1** | **+20.4 / desc +14.4**，末行基线 2327.6 | +38.0 quiz 标题行（下块） | 假阳性；盒内通过（另见 §4 真墨 +16） |
| P2 | y=605 | +48.1 | — | 通过 |
| P2 | y=858 | +47.7 | — | 通过 |
| P2 | y=200 | +11.4 / desc +4.9 | — | 通过 |
| P2 | y=545 | +4.4 / desc −1.6（末行中文，无降部） | — | 假阳性（§4 真墨 +4.0） |
| P2 | y=1618 ×4 | +60.8 / +31.5 | +32.0 `Atenção: …`（盒下独立段落） | 假阳性（2× 裁切目视：段落位于盒下白纸上，见 crop-p2-atencao.png） |
| P3 | y=200 | +47.7 | +37.0 `UM DIA, DOIS SENTIDOS`（下块标题） | 假阳性 |
| P3 | y=200 **D2** | **+10.4 / desc +3.9**，末行 `16h30.` 基线 540.6 | — | 通过（另见 §4 真墨 +11） |
| P3 | y=577 | +4.5 / desc −1.5（末行中文） | — | 假阳性（§4 真墨 +4.0） |
| P3 | y=877 | +19.4 | — | 通过 |
| P4 | y=270 **D5** | **+47.7 / desc +41.6**，末行基线 368.4，末行 `军头衔 · a pausa 休整期 · a taça 奖杯。` | — | 通过（另见 §4 真墨 +43.1） |
| P4 | y=200 | +110.8 | — | 通过 |
| P4 | y=602 | +4.5 / desc −1.5（末行中文） | — | 假阳性（§4 真墨 +4.0） |
| P5 | y=200 | +46.6 | — | 通过 |
| P5 | y=777 | +47.7 | — | 通过 |
| P5 | y=200 | +5.4 / desc −1.1（末行 `2027.`，数字无降部） | — | 假阳性（§4 真墨 +6.0） |
| P5 | y=539 | +4.5 / desc −1.5（末行中文） | — | 假阳性（§4 真墨 +3.5） |
| P6 | y=343 | +47.7 | — | 通过 |
| P6 | y=200 **D3** | **+13.2 / desc +6.9**，末行 `Página do Participante.` 基线 840.8 | — | 通过（另见 §4 真墨 +9） |
| P6 | y=866 | +19.4 | — | 通过 |
| P6 | y=1594 ×2 | +40.0 / +62.0 | +42.0 `EXERCÍCIOS 第6版练习`（下块标题） | 假阳性 |
| P7 | y=200 工具盒 | +26.7 | — | 通过 |
| P7 | y=1098 工具盒 | +4.5 / desc −1.5（末行中文） | — | 假阳性（§4 真墨 +3.5） |
| P7 | y=1394 工具盒 | +22.6 | — | 通过 |
| P8 | — | 0 盒 | — | — |

P7-TOOLBOX 汇总：3 盒，最小盒内 clearance +4.5，最小 desc-clear −1.5（即上表中文末行，假阳性）。

## §4 PIL 真墨复测（自写 pil_re2.py；PNG 为本人 cairosvg 自 SVG 重渲染，1950×2700，逐字节 = repo cards/；墨 = 灰度均值 <180）

```
D1 rows 2280-2360: [[2283, 2303], [2312, 2332], [2349, 2350]]
D1: box bottom=2348 last ink row=2332 ink clearance=+16px PASS >=+5   (fix2 称 +17：1px 方法差，与 proof1 +16 一致)
D2 rows 500-575 (x 1439-1862): [[500, 514], [526, 540]]   (552-570 无墨)
D2: box bottom=551 last ink row=540 ink clearance=+11px PASS >=+5
D3 rows 790-880 (x 1439-1862): [[796, 811], [825, 845]]   (855-875 无墨)
D3: box bottom=854 last ink row=845 ink clearance=+9px PASS >=+5
D7 model lines found: 10
  673.9 ink-right=1797 +65px | 693.4 ink-right=1814 +48px | 712.9 ink-right=1840 +22px
  732.4 ink-right=1797 +65px | 751.9 ink-right=1838 +24px | 771.4 ink-right=1801 +61px
  790.9 ink-right=1778 +84px | 810.4 ink-right=1838 +24px | 829.9 ink-right=1839 +23px
  849.4 ink-right=1723 +139px
  model words counted from SVG lines: 90 (= 88 + 'Texto modelo:' ×2 tokens)
D5 gloss box (rect x989 y270.48 w422.5 h145.675 -> right 1411.5 bottom 416.15):
  gloss lines found: 3 (y 308.98 / 338.71 / 368.43)
  ink row runs in box: [(291, 313), (321, 339), (351, 373)]
  last ink row=373 -> vertical clearance +43.1px (fix2 称 372/+44.2：1px 方法差)
  line ink-right: 1382 (+29.5) / 1384 (+27.5) / 1388 (+23.5 to box right)
  PIL widths (svglib.text_w, sans 20.5): line1 367.7 (+18.8) / line2 370.7 (+15.8) / line3 383.4 (+3.1 vs inner 386.5)
all-cream-box sweep (31 rects, last ink row inside box vs bottom): 全部 OK，最小 clearance +3.5px
  细节：P1 +44.2/+47.4/+12.4/+16.0；P2 +49.0/+43.4/+12.0/+4.0/+60.0/+31.0/+60.0/+60.0；
  P3 +46.4/+11.0/+4.0/+20.0；P4 +43.2/+109.0/+4.0；P5 +45.3/+44.0/+6.0/+3.5；
  P6 +47.1/+9.0/+15.0/+37.0/+59.0；P7 +25.5/+3.5/+21.5
```
D1 备注：2349–2350 两行墨为盒下 quiz 分隔线（qy=2350），在框底 2348 之下，不计入盒内墨底；裁切目视确认线在盒外。
2× 裁切目视（`crop-d1/d2/d3/d5/d7.png` + `crop-p2-atencao.png`）：D1/D2/D3/D7 均与 PIL 数值一致；D5 末行在盒内、盒底奶油余量大；P2 `Atenção:` 段落位于 4 日盒之下白纸上，非溢出。

## §5 p8 / freeze / 独立重渲染

```
$ tools/venv/bin/python tools/p8.py extract --p8 <core>/svg/p8-avaliacao.svg --total 150
noted set = 150 of 150 (parse: lines)
$ tools/venv/bin/python tools/p8.py compare --core-dir <core> --edition-dir <core> --target pt --total 150
core 150 noted / edition 150 noted — status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[]
$ tools/venv/bin/python tools/freeze.py baseline --build <core> --core-svg <core>/svg --out <scratch>/freeze
runtime: .../tools/venv/bin/python | Pillow 13.0.0 | FreeType 2.14.3
baseline: 8/8 SVGs byte-identical (repointed files: none)
  OK p1..p8（core == produced，逐文件 sha 一致）；core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)
$ tools/venv/bin/python tools/freeze.py diff --core-svg <core>/svg --edition-svg <core>/svg
p1..p8: +0/-0；TOTAL added CJK characters: 0
$ 本人 cairosvg 重渲染 SVG -> <scratch>/cards/*.png (1950×2700)
8 张全部与 repo cards/ 逐字节相同（cmp IDENTICAL ×8）
```

## §6 印/网文字层 + 字号 + 弯引号 + ABSTRACT

```
$ pdfinfo 两版：Pages 8；Page size 1462.5 x 2025 pts
$ pdftotext -layout A-Lucerna-VOL4.pdf print-all.txt; pdftotext -layout A-Lucerna-VOL4-web.pdf web-all.txt
print-all 104920 B / web-all 104920 B；cmp IDENTICAL；words 各 7262
$ pdftotext A-Lucerna-VOL4.pdf print-raw.txt; pdftotext A-Lucerna-VOL4-web.pdf web-raw.txt
print-raw 44487 B / web-raw 44487 B；cmp IDENTICAL；words 各 7263
$ word multiset diff: 0 / 0（双向）
$ 弯引号（印/网一致）：U+201C 3，U+201D 3，U+2019 0，« 40，» 40
$ fitz spans: 印/网 min font 均为 10.12pt；P8 min 10.12pt；≥ SOP §1.1 下限 9.75pt ✓
$ ABSTRACT.txt (524 B)：首句 "A Lucerna 葡萄牙语周报 VOL.4：…" 含 masthead ✓（SOP §9）
注：layout 字节数较 proof1 的 104,916 变为 104,920（+4 B）：gloss 多“头衔”二字后的 layout 换行空格变化；印/网彼此逐字节相同。
```

## §7 keycheck — 印 PDF RESPOSTAS-only vs text.md Respostas（自写 keycheck2.py）

```
$ pdftotext -f 8 -l 8 -raw A-Lucerna-VOL4.pdf print-p8-raw.txt
$ tools/venv/bin/python keycheck2.py   (顺序解析 1→150；答案取标记本行至首个 ' —' 之前)
md parsed: 150 keys 1..150 all present: True
pdf parsed: 150 keys 1..150 all present: True
common: 150; diffs: 0; only in md: []; only in print: []
抽查：Q134 'O Grêmio empatou por 1 a 1.' 两侧一致（幽灵键已排除）；Q140 全句一致；Q150 '✓ 范文见本版 H 区（88 词）'一致；
Q44/45/46 造句句一致；Q120 'B'、Q125 'A'、Q30 'A' 一致。
解析器说明：初版以 ' — '（两侧空格）切答案，在 Q30（' —帕尔马雷斯…'无后空格）处越过标记 31 而断言失败；
终版改取“标记所在整行、首个 ' —' 之前”为答案，覆盖两种分隔写法。md 侧同时处理了每页首项前的 '**Página N** — ' 前缀。
```

## §8 150 键手验（逐题语义，非仅 compare；本人通读 text.md 全文 534 行后逐题核对）

- P1（1–10）：1 consciência · 2 feriado · 3 sexta · 4 três · 5 6 · 6 decidem · 7 B · 8 B · 9 C · 10 B — 全对。
- P2（11–28）：11–15 B×5 · 16 cai · 17 dura · 18 descansamos · 19 abrem · 20 aproveita · 21 3 · 22 1695 · 23 2023 · 24 27 · 25 a · 26 b · 27 c · 28 d — 全对。
- P3（29–46）：29 C · 30 A · 31 B · 32 B · 33 A · 34 quilombo · 35 resistência · 36 escravizados · 37 líder · 38 memória · 39 combate · 40 morreu · 41 nasceu · 42 defendeu · 43 formaram · 44–46 造句句合法 — 全对。
- P4（47–64）：47 A · 48 B · 49 B · 50 B · 51 A · 52 b · 53 a · 54 d · 55 c · 56–58 mais · 59 menos · 60 empatou · 61 venceu · 62 abriu · 63 garantiu · 64 foram — 全对。
- P5（65–82）：65 B · 66 B · 67 A · 68 B · 69 B · 70 gabarito · 71 oficial · 72 extraoficiais · 73 espera · 74 nota · 75 pesa · 76 sairá · 77 publicarão · 78 decidirá · 79 chegará · 80 Verdadeiro · 81 Falso · 82 Verdadeiro — 全对。
- P6（83–100）：83 B · 84 A · 85 B · 86 B · 87 B · 88 A · 89 B · 90 B · 91 B · 92 B · 93 serão · 94 contam · 95 fixa · 96 pesa · 97 prazo · 98 dia útil · 99 coerência · 100 chute — 全对；83–86 算术：16–30 日共 15 天 = 10 工作日 + 5 休息日。
- P7（101–112）：101 em · 102 numa · 103 é · 104 B（aproveitamos）· 105 empatou · 106 venceu · 107 abriu · 108 B（saíram）· 109 sair · 110 for · 111 tiver · 112 B（sair）— 全对。
- P8（113–150）：113 A · 114 A · 115 B · 116 A · 117 B · 118 A · 119 A · 120 B（5 小时）· 121 B · 122 A · 123 B · 124 B · 125 A（周六 21，36 轮）· 126 B · 127 A · 128 A · 129 B · 130 B · 131 A · 132 B · 133–136 造句 · 137–140 翻译 · 141 c · 142 d · 143 b · 144 a · 145–149 A · 150 ✓ 范文（88 词，本人逐词数过，含 `×` 计 88；SVG 行计 90 词 = 88 + `Texto modelo:` 2 词）— 全对。
- 本周金句 8 条逐字核对均出自本期正文（P1×2、P3×2、P4、P5、P6、P2 各 1 条定位正确）。

## §9 外部事实抽查（本轮新检索 2 组 + 自算；其余组与 proof1 2026-11-11 验证一致，内容未变）

- Copa：决赛 Palmeiras × Grêmio，12 月 6 日周日，Mané Garrincha，单场首届；Grêmio 第 10 次决赛冲第 6 冠，Palmeiras 冲第 5 冠；半决赛比分/总比分/点球（Grêmio 1–1 Atlético-MG 首回合 2–0 总 3–1；Vasco 2–1 Palmeiras 首回合 1–0 总 2–2，点球 5–4）与正文一致（bolavip、sportytrader、portaldopalestra、foot-analytics）。
- Enem：Edital 64/2026（DOU 原文 item 15.1：gabarito 至 10º dia útil após 2º dia）；第二天 11 月 15 日周日 13h30–18h30，Natureza + Matemática 各 45 题；27–30 日窗口与公开计法分歧一致；个人成绩 2027 年 1 月；TRI（ulti、sisu.pro.br、cursosdoportal、in.gov.br）。
- 日历骨架：`TZ=America/Sao_Paulo date -d` 核 13 个日期星期全符；自算 10º dia útil = 11 月 30 日（16 日起计，扣 20 日假日与两周末）；16–30 日 = 15 天 = 10 + 5。

## §10 读者面内部语扫描

```
$ grep -in "SOP|proofread|cover|TODO|placeholder|lint|FIXME" print-all.txt
7 行命中，全为葡语词 todo(s)（“全部”）含子串 "todo" 的误报；真实内部标记 0 处。
$ grep -c "VOL.3" print-all.txt  -> 2（均在 P7 读者来信说明内，门禁逐字核对过，允许）
```

## §11 D5 传播核查（本轮不核，范围外）

pt-ko O1 字体漂移另案处理；D5 的 9 版 fan-out 一词修正属 fan-out 修复，不在本轮核。核心 gloss 源头已消歧（见 §0）。
