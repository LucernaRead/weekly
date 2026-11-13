# LOG — W47 ru-ko production `svg/` refresh (post-fix build SVGs)

Date: 2026-11-12 (UTC, ~02:45–02:47). Worker: ru-ko svg refresh (follow-up to
the ru-ko port+rebuild+sync, `scratch-ru-ko-port-rebuild/PORT-REBUILD-SYNC-LOG.md`).
Scope: **ru-ko ONLY**. No commit / push / lint / other edition. Nothing else touched.

## 0. Sources

- Source SVGs (freeze-verified build1):
  `hidden_files/w47/scratch-ru-ko-port-rebuild/ru-ko/build1/build-copy/svg/`
  — 8 files, p1-pervaya.svg … p8-test.svg.
- Destination: `~/workspace/weekly-git/production/2026-w47/2026-w47-ru-ko/svg/`
  (overwrite in place; PDFs, text.md, KIT, svglib.py untouched).
- Disk at start: **99G used / 51G free** (150G volume) — below the 100G stop
  line the whole run; the stop line was never crossed.

## 1. Copy — 8/8 verified by sha256

BEFORE (production `svg/`, pre-fix build; file `before-prod-svg-sha.txt`):

| File | sha256 (before) |
|---|---|
| p1-pervaya.svg | `739fd1e9237d753c738b7da87476e81b4f13ca8c8d424aef3d1a0873989fc946` |
| p2-zhizn.svg | `8cea636d1dc4ce12a3360b7a193dbf9335015856a786f2b1e4d3efa80f1fd713` |
| p3-kultura.svg | `14169503011c09065f384102f29b417de4a381be4f16eafe7d0408ba13ab2e91` |
| p4-sport.svg | `5f7b29992026da9f04957cb293daaede1d26a7d8987c3069db25c16d337abc5c` |
| p5-molodezh.svg | `c54640eb44a7cc4575c31990e5d76577ed985cd29a56321e3baee368eda77833` |
| p6-razbor.svg | `a0ca511b111d369261e346ed0fc0d738236233090b487c152625d667e3086824` |
| p7-yazyk.svg | `13d5371b80693814c32f09b006f1d7b700fd69a127329f4e66d26225060d0979` |
| p8-test.svg | `72cdd704cf7f9abfdaaf68eab680aafbb7239506786dc0d2cc198e9033404c25` |

AFTER (production `svg/` = build1 source, 8/8 MATCH; file `after-prod-svg-sha.txt`):

| File | sha256 (after = source) |
|---|---|
| p1-pervaya.svg | `a19a4cd7ad05118fb9c1fa6ee8a707ce5cf537322a2822505771755244cdaed2` |
| p2-zhizn.svg | `d03b09ec18591fa923b5714fbc413ec9bf04c0149f667eceb262a302531b0705` |
| p3-kultura.svg | `e9c1a7844a58db162390a912aa4a18f7a087bb87f4223bf535b9f1bf638ca0dd` |
| p4-sport.svg | `c215895687a3edaf420054d398c20337ab205e2e0ea1f3a423e1b3e494f8654c` |
| p5-molodezh.svg | `044d1231f54ba0c171be98b1ad34cc43886ee5379b8c507720a0ec8527ae07cd` |
| p6-razbor.svg | `7111c5e00d703ef042c564e22ce3f94c740a503c5e303eb40501b4c9315aa1ff` |
| p7-yazyk.svg | `ad32551e66e38e9eb6f8d8327eae185fb74116f9c9aa35622f7ad0a401a8eb00` |
| p8-test.svg | `9e33aab4421945ccc54778db8752032c0f657a9fcf97206955715b255180ecd3` |

- `cp` rc=0; per-file compare source vs production after copy: **MATCH 8/8**.
- p1 hash changed `739fd1e9…` → `a19a4cd7…` — the stale pre-fix hash is gone.

## 2. Freeze baseline (correct method, from repo root)

Command (run 02:46 UTC, `~/workspace/weekly-git`):

```
tools/venv/bin/python tools/freeze.py baseline \
  --build production/2026-w47/2026-w47-ru-ko \
  --core-svg production/2026-w47/2026-w47-ru-ko/svg \
  --out <this dir>/freeze-ru-ko \
  --json <this dir>/freeze-result.json
```

- **rc=0. Baseline: 8/8 SVGs byte-identical** (repointed files: none).
- Per page: p1 `a19a4cd7…`, p2 `d03b09ec…`, p3 `e9c1a784…`, p4 `c2158956…`,
  p5 `044d1231…`, p6 `7111c5e0…`, p7 `ad32551e…`, p8 `9e33aab4…` — core ==
  produced on all 8.
- Tool's own integrity line: "shipped core SVGs unchanged by the run (8 files
  re-hashed)"; re-hash after the run confirms production `svg/` unchanged by
  freeze (`after-freeze-prod-svg-sha.txt` diff vs after-copy = identical).
- Runtime: venv python, Pillow 13.0.0, FreeType 2.14.3.
- No "freeze print PDF == synced" check is claimed: freeze.py baseline runs
  run.py only, never render.py, so such a check is void by construction.
  PDF reproducibility evidence remains the port worker's two independent
  builds with byte-identical print PDFs (§2a of the port log).
- The 41 MB `freeze-ru-ko/build-copy/` was deleted immediately after the
  check; `freeze-ru-ko.log` + `freeze-result.json` kept; `freeze-ru-ko/svg/`
  left as an empty placeholder dir.

## 3. Production files untouched — re-hashed AFTER all work

| File | sha256 / md5 (after) | Size | mtime |
|---|---|---|---|
| `Lucerna-VOL4-ru-ko.pdf` (print) | `62538d215e2ef0cbe440faa23cb4e147dc78e9116e1b6db02fc07ca704635b27` | 22,005,230 B | Nov 12 02:41 |
| `Lucerna-VOL4-ru-ko-web.pdf` (web) | `e996c1f3826b6606c88b3ed05143de8299faaaba9f3e7a736f6cc4170ff6f350` | 3,510,669 B | Nov 12 02:41 |
| `2026-w47-ru-ko.text.md` | `5e9bd67201fd232aff598e0bbb487ba45821878e533392bc6e749444b090bffe` | 65,012 B | Nov 11 18:47 |
| `svglib.py` (md5) | `27f11789af7c828e47ca14eb00c1dded` | 24,488 B | Nov 12 02:23 |
| `WEEKLY-KIT.md` | (not edited; mtime Nov 12 02:42 from the port worker) | 24,994 B | Nov 12 02:42 |

All four SHAs match the port worker's synced values exactly (print
`62538d21…`, web `e996c1f3…`, text.md `5e9bd672…`, svglib md5 `27f11789…`).
Only the 8 `svg/` files changed in production.

## 4. Disk

- Before: 99G used / 51G free. After copy: 99G / 51G. After freeze run: 99G.
  After deleting the 41 MB freeze build-copy: **99G used / 51G free**.
  The 100G stop line was never approached.

## 5. Files in this scratch dir

- `LOG.md` (this file), `before-prod-svg-sha.txt`,
  `source-build1-svg-sha.txt`, `after-prod-svg-sha.txt`,
  `after-freeze-prod-svg-sha.txt`, `freeze-ru-ko.log`, `freeze-result.json`,
  `freeze-ru-ko/` (empty `svg/` placeholder only; build-copy deleted).
