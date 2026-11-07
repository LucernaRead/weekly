# COVER-KIT — W43 Weekly Cover for Simplified Chinese Readers

- Edition: `cover-w43-zh-cn` — week of 2026年10月19日至25日 (W43, October 19–25, 2026)
- Reader language: SIMPLIFIED CHINESE (zh-cn). All cover-original writing
  (title, intro, labels, explanations, footers) is natively written in
  Simplified Chinese — never converted from a Traditional version.
- Masthead: `Lucerna` with NO article (tables.json zh-cn entry: article
  null — Chinese takes no article). The cover itself carries NO VOL
  number; it is marked COVER (visible COVER badge on P1, COVER in every
  page footer).
- Format: 8 pages, 1950×2700, weekly visual system — warm ivory #f7f1e2,
  deep olive accents (#3e4c2a), serif headlines.
- Build dir: `hidden_files/cover-w43-zh-cn-build/` (`build.py` + `svg/` + `png/`).
- This dir: `svg/` (the 8 shipped SVGs) + `cover-w43-zh-cn.pdf` (text-layer
  web PDF built with `tools/webpdf.py`).

## Spec

SOP 附则五 (weekly-report-SOP.md, 2026-10-28): a weekly cover aggregates
the week's 12 core papers' P1 main headlines — one per target language —
with the headline and opening excerpt verbatim in the original language
and a 1–2 sentence explanation in the cover reader's language. The cover
is a website entry point, not a 131st regular edition; it is not entered
in the issues/ lint tree or index.json.

## The 12 sources (fixed order, verbatim from cover-backfill/headlines-w43.json)

The JSON was cross-checked against headlines-w43.md: all 12 headlines and
excerpts match character-for-character. No discrepancy with the source
cores was found, so nothing was silently fixed. VOLs below are the cores'
own VOLs (FR VOL.2, all others VOL.1), shown only on P8.

| # | Lang | Core dir | Masthead | VOL | Headline (verbatim) |
|---|------|----------|----------|-----|---------------------|
| 01 | en | weekly-report-en-vol1 | The Lucerna | VOL.1 | First Votes, First Games : America's Biggest Week of the Autumn |
| 02 | de | weekly-report-de-vol1 | Die Lucerna | VOL.1 | Eine Stunde geschenkt: Deutschland stellt die Uhren zurück — und elf Länder haben Ferien |
| 03 | fr | weekly-report-vol4 | Le Lucerna | VOL.2 | Présidentielle 2027 : les Français regardent déjà les sondages |
| 04 | es | weekly-report-es-vol1 | La Lucerna | VOL.1 | Este domingo: dormimos una hora más… ¡y se juega el Clásico! |
| 05 | it | weekly-report-it-vol1 | La Lucerna | VOL.1 | Un'ora in più di sonno: domenica torna l'ora solare |
| 06 | pt | weekly-report-pt-vol1 | A Lucerna | VOL.1 | Domingo é dia de decisão: o Brasil volta às urnas |
| 07 | nl | weekly-report-nl-vol1 | De Lucerna | VOL.1 | Een volle week: vakantie, design, dance — en een uur extra slaap |
| 08 | ru | weekly-report-ru-vol1 | Lucerna | VOL.1 | Первый снег — уже на этой неделе! |
| 09 | ja | weekly-report-ja-vol1 | Lucerna | VOL.1 | 土よう日、日本シリーズが始まる！ |
| 10 | ko | weekly-report-ko-vol1 | Lucerna | VOL.1 | 태풍 참피가 오고 있어요 |
| 11 | zh-cn | weekly-report-zhcn-vol1 | Lucerna | VOL.1 | 双11到了「付尾款」的这一周 |
| 12 | zh-tw | weekly-report-zhtw-vol1 | Lucerna | VOL.1 | 強颱薔琵壓境！週五、週六風雨最大 |

Excerpts are each item's P1 article-opening sentences (≤4 sentences),
verbatim from the same JSON file. The zh-tw item's headline and excerpt
stay in TRADITIONAL Chinese exactly as given; its explanation below is
written in Simplified Chinese (it is this cover's own writing for
Simplified readers).

## Layout (8 pages, binding)

- P1: masthead `Lucerna` + COVER badge + week label
  (2026年10月19日至25日) + cover title `一周十二条头条` + framing intro
  (generic framing only, no new facts: 十二份报纸，十二种语言，同一周。
  每条头条都以原文原样登载，内页附上原文摘录和简体中文讲解。)
  + 12 headline teasers in fixed order (source-language label in
  Simplified Chinese + verbatim headline, smaller type; two columns of 6).
- P2–P7: the 12 items in full, 2 per page, fixed order — P2: EN, DE.
  P3: FR, ES. P4: IT, PT. P5: NL, RU. P6: JA, KO. P7: zh-cn, zh-tw.
  Each item: source-language tag + core masthead, verbatim headline,
  verbatim excerpt, then a `简体中文讲解` box with a 1–2 sentence
  explanation in Simplified Chinese.
- P8: the week's 12 core papers at a glance, in fixed order: per core,
  masthead + VOL + verbatim headline (same extracted material only,
  nothing invented).

## Explanations (Simplified Chinese; every claim traceable to that item's headline + excerpt only)

- en: 美国大选日定在11月3日，但多州的投票已经开始：得克萨斯州以及阿拉斯加、阿肯色、康涅狄格和科罗拉多州10月19日星期一起开放提前投票。
- de: 德国将在周六夜间至周日凌晨结束夏令时，凌晨3点钟表拨回2点，多出一个小时；同时有十一个州正在放假。
- fr: 2027年法国总统大选虽然还没到，但法国人已经开始关注：本周法国谷歌搜索第一名就是“2027年总统大选民调”，每天有成千上万人搜索这些词。
- es: 本周日凌晨西班牙将调表：3点钟表拨回2点，夜晚长达25小时，可以多睡一小时；同一天还有国家德比。(Clásico glossed as 国家德比.)
- it: 意大利将在10月24日星期六夜间至25日星期日调表，凌晨3点钟表拨回2点，夜晚多出一小时；在七个月的夏令时之后，冬令时回来了。
- pt: 巴西人将在10月25日星期日、巴西利亚时间上午8点至下午5点再次投票，参加总统选举第二轮，对决双方是卢拉和弗拉维奥·博索纳罗。
- nl: 这是荷兰内容满满的一周：中部和南部地区整个星期都在放秋假，从10月17日星期六到25日星期日；北部地区上周已经放假，星期一重新开学。
- ru: 初雪可能就在本周降临：预报说第一片雪花可能出现在10月21日至23日的星期三到星期五，气温在零度左右。
- ja: 日本系列赛第一场将于10月24日星期六18点30分在横滨体育场举行，对阵双方是横滨DeNA海湾之星和福冈软银鹰，两队上次交手是两年前。
- ko: 第30号台风“灿比”正在北上，名字由老挝提供，意思是花的名字；气象厅21日早上说，它是非常强的台风。(참피 name glossed as 灿比.)
- zh-cn: 今年的双11来得早：京东10月12日晚上8点开始卖现货，10月20日晚上8点还有“开门红”；淘宝和天猫10月15日晚上8点开始预售，本周正是“付尾款”的一周。
- zh-tw: 强台风正向台湾东侧海面移动，预计周五、周六风雨最大；台风外围环流加上东北季风的“共伴效应”，会让雨下得更大、更久。(Headline/excerpt stay Traditional verbatim; this explanation is Simplified.)

## Build notes

- Builder: `hidden_files/cover-w43-zh-cn-build/build.py` — self-contained.
  Layout scaffolding follows the proven sibling cover builds; text
  measurement follows the Simplified Chinese core build
  (`weekly-report-zhcn-build/svglib.py`, HYBRID variant): PIL-measured
  greedy wrap (Latin/Cyrillic words whole, CJK per character), Noto CJK
  TTC faces JP=0 / KR=1 / SC=2 / TC=3 per tables.json. No content module
  from any core build dir was imported (module-level code in core dirs
  writes into the core's files dir); all code was copied into the cover
  build dir.
- NO punctuation rewriting was applied to anything: this cover's own
  Chinese text already uses full-width punctuation natively, so verbatim
  headlines/excerpts are measured and rendered byte-for-byte as loaded.
- Kinsoku post-processing (copied from the zh-cn core svglib: lines must
  not start with closing punctuation or end with opening punctuation)
  runs on every wrapped paragraph, and the build asserts every final
  line width ≤ max_w after kinsoku (wrap uses a 70-unit slack so a
  pulled-down character cannot overflow). Build asserts also cap every
  P1 teaser, every P2–P7 block, and P8 within the footer rule (y ≤ 2540).
- Fonts per item: source-language serif face (ja → JP, ko → KR,
  zh-tw → TC, all others → SC); the cover's own Chinese text uses the
  SC face throughout.

## Verification outputs

- Build asserts: all passed (P1 teasers end y=2051.9; P2–P7 blocks end
  y=1424–2044; P8 ends y=2010.5; all ≤ 2540).
- Visual eyeball of all 8 rendered PNGs (CairoSVG, 975×1350): no
  overflow, no cut-off text, no tofu/missing glyphs, no overlapping
  elements. All 12 scripts render: Latin, Cyrillic, Japanese, Korean,
  Simplified + Traditional Chinese. P7 checked specifically: zh-cn
  headline/excerpt in Simplified verbatim, zh-tw headline/excerpt in
  Traditional verbatim, zh-tw explanation in Simplified.
- Verbatim check (programmatic): concatenating all SVG `<text>` runs
  contains every one of the 12 headlines and 12 excerpts
  character-for-character (whitespace-insensitive join across wrapped
  lines). PASS 12/12 + 12/12.
- Own-writing script check: no Traditional-only characters in the
  explanation block of build.py. PASS.
- Occlusion audit: `tools/venv/bin/python tools/occlusion_audit.py
  <build svg dir>` → selftest OK (all six planted classes fired, clean
  controls silent); result: **0 flags — CLEAN**.
- Final PDF (`tools/venv/bin/python tools/webpdf.py <build svg dir>
  <out.pdf>`, exit 0): `cover-w43-zh-cn.pdf`, 8 pages, 573,828 bytes
  (< 7 MB target), 9,292 text bytes via pdftotext (non-empty text layer
  confirmed). All 12 headlines extract from the PDF
  (whitespace-insensitive check vs headlines-w43.json): 12/12 PASS.
  SHA-256: 24f32b578358aec83c0caca0eb8dbf4f3f257a3946e527ecf9d13b1de66b2c3e
  Embedded subset fonts: LucernaNotoSansCJKSC (Regular/Bold),
  LucernaNotoSerifCJKJP/KR/SC/TC (Regular/Bold each); 525 distinct chars.

## Issues found + fixed

- None during the build: no JSON-vs-MD discrepancy, no overflow, no
  audit flags, no glyph problems. The only pre-existing condition noted:
  P1 and the vertically centred P2–P7 pages carry generous empty space
  below the content (same as the sibling cover builds' layout); this is
  the shared template's design, not a defect, and was left as-is.
- No gate failed at any point, so no fix-and-repeat cycle was needed.

## Fix record — independent proofread problem 1 (P2 DE item explanation, timing phrase)

- Scope: exactly one string changed, in the build source only
  (`hidden_files/cover-w43-zh-cn-build/build.py`, EXPL["de"], line 213).
  No headline, excerpt, or other explanation was touched. Storm names
  untouched: ko item 灿比 and zh-tw item 薔琵 exactly as before.
- OLD (exact):
  德国将在周日夜间结束夏令时，凌晨3点钟表拨回2点，多出一个小时；同时有十一个国家正在放假。
- NEW (exact):
  德国将在周六夜间至周日凌晨结束夏令时，凌晨3点钟表拨回2点，多出一个小时；同时有十一个国家正在放假。
- Reason: the DE excerpt says "In der Nacht von Samstag auf Sonntag
  endet die Sommerzeit" — the night from Saturday to Sunday, ending
  03:00 Sunday. "周日夜间" reads as Sunday night, a day late, and
  contradicts the explanation's own correct "凌晨3点".
- Rebuild: `build.py` regenerated the 8 build SVGs; all 8 copied to the
  edition `svg/` dir; PDF rebuilt ONLY via
  `tools/venv/bin/python tools/webpdf.py <edition-svg-dir> <edition-pdf-path>`
  (exit 0; webpdf: 8 pages, 525 distinct chars, 574,115 bytes, 9,295 text bytes).
- Re-verification (2026-10-28):
  1. OLD string: 0 occurrences in all 8 edition SVGs and 0 in the PDF
     text layer (whitespace-insensitive); NEW string: present 1× in
     p2-items.svg and 1× in the PDF text layer.
  2. Occlusion audit: `tools/venv/bin/python tools/occlusion_audit.py
     <edition-svg-dir>` → selftest OK, 0 flags, exit 0.
  3. PDF: 8 pages (pdfinfo), 574,115 bytes (< 7 MB), pdftotext
     9,295 bytes (non-empty), all 12 headlines extract from the PDF
     (whitespace-insensitive vs headlines-w43.json): 12/12.
     SHA-256: 6f1f5a8c1f375269e395a1f1a5aa0be48b32323b13e14d2344351493a9d1c16f
  4. No other page changed: edition SVGs compared byte-for-byte
     against the pre-fix set — p1, p3, p4, p5, p6, p7, p8 IDENTICAL;
     only p2-items.svg differs (new SHA-256:
     661647a550e34cd0f1befc1d9a49a9b53cec7c842874a6d8f450b521709e2e1c).
     Build log unchanged otherwise (P2 de block ends y=2044, as before).

## Fix record — independent proofread problem 2 (P2 DE item explanation, wrong entity: states, not countries)

- Scope: exactly one string changed, in the build source only
  (`hidden_files/cover-w43-zh-cn-build/build.py`, EXPL["de"], line 213).
  Only the clause "十一个国家正在放假" changed to "十一个州正在放假";
  the timing clause ("周六夜间至周日凌晨…", fixed in problem 1) was
  left untouched. No headline, excerpt, or other explanation was
  touched. Storm names untouched: ko item 灿比 and zh-tw item 薔琵
  exactly as before.
- OLD (exact):
  德国将在周六夜间至周日凌晨结束夏令时，凌晨3点钟表拨回2点，多出一个小时；同时有十一个国家正在放假。
- NEW (exact):
  德国将在周六夜间至周日凌晨结束夏令时，凌晨3点钟表拨回2点，多出一个小时；同时有十一个州正在放假。
- Reason: the DE core article itself says "Elf Bundesländer haben in
  dieser Woche gleichzeitig Herbstferien" (P1 continuation; P5 repeats
  "11 Bundesländer"), and the core's P8 Chinese answer key glosses it
  "11 个州同时放假". Bundesländer are German federal states; 国家
  (countries) is wrong.
- Rebuild: `build.py` regenerated the 8 build SVGs; all 8 copied to the
  edition `svg/` dir; PDF rebuilt ONLY via
  `tools/venv/bin/python tools/webpdf.py <edition-svg-dir> <edition-pdf-path>`
  (exit 0; webpdf: 8 pages, 525 distinct chars, 573,828 bytes, 9,292 text bytes).
- Re-verification (2026-10-28):
  1. OLD string: 0 occurrences in all 8 edition SVGs and 0 in the PDF
     text layer; NEW string: present 1× in p2-items.svg and 1× in the
     PDF text layer.
  2. Occlusion audit: `tools/venv/bin/python tools/occlusion_audit.py
     <edition-svg-dir>` → selftest OK, 0 flags, exit 0.
  3. PDF: 8 pages (pdfinfo), 573,828 bytes (< 7 MB), pdftotext
     9,292 bytes (non-empty), all 12 headlines extract from the PDF
     (whitespace-insensitive vs headlines-w43.json): 12/12.
     SHA-256: 24f32b578358aec83c0caca0eb8dbf4f3f257a3946e527ecf9d13b1de66b2c3e
  4. No other page changed: edition SVGs compared byte-for-byte
     against the pre-fix set — p1, p3, p4, p5, p6, p7, p8 IDENTICAL;
     only p2-items.svg differs (new SHA-256:
     7193f0f84b6a93a7e7bb310dedaa72eab826dab04cc8a3f28c9a708f6dc11cd2).
     Build log unchanged otherwise (P2 de block ends y=2044, as before).
